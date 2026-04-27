"""
api_server/loaders.py
=====================

横断索引化フェーズ B（cross_index_spec.md §13）の API サーバ起動時ロード基盤。

7 索引 + miyasaka.json + api_mappings.json をメモリにロードし、

  - 篇 idx → ヒットエントリ集合の逆引き辞書（per_idx）
  - alias / matched_form → canonical の逆引き辞書（alias_to_canonical）
  - 7 ペアの共起マトリックス（co_occurrence・§13.7.3）

を起動時に前計算してメモリ常駐させる。/api/篇/:idx と詳細参照系 6 本
（/api/term, /api/person, /api/place, /api/citation, /api/sanskrit,
/api/kukai-work）はすべてこのストアから O(1) 〜 O(N) 程度で組み立てる。

使い方:

    from api_server.loaders import IndexStore
    store = IndexStore.load_default()
    篇カルテ = store.build_篇_card(idx=1, excerpt_chars=300)
    term参照 = store.build_reference(endpoint="terms", key="三密")

cross_index_spec.md §13.5 / §13.6 / §13.7.3 / §13.8.2 に準拠。
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Set, Tuple

# --------------------------------------------------------------------------
# 索引種別 → ファイル名 + 主キー（仕様 §13.6 / §13.5）の定義
# --------------------------------------------------------------------------

INDEX_FILES: Dict[str, str] = {
    "terms":         "index_shoryoshu_terms.json",          # 密教教学用語 (Tier 1-1)
    "citations":     "index_shoryoshu_citations.json",      # 典故書名 (Tier 1-2)
    "sanskrit":      "index_shoryoshu_sanskrit.json",       # 梵語 IAST (Tier 2-4)
    "kaimyo_jukugo": "index_shoryoshu_kaimyo.json",         # 戒名向け熟語 (Tier 2-3)
    "persons":       "index_shoryoshu_persons.json",        # 人名 (Tier 3-5)
    "places":        "index_shoryoshu_places.json",         # 地名 (Tier 3-6)
    "kukai_works":   "index_shoryoshu_kukai_works.json",    # 空海著作 (課題 D)
}

# 各索引で「主キー（エントリ識別子）」となるフィールド名
PRIMARY_KEY: Dict[str, str] = {
    "terms":         "term",
    "citations":     "term",
    "sanskrit":      "canonical",
    "kaimyo_jukugo": "jukugo",
    "persons":       "canonical",
    "places":        "canonical",
    "kukai_works":   "term",
}

# §13.7.3 で前計算する 7 ペア（無向）
CO_OCCURRENCE_PAIRS: List[Tuple[str, str]] = [
    ("kaimyo_jukugo", "persons"),
    ("kaimyo_jukugo", "places"),
    ("terms",         "persons"),
    ("terms",         "places"),
    ("kaimyo_jukugo", "terms"),
    ("persons",       "persons"),
    ("persons",       "places"),
]

# 参照系から呼ばれる「逆方向」ペア（前計算済みの転置で導出）
_REVERSE_PAIRS: List[Tuple[str, str]] = [
    ("persons",       "kaimyo_jukugo"),
    ("places",        "kaimyo_jukugo"),
    ("persons",       "terms"),
    ("places",        "terms"),
    ("terms",         "kaimyo_jukugo"),
    ("places",        "persons"),
]


# --------------------------------------------------------------------------
# データクラス
# --------------------------------------------------------------------------

@dataclass
class IndexEntry:
    """各索引エントリの薄いラッパ。元 JSON はそのまま raw に保持する。"""
    raw: Dict[str, Any]
    primary_key_field: str

    @property
    def name(self) -> str:
        return str(self.raw.get(self.primary_key_field, ""))

    @property
    def 篇分布(self) -> List[int]:
        return list(self.raw.get("篇分布", []))


@dataclass
class IndexStore:
    """
    起動時にロードした全索引・本文・マッピングを保持するインメモリストア。

    /api/篇/:idx は per_idx[name][idx] -> [(entry, occ_count), ...] を引き、
    /api/term/:term 等の参照系は entry_by_key + co_occurrence + alias_to_canonical
    を組み合わせて即時にレスポンスを組み立てる。
    """

    indices_raw: Dict[str, Dict[str, Any]]                 # name -> 索引 JSON 全体
    entries_by_index: Dict[str, List[IndexEntry]]          # name -> エントリ配列
    miyasaka: List[Dict[str, Any]]                          # 全 112 篇の本文
    api_mappings: Dict[str, Any]                            # CHARACTERISTIC_TO_ICHIJI 等

    # 篇 idx 別の逆引き：name -> idx -> [(entry, occ_count), ...]（occ_count 降順）
    per_idx: Dict[str, Dict[int, List[Tuple[IndexEntry, int]]]] = field(default_factory=dict)

    # primary key (canonical/term/jukugo) → IndexEntry
    entry_by_key: Dict[str, Dict[str, IndexEntry]] = field(default_factory=dict)

    # alias / matched_form → canonical（自身も自身を引ける形で含む）
    alias_to_canonical: Dict[str, Dict[str, str]] = field(default_factory=dict)

    # primary key → frozenset(篇分布) 高速 set 交差用
    entry_篇sets: Dict[str, Dict[str, frozenset]] = field(default_factory=dict)

    # 共起マトリックス（§13.7.3）：(a_name, b_name) -> a_key -> b_key -> count
    co_occurrence: Dict[Tuple[str, str], Dict[str, Dict[str, int]]] = field(default_factory=dict)

    schema_version: str = "1.4.0"

    # ------------------------------------------------------------------
    # ロード
    # ------------------------------------------------------------------

    @classmethod
    def load_default(cls, repo_root: Optional[Path] = None) -> "IndexStore":
        """リポジトリルートから既定パスでロードする。"""
        if repo_root is None:
            repo_root = Path(__file__).resolve().parent.parent
        return cls.load(
            mikkyou_dir=repo_root / "data" / "mikkyou",
            miyasaka_path=repo_root / "data" / "kukai" / "shoryoshu_miyasaka.json",
        )

    @classmethod
    def load(cls, mikkyou_dir: Path, miyasaka_path: Path) -> "IndexStore":
        # 1) 7 索引
        indices_raw: Dict[str, Dict[str, Any]] = {}
        entries_by_index: Dict[str, List[IndexEntry]] = {}
        for name, fn in INDEX_FILES.items():
            path = mikkyou_dir / fn
            with path.open(encoding="utf-8") as f:
                raw = json.load(f)
            indices_raw[name] = raw
            pk = PRIMARY_KEY[name]
            entries_by_index[name] = [IndexEntry(raw=e, primary_key_field=pk) for e in raw.get("entries", [])]

        # 2) miyasaka 全文
        with miyasaka_path.open(encoding="utf-8") as f:
            miyasaka = json.load(f)

        # 3) api_mappings.json（v1.4 で確定したマッピング 2 表）
        mappings_path = mikkyou_dir / "api_mappings.json"
        if mappings_path.exists():
            with mappings_path.open(encoding="utf-8") as f:
                api_mappings = json.load(f)
        else:
            api_mappings = {}

        store = cls(
            indices_raw=indices_raw,
            entries_by_index=entries_by_index,
            miyasaka=miyasaka,
            api_mappings=api_mappings,
        )
        store._build_per_idx()
        store._build_lookups()
        store._build_co_occurrence()
        return store

    # ------------------------------------------------------------------
    # 篇 idx → エントリ集合の逆引き辞書を構築
    # ------------------------------------------------------------------

    def _build_per_idx(self) -> None:
        """各索引の occurrences を走査し、name -> idx -> [(entry, count), ...] を構築。"""
        per: Dict[str, Dict[int, List[Tuple[IndexEntry, int]]]] = {}
        for name, entries in self.entries_by_index.items():
            idx_to_pairs: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
            for entry_id, entry in enumerate(entries):
                for occ in entry.raw.get("occurrences", []):
                    idx = occ.get("shoryoshu_idx")
                    if idx is None:
                        continue
                    idx_to_pairs[idx][entry_id] += 1
            resolved: Dict[int, List[Tuple[IndexEntry, int]]] = {}
            for idx, eid_to_count in idx_to_pairs.items():
                pairs = [(entries[eid], cnt) for eid, cnt in eid_to_count.items()]
                pairs.sort(key=lambda p: (-p[1], p[0].name))
                resolved[idx] = pairs
            per[name] = resolved
        self.per_idx = per

    # ------------------------------------------------------------------
    # alias_to_canonical / entry_by_key / entry_篇sets
    # ------------------------------------------------------------------

    def _build_lookups(self) -> None:
        """各索引の primary key と alias を逆引き可能にする。"""
        for name, entries in self.entries_by_index.items():
            pk = PRIMARY_KEY[name]
            by_key: Dict[str, IndexEntry] = {}
            篇sets: Dict[str, frozenset] = {}
            alias_map: Dict[str, str] = {}
            for e in entries:
                key_raw = e.raw.get(pk)
                if key_raw is None:
                    continue
                key = str(key_raw)
                by_key[key] = e
                篇sets[key] = frozenset(int(i) for i in e.raw.get("篇分布", []) or [])
                alias_map.setdefault(key, key)  # canonical も自身を引けるように
                for alias in _extract_aliases(name, e.raw):
                    if alias and alias not in alias_map:
                        alias_map[alias] = key
            self.entry_by_key[name] = by_key
            self.entry_篇sets[name] = 篇sets
            self.alias_to_canonical[name] = alias_map

    # ------------------------------------------------------------------
    # 共起マトリックス（§13.7.3）
    # ------------------------------------------------------------------

    def _build_co_occurrence(self) -> None:
        """7 ペア（無向）を前計算してメモリ常駐。逆方向も転置で派生。"""
        for a_name, b_name in CO_OCCURRENCE_PAIRS:
            mat: Dict[str, Dict[str, int]] = {}
            a_sets = self.entry_篇sets.get(a_name, {})
            b_sets = self.entry_篇sets.get(b_name, {})
            same = (a_name == b_name)
            for ak, aset in a_sets.items():
                if not aset:
                    continue
                row: Dict[str, int] = {}
                for bk, bset in b_sets.items():
                    if same and ak == bk:
                        continue
                    n = len(aset & bset)
                    if n > 0:
                        row[bk] = n
                if row:
                    mat[ak] = row
            self.co_occurrence[(a_name, b_name)] = mat

        # 逆方向（前計算済みの転置を派生）
        for a_name, b_name in _REVERSE_PAIRS:
            if (a_name, b_name) in self.co_occurrence:
                continue
            base = self.co_occurrence.get((b_name, a_name))
            if base is None:
                continue
            inv: Dict[str, Dict[str, int]] = {}
            for bk, row in base.items():
                for ak, n in row.items():
                    inv.setdefault(ak, {})[bk] = n
            self.co_occurrence[(a_name, b_name)] = inv

    # ------------------------------------------------------------------
    # 公開ヘルパ
    # ------------------------------------------------------------------

    def lookup_entry(self, index_name: str, key: str) -> Optional[Tuple[IndexEntry, str, bool]]:
        """
        key を canonical または alias として解決し、(entry, canonical_key, alias_matched)
        を返す。見つからなければ None。
        """
        amap = self.alias_to_canonical.get(index_name, {})
        canonical = amap.get(key)
        if canonical is None:
            return None
        entry = self.entry_by_key.get(index_name, {}).get(canonical)
        if entry is None:
            return None
        return (entry, canonical, canonical != key)

    def top_co_occurring(
        self,
        source_index: str,
        source_key: str,
        target_index: str,
        n: int = 10,
    ) -> List[Tuple[str, int]]:
        """
        source の 篇分布 と target_index 各エントリの 篇分布 の積集合を計算し、
        上位 N 件を (key, count) 降順で返す。

        前計算済みのペアならマトリックスから O(1) で参照。
        未計算のペア（citations や sanskrit など）はその場で set 交差を計算。
        """
        # 前計算済み or 転置済み
        mat = self.co_occurrence.get((source_index, target_index))
        if mat is not None:
            row = mat.get(source_key, {})
            items = sorted(row.items(), key=lambda p: (-p[1], p[0]))
            return items[:n]
        # フォールバック：その場で交差計算
        src_set = self.entry_篇sets.get(source_index, {}).get(source_key)
        if not src_set:
            return []
        same = (source_index == target_index)
        results: List[Tuple[str, int]] = []
        for tk, tset in self.entry_篇sets.get(target_index, {}).items():
            if same and tk == source_key:
                continue
            n_co = len(src_set & tset)
            if n_co > 0:
                results.append((tk, n_co))
        results.sort(key=lambda p: (-p[1], p[0]))
        return results[:n]

    # ------------------------------------------------------------------
    # /api/篇/:idx を組み立てる（§13.6）
    # ------------------------------------------------------------------

    def build_篇_card(
        self,
        idx: int,
        excerpt_chars: int = 300,
        include_full_text: bool = False,
    ) -> Dict[str, Any]:
        if not (0 <= idx < len(self.miyasaka)):
            raise ValueError(f"shoryoshu_idx={idx} is out of range (0..{len(self.miyasaka)-1})")

        entry = self.miyasaka[idx]
        ページ = entry.get("ページ", []) or []
        kakikudashi_full = "".join(p.get("kakikudashi", "") or "" for p in ページ)
        gendaigoyaku_full = "".join(p.get("gendaigoyaku", "") or "" for p in ページ)
        kk_len = len(kakikudashi_full)
        gg_len = len(gendaigoyaku_full)
        ratio = round(gg_len / kk_len, 2) if kk_len > 0 else 0.0

        indices_block: Dict[str, List[Dict[str, Any]]] = {}
        totals_block: Dict[str, int] = {}
        for name in INDEX_FILES.keys():
            pairs = self.per_idx.get(name, {}).get(idx, [])
            indices_block[name] = [_format_index_hit(name, e, cnt) for (e, cnt) in pairs]
            totals_block[name] = len(pairs)

        excerpts = {
            "kakikudashi_head": kakikudashi_full[:excerpt_chars],
            "gendaigoyaku_head": gendaigoyaku_full[:excerpt_chars],
        }

        result: Dict[str, Any] = {
            "shoryoshu_idx": idx,
            "篇名": entry.get("篇名"),
            "巻": entry.get("巻番号"),
            "原文題": entry.get("原文題"),
            "詩形": entry.get("詩形"),
            "page_count": len(ページ),
            "字数": {"書き下し": kk_len, "現代語訳": gg_len, "倍率": ratio},
            "indices": indices_block,
            "totals": totals_block,
            "excerpts": excerpts,
            "metadata": {"schema_version": self.schema_version},
        }
        if include_full_text:
            result["full_text"] = {
                "kakikudashi": kakikudashi_full,
                "gendaigoyaku": gendaigoyaku_full,
            }
        return result

    # ------------------------------------------------------------------
    # 詳細参照系 6 本（§13.5）
    # ------------------------------------------------------------------

    def build_reference(
        self,
        endpoint: str,
        key: str,
        full_context: bool = False,
        top_n: int = 10,
        max_occurrences_when_short: int = 5,
    ) -> Dict[str, Any]:
        """
        詳細参照系 6 本（terms / persons / places / citations / sanskrit /
        kukai_works）の共通レスポンスを組み立てる。

        - key は canonical / term / jukugo そのものか、alias / matched_form
          のいずれかで解決可能。
        - full_context=False の既定では occurrences を冒頭 max_occurrences_when_short 件
          に絞る（仕様 §13.5.1 の挙動を簡略化した実装。±400 字拡張は将来 v1.7 以降）。
        - top_n は related ブロックの各カテゴリ上限。

        endpoint が INDEX_FILES に存在しない、または key が解決できない場合は
        KeyError を投げる（FastAPI 側で 404 にマップ）。
        """
        if endpoint not in INDEX_FILES:
            raise KeyError(f"UNKNOWN_ENDPOINT: {endpoint}")

        result = self.lookup_entry(endpoint, key)
        if result is None:
            raise KeyError(f"NOT_FOUND: {endpoint}={key}")
        entry, canonical, alias_matched = result

        raw = dict(entry.raw)
        full_occ_count = len(raw.get("occurrences", []) or [])
        truncated = False
        if not full_context and "occurrences" in raw and full_occ_count > max_occurrences_when_short:
            raw["occurrences"] = list(raw["occurrences"])[:max_occurrences_when_short]
            truncated = True

        related = self._build_related_block(endpoint, canonical, top_n)

        return {
            "query": {
                "endpoint": endpoint,
                "key": key,
                "canonical": canonical,
                "alias_matched": alias_matched,
                "full_context": full_context,
            },
            "entry": raw,
            "related": related,
            "metadata": {
                "schema_version": self.schema_version,
                "occurrence_count_total": full_occ_count,
                "occurrence_count_returned": len(raw.get("occurrences", []) or []),
                "occurrence_truncated": truncated,
                "top_n": top_n,
            },
        }

    # ------------------------------------------------------------------
    # related ブロック組立（参照系 6 本ごとに方針を切替）
    # ------------------------------------------------------------------

    def _build_related_block(self, endpoint: str, canonical: str, n: int) -> Dict[str, Any]:
        related: Dict[str, Any] = {}
        if endpoint == "terms":
            related["co_occurring_kaimyo_jukugo"] = self._co_block(endpoint, canonical, "kaimyo_jukugo", n)
            related["co_occurring_persons"]       = self._co_block(endpoint, canonical, "persons", n)
            related["co_occurring_places"]        = self._co_block(endpoint, canonical, "places", n)
            related["co_occurring_citations"]     = self._co_block(endpoint, canonical, "citations", n)
        elif endpoint == "persons":
            related["co_occurring_persons"]       = self._co_block(endpoint, canonical, "persons", n)
            related["co_occurring_places"]        = self._co_block(endpoint, canonical, "places", n)
            related["co_occurring_terms"]         = self._co_block(endpoint, canonical, "terms", n)
            related["co_occurring_kaimyo_jukugo"] = self._co_block(endpoint, canonical, "kaimyo_jukugo", n)
            related["co_occurring_citations"]     = self._co_block(endpoint, canonical, "citations", n)
        elif endpoint == "places":
            related["co_occurring_persons"]       = self._co_block(endpoint, canonical, "persons", n)
            related["co_occurring_terms"]         = self._co_block(endpoint, canonical, "terms", n)
            related["co_occurring_kaimyo_jukugo"] = self._co_block(endpoint, canonical, "kaimyo_jukugo", n)
            related["co_occurring_citations"]     = self._co_block(endpoint, canonical, "citations", n)
        elif endpoint == "citations":
            related["co_occurring_persons"]       = self._co_block(endpoint, canonical, "persons", n)
            related["co_occurring_places"]        = self._co_block(endpoint, canonical, "places", n)
            related["co_occurring_terms"]         = self._co_block(endpoint, canonical, "terms", n)
            related["co_occurring_kaimyo_jukugo"] = self._co_block(endpoint, canonical, "kaimyo_jukugo", n)
        elif endpoint == "sanskrit":
            related["related_kaimyo_jukugo_via_sanskrit_origins"] = self._sanskrit_to_kaimyo(canonical, n)
            related["co_occurring_persons"]       = self._co_block(endpoint, canonical, "persons", n)
            related["co_occurring_places"]        = self._co_block(endpoint, canonical, "places", n)
            related["co_occurring_terms"]         = self._co_block(endpoint, canonical, "terms", n)
        elif endpoint == "kukai_works":
            related["co_occurring_persons"]       = self._co_block(endpoint, canonical, "persons", n)
            related["co_occurring_places"]        = self._co_block(endpoint, canonical, "places", n)
            related["co_occurring_terms"]         = self._co_block(endpoint, canonical, "terms", n)
            related["co_occurring_kaimyo_jukugo"] = self._co_block(endpoint, canonical, "kaimyo_jukugo", n)
        return related

    def _co_block(
        self,
        source_index: str,
        source_key: str,
        target_index: str,
        n: int,
    ) -> List[Dict[str, Any]]:
        pairs = self.top_co_occurring(source_index, source_key, target_index, n)
        out: List[Dict[str, Any]] = []
        for k, count in pairs:
            e = self.entry_by_key.get(target_index, {}).get(k)
            if e is None:
                continue
            item: Dict[str, Any] = {"co_count": count}
            if target_index == "persons":
                item["canonical"]   = k
                item["subcategory"] = e.raw.get("subcategory")
            elif target_index == "places":
                item["canonical"]   = k
                item["subcategory"] = e.raw.get("subcategory")
            elif target_index == "kaimyo_jukugo":
                item["jukugo"]              = k
                item["kaimyo_score"]        = e.raw.get("kaimyo_score")
                item["needs_human_review"]  = bool(e.raw.get("needs_human_review", False))
            elif target_index == "terms":
                item["term"]            = k
                item["kaimyo_suitable"] = bool(e.raw.get("kaimyo_suitable", False))
            elif target_index == "citations":
                item["term"] = k
            elif target_index == "kukai_works":
                item["term"] = k
            elif target_index == "sanskrit":
                item["canonical"] = k
            out.append(item)
        return out

    def _sanskrit_to_kaimyo(self, sanskrit_canonical: str, n: int) -> List[Dict[str, Any]]:
        """sanskrit_origins フィールドから kaimyo_jukugo の逆引き。"""
        kaimyo_entries = self.entries_by_index.get("kaimyo_jukugo", [])
        out: List[Dict[str, Any]] = []
        for e in kaimyo_entries:
            sos = e.raw.get("sanskrit_origins") or []
            # sanskrit_origins は list[str] のことも list[dict] のこともある（旧形式互換）
            for so in sos:
                so_canon = so if isinstance(so, str) else (so.get("canonical") if isinstance(so, dict) else None)
                if so_canon == sanskrit_canonical:
                    out.append({
                        "jukugo":             e.raw.get("jukugo"),
                        "kaimyo_score":       e.raw.get("kaimyo_score"),
                        "needs_human_review": bool(e.raw.get("needs_human_review", False)),
                        "occurrence_count":   e.raw.get("occurrence_count"),
                    })
                    break
        out.sort(key=lambda d: (-(d.get("kaimyo_score") or 0), d.get("jukugo") or ""))
        return out[:n]

    # ------------------------------------------------------------------
    # /api/kaimyo/candidates （§13.3 中核 1・v1.7 で新規追加）
    # ------------------------------------------------------------------

    def build_kaimyo_candidates(
        self,
        characteristics: List[str],
        min_score: float = 30.0,
        limit: int = 20,
        include_review: bool = False,
        prefer_persons: Optional[List[str]] = None,
        prefer_places: Optional[List[str]] = None,
        length: Optional[int] = None,
    ) -> Dict[str, Any]:
        """§13.3 GET /api/kaimyo/candidates の本体。

        Step 1: characteristics → ICHIJI_SET 解決（CHARACTERISTIC_TO_ICHIJI）
        Step 2: index_shoryoshu_kaimyo.json から候補抽出
                （kaimyo_chars × ICHIJI_SET の積集合・min_score・review・length）
        Step 3: prefer_persons / prefer_places 共起ボーナス（共通篇 1 つ +0.5・上限 +5）
        Step 4: 出典文（最多 4 件）+ 梵語原語（sanskrit 索引照合）
                + 関連人物（上位 5）+ 関連地名（上位 3）
        Step 5: final_score = kaimyo_score + bonus_score 降順 + limit 切詰

        例外:
            ValueError("MISSING_PARAMETER:characteristics")
                characteristics が空のとき
            ValueError("UNKNOWN_CHARACTERISTIC:<カンマ区切り>")
                CHARACTERISTIC_TO_ICHIJI に登録のないキーが含まれるとき
        """
        from datetime import datetime, timezone

        # ---- 入力検証 ----
        if not characteristics:
            raise ValueError("MISSING_PARAMETER:characteristics")

        # ---- Step 1: ICHIJI_SET 解決 ----
        cti = self.api_mappings.get("characteristic_to_ichiji", {}) or {}
        ichiji_set: Set[str] = set()
        unknown: List[str] = []
        for c in characteristics:
            chars = cti.get(c)
            if chars is None:
                unknown.append(c)
                continue
            for ch in chars or []:
                ichiji_set.add(str(ch))
        if unknown:
            raise ValueError("UNKNOWN_CHARACTERISTIC:" + ",".join(unknown))

        # ---- Step 3 準備: prefer_* を canonical 解決し、篇分布の和集合を作る ----
        prefer_set: Set[int] = set()
        resolved_persons: List[str] = []
        resolved_places: List[str] = []
        unresolved_persons: List[str] = []
        unresolved_places: List[str] = []
        if prefer_persons:
            for raw_p in prefer_persons:
                res = self.lookup_entry("persons", raw_p)
                if res is None:
                    unresolved_persons.append(raw_p)
                    continue
                _, canon, _ = res
                resolved_persons.append(canon)
                prefer_set |= self.entry_篇sets.get("persons", {}).get(canon, frozenset())
        if prefer_places:
            for raw_p in prefer_places:
                res = self.lookup_entry("places", raw_p)
                if res is None:
                    unresolved_places.append(raw_p)
                    continue
                _, canon, _ = res
                resolved_places.append(canon)
                prefer_set |= self.entry_篇sets.get("places", {}).get(canon, frozenset())

        # ---- Step 2 + Step 3: 候補抽出 + ボーナス加算 ----
        candidates: List[Dict[str, Any]] = []
        kaimyo_篇sets = self.entry_篇sets.get("kaimyo_jukugo", {})
        for entry in self.entries_by_index.get("kaimyo_jukugo", []):
            raw = entry.raw
            chars = list(raw.get("kaimyo_chars") or [])
            if not chars:
                continue
            matched = [c for c in chars if c in ichiji_set]
            if not matched:
                continue
            score = float(raw.get("kaimyo_score") or 0.0)
            if score < float(min_score):
                continue
            if (not include_review) and bool(raw.get("needs_human_review", False)):
                continue
            jukugo = str(raw.get("jukugo") or "")
            jl = len(jukugo)
            if length is not None and jl != int(length):
                continue

            # 共起ボーナス
            bonus = 0.0
            if prefer_set:
                cand_set = kaimyo_篇sets.get(jukugo, frozenset())
                common = len(cand_set & prefer_set)
                bonus = min(5.0, common * 0.5)

            candidates.append({
                "raw": raw,
                "matched": matched,
                "kaimyo_score": round(score, 2),
                "bonus_score": round(bonus, 2),
                "final_score": round(score + bonus, 2),
                "jukugo": jukugo,
                "length": jl,
            })

        total_matched = len(candidates)

        # ---- Step 5 (前段): ソート + 切詰 ----
        candidates.sort(key=lambda c: (-c["final_score"], -c["kaimyo_score"], c["jukugo"]))
        if limit is not None and limit >= 0:
            candidates = candidates[: int(limit)]

        # ---- Step 4: 付帯情報生成 ----
        sanskrit_by_canonical = self.entry_by_key.get("sanskrit", {})
        persons_by_canonical = self.entry_by_key.get("persons", {})
        places_by_canonical = self.entry_by_key.get("places", {})

        results: List[Dict[str, Any]] = []
        for rank, c in enumerate(candidates, start=1):
            raw = c["raw"]

            # 出典文（最多 4 件）
            examples: List[Dict[str, Any]] = []
            for occ in (raw.get("occurrences") or [])[:4]:
                examples.append({
                    "shoryoshu_idx":    occ.get("shoryoshu_idx"),
                    "篇名":              occ.get("篇名"),
                    "巻":                occ.get("巻"),
                    "context":          occ.get("context"),
                    "context_position": occ.get("context_position"),
                })

            # 梵語原語（sanskrit 索引照合・kaimyo の seed_definition で補強）
            sanskrit_out: List[Dict[str, Any]] = []
            for so in raw.get("sanskrit_origins") or []:
                so_canon = (
                    so if isinstance(so, str)
                    else (so.get("canonical") if isinstance(so, dict) else None)
                )
                if not so_canon:
                    continue
                sk = sanskrit_by_canonical.get(so_canon)
                sanskrit_out.append({
                    "canonical": so_canon,
                    "definition": raw.get("seed_definition") or "",
                    "occurrence_count_in_corpus": (sk.raw.get("occurrence_count") if sk else 0) or 0,
                    "linked_in_index": sk is not None,
                })

            # 関連人物（共起頻度上位 5）
            related_persons: List[Dict[str, Any]] = []
            for pk, count in self.top_co_occurring("kaimyo_jukugo", c["jukugo"], "persons", 5):
                pe = persons_by_canonical.get(pk)
                related_persons.append({
                    "canonical": pk,
                    "subcategory": pe.raw.get("subcategory") if pe else None,
                    "co_occurrence_count": count,
                })

            # 関連地名（共起頻度上位 3）
            related_places: List[Dict[str, Any]] = []
            for pk, count in self.top_co_occurring("kaimyo_jukugo", c["jukugo"], "places", 3):
                pe = places_by_canonical.get(pk)
                related_places.append({
                    "canonical": pk,
                    "subcategory": pe.raw.get("subcategory") if pe else None,
                    "co_occurrence_count": count,
                })

            results.append({
                "rank":               rank,
                "jukugo":             c["jukugo"],
                "length":             c["length"],
                "kaimyo_chars":       list(raw.get("kaimyo_chars") or []),
                "kaimyo_score":       c["kaimyo_score"],
                "bonus_score":        c["bonus_score"],
                "final_score":        c["final_score"],
                "source":             raw.get("source_tag"),
                "needs_human_review": bool(raw.get("needs_human_review", False)),
                "sanskrit_origins":   sanskrit_out,
                "matched_ichiji":     c["matched"],
                "occurrence_count":   raw.get("occurrence_count"),
                "篇分布_count":        len(raw.get("篇分布") or []),
                "examples":           examples,
                "related_persons":    related_persons,
                "related_places":     related_places,
            })

        return {
            "query": {
                "characteristics":     list(characteristics),
                "ichiji_resolved":     sorted(ichiji_set),
                "min_score":           float(min_score),
                "limit":               int(limit),
                "include_review":      bool(include_review),
                "length":              length,
                "prefer_persons":      resolved_persons,
                "prefer_places":       resolved_places,
                "unresolved_persons":  unresolved_persons,
                "unresolved_places":   unresolved_places,
            },
            "results": results,
            "metadata": {
                "total_matched_before_limit": total_matched,
                "schema_version":             self.schema_version,
                "data_corpus":                "shoryoshu_miyasaka_v_phase2_complete",
                "generated_at":               datetime.now(timezone.utc).isoformat(),
            },
        }

    # ------------------------------------------------------------------
    # /api/houwa/citations （§13.4 中核 2・v1.8 で新規追加）
    # ------------------------------------------------------------------

    def build_houwa_citations(
        self,
        theme: str,
        expand: bool = True,
        limit: int = 10,
        include_persons: bool = True,
        include_places: bool = False,
        include_kaimyo_jukugo: bool = True,
        min_hits: int = 1,
        excerpt_radius: int = 150,
    ) -> Dict[str, Any]:
        """§13.4 GET /api/houwa/citations の本体（v1.8 で実装）。

        Step 1: theme → THEME_EXPANSION で関連語展開（expand=false ならそのまま）
        Step 2: terms / citations / sanskrit (+persons +places +kaimyo_jukugo) を並行検索
        Step 3: 篇単位の集約（shoryoshu_idx でグルーピング）
        Step 4: 篇スコアリング
                terms*3 + citations*2 + sanskrit*2 + kaimyo_jukugo*1 + persons*1 + places*1
        Step 5: 出典文抜粋（gendaigoyaku の最初のヒット位置 ±excerpt_radius 字）
        Step 6: 篇スコア降順 + limit 切詰

        spec §13.4 への拡張点（v1.8 で追加）:
          - include_kaimyo_jukugo（既定 true）：戒名向け熟語索引（1971 件）を併用。
            terms 索引が 19 件の curated 教学用語のみで、無常・智慧・慈悲・金剛
            等の代表的テーマ語が kaimyo_jukugo にしか存在しないため、法話・
            諷誦文用途で実用性を確保するための拡張。spec 厳密準拠したい場合は
            false で抑止可能。

        例外:
            ValueError("MISSING_PARAMETER:theme")  theme が空のとき
        """
        if not theme:
            raise ValueError("MISSING_PARAMETER:theme")

        # ---- Step 1: テーマ展開 ----
        te = self.api_mappings.get("theme_expansion") or {}
        is_known_theme = theme in te
        if expand and is_known_theme:
            expanded_terms: List[str] = list(te[theme])
            if theme not in expanded_terms:
                expanded_terms.insert(0, theme)
        else:
            expanded_terms = [theme]

        # ---- Step 2 準備 ----
        target_indices: List[str] = ["terms", "citations", "sanskrit"]
        if include_kaimyo_jukugo:
            target_indices.append("kaimyo_jukugo")
        if include_persons:
            target_indices.append("persons")
        if include_places:
            target_indices.append("places")

        # ---- Step 2 + Step 3: 並行検索 + 篇単位集約 ----
        per_idx_hits: Dict[int, Dict[str, List[Dict[str, Any]]]] = defaultdict(
            lambda: defaultdict(list)
        )
        first_positions: Dict[int, int] = {}
        seen_canonicals: Set[Tuple[str, str]] = set()

        for term_word in expanded_terms:
            for idx_name in target_indices:
                amap = self.alias_to_canonical.get(idx_name, {})
                canon = amap.get(term_word)
                if canon is None:
                    continue
                seen_key = (idx_name, canon)
                if seen_key in seen_canonicals:
                    continue
                seen_canonicals.add(seen_key)

                entry = self.entry_by_key.get(idx_name, {}).get(canon)
                if entry is None:
                    continue

                occs_by_idx: Dict[int, int] = defaultdict(int)
                occs_first_pos: Dict[int, int] = {}
                for occ in entry.raw.get("occurrences", []) or []:
                    shidx = occ.get("shoryoshu_idx")
                    if shidx is None:
                        continue
                    occs_by_idx[shidx] += 1
                    pos = occ.get("context_position")
                    if isinstance(pos, int):
                        if shidx not in occs_first_pos or pos < occs_first_pos[shidx]:
                            occs_first_pos[shidx] = pos

                for shidx, cnt in occs_by_idx.items():
                    per_idx_hits[shidx][idx_name].append({
                        "key": canon,
                        "matched_form": term_word,
                        "count": cnt,
                    })
                    if shidx in occs_first_pos:
                        cur = first_positions.get(shidx)
                        if cur is None or occs_first_pos[shidx] < cur:
                            first_positions[shidx] = occs_first_pos[shidx]

        # ---- Step 4: 篇スコアリング ----
        weights: Dict[str, int] = {
            "terms":         3,
            "citations":     2,
            "sanskrit":      2,
            "kaimyo_jukugo": 1,
            "persons":       1,
            "places":        1,
        }
        candidates: List[Dict[str, Any]] = []
        for shidx, cat_hits in per_idx_hits.items():
            total_hits = sum(sum(h["count"] for h in lst) for lst in cat_hits.values())
            if total_hits < int(min_hits):
                continue
            score = 0
            for cat, lst in cat_hits.items():
                w = weights.get(cat, 0)
                for h in lst:
                    score += w * h["count"]
            candidates.append({
                "shoryoshu_idx": shidx,
                "score":         score,
                "cat_hits":      dict(cat_hits),
                "total_hits":    total_hits,
            })

        total_matched = len(candidates)

        # ---- Step 6: ソート + 切詰 ----
        candidates.sort(key=lambda c: (-c["score"], c["shoryoshu_idx"]))
        if limit is not None and limit >= 0:
            candidates = candidates[: int(limit)]

        # ---- Step 5: 出典文抜粋 + 結果整形 ----
        persons_by_canonical = self.entry_by_key.get("persons", {})
        places_by_canonical = self.entry_by_key.get("places", {})

        citations_out: List[Dict[str, Any]] = []
        for rank, c in enumerate(candidates, start=1):
            shidx = c["shoryoshu_idx"]
            miyasaka_entry = self.miyasaka[shidx]
            ページ = miyasaka_entry.get("ページ", []) or []
            kk_full = "".join(p.get("kakikudashi", "") or "" for p in ページ)
            gg_full = "".join(p.get("gendaigoyaku", "") or "" for p in ページ)
            kk_len = len(kk_full)
            gg_len = len(gg_full)
            ratio = round(gg_len / kk_len, 2) if kk_len > 0 else 0.0

            first_pos = first_positions.get(shidx)
            if first_pos is None or gg_len == 0:
                context_excerpt = gg_full[: int(excerpt_radius) * 2]
                excerpt_position = 0
            else:
                start = max(0, first_pos - int(excerpt_radius))
                end = min(gg_len, first_pos + int(excerpt_radius))
                context_excerpt = gg_full[start:end]
                excerpt_position = start

            hits_out: Dict[str, List[Dict[str, Any]]] = {
                "terms": [], "citations": [], "sanskrit": [],
                "kaimyo_jukugo": [], "persons": [], "places": [],
            }
            kaimyo_by_key = self.entry_by_key.get("kaimyo_jukugo", {})
            for cat in ("terms", "citations", "sanskrit", "kaimyo_jukugo", "persons", "places"):
                lst = c["cat_hits"].get(cat, []) or []
                lst_sorted = sorted(lst, key=lambda h: (-h["count"], h["key"]))
                cat_out: List[Dict[str, Any]] = []
                for h in lst_sorted:
                    k = h["key"]
                    base = {"matched_form": h["matched_form"], "count": h["count"]}
                    if cat == "terms":
                        cat_out.append({"term": k, **base})
                    elif cat == "citations":
                        cat_out.append({"term": k, **base})
                    elif cat == "sanskrit":
                        cat_out.append({"canonical": k, **base})
                    elif cat == "kaimyo_jukugo":
                        ke = kaimyo_by_key.get(k)
                        cat_out.append({
                            "jukugo": k,
                            "kaimyo_score": ke.raw.get("kaimyo_score") if ke else None,
                            "needs_human_review": bool(ke.raw.get("needs_human_review", False)) if ke else False,
                            **base,
                        })
                    elif cat == "persons":
                        pe = persons_by_canonical.get(k)
                        cat_out.append({
                            "canonical": k,
                            "subcategory": pe.raw.get("subcategory") if pe else None,
                            **base,
                        })
                    elif cat == "places":
                        pe = places_by_canonical.get(k)
                        cat_out.append({
                            "canonical": k,
                            "subcategory": pe.raw.get("subcategory") if pe else None,
                            **base,
                        })
                hits_out[cat] = cat_out

            citations_out.append({
                "rank":             rank,
                "shoryoshu_idx":    shidx,
                "篇名":              miyasaka_entry.get("篇名"),
                "巻":                miyasaka_entry.get("巻番号"),
                "score":            c["score"],
                "hits":             hits_out,
                "context_excerpt":  context_excerpt,
                "excerpt_position": excerpt_position,
                "字数": {
                    "書き下し": kk_len,
                    "現代語訳": gg_len,
                    "倍率":     ratio,
                },
            })

        return {
            "query": {
                "theme":                 theme,
                "expanded_terms":        expanded_terms,
                "expand":                bool(expand),
                "is_known_theme":        is_known_theme,
                "limit":                 int(limit),
                "include_persons":       bool(include_persons),
                "include_places":        bool(include_places),
                "include_kaimyo_jukugo": bool(include_kaimyo_jukugo),
                "min_hits":              int(min_hits),
            },
            "citations": citations_out,
            "metadata": {
                "total_篇_matched": total_matched,
                "schema_version":   self.schema_version,
                "data_corpus":      "shoryoshu_miyasaka_v_phase2_complete",
            },
        }



# --------------------------------------------------------------------------
# 索引ヒット 1 件を §13.6.2 出力スキーマ通りに整形（/api/篇/:idx 用）
# --------------------------------------------------------------------------

def _format_index_hit(name: str, entry: IndexEntry, count: int) -> Dict[str, Any]:
    raw = entry.raw
    if name == "terms":
        return {"term": raw.get("term"), "count": count, "kaimyo_suitable": bool(raw.get("kaimyo_suitable", False))}
    if name == "citations":
        return {"term": raw.get("term"), "count": count}
    if name == "sanskrit":
        return {"canonical": raw.get("canonical"), "count": count}
    if name == "kaimyo_jukugo":
        return {
            "jukugo":  raw.get("jukugo"),
            "score":   raw.get("kaimyo_score"),
            "review":  bool(raw.get("needs_human_review", False)),
            "count":   count,
        }
    if name == "persons":
        return {"canonical": raw.get("canonical"), "subcategory": raw.get("subcategory"), "count": count}
    if name == "places":
        return {"canonical": raw.get("canonical"), "subcategory": raw.get("subcategory"), "count": count}
    if name == "kukai_works":
        return {"term": raw.get("term"), "count": count}
    raise ValueError(f"unknown index name: {name}")


# --------------------------------------------------------------------------
# alias 抽出（索引ごとの形式差を吸収）
# --------------------------------------------------------------------------

def _extract_aliases(index_name: str, raw: Dict[str, Any]) -> List[str]:
    """各索引から alias 候補（人間が打鍵しうる表記）の文字列リストを抽出。

    形式差:
      - persons / places: aliases = list[str], matched_forms = list[{form, count}]
      - sanskrit:         aliases = list[{form, count}]
      - citations / kukai_works: aliases = list[str]
      - terms / kaimyo_jukugo:   aliases なし（primary key のみ）
    """
    out: List[str] = []
    aliases = raw.get("aliases") or []
    for a in aliases:
        if isinstance(a, str):
            out.append(a)
        elif isinstance(a, dict):
            f = a.get("form")
            if f:
                out.append(str(f))
    for mf in raw.get("matched_forms") or []:
        if isinstance(mf, dict):
            f = mf.get("form")
            if f:
                out.append(str(f))
    # 重複除去（出現順保持）
    seen: Set[str] = set()
    uniq: List[str] = []
    for s in out:
        if s and s not in seen:
            seen.add(s)
            uniq.append(s)
    return uniq

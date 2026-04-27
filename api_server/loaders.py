"""
api_server/loaders.py
=====================

横断索引化フェーズ B（cross_index_spec.md §13）の API サーバ起動時ロード基盤。

7 索引 + miyasaka.json + api_mappings.json をメモリにロードし、篇 idx →
ヒットエントリ集合の逆引き辞書を構築する。/api/篇/:idx をはじめとする
すべてのエンドポイントから O(1) で参照できる。

使い方:

    from api_server.loaders import IndexStore
    store = IndexStore.load_default()
    篇カルテ = store.build_篇_card(idx=1, excerpt_chars=300, include_full_text=False)

cross_index_spec.md §13.8.2 起動シーケンスに準拠。
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

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

    /api/篇/:idx は per_idx[name][idx] -> [(entry, occ_count), ...] を引いて
    すぐにレスポンスを組み立てる。
    """

    indices_raw: Dict[str, Dict[str, Any]]               # name -> 索引 JSON 全体
    entries_by_index: Dict[str, List[IndexEntry]]        # name -> エントリ配列
    miyasaka: List[Dict[str, Any]]                        # 全 112 篇の本文
    api_mappings: Dict[str, Any]                          # CHARACTERISTIC_TO_ICHIJI 等

    # 篇 idx 別の逆引き：name -> idx -> [(entry, occ_count), ...]（occ_count 降順）
    per_idx: Dict[str, Dict[int, List[Tuple[IndexEntry, int]]]] = field(default_factory=dict)

    schema_version: str = "1.4.0"

    # ------------------------------------------------------------------
    # ロード
    # ------------------------------------------------------------------

    @classmethod
    def load_default(cls, repo_root: Optional[Path] = None) -> "IndexStore":
        """リポジトリルートから既定パスでロードする。"""
        if repo_root is None:
            # api_server/loaders.py の親ディレクトリの親 = リポジトリルート
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
        return store

    # ------------------------------------------------------------------
    # 篇 idx → エントリ集合の逆引き辞書を構築
    # ------------------------------------------------------------------

    def _build_per_idx(self) -> None:
        """
        各索引の occurrences を走査し、name -> idx -> [(entry, count), ...] を構築。
        count は当該 idx 内の occurrence 数（出現回数）。降順で保持する。
        """
        per: Dict[str, Dict[int, List[Tuple[IndexEntry, int]]]] = {}
        for name, entries in self.entries_by_index.items():
            idx_to_pairs: Dict[int, Dict[int, int]] = defaultdict(lambda: defaultdict(int))
            # entry_id (= entries 配列内の位置) をキーに count を集計
            for entry_id, entry in enumerate(entries):
                for occ in entry.raw.get("occurrences", []):
                    idx = occ.get("shoryoshu_idx")
                    if idx is None:
                        continue
                    idx_to_pairs[idx][entry_id] += 1
            # 降順ソート + 元エントリへ解決
            resolved: Dict[int, List[Tuple[IndexEntry, int]]] = {}
            for idx, eid_to_count in idx_to_pairs.items():
                pairs = [(entries[eid], cnt) for eid, cnt in eid_to_count.items()]
                pairs.sort(key=lambda p: (-p[1], p[0].name))
                resolved[idx] = pairs
            per[name] = resolved
        self.per_idx = per

    # ------------------------------------------------------------------
    # /api/篇/:idx を組み立てる（§13.6）
    # ------------------------------------------------------------------

    def build_篇_card(
        self,
        idx: int,
        excerpt_chars: int = 300,
        include_full_text: bool = False,
    ) -> Dict[str, Any]:
        """
        仕様 §13.6.2 に準拠した篇カルテ JSON を組み立てる。

        idx が範囲外なら ValueError を投げる（FastAPI 側で 404 に変換）。
        """
        if not (0 <= idx < len(self.miyasaka)):
            raise ValueError(f"shoryoshu_idx={idx} is out of range (0..{len(self.miyasaka)-1})")

        entry = self.miyasaka[idx]
        ページ = entry.get("ページ", []) or []
        kakikudashi_full = "".join(p.get("kakikudashi", "") or "" for p in ページ)
        gendaigoyaku_full = "".join(p.get("gendaigoyaku", "") or "" for p in ページ)
        kk_len = len(kakikudashi_full)
        gg_len = len(gendaigoyaku_full)
        ratio = round(gg_len / kk_len, 2) if kk_len > 0 else 0.0

        # 各索引のヒット
        indices_block: Dict[str, List[Dict[str, Any]]] = {}
        totals_block: Dict[str, int] = {}
        for name in INDEX_FILES.keys():
            pairs = self.per_idx.get(name, {}).get(idx, [])
            indices_block[name] = [
                _format_index_hit(name, e, cnt) for (e, cnt) in pairs
            ]
            totals_block[name] = len(pairs)

        excerpts = {
            "kakikudashi_head": kakikudashi_full[:excerpt_chars],
            "gendaigoyaku_head": gendaigoyaku_full[:excerpt_chars],
        }

        result: Dict[str, Any] = {
            "shoryoshu_idx": idx,
            "篇名": entry.get("篇名"),
            "巻": entry.get("巻番号"),       # miyasaka.json では「巻番号」フィールド
            "原文題": entry.get("原文題"),
            "詩形": entry.get("詩形"),
            "page_count": len(ページ),
            "字数": {
                "書き下し": kk_len,
                "現代語訳": gg_len,
                "倍率": ratio,
            },
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


# --------------------------------------------------------------------------
# 索引ヒット 1 件を §13.6.2 出力スキーマ通りに整形
# --------------------------------------------------------------------------

def _format_index_hit(name: str, entry: IndexEntry, count: int) -> Dict[str, Any]:
    raw = entry.raw
    if name == "terms":
        return {
            "term": raw.get("term"),
            "count": count,
            "kaimyo_suitable": bool(raw.get("kaimyo_suitable", False)),
        }
    if name == "citations":
        return {"term": raw.get("term"), "count": count}
    if name == "sanskrit":
        return {"canonical": raw.get("canonical"), "count": count}
    if name == "kaimyo_jukugo":
        return {
            "jukugo": raw.get("jukugo"),
            "score": raw.get("kaimyo_score"),
            "review": bool(raw.get("needs_human_review", False)),
            "count": count,
        }
    if name == "persons":
        return {
            "canonical": raw.get("canonical"),
            "subcategory": raw.get("subcategory"),
            "count": count,
        }
    if name == "places":
        return {
            "canonical": raw.get("canonical"),
            "subcategory": raw.get("subcategory"),
            "count": count,
        }
    if name == "kukai_works":
        return {"term": raw.get("term"), "count": count}
    raise ValueError(f"unknown index name: {name}")

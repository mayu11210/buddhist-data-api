"""
_dev_references/validate_corpus.py
==================================

data/kukai/_corpus_manifest.json と実ファイルの整合性を検証するスクリプト。

使い方::

    python3 _dev_references/validate_corpus.py

役割:
  1. data/kukai/ 配下の全 *.json（アンダースコア始まりは除外）を列挙
  2. _corpus_manifest.json の files[] と過不足ないか確認
  3. 各ファイルの char_counts（kakikudashi / gendaigoyaku / genten / text）と
     manifest 記載値が一致するか確認
  4. data_status の bool（kakikudashi / gendaigoyaku / genten / kaimyo_excerpt）が
     実ファイルの状況と一致するか確認
  5. specialty_sections が実ファイルの top-level key と一致するか確認

役割（role）と完備判定（role_complete）の妥当性は本スクリプトでは検証しない
（それは設計判断のため、住職レビュー対象）。本スクリプトは純粋にメカニカルな
不整合（取込進捗の更新忘れ・char_counts のズレ等）を検出する。

設計方針メモ：図書館モデル（2026-05-03）／倉庫原則「メタデータは足し算」。

2026-06-10 拡張：dict_paragraphs 型（kakikudashi-data スキル取込の段落型 corpus・
bodaishinron-kouyou / 各開題 / dainichikyo / hizoki）に対応。char_counts は
「改行込み」「改行除き」の両規約を許容し、kaimyo_excerpt は検証対象外。
paragraphs / outline / translation_status 等の構造フィールドは specialty に数えない。

使い方は従来どおり: python3 _dev_references/validate_corpus.py
"""

from __future__ import annotations

import json
import os
import sys
from typing import Any, Dict, List

KUKAI_DIR = "data/kukai"
MANIFEST_PATH = "data/kukai/_corpus_manifest.json"

CORE_FIELDS = {
    "section",
    "source",
    "description",
    "text",
    "kakikudashi",
    "gendaigoyaku",
    "genten",
    "genten_source",
}

# dict_paragraphs 型（kakikudashi-data スキル取込・2026-06 系）の構造フィールド。
# これらは形式の一部であり specialty_sections には数えない（2026-06-10 追加）。
DICT_PARAGRAPHS_STRUCT_FIELDS = CORE_FIELDS | {
    "paragraphs",
    "outline",
    "translation_status",
    "format_note",
    "author",
    "base_text",
    "base_text_ref",
    "related",
    "taisho_ref",
    "genten_unavailable_reason",
}


def load_manifest() -> Dict[str, Any]:
    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def list_kukai_files() -> List[str]:
    return sorted(
        f
        for f in os.listdir(KUKAI_DIR)
        if f.endswith(".json") and not f.startswith("_")
    )


def measure_file(filename: str) -> Dict[str, Any]:
    """1 ファイルの実態を測定する。"""
    path = os.path.join(KUKAI_DIR, filename)
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    if isinstance(d, list):
        kk = sum(len(p.get("kakikudashi", "")) for e in d for p in e.get("ページ", []))
        gd = sum(len(p.get("gendaigoyaku", "")) for e in d for p in e.get("ページ", []))
        return {
            "type": "list",
            "entries_count": len(d),
            "char_counts": {
                "kakikudashi_total": kk,
                "gendaigoyaku_total": gd,
            },
            "data_status": {
                "kaimyo_excerpt": False,
                "kakikudashi": kk > 0,
                "gendaigoyaku": gd > 0,
                "genten": False,
                "specialty_sections": [],
            },
        }
    elif isinstance(d, dict) and isinstance(d.get("paragraphs"), list) and d["paragraphs"]:
        # dict_paragraphs 型（2026-06-10 対応）。
        # char_counts の歴史的経緯：register_manifest.py（スキル）は
        # 「トップレベル文字列から改行を除いた長さ」、手動登録分（dainichikyo 等）は
        # 「改行込みの長さ」で記録している。機械検証としては両規約を許容する。
        def _accept(key: str) -> set:
            v = d.get(key, "")
            if not isinstance(v, str):
                return {0}
            return {len(v), len(v.replace("\n", ""))}

        ps = d["paragraphs"]
        text_len = len(d.get("text", "")) if isinstance(d.get("text"), str) else 0
        kk_top = d.get("kakikudashi", "") if isinstance(d.get("kakikudashi"), str) else ""
        gd_top = d.get("gendaigoyaku", "") if isinstance(d.get("gendaigoyaku"), str) else ""
        gt_top = d.get("genten", "") if isinstance(d.get("genten"), str) else ""
        specialty = sorted(k for k in d.keys() if k not in DICT_PARAGRAPHS_STRUCT_FIELDS)
        return {
            "type": "dict_paragraphs",
            "paragraphs_count": len(ps),
            "untranslated_count": sum(1 for p in ps if not p.get("gendaigoyaku")),
            "char_counts_accept": {
                "kakikudashi": _accept("kakikudashi"),
                "gendaigoyaku": _accept("gendaigoyaku"),
                "genten": _accept("genten"),
                "text": _accept("text"),
                "paragraphs": {len(ps)},
            },
            "data_status": {
                # kaimyo_excerpt は dict_paragraphs では機械判定不能（text は
                # 概要文であり戒名抜粋ではない）ため検証対象外とする。
                "kakikudashi": len(kk_top) > 0,
                "gendaigoyaku": len(gd_top) > 0,
                "genten": len(gt_top) > 0,
                "specialty_sections": specialty,
            },
        }
    elif isinstance(d, dict):
        text_len = len(d.get("text", "")) if isinstance(d.get("text"), str) else 0
        kk = len(d.get("kakikudashi", "")) if isinstance(d.get("kakikudashi"), str) else 0
        gd = (
            len(d.get("gendaigoyaku", ""))
            if isinstance(d.get("gendaigoyaku"), str)
            else 0
        )
        gt = len(d.get("genten", "")) if isinstance(d.get("genten"), str) else 0
        specialty = sorted(k for k in d.keys() if k not in CORE_FIELDS)
        return {
            "type": "dict",
            "char_counts": {
                "text": text_len,
                "kakikudashi": kk,
                "gendaigoyaku": gd,
                "genten": gt,
            },
            "data_status": {
                "kaimyo_excerpt": text_len > 0,
                "kakikudashi": kk > 0,
                "gendaigoyaku": gd > 0,
                "genten": gt > 0,
                "specialty_sections": specialty,
            },
        }
    else:
        raise ValueError(f"unexpected JSON type for {filename}: {type(d).__name__}")


def main() -> int:
    manifest = load_manifest()
    files_meta_by_name = {m["filename"]: m for m in manifest.get("files", [])}

    real_files = list_kukai_files()
    real_set = set(real_files)
    manifest_set = set(files_meta_by_name.keys())

    errors: List[str] = []
    warnings: List[str] = []

    # 1. 過不足チェック
    missing_in_manifest = real_set - manifest_set
    missing_in_disk = manifest_set - real_set
    for fn in sorted(missing_in_manifest):
        errors.append(f"[過不足] manifest に未登録: {fn}")
    for fn in sorted(missing_in_disk):
        errors.append(f"[過不足] 実ファイル不在: {fn}")

    # 2. 各ファイルの整合性
    for fn in sorted(real_set & manifest_set):
        meta = files_meta_by_name[fn]
        actual = measure_file(fn)

        # type 一致
        if meta.get("type") != actual["type"]:
            errors.append(
                f"[type 不一致] {fn}: manifest={meta.get('type')!r} actual={actual['type']!r}"
            )
            continue

        # char_counts 一致
        if actual["type"] == "dict_paragraphs":
            # manifest に記載されたキーのみ照合（register_manifest.py は
            # kakikudashi / gendaigoyaku / paragraphs の 3 キーを書く。
            # genten / text は手動追記された場合のみ存在）。
            accept = actual["char_counts_accept"]
            for k, mv in meta.get("char_counts", {}).items():
                if k not in accept:
                    warnings.append(
                        f"[char_counts 未知キー] {fn}.{k}: manifest={mv}"
                    )
                    continue
                if mv not in accept[k]:
                    errors.append(
                        f"[char_counts 不一致] {fn}.{k}: manifest={mv} "
                        f"actual（許容値）={sorted(accept[k])}"
                    )
            if actual["untranslated_count"]:
                warnings.append(
                    f"[未訳段落] {fn}: {actual['untranslated_count']} 段落が未訳"
                )
        else:
            for k, v in actual["char_counts"].items():
                mv = meta.get("char_counts", {}).get(k)
                if mv != v:
                    errors.append(
                        f"[char_counts 不一致] {fn}.{k}: manifest={mv} actual={v}"
                    )

        # data_status の bool 一致（dict_paragraphs は kaimyo_excerpt を検証しない）
        ds_keys = (
            ("kakikudashi", "gendaigoyaku", "genten")
            if actual["type"] == "dict_paragraphs"
            else ("kaimyo_excerpt", "kakikudashi", "gendaigoyaku", "genten")
        )
        for k in ds_keys:
            mv = meta.get("data_status", {}).get(k)
            av = actual["data_status"].get(k)
            if mv != av:
                errors.append(
                    f"[data_status 不一致] {fn}.{k}: manifest={mv} actual={av}"
                )

        # specialty_sections 一致
        mspec = sorted(meta.get("data_status", {}).get("specialty_sections", []) or [])
        aspec = sorted(actual["data_status"].get("specialty_sections", []) or [])
        if mspec != aspec:
            errors.append(
                f"[specialty_sections 不一致] {fn}: manifest={mspec} actual={aspec}"
            )

        # entries_count （list 型のみ）
        if actual["type"] == "list":
            if meta.get("entries_count") != actual["entries_count"]:
                errors.append(
                    f"[entries_count 不一致] {fn}: manifest={meta.get('entries_count')} actual={actual['entries_count']}"
                )

    # 3. role / role_complete はメカニカル検証しない（住職レビュー対象）
    # ただし role が known な値か軽くチェック
    known_roles = {"primary_corpus", "auxiliary_meta", "specialty_meta", "excerpt_stub"}
    for fn, meta in files_meta_by_name.items():
        if meta.get("role") not in known_roles:
            warnings.append(
                f"[role 未知] {fn}: role={meta.get('role')!r} は known set 外"
            )

    # レポート
    print(f"validate_corpus.py — {MANIFEST_PATH} の整合検証")
    print(f"  manifest_files: {len(manifest_set)}")
    print(f"  real_files:     {len(real_set)}")
    print()
    if errors:
        print(f"❌ ERROR: {len(errors)} 件")
        for e in errors:
            print(f"  {e}")
    else:
        print("✅ メカニカル整合性 OK（manifest と実ファイルがすべて一致）")

    if warnings:
        print()
        print(f"⚠️  WARNING: {len(warnings)} 件")
        for w in warnings:
            print(f"  {w}")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())

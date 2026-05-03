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
        for k, v in actual["char_counts"].items():
            mv = meta.get("char_counts", {}).get(k)
            if mv != v:
                errors.append(
                    f"[char_counts 不一致] {fn}.{k}: manifest={mv} actual={v}"
                )

        # data_status の bool 一致
        for k in ("kaimyo_excerpt", "kakikudashi", "gendaigoyaku", "genten"):
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

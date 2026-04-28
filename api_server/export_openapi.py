"""
api_server/export_openapi.py
============================

FastAPI app から OpenAPI スキーマを抽出し、

  - api_server/openapi.json
  - api_server/openapi.yaml

の 2 形式で書き出す。v1.9 で追加（候補 D・OpenAPI 整備）。

実行:

    python -m api_server.export_openapi
    # または
    cd api_server && python export_openapi.py

依存: pyyaml（spec yaml 出力に使用）。

PyYAML が無くても json は必ず出力する（yaml は ImportError でスキップ + warning）。
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Dict


def _patch_openapi(schema: Dict[str, Any]) -> Dict[str, Any]:
    """FastAPI 自動生成 OpenAPI に手動補強を入れる。

    - servers セクション（ローカル + 想定本番）
    - 代表的エンドポイントの response example
    - v1.8 拡張点（include_kaimyo_jukugo の理由）を operation description に追記
    """
    schema.setdefault("servers", [
        {"url": "http://127.0.0.1:8000", "description": "ローカル開発"},
        {"url": "https://buddhist-data-api.onrender.com", "description": "本番（Render・v1.10〜稼働中・X-API-Key 必須）"},
    ])

    # /api/houwa/citations の include_kaimyo_jukugo 拡張理由を強調
    paths = schema.get("paths", {}) or {}
    houwa = (paths.get("/api/houwa/citations") or {}).get("get")
    if houwa:
        extra = (
            "\n\n**spec §13.4 への拡張（v1.8 で追加）**：`include_kaimyo_jukugo` 既定 true。"
            "terms 索引は curated 19 件のみで、無常・智慧・慈悲・金剛 等の代表的"
            "テーマ語が kaimyo_jukugo（1971 件）にしか存在しないため、法話・諷誦文用途で"
            "実用に耐える（慈悲 → 29 篇 / 智慧 min_hits=3 → 16 篇）。spec 厳密準拠したい"
            "場合は false で抑止可能。"
        )
        houwa["description"] = (houwa.get("description") or "") + extra

    # /api/kaimyo/candidates の error 例を responses に追加
    kaimyo = (paths.get("/api/kaimyo/candidates") or {}).get("get")
    if kaimyo:
        responses = kaimyo.setdefault("responses", {})
        responses["400"] = {
            "description": "MISSING_PARAMETER / UNKNOWN_CHARACTERISTIC / INVALID_LENGTH",
            "content": {
                "application/json": {
                    "examples": {
                        "missing": {
                            "summary": "characteristics 未指定",
                            "value": {
                                "detail": {
                                    "error": "MISSING_PARAMETER",
                                    "message": "characteristics is required (csv)",
                                    "schema_version": "1.4.0",
                                }
                            },
                        },
                        "unknown": {
                            "summary": "未登録の特性",
                            "value": {
                                "detail": {
                                    "error": "UNKNOWN_CHARACTERISTIC",
                                    "message": "the following characteristic(s) are not in CHARACTERISTIC_TO_ICHIJI",
                                    "unknown": ["未知の特性"],
                                    "available": ["学問熱心", "温和", "信仰深い"],
                                    "schema_version": "1.4.0",
                                }
                            },
                        },
                        "invalid_length": {
                            "summary": "length が 2 / 4 以外",
                            "value": {
                                "detail": {
                                    "error": "INVALID_LENGTH",
                                    "message": "length must be 2 or 4 (or unspecified)",
                                    "schema_version": "1.4.0",
                                }
                            },
                        },
                    }
                }
            },
        }

    return schema


def export(out_dir: Path | None = None) -> Dict[str, Path]:
    """openapi.json + openapi.yaml を api_server/ 直下に出力。"""
    here = Path(__file__).resolve().parent
    out_dir = out_dir or here

    # FastAPI app を import（lazy import で循環回避）
    sys.path.insert(0, str(here.parent))
    try:
        from api_server.main import app
    except ImportError:
        from main import app  # type: ignore

    schema = app.openapi()
    schema = _patch_openapi(schema)

    out_json = out_dir / "openapi.json"
    out_yaml = out_dir / "openapi.yaml"

    out_json.write_text(json.dumps(schema, ensure_ascii=False, indent=2), encoding="utf-8")

    written: Dict[str, Path] = {"json": out_json}
    try:
        import yaml  # type: ignore

        out_yaml.write_text(
            yaml.safe_dump(schema, allow_unicode=True, sort_keys=False, width=200),
            encoding="utf-8",
        )
        written["yaml"] = out_yaml
    except ImportError:
        sys.stderr.write("[warn] PyYAML が見つからないため openapi.yaml はスキップ。`pip install pyyaml` を推奨。\n")

    return written


def main() -> int:
    written = export()
    for fmt, path in written.items():
        size = path.stat().st_size
        print(f"  wrote {fmt:4s}: {path}  ({size:,} bytes)")
    print(f"OK: exported {len(written)} file(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

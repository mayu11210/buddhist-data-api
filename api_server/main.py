"""
api_server/main.py
==================

kaimyo-app 連携 API（候補 D・v1.5 雛形）の FastAPI エントリポイント。

cross_index_spec.md §13 に基づき、9 エンドポイントのうち本セッション（v1.5）で
実装するのは以下：

  * GET /                      … サービスメタ
  * GET /health                … 簡易ヘルスチェック
  * GET /api/mappings          … api_mappings.json 全体
  * GET /api/篇/{idx}          … §13.6 統合 1 本（篇カルテ）

参照系 6 本（§13.5）と中核 2 本（§13.3 / §13.4）は v1.6〜v1.8 で順次実装。

起動:

    uvicorn api_server.main:app --reload --port 8000

ロード対象（仕様 §13.8.2 起動シーケンス）:

  1. data/mikkyou/index_shoryoshu_*.json（7 ファイル）
  2. data/kukai/shoryoshu_miyasaka.json
  3. data/mikkyou/api_mappings.json
"""

from __future__ import annotations

from typing import Any, Dict
from urllib.parse import unquote

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

try:
    from api_server.loaders import IndexStore, INDEX_FILES
except ImportError:
    # uvicorn を api_server ディレクトリ内から起動した場合のフォールバック
    from loaders import IndexStore, INDEX_FILES  # type: ignore

# --------------------------------------------------------------------------
# FastAPI アプリ + 起動時ロード
# --------------------------------------------------------------------------

app = FastAPI(
    title="Buddhist Data API",
    description=(
        "性霊集 横断索引化フェーズ B（候補 D）に基づく仏教資料 API。"
        "kaimyo-app など複数の仏教関連アプリから共有される知識バンクを"
        "横断検索可能なエンドポイント群として公開する。v1.5 雛形では"
        "/api/篇/{idx}（篇カルテ統合エンドポイント）を実装。"
    ),
    version="1.5.0",
)


@app.on_event("startup")
def _load_indices() -> None:
    """
    仕様 §13.8.2 起動シーケンスに従い、7 索引 + miyasaka.json + api_mappings.json
    をメモリへロードし、篇 idx 別の逆引き辞書を構築する。
    """
    app.state.store = IndexStore.load_default()


def _store() -> IndexStore:
    """app.state.store を取得（型ヒント付き）。"""
    store: IndexStore = getattr(app.state, "store", None)
    if store is None:  # 通常はテスト等で startup を回避した場合のみ
        store = IndexStore.load_default()
        app.state.store = store
    return store


# --------------------------------------------------------------------------
# ルートとヘルス
# --------------------------------------------------------------------------

@app.get("/")
def root() -> Dict[str, Any]:
    store = _store()
    return {
        "service": "buddhist-data-api",
        "version": "1.5.0",
        "schema_version": store.schema_version,
        "loaded_indices": list(INDEX_FILES.keys()),
        "miyasaka_entries": len(store.miyasaka),
        "mappings": {
            "characteristic_to_ichiji": len(store.api_mappings.get("characteristic_to_ichiji", {}) or {}),
            "theme_expansion": len(store.api_mappings.get("theme_expansion", {}) or {}),
        },
        "endpoints": [
            "GET /",
            "GET /health",
            "GET /api/mappings",
            "GET /api/篇/{idx}",
        ],
        "spec": "_dev_references/cross_index_spec.md §13",
    }


@app.get("/health")
def health() -> Dict[str, str]:
    return {"status": "ok"}


@app.get("/api/mappings")
def get_mappings() -> Dict[str, Any]:
    """v1.4 で確定したマッピング 2 表（CHARACTERISTIC_TO_ICHIJI + THEME_EXPANSION）を返す。"""
    return _store().api_mappings


# --------------------------------------------------------------------------
# /api/篇/{idx} （§13.6 統合 1 本）
# --------------------------------------------------------------------------

# FastAPI は path に日本語（"篇"）を含めても OK だが、URL エンコード経由でも
# 確実に届くよう英語別名 /api/hen/{idx} も同居させる（共有性を高めるため）。

@app.get("/api/篇/{idx}")
@app.get("/api/hen/{idx}")
def get_篇(
    idx: int,
    excerpt_chars: int = Query(300, ge=0, le=5000, description="書き下し・訳の冒頭抜粋字数"),
    include_full_text: bool = Query(False, description="true で書き下し + 訳の全文を含める"),
) -> Any:
    """
    篇 idx（0..111）に対する全索引ヒットを統合した「篇カルテ」を返す。

    `include_full_text=false` 既定。`true` にすると `full_text.kakikudashi`
    `full_text.gendaigoyaku` に全文を載せる（最大 8 KB 程度／篇）。
    """
    store = _store()
    try:
        return store.build_篇_card(
            idx=idx,
            excerpt_chars=excerpt_chars,
            include_full_text=include_full_text,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


# --------------------------------------------------------------------------
# 開発用直接起動（python -m api_server.main）
# --------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server.main:app", host="127.0.0.1", port=8000, reload=False)

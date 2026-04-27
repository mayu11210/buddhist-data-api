"""
api_server/main.py
==================

kaimyo-app 連携 API（候補 D・v1.6 昇格）の FastAPI エントリポイント。

cross_index_spec.md §13 に基づき、9 エンドポイントのうち本実装で動くのは：

  v1.5（前回）:
    * GET /                      … サービスメタ
    * GET /health                … 簡易ヘルスチェック
    * GET /api/mappings          … api_mappings.json 全体
    * GET /api/篇/{idx}          … §13.6 統合 1 本（篇カルテ）

  v1.6（本回追加）:
    * GET /api/term/{key}         … §13.5 詳細参照系 6 本
    * GET /api/person/{key}
    * GET /api/place/{key}
    * GET /api/citation/{key}
    * GET /api/sanskrit/{key}
    * GET /api/kukai-work/{key}

中核 2 本（§13.3 /api/kaimyo/candidates・§13.4 /api/houwa/citations）は
v1.7・v1.8 で順次実装。

起動:

    uvicorn api_server.main:app --reload --port 8000

起動シーケンス（仕様 §13.8.2）:

  1. data/mikkyou/index_shoryoshu_*.json（7 ファイル）をロード
  2. data/kukai/shoryoshu_miyasaka.json をロード
  3. data/mikkyou/api_mappings.json をロード
  4. 共起マトリックス（§13.7.3）を構築
  5. alias_to_canonical / 篇 idx 別逆引きを構築
"""

from __future__ import annotations

from typing import Any, Dict
from urllib.parse import unquote

from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse

try:
    from api_server.loaders import IndexStore, INDEX_FILES, CO_OCCURRENCE_PAIRS
except ImportError:
    # uvicorn を api_server ディレクトリ内から起動した場合のフォールバック
    from loaders import IndexStore, INDEX_FILES, CO_OCCURRENCE_PAIRS  # type: ignore

# --------------------------------------------------------------------------
# FastAPI アプリ + 起動時ロード
# --------------------------------------------------------------------------

app = FastAPI(
    title="Buddhist Data API",
    description=(
        "性霊集 横断索引化フェーズ B（候補 D）に基づく仏教資料 API。"
        "kaimyo-app など複数の仏教関連アプリから共有される知識バンクを"
        "横断検索可能なエンドポイント群として公開する。v1.6 で詳細参照系 "
        "6 本（/api/term, /api/person, /api/place, /api/citation, "
        "/api/sanskrit, /api/kukai-work）と共起マトリックス前計算を追加。"
    ),
    version="1.6.0",
)


@app.on_event("startup")
def _load_indices() -> None:
    """
    仕様 §13.8.2 起動シーケンスに従い、7 索引 + miyasaka.json + api_mappings.json
    をメモリへロードし、篇 idx 別の逆引き辞書 + 共起マトリックス + alias 逆引きを
    すべて起動時に前計算する。
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
    co_pairs_total = sum(
        len(mat) for mat in store.co_occurrence.values()
    )
    return {
        "service": "buddhist-data-api",
        "version": "1.6.0",
        "schema_version": store.schema_version,
        "loaded_indices": list(INDEX_FILES.keys()),
        "miyasaka_entries": len(store.miyasaka),
        "mappings": {
            "characteristic_to_ichiji": len(store.api_mappings.get("characteristic_to_ichiji", {}) or {}),
            "theme_expansion":          len(store.api_mappings.get("theme_expansion", {}) or {}),
        },
        "alias_to_canonical_keys": {
            k: len(v) for k, v in store.alias_to_canonical.items()
        },
        "co_occurrence_pairs_precomputed": [list(p) for p in CO_OCCURRENCE_PAIRS],
        "co_occurrence_total_rows": co_pairs_total,
        "endpoints": [
            "GET /",
            "GET /health",
            "GET /api/mappings",
            "GET /api/篇/{idx}",
            "GET /api/term/{key}",
            "GET /api/person/{key}",
            "GET /api/place/{key}",
            "GET /api/citation/{key}",
            "GET /api/sanskrit/{key}",
            "GET /api/kukai-work/{key}",
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
# /api/篇/{idx} （§13.6 統合 1 本・v1.5 から継続）
# --------------------------------------------------------------------------

@app.get("/api/篇/{idx}")
@app.get("/api/hen/{idx}")
def get_篇(
    idx: int,
    excerpt_chars: int = Query(300, ge=0, le=5000, description="書き下し・訳の冒頭抜粋字数"),
    include_full_text: bool = Query(False, description="true で書き下し + 訳の全文を含める"),
) -> Any:
    """篇 idx（0..111）に対する全索引ヒットを統合した「篇カルテ」を返す。"""
    store = _store()
    try:
        return store.build_篇_card(
            idx=idx,
            excerpt_chars=excerpt_chars,
            include_full_text=include_full_text,
        )
    except ValueError as e:
        raise HTTPException(status_code=404, detail={"error": "NOT_FOUND", "message": str(e), "schema_version": store.schema_version})


# --------------------------------------------------------------------------
# /api/term, /person, /place, /citation, /sanskrit, /kukai-work
# （§13.5 詳細参照系 6 本・v1.6 で新規追加）
# --------------------------------------------------------------------------

def _build_reference_or_404(endpoint: str, key: str, full_context: bool, top_n: int) -> Any:
    """6 エンドポイント共通の参照系ハンドラ。alias 解決 + 共起 + 関連索引を返す。"""
    store = _store()
    # path から URL デコードされた値が来る前提だが、念のため二重デコード許容
    key_decoded = unquote(key)
    try:
        return store.build_reference(
            endpoint=endpoint,
            key=key_decoded,
            full_context=full_context,
            top_n=top_n,
        )
    except KeyError as e:
        msg = str(e).strip("'\"")
        if msg.startswith("UNKNOWN_ENDPOINT"):
            raise HTTPException(
                status_code=400,
                detail={"error": "UNKNOWN_ENDPOINT", "endpoint": endpoint, "schema_version": store.schema_version},
            )
        raise HTTPException(
            status_code=404,
            detail={
                "error": "NOT_FOUND",
                "endpoint": endpoint,
                "key": key_decoded,
                "schema_version": store.schema_version,
            },
        )


@app.get("/api/term/{key:path}")
def get_term(
    key: str,
    full_context: bool = Query(False, description="true で occurrences を全件返す"),
    top_n: int = Query(10, ge=1, le=100, description="related ブロック各カテゴリの上限件数"),
) -> Any:
    """密教教学用語（terms 索引）の詳細参照。共起する人名・地名・典故・戒名熟語を同梱。"""
    return _build_reference_or_404("terms", key, full_context, top_n)


@app.get("/api/person/{key:path}")
def get_person(
    key: str,
    full_context: bool = Query(False),
    top_n: int = Query(10, ge=1, le=100),
) -> Any:
    """人名（persons 索引）の詳細参照。alias / matched_form でも引ける。"""
    return _build_reference_or_404("persons", key, full_context, top_n)


@app.get("/api/place/{key:path}")
def get_place(
    key: str,
    full_context: bool = Query(False),
    top_n: int = Query(10, ge=1, le=100),
) -> Any:
    """地名（places 索引）の詳細参照。alias / matched_form でも引ける。"""
    return _build_reference_or_404("places", key, full_context, top_n)


@app.get("/api/citation/{key:path}")
def get_citation(
    key: str,
    full_context: bool = Query(False),
    top_n: int = Query(10, ge=1, le=100),
) -> Any:
    """典故書名（citations 索引）の詳細参照。aliases でも引ける。"""
    return _build_reference_or_404("citations", key, full_context, top_n)


@app.get("/api/sanskrit/{key:path}")
def get_sanskrit(
    key: str,
    full_context: bool = Query(False),
    top_n: int = Query(10, ge=1, le=100),
) -> Any:
    """梵語 IAST（sanskrit 索引）の詳細参照。漢訳熟語との対応も related に同梱。"""
    return _build_reference_or_404("sanskrit", key, full_context, top_n)


@app.get("/api/kukai-work/{key:path}")
@app.get("/api/kukai_work/{key:path}")
def get_kukai_work(
    key: str,
    full_context: bool = Query(False),
    top_n: int = Query(10, ge=1, le=100),
) -> Any:
    """空海著作（kukai_works 索引）の詳細参照。"""
    return _build_reference_or_404("kukai_works", key, full_context, top_n)


# --------------------------------------------------------------------------
# 開発用直接起動（python -m api_server.main）
# --------------------------------------------------------------------------

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("api_server.main:app", host="127.0.0.1", port=8000, reload=False)

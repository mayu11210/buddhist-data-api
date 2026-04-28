"""
api_server/tests/test_e2e_uvicorn.py
=====================================

実 uvicorn を subprocess で起動し、httpx で実 HTTP 経由で代表ルートを叩く smoke test。

TestClient は in-process なので ASGI を介さない最後の絞り込み（reverse proxy 越し挙動・
Unicode path・middleware など）は実 uvicorn でしか確認できない。本テストはそのカバレッジ。

実行:

    cd buddhist-data-api
    pytest api_server/tests/test_e2e_uvicorn.py -v

実行環境に uvicorn が無い / port 8765 が使用中等の場合は pytest.skip。
"""

from __future__ import annotations

import urllib.parse

import pytest

httpx = pytest.importorskip("httpx")


def test_e2e_root(live_url):
    r = httpx.get(f"{live_url}/", timeout=10.0)
    assert r.status_code == 200
    assert r.json()["version"] == "1.10.0"


def test_e2e_health(live_url):
    r = httpx.get(f"{live_url}/health", timeout=5.0)
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_e2e_hen_card_unicode_path(live_url):
    """Unicode path /api/篇/0 が実 HTTP 経由でも解決できる"""
    # urllib.parse は既定で Unicode を percent-encode する
    path = urllib.parse.quote("/api/篇/0", safe="/")
    r = httpx.get(f"{live_url}{path}", timeout=10.0)
    assert r.status_code == 200
    assert r.json()["shoryoshu_idx"] == 0


def test_e2e_kaimyo_candidates(live_url):
    r = httpx.get(
        f"{live_url}/api/kaimyo/candidates",
        params={"characteristics": "学問熱心,温和", "limit": 3},
        timeout=10.0,
    )
    assert r.status_code == 200
    body = r.json()
    assert 1 <= len(body["results"]) <= 3


def test_e2e_houwa_citations_即身成仏(live_url):
    r = httpx.get(
        f"{live_url}/api/houwa/citations",
        params={"theme": "即身成仏", "limit": 1},
        timeout=10.0,
    )
    assert r.status_code == 200
    body = r.json()
    assert body["citations"][0]["shoryoshu_idx"] == 59


def test_e2e_openapi_json(live_url):
    r = httpx.get(f"{live_url}/openapi.json", timeout=10.0)
    assert r.status_code == 200
    schema = r.json()
    assert schema["info"]["version"] == "1.10.0"
    # tags 5 グループが付与されている
    tag_names = {t["name"] for t in schema.get("tags", [])}
    assert tag_names >= {"Meta", "篇カルテ", "詳細参照系", "戒名候補", "法話典故"}


def test_e2e_swagger_ui(live_url):
    """Swagger UI HTML がレスポンスされる（FastAPI 既定 /docs）"""
    r = httpx.get(f"{live_url}/docs", timeout=10.0)
    assert r.status_code == 200
    assert "Swagger" in r.text or "swagger" in r.text

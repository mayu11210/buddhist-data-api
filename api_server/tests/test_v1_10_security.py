"""
api_server/tests/test_v1_10_security.py
========================================

v1.10 セキュリティ強化（APIキー認証 / CORS / 検索エンジン除け）の検証。

実行:

    cd buddhist-data-api
    pytest api_server/tests/test_v1_10_security.py -v

期待される挙動:

  - BUDDHIST_API_KEY 未設定（ローカル / 既存テスト）→ 認証スキップ・全部通る
  - BUDDHIST_API_KEY 設定済 → 公開ルート以外は X-API-Key 必須
  - 全レスポンスに X-Robots-Tag: noindex, nofollow が付く
  - /robots.txt で Disallow: / が返る
"""

from __future__ import annotations


# ============================================================
# 共通：noindex ヘッダーは認証ありなしを問わず常に付く
# ============================================================

def test_noindex_header_on_health(client):
    """/health のレスポンスに X-Robots-Tag が付く（認証スキップでも）。"""
    r = client.get("/health")
    assert r.status_code == 200
    assert r.headers.get("X-Robots-Tag") == "noindex, nofollow"


def test_noindex_header_on_root(client):
    r = client.get("/")
    assert r.status_code == 200
    assert r.headers.get("X-Robots-Tag") == "noindex, nofollow"


def test_robots_txt(client):
    """/robots.txt が Disallow: / を返す。"""
    r = client.get("/robots.txt")
    assert r.status_code == 200
    body = r.text.strip().splitlines()
    assert body[0].startswith("User-agent: *")
    assert any(line.startswith("Disallow: /") for line in body)
    assert r.headers.get("X-Robots-Tag") == "noindex, nofollow"


# ============================================================
# 認証スキップ系：BUDDHIST_API_KEY 未設定状態（既存テストと同じ）
# ============================================================

def test_auth_disabled_when_no_key(client):
    """既定（API_KEY 未設定）では保護対象も 200。既存テスト互換性確認。"""
    r = client.get("/api/篇/0")
    assert r.status_code == 200
    assert r.json()["shoryoshu_idx"] == 0


# ============================================================
# 認証必須系：API_KEY を一時的に有効化して挙動確認
# （middleware は module global API_KEY を late-binding で参照するので
#  monkeypatch で安全にテスト可能）
# ============================================================

def test_auth_required_when_key_set_returns_401(client, monkeypatch):
    """API_KEY 有効化中、X-API-Key 無しで保護ルートを叩くと 401。"""
    monkeypatch.setattr("api_server.main.API_KEY", "test-secret-key-v1-10")
    r = client.get("/api/篇/0")
    assert r.status_code == 401
    body = r.json()
    assert body["error"] == "UNAUTHORIZED"


def test_auth_required_with_correct_key_returns_200(client, monkeypatch):
    """正しい X-API-Key を送れば保護ルートも 200。"""
    monkeypatch.setattr("api_server.main.API_KEY", "test-secret-key-v1-10")
    r = client.get(
        "/api/篇/0",
        headers={"X-API-Key": "test-secret-key-v1-10"},
    )
    assert r.status_code == 200
    assert r.json()["shoryoshu_idx"] == 0


def test_auth_required_with_wrong_key_returns_401(client, monkeypatch):
    """間違った X-API-Key は 401。"""
    monkeypatch.setattr("api_server.main.API_KEY", "test-secret-key-v1-10")
    r = client.get(
        "/api/篇/0",
        headers={"X-API-Key": "WRONG-KEY"},
    )
    assert r.status_code == 401


def test_auth_skipped_paths_always_open(client, monkeypatch):
    """API_KEY 有効化中でも、公開パスは認証不要。"""
    monkeypatch.setattr("api_server.main.API_KEY", "test-secret-key-v1-10")
    for path in ["/", "/health", "/robots.txt", "/openapi.json"]:
        r = client.get(path)
        assert r.status_code == 200, f"{path} should be open without auth"


def test_auth_protected_endpoints(client, monkeypatch):
    """主要 API ルートが認証必須になっていることを横断確認。"""
    monkeypatch.setattr("api_server.main.API_KEY", "test-secret-key-v1-10")
    protected = [
        "/api/mappings",
        "/api/篇/0",
        "/api/term/三密",
        "/api/person/空海",
        "/api/place/高野山",
        "/api/citation/荘子",
        "/api/kukai-work/性霊集",
        "/api/kaimyo/candidates?characteristics=温和",
        "/api/houwa/citations?theme=慈悲",
    ]
    for path in protected:
        r = client.get(path)
        assert r.status_code == 401, f"{path} should require auth, got {r.status_code}"

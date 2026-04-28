"""
api_server/tests/test_integration.py
=====================================

v1.9 結合テスト（TestClient ベース・in-process・全 14 ルート + 主要エラー系）。

実行:

    cd buddhist-data-api
    pytest api_server/tests/test_integration.py -v

期待値の根拠は `引き継ぎメモ_2026-04-28_kaimyo_api_v17_v18_全9本完了.md` 参照：

  - 慈悲 → 29 篇 / 智慧 min_hits=3 → 16 篇
  - 学問熱心+温和 → 9 篇 マッチ
  - 即身成仏 → idx=59 即身成仏義本文を rank=1 抽出
"""

from __future__ import annotations

import urllib.parse


# ============================================================
# Meta（GET / / /health / /api/mappings）
# ============================================================

def test_root_returns_meta(client):
    r = client.get("/")
    assert r.status_code == 200
    body = r.json()
    assert body["service"] == "buddhist-data-api"
    assert body["version"] == "1.9.0"
    # 全 7 索引
    assert sorted(body["loaded_indices"]) == sorted([
        "terms", "citations", "sanskrit", "kaimyo_jukugo",
        "persons", "places", "kukai_works",
    ])
    # マッピング 2 表が読まれている
    assert body["mappings"]["characteristic_to_ichiji"] >= 10
    assert body["mappings"]["theme_expansion"] >= 5
    # 共起マトリックス前計算 7 ペア
    assert len(body["co_occurrence_pairs_precomputed"]) == 7


def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_get_mappings(client):
    r = client.get("/api/mappings")
    assert r.status_code == 200
    body = r.json()
    cti = body.get("characteristic_to_ichiji") or {}
    te = body.get("theme_expansion") or {}
    # CHARACTERISTIC_TO_ICHIJI に「学問熱心」「温和」が必ず存在
    assert "学問熱心" in cti
    assert "温和" in cti
    # THEME_EXPANSION に「無常」「慈悲」「智慧」が必ず存在
    for k in ("無常", "慈悲", "智慧"):
        assert k in te, f"theme_expansion missing key: {k}"


# ============================================================
# 篇カルテ（GET /api/篇/{idx} と alias /api/hen/{idx}）
# ============================================================

def test_hen_card_idx_0(client):
    r = client.get("/api/hen/0?excerpt_chars=120")
    assert r.status_code == 200
    body = r.json()
    assert body["shoryoshu_idx"] == 0
    assert isinstance(body["篇名"], str)
    assert len(body["excerpts"]["kakikudashi_head"]) <= 120
    assert "indices" in body
    assert set(body["indices"].keys()) >= {
        "terms", "citations", "sanskrit", "kaimyo_jukugo",
        "persons", "places", "kukai_works",
    }


def test_hen_card_idx_106_full_text(client):
    r = client.get("/api/hen/106?include_full_text=true")
    assert r.status_code == 200
    body = r.json()
    assert body["shoryoshu_idx"] == 106
    assert "full_text" in body
    assert isinstance(body["full_text"]["kakikudashi"], str)
    assert isinstance(body["full_text"]["gendaigoyaku"], str)
    assert body["字数"]["書き下し"] > 0


def test_hen_card_unicode_path(client):
    """日本語パス /api/篇/1 の解決（ASCII alias と一致するか）"""
    # httpx は自動で URL エンコードするはず
    r = client.get("/api/篇/1")
    assert r.status_code == 200
    assert r.json()["shoryoshu_idx"] == 1


def test_hen_card_out_of_range_404(client):
    r = client.get("/api/hen/999")
    assert r.status_code == 404
    detail = r.json()["detail"]
    assert detail["error"] == "NOT_FOUND"


# ============================================================
# 詳細参照系 6 本
# ============================================================

def test_term_三密(client):
    r = client.get("/api/term/三密?top_n=5")
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["endpoint"] == "terms"
    assert body["query"]["canonical"] == "三密"
    related_keys = set(body["related"].keys())
    assert "co_occurring_kaimyo_jukugo" in related_keys
    assert "co_occurring_persons" in related_keys
    assert "co_occurring_places" in related_keys


def test_person_alias_弘法大師_to_空海(client):
    """alias 解決：弘法大師 → 空海"""
    r = client.get("/api/person/弘法大師?top_n=5")
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["canonical"] == "空海"
    # alias_matched は bool（True = alias 経由）/ 元キーは query.key に保存
    assert body["query"]["alias_matched"] is True
    assert body["query"]["key"] == "弘法大師"


def test_place_高野山(client):
    r = client.get("/api/place/高野山")
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["canonical"] == "高野山"
    assert "related" in body


def test_citation_荘子(client):
    r = client.get("/api/citation/荘子?top_n=5")
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["endpoint"] == "citations"


def test_sanskrit_prajna_iast(client):
    """IAST 文字 prajñā を URL エンコード経由で引く"""
    key = urllib.parse.quote("prajñā")
    r = client.get(f"/api/sanskrit/{key}?top_n=5")
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["endpoint"] == "sanskrit"


def test_kukai_work_梵字悉曇字母并びに釈義(client):
    r = client.get("/api/kukai-work/梵字悉曇字母并びに釈義")
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["endpoint"] == "kukai_works"


def test_kukai_work_alias_underscore(client):
    """ASCII alias /api/kukai_work/{key} も動く（include_in_schema=False）"""
    r = client.get("/api/kukai_work/梵字悉曇字母并びに釈義")
    assert r.status_code == 200


def test_term_not_found_404(client):
    r = client.get("/api/term/絶対に存在しない教学用語ZZZ")
    assert r.status_code == 404
    assert r.json()["detail"]["error"] == "NOT_FOUND"


# ============================================================
# 中核 1：/api/kaimyo/candidates
# ============================================================

def test_kaimyo_candidates_学問熱心_温和(client):
    """学問熱心 + 温和 → 9 篇マッチ（引き継ぎメモ）"""
    r = client.get(
        "/api/kaimyo/candidates",
        params={"characteristics": "学問熱心,温和", "limit": 5},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["characteristics"] == ["学問熱心", "温和"]
    assert isinstance(body["results"], list)
    assert 1 <= len(body["results"]) <= 5
    # 上位は final_score 降順
    scores = [r["final_score"] for r in body["results"]]
    assert scores == sorted(scores, reverse=True)
    # rank が 1 始まりで連続
    ranks = [r["rank"] for r in body["results"]]
    assert ranks == list(range(1, len(ranks) + 1))


def test_kaimyo_candidates_prefer_persons_bonus(client):
    """prefer_persons=空海 で +5 の bonus が乗ること"""
    r = client.get(
        "/api/kaimyo/candidates",
        params={
            "characteristics": "学問熱心,温和",
            "prefer_persons": "空海",
            "limit": 5,
        },
    )
    assert r.status_code == 200
    body = r.json()
    assert "空海" in body["query"]["prefer_persons"]
    # 少なくとも 1 件は bonus_score > 0
    assert any(r["bonus_score"] > 0 for r in body["results"])


def test_kaimyo_candidates_length_filter(client):
    """length=4 で全結果が 4 字熟語"""
    r = client.get(
        "/api/kaimyo/candidates",
        params={"characteristics": "信仰深い", "length": 4, "limit": 10},
    )
    assert r.status_code == 200
    for c in r.json()["results"]:
        assert c["length"] == 4
        assert len(c["jukugo"]) == 4


def test_kaimyo_candidates_missing_param_400(client):
    r = client.get("/api/kaimyo/candidates")
    assert r.status_code == 400
    assert r.json()["detail"]["error"] == "MISSING_PARAMETER"


def test_kaimyo_candidates_unknown_characteristic_400(client):
    r = client.get(
        "/api/kaimyo/candidates",
        params={"characteristics": "未知の特性XYZ"},
    )
    assert r.status_code == 400
    detail = r.json()["detail"]
    assert detail["error"] == "UNKNOWN_CHARACTERISTIC"
    assert "未知の特性XYZ" in detail["unknown"]
    assert isinstance(detail["available"], list) and len(detail["available"]) > 0


def test_kaimyo_candidates_invalid_length_400(client):
    r = client.get(
        "/api/kaimyo/candidates",
        params={"characteristics": "学問熱心", "length": 3},
    )
    assert r.status_code == 400
    assert r.json()["detail"]["error"] == "INVALID_LENGTH"


# ============================================================
# 中核 2：/api/houwa/citations
# ============================================================

def test_houwa_citations_慈悲_29篇(client):
    """慈悲 → 29 篇マッチ（引き継ぎメモの期待値・min_hits=1 既定）"""
    r = client.get(
        "/api/houwa/citations",
        params={"theme": "慈悲", "limit": 50},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["theme"] == "慈悲"
    assert body["query"]["is_known_theme"] is True
    # 引き継ぎメモ：慈悲 → 29 篇
    assert body["metadata"]["total_篇_matched"] == 29


def test_houwa_citations_智慧_min_hits_3_16篇(client):
    """智慧 min_hits=3 → 16 篇（引き継ぎメモ）"""
    r = client.get(
        "/api/houwa/citations",
        params={"theme": "智慧", "min_hits": 3, "limit": 50},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["metadata"]["total_篇_matched"] == 16


def test_houwa_citations_即身成仏_rank1_idx59(client):
    """即身成仏 → idx=59 即身成仏義本文を rank=1 抽出（引き継ぎメモ）"""
    r = client.get(
        "/api/houwa/citations",
        params={"theme": "即身成仏", "limit": 5},
    )
    assert r.status_code == 200
    body = r.json()
    assert len(body["citations"]) >= 1
    top = body["citations"][0]
    assert top["rank"] == 1
    assert top["shoryoshu_idx"] == 59


def test_houwa_citations_expand_false(client):
    """expand=false で expanded_terms はテーマ語のみ"""
    r = client.get(
        "/api/houwa/citations",
        params={"theme": "慈悲", "expand": False, "limit": 3},
    )
    assert r.status_code == 200
    body = r.json()
    assert body["query"]["expanded_terms"] == ["慈悲"]


def test_houwa_citations_include_kaimyo_jukugo_false_strict_spec(client):
    """include_kaimyo_jukugo=false で spec §13.4 厳密準拠 → 慈悲が 0 篇近くになる"""
    r = client.get(
        "/api/houwa/citations",
        params={"theme": "慈悲", "include_kaimyo_jukugo": False, "limit": 50},
    )
    assert r.status_code == 200
    body = r.json()
    # 厳密準拠だと 29 篇から大幅減（kaimyo_jukugo にしか無いテーマ語のため）
    assert body["metadata"]["total_篇_matched"] < 29


def test_houwa_citations_excerpt_radius(client):
    """excerpt_radius=300 で context_excerpt が 600 字程度"""
    r = client.get(
        "/api/houwa/citations",
        params={"theme": "即身成仏", "excerpt_radius": 300, "limit": 1},
    )
    assert r.status_code == 200
    body = r.json()
    assert len(body["citations"]) == 1
    # ±300 字 = 約 600 字以内
    assert len(body["citations"][0]["context_excerpt"]) <= 600


def test_houwa_citations_missing_param_400(client):
    r = client.get("/api/houwa/citations")
    assert r.status_code == 400
    assert r.json()["detail"]["error"] == "MISSING_PARAMETER"


# ============================================================
# OpenAPI スキーマ自体の妥当性
# ============================================================

def test_openapi_schema_is_well_formed(client):
    r = client.get("/openapi.json")
    assert r.status_code == 200
    schema = r.json()
    assert schema["info"]["version"] == "1.9.0"
    assert schema["info"]["title"] == "Buddhist Data API"
    # tags メタ 5 グループ
    tag_names = {t["name"] for t in schema.get("tags", [])}
    assert tag_names >= {"Meta", "篇カルテ", "詳細参照系", "戒名候補", "法話典故"}
    # alias 2 本（/api/hen/{idx}, /api/kukai_work/{key}）は include_in_schema=False で隠れている
    paths = set(schema.get("paths", {}).keys())
    assert "/api/hen/{idx}" not in paths
    assert "/api/kukai_work/{key}" not in paths
    # 主要 12 ルートは public
    for must_have in [
        "/", "/health", "/api/mappings",
        "/api/篇/{idx}",
        "/api/term/{key}", "/api/person/{key}", "/api/place/{key}",
        "/api/citation/{key}", "/api/sanskrit/{key}", "/api/kukai-work/{key}",
        "/api/kaimyo/candidates", "/api/houwa/citations",
    ]:
        assert must_have in paths, f"OpenAPI paths missing: {must_have}"

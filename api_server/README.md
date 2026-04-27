# api_server/

性霊集 横断索引化フェーズ B（候補 D）の kaimyo-app 連携 API。
仕様: `_dev_references/cross_index_spec.md` §13。

## v1.5 で実装済

- `GET /` … サービスメタ
- `GET /health` … 簡易ヘルスチェック
- `GET /api/mappings` … `data/mikkyou/api_mappings.json` 全体
- `GET /api/篇/{idx}` (alias: `/api/hen/{idx}`) … 篇カルテ統合エンドポイント（§13.6）

## v1.6 以降の予定

- v1.6: `/api/term`, `/api/person`, `/api/place`, `/api/citation`, `/api/sanskrit`, `/api/kukai-work` + 共起マトリックス
- v1.7: `/api/kaimyo/candidates`（中核 1）
- v1.8: `/api/houwa/citations`（中核 2）
- v1.9: OpenAPI yaml 整備 + kaimyo-app 結合テスト + デプロイ

## ローカル起動

```bash
pip install -r api_server/requirements.txt
uvicorn api_server.main:app --reload --port 8000
```

## curl で動作確認

```bash
curl -s 'http://127.0.0.1:8000/health'
curl -s 'http://127.0.0.1:8000/'
curl -s 'http://127.0.0.1:8000/api/hen/1?excerpt_chars=120' | jq .
curl -s 'http://127.0.0.1:8000/api/hen/106?include_full_text=false&excerpt_chars=300' | jq '.字数, .totals'
```

## 起動時ロード

1. `data/mikkyou/index_shoryoshu_*.json`（7 ファイル）
2. `data/kukai/shoryoshu_miyasaka.json`
3. `data/mikkyou/api_mappings.json`

総メモリ概算 15〜20 MB（仕様 §13.8.2）。

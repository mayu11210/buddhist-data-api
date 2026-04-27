# api_server/

性霊集 横断索引化フェーズ B（候補 D）の kaimyo-app 連携 API。
仕様: `_dev_references/cross_index_spec.md` §13。

## v1.5 で実装済

- `GET /` … サービスメタ
- `GET /health` … 簡易ヘルスチェック
- `GET /api/mappings` … `data/mikkyou/api_mappings.json` 全体
- `GET /api/篇/{idx}` (alias: `/api/hen/{idx}`) … 篇カルテ統合エンドポイント（§13.6）

## v1.6 で追加

- `GET /api/term/{key}` … 密教教学用語（terms 索引）の詳細参照
- `GET /api/person/{key}` … 人名（persons 索引）の詳細参照（alias / matched_form でも引ける）
- `GET /api/place/{key}` … 地名（places 索引）の詳細参照（alias / matched_form でも引ける）
- `GET /api/citation/{key}` … 典故書名（citations 索引）の詳細参照（aliases でも引ける）
- `GET /api/sanskrit/{key}` … 梵語 IAST（sanskrit 索引）の詳細参照（aliases.form でも引ける）
- `GET /api/kukai-work/{key}` (alias: `/api/kukai_work/{key}`) … 空海著作（kukai_works 索引）の詳細参照
- 起動時前計算：共起マトリックス 7 ペア（§13.7.3）+ 派生 6 ペア・alias_to_canonical 逆引き辞書

## v1.7 で追加

- `GET /api/kaimyo/candidates` … 中核 1・故人特性 → 戒名候補生成（§13.3）
  - クエリ: `characteristics`（必須・csv）/ `min_score`（既定 30）/ `limit`（既定 20）/
    `include_review`（既定 false）/ `prefer_persons` / `prefer_places`（共起篇 1 つにつき +0.5・最大 +5）/
    `length`（2 または 4・未指定で両方）
  - 内部フロー: Step 1（CHARACTERISTIC_TO_ICHIJI 解決）→ Step 2（kaimyo_chars × ICHIJI_SET 積集合 + min_score + review + length フィルタ）
    → Step 3（prefer_persons・prefer_places 共起ボーナス）→ Step 4（出典文最多 4 件・梵語原語 sanskrit 索引照合・関連人物上位 5・関連地名上位 3）
    → Step 5（final_score = kaimyo_score + bonus_score 降順 + limit 切詰）
  - エラー: `MISSING_PARAMETER`（characteristics 空・400）/ `UNKNOWN_CHARACTERISTIC`（未登録キー・400・available 同梱）/ `INVALID_LENGTH`（2 / 4 以外・400）

## v1.8 以降の予定

- v1.8: `/api/houwa/citations`（中核 2・THEME_EXPANSION + 篇スコアリング + context 抜粋）
- v1.9: OpenAPI yaml 整備 + kaimyo-app 結合テスト + デプロイ

## ローカル起動

```bash
pip install -r api_server/requirements.txt
uvicorn api_server.main:app --reload --port 8000
```

`/docs`（Swagger UI）が http://127.0.0.1:8000/docs に自動生成される。

## curl で動作確認

### v1.5 系（篇カルテ）

```bash
curl -s 'http://127.0.0.1:8000/health'
curl -s 'http://127.0.0.1:8000/'
curl -s 'http://127.0.0.1:8000/api/hen/1?excerpt_chars=120' | jq .
curl -s 'http://127.0.0.1:8000/api/hen/106?include_full_text=false' | jq '.字数, .totals'
```

### v1.6 系（参照系 6 本）

```bash
# 密教教学用語
curl -s 'http://127.0.0.1:8000/api/term/三密?top_n=5' | jq '.query, (.related | keys)'

# 人名（alias 解決例：弘法大師 → 空海 で引く）
curl -s 'http://127.0.0.1:8000/api/person/弘法大師?top_n=5' | jq '.query'
curl -s 'http://127.0.0.1:8000/api/person/空海?top_n=10' | jq '.related.co_occurring_persons'

# 地名
curl -s 'http://127.0.0.1:8000/api/place/高野山' | jq '.related'

# 典故書名
curl -s 'http://127.0.0.1:8000/api/citation/荘子?top_n=5' | jq '.metadata, (.related | keys)'

# 梵語 IAST（IAST 文字を URL エンコードして渡す）
curl -s --data-urlencode 'top_n=5' \
  -G 'http://127.0.0.1:8000/api/sanskrit/prajñā' | jq '.related.related_kaimyo_jukugo_via_sanskrit_origins'

# 空海著作
curl -s 'http://127.0.0.1:8000/api/kukai-work/梵字悉曇字母并びに釈義' | jq '.entry'
```

### v1.7 系（戒名候補生成）

```bash
# 学問熱心 + 温和 → 上位 5 件（matched_ichiji + final_score を見る）
curl -s -G 'http://127.0.0.1:8000/api/kaimyo/candidates' \
  --data-urlencode 'characteristics=学問熱心,温和' \
  --data-urlencode 'limit=5' | jq '.query, (.results[] | {rank, jukugo, final_score, matched_ichiji})'

# prefer_persons / prefer_places 共起ボーナス（弘法大師→空海 alias 解決）
curl -s -G 'http://127.0.0.1:8000/api/kaimyo/candidates' \
  --data-urlencode 'characteristics=温和' \
  --data-urlencode 'prefer_persons=弘法大師,大日如来' \
  --data-urlencode 'prefer_places=高野山' \
  --data-urlencode 'limit=3' | jq '.results[] | {jukugo, kaimyo_score, bonus_score, final_score}'

# 4 字熟語のみ
curl -s -G 'http://127.0.0.1:8000/api/kaimyo/candidates' \
  --data-urlencode 'characteristics=信仰深い' \
  --data-urlencode 'length=4' | jq '.results[] | {jukugo, length, kaimyo_score}'

# レビュー対象を含める
curl -s -G 'http://127.0.0.1:8000/api/kaimyo/candidates' \
  --data-urlencode 'characteristics=清廉' \
  --data-urlencode 'include_review=true' | jq '.metadata, (.results | length)'

# エラー：未定義特性 → 400 + available 同梱
curl -s -G 'http://127.0.0.1:8000/api/kaimyo/candidates' \
  --data-urlencode 'characteristics=未知の特性' | jq '.detail'
```

## 起動時ロード（仕様 §13.8.2）

1. `data/mikkyou/index_shoryoshu_*.json`（7 ファイル）
2. `data/kukai/shoryoshu_miyasaka.json`
3. `data/mikkyou/api_mappings.json`
4. 共起マトリックス（7 ペア + 派生 6 ペア）の前計算
5. alias_to_canonical / 篇 idx 別逆引き辞書の構築

総メモリ概算 15〜20 MB。索引ロード + 全前計算で 100 ms 程度（参考値）。

## レスポンスのざっくりサイズ

| エンドポイント | top_n=3 で JSON シリアライズ |
|---|---|
| `/api/term/三密` | 約 2.5 KB |
| `/api/person/空海` | 約 3.0 KB |
| `/api/place/高野山` | 約 2.4 KB |
| `/api/citation/荘子` | 約 2.5 KB |
| `/api/sanskrit/prajñā` | 約 2.4 KB |
| `/api/kukai-work/梵字悉曇字母并びに釈義` | 約 1.4 KB |

`full_context=true` で occurrences を全件返すモードあり（IAST 文字や本文長次第で
数十〜100 KB に増える）。

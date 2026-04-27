# 横断索引化フェーズ B 設計書（cross_index_spec.md）

作成日：2026-04-27（フェーズ B 着手セッション）
版：**v1.2（戒名向け熟語抽出完了版・典故書名 + 密教教学用語 + 梵語 + 戒名向け熟語）**

更新履歴：
- 2026-04-27 v0.1 ドラフト作成 + 典故書名パイロット抽出（256 種・1187 件）
- 2026-04-27 v1.0 昇格：課題 A〜E 解消（CANONICAL_MAP 拡充・空海著作分離・除外辞書整備）+ 密教教学用語 19 語の本格抽出 + cross_index 共通スキーマ確定
- 2026-04-27 v1.1 昇格：Tier 2-4 梵語 IAST 抽出完了（438 種・654 件・表記揺れ統合 6 種・除外辞書 14 ノイズ語）
- 2026-04-27 v1.2 昇格：Tier 2-3 戒名向け熟語抽出完了（111 種・1971 件・起点 1 シード 11 + 起点 2 梵語漢訳 32 + 起点 3 補注ホワイトリスト 68・人手レビュー要 51 件マーカー）

---

## 0. 用途と背景

本データベース（buddhist-data-api）は kaimyo-app をはじめとする仏教関連アプリの共有知識バンクとして機能する。フェーズ 2 で全 112 篇の高品質訳が完成し、本文括弧書きに典故 1187 件・梵語 411 種・密教教学用語 19 種延べ 558 件・人名・地名等が埋め込まれた。これらは現状「本文の中に溶け込んだ参考情報」のままで、横断検索が困難な状態にある。

フェーズ B（横断索引化）では、この本文埋め込み情報を独立した検索可能データとして抽出・正規化・出典付き蓄積し、以下の用途に供する。

### 主な活用想定

1. **戒名選定候補の抽出**（kaimyo-app 戒名生成機能）
   - 故人の生前の特性に対応する仏教的に価値のある熟語・一字を抽出
   - 真言密教の世界観に沿った文字選定のための辞書基盤
   - 例：「学問熱心だった故人」→ 「智」「明」「学」「慧剣」「智剣」「玄機」等を、出典付きで提案

2. **法話・諷誦文生成のための真言宗教義・大師思想の貯蔵庫**（kaimyo-app 法話生成機能）
   - 「即身成仏」「三密」「大日如来」等の根本教義の解説・典拠の検索
   - 法話で引用すべき典故（『法華経』『涅槃経』『般若心経』『大智度論』等）の検索
   - 故人を偲ぶ文脈に適合する大師の言葉の検索

3. **真言宗教義の勉強会・学習用アプリ**（将来）
   - 各教義語の出典と用例の網羅
   - 大師原文と現代語訳のセット提示

---

## 1. 抽出カテゴリと優先順位（Cowork 提案）

ケンシン回答「優先順位は決められない」を受け、用途（戒名選定・教義貯蔵庫）から逆算して以下の優先順位を Cowork 提案する。

### Tier 1（最優先・教義貯蔵庫の核）

**カテゴリ 1: 密教教学用語**（19 語・延べ 558 件）

- 大師思想の核（密教・大日・法界・三密・即身成仏・阿字・遮那・心王・智剣・宝珠 等）
- 戒名・法話の両方で最も価値が高い
- 既に Excel `quality_report_phase2_index.xlsx`「密教教学用語」シートで集計済
- **抽出パターン**：本文中の語彙マッチ（19 語の正規辞書を作成）+ 括弧書き内の梵語注記

**カテゴリ 2: 典故書名**（256 種・延べ 1187 件）

- 法話で典故引用に必須
- 抽出パターンが最も明確（『〜』）
- 仏典系：『法華経』『涅槃経』『般若心経』『大智度論』『瑜伽師地論』『摩訶止観』『大日経』『金剛頂経』 等
- 漢学系：『荘子』『詩経』『論語』『書経』『易経』『山海経』 等
- **抽出パターン**：`『([^『』]+?)』` の正規表現

### Tier 2（次優先・戒名選定向け）

**カテゴリ 3: 戒名向け熟語候補**

- 二字熟語のうち仏教的価値が高いもの（智剣・宝珠・玄機・遮那・大悲・慈悲・浄信・智明 等）
- 一字のうち戒名適合語（智・明・慧・浄・聖・定・妙 等）
- **抽出方法**：Tier 1 から派生（密教教学用語を一字・二字に分解 + 補注に書かれた漢語熟語を抽出）

**カテゴリ 4: 梵語**（411 種・延べ 603 件）

- IAST 表記の正規化が必要（vipūyaka・navāśubha-bhāvanā・bodhi 等）
- 教学用語の補強情報として有用（戒名へのアプローチには副次的）
- **抽出パターン**：括弧書き内の Sanskrit 表記（IAST または Harvard-Kyoto）

### Tier 3（補助・参考情報）

**カテゴリ 5: 人名**

- 仏教人名（恵果・不空・善無畏・金剛智・空海・最澄・真済 等）
- 漢籍人名（荘子・荘周・葉公・許由・伯夷・王羲之 等）
- 梵語名併記がある場合は併記（Vairocana・Mañjuśrī 等）

**カテゴリ 6: 地名**

- 仏教地名（青龍寺・長安・天竺・霊鷲山・五台山 等）
- 日本地名（高野山・神泉苑・東大寺・大和 等）

---

## 2. データスキーマ案（v0.1 → v1.0 で確定）

### 2.1 ファイル構成

```
data/mikkyou/
├── index_shoryoshu_terms.json        # Tier 1-1 密教教学用語（v1.0 完成）
├── index_shoryoshu_citations.json    # Tier 1-2 典故書名（v1.0 完成）
├── index_shoryoshu_kukai_works.json  # 課題 D：空海著作・性霊集編纂物（v1.0 新規）
├── index_shoryoshu_kaimyo.json       # Tier 2-3 戒名向け熟語候補
├── index_shoryoshu_sanskrit.json     # Tier 2-4 梵語
├── index_shoryoshu_persons.json      # Tier 3-5 人名
├── index_shoryoshu_places.json       # Tier 3-6 地名
└── index_shoryoshu_meta.json         # 索引メタ情報（版・更新日・統計）
```

`index_*.json` の既存 3 ファイル（butsuzo・citations・kanji）は密教大辞典由来で別系統のため、新規索引は接頭辞 `index_shoryoshu_` で区別。

### 2.2 共通スキーマ（v1.0 確定）

```json
{
  "schema_version": "1.0",
  "category": "<カテゴリ名>",
  "source_corpus": "shoryoshu_miyasaka.json",
  "generated_at": "<ISO 日付>",
  "extraction_strategy": "<抽出方法の要約>",
  "summary": {
    "unique_terms": 0,
    "total_occurrences": 0,
    "covered_shoryoshu_idx_count": 0
  },
  "entries": [
    {
      "term": "<正規形>",
      "aliases": ["<表記揺れ>"],
      "sanskrit": "<IAST>",
      "definition": "<定義>",
      "kaimyo_suitable": true,
      "kaimyo_chars": ["<一字>"],
      "occurrence_count": 0,
      "篇分布": [0],
      "occurrences": [
        {
          "shoryoshu_idx": 0,
          "篇名": "真済序",
          "巻": "巻第一",
          "page_idx": 0,
          "context": "...真言加持の道、此の日来漸し...",
          "context_position": 1245,
          "raw_form": "<原表記・citations のみ>",
          "sanskrit_in_context": ["<梵語・terms のみ>"]
        }
      ]
    }
  ]
}
```

---

## 3. 抽出戦略

### 3.1 抽出パイプライン

```
shoryoshu_miyasaka.json (全 112 篇 gendaigoyaku)
   ↓
[1] 機械抽出（正規表現・辞書照合）
   ↓
[2] 篇別出現一覧の生成
   ↓
[3] 正規化（表記揺れ統合・梵語 IAST 統一）
   ↓
[4] 戒名適合性スコアリング（Tier 2）
   ↓
[5] index_shoryoshu_*.json への書込
```

### 3.2 各カテゴリの抽出ロジック

| カテゴリ | 抽出方法 | 主な課題 |
|---|---|---|
| 密教教学用語 | 19 語の辞書 + 本文 grep | 同表記の通俗的用法を排除（例：「密教」は密教教学用語、「秘密」は通俗的でも区別必要） |
| 典故書名 | `『([^『』]+?)』` 正規表現 | 書名の正規化（『大智度論』『智度論』『大論』の同一視） |
| 戒名向け熟語 | Tier 1 から派生 + 補注内熟語抽出 | 戒名適合性の判定（人手レビュー要） |
| 梵語 | 括弧書き内の Sanskrit 字種マッチ | IAST/HK 表記揺れの統一・性数の正規化 |
| 人名 | 補注内の人物言及パターン | 同名異人の区別・読み仮名の付与 |
| 地名 | 補注内の地名言及パターン | 仏教地名と一般地名の区別 |

---

## 4. kaimyo-app 連携 API 案（候補 D の前段）

### 4.1 想定エンドポイント

```
GET /api/kaimyo/candidates?characteristics=学問熱心,温和
  → 戒名候補一覧（出典付き）

GET /api/houwa/citations?theme=無常
  → 法話用典故引用候補

GET /api/term/:term
  → 教学用語の定義・梵語・出典・用例
```

### 4.2 内部データフロー

```
characteristics (戒名生成入力)
   ↓
特性 → カテゴリマッピング（学問→智・明・慧、温和→慈・悲・浄）
   ↓
index_shoryoshu_kaimyo.json から候補抽出
   ↓
出典文・解釈付与（index_shoryoshu_terms.json から補強）
   ↓
JSON レスポンス
```

---

## 5. 工数見積もり（5〜8 セッション・v1.0 で 2 セッション分完了）

| セッション | 作業内容 | 状態 |
|---|---|---|
| 1（着手）| 仕様書作成 + パイロット抽出（典故書名）+ スキーマ確定 | ✅ 完了 |
| **2（v1.0）** | **課題 A〜E 解消 + 典故書名 v1.0 + 密教教学用語 v1.0 + 共通スキーマ確定** | **✅ 完了** |
| **3（v1.1）** | **梵語 IAST の正規化 + index_shoryoshu_sanskrit.json（438 種・654 件）** | **✅ 完了** |
| 4 | 戒名向け熟語の選別・スコアリング + index_shoryoshu_kaimyo.json | 次セッション候補 |
| 5 | 人名抽出 + index_shoryoshu_persons.json | 未着手 |
| 6 | 地名抽出 + index_shoryoshu_places.json | 未着手 |
| 7 | 全索引の品質チェック + index_shoryoshu_meta.json 整備 | 未着手 |
| 8（予備）| kaimyo-app 連携 API のサンプル実装または検証 | 未着手 |

---

## 6. 留意事項

### 6.1 AI 由来補注の制約

品質報告書 §6 で明示した通り、本文埋め込み補注は Cowork（Claude Sonnet 4.6）由来の推定を含む。索引化作業は「Cowork 訳に書かれた語の網羅化」であり、「典故誤同定の検出」は別途専門家校閲（候補 E）が必要。

### 6.2 元データの非破壊原則

shoryoshu_miyasaka.json は変更しない。索引化は別ファイル（index_shoryoshu_*.json）への抽出。idx=106 のような明示的例外を除き、原文・訳文は触らない。

### 6.3 索引の更新タイミング

- shoryoshu_miyasaka.json に変更があった場合：影響範囲の篇のみ index を再生成（部分更新スクリプト要設計）
- 索引フォーマット変更時：`schema_version` をインクリメント

---

## 7. パイロット抽出結果（2026-04-27 第 1 セッション）

### 7.1 結果サマリ

| 指標 | 値 |
|---|---|
| 異なり書名数 | 256 種 |
| 延べ出現件数 | 1187 件 |
| 出現篇数 | 105 篇（93.8%） |
| canonical 統合 | 8 種 |

### 7.2 検出された改善課題（v1.0 で全て解消）

| 課題 | 内容 |
|---|---|
| A | 『理趣経』の表記揺れ統合（5 種・13 件） |
| B | 『易』→『易経』正規化（24 件） |
| C | 『仁王経』括弧書き混入（5 種） |
| D | 空海著作・性霊集編纂物の分離（5 件） |
| E | 書名でない『内典・外典』の除外 |

---

## 8. v1.0 本格抽出結果（2026-04-27 第 2 セッション）

`_dev_references/extract_citations.py`（パイロット版を本格版にリファクタ）と `_dev_references/extract_terms.py`（新規作成）で 2 つの索引を完成させた。

### 8.1 典故書名（v1.0・課題 A〜E 解消後）

出力先：
- `data/mikkyou/index_shoryoshu_citations.json`（典故書名・他者著作）
- `data/mikkyou/index_shoryoshu_kukai_works.json`（空海著作・性霊集編纂物）

| 指標 | パイロット v0.1 | 本格 v1.0 | 差分 |
|---|---|---|---|
| citations 異なり数 | 256 | **237** | -19（正規化により統合） |
| citations 延べ件数 | 1187 | **1181** | -6（除外 1 + kukai_works 5） |
| kukai_works 異なり数 | -（混入） | **5** | 新規分離 |
| kukai_works 延べ件数 | -（混入） | **5** | 新規分離 |
| excluded（『内典・外典』）| 1 件混入 | **1 件除外** | 課題 E 完了 |

**課題 A〜E 解消結果（自動検証）**

| 課題 | 旧状態 | v1.0 結果 |
|---|---|---|
| A. 理趣経表記揺れ | 6 種に分散 | **『理趣経』13 件 / aliases 5 種** ✅ |
| A. 理趣釈分離 | 1 種 | **『理趣釈』3 件 / aliases 2 種** ✅ |
| B. 易 → 易経 | 『易』24 件 + 『易経』9 件 = 33 件分散 | **『易経』33 件 / alias=『易』** ✅ |
| C. 仁王経括弧混入 | 6 種に分散 | **『仁王経』9 件 / aliases 5 種** ✅ |
| D. 空海著作分離 | citations に混在 | **kukai_works 5 種に分離** ✅ |
| E. 内典・外典除外 | citations に混入 | **excluded 1 件** ✅ |

**v1.0 出現上位 10**

| 順位 | 書名 | 件数 | 篇分布 |
|---|---|---|---|
| 1 | 『荘子』 | 103 | 53 篇 |
| 2 | 『詩経』 | 82 | 47 篇 |
| 3 | 『法華経』 | 71 | 34 篇 |
| 4 | 『論語』 | 67 | 37 篇 |
| 5 | 『書経』 | 60 | 31 篇 |
| 6 | 『涅槃経』 | 48 | 29 篇 |
| 7 | 『礼記』 | 39 | 28 篇 |
| 8 | **『易経』** | 33 | 21 篇（旧『易』24 + 『易経』9） |
| 9 | 『大智度論』 | 30 | 21 篇 |
| 10 | 『淮南子』 | 26 | 16 篇 |

**kukai_works 全 5 件**

| term | aliases | 分類タグ |
|---|---|---|
| 古今文字讃 | — | 空海請来書 |
| 古今篆隷の文体 | — | 空海請来書 |
| 大広智の影の讃 | 大広智（不空三蔵）の影（肖像）の讃 | idx12 篇名（空海碑文） |
| 梵字悉曇字母并びに釈義 | — | 空海著作 |
| 続性霊集補闕鈔 | 続性霊集補闕鈔（ぞくしょうりょうしゅうほけつしょう） | 性霊集編纂物 |

### 8.2 密教教学用語（Tier 1-1・新規生成）

出力先：`data/mikkyou/index_shoryoshu_terms.json`

抽出方針：
- 19 語の正規辞書（品質報告書 §2.3 準拠）
- **長語優先 substring 走査**で二重カウント回避（即身成仏 / 即身、阿字本不生 / 阿字 / 本不生 など）
- term ごとに `sanskrit`・`definition`・`kaimyo_suitable`・`kaimyo_chars` を付与
- 各 occurrence の前後 30 字スコープから周辺梵語注記（IAST）を抽出して `sanskrit_in_context` に集約

| 指標 | 値 |
|---|---|
| 異なり語数 | 19 種（辞書サイズと一致） |
| 延べ出現件数 | **544 件** |
| 出現篇数（密教 1 位）| 48 篇 |
| 戒名適合語 | **11 語**（kaimyo_suitable=true） |

**品質報告書 §2.3 との突合**

|語|本格抽出|品質報告書|差|
|---|---|---|---|
|密教|125|120|+5|
|大日|111|110|+1|
|法界|68|68|±0 ✅|
|三密|46|46|±0 ✅|
|法身|45|45|±0 ✅|
|真言|44|44|±0 ✅|
|大悲|26|26|±0 ✅|
|本不生|12|20|-8（阿字本不生に長語優先で吸収）|
|阿字|11|19|-8（阿字本不生に長語優先で吸収）|
|遮那|18|18|±0 ✅|
|心王|9|9|±0 ✅|
|阿字本不生|8|8|±0 ✅|
|即身成仏|7|6|+1|
|即身|0|6|-6（全件が即身成仏の一部だった）|
|玄機|5|5|±0 ✅|
|智剣|4|4|±0 ✅|
|三摩地|3|2|+1|
|無縁慈悲|1|1|±0 ✅|
|大空三昧|1|1|±0 ✅|

差分の解釈：
- 品質報告書の集計は単純 substring カウントで「即身成仏」が「即身」「成仏」を二重計上していた可能性。本格抽出は長語優先で重複排除、戒名選定への利用に最適化。
- 報告書 558 件 vs 本格抽出 544 件（差 -14）の主因は上記 substring 二重カウント解消。

**戒名適合語 11 語（kaimyo_suitable=true）**

即身成仏・無縁慈悲・大日・法界・三密・法身・真言・大悲・遮那・玄機・智剣

**周辺梵語注記の自動集約サンプル**（密教 unique 25 語）：
a-kāra, amoghavajra, bodhi, cetanā, cintāmaṇi, guhya, guhya-piṭaka, hṛd-cit-saṃkrama, mano-guhya, mantra, maṇi, …（Tier 2-4 梵語抽出の素材として再利用可）

### 8.3 v1.0 完成度評価

- ✅ **典故書名カテゴリ完成**：パイロットの 5 課題すべて解消
- ✅ **空海著作の分離**：他者著作引用とは性質が異なるため別ファイル化
- ✅ **密教教学用語カテゴリ完成**：19 語の網羅抽出 + 戒名適合性タグ付与
- ✅ **共通スキーマ確定**：以後の Tier 2-4（梵語）・Tier 3（人名・地名）は同スキーマで生成
- ⏭️ 次セッション以降の予定：
  - **Tier 2-4 梵語抽出**（411 種・603 件、本セッションで集約済の sanskrit_in_context を起点に）
  - **Tier 2-3 戒名向け熟語選別**（密教教学用語の kaimyo_suitable + 補注 2 字熟語抽出）
  - **Tier 3-5/6 人名・地名抽出**

---

## 9. v1.1 本格抽出結果：梵語 IAST（2026-04-27 第 3 セッション）

`_dev_references/extract_sanskrit.py`（新規作成）で梵語 IAST 索引を完成させた。

### 9.1 抽出方針

出力先：`data/mikkyou/index_shoryoshu_sanskrit.json`

抽出方針：
- 全 112 篇 gendaigoyaku に対し、ASCII ラテン文字 + IAST ダイアクリティカル（ā ī ū ṛ ṅ ñ ṇ ḍ ṭ ṣ ś ḥ ṃ）+ ハイフン + ピリオド + アポストロフィを許す正規表現で梵語候補を網羅抽出
- 3 文字以上を採用（密教種子字 vam・raṃ・vaṃ 等を含めるため最小値）
- **EXCLUDE_TOKENS（小文字基準・14 語）**で以下を除外：
  - メタ情報語：idx・kindle・ocr・claude.md
  - URL 断片：https・ran・hu（"https://hu hu ran" 由来）
  - 補注内英訳：milk・gruel・brass・gold・elixir・clavicle
  - ローマ字日本語：goshin-kekkai
- **小文字基準で canonical_key を生成**し、大文字小文字の表記揺れを統合
  - 例：`Vairocana`×1 + `vairocana`×8 → canonical=`vairocana`、aliases に両形をカウント保存
- IAST ダイアクリティカル含有/非含有を `has_diacritics` フラグで記録（戒名選定では IAST 含有が確実な梵語と扱える）
- ALIAS_MAP（異綴り統合・例：`vairochana`→`vairocana`）は拡張余地として準備（現状空）

### 9.2 結果サマリ

| 指標 | 値 |
|---|---|
| 異なり canonical 数 | **438 種** |
| 延べ出現件数 | **654 件** |
| IAST ダイアクリティカル含有 | 328 種（74.9%） |
| ASCII 純粋（dharma・bodhi 等の伝統綴り）| 110 種（25.1%） |
| 出現篇数 | 66 篇 / 112 篇（58.9%）|
| 表記揺れ統合 canonical | 6 種 |
| 除外辞書サイズ | 14 ノイズ語 |
| ALIAS_MAP サイズ | 0（拡張余地） |

引き継ぎメモ「411 種・603 件」（品質報告書由来見積り）に対し +27 種・+51 件の超過は、抽出基準を「IAST 含有 + ASCII 全候補から除外辞書のみで絞る」と広く取ったため（ホワイトリスト方式より網羅的）。

### 9.3 出現上位 20

| 順位 | canonical | 出現数 | IAST | 篇数 | 主漢訳 |
|---|---|---|---|---|---|
| 1 | bodhi | 10 |  | 8 | 菩提 |
| 2 | buddha | 9 |  | 9 | 仏陀 |
| 2 | vairocana | 9 | 大文字統合 | 9 | 毘盧遮那・大日如来 |
| 4 | bhikṣu | 7 | ★ | 7 | 比丘 |
| 4 | dharma | 7 |  | 7 | 法 |
| 4 | sattva | 7 |  | 7 | 薩埵 |
| 7 | samādhi | 6 | ★ | 5 | 三摩地 |
| 8 | ekayāna | 5 | ★ | 4 | 一乗 |
| 8 | gāthā | 5 | ★ | 5 | 偈 |
| 8 | māyā | 5 | ★ | 2 | 幻 |
| 8 | nāgārjuna | 5 | ★ | 4 | 龍樹 |
| 8 | prajñā | 5 | ★ | 5 | 般若 |
| 8 | sumeru | 5 |  | 5 | 須弥山 |
| 8 | ācārya | 5 | ★ | 5 | 阿闍梨 |
| 8 | śūnya | 5 | ★ | 2 | 空 |
| 16 | amoghavajra | 4 | 大文字統合 | 4 | 不空三蔵 |
| 16 | bhagavān | 4 | ★ | 4 | 世尊 |
| 16 | bodhisattva | 4 |  | 4 | 菩薩 |
| 16 | dharmakāya | 4 | ★ | 3 | 法身 |
| 16 | saṃgha | 4 | ★ | 4 | 僧伽 |

### 9.4 表記揺れ統合 6 件（canonical=小文字基準）

| canonical | aliases |
|---|---|
| vairocana | vairocana×8, Vairocana×1 |
| amoghavajra | Amoghavajra×2, amoghavajra×2 |
| mañjuśrī | mañjuśrī×2, Mañjuśrī×1 |
| ānanda | Ānanda×2, ānanda×1 |
| rāhula | Rāhula×1, rāhula×1 |
| tuṣita | Tuṣita×1, tuṣita×1 |

固有名詞（人名・本尊名）に冒頭大文字化と全小文字の揺れが残存。canonical 集約により検索利便性は確保。

### 9.5 戒名選定への適用ヒント

梵語そのものは戒名（漢字）にならないが、漢訳語との対応が選定補強情報になる：
- vairocana / mahāvairocana → 「遮那」「大日」（既に terms に登録済・kaimyo_suitable=true）
- prajñā → 「般若」「智」「慧」（戒名適合一字候補）
- karuṇā / mahā-karuṇā → 「大悲」「慈」「悲」（kaimyo_suitable=true）
- bodhi → 「菩提」「悟」「覚」
- śūnya / śūnyatā → 「空」「玄」
- 周辺漢訳の自動関連付けは Tier 2-3 戒名向け熟語選別フェーズで集約予定。

### 9.6 v1.1 完成度評価

- ✅ **梵語 IAST カテゴリ完成**：438 種・654 件・表記揺れ統合 6 種・除外辞書 14 ノイズ語
- ✅ **既知梵語 ASCII の網羅**：dharma・bodhi・vairocana 等のダイアクリティカルなし表記も拾えている（ホワイトリスト不要・除外辞書のみで十分な品質）
- ⏭️ 次セッション以降の予定：
  - **Tier 2-3 戒名向け熟語選別**（密教教学用語 + 梵語の漢訳対応 + 補注 2 字熟語抽出）
  - **Tier 3-5/6 人名・地名抽出**
  - **kaimyo-app 連携 API 設計**（候補 D）

---

## 10. v1.2 本格抽出結果：戒名向け熟語（2026-04-27 第 4 セッション）

`_dev_references/_tmp_extract_kaimyo_jukugo.py`（新規作成）で kaimyo-app の戒名選定用辞書を完成させた。スクリプトは Cowork sandbox 編集の安全のため `_dev_references/_tmp_*.py` 配下に置く運用（outputs フォルダの truncate 問題回避・引き継ぎメモ 2026-04-27_梵語抽出v1.1完了 §副次発見）。

### 10.1 抽出方針

出力先：`data/mikkyou/index_shoryoshu_kaimyo.json`

3 つの起点を組み合わせて戒名向け熟語を網羅：

**起点 1：密教教学用語の戒名適合 11 語（シード）**

`index_shoryoshu_terms.json` で `kaimyo_suitable=true` が付与された 11 語をそのままシードに採用：

即身成仏・無縁慈悲・大日・法界・三密・法身・真言・大悲・遮那・玄機・智剣

**起点 2：梵語の漢訳対応（手書きキュレーション）**

`SANSKRIT_TO_KAIMYO_JUKUGO`（51 エントリ）で梵語 → 戒名熟語の対応辞書を定義し、`index_shoryoshu_sanskrit.json` に該当 canonical が存在する場合のみ採用：

- prajñā → 般若・智慧
- karuṇā / mahā-karuṇā → 大悲・慈悲
- bodhi / bodhicitta → 菩提
- śūnya / śūnyatā → 空観
- samādhi → 三昧 / dhyāna → 禅定
- dharma / dharmakāya → 法身・正法 / dharma-dhātu → 法界
- mantra → 真言 / vajra → 金剛
- mahāvairocana → 大日・遮那 / vairocana → 遮那
- tathāgata → 如来 / tathatā → 真如 / nirvāṇa → 涅槃
- avalokiteśvara → 観音 / mañjuśrī → 文殊 / samantabhadra → 普賢 / amitābha → 弥陀
- śīla → 持戒 / kṣānti → 忍辱 / vīrya → 精進
- ratna / cintāmaṇi → 宝珠
- siddhi → 成就 / mokṣa → 解脱
- śraddhā → 浄信
- ekayāna → 一乗 / mahāyāna → 大乗
- pāramitā → 波羅蜜 / upāya → 方便
- praṇidhāna → 誓願 / mahāmudrā → 大印
- ほか

起点 1 のシードと重複する熟語（大日・遮那・大悲・法身・法界・真言）は起点 1 を優先。

**起点 3：補注内 2 字漢語熟語のホワイトリスト抽出**

全 112 篇 `gendaigoyaku` から括弧書き内（`（〜）`）の 2 字漢語熟語を機械抽出し、人手キュレートした `DOCTRINAL_2CHAR_WHITELIST`（約 150 語）と `KAIMYO_NOISE`（約 140 語）の 2 段フィルタで戒名向けに絞り込み：

- ホワイトリスト採用例：仏法・蓮華・真理・本性・清浄・解脱・大徳・心地・常住・霊妙
- ノイズ除外例：天皇・天子・空海・荘子・嵯峨・神泉・八二（年代）・譬喩（メタ）

機械的に 6,246 種・13,887 件出現する 2 字漢語からホワイトリスト＆ノイズ除外で 68 種に絞り込み。

### 10.2 戒名適合性スコアリング

```
kaimyo_score = freq_score + doctrinal_score + ichiji_score + aesthetic_score
                                                           （0〜75 点スケール）
```

| 要素 | 算出ルール | 上限 |
|---|---|---|
| `freq_score` | log10(occurrence_count + 1) × 12 | 25 |
| `doctrinal_score` | seed_terms=30, seed_sanskrit=20, paren_doctrinal=10 | 30 |
| `ichiji_score` | KAIMYO_ICHIJI（戒名適合一字 85 字）含字数 × 8 | 16 |
| `aesthetic_score` | 字形美・響き美のヒューリスティック（重複字 -2 / 全字 ICHIJI +2 / GOOD_PAIRS +2） | 4 |

**KAIMYO_ICHIJI（戒名適合一字 85 字・抜粋）**：

智・慧・明・覚・悟・聡・玄・慈・悲・仁・善・愛・浄・信・清・澄・寂・静・和・雅・真・常・実・正・法・道・理・心・性・空・無・元・本・妙・宝・尊・大・広・恵・徳・栄・光・明・照・月・華・蓮・雲・霞・山・海・泉・水・河・永・長・久・密・真・言・阿・吽・金・剛・仏・如・尊・聖・師・経・志・誓・願・念

### 10.3 人手レビュー要マーカー

`needs_human_review=true` を以下の条件で自動付与：

- 起点 3（補注由来）かつ kaimyo_score < 35 の語

シード 11 語（起点 1）と梵語漢訳対応 32 語（起点 2）は人手キュレート済のため `needs_human_review=false`。kaimyo-app 連携時はまずシード由来 43 語を確実な辞書として運用し、補注由来 68 語は段階的に人手校閲を経て採用する想定。

### 10.4 結果サマリ

| 指標 | 値 |
|---|---|
| 異なり熟語数 | **111 種** |
| 延べ出現件数 | **1,971 件** |
| 出現篇数 | **100 篇 / 112 篇（89.3%）** |
| 起点 1（密教教学用語シード） | 11 種 |
| 起点 2（梵語漢訳対応） | 32 種 |
| 起点 3（補注ホワイトリスト） | 68 種 |
| `needs_human_review=true` | 51 件（全て起点 3） |
| 4 字熟語（即身成仏・無縁慈悲）| 2 種（シード由来） |
| 出力ファイルサイズ | 978,464 bytes |

### 10.5 出現上位 15

| 順位 | jukugo | source | 出現数 | kaimyo_score | review |
|---|---|---|---|---|---|
| 1 | 金剛 | seed_sanskrit | 193 | 63.0 | false |
| 2 | 菩薩 | seed_sanskrit | 149 | 45.0 | false |
| 3 | 如来 | seed_sanskrit | 134 | 53.0 | false |
| 4 | 大日 | seed_terms | 111 | 62.6 | false |
| 5 | 涅槃 | seed_sanskrit | 78 | 42.8 | false |
| 6 | 法界 | seed_terms | 68 | 60.1 | false |
| 7 | 智慧 | seed_sanskrit | 63 | 61.7 | false |
| 8 | 般若 | seed_sanskrit | 57 | 41.2 | false |
| 9 | 仏法 | paren_doctrinal | 51 | 48.6 | false |
| 10 | 三密 | seed_terms | 46 | 58.1 | false |
| 10 | 三昧 | seed_sanskrit | 46 | 40.1 | false |
| 12 | 法身 | seed_terms | 45 | 60.0 | false |
| 13 | 真言 | seed_terms | 44 | 67.8 | false |
| 14 | 仏陀 | seed_sanskrit | 43 | 47.7 | false |
| 15 | 観音 | seed_sanskrit | 34 | 38.5 | false |

「真言」が score 67.8 で最高位（freq=20.0 + doctrinal=30 + ichiji=16 + aesthetic=2 = 68.0 → 一字「真」「言」が両方 KAIMYO_ICHIJI）。「金剛」は出現件数 193 と最多だが 4 文字戒名「金剛智」「金剛峯寺」等の人名・寺名の混入が一定数含まれる可能性あり（occurrences の context を kaimyo-app 側で再走査して人名フィルタ要）。

### 10.6 paren_doctrinal（起点 3・補注由来）の代表例

| jukugo | 出現数 | kaimyo_score | review |
|---|---|---|---|
| 仏法 | 51 | 48.6 | false |
| 蓮華 | 30 | 45.9 | false |
| 修行 | 28 | 27.6 | **true** |
| 真理 | 25 | 45.0 | false |
| 本来 | 22 | 34.3 | **true** |
| 聖王 | 22 | 34.3 | **true** |
| 真実 | 18 | 43.4 | false |
| 三宝 | 18 | 33.4 | **true** |
| 浄土 | 17 | 33.1 | **true** |
| 慈悲 | 13 | 43.8 | false |
| 清浄 | 10 | 42.5 | false |
| 大徳 | 8 | 39.5 | false |

「修行」「本来」「聖王」「三宝」「浄土」等は教義性は十分高いが戒名適合性のスコアが中位のため要レビュー。kaimyo-app の戒名候補生成時に「シード由来 43 + review=false の補注由来 17」の合計 60 種程度を「自動採用候補」として、残り 51 種を「人手校閲要候補」として段階運用する。

### 10.7 戒名適合一字（KAIMYO_ICHIJI 85 字）の収録

各 entry の `kaimyo_chars` に、その熟語を構成する字のうち KAIMYO_ICHIJI に含まれるものを保存。kaimyo-app 側で「故人の特性 → 適合一字 → 候補熟語」の逆引きマッピングに使用：

```jsonc
{
  "jukugo": "智慧",
  "kaimyo_chars": ["智", "慧"],
  "kaimyo_score": 61.7,
  "source_tag": "seed_sanskrit",
  "sanskrit_origins": ["prajñā"]
}
```

### 10.8 連携 API への接続イメージ

```
GET /api/kaimyo/candidates?characteristics=学問熱心,温和

  → 内部マッピング：学問熱心 → ["智","慧","明","覚","悟"]
                    温和   → ["慈","悲","仁","和","雅"]

  → index_shoryoshu_kaimyo.json から kaimyo_chars に該当字を含む entries を抽出

  → スコア順にソート、出典文（occurrences[0..n].context）付きで返却
```

実装は次セッション以降の §4 API 設計（候補 D）で本格設計する。

### 10.9 v1.2 完成度評価

- ✅ **戒名向け熟語カテゴリ完成**：111 種・1,971 件・起点 3 つの組合せで kaimyo-app 用辞書として機能
- ✅ **人手レビュー要マーカー実装**：51 件のグレーゾーン熟語を明示
- ✅ **シード由来 43 件の確実辞書**：人手キュレート済で `review=false`、即運用可
- ⏭️ 次セッション以降の予定：
  - **Tier 3-5/6 人名・地名抽出**（仏教人名 / 漢籍人名 / 仏教地名 / 日本地名）
  - **kaimyo-app 連携 API 設計**（候補 D・3〜5 セッション）
  - **paren_doctrinal の人手校閲ラウンド**（51 件のレビュー → 採否決定）


## §11 Tier 3-5 人名索引（v1.3 新規）

性霊集 gendaigoyaku に登場する人名を、仏教祖師・諸尊・諸天・諸子百家・神話伝説人物・天皇・貴族の各カテゴリで構造化する索引。kaimyo-app では「故人の修学・所属・尊崇する人物」と当索引を突き合わせて、戒名選定時の典拠例示や法話用引用に活用する。

出力ファイル：`data/mikkyou/index_shoryoshu_persons.json`

### 11.1 抽出方針

人手キュレートシード辞書による「漏れなく・誤検知少なく」の網羅型抽出。
シード辞書の各エントリには `canonical`（代表表記）, `aliases`（追号・尊称・略称・梵語名併記）, `subcategory`（後述の 9 分類）, `definition`（簡潔な人物紹介）, 任意の `sanskrit_canonical`（既存梵語索引へのリンク）を持たせる。

#### subcategory（taxonomy 9 分類）

| サブカテゴリ | 内容 | 代表例 |
|---|---|---|
| `buddhist_master_india` | インドの仏教祖師・仏弟子 | 釈迦・迦葉・阿難・舎利弗・龍樹・龍智 |
| `buddhist_master_china` | 中国の仏教祖師・密教伝持者 | 不空・善無畏・金剛智・恵果・玄奘・智顗・道宣 |
| `buddhist_master_japan` | 日本の仏教祖師・空海十大弟子 | 空海・最澄・真済・徳一・泰範・実恵・智泉・聖徳太子・鑑真 |
| `buddhist_buddha_bodhisattva` | 仏菩薩・諸尊 | 大日如来・阿弥陀・薬師・弥勒・観音・文殊・普賢・地蔵・虚空蔵・不動・勢至 |
| `buddhist_deva` | 諸天・天部・八部衆 | 梵天・帝釈天・夜叉・羅刹・阿修羅・迦楼羅・緊那羅 |
| `chinese_classical` | 諸子百家・古典文人 | 荘子・老子・孔子・孟子・荀子・韓非・列子・揚雄・宋玉・屈原・司馬遷・陶淵明・王羲之・張旭・郭璞 |
| `chinese_legend` | 神話・伝説人物 | 黄帝・堯・舜・禹・湯王・文王・武王・周公・太公望・許由・巣父・伯夷・葉公・伯牙・鍾子期 |
| `japanese_emperor` | 天皇・皇族 | 嵯峨天皇・桓武天皇・淳和天皇・光仁天皇・平城天皇 |
| `japanese_aristocrat` | 日本の貴族・文人 | 橘逸勢 |

### 11.2 マッチングの設計

- 各 seed の `canonical` と全 `aliases` を「surface 候補」として展開し、長表記優先（surface 文字数の降順）でマッチさせる。
- 例：「龍樹」と aliases「龍猛」を別エントリにせず canonical 「龍樹」に統一し、`matched_forms` で内訳を保持。
- 「Vairocana」「Mañjuśrī」「Avalokiteśvara」など梵語名を aliases に組み込むことで、既存梵語索引（v1.1）との整合を取る（`sanskrit_canonical` フィールドで直接リンク）。
- 一字人名（堯・舜・禹）は前後の文字が漢字でない場合のみ採用（`is_single_kanji=True` フラグ + 前後非漢字境界条件）。

### 11.3 出力スキーマ（per entry）

```jsonc
{
  "canonical": "釈迦",
  "aliases": ["釈尊", "釈迦牟尼", "能仁", "śākyamuni", "Śākyamuni"],
  "subcategory": "buddhist_master_india",
  "definition": "仏教の開祖。Śākyamuni。釈迦族の聖者。",
  "sanskrit_canonical": "śākyamuni",
  "sanskrit_canonical_in_index": false,  // 既存梵語索引にエントリがあるか
  "matched_forms": [
    {"form": "釈迦", "count": 41},
    {"form": "釈尊", "count": 37},
    {"form": "釈迦牟尼", "count": 11}
  ],
  "occurrence_count": 89,
  "篇分布": [0, 1, 6],
  "篇分布_count": 36,
  "occurrences": [
    {"shoryoshu_idx": 0, "篇名": "...", "巻": "巻第一", "page_idx": 0,
     "context": "...釈迦如来の...", "context_position": 1234,
     "matched_form": "釈迦"}
  ]
}
```

### 11.4 v1.3 結果サマリ

| 指標 | 値 |
|---|---|
| seed_dictionary_size | 81 |
| unique_persons | 81 |
| total_occurrences | 1,197 |
| covered_篇 | 109 / 112（97.3%）|

サブカテゴリ別の分布：

| サブカテゴリ | unique | occurrences |
|---|---|---|
| buddhist_master_japan | 10 | 248 |
| chinese_classical | 15 | 234 |
| buddhist_buddha_bodhisattva | 11 | 260 |
| buddhist_master_india | 8 | 130 |
| buddhist_master_china | 10 | 109 |
| chinese_legend | 14 | 91 |
| japanese_emperor | 5 | 70 |
| buddhist_deva | 7 | 53 |
| japanese_aristocrat | 1 | 2 |

### 11.5 出現上位 10

| 順位 | canonical | subcategory | occ |
|---|---|---|---|
| 1 | 空海 | buddhist_master_japan | 202 |
| 2 | 大日如来 | buddhist_buddha_bodhisattva | 135 |
| 3 | 荘子 | chinese_classical | 105 |
| 4 | 釈迦 | buddhist_master_india | 89 |
| 5 | 観音 | buddhist_buddha_bodhisattva | 45 |
| 6 | 恵果 | buddhist_master_china | 38 |
| 7 | 不空 | buddhist_master_china | 32 |
| 8 | 孔子 | chinese_classical | 32 |
| 9 | 嵯峨天皇 | japanese_emperor | 30 |
| 10 | 老子 | chinese_classical | 28 |

### 11.6 既存梵語索引（v1.1）とのクロスリンク

`sanskrit_canonical` フィールドで既存梵語索引（`index_shoryoshu_sanskrit.json`）の canonical キーへリンク。`sanskrit_canonical_in_index` で「既存索引にエントリ有無」を bool 値として保持し、kaimyo-app から「人名 → 梵語名 → 漢訳熟語」の三段クロスリンクを可能にする。

性霊集中で IAST 表記が登場しない仏菩薩名（阿弥陀 amitābha・迦葉 kāśyapa・目連 maudgalyāyana・舎利弗 śāriputra）は `sanskrit_canonical_in_index=false` となるが、後続のコーパス（『十住心論』『秘蔵宝鑰』等）追加時にリンクが有効化される予定。

---

## §12 Tier 3-6 地名索引（v1.3 新規）

性霊集 gendaigoyaku に登場する地名を、寺院・山・国/王朝・都城・旧国・神話・宇宙論・聖地のカテゴリで構造化する索引。kaimyo-app では「故人の出身地・修行地・所縁の聖地」と当索引を突き合わせて、戒名選定時の典拠例示や法話用引用に活用する。

出力ファイル：`data/mikkyou/index_shoryoshu_places.json`

### 12.1 抽出方針

人手キュレートシード辞書による網羅型抽出。`canonical`, `aliases`, `subcategory`（後述の 18 分類）, `definition`, 任意の `sanskrit_canonical` を持たせる。

#### subcategory（taxonomy 18 分類）

| サブカテゴリ | 内容 | 代表例 |
|---|---|---|
| `temple_china` | 中国の寺院 | 青龍寺・大興善寺・大慈恩寺 |
| `temple_japan` | 日本の寺院 | 東大寺・東寺・西寺・神護寺・高雄山寺・元興寺・興福寺・法隆寺 |
| `mountain_china` | 中国の山 | 五台山・天台山・廬山・崑崙 |
| `mountain_japan` | 日本の山 | 高野山・比叡山・吉野・室生 |
| `mountain_buddhist` | 仏教の山 | 霊鷲山・須弥山・雪山・香山 |
| `country_dynasty` | 中国の王朝 | 殷・周・夏・秦・漢・隋・梁・陳・魏・宋・北魏 |
| `country_china` | 春秋戦国諸国・中国の異称 | 燕・趙・斉・魯・楚・韓・呉・越・蜀・震旦（支那・神州・唐土・中華・華夏）|
| `country_western_region` | 西域諸国 | 于闐・亀茲・高昌・吐蕃・波斯・西域 |
| `country_india` | インド系地名 | 天竺（印度・身毒）・南天竺・中天竺 |
| `country_japan` | 日本国 | 日本（日域・本朝・我朝・皇朝・神国）|
| `capital_china` | 中国の都城 | 長安・洛陽 |
| `capital_japan` | 日本の都城 | 平安京・平城京・奈良・南都 |
| `province_japan` | 日本の旧国 | 大和・山城・河内・摂津・近江・伊勢・紀伊・伊予・阿波・讃岐・土佐・播磨・陸奥 |
| `mythological` | 神仙世界の地名 | 蓬莱・方丈・瀛洲 |
| `river_china` | 中国の河川 | 黄河・長江（揚子江）・渭水 |
| `cosmological_realm` | 仏教宇宙論の界 | 欲界・色界・無色界・兜率（兜率天）・極楽・安楽 |
| `sacred_site_indian` | インド仏教聖地 | 祇園精舎・舎衛城（舎衛国）・王舎城・迦毘羅・伽耶 |
| `sacred_site_japan` | 日本の聖地 | 神泉苑 |

### 12.2 マッチングの設計

- 長表記優先：「青龍寺」と「青龍」、「霊鷲山」と「霊山」、「祇園精舎」と「祇園」等で長い表記を先にマッチさせ、短表記は重複位置を除外。
- 1 文字王朝/国名（殷・周・夏・斉・楚・秦・燕・趙・魯・韓・呉・越・蜀・魏・宋・隋・漢・梁・陳）は前後の漢字非継続性を確認（`is_safe_single_char` 条件）。
- さらに `DYNASTY_REJECT_AFTER` で動詞・形容詞活用語尾を除外：
  - 「越」直後が `えゆしすさ` → 「越え/越ゆ/越し/越す/越さ」（動詞活用）として除外
  - 「斉」直後が `しひ` → 「斉しく/斉（ひと）し」（形容詞）として除外
- `DYNASTY_OK_AFTER` で許容直後文字（`王代朝末初年人`、王名の人名起点字 `紂湯文武穆桓` 等）を許容。

### 12.3 出力スキーマ（per entry）

```jsonc
{
  "canonical": "霊鷲山",
  "aliases": ["霊山", "耆闍崛山", "gṛdhrakūṭa"],
  "subcategory": "mountain_buddhist",
  "definition": "王舎城東北の山。釈迦が法華経などを説いた地。",
  "sanskrit_canonical": null,
  "matched_forms": [
    {"form": "霊鷲山", "count": 9},
    {"form": "霊山", "count": 4}
  ],
  "occurrence_count": 13,
  "篇分布_count": 7
}
```

### 12.4 v1.3 結果サマリ

| 指標 | 値 |
|---|---|
| seed_dictionary_size | 84 |
| unique_places | 70 |
| total_occurrences | 466 |
| covered_篇 | 92 / 112（82.1%）|

### 12.5 出現上位 15

| 順位 | canonical | subcategory | occ |
|---|---|---|---|
| 1 | 日本 | country_japan | 60 |
| 2 | 長安 | capital_china | 22 |
| 3 | 漢 | country_dynasty | 19 |
| 4 | 周 | country_dynasty | 16 |
| 5 | 殷 | country_dynasty | 16 |
| 6 | 須弥山 | mountain_buddhist | 15 |
| 7 | 陳 | country_dynasty | 13 |
| 8 | 震旦 | country_china | 13 |
| 9 | 霊鷲山 | mountain_buddhist | 13 |
| 10 | 青龍寺 | temple_china | 11 |
| 11 | 大和 | province_japan | 10 |
| 12 | 秦 | country_dynasty | 10 |
| 13 | 雪山 | mountain_buddhist | 10 |
| 14 | 極楽 | cosmological_realm | 9 |
| 15 | 神護寺 | temple_japan | 9 |

### 12.6 残課題と人手レビュー推奨事項

- 「越（と）ぶ」「斉（ひと）し」のように補注内で読み付け（漢字＋括弧ひらがな）された動詞・形容詞用法は、現行の活用語尾除外で完全には除外できない（数件残存）。kaimyo-app 連携前に人手レビューを推奨。
- 「夏」は「夏王朝」と「季節の夏」の両義語であり、文脈ベースの精密判定は将来の v1.4 で改善予定。
- 「南山」（終南山 / Mt.南）など複数解釈のある語は、現状 seed に未収録。次フェーズで「南山＝終南山」の文脈判定とともに採否決定。

### 12.7 v1.3 完成度評価

- ✅ **人名カテゴリ完成**：81 種・1,197 件・9 分類で kaimyo-app 用辞書として機能
- ✅ **地名カテゴリ完成**：70 種・466 件・18 分類で kaimyo-app 用辞書として機能
- ✅ **既存梵語索引とのクロスリンク**：`sanskrit_canonical` フィールドで人名・地名 → 梵語の三段リンク
- ✅ **長表記優先 + 1 文字境界条件**：誤検知抑止の二重ガード
- ⏭️ 次セッション以降の予定：
  - **kaimyo-app 連携 API 設計**（候補 D・3〜5 セッション）
  - **paren_doctrinal の人手校閲ラウンド**（51 件のレビュー → 採否決定）
  - **地名 v1.4 改善**：「夏（季節 vs 王朝）」「南山」等の精密文脈判定

---

最終更新：2026-04-27 v1.3 昇格（典故書名 + 空海著作分離 + 密教教学用語 + 梵語 IAST + 戒名向け熟語 + 人名 + 地名抽出完了）。次セッション以降は kaimyo-app 連携 API 設計または paren_doctrinal 人手校閲に進む。

# 横断索引化フェーズ B 設計書（cross_index_spec.md）

作成日：2026-04-27（フェーズ B 着手セッション）
版：**v1.8（G2-D dict 型 8 著作 Tier 3-5/3-6 persons/places 索引化完了 — 全 7 カテゴリ × 9 著作完成）**

更新履歴：
- 2026-04-27 v0.1 ドラフト作成 + 典故書名パイロット抽出（256 種・1187 件）
- 2026-04-27 v1.0 昇格：課題 A〜E 解消（CANONICAL_MAP 拡充・空海著作分離・除外辞書整備）+ 密教教学用語 19 語の本格抽出 + cross_index 共通スキーマ確定
- 2026-04-27 v1.1 昇格：Tier 2-4 梵語 IAST 抽出完了（438 種・654 件・表記揺れ統合 6 種・除外辞書 14 ノイズ語）
- 2026-04-27 v1.2 昇格：Tier 2-3 戒名向け熟語抽出完了（111 種・1971 件・起点 1 シード 11 + 起点 2 梵語漢訳 32 + 起点 3 補注ホワイトリスト 68・人手レビュー要 51 件マーカー）
- 2026-04-27 v1.3 昇格：Tier 3-5 人名抽出（81 種・1,197 件・9 分類・109/112 篇）+ Tier 3-6 地名抽出（70 種・466 件・18 分類・92/112 篇）完了
- 2026-04-27 v1.4 昇格：kaimyo-app 連携 API 設計編（§13 追加）。7 索引上に統合 API レイヤを設計、CHARACTERISTIC_TO_ICHIJI / THEME_EXPANSION / 共起ロジックを確定（候補 D 第 1 セッション）
- 2026-05-03 v1.5 昇格：**G2 着手**。dict 型 8 著作（弁顕密二教論・吽字義・声字実相義・即身成仏義・般若心経秘鍵・秘蔵宝鑰・大日経疏巻第一・三教指帰）に Tier 1（terms + citations + kukai_works）を展開。`extract_terms_dict.py` / `extract_citations_dict.py` 新設・著作別 7 索引方針確定（§14 追加）
- 2026-05-04 v1.6 昇格：**G2-B**。dict 型 8 著作に Tier 2-4 sanskrit を展開。`extract_sanskrit_dict.py` 新設。8 著作合計 1,460 canonical / 2,017 occurrences（うち大日経疏巻第一が 1,409 / 1,955 で圧倒的多数）。9 著作合計 1,898 canonical / 2,671 occurrences（改修前比 occ 4.08 倍）。著作間の梵語注記密度の差異が顕在化（弘大全集六由来の既訳 4 著作で sanskrit=0、Cowork 高品質訳の大日経疏で 1,955）。§15 追加
- 2026-05-04 v1.7 昇格：**G2-C**。dict 型 8 著作に Tier 2-3 kaimyo_jukugo を展開。`extract_kaimyo_jukugo_dict.py` 新設（性霊集版の 3 起点合成・スコアリング・ノイズ辞書を完全継承・_tmp_ prefix 廃止して git 追跡対象に）。8 著作合計 234 unique / 2,424 occurrences（うち大日経疏巻第一が 70 / 1,088 で圧倒的多数・seed_sanskrit 29 件で梵語漢訳起点も活発）。9 著作合計 345 unique / 4,395 occurrences（改修前比 occ 2.23 倍）。§16 追加
- 2026-05-04 v1.8 昇格：**G2-D**。dict 型 8 著作に Tier 3-5 persons + Tier 3-6 places を展開。`extract_persons_dict.py` / `extract_places_dict.py` 新設・共有 seed モジュール `seed_data_persons.py`（95 entries）・`seed_data_places.py`（91 entries）を新設して dict 版と既存 _tmp_ 版の双方が参照可能に。8 著作 persons 合計 157 unique / 1,216 occurrences・places 69 unique / 163 occurrences。**全 7 カテゴリで 9 著作カバレッジ達成**（terms / citations / kukai_works / sanskrit / kaimyo_jukugo / persons / places）。三教指帰の 孔子=14・荘子=6・老子=6 や中国王朝（漢=9・周=6・夏=6・楚=6・殷=5）が儒道仏比較作の特性として顕在化。§17 追加

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

## 4. kaimyo-app 連携 API 案（候補 D の前段・v1.0 暫定スケッチ）

> **本セクションは v1.0 時点の暫定スケッチ。v1.4（2026-04-27）で 7 索引（terms / citations / kukai_works / sanskrit / kaimyo / persons / places）が出揃ったため、本格設計は §13「kaimyo-app 連携 API 設計（v1.4 確定版）」に移行した。本セクションは設計の出発点として履歴保全。**

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


---

## §13 kaimyo-app 連携 API 設計（v1.4 確定版・候補 D 第 1 セッション）

横断索引化フェーズ B v1.3 で 7 索引（密教教学用語・典故書名・空海著作・梵語 IAST・戒名向け熟語・人名・地名）が出揃ったため、kaimyo-app（戒名・諷誦文・葬儀法話生成アプリ）および将来の周辺アプリ（日常法話・ブログ・教義学習アプリ等）から横断検索可能な API レイヤを v1.4 で確定する。

本節は「実装に直結する仕様書」として、エンドポイント・入出力・内部フロー・マッピングテーブル・アーキテクチャを v1.4 時点で確定し、リファレンス実装は次セッション以降（v1.5 以降）に着手する。

### 13.1 設計方針

| 方針 | 内容 |
|---|---|
| 読み取り専用 | 全エンドポイント GET のみ。索引データの書き換えは別経路（`_tmp_extract_*.py` の再実行）で行う。 |
| ステートレス REST | 認証・セッション・DB 不要。索引 JSON をメモリにロードして応答。 |
| データソース固定 | `data/mikkyou/index_shoryoshu_*.json`（7 ファイル）+ `data/kukai/shoryoshu_miyasaka.json`（本文・出典文抜粋用）。 |
| レスポンス形式 | `application/json; charset=utf-8`。原文引用部分は `gendaigoyaku` の context 抜粋。 |
| 索引非破壊 | API は索引ファイルを書き換えない。`schema_version` をレスポンスに含めて互換性を担保。 |
| CORS | kaimyo-app・blog-app 等から呼べるよう全許可（当面）。将来 origin ホワイトリスト化可。 |

### 13.2 エンドポイント一覧

統合系 2 本 + 詳細参照系 6 本 + 篇単位統合 1 本の計 9 本。

| 優先度 | パス | 用途 | データ源 |
|---|---|---|---|
| ★ 中核 | `GET /api/kaimyo/candidates` | 特性 → 戒名候補熟語 + 関連人物・地名 + 出典 | kaimyo + persons + places + sanskrit + miyasaka |
| ★ 中核 | `GET /api/houwa/citations` | テーマ → 法話用典故引用候補（篇単位スコア付き） | terms + citations + sanskrit + persons + places + miyasaka |
| 参照 | `GET /api/term/:term` | 教学用語の定義・梵語・典拠・用例 | terms + sanskrit + miyasaka |
| 参照 | `GET /api/person/:canonical` | 人名の詳細・サブカテゴリ・梵語名・出典・共起 | persons + sanskrit + miyasaka |
| 参照 | `GET /api/place/:canonical` | 地名の詳細・サブカテゴリ・出典・共起 | places + miyasaka |
| 参照 | `GET /api/citation/:canonical` | 典故書名の詳細・出現篇・前後文 | citations + miyasaka |
| 参照 | `GET /api/sanskrit/:canonical` | 梵語の詳細・表記揺れ・対応漢訳熟語 | sanskrit + kaimyo + miyasaka |
| 参照 | `GET /api/kukai-work/:canonical` | 空海著作言及の詳細 | kukai_works + miyasaka |
| 統合 | `GET /api/篇/:idx` | 篇単位で全索引のヒットを統合表示 | 7 索引 + miyasaka |

### 13.3 GET /api/kaimyo/candidates（中核 1）

故人の生前特性（自由語）から、戒名選定に適合する熟語候補を出典・関連人物地名付きで返す。

#### 13.3.1 入力（クエリパラメータ）

| パラメータ | 型 | 必須 | 既定 | 用途 |
|---|---|---|---|---|
| `characteristics` | csv string | ★ | — | 故人の特性キー（後述 CHARACTERISTIC_TO_ICHIJI のキー）。例 `学問熱心,温和` |
| `min_score` | number | — | 30 | `kaimyo_score` の下限。30 で「実用候補」、40 以上で「強推奨」程度。 |
| `limit` | int | — | 20 | 上位返却件数。 |
| `include_review` | bool | — | false | `needs_human_review=true` を含めるか。 |
| `prefer_persons` | csv string | — | — | 故人と所縁のある人名（人名索引の canonical または alias）。共起篇の候補にスコア加点。 |
| `prefer_places` | csv string | — | — | 故人と所縁のある地名。共起篇の候補にスコア加点。 |
| `length` | int (2 or 4) | — | — | 戒名熟語の字数指定。`2` で 2 字熟語のみ、`4` で 4 字熟語のみ、未指定で両方。 |

#### 13.3.2 内部フロー

```
Step 1: characteristics → 適合一字集合 ICHIJI_SET の解決
  CHARACTERISTIC_TO_ICHIJI（§13.7.1 で確定・15 特性）を参照。
  例：["学問熱心", "温和"] →
      ICHIJI_SET = {"智","慧","明","覚","悟","聡","文","博",
                    "慈","悲","仁","和","雅"}

Step 2: index_shoryoshu_kaimyo.json から候補抽出
  各 entry の `kaimyo_chars` と ICHIJI_SET の積集合が空でない entry を
  候補とする。`kaimyo_score >= min_score` でフィルタ。
  `include_review=false` なら `needs_human_review=false` のみ採用。
  `length` 指定時は jukugo の文字数で絞り込み。

Step 3: 共起ボーナスの加算
  prefer_persons / prefer_places が指定された場合、各候補熟語の
  `occurrences[].shoryoshu_idx` 集合と、人名・地名索引の同 canonical
  の `篇分布` 集合を比較し、共通篇 1 つにつき +0.5 点を `bonus_score`
  として付与（最大 +5）。

Step 4: 出典文 + 梵語原語 + 関連人物地名の付帯情報生成
  - 出典文：`occurrences[0..3].context`（最多 4 件）
  - 梵語原語：`sanskrit_origins`（kaimyo 索引に既に保持）を sanskrit
    索引と照合し `definition` を補強
  - 関連人物：候補熟語の `篇分布` と persons 索引の `篇分布` の積集合で
    共起頻度上位 5 件
  - 関連地名：同様に places 索引で共起頻度上位 3 件

Step 5: ソート & 切り詰め
  `final_score = kaimyo_score + bonus_score` 降順、`limit` 件で切る。
```

#### 13.3.3 出力スキーマ

```jsonc
{
  "query": {
    "characteristics": ["学問熱心", "温和"],
    "ichiji_resolved": ["智","慧","明","覚","悟","聡","文","博",
                        "慈","悲","仁","和","雅"],
    "min_score": 30,
    "limit": 20,
    "length": null
  },
  "results": [
    {
      "rank": 1,
      "jukugo": "智慧",
      "length": 2,
      "kaimyo_chars": ["智","慧"],
      "kaimyo_score": 61.7,
      "bonus_score": 0.0,
      "final_score": 61.7,
      "source": "seed_sanskrit",
      "needs_human_review": false,
      "sanskrit_origins": [
        {
          "canonical": "prajñā",
          "definition": "智慧。般若。",
          "occurrence_count_in_corpus": 14,
          "linked_in_index": true
        }
      ],
      "matched_ichiji": ["智","慧"],
      "occurrence_count": 63,
      "篇分布_count": 27,
      "examples": [
        {
          "shoryoshu_idx": 0,
          "篇名": "真済序",
          "巻": "巻第一",
          "context": "...智慧の海に...",
          "context_position": 1234
        }
      ],
      "related_persons": [
        {"canonical": "空海", "subcategory": "buddhist_master_japan", "co_occurrence_count": 12},
        {"canonical": "大日如来", "subcategory": "buddhist_buddha_bodhisattva", "co_occurrence_count": 8}
      ],
      "related_places": [
        {"canonical": "高野山", "subcategory": "mountain_japan", "co_occurrence_count": 4}
      ]
    }
  ],
  "metadata": {
    "total_matched_before_limit": 47,
    "schema_version": "1.4.0",
    "data_corpus": "shoryoshu_miyasaka_v_phase2_complete",
    "generated_at": "2026-04-27T..."
  }
}
```

#### 13.3.4 エラーレスポンス

```jsonc
// 400: characteristics 未指定
{"error": "MISSING_PARAMETER", "message": "characteristics is required", "schema_version": "1.4.0"}

// 400: 未定義の特性キー
{"error": "UNKNOWN_CHARACTERISTIC", "message": "characteristic '◯◯' is not in CHARACTERISTIC_TO_ICHIJI",
 "available": ["学問熱心","温和", ...], "schema_version": "1.4.0"}

// 200 with empty results: 該当なし
{"query": {...}, "results": [], "metadata": {"total_matched_before_limit": 0, ...}}
```

### 13.4 GET /api/houwa/citations（中核 2）

法話・諷誦文・ブログのテーマ語から、性霊集中で関連する典故・教学用語・梵語・人名・地名を統合検索し、篇単位でスコア付き返却する。

#### 13.4.1 入力

| パラメータ | 型 | 必須 | 既定 | 用途 |
|---|---|---|---|---|
| `theme` | string | ★ | — | 法話テーマ。THEME_EXPANSION（§13.7.2）のキーまたは自由語。 |
| `expand` | bool | — | true | THEME_EXPANSION で多言語展開するか（false ならテーマ語そのもののみ）。 |
| `limit` | int | — | 10 | 上位返却篇数。 |
| `include_persons` | bool | — | true | 関連人名を含めるか。 |
| `include_places` | bool | — | false | 関連地名を含めるか。 |
| `min_hits` | int | — | 1 | 篇あたり最低ヒット数（合計）。 |

#### 13.4.2 内部フロー

```
Step 1: テーマ展開
  THEME_EXPANSION[theme] → 関連語 list（漢字熟語 + 梵語 IAST + 異表記）。
  expand=false ならテーマ語そのもの 1 件のみ。

Step 2: 並行索引検索
  各関連語について以下を検索：
    a. terms 索引：term または matched_forms.form と一致
    b. citations 索引：term または aliases と一致
    c. sanskrit 索引：canonical または aliases と一致
    d. （include_persons）persons 索引：canonical または aliases と一致
    e. （include_places）places 索引：canonical または aliases と一致

Step 3: 篇単位の集約
  各ヒットを `shoryoshu_idx` でグルーピング。1 篇に対し各カテゴリのヒット
  数をカウント。

Step 4: 篇スコアリング
  篇スコア = Σ(category_weight × hit_count_in_篇)
  category_weight:
    terms      = 3 （教学用語の直接ヒットは最重要）
    citations  = 2
    sanskrit   = 2
    persons    = 1
    places     = 1
  `min_hits` 未満の篇は除外。

Step 5: 出典文抜粋
  各篇について shoryoshu_miyasaka.json[idx].ページ[0].gendaigoyaku から
  最初のヒット位置 ±150 字程度を抜粋（`context_excerpt`）。

Step 6: ソート & 切り詰め
  篇スコア降順、limit 件で切る。
```

#### 13.4.3 出力スキーマ

```jsonc
{
  "query": {
    "theme": "無常",
    "expanded_terms": ["無常", "anitya", "生滅", "変化"],
    "limit": 10,
    "include_persons": true,
    "include_places": false
  },
  "citations": [
    {
      "rank": 1,
      "shoryoshu_idx": 7,
      "篇名": "...",
      "巻": "巻第一",
      "score": 12,
      "hits": {
        "terms": [{"term": "...", "matched_form": "無常", "count": 3}],
        "citations": [{"term": "涅槃経", "count": 1}],
        "sanskrit": [{"canonical": "anitya", "count": 1}],
        "persons": [{"canonical": "釈迦", "subcategory": "buddhist_master_india"}],
        "places": []
      },
      "context_excerpt": "...生死無常の理を観じて...（200〜400 字）",
      "字数": {"書き下し": 1582, "現代語訳": 4023, "倍率": 2.54}
    }
  ],
  "metadata": {
    "total_篇_matched": 23,
    "schema_version": "1.4.0",
    "data_corpus": "shoryoshu_miyasaka_v_phase2_complete"
  }
}
```

### 13.5 詳細参照系（/api/term, /person, /place, /citation, /sanskrit, /kukai-work）

各索引のエントリ詳細を、共起情報・出典文・関連索引へのリンクを補強した形で返す。kaimyo-app の「もっと見る」「典拠を表示」UI で利用。

#### 13.5.1 共通入力

```
GET /api/term/:term
GET /api/person/:canonical
GET /api/place/:canonical
GET /api/citation/:canonical
GET /api/sanskrit/:canonical
GET /api/kukai-work/:canonical

? full_context=false   (任意・true なら occurrences の前後文を 400 字に拡張)
? lang=ja              (将来の多言語対応)
```

#### 13.5.2 共通レスポンス構造

```jsonc
{
  "query": {"endpoint": "term", "key": "三密"},
  "entry": {
    // 元索引のエントリ全体（schema_version も含む）
    ...
  },
  "related": {
    "kaimyo_jukugo": [
      {"jukugo": "三密", "kaimyo_score": 58.1, "needs_human_review": false}
    ],
    "sanskrit": [{"canonical": "tri-guhya"}],
    "co_occurring_persons": [
      {"canonical": "空海", "subcategory": "...", "co_count": 28}
    ],
    "co_occurring_places": [...],
    "co_occurring_citations": [...]
  },
  "metadata": {"schema_version": "1.4.0"}
}
```

存在しない canonical の場合は 404：

```jsonc
{"error": "NOT_FOUND", "endpoint": "person", "key": "存在しない人名",
 "schema_version": "1.4.0"}
```

### 13.6 GET /api/篇/:idx（統合 1 本）

故人の生涯・趣向に近い篇を提示する用途。idx を指定すると、その篇に含まれる全索引のヒットを統合した「篇カルテ」を返す。

#### 13.6.1 入力

```
GET /api/篇/:idx           (idx は 0..111)
? include_full_text=false  (true で書き下し + 訳の全文を含める。既定 false)
? excerpt_chars=300        (書き下し・訳の冒頭抜粋字数)
```

#### 13.6.2 出力スキーマ

```jsonc
{
  "shoryoshu_idx": 1,
  "篇名": "山に遊んで仙を慕う詩",
  "巻": "巻第一",
  "page_count": 1,
  "字数": {"書き下し": 1482, "現代語訳": 3551, "倍率": 2.40},
  "indices": {
    "terms": [{"term": "三密", "count": 2, "kaimyo_suitable": true}],
    "citations": [{"term": "荘子", "count": 5}],
    "sanskrit": [{"canonical": "...", "count": 1}],
    "kaimyo_jukugo": [{"jukugo": "...", "score": 45.2, "review": false}],
    "persons": [{"canonical": "荘子", "subcategory": "chinese_classical", "count": 12}],
    "places": [{"canonical": "崑崙", "subcategory": "mountain_china", "count": 1}],
    "kukai_works": []
  },
  "totals": {
    "terms": 4, "citations": 8, "sanskrit": 3,
    "kaimyo_jukugo": 9, "persons": 7, "places": 3
  },
  "excerpts": {
    "kakikudashi_head": "...（excerpt_chars 字）",
    "gendaigoyaku_head": "...（excerpt_chars 字）"
  },
  "metadata": {"schema_version": "1.4.0"}
}
```

### 13.7 マッピングテーブル v1.4 確定

API の入力（人間が直接書く特性・テーマ）を索引のキー（一字・正規語）に変換する 2 つのテーブルを v1.4 で確定する。

#### 13.7.1 CHARACTERISTIC_TO_ICHIJI（特性 → 適合一字）

15 特性を網羅。各値の一字は KAIMYO_ICHIJI（85 字）の部分集合。kaimyo-app 側の UI ラベルもこのキーをそのまま採用する想定。

| キー | 適合一字 |
|---|---|
| `学問熱心` | 智・慧・明・覚・悟・聡・文・博 |
| `温和` | 慈・悲・仁・和・雅 |
| `清廉` | 浄・信・清・澄・寂・静 |
| `信仰深い` | 真・信・誓・願・念・仏・尊 |
| `志高い` | 志・誓・願・光・栄・徳 |
| `慈愛` | 慈・悲・愛・恵・徳 |
| `勤勉` | 精・勤・行・進 |
| `寛大` | 広・大・寛・容・仁 |
| `質実` | 真・実・正・直・本 |
| `達観` | 玄・空・無・寂・静・悟・覚 |
| `風雅` | 雅・月・華・雲・霞・清 |
| `自然親和` | 山・海・泉・水・河・月・華・蓮 |
| `不動` | 金・剛・堅・定 |
| `長寿` | 永・長・久 |
| `光明` | 光・明・照・栄・華 |

実装では JSON 設定ファイル `data/mikkyou/api_mappings.json` 内の `characteristic_to_ichiji` キーに格納し、API サーバ起動時にロードする。kaimyo-app からも同ファイルを参照可能。将来の拡張は当ファイルへの追記で対応。

#### 13.7.2 THEME_EXPANSION（法話テーマ → 多言語展開）

10 テーマを v1.4 で確定。各値は索引で実際にヒットする表記（梵語 IAST 含む）の集合。

| キー | 展開語（漢字 + 梵語 + 異表記） |
|---|---|
| `無常` | 無常・anitya・生滅・変化 |
| `慈悲` | 慈悲・karuṇā・mahā-karuṇā・大悲・慈愛・慈 |
| `智慧` | 智慧・prajñā・般若・智・慧・明 |
| `空` | 空・śūnya・śūnyatā・空観・空性 |
| `解脱` | 解脱・mokṣa・涅槃・nirvāṇa |
| `即身成仏` | 即身成仏・siddhi・成就・成仏 |
| `大日如来` | 大日・大日如来・vairocana・mahāvairocana・遮那・毘盧遮那 |
| `三密` | 三密・身口意・tri-guhya |
| `法身` | 法身・dharmakāya・本性 |
| `菩提心` | 菩提心・bodhicitta・菩提・bodhi |

実装では同じ `data/mikkyou/api_mappings.json` の `theme_expansion` キーに格納。`/api/houwa/citations?expand=true` で参照される。

未掲載のテーマ（自由語）が来た場合は `expand=true` でも展開せずテーマ語そのもののみで検索する（`expanded_terms` には 1 件のみ含まれる）。

#### 13.7.3 共起マトリックス計算ロジック

API サーバ起動時に、7 索引の `occurrences[].shoryoshu_idx` または `篇分布` から「篇 × 索引エントリ」の二部グラフを構築し、エントリペアの共起篇数を求める。

```
preprocessing (起動時 1 回):
  for each pair (a, b) in (kaimyo_jukugo × persons),
                        (kaimyo_jukugo × places),
                        (terms × persons),
                        (terms × places),
                        (kaimyo_jukugo × terms),
                        (persons × persons),
                        (persons × places):
    co_occurrence[(a, b)] = |篇分布(a) ∩ 篇分布(b)|

メモリ概算:
  人名 81 × 地名 70 = 5,670 ペア → ~ 0.1 MB
  熟語 111 × 人名 81 = 8,991 ペア → ~ 0.2 MB
  全マトリックスでも ~ 数 MB 以内に収まる。
```

`/api/kaimyo/candidates` の Step 3（prefer_persons ボーナス）と Step 4（関連人物地名）、`/api/term/:term` 等の `co_occurring_*` フィールドはこのマトリックスから返す。

### 13.8 アーキテクチャ

#### 13.8.1 推奨実装スタック

| 選択肢 | メリット | デメリット |
|---|---|---|
| **TypeScript + Next.js API Routes** | kaimyo-app（同じ Next.js 想定）と同一リポジトリで運用可。fetch ベースで kaimyo-app 内部呼び出しに最適。 | 索引ファイルの読み込みコードを TS で書く必要。 |
| **Python + FastAPI** | 索引生成スクリプト（`_tmp_extract_*.py`）と同言語で索引ロジックを共有可能。pydantic で型バリデーション。 | kaimyo-app から HTTP 経由必須（追加プロセス）。 |

第 1 候補：**Python + FastAPI**（索引生成 Python と整合・型安全・OpenAPI 自動生成）。kaimyo-app は HTTP で呼ぶ。

#### 13.8.2 起動シーケンス

```
1. data/mikkyou/index_shoryoshu_*.json（7 ファイル）をメモリにロード
2. data/kukai/shoryoshu_miyasaka.json をメモリにロード（出典抜粋用）
3. data/mikkyou/api_mappings.json をロード（CHARACTERISTIC_TO_ICHIJI 等）
4. 共起マトリックスを構築（§13.7.3）
5. 各エントリの逆引き辞書を構築：
   - alias_to_canonical: 全 aliases → canonical のフラット辞書
   - 篇_to_entries: 篇 idx → 各索引のヒットエントリ集合
6. listen on port（既定 8000）
```

総メモリフットプリント概算：3〜6 MB（索引）+ 5〜8 MB（miyasaka 全文）+ 数 MB（共起マトリックス）= 15〜20 MB 程度。

#### 13.8.3 デプロイ

- 開発：`uvicorn main:app --reload --port 8000`（local）
- 本番：Vercel Functions または Cloud Run（FastAPI 対応）
- kaimyo-app からは `process.env.BUDDHIST_API_URL` 経由で呼ぶ

### 13.9 実装ロードマップ

| セッション | 作業 | 成果物 |
|---|---|---|
| **v1.4（本セッション）** | **§13 仕様書追加 + マッピング 2 表確定** | **cross_index_spec.md v1.4** |
| v1.5 | `data/mikkyou/api_mappings.json` 生成 + 索引ロード基盤 + `/api/篇/:idx` 実装（最も単純） | `api_server/`（FastAPI 雛形）+ 篇エンドポイント |
| v1.6 | `/api/term`・`/api/person`・`/api/place`・`/api/citation`・`/api/sanskrit`・`/api/kukai-work` 実装 + 共起マトリックス構築 | 詳細参照系 6 本完成 |
| v1.7 | `/api/kaimyo/candidates` 実装（CHARACTERISTIC_TO_ICHIJI 解決 + 共起ボーナス + 関連人物地名） | 中核 1 完成 |
| v1.8 | `/api/houwa/citations` 実装（THEME_EXPANSION + 篇スコアリング + context 抜粋） | 中核 2 完成 |
| v1.9 | OpenAPI yaml 整備 + kaimyo-app との結合テスト + README + デプロイ | 本番運用化 |

総工数：5〜6 セッション（v1.5〜v1.9）+ 本セッション（v1.4 仕様確定）= 6〜7 セッション。

### 13.10 v1.4 完成度評価

- ✅ **9 エンドポイントの仕様確定**：中核 2（kaimyo/candidates・houwa/citations）+ 詳細参照系 6 本 + 篇単位統合 1 本。
- ✅ **入出力スキーマの厳密化**：JSON レスポンスの構造を v1.4 で固定し、`schema_version` を全レスポンスに含める。
- ✅ **マッピングテーブル 2 表確定**：CHARACTERISTIC_TO_ICHIJI 15 特性 + THEME_EXPANSION 10 テーマ。`api_mappings.json` として外部設定化。
- ✅ **共起マトリックス計算ロジック明文化**：起動時前計算で API 応答性能を担保。
- ✅ **アーキテクチャ第 1 候補確定**：Python + FastAPI（索引生成スクリプトと言語統一）。
- ⏭️ 次セッション（v1.5）以降：`api_server/` ディレクトリ新設、`/api/篇/:idx` から実装開始（最も単純なエンドポイント）。

### 13.11 候補 D 進捗

| サブステップ | 状態 |
|---|---|
| §4 v1.0 暫定スケッチ → §13 v1.4 確定版へ昇格 | ✅ 本セッション完了 |
| 9 エンドポイント仕様策定 | ✅ 本セッション完了 |
| マッピング 2 表確定 | ✅ 本セッション完了 |
| アーキテクチャ第 1 候補確定 | ✅ 本セッション完了 |
| `api_mappings.json` 生成 | ⏭️ v1.5 |
| `api_server/` リファレンス実装 | ⏭️ v1.5〜v1.8 |
| OpenAPI yaml + デプロイ | ⏭️ v1.9 |

候補 D 全体（3〜5 セッション見積→ 仕様分が予想より厚いため 5〜6 セッションに修正）：本セッションが第 1 セッションとして完了。

---

## 14. G2 dict 型 8 著作 Tier 1 索引化（v1.5・2026-05-03）

設計方針メモ `kaimyo-app/設計方針メモ_2026-05-03_真言宗教えデータ整理_buddhist-data-api倉庫設計.md` のフェーズ 2 候補 G2「17 著作横断索引化」の第 1 弾。**性霊集（list 型）**だけだった索引基盤を **dict 型 8 著作**にも展開し、横断検索の対象を 1 → 9 著作に拡張した。

### 14.1 着手判断（2026-05-03 ケンシン決定）

3 つの設計判断：

| 判断軸 | 採用案 | 棄却案 |
|---|---|---|
| 索引構成 | **著作別 7 索引（同パターン拡張）** | 全著作統合 1 本／ハイブリッド |
| 着手スコープ | **Tier 1 から 8 著作分**（terms + citations + kukai_works） | 1 著作で 7 索引フルセット／全 8×7 一気 |
| 抽出フィールド | **gendaigoyaku のみ**（性霊集と統一） | gendaigoyaku + kakikudashi／全 3 フィールド |

著作別 7 索引方針により、`index_<corpus_id>_<category>.json` 命名で各著作ごとに索引が完結する。横断検索が必要になったら集約ファイル（`index_<category>_all.json` 等）を別途作成する余地を残す。

### 14.2 dict 型コーパスの索引化仕様

性霊集（list 型・112 篇分割）と異なり、dict 型コーパス（弁顕密二教論等）は **トップレベル `gendaigoyaku` 単一文字列**を持つ。索引化仕様：

| 項目 | list 型（性霊集） | dict 型（弁顕密二教論等） |
|---|---|---|
| 抽出ソース | `entry.ページ[].gendaigoyaku` | `top.gendaigoyaku` |
| 位置キー | `shoryoshu_idx` + `篇名` + `巻` + `page_idx` + `context_position` | `corpus_id` + `context_position` |
| 篇分布 | あり（`篇分布: [int]`） | なし（単一連続テキスト） |
| 篇境界 | 112 entries | なし |
| summary | `covered_shoryoshu_idx_count` | `gendaigoyaku_length` |

dict 型 occurrences の例：

```json
{
  "corpus_id": "nikyo-ron",
  "context": "...仏陀を法身、応身、化身の三身とするうち、応身、化身が説かれる...",
  "context_position": 122,
  "sanskrit_in_context": []
}
```

### 14.3 新設スクリプト

- `_dev_references/extract_terms_dict.py`（dict 型 19 語密教教学用語抽出・extract_terms.py の dict 版）
- `_dev_references/extract_citations_dict.py`（dict 型 典故書名抽出・extract_citations.py の dict 版）

両スクリプトとも `--corpus <filename>` または `--corpus all` で実行。19 語辞書・CANONICAL_MAP・除外辞書・KUKAI_WORKS 分類は性霊集版と完全互換（コードレベルで同一定義をコピー）。

### 14.4 G2 第 1 弾の生成結果（2026-05-03）

#### 14.4.1 terms（密教教学用語）

| 著作 | gendaigoyaku 字数 | 一致語数 / 19 | 延べ件数 | 上位 3 |
|---|---|---|---|---|
| nikyo-ron（弁顕密二教論）| 38,816 | 11 | 360 | 法身=101 / 密教=92 / 大日=60 |
| ujiji（吽字義）| 21,863 | 11 | 170 | 大日=74 / 阿字=28 / 法界=16 |
| shoji-jisso（声字実相義）| 14,087 | 10 | 136 | 大日=72 / 法身=24 / 真言=16 |
| sokushin-jobutsu（即身成仏義）| 20,298 | 14 | 361 | 大日=153 / 法身=54 / 密教=42 |
| hannya-hiken（般若心経秘鍵）| 14,186 | 7 | 105 | 密教=40 / 真言=30 / 大日=23 |
| hizo-houyaku（秘蔵宝鑰）| 75,246 | 13 | 257 | 大日=62 / 真言=40 / 密教=36 |
| dainichikyo-sho-vol1（大日経疏巻第一）| 101,714 | 14 | 286 | 真言=58 / 遮那=42 / 大悲=38 |
| sankyo-shiki（三教指帰）| 44,863 | 2 | 3 | 真言=2 / 法身=1 |
| **合計** | **331,073** | - | **1,678** | - |

意味的妥当性確認：
- **三教指帰**は空海 24 歳の儒道仏比較作で、密教教学用語が極端に少ない（真言=2・法身=1 のみ）のは妥当
- **即身成仏義**で大日=153・法身=54 が突出（中心教義の本拠）
- **大日経疏**で真言=58・遮那=42 が首位（『大日経』疏としての性格）
- **般若心経秘鍵**で密教=40 が首位（密教観点からの心経解釈）

#### 14.4.2 citations（典故書名・他者著作）

| 著作 | citations 異なり | 延べ件数 | 上位 3 |
|---|---|---|---|
| nikyo-ron | 51 | 142 | 大智度論=13 / 楞伽経=12 / 釈摩訶衍論=10 |
| ujiji | 14 | 37 | 大日経疏=12 / 大日経=4 / 守護国界主陀羅尼経=3 |
| shoji-jisso | 12 | 27 | 大日経=12 / 大日経疏=2 / 瑜伽師地論=2 |
| sokushin-jobutsu | 17 | 44 | 大日経=21 / 金剛頂経=5 / 毘盧遮那三摩地法=3 |
| hannya-hiken | 14 | 45 | 般若心経=21 / 大般若経=4 / 大日経疏=3 |
| hizo-houyaku | 57 | 139 | 大日経=26 / 法華経=24 / 釈摩訶衍論=10 |
| dainichikyo-sho-vol1 | 106 | 179 | 大智度論=25 / 大日経=11 / 法華経=6 |
| sankyo-shiki | 21 | 35 | 詩経=7 / 礼記=4 / 法華経=3 |
| **合計** | - | **648** | - |

意味的妥当性確認：
- **三教指帰**で漢籍（詩経・礼記・易経・書経）が首位 → 儒道仏比較作の性格と整合
- **般若心経秘鍵**で『般若心経』本体が 21 件首位 → 心経の註釈書としての性格と整合
- **大日経疏**は 106 種で最多典故 → 注釈書として網羅的引用の特性

#### 14.4.3 kukai_works（空海著作・性霊集編纂物）

| 著作 | 異なり | 延べ件数 | 内訳 |
|---|---|---|---|
| nikyo-ron | 3 | 8 | 菩提心論=5 / 秘蔵宝鑰=2 / 弁顕密二教論=1 |
| ujiji | 0 | 0 | — |
| shoji-jisso | 1 | 2 | 即身成仏義=2 |
| sokushin-jobutsu | 2 | 5 | 菩提心論=4 / 弁顕密二教論=1 |
| hannya-hiken | 1 | 1 | 菩提心論=1 |
| hizo-houyaku | 2 | 19 | 菩提心論=14 / 十住心論=5 |
| dainichikyo-sho-vol1 | 3 | 11 | 即身成仏義=5 / 弁顕密二教論=3 / 般若心経秘鍵=3 |
| sankyo-shiki | 1 | 1 | 三教指帰=1 |

extract_citations_dict.py で KUKAI_WORKS 分類辞書を性霊集版から拡張：弁顕密二教論・吽字義・即身成仏義・声字実相義・般若心経秘鍵・秘蔵宝鑰・十住心論・三教指帰・聾瞽指帰・御請来目録・性霊集・遍照発揮性霊集・菩提心論を追加（各「空海著作」または「空海関連」タグ付き）。

### 14.5 横断検索の現状

`_corpus_manifest.json` の `summary.indexed_corpora` ブロックで横断対応状況を一元管理：

```
indexed_corpora:
  terms:         9 / 10 primary_corpus（菩提心論除く）
  citations:     9 / 10
  kukai_works:   9 / 10
  sanskrit:      1 / 10（性霊集のみ・Tier 2-4）
  kaimyo_jukugo: 1 / 10（性霊集のみ・Tier 2-3）
  persons:       1 / 10（性霊集のみ・Tier 3-5）
  places:        1 / 10（性霊集のみ・Tier 3-6）
```

**Tier 1 全 9 著作完成。Tier 2-3 は性霊集のみ。**

### 14.6 残作業（G2 後続）

| サブステップ | 内容 | 工数 |
|---|---|---|
| ✅ G2-A | dict 型 8 著作の Tier 1 索引（terms + citations + kukai_works） | 1 セッション（本セッション） |
| ⏭️ G2-B | dict 型 8 著作の Tier 2-4 sanskrit 抽出（extract_sanskrit_dict.py 新設） | 1〜2 セッション |
| ⏭️ G2-C | dict 型 8 著作の Tier 2-3 kaimyo_jukugo 抽出（extract_kaimyo_jukugo_dict.py 新設） | 1〜2 セッション |
| ⏭️ G2-D | dict 型 8 著作の Tier 3-5/6 persons / places 抽出（extract_persons_dict.py / extract_places_dict.py 新設） | 1〜2 セッション |
| ⏭️ G2-E | 横断集約ファイル（index_<category>_all.json）生成スクリプト | 0.5 セッション |
| ⏭️ G2-F | 菩提心論の gendaigoyaku 取込後に再索引化 | 0.5 セッション |

### 14.7 v1.5 完成度評価

- ✅ **dict 型コーパスの索引化フローを確立**：トップレベル gendaigoyaku から occurrence を抽出し `corpus_id` + `context_position` で位置特定
- ✅ **著作別 7 索引方針**：`index_<corpus>_<category>.json` 命名規則で 9 著作 × 最大 7 カテゴリの索引体系を確立
- ✅ **24 索引ファイル新設**（8 著作 × 3 カテゴリ・合計 940 KB）：合計 1,678 件の terms + 648 件の citations + 47 件の kukai_works を索引化
- ✅ **manifest 統合**：`_corpus_manifest.json` の各 file entry に `index_status` ブロック追加・`summary.indexed_corpora` で全体可視化
- ✅ **NULL バイト 0 件・JSON 整合性 OK**（全 24 ファイル）
- ⏭️ 次セッション（G2-B 以降）：sanskrit / kaimyo_jukugo / persons / places の dict 型版抽出スクリプトを順次実装

### 14.8 設計方針メモとの対応

`kaimyo-app/設計方針メモ_2026-05-03_真言宗教えデータ整理_buddhist-data-api倉庫設計.md` のフェーズ 2 G2 進捗：

```
G1 ✅ L1 スキーマ統一（2026-05-03 commit c1e9494・案 A 既存破壊なし）
G2 🟡 L1 横断索引化
    G2-A ✅ Tier 1 dict 8 著作（本セッション）
    G2-B〜F ⏭️ Tier 2-4 段階展開
G3 ⏭️ 未着手 8 著作のロードマップ
G4 ⏭️ L2 字索引の新設
G5 ⏭️ L3 by_* 汎用 endpoint の整備
G6 ⏭️ kaimyo-app 暫定ハードコード 3 種の置き換え API
```

---

## 15. G2-B dict 型 8 著作 Tier 2-4 sanskrit 索引化（v1.6・2026-05-04）

G2-A（§14）に続く第 2 弾。性霊集に続いて dict 型 8 著作の梵語 IAST を索引化し、横断検索の対象を sanskrit でも 1 → 9 著作に拡張した。

### 15.1 新設スクリプト

`_dev_references/extract_sanskrit_dict.py`（dict 型 IAST 梵語抽出・extract_sanskrit.py の dict 版）

- `--corpus <filename>` または `--corpus all` で実行
- 正規表現・EXCLUDE_TOKENS（14 ノイズ語）・ALIAS_MAP・canonicalize ロジックは性霊集版と完全互換
- トップレベル `gendaigoyaku` のみを抽出対象とする（kakikudashi・genten・text は対象外）

### 15.2 G2-B の生成結果（2026-05-04）

| 著作 | gendaigoyaku 字数 | canonical 数 | 延べ件数 | IAST 含有 | ASCII 純粋 | 上位 3 |
|---|---|---|---|---|---|---|
| nikyo-ron（弁顕密二教論）| 38,816 | 0 | 0 | 0 | 0 | — |
| ujiji（吽字義）| 21,863 | 35 | 37 | 13 | 22 | dha=2 / hetu=2 / bandhana=1 |
| shoji-jisso（声字実相義）| 14,087 | 0 | 0 | 0 | 0 | — |
| sokushin-jobutsu（即身成仏義）| 20,298 | 9 | 11 | 1 | 8 | bodhi=2 / buddha=2 / anutpāda=1 |
| hannya-hiken（般若心経秘鍵）| 14,186 | 7 | 14 | 5 | 2 | bhā=2 / buddha=2 / mahā=2 |
| hizo-houyaku（秘蔵宝鑰）| 75,246 | 0 | 0 | 0 | 0 | — |
| dainichikyo-sho-vol1（大日経疏巻第一）| 101,714 | **1,409** | **1,955** | **1,144** | **265** | upāya=14 / prapañca=11 / samādhi=10 |
| sankyo-shiki（三教指帰）| 44,863 | 0 | 0 | 0 | 0 | — |
| **8 著作合計** | **331,073** | **1,460** | **2,017** | **1,163** | **297** | — |

### 15.3 重要な発見：著作間の梵語注記密度の格差

dict 型 8 著作の sanskrit 索引化で、各著作の現代語訳補注密度の格差が顕在化した：

**Cowork 高品質訳（典故・梵語注記が濃密）**
- dainichikyo-sho-vol1（大日経疏巻第一）：1,955 件・梵語注記が圧倒的多数（『大日経』疏として大量の Sanskrit 引用）
- 性霊集 112 篇（参考・改修前から）：654 件

**ujiji・hannya-hiken・sokushin-jobutsu（部分的に Cowork 補注あり）**
- 11〜37 件・密教字義論（吽字義）等で字源の梵語が直接言及されているケース

**弘大全集六 PDF Gemini OCR 由来の既訳（補注が薄い）**
- nikyo-ron（弁顕密二教論）：0 件
- shoji-jisso（声字実相義）：0 件
- hizo-houyaku（秘蔵宝鑰）：0 件
- sankyo-shiki（三教指帰）：0 件

これは現代語訳の **品質特性** であり、既訳の限界を反映している。将来 Tier 2-4 を充実させる場合、これら 4 著作の現代語訳を Cowork 高品質モードで再構築する候補（候補 G2-G）も検討余地あり。

### 15.4 横断検索の現状（2026-05-04 時点）

`_corpus_manifest.json` の `summary.indexed_corpora`：

```
indexed_corpora:
  terms:         9 / 10 primary_corpus（菩提心論除く）
  citations:     9 / 10
  kukai_works:   9 / 10
  sanskrit:      9 / 10  ← G2-B で 1 → 9 に拡大
  kaimyo_jukugo: 1 / 10
  persons:       1 / 10
  places:        1 / 10
```

**Tier 1 + sanskrit 全 9 著作完成。** Tier 2-3（kaimyo_jukugo / persons / places）は性霊集のみ。

### 15.5 改修前後の比較（occurrences）

| カテゴリ | 改修前（性霊集のみ）| dict 8 著作追加 | 9 著作合計 | 倍率 |
|---|---:|---:|---:|---:|
| sanskrit | 654 | +2,017 | 2,671 | **4.08x** |

dainichikyo-sho-vol1 の 1,955 件が突出して牽引。残り 7 著作分は合計 62 件で、補注密度の品質次第で大きく動く範囲。

### 15.6 残作業（G2 後続）

| サブステップ | 内容 | 工数 |
|---|---|---|
| ✅ G2-A | dict 型 8 著作の Tier 1（terms + citations + kukai_works）| 1 セッション（2026-05-03）|
| ✅ G2-B | dict 型 8 著作の Tier 2-4 sanskrit | 1 セッション（本セッション）|
| ⏭️ G2-C | dict 型 8 著作の Tier 2-3 kaimyo_jukugo | 1〜2 セッション |
| ⏭️ G2-D | dict 型 8 著作の Tier 3-5/6 persons / places | 1〜2 セッション |
| ⏭️ G2-E | 横断集約ファイル（index_<category>_all.json）生成 | 0.5 セッション |
| ⏭️ G2-F | 菩提心論 gendaigoyaku 取込後の再索引化 | 0.5 セッション |
| ⏭️ G2-G（新設候補）| 既訳 4 著作（nikyo-ron / shoji-jisso / hizo-houyaku / sankyo-shiki）の Cowork 高品質訳化（梵語注記濃密化）| 著作 1 つあたり 5〜10 セッション |

### 15.7 v1.6 完成度評価

- ✅ **dict 型 sanskrit 索引化フロー確立**：トップレベル gendaigoyaku から IAST 候補を網羅抽出し、`corpus_id` + `context_position` で位置特定
- ✅ **8 著作 sanskrit 索引完成**：合計 1,460 canonical / 2,017 occurrences（NULL バイト 0 件・JSON 整合 OK）
- ✅ **重要発見：補注密度の品質格差**：Cowork 高品質訳と弘大全集六 OCR 既訳で sanskrit カバレッジに大差。G2-G 候補として記録
- ✅ **manifest 統合**：`summary.indexed_corpora.sanskrit` を 1 → 9 に更新
- ⏭️ 次セッション（G2-C 以降）：kaimyo_jukugo / persons / places の dict 型版抽出

---

## 16. G2-C dict 型 8 著作 Tier 2-3 kaimyo_jukugo 索引化（v1.7・2026-05-04）

G2-A（§14）・G2-B（§15）に続く第 3 弾。性霊集に続いて dict 型 8 著作の戒名向け熟語を索引化し、横断検索の対象を kaimyo_jukugo でも 1 → 9 著作に拡張した。

### 16.1 新設スクリプト

`_dev_references/extract_kaimyo_jukugo_dict.py`（dict 型 戒名向け熟語抽出）

- `_tmp_extract_kaimyo_jukugo.py`（性霊集・list 型）の dict 版
- 性霊集版の `_tmp_` prefix（gitignored）を廃止して **git 追跡対象**に変更
- KAIMYO_ICHIJI（85 字戒名適合一字辞書）・SANSKRIT_TO_KAIMYO_JUKUGO（51 エントリ・梵語漢訳対応）・DOCTRINAL_2CHAR_WHITELIST（68 語ホワイトリスト）・KAIMYO_NOISE（140 語ノイズ除外）を完全継承
- スコアリング（freq + doctrinal + ichiji + aesthetic、0〜75 点）も完全互換
- `--corpus <filename>` または `--corpus all` で実行
- 各 dict 著作の `index_<corpus>_terms.json` と `index_<corpus>_sanskrit.json` を起点として参照

### 16.2 G2-C の生成結果（2026-05-04）

| 著作 | unique | matched | occurrences | seed_terms | seed_sanskrit | paren | review |
|---|---|---|---|---|---|---|---|
| nikyo-ron（弁顕密二教論）| 36 | 33 | 310 | 11 | 0 | 25 | 21 |
| ujiji（吽字義）| 25 | 20 | 177 | 11 | 2 | 12 | 11 |
| shoji-jisso（声字実相義）| 16 | 12 | 137 | 11 | 0 | 5 | 5 |
| sokushin-jobutsu（即身成仏義）| 22 | 18 | 333 | 11 | 2 | 9 | 9 |
| hannya-hiken（般若心経秘鍵）| 19 | 13 | 136 | 11 | 4 | 4 | 4 |
| hizo-houyaku（秘蔵宝鑰）| 32 | 28 | 236 | 11 | 0 | 21 | 20 |
| dainichikyo-sho-vol1（大日経疏巻第一）| **70** | **64** | **1,088** | 11 | **29** | 30 | 27 |
| sankyo-shiki（三教指帰）| 14 | 5 | 7 | 11 | 0 | 3 | 3 |
| **8 著作合計** | **234** | **193** | **2,424** | **88** | **37** | **109** | **100** |

### 16.3 著作別の戒名候補上位（kaimyo_score 順）

| 著作 | 上位 5 |
|---|---|
| nikyo-ron | 真言(67.8) / 法身(64.1) / 大日(59.4) / 大悲(55.7) / 三密(52.5) |
| ujiji | 真言(62.2) / 大日(60.4) / 真実(56.2) / 法界(52.6) / 法身(53.1) |
| shoji-jisso | 真言(63.2) / 大日(60.0) / 法身(56.6) / 法界(48.9) / 三密(45.6) |
| sokushin-jobutsu | 真言(67.2) / 大日(63.4) / 法身(60.6) / 三密(53.1) / 大悲(54.7) |
| hannya-hiken | 真言(66.2) / 大日(54.6) / 般若(38.6) / 仏陀(41.6) / 法界(48.9) |
| hizo-houyaku | 真言(66.8) / 大日(60.0) / 法身(57.1) / 法界(55.0) / 遮那(44.6) |
| dainichikyo-sho-vol1 | 真言(68.6) / 金剛(63.2) / 如来(53.4) / 法身(57.6) / 大悲(56.0) |
| sankyo-shiki | 真言(54.4) / 仏法(34.0) / 法身(44.0) / 仏陀(22.3) / 甘露(14.0) |

**「真言」が全 8 著作で最高位**：freq score + 全字 KAIMYO_ICHIJI 適合（真・言の 2 字一致）+ aesthetic ペアの組合せで安定的に高得点。kaimyo-app 戒名選定の中核候補として汎用性が高い。

### 16.4 dainichikyo-sho-vol1 の seed_sanskrit が 29 件で突出

大日経疏巻第一は sanskrit カテゴリで 1,409 canonical を持つため、SANSKRIT_TO_KAIMYO_JUKUGO（51 エントリ）の網にかかる canonical が 29 件もマッチした。具体的には：

- prajñā → 般若・智慧
- karuṇā → 大悲・慈悲
- bodhi / bodhicitta → 菩提
- śūnya / śūnyatā → 空観
- samādhi → 三昧
- dharma / dharmakāya → 法身・正法
- mantra → 真言（既に seed_terms 重複・除外）
- vajra → 金剛
- vairocana / mahāvairocana → 遮那・大日（既に seed_terms 重複・除外）
- tathāgata → 如来
- sattva → 薩埵
- buddha → 仏陀
- saṃgha → 僧伽
- bodhisattva → 菩薩
- dhyāna → 禅定
- nirvāṇa → 涅槃
- 等

これにより大日経疏は梵語起点・補注起点の双方が活発で、kaimyo_jukugo の総数が他著作を圧倒（70 unique vs 平均 22）。

### 16.5 改修前後の比較（occurrences）

| カテゴリ | 改修前（性霊集のみ）| dict 8 著作追加 | 9 著作合計 | 倍率 |
|---|---:|---:|---:|---:|
| kaimyo_jukugo | 1,971 | +2,424 | 4,395 | **2.23x** |

dainichikyo-sho-vol1 の 1,088 件 + 性霊集 1,971 件で全体の 70% を占める。残り 7 dict 著作は計 1,336 件で各種仏教教学用語が均等に分布。

### 16.6 横断検索の現状（2026-05-04 G2-C 完了時点）

`_corpus_manifest.json` の `summary.indexed_corpora`：

```
indexed_corpora:
  terms:         9 / 10 primary_corpus（菩提心論除く）
  citations:     9 / 10
  kukai_works:   9 / 10
  sanskrit:      9 / 10
  kaimyo_jukugo: 9 / 10  ← G2-C で 1 → 9 に拡大
  persons:       1 / 10
  places:        1 / 10
```

**Tier 1 + sanskrit + kaimyo_jukugo 全 9 著作完成（5 カテゴリ）。** Tier 3（persons / places）のみ性霊集限定。

### 16.7 review 要件 100 件の扱い

`needs_human_review=true` の 100 件は、すべて **paren_doctrinal 由来かつ kaimyo_score < 35** の語。kaimyo-app 連携時の運用方針：

- **第 1 段階**：seed_terms（88 件）+ seed_sanskrit（37 件）= 125 件を確実な戒名候補辞書として運用（needs_review=false）
- **第 2 段階**：paren_doctrinal の中で kaimyo_score ≥ 35 の語（109 - 100 = 9 件）を補強候補として運用
- **第 3 段階**：needs_review=true の 100 件は専門家校閲後に段階的採用

### 16.8 残作業（G2 後続）

| サブステップ | 内容 | 工数 |
|---|---|---|
| ✅ G2-A | dict 型 8 著作の Tier 1（terms + citations + kukai_works）| 1 セッション（2026-05-03）|
| ✅ G2-B | dict 型 8 著作の Tier 2-4 sanskrit | 1 セッション（2026-05-04）|
| ✅ G2-C | dict 型 8 著作の Tier 2-3 kaimyo_jukugo | 1 セッション（本セッション）|
| ⏭️ G2-D | dict 型 8 著作の Tier 3-5/6 persons / places | 1〜2 セッション |
| ⏭️ G2-E | 横断集約ファイル（index_<category>_all.json）生成 | 0.5 セッション |
| ⏭️ G2-F | 菩提心論 gendaigoyaku 取込後の再索引化 | 0.5 セッション |
| ⏭️ G2-G | 既訳 4 著作の Cowork 高品質訳化（梵語注記濃密化）| 各 5〜10 セッション |

### 16.9 v1.7 完成度評価

- ✅ **dict 型 kaimyo_jukugo 索引化フロー確立**：3 起点合成（seed_terms / seed_sanskrit / paren_doctrinal）+ スコアリング + needs_review マーカー
- ✅ **8 著作 kaimyo 索引完成**：合計 234 unique / 2,424 occurrences（NULL バイト 0 件・JSON 整合 OK）
- ✅ **重要発見：「真言」の汎用性**：8 著作すべてで上位の戒名候補・kaimyo-app の中核候補として運用可能
- ✅ **manifest 統合**：`summary.indexed_corpora.kaimyo_jukugo` を 1 → 9 に更新
- ✅ **5 カテゴリで 9 著作カバレッジ達成**：terms / citations / kukai_works / sanskrit / kaimyo_jukugo
- ⏭️ 次セッション（G2-D 以降）：persons / places の dict 型版抽出

---

## 17. G2-D dict 型 8 著作 Tier 3-5/3-6 persons・places 索引化（v1.8・2026-05-04）

G2-A・B・C に続く第 4 弾（最終）。性霊集に続いて dict 型 8 著作の人名・地名を索引化し、横断検索の対象を persons / places でも 1 → 9 著作に拡張。**これにより全 7 カテゴリで 9 著作カバレッジ達成**。

### 17.1 新設ファイル（4 種）

#### 共有 seed モジュール（git 追跡対象・新設）

- `_dev_references/seed_data_persons.py`（95 entries・9 subcategories）
- `_dev_references/seed_data_places.py`（91 entries・複数 subcategories）

dict 版と既存 _tmp_ 版が共通で利用可能な seed dictionary。「データの単一情報源」原則に基づき重複定義を回避。

#### 抽出スクリプト（git 追跡対象・新設）

- `_dev_references/extract_persons_dict.py`（dict 型 人名抽出・seed_data_persons から import）
- `_dev_references/extract_places_dict.py`（dict 型 地名抽出・seed_data_places から import）

`_tmp_extract_persons.py` / `_tmp_extract_places.py`（性霊集・list 型）の dict 型版。長表記優先・1 文字人名/王朝名の前後境界条件・dynasty context 判定は完全互換。

### 17.2 G2-D の生成結果（2026-05-04）

#### Persons（人名）

| 著作 | unique | occurrences | 上位 3 |
|---|---|---|---|
| nikyo-ron（弁顕密二教論）| 20 | 238 | 空海=80 / 大日如来=76 / 釈迦=21 |
| ujiji（吽字義）| 11 | 88 | 大日如来=74 / 帝釈天=3 / 不空=2 |
| shoji-jisso（声字実相義）| 7 | 82 | 大日如来=72 / 帝釈天=3 / 空海=3 |
| sokushin-jobutsu（即身成仏義）| 11 | 196 | 大日如来=157 / 空海=23 / 不空=5 |
| hannya-hiken（般若心経秘鍵）| 14 | 88 | 大日如来=23 / 空海=15 / 文殊=9 |
| hizo-houyaku（秘蔵宝鑰）| 38 | 209 | 大日如来=78 / 釈迦=26 / 普賢=12 |
| dainichikyo-sho-vol1（大日経疏巻第一）| 26 | 233 | 大日如来=74 / 弥勒=22 / 普賢=14 |
| sankyo-shiki（三教指帰）| 30 | 82 | 孔子=14 / 釈迦=9 / 老子=6 |
| **8 著作合計** | **157** | **1,216** | — |

#### Places（地名）

| 著作 | unique | occurrences | 上位 3 |
|---|---|---|---|
| nikyo-ron（弁顕密二教論）| 4 | 4 | 周 / 無色界 / 色界 |
| ujiji（吽字義）| 4 | 8 | 欲界=2 / 無色界=2 / 色界=2 |
| shoji-jisso（声字実相義）| 3 | 3 | 欲界 / 無色界 / 色界 |
| sokushin-jobutsu（即身成仏義）| 5 | 12 | 色界=4 / 欲界=3 / 安楽=2 |
| hannya-hiken（般若心経秘鍵）| 1 | 1 | 安楽=1 |
| hizo-houyaku（秘蔵宝鑰）| 22 | 60 | 安楽=8 / 色界=6 / 欲界=5 |
| dainichikyo-sho-vol1（大日経疏巻第一）| 9 | 25 | 色界=5 / 欲界=4 / 無色界=4 |
| sankyo-shiki（三教指帰）| 21 | 50 | 漢=9 / 周=6 / 夏=6 |
| **8 著作合計** | **69** | **163** | — |

### 17.3 重要発見：三教指帰の儒道仏比較作の特性が顕在化

三教指帰（24 歳作・儒道仏の対話劇）の persons / places 抽出結果が、その文芸的性格を完全に反映：

**Persons 上位（孔子=14・釈迦=9・老子=6・荘子=6）**：儒（孔子）・道（老子・荘子）・仏（釈迦）の三教代表者がバランスよく登場。

**Places 上位（漢=9・周=6・夏=6・楚=6・殷=5）**：中国王朝・国名が頻出。儒道仏比較を中国の歴史的舞台で展開する作品の性格と整合。

これは sankyo-shiki が他著作（sanskrit=0・kaimyo_jukugo=7 のみ）と異なる文芸的特性を持つことの裏付けでもあり、データベースの「文献特性の自己証明」として機能している。

### 17.4 重要発見：大日如来の中心性

8 著作中 6 著作で「大日如来」（aliases に大日・毘盧遮那・盧遮那・vairocana・mahāvairocana を含む）が最頻出人名：

- nikyo-ron: 76 / sokushin-jobutsu: 157 / shoji-jisso: 72 / hizo-houyaku: 78 / dainichikyo-sho-vol1: 74 / hannya-hiken: 23

「大日如来」は terms の「大日」「遮那」と alias 連携しているため、persons 索引の出現は terms とは独立にカウントされる。両方を統合して見ると密教の本尊としての中心性が圧倒的。

### 17.5 改修前後の比較（occurrences）

| カテゴリ | 改修前（性霊集のみ）| dict 8 著作追加 | 9 著作合計 | 倍率 |
|---|---:|---:|---:|---:|
| persons | 1,197 | +1,216 | 2,413 | **2.02x** |
| places | 466 | +163 | 629 | **1.35x** |

places の倍率が低い（1.35x）のは、dict 型 8 著作が概ね教義論述（諸子百家比較や宇宙論で地名が出る程度）で、地名の頻出する物語性が薄いため。最頻出の三教指帰（50 件）と秘蔵宝鑰（60 件）以外は数件レベル。

### 17.6 横断検索の現状（G2-D 完了時点）

`_corpus_manifest.json` の `summary.indexed_corpora`：

```
indexed_corpora:
  terms:         9 / 10 primary_corpus（菩提心論除く）
  citations:     9 / 10
  kukai_works:   9 / 10
  sanskrit:      9 / 10
  kaimyo_jukugo: 9 / 10
  persons:       9 / 10  ← G2-D で 1 → 9 に拡大
  places:        9 / 10  ← G2-D で 1 → 9 に拡大
```

🎯 **全 7 カテゴリで 9 著作カバレッジ完全達成**。残りは菩提心論（gendaigoyaku 提供待ち）の 1 著作のみ。

### 17.7 G2 全体の累積成果（2026-05-03〜2026-05-04）

| サブステップ | カテゴリ | 8 著作合計 occ | 9 著作合計 occ | 倍率 |
|---|---|---:|---:|---:|
| ✅ G2-A | terms | 1,678 | 2,222 | 4.08x |
| ✅ G2-A | citations | 648 | 1,829 | 1.55x |
| ✅ G2-A | kukai_works | 47 | 52 | 10.40x |
| ✅ G2-B | sanskrit | 2,017 | 2,671 | 4.08x |
| ✅ G2-C | kaimyo_jukugo | 2,424 | 4,395 | 2.23x |
| ✅ G2-D | persons | 1,216 | 2,413 | 2.02x |
| ✅ G2-D | places | 163 | 629 | 1.35x |
| **G2 合計** | — | **8,193** | **14,211** | **2.36x** |

横断索引化で実用 occurrence データが **改修前 6,018 → 改修後 14,211（2.36 倍）** に拡大。kaimyo-app の戒名選定・法話生成・典拠検索 API の素材として 9 著作横断で運用可能になった。

### 17.8 残作業（G2 完了後の派生候補）

| サブステップ | 内容 | 工数 |
|---|---|---|
| ✅ G2-A〜D | dict 型 8 著作の Tier 1+2-3+2-4+3-5+3-6 全て完了 | 4 セッション（2026-05-03〜2026-05-04）|
| ⏭️ G2-E | 横断集約ファイル（index_<category>_all.json）生成 | 0.5 セッション |
| ⏭️ G2-F | 菩提心論 gendaigoyaku 取込後の再索引化 | 0.5 セッション（並行候補 A 完了後）|
| ⏭️ G2-G | 既訳 4 著作の Cowork 高品質訳化（梵語注記濃密化）| 各 5〜10 セッション |
| ⏭️ G3 | 未着手 8 著作（御遺告・秘蔵講義「他界」・十住心論・日本真言哲学・理趣経・三昧耶戒・御請来目録・菩提心論）のロードマップ | 設計 1 セッション |
| ⏭️ G4 | L2 字索引の新設 | 2〜3 セッション |
| ⏭️ G5 | L3 by_* 汎用 endpoint の整備 | 3〜4 セッション |
| ⏭️ G6 | kaimyo-app 暫定ハードコード 3 種の置き換え API（候補 D §13 v1.4 仕様確定済）| 5〜6 セッション |

### 17.9 v1.8 完成度評価

- ✅ **dict 型 persons / places 索引化フロー確立**：seed dictionary を共有モジュール化・長表記優先 + 1 文字境界条件 + dynasty context 判定で誤検知抑止
- ✅ **8 著作 persons / places 索引完成**：合計 226 unique / 1,379 occurrences（NULL バイト 0 件・JSON 整合 OK）
- ✅ **重要発見：三教指帰の文芸的特性の自己証明**：persons（孔子・老子・荘子・釈迦）+ places（漢・周・夏・楚・殷）が儒道仏比較作の性格を完全反映
- ✅ **重要発見：大日如来の中心性**：8 著作中 6 著作で最頻出人名・密教の本尊としての地位を実データで証明
- ✅ **manifest 統合**：persons / places を 1 → 9 に更新・index_definitions.g2_status を「G2-A〜D 完了」に変更
- 🎯 **全 7 カテゴリで 9 著作カバレッジ達成**（terms / citations / kukai_works / sanskrit / kaimyo_jukugo / persons / places）
- 🎯 **G2 全体の累積：occurrences 6,018 → 14,211（2.36 倍）に拡大**・kaimyo-app 連携 API 実装の素材完備

### 17.10 設計方針メモとの対応（最終）

```
G1 ✅ L1 スキーマ統一（commit c1e9494・2026-05-03）
G2 ✅ L1 横断索引化（4 セッション完結）
    G2-A ✅ Tier 1（terms + citations + kukai_works）8 著作（commit d684523）
    G2-B ✅ Tier 2-4 sanskrit 8 著作（commit 2900292）
    G2-C ✅ Tier 2-3 kaimyo_jukugo 8 著作（commit c155aac）
    G2-D ✅ Tier 3-5/3-6 persons/places 8 著作（本コミット予定）
    G2-E〜G ⏭️ 集約・既訳改善・菩提心論再索引化（任意）
G3 ⏭️ 未着手 8 著作のロードマップ
G4 ⏭️ L2 字索引の新設
G5 ⏭️ L3 by_* 汎用 endpoint の整備
G6 ⏭️ kaimyo-app 暫定ハードコード 3 種の置き換え API（v1.4 仕様確定済 §13）
```

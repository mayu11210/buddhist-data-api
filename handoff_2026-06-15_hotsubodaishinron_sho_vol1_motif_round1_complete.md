# 引き継ぎメモ 2026-06-15 発菩提心論鈔 第一巻（宥快）motif 抽出 第1ラウンド（序説）完了

**日付**：2026-06-15
**種別**：kakikudashi-data Phase3 第1ラウンド（motif 抽出・序説 当論総論）
**起点 HEAD**：`4f16614`（発菩提心論鈔 Phase2 横断索引化）
**ステータス**：R1 完了・整合性検証＋巻き戻り assert＋verbatim 照合 全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json・CLAUDE.md・commit_message.txt・本メモ。corpus・manifest・索引は不変。

## Phase A 合意（全ラウンド遵守）
- 著者=宥快（非空海・確定・高野山学僧 1345-1416）→ 引用形式:典籍曰く 全件・大師系タグ非付与・source に 著者:宥快 保持。
- 目次 k001-k050（科段目次）・書名著者行 k051 は motif 化せず。論義見出し（「一、◯◯の事」）・牒文（短小）は直後の注釈本文に束ね。
- gabun 意図的未設定（経典注釈系・補注 II/MM 基準・将来 retrofit 可）。連動軸は完走後 retrofit。
- タグ語彙は既存再利用優先。新タグ値は判定表で明示。

## 成果（R1・m2466-m2471・6件）
| id | 束ね段 | 内容 | category | 核心 |
|---|---|---|---|---|
| m2466 | k052+k053 | 真言宗の当論依学（密蔵肝心・三学阿毘達磨蔵・官符） | 議論 | |
| m2467 | k054+k055 | 密蔵肝心の三義（顕密二教差別・菩提心諸法本源・勝義行願三摩地三門） | 核心句 | ★ |
| m2468 | k056+k057 | 製作時代と伝来（龍樹滅後八百年・不空翻訳・本朝請来） | 歴史記述 | |
| m2469 | k058+k059 | 両部分別（両部所依説と金剛頂部限定説） | 議論 | |
| m2470 | k060+k061 | 集義釈経の弁（集義論と釈経論の区別） | 定義 | |
| m2471 | k062+k063 | 不空所造かの弁（龍樹造の擁護・智証の不空集説批判） | 議論 | |

- 束ね6件（論義見出し/牒文を後続本文に verbatim 結合）。新タグ値 典故:付法伝・出典:発菩提心論鈔 のみ。
- タグ軸の注意：人名・地名は motif タグ軸に存在しない（索引のみ）。龍樹・不空・智証・青龍寺等は本文内容として保持し、persons/places 索引（Phase2）でカバー。

## stats 差分
- total_motifs 2496→2502（+6）・kakikudashi_chars_total +3,857・gendaigoyaku_chars_total +5,602。
- from_corpus_hotsubodaishinron-sho-vol1=6（新規キー）・篇別内訳に hotsubodaishinron-sho-vol1_序説（当論総論）追加・without_gabun_intentional に hotsubodaishinron-sho-vol1_m2466-m2471 追加。
- schema_history +1（origin: hotsubodaishinron-sho-vol1_round1）・schema 0.2 維持。

## 検証（全 pass）
- 整合性 10 項目（NUL0／再パース／total==配列／m-id 連番 missing=[] dup=False 最大 m2471／必須フィールド／半角括弧0／kk・gd recompute／schema 0.2）。
- 巻き戻り assert：m506 引用形式:典籍曰く／retrofit35 連動:sg31（m2464）温存。
- verbatim 照合：6 motif の kk・gd が corpus 段落の \n 結合と一致。
- build script：outputs/build_hotsubodai_r1.py（dry-run→--apply・allowed-new guard）。バックアップ：outputs/motifs_backup_pre_hotsubodai_r1.json。

## 残ラウンド
- R2 題号釈① 金剛頂瑜伽中 k064-k095（32段）
- R3 題号釈② 発阿耨多羅三藐三菩提心 k096-k121（26段）
- R4 副題釈 k122-k135＋造者釈 k136-k161（40段）
- R5 訳者釈 k162-k171＋結 k172
※段数が多い区分は適宜分割。完走後：連動軸 retrofit（顕密二教 sg18／三種菩提心 sg22 候補）・gabun 要否裁定・kaimyo-app 同期。

## 留意（git）
- 前 Phase2 push 後に .git/index 破損（末尾ゼロ SHA）あり。**commit_push.bat 前に fix_index.bat を流すこと**（履歴には無害）。

## 次セッション確認
1. CLAUDE.md 冒頭 → 本メモ → git log --oneline -3
2. motifs.json：total 2502・最終 m-id m2471・schema 0.2・from_corpus_hotsubodaishinron-sho-vol1=6
3. references/motif-extraction.md 必読・Phase A 合意は本メモ参照

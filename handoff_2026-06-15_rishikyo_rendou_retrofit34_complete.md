# 引き継ぎメモ 2026-06-15 理趣経 連動軸 retrofit 34 完走（Phase A→D 完了）

**日付**：2026-06-15
**種別**：連動軸 retrofit（retrofit 6/32 型＝新規 sg 新設＋既存軸被覆拡張）・Phase A→D 様式
**起点 HEAD**：`e420e0a`（理趣経 motif R1 完走・push 済を着手前に確認）
**ステータス**：Phase A→D 完了・整合性検証 10 項目＋巻き戻り/核心 assert 全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**commit_message.txt 更新確認**：✅ retrofit 34 用に書き換え済（冒頭行＝「理趣経 連動軸 retrofit 34 完走…」・作業内容と整合）
**変更ファイル**：data/indices/motifs.json（sg30/sg31 新設・連動タグ +12・stats 同期）・_dev_references/motifs_index_design.md（補注 JJ）・CLAUDE.md（タイトル行・現在の進捗に retrofit 34 ★）・commit_message.txt・本メモ。既存 motif の本文・他 corpus・索引は不変。

---

## Phase A 合意（ケンシン裁定・2026-06-15）

1. 新設 sg：**2 件**（十七清浄句・大欲/大楽）。如来蔵・煩悩即菩提は新規 sg 化せず既存主題タグ（主題:煩悩即菩提・密教:如来蔵）据置。
   - 根拠：4 候補テーマは倉庫内分布が理趣経内に閉じる（煩悩即菩提 4・如来蔵 1・大欲 1・十七清浄句 1・大楽 2）。新設は retrofit 32（sg28/sg29＝連動先 anchor 自身のみでも新設）が先例で正当化。十七清浄句・大欲は理趣経固有の署名教説ゆえ新設、如来蔵・煩悩即菩提は本来性/平等の射程ゆえ据置。
2. 既存軸連動：**sg03 即身成仏のみ**。本来性系（200 件）への連動は希薄化回避のため今回見送り。

## Phase B 判定（推奨表どおり・ケンシン裁定）

**新設成句 2 件**（sg29 直後挿入・sg ブロック一体保持）：

| id | text_kakikudashi | 出典 | anchor |
|---|---|---|---|
| sg30 | 十七清浄句 | 理趣経 序分・大楽不空三摩耶段（金剛薩埵章） | m2400 |
| sg31 | 大欲得清浄、大安楽富饒 | 理趣経 究竟段・深秘百字偈段 | m2413 |

いずれも 成句:famous・一句性:核心・含意:全人生・引用形式:典籍曰く（不空訳＝非空海・sg28/sg29 同運用）・gabun 意図的未設定。source.type=成句・出典_ref=理趣経。

**連動タグ +12（5 motif）**：

| motif | 節 | 付与 |
|---|---|---|
| m2400 | 序分・大楽不空三摩耶段（十七清浄句） | 連動:sg30・連動:m2400（自己）＋連動:sg31・連動:m2413（二軸・初例） |
| m2403 | 観自在・蓮華清浄段 | 連動:sg30・連動:m2400 |
| m2413 | 究竟段・深秘百字偈段 | 連動:sg31・連動:m2413（自己） |
| m2405 | 一切如来智印加持段 | 連動:sg03・連動:m533 |
| m2411 | 一切有情加持段（如来蔵） | 連動:sg03・連動:m533 |

**除外**（経証・真言・儀礼中心）：m2401・m2402・m2404・m2406・m2407・m2408・m2409・m2410・m2412・m2414。

## stats 差分（補注 EE/FF 継承・R1 stale 是正）

- total_motifs 2443→**2445**・famous_phrases 29→**31**
- kakikudashi_chars_total +16（sg30 KK 5＋sg31 KK 11）・gendaigoyaku_chars_total +817（sg30 GD 448＋sg31 GD 369）・gendai_gabun_chars_total **不変**（238704）
- 篇別内訳 `成句_二十九件`→`成句_三十一件`（sg30/sg31 追加・件数 31）
- motifs_without_gendai_gabun_intentional キー `sg01-sg29`→`sg01-sg31`
- top-level description 現況化（2445 motifs＝m1〜m2414＋成句 sg01〜sg31・理趣経 15 著作目完走・連動軸 **二十五→二十七系統**並立）
- schema_history（top-level）+1（origin: `retrofit_34:rishikyo_rendou_scan`・len 163→164）。**stats.schema_history は 14 件で不変**（retrofit は top-level のみ追記）。schema 0.2 維持。

## 検証（全 pass）

整合性 10 項目：total=配列 2445／m-id 連番 m1-m2414（欠落・重複なし）／NUL 0／JSON 再パース OK／schema 0.2／必須フィールド完全／連動タグ付与確認／famous 31／stats recompute 全ゼロ（kk/gd/gabun）／新規成句 半角括弧 0。追加：連動:sg 系統数 27（sg30/sg31 in use 確認）・篇別内訳 成句_三十一件・without_gabun sg01-sg31・補注 JJ present・design doc 半角括弧 0。
巻き戻り assert：m506 引用形式:典籍曰く 保持。核心 assert：sg30・sg31・m2400・m2411・m2413。
実装：outputs/retrofit34_rishikyo_rendou.py（dry-run→--apply）。バックアップ：outputs/motifs_backup_pre_retrofit34.json（未追跡・スクラッチ・次回消失）。

## 補注 JJ

`_dev_references/motifs_index_design.md` 末尾に 補注 JJ「理趣経 連動軸 retrofit と十七清浄句・大欲/大楽 成句 anchor 新設の運用」を追加（補注 II の次・letter 連番 JJ）。

## 残課題（次セッション以降・handoff 記録）

1. **gabun 要否裁定**（理趣経 motif の雅文体訳・現状 意図的未設定）。補注 II（理趣経開題 gabun 裁定）のジャンル基準＝「文藝系＝gabun／教学注釈系＝未設定」に照らすと、経典本文は教学注釈系の文体圏で未設定継続が見込み。GG/II 様式で独立裁定。
2. **kaimyo-app への motifs.json 同期**（倉庫 2445→kaimyo-app・SHA-256 一致確認・橋プール更新・理趣経 motif がプール入りする場合 CORPUS_DISPLAY_NAME に rishikyo: '理趣経' 追加を要検討）。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs 2445・famous_phrases 31・m-id 最終 m2414・sg 最終 sg31・連動:sg 系統数 27
3. m506 引用形式:典籍曰く（巻き戻り検知・不変のはず）
4. 理趣経（rishikyo）：Phase1 取込（0c5df0f）・Phase2 横断索引化（a0bba39）・Phase3 motif R1（e420e0a）・retrofit 34 連動軸（本コミット）。残＝gabun 要否裁定／kaimyo-app 同期。

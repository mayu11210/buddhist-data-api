# 引き継ぎメモ 2026-06-15 理趣釈（rishushaku.json）motif 抽出 第1ラウンド（巻上）完走

**日付**：2026-06-15
**種別**：motif 抽出（kakikudashi-data Phase3・第1ラウンド／全3ラウンド中）
**起点 HEAD**：`61d5139`（理趣釈 Phase2 横断索引化・push 済を着手前に確認）
**ステータス**：第1ラウンド完了・整合性検証 10 項目全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json・CLAUDE.md・commit_message.txt・本メモ。corpus・manifest・索引は不変。

---

## Phase A 合意（全ラウンド遵守・2026-06-15 ケンシン裁定）
- 書込方式：本体直接書込（並行書き手なし）。ID は最終 m-id の次から連番・配列末尾追記。
- 引用形式：伝・不空訳＝**非空海** → 全件 `引用形式:典籍曰く`、大師系タグ非付与。source に著者「伝・不空訳」保持。
- 首尾題・訳者行（k001/k002/k022/k023/k024/k057）は motif 化せず。語中切れ段・短小真言句は直前に束ね。
- gabun（雅文体訳）：意図的未設定（理趣経本体・開題・yugikyo と同運用・将来 retrofit 可）。
- 連動軸：完走後 retrofit。
- タグ語彙：理趣経本体（rishikyo m2400-m2414）・開題（rishukyo-kaidai m2384-m2399）の値を再利用優先。
- ラウンド分割（3 ラウンド）：**R1 巻上 k003-k021**／R2 巻下前半 k025-k043／R3 巻下後半 k044-k056。

## 成果（第1ラウンド・m2415-m2433・19件）

| id | 段 | 節 | 核心 |
|---|---|---|---|
| m2415 | k003 | 序分・通序の字釈（如是・我聞・婆伽梵・五仏・金剛加持・三昧耶智） | |
| m2416 | k004 | 序分・潅頂宝冠・一切智智・平等事業 | |
| m2417 | k005 | 序分・常恒三世・金剛大毘盧遮那 | |
| m2418 | k006 | 序分・説処＝他化自在天宮・大曼荼羅 | |
| m2419 | k007 | 序分・八大菩薩の眷属（菩提心・大悲・方便の三句） | |
| m2420 | k008 | 序分・説法の六徳（初中後善・純一円満清浄潔白） | |
| m2421 | k009 | 初段・妙適＝蘇囉多・無縁大悲・自他平等無二 | ★ |
| m2422 | k010 | 初段・欲箭〜味の十六清浄句（列挙） | |
| m2423 | k011 | 初段・一切法自性清浄・四種智印 | ★ |
| m2424 | k012 | 初段・聞持の功徳・十六大菩薩生 | |
| m2425 | k013 | 初段・大乗七義・現証・三昧耶・四種曼荼羅 | |
| m2426 | k014 | 初段・金剛薩埵の大智印（金剛慢印・本初大金剛） | |
| m2427 | k015 | 初段・吽字の四字義・菩提心為因・阿字本不生 | ★ |
| m2428 | k016 | 初段・十七字の種子と四種曼荼羅 | |
| m2429 | k017 | 初段・曼荼羅の安立次第と修行儀軌（初集会品） | |
| m2430 | k018 | 第二段・四種現等覚①金剛平等＝大円鏡智 | |
| m2431 | k019 | 第二段・四種現等覚②平等性・妙観察・成所作 | |
| m2432 | k020 | 第二段・聞持の功徳・アク字の四字義・四種涅槃 | |
| m2433 | k021 | 第二段・四大転輪王菩薩の曼荼羅と念誦 | |

- 束ねなし（全段 >100 字・語中切れなし）。新タグ値は **出典:理趣釈 のみ**（他は既存語彙再利用）。
- 一句性:核心 3 件（m2421／m2423／m2427）。

## stats 差分
- total_motifs 2445→**2464**（+19）
- kakikudashi_chars_total +9,366（改行除き）／gendaigoyaku_chars_total +12,452
- from_corpus_rishushaku=**19**（新規）
- 篇別内訳に `rishushaku_序分〜第二段（巻上）` 追加（節範囲・抽出_motif_数 19・id_範囲 m2415-m2433・属性 経典注釈〔伝・不空訳〕）
- motifs_without_gendai_gabun_intentional に `rishushaku_m2415-m2433` 追加
- schema_history +1（origin: rishushaku_round1）・schema_version 0.2 維持

## 検証（10 項目・全 pass）
NUL0／JSON 再パース／total==配列数 2464／m-id 連番 missing=[] dup=False（sg 31 不変）／必須フィールド完全／新規 半角括弧 0／recompute drift kk0・gd0／schema 0.2・history 165／原文 verbatim 一致／ホスト Grep 反映（m2433・rishushaku_round1）。＋ m506 引用形式:典籍曰く 巻き戻り assert pass。
- build script：outputs/build_rishushaku_r1.py（dry-run→--apply）。バックアップ：outputs/motifs_backup_pre_rishushaku_r1.json。

## 残作業（次セッション以降）
1. **R2 巻下前半 k025-k043**（第三段〜第九段・~19段）：同 Phase A 合意で判定表→build。
   - 留意：曼荼羅配置の継続による語中切れ束ね候補（例 k031→k032）・各段の字義釈（紇利字 k030・怛覽字 k033・アク字系）。
2. **R3 巻下後半 k044-k056**（第十段〜流通分・~13段）。k057 巻下尾題は motif 化せず。第十七段 五秘密（k054-k055）に「大欲得清浄・大安楽富饒」百字偈の配釈＝理趣経 sg31 連動候補。
3. 完走後：連動軸 retrofit（十七清浄句 sg30・大欲 sg31・即身成仏 sg03・阿字本不生 sg08 等との連動付与）／gabun 要否裁定／kaimyo-app への motifs.json 同期。

## 次セッション開始時の確認
1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本ラウンドコミット）
2. motifs.json：total_motifs 2464・最終 m-id m2433・schema 0.2
3. references/motif-extraction.md 必読（並行書き手・巻き戻り assert）

# 引き継ぎメモ 2026-06-15 理趣経 motif 抽出 第1ラウンド完走（Phase 3・完走）

**日付**：2026-06-15
**種別**：motif 抽出（kakikudashi-data スキル Phase 3・本体直接書込・rishikyo_round1）
**起点 HEAD**：`a0bba39`（理趣経 Phase2 横断索引化・push 済を着手前に確認）
**ステータス**：第1ラウンドで**完走**・整合性検証 10 項目＋巻き戻り assert 全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json（m2400-m2414 追記＋stats）・CLAUDE.md（タイトル行・現在の進捗に R1 ★）・commit_message.txt・本メモ。既存 motif・他 corpus・索引は不変。

---

## Phase A 合意（ケンシン裁定・2026-06-15・本ラウンド冒頭で確定）

1. 書込方式：本体直接書込（並行なし）・ID m2400 から連番・配列末尾追記。
2. 著者帰属／引用形式：不空訳＝非空海ゆえ **引用形式:典籍曰く** を全件付与・category:大師御言葉／引用形式:大師曰く は非付与（yugikyo 伝・金剛智訳と同運用）。source の 著者キーは「不空訳」。
3. 首題 k001・訳者 k002 は motif 化せず。
4. 天部心真言 k015-k017（七母女天／末度迦羅天／四姉妹女天）を **1 motif に束ね**（短小真言句・同一節・一連の供養場面）。
5. gabun（雅文体訳）は意図的未設定（hizoki/jujushinron/yugikyo 同運用・将来 retrofit 可）。
6. 連動軸タグは抽出時非付与・完走後 retrofit。
7. ラウンド割：19 段落・実質 15 motif を **1 ラウンドで完走**。

## 成果（m2400-m2414・15 motif）

| id | 段落 | 節 | 核心 |
|---|---|---|---|
| m2400 | k003 | 序分・大楽不空三摩耶段（十七清浄句） | ★核心 |
| m2401 | k004 | 毘盧遮那・四種現等覚 | |
| m2402 | k005 | 釈迦牟尼・降三世 | |
| m2403 | k006 | 観自在・蓮華清浄 | |
| m2404 | k007 | 虚空蔵・灌頂 | |
| m2405 | k008 | 一切如来智印加持 | |
| m2406 | k009 | 文殊・字輪 | |
| m2407 | k010 | 纔発心転法輪・入大輪 | |
| m2408 | k011 | 虚空庫・供養 | |
| m2409 | k012 | 摧一切魔・調伏 | |
| m2410 | k013 | 一切平等建立 | |
| m2411 | k014 | 一切有情加持・如来蔵 | ★核心 |
| m2412 | k015-k017 束ね | 外金剛部・天部心真言 | |
| m2413 | k018 | 究竟段・深秘百字偈 | ★核心 |
| m2414 | k019 | 流通分・集会讃嘆 | |

- 新タグ値 6（既存軸内追加）：出典:理趣経・密教:十七清浄句・密教:大楽・密教:如来蔵・主題:煩悩即菩提・主題:大欲。
- 引用形式:典籍曰く 全 15 件。一句性:核心 3 件（m2400/m2411/m2413）。
- 既存値再利用：密教（遮那/観音/灌頂/加持/三密/文殊/金剛薬叉/普賢/真言/理趣経）・主題（本来性/平等/菩提/菩提心/衆生救済/即身成仏/三解脱門/供養/奉献/讃辞/仏法）・文体（対句/長句/列挙/譬喩/散文/偈/讃辞/畳語）・category（密教教学/供養/献納物/讃辞）。

## stats 差分

- total_motifs 2428→2443（+15）
- kakikudashi_chars_total +5,357（改行除き・corpus 5,394 から首題 k001/訳者 k002 の 37 字を除いた値と一致）
- gendaigoyaku_chars_total +8,191
- from_corpus_rishikyo=15（新規）
- 篇別内訳に `rishikyo_序分十七清浄句〜流通分`（dict）追加
- motifs_without_gendai_gabun_intentional に `rishikyo_m2400-m2414` 追加
- gendai_gabun 系 stats 不変（gabun 未設定）
- schema_history +1（origin: rishikyo_round1・14 件）

## 検証（全 pass）

整合性 10 項目：NUL 0／JSON 再パース OK／total=配列 2443／m-id 連番 m1-m2414 欠落・重複なし／sg 29 不変／必須フィールド完全／新規 motif 半角括弧 0／stats=recompute 全ゼロ（kk/gd/from_corpus/gabun）／schema 0.2・schema_history 14／原文 verbatim 照合 OK。追加：ホスト Grep で m2414・total 2443・新タグ値反映確認。
巻き戻り assert：m506 引用形式:典籍曰く 保持（retrofit 温存検知）。
実装：outputs/build_rishikyo_r1.py（dry-run→--apply）。バックアップ：outputs/motifs_backup_pre_rishikyo_r1.json（未追跡・スクラッチ・次回消失）。

## 残課題（次セッション以降・handoff 記録）

1. **連動軸 retrofit**（完走後・Phase A→D 様式）：中心成句 sg 新設候補＝十七清浄句（m2400）・煩悩即菩提・大欲（m2413）・如来蔵（m2411）。既存軸との連動も検討（即身成仏 sg03・本来性系・大日経三句 sg07 等）。リポジトリ CLAUDE.md「retrofit セッション運用」節参照。
2. **gabun 要否裁定**（理趣経 motif の雅文体訳・現状 hizoki/yugikyo 同様 意図的未設定）。
3. **kaimyo-app への motifs.json 同期**（倉庫 2443→kaimyo-app・SHA-256 一致確認・橋プール更新・理趣経 motif がプール入りする場合 CORPUS_DISPLAY_NAME に rishikyo: '理趣経' 追加を要検討）。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs 2443・m-id 最終 m2414・from_corpus_rishikyo 15・schema_history 14
3. m506 引用形式:典籍曰く（巻き戻り検知・不変のはず）
4. 理趣経（rishikyo）3 フェーズ完了：Phase1 取込（0c5df0f）・Phase2 横断索引化（a0bba39）・Phase3 motif R1（本コミット）

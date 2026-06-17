# 引き継ぎメモ 2026-06-17 大日経疏 巻第二 motif 抽出 第1ラウンド完了（三十外道破 k002-k018）

**日付**：2026-06-17／**種別**：kakikudashi-data Phase3（motif 抽出）第1ラウンド
**起点 HEAD**：`d5f0605`（巻第二 Phase2 横断索引化）／**ステータス**：R1 完成・整合性検証全 pass・**未 commit / 未 push**

## Phase A 合意事項（巻第二・全ラウンド共通・厳守）
1. 書込方式：本体直接書込（並列なし）。ID は最終 m-id の次から連番・配列末尾追記。
2. 著者＝善無畏口述・一行筆受＝**非空海** → **引用形式:典籍曰く 全件付与・大師系タグ（category:大師御言葉／引用形式:大師曰く）非付与**。source.著者 に「善無畏口述・一行筆受」保持。
3. 短小段落の束ね：30字未満の真言句等は直前本文に束ね（R1 は該当なし）。
4. text_gendai_gabun（雅文体訳）は**意図的未設定**（経典注釈系・hizoki/理趣釈/発菩提心論鈔と同運用・後で retrofit 可）。
5. 連動軸タグは抽出時付与せず、**完走後に retrofit**。

## R1 成果（三十外道破 k002-k018 → m2526-m2542・17件）
- 品題 k001「入真言門住心品第一之余」は**首題ゆえ motif 化せず**。
- 共通タグ：category:密教教学／出典:大日経疏 巻第二〔新〕／引用形式:典籍曰く／主題:外道破〔新〕。
- 新タグ値 5：`出典:大日経疏 巻第二`・`主題:外道破`・`主題:神我`・`主題:阿頼耶`・`主題:声論`。
- 典故:大智度論 4件（k005 人量／k010 知者見者／k014 摩奴闍／k015 摩納婆）。文体:問答 4件（k002/k003/k004/k010）。
- 一句性:核心 2件：**m2535**（k011 能執所執・「執尚不可得」＝無自性）／**m2542**（k018 三十事総括・違理心→順理の世間八心へ転換）。
- 各 motif：尊貴(那羅延天)/自然/内我/人量(神我)/遍厳/補特伽羅(数取趣)/識/阿頼耶/知者見者/能執所執/内知外知/社怛梵/摩奴闍(人)/摩納婆(勝我)/常定生/声非声＋総括。
- stats：total 2556→2573・kk +4,314／gd +5,815・from_corpus_dainichikyo-sho-vol2=17・篇別内訳に dict エントリ追加・motifs_without_gendai_gabun_intentional に dainichikyo-sho-vol2_m2526-m2542 追記・schema_history（top-level）175→176・origin: dainichikyo-sho-vol2_round1。
- 整合性検証 10項目＋巻き戻り assert（m506 引用形式:典籍曰く 温存）全 pass：verbatim 0 mismatch・recompute drift 0・m-id 連番 m1-m2542・sg31 不変・NUL0・新規半角括弧0・schema_version 0.2。
- バックアップ：outputs/motifs_backup_pre_dainichikyo-sho-vol2_round1.json。build script：outputs/build_vol2_round1.py。

## 残ラウンド（outline 10 区分）
- R2：順理の世間八心 k019-k023（世間八心・殊勝心・決定心・嬰童心）
- R3〜：六十心 k024-k079（大きいので 2〜3 ラウンドに分割。各心は 1段1motif）
- 百六十心・三妄執 k080-k091／第一劫五喩・法無我 k092-k097／第二劫 自心本不生 k098-k099／第三劫 極無自性心 k100-k101／応供 宝珠喩 k102／信解行地 k103-k106。
- 着手前に references/motif-extraction.md を読む。

## 完走後の残課題
- 連動軸 retrofit（中心成句スキャン）／gabun 要否裁定／kaimyo-app への motifs.json 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`（HEAD が本 R1 コミット）。
2. motifs.json：total 2573・最終 m2542・schema 0.2。
3. R2（世間八心 k019-k023）から判定表を出して進める。

## 注意：phantom staged deletion（既知）
- render.yaml/start.bat/tsconfig.json/vercel.json/引き継ぎメモ_2026-05-06_*.md の staged deletion は全て disk 実在・HEAD あり＝既知 stale index（本作業由来でない）。commit_push.bat の index リセットで自動解消。SAFETY CHECK が deleted: で中止したら fix_index.bat 後に再実行。

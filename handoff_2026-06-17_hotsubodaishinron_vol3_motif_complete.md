# 引き継ぎメモ 2026-06-17 発菩提心論鈔 第三巻 Phase3 motif 抽出 全4ラウンド完走

**日付**：2026-06-17／**種別**：kakikudashi-data Phase3（motif 抽出）完走
**起点 HEAD**：発菩提心論鈔 第三巻 Phase2 横断索引化（`ee7fbfa`）／**ステータス**：完走・整合性検証全 pass・**未 commit / 未 push**

## Phase A 合意事項（第一巻と同じ・厳守）
著者＝宥快＝**非空海** → 引用形式:典籍曰く 全件・大師系タグ非付与・source.著者「宥快」保持・
text_gendai_gabun 意図的未設定・連動軸タグは完走後 retrofit・目次 k001-k023 は首題/目次ゆえ motif 化せず・見出し/牒文は直後の注釈本文に束ね。

## 成果（m2631-m2655・25件・total 2661→2686）
- **R1 菩提心の行相・行相の三門と三摩地 k024-k036**（m2631-m2637・7件）：結前生後／四種の心・菩提心は万行の根源〔m2632★核心〕／須知菩提心之行相の論義（瑜伽唯識・相分見分・入道章）／三門の惣表列名・三門分別・諸仏菩薩無時暫忘・三摩地為戒と昔在因地の六義。
- **R2 三種菩提心を戒とする義・三摩地の説黙 k037-k048**（m2638-m2643・6件）：発是心已／勝義行願三摩地為戒（三聚浄戒・三昧耶仏戒・サンマヤ三字）／乃至成仏無時暫忘／**三摩地の説黙＝即身成仏は真言法のみ・諸教に欠く・顕密分斉・他門会釈の反駁〔m2641★核心〕**／於諸教中／欠而不書。
- **R3 三門の列名と三種菩提心の分別 k049-k060**（m2644-m2649・6件）：三門の名字（大定智悲）〔m2644★核心〕／列次第／人法喩配釈（観音文殊金薩・三宝・三部）／三句配釈／訓釈／三摩地＝等念（平等護念・衆生即仏）。
- **R4 行願の牒釈・信の十義 k061-k070**（m2650-m2655・6件）：行願の牒釈（願と行・文殊普賢）／為修習之人（三密修習）／初行願者（得名・利益安楽の九義・世界海）／**観十方含識猶如己身＝同体の大悲・事理の同体〔m2653★核心〕**／事理同体の校合（一切衆生悉有仏性）／信の十義。
- 共通タグ：category:密教教学／出典:発菩提心論鈔／引用形式:典籍曰く。**新タグ値4**：主題:信・典故:即身成仏義・典故:弁顕密二教論・典故:起信論。一句性:核心 4件（m2632・m2641・m2644・m2653）。
- stats：kk +19,375／gd +27,258・from_corpus_hotsubodaishinron-sho-vol3=25・篇別内訳 4 dict 追加・motifs_without_gendai_gabun_intentional に hotsubodaishinron-sho-vol3_m2638-m2655・schema_history（top-level）184→188（R1-R4 各 origin）。
- 整合性検証 10項目＋巻き戻り assert（m506 典籍曰く／第一巻60件 温存）全 pass：verbatim 0・recompute drift 0・m-id 連番 m1-m2655・sg31 不変・NUL0・新規半角括弧0・段落 k024-k070 全網羅（目次 k001-k023 除外）。
- バックアップ：outputs/motifs_backup_pre_vol3_round1.json・..._round234.json。build script：outputs/build_vol3_round1.py・build_vol3_round234.py。

## 残課題（完走後・推奨ルート）
1. **連動軸 retrofit**（中心成句スキャン・既存軸被覆拡張）：vol3 は『菩提心論』の注釈ゆえ親子連動。候補＝sg22 三種菩提心〔anchor m506+m581〕／sg18 顕密二教〔m571〕／sg03 即身成仏〔m533〕／sg07 三句法門〔m713〕。第一巻 retrofit 36 と同型。直接連動（核心・術語 verbatim）に限定。
2. **gabun 要否裁定**：経典注釈系ゆえ意図的未設定の継続（第一巻と同運用）。
3. **kaimyo-app への motifs.json 同期**：total 2686 をコピー＋SHA-256 一致確認。新引用形式タグなし（典籍曰く・CORPUS_DISPLAY_NAME 既登録「発菩提心論鈔」）ゆえコード変更不要見込み。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. motifs.json：total 2686・最終 m2655・vol3 motif 25件（m2631-m2655）。
3. 連動軸 retrofit から着手（推奨ルート）。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。

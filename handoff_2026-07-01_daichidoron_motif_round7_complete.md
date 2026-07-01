# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第7ラウンド（三十七品義 摩訶衍・章末）完了＝三十七品義 全35段 完走

日付：2026-07-01
対象：data/indices/motifs.json（m4124-m4131 追加・total 4154→4162）
前提コミット（着手時 HEAD）：005c6c4（Round6 三十七品義 後半・声聞法 完了）

## Phase A 合意（ケンシン裁定・全ラウンド遵守／再掲）
- 本体直接書込・ID 連番末尾追記。著者＝伝・龍樹菩薩造・鳩摩羅什訳＝非空海 →引用形式:典籍曰く 全件・大師系タグ非付与。
- category:密教教学・出典:大智度論。text_kakikudashi＝漢文原典 genten・text_gendaigoyaku＝現代語訳（corpus verbatim）。
- 節＝section_major（"大智度論 " 除去）（section）。引用元＝各段 citation.kukai_work。
- gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
- 主題タグは既存値 Counter 再利用優先・新値は 主題 軸内のみ。文体は daichidoron palette{問答/譬喩/偈/列挙}内。

## 再利用ビルダー運用（Round6 で導入・継続）
- outputs/daichidoron_round_builder.py：`--plan plan_roundN.json`（dry-run）／`--apply`／`--verify`（10項目＋巻き戻り）。
  mid は最大 m-id の次から自動連番・baseline は現在値から動的算出・全 assert 内蔵。
- outputs/insert_claudemd_star.py：CLAUDE.md 巨大単一行へ★エントリ安全挿入（最前・backup＋検証・冪等 sig=entry[:90]）。
- 各ラウンド：plan_roundN.json（データのみ）＋claudemd_entry_roundN.txt（★ 開始・〕終端）を書き、script は使い回し。

## 第7ラウンド 成果（m4124-m4131・8件・total 4154→4162）
三十七品義 摩訶衍〔大乗〕・章末。全段単独 motif（束ね無し）。引用元＝各段 citation.kukai_work。

| id | 段 | 節（巻19・三十七品義 摩訶衍） | 主タグ | 文体 | 核心 |
|---|---|---|---|---|---|
| m4124 | k086 | (28)身念処（空観・身車の譬・無作智門） | 四念処/空/三解脱門 | 問答/譬喩 | － |
| m4125 | k087 | (29)受念処（虚誑顛倒・不生の門） | 四念処/苦/三解脱門 | 問答 | － |
| m4126 | k088 | (30)心念処（心性不生不滅・客塵所染） | 四念処/不生不滅/自心本性清浄 | 問答 | 核心 |
| m4127 | k089 | (31)法念処・四正勤四如意足（諸法性浄・無生法忍門） | 四念処/無自性/無生法忍 | 問答 | 核心 |
| m4128 | k090 | (32)五根（三解脱門となす） | 五根/三解脱門/修行 | 問答/列挙 | － |
| m4129 | k091 | (33)知根・五力（衆生の根を知る・無生法忍を得る） | 五力/衆生救済/無生法忍 | 列挙 | － |
| m4130 | k092 | (34)七覚分（戯論を捨て寂滅を実法相） | 七覚分/諸法実相 | 問答/列挙 | － |
| m4131 | k093 | (35)八聖道分・章の結（三十七品→菩薩位→一切種智・巻末） | 八正道/菩薩道/一切種智 | 問答/列挙 | 核心 |

- 新タグ値1（既存 主題 軸内）：無生法忍（k089 無生法忍門・k091 五力＝無生法忍を得る）。
- 再利用：四念処/空/三解脱門/苦/不生不滅/自心本性清浄/無自性/五根/五力/修行/衆生救済/七覚分/諸法実相/八正道/菩薩道/一切種智。
  （五根/五力/七覚分/八正道 は R6 新設値・自心本性清浄 は sg27 由来の 主題 値）。
- 核心3件：m4126 心性本浄客塵所染（空海 自心本性清浄 sg27・阿字本不生 直結）・m4127 諸法性浄互不汚染＋無生法忍門・
  m4131 三十七品を観じ声聞辟支仏地を過ぎ菩薩位に入り一切種智を成ず（章の結・巻末＝声聞法→菩薩→仏の教判）。
- 整合性検証10項目＋巻き戻り assert 全 pass（engine verify・ALL PASS）：total==len==4162・m1-m4131 連番 dup無 sg31・
  新規8件 節/tags 半角括弧0・stats drift0（kakikudashi 1040209→1043088 +2879・gendaigoyaku 1809763→1815453 +5690・
  from_corpus_daichidoron 82→90・gabun intentional +8）・schema_history 302→303・verbatim 一致・
  m506 典籍曰く/m4041/m4042/m4062 温存・新規に大師系タグ0。
- 篇別内訳：daichidoron_三十七品義（摩訶衍・章末：菩薩の空観による四念処〜八聖道）（巻第十九・k086-k093）
  motif数8・id範囲 m4124-m4131。gabun：daichidoron_round7_m4124-m4131=8。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round7.json。
- CLAUDE.md：Round7 の★エントリ自動挿入済（R7→R6→R5→vol20 の newest-first・backup CLAUDE.md.bak_pre_daichi_round7）。
  ※phase1/bodaishin/round1-4/アンソロジー各回の★は依然 未反映（過去 handoff の貼付用テキストにのみ存在）。バックフィル可（別作業）。

## ★ 三十七品義（巻第十九・k059-k093 全35段）完走
R5（前半 総論＋四念処 k059-073・m4097-4111）＋R6（後半 声聞法 k074-085・m4112-4123）＋R7（摩訶衍 k086-093・m4124-4131）。

## 残ラウンド
着手時に段落を読み15〜30段でラウンド割確定→判定表→承認→engine（--plan dry-run→--apply→--verify）→
CLAUDE.md 自動挿入→handoff/commit_message→push。
- 四悉檀 k118-125／八念 k094-101／仏の徳 k102-105／九相・三解脱門・三十二相・十想・八背捨・四禅 k106-117／
  般若の讃嘆・陀羅尼・字門 k155-209／二諦 k210-212／清浄 k213-217／説話 k218-222（文体:譬喩・主題:本生 不使用）／
  菩提心 k223-225。大部は複数ラウンドに割る。素材価値目安：菩提心・清浄・二諦・仏の徳は高め、字門/陀羅尼は列挙主体。
- 孤立段：k029（巻七・三昧）・k030（巻十三・優婆塞五戒）＝別途「引用抜粋ラウンド」。
  k031（付録・genten無し）＝motif化不可で保留。
- 完走後：連動軸 retrofit（阿字本不生 sg08／自心本性清浄 sg27／二諦／畢竟空＝本来清浄／大悲↔菩提心／
  諸法実相↔本不生・世間即涅槃↔顕密・心性本浄↔sg27・無生法忍/一切種智↔阿字本不生菩提心）・gabun 裁定・
  kaimyo-app への motifs.json 同期。

## 次セッション開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md を読む。
2. `git log --oneline -3` で HEAD が「Round7」コミットと一致するか確認。
3. motifs.json：total 4162・最終 m4131・from_corpus_daichidoron=90 を確認。
4. 次区分の段落を読み plan_round8.json を作成→判定表→承認→
   `daichidoron_round_builder.py --plan ...`（dry-run→--apply→--verify）→★txt を insert_claudemd_star.py で挿入→
   handoff/commit_message→push。

## 落とし穴メモ
- ホスト側 Write は長文で truncate → script/commit_message/handoff は bash ヒアドキュメントで書き wc -l／tail で検証。
- k059-k225 の多くは kakikudashi フィールド空・genten のみ（Phase A 通り text_kakikudashi=genten）。gendaigoyaku は整備済（要確認）。
- insert_claudemd_star.py の冪等署名は entry[:90]。同日複数ラウンドは先頭90字が一意になるようエントリ文頭を差別化。
- commit_push.bat は data/indices/・root *.md・_dev_references/ を staging。作業前からの M（source.doc 2件）・?? が巻き込まれ得る。
  push 前に git status／staging を確認。今回 corpus 不変・変更は motifs.json＋CLAUDE.md（line1）＋handoff＋commit_message.txt。
- 既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

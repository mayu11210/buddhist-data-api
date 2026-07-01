# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第6ラウンド（三十七品義 後半・声聞法）完了＋再利用ビルダー導入

日付：2026-07-01
対象：data/indices/motifs.json（m4112-m4123 追加・total 4142→4154）
前提コミット（着手時 HEAD）：3969a10（Round5 三十七品義 前半 完了）

## Phase A 合意（ケンシン裁定・全ラウンド遵守／再掲）
- 本体直接書込・ID 連番末尾追記。著者＝伝・龍樹菩薩造・鳩摩羅什訳＝非空海 →引用形式:典籍曰く 全件・大師系タグ非付与。
- category:密教教学・出典:大智度論。text_kakikudashi＝漢文原典 genten・text_gendaigoyaku＝現代語訳（corpus verbatim）。
- 節＝section_major（"大智度論 " 除去）（section）。引用元＝各段 citation.kukai_work。
- gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
- 主題タグは既存値 Counter 再利用優先・新値は 主題 軸内のみ。文体は daichidoron palette{問答/譬喩/偈/列挙}内。

## ★ 効率化：本ラウンドより再利用ビルダー導入（ケンシン承認 2026-07-01）
以後の daichidoron ラウンドは以下で回す（毎回160行の build script 書き直しを廃止）：
- **outputs/daichidoron_round_builder.py**（plan JSON 駆動の engine）
  - `--plan plan_roundN.json`（dry-run・全 pre-assert）／`--apply`（backup＋書込）／`--verify`（10項目＋巻き戻り）
  - mid は現在の最大 m-id の次から items 順に自動連番。baseline（total/stats/from_corpus）は現在値から動的算出。
  - 内蔵 assert：total==len・m506 典籍曰く・sg31・anchor(m4041/m4042/m4062)・kk/gd drift0・
    節/引用元/tags 半角括弧0・大師系タグ禁止・文体 palette・verbatim。
- **outputs/insert_claudemd_star.py**（CLAUDE.md 巨大単一行への★エントリ安全挿入）
  - `--entry-file <txt>（★ 開始・〕終端）--label <名>`。最前（newest-first）へ挿入・backup＋検証（バイト増分・
    署名一意・NUL0・行数不変・挿入位置）・冪等（署名 entry[:90] 既在なら SKIP）。
- 各ラウンドの成果物：plan_roundN.json（データのみ）＋★エントリ txt。script 本体は使い回し。

## 第6ラウンド 成果（m4112-m4123・12件・total 4142→4154）
三十七品義 後半・声聞法。全段単独 motif（束ね無し）。引用元＝全段「（声聞乗の基礎実践・空海の教判での位置づけ）」。

| id | 段 | 節（巻19・三十七品義） | 主タグ | 文体 |
|---|---|---|---|---|
| m4112 | k074 | (16)四念処の三種 定義 | 四念処/修行 | 列挙 |
| m4113 | k075 | (17)性念処の分別 | 四念処/智慧 | 列挙 |
| m4114 | k076 | (18)共念処の分別 | 四念処/修行 | 列挙 |
| m4115 | k077 | (19)縁念処の分別 | 四念処/修行 | 列挙 |
| m4116 | k078 | (20)内身・外身の観 | 不浄/四念処/無我 | 問答/譬喩 |
| m4117 | k079 | (21)内外の受・心・法 | 四念処/苦 | 問答/列挙 |
| m4118 | k080 | (22)四正勤 | 四正勤/精進/修行 | 問答 |
| m4119 | k081 | (23)四如意足 | 四如意足/禅定/智慧 | 問答/譬喩 |
| m4120 | k082 | (24)五根・五力 | 五根/五力/修行 | 列挙 |
| m4121 | k083 | (25)七覚分 | 七覚分/修行 | 問答/列挙 |
| m4122 | k084 | (26)八聖道分 | 八正道/戒/修行 | 問答/列挙 |
| m4123 | k085 | (27)諸地具不具・声聞法分別の結 | 三十七品/修行 | 列挙 |

- 新タグ値6（既存 主題 軸内）：四正勤・四如意足・五根・五力・七覚分・八正道
  （＝三十七品の各科・R4 の四無量各成分/六度各波羅蜜 個別値化と同型）。
- 再利用：四念処/三十七品/修行/智慧/精進/禅定/不浄/無我/苦/戒。
- 核心0件（アビダルマ分別＋各科の技術的定義が中心・章の技術的締め。素材価値は R5 本論より低い）。
- 整合性検証10項目＋巻き戻り assert 全 pass（engine verify・ALL PASS）：total==len==4154・
  m1-m4123 連番 dup無 sg31・新規12件 節/tags 半角括弧0・stats drift0（kakikudashi 1036705→1040209 +3504・
  gendaigoyaku 1803361→1809763 +6402・from_corpus_daichidoron 70→82・gabun intentional +12）・
  schema_history 301→302・verbatim 一致・m506 典籍曰く/m4041/m4042/m4062 温存・新規に大師系タグ0。
- 篇別内訳：daichidoron_三十七品義（後半・声聞法：三種念処分別＋四正勤〜八正道）（巻第十九・k074-k085）
  motif数12・id範囲 m4112-m4123。gabun：daichidoron_round6_m4112-m4123=12。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round6.json。
- CLAUDE.md：Round5＋Round6 の★エントリを自動挿入済（従来 daichidoron 分は全て未反映だった）。
  backup outputs/CLAUDE.md.bak_pre_daichi_round5／_round6。※phase1/bodaishin/round1-4/アンソロジー各回の
  ★エントリは依然 未反映（過去 handoff の貼付用テキストにのみ存在）。必要ならバックフィル可（別作業）。

## 残ラウンド
着手時に段落を読み15〜30段でラウンド割確定→判定表→承認→engine（--plan dry-run→--apply→--verify）→
CLAUDE.md 自動挿入→handoff/commit_message→push。
- **R7 摩訶衍 k086-093（8段・素材価値高）**：菩薩の空観による身受心法念処・空無相無作の三解脱門・
  心性本浄客塵所染・無生法忍・一切種智で章末。核心候補あり（心性不生不滅つねに浄相 等）。
  これで三十七品義（全35段）完走。
- 四悉檀 k118-125／八念 k094-101／仏の徳 k102-105／九相・三解脱門・三十二相・十想・八背捨・四禅 k106-117／
  般若の讃嘆・陀羅尼・字門 k155-209／二諦 k210-212／清浄 k213-217／説話 k218-222（文体:譬喩・主題:本生 不使用）／
  菩提心 k223-225。k059-k225 は大部・複数ラウンドに割る。
- 孤立段：k029（巻七・三昧）・k030（巻十三・優婆塞五戒）＝別途「引用抜粋ラウンド」。
  k031（付録・genten無し）＝motif化不可で保留。
- 完走後：連動軸 retrofit（阿字本不生 sg08／二諦／畢竟空＝本来清浄／大悲↔菩提心／諸法実相↔本不生・
  世間即涅槃↔顕密）・gabun 裁定・kaimyo-app への motifs.json 同期。

## 次セッション開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md を読む。
2. `git log --oneline -3` で HEAD が「Round6」コミットと一致するか確認。
3. motifs.json：total 4154・最終 m4123・from_corpus_daichidoron=82 を確認。
4. R7（摩訶衍 k086-093）等の段落を読み plan_round7.json を作成→判定表→承認→
   `python3 outputs/daichidoron_round_builder.py --plan outputs/plan_round7.json`（dry-run）→`--apply`→`--verify`→
   ★エントリ txt を書き `insert_claudemd_star.py` で挿入→handoff/commit_message→push。

## 落とし穴メモ
- ホスト側 Write は長文で truncate → script/commit_message/handoff は bash ヒアドキュメントで書き wc -l／tail で検証。
- k059-k085 は kakikudashi フィールド空・genten のみ（Phase A 通り text_kakikudashi=genten）。gendaigoyaku は整備済。
- insert_claudemd_star.py の冪等署名は entry[:90]（第5/第6 の「前半 k059-k073」「後半 k074-k085」で区別）。
  同日同ラウンド種別の複数エントリを入れる時は先頭90字が一意になるようエントリ文頭を差別化すること。
- commit_push.bat は data/indices/・root *.md・_dev_references/ を staging。作業前からの M（source.doc 2件）・
  RD（旧メモ1件）・?? が巻き込まれ得る。push 前に git status／staging を確認。今回 corpus 不変・
  変更は motifs.json＋CLAUDE.md（line1）＋handoff＋commit_message.txt。
- 既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第8ラウンド（仏の徳・二諦・清浄・菩提心＝小区分4つ一括）完了

日付：2026-07-02
対象：data/indices/motifs.json（m4132-m4146 追加・total 4162→4177）
前提コミット（着手時 HEAD）：9e6fddf（Round7 三十七品義 摩訶衍・章末 完了＝三十七品義 全35段 完走）

## Phase A 合意（ケンシン裁定・全ラウンド遵守／再掲）
- 本体直接書込・ID 連番末尾追記。著者＝伝・龍樹菩薩造・鳩摩羅什訳＝非空海 →引用形式:典籍曰く 全件・大師系タグ非付与。
- category:密教教学・出典:大智度論。text_kakikudashi＝漢文原典 genten・text_gendaigoyaku＝現代語訳（corpus verbatim）。
- 節＝section_major（"大智度論 " 除去）（section）。引用元＝各段 citation.kukai_work。
- gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
- 主題タグは既存値 Counter 再利用優先・新値は 主題 軸内のみ。文体は daichidoron palette{問答/譬喩/偈/列挙}内。

## 再利用ビルダー運用（Round6 導入・継続）
- outputs/daichidoron_round_builder.py：`--plan plan_roundN.json`（dry-run）／`--apply`／`--verify`（10項目＋巻き戻り）。
- outputs/insert_claudemd_star.py：`--entry-file <★txt> --label roundN`。entry は「★ 」開始・「〕」終端（末尾に「・」を付けない）。
- 各ラウンド：plan_roundN.json＋claudemd_entry_roundN.txt を書き、script は使い回し。

## 第8ラウンド 成果（m4132-m4146・15件・total 4162→4177）
小区分4つ一括（R4 四無量心・六波羅蜜の複数区分一括前例に倣う・ケンシン承認）。全段単独 motif（束ね無し）。

| id | 段 | 区分・節 | 主タグ | 文体 | 核心 |
|---|---|---|---|---|---|
| m4132 | k102 | 仏の徳・十力（巻24） | 仏徳/十力 | 列挙 | － |
| m4133 | k103 | 四無所畏（牛王師子吼・巻25） | 仏徳/四無所畏 | 列挙/譬喩 | － |
| m4134 | k104 | 四無礙智（義法辞楽説・巻25） | 仏徳/四無礙智/言語 | 列挙 | － |
| m4135 | k105 | 十八不共法（巻26） | 仏徳/十八不共法 | 列挙 | － |
| m4136 | k210 | 二諦・名字是俗諦実相是第一義諦（巻55・論） | 二諦/仮名/諸法実相 | 問答 | － |
| m4137 | k211 | 不壊仮名而説諸法実相（帝釈讃・経） | 仮名/諸法実相/二諦 | 問答 | 核心 |
| m4138 | k212 | 仏讃の所以・一切法仮名ゆえ般若を学ぶ（論） | 仮名/師資/大悲 | 問答 | － |
| m4139 | k213 | 清浄・是浄甚深畢竟浄故の問答連鎖（巻63・経） | 清浄/畢竟空 | 問答 | － |
| m4140 | k214 | 諸法実相本自清浄・常住不壊・清浄の異名列挙（論） | 清浄/諸法実相/本来性 | 譬喩/列挙 | 核心 |
| m4141 | k215 | 畢竟浄無所著・諸仏も清浄に著せず（論） | 清浄/畢竟空/仏身 | 問答 | － |
| m4142 | k216 | 畢竟空即是我清浄五衆清浄（論） | 清浄/無我/畢竟空 | 譬喩 | － |
| m4143 | k217 | 畢竟空即是畢竟清浄・人は空を畏るるゆえ清浄と言う（論） | 清浄/畢竟空/般若智慧 | 問答 | 核心 |
| m4144 | k223 | 菩提心・菩提薩埵の名義（金剛山の大心・巻4） | 菩提心/菩薩道/衆生救済 | 問答/偈 | － |
| m4145 | k224 | 発心＝大誓願・初発心偈 | 菩提心/発心/誓願 | 偈 | 核心 |
| m4146 | k225 | 不退転の三法（金剛願・悲心徹骨入髄・般舟三昧） | 発心/不退転/大悲 | 列挙 | － |

- 新タグ値6（すべて既存 主題 軸内・ケンシン承認）：十力/四無所畏/四無礙智/十八不共法（R6 五根五力七覚分八正道 新設と
  同型・密教:十力 は既存だが密教軸非付与ゆえ主題軸に新設）・仮名（假名教義概念・k210-212 の3件・主題:言語(21) は
  言語論一般と使い分け）・不退転（阿鞞跋致・1件）。
- 再利用：仏徳(7)/言語/二諦(8)/諸法実相(23)/師資/大悲/清浄(2)/畢竟空(2)/本来性(253)/仏身/無我/般若智慧/菩提心(131)/
  菩薩道/衆生救済/発心/誓願。
- 核心4件（承認済）：m4137 不壊仮名而説諸法実相（空海 即事而真との接点）・m4140 本自清浄常住不壊（sg27 自心本性清浄
  直結）・m4143 畢竟空即畢竟清浄・人畏空故言清浄・m4145 初発心時誓願当作佛已過諸世間応受世供養（偈）。
- 整合性検証10項目＋巻き戻り assert 全 pass（engine verify・ALL PASS）：total==len==4177・m1-m4146 連番 dup無 sg31・
  新規15件 節/tags 半角括弧0・stats drift0（kakikudashi 1043088→1046160 +3072・gendaigoyaku 1815453→1823462 +8009・
  from_corpus_daichidoron 90→105・gabun intentional +15）・schema_history 303→304・verbatim 一致・
  m506 典籍曰く/m4041/m4042/m4062 温存・新規に大師系タグ0。
- 篇別内訳：daichidoron_仏の徳・二諦・清浄・菩提心（巻第二十四〜二十六/五十五/六十三/四・k102-k105/k210-k212/
  k213-k217/k223-k225）motif数15・id範囲 m4132-m4146。gabun：daichidoron_round8_m4132-m4146=15。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round8.json。
- CLAUDE.md：Round8 の★エントリ自動挿入済（R8→R7→R6→… newest-first・backup CLAUDE.md.bak_pre_daichi_round8 相当は
  script 既定 CLAUDE.md.bak 系）。※過去分（phase1/round1-4 等）の★未反映は継続（バックフィル可・別作業）。

## 残ラウンド
- 四悉檀 k118-125（8段）／八念 k094-101（8段）→ この2つで R9（16段）が自然。
- 九相・三解脱門・三十二相・十想・八背捨・四禅 k106-117（12段）→ R10 候補。
- 説話 k218-222（5段・文体:譬喩・主題:本生 不使用）→ 小ラウンドまたは他と併合。
- 般若の讃嘆・陀羅尼・字門 k155-209（55段・列挙主体・大部）→ 複数ラウンドに割る（R11 以降）。
- 孤立段：k029（巻7・三昧）・k030（巻13・優婆塞五戒）＝別途「引用抜粋ラウンド」。k031（付録・genten無し）＝保留。
- 完走後：連動軸 retrofit（阿字本不生 sg08／自心本性清浄 sg27←m4140／即身成仏義 即事而真←m4137／三種菩提心 sg22←
  m4144-4146／二諦／畢竟空＝本来清浄←m4143／大悲↔菩提心）・gabun 裁定・kaimyo-app への motifs.json 同期。

## 次セッション開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md を読む。
2. `git log --oneline -3` で HEAD が「Round8」コミットと一致するか確認。
3. motifs.json：total 4177・最終 m4146・from_corpus_daichidoron=105 を確認。
4. 次区分（四悉檀＋八念 の16段が第一候補）を読み plan_round9.json 作成→判定表→承認→
   engine（dry-run→--apply→--verify）→★txt を insert_claudemd_star.py（--entry-file/--label）で挿入→
   handoff/commit_message→push。

## 落とし穴メモ
- insert_claudemd_star.py の entry は「〕」終端必須（末尾に「・」を付けると assert で弾かれる）。冪等署名は entry[:90]。
- 長文（script/commit_message/handoff）は bash ヒアドキュメントで書き wc -l／tail で末尾検証。
- k094 以降の多くは kakikudashi 空・genten のみ（Phase A 通り text_kakikudashi=genten）。
- commit_push.bat は _dev_references/ も staging。作業前からの M（dainichikyo-sho-vol19/vol20_build/source.doc 2件）が
  巻き込まれ得る。push 前に git status 確認。今回の変更＝motifs.json＋CLAUDE.md（line1）＋handoff＋commit_message.txt。
- 既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

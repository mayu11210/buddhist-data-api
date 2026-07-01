# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第9ラウンド（八念・四悉檀＝2区分一括）完了

日付：2026-07-02
対象：data/indices/motifs.json（m4147-m4162 追加・total 4177→4193）
前提コミット（着手時 HEAD）：937f378（Round8 仏の徳・二諦・清浄・菩提心 完了）

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

## 第9ラウンド 成果（m4147-m4162・16件・total 4177→4193）
2区分一括（R8 前例に倣う・ケンシン承認）。全段単独 motif（束ね無し）。核心3件とも承認済。

| id | 段 | 区分・節 | 主タグ | 文体 | 核心 |
|---|---|---|---|---|---|
| m4147 | k094 | 八念（1）念仏・如来十号（巻21） | 八念/念仏/仏徳 | 問答/列挙 | － |
| m4148 | k095 | 八念（2）念法・法の六徳と三法印（巻22） | 八念/三法印 | 列挙/譬喩 | － |
| m4149 | k096 | 八念（3）念僧・無上福田・仏は医王法は良薬僧は瞻病人 | 八念/三宝/福田 | 譬喩/列挙 | 核心 |
| m4150 | k097 | 八念（4）念戒・有漏無漏戒・善法の住処 | 八念/持戒 | 譬喩/列挙 | － |
| m4151 | k098 | 八念（5）念捨・財施法施・捨煩悩 | 八念/布施/煩悩 | 譬喩/列挙 | － |
| m4152 | k099 | 八念（6）念天・五善法・四種の天 | 八念/因果 | 問答/列挙 | － |
| m4153 | k100 | 八念（7）念入出息・如雨淹塵 | 八念/観法/禅定 | 譬喩 | － |
| m4154 | k101 | 八念（8）念死・出る息に入るを望まず＝真修死相 | 八念/無常/不放逸 | 問答/譬喩 | 核心 |
| m4155 | k118 | 四悉檀（1）総説・八万四千法蔵皆実（巻1） | 四悉檀/教判 | 列挙 | － |
| m4156 | k119 | 四悉檀（2）世界悉檀・車と人の譬 | 四悉檀/因縁/仮名 | 譬喩 | － |
| m4157 | k120 | 四悉檀（3）世界悉檀の問答・乳の譬 | 四悉檀/二諦/仮名 | 問答/譬喩 | － |
| m4158 | k121 | 四悉檀（4）各各為人悉檀・破群那の会通 | 四悉檀/対機説法/方便 | 問答 | － |
| m4159 | k122 | 四悉檀（5）対治悉檀・薬の譬 | 四悉檀/対治/方便 | 譬喩/列挙 | － |
| m4160 | k123 | 四悉檀（6）無常は対治にして第一義にあらず | 四悉檀/対治/無常/空 | 問答/偈 | － |
| m4161 | k124 | 四悉檀（7）第一義悉檀・不可破不可散・戯論の偈 | 四悉檀/正見/言語 | 問答/偈 | － |
| m4162 | k125 | 四悉檀（8）第一義の結・過一切語言道心行処滅・実相偈 | 四悉檀/諸法実相/言語 | 問答/偈 | 核心 |

- 新タグ値2（いずれも主題軸内・ケンシン承認）：八念（8件・R6 五根五力七覚分八正道 新設と同型・既存 主題:念仏 と併用）・
  四悉檀（8件・主題:教判 は教判論一般と使い分け）。
- 再利用：念仏/仏徳/三法印/三宝/福田/持戒/布施/煩悩/因果/観法/禅定/無常/不放逸/教判/因縁/仮名/二諦/対機説法/方便/
  対治/空/正見/諸法実相/言語。
- 核心3件（承認済）：m4149 仏は医王・法は良薬・僧は瞻病人／m4154 出る息に入るを望まず（真修死相・不放逸）／
  m4162 過一切語言道心行処滅＋一切実一切非実の実相偈。
- 整合性検証10項目＋巻き戻り assert 全 pass（engine verify・ALL PASS）：total==len==4193・m1-m4162 連番 dup無 sg31・
  新規16件 節/tags 半角括弧0・stats drift0（kakikudashi 1046160→1049670 +3510・gendaigoyaku 1823462→1831269 +7807・
  from_corpus_daichidoron 105→121・gabun intentional +16）・schema_history 304→305・verbatim 一致・
  m506 典籍曰く/m4041/m4042/m4062 温存・新規に大師系タグ0。
- 篇別内訳：daichidoron_八念・四悉檀（巻第二十一〜二十二/第一・k094-k101/k118-k125）motif数16・id範囲 m4147-m4162。
  gabun：daichidoron_round9_m4147-m4162=16。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round9.json。
- CLAUDE.md：Round9 の★エントリ自動挿入済（R9→R8→… newest-first・backup outputs/CLAUDE.md.bak_pre_round9）。
  ※過去分（phase1/round1-4 等）の★未反映は継続（バックフィル可・別作業）。

## 残ラウンド
- 九相・三解脱門・三十二相・十想・八背捨・四禅 k106-117（12段）→ R10 第一候補。
- 説話 k218-222（5段・文体:譬喩・主題:本生 不使用）→ 小ラウンドまたは他と併合。
- 般若の讃嘆・陀羅尼・字門 k155-209（55段・列挙主体・大部）→ 複数ラウンドに割る（R11 以降）。
- 孤立段：k029（巻7・三昧）・k030（巻13・優婆塞五戒）＝別途「引用抜粋ラウンド」。k031（付録・genten無し）＝保留。
- 完走後：連動軸 retrofit（阿字本不生 sg08／自心本性清浄 sg27←m4140／即身成仏義 即事而真←m4137／三種菩提心 sg22←
  m4144-4146／二諦／畢竟空＝本来清浄←m4143／言語道断心行処滅←m4162／大悲↔菩提心）・gabun 裁定・
  kaimyo-app への motifs.json 同期。

## 次セッション開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md を読む。
2. `git log --oneline -3` で HEAD が「Round9」コミットと一致するか確認。
3. motifs.json：total 4193・最終 m4162・from_corpus_daichidoron=121 を確認。
4. 次区分（九相〜四禅 k106-117 の12段が第一候補）を読み plan_round10.json 作成→判定表→承認→
   engine（dry-run→--apply→--verify）→★txt を insert_claudemd_star.py（--entry-file/--label）で挿入→
   handoff/commit_message→push。

## 落とし穴メモ
- insert_claudemd_star.py の entry は「〕」終端必須（末尾に「・」を付けると assert で弾かれる）。冪等署名は entry[:90]。
- 長文（script/commit_message/handoff）は bash ヒアドキュメントで書き wc -l／tail で末尾検証。
- k094 以降の多くは kakikudashi 空・genten のみ（Phase A 通り text_kakikudashi=genten）。
- commit_push.bat は _dev_references/ も staging。作業前からの M（dainichikyo-sho-vol19/vol20_build/source.doc 2件）が
  巻き込まれ得る。push 前に git status 確認。今回の変更＝motifs.json＋CLAUDE.md（line1）＋handoff＋commit_message.txt。
- 既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

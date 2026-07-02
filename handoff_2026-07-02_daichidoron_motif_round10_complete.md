# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第10ラウンド（九相・三解脱門・三十二相・十想・八背捨・四禅＝6区分一括）完了

日付：2026-07-02
対象：data/indices/motifs.json（m4163-m4174 追加・total 4193→4205）
前提コミット（着手時 HEAD）：aed2907（Round9 八念・四悉檀 完了）

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

## 第10ラウンド 成果（m4163-m4174・12件・total 4193→4205）
6区分一括（R8/R9 前例に倣う・ケンシン承認）。全段単独 motif（束ね無し）。核心3件とも承認済。

| id | 段 | 区分・節 | 主タグ | 文体 | 核心 |
|---|---|---|---|---|---|
| m4163 | k106 | 九相観 総説（巻21）・九相如縛賊十想如斬殺・身念処より涅槃城門 | 九相/不浄/観法 | 問答/列挙 | － |
| m4164 | k107 | 九相観 各相・膨脹〜焼の九段・一切有身皆帰無常 | 九相/不浄/無常 | 譬喩/列挙 | 核心 |
| m4165 | k108 | 三解脱門 総説（巻20）・空無相無作の定義・狂慧と三昧 | 三解脱門/空/三昧 | 問答/列挙 | － |
| m4166 | k109 | 三解脱門 摩訶衍・城の三門一門より入る・世間即是涅槃・愛見配当 | 三解脱門/諸法実相/対機説法 | 譬喩 | 核心 |
| m4167 | k110 | 三十二相（巻4）・足下安平〜白毫の列挙 | 三十二相/仏身/仏徳 | 列挙/譬喩 | － |
| m4168 | k111 | 三十二相と荘厳の義・七事勝転輪聖王・豪貴の女の譬 | 三十二相/仏身/教化 | 問答/譬喩 | － |
| m4169 | k112 | 十想（1）（巻23）・無常想苦想無我想 | 十想/無常/苦/無我 | 列挙 | 核心 |
| m4170 | k113 | 十想（2）・食不浄想（醸酒の譬）・一切世間不可楽想（八苦） | 十想/不浄/苦 | 譬喩/列挙 | － |
| m4171 | k114 | 十想（3）・死想不浄想・断離盡は涅槃を縁ず | 十想/涅槃/煩悩 | 列挙 | － |
| m4172 | k115 | 八背捨（巻21）・浄潔の五欲を背捨・浄背捨身作証 | 八背捨/禅定/観法 | 列挙 | － |
| m4173 | k116 | 八勝処・十一切処・勝知勝観で結使に随わず | 八背捨/禅定/煩悩 | 列挙 | － |
| m4174 | k117 | 四禅（巻20）・離五欲〜捨念清浄・如人服薬の譬 | 禅定/教化/方便 | 列挙/譬喩 | － |

- 新タグ値4（いずれも主題軸内・区分名＝法数名で R6/R9 新設と同型・ケンシン承認）：
  九相（2件・主題:不浄 と併用）・三十二相（2件・主題:仏身/仏徳 と併用）・十想（3件・主題:無常/苦/無我 と併用）・
  八背捨（2件・八勝処十一切処も同区分＝得解観の一連ゆえ2段とも付与）。
- 再利用：不浄/観法/無常/空/三昧/諸法実相/対機説法/仏身/仏徳/教化/苦/無我/涅槃/煩悩/禅定/方便。
- 核心3件（承認済）：m4164 一切有身皆帰無常／m4166 世間即是涅槃（即事而真と響き合う）／
  m4169 無常生厭・苦生畏・無我出抜令解脱。
- 整合性検証10項目＋巻き戻り assert 全 pass（engine verify・ALL PASS）：total==len==4205・m1-m4174 連番 dup無 sg31・
  新規12件 節/tags 半角括弧0・stats drift0（kakikudashi +2756・gendaigoyaku +5879・
  from_corpus_daichidoron 121→133・gabun intentional +12）・schema_history 305→306・verbatim 一致・
  m506 典籍曰く/m4041/m4042/m4062 温存・新規に大師系タグ0。
- 篇別内訳：daichidoron_九相・三解脱門・三十二相・十想・八背捨・四禅（巻第二十〜二十三/第四・k106-k117）
  motif数12・id範囲 m4163-m4174。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round10.json。
- CLAUDE.md：Round10 の★エントリ自動挿入済（R10→R9→… newest-first・backup は insert script 管理）。
  ※過去分（phase1/round1-4 等）の★未反映は継続（バックフィル可・別作業）。

## 残ラウンド
- 般若の讃嘆・陀羅尼・字門 k155-209（55段・列挙主体・大部）→ 複数ラウンドに割る（R11 以降・次セッション第一候補。
  着手時に55段の内訳を読み 15〜30 段単位のラウンド割を確定させること）。
- 説話 k218-222（5段・文体:譬喩・主題:本生 不使用）→ 小ラウンドまたは他と併合。
- 孤立段：k029（巻7・三昧）・k030（巻13・優婆塞五戒）＝別途「引用抜粋ラウンド」。k031（付録・genten無し）＝保留。
- 完走後：連動軸 retrofit（阿字本不生 sg08／自心本性清浄 sg27←m4140／即身成仏義 即事而真←m4137・m4166／
  三種菩提心 sg22←m4144-4146／二諦／畢竟空＝本来清浄←m4143／言語道断心行処滅←m4162／大悲↔菩提心）・
  gabun 裁定・kaimyo-app への motifs.json 同期。

## 次セッション開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md を読む。
2. `git log --oneline -3` で HEAD が「Round10」コミットと一致するか確認。
3. motifs.json：total 4205・最終 m4174・from_corpus_daichidoron=133 を確認。
4. 次区分（般若讃嘆・陀羅尼・字門 k155-209 のラウンド割確定→R11）を読み plan_round11.json 作成→判定表→承認→
   engine（dry-run→--apply→--verify）→★txt を insert_claudemd_star.py（--entry-file/--label）で挿入→
   handoff/commit_message→push。

## 落とし穴メモ
- insert_claudemd_star.py の entry は「〕」終端必須（末尾に「・」を付けると assert で弾かれる）。冪等署名は entry[:90]。
- 長文（script/commit_message/handoff）は bash ヒアドキュメントで書き wc -l／tail で末尾検証。
- k106-k117 は kakikudashi 空・genten のみ（Phase A 通り text_kakikudashi=genten）。k155 以降も同様の見込み。
- commit_push.bat は _dev_references/ も staging。作業前からの M（dainichikyo-sho-vol19/vol20_build/source.doc 2件）が
  巻き込まれ得る。push 前に git status 確認。今回の変更＝motifs.json＋CLAUDE.md（line1）＋handoff＋commit_message.txt。
- 既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第11ラウンド（般若波羅蜜・讃般若偈・四十二字門＝2区分一括）完了

日付：2026-07-02
対象：data/indices/motifs.json（m4175-m4189 追加・total 4205→4220）
前提コミット（着手時 HEAD）：2e18a97（Round10 九相〜四禅 完了）

## Phase A 合意（ケンシン裁定・全ラウンド遵守／再掲）
- 本体直接書込・ID 連番末尾追記。著者＝伝・龍樹菩薩造・鳩摩羅什訳＝非空海 →引用形式:典籍曰く 全件・大師系タグ非付与。
- category:密教教学・出典:大智度論。text_kakikudashi＝漢文原典 genten・text_gendaigoyaku＝現代語訳（corpus verbatim）。
- 節＝section_major（"大智度論 " 除去）（section）。引用元＝各段 citation.kukai_work。
- gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
- 主題タグは既存値 Counter 再利用優先・新値は 主題 軸内のみ。文体は daichidoron palette{問答/譬喩/偈/列挙}内。

## k155-209（55段）のラウンド割（今セッションでケンシン承認・確定）
- R11＝般若波羅蜜＋讃般若偈＋四十二字門 k155-169（15段）＝本ラウンド完了。
- R12＝四念処（経④＋論⑨）＋摩訶衍総枠＋陀羅尼総論 k170-188（19段）。
- R13＝寶塔校量品＋述誠品＋如法性実際 k189-209（21段）。
ブロック境界を崩さず corpus 順。R12/R13 は未着手。

## 再利用ビルダー運用（Round6 導入・継続）
- outputs/daichidoron_round_builder.py：`--plan plan_roundN.json`（dry-run）／`--apply`／`--verify`（10項目＋巻き戻り）。
- outputs/insert_claudemd_star.py：`--entry-file <★txt> --label roundN`。entry は「★ 」開始・「〕」終端（末尾に「・」を付けない）。
- 各ラウンド：plan_roundN.json＋claudemd_entry_roundN.txt を書き、script は使い回し。

## 第11ラウンド 成果（m4175-m4189・15件・total 4205→4220）
2区分一括（巻18 般若波羅蜜／巻48 四十二字門・ケンシン承認）。全段単独 motif（束ね無し）。核心3件承認済。

| id | 段 | 節 | 主タグ | 文体 | 核心 |
|---|---|---|---|---|---|
| m4175 | k155 | 般若波羅蜜（1）定義・因中説果・仏心中は一切種智 | 般若波羅蜜/一切種智/智慧 | 問答 | － |
| m4176 | k156 | （2）入海と燈の譬・煩悩の習と合しつつ実相を得る | 般若波羅蜜/諸法実相/煩悩 | 問答/譬喩 | － |
| m4177 | k157 | （3）諸法実相とは・捨一切観滅一切言語・如涅槃相 | 諸法実相/不生不滅/涅槃 | 問答/偈 | 核心 |
| m4178 | k158 | （4）なぜ摩訶か・四大人皆般若より生ず・諸仏の母 | 般若波羅蜜/涅槃/仏徳 | 問答 | － |
| m4179 | k159 | （5）三門・蜫勒/阿毘曇/空門・生空と法空 | 空/対機説法/仏法 | 列挙 | － |
| m4180 | k160 | （6）真空と邪見の別・塩の譬 | 空/顛倒/外道破 | 問答/譬喩 | － |
| m4181 | k161 | （7）一相と種種相・自性空に入れ無所著 | 諸法実相/方便/慈悲 | 列挙/譬喩 | － |
| m4182 | k162 | （8）無相無得・以無所得為得・梯と船の譬 | 般若波羅蜜/六波羅蜜/禅定 | 問答/譬喩 | 核心 |
| m4183 | k163 | 讃般若波羅蜜偈（上）・無所来去・縛と解脱 | 般若波羅蜜/智慧/解脱 | 偈 | －（候補どまり・非付与） |
| m4184 | k164 | 讃般若波羅蜜偈（下）・大火焰の不可取 | 般若波羅蜜/仮名/言語 | 偈 | － |
| m4185 | k165 | 四十二字門（経①）・阿字門一切法初不生 | 字門/阿字/本不生 | 列挙 | 核心 |
| m4186 | k166 | （経②）過荼無字・諸法如虚空＝阿字義 | 字門/虚空/言語 | 列挙 | － |
| m4187 | k167 | （経③）阿字印の二十功徳 | 字門/陀羅尼/功徳 | 列挙 | － |
| m4188 | k168 | （論①）字等語等＝畢竟空涅槃と同等・四十二字は一切字の根本 | 字門/陀羅尼/畢竟空 | 問答/列挙 | － |
| m4189 | k169 | （論②）字を破散すれば畢竟空＝般若・破竹の譬 | 字門/畢竟空/言語 | 譬喩 | － |

- 新タグ値：0（陀羅尼(1)・字門(50)・阿字(13)・本不生(67)・虚空(6)・功徳(5)・言語(24)・外道破(21) 等すべて既存値再利用）。
- 核心3件（承認済）：m4177 捨一切観滅一切言語・如涅槃相／m4182 以無所得為得／m4185 阿字門一切法初不生。
- m4185 は完走後の連動軸 retrofit で sg08（阿字本不生）連動の最有力候補（handoff R10 の retrofit リストに追加）。
- 整合性検証10項目＋巻き戻り assert 全 pass（engine verify・ALL PASS）：total==len==4220・m1-m4189 連番 dup無 sg31・
  新規15件 節/tags 半角括弧0・stats drift0（kakikudashi +3451・gendaigoyaku +7081・
  from_corpus_daichidoron 133→148・gabun intentional +15）・schema_history 306→307・verbatim 一致・
  m506 典籍曰く/m4041/m4042/m4062 温存・新規に大師系タグ0。ホスト側 Grep で total 4220/m4189/148 反映確認済。
- 篇別内訳：daichidoron_般若波羅蜜・讃般若偈・四十二字門（巻第十八/第四十八・k155-k169）motif数15・id範囲 m4175-m4189。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round11.json。
- CLAUDE.md：Round11 の★エントリ自動挿入済（+2627bytes・署名一意・NUL0）。
  ※過去分（phase1/round1-4 等）の★未反映は継続（バックフィル可・別作業）。

## 残ラウンド
- R12＝四念処＋摩訶衍総枠＋陀羅尼総論 k170-188（19段）→ 次セッション第一候補。
- R13＝寶塔校量品＋述誠品＋如法性実際 k189-209（21段）。
- 説話 k218-222（5段・文体:譬喩・主題:本生 不使用）→ 小ラウンドまたは他と併合。
- 孤立段：k029（巻7・三昧）・k030（巻13・優婆塞五戒）＝別途「引用抜粋ラウンド」。k031（付録・genten無し）＝保留。
- 完走後：連動軸 retrofit（阿字本不生 sg08←m4185・m4165 系／自心本性清浄 sg27←m4140／即身成仏義 即事而真←m4137・m4166／
  三種菩提心 sg22←m4144-4146／二諦／畢竟空＝本来清浄←m4143／言語道断心行処滅←m4162／大悲↔菩提心）・
  gabun 裁定・kaimyo-app への motifs.json 同期。

## 次セッション開始手順
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md を読む。
2. `git log --oneline -3` で HEAD が「Round11」コミットと一致するか確認。
3. motifs.json：total 4220・最終 m4189・from_corpus_daichidoron=148 を確認。
4. R12（k170-188・19段）を読み plan_round12.json 作成→判定表→承認→
   engine（dry-run→--apply→--verify）→★txt を insert_claudemd_star.py（--entry-file/--label）で挿入→
   handoff/commit_message→push。

## 落とし穴メモ
- insert_claudemd_star.py の entry は「〕」終端必須（末尾に「・」を付けると assert で弾かれる）。冪等署名は entry[:90]。
- 長文（script/commit_message/handoff）は bash ヒアドキュメントで書き wc -l／tail で末尾検証。
- k155-169 は kakikudashi 空・genten のみ（Phase A 通り text_kakikudashi=genten）。k170 以降も同様の見込み。
- commit_push.bat は _dev_references/ も staging。作業前からの M（dainichikyo-sho-vol19/vol20_build/source.doc 2件）が
  巻き込まれ得る。またリポジトリ直下に未追跡の DST・ZoomInstallerFull.exe あり（作業対象外）→ push 前に git status 確認。
- 既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

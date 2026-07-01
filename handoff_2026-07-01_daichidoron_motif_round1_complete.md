# 引き継ぎ：大智度論（空海引用集）Phase3 motif 抽出 第1ラウンド 完了

日付：2026-07-01
対象：data/indices/motifs.json（m4042-m4045 追加）＋ data/kukai/daichidoron.json（菩提心 k223-225・未pushぶん同梱）

## Phase A 合意（ケンシン裁定・全ラウンド遵守）
- 書込方式：本体直接書込。ID は既存最終 m4041 の次から連番（今回 m4042-m4045）。
- 著者＝伝・龍樹菩薩造・鳩摩羅什訳＝非空海 →**引用形式:典籍曰く 全件**・大師系タグ非付与。
  source に 著者 保持（"伝・龍樹菩薩造・鳩摩羅什訳"）。
- category：**category:密教教学**（龍樹の菩提心論など既存教学 corpus と揃える・(a)採用）。出典:大智度論。
- **text_kakikudashi ＝ 漢文原典（genten）を採用**（アンソロジーは書き下し層なし＝(a)採用）。
  text_gendaigoyaku ＝ 現代語訳。いずれも corpus から verbatim。
- gabun（雅文体）は意図的未設定（後日 retrofit 可）。連動軸は完走後 retrofit。
- 短小段落の束ね：あり（今回は該当なし・全て単独 motif）。

## 第1ラウンド成果（m4042-m4045・4件・total 4072→4076）
| id | 段落 | 大智度論 | 主タグ | 一句性 |
|---|---|---|---|---|
| m4042 | k001 | 巻5 等忍〜無生忍 | 主題:諸法実相/不生不滅/無生忍・密教:本不生・文体:偈 | 核心（八不偈） |
| m4043 | k002 | 巻9 仏の二種身 | 主題:法身/二身・密教:法身・文体:問答 | 核心（法性身・父母生身） |
| m4044 | k003 | 巻38 二諦 | 主題:二諦/世俗諦/第一義諦・文体:問答 | 核心（佛法中有二諦） |
| m4045 | k004 | 巻27 三智 | 主題:三智/一切智/一切種智・文体:問答 | － |
- 新タグ値（既存 主題 軸内の値追加）：主題:世俗諦/第一義諦/一切智/二身/無生忍/不生不滅。
  再利用：主題:二諦(既7)/三智(既1)/一切種智(既1)/法身(既99)/諸法実相(既10)、密教:本不生/法身、文体:偈/問答。
- 整合性検証10項目＋巻き戻り assert（m506 典籍曰く／sg31／famous31／m4041 温存／stats=recompute drift0／verbatim一致）**全 pass**。
- stats：total 4076・kakikudashi_chars_total/gendaigoyaku_chars_total 加算・from_corpus_daichidoron=4・
  篇別内訳['daichidoron'] 追加・motifs_without_gendai_gabun_intentional['daichidoron_round1_m4042-m4045'] 追加・
  schema_history 295→296（top-level・stats側は温存）。
- バックアップ：outputs/motifs_backup_pre_daichidoron_round1.json。

## 残ラウンド（handoff 記載・225段落 → 推定 200+ motif・多セッション）
- R2 以降：十八空品 k005-k028（24段・内外空/空空/大空/第一義空/畢竟空/無始空…）→ 2ラウンド程度に分割。
- 十喩 k032-042／四悉檀 k118-125／四無量 k043-049／六波羅蜜 k050-058／三十七品 k059-093／
  八念 k094-101／仏の徳 k102-105／九相/三解脱門/三十二相/十想/八背捨/四禅／
  二諦 k210-212／清浄 k213-217／説話 k218-222／菩提心 k223-225 等。
  ※ k218-222 説話は 本生譚（文体:譬喩/主題:本生 は不使用＝文体:譬喩で表す先例に留意）。
  ※ 主題タグは毎ラウンド既存値を Counter で集計し再利用優先・新値は軸内のみ。
- 完走後：連動軸 retrofit（阿字本不生 sg08/二諦 等と daichidoron の親子連動）・gabun 裁定・
  kaimyo-app への motifs.json 同期（NUL0/total/引用形式タグ反映）。

## ★ CLAUDE.md タイトル更新（未反映・貼付用）— 720KB 単一行で Edit ツール不可のため保留
次の★エントリを CLAUDE.md 冒頭タイトル「…2026-04-25〜・」の直後に手動挿入してください：
「★ 2026-07-01 大智度論（空海引用集・daichidoron.json）Phase3 motif 抽出 第1ラウンド完了〔k001-k004→m4042-m4045・4件・total 4072→4076・引用形式:典籍曰く 全件（伝・龍樹造/鳩摩羅什訳＝非空海）・category:密教教学・出典:大智度論・gabun 意図的未設定・text_kakikudashi＝漢文原典 genten・核心3〔八不偈・二身・二諦〕・新タグ値 主題:世俗諦/第一義諦/一切智/二身/無生忍/不生不滅・整合性検証10項目＋m506 巻き戻り assert 全 pass・schema_history 295→296・残＝R2 十八空品 以降〕」

## この push に含まれるもの（HEAD=eaab5d1 説話 からの差分）
- data/indices/motifs.json（Round1 追記・主）
- data/kukai/daichidoron.json（菩提心 k223-225・未pushぶん）＋ _corpus_manifest.json（paragraphs 222→225）
- commit_message.txt（2件合体）・handoff（本ファイル＋菩提心 handoff）
commit_push.bat は data/indices/ を staging 済（motifs.json 反映される）。

## 落とし穴メモ
- 文書はホスト側ツールで編集。motifs.json は bash 側で書き、ホスト側で total/最終 m-id を確認済。
- 全角括弧厳守・既存 motif／他 corpus には触れない（追記のみ）。1リポジトリ1書き手。

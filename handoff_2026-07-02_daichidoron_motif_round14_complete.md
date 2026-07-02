# 引き継ぎ：大智度論 Phase3 motif 抽出 第14ラウンド【完了】

日付：2026-07-02
状態：**R14 完了・motifs.json 書込済・検証全 pass・push 待ち**。
着手時 HEAD：01e35ab（R13 完了コミット）。

## 経緯
- R13 handoff の「残ラウンド＝説話 k218-222（5段）」から着手。
- 着手前チェック（HEAD 01e35ab・total 4260・m4229・from_corpus 188・schema_history 309・schema_version 0.2 一致・R13 push 済・並行セッション無し）
  → k218-222 の genten／gendaigoyaku を読み判定表をケンシンに提示 → **承認（このまま）**（核心2＝k219/k222）→ 書込実施。

## Phase A 合意（継続・全件適用）
引用形式:典籍曰く 全件（伝・龍樹菩薩造/鳩摩羅什訳＝非空海）・category:密教教学・出典:大智度論・
text_kakikudashi＝漢文原典 genten・gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
全段単独 motif（束ね無し）・文体は daichidoron palette{問答/譬喩/偈/列挙}内。新タグ値は原則0。

## 成果（判定表どおり・5段→5件・全段単独 motif・束ね無し）
- id：m4230-m4234／段：k218-k222／篇別内訳キー：daichidoron_説話〈本生・言及〉六波羅蜜（巻第四/第十四/第四十九ほか・k218-k222）
- k218 尸毘王の割肉貿鴿（檀波羅蜜満・慈悲捨身）m4230〔主題:布施/慈悲/衆生救済・文体:譬喩〕
- k219 須陀須摩王と鹿足王（尸羅波羅蜜満・実語持戒）m4231 核心〔主題:持戒/戒・文体:譬喩/偈〕
- k220 毒龍の持戒（尸羅波羅蜜・一日戒・捨身法施）m4232〔主題:持戒/戒/布施・文体:譬喩〕
- k221 羼提仙人と歌利王（羼提波羅蜜・忍辱・慈）m4233〔主題:忍辱/慈悲・文体:譬喩〕
- k222 薩陀波崙〈常啼〉菩薩の求法（言及・敬師）m4234 核心〔主題:師資/精進・文体:列挙〕
- 核心2：
  - m4231（k219）実語第一戒偈＝実語第一戒・実語昇天梯・実語小而大・妄語入地獄（実語＝第一の戒の典拠・法話素材）
  - m4234（k222）十方仏教＝汝、法師に於いて其の短を念ずる莫れ、常に敬畏を生ぜよ（敬師・求法捨身の範）
- 核心の代替候補（今回は非付与）：m4230（k218 実誓願で身平復）・m4232（k220 今以肉施後以法施）・m4233（k221 我修慈忍心不動・血変為乳）
- 新タグ値0（布施/慈悲/衆生救済/持戒/戒/忍辱/師資/精進 全て既存値再利用）
- 裁定メモ：k219「実語」・k222「求法」は本来の核心概念だが既存値へ写像（実語→持戒/戒、求法→精進/師資）。厳密に立てるなら 主題:実語・主題:求法 の新設も可（ケンシンは「このまま承認」＝新設せず）。

## stats 差分（期待値どおり）
- total_motifs 4260→4265／最終 id m4229→m4234／from_corpus_daichidoron 188→193
- kakikudashi_chars +1437／gendaigoyaku_chars +3404（改行除き）
- schema_history 309→310（origin: daichidoron_round14）
- motifs_without_gendai_gabun_intentional に daichidoron_round14_m4230-m4234=5 追記

## 検証
- engine（outputs/daichidoron_round_builder.py --verify）10項目＋巻き戻り assert（m506/anchor/大師0/典籍曰く）全 pass。
- ホスト側 Grep で total 4265・m4234・from_corpus 193・schema_history 310・篇別内訳キー・gabun エントリ・CLAUDE.md ★entry round14 反映確認済。
- backup：outputs/motifs_backup_pre_daichidoron_round14.json。
- CLAUDE.md ★entry round14 挿入済（insert_claudemd_star.py・+2044bytes・行数 1395 不変・署名一意・NUL0）。

## 残ラウンド（R14 の後）——大智度論は本生譚まで消化、以後は特殊段のみ
- **孤立段 k029/k030＝別途「引用抜粋」ラウンド**（次はここが候補）。
- k031＝genten 無しで motif 化不可・保留。
- 完走後：連動軸 retrofit（sg08←m4185・m4203・m4210 等の阿字/真言/畢竟空 候補、諸法実相/法性系 候補・handoff R11/R12 のリスト参照）・gabun 裁定・kaimyo-app 同期。
  今回の核心 m4231（実語第一戒偈）・m4234（敬師）も retrofit 時の成句/連動候補として要検討。

## 落とし穴（継続）
- CLAUDE.md は単一行巨大ファイル・Edit 不可→insert_claudemd_star.py 必須（entry「★ 」開始・「〕」終端・内部改行不可・冪等 sig=entry[:90]）。
- 長文は bash ヒアドキュメントで書き末尾検証。全角括弧のみ・割注〔 〕〈 〉。文書はホスト側 Read/Write/Edit。
- commit_push.bat は data/indices/・CLAUDE.md・*.md（handoff 含む）・_dev_references/ を staging。
  作業前からの M 2件（_dev_references/dainichikyo-sho-vol19/20_build/source.doc）が同梱され得る（既知・許容）。
  直下の未追跡 DST・ZoomInstallerFull.exe・_dev_scripts/・outputs/ は staging 対象外→push 前に git status 確認。
  作業前から RD（rename/削除表示）1件＝引き継ぎメモ_2026-05-06_…idx48….md 系の phantom rename が git status に出る（既知・今回作成なし）。Step 4.5 SAFETY CHECK（deleted: 検出で中止）は今回 deletion 無しで pass 見込み。
- 1リポジトリ1書き手。既存 motif・他 corpus に触れない（追記のみ）。

## 次セッション開始手順（R15＝孤立段 k029/k030 引用抜粋ラウンド等）
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md（kakikudashi-data スキル同梱）を読む。
2. `git log --oneline -3` で HEAD＝R14 コミット・motifs.json 4265/m4234/193/310 を確認。
3. k029/k030 の corpus 本文を読み判定表を作成→提示→承認→plan_round15.json→engine dry-run→apply→verify→
   claudemd_entry_round15.txt→insert_claudemd_star.py --label round15→handoff/commit_message→git status 確認→push 依頼。

## ケンシン貼付用テンプレ（次セッション）
```
buddhist-data-api の大智度論（daichidoron.json）Phase3 motif 抽出 R15（孤立段 k029/k030・引用抜粋ラウンド）を開始してください。
まず CLAUDE.md 冒頭と handoff_2026-07-02_daichidoron_motif_round14_complete.md を読み、
references/motif-extraction.md（kakikudashi-data スキル同梱）に従うこと。
現状：HEAD＝R14 コミット・motifs.json は total 4265・最終 m4234・from_corpus_daichidoron=193・schema_history 310。
手順：k029/k030 を読み判定表を私に提示→承認→plan_round15.json→daichidoron_round_builder.py dry-run→--apply→--verify→
claudemd_entry_round15.txt→insert_claudemd_star.py→handoff/commit_message 更新→git status 確認→push 依頼。
Phase A 合意継続（引用形式:典籍曰く 全件・gabun 未設定・連動軸 retrofit 後回し）。新タグ値は原則 0 で設計。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。commit_push.bat は _dev_references/ も staging・
直下の未追跡 DST/ZoomInstallerFull.exe/_dev_scripts/ は対象外→push 前に git status 確認。
k031 は genten 無しで保留。完走後に連動軸 retrofit・gabun 裁定・kaimyo-app 同期。
```

# 引き継ぎ：大智度論 Phase3 motif 抽出 第15ラウンド【完了】

日付：2026-07-02
状態：**R15 完了・motifs.json 書込済・検証全 pass・push 待ち**。
着手時 HEAD：5cf2fb3（R14 完了コミット）。

## 経緯
- R14 handoff の「残ラウンド＝孤立段 k029/k030 引用抜粋ラウンド」から着手。
- 着手前チェック（HEAD 5cf2fb3・total 4265・m4234・from_corpus 193・schema_history 310・schema_version 0.2 一致・R14 push 済・並行セッション無し・k029/k030 未収録）
  → k029/k030 の genten／gendaigoyaku を読み判定表をケンシンに提示 → **承認（このまま）**（核心1＝k029）→ 書込実施。
- 着手前に git のワークツリー phantom（下記「落とし穴」）を整理する cleanup スクリプトを用意（apply は git 非依存のため motif 作業は lock の影響を受けず先行実施）。

## Phase A 合意（継続・全件適用）
引用形式:典籍曰く 全件（伝・龍樹菩薩造/鳩摩羅什訳＝非空海）・category:密教教学・出典:大智度論・
text_kakikudashi＝漢文原典 genten・gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
全段単独 motif（束ね無し）・文体は daichidoron palette{問答/譬喩/偈/列挙}内。新タグ値は原則0。

## 成果（判定表どおり・2段→2件・全段単独 motif・束ね無し）
- id：m4235-m4236／段：k029-k030／篇別内訳キー：daichidoron_孤立段〈経由引用〉三昧の定義・優婆塞五戒（巻第七/第十三・k029-k030）
- k029 三昧の定義（巻第七・十住心論→摩訶止観 経由・善心一処住不動是名三昧・三種三昧〈有覚有観/無覚有観/無覚無観〉・四種三昧〈欲界/色界/無色界/不繋〉・百千三昧遊戯出生・戯＝自在〈師子在鹿中自在無畏〉）m4235 核心〔主題:三昧/禅定・文体:問答/列挙〕
- k030 優婆塞五戒の五種（巻第十三・十住心論経由・四罪不作＝身善律儀/妄語不作＝口善律儀・一分行/少分行/多分行/満行/断婬の五種優婆塞）m4236〔主題:在家五戒/戒・文体:列挙〕
- 核心1：
  - m4235（k029）「善き心が一処に住して動かない、是れを三昧と名づく（善心一処住不動、是名三昧）」＝三昧定義の名句。空海が『秘密曼荼羅十住心論』第八住心（一道無為心）に摩訶止観経由で引く核心句（法話素材）。
- 新タグ値0（三昧/禅定/在家五戒/戒 全て既存値再利用）
- 裁定注（motif には影響なし・倉庫原則＝本文を verbatim 格納しタグを付けるのみ）：
  - k029：引用元は citation.kukai_work「秘密曼荼羅十住心論（摩訶止観 経由）」。摩訶止観の付加語「調直定」は大智度論本文にはない（本 genten には含まれない）。
  - k030：citation_type「内容対応（要注記）」。十住心論が「智度論云」として引く字句（戒有五種…若受一戒是名一分…五戒是名満分）は実は『大般涅槃経』巻第三十四の文で、大智度論 巻第十三の対応本文（一分行〜満行の五種優婆塞＝本 genten）を格納。出典:大智度論 のまま。

## stats 差分（期待値どおり）
- total_motifs 4265→4267／最終 id m4234→m4236／from_corpus_daichidoron 193→195
- kakikudashi_chars +454／gendaigoyaku_chars +852（改行除き）
- schema_history 310→311（origin: daichidoron_round15）
- motifs_without_gendai_gabun_intentional に daichidoron_round15_m4235-m4236=2 追記

## 検証
- engine（outputs/daichidoron_round_builder.py --verify）10項目＋巻き戻り assert（m506/anchor/大師0/典籍曰く）全 pass。
- ホスト側で total 4267・m4236・from_corpus 195・schema_history 311・篇別内訳キー・gabun エントリ・tags（m4235=三昧/禅定/問答/列挙/核心、m4236=在家五戒/戒/列挙）・genten verbatim 反映確認済。
- backup：outputs/motifs_backup_pre_daichidoron_round15.json。
- CLAUDE.md ★entry round15 挿入済（insert_claudemd_star.py・+2051bytes・行数 1395 不変・署名一意・NUL0）。

## 残ラウンド（R15 の後）——大智度論は本文・説話・孤立段まで消化、以後は特殊段のみ
- **k031＝genten 無しで motif 化不可・保留**（付録：言及・別称・典拠一覧。本文引用が無いため motif 化せず）。
- **通常ラウンドの対象段はこれで消化完了**（残は k031 の保留のみ）。
- 完走後：連動軸 retrofit（sg08←m4185・m4203・m4210 等の阿字/真言/畢竟空 候補、諸法実相/法性系 候補・handoff R11/R12 のリスト参照。今回の m4235 三昧定義は sg 成句/連動候補として要検討）・gabun 裁定・kaimyo-app 同期。

## 落とし穴（継続）
- **着手時に git ワークツリーへ phantom が残っていた**：staged 削除 D「引き継ぎメモ_2026-05-06_…idx48…檀像願文.md」（実体は存在）／phantom rename R「データ問い合わせガイド.md -> 空 path」／stale .git/index.lock。サンドボックス側から .git/index.lock は外せない（マウント不整合で mv も git restore も失敗）ため、Windows 側 cleanup_git_state_pre_round15.bat（index.lock 退避＋cleanup_git_state_pre_round15.py で staged D/R を unstage・実体ありでクリーン化・HEAD 欠落分のみ復元）をダブルクリックして整理する運用。push 前に必ず実行。
- CLAUDE.md は単一行巨大ファイル・Edit 不可→insert_claudemd_star.py 必須（entry「★ 」開始・「〕」終端・内部改行不可・冪等 sig=entry[:90]）。
- 長文は bash ヒアドキュメントで書き末尾検証。全角括弧のみ・割注〔 〕〈 〉。文書はホスト側 Read/Write/Edit。
- commit_push.bat は data/indices/・CLAUDE.md・*.md（handoff 含む）・_dev_references/ を staging。
  作業前からの M 2件（_dev_references/dainichikyo-sho-vol19/20_build/source.doc）が同梱され得る（既知・許容）。
  直下の未追跡 DST・ZoomInstallerFull.exe・_dev_scripts/・outputs/ は staging 対象外→push 前に git status 確認。
  Step 4.5 SAFETY CHECK（deleted: 検出で中止）は cleanup 実行後 deletion 無しで pass 見込み。
- 1リポジトリ1書き手。既存 motif・他 corpus に触れない（追記のみ）。

## push 手順（ケンシン）
1. `outputs\cleanup_git_state_pre_round15.bat` をダブルクリック → 最終 git status に「deleted:」「phantom renamed:」が無いことを確認。
2. `commit_push.bat` をダブルクリック → commit＋push。
3. 「pushした」の報告で、git log --oneline -3 と origin 反映を検証。

## 次セッション開始手順（完走後 retrofit 等）
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md（kakikudashi-data スキル同梱）を読む。
2. `git log --oneline -3` で HEAD＝R15 コミット・motifs.json 4267/m4236/195/311 を確認。
3. 通常ラウンドは消化済。以後は (a) 連動軸 retrofit（Phase A→B→C→D 様式・CLAUDE.md「retrofit セッション運用」節）、(b) gabun 要否裁定、(c) kaimyo-app 同期 のいずれか。k031 は genten 取得できれば別途。

## ケンシン貼付用テンプレ（次セッション・完走後 retrofit 例）
```
buddhist-data-api の大智度論（daichidoron.json）Phase3 は R15（k029/k030）で通常ラウンド消化完了。
次は完走後処理の連動軸 retrofit を開始してください（または gabun 裁定／kaimyo-app 同期）。
まず CLAUDE.md 冒頭と handoff_2026-07-02_daichidoron_motif_round15_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：HEAD＝R15 コミット・motifs.json total 4267・最終 m4236・from_corpus_daichidoron 195・schema_history 311。
連動軸候補：sg08 阿字本不生←m4185/m4203/m4210、諸法実相/法性系、三昧定義 m4235 の成句化 等（R11/R12 handoff のリスト参照）。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。git phantom は cleanup_git_state_pre_*.bat で整理。
k031 は genten 無しで保留。
```

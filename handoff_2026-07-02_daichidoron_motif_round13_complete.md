# 引き継ぎ：大智度論 Phase3 motif 抽出 第13ラウンド【完了】

日付：2026-07-02
状態：**R13 完了・motifs.json 書込済・検証全 pass・push 待ち**。
着手時 HEAD：a34068a（R12 完了コミット）。

## 経緯
- R12 handoff の「残ラウンド R13＝寶塔校量品＋述誠品＋如法性実際 k189-209（21段）」から着手。
- 着手前チェック（HEAD a34068a・total 4239・m4208・from_corpus 167・schema_history 308 一致・R12 push 済）
  → k189-209 の corpus 本文を読み判定表をケンシンに提示 → **承認**（核心3件＝k190/k204/k207）→ 書込実施。

## Phase A 合意（継続・全件適用）
引用形式:典籍曰く 全件（伝・龍樹菩薩造/鳩摩羅什訳＝非空海）・category:密教教学・出典:大智度論・
text_kakikudashi＝漢文原典 genten・gabun 意図的未設定・密教軸/典故軸/連動軸 非付与（完走後 retrofit）。
全段単独 motif（束ね無し）・文体は daichidoron palette{問答/譬喩/偈/列挙}内。

## 成果（判定表どおり・21段→21件・全段単独 motif・束ね無し）
- id：m4209-m4229／段：k189-k209／篇別内訳キー：daichidoron_寶塔校量・述誠・如法性実際（巻第五十七/第三十二・k189-k209）
- 寶塔校量品 k189-199（m4209-m4219）／述誠品 k200-201（m4220-m4221）／如法性実際 k202-209（m4222-m4229）
- 核心3：
  - m4210（k190）般若＝大明咒無上咒・三世諸仏是を学んで阿耨菩提を得（般若心経 大神咒大明咒無上咒の出典・空海が心経を大心真言三摩地法門と読む典拠）
  - m4224（k204）三は諸法実相の異名・三法印＝無常印無我印涅槃寂滅印
  - m4227（k207）法性＝涅槃性・一切世間法中皆涅槃性（黄石金性白石銀性の譬）
- 核心の代替候補（今回は非付与）：m4214（k194 一切種智ゆえに仏）・m4218（k198 一切諸仏の法印）・m4221（k201 般若常住不滅）・m4229（k209 諸法実相常住不動）
- 新タグ値 0（般若波羅蜜/功徳/煩悩/真言/畢竟空/供養/因果/一切種智/方便/二乗/中道/信解/三乗/諸法実相/三宝/常住/法性/空/実際/三法印/無常/十二因縁/涅槃 全て既存値再利用）

## stats 差分（期待値どおり）
- total_motifs 4239→4260／最終 id m4208→m4229／from_corpus_daichidoron 167→188
- kakikudashi_chars +5476／gendaigoyaku_chars +10687（改行除き）
- schema_history 308→309（origin: daichidoron_round13）

## 検証
- engine（outputs/daichidoron_round_builder.py --verify）10項目＋巻き戻り assert（m506/anchor/大師0/典籍曰く）全 pass。
- ホスト側 Grep で total 4260・m4229・schema_history 309・篇別内訳キー・CLAUDE.md ★entry round13 反映確認済。
- backup：outputs/motifs_backup_pre_daichidoron_round13.json。
- CLAUDE.md ★entry round13 挿入済（insert_claudemd_star.py・+5215bytes・行数 1395 不変・署名一意・NUL0）。

## 残ラウンド（R13 の後）
- **説話 k218-222（5段）＝小ラウンドまたは併合**。次はここが候補。
- 孤立段 k029/k030＝別途引用抜粋ラウンド。k031＝genten 無しで motif 化不可保留。
- 完走後：連動軸 retrofit（sg08←m4185・m4203・m4210 等の阿字/真言/畢竟空 候補、諸法実相/法性系 候補・handoff R11/R12 のリスト参照）・gabun 裁定・kaimyo-app 同期。

## 落とし穴（継続）
- CLAUDE.md は単一行巨大ファイル・Edit 不可→insert_claudemd_star.py 必須（entry「★ 」開始・「〕」終端・内部改行不可・冪等 sig=entry[:90]）。
- 長文は bash ヒアドキュメントで書き末尾検証。全角括弧のみ・割注〔 〕〈 〉。文書はホスト側 Read/Write/Edit。
- commit_push.bat は data/indices/・CLAUDE.md・*.md（handoff 含む）・_dev_references/ を staging。
  作業前からの M 2件（_dev_references/dainichikyo-sho-vol19/20_build/source.doc）が同梱され得る（既知・許容）。
  直下の未追跡 DST・ZoomInstallerFull.exe・_dev_scripts/・outputs/ は staging 対象外→push 前に git status 確認。
  Step 4.5 SAFETY CHECK（deleted: 検出で中止）は今回 deletion 無しで pass 見込み。
- 1リポジトリ1書き手。既存 motif・他 corpus に触れない（追記のみ）。

## 次セッション開始手順（R14＝説話 k218-222 等）
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md（kakikudashi-data スキル同梱）を読む。
2. `git log --oneline -3` で HEAD＝R13 コミット・motifs.json 4260/m4229/188/309 を確認。
3. k218-222 の corpus 本文を読み判定表を作成→提示→承認→plan_round14.json→engine dry-run→apply→verify→
   claudemd_entry_round14.txt→insert_claudemd_star.py --label round14→handoff/commit_message→push 依頼。

## ケンシン貼付用テンプレ（次セッション）
```
buddhist-data-api の大智度論（daichidoron.json）Phase3 motif 抽出 R14（説話 k218-222・5段）を開始してください。
まず CLAUDE.md 冒頭と handoff_2026-07-02_daichidoron_motif_round13_complete.md を読み、
references/motif-extraction.md（kakikudashi-data スキル同梱）に従うこと。
現状：HEAD＝R13 コミット・motifs.json は total 4260・最終 m4229・from_corpus_daichidoron=188・schema_history 309。
手順：k218-222 を読み判定表を私に提示→承認→plan_round14.json→daichidoron_round_builder.py dry-run→--apply→--verify→
claudemd_entry_round14.txt→insert_claudemd_star.py→handoff/commit_message 更新→git status 確認→push 依頼。
Phase A 合意継続（引用形式:典籍曰く 全件・gabun 未設定・連動軸 retrofit 後回し）。新タグ値は原則 0 で設計。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。commit_push.bat は _dev_references/ も staging・
直下の未追跡 DST/ZoomInstallerFull.exe/_dev_scripts/ は対象外→push 前に git status 確認。
孤立段 k029/k030 は引用抜粋ラウンド・k031 は genten 無しで保留。完走後に連動軸 retrofit・gabun 裁定・kaimyo-app 同期。
```

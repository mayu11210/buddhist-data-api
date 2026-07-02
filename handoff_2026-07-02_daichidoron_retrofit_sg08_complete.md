# 引き継ぎ：大智度論 Phase3 完走後 連動軸 retrofit 第一弾（sg08 阿字本不生）【完了】

日付：2026-07-02
状態：**完了・motifs.json 書込済・整合性検証 全 pass・push 待ち**。
着手時 HEAD：ae25886（R15 完了コミット）。
種別：**連動軸 retrofit（retrofit 7／大日経疏 vol13-20 型＝新規 sg/anchor なし・既存軸被覆拡張・タグのみ変更）**。

## 冒頭サマリ（Phase D 必須チェック）
- [x] motifs.json 反映完了（6 項目整合性検証 全 pass）
- [x] schema_history 追記済（311→312・origin retrofit:daichidoron_rendou_scan）
- [x] motifs_index_design.md 補注 DDD 追加済
- [x] 本体 CLAUDE.md 更新済（★entry・insert_claudemd_star.py・+1556bytes・行数1395不変）
- [x] **commit_message.txt 書き換え済（本 retrofit 用・冒頭行整合）**
- [x] handoff_*.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 全角括弧バランス確認（（）14/14・〔〕1/1・〈〉1/1）
- [x] サイズ差分想定内（motifs.json +1373bytes・タグ8件分）

## 経緯
- R15 handoff「完走後：連動軸 retrofit（sg08←m4185…）」から着手。着手前チェックで HEAD=ae25886・total 4267・最終 m4236・from_corpus_daichidoron 195・schema_history 311・schema_version 0.2 が handoff と一致（並行セッション無し）を確認。
- **原則11（ラベルより内容を信頼）による報告**：R15 handoff／ケンシン貼付テンプレは sg08 阿字本不生・sg09 諸法実相を「新設」候補のように記していたが、**実体では sg08・sg09 とも既存**（sg08 anchor=m549・既に 79 members／sg09 anchor=m637・4 members）。よって本作業は retrofit 7 型（新規 sg-id 無し・既存軸へ連動タグ付与）と確定。また貼付テンプレの「m4210」は sg08 に不適合（本文＝深般若受持で毒藥火坑に傷つかず・主題:般若波羅蜜/真言・阿字本不生と無関係＝誤記）と判定。

## Phase A 裁定（ケンシン）
- 対象軸＝**sg08 のみ（字門群）**。sg09 諸法実相（Q2＝全 28 件）・m4235 三昧定義 成句化 sg32（見送り）は次セッション以降へ繰延。

## Phase B 判定表（ケンシン承認：付与セット＝m4185・m4186・m4188・m4189 の 4 件）
| id | 段 | 本文の核 | 連動度 | 判定 |
|---|---|---|---|---|
| m4185 | k165 | 【經】「阿字門、一切法初不生故」＝四十二字門の首・阿字本不生の locus classicus（主題:字門/阿字/本不生・核心） | ◎ | 付与 ★中核 |
| m4186 | k166 | 【經】字門列挙の続き（簸・䭾・賒…諸法不可得）＝同一の四十二字門一連 | ○ | 付与 |
| m4188 | k168 | 【論】釋曰・字等語等＝畢竟空涅槃と同等・四十二字は一切字の根本〈初阿後荼〉 | ◎ | 付与 |
| m4189 | k169 | 【論】破散諸字→言語空→畢竟空＝般若・破竹の譬 | ○ | 付与 |
| m4187 | k167 | 【經】阿字印の二十功徳＝阿字印は明示だが内容は功徳列挙 | △ | **除外** |
| m4203 | k183 | 摩訶衍総枠の長列挙中「字等語等諸字入門」は付随言及・字門は第4主題 | ✕ | **除外** |
- 除外理由は「功徳列挙／付随言及＝直接連動未満」（`経証〔経文引用＋問題提起〕除外先例` m698/m712/m632/m635 とは別類型）。

## 成果（連動タグ +8）
- 対象 4 motif に `連動:sg08`＋`連動:m549` を末尾追記（既存 members 書式に一致）。
- sg08 阿字本不生 連動 members：79 → **83**。

## stats 差分（タグのみ変更＝本体数値は全て不変）
- total_motifs 4267 不変／最終 id m4236 不変／from_corpus_daichidoron 195 不変。
- kakikudashi_chars／gendaigoyaku_chars／famous_phrases（31）不変。
- schema_history 311→312（origin: retrofit:daichidoron_rendou_scan）。

## 検証
- ホスト側再検証で 6 項目全 pass：NUL0・JSON 再パース OK・total==配列数(4267)・m-id 連番(missing/dup 無・sg 31 件)・必須フィールド完全・schema_version 0.2/schema_history 312。
- recompute drift 0（kk/gd/from_corpus_daichidoron 全ゼロ）。
- 巻き戻り assert 全 pass：m506=引用形式:典籍曰く／anchor m549 自己参照タグ（連動:sg08・連動:m549）温存／大智度論 大師0／対象 4 件の元タグ温存・除外 2 件（m4187/m4203）に連動タグ無し。
- backup：outputs/motifs_backup_pre_daichidoron_retrofit_sg08.json。
- build script：outputs/retrofit_daichidoron_sg08_builder.py（dry-run→--apply）。

## 落とし穴（継続）
- CLAUDE.md は単一行巨大ファイル・Edit 不可 → insert_claudemd_star.py 必須（★開始・〕終端・内部改行不可・冪等 sig=entry[:90]）。今回 +1556bytes・行数1395不変。
- 長文編集は bash ヒアドキュメント／Python in-memory 編集＋write back。Edit tool で JSON 直接編集はしない。文書はホスト側 Read/Write/Edit。
- git ワークツリー phantom（staged D／phantom rename R／stale index.lock）はサンドボックスから外せない → Windows 側 cleanup_git_state_pre_*.bat をダブルクリックで整理。push 前に必ず実行。commit_push.bat の Step 4.5 SAFETY CHECK（deleted 検出で中止）は cleanup 後 pass 見込み。
- commit_push.bat は data/indices/・CLAUDE.md・*.md（handoff 含む）・_dev_references/ を staging。直下の未追跡や outputs/・_dev_scripts/ は対象外 → push 前に git status 確認。
- 1 リポジトリ 1 書き手。既存 motif・他 corpus に触れない（本 retrofit は既存 4 motif へのタグ追記のみ）。

## push 手順（ケンシン）
1. 必要なら `outputs\cleanup_git_state_pre_*.bat` 相当で git 状態を整理し、`git status` に「deleted:」「phantom renamed:」が無いことを確認。
2. `commit_push.bat` をダブルクリック → commit＋push。冒頭行「大智度論 Phase3 完走後 連動軸 retrofit 第一弾（sg08…）」が作業内容と整合していることを Step 5 で目視確認。
3. 「pushした」の報告で、`git log --oneline -3` と origin 反映、`--stat`（data/indices/motifs.json・CLAUDE.md・motifs_index_design.md・本 handoff）を検証。

## 次セッション開始手順（次の連動軸 retrofit 等）
1. リポジトリ CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md（kakikudashi-data スキル同梱）＋CLAUDE.md「retrofit セッション運用」節を読む。
2. `git log --oneline -3` で HEAD＝本 retrofit コミット・motifs.json total 4267／最終 m4236／from_corpus_daichidoron 195／schema_history 312／sg08 members 83 を確認。
3. 次候補：
   - (a) **sg09 諸法実相 retrofit**（anchor m637・大智度論候補 28 件＝m4042/m4048/m4058/m4059/m4066/m4067/m4070/m4072/m4073/m4080/m4086/m4095/m4130/m4136/m4137/m4140/m4162/m4166/m4176/m4177/m4181/m4202/m4218/m4222/m4223/m4224/m4225/m4226/m4227/m4228/m4229）。**ケンシン Q2 裁定＝全 28 件**。ただし sg09 は「強連動」原則との兼ね合いで Phase B 判定表を再提示し経証・付随言及を除外裁定するのが安全（現状 sg09 members わずか 4 件のため被覆過多に注意）。
   - (b) m4235 三昧定義「善心一処住不動、是名三昧」の成句化（sg32 新設）。今回見送り＝軸設計合意（Phase A）から。
   - (c) gabun 要否裁定（大智度論＝伝 龍樹造/鳩摩羅什訳・非空海・経典引用系ゆえ意図的未設定見込み・補注 II/MM/QQ 基準）。
   - (d) kaimyo-app 同期（data/indices/motifs.json コピー＋NUL0/total/引用形式タグ反映確認。新引用形式タグ導入なしのため冠生成ロジック改修は不要見込み）。
   - k031 は genten 取得できれば別途 motif 化。

## ケンシン貼付用テンプレ（次セッション・sg09 諸法実相 retrofit 例）
```
buddhist-data-api の大智度論（daichidoron.json）は sg08 阿字本不生 連動 retrofit（字門群 4 件）まで完了。
次は連動軸 retrofit 第二弾＝sg09 諸法実相（anchor m637）への大智度論 諸法実相/法性/実際 群の連動を開始してください。
まず CLAUDE.md 冒頭と handoff_2026-07-02_daichidoron_retrofit_sg08_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。
現状：HEAD＝sg08 retrofit コミット・motifs.json total 4267・最終 m4236・from_corpus_daichidoron 195・schema_history 312・sg08 members 83。
sg09 候補は大智度論 28 件（Q2 裁定＝全 28 件）。Phase B 判定表で経証/付随言及の除外を再確認のうえ付与。
落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。git phantom は cleanup_git_state_pre_*.bat で整理。
m4235 三昧定義 成句化 sg32 は見送り継続。k031 は genten 無しで保留。
```

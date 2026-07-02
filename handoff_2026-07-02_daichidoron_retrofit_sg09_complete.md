# handoff: 大智度論 連動軸 retrofit 第二弾（sg09 諸法実相）完了

**状態**：完了・motifs.json 書込済・整合性検証 全 pass・**push 待ち**
**着手時 HEAD**：394f9fe（sg08 retrofit 第一弾）
**種別**：連動軸 retrofit（retrofit 7 型＝新規 sg/anchor なし・既存軸被覆拡張・タグのみ変更）

## Phase D 完了チェックリスト（commit_push.bat 実行前）

- [x] motifs.json 反映完了【整合性検証 8 項目＋巻き戻り assert 全 pass】
- [x] schema_history 追記済（312→313・origin: retrofit:daichidoron_rendou_scan）
- [x] motifs_index_design.md に補注 EEE 追加済
- [x] 本体 CLAUDE.md 更新済【タイトル行 ★entry・insert_claudemd_star.py・+1221bytes・行数1395不変】
- [x] **commit_message.txt 書き換え済【当該 retrofit 用・冒頭行整合】**
- [x] handoff_2026-07-02_daichidoron_retrofit_sg09_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 新規タグに半角括弧 0
- [x] サイズ差分が想定範囲内（motifs.json タグのみ・補注 EEE +29行・CLAUDE.md +1221bytes）

## Phase A（sg08 セッションで確定済・踏襲）

大智度論＝伝 龍樹菩薩造/鳩摩羅什訳＝**非空海**。引用形式:典籍曰く 系。連動軸 retrofit は
完走後スキャンで既存 anchor へ被覆拡張（新規 sg-id は立てない）。強連動原則・被覆過多回避。

## Phase B 判定表（ケンシン裁定＝付与25/除外6）

**重要・不一致解消**：sg08 handoff の sg09 候補は本文ラベルで「全 28 件」と 3 箇所に記すが、
**実際に列挙された m-id は 31 件**（差 3）。原則11（ラベルより内容を信頼）により全 31 件の本文を
精査し判定表をケンシンに提示、**付与25/除外6** に裁定確定。

### 付与 25 件（連動:sg09＋連動:m637）

諸法実相・法性・実際を教学的中核とする motif：

| id | 核心 |
|---|---|
| m4042 | 諸法相偈〈不生不滅…〉→深入諸法実相・無生忍 |
| m4048 | 般若＝諸法実相・十八空との異一 |
| m4058 | 第一義空＝諸法実相亦空 |
| m4059 | 有為法実相即是無為 |
| m4067 | 一切法空・入諸法実相則無所覚知 |
| m4072 | 如焰・近聖法則知諸法実相 |
| m4073 | 如水中月・実法相在如法性実際 |
| m4080 | 如化・如法性如如如真際 |
| m4095 | 諸法実相是般若波羅蜜（定義） |
| m4136 | 二諦仮名・如法性実際＝仮名の実相 |
| m4137 | 不壊仮名而説諸法実相 |
| m4140 | 諸法実相本自清浄・実相異名列挙 |
| m4162 | 第一義悉檀＝諸法実相 |
| m4166 | 三解脱門縁諸法実相・涅槃城 |
| m4176 | 菩薩云何得諸法実相・入海喩 |
| m4177 | 諸法実相の定義・讃般若偈 |
| m4181 | 諸法一相所謂無相・実相是般若 |
| m4222 | 【經論】如法性実際・実相＝如 |
| m4223 | 法性・実際の定義 |
| m4224 | 如法性実際＝諸法実相異名・三法印 |
| m4225 | 三法印と諸法実相・善入法性是実際 |
| m4226 | 如法性実際・声聞/摩訶衍 |
| m4227 | 入無量法性中・法性論 |
| m4228 | 九種法・三如〈下中上如〉 |
| m4229 | 諸法実相常住不動・法性清浄・実際 |

### 除外 6 件（強連動未満・温存）

| id | 核心テーマ | 除外理由 |
|---|---|---|
| m4066 | 一切法空（相分析） | 諸法実相語ゼロ・空義であり実相中核でない |
| m4070 | 十喩【經】列挙＋【論】解空序 | 実相語ゼロ・経文引用＋問題提起で経証寄り。実喩本体は m4072-m4080 |
| m4086 | 慈三縁・大悲是般若母 | 実相は無縁慈説明中の付随言及 |
| m4130 | 七覚分 | 諸法実相語ゼロ・實法相の一言のみ |
| m4202 | 本願大悲・七住地 | 実相は不取涅槃の四因の一の付随言及 |
| m4218 | 般若供養校量・宝塔福徳 | 諸法実相語ゼロ・福徳校量が核心 |

## 成果・stats 差分（タグのみ変更）

- 連動タグ +50（25 件 × 連動:sg09＋連動:m637）
- **sg09 諸法実相 連動 members：4 → 29**（既存 m152/m338/m637/m639 ＋ 大智度論 25 件）
- total_motifs **4267 不変**／最終 id **m4236 不変**／from_corpus_daichidoron **195 不変**
- kakikudashi/gendaigoyaku 字数・famous_phrases 31：**不変**
- schema_history **312 → 313**（origin: retrofit:daichidoron_rendou_scan）
- sg08 連動 members **83 不変**

## 検証（全 pass）

**整合性 8 項目**：NUL0／JSON reparse OK／total==array 4267／m-id 連番（m1-m4236 missing/dup なし・sg=31）／
必須フィールド完全／新規タグ半角括弧 0／recompute drift 0（kk/gd/from_corpus）／schema_version 0.2 維持・history +1。
**追加**：本文 verbatim（対象25件 body＝backup と一致）／ホスト側 Grep で反映確認（total 4267・補注 EEE・CLAUDE.md 署名）。
**巻き戻り検知 assert**：m506 典籍曰く／sg08 anchor m549 自己参照（連動:sg08＋連動:m549）／sg08 members 83／
sg09 anchor m637 自己参照（連動:sg09＋連動:m637）／除外 6 件 非付与／tag-changed motif ちょうど 25 件（＝付与集合と一致）。

**backup**：`outputs/motifs_backup_pre_daichidoron_retrofit_sg09.json`
**build script**：`outputs/retrofit_daichidoron_sg09_builder.py`（dry-run→--apply・全 assert 内蔵）

## 落とし穴（継続）

- CLAUDE.md は巨大単一行で Edit 不可 → **insert_claudemd_star.py** 必須（★開始・〕終端・冪等・行数不変）。今回 +1221bytes・行数1395不変。
- 長文編集は Python in-memory＋write back / bash heredoc のみ。Edit ツールで motifs.json を直接編集しない。文書はホスト側 Read/Write/Edit。
- git phantom（staged D／幻影 rename R／stale index.lock）はサンドボックスから脱出不可 → Windows の `cleanup_git_state_pre_*.bat` をダブルクリックで整理してから push。
- commit_push.bat は data/indices/・CLAUDE.md・*.md（handoff 含む）・_dev_references/ のみ stage。push 前に `git status` で「deleted:」「phantom renamed:」が無いこと確認。
- 1 リポジトリ 1 書き手（本 retrofit＝既存 25 件へのタグ追記のみ）。

## push 手順（ケンシン）

1. 必要なら `outputs\cleanup_git_state_pre_*.bat` 相当を実行し `git status` に「deleted:」「phantom renamed:」が無いことを確認。
2. `commit_push.bat` をダブルクリック → commit+push。冒頭行「大智度論 Phase3 完走後 連動軸 retrofit 第二弾（sg09 諸法実相…）」が作業内容と整合（Step5 目視確認）。
3. 「push した」報告後、`git log --oneline -3`・origin 反映・`--stat`（data/indices/motifs.json・CLAUDE.md・motifs_index_design.md・本 handoff）を検証。

## 次セッション開始手順

1. 読む：CLAUDE.md 冒頭＋本 handoff＋references/motif-extraction.md＋CLAUDE.md「retrofit セッション運用」節。
2. `git log --oneline -3` で HEAD＝本 retrofit コミットを確認。motifs.json total 4267／最終 m4236／from_corpus_daichidoron 195／schema_history 313／sg08 members 83／**sg09 members 29**。
3. 次候補：
   - (a) **m4235 三昧定義「善心一処住不動、是名三昧」の成句化**（sg32 新設）— 見送り継続中。着手ならケンシン軸設計合意（Phase A）から。
   - (b) 大智度論 gabun（雅文体訳）要否裁定 — 非空海・引用形式:典籍曰く 系ゆえ意図的未設定が予想（補注 CCC 等の運用に準拠）。
   - (c) kaimyo-app への motifs.json 同期（単純コピー＋NUL0／total 4267／引用形式タグ反映確認。新引用形式タグ導入なしのため冠生成ロジック改修は不要見込み）。
   - (d) 他の既存 anchor への大智度論 連動 retrofit 追加検討（今回 sg09 で諸法実相群は被覆。残 195-25-4字門=約 166 件のうち強連動候補があれば）。
   - k031 は genten 無しで保留。

## ケンシン貼付用テンプレ（次セッション例・sg32 成句化 または gabun 裁定）

```
buddhist-data-api の大智度論（daichidoron.json）は sg09 諸法実相 連動 retrofit（諸法実相/法性/実際 群 25件→+50タグ）まで完了・push 済。
次は〔m4235 三昧定義「善心一処住不動、是名三昧」の成句化 sg32 新設／大智度論 gabun 要否裁定／kaimyo-app 同期〕のいずれかを進めてください。

まず CLAUDE.md 冒頭と handoff_2026-07-02_daichidoron_retrofit_sg09_complete.md、
references/motif-extraction.md と CLAUDE.md「retrofit セッション運用」節を読むこと。

現状：HEAD＝sg09 retrofit コミット・motifs.json total 4267・最終 m4236・from_corpus_daichidoron 195・schema_history 313・sg08 members 83・sg09 members 29。

落とし穴：CLAUDE.md は Edit 不可→insert_claudemd_star.py。git phantom は cleanup_git_state_pre_*.bat で整理。
k031 は genten 無しで保留。
```

# 引き継ぎメモ 2026-06-10 retrofit 29 完走（菩提心論 引用形式是正）

**日付**：2026-06-10
**種別**：retrofit（タグ是正・本体直接書込）
**起点 HEAD**：`71c607a`（秘蔵記 motif 第 2 ラウンド）
**ステータス**：作業完了・整合性検証 8 項目全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）

---

## 是正内容（ケンシン裁定 2026-06-10・retrofit 29 番号充当）

菩提心論（龍猛菩薩造・不空訳）の 4 motif に誤付与されていた `引用形式:大師曰く` を
`引用形式:典籍曰く` に置換。m516/m519 は `category:大師御言葉` も除去（−2 タグ）。

| id | 節 | 内容 | 操作 |
|---|---|---|---|
| m506 | 第一節 | 善悪標心・発菩提心総説（sg22 本文系 anchor） | 大師曰く→典籍曰く |
| m516 | 第四節 | 我れ自心を見るに形は月輪の如し | 同上＋大師御言葉 除去 |
| m519 | 第四節 | 凡人の心は合蓮華・仏の心は満月 | 同上＋大師御言葉 除去 |
| m520 | 第五節 | 父母所生の身に速やかに大覚位を証す | 大師曰く→典籍曰く |

- 背景：kaimyo-app の「弘法大師のたまわく、」冠生成が龍猛菩薩の言葉の誤引用となるため。
  三教指帰 retrofit 4 に続く引用事故防止設計の第二例（発言主体弁別→著者帰属弁別）。
- 事前スキャンで誤付与は菩提心論 4 件のみと確認（大日経疏〔一行記〕等への誤付与ゼロ・
  成句 sg03/sg17-sg20/sg23/sg24 の 大師曰く 7 件は全て空海著作由来で正当）。
- 連動軸タグ（連動:sg22／連動:m506／連動:m581 等）は全件 verbatim 温存。
- m520 と sg03（即身成仏義）の同句異所属弁別は補注 CC 参照。
- total_motifs 2326 不変・schema 0.2 維持・schema_history 152 件
  （+1・origin: retrofit_29:attribution_fix）。
- 補注 CC を motifs_index_design.md §2 末尾（補注 BB の次・§3 の前）に追加。
- 実装：outputs/retrofit29_bodaishinron_inyou.py（dry-run＋--apply 二段運用）
- バックアップ：outputs/motifs_backup_pre_retrofit29.json

## Phase D 必須チェックリスト

- [x] motifs.json 反映完了（整合性検証 8 項目全 pass）
- [x] schema_history 追記済（152 件）
- [x] motifs_index_design.md に補注 CC 追加済
- [x] 本体 CLAUDE.md 更新済（タイトル行・進捗ヘッダ・ホスト側 Edit）
- [x] commit_message.txt 書き換え済（retrofit 29 用・冒頭行整合）
- [x] handoff_*.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] サイズ差分が想定範囲内（motifs.json 5,416,743→5,417,543 bytes・+800）

## 残課題

1. **kaimyo-app 側：引用形式:典籍曰く の冠生成ロジック未実装**（最重要・別セッション）。
   - 「〔典籍名〕に曰く、」型（source.著作名 から生成）
   - 「〔著者〕、〔典籍名〕に曰く、」合成型（秘蔵記は source.著者、既存著作は
     corpus manifest の著者情報から解決）
   - 対象：本是正 4 件（m506/m516/m519/m520・菩提心論）＋秘蔵記 25 件（m2275-m2299）
   - 併せて kaimyo-app 側で 引用形式:大師曰く の生成ロジックが「出典タグ＝菩提心論」を
     大師曰く扱いしていないか（タグ駆動でなく出典駆動の実装になっていないか）の点検を推奨
2. 秘蔵記 motif 第 3 ラウンド以降（k047-k129・R3〜R6）→ 完走後 **retrofit 30**
   （秘蔵記 連動軸スキャン・番号繰り下げ済み）＋ gabun 付与の要否裁定
3. description 等の「sg01〜sg26」旧表記（実際は sg27 まで 27 件）は温存中（小是正候補）

## 次セッション開始時の流れ

1. CLAUDE.md → 本メモ → `git log --oneline -3`
2. motifs.json の total_motifs=2326・m506 に 引用形式:典籍曰く を確認
3. 最優先候補：(α) kaimyo-app セッションで典籍曰く対応／(β) 秘蔵記 R3（k047-k064 字義・言語論）

## 新セッション開始用メッセージ（ケンシン貼付テンプレ・buddhist-data-api 続行の場合）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- 秘蔵記 motif R2 完走（k021-k046 → m2283-m2299・total_motifs 2326）
- retrofit 29 完走（菩提心論 4 件 大師曰く→典籍曰く 是正・大師御言葉 2 件除去）
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-10_retrofit29_complete.md
## 確認
git log --oneline -3・motifs.json total_motifs=2326・m506 が 引用形式:典籍曰く
## 次の作業
秘蔵記 第 3 ラウンド：字義・言語論（k047-k064）の motif 抽出
（kaimyo-app 側の 典籍曰く 冠生成対応は kaimyo-app セッションで別途）
## 注意点
- マウント同期不具合が継続中。CLAUDE.md 等の編集はホスト側ツール（Edit/Write）で。
- 連動軸スキャンは retrofit 30 に繰り下げ済み。
進める前に、最優先タスクを確認してください。
```

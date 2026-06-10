# 引き継ぎメモ 2026-06-11 retrofit 31 完走（stale メタデータ一括是正・motif 本体不変）

**日付**：2026-06-11
**種別**：整合性保守型 retrofit（retrofit 9 anchor 自己参照補完・retrofit 29 引用形式是正に続く第三例・メタデータのみの変更は初例・新規 sg-id なし）
**起点 HEAD**：`473e590`（retrofit 30・push 済を本セッション着手前に確認）
**ステータス**：作業完了・整合性検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**commit_message.txt 更新確認**：✅ 本 retrofit 用に書き換え済（冒頭行整合）

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了（メタデータのみ・motif 本体 verbatim 不変・total_motifs 2391 不変）
- [x] schema_history 追記済（origin: retrofit_31:stale_metadata_fix・158 件）
- [x] motifs_index_design.md に補注 EE 追加済（346,378→349,508 bytes・半角括弧 0）
- [x] 本体 CLAUDE.md 更新済（タイトル行・進捗ヘッダ・ホスト側 Edit で実施）
- [x] commit_message.txt 書き換え済（ホスト側 Write・冒頭行整合確認済）
- [x] handoff_2026-06-11_retrofit31_complete.md 作成済（本ファイル・ホスト側 Write）
- [x] NUL バイト 0 件・JSON 再パース確認
- [x] stats recompute 差分全ゼロ確認（メタデータのみのため当然だが実測確認）
- [x] 正準形式 indent=1・末尾改行なしで書込（適用前 round-trip assert pass）

---

## Phase A 合意事項（ケンシン裁定 2026-06-11）

1. **handoff 指定 3 件＋description 現況化を是正**（最優先タスク (A) 採用）
2. **stats.description は温存**（2026-05-25 W1 マージの日付付きナラティブ・
   履歴記述として schema_history と同扱い）
3. **jujushinron_m2175-m2274 エントリを補完する**（被覆漏れの解消）

## 本 retrofit の成果（是正 4 件）

| # | 箇所 | 旧 | 新 |
|---|---|---|---|
| 1 | top-level description | 2200 motifs＝m01〜m2174＋成句 sg01〜sg26（2026-05-25 時点） | 2391 motifs＝m1〜m2364＋成句 sg01〜sg27・秘蔵記完了・retrofit 30 反映・連動軸二十三系統並立 |
| 2 | stats.篇別内訳 | 「成句_七件」（sg01〜sg07・件数 7） | 「成句_二十七件」（sg01〜sg27・件数 27・キー位置保持） |
| 3 | intentional 辞書キー | 「sg01-sg07」 | 「sg01-sg27」（値温存・キー位置保持） |
| 4 | intentional 辞書 | jujushinron エントリなし（被覆漏れ） | 「jujushinron_m2175-m2274」補完 → 被覆 218/218 完全 |

- gabun 意図的未設定の実測：218 件＝m06（1）＋成句 sg01〜sg27（27）＋
  十住心論 m2175-m2274（100）＋秘蔵記 m2275-m2364（90）
- 温存：stats.description・schema_history 内旧表記（sg01〜sg06 等・1 件確認）
- motifs.json 5,561,979→5,563,757 bytes（+1,778）・generated_at 2026-06-11 に更新
- 補注 EE：現況系フィールド（description・篇別内訳・intentional・famous_phrases）と
  履歴系フィールド（schema_history・stats.description）の弁別原則を明文化。
  今後の拡張時は現況系の同期更新を Phase C チェック項目として意識する
- 実装：outputs/retrofit31_stale_metadata_fix.py（dry-run＋apply 二段運用・
  適用前 assert に m506 典籍曰く＋m2362 連動:sg20＋indent=1 round-trip を装備）
- バックアップ：outputs/motifs_backup_pre_retrofit31.json

## 副次発見・要注意事項

1. **本セッション冒頭に PC が再起動**したが影響ゼロ（retrofit 30 は push 済だった）。
   再起動後にマウント同期の phantom 差分（CLAUDE.md の M 表示・実体はホスト側正常）も
   解消された。マウント stale が疑わしいときは再起動が有効な可能性。
2. 着手時検証：HEAD 473e590・total_motifs 2391・m2362 連動:sg20・m506 典籍曰く・
   全 pass（巻き戻りなし）。
3. motifs.json 正準形式は indent=1・末尾改行なし（retrofit 30 知見を継承・
   本スクリプトの適用前 assert で機械的に検知）。
4. CLAUDE.md は行数 1394 だが 1 行が最大 8 万字級のため Read tool の全文読みは不可。
   タイトル行・進捗ヘッダの更新は短い unique 文字列での Edit が有効だった。

## 残作業（次セッション以降の選択肢）

- **kaimyo-app 側**：引用形式:典籍曰く 冠生成ロジック未実装（retrofit 29 残課題）・
  motifs.json 同期（秘蔵記 90 motif＋retrofit 30 連動タグ＋本 retrofit メタデータ反映）
- 新規 corpus の Phase 1〜3（次の書き下し素材があれば kakikudashi-data スキルの全工程）
- 秘蔵記・十住心論 gabun の将来 retrofit（意図的未設定の温存継続案件）

## 次セッション開始時の流れ

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2391・description に「2391 motifs」・
   成句_二十七件・sg01-sg27・jujushinron_m2175-m2274・m506 典籍曰く を確認
3. 残作業から最優先をケンシンに確認

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- retrofit 31 完走（stale メタデータ一括是正・description 現況化・
  成句_二十七件・sg01-sg27・jujushinron_m2175-m2274 補完・
  motif 本体／タグ／total_motifs 2391 不変・補注 EE）
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-11_retrofit31_complete.md
## 確認
git log --oneline -3 で HEAD 確認・motifs.json total_motifs=2391・
description に「2391 motifs＝m1〜m2364＋成句 sg01〜sg27」・
m506 に 引用形式:典籍曰く（巻き戻り検知）
## 次の作業候補
(A) kaimyo-app 側（典籍曰く冠生成・motifs.json 同期）
(B) 新規 corpus Phase 1（素材があれば）
(C) 秘蔵記・十住心論 gabun retrofit（温存継続案件）
## 注意点
- motifs.json の正準形式は indent=1・末尾改行なし（round-trip assert に注意）
- マウント同期不具合継続前提。CLAUDE.md・commit_message.txt・handoff は
  必ずホスト側ツール（Edit/Write）で編集すること
- スクリプトの適用前 assert に m506 典籍曰く チェックを継承すること
進める前に、最優先タスクを確認してください。
```

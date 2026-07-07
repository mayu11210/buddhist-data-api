# handoff: 説話タグ軸すり合わせ v1 完了

**日付**：2026-07-07
**着手時 HEAD**：倉庫 e6d158a／kaimyo-app 7bee107（いずれも push 済確認済）
**種別**：新規参照ドキュメント追加（倉庫）＋ picker 再構築（kaimyo-app）。既存 data/index/corpus 不変
**方針裁定**：ケンシン「B：16軸を統制化＋crosswalk」（2026-07-07）

## 経緯

handoff_2026-07-05 残タスク (b)「説話タグ軸と motifs.json 軸体系の正式すり合わせ」。
調査で判明した要点：motifs.json の意味軸のうち `主題` は自由記述（2907値）で、
setsuwa の99タグを1:1で移せる統制テーマ軸が motifs 側に存在しない。よって機械的
リマップは不可能。B案＝setsuwa 独自の正準テーマ軸を統制語彙として確立し、motifs へは
参照 crosswalk のみ付与（マージなし・別系統資産）を採用。

## 成果物

### buddhist-data-api（新規1）
- **_dev_references/setsuwa_tag_axes_v1.md**：
  - 正準テーマ軸20軸（A01〜A20）・99タグを排他割当（被覆99/99・重複0・幽霊0）
  - motifs crosswalk 表（各軸→主題/感情調/含意の射程/故人/人生像・参照のみ）
  - タグ→軸 全割当一覧・picker 反映内容・回帰結果・運用メモ・次工程
  - v1 前身 setsuwa_catalog_v1.md（16軸）を20軸へ拡張（A17仏性本来性／A18導き方便回復／
    A19立ち直り改心／A20今を生きる実践 を新設）

### kaimyo-app（変更1）
- **lib/setsuwa-picker.ts**：SETSUWA_AXES（20軸）をエクスポート追加＋
  SETSUWA_THEME_KEYWORDS を統制語彙で再構築。ロジック（pickSetsuwa 等）は不変。
  gap キーワードで全99タグ到達可能化。

## 検証

- 20軸で全99タグを過不足なく被覆（重複0・漏れ0・幽霊0）
- 旧辞書 vs 新辞書・代表入力70件バッテリー：gap 除外時 上位2話 45/45 完全一致／
  gap 込みでも上位1話 70/70 完全一致（差分は2番手のみ5件）。picker は最大1話織り込みゆえ実質不変
- 文書化4テーマ top pick（s002/s022/s008/s021）再現・空テーマ非選定
- 旧辞書で到達不能だった6タグ（休息・再生・回復・広い視野・改心・目に見えぬ支え）を到達可能化
- ハーネス：outputs/setsuwa_axis_harness.py（旧新辞書の完全写し＋pickSetsuwa 再現＋バッテリー）

## コミット状況（重要・次セッション注意）

- **倉庫**：setsuwa_tag_axes_v1.md は d728204 として push 済。ただし commit_push.bat が
  commit_message.txt（push4 の内容のまま）を流用したため、**d728204 のメッセージは
  「push4_sync_setsuwa.bat 新設」と齟齬**（内容＝.md 追加のみで安全）。本 handoff コミット
  時に commit_message.txt を本作業内容へ更新済。
- **kaimyo-app**：picker 変更は commit_setsuwa_sync.bat で別途コミット要
  （commit_message_setsuwa_sync.txt を本作業内容へ更新済・whitelist に lib/setsuwa-picker.ts 含む）。
- **CLAUDE.md ★entry**：本セッションでは未追記（handoff＋spec doc で継続性を担保）。
  必要なら次セッションで line1 へ bash-python 挿入（backup+assert・handoff_2026-07-05 方式）。

## 落とし穴メモ

- sandbox 側のファイル末尾 truncate/stale 表示は既知 phantom（ホスト側は正常）。
  picker は sandbox で13408バイトに見えるが、ホスト Read は全文（SETSUWA_AXES 込み）で健全。
- picker の tsc は sandbox 不可（EOF 誤検出）。ホスト側 `tsc --noEmit -p tsconfig.json` で確認。
- source.doc 2件（vol19/vol20_build）の M 表示は既知 phantom。
- kaimyo-app の stale .git\index.lock は commit bat が自動削除。
- 倉庫 commit_push.bat SAFETY CHECK が「deleted:」で停止時は handoff_2026-07-05 の
  stale staged rename 対処（git restore --staged）を参照。

## 次にやること

1. kaimyo-app で commit_setsuwa_sync.bat 実行（picker を commit+push）
2. 倉庫で commit_push.bat 実行（本 handoff＋更新済 commit_message.txt を commit）
3. handoff_2026-07-05 残タスク：(c) 説話拡充（忍耐・慈悲系異伝・大智度論 k218-222 相互参照）／
   (d) 新著作取込（Phase 1〜）。(c) 拡充時は新タグを20軸へ割当し被覆100%維持、
   収まらぬ新テーマのみ軸追加で仕様書を v2 に更新。

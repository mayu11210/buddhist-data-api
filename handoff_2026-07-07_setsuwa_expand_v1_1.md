# handoff: 説話ライブラリ v1.1（拡充＋大智度論 相互参照）

**日付**：2026-07-07（タグ軸すり合わせ v1＝bd8b48a の後続）
**着手時 HEAD**：倉庫 bd8b48a／kaimyo-app 695b33b
**種別**：setsuwa.json コンテンツ拡充＋相互参照フィールド追加。motifs/corpus/索引は不変
**方針裁定**：ケンシン（2026-07-07）＝相互参照は setsuwa.json にフィールド追加／拡充は葬送向き厳選

## 経緯

handoff_2026-07-05 残タスク (c)「説話拡充（忍耐・慈悲系異伝・大智度論 k218-222 相互参照）」。
大智度論 巻第四の本生譚5話（k218-222／m4230-m4234）を調査したところ、既存 setsuwa と
2件重複（尸毘王・羼提仙人）。相互参照を付け、葬送向きの新規1話を厳選追加した。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：schema 1.0→1.1・count 40→41
  - 新規 **s041 須陀須摩王の実語**（実語＝命がけで約束を守る信義・大智度論 巻第四 k219）。
    tags=誠実／正直／信念（既存99タグ内・新タグなし＝被覆99/99 維持）。canon=tale
  - **corpus_refs**（任意フィールド・schema 1.1・`{corpus,para,motif,note}`）を付与：
    s009 尸毘王↔daichidoron k218/m4230／s011 忍辱仙人↔k221/m4233／s041↔k219/m4231
    （setsuwa→corpus の片方向。corpus 側は不変＝validate_corpus.py 非干渉）
  - description 更新（41話・タグ軸統制済み・corpus_refs 説明）
- **_dev_references/setsuwa_tag_axes_v1.md**：§8「大智度論との相互参照」追加・41話へ
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 40→41 に更新
- **handoff_2026-07-07_setsuwa_expand_v1_1.md**（本ファイル）

### kaimyo-app（変更2）
- **lib/warehouse.ts**：SetsuwaCorpusRef 型を新設・Setsuwa に corpus_refs?（任意）追加・
  stale コメント是正。picker は corpus_refs 未使用
- **data/indices/setsuwa.json**：倉庫 v1.1 から同期（41話）

## 見送り（裁定）

大智度論 k220 毒龍（剝皮）・k222 薩陀波崙（売身）は描写が凄惨で葬送法話トーンに不適のため
v1.1 では追加せず・相互参照も未付与。将来テーマ次第で再検討。

## 検証

- JSON 再パース OK／count 41・records 41／synopsis 246字（150-250内）／半角括弧0／NUL0
- s041 新タグ0＝被覆99/99 維持・20軸不変（picker 辞書・SETSUWA_AXES 変更不要）
- picker 回帰（outputs/setsuwa_axis_harness.py・本番辞書 H.NEW で41話ロード）：
  文書化5テーマ（誠実→s002/s039・感謝と自立→s006/s022・信念→s008/s001・看取り→s021/s009・
  無常→s028/s005）は完全不変。s041 は「信義／約束／実語」系テーマで top pick 化を確認
- backup：outputs/setsuwa.json.bak_pre_v1_1

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.1＋spec §8＋push4（count41）＋本 handoff を commit+push
   （commit_message.txt 更新済）。SAFETY CHECK「deleted:」停止時は handoff_2026-07-05 の
   stale rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count41）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋warehouse.ts を commit+push
   （commit_message_setsuwa_sync.txt 更新済・whitelist に両ファイル含む）
4. tsc はホスト側 `tsc --noEmit -p tsconfig.json` で確認（sandbox 末尾 truncate 表示のため）

## 落とし穴メモ

- sandbox の末尾 truncate/stale 表示は既知 phantom（ホスト側は正常）。
- source.doc 2件（vol19/vol20_build）M 表示・kaimyo-app stale index.lock（bat 自動削除）も既知。
- corpus_refs は setsuwa 側のみ（別系統資産・逆参照は spec §8 の表で代替）。

## 検証追記（2026-07-07・後続セッション）

未了だった **kaimyo-app ホスト側 tsc を確認済み＝型エラーなし（TSC_EXIT=0・診断0行）**。
picker の SETSUWA_AXES エクスポート／warehouse.ts の SetsuwaCorpusRef 型・Setsuwa.corpus_refs?
は committed HEAD 上でクリーンにパス（両 .ts が --listFiles でコンパイル対象入りも確認）。

- kaimyo-app HEAD = **aee5a0c** 照合済（a3a1d11 は取りこぼし→再コミット是正の痕跡）
- 手法：sandbox worktree の truncate phantom を回避するため、健全な git object から
  `git archive HEAD` を /tmp（sandbox ローカル fs）へ展開し、full ロードされる node_modules を
  symlink して `node_modules/.bin/tsc --noEmit -p tsconfig.json` を実行。これで EOF 誤検出を排除。
- phantom 再現値（記録用）：sandbox worktree は picker=13408／warehouse=9700／setsuwa=46966 バイトに
  truncate 表示、HEAD blob は 17935／10281／49280 で健全。git status の M 表示（.bat 群含む多数）も
  同 truncate 由来の偽差分＝committed 内容に変更なし。

## 次にやること

- (c) 追加拡充の余地：忍耐・慈悲系の穏やかな異伝（非大智度論）を厳選追加（被覆100%維持・
  新テーマのみ軸追加で仕様書 v2）。
- (d) 新著作取込（Phase 1〜・kakikudashi-data スキル）。

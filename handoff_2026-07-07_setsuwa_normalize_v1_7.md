# handoff: 説話ライブラリ v1.7（既存5話 synopsis 字数正規化）

**日付**：2026-07-07（v1.6＝a079dd4／CLAUDE.md ★entry＝f103d29 の後続）
**着手時 HEAD**：倉庫 f103d29／kaimyo-app 0233569
**種別**：既存5話 synopsis の字数正規化のみ（話数・タグ・軸・被覆は不変・count 61 のまま・新レコードなし）
**方針裁定**：ケンシン（2026-07-07）＝残タスクの synopsis 字数正規化

## 経緯

v1 初版で synopsis が 150字をわずかに下回っていた5話（spec §11/§13 で正規化候補として記載）を、
筋・登場人物・結末・中立文体を変えずに穏やかに肉付けし、規約の 150-250 内へ揃えた。

## 成果物

### buddhist-data-api（変更2＋新規1）
- **data/indices/setsuwa.json**：以下5話の synopsis を肉付け（count 61 不変・tags/point/
  connective_example/source/canon は不変）
  - s014 化城宝処 149→205／s015 薬草喩 148→202／s021 病める修行者の看病 148→201／
    s022 自灯明・法灯明 142→196／s024 スジャータの乳粥 146→189
  - 加筆は描写の補足のみ（導師の慈悲・雨の一味・看病の手順・阿難の様子・苦行の激しさ 等）
- **_dev_references/setsuwa_tag_axes_v1.md**：§14「既存5話の synopsis 字数正規化」追加
- **handoff_2026-07-07_setsuwa_normalize_v1_7.md**（本ファイル）
- push4_sync_setsuwa.bat は count guard 61 のまま変更なし

### kaimyo-app（変更1＝データのみ）
- **data/indices/setsuwa.json**：倉庫 v1.7 から同期（5話 synopsis 正規化）
- warehouse.ts・picker.ts はコード変更なし

## 検証（ホスト権威）

- 改変前に新 synopsis 5件を fragment 単体検証：新字数 205/202/201/196/189（全て150-250内）・
  半角括弧0・英字混入0
- Edit ツール5件（各 synopsis 文字列値の完全置換＝JSON 構造不変）→ ホスト Read で5話とも反映確認
- ⚠️ sandbox mount は setsuwa.json を stale 表示（本セッションでも編集後 python parse が
  char23025 で失敗）。full JSON parse は **push 後 git show HEAD（object store 権威）で確認**する。
- picker 影響なし（tags 不変・synopsis は pickSetsuwa の選定スコアに不関与＝tags 照合のみ）

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json（5話 synopsis）＋spec §14＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count61）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit

## 落とし穴メモ

- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
  synopsis 文字列値の置換のみで新レコードや構造は触っていないため、JSON 構造は保存される
  （新 synopsis に ASCII ダブルクォート・バックスラッシュ無し＝エスケープ問題なし）。
- push 後の検証：git show HEAD:data/indices/setsuwa.json を parse し count 61・
  対象5話 synopsis 150-250内・unknown tags [] を確認。両 HEAD blob SHA-256 一致も照合。

## 次にやること（残タスク）

- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の .doc/.docx/写真/
  貼り付けと形式をケンシンに確認してから着手。
- 任意：picker prompt「出典検証済みの40話から選定」の表示ずれ（現61話）。ハードコード「61話」に
  更新するか／数を除いて将来無依存化するか／動的に count を差し込むか はケンシン裁定。
  いずれも lib/setsuwa-picker.ts の変更＝要ホスト tsc（sandbox は truncate で tsc 不可）。

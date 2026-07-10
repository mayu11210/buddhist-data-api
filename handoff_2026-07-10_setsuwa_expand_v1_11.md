# handoff: 説話ライブラリ v1.11（縁起＝相互依存の説話 追加・2話）

**日付**：2026-07-10（v1.10＝92a4ca8 の後続）
**着手時 HEAD**：倉庫 92a4ca8／kaimyo-app fb5e379（いずれも push 済・69話 SHA 一致 IDENTICAL 確認済）
**種別**：setsuwa.json コンテンツ拡充（2話・count 69→71）。motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0
**方針裁定**：ケンシン（2026-07-10）＝「縁起関係で良い説話」を指定

## 経緯

「すべてのいのちは支え合い関わり合って成り立つ（縁起・ご縁・つながり）」という葬送の核テーマを
補う2話。相依の相応部と重重無尽の華厳。既存99タグ内・新タグ0で表現（picker 無改修）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 69→71・description 71話
  - s070 二束の葦（縁起の譬え）相応部 芦束経 SN12.67（因縁相応）／漢訳 雑阿含経・early
    tags=支え合い／ご縁／人生の実相／気づき（A10/A05/A17）
  - s071 因陀羅網（重重無尽のつながり）華厳経（華厳思想・帝網＝縁起の譬え）・mahayana
    tags=ご縁／いのちの重さ／世界への眼差し／気づき（A10/A14/A16/A17）
  - 既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし
- **_dev_references/setsuwa_tag_axes_v1.md**：§18「縁起（相互依存）の説話 追加（v1.11）」・対象を71話へ
- **push4_sync_setsuwa.bat**：count guard 69→71
- **handoff_2026-07-10_setsuwa_expand_v1_11.md**（本ファイル）

### kaimyo-app（変更2＝データ＋同期メッセージ）
- **data/indices/setsuwa.json**：倉庫 v1.11 から同期（71話・push4 が実施）
- **commit_message_setsuwa_sync.txt**：v1.11/71話 に更新（ラベルずれ再発防止・先回り更新）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0・canon 既存枠）

## 検証（ホスト権威）

⚠️ setsuwa.json・spec doc とも sandbox mount stale/truncate 表示の既知 phantom。Read ツール
（ホスト権威）＋自己完結ハーネスで実施：

- 新2レコード fragment 単体 JSON 検証：synopsis 237/221字（150-250内）・半角括弧0・
  英字混入は source の経典略号のみ（SN12.67）・全タグ既存99内・新タグ0・NUL0・JSON 妥当
- 出典検証（Web）：s070＝相応部 SN12.67 芦束経（Naḷakalāpī・SN12 因縁相応・二束の葦の相依＝縁起）。
  s071＝因陀羅網／帝網（華厳の重重無尽の縁起イメージ・出典は華厳系とやや広め＝教義的譬え）
- Edit 後 Read 再確認：count 71・description 71話・s069 は `},` で閉じ s070-071 挿入・
  s071 末尾カンマなし・配列 `]`＋オブジェクト `}` 健全（1073行）

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.11＋spec §18＋push4（count71）＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count71）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋更新済 commit_message_setsuwa_sync.txt
   を commit+push
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：両 HEAD の setsuwa.json を git show で parse し count 71・s070/s071 反映・
   SHA-256 一致を確認

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・.bat を truncate/stale 表示する既知 phantom。
  整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。commit_push を複数回回すと
  2回目以降は「nothing added to commit」＝既にコミット済のサイン（実害なし）。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 選定基準：葬送向きの穏やかなトーン・凄惨な描写や自死を含む伝承は不採用。

## 次にやること

- 任意：picker に「縁起・因縁・つながり → ご縁・支え合い・人生の実相」のキーワード対応を追加
  （SETSUWA_THEME_KEYWORDS・新タグ0のまま・要ホスト tsc）＝縁起語の法話テーマで s070/s071 を確実に surface。
- (c') さらなる拡充（任意）。薄い軸は A19 立ち直り（4）・A03 自立（5）・A20 今を生きる（5）。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。

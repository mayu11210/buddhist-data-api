# handoff: 説話ライブラリ v1.9（和製説話＝日本仏教説話集を初導入・2話）

**日付**：2026-07-10（v1.8＝a7298b5 の後続）
**着手時 HEAD**：倉庫 a7298b5／kaimyo-app 6b55a71（いずれも push 済）
**種別**：setsuwa.json コンテンツ拡充（2話・count 66→68）。motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0
**方針裁定**：ケンシン（2026-07-10）＝残タスク (c') 和製説話の取り入れ。「伝わりそうなもの」を横断選定・方式A採用

## 経緯

これまで印度系（阿含・大乗・本生譚）に限っていた素材に、日本の仏教説話集から葬送向きの
2話を初めて加えた。**方式A＝canon を新設せず既存 `tale` 枠に分類し、source に所載説話集を
明記**（warehouse.ts の canon 型 'early'|'mahayana'|'tale' 不変＝コード変更・tsc 不要。
picker は canon 未使用）。tale の定義を「譬喩・本生・因縁譚および和漢の説話集」に拡張。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 66→68・description（68話＋tale 定義に和漢説話集を追記）
  - s067 わらしべ長者 今昔物語集 巻十六（長谷観音利益譚）／宇治拾遺物語・tale
    tags=ご縁／導き／善き行い／気づき（A10/A18/A12/A17）
  - s068 玄敏僧都の遁世 発心集 第一（鴨長明）・tale
    tags=手放す／とらわれない／謙虚／人柄（A13/A14/A15）
  - 既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし
  - 薄い軸を補強：A13 手放す 4→5・A15 遺徳人柄 4→5
- **_dev_references/setsuwa_tag_axes_v1.md**：§16「和製説話の導入（v1.9・方式A）」追加・対象を68話へ
- **push4_sync_setsuwa.bat**：count guard 66→68
- **handoff_2026-07-10_setsuwa_expand_v1_9.md**（本ファイル）

### kaimyo-app（変更2＝データ＋同期メッセージ）
- **data/indices/setsuwa.json**：倉庫 v1.9 から同期（68話・push4 が実施）
- **commit_message_setsuwa_sync.txt**：v1.9/68話 に更新（v1.8 のラベルずれ再発防止・先回り更新）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（方式A＝新タグ0・canon 新設なし）

## 検証（ホスト権威）

⚠️ setsuwa.json も spec doc も sandbox mount が stale/truncate 表示（本セッションでも
bash tail が spec の §15 前を表示・setsuwa.json full parse も stale）。Read ツール（ホスト権威）
＋自己完結ハーネスで実施：

- 新2レコード fragment 単体 JSON 検証：synopsis 243/243字（150-250内）・半角括弧0・
  英字混入0・全タグ既存99内・新タグ0・NUL0・JSON 妥当
- 出典検証（Web）：わらしべ長者＝今昔物語集 巻十六「長谷にまゐりし男、観音の助けによりて
  富を得たる語 第二十八」／宇治拾遺物語。玄敏僧都＝発心集 第一第1話「玄敏僧都、遁世逐電の事」。
  見送り：弘法水（folk 拡散・単一所載の典拠なし）／雀報恩 宇治拾遺3-16（後半が凄惨・毒虫の死）
- Edit 後 Read 再確認：count 68・description 68話＋tale 定義拡張・s066 は `},` で閉じ
  s067-068 挿入・s068 末尾カンマなし・配列 `]`＋オブジェクト `}` 健全（1028行）

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.9＋spec §16＋push4（count68）＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count68）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋更新済 commit_message_setsuwa_sync.txt
   を commit+push（今回はラベルも v1.9/68話 で正しく出る）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：両 HEAD の setsuwa.json を git show で parse し count 68・s067/s068 反映・
   SHA-256 一致を確認

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・.bat を truncate/stale 表示する既知 phantom。
  整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 和製説話は方式A（canon:tale・source に所載集明記）。将来 canon 分類を細かくするなら
  warehouse.ts の union 拡張＝要ホスト tsc（方式B）。
- 選定基準：葬送向きの穏やかなトーン・凄惨な描写や自死を含む伝承は不採用（雀報恩を見送った基準）。

## 次にやること

- (c') さらなる拡充（任意）。和製の続き候補＝沙石集の正直・慈悲譚、往生譚（今昔15・往生極楽記）、
  雀報恩を核だけ再話して採るか等。薄い軸は A19 立ち直り（4）・A03 自立（5）・A20 今を生きる（5）。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。

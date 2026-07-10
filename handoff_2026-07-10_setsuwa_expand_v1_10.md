# handoff: 説話ライブラリ v1.10（誠実＝正直の徳の和製説話 追加・1話）

**日付**：2026-07-10（v1.9＝56a30bb の後続）
**着手時 HEAD**：倉庫 56a30bb／kaimyo-app d018e70（いずれも push 済・68話 SHA 一致 IDENTICAL 確認済）
**種別**：setsuwa.json コンテンツ拡充（1話・count 68→69）。motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0
**方針裁定**：ケンシン（2026-07-10）＝「誠実に生きた人が出てくる心に響く説話」を指定

## 経緯

和製説話（方式A・canon:tale・v1.9 導入）の続きとして、誠実・正直をテーマにした沙石集の
1話を追加した。方式A（canon 新設せず既存 tale 枠・source に所載集明記）を継続。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 68→69・description 69話
  - s069 正直の徳（拾った銀を返した夫婦）沙石集（無住・「いみじき成敗／正直の徳」）・tale
    tags=正直／誠実／真心／善き行い（A01/A12）
  - 既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし
- **_dev_references/setsuwa_tag_axes_v1.md**：§17「誠実（正直の徳）の追加（v1.10）」・対象を69話へ
- **push4_sync_setsuwa.bat**：count guard 68→69
- **handoff_2026-07-10_setsuwa_expand_v1_10.md**（本ファイル）

### kaimyo-app（変更2＝データ＋同期メッセージ）
- **data/indices/setsuwa.json**：倉庫 v1.10 から同期（69話・push4 が実施）
- **commit_message_setsuwa_sync.txt**：v1.10/69話 に更新（ラベルずれ再発防止・先回り更新）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（方式A＝新タグ0・canon 新設なし）

## 検証（ホスト権威）

⚠️ setsuwa.json・spec doc とも sandbox mount stale/truncate 表示の既知 phantom。Read ツール
（ホスト権威）＋自己完結ハーネスで実施：

- 新1レコード fragment 単体 JSON 検証：synopsis 242字（150-250内）・半角括弧0・英字混入0・
  全タグ既存99内・新タグ0・NUL0・JSON 妥当
- 出典検証（Web）：沙石集「いみじき成敗／正直の徳」（唐土の餅売り夫婦、拾った銀を返す→
  嘘の落とし主を国守が見抜く）を確認
- Edit 後 Read 再確認：count 69・description 69話・s068 は `},` で閉じ s069 挿入・
  s069 末尾カンマなし・配列 `]`＋オブジェクト `}` 健全（1043行）

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.10＋spec §17＋push4（count69）＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count69）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋更新済 commit_message_setsuwa_sync.txt
   を commit+push
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：両 HEAD の setsuwa.json を git show で parse し count 69・s069 反映・
   SHA-256 一致を確認

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・.bat を truncate/stale 表示する既知 phantom。
  整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 選定基準：葬送向きの穏やかなトーン・凄惨な描写や自死を含む伝承は不採用。

## 次にやること

- (c') さらなる拡充（任意）。和製の続き候補＝往生譚（今昔15・往生極楽記）、雀報恩を核だけ再話、
  沙石集の慈悲譚 等。薄い軸は A19 立ち直り（4）・A03 自立（5）・A20 今を生きる（5）。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。

# handoff: 説話ライブラリ v1.6（無常実相・今を生きる系4話 拡充）

**日付**：2026-07-07（v1.5＝36e6703 の後続）
**着手時 HEAD**：倉庫 36e6703／kaimyo-app dba73b9（いずれも push 済・両 HEAD blob バイト一致）
**種別**：setsuwa.json コンテンツ拡充のみ（motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0）
**方針裁定**：ケンシン（2026-07-07）＝残タスク (c') さらなる拡充。葬送中心テーマの薄めの軸を補強

## 経緯

handoff v1.5 の (c') 継続。まだ薄めだった軸（A05 無常実相＝3話・A20 今を生きる）――いずれも葬送の
中心テーマ――を補強する4話。いずれも既存99タグ内で厳選。凄惨な描写・自死を含む伝承は不採用
（例：Vakkali「法を見る者は我を見る」は教え自体は美しいが伝承が自死を含むため採用せず、
代わりに会者定離〔アーナンダへの慰め〕を採用）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 57→61（schema 1.1 のまま）
  - s058 四門出遊（過去現在因果経ほか 仏伝・tale）tags=無常／人生の実相／気づき／求道
  - s059 一夜賢者の偈（中部 一夜賢者経 MN131・early）tags=今を生きる／一日を大切に／今なすべきこと／実践
  - s060 アーナンダへの慰め（長阿含 遊行経／大般涅槃経・early）tags=無常／悲しみの受容／最後の教え／遺された者へ
  - s061 沙羅双樹の花（長阿含 遊行経／大般涅槃経・early）tags=無常／人生の実相／最後のご縁／美しさへの感謝
  - いずれも既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし（非大智度論）
  - description（57話→61話）更新
- **_dev_references/setsuwa_tag_axes_v1.md**：§13「無常実相・今を生きる系の拡充（v1.5 続）」追加・対象を61話へ
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 57→61 に更新
- **handoff_2026-07-07_setsuwa_expand_v1_6.md**（本ファイル）

### kaimyo-app（変更1＝データのみ）
- **data/indices/setsuwa.json**：倉庫 v1.6 から同期（61話）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0のため辞書・型とも不変）

## 検証（ホスト権威）

⚠️ setsuwa.json も spec doc も sandbox mount が stale/truncate 表示。Read ツール（ホスト権威）
＋自己完結ハーネスで実施：

- 新4レコード fragment 単体 JSON 検証：synopsis 192/196/208/199字（全て150-250内）・
  半角括弧0・英字混入は source の経典略号のみ（MN131 等・既存 AN4.36/SN47.13 と同慣行）・
  全タグ既存99内・新タグ0・NUL0
- Edit 後 Read 再確認：count 61・s057 は `},` で閉じ s058-061 挿入・レコード間カンマ適正・
  配列 `]`＋オブジェクト `}` 健全・s061 末尾カンマなし（923行）
- picker 回帰（57話 vs 61話・タグ埋め込み自己完結ハーネス）：
  - **文書化5テーマの top1 完全不変**＝誠実 s001・感謝と自立 s006・信念 s008・看取り s021・無常 s028
  - 新4話は 今を生きる→s059・涅槃の花→s061・会者定離→s060(#2)・四門→s058(無常/求道系で surface)
    で正しく上位化

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.6＋spec §13＋push4（count61）＋本 handoff＋
   更新済 commit_message.txt を commit+push。SAFETY CHECK「deleted:」停止時は handoff_2026-07-05 の
   stale staged rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count61）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・picker.ts・warehouse.ts・多数の .bat を truncate/stale
  表示する既知 phantom。整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
  .md 追記は末尾 anchor を Read で正確に確認してから Edit。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 説話選定の基準：非大智度論・葬送向きの穏やかなトーン・凄惨な描写や自死を含む伝承は不採用。

## 現状（61話・軸カバレッジ）

今セッションで20話追加（s042-s061）。20軸すべて3話以上でバランス良好。相対的にまだ薄いのは
A03 自立中道 の一部・A16 世界への眼差し の一部程度。既存で 150字弱の旧話（s014/s015/s021/s022/s024
＝v1 初版）は肉付け正規化の候補（今セッション追加分は全て範囲内）。

## 次にやること

- (c') さらなる拡充（余地は縮小・任意）or 既存5話（s014/s015/s021/s022/s024）の synopsis 字数正規化。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の形式をケンシンに確認。
- 任意：picker prompt「出典検証済みの40話から選定」の表示ずれ修正（現在61話・要ホスト tsc）。
- 拡充が一段落したら CLAUDE.md ★entry 追記の検討（現状は handoff＋spec doc で継続性担保）。

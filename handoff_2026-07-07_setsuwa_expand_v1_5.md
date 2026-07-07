# handoff: 説話ライブラリ v1.5（仏性本来性・絆縁系4話 拡充）

**日付**：2026-07-07（v1.4＝2ef3579 の後続）
**着手時 HEAD**：倉庫 2ef3579／kaimyo-app b1eec44（いずれも push 済・両 HEAD blob バイト一致）
**種別**：setsuwa.json コンテンツ拡充のみ（motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0）
**方針裁定**：ケンシン（2026-07-07）＝残タスク (c') さらなる拡充。薄めの軸を補強

## 経緯

handoff v1.4 の (c') 継続。薄めだった軸（A17 仏性本来性＝3話・A10 絆縁〔夫婦 s035・友情 s037 各1話〕）
を補強する4話。いずれも既存99タグ内で厳選（凄惨な描写は不採用の基準を継続）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 53→57（schema 1.1 のまま）
  - s054 力士の額の宝珠（大般涅槃経 如来性品・mahayana）tags=仏性／本来の宝／気づき／本来の豊かさ
  - s055 善財童子の旅（華厳経 入法界品・mahayana）tags=ご縁／求道／気づき／導き
  - s056 四禽の友情（ジャータカ・クルンガ鹿友情譚・tale）tags=友情／支え合い／ご縁／思いやり
  - s057 カッサパ夫妻・共に道を歩む（長老尼偈／長老偈 とその註・early）tags=夫婦の絆／共に歩む／求道／志
  - いずれも既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし（非大智度論）
  - description（53話→57話）更新
- **_dev_references/setsuwa_tag_axes_v1.md**：§12「仏性本来性・絆縁系の拡充（v1.4 続）」追加・対象を57話へ
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 53→57 に更新
- **handoff_2026-07-07_setsuwa_expand_v1_5.md**（本ファイル）

### kaimyo-app（変更1＝データのみ）
- **data/indices/setsuwa.json**：倉庫 v1.5 から同期（57話）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0のため辞書・型とも不変）

## 検証（ホスト権威）

⚠️ setsuwa.json も spec doc も sandbox mount が stale/truncate 表示。Read ツール（ホスト権威）
＋自己完結ハーネスで実施：

- 新4レコード fragment 単体 JSON 検証：synopsis 209/201/208/213字（全て150-250内）・
  半角括弧0・英字混入0・全タグ既存99内・新タグ0・NUL0
- Edit 後 Read 再確認：count 57・s053 は `},` で閉じ s054-057 挿入・レコード間カンマ適正・
  配列 `]`＋オブジェクト `}` 健全・s057 末尾カンマなし（863行）
- picker 回帰（53話 vs 57話・タグ埋め込み自己完結ハーネス）：
  - **文書化5テーマの top1 完全不変**＝誠実 s001・感謝と自立 s006・信念 s008・看取り s021・無常 s028
  - 新4話は 仏性本来→s054・ご縁の旅→s055・友情支え合い→s037継続(s056 同点2位)・夫婦共に→s057
    で正しく上位化

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.5＋spec §12＋push4（count57）＋本 handoff＋
   更新済 commit_message.txt を commit+push。SAFETY CHECK「deleted:」停止時は handoff_2026-07-05 の
   stale staged rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count57）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・picker.ts・warehouse.ts・多数の .bat を truncate/stale
  表示する既知 phantom（.md も対象）。整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
  .md 追記は末尾 anchor を Read で正確に確認してから Edit。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 新4話は corpus_refs なし（非大智度論）。
- picker prompt 文字列「出典検証済みの40話から選定」は v1 以来「40話」のまま（現在57話）＝軽微な
  表示ずれ。修正するなら「40」→「57」＋ホスト tsc。

## 現状の軸カバレッジ（57話・参考）

ほぼ全軸が3話以上。相対的にまだ薄いのは A05 無常実相（s005/s028/s038）、A20 今を生きる、
A18 導き方便 の一部。既存で 150字をわずかに下回る旧話（s014/s015/s021/s022/s024＝いずれも v1 初版）
は肉付け正規化の候補（今回追加の s042-s057 は全て範囲内）。

## 次にやること

- (c') さらなる拡充 or 既存5話（s014/s015/s021/s022/s024）の synopsis 字数正規化。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の形式をケンシンに確認。
- 任意：picker prompt の「40話→57話」表示ずれ修正（要ホスト tsc）。
- 拡充が一段落したら CLAUDE.md ★entry 追記の検討。

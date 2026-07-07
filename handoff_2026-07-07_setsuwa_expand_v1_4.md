# handoff: 説話ライブラリ v1.4（遺徳・人柄・立ち直り・自立系4話 拡充）

**日付**：2026-07-07（v1.3＝61a23c5 の後続）
**着手時 HEAD**：倉庫 61a23c5／kaimyo-app 7db9262（いずれも push 済・両 HEAD blob バイト一致）
**種別**：setsuwa.json コンテンツ拡充のみ（motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0）
**方針裁定**：ケンシン（2026-07-07）＝残タスク (c') さらなる拡充。薄めの軸を補強

## 経緯

handoff v1.3 の (c') 継続。薄めだった軸（A15 遺徳人柄＝2話・A19 立ち直り改心＝2話・A03 自立中道）を
補強する4話。いずれも既存99タグ内で厳選（凄惨な描写は不採用の基準を継続）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 49→53（schema 1.1 のまま）
  - s050 アッサジの静かな威儀（律蔵大品・early）tags=人柄／謙虚／ご縁／導き
  - s051 サーリプッタの遺徳（相応部 純陀経 SN47.13・early）tags=遺徳／徳は残る／目に見えぬ支え／遺された者へ
  - s052 アンバパーリーの生き直し（長老尼偈／大般涅槃経・early）tags=立ち直り／再生／布施／気づき
  - s053 ダニヤ経（スッタニパータ1.2・early）tags=中道／自立／手放す／とらわれない
  - いずれも既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし（非大智度論）
  - description（49話→53話）更新
- **_dev_references/setsuwa_tag_axes_v1.md**：§11「遺徳・人柄・立ち直り・自立系の拡充（v1.3 続）」
  追加・対象を53話へ（§2 の20軸・§4 割当は不変＝仕様は v1 のまま）
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 49→53 に更新
- **handoff_2026-07-07_setsuwa_expand_v1_4.md**（本ファイル）

### kaimyo-app（変更1＝データのみ）
- **data/indices/setsuwa.json**：倉庫 v1.4 から同期（53話）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0のため辞書・型とも不変）

## 検証（ホスト権威）

⚠️ setsuwa.json も spec doc も sandbox mount が stale/truncate 表示（spec doc は §7 までしか見えず、
setsuwa.json はサイズ・parse phantom）。Read ツール（ホスト権威）＋自己完結ハーネスで実施：

- 新4レコード fragment 単体 JSON 検証：synopsis 215/211/185/198字（全て150-250内）・
  半角括弧0・全タグ既存99内・新タグ0・NUL0
- Edit 後 Read 再確認：count 53・s049 は `},` で閉じ s050-053 挿入・レコード間カンマ適正・
  配列 `]`＋オブジェクト `}` 健全・s053 末尾カンマなし（803行）
- picker 回帰（49話 vs 53話・タグ埋め込み自己完結ハーネス）：
  - **文書化5テーマの top1 完全不変**＝誠実 s001・感謝と自立 s006・信念 s008・看取り s021・無常 s028
  - 新4話は 人柄威儀→s040継続(s050 #2)・遺徳→s051・自立中道→s010継続(s053 同点2位)・
    安らかな臨終→s048継続(s053 同点2位) で正しく上位化

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.4＋spec §11＋push4（count53）＋本 handoff＋
   更新済 commit_message.txt を commit+push。SAFETY CHECK「deleted:」停止時は handoff_2026-07-05 の
   stale staged rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count53）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
   （commit_message_setsuwa_sync.txt 更新済＝データのみ・warehouse/picker は no-op ステージ）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc（setsuwa_tag_axes_v1.md）・picker.ts・warehouse.ts・
  多数の .bat を truncate/stale 表示する既知 phantom（.md も対象。spec doc の tail が §7 に見える等）。
  git status の M・git diff の deletions も同 phantom＝committed 内容に変更なし。整合は Read＋
  git show HEAD＋SHA-256（object store 権威）で行う。**.md の追記も Edit ツールで行い、末尾 anchor は
  Read ツールで正確な文字列を確認してから**（本セッションで §10 末尾の空白差異で Edit 1回失敗→
  Read で正確な末尾を取得して成功）。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 新4話は corpus_refs なし（非大智度論）。将来これら原典（律蔵・相応部・長老尼偈・スッタニパータ）を
  倉庫 corpus に取り込んだ際に §8 と同形式で相互参照を検討。
- picker prompt 文字列「出典検証済みの40話から選定」は v1 以来「40話」のまま（現在53話）＝軽微な
  表示ずれ。コード変更＝要ホスト tsc のため本 v1.4 でも触らず。修正するなら「40」→「53」＋ホスト tsc。

## 次にやること

- (c') さらなる拡充の余地：ほぼ全軸が3話以上に。まだ相対的に薄いのは A17 仏性本来性（s003/s004/s047）、
  A10 絆縁（夫婦・友）あたり。新タグは20軸へ割当し被覆100%維持、収まらぬ新テーマのみ軸追加で仕様書 v2。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の形式をケンシンに確認。
- 任意：picker prompt の「40話→53話」表示ずれ修正（要ホスト tsc）。
- 拡充が一段落したら CLAUDE.md ★entry 追記の検討（現状は handoff＋spec doc で継続性担保）。

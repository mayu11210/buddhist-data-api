# handoff: 説話ライブラリ v1.3（和合・本来性・臨終・布施系4話 拡充）

**日付**：2026-07-07（v1.2＝0e5d4d1 の後続）
**着手時 HEAD**：倉庫 0e5d4d1／kaimyo-app 820850c（いずれも push 済確認済・両 HEAD blob バイト一致）
**種別**：setsuwa.json コンテンツ拡充のみ（motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0）
**方針裁定**：ケンシン（2026-07-07）＝残タスク (c') さらなる拡充。薄めの軸補強＋葬送核心

## 経緯

handoff v1.2 の (c') 継続。薄めだった軸（A13 手放す＝2話・A14 和合謙虚＝2話・A16/A17 自然/
世界への眼差し/本来性）を補強しつつ、葬送法話の頻出アーキタイプ「安らかな臨終」「生涯の布施
（寛大な恩人）」を新設した4話。いずれも既存99タグ内で厳選（凄惨な描写は不採用の基準を継続）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 45→49（schema 1.1 のまま）
  - s046 象と猿の森（コーサンビーの和解・律蔵大品／法句経註・tale）
    tags=和合／謙虚／寄り添い／思いやり（A14+A07）。争いを謙虚に歩み寄り和解へ
  - s047 泥に染まぬ蓮（ドーナ経 AN4.36・early）
    tags=生の肯定／本来の豊かさ／気づき／世界への眼差し（A16+A17）。世に染まらず清らかに咲く
  - s048 チッタ長者の安らかな臨終（相応部 SN41・early）
    tags=手放す／とらわれない／最後の教え／心の持ち方（A13+A18+A06）。執着を手放し穏やかに旅立つ
  - s049 給孤独長者の生涯の布施（中阿含経ほか／祇園精舎建立・tale）
    tags=布施／志／真心／善き行い（A12+A04+A01）。生涯を施しに尽くした恩人の原型
  - いずれも既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし（非大智度論）
  - description（45話→49話）更新
- **_dev_references/setsuwa_tag_axes_v1.md**：§10「和合・本来性・臨終・布施系の拡充（v1.2 続）」
  追加・対象を49話へ（§2 の20軸・§4 割当は不変＝仕様は v1 のまま）
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 45→49 に更新
- **handoff_2026-07-07_setsuwa_expand_v1_3.md**（本ファイル）

### kaimyo-app（変更1＝データのみ）
- **data/indices/setsuwa.json**：倉庫 v1.3 から同期（49話）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0のため辞書・型とも不変）

## 検証（ホスト権威）

⚠️ setsuwa.json は sandbox mount が stale/truncate 表示のため bash パース非採用。Read ツール
（ホスト権威）＋自己完結ハーネスで実施：

- 新4レコード fragment 単体 JSON 検証：synopsis 212/198/197/196字（全て150-250内）・
  半角括弧0・全タグ既存99内・新タグ0・NUL0
- Edit 後 Read 再確認：count 49・s045 は `},` で閉じ s046-049 挿入・レコード間カンマ適正・
  配列 `]`＋オブジェクト `}` 健全・s049 末尾カンマなし
- picker 回帰（45話 vs 49話・タグ埋め込み自己完結ハーネス・lib/setsuwa-picker.ts 忠実移植）：
  - **文書化5テーマの top1 完全不変**＝誠実 s001・感謝と自立 s006・信念 s008・看取り s021・無常 s028
    （看取りの #2 が s044→s046 に推移したが織り込み対象=#1 は保存）
  - 新4話は 和合謙虚→s026継続(s046 同点2位)・蓮生の肯定→s039継続(s047 2位)・
    安らかな臨終→s048・布施の生涯→s049 で正しく上位化

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.3＋spec §10＋push4（count49）＋本 handoff＋
   更新済 commit_message.txt を commit+push。SAFETY CHECK「deleted:」停止時は handoff_2026-07-05 の
   stale staged rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count49）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
   （commit_message_setsuwa_sync.txt 更新済＝データのみ・warehouse/picker は no-op ステージ）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
   （push4 前に kaimyo commit すると取りこぼす）

## 落とし穴メモ

- sandbox mount は setsuwa.json/picker.ts/warehouse.ts/多数の .bat を truncate/stale 表示する
  既知 phantom。git status の M・git diff の deletions も同 phantom＝committed 内容に変更なし。
  Windows 側 git は真の host ファイルをコミットするため pipeline は安全。整合は Read＋git show HEAD
  ＋SHA-256（object store 権威）で行う。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash での read-modify-write は禁止。
- 新4話は corpus_refs なし（非大智度論）。将来これら原典（律蔵・増支部・相応部・中阿含経）を
  倉庫 corpus に取り込んだ際に §8 と同形式で相互参照を検討。
- picker prompt 文字列「出典検証済みの40話から選定」（formatSetsuwaForPrompt）は v1 以来「40話」
  のまま（現在49話）＝軽微な表示ずれ。コード変更＝要ホスト tsc のため本 v1.3 でも触らず
  （データのみ同期の原則保持）。修正するなら「40」→「49」の1語＋ホスト tsc 確認。

## 次にやること

- (c') さらなる拡充の余地：まだ薄い軸＝A15 遺徳人柄（s013/s040 の2話）、A19 立ち直り改心
  （s016/s025 の2話）、A03 自立中道など。新タグは20軸へ割当し被覆100%維持、収まらぬ新テーマのみ
  軸追加で仕様書 v2 に更新。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の形式をケンシンに確認。
- 任意：picker prompt の「40話→49話」表示ずれ修正（要ホスト tsc）。

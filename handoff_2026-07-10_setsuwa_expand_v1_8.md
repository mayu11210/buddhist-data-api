# handoff: 説話ライブラリ v1.8（忍耐・和合・謙虚・立ち直り・精進系5話 拡充）

**日付**：2026-07-07 の v1.7（normalize）＝直近正本の後続。着手は 2026-07-10。
**着手時 HEAD**：倉庫 429920d／kaimyo-app b478011（picker 動的count化 df8cf85 の後・いずれも push 済）
**種別**：setsuwa.json コンテンツ拡充のみ（motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0）
**方針裁定**：ケンシン（2026-07-10）＝残タスク (c') さらなる拡充。諸経典より抽出・「心に響く」おすすめ5話を採用・倉庫正本も更新

## 経緯

薄めだった軸（A08 忍耐寛容＝4・A14 謙虚和合＝4・A19 立ち直り改心＝3・A11 精進継続＝5）を
補強する5話。諸経典（相応部・中部・増支部・摩登伽経・増一阿含）から出典を Web 検証のうえ厳選。
いずれも既存99タグ内で構成し、葬送向きの穏やかなトーン・非凄惨・自死を含まない。非大智度論。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 61→66（schema 1.1 のまま）・description 61→66話
  - s062 受け取られぬ贈り物（罵るバラモン）相応部 阿羅漢罵経 SN7.2／漢訳 雑阿含・early
    tags=寛容／忍耐／怨みを超える／不動心（A08）
  - s063 牛角林の三比丘（水と乳の和合）中部 牛角林小経 MN31／漢訳 中阿含 牛角娑羅林経・early
    tags=和合／共に歩む／思いやり／謙虚（A14/A10/A07）
  - s064 大地のごとき心（サーリプッタの謙虚）増支部 師子吼経 AN9.11・early
    tags=謙虚／寛容／忍耐／自他の尊重（A14/A08）
  - s065 摩登伽女の生き直し 摩登伽経（西晋・竺法護訳）・tale
    tags=立ち直り／再生／気づき／平等の恵み（A19/A17/A16）
  - s066 阿那律の精進と天眼 増一阿含経ほか・early
    tags=精進／継続／不退転／あきらめない（A11/A04）
  - いずれも既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし・corpus_refs なし（非大智度論）
  - 薄い軸を補強：A08 4→6・A14 4→6・A19 3→4・A11 5→6。20軸すべて4話以上
- **_dev_references/setsuwa_tag_axes_v1.md**：§15「忍耐・和合・謙虚・立ち直り・精進系の拡充（v1.8）」追加・対象を66話へ
- **push4_sync_setsuwa.bat**：HEAD blob の count guard を 61→66 に更新
- **handoff_2026-07-10_setsuwa_expand_v1_8.md**（本ファイル）

### kaimyo-app（変更1＝データのみ・push4 が同期）
- **data/indices/setsuwa.json**：倉庫 v1.8 から同期（66話）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0のため辞書・型とも不変）。
  picker 見出しは 2026-07-10 df8cf85 で動的count化済＝66話が自動反映される

## 検証（ホスト権威）

⚠️ setsuwa.json も spec doc も sandbox mount が stale/truncate 表示（本セッションでも
setsuwa.json の bash full parse が char35629 で失敗）。Read ツール（ホスト権威）＋自己完結
ハーネスで実施：

- 新5レコード fragment 単体 JSON 検証：synopsis 244/228/223/212/214字（全て150-250内）・
  半角括弧0・英字混入は source の経典略号のみ（SN7.2/MN31/AN9.11・既存 AN4.36/SN47.13/MN131 と
  同慣行）・全タグ既存99内・新タグ0・NUL0・JSON 妥当
- 出典検証（Web）：SN7.2 阿羅漢罵経・MN31 牛角林小経・AN9.11 師子吼経・摩登伽経（竺法護訳）・
  増一阿含（阿那律 天眼第一）を確認。難陀（Udāna3.2＋サウンダラナンダ）は漢訳一本の典拠が
  立てにくく出典検証基準により見送り／犀角経は葬送に孤高すぎるとして今回不採用
- Edit 後 Read 再確認：count 66・description 66話・s061 は `},` で閉じ s062-066 挿入・
  s066 末尾カンマなし・配列 `]`＋オブジェクト `}` 健全（998行）

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.8＋spec §15＋push4（count66）＋本 handoff＋
   更新済 commit_message.txt を commit+push。SAFETY CHECK「deleted:」停止時は
   handoff_2026-07-05 の stale staged rename 対処（git restore --staged）参照
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count66）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json を commit+push
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：`git show HEAD:data/indices/setsuwa.json` を parse し count 66・
   s062-066 の synopsis 150-250内・unknown tags [] を確認。両 HEAD blob SHA-256 一致も照合

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・picker.ts・warehouse.ts・多数の .bat を truncate/stale
  表示する既知 phantom。整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 説話選定の基準：非大智度論・葬送向きの穏やかなトーン・凄惨な描写や自死を含む伝承は不採用。

## 現状（66話・軸カバレッジ）

20軸すべて4話以上。今回で A08/A14 が6話・A19 が4話・A11 が6話に。相対的にまだ薄いのは
A19 立ち直り改心（4）・A03 自立中道（5）・A20 今を生きる（5）程度。

## 次にやること

- (c') さらなる拡充（余地は縮小・任意）。A19/A03/A20 の補強候補あり（犀角経は保留）。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。書き下し原稿の形式をケンシンに確認。

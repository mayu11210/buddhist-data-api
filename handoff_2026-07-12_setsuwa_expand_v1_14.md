# handoff: 説話ライブラリ v1.14（生きざま賛嘆系 拡充・3話）

**日付**：2026-07-12（v1.13＝1e39e71 の後続・同日連続作業）
**着手時 HEAD**：倉庫 1e39e71／kaimyo-app a8a761e（いずれも push 済・79話 SHA 一致 IDENTICAL 確認済）
**種別**：setsuwa.json コンテンツ拡充（3話・count 79→82）。motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0
**方針裁定**：ケンシン（2026-07-12）＝「お葬式で故人の生きざまを賛嘆する説話」用途。
持ち込みハッタカ（ChatGPT 探索由来）＋Cowork（Fable 5）推奨2話＝案②採用（医王ジーヴァカは見送り・将来候補）

## 経緯

ケンシンが ChatGPT 提案のハッタカ居士（四摂法）の適否を照会 → Cowork が未収録確認・
「接し方の徳」型は既存79話にない構造と評価 → あわせて Cowork から生きざま賛嘆系の
未収録推奨3候補を提示 → 裁定②＝ハッタカ＋林を植える者＋東に傾く樹の3話採用。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 79→82・description 82話
  - s080 ハッタカ居士と四摂法（人をつなぐ四つの徳）増支部 AN8.23-24・四摂法 AN4.32・early
    tags=人柄／思いやり／布施／謙虚／ご縁（A15/A07/A12/A14/A10）
  - s081 林を植える人（功徳は昼夜に増す）相応部 植林経 SN1.47／漢訳 雑阿含経997経・early
    tags=善き行い／徳は残る／布施／働くこと（A12/A15/A02）
  - s082 東に傾く樹（マハーナーマへの教え）相応部 SN55.21-22／漢訳 雑阿含経930経・early
    tags=心の持ち方／善き行い／徳は残る／遺された者へ（A06/A12/A15）
  - 既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし
- **_dev_references/setsuwa_tag_axes_v1.md**：§21「生きざま賛嘆系の拡充（v1.14）」・対象を82話へ
- **push4_sync_setsuwa.bat**：count guard 79→82
- **handoff_2026-07-12_setsuwa_expand_v1_14.md**（本ファイル）

### kaimyo-app（変更2＝データ＋同期メッセージ）
- **data/indices/setsuwa.json**：倉庫 v1.14 から同期（82話・push4 が実施）
- **commit_message_setsuwa_sync.txt**：v1.14/82話 に更新（先回り更新）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0・canon 既存枠・すべて early）

## 設計メモ（生きざま賛嘆の三点セット）

- s080「人への接し方」（四摂＝布施・愛語・利行・同事→参列者への呼びかけに直接展開できる4部構成）
- s081「残した働き」（公共への貢献は本人の死後も生きて働く・功徳昼夜増）
- s082「生涯の傾き」（最期の様子によらず生涯の善が故人を導く＝遺族の不安への直接の答え）
- 既存 s040 徳の香り（法句経54偈）・s050 アッサジ・s051 サーリプッタ遺徳と併用可。
  ChatGPT 提示の法話構成（ハッタカ→四摂の呼びかけ→徳の香り）は s080＋s040 で再現可能。

## 検証（ホスト権威）

⚠️ sandbox mount stale/truncate 表示の既知 phantom 継続。Read ツール（ホスト権威）＋自己完結ハーネス：

- 新3レコード検証：synopsis 239/216/228字（150-250内）・半角混入0（全角のみ）・全タグ既存99内・
  新タグ0・JSON 妥当
- 出典検証（Web）：s080＝AN8.23-24（ハッタカの七→八の美徳・「他の在家の人はいなかったか」の謙虚）・
  AN4.32（四摂事）・ハッタカは「四摂によって衆を摂する第一」の在家弟子。s081＝SN1.47 Vanaropa
  （園・林・橋・井戸・宿を施す者の功徳は昼夜に増す）。s082＝SN55.21-22（「恐れるな、マハーナーマ」＋
  東に傾く樹の譬え）
- タグ実数補強：人柄 3→4・徳は残る 2→4・遺された者へ 3→4・働くこと／ご縁／謙虚 各＋1

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.14＋spec §21＋push4（count82）＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count82）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋更新済 commit_message_setsuwa_sync.txt
   を commit+push（「Nothing to commit」は既コミット済のサイン＝正常）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：両 HEAD の setsuwa.json を git show で parse し count 82・s080-082 反映・
   SHA-256 一致を確認

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・.bat を truncate/stale 表示する既知 phantom。
  整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- タグは setsuwa の99語彙で照合（motifs.json 側の軸語彙と混同しない＝v1.13 の「慈愛」検出が前例）。

## 次にやること

- 任意：picker キーワード対応（縁起・因縁・つながり → ご縁・支え合い・人生の実相・要ホスト tsc）。
- 将来候補：医王ジーヴァカ（職能奉仕型の賛嘆・synopsis の焦点設計が課題）。
- (c') さらなる拡充（任意）／(d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。

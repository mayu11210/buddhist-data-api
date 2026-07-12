# handoff: 説話ライブラリ v1.13（親子の情・悲しみの受容系 拡充・3話）

**日付**：2026-07-12（v1.12＝cb57a64 の後続）
**着手時 HEAD**：倉庫 cb57a64／kaimyo-app 7c4b1d6（いずれも push 済・76話 SHA 一致 IDENTICAL 確認済）
**種別**：setsuwa.json コンテンツ拡充（3話・count 76→79）。motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0
**方針裁定**：ケンシン（2026-07-12）＝持ち込み3候補（ChatGPT 探索由来）。Cowork が未収録確認・
適合性評価（薄い領域の実数照合）を提示し「3話すべて採用」の裁定

## 経緯

ケンシンが ChatGPT で探索した感動系説話3話の持ち込み。全て未収録を確認。タグ実数照合で
親の恩（2）・親の愛（1）・悲しみの受容（2）・癒し（1）という葬送中核の薄い領域をちょうど
埋めると判明し、全採用。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 76→79・description 79話
  - s077 慈童女（じどうにょ）の鉄輪 雑宝蔵経 巻第一「慈童女縁」・tale
    tags=親の恩／報恩／利他／自己犠牲／慈悲（A09/A07）
    孝心→罪→受苦→「一切の苦を我が身に」＝世間善から菩提心が生まれる瞬間（真言宗法話向き）
  - s078 迦旦遮羅（かたんしゃら）――五百生の母 雑宝蔵経 巻第一・tale
    tags=親の愛／親子の絆／慈悲／平等の恵み（A09/A07/A16）
  - s079 ウッビリーの悲しみの矢 長老尼偈 51-53偈・early
    tags=悲しみの受容／悲しみと向き合う／癒し／気づき／子ども（A06/A17）
    s005 キサーゴータミーの補完（行動を通した自得 vs 一句で開く）
  - 既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし
- **_dev_references/setsuwa_tag_axes_v1.md**：§20「親子の情・悲しみの受容系の拡充（v1.13）」・対象を79話へ
- **push4_sync_setsuwa.bat**：count guard 76→79
- **handoff_2026-07-12_setsuwa_expand_v1_13.md**（本ファイル）

### kaimyo-app（変更2＝データ＋同期メッセージ）
- **data/indices/setsuwa.json**：倉庫 v1.13 から同期（79話・push4 が実施）
- **commit_message_setsuwa_sync.txt**：v1.13/79話 に更新（先回り更新）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0・canon 既存枠）

## 検証（ホスト権威）

⚠️ setsuwa.json・spec doc・.bat とも sandbox mount stale/truncate 表示の既知 phantom。Read ツール
（ホスト権威）＋自己完結ハーネスで実施：

- 新3レコード検証：synopsis 245/216/224字（150-250内）・半角混入0（全角のみ・east_asian_width 検査）・
  全タグ既存99内・新タグ0・JSON 妥当
- 出典検証（Web）：s077＝雑宝蔵経（T203）巻第一 第7話「慈童女縁」。s078＝同巻第一の老母
  迦旦遮羅（過去五百生の母・抱仏・後に出家し阿羅漢）。s079＝テーリーガーター（長老尼偈）
  51-53偈 ウッビリー（娘ジーヴァー・八万四千・胸の矢）
- 執筆時是正2件：①タグ「慈愛」は motifs.json 側の軸語彙で setsuwa 99語彙外＝ハーネスが検出し
  「慈悲」に差替（新タグ0 維持）。②s077 synopsis 253字→245字に短縮（150-250 規約）
- 非凄惨基準：s077 の地獄・鉄輪は目連救母（s007）先例内（贖いと転換が主眼）。
  獄卒に打たれる最期の描写は synopsis に含めない

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.13＋spec §20＋push4（count79）＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count79）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋更新済 commit_message_setsuwa_sync.txt
   を commit+push（「Nothing to commit」は既コミット済のサイン＝正常）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：両 HEAD の setsuwa.json を git show で parse し count 79・s077-079 反映・
   SHA-256 一致を確認

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・.bat を truncate/stale 表示する既知 phantom。
  整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- **タグは setsuwa の99語彙（setsuwa.json 実データ由来）で照合すること。motifs.json 側の
  軸語彙（慈愛・孝心 等）と混同しない**（今回「慈愛」で検出＝ハーネスの新タグ0チェックが機能）。
- 選定基準：葬送向き・非凄惨・自死不採用。地獄描写は目連救母（s007）・慈童女（s077）の先例＝
  贖い・転換が主眼なら synopsis の書き方で基準内に収める。

## 次にやること

- 任意：picker に「縁起・因縁・つながり → ご縁・支え合い・人生の実相」のキーワード対応を追加
  （SETSUWA_THEME_KEYWORDS・要ホスト tsc）。
- (c') さらなる拡充（任意）。v1.13 で親の恩3・親の愛2・悲しみの受容3・癒し2 に補強。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。

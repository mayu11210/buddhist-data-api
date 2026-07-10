# handoff: 説話ライブラリ v1.12（立ち直り・自立・今を生きる系 拡充・5話）

**日付**：2026-07-10（v1.11＝b29bb53 の後続）
**着手時 HEAD**：倉庫 b29bb53／kaimyo-app 07fa16b（いずれも push 済・71話 SHA 一致 IDENTICAL 確認済）
**種別**：setsuwa.json コンテンツ拡充（5話・count 71→76）。motifs/corpus/7カテゴリ索引・20軸統制語彙は不変・新タグ0
**方針裁定**：ケンシン（2026-07-10）＝薄い軸補強の5候補を提示し「5話すべて採用」の裁定

## 経緯

残タスク (c') の第8弾。相対的にまだ薄めだった軸（A19 立ち直り改心＝4・A03 自立中道＝5・
A20 今を生きる＝5）を補強する5話。すべて初期経典系（early）。既存99タグ内・新タグ0で表現
（picker 無改修）。

## 成果物

### buddhist-data-api（変更3＋新規1）
- **data/indices/setsuwa.json**：count 71→76・description 76話
  - s072 難陀（ナンダ）の道心 増一阿含経ほか／パーリ ウダーナ3.2・early
    tags=改心／立ち直り／執着を離れる／方便／導き（A19/A13/A18）
  - s073 掃除人スニータの出家 長老偈620-631偈・early
    tags=再生／立ち直り／平等の恵み／自分の足で歩む／気づき（A19/A16/A03/A17）
  - s074 中道の教え（初転法輪）相応部 転法輪経 SN56.11／漢訳 雑阿含経379経・early
    tags=中道／自分の歩幅／歩み／導き（A03/A02/A18）
  - s075 自らを頼りとせよ（法句経百六十偈）法句経160偈＝クマーラカッサパの母の因縁・early
    tags=自立／自分の足で歩む／手放す／親子の絆／心の持ち方（A03/A13/A09/A06）
  - s076 一日の生（法句経百十偈）法句経110-112偈＝沙弥サンキッチャの因縁・early
    tags=一日を大切に／今を生きる／精進／善き行い（A20/A11/A12）
  - 既存99タグ内・新タグ0＝被覆99/99 維持・軸追加なし
- **_dev_references/setsuwa_tag_axes_v1.md**：§19「立ち直り・自立・今を生きる系の拡充（v1.12）」・対象を76話へ
- **push4_sync_setsuwa.bat**：count guard 71→76
- **handoff_2026-07-10_setsuwa_expand_v1_12.md**（本ファイル）

### kaimyo-app（変更2＝データ＋同期メッセージ）
- **data/indices/setsuwa.json**：倉庫 v1.12 から同期（76話・push4 が実施）
- **commit_message_setsuwa_sync.txt**：v1.12/76話 に更新（ラベルずれ再発防止・先回り更新）
- **lib/warehouse.ts・lib/setsuwa-picker.ts はコード変更なし**（新タグ0・canon 既存枠・すべて early）

## 検証（ホスト権威）

⚠️ setsuwa.json・spec doc・.bat とも sandbox mount stale/truncate 表示の既知 phantom。Read ツール
（ホスト権威）＋自己完結ハーネスで実施：

- 新5レコード fragment 単体 JSON 検証：synopsis 203/201/202/204/200字（150-250内）・
  半角混入0（全角のみ・east_asian_width 検査）・全タグ既存99内・新タグ0・JSON 妥当・
  count/id 76・重複0・軸カウント A19 6／A03 8／A20 6
- 出典検証（Web）：s072＝難陀（孫陀羅難陀）増一阿含・ウダーナ3.2（妻への執着→方便→悟り）。
  s073＝スニータ長老 Theragāthā 620-631（掃除人→阿羅漢・平等）。s074＝転法輪経 SN56.11／
  雑阿含379（二辺を離れた中道）。s075＝法句経160偈 attā hi attano nātho（因縁＝クマーラカッサパの母）。
  s076＝法句経110-112偈（一日の生）。**112偈の因縁サッパダーサは自死未遂を含むため不採用**＝
  110偈側サンキッチャ（盗賊の頭領の改心）を採用。s072 の地獄描写は synopsis に含めず（非凄惨基準）
- Edit 後：count 76・description 76話・s071 は `},` で閉じ s072-076 挿入・s076 末尾カンマなし・
  配列 `]`＋オブジェクト `}` 健全

## コミット手順（ケンシン）

1. **倉庫** `commit_push.bat`：setsuwa.json v1.12＋spec §19＋push4（count76）＋本 handoff＋
   更新済 commit_message.txt を commit+push
2. **倉庫** `push4_sync_setsuwa.bat`：HEAD（count76）の setsuwa.json を kaimyo-app へ同期＋SHA 照合
3. **kaimyo-app** `commit_setsuwa_sync.bat`：同期済 setsuwa.json＋更新済 commit_message_setsuwa_sync.txt
   を commit+push（「Nothing to commit」は既コミット済のサイン＝正常）
4. コミット順序厳守：倉庫 commit_push → push4 同期 → kaimyo commit
5. push 後の最終検証：両 HEAD の setsuwa.json を git show で parse し count 76・s072-076 反映・
   SHA-256 一致を確認

## 落とし穴メモ

- sandbox mount は setsuwa.json・spec doc・.bat を truncate/stale 表示する既知 phantom。
  整合は Read＋git show HEAD＋SHA-256（object store 権威）で行う。commit_push を複数回回すと
  2回目以降は「nothing added to commit」＝既にコミット済のサイン（実害なし）。
- setsuwa.json の改変は Edit ツール（ホスト権威）のみ。bash read-modify-write 禁止。
- 選定基準：葬送向きの穏やかなトーン・凄惨な描写や自死を含む伝承は不採用（因縁譚レベルでも適用＝
  今回の112偈因縁の不採用が前例）。

## 次にやること

- 任意：picker に「縁起・因縁・つながり → ご縁・支え合い・人生の実相」のキーワード対応を追加
  （SETSUWA_THEME_KEYWORDS・新タグ0のまま・要ホスト tsc）。
- (c') さらなる拡充（任意）。v1.12 で20軸すべて5話以上に到達（最薄は A20 の6話ほか）。
- (d) 新著作の取込（Phase 1〜・kakikudashi-data スキル）。

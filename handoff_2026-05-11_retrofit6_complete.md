# 引き継ぎメモ：retrofit 6 完走〔大日経三句法門連動 retrofit〕

**日付**：2026-05-11
**フェーズ**：retrofit 6（retrofit 5 完走に続く第三の retrofit セッション）
**対象**：大日経 住心品「三句法門」の連動 retrofit〔新規 sg07 + 連動 anchor m713〕
**ステータス**：完走〔Phase A 軸設計合意・Phase B 7 motif 判定・Phase C 本体反映＋補注 F 追加＋CLAUDE.md 更新・整合性検証 全 pass〕
**次フェーズ**：retrofit 7 候補〔般若心経 色即是空連動／吽字義 阿字本不生連動〕／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 等から選択

---

## (a) 本セッションの位置づけ

2026-05-11 の Phase 4 W2 本体マージセッション完走〔commit `6ef4992`〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit `7c85b6f`〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit `2f2b858`〕に続く第三の retrofit セッションとして実施。

retrofit 6 の主旨は、retrofit 5 で新設した連動軸を、即身成仏義 sg03/m533 連動に続いて **大日経 住心品「三句法門」連動** に拡張すること。大日経 住心品の中核思想「菩提心為因・大悲為根・方便為究竟」と思想的に強く連動する 7 motif を横断検索可能なタグで紐づけ、kaimyo-app 等の利用側で「三句法門連動 motif」を一括取得できる基盤を整備する。

ケンシン裁定で以下三案を採用：

- **判断 1**：連動基準成句の指定方式 → **案 a 採用**〔sg07 新設「菩提心為因、大悲為根、方便為究竟」＋ m713 anchor〕。retrofit 5 と完全対称の漢文成句／書き下し双軸構造を保つ。
- **判断 2**：対象 motif → 7 件付与〔m565/m637/m714/m715/m716/m723/m724〕・m712〔§51-52 金剛手の三問・問題提起〕は除外〔retrofit 5 m698 と同型〕。
- **判断 3**：タグ値表記 → **案 a 採用**〔`連動:sg07` + `連動:m713`〕。retrofit 5 と同表記法。

Phase A〔軸設計合意〕・Phase B〔7 motif 判定〕・Phase C〔本体反映＋補注 F 追加＋CLAUDE.md 更新＋引き継ぎメモ作成〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

連動軸は retrofit 5 で既設のため、本 retrofit では新規軸は導入せず、既存軸内のタグ値追加のみ。

**追加成句：sg07**

| 項目 | 値 |
|---|---|
| id | `sg07` |
| text_kakikudashi | 菩提心為因、大悲為根、方便為究竟〔16 字〕 |
| text_gendaigoyaku | 菩提心を因と為し、大悲を根と為し、方便を究竟と為す。〔26 字〕 |
| source.type | 成句 |
| source.出典_ref | 大日経 |
| tags（12 値） | `category:密教教学`・`成句:famous`・`主題:三句法門`・`主題:菩提心`・`主題:大悲`・`主題:方便`・`出典:大日経`・`出典:住心品`・`引用形式:経曰く`・`一句性:核心`・`密教:大日`・`含意:全人生` |

text_gendai_gabun は未設定〔sg01-sg06 と同様に儀礼朗誦の伝統で漢文成句のまま使うため〕。

**追加連動タグ値**

| タグ値 | 連動先 | 位置づけ |
|---|---|---|
| `連動:sg07` | sg07「菩提心為因、大悲為根、方便為究竟」（大日経 住心品出典の漢文成句） | 三句法門の最有名の決まり文句 |
| `連動:m713` | m713（大日経疏 §53「菩提心を因とし、大悲を根とし、方便を究竟とす…」） | sg07 の書き下し総説・三句法門の核心解釈 |

### Phase B：7 motif の連動判定表

| m-id | 出典 | 既存連動 | 追加タグ | 判定根拠 |
|---|---|---|---|---|
| m565 | 吽字義 第三節 | - | 連動:sg07・連動:m713 | 「大日経・金剛頂経…菩提を因とし、大悲を根とし、方便を究竟となすの三句に過ぎず」と直接引用・他著作からの核心句 |
| m637 | 秘蔵宝鑰 第八住心 一道無為心 第二節 | - | 連動:sg07・連動:m713 | `主題:三句法門` 既付与・法華三昧と三句法門を結ぶ秘蔵宝鑰の章 |
| m714 | 大日経疏 §54-55 因論 | - | 連動:sg07・連動:m713 | 三句の「因」節〔菩提心〕の本格解釈・白浄信心・家中宝蔵譬 |
| m715 | 大日経疏 §56 大悲根論 | - | 連動:sg07・連動:m713 | 三句の「根」節〔大悲〕の本格解釈・迦盧拏・三力加持・大悲五大 |
| m716 | 大日経疏 §57 方便究竟論 | - | 連動:sg07・連動:m713 | 三句の「究竟」節〔方便〕の本格解釈・醍醐妙果・三密の源・真金錬冶譬 |
| m723 | 大日経疏 §68-69 浄菩提心門 | - | 連動:sg07・連動:m713 | 三句の結論的展開〔三種無二・悲根方便波羅蜜〕 |
| m724 | 大日経疏 §70 三句の大宗 | 連動:sg03・連動:m533 | 連動:sg07・連動:m713 を追加 | 三句法門の総結・既存連動と並列で二軸連動に到達 |

**除外判定**：m712〔§51-52 金剛手の三問〔何因・云何根・云何究竟〕〕は問題提起部分のため除外。retrofit 5 m698〔§31 執金剛秘密主の問・三問〕と同型と判定。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 750 | 751 | +1 |
| famous_phrases | 6 | 7 | +1 |
| ファイルサイズ | 2,587,778 bytes | 2,589,594 bytes | +1,816 |
| kakikudashi_chars_total | 112,756 | 112,772 | +16 |
| gendaigoyaku_chars_total | 305,726 | 305,752 | +26 |
| gendai_gabun_chars_total | 154,931 | 154,931 | 0〔sg07 は雅文体訳未設定〕 |
| motifs_with_gendai_gabun | 743 | 743 | 0 |
| 連動タグを持つ motif | 4 | 11〔+7〕／うち m724 は二軸連動 | +14 タグ |
| schema_history 件数 | 63 | 64 | +1 |
| 篇別内訳 `成句_六件` | sg01-sg06 | `成句_七件` sg01-sg07 | キー変更 |

**整合性検証〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 751 vs 751 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 7 motif 連動タグ付与 | missing=[] ✓ |
| 7 | sg07 存在 | ✓ |
| 8 | m724 二軸連動 | sg03・m533・sg07・m713 all True ✓ |

### Phase D：補注 F 追加・CLAUDE.md 更新

- `_dev_references/motifs_index_design.md` §2 に補注 F〔大日経三句法門連動の運用〕新規追加〔36,773→41,121 bytes・+4,348 bytes〕。新規 sg07 entry の構造表・追加連動タグ値表・retrofit 6 実施結果・設計上の論点〔二軸連動の運用／問題提起 motif の除外原則／本 retrofit による横断性の達成〕を明文化。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 6 完走エントリを追加〔198,607→202,603 bytes・+3,996 bytes〕。retrofit 5 エントリは保全。

### 設計上の新規ポイント

#### (i) 二軸連動の実現

m724〔大日経疏 §70 三句の大宗〕は本 retrofit で：

- **既存**：`連動:sg03`〔即身成仏義「父母所生身、速証大覚位」〕・`連動:m533`〔同 書き下し〕
- **追加**：`連動:sg07`〔大日経 三句法門「菩提心為因、大悲為根、方便為究竟」〕・`連動:m713`〔大日経疏 §53 総説〕

の **四つの連動タグ** を持つ。これは「同一 motif が複数の中心成句に対する根拠句として機能する」運用が schema 0.2 で問題なく実現できることを実証した。今後も中心成句の追加に伴い、横断的な参照が拡張可能。

#### (ii) sg07 における出典の二段表記

sg07 の出典は、retrofit 5 の sg03〔即身成仏義〕と異なり、**経典名（大日経）と章名（住心品）の二段** で表記〔`出典:大日経` + `出典:住心品`〕。retrofit 5 は空海の著作出典で完結したが、本 retrofit は経典出典のため、章レベルの粒度を保持する設計に到達。今後の経典系成句追加〔般若心経・法華経 等〕にも本表記法を踏襲する。

#### (iii) 問題提起 motif 除外原則の継続適用

m712〔§51-52 金剛手の三問〕は retrofit 5 の m698〔§31 三問〕除外と同型の判断で除外。`主題:三句法門` タグは付与済〔テーマ検索には反応〕だが、`連動:` タグは付与しない。これにより kaimyo-app の検索意図「○○連動 motif を集める」におけるノイズを継続的に回避できる。

#### (iv) Edit tool truncate 回避方針の継続実証

retrofit 5 で確立した「長文編集は Python script による in-memory 編集 + write back」方針を本 retrofit でも継続適用〔CLAUDE.md・motifs_index_design.md・motifs.json すべて Python script 経由〕。Edit tool truncate 事象は本 retrofit では発生せず、方針の有効性が再確認された。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 7〔他著作の連動軸拡張〕

retrofit 5 handoff §(c) で示された残りのサブ候補：

- **般若心経 色即是空連動**：sg02「色即是空」と般若心経秘鍵〔m491-m505〕・大日経疏の関連 motif〔即色実相・本不生関連〕を紐づけ。規模 5〜8 motif 程度。
- **吽字義 阿字本不生連動**：吽字義の核心句〔m549-m566 のうち本不生関連〕と大日経疏の本不生関連 motif を紐づけ。規模 10 motif 前後。
- **その他の中心成句**：法華経諸法実相／華厳経一即一切／弁顕密二教論 顕密判 等への展開も可能。

retrofit 5・6 で確立した手順〔Phase A 軸設計合意 → Phase B 判定 → Phase C 反映 → Phase D 補注追加〕を踏襲して 1 セッション目安で進められる。

### 選択肢 B：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 C：kaimyo-app 教学系素材活用

本 retrofit で連動軸が二系統〔即身成仏 sg03 + 三句法門 sg07〕整備されたため、kaimyo-app 側で：

- 「連動:sg03」「連動:m533」を持つ 4 motif → 即身成仏連動素材プール
- 「連動:sg07」「連動:m713」を持つ 7 motif → 三句法門連動素材プール
- m724 を介した二軸横断〔即身成仏 ↔ 三句法門〕の素材選択ロジック
- 三教指帰の発言者軸〔retrofit 4〕と組み合わせた空海主体性の明確化

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 主題:三句法門 タグの整理

事前調査で判明した通り、`主題:三句法門` タグを持つ motif は 8 件〔m565/m637/m712/m713/m714/m715/m716/m723/m724〕。retrofit 6 では m713 を anchor とし、それ以外の 7 件に `連動:` タグを追加した。`主題:三句法門` タグは「テーマ検索用」、`連動:sg07`・`連動:m713` タグは「中心成句連動検索用」として明確に分離された。

### (d-2) sg-id 連番性の維持

sg07 を sg06 の直後〔index 100〕に挿入し、sg ブロックを一体保持。今後の sg 追加もこの慣例を踏襲する〔sg* は連番で motif 配列の中央に集約〕。

### (d-3) 出典:住心品 タグの新規導入

sg07 で `出典:住心品` タグを新規導入。今後、大日経 住心品出典の motif が増える場合、本タグで章レベルの横断検索が可能。経典系成句の章名タグ運用の最初の事例。

### (d-4) 本体 motifs.json のサイズ拡大

retrofit 6 で +1,816 bytes〔2,587,778 → 2,589,594 bytes〕。retrofit 5 〔+1,226〕・retrofit 4〔+1,525〕に続き 3 連続で +1,000〜2,000 bytes 規模の retrofit。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-5) gendai_gabun 字数管理

sg07 は gendai_gabun 未設定のため `motifs_with_gendai_gabun` は 743 維持〔成句は儀礼朗誦の伝統で漢文成句のまま使う方針〕。`motifs_without_gendai_gabun_intentional` のキーを `sg01-sg06` から `sg01-sg07` に更新して整合化。

### (d-6) ファイル truncate の予防継続

本 retrofit でも Python script による in-memory 編集 + write back 方針を継続。motifs.json・CLAUDE.md・motifs_index_design.md いずれも書き込み後の NUL バイト検証〔0 件確認〕とサイズ差確認を実施。Edit tool は使用せず。

### (d-7) commit_push.bat 安全装置の確認

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト・バックアップ・引き継ぎメモ〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md〕のみで、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔751 件・m1-m744 + sg01-sg07・2,589,594 bytes〕
- 本 retrofit build script：`outputs/retrofit6_three_sentences.py`〔dry-run + 本番適用の二段運用〕
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit6.json`〔retrofit 前 motifs.json・2,587,778 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit6.md`〔retrofit 前 motifs_index_design.md・36,773 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit6.md`〔retrofit 前 CLAUDE.md・198,607 bytes〕
- 前 retrofit handoff：`handoff_2026-05-11_retrofit5_complete.md`〔即身成仏義 sg03 連動〕
- 前々 retrofit handoff：`handoff_2026-05-11_retrofit4_complete.md`〔三教指帰 発言者軸〕
- W2 マージ handoff：`handoff_2026-05-11_w2_merge_complete.md`
- 補注 F 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 6 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit 7c85b6f〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit 2f2b858〕→ 同日 retrofit 6 完走〔大日経三句法門連動・新規 sg07 + 連動 anchor m713〕。本体 motifs.json は 751 件・2,589,594 bytes・schema_history 64 件。motifs_index_design.md §2 に補注 F 追加。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit6_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit5_complete.md`〔retrofit 5 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit4_complete.md`〔retrofit 4 完走サマリ〕
4. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
5. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E/F 含む〕
6. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・751 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。

【本セッションの選択肢】
(A) retrofit 7 候補〔般若心経 色即是空連動／吽字義 阿字本不生連動 等〕：連動軸の他著作拡張
(B) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(C) kaimyo-app 教学系素材活用：連動軸〔sg03/sg07〕を活用した戒名・諷誦文の組込
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避・本 retrofit でも継続実証〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 本体 motifs.json は 2,589,594 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-11〔retrofit 6 完走・大日経三句法門連動 retrofit・新規 sg07「菩提心為因、大悲為根、方便為究竟」と書き下し anchor m713〔大日経疏 §53 三句法門の総説〕の双軸を確立・7 motif〔m565/m637/m714/m715/m716/m723/m724〕に `連動:sg07`・`連動:m713` を付与〔+14 タグ〕・m712 除外・m724 二軸連動到達・schema 0.2 維持・整合性検証 8 項目全 pass・本体 motifs.json 2,589,594 bytes〔+1,816〕・schema_history 64 件〔+1〕・補注 F 追加〔motifs_index_design.md §2・36,773→41,121 bytes〕・CLAUDE.md 更新完了〔198,607→202,603 bytes〕〕

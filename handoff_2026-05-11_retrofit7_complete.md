# 引き継ぎメモ：retrofit 7 完走〔般若心経 色即是空連動 retrofit〕

**日付**：2026-05-11
**フェーズ**：retrofit 7（retrofit 6 完走に続く第四の retrofit セッション）
**対象**：般若心経「色即是空」連動 retrofit〔新規 sg-id 追加なし・既存 m630 を anchor 化〕
**ステータス**：完走〔Phase A 軸設計合意・Phase B 6 motif 判定・Phase C 本体反映＋補注 G 追加＋CLAUDE.md 更新・整合性検証 全 pass〕
**次フェーズ**：retrofit 8 候補〔吽字義 阿字本不生連動〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用／W2 repo 凍結手続 等から選択

---

## (a) 本セッションの位置づけ

2026-05-11 の Phase 4 W2 本体マージセッション完走〔commit `6ef4992`〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit `7c85b6f`〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit `2f2b858`〕→ 同日 retrofit 6 完走〔大日経三句法門連動・新規 sg07 + 連動 anchor m713・commit `ce9fe0f`〕に続く第四の retrofit セッションとして実施。

retrofit 7 の主旨は、retrofit 5・6 で確立した連動軸を、般若心経「色即是空」連動に拡張すること。本 retrofit は新規 sg-id・新規軸の追加を行わず、既存 sg02「色即是空」を成句 anchor、既存 motif m630〔秘蔵宝鑰 第七章 覚心不生心 第一節 大綱〕を書き下し anchor として採用する点で、retrofit 5・6 とは構造的に異なる初例となった。

ケンシン裁定で以下三案を採用：

- **判断 1**：書き下し anchor → **m630 採用**〔秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱〕。「色は空に異ならざれば…是の故に色即ち是れ空、空即ち是れ色なり」を含み、般若心経核心四句〔色不異空・空不異色・色即是空・空即是色〕の書き下し展開がすべて集約される最強の anchor。
- **判断 2**：対象規模 → **強連動 6 件のみ採用**〔m331/m499/m500/m631/m633/m634〕。中程度連動候補〔m318/m496/m498/m504/m510〕および本不生軸寄り候補〔m652/m684/m685/m702〕は本 retrofit ではスコープ外。
- **判断 3**：経証 motif 除外 → **m632/m635 除外**〔経文引用＋問題提起部分・retrofit 5 m698・retrofit 6 m712 と同型の判断〕。

Phase A〔軸設計合意〕・Phase B〔6 motif 判定〕・Phase C〔本体反映＋補注 G 追加＋CLAUDE.md 更新＋引き継ぎメモ作成〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

連動軸は retrofit 5 で既設のため、新規軸は導入せず。新規 sg-id も追加せず、anchor 構成のみで本 retrofit が成立した点が新規。

**anchor 構成**

| 項目 | 値 |
|---|---|
| 成句 anchor | `sg02`（既存・「色即是空」） |
| 書き下し anchor | `m630`（既存・秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱） |

**追加連動タグ値**

| タグ値 | 連動先 | 位置づけ |
|---|---|---|
| `連動:sg02` | sg02「色即是空」（般若心経出典の漢文成句） | 般若心経核心四句の最有名の決まり文句 |
| `連動:m630` | m630（秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱「色は空に異ならざれば…是の故に色即ち是れ空、空即ち是れ色なり…」） | sg02 を含む般若心経四句の書き下し展開・空海自身による般若空観の核心解釈 |

### Phase B：6 motif の連動判定表

| m-id | 出典 | 既存連動 | 追加タグ | 判定根拠 |
|---|---|---|---|---|
| m331 | 性霊集 idx=109 十喩を詠ずる詩・陽焔の喩 | - | 連動:sg02・連動:m630 | 「五蘊皆空は真実の法なり」+ 既存 典故:般若心経・典故:大品般若経 |
| m499 | 般若心経秘鍵 | - | 連動:sg02・連動:m630 | 「観人智慧を修して 深く五衆の空を照らす」五蘊皆空の書き下し展開 |
| m500 | 般若心経秘鍵 | - | 連動:sg02・連動:m630 | 「色空本より不二なり 事理元より来かた同なり」色空不二の核心句 |
| m631 | 秘蔵宝鑰 第七章 第一節 心王自在・南宗綱領 | - | 連動:sg02・連動:m630 | 「唯薀の無性に迷えるを悲しみ、他縁の境智を阻てたるを歎く」五蘊無自性の本格論 |
| m633 | 秘蔵宝鑰 第七章 第一節 八不中道 | - | 連動:sg02・連動:m630 | 「本不生とは兼ねて八種に通ず」中観八不論の核心 |
| m634 | 秘蔵宝鑰 第七章 第二節 頌 | - | 連動:sg02・連動:m630 | 「五韻 因縁生の法は、本より無性なり。空・仮・中道都べて不生なり」三観頌・五韻頌 |

**除外判定**：
- m632/m635〔秘蔵宝鑰 第七章 第一節 経証・第二節 経証（五重問答）〕：経文引用＋問題提起部分のため除外〔retrofit 5 m698・retrofit 6 m712 と同型〕
- m318/m496/m498/m504/m510〔中程度連動候補〕：本 retrofit ではスコープ外〔将来の拡張余地として温存〕
- m652/m684/m685/m702〔本不生軸寄り・主題:空 等の周辺連動〕：別軸として将来 retrofit 8〔吽字義 阿字本不生連動〕で扱う想定

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 751 | 751 | 0 |
| famous_phrases | 7 | 7 | 0 |
| ファイルサイズ | 2,589,594 bytes | 2,590,796 bytes | +1,202 |
| kakikudashi_chars_total | 112,772 | 112,772 | 0 |
| gendaigoyaku_chars_total | 305,752 | 305,752 | 0 |
| gendai_gabun_chars_total | 154,931 | 154,931 | 0 |
| motifs_with_gendai_gabun | 743 | 743 | 0 |
| 連動タグを持つ motif | 11 | 17〔+6〕 | +12 タグ |
| schema_history 件数 | 64 | 65 | +1 |

**整合性検証〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 751 vs 751 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 6 motif 連動タグ付与 | missing=[] ✓ |

### Phase D：補注 G 追加・CLAUDE.md 更新

- `_dev_references/motifs_index_design.md` §2 に補注 G〔般若心経 色即是空連動の運用〕新規追加〔41,121→47,028 bytes・+5,907 bytes〕。anchor 構成・追加連動タグ値表・retrofit 7 実施結果・設計上の論点 5 項目〔(i) 新規 sg-id 追加なしの初例／(ii) 本 retrofit による横断性の達成／(iii) 連動軸の三系統並立／(iv) 本不生連動軸との切り分け／(v) 問題提起 motif 除外原則の継続適用〕を明文化。補注 A-G 全 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 7 完走エントリを追加〔202,603→210,895 bytes・+8,292 bytes〕。retrofit 5・6 エントリは保全。半角括弧チェック open=5/close=5 でバランス確認。NUL バイト 0 件確認。

### 設計上の新規ポイント

#### (i) 新規 sg-id 追加なしの初例

retrofit 5 では新規軸『連動』の新設＋sg03/m533 を既存活用、retrofit 6 では新規 sg07 を新設＋m713 を既存活用してきた。本 retrofit 7 は **新規 sg-id・新規軸ともに追加なし** で、anchor 構成のみで成立した初例。sg02 が schema 0.2 当初から存在していたため可能となった。今後、既存 sg-id を中心成句として活用する連動 retrofit の参照モデル。

#### (ii) 既存 motif を書き下し anchor 化する設計

m630〔秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱〕は、空海自身による般若空観の核心解釈の本格論として、般若心経核心四句〔色不異空・空不異色・色即是空・空即是色〕の書き下し展開がすべて集約されている。これを anchor 化することで、kaimyo-app は「色即是空連動 motif」を求めて検索した際に、表層の漢文成句（sg02）だけでなく、その背後の論理的展開全体に到達可能となった。retrofit 6 の m713 と完全に対称な構造。

#### (iii) 連動軸の三系統並立

本 retrofit で連動軸は：

- **即身成仏 sg03/m533**〔retrofit 5・大日経疏 4 motif〕
- **三句法門 sg07/m713**〔retrofit 6・大日経疏 6 motif + 吽字義 1 + 秘蔵宝鑰 1 = 7 motif〕
- **色即是空 sg02/m630**〔retrofit 7・般若心経秘鍵 3 + 秘蔵宝鑰 3 + 性霊集 1 = 6 motif〕

の三系統が並立。kaimyo-app は中心成句別に素材プールを切替可能な基盤を備え、教学テーマに応じた素材選択ロジックを構築できる状態に到達した。

#### (iv) 本不生連動軸との切り分け

本 retrofit ではスコープ外とした m632/m635/m652/m684/m685 等は「主題:本不生」「主題:阿字」「密教:本不生」を持つ。これらは将来 retrofit 8 候補〔吽字義 阿字本不生連動〕として温存。「色即是空（般若空観）」と「阿字本不生（密教空観）」は思想的に隣接するが、anchor を切り分けることで kaimyo-app での検索意図「般若系空観 motif を集める」と「密教系本不生 motif を集める」を弁別可能にする設計に到達。

#### (v) 問題提起 motif 除外原則の継続適用

m632〔経証・大日尊が秘密主に告げる経文「自身の本不生を覚る」〕・m635〔経証・五重問答〕は retrofit 5 m698〔§31 三問〕・retrofit 6 m712〔§51-52 三問〕と同型の判断で除外。これにより kaimyo-app の検索意図「色即是空連動 motif を集める」におけるノイズを継続的に回避できる。

#### (vi) Edit tool truncate 回避方針の継続実証

retrofit 5・6 で確立した「長文編集は Python script による in-memory 編集 + write back」方針を本 retrofit でも継続適用〔motifs.json・motifs_index_design.md・CLAUDE.md すべて Python script 経由〕。Edit tool truncate 事象は本 retrofit では発生せず、方針の有効性が再確認された。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 8〔吽字義 阿字本不生連動〕

本 retrofit でスコープ外とした本不生軸寄りの候補を別軸として整備：

- 候補 motif：m652〔秘蔵宝鑰 第十章 菩提心論 阿字本不生・阿字五義・八葉白蓮頌〕／m632〔秘蔵宝鑰 第七章 第一節 経証「自身の本不生を覚る」〕／m633〔秘蔵宝鑰 第七章 第一節 八不中道「本不生とは兼ねて八種に通ず」〕／m635〔秘蔵宝鑰 第七章 第二節 経証〕／吽字義 m549-m566 の本不生関連 motif 群／大日経疏の本不生関連 motif。
- 規模 10 motif 前後・中規模。
- anchor 候補：吽字義の核心句から sg-id 新設するか、既存 motif を anchor 化するか。

retrofit 5・6・7 で確立した手順〔Phase A 軸設計合意 → Phase B 判定 → Phase C 反映 → Phase D 補注追加〕を踏襲して 1 セッション目安で進められる。

### 選択肢 B：retrofit 9 候補〔法華経諸法実相連動／華厳経一即一切連動 等〕

連動軸の他経典への拡張：

- 法華経諸法実相：「唯仏与仏乃能究尽諸法実相」〔法華経 方便品〕を anchor に、空海著作中の法華経関連 motif を紐づけ。
- 華厳経一即一切：「一即一切、一切即一」を anchor に、空海著作中の華厳経関連 motif を紐づけ。
- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用

本 retrofit で連動軸が三系統〔即身成仏 sg03 + 三句法門 sg07 + 色即是空 sg02〕整備されたため、kaimyo-app 側で：

- 「連動:sg02」「連動:m630」を持つ 6 motif → 般若・色即是空連動素材プール
- 「連動:sg03」「連動:m533」を持つ 4 motif → 即身成仏連動素材プール
- 「連動:sg07」「連動:m713」を持つ 7 motif → 三句法門連動素材プール
- m724 を介した二軸横断〔即身成仏 ↔ 三句法門〕の素材選択ロジック
- 三教指帰の発言者軸〔retrofit 4〕と組み合わせた空海主体性の明確化

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) sg02 の従来運用と連動軸付与の整合性

sg02〔「色即是空」〕は schema 0.2 当初から存在し、tags に `category:本来性`・`成句:famous`・`出典:般若心経`・`引用形式:経曰く`・`一句性:核心`・`主題:本来性`・`含意:全人生` の 7 値を持つ。本 retrofit では sg02 自体のタグは無変更〔anchor 化のみ〕で、連動先の 6 motif にのみ `連動:sg02`・`連動:m630` を付与した。これにより sg02 の従来運用は完全に保全。

### (d-2) m630 の anchor 適性

m630 は秘蔵宝鑰 第七章 覚心不生心 第一節 大綱で、空海が自身の十住心論の中で般若空観を本格的に論じる節。tags は既に `category:序論`・`category:典故引用`・`category:密教教学`・`主題:住心`・`主題:中観`・`主題:八不`・`主題:覚心不生`・`主題:空`・`主題:中道`・`主題:不二`・`文体:対句`・`文体:長句`・`引用形式:大師曰く`・`出典:秘蔵宝鑰`・`出典:巻の下 第七章 覚心不生心 第一節 大綱` の 15 値を持ち、本 retrofit でこれに `連動:sg02`・`連動:m630` を加えて 17 値となった。anchor 自体が連動先タグを持つことは retrofit 6 の m713 と同じ運用。

### (d-3) 性霊集 idx=109 十喩を詠ずる詩〔m331〕の取扱い

m331 は性霊集 第十巻「十喩を詠ずる詩」の陽焔の喩を含み、本文中に「五蘊皆空は真実の法なり」が明示的に登場する。既存の `典故:般若心経`・`典故:大品般若経` タグから般若系典故が確認できるため、本 retrofit で連動軸付与の対象に含めた。教学系著作〔般若心経秘鍵・秘蔵宝鑰〕に限らず、詩文系の motif も連動軸に取り込めることを実証。

### (d-4) m500 の特殊性

m500〔般若心経秘鍵〕の本文「色空本より不二なり 事理元より来かた同なり」は、般若心経の「色即是空・空即是色」を空海が偈頌形式で言い換えた典型例。`引用形式:大師曰く` が付与されていない〔偈頌のため〕が、思想的連動は最も直接的。

### (d-5) 本体 motifs.json のサイズ拡大

retrofit 7 で +1,202 bytes〔2,589,594 → 2,590,796 bytes〕。retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 4 連続で +1,000〜2,000 bytes 規模の retrofit。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-6) gendai_gabun 字数管理

本 retrofit は新規 motif 追加なし・タグ追加のみのため、`motifs_with_gendai_gabun` は 743 維持。gendai_gabun_chars_total も 154,931 維持。

### (d-7) ファイル truncate の予防継続

本 retrofit でも Python script による in-memory 編集 + write back 方針を継続。motifs.json・CLAUDE.md・motifs_index_design.md いずれも書き込み後の NUL バイト検証〔0 件確認〕とサイズ差確認、半角括弧バランス検証〔open=5/close=5〕を実施。Edit tool は使用せず。

### (d-8) commit_push.bat 安全装置の確認

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 3 件・バックアップ 3 件・引き継ぎメモ 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md〕のみで、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

### (d-9) commit_message.txt 更新漏れと訂正コミットの経緯

retrofit 7 の本体 commit〔`2d0d728`〕の commit message が、retrofit 6 の commit_message.txt の内容〔「retrofit 6 完走：大日経三句法門連動 retrofit〔新規 sg07 + 連動 anchor m713〕」〕のまま push された。Phase D で commit_message.txt を retrofit 7 用に書き換える手順を組み込んでいなかったことが原因。

経緯：

- 2d0d728：実体は retrofit 7 の変更〔handoff_2026-05-11_retrofit7_complete.md・outputs/CLAUDE_md_backup_pre_retrofit7.md・motifs_index_design_backup_pre_retrofit7.md・retrofit 7 適用後の motifs.json/CLAUDE.md/motifs_index_design.md〕を含むが、commit message が retrofit 6 のもの。データ整合性は問題なし。
- ケンシン裁定で選択肢 A〔追加 commit で訂正メモを残す〕を採用。履歴改変〔amend + force push〕は回避。
- 訂正コミット：commit_message.txt を「[訂正] retrofit 7 完走：般若心経 色即是空連動 retrofit〔前 commit 2d0d728 のメッセージ誤り訂正・実体は retrofit 7〕」で書き換え、本 handoff §(d-9) を追記して push。

再発防止策（次セッション以降のケンシン判断に委ねる選択肢）：

- CLAUDE.md の retrofit セッション運用手順 Phase D に「commit_message.txt を当該 retrofit 用に書き換える」を必須項目として明文化
- commit_push.bat の Step 5 で commit_message.txt の冒頭行が「今回作業の内容」と整合しているか軽い目視確認を実施
- handoff 作成時のテンプレに「commit_message.txt 更新確認」のチェック項目を追加

本訂正コミットで git log の見た目上の不整合を明示的に解消した。retrofit 8 以降では Phase D の commit_message.txt 更新を必須化する。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔751 件・m1-m744 + sg01-sg07・2,590,796 bytes〕
- 本 retrofit build script：`outputs/retrofit7_iroku_zekuu.py`〔dry-run + 本番適用の二段運用〕
- 補注 G 追加 script：`outputs/add_chunote_g_retrofit7.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit7.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit7.json`〔retrofit 前 motifs.json・2,589,594 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit7.md`〔retrofit 前 motifs_index_design.md・41,121 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit7.md`〔retrofit 前 CLAUDE.md・202,603 bytes〕
- 前 retrofit handoff：`handoff_2026-05-11_retrofit6_complete.md`〔大日経三句法門連動〕
- 前々 retrofit handoff：`handoff_2026-05-11_retrofit5_complete.md`〔即身成仏義 sg03 連動〕
- 前々々 retrofit handoff：`handoff_2026-05-11_retrofit4_complete.md`〔三教指帰 発言者軸〕
- W2 マージ handoff：`handoff_2026-05-11_w2_merge_complete.md`
- 補注 G 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 7 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit 7c85b6f〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit 2f2b858〕→ 同日 retrofit 6 完走〔大日経三句法門連動・新規 sg07 + 連動 anchor m713・commit ce9fe0f〕→ 同日 retrofit 7 完走〔般若心経 色即是空連動・既存 sg02/m630 を anchor 化〕。本体 motifs.json は 751 件・2,590,796 bytes・schema_history 65 件。motifs_index_design.md §2 に補注 G 追加〔補注 A-G 全 intact〕。連動軸は〔即身成仏 sg03/m533〕〔三句法門 sg07/m713〕〔色即是空 sg02/m630〕の三系統並立に到達。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit7_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit6_complete.md`〔retrofit 6 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit5_complete.md`〔retrofit 5 完走サマリ〕
4. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
5. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E/F/G 含む〕
6. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・751 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 7 commit です。

【本セッションの選択肢】
(A) retrofit 8 候補〔吽字義 阿字本不生連動〕：本不生連動軸の整備
(B) retrofit 9 候補〔法華経諸法実相／華厳経一即一切／弁顕密二教論 顕密判 等〕：連動軸の他経典拡張
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸三系統〔sg02/sg03/sg07〕を活用した戒名・諷誦文の組込
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避・本 retrofit でも継続実証〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 本体 motifs.json は 2,590,796 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-11〔retrofit 7 完走・般若心経 色即是空連動 retrofit・既存 sg02「色即是空」を成句 anchor、既存 m630〔秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱〕を書き下し anchor として採用・6 motif〔m331/m499/m500/m631/m633/m634〕に `連動:sg02`・`連動:m630` を付与〔+12 タグ〕・m632/m635 除外・新規 sg-id 追加なしの初例・schema 0.2 維持・整合性検証 6 項目全 pass・本体 motifs.json 2,590,796 bytes〔+1,202〕・schema_history 65 件〔+1〕・補注 G 追加〔motifs_index_design.md §2・41,121→47,028 bytes〕・CLAUDE.md 更新完了〔202,603→210,895 bytes〕・連動軸三系統並立〔即身成仏 sg03 + 三句法門 sg07 + 色即是空 sg02〕に到達〕

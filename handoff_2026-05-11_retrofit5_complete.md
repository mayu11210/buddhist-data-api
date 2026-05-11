# 引き継ぎメモ：retrofit 5 完走〔即身成仏義 sg03 連動 retrofit〕

**日付**：2026-05-11
**フェーズ**：retrofit 5（W2 マージ・retrofit 4 完走に続く後処理セッション）
**対象**：大日経疏 巻第一の 4 motif〔m724/m729/m733/m740〕に sg03/m533 連動タグを付与
**ステータス**：完走〔Phase A 軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋補注 E 追加＋CLAUDE.md 更新・整合性検証 全 pass〕
**次フェーズ**：W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用／W2 repo 凍結手続 等から選択

---

## (a) 本セッションの位置づけ

2026-05-11 の Phase 4 W2 本体マージセッション完走〔commit `6ef4992`・本体 750 motifs 到達〕→ 同日 retrofit 4 完走〔三教指帰 m656-m676 21 motif 発言者軸新設〕に続く第二の retrofit セッションとして実施。

retrofit 5 の主旨は、即身成仏義の中心成句〔sg03「父母所生身、速証大覚位」漢文成句／m533 同 第一節書き下し形〕と思想的に強く連動する大日経疏 巻第一の motif を、横断検索可能なタグで紐づけること。kaimyo-app 等の利用側で「即身成仏連動 motif」を一括取得できる基盤を整備する。

ケンシン裁定で以下三案を採用：

- 連動基準成句：sg03 + m533〔handoff の「sg06」は誤記と判定して訂正〕
- m698 取扱：除外〔§31 三問・問題提起部分のため〕
- 軸名：『連動』〔最短・中立・汎用的〕

Phase A〔軸設計合意〕・Phase B〔4 motif 判定〕・Phase C〔本体反映＋補注 E 追加＋CLAUDE.md 更新＋引き継ぎメモ作成〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

新規軸『連動』を schema 0.2 に追加〔軸新設は workshop_protocol §5 通り本体マージ・retrofit セッションで合意〕。

**連動軸の値（2 種・初期）**：

| タグ値 | 連動先 | 位置づけ |
|---|---|---|
| `連動:sg03` | sg03「父母所生身、速証大覚位」（即身成仏義出典の漢文成句） | 即身成仏義の最有名の決まり文句 |
| `連動:m533` | m533（即身成仏義 第一節書き下し「もし人仏慧を求めて、菩提心に通達すれば、父母所生の身に、速に大覚の位を証す」） | sg03 の書き下し形・空海が即身成仏義の核心典拠とした八箇の証文の最後 |

### Phase B：4 motif の連動判定表

| m-id | 章節 | 即身成仏との関係 | 追加タグ |
|---|---|---|---|
| m724 | §70 三句の大宗・浄菩提心開示の完結 | 即身成仏の論理的前提〔菩提心を因・大悲を根・方便を究竟〕 | 連動:sg03・連動:m533 |
| m729 | §80 諸仏菩薩同等住・浄月十五日譬 | 「行人は位大覚に同じ」＝即身成仏の譬喩 | 連動:sg03・連動:m533 |
| m733 | §84-85 龍樹冶人譬・初発心時即仏 | 「初発心の時、すなわち仏と名づく」＝sg03 の直接的根拠句 | 連動:sg03・連動:m533 |
| m740 | §92 五通仙人薬物錬冶譬・神変加持 | 「神変加持不思議の業を成ずる」＝即身成仏の方便論 | 連動:sg03・連動:m533 |

**除外判定**：m698〔§31 執金剛秘密主の問・三問〔因・根・究竟〕〕は問題提起部分のため除外。tags に `主題:加持身` あるが、間接連動のため軸スコープ外と判断〔kaimyo-app での即身成仏連動検索時のノイズ回避〕。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 750 | 750 | 0 |
| ファイルサイズ | 2,586,552 bytes | 2,587,778 bytes | +1,226 |
| 4 motif タグ追加 | - | - | +8 タグ |
| schema_history 件数 | 62 | 63 | +1 |
| 連動軸を持つ motif | 0 | 4 | +4 |

**整合性検証〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 750 vs 750 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 4 motif 連動タグ付与 | missing=[] ✓ |

### Phase D：補注 E 追加・CLAUDE.md 更新

- `_dev_references/motifs_index_design.md` §2 に補注 E〔成句連動の motif 識別タグ運用〕新規追加。連動軸の定義・運用ルール 5 項目・将来展開可能性〔大日経三句法門・般若心経色即是空 等への転用〕を明文化。
- 本体 CLAUDE.md：着手前に git HEAD から復元〔ワーキングディレクトリの CLAUDE.md は前回セッションの Edit tool truncate により末尾切断状態で 190,174 bytes・正常版は HEAD の 192,824 bytes〕。タイトル行と最終更新行の両方に retrofit 5 完走エントリを追加〔192,824→198,607 bytes・+5,783 bytes〕。

### 設計上の新規ポイント

#### (i) handoff 誤記の発見と訂正

前セッション handoff〔W2 マージ完走サマリ・retrofit 4 完走サマリ〕に「即身成仏義 sg06 連動」と記載されていたが、本セッション初手の事実確認で以下を判明：

- sg06 の本体内容は「我則金剛、我則法界」〔性霊集 idx=72 智泉達嚫の文出典の別系統成句〕
- 即身成仏義出典の「父母所生身、速証大覚位」は実は **sg03**〔成句:famous・引用形式:大師曰く 付き〕
- handoff の「sg06」は単純な取り違え誤記と判定

CLAUDE.md 原則 11「ラベルより内容を信頼」を踏襲し、ケンシン裁定で正式に「sg03 + m533 を連動基準成句として採用」に訂正してから着手。

#### (ii) 連動軸の汎用性設計

軸名は『連動』〔最短・中立・汎用的〕を採用。タグ値は `連動:sg03` `連動:m533` のように本体既存 motif id を参照する形式。これにより：

- 将来、他著作の核心成句〔大日経三句法門・般若心経色即是空・法華経諸法実相 等〕への連動にも転用可能〔タグ値追加のみ・新規軸新設は不要〕
- sg* 以外の m-id 同士の連動にも適用可能

#### (iii) 「直接連動」と「間接連動」の線引き

m698 を除外する判断は、kaimyo-app での検索体験を直接想定したもの。「即身成仏連動 motif を集める」という検索意図に対し、問題提起や問いの motif が混じることのノイズ性を重視した。今後の連動軸付与時にも本原則を踏襲：

- **付与する**：中心成句の論理的根拠となる回答・譬喩・方便論
- **付与しない**：問題提起・対比対象の他思想・周辺的言及

#### (iv) Edit tool truncate の再発生確認と対処

前回セッションの CLAUDE.md 編集で truncate が再発生していたことが本セッションで判明〔ワーキングディレクトリ 190,174 bytes・HEAD 192,824 bytes・末尾文中切断〕。

教訓と対処：

- 本 retrofit でも CLAUDE.md・motifs.json の更新は **すべて Python script で in-memory 編集 + write back** 方針を踏襲〔retrofit 4 先例 outputs/retrofit4_speaker_axis.py を踏襲〕
- 着手前に必ず `wc -c` と `git diff --stat` で truncate の有無を確認すべき〔本セッションで実行・truncate 発見〕

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 B：kaimyo-app 教学系素材活用

本 retrofit で連動軸が整備されたため、kaimyo-app 側で：

- 「連動:sg03」「連動:m533」を持つ 4 motif を「即身成仏連動素材プール」として戒名・諷誦文・引導文の素材に組込
- sg03 + m533 + m724 + m729 + m733 + m740 の 6 motif を即身成仏義の縦割り教学体系として参照可能
- 三教指帰の発言者軸〔retrofit 4〕と組み合わせて、空海の主体性を明確にした素材選択ロジックを実装

### 選択肢 C：他著作の連動軸拡張〔将来の retrofit 候補〕

連動軸は汎用設計のため、他著作にも転用可能：

- **大日経 三句法門連動**：秘蔵宝鑰 第八住心 一道無為心〔m637・既に主題:三句法門 付与済〕・大日経疏 巻第一 §70〔m724〕を「連動:三句法門基準 motif」で紐づけ
- **般若心経 色即是空連動**：sg02「色即是空」と般若心経秘鍵・大日経疏の関連 motif を紐づけ
- **吽字義 阿字本不生連動**：吽字義の核心句 m549〜m566 と大日経疏の本不生関連 motif を紐づけ

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) CLAUDE.md の前回 truncate 状態

ワーキングディレクトリの CLAUDE.md が前回セッションの Edit tool truncate により 190,174 bytes〔正常版 192,824 bytes〕に切断されていた。本セッションで `git show HEAD:CLAUDE.md > CLAUDE.md` で復元してから retrofit 5 更新を適用。

教訓：CLAUDE.md ルール記載通り、着手前に必ず以下を実行する：

```bash
wc -c CLAUDE.md
git diff --stat CLAUDE.md
git log -1 -- CLAUDE.md
```

ワーキングと HEAD のサイズ差が顕著な場合〔本件は -2,650 bytes〕は truncate を疑う。

### (d-2) sg06 表記の混乱

handoff の「sg06」誤記は前々セッション〔W2 マージ完走サマリ〕でも記載されており、本 retrofit セッションが初めて訂正の機会となった。今後の handoff 作成時は：

- 成句 id を引用する場合、必ず本体 motifs.json で内容確認してから記載する
- 章節番号〔R23 §28 等〕も同様に本体側の節番号と整合確認する

### (d-3) 連動軸の値増加に伴うタグ数管理

連動軸の値は将来増加する〔大日経三句法門・般若心経色即是空 等〕。motifs.json のタグ総数管理〔stats.tag_distribution 等〕を将来追加する設計検討も視野に入る〔本セッションでは未実装〕。

### (d-4) 本体 motifs.json のサイズ拡大

retrofit 5 で +1,226 bytes〔2,586,552 → 2,587,778 bytes〕。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。巨大化対策〔分割保持・SQLite 移行〕の検討は別セッションに譲る。

### (d-5) schema_history の origin タグ継承

W2 マージ・retrofit 4 で導入した `origin` フィールドを retrofit 5 でも継承〔`origin: retrofit_5:doctrine`〕。本体側で workshop 由来・retrofit 由来エントリを識別可能に。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔750 件・m1-m744 + sg01-sg06・2,587,778 bytes〕
- 本 retrofit build script：`outputs/retrofit5_renkou_axis.py`〔dry-run + 本番適用の二段運用〕
- 本 retrofit CLAUDE.md update script：`outputs/update_claude_md_retrofit5.py`
- バックアップ：`outputs/motifs_backup_pre_retrofit5.json`〔retrofit 前 motifs.json〕／`outputs/CLAUDE_md_backup_pre_retrofit5.md`〔retrofit 前 CLAUDE.md〕
- 前 retrofit handoff：`handoff_2026-05-11_retrofit4_complete.md`
- 前マージ handoff：`handoff_2026-05-11_w2_merge_complete.md`
- 補注 E 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 5 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージセッション完走〔commit `6ef4992`・本体 750 motifs 到達〕→ 同日 retrofit 4 完走〔三教指帰 m656-m676 21 motif 発言者軸新設〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動 retrofit・大日経疏 巻第一 4 motif〔m724/m729/m733/m740〕に連動:sg03・連動:m533 を付与・新規軸『連動』を schema 0.2 に追加〕。本体 motifs.json は 750 件・2,587,778 bytes・schema_history 63 件。前 handoff の「sg06 連動」は「sg03 連動」の誤記と本セッションで判定し訂正。motifs_index_design.md §2 に補注 E 追加。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit5_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit4_complete.md`〔retrofit 4 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_w2_merge_complete.md`〔W2 マージ完走サマリ〕
4. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
5. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E 含む〕
6. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・750 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 5 commit〔ケンシン push 時点〕です。

【本セッションの選択肢】
(A) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(B) kaimyo-app 教学系素材活用：連動軸を活用した戒名・諷誦文の組込
(C) 他著作の連動軸拡張〔大日経三句法門・般若心経色即是空・吽字義阿字本不生 等〕：将来の retrofit 候補
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避・本 retrofit でも適用済〕
- CLAUDE.md は前回セッションで truncate された状態だったため本 retrofit で git HEAD から復元済。着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 本体 motifs.json は 2,587,778 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-11〔retrofit 5 完走・即身成仏義 sg03 連動 retrofit・大日経疏 巻第一 4 motif〔m724/m729/m733/m740〕に連動:sg03・連動:m533 を付与〔+8 タグ〕・新規軸『連動』を schema 0.2 に追加・schema 0.2 維持・整合性検証 6 項目 全 pass・本体 motifs.json 2,587,778 bytes〔+1,226〕・schema_history 63 件〔+1〕・補注 E 追加〔motifs_index_design.md §2〕・CLAUDE.md 更新完了〔192,824→198,607 bytes〕・前回 truncate 状態の CLAUDE.md は git HEAD から復元してから更新〕

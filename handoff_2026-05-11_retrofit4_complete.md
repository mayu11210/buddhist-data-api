# 引き継ぎメモ：retrofit 4 完走〔三教指帰 戯曲形式 発言主体識別タグ運用〕

**日付**：2026-05-11
**フェーズ**：retrofit 4（W2 マージ後の後処理セッション）
**対象**：三教指帰 m656-m676（21 motif）の戯曲形式 発言主体識別タグ運用
**ステータス**：完走〔Phase A 軸設計合意・Phase B 21 motif 判定・Phase C 本体反映・整合性検証 全 pass〕
**次フェーズ**：retrofit 5〔即身成仏義 sg06 連動 retrofit〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用 等から選択

---

## (a) 本セッションの位置づけ

2026-05-11 の Phase 4 W2 本体マージセッション完走〔commit `6ef4992`・本体 750 motifs 到達〕の後処理として、W2 マージ時に「対象判定が複数 motif にわたるため別途 retrofit セッションに譲る」と判断された retrofit 4 を実施。

retrofit 4 の主旨は、三教指帰の戯曲形式（亀毛先生・虚亡隠士・仮名乞児・蛭牙公子・兎角公・或人の対話劇）において、登場人物ごとに思想立場が異なるため、発言主体を識別するタグを整備すること。本体マージ時に確認された「category:大師御言葉 タグが虚亡隠士・亀毛先生の発言にも付与されている」誤運用も同時に清揃する。

ケンシン裁定で以下三案を採用：

- 軸設計：案 a〔新規軸『発言者』を新設・推奨〕
- タグ清揃：ハイ〔すべて清揃・推奨〕
- 混在 motif の扱い：仮名乞児主体のため category:大師御言葉・引用形式:大師曰く を保持〔推奨〕

Phase A〔軸設計合意〕・Phase B〔21 motif 判定〕・Phase C〔本体 motifs.json 反映＋補注 D 追加＋CLAUDE.md 更新＋引き継ぎメモ作成〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

新規軸『発言者』を schema 0.2 に追加〔軸新設は workshop_protocol §5 通り本体マージセッション=本 retrofit セッションで合意〕。

**発言者軸の値（7 種）**：

| タグ値 | 該当人物 | 位置づけ |
|---|---|---|
| `発言者:空海` | 弘法大師空海ご自身 | 自序・地の文の編者 |
| `発言者:仮名乞児` | けみょうこつじ | 仏教代表・空海の分身（架空人物） |
| `発言者:亀毛先生` | きもうせんせい | 儒教代表（架空人物） |
| `発言者:虚亡隠士` | きょもういんじ | 道教代表（架空人物） |
| `発言者:蛭牙公子` | しつがこうし | 教化対象青年（架空人物） |
| `発言者:兎角公` | とかくこう | 蛭牙の伯父・儒教側人物（架空人物） |
| `発言者:或人` | あるひと | 仮名乞児への問者（無名） |

### Phase B：21 motif の発言主体判定表

| m-id | 章節 | 発言主体 | 追加 | 除去 |
|---|---|---|---|---|
| m656 | 巻の上 自序 | 空海 | 発言者:空海 | - |
| m657 | 巻の上 §1 亀毛紹介 | 地の文 | 発言者:空海 | - |
| m658 | 巻の上 §2 賢愚 | 亀毛先生 | 発言者:亀毛先生 | - |
| m659 | 巻の上 §3 父母疾 | 亀毛先生 | 発言者:亀毛先生 | - |
| m660 | 巻の上 §4 孝徳忠義 | 亀毛先生 | 発言者:亀毛先生 | - |
| m661 | 巻の上 §5-6 偕老 | 亀毛先生＋蛭牙 | 発言者:亀毛先生・発言者:蛭牙公子 | - |
| m662 | 巻の中 §7-8 虚亡登場 | 虚亡隠士 | 発言者:虚亡隠士 | category:大師御言葉・引用形式:大師曰く |
| m663 | 巻の中 §8 不死神術 | 虚亡隠士 | 発言者:虚亡隠士 | category:大師御言葉・引用形式:大師曰く |
| m664 | 巻の中 §8 道学禁忌 | 虚亡隠士 | 発言者:虚亡隠士 | category:大師御言葉・引用形式:大師曰く |
| m665 | 巻の中 §9 霊宝密術 | 虚亡隠士 | 発言者:虚亡隠士 | category:大師御言葉・引用形式:大師曰く |
| m666 | 巻の中 §10 世俗批判 | 虚亡＋亀毛・蛭牙・兎角合同 | 発言者 4 値 | category:大師御言葉・引用形式:大師曰く |
| m667 | 巻の下 §11 仮名紹介 | 地の文 | 発言者:空海 | - |
| m668 | 巻の下 §12 或人問・仮名答 | 或人＋仮名乞児 | 発言者:或人・発言者:仮名乞児 | - |
| m669 | 巻の下 §13 大孝論 | 仮名乞児 | 発言者:仮名乞児 | - |
| m670 | 巻の下 §14 智剣弁泉 | 仮名乞児 | 発言者:仮名乞児 | - |
| m671 | 巻の下 §15 三界六趣 | 仮名乞児 | 発言者:仮名乞児 | - |
| m672 | 巻の下 §16 無常の賦 | 仮名乞児 | 発言者:仮名乞児 | - |
| m673 | 巻の下 §17-18 生死海 | 仮名乞児 | 発言者:仮名乞児 | - |
| m674 | 巻の下 §19 大菩提 | 仮名乞児 | 発言者:仮名乞児 | - |
| m675 | 巻の下 §20 廻心 | 亀毛公等廻心＋仮名乞児結語 | 発言者 5 値 | - |
| m676 | 巻の下 結偈 | 仮名乞児 | 発言者:仮名乞児 | - |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 750 | 750 | 0 |
| ファイルサイズ | 2,585,027 bytes | 2,586,552 bytes | +1,525 |
| 三教指帰 motif タグ数 | - | - | +30 / -10 |
| schema_history 件数 | 61 | 62 | +1 |
| 発言者軸を持つ motif | 0 | 21 | +21 |

**整合性検証〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | stats vs recompute 差分〔全 5 項目〕 | (0, 0, 0, 0, 0) ✓ |
| 2 | NUL バイト 0 件 | ✓ |
| 3 | m-id 連番性〔m1-m744〕 | missing=[] ✓ |
| 4 | 篇別内訳 全 dict 形式 | 67/67 ✓ |
| 5 | 新規挿入文字列の半角括弧 | 0 件 ✓ |
| 6 | schema_version 0.2 維持 | ✓ |

### Phase D：補注 D 追加・CLAUDE.md 更新

- `_dev_references/motifs_index_design.md` §2 に補注 D〔戯曲形式の発言主体識別タグ運用〕新規追加。発言者軸 7 値の定義・運用ルール 5 項目・将来の戯曲対話形式著作への展開可能性を明文化。
- 本体 CLAUDE.md 最終更新行に retrofit 4 完走エントリを追加。

### 設計上の新規ポイント

#### (i) 軸新設の運用先例〔発言者軸〕

W1 マージで導入された『主体』軸〔代筆書状の送信者識別〕に続き、retrofit 4 で『発言者』軸を新設。workshop_protocol §5 通り、新規軸は本体マージセッション〔retrofit セッションも含む〕で合意してから追加する原則を運用。schema_version は 0.2 維持〔フィールド構造変更なし・データ拡張のみ〕。

#### (ii) category:大師御言葉 の意味的純化

「弘法大師の御言葉」の意味で運用されていた本タグが、戯曲形式の他思想代表（亀毛先生・虚亡隠士）にも誤って付与されていた問題を清揃。kaimyo-app 等の利用側で「弘法大師の御言葉」として安全に引用可能な motif と、「対話相手の言葉」として識別される motif の区別が即座に利用可能に。

#### (iii) 混在 motif の処理原則

m666（虚亡隠士発言＋亀毛・蛭牙・兎角の合同改心）・m668（或人問＋仮名乞児答）・m675（亀毛公等廻心＋仮名乞児結語）のように 1 motif 内に複数発言者が登場する場合の処理原則：

- 発言者軸には登場する全員を付与
- category:大師御言葉・引用形式:大師曰く は「motif の主体・結論部」が仮名乞児 or 空海なら保持、対話相手主体なら除去
- m666 は虚亡隠士発言が中心〔末尾の合同改心は短い〕→ 除去
- m668・m675 は仮名乞児の応答・結語が中心〔他人物発言は導入〕→ 保持

将来の戯曲・対話形式著作への展開時に本原則を踏襲する。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 5〔即身成仏義 sg06 連動 retrofit〕

W2 マージ時に retrofit 4 と並んで「対象判定が複数 motif にわたるため別途」とされた retrofit 5。対象は即身成仏義 sg06「父母所生身、速証大覚位」と連動する教学系 motif〔m698・m724・m729・m733・m740 = 5 件〕。

実施事項：
- 連動タグの軸設計合意〔軸名候補：『連動』『連動成句』『関連成句』等〕
- 連動タグの運用ルール〔kaimyo-app での参照経路〕
- 該当 5 motif への付与

retrofit 4 と同じ Phase A・B・C 三段構造で進める〔1 セッション目安〕。

### 選択肢 B：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 C：kaimyo-app 教学系素材活用

本 retrofit で発言者軸が整備されたため、kaimyo-app 側で：

- 「発言者:仮名乞児」「発言者:空海」を持つ motif のみを「弘法大師の御言葉」として引用するロジック実装
- 三教指帰の戯曲形式素材を法話・戒名・諷誦文の導入素材として活用
- 即身成仏義 sg06 連動句・吽字義 阿字本不生・声字実相義 五大皆有響 等の戒名・諷誦文への組込

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) Edit tool 長文 truncate 事象は本セッションでは再現せず

W2 本体マージセッションでは Edit tool の長文 truncate 事象が再現発生したが、本 retrofit セッションでは Python script で in-memory 編集後 write back する方針〔outputs/retrofit4_speaker_axis.py 単独実装〕により完全回避。先例 merge_w2_into_body.py を踏襲した dry-run + 本番適用の二段運用が再び有効性を実証。

### (d-2) 半角括弧の予防

新規挿入文字列〔発言者:* タグ 7 値・schema_history retrofit_4 エントリ〕に半角括弧を含めない方針で執筆。Python script 内で予防的にカウント検証〔0 件確認〕。

### (d-3) 発言者軸の他著作への展開可能性

三教指帰に限らず、対話形式・問答形式で進行する他著作にも本軸を転用可能：
- 経典の対話パート〔阿難尊者・舎利弗・仏陀等の対話〕
- 論書の問答節〔大日経疏 巻第一 §85-88 の偈問偈答 等〕
- 性霊集の代筆書状〔形式上の発信者と代筆者の双方を発言者として記録する案も〕

将来該当 motif が発生した時点で本軸を付与し、補注 D 末尾に追加する。

### (d-4) 本体 motifs.json のサイズ拡大

retrofit 4 で +1,525 bytes〔2,585,027 → 2,586,552 bytes〕。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。巨大化対策〔分割保持・SQLite 移行〕の検討は別セッションに譲る。

### (d-5) schema_history の origin タグ

W2 マージで導入した `origin` フィールドを retrofit 4 でも継承〔`origin: retrofit_4:doctrine`〕。本体側で workshop 由来・retrofit 由来エントリを識別可能に。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔750 件・m1-m744 + sg01-sg06・2,586,552 bytes〕
- 本 retrofit build script：`outputs/retrofit4_speaker_axis.py`〔dry-run + 本番適用の二段運用〕
- バックアップ：`outputs/motifs_backup_pre_retrofit4.json`〔retrofit 前 motifs.json〕
- 前セッション handoff〔W2 本体マージ完走〕：`handoff_2026-05-11_w2_merge_complete.md`
- 補注 D 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 4 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージセッション完走〔commit `6ef4992`・本体 750 motifs 到達〕の後、同日中に retrofit 4 完走〔三教指帰 m656-m676 21 motif 発言者軸新設＋category:大師御言葉・引用形式:大師曰く 誤運用清揃〕。本体 motifs.json は 750 件・2,586,552 bytes・schema_history 62 件。新規軸『発言者』を schema 0.2 に追加〔軸新設は本体マージで合意の原則を運用〕。motifs_index_design.md §2 に補注 D 追加。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit4_complete.md`〔本 retrofit セッション完走サマリ〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_w2_merge_complete.md`〔W2 マージ完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・750 件〕

【本セッションの選択肢】
(A) retrofit 5〔即身成仏義 sg06 連動 retrofit・m698/m724/m729/m733/m740〕：連動タグの軸設計から
(B) W1 継続抽出〔buddhist-shoryoshu-workshop〕：性霊集 残 55 篇から motif 抽出
(C) kaimyo-app 教学系素材活用：発言者軸を活用した戒名・諷誦文の組込
(D) W2 repo 凍結手続：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避・本 retrofit でも適用済〕
- 軸新設は本体マージセッション〔retrofit セッション含む〕で合意の原則を厳守
```

---

最終更新：2026-05-11〔retrofit 4 完走・三教指帰 m656-m676 21 motif 発言者軸新設＋category:大師御言葉・引用形式:大師曰く 誤運用清揃・schema 0.2 維持・整合性検証 全 pass・本体 motifs.json 2,586,552 bytes・補注 D 追加・CLAUDE.md 更新完了〕

# 引き継ぎメモ：retrofit 14 完走〔法華経 見宝塔品 多宝塔連動 retrofit〕

**日付**：2026-05-12
**フェーズ**：retrofit 14（retrofit 13 完走に続く第十一の retrofit セッション）
**対象**：法華経 見宝塔品 多宝塔連動軸の新設。新規 sg-id `sg13`「多宝塔」を追加し、書き下し anchor として **m424 を単独採用**（性霊集 第八巻 idx=78 先師勤操表白・「多宝塔の中に帰し玉えるか」・性霊集中で「多宝塔」原語直接含有唯一例）。retrofit 10 sg09/m637 以来となる単独 anchor 体制の再採用例。連動軸が八系統 → 九系統並立に到達。法華経内部の **迹門四段（諸法実相＋三譬：火宅三車・良医病子・化城宝処）＋本門一段（多宝塔）= 五段構成** に到達。**法華経 本門の中心譬を初の独立軸化**（retrofit 10-13 は方便品＋迹門三譬の迹門中心構成）。**法華経 譬喩別軸 四譬完成体**〔火宅三車・良医病子・化城宝処・多宝塔〕に到達。
**ステータス**：完走〔Phase A 軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 N 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 15 候補〔法華経譬喩別軸（信解品 長者窮子 m717 温存／五百弟子授記品 衣裏珠／薬草喩品 三草二木／従地涌出品 地涌の菩薩 m222・m639 温存／薬王菩薩本事品 焼身供養）／弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸九系統 anchor 完全整合済〕等から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_14:doctrine〕
- [x] motifs_index_design.md に補注 N 追加済〔A-N 全 14 件 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 14 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-12_retrofit14_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 追加部分 全角括弧バランス確認〔commit_message.txt 〔16/16・（69/69〕〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

retrofit 13 完走〔法華経 化城喩品 化城宝処連動・新規 sg12 + 既存 m227/m569 を書き下し anchor 二重体制で採用・commit `8d40144`〕に続く第十一の retrofit セッション。

retrofit 13 完走 handoff §(c) 選択肢 A〔retrofit 14 候補：法華経譬喩別軸〕に着手。2026-05-12 にケンシン裁定で「見宝塔品 多宝塔軸」を選定し、判断 1-5 を 1 セッション内で連続裁定〔(1) 中心成句 = 多宝塔、(2) 単独 anchor m424、(3) 規模 anchor 1 + 強連動 3 = 4 motif、(4) 強連動 m637+m690+m262、(5) 補注 J 単独 anchor タグ運用継承〕。Phase A〜D を 1 commit にまとめて完走する方針で進行。

**本 retrofit の特徴**：

- 新規 sg-id `sg13`「多宝塔」を追加〔出典:法華経 見宝塔品「爾時仏前有七宝塔・従地涌出住在空中」「即時釈迦牟尼仏入其塔中坐其半座・結加趺坐」〕
- 書き下し anchor は **単独採用**：m424（性霊集 第八巻 idx=78 先師勤操表白・追慕弔辞独立譬）
- 強連動 4 motif（anchor 1 + 強連動 3）に「連動:sg13」「連動:m424」を付与（+8 タグ・補注 J 単独 anchor 運用継承）
- 法華経内部で迹門四段（諸法実相 sg09・火宅三車 sg10・良医病子 sg11・化城宝処 sg12）＋本門一段（多宝塔 sg13）の五段構成に到達
- 連動軸九系統並立に到達
- **法華経 本門の中心譬を初の独立軸化**：retrofit 10-13 は方便品＋迹門三譬の迹門中心構成だったが、本 retrofit で見宝塔品 多宝塔（本門 流通分）を初めて独立軸化
- **単独 anchor 体制の retrofit 10 以来の再採用例**：retrofit 11-13 で二重 anchor 体制が連続採用された後、本 retrofit で単独 anchor が再採用される
- **m637 二重所属の運用**：sg09 諸法実相 anchor と sg13 多宝塔強連動の二系統二重所属（retrofit 9 m713/m630 同型）

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg13 =「多宝塔」（3 字成句・retrofit 8-13 sg08-sg12 と同型の sg ID 連番運用）
- **判断 2**：書き下し anchor = m424 単独採用（案 A・retrofit 10 sg09/m637 同型）
- **判断 3**：規模 = anchor 1 + 強連動 3 = 4 motif（最小規模・retrofit 10 と同規模）
- **判断 4**：強連動 3 件 = m637（秘蔵宝鑰 巻の下 第八章 一道無為心 第二節）+ m690（大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現）+ m262（性霊集 第八巻 idx=76 三嶋大夫亡息女表白）
- **判断 5**：単独 anchor タグ運用 = 補注 J 案 A 単独版〔retrofit 10 と同型ルール継承・全 motif に「連動:sg13」「連動:m424」の 2 タグ付与〕

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

**判定対象 motif 候補**：

法華経 多宝塔関連 motif の分布把握：
- 「多宝塔」原語直接含有: 1 件（m424・性霊集中唯一例）
- 「多宝」原語直接含有: 3 件（m424, m262, m637）
- 「宝塔」原語直接含有: 5 件（m424, m262, m637, m690, sg09）
- 「見宝塔」直接含有: 3 件（m424, m262, m637）
- 「典故:法華経見宝塔品」系タグ保持 motif: 2 件（m424, m262）
- 「主題:多宝分身三世仏」タグ保持 motif: 1 件（m262）

候補 motif の整理：
- m424：性霊集 第八巻 idx=78 先師勤操表白・「多宝塔の中に帰し玉えるか」直接含有・既存タグ「典故:法華経見宝塔品」「場面:多宝塔帰」二重保持・**最有力 anchor 候補（追慕弔辞独立譬）・性霊集中で「多宝塔」原語含有唯一例**
- m262：性霊集 第八巻 idx=76 三嶋大夫亡息女表白・「多宝分身三世の仏」（廻向呼びかけ）・既存タグ「主題:多宝分身三世仏」「典故:法華経見宝塔品多宝」「場面:多宝分身」三重保持
- m637：秘蔵宝鑰 巻の下 第八章 一道無為心 第二節・「宝塔騰踊して二仏同座」（本門宝塔湧現論述・天台教判）・既存 sg09 諸法実相 anchor（既に 連動:sg07/m713・連動:sg09/m637 付与）
- m690：大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現・「法華の序分や従地湧出品の因縁の如し」（法華本門宝塔湧現と密教法界曼荼羅の対比論述）
- m222：性霊集 第六巻 idx=44 桓武皇帝奉為金字法華 達嚫・「踊出の瑞」（従地涌出品）・本 retrofit ではスコープ外（隣接品扱い・将来 retrofit 15 以降の従地涌出品軸候補に温存）
- m639：秘蔵宝鑰・「従地涌出・地涌」（隣接品）・本 retrofit ではスコープ外
- m717：大日経疏 §58 自心実知・「人の宝蔵を開いて」（宝所概念）・本 retrofit ではスコープ外（将来 retrofit 15 以降の信解品 長者窮子軸候補に温存）

判断 2 anchor 選定の三案：
- 案 A：m424 単独（多宝塔原語直接含有の唯一例・retrofit 10 sg09/m637 同型）
- 案 B：m424 + m262 二重（文体対比型・両方表白系・retrofit 12 sg11/m44+m70 同型）
- 案 C：m424 + m637 二重（系統対比型・表白系+秘蔵宝鑰天台教判系・retrofit 11/13 同型／m637 は既 sg09 anchor で三重所属）

ケンシン裁定で **案 A 単独 m424** を採用。理由：(1)「多宝塔」原語の kakikudashi 直接含有が性霊集中で m424 ただ 1 件、(2) m424 が「多宝塔の中に帰し玉えるか、当、鷲峯の窟の裏に還り玉うか」と独立した追慕弔辞譬として運用される唯一明確な性霊集例である点、(3) 残る候補（m637/m262/m690）はそれぞれ別系統の文脈に位置するため anchor として三重化するより強連動として運用する方が体系上明快である点、(4) 譬喩別軸の anchor 体制選択基準として「単独／二重 anchor は譬喩の典籍系統的分布に応じて柔軟に選択」の運用方針を再確認する意義。

### Phase B：4 motif の判定表

| m-id | 出典 | kakikudashi 多宝塔系 keyword 直接含有 | 既存連動タグ | 既存関連タグ（主要） | 系統 | 役割 | 採否 |
|---|---|---|---|---|---|---|---|
| m424 | 性霊集 第八巻 idx=78 先師勤操表白 | 「多宝塔の中に帰し玉えるか」（多宝塔 1 + 見宝塔品 1 直接含有） | なし | 典故:法華経見宝塔品・場面:多宝塔帰・故人:師・故人:僧侶 | 表白系（追慕弔辞・独立譬運用） | **anchor 単独** | **採用** |
| m637 | 秘蔵宝鑰 巻の下 第八章 一道無為心 第二節 | 「会三帰一して仏智の深多を讃し、指本遮末して成覚の久遠を談じ、宝塔騰踊して二仏同座し」（宝塔 2 + 見宝塔 1 + 多宝 1 多重直接含有） | 連動:sg07・連動:m713・連動:sg09・連動:m637 | 主題:三句法門・密教:初法明道・主題:法華三昧・主題:本来性 | 教学系（天台教判・秘蔵宝鑰） | 強連動（sg09 と二重所属） | **採用** |
| m690 | 大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現 | 「法華の序分や従地湧出品の因縁の如し」（宝塔 1 + 湧出 1 直接含有・本門宝塔湧現対比） | なし | 主題:加持身・主題:秘密荘厳・密教:曼荼羅・主題:即身成仏 | 教学系（大日経疏） | 強連動 | **採用** |
| m262 | 性霊集 第八巻 idx=76 三嶋大夫亡息女表白 | 「鷲峯海会の釈迦尊、多宝分身三世の仏」（多宝 1 + 見宝塔 1 直接含有） | なし | 主題:多宝分身三世仏・典故:法華経見宝塔品多宝・場面:多宝分身 | 表白系（廻向呼びかけ） | 強連動 | **採用** |
| m222 | 性霊集 第六巻 idx=44 桓武皇帝奉為金字法華 達嚫 | 「踊出の瑞」（従地涌出品） | なし | 典故:法華経従地涌出品・典故:法華経霊鷲山・場面:踊出瑞 | 達嚫系 | 隣接品 | スコープ外（従地涌出品軸候補） |
| m639 | 秘蔵宝鑰 | 「従地涌出・地涌」（隣接品） | なし | — | 教学系 | 隣接品 | スコープ外 |
| m717 | 大日経疏 §58 自心実知 | 「人の宝蔵を開いて」（宝所概念） | なし | 典故:法華経・典故:大日経 | 宝所概念系 | 温存 | スコープ外（信解品 長者窮子軸候補） |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 756 | 757 | +1（sg13 新規追加） |
| ファイルサイズ | 2,610,239 bytes | 2,614,532 bytes | +4,293 |
| 連動タグを持つ motif | 47 | 51 | +4（m424/m637/m690/m262 新規連動） |
| famous_phrases | 12 | 13 | +1（sg13 追加で recompute） |
| schema_history 件数 | 71 | 72 | +1 |
| kakikudashi_chars_total | 112,776 | 112,779 | +3（「多宝塔」3 字） |
| gendaigoyaku_chars_total | 306,427 | 307,059 | +632（sg13 description） |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 757 vs 757 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[], count=744 ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔4 motif + 各 2 タグ〕 | missing=[] ✓ |
| 7 | sg13 配列追加〔末尾 pos=756〕 | ✓ |

### Phase D：補注 N 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 N〔法華経 見宝塔品 多宝塔連動の運用〕新規追加〔100,507→115,100 bytes・+14,593 bytes〕。anchor 構成表（単独 anchor 体制・retrofit 10 sg09/m637 同型）・追加連動タグ値表・単独 anchor タグ運用ルール（補注 J 案 A 単独版継承）・anchor 体制選択基準表（単独／系統対比型／文体対比型の三型運用）・retrofit 14 実施結果・設計上の論点 8 項目〔(i) 単独 anchor 体制の retrofit 10 以来の再採用／(ii) 連動軸九系統並立／(iii) 法華経 譬喩別軸 四譬完成体／(iv) 法華経 本門の中心譬を初の独立軸化／(v) 二重所属の運用確立／(vi) kakikudashi 直接含有を客観基準とする継続／(vii) 譬喩別軸の今後の展開／(viii) schema_history origin タグの定着〕を明文化。補注 A-N 全 14 件 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 14 完走エントリを追加〔247,340→253,981 bytes・+6,641 bytes〕。retrofit 4-14 全エントリ intact 確認済。NUL バイト 0 件確認。
- `commit_message.txt` を retrofit 14 用に完全書き換え〔13,897 bytes・NUL 0・冒頭行整合確認済・全角括弧 〔16/16・（69/69〕。冒頭行を「retrofit 14 完走：法華経 見宝塔品 多宝塔連動 retrofit〔新規 sg13「多宝塔」+ 既存 m424 を書き下し anchor 単独採用・連動軸九系統並立に到達〕」として、Phase D 必須チェックリストに完全準拠。Python `write_bytes` 直接書き込み方式で作成。

### 設計上の新規ポイント

#### (i) 単独 anchor 体制の retrofit 10 以来の再採用

retrofit 10 sg09/m637 が初の単独 anchor、retrofit 11-13 で二重 anchor 体制が三例連続で確立（系統対比型 2 例・文体対比型 1 例）した後、本 retrofit で単独 anchor 体制が retrofit 10 以来 4 retrofit ぶりに再採用される。これにより譬喩別軸の anchor 体制は **「単独／二重 anchor は譬喩の典籍系統的分布に応じて柔軟に選択」** の運用方針が定着。一律の二重 anchor 化を強制しない柔軟運用基盤が確立。

#### (ii) 連動軸九系統並立に到達

本 retrofit で連動軸は以下の九系統が並立：

| 連動軸 | 成句 anchor | 書き下し anchor | 自己参照タグ | 確立 retrofit |
|---|---|---|---|---|
| 即身成仏 | sg03 | m533 | 連動:sg03・連動:m533 | retrofit 5 |
| 三句法門 | sg07 | m713 | 連動:sg07・連動:m713 | retrofit 6 → retrofit 9 で補完 |
| 色即是空 | sg02 | m630 | 連動:sg02・連動:m630 | retrofit 7 → retrofit 9 で補完 |
| 阿字本不生 | sg08 | m549 | 連動:sg08・連動:m549 | retrofit 8 |
| 諸法実相 | sg09 | m637 | 連動:sg09・連動:m637 | retrofit 10 |
| 火宅三車 | sg10 | m209 + m636（二重・系統対比型） | 連動:sg10・連動:m209・連動:m636 | retrofit 11 |
| 良医病子 | sg11 | m44 + m70（二重・文体対比型） | 連動:sg11・連動:m44・連動:m70 | retrofit 12 |
| 化城宝処 | sg12 | m227 + m569（二重・系統対比型） | 連動:sg12・連動:m227・連動:m569 | retrofit 13 |
| **多宝塔** | **sg13** | **m424（単独）** | **連動:sg13・連動:m424** | **retrofit 14（本 retrofit）** |

kaimyo-app は九つの教学テーマで素材プールを切替可能：即身成仏／菩薩道の三句／般若空観／密教空観／法華空観（諸法実相）／法華譬喩（火宅三車・三乗教判）／法華譬喩（良医病子・方便涅槃）／法華譬喩（化城宝処・方便引導／顕密二教判）／法華本門（多宝塔・本門宝塔湧現／二仏同座）。

#### (iii) 法華経 譬喩別軸 四譬完成体に到達

retrofit 11 sg10「火宅三車」（譬喩品 三乗教判）・retrofit 12 sg11「良医病子」（如来寿量品 方便涅槃）・retrofit 13 sg12「化城宝処」（化城喩品 方便引導／顕密二教判）・retrofit 14 sg13「多宝塔」（見宝塔品 本門宝塔湧現／二仏同座）の **四譬完成体** に到達。さらに retrofit 10 sg09「諸法実相」（方便品 抽象核心）と合わせて、法華経 内部における **迹門四段（諸法実相＋三譬：火宅三車・良医病子・化城宝処）＋本門一段（多宝塔）= 五段構成** が形成される。

#### (iv) 法華経 本門の中心譬を初の独立軸化

retrofit 10-13 の四軸（諸法実相・火宅三車・良医病子・化城宝処）は法華経 **迹門（前半 14 品・方便品＋三譬）** を中心としていたが、本 retrofit で初めて法華経 **本門（後半 14 品・久遠実成）** の中心譬である見宝塔品 多宝塔を独立軸化。法華経の **迹本二門** の双方が軸として明示化される運用基盤に到達。今後の薬王菩薩本事品（本門流通分・焼身供養）・観世音菩薩普門品（本門流通分・観音三十三応身）等の本門品譬喩別軸への展開基盤も整備。

#### (v) m637 二重所属の運用確立

m637 が sg09 諸法実相 anchor と sg13 多宝塔強連動の二系統二重所属となる。retrofit 9 で確立した「過去 anchor 自己参照タグ補完」（m713/m630 の sg07/sg02 + 自己参照タグ）の運用に続く、anchor motif の **明示的な複数系統所属** の第二例。kaimyo-app 検索では「連動:m637 で sg09 全件取得」「連動:m424 で sg13 全件取得」が独立して動作するため、二重所属による検索干渉は発生しない。

#### (vi) kakikudashi 直接含有を客観基準とする継続

本 retrofit でも強連動の客観基準として「kakikudashi 本文に多宝塔関連 keyword（多宝塔・多宝・宝塔・見宝塔・分身・湧出・二仏 等）直接含有」を採用：

- m424：多宝塔（1 直接含有）+ 見宝塔品（1）+ 既存タグ「典故:法華経見宝塔品」「場面:多宝塔帰」
- m637：宝塔（2）+ 見宝塔（1）+ 多宝（1）多重直接含有・本門宝塔湧現論述
- m690：宝塔（1）+ 湧出（1）直接含有・本門宝塔湧現対比
- m262：多宝（1）+ 見宝塔（1）直接含有・既存「主題:多宝分身三世仏」「典故:法華経見宝塔品多宝」三重タグ

全 4 motif が原語直接含有を満たす。retrofit 13 補注 M で確立した「タグ保持補助基準」は本 retrofit では発動せず、純粋な kakikudashi 直接含有基準のみで 4 motif 全件採択。retrofit 10 補注 J § 「kakikudashi 直接含有を客観基準とする選定」の最も明快な再適用例。

#### (vii) 譬喩別軸の今後の展開

法華経の譬喩素材は他に「信解品 長者窮子（m717 大日経疏 §58「人の宝蔵を開いて」自心実知・retrofit 13 で温存）」「五百弟子授記品 衣裏珠」「薬草喩品 三草二木」「従地涌出品 地涌の菩薩（m222・m639 温存）」「薬王菩薩本事品 焼身供養」「観世音菩薩普門品 三十三応身」等が残存。本 retrofit で sg13「多宝塔」を譬喩別軸の第四例（本門軸の初例）として確立し、retrofit 11 sg10「火宅三車」・retrofit 12 sg11「良医病子」・retrofit 13 sg12「化城宝処」と並ぶ四例目の譬喩別軸として位置づく。retrofit 15 以降で順次これらの譬喩別軸を追加可能。

#### (viii) Phase D 必須チェックリストの完全運用化（retrofit 14 で 6 回目の完走）

retrofit 9 が初の完全準拠、retrofit 10-13 が 2-5 回目、本 retrofit 14 で 6 回目の完全準拠 retrofit として位置づく。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 14 完走：法華経 見宝塔品 多宝塔連動 retrofit〔新規 sg13「多宝塔」+ 既存 m424 を書き下し anchor 単独採用・連動軸九系統並立に到達〕」が本セッション内容と完全整合。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 15〔法華経譬喩別軸〕

連動軸の譬喩別細分化（本 retrofit の延長）：

- **信解品 長者窮子**（m717 大日経疏 §58「人の宝蔵を開いて」自心実知）を anchor 候補・本 retrofit で温存
- **五百弟子授記品 衣裏珠**（要候補調査）
- **薬草喩品 三草二木**（要候補調査）
- **従地涌出品 地涌の菩薩**（m222 性霊集 第六巻 idx=44 達嚫「踊出の瑞」・m639 秘蔵宝鑰「従地涌出」温存）
- **薬王菩薩本事品 焼身供養**（要候補調査・本門流通分）
- **観世音菩薩普門品 三十三応身**（要候補調査・本門流通分）
- 規模 4-10 motif 前後・小〜中規模

### 選択肢 B：retrofit 15 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕

- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ。sg12（化城宝処）が顕密判の譬喩別軸として位置づいているため、本軸はその抽象的・体系的版に当たる
- 秘蔵宝鑰 十住心：「十住心」を anchor に、住心論系 motif を紐づけ

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸九系統 anchor 完全整合済〕

本 retrofit で連動軸九系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg13」を持つ 4 motif → 多宝塔連動素材プール（法華本門・本門宝塔湧現／二仏同座）
- 「連動:m424」の anchor 検索で 4 件全件取得可能（補注 J 単独 anchor 設計）
- 単独 anchor 体制と既存二重 anchor 体制の同型運用（kaimyo-app 検索ロジックは単独 anchor と同等）
- m637 の二系統二重所属：sg09 諸法実相（既存）と sg13 多宝塔（新規）を独立検索可能
- 法華経内部の五段構成検索：「諸法実相（抽象的）」 vs 「火宅三車（三乗教判）」 vs 「良医病子（方便涅槃）」 vs 「化城宝処（方便引導／顕密二教判）」 vs 「多宝塔（本門 宝塔湧現／二仏同座）」の弁別
- 譬喩別軸の追加準備〔retrofit 15 以降の長者窮子・衣裏珠・三草二木・地涌の菩薩等への拡張〕
- **特に多宝塔軸は法華経 本門の中心譬を初導入したため、kaimyo-app の本門教学解説（久遠実成・二仏同座）への直結が極めて強い**

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 単独 anchor 体制の retrofit 10 以来の再採用

retrofit 11-13 で二重 anchor 体制が三例連続採用された後、本 retrofit で単独 anchor 体制を再採用。譬喩別軸の anchor 体制選択基準として「単独／二重 anchor は譬喩の典籍系統的分布に応じて柔軟に選択」の運用方針が定着。将来の譬喩別軸でも、譬喩 keyword の含有分布に応じて単独／二重を自由に選択可能。

### (d-2) 法華経 本門の中心譬を初の独立軸化

retrofit 1-13 の連動軸は法華経 迹門（方便品＋三譬）と他経典の教学を中心としていたが、本 retrofit で初めて法華経 本門（見宝塔品 多宝塔）を独立軸化。法華経の迹本二門の双方が軸として明示化される運用基盤に到達。今後の薬王菩薩本事品・観世音菩薩普門品等の本門品譬喩別軸への展開基盤も整備。

### (d-3) m637 二重所属の運用確立

m637 が sg09 諸法実相 anchor と sg13 多宝塔強連動の二系統二重所属となる。retrofit 9 m713/m630 同型の anchor motif の明示的な複数系統所属の第二例。kaimyo-app 検索ロジックでは「連動:m637 で sg09 全件」「連動:m424 で sg13 全件」が独立して動作するため、二重所属による検索干渉は発生しない。

### (d-4) Write tool truncate 事象の予防対策（本 retrofit で 0 件発生）

本 retrofit では Python script を bash heredoc + write_bytes 方式で直接書き込みする運用を全面採用したため、Write tool truncate 事象は発生せず。retrofit 9-13 で複数回再発生した事象を継続予防。今後も Python script 作成時は Write tool ではなく bash heredoc + Python write_bytes 方式を優先することが推奨される。

### (d-5) CLAUDE.md 全角括弧バランス維持

CLAUDE.md は本 retrofit 前は 〔/〕 各 611 件で完全バランス、本 retrofit 後は 〔/〕 各 633 件で完全バランス維持（+22 件・追加部分も balanced）。半角 （）には -1 の pre-existing 差分があるが、本 retrofit の追加部分は内部 balanced（footer_marker 1 開きを除けば +14/+14）。

### (d-6) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9-13 で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を継続採用。最終検証で NUL 0 件確認。

### (d-7) retrofit 14 後の motifs.json サイズ

retrofit 14 で +4,293 bytes〔2,610,239 → 2,614,532 bytes〕。retrofit 13〔+5,407〕・retrofit 12〔+4,529〕・retrofit 11〔+3,314〕・retrofit 10〔+2,383〕・retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 11 連続で +1,000〜5,500 bytes 規模の retrofit。本 retrofit は anchor 単独・規模最小（4 motif）のため retrofit 12（4 motif・+4,529）と同等規模に位置づく。新規 sg13 motif の description 632 字（sg12 の 675 字より少し短い）・強連動 4 motif への +8 タグの組合せ。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-8) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg13 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg13 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg12 と同方針）。gendai_gabun_chars_total も 154,931 維持。kakikudashi_chars_total は +3 字（「多宝塔」3 字）、gendaigoyaku_chars_total は +632 字（sg13 description）増加。

### (d-9) git 状態の異常（retrofit 9-13 §(d-1) 同型・継続中の可能性）

本セッション開始時に `git log` で HEAD 8d40144 確認済だが、`git status --short` 実行時に `fatal: unable to read e4a38751f5000000000000000000000000000000` のインデックス参照エラーを観測。commit 履歴自体は intact だが、git index に corrupt 参照が残存する状態。ケンシン側の commit_push.bat 実行時に bash mount 側と Windows 側の乖離が再発する可能性があるため、実行時に確認推奨。retrofit 9-13 で観測された §(d-1) 同型の継続中現象。

### (d-10) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 4 件・バックアップ 3 件・handoff 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

### (d-11) Phase D 必須チェックリストの retrofit 14 で完全運用化（6 回目）

retrofit 9 で初の完全準拠を達成、retrofit 10 で 2 回目、retrofit 11 で 3 回目、retrofit 12 で 4 回目、retrofit 13 で 5 回目、本 retrofit 14 で 6 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 14 完走：法華経 見宝塔品 多宝塔連動 retrofit〔新規 sg13「多宝塔」+ 既存 m424 を書き下し anchor 単独採用・連動軸九系統並立に到達〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔757 件・m1-m744 + sg01-sg13・2,614,532 bytes〕
- 本 retrofit build script：`outputs/retrofit14_taho_to.py`〔dry-run + 本番適用の二段運用〕
- 補注 N 追加 script：`outputs/update_motifs_index_design_r14.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_r14.py`
- commit_message.txt 書き換え script：`outputs/write_commit_message_r14.py`
- 本 handoff 作成 script：`outputs/write_handoff_r14.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit14.json`〔retrofit 前 motifs.json・2,610,239 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit14.md`〔retrofit 前 motifs_index_design.md・100,507 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit14.md`〔retrofit 前 CLAUDE.md・247,340 bytes〕
- 前 retrofit handoff：`handoff_2026-05-12_retrofit13_complete.md`〔法華経 化城喩品 化城宝処連動〕
- 補注 N 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 14 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-10 完走 → 2026-05-12 retrofit 11/12/13/14 完走に到達。retrofit 14 完走〔法華経 見宝塔品 多宝塔連動・新規 sg13 + 既存 m424 を書き下し anchor 単独採用・連動軸九系統並立に到達〕。本体 motifs.json は 757 件・2,614,532 bytes・schema_history 72 件。motifs_index_design.md §2 に補注 N 追加〔補注 A-N 全 14 件 intact・115,100 bytes〕。CLAUDE.md は 253,981 bytes〔retrofit 4-14 全エントリ intact〕。連動軸九系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）〕の anchor 自己参照タグ運用が完全整合に到達。法華経内部の五段構成〔迹門四段（諸法実相＋三譬：火宅三車・良医病子・化城宝処）＋本門一段（多宝塔）〕も成立。単独 anchor 体制の retrofit 10 以来の再採用例。法華経 本門の中心譬を初の独立軸化。法華経 譬喩別軸 四譬完成体に到達。m637 二重所属の運用（sg09 と sg13）。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit14_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit13_complete.md`〔retrofit 13 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-N 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・757 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 14 commit です。

【本セッションの選択肢】
(A) retrofit 15 候補〔法華経譬喩別軸：信解品 長者窮子 m717 温存／五百弟子授記品 衣裏珠／薬草喩品 三草二木／従地涌出品 地涌の菩薩 m222・m639 温存／薬王菩薩本事品 焼身供養／観世音菩薩普門品 三十三応身〕
(B) retrofit 15 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸九系統 anchor 完全整合済の素材プール活用〔特に sg13 多宝塔は法華本門の中心譬として kaimyo-app の本門教学解説に最適〕
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 単独 anchor 体制（補注 J/N 案 A 単独版）と二重 anchor 体制（補注 K/L/M 案 A 二重版）は譬喩の典籍系統的分布に応じて柔軟に選択
- 本体 motifs.json は 2,614,532 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須。可能な限り Python script の `path.write_bytes(data)` を使用

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-12〔retrofit 14 完走・法華経 見宝塔品 多宝塔連動 retrofit。新規 sg-id sg13「多宝塔」を追加〔出典:法華経 見宝塔品「爾時仏前有七宝塔・従地涌出住在空中」「即時釈迦牟尼仏入其塔中坐其半座・結加趺坐」〕、書き下し anchor として **m424 を単独採用**：m424（性霊集 第八巻 idx=78 先師勤操表白・「多宝塔の中に帰し玉えるか、当、鷲峯の窟の裏に還り玉うか」・「多宝塔」原語直接含有・性霊集中で「多宝塔」原語含有唯一例・追慕弔辞独立譬として運用）。強連動 4 motif〔m424(anchor 単独・性霊集 表白追慕)/m637(秘蔵宝鑰 巻の下 第八章 一道無為心 第二節・「会三帰一して仏智の深多を讃し、指本遮末して成覚の久遠を談じ、宝塔騰踊して二仏同座し」・諸法実相 sg09 と sg13 多宝塔の二重所属)/m690(大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現・「法華の序分や従地湧出品の因縁の如し」・本門宝塔湧現対比)/m262(性霊集 第八巻 idx=76 三嶋大夫亡息女表白・「鷲峯海会の釈迦尊、多宝分身三世の仏」・廻向呼びかけ)〕に `連動:sg13`・`連動:m424` を付与（+8 タグ・補注 J 案 A 単独 anchor 運用継承）。total_motifs 756→757（+1 新規 sg13）・famous_phrases 12→13。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,614,532 bytes〔+4,293〕・schema_history 72 件〔+1・origin: retrofit_14:doctrine〕・補注 N 追加〔motifs_index_design.md §2・100,507→115,100 bytes・+14,593〕・CLAUDE.md 更新完了〔247,340→253,981 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸九系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）〕に到達——法華経内部で迹門四段（諸法実相＋三譬：火宅三車・良医病子・化城宝処）＋本門一段（多宝塔）の五段構成に到達。**単独 anchor 体制の retrofit 10 以来の再採用例**（譬喩の典籍系統的分布に応じて単独／二重を柔軟選択する運用方針の定着）・**法華経 本門の中心譬を初の独立軸化**（retrofit 10-13 は方便品＋迹門三譬の迹門中心構成）・**法華経 譬喩別軸 四譬完成体**（火宅三車・良医病子・化城宝処・多宝塔）に到達・**m637 二重所属の運用**（sg09 諸法実相 anchor と sg13 多宝塔強連動の二系統二重所属・retrofit 9 m713/m630 同型）。Phase D 必須チェックリストに完全準拠する第六の retrofit〕

# 引き継ぎメモ：retrofit 15 完走〔法華経 薬草喩品 三草二木連動 retrofit〕

**日付**：2026-05-12
**フェーズ**：retrofit 15（retrofit 14 完走に続く第十二の retrofit セッション）
**対象**：法華経 薬草喩品 三草二木連動軸の新設。新規 sg-id `sg14`「三草二木」を追加し、書き下し anchor として **m215 + m636 を二重採用**（系統対比型・retrofit 11/13 同型）：m215（性霊集 第六巻 idx=44 桓武皇帝法華達嚫・性霊集 達嚫系・典故:法華経薬草喩品 タグ保持）+ m636（秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱・秘蔵宝鑰系・既 sg10 火宅三車 anchor の片翼・sg10/sg14 二系統二重所属）。retrofit 11/13 の系統対比型二重 anchor 体制の再採用例（第三例）。連動軸が九系統 → 十系統並立に到達。法華経内部の **迹門五段（諸法実相＋四譬：火宅三車・良医病子・化城宝処・三草二木）＋本門一段（多宝塔）= 六段構成** に到達。**法華経 迹門 正宗分の中核譬を初の独立軸化**（retrofit 11-13 は迹門の具体的譬喩、retrofit 14 は本門 流通分、本 retrofit で初めて迹門 正宗分の中核譬を独立軸化）。**法華経 譬喩別軸 五譬完成体**〔火宅三車・良医病子・化城宝処・多宝塔・三草二木〕に到達。**anchor 同士の二重所属としては本 retrofit が初例**（m636 が sg10 火宅三車 anchor と sg14 三草二木 anchor の二系統 anchor・retrofit 14 m637 は anchor + 強連動の二重所属だったため、anchor + anchor の二重所属は本 retrofit が初例）。
**ステータス**：完走〔Phase A 軸設計合意・Phase B 5 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 O 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 16 候補〔法華経譬喩別軸（信解品 長者窮子 m717 温存／五百弟子授記品 衣裏珠／従地涌出品 地涌の菩薩 m222・m639 温存／観世音菩薩普門品 三十三応身）／弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸十系統 anchor 完全整合済〕等から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_15:doctrine〕
- [x] motifs_index_design.md に補注 O 追加済〔A-O 全 15 件 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 15 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-12_retrofit15_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 追加部分 全角括弧バランス確認〔commit_message.txt 〔32/32・（125/125〕／補注 O 〔13/13・（101/101〕／CLAUDE.md 追加部分 〔24/24・（19/19〕〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

retrofit 14 完走〔法華経 見宝塔品 多宝塔連動・新規 sg13 + 既存 m424 を書き下し anchor 単独採用・commit `304e15d`〕に続く第十二の retrofit セッション。

retrofit 14 完走 handoff §(c) 選択肢 A〔retrofit 15 候補：法華経譬喩別軸〕に着手。2026-05-12 にケンシン裁定で「薬草喩品 三草二木軸」を選定し、判断 1-5 を 1 セッション内で連続裁定〔(1) 中心成句 = 三草二木、(2) 二重 anchor m215 + m636（系統対比型）、(3) 規模 anchor 2 + 強連動 3 = 5 motif、(4) 強連動 m237+m712+m706、(5) 補注 K/L/M 案 A 二重版継承〕。Phase A〜D を 1 commit にまとめて完走する方針で進行。

**本 retrofit の特徴**：

- 新規 sg-id `sg14`「三草二木」を追加〔出典:法華経 薬草喩品「其雲所雨一味之水、草木叢林、随分受潤・各得生長」「仏平等説、如一味雨、随衆生性、所受不同」〕
- 書き下し anchor は **二重採用**（系統対比型）：m215（性霊集 第六巻 idx=44 桓武皇帝法華達嚫・性霊集 達嚫系）+ m636（秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱・秘蔵宝鑰系／既 sg10 火宅三車 anchor の片翼）
- 強連動 3 motif（anchor 2 + 強連動 3 = 計 5 motif）に「連動:sg14」「連動:m215」「連動:m636」を付与（+14 タグ・m636 既存「連動:m636」重複除く・補注 K/L/M 案 A 二重版運用継承）
- 法華経内部で迹門五段（諸法実相 sg09・火宅三車 sg10・良医病子 sg11・化城宝処 sg12・三草二木 sg14）＋本門一段（多宝塔 sg13）の六段構成に到達
- 連動軸十系統並立に到達
- **法華経 迹門 正宗分の中核譬を初の独立軸化**：retrofit 11-13 は具体的譬喩（火宅三車・良医病子・化城宝処）を独立軸化、retrofit 14 は本門 流通分（多宝塔）を独立軸化したのに対し、本 retrofit で初めて迹門 正宗分の中核譬（薬草喩品 三草二木）を独立軸化
- **anchor 同士の二重所属としては本 retrofit が初例**：m636 が sg10 火宅三車 anchor と sg14 三草二木 anchor の二系統 anchor になる（retrofit 14 m637 は anchor + 強連動の二重所属だったため、本 retrofit で anchor + anchor の二重所属が初例化）

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg14 =「三草二木」（4 字成句・sg10「火宅三車」と同型の 4 字構成）
- **判断 2**：書き下し anchor = m215 + m636 二重採用（案 C・系統対比型・retrofit 11/13 同型）
- **判断 3**：規模 = anchor 2 + 強連動 3 = 5 motif（最小〜中規模・retrofit 12 良医病子相当）
- **判断 4**：強連動 3 件 = m237（性霊集 第六巻 idx=45 天長皇帝故中務卿親王 檀像願文）+ m712（大日経疏 §51-52 金剛手三問・毘盧遮那応答開始）+ m706（大日経疏 §45 虚空譬）
- **判断 5**：二重 anchor タグ運用 = 補注 K/L/M 案 A 二重版〔retrofit 11/12/13 と同型ルール継承・全 motif に「連動:sg14」「連動:m215」「連動:m636」の 3 タグ付与・m636 のみ既存「連動:m636」重複により実質 +2 タグ〕

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

**Phase A 自動スキャン**：法華経譬喩別軸 6 譬の hit 数を比較：

| 候補 | kakikudashi 直接 | 全本文 | タグ保有 | anchor 候補 |
|---|---:|---:|---:|---|
| P1 信解品 長者窮子 | 8 | 19 | 0 | m717（温存・大日経疏 §58） |
| P2 五百弟子授記品 衣裏珠 | 4 | 17 | 0 | 該当弱 |
| P3 薬草喩品 三草二木 | 11 | 27 | 2 | m215/m636/m237（採用） |
| P4 従地涌出品 地涌の菩薩 | 4 | 5 | 1 | m222（温存） |
| P5 薬王菩薩本事品 焼身供養 | 4 | 9 | 0 | **anchor 確立不可**（焼身/燃身/燃指/薬王菩薩 直接含有 0 件・スコープ外確定） |
| P6 観世音菩薩普門品 三十三応身 | 22 | 62 | 1 | 観音信仰一般に拡散・絞り込み要 |

判定対象 motif 候補：

法華経 三草二木関連 motif の分布把握：
- 「三草」kakikudashi 直接含有: 1 件（m636）
- 「二木」kakikudashi 直接含有: 0 件（本文含有のみ）
- 「薬草」kakikudashi 直接含有: 0 件
- 「草木」kakikudashi 直接含有: 6 件（m215, m559, m562, m636, m706, m710）
- 「雲雨」kakikudashi 直接含有: 1 件（m215）
- 「雨潤」kakikudashi 直接含有: 1 件（m712）
- 「一雨」kakikudashi 直接含有: 1 件（m636）
- 「卉木」kakikudashi 直接含有: 1 件（m736）
- 「上中下」kakikudashi 直接含有: 2 件（m728/m730）
- 「典故:法華経薬草喩品」系タグ保持 motif: 2 件（m215, m237）
- 「主題:雲雨草木果結」タグ保持 motif: 1 件（m215）

候補 motif の整理：
- m215：性霊集 第六巻 idx=44 桓武皇帝法華達嚫・「雲雨覆い澍いで而も煩を解き、草木滋く茂して而も果を結ぶ」直接含有・既存タグ「典故:法華経薬草喩品」「主題:雲雨草木果結」「場面:雲雨草木果結」保持・**最有力 anchor 候補（性霊集 法華経薬草喩品 正面引用）**
- m636：秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱・「一乗を三草に開く」「一雨の円音…草木の芽葉」・「三草」「草木」「一雨」kakikudashi 直接含有 3 件・既存 sg10 火宅三車 anchor の片翼（連動:sg10/m209/m636 保持）・**最有力 anchor 候補（秘蔵宝鑰 天台教判・sg10/sg14 二系統二重所属）**
- m237：性霊集 第六巻 idx=45 天長皇帝故中務卿親王 檀像願文・「乗蓮の金体は累日の光彩を流し、潤草の玉文は梵釈の誠請を致す」・「潤草」kakikudashi 直接含有・既存タグ「典故:法華経薬草喩品」「主題:潤草玉文梵釈誠請」保持・**強連動 性霊集 願文系**
- m712：大日経疏 巻第一 §51-52 金剛手三問・毘盧遮那応答開始・「春陽の始めに萌種甲折け、雷風鼓動し、時雨潤灑」・「雨潤」直接含有・三句法門系・**強連動 大日経疏 三句法門系**
- m706：大日経疏 巻第一 §45 虚空譬・「一切の草木はこれに因って生長し、有情の事業はこれに依って成ずることを得」・「草木」直接含有・本来性 法界系・**強連動 大日経疏 本来性 法界系**
- m710：大日経疏 水大論・「草木を潤し華果を生じ」・スコープ外（規模 5 制約による温存）
- m736：大日経疏 性大論・「卉木の地に依って生ずる」・スコープ外（規模 5 制約による温存）
- m728/m730：大日経疏 §54 五障/性大「上中下」・スコープ外（薬草の譬とは別文脈で誤検出近く除外）
- m559/m562/m563：吽字義「草木」・スコープ外（吽字義として別系統）
- m717：大日経疏 §58 自心実知「人の宝蔵を開いて」・スコープ外（信解品 長者窮子軸候補に温存）
- m222/m639：従地涌出品「踊出の瑞」「従地涌出」・スコープ外（従地涌出品軸候補に温存）

判断 2 anchor 選定の三案：
- 案 A：m215 単独（性霊集系のみ・retrofit 10/14 同型）
- 案 B：m636 単独（秘蔵宝鑰系のみ・既 sg10 連動の二重所属を活用）
- 案 C：m215 + m636 二重（系統対比型・retrofit 11/13 同型）

ケンシン裁定で **案 C：m215 + m636 二重採用（系統対比型）** を採用。理由：(1) 性霊集中で m215 が「典故:法華経薬草喩品」タグを保持しつつ「草木」「雲雨」を kakikudashi 直接含有する **桓武皇帝法華達嚫の正面引用** 例である点、(2) 秘蔵宝鑰中で m636 が「三草」「草木」「一雨」を kakikudashi 直接含有しつつ既に sg10 火宅三車 anchor として確立済である点、(3) 性霊集系（m215）と秘蔵宝鑰系（m636）の系統対比型運用が retrofit 11 sg10/m209+m636・retrofit 13 sg12/m227+m569 で確立した既定パターンに完全合致する点。

### Phase B：5 motif の判定表

| m-id | 出典 | kakikudashi keyword 直接含有 | 既存連動タグ | 既存関連タグ（主要） | 系統 | 役割 | 採否 |
|---|---|---|---|---|---|---|---|
| m215 | 性霊集 第六巻 idx=44 桓武皇帝法華達嚫 | 「雲雨覆い澍いで」「草木滋く茂して」（草木 1 + 雲雨 1） | なし | 典故:法華経薬草喩品・主題:雲雨草木果結・場面:雲雨草木果結 | 達嚫系（性霊集 法華経薬草喩品 正面引用） | **anchor 1（性霊集系）** | **採用** |
| m636 | 秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱 | 「一乗を三草に開く」「一雨の円音…草木の芽葉」（三草 1 + 草木 1 + 一雨 1） | 連動:sg10・連動:m209・連動:m636 | 主題:住心/天台/教判/一道無為/本来性/機根 | 教学系（秘蔵宝鑰 天台教判） | **anchor 2（秘蔵宝鑰系・sg10/sg14 二系統二重所属）** | **採用** |
| m237 | 性霊集 第六巻 idx=45 天長皇帝故中務卿親王 檀像願文 | 「潤草の玉文は梵釈の誠請を致す」（潤草 1） | なし | 典故:法華経薬草喩品・主題:潤草玉文梵釈誠請・主題:乗蓮金体累日光彩 | 願文系（性霊集 法華経薬草喩品 タグ保持） | 強連動 | **採用** |
| m712 | 大日経疏 巻第一 §51-52 金剛手三問・毘盧遮那応答開始 | 「春陽の始めに萌種甲折け、雷風鼓動し、時雨潤灑」（雨潤 1） | なし | 主題:加持身/三句法門/三句/菩提/智慧/法身 | 教学系（大日経疏 三句法門系） | 強連動 | **採用** |
| m706 | 大日経疏 巻第一 §45 虚空譬 | 「一切の草木はこれに因って生長し」（草木 1） | なし | 主題:本来性/法界/智慧/法身/仏身/不二/菩提/五大 | 教学系（大日経疏 本来性 法界系） | 強連動 | **採用** |
| m710 | 大日経疏 水大論 | 「草木を潤し華果を生じ」 | なし | 主題:智慧/慈悲/衆生救済 | 教学系 | 温存 | スコープ外（規模 5 制約） |
| m736 | 大日経疏 性大論 | 「卉木の地に依って生ずる」 | なし | 主題:菩提心/大菩提/法身 | 教学系 | 温存 | スコープ外 |
| m728/m730 | 大日経疏 §54 五障/性大 | 「上中下品」「上中下の性の種類」 | なし | — | 教学系 | — | スコープ外（誤検出近く） |
| m559/m562/m563 | 吽字義 | 「草木」 | なし | 主題:吽字 | 教学系（吽字義） | — | スコープ外（別系統） |
| m717 | 大日経疏 §58 自心実知 | 「人の宝蔵を開いて」「譬えば長者の家の窮子の如し」 | なし | 典故:法華経・典故:大日経 | 信解品系 | 温存 | スコープ外（将来 信解品 長者窮子軸候補） |
| m222/m639 | 性霊集 idx=44／秘蔵宝鑰 | 「踊出の瑞」「従地涌出」 | m639 に 連動:sg09/m637 | — | 従地涌出品系 | 温存 | スコープ外（将来 従地涌出品 地涌の菩薩軸候補） |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 757 | 758 | +1（sg14 新規追加） |
| ファイルサイズ | 2,614,532 bytes | 2,620,393 bytes | +5,861 |
| 連動タグを持つ motif | 51 | 56 | +5（m215/m237/m706/m712 新規連動 + m636 sg14 連動追加） |
| 連動タグ総数 | — | — | +14（m215/m237/m706/m712 各 +3 + m636 +2） |
| famous_phrases | 13 | 14 | +1（sg14 追加で recompute） |
| schema_history 件数 | 72 | 73 | +1 |
| kakikudashi_chars_total | 112,779 | 112,783 | +4（「三草二木」4 字） |
| gendaigoyaku_chars_total | 307,059 | 307,915 | +856（sg14 description） |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 758 vs 758 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[], count=744 ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔5 motif〕 | missing=[] ✓ |
| 7 | sg14 配列追加〔末尾 pos=757〕 | ✓ |

### Phase D：補注 O 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 O〔法華経 薬草喩品 三草二木連動の運用〕新規追加〔115,100→130,096 bytes・+14,996 bytes〕。anchor 構成表（二重 anchor 体制 系統対比型・retrofit 11/13 同型）・追加連動タグ値表・二重 anchor タグ運用ルール（補注 K/L/M 案 A 二重版継承）・retrofit 15 実施結果・設計上の論点 8 項目〔(i) 二重 anchor 体制 系統対比型の retrofit 11/13 以来の再採用／(ii) 連動軸十系統並立／(iii) 法華経 譬喩別軸 五譬完成体／(iv) 法華経 迹門 正宗分の中核譬を初の独立軸化／(v) anchor 二重所属の運用第二例・anchor 同士の二重所属としては初例／(vi) kakikudashi 直接含有を客観基準とする継続・キーワードリスト拡張による発見的補完／(vii) 譬喩別軸の今後の展開／(viii) schema_history origin タグの定着〕を明文化。補注 A-O 全 15 件 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 15 完走エントリを追加〔253,981→262,035 bytes・+8,054 bytes〕。retrofit 4-15 全エントリ intact 確認済。NUL バイト 0 件確認。
- `commit_message.txt` を retrofit 15 用に完全書き換え〔23,966 bytes・NUL 0・冒頭行整合確認済・全角括弧 〔32/32・（125/125〕。冒頭行を「retrofit 15 完走：法華経 薬草喩品 三草二木連動 retrofit〔新規 sg14「三草二木」+ 既存 m215+m636 を書き下し anchor 二重採用（系統対比型）・連動軸十系統並立に到達・anchor 同士の二重所属が初例〕」として、Phase D 必須チェックリストに完全準拠。Python `write_bytes` 直接書き込み方式で作成。

### 設計上の新規ポイント

#### (i) 二重 anchor 体制 系統対比型の retrofit 11/13 以来の再採用

retrofit 11 sg10/m209+m636 が初の系統対比型二重 anchor（願文系+教学系）、retrofit 13 sg12/m227+m569 が第二例（願文系+顕密判教学系）、本 retrofit で第三例（達嚫系+秘蔵宝鑰系）の系統対比型二重 anchor 体制を採用。文体対比型（retrofit 12 sg11/m44+m70）と単独 anchor 体制（retrofit 10 sg09/m637・retrofit 14 sg13/m424）に対し、系統対比型が **譬喩別軸の標準運用形** として確立した感触を得る。性霊集系 anchor（願文・達嚫・表白）と秘蔵宝鑰系 anchor（教判・住心論）の対比は、空海の文体間横断を構造化する基本枠組みとして安定運用化。

#### (ii) 連動軸十系統並立に到達

本 retrofit で連動軸は以下の十系統が並立：

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
| 多宝塔 | sg13 | m424（単独） | 連動:sg13・連動:m424 | retrofit 14 |
| **三草二木** | **sg14** | **m215 + m636（二重・系統対比型・m636 は sg10/sg14 二系統二重所属）** | **連動:sg14・連動:m215・連動:m636** | **retrofit 15（本 retrofit）** |

kaimyo-app は十の教学テーマで素材プールを切替可能：即身成仏／菩薩道の三句／般若空観／密教空観／法華空観（諸法実相）／法華譬喩（火宅三車・三乗教判）／法華譬喩（良医病子・方便涅槃）／法華譬喩（化城宝処・方便引導／顕密二教判）／法華本門（多宝塔・本門宝塔湧現／二仏同座）／法華譬喩（三草二木・一味雨潤／一乗教判）。

#### (iii) 法華経 譬喩別軸 五譬完成体に到達

retrofit 11 sg10「火宅三車」（譬喩品 三乗教判）・retrofit 12 sg11「良医病子」（如来寿量品 方便涅槃）・retrofit 13 sg12「化城宝処」（化城喩品 方便引導／顕密二教判）・retrofit 14 sg13「多宝塔」（見宝塔品 本門宝塔湧現／二仏同座）・retrofit 15 sg14「三草二木」（薬草喩品 一味雨潤／一乗教判）の **五譬完成体** に到達。さらに retrofit 10 sg09「諸法実相」（方便品 抽象核心）と合わせて、法華経 内部における **迹門五段（諸法実相＋四譬：火宅三車・良医病子・化城宝処・三草二木）＋本門一段（多宝塔）= 六段構成** が形成される。

#### (iv) 法華経 迹門 正宗分の中核譬を初の独立軸化

retrofit 11-13 は法華経 迹門の具体的譬喩（火宅三車・良医病子・化城宝処）を独立軸化、retrofit 14 は法華経 本門 流通分（多宝塔）を独立軸化したのに対し、本 retrofit で初めて法華経 **迹門 正宗分** の中核譬（薬草喩品 三草二木）を独立軸化。薬草喩品は法華経 一乗教判（一切衆生悉皆成仏・機根対応・一味雨潤・草木滋茂）の理論的基盤となる譬で、kaimyo-app の本門教学解説（観音・薬王・地蔵等の機根応身説）・一切衆生悉皆成仏への直結が極めて強い。

#### (v) anchor 二重所属の運用第二例・anchor 同士の二重所属としては初例

m636 が sg10 火宅三車 anchor と sg14 三草二木 anchor の二系統二重所属となる。retrofit 14 m637（sg09 諸法実相 anchor と sg13 多宝塔強連動の二系統二重所属）に続く、anchor motif の明示的な複数系統所属の第二例。特に **anchor 同士の二重所属**（anchor + anchor の二重所属）は本 retrofit が初例で、retrofit 14 の m637（anchor + 強連動）から一段進んだ形態。kaimyo-app 検索では「連動:m636 で sg10/sg14 両軸全件取得」が成立する。検索ロジック上は「連動:m636」「連動:m215」「連動:m209」が並列して動作する（互いに干渉せず）。

#### (vi) kakikudashi 直接含有を客観基準とする継続・キーワードリスト拡張による発見的補完

本 retrofit でも強連動の客観基準として「kakikudashi 本文に三草二木関連 keyword（三草・二木・薬草・草木・潤草・雨潤・雲雨・一雨・卉木 等）直接含有」を採用：

- m215：草木（1）+ 雲雨（1）+ 既存タグ「典故:法華経薬草喩品」「主題:雲雨草木果結」
- m636：三草（1）+ 草木（1）+ 一雨（1）多重直接含有・天台教判
- m237：潤草（1）直接含有・既存「典故:法華経薬草喩品」タグ
- m712：雨潤（1）直接含有・三句法門系
- m706：草木（1）直接含有・本来性 法界系

全 5 motif が原語直接含有を満たす。retrofit 14 補注 N の純粋 kakikudashi 直接含有基準の継続。なお Phase A 自動スキャンの keyword リストには「潤草」が含まれず m237 は kakikudashi 直接含有として検出されなかったが、人手レビューで「潤草」直接含有が確認された。これは補注 M で確立した「タグ保持補助基準」と並んで「キーワードリスト拡張による発見的補完」の運用例として記録（将来の retrofit でも Phase A 自動スキャン後の人手レビューで keyword リスト不備による見落としを救う運用が継続される）。

#### (vii) 譬喩別軸の今後の展開

法華経の譬喩素材は他に「信解品 長者窮子（m717 大日経疏 §58「人の宝蔵を開いて」自心実知・retrofit 13-15 で温存）」「五百弟子授記品 衣裏珠」「従地涌出品 地涌の菩薩（m222・m639 温存）」「薬王菩薩本事品 焼身供養（kakikudashi 直接含有 0 件のため anchor 確立不可・スコープ外確定）」「観世音菩薩普門品 三十三応身（観音信仰一般に拡散・規模絞り込み要）」等が残存。本 retrofit で sg14「三草二木」を譬喩別軸の第五例（迹門 正宗分の初例）として確立し、retrofit 11 sg10「火宅三車」・retrofit 12 sg11「良医病子」・retrofit 13 sg12「化城宝処」・retrofit 14 sg13「多宝塔」と並ぶ五例目の譬喩別軸として位置づく。retrofit 16 以降で順次これらの譬喩別軸を追加可能。

#### (viii) Phase D 必須チェックリストの完全運用化（retrofit 15 で 7 回目の完走）

retrofit 9 が初の完全準拠、retrofit 10-14 が 2-6 回目、本 retrofit 15 で 7 回目の完全準拠 retrofit として位置づく。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 15 完走：法華経 薬草喩品 三草二木連動 retrofit〔新規 sg14「三草二木」+ 既存 m215+m636 を書き下し anchor 二重採用（系統対比型）・連動軸十系統並立に到達・anchor 同士の二重所属が初例〕」が本セッション内容と完全整合。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 16〔法華経譬喩別軸 残候補〕

連動軸の譬喩別細分化（本 retrofit の延長）：

- **信解品 長者窮子**（m717 大日経疏 §58「人の宝蔵を開いて」「譬えば長者の家の窮子の如し」・「長者」「窮子」「宝蔵」三重直接含有・最有力候補）を anchor 候補・本 retrofit で温存
- **五百弟子授記品 衣裏珠**（要候補調査・宝珠キーワード過剰検出のため絞り込み要）
- **従地涌出品 地涌の菩薩**（m222 性霊集 第六巻 idx=44 達嚫「踊出の瑞」・m639 秘蔵宝鑰「従地涌出」温存）
- **観世音菩薩普門品 三十三応身**（観音信仰一般に拡散・規模絞り込み要・m440 が典故:法華経観世音菩薩普門品 タグ保持）
- **薬王菩薩本事品 焼身供養**：kakikudashi 直接含有 0 件のため anchor 確立不可・**スコープ外確定**
- 規模 4-10 motif 前後・小〜中規模

### 選択肢 B：retrofit 16 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕

- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ。sg12（化城宝処）が顕密判の譬喩別軸として位置づいているため、本軸はその抽象的・体系的版に当たる
- 秘蔵宝鑰 十住心：「十住心」を anchor に、住心論系 motif を紐づけ

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸十系統 anchor 完全整合済〕

本 retrofit で連動軸十系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg14」を持つ 5 motif → 三草二木連動素材プール（法華迹門 一味雨潤・一乗教判・一切衆生悉皆成仏）
- 「連動:m215」「連動:m636」のいずれの anchor 検索で 5 件全件取得可能（補注 K/L/M 二重 anchor 設計）
- 二重 anchor 体制の標準運用形（系統対比型）の完全整合
- m636 の二系統二重所属：sg10 火宅三車 anchor（既存）と sg14 三草二木 anchor（新規）を独立検索可能
- 法華経内部の六段構成検索：「諸法実相（抽象的）」 vs 「火宅三車（三乗教判）」 vs 「良医病子（方便涅槃）」 vs 「化城宝処（方便引導／顕密二教判）」 vs 「多宝塔（本門 宝塔湧現／二仏同座）」 vs 「三草二木（一味雨潤／一乗教判）」の弁別
- 譬喩別軸の追加準備〔retrofit 16 以降の長者窮子・衣裏珠・地涌の菩薩・観音三十三応身等への拡張〕
- **特に三草二木軸は法華迹門 正宗分 一乗教判の理論基盤を初導入したため、kaimyo-app の一切衆生悉皆成仏 関連教学解説（観音・薬王・地蔵等の機根応身説）への直結が極めて強い**

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 系統対比型二重 anchor の標準運用形化

retrofit 11/13/15 の三例で系統対比型二重 anchor 体制が確立。性霊集系（達嚫・願文・表白）vs 秘蔵宝鑰系（教判・住心論）の対比が、譬喩別軸の標準運用形として安定化。将来の譬喩別軸でも、譬喩 keyword の典籍系統的分布に応じて自然に系統対比型を選択可能。

### (d-2) anchor 同士の二重所属が初例

retrofit 14 m637 が anchor + 強連動の二重所属だったのに対し、本 retrofit m636 は sg10/sg14 の anchor + anchor の二重所属。kaimyo-app 検索ロジックでは「連動:m636 で sg10/sg14 両軸全件取得」「連動:m215 で sg14 全件取得」「連動:m209 で sg10 全件取得」が並列して動作する（互いに干渉せず）。

### (d-3) Phase A 自動スキャンの keyword リスト不備による見落としを救う運用

m237 は kakikudashi に「潤草」を含有するが、自動スキャンのキーワードリストに「潤草」が無いため検出されなかった。Phase B 人手レビューで「潤草」直接含有が確認され救済された。将来の retrofit でも Phase A 自動スキャン後の人手レビューで keyword リスト不備による見落としを救う運用が継続される。

### (d-4) Write tool truncate 事象の予防対策（本 retrofit で 0 件発生）

本 retrofit では Python script を bash heredoc + write_bytes 方式または Write tool + NUL 検証で書き込みする運用を全面採用したため、Write tool truncate 事象は発生せず。retrofit 9-14 で複数回再発生した事象を継続予防。

### (d-5) CLAUDE.md 全角括弧バランス維持

CLAUDE.md は本 retrofit 前は 〔/〕各 633 件で完全バランス、本 retrofit 後は 〔/〕各 657 件で完全バランス維持（+24 件・追加部分も balanced）。半角（）には -1 の pre-existing 差分があるが、本 retrofit の追加部分は内部 balanced（+19/+19）。

### (d-6) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9-14 で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を継続採用。最終検証で NUL 0 件確認。

### (d-7) retrofit 15 後の motifs.json サイズ

retrofit 15 で +5,861 bytes〔2,614,532 → 2,620,393 bytes〕。retrofit 14〔+4,293〕・retrofit 13〔+5,407〕・retrofit 12〔+4,529〕・retrofit 11〔+3,314〕・retrofit 10〔+2,383〕・retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 12 連続で +1,000〜6,000 bytes 規模の retrofit。本 retrofit は anchor 二重・規模 5 motif で retrofit 13 化城宝処（4 系統 6 motif）に近い規模。新規 sg14 motif の description 856 字。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-8) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg14 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg14 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg13 と同方針）。gendai_gabun_chars_total も 154,931 維持。kakikudashi_chars_total は +4 字（「三草二木」4 字）、gendaigoyaku_chars_total は +856 字（sg14 description）増加。

### (d-9) git 状態の異常（retrofit 9-14 §(d-1) 同型・継続中の可能性）

本セッション開始時に retrofit 14 §(d-9) で記録の通り、git status --short 実行時に \002・\b の制御文字 path を含む UU/AD 異常、package.json/render.yaml/tsconfig.json/vercel.json/start.bat 削除ステージ等が残存していることを確認。commit 履歴自体は intact だが、git index に corrupt 参照が残存する状態。cleanup_git_state_pre_retrofit15.bat + cleanup_git_state_pre_retrofit15.py をケンシン側でダブルクリック実行することで整理。

### (d-10) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 5 件・バックアップ 3 件・handoff 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み（cleanup 経由でステージング削除が解消されるため）。

### (d-11) Phase D 必須チェックリストの retrofit 15 で完全運用化（7 回目）

retrofit 9 で初の完全準拠を達成、retrofit 10 で 2 回目、retrofit 11 で 3 回目、retrofit 12 で 4 回目、retrofit 13 で 5 回目、retrofit 14 で 6 回目、本 retrofit 15 で 7 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 15 完走：法華経 薬草喩品 三草二木連動 retrofit〔新規 sg14「三草二木」+ 既存 m215+m636 を書き下し anchor 二重採用（系統対比型）・連動軸十系統並立に到達・anchor 同士の二重所属が初例〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔758 件・m1-m744 + sg01-sg14・2,620,393 bytes〕
- 本 retrofit build script：`outputs/retrofit15_sanso_niboku.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit15_phaseA_scan.py`／結果：`outputs/retrofit15_phaseA_candidates.txt`
- Phase B inspect 結果：`outputs/retrofit15_phaseB_inspect.txt`
- 補注 O 追加 script：`outputs/update_motifs_index_design_r15.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_r15.py`
- commit_message.txt 書き換え script：`outputs/write_commit_message_r15.py`
- 本 handoff 作成 script：`outputs/write_handoff_r15.py`
- git cleanup script：`outputs/cleanup_git_state_pre_retrofit15.bat` + `.py`〔ケンシン側でダブルクリック実行〕
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit15.json`〔retrofit 前 motifs.json・2,614,532 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit15.md`〔retrofit 前 motifs_index_design.md・115,100 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit15.md`〔retrofit 前 CLAUDE.md・253,981 bytes〕
- 前 retrofit handoff：`handoff_2026-05-12_retrofit14_complete.md`〔法華経 見宝塔品 多宝塔連動〕
- 補注 O 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 15 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-10 完走 → 2026-05-12 retrofit 11/12/13/14/15 完走に到達。retrofit 15 完走〔法華経 薬草喩品 三草二木連動・新規 sg14 + 既存 m215+m636 を書き下し anchor 二重採用（系統対比型）・連動軸十系統並立に到達・anchor 同士の二重所属が初例〕。本体 motifs.json は 758 件・2,620,393 bytes・schema_history 73 件。motifs_index_design.md §2 に補注 O 追加〔補注 A-O 全 15 件 intact・130,096 bytes〕。CLAUDE.md は 262,035 bytes〔retrofit 4-15 全エントリ intact〕。連動軸十系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636（m636 は sg10/sg14 二系統二重所属）〕の anchor 自己参照タグ運用が完全整合に到達。法華経内部の六段構成〔迹門五段（諸法実相＋四譬：火宅三車・良医病子・化城宝処・三草二木）＋本門一段（多宝塔）〕も成立。系統対比型二重 anchor 体制の retrofit 11/13 以来の再採用例（第三例）。法華経 迹門 正宗分の中核譬を初の独立軸化。法華経 譬喩別軸 五譬完成体に到達。anchor 同士の二重所属が初例（m636 sg10/sg14）。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit15_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit14_complete.md`〔retrofit 14 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-O 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・758 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 15 commit です。

【本セッションの選択肢】
(A) retrofit 16 候補〔法華経譬喩別軸：信解品 長者窮子 m717 温存／五百弟子授記品 衣裏珠／従地涌出品 地涌の菩薩 m222・m639 温存／観世音菩薩普門品 三十三応身。薬王菩薩本事品 焼身供養はスコープ外確定〕
(B) retrofit 16 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸十系統 anchor 完全整合済の素材プール活用〔特に sg14 三草二木は法華迹門 正宗分 一乗教判の理論基盤として kaimyo-app の一切衆生悉皆成仏 関連教学解説に最適〕
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 単独 anchor 体制（補注 J/N 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O 案 A 二重版）は譬喩の典籍系統的分布に応じて柔軟に選択
- 本体 motifs.json は 2,620,393 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須。可能な限り Python script の `path.write_bytes(data)` を使用

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-12〔retrofit 15 完走・法華経 薬草喩品 三草二木連動 retrofit。新規 sg-id sg14「三草二木」を追加〔出典:法華経 薬草喩品「其雲所雨一味之水、草木叢林、随分受潤・各得生長」「仏平等説、如一味雨、随衆生性、所受不同」〕、書き下し anchor として **m215 + m636 を二重採用**（系統対比型・retrofit 11/13 同型）：m215（性霊集 第六巻 idx=44 桓武皇帝法華達嚫・「雲雨覆い澍いで而も煩を解き、草木滋く茂して而も果を結ぶ」・「草木」「雲雨」kakikudashi 直接含有・典故:法華経薬草喩品 タグ保持・性霊集 達嚫系 anchor）／m636（秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱・「一乗を三草に開く」「一雨の円音…草木の芽葉」・「三草」「草木」「一雨」kakikudashi 直接含有・既 sg10 火宅三車 m209+m636 二重 anchor の片翼・sg10/sg14 二系統二重所属・秘蔵宝鑰系 anchor）。強連動 3 motif〔m237(性霊集 第六巻 idx=45 天長皇帝故中務卿親王 檀像願文・「潤草の玉文」・性霊集 願文系)/m712(大日経疏 §51-52 金剛手三問・「時雨潤灑」雨潤・大日経疏 三句法門系)/m706(大日経疏 §45 虚空譬・「一切の草木」・大日経疏 本来性 法界系)〕に `連動:sg14`・`連動:m215`・`連動:m636` を付与（+14 タグ・m636 既存「連動:m636」重複除く・補注 K/L/M 案 A 二重版運用継承）。total_motifs 757→758（+1 新規 sg14）・famous_phrases 13→14。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,620,393 bytes〔+5,861〕・schema_history 73 件〔+1・origin: retrofit_15:doctrine〕・補注 O 追加〔motifs_index_design.md §2・115,100→130,096 bytes・+14,996〕・CLAUDE.md 更新完了〔253,981→262,035 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸十系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636（系統対比型・m636 は sg10/sg14 二系統二重所属）〕に到達——法華経内部で迹門五段（諸法実相＋四譬：火宅三車・良医病子・化城宝処・三草二木）＋本門一段（多宝塔）の六段構成に到達。**系統対比型二重 anchor 体制の retrofit 11/13 以来の再採用例**（第三例・系統対比型が譬喩別軸の標準運用形として確立）・**法華経 迹門 正宗分の中核譬を初の独立軸化**（retrofit 11-13 は迹門 具体的譬喩、retrofit 14 は本門 流通分の独立軸化）・**法華経 譬喩別軸 五譬完成体**（火宅三車・良医病子・化城宝処・多宝塔・三草二木）に到達・**anchor 同士の二重所属が初例**（m636 sg10/sg14 二系統 anchor・retrofit 14 m637 は anchor + 強連動の二重所属だったため、anchor + anchor の二重所属は本 retrofit が初例）。Phase D 必須チェックリストに完全準拠する第七の retrofit〕

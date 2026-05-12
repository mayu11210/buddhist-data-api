# 引き継ぎメモ：retrofit 17 完走〔法華経 従地涌出品 地涌の菩薩連動 retrofit〕

**日付**：2026-05-12
**フェーズ**：retrofit 17（retrofit 16 完走に続く第十四の retrofit セッション）
**対象**：法華経 従地涌出品 地涌の菩薩連動軸の新設。新規 sg-id `sg16`「従地涌出」を追加し、書き下し anchor として **m639 + m690 を二重採用**（系統対比型・秘蔵宝鑰系 vs 大日経疏系・retrofit 11/13/15 同型 第四例）：m639（秘蔵宝鑰 巻の下 第八章 一道無為心 第三節 釈文・顕密判・天台教判・「上行等の従地涌出の諸の菩薩と、一処に同会す」「常寂光土の毘盧遮那」kakikudashi 直接含有・既 sg09 諸法実相 anchor 片翼の sg09/sg16 二系統 anchor 二重所属）+ m690（大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現・法華序分対比・「法華の序分や従地湧出品の因縁の如し」kakikudashi 直接含有）。連動軸十二系統並立に到達。法華経内部の **迹門六段（諸法実相＋五譬：火宅三車・良医病子・化城宝処・三草二木・長者窮子）＋本門二段（多宝塔・従地涌出）= 八段構成** に到達。**二重 anchor 体制 系統対比型の運用第四例**（本 retrofit で初めて性霊集を含まない系統対比型が成立）。**法華経 本門 序分の中核場面を初の独立軸化**（retrofit 11-13・15-16 は迹門譬説周、retrofit 14 は本門流通分、本 retrofit で初めて本門序分を独立軸化）。**m639 の sg09/sg16 二系統 anchor 二重所属の第二例**（retrofit 15 m636 sg10/sg14 同型）。**小規模 retrofit の第二例**（retrofit 14 多宝塔 4 motif に続く 3 motif の最小規模・kakikudashi 直接含有基準の厳格適用により自然収束された運用例）。
**ステータス**：完走〔Phase A 軸設計合意・Phase B 3 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 Q 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 18 候補〔法華経譬喩・場面別軸 残候補：観世音菩薩普門品 三十三応身（観音信仰一般に拡散・規模絞り込み要）／安楽行品・法師品 等の迹門残品中核句／嘱累品〜普賢菩薩勧発品 等の本門流通分残品中核句〕／弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸／大日経疏 vol1 内部体系軸 等／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸十二系統 anchor 完全整合済〕等から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_17:doctrine〕
- [x] motifs_index_design.md に補注 Q 追加済〔A-Q 全 17 件 intact・163,334 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・269,787→277,454 bytes〕
- [x] **commit_message.txt 書き換え済〔retrofit 17 用・冒頭行整合確認済・25,740 bytes〕**
- [x] handoff_2026-05-12_retrofit17_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 全角括弧バランス確認〔commit_message.txt 〔37/37・（129/129）〕／補注 Q 内部 〔15/15・（100/100）〕／CLAUDE.md 追加部分 〔20/20・balanced〕〕
- [x] サイズ差分が想定範囲内〔motifs.json +6,198／motifs_index_design.md +16,510／CLAUDE.md +7,667／commit_message.txt 19,963→25,740〕

---

## (a) 本セッションの位置づけ

retrofit 16 完走〔法華経 信解品 長者窮子連動・新規 sg15 + 既存 m717 を書き下し anchor 単独採用・commit `5c94155`〕に続く第十四の retrofit セッション。

retrofit 16 完走 handoff §(c) 選択肢 A〔retrofit 17 候補：法華経譬喩別軸 残候補〕に着手。2026-05-12 にケンシン裁定で「従地涌出品 地涌の菩薩軸」を選定し、判断 1-5 を 1 セッション内で連続裁定〔(1) 中心成句 = 従地涌出、(2) 書き下し anchor = m639 + m690 二重採用（系統対比型）、(3) 規模 anchor 2 + 強連動 1 = 3 motif、(4) 強連動 m222、(5) 補注 K/L/M/O 案 A 二重版継承〕。Phase A〜D を 1 commit にまとめて完走する方針で進行。

**本 retrofit の特徴**：

- 新規 sg-id `sg16`「従地涌出」を追加〔出典:法華経 従地涌出品「諸の菩薩摩訶薩、無量千万億にして同時に踊出す」「上行・無辺行・浄行・安立行と名づく」「此の諸の菩薩は、我が娑婆世界自に従って涌き出ずる所なり」〕
- 書き下し anchor は **二重採用**（系統対比型・retrofit 11/13/15 同型 第四例）：m639（秘蔵宝鑰 巻の下 第八章 一道無為心 第三節 釈文・顕密判・天台教判・**既 sg09 諸法実相 anchor 片翼の sg09/sg16 二系統 anchor 二重所属**） + m690（大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現・法華序分対比）
- 強連動 1 motif（anchor 2 + 強連動 1 = 計 3 motif）に「連動:sg16」「連動:m639」「連動:m690」を付与（+9 タグ・補注 K/L/M/O 案 A 二重版運用継承）
- 法華経内部で迹門六段（諸法実相 sg09・火宅三車 sg10・良医病子 sg11・化城宝処 sg12・三草二木 sg14・長者窮子 sg15）＋本門二段（多宝塔 sg13・従地涌出 sg16）の **八段構成** に到達
- 連動軸十二系統並立に到達
- **二重 anchor 体制 系統対比型の運用第四例**：retrofit 11/13/15 は性霊集系を片翼に含む系統対比型だったが、本 retrofit は秘蔵宝鑰系 m639 vs 大日経疏系 m690 の系統対比型で **本 retrofit で初めて性霊集を含まない系統対比型が成立**。性霊集 m222 は「踊出の瑞」kakikudashi 直接含有のみで成句「従地涌出」自体は含まないため強連動に降格された判定
- **法華経 本門 序分の中核場面を初の独立軸化**：retrofit 11-13・15-16 は迹門譬説周の具体的譬喩、retrofit 14 は本門流通分（多宝塔）の独立軸化に対し、本 retrofit で初めて **本門 序分（従地涌出品）** の中核場面を独立軸化
- **anchor 二重所属の運用第二例**：m639 が sg09 諸法実相 anchor / sg16 従地涌出 anchor の二系統 anchor として運用される構造は retrofit 15 m636 sg10/sg14 同型の第二例
- **小規模 retrofit の第二例**：retrofit 14 多宝塔（4 motif）に続く 3 motif の最小規模・kakikudashi 直接含有基準の厳格適用により自然収束

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg16 =「従地涌出」（4 字成句・法華経 従地涌出品 の品名そのもの・最も流通・sg10「火宅三車」「三草二木」「長者窮子」と同型の 4 字構成）
- **判断 2**：書き下し anchor = m639 + m690 二重採用（案 A・系統対比型・retrofit 11/13/15 同型 第四例）
- **判断 3**：規模 = anchor 2 + 強連動 1 = 3 motif（最小規模・kakikudashi 直接含有基準の厳格適用により自然収束）
- **判断 4**：強連動 1 件 = m222（性霊集 第六巻 idx=44 桓武皇帝奉為太上御書金字法華講達嚫・「踊出の瑞」kakikudashi 直接含有・「典故:法華経従地涌出品」タグ保持）
- **判断 5**：二重 anchor タグ運用 = 補注 K/L/M/O 案 A 二重版〔retrofit 11/13/15 と同型ルール継承・全 motif に「連動:sg16」「連動:m639」「連動:m690」の 3 タグ付与・m639 は既存「連動:sg09」「連動:m637」を保持しつつ新規 3 タグ追加〕

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

**Phase A 自動スキャン**：retrofit 16 完走 handoff §(c) 残候補 3 候補（衣裏珠／地涌の菩薩／三十三応身）を一括スキャン：

| 候補 | kakikudashi 直接 | 全本文 | タグ保有 | anchor 候補 | 判定 |
|---|---:|---:|---:|---|---|
| P1 五百弟子授記品 衣裏珠 | 0〜1 件〔核心 keyword「衣裏」「繋珠」「酔人」「親友」kaki 直接含有 0 件・「酔児」kaki 1 件 = m70（既 sg11 良医病子 anchor）〕 | 32 件 | 1 件 m70 | anchor 確立不可〔m70 の衣裏珠言及は gendaigoyaku 補注のみ〕 | **スコープ外確定** |
| P2 従地涌出品 地涌の菩薩 | 5 件〔m222「踊出の瑞」・m639「上行等の従地涌出」・m690「法華の序分や従地湧出品」・m671（三教指帰 別文脈・除外）・m92（位階「上行」別文脈・除外）〕 | 4 件 | 1 件 m222 | m222・m639・m690 の 3 軸 | **採用** |
| P3 観世音菩薩普門品 三十三応身 | 21 件〔観音信仰一般に拡散・「三十三」kaki 直接含有 0 件〕 | 41 件 | 1 件 m440 | 規模絞り込み困難 | **次 retrofit 候補に温存** |

判定結果：

- 「衣裏」「繋珠」「酔人」「親友」（衣裏珠譬の核心 keyword）の kakikudashi 直接含有が全て 0 件で、空海著作中に衣裏珠譬の正面引用が存在しない → 衣裏珠は **anchor 確立不可・スコープ外確定**（薬王菩薩本事品 焼身供養と同型判定・retrofit 15 で薬王菩薩本事品スコープ外確定に続く第二例）
- 「従地涌出」kakikudashi 直接含有が m639 + m690 の 2 件・「踊出」kakikudashi 直接含有が m222 の 1 件・計 3 motif が明確に成句対応 → 地涌の菩薩軸は **採用可能**
- 「三十三」kakikudashi 直接含有が 0 件で観音信仰一般に拡散しているため絞り込み設計が retrofit 17 単位では重い → 三十三応身は **次 retrofit 候補に温存**

判断 2 anchor 選定の検討：

- 案 A：m639 単独（秘蔵宝鑰系のみ・既 sg09 片翼の二重所属）
- 案 B：m690 単独（大日経疏系のみ・新規 anchor）
- 案 C：m639 + m690 二重（系統対比型：秘蔵宝鑰 vs 大日経疏）
- 案 D：m222 + m639 二重（性霊集 vs 秘蔵宝鑰・但し m222 は「踊出」のみで成句「従地涌出」直接含有なし）
- 案 E：m222 単独（性霊集系のみ・「踊出」のみで成句との直接対応が弱い）

ケンシン裁定で **案 C：m639 + m690 二重採用（系統対比型・秘蔵宝鑰 vs 大日経疏）** を採用。理由：(1)「従地涌出」kakikudashi 直接含有が m639 と m690 の 2 件で系統対比成立、(2) m639 が既 sg09 諸法実相 anchor 片翼として sg09/sg16 二系統 anchor 二重所属の構造を成立させ、retrofit 15 m636 sg10/sg14 二重所属に続く第二例として運用基盤拡張に寄与する、(3) m690 が大日経疏 vol1 §22 で法華経 本門 序分の地涌瑞相を「彼の疑問に因んでこれを演説すれば、すなわち聞者の信楽は倍増して深く語義に入る。法華の序分や従地湧出品の因縁の如し」と引用し、毘盧遮那の差別智身による法門開示の論理基盤として運用する正面引用例である点、(4) 性霊集 m222 は「踊出」のみで成句「従地涌出」自体は含まないため強連動に降格して系統対比の純度を高める判定。

### Phase B：3 motif の判定表

| m-id | 出典 | kakikudashi keyword 直接含有 | 既存連動タグ | 既存関連タグ（主要） | 系統 | 役割 | 採否 |
|---|---|---|---|---|---|---|---|
| m639 | 秘蔵宝鑰 巻の下 第八章 一道無為心 第三節 釈文・顕密判・天台教判 | 「上行等の従地涌出の諸の菩薩と、一処に同会す」「常寂光土の毘盧遮那」（従地涌出 1 + 涌出 1 + 上行 1） | 連動:sg09 / 連動:m637 | category:大師御言葉・category:教判・category:密教教学・主題:一道無為・主題:法華三昧・主題:如実知自心・主題:顕密二教・密教:法身・密教:大日・典故:大日経・典故:大日経疏・典故:大智度論・典故:中論・典故:法華経・出典:秘蔵宝鑰 | 秘蔵宝鑰 顕密判・天台教判系 | **anchor**（二重・系統対比型・秘蔵宝鑰系・既 sg09 諸法実相 anchor 片翼・sg09/sg16 二系統 anchor 二重所属） | **採用** |
| m690 | 大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現・法華序分対比 | 「法華の序分や従地湧出品の因縁の如し」「普賢、秘密主等の上首の諸の仁者は、すなわちこれ毘盧遮那の差別智身なり」（従地涌出/湧出 1 + 涌出 1 + 普門 1） | なし | category:密教教学・主題:法身・主題:本来性・密教:毘盧遮那・密教:曼荼羅・典故:大日経・典故:法華経・出典:大日経疏 巻第一・出典:§22 身無尽荘厳蔵奮迅示現 | 大日経疏 vol1 §22 法華序分対比系 | **anchor**（二重・系統対比型・大日経疏系） | **採用** |
| m222 | 性霊集 第六巻 idx=44 桓武皇帝奉為太上御書金字法華講達嚫 | 「釈迦再び生れて鷲嶺の会輻湊し、四衆重ねて集り、踊出の瑞、森羅なり」（踊出 1） | なし | category:供養・category:讃美・category:典故引用・主題:四衆重集踊出瑞・主題:釈迦再生鷲嶺会輻湊・故人:天皇・故人:父・典故:法華経従地涌出品・典故:法華経霊鷲山・場面:四衆重集踊出瑞・出典:性霊集_idx44・出典:第六巻・出典:達嚫 | 性霊集 達嚫系 | 強連動 | **採用** |
| m28 | 性霊集 第八巻 idx=74 孝子先妣周忌曼荼羅供養表白 | kaki 直接含有なし（補注由来検出のみ） | なし | category:廻向・category:発願・category:密教教学・故人:母・密教:曼荼羅・典故:涅槃経・典故:法華経 | 性霊集 願文系 | — | スコープ外（kaki 直接含有基準で除外） |
| m92 | 性霊集 第七巻 idx=55 笠大夫先妣大曼荼羅願文 | 「弟子従五位上行左衛門」位階「上行」kaki 直接含有 | なし | category:帰命・category:景気導入・category:密教教学・category:讃美・故人:在家女性・故人:母 | 位階文脈・別文脈 | — | スコープ外（地涌四菩薩の上行菩薩とは別文脈・除外） |
| m671 | 三教指帰 巻の下 第三章 §15 三界六趣無常 | 「牛頭・馬頭、自然に涌出して」kaki 直接含有 | なし | category:典故引用・category:大師御言葉・主題:慈悲・主題:無常・主題:衆生救済 | 三教指帰 六趣輪廻系・別文脈 | — | スコープ外（六趣輪廻の鬼界涌出別文脈・除外） |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 759 | 760 | +1（sg16 新規追加） |
| ファイルサイズ | 2,627,741 bytes | 2,633,939 bytes | +6,198 |
| 連動タグを持つ motif | 61 | 64 | +3（m639/m690/m222 新規連動） |
| 連動タグ総数 | — | — | +9（m639 +3 / m690 +3 / m222 +3） |
| famous_phrases | 15 | 16 | +1（sg16 追加で recompute） |
| schema_history 件数 | 74 | 75 | +1（origin: retrofit_17:doctrine） |
| kakikudashi_chars_total | 112,787 | 112,791 | +4（「従地涌出」4 字） |
| gendaigoyaku_chars_total | 309,191 | 310,796 | +1,605（sg16 description） |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 760 vs 760 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、extra=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔3 motif × 3 tags〕 | missing=[] ✓ |
| 7 | sg16 配列追加〔末尾 pos=759〕 sg01-sg16 連番 | ✓ |

### Phase D：補注 Q 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 Q〔法華経 従地涌出品 地涌の菩薩連動の運用〕新規追加〔146,824→163,334 bytes・+16,510 bytes〕。anchor 構成表（二重 anchor 体制・系統対比型・retrofit 11/13/15 同型 第四例）・追加連動タグ値表・二重 anchor タグ運用ルール（補注 K/L/M/O 案 A 二重版継承）・m639 の sg09/sg16 二系統 anchor 二重所属（第二例）・retrofit 17 実施結果・設計上の論点 8 項目〔(i) 二重 anchor 体制 系統対比型の運用第四例／(ii) 連動軸十二系統並立／(iii) 法華経 譬喩・場面別軸 七譬完成体／(iv) 法華経 本門 序分の中核場面を初の独立軸化／(v) anchor 二重所属の運用第二例／(vi) kakikudashi 直接含有基準の小規模 retrofit への適用／(vii) 法華経内部の八段構成の完成と今後の展開／(viii) schema_history origin タグの定着〕を明文化。補注 A-Q 全 17 件 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 17 完走エントリを追加〔269,787→277,454 bytes・+7,667 bytes〕。retrofit 4-17 全エントリ intact 確認済。NUL バイト 0 件確認。全角〔/〕balanced 697/697〔追加部分 +20/+20〕。
- `commit_message.txt` を retrofit 17 用に完全書き換え〔25,740 bytes・NUL 0・冒頭行整合確認済・全角括弧 37/37・（129/129）〕。冒頭行を「retrofit 17 完走：法華経 従地涌出品 地涌の菩薩連動 retrofit〔新規 sg16「従地涌出」+ 既存 m639+m690 を書き下し anchor 二重採用（系統対比型 第四例・秘蔵宝鑰系 vs 大日経疏系）・連動軸十二系統並立に到達・法華経内部 八段構成完成・m639 が sg09/sg16 二系統 anchor 二重所属 第二例・法華経 本門 序分の中核場面を初の独立軸化〕」として、Phase D 必須チェックリストに完全準拠。Python `write_bytes` 直接書き込み方式で作成。

### 設計上の新規ポイント

#### (i) 二重 anchor 体制 系統対比型の運用第四例〔本 retrofit で初めて性霊集を含まない系統対比型が成立〕

retrofit 11 sg10/m209+m636（性霊集 vs 秘蔵宝鑰）・retrofit 13 sg12/m227+m569（性霊集 vs 秘蔵宝鑰）・retrofit 15 sg14/m215+m636（性霊集 vs 秘蔵宝鑰）の三例で系統対比型二重 anchor 体制が確立。本 retrofit 17 sg16/m639+m690（秘蔵宝鑰 vs 大日経疏）は **本 retrofit で初めて性霊集を含まない系統対比型** が成立する事例。譬喩・場面 keyword の典籍系統的分布が性霊集に正面引用を持たない場合の柔軟運用形として確立。これは補注 N で明示化した「単独／二重 anchor は譬喩の典籍系統的分布に応じて柔軟に選択」運用方針のさらなる拡張で、今後の retrofit で「単独 anchor 体制（retrofit 10/14/16）vs 二重 anchor 体制 性霊集系を含む系統対比型（retrofit 11/13/15）vs 二重 anchor 体制 性霊集系を含まない系統対比型（本 retrofit 17）vs 文体対比型（retrofit 12）」の四つの運用パターンから自由選択可能になる。

#### (ii) 連動軸十二系統並立に到達

本 retrofit で連動軸は以下の十二系統が並立：

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
| 三草二木 | sg14 | m215 + m636（二重・系統対比型・m636 は sg10/sg14 二系統 anchor 二重所属） | 連動:sg14・連動:m215・連動:m636 | retrofit 15 |
| 長者窮子 | sg15 | m717（単独） | 連動:sg15・連動:m717 | retrofit 16 |
| **従地涌出** | **sg16** | **m639 + m690（二重・系統対比型・m639 は sg09/sg16 二系統 anchor 二重所属）** | **連動:sg16・連動:m639・連動:m690** | **retrofit 17（本 retrofit）** |

kaimyo-app は十二の教学テーマで素材プールを切替可能：即身成仏／菩薩道の三句／般若空観／密教空観／法華空観（諸法実相）／法華譬喩（火宅三車・三乗教判）／法華譬喩（良医病子・方便涅槃）／法華譬喩（化城宝処・方便引導／顕密二教判）／法華本門（多宝塔・本門宝塔湧現／二仏同座）／法華譬喩（三草二木・一味雨潤／一乗教判）／法華譬喩（長者窮子・自心実知／衆生本有）／法華本門（従地涌出・本門序分／久遠実成）。

#### (iii) 法華経 譬喩・場面別軸 七譬完成体に到達

retrofit 11 sg10「火宅三車」（譬喩品 三乗教判）・retrofit 12 sg11「良医病子」（如来寿量品 方便涅槃）・retrofit 13 sg12「化城宝処」（化城喩品 方便引導／顕密二教判）・retrofit 14 sg13「多宝塔」（見宝塔品 本門宝塔湧現／二仏同座）・retrofit 15 sg14「三草二木」（薬草喩品 一味雨潤／一乗教判）・retrofit 16 sg15「長者窮子」（信解品 自心実知／衆生本有）・retrofit 17 sg16「従地涌出」（従地涌出品 本門序分／久遠実成）の **七譬完成体** に到達。さらに retrofit 10 sg09「諸法実相」（方便品 抽象核心）と合わせて、法華経 内部における **迹門六段（諸法実相＋五譬：火宅三車・良医病子・化城宝処・三草二木・長者窮子）＋本門二段（多宝塔・従地涌出）= 八段構成** が形成される。

#### (iv) 法華経 本門 序分 の中核場面を初の独立軸化

retrofit 10 sg09「諸法実相」は方便品 法説周（迹門第一周）の抽象核心、retrofit 11-13・15-16 は迹門譬説周の具体的譬喩（火宅三車・良医病子・化城宝処・三草二木・長者窮子）の独立軸化、retrofit 14 sg13「多宝塔」は **本門 流通分**（見宝塔品）の独立軸化に対し、本 retrofit 17 で初めて **法華経 本門 序分**（従地涌出品）の中核場面を独立軸化。法華経 本門は序分（従地涌出品）＋正宗分（如来寿量品）＋流通分（見宝塔品〜普賢菩薩勧発品）の三段で構成され、本門 序分の地涌瑞相が本門 正宗分の久遠実成を引き出す論理的前提となるため、本 retrofit で本門序分独立軸化が成立することで法華経 本門の構造的二段（多宝塔＝流通分／従地涌出＝序分）が連動軸として明示化される。

#### (v) anchor 二重所属の運用第二例

m639 が sg09 諸法実相 anchor / sg16 従地涌出 anchor の二系統 anchor として運用される構造は retrofit 15 m636 の sg10/sg14 二重所属に続く第二例。単一 motif が複数の連動軸 anchor として運用される構造は (1) その motif が連動軸成句を kakikudashi に複数同時に直接含有する場合、(2) 当該 motif が複数の教学的中核論を一節内で展開する場合、(3) 連動軸成句の典籍系統的分布が当該 motif の系統と重なる場合に成立。m639 は秘蔵宝鑰 巻の下 第八章 一道無為心 第三節 で「諸法実相」と「従地涌出」を同一節内で展開する稀有な motif で、法華経 迹門（方便品 諸法実相）と本門（従地涌出品 地涌の菩薩）を一括包摂する空海独自の天台教判運用拠点として機能する。今後の retrofit でも同様の二重所属事例が増加することで、連動軸間の交差構造が motif レベルで明示化される基盤となる。

#### (vi) kakikudashi 直接含有基準の小規模 retrofit への適用〔小規模 retrofit の第二例〕

本 retrofit は kakikudashi 直接含有を厳格基準とした結果、対象 motif が anchor 2 + 強連動 1 = 3 motif の小規模 retrofit に自然に収束した。これは retrofit 14 多宝塔（4 motif）に続く **第二の小規模 retrofit** で、kaki 直接含有基準が retrofit 規模を客観的に決定する運用基盤として機能していることを示す（過去 retrofit 5-13・15-16 は 4-9 motif の中規模が多数）。性霊集側に「踊出」含有 m222 が 1 件のみ、それ以外の「地涌」「従地涌出」「涌出」直接含有が m639・m690 の 2 件のみという典籍系統的分布が、強制的に小規模を要請する。今後の譬喩別軸（衣裏珠・観音三十三応身等）でも kaki 直接含有基準の厳格適用により自然な規模絞り込みが期待される。

#### (vii) 法華経内部の八段構成の完成と今後の展開

本 retrofit で法華経内部の連動軸構造は迹門六段（諸法実相＋五譬：火宅三車・良医病子・化城宝処・三草二木・長者窮子）＋本門二段（多宝塔・従地涌出）の八段構成に到達。残候補は (i) 五百弟子授記品 衣裏珠（kaki 直接含有 0 件のためスコープ外確定推奨・本 retrofit Phase A スキャンで確定）・(ii) 観世音菩薩普門品 三十三応身（観音信仰一般に拡散・規模絞り込み要・kaki 直接含有 21 件 + 全文 41 件と最大規模だが「三十三」kaki 直接含有 0 件のため絞り込み必要）・(iii) 安楽行品・法師品 等の迹門残品の中核句・(iv) 嘱累品〜普賢菩薩勧発品 等の本門 流通分残品の中核句。これらは将来の retrofit で順次追加可能だが、kaki 直接含有基準の厳格適用により採択範囲は限定的になる見込み。kaimyo-app 側では本 retrofit 17 で完成した八段構成を基本骨格として、法華経 迹門/本門の弁別駆動辞書を構築可能。特に sg16「従地涌出」は法華経 本門 序分の中核場面として、kaimyo-app の久遠実成・常寂光土・毘盧遮那差別智身関連教学解説への直結が極めて強い。

#### (viii) Phase D 必須チェックリストの完全運用化（retrofit 17 で 9 回目の完走）

retrofit 9 が初の完全準拠、retrofit 10-16 が 2-8 回目、本 retrofit 17 で 9 回目の完全準拠 retrofit として位置づく。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 17 完走：法華経 従地涌出品 地涌の菩薩連動 retrofit〔新規 sg16「従地涌出」+ 既存 m639+m690 を書き下し anchor 二重採用（系統対比型 第四例・秘蔵宝鑰系 vs 大日経疏系）・連動軸十二系統並立に到達・法華経内部 八段構成完成・m639 が sg09/sg16 二系統 anchor 二重所属 第二例・法華経 本門 序分の中核場面を初の独立軸化〕」が本セッション内容と完全整合。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 18〔法華経譬喩・場面別軸 残候補〕

連動軸の譬喩・場面別細分化（本 retrofit の延長）：

- **観世音菩薩普門品 三十三応身**（観音信仰一般に拡散・規模絞り込み要・kaki 直接含有 21 件 + 全文 41 件・「三十三」kaki 直接含有 0 件のため絞り込み必要・「観音」「観世音」「普門」「応身」「応現」「随類」keyword の精査要）
- **法師品 (第十)**（迹門の経典受持・読誦・解説の中核品・「五種法師」「四安楽行」keyword）
- **安楽行品 (第十四)**（迹門 流通分の中核品・「四安楽行」「行処・親近処」keyword）
- **嘱累品〜普賢菩薩勧発品 (第二十二〜二十八)**（本門 流通分の中核品群・「神力品」「嘱累品」「薬王菩薩本事品」「妙音菩薩品」「陀羅尼品」「妙荘厳王本事品」「普賢菩薩勧発品」）
- **五百弟子授記品 衣裏珠**：kakikudashi 直接含有 0 件のため anchor 確立不可・**スコープ外確定**（本 retrofit Phase A で確定）
- **薬王菩薩本事品 焼身供養**：kakikudashi 直接含有 0 件のため anchor 確立不可・**スコープ外確定**（retrofit 15 Phase A で確定）
- 規模 3-7 motif 前後・小規模

### 選択肢 B：retrofit 18 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸／大日経疏 内部体系軸 等〕

- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ。sg12（化城宝処）が顕密判の譬喩別軸として位置づいているため、本軸はその抽象的・体系的版に当たる
- 秘蔵宝鑰 十住心：「十住心」を anchor に、住心論系 motif を紐づけ
- 大日経疏 vol1 内部体系：retrofit 16 で確立した「単一著作内部の連節関係を連動軸として明示化」運用を継続して、大日経疏 vol1 の §1-§99 の主要節点を体系軸化

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸十二系統 anchor 完全整合済〕

本 retrofit で連動軸十二系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg16」を持つ 3 motif → 従地涌出連動素材プール（法華本門 序分・地涌瑞相・本仏寿量長遠・常寂光土・毘盧遮那差別智身）
- 「連動:m639」「連動:m690」の anchor 検索でそれぞれ 3 件全件取得可能（補注 K/L/M/O 二重 anchor 設計）
- m639 は sg09/sg16 二系統 anchor 二重所属（法華経 迹門 諸法実相 + 本門 序分 従地涌出を一括包摂する空海独自の天台教判運用拠点）
- 二重 anchor 体制 系統対比型の完全整合（性霊集系を含まない秘蔵宝鑰系 vs 大日経疏系の対比形）
- 法華経内部の八段構成検索：「諸法実相（抽象核心）」 vs 「火宅三車（三乗教判）」 vs 「良医病子（方便涅槃）」 vs 「化城宝処（方便引導／顕密二教判）」 vs 「多宝塔（本門宝塔湧現／二仏同座）」 vs 「三草二木（一味雨潤／一乗教判）」 vs 「長者窮子（自心実知／衆生本有）」 vs 「従地涌出（本門序分／久遠実成）」の弁別
- 譬喩・場面別軸の追加準備〔retrofit 18 以降の三十三応身・法師品・安楽行品 等への拡張〕
- **特に従地涌出軸は法華経 本門 序分の中核場面を初導入したため、kaimyo-app の久遠実成・常寂光土・毘盧遮那差別智身・本門教学解説への直結が極めて強い**

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 二重 anchor 体制 系統対比型の運用第四例として確立〔本 retrofit で初めて性霊集を含まない系統対比型が成立〕

retrofit 11/13/15 の三例で性霊集系を片翼に含む系統対比型二重 anchor 体制が確立したのに対し、本 retrofit 17 は秘蔵宝鑰系 vs 大日経疏系の対比で **本 retrofit で初めて性霊集を含まない系統対比型** が成立。譬喩・場面 keyword の典籍系統的分布で単独/二重 + 性霊集含有/不含有 を柔軟に選択する運用方針が定着。将来の譬喩・場面別軸でも、譬喩 keyword の含有が一拠点集中なら単独 anchor、性霊集系・秘蔵宝鑰系に分散なら二重 anchor（系統対比型・性霊集を片翼に含む or 含まない）、同一系統内で文体差があれば二重 anchor（文体対比型）を選択可能。

### (d-2) 法華経 本門 序分 の中核場面を初の独立軸化

過去 retrofit が法華経 迹門（諸法実相・火宅三車・良医病子・化城宝処・三草二木・長者窮子）と本門 流通分（多宝塔）の独立軸化を中心としていたのに対し、本 retrofit は **法華経 本門 序分（従地涌出品）の中核場面を初の独立軸化**。法華経 本門は序分（従地涌出品）＋正宗分（如来寿量品）＋流通分（見宝塔品〜普賢菩薩勧発品）の三段で構成され、本門 序分の地涌瑞相が本門 正宗分の久遠実成を引き出す論理的前提となるため、本 retrofit で本門序分独立軸化が成立することで法華経 本門の構造的二段が連動軸として明示化される。今後の retrofit で本門 正宗分（如来寿量品）の独立軸化が成立すれば、法華経 本門の三段全てが連動軸として明示化される。

### (d-3) Phase A 自動スキャンの keyword リスト運用継続

retrofit 15 §(d-3)・retrofit 16 §(d-3) で確立したキーワードリスト拡張による発見的補完運用を本 retrofit でも継続。本 retrofit では Phase A 自動スキャンで「地涌・従地涌出・涌出・踊出・湧出・従地・六万恒河沙・三千大千・大地震裂・下方虚空・本化・上行・無辺行・浄行・安立行 等」を網羅したため、人手レビューでの追加発見は発生せず。将来の retrofit でも Phase A 自動スキャン後の人手レビューで keyword リスト不備による見落としを救う運用が継続される。

### (d-4) Write tool truncate 事象の予防対策（本 retrofit で 0 件発生）

本 retrofit では Python script を bash heredoc + write_bytes 方式または Write tool + NUL 検証で書き込みする運用を全面採用したため、Write tool truncate 事象は発生せず。retrofit 9-15 で複数回再発生した事象を継続予防。CLAUDE.md 更新時のみ Python script の検証段階で NameError が発生したが、書き込み自体は成功し（277,454 bytes・想定値と一致）、再検証で全 pass を確認。

### (d-5) CLAUDE.md 全角括弧バランス維持

CLAUDE.md は本 retrofit 前は 〔/〕各 677 件で完全バランス、本 retrofit 後は 〔/〕各 697 件で完全バランス維持（+20 件・追加部分も balanced）。半角（）には -1 の pre-existing 差分があるが、本 retrofit の追加部分は内部 balanced。retrofit 16 で末尾形式を誤りロールバック事案があった件は本 retrofit で予防：retrofit 16 のタイトル行末尾形式「Phase D 必須チェックリストに完全準拠する第八の retrofit。引き継ぎメモ：handoff_2026-05-12_retrofit16_complete.md〔ASCII 名〕」を厳密に踏襲して「Phase D 必須チェックリストに完全準拠する第九の retrofit。引き継ぎメモ：handoff_2026-05-12_retrofit17_complete.md〔ASCII 名〕」として記述（最終更新行も同型）。

### (d-6) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9-16 で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を継続採用。最終検証で NUL 0 件確認。

### (d-7) retrofit 17 後の motifs.json サイズ

retrofit 17 で +6,198 bytes〔2,627,741 → 2,633,939 bytes〕。retrofit 16〔+7,348〕・retrofit 15〔+5,861〕・retrofit 14〔+4,293〕・retrofit 13〔+5,407〕・retrofit 12〔+4,529〕・retrofit 11〔+3,314〕・retrofit 10〔+2,383〕・retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 14 連続で +1,000〜8,000 bytes 規模の retrofit。本 retrofit は anchor 二重・規模 3 motif で retrofit 14 多宝塔（4 motif）と同程度の小規模。新規 sg16 motif の description 1,605 字（過去：sg13 多宝塔 793 字／sg14 三草二木 856 字／sg15 長者窮子 1,276 字 を上回り過去最長）。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-8) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg16 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg16 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg15 と同方針）。gendai_gabun_chars_total も 154,931 維持。kakikudashi_chars_total は +4 字（「従地涌出」4 字）、gendaigoyaku_chars_total は +1,605 字（sg16 description）増加。

### (d-9) git 状態の異常（retrofit 14-16 §(d-9) 同型・継続中の可能性）

本セッション開始時に retrofit 16 §(d-9) で記録の通り、git status --short 実行時に index 異常が残存する可能性を確認。commit 履歴自体は intact だが、git index に corrupt 参照が残存する状態。cleanup 系 bat + .py をケンシン側でダブルクリック実行することで整理。

### (d-10) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 6 件・バックアップ 3 件・handoff 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

### (d-11) Phase D 必須チェックリストの retrofit 17 で完全運用化（9 回目）

retrofit 9 で初の完全準拠を達成、retrofit 10-16 で 2-8 回目、本 retrofit 17 で 9 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 17 完走：法華経 従地涌出品 地涌の菩薩連動 retrofit〔新規 sg16「従地涌出」+ 既存 m639+m690 を書き下し anchor 二重採用（系統対比型 第四例・秘蔵宝鑰系 vs 大日経疏系）・連動軸十二系統並立に到達・法華経内部 八段構成完成・m639 が sg09/sg16 二系統 anchor 二重所属 第二例・法華経 本門 序分の中核場面を初の独立軸化〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔760 件・m1-m744 + sg01-sg16・2,633,939 bytes〕
- 本 retrofit build script：`outputs/retrofit17_jujiyujutsu.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit17_phaseA_scan.py`／結果：`outputs/retrofit17_phaseA_candidates.txt`
- 補注 Q 追加 script：`outputs/update_motifs_index_design_r17.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_r17.py`
- commit_message.txt 書き換え script：`outputs/write_commit_message_r17.py`
- 本 handoff 作成 script：`outputs/write_handoff_r17.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit17.json`〔retrofit 前 motifs.json・2,627,741 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit17.md`〔retrofit 前 motifs_index_design.md・146,824 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit17.md`〔retrofit 前 CLAUDE.md・269,787 bytes〕
- 前 retrofit handoff：`handoff_2026-05-12_retrofit16_complete.md`〔法華経 信解品 長者窮子連動〕
- 補注 Q 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 17 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-10 完走 → 2026-05-12 retrofit 11/12/13/14/15/16/17 完走に到達。retrofit 17 完走〔法華経 従地涌出品 地涌の菩薩連動・新規 sg16 + 既存 m639+m690 を書き下し anchor 二重採用（系統対比型 第四例・秘蔵宝鑰系 vs 大日経疏系）・連動軸十二系統並立に到達・法華経内部 八段構成完成・m639 が sg09/sg16 二系統 anchor 二重所属 第二例・法華経 本門 序分の中核場面を初の独立軸化〕。本体 motifs.json は 760 件・2,633,939 bytes・schema_history 75 件。motifs_index_design.md §2 に補注 Q 追加〔補注 A-Q 全 17 件 intact・163,334 bytes〕。CLAUDE.md は 277,454 bytes〔retrofit 4-17 全エントリ intact〕。連動軸十二系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）〕の anchor 自己参照タグ運用が完全整合に到達。法華経内部の八段構成〔迹門六段（諸法実相＋五譬：火宅三車・良医病子・化城宝処・三草二木・長者窮子）＋本門二段（多宝塔・従地涌出）〕も成立。二重 anchor 体制 系統対比型の運用第四例（本 retrofit で初めて性霊集を含まない系統対比型が成立）。法華経 本門 序分の中核場面を初の独立軸化。anchor 二重所属の運用第二例（m639 が sg09/sg16 二系統 anchor 二重所属）。小規模 retrofit の第二例（3 motif）。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit17_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit16_complete.md`〔retrofit 16 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-Q 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・760 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 17 commit です。

【本セッションの選択肢】
(A) retrofit 18 候補〔法華経譬喩・場面別軸：観世音菩薩普門品 三十三応身（観音信仰一般に拡散・規模絞り込み要）／法師品（迹門五種法師）／安楽行品（迹門四安楽行）／嘱累品〜普賢菩薩勧発品（本門流通分残品）。衣裏珠・薬王菩薩本事品は kakikudashi 直接含有 0 件のためスコープ外確定〕
(B) retrofit 18 候補〔弁顕密二教論 顕密判軸／秘蔵宝鑰 十住心軸／大日経疏 vol1 内部体系軸 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸十二系統 anchor 完全整合済の素材プール活用〔特に sg16 従地涌出は法華経 本門 序分・久遠実成・常寂光土・毘盧遮那差別智身の理論基盤として kaimyo-app の久遠遍照・本門教学解説に最適〕
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 単独 anchor 体制（補注 J/N/P 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q 案 A 二重版）は譬喩の典籍系統的分布に応じて柔軟に選択
- 本体 motifs.json は 2,633,939 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須。可能な限り Python script の `path.write_bytes(data)` を使用
- CLAUDE.md タイトル行・最終更新行の追記は過去エントリ形式（`〔...〕 ★ retrofit N-1` で繋がる形式）に厳密に従うこと〔retrofit 16 で末尾形式を誤りロールバック事案あり・retrofit 17 で踏襲確認済〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-12〔retrofit 17 完走・法華経 従地涌出品 地涌の菩薩連動 retrofit。新規 sg-id sg16「従地涌出」を追加〔出典:法華経 従地涌出品「諸の菩薩摩訶薩、無量千万億にして同時に踊出す」「上行・無辺行・浄行・安立行と名づく」「此の諸の菩薩は、我が娑婆世界自に従って涌き出ずる所なり」〕、書き下し anchor として **m639+m690 二重採用**（retrofit 11/13/15 同型・系統対比型 第四例）：m639（秘蔵宝鑰 巻の下 第八章 一道無為心 第三節・「上行等の従地涌出の諸の菩薩と、一処に同会す」「常寂光土の毘盧遮那」kakikudashi 直接含有・既 sg09 諸法実相 anchor 片翼・sg09/sg16 二系統 anchor 二重所属） + m690（大日経疏 巻第一 §22 身無尽荘厳蔵奮迅示現・法華序分対比・「法華の序分や従地湧出品の因縁の如し」kakikudashi 直接含有・大日経疏 vol1 §22 法華序分対比の核心節）。強連動 1 motif：m222（性霊集 第六巻 idx=44 桓武皇帝法華達嚫・「踊出の瑞」kakikudashi 直接含有・典故:法華経従地涌出品 タグ保持）に「連動:sg16」「連動:m639」「連動:m690」を付与（+9 タグ・補注 K/L/M/O 案 A 二重版運用継承）。total_motifs 759→760（+1 新規 sg16）・famous_phrases 15→16。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,633,939 bytes〔+6,198〕・schema_history 75 件〔+1・origin: retrofit_17:doctrine〕・補注 Q 追加〔motifs_index_design.md §2・146,824→163,334 bytes・+16,510〕・CLAUDE.md 更新完了〔269,787→277,454 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸十二系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）〕に到達——法華経内部で迹門六段（諸法実相＋五譬：火宅三車・良医病子・化城宝処・三草二木・長者窮子）＋本門二段（多宝塔・従地涌出）の八段構成に到達。**二重 anchor 体制 系統対比型の運用第四例**（過去三例 retrofit 11/13/15 は性霊集系を片翼に含むが、本 retrofit は秘蔵宝鑰系 vs 大日経疏系の対比で性霊集を含まない初例・性霊集 m222 は強連動に降格）・**法華経 譬喩・場面別軸 七譬完成体**（火宅三車・良医病子・化城宝処・多宝塔・三草二木・長者窮子・従地涌出）に到達・**法華経 本門 序分の中核場面を初の独立軸化**（retrofit 11-13・15-16 は迹門譬説周、retrofit 14 は本門流通分、本 retrofit で初めて本門 序分を独立軸化）・**anchor 二重所属の運用第二例**（m639 が sg09 諸法実相 anchor / sg16 従地涌出 anchor の二系統 anchor 二重所属・retrofit 15 m636 sg10/sg14 同型）・**小規模 retrofit の第二例**（retrofit 14 多宝塔 4 motif に続く 3 motif の最小規模・kakikudashi 直接含有基準の厳格適用により自然収束）。Phase D 必須チェックリストに完全準拠する第九の retrofit〕

# 引き継ぎメモ：retrofit 22 完走〔大日経疏 vol1 浄菩提心 教学系軸連動 retrofit〕

**日付**：2026-05-22
**フェーズ**：retrofit 22（retrofit 21 完走に続く第十九の retrofit セッション）
**対象**：『大日経』住心品・『大日経疏』巻第一に説かれる密教の菩提心論・実践論の中心概念「浄菩提心」の連動軸新設。新規 sg-id `sg21`「浄菩提心」を追加し、書き下し anchor として **二重 anchor 系統対比型 m728+m638** を採用。m728（大日経疏 巻第一 §77-79・「経に秘密主よ、この菩薩の浄菩提心門を初法明道と名く……今この宗は、直に浄菩提心をもって門とす」浄菩提心門を初法明道と規定する大日経疏の核心釈文）を大日経疏系 anchor、m638（秘蔵宝鑰 第三節 経証・「此の菩薩の浄菩提心門を、初法明道と名づく」浄菩提心門＝初法明道の経文を結ぶ大日経 引証）を秘蔵宝鑰系 anchor とする。強連動 6 motif（m632 秘蔵宝鑰 第一節 / m718 大日経疏 §59-60 / m725 §71-73 / m732 §83 / m735 §87 / m739 §91）に連動タグを付与。連動軸十七系統並立に到達。本 retrofit は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句 に続く **教学系軸の第五例**。retrofit 11 火宅三車・retrofit 13 化城宝処・retrofit 15 三草二木・retrofit 17 従地涌出 同型の **二重 anchor 体制 系統対比型の運用第五例**。anchor 2 ＋ 強連動 6 ＝ 8 motif の単一軸 retrofit としての最大規模。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 8 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 V 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 23 候補〔教学系軸：吽字義軸（中心成句要再検討）／菩提心論軸（中心成句要再検討）／般若心経秘鍵・三教指帰 等の未軸化 corpus〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_22:doctrine〕
- [x] motifs_index_design.md に補注 V 追加済〔補注 A-V 全 22 件 intact・215,343→231,348 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・313,778→324,423 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 22 用・冒頭行整合確認済〕
- [x] handoff_2026-05-22_retrofit22_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 21 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 21 完走〔即身成仏義 二頌八句 教学系軸連動・新規 sg20 + 既存 m534 を書き下し anchor 単独採用・commit `7aaeba9`〕に続く第十九の retrofit セッション。

retrofit 21 完走 handoff §(c) 選択肢 A〔retrofit 22 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で大日経疏 vol1 浄菩提心軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg21`「浄菩提心」を追加〔出典:大日経 住心品・『大日経』住心品および『大日経疏』巻第一に説かれる密教の菩提心論・実践論の中心概念・経文「この菩薩の浄菩提心門を初法明道と名づく」に由来〕
- 書き下し anchor は **二重 anchor 系統対比型 m728+m638**（m728 大日経疏 巻第一 §77-79・m638 秘蔵宝鑰 第三節 経証）
- 強連動 6 motif（m632 秘蔵宝鑰 第一節 / m718 大日経疏 §59-60 / m725 §71-73 / m732 §83 / m735 §87 / m739 §91）に「連動:sg21」「連動:m638」「連動:m728」を付与（+24 タグ）
- 連動軸十七系統並立に到達
- **教学系軸の第五例**（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句 に続く・浄菩提心は空海の菩提心論・密教実践論を主題とする）
- **二重 anchor 体制 系統対比型の運用第五例**（retrofit 11 火宅三車・retrofit 13 化城宝処・retrofit 15 三草二木・retrofit 17 従地涌出 に続く・retrofit 17 同型の秘蔵宝鑰×大日経疏 系統対比）
- **8 motif retrofit**（anchor 2 ＋ 強連動 6・単一軸 retrofit としての最大規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 21 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸十六系統（sg02/sg03/sg07-sg20）の anchor がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（retrofit 21 で sg03 anchor m533 を補整済・retrofit 22 では anchor 補整不要）。Phase A スキャンで retrofit 22 候補三件（大日経疏 vol1 浄菩提心軸／吽字義軸／菩提心論軸）の中心成句の kakikudashi 直接含有を全 764 motif にわたり網羅検査：

| 候補 | kakikudashi 支持 | 既存軸重複 | 判定 |
|---|---|---|---|
| 大日経疏 vol1 浄菩提心軸 | 「浄菩提心」14 件（大日経疏 巻第一 12・秘蔵宝鑰 2）・clean 8 件で軸構成可 | 大日経疏 12 件中 overlap 6 件（sg07×4・sg03×2・sg15×1）・clean 8 件は連動タグ overlap ゼロ | 採用 |
| 吽字義軸 | 「吽字」literal kakikudashi 直接含有 0 件・字相 3 件/字義 2 件は 3 corpus に拡散 | 中心成句不明瞭 | 基準未達・retrofit 23 以降に温存 |
| 菩提心論軸 | 「三種菩提心」「三摩地戒」kakikudashi 直接含有 0 件・「菩提心論」10 件は他典籍の引用・bodaishinron corpus 自身が中心成句を直接含有せず | — | 基準未達・retrofit 23 以降に温存 |

retrofit 22 Phase A スキャンの実測で、浄菩提心 が三句法門 sg07 と主題的に隣接するものの、clean 8 件（大日経疏 6 件 m718/m725/m728/m732/m735/m739 + 秘蔵宝鑰 2 件 m632/m638）は sg07 と連動タグ overlap がゼロであること、overlap 6 件（m715/m716/m723 は sg07・m724 は sg03/sg07・m738 は sg15・m740 は sg03）を除外して clean 8 件で軸構成が可能であることを確認。ケンシン裁定で判断 1-3：

- **判断 1**：軸採用 = 候補1 大日経疏 vol1 浄菩提心軸（clean 8 件で軸構成可・thematic adjacency と連動タグ overlap を区別し overlap 6 件を除外・retrofit 21 §(d-3) の方針適用）
- **判断 2**：中心成句 sg21 =「浄菩提心」（『大日経』住心品の経文「この菩薩の浄菩提心門を初法明道と名づく」に由来・kakikudashi 実形が「浄菩提心」一形・「清浄の菩提心」「清浄菩提心」等の表記形は 0 件）
- **判断 3**：anchor 体制・規模 = 案 B 二重 anchor 系統対比型 m728+m638・8 motif（同一経文「浄菩提心門を初法明道と名づく」を大日経疏 釈文 m728 と秘蔵宝鑰 引証 m638 の二系統で保持。案 A 単独 anchor m728・大日経疏限定 6 motif、案 C 単独 anchor m728・秘蔵宝鑰込み 8 motif を退け、同一経文を釈文と引証の二系統で保持する点を重視して案 B を採用）

### Phase B：8 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m728 | 大日経疏 巻第一 §77-79 | 書き下し anchor（大日経疏系・片翼・自己参照）・「経に秘密主よ、この菩薩の浄菩提心門を初法明道と名く……今この宗は、直に浄菩提心をもって門とす……浄菩提心をもって諸法を照明するに因るが故に……八万四千の宝聚門と成る」浄菩提心門を初法明道と規定する大日経疏の核心釈文 |
| m638 | 秘蔵宝鑰 第三節 経証 | 書き下し anchor（秘蔵宝鑰系・片翼・自己参照）・「秘密主。云何んが菩提とならば、謂く実の如くに自心を知るなり……此の菩薩の浄菩提心門を、初法明道と名づく」菩提を如実知自心と説き浄菩提心門＝初法明道の経文を結ぶ大日経 引証 |
| m632 | 秘蔵宝鑰 第一節 経証・釈文 | 強連動・「心主自在といっぱ即ち是れ、浄菩提心の更に一転の開明を作して、前劫に倍勝することを明かす」心主自在を浄菩提心の一転の開明とし、心王の本浄と覚心不生・阿字門を説く |
| m718 | 大日経疏 巻第一 §59-60 | 強連動・「この無相の菩提心を離れて外に、更に一法もなきなり」「浄菩提心は諸観を出過し、衆相を離れたる」阿耨多羅三藐三菩提の無相を虚空に喩える段 |
| m725 | 大日経疏 巻第一 §71-73 | 強連動・「世尊は前に既に広く浄菩提心の如実の相を説く……この頓覚成仏の入心実相門を説く」自心を分段顕色形色等に求めるに不可得とし、浄菩提心の如実相を心の実相門として説く自心知方便段 |
| m732 | 大日経疏 巻第一 §83 | 強連動・「浄菩提心はその性法爾として金剛の如くなるが故に……無為戒に住す」浄菩提心の法爾金剛性と尸羅清冷義を蓮華譬・水性清冷譬で説く無為戒段 |
| m735 | 大日経疏 巻第一 §87 | 強連動・「云何がこの心に菩提の種子が発生することを了知す……究竟の浄菩提心を得る」執金剛秘密主が偈をもって菩提心の生・相・次第を問う九句総挙段 |
| m739 | 大日経疏 巻第一 §91 | 強連動・「世間に更に法として、もって浄菩提心の相を表示すべき者あることなし……無量なること虚空の如し」浄菩提心の相貌を虚空譬で答え、本不生・常住不変・正等覚顕現を説く菩提心相貌段 |

体系内連節カバー：浄菩提心の経証（m638 秘蔵宝鑰 第三節・m632 秘蔵宝鑰 第一節）から、大日経疏 巻第一の §59-60 阿耨多羅三藐三菩提の無相（m718）→ §71-73 自心知方便（m725）→ §77-79 初法明道（m728 anchor）→ §83 無為戒（m732）→ §87 九句総挙（m735）→ §91 菩提心相貌（m739）にわたる浄菩提心の如実相の詳説を一括包摂。

**除外・温存**：大日経疏 巻第一 浄菩提心 12 件のうち overlap 6 件（m715・m716・m723 は三句法門 sg07 連動済／m724 は sg03・sg07 連動済／m738 は長者窮子 sg15 連動済／m740 は即身成仏 sg03 連動済）は連動タグ overlap をもち、浄菩提心と主題的に隣接するが既存軸の領域にあるため本軸には含めず温存。本軸 8 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 764 | 765 | +1（sg21 新規追加） |
| famous_phrases | 20 | 21 | +1 |
| ファイルサイズ | 2,656,569 bytes | 2,664,294 bytes | +7,725 |
| schema_history | 79 | 80 | +1（origin: retrofit_22:doctrine） |
| 連動タグ総数 | — | — | +24（sg21 軸 8 motif × 3） |
| kakikudashi_chars_total | 112,824 | 112,828 | +4（「浄菩提心」4 字） |
| gendaigoyaku_chars_total | 317,501 | 319,480 | +1,979（sg21 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 765 vs 765 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0、trailing=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg21 軸 8 motif × 3〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg21 連番・末尾 sg21 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 21 で recompute した stats は retrofit 22 着手時点で全 5 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 22 では stats を全件 recompute して真値を書き込み（total_motifs 765・famous_phrases 21・kakikudashi_chars_total 112,828・gendaigoyaku_chars_total 319,480・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。top-level generated_at は 2026-05-22T00:00:00+09:00 を維持。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 V 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 V〔大日経疏 vol1 浄菩提心 教学系軸連動の運用〕新規追加（215,343→231,348 bytes・+16,005・補注 A-V 全 22 件 intact・全角丸括弧 90/90 balanced・〔〕21/21 balanced・かぎ括弧 32/32 balanced・二重かぎ 13/13 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 22 完走エントリを追加（313,778→324,423 bytes・retrofit 4-22 全エントリ intact・追加部分の全角角括弧 40/40・かぎ括弧 9/9・二重かぎ 7/7 balanced・新規半角括弧 0 件・全角〔〕全体 1037/1037 balanced）。
- `commit_message.txt` を retrofit 22 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-22_retrofit22_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第五例・空海の菩提心論軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学、retrofit 21 即身成仏義 二頌八句軸は空海の即身成仏論を主題とする教学系軸であった。retrofit 22 浄菩提心軸はその継続でありながら、『大日経』住心品・『大日経疏』巻第一に説かれる密教の菩提心論・実践論を主題とする点に特色をもつため、教学系軸の第五例と位置づける。三句法門 sg07 が因たる菩提心の教学的綱格を anchor とするのに対し、浄菩提心 sg21 はその因たる菩提心が行者において如実に浄められ初法明道の門として現成する実践的局面を anchor とする。

#### 2. 連動軸十七系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）〕の十七系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）・即身成仏論（六大四曼三密）に加えて、菩提心論・密教実践論・本来性論（浄菩提心）でも素材プールを切替可能。

#### 3. 二重 anchor 体制 系統対比型の運用第五例

retrofit 11 sg10/m209+m636（性霊集 vs 秘蔵宝鑰）・retrofit 13 sg12/m227+m569（性霊集 vs 秘蔵宝鑰）・retrofit 15 sg14/m215+m636（性霊集 vs 秘蔵宝鑰）・retrofit 17 sg16/m639+m690（秘蔵宝鑰 vs 大日経疏）に続く第五の系統対比型。本 retrofit 22 sg21/m638+m728 は retrofit 17 sg16 と同じく秘蔵宝鑰系と大日経疏系を対比する系統対比型で、同一典籍系統の対比をなす第二例。法華経 譬喩・場面別軸（sg10-sg16）で確立した二重 anchor 系統対比型を、教学系軸において運用する初例。

#### 4. 同一経文の釈文 anchor と引証 anchor の対比

本軸の二重 anchor は、m728 が『大日経疏』巻第一における大日経 経文「この菩薩の浄菩提心門を初法明道と名づく」の釈文、m638 が『秘蔵宝鑰』第三節 経証における同一経文の引証であり、同一の経文を釈文系統と引証系統の二系統で保持する。retrofit 17 sg16 が法華経 従地涌出品の場面を秘蔵宝鑰 釈文と大日経疏 釈文の二系統で対比したのに対し、本 retrofit 22 sg21 は大日経 経文を疏（大日経疏）と引証（秘蔵宝鑰）の二系統で対比する点に特色がある。

#### 5. 三句法門 sg07 と浄菩提心 sg21 の並立・thematic adjacency と連動タグ overlap の区別

三句法門 sg07 が『大日経』住心品の教学的三句（菩提心因・大悲根・方便究竟）を anchor とするのに対し、本軸 sg21 は三句法門が開示する当体たる浄菩提心が行者に如実に浄められ初法明道の門として現成する局面を anchor とする。両軸は『大日経』『大日経疏』のうちに教学的綱格（sg07）と実践的現成（sg21）として並立する。Phase A において、浄菩提心が sg07 と主題的に隣接（thematic adjacency）するものの、clean 8 件は連動タグ overlap がゼロであることを実測し、retrofit 21 §(d-3) で確立した「thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する」方針に基づき、overlap 6 件を除外して clean 8 件で軸を構成した。

#### 6. 8 motif 規模・単一軸 retrofit の最大規模

anchor 2 ＋ 強連動 6 ＝ 8 motif は、retrofit 14-21 の小規模 retrofit（3-5 motif）、retrofit 11-13・15 の二重 anchor 譬喩別軸（4-6 motif）をも上回る、単一軸 retrofit としての最大規模。浄菩提心の経証 2 件（秘蔵宝鑰）と大日経疏 巻第一の如実相詳説 6 件を一括して連動軸化したことによる。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=765  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0 trailing=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg21軸 8motif×3 全付与  OK
7. sg list sg01-sg21 continuous, tail=sg21  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK

[stats（retrofit 22 後）]
total_motifs=765  famous_phrases=21
kakikudashi_chars_total=112,828
gendaigoyaku_chars_total=319,480
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=80 entries
file size=2,664,294 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 23〔教学系軸の継続〕

- **吽字義軸**：空海 三部書の残る一。「吽字」literal の kakikudashi 直接含有 0 件で中心成句が不明瞭。字相・字義あるいは吽字 四字（阿・訶・汙・麼）の構造を成句として再検討する余地がある。sg08 阿字本不生 anchor m549 が吽字義 corpus 内に居住するため重複の整理が要。
- **菩提心論軸**：「三種菩提心」「三摩地戒」の kakikudashi 直接含有 0 件で中心成句が不明瞭。bodaishinron corpus（15 件）自身が中心成句を直接含有しない。三種の菩提心（行願・勝義・三摩地）の構造を成句として再検討する余地がある。
- **般若心経秘鍵・三教指帰 等の未軸化 corpus**：般若心経秘鍵（15 件）・三教指帰（21 件）は独立軸が未設置。大日経疏 巻第一 corpus は 68 件中 26 件が連動タグ保有（retrofit 22 後）で 42 件が未連動であり、他主題（如実知自心 等）の軸化余地が残る。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸十七系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg21 浄菩提心（大日経疏 vol1）は菩提心論・密教実践論・本来性論を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔十六系統全件 OK〕

retrofit 21 §(d-1) の指示に従い、retrofit 22 着手時に連動軸十六系統（sg02/sg03/sg07-sg20）の anchor 自己参照タグ全件検証を実施した結果、全 anchor motif が「連動:sgNN」「連動:m(anchor)」を保有していることを確認した（retrofit 21 で sg03 anchor m533 を補整済のため欠落なし）。retrofit 22 では anchor 補整は不要であった。今後 anchor を扱う retrofit でも着手時の自己参照タグ全件検証を継続する。なお retrofit 22 で追加した sg21 二重 anchor m728・m638 も「連動:sg21」「連動:m638」「連動:m728」の自己参照タグを保有し、連動軸十七系統 anchor の自己参照タグは完全整合を維持する。

### (d-2) 浄菩提心軸と三句法門 sg07 の隣接

浄菩提心は三句法門 sg07（菩提心因・大悲根・方便究竟）と主題的に隣接する。retrofit 22 Phase A の実測で、clean 8 件（大日経疏 6 件 + 秘蔵宝鑰 2 件）は sg07 と連動タグ overlap がゼロであることを確認し、overlap 6 件（sg07×4・sg03×2・sg15×1）は温存して clean 8 件で軸を構成した。retrofit 21 §(d-3) の「thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する」方針の再運用例。

### (d-3) 大日経疏 巻第一 corpus のカバー範囲

本 retrofit は大日経疏 巻第一の §59-91（浄菩提心 motif の clean 6 件）を連動軸化した。大日経疏 巻第一 corpus は全 68 件中、retrofit 22 後で 26 件が連動タグを保有し 42 件が未連動である。三句法門 sg07・浄菩提心 sg21 のほか、如実知自心（「実の如く自心を知る」kakikudashi 直接含有は m717/m720 等）・大日経疏の他主題を将来 retrofit で軸化する余地が残る。

### (d-4) .git/index.lock 残留と除去

retrofit 22 セッション中、git status 実行時に 0 バイトの `.git/index.lock` が残留した。bash mount は `.git` ディレクトリへの unlink を許可しない（「Operation not permitted」）ため、`mcp__cowork__allow_cowork_file_delete` で削除許可を取得して除去した。commit_push.bat 実行前に lock 残留がないことを確認済。今後 git status 等の git コマンド実行後は `.git/index.lock` 残留に留意し、残留した場合は commit_push.bat 実行前に除去する。

### (d-5) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg21 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-22 で sg08-sg21 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-22 一貫して未更新の pre-existing 事象。retrofit 22 でも踏襲し未変更とした。将来 "sg01-sg21" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-6) 編集手法・truncate 事象回避

retrofit 22 のビルドスクリプト（`outputs/retrofit22_joubodaishin.py`）・Phase A スキャンスクリプト（`outputs/retrofit22_phaseA_scan.py`・`retrofit22_phaseA_scan3.py`）・検証スクリプト（`outputs/retrofit22_verify.py`）・補注 V 追加スクリプト（`outputs/add_chunote_v_retrofit22.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit22.py`）・commit_message.txt・本 handoff はすべて bash heredoc 方式で作成し、Edit/Write tool の truncate 事象を回避した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（dry-run + 本番適用の二段運用）。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。今後もスクリプト・長文ファイルの作成は bash heredoc / Python write_bytes を第一選択とすることを推奨。

### (d-7) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-21 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。

### (d-8) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 22 後で 全角〔/〕1037/1037 balanced。retrofit 22 の追加部分は全角角括弧 40 対・かぎ括弧 9 対・二重かぎ 7 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5)・retrofit 19 §(d-7)・retrofit 20 §(d-7)・retrofit 21 §(d-7) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔765 件・m1-m744 + sg01-sg21・2,664,294 bytes・schema_history 80 件〕
- 本 retrofit build script：`outputs/retrofit22_joubodaishin.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit22_phaseA_scan.py`・`outputs/retrofit22_phaseA_scan3.py`
- Phase A 結果まとめ：`outputs/retrofit22_phaseA_candidates.txt`
- 整合性検証 script：`outputs/retrofit22_verify.py`
- 補注 V 追加 script：`outputs/add_chunote_v_retrofit22.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit22.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit22.json`〔retrofit 前 motifs.json・2,656,569 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit22.md`〔retrofit 前・215,343 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit22.md`〔retrofit 前・313,778 bytes〕
  - `outputs/commit_message_backup_pre_retrofit22.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-22_retrofit21_complete.md`〔即身成仏義 二頌八句 教学系軸連動〕
- 補注 V 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 22 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-21 完走 → 2026-05-22 retrofit 22 完走〔大日経疏 vol1 浄菩提心 教学系軸連動・新規 sg21「浄菩提心」+ 二重 anchor 系統対比型 m728+m638 採用（大日経疏 巻第一 §77-79 釈文 + 秘蔵宝鑰 第三節 引証）・強連動 6 件（m632/m718/m725/m732/m735/m739）・連動軸十七系統並立に到達・教学系軸の第五例・二重 anchor 系統対比型 第五例〕。本体 motifs.json は 765 件・2,664,294 bytes・schema_history 80 件。motifs_index_design.md §2 に補注 V 追加〔補注 A-V 全 22 件 intact・231,348 bytes〕。CLAUDE.md は 324,423 bytes〔retrofit 4-22 全エントリ intact〕。連動軸十七系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）〕の anchor 自己参照タグ運用が完全整合。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit22_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit21_complete.md`〔retrofit 21 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-V 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・765 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 22 commit です。

【本セッションの選択肢】
(A) retrofit 23 候補〔教学系軸：吽字義軸（中心成句要再検討）／菩提心論軸（中心成句要再検討）／般若心経秘鍵・三教指帰 等の未軸化 corpus・大日経疏 巻第一 残 42 件の他主題軸化〕
(B) kaimyo-app 教学系素材活用：連動軸十七系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- git status 等の実行後は .git/index.lock 残留に留意〔残留時は commit_push.bat 実行前に除去・retrofit 22 §(d-4)〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)・retrofit 22 で再運用〕
- anchor を扱う retrofit では着手時に anchor 自己参照タグ全件検証を行う〔retrofit 21 §(d-1)・retrofit 22 で全件 OK 確認〕
- 単独 anchor 体制（補注 J/N/P/R/S/T/U 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q/V 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-22〔retrofit 22 完走・大日経疏 vol1 浄菩提心 教学系軸連動 retrofit。新規 sg-id `sg21`「浄菩提心」を新設〔出典:大日経 住心品〕、書き下し anchor として二重 anchor 系統対比型 m728+m638 を採用（m728 大日経疏 巻第一 §77-79「経に秘密主よ、この菩薩の浄菩提心門を初法明道と名く……今この宗は、直に浄菩提心をもって門とす」浄菩提心門を初法明道と規定する大日経疏の核心釈文／m638 秘蔵宝鑰 第三節 経証「此の菩薩の浄菩提心門を、初法明道と名づく」浄菩提心門＝初法明道の大日経 引証）。強連動 6 motif：m632（秘蔵宝鑰 第一節 経証・釈文）/ m718（大日経疏 §59-60）/ m725（§71-73）/ m732（§83）/ m735（§87）/ m739（§91）に「連動:sg21」「連動:m638」「連動:m728」を付与（+24 タグ）。total_motifs 764→765（+1 新規 sg21）・famous_phrases 20→21。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,664,294 bytes〔+7,725〕・schema_history 80 件〔+1・origin: retrofit_22:doctrine〕・補注 V 追加〔motifs_index_design.md §2・215,343→231,348 bytes・+16,005〕・CLAUDE.md 更新完了〔313,778→324,423 bytes〕・commit_message.txt 書き換え済。連動軸十七系統並立に到達。教学系軸（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句）に続く教学系軸の第五例で、空海の菩提心論・密教実践論を主題とする軸。二重 anchor 体制 系統対比型の運用第五例（retrofit 11/13/15/17 に続く・retrofit 17 同型の秘蔵宝鑰×大日経疏 系統対比）。同一経文「浄菩提心門を初法明道と名づく」を大日経疏 釈文 m728 と秘蔵宝鑰 引証 m638 の二系統で保持。三句法門 sg07（教学的綱格）と浄菩提心 sg21（実践的現成）が大日経・大日経疏のうちに並立。anchor 2 ＋ 強連動 6 ＝ 8 motif の単一軸 retrofit 最大規模。Phase D 必須チェックリストに完全準拠する第十四の retrofit〕

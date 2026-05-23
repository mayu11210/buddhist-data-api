# 引き継ぎメモ：retrofit 26 完走〔大日経疏 加持身 教学系軸連動 retrofit〕

**日付**：2026-05-23
**フェーズ**：retrofit 26（retrofit 25 完走に続く第二十三の retrofit セッション）
**対象**：空海所依の根本聖典『大日経』の註釈書『大日経疏』巻第一に説かれる、大日如来の身をめぐる密教仏身論の中心概念「加持身」の連動軸新設。新規 sg-id `sg25`「加持身」を追加し、書き下し anchor として **単独 anchor m679** を採用。m679（大日経疏 巻第一 §3-§5 序・「次に如来というは、これ仏の加持身のその所住の処にして、仏の受用身と名づく……既に遍一切処の加持力より生ず。すなわち無相法身と無二無別なり」加持身を本地法身に対する受用身と定義する大日経疏の核心句）を単独の書き下し anchor とする。強連動 4 motif（m677 §1 経題釈 神変加持 / m689 §20-§21 加持受用身 / m692 §24 遍一切加持身 / m695 §27 秘密加持）に連動タグを付与。連動軸二十一系統並立に到達。本 retrofit は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 に続く **教学系軸の第九例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 六大無礙・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 同型の **単独 anchor 体制の運用第九例**。anchor 1 ＋ 強連動 4 ＝ 5 motif の小規模 retrofit。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 5 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 Z 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 27 候補〔教学系軸：般若心経秘鍵 仏法不外求軸（m492/m493 clean・規模再検討要）／三教指帰軸／大日経疏 巻第一 残 37 件のさらなる主題軸化〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_26:doctrine〕
- [x] motifs_index_design.md に補注 Z 追加済〔補注 A-Z 全 26 件 intact・282,270→301,708 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・340,560→346,139 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 26 用・冒頭行整合確認済〕
- [x] handoff_2026-05-23_retrofit26_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 25 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 25 完走〔吽字義 吽字四字 教学系軸連動・commit `8a320d0`〕に続く第二十三の retrofit セッション。

retrofit 25 完走 handoff §(c) 選択肢 A〔retrofit 26 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で大日経疏 加持身軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg25`「加持身」を追加〔出典:大日経疏・唐の善無畏三蔵の講説を一行阿闍梨が筆録した『大日経疏』巻第一に説かれる、大日如来の身をめぐる密教仏身論の中心概念〕
- 書き下し anchor は **単独 anchor m679**（大日経疏 巻第一 §3-§5 序）
- 強連動 4 motif（m677 §1 経題釈 神変加持 / m689 §20-§21 加持受用身 / m692 §24 遍一切加持身 / m695 §27 秘密加持）に「連動:sg25」「連動:m679」を付与（+10 タグ）
- 連動軸二十一系統並立に到達
- **教学系軸の第九例**（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 に続く・加持身は大日如来の身の密教仏身論を主題とする）
- **単独 anchor 体制の運用第九例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 六大無礙・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 に続く）
- **5 motif retrofit**（anchor 1 ＋ 強連動 4・retrofit 21 即身成仏義・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門 と同規模の小規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 25 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸二十系統（sg02/sg03/sg07-sg24）の書き下し anchor がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg24）は二十系統一律に連動タグ未保有であり、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりで整合。Phase A スキャンで retrofit 26 候補（般若心経秘鍵 仏法不外求軸／三教指帰軸／大日経疏 巻第一 残 42 件他主題軸）の中心成句の kakikudashi 直接含有を全 768 motif にわたり網羅検査：

| 候補 | corpus clean 率 | kakikudashi 支持 | 判定 |
|---|---|---|---|
| 大日経疏 加持身軸 | dainichikyo-sho-vol1 未連動 42/68・うち 26 件が 主題:加持身 | 「加持」literal 17 件・経題釈 神変加持（m677）→ 序 加持身定義（m679）→ 加持受用身（m689）→ 遍一切加持身（m692）→ 秘密加持（m695）の一貫した加持身論 | 採用 |
| 般若心経秘鍵 仏法不外求軸 | hannya-hiken（本軸該当 2 件 clean） | thesis 句「仏法遥かに非ず／真如外に非ず／心中にして即ち近し」literal は m492 専属・強連動候補 m493 1 件のみで anchor＋強連動 2 motif の過去最小規模 | 基準未達・retrofit 27 以降に温存 |
| 三教指帰軸 | sankyo-shiki 21/21 完全 clean | 「三教」literal 3 件すべて枠組み motif・連動軸モデルへの適合が弱い（retrofit 4 発言者軸運用済） | 基準未達・retrofit 27 以降に温存 |

retrofit 24-25 完走 handoff は大日経疏 巻第一 残 42 件を「中心成句不明瞭」と暫定評価していたが、これは如実知自心・三劫・六無畏 をスキャンした結果であった。retrofit 26 Phase A で「加持身」を中心成句として候補語を変えてスキャンした結果、dainichikyo-sho-vol1 corpus 68 件中 未連動 42 件のうち 26 件が 主題:加持身 を保有し、「加持」literal も 17 件あって、経題釈（神変加持）→ 序（如来加持身）→ 本論（遍一切加持身）→ 清浄句義（秘密加持）にわたる一貫した加持身論の教学線が clean motif 群に存在することを確認した。ケンシン裁定で判断 1-3：

- **判断 1**：軸採用 = 大日経疏 加持身軸（dainichikyo-sho-vol1 corpus 未連動 42 件のうち 26 件が 主題:加持身・正常規模 5 motif を成立させられる候補。仏法不外求軸は 2 motif で過去最小を下回り、三教指帰軸は連動軸モデルに不適合のため退けた）
- **判断 2**：中心成句 sg25 =「加持身」（『大日経疏』巻第一が毘盧遮那の身を本地法身と加持身の二門に分かち、本地法身が遍一切処の加持力より生じて衆生のために身語意の三密を現じる受用身を「加持身」と名づける密教仏身論の中心概念・m679 が定義を literal kakikudashi 直接含有。「神変加持」案は経題釈の語義解説で定義性が m679 より弱く、「加持身説法」案は literal 直接含有 0 件のため退けた）
- **判断 3**：anchor 体制・規模 = 単独 anchor m679・5 motif（本軸の典籍は『大日経疏』巻第一の一系統のみで引証系統の対 anchor を欠くため、retrofit 22-23 の二重 anchor 系統対比型ではなく単独 anchor が自然形）

### Phase B：5 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m679 | 大日経疏 巻第一 §3-§5 序 | 書き下し anchor（単独・自己参照）・「次に如来というは、これ仏の加持身のその所住の処にして、仏の受用身と名づく……既に遍一切処の加持力より生ず。すなわち無相法身と無二無別なり」加持身を本地法身に対する受用身と定義する大日経疏の核心句 |
| m677 | 大日経疏 巻第一 §1 経題釈 | 強連動・「神変加持とは、旧訳には、あるいは神力所持といい、あるいは仏所護念という……自在神力加持三昧に住して、普く一切衆生のために、種々諸趣の所喜見の身を示す」経題『大毘盧遮那成仏神変加持』の「加持」を釈す句 |
| m689 | 大日経疏 巻第一 §20-§21 | 強連動・「身平等の密印、語平等の真言、心平等の妙観をもって方便とするが故に、加持受用身を逮見す。かくの如くの加持受用身は、すなわちこれ毘盧遮那の遍一切の身なり」加持受用身を遍一切身・行者の平等智身として釈す句 |
| m692 | 大日経疏 巻第一 §24 | 強連動・「かくの如く毘盧遮那は、普く十方一切の世界において、一々に皆仏の加持身を現ず……如来、もし加持を捨てるときは、すなわち現前せず」遍一切加持身と般舟三昧を説く句 |
| m695 | 大日経疏 巻第一 §27 清浄句義 | 強連動・「種々の因縁と無数の方便は……その実事を究めれば、秘密加持に非ざることなし。各々能く如来の清浄知見を開示す」清浄句義の本実を秘密加持とする句 |

体系内連節カバー：経題釈の神変加持（m677 §1）→ 加持身の定義（m679 §3-§5 序 anchor）→ 加持受用身＝遍一切身（m689 §20-§21）→ 遍一切加持身（m692 §24）→ 秘密加持＝清浄句義の本実（m695 §27）の大日経疏 巻第一 §1〜§27 を一括包摂。

**除外・温存**：dainichikyo-sho-vol1 corpus（68 件）のうち、加持身 theme を保有しつつ既存軸に連動済の m686（§15 二十執金剛③・retrofit 8 で sg08 阿字本不生）・m711（§50 五字門・retrofit 8 で sg08 阿字本不生）・m712（§51-52 三句法門・retrofit 15 で sg14 三草二木）は本軸から除外。clean の m680（§6-§7 加持注処・広大金剛法界宮）・m693（§25 真言道句の遍説）等は加持身軸と thematic に隣接するが、5 motif の正常規模を保つため本軸から除外して温存。三句法門 sg07・即身成仏 sg03・浄菩提心 sg21 連動済の motif 群も別系統のため温存。本軸 5 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 768 | 769 | +1（sg25 新規追加） |
| famous_phrases | 24 | 25 | +1 |
| ファイルサイズ | 2,682,561 bytes | 2,687,746 bytes | +5,185 |
| schema_history | 83 | 84 | +1（origin: retrofit_26:doctrine） |
| 連動タグ総数 | — | — | +10（sg25 軸 5 motif × 2） |
| kakikudashi_chars_total | 112,846 | 112,849 | +3（「加持身」3 字） |
| gendaigoyaku_chars_total | 324,146 | 325,271 | +1,125（sg25 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 769 vs 769 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg25 軸 5 motif × 2〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg25 連番・末尾 sg25 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 25 で recompute した stats は retrofit 26 着手時点で全 6 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 26 では stats を全件 recompute して真値を書き込み（total_motifs 769・famous_phrases 25・kakikudashi_chars_total 112,849・gendaigoyaku_chars_total 325,271・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。char 集計規則は「text フィールドから改行（\n）を除いた文字数の総和」であり、retrofit 26 着手時の drift check でこの規則が stored 値と完全一致することを確認したうえで recompute した（(d-6) 参照）。motifs.json は `json.dumps(ensure_ascii=False, indent=2)`・末尾改行なしの round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 Z 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 Z〔大日経疏 加持身 教学系軸連動の運用〕新規追加（282,270→301,708 bytes・+19,438・補注 A-Z 全 26 件 intact・補注 Z 内部の〔〕24/24・「」39/39・『』28/28・全角丸括弧 104/104 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 26 完走エントリを追加（340,560→346,139 bytes・retrofit 4-26 全エントリ intact・追加部分の〔〕12 対・「」4 対・『』2 対・全角丸括弧 1 対がいずれも balanced・新規半角括弧 0 件）。
- `commit_message.txt` を retrofit 26 用に書き換え（冒頭行整合確認済・13,714 bytes）。
- handoff_2026-05-23_retrofit26_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第九例・密教仏身論軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学、retrofit 21 即身成仏義 二頌八句軸は空海の即身成仏論、retrofit 22 浄菩提心軸は『大日経』『大日経疏』の菩提心論、retrofit 23 三種菩提心軸は龍猛菩薩造『菩提心論』の発菩提心論、retrofit 24 大心真言三摩地法門軸は空海撰『般若心経秘鍵』による『般若心経』の密教的読解、retrofit 25 吽字四字軸は空海撰『吽字義』による聖音「吽」一字の密教字義論を主題とする教学系軸であった。retrofit 26 加持身軸はその継続でありながら、『大日経疏』巻第一による大日如来の身の密教仏身論を主題とする点に特色をもつため、教学系軸の第九例と位置づける。浄菩提心 sg21 が同じ『大日経』『大日経疏』の菩提心論（行者の心の本来性）を軸とするのに対し、加持身 sg25 は同じ『大日経疏』巻第一のうちに大日如来の身（仏の側）の論を軸とし、『大日経疏』巻第一のうちに仏身論（sg25）と菩提心論（sg21）として並立する。

#### 2. 連動軸二十一系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）、加持身 sg25/m679（単独）〕の二十一系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）・即身成仏論（六大四曼三密）・本来性論（浄菩提心）・発菩提心論（三種菩提心）・密教的心経読解（大心真言三摩地法門）・聖音の字義論（吽字四字）に加えて、加持・受用身・四種法身（加持身）でも素材プールを切替可能。

#### 3. 単独 anchor 体制の運用第九例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599・retrofit 19 顕密二教 sg18/m571・retrofit 20 声字実相 sg19/m525・retrofit 21 六大無礙 sg20/m534・retrofit 24 大心真言三摩地法門 sg23/m496・retrofit 25 吽字四字 sg24/m564 に続く第九の単独 anchor 体制。本軸の典籍は『大日経疏』巻第一の一系統のみであり、引証系統の対 anchor を欠くため、典籍系統対比型の二重 anchor（retrofit 22 浄菩提心・retrofit 23 三種菩提心）を要さず単独 anchor が自然形となる。retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 に続いて単独 anchor 体制を継続する。

#### 4. anchor 直接含有による中心成句支持

retrofit 26 加持身 sg25 は、中心成句「加持身」を anchor m679 が「これ仏の加持身のその所住の処にして、仏の受用身と名づく」と literal kakikudashi で直接含有し、加持身を本地法身に対する受用身と規定する定義そのものが anchor に明示される。retrofit 20 声字実相・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 と同型の、中心成句が anchor に直接現れる教学系軸。

#### 5. handoff 暫定評価の Phase A 追加スキャンによる更新

retrofit 24-25 完走 handoff は大日経疏 巻第一 残 42 件を「中心成句不明瞭」と暫定評価していたが、これは如実知自心・三劫・六無畏 をスキャンした結果であった。retrofit 26 Phase A で「加持身」を中心成句として候補語を変えてスキャンした結果、未連動 42 件中 26 件が 主題:加持身 を保有し経題釈から清浄句義まで一貫した加持身論の教学線が確認され、正常規模（5 motif）の連動軸を成立させられることが判明した。候補スキャンは中心成句の候補語を網羅的に変えてスキャンすべきという retrofit 20・retrofit 21 完走 handoff の候補スキャン方針の実例となった。handoff の暫定評価は将来 retrofit の着手判断の出発点であって最終判定ではなく、Phase A では候補語を変えて再スキャンすることが重要である。

#### 6. thematic adjacency と連動タグ overlap の区別の再運用・大日経疏 corpus の既存軸 overlap への対応

dainichikyo-sho-vol1 corpus には三句法門 sg07・即身成仏 sg03・阿字本不生 sg08・三草二木 sg14・浄菩提心 sg21 等の既存軸 anchor・強連動 motif が居住し、加持身 theme を保有する m686/m711 が sg08 阿字本不生、m712 が sg14 三草二木 に連動済である。本軸は加持身を本地法身に対する受用身と定義する m679 を anchor とし、既に他軸に連動済の motif は本軸から除外して、神変加持（m677）・加持受用身（m689）・遍一切加持身（m692）・秘密加持（m695）の clean motif で軸を構成した。これにより加持身軸と既存軸の連動タグ overlap はゼロに保たれ、加持身 sg25 は大日如来の身の論を、浄菩提心 sg21 は行者の菩提心の論を、それぞれ別系統の連動軸として並立させる。retrofit 21 補注 U・retrofit 22 補注 V・retrofit 23 補注 W・retrofit 24 補注 X・retrofit 25 補注 Y の方針を踏襲。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=769  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg25軸 5motif×2 全付与  OK
7. sg list sg01-sg25 continuous, tail=sg25  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK
   anchor 自己参照タグ 連動軸二十一系統: ALL OK

[stats（retrofit 26 後）]
total_motifs=769  famous_phrases=25
kakikudashi_chars_total=112,849
gendaigoyaku_chars_total=325,271
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=84 entries
file size=2,687,746 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 27〔教学系軸の継続〕

- **般若心経秘鍵 仏法不外求軸**：般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす。ただし「仏法不外求」thesis 句の literal kakikudashi 直接含有は m492 専属で強連動 motif 群が m493 1 件にとどまり anchor＋強連動 2 motif の過去最小規模となるため、軸規模の再検討を要する（retrofit 26 Phase A の実測で他 corpus からの clean な引証 motif も得られないことを確認済・(d-2) 参照）。
- **三教指帰軸**：sankyo-shiki corpus 21 件は全件 clean だが、「三教」literal 3 件（m656/m675/m676）はいずれも枠組み motif で、連動軸モデル（成句＋書き下し anchor＋強連動）への適合が弱い。retrofit 4 で発言者軸（亀毛先生／虚亡隠士／仮名乞児）を運用済（(d-3) 参照）。
- **大日経疏 巻第一 残 37 件のさらなる主題軸化**：retrofit 26 後、dainichikyo-sho-vol1 68 件のうち未連動は 37 件。加持身軸（retrofit 26）・浄菩提心軸（retrofit 22）・三句法門軸（retrofit 6）等で主要テーマは軸化済。残 37 件に正常規模の中心成句が立つかは Phase A の候補語スキャン次第（(d-4) 参照）。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸二十一系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg25 加持身（大日経疏）は加持・受用身・四種法身（自性・受用・変化・等流）・加持身説法 を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔二十系統 書き下し anchor 全件 OK・retrofit 26 後 二十一系統 完全整合〕

retrofit 21 §(d-1)・retrofit 25 §(d-1) の指示に従い、retrofit 26 着手時に連動軸二十系統（sg02/sg03/sg07-sg24）の書き下し anchor 自己参照タグ全件検証を実施した結果、全 anchor（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728/m506/m581/m496/m564・m636 は sg10/sg14 共有）がすべて「連動:sgNN」「連動:m(anchor)」を保有していることを確認した（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg24）は二十系統一律に連動タグ未保有であるが、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりであり、defect ではなく二十系統一律の設計仕様。retrofit 26 で追加した sg25 単独 anchor m679 も「連動:sg25」「連動:m679」を保有し、検証スクリプトで連動軸二十一系統 anchor の自己参照タグが ALL OK（完全整合）であることを確認した。今後 anchor を扱う retrofit でも着手時の書き下し anchor 自己参照タグ全件検証を継続する。

### (d-2) 般若心経秘鍵 仏法不外求軸の規模問題と温存

般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る。明暗他に非ざれば、信修すれば忽ちに証す」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす（m492 は既存「主題:仏法不外求」タグ保持）。retrofit 24-25 完走 handoff が retrofit 26 以降の独立軸候補として温存したものだが、retrofit 26 Phase A スキャンの実測で、「仏法不外求」の thesis 句「仏法遥かに非ず／真如外に非ず／心中にして即ち近し」の literal kakikudashi 直接含有は m492 専属、強連動候補も m493 1 件にとどまり anchor m492 ＋ 強連動 m493 ＝ 2 motif と過去最小（retrofit 20 声字実相・retrofit 25 吽字四字 各 4 motif）を下回る規模となることを再確認した。さらに本来性 thesis の literal を他 corpus に拡張してもクリーンな引証 motif は得られず（本来性 theme は 88 件の clean motif に拡散する thematic adjacency にとどまる）、強連動 motif 群の構造的拡大が困難であることが判明した。連動軸として構造的に薄いため、retrofit 26 ではケンシン裁定で大日経疏 加持身軸を採用し、仏法不外求軸は retrofit 27 以降に温存した。将来 retrofit で仏法不外求軸を採る場合、anchor＋強連動 2 motif の最小規模を許容するか否かの判断を要する。

### (d-3) 三教指帰軸の温存

sankyo-shiki corpus 21 件は全件 clean だが、「三教」literal 3 件（m656/m675/m676）はいずれも儒道仏の枠組みを述べる枠組み motif であり、連動軸モデル（中心成句＋書き下し anchor＋強連動）への適合が弱い。三教指帰は retrofit 4 で発言者軸（亀毛先生／虚亡隠士／仮名乞児）を運用済であり、連動軸としての軸化は retrofit 27 以降に温存。

### (d-4) 大日経疏 巻第一 corpus のカバー範囲

retrofit 26 後、dainichikyo-sho-vol1 corpus（68 件）は 31 件が連動タグ保有（sg25 加持身 5 件 m677/m679/m689/m692/m695・sg07 三句法門 6 件・sg08 阿字本不生 4 件・sg21 浄菩提心 6 件・sg03 即身成仏 4 件・sg15 長者窮子 3 件・sg14 三草二木 2 件・sg12 化城宝処 1 件・sg13 多宝塔 1 件・sg16 従地涌出 1 件）・37 件が未連動である。未連動 37 件は加持注処（m680）・真言道句の遍説（m693）・二十執金剛の列挙・執金剛秘密主の三問 等を含むが、中心成句が明瞭な軸候補が残るかは retrofit 27 以降の Phase A 候補語スキャン次第。

### (d-5) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg25 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-26 で sg08-sg25 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-26 一貫して未更新の pre-existing 事象。retrofit 26 でも踏襲し未変更とした。将来 "sg01-sg25" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-6) 編集手法・truncate 事象の再発と回避

retrofit 26 では、補注 Z 追加スクリプト（`outputs/add_chunote_z_retrofit26.py`）を当初 Write tool で作成（20,960 bytes・作成時は完全）したのち、Edit tool で 1 箇所を修正したところ、**Edit tool がファイルを末尾切り捨て（truncate）した**事象が発生した（retrofit 25 §(d-6) が記録した commit_message.txt の Write tool truncate 事象に続く第二例で、今回は Edit tool・約 21KB のファイルで発生）。これを受けて、補注 Z 本文を独立した markdown ファイル（`outputs/chunote_z_retrofit26.md`）に bash heredoc で書き出し、それを読み込んで挿入する小規模スクリプトに作り直して回避した。本 retrofit のスクリプト・長文ファイル（motifs.json 反映・補注 Z 追加・CLAUDE.md 更新・commit_message.txt・本 handoff）はいずれも **bash heredoc または Python write_bytes 方式**で作成・更新し、Edit/Write tool は短いスクリプトの patch 用途に限定した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（motifs.json は dry-run + 検証 + 本番適用の二段運用）。motifs.json は json round-trip 完全一致（`json.dumps(ensure_ascii=False, indent=2)`・末尾改行なし）を事前確認のうえ編集。全ファイル NUL 0 件確認済。**今後もスクリプト・長文ファイルの作成・更新は bash heredoc / Python write_bytes を第一選択とし、Edit/Write tool での長文ファイル操作は避けることを強く推奨する**。なお stats の char 集計規則は「text フィールド値から改行（\n）を除いた文字数の総和」であり、retrofit 26 着手時の drift check で素朴な `len()` が stored 値と +638/+577/+3,250 ずれること、`\n` を除けば完全一致することを実測で確認した。recompute スクリプトはこの `\n` 除去規則を用いている。

### (d-7) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト（retrofit26_phaseA_scan.py・retrofit26_kajishin.py・retrofit26_verify.py・add_chunote_z_retrofit26.py・update_claude_md_retrofit26.py・chunote_z_retrofit26.md・_dryrun_motifs_r26.json）・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。retrofit 26 着手時に `git status --short` を確認した結果、`.git/index.lock` 残留はなく、staged 変更（削除ステージ等）も検出されず、git index は健全であった。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-25 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。bash サンドボックスのマウント層に見える `.git/index.lock` 等は実 Windows の `.git` には存在しない一時アーティファクトであり commit_push.bat には影響しない（retrofit 25 で確認済）。

### (d-8) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 26 後で 全角〔/〕1137/1137・「」672/672・『』90/90 balanced、全角丸括弧（）は 1193/1194（pre-existing で閉じ括弧が 1 件超過・backup pre_retrofit26 で 1191/1192 と確認）、半角括弧は 284/287（pre-existing 差分・backup と同一）。retrofit 26 の追加部分（タイトル行・最終更新行の retrofit 26 エントリ）は〔〕12 対・「」4 対・『』2 対・全角丸括弧 1 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである。全角丸括弧・半角括弧の pre-existing 差分は retrofit 26 で新たに発生したものではなく、追加部分が balanced であれば許容する運用〔retrofit 17 §(d-5)・retrofit 19〜25 §(d-7)/§(d-8) で記録された CLAUDE.md pre-existing 括弧差分の継続〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔769 件・m1-m744 + sg01-sg25・2,687,746 bytes・schema_history 84 件〕
- 本 retrofit build script：`outputs/retrofit26_kajishin.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit26_phaseA_scan.py`
- 整合性検証 script：`outputs/retrofit26_verify.py`
- 補注 Z 本文：`outputs/chunote_z_retrofit26.md`／補注 Z 挿入 script：`outputs/add_chunote_z_retrofit26.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit26.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit26.json`〔retrofit 前 motifs.json・2,682,561 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit26.md`〔retrofit 前・282,270 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit26.md`〔retrofit 前・340,560 bytes〕
  - `outputs/commit_message_backup_pre_retrofit26.txt`〔retrofit 前 commit_message.txt〕
  - `outputs/_dryrun_motifs_r26.json`〔retrofit 26 dry-run・検証用〕
- 前 retrofit handoff：`handoff_2026-05-23_retrofit25_complete.md`〔吽字義 吽字四字 教学系軸連動〕
- 補注 Z 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 26 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-25 完走 → 2026-05-23 retrofit 26 完走〔大日経疏 加持身 教学系軸連動・新規 sg25「加持身」+ 単独 anchor m679 採用（大日経疏 巻第一 §3-§5 序）・強連動 4 件（m677/m689/m692/m695）・連動軸二十一系統並立に到達・教学系軸の第九例・単独 anchor 体制 第九例〕。本体 motifs.json は 769 件・2,687,746 bytes・schema_history 84 件。motifs_index_design.md §2 に補注 Z 追加〔補注 A-Z 全 26 件 intact・301,708 bytes〕。CLAUDE.md は 346,139 bytes〔retrofit 4-26 全エントリ intact〕。連動軸二十一系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）、加持身 sg25/m679（単独）〕の書き下し anchor 自己参照タグ運用が完全整合。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-23_retrofit26_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-23_retrofit25_complete.md`〔retrofit 25 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-Z 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・769 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 26 commit です。

【本セッションの選択肢】
(A) retrofit 27 候補〔教学系軸：般若心経秘鍵 仏法不外求軸（m492/m493 clean・anchor＋強連動 2 motif の最小規模・規模再検討要）／三教指帰軸／大日経疏 巻第一 残 37 件のさらなる主題軸化〕
(B) kaimyo-app 教学系素材活用：連動軸二十一系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- bash サンドボックスのマウント層に見える .git/index.lock 等は実 Windows の .git には存在しない一時アーティファクト・commit_push.bat には影響しない〔retrofit 25-26 で確認済〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Write tool が commit_message.txt を、Edit tool が約 21KB スクリプトを truncate した事象が retrofit 25-26 で発生・heredoc で回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用〔char 集計規則は text フィールドから改行を除いた文字数の総和〕
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは中心成句の候補語を網羅的に変えてスキャンする〔retrofit 26 §(d-5)・handoff の暫定評価は出発点であって最終判定ではない〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)・retrofit 22-26 で再運用〕
- anchor を扱う retrofit では着手時に書き下し anchor 自己参照タグ全件検証を行う〔retrofit 26 で連動軸二十一系統 全件 OK 確認〕
- sg 成句 motif 自身は連動タグ未保有（成句は連動の参照先であり連動 motif プールの成員ではない・二十一系統一律の設計仕様）
- 単独 anchor 体制（補注 J/N/P/R/S/T/U/X/Y/Z 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q/V/W 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-23〔retrofit 26 完走・大日経疏 加持身 教学系軸連動 retrofit。新規 sg-id `sg25`「加持身」を新設〔出典:大日経疏〕、書き下し anchor として単独 anchor m679 を採用（m679 大日経疏 巻第一 §3-§5 序「次に如来というは、これ仏の加持身のその所住の処にして、仏の受用身と名づく……既に遍一切処の加持力より生ず。すなわち無相法身と無二無別なり」加持身を本地法身に対する受用身と定義する大日経疏の核心句）。強連動 4 motif：m677（§1 経題釈 神変加持）/ m689（§20-§21 加持受用身）/ m692（§24 遍一切加持身）/ m695（§27 秘密加持）に「連動:sg25」「連動:m679」を付与（+10 タグ）。total_motifs 768→769（+1 新規 sg25）・famous_phrases 24→25。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,687,746 bytes〔+5,185〕・schema_history 84 件〔+1・origin: retrofit_26:doctrine〕・補注 Z 追加〔motifs_index_design.md §2・282,270→301,708 bytes・+19,438〕・CLAUDE.md 更新完了〔340,560→346,139 bytes〕・commit_message.txt 書き換え済。連動軸二十一系統並立に到達。教学系軸（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字）に続く教学系軸の第九例で、『大日経疏』巻第一による大日如来の身の密教仏身論を主題とする軸。単独 anchor 体制の運用第九例（retrofit 14/16/18/19/20/21/24/25 に続く）。中心成句「加持身」の定義を anchor m679 が literal で直接含有する。retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 に続いて単独 anchor 体制を継続。anchor 1 ＋ 強連動 4 ＝ 5 motif の小規模 retrofit。handoff が「中心成句不明瞭」と暫定評価していた大日経疏 巻第一 残 42 件を、Phase A で「加持身」を候補語として再スキャンすることで正常規模の軸として成立させた。Phase D 必須チェックリストに完全準拠する第十八の retrofit〕

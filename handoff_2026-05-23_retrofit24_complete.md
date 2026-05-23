# 引き継ぎメモ：retrofit 24 完走〔般若心経秘鍵 大心真言三摩地法門 教学系軸連動 retrofit〕

**日付**：2026-05-23
**フェーズ**：retrofit 24（retrofit 23 完走に続く第二十一の retrofit セッション）
**対象**：空海撰『般若心経秘鍵』に説かれる『般若心経』の密教的読解の中心概念「大心真言三摩地法門」の連動軸新設。新規 sg-id `sg23`「大心真言三摩地法門」を追加し、書き下し anchor として **単独 anchor m496** を採用。m496（般若心経秘鍵 第四節 題号釈・「大般若波羅蜜多心経といっぱ、即ち是れ大般若菩薩の大心真言三摩地法門なり。文は一紙に欠けて、行は則ち十四なり」心経の題号を大心真言三摩地法門と規定する核心句）を単独の書き下し anchor とする。強連動 4 motif（m491 第一節 帰敬讃 / m498 第八節 大心咒の釈 / m501 第九節 真言不思議の頌 / m504 第十一節 結頌）に連動タグを付与。連動軸十九系統並立に到達。本 retrofit は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心 に続く **教学系軸の第七例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句 同型の **単独 anchor 体制の運用第七例**。anchor 1 ＋ 強連動 4 ＝ 5 motif の小規模 retrofit。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 5 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 X 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 25 候補〔教学系軸：吽字義軸（中心成句要再検討）／三教指帰軸／般若心経秘鍵 仏法不外求軸（m492/m493 clean）／大日経疏 巻第一 残 42 件の他主題軸化〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_24:doctrine〕
- [x] motifs_index_design.md に補注 X 追加済〔補注 A-X 全 24 件 intact・247,628→264,587 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・330,354→335,377 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 24 用・冒頭行整合確認済〕
- [x] handoff_2026-05-23_retrofit24_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 23 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 23 完走〔菩提心論 三種菩提心 教学系軸連動・commit `20abe36`〕に続く第二十一の retrofit セッション。

retrofit 23 完走 handoff §(c) 選択肢 A〔retrofit 24 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で般若心経秘鍵 大心真言三摩地法門軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg23`「大心真言三摩地法門」を追加〔出典:般若心経秘鍵・空海撰『般若心経秘鍵』の題号釈において『般若心経』の本質を規定する密教的心経読解の中心概念〕
- 書き下し anchor は **単独 anchor m496**（般若心経秘鍵 第四節 題号釈）
- 強連動 4 motif（m491 第一節 帰敬讃 / m498 第八節 大心咒の釈 / m501 第九節 真言不思議の頌 / m504 第十一節 結頌）に「連動:sg23」「連動:m496」を付与（+10 タグ）
- 連動軸十九系統並立に到達
- **教学系軸の第七例**（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心 に続く・大心真言三摩地法門は顕教経典『般若心経』の密教的読解を主題とする）
- **単独 anchor 体制の運用第七例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句 に続く）
- **5 motif retrofit**（anchor 1 ＋ 強連動 4・retrofit 21 即身成仏義・retrofit 23 三種菩提心 と同規模の小規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 23 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸十八系統（sg02/sg03/sg07-sg22）の書き下し anchor 26 motif（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728/m506/m581）がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg22）は十八系統一律に連動タグ未保有であり、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりで整合。Phase A スキャンで retrofit 24 候補（般若心経秘鍵軸／吽字義軸／三教指帰軸／大日経疏 巻第一 残 42 件他主題軸）の中心成句の kakikudashi 直接含有を全 766 motif にわたり網羅検査：

| 候補 | corpus clean 率 | kakikudashi 支持 | 判定 |
|---|---|---|---|
| 般若心経秘鍵軸 | hannya-hiken 12/15 clean | 「大心真言三摩地法門」literal を m496 が直接含有・真言/陀羅尼系 clean 4 件（m491/m498/m501/m504）が強連動候補で主題一貫 | 採用 |
| 吽字義軸 | ujiji 13/18 clean | 字相/字義は 3 corpus 拡散・阿訶汙麼 m564 のみ・sg08 阿字本不生 anchor m549 が corpus 内居住で overlap 整理を要す | 基準未達・retrofit 25 以降に温存 |
| 三教指帰軸 | sankyo-shiki 21/21 完全 clean | 「三教」literal 3 件すべて枠組み motif・連動軸モデルへの適合が弱い（retrofit 4 発言者軸運用済） | 基準未達・retrofit 25 以降に温存 |
| 大日経疏 残 42 件他主題軸 | — | 如実知自心 2 件すべて既存軸 overlap・三劫/六無畏 corpus 内 0 件で中心成句不明瞭 | 基準未達・retrofit 25 以降に温存 |

retrofit 24 Phase A スキャンの実測で、般若心経秘鍵 corpus（hannya-hiken・m491-m505 の 15 件）は 12 件が連動タグ未保有の clean（m494 は sg11 良医病子・m499/m500 は sg02 色即是空 連動済）であり、『心経』を真言・陀羅尼の法門として読む密教的読解が clean motif 群に一貫することを確認。中心成句「大心真言三摩地法門」の literal kakikudashi 直接含有は m496（般若心経秘鍵 第四節 題号釈）1 件であり、これを単独の書き下し anchor とする構成が可能であることを確認。ケンシン裁定で判断 1-3：

- **判断 1**：軸採用 = 般若心経秘鍵軸（hannya-hiken corpus 15 件中 12 件 clean・『心経』を真言・陀羅尼の法門として読む密教的読解が clean motif 群に一貫）
- **判断 2**：中心成句 sg23 =「大心真言三摩地法門」（般若心経秘鍵 題号釈において『般若心経』の本質を規定する中心概念・m496 が literal kakikudashi 直接含有・retrofit 23「三種菩提心」が literal 0 件であったのに対し本 retrofit は anchor 直接含有 1 件で成句支持がより強い）
- **判断 3**：anchor 体制・規模 = 単独 anchor m496・5 motif（成句「大心真言三摩地法門」の literal kakikudashi 直接含有は m496 単独であり引証系統の対 anchor を欠くため、retrofit 22-23 の二重 anchor 系統対比型ではなく単独 anchor が自然形）

### Phase B：5 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m496 | 般若心経秘鍵 第四節 題号釈 | 書き下し anchor（単独・自己参照）・「大般若波羅蜜多心経といっぱ、即ち是れ大般若菩薩の大心真言三摩地法門なり。文は一紙に欠けて、行は則ち十四なり」心経の題号を大心真言三摩地法門と規定する核心句 |
| m491 | 般若心経秘鍵 第一節 | 強連動・「文殊の利剣は諸戯を絶つ……諸教を含蔵せる陀羅尼なり」般若菩薩・覚母を真言・陀羅尼・種子として讃ずる帰敬の偈 |
| m498 | 般若心経秘鍵 第八節 | 強連動・「般若心と言っぱ、此の菩薩に身心等の陀羅尼有り。是の経の真言は、即ち大心咒なり。此の心真言に依って、般若心の名を得」心経の真言を大心咒と定める釈 |
| m501 | 般若心経秘鍵 第九節 | 強連動・「真言は不思議なり、観誦すれば無明を除く、一字に千理を含み、即身に法如を証す」真言観誦の不思議の功徳を頌する句 |
| m504 | 般若心経秘鍵 第十一節 | 強連動・「我れ秘密真言の義に依って、略して心経五分の文を讃す、一字一文法界に遍じ、無終無始にして我が心分なり」秘鍵全篇が秘密真言の義によって心経を讃したものであると結ぶ句 |

体系内連節カバー：帰敬讃（m491 第一節）→ 題号釈の核心句（m496 第四節 anchor）→ 大心咒の釈（m498 第八節）→ 真言不思議の頌（m501 第九節）→ 秘密真言の義による結頌（m504 第十一節）の般若心経秘鍵 第一〜第十一節を一括包摂。

**除外・温存**：般若心経秘鍵 corpus（hannya-hiken 15 件）のうち本軸に含めなかった 10 件のうち、m494（衆生迷情・長眠の子）は retrofit 12 で良医病子 sg11、m499・m500（色空本不二）は retrofit 7 で色即是空 sg02 に連動済。clean の m492・m493（「仏法遥かに非ず、心中にして即ち近し」仏法不外求）は本来性・即身内証を主題とする別の中心成句候補であり、retrofit 25 以降の独立軸候補として温存（(d-2) 参照）。m495（機根教判）・m497（密教深広・法界縁起）・m502（医王の目・洞察）・m503（顕密は人に在り）・m505（弘仁九年 大疫 結語）は大心真言三摩地法門とは別主題であり「主題:般若智慧」等のタグ保持により別途検索可能なため温存。本軸 5 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 766 | 767 | +1（sg23 新規追加） |
| famous_phrases | 22 | 23 | +1 |
| ファイルサイズ | 2,670,386 bytes | 2,676,192 bytes | +5,806 |
| schema_history | 81 | 82 | +1（origin: retrofit_24:doctrine） |
| 連動タグ総数 | — | — | +10（sg23 軸 5 motif × 2） |
| kakikudashi_chars_total | 112,833 | 112,842 | +9（「大心真言三摩地法門」9 字） |
| gendaigoyaku_chars_total | 321,021 | 322,464 | +1,443（sg23 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 767 vs 767 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg23 軸 5 motif × 2〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg23 連番・末尾 sg23 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 23 で recompute した stats は retrofit 24 着手時点で全 6 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 24 では stats を全件 recompute して真値を書き込み（total_motifs 767・famous_phrases 23・kakikudashi_chars_total 112,842・gendaigoyaku_chars_total 322,464・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 X 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 X〔般若心経秘鍵 大心真言三摩地法門 教学系軸連動の運用〕新規追加（247,628→264,587 bytes・+16,959・補注 A-X 全 24 件 intact・全角丸括弧 1574/1574 balanced・〔〕262/262 balanced・かぎ括弧 829/829 balanced・二重かぎ 61/61 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 24 完走エントリを追加（330,354→335,377 bytes・retrofit 4-24 全エントリ intact・追加部分の〔〕12/12・かぎ括弧 4/4・二重かぎ 3/3・全角丸括弧 1/1 balanced・新規半角括弧 0 件・全角〔〕全体 1089/1089 balanced）。
- `commit_message.txt` を retrofit 24 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-23_retrofit24_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第七例・顕教経典の密教的読解軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学、retrofit 21 即身成仏義 二頌八句軸は空海の即身成仏論、retrofit 22 浄菩提心軸は『大日経』『大日経疏』の菩提心論、retrofit 23 三種菩提心軸は龍猛菩薩造『菩提心論』の発菩提心論を主題とする教学系軸であった。retrofit 24 大心真言三摩地法門軸はその継続でありながら、空海撰『般若心経秘鍵』による『般若心経』の密教的読解を主題とする点に特色をもつため、教学系軸の第七例と位置づける。retrofit 20-23 が空海三部書・密教論書の本体（声字実相義・即身成仏義・大日経疏・菩提心論）を軸化したのに対し、本 retrofit は顕教の経典『般若心経』を密教的に読みかえる空海の註釈そのものを軸化する点に特色がある。

#### 2. 連動軸十九系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）〕の十九系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）・即身成仏論（六大四曼三密）・本来性論（浄菩提心）・発菩提心論（三種菩提心）に加えて、般若心経・真言・陀羅尼（大心真言三摩地法門）でも素材プールを切替可能。

#### 3. 単独 anchor 体制の運用第七例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599・retrofit 19 顕密二教 sg18/m571・retrofit 20 声字実相 sg19/m525・retrofit 21 六大無礙 sg20/m534 に続く第七の単独 anchor 体制。成句「大心真言三摩地法門」の literal kakikudashi 直接含有は般若心経秘鍵 第四節 題号釈 m496 単独であり、引証系統の対 anchor を欠くため、典籍系統対比型の二重 anchor（retrofit 22 浄菩提心・retrofit 23 三種菩提心）を要さず単独 anchor が自然形となる。retrofit 22-23 の二重 anchor 系統対比型に続いて、本 retrofit で単独 anchor 体制に戻る。

#### 4. anchor 直接含有による中心成句支持

retrofit 23 三種菩提心 sg22 は中心成句「三種菩提心」の literal kakikudashi 直接含有が 0 件で、書き下し「勝義・行願・三摩地を戒となす」を二重 anchor が担う構成であった。これに対し retrofit 24 大心真言三摩地法門 sg23 は、中心成句「大心真言三摩地法門」を anchor m496 が literal で直接含有しており、成句 anchor と書き下し anchor が同一語を共有する自己参照の最も明瞭な形をなす。retrofit 20 声字実相（語「声字実相」を m521 が含有・中心頌冒頭句「五大皆有響」を m525 が含有）と同型の、中心成句が anchor に直接現れる教学系軸。

#### 5. thematic adjacency と連動タグ overlap の区別の再運用

本軸 5 motif（m491/m496/m498/m501/m504）は「主題:即身成仏」「密教:般若菩薩」等を即身成仏 sg03・色即是空 sg02 と共有して主題的に隣接するが、いずれも着手前は連動タグ未保有の clean であり、既存軸との連動タグ overlap はゼロである。retrofit 21 補注 U・retrofit 22 補注 V・retrofit 23 補注 W で確立した「thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する」方針を踏襲し、clean motif を採って軸を構成、既に sg11/sg02 に連動済の m494/m499/m500 は本軸に含めなかった。

#### 6. 5 motif 規模・小規模 retrofit

anchor 1 ＋ 強連動 4 ＝ 5 motif は retrofit 21 即身成仏義 二頌八句（5 motif）・retrofit 23 三種菩提心（5 motif）と同等の小規模 retrofit。般若心経秘鍵 corpus 15 件のうち『心経』を真言・陀羅尼の法門として読む骨格 5 件に絞り、仏法不外求（m492/m493）・機根教判（m495）・密教深広（m497）等の別主題 motif を温存することで自然に小規模化した。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=767  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg23軸 5motif×2 全付与  OK
7. sg list sg01-sg23 continuous, tail=sg23  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK
   anchor 自己参照タグ 連動軸十九系統: ALL OK

[stats（retrofit 24 後）]
total_motifs=767  famous_phrases=23
kakikudashi_chars_total=112,842
gendaigoyaku_chars_total=322,464
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=82 entries
file size=2,676,192 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 25〔教学系軸の継続〕

- **吽字義軸**：ujiji corpus 18 件中 13 件 clean。中心成句が不明瞭（「字相/字義」は ujiji・nikyo-ron・hizo-houyaku の 3 corpus に拡散・「阿訶汙麼（吽字四字）」は m564 のみ）。sg08 阿字本不生 anchor m549 が ujiji corpus 内に居住するため重複の整理が要。吽字 四字（阿・訶・汙・麼＝法身・報身・応身・化身）の構造を成句として再検討する余地がある。
- **般若心経秘鍵 仏法不外求軸**：般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補をなす。retrofit 24 は大心真言三摩地法門軸に絞ったため、仏法不外求軸は独立軸候補として温存した。ただし「仏法不外求」literal kakikudashi 直接含有は m492 1 件のみで、強連動 motif 群の構成に再検討を要する。
- **三教指帰軸**：sankyo-shiki corpus 21 件は全件 clean だが、「三教」literal 3 件（m656/m675/m676）はいずれも枠組み motif で、連動軸モデル（成句＋書き下し anchor＋強連動）への適合が弱い。retrofit 4 で発言者軸（亀毛先生／虚亡隠士／仮名乞児）を運用済。
- **大日経疏 巻第一 残 42 件他主題軸**：dainichikyo-sho-vol1 68 件中 42 件が未連動。如実知自心は 2 件すべて既存軸 overlap・外道破斥 等は中心成句不明瞭で、retrofit 22-23 同様に基準未達と判定済。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸十九系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg23 大心真言三摩地法門（般若心経秘鍵）は般若心経・真言・陀羅尼を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔十八系統 書き下し anchor 全件 OK・retrofit 24 後 十九系統 完全整合〕

retrofit 21 §(d-1)・retrofit 23 §(d-1) の指示に従い、retrofit 24 着手時に連動軸十八系統（sg02/sg03/sg07-sg22）の書き下し anchor 自己参照タグ全件検証を実施した結果、全 26 motif（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728/m506/m581）がすべて「連動:sgNN」「連動:m(anchor)」を保有していることを確認した（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg22）は十八系統一律に連動タグ未保有であるが、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりであり、defect ではなく十八系統一律の設計仕様。retrofit 24 で追加した sg23 単独 anchor m496 も「連動:sg23」「連動:m496」を保有し、検証スクリプトで連動軸十九系統 anchor の自己参照タグが ALL OK（完全整合）であることを確認した。今後 anchor を扱う retrofit でも着手時の書き下し anchor 自己参照タグ全件検証を継続する。

### (d-2) 般若心経秘鍵 仏法不外求軸の温存

般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る。明暗他に非ざれば、信修すれば忽ちに証す」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす（m492 は既存「主題:仏法不外求」タグ保持）。retrofit 24 は大心真言三摩地法門軸（『心経』を真言・陀羅尼の法門として読む密教的読解の核心 thesis）に絞り、仏法不外求軸（『心経』の説く悟りが行者の心中にあって即身に証されるとする本来性論）は別系統のため retrofit 25 以降の独立軸候補として温存した。ただし「仏法不外求」の書き下し「仏法遥かに非ず／真如外に非ず」の kakikudashi 直接含有は m492 1 件のみであり、強連動 motif 群（m493 等）の構成に再検討を要する。

### (d-3) 般若心経秘鍵 corpus のカバー範囲

retrofit 24 後、般若心経秘鍵 corpus（hannya-hiken 15 件）は 8 件が連動タグ保有（sg23 軸 5 件 m491/m496/m498/m501/m504・sg11 良医病子 m494・sg02 色即是空 m499/m500）・7 件が未連動（m492/m493/m495/m497/m502/m503/m505）である。未連動 7 件のうち m492/m493 は仏法不外求軸候補（(d-2)）、残 5 件は機根教判・密教深広・洞察・顕密・鎮疫結語の別主題であり、中心成句が明瞭でないため将来 retrofit での軸化余地は限定的。

### (d-4) 吽字義 corpus の sg08 overlap

吽字義 corpus（ujiji 18 件）は retrofit 24 後も 13 件 clean だが、sg08 阿字本不生 anchor m549 が ujiji corpus 内（第一節）に居住し、m551/m552/m553 も sg08 連動済・m565 が sg07 連動済である。将来 吽字義軸を新設する場合、sg08 阿字本不生 との重複（阿字の義は吽字四字 阿・訶・汙・麼 の一であり、吽字義 corpus 内に阿字本不生 anchor が同居する構造）の整理を要する。retrofit 23 §(c)・retrofit 22 §(c) に続く指摘。

### (d-5) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg23 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-24 で sg08-sg23 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-24 一貫して未更新の pre-existing 事象。retrofit 24 でも踏襲し未変更とした。将来 "sg01-sg23" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-6) 編集手法・truncate 事象回避

retrofit 24 のビルドスクリプト（`outputs/retrofit24_daishin_shingon.py`）・Phase A スキャンスクリプト（`outputs/retrofit24_phaseA_scan.py`）・検証スクリプト（`outputs/retrofit24_verify.py`）・補注 X 追加スクリプト（`outputs/add_chunote_x_retrofit24.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit24.py`）・commit_message.txt・本 handoff はすべて bash heredoc 方式で作成し、Edit/Write tool の truncate 事象を回避した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（dry-run + 本番適用の二段運用）。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。今後もスクリプト・長文ファイルの作成は bash heredoc / Python write_bytes を第一選択とすることを推奨。

### (d-7) git 状態・commit_push.bat について・予告された index 異常は非検出

retrofit 23 完走 handoff および新セッション貼付メッセージで「前セッション push 後に git index 異常（cache entry null sha1・tsconfig.json/vercel.json/引き継ぎメモ…の削除ステージ）が残存」と予告されていたが、retrofit 24 着手時に `git status --short`・`git diff --cached --name-status` を実行して確認した結果、**削除ステージ・staged 変更は一切検出されず（diff --cached 空）、`.git/index.lock` 残留もなく、git index は健全**であった。`git fsck` では dangling commit/tree が複数検出されたが、これは孤立オブジェクトであり無害。したがって retrofit 24 では fix_index.bat 等による index 整理は不要であった。本コミットは新規ファイル追加〔outputs 配下スクリプト・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-23 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。git status 等の実行後は `.git/index.lock` 残留に留意し、残留した場合は commit_push.bat 実行前に除去する（retrofit 22 §(d-4)）。

### (d-8) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 24 後で 全角〔/〕1089/1089 balanced。retrofit 24 の追加部分（タイトル行・最終更新行の retrofit 24 エントリ）は〔〕12 対・かぎ括弧 4 対・二重かぎ 3 対・全角丸括弧 1 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5)・retrofit 19 §(d-7)・retrofit 20 §(d-7)・retrofit 21 §(d-7)・retrofit 22 §(d-8)・retrofit 23 §(d-8) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔767 件・m1-m744 + sg01-sg23・2,676,192 bytes・schema_history 82 件〕
- 本 retrofit build script：`outputs/retrofit24_daishin_shingon.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit24_phaseA_scan.py`
- Phase A 結果まとめ：`outputs/retrofit24_phaseA_out.txt`
- 整合性検証 script：`outputs/retrofit24_verify.py`
- 補注 X 追加 script：`outputs/add_chunote_x_retrofit24.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit24.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit24.json`〔retrofit 前 motifs.json・2,670,386 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit24.md`〔retrofit 前・247,628 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit24.md`〔retrofit 前・330,354 bytes〕
  - `outputs/commit_message_backup_pre_retrofit24.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-22_retrofit23_complete.md`〔菩提心論 三種菩提心 教学系軸連動〕
- 補注 X 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 24 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-23 完走 → 2026-05-23 retrofit 24 完走〔般若心経秘鍵 大心真言三摩地法門 教学系軸連動・新規 sg23「大心真言三摩地法門」+ 単独 anchor m496 採用（般若心経秘鍵 第四節 題号釈）・強連動 4 件（m491/m498/m501/m504）・連動軸十九系統並立に到達・教学系軸の第七例・単独 anchor 体制 第七例〕。本体 motifs.json は 767 件・2,676,192 bytes・schema_history 82 件。motifs_index_design.md §2 に補注 X 追加〔補注 A-X 全 24 件 intact・264,587 bytes〕。CLAUDE.md は 335,377 bytes〔retrofit 4-24 全エントリ intact〕。連動軸十九系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）〕の書き下し anchor 自己参照タグ運用が完全整合。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-23_retrofit24_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit23_complete.md`〔retrofit 23 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-X 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・767 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 24 commit です。

【本セッションの選択肢】
(A) retrofit 25 候補〔教学系軸：吽字義軸（中心成句要再検討）／三教指帰軸／般若心経秘鍵 仏法不外求軸（m492/m493 clean）／大日経疏 巻第一 残 42 件の他主題軸化〕
(B) kaimyo-app 教学系素材活用：連動軸十九系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- git status 等の実行後は .git/index.lock 残留に留意〔残留時は commit_push.bat 実行前に除去・retrofit 22 §(d-4)〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)・retrofit 22-24 で再運用〕
- anchor を扱う retrofit では着手時に書き下し anchor 自己参照タグ全件検証を行う〔retrofit 21 §(d-1)・retrofit 24 で全件 OK 確認〕
- sg 成句 motif 自身は連動タグ未保有（成句は連動の参照先であり連動 motif プールの成員ではない・十九系統一律の設計仕様・retrofit 24 §(d-1)）
- 単独 anchor 体制（補注 J/N/P/R/S/T/U/X 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q/V/W 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-23〔retrofit 24 完走・般若心経秘鍵 大心真言三摩地法門 教学系軸連動 retrofit。新規 sg-id `sg23`「大心真言三摩地法門」を新設〔出典:般若心経秘鍵〕、書き下し anchor として単独 anchor m496 を採用（m496 般若心経秘鍵 第四節 題号釈「大般若波羅蜜多心経といっぱ、即ち是れ大般若菩薩の大心真言三摩地法門なり。文は一紙に欠けて、行は則ち十四なり」心経の題号を大心真言三摩地法門と規定する核心句）。強連動 4 motif：m491（第一節 帰敬讃）/ m498（第八節 大心咒の釈）/ m501（第九節 真言不思議の頌）/ m504（第十一節 結頌）に「連動:sg23」「連動:m496」を付与（+10 タグ）。total_motifs 766→767（+1 新規 sg23）・famous_phrases 22→23。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,676,192 bytes〔+5,806〕・schema_history 82 件〔+1・origin: retrofit_24:doctrine〕・補注 X 追加〔motifs_index_design.md §2・247,628→264,587 bytes・+16,959〕・CLAUDE.md 更新完了〔330,354→335,377 bytes〕・commit_message.txt 書き換え済。連動軸十九系統並立に到達。教学系軸（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心）に続く教学系軸の第七例で、空海撰『般若心経秘鍵』による『般若心経』の密教的読解を主題とする軸。単独 anchor 体制の運用第七例（retrofit 14/16/18/19/20/21 に続く）。中心成句「大心真言三摩地法門」を anchor m496 が literal で直接含有し、retrofit 23 三種菩提心（literal 0 件）より強い成句支持をなす。retrofit 22 浄菩提心・retrofit 23 三種菩提心 の二重 anchor 系統対比型に続いて単独 anchor 体制に戻る。anchor 1 ＋ 強連動 4 ＝ 5 motif の小規模 retrofit。Phase D 必須チェックリストに完全準拠する第十六の retrofit〕

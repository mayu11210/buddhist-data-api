# 引き継ぎメモ：retrofit 25 完走〔吽字義 吽字四字 教学系軸連動 retrofit〕

**日付**：2026-05-23
**フェーズ**：retrofit 25（retrofit 24 完走に続く第二十二の retrofit セッション）
**対象**：空海撰『吽字義』に説かれる聖音「吽」一字をめぐる密教字義論の中心概念「吽字四字」の連動軸新設。新規 sg-id `sg24`「吽字四字」を追加し、書き下し anchor として **単独 anchor m564** を採用。m564（吽字義 第三節 四字合釈・「つぎに合して釈せば、この吽は四字をもって一字を成ず。いわゆる四字とは阿・訶・汙・麼なり。阿は法身の義、訶は報身の義、汙は応身の義、麼は化身の義なり。この四種をあげてかの諸法を摂するに、括らざるところなし」吽字を四字四身として総合する合釈核心句）を単独の書き下し anchor とする。強連動 3 motif（m550 第一節 字相字義 / m561 第二節 麼字 / m566 第四節 大空点・佉字門）に連動タグを付与。連動軸二十系統並立に到達。本 retrofit は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門 に続く **教学系軸の第八例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 24 大心真言三摩地法門 同型の **単独 anchor 体制の運用第八例**。anchor 1 ＋ 強連動 3 ＝ 4 motif の小規模 retrofit。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 Y 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 26 候補〔教学系軸：般若心経秘鍵 仏法不外求軸（m492/m493 clean・規模再検討要）／三教指帰軸／大日経疏 巻第一 残 42 件の他主題軸化〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_25:doctrine〕
- [x] motifs_index_design.md に補注 Y 追加済〔補注 A-Y 全 25 件 intact・264,587→282,270 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・335,377→340,560 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 25 用・冒頭行整合確認済〕
- [x] handoff_2026-05-23_retrofit25_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 24 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 24 完走〔般若心経秘鍵 大心真言三摩地法門 教学系軸連動・commit `812a1f9`〕に続く第二十二の retrofit セッション。

retrofit 24 完走 handoff §(c) 選択肢 A〔retrofit 25 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で吽字義 吽字四字軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg24`「吽字四字」を追加〔出典:吽字義・空海撰『吽字義』に説かれる聖音「吽」一字を阿・訶・汙・麼の四字に開き法身・報身・応身・化身の四身を配する密教字義論の中心概念〕
- 書き下し anchor は **単独 anchor m564**（吽字義 第三節 四字合釈）
- 強連動 3 motif（m550 第一節 字相字義 / m561 第二節 麼字 / m566 第四節 大空点・佉字門）に「連動:sg24」「連動:m564」を付与（+8 タグ）
- 連動軸二十系統並立に到達
- **教学系軸の第八例**（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門 に続く・吽字四字は聖音「吽」一字の密教字義論を主題とする）
- **単独 anchor 体制の運用第八例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 24 大心真言三摩地法門 に続く）
- **4 motif retrofit**（anchor 1 ＋ 強連動 3・retrofit 20 声字実相 と同規模の小規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 24 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸十九系統（sg02/sg03/sg07-sg23）の書き下し anchor がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg23）は十九系統一律に連動タグ未保有であり、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりで整合。Phase A スキャンで retrofit 25 候補（吽字義軸／三教指帰軸／般若心経秘鍵 仏法不外求軸／大日経疏 巻第一 残 42 件他主題軸）の中心成句の kakikudashi 直接含有を全 767 motif にわたり網羅検査：

| 候補 | corpus clean 率 | kakikudashi 支持 | 判定 |
|---|---|---|---|
| 吽字義軸 | ujiji 13/18 clean | 四字合釈「この吽は四字をもって一字を成ず……阿・訶・汙・麼」literal を m564 が直接含有・字相字義/麼字/大空点の clean 3 件（m550/m561/m566）が強連動候補で主題一貫 | 採用 |
| 般若心経秘鍵 仏法不外求軸 | hannya-hiken（本軸該当 2 件 clean） | 「仏法不外求」書き下し直接含有 m492 1 件のみ・強連動 m493 1 件で anchor＋強連動 2 motif の過去最小規模 | 基準未達・retrofit 26 以降に温存 |
| 三教指帰軸 | sankyo-shiki 21/21 完全 clean | 「三教」literal 3 件すべて枠組み motif・連動軸モデルへの適合が弱い（retrofit 4 発言者軸運用済） | 基準未達・retrofit 26 以降に温存 |
| 大日経疏 残 42 件他主題軸 | — | 如実知自心は sg15 長者窮子 anchor m717 で吸収済・三劫/六無畏 corpus 内 0 件で中心成句不明瞭 | 基準未達・retrofit 26 以降に温存 |

retrofit 25 Phase A スキャンの実測で、吽字義 corpus（ujiji・m549-m566 の 18 件）は 13 件が連動タグ未保有の clean（m549/m551/m552/m553 は sg08 阿字本不生・m565 は sg07 三句法門 連動済）であり、聖音「吽」を四字四身の一字として読みひらく密教字義論が clean motif 群に一貫することを確認。中心成句「吽字四字」の四字合釈は m564（吽字義 第三節）が「この吽は四字をもって一字を成ず。いわゆる四字とは阿・訶・汙・麼なり」と literal kakikudashi に直接含有し、これを単独の書き下し anchor とする構成が可能であることを確認。ケンシン裁定で判断 1-3：

- **判断 1**：軸採用 = 吽字義軸（ujiji corpus 18 件中 13 件 clean・聖音「吽」を四字四身の一字として読む密教字義論が clean motif 群に一貫・正常規模 retrofit を成立させられる唯一の候補）
- **判断 2**：中心成句 sg24 =「吽字四字」（『吽字義』四字合釈において聖音「吽」を阿・訶・汙・麼の四字に開き法身・報身・応身・化身の四身を配する吽字義固有の中心概念・m564 が literal kakikudashi 直接含有。「字相字義」案は nikyo-ron・hizo-houyaku にも分布し吽字義固有性が弱いため退けた）
- **判断 3**：anchor 体制・規模 = 単独 anchor m564・4 motif（四字合釈の literal kakikudashi 直接含有は m564 単独であり引証系統の対 anchor を欠くため、retrofit 22-23 の二重 anchor 系統対比型ではなく単独 anchor が自然形）

### Phase B：4 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m564 | 吽字義 第三節 四字合釈 | 書き下し anchor（単独・自己参照）・「つぎに合して釈せば、この吽は四字をもって一字を成ず。いわゆる四字とは阿・訶・汙・麼なり。阿は法身の義、訶は報身の義、汙は応身の義、麼は化身の義なり。この四種をあげてかの諸法を摂するに、括らざるところなし」吽字を四字四身として総合する合釈核心句 |
| m550 | 吽字義 第一節 | 強連動・「一切世間はただしかくのごとくの字相のみを知って、未だ曾つて字義を解せず。この故に生死の人となす。如来は実のごとく実義を知り知りたまえり。このゆえに大覚と号す」字相（浅略釈）と字義（深秘釈）を対比し密教言語観の根本テーゼを宣言する句 |
| m561 | 吽字義 第二節 | 強連動・「経にいわく、麼字とは大日の種子なり。一切世間は我我を計すといえども、未だ実義を証せず。ただ大日如来のみいまして、無我の中において大我を得たまえり」吽字四字の麼字を大日の種子・無我大我として釈す句 |
| m566 | 吽字義 第四節 | 強連動・「擁護の義とは、上に大空の点あり、これ佉字門なり……中に訶字あり、これ因の義なり。この虚空蔵の中において真因の種子を含養す」吽字の大空の点を佉字門・訶字を因として釈す擁護段の句 |

体系内連節カバー：字相字義の対比（m550 第一節）→ 麼字の釈（m561 第二節）→ 四字合釈の核心句（m564 第三節 anchor）→ 大空点・佉字門の釈（m566 第四節）の吽字義 第一〜第四節を一括包摂。

**除外・温存**：吽字義 corpus（ujiji 18 件）のうち本軸に含めなかった 14 件のうち、m549（阿字の義）・m551（訶字門 因不可得）・m552（阿字三義）・m553（本不生際・如実知自心）は retrofit 8 で阿字本不生 sg08、m565（『大日経』『金剛頂経』の菩提因・大悲根・方便究竟）は retrofit 6 で三句法門 sg07 に連動済。clean の m555（阿字七義）は阿字を主題とし sg08 阿字本不生 と thematic に重なるため本軸から除外（(d-3) 参照）。m554（甚深秘蔵）・m556-m560（一心法界・日月星辰・真如法性・水波・同一多如）・m562（法身三密）・m563（われすなわち法界）は吽字四字の四字合釈とは別主題であり「主題:吽字」等のタグ保持により別途検索可能なため温存。本軸 4 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 767 | 768 | +1（sg24 新規追加） |
| famous_phrases | 23 | 24 | +1 |
| ファイルサイズ | 2,676,192 bytes | 2,682,561 bytes | +6,369 |
| schema_history | 82 | 83 | +1（origin: retrofit_25:doctrine） |
| 連動タグ総数 | — | — | +8（sg24 軸 4 motif × 2） |
| kakikudashi_chars_total | 112,842 | 112,846 | +4（「吽字四字」4 字） |
| gendaigoyaku_chars_total | 322,464 | 324,146 | +1,682（sg24 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 768 vs 768 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg24 軸 4 motif × 2〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg24 連番・末尾 sg24 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 24 で recompute した stats は retrofit 25 着手時点で全 6 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 25 では stats を全件 recompute して真値を書き込み（total_motifs 768・famous_phrases 24・kakikudashi_chars_total 112,846・gendaigoyaku_chars_total 324,146・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 Y 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 Y〔吽字義 吽字四字 教学系軸連動の運用〕新規追加（264,587→282,270 bytes・+17,683・補注 A-Y 全 25 件 intact・全角丸括弧 102/102 balanced・〔〕23/23 balanced・かぎ括弧 39/39 balanced・二重かぎ 16/16 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 25 完走エントリを追加（335,377→340,560 bytes・retrofit 4-25 全エントリ intact・追加部分の〔〕12/12・かぎ括弧 6/6・二重かぎ 2/2・全角丸括弧 1/1 balanced・新規半角括弧 0 件・全角〔〕全体 1113/1113 balanced）。
- `commit_message.txt` を retrofit 25 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-23_retrofit25_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第八例・聖音の字義論軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学、retrofit 21 即身成仏義 二頌八句軸は空海の即身成仏論、retrofit 22 浄菩提心軸は『大日経』『大日経疏』の菩提心論、retrofit 23 三種菩提心軸は龍猛菩薩造『菩提心論』の発菩提心論、retrofit 24 大心真言三摩地法門軸は空海撰『般若心経秘鍵』による『般若心経』の密教的読解を主題とする教学系軸であった。retrofit 25 吽字四字軸はその継続でありながら、空海撰『吽字義』による聖音「吽」一字の密教字義論を主題とする点に特色をもつため、教学系軸の第八例と位置づける。声字実相 sg19 が真言・声字の総論（声字実相義）を軸とするのに対し、吽字四字 sg24 はその個別の一字（聖音「吽」）に四字四身の構造を読む字義論の各論を軸とし、空海の密教言語論のうちに総論（sg19）と一字の各論（sg24）として並立する。

#### 2. 連動軸二十系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）〕の二十系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）・即身成仏論（六大四曼三密）・本来性論（浄菩提心）・発菩提心論（三種菩提心）・密教的心経読解（大心真言三摩地法門）に加えて、吽字・字義・四身（吽字四字）でも素材プールを切替可能。

#### 3. 単独 anchor 体制の運用第八例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599・retrofit 19 顕密二教 sg18/m571・retrofit 20 声字実相 sg19/m525・retrofit 21 六大無礙 sg20/m534・retrofit 24 大心真言三摩地法門 sg23/m496 に続く第八の単独 anchor 体制。四字合釈「この吽は四字をもって一字を成ず……阿・訶・汙・麼」の literal kakikudashi 直接含有は吽字義 第三節 m564 単独であり、引証系統の対 anchor を欠くため、典籍系統対比型の二重 anchor（retrofit 22 浄菩提心・retrofit 23 三種菩提心）を要さず単独 anchor が自然形となる。retrofit 24 大心真言三摩地法門 に続いて単独 anchor 体制を継続する。

#### 4. anchor 直接含有による中心成句支持

retrofit 23 三種菩提心 sg22 は中心成句「三種菩提心」の literal kakikudashi 直接含有が 0 件で書き下し anchor が成句を担う構成であった。これに対し retrofit 25 吽字四字 sg24 は、四字合釈「この吽は四字をもって一字を成ず。いわゆる四字とは阿・訶・汙・麼なり」を anchor m564 が literal で直接含有し、四字四身の構造そのものが anchor に明示される。retrofit 20 声字実相・retrofit 24 大心真言三摩地法門 と同型の、中心成句が anchor に直接現れる教学系軸。

#### 5. thematic adjacency と連動タグ overlap の区別の再運用・sg08 阿字本不生 overlap への対応

吽字義 corpus には sg08 阿字本不生 anchor m549 が居住し（retrofit 23 完走 handoff §(c)・retrofit 24 完走 handoff §(d-4) が指摘した overlap）、阿字を主題とする m549/m551/m552/m553 が sg08 に連動済である。本軸は阿・訶・汙・麼の四字を統合する四字合釈 m564 を anchor とし、阿字に固有の clean motif m555（阿字七義）は sg08 阿字本不生 と thematic に重なるため本軸から除外して、字相字義（m550）・麼字（m561）・大空点（m566）の clean motif で軸を構成した。これにより吽字義軸と阿字本不生軸の連動タグ overlap はゼロに保たれ、阿字本不生 sg08 は吽字の一構成要素たる阿字を、吽字四字 sg24 は四字を統合する吽字一字を、それぞれ別系統の連動軸として並立させる。retrofit 21 補注 U・retrofit 22 補注 V・retrofit 23 補注 W・retrofit 24 補注 X の方針を踏襲。

#### 6. 4 motif 規模・小規模 retrofit

anchor 1 ＋ 強連動 3 ＝ 4 motif は retrofit 20 声字実相（4 motif）と同等の小規模 retrofit。吽字義 corpus 18 件のうち聖音「吽」を四字四身として読む骨格 4 件（字相字義・麼字・四字合釈・大空点）に絞り、阿字本不生 sg08 連動済の m549/m551/m552/m553・三句法門 sg07 連動済の m565・別主題 motif（一心法界・日月星辰・真如法性 等）を温存することで自然に小規模化した。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=768  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg24軸 4motif×2 全付与  OK
7. sg list sg01-sg24 continuous, tail=sg24  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK
   anchor 自己参照タグ 連動軸二十系統: ALL OK

[stats（retrofit 25 後）]
total_motifs=768  famous_phrases=24
kakikudashi_chars_total=112,846
gendaigoyaku_chars_total=324,146
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=83 entries
file size=2,682,561 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 26〔教学系軸の継続〕

- **般若心経秘鍵 仏法不外求軸**：般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす。ただし「仏法不外求」の書き下し直接含有は m492 1 件のみで、強連動 motif 群が m493 1 件にとどまり anchor＋強連動 2 motif の過去最小規模となるため、軸規模の再検討を要する（(d-2) 参照）。
- **三教指帰軸**：sankyo-shiki corpus 21 件は全件 clean だが、「三教」literal 3 件（m656/m675/m676）はいずれも枠組み motif で、連動軸モデル（成句＋書き下し anchor＋強連動）への適合が弱い。retrofit 4 で発言者軸（亀毛先生／虚亡隠士／仮名乞児）を運用済。
- **大日経疏 巻第一 残 42 件他主題軸**：dainichikyo-sho-vol1 68 件中 42 件が未連動。如実知自心は sg15 長者窮子 anchor m717 が吸収済・三劫/六無畏 は corpus 内 0 件で中心成句不明瞭。retrofit 22-25 同様に基準未達と判定済。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸二十系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg24 吽字四字（吽字義）は吽字・字義・四身（法身・報身・応身・化身）を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔十九系統 書き下し anchor 全件 OK・retrofit 25 後 二十系統 完全整合〕

retrofit 21 §(d-1)・retrofit 24 §(d-1) の指示に従い、retrofit 25 着手時に連動軸十九系統（sg02/sg03/sg07-sg23）の書き下し anchor 自己参照タグ全件検証を実施した結果、全 anchor（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728/m506/m581/m496・m636 は sg10/sg14 共有）がすべて「連動:sgNN」「連動:m(anchor)」を保有していることを確認した（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg23）は十九系統一律に連動タグ未保有であるが、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりであり、defect ではなく十九系統一律の設計仕様。retrofit 25 で追加した sg24 単独 anchor m564 も「連動:sg24」「連動:m564」を保有し、検証スクリプトで連動軸二十系統 anchor の自己参照タグが ALL OK（完全整合）であることを確認した。今後 anchor を扱う retrofit でも着手時の書き下し anchor 自己参照タグ全件検証を継続する。

### (d-2) 般若心経秘鍵 仏法不外求軸の規模問題と温存

般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る。明暗他に非ざれば、信修すれば忽ちに証す」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす（m492 は既存「主題:仏法不外求」タグ保持）。retrofit 24 完走 handoff §(d-2) が retrofit 25 以降の独立軸候補として温存したものだが、retrofit 25 Phase A スキャンの実測で、「仏法不外求」の書き下し「仏法遥かに非ず／真如外に非ず」の literal kakikudashi 直接含有は m492 1 件のみ、強連動候補も m493 1 件にとどまり、anchor m492 ＋ 強連動 m493 ＝ 2 motif と過去最小（retrofit 20 声字実相 4 motif）を下回る規模となることが判明した。連動軸として構造的に薄いため、retrofit 25 ではケンシン裁定で吽字義軸を採用し、仏法不外求軸は retrofit 26 以降に温存した。将来 retrofit で仏法不外求軸を採る場合、強連動 motif 群の構成（他 corpus からの引証 motif 等を含めた拡大）を再検討する必要がある。

### (d-3) 吽字義軸と sg08 阿字本不生軸の overlap 処理

吽字義 corpus（ujiji 18 件）には sg08 阿字本不生 anchor m549 が第一節に居住し、阿字を主題とする m549/m551/m552/m553 が sg08 に連動済である。聖音「吽」は阿・訶・汙・麼の四字をもって成る一字であり、阿字はその一構成要素であるため、吽字義軸と阿字本不生 sg08 は thematic に隣接する。retrofit 25 はこの overlap を、四字を統合する四字合釈 m564 を anchor とし、阿字に固有の clean motif m555（阿字七義）を本軸から除外することで処理した。本軸 4 motif（m564/m550/m561/m566）はいずれも着手前 clean であり、既存軸との連動タグ overlap はゼロである。吽字四字 sg24 は四字を統合する吽字一字を、阿字本不生 sg08 は吽字の一構成要素たる阿字を、それぞれ別系統の連動軸として並立させる。retrofit 23 §(c)・retrofit 24 §(d-4) が指摘した吽字義 corpus の sg08 overlap は、本 retrofit で連動タグ overlap ゼロのまま軸化を達成したことで一段落した。

### (d-4) 吽字義 corpus のカバー範囲

retrofit 25 後、吽字義 corpus（ujiji 18 件）は 9 件が連動タグ保有（sg24 軸 4 件 m550/m561/m564/m566・sg08 阿字本不生 4 件 m549/m551/m552/m553・sg07 三句法門 1 件 m565）・9 件が未連動（m554/m555/m556/m557/m558/m559/m560/m562/m563）である。未連動 9 件のうち m555 は阿字七義（sg08 阿字本不生 と thematic 隣接）、残 8 件は甚深秘蔵・一心法界・日月星辰・真如法性・水波・同一多如・法身三密・われすなわち法界 の別主題であり、中心成句が明瞭でないため将来 retrofit での軸化余地は限定的。

### (d-5) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg24 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-25 で sg08-sg24 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-25 一貫して未更新の pre-existing 事象。retrofit 25 でも踏襲し未変更とした。将来 "sg01-sg24" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-6) 編集手法・truncate 事象回避

retrofit 25 のビルドスクリプト（`outputs/retrofit25_unji_yonji.py`）・Phase A スキャンスクリプト（`outputs/retrofit25_phaseA_scan.py`）・検証スクリプト（`outputs/retrofit25_verify.py`）・補注 Y 追加スクリプト（`outputs/add_chunote_y_retrofit25.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit25.py`）はいずれも Python script として作成。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（dry-run + 本番適用の二段運用）。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。今後もスクリプト・長文ファイルの作成は Python write_bytes / bash heredoc を第一選択とすることを推奨。

### (d-7) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。retrofit 25 着手時に `git status --short` を確認した結果、`.git/index.lock` 残留はなく、staged 変更（削除ステージ等）も検出されず、git index は健全であった。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-24 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。git status 等の実行後は `.git/index.lock` 残留に留意し、残留した場合は commit_push.bat 実行前に除去する（retrofit 22 §(d-4)）。

### (d-8) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 25 後で 全角〔/〕1113/1113 balanced。retrofit 25 の追加部分（タイトル行・最終更新行の retrofit 25 エントリ）は〔〕12 対・かぎ括弧 6 対・二重かぎ 2 対・全角丸括弧 1 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5)・retrofit 19 §(d-7)・retrofit 20 §(d-7)・retrofit 21 §(d-7)・retrofit 22 §(d-8)・retrofit 23 §(d-8)・retrofit 24 §(d-8) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔768 件・m1-m744 + sg01-sg24・2,682,561 bytes・schema_history 83 件〕
- 本 retrofit build script：`outputs/retrofit25_unji_yonji.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit25_phaseA_scan.py`
- Phase A 結果まとめ：`outputs/retrofit25_phaseA_out.txt`
- 整合性検証 script：`outputs/retrofit25_verify.py`
- 補注 Y 追加 script：`outputs/add_chunote_y_retrofit25.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit25.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit25.json`〔retrofit 前 motifs.json・2,676,192 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit25.md`〔retrofit 前・264,587 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit25.md`〔retrofit 前・335,377 bytes〕
  - `outputs/commit_message_backup_pre_retrofit25.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-23_retrofit24_complete.md`〔般若心経秘鍵 大心真言三摩地法門 教学系軸連動〕
- 補注 Y 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 25 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-24 完走 → 2026-05-23 retrofit 25 完走〔吽字義 吽字四字 教学系軸連動・新規 sg24「吽字四字」+ 単独 anchor m564 採用（吽字義 第三節 四字合釈）・強連動 3 件（m550/m561/m566）・連動軸二十系統並立に到達・教学系軸の第八例・単独 anchor 体制 第八例〕。本体 motifs.json は 768 件・2,682,561 bytes・schema_history 83 件。motifs_index_design.md §2 に補注 Y 追加〔補注 A-Y 全 25 件 intact・282,270 bytes〕。CLAUDE.md は 340,560 bytes〔retrofit 4-25 全エントリ intact〕。連動軸二十系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）〕の書き下し anchor 自己参照タグ運用が完全整合。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-23_retrofit25_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-23_retrofit24_complete.md`〔retrofit 24 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-Y 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・768 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 25 commit です。

【本セッションの選択肢】
(A) retrofit 26 候補〔教学系軸：般若心経秘鍵 仏法不外求軸（m492/m493 clean・規模再検討要）／三教指帰軸／大日経疏 巻第一 残 42 件の他主題軸化〕
(B) kaimyo-app 教学系素材活用：連動軸二十系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- git status 等の実行後は .git/index.lock 残留に留意〔残留時は commit_push.bat 実行前に除去・retrofit 22 §(d-4)〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)・retrofit 22-25 で再運用〕
- anchor を扱う retrofit では着手時に書き下し anchor 自己参照タグ全件検証を行う〔retrofit 21 §(d-1)・retrofit 25 で全件 OK 確認〕
- sg 成句 motif 自身は連動タグ未保有（成句は連動の参照先であり連動 motif プールの成員ではない・二十系統一律の設計仕様・retrofit 25 §(d-1)）
- 単独 anchor 体制（補注 J/N/P/R/S/T/U/X/Y 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q/V/W 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-23〔retrofit 25 完走・吽字義 吽字四字 教学系軸連動 retrofit。新規 sg-id `sg24`「吽字四字」を新設〔出典:吽字義〕、書き下し anchor として単独 anchor m564 を採用（m564 吽字義 第三節 四字合釈「つぎに合して釈せば、この吽は四字をもって一字を成ず。いわゆる四字とは阿・訶・汙・麼なり。阿は法身の義、訶は報身の義、汙は応身の義、麼は化身の義なり。この四種をあげてかの諸法を摂するに、括らざるところなし」吽字を四字四身として総合する合釈核心句）。強連動 3 motif：m550（第一節 字相字義）/ m561（第二節 麼字）/ m566（第四節 大空点・佉字門）に「連動:sg24」「連動:m564」を付与（+8 タグ）。total_motifs 767→768（+1 新規 sg24）・famous_phrases 23→24。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,682,561 bytes〔+6,369〕・schema_history 83 件〔+1・origin: retrofit_25:doctrine〕・補注 Y 追加〔motifs_index_design.md §2・264,587→282,270 bytes・+17,683〕・CLAUDE.md 更新完了〔335,377→340,560 bytes〕・commit_message.txt 書き換え済。連動軸二十系統並立に到達。教学系軸（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門）に続く教学系軸の第八例で、空海撰『吽字義』による聖音「吽」一字の密教字義論を主題とする軸。単独 anchor 体制の運用第八例（retrofit 14/16/18/19/20/21/24 に続く）。中心成句「吽字四字」の四字合釈を anchor m564 が literal で直接含有する。retrofit 24 大心真言三摩地法門 に続いて単独 anchor 体制を継続。anchor 1 ＋ 強連動 3 ＝ 4 motif の小規模 retrofit。sg08 阿字本不生 overlap は四字合釈 m564 を anchor とし阿字固有 motif を除外することで連動タグ overlap ゼロのまま処理。Phase D 必須チェックリストに完全準拠する第十七の retrofit〕

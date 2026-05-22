# 引き継ぎメモ：retrofit 23 完走〔菩提心論 三種菩提心 教学系軸連動 retrofit〕

**日付**：2026-05-22
**フェーズ**：retrofit 23（retrofit 22 完走に続く第二十の retrofit セッション）
**対象**：龍猛菩薩造『金剛頂瑜伽中発阿耨多羅三藐三菩提心論』（菩提心論）に説かれる密教の菩提心論の中心概念「三種菩提心」（行願・勝義・三摩地）の連動軸新設。新規 sg-id `sg22`「三種菩提心」を追加し、書き下し anchor として **二重 anchor 系統対比型 m506+m581** を採用。m506（菩提心論 第一節・「諸仏菩薩、昔は因地にあって、この心を発しおわり、勝義・行願・三摩地を戒となす……ただ真言法の中にのみ即身成仏するが故に、これ三摩地の法を説くなり」三種菩提心を戒とする総説）を菩提心論 本文系 anchor、m581（弁顕密二教論 巻上 第二章 第二節（十）引証喩釈・『金剛頂発菩提心論』を引いて「勝義・行願・三摩地を戒となす」と説く引証）を弁顕密二教論 引証系 anchor とする。強連動 3 motif（m507 菩提心論 第二節 行願菩提心 / m510 第三節 勝義菩提心 / m516 第四節 三摩地菩提心 月輪観）に連動タグを付与。連動軸十八系統並立に到達。本 retrofit は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心 に続く **教学系軸の第六例**。retrofit 11 火宅三車・retrofit 13 化城宝処・retrofit 15 三草二木・retrofit 17 従地涌出・retrofit 22 浄菩提心 同型の **二重 anchor 体制 系統対比型の運用第六例**。anchor 2 ＋ 強連動 3 ＝ 5 motif の小規模 retrofit。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 5 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 W 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 24 候補〔教学系軸：般若心経秘鍵軸（中心成句要再検討）／吽字義軸（中心成句要再検討）／三教指帰 等の未軸化 corpus・大日経疏 巻第一 残 42 件の他主題軸化〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_23:doctrine〕
- [x] motifs_index_design.md に補注 W 追加済〔補注 A-W 全 23 件 intact・231,348→247,628 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・324,423→330,354 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 23 用・冒頭行整合確認済〕
- [x] handoff_2026-05-22_retrofit23_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 22 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 22 完走〔大日経疏 vol1 浄菩提心 教学系軸連動・commit `70a856d`〕に続く第二十の retrofit セッション。

retrofit 22 完走 handoff §(c) 選択肢 A〔retrofit 23 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で菩提心論 三種菩提心軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg22`「三種菩提心」を追加〔出典:菩提心論・龍猛菩薩造『金剛頂瑜伽中発阿耨多羅三藐三菩提心論』に説かれる行願・勝義・三摩地の三種の菩提心を総称する密教菩提心論の中心概念〕
- 書き下し anchor は **二重 anchor 系統対比型 m506+m581**（m506 菩提心論 第一節 本文・m581 弁顕密二教論 巻上 第二章 第二節（十）引証）
- 強連動 3 motif（m507 菩提心論 第二節 行願菩提心 / m510 第三節 勝義菩提心 / m516 第四節 三摩地菩提心 月輪観）に「連動:sg22」「連動:m506」「連動:m581」を付与（+15 タグ）
- 連動軸十八系統並立に到達
- **教学系軸の第六例**（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心 に続く・三種菩提心は密教の発菩提心の実践を主題とする）
- **二重 anchor 体制 系統対比型の運用第六例**（retrofit 11 火宅三車・retrofit 13 化城宝処・retrofit 15 三草二木・retrofit 17 従地涌出・retrofit 22 浄菩提心 に続く・出典の本文 m506 と他著作の引証 m581 を対比する初例）
- **5 motif retrofit**（anchor 2 ＋ 強連動 3・retrofit 20-21 と同等の小規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 22 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸十七系統（sg02/sg03/sg07-sg21）の書き下し anchor 22 motif（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728）がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（補整不要）。なお sg 成句 motif 自身（sg02/sg03/sg07-sg21）は十七系統すべて一律に連動タグ未保有であり、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計（過去 retrofit の検証対象も書き下し anchor の mNNN）どおりで整合。Phase A スキャンで retrofit 23 候補（菩提心論軸／般若心経秘鍵軸／吽字義軸／大日経疏 巻第一 残 42 件他主題軸）の中心成句の kakikudashi 直接含有を全 765 motif にわたり網羅検査：

| 候補 | corpus clean 率 | kakikudashi 支持 | 判定 |
|---|---|---|---|
| 菩提心論軸 | bodaishinron 15/15 完全 clean | 「三種菩提心」literal 0 件・書き下し「勝義・行願・三摩地を戒となす」を m506・m581 が直接含有 | 採用 |
| 般若心経秘鍵軸 | hannya-hiken 12/15 clean | 各中心成句候補が 1 件のみ・成句性が弱い | retrofit 24 以降に温存 |
| 吽字義軸 | ujiji 12/18 clean | 「吽」kakikudashi 直接含有 2 件・字相/字義 3 corpus 拡散・中心成句不明瞭 | 基準未達・retrofit 24 以降に温存 |
| 大日経疏 残 42 件他主題軸 | — | 如実知自心 4 件すべて既存軸連動済（overlap 100%）・外道破斥 m741-744 等は中心成句不明瞭 | 基準未達・retrofit 24 以降に温存 |

retrofit 23 Phase A スキャンの実測で、菩提心論 corpus（bodaishinron・m506-m520 の 15 件）が全件連動タグ未保有の完全 clean であり、行願・勝義・三摩地の三種菩提心という明確な教学構造を corpus 内にもつ唯一の候補であることを確認。中心成句「三種菩提心」の literal kakikudashi 直接含有は 0 件だが、書き下し「勝義・行願・三摩地を戒となす」を m506（菩提心論 第一節 本文）と m581（弁顕密二教論 引証）が同一文で直接含有することが判明し、二重 anchor 系統対比型の構成が可能であることを確認。ケンシン裁定で判断 1-3：

- **判断 1**：軸採用 = 菩提心論軸（bodaishinron corpus 15 件が完全 clean・三種菩提心の明確な教学構造）
- **判断 2**：中心成句 sg22 =「三種菩提心」（龍猛菩薩造『菩提心論』に説かれる行願・勝義・三摩地の三種の菩提心を総称する密教菩提心論の中心概念）
- **判断 3**：anchor 体制・規模 = 二重 anchor 系統対比型 m506+m581・5 motif（同一文「勝義・行願・三摩地を戒となす」を菩提心論 本文 m506 と弁顕密二教論 引証 m581 の二系統で保持。単独 anchor m506 案・秘蔵宝鑰 引証 m651/m653 を含む拡大案を退け、本文系統と引証系統の二系統で保持する点を重視）

### Phase B：5 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m506 | 菩提心論 第一節 | 書き下し anchor（菩提心論 本文系・片翼・自己参照）・「諸仏菩薩、昔は因地にあって、この心を発しおわり、勝義・行願・三摩地を戒となす……ただ真言法の中にのみ即身成仏するが故に、これ三摩地の法を説くなり」三種菩提心を戒とする総説 |
| m581 | 弁顕密二教論 巻上 第二章 第二節（十）引証喩釈 | 書き下し anchor（弁顕密二教論 引証系・片翼・自己参照）・「『金剛頂発菩提心論』にいわく、諸仏菩薩、昔因地に在して、この心を発しおわって勝義・行願・三摩地を戒となす……惟真言法の中にのみ即身成仏するが故に、これ三摩地の法を説く」菩提心論を引く引証 |
| m507 | 菩提心論 第二節 | 強連動・「我まさに無余の有情界を利益し安楽すべし。十方の含識を観ずること、なおし己身の如し」行願菩提心の文 |
| m510 | 菩提心論 第三節 | 強連動・「二に勝義とは、一切の法は無自性と観ず。大毘盧遮那成仏経にいうが如し……この観を作しおわるを勝義の菩提心と名づく」勝義菩提心の定義 |
| m516 | 菩提心論 第四節 | 強連動・「一切有情は悉く普賢の心を含せり。我れ自心を見るに形は月輪の如し。満月円明の体はすなわち菩提心と相類せり」三摩地菩提心の月輪観 |

体系内連節カバー：三種菩提心を戒とする総説（m506 菩提心論 本文・m581 弁顕密二教論 引証）から、行願菩提心（m507 第二節）→ 勝義菩提心（m510 第三節）→ 三摩地菩提心 月輪観（m516 第四節）にわたる三種菩提心の三門を一括包摂。

**除外・温存**：菩提心論 corpus（bodaishinron 15 件）のうち本軸に含めなかった 10 件は三種菩提心の総説・三門の核心句以外（行願敷衍 m508/m509、勝義敷衍・引証 m511-m514、三句法門引証 m515、三摩地敷衍 m517-m519、即身成仏 結頌 m520）であり「主題:菩提心」等のタグ保持により別途検索可能なため温存。m515 は『大毘盧遮那経』の三句法門「菩提を因となし大悲を根となし方便を究竟となす」を引く motif で三句法門 sg07 と主題的に隣接するが、本軸（三種菩提心＝行願・勝義・三摩地）とは別系統のため温存。m520 は『菩提心論』結頌で即身成仏 sg03 の経偈と同一の偈「父母所生の身に速やかに大覚位を証す」を含むが即身成仏 結頌の別系統のため温存（将来 retrofit で sg03 連動の補整余地あり・(d-3) 参照）。本軸 5 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 765 | 766 | +1（sg22 新規追加） |
| famous_phrases | 21 | 22 | +1 |
| ファイルサイズ | 2,664,294 bytes | 2,670,386 bytes | +6,092 |
| schema_history | 80 | 81 | +1（origin: retrofit_23:doctrine） |
| 連動タグ総数 | — | — | +15（sg22 軸 5 motif × 3） |
| kakikudashi_chars_total | 112,828 | 112,833 | +5（「三種菩提心」5 字） |
| gendaigoyaku_chars_total | 319,480 | 321,021 | +1,541（sg22 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 766 vs 766 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg22 軸 5 motif × 3〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg22 連番・末尾 sg22 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 22 で recompute した stats は retrofit 23 着手時点で全 6 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 23 では stats を全件 recompute して真値を書き込み（total_motifs 766・famous_phrases 22・kakikudashi_chars_total 112,833・gendaigoyaku_chars_total 321,021・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 W 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 W〔菩提心論 三種菩提心 教学系軸連動の運用〕新規追加（231,348→247,628 bytes・+16,280・補注 A-W 全 23 件 intact・全角丸括弧 106/106 balanced・〔〕21/21 balanced・かぎ括弧 29/29 balanced・二重かぎ 16/16 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 23 完走エントリを追加（324,423→330,354 bytes・retrofit 4-23 全エントリ intact・追加部分の〔〕14/14・かぎ括弧 7/7・二重かぎ 2/2・全角丸括弧 2/2 balanced・新規半角括弧 0 件・全角〔〕全体 1065/1065 balanced）。
- `commit_message.txt` を retrofit 23 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-22_retrofit23_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第六例・密教菩提心論軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学、retrofit 21 即身成仏義 二頌八句軸は空海の即身成仏論、retrofit 22 浄菩提心軸は『大日経』『大日経疏』の菩提心論を主題とする教学系軸であった。retrofit 23 三種菩提心軸はその継続でありながら、龍猛菩薩造『菩提心論』に説かれる密教の発菩提心の実践（行願・勝義・三摩地）を主題とする点に特色をもつため、教学系軸の第六例と位置づける。三句法門 sg07 が密教修行の総綱を因・根・究竟の次第で説き、浄菩提心 sg21 がその因たる菩提心が行者に如実に浄められ現成する局面を anchor とするのに対し、三種菩提心 sg22 はその因たる菩提心そのものを行願・勝義・三摩地の三門に開いて行者が現に発し護持すべき具体相を anchor とする。

#### 2. 連動軸十八系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）〕の十八系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）・即身成仏論（六大四曼三密）・本来性論（浄菩提心）に加えて、菩提心論・発心・密教実践論（三種菩提心）でも素材プールを切替可能。

#### 3. 二重 anchor 体制 系統対比型の運用第六例・本文系統と引証系統の対比

retrofit 11 sg10/m209+m636（性霊集 vs 秘蔵宝鑰）・retrofit 13 sg12/m227+m569（性霊集 vs 秘蔵宝鑰）・retrofit 15 sg14/m215+m636（性霊集 vs 秘蔵宝鑰）・retrofit 17 sg16/m639+m690（秘蔵宝鑰 vs 大日経疏）・retrofit 22 sg21/m638+m728（秘蔵宝鑰 vs 大日経疏）に続く第六の系統対比型。本 retrofit 23 sg22/m506+m581 は、retrofit 22 sg21 が同一経文を釈文（大日経疏）と引証（秘蔵宝鑰）の二系統で対比したのと同型でありながら、出典の本文そのもの（菩提心論 m506）と他著作による引証（弁顕密二教論 m581）を対比する点に特色がある。本文系統 anchor と引証系統 anchor の対比は連動軸として初例。

#### 4. 菩提心論 corpus の完全 clean からの軸構成

菩提心論 corpus（bodaishinron 15 件）は retrofit 23 着手時点で全件が連動タグ未保有の完全 clean であり、行願・勝義・三摩地の三種菩提心という明確な教学構造を corpus 内にもつ唯一の retrofit 23 候補であった。本軸は corpus 15 件のうち三種菩提心の総説（m506）と三門の核心句（m507 行願・m510 勝義・m516 三摩地）の 4 件を採り、残 10 件は三門の敷衍・引証として温存した。retrofit 20 声字実相義（4 of 12）・retrofit 21 即身成仏義（5 of 16）と同型の、単一典籍の骨格を採り敷衍を温存する教学系軸の構成。

#### 5. 三句法門 sg07 と三種菩提心 sg22 の並立・thematic adjacency と連動タグ overlap の区別

三句法門 sg07 が『大日経』住心品の教学的三句（菩提心因・大悲根・方便究竟）を密教修行の総綱として説くのに対し、本軸 sg22 はその因たる菩提心そのものを行願・勝義・三摩地の三種に開いて行者が現に発し護持すべき具体相を説く。両軸は密教の菩提心論のうちに、修行の総綱（sg07）と発菩提心の三門（sg22）として並立する。Phase A において、菩提心論 m515 が『大毘盧遮那経』の三句法門を引く motif であり sg07 と主題的に隣接（thematic adjacency）するが、本軸（三種菩提心）とは別系統のため温存した。retrofit 21 補注 U・retrofit 22 補注 V で確立した「thematic adjacency と連動タグ overlap を区別する」方針の再運用例。

#### 6. 5 motif 規模・小規模 retrofit

anchor 2 ＋ 強連動 3 ＝ 5 motif は retrofit 20 声字実相（4 motif）・retrofit 21 即身成仏義（5 motif）と同等の小規模 retrofit。三種菩提心の総説と行願・勝義・三摩地の三門に絞り、敷衍・引証を温存することで自然に小規模化した。retrofit 22 浄菩提心（8 motif）が単一軸 retrofit の最大規模であったのに対し、本 retrofit は中規模・小規模の系統に戻る。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=766  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg22軸 5motif×3 全付与  OK
7. sg list sg01-sg22 continuous, tail=sg22  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK

[stats（retrofit 23 後）]
total_motifs=766  famous_phrases=22
kakikudashi_chars_total=112,833
gendaigoyaku_chars_total=321,021
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=81 entries
file size=2,670,386 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 24〔教学系軸の継続〕

- **般若心経秘鍵軸**：hannya-hiken corpus 15 件中 12 件 clean（m494 sg11・m499/m500 sg02 が overlap）。中心成句候補（m492 仏法不外求・m496 大心真言三摩地法門・m501 真言不思議）はいずれも kakikudashi 直接含有が 1 件のみで成句性が弱く、中心成句の再検討を要する。
- **吽字義軸**：ujiji corpus 18 件中 12 件 clean（m549/m551/m552/m553 が sg08・m565 が sg07）。「吽」literal の kakikudashi 直接含有 2 件で中心成句が不明瞭。字相・字義あるいは吽字 四字（阿・訶・汙・麼）の構造を成句として再検討する余地がある。sg08 阿字本不生 anchor m549 が吽字義 corpus 内に居住するため重複の整理が要。
- **三教指帰 等の未軸化 corpus**：三教指帰（sankyo-shiki 21 件・retrofit 4 で発言者軸を運用済）は独立連動軸が未設置。大日経疏 巻第一 corpus は 68 件中 26 件が連動タグ保有・42 件が未連動であり、外道破斥（m741-m744）等の他主題の軸化余地が残るが、いずれも中心成句が不明瞭。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸十八系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg22 三種菩提心（菩提心論）は菩提心論・発心・密教実践論を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔十七系統 書き下し anchor 全件 OK〕

retrofit 21 §(d-1)・retrofit 22 §(d-1) の指示に従い、retrofit 23 着手時に連動軸十七系統（sg02/sg03/sg07-sg21）の書き下し anchor 自己参照タグ全件検証を実施した結果、全 22 motif（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728）が「連動:sgNN」「連動:m(anchor)」を保有していることを確認した（補整不要）。なお sg 成句 motif 自身（sg02/sg03/sg07-sg21）は十七系統すべて一律に連動タグ未保有であるが、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりであり、過去 retrofit の anchor 自己参照タグ検証も書き下し anchor の mNNN を対象としてきた（retrofit 21 の sg03 補整も anchor m533 に対するもの）。defect ではなく十七系統一律の設計仕様。retrofit 23 で追加した sg22 二重 anchor m506・m581 も「連動:sg22」「連動:m506」「連動:m581」を保有し、連動軸十八系統 書き下し anchor の自己参照タグは完全整合を維持する。今後 anchor を扱う retrofit でも着手時の書き下し anchor 自己参照タグ全件検証を継続する。

### (d-2) 菩提心論軸と三句法門 sg07 の隣接

三種菩提心は三句法門 sg07（菩提心因・大悲根・方便究竟）と主題的に隣接する。retrofit 23 Phase A の実測で、菩提心論 corpus（bodaishinron 15 件）は全件が連動タグ未保有の完全 clean であることを確認した。菩提心論 m515 は『大毘盧遮那経』の三句法門を引く motif で sg07 と主題的に隣接するが、本軸（三種菩提心＝行願・勝義・三摩地）とは別系統のため温存した。retrofit 21 §(d-3) の「thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する」方針の再運用例。なお m515 は三句法門「菩提を因となし大悲を根となし方便を究竟となす」を kakikudashi に直接含有する clean motif であり、retrofit 6 sg07 軸（補注 F・対象 7 motif）には含まれていない。将来 retrofit で sg07 連動の補整を検討する余地がある（菩提心論 corpus 内の三句法門 引証）。

### (d-3) m520 と即身成仏 sg03 の偈の同一性

菩提心論 第五節 m520「もし人、仏慧を求めて菩提心に通達すれば、父母所生の身に速やかに大覚位を証す」は、即身成仏 sg03 の anchor m533（即身成仏義 第一節・「もし人仏慧を求めて、菩提心に通達すれば、父母所生の身に、速に大覚の位を証す」）と同一の偈（金剛頂経の偈）を含む。m520 は本 retrofit 23 では即身成仏 結頌の別系統として温存したが、現状 m520 は連動タグ未保有であり、即身成仏 sg03 連動の補整余地がある。将来 retrofit で m520 への「連動:sg03」「連動:m533」補整を検討（菩提心論 corpus 内の即身成仏 経偈）。

### (d-4) 大日経疏 巻第一 corpus のカバー範囲

retrofit 23 着手時点で大日経疏 巻第一 corpus（dainichikyo-sho-vol1 68 件）は 26 件が連動タグ保有・42 件が未連動である。retrofit 23 は菩提心論 corpus を扱ったため大日経疏 corpus には変更なし。retrofit 22 §(d-3) 同様、大日経疏 巻第一の他主題（如実知自心は 4 件すべて既存軸 overlap・外道破斥 m741-m744・序分会衆段 等）の軸化余地は残るが、いずれも中心成句が不明瞭であり Phase A で基準未達と判定済。

### (d-5) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg22 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-23 で sg08-sg22 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-23 一貫して未更新の pre-existing 事象。retrofit 23 でも踏襲し未変更とした。将来 "sg01-sg22" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-6) 編集手法・truncate 事象回避

retrofit 23 のビルドスクリプト（`outputs/retrofit23_sanshu_bodaishin.py`）・Phase A スキャンスクリプト（`outputs/retrofit23_phaseA_scan.py`・`retrofit23_phaseA_scan2.py`・`retrofit23_phaseA_scan3.py`）・検証スクリプト（`outputs/retrofit23_verify.py`）・補注 W 追加スクリプト（`outputs/add_chunote_w_retrofit23.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit23.py`）・commit_message.txt・本 handoff はすべて bash heredoc 方式で作成し、Edit/Write tool の truncate 事象を回避した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（dry-run + 本番適用の二段運用）。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。今後もスクリプト・長文ファイルの作成は bash heredoc / Python write_bytes を第一選択とすることを推奨。

### (d-7) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-22 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。git status 等の実行後は `.git/index.lock` 残留に留意し、残留した場合は commit_push.bat 実行前に除去する（retrofit 22 §(d-4)）。

### (d-8) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 23 後で 全角〔/〕1065/1065 balanced。retrofit 23 の追加部分（タイトル行・最終更新行の retrofit 23 エントリ）は〔〕14 対・かぎ括弧 7 対・二重かぎ 2 対・全角丸括弧 2 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5)・retrofit 19 §(d-7)・retrofit 20 §(d-7)・retrofit 21 §(d-7)・retrofit 22 §(d-8) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔766 件・m1-m744 + sg01-sg22・2,670,386 bytes・schema_history 81 件〕
- 本 retrofit build script：`outputs/retrofit23_sanshu_bodaishin.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit23_phaseA_scan.py`・`retrofit23_phaseA_scan2.py`・`retrofit23_phaseA_scan3.py`
- Phase A 結果まとめ：`outputs/retrofit23_phaseA_out1.txt`・`retrofit23_phaseA_out2.txt`・`retrofit23_phaseA_out3.txt`
- 整合性検証 script：`outputs/retrofit23_verify.py`
- 補注 W 追加 script：`outputs/add_chunote_w_retrofit23.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit23.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit23.json`〔retrofit 前 motifs.json・2,664,294 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit23.md`〔retrofit 前・231,348 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit23.md`〔retrofit 前・324,423 bytes〕
  - `outputs/commit_message_backup_pre_retrofit23.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-22_retrofit22_complete.md`〔大日経疏 vol1 浄菩提心 教学系軸連動〕
- 補注 W 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 23 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-22 完走 → 2026-05-22 retrofit 23 完走〔菩提心論 三種菩提心 教学系軸連動・新規 sg22「三種菩提心」+ 二重 anchor 系統対比型 m506+m581 採用（菩提心論 第一節 本文 + 弁顕密二教論 巻上 第二章 第二節 引証）・強連動 3 件（m507/m510/m516）・連動軸十八系統並立に到達・教学系軸の第六例・二重 anchor 系統対比型 第六例〕。本体 motifs.json は 766 件・2,670,386 bytes・schema_history 81 件。motifs_index_design.md §2 に補注 W 追加〔補注 A-W 全 23 件 intact・247,628 bytes〕。CLAUDE.md は 330,354 bytes〔retrofit 4-23 全エントリ intact〕。連動軸十八系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）〕の書き下し anchor 自己参照タグ運用が完全整合。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit23_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit22_complete.md`〔retrofit 22 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-W 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・766 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 23 commit です。

【本セッションの選択肢】
(A) retrofit 24 候補〔教学系軸：般若心経秘鍵軸（中心成句要再検討）／吽字義軸（中心成句要再検討）／三教指帰 等の未軸化 corpus・大日経疏 巻第一 残 42 件の他主題軸化〕
(B) kaimyo-app 教学系素材活用：連動軸十八系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- git status 等の実行後は .git/index.lock 残留に留意〔残留時は commit_push.bat 実行前に除去・retrofit 22 §(d-4)〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)・retrofit 22-23 で再運用〕
- anchor を扱う retrofit では着手時に書き下し anchor 自己参照タグ全件検証を行う〔retrofit 21 §(d-1)・retrofit 23 で全件 OK 確認〕
- sg 成句 motif 自身は連動タグ未保有（成句は連動の参照先であり連動 motif プールの成員ではない・十八系統一律の設計仕様・retrofit 23 §(d-1)）
- 単独 anchor 体制（補注 J/N/P/R/S/T/U 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q/V/W 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-22〔retrofit 23 完走・菩提心論 三種菩提心 教学系軸連動 retrofit。新規 sg-id `sg22`「三種菩提心」を新設〔出典:菩提心論〕、書き下し anchor として二重 anchor 系統対比型 m506+m581 を採用（m506 菩提心論 第一節「諸仏菩薩、昔は因地にあって、この心を発しおわり、勝義・行願・三摩地を戒となす……ただ真言法の中にのみ即身成仏するが故に、これ三摩地の法を説くなり」三種菩提心を戒とする総説／m581 弁顕密二教論 巻上 第二章 第二節（十）引証「『金剛頂発菩提心論』にいわく……勝義・行願・三摩地を戒となす」菩提心論を引く引証）。強連動 3 motif：m507（菩提心論 第二節 行願菩提心）/ m510（第三節 勝義菩提心）/ m516（第四節 三摩地菩提心 月輪観）に「連動:sg22」「連動:m506」「連動:m581」を付与（+15 タグ）。total_motifs 765→766（+1 新規 sg22）・famous_phrases 21→22。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,670,386 bytes〔+6,092〕・schema_history 81 件〔+1・origin: retrofit_23:doctrine〕・補注 W 追加〔motifs_index_design.md §2・231,348→247,628 bytes・+16,280〕・CLAUDE.md 更新完了〔324,423→330,354 bytes〕・commit_message.txt 書き換え済。連動軸十八系統並立に到達。教学系軸（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心）に続く教学系軸の第六例で、龍猛菩薩造『菩提心論』の密教菩提心論を主題とする軸。二重 anchor 体制 系統対比型の運用第六例（retrofit 11/13/15/17/22 に続く）。同一文「勝義・行願・三摩地を戒となす」を菩提心論 本文 m506 と弁顕密二教論 引証 m581 の二系統で保持し、本文系統 anchor と引証系統 anchor を対比する初例。三句法門 sg07（密教修行の総綱）と三種菩提心 sg22（発菩提心の三門）が密教菩提心論のうちに並立。anchor 2 ＋ 強連動 3 ＝ 5 motif の小規模 retrofit。Phase D 必須チェックリストに完全準拠する第十五の retrofit〕

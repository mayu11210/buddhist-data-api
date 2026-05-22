# 引き継ぎメモ：retrofit 21 完走〔即身成仏義 二頌八句 教学系軸連動 retrofit〕

**日付**：2026-05-22
**フェーズ**：retrofit 21（retrofit 20 完走に続く第十八の retrofit セッション）
**対象**：空海の即身成仏論＝密教成仏論の根幹「即身成仏義 二頌八句」の連動軸新設。新規 sg-id `sg20`「六大無礙」を追加し、書き下し anchor として既存 m534（即身成仏義 第二節・二頌八句 即身頌「六大無礙にして常に瑜伽なり、四種曼荼各々離れず、三密加持すれば速疾に顕わる、重々帝網なるを即身と名づく」即身の二字を釈し六大四曼三密の三大によって即身成仏を論証する根本宣言）を **単独採用**。強連動 4 motif（m535 第二節 成仏頌 / m537 第三節 六大段 / m539 第四節 四曼段 / m540 第五節 三密段）に連動タグを付与。あわせて Phase A で発見した sg03 即身成仏 anchor m533 の自己参照タグ欠落を補整。連動軸十六系統並立に到達。本 retrofit は retrofit 20 声字実相 に続く **教学系軸の第四例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相 同型の **単独 anchor 体制の運用第六例**。anchor 1 ＋ 強連動 4 ＝ 5 motif の **小規模 retrofit 第六例**。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 5 motif 判定＋sg03 補整・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 U 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 22 候補〔教学系軸：大日経疏 vol1 浄菩提心軸（retrofit 21 Phase A 次点）／吽字義軸（中心成句要再検討）／菩提心論 等〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_21:doctrine〕
- [x] motifs_index_design.md に補注 U 追加済〔補注 A-U 全 21 件 intact・200,245→215,343 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・304,043→313,778 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 21 用・冒頭行整合確認済〕
- [x] handoff_2026-05-22_retrofit21_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 20 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 20 完走〔声字実相 教学系軸連動・新規 sg19 + 既存 m525 を書き下し anchor 単独採用・commit `30595db`〕に続く第十八の retrofit セッション。

retrofit 20 完走 handoff §(c) 選択肢 A〔retrofit 21 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で即身成仏義 二頌八句軸（六大四曼三密軸）を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg20`「六大無礙」を追加〔出典:即身成仏義・六大四曼三密の三大によって凡夫の即身成仏を論証する密教成仏論の中心成句・即身成仏義 二頌八句 即身頌の冒頭句〕
- 書き下し anchor は m534 単独（即身成仏義 第二節・二頌八句 即身頌「六大無礙にして常に瑜伽なり、四種曼荼各々離れず、三密加持すれば速疾に顕わる、重々帝網なるを即身と名づく」）
- 強連動 4 motif（m535 第二節 成仏頌 / m537 第三節 六大段 / m539 第四節 四曼段 / m540 第五節 三密段）に「連動:sg20」「連動:m534」を付与（+10 タグ）
- 副次：sg03 即身成仏 anchor m533 に自己参照タグ「連動:sg03」「連動:m533」を補整（+2 タグ）
- 連動軸十六系統並立に到達
- **教学系軸の第四例**（retrofit 20 声字実相 に続く・声字実相が言語哲学を主題とするのに対し即身成仏義 二頌八句は即身成仏論・密教成仏論を主題とする）
- **単独 anchor 体制の運用第六例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相 に続く）
- **小規模 retrofit の第六例**（5 motif・retrofit 14/18/19/20 に近い小規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 20 完走 handoff §(c) 選択肢 A に着手。Phase A スキャンで retrofit 21 候補三件（大日経疏 vol1 浄菩提心軸／即身成仏義 六大四曼三密軸／吽字義軸）の中心成句の kakikudashi 直接含有を全 763 motif にわたり網羅検査：

| 候補 | kakikudashi 支持 | 既存軸重複 | 判定 |
|---|---|---|---|
| 即身成仏義 六大四曼三密軸 | 二頌八句 即身頌の「六大無礙」「四種曼荼」「三密加持」「重々帝網」の 4 語が m534 単一 motif に集約 | 即身成仏義 16 件中 連動タグ有りは m536（sg08）のみ・sg03 連動タグ重複ゼロ | 採用 |
| 大日経疏 vol1 浄菩提心軸 | 「浄菩提心」14 件中 12 件が大日経疏 巻第一に集中 | 12 件中 6 件 clean（m718/m725/m728/m732/m735/m739）・6 件 overlap（sg07×4・sg03×2・sg15×1） | 次点・retrofit 22 以降に温存 |
| 吽字義軸 | 「吽字」literal kakikudashi 直接含有 0 件・字相3件/字義2件は 3 corpus に拡散 | 18 件中 5 件が既存軸連動・sg08 anchor m549 が吽字義 corpus 内に居住 | 基準未達・retrofit 22 以降に温存 |

retrofit 20 Phase A では即身成仏義 六大四曼三密軸は「m534 が sg03 anchor m533 と同一二頌八句を分割・sg03 と重複」として見送られたが、retrofit 21 Phase A スキャンの実測で sg03 即身成仏 の連動 motif（m724/m729/m733/m740）はすべて大日経疏 巻第一に所在し、即身成仏義 corpus とは連動タグが一切重複しないこと、sg03 anchor m533（金剛頂経の経偈）と本軸 anchor m534（空海の論証頌）は経証 対 論証として主題が判然と分離することを確認。ケンシン裁定で判断 1-5：

- **判断 1**：軸採用 = 候補2 即身成仏義 六大四曼三密軸（連動タグ overlap ゼロ・sg03 と経証 対 論証で主題明確分離）
- **判断 2**：中心成句 sg20 =「六大無礙」（即身成仏義 二頌八句 即身頌の冒頭句・出典:即身成仏義。sg19「五大皆有響」が声字実相義 四句頌の冒頭句であったのと同型）
- **判断 3**：書き下し anchor = m534 単独採用（即身成仏義 第二節 即身頌・単独 anchor 体制・retrofit 14/16/18/19/20 同型 第六例。m534 と m535 は同一典籍同一節であり系統対比型の二重 anchor には当たらず、軸名「六大四曼三密」が m534 の内容に対応するため単独 anchor が自然形）
- **判断 4**：規模 = anchor 1 ＋ 強連動 4 ＝ 5 motif（即身成仏義 第二〜第五節・小規模）。強連動 4 件 = m535（成仏頌）/ m537（六大段）/ m539（四曼段）/ m540（三密段）
- **判断 5**：副次発見 sg03 anchor m533 の自己参照タグ欠落（15 軸 anchor 中 sg03 のみ）を retrofit 21 で併せて補整

### Phase B：5 motif 判定表 + sg03 補整

| m-id | 出典 | 役割 |
|---|---|---|
| m534 | 即身成仏義 第二節 | 書き下し anchor（単独・自己参照）・「六大無礙にして常に瑜伽なり、四種曼荼各々離れず、三密加持すれば速疾に顕わる、重々帝網なるを即身と名づく」即身の二字を釈し六大四曼三密の三大に集約する二頌八句の即身頌・即身成仏論の根本宣言 |
| m535 | 即身成仏義 第二節 | 強連動・「法然に薩般若を具足して、心数心王刹塵に過ぎたり、各々五智無際智を具す、円鏡力の故に実覚智なり」二頌八句のうち成仏の二字を釈する成仏頌 |
| m537 | 即身成仏義 第三節 | 強連動・「かくのごとくの六大能く一切の仏および一切衆生器界等の四種法身と三種世間とを造す」六大が四種法身と三種世間を造すことを説く六大段の核心句 |
| m539 | 即身成仏義 第四節 | 強連動・「かくのごときの四種曼荼羅・四種智印その数無量なり。一一の量虚空に同じ……」四種曼荼羅・四種智印が無量にして相互不離であることを説く四曼段の核心句 |
| m540 | 即身成仏義 第五節 | 強連動・「三密とは一には身密、二には語密、三には心密なり。法仏の三密は甚深微細にして……」身密・語密・心密の三密を定義する三密段の核心句 |
| m533 | 即身成仏義 第一節 | sg03 即身成仏 anchor・自己参照タグ補整対象（「連動:sg03」「連動:m533」を付与） |

体系内連節カバー：即身頌（m534 第二節 anchor）→ 成仏頌（m535 第二節）→ 六大段（m537 第三節）→ 四曼段（m539 第四節）→ 三密段（m540 第五節）の即身成仏義 第二〜第五節を一括包摂。二頌八句（即身頌＋成仏頌）の完結と、六大・四曼・三密の三大各段を連動軸として明示化。

**除外・温存**：即身成仏義 第一節 経偈 m533 は即身成仏 sg03 の anchor であり別系統（経証 対 論証）のため本軸 anchor とはしない。第三節 m536（「我れ本不生を覚り……」）は retrofit 8 で阿字本不生 sg08/m549 連動済のため sg08 単独連動のまま温存。第六〜第九節（m543-m548 重重帝網・三無差別・本来寂静・五智・円鏡智）は二頌八句の敷衍・後論であり「主題:即身成仏」等のタグ保持により別途検索可能なため温存。本軸 5 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない（retrofit 20 で m524 が sg08/sg19 二系統連動となったのとは異なる）。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 763 | 764 | +1（sg20 新規追加） |
| famous_phrases | 19 | 20 | +1 |
| ファイルサイズ | 2,650,402 bytes | 2,656,569 bytes | +6,167 |
| schema_history | 78 | 79 | +1（origin: retrofit_21:doctrine） |
| 連動タグ総数 | — | — | +12（sg20 軸 5 motif × 2 ＝ 10 / sg03 補整 m533 × 2 ＝ 2） |
| kakikudashi_chars_total | 112,820 | 112,824 | +4（「六大無礙」4 字） |
| gendaigoyaku_chars_total | 316,018 | 317,501 | +1,483（sg20 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 764 vs 764 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg20 軸 5 motif × 2 + m533 × 2〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg20 連番・末尾 sg20 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 20 で recompute した stats は retrofit 21 着手時点で全 5 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 21 では stats を全件 recompute して真値を書き込み（total_motifs 764・famous_phrases 20・kakikudashi_chars_total 112,824・gendaigoyaku_chars_total 317,501・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。top-level generated_at は 2026-05-22T00:00:00+09:00 を維持。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 U 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 U〔即身成仏義 二頌八句 教学系軸連動の運用〕新規追加（200,245→215,343 bytes・+15,098・補注 A-U 全 21 件 intact・全角丸括弧 89/89 balanced・〔〕20/20 balanced・かぎ括弧 43/43 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 21 完走エントリを追加（304,043→313,778 bytes・retrofit 4-21 全エントリ intact・追加部分の全角角括弧 37/37・かぎ括弧 12/12 balanced・新規半角括弧 0 件・全角〔〕全体 957/957 balanced）。
- `commit_message.txt` を retrofit 21 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-22_retrofit21_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第四例・空海 三部書の即身成仏論軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学＝密教言語論を主題とする教学系軸であった。retrofit 21 即身成仏義 二頌八句軸はその継続でありながら、六大四曼三密の三大によって凡夫の即身成仏を論証する空海の即身成仏論・密教成仏論を主題とする点に特色をもつため、教学系軸の第四例と位置づける。即身成仏義 は声字実相義（sg19）・吽字義 と並ぶ空海 三部書の一であり、本 retrofit により三部書のうち即身成仏義・声字実相義 の二著作が論の本体（即身成仏義 二頌八句／声字実相義 四句頌）を anchor とする連動軸をもつに至った。

#### 2. 連動軸十六系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）〕の十六系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）に加えて、即身成仏論・密教成仏論（六大四曼三密）でも素材プールを切替可能。

#### 3. 同一典籍内の経証軸と論証軸の並立

即身成仏 sg03 が即身成仏義 第一節の経偈「父母所生の身に、速に大覚の位を証す」（金剛頂経の偈・即身成仏の経証）を anchor とするのに対し、本軸 sg20 は即身成仏義 第二節以降の二頌八句（空海自身による即身成仏の論証頌）を anchor とする。同一典籍『即身成仏義』のうちに経証軸（sg03）と論証軸（sg20）が並立する。秘蔵宝鑰 が諸法実相 sg09・十住心 sg17 の二軸 anchor を擁するのに続く「同一典籍 二軸」の事例だが、即身成仏義 の場合は経証 対 論証という典籍内部の論述構造の対比をなす点に特色がある。

#### 4. 単独 anchor 体制の運用第六例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599・retrofit 19 顕密二教 sg18/m571・retrofit 20 声字実相 sg19/m525 に続く第六の単独 anchor 体制。即身成仏義 二頌八句の核心は m534 の即身頌に集約され、成仏頌 m535 は強連動として位置づくため、典籍系統対比型の二重 anchor を要さず単独 anchor が自然形となる。

#### 5. anchor 自己参照タグの完全整合

retrofit 21 Phase A の anchor 自己参照タグ全件検証で、連動軸（sg20 追加前の十五系統）の anchor のうち即身成仏 sg03 anchor m533 のみ自己参照タグ「連動:sg03」「連動:m533」を欠落していることが判明した。sg03 は連動軸最初期（retrofit 5）の軸であり、retrofit 9 の anchor 自己参照タグ運用導入時に補整されないまま残存した pre-existing 事象である。本 retrofit でこれを補整し、連動軸十六系統の anchor すべてが自己参照タグを保有する完全整合状態に到達した。

#### 6. 小規模 retrofit の第六例

anchor 1 ＋ 強連動 4 ＝ 5 motif は retrofit 14 多宝塔・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相（各 4 motif）に近い小規模。即身成仏義 二頌八句（第二節）と六大・四曼・三密の三段（第三〜第五節）に絞り、第一節 経偈（sg03 領域）・第六〜第九節 後論を温存することで自然に小規模化した。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=764  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg20軸5motif×2 + m533×2 全付与  OK
7. sg list sg01-sg20 continuous, tail=sg20  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK

[stats（retrofit 21 後）]
total_motifs=764  famous_phrases=20
kakikudashi_chars_total=112,824
gendaigoyaku_chars_total=317,501
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=79 entries
file size=2,656,569 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 22〔教学系軸の継続〕

- **大日経疏 vol1 浄菩提心軸**：retrofit 21 Phase A の次点。「浄菩提心」12 件が大日経疏 巻第一に集中し kakikudashi 支持は強い。12 件中 clean 6 件（m718/m725/m728/m732/m735/m739）で軸構成は可能だが、定義頌の最有力 m716 が sg07 三句法門 占有のため anchor 選定に設計上の工夫を要す。
- **吽字義軸**：「吽字」literal の kakikudashi 直接含有 0 件で中心成句が不明瞭。字相・字義あるいは吽字 四字（阿・訶・汙・麼）の構造を成句として再検討する余地がある。sg08 阿字本不生 anchor m549 が吽字義 corpus 内に居住するため重複の整理が要。
- **菩提心論 三摩地戒 等**：retrofit 20 で基準未達と判定済。再検討の余地は小さい。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸十六系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg20 六大無礙（即身成仏義 二頌八句）は即身成仏論・密教成仏論・本来性論を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) sg03 anchor 自己参照タグ欠落の補整

retrofit 21 Phase A で、連動軸 anchor の自己参照タグ全件検証を実施した結果、即身成仏 sg03 anchor m533 のみ「連動:sg03」「連動:m533」を欠落していることが判明した。retrofit 20 handoff §概要の「anchor 自己参照タグ運用が完全整合に到達」の記述は、この sg03 の欠落を見落としていた。sg03 は連動軸最初期（retrofit 5）の軸であり、retrofit 9 の anchor 自己参照タグ運用導入時に補整されなかった pre-existing 事象。本 retrofit 21 でケンシン裁定により m533 に「連動:sg03」「連動:m533」を補整し、十六系統 anchor の自己参照タグを完全整合とした。今後 anchor を扱う retrofit では着手時に自己参照タグ全件検証を行うことを推奨。

### (d-2) 即身成仏義 の連動軸カバー範囲

本 retrofit は即身成仏義 第二〜第五節（m534/m535/m537/m539/m540）を連動軸化した。第一節 経偈 m533 は sg03 anchor（経証軸）、第三節 m536 は sg08 阿字本不生 連動済のため別系統として温存。第六〜第九節（m543-m548 重重帝網・三無差別・本来寂静・五智・円鏡智）は二頌八句の敷衍・後論であり「主題:即身成仏」タグ保持により別途検索可能なため温存した。将来 retrofit で即身成仏義 後半（第六〜第九節）を連動軸に拡張する余地は残る。

### (d-3) retrofit 20 Phase A の見送り判定の再検討

即身成仏義 六大四曼三密軸は retrofit 20 Phase A で「m534 が sg03 anchor m533 と同一二頌八句を分割・sg03 と重複」として見送られた。retrofit 21 Phase A の全件スキャンの実測では、sg03 即身成仏 の連動 motif（m724/m729/m733/m740）はすべて大日経疏 巻第一に所在し即身成仏義 corpus とは連動タグが一切重複しないこと、sg03 anchor m533 と本軸 anchor m534 は同一典籍ながら経証 対 論証として主題が判然と分離することを確認し、採用に至った。候補スキャンは連動タグの実測（thematic adjacency と連動タグ overlap を区別）に基づいて判定すべきという教訓。

### (d-4) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg20 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-21 で sg08-sg20 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-21 一貫して未更新の pre-existing 事象。retrofit 21 でも踏襲し未変更とした。将来 "sg01-sg20" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-5) 編集手法・truncate 事象回避

retrofit 21 のビルドスクリプト（`outputs/retrofit21_sokushin_jobutsu.py`）・Phase A スキャンスクリプト（`outputs/retrofit21_phaseA_scan.py`・`retrofit21_phaseA_scan2.py`）・補注 U 追加スクリプト（`outputs/add_chunote_u_retrofit21.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit21.py`）・commit_message.txt・本 handoff はすべて bash heredoc 方式で作成し、Edit/Write tool の truncate 事象を回避した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（dry-run + 本番適用の二段運用）。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。今後もスクリプト・長文ファイルの作成は bash heredoc / Python write_bytes を第一選択とすることを推奨。

### (d-6) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-20 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。

### (d-7) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 21 後で 全角〔/〕957/957 balanced。retrofit 21 の追加部分は全角角括弧 37 対・かぎ括弧 12 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5)・retrofit 19 §(d-7)・retrofit 20 §(d-7) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔764 件・m1-m744 + sg01-sg20・2,656,569 bytes・schema_history 79 件〕
- 本 retrofit build script：`outputs/retrofit21_sokushin_jobutsu.py`〔dry-run + 本番適用の二段運用〕
- Phase A スキャン script：`outputs/retrofit21_phaseA_scan.py`・`outputs/retrofit21_phaseA_scan2.py`
- Phase A 結果まとめ：`outputs/retrofit21_phaseA_candidates.txt`
- 補注 U 追加 script：`outputs/add_chunote_u_retrofit21.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit21.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit21.json`〔retrofit 前 motifs.json・2,650,402 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit21.md`〔retrofit 前・200,245 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit21.md`〔retrofit 前・304,043 bytes〕
  - `outputs/commit_message_backup_pre_retrofit21.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-22_retrofit20_complete.md`〔声字実相 教学系軸連動〕
- 補注 U 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 21 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-20 完走 → 2026-05-22 retrofit 21 完走〔即身成仏義 二頌八句 教学系軸連動・新規 sg20「六大無礙」+ 既存 m534 を書き下し anchor 単独採用・強連動 4 件（m535/m537/m539/m540）・sg03 anchor 自己参照タグ補整・連動軸十六系統並立に到達・教学系軸の第四例・単独 anchor 体制 第六例〕。本体 motifs.json は 764 件・2,656,569 bytes・schema_history 79 件。motifs_index_design.md §2 に補注 U 追加〔補注 A-U 全 21 件 intact・215,343 bytes〕。CLAUDE.md は 313,778 bytes〔retrofit 4-21 全エントリ intact〕。連動軸十六系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）〕の anchor 自己参照タグ運用が完全整合に到達（retrofit 21 で sg03 anchor m533 を補整）。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit21_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit20_complete.md`〔retrofit 20 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-U 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・764 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 21 commit です。

【本セッションの選択肢】
(A) retrofit 22 候補〔教学系軸：大日経疏 vol1 浄菩提心軸（retrofit 21 Phase A 次点・clean 6 件で軸構成可・要設計）／吽字義軸（中心成句要再検討）／菩提心論 等〕
(B) kaimyo-app 教学系素材活用：連動軸十六系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)〕
- anchor を扱う retrofit では着手時に anchor 自己参照タグ全件検証を行う〔retrofit 21 §(d-1)〕
- 単独 anchor 体制（補注 J/N/P/R/S/T/U 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-22〔retrofit 21 完走・即身成仏義 二頌八句 教学系軸連動 retrofit。新規 sg-id `sg20`「六大無礙」を新設〔出典:即身成仏義〕、書き下し anchor として既存 m534 を単独採用（即身成仏義 第二節・二頌八句 即身頌「六大無礙にして常に瑜伽なり、四種曼荼各々離れず、三密加持すれば速疾に顕わる、重々帝網なるを即身と名づく」）。強連動 4 motif：m535（第二節 成仏頌）/ m537（第三節 六大段）/ m539（第四節 四曼段）/ m540（第五節 三密段）に「連動:sg20」「連動:m534」を付与（+10 タグ）。副次：sg03 即身成仏 anchor m533 に自己参照タグ「連動:sg03」「連動:m533」を補整（+2 タグ）。計 +12 タグ。total_motifs 763→764（+1 新規 sg20）・famous_phrases 19→20。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,656,569 bytes〔+6,167〕・schema_history 79 件〔+1・origin: retrofit_21:doctrine〕・補注 U 追加〔motifs_index_design.md §2・200,245→215,343 bytes・+15,098〕・CLAUDE.md 更新完了〔304,043→313,778 bytes〕・commit_message.txt 書き換え済。連動軸十六系統並立に到達。教学系軸（retrofit 20 声字実相）に続く教学系軸の第四例で空海 三部書 即身成仏義 の即身成仏論軸。単独 anchor 体制の運用第六例。小規模 retrofit の第六例（5 motif）。同一典籍 即身成仏義 のうちに経証軸 sg03 と論証軸 sg20 が並立。sg03 anchor 自己参照タグ補整で十六系統 anchor 自己参照タグ完全整合に到達。即身成仏義 第六〜第九節（後論）を温存。Phase D 必須チェックリストに完全準拠する第十三の retrofit〕

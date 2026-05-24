# 引き継ぎメモ：retrofit 27 完走〔大日経疏 一切智智 教学系軸連動 retrofit〕

**日付**：2026-05-24
**フェーズ**：retrofit 27（retrofit 26 完走に続く第二十四の retrofit セッション）
**対象**：空海所依の根本聖典『大日経』の註釈書『大日経疏』巻第一が註釈する、『大日経』入真言門住心品の根本概念「一切智智」の連動軸新設。新規 sg-id `sg26`「一切智智」を追加し、書き下し anchor として **単独 anchor m698** を採用。m698（大日経疏 巻第一 §31 執金剛秘密主の問・「世尊よ、云何が如来応供正遍知は一切智智を得たり……云何が如来応供正遍知はこの一切智智を得たるやと」一切智智の獲得を因・根・究竟の三問とともに問い真言密教の教説をひらく住心品の根本問）を単独の書き下し anchor とする。強連動 5 motif（m705 §44 五喩総説 / m707 §46 地譬 / m708 §47 火譬 / m709 §48 風譬 / m710 §49 水譬）に連動タグを付与。連動軸二十二系統並立に到達。本 retrofit は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 に続く **教学系軸の第十例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 六大無礙・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 同型の **単独 anchor 体制の運用第十例**。anchor 1 ＋ 強連動 5 ＝ 6 motif の retrofit。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 6 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 AA 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 28 候補〔教学系軸：般若心経秘鍵 仏法不外求軸（m492/m493 clean・anchor＋強連動 2 motif の最小規模・規模再検討要）／三教指帰軸／大日経疏 巻第一 残 31 件のさらなる主題軸化〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_27:doctrine〕
- [x] motifs_index_design.md に補注 AA 追加済〔補注 A-Z＋AA 全 27 件 intact・301,708→322,130 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・346,139→351,696 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 27 用・冒頭行整合確認済〕
- [x] handoff_2026-05-24_retrofit27_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 26 recompute 済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 26 完走〔大日経疏 加持身 教学系軸連動・commit `b100303`〕に続く第二十四の retrofit セッション。

retrofit 26 完走 handoff §(c) 選択肢 A〔retrofit 27 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で大日経疏 一切智智軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg26`「一切智智」を追加〔出典:大日経疏・唐の善無畏三蔵の講説を一行阿闍梨が筆録した『大日経疏』巻第一が註釈する『大日経』入真言門住心品の根本概念〕
- 書き下し anchor は **単独 anchor m698**（大日経疏 巻第一 §31 執金剛秘密主の問）
- 強連動 5 motif（m705 §44 五喩総説 / m707 §46 地譬 / m708 §47 火譬 / m709 §48 風譬 / m710 §49 水譬）に「連動:sg26」「連動:m698」を付与（+12 タグ）
- 連動軸二十二系統並立に到達
- **教学系軸の第十例**（retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 に続く・一切智智は『大日経』入真言門住心品の根本概念を主題とする）
- **単独 anchor 体制の運用第十例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教・retrofit 20 声字実相・retrofit 21 六大無礙・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 に続く）
- **6 motif retrofit**（anchor 1 ＋ 強連動 5・retrofit 22 浄菩提心 8 motif に次ぐ規模で、retrofit 21・23・24・26 各 5 motif をやや上回る）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 26 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸二十一系統（sg02/sg03/sg07-sg25）の書き下し anchor がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg25）は二十一系統一律に連動タグ未保有であり、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりで整合。Phase A スキャンで retrofit 27 候補（般若心経秘鍵 仏法不外求軸／三教指帰軸／大日経疏 巻第一 残 37 件のさらなる主題軸化）の中心成句の kakikudashi 直接含有を全 769 motif にわたり網羅検査：

| 候補 | corpus clean 率 | kakikudashi 支持 | 判定 |
|---|---|---|---|
| 大日経疏 一切智智軸 | dainichikyo-sho-vol1 未連動 37/68 | 「一切智智」literal が clean 8 件（m678/m698/m701/m707/m708/m709/m710/m719）に集中・§44-§49 の五喩（m705 総説＋m707/m708/m709/m710）が「譬えば X 界は…如く、かくの如く一切智智は…」の構文で構造的に明瞭な clean クラスタをなす | 採用 |
| 般若心経秘鍵 仏法不外求軸 | hannya-hiken（本軸該当 2 件 clean） | thesis 句「仏法遥かに非ず／真如外に非ず」literal は m492 専属・強連動候補 m493 1 件のみで anchor＋強連動 2 motif の過去最小規模 | 基準未達・retrofit 28 以降に温存 |
| 三教指帰軸 | sankyo-shiki 21/21 完全 clean | 「三教」literal（m656/m670/m675/m676）すべて枠組み motif・連動軸モデルへの適合が弱い（retrofit 4 発言者軸運用済） | 基準未達・retrofit 28 以降に温存 |

retrofit 26 完走 handoff §(d-4) は大日経疏 巻第一 残 37 件について「中心成句が明瞭な軸候補が残るかは retrofit 27 以降の Phase A 候補語スキャン次第」と暫定評価していた。retrofit 27 Phase A で「一切智智」を中心成句として候補語を変えてスキャンした結果、未連動 37 件のうち clean 8 件が「一切智智」literal を直接含有し、とりわけ §44-§49 の五種の譬喩（虚空・地・水・火・風）が一切智智を illustrate する構造的に明瞭な clean クラスタをなすことを確認した。ケンシン裁定で判断 1-3：

- **判断 1**：軸採用 = 大日経疏 一切智智軸（dainichikyo-sho-vol1 corpus に正常規模の連動軸を成立させられる候補。仏法不外求軸は 2 motif で過去最小を下回り、三教指帰軸は連動軸モデルに不適合のため退けた）
- **判断 2**：中心成句 sg26 =「一切智智」（『大日経』入真言門住心品の根本概念で、『大日経疏』が品名を釈して「衆生の自心品は、すなわちこれ一切智智なり」と説く、一切智のなかの智、諸法を実のごとくに了知する仏のみの自証の智〔梵語サルヴァジュニャ・ジュニャーナ〕。m698 が「云何が如来応供正遍知はこの一切智智を得たるや」と literal kakikudashi 直接含有。「五種譬喩」案は anchor m705 が 2 文と薄く中心成句が構造ラベル寄りのため、「自心本性清浄」案は浄菩提心 sg21 と主題が重なるため退けた）
- **判断 3**：anchor 体制・規模 = 単独 anchor m698・6 motif（本軸の典籍は『大日経疏』巻第一の一系統のみで引証系統の対 anchor を欠くため、retrofit 22-23 の二重 anchor 系統対比型ではなく単独 anchor が自然形）

### Phase B：6 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m698 | 大日経疏 巻第一 §31 執金剛秘密主の問 | 書き下し anchor（単独・自己参照）・「世尊よ、云何が如来応供正遍知は一切智智を得たり……云何が如来応供正遍知はこの一切智智を得たるやと」一切智智の獲得を因・根・究竟の三問とともに問う住心品の根本問 |
| m705 | 大日経疏 巻第一 §44 五喩総説 | 強連動・「執金剛は仏の神力を承けて、大悲胎蔵の秘密方便を発起せんと欲するが為の故に、復た五種の譬喩を説く。謂ゆる虚空、地、水、火、風なり」一切智智を illustrate する五種の譬喩を総説する句 |
| m707 | 大日経疏 巻第一 §46 地譬 | 強連動・「譬えば大地は一切衆生の依たるが如く、かくの如く一切智智は、天、人、阿修羅の依たり」一切智智を一切衆生を養育する大地に喩える句 |
| m708 | 大日経疏 巻第一 §47 火譬 | 強連動・「譬えば火界は一切の薪を燒くに厭足あることなきが如く、かくの如く一切智智も一切無智の薪を燒くに厭足なし」一切智智を聖凡平等に無始の大夜を照らす智火に喩える句 |
| m709 | 大日経疏 巻第一 §48 風譬 | 強連動・「譬えば風界は一切の塵を除くが如く、この一切智智も一切の諸の煩悩の塵を除去す」一切智智を無明の大樹を摧壊する慧風に喩える句 |
| m710 | 大日経疏 巻第一 §49 水譬 | 強連動・「譬えば水界は一切衆生はこれによって歓楽するが如く、かくの如く一切智智は諸天世人の利楽をなす」一切智智を本性清潔にして群生を利潤する智水に喩える句 |

体系内連節カバー：一切智智の獲得を問う根本問（m698 §31）→ 一切智智を illustrate する五喩の総説（m705 §44）→ 地譬（m707 §46）→ 火譬（m708 §47）→ 風譬（m709 §48）→ 水譬（m710 §49）の大日経疏 巻第一 §31〜§49 を一括包摂。

**除外・温存**：dainichikyo-sho-vol1 corpus（68 件）のうち、五喩の一たる虚空譬 m706（§45）は retrofit 15 で sg14 三草二木 に連動済のため本軸から除外・温存。一切智智 literal を保有する clean の m678（§2 品名釈・「自心品＝一切智智」の定義・多主題 motif）・m701（§38-40 問の意・趣・性欲）・m719（§61 自心本性清浄）は一切智智軸と thematic に隣接するが、6 motif の正常規模を保つため本軸から除外して温存。三句法門 sg07・浄菩提心 sg21・加持身 sg25 連動済の motif 群も別系統のため温存。本軸 6 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 769 | 770 | +1（sg26 新規追加） |
| famous_phrases | 25 | 26 | +1 |
| ファイルサイズ | 2,687,746 bytes | 2,692,504 bytes | +4,758 |
| schema_history | 84 | 85 | +1（origin: retrofit_27:doctrine） |
| 連動タグ総数 | — | — | +12（sg26 軸 6 motif × 2） |
| kakikudashi_chars_total | 112,849 | 112,853 | +4（「一切智智」4 字） |
| gendaigoyaku_chars_total | 325,271 | 326,255 | +984（sg26 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 770 vs 770 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg26 軸 6 motif × 2〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg26 連番・末尾 sg26 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0, fp=0 ✓ |

retrofit 26 で recompute した stats は retrofit 27 着手時点で全 6 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 27 では stats を全件 recompute して真値を書き込み（total_motifs 770・famous_phrases 26・kakikudashi_chars_total 112,853・gendaigoyaku_chars_total 326,255・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。char 集計規則は「text フィールド値から改行（\n）を除いた文字数の総和」であり、retrofit 27 着手時の drift check でこの規則が stored 値と完全一致することを確認したうえで recompute した。motifs.json は `json.dumps(ensure_ascii=False, indent=2)`・末尾改行なしの round-trip 完全一致を事前確認のうえ編集（dry-run + 検証 + 本番適用の二段運用）。

### Phase D：補注 AA 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 AA〔大日経疏 一切智智 教学系軸連動の運用〕新規追加（301,708→322,130 bytes・+20,422・補注 A-Z＋AA 全 27 件 intact・補注 AA 内部の〔〕25/25・「」38/38・『』29/29・全角丸括弧 115/115 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 27 完走エントリを追加（346,139→351,696 bytes・retrofit 4-27 全エントリ intact・追加部分の〔〕13 対・「」5 対・『』3 対・全角丸括弧 1 対がいずれも balanced・新規半角括弧 0 件）。
- `commit_message.txt` を retrofit 27 用に書き換え（冒頭行整合確認済・15,523 bytes）。
- handoff_2026-05-24_retrofit27_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第十例・密教根本概念軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸は空海の教判を主題とする教学体系軸、retrofit 20 声字実相軸は空海の言語哲学、retrofit 21 即身成仏義 二頌八句軸は空海の即身成仏論、retrofit 22 浄菩提心軸は『大日経』『大日経疏』の菩提心論、retrofit 23 三種菩提心軸は龍猛菩薩造『菩提心論』の発菩提心論、retrofit 24 大心真言三摩地法門軸は空海撰『般若心経秘鍵』による『般若心経』の密教的読解、retrofit 25 吽字四字軸は空海撰『吽字義』による聖音「吽」一字の密教字義論、retrofit 26 加持身軸は『大日経疏』巻第一による大日如来の身の密教仏身論を主題とする教学系軸であった。retrofit 27 一切智智軸はその継続でありながら、『大日経疏』巻第一が註釈する『大日経』入真言門住心品の根本概念「一切智智」――仏のさとりの智慧そのもの――を主題とする点に特色をもつため、教学系軸の第十例と位置づける。加持身 sg25 が『大日経疏』巻第一における大日如来の身（仏の側）の論、浄菩提心 sg21 が同じ『大日経疏』巻第一における行者の菩提心（衆生の側）の論を軸とするのに対し、一切智智 sg26 は『大日経疏』巻第一が掲げる仏の自証の智そのものを軸とし、『大日経疏』巻第一のうちに仏身論（sg25）・菩提心論（sg21）・智論（sg26）として並立する。

#### 2. 連動軸二十二系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）、加持身 sg25/m679（単独）、一切智智 sg26/m698（単独）〕の二十二系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）・密教言語論（声字実相）・即身成仏論（六大四曼三密）・本来性論（浄菩提心）・発菩提心論（三種菩提心）・密教的心経読解（大心真言三摩地法門）・聖音の字義論（吽字四字）・密教仏身論（加持身）に加えて、一切智智・五喩（虚空地水火風）・仏の自証の智（一切智智）でも素材プールを切替可能。

#### 3. 単独 anchor 体制の運用第十例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599・retrofit 19 顕密二教 sg18/m571・retrofit 20 声字実相 sg19/m525・retrofit 21 六大無礙 sg20/m534・retrofit 24 大心真言三摩地法門 sg23/m496・retrofit 25 吽字四字 sg24/m564・retrofit 26 加持身 sg25/m679 に続く第十の単独 anchor 体制。本軸の典籍は『大日経疏』巻第一の一系統のみであり、引証系統の対 anchor を欠くため、典籍系統対比型の二重 anchor（retrofit 22 浄菩提心・retrofit 23 三種菩提心）を要さず単独 anchor が自然形となる。retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 に続いて単独 anchor 体制を継続する。

#### 4. anchor 直接含有による中心成句支持・問答の対をなす sg07 との並立

retrofit 27 一切智智 sg26 は、中心成句「一切智智」を anchor m698 が「云何が如来応供正遍知はこの一切智智を得たるや」と literal kakikudashi で直接含有し、一切智智の獲得を因・根・究竟の三問とともに問う住心品の根本問が anchor に明示される。retrofit 20 声字実相・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身 と同型の、中心成句が anchor に直接現れる教学系軸。なお m698 §31 の三問（因・根・究竟）に対する如来の答えが既存軸 三句法門 sg07（菩提心を因とし・大悲を根とし・方便を究竟とす）であり、一切智智 sg26 はその問の側を、三句法門 sg07 は答の側をなして、問答の対をなして並立する。

#### 5. handoff 暫定評価の Phase A 候補語スキャンによる更新

retrofit 26 完走 handoff §(d-4) は大日経疏 巻第一 残 37 件について「中心成句が明瞭な軸候補が残るかは retrofit 27 以降の Phase A 候補語スキャン次第」と暫定評価していた。retrofit 27 Phase A で「一切智智」を中心成句として候補語を変えてスキャンした結果、未連動 37 件中 clean 8 件が「一切智智」literal を直接含有し、§44-§49 の五喩が構造的に明瞭な clean クラスタをなして正常規模（6 motif）の連動軸を成立させられることが判明した。候補スキャンは中心成句の候補語を網羅的に変えてスキャンすべきという retrofit 20・retrofit 21・retrofit 26 完走 handoff の候補スキャン方針の実例となった。handoff の暫定評価は将来 retrofit の着手判断の出発点であって最終判定ではなく、Phase A では候補語を変えて再スキャンすることが重要である。

#### 6. thematic adjacency と連動タグ overlap の区別の再運用・大日経疏 corpus の既存軸 overlap への対応

dainichikyo-sho-vol1 corpus には三句法門 sg07・即身成仏 sg03・阿字本不生 sg08・三草二木 sg14・浄菩提心 sg21・加持身 sg25 等の既存軸 anchor・強連動 motif が居住し、一切智智を illustrate する五喩の一たる虚空譬 m706 が sg14 三草二木 に連動済である。本軸は一切智智の獲得を問う m698 を anchor とし、既に他軸に連動済の motif（虚空譬 m706 等）は本軸から除外して、五喩総説（m705）・地譬（m707）・火譬（m708）・風譬（m709）・水譬（m710）の clean motif で軸を構成した。これにより一切智智軸と既存軸の連動タグ overlap はゼロに保たれ、一切智智 sg26 は仏の自証の智の論を、三句法門 sg07 はその獲得の構造の論を、加持身 sg25 は大日如来の身の論を、それぞれ別系統の連動軸として並立させる。retrofit 21 補注 U・retrofit 22 補注 V・retrofit 23 補注 W・retrofit 24 補注 X・retrofit 25 補注 Y・retrofit 26 補注 Z の方針を踏襲。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=770  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ sg26軸 6motif×2 全付与  OK
7. sg list sg01-sg26 continuous, tail=sg26  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0 fp=0  OK
   anchor 自己参照タグ 連動軸二十二系統: ALL OK

[stats（retrofit 27 後）]
total_motifs=770  famous_phrases=26
kakikudashi_chars_total=112,853
gendaigoyaku_chars_total=326,255
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=85 entries
file size=2,692,504 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 28〔教学系軸の継続〕

- **般若心経秘鍵 仏法不外求軸**：般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす。ただし「仏法不外求」thesis 句の literal kakikudashi 直接含有は m492 専属で強連動 motif 群が m493 1 件にとどまり anchor＋強連動 2 motif の過去最小規模となるため、軸規模の再検討を要する（retrofit 25-27 Phase A の実測で他 corpus からの clean な引証 motif も得られないことを確認済・(d-2) 参照）。
- **三教指帰軸**：sankyo-shiki corpus 21 件は全件 clean だが、「三教」literal（m656/m670/m675/m676）はいずれも枠組み motif で、連動軸モデル（成句＋書き下し anchor＋強連動）への適合が弱い。retrofit 4 で発言者軸（亀毛先生／虚亡隠士／仮名乞児）を運用済（(d-3) 参照）。
- **大日経疏 巻第一 残 31 件のさらなる主題軸化**：retrofit 27 後、dainichikyo-sho-vol1 68 件のうち未連動は 31 件。一切智智軸（retrofit 27）・加持身軸（retrofit 26）・浄菩提心軸（retrofit 22）・三句法門軸（retrofit 6）等で主要テーマは軸化済。残 31 件は二十執金剛の列挙（m684/m685）・梵本諸名釈・外道破斥群（m737/m741/m742/m743/m744 等）・自心本性清浄（m719）等を含むが、中心成句が明瞭な軸候補が残るかは Phase A の候補語スキャン次第（(d-4) 参照）。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸二十二系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg26 一切智智（大日経疏）は一切智智・五喩（虚空地水火風）・仏の自証の智 を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔二十一系統 書き下し anchor 全件 OK・retrofit 27 後 二十二系統 完全整合〕

retrofit 21 §(d-1)・retrofit 26 §(d-1) の指示に従い、retrofit 27 着手時に連動軸二十一系統（sg02/sg03/sg07-sg25）の書き下し anchor 自己参照タグ全件検証を実施した結果、全 anchor（m630/m533/m713/m549/m637/m209/m636/m44/m70/m227/m569/m424/m215/m717/m639/m690/m599/m571/m525/m534/m638/m728/m506/m581/m496/m564/m679・m636 は sg10/sg14 共有）がすべて「連動:sgNN」「連動:m(anchor)」を保有していることを確認した（補整不要）。sg 成句 motif 自身（sg02/sg03/sg07-sg25）は二十一系統一律に連動タグ未保有であるが、これは「成句は連動の参照先であって連動 motif プールの成員ではない」という既存設計どおりであり、defect ではなく一律の設計仕様。retrofit 27 で追加した sg26 単独 anchor m698 も「連動:sg26」「連動:m698」を保有し、検証スクリプトで連動軸二十二系統 anchor の自己参照タグが ALL OK（完全整合）であることを確認した。今後 anchor を扱う retrofit でも着手時の書き下し anchor 自己参照タグ全件検証を継続する。

### (d-2) 般若心経秘鍵 仏法不外求軸の規模問題と温存

般若心経秘鍵 第二節の clean motif m492「仏法遥かに非ず、心中にして即ち近し。真如外に非ず、身を棄てて何くんか求めん」・m493「迷悟我に在れば、発心すれば即ち到る。明暗他に非ざれば、信修すれば忽ちに証す」は、本来性・即身内証を主題とする般若心経秘鍵のもう一つの中心成句候補「仏法不外求」をなす（m492 は既存「主題:仏法不外求」タグ保持）。retrofit 24-26 完走 handoff が独立軸候補として温存し、retrofit 27 Phase A スキャンの実測でも、「仏法不外求」thesis 句の literal kakikudashi 直接含有は m492 専属、強連動候補も m493 1 件にとどまり anchor m492 ＋ 強連動 m493 ＝ 2 motif と過去最小（retrofit 25 吽字四字 4 motif）を下回る規模となることを再確認した。本来性 theme を他 corpus に拡張してもクリーンな引証 motif は得られず（本来性 theme は多数の clean motif に拡散する thematic adjacency にとどまる）、強連動 motif 群の構造的拡大が困難である。連動軸として構造的に薄いため、retrofit 27 ではケンシン裁定で大日経疏 一切智智軸を採用し、仏法不外求軸は retrofit 28 以降に温存した。将来 retrofit で仏法不外求軸を採る場合、anchor＋強連動 2 motif の最小規模を許容するか否かの判断を要する。

### (d-3) 三教指帰軸の温存

sankyo-shiki corpus 21 件は全件 clean だが、「三教」literal（m656/m670/m675/m676）はいずれも儒道仏の枠組みを述べる枠組み motif であり、連動軸モデル（中心成句＋書き下し anchor＋強連動）への適合が弱い。三教指帰は retrofit 4 で発言者軸（亀毛先生／虚亡隠士／仮名乞児）を運用済であり、連動軸としての軸化は retrofit 28 以降に温存。

### (d-4) 大日経疏 巻第一 corpus のカバー範囲

retrofit 27 後、dainichikyo-sho-vol1 corpus（68 件）は 37 件が連動タグ保有（sg26 一切智智 6 件 m698/m705/m707/m708/m709/m710・sg25 加持身 5 件・sg07 三句法門 6 件・sg08 阿字本不生 4 件・sg21 浄菩提心 6 件・sg03 即身成仏 4 件・sg15 長者窮子 3 件・sg14 三草二木 2 件・sg12 化城宝処 1 件・sg13 多宝塔 1 件・sg16 従地涌出 1 件・一部 motif は多系統連動のため per-axis 合計は unique 37 を上回る）・31 件が未連動である。未連動 31 件は二十執金剛の列挙（m684/m685）・梵本諸名釈・大楼閣宝王・諸大菩薩列挙・自心本性清浄（m719）・外道破斥群（m737/m741/m742/m743/m744 等）・加持注処（m680）等を含む。一切智智 literal を保有する clean の m678（§2 品名釈）・m701（§38-40 問の意）・m719（§61 自心本性清浄）は一切智智軸と thematic に隣接するが本軸の正常規模を保つため温存した。中心成句が明瞭な軸候補が残るかは retrofit 28 以降の Phase A 候補語スキャン次第。

### (d-5) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg26 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-27 で sg08-sg26 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-27 一貫して未更新の pre-existing 事象。retrofit 27 でも踏襲し未変更とした。将来 "sg01-sg26" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-6) 編集手法・truncate 事象回避

retrofit 27 のビルドスクリプト（`outputs/retrofit27_issaichichi.py`）・Phase A スキャン（インライン Python）・検証スクリプト（`outputs/retrofit27_verify.py`）・補注 AA 追加スクリプト（`outputs/add_chunote_aa_retrofit27.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit27.py`）・補注 AA 本文（`outputs/chunote_aa_retrofit27.md`）・commit_message.txt・本 handoff はいずれも **bash heredoc または Python write_bytes 方式**で作成・更新した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（motifs.json は dry-run + 検証 + 本番適用の二段運用）。motifs.json は json round-trip 完全一致（`json.dumps(ensure_ascii=False, indent=2)`・末尾改行なし）を事前確認のうえ編集。retrofit 25-26 §(d-6) が記録した Write/Edit tool の truncate 事象を踏まえ、retrofit 27 では長文ファイル・スクリプトの作成・更新に Write/Edit tool を一切用いず、bash heredoc / Python write_bytes を第一選択とした結果、truncate 事象は発生しなかった。**今後もスクリプト・長文ファイルの作成・更新は bash heredoc / Python write_bytes を第一選択とし、Edit/Write tool での長文ファイル操作は避けることを強く推奨する**。stats の char 集計規則は「text フィールド値から改行（\n）を除いた文字数の総和」であり、retrofit 27 着手時の drift check でこの規則が stored 値と完全一致することを実測で確認したうえで recompute した。

### (d-7) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト（retrofit27_issaichichi.py・retrofit27_verify.py・add_chunote_aa_retrofit27.py・update_claude_md_retrofit27.py・chunote_aa_retrofit27.md・_dryrun_motifs_r27.json）・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。`git status --short` で deleted（D）行が 0 件であることを確認済で、commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-26 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx 等・計 166 件）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。retrofit 27 着手後の `git status` 実行時に bash サンドボックスのマウント層が `.git/index.lock` を unlink できない旨の warning（Operation not permitted）が出たが、これは実 Windows の `.git` には存在しない一時アーティファクトであり commit_push.bat には影響しない（retrofit 25-26 §(d-7) で確認済の事象）。

### (d-8) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 27 後で 全角〔/〕1163/1163・「」682/682・『』96/96 balanced、全角丸括弧（）は 1195/1196（pre-existing で閉じ括弧が 1 件超過・backup pre_retrofit27 で 1193/1194 と確認）、半角括弧は 284/287（pre-existing 差分・backup と同一）。retrofit 27 の追加部分（タイトル行・最終更新行の retrofit 27 エントリ）は〔〕13 対・「」5 対・『』3 対・全角丸括弧 1 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである。全角丸括弧・半角括弧の pre-existing 差分は retrofit 27 で新たに発生したものではなく、追加部分が balanced であれば許容する運用〔retrofit 17 §(d-5)・retrofit 19〜26 §(d-7)/§(d-8) で記録された CLAUDE.md pre-existing 括弧差分の継続〕。

### (d-9) CLAUDE.md 最終更新行の日付プレフィックスが stale

CLAUDE.md 最終更新行（line 1395）の冒頭は「最終更新:2026-05-22（**★ retrofit 27 完走〔…〕…」となっており、日付プレフィックス「2026-05-22」が retrofit 25（2026-05-23）・retrofit 26（2026-05-23）でも未更新のまま継続している pre-existing 事象である。retrofit 27 では retrofit 26 同型に最新エントリ「★ retrofit 27 完走…」を最終更新行の先頭に prepend し、日付プレフィックスは未変更とした（retrofit 25-26 の運用を踏襲・(d-5) の stale ラベルと同様、pre-existing 事象として記録のみ）。将来 retrofit で日付プレフィックスを最新 retrofit の日付へ補正するか否かはケンシン裁定とする。なおタイトル行（line 1）の各 retrofit エントリは「★ 2026-05-24 retrofit 27 完走…」のように個別に日付を保持しており、retrofit 27 エントリも正しく 2026-05-24 を保持する。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔770 件・m1-m744 + sg01-sg26・2,692,504 bytes・schema_history 85 件〕
- 本 retrofit build script：`outputs/retrofit27_issaichichi.py`〔dry-run + 本番適用の二段運用〕
- 整合性検証 script：`outputs/retrofit27_verify.py`
- 補注 AA 本文：`outputs/chunote_aa_retrofit27.md`／補注 AA 挿入 script：`outputs/add_chunote_aa_retrofit27.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit27.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit27.json`〔retrofit 前 motifs.json・2,687,746 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit27.md`〔retrofit 前・301,708 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit27.md`〔retrofit 前・346,139 bytes〕
  - `outputs/commit_message_backup_pre_retrofit27.txt`〔retrofit 前 commit_message.txt〕
  - `outputs/_dryrun_motifs_r27.json`〔retrofit 27 dry-run・検証用〕
- 前 retrofit handoff：`handoff_2026-05-23_retrofit26_complete.md`〔大日経疏 加持身 教学系軸連動〕
- 補注 AA 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 27 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-26 完走 → 2026-05-24 retrofit 27 完走〔大日経疏 一切智智 教学系軸連動・新規 sg26「一切智智」+ 単独 anchor m698 採用（大日経疏 巻第一 §31 執金剛秘密主の問）・強連動 5 件（m705/m707/m708/m709/m710）・連動軸二十二系統並立に到達・教学系軸の第十例・単独 anchor 体制 第十例〕。本体 motifs.json は 770 件・2,692,504 bytes・schema_history 85 件。motifs_index_design.md §2 に補注 AA 追加〔補注 A-Z＋AA 全 27 件 intact・322,130 bytes〕。CLAUDE.md は 351,696 bytes〔retrofit 4-27 全エントリ intact〕。連動軸二十二系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）、加持身 sg25/m679（単独）、一切智智 sg26/m698（単独）〕の書き下し anchor 自己参照タグ運用が完全整合。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教、教学系軸は retrofit 20 声字実相・retrofit 21 即身成仏義 二頌八句・retrofit 22 浄菩提心・retrofit 23 三種菩提心・retrofit 24 大心真言三摩地法門・retrofit 25 吽字四字・retrofit 26 加持身・retrofit 27 一切智智 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-24_retrofit27_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-23_retrofit26_complete.md`〔retrofit 26 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-AA 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・770 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 27 commit です。

【本セッションの選択肢】
(A) retrofit 28 候補〔教学系軸：般若心経秘鍵 仏法不外求軸（m492/m493 clean・anchor＋強連動 2 motif の最小規模・規模再検討要）／三教指帰軸／大日経疏 巻第一 残 31 件のさらなる主題軸化〕
(B) kaimyo-app 教学系素材活用：連動軸二十二系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- bash サンドボックスのマウント層に見える .git/index.lock 等は実 Windows の .git には存在しない一時アーティファクト・commit_push.bat には影響しない〔retrofit 25-27 で確認済〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Write/Edit tool が長文ファイルを truncate した事象が retrofit 25-26 で発生・retrofit 27 は heredoc 徹底で truncate 0 件〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用〔char 集計規則は text フィールドから改行を除いた文字数の総和〕
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 候補スキャンは中心成句の候補語を網羅的に変えてスキャンする〔retrofit 26 §(d-5)・retrofit 27 §(b) で再運用・handoff の暫定評価は出発点であって最終判定ではない〕
- 候補スキャンは thematic adjacency と連動タグ overlap を区別し、連動タグの実測に基づいて判定する〔retrofit 21 §(d-3)・retrofit 22-27 で再運用〕
- anchor を扱う retrofit では着手時に書き下し anchor 自己参照タグ全件検証を行う〔retrofit 27 で連動軸二十二系統 全件 OK 確認〕
- sg 成句 motif 自身は連動タグ未保有（成句は連動の参照先であり連動 motif プールの成員ではない・二十二系統一律の設計仕様）
- 単独 anchor 体制（補注 J/N/P/R/S/T/U/X/Y/Z/AA 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q/V/W 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- CLAUDE.md 最終更新行の日付プレフィックス「2026-05-22」は retrofit 25-27 で stale のまま継続〔handoff §(d-9)〕・補正可否はケンシン裁定
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-24〔retrofit 27 完走・大日経疏 一切智智 教学系軸連動 retrofit。新規 sg-id `sg26`「一切智智」を新設〔出典:大日経疏〕、書き下し anchor として単独 anchor m698 を採用（m698 大日経疏 巻第一 §31 執金剛秘密主の問「世尊よ、云何が如来応供正遍知は一切智智を得たり……云何が如来応供正遍知はこの一切智智を得たるやと」一切智智の獲得を因・根・究竟の三問とともに問う住心品の根本問）。強連動 5 motif：m705（§44 五喩総説）/ m707（§46 地譬）/ m708（§47 火譬）/ m709（§48 風譬）/ m710（§49 水譬）に「連動:sg26」「連動:m698」を付与（+12 タグ）。total_motifs 769→770（+1 新規 sg26）・famous_phrases 25→26。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,692,504 bytes〔+4,758〕・schema_history 85 件〔+1・origin: retrofit_27:doctrine〕・補注 AA 追加〔motifs_index_design.md §2・301,708→322,130 bytes・+20,422〕・CLAUDE.md 更新完了〔346,139→351,696 bytes〕・commit_message.txt 書き換え済。連動軸二十二系統並立に到達。教学系軸（retrofit 20 声字実相〜retrofit 26 加持身）に続く教学系軸の第十例で、『大日経疏』巻第一が註釈する『大日経』入真言門住心品の根本概念「一切智智」を主題とする軸。単独 anchor 体制の運用第十例（retrofit 14/16/18/19/20/21/24/25/26 に続く）。中心成句「一切智智」を anchor m698 が literal で直接含有する。一切智智の獲得を問う m698 §31 の三問に対する答えが三句法門 sg07 であり、一切智智 sg26 は問の側を、三句法門 sg07 は答の側をなして問答の対をなして並立する。retrofit 24-26 に続いて単独 anchor 体制を継続。anchor 1 ＋ 強連動 5 ＝ 6 motif の retrofit。handoff が「中心成句が明瞭な軸候補が残るかは Phase A 候補語スキャン次第」と暫定評価していた大日経疏 巻第一 残 37 件を、Phase A で「一切智智」を候補語として再スキャンすることで正常規模の軸として成立させた。Phase D 必須チェックリストに完全準拠する第十九の retrofit〕

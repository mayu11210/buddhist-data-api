# 引き継ぎメモ：retrofit 28 完走〔大日経疏 自心本性清浄 教学系軸連動 retrofit〕

**日付**：2026-05-25
**フェーズ**：retrofit 28（retrofit 27 完走に続く第二十五の retrofit セッション）
**対象**：空海所依の根本聖典『大日経』の註釈書『大日経疏』巻第一が掲げる根本定理「自心本性清浄」の連動軸新設。新規 sg-id `sg27`「自心本性清浄」を追加し、書き下し anchor として **単独 anchor m719**（大日経疏 巻第一 §61 金剛手の再問と仏答）を採用。強連動 3 motif（m721 §64-65／m726 §74-75／m727 §76）に連動タグを付与。連動軸二十三系統並立に到達。教学系軸の第十一例・単独 anchor 体制の運用第十一例。anchor 1 ＋ 強連動 3 ＝ 4 motif の retrofit。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 BB 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 29 候補〔般若心経秘鍵 仏法不外求軸（2 motif・過去最小未満）／三教指帰軸（連動軸モデル不適合）／大日経疏 巻第一 残 27 件〕／**W1 マージで増えた性霊集 1903 未連動 motif の活用（戦略的検討事項）**／kaimyo-app 教学系素材活用／W2 buddhist-doctrine-workshop repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_28:doctrine・148 件〕
- [x] motifs_index_design.md に補注 BB 追加済〔補注 A-Z＋AA＋BB 全 28 件 intact・322,130→339,027 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・357,626→363,122 bytes・行数 1396 不変〕
- [x] commit_message.txt 書き換え済〔retrofit 28 用・冒頭行整合確認済〕
- [x] handoff_2026-05-25_retrofit28_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認

---

## (a) 本セッションの位置づけ

2026-05-25 Phase 4 W1 完走マージ（commit `66b13db` の前の `310fea6`・W1 buddhist-shoryoshu-workshop の性霊集 残篇を本体統合・total_motifs 2200）・W1 repo 凍結（選択肢 A 完了）に続き、retrofit 27 完走 handoff §(c) 選択肢 A〔retrofit 28 候補：教学系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で大日経疏 自心本性清浄軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg27`「自心本性清浄」を追加〔出典:大日経疏・『大日経疏』巻第一が註釈する『大日経』入真言門住心品の根本定理〕
- 書き下し anchor は **単独 anchor m719**（大日経疏 巻第一 §61 金剛手の再問と仏答）
- 強連動 3 motif（m721 §64-65 青黄赤白離相・心実相／m726 §74-75 陰界入心不可得・自心本不生悟入／m727 §76 即時人法戯論浄・自然覚・頓悟法門）に「連動:sg27」「連動:m719」を付与（+8 タグ）
- 連動軸二十三系統並立に到達
- **教学系軸の第十一例**（retrofit 20 声字実相〜retrofit 27 一切智智 に続く）
- **単独 anchor 体制の運用第十一例**
- **4 motif retrofit**（anchor 1 ＋ 強連動 3・retrofit 19 顕密二教・retrofit 25 吽字四字 と同規模）
- **W1 完走マージ後の本体 2200 motif を対象とする初の retrofit**

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 27 完走 handoff §(c) 選択肢 A に着手。着手時に anchor 自己参照タグ全件検証を実施し、連動軸二十二系統（sg02/sg03/sg07-sg26）の書き下し anchor がすべて「連動:sgNN」「連動:m(anchor)」を保有する完全整合状態を確認（補整不要）。Phase A スキャンで W1 完走マージ後の本体 2200 motif を実測した結果：

| 候補 | 実測 | 判定 |
|---|---|---|
| 大日経疏 自心本性清浄軸 | dainichikyo-sho-vol1 未連動 31 件のうち §61 m719（自心本性清浄・大日経根本定理）を anchor とし、§64-65 m721・§74-75 m726・§76 m727 が clean クラスタをなす | 採用 |
| 般若心経秘鍵 仏法不外求軸 | m492 anchor ＋ 強連動 m493 ＝ 2 motif で過去最小（retrofit 25 吽字四字 4 motif）を下回る | 基準未達・retrofit 29 以降に温存 |
| 三教指帰軸 | sankyo-shiki 21 件 clean だが「三教」literal が枠組み motif で連動軸モデル不適合 | 基準未達・retrofit 29 以降に温存 |

ケンシン裁定（retrofit 28 Phase A）により候補 大日経疏 自心本性清浄軸を採用。中心成句 sg27「自心本性清浄」、anchor を単独 anchor m719、強連動 3 件の 4 motif retrofit として軸を構成。

### Phase B：4 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m719 | 大日経疏 巻第一 §61 金剛手の再問と仏答 | 書き下し anchor（単独・自己参照）・「自らの心に菩提と、及び一切智とを尋求す。何をもっての故に、本性清浄なるが故に……衆生の自心の実相は、すなわちこれ菩提なり。有仏にも無仏にも、常に自ら厳浄なり」自心の本性清浄を説く大日経の根本定理 |
| m721 | 大日経疏 巻第一 §64-65 青黄赤白離相・盲人摸象 | 強連動・「如来応正等覚は青にあらず、黄にあらず……真我に約して心の実相を明かす」一切の相を離れた心の実相を明かす段 |
| m726 | 大日経疏 巻第一 §74-75 陰界入摩訶般若 | 強連動・「即時に懸かに自心の本不生際を悟る。如来智見の大菩提道の中において、遠塵離垢し、法眼浄を得たり」陰界入を分析して自心の本不生際を悟る真言菩薩の観法 |
| m727 | 大日経疏 巻第一 §76 即時人法戯論浄 | 強連動・「初発心の時において直ちに自心の実相を観じ、本不生を了知するが故に……自然覚を成じて、他に由って悟らず」初発心における自心実相観と頓悟の法門 |

体系内連節カバー：自心の本性清浄を説く根本定理（m719 §61）→ 一切の相を離れた心の実相（m721 §64-65）→ 陰界入分析による自心の本不生際の悟入（m726 §74-75）→ 初発心における自心実相観と頓悟（m727 §76）の大日経疏 巻第一 §61〜§76 を一括包摂。

**除外・温存**：dainichikyo-sho-vol1 corpus のうち、§59-91 の浄菩提心系 motif（m718/m725/m728/m732/m735/m739 ほか）は retrofit 22 で浄菩提心 sg21 に連動済。自心実相・本来性系の clean motif（m700 §37 自証境ほか）は自心本性清浄軸と thematic に隣接するが 4 motif の正常規模を保つため温存。本軸 4 motif はいずれも着手前は連動タグ未保有であり、多系統連動 motif は新たに発生しない。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 2200 | 2201 | +1（sg27 新規追加） |
| famous_phrases | 26 | 27 | +1 |
| ファイルサイズ | 5,094,815 bytes | 5,099,034 bytes | +4,219 |
| schema_history | 147 | 148 | +1（origin: retrofit_28:doctrine） |
| 連動タグ総数 | — | — | +8（sg27 軸 4 motif × 2） |
| kakikudashi_chars_total | 146,057 | 146,063 | +6（「自心本性清浄」6 字） |
| gendaigoyaku_chars_total | 549,031 | 549,822 | +791（sg27 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 2201 vs 2201 ✓ |
| 2 | m-id 連番性〔m1-m2174〕 | missing=[]、count=2174、dups=なし ✓ |
| 3 | NUL バイト 0 件 | 0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性〔id/source/text_kakikudashi/text_gendaigoyaku/tags〕 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔sg27 軸 4 motif × 2〕 | missing=[] ✓ |
| 7 | sg 配列 sg01-sg27 連番・末尾 sg27 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0, fp=0 ✓ |

着手時点で W1 完走マージ後の stats が drift ゼロであることを確認（pre-change drift check で stored=recompute 完全一致）。retrofit 28 では stats 6 項目を全件 recompute（total_motifs 2201・famous_phrases 27・kakikudashi_chars_total 146063・gendaigoyaku_chars_total 549822・gendai_gabun_chars_total 238704・motifs_with_gendai_gabun 2173）。motifs.json は `json.dumps(ensure_ascii=False, indent=2)`・末尾改行なしの round-trip 完全一致を事前確認のうえ編集（dry-run + 検証 + 本番適用の二段運用）。

### Phase D：補注 BB 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 BB〔大日経疏 自心本性清浄 教学系軸連動の運用〕新規追加（322,130→339,027 bytes・+16,897・補注 A-Z＋AA＋BB 全 28 件 intact・補注 BB 内部の〔〕26/26・「」37/37・『』14/14・全角丸括弧 102/102 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 28 完走エントリを追加（357,626→363,122 bytes・行数 1396 不変・追加部分の〔〕12 対・「」4 対・『』2 対がいずれも balanced・新規半角括弧/全角丸括弧 0 件）。
- `commit_message.txt` を retrofit 28 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-25_retrofit28_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第十一例・大日経疏 巻第一の四軸並立

retrofit 22 浄菩提心軸が『大日経疏』巻第一における行者の菩提心の論、retrofit 26 加持身軸が同巻第一における大日如来の身の論、retrofit 27 一切智智軸が同巻第一が掲げる仏の自証の智の論を軸とするのに続き、retrofit 28 自心本性清浄軸は同巻第一が掲げる衆生の自心の本性清浄をめぐる根本定理を軸とする。『大日経疏』巻第一のうちに、仏身論（加持身 sg25）・智論（一切智智 sg26）・菩提心論（浄菩提心 sg21）・本性論（自心本性清浄 sg27）が並立する。一切智智 sg26 が仏の自証の智そのものを軸とするのに対し、自心本性清浄 sg27 はその一切智智がそもそも衆生の自心に本来そなわる所以を明かす根本定理を軸とし、sg26 が問の側「云何が一切智智を得たるや」、sg27 が答の側「本性清浄なるが故に」を担って対をなす。

#### 2. 連動軸二十三系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）、六大無礙 sg20/m534（単独）、浄菩提心 sg21/m638+m728（系統対比型）、三種菩提心 sg22/m506+m581（系統対比型）、大心真言三摩地法門 sg23/m496（単独）、吽字四字 sg24/m564（単独）、加持身 sg25/m679（単独）、一切智智 sg26/m698（単独）、自心本性清浄 sg27/m719（単独）〕の二十三系統並立に到達。

#### 3. 浄菩提心 sg21 との節間隙運用

浄菩提心 sg21（retrofit 22）は大日経疏 巻第一 §59-91 のうち §59-60（m718）・§71-73（m725）・§77-79（m728 anchor）・§83（m732）・§87（m735）・§91（m739）をカバーするのに対し、自心本性清浄 sg27 はその間隙にあたる §61（m719 anchor）・§64-65（m721）・§74-75（m726）・§76（m727）をカバーする。両軸は『大日経疏』巻第一 §59-91 の自心をめぐる教学線を共有する thematic adjacency にありながら、連動タグ overlap はゼロに保たれ、別系統の連動軸として並立する。Phase A 着手前に「sg21 と主題が近接し除外原則を厳密に運用する要あり」とケンシンに提示し、裁定で採用となった。

#### 4. W1 完走マージ後の本体 2200 motif を対象とする初の retrofit

retrofit 5-27 は本体 motifs.json が 750-770 motif の状態で実施されたが、retrofit 28 は 2026-05-25 Phase 4 W1 完走マージ（性霊集 残篇 sw124-sw1553 を m745-m2174 に統合・total_motifs 2200）後の本体を対象とする初の retrofit である。対象 corpus（大日経疏 巻第一）は教学系 m491-m744 の範囲にあり W1 マージの影響を受けないが、整合性検証 2（m-id 連番性）は m1-m2174 の全範囲で実施した。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=2201  OK
2. m-id range m1-m2174 continuous count=2174 missing=[] dups=False  OK
3. NUL bytes=0  OK
4. schema_version=0.2  OK
5. required fields incomplete=[]  OK
6. 連動タグ sg27軸 4motif×2 全付与 missing=[]  OK
7. sg list sg01-sg27 continuous tail=sg27  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0 fp=0  OK
   anchor m719 self-reference tags  OK / motif text 半角括弧 0

[stats（retrofit 28 後）]
total_motifs=2201  famous_phrases=27
kakikudashi_chars_total=146,063
gendaigoyaku_chars_total=549,822
gendai_gabun_chars_total=238,704
motifs_with_gendai_gabun=2,173
schema_history=148 entries
file size=5,099,034 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 29〔教学系軸の継続〕

- **般若心経秘鍵 仏法不外求軸**：m492 anchor ＋ 強連動 m493 ＝ 2 motif で過去最小未満。最小規模軸を許容するか要判断。
- **三教指帰軸**：sankyo-shiki 21 件 clean だが連動軸モデル不適合。retrofit 4 で発言者軸を運用済。
- **大日経疏 巻第一 残 27 件**：retrofit 28 後、dainichikyo-sho-vol1 68 件のうち未連動は 27 件（retrofit 27 時点 31 件から sg27 軸 4 件を連動）。中心成句が明瞭な軸候補が残るかは Phase A 候補語スキャン次第。

### 選択肢 B：W1 マージで増えた性霊集 1903 未連動 motif の活用〔戦略的検討事項〕

2026-05-25 Phase 4 W1 完走マージで性霊集 motif が 1921 件に増加し、うち 1903 件が連動タグ未保有である。教学系 corpus の連動軸候補が枯渇しつつある一方、性霊集側は大規模な未活用素材プールとなっている。retrofit 連動軸モデル（中心成句＋書き下し anchor＋強連動）を性霊集に適用するか、既存の法華経連動軸（sg10-sg16）を W1 マージ由来の性霊集 法華経譬喩 allusion で被覆拡張するか（retrofit 7 型・新規 sg-id なし）は、retrofit 29 以降の戦略的検討事項。retrofit 28 Phase A 実測では、未連動 × 典故:法華経 系が 43 件あり、うち火宅三車関連が約 6 件、他軸は各 1 件程度と薄い分布。

### 選択肢 C：kaimyo-app 教学系素材活用

連動軸二十三系統 anchor 完全整合済の素材プールを kaimyo-app で活用。

### 選択肢 D：W2 buddhist-doctrine-workshop repo 凍結手続〔workshop_protocol §10(5)〕

W2 は 2026-05-11 に本体マージ済。W1 repo は本セッション前に archive 化済。W2 repo の凍結（archive 化）が未了であれば実施。

---

## (d) 副次発見・要注意事項

### (d-1) anchor 自己参照タグ全件検証〔retrofit 28 後 二十三系統 完全整合〕

retrofit 28 着手時に連動軸二十二系統（sg02/sg03/sg07-sg26）の書き下し anchor 自己参照タグ全件検証を実施し、全 anchor が「連動:sgNN」「連動:m(anchor)」を保有する完全整合を確認（補整不要）。retrofit 28 で追加した sg27 単独 anchor m719 も「連動:sg27」「連動:m719」を保有。sg 成句 motif 自身（sg02/sg03/sg07-sg27）は連動タグ未保有（成句は連動の参照先であり連動 motif プールの成員ではない・一律の設計仕様）。今後 anchor を扱う retrofit でも着手時の全件検証を継続する。

### (d-2) 般若心経秘鍵 仏法不外求軸・(d-3) 三教指帰軸の温存

retrofit 24-28 の Phase A で繰り返し候補に挙がるが、仏法不外求軸は anchor＋強連動 2 motif の最小規模、三教指帰軸は連動軸モデル不適合のため温存継続。将来 retrofit で仏法不外求軸を採る場合、2 motif の最小規模を許容するか否かの判断を要する。

### (d-4) 大日経疏 巻第一 corpus のカバー範囲

retrofit 28 後、dainichikyo-sho-vol1 corpus（68 件）は 41 件が連動タグ保有（sg27 自心本性清浄 4 件 m719/m721/m726/m727 を追加）・27 件が未連動。

### (d-5) 篇別内訳 `成句_七件` キーが stale

motifs.json の stats.篇別内訳 に `成句_七件` キー（motifs: sg01-sg07・件数 7）があるが、sg08-sg27 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-28 で sg08-sg27 を追加しても未更新）。これは整合性検証 8 項目（数値 stats の recompute）の対象外の説明ラベルであり、retrofit 8-28 一貫して未更新の pre-existing 事象。retrofit 28 でも踏襲し未変更とした。将来「成句_二十七件」等への補正を検討。

### (d-6) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

retrofit 5-27 §(d-5) で記録された pre-existing 事象。"sg01-sg07" キーは sg08-sg27 追加後も未更新。整合性検証対象外。retrofit 28 でも踏襲し未変更。

### (d-7) sg 成句 motif は 5 キー構造（text_gendai_gabun キーなし）

sg01-sg27 および m06 は `text_gendai_gabun` キーを持たない 5 キー構造（id/source/text_kakikudashi/text_gendaigoyaku/tags）。schema 0.2 で text_gendai_gabun はオプションフィールドであり、成句は儀礼朗誦の伝統で漢文・成句形のまま使うため雅文体訳を設けない設計（motifs_index_design.md §3）。retrofit 28 の sg27 もこの 5 キー構造で構築。整合性検証 5（必須フィールド完全性）は text_gendai_gabun を必須に含めない（id/source/text_kakikudashi/text_gendaigoyaku/tags の 5 フィールドで判定）。

### (d-8) 編集手法・truncate 事象回避

retrofit 28 のビルドスクリプト（`outputs/retrofit28_jishin_honjo_shojo.py`）・Phase D 挿入スクリプト（`outputs/retrofit28_phaseD_insert.py`）・補注 BB 本文（`outputs/chunote_bb_retrofit28.md`）・CLAUDE.md エントリ（`outputs/claude_entry_r28.txt`）・commit_message.txt・本 handoff はいずれも bash heredoc または Python write 方式で作成。motifs.json は dry-run + 検証 + 本番適用の二段運用。Write/Edit tool の長文 truncate を避けるため bash heredoc を第一選択とした。

### (d-9) git 状態・commit_push.bat について

本コミットは新規ファイル追加（outputs 配下スクリプト・バックアップ・handoff）と既存ファイル更新（motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt）のみで削除なし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。

### (d-10) CLAUDE.md 最終更新行の日付プレフィックスが stale

CLAUDE.md 最終更新行（line 1395）の冒頭は「最終更新:2026-05-25（**★ 2026-05-25 retrofit 28 完走…」となり、retrofit 28 エントリを先頭 prepend した。日付プレフィックス「2026-05-25」は W1 完走マージで更新済のため retrofit 28 でも整合。なお line 1349 にも旧い「最終更新:2026-05-09」行が pre-existing で残存しているが、retrofit 27 以前から未変更のため本 retrofit でも未変更とした。

---

## 関連リンク

- 本体 motifs.json：`data/indices/motifs.json`〔2201 件・m1-m2174 ＋ sg01-sg27・5,099,034 bytes・schema_history 148 件〕
- 本 retrofit build script：`outputs/retrofit28_jishin_honjo_shojo.py`〔dryrun/apply 二段運用〕
- Phase D 挿入 script：`outputs/retrofit28_phaseD_insert.py`
- 補注 BB 本文：`outputs/chunote_bb_retrofit28.md`
- CLAUDE.md エントリ：`outputs/claude_entry_r28.txt`
- バックアップ：`outputs/motifs_backup_pre_retrofit28.json`／`outputs/motifs_index_design_backup_pre_retrofit28.md`／`outputs/CLAUDE_md_backup_pre_retrofit28.md`／`outputs/commit_message_backup_pre_retrofit28.txt`／`outputs/_dryrun_motifs_r28.json`
- 前 retrofit handoff：`handoff_2026-05-24_retrofit27_complete.md`〔大日経疏 一切智智 教学系軸連動〕
- W1 完走マージ handoff：`handoff_2026-05-25_w1_completion_merge_complete.md`
- 補注 BB 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 28 完了後）===

【最初にやること】
作業フォルダ C:\Users\user\buddhist-data-api を mcp__cowork__request_cowork_directory で接続してください。

【セッション概要】
2026-05-25 Phase 4 W1 完走マージ（total_motifs 2200）・W1 repo 凍結 → retrofit 28 完走
〔大日経疏 自心本性清浄 教学系軸連動・新規 sg27「自心本性清浄」+ 単独 anchor m719・
強連動 3 件（m721/m726/m727）・連動軸二十三系統並立に到達・教学系軸の第十一例〕。
本体 motifs.json は 2201 件・5,099,034 bytes・schema_history 148 件。

【最初に読むファイル（順番）】
1. handoff_2026-05-25_retrofit28_complete.md（本 retrofit 完走サマリ）
2. handoff_2026-05-24_retrofit27_complete.md（retrofit 27 完走サマリ）
3. CLAUDE.md（本体ルール・進捗ヘッダ）
4. _dev_references/motifs_index_design.md（schema 0.2 仕様・補注 D-BB）
5. data/indices/motifs.json（本体現況・2201 件）

着手前に git log --oneline -5 で HEAD 確認してください。

【次フェーズの選択肢】
(A) retrofit 29 候補（般若心経秘鍵 仏法不外求軸／三教指帰軸／大日経疏 巻第一 残 27 件）
(B) W1 マージで増えた性霊集 1903 未連動 motif の活用（戦略的検討事項）
(C) kaimyo-app 教学系素材活用
(D) W2 buddhist-doctrine-workshop repo 凍結手続

【注意点】
- bash mount 経由 git 書き込み禁止（commit_push.bat 経由でケンシン側ダブルクリック）
- 長文編集・スクリプト作成は bash heredoc または Python write 方式を採用
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- anchor を扱う retrofit では着手時に書き下し anchor 自己参照タグ全件検証を行う
- Phase D 必須チェックリストに従う（commit_message.txt 更新は必須項目）

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-25〔retrofit 28 完走・大日経疏 自心本性清浄 教学系軸連動 retrofit。新規 sg-id `sg27`「自心本性清浄」を新設〔出典:大日経疏〕、書き下し anchor として単独 anchor m719（大日経疏 巻第一 §61 金剛手の再問と仏答）を採用。強連動 3 motif：m721（§64-65 青黄赤白離相・心実相）/ m726（§74-75 陰界入心不可得・自心本不生悟入）/ m727（§76 即時人法戯論浄・自然覚・頓悟法門）に「連動:sg27」「連動:m719」を付与（+8 タグ）。total_motifs 2200→2201・famous_phrases 26→27。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 5,099,034 bytes〔+4,219〕・schema_history 148 件〔+1・origin: retrofit_28:doctrine〕・補注 BB 追加〔motifs_index_design.md §2・322,130→339,027 bytes〕・CLAUDE.md 更新完了〔357,626→363,122 bytes〕・commit_message.txt 書き換え済。連動軸二十三系統並立に到達。教学系軸の第十一例・単独 anchor 体制の運用第十一例。W1 完走マージ後の本体 2200 motif を対象とする初の retrofit。Phase D 必須チェックリストに完全準拠する第二十の retrofit〕

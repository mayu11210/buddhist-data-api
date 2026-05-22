# 引き継ぎメモ：retrofit 20 完走〔声字実相 教学系軸連動 retrofit〕

**日付**：2026-05-22
**フェーズ**：retrofit 20（retrofit 19 完走に続く第十七の retrofit セッション）
**対象**：空海の言語哲学＝密教言語論の根幹「声字実相」の連動軸新設。新規 sg-id `sg19`「五大皆有響」を追加し、書き下し anchor として既存 m525（声字実相義 第四節・四句頌「五大にみな響あり、十界に言語を具す、六塵ことごとく文字なり、法身はこれ実相なり」一切の存在を法身の文字とみる声字実相義の中心頌）を **単独採用**。強連動 3 motif（m521 第一節 綱領 / m523 第二節 三義定義 / m524 第三節 阿字声字釈）に連動タグを付与。連動軸十五系統並立に到達。本 retrofit は retrofit 18 十住心・retrofit 19 顕密二教 の教学体系軸に続く **教学系軸の第三例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教 同型の **単独 anchor 体制の運用第五例**。anchor 1 + 強連動 3 = 4 motif の **小規模 retrofit 第五例**。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 T 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 21 候補〔教学系軸：大日経疏 vol1 浄菩提心軸／即身成仏義 六大四曼三密軸／吽字義 等〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_20:doctrine〕
- [x] motifs_index_design.md に補注 T 追加済〔補注 A-T 全 20 件 intact・187,184→200,245 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・294,976→304,043 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 20 用・冒頭行整合確認済〕
- [x] handoff_2026-05-22_retrofit20_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 19 補正済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 19 完走〔顕密二教 教学体系軸連動・新規 sg18 + 既存 m571 を書き下し anchor 単独採用・commit `bd170e3`〕に続く第十七の retrofit セッション。

retrofit 19 完走 handoff §(c) 選択肢 A〔retrofit 20 候補：教学体系軸の継続〕に着手。Phase A スキャンの結果、ケンシン裁定で声字実相軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg19`「五大皆有響」を追加〔出典:声字実相義・空海が一切の声・字・実相は法身大日如来の三密の活動にほかならないとする密教言語論・万物文字論の中心成句・声字実相義 四句頌の冒頭句〕
- 書き下し anchor は m525 単独（声字実相義 第四節・四句頌「五大にみな響あり、十界に言語を具す、六塵ことごとく文字なり、法身はこれ実相なり」）
- 強連動 3 motif（m521 第一節 綱領 / m523 第二節 三義定義 / m524 第三節 阿字声字釈）に「連動:sg19」「連動:m525」を付与（+8 タグ）
- 連動軸十五系統並立に到達
- **教学系軸の第三例**（retrofit 18 十住心・retrofit 19 顕密二教 に続く・ただし両者が教判を主題とするのに対し声字実相は言語哲学を主題とする）
- **単独 anchor 体制の運用第五例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心・retrofit 19 顕密二教 に続く）
- **小規模 retrofit の第五例**（4 motif・retrofit 14 多宝塔・retrofit 18 十住心・retrofit 19 顕密二教 と同規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 19 完走 handoff §(c) 選択肢 A に着手。Phase A スキャンで retrofit 20 候補（大日経疏 vol1 内部体系軸／声字実相義 五大皆有響軸／菩提心論 三摩地戒／即身成仏義 六大四曼三密 等）の中心成句の kakikudashi 直接含有を全 762 motif にわたり網羅検査：

| 候補 | kakikudashi 支持 | 判定 |
|---|---|---|
| 声字実相義 声字実相軸 | m525 が四句頌「五大にみな響あり…」を直接含有・m521 が「声字実相」を直接含有・既存軸との重複極小（m524 の sg08 連動 1 件のみ） | 採用 |
| 大日経疏 vol1 浄菩提心軸 | 「浄菩提心」14 件中 12 件が大日経疏に集中するも、当該 motif の m715/m716/m723/m724 が既に sg07 連動・m724/m740 が sg03 連動・m738 が sg15 連動で重複大 | retrofit 21 以降に温存 |
| 即身成仏義 六大四曼三密軸 | m534 下頌「六大無礙にして…」が sg03 即身成仏 anchor m533 上頌と同一二頌八句を分割・sg03 と重複 | 見送り |
| 菩提心論 三摩地戒軸 | 「三摩地戒」「三種の菩提心」kakikudashi 直接含有 0 件・「三摩地」は他典籍に拡散 | 基準未達・スコープ外 |

声字実相義 は即身成仏義・吽字義 と並ぶ空海 三部書の一でありながら独立軸が未設置であり、kakikudashi 直接含有が明確で既存軸との重複が極小であるため、本 retrofit は声字実相義 内部に限定して軸を構成。ケンシン裁定で判断 1-5：

- **判断 1**：中心成句 sg19 =「五大皆有響」（声字実相義 四句頌の冒頭句・出典:声字実相義）。当初スキャンで「五大に皆な響きあり」0 件と出たが、これは仮名遣い差（「皆な」対「みな」）であり、kakikudashi の実形「五大にみな響あり」を m525 が直接含有する。
- **判断 2**：書き下し anchor = m525 単独採用（声字実相義 第四節 四句頌・単独 anchor 体制・retrofit 14/16/18/19 同型 第五例）
- **判断 3**：強連動 = 声字実相義 内部限定（anchor m525 + 強連動 3 件 = 計 4 motif）
- **判断 4**：強連動 3 件 = m521（第一節 綱領）/ m523（第二節 三義定義）/ m524（第三節 阿字声字釈）
- **判断 5**：単独 anchor タグ運用 = 補注 J/N/P/R/S 案 A 単独版（全 motif に「連動:sg19」「連動:m525」の 2 タグ付与）

成句・anchor の組合せは、案 X（成句「五大皆有響」/ anchor m525 四句頌）と案 Y（成句「声字実相」/ anchor m521 第一節定義句）の 2 案をケンシンに提示し、声字実相義 で最も人口に膾炙した核心句は四句頌であり anchor を核心句に置く原則から **案 X を採用**。

### Phase B：4 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m525 | 声字実相義 第四節 | 書き下し anchor（単独・自己参照）・「五大にみな響あり、十界に言語を具す、六塵ことごとく文字なり、法身はこれ実相なり」一切の存在を法身の文字とみる声字実相義の中心頌 |
| m521 | 声字実相義 第一節 | 強連動・「いわゆる声字実相とはすなわちこれ法仏平等の三密、衆生本有の曼荼なり。故に大日如来この声字実相の義を説いて、かの衆生長眠の耳を驚かしたもう」声字実相を法仏平等の三密・衆生本有の曼荼と規定する全篇の綱領 |
| m523 | 声字実相義 第二節 | 強連動・「内外の風気わずかに発すれば必ず響くを名づけて声という。声発して虚からず、必ず物の名を表するを号して字という。名は必ず体を招く。これを実相と名づく」声・字・実相の三義を定義する釈名の核心句 |
| m524 | 声字実相義 第三節 | 強連動・「梵本の初の阿字、口を開いて呼ぶ時に阿の声あるはすなわちこれ声なり……法身とは諸法本不生の義、すなわちこれ実相なり」阿字一字に声・字・実相の三種を具足する密教言語論の典型例。既に sg08（阿字本不生）連動済のため sg08/sg19 二系統連動 motif となる |

体系内連節カバー：定義の綱領（m521 第一節）→ 三義の語義定義（m523 第二節）→ 阿字の具体例（m524 第三節）→ 五大皆有響の中心頌（m525 第四節 anchor）の声字実相義 第一〜第四節を一括包摂。

**除外・温存**：声字実相義 第五節 真言論（m526-m529）・第六節 色塵論（m530-m532）は声字実相の応用・展開を扱う motif であり「主題:声字実相」タグ保持により別途検索可能なため温存。m522（第一節・「衆生痴暗にして自ら覚るに由なし、如来加持してその帰趣を示したもう」）は加持を主題とする第一節の付随句であり、声字実相の定義を直接担わないため対象外とした。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 762 | 763 | +1（sg19 新規追加） |
| famous_phrases | 18 | 19 | +1 |
| ファイルサイズ | 2,644,758 bytes | 2,650,402 bytes | +5,644 |
| schema_history | 77 | 78 | +1（origin: retrofit_20:doctrine） |
| 連動タグ総数 | — | — | +8（m525/m521/m523/m524 各 +2） |
| kakikudashi_chars_total | 112,815 | 112,820 | +5（「五大皆有響」5 字） |
| gendaigoyaku_chars_total | 314,650 | 316,018 | +1,368（sg19 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 763 vs 763 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0, trailing=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔4 motif × 2 tags〕 | missing=[] ✓ |
| 7 | sg19 配列末尾追加・sg01-sg19 連番 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 19 で recompute した stats は retrofit 20 着手時点で全 5 項目 drift ゼロを確認（pre-change drift check で stored=recompute 一致）。retrofit 20 では stats を全件 recompute して真値を書き込み（total_motifs 763・famous_phrases 19・kakikudashi_chars_total 112,820・gendaigoyaku_chars_total 316,018・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。top-level generated_at は 2026-05-22T00:00:00+09:00 を維持。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 T 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 T〔声字実相 教学系軸連動の運用〕新規追加（187,184→200,245 bytes・+13,061・補注 A-T 全 20 件 intact・全角丸括弧 71/71 balanced・〔〕18/18 balanced・かぎ括弧 34/34 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 20 完走エントリを追加（294,976→304,043 bytes・retrofit 4-20 全エントリ intact・追加部分の全角角括弧 31/31・かぎ括弧 10/10 balanced・新規半角括弧 0 件・全角〔〕全体 883/883 balanced）。
- `commit_message.txt` を retrofit 20 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-22_retrofit20_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学系軸の第三例・空海 三部書の言語哲学軸

retrofit 18 十住心軸・retrofit 19 顕密二教軸はいずれも空海の教判を主題とする教学体系軸であった。retrofit 20 声字実相軸はその継続でありながら、一切の声・字・実相が法身大日如来の三密の活動にほかならないとする空海の言語哲学・存在論を主題とする点に特色をもつため、本 retrofit では教学体系軸と区別して **教学系軸の第三例** と位置づける。声字実相義 は即身成仏義（即身成仏 sg03 の出典）・吽字義 と並ぶ空海 三部書の一であり、本 retrofit により三部書のうち即身成仏義・声字実相義 の二著作が連動軸 anchor をもつに至った。

#### 2. 連動軸十五系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）〕の十五系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）・顕密判（顕密二教）に加えて、密教言語論・万物文字論（声字実相）でも素材プールを切替可能。

#### 3. 単独 anchor 体制の運用第五例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599・retrofit 19 顕密二教 sg18/m571 に続く第五の単独 anchor 体制。声字実相の中心頌は m525 の四句頌が単一の核心句であり、典籍系統対比型の二重 anchor を要さず単独 anchor が自然形となる。第一節の定義句 m521（「いわゆる声字実相とは……」）は語「声字実相」そのものを直接含有する全篇の綱領だが、ケンシン裁定で中心成句を四句頌冒頭句「五大皆有響」と定めたため、m521 は anchor ではなく強連動に位置づけた。

#### 4. 多系統連動 motif の第二類型

retrofit 17 で m639 が sg09 諸法実相・sg16 従地涌出 の二系統 anchor に二重所属したのは「anchor の多系統所属」であった。retrofit 20 で m524（声字実相義 第三節 阿字声字釈）が sg08 阿字本不生・sg19 声字実相 の二系統に連動するのは「強連動 motif の多系統所属」であり、多系統連動 motif の第二類型に当たる。阿字一字が阿字本不生の義（sg08）と声字実相の典型例（sg19）の双方を担うため、m524 は両軸を橋渡しする結節点となる。

#### 5. 小規模 retrofit の第五例

anchor 1 ＋ 強連動 3 ＝ 4 motif は retrofit 14 多宝塔・retrofit 18 十住心・retrofit 19 顕密二教（各 4 motif）と同規模。声字実相義 の骨格を成す第一〜第四節（綱領・三義定義・阿字声字釈・中心頌）に絞り、第五節 真言論・第六節 色塵論を温存することで自然に小規模化した。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=763  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0 trailing=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ 4 motif x 2 tags 全付与  OK
7. sg list sg01-sg19 continuous, tail=sg19  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK

[stats（retrofit 20 後）]
total_motifs=763  famous_phrases=19
kakikudashi_chars_total=112,820
gendaigoyaku_chars_total=316,018
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=78 entries
file size=2,650,402 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 21〔教学系軸の継続〕

- **大日経疏 vol1 浄菩提心軸**：「浄菩提心」は大日経疏 巻第一に 12 件集中し kakikudashi 支持は強いが、当該 motif の複数が既に sg07 三句法門 連動済であり、重複しない節点に絞り込む設計が要。
- **即身成仏義 六大四曼三密軸**：m534 下頌が sg03 即身成仏 anchor m533 上頌と同一二頌八句を分割するため、sg03 との重複を整理する設計が要。
- **吽字義**：空海 三部書の残る一。吽字一字の字相・字義を体系軸化する候補。阿字本不生 sg08 の anchor m549 が吽字義 出典であるため重複の整理が要。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸十五系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg19 五大皆有響（声字実相）は密教言語論・万物文字論・本来性論を駆動する辞書として、戒名・諷誦文・引導文の素材選択に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 声字実相義 の連動軸カバー範囲

本 retrofit は声字実相義 第一〜第四節（m521/m523/m524/m525）を連動軸化した。第五節 真言論（m526「故に経に真語者・実語者……」/m527/m528/m529）・第六節 色塵論（m530「顕形表等の色あり……」/m531/m532）は「主題:声字実相」タグ保持により別途検索可能なため温存した。将来 retrofit で声字実相義 全篇（第一〜第六節）を連動軸に拡張する余地は残る。

### (d-2) 候補スキャンの仮名遣い差に関する注意

Phase A スキャンで中心成句「五大に皆な響きあり」を検索した際、kakikudashi 直接含有 0 件と出た。これは kakikudashi の実形が「五大にみな響あり」（「皆な」ではなく「みな」、「響きあり」ではなく「響あり」）であったためである。候補スキャンでは仮名遣い・送り仮名のゆれを考慮し、複数の表記形でスキャンする必要がある。今後の Phase A スキャンでも留意。

### (d-3) m524 の多系統連動

m524（声字実相義 第三節 阿字声字釈）は retrofit 8 で阿字本不生 sg08/m549 の強連動として既にタグ付与済であり、本 retrofit で「連動:sg19」「連動:m525」を追加したことで sg08/sg19 二系統に連動する多系統連動 motif となった。m524 の現在の連動タグは〔連動:sg08, 連動:m549, 連動:sg19, 連動:m525〕の 4 件（axis ペア順次・retrofit 17 m639 の二重所属タグ運用と同型）。

### (d-4) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg19 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-20 で sg08-sg19 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-20 一貫して未更新の pre-existing 事象。retrofit 20 でも踏襲し未変更とした。将来 "sg01-sg19" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-5) 編集手法・truncate 事象回避

retrofit 20 のビルドスクリプト（`outputs/retrofit20_shoji_jisso.py`）・補注 T 追加スクリプト（`outputs/add_chunote_t_retrofit20.py`）・CLAUDE.md 更新スクリプト（`outputs/update_claude_md_retrofit20.py`）・commit_message.txt・本 handoff はすべて bash heredoc 方式で作成し、retrofit 19 §(d-3) で記録された Edit/Write tool の truncate 事象を回避した。motifs.json・motifs_index_design.md・CLAUDE.md の更新はいずれも Python script による read → in-memory 編集 → write_bytes 方式（dry-run + 本番適用の二段運用）。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。今後もスクリプト・長文ファイルの作成は bash heredoc / Python write_bytes を第一選択とすることを推奨。

### (d-6) git 状態・commit_push.bat について

本コミットは新規ファイル追加〔outputs 配下スクリプト・バックアップ・handoff〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-19 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/・遍照発揮性霊集.docx）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。なお commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。

### (d-7) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 20 後で 全角〔/〕883/883 balanced。retrofit 20 の追加部分は全角角括弧 31 対・かぎ括弧 10 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5)・retrofit 19 §(d-7) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔763 件・m1-m744 + sg01-sg19・2,650,402 bytes・schema_history 78 件〕
- 本 retrofit build script：`outputs/retrofit20_shoji_jisso.py`〔dry-run + 本番適用の二段運用〕
- 補注 T 追加 script：`outputs/add_chunote_t_retrofit20.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit20.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit20.json`〔retrofit 前 motifs.json・2,644,758 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit20.md`〔retrofit 前・187,184 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit20.md`〔retrofit 前・294,976 bytes〕
  - `outputs/commit_message_backup_pre_retrofit20.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-22_retrofit19_complete.md`〔顕密二教 教学体系軸連動〕
- 補注 T 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 20 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-19 完走 → 2026-05-22 retrofit 20 完走〔声字実相 教学系軸連動・新規 sg19「五大皆有響」+ 既存 m525 を書き下し anchor 単独採用・強連動 3 件（m521/m523/m524）・連動軸十五系統並立に到達・教学系軸の第三例・単独 anchor 体制 第五例〕。本体 motifs.json は 763 件・2,650,402 bytes・schema_history 78 件。motifs_index_design.md §2 に補注 T 追加〔補注 A-T 全 20 件 intact・200,245 bytes〕。CLAUDE.md は 304,043 bytes〔retrofit 4-20 全エントリ intact〕。連動軸十五系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）、五大皆有響 sg19/m525（単独）〕の anchor 自己参照タグ運用が完全整合に到達。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教 の二例、教学系軸は retrofit 20 声字実相 が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit20_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit19_complete.md`〔retrofit 19 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-T 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・763 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 20 commit です。

【本セッションの選択肢】
(A) retrofit 21 候補〔教学系軸：大日経疏 vol1 浄菩提心軸／即身成仏義 六大四曼三密軸／吽字義 等〕
(B) kaimyo-app 教学系素材活用：連動軸十五系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用
- 候補スキャンは仮名遣い・送り仮名のゆれを考慮し複数表記形でスキャンする〔retrofit 20 §(d-2)〕
- 単独 anchor 体制（補注 J/N/P/R/S/T 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-22〔retrofit 20 完走・声字実相 教学系軸連動 retrofit。新規 sg-id `sg19`「五大皆有響」を新設〔出典:声字実相義〕、書き下し anchor として既存 m525 を単独採用（声字実相義 第四節・四句頌「五大にみな響あり、十界に言語を具す、六塵ことごとく文字なり、法身はこれ実相なり」）。強連動 3 motif：m521（第一節 綱領）/ m523（第二節 三義定義）/ m524（第三節 阿字声字釈）に「連動:sg19」「連動:m525」を付与（+8 タグ・補注 J/N/P/R/S 単独 anchor 運用継承）。total_motifs 762→763（+1 新規 sg19）・famous_phrases 18→19。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,650,402 bytes〔+5,644〕・schema_history 78 件〔+1・origin: retrofit_20:doctrine〕・補注 T 追加〔motifs_index_design.md §2・187,184→200,245 bytes・+13,061〕・CLAUDE.md 更新完了〔294,976→304,043 bytes〕・commit_message.txt 書き換え済。連動軸十五系統並立に到達。教学体系軸（retrofit 18 十住心・retrofit 19 顕密二教）に続く教学系軸の第三例で空海 三部書 声字実相義 の言語哲学軸。単独 anchor 体制の運用第五例。小規模 retrofit の第五例（4 motif）。m524 が sg08/sg19 二系統連動の多系統連動 motif（強連動 motif の多系統所属 第一例）。声字実相義 第五節 真言論・第六節 色塵論を温存。Phase D 必須チェックリストに完全準拠する第十二の retrofit〕

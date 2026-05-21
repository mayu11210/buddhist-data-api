# 引き継ぎメモ：retrofit 19 完走〔顕密二教 教学体系軸連動 retrofit〕

**日付**：2026-05-22
**フェーズ**：retrofit 19（retrofit 18 完走に続く第十六の retrofit セッション）
**対象**：空海の教判の根幹「顕密二教」の連動軸新設。新規 sg-id `sg18`「顕密二教」を追加し、書き下し anchor として既存 m571（弁顕密二教論 巻上 第二章 本論 第一節 問答決疑・「問う、顕密二教その別いかん。答う、他受用・応化身の随機の説これを顕といい、自受用・法性仏、内証智の境を説きたもう、これを秘と名づく」顕と密の別を問答で端的に定義する顕密判の核心句）を **単独採用**。強連動 3 motif（m567 序説 大意序 / m588 巻下 引証喩釈 喩釈総括 / m593 顕密分斉）に連動タグを付与。連動軸十四系統並立に到達。本 retrofit は retrofit 18 十住心 に続く **教学体系軸の第二例**。retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心 同型の **単独 anchor 体制の運用第四例**。anchor 1 + 強連動 3 = 4 motif の **小規模 retrofit 第四例**。
**ステータス**：完走〔Phase A 候補スキャン＋軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 8 項目全 pass・Phase D 補注 S 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 20 候補〔教学体系軸：大日経疏 vol1 内部体系軸／声字実相義 五大皆有響軸 等〕／kaimyo-app 教学系素材活用／W1 buddhist-shoryoshu-workshop 継続抽出／W2 repo 凍結手続 から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔整合性検証 8 項目全 pass〕
- [x] schema_history 追記済〔origin: retrofit_19:doctrine〕
- [x] motifs_index_design.md に補注 S 追加済〔補注 A-S 全 19 件 intact・175,046→187,184 bytes〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行・285,989→294,976 bytes〕
- [x] commit_message.txt 書き換え済〔retrofit 19 用・冒頭行整合確認済〕
- [x] handoff_2026-05-22_retrofit19_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] stats recompute 差分全ゼロ確認（retrofit 18 補正済 stats が drift ゼロのまま継承）

---

## (a) 本セッションの位置づけ

retrofit 18 完走〔十住心 教学体系軸連動・新規 sg17 + 既存 m599 を書き下し anchor 単独採用・commit `1be6181`〕に続く第十六の retrofit セッション。

retrofit 18 完走 handoff §(c) 選択肢 A〔retrofit 19 候補：弁顕密二教論 顕密判軸（m571 anchor）〕に着手。ケンシン裁定で顕密二教軸を新設する方針を採用し、Phase A〜D を 1 commit にまとめて完走。

**本 retrofit の特徴**：

- 新規 sg-id `sg18`「顕密二教」を追加〔出典:弁顕密二教論・空海が応化身の随機説（顕教）と法身大日如来の内証自境説（密教）とを判別する教判の根幹・『弁顕密二教論』二巻の論題〕
- 書き下し anchor は m571 単独（弁顕密二教論 巻上 第二章 本論 第一節 問答決疑・顕密判の定義問答）
- 強連動 3 motif（m567 序説 大意序 / m588 巻下 引証喩釈 喩釈総括 / m593 顕密分斉）に「連動:sg18」「連動:m571」を付与（+8 タグ）
- 連動軸十四系統並立に到達
- **教学体系軸の第二例**（retrofit 18 十住心 に続く）
- **単独 anchor 体制の運用第四例**（retrofit 14 多宝塔・retrofit 16 長者窮子・retrofit 18 十住心 に続く）
- **小規模 retrofit の第四例**（4 motif・retrofit 14 多宝塔・retrofit 18 十住心 と同規模）

---

## (b) 本セッションの主な成果

### Phase A：候補スキャン＋軸設計合意

retrofit 18 完走 handoff §(c) 選択肢 A に着手。Phase A スキャンで「顕密二教」「顕密」および周辺キーワード（顕教・密教・顕乗・密乗・他受用・自受用・随機の説・内証智・応化身・法性仏 等）の kakikudashi 直接含有を全 761 motif にわたり網羅検査：

| 成句含有 | motif | 系統 |
|---|---|---|
| 「顕密二教」直接含有（成句そのもの） | m571・m588 | いずれも弁顕密二教論 |
| 「顕密」直接含有（短縮形） | m277・m278（性霊集 idx=105 泰範代筆書状）・m503（般若心経秘鍵 第十節）・m593（弁顕密二教論 巻下 顕密分斉） | 性霊集・般若心経秘鍵・弁顕密二教論 |

成句「顕密二教」自体の直接含有は弁顕密二教論 内部の m571・m588 の 2 件に集中し、短縮形「顕密」も含めても顕密判の中核は弁顕密二教論 内部にある。顕密二教判は弁顕密二教論 二巻の論題そのものであり、anchor は同論内部に求めるのが自然形。ケンシン裁定で判断 1-5：

- **判断 1**：中心成句 sg18 =「顕密二教」（4 字成句・弁顕密二教論の論題そのもの・m571/m588 が kakikudashi 直接含有）
- **判断 2**：書き下し anchor = m571 単独採用（単独 anchor 体制・retrofit 14/16/18 同型 第四例）
- **判断 3**：強連動 = 弁顕密二教論 内部限定（anchor m571 + 強連動 3 件 = 計 4 motif）
- **判断 4**：強連動 3 件 = m567（序説 大意序）/ m588（巻下 引証喩釈 喩釈総括）/ m593（顕密分斉）
- **判断 5**：単独 anchor タグ運用 = 補注 J/N/P/R 案 A 単独版（全 motif に「連動:sg18」「連動:m571」の 2 タグ付与）

### Phase B：4 motif 判定表

| m-id | 出典 | 役割 |
|---|---|---|
| m571 | 弁顕密二教論 巻上 第二章 本論 第一節 問答決疑 | 書き下し anchor（単独・自己参照）・「問う、顕密二教その別いかん。答う……」顕と密の別を問答で端的に定義する顕密判の定義句 |
| m567 | 弁顕密二教論 巻上 第一章 序説（大意序） | 強連動・「それ仏に三身あり、教はすなわち二種なり。応化の開説を名づけて顕教という……これを密教という」三身説による顕密二教の大綱・論冒頭の総説 |
| m588 | 弁顕密二教論 巻下 第二章 本論 第二節 引証喩釈（十五）分別聖位経 喩釈 | 強連動・「顕学の智人みな法身は説法せずという。この義しからず。顕密二教の差別かくのごとし」諸経の引証を承けて法身説法を確証する巻下の喩釈総括 |
| m593 | 弁顕密二教論 巻下 第二章 本論 第四節 顕密分斉 | 強連動・「顕密の義重々無数なり……一には衆生秘密、二には如来秘密なり」顕と密の境界の重層性を二義で整理 |

体系内連節カバー：序説 大意序（m567）→ 本論 定義問答（m571 anchor）→ 巻下 引証喩釈総括（m588）→ 顕密分斉（m593）の弁顕密二教論 内部四節を一括包摂。

**除外・温存**：m585（弁顕密二教論 巻下 引証喩釈（十四）五秘密経・『金剛頂五秘密経』丸ごと引用）は経証 motif として除外〔retrofit 5 m698・retrofit 6 m712・retrofit 7 m632/m635 以来の経証〔経文引用＋問題提起〕除外原則の継続適用〕。引証喩釈系 m576/m577（華厳五教章・大乗法苑義林章の引証喩釈）・性霊集 m277/m278（idx=105 泰範代筆書状）・般若心経秘鍵 m503（第十節）は「主題:顕密二教」タグ保持により別途検索可能なため温存。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 761 | 762 | +1（sg18 新規追加） |
| famous_phrases | 17 | 18 | +1 |
| ファイルサイズ | 2,639,066 bytes | 2,644,758 bytes | +5,692 |
| schema_history | 76 | 77 | +1（origin: retrofit_19:doctrine） |
| 連動タグ総数 | — | — | +8（m571/m567/m588/m593 各 +2） |
| kakikudashi_chars_total | 112,811 | 112,815 | +4（「顕密二教」4 字） |
| gendaigoyaku_chars_total | 313,217 | 314,650 | +1,433（sg18 description） |

**整合性検証 8 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 762 vs 762 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[]、count=744 ✓ |
| 3 | NUL バイト 0 件 | any=0, trailing=0 ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔4 motif × 2 tags〕 | missing=[] ✓ |
| 7 | sg18 配列末尾追加・sg01-sg18 連番 | ✓ |
| 8 | stats recompute 差分全ゼロ | kaki=0, gg=0, gabun=0, mwg=0 ✓ |

retrofit 18 で recompute 補正した stats は retrofit 19 着手時点で全 6 項目 drift ゼロを確認（baseline recompute 一致）。retrofit 19 では stats を全件 recompute して真値を書き込み（total_motifs 762・famous_phrases 18・kakikudashi_chars_total 112,815・gendaigoyaku_chars_total 314,650・gendai_gabun_chars_total 154,931・motifs_with_gendai_gabun 743）。top-level generated_at を 2026-05-22T00:00:00+09:00 に更新。motifs.json は `json.dumps(ensure_ascii=False, indent=2)` の round-trip 完全一致を事前確認のうえ編集。

### Phase D：補注 S 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 S〔顕密二教 教学体系軸連動の運用〕新規追加（175,046→187,184 bytes・+12,138・補注 A-S 全 19 件 intact・全角括弧 68/68 balanced・〔〕18/18 balanced・半角括弧 0 件）。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 19 完走エントリを追加（285,989→294,976 bytes・retrofit 4-19 全エントリ intact・追加部分の全角括弧 5/5・〔〕31/31 balanced・新規半角括弧 0 件）。
- `commit_message.txt` を retrofit 19 用に書き換え（冒頭行整合確認済）。
- handoff_2026-05-22_retrofit19_complete.md 作成（本ファイル）。

### 設計上の新規ポイント

#### 1. 教学体系軸の第二例

retrofit 18 十住心軸は法華経 譬喩・場面別軸（retrofit 10-17 八段構成）から空海教学の体系軸への転換 第一例であった。retrofit 19 顕密二教軸はその継続で教学体系軸の第二例。十住心が衆生の心の浅深を十段に体系づけた **縦軸の体系** であるのに対し、顕密二教判は一切の仏教を顕・密の二教に判別する **横軸の教判** であり、両者は九顕一密（初九住心＝顕・第十秘密荘厳心＝密）において交わる。

#### 2. 連動軸十四系統並立に到達

〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）〕の十四系統並立に到達。kaimyo-app は教学テーマ・空海教学の体系総覧（十住心）に加えて、顕教・密教の弁別駆動辞書（顕密二教）でも素材プールを切替可能。

#### 3. 単独 anchor 体制の運用第四例

retrofit 14 多宝塔 sg13/m424・retrofit 16 長者窮子 sg15/m717・retrofit 18 十住心 sg17/m599 に続く第四の単独 anchor 体制。顕密二教判の定義句は m571 の問答決疑が単一の核心句であり、成句「顕密二教」を kakikudashi に直接含有する motif が弁顕密二教論 内部に集中する（m571・m588）ため、典籍系統対比型の二重 anchor を要さず単独 anchor が自然形となる。論冒頭の有名な総説 m567 は「顕密二教」を kakikudashi に直接含有しない（「顕教」「密教」「密蔵」「顕略」を含む）ため anchor ではなく強連動に位置づけた。

#### 4. 小規模 retrofit の第四例・経証除外原則の継続適用

anchor 1 ＋ 強連動 3 ＝ 4 motif は retrofit 14 多宝塔・retrofit 18 十住心（各 4 motif）と同規模。論の骨格を成す序説・本論定義・引証喩釈総括・顕密分斉の四節に絞り、引証喩釈系 motif・経証 motif・他典籍系統 motif を温存または除外することで自然に小規模化した。m585（『金剛頂五秘密経』丸ごと引用）を経証 motif として除外したのは retrofit 5/6/7/8 以来の経証除外原則の継続適用。

### 検証結果

```
[整合性検証 8 項目]
1. total_motifs(stats)=array_len=762  OK
2. m-id range m1-m744 continuous count=744  OK
3. NUL bytes any=0 trailing=0  OK
4. schema_version=0.2  OK
5. required fields complete  OK
6. 連動タグ 4 motif x 2 tags 全付与  OK
7. sg list sg01-sg18 continuous, tail=sg18  OK
8. stats recompute 差分 kaki=0 gg=0 gabun=0 mwg=0  OK

[stats（retrofit 19 後）]
total_motifs=762  famous_phrases=18
kakikudashi_chars_total=112,815
gendaigoyaku_chars_total=314,650
gendai_gabun_chars_total=154,931
motifs_with_gendai_gabun=743
schema_history=77 entries
file size=2,644,758 bytes
```

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 20〔教学体系軸の継続〕

- **大日経疏 vol1 内部体系軸**：浄菩提心・十地・百六十心 等の内部節点の体系軸化。ただし三句法門 sg07・阿字本不生 sg08 と一部重複するため、重複しない節点に絞り込む設計が要。
- **声字実相義 五大皆有響軸**：「五大に皆な響きあり」を中心成句に、声字実相義 の motif を体系軸化する候補。
- 他の教学系著作（菩提心論 三摩地戒・即身成仏義 六大四曼三密 等）の体系軸化候補。

### 選択肢 B：kaimyo-app 教学系素材活用

連動軸十四系統 anchor 完全整合済の素材プールを kaimyo-app で活用。sg18 顕密二教は顕教・密教の弁別を駆動する辞書として、戒名・諷誦文・引導文の硬軟段階選択（顕教的表現／密教的表現）に直結。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残篇から motif 抽出を W1 workshop で継続。

### 選択肢 D：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop（W2）の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 顕密二教 直接含有 motif の典籍分布

成句「顕密二教」の kakikudashi 直接含有は弁顕密二教論 m571・m588 の 2 件に集中し、短縮形「顕密」を含めても m277/m278（性霊集）・m503（般若心経秘鍵）・m593（弁顕密二教論）の 4 件にとどまる。顕密判が弁顕密二教論 の論題そのものであることを反映し、本軸は弁顕密二教論 内部限定の単独 anchor 構成が自然形となった。性霊集 m277/m278・般若心経秘鍵 m503 は「主題:顕密二教」タグで別途検索可能であり、将来 retrofit で多典籍系統に拡張する余地は残る。

### (d-2) motifs_without_gendai_gabun_intentional の "sg01-sg07" キーが stale

motifs.json の stats.motifs_without_gendai_gabun_intentional に "sg01-sg07" キーがあるが、sg08-sg18 が追加された現在も未更新（retrofit 6 で sg06→sg07 に更新されて以降、retrofit 8-19 で sg08-sg18 を追加しても未更新）。これは stats の数値項目ではなく説明ラベルのため整合性検証 8 項目の対象外であり、retrofit 5-19 一貫して未更新の pre-existing 事象。retrofit 19 でも踏襲し未変更とした。将来 "sg01-sg18" 等への補正を検討（数値 stats ではないため drift 補正の対象とは別扱い）。

### (d-3) Edit/Write tool の truncate 事象が retrofit 19 でも再発

ビルドスクリプト `outputs/retrofit19_kenmitsu.py` を Write tool で作成した際、ファイル末尾が truncate される事象が発生（handoff §(d-5) 既知事象）。Edit tool による末尾修復も再度 truncate された。最終的に **bash heredoc（`cat > file <<'PYEOF' … PYEOF`）による書き込み** で確実に作成。retrofit 19 のスクリプト・補注 S・commit_message.txt・本 handoff はすべて bash heredoc または Python write_bytes 方式で作成し、truncate 事象を回避。今後もスクリプト・長文ファイルの作成は bash heredoc / Python write_bytes を第一選択とすることを推奨。

### (d-4) m639 の「顕教」kakikudashi 含有について

m639（秘蔵宝鑰 巻の下 第八章 一道無為心 第三節）は kakikudashi に「諸の顕教に於ては……真言門に望むれば」と顕密判の運用を含むが、成句「顕密二教」「顕密」自体は直接含有しないため kakikudashi 直接含有基準で本 retrofit の対象外とした。m639 は既に sg09 諸法実相・sg16 従地涌出 の二系統 anchor として運用されており、将来 retrofit で顕密判への関与を追補する場合は多系統 anchor・連動の拠点となりうる（本 retrofit では弁顕密二教論 内部四節に絞ったため対象外）。

### (d-5) git 状態・commit_push.bat について

本コミットは新規ファイル追加（outputs 配下スクリプト・バックアップ・handoff）と既存ファイル更新（motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt）のみで、削除はなし。commit_push.bat の SAFETY CHECK（deleted 検出 → 中止ガード）は発動しない見込み。bash mount 経由 git 書き込みは禁止のため、commit/push は commit_push.bat のダブルクリックでケンシン側が実行する。git status --short には retrofit 4-18 由来の未追跡ファイル（outputs 配下スクリプト・バックアップ群・_dev_scripts/）が多数残存しているが、これは過去 retrofit と同型の状態で commit 対象に含まれる。 なお bash サンドボックスから git status 実行時に `.git/index.lock` を unlink できない警告が出るが、これは retrofit 14-17 §(d-9) で記録された既知の git index 異常の継続であり、commit 履歴自体は intact。ケンシン側で cleanup 系 bat の実行により整理可能。また commit_message.txt は .gitignore 対象（`git commit -F commit_message.txt` のソースファイル・追跡対象外）のため git diff には現れない。

### (d-6) 編集手法

motifs.json・motifs_index_design.md・CLAUDE.md・commit_message.txt の更新はいずれも Python script による read → in-memory 編集 → write back 方式、またはスクリプト本体は bash heredoc 方式で作成。motifs.json は json round-trip 完全一致を事前確認のうえ json.loads/json.dumps（ensure_ascii=False, indent=2）で編集。全ファイル NUL 0 件確認済。

### (d-7) CLAUDE.md の括弧 pre-existing 差分

CLAUDE.md は retrofit 19 後で 全角〔/〕821/821 balanced。全角の丸括弧は 1183/1184〔差分 -1〕、半角の丸括弧は 284/287〔差分 -3〕の pre-existing 差分があるが、retrofit 19 の追加部分は全角丸括弧 5 対・全角角括弧 31 対がいずれも balanced、新規半角括弧 0 件で内部完全バランスである〔retrofit 17 §(d-5) で記録された CLAUDE.md pre-existing 括弧差分の継続・追加部分が balanced であれば許容する運用〕。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔762 件・m1-m744 + sg01-sg18・2,644,758 bytes・schema_history 77 件〕
- 本 retrofit build script：`outputs/retrofit19_kenmitsu.py`〔dry-run + 本番適用の二段運用〕
- 補注 S 追加 script：`outputs/add_chunote_s_retrofit19.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit19.py`
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit19.json`〔retrofit 前 motifs.json・2,639,066 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit19.md`〔retrofit 前・175,046 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit19.md`〔retrofit 前・285,989 bytes〕
  - `outputs/commit_message_backup_pre_retrofit19.txt`〔retrofit 前 commit_message.txt〕
- 前 retrofit handoff：`handoff_2026-05-21_retrofit18_complete.md`〔十住心 教学体系軸連動〕
- 補注 S 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕・§7〔必須検証項目〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 19 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 W2 本体マージ完走 → retrofit 4-18 完走 → 2026-05-22 retrofit 19 完走〔顕密二教 教学体系軸連動・新規 sg18「顕密二教」+ 既存 m571 を書き下し anchor 単独採用・強連動 3 件（m567/m588/m593）・連動軸十四系統並立に到達・教学体系軸の第二例・単独 anchor 体制 第四例〕。本体 motifs.json は 762 件・2,644,758 bytes・schema_history 77 件。motifs_index_design.md §2 に補注 S 追加〔補注 A-S 全 19 件 intact・187,184 bytes〕。CLAUDE.md は 294,976 bytes〔retrofit 4-19 全エントリ intact〕。連動軸十四系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636、良医病子 sg11/m44+m70、化城宝処 sg12/m227+m569、多宝塔 sg13/m424（単独）、三草二木 sg14/m215+m636、長者窮子 sg15/m717（単独）、従地涌出 sg16/m639+m690（系統対比型）、十住心 sg17/m599（単独）、顕密二教 sg18/m571（単独）〕の anchor 自己参照タグ運用が完全整合に到達。法華経 譬喩・場面別軸は retrofit 17 の八段構成をもって完成体。教学体系軸は retrofit 18 十住心・retrofit 19 顕密二教 の二例が並立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-22_retrofit19_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-21_retrofit18_complete.md`〔retrofit 18 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D-S 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・762 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 19 commit です。

【本セッションの選択肢】
(A) retrofit 20 候補〔教学体系軸：大日経疏 vol1 内部体系軸／声字実相義 五大皆有響軸 等〕
(B) kaimyo-app 教学系素材活用：連動軸十四系統 anchor 完全整合済の素材プール活用
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残篇から motif 抽出
(D) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集・スクリプト作成は bash heredoc または Python write_bytes 方式を採用〔Edit/Write tool truncate 事象回避・retrofit 19 で再発確認済〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 整合性検証は stats recompute 差分チェックを含む 8 項目で運用〔retrofit 18 で追加〕
- 単独 anchor 体制（補注 J/N/P/R/S 案 A 単独版）と二重 anchor 体制（補注 K/L/M/O/Q 案 A 二重版）は anchor の典籍系統的分布に応じて柔軟に選択
- Phase D 必須チェックリストに従う〔commit_message.txt 更新は必須項目〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-22〔retrofit 19 完走・顕密二教 教学体系軸連動 retrofit。新規 sg-id `sg18`「顕密二教」を新設〔出典:弁顕密二教論〕、書き下し anchor として既存 m571 を単独採用（弁顕密二教論 巻上 第二章 本論 第一節 問答決疑・顕密判の定義句）。強連動 3 motif：m567（序説 大意序）/ m588（巻下 引証喩釈 喩釈総括）/ m593（顕密分斉）に「連動:sg18」「連動:m571」を付与（+8 タグ・補注 J/N/P/R 単独 anchor 運用継承）。total_motifs 761→762（+1 新規 sg18）・famous_phrases 17→18。schema 0.2 維持・整合性検証 8 項目全 pass。本体 motifs.json 2,644,758 bytes〔+5,692〕・schema_history 77 件〔+1・origin: retrofit_19:doctrine〕・補注 S 追加〔motifs_index_design.md §2・175,046→187,184 bytes・+12,138〕・CLAUDE.md 更新完了〔285,989→294,976 bytes〕・commit_message.txt 書き換え済。連動軸十四系統並立に到達。教学体系軸の第二例（retrofit 18 十住心 に続く）。単独 anchor 体制の運用第四例。小規模 retrofit の第四例（4 motif）。経証 motif m585 除外・引証喩釈系 m576/m577・他典籍系統 m277/m278/m503 温存。Phase D 必須チェックリストに完全準拠する第十一の retrofit〕

# handoff 2026-06-25 — 大日経疏 巻第二十 Phase3 motif 抽出＋retrofit＋gabun 完走（push2）／**T1796 全20巻 motif 完結**

## 到達点
`data/indices/motifs.json` に巻第二十の motif を **m3959-m4041（83件）** 追記し、連動軸 retrofit と gabun 裁定まで完走。
motif 全工程を **1 push（push2）** に集約。**total 3989→4072**・schema_history **293→295**（round_all＋retrofit 各1）。
`commit_message.txt` 更新済み・**`commit_vol20_push2.bat` 実行待ち**。HEAD 起点：6c7c039（push1）。

- **これにより大日経疏 全20巻 corpus/genten/横断索引/motif 完備（最終巻）**。

## Phase A 合意（巻第二〜十九 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全件 `引用形式:典籍曰く`・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第二十`／`引用形式:典籍曰く`。
- 1段=1motif（束ねなし）・gabun 意図的未設定・連動軸は完走後 retrofit。構造段 k001/k002/k003/k028/k039/k050/k067 は motif 化せず。
- **節は corpus の paragraphs[].section から直接取得**し、節==corpus.section を全83件 assert。
- **囑累品の種子字段 k080（doc 埋込画像 image1.png 本文転記）は motif 化する（ケンシン裁定・vol18 百字生品 種字段 precedent）**。

## 内訳（核心15件・新運用＝判定表全件まとめて提示→確認後 round_all で一括処理）
| 品 | 範囲 | m-id | 件 | 核心 |
|---|---|---|---|---|
| 世出世護摩法品第二十七之余 | k004-k027 | m3959-m3982 | 24 | m3962 火の自性＝如来一切智光／m3973 内護摩三和合 本尊即火即自身／m3975 大悲の忿怒で煩悩薪を焼く |
| 本尊三昧品第二十八 | k029-k038 | m3983-m3992 | 10 | m3986 字の二種と阿字の首／m3992 縁起観より般若の洗滌へ頓入仏果 |
| 無相三昧品第二十九 | k040-k049 | m3993-m4002 | 10 | m3994 三平等への観の開示／m4002 三平等の法門に入り真言実相を証し如来と同じ |
| 世出世持誦品第三十 | k051-k066 | m4003-m4018 | 16 | m4007 菩提心観＝心即仏自身即仏／m4011 三事平等 字即本尊即心即法界体性／m4016 三句法門と三落叉の相応 |
| 囑累品第三十一 | k068-k090 | m4019-m4041 | 23 | m4027 八葉皆大日如来一体／m4029 五仏阿字五転と方便普門法界身／m4032 一切尊皆大日如来に帰す／m4037 我即法界毘盧遮那の諦信 |

- ※ 囑累品 m4031（k080）＝**諸尊の種子字と五転〔金剛手嚩/蓮花尊娑/文殊麼〕**＝doc 埋込画像転記段（種子字割注化）。
- 判定表ドラフトはサブエージェント2体（g1=護摩之余+本尊三昧+無相三昧／g2=持誦品+囑累品）→本体で正規化（軸ずれ・主題:本生→文体:譬喩・潅頂→灌頂・核心 厳選）→ケンシン裁定「このまま処理」で確定。判定表は `_dev_references/dainichikyo-sho-vol20_build/motif_table_g1.json`／`motif_table_g2.json`。
- **新タグ値4（既存軸内）**：`主題:不放逸`（k068「不放逸に住すべし」）／`主題:付属`（囑累＝付属の品）／`主題:邪正`（護摩品の邪正の弁）／`典故:普賢観経`（k075）。文体 語釈57/譬喩16/列挙6/問答5/陳述4。

## 連動軸 retrofit（タグのみ・total 不変・ケンシン裁定 sg 新設なし）
- 新規 sg/anchor なし＝既存軸の被覆拡張（巻第二〜十九 retrofit 同型）。core verbatim に限定し 6 件に +14 連動タグ：
  - sg07 三句法門〔m713〕← m4016（k064 菩提心種子＝因・大悲為根・方便為究竟＝大日経 住心品 三句 verbatim・**強連動**）／m4024（k073 三句を問う＝菩提心種子・大悲根・方便後）
  - sg08 阿字本不生〔m549〕← m4002（k049 三事縁生＝不生不滅＝阿字門・法界性）／m4009（k057 当に本来不生に住すべし＝心これなり）
  - sg21 浄菩提心〔m638+m728〕← m3994（k041 浄菩提心の初法明門に入る・**強連動**）／m4033（k082 此の地は即ち是れ浄菩提心）
- sg27 自心本性清浄 は vol20 に core verbatim 直結なく見送り（温存）。origin: retrofit:dainichikyo-sho-vol20_rendou_scan。

## gabun 裁定
- vol20 全83 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十九 同運用）。`motifs_without_gendai_gabun_intentional` に `dainichikyo-sho-vol20_round_all` 記載。

## 検証（全 pass）
- NUL0／JSON再パースOK／m-id 連番 m1-m4041 missing=[] dup=False／total=配列 4072／sg31・famous31／vol20 83件 全件 典籍曰く・大師系0・半角括弧0（kk/gd/tags）／kk・gd recompute drift 0／verbatim 一致（節=corpus section 一致）／from_corpus_vol20=83／核心15／schema_version 0.2・schema_history 295。
- 巻き戻り assert：m506 典籍曰く／vol19 m3878-m3958（from_corpus_vol19=81）／from_corpus_vol18=45／anchor m549 連動:sg08・m719 連動:sg27 温存。
- ホスト Grep：CLAUDE.md line1 に push2 ★エントリ反映確認。バックアップ `_dev_references/dainichikyo-sho-vol20_build/motifs_backup_pre_vol20_motif.json`／`_pre_vol20_retrofit.json`。

## push（push2）
- 変更ファイルは `data/indices/motifs.json`＋`CLAUDE.md`＋本 handoff＋`_dev_references/dainichikyo-sho-vol20_build/`（motif_table 等）のみ。commit_message.txt／bat は gitignore（add しない）。
- **`commit_vol20_push2.bat`**（専用・幻の削除回避・git reset HEAD→対象パスのみ stage→build dir の source.doc/docx と LibreOffice junk を reset 除外→staged 削除ガード→commit→push→Step8 で total_motifs 4072 の HEAD 在否確認）。標準 commit_push.bat は使わない。
- push 後は `git show HEAD:data/indices/motifs.json` で total_motifs 4072・最終 m4041 を確認。

## 残（push3）＋全20巻完了の残課題
- **kaimyo-app 同期**：別リポジトリ（接続済み・HEAD a3f6138）。motifs.json を kaimyo-app/data/indices/motifs.json にコピー・NUL0／total 4072／引用形式:典籍曰く 反映確認・SHA-256 一致。冠は source.著作名 フォールバックで「大日経疏 巻第二十に曰く、」＝新引用形式タグなしのためコード変更なし見込み。`commit_motifs_sync.bat`／`commit_message_motifs_sync.txt`。
- **全20巻 完結に伴う最終確認（push3 の handoff に記録）**：
  - 全巻 genten 完備（巻一〜二十 全て genten 投入済・manifest genten_present=29）。
  - 連動軸 sg 新設は全巻通して「なし」（既存軸被覆拡張のみ）で一貫。
  - 大日経疏 全20巻 motif 件数の総括（巻別 motif 数・核心・連動軸）を push3 handoff にまとめる。

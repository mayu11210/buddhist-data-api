# handoff 2026-06-25 — 大日経疏 巻第十九 Phase3 motif 抽出＋retrofit＋gabun 完走（push2）

## 到達点
`data/indices/motifs.json` に巻第十九の motif を **m3878-m3958（81件）** 追記し、連動軸 retrofit と gabun 裁定まで完走。
motif 全工程を **1 push（push2）** に集約。**total 3908→3989**・schema_history **291→293**（round_all＋retrofit 各1）。
`commit_message.txt` 更新済み・`commit_vol19_push2.bat` 実行待ち。HEAD 起点：04354da（push1）。

## Phase A 合意（巻第二〜十八 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全件 `引用形式:典籍曰く`・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十九`／`引用形式:典籍曰く`。
- 1段=1motif（束ねなし）・gabun 意図的未設定・連動軸は完走後 retrofit。構造段 k001/k002/k003/k027/k048/k056/k065/k078/k084 は motif 化せず。
- **節は corpus の paragraphs[].section から直接取得**し、節==corpus.section を全81件 assert。

## 内訳（核心13件・新運用＝判定表全件まとめて提示→確認後 round_all で一括処理）
| 品 | 範囲 | m-id | 件 | 核心 |
|---|---|---|---|---|
| 百字位成品第二十一 | k004-k026 | m3878-m3900 | 23 | m3891 縁生実相＝阿字法界／m3900 慧方便で大空壇（品結） |
| 百字成就持誦品第二十二 | k028-k047 | m3901-m3920 | 20 | m3906 浄空＝本不生＝菩提心／m3913 阿字＝不生不滅＝如来身／m3920 字義を識れば仏と成る（品結） |
| 百字真言法品第二十三 | k049-k055 | m3921-m3927 | 7 | m3926 一字に無量義＝如来自然智門 |
| 説菩提性品第二十四 | k057-k064 | m3928-m3935 | 8 | m3932 真言の義＝菩提／m3935 菩提性＝阿字門一切智の句（品結） |
| 三三昧耶行品第二十五 | k066-k077 | m3936-m3947 | 12 | m3941 三句法門／m3942 三宝一体＝三三昧耶／m3945 三平等＝菩提 |
| 明如来品第二十六 | k079-k083 | m3948-m3952 | 5 | m3949 菩薩・仏の名義（摩訶衍道）／m3951 如来・如去の名義 |
| 護摩法品第二十七 | k085-k090 | m3953-m3958 | 6 | 核心0 |

- 本文 k004-k090 全網羅。判定表ドラフトはサブエージェント2体（品21-23／品24-27）で作成→密度・新タグを精査（密教/主題 軸ずれ正規化・主題:本生 除去）→ケンシン裁定「このまま処理」で確定。判定表は `_dev_references/dainichikyo-sho-vol19_build/motif_table_b1.json`／`motif_table_b2.json`／`motif_table_refined.json`。
- 新タグ値4（既存軸内の値追加）：`出典:大日経疏 巻第十九`／`主題:真言救世者`（vol19 中心概念・2件）／`典故:月灯三昧経`（k023・gd『月灯三昧経』）／`典故:菩薩蔵経`（k081・gd『菩薩蔵経』）。
- 正規化：drafting agent の `密教:外道/大乗/字門/字輪相/無明/真言道/虚空/阿頼耶` を `主題:` へ寄せ（既存値再利用）・`密教:潅頂`→`密教:灌頂`・`主題:本生`→`文体:譬喩`（vol17/18 規約）。文体 内訳 語釈66/譬喩14/問答5/列挙5/陳述1。

## 連動軸 retrofit（タグのみ・total 不変）
- 新規 sg/anchor なし＝既存軸の被覆拡張（巻第二〜十八 retrofit 同型）。core verbatim に限定し 5 件に +11 連動タグ：
  - sg08 阿字本不生〔m549〕← m3913（k040 阿字＝我自身＝本不生無滅＝如来の身）／m3912（k039 阿字より一切真言門生じ不生の理を顕す）／m3921（k049 阿字＝本不生不可得空）
  - sg07 三句法門〔m713〕← m3941（k071 菩提心為因・大悲為根・方便為究竟＝大日経 住心品 三句 verbatim・強連動）
  - sg21 浄菩提心〔m638+m728〕← m3907（k034 虚空等心＝浄菩提心、従此浄菩提心而生大悲心）
- sg27 自心本性清浄 は vol19 に core verbatim 直結なく見送り（温存）。origin: retrofit:dainichikyo-sho-vol19_rendou_scan。

## gabun 裁定
- vol19 全81 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十八 同運用）。`motifs_without_gendai_gabun_intentional` に `dainichikyo-sho-vol19_round_all` 記載。

## 検証（全 pass）
- NUL0／JSON再パースOK／m-id 連番 m1-m3958 missing=[] dup=False／total=配列 3989／sg31・famous31／vol19 81件 全件 典籍曰く・大師系0・半角括弧0（kk/gd/tags）／kk・gd recompute drift 0／verbatim 一致（節=corpus section 一致）／from_corpus_vol19=81／核心13／schema_version 0.2・schema_history 293。
- 巻き戻り assert：m506 典籍曰く／vol18 m3877（corpus vol18）・from_corpus_vol18=45／from_corpus_vol17=88／anchor m549 連動:sg08・m719 連動:sg27 温存。
- ホスト Grep：total_motifs 3989・m3958 反映確認。バックアップ `_dev_references/dainichikyo-sho-vol19_build/motifs_backup_pre_vol19_motif.json`／`_pre_vol19_retrofit.json`。

## push（push2）
- 変更ファイルは `data/indices/motifs.json`＋`CLAUDE.md`＋本 handoff＋`_dev_references/dainichikyo-sho-vol19_build/`（motif_table 等）＋commit_message.txt のみ。
- **`commit_vol19_push2.bat`**（専用・幻の削除回避・git reset HEAD→対象パスのみ stage→build dir の source.doc/docx と LibreOffice junk を reset 除外→staged 削除ガード）。標準 commit_push.bat は使わない。**`git add` に gitignore 対象（bat・commit_message.txt）を入れない**。
- push 後は `git show HEAD:data/indices/motifs.json` で total_motifs 3989・最終 m3958 を確認（バット Step8 で自動確認）。

## 残（push3）
- kaimyo-app 同期：別リポジトリ（接続済み・HEAD 693e156）。motifs.json を kaimyo-app/data/indices/motifs.json にコピー・NUL0／total 3989／引用形式:典籍曰く 反映確認・SHA-256 一致。冠は source.著作名 フォールバックで「大日経疏 巻第十九に曰く、」＝新引用形式タグなしのためコード変更なし見込み。`commit_motifs_sync.bat`／`commit_message_motifs_sync.txt`。

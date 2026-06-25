# handoff 2026-06-25 — 大日経疏 巻第十八 Phase3 motif 抽出＋retrofit＋gabun 完走（push2）

## 到達点
`data/indices/motifs.json` に巻第十八の motif を **m3833-m3877（45件）** 追記し、連動軸 retrofit と gabun 裁定まで完走。
motif 全工程を **1 push（push2）** に集約。**total 3863→3908**・schema_history **289→291**（round_all＋retrofit 各1）。
`commit_message.txt` 更新済み・`commit_vol18_push2.bat` 実行待ち。HEAD 起点：1010c46（push1）。

## Phase A 合意（巻第二〜十七 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全件 `引用形式:典籍曰く`・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十八`／`引用形式:典籍曰く`。
- 1段=1motif（束ねなし）・gabun 意図的未設定・連動軸は完走後 retrofit。構造段 k001/k002/k003/k027/k037 は motif 化せず。
- **節は corpus の paragraphs[].section から直接取得**し、節==corpus.section を全45件 assert。

## 内訳（核心16件・新運用＝判定表全件まとめて提示→確認後 round_all で一括処理）
| 品 | 範囲 | m-id | 件 | 核心 |
|---|---|---|---|---|
| 受方便学処品第十八之余 | k004-k026 | m3833-m3855 | 23 | m3834 本性戒＝阿字門/m3847 本性清浄心/m3850 邪見即慧性/m3854 無漏性戒/m3855 四重根本・長者窮子 |
| 百字生品第十九 | k028-k036 | m3856-m3864 | 9 | m3856 真言王/m3858 暗字＝一切真言の心/m3859 真言導師＝救世者/m3863 清浄我＝毘盧遮那 |
| 百字果相応品第二十 | k038-k050 | m3865-m3877 | 13 | m3866 第十一地陀羅尼形/m3869 大空本不生/m3871 鏡像無相荘厳/m3873 遍法界の菩提/m3874 胎は阿字より生ず/m3875 正遍知の句・四無量/m3877 暗字悉地の果 |

- 本文 k004-k050 全網羅。判定表ドラフトはサブエージェントで作成→密度・新タグを精査（主題:本生 除去・典故:然灯仏 除去）→ケンシン裁定「このまま処理（リッチ寄り）」で確定。判定表は `_dev_references/dainichikyo-sho-vol18_build/motif_table_vol18.md`／`motif_table_refined.json`。
- 新タグ値57（既存軸内の値追加）：主題50（八戒名＋本巻固有の教義/場面語）・典故7（僧伽吒経/菩薩戒大本/長阿含/賢愚経/菩薩蔵本生/本生経/六根浄品）。主題:異方便・本性戒・阿字門・大空 等は既存値再利用。

## 連動軸 retrofit（タグのみ・total 不変）
- 新規 sg/anchor なし＝既存軸の被覆拡張（巻第二〜十七 retrofit 同型）。core verbatim に限定し 3 件に +6 連動タグ：
  - sg08 阿字本不生〔m549〕← m3869（k042 この一字は大空本不生に同じ・百字の身も亦た）／m3874（k047 如来性より生ず＝これ阿字より生ず）
  - sg27 自心本性清浄〔m719〕← m3847（k018 菩薩本性清浄心）
- sg26 一切智智／sg21 浄菩提心 は vol18 に core verbatim 直結なく見送り（温存）。origin: retrofit:dainichikyo-sho-vol18_rendou_scan。

## gabun 裁定
- vol18 全45 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十七 同運用）。`motifs_without_gendai_gabun_intentional` に `dainichikyo-sho-vol18_round_all` 記載。

## 検証（全 pass）
- NUL0／JSON再パースOK／m-id 連番 m1-m3877 missing=[] dup=False／total=配列 3908／sg31・famous31／vol18 45件 全件 典籍曰く・大師系0・半角括弧0（kk/gd とも）／kk・gd recompute drift 0／verbatim 一致（節=corpus section 一致）／from_corpus_vol18=45／核心16／schema_version 0.2・schema_history 291。
- 巻き戻り assert：m506 典籍曰く／vol17 m3832（corpus vol17）・from_corpus_vol17=88／from_corpus_vol16=66／anchor m549 連動:sg08・m719 連動:sg27 温存。
- ホスト Grep：m3877・total_motifs 3908 反映確認。バックアップ `_dev_references/dainichikyo-sho-vol18_build/motifs_backup_pre_vol18_motif.json`／`_pre_vol18_retrofit.json`。

## push（push2）
- 変更ファイルは `data/indices/motifs.json`＋`CLAUDE.md`＋本 handoff＋`_dev_references/dainichikyo-sho-vol18_build/`＋commit_message.txt のみ。
- **`commit_vol18_push2.bat`**（専用・幻の削除回避）を用意。標準 commit_push.bat は使わない。
- push 後は `git show HEAD:data/indices/motifs.json` で total_motifs 3908・最終 m3877 を確認（マウント同期遅延の再発防止。旧版なら補完コミットで是正）。

## 残（push3）
- kaimyo-app 同期：別リポジトリ。motifs.json を kaimyo-app/data/indices/motifs.json にコピー・NUL0／total 3908／引用形式:典籍曰く 反映確認・SHA-256 一致。冠は source.著作名 フォールバックで「大日経疏 巻第十八に曰く、」＝新引用形式タグなしのためコード変更なし見込み。要フォルダ接続。

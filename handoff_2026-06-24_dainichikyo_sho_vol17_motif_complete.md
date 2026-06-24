# handoff 2026-06-24 — 大日経疏 巻第十七 Phase3 motif 抽出 全6ラウンド＋retrofit＋gabun 完走（push2）

## 到達点
`data/indices/motifs.json` に巻第十七の motif を **m3745-m3832（88件）** 追記し、連動軸 retrofit と gabun 裁定まで完走。
新運用に従い **motif 全工程を1 push（push2）** に集約。**total 3775→3863**・schema_history **282→289**（R1-6 各＋retrofit 1）。
`commit_message.txt` 更新済み・`commit_vol17_push2.bat` 実行待ち。

## Phase A 合意（巻第二〜十六 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全件 `引用形式:典籍曰く`・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十七`／`引用形式:典籍曰く`。
- 1段=1motif（束ねなし）・gabun 意図的未設定・連動軸は完走後 retrofit。構造段 k001/k002/k003/k014/k036/k063/k065 は motif 化せず。
- **節は corpus の paragraphs[].section から直接取得**し、節==corpus.section を全88件 assert（vol16 の判定表ずれ事故の再発防止）。

## 6ラウンド（核心20件）
| R | 範囲 | m-id | 件 | 核心 |
|---|---|---|---|---|
| R1 秘密八印品第十四 | k004-k013 | m3745-m3754 | 10 | 1（八印=甚極秘密・神験感応 m3745） |
| R2 持明禁戒品第十五 | k015-k035 | m3755-m3775 | 21 | 5（制戒=正覚住 m3761／三平等・等引 m3762／如来無師の慧 m3764／瓦礫諸宝平等 m3765／一味の見 m3770） |
| R3 阿闍梨真実智品第十六 前半 | k037-k049 | m3776-m3788 | 13 | 3（阿=一切法本不生 m3778／字の理性=本不生 m3782／本不生を顕す m3787） |
| R4 同 後半 | k050-k062 | m3789-m3801 | 13 | 5（阿闍梨即如来 m3789／広大智阿闍梨 m3791／遍一切処・諸尊みな我 m3796／一百八号皆阿字 m3797／常住即仏 m3801） |
| R5 布字品第十七＋受方便学処品第十八 前半 | k064・k066-k080 | m3802-m3817 | 16 | 4（布字観・仏即一切智 m3802／自性本源の戒 m3806／真四重禁・捨佛断命 m3811／※k087 はR6） |
| R6 受方便学処品第十八 後半 | k081-k095 | m3818-m3832 | 15 | 4（一道法門=阿字門 m3821／大乗十善=一切法平等 m3824／方便殺・大悲心 m3829／※） |

- 新タグ値（既存軸内の値追加）：`典故:文殊経`／`典故:宝蔵経`／`典故:大方便経`（いずれも疏の文中引用に忠実）。密教は既存語彙を再利用（密教:灌頂に統一・密教:瑜伽は不採用で主題:瑜伽座へ）。本文 k004-k095 全網羅。

## 連動軸 retrofit（タグのみ・total 不変）
- 新規 sg/anchor なし＝既存軸の被覆拡張（巻第二〜十六 retrofit 同型）。core verbatim に限定し 4 件に +8 連動タグ：
  - sg08 阿字本不生〔m549〕← m3778（k039 阿=一切法本不生）／m3782（k043 字の理性=本不生）／m3787（k048 本不生の義より生じ本不生を解す）
  - sg26 一切智智〔m698〕← m3779（k040 巧妙智=一切智智の別名）
- sg21 浄菩提心／sg27 自心本性清浄 は vol17 に core verbatim 直結なく見送り（温存）。origin: retrofit:dainichikyo-sho-vol17_rendou_scan。

## gabun 裁定
- vol17 全88 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十六 同運用）。`motifs_without_gendai_gabun_intentional` に round1-6 記載済。

## 検証（全 pass）
- NUL0／JSON再パースOK／m-id 連番 m1-m3832 missing=[] dup=False／total=配列 3863／sg31／vol17 88件 全件 典籍曰く・大師系0・半角括弧0（kk/gd とも）／kk・gd recompute drift 0／verbatim 一致（節=corpus section 一致）／from_corpus_vol17=88／核心20／schema_version 0.2・schema_history 289。
- 巻き戻り assert：m506 典籍曰く／vol16 retrofit m3734 連動:sg08・m3720 連動:sg21／vol16 66件・vol15 78件 温存。
- ホスト Grep：m3832 反映確認。バックアップ outputs/vol17_motif/motifs_backup_pre_vol17_r1..r6.json／_pre_vol17_retrofit.json。build: _dev_references/dainichikyo-sho-vol17_build/build.py／tags.py。

## push（push2）
- 変更ファイルは `data/indices/motifs.json`＋`CLAUDE.md`＋本 handoff＋`_dev_references/dainichikyo-sho-vol17_build/`＋commit_message.txt のみ。
- **`commit_vol17_push2.bat`**（専用・幻の削除回避）を用意。標準 commit_push.bat は使わない。
- push 後は `git show HEAD:data/indices/motifs.json` で total_motifs 3863・最終 m3832 を確認（vol16 push2 のマウント同期遅延の再発防止）。旧版を掴んでいたら補完コミットで是正。

## 残（push3）
- kaimyo-app 同期：別リポジトリ。motifs.json を kaimyo-app/data/indices/motifs.json にコピー・NUL0／total 3863／引用形式:典籍曰く 反映確認・SHA-256 一致。冠は source.著作名 フォールバックで「大日経疏 巻第十七に曰く、」＝新引用形式タグなしのためコード変更なし見込み。要フォルダ接続。

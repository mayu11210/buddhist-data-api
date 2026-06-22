# 引き継ぎメモ — 大日経疏 巻第十三 Phase3 motif 抽出（全6ラウンド完走）＋連動軸 retrofit（2026-06-23）

genten 後送＋Phase2（commit `8b8a4f9`）に続けて Phase3 motif 抽出を全6ラウンドで完走し、連動軸 retrofit まで実施。残るは kaimyo-app 同期のみ。

## Phase A 合意（巻第十二踏襲）
著者=善無畏口述/一行筆受＝非空海 → 全件 `引用形式:典籍曰く`・大師系タグ非付与・`gabun 意図的未設定`。本体直接書込・ID は m3482 から連番。1段=1motif（束ねなし）。品題は motif 化せず。密印品は印相・真言字義が大半なので `文体:語釈`、`一句性:核心` は精選。各ラウンド判定表をケンシン承認の上で build。

## Phase3 成果（m3482-m3548・67 motif・total 3512→3579）
本文 k004-k071 全網羅（首題 k001／撰号 k002／品題 k003〔転字輪漫荼羅行品第八之余〕・k021〔密印品第九〕は除外）。

- **R1**（m3482-m3490・9）転字輪品之余 彩色と諸尊の図像 k004-k008＋漫荼羅造立と四大結護 k009-k012。核心1（m3484 阿字＝第一義諦）。新タグ 典故:大般若経（m3485）。
- **R2**（m3491-m3498・8）外漫荼羅と潅頂法 k013-k020。核心2（m3496 阿字＝法界体性／m3498 潅頂＝十方諸仏の法水法王位）。典故:法華経（m3495 開仏知見）。
- **R3**（m3499-m3510・12）密印品 如来身密印と三明真言 k022-k024／十二合掌と三昧耶印 k025-k028／転法輪印刀印法螺印坐印 k029-k033。核心3（m3501 三昧耶＝不可越・三法成就／m3505 我即法界／m3507 刀印＝大智・吽字本不生）。
- **R4**（m3511-m3522・12）如来の諸印と真言の字義 k034-k045。核心4（m3513 十力は大慈より生ず／m3514 仏眼＝大悲の空／m3519 大界＝発心より成仏まで間断せず／m3522 一字に無窮の義・一音説法）。
- **R5**（m3523-m3535・13）諸菩薩の印 前半 k046-k058。核心4（m3524 普賢＝三世の仏と等し／m3526 観音＝大悲を体／m3533 施無畏＝阿字門に住す／m3534 大慈＝自性清浄心より生ず）。
- **R6**（m3536-m3548・13・完走）諸菩薩の印 後半 k059-k066＋仏頂の諸印と諸天の印 k067-k071。核心2（m3541 金剛針＝諸法の源に達す／m3543 一切仏頂＝二縛を空・三空三昧）。

一句性:核心 計16件。新タグ値は 典故:大般若経／典故:法華経 のみ（密教は既存値再利用）。
build script：`outputs/build_motifs_vol13_r1.py`〜`r6.py`。バックアップ：`outputs/motifs_backup_pre_vol13_r1.json`〜`r6.json`。

## 連動軸 retrofit（新規 sg/anchor なし・タグのみ +12）
vol13 motif 6 件に連動タグ（直接連動・核心 verbatim 限定）。
- sg08 阿字本不生〔m549〕← m3507・m3511・m3515・m3533
- sg27 自心本性清浄〔m719〕← m3534・m3538

total 3579 不変・famous 31 不変。script：`outputs/retrofit_vol13_rendou.py`。バックアップ：`outputs/motifs_backup_pre_vol13_rendou.json`。

## gabun 裁定
vol13 全 67 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十二 同運用）。`stats.motifs_without_gendai_gabun_intentional` に `dainichikyo-sho-vol13_round_all` を記載済み。

## 検証（全ラウンド pass）
NUL 0・JSON 再パース OK・total=配列数 3579・m-id 連番 m1-m3548 missing=[] dup=False・必須フィールド完全・新規分 半角括弧 0・stats=recompute 全ゼロ・schema_version 0.2・schema_history +7（round1-6＋retrofit）・原文 verbatim 一致・全件 典籍曰く・大師系 0・anchor m549/m719 温存・m506 典籍曰く 巻き戻り assert。ホスト側 Grep で motifs.json（最終 m-id）・CLAUDE.md（★ Phase3 エントリ）反映確認。

## 残課題
**kaimyo-app 同期**（別リポジトリ・未接続）：倉庫 `data/indices/motifs.json`（3579件）を kaimyo-app 側へ単純コピー → NUL 0／total／引用形式タグ反映確認・SHA-256 一致確認。新引用形式タグの導入はないため kaimyo-app 側コード変更なし見込み（冠は source.著作名 フォールバックで「大日経疏 巻第十三に曰く、」）。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝Phase3＋retrofit に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後 kaimyo-app リポジトリを接続して motifs.json 同期。

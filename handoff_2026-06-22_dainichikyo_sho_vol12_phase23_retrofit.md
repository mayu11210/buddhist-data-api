# 引き継ぎメモ — 大日経疏 巻第十二 Phase2＋Phase3＋連動軸 retrofit（2026-06-22）

巻第十二 Phase1 取込（commit `949e542`）に続けて、Phase2 横断索引化・Phase3 motif 抽出・連動軸 retrofit・gabun 裁定を一気に実施した。

## Phase2 横断索引化（36 著作目）
- `_dev_references/` の extract 6本（terms/citations/sanskrit/kaimyo_jukugo/persons/places）の DICT_CORPUS_LIST と `aggregate_indices.py` の ALL_CORPORA に `dainichikyo-sho-vol12` を追加。
- per-corpus 索引 7本を `data/mikkyou/` に生成（terms 19語 matched10・top 阿字88/真言49・citations 4種・sanskrit 3〔haṃ/maṇḍa/śāntika〕・kaimyo 19種・persons 7名・places 3地）。
- 集約 `index_<cat>_all.json` 7本を 36 著作で再生成（corpora_count 35→36・全7カテゴリ合計 unique 3,262/occ 26,192）。
- manifest：vol12 index_status 7カテゴリ present・summary.indexed_corpora 各 35→36。
- 倉庫 validate_corpus.py 47/47 OK。

## Phase3 motif 抽出（58件 m3424-m3481・total 3454→3512）
- 本文 k004-k063 全網羅（首題 k001／撰号 k002／品題 k003・k017・k040 は motif 化せず）・**1段=1motif**（vol8〜11 同型）。
- 全件 `引用形式:典籍曰く`（善無畏口述/一行筆受＝非空海）・大師系タグ非付与・gabun 意図的未設定。
- タグ：`category:密教教学`／`出典:大日経疏 巻第十二`／`主題:〜`／`密教:〜`／`文体:語釈`（譬喩7件）／`一句性:核心`20件／`典故:法華経`（k015/k039）・`典故:央掘魔羅経`（k025）。
- 整合性10項目＋m506 典籍曰く 巻き戻り assert 全 pass（verbatim 一致・vol11 74件温存・recompute 一致）。
- build script：`outputs/vol12/build_motifs.py`。バックアップ：`outputs/motifs_backup_pre_vol12.json`。

## 連動軸 retrofit（新規 sg/anchor なし・タグのみ・核心 verbatim 6件 +12）
- sg08 阿字本不生（m549）← m3440（k021）/ m3466（k048）/ m3470（k052）
- sg26 一切智智（m698）← m3436（k016）/ m3471（k053）
- sg27 自心本性清浄（m719）← m3443（k024）
- total 3512 不変・famous 31 不変。script：`outputs/vol12/retrofit_motifs.py`。

## gabun 裁定
vol12 全58 motif の gabun は**意図的未設定を継続**（非空海・経典注釈系・全件 典籍曰く＝巻第二〜十一 同運用）。stats.motifs_without_gendai_gabun_intentional に `dainichikyo-sho-vol12_round_all` を記載。

## 残課題（要対応）
1. **genten 後送**（最優先・本セッション未了）：CBETA `T1796_012` を Chrome 経由で取得。本セッション中ずっと Claude in Chrome が未接続だったため未実施。巻第十一の手順（`#body` 抽出→夾註を〔〕化・校勘アンカー除去・gaiji は Unicode 保持→900cp×チャンクで SHA-256 照合→corpus の genten/genten_source 更新→manifest data_status.genten=true・char_counts.genten 付与）。**次回は Chrome 拡張をこのアカウントでサインインしてから着手。**
2. **kaimyo-app 同期**：倉庫 motifs.json（3512件）を kaimyo-app 側へコピー・SHA-256 一致確認（別リポジトリ・未接続）。冠は source.著作名 フォールバックで「大日経疏 巻第十二に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝Phase2＋Phase3＋retrofit に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後、Chrome を接続して genten 後送 → kaimyo-app 同期。

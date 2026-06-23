# 引き継ぎメモ — 大日経疏 巻第十五 Phase2 横断索引化 完了（2026-06-23）

genten 後送（commit `60d2270`）に続けて、Phase2 横断索引化（39 著作目）を実施した。巻第十四と同手順。

## 実施
1. 6本の extract スクリプト（terms／citations／sanskrit／kaimyo_jukugo／persons／places）の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に `dainichikyo-sho-vol15` を vol14 直後に追加（構文チェック pass）。
2. 6本を `--corpus dainichikyo-sho-vol15.json` で実行 → `data/mikkyou/` に per-corpus 索引 7本生成。
3. `aggregate_indices.py` 実行 → 集約 `index_<cat>_all.json` 7本を 39 著作で再生成。

## per-corpus 生成結果（vol15）
- terms：matched 9/19・occ 160（top 真言107／法界24／大悲11／阿字7／遮那5）
- citations：**5種5件**（宝炬陀羅尼経・法華経・般若経・華厳経・金剛経）。**全て真正の経名**。`『』` は経名のみで台詞・字義グロスの混入なし（gendaigoyaku の `『』` 5箇所＝この5経名のみ）→ **vol14 のような citations 是正は不要**。
- kukai_works：0
- sanskrit：0（注釈書・割注に IAST なし＝vol13/vol14 同様）
- kaimyo_jukugo：unique 11／matched 6／occ 150（真言107／法界24／大悲11／遮那5／大日2）
- persons：unique 12／occ 35（不動9／大日如来7／観音5／帝釈天4／善無畏2）
- places：unique 3／occ 10（須弥山7／欲界2／安楽1）

## 集約（39 著作）
全7カテゴリ合計 unique 3,264／occ 27,503。max_cov：citations 大日経162(19著作)・法華経151(23著作)／kaimyo 真言1905(39著作)／persons 大日如来1278(38著作)／places 安楽190(23著作)。

## manifest 更新
- vol15 `index_status` 7カテゴリ present:true（file 名付き）。
- `summary.indexed_corpora` 各 38→39。
- `aggregate_indices.corpora_count` 38→39・`source_corpora` に `dainichikyo-sho-vol15` 追加（vol14 直後）。
- 倉庫 `validate_corpus.py` 50/50 メカニカル整合 OK。

## 残課題
1. **Phase3 motif 抽出**（ラウンド制）：著者＝善無畏口述/一行筆受＝非空海 → `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十四 同運用）。着手前に `references/motif-extraction.md` を読み、Phase A 合意（束ね方針・ラウンド分割）を確認。曼荼羅造立次第・潅頂・三昧耶五種・悉地・見諦・身秘密の譬喩群（乾闥婆城・帝釈網・如意珠・虹霓・牛蹄涔と大海）が核心候補。
2. **kaimyo-app 同期**（Phase3 後・別リポジトリ）。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝Phase2 に更新済み）。push 後 `git log` 先頭が本件・`origin/main..HEAD` 空を確認。その後 Phase3 motif 抽出へ。

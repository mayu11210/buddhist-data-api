# 引き継ぎメモ — 大日経疏 巻第十四 Phase2 横断索引化 完了（2026-06-23）

巻第十四 genten 後送（commit `b7c6587`）に続けて、Phase2 横断索引化（38 著作目）を実施した。Phase3 motif 抽出・kaimyo-app 同期が残課題。

## Phase2 横断索引化（38 著作目）
- extract 6本（terms/citations/sanskrit/kaimyo_jukugo/persons/places）の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に `dainichikyo-sho-vol14` を vol13 直後へ追加。
- per-corpus 索引 7本を `data/mikkyou/` に生成：
  - terms：matched 9/19・top 法界69/真言59/阿字50/遮那19/大悲10
  - citations：0（下記是正後）／kukai_works：0／sanskrit：0（IAST/ASCII なし）
  - kaimyo_jukugo：unique14/matched9/occ178（seed_terms11/paren3/review2）
  - persons：9名/occ44（大日如来26/不動9/梵天3/善無畏1/夜叉1 ほか）
  - places：3/occ4（殷2/越1/須弥山1）
- 集約 `index_<cat>_all.json` 7本を 38 著作で再生成：全7カテゴリ合計 unique 3,263 / occ 27,143・各 *_all.json corpora_count=38。占有増分 occ +453（26,690→27,143）＝vol14 per-corpus 合計（terms227+kaimyo178+persons44+places4）と一致。unique は 3,263 不変（vol14 は新規語彙を追加せず）。
- manifest：vol14 index_status 7カテゴリ present・summary.indexed_corpora 各 37→38・aggregate_indices.corpora_count 37→38・source_corpora に vol14 追加。

## citations 是正（ケンシン裁定）
- **問題**：vol14 gendaigoyaku が字義グロス・話者の台詞に `『』` を7箇所使用していた（vol11-13 は `『』`＝書名限定の規約・例 vol11『華厳』『中論』、vol13『大般若経』）。citation 抽出パターン `『…』` がこれを機械的に拾い、偽書名6件（尾・薬・薬叉持明・清浄の音を出す・超越・願わくは…／k047 の長文台詞は >30字フィルタで除外され6件）が混入していた。
- **裁定**：k007/k040/k044/k047 の `『』` 7対を `「」` に統一（1:1 の字置換・字数不変 35,910・本文内容そのまま・kakikudashi/genten 不変）。vol11-13 規約に整合し citations 6→0 にクリーン化。
- 是正後に vol14 索引 6本を再生成→集約を再生成。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／57段全訳／半角括弧 0。
- 倉庫 validate_corpus.py：49/49 メカニカル整合 OK。
- 集約増分＝per-corpus 件数一致（occ +453）。
- ホスト側 Grep で manifest（indexed_corpora 38・corpora_count 38）・CLAUDE.md（★ Phase2 エントリ）反映確認。

## 残課題
1. **Phase3 motif 抽出**（ラウンド制・未着手）：著者=善無畏口述/一行筆受＝非空海 → 全件 `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十三 同運用）。対象は本文段（首題 k001／撰号 k002／品題 k003・k010・k028 を除く）。1段=1motif（vol8〜13 同型）。**着手前に必ず `references/motif-extraction.md` を読み、judgment table を提示してケンシンの承認を得てから build。** Phase A 合意は巻第十三を踏襲（要ケンシン確認）。密印品之余（印相が大半）は核心精選、字輪品（阿字五転）・秘密漫荼羅品（法界生・大真言王・自然成仏偈）は核心候補多め。最終 m-id・total は着手時に motifs.json で確認。
2. **kaimyo-app 同期**（別リポジトリ・未接続）：Phase3 後に motifs.json を kaimyo-app 側へコピー・SHA-256 一致確認。冠は source.著作名 フォールバックで「大日経疏 巻第十四に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝Phase2＋citations 是正 に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後 Phase3 motif 抽出へ（要ケンシン承認）。

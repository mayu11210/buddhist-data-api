# 引き継ぎメモ — 大日経疏 巻第十三 genten 後送＋Phase2 横断索引化（2026-06-23）

巻第十三 Phase1 取込（commit `09787ee`）に続けて、genten 後送・Phase2 横断索引化を実施した。Phase3 motif 抽出と kaimyo-app 同期が残課題。

## genten 後送（CBETA T1796_013）
- **対象**：`data/kukai/dainichikyo-sho-vol13.json` の genten/genten_source。
- **取得**：CBETA 線上閱讀 `T1796_013`（大正蔵 No.1796 vol.39）を Claude in Chrome で `#body` から取得（JS レンダリング）。
- **清掃**（vol10〜12 同体裁）：
  - 夾註（inline-note・DOM の `small.inline-note` 433 件）を半角括弧から `〔 〕` に変換。
  - 校勘アンカー（`.noteAnchor`/`.note-link` 163）を除去。`◎` なし。
  - gaiji 4字（嬭 U+5B2D・𤙖 U+24656・𭌆 U+2D306・𭘬 U+2D62C）を Unicode で保持。
  - 悉曇 IAST 5組（ka・aḥ・aḥ・haṃ・jaḥ＝`.siddam`）は半角括弧のまま温存。
  - 冒頭に `大毘盧遮那成佛經疏卷第十三　原典（…CBETA 線上閱讀 T1796_013）` ヘッダ付与。
- **本文**：20,132字cp（改行443含む・改行除外 19,689字）・夾註〔〕433組・半角括弧5組（IAST のみ）・残存 [] 0・NUL 0。
- **取込の信頼性**：ブラウザ側で clean text を生成→ window.__g を blob download（`cbeta_T1796_013_genten.txt`・59,425 bytes）→ Downloads マウントで読込。全文 SHA-256 `87e05fe3f2e9c75df305957a932dbd952d272da127580426e1e11e08718630e8` をブラウザ側・Python 側で照合しバイト一致を確認（900cp×23 チャンクの per-chunk hash もブラウザ側で算出済）。
- `genten_source` を vol12 同形式に更新。
- manifest：data_status.genten=true・genten_unavailable_reason 削除・char_counts.genten=19,689・summary.genten_present 21→22・notes 追記。
- ビルド素材：`_dev_references/dainichikyo-sho-vol13_build/genten_T1796_013_clean.txt`。

## Phase2 横断索引化（37 著作目）
- extract 6本＋`aggregate_indices.py` の ALL_CORPORA に `dainichikyo-sho-vol13` を追加。
- per-corpus 索引 7本を `data/mikkyou/` に生成（terms matched8/19・top 真言101/法界36/阿字20・citations 1〔大般若経〕・sanskrit 2〔dhātu・kāla〕・kaimyo unique31/matched25・persons 17名/occ67・places 2/occ7）。
- 集約 `index_<cat>_all.json` 7本を 37 著作で再生成（全7カテゴリ合計 unique 3,263/occ 26,690・各 *_all.json の corpora_count=37）。
- manifest：vol13 index_status 7カテゴリ present・summary.indexed_corpora 各 36→37。
- **メタデータ是正**：manifest `aggregate_indices.source_corpora`/`corpora_count` が 32 のまま（vol9〜12 が未反映の累積ドリフト）だったため、生成済み集約ファイルの実体＝37 著作に同期し是正（description に注記）。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／71段全訳／半角括弧 0。
- 倉庫 validate_corpus.py：48/48 メカニカル整合 OK。
- ホスト側 Grep で corpus（genten_source）・manifest（genten_present 22・corpora_count 37）・CLAUDE.md（★ 2026-06-23 エントリ）反映確認。

## 残課題
1. **Phase3 motif 抽出**（ラウンド制・未着手）：著者=善無畏口述/一行筆受＝非空海 → 全件 `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十二 同運用）。対象は本文67段（首題 k001／撰号 k002／品題 k003・k021 を除く k004-k020＋k022-k071）。1段=1motif（vol8〜12 同型）。最終 m-id=m3481・total 3512・sg 31・schema 0.2。密印品（k022-k071）は印相・真言字義が大半 → 手印の語釈は `文体:語釈`、`一句性:核心` は精選。Phase A 合意は巻第十二を踏襲（要ケンシン確認）。**着手前に judgment table を提示してケンシンの承認を得てから build。**
2. **kaimyo-app 同期**（別リポジトリ・未接続）：Phase3 後に motifs.json を kaimyo-app 側へコピー・SHA-256 一致確認。冠は source.著作名 フォールバックで「大日経疏 巻第十三に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝genten 後送＋Phase2 に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後 Phase3 motif 抽出へ。

# 引き継ぎメモ — 大日経疏 巻第十四 genten 後送 完了（2026-06-23）

巻第十四 Phase1 取込（commit `d808d74`）に続けて、genten 後送を実施した。Phase2 横断索引化・Phase3 motif 抽出・kaimyo-app 同期が残課題。

## genten 後送（CBETA T1796_014）
- **対象**：`data/kukai/dainichikyo-sho-vol14.json` の genten/genten_source。
- **取得**：CBETA 線上閱讀 `T1796_014`（大正蔵 No.1796 vol.39）を Claude in Chrome で取得（JS レンダリング）。**live #body の innerText を採用**してブロック構造（首題・撰号・品題・尾題）を温存した（detached clone の innerText だと CSS レイアウトを失い、隠れている行番号ラベル `.lb`〔T39n1796_pXXX〕が露出し品題が本文と結合してしまうため）。
- **清掃**（vol10〜13 同体裁）：
  - 夾註（`small.inline-note` 80 件）を半角括弧から `〔 〕` に変換。
  - 校勘アンカー・マーカー除去（`.noteAnchor`／`.note-link`／`.note-link-cbeta`／`.star` 計123）。`[n]`系・`[＊]`系とも除去。
  - gaiji 2字（𭌆 U+2D306・𠸪 U+20E2A＝`.gaijiAnchor`、Unicode で本文に保持。除去対象に含めない）。
  - 悉曇 IAST 7組（hūṃ・raṃ・raḥ・hraḥ・haḥ・raṃ・raḥ＝`.siddam`）は半角括弧のまま温存。
  - 冒頭に `大毘盧遮那成佛經疏卷第十四　原典（…CBETA 線上閱讀 T1796_014）` ヘッダ付与。
- **本文**：16,486字cp（改行129含む・改行除外 16,357字）・夾註〔〕80組・半角括弧7組（IAST のみ）・残存 [] 0・NUL 0。尾題「大毘盧遮那成佛經疏卷第十四」あり。
- **取込の信頼性**：ブラウザ側で clean text を生成→ `window.__g` を blob download（`cbeta_T1796_014_genten.txt`・49,081 bytes）→ Downloads マウントで読込。全文 SHA-256 `03af7e863f05de0240aa6aead9056f49860d5ac42622cdf86872374ce95e5a7d` をブラウザ側・Python 側で照合しバイト一致を確認。
  - 注：tool 返り値経由の base64/plain-text 転送はコンテンツフィルタ・truncation で不可だったため、vol13 同様 blob download + Downloads マウントで読込。
- `genten_source` を vol13 同形式に更新：`大正新脩大藏經 No.1796『大毘盧遮那成佛神變加持經疏』卷第十四（善無畏口述・一行筆受）／CBETA 線上閱讀 T1796_014`。
- manifest：data_status.genten=true・genten_unavailable_reason 削除・char_counts.genten=16357・summary.genten_present 22→23・notes 追記。
- ビルド素材：`_dev_references/dainichikyo-sho-vol14_build/genten_T1796_014_clean.txt`。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／57段全訳／半角括弧 0。
- 倉庫 validate_corpus.py：49/49 メカニカル整合 OK（ERROR/WARNING 0）。
- ホスト側 Grep で corpus（genten_source）・manifest（genten_present 23・char_counts.genten 16357）・CLAUDE.md（★ genten 後送 エントリ）反映確認。

## 残課題
1. **Phase2 横断索引化**（38 著作目・未着手）：extract 6本＋`aggregate_indices.py` の ALL_CORPORA／DICT_CORPUS_LIST に `dainichikyo-sho-vol14` 追加 → per-corpus 索引 7本生成 → 集約 `index_<cat>_all.json` 7本を全38著作で再生成（corpora_count=38）→ manifest index_status 7カテゴリ present・summary.indexed_corpora 各 37→38。巻第十三と同手順。
2. **Phase3 motif 抽出**（ラウンド制・未着手）：著者=善無畏口述/一行筆受＝非空海 → 全件 `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十三 同運用）。対象は本文段（首題 k001／撰号 k002／品題 k003・k010・k028 を除く）。**着手前に judgment table を提示してケンシンの承認を得てから build。** Phase A 合意は巻第十三を踏襲（要ケンシン確認）。密印品之余（印相が大半）は核心を精選、字輪品（阿字五転）・秘密漫荼羅品（法界生・大真言王・自然成仏偈）は核心候補多め。
3. **kaimyo-app 同期**（別リポジトリ・未接続）：Phase3 後に motifs.json を kaimyo-app 側へコピー・SHA-256 一致確認。冠は source.著作名 フォールバックで「大日経疏 巻第十四に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝genten 後送 に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後 Phase2 横断索引化へ（要ケンシン確認）。

# 引き継ぎメモ 2026-06-17 大日経疏 巻第二 genten 後送 完了（漢文原典 取得・清掃・充填＋manifest 更新＋validate）

**日付**：2026-06-17／**種別**：kakikudashi-data Phase1 残課題（genten 後送）完成
**起点 HEAD**：`3fac6b1`（巻第二 Phase1 完成）／**ステータス**：genten 後送 完成・検証全 pass・**未 commit / 未 push**

## 成果（genten 後送 完了）
- **漢文原典 genten を CBETA 線上閱讀 T1796_002 より取得・充填**。dainichikyo-sho-vol2.json の top-level `genten` に全 21,201 字（codepoint・改行除去 21,101・byte 63,341）。
- 出典：大正新脩大藏經 第39巻 No.1796『大毘盧遮那成佛經疏』巻第二（善無畏口述・一行筆受・入真言門住心品第一之餘の注釈）。CBETA reader が JS のため Chrome 経由（get_page_text／javascript_tool）で取得。
- **清掃は理趣釈と同手順**：校勘 anchor（[n]・[A n]・[＊]）156 件除去・夾註「(此二名是菩提闍梨解)」のみ半角括弧→〔 〕に温存・標點本文採用・本巻に悉曇字なし。首題ヘッダ付与（vol1 と平行）。
- **転送精度を多項式ハッシュ 2 種（base131／base1000003）＋符号点和でブラウザ⇔python 全体一致検証**＝文字単位で完全一致。astral 字 𨶳(U+28DB3)・𩀟(U+2901F) の 2 字につき JS UTF-16 len は 21,203（codepoint+2）。
- **corpus**：genten 充填＋genten_source を CBETA 出典に更新。NUL0・再パース OK。
- **manifest**：data_status.genten=true・genten_unavailable_reason 削除・char_counts.genten=21101・taisho_ref『T1796 / vol.39（巻第二）』・notes 更新・summary.genten_present 11→12。
- **検証全 pass**：skill validate（NUL0/未訳0/半角括弧0）・倉庫側 validate_corpus.py 28/28 メカニカル整合 OK（char_counts/data_status 含む）。
- ビルド素材：`_dev_references/dainichikyo-sho-vol2_build/` に raw_body.txt（CBETA 生本文・anchor 付き）／clean_genten.py（清掃スクリプト）／genten.txt（清掃済み genten）を永続保存。

## 残課題（順）
1. **Phase2 横断索引化**：extract 6本＋aggregate_indices.py の ALL_CORPORA に dainichikyo-sho-vol2 追加→per-corpus 7 本生成→集約 7 本再生成→manifest index_status 付与。17 著作目（巻第一は別途 dict 型で索引済）。
2. **Phase3 motif 抽出**：Phase A 合意（著者=善無畏口述・一行筆受＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun は経典注釈系ゆえ意図的未設定〔hizoki/理趣釈/発菩提心論鈔と同運用〕・連動軸は完走後 retrofit）→outline 10 区分でラウンド分割。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`（HEAD が本 genten 後送コミット）。
2. data/kukai/dainichikyo-sho-vol2.json：top-level genten（21,201字）・genten_source（CBETA）。
3. Phase2 横断索引化 から着手か、Phase3 motif 抽出 か、ケンシン意向を確認。

## 留意
- 書き込み系 git は commit_push.bat 経由（前に fix_index.bat）。SAFETY CHECK で deleted: 検出時は phantom deletion を疑う。
- CLAUDE.md は単一行巨大ファイルで Read/Edit 不可のため python で 1 箇所アンカー置換→ホスト Grep で反映確認済み。
- genten の char_counts は倉庫 validate_corpus.py の `_accept`＝{len, 改行除去 len} のどちらも受理。kk/gd と揃え改行除去値（21101）を採用。

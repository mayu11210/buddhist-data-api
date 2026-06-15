# 引き継ぎメモ 2026-06-15 理趣釈（rishushaku.json）Phase1 取込（生成・検証済・genten 残・未 commit）

**日付**：2026-06-15
**種別**：新規 corpus 取込（kakikudashi-data Phase1）／**Phase1 本体完了・genten のみ残・commit_push.bat 実行待ち**
**起点 HEAD**：`7106a76`（理趣経 連動軸 retrofit 34 完走）
**ステータス**：rishushaku.json 生成＋スキル validate＋倉庫 validate_corpus.py 全 26 件一致 OK・manifest 昇格済・CLAUDE.md 反映済・**未 commit / 未 push**
**変更ファイル**：data/kukai/rishushaku.json（新規）・data/kukai/_corpus_manifest.json（rishushaku 昇格＋rishikyo 逆リンク）・CLAUDE.md（★ 理趣釈 Phase1 エントリ先頭追加）・commit_message.txt・本メモ。**data/indices/motifs.json は不変**。

---

## 今セッションでやったこと

1. **素材**：ユーザー提供 doc『大楽金剛不空真実三昧耶経般若波羅蜜多理趣釈』（伝・不空訳の『理趣経』本文注釈）。libreoffice で .docx 変換 → extract_paragraphs.py で 12 ブロック（23,857 字）抽出。
2. **段落化（ケンシン裁定：細分割）**：12 ブロックは粗いため、経の句・主題ごとに細分割。巻上下を **序分＋十七段＋流通分**の科段に整理し **57 段落 k001-k057**（首題/訳者/尾題含む）。境界はレンマ句で機械分割し一意性・順序を検証。
3. **現代語訳（butten-yasashii-yaku）**：全 57 段落を訳出（5 バッチ累積ビルド）。本文は平易に組み替え、原語・術語・真言字義は割注〔 〕で温存・全角括弧厳守。現代語訳 33,087 字／書き下し 23,877 字。
4. **JSON 生成**：dict_paragraphs スキーマ（rishikyo/yugikyo 同形式）で直接ビルド。top-level に section/source/author/base_text/base_text_ref/genten/outline/translation_status/kakikudashi/gendaigoyaku/paragraphs。outline は科段 23 区分。
5. **manifest 登録**：register_manifest.py → 手動精緻化（taisho_ref=T1003/vol.19・notes・summary 各 +1）。**rishikyo.json 側に relations.commentaries=[rishushaku.json] 逆リンク**を付与、rishikyo notes の「理趣釈は別途・未取込」を「Phase1 取込済」に更新。

## ケンシン裁定（本セッション）

- 作業範囲：**Phase1 取込まで**（Phase2 横断索引化・Phase3 motif 抽出は別セッション）。
- genten：**CBETA T1003 を取込**する方針。ただし下記の技術制約で本セッションは未取込。
- 段落分割：**経の句・主題ごとに細分割**。
- genten 取得手段：**Chrome 接続して取得**する方針（理趣経本体と同手順）。

## ★ 残課題：genten（最優先）

- **genten（漢文原典 CBETA/大正蔵 T1003・vol.19『大樂金剛不空真實三昧耶經般若波羅蜜多理趣釋』）は未取込**。
- 理由：CBETA reader は JS レンダリングで web_fetch 不可。GitHub raw XML（`T/T19/T19n1003.xml`・238,335 bytes）は web_fetch の出力上限で前半（607a-611c）のみ取得・後半欠落。curl 等は不可。本セッション中 Chrome 拡張が未接続だったため Chrome MCP も使用不可。
- 取得済の前半 XML は outputs にあるが**次セッションで消える**ため、retrofit 時は再取得（Chrome reader レンダリング → get_page_text、または GitHub raw を分割取得）。校勘記号 anchor 除去・夾註は〔 〕温存・悉曇字（SD-*）はローマ字転写（charDecl の Unicode transcription 値）で代替。
- retrofit 後：corpus の `genten`/`genten_source` を更新、`genten_unavailable_reason` を削除、manifest の data_status.genten=true・summary.genten_present +1。

## 検証（済）

- スキル validate_corpus.py：JSON 再パース OK・NUL 0・段落 57/未訳 0・現代語訳 半角括弧 0・**総合 OK**。
- 倉庫 _dev_references/validate_corpus.py：manifest 26／実 26 一致・✅ OK。
- CLAUDE.md 反映（host-side Grep で確認）・rishushaku.json NUL 0・kakikudashi 23,877／gendaigoyaku 33,087 字。

## 残課題（次セッション・この順で）

1. **commit**：commit_push.bat ダブルクリック（commit_message.txt 更新済）。push 後 `git log --oneline -3`。
   - 注意：commit_push.bat は Step2 で `git reset HEAD` 後、`git add data/kukai/` 等のディレクトリ単位 add（`-u` なし）。Step4.5 で deleted ガードあり。working tree に残る既存削除（package.json 等）は add されず安全。
   - **同梱注意**：前セッション gabun 裁定の未 commit 文書（`_dev_references/motifs_index_design.md` 補注 KK・CLAUDE.md gabun エントリ）が working tree に残存しており、本コミットに同梱される（commit_message.txt に明記済）。
2. **genten retrofit**（上記★）：Chrome 接続 → CBETA T1003 全文取得 → corpus・manifest 更新 → 再 validate → commit。
3. **Phase2 横断索引化**：extract_*_dict.py 6 本の DICT_CORPUS_LIST と aggregate_indices.py の ALL_CORPORA に `rishushaku.json` 追加 → per-corpus 7 本生成 → 集約再生成 → manifest index_status 付与・summary.indexed_corpora 各 +1。
4. **Phase3 motif 抽出**：references/motif-extraction.md 必読。Phase A 合意（伝・不空訳＝非空海ゆえ **引用形式:典籍曰く** 想定・大師系タグ非付与・短小段の束ね方針・gabun 要否・連動軸は完走後 retrofit）。ラウンド制。理趣経本文・理趣経開題との相互参照に留意。

## 注意点

- **作業中間ファイルはスクラッチパッド（outputs）にあり次セッションで消える**：rishushaku_segments.json・trans_batch1-5.json・rishushaku_genten.txt（前半のみ）・rishushaku_T1003_raw.xml（前半のみ）。内容は rishushaku.json に格納済（genten を除く）。
- マウント同期不具合継続前提：文書はホスト側ツール（Read/Edit/Write/Grep）で確認。CLAUDE.md は超長行のため bash-python で編集し host Grep で反映確認した。
- 既存 motifs.json（total 2445）は不変。理趣経本体 rishikyo.json・理趣経開題 rishukyo-kaidai.json とは別 corpus（本件は注釈書＝理趣釈）。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`
2. data/kukai/rishushaku.json：section「理趣釈（…）」・paragraphs 57・translation_status remaining 0・genten 空（未取込）
3. _corpus_manifest.json：rishushaku エントリ role=primary_corpus・data_status genten=false／kakikudashi・gendaigoyaku=true・relations.commentary_of=rishikyo.json。rishikyo 側 relations.commentaries=[rishushaku.json]。

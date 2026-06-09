# 大日経 本文データ化 引き継ぎメモ

## これは何
真言密教の根本経典『大日経（大毘盧遮那成仏神変加持経）』全文の書き下しを
`data/kukai/dainichikyo.json` に取込み、現代語訳を **巻ごとに分割** して
段階的に付与している作業。文体は butten-yasashii-yaku スキル。

## 進捗（最新）
- 全 896 段落（pidx1-43 目次／44 以降 本文・全七巻三十六品）
- 訳済：**目次（1-43）＋巻第一（44-83）＋巻第二前半（84-137）** ＝ 137 段落
- 未訳：759 段落
  - 巻第二「普通真言蔵品 第四」（pidx 138-378・真言集 241 段落・総 約5千字）＋尾題 379
  - 巻第三（380-427）／巻第四 密印品（428-646・大）／巻第五（647-729）／
    巻第六（730-778）／巻第七 供養法（779-896）

## 次セッションの進め方
1. CLAUDE.md と本メモを読む。`data/kukai/dainichikyo.json` の
   translation_status で訳済/未訳を確認。
2. outputs に作業用がある場合は流用。無ければ次の要領で再構築：
   - 段落本文：`大毘盧遮那成仏神変加持経.doc` を extract_paragraphs.py で
     paras4.json 化（pidx は本文＝段落番号、目次除く先頭が表題）。
   - 既訳は `data/kukai/dainichikyo.json` の paragraphs[].gendaigoyaku に
     入っているので、未訳の pidx だけ trans4_*.json に追記。
   - config は `outputs/config4.json`（全巻 section 構造を確定済）。
   - build：`python3 .../kakikudashi-data/scripts/build_corpus.py config4.json`
     → register_manifest.py → validate_corpus.py。
3. 次の対象は **巻第二 普通真言蔵品（pidx 138-378）**。大半が短い真言なので
   読み＋意味の割注で機械的に進む。その後 尾題 379、続いて巻第三〜七。
4. 巻ごとに push（commit_message.txt を更新 → commit_push.bat）。

## メモ
- 真言は〔読み／教義的意味〕の割注。梵字・字門も逐一。半角括弧は使わない
  （現代語訳に ( ) を混ぜない。割注は〔 〕、引用は「」）。
- validate の「総合: 要確認」は未訳が残るための正常表示。全巻完了で「OK」。
- 既存 `dainichikyo-sho-vol1.json`（疏）・`dainichikyo-kaidai.json`（開題）と
  対の根本経典。meta.related に相互参照済み。

# 引き継ぎメモ — 大日経疏 巻第十二 Phase1 取込 完了（2026-06-22）

## 今回やったこと
ユーザー提供 doc『大毘盧遮那成仏神変加持経疏 巻第十二』（善無畏口述・一行筆受）を、書き下しデータ化スキルの Phase1 で取り込んだ。巻第十一と同型。

- **対象**：`data/kukai/dainichikyo-sho-vol12.json`（新規・36 著作目）
- **内容**：大日経 悉地出現品第六之余〜成就悉地品第七〜転字輪漫荼羅行品第八の注釈
- **段落化**：元 doc が巨大ブロック（14 ブロック・最大8,591字・半角空白952除去後で総27,639字）だったため、科文・話題境界で **63 段**に段落化（巻第三〜十一 同型）。品題3つ（悉地出現品第六之余／成就悉地品第七／転字輪漫荼羅行品第八）は構造段落として保持。割注の全角括弧60対は kakikudashi に温存。尾題なし（巻第十三へ続く）。段落結合が原文（空白除去後27,639字）を完全再現 assert pass。
- **現代語訳**：全63段を butten-yasashii-yaku 文体で現代語訳（gendaigoyaku 35,598字）。
- **科段（outline）21 区分**：首題／撰号／品題（悉地出現品第六之余）／加持の法と薬の成就／縛字門の息災曼荼羅／囉字門の除障と訶字門／風曼荼羅と成就／佉字門の大空と器物成就／嚩字門・羅字門と影像随順／品題（成就悉地品第七）／金剛＝秘密慧と希有の問い／心処＝漫荼羅と自心本浄／八葉の四智と阿字円明観／菴字門と六根浄・心仏を見る／覧字門と真実智／品題（転字輪漫荼羅行品第八）／甘露生三昧と明妃／阿字輪の功徳と自歎／菩提座と阿字真言／大悲胎蔵生漫荼羅の敷置／漫荼羅の方位画線と彩色。

## ビルド・登録
- `build_corpus.py`（title_is_first=false で k001＝首題）で corpus JSON 生成。
- `_corpus_manifest.json` に primary_corpus / role_complete / dict_paragraphs で登録（vol11 直後に挿入）。taisho_ref `T1796 / vol.39（巻第十二）`。
- summary 更新：total_files 46→47・primary 32→33・role_complete 34→35・kk/gd present 各 33→34。
- ビルド素材を `_dev_references/dainichikyo-sho-vol12_build/`（blocks_raw.json・paras.json・config.json・trans_batch*.json）に永続保存。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／63段全訳／半角括弧 0（全角割注60対 温存）。
- 倉庫 validate（`_dev_references/validate_corpus.py`）：全 47 件メカニカル整合 OK。
- ホスト側 Grep で corpus・manifest・CLAUDE.md の反映確認。

## 状態と残課題
Phase1（corpus 取込）完了。残りは巻第十一と同じ流れ：

1. **genten 後送**：T1796 vol.39 巻第十二を CBETA 線上閱讀 `T1796_012` から Chrome 経由で取得（CBETA は JS レンダリング）。巻第十一と同手順（`#body` 抽出→夾註を〔〕化・校勘アンカー除去・gaiji は Unicode 保持→900cp×チャンク分割で SHA-256 照合→JSON の genten/genten_source 更新→manifest data_status.genten=true）。
2. **Phase2 横断索引化**（36 著作目）：extract 6本＋aggregate に dainichikyo-sho-vol12 追加。
3. **Phase3 motif 抽出**（ラウンド制）：著者=善無畏口述/一行筆受＝非空海 → `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十一 同運用）。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。

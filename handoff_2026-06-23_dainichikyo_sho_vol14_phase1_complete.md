# 引き継ぎメモ — 大日経疏 巻第十四 Phase1 取込 完了（2026-06-23）

## 今回やったこと
ユーザー提供 doc『大毘盧遮那成仏神変加持経疏 巻第十四』（善無畏口述・一行筆受）を、書き下しデータ化スキルの Phase1 で取り込んだ。巻第十三と同型。

- **対象**：`data/kukai/dainichikyo-sho-vol14.json`（新規・38 著作目）
- **内容**：大日経 密印品第九之余〜字輪品第十〜秘密漫荼羅品第十一 の注釈
- **段落化**：元 doc が巨大ブロック（15 ブロック・最大 8,157字）だったため、科文・話題境界で **57 段**に段落化（巻第三〜十三 同型）。品題3つ（密印品第九之余 k003／字輪品第十 k010／秘密漫荼羅品第十一 k028）は構造段落として保持。割注の全角括弧60対は kakikudashi に温存。**尾題なし**（秘密漫荼羅品の途中＝大導師の段で巻末・巻第十五へ続く）。段落結合が原文（空白除去後 27,532字）を完全再現 assert pass。
- **現代語訳**：全57段を butten-yasashii-yaku 文体で現代語訳（gendaigoyaku 35,854字）。
- **科段（outline）23 区分**：首題／撰号／品題（密印品之余）／諸天眷属の印 後半／乾闥婆夜叉荼吉尼等の印と真言字義／越三昧耶罪の誡め（印品結び）／品題（字輪品）／遍一切処法門と阿字三部／五字輪と五転・母音三昧の字／字道門と菩薩の行儛／初中後相加と無上殊勝句／身への四重布字／諸字の色と四種輪・不動輪・句輪／品題（秘密漫荼羅品）／法界蔵と平等厳蔵／法界増身と能生諸仏偈・三種の生／智と方便・展転加持／四院分位と五輪布置／輪形五位と世界成壊・法界胎蔵漫荼羅／身語意密と大真言王・字義／三道真言と四魔降伏・三処／諸仏問請と一切智成・歎徳偈／自覚無師智と自然成仏・優陀那偈。

## ビルド・登録
- `build_corpus.py`（title_is_first=false で k001＝首題）で corpus JSON 生成。
- `_corpus_manifest.json` に primary_corpus / role_complete / dict_paragraphs で登録（vol13 直後に挿入）。taisho_ref `T1796 / vol.39（巻第十四）`。
- summary 更新：total_files 48→49・primary 34→35・role_complete 36→37・kk/gd present 各 35→36（genten_present 22 不変＝後送・indexed_corpora 37 不変＝Phase2 未）。
- ビルド素材を `_dev_references/dainichikyo-sho-vol14_build/`（vol14_blocks_clean.json・paras.json・config_vol14.json・trans_all.json・trans_batch1〜6.json）に永続保存。
- CLAUDE.md 冒頭に ★ Phase1 エントリを追記。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／57段全訳／半角括弧 0（全角割注60対 温存）。
- 段落結合＝原文（空白除去後 27,532字）完全再現 assert pass。
- 倉庫 validate（`_dev_references/validate_corpus.py`）：全 49 件メカニカル整合 OK（ERROR/WARNING 0）。
- ホスト側 Grep で corpus（k057）・manifest（vol14 エントリ）・CLAUDE.md（★ Phase1 エントリ）の反映確認。

## 状態と残課題
Phase1（corpus 取込）完了。残りは巻第十三と同じ流れ：

1. **genten 後送**：T1796 vol.39 巻第十四を CBETA 線上閱讀 `T1796_014` から Chrome 経由で取得（CBETA は JS レンダリング）。巻第十三と同手順（`#body` 抽出→夾註を〔〕化・校勘アンカー除去・gaiji は Unicode 保持・悉曇 IAST は半角括弧温存→チャンク分割で SHA-256 照合→JSON の genten/genten_source 更新・genten_unavailable_reason 削除・manifest data_status.genten=true・char_counts.genten 付与・summary.genten_present 22→23）。
2. **Phase2 横断索引化**（38 著作目）：extract 6本＋aggregate に dainichikyo-sho-vol14 追加。
3. **Phase3 motif 抽出**（ラウンド制）：著者=善無畏口述/一行筆受＝非空海 → `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十三 同運用）。密印品之余は印相が大半なので核心は精選。字輪品（阿字五転）・秘密漫荼羅品（法界生・大真言王・自然成仏偈）は核心候補が多い。
4. **kaimyo-app 同期**：Phase3 後に motifs.json を kaimyo-app 側へコピー・SHA-256 一致確認（別リポジトリ）。冠は source.著作名 フォールバックで「大日経疏 巻第十四に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝Phase1 に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後 genten 後送 → Phase2 横断索引化へ。

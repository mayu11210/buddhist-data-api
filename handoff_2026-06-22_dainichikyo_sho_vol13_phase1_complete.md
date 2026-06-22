# 引き継ぎメモ — 大日経疏 巻第十三 Phase1 取込 完了（2026-06-22）

## 今回やったこと
ユーザー提供 doc『大毘盧遮那成仏神変加持経疏 巻第十三』（善無畏口述・一行筆受）を、書き下しデータ化スキルの Phase1 で取り込んだ。巻第十二と同型。

- **対象**：`data/kukai/dainichikyo-sho-vol13.json`（新規・37 著作目）
- **内容**：大日経 転字輪漫荼羅行品第八之余〜密印品第九 の注釈
- **段落化**：元 doc が巨大ブロック（8 ブロック・最大19,319字）だったため、科文・話題境界で **71 段**に段落化（巻第三〜十二 同型）。品題2つ（転字輪漫荼羅行品第八之余 k003／密印品第九 k021）は構造段落として保持。割注の全角括弧419対は kakikudashi に温存。**底本の閉じ落ち割注1件（k062 吽（長声…の閉じ括弧が底本に欠落・割注境界で k062／k063 に分段）も verbatim 温存**（vol10 先例）。尾題なし（巻第十四へ続く）。段落結合が原文（空白除去後32,722字）を完全再現 assert pass。
- **現代語訳**：全71段を butten-yasashii-yaku 文体で現代語訳（gendaigoyaku 40,277字）。
- **科段（outline）14 区分**：首題／撰号／品題（転字輪…之余）／彩色と諸尊の図像／漫荼羅造立と四大結護／外漫荼羅と潅頂法／品題（密印品第九）／如来身密印と三明真言／十二合掌と三昧耶印／転法輪印・刀印・法螺印・坐印／如来の諸印と真言の字義／諸菩薩の印 前半／諸菩薩の印 後半／仏頂の諸印と諸天の印。

## ビルド・登録
- `build_corpus.py`（title_is_first=false で k001＝首題）で corpus JSON 生成。
- `_corpus_manifest.json` に primary_corpus / role_complete / dict_paragraphs で登録（vol12 直後に挿入）。taisho_ref `T1796 / vol.39（巻第十三）`。
- summary 更新：total_files 47→48・primary 33→34・role_complete 35→36・kk/gd present 各 34→35（genten_present 21 不変＝後送）。
- ビルド素材を `_dev_references/dainichikyo-sho-vol13_build/`（blocks_raw.json・paras.json・config.json・trans_all.json・trans_batch1〜6.json）に永続保存。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／71段全訳／半角括弧 0（全角割注419対 温存）。
- 段落結合＝原文（空白除去後 32,722字）完全再現 assert pass。
- 倉庫 validate（`_dev_references/validate_corpus.py`）：全 48 件メカニカル整合 OK。
- ホスト側 Grep で corpus・manifest・CLAUDE.md の反映確認。

## 状態と残課題
Phase1（corpus 取込）完了。残りは巻第十二と同じ流れ：

1. **genten 後送**：T1796 vol.39 巻第十三を CBETA 線上閱讀 `T1796_013` から Chrome 経由で取得（CBETA は JS レンダリング）。巻第十二と同手順（`#body` 抽出→夾註を〔〕化・校勘アンカー除去・gaiji は Unicode 保持・悉曇 IAST は半角括弧温存→900cp×チャンク分割で SHA-256 照合→JSON の genten/genten_source 更新→manifest data_status.genten=true・genten_unavailable_reason 削除・char_counts.genten 付与・summary.genten_present 21→22）。
2. **Phase2 横断索引化**（37 著作目）：extract 6本＋aggregate に dainichikyo-sho-vol13 追加。
3. **Phase3 motif 抽出**（ラウンド制）：著者=善無畏口述/一行筆受＝非空海 → `引用形式:典籍曰く`・大師系タグ非付与・gabun 意図的未設定（巻第二〜十二 同運用）。密印品は印相・真言字義が大半なので核心は精選（手印の語釈は文体:語釈）。
4. **kaimyo-app 同期**：Phase3 後に motifs.json を kaimyo-app 側へコピー・SHA-256 一致確認（別リポジトリ）。冠は source.著作名 フォールバックで「大日経疏 巻第十三に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝Phase1 に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。その後 Phase2 横断索引化へ。

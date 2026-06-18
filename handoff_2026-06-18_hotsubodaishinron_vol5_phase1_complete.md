# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第五巻 Phase1 完成（全訳＋corpus ビルド＋manifest 登録＋validate）

**日付**：2026-06-18／**種別**：kakikudashi-data Phase1（取込）完成
**起点 HEAD**：発菩提心論鈔 第二巻 完結（`7bfdd8e`）／**ステータス**：Phase1 完成・検証全 pass・**未 commit / 未 push**

## 成果（Phase1 完成）
- **現代語訳 全103段 完訳**（batch1-3・butten-yasashii-yaku）。現代語訳総字数 17,391字。kakikudashi 13,248字。
  - batch1 k001-k035（首題・目次・書名）／batch2 k036-k064（勝義の菩提心の総説・勝義の得名〔般若の妙恵で九種住心を無自性と観じ捨劣得勝〕・観一切法無自性・**相説旨陳の二段〔有相観/無相観・人空/法空・両部配当・十住心配当・k047 929字〕**・第一住心〔凡夫の名聞利養・三毒五欲〕）／
    batch3 k065-k103（外道の行相〔恋其身命・薬物による仙宮住寿・生天を究竟と計す・**k066 1355字／k075 1075字**〕・**業力若尽未離三界の文点四義〔k084 788字〕**・煩悩尚存・宿殃悪念・沈淪苦海・無自性の結成〔夢幻陽焔の十喩〕・二諦義・**外道の原由〔経律異相の九十六種外道の起源・k102 1100字〕**・一段畢）。
- **corpus JSON ビルド**：`data/kukai/hotsubodaishinron-sho-vol5.json`。section「発菩提心論鈔 第五巻」／author「宥快」／
  base_text_ref relation:commentary_of（bodaishinron.json）／genten 空〔中世日本の鈔・大正蔵範疇外〕／outline 10 区分／paragraphs 103／translation_status 103-103。
- **manifest 登録**：primary_corpus／role_complete／dict_paragraphs。char_counts kk13248・gd17391・para103。
  summary：total_files 31→32・primary_corpus 18→19・role_complete_files 19→20・kakikudashi/gendaigoyaku_present 各 18→19。
  bodaishinron.json の commentaries に vol5 逆リンク追加（vol1〜vol5 の順に整列）。
- **検証 全 pass**：NUL0／未訳0／半角括弧0・倉庫 validate_corpus.py 32/32 メカニカル整合 OK。
  - ※ batch3 で段落化ずれ（k070「恋其身命文」見出し欠落＋k070 以降 1 段ずれ）を検出し、kakikudashi との全 103 段アライメントを再検証して是正済。
- ビルド素材を `_dev_references/hotsubodaishinron-sho-vol5_build/` に永続保存（source.docx・paras.json・outline.json・trans_1〜3.json）。
- **★ これで発菩提心論鈔 第一〜第五巻が全巻 倉庫入り。**

## outline 10 区分
首題(k001)／目次(k002-k034)／書名〔重題〕(k035)／勝義の菩提心の総説・勝義の得名(k036-k043)／
観一切法無自性・相説旨陳の二段(k044-k049)／第一住心〔凡夫執着・三毒五欲〕(k050-k064)／
外道〔恋其身命・薬物生天・業果〕(k065-k079)／業力若尽未離三界・煩悩尚存・宿殃悪念(k080-k096)／
当知外道之法・無自性結成・二諦義・外道の原由(k097-k102)／結(k103)。

## 残課題（順）
1. **Phase2 横断索引化**：extract 6本＋aggregate_indices.py の ALL_CORPORA に hotsubodaishinron-sho-vol5 追加→per-corpus 7本生成→集約 7本再生成→manifest index_status 付与。21 著作目（indexed_corpora 20→21）。
2. **Phase3 motif 抽出**：Phase A 合意は第一/二/三/四巻と同じ（著者=宥快＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit）。outline の本文区分でラウンド分割。目次 k001-k035／尾題 k103 は motif 化せず。論義見出し・牒文は直後の注釈本文に束ねる。
3. **完走後**：連動軸 retrofit（候補＝sg22 三種菩提心〔勝義菩提心〕／sg17 十住心〔九種住心無自性・第一住心・嬰童無畏心〕／sg18 顕密二教 等）／gabun 裁定／kaimyo-app 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. data/kukai/hotsubodaishinron-sho-vol5.json（103段・全訳）・manifest の vol5 entry。
3. Phase2 横断索引化 から着手。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。

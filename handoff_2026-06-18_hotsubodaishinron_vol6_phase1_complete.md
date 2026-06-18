# 引き継ぎメモ 2026-06-18 発菩提心論鈔 第六巻 Phase1 完成（全訳＋corpus ビルド＋manifest 登録＋validate）

**日付**：2026-06-18／**種別**：kakikudashi-data Phase1（取込）完成
**起点 HEAD**：発菩提心論鈔 第五巻 完結（`6223d8f`）／**ステータス**：Phase1 完成・検証全 pass・**未 commit / 未 push**

## 成果（Phase1 完成）
- **現代語訳 全106段 完訳**（batch1-4・butten-yasashii-yaku）。現代語訳総字数 21,109字。kakikudashi 16,047字。
  内容＝二乗〔声聞・縁覚〕の無自性（勝義の菩提心の続き・十住心の第四唯蘊無我心／第五抜業因種心に当たる）。
  - batch1 k001-k036（首題・目次・書名）／batch2 k037-k052（二乗の総表・声聞執四諦法〔声聞の得名三義・**k044 2059字**〕・縁覚執十二因縁〔部行麟喩・三世両重の十二因縁・**k052 1351字**〕）／
    batch3 k053-k076（二乗の合釈〔五蘊観・破衆生執・**k054 1492字**〕・修行得果・小涅槃の四種・真言行者の観〔人空法有・但浄意識・末那梨耶を覚知せず・灰身滅智湛然常寂・**k076 913字**〕）／
    batch4 k077-k106（五性各別と一性皆成・定性不定性の回心の劫限・従化城起超三界・宿信仏発大心・諸仏の加持による回小入大・**三無数劫の難行苦行〔回心は初住か十信か・第六か第八住心か・k092 1225字〕**・智恵狭劣亦不可楽〔無自性結成〕・一段畢）。
- **corpus JSON ビルド**：`data/kukai/hotsubodaishinron-sho-vol6.json`。section「発菩提心論鈔 第六巻」／author「宥快」／
  base_text_ref relation:commentary_of（bodaishinron.json）／genten 空〔中世日本の鈔・大正蔵範疇外〕／outline 12 区分／paragraphs 106／translation_status 106-106。
- **manifest 登録**：primary_corpus／role_complete／dict_paragraphs。char_counts kk16047・gd21109・para106。
  summary：total_files 32→33・primary_corpus 19→20・role_complete_files 20→21・kakikudashi/gendaigoyaku_present 各 19→20。
  bodaishinron.json の commentaries に vol6 逆リンク追加（vol1〜vol6 の順に整列）。
- **検証 全 pass**：NUL0／未訳0／半角括弧0・段落アライメント spot-check OK・倉庫 validate_corpus.py 33/33 メカニカル整合 OK。
- ビルド素材を `_dev_references/hotsubodaishinron-sho-vol6_build/` に永続保存（source.docx・paras.json・outline.json・trans_1〜4.json）。
- **★ これで発菩提心論鈔 第一〜第六巻が全巻 倉庫入り。**

## outline 12 区分
首題(k001)／目次(k002-k035)／書名〔重題〕(k036)／二乗の総表・声聞執四諦法(k037-k046)／縁覚執十二因縁(k047-k052)／
二乗の合釈〔破衆生執・尅証其果趣涅槃〕(k053-k064)／真言行者の観〔雖破人執猶有法執・灰身滅智〕(k065-k076)／定性不定性の回心(k077-k082)／
従化城起超三界・宿信仏発大心(k083-k090)／三無数劫の難行苦行・然得成仏(k091-k099)／既知声聞縁覚・智恵狭劣亦不可楽〔無自性結成〕(k100-k105)／結(k106)。

## 残課題（順）
1. **Phase2 横断索引化**：22 著作目（indexed_corpora 21→22）。
2. **Phase3 motif 抽出**：Phase A 合意は第一〜五巻と同じ（著者=宥快＝**非空海**→引用形式:典籍曰く 全件・大師系タグ非付与・gabun 意図的未設定・連動軸は完走後 retrofit）。目次 k001-k036／尾題 k106 は motif 化せず。論義見出し・牒文は直後の注釈本文に束ねる。
3. **完走後**：連動軸 retrofit（候補＝sg17 十住心〔第四第五住心・二乗〕／sg22 三種菩提心〔勝義菩提心〕／sg12 化城宝処〔従化城起〕／sg11 良医病子 等。特に五性各別と一性皆成・二乗の無自性・化城）／gabun 裁定／kaimyo-app 同期。

## 次セッション開始時の確認
1. CLAUDE.md 冒頭→本メモ→`git log --oneline -3`。
2. data/kukai/hotsubodaishinron-sho-vol6.json（106段・全訳）・manifest の vol6 entry。
3. Phase2 横断索引化 から着手。

## 注意：phantom staged deletion（既知）
package.json 等の staged deletion は全て disk 実在・既知 stale index。commit_push.bat の index リセットで自動解消。

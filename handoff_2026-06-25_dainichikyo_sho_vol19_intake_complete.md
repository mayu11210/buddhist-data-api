# handoff 2026-06-25 — 大日経疏 巻第十九 取込（Phase1＋genten＋Phase2）完了（push1）

## 到達点
大日経疏 巻第十九（`data/kukai/dainichikyo-sho-vol19.json`・善無畏口述/一行筆受＝**非空海**）の
**取込ひとまとめ（Phase1＋genten＋Phase2 横断索引化＝43著作目）が完了**。3工程を **1 push（push1）** に集約。
`commit_message.txt` 更新済み。`commit_vol19_push1.bat` 実行待ち。

- 43 著作目。motif は次フェーズで **m3878 から連番**（現 motifs.json total 3908・最終 m3877・不変）。
- 倉庫 `validate_corpus.py` **54/54 OK**。
- HEAD 起点：930fb73（巻第十八 push2）。

## 巻第十九の内容（7品＝二十一〜二十七）
1. 百字位成品第二十一＝金剛手の真言救世者（百門の王＝暗字）の偈問（誰が・何処で・誰が説く）と仏の答。八葉蓮華の意生・円明月輪の心鏡観、囉字慧眼で本尊を観じ己身を同ぜしむ、影像縁起（垢身より浄身）と本不生、白黄赤の作意・幻の喩で出世間心。
2. 百字成就持誦品第二十二＝身は意より生じ浄心から光を流出、如意珠の喩、無分別法界、住無尽衆生界淨除＝三昧流出/不思議/転他門の四句、虚空等心＝浄菩提心より大悲、阿字＝本不生と算数の喩、阿字より嚩・迦等の字門（迦佉哦伽…娑訶）を字義で釈、仰壤拏曩莾の五字と三十二相、別処の文の混入を疏者が指摘。
3. 百字真言法品第二十三＝空による加持と阿字第一句、声字真言の縁起、一字に百字の軌儀。
4. 説菩提性品第二十四＝菩提性＝阿字門一切智の句、虚空の喩（一切万有の所依にして無所依・三世を出過）。
5. 三三昧耶行品第二十五＝三三昧耶＝三平等（菩提心為因・大悲為根・方便為究竟／仏法僧／三身）、相続不間断、初心→如実智→大悲の三、草藉の戒と障の縁。
6. 明如来品第二十六＝如来・人中尊・菩薩・仏導師の名義を虚空菩提/十地通達/十力/慧害無明/自証如去で釈、巻末に大本は各百余偈を各一偈に略す旨の編集注記。
7. 護摩法品第二十七＝外典韋陀の火祠と真言門の火法の邪正、梵王が牛形となる本生譚、人生儀礼ごとの火神名と火法、梵天への布施・莎訶で巻末。

## Phase1（corpus）
- 段落化：元 doc の本文ブロック（百字位成品 最大10,082字）を科文・話題境界で**本文81段**に分割＋構造9段（首題 k001／撰号 k002／品題7＝k003・k027・k048・k056・**k065**・k078・k084）＝**全90段 k001-k090**。内訳：百字位成品 23段（k004-k026）／百字成就持誦品 20段（k028-k047）／百字真言法品 7段（k049-k055）／説菩提性品 8段（k057-k064）／三三昧耶行品 12段（k066-k077）／明如来品 5段（k079-k083）／護摩法品 6段（k085-k090）。
- **三三昧耶行品第二十五の品題 補入（ケンシン裁定）**：元 doc は説菩提性品第二十四の本文（[9]）に続けて三三昧耶行品の本文へ話題遷移するのみで**品題行が欠落**。CBETA T1796_019 の head「次三三昧耶行品第二十五」を確認し、構造段 k065（書き下し「次三三昧耶行品第二十五」）として補入。他6品題は doc にあり（k003/k027/k048/k056/k078/k084・k078 は doc 本文[10]先頭にインライン埋込→切り出し）。
- **重複ブロックなし**：各本文ブロック内に60字連続重複の検知ゼロ（vol15/17/18 と異なり除去不要）。元 doc に埋込画像なし。段落結合が原 doc 本文を完全再現する assert pass（全角割注の半角括弧0・NUL0）。
- 現代語訳 butten-yasashii-yaku **全90段訳済**。段落化は本体で実施（科文/話題境界・自動セグメンタ→割注分割なし/括弧balance assert）、訳は**品ごと分割サブエージェント7体**で作成し、各段を id キーで回収。**全段で「書き下しスライス＝訳」の1:1整合**（per-品 verbatim concat assert・ratio 外れ0・重複訳0・全段 section ラベル付与）を検証。kk 34,721字／gd 52,259字（1.51x）。
- **citations 是正（vol14 precedent）**：明如来品（k079-k083）の名義釈で『仏』『如来』『菩薩』『人中尊』『正覚』『仏導師』『仏陀』『三菩提』『菩提』『正等覚』『慧害』『如去』の12語を『』で表記し、citations 索引に偽書名が混入。該当4段（k079-k082）の『X』→「X」に統一（1:1・字数不変・kk/genten 不変・vol11-13/18 規約＝『』は書名限定に整合）。残る真の書名6件〔法華経 k007／中論 k015／月灯三昧経 k023／大般若経 k036／般若経 k043／菩薩蔵経 k081〕。
- corpus 構造は vol18 同型（section/source/base_text/genten/genten_source/text/format_note/outline/translation_status/kakikudashi/gendaigoyaku/paragraphs〔id・section_major・section・kakikudashi・gendaigoyaku〕）。**「節」は paragraphs[].section から直接取得**すること。
- manifest：vol19 entry を vol18 直後に登録・summary（total_files 53→54・primary 39→40・role_complete 41→42・kk/gd present 40→41・genten_present 27→28）。char_counts kk34,721／gd52,259／genten18,880／paragraphs90。

## genten（CBETA T1796_019）
- Chrome で `https://cbetaonline.dila.edu.tw/zh/T1796_019` を取得（`#body` の `.juan`×2／`.byline`／`.div-pin`×7 構造）。
- 夾註66（`.inline-note`）を ( )→〔 〕化／`.lb`(行番号926)・`.lb_br`・`.noteAnchor`(60)・`.note-link`・`.note-link-cbeta`・`.scan-image-display-btn`・`.glyphicon`・`.label`・`.lineInfo`・`.star` 除去／残存校異 [1]-[A6] 除去。
- 悉曇は CBETA の IAST を**半角括弧で温存**（(ka)(kha)…(sa) の27箇所＝字門）。gaiji 𭋥（U+2D2E5）Unicode 保持（1箇所＝astral）。
- 構造：juan1+byline（無 \n 連結）＋\n＋7 div-pin（品題本文 連結・空白除去）を \n 区切り＋\n＋juan2（巻末）。改行8。
- **バイト照合**：クリーニング後の #body を `<pre>` に注入し **get_page_text で全文を一括回収**。`window.__genten` の **UTF-16長 18,889＋FNV-1a 223344142** をブラウザ側計算値と一致照合。**1400字×14チャンクの per-chunk FNV-1a も全件一致**（Python 側 UTF-16-LE 単位で再計算）。codepoint は astral 𭋥 1字ぶん少ない 18,888。
- corpus.genten 投入・char_counts.genten=18,880（改行除き codepoint）・manifest genten_present 27→28。
- clean txt 保存：`_dev_references/dainichikyo-sho-vol19_build/genten_T1796_019_clean.txt`。

## Phase2（横断索引化・43著作目）
- `_dev_references/extract_{terms,citations,sanskrit,kaimyo_jukugo,persons,places}_dict.py` の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に vol19 追加。
- per-corpus 7本生成（`data/mikkyou/index_dainichikyo-sho-vol19_*.json`）：terms matched10・occ258（真言132/阿字65/大悲18/本不生18/法界8）／citations 6種〔是正後・全て真正書名〕／kukai_works 0／sanskrit 0（注釈書・割注に IAST なし・ASCII 4 は doc/genten 等のメタ語）／kaimyo unique19/matched14/occ183／persons 7（梵天20・大日如来12・不空6・観音2・善無畏1）／places 2（欲界/色界）。
- aggregate 7本再生成（**43著作**・corpora_count 42→43・全7カテゴリ合計 unique 3,288/occ 29,043）。manifest aggregate source_corpora/corpora_count 同期・summary.indexed_corpora 各42→43。

## 次フェーズ（push2＝motif）— Phase A 合意（巻第二〜十八 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全 motif に「引用形式:典籍曰く」・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十九`／`引用形式:典籍曰く`。
- gabun（雅文体訳）は意図的未設定・連動軸は完走後 retrofit・1段=1motif（束ねは語中切れ等のみ）。
- 構造段 k001/k002/k003/k027/k048/k056/k065/k078/k084 は motif 化しない → **motif 対象は本文81段**。
- **m3878 から連番**。判定表は全ラウンドまとめて提示→確認後止めず一気に処理（round_all）。着手前に `references/motif-extraction.md` を再読。**「節」は corpus の paragraphs[].section から直接取得し、節==corpus.section を全件 assert**。
- 連動軸 retrofit 候補（core verbatim 限定でスキャン）：sg08 阿字本不生（百字成就持誦品・百字真言法品「阿字＝一切諸法本不生／阿字第一句」、説菩提性品「菩提性＝阿字門一切智の句」）・sg07 三句法門（三三昧耶行品「菩提心為因・大悲為根・方便為究竟」＝大日経 住心品 三句 verbatim・**強連動候補**）・sg21 浄菩提心（百字成就持誦品「虚空等心＝浄菩提心より大悲」）・sg17 十住心 等。

## 次フェーズ（push3＝kaimyo-app 同期）
- motifs.json コピー・SHA-256 一致確認。motif 完走後。冠は source.著作名 フォールバックで「大日経疏 巻第十九に曰く、」＝新引用形式タグなしのためコード変更なし見込み。

## 検証ログ（pass）
- Phase1：JSON再パースOK・NUL0・全90段訳済・半角括弧0（kk/gd）・段落連結 per-品 verbatim assert pass・訳の段境界1:1整合（ratio 外れ0・重複訳0）・citations 是正後 偽書名0・validate 54/54。
- genten：UTF-16長18,889＋FNV-1a 223344142＋14チャンク per-chunk hash でブラウザ正本とバイト同一性照合・夾註66/校勘/gaiji 𭋥/悉曇27検査・validate 54/54。
- Phase2：per-corpus 7本＋aggregate 7本生成・indexed_corpora 各43・validate 54/54。

## commit_push 注意
- 標準 `commit_push.bat` は phantom staged 削除で Step4.5 中止するため使わない。**専用 `commit_vol19_push1.bat`**（git reset HEAD→vol19 対象パスのみ stage→ステージ済み削除のみ安全チェック→commit→push）を用意。
- **`git add` に gitignore 対象（`/*.bat`・`/commit_message*.txt`）を入れない**。commit_message は `-F` で読むため add 不要・bat 自身も add 不要。build dir 内の source.doc/source.docx と LibreOffice の `.~lock.source.docx#`・`*.tmp` は stage 後に `git reset` で除外（サンドボックスから rm 不可）。
- push 後は `git show HEAD:data/kukai/dainichikyo-sho-vol19.json` 等で反映を確認（マウント同期遅延に注意）。

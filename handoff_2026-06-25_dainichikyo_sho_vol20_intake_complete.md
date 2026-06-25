# handoff 2026-06-25 — 大日経疏 巻第二十（Phase1＋genten＋Phase2）完了（push1）／**T1796 全20巻 完結**

## 到達点
大日経疏 巻第二十（`data/kukai/dainichikyo-sho-vol20.json`・善無畏口述/一行筆受＝**非空海**・**T1796 全20巻の最終巻**）の
**取込ひとまとめ（Phase1＋genten＋Phase2 横断索引化＝44著作目）が完了**。3工程を **1 push（push1）** に集約。
`commit_message.txt` 更新済み。**`commit_vol20_push1.bat` 実行待ち**。

- 44 著作目。motif は次フェーズで **m3959 から連番**（現 motifs.json total 3989・最終 m3958・不変）。
- 倉庫 `validate_corpus.py` **55/55 OK**。
- HEAD 起点：eddcb7b（巻第十九 push2）。
- **これにより大日経疏 巻一〜二十 全巻 corpus/genten/横断索引 完備（最終巻）**。

## 巻第二十の内容（5品＝二十七之余〜三十一）
1. **世出世護摩法品第二十七之余**＝巻第十九 護摩法品の残り。外道（梵行）の事火＝邪護摩（縛羊/触穢/熟食/拝日月天/息災・増益・除障・攝召・燒林木・暖腹 等の火神名と作法）と、仏が成正覚の後に説く真慧の火十二種（智火＝大因陀羅／行満／風燥／…／悉成）、火天の三摩地形、内護摩＝煩悩を薪・智慧を火として焚き浄菩提心を得る義、火爐の作法（一肘量・金剛囲・茅の右施）と三落叉的次第。「世出世火品了る」で品結。
2. **本尊三昧品第二十八**＝諸尊の三種形＝字（声・菩提心）・印（有相無相）・形貌（浄非浄）、各々二種、有相より無相へ引入、本尊と行者の感応（方諸向月・円鏡向日の喩・冥応）、本尊形を観じて自身を本尊身とす。『大般若』の洗滌観心で円頓に入る。
3. **無相三昧品第二十九**＝無相三昧の観法、想は身か心意かを尋ね、身は業生にして草木瓦石に等し（『大般若』倉囷の三十六物観）、像の喩で身相を離れ、語は空谷響・心は三世不可得と観じ、身口意の戯論を離れて真言実相を証し仏と住を同じくす。即ち阿字門・法界の性。
4. **世出世持誦品第三十**＝秘密念誦の法、心念誦と出入息念誦を第一とし四種念誦、世間（有縁・字句・出入息）と出世間（意念誦・離文字・本来不生）の持誦、三落叉＝三十万遍の数義と身語意の三相（相義・見義・垛義・標義）・三垢を除き三功徳を生ず、三句法門との相応、師に依らざる者の五無間の誡め。「次は観囑品なり」で囑累品へ。
5. **囑累品第三十一**＝経の付属（十世界微塵数の金剛菩薩）と不放逸の誡め、弟子の相を択ぶ義（観囑品・良晨/根性/相貌・佛子の相）、佛への加持請、大悲胎蔵漫荼羅の三句（菩提心因・大悲根・方便究竟）と中台八葉の配釈（普賢＝菩提心/文殊＝慧/弥勒＝悲/観音＝証・五仏＝宝幢/華開敷/阿弥陀/鼓音）、**諸尊の種子字と五転（金剛手嚩/蓮花尊娑/文殊麼）＝埋込画像**、一切の本尊は皆大日如来に帰す、百字輪の内外出入（迦字四転）、法身の自在神変加持（帝釈宮/歓喜園/天鼓/梵王の喩）、北方阿閦は経の誤＝鼓音仏が正とする疏者の指摘で巻末。巻末に **嘉保二年二月廿日 金剛峯寺奥院東菴室 觀音院 の写本奥書**。

## Phase1（corpus）
- 段落化：元 doc 6大ブロック（護摩法品之余 9,699／本尊三昧 3,475／無相三昧 3,844／持誦品 5,926／囑累品 p31 4,782＋p31b 3,814）を科文・話題境界で**本文82段**＋構造7段（首題 k001／撰号 k002／品題5＝**k003 世出世護摩法品之余/k028 本尊三昧品/k039 無相三昧品/k050 世出世持誦品/k067 囑累品**）に段落化。
- **埋込画像 image1.png 本文補入（ケンシン裁定・vol18 precedent）**：囑累品の地の文に悉曇種子字（金剛手嚩=va/蓮花尊娑=sa/文殊麼=ma の五転〔行・菩提心・成菩提・涅槃・方便〕）の画像が挟まる（python-docx で抽出不可）。画像を判読し **CBETA T1796_020 の該当文（如金剛手種子(va)字…(māḥ)方便）と照合**して書き下しを起こし、**種字を割注〔悉曇 X〕化・読みは CBETA sd-gif の IAST に統一**。1段（**k080**）として p31（…中台の如きは一切の本尊も亦たかくの如く説くべし）と p31b（余の一切尊の種子の字も皆亦た…）の間に補入＝**全90段 k001-k090**。
- **重複ブロックなし**（各本文ブロック内60字連続重複の検知ゼロ・vol19 同型・除去不要）。**段落結合が原 doc 本文を完全再現する assert pass（image 補入除く・5品全 recon 一致）**。元 doc 埋込画像は image1.png 1点のみ。
- 品題は doc に全て存在（vol19 のような品題欠落・CBETA 補入は**不要**）。CBETA pinHead と doc 品題が一致確認（5品）。
- 現代語訳 butten-yasashii-yaku **全90段訳済**。段落化は本体で実施（自動セグメンタ・括弧balance assert・reconstruction verbatim assert）、訳は**品ごと分割サブエージェント4体**（護摩品之余24／本尊三昧+無相三昧20／持誦品16／囑累品22）で section ラベル＋gendaigoyaku を回収（kakikudashi は本体が verbatim 保持）。構造7段は本体で訳。**全段で「書き下しスライス＝訳」の1:1整合**（top kk/gd == 段落 \n 結合・半角括弧0・全角割注〔 〕・seq77/78 の丸括弧→〔 〕是正）。kk 31,914字／gd 40,480字（1.27x）。
- **citations**：囑累品/本尊三昧品の引用は『大般若経／摩訶毘盧遮那成菩提加持神変経（＝大日経の正式名）／普賢観経／金剛頂』の **4種＝全て真正書名**。**vol14/19 のような名義釈『仏』『如来』等の偽書名混入は無し＝citations 是正 不要**（明如来品のような名義釈品が本巻に無いため）。
- corpus 構造は vol19 同型（section/source/base_text/genten/genten_source/text/format_note/outline/translation_status/kakikudashi/gendaigoyaku/paragraphs〔id・section_major・section・kakikudashi・gendaigoyaku〕）。**「節」は paragraphs[].section から直接取得**。
- manifest：vol20 entry を vol19 直後に登録・summary（total_files 54→55・primary 40→41・role_complete 42→43・kk/gd present 41→42・genten_present 28→29）。char_counts kk31,914／gd40,480／genten17,465／paragraphs90。

## genten（CBETA T1796_020）
- Chrome で `https://cbetaonline.dila.edu.tw/zh/T1796_020` を取得。`#body` 構造：`.juan`×2（juan0=首題／juan1=尾題「大毘盧遮那經釋義卷第二十」）／`.byline`（沙門一行阿闍梨記）／`.div-pin`×5（5品）／**`.div-w`＝嘉保二年 写本奥書**。
- 夾註33（`.inline-note`）を ( )/（）→〔 〕化／`.lb`(行番号872)・`.lb_br`・`.noteAnchor`(64)・`.note-link`・`.note-link-cbeta`・`.scan-image-display-btn`・`.glyphicon`・`.label`・`.lineInfo`・`.star` 除去／残存校異 [3]等 除去。
- 悉曇は CBETA の sd-gif（glyph 画像）＋直後の IAST を**半角括弧で温存**（(va)(vā)(vaṃ)(vaḥ)(vāḥ)/(sa)…/(ma)…/(ka)(kā)(kaṃ)(kaḥ)/(a) の22箇所＝五転 IAST。glyph 画像は text 抽出で落ちる）。gaiji 𦿔（U+26FD4）Unicode 保持（1箇所＝astral）。
- 構造：juan0(首題)＋byline 無\n連結＋\n＋5 div-pin を\n区切り＋\n＋juan1(尾題)＋\n＋div-w(嘉保奥書)＝**改行7**。
- **バイト照合**：クリーニング後 #body を `<pre>` に注入し get_page_text で全文一括回収。`window.__genten` の **UTF-16長 17,473＋FNV-1a 2431520954** をブラウザ側計算値と一致照合。**1400字×13チャンクの per-chunk FNV-1a 全件一致**（Python 側 UTF-16-LE 単位で再計算）。codepoint は astral 𦿔 1字ぶん少ない 17,472。
- corpus.genten 投入・char_counts.genten=17,465（改行除き codepoint）・manifest genten_present 28→29。
- clean txt：`_dev_references/dainichikyo-sho-vol20_build/genten_T1796_020_clean.txt`。
- 注：CBETA の最初の filter ブロックは outerHTML/href（query string）が原因で、本文・奥書テキストは get_page_text で問題なく回収可（structural 探査は class/boolean のみ返す方式で回避）。

## Phase2（横断索引化・44著作目）
- `_dev_references/extract_{terms,citations,sanskrit,kaimyo_jukugo,persons,places}_dict.py` の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に vol20 追加。
- per-corpus 7本生成（`data/mikkyou/index_dainichikyo-sho-vol20_*.json`）：terms matched11・occ148（真言58/大悲24/大日16/遮那12/阿字11）／citations 4種5件〔全真正書名・excluded0〕／kukai_works 0／sanskrit 9〔IAST 9＝種子字 va/sa/ma 五転 maḥ/maṃ/māḥ/saḥ/saṃ 等〕／kaimyo unique11/matched6/occ126／persons 13（大日如来28・文殊10・観音6・普賢5・弥勒4）／places 1（周2）。
- aggregate 7本再生成（**44著作**・corpora_count 43→44・全7カテゴリ合計 unique 3,295/occ 29,399）。manifest aggregate source_corpora/corpora_count 同期・summary.indexed_corpora 各43→44・index_status 7present。

## 次フェーズ（push2＝motif）— Phase A 合意（巻第二〜十九 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全 motif に「引用形式:典籍曰く」・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第二十`／`引用形式:典籍曰く`。
- gabun（雅文体訳）は意図的未設定・連動軸は完走後 retrofit・1段=1motif（束ねは語中切れ等のみ）。
- 構造段 k001/k002/k003/k028/k039/k050/k067 は motif 化しない → **motif 対象は本文82段＋種子字 k080＝計83段**（※ k080 種子字段の motif 化要否は要裁定。vol18 の百字生品 種字段は motif 化済の precedent あり）。
- **m3959 から連番**。判定表は全ラウンドまとめて提示→確認後止めず一気に処理（round_all）。着手前に `references/motif-extraction.md` を再読。**「節」は corpus の paragraphs[].section から直接取得し、節==corpus.section を全件 assert**。
- 軸ずれ正規化（主題:本生 不使用→文体:譬喩・潅頂→灌頂・核心は 1品2〜3件）。新タグ値は既存軸内のみ。
- 連動軸 retrofit 候補（core verbatim 限定でスキャン）：**sg08 阿字本不生**（無相三昧品「阿字之門/法界之性」・持誦品「本来不生＝心」・囑累品「初阿字…動首の義」）・**sg07 三句法門**（持誦品/囑累品「菩提心為因・大悲為根・方便為究竟」＝大日経 三句 verbatim・**強連動候補**）・**sg21 浄菩提心**（無相三昧品「淨菩提心初法明門」・囑累品「此地者即是淨菩提心」）・sg27 自心本性清浄・本尊三昧/無相三昧の観法系（瑜伽観・月輪観）。新 sg 新設の要否は要裁定。

## 次フェーズ（push3＝kaimyo-app 同期）
- motifs.json コピー・SHA-256 一致確認。motif 完走後。冠は source.著作名 フォールバックで「大日経疏 巻第二十に曰く、」＝新引用形式タグなしのためコード変更なし見込み。`commit_motifs_sync.bat`／`commit_message_motifs_sync.txt`（kaimyo-app HEAD a3f6138）。

## 全20巻 完結に伴う残課題（最終巻のため・handoff/CLAUDE に記録）
- **全巻 genten 完備確認**：巻一〜二十 全て genten 投入済（巻二十で完備）。要：全巻一括 validate と genten_present の最終確認（現 manifest genten_present=29・大日経疏20巻＋他著作）。
- **連動軸 sg 新設の要否**：本尊三昧品/無相三昧品/世出世持誦品 の観法・三落叉・三平等は既存 sg08/sg07/sg21/sg27 で被覆できるか、新 sg（例：三落叉・本尊瑜伽観）が要るかを push2 retrofit 時に裁定。
- **大日経疏 全20巻 motif サマリ**：全巻 motif 抽出完走後、巻別 motif 件数・核心・連動軸の全巻総括を handoff に記録。

## 検証ログ（pass）
- Phase1：JSON再パースOK・NUL0・全90段訳済・半角括弧0（kk/gd）・top kk/gd==段落\n結合・段落連結 per-品 verbatim assert pass（image 補入除く・5品 recon 一致）・citations 真正書名のみ・validate 55/55。
- genten：UTF-16長17,473＋FNV-1a 2431520954＋13チャンク per-chunk hash でブラウザ正本とバイト同一性照合・夾註33/校勘/gaiji 𦿔/悉曇22検査・validate 55/55。
- Phase2：per-corpus 7本＋aggregate 7本生成・corpora_count 44・indexed_corpora 各44・validate 55/55。

## commit_push 注意
- 標準 `commit_push.bat` は phantom staged 削除で Step4.5 中止するため使わない。**専用 `commit_vol20_push1.bat`**（git reset HEAD→vol20 対象パスのみ stage→build dir の source.doc/docx と LibreOffice `.~lock`/`lu46ftrhr.tmp` を reset 除外→staged 削除ガード→commit→push→Step8 で vol20 corpus/terms index の HEAD 在否確認）を用意。
- **`git add` に gitignore 対象（`/*.bat`・`/commit_message*.txt`）を入れない**。commit_message は `-F` で読むため add 不要・bat 自身も add 不要。
- push 後は `git show HEAD:data/kukai/dainichikyo-sho-vol20.json` 等で反映を確認（マウント同期遅延に注意）。

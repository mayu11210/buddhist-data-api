# handoff 2026-06-25 — 大日経疏 巻第十八 取込（Phase1＋genten＋Phase2）完了（push1）

## 到達点
大日経疏 巻第十八（`data/kukai/dainichikyo-sho-vol18.json`・善無畏口述/一行筆受＝**非空海**）の
**取込ひとまとめ（Phase1＋genten＋Phase2 横断索引化＝42著作目）が完了**。3工程を **1 push（push1）** に集約。
`commit_message.txt` 更新済み。`commit_vol18_push1.bat` 実行待ち。

- 42 著作目。motif は次フェーズで **m3833 から連番**（現 motifs.json total 3863・最終 m3832・不変）。
- 倉庫 `validate_corpus.py` **53/53 OK**。
- HEAD 起点：1f618e2（巻第十七 push2 補完）。

## 巻第十八の内容（3品）
1. 受方便学処品第十八之余（巻第十七からの続き）＝菩薩の十善戒（不与取・不邪行・不妄語・不麁語・不両舌・不綺語・不貪・不瞋・邪見）の各条と方便（慧方便具足）の釈、各戒を例証する本生譚・譬喩（童真比丘と童女／僧伽吒経 屍を負う夫婦／華厳善見女人／長阿含 思益王と長手王／師子王と人肉を食う獣性の子・善奴王／菩薩蔵本生 慶雲＝摩納婆が燃灯仏に授記され第九地に登る）、在家出家の二種菩薩と在家五戒の句、四重根本（謗法・捨菩提心・慳・悩衆生）、無漏性戒。
2. 百字生品第十九＝不空教の真言＝暗字（一切真言の心・真言王・真言導師・救世者）、百光遍照真言と自体加持・神変、字輪の構成（中央に真言王／外一輪に十二三昧声／外輪に百字）、百字の布字（迦字四転 ka／kā／kaṃ／kaḥ＝二十五字×四＝百字）と五重布字。
3. 百字果相応品第二十＝正覚大智灌頂地（第十一地）と陀羅尼形の仏事、語字輪の広長・胎蔵生の影像、無量世界海門と普賢行願、心無量より四無量を得て正等覚を成ず＝暗字悉地の果。

## Phase1（corpus）
- 段落化：元 doc の本文ブロック（受方便学処品之余 最大約24,300字）を科文・話題境界で**本文45段**に分割＋構造5段（首題 k001／撰号 k002／品題3＝k003・k027・k037）＝**全50段 k001-k050**。内訳：受方便学処品之余 23段（k004-k026）／百字生品第十九 9段（k028-k036）／百字果相応品第二十 13段（k038-k050）。
- **重複ブロックの検知・除去（巻第十五・十七 precedent 踏襲）**：原 doc に明らかなコピー由来の連続重複が1箇所。
  - 受方便学処品之余・不両舌戒の**野干師子の譬（805字）＋直後の「非時／時語／非処」passage（163字）＝計968字が二重化**（[6618:7586] と [7586:8554] が一致）→後出を除去。
  - 除去後の段落結合が原文（重複除去後）**23,333字**を完全再現する assert pass。**genten（CBETA T1796_018）照合で野干師子の譬・外道師領徒千人の因縁とも原典側に一度のみ存在（傳我法已畢／分徒五百／領徒千人 いずれも genten 内 出現1回）＝コピー由来と確定**し除去を維持。
- **doc 埋込画像2点**（`word/media/image1.png` `image2.png`）＝**百字生品の悉曇種字を地の文に挟み込んだ"本文そのもの"**（python-docx では本文が抽出されない）。各画像の地の文を kakikudashi に転記し、悉曇種字（迦字四転）の位置に **〔悉曇 ka〕〔悉曇 kā〕〔悉曇 kaṃ〕〔悉曇 kaḥ〕** の割注を置いて温存（**ケンシン裁定＝本文転記＋種字を割注化**）。読みは CBETA 原典音写に統一。
  - image1＝「先ず〔悉曇 ka〕迦等の二十五より、次に〔悉曇 kā〕等の二十五、次に〔悉曇 kaṃ〕等の二十五、次に〔悉曇 kaṃ〕等の二十五なり。」（第一系列は CBETA・doc とも ka/kā/kaṃ/kaṃ で第四が kaṃ）。
  - image2＝「もし五重に布すことを作せば、この〔悉曇 ka〕等の二十五字は第一輪と為し、〔悉曇 kā〕等を第二輪と為し、〔悉曇 kaṃ〕等を第三輪と為し、〔悉曇 kaḥ〕等を第四輪と為るも亦た得たり（更にこれを問え）。意未だ尽くさず。」（五重布の系列は ka/kā/kaṃ/kaḥ）。
  - 種字計8個（ka×2／kā×2／kaṃ×3／kaḥ×1）を verbatim 温存。CBETA「先從(ka)迦等廿五，次(kā)等廿五，次(kaṃ)等廿五，次(kaṃ)等廿五…(kaḥ)等為第四輪」と一致。
- 現代語訳 butten-yasashii-yaku **全50段訳済**（半角括弧0）。段落化＋訳は分割サブエージェントで作成し、**全段で「書き下しスライス＝訳」の1:1整合（連結=原文 verbatim、訳の冒頭/末尾が各段の冒頭/末尾に対応）を assert で検証**（受方便学処品で訳の段境界ずれを1度検知→該当8段を独立スライスで再訳して是正済）。
- corpus 構造は vol17 同型（section/source/base_text/genten/genten_source/text/format_note/outline/translation_status/kakikudashi/gendaigoyaku/paragraphs〔id・section_major・section・kakikudashi・gendaigoyaku〕）。section は科段ラベル（motif 判定表の「節」は **paragraphs[].section から直接取得**すること）。
- manifest：vol18 entry を vol17 直後に登録・summary（total_files 52→53・primary 38→39・kk/gd present 39→40・genten_present 26→27）。char_counts kakikudashi 30,949／gendaigoyaku 48,977／genten 16,958／paragraphs 50。

## genten（CBETA T1796_018）
- Chrome で `https://cbetaonline.dila.edu.tw/zh/T1796_018` を取得（`#body` の `.juan/.byline/.div-pin` 構造）。
- 夾註34（`.inline-note`）を ( )→〔 〕化（夾註内に紛れた CBETA 行ref `T39n1796_p...` も除去）／`.lb`(行番号848)・`.lb_br`・`.noteAnchor`・`.note-link`・`.scan-image-display-btn`・`.glyphicon`・`.label`・`.lineInfo` 除去／残存校異 [1]-[A7] 除去。
- 悉曇は CBETA の IAST を**半角括弧で温存**（(ka)(kā)(kaṃ)(kaḥ)(aṃ) の9箇所＝CBETA は悉曇 gif を IAST 付きで表示）。gaiji 𡱈（U+21C48）Unicode 保持（2箇所＝astral）。
- **バイト照合**：blob 再DL は Chrome の多重DL制限で不可、base64 転送は Chrome MCP のフィルタで遮断されたため、クリーニング後の #body を `<pre>` に注入し **get_page_text で全文を一括回収**。`window.__genten` の **UTF-16長 16,973＋FNV-1a 1632669972** をブラウザ側計算値と一致照合（Python 側で UTF-16-LE 単位で再計算し一致確認・codepoint は astral 𡱈 2字ぶん少ない 16,971）。
- corpus.genten 投入・char_counts.genten=16,958（改行除き codepoint）・manifest genten_present 26→27。
- clean txt 保存：`_dev_references/dainichikyo-sho-vol18_build/genten_T1796_018_clean.txt`。

## Phase2（横断索引化・42著作目）
- `_dev_references/extract_{terms,citations,sanskrit,kaimyo_jukugo,persons,places}_dict.py` の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に vol18 追加。
- per-corpus 7本生成（`data/mikkyou/index_dainichikyo-sho-vol18_*.json`）：terms 9種（真言61/法界10/大日7/遮那7/大悲6）／citations（智度論・華厳経・僧伽吒経・大智度論・宝雲経）／kukai_works 0／sanskrit（kaṃ/kaḥ 等の悉曇 IAST）／kaimyo／persons 16（大日如来13・普賢9・不空5・釈迦5・夜叉3）／places（安楽）。
- aggregate 7本再生成（**42著作**・corpora_count 41→42・summary.indexed_corpora 各41→42）。manifest aggregate stats 全カテゴリ再同期。
- **注意（既存挙動の踏襲）**：places の dynasty 検出等は seed 辞書由来の既存挙動（vol11-17 同型）。vol18 のみ是正せず踏襲。

## 次フェーズ（push2＝motif）— Phase A 合意（巻第二〜十七 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全 motif に「引用形式:典籍曰く」・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十八`／`引用形式:典籍曰く`。
- gabun（雅文体訳）は意図的未設定・連動軸は完走後 retrofit・1段=1motif（束ねは語中切れ等のみ）。
- 首題/撰号/品題（k001/k002/k003/k027/k037）は motif 化しない → **motif 対象は本文45段**（k004-k026／k028-k036／k038-k050）。
- **m3833 から連番**。判定表は全ラウンドまとめて提示→確認後止めず一気に処理（新運用）。着手前に `references/motif-extraction.md` を再読。**「節」は corpus の paragraphs[].section から直接取得し、節==corpus.section を全件 assert**。
- 連動軸 retrofit 候補：sg08 阿字本不生（百字果相応品「以此一字同於大空、本不生故」＝百字の身も本不生／受方便学処品「無為戒＝阿字門を離れず」）・sg21 浄菩提心・sg27 自心本性清浄（不瞋戒「心本性清浄」）・sg17 十住心 等を core verbatim 限定でスキャン。

## 次フェーズ（push3＝kaimyo-app 同期）
- 要フォルダ接続（kaimyo-app）。motifs.json コピー・SHA-256 一致確認。motif 完走後。

## 検証ログ（pass）
- Phase1：JSON再パースOK・NUL0・全50段訳済・半角括弧0（kk/gd）・段落連結 assert pass（受方便学処品 23,333字／百字生品 3,173字／百字果相応品 4,391字）・訳の段境界1:1整合 全段確認・validate 53/53。
- genten：UTF-16長16,973＋FNV-1a 1632669972 でブラウザ正本とバイト同一性照合・夾註/校勘/gaiji/悉曇検査・重複の原典1回 確認・validate 53/53。
- Phase2：per-corpus 7本＋aggregate 7本生成・indexed_corpora 各42・validate 53/53。

## commit_push 注意
- 標準 `commit_push.bat` は package.json 等の幻の staged 削除で Step4.5 中止するため使わない。**専用 `commit_vol18_push1.bat`**（git reset HEAD→vol18 対象パスのみ stage→ステージ済み削除のみ安全チェック→commit→push）を用意。
- push 後は `git show HEAD:data/kukai/dainichikyo-sho-vol18.json` 等で反映を確認（マウント同期遅延に注意）。

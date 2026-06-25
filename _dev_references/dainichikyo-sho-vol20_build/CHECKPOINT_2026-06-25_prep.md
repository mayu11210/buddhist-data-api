# CHECKPOINT 2026-06-25 — 大日経疏 巻第二十（T1796 最終巻）取込

## 進捗更新（segmentation + 訳 完了・残＝genten/種子字画像＝要 Chrome）
- **段落化完了**：`segment.py`→`paras_skeleton.json`（**89段**＝構造7＋本文82）。本文 avg384字・max720（seq4=巨大割注・正当）・**reconstruction verbatim assert pass・全角割注（）balance OK・半角( )=0**。
- 構造段：首題k相当 seq1／撰号 seq2／品題5（seq3,28,39,50,67）。
- **本文訳 完了**：品ごとサブエージェント4体で out_A_homa(24)／out_B_honzon_musou(20)／out_C_jiju(16)／out_D_zokurui(22)＝**82段**。構造7段は本体で `out_struct.json`。全件 seq カバー確認・**gendaigoyaku 半角( )/丸括弧（）=0**（seq77/78 の（）→〔 〕是正済）。
- `build_corpus_vol20.py` 準備済（out_struct+out_A〜D＋out_image.json〔未〕＋genten_T1796_020_clean.txt〔未〕を読んで `data/kukai/dainichikyo-sho-vol20.json` 生成。image 段は after_seq=79 に挿入＝囑累品 p31→p31b の間）。
- **残（要 Chrome／CBETA T1796_020）**：(1) genten 全文バイト照合抽出→`genten_T1796_020_clean.txt`、(2) 種子字画像 image1.png 転記＝`out_image.json`（金剛手/蓮華眼/文殊 の種子字＋五転・読みは CBETA sd-gif の IAST に統一）。その後 build→validate→manifest(44著作目)→Phase2横断索引化。

---
## （以下・初回調査メモ）

週間制限が近づいたため、**リポジトリのトラッキング対象ファイルを一切変更していない安全な地点**（corpus JSON 生成・manifest 登録・commit の前）で中断。
本巻は **T1796 全20巻の最終巻**（巻末 colophon 確認＝後述）。次セッションはこの調査結果から corpus 化に直接入れる。

## 起点状態（中断時・確認済み）
- buddhist-data-api HEAD: `eddcb7b`（vol19 push2）。kaimyo-app HEAD: `a3f6138`。
- motifs.json total **3989**・最終 **m3958**・両リポジトリ SHA-256 一致
  （`cbb17d041604df73005ce3c3fbf77b1939e44473f612e2d60a975c2acd370284`）。
- 倉庫 corpus 54 files・横断索引 43 著作目。**巻第二十は 44 著作目・motif は m3959 から連番**。
- CLAUDE.md line1 アンカー `# buddhist-data-api 作業ルール（現代語訳作業・2026-04-25〜・` 確認済（先頭★= vol19）。
- **トラッキング対象の変更なし**（git status clean のはず）。作った build 成果物は下記のみ（全て新規・未 stage）。

## 完了済みの準備作業（build dir `_dev_references/dainichikyo-sho-vol20_build/`）
- `source.doc`（添付コピー）→ libreoffice で `source.docx` 変換済。
- `blocks_full.json` … 本文6大ブロックを抽出済（後述ラベル）。
- `img_extract/word/media/image1.png` … doc 埋込画像（**本文＝悉曇種子字**。要転記。後述）。

## 巻第二十の構造（doc・CBETA 両確認＝一致）
**5品**。doc の本文大ブロック6個（ラベル=blocks_full.json のキー）：

| ラベル | 品 | doc文字数 | 備考 |
|---|---|---|---|
| p27yo | 世出世護摩法品第二十七之余 | 9699 | 巻第十九 護摩法品の**残り（之余）**。冒頭「羊を縛ぐ時は…」末「…世出世火品了る…今内法の火神は…三昧に住するなり。」 |
| p28 | 次本尊三昧品第二十八 | 3475 | 「爾時、執金剛秘密生、仏に白して…」 |
| p29 | 次無相三昧品第二十九 | 3844 | 「復た次に、大日世尊、執金剛秘密主に告げて…」 |
| p30 | 次世出世持誦品第三十 | 5926 | 「この世出世間持誦品、上来の一部の経の意は…」 |
| p31 | 次囑累品第三十一 | 4782 | 「次に仏、大会に告ぐ…」末「…中台の如きは、一切の本尊も亦たかくの如く説くべし。」 |
| p31b | （囑累品 続き＝画像の後） | 3814 | 「余の一切尊の種子の字も皆亦たかくの如く広く説くべし…」末「…鼓音仏をもって定と為すなり。」 |

- **品題行は doc に全て存在**（p27yo/p28/p29/p30/p31 の各冒頭の短ブロック）。vol19 のような品題欠落・補入は**不要**。
  - 首題ブロック `大毘盧遮那成仏神変加持経疏巻第二十`／撰号 `沙門一行阿闍梨記`／品題 `世出世護摩法品第二十七之余`。
- **重複ブロックなし**：6大ブロックとも 60字連続重複の検知ゼロ（除去不要。vol15/17/18 と異なる）。
- p31 と p31b は同一「囑累品第三十一」の本文で、**間に埋込画像（種子字）が挟まる**。

## 埋込画像 image1.png（要・本文転記＝ケンシン裁定事項の踏襲）
- 位置：doc 段落 par26（p31 本文末「…中台の如きは、一切の本尊も亦たかくの如く説くべし」と p31b 冒頭「余の一切尊の種子の字も…」の**間**＝囑累品の地の文）。
- 内容（画像から判読・**悉曇種子字＋五転（行・菩提・成菩提＝三菩提・涅槃・方便）の対応**）。縦書右→左。要旨：
  - 「金剛手の種子〔◇〕字の如きは、すなわちこれ五事（五転）を成ず。…方便を…後と為す可き有り。」
  - 「蓮華眼（蓮華部）等の如きも、亦た五事有り。〔◇〕は是れ行、〔◇〕は是れ菩提（心）、〔◇〕は是れ成菩提（三菩提）、〔◇〕は是れ涅槃、〔◇〕は是れ方便なり。」
  - 「文殊の如きは〔◇〕字をもって種子と為す。〔◇〕は是れ行、〔◇〕は菩提心、〔◇〕は成菩提、〔◇〕は涅槃、〔◇〕は方便なり。」
  - ※上は判読下書き。**確定読みは CBETA で要照合**（下記）。種字は割注〔 〕化し、読みは CBETA 音写に統一する（kk/gd とも半角括弧厳禁・割注〔 〕）。

## CBETA T1796_020（genten 元・調査済／本転送は未実施）
- URL: `https://cbetaonline.dila.edu.tw/zh/T1796_020`。`#body` 確認。
- 構造：`.juan`×2／`.byline`×1（沙門一行阿闍梨記）／`.div-pin`×5（5品＝上記順）。`.inline-note`（夾註）**33**。body textContent 長 ≈ 33,405。
- **最終巻確証**：巻末 colophon
  `大毘盧遮那[3]經釋義卷第二十／嘉保二年二月廿日，於金剛峯寺奧院東菴室，觀音院…`（嘉保二年=1095 写本奥書）。次巻 T1796_021 は存在しない。
- **悉曇の表現**：CBETA は悉曇を `<img src=.../sd-gif/...gif>` ＋直後に IAST 半角括弧（例 `(va)(vā)(vaṃ)(vaḥ)(vāḥ)(sa)(sā)(saṃ)…`）。
  → vol19 同様、**IAST 半角括弧を温存**（glyph 画像は text 抽出で落ちる。これは genten のみの半角例外）。sd-gif 計22。
  → **doc 画像 image1.png の種子字確定読みは、この CBETA 末尾付近（囑累品 金剛手/蓮華眼/文殊 種子字＝五転）の IAST と照合して確定する**こと。
- gaijiAnchor 例 `𦿔`（U+26FD4 等）あり＝Unicode 温存。
- 校異マーカー `[11][12][3]` 等は除去対象。

## 残作業（次セッション・vol19 と同手順／push は1巻3回集約）
### push1（取込）
1. 段落化：p27yo〜p31b を科文/話題境界で本文段に分割（自動セグメンタ→割注分割なし/括弧balance assert）。構造段＝首題 k001／撰号 k002／品題5。**image1.png の種子字段を囑累品 p31→p31b の間に地の文として挿入**（種字割注化・読みは CBETA 音写）。段落結合＝原 doc 完全再現 assert（埋込画像分は CBETA 照合で補入＝ケンシン裁定踏襲）。
2. 現代語訳：butten-yasashii-yaku。品ごと分割サブエージェント（書き下しスライス＝訳の 1:1 整合 assert・全角割注〔 〕・半角括弧0）。
3. corpus JSON `data/kukai/dainichikyo-sho-vol20.json`（vol19 同型 12 top-keys／paragraphs id=kNNN・section_major/section/kakikudashi/gendaigoyaku）。section名 `大毘盧遮那成仏神変加持経疏 巻第二十`・source `沙門一行阿闍梨記（善無畏口述・一行筆受）`。
4. manifest 登録（**44 著作目**・vol19 直後）。summary total_files 54→55・genten_present 28→29 等。
5. 検証：`scripts/validate_corpus.py` ＋ **倉庫側 `_dev_references/validate_corpus.py`（引数なし全件）** ERROR/WARNING 0。
6. genten：Chrome で T1796_020 `#body` クリーニング（inline-note ( )→〔 〕・lb/行番号/noteAnchor/校異除去・悉曇 IAST 半角温存・gaiji Unicode 温存）→ `<pre>` 注入 → get_page_text 全文回収 → **UTF-16長＋FNV-1a＋1400字チャンク per-chunk hash でバイト照合**。clean txt を `genten_T1796_020_clean.txt` に保存。
7. Phase2 横断索引化（44 著作目）：extract_*_dict.py 6本 `DICT_CORPUS_LIST`＋aggregate_indices.py `ALL_CORPORA` に `dainichikyo-sho-vol20.json` 追加→per-corpus 7本＋aggregate 7本再生成。**citations の名義釈『』偽書名は「」へ是正**（vol14/19 同型・要確認＝明如来品ほど名義釈は少ない見込みだが本尊三昧/囑累品の尊名引用に注意）。
8. `commit_vol20_push1.bat`（vol19 bat を雛形に対象パス置換）。**gitignore 対象（/*.bat・/commit_message*.txt）は add しない**。build dir の source.doc/docx・LibreOffice `.~lock`/`.tmp` は stage 後 git reset 除外。

### push2（motif）
- Phase A 踏襲：全件 `引用形式:典籍曰く`・大師系非付与・source に著者保持。共通タグ `category:密教教学`／`出典:大日経疏 巻第二十`／`引用形式:典籍曰く`。1段=1motif・gabun 意図的未設定・連動軸は完走後 retrofit。構造段（首題/撰号/品題5）は motif 化しない。
- **m3959 から連番**。判定表サブエージェント→軸ずれ正規化（主題:本生不使用→文体:譬喩・潅頂→灌頂・核心1品2〜3件）→全件提示→確認後 round_all 一括（dry-run＋整合性8+2項目＋巻き戻り assert＋backup＋schema_history）。
- 連動軸 retrofit 候補（core verbatim 限定）：sg08 阿字本不生・sg21 浄菩提心・**本尊三昧品=観法系**（瑜伽観・月輪観）／無相三昧品=無相・真言実相／世出世持誦=三落叉。新 sg 新設要否は要裁定。
- `commit_vol20_push2.bat`。

### push3（kaimyo-app 同期）
- motifs.json コピー→SHA-256 一致→`commit_message_motifs_sync.txt` 更新→既存 `commit_motifs_sync.bat` 実行依頼。

### 全20巻完了 handoff（最終巻のため）
- 残課題記録：全巻 genten 完備確認・連動軸 sg 新設要否・全20巻通しの索引/motif サマリ。

## 注意（再掲・落とし穴）
- CLAUDE.md は line1 約25万字1行。ホスト Read/Edit 不可。bash python で line1 アンカー直後に★prepend→ホスト Grep で確認。「現在の進捗」節は理趣経で凍結中＝触らない。
- 専用 bat は ASCII のみ・rem に `< > & |` 不可。書込系 git 不可（commit_message 更新→bat 実行依頼・push 確認は git log 読取のみ）。
- 全角（）厳守・割注〔 〕・半角 ( ) 混入禁止（kk/gd とも）。genten の悉曇 IAST のみ半角例外。
- マウント同期遅延：文書はホスト Write/Edit、JSON はホスト Grep で反映確認。push 後は `git show HEAD:...` で確認。

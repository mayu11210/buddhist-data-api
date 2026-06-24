# handoff 2026-06-24 — 大日経疏 巻第十七 取込（Phase1＋genten＋Phase2）完了

## 到達点
大日経疏 巻第十七（`data/kukai/dainichikyo-sho-vol17.json`・善無畏口述/一行筆受＝**非空海**）の
**取込ひとまとめ（Phase1＋genten＋Phase2 横断索引化＝41著作目）が完了**。新運用に従い、この3工程は
**1 push に集約（push1＝取込）**する。`commit_message.txt` 更新済み。`commit_vol17_push1.bat` 実行待ち。

- 41 著作目。motif は次フェーズで **m3745 から連番**（現 motifs.json total 3775・最終 m3744・不変）。
- 倉庫 `validate_corpus.py` **52/52 OK**。

## 巻第十七の内容（5品）
1. 秘密八印品第十四（秘密八印＝第一〜第八印の印相・漫荼羅・真言、八印を八仏菩薩〔宝幢・開敷花王・阿弥陀・鼓音・普賢・文殊・弥勒・観自在〕に配当、阿闍梨授法の誡め・六月三月の修行期間）
2. 持明禁戒品第十五（真言行者の戒＝尸羅本性戒と没栗多時限戒、金剛手の五頌の問、大日如来の讃と語義釈〔索多・薩埵・大福徳者〕、三平等＝身印・語真言・心本尊、落叉＝見、六月持誦法〔金剛阿字／水嚩／火囉／風訶／金水阿嚩／風火訶羅〕と功徳）
3. 阿闍梨真実智品第十六（一切真言の心＝阿字、阿字本不生・種子、布字＝支分に布す、根本字〔阿刹羅〕と増加字〔哩比〕の不一不異、阿闍梨＝如来・諸天尊号はみな我〔毘盧遮那〕の列挙、常住＝仏で結ぶ）
4. 布字品第十七（身体各部位への梵字配当〔迦佉哦…暗噁〕、仏即一切智）
5. 受方便学処品第十八（菩薩戒＝学処、十善戒、授戒次第〔三帰＝常住秘密三宝・十無尽蔵・表白〕、菩薩の十重禁戒、声聞外道との差別＝一道法門〔阿字門〕、不殺・不与取戒の方便〔毒蟒・五百商人・師子の譬〕）

## Phase1（corpus）
- 段落化：元 doc を科文・話題境界で**本文88段**に分割＋構造7段（首題 k001／撰号 k002／品題5＝k003・k014・k036・k063・k065）＝**全95段 k001-k095**。
- **重複ブロックの検知・除去（巻第十五 precedent 踏襲）**：原 doc に明らかなコピー由来の連続重複が2箇所。
  - (1) 阿闍梨真実智品の字論ブロック（「人の頭無ければ…阿より一切語言の声を生ず」）**906字が二度連続**→後出を除去。
  - (2) 同品末の結び（「猶道場に坐する時…常住即仏」）**342字**が、**布字品第十七の品題直後にも重出**（doc 上の誤挿入）→後出を除去し、結びは阿闍梨真実智品末（k061-k062）に一度のみ保持。
  - 除去後の段落結合が原文（重複除去後・図像標識除外）**28,922字**を完全再現する assert pass。**genten（CBETA T1796_017）照合で両重複とも原典側に存在せず（字論・結びとも CBETA で各1回）＝コピー由来と確定**。布字品第十七の品題境界も CBETA どおり（品16末「常住即佛也」→布字品第十七「即義與上相連也」）。
- **doc 埋込画像9点**（`word/media/image1-9.png`）：image1＝第一印の三角漫荼羅図、image2-9＝悉曇真言8点。Unicode 等価字なきため**位置標識〔図・…〕＋読み割注**で温存（ケンシン裁定）。**悉曇真言の読みは CBETA 原典音写に統一**（第一印 藍𡀩／第二印 鑁縛／第三印 三索／第四印 憾郝／第五印 暗惡。doc 画像 OCR の暫定読み「落」「邦」は 𡀩／郝 の誤読として是正）。
- 現代語訳 butten-yasashii-yaku **全95段訳済**（半角括弧0）。corpus 構造は vol16 同型（section/source/base_text/genten/genten_source/text/format_note/outline/translation_status/kakikudashi/gendaigoyaku/paragraphs〔id・section_major・section・kakikudashi・gendaigoyaku〕）。section は科段ラベルを付与（motif 判定表の「節」は **paragraphs[].section から直接取得**すること）。
- manifest：vol17 entry を vol16 直後に登録・summary（total_files 51→52・primary 37→38・kk/gd present 38→39）。char_counts kakikudashi 29,271／gendaigoyaku 45,921／genten 16,024／paragraphs 95。

## genten（CBETA T1796_017）
- Chrome で `https://cbetaonline.dila.edu.tw/zh/T1796_017` を取得（`#body` の `.juan/.byline/.head/.div-pin` 構造）。
- 夾註79（`.inline-note`）を ( )→〔 〕化／`.lb`(行番号803)・`.lb_br`・`.noteAnchor`・`.note-link`・`.scan-image-display-btn`・`.glyphicon`・`.label`・`.lineInfo` 除去／残存校異 [A1]-[A4] 除去。
- 悉曇は CBETA の IAST を**半角括弧で温存**（(raṃ)(va) 等）。gaiji 𡀩（U+2102D 等）Unicode 保持。
- **content 図版1点**：第一印の三角漫荼羅 `T39p0750_01`。**重要**：CBETA の `.div-figure` は図像だけでなく**第一印の本文（其第一印者…其真言曰）を内包**するため、div-figure 全体を置換せず**内部の img のみを〔図 T39p0750_01〕に置換し本文を保持**した（当初 div-figure 全置換で第一印本文192字を落とす不具合→修正済み）。
- バイト一致：**Chrome の多重DL制限**で初回以降の blob download が保存されず（同一プロファイルで2回目以降ブロック）。初回DL版は SHA-256 `db4b7dd0…` でブラウザ⇔Python バイト一致を確認済みだが第一印本文を欠く版だったため、当該192字ブロックを CBETA 本文どおり補入。補入版を**ブラウザ正本 window.__genten と UTF-16長 16,071＋FNV-1a 2268135876 で完全一致照合**し byte 同一性を確認（DL不能のため SHA-256 の代替に UTF-16長＋FNV-1a を採用）。
- corpus.genten 投入・genten_unavailable_reason 削除・char_counts.genten=16,024・manifest genten_present 25→26。
- clean txt 保存：`_dev_references/dainichikyo-sho-vol17_build/genten_T1796_017_clean.txt`。

## Phase2（横断索引化・41著作目）
- `_dev_references/extract_{terms,citations,sanskrit,kaimyo_jukugo,persons,places}_dict.py` の `DICT_CORPUS_LIST` と `aggregate_indices.py` の `ALL_CORPORA` に vol17 追加。
- per-corpus 7本生成（`data/mikkyou/index_dainichikyo-sho-vol17_*.json`）：terms 9種 occ141／citations（涅槃経・仏性論・宝蔵経・大方便経・文殊経）／kukai_works 0／sanskrit 9（raṃ/vaṃ/saṃ/haṃ/aṃ/ā/khi 等の悉曇 IAST）／kaimyo／persons 16／places。
  - 注意：当初 marker 文言「CBETA音写」が sanskrit に "cbeta" として誤検出されたため、marker を「音写」に修正のうえ再抽出（cbeta 除去）。
- aggregate 7本再生成（**41著作**・corpora_count 40→41・summary.indexed_corpora 各40→41）。manifest aggregate stats も全カテゴリ再同期。
- **注意（既存挙動の踏襲）**：places の「殷/周」等の dynasty 検出は seed 辞書由来の既存挙動（vol11-16 同型）。vol17 のみ是正せず踏襲（seed の全体見直しは別課題）。

## 次フェーズ（push2＝motif）— Phase A 合意（巻第二〜十六 同運用・踏襲）
- 著者＝善無畏口述/一行筆受＝**非空海** → 全 motif に「引用形式:典籍曰く」・大師系タグ非付与・source に著者保持。
- 共通タグ：`category:密教教学`／`出典:大日経疏 巻第十七`／`引用形式:典籍曰く`。
- gabun（雅文体訳）は意図的未設定・連動軸は完走後 retrofit・1段=1motif（束ねは語中切れ等のみ）。
- 首題/撰号/品題（k001/k002/k003/k014/k036/k063/k065）は motif 化しない → **motif 対象は本文88段**。
- **m3745 から連番**。判定表は全ラウンドまとめて提示→確認後止めず一気に処理（新運用）。着手前に `references/motif-extraction.md` を再読。**「節」は corpus の paragraphs[].section から直接取得し、節==corpus.section を全件 assert**（vol16 の判定表ずれ事故の再発防止）。

## 次フェーズ（push3＝kaimyo-app 同期）
- 要フォルダ接続（kaimyo-app）。motifs.json コピー・SHA-256 一致確認。motif 完走後。

## 検証ログ（pass）
- Phase1：JSON再パースOK・NUL0・全95段訳済・半角括弧0（kk/gd）・段落連結（図像標識除外）assert pass・validate 52/52。
- genten：UTF-16長16,071＋FNV-1a でブラウザ正本とバイト同一性照合・夾註/校勘/gaiji/悉曇/図版検査・validate 52/52。
- Phase2：per-corpus 7本＋aggregate 7本生成・indexed_corpora 各41・validate 52/52。

## commit_push 注意
- 標準 `commit_push.bat` は package.json 等の幻の staged 削除で Step4.5 中止するため使わない。**専用 `commit_vol17_push1.bat`**（git reset HEAD→vol17 対象パスのみ stage→ステージ済み削除のみ安全チェック→commit→push）を用意。
- push 後は `git show HEAD:data/kukai/dainichikyo-sho-vol17.json` 等で反映を確認（マウント同期遅延に注意）。

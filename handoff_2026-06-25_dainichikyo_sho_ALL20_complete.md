# handoff 2026-06-25 — 大日経疏（T1796）全20巻 完結 総括／push3 kaimyo-app 同期 完了

## 到達点
**大日経疏（大毘盧遮那成仏神変加持経疏・T1796 vol.39・善無畏口述/一行筆受）巻一〜二十 全20巻**の
倉庫取込が**完結**。巻第二十（最終巻）の push1（取込）／push2（motif）／push2 補遺（motifs.json 是正）／
push3（kaimyo-app 同期）まで完了。**全20巻 corpus／genten／横断索引／motif 完備**。

- buddhist-data-api：corpus 55 files（_corpus_manifest 含む）・横断索引 44 著作目・genten_present 29。
- motifs.json：total **4072**・最終 **m4041**・schema_version 0.2・schema_history 295。
- kaimyo-app：motifs.json 同期済（total 4072・vol20 83件・倉庫とバイト一致＝push3_sync_kaimyo.bat の fc /b で確認）。

## 大日経疏 全20巻 motif 件数（from_corpus・合計 1,353件）
| 巻 | corpus | motif数 | 主要品 |
|---|---|---|---|
| 巻第一 | dainichikyo-sho-vol1 | 68 | 入真言門住心品（序・三句・六無畏 前段）※原 7 著作期に抽出（m-id 低位） |
| 巻第二 | dainichikyo-sho-vol2 | 105 | 住心品之余（三十外道破・六十心・百六十心・三劫・信解行地） |
| 巻第三 | dainichikyo-sho-vol3 | 71 | 六無畏・十縁生句十喩／具縁品 品題釈・大悲胎蔵 |
| 巻第四 | dainichikyo-sho-vol4 | 61 | 具縁品之余（択地・治地・白檀漫荼羅・弟子摂受） |
| 巻第五 | dainichikyo-sho-vol5 | 60 | 具縁品之余（三世無障礙智戒・中胎八葉・三部諸尊三昧耶形） |
| 巻第六 | dainichikyo-sho-vol6 | 42 | 三昧耶形図法・成菩提印・制底＝法身舎利・八地＝観自在 |
| 巻第七 | dainichikyo-sho-vol7 | 68 | 五十字門（字輪）・旋陀羅尼・加持身＝本地法身 |
| 巻第八 | dainichikyo-sho-vol8 | 54 | 漫荼羅供養法・寂然護摩・灌頂壇・慶賀偈 |
| 巻第九 | dainichikyo-sho-vol9 | 59 | 具縁品之余末／息障品（不動明王・摩醯首羅降伏） |
| 巻第十 | dainichikyo-sho-vol10 | 73 | 息障品之余／普通真言蔵品／世間成就品 |
| 巻第十一 | dainichikyo-sho-vol11 | 74 | 悉地出現品（三世無量門・荘厳清浄蔵三昧・阿字布字観） |
| 巻第十二 | dainichikyo-sho-vol12 | 58 | 悉地出現品之余／成就悉地品／転字輪漫荼羅行品 |
| 巻第十三 | dainichikyo-sho-vol13 | 67 | 転字輪漫荼羅行品之余／密印品（如来身密印・諸菩薩印） |
| 巻第十四 | dainichikyo-sho-vol14 | 52 | 密印品之余／字輪品／秘密漫荼羅品 |
| 巻第十五 | dainichikyo-sho-vol15 | 78 | 秘密漫荼羅品之余（造立次第・潅頂・悉地・護摩） |
| 巻第十六 | dainichikyo-sho-vol16 | 66 | 秘密漫荼羅品之余／入秘密漫荼羅品／入秘密漫荼羅位品 |
| 巻第十七 | dainichikyo-sho-vol17 | 88 | 秘密八印品／持明禁戒品／阿闍梨真実智品／布字品／受方便学処品 |
| 巻第十八 | dainichikyo-sho-vol18 | 45 | 受方便学処品之余／百字生品／百字果相応品 |
| 巻第十九 | dainichikyo-sho-vol19 | 81 | 百字位成品〜護摩法品（21〜27 の7品） |
| 巻第二十 | dainichikyo-sho-vol20 | 83 | 護摩法品之余／本尊三昧品／無相三昧品／世出世持誦品／囑累品（最終） |
| **合計** | | **1,353** | |

## 全巻通しての運用一貫性（巻第二〜二十）
- **著者帰属**：善無畏口述/一行筆受＝非空海 → 全 motif `引用形式:典籍曰く`・大師系タグ非付与・source に著者保持。
- **gabun**：全巻 意図的未設定（経典注釈系・全件 典籍曰く）。`motifs_without_gendai_gabun_intentional` に各巻 round_all キー。
- **連動軸 sg 新設**：全巻通して**新設なし**（既存軸 sg07 三句法門／sg08 阿字本不生／sg21 浄菩提心／sg27 自心本性清浄 等の被覆拡張のみ・core verbatim 限定 retrofit）。sg 総数 31 不変・famous 31 不変。
- **段落化**：元 doc 巨大ブロックを科文・話題境界で段落化・1段=1motif・段落結合＝原 doc 完全再現 assert。
- **genten**：全巻 CBETA 線上閱讀 T1796_0NN を Chrome 経由 #body 抽出・夾註〔〕化・校勘/行番号除去・悉曇 IAST 半角温存・gaiji Unicode 温存・UTF-16長＋FNV-1a＋チャンク hash でバイト同一性照合。manifest genten_present に計上。
- **埋込画像（悉曇種子字）**：vol18（百字生品 迦字四転）・vol20（囑累品 金剛手嚩/蓮花尊娑/文殊麼 五転）で doc 埋込画像を本文転記＋種字割注化・読みは CBETA 音写統一（ケンシン裁定）。
- **citations 名義釈是正**：vol14/19 で名義釈の『仏』『如来』等 偽書名を「」へ是正。vol20 は名義釈品なく是正不要（4種全て真正書名）。

## 巻第二十 push 履歴（最終巻）
1. **push1**（6c7c039）：取込＝Phase1＋genten＋Phase2 横断索引化（44著作目）。全90段（本文82＋構造7＋種子字 k080）。
2. **push2**（24281bf）：motif 抽出 round_all（m3959-m4041・83件）＋連動軸 retrofit（+14 連動タグ）＋gabun。
   - **※注意（再発防止）**：push2 コミットは CLAUDE.md／handoff／build dir を含んだが、**マウント同期ラグで data/indices/motifs.json が旧版（3989）のまま staging されコミット漏れ**。working tree は 4072 で無傷だった。
3. **push2 補遺**：`commit_vol20_push2_fix.bat`（staged 検証ガード付き）で motifs.json（4072）を是正コミット。
4. **push3**：`push3_sync_kaimyo.bat`（倉庫コミット確認→コピー→certutil SHA-256＋fc /b バイト一致）→ kaimyo-app `commit_motifs_sync.bat` で同期コミット。

## 教訓（次巻以降の他著作で踏襲）
- **bash で JSON を書いた直後の専用 commit bat は、motifs.json の staging 漏れに注意**（マウント同期ラグ）。commit bat に「対象ファイルが staged か」を `git diff --cached --name-only | findstr` で検証するガードを入れる（push2_fix・push3 bat で実装済）。コミット後は必ず `git show HEAD:data/indices/motifs.json | findstr total_motifs` で committed blob を確認する。
- サンドボックス（bash）が落ちても、push3 同期は Windows バット（copy＋certutil＋fc /b）で完結できる。

## 残課題
- **大日経疏 T1796 全20巻＝完結**。後続の取込対象（他著作）があれば別途。倉庫 corpus 55・横断索引 44 著作・motifs total 4072。
- 本 handoff／push3 関連 bat（`push3_sync_kaimyo.bat`・`commit_vol20_push2_fix.bat`）は gitignore（/*.bat）。CLAUDE.md line1 への全20巻完結エントリ追記は任意（push2 エントリで「全20巻 corpus/genten/横断索引/motif 完備」を既述）。

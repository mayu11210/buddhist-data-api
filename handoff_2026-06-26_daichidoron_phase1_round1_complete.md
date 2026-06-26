# 引き継ぎ：大智度論（空海引用集）Phase1 Round1 完了

日付：2026-06-26
対象：data/kukai/daichidoron.json（新設）

## 方針（ユーザー裁定済）
- スコープ：弘法大師空海の真撰著作が引用・言及する『大智度論』（大正蔵 No.1509）
  の箇所を集成する「引用アンソロジー型」corpus。
- 含める引用タイプ：逐語引用・別称引用・書名言及の**全タイプ**。
- 各段落の中身：**genten（漢文・引用＋前後の文脈）＋gendaigoyaku（現代語訳）**。
- **書き下し（kakikudashi）層は持たない**（ユーザー「書き下しは要らない」）。
- genten の範囲：**引用＋前後の文脈**（ユーザー裁定）。空海の引用句だけでなく、
  T1509 のその引用が属する論述のまとまり（前後あわせ概ね300〜600字）を収める。
  → 文脈は T1509 原典から取得が必要（空海側の引用文だけでは前後が無い）。
- 大日経疏・発菩提心論疏など他者撰述（一行等）は「空海が引用」ではないので除外。

## 構造
- collection_type: "citation_anthology"。
- paragraphs[] 各要素＝『大智度論』の一引用箇所：
  id / section_major（引用元の空海著作名）/ section / kakikudashi（空）/
  genten（漢文）/ gendaigoyaku（現代語訳）/ citation{kukai_work, kukai_corpus_file,
  kukai_locus, daichidoron_juan, citation_type, via}。
- manifest data_status：kakikudashi=false, gendaigoyaku=false（top-level 方式・
  per-paragraph 訳は untranslated_count=0 で担保）, specialty_sections=['collection_type']。
  ※ これらは validate_corpus.py の actual と一致必須（auto-register は kakikudashi=true・
  specialty=[] と誤設定するので手で是正した）。

## Round1（完了・k001-k004／全件 逐語引用・引用＋前後文脈）
- k001 二教論 巻第五（摩訶薩埵釋論第九〜菩薩功徳釋論第十・等忍の段）
  八不偈〜衆生等忍〜法等忍〜諸法不生不滅偈〜已得解脱〜無生忍＝助仏道初門
- k002 二教論 巻第九（初品中放光釋論之余）仏の二種身（法性身・父母生身）
- k003 二教論 巻第三十八（釋往生品第四之上）二諦（世諦・第一義諦）
- k004 吽字義 巻第二十七（釋初品中大慈大悲義第四十二）三智（薩婆若の三種名）
- genten は CBETA 線上閱讀 T25n1509 の各巻を Claude-in-Chrome（get_page_text）で
  取得し、引用句＋前後文脈を収録。CBETA 校勘記号除去・夾註は〔 〕温存。
  k001 は巻5本文と逐語一致を確認済。
- 倉庫側 validate_corpus.py：ERROR/WARNING 0。

## T1509 本文取得の確立した方法（重要）
- CBETA online reader は JS 描画。web_fetch では空応答（17MB単一XMLも空）。
- **Claude-in-Chrome で `https://cbetaonline.dila.edu.tw/zh/T1509_{巻3桁}`（例 T1509_005）
  に navigate → get_page_text で巻全文の漢文が取得できる**（実証済）。
- 長い巻は subagent に「引用句＋前後文脈のみ抜粋・校勘記号除去」で依頼すると
  本体コンテキストを節約できる（R1 の巻9/27/38 はこの方式）。

## 残ラウンド（未着手）
全引用 locus は90 hit 抽出済（下記は distinct 主要分）。
### 二教論（残）
- 別称言及：「菩提・智度・摩訶衍」（所依経論列挙）、「楞伽法仏…智度性身妙色之句」、
  龍猛『釈論』＝大智度論の別称（機根離れ）。
### 十住心論（大日経疏＝善無畏釈 経由の智度論引用。via に "大日経疏（善無畏釈）" を明記）
- 無始生死「世間若衆生若法皆無有始…」
- 知者見者「目覩色名為見者、五識知名為知者…」／神我量「有計神大小随人身…」／
  摩奴闍「智度翻為人」／摩納婆「有計神在心中微細如芥子…」／十六知見
- 五戒分「戒有五種…若受一戒是名一分…満分」／六斎日（五通仙人断食）／
  星宮日月「修下之下品十善生諸星宮…」／八十部尸羅波羅蜜／
  麟角衆出「言已得決択分成衆出者…」／三昧調直定（「大論云、善心一処住不動…」※
  これは摩訶止観経由）／鼻下糞「如人鼻下有糞…」／閻浮提人「持下品五戒則生其中…」
- 別称言及：法華・中論・智度を所依（天台所依列挙）。
### 秘蔵宝鑰
- 「智度には入仏道の初門と名づく」（大日経疏経由・別称）／法華・中論・智度（所依列挙）。
### 声字実相義
- 「法華・華厳・智度等にも種種の色の差別を説けり」（書名言及）。
### 性霊集（多くは訳注の典拠言及。本文逐語ではない＝citation_type:典拠言及）
- 芥子劫/磐石劫＝巻5／九相観（九相詩）＝巻21・22／恒河女人（子を救い天生）＝巻30／
  五眼＝巻33／四毒蛇（四大）／草繋比丘／護鴈／一切衆生皆依食住＝巻31／途聞途説＝巻31 等。

## 次にやること
1. ユーザーに commit_push.bat 実行を依頼（Round1 反映）。
2. T1509 原典の逐一校合方法を確定（CBETA T25n1509・17MB 単一XML。web_fetch は
   45KB 級は取得可だが17MBは空応答。per-巻 取得は Claude-in-Chrome で CBETA online
   reader をレンダリングするか、巻指定の取得手段を要検討）。
3. Round2 以降：十住心論経由分（via 明記）→秘蔵宝鑰→声字実相義→性霊集の順を推奨。
4. 完走後 Phase2 横断索引化（7カテゴリの DICT_CORPUS_LIST/ALL_CORPORA に
   daichidoron.json 追加）、Phase3 motif 抽出。

## 落とし穴メモ
- 文書（CLAUDE.md/handoff/commit_message）はホスト側ツールで編集（マウント同期ラグ）。
- 全角括弧（）厳守・割注〔 〕。genten/gendaigoyaku に半角 () を混ぜない。
- 既存 corpus・他著作には触れない（daichidoron.json への追記のみ）。

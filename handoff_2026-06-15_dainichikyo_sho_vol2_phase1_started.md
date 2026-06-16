# 引き継ぎメモ 2026-06-15 大日経疏 巻第二 Phase1 着手（段落化＋骨組み＋現代語訳バッチ1）

**日付**：2026-06-15
**種別**：kakikudashi-data Phase1（corpus 取込・進行中／現代語訳バッチ制・複数セッション）
**起点 HEAD**：`134914e`（発菩提心論鈔 retrofit36＋gabun）
**ステータス**：Phase1 着手・**WIP（訳済 6/106）**・未 commit / 未 push（commit_push.bat 実行待ち）
**新規**：`data/kukai/dainichikyo-sho-vol2.json`（dict_paragraphs・kakikudashi 全充填・gendaigoyaku 6段のみ）

## 素材・著者
- doc『大毘盧遮那成佛神変加持経疏 巻第二』。大日経疏 巻第一（dainichikyo-sho-vol1）の続巻＝入真言門住心品第一之余。
- 著者：善無畏三蔵 口述・一行阿闍梨 筆受（**非空海**→ motif 抽出時 引用形式:典籍曰く 想定）。source に保持。

## ケンシン裁定（2026-06-15）
- 現代語訳：**Claude が butten-yasashii-yaku でバッチ訳（複数セッション）**。
- JSON 構造：**段落形式 dict_paragraphs**（理趣釈・発菩提心論鈔と同形式・巻第一フラット形式とは異なる）。

## 段落化（106 段落 k001-k106・kakikudashi 38,464 字）
outline 10 区分（para_range＝k番号）：
| id_range | 大科 | 小科 |
|---|---|---|
| k001 | 品題 | 入真言門住心品第一之余 |
| k002-k018 | 違理の心〔外道破〕 | 我分三十事の遮破（尊貴〜声非声） |
| k019-k023 | 順理の世間心 | 世間八心・殊勝心・決定心 |
| k024-k079 | 六十心 | 六十心の総説と一々の相（貪心〜猨猴心） |
| k080-k091 | 百六十心・三妄執 | 五根本煩悩・百六十心・世間三妄執を越える |
| k092-k097 | 出世間心〔第一劫〕 | 五蘊性空の五喩・法無我〔無縁乗〕・阿頼耶の幻喩 |
| k098-k099 | 第二劫 | 自心本不生〔心主自在〕 |
| k100-k101 | 第三劫 | 極無自性心〔真言門菩薩行・空性十喩〕 |
| k102 | 応供の宝珠喩 | 三劫の始終と摩尼宝珠の譬喩 |
| k103-k106 | 信解行地 | 信解行地・三心・十心・十地 |
- 長段落5件（>1500字）は大乗荘厳経論の偈・真言門段 等の分割不可の長文引用ゆえ許容。

## 現代語訳バッチ（butten-yasashii-yaku・平易・割注〔〕で原語温存・半角括弧禁止）
- **batch1 完了：k001-k006**（品題＋外道破前半 尊貴/自然/内我/人量/遍厳/寿者）。訳済 6/106。
- 残バッチ目安：batch2 外道破後半 k007-k018／batch3 八心殊勝心 k019-k023／batch4-8 六十心 k024-k079（~12段ずつ）／batch9 百六十心三妄執 k080-k091／batch10 第一劫五喩法無我 k092-k097／batch11 第二三劫宝珠 k098-k102／batch12 信解行地 k103-k106。

## ビルド手順（次セッション継続）
ビルド素材は **`_dev_references/dainichikyo-sho-vol2_build/`** に永続保存：
- `paras.json`（106段＋題名 107要素）・`trans_1.json`（k001-k006 訳）・`config_template.json`（<REPO> を実パスに置換）・`vol2_kakikudashi_source.txt`（底本）。
- 継続手順：(1) `trans_2.json` 等に {"7":"訳",...}（キー＝k番号）を書く。(2) config_template の `<REPO>` を当セッションの実パス（/sessions/<id>/mnt/buddhist-data-api）に置換し config.json 化。(3) `python3 <skill>/scripts/build_corpus.py config.json` で dainichikyo-sho-vol2.json 再生成。(4) 半角括弧0・NUL0 確認。
- スキル scripts：build_corpus.py（paras＋trans_*→corpus）／validate_corpus.py。

## 残課題（順）
1. 現代語訳 全106段 完訳（バッチ継続・複数セッション）。
2. 全訳後：manifest 登録（register_manifest.py・dict_paragraphs・role_complete）→ 倉庫側 validate_corpus.py 全pass。
3. genten 後送：SAT/CBETA 大正蔵 T1796 vol.39 巻第二（巻第一は p.579a-593a なので巻第二は p.593a〜）。
4. Phase2 横断索引化（extract6＋aggregate に dainichikyo-sho-vol2 追加）。
5. Phase3 motif 抽出（Phase A：著者=善無畏/一行＝非空海→引用形式:典籍曰く・連動軸候補 阿字本不生 sg08／浄菩提心 sg21／六十心 等）。

## 留意（git）
- WIP corpus は manifest 未登録（未訳段落で validate を割らないため）。commit_push.bat 前に fix_index.bat。

## 次セッション確認
1. CLAUDE.md 冒頭 → 本メモ → git log
2. dainichikyo-sho-vol2.json：106段・訳済6・kakikudashi 38,464
3. _dev_references/dainichikyo-sho-vol2_build/ のビルド素材でバッチ継続

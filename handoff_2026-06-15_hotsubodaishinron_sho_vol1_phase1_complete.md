# 引き継ぎメモ 2026-06-15 発菩提心論鈔 第一巻（宥快）Phase1 取込 完了

**日付**：2026-06-15
**種別**：kakikudashi-data Phase1（corpus 取込・段落化→現代語訳→JSON 化→manifest 登録）
**起点 HEAD**：`7546ab1`（理趣釈 retrofit 35。並行セッション完了・コミット済を着手後に確認）
**ステータス**：Phase1 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**新規著作**：`data/kukai/hotsubodaishinron-sho-vol1.json`（primary_corpus 14 件目）

---

## 素材
- ユーザー提供 doc『発菩提心論鈔 第一巻 宥快.doc』（uploads）。
- 著者：宥快〔ゆうかい・1345-1416〕。高野山の学僧。**著者確定（伝・ではない）**。
- 注釈対象（base_text）：菩提心論＝金剛頂瑜伽中発阿耨多羅三藐三菩提心論（龍樹著・不空訳・
  T1665）。倉庫内 `bodaishinron.json`。注釈書としては浄厳『菩提心論講要』
  （bodaishinron-kouyou.json）に次ぐ 2 件目。

## 成果（段落・科段）
- 173 段落抽出（先頭が title 行）→ title_is_first で本文 172 段（k001-k172）。**全訳済・未訳 0**。
- k001-k050＝巻頭の科段目次、k051 以降が本文（牒文＋論義見出し＋注釈本文の交互構成）、
  k172＝「一段畢」。
- outline 8 区分：
  | 区分 | id 範囲 | section_major / section |
  |---|---|---|
  | 目次 | k001-k050 | 目次／科段目次 |
  | 序説 | k051-k063 | 序説／当論総論（密蔵肝心・製作時代・両部分別・集義釈経・不空所造かの弁） |
  | 題号釈① | k064-k095 | 題号釈／金剛頂瑜伽中（両題・五言法喩・金剛の諸義・頂・瑜伽・中・六字多義） |
  | 題号釈② | k096-k121 | 題号釈／発阿耨多羅三藐三菩提心（梵語・菩提・心・菩提心・発心・論の釈） |
  | 副題釈 | k122-k135 | 副題釈／瑜伽惣持教門説菩提心観行修持義（惣持四種五種・教門・説菩提心・観行修持） |
  | 造者釈 | k136-k161 | 造者釈／龍猛菩薩造（龍猛龍樹の得名・出現・寿限・地位・部数・菩薩・造・撰号） |
  | 訳者釈 | k162-k171 | 訳者釈／大興善寺三蔵沙門大広智不空奉詔訳 |
  | 結 | k172-k172 | 結／一段畢 |

## 文体
- butten-yasashii-yaku：本文は平易な現代語に組み替え、原語・術語は割注〔 〕で多めに温存。
  経名のみ明示・T 番号/訳者名は本文に出さず。半角括弧 0。
- 内容上の特徴：一義（諸説）併記が多い学派論争型。智証（円珍）の「不空造」説への批判
  （k063）、安然の「菩提＝覚」説への批判（k101）、菩提心の四重秘釈と空海による再配置
  （k111）などが山場。

## genten
- 漢文原典は未収録（書き下しのみ）。`genten=""`・`genten_source` に底本明記。
  bodaishinron-kouyou と同方針。

## manifest / 逆リンク
- `_corpus_manifest.json`：dict_paragraphs / primary_corpus で登録
  （relations.commentary_of=bodaishinron.json）。char_counts 自動算出。
- summary 足し算：total_files 26→27・role_breakdown.primary_corpus 13→14・
  role_complete_files 14→15・kakikudashi_present 13→14・gendaigoyaku_present 13→14。
  genten_present 11・indexed_corpora 各 15 は据置（Phase2 未了）。
- `bodaishinron.json` の `commentaries` に逆リンク追加
  （bodaishinron-kouyou.json に続き hotsubodaishinron-sho-vol1.json）。

## 検証（全 pass）
- スキル同梱 validate_corpus.py：JSON 再パース OK／NUL0／段落 172・未訳 0／現代語訳 半角括弧 0。
- 倉庫側 `_dev_references/validate_corpus.py`：manifest 27＝実ファイル 27、char_counts 整合、
  メカニカル整合性 OK。
- ホスト Grep 反映確認：corpus（section・一段畢・translated 172）・manifest・bodaishinron
  逆リンク すべて反映。
- build script：outputs/config_hotsubodai.json・trans_batch1-7.json（累積ビルド）。

## 並行セッション注記
- 着手時 HEAD は 3d3f92e（理趣釈 R3）だったが、作業中に並行セッションが retrofit 35 を
  コミット（HEAD 7546ab1）。当該作業は完結・ワーキングツリーは motifs.json 等クリーン。
  以後は本セッションが単独書き手。
- index に package.json / render.yaml / start.bat / tsconfig.json / vercel.json・
  outputs/ バックアップ等の **phantom 削除ステージ**が着手前から存在。各ファイルはホスト
  実体あり（実害なし）。commit_push.bat は Step2 `git reset HEAD` で当該ステージを解消し、
  Step4.5 SAFETY CHECK（deleted: 検出で abort）で再発防止するため、通常実行で安全。

## 残作業
1. **Phase2 横断索引化**（7 カテゴリ）：extract 6 本の DICT_CORPUS_LIST と
   aggregate_indices.py の ALL_CORPORA に hotsubodaishinron-sho-vol1.json 追加 →
   per-corpus 索引生成 → 集約再生成 → manifest index_status 付与・indexed_corpora +1。
2. **Phase3 motif 抽出**：Phase A 合意（著者＝宥快 確定→大師系タグ不可・引用形式タグ要検討、
   束ね方針、gabun 要否）→ ラウンド分割。references/motif-extraction.md 必読。
3. 第二巻以降が提供されれば同手順で追加取込。

## 次セッション開始時の確認
1. `git log --oneline -3`（HEAD が本 Phase1 コミットであること）
2. `data/kukai/hotsubodaishinron-sho-vol1.json`：translated 172・outline 8 区分
3. Phase2 着手なら _dev_references の extract/aggregate スクリプト群を参照

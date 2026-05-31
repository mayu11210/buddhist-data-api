# 引き継ぎメモ：十住心論 横断索引化＋manifest 昇格（push 前・commit 待ち）

**日付**：2026-05-31
**種別**：本体マージ仕上げ（W3 jujushinron → buddhist-data-api 本体の最優先タスク A＋B）
**ステータス**：作業完了・**全検証 pass・ただし未 commit / 未 push**（commit_push.bat の巻き込み問題のため住職判断待ち）
**起点 HEAD**：`c18093e`（十住心論 motif 中間マージ）。直前 `597a0e8`（jujushinron.json 本文3点 取込）。

---

## 今回やったこと（最優先タスク A＋B）

前回までに済んでいた中間マージ（597a0e8 で本文3点、c18093e で motif jw001-045→m2175-m2219）に続き、
**他の完備著作と同じ状態にする仕上げ**として横断索引化と manifest 昇格を実施。bodaishinron 候補 D と同手順。

### A-1 横断索引化（スクリプト修正）
6 本の extract と aggregate に `jujushinron` を 11 著作目として追加（bodaishinron 行の直後）：
- `_dev_references/extract_terms_dict.py` / `extract_citations_dict.py` / `extract_persons_dict.py` /
  `extract_places_dict.py` / `extract_sanskrit_dict.py` / `extract_kaimyo_jukugo_dict.py`（`'jujushinron.json'`）
- `_dev_references/aggregate_indices.py`（`'jujushinron'`・拡張子なし）

### A-2 per-corpus 索引 7 本を生成（data/mikkyou/・新規ファイル）
`python3 _dev_references/extract_<cat>_dict.py --corpus jujushinron.json` を 6 本実行。
- index_jujushinron_terms.json … 19 語 / 539 件
- index_jujushinron_citations.json … 179 語 / 503 件
- index_jujushinron_kukai_works.json … 2 語 / 3 件
- index_jujushinron_sanskrit.json … 1 語 / 1 件
- index_jujushinron_kaimyo.json … 38 語 / 552 件
- index_jujushinron_persons.json … 38 名 / 403 件
- index_jujushinron_places.json … 20 地 / 237 件

### A-3 集約 index_<cat>_all.json 7 本を 11 著作で再生成（既存ファイルを上書き）
`python3 _dev_references/aggregate_indices.py`。総占有 before→after：
- terms 2281→2820・citations 1847→2350・kukai_works 52→55・sanskrit 2671→2672・
  kaimyo_jukugo 4454→5006・persons 2434→2837・places 639→876。全 7 本で corpora_count 10→11。

### A-4 _corpus_manifest.json 昇格
jujushinron を `excerpt_stub` → `primary_corpus`。
- char_counts は**実ファイル基準**：text 330・kakikudashi **159,666**・gendaigoyaku **292,975**・genten **91,904**。
- index_status 7 カテゴリ付与。
- summary：primary_corpus 10→11・excerpt_stub 6→5・role_complete_files 11→12・
  kakikudashi/gendaigoyaku_present 各 +1・genten_present 8→9・indexed_corpora 各 10→11。
- aggregate_indices：source_corpora に jujushinron 追加・corpora_count 10→11・各カテゴリ統計更新。

### B 本体 CLAUDE.md 更新
- タイトル行（line 1）の `2026-04-25〜・` 直後に 2026-05-31 マーカーを挿入（retrofit28 マーカーは温存）。
- 進捗ヘッダ（line 960 `## 現在の進捗`）の日付を 2026-05-25→2026-05-31 にし本作業の要約を追記（W1 完走マージ記述は温存）。

---

## ⚠️ 重要：未 commit。なぜ止めたか（次セッションの最初の判断事項）

`commit_push.bat` はディレクトリ単位 add（`_dev_references/`・`data/kukai/`・`data/mikkyou/`・`*.md`・`outputs/` ほか）。
そのため今回の成果物だけでなく**以前のセッションからの未コミット変更を大量に巻き込む**。特に：
- ルートの `package.json` `render.yaml` `start.bat` `tsconfig.json` `vercel.json` が **削除ステージ(D)** 状態
  → bat の Step 4.5 安全ガードが `deleted:` を検出して **commit を中断する**見込み。
- `outputs/` に retrofit 系の dryrun/backup/スクリプトが多数（??）。
- `_dev_references/jujushinron_vol10/` の W3 作業ファイル 3 点が変更(M)。

→ このまま bat を回すと Step 4.5 で止まる可能性が高い。**今回分だけをクリーンに commit するか、巻き込みごと進めるか**を住職が決める必要があり、本セッションでは push せず保留した。

### 次セッションでの選択肢
1. **今回分だけ commit**（推奨）：専用の一回限り .bat を作り、対象を明示列挙して `git add` する。
   対象＝下記「今回の成果物ファイル一覧」。`package.json` 等の D 状態には触れない（別途整理）。
2. **巻き込みごと commit**：既存 commit_push.bat を使うが、Step 4.5 で止まるので、削除(D)を意図的に扱う
   dedicated .bat（`git rm` 明示）か、`git reset` で D を外してから実行する等の前処理が必要。
3. まず `git status` を確認し、住職と相談して方針決定。

---

## 今回の成果物ファイル一覧（commit 対象）

変更(M)：
- `_dev_references/extract_terms_dict.py`
- `_dev_references/extract_citations_dict.py`
- `_dev_references/extract_persons_dict.py`
- `_dev_references/extract_places_dict.py`
- `_dev_references/extract_sanskrit_dict.py`
- `_dev_references/extract_kaimyo_jukugo_dict.py`
- `_dev_references/aggregate_indices.py`
- `data/kukai/_corpus_manifest.json`
- `data/mikkyou/index_terms_all.json`
- `data/mikkyou/index_citations_all.json`
- `data/mikkyou/index_kukai_works_all.json`
- `data/mikkyou/index_sanskrit_all.json`
- `data/mikkyou/index_kaimyo_jukugo_all.json`
- `data/mikkyou/index_persons_all.json`
- `data/mikkyou/index_places_all.json`
- `CLAUDE.md`
- `commit_message.txt`（今回作業用に書き換え済み）

新規(??)：
- `data/mikkyou/index_jujushinron_terms.json`
- `data/mikkyou/index_jujushinron_citations.json`
- `data/mikkyou/index_jujushinron_kukai_works.json`
- `data/mikkyou/index_jujushinron_sanskrit.json`
- `data/mikkyou/index_jujushinron_kaimyo.json`
- `data/mikkyou/index_jujushinron_persons.json`
- `data/mikkyou/index_jujushinron_places.json`
- `handoff_2026-05-31_jujushinron_cross_index_complete.md`（本メモ）

バックアップ（commit 不要・/tmp と outputs に退避済み）：
- `outputs/CLAUDE.md.bak_pre_jujushinron_indexB`
- `outputs/_corpus_manifest.json.bak_pre_jujushinron`
- `outputs/idx_backup_pre_jujushinron/`（集約 7 本の更新前）

---

## 最終検証（全 pass・2026-05-31）

```
scripts py_compile: 7/7 OK
jujushinron in all 7 lists: OK
NUL/JSON on 15 files: OK
aggregate 11-corpora + jujushinron: OK
validate_corpus.py RC=0 OK（manifest と実ファイル全一致）
manifest: primary=11 excerpt=5 role_complete=12 genten=9 agg=11
CLAUDE.md title+progress markers: OK（retrofit28・W1ヘッダ温存）
commit_message.txt bytes=2116
```

数値修正の経緯：当初 W3 handoff の「マージ予定字数」（kk156,213/gd284,909/gt91,397）で manifest を書いたが
validate_corpus.py が char_counts 不一致で FAIL。実際にコミット済みの jujushinron.json は字数が異なる
（kk159,666/gd292,975/gt91,904）ため、全数値を実ファイル・実索引から再計算して修正済み。

---

## 残・次段（任意・最優先タスク完了後の選択肢）

- 成句 sg28 以降の採番（如実知自心・九種住心無自性 等。阿字本不生は既存 sg08 で連動済み）。
- W3 motif 追補（巻十の字門各字義・巻二輪王段・巻六三性詳説/十地各地・巻九十玄門各門 等。45→100〜150 件）。
  追補したら次回マージで m2220 以降に追加。
- W3 リポジトリの凍結（archive 化・GitHub 操作）。
- `package.json` 等ルートの削除(D)状態・outputs/ 大量未追跡ファイルの整理（別タスク）。

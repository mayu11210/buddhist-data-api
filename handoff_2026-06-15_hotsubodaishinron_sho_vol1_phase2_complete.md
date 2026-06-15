# 引き継ぎメモ 2026-06-15 発菩提心論鈔 第一巻（宥快）Phase2 横断索引化 完了

**日付**：2026-06-15
**種別**：kakikudashi-data Phase2（横断索引化・7 カテゴリ）
**起点 HEAD**：`02545d8`（理趣釈 gabun 裁定）。発菩提心論鈔 Phase1 は `1e13c7d`。
**ステータス**：Phase2 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**対象**：data/kukai/hotsubodaishinron-sho-vol1.json（16 著作目・index_status 付与）

---

## 成果
- extract 6 本の DICT_CORPUS_LIST ＋ aggregate_indices.py の ALL_CORPORA に hotsubodaishinron-sho-vol1 追加（dict 型 15 著作目・性霊集含め 16 著作目）。
- per-corpus 索引 7 本生成（data/mikkyou/index_hotsubodaishinron-sho-vol1_*.json）：
  | カテゴリ | 件数 | occ | 備考 |
  |---|---|---|---|
  | terms | 19 | 146 | matched 13・kaimyo_suitable 11 |
  | citations | 95 | 210 | 付法伝15・大日経12・大日経疏11 ほか |
  | kukai_works | 4 | 10 | 菩提心論5・即身成仏義3 ほか |
  | sanskrit | 0 | 0 | 書き下しのみ・IAST なし＝妥当 |
  | kaimyo_jukugo | 11 | 109 | matched 8・review 0 |
  | persons | 19 | 202 | subcat 5・龍樹80/不空42/大日如来41 |
  | places | 15 | 25 | subcat 9・大興善寺5/西域5 |
- 集約 index_<cat>_all.json 7 本を 16 著作で再生成。集約 total_occ 増分が per-corpus 件数と全 7 カテゴリ一致を照合済。

## stats 差分（集約 total_occ）
- terms 3531→3677／citations 2374→2584／kukai_works 55→65／sanskrit 2684（不変）／
  kaimyo_jukugo 5533→5642／persons 3149→3351／places 939→964。

## manifest 更新
- hotsubodai entry に index_status（7 カテゴリ present）付与。
- summary.indexed_corpora 全カテゴリ 15→16。
- aggregate_indices.corpora_count 15→16・source_corpora に追加・description 追記・generated_at 2026-06-15。

## 検証（全 pass）
- 倉庫側 validate_corpus.py：manifest 27＝実ファイル 27・メカニカル整合 OK。
- 集約＝per-corpus 件数 全 7 カテゴリ一致（aggregate total_occ == per-corpus sum）。
- motifs.json 不変（Phase2 は索引のみ）。
- build/更新 script：outputs/phase2_add_corpus_hotsubodai.py・phase2_update_manifest_hotsubodai.py・phase2_hotsubodai_docs.py。バックアップ：outputs/_corpus_manifest.json.bak_pre_hotsubodai_index。

## 残作業
1. **Phase3 motif 抽出**：Phase A 合意（著者＝宥快 確定＝**大師系タグ不可**・引用形式タグ要検討〔大師曰く不可・典籍曰く 系か・宥快 注釈ゆえ要裁定〕・束ね方針・gabun 要否・連動軸は完走後 retrofit）→ ラウンド分割。references/motif-extraction.md 必読。172 段落・outline 8 区分。
2. 第二巻以降が提供されれば同手順で追加取込。

## 次セッション開始時の確認
1. `git log --oneline -3`（HEAD が本 Phase2 コミット）
2. _corpus_manifest.json：hotsubodai index_status 7 カテゴリ・indexed_corpora 16
3. Phase3 着手なら references/motif-extraction.md 必読・Phase A 著者帰属（宥快）裁定から

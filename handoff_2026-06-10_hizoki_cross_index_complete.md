# 引き継ぎメモ 2026-06-10 秘蔵記 横断索引化完了（hizoki を 12 著作目として全 7 カテゴリ索引化）

**日付**：2026-06-10
**種別**：横断索引化（最優先タスク α・ケンシン選択）
**起点 HEAD**：`5d84219`（秘蔵記取込）。jujushinron 横断索引化（2026-05-31）と同手順。
**ステータス**：作業完了・全検証 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）

---

## 本セッションの主な成果

### A-1 横断索引化（スクリプト修正）
6 本の extract と aggregate に `hizoki` を追加（jujushinron 行の直後）：
- `_dev_references/extract_terms_dict.py` / `extract_citations_dict.py` / `extract_persons_dict.py` /
  `extract_places_dict.py` / `extract_sanskrit_dict.py` / `extract_kaimyo_jukugo_dict.py`（`'hizoki.json'`）
- `_dev_references/aggregate_indices.py`（`'hizoki'`・拡張子なし）

### A-2 per-corpus 索引 7 本を生成（data/mikkyou/・新規ファイル）
- index_hizoki_terms.json … 19 語中 12 語一致 / 286 件
- index_hizoki_citations.json … 6 語 / 10 件
- index_hizoki_kukai_works.json … 0 語 / 0 件（雑記体口決書のため空。正常）
- index_hizoki_sanskrit.json … 0 語 / 0 件（訳は読みを仮名表記のため空。正常）
- index_hizoki_kaimyo.json … 11 語中 7 語一致 / 228 件
- index_hizoki_persons.json … 15 名 / 75 件
- index_hizoki_places.json … 9 地 / 19 件

### A-3 集約 index_<cat>_all.json 7 本を 12 著作で再生成
総占有 before→after（全 7 本で corpora_count 11→12）：
- terms 2820→3106（+286）・citations 2350→2360（+10）・kukai_works 55→55（±0）・
  sanskrit 2672→2672（±0）・kaimyo_jukugo 5006→5234（+228）・
  persons 2837→2912（+75）・places 876→895（+19）
- **増分は per-corpus 件数と全カテゴリで完全一致**（独立検証済）

### A-4 _corpus_manifest.json 更新
- hizoki に index_status 7 カテゴリ付与（jujushinron と同形式・実ファイル基準）
- summary.indexed_corpora 各カテゴリ 11→12
- aggregate_indices：source_corpora に hizoki 追加・corpora_count 12・各カテゴリ統計更新
- notes に索引化追記

### B validate_corpus.py の dict_paragraphs 対応（ケンシン承認済・本セッション）
旧 validator は dict_paragraphs 型（kakikudashi-data スキル取込の 6 ファイル：
bodaishinron-kouyou / dainichikyo-kaidai / rishukyo-kaidai / kongocho-kaidai /
dainichikyo / hizoki）を知らず「type 不一致」7 件を出していた（既存問題・索引化とは無関係）。
- dict_paragraphs 分岐を追加：paragraphs 数・段落合算字数を照合
- char_counts は「改行込み」（dainichikyo 等の手動登録）と「改行除き」
  （register_manifest.py 規約）の**両規約を許容**
- kaimyo_excerpt は機械判定不能のため dict_paragraphs では検証対象外
- paragraphs / outline / translation_status / format_note / author / base_text /
  base_text_ref / related / taisho_ref / genten_unavailable_reason は構造フィールド
  として specialty_sections に数えない
- 未訳段落があれば WARNING 表示（取込途中ファイルの検知用）

### C 既存不整合 2 件の是正（validator 拡張で発覚）
1. `bodaishinron.json`：6/7 の講要取込時に追加された top-level `commentaries` キーが
   manifest の specialty_sections に未反映 → `["commentaries"]` を記載。
   summary.with_specialty_sections 4→5。
2. `bodaishinron-kouyou.json`：manifest の gendaigoyaku 26,920 字が実測（26,907 字・
   改行除き）と不一致（登録後の微修正の更新漏れとみられる）→ 26,907 に補正・notes 追記。

---

## 最終検証（全 pass・2026-06-10）

```
py_compile: extract×6 + aggregate = 7/7 OK
hizoki in all 7 script lists: OK
per-corpus 7 ファイル + 集約 7 ファイル: NUL 0 件・JSON 再パース OK
集約増分 = per-corpus 件数: 全カテゴリ一致
validate_corpus.py: 全 24 ファイル整合 OK（ERROR 0・WARNING 0）RC=0
manifest: indexed_corpora 各 12・aggregate corpora_count 12
CLAUDE.md: タイトル行＋進捗ヘッダに 2026-06-10 マーカー追記（既存マーカー温存）
```

---

## commit 対象（commit_push.bat の dir 単位 add で全て拾われる）

変更(M)：extract×6・aggregate_indices.py・validate_corpus.py・
_corpus_manifest.json・index_*_all.json×7・CLAUDE.md・commit_message.txt
新規(??)：index_hizoki_*.json×7・本メモ

**巻き込み確認済**：outputs/ は bat の stage 対象外。ルート未追跡の
`_dev_scripts/`・`dainichikyo_genten.txt`・`遍照発揮性霊集.docx` も対象外（*.md のみ拾う）。
deleted ステージなし（Step 4.5 安全装置で停止しない見込み）。
バックアップは outputs/idx_backup_pre_hizoki/（集約 7 本）と
outputs/_corpus_manifest.json.bak_pre_hizoki_index に退避済（commit 不要）。

---

## 副次発見・要注意事項

1. **handoff_dainichikyo_honbun.md が古い**：内容が「訳済 137 段落」のままだが、
   実際は b5f5c86 で全 896 段落訳済・cba66ff で genten 64,901 字完備。
   次セッションで _archive/memos/ への移動または更新を推奨（今回は触っていない）。
2. **Cowork の mount 同期不具合（本セッション中）**：ホスト側 Edit の内容が
   サンドボックス側マウントに反映されない事象（validate_corpus.py が 7,292 バイトで
   切れて見える）。**実体（Windows 側）は完全**で、検証は /tmp ミラーで実施し pass。
   bat は Windows 側で動くため commit には影響なし。commit 後に
   `git show HEAD:_dev_references/validate_corpus.py | tail -3` で
   `sys.exit(main())` が見えることを確認すると安心。
3. ルート未追跡の `dainichikyo_genten.txt`（genten 取込の中間ファイル）と
   `_dev_scripts/`・outputs/ 配下の retrofit 系作業ファイルの整理は別タスクのまま。

---

## 残作業・次セッションの選択肢

- (β) 秘蔵記 motif 抽出（retrofit/workshop 方式の方針確認から・Phase A 軸設計合意が必要）
- (γ) 別著作の書き下しデータ化（kakikudashi-data スキル。ルートに『遍照発揮性霊集』
  docx が置かれているのが見える——次対象候補かはケンシンに確認）
- 未索引の dict_paragraphs 残り 5 件（bodaishinron-kouyou・各開題 3 件・dainichikyo）の
  横断索引化（本セッションと同手順で 1 セッション 1〜5 件可）
- handoff_dainichikyo_honbun.md の整理（上記 副次発見 1）

## 次セッション開始時の流れ
1. CLAUDE.md → 本メモ → git log --oneline -3（HEAD が本コミットであること）
2. grep "hizoki" _dev_references/extract_terms_dict.py で索引化反映を内容検証
3. python3 _dev_references/validate_corpus.py で RC=0 を確認
4. ケンシンの最新意向を確認してから作業開始

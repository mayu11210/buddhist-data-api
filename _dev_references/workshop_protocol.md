# workshop 方式 標準仕様書（2026-05-08 初版）

本書は buddhist-data-api 本体（最終データ保管庫）と並列に運用される **workshop 形式の独立 GitHub repo** の標準仕様を定める。本体での motif 抽出は commit `3e261b3`（2026-05-08 候補 B 第 12 ラウンド完走）を**最終地点**として停止し、以後の motif 抽出は workshop（W1 性霊集・W2 教学系）で行う。各 workshop が完走した時点で、本体側のマージセッションで一括移設する。

---

## 1. 概要

### workshop 方式の目的

buddhist-data-api 本体は **「仏教知識の保管庫」**（倉庫設計原則・本体 CLAUDE.md §倉庫設計原則と文体モチーフ索引）であり、最終データを保管する場として位置付けられている。一方、motif 抽出作業は本体上で進めるとセッションごとに本体 CLAUDE.md・motifs.json の同時更新が必要になり、(a) コンテキストが重くなりやすい、(b) 並列セッションで衝突リスクが高い、(c) 本体の最終形が抽出途中の半完成状態で commit され続ける、という問題があった。

そこで **「抽出作業は独立 workshop で並列に進め、完走時に本体へ一括マージする」** 方式に移行する。これは kaimyo-app（アプリ実装側）と本体の関係を motif 抽出作業にも拡張したもので、kaimyo-app と同じ並列パターンを踏襲する。

### 倉庫設計原則との関係

workshop は **抽出専用の作業場** であり、本体倉庫の代替ではない。workshop で作成された motif は最終的にすべて本体 `data/indices/motifs.json` に統合される。倉庫設計原則（キュレーション禁止・アプリ固有構造の排除・タグ軸の網羅性）は workshop でも厳守する。workshop が独自スキーマを発明することは禁止であり、本体 schema 0.2 に完全準拠する。

---

## 2. 構成

並列で運用される workshop は以下の二つ：

| repo | 対象 | ID プレフィックス | 想定セッション数 |
|---|---|---|---|
| **W1：buddhist-shoryoshu-workshop** | 性霊集（残 77 篇） | `sw` | 5〜10 |
| **W2：buddhist-doctrine-workshop** | 教学系 9 著作 | `tw` | 5〜8 |

W2 で扱う教学系 9 著作は次の通り：即身成仏義／吽字義／声字実相義／弁顕密二教論／般若心経秘鍵／秘蔵宝鑰／大日経疏 巻第一／菩提心論／三教指帰。

W1・W2 は完全に独立した GitHub repo として運用され、互いに依存しない。各 workshop は kaimyo-app と並列に運用可能で、最大 3 並列（kaimyo-app + W1 + W2）まで拡張可能。管理負荷を抑えたい場合は段階的に拡張する（最初は W1 のみ → 安定したら W2 追加）。

---

## 3. スキーマ準拠（schema 0.2 凍結期間中の運用ルール）

workshop は本体 motifs.json schema 0.2 に **完全準拠** する。本体 `_dev_references/motifs_index_design.md` を真値とする。schema 0.2 は以下の構造を持つ：

各 motif は次の 5 つの主要フィールドを持つ：`id`・`source`（corpus / idx / 巻番号 / 篇名・成句なら出典_ref + type）・`text_kakikudashi`（必須）・`text_gendaigoyaku`（必須・neutral 訳・補注付き）・`text_gendai_gabun`（オプション・雅文体訳・kaimyo-app 諷誦文中段用）・`tags`（多軸ハッシュタグ配列）。

workshop が独自にフィールドを追加・改名・削除することは禁止する。schema 変更が必要な場合は本章 §11「スキーマ更新プロトコル」に従い、本体側で先に決定してから全 workshop に通達する。

workshop の motifs.json は本体構造を踏襲しつつ、staging 用の軽量版とする。`tag_axes` セクション（standard_9 / special_6 / exception）と `field_rules` セクションは本体を参照すれば十分なため省略してよいが、`stats` セクションは本体と同じ集計項目（total_motifs・kakikudashi_chars_total・gendai_gabun_chars_total・gendaigoyaku_chars_total・motifs_with_gendai_gabun・篇別内訳）を持たせる。

---

## 4. ID 体系（staging プレフィックス）

workshop 内では本体連番（m001〜m287）と衝突しない staging ID を用いる：

| workshop | プレフィックス | 採番例 |
|---|---|---|
| W1 性霊集 | `sw` | sw001・sw002・sw003・… |
| W2 教学系 | `tw` | tw001・tw002・tw003・… |

採番は各 workshop 内で 001 から開始し、ラウンド順に連番を振る。移設マージセッション（本章 §10）では、本体最終 m-id（commit `3e261b3` 時点で `m287`）の次から本体連番に再番号付けする。例えば W1 で 100 件抽出した場合、本体に移設する際には `sw001`〜`sw100` を `m288`〜`m387` に一括変換する。

成句は本体側で `sg01`〜`sg06` の 6 件のみ確定済みのため、workshop では新規成句を追加しない（本体マージ時に成句が発生する場合は本体側で `sg07` 以降を採番する）。

---

## 5. タグ軸の遵守（標準 9 軸 + 特殊 6 軸 + 成句例外）

workshop は本体 `_dev_references/motifs_index_design.md` §2 で定義された **タグ軸体系** を厳守する：

**標準 9 軸**：`category`・`season`・`故人`・`場面`・`硬さ`・`密教`・`典故`・`出典`・`文体`。
**特殊 6 軸**（人生集約句用）：`主題`・`人生像`・`感情調`・`一句性`・`引用形式`・`含意の射程`。
**例外軸**：`成句`（漢文成句のまま保管する稀少例外）。

新規タグ値の追加は許容される（例：`故人:娘` のような故人軸の値追加）が、新規 **タグ軸** の発明は本体マージセッションでの合意が必要。

特に注意すべき運用ルール：

- **主題タグは普遍的概念に限る**（マージセッション 2026-05-07 合意）：`主題:師弟`・`主題:慈愛`・`主題:菩提心` のような普遍仏教概念のみ使用し、本文断片からの固有名詞抽出は禁止。kaimyo-app 側で発生した「主題タグの固有名詞化問題」（280 種以上）の再発を防ぐ。
- **含意の射程は七区分**（2026-05-08 時点）：冥福廻向・総廻向・現当二利廻向・個別廻向・生生世世（誓願型）・再来期待（君臣交誼型）・辞退（謙辞型）。第八区分以降を新規導入する場合は workshop で合意した上で本体マージで確定する。

---

## 6. 文体規定 7 項目（雅文体訳の執筆ガイド・再掲）

`text_gendai_gabun`（雅文体訳）の執筆は本体 `_dev_references/motifs_index_design.md` §3 に定める文体規定 7 項目を厳守する。再掲：

(1) **やまと言葉優先**：旱魃→ひでり・商羊→雨呼ぶ鳥・脣吻→くちびる・密蔵→秘めたる蔵 等、和語に開ける語は和語化する。
(2) **補注非埋込**：読み・典故・字義は雅文体訳に入れず gendaigoyaku（学習者向け補注付き訳）に集約する。
(3) **対句・畳語・呼びかけ保持**：「哀れなるかな悲しきかな」「勉めよ勉めよ」「なにとて早く帰りたまひて」のような朗誦上の構造を保つ。
(4) **雅文体活用形**：たまふ／たまへり／なりき／つひに／たまひて／いとひたまへり／ひきゐて／ひたしまつれり 等、文語の活用形を用いる。
(5) **現代口語回避**：「〜ですね」「〜だよ」のような現代口語的表現を排除する。
(6) **情緒優先**：意味の正確性より朗誦時の情緒が優先される箇所がある（諷誦文・儀礼朗誦の用途を想定）。
(7) **朗誦適性**：声に出して読んだときの息継ぎ・調子を考慮する。長句が続いて朗誦できない場合は分割を許容する。

---

## 7. 必須検証項目

各 workshop での 1 篇分の抽出が完了したとき、commit する前に以下の検証を必ず実施する：

(1) **半角括弧予防的全角徹底**：`fix_parens` 関数を build script の Python 内に実装し、新規挿入分のすべての `(` `)` を `（` `）` に変換した上で motifs.json に書き込む。grep で半角括弧 0 件を確認する（既存の意図的半角箇所がある場合は PRESERVE 文字列で避難してから replace_all を実施する）。
(2) **stats と recompute の差分ゼロ**：build script 末尾で stats の 5 項目（total_motifs・kakikudashi・gendai_gabun・gendaigoyaku・motifs_with_gendai_gabun）と Python `len(s.replace("\n",""))` 集計の差分を表示し、全項目 0 を確認する。差分があれば recompute 値を真値として stored を補正する（マージセッション原則踏襲）。
(3) **篇別内訳エントリは dict 形式**：`is_dict` 検証を build script に組み込み、文字列形式（説明文がそのまま値）になっていないか確認する。本体で発生した idx=45 形式不正修復（マージセッション 2026-05-07）の再発を防ぐ。
(4) **NUL バイト 0 件**：書込後に `len(raw) - len(raw.rstrip(b'\x00'))` で末尾 NULL バイトを検出し、0 でなければ `git show HEAD:<path> > <path>` で復旧する。

---

## 8. 引き継ぎメモ運用（ASCII 名）

引き継ぎメモは **ASCII 名で作成** する。日本語名は git の認識問題（git status に出ない例が本体で発生・第 11 ラウンド commit `f4a86ed` の副次発見）を避けるため使わない。命名規約：

```
handoff_YYYY-MM-DD_<round>_<idx>_<status>.md
```

例：`handoff_2026-05-15_w1_round01_idx10_complete.md`（W1 第 1 ラウンド・idx=10 完走）。本体の引き継ぎメモは `handoff_2026-05-08_round12_idx105_complete.md` の形式で蓄積されているため、これに揃える。

引き継ぎメモには次の 4 セクションを含める：(a) 本セッションの位置づけ、(b) 本セッションの主な成果（motifs.json 拡張テーブル + 抽出単位テーブル + 設計上の新規ポイント）、(c) 残作業（次セッション以降の選択肢）、(d) 副次発見・要注意事項。

---

## 9. commit_push.bat 運用（path 設定方法・bash 経由 git 禁止）

各 workshop は本テンプレ（`workshop_commit_push_template.bat`）を起点とし、`cd /d` の path を当該 workshop の Windows 側パスに書き換えて運用する。例：

- W1：`cd /d "C:\Users\user\buddhist-shoryoshu-workshop"`
- W2：`cd /d "C:\Users\user\buddhist-doctrine-workshop"`

ASCII のみで .bat を書く原則は厳守（cmd.exe Shift-JIS 解釈で日本語が壊れる）。日本語のコミットメッセージは `commit_message.txt`（UTF-8）に書き、`git commit -F commit_message.txt` で読ませる。

**bash 経由 git は禁止** する（本体で 2026-05-03 G2-A 着手時に phantom deletion 事故が発生した経緯を踏襲）。Cowork サンドボックスからの git 実行は **読み取り系のみ**（log・status・diff・show）に留め、commit / push / reset / stash / checkout 等の書き込み系は必ず Windows 側で .bat ダブルクリックで実行する。

---

## 10. 移設マージセッション手順（本体側で実施・各 workshop 完走時 1 回・1 セッション目安）

各 workshop が完走した時点で、本体側でマージセッションを 1 回実施する。手順：

(1) workshop 側の motifs.json から motif 配列を読込み、staging ID（sw / tw）を本体最終 m-id の次から連番で再番号付けする（例：W1 完走時 `sw001`〜`sw100` → `m288`〜`m387`）。
(2) 本体 `data/indices/motifs.json` の motifs 配列末尾に追記し、stats 全項目を recompute して整合化する。`篇別内訳` を本体形式（dict）で追加する。
(3) 本体 CLAUDE.md のタイトル・進捗ヘッダ・並行候補テーブル・「次の作業」セクション・最終更新行を更新する。
(4) workshop 側で `主題:*` タグの固有名詞化等の問題が発生していた場合、本体マージ時に整理する（本体マージで初めて本体に統合されるため、整理のチャンス）。
(5) 移設後、workshop 側 repo を凍結する（読み取り専用化または archive 化）。再開する場合は新 workshop を立ち上げる。
(6) 本体側で move 後の commit を push し、kaimyo-app 等の利用側アプリが新 motif を即座に参照できる状態にする。

---

## 11. スキーマ更新プロトコル

schema 変更が必要になった場合（例：新フィールド追加・新タグ軸新設）、以下の順序で実施する：

(1) **本体で先に決定**：本体 `_dev_references/motifs_index_design.md` で schema 0.3 を提案・合意する。
(2) **全 workshop に通達**：本体 CLAUDE.md および本書 §3 を更新し、全 workshop の CLAUDE.md（テンプレ §2）にも反映する。
(3) **workshop は同時追従**：各 workshop は次のラウンド開始時から新 schema に切り替える。既存 workshop データは本体マージ時に schema 変換する（変換スクリプトは本体側で用意）。

schema 凍結期間中は workshop が独自に新フィールド・新軸を発明することを禁止する。発明したい場合は workshop 側で proposal を引き継ぎメモに書き、本体マージセッションで合意してから schema 0.3 化する。

---

## 12. kaimyo-app との連携

各 workshop が本体にマージされた直後から、kaimyo-app は新 motif を即座に参照可能になる。具体的な連携経路：

(a) kaimyo-app は本体 `data/indices/motifs.json` を参照する（直接 fetch または横断索引 API 経由）。
(b) 本体 schema 0.2 で導入された `text_gendai_gabun`（雅文体訳）は kaimyo-app の「硬さ」UI（硬→kakikudashi / 中（標準）→gendai_gabun / 柔→将来追加）と直結している。
(c) kaimyo-app 側のテーマ駆動辞書設計（commit `625451f`・2026-05-07）は本体 `主題:*` タグ群と連動する。workshop で新規導入する `主題:*` タグは kaimyo-app の辞書整備時に直接利用される。

workshop の motif 抽出は最終的に kaimyo-app の表現拡張に直結するため、kaimyo-app 側の引き継ぎメモも適宜参照しつつ進める。並列セッションで運用する場合は本体マージセッションで衝突を解消する（本体マージ時に kaimyo-app 側更新は触らない原則を踏襲）。

---

## 関連ファイル

- 本書：`_dev_references/workshop_protocol.md`（本体・標準仕様書）
- workshop CLAUDE.md テンプレ：`_dev_references/workshop_CLAUDE_template.md`
- workshop commit_push.bat テンプレ：`_dev_references/workshop_commit_push_template.bat`
- 本体 schema 仕様：`_dev_references/motifs_index_design.md`（schema 0.2 真値）
- 本体 motifs.json：`data/indices/motifs.json`（最終データ保管庫・以後 motif は本体に追加しない）
- 本体 CLAUDE.md：リポジトリ直下（倉庫設計原則・並行候補テーブル・最終更新行）

---

最終更新：2026-05-08（Phase 1 着手・workshop 方式標準仕様書 初版）

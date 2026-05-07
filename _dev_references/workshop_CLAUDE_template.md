# workshop CLAUDE.md テンプレ（最小ルール・2026-05-08 初版）

本テンプレは workshop 形式 repo（W1：buddhist-shoryoshu-workshop / W2：buddhist-doctrine-workshop）の `CLAUDE.md` 初期内容として使用する。各 workshop はこのテンプレをコピーして該当箇所（`<W名>`・対象著作・ID プレフィックス等）を書き換える。

---

# <W名> CLAUDE.md（motif 抽出専用 workshop）

このリポジトリは **buddhist-data-api 本体（最終データ保管庫）と並列運用される motif 抽出専用 workshop** です。本体の commit `3e261b3`（2026-05-08 候補 B 第 12 ラウンド完走）を起点に、本体での motif 抽出を停止し、本 workshop で並列に抽出を進めます。完走時に本体側でマージセッションを実施し、本 workshop の motif を本体 `data/indices/motifs.json` に統合します。

## 1. workshop の目的

- **motif 抽出専用**：本 workshop は motif 抽出作業に特化した作業場です。最終形は本体に移設するため、本 workshop の motifs.json は staging（仮置き）として扱います。
- **対象**：<対象著作・例：性霊集 残 77 篇 / 教学系 9 著作>
- **完走条件**：<対象範囲の全 motif 抽出が完了した時点 / 想定セッション数：5〜10>

## 2. スキーマ準拠

本 workshop の motifs.json は本体 schema 0.2 に **完全準拠** します。本体 `_dev_references/motifs_index_design.md` を真値とし、独自にフィールドを追加・改名・削除しません。

詳細仕様は本体 `_dev_references/workshop_protocol.md` §3 参照。標準 9 軸 + 特殊 6 軸 + 成句例外のタグ軸体系（同 §5）と、文体規定 7 項目（同 §6）も厳守します。

主題タグは普遍的概念に限る（マージセッション 2026-05-07 合意）。本文断片からの固有名詞抽出は禁止します。

## 3. ID プレフィックス

本 workshop 内では staging ID として **`<sw / tw>` プレフィックス** を用います。採番は 001 から開始し、ラウンド順に連番を振ります（例：sw001・sw002・…）。本体マージセッションで本体最終 m-id（commit `3e261b3` 時点で `m287`）の次から本体連番に再番号付けします。

## 4. 完走時のマージ依頼手順

本 workshop の対象範囲が完走した時点で：

1. 引き継ぎメモを ASCII 名（`handoff_YYYY-MM-DD_<W>_completion_summary.md`）で作成。
2. ケンシンに「workshop 完走しました。本体側でマージセッションをお願いします」と告知。
3. ケンシンが本体 repo の Cowork セッションを起動し、マージセッション 1 回で移設。本体 CLAUDE.md・motifs.json が更新され、本 workshop 側 repo は凍結。

詳細は本体 `_dev_references/workshop_protocol.md` §10 参照。

## 5. 必須検証項目

各 1 篇分の抽出完了 commit 前に：

- 半角括弧予防的全角徹底（`fix_parens` 関数を Python 内に実装）
- stats と recompute 差分ゼロ
- 篇別内訳エントリは dict 形式
- NUL バイト 0 件

詳細は本体 `_dev_references/workshop_protocol.md` §7 参照。

## 6. git 運用

- **bash 経由 git 禁止**：commit / push / reset / stash 等の書き込み系は必ず Windows 側で `.bat` ダブルクリックで実行。
- **commit_push.bat 経由のみ**：本 workshop 直下の `commit_push.bat`（本体テンプレを path 書換えしたもの）を使用。
- **引き継ぎメモは ASCII 名**：日本語名は git 認識問題リスクのため避ける。

詳細は本体 `_dev_references/workshop_protocol.md` §8・§9 参照。

## 7. 参照（本体側）

- `C:\Users\user\buddhist-data-api\_dev_references\workshop_protocol.md`（標準仕様書・真値）
- `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`（schema 0.2 仕様書）
- `C:\Users\user\buddhist-data-api\data\indices\motifs.json`（本体最終形・以後 motif は本体に追加しない・読込のみ）
- `C:\Users\user\buddhist-data-api\data\kukai\<対象著作>.json`（書き下し原典・参照用）

---

最終更新：2026-05-08（workshop CLAUDE.md テンプレ 初版）

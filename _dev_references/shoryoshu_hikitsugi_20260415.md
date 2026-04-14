# 引き継ぎメモ 2026-04-15

## 完了したこと

### 書き下しテキストの全巻追記完了
`_dev_references/shoryoshu_kakikudashi_raw.txt` に、
Kindle版「全文書き下し 遍照発揮性霊集」（PowerToysテキスト抽出）を
巻第一〜巻第十まで全巻追記し終えた。

- 総行数：4676行
- 最終コミット：`2d88d8f`「書き下し生テキスト：巻第十（九相詩・十二因縁詩序・奥書）追記――全十巻完了」

---

## 次にやること

### ステップ1：fix_columns.py を実行する

```bash
cd /sessions/.../mnt/buddhist-data-api/_dev_references
python fix_columns.py
```

- 入力：`shoryoshu_kakikudashi_raw.txt`（4676行、ルビ含む）
- 出力：`shoryoshu_kakikudashi.txt`（列逆順修正・ルビ除去済み）
- 注意：このスクリプトは `===` 区切り行をページ区切りとして使う。
  今回の raw ファイルは `=== 巻第X ===` という形式でセクション区切りのみ設けており、
  ページ単位の `===` 区切りは挿入していない。
  → 列逆順修正の効果はほぼ無いが、**ルビ除去**は有効に機能する。
  → 実際には「ルビ除去フィルター」として使う形になる。

### ステップ2：出力テキストを確認する

`shoryoshu_kakikudashi.txt` を目視で確認し、
ルビ行が適切に除去されているか、本文が壊れていないかチェックする。

### ステップ3：shoryoshu_raw.txt のOCR校正に使う

`shoryoshu_raw.txt`（OCR抽出原文）の誤字・脱字を、
`shoryoshu_kakikudashi.txt`（書き下し照合元）と突き合わせて校正する。

---

## ファイル構成（関連ファイル）

| ファイル | 役割 |
|---|---|
| `shoryoshu_kakikudashi_raw.txt` | Kindle書き下し生テキスト（ルビ含む） |
| `fix_columns.py` | 列逆順修正・ルビ除去スクリプト |
| `shoryoshu_kakikudashi.txt` | fix_columns.py 出力（まだ生成していない） |
| `shoryoshu_raw.txt` | 底本OCR抽出テキスト（校正対象） |
| `shoryoshu_corrections.txt` | 校正メモ |

---

## fix_columns.py の仕様メモ

- `===` で始まる行をページ区切りとみなす
- 空行をブロック（列）区切りとみなし、ブロックを逆順にする
- ひらがな・カタカナのみ・10文字以下の行をルビとして除去
- オプション：`--keep-ruby`（ルビを残す）、`--dry-run`（プレビュー）、`--debug`

---

## raw ファイルの注意点

- PowerToysで抽出した順序（左→右列）のまま保存している
- 縦書き正読み順（右→左）への修正は fix_columns.py が担当
- ただし今回は `===` ページ区切りを巻単位でしか入れていないため、
  列逆順修正の精度は限定的。ルビ除去メインで使う。
- 一部に同じページを2回貼ったとみられる重複箇所がある可能性あり（目視要確認）

---

最終更新：2026-04-15（全十巻完了・次セッションへの引き継ぎ）

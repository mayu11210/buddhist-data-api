# 性霊集作業 引き継ぎメモ
更新: 2026-04-14

---

## 現在の作業フェーズ

**フェーズ1（取り込みフェーズ）継続中。**

今セッションは「性霊集OCR校正の補助データ整備」が中心だった。
宮坂版書き下し（shoryoshu_miyasaka.json）と定本OCR（teihon_vol8_ocr.txt）をつき合わせて、
shoryoshu_raw.txt の原文テキストを校正する体制を整えた。

---

## 今セッションで完了したこと

### 1. p.31 遊山慕仙詩并序 の校正照合
- 定本PDF（08第八巻.pdf）の p.31 を画像で直接読み取り
- 宮坂版書き下し（shoryoshu_miyasaka.json p.158-159）と照合
- `_dev_references/shoryoshu_corrections.txt` に以下を追記・確定:

| OCR誤読 | 正読 | 照合根拠 |
|---------|------|----------|
| 遊山慕仙**抒**序（題名） | 遊山慕仙**詩并**序 | PDF画像目視 |
| 背何**山**郭氏 | 昔何**生**郭氏 | PDF画像目視 |
| 五十三**言** | 五十三**字** | PDF画像・宮坂版 |
| 余披**波**之次 | 余披**閲**之次 | PDF画像目視 |
| 空談**牛彌**未説 | 空談**乃**（…）未説 | PDF画像目視 |
| 大仙之**留居** | 大仙之**窟房** | PDF画像目視 |
| **高祖**風易起 | **高山**風易起 | 宮坂版「高山は風起り易く」 |
| 深**水才子**難量 | 深**海水**難量 | 宮坂版「深海は水量り難し」 |
| 吟悲惜常 | 吟詠再三・惜義理之未盡 | PDF画像目視 |

- p.32-33（五言詩密集部分）はOCR不能のため、照合は宮坂版書き下しで代替

### 2. 書き下しデータ収集の仕組みを整備
Kindle「全文書き下し遍照発揮性霊集」からPowerToysで抽出したテキストを収集する体制を構築:

- **`_dev_references/shoryoshu_kakikudashi_raw.txt`**
  ケンシンがKindleから貼り付けていく収集ファイル。
  現在は扉テキスト（遍照発揮性霊集 / 真済撰）のみ入っている。

- **`_dev_references/fix_columns.py`**
  PowerToys縦書き抽出の列逆順問題を修正するスクリプト。
  使い方: `python fix_columns.py` → `shoryoshu_kakikudashi.txt` に出力
  オプション: `--dry-run`（画面確認のみ）、`--debug`（列数表示）

### 3. git コミット状況
- ローカルmainは origin/main より **3コミット先行**（push.bat 未実行）
- コミットハッシュ: 7332e15（最新）、33f3e12、6afb6c6

---

## 次のセッションで取り組む作業

### 優先度 高：書き下しデータの収集と照合

1. **ケンシンが shoryoshu_kakikudashi_raw.txt にKindle書き下しを貼り付けていく**
   - PowerToysで1ページ（または1詩）ずつ抽出 → 貼り付け → ページ区切り `=== ===` を挿入
   - ある程度たまったら `python fix_columns.py` で列順修正 → shoryoshu_kakikudashi.txt に出力

2. **shoryoshu_kakikudashi.txt を使って shoryoshu_raw.txt のOCRを校正**
   - shoryoshu_raw.txt の各ページのOCRテキストと書き下しを照合
   - 誤読箇所を shoryoshu_corrections.txt に記録

3. **shoryoshu_miyasaka.json の続き（p.202〜）**
   - 次の作業: `大和の州益田の池の碑銘 并びに序`（宮坂版 p.202〜）
   - 底本PDF: `性霊集　第一巻、第二巻.pdf`（性霊集フォルダ内）
   - 注意: chu フィールドを各篇に追加する（2026-04-13以降の方針）

### 優先度 中：OCR照合の継続

- p.32-33（五言詩密集部分）: 宮坂版書き下しを使って照合（OCR自体は読めない）
- shoryoshu_corrections.txt への記録を継続

---

## ファイル・データの場所まとめ

| ファイル | 場所 | 用途 |
|---------|------|------|
| 定本OCR | `_dev_references/teihon_vol8_ocr.txt` | 性霊集本文OCR（471ページ分） |
| 性霊集抜粋OCR | `_dev_references/shoryoshu_raw.txt` | pp.30-269（240ページ）の抜粋 |
| OCR校正レポート | `_dev_references/shoryoshu_corrections.txt` | p.31-34の校正照合結果 |
| 書き下し収集（raw） | `_dev_references/shoryoshu_kakikudashi_raw.txt` | Kindle抽出テキスト貼り付け先 |
| 列修正スクリプト | `_dev_references/fix_columns.py` | 列逆順修正 |
| 書き下し修正済み | `_dev_references/shoryoshu_kakikudashi.txt` | fix_columns.py の出力（未生成） |
| 宮坂版書き下しJSON | `data/kukai/shoryoshu_miyasaka.json` | 取り込み済み pp.158-201 |
| 定本PDF | `~/OneDrive/デスクトップ/DATE/真言/性霊集/` | 底本（絶対基準） |

---

## 重要な照合ルール（再確認）

1. **底本PDF > 定本OCR > 宮坂版書き下し > Coworkの知識** の優先順位
2. 宮坂版は「書き下し」（読み方の参考）であり、漢字表記の根拠にはならない
3. shoryoshu.json は修正対象であり照合元ではない
4. chu フィールドは各篇の注釈ページの内容を格納する（2026-04-13追加方針）

---

## push.bat 実行依頼

セッション終了のため push が必要です。
ローカルに 3コミット溜まっています（origin/main より先行）。
**push.bat を実行してください。**

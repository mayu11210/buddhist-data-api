# 性霊集 引き継ぎメモ
作成日：2026-04-11（最終更新）

---

## ✅ 今セッションで完了した作業

### 中巻 完了
- p486-494 取り込み完了（高野山万灯会願文訓読完結・勧進奉造仏塔知識書漢文・訓読・語注）
- コミット: e56f621

### 下巻 第一バッチ完了（p8-22）
- p8-14: 宮中真言院正月御修法奉状（漢文・訓読・語注）
- p15-18: 祈誓弘仁天皇御匡尼表（漢文・訓読・語注）
- p19-21: 贈玄賓法師勅書（漢文・訓読・語注）
- p22: 大僧都空海婴疾上表辞職奉状 漢文のみ
- コミット: 3de4119

---

## 次回の作業

### 開始位置
**性霊集 下巻 p23から**
内容：大僧都空海婴疾上表辞職奉状 の **訓読・語注**から

### PDFの場所
`C:\Users\user\OneDrive\デスクトップ\DATE\真言\性霊集\性霊集 下巻.pdf`
（マウント後は `/sessions/.../mnt/性霊集/性霊集　下巻.pdf`）

### 目次（下巻 巻第九）の残り
| ページ | 内容 |
|--------|------|
| p22-28 | 大僧都空海婴疾上表辞職奉状（漢文完了・訓読語注が残り） |
| p28 | 勅答 一首 |
| p34 | 奉造東寺塔材木史運勅進表 一首 |
| p42 | 永忠僧都少僧都表 一首 |
| p47 | 永忠僧都被訴乙大定処表 一首 |
| p52 | 於紀忠国伊都郡高野峯被訴乙大定処表 一首 |
| p61 | 高野四至塔 白文 |
| p68 | 勧明鐘知識文 |
| p72 | 紀伊国伊郁都高野寺鐘知識文 一首 |

---

## JSONファイルの現状

- ファイル：`data/kukai/shoryoshu.json`
- 文字数：**100,457文字**
- 構造：`{"section": "性霊集", "source": "...", "text": "...（全文）..."}`
- textフィールドに全内容が連続テキストとして格納されている

---

## 作業ルール（必ず守ること）

1. **PDFが絶対の基準**。Coworkの知識で勝手に補完・書き換えしない
2. **OCRは使わない**。Coworkが視覚的にPDFを直接読む
3. `pdf2image`（DPI=200）+ `PIL.Image`でズームして確認する
4. 不確かな字は必ずズーム確認。判断できない場合はユーザーに報告
5. 既存JSONの構造を変えない。textフィールドに追記するだけ
6. コミットメッセージは日本語・簡潔に
7. **push.batはユーザーが手動実行**（Coworkはpushしない）
8. エラーが出たら勝手にリトライせず、必ず報告する
9. 一度に大量処理せず、15ページ程度のバッチで進める

---

## 典型的な作業手順

```python
# PDFページを画像化
from pdf2image import convert_from_path
pages = convert_from_path(pdf_path, dpi=200, first_page=X, last_page=Y)

# 不確かな字をズーム確認
from PIL import Image
img = Image.open('page.jpg')
crop = img.crop((x0, y0, x1, y1))
crop.resize((w*2, h*2), Image.LANCZOS).save('zoom.jpg')
```

JSONへの追記：
```python
import json
with open('data/kukai/shoryoshu.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
data['text'] += new_content
with open('data/kukai/shoryoshu.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

---

## コミット履歴（今セッション）

| ハッシュ | 内容 |
|---------|------|
| e56f621 | 性霊集中巻p486-494追記・中巻完了 |
| 3de4119 | 性霊集下巻p8-22追記（巻第九開始） |

---

最終更新：2026-04-11

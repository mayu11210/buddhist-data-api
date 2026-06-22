# 引き継ぎメモ — 大日経疏 巻第十二 genten 後送 完了（2026-06-22）

巻第十二の最後の残課題だった漢文原典 genten を後送した。これで巻第十二は全工程（Phase1-3＋連動軸 retrofit＋gabun＋genten）を完走。

## やったこと
- **対象**：`data/kukai/dainichikyo-sho-vol12.json` の genten/genten_source。
- **取得元**：CBETA 線上閱讀 `T1796_012`（大正蔵 No.1796 vol.39・善無畏口述/一行筆受）を Claude in Chrome で取得（`#body` 抽出）。
- **清掃**（vol10/vol11 同体裁）：
  - 夾註（inline-note）66 件を半角括弧から `〔 〕` に変換。
  - 校勘アンカー 75 件（`[n]`系）を除去。`◎` なし。
  - gaiji 4 字（𭊭 U+2D2AD×3・嬭 U+5B2D・𤦲 U+249B2）を Unicode で保持。
  - **悉曇 IAST 4組（va・haṃ・ma・raṃ）は半角括弧のまま温存**（vol8〜9 と同じく siddham 音写は ( ) で保全）。
  - 五大の色図（□金剛地黃　○水地白…）の全角空白も温存。
  - 冒頭に `大毘盧遮那成佛經疏卷第十二　原典（…CBETA 線上閱讀 T1796_012）` ヘッダ付与。
- **本文**：全 15,401 字（cp）・夾註〔〕66組・半角括弧4組（IAST のみ）・NUL 0。
- **取込の信頼性**：900cp×18 チャンクに分割し、各チャンクの SHA-256 と全文 SHA-256（`f38217d8…b129`）をブラウザ側と Python 側で照合してバイト一致を確認。
- `genten_source` を vol10/vol11 同形式に更新。

## manifest 更新
- data_status.genten=true・genten_unavailable_reason 削除。
- char_counts.genten=15345（改行除外）・summary.genten_present 20→21・notes に後送完了を追記。

## 検証（すべて pass）
- スキル validate：JSON 再パース OK／NUL 0／63段全訳／半角括弧 0。
- 倉庫 validate：全 47 件メカニカル整合 OK。
- ホスト側 Grep で corpus・manifest・CLAUDE.md の反映確認。

## 残課題
- **kaimyo-app 同期**（別リポジトリ・未接続）：倉庫 motifs.json（3512件）を kaimyo-app 側へコピー・SHA-256 一致確認。冠は source.著作名 フォールバックで「大日経疏 巻第十二に曰く、」＝コード変更なし見込み。

## 次の作業
`commit_push.bat` をダブルクリックして commit/push（commit_message.txt は本件＝genten 後送 に更新済み）。push 後は `git log --oneline` 先頭が本件、`git log origin/main..HEAD` が空になることを確認。

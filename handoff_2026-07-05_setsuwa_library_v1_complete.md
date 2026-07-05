# handoff: 経典説話ライブラリ v1 新設 完了

**状態**：push 待ち（commit_push.bat ケンシン実行待ち）
**着手時 HEAD**：762e2e6（sg06 anchor 設計・push 済確認済）
**種別**：新規索引ファイル追加（既存 motif・corpus・7カテゴリ索引は一切変更なし）

## 経緯

kaimyo-aoo の法話生成（核テーマ選択→法話）に、テーマに合う経典説話を織り込みたい
というケンシンの要望から。生成 AI に毎回説話を出させると出典捏造リスクがあるため、
検証済みの説話データ集を倉庫に持ち、テーマ→tags 照合で注入する方式を採用。

## 成果物

1. **data/indices/setsuwa.json**（新規・約 46KB）
   - 40話＝canon 内訳：early 20（阿含・パーリ）／mahayana 10（法華・涅槃等）／
     tale 10（賢愚経・ジャータカ・譬喩経・雑宝蔵経等）
   - フィールド：id（s001〜s040）／title／source／canon／tags／synopsis（150〜250字・
     中立文体）／point／connective_example（「経典に〜がございます」型の織り込み例文）
   - 口調（でございます調等）は kaimyo-aoo 生成側で調整する前提
2. **_dev_references/setsuwa_catalog_v1.md**（新規・人間確認用の出典カタログ）
   - テーマ軸索引（16軸）・kaimyo-aoo 現行3テーマ（誠実な眼差し／感謝と自立／
     信念の羅針盤）との対応表つき
3. CLAUDE.md ★entry（2026-07-05）／commit_message.txt 更新

## 選定・執筆方針（ケンシン確認済）

- 経典説話のみ（大師伝承は含めない・2026-07-05 裁定）
- 初期経典を厚めに（31〜40 は初期経典からの増補ラウンド）
- 戒名法話文脈を意識した選定：良医病子（遺した言葉）・自灯明（見送り後の自立）・
  純陀（参列者の供養）・徳の香り（遺徳）・第二の矢（遺族の悲しみ）・
  世界は美しい（写真愛好家テーマ）等
- あらすじは現代語の再話＝genten なし。corpus 系（validate_corpus.py）の対象外。
  大智度論 corpus の説話段落（k218-222・genten つき）とは別系統の資産

## 検証

- JSON 再パース OK／count 40／全フィールド非空／NUL 0／半角括弧 0（全角のみ）
- bash 側で書き、ホスト側 Grep で反映確認（s040・末尾コンテンツ・CLAUDE.md 署名一意）
- CLAUDE.md はバックアップ outputs/CLAUDE.md.bak_pre_setsuwa_v1 を取得のうえ
  bash 側 python で挿入（行1が27.5万字でホスト Edit 不可のため）・前後長・末尾一致 assert 済

## 次にやること

1. ケンシンに commit_push.bat 実行を依頼（→ 完了後 git log --oneline で push 確認）
2. kaimyo-aoo（kaimyo-app）への setsuwa.json 同期。motifs.json の
   push3_sync_kaimyo.bat と同型の手順が使える（SRC/DST を setsuwa.json に読み替え）。
   アプリ側の読み込み実装（テーマ→tags 照合→プロンプト注入）は別セッション
3. タグ軸を motifs.json の軸体系と正式にすり合わせ（現状は自然語タグ）
4. 拡充候補：忍耐・慈悲系の異伝、性霊集願文（候補B資産）との接続、
   大智度論 k218-222（genten つき説話）への相互参照付与

## 落とし穴メモ

- **sg06 handoff 注意2 の stale staged rename が未解消のまま残存**
  （引き継ぎメモ_2026-05-06_…idx48… → 「引き継ぎメモ_202」の phantom rename）。
  commit_push.bat の SAFETY CHECK が「deleted:」で停止する場合は、ホスト側で
  `git restore --staged "引き継ぎメモ_202" "引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md"`
  を実行してから再度 commit_push.bat を実行のこと
- bash 側 git status の source.doc 2 件（vol19/vol20_build）の M 表示は既知の phantom
  （sg04/sg05/sg06 時と同一事象・今回作業と無関係）
- 全角括弧厳守・既存ファイルには触れない（本セッションの変更＝新規2＋CLAUDE.md＋
  commit_message.txt のみ）

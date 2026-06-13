# 引き継ぎメモ 2026-06-13 理趣経開題 motif 抽出 第1ラウンド完走（m2384-m2399・total 2428）

**日付**：2026-06-13
**種別**：motif 抽出ラウンド（本体直接書込・rishukyo-kaidai 初回＝1ラウンドで完走）
**起点 HEAD**：`11c97af`（kaimyo-app 同期完了の記録・着手前に巻き戻り検知全 pass で確認）
**ステータス**：作業完了・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json（m2384-m2399 16件追加・stats 更新・schema_history 追記）・CLAUDE.md（タイトル行・現在の進捗）・commit_message.txt・本メモ
**commit_message.txt 更新確認**：済（冒頭行＝本ラウンドの内容と整合）

---

## Phase A 合意事項（ケンシン裁定 2026-06-13・以後の理趣経開題系作業で遵守）

1. 本体直接書込（並行セッションなし）・ID 連番
2. 引用形式：空海確実著作 → 十住心論方式。本ラウンドは全16件 引用形式:大師曰く（category:大師御言葉は付与せず）
3. 束ね：廻向偈 k012-k015 を \n 結合で 1 motif（m2398）。表題・尾題・署名・日付・宛先（k001/k003/k004/k005/k008/k010/k016/k017/k019/k020/k021）は motif 化せず
4. gabun 未設定（hizoki/jujushinron/yugikyo 同運用・将来 retrofit 可）
5. 連動軸は抽出時付与せず（完走後 retrofit）
6. **k011 分割の明示的例外**：真実経文句 三段科文（7,074字・既存最大 motif 2,582字の約3倍）を科文章境界 9 マーカーで 10 分割（m2388-m2397）。「段落は分割しない」原則の明示的例外としてケンシン裁定。分割片の再結合＝原文一致（空白差なし）を build script で assert 済。篇別内訳の当該エントリに特記あり

## 成果（16件・m2384-m2399）

| id | 段落 | 内容 | 字数 |
|---|---|---|---|
| m2384 | k002 | 弟子帰命・講読文（先妣追悼＋題目釈） | 1,394 |
| m2385 | k006 | 生死之河・大意 ★核心 | 624 |
| m2386 | k007 | 生死之河・題目釈（大三法羯・四種曼荼羅） | 1,414 |
| m2387 | k009 | 将釈此経・三門釈 ★核心 | 526 |
| m2388 | k011 1/10 | 三段総説・縁起分（通序七事・五智歎徳） | 853 |
| m2389 | k011 2/10 | 正説分総説・十七章列挙 | 279 |
| m2390 | k011 3/10 | 第一 金剛薩埵章（十七句五分・三密観） | 1,273 |
| m2391 | k011 4/10 | 第二 毘盧遮那章（四智四波羅蜜配釈） | 429 |
| m2392 | k011 5/10 | 第三〜六章（降三世・観自在・虚空蔵・金剛拳） | 1,157 |
| m2393 | k011 6/10 | 第七〜十章（文殊・纔発意・虚空庫・摧魔） | 891 |
| m2394 | k011 7/10 | 第十一〜十二章＋同異問答 | 502 |
| m2395 | k011 8/10 | 第十三〜十五章（七母女天・三兄弟・四姉妹） | 187 |
| m2396 | k011 9/10 | 第十六〜十七章（四波羅蜜大曼荼羅・五秘密） | 1,094 |
| m2397 | k011 10/10 | 流通分 | 400 |
| m2398 | k012-k015 | 廻向偈（束ね） ★核心 | 43 |
| m2399 | k018 | 実相般若経答釈・四問答釈 | 1,734 |

- 新タグ値 5：出典:理趣経開題／出典:真実経文句／出典:実相般若経答釈・category:科文・密教:十六大菩薩（いずれも既存軸内の値追加・schema 0.2 不変）
- 一句性:核心 3：m2385（生死の河／涅槃の山）・m2387（阿字廓然不生不滅）・m2398（無尽灯廻向偈）

## stats 差分

- total_motifs 2412→2428・famous_phrases 29 不変（sg01-sg29）
- kakikudashi_chars_total 239,034→251,834（+12,800）／gendaigoyaku_chars_total 706,808→726,701（+19,893）
- from_corpus_rishukyo-kaidai=16 新設・篇別内訳「rishukyo-kaidai_開題三種・真実経文句・実相般若経答釈」追加
- schema_history +1（origin: rishukyo-kaidai_round1）・motifs_without_gendai_gabun_intentional に rishukyo-kaidai_m2384-m2399 追記

## 検証（全 pass）

- 着手時巻き戻り検知：HEAD 11c97af・total=2412・sg01-sg29・m506 引用形式:典籍曰く・m2375/m2378/m2381 一句性:核心・m2381 連動:sg28＋sg03・m2375 連動:sg29＋sg19
- 適用後 10 項目：NUL 0／再パース OK／total=配列=2428／m1〜m2399 連番（missing=[]・dup なし）／必須フィールド完全／新規半角括弧 0／recompute drift 0（kaki・gen・gabun・from_corpus）／schema 0.2 維持・history +1／verbatim 照合（k011 分割再結合＝原文一致・束ね・単独とも）／ホスト側 Grep 反映確認（total 2428・m2399・rishukyo-kaidai_round1）
- バックアップ：outputs/motifs_backup_pre_rishukyo_r1.json（リポ outputs・untracked）
- build script：（Cowork セッション側 outputs に保管・build_rishukyo_r1.py・dry-run → --apply 方式）

## 副次発見・要注意事項

- **マウント同期不具合継続**：bash 側 CLAUDE.md が末尾欠損（sha256 が HEAD と不一致・末尾が retrofit 節途中で切れる）を本セッションでも確認。CLAUDE.md・commit_message.txt・本メモはホスト側ツール（Edit/Write）で編集した。motifs.json は bash 側で書き、ホスト側 Grep で反映確認（正常）
- bash 側 git status の幻影差分（M CLAUDE.md・M motifs_index_design.md）継続。commit_push.bat の index リセットで解消される類
- CLAUDE.md はタイトル行（1 行目）が巨大化しておりホスト Read（行単位）でも 1 行目だけでサイズ上限超過。今回はホスト Edit（部分文字列アンカー）で更新した。将来タイトル行の短縮（過去 ★ エントリの本文への移設）を検討する価値あり

## 残作業（次セッション・補注 GG 処理順）

1. **連動軸 retrofit**：理趣経開題 16 motif の連動スキャン（候補例：m2387 阿字廓然 ↔ 阿字本不生系 sg・m2390/m2399 金剛薩埵・三密系・m2385 生死涅槃対比）。Phase A〜D 様式
2. **gabun 要否裁定**：意図的未設定の継続可否（hizoki/jujushinron/yugikyo は継続中）
3. **kaimyo-app 同期**：motifs.json 2428 版の単純コピー＋SHA-256 一致確認。新 80 字以下 motif（m2398 廻向偈 43 字）が橋プール入りする可能性 → 冠生成（理趣経開題系の CORPUS_DISPLAY_NAME 要否）をアプリ側で確認
4. その後の次期 corpus 候補：金剛頂経開題（47 段落）・大日経開題（97 段落）・菩提心論講要（146 段落・典籍曰く）・大日経本体（896 段落・長期）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2428・最終 m-id=m2399・sg01-sg29・m506 引用形式:典籍曰く・m2375/m2378/m2381 一句性:核心・m2381 連動:sg28・m2385/m2387/m2398 一句性:核心（本ラウンド分・巻き戻り検知）
3. スクリプトの適用前 assert に m506 典籍曰く＋核心チェック（m2375/m2378/m2381 系と m2385/m2387/m2398 系）を継承
4. マウント同期不具合継続前提：文書はホスト側ツールで編集・motifs.json の正準形式は indent=1・末尾改行なし

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- 理趣経開題 motif 抽出 第1ラウンド完走 commit 済（commit <ハッシュ>）：
  m2384-m2399 16件・total 2412→2428・新タグ値5・核心3・k011 科文10分割（明示的例外）
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-13_rishukyo_kaidai_motif_round1_complete.md
## 確認
git log --oneline -3 で HEAD・motifs.json total_motifs=2428・最終 m-id=m2399・sg01-sg29・
m506 引用形式:典籍曰く・m2385/m2387/m2398 一句性:核心（巻き戻り検知）
## 次の作業
完走後残課題（補注 GG 処理順）：連動軸 retrofit → gabun 裁定 → kaimyo-app 同期。
着手順はケンシンの意向を冒頭で確認
## 注意点
- マウント同期不具合継続前提。文書はホスト側ツールで編集
- motifs.json の正準形式は indent=1・末尾改行なし
- スクリプトの適用前 assert に m506 典籍曰く＋核心チェックを継承
進める前に、最優先タスクを確認してください。
```

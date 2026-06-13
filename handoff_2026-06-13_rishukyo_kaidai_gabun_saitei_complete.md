# 引き継ぎメモ 2026-06-13 理趣経開題 gabun 要否裁定完了（意図的未設定の継続＋線引きのジャンル基準精緻化）

**日付**：2026-06-13
**種別**：裁定記録セッション（retrofit 33 完走後残課題①・データ変更なし・文書 only）
**起点 HEAD**：`95d1287`（retrofit 33・着手前に巻き戻り検知全 pass で確認）
**ステータス**：裁定完了・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：_dev_references/motifs_index_design.md（補注 II）・CLAUDE.md（タイトル行・現在の進捗）・commit_message.txt・本メモ。**data/indices/motifs.json は不変**。corpus・索引・manifest も不変。
**commit_message.txt 更新確認**：済（冒頭行＝本裁定の内容と整合）

---

## ケンシン裁定（本セッション）

1. **着手順**：①gabun 要否裁定を選択（②kaimyo-app 同期は残作業へ）
2. **gabun 裁定**：理趣経開題 全 16 motifs（m2384-m2399）の gendai_gabun は **意図的未設定を継続**（hizoki/jujushinron/yugikyo と同運用・将来 retrofit 可能性は温存）
3. **線引きの精緻化**：運用線引きを**著者帰属基準からジャンル基準へ精緻化**することを承認

## 線引きの精緻化（詳細は補注 II）

- **旧**：「空海自筆（性霊集系）＝gabun あり／非空海・教学系 W3 以降＝意図的未設定」＝著者帰属（自筆／非自筆）が主軸
- **新**：「**性霊集系の文藝ジャンル（願文・表白・詩文等）＝gabun あり／教学・注釈系（開題・論義・経典注釈等、非性霊集）＝gabun 意図的未設定（自筆・非自筆を問わず）**」＝ジャンルが主軸
- **本裁定の意義**：瑜祇経までは非空海（伝・金剛智訳）ゆえ著者帰属軸で判定できたが、理趣経開題は**初の「空海自筆かつ教学注釈系」corpus**であり、「自筆＝gabun」と「教学系＝未設定」のどちらを優先するかが初めて問われた。判定軸をジャンルへ移すことで自筆・非自筆を問わず一貫判定が可能になり、今後の空海自筆の開題系 corpus（金剛頂経開題・大日経開題等）にもそのまま適用できる。

## 根拠

- 開題＝経典注釈・教学総説で密教術語が密に積層した本文（m2386 題目釈・m2387 三門釈等）は、願文・表白のような文藝的修辞を雅文体に開く対象とは性格を異にする（十住心論・秘蔵記・瑜祇経と同じ教学注釈系の文体圏）。
- kaimyo-app は gabun 不在時 text_kakikudashi にフォールバックする設計（§3 柔モード）のため、未設定でも利用側の欠落は生じない。
- 著者帰属を主軸とした旧線引きでは空海自筆の教学注釈系が宙に浮く。ジャンル基準に揃えることで判定の一貫性を確保。

## データへの影響

- **motifs.json 不変**：total_motifs 2428・sg01-sg29・schema 0.2・schema_history（top-level）163 のまま。famous_phrases 29 不変。
- stats.motifs_without_gendai_gabun_intentional の rishukyo-kaidai_m2384-m2399 キー（「理趣経開題 motif は gabun 未設定（hizoki/jujushinron/yugikyo と同運用・将来 retrofit 可）」）は **R1（motif 抽出第1ラウンド）時点で記載済み**のため温存。実データは既に未設定側に整合（**2428＝gabun 有 2173＋意図的未設定 255**〔m06 1＋sg01-sg29 29＋jujushinron 100＋hizoki 90＋yugikyo 19＋rishukyo-kaidai 16〕）。
- 本裁定の記録は補注 II・CLAUDE.md・本メモのみ（文書 only）。

## 副次対応（本セッションで同時処理）

1. **作業ツリー破損 2 ファイルの HEAD 復元**：着手時、git に未コミット差分が 2 件存在（`_dev_references/motifs_index_design.md` 末尾 -87 行〔補注 HH の schema_history 是正・多系統連動論点がまるごと欠落〕・`CLAUDE.md` 化け 1 行〔末尾マルチバイト 1 バイトズレ〕）。いずれも retrofit 33 で正しくコミット済みの内容がマウント同期 truncation で作業ツリー側だけ削れたもの。`git restore` は bash 側 unlink 不可（Operation not permitted）で失敗したため、**in-place リダイレクト（`git show HEAD:path > path`・inode 保持）で復元**し内容ロスなしを確認。
2. **作業残骸クリーンアップ**：`_tmp_build33.py`（0 バイト）を削除（cowork file delete 許可後に rm）。

## 検証（着手時・全 pass）

巻き戻り検知：HEAD 95d1287／total_motifs=2428=len／m-id 連番 m01-m2399（missing なし）／sg01-sg29（29 件・famous 29）／m506 引用形式:典籍曰く／m2386 連動:sg20/sg03/sg18／m2387 連動:sg08／m2399 連動:sg03／m2375・m2378・m2381・m2385・m2387・m2398 一句性:核心／schema_history（top-level）=163・末尾 origin=retrofit_33:rishukyo-kaidai_rendou_scan。
本セッションは motifs.json に触れないため適用後の JSON 再検証は不要（不変をホスト側 Grep で確認）。

## 副次発見・要注意事項

- **マウント同期不具合の方向性を実地確認**：本セッションでは host 側 Edit が bash/git 側に**部分的にしか伝播しない**事象を確認。CLAUDE.md の host Edit は bash 側にも反映（git が M 検知）したが、motifs_index_design.md の host Edit（補注 II 追加）は bash 側に未反映（grep 0・行数 1641 のまま・git diff 空）。**host 側 Grep では補注 II 存在確認済み**。commit は host 側 commit_push.bat 実行で行われるため host ファイル状態（＝正）が拾われる。**文書の真値は host 側。bash/git は stale ミラーとして扱い、bash 側 git status を最終確認に使わないこと**。
- CLAUDE.md タイトル行（1 行目・73,277 字・145KB）巨大化継続。Edit 前に 2 行目以降を小さく Read してファイル登録→部分文字列アンカーで Edit する手順を踏襲。
- 補注ラベルは **II**（GG＝瑜祇経 gabun・HH＝retrofit 33 で既使用）。
- repo ルート直下に `python-3.14.6-amd64.exe`（30MB・untracked・gitignore 外・6/11 迷い込み）が残存。削除可だが本セッションでは保留（要ケンシン確認）。

## 残作業（次セッション）

- **kaimyo-app 側 motifs.json 同期**（理趣経開題 完走後残課題の最後）：2428 版の単純コピー＋SHA-256 一致確認。m2398 廻向偈 43 字が橋プール入りする可能性 → 冠生成（理趣経開題系 CORPUS_DISPLAY_NAME 要否）をアプリ側で確認。**着手前に kakikudashi-data スキル必読**。
- その後の次期 corpus 候補：金剛頂経開題（47 段落）・大日経開題（97 段落）・菩提心論講要（146 段落・典籍曰く）・大日経本体（896 段落・長期）。

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2428・最終 m-id=m2399・sg01-sg29・m506 引用形式:典籍曰く・m2386 連動:sg20/sg03/sg18・m2387 連動:sg08・m2399 連動:sg03・m2375/m2378/m2381/m2385/m2387/m2398 一句性:核心（巻き戻り検知・本裁定は motifs.json 不変ゆえ retrofit 33 と同一値のはず）
3. schema_history（top-level）=163・末尾 origin=retrofit_33:rishukyo-kaidai_rendou_scan（本裁定で不変）
4. スクリプトの適用前 assert に m506 典籍曰く＋核心チェックを継承
5. マウント同期不具合継続前提：**文書はホスト側ツールで編集・読み（bash/git は stale ミラー）**・motifs.json の正準形式は indent=1・末尾改行なし

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- 理趣経開題 gabun 要否裁定完了 commit 済（commit <ハッシュ>）：意図的未設定を継続・
  線引きを著者帰属基準からジャンル基準へ精緻化（性霊集の文藝系＝gabun あり／
  教学・注釈系＝意図的未設定・自筆問わず）・補注 II・motifs.json 不変・
  total_motifs 2428・sg01-sg29・schema_history top-level 163 のまま
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-13_rishukyo_kaidai_gabun_saitei_complete.md
## 確認
git log --oneline -3 で HEAD・motifs.json total_motifs=2428・最終 m2399・sg01-sg29・
m506 典籍曰く・m2386 連動:sg20/sg03/sg18・m2387 連動:sg08・m2399 連動:sg03（巻き戻り検知）・
schema_history top-level=163・末尾 retrofit_33
## 次の作業
理趣経開題 完走後残課題の最後：kaimyo-app 側 motifs.json 同期
（2428 版コピー＋SHA-256 一致・m2398 廻向偈の橋プール入り可否・CORPUS_DISPLAY_NAME 要否確認・
着手前に kakikudashi-data スキル必読）
## 注意点
- マウント同期不具合継続前提。文書はホスト側ツールで編集・読み（bash/git は stale ミラー）
- motifs.json の正準形式は indent=1・末尾改行なし
- schema_history は二系統併存。追記は top-level のみ。着手時に末尾 origin と件数を照合
- スクリプトの適用前 assert に m506 典籍曰く＋核心チェックを継承
進める前に、最優先タスクを確認してください。
```

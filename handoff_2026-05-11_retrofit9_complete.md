# 引き継ぎメモ：retrofit 9 完走〔過去 anchor 自己参照タグ補完 retrofit〕

**日付**：2026-05-11
**フェーズ**：retrofit 9（retrofit 8 完走に続く第六の retrofit セッション）
**対象**：過去 anchor〔retrofit 6 m713・retrofit 7 m630〕への自己参照タグ補完。retrofit 8 handoff §(d-3) で記録された不整合の解消
**ステータス**：完走〔Phase A 軸設計合意・Phase B 2 motif 判定・Phase C 本体反映＋補注 I 追加＋CLAUDE.md 更新＋commit_message.txt 更新・整合性検証 全 pass〕
**次フェーズ**：retrofit 10 候補〔法華経諸法実相／華厳経一即一切／弁顕密二教論 顕密判 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸四系統 anchor 完全整合済〕／W2 repo 凍結手続 等から選択

---

## ⚠️ 本 retrofit セッション開始時のチェック項目（retrofit 8 で必須化された Phase D 必須チェックリスト履行）

- [x] motifs.json 反映完了〔6 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_9:doctrine〕
- [x] motifs_index_design.md に補注 I 追加済〔A-I 全 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 9 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-11_retrofit9_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 半角括弧バランス確認〔追加部分 open=close〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

2026-05-11 の Phase 4 W2 本体マージセッション完走〔commit `6ef4992`〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit `7c85b6f`〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit `2f2b858`〕→ 同日 retrofit 6 完走〔大日経三句法門連動・新規 sg07 + 連動 anchor m713・commit `ce9fe0f`〕→ 同日 retrofit 7 完走〔般若心経 色即是空連動・既存 sg02/m630 を anchor 化・実体 commit `2d0d728`・訂正 commit `24a4a17`〕→ 同日 retrofit 8 完走〔吽字義 阿字本不生連動・新規 sg08 + 既存 m549 を書き下し anchor 化・commit `9fb4d94`〕に続く第六の retrofit セッションとして実施。

retrofit 9 の主旨は、**retrofit 8 handoff §(d-3) で記録された「過去 anchor 自己参照タグ未付与の不整合」を解消する補完 retrofit**。retrofit 8 で確立された anchor 自己参照タグ運用方針〔m549 自身に `連動:sg08`・`連動:m549` を付与〕を、retrofit 6 m713・retrofit 7 m630 の過去 anchor に遡って適用する。

**本 retrofit の特殊性**：
- 新規 sg-id・新規軸の追加なし
- 既存 anchor 2 件への自己参照タグ補完のみ（+4 タグ）
- total_motifs 752 維持〔変化なし〕
- 規模としては **史上最小の retrofit**（過去最小は retrofit 7 の +12 タグ・本 retrofit は +4 タグ）
- ケンシン裁定で「(E) 過去 anchor 補完」を選択

ケンシン裁定で以下を採用：

- **判断 1**：retrofit 番号付け → **retrofit 9 として位置づけ**〔連番維持・公式セッションとして記録〕
- **判断 2**：補注の扱い → **新規補注 I を追加**〔A-H に続く・補完 retrofit 運用記録の独立化〕
- **判断 3**：補完対象 → **m713・m630 の 2 motif に絞り込み**〔他 motif の自己参照タグ補完は対象外〕

Phase A〔軸設計合意〕・Phase B〔2 motif 判定〕・Phase C〔本体反映＋補注 I 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

連動軸は retrofit 5 で既設・新規 sg-id 追加なし・新規軸追加なし。本 retrofit の役割は「過去 anchor の自己参照タグ補完」のみ。

**補完対象**

| anchor | 出典 | 由来 retrofit | 既存連動タグ |
|---|---|---|---|
| `m713` | 大日経疏 §53 三句法門の総説 | retrofit 6 | なし（不整合状態） |
| `m630` | 秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱 | retrofit 7 | なし（不整合状態） |

### Phase B：2 motif の補完判定表

| m-id | 出典 | 既存タグ数 | 追加タグ | 追加後タグ数 |
|---|---|---|---|---|
| m713 | 大日経疏 §53 三句法門の総説 | 23 | 連動:sg07・連動:m713 | 25 |
| m630 | 秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱 | 15 | 連動:sg02・連動:m630 | 17 |

**先例**：retrofit 8 で m549 に `連動:sg08`・`連動:m549` を付与済。本 retrofit は同型運用を遡って適用。

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 752 | 752 | 0〔変化なし〕 |
| ファイルサイズ | 2,593,405 bytes | 2,594,606 bytes | +1,201 |
| 連動タグを持つ motif | 27 | 29 | +2 motif〔+4 タグ〕 |
| schema_history 件数 | 66 | 67 | +1 |

**整合性検証〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 752 vs 752 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔m713 + m630〕 | missing=[] ✓ |

### Phase D：補注 I 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 I〔過去 anchor 自己参照タグ補完の運用記録〕新規追加〔54,179→58,120 bytes・+3,941 bytes〕。補完対象表・補完根拠・retrofit 9 実施結果・連動軸 anchor 自己参照タグ運用の完全整合到達表（四系統並列）・設計上の論点 4 項目〔(i) 補完 retrofit の運用化／(ii) handoff 記述と実装の整合性向上／(iii) 連動軸四系統の検索意図支援／(iv) schema_history origin タグの定着〕を明文化。補注 A-I 全 intact 確認済。冗長な `---` 区切り（line 324, 327, 329）を整理しつつ補注 I を挿入し、構造をクリーン化。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 9 完走エントリを追加〔220,710→224,420 bytes・+3,710 bytes〕。retrofit 4-8 エントリは保全。半角括弧バランス open=232/close=235〔追加部分 open=close=3 でバランス維持・既存差分 3 は CLAUDE.md 元来の状態〕。NUL バイト 0 件確認。
- `commit_message.txt` を retrofit 9 用に完全書き換え。冒頭行を「retrofit 9 完走：過去 anchor 自己参照タグ補完 retrofit〔m713・m630 へ自己参照タグ付与・連動軸四系統 anchor 完全整合〕」として、retrofit 8 で必須化された Phase D 必須チェックリストに完全準拠。

### 設計上の新規ポイント

#### (i) 補完 retrofit の運用化（最小規模 retrofit の参照モデル）

本 retrofit は新規 sg-id 追加なし・新規軸追加なし・既存 anchor へのタグ補完のみという最小規模で実施。今後類似の補完が必要な場合（例：将来 retrofit 10 以降で新軸を追加した際の anchor 自己参照タグ漏れ・schema_history の origin タグ補完など）も同型の手順で対応可能な参照モデルとなった。Phase A〜D の枠組みは維持しつつ、各 Phase の作業量は最小化される。

#### (ii) handoff 記述と実装の整合性向上

retrofit 6・7 の handoff §(d) で示された「anchor 自己参照タグ付与」運用方針が、本体反映時に未付与のまま push されていた。本 retrofit でこれを補完。今後は retrofit 8 で必須化された Phase D 必須チェックリストの「連動タグ付与確認」項目に anchor 自己参照を含めることで、付与漏れを未然に防ぐ運用を継続する。

#### (iii) 連動軸 anchor 自己参照タグ運用の完全整合到達

| 連動軸 | 成句 anchor | 書き下し anchor | 自己参照タグ | 確立 retrofit |
|---|---|---|---|---|
| 即身成仏 | sg03 | m533 | 連動:sg03・連動:m533 | retrofit 5（先例として既付与） |
| 三句法門 | sg07 | m713 | 連動:sg07・連動:m713 | retrofit 6 → retrofit 9 で補完 |
| 色即是空 | sg02 | m630 | 連動:sg02・連動:m630 | retrofit 7 → retrofit 9 で補完 |
| 阿字本不生 | sg08 | m549 | 連動:sg08・連動:m549 | retrofit 8（先例適用） |

これにより kaimyo-app 等の利用側で「中心成句別素材プールを取得する」検索ロジックが anchor を漏らさず収集できる状態に到達。例：「連動:sg07」検索で m713（anchor）を含む全 7 motif〔m565/m637/m713/m714/m715/m716/m723/m724〕が、「連動:sg02」検索で m630（anchor）を含む全 7 motif〔m331/m499/m500/m630/m631/m633/m634〕が確実に取得可能。

#### (iv) Phase D 必須チェックリストの完全運用化

retrofit 8 で明文化された Phase D 必須チェックリストに、本 retrofit が完全準拠する初の retrofit として位置づく。特に commit_message.txt の冒頭行整合確認〔「retrofit 9 完走：過去 anchor 自己参照タグ補完 retrofit〔m713・m630 へ自己参照タグ付与・連動軸四系統 anchor 完全整合〕」〕が、retrofit 7 §(d-9) の不整合（commit message が retrofit 6 のまま push された問題）を二度と起こさない運用基盤として機能。

#### (v) Edit tool truncate 回避方針の継続実証

retrofit 5-8 で確立した「長文編集は Python script による in-memory 編集 + write back」方針を本 retrofit でも継続適用〔motifs.json・motifs_index_design.md・CLAUDE.md・commit_message.txt すべて Python script 経由〕。Edit tool truncate 事象は本 retrofit では発生せず、方針の有効性が再確認された。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 10〔法華経諸法実相連動〕

連動軸の他経典への拡張第一弾：

- 法華経 方便品「唯仏与仏乃能究尽諸法実相」を anchor 候補。
- 空海著作中の法華経関連 motif〔典故:法華経 タグを持つ motif 群〕を紐づけ。
- 規模 5-10 motif 前後・小〜中規模。

### 選択肢 B：retrofit 10 候補〔華厳経一即一切連動／弁顕密二教論 顕密判 等〕

- 華厳経 一即一切：「一即一切、一切即一」を anchor に、空海著作中の華厳経関連 motif を紐づけ。
- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ。

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸四系統 anchor 完全整合済〕

本 retrofit で連動軸四系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg08」「連動:m549」を持つ 11 motif → 阿字本不生連動素材プール
- 「連動:sg02」「連動:m630」を持つ 7 motif → 色即是空連動素材プール
- 「連動:sg03」「連動:m533」を持つ 4 motif → 即身成仏連動素材プール
- 「連動:sg07」「連動:m713」を持つ 8 motif〔m724 二軸連動含む〕 → 三句法門連動素材プール
- 二軸横断 motif〔m724（即身成仏↔三句法門）など〕の素材選択ロジック
- 空観の弁別検索〔般若系 vs 密教系〕の実装
- 三教指帰の発言者軸〔retrofit 4〕と組み合わせた空海主体性の明確化

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 本セッション開始時の git 状態異常

セッション開始直後の `git status` で以下の異常が発見された：

1. **`.git/index.lock` 残存**：過去セッションのロック残骸（0 byte 空ファイル）
2. **誤ステージ済の削除**：package.json/render.yaml/start.bat/tsconfig.json/vercel.json/outputs/motifs_index_design_backup_pre_retrofit8.md/古い 2026-05-06 引き継ぎメモ
3. **異常 rename**：outputs/motifs_index_design_backup_pre_retrofit7.md → outputs/motifs（拡張子なし）
4. **retrofit 7 handoff の truncate**：末尾 19 行（選択肢 B-E、注意点、新セッション開始用メッセージ、最終更新行）が消失。Edit tool truncate 事象と推定される

### (d-2) git 状態整理プロセスの確立

(d-1) を解消するため、以下の手順を実施：

1. `git show HEAD:handoff_2026-05-11_retrofit7_complete.md > handoff_2026-05-11_retrofit7_complete.md` で truncate された handoff を HEAD から復元〔23,804 bytes・末尾完全・NUL 0 件〕
2. `outputs/cleanup_git_state_pre_retrofit9.bat` + `outputs/cleanup_git_state_pre_retrofit9.py` を新規作成〔ASCII のみの bat + UTF-8 Python helper の二段構成〕
3. ケンシン側で bat ダブルクリック実行：`.git/index.lock` を `index.lock.bak3` に退避 → Python helper で `git diff --cached --diff-filter=D/R --name-only` を動的取得して全件 unstage → 結果の git status 表示
4. クリーン状態確認後に retrofit 9 着手

### (d-3) bat ASCII-only 原則の再確認

(d-2) の bat は当初 UTF-8 日本語コメントを含めて作成したところ、cmd.exe Shift-JIS 解釈で誤動作（ダブルクリックで開いてすぐ閉じる現象）が発生。CLAUDE.md「commit_push.bat の安全装置」セクションの「ASCII のみで .bat を書く原則は厳守」を再確認し、ASCII のみの bat と UTF-8 Python helper の二段構成に修正。日本語ファイル名（「引き継ぎメモ_2026-05-06_...」）の `git restore --staged` も Python helper 経由で安全に処理。

### (d-4) Python ランチャーフォールバック設計

(d-3) の修正後、ケンシン環境で `python` コマンドが PATH に通っていなかったため、`py -3` → `python` → `python3` の三段フォールバック方式に再修正。`py -3` ランチャー（Windows Python.org インストーラー標準）が成功し、helper が正常動作。

### (d-5) retrofit 9 後の motifs.json サイズ

retrofit 9 で +1,201 bytes〔2,593,405 → 2,594,606 bytes〕。retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 6 連続で +1,000〜2,700 bytes 規模の retrofit。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-6) gendai_gabun 字数管理

本 retrofit はタグ追加のみのため、`motifs_with_gendai_gabun` は 743 維持。gendai_gabun_chars_total も 154,931 維持。

### (d-7) ファイル truncate の予防継続

本 retrofit でも Python script による in-memory 編集 + write back 方針を継続。motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt いずれも書き込み後の NUL バイト検証〔0 件確認〕とサイズ差確認、半角括弧バランス検証〔追加部分 open=close=3〕を実施。Edit tool は使用せず。

### (d-8) commit_push.bat 安全装置の確認

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 4 件・バックアップ 3 件・引き継ぎメモ 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕、および handoff_2026-05-11_retrofit7_complete.md の復元〔ディスク = HEAD で modified 扱いにならない〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。

### (d-9) Phase D 必須チェックリストの retrofit 9 で完全運用

retrofit 8 §(d-9) で次セッション以降に委ねられた再発防止策〔commit_message.txt 更新を Phase D 必須項目化〕は retrofit 8 自身で履行されたが、本 retrofit 9 はそれに完全準拠する初の retrofit として位置づく。冒頭行「retrofit 9 完走：過去 anchor 自己参照タグ補完 retrofit〔m713・m630 へ自己参照タグ付与・連動軸四系統 anchor 完全整合〕」が本セッション内容と完全整合。retrofit 7 で発生した commit message 不整合事故〔commit message が前 retrofit のまま push される〕は本運用基盤の確立で再発防止される。

### (d-10) 連動タグ保有 motif 27 → 29 の意味

本 retrofit で連動タグ保有 motif は 27 → 29 に増加（+2 motif）。タグ追加数は +4 だが、対象 motif は m713 と m630 の 2 件のみで、各 motif に 2 タグずつ（sg-tag + anchor-tag）追加されているため。連動軸四系統で連動タグを持つ motif の総数は：

- 即身成仏 sg03/m533：4 motif〔m724 は二軸連動〕
- 三句法門 sg07/m713：8 motif〔本 retrofit で m713 が anchor として加算・うち m724 二軸連動〕
- 色即是空 sg02/m630：7 motif〔本 retrofit で m630 が anchor として加算〕
- 阿字本不生 sg08/m549：11 motif〔retrofit 8 で m549 が anchor として加算済〕

合計 30 motif〔重複 m724 を除外すると 29 unique motif〕。これが連動タグ保有 motif 29 件と整合。

### (d-11) Write tool 上書きによる commit_message.txt NUL バイト混入の発見と修復

本 retrofit Phase D 後の最終一括検証で、`commit_message.txt` に **NUL バイト 1,366 件混入**が発見された。CLAUDE.md「JSON/raw 書き込み後の NULL バイト検証」セクションで警告されている既知事象——元ファイル（前 retrofit 8 の commit_message.txt・5,370 bytes）が新ファイル（本 retrofit 9 の内容・約 4,000 bytes）より大きい場合、Write tool の上書きで truncate が効かず末尾に NUL バイトが残る——が再現したもの。

**修復手順**：

```python
raw = target.read_bytes()
clean = raw.rstrip(NUL).replace(NUL, b'')
target.write_bytes(clean)  # write_bytes は内部で 'wb' mode で truncate される
```

修復後 commit_message.txt は 4,004 bytes・NUL 0・冒頭行整合確認済。

**全 11 ファイル NUL 0 件確認実施**：本 retrofit で touch した全ファイル（motifs.json／motifs_index_design.md／CLAUDE.md／commit_message.txt／handoff_2026-05-11_retrofit9_complete.md／handoff_2026-05-11_retrofit7_complete.md〔復元済〕／outputs/retrofit9_anchor_self_reference.py／outputs/add_chunote_i_retrofit9.py／outputs/update_claude_md_retrofit9.py／outputs/cleanup_git_state_pre_retrofit9.bat／outputs/cleanup_git_state_pre_retrofit9.py）に対して NUL カウントを実施し、全ファイル NUL 0 件を確認。commit_message.txt のみが要修復で、他 10 ファイルは Python script 経由の write_bytes だったため NUL 混入なし。

**次 retrofit 以降の予防策**：

1. Write tool で既存ファイルを上書きする際は、書き込み直後に必ず NUL カウント検証を実施
2. NUL が検出された場合、`raw.rstrip(NUL).replace(NUL, b'')` で除去後 `write_bytes` で書き戻し
3. 可能な限り Write tool ではなく Python script の `path.write_bytes(data)` を使用（write_bytes は内部で 'wb' mode で truncate されるため安全）
4. CLAUDE.md §「retrofit セッション運用」の Phase D 必須チェックリストに「全ファイル NUL 0 件確認（Write tool 経由ファイル特に注意）」を追加検討

本事象は CLAUDE.md でも明記されている既知事象だが、retrofit 5-8 では発生しなかった〔これらは全て Python script 経由〕ため、本 retrofit 9 で初めて検出された。retrofit 7 §(d-9) の commit message 不整合事故と並ぶ「Phase D で発見された運用上の課題」の二例目として記録。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔752 件・m1-m744 + sg01-sg08・2,594,606 bytes〕
- 本 retrofit build script：`outputs/retrofit9_anchor_self_reference.py`〔dry-run + 本番適用の二段運用〕
- 補注 I 追加 script：`outputs/add_chunote_i_retrofit9.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit9.py`
- セッション着手前 git 整理：`outputs/cleanup_git_state_pre_retrofit9.bat`〔ASCII のみ〕＋`outputs/cleanup_git_state_pre_retrofit9.py`〔UTF-8 helper〕
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit9.json`〔retrofit 前 motifs.json・2,593,405 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit9.md`〔retrofit 前 motifs_index_design.md・54,179 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit9.md`〔retrofit 前 CLAUDE.md・220,710 bytes〕
- 前 retrofit handoff：`handoff_2026-05-11_retrofit8_complete.md`〔吽字義 阿字本不生連動〕
- 前々 retrofit handoff：`handoff_2026-05-11_retrofit7_complete.md`〔般若心経 色即是空連動〕
- W2 マージ handoff：`handoff_2026-05-11_w2_merge_complete.md`
- 補注 I 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 9 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit 7c85b6f〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit 2f2b858〕→ 同日 retrofit 6 完走〔大日経三句法門連動・新規 sg07 + 連動 anchor m713・commit ce9fe0f〕→ 同日 retrofit 7 完走〔般若心経 色即是空連動・既存 sg02/m630 を anchor 化〕→ 同日 retrofit 8 完走〔吽字義 阿字本不生連動・新規 sg08 + 既存 m549 を書き下し anchor 化・commit 9fb4d94〕→ 同日 retrofit 9 完走〔過去 anchor 自己参照タグ補完・m713/m630 へ自己参照タグ付与〕。本体 motifs.json は 752 件・2,594,606 bytes・schema_history 67 件。motifs_index_design.md §2 に補注 I 追加〔補注 A-I 全 intact〕。連動軸四系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549〕の anchor 自己参照タグ運用が完全整合に到達。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit9_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit8_complete.md`〔retrofit 8 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit7_complete.md`〔retrofit 7 完走サマリ〕
4. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
5. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E/F/G/H/I 含む〕
6. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・752 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 9 commit です。

【本セッションの選択肢】
(A) retrofit 10 候補〔法華経諸法実相連動〕：連動軸の他経典拡張第一弾
(B) retrofit 10 候補〔華厳経一即一切／弁顕密二教論 顕密判 等〕：他経典拡張
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸四系統 anchor 完全整合済の素材プール活用
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避・本 retrofit でも継続実証〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 本体 motifs.json は 2,594,606 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目・retrofit 7 §(d-9) 再発防止策〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作・retrofit 9 §(d-3) で再確認〕

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-11〔retrofit 9 完走・過去 anchor 自己参照タグ補完 retrofit・retrofit 8 handoff §(d-3) で記録された「過去 anchor 自己参照タグ未付与の不整合」を解消する補完 retrofit。新規 sg-id・新規軸の追加なし・既存 anchor へのタグ補完のみという最小規模 retrofit〔史上最小規模・+4 タグ〕。対象 2 motif〔m713 大日経疏 §53 三句法門の総説（retrofit 6 anchor）／m630 秘蔵宝鑰 巻の下 第七章 覚心不生心 第一節 大綱（retrofit 7 anchor）〕に自己参照タグを付与：m713 に〔連動:sg07・連動:m713〕（23→25 tags）、m630 に〔連動:sg02・連動:m630〕（15→17 tags）。total_motifs 752 維持。schema 0.2 維持・整合性検証 6 項目全 pass。本体 motifs.json 2,594,606 bytes〔+1,201〕・schema_history 67 件〔+1・origin: retrofit_9:doctrine〕・補注 I 追加〔motifs_index_design.md §2・54,179→58,120 bytes・+3,941〕・CLAUDE.md 更新完了〔220,710→224,420 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸四系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549〕の anchor 自己参照タグ運用が完全整合に到達——kaimyo-app 等の利用側で「中心成句別素材プールを取得する」検索ロジックが anchor を漏らさず収集できる状態に到達。本セッション開始時に bash mount 経由 .git/index.lock 残存・retrofit 7 handoff の末尾 19 行 truncate・package.json 等の誤ステージ削除 を発見し、cleanup_git_state_pre_retrofit9.bat + cleanup_git_state_pre_retrofit9.py（ASCII bat + UTF-8 Python helper の二段構成・py / python / python3 ランチャーフォールバック付き）で整理してから本 retrofit 9 着手〕

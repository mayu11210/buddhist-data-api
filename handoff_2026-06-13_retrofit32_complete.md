# 引き継ぎメモ 2026-06-13 retrofit 32 完走（瑜祇経 連動軸 retrofit・sg28/sg29 新設）

**日付**：2026-06-13
**種別**：retrofit セッション（Phase A〜D・retrofit 6 型＝新規 sg 新設＋既存軸被覆拡張）
**起点 HEAD**：`511c462`（瑜祇経 R2・push 済を着手前に検証全 pass で確認）
**ステータス**：retrofit 32 完了・検証全 pass・**未 commit / 未 push**（commit_push.bat 実行待ち）
**変更ファイル**：data/indices/motifs.json・_dev_references/motifs_index_design.md（補注 FF）・
CLAUDE.md・commit_message.txt・本メモ。corpus・索引・manifest は不変。
**commit_message.txt 更新確認**：済（冒頭行＝retrofit 32 の内容と整合・Phase D §(d-9) チェック済）

---

## ケンシン裁定（本セッション・Phase A／B）

1. **最優先タスク**：①連動軸 retrofit を選択（②gabun 裁定・③kaimyo-app 同期は残作業へ）
2. **sg 新設範囲**：2 件新設（即身五仏＋言語即真言）
3. **sg28 成句形**：四句全体・通行形「如如」採用（genten T867 は「如和同一體」。
   底本 verbatim より通行形を優先した初例・gendaigoyaku 解説内に底本差を明記）
4. **引用形式**：sg28/sg29 とも 引用形式:典籍曰く（R1 Phase A 合意と整合。
   sg07 経曰く 先例とは著者帰属確実性〔瑜祇経＝伝・金剛智訳〕で使い分け）
5. **強候補 4 件**：全件採用（m2369/m2372→sg27・m2381→sg03・m2375→sg19）
6. **境界 3 件**：m2366→sg27 のみ採用。m2378・m2380 は温存（DD 修法配当温存原則の継承）

## 成果

### 新設成句 2 件（sg27 直後に挿入・sg ブロック一体保持）

| id | text_kakikudashi | 出典（品） | anchor |
|---|---|---|---|
| sg28 | 金剛即宝光、蓮華即羯磨、如如同一体、即此身五仏 | 内作業灌頂悉地品第十一 | m2381 |
| sg29 | 所出言便成真言、挙動支節成大印契 | 金剛吉祥大成就品第九 | m2375 |

共通タグ：category:密教教学・成句:famous・出典:瑜祇経・引用形式:典籍曰く・一句性:核心・含意:全人生。
gabun は成句方針により意図的未設定（without_gabun キー sg01-sg29 に統合）。

### 連動タグ付与（5 motif・+14）

- **m2381** → 連動:sg28・連動:m2381・連動:sg03・連動:m533〔即ちこの身五仏なり＝即身成仏の経証。
  多系統連動の第四例（m524・m637・m2362 に続く）〕
- **m2375** → 連動:sg29・連動:m2375・連動:sg19・連動:m525〔言語即真言⇄声字実相の典籍横断〕
- **m2369** → 連動:sg27・連動:m719〔本有の金剛の光明・清浄にして染まらず・本来寂静〕
- **m2372** → 連動:sg27・連動:m719〔一切の法は本来清浄なりと観すべし〕
- **m2366** → 連動:sg27・連動:m719〔本有不生の性を開かん等・神変目的宣言 4 回（境界採用）〕

### 温存 14 件（根拠は補注 FF）

m2378（内護摩本義・修法文脈）・m2380（仏性月喩・観想構成文脈）・m2373/m2382（吽字＝種子観想・
DD m2304 同型）・m2376（一切智々＝功徳列挙）・m2365（会座荘厳叙述）・
m2367/m2368/m2370/m2371/m2374/m2377/m2379/m2383（修法・儀軌・図像・讃文脈）

## stats 差分

- total_motifs 2410→**2412**（+2 sg）・famous_phrases 27→**29**・sg 27→29 件
- kakikudashi_chars_total 238,995→239,034（+39）・gendaigoyaku_chars_total 705,934→706,808（+874）
- 篇別内訳 成句_二十七件→成句_二十九件（sg28/sg29 追記・件数 29・キー位置保持）
- motifs_without_gendai_gabun_intentional キー sg01-sg27→sg01-sg29（値温存・キー位置保持）
- top-level description 現況化（2412 motifs＝m1〜m2383＋成句 sg01〜sg29・連動軸**二十五系統**並立）
- schema_history 160→161（origin: retrofit_32:yugikyo_rendou_scan）・stats.generated_at 2026-06-13 不変

## 検証（全 pass）

整合性 12 項目：total=len=2412／m-id 連番 m1-m2383（missing/dup なし）／NUL 0／schema 0.2／
必須フィールド完全／連動タグ +14／sg01-sg29 連番・挿入位置（sg27 直後）／recompute 全ゼロ／
m506 典籍曰く・核心 3 post／anchor 自己参照 5 軸（sg03/m533・sg19/m525・sg27/m719・sg28/m2381・
sg29/m2375）／新規 sg 半角括弧 0／schema_history +1。
巻き戻り検知：m506 引用形式:典籍曰く・m2375/m2378/m2381 一句性:核心 とも適用前後 pass。
ホスト側 Grep 反映確認（total_motifs 2412・sg28/sg29・連動:sg28/sg29 各 2 件）。
バックアップ：outputs/motifs_backup_pre_retrofit32.json（コミット対象外）。
build script：outputs/retrofit32_yugikyo_rendou_scan.py（dry-run→apply・コミット対象外）。

## 副次発見・要注意事項

- マウント同期不具合継続前提（bash 側 git status に幻影差分 M CLAUDE.md あり・ホスト実体は正常）。
  着手時の git status に旧 2026-05-06 引き継ぎメモの RD（rename staged・文字化け表示）も見えたが、
  commit_push.bat の Step 1-2 index リセットで解消される類。Step 4.5 で deleted: 検出時は
  phantom 疑いとしてホスト実体確認のこと。
- sg28 で「通行形 ＞ 底本 verbatim」の成句表記先例ができた（補注 FF）。今後の成句新設時は
  底本差の有無を genten 照合で必ず確認し、差があればケンシン裁定とする。

## 残作業（次セッション以降）

- **gabun（雅文体訳）要否裁定**（yugikyo 全 19 motifs・hizoki/jujushinron と同運用中）
- **kaimyo-app 側 motifs.json 同期**（単純コピー＋NUL 0／total 2412／引用形式タグ確認。
  典籍曰く冠生成ロジック対応要否・新 sg28/sg29 の扱い確認を含む）

## 次セッション開始時の確認

1. CLAUDE.md → 本メモ → `git log --oneline -3`（HEAD が本コミットであること）
2. motifs.json：total_motifs=2412・最終 m-id=m2383・sg01-sg29・m506 引用形式:典籍曰く・
   m2375/m2378/m2381 一句性:核心・m2381 連動:sg28・m2375 連動:sg29（巻き戻り検知）
3. スクリプトの適用前 assert に m506 典籍曰く＋核心 3 チェックを継承すること
4. マウント同期不具合継続前提：文書はホスト側ツールで編集・motifs.json の正準形式は
   indent=1・末尾改行なし

## 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
buddhist-data-api の続き。まず CLAUDE.md を読んでから進めてください。
## 前セッションまでの到達点
- retrofit 32 完走（commit <ハッシュ>）：瑜祇経 連動軸 retrofit・sg28 即身五仏／
  sg29 言語即真言 新設（anchor m2381/m2375）・強連動 5 motif に +14 連動タグ
  （m2381→sg03・m2375→sg19・m2366/m2369/m2372→sg27）・温存 m2378/m2380・
  total_motifs 2410→2412・連動軸二十五系統・補注 FF
## 最初に読むファイル
1. CLAUDE.md
2. handoff_2026-06-13_retrofit32_complete.md
## 確認
git log --oneline -3 で HEAD・motifs.json total_motifs=2412・sg01-sg29・
m506 引用形式:典籍曰く・m2375/m2378/m2381 一句性:核心・m2381 連動:sg28（巻き戻り検知）
## 次の作業
（いずれかをケンシン裁定）①gabun 要否裁定（yugikyo 19 motifs）／
②kaimyo-app 側 motifs.json 同期（典籍曰く冠生成・sg28/sg29 対応確認含む）
## 注意点
- マウント同期不具合継続前提。文書はホスト側ツールで編集
- motifs.json の正準形式は indent=1・末尾改行なし
- スクリプトの適用前 assert に m506 典籍曰く＋核心 3 チェックを継承
進める前に、最優先タスクを確認してください。
```

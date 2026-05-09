# 引き継ぎメモ：★ Phase 4 W1 マージセッション完了 ★（W1 buddhist-shoryoshu-workshop → 本体統合）

**日付**：2026-05-09
**フェーズ**：Phase 4 W1（W1 性霊集 workshop の本体への移設マージ）
**起点**：本体 commit `3e261b3`（2026-05-08 候補 B 第 12 ラウンド完走・m287 まで）
**終点**：本マージで本体 motifs.json は m001〜m404 + sg01〜sg06 = 410 motifs に到達
**選択**：案 A1（含意の射程 第八〜第十区分を本マージで確定・schema 0.2 維持）

---

## (a) 本セッションの位置づけ

W1 buddhist-shoryoshu-workshop（commit `9740953`・第 11 ラウンド完走 idx=37 大使福州観察使書・★ W1 全篇完走★）+ マージ準備 commit `b76d966` を起点に、本体 buddhist-data-api 側で Phase 4 W1 マージセッションを実施。W1 staging motif 計 123 件（sw001〜sw123）を本体 motifs.json に再番号付け統合。schema 0.3 化候補（含意の射程 第八〜第十区分）を案 A1 で確定。

paste メッセージのラベル参照誤記を CLAUDE.md 原則 11「ラベルより内容を信頼」で発見・修正：
- paste 主張：「m287 まで → sw001 → m288 → m410」
- 実状：m-id は m01〜m281（281 件）+ sg01〜sg06（6 件）= 計 287 件
- **正しいマッピング**：sw001 → m282 / sw123 → m404（最終 410 件は paste と整合）

---

## (b) 本セッションの主な成果

### Phase A：機械的マージ（schema 0.2 維持）

**実装**：`outputs/merge_w1_to_main.py`（単独 Python build script・dry-run + 本番適用の二段運用）

**統計差分**：

| 項目 | 反映前（commit 3e261b3）| 反映後（本マージ）|
|---|---|---|
| total_motifs | 287 | **410**（+123） |
| kakikudashi_chars_total | 20,216 | **31,985**（+11,769） |
| gendai_gabun_chars_total | 45,002 | **64,383**（+19,381） |
| gendaigoyaku_chars_total | 71,122 | **109,748**（+38,626） |
| motifs_with_gendai_gabun | 280 | **403**（+123） |
| 篇別内訳エントリ数 | 36 | **50**（+14） |
| stats vs recompute 差分 | 全ゼロ | **全ゼロ**（5 項目維持） |

**from_idxNN 追加（14 篇）**：idx=10 (12 件)・idx=1 (12 件)・idx=6 (6 件)・idx=7 (7 件)・idx=110 (11 件)・idx=109 (11 件)・idx=85 (8 件)・idx=108 (1 件)・idx=22 (5 件)・idx=88 (4 件)・idx=34 (7 件)・idx=106 (13 件)・idx=39 (13 件)・idx=37 (13 件) = 計 123 件

**検証 6 項目すべて pass**：
1. total_motifs = 410（target 410）OK
2. m-id 連番 m001〜m404 隙間なし・重複なし・sg-ids 6 件 OK
3. 半角括弧（motif text フィールド）open=0/close=0 OK
4. stats vs recompute 差分（5 項目）すべてゼロ OK
5. 篇別内訳 50 entries 全 dict 形式（non-dict ゼロ）OK
6. NUL バイト 0 件 OK

### Phase B：含意の射程 第八〜第十区分を確定（案 A1 採用）

| 区分 | タグ値 | 付与 motif | 出典 |
|---|---|---|---|
| 第八 | `含意の射程:辞退（教学型）` | **m378**（旧 sw097） | idx=106 結句・空海による最澄宛理趣釈経借用辞退 |
| 第九 | `含意の射程:求請（嘆願型）` | **m391**（旧 sw110） | idx=39 結句年代特定・空海による経書求請 |
| 第十 | `含意の射程:陳情（外交型）` | **m404**（旧 sw123） | idx=37 結句祈願典故六連・空海代筆遣唐使船福州陳情 |

含意の射程は篇内の代表 motif（結句または動機集約句）にのみ付与する原則を補注 C で明文化。

第七区分「辞退（謙辞型）」（idx=105 m281）と第八区分「辞退（教学型）」（idx=106 m378）は同じ「辞退」の動機別細分化：
- **謙辞型**：自分の力不足・年齢・地位等を理由に辞退（泰範が叡山行脚を辞退）
- **教学型**：教学上の理由・密教戒律上の理由で辞退（空海が顕密分守の立場から辞退）

schema_version は 0.2 維持（フィールド構造変更なし・タグ値運用拡張のみ）。

### `_dev_references/motifs_index_design.md` 補注追加

タグ軸セクション（§2）の末尾に補注 A・B・C を追加：

- **補注 A**：含意の射程 タグ値の運用拡張（2026-05-09 W1 マージで更新）：第一〜第十区分の運用記録 + 第七 vs 第八区分の細分化整理 + 新規区分の workshop proposal → 本体マージ合意プロトコル明文化
- **補注 B**：代筆書状・代筆勅書の motif 化方針：形式発信者を category:大師御言葉 で保持／代筆事実は gendaigoyaku 補注に明示／生者宛は故人タグ非付与／主体軸は形式発信者 + 代筆者双方を記録／対象軸は受信者を記録
- **補注 C**：含意の射程 タグの「代表 motif 付与」原則：篇内全 motif に一律付与せず結句または発心・廻向の主体句に限定

### 本体 CLAUDE.md 更新

- タイトル行：W1 マージセッション完走エントリを冒頭に追加
- 現在の進捗ヘッダ：410 motifs / 性霊集 49 篇 43.8% 抽出済を反映
- 次の作業セクション：Phase 4 W1 完了 → Phase 2b W2 立ち上げに変更
- 全体ロードマップ：Phase 2a/3 W1/4 W1 を完了印（★）付き行に更新
- 並行候補テーブル：候補 M 状態更新・候補 N（W1 archive + W2 前提条件）新規追加
- 最終更新行：本マージセッションエントリを冒頭に追加

### W1 archive 化方針（候補 N）

- (a) GitHub.com 上で `mayu11210/buddhist-shoryoshu-workshop` repo を archive（read-only）化する → ケンシン側で本マージ push 完了後に実施
- (b) ローカル `C:\Users\user\buddhist-shoryoshu-workshop\` は保全（消去しない）→ Phase 2 W1 ラウンドの履歴・引き継ぎメモ群はすべて参照可能なまま残る
- (c) 再開する場合は新 workshop（例：buddhist-shoryoshu-workshop-v2）を立ち上げる方針（プロトコル §10 (5) 準拠）

### W2 立ち上げ前提条件確立

- **schema 0.2 を維持**（W1 と同じ・フィールド構造変更なし）
- **タグ inventory**：含意の射程 10 区分（W1 マージ後の本体最新値）・主題タグ普遍概念限定原則（kaimyo-app 整理候補との整合）・代筆書状の motif 化方針（補注 B 準拠）
- **W2 スコープ**：教学系 9 著作（即身成仏義／吽字義／声字実相義／弁顕密二教論／般若心経秘鍵／秘蔵宝鑰／大日経疏 巻第一／菩提心論／三教指帰）
- **ID プレフィックス**：tw（W2 staging）→ 完走時に本体 m405 以降に再番号付け統合（W1 マージ後の本体最終 m-id m404 の次から）
- **想定セッション数**：5〜8 ラウンド

---

## (c) 残作業（次セッション以降の選択肢）

### 選択肢 A：Phase 2b W2 立ち上げ ★最優先

**手順**：

1. ケンシン側で GitHub.com 上に `mayu11210/buddhist-doctrine-workshop` repo を作成（Private 推奨）
2. ローカルに clone：`C:\Users\user\buddhist-doctrine-workshop\`
3. 本体から以下 3 ファイルをコピー（path 書換え）：
   - `_dev_references/workshop_protocol.md` → workshop 直下の `_dev_references/workshop_protocol.md`（参照用）
   - `_dev_references/workshop_CLAUDE_template.md` → workshop 直下の `CLAUDE.md`（W2 用に書き換え）
   - `_dev_references/workshop_commit_push_template.bat` → workshop 直下の `commit_push.bat`（path 書換え）
4. 本体から教学系 9 著作 json をコピー：
   - `data/kukai/sokushin-jobutsu.json`（即身成仏義）
   - `data/kukai/ujiji.json`（吽字義）
   - `data/kukai/shoji-jisso.json`（声字実相義）
   - `data/kukai/nikyo-ron.json`（弁顕密二教論）
   - `data/kukai/hannya-hiken.json`（般若心経秘鍵）
   - `data/kukai/hizo-houyaku.json`（秘蔵宝鑰）
   - `data/kukai/dainichikyo-sho-vol1.json`（大日経疏 巻第一）
   - `data/kukai/bodaishinron.json`（菩提心論）
   - `data/kukai/sankyo-shiki.json`（三教指帰）
5. 初期 `data/indices/motifs.json` を作成：
   ```json
   {
     "schema_version": "0.2",
     "_workshop": "W2 buddhist-doctrine-workshop",
     "schema_history": [],
     "motifs": [],
     "famous_phrases": [],
     "stats": {
       "total_motifs": 0,
       "kakikudashi_chars_total": 0,
       "gendai_gabun_chars_total": 0,
       "gendaigoyaku_chars_total": 0,
       "motifs_with_gendai_gabun": 0,
       "from_idx_breakdown": {}
     }
   }
   ```
6. Cowork 起動 → このフォルダを選択 → Phase 2b セッション開始

### 選択肢 B：性霊集 残 63 篇の継続抽出

W1 完走後の継続として、性霊集 残 63 篇（49 篇 → 全 112 篇）の motif 抽出を W1 拡張または新 workshop（例：buddhist-shoryoshu-workshop-v2）で実施。Phase 2b W2 とは並列可能。

### 選択肢 C：kaimyo-app 並列セッション

kaimyo-app 側のテーマ駆動辞書設計（commit `625451f` 系統）の継続。本マージで本体に追加された motif（m282〜m404）を kaimyo-app 側辞書に統合する作業余地あり。

---

## (d) 副次発見・要注意事項

### paste メッセージのラベル誤記事例

paste メッセージ（W1 → 本体マージ起動用）で「m287」を本体最終 m-id として記載していたが、実状は：
- m-id：m01〜m281（281 件）
- sg-id：sg01〜sg06（6 件）
- total_motifs：287（m + sg 合算）

「m287」は配列総数であって最終 m-id ではない。CLAUDE.md 原則 11「ラベルより内容を信頼」に従い、本マージ着手前に grep + JSON 解析で実状を確認し、マッピングを「sw001 → m282 / sw123 → m404」に修正してから Phase A に着手した。総数 410 は paste と整合。

**教訓**：paste メッセージ内の m-id 記載は本マージのような重要操作の前に必ず実状で再検証する。

### W1 で導入された普遍仏教概念タグ

W1 完走時に新規導入された主題タグ（普遍仏教概念に限定する原則準拠）：

- **idx=106 系統**：主題:師弟・主題:謙辞・主題:教判・主題:自行化他・主題:顕密二教・主題:醍醐・主題:辞退（既出 idx=105 由来）
- **idx=39 系統**：主題:辺境・主題:艱難・主題:時運・主題:歎き・主題:感応・主題:謝恩・主題:救済・主題:奉公（生者向け）
- **idx=37 系統**：主題:教化・主題:讃美・主題:無常（既出再使用）

これらはすべて kaimyo-app 側のテーマ駆動辞書設計（故人固有性キーワード→仏教概念タグ + 譬えキーワードのハイブリッド・2026-05-07 マージセッション合意）と直結。

### W1 で導入された典故タグ群

W1 マージで本体に流入した典故タグ inventory（既出は省略）：

- **新規**：典故:列子・典故:周礼・典故:楚辞・典故:山海経・典故:中阿含経・典故:金剛経・典故:神農本草経・典故:黄帝内経・典故:中庸・典故:孔子家語・典故:太平御覧・典故:新序・典故:心地観経・典故:後漢書・典故:荀子・典故:漢書・典故:孟子・典故:老子
- **既出再使用**：典故:荘子・典故:法華経・典故:論語・典故:史記・典故:詩経・典故:書経・典故:淮南子・典故:涅槃経・典故:華厳経・典故:礼記

性霊集の漢籍動員密度の広さが本マージで本体タグ inventory に集約された。

### 出典軸の使い分け（出典:書状 vs 出典:啓）

W1 で確立した使い分け：
- **出典:書状**：私信を含む広範な書状形式（idx=106 最澄宛・idx=37 観察使宛代筆）
- **出典:啓**：中国古典文学における特定の文書形式（多くは官員に提出する正式な要請文書・idx=39 越州節度使啓）

本マージで本体タグ inventory に統合された。

### 代筆書状の motif 化先例

W1 で確立した代筆書状の motif 化方針（idx=22／37／88／105／106／39）：
- 形式上の発信者を `category:大師御言葉` で保持
- 代筆事実は `text_gendaigoyaku` の補注に明示
- 生者宛は故人タグ非付与
- 主体軸は形式発信者 + 代筆者の双方を記録（例：`主体:泰範（代筆者：空海）`）
- 対象軸は受信者を記録（例：`対象:最澄`）

これらは本マージで `motifs_index_design.md` 補注 B として明文化された。

### 含意の射程 タグの代表 motif 付与原則

含意の射程は篇内の代表 motif（結句または動機集約句）に **限定して** 付与する。篇内全 motif に一律付与すると検索ノイズとなる。本マージで `motifs_index_design.md` 補注 C として明文化された。

### Linux サンドボックスの bash タイムアウト挙動

本セッション中、bash 出力が timeout で帰ってこない事象が一度発生。Python build script を heredoc で書き出して実行する形式に切り替えて解消。次回マージセッションでも同様の対応を推奨：複雑な script は `outputs/` に書き出してから `python3` で起動する形式。

---

## (e) 進捗テーブル（W1 マージ完了時）

### 性霊集 motif 抽出進捗

| 状態 | 篇数 | 篇 |
|---|---|---|
| 本体既存（commit 3e261b3 まで）| 35 篇 | idx=12, 44, 45, 47-66 多数, 68-76, 81, 89, 102, 105 等 |
| W1 マージで追加 | 14 篇 | idx=1, 6, 7, 10, 22, 34, 37, 39, 85, 88, 106, 108, 109, 110 |
| **計** | **49 篇 / 全 112 篇 43.8% 抽出済** | – |
| 残 | 63 篇 | – |

### 全体ロードマップ進捗（13 セッション完了 / 残 7〜10 セッション）

| Phase | 状態 |
|---|---|
| Phase 1（本体プロトコル整備） | ★ 完了（2026-05-08）★ |
| Phase 2a（W1 立ち上げ） | ★ 完了（2026-05-08）★ |
| Phase 3 W1（W1 14 篇 motif 抽出） | ★ 完了（2026-05-08〜2026-05-09・第 1〜11 ラウンド・sw001〜sw123）★ |
| Phase 4 W1（W1→本体 マージ） | ★ 完了（2026-05-09・本マージ・m282〜m404 統合）★ |
| Phase 2b（W2 立ち上げ） | 次セッション |
| Phase 3 W2（教学系 9 著作 motif 抽出） | 5〜8 セッション |
| Phase 4 W2（W2→本体 マージ） | 1 セッション |

---

## 関連ファイル

- 本マージ build script：`outputs/merge_w1_to_main.py`（dry-run + 本番適用版・410 motifs 統合）
- 本体最終 motifs.json：`data/indices/motifs.json`（410 motifs / m001〜m404 + sg01〜sg06）
- 本体 schema 仕様：`_dev_references/motifs_index_design.md`（schema 0.2 + 補注 A/B/C）
- 本体 workshop プロトコル：`_dev_references/workshop_protocol.md`（マージ手順 §10 / schema 更新 §11）
- W1 完走時 引き継ぎメモ：`C:\Users\user\buddhist-shoryoshu-workshop\handoff_2026-05-09_w1_completion_summary.md`（参照用）
- W1 マージ準備メモ：`C:\Users\user\buddhist-shoryoshu-workshop\merge_session_paste_message.md`（本マージ起動時に貼付済）
- W1 staging motifs.json：`C:\Users\user\buddhist-shoryoshu-workshop\data\indices\motifs.json`（123 motifs sw001〜sw123・archive 化対象）
- 本体 CLAUDE.md：`CLAUDE.md`（タイトル・進捗ヘッダ・並行候補テーブル更新済）
- 前セッション handoff：`handoff_2026-05-08_round12_idx105_complete.md`（本体最終ラウンド・本マージ起点）

---

## 新セッション開始用メッセージ（ケンシン貼付テンプレ・Phase 2b W2 立ち上げ用）

```
=== buddhist-data-api 本体 → buddhist-doctrine-workshop（W2）立ち上げ用 ===
新セッション開始です。Phase 4 W1 マージセッション完了（commit 未確定・本セッション push 後に確定）を経て、
次フェーズは Phase 2b：W2 buddhist-doctrine-workshop 立ち上げです（kaimyo-app と同じ並列パターンの workshop 系統）。

【本セッションの目的】
W2 buddhist-doctrine-workshop（教学系 9 著作・ID プレフィックス tw）を立ち上げ、
Phase 3 W2（motif 抽出 5〜8 セッション）に着手できる状態にします。

【最初に読むファイル（順番）】
1. CLAUDE.md（本体ルール・進捗ヘッダ・W1 マージ完了状態を反映済）
2. handoff_2026-05-09_w1_merge_complete.md（W1 マージ完了引き継ぎメモ）
3. _dev_references/workshop_protocol.md（標準仕様書 12 章構成）
4. _dev_references/workshop_CLAUDE_template.md（workshop 用 CLAUDE.md テンプレ）
5. _dev_references/workshop_commit_push_template.bat（commit_push.bat テンプレ）
6. _dev_references/motifs_index_design.md（schema 0.2 + 補注 A/B/C 含意の射程 10 区分）
7. data/indices/motifs.json（本体最終形・410 motifs / m001〜m404 + sg01〜sg06・参照のみ）

【git log 確認】
git log --oneline -5（HEAD は本セッション push commit 直後・W1 マージ完了 commit）

【本セッションの作業項目】
1. ケンシン側で GitHub.com 上に mayu11210/buddhist-doctrine-workshop repo を作成（Private 推奨）
2. ローカルに clone：C:\Users\user\buddhist-doctrine-workshop\
3. Cowork でこのフォルダを選択
4. 本体から以下のファイルをコピー：
   - _dev_references/workshop_protocol.md → 同名で workshop 直下にコピー
   - _dev_references/workshop_CLAUDE_template.md → workshop 直下の CLAUDE.md として書き換え（W2 用・教学系 9 著作スコープ・ID プレフィックス tw）
   - _dev_references/workshop_commit_push_template.bat → workshop 直下の commit_push.bat として path 書換え
5. 本体から教学系 9 著作 json をコピー：
   - sokushin-jobutsu.json / ujiji.json / shoji-jisso.json / nikyo-ron.json / hannya-hiken.json /
     hizo-houyaku.json / dainichikyo-sho-vol1.json / bodaishinron.json / sankyo-shiki.json
6. 初期 data/indices/motifs.json を作成（schema 0.2・空 motifs 配列・空 famous_phrases）
7. ケンシン側で commit_push.bat ダブルクリック → 初期 commit + push
8. workshop 立ち上げ完了の引き継ぎメモを作成（ASCII 名）

【今セッションでの絶対遵守事項】
- ★ W1 workshop の motifs.json は触らない（commit 9740953 で凍結・本マージで本体に統合済）★
- ★ 本体 motifs.json は触らない（本マージで 410 motifs に到達・以後は W2 マージで増分）★
- ★ 本セッションは W2 立ち上げのみ・motif 抽出は次セッション（Phase 3 W2 第 1 ラウンド）以降 ★
- bash 経由 git は禁止（commit / push / reset 等の書き込み系）
- ASCII のみで .bat を書く（cmd.exe Shift-JIS 解釈で日本語が壊れる）
- workshop 内 ID プレフィックスは tw（staging）・本体マージ時に m405 以降に再番号付け
- 主題タグは普遍仏教概念に限る（固有名詞抽出禁止・W1 で確立済原則踏襲）
- 含意の射程は本体の 10 区分から始め、新規区分は workshop で proposal → 本体マージで合意

【次セッション以降のロードマップ】
- Phase 2b（W2 立ち上げ・本セッション）：1 セッション
- Phase 3 W2（教学系 9 著作 motif 抽出）：5〜8 セッション
- Phase 4 W2（W2→本体 マージ）：1 セッション
- 並行候補：性霊集 残 63 篇の継続抽出（W1 拡張または別 workshop）

進める前に、W2 の repo 名（mayu11210/buddhist-doctrine-workshop）と Private 設定の確認、
および ID プレフィックス tw を採用する判断について確認してください。
=== ここまで ===
```

---

最終更新：2026-05-09（**★ Phase 4 W1 マージセッション完了★・W1 buddhist-shoryoshu-workshop（commit 9740953）から 123 motif（sw001〜sw123）を本体に統合・sw → m282〜m404 機械的再番号付け・本体 motifs.json 410 motifs（m001〜m404 + sg01〜sg06）達成・含意の射程 第八〜第十区分を確定（案 A1 採用）：辞退（教学型）m378／求請（嘆願型）m391／陳情（外交型）m404・schema 0.2 維持・motifs_index_design.md 補注 A/B/C 追加・本体 CLAUDE.md タイトル/進捗ヘッダ/全体ロードマップ/並行候補テーブル M+N/最終更新行 全更新・W1 archive 化方針確定（GitHub.com 上で archive・ローカル保全）・W2 立ち上げ前提条件確立（schema 0.2 / タグ inventory / 教学系 9 著作スコープ / ID プレフィックス tw）・性霊集抽出済み 49 篇 / 全 112 篇 43.8%・残 63 篇・全体ロードマップ 13/15-23 セッション完了・残 7〜10 セッション**）

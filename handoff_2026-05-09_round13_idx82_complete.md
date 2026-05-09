# 引き継ぎメモ：候補 B 第 13 ラウンド完走（idx=82・本体直接書込方式・W1 マージ後初）

**日付**：2026-05-09
**フェーズ**：候補 B 第 13 ラウンド（性霊集 残 62 篇継続抽出・本体直接書込）
**起点**：本体 commit `1c673fb`（2026-05-09 Phase 4 W1 マージセッション完走・410 motifs 到達）
**終点**：本ラウンドで本体 motifs.json は m001〜m412 + sg01〜sg06 = 418 motifs に到達
**篇**：idx=82 有る人先師の為に法事を修する願文（第八巻・500 字本文）

---

## (a) 本セッションの位置づけ

### 方針転換：本体直接書込方式採用

W1 マージセッション完了後の引き継ぎメモ（`handoff_2026-05-09_w1_merge_complete.md`）および本体 CLAUDE.md「次の作業」セクションは「次フェーズ＝Phase 2b W2 buddhist-doctrine-workshop 立ち上げ」と記載していたが、これは ★ 誤り ★ であることが本セッション開始時にケンシンより判明：

- 実状：W2 教学系 workshop は別 Cowork セッションで既に並列稼働中（秘蔵宝鑰の motif 抽出を本体に直接書き込む方式で進行中）
- 本セッションは方針転換：本体内で性霊集 残 63 篇の motif 抽出を継続する
- workshop 方式（W1）は実績で確立したが、性霊集 継続については本体直接抽出に戻す判断
- 理由：(a) W1 完走で workshop 方式の知見蓄積完了、(b) 残 63 篇は kaimyo-app 諷誦文素材として直接性が高く本体に逐次反映するほうが利用側参照が早い、(c) 並列 W2 と同時走行で workshop 数を抑える

### W1 マージ未 commit の発見と先行 push

着手前に本体 git status を確認したところ、W1 マージは motifs.json レベルでは反映済（410 件）だが **未 commit 状態**であった（HEAD が `d2d0858` のままで W1 マージ commit が存在しない）。

ケンシン判断で **A 案（先行 push）** を採用：
1. description / schema_history が W1 マージエントリ未追加だったため、`patch_w1_merge_description_history.py` で補完（fix_parens + 検証 6 項目組み込み）
2. commit_message.txt（既存・W1 マージ用 48 行）をそのまま使用
3. commit_push.bat 実行 → W1 マージ commit `1c673fb` 化・push 完了

その後、本セッションの本作業（idx=82 8 件抽出）に着手。

---

## (b) 本セッションの主な成果

### Phase A：W1 マージ description / schema_history 補完

**実装**：`_dev_scripts/patch_w1_merge_description_history.py`（dry-run + 本番適用の二段運用）

**追加内容**：
- `stats.description`：W1 マージ完了状態に更新（410 motifs 達成・含意の射程 第八〜第十区分確定・補注 A/B/C 追加など）
- `stats.schema_history`：W1 マージエントリ追加（version 0.2・date 2026-05-09・session phase4-w1-merge・changes 8 項目・merged_from セクション付き）

**検証 6 項目すべて pass**（補完後）

### Phase B：idx=82 motif 抽出（候補 B 第 13 ラウンド）

**実装**：`_dev_scripts/build_idx82_motifs.py`（dry-run + 本番適用の二段運用）

**抽出 8 件**：

| ID | 字数 | 内容 | 主要タグ |
|---|---|---|---|
| m405 | 75 | 序論譬喩：大海羅睺脚・蘇迷大士手・深海大山 | category:景気導入／典故:阿含経・大智度論・華厳経 |
| m406 | 61 | 二親厳君対比：身粉命殞・四大肉身・一世富貴 | 主題:報恩・孝心 |
| m407 | 83 | 智灯法食・三界四徳・大師恩讃（一句性核心） | 主題:智慧／典故:涅槃経四徳 |
| m408 | 33 | 沐易報難・厳師功（一句性核心） | 主題:師恩・報恩 |
| m409 | 75 | 故禅尼讃美：徳本衆迷・形柔儀業丈夫・除疑根四波縛底 | 故人:禅尼／密教:除疑／典故:律蔵四波羅夷 |
| m410 | 27 | 暁鐘夕鼓・念念為思（一句性核心） | 主題:無常・念念 |
| m411 | 93 | 百年万歳業・業賊四魔・命藤死王・痴愛無明 | 密教:四魔／典故:涅槃経四魔・心地観経 |
| m412 | 53 | 朝烏春雷・長眠子驚・先師貽紹（結句発願） | 含意:全人生／典故:易経雷地豫・礼記月令啓蟄 |

**統計差分**：

| 項目 | 反映前（W1 マージ後）| 反映後（本ラウンド）|
|---|---|---|
| total_motifs | 410 | **418**（+8）|
| kakikudashi_chars_total | 31,985 | **32,485**（+500）|
| gendai_gabun_chars_total | 64,383 | **65,177**（+794）|
| gendaigoyaku_chars_total | 109,748 | **110,884**（+1,136）|
| motifs_with_gendai_gabun | 403 | **411**（+8）|
| 篇別内訳エントリ数 | 50 | **51**（+1）|
| from_idxNN 数 | 49 | **50**（+1：from_idx82=8）|

**検証 6 項目すべて pass**：
1. m-id 連番 m001〜m412 隙間なし・重複なし
2. 半角括弧（motif text）0 件
3. 篇別内訳 51 entries 全 dict 形式
4. stats vs recompute 差分（5 項目）すべてゼロ
5. JSON シリアライズ整合 OK
6. NUL バイト 0 件・schema_version 0.2 維持

### 設計上の新規ポイント

- **(a) 故人軸『禅尼』新規導入候補**：性霊集中で本篇のみ・尼僧女性師への追善願文・補注 B 代筆書状ではない直接弟子発願型。kaimyo-app との整合のため「故人:師」「故人:女性」併用。
- **(b) 含意の射程「全人生」を m412 結句発願に運用**：「兼ねて先師の貽を紹がん」（先師の遺せる教えを継ぐ）の発心継承宣言型。idx=105/106 の辞退型ではない。本体既存の「含意:全人生」軸を用い新規区分は導入せず（補注 A 運用ルール 1 準拠）。
- **(c) 「形柔儀・業丈夫」**：性別を超えた仏道修行の理想像（女性僧讃美の典型表現）を motif 化。kaimyo-app の「主題:徳行」「主題:慈愛」軸と整合。
- **(d) 典故密度十一件**：阿含経／大智度論（羅睺）／華厳経須弥山大士手擲／涅槃経四徳／律蔵四波羅夷／大日経除一切蓋障三昧／涅槃経四魔／大智度論四魔／心地観経／易経雷地豫／礼記月令啓蟄。
- **(e) 4 層構造**：序論譬喩（羅睺脚・大士手・深海大山）→ 二親厳君対比 vs 大師恩 → 沐易報難・厳師功核心 → 故禅尼讃美 → 暁鐘夕鼓念念無常 → 業賊四魔・命藤死王・痴愛無明 → 朝烏春雷・先師貽紹結句発願。

### 副次対応

- 本体への W2 直接書込は **本セッション時点で未発生**（W2 並列セッションは別途進行中だが motifs.json への影響なし）。本セッションの抽出は m405〜m412 で連番衝突なし。
- _dev_references/motifs_index_design.md は modified マークが残ったまま（Windows ⇔ Linux サンドボックス改行コード差分の可能性）。本ラウンドでは触らず保留。
- _dev_scripts/ は git 未追跡で commit に含まれない（patch_w1_merge_description_history.py / build_idx82_motifs.py 等のローカル使い捨てスクリプト群）。将来 .gitignore 整備候補。

---

## (c) 残作業（次セッション以降の選択肢）

### 性霊集 残 62 篇の継続抽出方針

| 群 | 篇数 | 字数 | kaimyo-app 親和性 | 推奨優先度 |
|---|---|---|---|---|
| 第八巻 願文・表白文系（残り） | 7 篇 | 4,987 字 | ★最高（弔辞・追悼系延長） | A：最高優先 |
| 第九巻 高野山関連 | 13 篇 | – | ★高（聖地・空海最晩年） | B：高優先 |
| 第二巻 idx=11 益田池碑銘 | 1 篇 | 1,595 字 | ★高（碑文系・idx=10 と並ぶ規模） | C：高優先 |
| 第十巻 idx=101 綜芸種智院式 | 1 篇 | 2,288 字 | 中（教育機関趣意） | D：中 |
| 第三巻 詩・贈答系 | 5 篇 | – | 中 | E：中 |
| 第四巻 表・啓 | 17 篇 | – | 中（行政書状） | F：中 |
| その他 | 18 篇 | – | – | G：低〜中 |

### 第八巻 残り 7 篇（A 群）の優先順序

1. **idx=78 先師為梵網経講釈表白**（1,368 字）★ 本ラウンド idx=82 と同形（先師追善）・最有力候補
2. **idx=77 仏経講演四恩報徳表白**（1,474 字）四恩報徳・心地観経四恩との接続
3. **idx=79 有人先舅為法事修願文**（297 字）短編・先舅追善
4. **idx=80 和尚皇帝為大般若経転読願文**（411 字）皇帝発願・大般若経
5. **idx=83 公家仁王講修表白**（688 字）国家鎮護・仁王経
6. **idx=84 高野山万灯会願文**（491 字）★ 高野山系・空海最晩年
7. **idx=67 播州和判官攘災願文**（258 字）攘災・地方願文

1 セッション 1〜3 篇で消化想定。残 62 篇 ÷ 平均 2.5 篇 ＝ **約 25 セッション**で完走見通し。

### 並行候補（保留）

- **W2 教学系 workshop**：別 Cowork セッションで並列稼働中・本体に直接書込中。本セッションでは触らない（衝突回避）。完走時は別途マージセッションを起動するか・本体直接書込なら不要。
- **kaimyo-app テーマ駆動辞書実装集約**：故人固有性キーワード→仏教概念タグのハイブリッド辞書。kaimyo-app セッションで進行中。
- **候補 H/I/G**：未取込著作（十住心論・御請来目録 等）／性霊集出典戦略再設計／大日経疏 巻第二〜二十。

---

## (d) 副次発見・要注意事項

### 本セッション開始時の方針転換

- 引き継ぎメモ（`handoff_2026-05-09_w1_merge_complete.md`）と本体 CLAUDE.md「次の作業」セクションが Phase 2b W2 立ち上げを記載していたが、ケンシンの口頭確認で W2 既稼働を判明。引き継ぎメモは記載と実状の齟齬が発生する場合があるので、**新セッション開始時は必ずケンシンの最新意向を確認する**こと。原則 11「ラベルより内容を信頼」に加え、「引き継ぎメモより最新ケンシン指示を信頼」が運用ルールとして確立。

### W1 マージ未 commit 状態の発見

- W1 マージセッションが motifs.json 編集と引き継ぎメモ作成は完了したが、commit_push.bat 実行はケンシン側で未実施だった。本体 git status で確認できる。次マージセッションでも同様の状況が起こりうるので、**新セッション開始時に必ず `git status` と `git log -5` で HEAD と未 commit 変更を確認**。

### W1 マージで commit_message.txt は宣言したが motifs.json には未反映だった項目

- W1 マージ commit_message.txt の line 8「schema_history マージエントリ追加」は宣言と実装が齟齬していた（motifs.json には未追加）。本セッションの patch script で補完済。**今後 commit_message.txt と実装の整合確認をマージセッションの必須項目に加える**。

### 故人軸『禅尼』の新規導入

- 性霊集中で本篇のみ。idx=78「先師為梵網経講釈表白」（次候補）でも先師追善があるため、idx=78 着手時に故人軸を再点検する（先師が男性僧の場合は「禅師」「先師」軸を使う・禅尼は本篇限定）。

### 含意の射程「全人生」の運用例

- 本ラウンドで初めて運用（既存軸として design.md §2 第 100 行に記載済）。発心継承宣言型として位置づけ。idx=78 等の他先師追善篇でも応用可能。

### Linux サンドボックスのファイル操作

- _dev_references/motifs_index_design.md が modified マーク残存。Windows ⇔ Linux サンドボックスの改行コード差分の可能性。次マージセッションで `git checkout _dev_references/motifs_index_design.md` 等で必要なら整理。

---

## (e) 進捗テーブル

### 性霊集抽出進捗（2026-05-09 候補 B 第 13 ラウンド完走時）

| 項目 | 値 |
|---|---|
| 抽出済み篇数 | **50 篇 / 全 112 篇 44.6%** |
| 残篇数 | **62 篇** |
| 抽出済み motif 数 | **412 件**（m001〜m412・sg01〜sg06 を除く本体 motif） |
| 全 motif 数（成句含む）| **418 件** |
| kakikudashi 合計 | **32,485 字** |
| gendai_gabun 合計 | **65,177 字** |
| gendaigoyaku 合計 | **110,884 字** |
| motifs_with_gendai_gabun | **411 件** |
| 篇別内訳エントリ数 | **51 件** |
| stats vs recompute 差分 | **全 5 項目ゼロ達成** |

### 本体 commit log（直近 3 件）

- `1c673fb` 2026-05-09 Phase 4 W1 マージセッション完走（410 motifs 到達）
- `d2d0858` 2026-05-08 Phase 1 完了：本体プロトコル整備（workshop 方式移行）
- `3e261b3` 2026-05-08 候補 B 第 12 ラウンド完走：idx=105 m272〜m281

本セッション完走 push 後の HEAD は **新 commit（候補 B 第 13 ラウンド完走）**。

---

## (f) 関連ファイル群

| ファイル | 内容 |
|---|---|
| `data/indices/motifs.json` | 本体最終形 motif 配列（418 件） |
| `data/kukai/shoryoshu_miyasaka.json` | 性霊集本文真値（112 篇） |
| `_dev_references/motifs_index_design.md` | schema 0.2 仕様書・補注 A/B/C |
| `CLAUDE.md` | 本体ルール・進捗ヘッダ・次の作業 |
| `_dev_scripts/build_idx82_motifs.py` | 本ラウンド build script（先例として保全） |
| `_dev_scripts/patch_w1_merge_description_history.py` | W1 マージ補完 script |
| `commit_message.txt` | 本ラウンド commit メッセージ |
| `handoff_2026-05-09_round13_idx82_complete.md` | 本引き継ぎメモ |
| `handoff_2026-05-09_w1_merge_complete.md` | W1 マージ完了引き継ぎメモ（参照用） |

---

## (g) 新セッション開始用メッセージ（ケンシン貼付テンプレ）

```
=== buddhist-data-api 本体・性霊集 残 62 篇 継続抽出セッション 用貼付メッセージ ===

新セッション開始です。

【最初に読むファイル（順番）】
1. CLAUDE.md（本体ルール・進捗ヘッダ・候補 B 第 13 ラウンド完走状態）
2. handoff_2026-05-09_round13_idx82_complete.md（本ラウンド引き継ぎメモ）
3. _dev_references/motifs_index_design.md（schema 0.2 + 補注 A/B/C）
4. data/indices/motifs.json（本体最終形・418 motifs / m001〜m412 + sg01〜sg06）
   ※並列 W2（別 Cowork セッション）が本体に直接書込中の可能性あり。最新 m-id を必ず実状確認
5. data/kukai/shoryoshu_miyasaka.json（性霊集本文真値・残 62 篇）
6. _dev_scripts/build_idx82_motifs.py（直近 build script 先例）

【git log 確認】
git log --oneline -5（HEAD は本ラウンド完走 commit）

【本セッションの第一ターゲット候補】
- idx=78 先師為梵網経講釈表白（第八巻 1,368 字）★ idx=82 と同形（先師追善）
- idx=77 仏経講演四恩報徳表白（第八巻 1,474 字）
- idx=79 有人先舅為法事修願文（第八巻 297 字・短編）
- idx=84 高野山万灯会願文（第八巻 491 字・空海最晩年）
- またはケンシン指定の他篇

【ID 採番ルール】
- 着手前に必ず data/indices/motifs.json の最新 m-id を確認し、その次から採番する
- 並列 W2 が本体に直接書込中の場合、m-id 衝突を発見したら作業を止めてケンシンに報告

【今セッションでの絶対遵守事項】
- W1 workshop の motifs.json は触らない（commit 9740953 で凍結）
- W2 workshop（別 Cowork セッション）の作業領域も触らない（並列稼働中・衝突回避）
- 本体 motifs.json への追記は build script（Python）経由で行う
  （Edit tool truncation リスク回避・先例 _dev_scripts/build_idx82_motifs.py 参照）
- 検証 6 項目を必ず通す（total / m-id 連番 / 半角括弧 0 / stats=recompute / 篇別内訳 dict / NUL 0）
- bash 経由 git は禁止（commit / push / reset 等の書き込み系）
- ASCII のみで .bat を書く・日本語 commit は commit_message.txt（UTF-8）経由
- 主題タグは普遍仏教概念に限る（固有名詞抽出禁止）
- 含意の射程は本体 10 区分から始め、新規区分は引き継ぎメモで proposal → 次マージセッションで合意
- schema 0.2 維持（タグ値追加のみ）

【作業フロー（1 篇単位の標準サイクル）】
1. shoryoshu_miyasaka.json から該当 idx の kakikudashi / gendaigoyaku を読む
2. motif 候補（5〜13 件）を識別：核心句・対句・典故・廻向・場面導入 等
3. 各 motif に schema 0.2 準拠で kakikudashi（既出）+ text_gendai_gabun（新規執筆・文体規定 7 項目）
   + text_gendaigoyaku（補注付き・既訳ベースで補強）+ tags（標準 9 + 特殊 6 軸）を割当
4. Python build script で motifs.json に追加・stats recompute・篇別内訳 dict 追加
5. 検証 6 項目 pass 確認
6. commit_message.txt 更新 → ケンシン側で commit_push.bat ダブルクリック → push
7. 引き継ぎメモ作成（ASCII 名・handoff_YYYY-MM-DD_round<NN>_idx<NN>_complete.md）

【マイルストーン進捗】
- 性霊集：50/112 篇 44.6% 抽出済み・残 62 篇
- 本体 motifs.json：418 件（m001〜m412 + sg01〜sg06）
- schema_version：0.2（含意の射程 10 区分対応・補注 A/B/C 適用済）

【ロードマップ】
- 本セッション以降：性霊集 残 62 篇を 1 篇ずつ（または短篇複数の組合せで）抽出継続
- 想定：1 セッション 1〜3 篇 × 約 25 セッションで完走
- 並列：W2 教学系 workshop は別 Cowork セッションで進行中・本体に直接書込中

進める前に、最優先タスク（次の対象篇）を確認してください。
=== ここまで ===
```

---

最終更新：2026-05-09（候補 B 第 13 ラウンド完走・本体直接書込方式採用・W1 マージ description/schema_history 補完先行・idx=82 8 件抽出 m405〜m412・性霊集 50 篇 44.6%・残 62 篇）

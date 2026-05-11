# 引き継ぎメモ：retrofit 10 完走〔法華経 諸法実相連動 retrofit〕

**日付**：2026-05-11
**フェーズ**：retrofit 10（retrofit 9 完走に続く第七の retrofit セッション）
**対象**：法華経 諸法実相連動軸の新設。新規 sg-id `sg09`「諸法実相」を追加し、書き下し anchor として既存 `m637`（秘蔵宝鑰 巻の下 第八章 一道無為心 第二節）を採用。連動軸が四系統 → 五系統並立に到達
**ステータス**：完走〔Phase A 軸設計合意・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 J 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 11 候補〔法華経譬喩別軸（寿量品 良医病子／譬喩品 火宅三車／化城喩品 化城／見宝塔品 多宝塔）／華厳経 一即一切／弁顕密二教論 顕密判 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸五系統 anchor 完全整合済〕 等から選択

---

## ⚠️ Phase D 必須チェックリスト履行（retrofit 8 で必須化・retrofit 9 で完全運用化）

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_10:doctrine〕
- [x] motifs_index_design.md に補注 J 追加済〔A-J 全 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 10 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-11_retrofit10_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 半角括弧バランス確認〔追加部分 open=close〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

2026-05-11 の Phase 4 W2 本体マージセッション完走〔commit `6ef4992`〕→ 同日 retrofit 4 完走〔三教指帰 発言者軸新設・commit `7c85b6f`〕→ 同日 retrofit 5 完走〔即身成仏義 sg03 連動・新規軸『連動』導入・commit `2f2b858`〕→ 同日 retrofit 6 完走〔大日経三句法門連動・新規 sg07 + 連動 anchor m713・commit `ce9fe0f`〕→ 同日 retrofit 7 完走〔般若心経 色即是空連動・既存 sg02/m630 を anchor 化〕→ 同日 retrofit 8 完走〔吽字義 阿字本不生連動・新規 sg08 + 既存 m549 を書き下し anchor 化・commit `9fb4d94`〕→ 同日 retrofit 9 完走〔過去 anchor 自己参照タグ補完・m713/m630 へ自己参照タグ付与・commit `006289b`〕に続く第七の retrofit セッションとして実施。

retrofit 10 の主旨は、**連動軸を「法華経 諸法実相」に拡張する第五の連動軸を確立**すること。retrofit 7 で sg02「色即是空」（般若空観）、retrofit 8 で sg08「阿字本不生」（密教空観）が確立されたのに続き、本 retrofit で sg09「諸法実相」（法華空観）を確立。三空観の弁別設計を完成させる。

**本 retrofit の特徴**：

- 新規 sg-id `sg09`「諸法実相」を追加〔出典:法華経 方便品「唯仏与仏乃能究尽諸法実相」〕
- 書き下し anchor として既存 motif `m637`（秘蔵宝鑰 巻の下 第八章 一道無為心 第二節）を採用
- anchor m637 は既に retrofit 6 で `連動:sg07`・`連動:m713`（三句法門）付与済のため、本 retrofit で三軸連動 motif に到達〔retrofit 5 m724 二軸連動の発展形〕
- 強連動 4 motif〔m637・m639・m152・m338〕に `連動:sg09`・`連動:m637` を付与（+8 タグ）

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg09 = 「諸法実相」（簡潔な 4 字成句・retrofit 8 sg08 と同型）
- **判断 2**：書き下し anchor = m637（秘蔵宝鑰 第八住心 第二節・法華経の総合論述）
- **判断 3**：規模 = 強連動のみ 4 件（中程度連動は将来 retrofit に温存）
- **判断 4**（Phase B）：強連動 4 件の選定 = m637(anchor) + m639 + m152 + m338（kakikudashi 本文「実相」直接含有を客観基準として確保）

Phase A〔軸設計合意〕・Phase B〔4 motif 判定〕・Phase C〔本体反映＋補注 J 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕を 1 commit にまとめる方針。

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意

**判定対象 motif 候補**：

法華経関連 motif の分布把握：
- 「典故:法華経」タグ保有 24 件
- 本文に法華経キーワード（諸法実相／法華経／妙法蓮華／三車／化城／良医／薬子／宝塔／多宝／霊鷲／鷲峯／如来寿量／提婆達多／観世音菩薩普門／二乗作仏／唯仏与仏）含有 39 件
- 「諸法実相」kakikudashi 直接含有 motif は 1 件のみ（m725 大日経疏 巻第一）
- 「実相」kakikudashi 含有 motif は 30 件以上（声字実相義・大日経疏・秘蔵宝鑰・性霊集多数）
- 「会三帰一」kakikudashi 含有 motif は m637 のみ
- 「久遠」kakikudashi 含有：m628・m637・m642・m741

**判定 1〜4 のケンシン裁定**で sg09「諸法実相」・anchor m637・規模 4 件・選定 m637+m639+m152+m338 を確定。

### Phase B：4 motif の判定表

| m-id | 出典 | 既存連動タグ | 法華・実相タグ | kakikudashi「実相」直接含有 | 採否 |
|---|---|---|---|---|---|
| m637 | 秘蔵宝鑰 第八住心 第二節 | 連動:sg07・連動:m713 | 主題:法華三昧・典故:法華経 | 「実の如く自身を知る」あり・「諸法実相」直接含有なしだが法華経題材網羅 | **採用（anchor 三軸連動）** |
| m639 | 秘蔵宝鑰 第八住心 第三節 | なし | 主題:法華三昧・典故:法華経 | なし（「法華」「中論」「智度」「法華三昧」含有・天台教判） | **採用（同章続編）** |
| m152 | 性霊集 田小貳願文・第七巻 | なし | 密教:実相 | **「智鏡を懐いて以て実相を照らさん」直接含有** | **採用（性霊集 願文系の代表）** |
| m338 | 性霊集 十喩詩・第十巻 | なし | なし | **「実相如如にして一味の法なり」直接含有** | **採用（性霊集 詩系の代表）** |
| m172 | 性霊集 葛木参軍・第七巻 | なし | 密教:実相 | 「如如の実相に入らしめん」直接含有 | 温存（m152 と類似の願文系・重複） |
| m227 | 性霊集 橘寺願文・第六巻 | なし | 典故:法華経化城喩品 | なし（「如如」のみ・gendaigoyaku 補注で「諸法実相」） | 温存（kakikudashi 本文に未含有・客観基準不明確） |
| m725 | 大日経疏 巻第一 | なし | — | **「諸法実相」直接含有** | 温存（大日経疏 浄菩提心論文脈・法華経中心成句として位置づけ弱） |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 752 | 753 | +1（sg09 新規追加） |
| ファイルサイズ | 2,594,606 bytes | 2,596,989 bytes | +2,383 |
| 連動タグを持つ motif | 29 | 33 | +4（m637 既存に追加・m639/m152/m338 新規連動） |
| famous_phrases | 7（stats 旧値・実数 8） | 9（sg09 追加で実数整合） | +2（旧値の不整合を訂正含む） |
| schema_history 件数 | 67 | 68 | +1 |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 753 vs 753 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔m637/m639/m152/m338〕 | missing=[] ✓ |
| 7 | sg09 配列末尾追加 | ✓ |

### Phase D：補注 J 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 J〔法華経 諸法実相連動の運用記録〕新規追加〔58,120→65,559 bytes・+7,439 bytes〕。anchor 構成表・追加連動タグ値表・retrofit 10 実施結果・設計上の論点 6 項目〔(i) 三軸連動 motif の到達／(ii) 連動軸の五系統並立／(iii) 法華経空観の弁別設計／(iv) kakikudashi 直接含有を客観基準とする選定／(v) 譬喩別連動軸の温存／(vi) schema_history origin タグの定着〕を明文化。補注 A-J 全 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 10 完走エントリを追加〔224,420→229,785 bytes・+5,365 bytes〕。retrofit 4-10 全エントリ intact 確認済。半角括弧バランス維持。NUL バイト 0 件確認。
- `commit_message.txt` を retrofit 10 用に完全書き換え〔5,998 bytes・NUL 0・冒頭行整合確認済〕。冒頭行を「retrofit 10 完走：法華経 諸法実相連動 retrofit〔新規 sg09「諸法実相」+ 既存 m637 を書き下し anchor 化・連動軸五系統並立に到達〕」として、retrofit 8 で必須化された Phase D 必須チェックリストに完全準拠。retrofit 9 §(d-11) で警告された Write tool 上書き NUL バイト混入事象を回避するため、Python `write_bytes` 経由で書き込み。

### 設計上の新規ポイント

#### (i) 三軸連動 motif の到達

anchor m637 は既に retrofit 6 で `連動:sg07`・`連動:m713`（三句法門）が付与済であり、本 retrofit で `連動:sg09`・`連動:m637`（諸法実相）が追加されて三軸連動状態（三句法門 + 諸法実相 + 自己参照）に到達。retrofit 5 m724（即身成仏 sg03 + 三句法門 sg07 の二軸連動）を発展させた前例。秘蔵宝鑰 第八住心 第二節 m637 は、空海の住心論的視座で「法華経が密教の前段教（初法明道）として位置づけられる」ことを示し、大日経 三句法門と法華経 諸法実相が地続きの位置に重なる教学的根拠を反映する。

#### (ii) 連動軸の五系統並立

本 retrofit で連動軸は以下の五系統が並立：

| 連動軸 | 成句 anchor | 書き下し anchor | 自己参照タグ | 確立 retrofit |
|---|---|---|---|---|
| 即身成仏 | sg03 | m533 | 連動:sg03・連動:m533 | retrofit 5（先例として既付与） |
| 三句法門 | sg07 | m713 | 連動:sg07・連動:m713 | retrofit 6 → retrofit 9 で補完 |
| 色即是空 | sg02 | m630 | 連動:sg02・連動:m630 | retrofit 7 → retrofit 9 で補完 |
| 阿字本不生 | sg08 | m549 | 連動:sg08・連動:m549 | retrofit 8（先例適用） |
| **諸法実相** | **sg09** | **m637** | **連動:sg09・連動:m637** | **retrofit 10（本 retrofit）** |

kaimyo-app は「即身成仏」「菩薩道の三句」「般若空観」「密教空観」「法華空観」の五つの教学テーマで素材プールを切替可能。

#### (iii) 法華経空観の弁別設計

法華経 諸法実相（sg09/m637）・般若心経 色即是空（sg02/m630）・吽字義 阿字本不生（sg08/m549）の三空観で kaimyo-app の検索意図を明確に弁別可能：

- 「法華経 諸法実相」検索 → m637/m639/m152/m338（本 retrofit 4 件）
- 「般若心経 色即是空」検索 → m630 + retrofit 7 の 6 件（計 7 件）
- 「阿字本不生」検索 → m549 + retrofit 8 の 10 件（計 11 件）

それぞれ独立した素材プールとして取得可能。

#### (iv) kakikudashi 直接含有を客観基準とする選定

本 retrofit では強連動の客観基準として「kakikudashi 本文に『実相』直接含有」を採用。m152（智鏡懐実相照）・m338（実相如如一味）・m637（実の如く自身を知る + 法華経題材網羅）・m639（法華・中論・智度 + 法華三昧）で基準を満たす。m227（諸法実相が gendaigoyaku 補注のみ・kakikudashi 本文に未含有）・m725（大日経疏の浄菩提心論文脈）は基準不明確として温存。

#### (v) 譬喩別連動軸の温存

法華経関連 motif で本 retrofit ではスコープ外とした以下は、各譬喩別軸として将来 retrofit 11 以降で個別の連動軸を設けることが可能：

- 寿量品 良医病子（m70/m44）
- 譬喩品 火宅三車（m209/m460）
- 化城喩品 化城（m227/m486/m489）
- 見宝塔品 多宝塔（m222/m262/m424）

「諸法実相」軸が法華経の最も抽象的・中心的な空観を捉えるのに対し、譬喩別軸は法華経の具体的法話素材を整理する補完軸として機能する設計。

#### (vi) Phase D 必須チェックリストの完全運用化（retrofit 10 で 2 回目の完走）

retrofit 9 が Phase D 必須チェックリストに完全準拠する初の retrofit となり、本 retrofit 10 は 2 回目の完全準拠 retrofit として位置づく。特に commit_message.txt の冒頭行整合確認〔「retrofit 10 完走：法華経 諸法実相連動 retrofit...」〕が、retrofit 7 §(d-9) の不整合（commit message が retrofit 6 のまま push された問題）を再発させない運用基盤として継続機能。

#### (vii) Write tool truncate 回避の継続実証＋NUL 混入再発と修復

retrofit 5-9 で確立した「長文編集は Python script による in-memory 編集 + write back」方針を本 retrofit でも継続適用〔motifs.json・motifs_index_design.md・CLAUDE.md・commit_message.txt すべて Python script 経由〕。ただし本セッションで Write tool による Python script 自体の作成時に **2 回 truncate 事象が再発生**（retrofit10_shoho_jisso.py と add_chunote_j_retrofit10.py）、それぞれ Python の `path.write_bytes()` で末尾を補完して修復。Edit tool は使用せず。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 11〔法華経譬喩別軸〕

連動軸の譬喩別細分化：

- 寿量品 良医病子（m70/m44）を anchor 候補
- 譬喩品 火宅三車（m209/m460）を anchor 候補
- 化城喩品 化城（m227/m486/m489）を anchor 候補
- 見宝塔品 多宝塔（m222/m262/m424）を anchor 候補
- 規模 5-10 motif 前後・小〜中規模

### 選択肢 B：retrofit 11 候補〔華厳経 一即一切連動／弁顕密二教論 顕密判 等〕

- 華厳経 一即一切：「一即一切、一切即一」を anchor に、空海著作中の華厳経関連 motif を紐づけ
- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸五系統 anchor 完全整合済〕

本 retrofit で連動軸五系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg09」「連動:m637」を持つ 4 motif → 諸法実相連動素材プール（法華空観）
- 「連動:sg08」「連動:m549」を持つ 11 motif → 阿字本不生連動素材プール（密教空観）
- 「連動:sg02」「連動:m630」を持つ 7 motif → 色即是空連動素材プール（般若空観）
- 「連動:sg03」「連動:m533」を持つ 4 motif → 即身成仏連動素材プール
- 「連動:sg07」「連動:m713」を持つ 8 motif → 三句法門連動素材プール
- 二軸・三軸横断 motif〔m724（即身成仏↔三句法門）、m637（三句法門↔諸法実相）〕の素材選択ロジック
- 三空観の弁別検索〔法華系 vs 般若系 vs 密教系〕の実装
- 三教指帰の発言者軸〔retrofit 4〕と組み合わせた空海主体性の明確化

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) 本セッション開始時の git 状態異常（retrofit 9 §(d-1) と同型再発）

セッション開始直後の `git status` で以下の異常が発見された：

1. **誤ステージ済の削除**：package.json/render.yaml/start.bat/tsconfig.json/vercel.json/引き継ぎメモ_2026-05-06_候補B第4ラウンド継続_idx48東太上故中務卿親王檀像願文.md/outputs/motifs_index_design_backup_pre_retrofit{6,7,8,9}.md
2. **異常 rename**：outputs/CLAUDE_md_backup_pre_retrofit_workflow.md → outputs/CLAUDE_md_backup_pre_retrofit_（拡張子なしファイル名への rename）
3. **.git/index.lock 残存**（bash mount 側で検出・retrofit 9 同型）

retrofit 9 §(d-1) で記述された事象が完全に再発。原因は不明だが、bash mount の git 操作とのインタラクション（fsmonitor 等の背景プロセス）の影響と推定される。

### (d-2) git 状態整理プロセスの確立（retrofit 9 同型を踏襲＋拡張）

(d-1) を解消するため、以下の手順を実施：

1. `outputs/cleanup_git_state_pre_retrofit10.bat` + `outputs/cleanup_git_state_pre_retrofit10.py` を新規作成〔ASCII のみの bat + UTF-8 Python helper の二段構成・retrofit 9 同型〕
2. **新機能 Step 2-5**：staged 削除取消後の unstaged deletions（working dir に欠落）を `git ls-files --deleted` で列挙し、HEAD に存在するものを `git checkout HEAD -- <file>` で working dir に復元（start.bat・引き継ぎメモ_2026-05-06_... が自動復元）
3. ケンシン側で bat ダブルクリック実行：`.git/index.lock` を `index.lock.bak4` に退避 → Python helper で `git diff --cached --diff-filter=D/R --name-only` を動的取得して全件 unstage → 異常 rename 空ファイル掃除 → HEAD 既存ファイル復元 → 結果の git status 表示
4. Windows cmd.exe 表示でクリーン状態確認後に retrofit 10 着手

### (d-3) bash mount git status と Windows git status の乖離（retrofit 9 §(d-8) の継続）

cleanup 実行後、Windows cmd.exe で `nothing added to commit` を確認したが、bash mount から `git status` を実行すると staged deletions が再表示された。これは CLAUDE.md「Windows ⇔ サンドボックスのファイルシステム同期タイミング」事象。

retrofit 9 §(d-8) の前例（「commit_push.bat の Step 4.5 SAFETY CHECK は発動しない見込み」が実際に発動せず正常 commit された）に従い、**Windows 側のクリーン状態を真実とみなして retrofit 10 作業を進行**。最終 commit 時に commit_push.bat の Step 4.5 SAFETY CHECK が万一発動した場合は中止して再 cleanup する方針。

### (d-4) retrofit 9 commit に outputs/ 配下ファイル群が含まれていなかった事象の発見

git show HEAD で確認した結果、retrofit 9 commit (006289b) は motifs.json / CLAUDE.md / motifs_index_design.md / commit_message.txt / handoff_2026-05-11_retrofit9_complete.md のみを含み、**retrofit 9 で作成した outputs/ 配下の build script 5 件・backup 3 件は commit に含まれていなかった**。commit message 内では「outputs/retrofit9_anchor_self_reference.py」「outputs/motifs_backup_pre_retrofit9.json」等を記載しているが、実際の commit には未含有。これは commit_push.bat の固定 stage 対象に outputs/ が含まれていない可能性。

本 retrofit 10 では outputs/ 配下の新規ファイルも commit に含めるよう、commit_push.bat 実行前に明示的に `git add outputs/cleanup_git_state_pre_retrofit10.bat outputs/cleanup_git_state_pre_retrofit10.py outputs/retrofit10_shoho_jisso.py outputs/add_chunote_j_retrofit10.py outputs/update_claude_md_retrofit10.py outputs/motifs_backup_pre_retrofit10.json outputs/motifs_index_design_backup_pre_retrofit10.md outputs/CLAUDE_md_backup_pre_retrofit10.md` 等の追加 staging を検討する必要がある。または、これらを別途のスタンドアロン .bat で push する運用も可能。

### (d-5) Write tool truncate 事象の 2 回再発生と修復

本 retrofit Phase D で **Write tool truncate 事象が 2 回再発生**：

1. **retrofit10_shoho_jisso.py**：末尾 `if` のみで止まり、`nul_after > 0:` 以降が消失。bash heredoc + Python `write_bytes` で末尾を補完して修復
2. **add_chunote_j_retrofit10.py**：末尾 `    p` で止まり、Step 8 以降が消失。同様の方法で修復

retrofit 5-9 では発生していなかったが、本 retrofit で 2 回連続再発。原因は Write tool 内部のバッファリング処理と推定される。今後は Python script 作成時も `path.write_bytes()` 直接書き込み方式を優先することが推奨される。

### (d-6) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9 §(d-11) で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を採用。bash heredoc で content を構築して Python `write_bytes` する手順。最終検証で NUL 0 件確認。

### (d-7) retrofit 10 後の motifs.json サイズ

retrofit 10 で +2,383 bytes〔2,594,606 → 2,596,989 bytes〕。retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 7 連続で +1,000〜2,700 bytes 規模の retrofit。新規 sg09 motif の description が長めのため retrofit 8 の +2,609 に近い。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-8) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg09 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg09 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg08 と同方針）。gendai_gabun_chars_total も 154,931 維持。

### (d-9) famous_phrases stats 値の不整合訂正

retrofit 前の stats.famous_phrases は 7 だったが、実際の「成句:famous」タグ保有 motif は sg01-sg08 の 8 件だった。本 retrofit で sg09 追加に伴い recompute して famous_phrases=9（sg01-sg09 の 9 件）に整合化。これは過去 retrofit で sg08 追加時に stats が更新されなかったことに起因する。

### (d-10) ファイル truncate の予防継続

本 retrofit でも Python script による in-memory 編集 + write back 方針を継続。motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt・handoff いずれも書き込み後の NUL バイト検証〔0 件確認〕とサイズ差確認、半角括弧バランス検証〔全角括弧バランス・追加部分のみで検証〕を実施。

### (d-11) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 5 件・バックアップ 3 件・引き継ぎメモ 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。ただし、bash mount 側で staged deletions が表示されている状態と Windows 側のクリーン状態の乖離（d-3）の影響で、commit_push.bat 実行時に予期しない挙動を示す可能性がある。要 ケンシン実行時の確認。

### (d-12) Phase D 必須チェックリストの retrofit 10 で完全運用化（2 回目）

retrofit 9 §(d-9) で初の完全準拠を達成、本 retrofit 10 で 2 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 10 完走：法華経 諸法実相連動 retrofit〔新規 sg09「諸法実相」+ 既存 m637 を書き下し anchor 化・連動軸五系統並立に到達〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔753 件・m1-m744 + sg01-sg09・2,596,989 bytes〕
- 本 retrofit build script：`outputs/retrofit10_shoho_jisso.py`〔dry-run + 本番適用の二段運用〕
- 補注 J 追加 script：`outputs/add_chunote_j_retrofit10.py`
- CLAUDE.md 更新 script：`outputs/update_claude_md_retrofit10.py`
- セッション着手前 git 整理：`outputs/cleanup_git_state_pre_retrofit10.bat`〔ASCII のみ〕＋`outputs/cleanup_git_state_pre_retrofit10.py`〔UTF-8 helper・Step 2-5 で HEAD 既存ファイル復元機能追加〕
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit10.json`〔retrofit 前 motifs.json・2,594,606 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit10.md`〔retrofit 前 motifs_index_design.md・58,120 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit10.md`〔retrofit 前 CLAUDE.md・224,420 bytes〕
- 前 retrofit handoff：`handoff_2026-05-11_retrofit9_complete.md`〔過去 anchor 自己参照タグ補完〕
- 前々 retrofit handoff：`handoff_2026-05-11_retrofit8_complete.md`〔吽字義 阿字本不生連動〕
- 補注 J 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 10 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-9 完走 → 同日 retrofit 10 完走〔法華経 諸法実相連動・新規 sg09 + 既存 m637 を書き下し anchor 化・連動軸五系統並立に到達〕。本体 motifs.json は 753 件・2,596,989 bytes・schema_history 68 件。motifs_index_design.md §2 に補注 J 追加〔補注 A-J 全 intact・65,559 bytes〕。CLAUDE.md は 229,785 bytes〔retrofit 4-10 全エントリ intact〕。連動軸五系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637〕の anchor 自己参照タグ運用が完全整合に到達。三空観の弁別設計〔法華・般若・密教〕も成立。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit10_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit9_complete.md`〔retrofit 9 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E/F/G/H/I/J 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・753 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 10 commit です。

【本セッションの選択肢】
(A) retrofit 11 候補〔法華経譬喩別軸：寿量品 良医病子／譬喩品 火宅三車／化城喩品 化城／見宝塔品 多宝塔〕
(B) retrofit 11 候補〔華厳経 一即一切／弁顕密二教論 顕密判 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸五系統 anchor 完全整合済の素材プール活用
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit tool truncate 事象回避・本 retrofit でも 2 回再発・継続実証〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 本体 motifs.json は 2,596,989 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目・retrofit 7 §(d-9) 再発防止策〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作・retrofit 9 §(d-3) で再確認〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須〔Write tool 上書き既知事象・retrofit 9 §(d-11)・retrofit 10 §(d-5) で複数回検出〕。可能な限り Python script の `path.write_bytes(data)` を使用

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-11〔retrofit 10 完走・法華経 諸法実相連動 retrofit。新規 sg-id sg09「諸法実相」を追加〔出典:法華経 方便品「唯仏与仏乃能究尽諸法実相」〕、書き下し anchor として既存 m637（秘蔵宝鑰 巻の下 第八章 一道無為心 第二節）を採用。強連動 4 motif〔m637(anchor 三軸連動)/m639/m152/m338〕に `連動:sg09`・`連動:m637` を付与（+8 タグ）。total_motifs 752→753（+1 新規 sg09）。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,596,989 bytes〔+2,383〕・schema_history 68 件〔+1・origin: retrofit_10:doctrine〕・補注 J 追加〔motifs_index_design.md §2・58,120→65,559 bytes・+7,439〕・CLAUDE.md 更新完了〔224,420→229,785 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸五系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637〕に到達——kaimyo-app は法華空観・般若空観・密教空観の三空観で検索意図弁別可能。本セッション開始時に bash mount 経由 git status の異常〔retrofit 9 同型再発〕を発見し、cleanup_git_state_pre_retrofit10.bat + cleanup_git_state_pre_retrofit10.py（HEAD 既存ファイル復元機能追加版）で整理してから本 retrofit 10 着手。Phase D 必須チェックリストに完全準拠する第二の retrofit〕

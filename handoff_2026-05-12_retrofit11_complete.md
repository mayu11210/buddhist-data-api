# 引き継ぎメモ：retrofit 11 完走〔法華経 譬喩品 火宅三車連動 retrofit〕

**日付**：2026-05-12
**フェーズ**：retrofit 11（retrofit 10 完走に続く第八の retrofit セッション）
**対象**：法華経 譬喩品 火宅三車連動軸の新設。新規 sg-id `sg10`「火宅三車」を追加し、書き下し anchor として **二重体制** を初導入：既存 `m209`（性霊集 第八巻 願文系 anchor）と既存 `m636`（秘蔵宝鑰 巻の下 第八章 教学系 anchor）の二つを並立 anchor として指定。連動軸が五系統 → 六系統並立に到達。法華経内部で「諸法実相（抽象的核心）」と「火宅三車（具体的譬喩）」の二段構成に到達。
**ステータス**：完走〔Phase A 軸設計合意〔前セッション中断 → 本セッション再開〕・Phase B 4 motif 判定・Phase C 本体反映＋整合性検証 7 項目全 pass・Phase D 補注 K 追加＋CLAUDE.md 更新＋commit_message.txt 更新＋本 handoff 作成〕
**次フェーズ**：retrofit 12 候補〔法華経譬喩別軸（寿量品 良医病子／化城喩品 化城／見宝塔品 多宝塔）／華厳経 一即一切／弁顕密二教論 顕密判 等〕／W1 buddhist-shoryoshu-workshop 継続抽出／kaimyo-app 教学系素材活用〔連動軸六系統 anchor 完全整合済〕等から選択

---

## ⚠️ Phase D 必須チェックリスト履行

- [x] motifs.json 反映完了〔7 項目整合性検証 全 pass〕
- [x] schema_history 追記済〔origin: retrofit_11:doctrine〕
- [x] motifs_index_design.md に補注 K 追加済〔A-K 全 intact〕
- [x] 本体 CLAUDE.md 更新済〔タイトル行・最終更新行〕
- [x] **commit_message.txt 書き換え済〔retrofit 11 用・冒頭行整合確認済〕**
- [x] handoff_2026-05-12_retrofit11_complete.md 作成済（本ファイル）
- [x] 全ファイル NUL バイト 0 件確認
- [x] 半角括弧バランス確認〔追加部分 open=close〕
- [x] サイズ差分が想定範囲内

---

## (a) 本セッションの位置づけ

retrofit 10 完走〔法華経 諸法実相連動・新規 sg09 + 既存 m637 を書き下し anchor 化〕に続く第八の retrofit セッション。

retrofit 10 §(c) 選択肢 A〔retrofit 11 候補：法華経譬喩別軸〕に着手。2026-05-11 にケンシン裁定で「譬喩品 火宅三車軸」を選定し Phase A 設計合意の途中（anchor 二重体制 m209/m636、中心成句「火宅三車」、規模 4 件まで確定）でセッション切替。HEAD は retrofit 10 commit `9006ba1` のまま。本セッション（2026-05-12）で Phase A の最終決定〔強連動 2 件 = m311 + m615、案 A = 全 motif に二重 anchor 明示〕からの再開・Phase B・C・D を 1 commit にまとめて完走する方針で進行。

**本 retrofit の特徴**：

- 新規 sg-id `sg10`「火宅三車」を追加〔出典:法華経 譬喩品「初説三乗引導衆生、然後但以大乗而度脱之」〕
- 書き下し anchor の **二重体制** を初導入：m209（願文系 anchor）+ m636（教学系 anchor）
- 強連動 4 motif に「連動:sg10」「連動:m209」「連動:m636」を付与（+12 タグ・案 A 採用＝全 motif に二重 anchor 明示）
- 法華経内部で抽象的核心（sg09 諸法実相）と具体的譬喩（sg10 火宅三車）の二段構成に到達
- 連動軸六系統並立に到達

ケンシン裁定で以下を採用：

- **判断 1**：中心成句 sg10 = 「火宅三車」（簡潔な 4 字成句・retrofit 8 sg08「阿字本不生」・retrofit 10 sg09「諸法実相」と同型）
- **判断 2**：書き下し anchor = m209（願文系）+ m636（教学系）の二重体制
- **判断 3**：規模 = 強連動 4 件
- **判断 4**（本セッション）：強連動 2 件の選定 = m311（性霊集 詩・三界火宅）+ m615（秘蔵宝鑰 第四住心 唯蘊無我心・羊車）
- **判断 5**（本セッション）：二重 anchor タグ運用 = 案 A〔全 motif に二重 anchor 明示〕

---

## (b) 本セッションの主な成果

### Phase A：軸設計合意（前セッション中断 → 本セッションで最終確定）

**判定対象 motif 候補**：

法華経 火宅三車関連 motif の分布把握（retrofit11_phaseA_candidates.txt より）：
- 典故:法華経 タグ保有 25 件
- 火宅キーワード本文含有 24 件
- 譬喩品系タグ保有 2 件（m209・m243）

候補 motif の整理：
- m209：性霊集 第八巻 有る人の亡親の為に法事を修する願文・火宅/三車/白牛車/牛車/一仏乗 5 keyword 直接含有・願文系 anchor 候補
- m636：秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱・界外の一車・天台教判全体構造の総合論述・教学系 anchor 候補
- m311：性霊集 第一巻 山に入る興 雑言・三界火宅直接含有・詩系
- m489：性霊集 第八巻 攘災願文・7 keywords 全部含有
- m615：秘蔵宝鑰 巻の中 第四章 唯蘊無我心 第一節・羊車直接含有・教学系第二段
- m622：秘蔵宝鑰 巻の中 第五章 抜業因種心・鹿車直接含有・教学系第三段

本セッション開始時の判断（AskUserQuestion でケンシン確定）：

- 強連動 2 件 = m311 + m615（推奨案・願文/詩/教学第一段/教学第二段の 4 系統カバー）
- 二重 anchor タグ運用 = 案 A（全 motif に「連動:sg10」「連動:m209」「連動:m636」3 タグ全付与）

### Phase B：4 motif の判定表

| m-id | 出典 | 既存連動タグ | 既存関連タグ（主要） | kakikudashi 火宅 keyword | 系統 | 役割 | 採否 |
|---|---|---|---|---|---|---|---|
| m209 | 性霊集 第八巻 有る人の亡親の為に法事を修する願文 | なし | 主題:火宅宝車・典故:法華経譬喩品・場面:火宅宝車 | 火宅・三車・白牛車・牛車・一仏乗（5 keyword 直接含有） | 願文系 | **anchor（願文系）** | **採用** |
| m636 | 秘蔵宝鑰 巻の下 第八章 一道無為心 第一節 大綱 | なし | 主題:教判・主題:一道無為・主題:住心 | 「界外の一車は大小入らず」（一車・大小含意網羅） | 教学系 | **anchor（教学系）** | **採用** |
| m311 | 性霊集 第一巻 山に入る興 雑言 | なし | 典故:法華経・主題:発心・遁世 | 三界火宅（直接含有） | 詩系 | 強連動 | **採用** |
| m615 | 秘蔵宝鑰 巻の中 第四章 唯蘊無我心 第一節 | なし | 主題:声聞乗・主題:四諦・主題:住心 | 「大覚世尊此の羊車を説いて」羊車（直接含有） | 教学系第二段 | 強連動 | **採用** |
| m489 | 性霊集 第八巻 攘災願文 | なし | — | 7 keywords 全部含有（火宅/三車/羊車/鹿車/白牛車/牛車/一仏乗） | 願文系（追加） | 温存 | スコープ外 |
| m622 | 秘蔵宝鑰 巻の中 第五章 抜業因種心 | なし | — | 鹿車「縁覚の鹿車は言説なし」 | 教学系第三段 | 温存 | スコープ外 |
| m460 | 性霊集 第八巻 公家の仁王講を修せらるる表白 | なし | 典故:法華経化城喩品 | （火宅 keywords 0 件・化城喩品系） | — | 温存（化城喩品別軸候補） | スコープ外 |

### Phase C：本体 motifs.json 反映

| 項目 | retrofit 前 | retrofit 後 | 差分 |
|---|---|---|---|
| total_motifs | 753 | 754 | +1（sg10 新規追加） |
| ファイルサイズ | 2,596,989 bytes | 2,600,303 bytes | +3,314 |
| 連動タグを持つ motif | 33 | 37 | +4（m209/m636/m311/m615 新規連動） |
| famous_phrases | 9 | 10 | +1（sg10 追加で recompute） |
| schema_history 件数 | 68 | 69 | +1 |

**整合性検証 7 項目〔全 pass〕**：

| # | 項目 | 結果 |
|---|---|---|
| 1 | total_motifs〔stats vs 配列〕 | 754 vs 754 ✓ |
| 2 | m-id 連番性〔m1-m744〕 | missing=[], extra=[] ✓ |
| 3 | NUL バイト 0 件 | ✓ |
| 4 | schema_version 0.2 維持 | ✓ |
| 5 | 必須フィールド完全性 | incomplete=[] ✓ |
| 6 | 連動タグ付与〔m209/m636/m311/m615 + 各 3 タグ〕 | missing=[] ✓ |
| 7 | sg10 配列追加〔sg09 直後〕 | ✓ |

### Phase D：補注 K 追加・CLAUDE.md 更新・commit_message.txt 更新

- `_dev_references/motifs_index_design.md` §2 に補注 K〔法華経 譬喩品 火宅三車連動の運用〕新規追加〔65,559→74,761 bytes・+9,202 bytes〕。anchor 構成表（二重 anchor 体制を初導入）・追加連動タグ値表・二重 anchor タグ運用ルール（案 A 採用）・retrofit 11 実施結果・設計上の論点 6 項目〔(i) 二重 anchor 体制の初導入／(ii) 連動軸六系統並立に到達／(iii) 法華経内部の二段構成／(iv) kakikudashi 直接含有を客観基準とする継続／(v) 譬喩別軸の今後の展開／(vi) schema_history origin タグの定着〕を明文化。補注 A-K 全 intact 確認済。
- 本体 CLAUDE.md：タイトル行と最終更新行の両方に retrofit 11 完走エントリを追加〔229,785→235,797 bytes・+6,012 bytes〕。retrofit 4-11 全エントリ intact 確認済。半角括弧バランス維持。NUL バイト 0 件確認。
- `commit_message.txt` を retrofit 11 用に完全書き換え〔7,330 bytes・NUL 0・冒頭行整合確認済〕。冒頭行を「retrofit 11 完走：法華経 譬喩品 火宅三車連動 retrofit〔新規 sg10「火宅三車」+ 既存 m209/m636 を書き下し anchor 二重体制で採用・連動軸六系統並立に到達〕」として、Phase D 必須チェックリストに完全準拠。Python `write_bytes` 直接書き込み方式で作成（retrofit 9 §(d-11) Write tool truncate 事象回避策の継続）。

### 設計上の新規ポイント

#### (i) 二重 anchor 体制の初導入

retrofit 5-10 は単一書き下し anchor 1 件の運用だったが、本 retrofit 11 で **二重 anchor 体制** を初導入。法華経 火宅三車の典籍系統が「願文系（性霊集 法事願文の典故引用）」と「教学系（秘蔵宝鑰 教判論の説相）」に明確に二分されるため、いずれか一方では包摂できない判断から二重化を採用。`m209` は願文系の代表（火宅宝車・浄土妙門の対句で法華・薬師の二経対照）、`m636` は教学系の代表（一車・大小の判教構造と天台一乗教学）。

**案 A 採用ルール**：すべての強連動 motif に「連動:sg10」「連動:m209」「連動:m636」の 3 タグ全てを付与。kaimyo-app 検索で「連動:m209」「連動:m636」のいずれの anchor 検索でも 4 件全件取得可能。検索ロジック単純化が利点。

#### (ii) 連動軸六系統並立に到達

本 retrofit で連動軸は以下の六系統が並立：

| 連動軸 | 成句 anchor | 書き下し anchor | 自己参照タグ | 確立 retrofit |
|---|---|---|---|---|
| 即身成仏 | sg03 | m533 | 連動:sg03・連動:m533 | retrofit 5 |
| 三句法門 | sg07 | m713 | 連動:sg07・連動:m713 | retrofit 6 → retrofit 9 で補完 |
| 色即是空 | sg02 | m630 | 連動:sg02・連動:m630 | retrofit 7 → retrofit 9 で補完 |
| 阿字本不生 | sg08 | m549 | 連動:sg08・連動:m549 | retrofit 8 |
| 諸法実相 | sg09 | m637 | 連動:sg09・連動:m637 | retrofit 10 |
| **火宅三車** | **sg10** | **m209 + m636（二重）** | **連動:sg10・連動:m209・連動:m636** | **retrofit 11（本 retrofit）** |

kaimyo-app は「即身成仏」「菩薩道の三句」「般若空観」「密教空観」「法華空観（諸法実相）」「法華譬喩（火宅三車）」の六つの教学テーマで素材プールを切替可能。

#### (iii) 法華経内部の二段構成

retrofit 10 sg09「諸法実相」（抽象的核心）と retrofit 11 sg10「火宅三車」（具体的譬喩）の二段構成に到達。法華経の最も抽象的・中心的な空観と最も具体的・象徴的な譬喩素材が、別個の連動軸として明示的に弁別可能となる。今後の譬喩別軸展開（化城喩・良医喩・多宝塔等）への基盤を整備。

#### (iv) 4 系統カバー設計

4 motif の選定は以下の 4 系統を一括包摂する設計：

- 願文系：m209（性霊集 第八巻 有る人の亡親の為に法事を修する願文・anchor）
- 詩系：m311（性霊集 第一巻 山に入る興 雑言）
- 教学系第一段：m636（秘蔵宝鑰 第八住心 一道無為心・anchor）
- 教学系第二段：m615（秘蔵宝鑰 第四住心 唯蘊無我心）

kaimyo-app の素材検索で、戒名・諷誦文・引導文・法話のジャンル別に対応可能な多様性を確保。

#### (v) kakikudashi 直接含有を客観基準とする継続

本 retrofit でも強連動の客観基準として「kakikudashi 本文に火宅三車関連 keyword 直接含有」を採用：

- m209：火宅・三車・白牛車・牛車・一仏乗（5 keyword 直接含有）
- m636：「界外の一車は大小入らず」（一車・三車・大小の含意網羅・教判全体構造）
- m311：三界火宅（直接含有）
- m615：「大覚世尊此の羊車を説いて」（羊車直接含有）

retrofit 10 補注 J §「kakikudashi 直接含有を客観基準とする選定」の方針を継続適用。

#### (vi) 譬喩別軸の今後の展開

法華経の譬喩素材は他に「寿量品 良医病子（m70/m44）」「化城喩品 化城（m227/m486/m489）」「見宝塔品 多宝塔（m222/m262/m424）」等が存在。本 retrofit 11 sg10「火宅三車」を最初の譬喩別軸として確立した上で、retrofit 12 以降で順次これらの譬喩別軸を追加可能。各譬喩別軸は本 retrofit の単一/二重 anchor 体制の選択を運用基盤として継承する。

#### (vii) Phase D 必須チェックリストの完全運用化（retrofit 11 で 3 回目の完走）

retrofit 9 が初の完全準拠、retrofit 10 が 2 回目、本 retrofit 11 で 3 回目の完全準拠 retrofit として位置づく。特に commit_message.txt の冒頭行整合確認〔「retrofit 11 完走：法華経 譬喩品 火宅三車連動 retrofit...」〕が、retrofit 7 §(d-9) の不整合（commit message が retrofit 6 のまま push された問題）を再発させない運用基盤として継続機能。

---

## (c) 残作業〔次セッション以降の選択肢〕

### 選択肢 A：retrofit 12〔法華経譬喩別軸〕

連動軸の譬喩別細分化（本 retrofit の延長）：

- 寿量品 良医病子（m70/m44）を anchor 候補
- 化城喩品 化城（m227/m486/m489）を anchor 候補
- 見宝塔品 多宝塔（m222/m262/m424）を anchor 候補
- 規模 5-10 motif 前後・小〜中規模

### 選択肢 B：retrofit 12 候補〔華厳経 一即一切連動／弁顕密二教論 顕密判 等〕

- 華厳経 一即一切：「一即一切、一切即一」を anchor に、空海著作中の華厳経関連 motif を紐づけ
- 弁顕密二教論 顕密判：「顕密二教」を anchor に、教判系 motif を紐づけ

### 選択肢 C：W1 buddhist-shoryoshu-workshop 継続抽出

性霊集 残 55 篇から motif 抽出を W1 workshop で並列進行。本体側で第 19 ラウンドまで完走済〔482→496 motifs〕。W1 完走時に第 2 回本体マージセッションを実施。

### 選択肢 D：kaimyo-app 教学系素材活用〔連動軸六系統 anchor 完全整合済〕

本 retrofit で連動軸六系統の anchor 自己参照タグ運用が完全整合に到達したため、kaimyo-app 側で：

- 「連動:sg10」を持つ 4 motif → 火宅三車連動素材プール（法華経譬喩）
- 「連動:m209」「連動:m636」のいずれでも 4 motif 取得可能（案 A 二重 anchor 設計）
- 二重 anchor 体制と既存単一 anchor 体制の同型運用（kaimyo-app 検索ロジックは単一 anchor と同等）
- 法華経内部の二段構成検索：「諸法実相（抽象的）」 vs 「火宅三車（具体的）」の弁別
- 譬喩別軸の追加準備〔retrofit 12 以降の化城喩・良医喩・多宝塔等への拡張〕

### 選択肢 E：W2 repo 凍結手続〔workshop_protocol §10(5)〕

buddhist-doctrine-workshop の archive 化 or 読み取り専用化。

---

## (d) 副次発見・要注意事項

### (d-1) Phase A の前セッション持ち越し（再開セッション）

retrofit 11 Phase A は前セッション（2026-05-11）で着手し、anchor 二重体制（m209/m636）と中心成句「火宅三車」と規模 4 件まで確定したが、強連動 2 件の最終選定と二重 anchor タグ運用方針（案 A/B）の最終決定をセッション切替で持ち越し。本セッション（2026-05-12）で AskUserQuestion で再開・即座に判断確定（m311 + m615、案 A）してから Phase B → C → D を 1 commit にまとめて完走。

### (d-2) 二重 anchor 体制の初導入に伴う設計上の論点

書き下し anchor の二重化は本 retrofit が初例。retrofit 5-10 は単一 anchor 運用（sg03/m533、sg07/m713、sg02/m630、sg08/m549、sg09/m637）であり、本 retrofit で sg10/m209+m636 の二重 anchor を初導入。法華経 火宅三車の典籍系統が「願文系」と「教学系」に明確に二分されるため、いずれか一方では包摂できない判断から二重化を採用。将来の譬喩別軸（化城喩・良医喩・多宝塔等）でも同型の二重化が必要となる可能性があり、その際は本 retrofit の運用設計（案 A 採用ルール）を踏襲する。

### (d-3) Write tool truncate 事象の再発生と修復

本 retrofit Phase C で Write tool truncate 事象が 1 回再発生：

- **outputs/retrofit11_kataku_sansha.py**：末尾の `sys.exit(main())` が消失。Python の `path.write_bytes()` で末尾を補完して修復。

retrofit 9-10 で報告された Write tool 既知事象（retrofit 10 §(d-5) で 2 回再発）の継続。修復後の dry-run・本番適用ともに正常動作。今後も Python script 作成時は Write tool 直後に末尾検証を実施し、必要に応じて Python `path.write_bytes()` 直接書き込み方式で修復する運用を継続。

### (d-4) m-id 連番性検証ロジックの修正

retrofit 10 までは「m-id 連番性〔m1-m744〕missing=[], extra=[] ✓」の検証 OK が出ていたが、本 retrofit の dry-run 検証ロジックで「`not mid.startswith('m0')`」を条件に含めていたため、`m01`〜`m09`（先頭ゼロ付き表記）が除外され missing=[1,2,3,4,5,6,7,8,9] が表示された。正規表現 `^m\d+$` ベースに修正して全 motif を正しくカウント。本番適用時は修正後のロジックで全 pass を確認。今後の retrofit でも検証ロジックの正規化を継続。

### (d-5) commit_message.txt は Python `write_bytes` 直接書き込みで作成

retrofit 9 §(d-11) で警告された Write tool 上書き NUL 混入事象を回避するため、commit_message.txt と handoff（本ファイル）の作成は Python `path.write_bytes()` 直接書き込み方式を採用。最終検証で NUL 0 件確認。

### (d-6) retrofit 11 後の motifs.json サイズ

retrofit 11 で +3,314 bytes〔2,596,989 → 2,600,303 bytes〕。retrofit 10〔+2,383〕・retrofit 9〔+1,201〕・retrofit 8〔+2,609〕・retrofit 7〔+1,202〕・retrofit 6〔+1,816〕・retrofit 5〔+1,226〕・retrofit 4〔+1,525〕に続き 8 連続で +1,000〜3,400 bytes 規模の retrofit。新規 sg10 motif の description が長めかつ強連動 4 motif への +12 タグの累積で retrofit 8 の +2,609 や retrofit 10 の +2,383 を上回る最大値。次回 W1 マージ〔性霊集 残 55 篇分・約 1MB 見込み〕で再拡大予定。

### (d-7) gendai_gabun 字数管理

本 retrofit はタグ追加 + sg10 motif 追加のため、`motifs_with_gendai_gabun` は 743 維持（sg10 は成句のため `text_gendai_gabun` 設定なし・既存 sg01-sg09 と同方針）。gendai_gabun_chars_total も 154,931 維持。

### (d-8) git 状態の異常（retrofit 9/10 §(d-1) 同型・継続中）

セッション開始時に `git status` で前セッション同型の異常が継続：

- 誤ステージ済の削除：package.json/render.yaml/start.bat/tsconfig.json/vercel.json/outputs/motifs_index_design_backup_pre_retrofit*.md/outputs/CLAUDE_md_backup_pre_retrofit9.md 等
- 異常 rename：outputs/CLAUDE_md_backup_pre_retrofit8.md → outputs/CLAUDE_md_backup_pre_r（拡張子なしへの rename）

Phase D 直前にケンシン側で `outputs/cleanup_git_state_pre_retrofit11.bat` をダブルクリック実行して整理してから commit_push.bat へ進む方針。

### (d-9) commit_push.bat 安全装置の発動見込み

本 retrofit では新規ファイル追加〔outputs 配下のスクリプト 4 件・バックアップ 3 件・handoff 1 件〕と既存ファイル更新〔motifs.json・CLAUDE.md・motifs_index_design.md・commit_message.txt〕で、削除はなし。commit_push.bat の Step 4.5 SAFETY CHECK〔deleted 検出 → 中止ガード〕は発動しない見込み。ただし、bash mount 側で staged deletions が表示されている状態と Windows 側のクリーン状態の乖離（retrofit 10 §(d-3) 継続）の影響で、commit_push.bat 実行時に予期しない挙動を示す可能性がある。要 ケンシン実行時の確認。

### (d-10) Phase D 必須チェックリストの retrofit 11 で完全運用化（3 回目）

retrofit 9 で初の完全準拠を達成、retrofit 10 で 2 回目、本 retrofit 11 で 3 回目の完全準拠を達成。Phase D 必須チェックリストが定着した運用基盤として機能。冒頭行「retrofit 11 完走：法華経 譬喩品 火宅三車連動 retrofit〔新規 sg10「火宅三車」+ 既存 m209/m636 を書き下し anchor 二重体制で採用・連動軸六系統並立に到達〕」が本セッション内容と完全整合。

---

## 関連リンク

- 本体：`C:\Users\user\buddhist-data-api\`
- 本体 motifs.json：`data/indices/motifs.json`〔754 件・m1-m744 + sg01-sg10・2,600,303 bytes〕
- 本 retrofit build script：`outputs/retrofit11_kataku_sansha.py`〔dry-run + 本番適用の二段運用〕
- 補注 K 追加 script：`/tmp/add_chunote_k_retrofit11.py`（一時 script・本セッション内のみ）
- CLAUDE.md 更新 script：`/tmp/update_claude_md_retrofit11.py`（一時 script・本セッション内のみ）
- commit_message.txt 書き換え script：`/tmp/write_commit_message_retrofit11.py`（一時 script・本セッション内のみ）
- セッション着手前 git 整理：`outputs/cleanup_git_state_pre_retrofit11.bat`〔ASCII のみ・前セッションで準備済〕＋`outputs/cleanup_git_state_pre_retrofit11.py`〔UTF-8 helper・前セッションで準備済〕
- Phase A 候補スキャン：`outputs/retrofit11_phaseA_scan.py`＋`outputs/retrofit11_phaseA_candidates.txt`〔前セッションで準備済〕
- バックアップ：
  - `outputs/motifs_backup_pre_retrofit11.json`〔retrofit 前 motifs.json・2,596,989 bytes〕
  - `outputs/motifs_index_design_backup_pre_retrofit11.md`〔retrofit 前 motifs_index_design.md・65,559 bytes〕
  - `outputs/CLAUDE_md_backup_pre_retrofit11.md`〔retrofit 前 CLAUDE.md・229,785 bytes〕
- 前 retrofit handoff：`handoff_2026-05-11_retrofit10_complete.md`〔法華経 諸法実相連動〕
- 前 retrofit Phase A in-progress：`handoff_2026-05-11_retrofit11_phaseA_inprogress.md`〔本セッション開始時の引き継ぎメモ〕
- 補注 K 追加先：`_dev_references/motifs_index_design.md` §2
- workshop_protocol：`_dev_references/workshop_protocol.md` §5〔新規軸新設ルール〕

---

## 新セッション開始用メッセージ〔ケンシン貼付テンプレ〕

```
=== buddhist-data-api（本体）新セッション貼付用メッセージ（retrofit 11 完了後・次フェーズ着手版）===

【最初にやること】
作業フォルダ `C:\Users\user\buddhist-data-api` を mcp__cowork__request_cowork_directory で接続してください。接続完了後、以下の必読ファイルを順に読み込んで作業に着手してください。

【セッション概要】
2026-05-11 に Phase 4 W2 本体マージ完走〔commit 6ef4992・本体 750 motifs〕→ 同日 retrofit 4-10 完走 → 2026-05-12 retrofit 11 完走〔法華経 譬喩品 火宅三車連動・新規 sg10 + 既存 m209/m636 を書き下し anchor 二重体制で採用・連動軸六系統並立に到達〕。本体 motifs.json は 754 件・2,600,303 bytes・schema_history 69 件。motifs_index_design.md §2 に補注 K 追加〔補注 A-K 全 intact・74,761 bytes〕。CLAUDE.md は 235,797 bytes〔retrofit 4-11 全エントリ intact〕。連動軸六系統〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636〕の anchor 自己参照タグ運用が完全整合に到達。法華経内部の二段構成〔諸法実相（抽象的核心）+ 火宅三車（具体的譬喩）〕も成立。二重 anchor 体制の初例。

【最初に読むファイル（順番）】
1. `C:\Users\user\buddhist-data-api\handoff_2026-05-12_retrofit11_complete.md`〔本 retrofit セッション完走サマリ・必読〕
2. `C:\Users\user\buddhist-data-api\handoff_2026-05-11_retrofit10_complete.md`〔retrofit 10 完走サマリ〕
3. `C:\Users\user\buddhist-data-api\CLAUDE.md`〔本体側 CLAUDE.md・§「retrofit セッション運用」確認〕
4. `C:\Users\user\buddhist-data-api\_dev_references\motifs_index_design.md`〔schema 0.2 仕様・補注 D/E/F/G/H/I/J/K 含む〕
5. `C:\Users\user\buddhist-data-api\data\indices\motifs.json`〔本体現況・754 件〕

着手前に `git log --oneline -5` で HEAD 確認してください。HEAD は本 retrofit 11 commit です。

【本セッションの選択肢】
(A) retrofit 12 候補〔法華経譬喩別軸：寿量品 良医病子／化城喩品 化城／見宝塔品 多宝塔〕
(B) retrofit 12 候補〔華厳経 一即一切／弁顕密二教論 顕密判 等〕
(C) W1 buddhist-shoryoshu-workshop 継続抽出：性霊集 残 55 篇から motif 抽出
(D) kaimyo-app 教学系素材活用：連動軸六系統 anchor 完全整合済の素材プール活用
(E) W2 repo 凍結手続〔workshop_protocol §10(5)〕：archive 化 or 読み取り専用化

【注意点】
- bash mount 経由 git 書き込み禁止〔commit_push.bat 経由でケンシン側ダブルクリック〕
- 長文編集は Python script で in-memory 編集後 write back する代替手法を採用〔Edit/Write tool truncate 事象回避・本 retrofit でも 1 回再発・継続実証〕
- 軸新設は本体マージ・retrofit セッションで合意の原則を厳守
- 二重 anchor 体制の運用ルール（案 A）は将来の譬喩別軸でも踏襲（補注 K 参照）
- 本体 motifs.json は 2,600,303 bytes・W1 マージで再拡大見込み〔将来分割設計検討〕
- 着手前に `wc -c CLAUDE.md` と `git diff --stat` で truncate 確認推奨
- **Phase D 必須チェックリストに従う**〔CLAUDE.md §「retrofit セッション運用」参照・commit_message.txt 更新は必須項目〕
- bat ファイルは ASCII のみで作成〔cmd.exe Shift-JIS 解釈で日本語誤動作〕
- Write tool で既存ファイルを上書きする際は書き込み直後に NUL カウント検証必須〔Write tool 上書き既知事象・本 retrofit でも再発検出〕。可能な限り Python script の `path.write_bytes(data)` を使用

進める前に、最優先タスクを確認してください。
```

---

最終更新：2026-05-12〔retrofit 11 完走・法華経 譬喩品 火宅三車連動 retrofit。新規 sg-id sg10「火宅三車」を追加〔出典:法華経 譬喩品「初説三乗引導衆生、然後但以大乗而度脱之」〕、書き下し anchor として **二重体制** を初導入：m209（性霊集 第八巻 願文系 anchor）+ m636（秘蔵宝鑰 第八章 教学系 anchor）。強連動 4 motif〔m209(anchor 願文系)/m636(anchor 教学系)/m311(性霊集 第一巻 三界火宅)/m615(秘蔵宝鑰 第四住心 羊車)〕に `連動:sg10`・`連動:m209`・`連動:m636` を付与（+12 タグ・案 A 採用＝全 motif に二重 anchor 明示）。total_motifs 753→754（+1 新規 sg10）・famous_phrases 9→10。schema 0.2 維持・整合性検証 7 項目全 pass。本体 motifs.json 2,600,303 bytes〔+3,314〕・schema_history 69 件〔+1・origin: retrofit_11:doctrine〕・補注 K 追加〔motifs_index_design.md §2・65,559→74,761 bytes・+9,202〕・CLAUDE.md 更新完了〔229,785→235,797 bytes〕・commit_message.txt 書き換え済〔Phase D 必須項目クリア・冒頭行整合確認済〕。連動軸六系統並立〔即身成仏 sg03/m533、三句法門 sg07/m713、色即是空 sg02/m630、阿字本不生 sg08/m549、諸法実相 sg09/m637、火宅三車 sg10/m209+m636〕に到達——法華経内部で諸法実相（抽象的核心）と火宅三車（具体的譬喩）の二段構成に到達。二重 anchor 体制の初例として将来の譬喩別軸展開（化城喩・良医喩・多宝塔等）への運用基盤を整備。Phase D 必須チェックリストに完全準拠する第三の retrofit〕

# 引き継ぎメモ：十住心論 motif 中間マージ（W3 jw001-045 → 本体 m2175-m2219）

**日付**：2026-05-31
**種別**：本体マージセッション（W3 buddhist-jujushinron-workshop → buddhist-data-api 本体）
**ステータス**：本体 motifs.json 反映済み・commit_push.bat 実行待ち

## 概要

W3 で抽出した十住心論 motif 45 件（jw001-045）を本体 `data/indices/motifs.json` に統合。
本体最終 m-id m2174 の次から連番で **m2175〜m2219** に再番号付け。

- total_motifs 2201 → **2246**（m1-m2219 ＋ sg01-sg27）。
- 巻別：巻一4・巻二4・巻三4・巻四3・巻五3・巻六5・巻七3・巻八3・巻九4・巻十12。
- 3層構成：各顕教住心の「定義＋密教合流（九顕一密）＋中核教学」＋巻十（密教）12件＋追補。

## 再番号付けの確認

- jw001→m2175 … jw045→m2219（連番・W3 内 jw 採番順）。
- 連動タグは本体 anchor を参照（sg17/m599・sg02/m630・sg03/m533・sg08/m549・sg18/m571）。全て本体に存在を確認済み。jw 内部相互参照は無し。

## stats（全件 recompute で確定）

| 項目 | 旧 | 新 |
|---|---|---|
| total_motifs | 2201 | 2246 |
| kakikudashi_chars_total | 146,063 | 156,113（+10,050） |
| gendaigoyaku_chars_total | 549,822 | 573,569（+23,747） |

- 事前ドリフト 0（backup の stored＝recompute を確認）。増分は新規45件の寄与のみ。
- from_corpus_jujushinron=45 を追加。篇別内訳に jujushinron_巻第一〜巻第十 の dict エントリ10件を追加。schema_history に W3 マージエントリ追記。schema_version 0.2 維持。

## 検証（全 pass）

NUL 0／total=array 2246／m 連番 m1-m2219 missing なし／sg 27 件／新規 motif source 全 dict(corpus=jujushinron)／新規 motif 半角括弧 0／id 重複 0／recompute 差分ゼロ。
バックアップ：`data/indices/motifs.json.bak_pre_jujushinron_merge`。

## 残・次段

- 本コミットは motifs.json のみ。jujushinron.json 本文3点（原典・書き下し・現代語訳）は前コミット 597a0e8 で中間取込済み。
- 本マージは「中間マージ」。W3 でさらに motif を追補した場合（巻十の字門各字義・巻二輪王段・巻六三性詳説・巻九十玄門各門 等）、次回マージで m2220 以降に追加する。
- jsg 成句候補（如実知自心・阿字本不生・九種住心無自性 等）は未採番。本体で sg28 以降に採番する場合は別 retrofit セッションで。
- 本体 CLAUDE.md のタイトル行・進捗ヘッダ更新は未実施（任意・次セッションで追記可）。

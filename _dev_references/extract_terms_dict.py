#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化 G2（dict 型著作向け・密教教学用語抽出）

dict 型コーパス（弁顕密二教論・吽字義 等）の **トップレベル `gendaigoyaku`**
（単一の連続する現代語訳テキスト）から、19 語の密教教学用語を辞書ベース
で抽出し、`data/mikkyou/index_<corpus>_terms.json` を生成する。

extract_terms.py（性霊集・list 型 112 篇向け）の dict 型版。19 語辞書・
長語優先 substring 走査・周辺梵語注記抽出のロジックは extract_terms.py
と完全互換。

仕様：cross_index_spec.md v1.5 §1 Tier 1-1 / G2 dict 型コーパス索引化

使い方：
    python3 _dev_references/extract_terms_dict.py --corpus nikyo-ron.json
    python3 _dev_references/extract_terms_dict.py --corpus all  # primary_corpus 全 dict 著作

dict 型コーパスは篇分割を持たないため、occurrences は `corpus_id` +
`context_position`（gendaigoyaku 内オフセット）+ `context` で出典を一意に
特定する。
"""

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE_DIR = ROOT / 'data' / 'kukai'
OUTPUT_DIR = ROOT / 'data' / 'mikkyou'

# ====== dict 型 primary_corpus 著作（manifest と整合）======
# extract_terms_dict.py の対象（性霊集はリスト型のため別途 extract_terms.py）。
# 菩提心論は kakikudashi のみで gendaigoyaku 待ちのため対象外。
DICT_CORPUS_LIST = [
    'nikyo-ron.json',
    'ujiji.json',
    'shoji-jisso.json',
    'sokushin-jobutsu.json',
    'hannya-hiken.json',
    'hizo-houyaku.json',
    'dainichikyo-sho-vol1.json',
    'sankyo-shiki.json',
]

# ====== 19 語辞書（extract_terms.py と完全同期）======
TERMS_DEF = [
    {'term': '阿字本不生', 'sanskrit': 'ā-di-an-utpāda',
     'definition': '密教根本教義。阿字（a-kāra）が本来不生（不滅）であることを観じ、万物の本源を悟る。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '即身成仏', 'sanskrit': 'sa-deha-prāpti-buddhatva',
     'definition': '空海『即身成仏義』中心教義。父母所生の身のまま、現生で仏となる密教の道。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['成', '仏']},
    {'term': '無縁慈悲', 'sanskrit': 'an-ārambaṇa-karuṇā',
     'definition': '対象を限定せず、すべての衆生に注がれる無条件の大悲。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['慈', '悲']},
    {'term': '大空三昧', 'sanskrit': 'mahā-śūnyatā-samādhi',
     'definition': '大空（一切法空）を観ずる三昧。密教の高次禅定。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '本不生', 'sanskrit': 'ādyanutpāda',
     'definition': '一切法の本来不生不滅。阿字本不生の核となる教義。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '三摩地', 'sanskrit': 'samādhi',
     'definition': '禅定。心を一境に住して散乱を離れた状態。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '密教', 'sanskrit': 'guhya-mantra-yāna',
     'definition': '空海の宗派自称。秘密真言乗。大日如来の内証を直接伝える教え。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '大日', 'sanskrit': 'Mahāvairocana',
     'definition': '大日如来。密教の本尊。遮那と同義。法身そのもの。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['大', '日']},
    {'term': '法界', 'sanskrit': 'dharma-dhātu',
     'definition': '宇宙の真実相。一切法の根本領域。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['法', '界']},
    {'term': '三密', 'sanskrit': 'trīṇi guhyāni',
     'definition': '身密（kāya-guhya）・口密（vāk-guhya）・意密（mano-guhya）。仏の三業を行者が修して即身成仏に至る道。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['密']},
    {'term': '法身', 'sanskrit': 'dharmakāya',
     'definition': '仏の真実身。大日如来は六大法身。形相を超えた法そのもの。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['法', '身']},
    {'term': '真言', 'sanskrit': 'mantra',
     'definition': '真言陀羅尼。仏の真実言語。密教修行の中心。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['真', '言']},
    {'term': '大悲', 'sanskrit': 'mahā-karuṇā',
     'definition': '仏の大いなる慈悲。一切衆生を救う心。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['大', '悲']},
    {'term': '阿字', 'sanskrit': 'a-kāra',
     'definition': '密教根本字。梵語五十字門の最初の字。本不生を象徴。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '遮那', 'sanskrit': 'Vairocana',
     'definition': '毘盧遮那の略。大日如来。光明遍照。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['遮', '那']},
    {'term': '心王', 'sanskrit': 'citta-rāja',
     'definition': '八識の根本識。心の主体・統括者。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '即身', 'sanskrit': 'sa-deha',
     'definition': '即身成仏の略。父母所生の身のまま現生で仏となる。',
     'kaimyo_suitable': False, 'kaimyo_chars': []},
    {'term': '玄機', 'sanskrit': '—',
     'definition': '玄妙なる機関・機微。密教の深秘の働き。漢語起源（『荘子』『老子』由来）。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['玄', '機']},
    {'term': '智剣', 'sanskrit': 'jñāna-khaḍga',
     'definition': '煩悩を断ずる智慧の剣。文殊菩薩・不動明王の象徴。',
     'kaimyo_suitable': True, 'kaimyo_chars': ['智', '剣']},
]

# 長語優先のためソート（長さ降順）
TERMS_ORDERED = sorted(TERMS_DEF, key=lambda d: -len(d['term']))

# ====== 抽出パターン ======
RE_SANSKRIT = re.compile(
    "[A-Za-zĀāĪīŪūṅÑñṬṭḌḍṆṇḶḷŚśṢṣṚṛḤḥṂṃ]"
    "[A-Za-zĀāĪīŪūṅÑñṬṭḌḍṆṇḶḷŚśṢṣṚṛḤḥṂṃ\\-\\.’ʼ']+"
)


def extract_sanskrit_in_context(text, position, term_len, window=30):
    start = max(0, position - window)
    end = min(len(text), position + term_len + window)
    ctx = text[start:end]
    found = RE_SANSKRIT.findall(ctx)
    return [s for s in found if len(s) >= 3]


def corpus_id_of(filename: str) -> str:
    """nikyo-ron.json -> nikyo-ron"""
    return Path(filename).stem


def extract_one_corpus(corpus_filename: str):
    """dict 型コーパス 1 ファイルから 19 語の occurrences を抽出。

    対象は **トップレベル `gendaigoyaku` のみ**（連続テキスト 1 本）。
    occurrences の位置キーは `context_position`（gendaigoyaku 内のオフセット）。
    篇分割を持たないため `shoryoshu_idx`/`篇分布` は付与しない。
    """
    path = SOURCE_DIR / corpus_filename
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if not isinstance(data, dict):
        raise ValueError(
            f'{corpus_filename}: 想定 dict だが {type(data).__name__} だった。'
            f'list 型コーパスは extract_terms.py を使用してください。'
        )

    text = data.get('gendaigoyaku', '') or ''
    if not text:
        return None  # gendaigoyaku なし（菩提心論等）はスキップ

    cid = corpus_id_of(corpus_filename)
    table = defaultdict(lambda: {'occurrences': []})

    # 長語優先・破壊的探索（同字数のスペース置換で消費・extract_terms.py と同じロジック）
    consumed = list(text)
    for tdef in TERMS_ORDERED:
        term = tdef['term']
        tlen = len(term)
        src = ''.join(consumed)
        pos = 0
        while True:
            p = src.find(term, pos)
            if p < 0:
                break
            ctx_start = max(0, p - 30)
            ctx_end = min(len(text), p + tlen + 30)
            context = text[ctx_start:ctx_end].replace('\n', ' ')
            sanskrit_hits = extract_sanskrit_in_context(text, p, tlen, window=30)

            table[term]['occurrences'].append({
                'corpus_id': cid,
                'context': context,
                'context_position': p,
                'sanskrit_in_context': sorted(set(sanskrit_hits)) if sanskrit_hits else [],
            })

            for i in range(p, p + tlen):
                consumed[i] = ' '
            pos = p + tlen
            src = ''.join(consumed)

    return {
        'corpus_id': cid,
        'corpus_filename': corpus_filename,
        'gendaigoyaku_length': len(text),
        'table': table,
    }


def build_doc(corpus_filename: str, gendaigoyaku_length: int, table) -> dict:
    """1 コーパス分の occurrences テーブルから索引 JSON を組み立て。

    extract_terms.py と異なり篇分割を持たないため `篇分布` を持たない。
    その代わり `gendaigoyaku_length`（オフセット範囲の参考）を summary に置く。
    """
    cid = corpus_id_of(corpus_filename)

    entries = []
    for tdef in TERMS_DEF:
        term = tdef['term']
        payload = table.get(term, {'occurrences': []})
        occs = payload['occurrences']
        entries.append({
            'term': term,
            'term_kana': '',
            'sanskrit': tdef['sanskrit'],
            'definition': tdef['definition'],
            'kaimyo_suitable': tdef['kaimyo_suitable'],
            'kaimyo_chars': tdef['kaimyo_chars'],
            'occurrence_count': len(occs),
            'occurrences': occs,
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], e['term']))

    total_occ = sum(e['occurrence_count'] for e in entries)

    return {
        'schema_version': '1.0',
        'category': '密教教学用語（mikkyo terms）',
        'source_corpus': corpus_filename,
        'corpus_type': 'dict',
        'extraction_field': 'gendaigoyaku',
        'generated_at': date.today().isoformat(),
        'extraction_strategy': '辞書ベース（19 語）+ 長語優先 substring 走査 + 周辺梵語注記抽出',
        'dictionary_size': len(TERMS_DEF),
        'gendaigoyaku_length': gendaigoyaku_length,
        'summary': {
            'unique_terms': len(entries),
            'total_occurrences': total_occ,
            'kaimyo_suitable_count': sum(1 for e in entries if e['kaimyo_suitable']),
            'matched_term_count': sum(1 for e in entries if e['occurrence_count'] > 0),
        },
        'entries': entries,
    }


def write_doc(doc: dict, corpus_filename: str) -> Path:
    cid = corpus_id_of(corpus_filename)
    out_path = OUTPUT_DIR / f'index_{cid}_terms.json'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    # NULL バイト検証（CLAUDE.md 必須運用）
    with open(out_path, 'rb') as f:
        raw = f.read()
    nulls = len(raw) - len(raw.rstrip(b'\x00'))
    if nulls != 0:
        raise AssertionError(f'NULL byte tail detected in {out_path}: {nulls} bytes')
    return out_path


def process(corpus_filename: str, *, verbose=True) -> dict:
    res = extract_one_corpus(corpus_filename)
    if res is None:
        if verbose:
            print(f'[SKIP] {corpus_filename}: gendaigoyaku が空（菩提心論等）')
        return None

    doc = build_doc(corpus_filename, res['gendaigoyaku_length'], res['table'])
    out_path = write_doc(doc, corpus_filename)

    if verbose:
        s = doc['summary']
        print(f"[OK] {corpus_filename:<28s} -> {out_path.name}")
        print(f"     gendaigoyaku={doc['gendaigoyaku_length']:,} 字"
              f" / matched_terms={s['matched_term_count']}/{s['unique_terms']}"
              f" / total_occ={s['total_occurrences']}")
        # 上位 5 語
        top = [e for e in doc['entries'] if e['occurrence_count'] > 0][:5]
        if top:
            top_str = ', '.join(f"{e['term']}={e['occurrence_count']}" for e in top)
            print(f"     top: {top_str}")
    return doc


def main():
    ap = argparse.ArgumentParser(description='dict 型著作向け 密教教学用語索引生成')
    ap.add_argument('--corpus', required=True,
                    help="対象著作 (例: nikyo-ron.json) または 'all' で全 dict 型 primary_corpus")
    args = ap.parse_args()

    targets = DICT_CORPUS_LIST if args.corpus == 'all' else [args.corpus]

    print('=' * 70)
    print(f'extract_terms_dict.py — 対象 {len(targets)} 著作')
    print('=' * 70)

    for fn in targets:
        try:
            process(fn)
        except Exception as e:
            print(f'[ERR] {fn}: {e}', file=sys.stderr)
            raise

    print('\n完了。')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化 G2-D（dict 型著作向け・人名抽出）

dict 型コーパス（弁顕密二教論・吽字義 等）の **トップレベル `gendaigoyaku`**
から、仏教史上の人物・漢籍人物・日本史上の人物を網羅抽出し、
`data/mikkyou/index_<corpus>_persons.json` を生成する。

`_tmp_extract_persons.py`（性霊集・list 型）の dict 型版。
PERSONS seed dict（95 entries・9 subcategories）は共有モジュール
`seed_data_persons.py` から import する。

仕様：cross_index_spec.md v1.8 §17 G2-D / 旧 §11 Tier 3-5 dict 拡張

使い方：
    python3 _dev_references/extract_persons_dict.py --corpus nikyo-ron.json
    python3 _dev_references/extract_persons_dict.py --corpus all
"""

import argparse
import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# 共有 seed
sys.path.insert(0, str(Path(__file__).parent))
from seed_data_persons import PERSONS, collect_match_intervals  # noqa: E402

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE_DIR = ROOT / 'data' / 'kukai'
OUTPUT_DIR = ROOT / 'data' / 'mikkyou'

# ====== dict 型 primary_corpus 著作 ======
DICT_CORPUS_LIST = [
    'nikyo-ron.json',
    'ujiji.json',
    'shoji-jisso.json',
    'sokushin-jobutsu.json',
    'hannya-hiken.json',
    'hizo-houyaku.json',
    'dainichikyo-sho-vol1.json',
    'sankyo-shiki.json',
    'bodaishinron.json',  # 2026-05-04 追加（候補 D・9 著作目）
]


def corpus_id_of(filename: str) -> str:
    return Path(filename).stem


def extract_one_corpus(corpus_filename: str, sanskrit_canonicals: set):
    src_path = SOURCE_DIR / corpus_filename
    with open(src_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f'{corpus_filename}: 想定 dict だが {type(data).__name__}')

    text = data.get('gendaigoyaku', '') or ''
    if not text:
        return None

    cid = corpus_id_of(corpus_filename)

    # canonical → entry-skeleton
    table = defaultdict(lambda: {
        'occurrences': [],
        'forms': defaultdict(int),
    })

    # surfaces 一覧（長一致優先のためソート）
    surfaces = []  # (surface, canonical, is_single_kanji)
    for p in PERSONS:
        cn = p['canonical']
        sk = p.get('is_single_kanji', False)
        surfaces.append((cn, cn, sk))
        for a in p['aliases']:
            surfaces.append((a, cn, False))
    surfaces.sort(key=lambda x: -len(x[0]))

    # 重複防止：マッチ済みインターバル
    taken = []  # list of (s, e), sorted

    def overlap(s, e):
        for ts, te in taken:
            if not (e <= ts or s >= te):
                return True
        return False

    for surface, canonical, single_kanji in surfaces:
        hits = collect_match_intervals(text, surface, single_kanji)
        for s, e in hits:
            if overlap(s, e):
                continue
            taken.append((s, e))
            ctx_start = max(0, s - 30)
            ctx_end = min(len(text), e + 30)
            context = text[ctx_start:ctx_end].replace('\n', ' ')
            table[canonical]['occurrences'].append({
                'corpus_id': cid,
                'context': context,
                'context_position': s,
                'matched_form': surface,
            })
            table[canonical]['forms'][surface] += 1
    taken.sort()

    return {
        'corpus_id': cid,
        'corpus_filename': corpus_filename,
        'gendaigoyaku_length': len(text),
        'table': table,
    }


def build_doc(corpus_filename: str, gendaigoyaku_length: int, table, sanskrit_canonicals: set) -> dict:
    seed_lookup = {p['canonical']: p for p in PERSONS}
    entries = []
    for canonical, blob in table.items():
        if not blob['occurrences']:
            continue
        seed = seed_lookup[canonical]
        forms_list = [{'form': k, 'count': v}
                      for k, v in sorted(blob['forms'].items(), key=lambda x: -x[1])]
        sk_canonical = seed.get('sanskrit_canonical')
        sk_in_index = (sk_canonical in sanskrit_canonicals) if sk_canonical else None
        entries.append({
            'canonical': canonical,
            'aliases': seed['aliases'],
            'subcategory': seed['subcategory'],
            'definition': seed['definition'],
            'sanskrit_canonical': sk_canonical,
            'sanskrit_canonical_in_index': sk_in_index,
            'matched_forms': forms_list,
            'occurrence_count': len(blob['occurrences']),
            'occurrences': blob['occurrences'],
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], e['canonical']))

    # subcategory 別集計
    by_sub = defaultdict(lambda: {'unique': 0, 'occurrences': 0})
    for e in entries:
        s = e['subcategory']
        by_sub[s]['unique'] += 1
        by_sub[s]['occurrences'] += e['occurrence_count']

    return {
        'schema_version': '1.3',
        'category': '人名索引',
        'source_corpus': corpus_filename,
        'corpus_type': 'dict',
        'extraction_field': 'gendaigoyaku',
        'generated_at': str(date.today()),
        'extraction_strategy': '人手キュレートシード辞書（仏教祖師・諸尊・諸天・諸子百家・神話人物・天皇・貴族）。長表記優先・1 文字人名は前後非漢字境界条件で誤検知抑止。',
        'subcategory_taxonomy': sorted({p['subcategory'] for p in PERSONS}),
        'seed_dictionary_size': len(PERSONS),
        'gendaigoyaku_length': gendaigoyaku_length,
        'summary': {
            'unique_terms': len(entries),
            'unique_persons': len(entries),
            'total_occurrences': sum(e['occurrence_count'] for e in entries),
            'by_subcategory': {k: dict(v) for k, v in sorted(by_sub.items())},
        },
        'entries': entries,
    }


def write_doc(doc: dict, corpus_filename: str) -> Path:
    cid = corpus_id_of(corpus_filename)
    out_path = OUTPUT_DIR / f'index_{cid}_persons.json'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(doc, ensure_ascii=False, indent=2).encode('utf-8')
    payload = payload.rstrip(b'\x00')
    with open(out_path, 'wb') as f:
        f.write(payload)
    raw = out_path.read_bytes()
    nul = b'\x00'
    nulls = len(raw) - len(raw.rstrip(nul))
    if nulls != 0:
        raise AssertionError(f'NULL byte tail in {out_path}: {nulls}')
    return out_path


def process(corpus_filename: str, *, verbose=True):
    cid = corpus_id_of(corpus_filename)
    sanskrit_path = OUTPUT_DIR / f'index_{cid}_sanskrit.json'
    if sanskrit_path.exists():
        with open(sanskrit_path, 'r', encoding='utf-8') as f:
            sd = json.load(f)
        sanskrit_canonicals = {e['canonical'] for e in sd['entries']}
    else:
        sanskrit_canonicals = set()

    res = extract_one_corpus(corpus_filename, sanskrit_canonicals)
    if res is None:
        if verbose:
            print(f'[SKIP] {corpus_filename}: gendaigoyaku が空')
        return None

    doc = build_doc(corpus_filename, res['gendaigoyaku_length'], res['table'], sanskrit_canonicals)
    out_path = write_doc(doc, corpus_filename)

    if verbose:
        s = doc['summary']
        print(f"[OK] {corpus_filename:<28s} -> {out_path.name}")
        print(f"     gendaigoyaku={doc['gendaigoyaku_length']:,} 字"
              f" / unique={s['unique_persons']}"
              f" / occ={s['total_occurrences']}")
        # 上位 5 人
        top = doc['entries'][:5]
        if top:
            top_str = ', '.join(f"{e['canonical']}({e['subcategory'].split('_')[-1]})={e['occurrence_count']}" for e in top)
            print(f"     top: {top_str}")
    return doc


def main():
    ap = argparse.ArgumentParser(description='dict 型著作向け 人名索引生成')
    ap.add_argument('--corpus', required=True,
                    help="対象著作 (例: nikyo-ron.json) または 'all'")
    args = ap.parse_args()
    targets = DICT_CORPUS_LIST if args.corpus == 'all' else [args.corpus]
    print('=' * 70)
    print(f'extract_persons_dict.py — 対象 {len(targets)} 著作')
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

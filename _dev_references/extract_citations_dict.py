#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化 G2（dict 型著作向け・典故書名抽出）

dict 型コーパス（弁顕密二教論・吽字義 等）の **トップレベル `gendaigoyaku`**
から、『〜』形式の書名を抽出し、以下 2 ファイルを生成する：

- data/mikkyou/index_<corpus>_citations.json  典故書名（他者著作の引用）
- data/mikkyou/index_<corpus>_kukai_works.json  空海著作・性霊集編纂物等

extract_citations.py（性霊集・list 型 112 篇向け）の dict 型版。
正規表現・CANONICAL_MAP・除外辞書・KUKAI_WORKS のロジックは extract_citations.py
と完全互換。

仕様：cross_index_spec.md v1.5 §1 Tier 1-2 / G2 dict 型コーパス索引化

使い方：
    python3 _dev_references/extract_citations_dict.py --corpus nikyo-ron.json
    python3 _dev_references/extract_citations_dict.py --corpus all  # 全 dict 著作
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
]

# ====== 抽出パターン ======
RE_CITATION = re.compile(r'『([^『』]+?)』')
RE_PAREN_ZEN = re.compile(r'（[^（）]*?）')


def preprocess(book: str) -> str:
    prev = None
    s = book
    while prev != s:
        prev = s
        s = RE_PAREN_ZEN.sub('', s)
    return s.strip()


# ====== 書名正規化辞書（extract_citations.py と完全同期）======
CANONICAL_MAP = {
    # 大智度論
    '智度論': '大智度論',
    '大論': '大智度論',
    # 法華経
    '妙法蓮華経': '法華経',
    # 涅槃経
    '大般涅槃経': '涅槃経',
    # 般若心経
    '心経': '般若心経',
    '般若波羅蜜多心経': '般若心経',
    # 大日経
    '大毘盧遮那成仏神変加持経': '大日経',
    # 金剛頂経
    '金剛頂瑜伽中略出念誦経': '金剛頂経',
    # 瑜伽師地論
    '瑜伽論': '瑜伽師地論',
    # 課題 A：理趣経の表記揺れ統合
    '大楽金剛不空三昧耶理趣経': '理趣経',
    '大楽金剛不空真実三摩耶経': '理趣経',
    '大楽金剛不空真実三摩耶経般若波羅蜜多理趣品': '理趣経',
    '大楽金剛不空真実三昧耶経・般若波羅蜜多理趣品': '理趣経',
    '大三昧耶理趣経': '理趣経',
    '大楽金剛不空真実三摩耶経般若波羅蜜多理趣釈': '理趣釈',
    '理趣釈経': '理趣釈',
    # 課題 B：易 → 易経
    '易': '易経',
    # 課題 C：仁王経 系統
    '仁王般若経': '仁王経',
    '仁王般若波羅蜜護国経': '仁王経',
    '仁王護国般若波羅蜜多経': '仁王経',
    '仁王護国般若経': '仁王経',
    '仁王般若波羅蜜経': '仁王経',
}

EXCLUDE_TERMS = {
    '内典・外典',
}

# ====== 空海著作・性霊集編纂物（別ファイルへ分離）======
KUKAI_WORKS = {
    # 空海請来書・著作
    '梵字悉曇字母并びに釈義': '空海著作',
    '古今文字讃': '空海請来書',
    '古今篆隷の文体': '空海請来書',
    # 性霊集自体（真済編纂）
    '続性霊集補闕鈔': '性霊集編纂物',
    # idx=12 篇名そのもの
    '大広智の影の讃': 'idx12篇名（空海碑文）',
    '大広智不空三蔵の影の讃': 'idx12篇名（空海碑文・括弧前）',
    # 弁顕密二教論・吽字義 等で自著言及がある場合に追加可能
    '弁顕密二教論': '空海著作',
    '吽字義': '空海著作',
    '即身成仏義': '空海著作',
    '声字実相義': '空海著作',
    '般若心経秘鍵': '空海著作',
    '秘蔵宝鑰': '空海著作',
    '十住心論': '空海著作',
    '秘密曼荼羅十住心論': '空海著作',
    '三教指帰': '空海著作',
    '聾瞽指帰': '空海著作',
    '御請来目録': '空海著作',
    '性霊集': '空海関連（弟子真済編）',
    '遍照発揮性霊集': '空海関連（弟子真済編）',
    '菩提心論': '空海関連（不空訳・真言宗根本論書）',
    # 大日経疏は不空訳『大日経』への一行阿闍梨疏。空海著作ではないが、空海の
    # 講筵で多用される根本注釈書のため、citations 側に残す（kukai_works には含めない）。
}


def canonicalize(book: str) -> str:
    pre = preprocess(book)
    return CANONICAL_MAP.get(pre, pre)


def classify(term: str) -> str:
    if term in KUKAI_WORKS:
        return 'kukai_works'
    return 'citations'


def corpus_id_of(filename: str) -> str:
    return Path(filename).stem


def extract_one_corpus(corpus_filename: str):
    path = SOURCE_DIR / corpus_filename
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(f'{corpus_filename}: 想定 dict だが {type(data).__name__}')

    text = data.get('gendaigoyaku', '') or ''
    if not text:
        return None

    cid = corpus_id_of(corpus_filename)
    citations = defaultdict(lambda: {'occurrences': [], 'aliases': set()})
    kukai = defaultdict(lambda: {'occurrences': [], 'aliases': set()})
    excluded_log = []

    for m in RE_CITATION.finditer(text):
        raw_book = m.group(1).strip()
        if not raw_book or len(raw_book) > 30 or '\n' in raw_book:
            continue
        canonical = canonicalize(raw_book)
        if canonical in EXCLUDE_TERMS or preprocess(raw_book) in EXCLUDE_TERMS:
            excluded_log.append((raw_book, text[max(0, m.start()-20):m.end()+20]))
            continue

        start = max(0, m.start() - 30)
        end = min(len(text), m.end() + 30)
        context = text[start:end].replace('\n', ' ')

        occ = {
            'corpus_id': cid,
            'context': context,
            'context_position': m.start(),
            'raw_form': raw_book,
        }

        bucket = kukai if classify(canonical) == 'kukai_works' else citations
        bucket[canonical]['occurrences'].append(occ)
        if raw_book != canonical:
            bucket[canonical]['aliases'].add(raw_book)

    return {
        'corpus_id': cid,
        'corpus_filename': corpus_filename,
        'gendaigoyaku_length': len(text),
        'citations': citations,
        'kukai': kukai,
        'excluded_log': excluded_log,
    }


def build_entries(table) -> list:
    entries = []
    for term, payload in table.items():
        occs = payload['occurrences']
        entries.append({
            'term': term,
            'aliases': sorted(payload['aliases']),
            'occurrence_count': len(occs),
            'occurrences': occs,
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], e['term']))
    return entries


def build_doc(corpus_filename: str, gendaigoyaku_length: int, entries, *, category, extra=None):
    total_occ = sum(e['occurrence_count'] for e in entries)
    doc = {
        'schema_version': '1.0',
        'category': category,
        'source_corpus': corpus_filename,
        'corpus_type': 'dict',
        'extraction_field': 'gendaigoyaku',
        'generated_at': date.today().isoformat(),
        'extraction_pattern': '『([^『』]+?)』',
        'canonicalization_dict_size': len(CANONICAL_MAP),
        'exclude_dict_size': len(EXCLUDE_TERMS),
        'kukai_works_dict_size': len(KUKAI_WORKS),
        'gendaigoyaku_length': gendaigoyaku_length,
        'summary': {
            'unique_terms': len(entries),
            'total_occurrences': total_occ,
        },
        'entries': entries,
    }
    if extra:
        doc.update(extra)
    return doc


def write_doc(doc: dict, corpus_filename: str, suffix: str) -> Path:
    cid = corpus_id_of(corpus_filename)
    out_path = OUTPUT_DIR / f'index_{cid}_{suffix}.json'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    with open(out_path, 'rb') as f:
        raw = f.read()
    nul = b'\x00'
    nulls = len(raw) - len(raw.rstrip(nul))
    if nulls != 0:
        raise AssertionError(f'NULL byte tail detected in {out_path}: {nulls} bytes')
    return out_path


def process(corpus_filename: str, *, verbose=True):
    res = extract_one_corpus(corpus_filename)
    if res is None:
        if verbose:
            print(f'[SKIP] {corpus_filename}: gendaigoyaku が空')
        return None, None

    cit_entries = build_entries(res['citations'])
    kuk_entries = build_entries(res['kukai'])
    cit_doc = build_doc(corpus_filename, res['gendaigoyaku_length'], cit_entries,
                        category='典故書名（citations・他者著作）')
    kuk_doc = build_doc(corpus_filename, res['gendaigoyaku_length'], kuk_entries,
                        category='空海著作・性霊集編纂物（kukai works）',
                        extra={'classification_table': KUKAI_WORKS})

    cit_path = write_doc(cit_doc, corpus_filename, 'citations')
    kuk_path = write_doc(kuk_doc, corpus_filename, 'kukai_works')

    if verbose:
        print(f"[OK] {corpus_filename:<28s}")
        print(f"     gendaigoyaku={res['gendaigoyaku_length']:,} 字"
              f" / citations={cit_doc['summary']['unique_terms']} 種・"
              f"{cit_doc['summary']['total_occurrences']} 件"
              f" / kukai_works={kuk_doc['summary']['unique_terms']} 種・"
              f"{kuk_doc['summary']['total_occurrences']} 件"
              f" / excluded={len(res['excluded_log'])} 件")
        if cit_entries[:3]:
            top = ', '.join(f"『{e['term']}』={e['occurrence_count']}" for e in cit_entries[:5])
            print(f"     top citations: {top}")
        if kuk_entries[:3]:
            top = ', '.join(f"『{e['term']}』={e['occurrence_count']}" for e in kuk_entries[:5])
            print(f"     top kukai_works: {top}")

    return cit_doc, kuk_doc


def main():
    ap = argparse.ArgumentParser(description='dict 型著作向け 典故書名索引生成')
    ap.add_argument('--corpus', required=True,
                    help="対象著作 (例: nikyo-ron.json) または 'all'")
    args = ap.parse_args()
    targets = DICT_CORPUS_LIST if args.corpus == 'all' else [args.corpus]
    print('=' * 70)
    print(f'extract_citations_dict.py — 対象 {len(targets)} 著作')
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

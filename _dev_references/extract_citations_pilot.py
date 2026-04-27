#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化フェーズ B パイロット抽出スクリプト（典故書名）

shoryoshu_miyasaka.json の全 112 篇 gendaigoyaku から
『〜』形式の書名を抽出し、index_shoryoshu_citations.json を生成する。

仕様：cross_index_spec.md v0.1 §1 Tier 1-2 / §2.2 共通スキーマ
"""

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE = ROOT / 'data' / 'kukai' / 'shoryoshu_miyasaka.json'
OUTPUT = ROOT / 'data' / 'mikkyou' / 'index_shoryoshu_citations.json'

# ====== 抽出パターン ======
# 『〜』スコープ。ネスト・行跨ぎは想定しない（性霊集の補注は単一行内が前提）
RE_CITATION = re.compile(r'『([^『』]+?)』')

# ====== 書名正規化辞書（パイロット版・段階拡張）======
# 「同一典籍の異表記」を一つに統合する。表記揺れの代表例のみ。
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
}

def canonicalize(book):
    return CANONICAL_MAP.get(book, book)


def extract_citations():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        corpus = json.load(f)

    # term -> {'occurrences': [...], 'occurrence_count': int, 'aliases': set}
    citations = defaultdict(lambda: {'occurrences': [], 'aliases': set()})

    for idx, item in enumerate(corpus):
        篇名 = item.get('篇名', '')
        巻 = item.get('巻番号', '')
        for page_idx, page in enumerate(item.get('ページ', [])):
            text = page.get('gendaigoyaku', '')
            if not text:
                continue
            for m in RE_CITATION.finditer(text):
                raw_book = m.group(1).strip()
                # 明らかなノイズ（長すぎる・空・改行混入）を除外
                if not raw_book or len(raw_book) > 30 or '\n' in raw_book:
                    continue
                canonical = canonicalize(raw_book)
                # 周辺コンテキスト（前後 30 字）
                start = max(0, m.start() - 30)
                end = min(len(text), m.end() + 30)
                context = text[start:end].replace('\n', ' ')

                citations[canonical]['occurrences'].append({
                    'shoryoshu_idx': idx,
                    '篇名': 篇名,
                    '巻': 巻,
                    'page_idx': page_idx,
                    'context': context,
                    'context_position': m.start(),
                    'raw_form': raw_book,
                })
                if raw_book != canonical:
                    citations[canonical]['aliases'].add(raw_book)

    # entries 化（出現回数降順）
    entries = []
    for term, payload in citations.items():
        occs = payload['occurrences']
        entries.append({
            'term': term,
            'aliases': sorted(payload['aliases']),
            'occurrence_count': len(occs),
            '篇分布': sorted(set(o['shoryoshu_idx'] for o in occs)),
            'occurrences': occs,
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], e['term']))

    return entries


def main():
    entries = extract_citations()

    # 集計サマリ
    total_occ = sum(e['occurrence_count'] for e in entries)
    total_terms = len(entries)
    篇span = sorted({i for e in entries for i in e['篇分布']})

    output_doc = {
        'schema_version': '0.1',
        'category': '典故書名（citations）',
        'source_corpus': 'shoryoshu_miyasaka.json',
        'generated_at': date.today().isoformat(),
        'extraction_pattern': '『([^『』]+?)』',
        'canonicalization_dict_size': len(CANONICAL_MAP),
        'summary': {
            'unique_terms': total_terms,
            'total_occurrences': total_occ,
            'covered_shoryoshu_idx_count': len(篇span),
        },
        'entries': entries,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(output_doc, f, ensure_ascii=False, indent=2)

    print(f'== パイロット抽出完了 ==')
    print(f'unique terms: {total_terms}')
    print(f'total occurrences: {total_occ}')
    print(f'covered 篇 idx 数: {len(篇span)}')
    print(f'\n出現上位 25:')
    for e in entries[:25]:
        aliases = f' (aliases: {", ".join(e["aliases"])})' if e['aliases'] else ''
        print(f'  {e["term"]:<20s} {e["occurrence_count"]:4d} 件 / {len(e["篇分布"]):3d} 篇{aliases}')

    # 短い・1 字書名（誤抽出の疑い）と長い書名（誤抽出の疑い）を出力
    print(f'\n注意：1〜2 字の term（誤抽出疑い）:')
    short = [e for e in entries if len(e['term']) <= 2]
    for e in short[:10]:
        print(f'  「{e["term"]}」: {e["occurrence_count"]} 件 - 例 context: {e["occurrences"][0]["context"][:60]!r}')

    print(f'\n注意：10 字以上の term（誤抽出疑い）:')
    long_terms = [e for e in entries if len(e['term']) >= 10]
    for e in long_terms[:10]:
        print(f'  「{e["term"][:30]}...」: {e["occurrence_count"]} 件')


if __name__ == '__main__':
    main()

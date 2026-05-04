#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化 G2-E：横断集約ファイル生成

性霊集（list 型）と dict 型 9 著作の per-corpus index ファイル
（data/mikkyou/index_<corpus>_<category>.json）から、10 著作横断の
集約 index を生成する。

出力（7 ファイル）：
  data/mikkyou/index_terms_all.json
  data/mikkyou/index_citations_all.json
  data/mikkyou/index_kukai_works_all.json
  data/mikkyou/index_sanskrit_all.json
  data/mikkyou/index_kaimyo_jukugo_all.json
  data/mikkyou/index_persons_all.json
  data/mikkyou/index_places_all.json

スキーマ方針（v1.0）：
  per-corpus index ファイルが詳細 occurrences の正本。集約ファイルは
  「term + by_corpus 件数 + 共通メタ」のサマリ構造でファイルサイズを圧縮し、
  横断検索（kaimyo-app の 「この語は何著作で出現？」「全著作合計件数？」）
  を高速化する。

仕様：cross_index_spec.md v1.9 §18 G2-E

使い方：
    python3 _dev_references/aggregate_indices.py
"""

import json
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
MIKKYOU = ROOT / 'data' / 'mikkyou'

# ====== 10 著作（性霊集 + dict 9・2026-05-04 候補 D で bodaishinron 追加）======
ALL_CORPORA = [
    'shoryoshu_miyasaka',
    'nikyo-ron',
    'ujiji',
    'shoji-jisso',
    'sokushin-jobutsu',
    'hannya-hiken',
    'hizo-houyaku',
    'dainichikyo-sho-vol1',
    'sankyo-shiki',
    'bodaishinron',  # 2026-05-04 追加（候補 D・9 著作目の dict 型）
]


def per_corpus_filename(corpus_id: str, category: str) -> str:
    """per-corpus index ファイル名を返す。

    性霊集の kaimyo は index_shoryoshu_kaimyo.json
    dict 著作の kaimyo は index_<corpus>_kaimyo.json
    （aggregate ファイルは index_kaimyo_jukugo_all.json なので、suffix は別管理）
    """
    if corpus_id == 'shoryoshu_miyasaka':
        # 性霊集の per-corpus index は index_shoryoshu_<cat>.json
        return f'index_shoryoshu_{category}.json'
    return f'index_{corpus_id}_{category}.json'


# ====== 7 カテゴリの設定 ======
# - per_corpus_suffix: per-corpus index ファイルの suffix（_kaimyo / _terms 等）
# - aggregate_filename: 集約ファイル名
# - term_key: entry 内の term キー（term / canonical / jukugo）
# - shared_metadata_fields: 集約に保持する category 別共通メタ field 名
CATEGORIES = [
    {
        'name': 'terms',
        'per_corpus_suffix': 'terms',
        'aggregate_filename': 'index_terms_all.json',
        'term_key': 'term',
        'shared_metadata_fields': ['sanskrit', 'definition', 'kaimyo_suitable', 'kaimyo_chars'],
        'description': '密教教学用語（19 語辞書ベース）',
    },
    {
        'name': 'citations',
        'per_corpus_suffix': 'citations',
        'aggregate_filename': 'index_citations_all.json',
        'term_key': 'term',
        'shared_metadata_fields': [],
        'description': '典故書名（『〜』形式・他者著作）',
    },
    {
        'name': 'kukai_works',
        'per_corpus_suffix': 'kukai_works',
        'aggregate_filename': 'index_kukai_works_all.json',
        'term_key': 'term',
        'shared_metadata_fields': [],
        'description': '空海著作・性霊集編纂物（自著言及）',
    },
    {
        'name': 'sanskrit',
        'per_corpus_suffix': 'sanskrit',
        'aggregate_filename': 'index_sanskrit_all.json',
        'term_key': 'canonical',
        'shared_metadata_fields': ['has_diacritics'],
        'description': '梵語 IAST',
    },
    {
        'name': 'kaimyo_jukugo',
        'per_corpus_suffix': 'kaimyo',
        'aggregate_filename': 'index_kaimyo_jukugo_all.json',
        'term_key': 'jukugo',
        'shared_metadata_fields': ['source_tag', 'sanskrit_origins', 'seed_definition',
                                   'seed_sanskrit', 'kaimyo_chars'],
        'description': '戒名向け熟語（3 起点合成 + スコアリング）',
    },
    {
        'name': 'persons',
        'per_corpus_suffix': 'persons',
        'aggregate_filename': 'index_persons_all.json',
        'term_key': 'canonical',
        'shared_metadata_fields': ['subcategory', 'definition', 'aliases', 'sanskrit_canonical'],
        'description': '人名（仏教祖師・諸尊・諸子百家・天皇・貴族）',
    },
    {
        'name': 'places',
        'per_corpus_suffix': 'places',
        'aggregate_filename': 'index_places_all.json',
        'term_key': 'canonical',
        'shared_metadata_fields': ['subcategory', 'definition', 'aliases'],
        'description': '地名（寺院・山・国・王朝・聖地・宇宙論界）',
    },
]


def aggregate_one_category(cat_config: dict) -> dict:
    """1 カテゴリ分の per-corpus index を集約。"""
    name = cat_config['name']
    suffix = cat_config['per_corpus_suffix']
    term_key = cat_config['term_key']
    meta_fields = cat_config['shared_metadata_fields']

    # term → {by_corpus: {corpus: count}, metadata: {...}, all_aliases: set}
    table = defaultdict(lambda: {
        'by_corpus': {},
        'metadata': None,
        'aliases_per_corpus': defaultdict(list),
    })

    # by_corpus stats（カテゴリ別の per-corpus 集計）
    by_corpus_stats = {}
    missing_corpora = []

    for corpus_id in ALL_CORPORA:
        idx_path = MIKKYOU / per_corpus_filename(corpus_id, suffix)
        if not idx_path.exists():
            missing_corpora.append(corpus_id)
            by_corpus_stats[corpus_id] = {'unique': 0, 'occurrences': 0, 'present': False}
            continue

        with open(idx_path, 'r', encoding='utf-8') as f:
            d = json.load(f)
        s = d.get('summary', {})
        unique_count = (s.get('unique_terms') or s.get('unique_canonicals')
                        or s.get('unique_jukugo') or s.get('unique_persons')
                        or s.get('unique_places') or 0)
        by_corpus_stats[corpus_id] = {
            'unique': unique_count,
            'occurrences': s.get('total_occurrences', 0),
            'present': True,
        }

        for e in d.get('entries', []):
            t = e.get(term_key)
            if t is None:
                continue
            occ = e.get('occurrence_count', 0)
            if occ == 0:
                # 0 件 entry はスキップ（terms の dict 辞書ベース全展開のような場合）
                continue
            table[t]['by_corpus'][corpus_id] = occ

            # metadata（最初の出現時に取得・全著作で共通な field）
            if table[t]['metadata'] is None:
                meta = {f: e.get(f) for f in meta_fields if f in e}
                table[t]['metadata'] = meta

            # aliases 集約（citations: aliases / kaimyo: なし / persons,places: 共有 seed）
            if 'aliases' in e:
                a = e['aliases']
                if isinstance(a, list):
                    table[t]['aliases_per_corpus'][corpus_id] = a

    # entries 整形
    entries = []
    for term, payload in table.items():
        by_corpus = payload['by_corpus']
        total = sum(by_corpus.values())
        covered = sorted(by_corpus.keys())
        entry = {
            term_key: term,
            'total_occurrence_count': total,
            'covered_corpora_count': len(covered),
            'covered_corpora': covered,
            'by_corpus': dict(by_corpus),
        }
        # metadata（共通フィールドのみ・None 値除外）
        if payload['metadata']:
            md = {k: v for k, v in payload['metadata'].items() if v is not None and v != []}
            if md:
                entry['metadata'] = md
        entries.append(entry)

    # 出現件数降順、同件数は covered_corpora_count 降順、同位は term 昇順
    entries.sort(key=lambda e: (-e['total_occurrence_count'], -e['covered_corpora_count'], e[term_key]))

    # 統計
    multi = sum(1 for e in entries if e['covered_corpora_count'] > 1)
    max_coverage = max((e['covered_corpora_count'] for e in entries), default=0)

    doc = {
        'schema_version': '1.0',
        'category': name,
        'category_description': cat_config['description'],
        'aggregate_type': 'cross_corpus',
        'generated_at': str(date.today()),
        'source_corpora': ALL_CORPORA,
        'corpora_count': len(ALL_CORPORA),
        'corpora_with_data': sum(1 for s in by_corpus_stats.values() if s['present']),
        'missing_corpora': missing_corpora,
        'term_key': term_key,
        'note': '詳細 occurrences は per-corpus index（index_<corpus>_<cat>.json）に格納。本ファイルはサマリ集約で「全著作横断のどの語が何著作で何回出現するか」を高速参照する。',
        'summary': {
            'unique_terms_total': len(entries),
            'total_occurrences': sum(e['total_occurrence_count'] for e in entries),
            'terms_in_multiple_corpora': multi,
            'max_corpus_coverage': max_coverage,
            'by_corpus': by_corpus_stats,
        },
        'entries': entries,
    }
    return doc


def write_doc(doc: dict, filename: str) -> Path:
    out_path = MIKKYOU / filename
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


def main():
    print('=' * 70)
    print(f'aggregate_indices.py — 全 {len(CATEGORIES)} カテゴリを {len(ALL_CORPORA)} 著作から集約')
    print('=' * 70)
    grand_total_unique = 0
    grand_total_occ = 0
    for cat in CATEGORIES:
        doc = aggregate_one_category(cat)
        out_path = write_doc(doc, cat['aggregate_filename'])
        s = doc['summary']
        size = out_path.stat().st_size
        print(f"[OK] {cat['aggregate_filename']:<32s}"
              f" -> {size:>9,} bytes")
        print(f"     unique_total={s['unique_terms_total']:>5} / "
              f"total_occ={s['total_occurrences']:>5} / "
              f"multi-corpora={s['terms_in_multiple_corpora']:>4} / "
              f"max_cov={s['max_corpus_coverage']}/{doc['corpora_count']}")
        # 上位 3 を表示
        top = doc['entries'][:3]
        if top:
            tk = cat['term_key']
            top_str = ' / '.join(
                f"{e[tk]}={e['total_occurrence_count']}({e['covered_corpora_count']}著作)"
                for e in top
            )
            print(f"     top: {top_str}")
        grand_total_unique += s['unique_terms_total']
        grand_total_occ += s['total_occurrences']

    print()
    print(f'■ 全 7 カテゴリ合計：unique_terms={grand_total_unique:,} / occurrences={grand_total_occ:,}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化フェーズ B 本格抽出スクリプト（密教教学用語）

shoryoshu_miyasaka.json の全 112 篇 gendaigoyaku から
品質報告書 §2.3 で同定された 19 語の密教教学用語を辞書ベースで抽出し、
data/mikkyou/index_shoryoshu_terms.json を生成する。

仕様：cross_index_spec.md v1.0 §1 Tier 1-1 / §2.2 共通スキーマ

抽出方針：
- 19 語の正規辞書 + 本文 grep
- 長語優先（substring 二重カウントを回避）：阿字本不生 → 阿字、即身成仏 → 即身、大空三昧 → 三摩地（独立）
- 括弧書き内の梵語注記を occurrences[].sanskrit_in_context に集約（前後 30 字スコープ）
- term ごとに sanskrit（代表梵語）・definition（簡潔定義）・kaimyo_suitable・kaimyo_chars を付与
"""

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE = ROOT / 'data' / 'kukai' / 'shoryoshu_miyasaka.json'
OUTPUT = ROOT / 'data' / 'mikkyou' / 'index_shoryoshu_terms.json'

# ====== 19 語辞書（品質報告書 §2.3「密教教学用語」シート準拠）======
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
# 括弧書き内の梵語注記抽出（前後 30 字スコープで）
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


def extract_terms():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        corpus = json.load(f)

    table = defaultdict(lambda: {'occurrences': []})

    for idx, item in enumerate(corpus):
        篇名 = item.get('篇名', '')
        巻 = item.get('巻番号', '')
        for page_idx, page in enumerate(item.get('ページ', [])):
            text = page.get('gendaigoyaku', '')
            if not text:
                continue

            # 長語優先・破壊的探索（同じ字数のスペース置換で位置を保ちつつ消費）
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
                        'shoryoshu_idx': idx,
                        '篇名': 篇名,
                        '巻': 巻,
                        'page_idx': page_idx,
                        'context': context,
                        'context_position': p,
                        'sanskrit_in_context': sorted(set(sanskrit_hits)) if sanskrit_hits else [],
                    })

                    for i in range(p, p + tlen):
                        consumed[i] = ' '
                    pos = p + tlen
                    src = ''.join(consumed)

    return table


def build_entries(table):
    """辞書 19 語すべてを必ずエントリ化（0 件の語も含める）"""
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
            '篇分布': sorted(set(o['shoryoshu_idx'] for o in occs)),
            'occurrences': occs,
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], e['term']))
    return entries


def main():
    table = extract_terms()
    entries = build_entries(table)

    total_occ = sum(e['occurrence_count'] for e in entries)
    span = sorted({i for e in entries for i in e['篇分布']})

    doc = {
        'schema_version': '1.0',
        'category': '密教教学用語（mikkyo terms）',
        'source_corpus': 'shoryoshu_miyasaka.json',
        'generated_at': date.today().isoformat(),
        'extraction_strategy': '辞書ベース（19 語）+ 長語優先 substring 走査 + 周辺梵語注記抽出',
        'dictionary_size': len(TERMS_DEF),
        'summary': {
            'unique_terms': len(entries),
            'total_occurrences': total_occ,
            'covered_shoryoshu_idx_count': len(span),
            'kaimyo_suitable_count': sum(1 for e in entries if e['kaimyo_suitable']),
        },
        'entries': entries,
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)

    with open(OUTPUT, 'rb') as f:
        raw = f.read()
    nulls = len(raw) - len(raw.rstrip(b'\x00'))
    assert nulls == 0, f'NULL byte tail detected: {nulls} bytes'

    print('=' * 60)
    print('== 密教教学用語抽出完了（v1.0）==')
    print('=' * 60)
    print(f'\nunique terms: {doc["summary"]["unique_terms"]}')
    print(f'total occurrences: {doc["summary"]["total_occurrences"]}')
    print(f'covered 篇 idx 数: {doc["summary"]["covered_shoryoshu_idx_count"]}')
    print(f'戒名適合語: {doc["summary"]["kaimyo_suitable_count"]} 語')

    print(f'\n出現順:')
    print(f'{"term":<10s} {"件数":>5s}  {"篇":>3s}  {"梵語":<35s}  {"戒名":<6s} chars')
    for e in entries:
        kaimyo = '○' if e['kaimyo_suitable'] else '—'
        chars = '/'.join(e['kaimyo_chars']) if e['kaimyo_chars'] else ''
        print(f'{e["term"]:<10s} {e["occurrence_count"]:>5d}  {len(e["篇分布"]):>3d}  {e["sanskrit"]:<35s}  {kaimyo:<6s} {chars}')

    print(f'\n=== 品質報告書 §2.3 との突合 ===')
    REPORT_COUNTS = {
        '密教': 120, '大日': 110, '法界': 68, '三密': 46, '法身': 45,
        '真言': 44, '大悲': 26, '本不生': 20, '阿字': 19, '遮那': 18,
        '心王': 9, '阿字本不生': 8, '即身成仏': 6, '即身': 6, '玄機': 5,
        '智剣': 4, '三摩地': 2, '無縁慈悲': 1, '大空三昧': 1,
    }
    by_term = {e['term']: e['occurrence_count'] for e in entries}
    print(f'{"term":<10s}  本格抽出  品質報告書  差')
    for t in REPORT_COUNTS:
        a = by_term.get(t, 0)
        b = REPORT_COUNTS[t]
        diff = a - b
        mark = '✅' if diff == 0 else ('⚠ ' if abs(diff) <= 5 else '✗ ')
        print(f'  {mark} {t:<8s}  {a:>4d}    {b:>4d}      {diff:+d}')

    print(f'\n=== 抽出された周辺梵語注記サンプル（上位 5 語）===')
    for e in entries[:5]:
        sk_set = set()
        for o in e['occurrences']:
            sk_set.update(o['sanskrit_in_context'])
        if sk_set:
            print(f'  「{e["term"]}」 unique 梵語語数: {len(sk_set)} / 例:', ', '.join(sorted(sk_set))[:120])


if __name__ == '__main__':
    main()

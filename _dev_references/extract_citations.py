#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化フェーズ B 本格抽出スクリプト（典故書名）

shoryoshu_miyasaka.json の全 112 篇 gendaigoyaku から
『〜』形式の書名を抽出し、以下 2 ファイルを生成する：

- data/mikkyou/index_shoryoshu_citations.json  典故書名（他者著作の引用）
- data/mikkyou/index_shoryoshu_kukai_works.json  空海著作・性霊集編纂物等

仕様：cross_index_spec.md v1.0 §1 Tier 1-2 / §2.2 共通スキーマ
パイロット → 本格版へのリファクタ点：
  - 課題 A：『理趣経』の表記揺れ統合（CANONICAL_MAP 拡充）
  - 課題 B：『易』→『易経』正規化
  - 課題 C：『仁王経』等の括弧書き混入対処（前処理）
  - 課題 D：空海著作・性霊集編纂物の分離出力
  - 課題 E：書名でない『〜』の除外辞書
"""

import json
import re
from collections import defaultdict
from datetime import date
from pathlib import Path

# ====== パス ======
ROOT = Path(__file__).parent.parent
SOURCE = ROOT / 'data' / 'kukai' / 'shoryoshu_miyasaka.json'
OUTPUT_CITATIONS = ROOT / 'data' / 'mikkyou' / 'index_shoryoshu_citations.json'
OUTPUT_KUKAI = ROOT / 'data' / 'mikkyou' / 'index_shoryoshu_kukai_works.json'

# ====== 抽出パターン ======
# 『〜』スコープ。ネスト・行跨ぎは想定しない（性霊集の補注は単一行内が前提）
RE_CITATION = re.compile(r'『([^『』]+?)』')

# ====== 前処理 ======
# 全角括弧書き（読み仮名・補注）を除去：
#   仁王（般若波羅蜜）経 → 仁王経
#   続性霊集補闕鈔（ぞくしょうりょうしゅうほけつしょう） → 続性霊集補闕鈔
#   大広智（不空三蔵）の影（肖像）の讃 → 大広智の影の讃
RE_PAREN_ZEN = re.compile(r'（[^（）]*?）')


def preprocess(book: str) -> str:
    """書名の前処理（括弧書き除去・末尾末尾空白除去・中点除去）"""
    prev = None
    s = book
    # 入れ子はないが念のため何度かループ
    while prev != s:
        prev = s
        s = RE_PAREN_ZEN.sub('', s)
    # 中点・全角空白の前後不要要素は維持（理趣品は中点併記の異体に統合する）
    return s.strip()


# ====== 書名正規化辞書（v1.0・段階拡張）======
# 「同一典籍の異表記」を一つに統合する。
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
    # 理趣釈は別書（不空による『理趣経』の註釈）
    '大楽金剛不空真実三摩耶経般若波羅蜜多理趣釈': '理趣釈',
    '理趣釈経': '理趣釈',
    # 課題 B：易 → 易経
    '易': '易経',
    # 課題 C：仁王経 系統（前処理で括弧除去後の正規化）
    '仁王般若経': '仁王経',
    '仁王般若波羅蜜護国経': '仁王経',
    '仁王護国般若波羅蜜多経': '仁王経',
    '仁王護国般若経': '仁王経',
    '仁王般若波羅蜜経': '仁王経',  # 仁王（般若波羅蜜）経 の前処理後
}

# ====== 課題 E：書名でない『〜』の除外辞書 ======
EXCLUDE_TERMS = {
    '内典・外典',  # 仏典/外典の総称（書名ではない）
}

# ====== 課題 D：空海著作・性霊集編纂物（別ファイルへ分離）======
# 前処理後の term をキーにする。値は分類タグ。
KUKAI_WORKS = {
    # 空海請来書・著作
    '梵字悉曇字母并びに釈義': '空海著作',
    '古今文字讃': '空海請来書',
    '古今篆隷の文体': '空海請来書',
    # 性霊集自体（真済編纂）
    '続性霊集補闕鈔': '性霊集編纂物',
    # idx=12 篇名そのもの（『〜の影の讃』として本文中に自己参照される）
    '大広智の影の讃': 'idx12篇名（空海碑文）',
    '大広智不空三蔵の影の讃': 'idx12篇名（空海碑文・括弧前）',
}


def canonicalize(book: str) -> str:
    """前処理 → CANONICAL_MAP 引き当て → 正規形を返す"""
    pre = preprocess(book)
    return CANONICAL_MAP.get(pre, pre)


def classify(term: str) -> str:
    """term を 'citations'（典故書名）または 'kukai_works'（空海著作）に分類"""
    if term in KUKAI_WORKS:
        return 'kukai_works'
    return 'citations'


def extract_citations():
    with open(SOURCE, 'r', encoding='utf-8') as f:
        corpus = json.load(f)

    # term -> {'occurrences': [...], 'aliases': set}
    citations = defaultdict(lambda: {'occurrences': [], 'aliases': set()})
    kukai = defaultdict(lambda: {'occurrences': [], 'aliases': set()})

    excluded_log = []  # (idx, raw_book, context)

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

                # 前処理 + 正規化
                canonical = canonicalize(raw_book)

                # 課題 E：除外辞書
                if canonical in EXCLUDE_TERMS or preprocess(raw_book) in EXCLUDE_TERMS:
                    excluded_log.append((idx, raw_book, text[max(0, m.start()-20):m.end()+20]))
                    continue

                # 周辺コンテキスト（前後 30 字）
                start = max(0, m.start() - 30)
                end = min(len(text), m.end() + 30)
                context = text[start:end].replace('\n', ' ')

                occ = {
                    'shoryoshu_idx': idx,
                    '篇名': 篇名,
                    '巻': 巻,
                    'page_idx': page_idx,
                    'context': context,
                    'context_position': m.start(),
                    'raw_form': raw_book,
                }

                bucket = kukai if classify(canonical) == 'kukai_works' else citations
                bucket[canonical]['occurrences'].append(occ)
                if raw_book != canonical:
                    bucket[canonical]['aliases'].add(raw_book)

    return citations, kukai, excluded_log


def build_entries(table):
    entries = []
    for term, payload in table.items():
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


def build_doc(entries, *, category, schema_version='1.0', extra=None):
    total_occ = sum(e['occurrence_count'] for e in entries)
    span = sorted({i for e in entries for i in e['篇分布']})
    doc = {
        'schema_version': schema_version,
        'category': category,
        'source_corpus': 'shoryoshu_miyasaka.json',
        'generated_at': date.today().isoformat(),
        'extraction_pattern': '『([^『』]+?)』',
        'canonicalization_dict_size': len(CANONICAL_MAP),
        'exclude_dict_size': len(EXCLUDE_TERMS),
        'kukai_works_dict_size': len(KUKAI_WORKS),
        'summary': {
            'unique_terms': len(entries),
            'total_occurrences': total_occ,
            'covered_shoryoshu_idx_count': len(span),
        },
        'entries': entries,
    }
    if extra:
        doc.update(extra)
    return doc


def main():
    citations, kukai, excluded_log = extract_citations()

    cit_entries = build_entries(citations)
    kuk_entries = build_entries(kukai)

    cit_doc = build_doc(cit_entries, category='典故書名（citations・他者著作）')
    kuk_doc = build_doc(
        kuk_entries,
        category='空海著作・性霊集編纂物（kukai works）',
        extra={
            'classification_table': KUKAI_WORKS,
        },
    )

    OUTPUT_CITATIONS.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_CITATIONS, 'w', encoding='utf-8') as f:
        json.dump(cit_doc, f, ensure_ascii=False, indent=2)
    with open(OUTPUT_KUKAI, 'w', encoding='utf-8') as f:
        json.dump(kuk_doc, f, ensure_ascii=False, indent=2)

    # NULL バイト検証（CLAUDE.md 必須運用）
    for p in (OUTPUT_CITATIONS, OUTPUT_KUKAI):
        with open(p, 'rb') as f:
            raw = f.read()
        nulls = len(raw) - len(raw.rstrip(b'\x00'))
        assert nulls == 0, f'NULL byte tail detected in {p}: {nulls} bytes'

    # ====== サマリ出力 ======
    print('=' * 60)
    print('== 本格抽出完了（v1.0）==')
    print('=' * 60)
    print(f'\n[citations] 典故書名（他者著作）')
    print(f'  unique terms: {cit_doc["summary"]["unique_terms"]}')
    print(f'  total occurrences: {cit_doc["summary"]["total_occurrences"]}')
    print(f'  covered 篇 idx 数: {cit_doc["summary"]["covered_shoryoshu_idx_count"]}')

    print(f'\n[kukai_works] 空海著作・性霊集編纂物')
    print(f'  unique terms: {kuk_doc["summary"]["unique_terms"]}')
    print(f'  total occurrences: {kuk_doc["summary"]["total_occurrences"]}')
    print(f'  covered 篇 idx 数: {kuk_doc["summary"]["covered_shoryoshu_idx_count"]}')

    print(f'\n[excluded] 除外辞書ヒット件数: {len(excluded_log)}')
    for idx, raw, ctx in excluded_log[:5]:
        print(f'  idx={idx}: 「{raw}」  context={ctx[:50]!r}')

    print(f'\n[citations] 出現上位 25:')
    for e in cit_entries[:25]:
        aliases = f'  aliases={", ".join(e["aliases"])}' if e['aliases'] else ''
        print(f'  {e["term"]:<20s} {e["occurrence_count"]:4d} 件 / {len(e["篇分布"]):3d} 篇{aliases}')

    print(f'\n[kukai_works] 全エントリ:')
    for e in kuk_entries:
        aliases = f'  aliases={", ".join(e["aliases"])}' if e['aliases'] else ''
        print(f'  {e["term"]:<25s} {e["occurrence_count"]:4d} 件 / {len(e["篇分布"]):3d} 篇{aliases}')

    # 検証：残課題（パイロットからの改善確認）
    print(f'\n=== v1.0 改善検証 ===')
    cit_terms = {e['term'] for e in cit_entries}
    for chk in ['理趣経', '理趣釈', '易経', '仁王経']:
        e = next((x for x in cit_entries if x['term'] == chk), None)
        if e:
            print(f'  ✅ 『{chk}』: {e["occurrence_count"]} 件 / aliases={e["aliases"]}')
        else:
            print(f'  ⚠ 『{chk}』: 見つからず')
    for chk in ['理趣品', '易', '内典・外典']:
        if chk in cit_terms:
            print(f'  ⚠ 『{chk}』が citations に残存')
        else:
            print(f'  ✅ 『{chk}』は citations に存在しない（正規化/除外済）')

    # 1〜2 字 term（誤抽出疑い）
    print(f'\n注意：1〜2 字の term（誤抽出疑い）:')
    short = [e for e in cit_entries if len(e['term']) <= 2]
    for e in short[:10]:
        print(f'  「{e["term"]}」: {e["occurrence_count"]} 件 - 例 context: {e["occurrences"][0]["context"][:50]!r}')


if __name__ == '__main__':
    main()

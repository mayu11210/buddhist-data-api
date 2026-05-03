#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
横断索引化 G2-B（dict 型著作向け・梵語 IAST 抽出）

dict 型コーパス（弁顕密二教論・吽字義 等）の **トップレベル `gendaigoyaku`**
（単一の連続する現代語訳テキスト）から、IAST 表記の梵語を網羅抽出し、
`data/mikkyou/index_<corpus>_sanskrit.json` を生成する。

extract_sanskrit.py（性霊集・list 型 112 篇向け）の dict 型版。
正規表現・EXCLUDE_TOKENS・ALIAS_MAP・canonicalize ロジックは extract_sanskrit.py
と完全互換。

仕様：cross_index_spec.md v1.6 §15 G2-B / 旧 §9 Tier 2-4 dict 拡張

使い方：
    python3 _dev_references/extract_sanskrit_dict.py --corpus nikyo-ron.json
    python3 _dev_references/extract_sanskrit_dict.py --corpus all   # 全 dict 著作

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

# ====== 抽出パターン（extract_sanskrit.py と完全同期）======
DIACRITICS = "ĀāĪīŪūṅÑñṬṭḌḍṆṇḶḷŚśṢṣṚṛḤḥṂṃ"

RE_SANSKRIT = re.compile(
    r"[A-Za-z" + DIACRITICS + r"]"
    r"[A-Za-z" + DIACRITICS + r"\-\.’ʼ']+"
)

# ====== 除外辞書（小文字基準・extract_sanskrit.py と完全同期）======
EXCLUDE_TOKENS = {
    # メタ情報・自己参照
    'idx',
    'kindle',
    'ocr',
    'claude.md',
    # URL 断片
    'https',
    'ran',
    'hu',
    # 補注内の英語訳語
    'milk',
    'gruel',
    'brass',
    'gold',
    'elixir',
    'clavicle',
    # ローマ字日本語
    'goshin-kekkai',
    # dict 型著作で発見されるかもしれない追加ノイズ語は実行後に EXCLUDE 拡張
}

# ====== 表記揺れ統合マップ ======
ALIAS_MAP = {
    # 'vairochana': 'vairocana',  # 異綴り発見次第追加
}


def canonicalize(token: str) -> str:
    """大文字小文字統一 + ALIAS_MAP 適用"""
    lower = token.lower()
    return ALIAS_MAP.get(lower, lower)


def has_diacritic(token: str) -> bool:
    return any(c in DIACRITICS for c in token)


def corpus_id_of(filename: str) -> str:
    """nikyo-ron.json -> nikyo-ron"""
    return Path(filename).stem


def extract_one_corpus(corpus_filename: str):
    """dict 型コーパス 1 ファイルから IAST 梵語の occurrences を抽出。

    対象は **トップレベル `gendaigoyaku` のみ**。kakikudashi（書き下し漢字
    のみ・Latin 含まず）・genten（漢文原典・Latin 含まず）・text（kaimyo-app
    引用集・Latin ほぼ含まず）は対象外。
    """
    path = SOURCE_DIR / corpus_filename
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if not isinstance(data, dict):
        raise ValueError(
            f'{corpus_filename}: 想定 dict だが {type(data).__name__} だった'
        )

    text = data.get('gendaigoyaku', '') or ''
    if not text:
        return None

    cid = corpus_id_of(corpus_filename)
    table = defaultdict(lambda: {
        'occurrences': [],
        'forms': defaultdict(int),
    })

    for m in RE_SANSKRIT.finditer(text):
        tok = m.group(0)
        if len(tok) < 3:
            continue
        cl = tok.lower()
        if cl in EXCLUDE_TOKENS:
            continue
        ck = canonicalize(tok)
        p = m.start()
        ctx_start = max(0, p - 30)
        ctx_end = min(len(text), p + len(tok) + 30)
        context = text[ctx_start:ctx_end].replace('\n', ' ')

        table[ck]['occurrences'].append({
            'corpus_id': cid,
            'context': context,
            'context_position': p,
            'sanskrit_form': tok,
        })
        table[ck]['forms'][tok] += 1

    return {
        'corpus_id': cid,
        'corpus_filename': corpus_filename,
        'gendaigoyaku_length': len(text),
        'table': table,
    }


def build_doc(corpus_filename: str, gendaigoyaku_length: int, table) -> dict:
    """1 コーパス分の occurrences テーブルから索引 JSON を組み立て。"""
    cid = corpus_id_of(corpus_filename)

    entries = []
    for ck in sorted(table.keys()):
        d = table[ck]
        forms_sorted = sorted(d['forms'].items(), key=lambda x: (-x[1], x[0]))
        representative = forms_sorted[0][0]
        aliases = [{'form': f, 'count': c} for f, c in forms_sorted]
        entries.append({
            'canonical': ck,
            'representative_form': representative,
            'aliases': aliases,
            'alias_count': len(aliases),
            'has_diacritics': has_diacritic(ck) or any(has_diacritic(a['form']) for a in aliases),
            'occurrence_count': len(d['occurrences']),
            'occurrences': d['occurrences'],
        })
    entries.sort(key=lambda e: (-e['occurrence_count'], e['canonical']))

    return {
        'schema_version': '1.1',
        'category': '梵語 IAST 索引',
        'source_corpus': corpus_filename,
        'corpus_type': 'dict',
        'extraction_field': 'gendaigoyaku',
        'generated_at': str(date.today()),
        'extraction_strategy': '正規表現 IAST 抽出 + EXCLUDE_TOKENS 除外 + 小文字 canonical 集約',
        'exclude_tokens_count': len(EXCLUDE_TOKENS),
        'alias_map_size': len(ALIAS_MAP),
        'gendaigoyaku_length': gendaigoyaku_length,
        'summary': {
            'unique_terms': len(entries),  # manifest 集約用に terms と統一名
            'unique_canonicals': len(entries),
            'total_occurrences': sum(e['occurrence_count'] for e in entries),
            'with_diacritics_count': sum(1 for e in entries if e['has_diacritics']),
            'ascii_only_count': sum(1 for e in entries if not e['has_diacritics']),
            'multi_form_canonicals': sum(1 for e in entries if e['alias_count'] > 1),
        },
        'entries': entries,
    }


def write_doc(doc: dict, corpus_filename: str) -> Path:
    cid = corpus_id_of(corpus_filename)
    out_path = OUTPUT_DIR / f'index_{cid}_sanskrit.json'
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(doc, ensure_ascii=False, indent=2).encode('utf-8')
    payload = payload.rstrip(b'\x00')
    with open(out_path, 'wb') as f:
        f.write(payload)
    # 念のため再検証
    with open(out_path, 'rb') as f:
        raw = f.read()
    nul = b'\x00'
    nulls = len(raw) - len(raw.rstrip(nul))
    if nulls != 0:
        raise AssertionError(f'NULL byte tail detected in {out_path}: {nulls} bytes')
    return out_path


def process(corpus_filename: str, *, verbose=True) -> dict:
    res = extract_one_corpus(corpus_filename)
    if res is None:
        if verbose:
            print(f'[SKIP] {corpus_filename}: gendaigoyaku が空')
        return None

    doc = build_doc(corpus_filename, res['gendaigoyaku_length'], res['table'])
    out_path = write_doc(doc, corpus_filename)

    if verbose:
        s = doc['summary']
        print(f"[OK] {corpus_filename:<28s} -> {out_path.name}")
        print(f"     gendaigoyaku={doc['gendaigoyaku_length']:,} 字"
              f" / canonical={s['unique_canonicals']}"
              f" / total={s['total_occurrences']}"
              f" / IAST={s['with_diacritics_count']}"
              f" / ASCII={s['ascii_only_count']}")
        # 上位 5 語
        top = [e for e in doc['entries'] if e['occurrence_count'] > 0][:5]
        if top:
            top_str = ', '.join(f"{e['canonical']}={e['occurrence_count']}" for e in top)
            print(f"     top: {top_str}")
    return doc


def main():
    ap = argparse.ArgumentParser(description='dict 型著作向け 梵語 IAST 索引生成')
    ap.add_argument('--corpus', required=True,
                    help="対象著作 (例: nikyo-ron.json) または 'all' で全 dict 型 primary_corpus")
    args = ap.parse_args()

    targets = DICT_CORPUS_LIST if args.corpus == 'all' else [args.corpus]

    print('=' * 70)
    print(f'extract_sanskrit_dict.py — 対象 {len(targets)} 著作')
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

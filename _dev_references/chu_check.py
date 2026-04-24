#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""chu_check.py — 注 raw 貼付テキストと書き下し本文の突合ツール

ケンシンが貼り付けた Gemini OCR 番号あり版テキストと、JSON の書き下し本文
（ページ[].kakikudashi）を突き合わせ、字形が一致する項目（一致）と
字形が異なる項目（差分）に分類する。差分項目には異体字候補の検出と、
解説文傍証ルール（原則 12 例外）の自動判定候補も表示する。

Usage:
    python3 _dev_references/chu_check.py --idx 0 --input /tmp/paste.txt

Input format（Gemini OCR 番号あり版）:
    一 見出し語　解説文
    二 見出し語
    解説文…

Output:
    一致 N 項目（書き下しに完全一致）
    差分 M 項目（要判定・解説文傍証候補を併記）
"""
import argparse
import json
import re
import sys


# 異体字対応表（raw 側字 ↔ 書き下し側字）
# 巻第五までの実績＋CLAUDE.md に記載の代表例
VARIANTS = {
    '灌': '潅', '潅': '灌',
    '燈': '灯', '灯': '燈',
    '毗': '毘', '毘': '毗',
    '廈': '厦', '厦': '廈',
    '島': '嶋', '嶋': '島',
    '藪': '薮', '薮': '藪',
    '辯': '弁', '弁': '辯',
    '鳧': '鳬', '鳬': '鳧',
    '聰': '聡', '聡': '聰',
    '飧': '飡', '飡': '飧',
    '舶': '舳', '舳': '舶',
    '瀆': '涜', '涜': '瀆',
    '羲': '曦', '曦': '羲',
    '秉': '乗', '乗': '秉',
}


def extract_entries(text):
    """貼付テキストから (番号文字列, 見出し語, 解説文) を抽出。

    「番号 見出し語 解説文」「番号 見出し語\n解説文」どちらも許容。
    行頭の漢数字番号で新項目開始と判定する。
    """
    lines = text.split('\n')
    # 漢数字（一〜九・〇・十）で始まり、空白で区切られる行
    num_pattern = re.compile(r'^([一二三四五六七八九〇十]+)[\s\u3000]+(.+)$')

    entries = []
    current = None
    for line in lines:
        line = line.rstrip()
        if not line:
            # 空行は項目の境界にしない（解説文が複数行にまたがることもある）
            continue
        m = num_pattern.match(line)
        if m:
            if current:
                entries.append(current)
            num_str = m.group(1)
            rest = m.group(2)
            # 見出し語と解説文を分ける：最初の全角/半角スペースまで
            parts = re.split(r'[\s\u3000]+', rest, maxsplit=1)
            if len(parts) == 2:
                headword, explanation = parts[0], parts[1]
            else:
                headword = parts[0]
                explanation = ''
            current = {
                'num_str': num_str,
                'headword': headword,
                'explanation': explanation,
            }
        else:
            if current:
                current['explanation'] = (current['explanation'] + '\n' + line).strip()
    if current:
        entries.append(current)
    return entries


def strip_ruby(s):
    """見出し語から読み仮名（ひらがな/カタカナのみの（））と《》を除去"""
    s = re.sub(r'（[ぁ-んァ-ン・ー\s\u3000]+）', '', s)
    s = re.sub(r'《[^》]+》', '', s)
    return s.strip()


def find_match(headword, kakikudashi):
    """書き下しに見出し語が含まれるかチェック。

    Returns:
        'exact' … 完全一致
        'exact_stem' … ひらがな末尾活用を除いた語幹で一致
        ('variant', raw_ch, kak_ch, variant_str) … 異体字で一致
        ('near', nearest_str, diff_char_raw, diff_char_kak) … 1 字違い近接一致
        None … 見つからず
    """
    if headword in kakikudashi:
        return 'exact'
    # 見出し語の末尾がひらがな活用語尾（す/し/る/て/た/ぬ/ず 等）の場合、
    # 末尾のひらがな連続を除いた語幹で再検索。書き下し側で別活用（提葉凋落し）
    # として出ていても語幹一致なら OK 扱い。
    m = re.match(r'^(.*?[^\u3040-\u309f\u30a0-\u30ff])([\u3040-\u309f]+)$', headword)
    if m:
        stem = m.group(1)
        if len(stem) >= 2 and stem in kakikudashi:
            return 'exact_stem'
    # 異体字テーブルで置換して再検索
    for raw_ch, kak_ch in VARIANTS.items():
        if raw_ch in headword:
            variant = headword.replace(raw_ch, kak_ch)
            if variant in kakikudashi:
                return ('variant', raw_ch, kak_ch, variant)
    # 1 字違い近接一致検索（見出し語の長さが 2 以上）
    if len(headword) >= 2:
        for i in range(len(headword)):
            before = headword[:i]
            after = headword[i+1:]
            # before + 任意 1 字 + after が書き下しに現れるか
            if after:
                pat = re.compile(re.escape(before) + r'([^\s\u3000\n])' + re.escape(after))
            else:
                if not before:
                    continue
                pat = re.compile(re.escape(before) + r'([^\s\u3000\n])')
            m = pat.search(kakikudashi)
            if m:
                kak_ch = m.group(1)
                raw_ch = headword[i]
                if kak_ch != raw_ch:
                    nearest = before + kak_ch + after
                    return ('near', nearest, raw_ch, kak_ch)
    return None


def detect_evidence(explanation, target_char):
    """解説文傍証パターン（A/B/C）の検出。

    Returns: (hints_list, occurrence_count)
    """
    hints = []
    count = explanation.count(target_char)

    # パターン B: 底本差の明記
    if '勝又本' in explanation or '諸本では' in explanation or '諸本に' in explanation:
        hints.append('パターン B（底本差を明記）')

    # パターン C: 『書名』引用中に target_char
    for m in re.finditer(r'『[^』]*』', explanation):
        if target_char in m.group(0):
            hints.append(f'パターン C（典故引用「{m.group(0)[:20]}…」内に「{target_char}」）')
            break
    # 「」引用中も検査
    for m in re.finditer(r'「[^」]*」', explanation):
        if target_char in m.group(0):
            hints.append(f'パターン C（引用「{m.group(0)[:20]}…」内に「{target_char}」）')
            break

    # パターン A: 字義を論じる定型
    pattern_a = re.compile(
        re.escape(target_char) +
        r'(は|を|、|という|をもって|の意|也)'
    )
    if pattern_a.search(explanation):
        hints.append(f'パターン A（「{target_char}」を字義的に論じる）')

    return hints, count


def process(idx, input_path, json_path):
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)
    if not (0 <= idx < len(data)):
        print(f'ERROR: idx {idx} 範囲外（0〜{len(data)-1}）', file=sys.stderr)
        sys.exit(1)
    entry = data[idx]
    title = entry.get('篇名', '?')
    kan = entry.get('巻番号', '?')
    kakikudashi = '\n'.join(pg.get('kakikudashi', '') for pg in entry.get('ページ', []))

    with open(input_path, encoding='utf-8') as f:
        raw_text = f.read()

    entries = extract_entries(raw_text)

    print(f'=== idx={idx} {kan}「{title}」注 突合結果 ===')
    print(f'書き下し文字数: {len(kakikudashi)}')
    print(f'貼付項目数: {len(entries)}')
    print()

    matches = []
    diffs = []
    for e in entries:
        hw_clean = strip_ruby(e['headword'])
        e['hw_clean'] = hw_clean
        result = find_match(hw_clean, kakikudashi)
        e['match_result'] = result
        if result in ('exact', 'exact_stem'):
            matches.append(e)
        else:
            diffs.append(e)

    # 一致一覧
    print(f'[一致 {len(matches)} 項目]')
    for e in matches:
        tag = '' if e['match_result'] == 'exact' else '（語幹一致）'
        print(f'  {e["num_str"]} {e["headword"]} ✓{tag}')
    print()

    # 差分一覧＋判定候補
    print(f'[差分 {len(diffs)} 項目 ← 要判定]')
    for e in diffs:
        r = e['match_result']
        print(f'  {e["num_str"]} {e["headword"]}')
        target_char = None
        if r is None:
            print('    → 書き下しに一致なし（近接候補も未検出）')
        elif isinstance(r, tuple):
            kind = r[0]
            if kind == 'variant':
                _, raw_ch, kak_ch, variant = r
                print(f'    → 書き下しに「{variant}」あり（異体字 {raw_ch}→{kak_ch}）')
                target_char = raw_ch
            elif kind == 'near':
                _, nearest, raw_ch, kak_ch = r
                print(f'    → 書き下し近接「{nearest}」（1 字違い {raw_ch}→{kak_ch}）')
                target_char = raw_ch

        # 解説文傍証
        if target_char:
            hints, count = detect_evidence(e['explanation'], target_char)
            print(f'    解説文内「{target_char}」出現: {count} 回')
            if hints:
                for h in hints:
                    print(f'    ★ {h}')
                print(f'    判定候補: raw 維持（解説文傍証あり）')
            else:
                print(f'    判定候補: 書き下し準拠（解説文傍証なし）')
        print()

    # サマリー
    print('=== 概要 ===')
    print(f'一致: {len(matches)} / 差分: {len(diffs)} / 合計: {len(entries)}')


def main():
    ap = argparse.ArgumentParser(description='注 raw 貼付テキストと書き下しの突合')
    ap.add_argument('--idx', type=int, required=True, help='JSON の entry index（0 起点）')
    ap.add_argument('--input', type=str, required=True, help='貼付テキスト ファイルパス')
    ap.add_argument('--json', type=str,
                    default='data/kukai/shoryoshu_miyasaka.json',
                    help='JSON パス（既定: data/kukai/shoryoshu_miyasaka.json）')
    args = ap.parse_args()
    process(args.idx, args.input, args.json)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
fix_columns.py
──────────────────────────────────────────────────────────────────
PowerToys Text Extractor で縦書き Kindle ページを抽出すると、
列が「左から右」の順（スクリーン座標順）で並ぶ。
日本語縦書きの正しい読み順は「右から左」なので、列を逆順にする。

入力：shoryoshu_kakikudashi_raw.txt
出力：shoryoshu_kakikudashi.txt

使い方：
    python fix_columns.py

オプション：
    python fix_columns.py --dry-run   # 標準出力に表示するだけ
    python fix_columns.py --debug     # 列分割の詳細を表示

──────────────────────────────────────────────────────────────────
列の区切り方（PowerToys の出力形式に合わせて調整可能）：

PowerToys は縦書き列をどのように抽出するか：
  - パターン A: 各列が1行ずつ出力される（列 = 1行）
    例: 行1=一番左の列、行2=その右の列 → 逆順にする
  - パターン B: 各列が複数行（文字ごと1行）で出力される
    例: 行1=左列の1文字目、行2=左列の2文字目、... → 空行区切りで列を分割

このスクリプトはデフォルトでパターン A を想定し、
「=== ページ区切り ===」内の行を逆順に並べ替える。

パターン B の場合は --mode=multiline オプションを使う。
"""

import argparse
import re
import sys
from pathlib import Path

# ───── 定数 ─────────────────────────────────────────────────────
INPUT_FILE  = Path(__file__).parent / "shoryoshu_kakikudashi_raw.txt"
OUTPUT_FILE = Path(__file__).parent / "shoryoshu_kakikudashi.txt"

# コメント行・ヘッダーのパターン（スキップする行）
COMMENT_PATTERN = re.compile(r"^#{1,}")
PAGE_DELIMITER  = re.compile(r"^===")  # === ページ N === 形式

# ルビ（振り仮名）検出パターン
# ひらがな・カタカナ・長音符・スペースのみからなる短い行をルビとみなす
RUBY_PATTERN = re.compile(r"^[\u3040-\u309F\u30A0-\u30FC\s]+$")
MAX_RUBY_LEN = 10  # これ以下の文字数（strip後）をルビとみなす


# ───── ユーティリティ ────────────────────────────────────────────
def is_comment(line: str) -> bool:
    return bool(COMMENT_PATTERN.match(line))


def is_page_delimiter(line: str) -> bool:
    return bool(PAGE_DELIMITER.match(line))


def is_empty(line: str) -> bool:
    return line.strip() == ""


def is_ruby(line: str) -> bool:
    """ひらがな・カタカナのみからなる行（ルビ）かどうかを判定する（文字数制限なし）"""
    stripped = line.strip()
    if not stripped:
        return False
    return bool(RUBY_PATTERN.match(stripped))


# ───── 列逆順モード（パターン A: 1列 = 1行）────────────────────
def process_singleline_mode(lines: list[str], debug: bool = False, strip_ruby: bool = True) -> list[str]:
    """
    空行を列の区切りとし、「===」をページ区切りとして扱う。
    ページ内の列（各空行で区切られたブロック）を逆順にする。
    """
    output: list[str] = []
    current_page_header: str | None = None
    current_page_blocks: list[list[str]] = []  # ページ内の列ブロックのリスト
    current_block: list[str] = []              # 現在の列ブロック

    def flush_page():
        """現在のページを逆順にして output に書き出す"""
        nonlocal current_block
        if current_block:
            current_page_blocks.append(current_block)
            current_block = []

        if current_page_header is not None:
            output.append(current_page_header)

        if debug and current_page_blocks:
            print(f"[DEBUG] ページ内 {len(current_page_blocks)} 列 → 逆順に並べ替え",
                  file=sys.stderr)

        # 逆順にして展開
        for block in reversed(current_page_blocks):
            output.extend(block)
            output.append("")  # 列間の空行を復元

        current_page_blocks.clear()

    for raw_line in lines:
        line = raw_line.rstrip("\n")

        # コメント行はそのまま出力
        if is_comment(line):
            # ページ処理中はいったん flush
            flush_page()
            output.append(line)
            current_page_header = None
            continue

        # ページ区切り行
        if is_page_delimiter(line):
            flush_page()
            current_page_header = line
            continue

        # 空行 → 列ブロックの区切り
        if is_empty(line):
            if current_block:
                current_page_blocks.append(current_block)
                current_block = []
            # ページが始まっていない場合は空行をそのまま出力
            if current_page_header is None and not current_page_blocks:
                output.append("")
            continue

        # ルビ行（ひらがな・カタカナのみの行）→ 《》で括って残す
        if is_ruby(line):
            marked = f"《{line.strip()}》"
            if debug:
                print(f"[DEBUG] ルビ: {marked!r}", file=sys.stderr)
            current_block.append(marked)
            continue

        # 通常行 → 現在のブロックに追加
        current_block.append(line)

    # ファイル末尾の残りを flush
    flush_page()

    # 末尾の余分な空行を整理
    while output and output[-1] == "":
        output.pop()

    return output


# ───── 多行列モード（パターン B: 1文字 = 1行、空行で列分割）────
def process_multiline_mode(lines: list[str], debug: bool = False, strip_ruby: bool = True) -> list[str]:
    """
    空行を列の区切りとして扱い、列内は複数行のまま。
    ページ区切り（===）内で列を逆順にする。
    パターン A と同じロジックだが、ブロック内に複数行が入る。
    """
    # 実装は singleline と同一（ブロック内の処理が同じ）
    return process_singleline_mode(lines, debug, strip_ruby)


# ───── メイン ────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(
        description="PowerToys縦書き抽出テキストの列順を修正する"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="ファイルに書き込まず標準出力に表示する"
    )
    parser.add_argument(
        "--debug", action="store_true",
        help="列分割の詳細をステータス出力する"
    )
    parser.add_argument(
        "--mode", choices=["singleline", "multiline"], default="singleline",
        help="列分割モード（デフォルト: singleline）"
    )
    parser.add_argument(
        "--keep-ruby", action="store_true",
        help="ルビ（振り仮名）行を除去せずにそのまま残す"
    )
    parser.add_argument(
        "--input", type=Path, default=INPUT_FILE,
        help=f"入力ファイル（デフォルト: {INPUT_FILE.name}）"
    )
    parser.add_argument(
        "--output", type=Path, default=OUTPUT_FILE,
        help=f"出力ファイル（デフォルト: {OUTPUT_FILE.name}）"
    )
    args = parser.parse_args()

    # 入力ファイル読み込み
    if not args.input.exists():
        print(f"エラー: 入力ファイルが見つかりません: {args.input}", file=sys.stderr)
        sys.exit(1)

    with open(args.input, encoding="utf-8") as f:
        lines = f.readlines()

    print(f"入力: {args.input} ({len(lines)} 行)", file=sys.stderr)

    strip_ruby = not args.keep_ruby
    if strip_ruby:
        print("ルビ除去: 有効（無効にするには --keep-ruby）", file=sys.stderr)

    # 処理
    if args.mode == "multiline":
        result = process_multiline_mode(lines, args.debug, strip_ruby)
    else:
        result = process_singleline_mode(lines, args.debug, strip_ruby)

    output_text = "\n".join(result) + "\n"

    # 出力
    if args.dry_run:
        print(output_text)
    else:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(output_text)
        print(f"出力: {args.output} ({len(result)} 行)", file=sys.stderr)
        print("完了。", file=sys.stderr)


if __name__ == "__main__":
    main()

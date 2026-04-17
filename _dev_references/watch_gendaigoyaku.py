#!/usr/bin/env python3
"""
shoryoshu_gendaigoyaku_raw.txt を5分ごとに監視して、
新しい行が追加されたら逆順修正して shoryoshu_gendaigoyaku.txt に追記するスクリプト

使い方:
  python3 _dev_references/watch_gendaigoyaku.py &

終了:
  kill <PID>  または  Ctrl+C
"""

import time
import os
from datetime import datetime

BASE = os.path.dirname(os.path.abspath(__file__))
RAW_FILE    = os.path.join(BASE, "shoryoshu_gendaigoyaku_raw.txt")
OUTPUT_FILE = os.path.join(BASE, "shoryoshu_gendaigoyaku.txt")
INTERVAL    = 300  # 5分 = 300秒


def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.readlines()


def append_reversed(new_lines, output_path):
    """新規行を逆順にしてoutputに追記する。"""
    # 末尾の空行を除去してブロクとして扱う
    block = [l for l in new_lines if l.strip()]
    if not block:
        return 0
    reversed_block = list(reversed(block))
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(output_path, "a", encoding="utf-8") as f:
        f.write(f"\n===== {ts} ({len(block)}行 → 逆順) =====\n")
        for line in reversed_block:
            f.write(line if line.endswith("\n") else line + "\n")
    return len(block)


def main():
    last_count = len(read_lines(RAW_FILE))
    print(f"[{datetime.now():%H:%M:%S}] 監視開始: {RAW_FILE}")
    print(f"[{datetime.now():%H:%M:%S}] 初期行数: {last_count}行 / 間隔: {INTERVAL}秒")

    while True:
        time.sleep(INTERVAL)
        try:
            current_lines = read_lines(RAW_FILE)
            current_count = len(current_lines)

            if current_count > last_count:
                new_lines = current_lines[last_count:]
                n = append_reversed(new_lines, OUTPUT_FILE)
                print(f"[{datetime.now():%H:%M:%S}] 新規 {len(new_lines)}行検出 → 逆順{n}行を追記")
                last_count = current_count
            else:
                print(f"[{datetime.now():%H:%M:%S}] 変化なし (行数: {current_count})")

        except Exception as e:
            print(f"[{datetime.now():%H:%M:%S}] エラー: {e}")


if __name__ == "__main__":
    main()

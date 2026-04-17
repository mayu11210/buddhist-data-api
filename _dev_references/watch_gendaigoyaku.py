#!/usr/bin/env python3
"""
shoryoshu_gendaigoyaku_input.txt を5分ごとに監視して、
新しい内容が追加されたら fix_columns.py --drop-ruby を実行し
shoryoshu_gendaigoyaku.txt を更新するスクリプト。
処理完了後は input.txt を空にする（処理済みの合図）。

使い方:
  python3 _dev_references/watch_gendaigoyaku.py &

終了:
  kill <PID>  または  Ctrl+C
"""

import time
import os
import subprocess
from datetime import datetime

BASE        = os.path.dirname(os.path.abspath(__file__))
RAW_FILE    = os.path.join(BASE, "shoryoshu_gendaigoyaku_input.txt")
OUTPUT_FILE = os.path.join(BASE, "shoryoshu_gendaigoyaku.txt")
FIX_SCRIPT  = os.path.join(BASE, "fix_columns.py")
INTERVAL    = 300  # 5分 = 300秒


def get_line_count(path):
    with open(path, "r", encoding="utf-8") as f:
        return sum(1 for _ in f)


def run_fix_columns():
    """fix_columns.py --drop-ruby を実行して gendaigoyaku.txt を上書き更新する。"""
    result = subprocess.run(
        [
            "python3", FIX_SCRIPT,
            "--drop-ruby",
            "--input",  RAW_FILE,
            "--output", OUTPUT_FILE,
        ],
        capture_output=True,
        text=True,
        encoding="utf-8",
    )
    return result.returncode, result.stderr.strip()


def clear_input():
    """input.txt を空にする（処理済みの合図）。"""
    with open(RAW_FILE, "w", encoding="utf-8") as f:
        f.write("")


def main():
    last_count = get_line_count(RAW_FILE)
    print(f"[{datetime.now():%H:%M:%S}] 監視開始: {RAW_FILE}")
    print(f"[{datetime.now():%H:%M:%S}] 初期行数: {last_count}行 / 間隔: {INTERVAL}秒")

    while True:
        time.sleep(INTERVAL)
        try:
            current_count = get_line_count(RAW_FILE)

            if current_count > last_count:
                added = current_count - last_count
                print(f"[{datetime.now():%H:%M:%S}] 新規 {added}行検出 → fix_columns.py 実行中...")
                returncode, stderr = run_fix_columns()
                if returncode == 0:
                    print(f"[{datetime.now():%H:%M:%S}] 完了: {OUTPUT_FILE} を更新しました")
                    if stderr:
                        print(f"[{datetime.now():%H:%M:%S}] {stderr}")
                    clear_input()
                    print(f"[{datetime.now():%H:%M:%S}] {RAW_FILE} を空にしました（処理済み）")
                    last_count = 0
                else:
                    print(f"[{datetime.now():%H:%M:%S}] エラー (終了コード {returncode}): {stderr}")
                    last_count = current_count
            else:
                print(f"[{datetime.now():%H:%M:%S}] 変化なし (行数: {current_count})")

        except Exception as e:
            print(f"[{datetime.now():%H:%M:%S}] エラー: {e}")


if __name__ == "__main__":
    main()

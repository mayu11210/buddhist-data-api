"""
api_server/tests/conftest.py
============================

pytest フィクスチャ：

- `client` … FastAPI TestClient（in-process・高速・全テストで共有）
- `live_url` … 実 uvicorn サーバを subprocess で起動した URL（end-to-end smoke 用）

`live_url` は port 8765 を使い、起動失敗時は pytest.skip する。
"""

from __future__ import annotations

import os
import socket
import subprocess
import sys
import time
from pathlib import Path
from typing import Iterator

import pytest


REPO_ROOT = Path(__file__).resolve().parents[2]
LIVE_PORT = int(os.environ.get("BUDDHIST_API_TEST_PORT", "8765"))


@pytest.fixture(scope="session")
def client():
    """FastAPI TestClient（in-process・全テスト共有）。"""
    sys.path.insert(0, str(REPO_ROOT))
    from fastapi.testclient import TestClient

    from api_server.main import app

    with TestClient(app) as c:
        yield c


def _wait_port(host: str, port: int, timeout: float) -> bool:
    """指定 port が listen 状態になるまで待機。"""
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with socket.create_connection((host, port), timeout=0.5):
                return True
        except OSError:
            time.sleep(0.2)
    return False


@pytest.fixture(scope="session")
def live_url() -> Iterator[str]:
    """実 uvicorn を subprocess で起動した base URL を返す。

    起動失敗時は pytest.skip する（CI で uvicorn が無い等）。
    """
    cmd = [
        sys.executable, "-m", "uvicorn",
        "api_server.main:app",
        "--host", "127.0.0.1",
        "--port", str(LIVE_PORT),
        "--log-level", "warning",
    ]
    proc = subprocess.Popen(
        cmd,
        cwd=str(REPO_ROOT),
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )
    try:
        if not _wait_port("127.0.0.1", LIVE_PORT, timeout=20.0):
            stderr = (proc.stderr.read().decode("utf-8", errors="replace") if proc.stderr else "")[-2000:]
            proc.terminate()
            proc.wait(timeout=5)
            pytest.skip(f"uvicorn did not start on port {LIVE_PORT}\n{stderr}")
        yield f"http://127.0.0.1:{LIVE_PORT}"
    finally:
        proc.terminate()
        try:
            proc.wait(timeout=5)
        except subprocess.TimeoutExpired:
            proc.kill()

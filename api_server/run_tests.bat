@echo off
REM v1.9 結合テスト一括ランチャー
REM 使い方: ダブルクリック または cmd から実行

cd /d %~dp0..

echo === step 1: install test deps ===
pip install -r api_server\requirements-test.txt
if errorlevel 1 goto :err

echo.
echo === step 2: run pytest (TestClient + e2e uvicorn) ===
pytest api_server\tests -v
if errorlevel 1 goto :err

echo.
echo === all tests passed ===
exit /b 0

:err
echo.
echo === FAILED ===
exit /b 1

@echo off
REM OpenAPI スキーマを openapi.json + openapi.yaml に書き出す
REM 使い方: ダブルクリック または cmd から実行

cd /d %~dp0..
python -m api_server.export_openapi

@echo off
setlocal
chcp 65001 >nul

REM Export OpenAPI schema (json + yaml) - ASCII-only / pause-on-error
REM Usage: double-click

cd /d "%~dp0.."

echo.
echo ===== Step 1: Check Python =====
python --version
if errorlevel 1 (
    echo ERROR: python not on PATH
    goto :err
)

echo.
echo ===== Step 2: Run export_openapi =====
python -m api_server.export_openapi
if errorlevel 1 goto :err

echo.
echo ===== EXPORT OK =====
echo Files written under api_server\
dir "api_server\openapi.*"
echo.
pause
exit /b 0

:err
echo.
echo ===== FAILED =====
echo.
pause
exit /b 1

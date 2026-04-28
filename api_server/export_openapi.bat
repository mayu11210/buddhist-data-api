@echo off
setlocal
chcp 65001 >nul

REM Export OpenAPI schema (json + yaml) - py launcher / ASCII-only / pause-on-error
REM Usage: double-click
REM Updated 2026-04-28: switched from `python` to `py -m ...` because Python
REM was installed user-only without Add-to-PATH on this machine.

cd /d "%~dp0.."

echo.
echo ===== Step 1: Check py launcher =====
py --version
if errorlevel 1 (
    echo ERROR: py launcher not found
    goto :err
)

echo.
echo ===== Step 2: Run export_openapi =====
py -m api_server.export_openapi
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

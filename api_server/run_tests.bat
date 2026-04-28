@echo off
setlocal
chcp 65001 >nul

REM v1.9 integration test launcher (py launcher / ASCII-only / pause-on-error)
REM Usage: double-click
REM Updated 2026-04-28: switched from `python` to `py -m ...` because Python
REM was installed user-only without Add-to-PATH on this machine.
REM Updated 2026-04-28: Step 2 now installs BOTH requirements.txt (runtime:
REM fastapi/uvicorn/pydantic) AND requirements-test.txt (httpx/pytest/PyYAML).

cd /d "%~dp0.."

echo.
echo ===== Step 1: Check py launcher =====
py --version
if errorlevel 1 (
    echo ERROR: py launcher not found
    goto :err
)

echo.
echo ===== Step 2a: Install runtime deps (fastapi/uvicorn/pydantic) =====
py -m pip install -r "api_server\requirements.txt"
if errorlevel 1 goto :err

echo.
echo ===== Step 2b: Install test deps (httpx/pytest/PyYAML) =====
py -m pip install -r "api_server\requirements-test.txt"
if errorlevel 1 goto :err

echo.
echo ===== Step 3: Run pytest =====
py -m pytest "api_server\tests" -v
if errorlevel 1 goto :err

echo.
echo ===== ALL TESTS PASSED =====
echo.
pause
exit /b 0

:err
echo.
echo ===== FAILED =====
echo.
pause
exit /b 1

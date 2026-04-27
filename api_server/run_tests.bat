@echo off
setlocal
chcp 65001 >nul

REM v1.9 integration test launcher (ASCII-only / pause-on-error)
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
echo ===== Step 2: Install test deps =====
pip install -r "api_server\requirements-test.txt"
if errorlevel 1 goto :err

echo.
echo ===== Step 3: Run pytest =====
pytest "api_server\tests" -v
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

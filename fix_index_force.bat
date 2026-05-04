@echo off
setlocal

rem ============================================================
rem  fix_index_force.bat  (2026-05-04)
rem
rem  Force-rebuilds .git/index unconditionally, then resets to HEAD
rem  so any phantom-staged deletions are wiped.
rem
rem  Use this when fix_index.bat fails to detect corruption
rem  (its findstr check is too narrow for some failure modes
rem  where `git status` partially works but `git fsck` and
rem  `git diff` fail with "unknown index entry format").
rem
rem  ASCII-only per CLAUDE.md rule (cmd.exe Shift-JIS gotcha).
rem ============================================================

cd /d "C:\Users\user\buddhist-data-api"

echo.
echo ===== Step 1: Show current symptoms =====
echo --- git fsck ---
git fsck --no-dangling 2>&1 | findstr /R /C:"^error:" /C:"^fatal:"
echo --- git status excerpt ---
git status -s 2>&1 | findstr /R /C:"^D " /C:"^RD" /C:"corrupt" 2>&1 | findstr /N "^" | findstr /R "^[1-9]:" 2>&1
echo.

echo ===== Step 2: Remove stale locks (if present) =====
if exist ".git\index.lock"           del /f /q ".git\index.lock"
if exist ".git\HEAD.lock"            del /f /q ".git\HEAD.lock"
if exist ".git\index.stash.102"      del /f /q ".git\index.stash.102"
if exist ".git\index.stash.102.lock" del /f /q ".git\index.stash.102.lock"
echo Locks cleaned.
echo.

echo ===== Step 3: FORCE delete .git\index (no detection check) =====
if exist ".git\index" (
    del /f /q ".git\index"
    if exist ".git\index" (
        echo ERROR: failed to delete .git\index
        goto :end
    )
    echo Deleted .git\index
) else (
    echo .git\index not found (already gone).
)
echo.

echo ===== Step 4: Rebuild index from HEAD tree =====
git read-tree HEAD
if errorlevel 1 (
    echo ERROR: git read-tree HEAD failed.
    goto :end
)
echo Index rebuilt from HEAD.
echo.

echo ===== Step 5: Refresh index against working tree =====
git update-index --refresh > nul 2>&1
echo done.
echo.

echo ===== Step 6: Sanity checks =====
echo --- git fsck ---
git fsck --no-dangling 2>&1 | findstr /R /C:"^error:" /C:"^fatal:"
if errorlevel 1 (
    echo OK: git fsck clean.
)
echo --- git status (deletions should be gone) ---
git status -s
echo.
git log --oneline -3
echo.

:end
echo.
echo ##### Done #####
echo.
echo NEXT: if "git status" looks healthy and shows no "D " entries
echo for files you did not actually delete, run commit_push.bat.
echo.
echo Press any key to close.
pause > nul
endlocal

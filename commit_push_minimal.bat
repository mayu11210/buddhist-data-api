@echo off
setlocal

rem ============================================================
rem  commit_push_minimal.bat  (2026-05-04)
rem
rem  Backup commit/push for the rare case when commit_push.bat's
rem  Step 4.5 SAFETY CHECK aborts due to phantom deletions in
rem  data/mikkyou/ or other dir-level git add targets.
rem
rem  This bat stages ONLY:
rem    - CLAUDE.md
rem    - data/indices/motifs.json
rem    - commit_push.bat (the bat itself, since we added :end+pause)
rem    - fix_index_force.bat (if present)
rem    - commit_push_minimal.bat (this bat)
rem    - any *.md at repo root
rem
rem  It SKIPS dir-level adds for data/mikkyou/, data/kukai/, etc.
rem  to avoid re-introducing phantoms.
rem
rem  Reads commit message from commit_message.txt (UTF-8).
rem ============================================================

cd /d "C:\Users\user\buddhist-data-api"

echo.
echo ===== Step 1: Clean stale locks =====
if exist ".git\index.lock"           del /f /q ".git\index.lock"
if exist ".git\HEAD.lock"            del /f /q ".git\HEAD.lock"
if exist ".git\index.stash.102"      del /f /q ".git\index.stash.102"
if exist ".git\index.stash.102.lock" del /f /q ".git\index.stash.102.lock"
echo   done.

echo.
echo ===== Step 2: Reset index to HEAD =====
git reset HEAD
if errorlevel 1 (
    echo   ERROR: git reset HEAD failed.
    goto :end
)
echo   done.

echo.
echo ===== Step 3: Stage MINIMAL set of files =====
git add CLAUDE.md
git add data/indices/motifs.json
git add commit_push.bat
git add commit_push_minimal.bat
git add fix_index_force.bat
git add *.md
echo   done.

echo.
echo ===== Step 4: Show what will be committed =====
git diff --cached --stat
echo.

echo.
echo ===== Step 4.5: SAFETY CHECK =====
git status | findstr /C:"deleted:"
if not errorlevel 1 (
    echo.
    echo   ##### DANGER: deletions still staged. Aborting. #####
    echo   Even minimal staging picked up deletions.
    echo   Run fix_index_force.bat first.
    goto :end
)
echo   OK: no deletions staged.

echo.
echo ===== Step 5: Check commit_message.txt =====
if not exist "commit_message.txt" (
    echo   ERROR: commit_message.txt not found.
    goto :end
)
echo   Commit message file found. Contents:
type commit_message.txt
echo.

echo.
echo ===== Step 6: Commit =====
git commit -F commit_message.txt
if errorlevel 1 (
    echo   ERROR: git commit failed. Push skipped.
    goto :end
)

echo.
echo ===== Step 7: Push =====
git push origin main
if errorlevel 1 (
    echo   ERROR: git push failed.
    goto :end
)

echo.
echo ===== Step 8: Verify =====
git log --oneline -3
echo.
git status -s
echo.
git log origin/main..HEAD
echo   (empty above = pushed in sync with origin/main)

:end
echo.
echo ##### Done #####
echo.
echo Press any key to close.
pause > nul
endlocal

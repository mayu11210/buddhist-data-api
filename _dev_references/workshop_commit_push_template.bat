@echo off
setlocal

rem ============================================================
rem  commit_push.bat (workshop template - 2026-05-08)
rem
rem  Usage: double-click
rem
rem  Workshop variant of buddhist-data-api commit_push.bat.
rem  Each workshop (W1: buddhist-shoryoshu-workshop, W2:
rem  buddhist-doctrine-workshop) copies this file and rewrites
rem  the `cd /d` path on line below to its own Windows path.
rem
rem  ASCII-only, no Japanese (cmd.exe Shift-JIS issue).
rem  Japanese commit messages go in commit_message.txt (UTF-8)
rem  read via `git commit -F commit_message.txt`.
rem
rem  Stages:
rem    - data/indices/motifs.json    (workshop staging motifs)
rem    - CLAUDE.md
rem    - all *.md at repo root (handoff memos)
rem    - _dev_references/             (build scripts, design notes)
rem    - data/kukai/                  (reference text JSON, if any)
rem    - commit_push.bat itself
rem
rem  Safety:
rem    - Step 4.5 aborts on staged deletions (phantom-deletion guard,
rem      same as buddhist-data-api commit_push.bat).
rem ============================================================

rem ===== EDIT THIS LINE FOR EACH WORKSHOP =====
rem  W1: cd /d "C:\Users\user\buddhist-shoryoshu-workshop"
rem  W2: cd /d "C:\Users\user\buddhist-doctrine-workshop"
cd /d "C:\Users\user\<WORKSHOP_DIR>"
rem ===== END EDIT =====

echo.
echo ===== Step 1: Clean stale locks =====
if exist ".git\index.lock"           del /f /q ".git\index.lock"
if exist ".git\HEAD.lock"            del /f /q ".git\HEAD.lock"
if exist ".git\index.stash.102"      del /f /q ".git\index.stash.102"
if exist ".git\index.stash.102.lock" del /f /q ".git\index.stash.102.lock"
echo   done.

echo.
echo ===== Step 2: Reset index to HEAD (fix any mismatch) =====
git reset HEAD
if errorlevel 1 (
    echo   ERROR: git reset HEAD failed.
    goto :end
)
echo   done.

echo.
echo ===== Step 3: Stage target files (workshop variant) =====
git add data/indices/motifs.json
git add CLAUDE.md
rem ASCII-only pattern works for Japanese filenames too.
git add *.md
git add _dev_references/
git add data/kukai/
git add data/indices/
git add commit_push.bat
rem 2026-05-04 REMOVED `git add -u` (phantom-deletion incident in main repo).
rem Tracked-file modifications are covered by dir-level `git add <dir>/` above.
rem Genuine deletions go in a dedicated bat with explicit `git rm <path>`.
if errorlevel 1 (
    echo   ERROR: git add failed.
    goto :end
)
echo   done.

echo.
echo ===== Step 4: Show what will be committed =====
git diff --cached --stat
echo.

echo.
echo ===== Step 4.5: SAFETY CHECK - look for unintended deletions =====
git status | findstr /C:"deleted:"
if not errorlevel 1 (
    echo.
    echo   ##### DANGER: deletions are staged. Aborting commit. #####
    echo   This is the phantom-deletion safety guard.
    echo   If you really intended to delete files, use a dedicated bat
    echo   with explicit `git rm`. Otherwise contact Cowork.
    goto :end
)
echo   OK: no deletions staged.

echo.
echo ===== Step 5: Check commit_message.txt exists =====
if not exist "commit_message.txt" (
    echo   ERROR: commit_message.txt not found.
    echo   Please create commit_message.txt in the repo root with the commit message.
    goto :end
)
echo   Commit message file found. Contents:
type commit_message.txt
echo.

echo.
echo ===== Step 6: Commit using -F commit_message.txt =====
git commit -F commit_message.txt
if errorlevel 1 (
    echo   ERROR: git commit failed. Push skipped.
    goto :end
)

echo.
echo ===== Step 7: Push to origin/main =====
git push origin main
if errorlevel 1 (
    echo   ERROR: git push failed.
    goto :end
)

echo.
echo ===== Step 8: Verify =====
git log --oneline -3
echo.
git status
:end
echo.
echo ##### Done #####
echo.
echo Press any key to close.
pause > nul
endlocal

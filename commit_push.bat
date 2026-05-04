@echo off
setlocal

rem ============================================================
rem  commit_push.bat  (2026-04-21 new flow standard)
rem
rem  Usage: double-click
rem
rem  One-shot helper that runs commit + push in a single action.
rem  This is the DEFAULT helper for the per-screenshot cycle
rem  (OCR -> JSON reflect -> commit_message.txt -> this .bat).
rem
rem  If commit fails (no staged changes, etc.), push is skipped.
rem
rem  - Reads commit message from commit_message.txt (UTF-8)
rem    to avoid cmd.exe Shift-JIS encoding issues with Japanese.
rem  - Stages the five files we ever edit:
rem      data/kukai/shoryoshu_miyasaka.json
rem      _dev_references/shoryoshu_vol5_kindle_ruby.md
rem      _dev_references/kindle_ocr_rules.md
rem      _dev_references/shoryoshu_gendaigoyaku_raw.txt
rem      CLAUDE.md
rem    plus any new/changed files under _archive/memos/
rem    (git add is a no-op if a file has no changes.)
rem  - Commits via: git commit -F commit_message.txt
rem  - Pushes to origin/main.
rem
rem  Keep 1_commit.bat and 2_push.bat around for the rare case
rem  where commit-only or push-only is explicitly needed.
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
echo ===== Step 2: Reset index to HEAD (fix any mismatch) =====
git reset HEAD
if errorlevel 1 (
    echo   ERROR: git reset HEAD failed.
    goto :end
)
echo   done.

echo.
echo ===== Step 3: Stage target files (generic) =====
git add data/kukai/shoryoshu_miyasaka.json
git add _dev_references/shoryoshu_vol5_kindle_ruby.md
git add _dev_references/kindle_ocr_rules.md
git add _dev_references/shoryoshu_gendaigoyaku_raw.txt
git add CLAUDE.md
rem 2026-04-25 added: stage any *.md at repo root (CLAUDE.md + handoff memos).
rem ASCII-only pattern works for Japanese filenames too.
git add *.md
rem 2026-04-24 added: stage anything new under _archive/memos/
rem (e.g. retired CLAUDE.md snapshots, old handoff memos).
git add _archive/memos/
rem 2026-05-03 added: stage anything new under _archive/scripts/
rem (e.g. retired one-shot setup scripts moved to archive).
git add _archive/scripts/
rem 2026-04-24 added: stage anything new under _dev_references/
rem (e.g. chu_check.py and other helper scripts).
git add _dev_references/
rem 2026-04-27 added: stage anything new under data/mikkyou/
rem (e.g. index_shoryoshu_*.json cross-index files for phase B).
git add data/mikkyou/
rem 2026-05-01 added: stage anything new/modified under data/kukai/
rem (e.g. nikyo-ron.json gendaigoyaku additions, beyond shoryoshu_miyasaka.json).
git add data/kukai/
rem 2026-05-04 added: stage anything new/modified under data/indices/
rem (e.g. motifs.json multi-axis tagged motif index, warehouse-mode Step 2).
git add data/indices/
rem 2026-04-27 added (v1.5): stage anything new under api_server/
rem (FastAPI reference impl for kaimyo-app linkage API).
git add api_server/
rem 2026-04-28 added (v1.10): stage Render Blueprint + env example
rem (top-level new files for production deploy).
git add render.yaml
git add .env.example
git add .gitignore
rem 2026-05-04 added: stage commit-helper bats themselves at repo root
rem (commit_push.bat updates, fix_index_force.bat, commit_push_minimal.bat).
rem ASCII-only block; do NOT add Japanese comments here (cmd.exe Shift-JIS).
git add commit_push.bat
git add commit_push_minimal.bat
git add fix_index_force.bat
rem 2026-05-04 REMOVED: previously had `git add -u` to stage tracked-file
rem deletions for archive moves. It caused a phantom deletion incident on
rem 2026-05-03 (G2-A run) where Windows<->sandbox sync timing made existing
rem files briefly appear missing, triggering staged deletions of 23+ files
rem (data/mikkyou/ri.json, sa.json, lib/search.ts, package.json, etc.).
rem
rem Tracked-file modifications inside data/kukai/, data/mikkyou/,
rem _dev_references/, _archive/memos/, _archive/scripts/, api_server/ are
rem already covered by the dir-level `git add <dir>/` calls above. Genuine
rem deletions (rare, archive moves) should be handled by a dedicated bat
rem with explicit `git rm <path>` so they are intentional.
rem
rem Safety net: Step 4.5 below detects any 'deleted:' lines and aborts the
rem commit if found, preventing a repeat of the phantom-deletion incident.
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
rem Detect any 'deleted:' entries in the staged area. If found, abort
rem the commit (prevents the 2026-05-03 phantom-deletion incident from
rem repeating). To intentionally delete a tracked file, use a dedicated
rem one-shot bat with explicit `git rm <path>` instead of this generic bat.
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

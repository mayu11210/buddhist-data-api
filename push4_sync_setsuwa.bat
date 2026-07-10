@echo off
setlocal
rem ============================================================
rem  push4_sync_setsuwa.bat  (2026-07-05)
rem  Copies buddhist-data-api setsuwa.json -> kaimyo-app and
rem  verifies byte-identity (certutil SHA-256 + fc /b).
rem  GUARD: aborts if the warehouse setsuwa.json is NOT yet
rem  committed to HEAD (so we never sync an uncommitted file).
rem  Same shape as push3_sync_kaimyo.bat (motifs.json version).
rem  Run this FIRST, then run commit_setsuwa_sync.bat in kaimyo-app.
rem ============================================================
set SRC=C:\Users\user\buddhist-data-api\data\indices\setsuwa.json
set DST=C:\Users\user\kaimyo-app\data\indices\setsuwa.json

echo.
echo ===== Step 1: warehouse (buddhist-data-api) commit state =====
cd /d "C:\Users\user\buddhist-data-api"
git --no-pager log --oneline -3
echo.
echo   --- is setsuwa.json committed to HEAD? (no output below = yes) ---
git --no-pager diff --stat HEAD -- data/indices/setsuwa.json
git diff --quiet HEAD -- data/indices/setsuwa.json
if errorlevel 1 (
    echo.
    echo   ##### WARN: warehouse setsuwa.json differs from HEAD = NOT committed. #####
    echo   Commit it in the warehouse first, then re-run this. Aborting.
    goto :end
)
echo   OK: warehouse setsuwa.json == HEAD (committed).

echo.
echo ===== Step 2: confirm count 69 in HEAD blob =====
git show HEAD:data/indices/setsuwa.json > "%TEMP%\wh_setsuwa.json"
findstr /C:"\"count\": 69" "%TEMP%\wh_setsuwa.json" >nul
if errorlevel 1 (
    echo   ##### WARN: "count": 69 NOT found in HEAD. Aborting. #####
    del /q "%TEMP%\wh_setsuwa.json" 2>nul
    goto :end
)
echo   OK: count 69 in HEAD.
del /q "%TEMP%\wh_setsuwa.json" 2>nul

echo.
echo ===== Step 3: copy SRC -^> DST =====
copy /Y "%SRC%" "%DST%"
if errorlevel 1 ( echo   ERROR: copy failed & goto :end )

echo.
echo ===== Step 4: SHA-256 of both =====
certutil -hashfile "%SRC%" SHA256
certutil -hashfile "%DST%" SHA256

echo.
echo ===== Step 5: binary compare (fc /b) =====
fc /b "%SRC%" "%DST%" >nul
if errorlevel 1 (
    echo   ##### MISMATCH: SRC and DST differ. Aborting. #####
    goto :end
)
echo   OK: SRC and DST are byte-identical.

echo.
echo ============================================================
echo  SYNC COPY DONE. Next: run commit_setsuwa_sync.bat in
echo  kaimyo-app to commit + push the synced setsuwa.json and
echo  the theme-matching implementation.
echo ============================================================

:end
echo.
echo Done. Press any key to close.
pause >nul

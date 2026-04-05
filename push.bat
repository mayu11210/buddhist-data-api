@echo off
cd /d "%~dp0"
git add .
git commit -m "データ更新"
git push origin main
echo プッシュ完了
pause

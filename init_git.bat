@echo off
cd /d "%~dp0"
echo Gitを初期化してGitHubにプッシュします...
git init
git add .
git commit -m "仏教データ保管庫 初回コミット"
git branch -M main
git remote add origin https://github.com/mayu11210/buddhist-data-api.git
git push -u origin main
echo.
echo 完了しました！
pause

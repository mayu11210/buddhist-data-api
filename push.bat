@echo off
cd /d %~dp0
echo GitHubにプッシュしています...
git push origin main
if %errorlevel% == 0 (
    echo.
    echo プッシュ完了しました。
) else (
    echo.
    echo エラーが発生しました。上のメッセージを確認してください。
)
pause

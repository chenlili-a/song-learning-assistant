@echo off
:: Enable UTF-8 encoding in cmd window
chcp 65001 > nul
echo ==============================================
echo   正在啟動「雙語歌唱練習助手 - 新增歌曲精靈」...
echo ==============================================
python "%~dp0add_song_wizard.py"

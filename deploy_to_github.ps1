# -*- coding: utf-8 -*-
# Set encoding to UTF-8 for PowerShell console
$OutputEncoding = [System.Text.Encoding]::UTF8
[Console]::InputEncoding = [System.Text.Encoding]::UTF8
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8

Write-Output "=================================================="
Write-Output "       雙語歌唱練習助手 - 一鍵發佈網站精靈         "
Write-Output "=================================================="

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$htmlPath = Join-Path $scriptDir "song_practice_helper.html"
$indexPath = Join-Path $scriptDir "index.html"

# 1. Copy song_practice_helper.html to index.html for GitHub Pages root resolution
if (Test-Path $htmlPath) {
    Copy-Item $htmlPath $indexPath -Force
    Write-Output "✓ 已生成適合部署的網頁主檔 (index.html)"
} else {
    Write-Output "❌ 找不到網頁檔案：$htmlPath"
    Read-Host "請按 Enter 鍵關閉..."
    exit
}

# 2. Check if git is initialized
if (!(Test-Path (Join-Path $scriptDir ".git"))) {
    Write-Output "正在本機建立 Git 版本庫..."
    Set-Location $scriptDir
    git init
    git branch -M main
} else {
    Set-Location $scriptDir
}

# 3. Add and commit files
Write-Output "正在將網頁檔案加入暫存區..."
git add index.html song_practice_helper.html add_song_wizard.py how_to_add_songs.md .gitignore deploy_to_github.ps1
git commit -m "Deploy song practice assistant to GitHub Pages"

# 4. Check remote origin
$remote = git remote get-url origin 2>$null
if (!$remote) {
    Write-Output "`n=================================================="
    Write-Output " 請到您的 GitHub (https://github.com/) 建立一個新倉庫"
    Write-Output " 倉庫名稱建議使用: song-learning-assistant"
    Write-Output " 建立完畢後，請複製它的 HTTPS 網址。"
    Write-Output "=================================================="
    
    $repoUrl = Read-Host "請在此處貼上您的 GitHub 倉庫網址 (例如 https://github.com/您的帳號/倉庫名.git)"
    $repoUrl = $repoUrl.Trim()
    
    if (!$repoUrl) {
        Write-Output "❌ 網址不能為空，部署取消。"
        Read-Host "請按 Enter 鍵關閉..."
        exit
    }
    
    git remote add origin $repoUrl
    Write-Output "✓ 已成功連結遠端倉庫！"
} else {
    Write-Output "✓ 已偵測到已連結的遠端倉庫: $remote"
}

# 5. Push to GitHub
Write-Output "`n正在將網頁上傳至 GitHub (可能需要您登入帳號授權)..."
git push -u origin main -f

if ($LASTEXITCODE -eq 0) {
    Write-Output "`n=================================================="
    Write-Output " 🎉 恭喜您！網頁已成功上傳至 GitHub！"
    Write-Output "=================================================="
    Write-Output " 📢 最後一步：開啟您的網站"
    Write-Output " 1. 開啟您的 GitHub 倉庫網頁。"
    Write-Output " 2. 點擊頂部的 [Settings] (設定)。"
    Write-Output " 3. 點選左側選單的 [Pages]。"
    Write-Output " 4. 在 Build and deployment 下方的 [Branch] 選單："
    Write-Output "    將 [None] 改為 [main] (或是主分支)，右側保持 [/ (root)]，點擊 [Save] (儲存)。"
    Write-Output " 5. 等待 1-2 分鐘後，您的專屬網站就正式開通了！"
    Write-Output "    您的網址將會是: https://您的帳號.github.io/倉庫名稱/"
    Write-Output "=================================================="
} else {
    Write-Output "`n❌ 上傳失敗。請確認您的 GitHub 帳號已登入且擁有該倉庫的寫入權限。"
}

Read-Host "請按 Enter 鍵關閉..."

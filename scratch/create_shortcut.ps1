$WshShell = New-Object -ComObject WScript.Shell
$desktopPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath("Desktop"), "雙語歌唱學習助手.lnk")
$Shortcut = $WshShell.CreateShortcut($desktopPath)
$Shortcut.TargetPath = "C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4\song_practice_helper.html"
$Shortcut.Description = "開啟雙語歌唱與朗讀自主學習助手"
$Shortcut.WorkingDirectory = "C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4"
$Shortcut.Save()
Write-Output "Shortcut created at: $desktopPath"

$WshShell = New-Object -ComObject WScript.Shell
$desktopPath = [System.IO.Path]::Combine([System.Environment]::GetFolderPath("Desktop"), "Song_Practice_Helper.lnk")
$Shortcut = $WshShell.CreateShortcut($desktopPath)
$Shortcut.TargetPath = "C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4\song_practice_helper.html"
$Shortcut.Description = "Open Song Practice Helper"
$Shortcut.WorkingDirectory = "C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4"
$Shortcut.Save()
Write-Output "Shortcut created at: $desktopPath"

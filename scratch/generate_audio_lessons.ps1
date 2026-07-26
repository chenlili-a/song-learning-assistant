Add-Type -AssemblyName System.Speech

# Define target paths
$basePath = "C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4"
$agPath = Join-Path $basePath "amazing_grace_pronunciation.wav"
$sgPath = Join-Path $basePath "the_salley_gardens_pronunciation.wav"
$slPath = Join-Path $basePath "santa_lucia_pronunciation.wav"

function Generate-Lesson {
    param(
        [string]$outputPath,
        [string]$introText,
        [string[]]$lines,
        [int]$rate = -3
    )
    $synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
    $synth.SelectVoice("Microsoft Zira Desktop")
    $synth.Rate = $rate
    $synth.SetOutputToWaveFile($outputPath)
    
    $prompt = New-Object System.Speech.Synthesis.PromptBuilder
    
    # Add intro at normal speed
    $synth.Rate = 0
    $prompt.AppendText($introText)
    $prompt.AppendBreak([TimeSpan]::FromSeconds(2.0))
    
    # Speak each line with a pause for the user to repeat
    foreach ($line in $lines) {
        $prompt.AppendText($line)
        $prompt.AppendBreak([TimeSpan]::FromSeconds(3.5))
    }
    
    $synth.Speak($prompt)
    $synth.Dispose()
    Write-Output "Generated: $outputPath"
}

# 1. Amazing Grace
$agLines = @(
    "Amazing grace! How sweet the sound",
    "That saved a wretch like me!",
    "I once was lost, but now am found;",
    "Was blind, but now I see.",
    
    "'Twas grace that taught my heart to fear,",
    "And grace my fears relieved;",
    "How precious did that grace appear",
    "The hour I first believed.",
    
    "Through many dangers, toils and snares,",
    "I have already come;",
    "'Tis grace hath brought me safe thus far,",
    "And grace will lead me home.",
    
    "When we've been there ten thousand years,",
    "Bright shining as the sun,",
    "We've no less days to sing God's praise",
    "Than when we first begun."
)
Generate-Lesson -outputPath $agPath -introText "Amazing Grace. Line by line pronunciation practice. Please repeat after each line." -lines $agLines -rate -3

# 2. Down by the Salley Gardens
$sgLines = @(
    "Down by the salley gardens my love and I did meet;",
    "She passed the salley gardens with little snow-white feet.",
    "She bid me take love easy, as the leaves grow on the tree;",
    "But I, being young and foolish, with her would not agree.",
    
    "In a field by the river my love and I did stand,",
    "And on my leaning shoulder she laid her snow-white hand.",
    "She bid me take life easy, as the grass grows on the weirs;",
    "But I was young and foolish, and now am full of tears."
)
Generate-Lesson -outputPath $sgPath -introText "Down by the Salley Gardens. Line by line pronunciation practice. Please repeat after each line." -lines $sgLines -rate -3

# 3. Santa Lucia (Using English voice Zira, slow speed)
$slLines = @(
    "Sul mare luccica l’astro d’argento.",
    "Placida è l’onda, prospero è il vento.",
    "Venite all’agile barchetta mia,",
    "Santa Lucia! Santa Lucia!",
    
    "Con questo zeffiro così soave,",
    "Oh, com’è bello star sulla nave!",
    "Su passeggeri, venite via!",
    "Santa Lucia! Santa Lucia!"
)
Generate-Lesson -outputPath $slPath -introText "Santa Lucia. Line by line pronunciation practice. Please repeat after each line." -lines $slLines -rate -3

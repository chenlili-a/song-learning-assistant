import os
import urllib.request
import urllib.parse
import time

# Create directories
dest_dir = r"C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4\audio"
os.makedirs(dest_dir, exist_ok=True)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

songs_data = {
    "ag": {
        "lang": "en",
        "lines": [
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
        ]
    },
    "sg": {
        "lang": "en",
        "lines": [
            "Down by the salley gardens my love and I did meet;",
            "She passed the salley gardens with little snow-white feet.",
            "She bid me take love easy, as the leaves grow on the tree;",
            "But I, being young and foolish, with her would not agree.",
            "In a field by the river my love and I did stand,",
            "And on my leaning shoulder she laid her snow-white hand.",
            "She bid me take life easy, as the grass grows on the weirs;",
            "But I was young and foolish, and now am full of tears."
        ]
    },
    "sl": {
        "lang": "it",  # Italian!
        "lines": [
            "Sul mare luccica l’astro d’argento.",
            "Placida è l’onda, prospero è il vento.",
            "Venite all’agile barchetta mia,",
            "Santa Lucia! Santa Lucia!",
            "Con questo zeffiro così soave,",
            "Oh, com’è bello star sulla nave!",
            "Su passeggeri, venite via!",
            "Santa Lucia! Santa Lucia!"
        ]
    }
}

for prefix, info in songs_data.items():
    lang = info["lang"]
    for i, line in enumerate(info["lines"]):
        filename = f"{prefix}_{i+1}.mp3"
        filepath = os.path.join(dest_dir, filename)
        
        # Clean text a bit for the TTS engine
        clean_line = line.replace("’", "'").replace("‘", "'")
        encoded_text = urllib.parse.quote(clean_line)
        url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_text}&tl={lang}&client=tw-ob"
        
        print(f"Downloading {filename} for line: '{line}'...")
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req) as response:
                with open(filepath, 'wb') as f:
                    f.write(response.read())
            # Sleep slightly to avoid rate limit
            time.sleep(0.5)
        except Exception as e:
            print(f"Failed to download {filename}: {e}")

print("All downloads finished.")

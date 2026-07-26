import urllib.request
import json

url = "https://archive.org/metadata/favoritehymns01_1606_librivox"
try:
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode('utf-8'))
        files = data.get("files", [])
        for f in files:
            name = f.get("name", "")
            if "amazing" in name.lower() and name.endswith(".mp3"):
                print(f"Found Amazing Grace MP3: {name}")
                print(f"Direct download link: https://archive.org/download/favoritehymns01_1606_librivox/{name}")
except Exception as e:
    print(f"Error: {e}")

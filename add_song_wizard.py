# -*- coding: utf-8 -*-
import os
import re
import urllib.request
import urllib.parse
import json

def main():
    print("=========================================")
    # Welcome banner in Chinese
    print("        雙語歌唱練習助手 - 新增歌曲精靈        ")
    print("=========================================")
    
    # 1. Get current path settings
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Assuming HTML is in the same folder as this script
    html_path = os.path.join(script_dir, "song_practice_helper.html")
    audio_dir = os.path.join(script_dir, "audio")
    
    if not os.path.exists(html_path):
        print(f"⚠️ 找不到網頁檔案：{html_path}")
        print("請確保此腳本與 song_practice_helper.html 放置在同一個資料夾中！")
        input("按任意鍵結束...")
        return

    # 2. Collect song metadata
    song_id = input("1. 請輸入新歌曲英文代號 (如 'yesterday'): ").strip().lower()
    if not re.match(r"^[a-z0-9_]+$", song_id):
        print("❌ 歌曲代號只能包含英文小寫、數字與底線！")
        return
        
    title = input("2. 請輸入歌曲標題 (如 'Yesterday (昨日)'): ").strip()
    desc = input("3. 請輸入歌曲簡介 (如 '披頭四樂團經典，流傳半世紀的憂傷民謠。'): ").strip()
    
    tempo_input = input("4. 請輸入歌曲速度 BPM (如 75，直接 Enter 預設為 80): ").strip()
    tempo = int(tempo_input) if tempo_input.isdigit() else 80
    
    lang = input("5. 請輸入歌詞發音語系代碼 (英文為 en, 義大利文為 it, 法文為 fr, 德文為 de，直接 Enter 預設為 en): ").strip().lower()
    if not lang:
        lang = "en"
        
    video_url = input("6. 請輸入 YouTube 真人教唱/示範影片網址 (如 https://www.youtube.com/watch?v=xxxx): ").strip()
    if not video_url:
        video_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(title)}+唱歌教學"
        
    video_text = f"開啟《{title.split('(')[0].strip()}》真人示範影片"
    yt_search_url = f"https://www.youtube.com/results?search_query={urllib.parse.quote(title.split('(')[0].strip())}+唱歌教學"
    yt_search_text = f"在 YouTube 搜尋《{title.split('(')[0].strip()}》教唱"

    # 3. Collect lines
    lines = []
    line_idx = 1
    print("\n--- 請開始輸入逐句歌詞 ---")
    print("提示：若輸入完畢，直接在「英文/原文歌詞」欄位按 Enter 鍵即可結束。")
    
    while True:
        print(f"\n【第 {line_idx} 句】")
        text = input("▶ 英文/原文歌詞: ").strip()
        if not text:
            break
            
        translation = input("▶ 中文翻譯: ").strip()
        ipa = input("▶ 國際音標 IPA (可直接 Enter 跳過): ").strip()
        pinyin = input("▶ 中文諧音/拼音 (可直接 Enter 跳過): ").strip()
        tips = input("▶ 歌唱指導提示 (如：此句最高音請用頭聲唱出，可直接 Enter 跳過): ").strip()
        
        # Audio file path to be saved
        audio_filename = f"audio/{song_id}_{line_idx}.mp3"
        
        lines.append({
            "text": text,
            "translation": translation,
            "ipa": ipa,
            "pinyin": pinyin,
            "audio": audio_filename,
            "tips": f"<b>教唱：</b>{tips}" if tips else "",
            "notes": [] # MIDI melody notes can be manually added in HTML if desired
        })
        line_idx += 1

    if not lines:
        print("❌ 未輸入任何歌詞，取消新增。")
        return

    # 4. Download Google TTS audio files
    print("\n正在為您下載發音朗讀音檔...")
    if not os.path.exists(audio_dir):
        os.makedirs(audio_dir)
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    for idx, line in enumerate(lines):
        local_audio_path = os.path.join(script_dir, "audio", f"{song_id}_{idx+1}.mp3")
        q = urllib.parse.quote(line["text"])
        tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl={lang}&q={q}"
        
        print(f"  → 正在下載第 {idx+1}/{len(lines)} 句發音...")
        try:
            req = urllib.request.Request(tts_url, headers=headers)
            with urllib.request.urlopen(req) as response:
                with open(local_audio_path, 'wb') as out_file:
                    out_file.write(response.read())
        except Exception as e:
            print(f"  ⚠️ 第 {idx+1} 句下載失敗: {e} (您的本機網頁依然能使用，但該句發音可能會無法播放)")

    # 5. Inject into song_practice_helper.html
    print("\n正在將新歌曲資料寫入網頁...")
    try:
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        # Construct the new song object content
        song_object = {
            "title": title,
            "desc": desc,
            "tempo": tempo,
            "videoUrl": video_url,
            "videoText": video_text,
            "ytSearchUrl": yt_search_url,
            "ytSearchText": yt_search_text,
            "lines": lines
        }
        
        # Serialize to formatted JS object
        song_js_str = json.dumps(song_object, ensure_ascii=False, indent=12)
        # Fix indentation formatting
        song_js_str = song_js_str.replace("{\n            ", "{\n            ")
        
        # We need to find the ending brace of the songs dictionary in HTML
        # In the modified HTML, it ends with:
        #             ]
        #         }
        #     };
        target_ending = "            ]\n        }\n    };"
        new_ending = f"            ]\n        }},\n        {song_id}: {song_js_str}\n    }};"
        
        if target_ending in html_content:
            new_html_content = html_content.replace(target_ending, new_ending)
        else:
            # Fallback for slightly different line endings (Windows/Unix)
            target_ending_rn = "            ]\r\n        }\r\n    };"
            new_ending_rn = f"            ]\r\n        }},\r\n        {song_id}: {song_js_str}\r\n    }};"
            if target_ending_rn in html_content:
                new_html_content = html_content.replace(target_ending_rn, new_ending_rn)
            else:
                print("❌ 找不到網頁中的歌曲資料插入點，請確認 HTML 結構未被更動過。")
                return

        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_html_content)
            
        # Create a new Tab button dynamically in HTML so the user can click it!
        # The tab container in HTML looks like:
        # <button class="tab-btn active" onclick="switchSong('ag')">Amazing Grace</button>
        # <button class="tab-btn" onclick="switchSong('sg')">The Salley Gardens</button>
        # <button class="tab-btn" onclick="switchSong('sl')">Santa Lucia</button>
        # We need to add the new button:
        # <button class="tab-btn" onclick="switchSong('[song_id]')">[title]</button>
        
        # Let's read the updated HTML content
        with open(html_path, "r", encoding="utf-8") as f:
            html_content = f.read()
            
        short_title = title.split("(")[0].strip()
        tab_target = f'<button class="tab-btn" onclick="switchSong(\'sl\')">Santa Lucia</button>'
        tab_replacement = tab_target + f'\n            <button class="tab-btn" onclick="switchSong(\'{song_id}\')">{short_title}</button>'
        
        if tab_target in html_content:
            html_content = html_content.replace(tab_target, tab_replacement)
        else:
            tab_target_rn = f'<button class="tab-btn" onclick="switchSong(\'sl\')">Santa Lucia</button>'
            tab_replacement_rn = tab_target_rn + f'\r\n            <button class="tab-btn" onclick="switchSong(\'{song_id}\')">{short_title}</button>'
            html_content = html_content.replace(tab_target_rn, tab_replacement_rn)
            
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print("\n🎉 成功！新歌曲已成功加入您的學習助手！")
        print(f"現在，雙擊桌面上的「Song_Practice_Helper」捷徑開啟網頁，")
        print(f"您將會看到多出一個《{short_title}》的選單頁籤！")
    except Exception as e:
        print(f"❌ 寫入網頁檔案時發生錯誤: {e}")
        
    input("\n請按 Enter 鍵關閉此視窗...")

if __name__ == "__main__":
    main()

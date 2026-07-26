# 如何新增更多歌曲到您的「歌唱自主學習助手」

為了讓您（即使是電腦新手）以後可以隨時加入任何新歌，我為您打包了一個**「新增歌曲精靈（技能包）」**！
您**完全不需要手動修改任何網頁程式碼**，只需按照以下方法操作即可。

---

## 🚀 快速使用方法

我已經在您的**電腦桌面上**建立了一個名為 **`Add_New_Song`** 的捷徑/批次檔。

1. 到電腦桌面雙擊 **`Add_New_Song`** 圖示。
2. 系統會彈出一個黑色視窗（如下圖所示的引導畫面），一步步詢問您歌曲資訊：
   * **歌曲代號**：輸入英文小寫，例如 `yesterday`。
   * **歌曲標題**：例如 `Yesterday (昨日)`。
   * **歌曲簡介**：例如 `披頭四樂團經典民謠。`。
   * **發音語言代碼**：英文打 `en`、日文打 `ja`、法文打 `fr`、韓文打 `ko` 等。
   * **YouTube 網址**：您可以直接貼上網址，如果沒有也可以直接按 Enter，程式會自動幫您設定為 YouTube 搜尋網址！
3. **輸入歌詞**：
   * 程式會一句一句詢問您「原文歌詞」、「中文翻譯」、「國際音標（可跳過）」與「中文諧音拼音（可跳過）」、「歌唱秘笈（可跳過）」。
   * **結束輸入**：當全部歌詞輸入完畢後，在詢問原文歌詞時**直接按下 Enter 鍵**即可。
4. **自動生成**：
   * 程式會自動連線 Google 翻譯，下載**整首歌每一句的真人發音朗讀檔**，並儲存到您的本機 `audio/` 資料夾中。
   * 程式會自動將新歌曲的資料庫注入到網頁中，並在網頁頂端**自動新增一個專屬的點選頁籤**！

完成後，您只需重新整理網頁，就會發現您的新歌曲已經加入完畢，可以直接點擊播放、看拼音與朗讀練習了！

---

## 🛠️ 技術原理與架構（日後手動微調用）

如果您日後想微調歌曲內容，可以參考本系統的檔案結構：

### 1. 檔案位置
所有檔案皆存放在您的專案目錄：
`C:\Users\Chen\.gemini\antigravity\brain\ad2b16ce-4b04-4380-84e8-bf394ff8a5e4\`

*   **[song_practice_helper.html](file:///C:/Users/Chen/.gemini/antigravity/brain/ad2b16ce-4b04-4380-84e8-bf394ff8a5e4/song_practice_helper.html)**：主網頁檔案。
*   **[add_song_wizard.py](file:///C:/Users/Chen/.gemini/antigravity/brain/ad2b16ce-4b04-4380-84e8-bf394ff8a5e4/add_song_wizard.py)**：背後運行的 Python 新增精靈腳本。
*   **[audio/](file:///C:/Users/Chen/.gemini/antigravity/brain/ad2b16ce-4b04-4380-84e8-bf394ff8a5e4/audio)**：存放所有發音朗讀音檔的資料夾。

### 2. 網頁中的資料庫結構
在 `song_practice_helper.html` 檔案底部的 `<script>` 區塊中，包含了一個名為 `songs` 的 JavaScript 物件。它的結構如下：

```javascript
const songs = {
    // 歌曲代號
    ag: {
        title: "Amazing Grace (奇異恩典)",
        desc: "英國經典聖詩，感人至深的救贖與恩典之歌。",
        tempo: 85,
        videoUrl: "https://www.youtube.com/watch?v=78k5K4aY35o", // 影片網址
        videoText: "開啟《Amazing Grace》推薦教唱影片",
        ytSearchUrl: "https://www.youtube.com/results?search_query=Amazing+Grace+唱歌教學",
        ytSearchText: "在 YouTube 搜尋《Amazing Grace》教唱",
        lines: [
            { 
                text: "Amazing grace! How sweet the sound", // 原文
                translation: "奇異恩典！何等甘甜的歌聲", // 翻譯
                ipa: "[əˈmeɪzɪŋ ɡreɪs / haʊ swiːt ðə saʊnd]", // 音標
                pinyin: "阿妹晶 葛雷斯！豪 絲威特 德 桑德", // 諧音拼音
                audio: "audio/ag_1.mp3", // 音檔位置
                tips: "<b>教唱：</b>弱起拍，要輕輕地發聲...", // 歌唱秘笈
                notes: [ // 旋律音高 (可省略)
                    {midi: 62, duration: 1.0}, 
                    {midi: 67, duration: 2.0}
                ]
            }
        ]
    }
};
```

如果您需要微調發音或拼音，也可以直接用筆記本或 Markdown 編輯器打開網頁檔案，搜尋您的歌曲標題，手動更改裡面的文字即可！

# 🎵 雙語歌唱學習助手 - 歌曲資料庫與鋼琴音符對照表 (V17)

本文件整理了網頁中所有的歌曲資料庫，包含歌詞、英文/義大利文音標、中文諧音，以及每一句對應的 **實體鋼琴音符（聽旋律功能）**。
您可以將此文件提供給音樂老師、琴友或程式開發人員，他們可以直接修改下方 `notes` 欄位中的音符，修改完成後，AI 隨時可以幫您寫入網頁中！

---

## 🎹 MIDI 音符與唱名快速對照表
在資料庫中，`midi` 代表音高，數字越大音越高：
*   **60**: C5 (中音 Do)
*   **62**: D5 (中音 Re)
*   **64**: E5 (中音 Mi)
*   **65**: F5 (中音 Fa)
*   **67**: G5 (中音 Sol)
*   **69**: A5 (中音 La)
*   **71**: B5 (中音 Si)
*   **72**: C6 (高音 Do)
*   **74**: D6 (高音 Re)
*   **76**: E6 (高音 Mi)
*   **77**: F6 (高音 Fa)
*   **79**: G6 (高音 Sol)
*   **81**: A6 (高音 La)
*   *每個音符的 `duration: 1.0` 代表 1 拍，`duration: 0.5` 代表半拍。*

---

## 🎼 歌曲 1：Amazing Grace (奇異恩典)
*   **預設節奏 (Tempo)**: 85 BPM (3/4 拍)

| 句數 | 英文歌詞 | 中文翻譯 | 聽旋律鋼琴音符 (Midi & 拍數) | 唱名對照 (音高與長度) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Amazing grace! How sweet the sound | 奇異恩典！何等甘甜的歌聲 | `[62, 1拍]`, `[67, 2拍]`, `[71, 0.5拍]`, `[67, 0.5拍]`, `[71, 2拍]`, `[69, 1拍]`, `[67, 2拍]`, `[64, 1拍]`, `[62, 2拍]` | D5(1拍) -> G5(2拍) -> B5(0.5拍) -> G5(0.5拍) -> B5(2拍) -> A5(1拍) -> G5(2拍) -> E5(1拍) -> D5(2拍) |
| **2** | That saved a wretch like me! | 拯救了像我這樣一個無用的人！ | `[62, 1拍]`, `[67, 2拍]`, `[71, 0.5拍]`, `[67, 0.5拍]`, `[71, 2拍]`, `[69, 1拍]`, `[74, 4拍]` | D5(1拍) -> G5(2拍) -> B5(0.5拍) -> G5(0.5拍) -> B5(2拍) -> A5(1拍) -> D6(4拍) |
| **3** | I once was lost, but now am found; | 我曾迷失，如今已被尋回； | `[71, 1拍]`, `[74, 2拍]`, `[71, 0.5拍]`, `[74, 0.5拍]`, `[71, 2拍]`, `[67, 1拍]`, `[62, 2拍]`, `[64, 1拍]`, `[67, 2拍]` | B5(1拍) -> D6(2拍) -> B5(0.5拍) -> D6(0.5拍) -> B5(2拍) -> G5(1拍) -> D5(2拍) -> E5(1拍) -> G5(2拍) |
| **4** | Was blind, but now I see. | 曾經盲目，如今終得看見。 | `[64, 1拍]`, `[67, 2拍]`, `[71, 0.5拍]`, `[67, 0.5拍]`, `[71, 2拍]`, `[69, 1拍]`, `[67, 4拍]` | E5(1拍) -> G5(2拍) -> B5(0.5拍) -> G5(0.5拍) -> B5(2拍) -> A5(1拍) -> G5(4拍) |

---

## 🎼 歌曲 2：Down by the Salley Gardens (莎莉花園深處)
*   **預設節奏 (Tempo)**: 75 BPM (3/4 拍)

| 句數 | 英文歌詞 | 中文翻譯 | 聽旋律鋼琴音符 (Midi & 拍數) | 唱名對照 (音高與長度) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Down by the salley gardens my love and I did meet; | 在柳樹園的深處，我和我的愛人相遇； | `[60, 1]`, `[65, 1]`, `[67, 1]`, `[69, 1.5]`, `[67, 0.5]`, `[65, 1]`, `[67, 1]`, `[69, 1]`, `[72, 1.5]`, `[74, 0.5]`, `[72, 1]`, `[69, 1]`, `[67, 2]` | C5(1) -> F5(1) -> G5(1) -> A5(1.5) -> G5(0.5) -> F5(1) -> G5(1) -> A5(1) -> C6(1.5) -> D6(0.5) -> C6(1) -> A5(1) -> G5(2) |
| **2** | She passed the salley gardens with little snow-white feet. | 她邁著雪白的小腳，走過柳樹園。 | `[60, 1]`, `[65, 1]`, `[67, 1]`, `[69, 1.5]`, `[67, 0.5]`, `[65, 1]`, `[67, 1]`, `[69, 1]`, `[72, 1.5]`, `[74, 0.5]`, `[72, 1]`, `[69, 1]`, `[65, 2]` | C5(1) -> F5(1) -> G5(1) -> A5(1.5) -> G5(0.5) -> F5(1) -> G5(1) -> A5(1) -> C6(1.5) -> D6(0.5) -> C6(1) -> A5(1) -> F5(2) |
| **3** | She bid me take love easy, as the leaves grow on the tree; | 她勸我對戀愛抱持淡然態度... | `[67, 1]`, `[69, 1]`, `[72, 1]`, `[74, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[69, 1]`, `[72, 1.5]`, `[74, 0.5]`, `[72, 1]`, `[69, 1]`, `[67, 1]`, `[67, 2]` | G5(1) -> A5(1) -> C6(1) -> D6(1.5) -> C6(0.5) -> A5(1) -> G5(1) -> A5(1) -> C6(1.5) -> D6(0.5) -> C6(1) -> A5(1) -> G5(1) -> G5(2) |
| **4** | But I, being young and foolish, with her would not agree. | 但那時的我年輕愚蠢，不肯聽從她的勸告。 | `[60, 1]`, `[65, 1]`, `[67, 1]`, `[69, 1.5]`, `[67, 0.5]`, `[65, 1]`, `[67, 1]`, `[69, 1]`, `[72, 1]`, `[74, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[65, 2]` | C5(1) -> F5(1) -> G5(1) -> A5(1.5) -> G5(0.5) -> F5(1) -> G5(1) -> A5(1) -> C6(1) -> D6(1.5) -> C6(0.5) -> A5(1) -> G5(1) -> F5(2) |

---

## 🎼 歌曲 3：Santa Lucia (桑塔露琪亞)
*   **預設節奏 (Tempo)**: 100 BPM (3/8 拍，本曲在代碼中會自動乘以 0.5 拍頻，以符合義大利船歌輕快律動)

| 句數 | 義大利文歌詞 | 中文翻譯 | 聽旋律鋼琴音符 (Midi & 拍數) | 唱名對照 (音高與長度) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Sul mare luccica l’astro d’argento. | 銀色的月星在海面上閃爍。 | `[79, 3]`, `[79, 1]`, `[84, 2]`, `[76, 3]`, `[76, 1]`, `[74, 2]`, `[72, 3]`, `[74, 1]`, `[77, 2]`, `[81, 4]`, `[79, 2]` | G5(3) -> G5(1) -> C6(2) -> E5(3) -> E5(1) -> D5(2) -> C5(3) -> D5(1) -> F5(2) -> A5(4) -> G5(2) |
| **2** | Placida è l’onda, prospero è il vento. | 微波粼粼，風兒和煦。 | `[77, 3]`, `[77, 1]`, `[83, 2]`, `[74, 3]`, `[74, 1]`, `[72, 2]`, `[71, 3]`, `[72, 1]`, `[76, 2]`, `[79, 4]`, `[79, 2]` | F5(3) -> F5(1) -> B5(2) -> D5(3) -> D5(1) -> C5(2) -> B4(3) -> C5(1) -> E5(2) -> G5(4) -> G5(2) |
| **3** | Venite all’agile barchetta mia, | 快來坐上我這輕巧的小船吧， | `[79, 3]`, `[79, 1]`, `[84, 2]`, `[76, 3]`, `[76, 1]`, `[74, 2]`, `[72, 1.5]`, `[71, 0.5]`, `[72, 1]`, `[74, 1]`, `[76, 1]`, `[77, 1]` | G5(3) -> G5(1) -> C6(2) -> E5(3) -> E5(1) -> D5(2) -> C5(1.5) -> B4(0.5) -> C5(1) -> D5(1) -> E5(1) -> F5(1) |
| **4** | Santa Lucia! Santa Lucia! | 桑塔露琪亞！桑塔露琪亞！ | `[81, 3]`, `[81, 1]`, `[86, 2]`, `[83, 3]`, `[79, 1]`, `[81, 2]`, `[83, 2]`, `[84, 4]` | A5(3) -> A5(1) -> D6(2) -> B5(3) -> G5(1) -> A5(2) -> B5(2) -> C6(4) |

---

## 💻 網頁背後的原始 JavaScript 程式碼段落
您可以將這段代碼直接複製給懂網頁的工程師或音樂老師，他們修改完成後，您可以把修改好的 `.md` 文件內容丟回給我，我會直接幫您寫入並部署！

```javascript
const songs = {
    // 奇異恩典
    ag: {
        title: "Amazing Grace (奇異恩典)",
        tempo: 85,
        videoUrl: "https://www.youtube.com/watch?v=78k5K4aY35o",
        ytSearchUrl: "https://www.youtube.com/results?search_query=Amazing+Grace+歌唱教學",
        lines: [
            { text: "Amazing grace! How sweet the sound", notes: [{midi: 62, duration: 1.0}, {midi: 67, duration: 2.0}, {midi: 71, duration: 0.5}, {midi: 67, duration: 0.5}, {midi: 71, duration: 2.0}, {midi: 69, duration: 1.0}, {midi: 67, duration: 2.0}, {midi: 64, duration: 1.0}, {midi: 62, duration: 2.0}] },
            { text: "That saved a wretch like me!", notes: [{midi: 62, duration: 1.0}, {midi: 67, duration: 2.0}, {midi: 71, duration: 0.5}, {midi: 67, duration: 0.5}, {midi: 71, duration: 2.0}, {midi: 69, duration: 1.0}, {midi: 74, duration: 4.0}] },
            { text: "I once was lost, but now am found;", notes: [{midi: 71, duration: 1.0}, {midi: 74, duration: 2.0}, {midi: 71, duration: 0.5}, {midi: 74, duration: 0.5}, {midi: 71, duration: 2.0}, {midi: 67, duration: 1.0}, {midi: 62, duration: 2.0}, {midi: 64, duration: 1.0}, {midi: 67, duration: 2.0}] },
            { text: "Was blind, but now I see.", notes: [{midi: 64, duration: 1.0}, {midi: 67, duration: 2.0}, {midi: 71, duration: 0.5}, {midi: 67, duration: 0.5}, {midi: 71, duration: 2.0}, {midi: 69, duration: 1.0}, {midi: 67, duration: 4.0}] }
        ]
    },
    // 莎莉花園
    sg: {
        title: "Down by the Salley Gardens (莎莉花園深處)",
        tempo: 75,
        videoUrl: "https://www.youtube.com/watch?v=kYv_3e8-D-Y",
        lines: [
            { text: "Down by the salley gardens my love and I did meet;", notes: [{midi: 60, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.5}, {midi: 67, duration: 0.5}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.5}, {midi: 74, duration: 0.5}, {midi: 72, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 67, duration: 2.0}] },
            { text: "She passed the salley gardens with little snow-white feet.", notes: [{midi: 60, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.5}, {midi: 67, duration: 0.5}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.5}, {midi: 74, duration: 0.5}, {midi: 72, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 65, duration: 2.0}] },
            { text: "She bid me take love easy, as the leaves grow on the tree;", notes: [{midi: 67, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.0}, {midi: 74, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.5}, {midi: 74, duration: 0.5}, {midi: 72, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 67, duration: 2.0}] },
            { text: "But I, being young and foolish, with her would not agree.", notes: [{midi: 60, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.5}, {midi: 67, duration: 0.5}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.0}, {midi: 74, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 65, duration: 2.0}] }
        ]
    },
    // 桑塔露琪亞
    sl: {
        title: "Santa Lucia (桑塔露琪亞)",
        tempo: 100,
        videoUrl: "https://www.youtube.com/watch?v=X9LJaxL0URM",
        lines: [
            { text: "Sul mare luccica l’astro d’argento.", notes: [{midi: 79, duration: 3.0}, {midi: 79, duration: 1.0}, {midi: 84, duration: 2.0}, {midi: 76, duration: 3.0}, {midi: 76, duration: 1.0}, {midi: 74, duration: 2.0}, {midi: 72, duration: 3.0}, {midi: 74, duration: 1.0}, {midi: 77, duration: 2.0}, {midi: 81, duration: 4.0}, {midi: 79, duration: 2.0}] },
            { text: "Placida è l’onda, prospero è il vento.", notes: [{midi: 77, duration: 3.0}, {midi: 77, duration: 1.0}, {midi: 83, duration: 2.0}, {midi: 74, duration: 3.0}, {midi: 74, duration: 1.0}, {midi: 72, duration: 2.0}, {midi: 71, duration: 3.0}, {midi: 72, duration: 1.0}, {midi: 76, duration: 2.0}, {midi: 79, duration: 4.0}, {midi: 79, duration: 2.0}] }
        ]
    }
};
```

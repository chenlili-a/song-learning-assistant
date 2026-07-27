# 🎵 雙語歌唱學習助手 - 歌曲資料庫與鋼琴音符對照表 (V18)

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
*   **70**: Bb5 (中音降Si)
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
| **1** | Amazing grace! How sweet the sound | 奇異恩典！何等甘甜的歌聲 | `[62, 1]`, `[67, 2]`, `[71, 0.5]`, `[67, 0.5]`, `[71, 2]`, `[69, 1]`, `[67, 2]`, `[64, 1]`, `[62, 2]` | D5(1拍) -> G5(2拍) -> B5(0.5拍) -> G5(0.5拍) -> B5(2拍) -> A5(1拍) -> G5(2拍) -> E5(1拍) -> D5(2拍) |

---

## 🎼 歌曲 2：Down by the Salley Gardens (莎莉花園深處)
*   **預設節奏 (Tempo)**: 75 BPM (3/4 拍)

| 句數 | 英文歌詞 | 中文翻譯 | 聽旋律鋼琴音符 (Midi & 拍數) | 唱名對照 (音高與長度) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Down by the salley gardens my love and I did meet; | 在柳樹園的深處，我和我的愛人相遇； | `[65, 1]`, `[65, 1]`, `[69, 1]`, `[70, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[65, 1]`, `[67, 1.5]`, `[69, 0.5]`, `[67, 1]`, `[65, 1]`, `[65, 2]` | F5(1拍) -> F5(1拍) -> A5(1拍) -> Bb5(1.5拍) -> C6(0.5拍) -> A5(1拍) -> G5(1拍) -> F5(1拍) -> G5(1.5拍) -> A5(0.5拍) -> G5(1拍) -> F5(1拍) -> F5(2拍) |
| **2** | She passed the salley gardens with little snow-white feet. | 她邁著雪白的小腳，走過柳樹園。 | `[65, 1]`, `[65, 1]`, `[69, 1]`, `[70, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[65, 1]`, `[67, 1.5]`, `[69, 0.5]`, `[67, 1]`, `[65, 1]`, `[65, 2]` | 同上（收在 F5 根音上） |
| **3** | She bid me take love easy, as the leaves grow on the tree; | 她勸我對戀愛抱持淡然態度... | `[69, 1]`, `[69, 1]`, `[72, 1]`, `[74, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[69, 1]`, `[72, 1.5]`, `[74, 0.5]`, `[72, 1]`, `[69, 1]`, `[67, 1]`, `[67, 2]` | A5(1拍) -> A5(1拍) -> C6(1拍) -> D6(1.5拍) -> C6(0.5拍) -> A5(1拍) -> G5(1拍) -> A5(1拍) -> C6(1.5拍) -> D6(0.5拍) -> C6(1拍) -> A5(1拍) -> G5(1拍) -> G5(2拍) |
| **4** | But I, being young and foolish, with her would not agree. | 但那時的我年輕愚蠢，不肯聽從她的勸告。 | `[65, 1]`, `[65, 1]`, `[69, 1]`, `[70, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[65, 1]`, `[67, 1]`, `[69, 1.5]`, `[72, 0.5]`, `[69, 1]`, `[67, 1]`, `[65, 2]` | F5(1) -> F5(1) -> A5(1) -> Bb5(1.5) -> C6(0.5) -> A5(1) -> G5(1) -> F5(1) -> G5(1) -> A5(1.5) -> C6(0.5) -> A5(1) -> G5(1) -> F5(2) |

---

## 🎼 歌曲 3：Santa Lucia (桑塔露琪亞)
*   **預設節奏 (Tempo)**: 100 BPM (3/8 拍)

| 句數 | 義大利文歌詞 | 中文翻譯 | 聽旋律鋼琴音符 (Midi & 拍數) | 唱名對照 (音高與長度) |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Sul mare luccica l’astro d’argento. | 銀色的月星在海面上閃爍。 | `[79, 3]`, `[79, 1]`, `[84, 2]`, `[76, 3]`, `[76, 1]`, `[74, 2]`, `[72, 3]`, `[74, 1]`, `[77, 2]`, `[81, 4]`, `[79, 2]` | G5(3) -> G5(1) -> C6(2) -> E5(3) -> E5(1) -> D5(2) -> C5(3) -> D5(1) -> F5(2) -> A5(4) -> G5(2) |

---

## 💻 網頁背後的原始 JavaScript 程式碼段落
```javascript
const songs = {
    sg: {
        title: "Down by the Salley Gardens (莎莉花園深處)",
        tempo: 75,
        lines: [
            { text: "Down by the salley gardens my love and I did meet;", notes: [{midi: 65, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 70, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.5}, {midi: 69, duration: 0.5}, {midi: 67, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 65, duration: 2.0}] },
            { text: "She passed the salley gardens with little snow-white feet.", notes: [{midi: 65, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 70, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.5}, {midi: 69, duration: 0.5}, {midi: 67, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 65, duration: 2.0}] },
            { text: "She bid me take love easy, as the leaves grow on the tree;", notes: [{midi: 69, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.0}, {midi: 74, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 72, duration: 1.5}, {midi: 74, duration: 0.5}, {midi: 72, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 67, duration: 2.0}] },
            { text: "But I, being young and foolish, with her would not agree.", notes: [{midi: 65, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 69, duration: 1.0}, {midi: 70, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 65, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 69, duration: 1.5}, {midi: 72, duration: 0.5}, {midi: 69, duration: 1.0}, {midi: 67, duration: 1.0}, {midi: 65, duration: 2.0}] }
        ]
    }
};
```

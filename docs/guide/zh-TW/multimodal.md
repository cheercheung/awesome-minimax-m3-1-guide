# 圖片與影片輸入

[返回案例](../../../README_zh-TW.md)

圖片輸入適合參考圖、版面和比較，影片輸入適合分析時間變化，保留原始檔案並交代各項輸入用途，逐鏡頭拆解應分別安排畫面分析、音軌轉錄與最終表格，手冊流程使用 OpenCV、PyAV 與 faster-whisper，大型影片可依下表選擇 Files API

| 輸入 | 限制 |
|---|---|
| 圖片 | 10 MB |
| URL 或 base64 影片 | 50 MB |
| 請求主體 | 64 MB |
| Files API 影片 | 512 MB |

### 參考

- [來源手冊](../../../sources/handbook.md)
- [官方文件 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)

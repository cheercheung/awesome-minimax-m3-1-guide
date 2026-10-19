# 從 M3 與 Preview 遷移

[返回案例](../../../README_zh-TW.md)

目前官方文件使用 MiniMax-M3.1-Flash，手冊中的 MiniMax-M3.1-Flash-Preview 在原始 Prompt 與紀錄中保留，新設定採用目前模型識別碼，移除關閉思考或 none 的設定，OpenAI 相容回應讀取 reasoning_content，最終回答讀取 content，不傳入 reasoning_split=false，工具對話保留完整助手訊息與對應結果


### 參考

- [來源手冊](../../../sources/handbook.md)
- [官方文件 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [官方文件 · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [官方文件 · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

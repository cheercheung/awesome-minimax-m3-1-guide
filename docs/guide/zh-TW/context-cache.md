# 上下文與快取

[返回案例](../../../README_zh-TW.md)

模型上下文視窗為 1,000,000 token，長篇專案可按固定指令、穩定工具清單與可重用資料組織，自動快取會辨識重複上下文，迭代時保持未變內容穩定，並檢查回傳的快取用量欄位，上下文與輸出預算應分別管理，大型輸入視窗不代表可以無限輸出

| 協定 | 快取用量 |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### 參考

- [來源手冊](../../../sources/handbook.md)
- [官方文件 · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

# 協定欄位速查

[返回案例](../../../README_zh-TW.md)

依使用的協定選擇思考深度與回傳欄位，多輪工具對話保留呼叫識別碼及完整助手訊息，讀取前確認 thinking 區塊或 reasoning 欄位是否存在，下表供欄位對照，完整請求結構請參考連結的官方文件

| 協定 | 思考深度欄位 | 思考內容 |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### 參考

- [來源手冊](../../../sources/handbook.md)
- [官方文件 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [官方文件 · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [官方文件 · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

# 思考深度

[返回案例](../../../README_zh-TW.md)

MiniMax-M3.1-Flash 持續啟用思考，支援 low、medium、high、xhigh、max，目前預設 max，較高等級通常需要更多生成 token 與時間，快速迭代可降低等級，複雜分析再提高等級，思考與最終回答共用輸出預算，工具呼叫回合可能沒有思考欄位，讀取前先確認是否存在

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

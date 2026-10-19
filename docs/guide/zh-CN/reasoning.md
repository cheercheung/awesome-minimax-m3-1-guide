# 思考深度

[返回案例](../../../README_zh-CN.md)

MiniMax-M3.1-Flash 保持思考开启，支持 low、medium、high、xhigh、max，当前默认 max，较高档位通常需要更多生成 token 和时间，快速迭代可降低档位，复杂分析再提高档位，思考 token 与最终回答共享输出预算，工具调用轮次可能没有思考字段，读取前先判断是否存在

| 协议 | 思考深度字段 | 思考内容 |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### 参考

- [来源手册](../../../sources/handbook.md)
- [官方文档 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [官方文档 · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [官方文档 · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

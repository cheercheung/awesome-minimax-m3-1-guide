# 协议字段速查

[返回案例](../../../README_zh-CN.md)

按所用协议选择思考深度和返回字段，多轮工具对话保留调用标识与完整助手消息，读取前检查 thinking 块或 reasoning 字段是否存在，下表用于字段对照，完整请求结构可查看所链接的官方文档

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

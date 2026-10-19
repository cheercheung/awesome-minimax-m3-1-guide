# Protocol field reference

[Back to cases](../../../README.md)

Match the effort and response fields to the protocol in use. Preserve tool-call identifiers and complete assistant messages across turns. Inspect whether a thinking block or reasoning field exists before accessing it. The table below is a field reference; use the linked official documentation for the current request schema.

| Protocol | Effort field | Reasoning output |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Reference

- [Source handbook](../../../sources/handbook.md)
- [Official documentation · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Official documentation · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Official documentation · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

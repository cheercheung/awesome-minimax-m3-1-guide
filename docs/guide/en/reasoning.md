# Reasoning effort

[Back to cases](../../../README.md)

MiniMax-M3.1-Flash keeps thinking enabled. Select low, medium, high, xhigh or max; the current default is max. Higher effort generally needs more generation tokens and time. Set a smaller effort for quick iterations and raise it when the task needs deeper analysis. Thinking tokens share the output budget. A tool-call response can omit a thinking field, so check for its presence when reading responses.

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

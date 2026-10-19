# Context and caching

[Back to cases](../../../README.md)

The model has a 1,000,000-token context window. Organize a long project with stable instructions, a consistent tool list and reusable reference material. Automatic caching recognizes repeated context. Keep unchanged content stable between iterations and inspect the returned cache-usage fields. Read the output budget separately from the context window: a large input window does not reserve space for an unlimited answer.

| Protocol | Cache usage |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### Reference

- [Source handbook](../../../sources/handbook.md)
- [Official documentation · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

# Migrate from M3 and Preview

[Back to cases](../../../README.md)

Current official documentation uses MiniMax-M3.1-Flash. The supplied handbook uses MiniMax-M3.1-Flash-Preview; preserve that spelling inside its original prompts and records. Update the model identifier in new configurations. Remove attempts to disable thinking or use none. For OpenAI-compatible responses, read reasoning_content and keep final text in content; do not request reasoning_split=false. In tool conversations, retain the complete assistant message and the matching tool results.


### Reference

- [Source handbook](../../../sources/handbook.md)
- [Official documentation · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Official documentation · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Official documentation · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

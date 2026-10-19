# 上下文与缓存

[返回案例](../../../README_zh-CN.md)

模型上下文窗口为 1,000,000 token，长项目可按固定指令、稳定工具清单和可复用资料组织，自动缓存识别重复上下文，迭代时保持未变化内容稳定，并查看返回的缓存用量字段，上下文窗口与输出预算分别管理，大输入窗口不代表可以无限输出

| 协议 | 缓存用量 |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### 参考

- [来源手册](../../../sources/handbook.md)
- [官方文档 · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

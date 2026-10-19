# 从 M3 与 Preview 迁移

[返回案例](../../../README_zh-CN.md)

当前官方文档使用 MiniMax-M3.1-Flash，手册中的 MiniMax-M3.1-Flash-Preview 在原始 Prompt 和记录中保留，新配置使用当前模型标识，移除关闭思考或 none 设置，OpenAI 兼容返回读取 reasoning_content，最终回答读取 content，不传 reasoning_split=false，工具对话保留完整助手消息与对应工具结果


### 参考

- [来源手册](../../../sources/handbook.md)
- [官方文档 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [官方文档 · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [官方文档 · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

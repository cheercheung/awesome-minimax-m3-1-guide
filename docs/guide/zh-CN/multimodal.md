# 图片与视频输入

[返回案例](../../../README_zh-CN.md)

图片输入适合参考图、版式和对比，视频输入适合时间维度的分析，保留原文件并说明每份输入的用途，逐镜头拆解任务应分别组织画面分析、音轨转写与最终表格，手册工作流使用了 OpenCV、PyAV 和 faster-whisper，大视频应根据下表选择 Files API

| 输入 | 限制 |
|---|---|
| 图片 | 10 MB |
| URL 或 base64 视频 | 50 MB |
| 请求体 | 64 MB |
| Files API 视频 | 512 MB |

### 参考

- [来源手册](../../../sources/handbook.md)
- [官方文档 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)

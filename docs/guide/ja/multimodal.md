# 画像と動画の入力

[事例に戻る](../../../README_ja.md)

画像は参考、レイアウト、比較に、動画は時間的な分析に使います。元ファイルを保存し、それぞれの役割を示します。ショット分解では映像分析、音声文字起こし、最終表を分けます。手引きでは OpenCV、PyAV、faster-whisper が使われています。大きな動画で Files API が必要かは下表で判断します。

| 入力 | 上限 |
|---|---|
| 画像 | 10 MB |
| URL または base64 の動画 | 50 MB |
| リクエスト本文 | 64 MB |
| Files API 経由の動画 | 512 MB |

### 参照

- [元の手引き](../../../sources/handbook.md)
- [公式文書 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)

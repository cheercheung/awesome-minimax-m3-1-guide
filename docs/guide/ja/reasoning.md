# 思考の深さ

[事例に戻る](../../../README_ja.md)

MiniMax-M3.1-Flash は思考を有効に保ちます。low、medium、high、xhigh、max に対応し、現在の既定値は max です。高い段階では通常、生成トークンと時間が増えます。短い反復では下げ、深い分析では上げます。思考と最終回答は出力予算を共有します。ツール応答では思考フィールドがない場合があるため、存在を確認して読み取ります。

| プロトコル | 思考深度フィールド | 思考の出力 |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### 参照

- [元の手引き](../../../sources/handbook.md)
- [公式文書 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [公式文書 · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [公式文書 · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

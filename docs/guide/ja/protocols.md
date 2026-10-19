# プロトコル別フィールド一覧

[事例に戻る](../../../README_ja.md)

使用するプロトコルに応じて思考の深さと応答フィールドを選びます。ツール呼び出しの識別子と助手メッセージ全体を維持します。thinking や reasoning の存在を確認してから読み取ります。表はフィールドの対照用で、完全な現行スキーマはリンク先の公式文書を参照できます。

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

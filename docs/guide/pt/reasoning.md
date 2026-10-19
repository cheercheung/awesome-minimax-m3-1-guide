# Profundidade de raciocínio

[Voltar aos casos](../../../README_pt.md)

MiniMax-M3.1-Flash mantém o raciocínio ativado. Aceita low, medium, high, xhigh e max; o padrão atual é max. Níveis maiores costumam exigir mais tempo e tokens de geração. Use níveis menores nas iterações rápidas e aumente para análises profundas. O raciocínio divide o orçamento de saída. Algumas respostas de ferramentas omitem esse campo; verifique sua presença.

| Protocolo | Campo de profundidade | Saída de raciocínio |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Referência

- [Manual de origem](../../../sources/handbook.md)
- [Documentação oficial · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Documentação oficial · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Documentação oficial · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

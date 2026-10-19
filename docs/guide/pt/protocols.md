# Referência de campos por protocolo

[Voltar aos casos](../../../README_pt.md)

Escolha os campos de profundidade e resposta conforme o protocolo. Preserve identificadores e mensagens completas em conversas com ferramentas. Confira a presença de thinking ou reasoning antes da leitura. A tabela compara os campos; os links oficiais fornecem o esquema atual.

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

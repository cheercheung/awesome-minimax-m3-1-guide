# Contexto e cache

[Voltar aos casos](../../../README_pt.md)

O contexto comporta 1,000,000 tokens. Organize projetos longos com instruções estáveis, ferramentas consistentes e referências reutilizáveis. O cache automático reconhece conteúdo repetido. Preserve o conteúdo que não mudou e consulte os campos de uso do cache. Gerencie separadamente a janela de contexto e o orçamento de saída.

| Protocolo | Uso de cache |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### Referência

- [Manual de origem](../../../sources/handbook.md)
- [Documentação oficial · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

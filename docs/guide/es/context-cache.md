# Contexto y caché

[Volver a los casos](../../../README_es.md)

El contexto admite 1,000,000 tokens. Organiza proyectos largos con instrucciones estables, herramientas consistentes y referencias reutilizables. La caché automática reconoce contenido repetido. Mantén estable lo que no cambia y consulta los campos de uso de caché. Gestiona por separado la ventana de contexto y el presupuesto de salida.

| Protocolo | Uso de caché |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### Referencia

- [Manual de origen](../../../sources/handbook.md)
- [Documentación oficial · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

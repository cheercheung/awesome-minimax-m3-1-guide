# Referencia de campos por protocolo

[Volver a los casos](../../../README_es.md)

Escoge los campos de profundidad y respuesta según el protocolo. Conserva identificadores y mensajes completos en conversaciones con herramientas. Comprueba la presencia de thinking o reasoning antes de leerlos. La tabla permite comparar campos; los enlaces oficiales contienen el esquema actual.

| Protocolo | Campo de profundidad | Salida de razonamiento |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Referencia

- [Manual de origen](../../../sources/handbook.md)
- [Documentación oficial · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Documentación oficial · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Documentación oficial · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

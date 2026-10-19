# Profundidad de razonamiento

[Volver a los casos](../../../README_es.md)

MiniMax-M3.1-Flash mantiene el razonamiento activado. Admite low, medium, high, xhigh y max; el valor predeterminado actual es max. Un nivel mayor suele necesitar más tiempo y tokens de generación. Reduce el nivel durante iteraciones rápidas y auméntalo para análisis complejos. El razonamiento comparte el presupuesto de salida. Comprueba si el campo existe: algunas respuestas con herramientas pueden omitirlo.

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

# Denktiefe

[Zurück zu den Fällen](../../../README_de.md)

MiniMax-M3.1-Flash lässt das Denken aktiviert. Verfügbar sind low, medium, high, xhigh und max; aktuell ist max der Standard. Höhere Stufen benötigen meist mehr Zeit und Ausgabetokens. Senken Sie die Stufe für schnelle Iterationen und erhöhen Sie sie für tiefere Analysen. Denken und Antwort teilen sich das Ausgabebudget. Prüfen Sie vor dem Lesen, ob das Denkfeld vorhanden ist.

| Protokoll | Feld für Denktiefe | Denkausgabe |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Referenz

- [Quellhandbuch](../../../sources/handbook.md)
- [Offizielle Dokumentation · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Offizielle Dokumentation · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Offizielle Dokumentation · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

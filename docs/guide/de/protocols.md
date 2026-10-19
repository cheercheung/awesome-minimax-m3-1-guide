# Protokollfelder im Überblick

[Zurück zu den Fällen](../../../README_de.md)

Wählen Sie Denk- und Antwortfelder passend zum Protokoll. Bewahren Sie Kennungen und vollständige Assistentennachrichten in Werkzeugdialogen. Prüfen Sie vor dem Zugriff, ob thinking oder reasoning vorhanden ist. Die Tabelle dient als Feldvergleich; die offizielle Dokumentation enthält das aktuelle Schema.

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

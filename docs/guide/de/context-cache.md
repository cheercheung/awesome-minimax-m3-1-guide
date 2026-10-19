# Kontext und Cache

[Zurück zu den Fällen](../../../README_de.md)

Das Kontextfenster umfasst 1,000,000 Tokens. Gliedern Sie lange Projekte mit stabilen Anweisungen, einer festen Werkzeugliste und wiederverwendbaren Quellen. Automatisches Caching erkennt wiederholten Kontext. Halten Sie unveränderte Inhalte stabil und prüfen Sie die zurückgegebenen Cache-Nutzungsfelder. Kontextfenster und Ausgabebudget sind getrennt zu verwalten.

| Protokoll | Cache-Nutzung |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### Referenz

- [Quellhandbuch](../../../sources/handbook.md)
- [Offizielle Dokumentation · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

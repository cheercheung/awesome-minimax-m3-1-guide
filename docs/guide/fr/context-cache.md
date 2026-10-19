# Contexte et cache

[Retour aux cas](../../../README_fr.md)

Le contexte accueille 1,000,000 tokens. Structurez les longs projets avec des consignes stables, une liste d’outils constante et des références réutilisables. Le cache automatique reconnaît le contenu répété. Gardez les éléments inchangés stables et consultez les champs d’utilisation du cache. Gérez séparément fenêtre de contexte et budget de sortie.

| Protocole | Utilisation du cache |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### Référence

- [Manuel source](../../../sources/handbook.md)
- [Documentation officielle · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

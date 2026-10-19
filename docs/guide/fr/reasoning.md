# Profondeur de raisonnement

[Retour aux cas](../../../README_fr.md)

MiniMax-M3.1-Flash garde le raisonnement activé. Les niveaux sont low, medium, high, xhigh et max ; la valeur actuelle par défaut est max. Un niveau supérieur demande généralement plus de temps et de tokens. Réduisez-le pour les itérations rapides, puis augmentez-le pour les analyses complexes. Le raisonnement partage le budget de sortie. Vérifiez sa présence avant de lire une réponse liée aux outils.

| Protocole | Champ de profondeur | Sortie du raisonnement |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Référence

- [Manuel source](../../../sources/handbook.md)
- [Documentation officielle · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Documentation officielle · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Documentation officielle · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

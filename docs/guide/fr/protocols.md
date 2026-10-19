# Référence des champs par protocole

[Retour aux cas](../../../README_fr.md)

Choisissez les champs de profondeur et de réponse selon le protocole. Conservez les identifiants et messages complets pendant les échanges avec outils. Vérifiez la présence de thinking ou reasoning avant leur lecture. Le tableau compare les champs ; les documents officiels donnent le schéma actuel.

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

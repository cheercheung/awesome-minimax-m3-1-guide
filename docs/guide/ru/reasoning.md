# Глубина рассуждений

[Вернуться к примерам](../../../README_ru.md)

MiniMax-M3.1-Flash сохраняет рассуждения включёнными. Поддерживаются low, medium, high, xhigh и max; текущий уровень по умолчанию — max. Повышение обычно требует больше времени и выходных токенов. Снижайте уровень для быстрых итераций и повышайте для глубокого анализа. Рассуждения и ответ используют общий выходной бюджет. Перед чтением проверьте наличие поля: в ответах с инструментами оно иногда отсутствует.

| Протокол | Поле глубины | Вывод рассуждений |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Источники

- [Исходное руководство](../../../sources/handbook.md)
- [Официальная документация · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Официальная документация · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Официальная документация · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

# Поля разных протоколов

[Вернуться к примерам](../../../README_ru.md)

Выбирайте поля глубины и ответа под используемый протокол. Между ходами сохраняйте идентификаторы вызовов и полные сообщения ассистента. До чтения проверяйте наличие thinking или reasoning. Таблица служит сравнением полей, а актуальная полная схема доступна по официальным ссылкам.

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

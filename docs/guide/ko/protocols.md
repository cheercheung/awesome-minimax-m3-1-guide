# 프로토콜별 필드 참조

[사례로 돌아가기](../../../README_ko.md)

프로토콜에 맞는 사고 깊이와 응답 필드를 선택합니다. 도구 호출 식별자와 전체 어시스턴트 메시지를 여러 턴에 걸쳐 보존합니다. thinking 또는 reasoning의 존재 여부를 확인한 뒤 읽습니다. 표는 필드 비교용이며 현재 전체 스키마는 공식 문서에서 확인할 수 있습니다.

| 프로토콜 | 사고 깊이 필드 | 사고 출력 |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### 참고

- [원본 설명서](../../../sources/handbook.md)
- [공식 문서 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [공식 문서 · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [공식 문서 · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

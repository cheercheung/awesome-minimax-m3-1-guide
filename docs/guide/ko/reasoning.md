# 사고 깊이

[사례로 돌아가기](../../../README_ko.md)

MiniMax-M3.1-Flash는 사고 기능을 켜 둡니다. low, medium, high, xhigh, max를 지원하며 현재 기본값은 max입니다. 높은 단계는 보통 더 많은 생성 토큰과 시간을 사용합니다. 빠른 반복에서는 낮추고 깊은 분석에서는 높입니다. 사고와 최종 답변은 출력 예산을 공유합니다. 도구 응답에 사고 필드가 없을 수 있으므로 존재 여부를 확인합니다.

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

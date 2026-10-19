# 컨텍스트와 캐시

[사례로 돌아가기](../../../README_ko.md)

컨텍스트 창은 1,000,000토큰입니다. 긴 프로젝트를 고정 지침, 안정적인 도구 목록, 재사용 자료로 구성합니다. 자동 캐시는 반복되는 내용을 인식합니다. 바뀌지 않은 내용은 유지하고 응답의 캐시 사용량 필드를 확인합니다. 컨텍스트 창과 출력 예산은 따로 관리합니다.

| 프로토콜 | 캐시 사용량 |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### 참고

- [원본 설명서](../../../sources/handbook.md)
- [공식 문서 · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

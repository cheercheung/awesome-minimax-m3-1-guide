# 이미지와 동영상 입력

[사례로 돌아가기](../../../README_ko.md)

이미지는 참고, 배치, 비교에 사용하고 동영상은 시간적 분석에 사용합니다. 원본 파일을 보존하고 각 입력의 목적을 밝힙니다. 쇼트 분해에서는 화면 분석, 오디오 전사, 최종 표를 분리합니다. 설명서의 작업 흐름은 OpenCV, PyAV, faster-whisper를 사용합니다. 큰 영상에 Files API가 필요한지는 아래 제한으로 판단합니다.

| 입력 | 제한 |
|---|---|
| 이미지 | 10 MB |
| URL 또는 base64 동영상 | 50 MB |
| 요청 본문 | 64 MB |
| Files API 동영상 | 512 MB |

### 참고

- [원본 설명서](../../../sources/handbook.md)
- [공식 문서 · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)

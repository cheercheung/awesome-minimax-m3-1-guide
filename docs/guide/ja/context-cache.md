# コンテキストとキャッシュ

[事例に戻る](../../../README_ja.md)

コンテキストウィンドウは 1,000,000 トークンです。長い作業は固定した指示、安定したツール一覧、再利用する資料で整理します。自動キャッシュは繰り返される内容を認識します。変更のない内容は安定させ、返されたキャッシュ使用量を確認します。入力コンテキストと出力予算は別々に管理します。

| プロトコル | キャッシュ使用量 |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### 参照

- [元の手引き](../../../sources/handbook.md)
- [公式文書 · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

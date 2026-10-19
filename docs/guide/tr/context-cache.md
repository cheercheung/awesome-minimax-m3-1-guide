# Bağlam ve önbellek

[Örneklere dön](../../../README_tr.md)

Bağlam penceresi 1,000,000 tokendir. Uzun projeleri sabit talimatlar, tutarlı araç listesi ve yeniden kullanılabilir kaynaklarla düzenleyin. Otomatik önbellek yinelenen bağlamı tanır. Değişmeyen içeriği sabit tutun ve dönen önbellek kullanım alanlarını inceleyin. Bağlam penceresini ve çıktı bütçesini ayrı yönetin.

| Protokol | Önbellek kullanımı |
|---|---|
| Anthropic | `usage.cache_read_input_tokens` |
| OpenAI Chat Completions | `usage.prompt_tokens_details.cached_tokens` |

### Kaynak

- [Kaynak el kitabı](../../../sources/handbook.md)
- [Resmî belgeler · 1](https://platform.minimax.cn/docs/api-reference/text-prompt-caching)

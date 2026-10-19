# Protokol alanları başvurusu

[Örneklere dön](../../../README_tr.md)

Derinlik ve yanıt alanlarını kullanılan protokole göre seçin. Araç çağrısı kimliklerini ve tam asistan mesajlarını turlar arasında koruyun. thinking veya reasoning alanını okumadan önce varlığını denetleyin. Tablo alanları karşılaştırır; güncel şema için resmî belge bağlantılarını kullanın.

| Protokol | Derinlik alanı | Düşünme çıktısı |
|---|---|---|
| Anthropic | `output_config.effort` | `thinking` |
| OpenAI Chat Completions | `reasoning_effort` | `reasoning_content` |
| OpenAI Responses | `reasoning.effort` | `type: "reasoning"` |

### Kaynak

- [Kaynak el kitabı](../../../sources/handbook.md)
- [Resmî belgeler · 1](https://platform.minimax.cn/docs/api-reference/text-anthropic-api)
- [Resmî belgeler · 2](https://platform.minimax.cn/docs/api-reference/text-openai-api)
- [Resmî belgeler · 3](https://platform.minimax.cn/docs/api-reference/responses-create)

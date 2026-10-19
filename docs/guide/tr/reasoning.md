# Akıl yürütme derinliği

[Örneklere dön](../../../README_tr.md)

MiniMax-M3.1-Flash düşünmeyi açık tutar. low, medium, high, xhigh ve max desteklenir; güncel varsayılan max değeridir. Yüksek düzey genellikle daha fazla üretim tokeni ve zaman gerektirir. Hızlı yinelemelerde düşürün, derin analizlerde yükseltin. Düşünme ve son yanıt çıktı bütçesini paylaşır. Araç yanıtlarında düşünme alanı bulunmayabilir; okumadan önce varlığını denetleyin.

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

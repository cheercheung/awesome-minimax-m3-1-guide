# Source handbook

Material supplied for this collection: MiniMax M3.1 Flash 使用手册

| Case | Source line | Task |
|---|---:|---|
| [MM-001](#mm-001) | 92 | Preserve native terminal scrolling |
| [MM-002](#mm-002) | 93 | Retry contended SQLite writes |
| [MM-003](#mm-003) | 94 | Stop non-terminating interval splits |
| [MM-004](#mm-004) | 95 | Reject empty ISO durations |
| [MM-005](#mm-005) | 105 | Selectable terminal themes |
| [MM-006](#mm-006) | 106 | Connect mcode to claude-tap |
| [MM-007](#mm-007) | 107 | Review and repair dynamic workflows |
| [MM-008](#mm-008) | 108 | An mcode profile for acpx |
| [MM-009](#mm-009) | 118 | Profile and optimize Flowdesk |
| [MM-010](#mm-010) | 122 | Iterate on rsync performance |
| [MM-011](#mm-011) | 134 | An interactive Temple of Heaven |
| [MM-012](#mm-012) | 135 | A voxel Millennium Falcon |
| [MM-013](#mm-013) | 136 | Drive a Curiosity rover |
| [MM-014](#mm-014) | 137 | Inside an ancient palace |
| [MM-015](#mm-015) | 147 | DANCE2000 rhythm arcade |
| [MM-016](#mm-016) | 148 | Multiplayer flight chess |
| [MM-017](#mm-017) | 149 | BAMBOO HOP pet flight |
| [MM-018](#mm-018) | 150 | Escape a pursuing city |
| [MM-019](#mm-019) | 160 | A retro restaurant website |
| [MM-020](#mm-020) | 161 | A fragrance brand website |
| [MM-021](#mm-021) | 162 | A GTA-style personality quiz |
| [MM-022](#mm-022) | 163 | A cinematic scrolling website |
| [MM-023](#mm-023) | 164 | A terminal-style creative archive |
| [MM-024](#mm-024) | 165 | A Windows XP browser desktop |
| [MM-025](#mm-025) | 177 | Animate a climate spiral |
| [MM-026](#mm-026) | 178 | Tell a war-data story |
| [MM-027](#mm-027) | 179 | Visualize ancient wonders |
| [MM-028](#mm-028) | 180 | Compare overseas launch markets |
| [MM-029](#mm-029) | 190 | Break a film into shots |
| [MM-030](#mm-030) | 191 | Find and mark image differences |
| [MM-031](#mm-031) | 192 | A red-octopus reference-film remake |
| [MM-032](#mm-032) | 193 | A MiniMax Design brand-film remake |
| [MM-033](#mm-033) | 194 | A code-rendered film about language models |
| [MM-034](#mm-034) | 195 | Solve an IChO Avogadro problem |
| [MM-035](#mm-035) | 205 | Research a BOE event |
| [MM-036](#mm-036) | 206 | Analyze PCB expectation gaps |
| [MM-037](#mm-037) | 207 | Map the Vera Rubin supply chain |
| [MM-038](#mm-038) | 208 | Model rubber-chain transmission |
| [MM-039](#mm-039) | 209 | A three-statement and DCF workbook |
| [MM-040](#mm-040) | 210 | An options-book risk package |
| [MM-041](#mm-041) | 216 | Iterate on time-series imputation |
| [MM-042](#mm-042) | 222 | Reconfigure a phased-array antenna |
| [MM-043](#mm-043) | 223 | Optimize a support structure |
| [MM-044](#mm-044) | 224 | Simulate elastic objects |
| [MM-045](#mm-045) | 225 | Stitch dual-camera video |
| [MM-046](#mm-046) | 243 | An electric-vehicle industry deck |
| [MM-047](#mm-047) | 244 | A generative-video market deck |
| [MM-048](#mm-048) | 250 | A CampusOS product deck |
| [MM-049](#mm-049) | 258 | A civilization-origins lesson |
| [MM-050](#mm-050) | 259 | An editorial-style talk |
| [MM-051](#mm-051) | 260 | An illustrated phonics lesson |
| [MM-052](#mm-052) | 261 | An Everest terrain presentation |
| [MM-053](#mm-053) | 267 | A seven-day Bali travel brief |

<a id="mm-001"></a>
## MM-001: Preserve native terminal scrolling

```text
长对话中鼠标滚轮或输出完成后，偶发跳回 TUI 对话顶部。
```


<a id="mm-002"></a>
## MM-002: Retry contended SQLite writes

```text
多个 mcode 进程共用一个 WAL 模式的 SQLite 库，并发写时后来者等锁超过 5 秒就抛 `database is locked` 且不重试，直接打断正在跑的 turn。
```


<a id="mm-003"></a>
## MM-003: Stop non-terminating interval splits

```text
负时长或负份数导致区间分割不终止。
```


<a id="mm-004"></a>
## MM-004: Reject empty ISO durations

```text
`P`、`PT` 等无组件 ISO 时长被误判为有效零时长。
```


<a id="mm-005"></a>
## MM-005: Selectable terminal themes

```text
增加 `/theme`、具名主题、明暗锁定及自定义配色。
```


<a id="mm-006"></a>
## MM-006: Connect mcode to claude-tap

```text
给 claude\-tap 增加 `--tap-client mcode`，安全过滤并持久化模型请求，在 dashboard 中标识 MiniMax Code，并提供真实 trace\-viewer 证据。
```


<a id="mm-007"></a>
## MM-007: Review and repair dynamic workflows

```text
研究 dynamic\-workflow 的实现方式，然后实现一个动态工作流的插件
```


<a id="mm-008"></a>
## MM-008: An mcode profile for acpx

```text
增加 `mcode -> mcode acp` 内置 profile，让用户无需重复 custom\-agent override 即可进入标准 `acpx <agent>` 工作流。
```


<a id="mm-009"></a>
## MM-009: Profile and optimize Flowdesk

[Supplied Prompt](../prompts/MM-009.md)

- [performance-chart.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png)
- [after-desktop.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png)
- [Flowdesk-源码与性能证据.zip](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/414dd588fb6d5834.zip)
- [Flowdesk-火焰图分析过程与复核.zip](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df80eba46d1f48b2.zip)

<a id="mm-010"></a>
## MM-010: Iterate on rsync performance

```text
**rsync 增量传输路径性能优化**
在保持传输字节、目录树、元数据、校验和、协议行为及错误处理不变的前提下，优化 rsync 的 delta/update 路径。
\-
Optimize rsync delta/update paths while preserving transferred bytes, destination tree, metadata, checksums, protocol\-visible behavior, and errors\.
```

- [clipboard.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png)
- [m31-rsync-iteration.gif](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif)

<a id="mm-011"></a>
## MM-011: An interactive Temple of Heaven

[Supplied Prompt](../prompts/MM-011.md)

[Open project](https://71ewexrmdwv66.space.mcode.cn/)

- [image 1.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg)

<a id="mm-012"></a>
## MM-012: A voxel Millennium Falcon

[Supplied Prompt](../prompts/MM-012.md)

[Open project](https://2i4ng4prh3z15.space.mcode.cn/)

- [image.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png)

<a id="mm-013"></a>
## MM-013: Drive a Curiosity rover

[Supplied Prompt](../prompts/MM-013.md)

[Open project](https://84nimch0fsp40.space.mcode.cn/)

- [image 3.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg)

<a id="mm-014"></a>
## MM-014: Inside an ancient palace

[Supplied Prompt](../prompts/MM-014.md)

[Open project](https://3526g54twnq3b.space.mcode.cn/)

- [image 2.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg)

<a id="mm-015"></a>
## MM-015: DANCE2000 rhythm arcade

[Supplied Prompt](../prompts/MM-015.md)

[Open project](https://260srblym7fzp.space.mcode.cn/)

- [跳舞机.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf.mp4)

<a id="mm-016"></a>
## MM-016: Multiplayer flight chess

[Supplied Prompt](../prompts/MM-016.md)

[Open project](https://low4r5gkb56gq.space.mcode.cn)

- [飞行棋.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8.mp4)

<a id="mm-017"></a>
## MM-017: BAMBOO HOP pet flight

[Supplied Prompt](../prompts/MM-017.md)

[Open project](https://tjb51tpmdbxvd.space.mcode.cn/)

- [Flyingbird.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c.mp4)

<a id="mm-018"></a>
## MM-018: Escape a pursuing city

[Supplied Prompt](../prompts/MM-018.md)

[Open project](https://dk3fzfkfveju6.space.mcode.cn)

- [夜城逃生.mov](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c.mp4)

<a id="mm-019"></a>
## MM-019: A retro restaurant website

[Supplied Prompt](../prompts/MM-019.md)

[Open project](https://pxv1w29d70k1l.space.mcode.cn)

- [截屏2026-09-23 18.40.59.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg)

<a id="mm-020"></a>
## MM-020: A fragrance brand website

[Supplied Prompt](../prompts/MM-020.md)

[Open project](https://yhnj4qzy5fg2e.space.mcode.cn/)

- [截屏2026-09-23 18.49.23.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg)

<a id="mm-021"></a>
## MM-021: A GTA-style personality quiz

[Supplied Prompt](../prompts/MM-021.md)

[Open project](https://3ir72drzi62wq.space.mcode.cn/)

- [截屏2026-09-23 19.45.39.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg)

<a id="mm-022"></a>
## MM-022: A cinematic scrolling website

[Supplied Prompt](../prompts/MM-022.md)

[Open project](https://d3piolkdzfrut.space.mcode.cn/)

- [Clipboard_Screenshot_1790136326.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg)

<a id="mm-023"></a>
## MM-023: A terminal-style creative archive

[Supplied Prompt](../prompts/MM-023.md)

[Open project](https://n2nbcgw6hbpr7.space.mcode.cn/)

- [Clipboard_Screenshot_1790136285.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg)

<a id="mm-024"></a>
## MM-024: A Windows XP browser desktop

[Supplied Prompt](../prompts/MM-024.md)

[Open project](https://p7itx30utl0rg.space.mcode.cn/)

- [Clipboard_Screenshot_1790136549.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg)

<a id="mm-025"></a>
## MM-025: Animate a climate spiral

[Supplied Prompt](../prompts/MM-025.md)

[Open project](https://asel6nns59e7l.space.mcode.cn/)

- [Clipboard_Screenshot_1790156482.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png)

<a id="mm-026"></a>
## MM-026: Tell a war-data story

[Supplied Prompt](../prompts/MM-026.md)

[Open project](https://ofw1iav2nxwlq.space.mcode.cn/)

- [Clipboard_Screenshot_1790157646.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png)

<a id="mm-027"></a>
## MM-027: Visualize ancient wonders

[Supplied Prompt](../prompts/MM-027.md)

[Open project](https://q02qt318izml9.space.mcode.cn/)

- [Clipboard_Screenshot_1790161143.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png)

<a id="mm-028"></a>
## MM-028: Compare overseas launch markets

[Supplied Prompt](../prompts/MM-028.md)

[Open project](https://825z92nzmpz5i.space.mcode.cn/)

- [截屏2026-09-23 19.02.39.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png)

<a id="mm-029"></a>
## MM-029: Break a film into shots

[Supplied Prompt](../prompts/MM-029.md)

- [20260923-192042.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511.mp4)
- [20260923-192042_shot_breakdown.xlsx](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/159da4fa9b1d5088.xlsx)

<a id="mm-030"></a>
## MM-030: Find and mark image differences

[Supplied Prompt](../prompts/MM-030.md)

- [找不同1.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg)
- [找不同2.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg)
- [两幅图片找不同对比图.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png)

<a id="mm-031"></a>
## MM-031: A red-octopus reference-film remake

[Supplied Prompt](../prompts/MM-031.md)

- [15-45-37-911-asset_20260914-154537-911_d59c7ca9568e_1799c40c-34932524975-1-192 (1).mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60.mp4)
- [15-45-37-931-asset_20260914-154537-931_8acfdff02394_a9e6b03e-章鱼8.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png)
- [红色章鱼玩偶_30秒完整版_精确.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645.mp4)

<a id="mm-032"></a>
## MM-032: A MiniMax Design brand-film remake

[Supplied Prompt](../prompts/MM-032.md)

- [18-21-39-532-asset_20260923-182139-532_445d044cb416_d3949c94-40481458945-1-192.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662.mp4)
- [minimax-design-20s-white-wordmark.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de.mp4)

<a id="mm-033"></a>
## MM-033: A code-rendered film about language models

[Supplied Prompt](../prompts/MM-033.md)

- [what_it_is_like_to_be_m3_1.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb.mp4)

<a id="mm-034"></a>
## MM-034: Solve an IChO Avogadro problem

[Supplied Prompt](../prompts/MM-034.md)

[Worked solution](icho-solution.md)

- [icho.pdf](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b29e8aae314fa1c6.pdf)

<a id="mm-035"></a>
## MM-035: Research a BOE event

[Supplied Prompt](../prompts/MM-035.md)

- [案例1_事件推演与历史溯源_京东方IPC大会.md](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1e131881231a01c5.md)

<a id="mm-036"></a>
## MM-036: Analyze PCB expectation gaps

[Supplied Prompt](../prompts/MM-036.md)

- [案例2_市场预期差分析_PCB产业链.md](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0cbe3c574b5e08fc.md)

<a id="mm-037"></a>
## MM-037: Map the Vera Rubin supply chain

[Supplied Prompt](../prompts/MM-037.md)

- [Clipboard_Screenshot_1790154551.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png)
- [案例4_Vera-Rubin产业链拆解制图.html](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8889bb403cd7f264.html)

<a id="mm-038"></a>
## MM-038: Model rubber-chain transmission

[Supplied Prompt](../prompts/MM-038.md)

- [Clipboard_Screenshot_1790152819.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png)
- [案例3_产业链测算建模_橡胶产业链.md](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/844630115d45f40f.md)
- [案例3_附图_橡胶产业链图表(离线可打开).html](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/388c6c6ef297587f.html)
- [案例3_附表_橡胶产业链传导模型(公式联动).xlsx](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/090d3b23d68df28f.xlsx)

<a id="mm-039"></a>
## MM-039: A three-statement and DCF workbook

[Supplied Prompt](../prompts/MM-039.md)

- [Clipboard_Screenshot_1790153571.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png)
- [贵州茅台_三张表及DCF估值模型.xlsx](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1c7361281c27dfeb.xlsx)

<a id="mm-040"></a>
## MM-040: An options-book risk package

[Supplied Prompt](../prompts/MM-040.md)

- [Clipboard_Screenshot_1790002601.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png)
- [RM_inputs.zip](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/942c1d385ba7c6cc.zip)
- [risk_summary.md](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/11e06ea49a285da0.md)
- [risk_report.xlsx](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e0978b7143a373a4.xlsx)
- [risk_engine.py](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/35d63b32974e1b83.py)

<a id="mm-041"></a>
## MM-041: Iterate on time-series imputation

```text
**多变量时间序列缺失值填补（任务摘要）**
实现一个填补模型：输入随机缺失的多变量时间序列和观测标记，根据时间上下文及变量之间的依赖恢复缺失值。训练与评测流程固定，仅修改 Custom\.py；可只读参考 DLinear、TimesNet、PatchTST 等实现，按缺失位置的重建误差评测。
```

- [clipboard.gif](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif)

<a id="mm-042"></a>
## MM-042: Reconfigure a phased-array antenna

```text
**相控阵天线重构**
一个相控阵天线中有部分单元失效。请调整其余单元的相位，让主波束对准指定方向，同时压低旁瓣，减少信号向其他方向泄漏。
```

- [antenna-anonymized.gif](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif)

<a id="mm-043"></a>
## MM-043: Optimize a support structure

```text
**支撑结构拓扑优化**
请优化支撑结构的材料布局：在固定支撑和载荷条件下，材料占比不超过 45%，尽量降低结构柔度，让它受力时更不易变形。
```

- [structure-anonymized.gif](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif)

<a id="mm-044"></a>
## MM-044: Simulate elastic objects

```text
**弹性物体物理仿真**
构建可模拟弹性物体动力学的系统，并检验对未见重力、刚度和摩擦条件的预测。
```

- [spring_gaus_showcase.mp4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef.mp4)

<a id="mm-045"></a>
## MM-045: Stitch dual-camera video

```text
**CPU 双路视频全景拼接**
20 组用两台手持相机同时拍的视频（共 9,000 多帧，包含夜景、弱纹理、快速运动场景），两路画面存在视差和抖动。
请做一个在线视频拼接系统：逐帧把两路画面对齐到同一画布，拼缝看不出来、时间上不能抖、对齐失败要有兜底。只有 CPU 可用。
同一任务交给三个模型，各独立跑 3 次：M3\.1\-Flash\-Preview / 其他模型1 / 其他模型2。统一 harness 与评测配置，8h 工作 \+ 8h 独立评审，CPU\-only 沙盒，隐藏评测集（20 序列 / 9,241 帧）全量计分。
```

- [panorama-anonymized.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png)

<a id="mm-046"></a>
## MM-046: An electric-vehicle industry deck

```text
**全球电动车行业研究**
制作英文全球电动车市场研究演示，比较区域市场、产业链、竞争格局与行业发展因素。
```

- [Clipboard_Screenshot_1792137072.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png)
- [Clipboard_Screenshot_1792137102.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png)

<a id="mm-047"></a>
## MM-047: A generative-video market deck

```text
**生成式视频市场分析**
围绕生成式视频市场、核心技术、时序一致性与指令遵循能力制作英文行业分析，采用咨询报告风格，以多栏布局、细线表格和多种图表呈现高密度信息。
```

- [clipboard 1.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png)

<a id="mm-048"></a>
## MM-048: A CampusOS product deck

```text
**CampusOS 校园产品演示**
为校园应用 CampusOS 制作12页英文产品演示，使用深色紫色风格，展示校园信息分散的问题、产品模块与界面。
```

- [filename.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png)

<a id="mm-049"></a>
## MM-049: A civilization-origins lesson

```text
**文明起源：博物馆式文化展示**
用西班牙语生成10页关于文明起源的幻灯片。
```

- [Clipboard_Screenshot_1791803752.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png)
- [Clipboard_Screenshot_1791803805.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png)

<a id="mm-050"></a>
## MM-050: An editorial-style talk

```text
**折叠：极简编辑式演讲**
制作8页中文电子杂志风演讲PPT，采用黑色与米白色、衬线大标题和无衬线正文。大字主视觉页与常规内容页交替，使用充分留白，并补充演讲备注与计划时长。
```

- [filename 1.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png)

<a id="mm-051"></a>
## MM-051: An illustrated phonics lesson

```text
**自然拼读：儿童插画课件**
为一年级学生制作“\-at”单词家族的自然拼读课程，包含发音导入、cat/hat/mat示例、配对、故事、句子练习、课堂游戏、单词搜寻、拼写和课后活动。
```

- [filename 2.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png)

<a id="mm-052"></a>
## MM-052: An Everest terrain presentation

```text
**珠峰地形与探险路线**
制作8页中文珠峰主题演示，包含地形背景、海拔数据、路线、营地比较、风险与3D展示说明，保持统一品牌配色。
```

- [Clipboard_Screenshot_1792137528.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png)
- [Clipboard_Screenshot_1792137546.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png)

<a id="mm-053"></a>
## MM-053: A seven-day Bali travel brief

```text
**巴厘岛七日旅行简报**
将给定英文旅行行程整理为简体中文演示，加入地点图片、每日时间安排、预算页，并以七日时间轴收尾。
```

- [Clipboard_Screenshot_1792137588.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png)
- [Clipboard_Screenshot_1792137630.png](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png)

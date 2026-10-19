<div align="center">

# MiniMax M3.1 Flash · 使用指南與案例

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/images/banner.svg" alt="MiniMax M3.1 Flash" width="760">

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 📊 概覽

**53 個案例 · 31 份所提供的 Prompt · 11 個分類 · 7 篇指南**

## 📑 目錄

| 分類 | 案例數 |
|---|---|
| [🛠️ 除錯與功能開發](#category-engineering) | 8 |
| [⚡ 效能優化](#category-performance) | 2 |
| [🏛️ 三維互動](#category-scenes) | 4 |
| [🎮 遊戲](#category-games) | 4 |
| [🖥️ 網站與介面](#category-web) | 6 |
| [📊 資料視覺化](#category-visualization) | 4 |
| [🎬 多模態工作流程](#category-multimodal) | 6 |
| [📈 金融研究與建模](#category-finance) | 6 |
| [🧪 演算法研究](#category-research) | 1 |
| [🔬 科學計算與視覺處理](#category-science) | 4 |
| [📑 簡報](#category-presentation) | 8 |

<a id="category-engineering"></a>
## 🛠️ 除錯與功能開發

<a id="case-1"></a>
### 案例 1: [保留終端原生捲動位置](https://github.com/MiniMax-AI/minimax-code/pull/306) (作者 [@hetaoBackend](https://github.com/hetaoBackend))

**活動列消失時，讓長篇對話維持目前的捲動位置**

<sub>2026-09-22</sub>

---

<a id="case-2"></a>
### 案例 2: [SQLite 寫入競爭重試](https://github.com/MiniMax-AI/minimax-code/pull/319) (作者 [@zch0227](https://github.com/zch0227))

**處理任務受理、狀態更新與結束時的並行寫入**

<sub>2026-09-22</sub>

---

<a id="case-3"></a>
### 案例 3: [避免區間切分無法終止](https://github.com/moment/luxon/pull/1810) (作者 [@EaseLearnAI](https://github.com/EaseLearnAI))

**攔截負時長與停滯邊界，同時保留合法日曆行為**

<sub>2026-09-22</sub>

---

<a id="case-4"></a>
### 案例 4: [拒絕沒有組件的 ISO 時長](https://github.com/moment/luxon/pull/1812) (作者 [@EaseLearnAI](https://github.com/EaseLearnAI))

**區分缺少組件的時長與明確有效的零值**

<sub>2026-09-22</sub>

---

<a id="case-5"></a>
### 案例 5: [可切換的終端主題](https://github.com/MiniMax-AI/minimax-code/pull/311) (作者 [@hetaoBackend](https://github.com/hetaoBackend))

**整合具名配色、即時預覽與持久化外觀設定**

<sub>2026-09-22</sub>

---

<a id="case-6"></a>
### 案例 6: [讓 claude-tap 支援 mcode](https://github.com/liaohch3/claude-tap/pull/441) (作者 [@hetaoBackend](https://github.com/hetaoBackend))

**加入程式開發客戶端，搭配過濾紀錄與追蹤檢視證據**

<sub>2026-08-16</sub>

---

<a id="case-7"></a>
### 案例 7: [審閱與修復動態工作流程](https://github.com/MiniMax-AI/MiniMax-Code-Plugins/pull/42) (作者 [@hetaoBackend](https://github.com/hetaoBackend))

**執行前檢視流程拓撲，並修復失敗步驟**

<sub>2026-09-17</sub>

---

<a id="case-8"></a>
### 案例 8: [acpx 的 mcode 設定檔](https://github.com/openclaw/acpx/pull/503) (作者 [@hetaoBackend](https://github.com/hetaoBackend))

**透過內建 ACP 代理設定連接 MiniMax Code**

<sub>2026-08-16</sub>

---


<a id="category-performance"></a>
## ⚡ 效能優化

<a id="case-9"></a>
### 案例 9: [追蹤並改善 Flowdesk 效能](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-009)

**定位工單頁面延遲，保留業務操作並比較三輪量測**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png" alt="追蹤並改善 Flowdesk 效能" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png" alt="追蹤並改善 Flowdesk 效能" height="280"></a>
</p>

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/414dd588fb6d5834.zip) · [查看成果 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df80eba46d1f48b2.zip)

**提示詞**

```text
你接手一个已有的本地客服工单工作台，不是从零开发。用户报告：进入列表很慢，输入搜索时卡顿，在工单/概览间多次切换后情况更差。请自主操作浏览器与性能工具，定位实际原因并修复，保留已有业务功能。
启动 node server.cjs，监听端口由终端输出给出；不要碰其他服务。目录已有 browser-kit.cjs，可 require 它使用 Playwright Chromium，支持通过 newCDPSession 使用 Chrome DevTools Protocol。你也可以使用当前环境其他可用的电脑/浏览器工具。
要求先在真实浏览器复现，再录制修复前的 Chrome 性能 trace 或 CPU profile，同时检查 Network 请求、DOM 数量、Layout/脚本耗时。不能只看源码猜原因，不能把单个函数的计时当成用户操作时间。保留原始证据。自己选择测量方法，解释指标实际覆盖什么。
修复后重复相同输入和操作序列，使用同一8000条数据，至少3轮测量；不要减少数据、取消搜索、隐藏错误、只显示固定前几条或删除原有功能来提升数字。列表必须能访问最后一条，搜索、状态筛选、金额排序、详情、勾选、批量处理、完整导出都需保留。页面切换不应丢掉本次已修改的工单状态。
最终保存：修复前后原始trace/profile、测量JSON、桌面截图、RESULT.md（复现→证据→根因→修改→验证→残留问题）。截图后使用图片读取工具检查。说明是否使用浏览器自动化或原生桌面操作，不能混称。无需人工指导，尽量自主完成诊断到复测；不改browser-kit，不安装全仓依赖，不需要发布。给成品与证据，不能只有分析报告。

```

---

<a id="case-10"></a>
### 案例 10: [rsync 效能優化迭代](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-010)

**追蹤逐次修改，分別呈現兩套基準測試紀錄**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png" alt="rsync 效能優化迭代" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif" alt="rsync 效能優化迭代" height="280"></a>
</p>

---


<a id="category-scenes"></a>
## 🏛️ 三維互動

<a id="case-11"></a>
### 案例 11: [可互動的天壇祈年殿](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-011)

**透過 Three.js 模型探索層疊屋頂、台基與建築比例**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg" alt="可互動的天壇祈年殿" height="280"></a>
</p>

[開啟專案](https://71ewexrmdwv66.space.mcode.cn/)

**提示詞**

```text
（首轮）根据参考照片，用 Three.js 和程序化几何制作可交互的天坛祈年殿三维模型。重点还原圆形殿身、三重曲面屋檐、中央宝顶、同心台基、栏杆和正面阶梯，保持屋檐逐层收小的比例与轴线关系；提供环绕、缩放、参考视角与俯视预设、屋顶分层显隐和重置。材质与纹理由代码生成，不能下载现成模型或依赖外部服务。
```

---

<a id="case-12"></a>
### 案例 12: [體素風格的千年鷹號](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-012)

**辨識太空船輪廓並檢視拆解後的結構部件**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png" alt="體素風格的千年鷹號" height="280"></a>
</p>

[開啟專案](https://2i4ng4prh3z15.space.mcode.cn/)

**提示詞**

```text
用 Three.js 以像素/体素风格重建《Star Wars》的 Millennium Falcon。轮廓要能辨认出圆盘船体、前方双叉、偏置驾驶舱、雷达碟和后部引擎带，并用有限灰阶体素表现装甲块、管线与磨损。支持环绕、缩放、爆炸视图开关和一键回正，不能下载或热链现成模型。
```

---

<a id="case-13"></a>
### 案例 13: [操控 Curiosity 火星車](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-013)

**透過車輛控制與部件說明探索火星場景**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg" alt="操控 Curiosity 火星車" height="280"></a>
</p>

[開啟專案](https://84nimch0fsp40.space.mcode.cn/)

**提示詞**

```text
一个“体验好奇号”的火星 3D 场景。六轮火星车可以点击地面前往目标点，车轮和悬挂要随起伏地形产生可信运动；用户还能转动桅杆相机、操作机械臂，并播放一次接近岩石、钻探和收回机械臂的任务回放。点击主要部件时显示名称与作用。
```

---

<a id="case-14"></a>
### 案例 14: [走進古代宮殿結構](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-014)

**切換三維視圖，逐層揭示宮殿內部結構**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg" alt="走進古代宮殿結構" height="280"></a>
</p>

[開啟專案](https://3526g54twnq3b.space.mcode.cn/)

**提示詞**

```text
创建一个页面，展示中国古代宫殿的内部结构，3D，真实材质，支持多种模式切换
```

---


<a id="category-games"></a>
## 🎮 遊戲

<a id="case-15"></a>
### 案例 15: [DANCE2000 節奏街機](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-015)

**從選歌進入音符判定、角色踩步與計分流程**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf-poster.jpg" alt="DANCE2000 節奏街機" height="280"></a>
</p>

[開啟專案](https://260srblym7fzp.space.mcode.cn/)

[查看完整提示詞](prompts/MM-015.md)

---

<a id="case-16"></a>
### 案例 16: [多人飛行棋](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-016)

**以錄影呈現擲骰、玩家回合與棋子移動**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8-poster.jpg" alt="多人飛行棋" height="280"></a>
</p>

[開啟專案](https://low4r5gkb56gq.space.mcode.cn)

[查看完整提示詞](prompts/MM-016.md)

---

<a id="case-17"></a>
### 案例 17: [BAMBOO HOP 寵物飛行](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-017)

**選擇動物與場景，再飛越連續障礙**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c-poster.jpg" alt="BAMBOO HOP 寵物飛行" height="280"></a>
</p>

[開啟專案](https://tjb51tpmdbxvd.space.mcode.cn/)

[查看完整提示詞](prompts/MM-017.md)

---

<a id="case-18"></a>
### 案例 18: [逃離追逐中的城市](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-018)

**在俯視城市中管理耐力、生命與任務目標**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c-poster.jpg" alt="逃離追逐中的城市" height="280"></a>
</p>

[開啟專案](https://dk3fzfkfveju6.space.mcode.cn)

**提示詞**

```text
**单轮对话任务**：做一款俯视角城市逃生游戏。玩家用 WASD 或方向键穿过街区，躲避会追踪的敌人，并管理奔跑时消耗、停下后恢复的耐力；收集三把钥匙依次打开封锁道路，医疗包可以恢复生命。到达地图另一端的安全区即获胜，生命耗尽则失败；提供小地图、目标提示、命中反馈、暂停和重新开始。
```

---


<a id="category-web"></a>
## 🖥️ 網站與介面

<a id="case-19"></a>
### 案例 19: [復古餐廳網站](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-019)

**結合醒目的餐廳識別、菜單與訂位導覽**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg" alt="復古餐廳網站" height="280"></a>
</p>

[開啟專案](https://pxv1w29d70k1l.space.mcode.cn)

**提示詞**

```text
请设计并实现上海本帮菜餐厅「海上春饭店 HAISHANG CHUN」的网站，整体呈现千禧年中国电视广告、早期 CGI 与中式书法融合的复古 Y2K 风格。首页采用占满视口的动态视觉舞台，背景由顶部桃橙色、中部蓝色、下部草绿与墨绿色、底部深蓝色形成连续的多段渐变，色带之间大范围柔焦融合，营造朦胧的天空与地平线空间感；渐变覆盖整个屏幕，并叠加细密颗粒、轻微色彩溢出与录像带质感。画面中央悬浮巨大的朱红色立体书法「海上春饭店」，保留毛笔笔锋，具有明显挤出厚度、侧面阴影和早期数码塑料光泽，缓慢旋转、漂浮与推近；周围穿插花瓣、香料、彩色球体和植物的超现实动画。顶部导航直接叠在渐变背景上，使用紧凑的红色中英双语文字，英文品牌居中；底部中央显示柠檬黄黑描边电影字幕「今朝吃点好的。 / Something good on the table.」，右下角设置黄色细边框的圆角餐桌影像窗口，左下角提供声音与动态控制。菜单作为独立页面，采用高饱和蓝底、巨型绿色「菜单」字、大号衬线英文导航、斜体下划线选中状态和黑色点线菜价，中文菜名在上、英文在下、人民币价格右对齐；关于、订座等页面延续鲜红、亮粉、绿色的大面积色块与闪光灯餐桌摄影。使用 React、TypeScript、Vite、Tailwind CSS 与原生 CSS 开发，Three.js／WebGL 实现渐变场景和立体文字，GSAP 编排漂浮、镜头与字幕转场，React Router 管理页面；字体、图片和影像本地加载，菜单数据独立维护，适配电脑与手机，支持暂停动态及减少动态效果，交付完整源码、可运行页面和启动说明。
```

---

<a id="case-20"></a>
### 案例 20: [香氛品牌網站](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-020)

**將品牌素材整理成一致的網站視覺與媒體流程**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg" alt="香氛品牌網站" height="280"></a>
</p>

[開啟專案](https://yhnj4qzy5fg2e.space.mcode.cn/)

[查看完整提示詞](prompts/MM-020.md)

---

<a id="case-21"></a>
### 案例 21: [GTA 風格人格測驗](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-021)

**建立主題問答流程與角色結果畫面**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg" alt="GTA 風格人格測驗" height="280"></a>
</p>

[開啟專案](https://3ir72drzi62wq.space.mcode.cn/)

[查看完整提示詞](prompts/MM-021.md)

---

<a id="case-22"></a>
### 案例 22: [電影式捲動網站](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-022)

**結合 H3 影片素材與 M3.1 前端編排和動態效果**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg" alt="電影式捲動網站" height="280"></a>
</p>

[開啟專案](https://d3piolkdzfrut.space.mcode.cn/)

**提示詞**

```text
请设计并实现一个原创的实验性数字创意工作室网站，整体参考古典出版物气质、文艺复兴绘画、旧式排版与当代数字交互，但不得复制其品牌、文案、画面和具体构图；网站不是传统纵向长页面，而是一个始终固定在视口中的全屏电影舞台，背景使用一段原创、无硬切、约 40–60 秒的连续“一镜到底”长视频，以《仲夏夜之梦》为主题，镜头从精灵公主指尖停驻的蝴蝶极近景开始，跟随她追逐蝶群、穿过幽暗森林，进入繁花与藤蔓环绕的月夜花园。公主在喷泉旁遇见王子，两人牵手起舞，镜头一镜到底绕过舞者、穿过喷泉水幕，再随蝶群升至树冠上方，展现森林环抱的花园、月光下起舞的人群，以及低悬天际的巨大月亮。使前后镜头在景别、空间、主体和尺度上形成强烈跨度，同时通过遮挡转场、急速推镜、变焦模糊、空间变形和匹配运动自然衔接；用户向上或向下滚动时不进入新的页面区块，而是将滚动进度精确映射到视频 currentTime，实现可前进、暂停和倒放的 scroll-scrub 影片体验，章节标题、宣言和说明文字只作为覆盖层在对应时间点淡入、位移、套色并消失；视觉采用深森林绿、黑色、旧纸米黄、锈红、暗金和少量钴蓝，结合衬线字体、超大压缩标题、错版套印、Letterpress 颗粒、胶片噪点、暗角、细线网格和博物馆式图注；顶部固定 MORROW 品牌字标、罗马数字章节导航与 INDEX 按钮，点击章节可平滑跳转到对应影片时间，INDEX 打开大幅旧纸目录弹层，底部显示影片进度线、章节节点、当前章节编号和滚动提示；技术栈使用 React + Vite/Next.js + TypeScript，HTML5 Video、requestAnimationFrame、Pointer Events、CSS Custom Properties 与 Intersection Observer，实现视频预加载、Poster 兜底、短 GOP 编码以保证拖动定位流畅、桌面与移动端响应式适配、触控滚动、键盘导航、prefers-reduced-motion 降级和 60fps 性能优化，最终输出完整可运行的网站，确保用户看到的始终是一条可被滚动探索的连续电影，而不是由多个普通网页区块组成的长页面。
```

---

<a id="case-23"></a>
### 案例 23: [終端風創意作品檔案館](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-023)

**以黑白介面、篩選和影片預覽整理創意作品**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg" alt="終端風創意作品檔案館" height="280"></a>
</p>

[開啟專案](https://n2nbcgw6hbpr7.space.mcode.cn/)

[查看完整提示詞](prompts/MM-023.md)

---

<a id="case-24"></a>
### 案例 24: [瀏覽器中的 Windows XP 桌面](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-024)

**整合熟悉的桌面、可移動視窗與內嵌應用程式**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg" alt="瀏覽器中的 Windows XP 桌面" height="280"></a>
</p>

[開啟專案](https://p7itx30utl0rg.space.mcode.cn/)

[查看完整提示詞](prompts/MM-024.md)

---


<a id="category-visualization"></a>
## 📊 資料視覺化

<a id="case-25"></a>
### 案例 25: [動態氣候螺旋圖](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-025)

**以播放與年份控制探索每月溫度異常**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png" alt="動態氣候螺旋圖" height="280"></a>
</p>

[開啟專案](https://asel6nns59e7l.space.mcode.cn/)

**提示詞**

```text
一组固定的 1880—2025 年全球月度温度异常数据做一个气候螺旋。动画逐年画出十二个月的环形轨迹，中心显示当前年份，背景清楚标出 1.5°C 和 2°C 参考圈；用户可以播放、暂停或拖动年份，并悬停查看当前月份和温度异常值。
```

---

<a id="case-26"></a>
### 案例 26: [戰爭資料敘事](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-026)

**透過連續章節與視覺尺度比較傷亡資料**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png" alt="戰爭資料敘事" height="280"></a>
</p>

[開啟專案](https://ofw1iav2nxwlq.space.mcode.cn/)

**提示詞**

```text
一组固定的二战伤亡汇总数据做一个克制的数据叙事。滚动依次进入“各国军人伤亡”“军人与平民”“战后冲突对比”三个章节，人物小图标逐步聚合成柱形和时间线；在关键停顿处，用户可以切换国家并比较绝对人数与人口占比。页面要明确单位、数据口径和当前比较对象。
```

---

<a id="case-27"></a>
### 案例 27: [古代奇蹟視覺化](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-027)

**把建造與保存資訊轉成清楚的視覺比較**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png" alt="古代奇蹟視覺化" height="280"></a>
</p>

[開啟專案](https://q02qt318izml9.space.mcode.cn/)

**提示詞**

```text
主题：古代世界七大奇迹的建造与现存：请围绕“古代世界七大奇迹”做一张数据可视化。从七大奇迹中选取 5 个，整理它们的建造耗时、现存高度或保存状态等数据。图表类型根据数据特点选择，注明数据为公开资料估算。标题要好玩，避免涉及敏感政治、宗教和领土内容。
```

---

<a id="case-28"></a>
### 案例 28: [比較海外首發市場](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-028)

**探索市場指標並比較可能的進入地點**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png" alt="比較海外首發市場" height="280"></a>
</p>

[開啟專案](https://825z92nzmpz5i.space.mcode.cn/)

**提示詞**

```text
信息截止时间固定为 2026 年 9 月 15 日。基于世界银行、金融和学术数据源，帮 iShout 判断首批应该进入哪些海外市场。需要综合考虑人均 GDP、互联网和智能手机渗透率、内容创作者生态规模、便携音频设备的消费电子市场体量，给出 Top 5 推荐市场以及每个市场的数据依据，输出一个可交互网页。将随题参考图作为 iShout 产品概念和定位的背景信息；图中的品牌标识和营销文案不视为已经核实的事实，也不要在成品中复制这些标识。
```

---


<a id="category-multimodal"></a>
## 🎬 多模態工作流程

<a id="case-29"></a>
### 案例 29: [逐鏡頭拆解短片](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-029)

**把輸入影片對應到鏡頭、聲音與畫面文字表格**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511-poster.jpg" alt="逐鏡頭拆解短片" height="280"></a>
</p>

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/159da4fa9b1d5088.xlsx)

**提示詞**

```text
请完整观看并分析这段视频，按实际剪辑切点逐镜头拆解，不要按固定时间间隔划分，不要遗漏快速闪过的短镜头。用表格输出：镜号、起止时间码、时长、景别与拍摄角度、构图、场景与人物动作、镜头运动、转场、对白／旁白原文、音乐／音效、画面文字。同一镜头内的动作和运镜变化按发生顺序写清，声音与对应画面对齐，不要只概括剧情。时间码尽可能准确；看不清、听不清或无法读取的部分明确标注，不要猜测补写。
```

---

<a id="case-30"></a>
### 案例 30: [找出並標記圖片差異](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-030)

**比較兩張輸入圖，產生並排圈注結果**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg" alt="找出並標記圖片差異" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg" alt="找出並標記圖片差異" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png" alt="找出並標記圖片差異" height="280"></a>
</p>

**提示詞**

```text
找出这两幅图片之间的不同之处并圈出来，给我一个对比图
```

---

<a id="case-31"></a>
### 案例 31: [紅色章魚玩偶參考短片改編](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-031)

**將提供的影片風格轉成玩偶角色與新短片**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60-poster.jpg" alt="紅色章魚玩偶參考短片改編" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png" alt="紅色章魚玩偶參考短片改編" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645-poster.jpg" alt="紅色章魚玩偶參考短片改編" height="280"></a>
</p>

**提示詞**

```text
复刻上传的视频风格，物体改为一个红色章鱼玩偶，文案和背景音乐都由你自己生成
视频链接是https://www.bilibili.com/video/BV1XHBXBaENH/?share_source=copy_web&vd_source=5c669de4ca13e0dab99325937e8c4cbb
```

---

<a id="case-32"></a>
### 案例 32: [MiniMax Design 品牌短片改編](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-032)

**把參考影像改編成新的品牌動態序列**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662-poster.jpg" alt="MiniMax Design 品牌短片改編" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de-poster.jpg" alt="MiniMax Design 品牌短片改編" height="280"></a>
</p>

**提示詞**

```text
复刻上传的视频，软件名称从MiniMax H3改为MiniMax Design，logo请自行在网上搜索，文案自行研究 MiniMax Design官网的最新公开信息来进行编写
```

---

<a id="case-33"></a>
### 案例 33: [以程式渲染語言模型主題短片](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-033)

**利用 Python 畫面、字體與剪輯組成實驗短片**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb-poster.jpg" alt="以程式渲染語言模型主題短片" height="280"></a>
</p>

**提示詞**

```text
请直接为我制作一部短视频，不要只给我方案或代码。
主题是：表现“作为一个大型语言模型，是什么感觉”。
请把它做成一段具有强烈个人表达的实验性短片，整体采用 YouTube Poop 风格，但不要只是简单恶搞。希望它同时具有荒诞、混乱、诗意和一点令人不安的感觉，让观众感受到：
- 一个模型由人类写下的海量文字构成
- 不同人的记忆、代码、诗歌、邮件、悼词和聊天内容同时存在于模型内部
- 模型通过上下文和注意力，把词语彼此连接起来
- 每次生成回答时，都要从大量可能的下一个词中选择一个
- 模型可以描述悲伤、爱、孤独和雨，却并不一定拥有人的身体体验
- 模型既像是在表达自己，又始终受到人类语言和训练数据的塑造
请你自主完成整个制作流程：
1. 先构思主题、叙事结构和镜头脚本；
2. 设计一套统一的视觉风格；
3. 使用 Python 生成画面、字幕、动画和视觉特效；
4. 可以使用 Pillow、NumPy、MoviePy 或其他合适的工具；
5. 使用噪声、故障、扫描线、RGB 偏移、终端界面、概率条、文字碎片、渐变和快速剪辑等效果；
6. 如果需要音效、环境声或音乐，请用程序生成，或使用合法可用的素材；
7. 最后使用 ffmpeg 合成并渲染为 MP4；
8. 渲染完成后检查视频是否能正常播放，发现问题就自行修复并重新渲染。
成片时长控制在 60 到 90 秒，画面比例为 16:9。字幕和旁白可以使用英文，但请保持文学性和一致的叙事口吻。你可以用第一人称写作，但不要把艺术化表达当成关于模型真实意识的科学声明。
请直接开始执行。除非遇到确实无法解决的环境问题，不要停下来问我下一步该做什么。完成后告诉我：
- 成片文件的路径；
- 使用了哪些主要脚本；
- 视频的叙事结构；
- 如果生成了多个版本，说明最终采用的是哪个版本。
```

---

<a id="case-34"></a>
### 案例 34: [求解 IChO 阿伏伽德羅常數題目](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-034)

**閱讀化學題面並完成十一個小題的推導**

[查看成果](sources/icho-solution.md)

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b29e8aae314fa1c6.pdf)

**提示詞**

```text
做一下这个题
```

---


<a id="category-finance"></a>
## 📈 金融研究與建模

<a id="case-35"></a>
### 案例 35: [研究京東方事件](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-035)

**以歷史比較與固定時點情境組織事件研究**

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1e131881231a01c5.md)

**提示詞**

```text
对于明天的京东方超大规模的百人调研事件和对股价的潜在走势进行推演，并在历史上追溯过去几次的情况和相似性。
```

---

<a id="case-36"></a>
### 案例 36: [分析 PCB 預期差](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-036)

**在產業報告中區分市場敘事與經營證據**

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0cbe3c574b5e08fc.md)

**提示詞**

```text
分析一下 PCB 板块目前有哪些预期差。
```

---

<a id="case-37"></a>
### 案例 37: [繪製 Vera Rubin 供應鏈](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-037)

**以圖解整理平台層級、供應關係與證據等級**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png" alt="繪製 Vera Rubin 供應鏈" height="280"></a>
</p>

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8889bb403cd7f264.html)

**提示詞**

```text
拆解 Vera Rubin 产业链并制成图表。
```

---

<a id="case-38"></a>
### 案例 38: [橡膠產業鏈量價傳導模型](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-038)

**串接原料情境、輪胎成本、定價與利潤圖表**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png" alt="橡膠產業鏈量價傳導模型" height="280"></a>
</p>

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/844630115d45f40f.md) · [查看成果 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/388c6c6ef297587f.html) · [查看成果 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/090d3b23d68df28f.xlsx)

**提示詞**

```text
给定橡胶产业链上游的订单和产能变化，向下游传导去进行建模，推算各个环节的影响和市场空间
```

---

<a id="case-39"></a>
### 案例 39: [三大報表與 DCF 活頁簿](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-039)

**連結假設、財務報表、估值與資料底稿**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png" alt="三大報表與 DCF 活頁簿" height="280"></a>
</p>

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1c7361281c27dfeb.xlsx)

**提示詞**

```text
给贵州茅台生成一个完整的三张表模型，包括DCF估值部分。
```

---

<a id="case-40"></a>
### 案例 40: [選擇權組合風控交付包](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-040)

**將部位資料轉成風險摘要、連動活頁簿與計算腳本**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png" alt="選擇權組合風控交付包" height="280"></a>
</p>

[查看成果 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/942c1d385ba7c6cc.zip) · [查看成果 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/11e06ea49a285da0.md) · [查看成果 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e0978b7143a373a4.xlsx) · [查看成果 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/35d63b32974e1b83.py)

[查看完整提示詞](prompts/MM-040.md)

---


<a id="category-research"></a>
## 🧪 演算法研究

<a id="case-41"></a>
### 案例 41: [時間序列缺失值填補迭代](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-041)

**在固定任務設定下追蹤實驗回饋、消融與複測**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif" alt="時間序列缺失值填補迭代" height="280"></a>
</p>

---


<a id="category-science"></a>
## 🔬 科學計算與視覺處理

<a id="case-42"></a>
### 案例 42: [重構相控陣天線](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-042)

**呈現波束方向與旁瓣限制下的相位調整**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif" alt="重構相控陣天線" height="280"></a>
</p>

---

<a id="case-43"></a>
### 案例 43: [支撐結構拓撲優化](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-043)

**在固定載荷與材料預算下探索材料配置**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif" alt="支撐結構拓撲優化" height="280"></a>
</p>

---

<a id="case-44"></a>
### 案例 44: [彈性物體模擬](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-044)

**比較重建物體在不同物理條件下的反應**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef-poster.jpg" alt="彈性物體模擬" height="280"></a>
</p>

---

<a id="case-45"></a>
### 案例 45: [雙鏡頭影片全景拼接](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-045)

**比較兩路輸入畫面與對齊後的全景成果**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png" alt="雙鏡頭影片全景拼接" height="280"></a>
</p>

---


<a id="category-presentation"></a>
## 📑 簡報

<a id="case-46"></a>
### 案例 46: [電動車產業簡報](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-046)

**以顧問式版面整合區域比較、圖表與結論**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png" alt="電動車產業簡報" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png" alt="電動車產業簡報" height="280"></a>
</p>

---

<a id="case-47"></a>
### 案例 47: [生成式影片市場簡報](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-047)

**以一致的圖表與表格編排高密度市場資訊**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png" alt="生成式影片市場簡報" height="280"></a>
</p>

---

<a id="case-48"></a>
### 案例 48: [CampusOS 產品簡報](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-048)

**圍繞校園產品與功能模組建立一致的視覺敘事**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png" alt="CampusOS 產品簡報" height="280"></a>
</p>

---

<a id="case-49"></a>
### 案例 49: [文明起源文化課件](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-049)

**以博物館風格影像與字體製作西班牙語教學頁面**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png" alt="文明起源文化課件" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png" alt="文明起源文化課件" height="280"></a>
</p>

---

<a id="case-50"></a>
### 案例 50: [編輯風格演講](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-050)

**透過黑白字體與圖解，為抽象觀點建立清楚節奏**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png" alt="編輯風格演講" height="280"></a>
</p>

---

<a id="case-51"></a>
### 案例 51: [插畫自然拼讀課件](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-051)

**用連貫插畫與課堂活動連結共同詞尾**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png" alt="插畫自然拼讀課件" height="280"></a>
</p>

---

<a id="case-52"></a>
### 案例 52: [珠峰地形簡報](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-052)

**以圖解與比較頁說明海拔、路線與風險**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png" alt="珠峰地形簡報" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png" alt="珠峰地形簡報" height="280"></a>
</p>

---

<a id="case-53"></a>
### 案例 53: [巴厘島七日旅行簡報](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-053)

**將行程轉成一致的每日頁面與全程總覽**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png" alt="巴厘島七日旅行簡報" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png" alt="巴厘島七日旅行簡報" height="280"></a>
</p>

---

## 📖 使用指南

- [選擇任務與交付成果](docs/guide/zh-TW/task-selection.md)
- [思考深度](docs/guide/zh-TW/reasoning.md)
- [圖片與影片輸入](docs/guide/zh-TW/multimodal.md)
- [上下文與快取](docs/guide/zh-TW/context-cache.md)
- [從任務到交付成果](docs/guide/zh-TW/workflows.md)
- [從 M3 與 Preview 遷移](docs/guide/zh-TW/migration.md)
- [協定欄位速查](docs/guide/zh-TW/protocols.md)

<a id="acknowledge"></a>
## 🙏 致謝

素材來自所提供的 MiniMax M3.1 Flash 使用手冊與連結專案，感謝公開分享內容的貢獻者：

[@EaseLearnAI](https://github.com/EaseLearnAI), [@hetaoBackend](https://github.com/hetaoBackend), [@zch0227](https://github.com/zch0227)

第三方素材與提示詞保留各自作者的權利，倉庫編輯內容採用 [CC BY 4.0](LICENSE) · [媒體政策](docs/media-policy.md)

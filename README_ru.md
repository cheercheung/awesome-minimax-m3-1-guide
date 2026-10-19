<div align="center">

# MiniMax M3.1 Flash · Руководство и примеры применения

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/images/banner.svg" alt="MiniMax M3.1 Flash" width="760">

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 📊 Обзор

**53 примера · 31 предоставленный Prompt · 11 категорий · 7 руководств**

## 📑 Содержание

| Категория | Примеры |
|---|---|
| [🛠️ Отладка и разработка функций](#category-engineering) | 8 |
| [⚡ Оптимизация производительности](#category-performance) | 2 |
| [🏛️ 3D-взаимодействие](#category-scenes) | 4 |
| [🎮 Игры](#category-games) | 4 |
| [🖥️ Веб-интерфейсы](#category-web) | 6 |
| [📊 Визуализация данных](#category-visualization) | 4 |
| [🎬 Мультимодальные процессы](#category-multimodal) | 6 |
| [📈 Финансовые исследования и моделирование](#category-finance) | 6 |
| [🧪 Исследование алгоритмов](#category-research) | 1 |
| [🔬 Научные и визуальные вычисления](#category-science) | 4 |
| [📑 Презентации](#category-presentation) | 8 |

<a id="category-engineering"></a>
## 🛠️ Отладка и разработка функций

<a id="case-1"></a>
### Пример 1: [Сохранение естественной прокрутки терминала](https://github.com/MiniMax-AI/minimax-code/pull/306) (автор [@hetaoBackend](https://github.com/hetaoBackend))

**Удерживать положение длинного диалога при исчезновении строк активности**

<sub>2026-09-22</sub>

---

<a id="case-2"></a>
### Пример 2: [Повтор конфликтующих записей SQLite](https://github.com/MiniMax-AI/minimax-code/pull/319) (автор [@zch0227](https://github.com/zch0227))

**Обрабатывать одновременную запись при приёме, обновлении и завершении задач**

<sub>2026-09-22</sub>

---

<a id="case-3"></a>
### Пример 3: [Предотвращение бесконечного деления интервалов](https://github.com/moment/luxon/pull/1810) (автор [@EaseLearnAI](https://github.com/EaseLearnAI))

**Проверять отрицательные длительности и неподвижные границы, сохраняя корректную работу календаря**

<sub>2026-09-22</sub>

---

<a id="case-4"></a>
### Пример 4: [Отклонение ISO-длительностей без компонентов](https://github.com/moment/luxon/pull/1812) (автор [@EaseLearnAI](https://github.com/EaseLearnAI))

**Отличать пустую длительность от явно заданного допустимого нуля**

<sub>2026-09-22</sub>

---

<a id="case-5"></a>
### Пример 5: [Выбираемые темы терминала](https://github.com/MiniMax-AI/minimax-code/pull/311) (автор [@hetaoBackend](https://github.com/hetaoBackend))

**Объединить именованные палитры, предпросмотр и сохранение настроек**

<sub>2026-09-22</sub>

---

<a id="case-6"></a>
### Пример 6: [Подключение mcode к claude-tap](https://github.com/liaohch3/claude-tap/pull/441) (автор [@hetaoBackend](https://github.com/hetaoBackend))

**Добавить клиент разработки с фильтрацией записей и подтверждением работы просмотрщика трасс**

<sub>2026-08-16</sub>

---

<a id="case-7"></a>
### Пример 7: [Проверка и исправление динамических процессов](https://github.com/MiniMax-AI/MiniMax-Code-Plugins/pull/42) (автор [@hetaoBackend](https://github.com/hetaoBackend))

**Изучать топологию до запуска и исправлять неудавшиеся шаги**

<sub>2026-09-17</sub>

---

<a id="case-8"></a>
### Пример 8: [Профиль mcode для acpx](https://github.com/openclaw/acpx/pull/503) (автор [@hetaoBackend](https://github.com/hetaoBackend))

**Подключить MiniMax Code через встроенный профиль агента ACP**

<sub>2026-08-16</sub>

---


<a id="category-performance"></a>
## ⚡ Оптимизация производительности

<a id="case-9"></a>
### Пример 9: [Анализ и оптимизация Flowdesk](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-009)

**Найти медленные экраны, сохранить рабочие операции и сравнить три серии измерений**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png" alt="Анализ и оптимизация Flowdesk" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png" alt="Анализ и оптимизация Flowdesk" height="280"></a>
</p>

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/414dd588fb6d5834.zip) · [Посмотреть результат 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df80eba46d1f48b2.zip)

**Промпт**

```text
你接手一个已有的本地客服工单工作台，不是从零开发。用户报告：进入列表很慢，输入搜索时卡顿，在工单/概览间多次切换后情况更差。请自主操作浏览器与性能工具，定位实际原因并修复，保留已有业务功能。
启动 node server.cjs，监听端口由终端输出给出；不要碰其他服务。目录已有 browser-kit.cjs，可 require 它使用 Playwright Chromium，支持通过 newCDPSession 使用 Chrome DevTools Protocol。你也可以使用当前环境其他可用的电脑/浏览器工具。
要求先在真实浏览器复现，再录制修复前的 Chrome 性能 trace 或 CPU profile，同时检查 Network 请求、DOM 数量、Layout/脚本耗时。不能只看源码猜原因，不能把单个函数的计时当成用户操作时间。保留原始证据。自己选择测量方法，解释指标实际覆盖什么。
修复后重复相同输入和操作序列，使用同一8000条数据，至少3轮测量；不要减少数据、取消搜索、隐藏错误、只显示固定前几条或删除原有功能来提升数字。列表必须能访问最后一条，搜索、状态筛选、金额排序、详情、勾选、批量处理、完整导出都需保留。页面切换不应丢掉本次已修改的工单状态。
最终保存：修复前后原始trace/profile、测量JSON、桌面截图、RESULT.md（复现→证据→根因→修改→验证→残留问题）。截图后使用图片读取工具检查。说明是否使用浏览器自动化或原生桌面操作，不能混称。无需人工指导，尽量自主完成诊断到复测；不改browser-kit，不安装全仓依赖，不需要发布。给成品与证据，不能只有分析报告。

```

---

<a id="case-10"></a>
### Пример 10: [Пошаговое улучшение производительности rsync](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-010)

**Отслеживать отдельные оптимизации и разделять два набора результатов**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png" alt="Пошаговое улучшение производительности rsync" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif" alt="Пошаговое улучшение производительности rsync" height="280"></a>
</p>

---


<a id="category-scenes"></a>
## 🏛️ 3D-взаимодействие

<a id="case-11"></a>
### Пример 11: [Интерактивный Храм Неба](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-011)

**Изучать многоярусные крыши, террасы и пропорции через модель Three.js**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg" alt="Интерактивный Храм Неба" height="280"></a>
</p>

[Открыть проект](https://71ewexrmdwv66.space.mcode.cn/)

**Промпт**

```text
（首轮）根据参考照片，用 Three.js 和程序化几何制作可交互的天坛祈年殿三维模型。重点还原圆形殿身、三重曲面屋檐、中央宝顶、同心台基、栏杆和正面阶梯，保持屋檐逐层收小的比例与轴线关系；提供环绕、缩放、参考视角与俯视预设、屋顶分层显隐和重置。材质与纹理由代码生成，不能下载现成模型或依赖外部服务。
```

---

<a id="case-12"></a>
### Пример 12: [Millennium Falcon из вокселей](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-012)

**Узнать силуэт корабля и рассмотреть разнесённые детали конструкции**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png" alt="Millennium Falcon из вокселей" height="280"></a>
</p>

[Открыть проект](https://2i4ng4prh3z15.space.mcode.cn/)

**Промпт**

```text
用 Three.js 以像素/体素风格重建《Star Wars》的 Millennium Falcon。轮廓要能辨认出圆盘船体、前方双叉、偏置驾驶舱、雷达碟和后部引擎带，并用有限灰阶体素表现装甲块、管线与磨损。支持环绕、缩放、爆炸视图开关和一键回正，不能下载或热链现成模型。
```

---

<a id="case-13"></a>
### Пример 13: [Управление марсоходом Curiosity](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-013)

**Исследовать Марс с управлением машиной и пояснениями к компонентам**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg" alt="Управление марсоходом Curiosity" height="280"></a>
</p>

[Открыть проект](https://84nimch0fsp40.space.mcode.cn/)

**Промпт**

```text
一个“体验好奇号”的火星 3D 场景。六轮火星车可以点击地面前往目标点，车轮和悬挂要随起伏地形产生可信运动；用户还能转动桅杆相机、操作机械臂，并播放一次接近岩石、钻探和收回机械臂的任务回放。点击主要部件时显示名称与作用。
```

---

<a id="case-14"></a>
### Пример 14: [Внутреннее устройство древнего дворца](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-014)

**Раскрывать конструкцию с помощью переключаемых трёхмерных представлений**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg" alt="Внутреннее устройство древнего дворца" height="280"></a>
</p>

[Открыть проект](https://3526g54twnq3b.space.mcode.cn/)

**Промпт**

```text
创建一个页面，展示中国古代宫殿的内部结构，3D，真实材质，支持多种模式切换
```

---


<a id="category-games"></a>
## 🎮 Игры

<a id="case-15"></a>
### Пример 15: [Ритм-аркада DANCE2000](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-015)

**Пройти от выбора песни к синхронным нотам, движениям персонажа и подсчёту очков**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf-poster.jpg" alt="Ритм-аркада DANCE2000" height="280"></a>
</p>

[Открыть проект](https://260srblym7fzp.space.mcode.cn/)

[Прочитать полный промпт](prompts/MM-015.md)

---

<a id="case-16"></a>
### Пример 16: [Многопользовательская Flight Chess](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-016)

**Проследить броски кубика, очередность и движение фишек на готовом поле**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8-poster.jpg" alt="Многопользовательская Flight Chess" height="280"></a>
</p>

[Открыть проект](https://low4r5gkb56gq.space.mcode.cn)

[Прочитать полный промпт](prompts/MM-016.md)

---

<a id="case-17"></a>
### Пример 17: [Полёт питомцев в BAMBOO HOP](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-017)

**Выбрать животное и пейзаж, затем пролететь между препятствиями**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c-poster.jpg" alt="Полёт питомцев в BAMBOO HOP" height="280"></a>
</p>

[Открыть проект](https://tjb51tpmdbxvd.space.mcode.cn/)

[Прочитать полный промпт](prompts/MM-017.md)

---

<a id="case-18"></a>
### Пример 18: [Побег из города с преследованием](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-018)

**Перемещаться по городу сверху, управляя выносливостью, здоровьем и целями**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c-poster.jpg" alt="Побег из города с преследованием" height="280"></a>
</p>

[Открыть проект](https://dk3fzfkfveju6.space.mcode.cn)

**Промпт**

```text
**单轮对话任务**：做一款俯视角城市逃生游戏。玩家用 WASD 或方向键穿过街区，躲避会追踪的敌人，并管理奔跑时消耗、停下后恢复的耐力；收集三把钥匙依次打开封锁道路，医疗包可以恢复生命。到达地图另一端的安全区即获胜，生命耗尽则失败；提供小地图、目标提示、命中反馈、暂停和重新开始。
```

---


<a id="category-web"></a>
## 🖥️ Веб-интерфейсы

<a id="case-19"></a>
### Пример 19: [Ретросайт ресторана](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-019)

**Соединить выразительный образ ресторана с меню и навигацией к бронированию**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg" alt="Ретросайт ресторана" height="280"></a>
</p>

[Открыть проект](https://pxv1w29d70k1l.space.mcode.cn)

**Промпт**

```text
请设计并实现上海本帮菜餐厅「海上春饭店 HAISHANG CHUN」的网站，整体呈现千禧年中国电视广告、早期 CGI 与中式书法融合的复古 Y2K 风格。首页采用占满视口的动态视觉舞台，背景由顶部桃橙色、中部蓝色、下部草绿与墨绿色、底部深蓝色形成连续的多段渐变，色带之间大范围柔焦融合，营造朦胧的天空与地平线空间感；渐变覆盖整个屏幕，并叠加细密颗粒、轻微色彩溢出与录像带质感。画面中央悬浮巨大的朱红色立体书法「海上春饭店」，保留毛笔笔锋，具有明显挤出厚度、侧面阴影和早期数码塑料光泽，缓慢旋转、漂浮与推近；周围穿插花瓣、香料、彩色球体和植物的超现实动画。顶部导航直接叠在渐变背景上，使用紧凑的红色中英双语文字，英文品牌居中；底部中央显示柠檬黄黑描边电影字幕「今朝吃点好的。 / Something good on the table.」，右下角设置黄色细边框的圆角餐桌影像窗口，左下角提供声音与动态控制。菜单作为独立页面，采用高饱和蓝底、巨型绿色「菜单」字、大号衬线英文导航、斜体下划线选中状态和黑色点线菜价，中文菜名在上、英文在下、人民币价格右对齐；关于、订座等页面延续鲜红、亮粉、绿色的大面积色块与闪光灯餐桌摄影。使用 React、TypeScript、Vite、Tailwind CSS 与原生 CSS 开发，Three.js／WebGL 实现渐变场景和立体文字，GSAP 编排漂浮、镜头与字幕转场，React Router 管理页面；字体、图片和影像本地加载，菜单数据独立维护，适配电脑与手机，支持暂停动态及减少动态效果，交付完整源码、可运行页面和启动说明。
```

---

<a id="case-20"></a>
### Пример 20: [Сайт парфюмерного бренда](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-020)

**Превратить материалы бренда в согласованный сайт и медиапроцесс**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg" alt="Сайт парфюмерного бренда" height="280"></a>
</p>

[Открыть проект](https://yhnj4qzy5fg2e.space.mcode.cn/)

[Прочитать полный промпт](prompts/MM-020.md)

---

<a id="case-21"></a>
### Пример 21: [Тест личности в стиле GTA](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-021)

**Создать тематические вопросы и экран результата с персонажем**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg" alt="Тест личности в стиле GTA" height="280"></a>
</p>

[Открыть проект](https://3ir72drzi62wq.space.mcode.cn/)

[Прочитать полный промпт](prompts/MM-021.md)

---

<a id="case-22"></a>
### Пример 22: [Кинематографичный сайт с прокруткой](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-022)

**Совместить видео H3 с фронтенд-композицией и движением от M3.1**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg" alt="Кинематографичный сайт с прокруткой" height="280"></a>
</p>

[Открыть проект](https://d3piolkdzfrut.space.mcode.cn/)

**Промпт**

```text
请设计并实现一个原创的实验性数字创意工作室网站，整体参考古典出版物气质、文艺复兴绘画、旧式排版与当代数字交互，但不得复制其品牌、文案、画面和具体构图；网站不是传统纵向长页面，而是一个始终固定在视口中的全屏电影舞台，背景使用一段原创、无硬切、约 40–60 秒的连续“一镜到底”长视频，以《仲夏夜之梦》为主题，镜头从精灵公主指尖停驻的蝴蝶极近景开始，跟随她追逐蝶群、穿过幽暗森林，进入繁花与藤蔓环绕的月夜花园。公主在喷泉旁遇见王子，两人牵手起舞，镜头一镜到底绕过舞者、穿过喷泉水幕，再随蝶群升至树冠上方，展现森林环抱的花园、月光下起舞的人群，以及低悬天际的巨大月亮。使前后镜头在景别、空间、主体和尺度上形成强烈跨度，同时通过遮挡转场、急速推镜、变焦模糊、空间变形和匹配运动自然衔接；用户向上或向下滚动时不进入新的页面区块，而是将滚动进度精确映射到视频 currentTime，实现可前进、暂停和倒放的 scroll-scrub 影片体验，章节标题、宣言和说明文字只作为覆盖层在对应时间点淡入、位移、套色并消失；视觉采用深森林绿、黑色、旧纸米黄、锈红、暗金和少量钴蓝，结合衬线字体、超大压缩标题、错版套印、Letterpress 颗粒、胶片噪点、暗角、细线网格和博物馆式图注；顶部固定 MORROW 品牌字标、罗马数字章节导航与 INDEX 按钮，点击章节可平滑跳转到对应影片时间，INDEX 打开大幅旧纸目录弹层，底部显示影片进度线、章节节点、当前章节编号和滚动提示；技术栈使用 React + Vite/Next.js + TypeScript，HTML5 Video、requestAnimationFrame、Pointer Events、CSS Custom Properties 与 Intersection Observer，实现视频预加载、Poster 兜底、短 GOP 编码以保证拖动定位流畅、桌面与移动端响应式适配、触控滚动、键盘导航、prefers-reduced-motion 降级和 60fps 性能优化，最终输出完整可运行的网站，确保用户看到的始终是一条可被滚动探索的连续电影，而不是由多个普通网页区块组成的长页面。
```

---

<a id="case-23"></a>
### Пример 23: [Творческий архив в стиле терминала](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-023)

**Организовать работы с монохромной навигацией, фильтрами и видеопредпросмотром**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg" alt="Творческий архив в стиле терминала" height="280"></a>
</p>

[Открыть проект](https://n2nbcgw6hbpr7.space.mcode.cn/)

[Прочитать полный промпт](prompts/MM-023.md)

---

<a id="case-24"></a>
### Пример 24: [Рабочий стол Windows XP в браузере](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-024)

**Объединить знакомый интерфейс, перемещаемые окна и встроенные приложения**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg" alt="Рабочий стол Windows XP в браузере" height="280"></a>
</p>

[Открыть проект](https://p7itx30utl0rg.space.mcode.cn/)

[Прочитать полный промпт](prompts/MM-024.md)

---


<a id="category-visualization"></a>
## 📊 Визуализация данных

<a id="case-25"></a>
### Пример 25: [Анимация климатической спирали](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-025)

**Изучать месячные температурные аномалии с воспроизведением и выбором года**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png" alt="Анимация климатической спирали" height="280"></a>
</p>

[Открыть проект](https://asel6nns59e7l.space.mcode.cn/)

**Промпт**

```text
一组固定的 1880—2025 年全球月度温度异常数据做一个气候螺旋。动画逐年画出十二个月的环形轨迹，中心显示当前年份，背景清楚标出 1.5°C 和 2°C 参考圈；用户可以播放、暂停或拖动年份，并悬停查看当前月份和温度异常值。
```

---

<a id="case-26"></a>
### Пример 26: [Повествование на основе военных данных](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-026)

**Сравнивать потери через последовательные главы и визуальные масштабы**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png" alt="Повествование на основе военных данных" height="280"></a>
</p>

[Открыть проект](https://ofw1iav2nxwlq.space.mcode.cn/)

**Промпт**

```text
一组固定的二战伤亡汇总数据做一个克制的数据叙事。滚动依次进入“各国军人伤亡”“军人与平民”“战后冲突对比”三个章节，人物小图标逐步聚合成柱形和时间线；在关键停顿处，用户可以切换国家并比较绝对人数与人口占比。页面要明确单位、数据口径和当前比较对象。
```

---

<a id="case-27"></a>
### Пример 27: [Визуализация древних чудес света](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-027)

**Превратить сведения о строительстве и сохранности в понятное сравнение**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png" alt="Визуализация древних чудес света" height="280"></a>
</p>

[Открыть проект](https://q02qt318izml9.space.mcode.cn/)

**Промпт**

```text
主题：古代世界七大奇迹的建造与现存：请围绕“古代世界七大奇迹”做一张数据可视化。从七大奇迹中选取 5 个，整理它们的建造耗时、现存高度或保存状态等数据。图表类型根据数据特点选择，注明数据为公开资料估算。标题要好玩，避免涉及敏感政治、宗教和领土内容。
```

---

<a id="case-28"></a>
### Пример 28: [Сравнение зарубежных рынков запуска](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-028)

**Исследовать показатели и сравнивать возможные направления выхода**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png" alt="Сравнение зарубежных рынков запуска" height="280"></a>
</p>

[Открыть проект](https://825z92nzmpz5i.space.mcode.cn/)

**Промпт**

```text
信息截止时间固定为 2026 年 9 月 15 日。基于世界银行、金融和学术数据源，帮 iShout 判断首批应该进入哪些海外市场。需要综合考虑人均 GDP、互联网和智能手机渗透率、内容创作者生态规模、便携音频设备的消费电子市场体量，给出 Top 5 推荐市场以及每个市场的数据依据，输出一个可交互网页。将随题参考图作为 iShout 产品概念和定位的背景信息；图中的品牌标识和营销文案不视为已经核实的事实，也不要在成品中复制这些标识。
```

---


<a id="category-multimodal"></a>
## 🎬 Мультимодальные процессы

<a id="case-29"></a>
### Пример 29: [Разбор фильма по планам](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-029)

**Сопоставить видео с таблицей планов, звука и экранного текста**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511-poster.jpg" alt="Разбор фильма по планам" height="280"></a>
</p>

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/159da4fa9b1d5088.xlsx)

**Промпт**

```text
请完整观看并分析这段视频，按实际剪辑切点逐镜头拆解，不要按固定时间间隔划分，不要遗漏快速闪过的短镜头。用表格输出：镜号、起止时间码、时长、景别与拍摄角度、构图、场景与人物动作、镜头运动、转场、对白／旁白原文、音乐／音效、画面文字。同一镜头内的动作和运镜变化按发生顺序写清，声音与对应画面对齐，不要只概括剧情。时间码尽可能准确；看不清、听不清或无法读取的部分明确标注，不要猜测补写。
```

---

<a id="case-30"></a>
### Пример 30: [Поиск и выделение различий изображений](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-030)

**Сравнить два исходных изображения и выдать параллельный результат с пометками**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg" alt="Поиск и выделение различий изображений" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg" alt="Поиск и выделение различий изображений" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png" alt="Поиск и выделение различий изображений" height="280"></a>
</p>

**Промпт**

```text
找出这两幅图片之间的不同之处并圈出来，给我一个对比图
```

---

<a id="case-31"></a>
### Пример 31: [Ремейк референсного фильма с красным осьминогом](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-031)

**Перенести заданный стиль на игрушечного героя и новый короткометражный фильм**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60-poster.jpg" alt="Ремейк референсного фильма с красным осьминогом" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png" alt="Ремейк референсного фильма с красным осьминогом" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645-poster.jpg" alt="Ремейк референсного фильма с красным осьминогом" height="280"></a>
</p>

**Промпт**

```text
复刻上传的视频风格，物体改为一个红色章鱼玩偶，文案和背景音乐都由你自己生成
视频链接是https://www.bilibili.com/video/BV1XHBXBaENH/?share_source=copy_web&vd_source=5c669de4ca13e0dab99325937e8c4cbb
```

---

<a id="case-32"></a>
### Пример 32: [Ремейк брендового фильма MiniMax Design](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-032)

**Преобразовать референсные изображения в новую фирменную анимационную последовательность**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662-poster.jpg" alt="Ремейк брендового фильма MiniMax Design" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de-poster.jpg" alt="Ремейк брендового фильма MiniMax Design" height="280"></a>
</p>

**Промпт**

```text
复刻上传的视频，软件名称从MiniMax H3改为MiniMax Design，logo请自行在网上搜索，文案自行研究 MiniMax Design官网的最新公开信息来进行编写
```

---

<a id="case-33"></a>
### Пример 33: [Фильм о языковых моделях, созданный кодом](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-033)

**Собрать экспериментальную короткометражку из графики Python, типографики и монтажа**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb-poster.jpg" alt="Фильм о языковых моделях, созданный кодом" height="280"></a>
</p>

**Промпт**

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
### Пример 34: [Решение задачи IChO о числе Авогадро](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-034)

**Прочитать условие по химии и разобрать одиннадцать вопросов**

[Посмотреть результат](sources/icho-solution.md)

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b29e8aae314fa1c6.pdf)

**Промпт**

```text
做一下这个题
```

---


<a id="category-finance"></a>
## 📈 Финансовые исследования и моделирование

<a id="case-35"></a>
### Пример 35: [Исследование события BOE](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-035)

**Построить анализ на исторических сравнениях и датированных сценариях**

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1e131881231a01c5.md)

**Промпт**

```text
对于明天的京东方超大规模的百人调研事件和对股价的潜在走势进行推演，并在历史上追溯过去几次的情况和相似性。
```

---

<a id="case-36"></a>
### Пример 36: [Анализ разрыва ожиданий в отрасли PCB](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-036)

**Отделить рыночные истории от операционных свидетельств в отраслевом отчёте**

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0cbe3c574b5e08fc.md)

**Промпт**

```text
分析一下 PCB 板块目前有哪些预期差。
```

---

<a id="case-37"></a>
### Пример 37: [Карта цепочки поставок Vera Rubin](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-037)

**Упорядочить уровни платформы, связи поставок и категории доказательств на схеме**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png" alt="Карта цепочки поставок Vera Rubin" height="280"></a>
</p>

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8889bb403cd7f264.html)

**Промпт**

```text
拆解 Vera Rubin 产业链并制成图表。
```

---

<a id="case-38"></a>
### Пример 38: [Моделирование передачи изменений в каучуковой цепочке](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-038)

**Связать сырьевые сценарии с затратами на шины, ценами и маржой**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png" alt="Моделирование передачи изменений в каучуковой цепочке" height="280"></a>
</p>

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/844630115d45f40f.md) · [Посмотреть результат 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/388c6c6ef297587f.html) · [Посмотреть результат 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/090d3b23d68df28f.xlsx)

**Промпт**

```text
给定橡胶产业链上游的订单和产能变化，向下游传导去进行建模，推算各个环节的影响和市场空间
```

---

<a id="case-39"></a>
### Пример 39: [Книга трёх финансовых отчётов и DCF](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-039)

**Связать допущения, финансовые отчёты, оценку и исходные данные**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png" alt="Книга трёх финансовых отчётов и DCF" height="280"></a>
</p>

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1c7361281c27dfeb.xlsx)

**Промпт**

```text
给贵州茅台生成一个完整的三张表模型，包括DCF估值部分。
```

---

<a id="case-40"></a>
### Пример 40: [Пакет анализа риска опционного портфеля](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-040)

**Превратить позиции в записку, связанную книгу и расчётный скрипт**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png" alt="Пакет анализа риска опционного портфеля" height="280"></a>
</p>

[Посмотреть результат 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/942c1d385ba7c6cc.zip) · [Посмотреть результат 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/11e06ea49a285da0.md) · [Посмотреть результат 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e0978b7143a373a4.xlsx) · [Посмотреть результат 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/35d63b32974e1b83.py)

[Прочитать полный промпт](prompts/MM-040.md)

---


<a id="category-research"></a>
## 🧪 Исследование алгоритмов

<a id="case-41"></a>
### Пример 41: [Итерации заполнения пропусков временных рядов](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-041)

**Отслеживать эксперименты, абляции и повторные проверки при фиксированных настройках**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif" alt="Итерации заполнения пропусков временных рядов" height="280"></a>
</p>

---


<a id="category-science"></a>
## 🔬 Научные и визуальные вычисления

<a id="case-42"></a>
### Пример 42: [Перенастройка фазированной антенной решётки](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-042)

**Визуализировать настройку фаз при ограничениях направления луча и боковых лепестков**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif" alt="Перенастройка фазированной антенной решётки" height="280"></a>
</p>

---

<a id="case-43"></a>
### Пример 43: [Оптимизация опорной конструкции](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-043)

**Исследовать распределение материала при заданной нагрузке и его ограниченном объёме**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif" alt="Оптимизация опорной конструкции" height="280"></a>
</p>

---

<a id="case-44"></a>
### Пример 44: [Симуляция упругих объектов](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-044)

**Сравнивать восстановленные объекты в изменяющихся физических условиях**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef-poster.jpg" alt="Симуляция упругих объектов" height="280"></a>
</p>

---

<a id="case-45"></a>
### Пример 45: [Сшивка видео двух камер](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-045)

**Сравнить два входных ракурса с совмещённой панорамой**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png" alt="Сшивка видео двух камер" height="280"></a>
</p>

---


<a id="category-presentation"></a>
## 📑 Презентации

<a id="case-46"></a>
### Пример 46: [Презентация об отрасли электромобилей](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-046)

**Объединить региональные сравнения, графики и выводы в консультационном оформлении**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png" alt="Презентация об отрасли электромобилей" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png" alt="Презентация об отрасли электромобилей" height="280"></a>
</p>

---

<a id="case-47"></a>
### Пример 47: [Презентация о рынке генеративного видео](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-047)

**Упорядочить плотную рыночную информацию согласованными графиками и таблицами**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png" alt="Презентация о рынке генеративного видео" height="280"></a>
</p>

---

<a id="case-48"></a>
### Пример 48: [Презентация продукта CampusOS](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-048)

**Построить единое визуальное повествование о продукте и его модулях**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png" alt="Презентация продукта CampusOS" height="280"></a>
</p>

---

<a id="case-49"></a>
### Пример 49: [Урок об истоках цивилизации](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-049)

**Использовать музейные изображения и типографику для учебных страниц на испанском**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png" alt="Урок об истоках цивилизации" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png" alt="Урок об истоках цивилизации" height="280"></a>
</p>

---

<a id="case-50"></a>
### Пример 50: [Выступление в редакционном стиле](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-050)

**Придать абстрактным идеям ясный ритм монохромной типографикой и схемами**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png" alt="Выступление в редакционном стиле" height="280"></a>
</p>

---

<a id="case-51"></a>
### Пример 51: [Иллюстрированный урок фонетики](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-051)

**Связать семейство слов с повторяющимися рисунками и классными заданиями**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png" alt="Иллюстрированный урок фонетики" height="280"></a>
</p>

---

<a id="case-52"></a>
### Пример 52: [Презентация о рельефе Эвереста](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-052)

**Объяснить высоты, маршруты и риски с помощью схем и сравнений**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png" alt="Презентация о рельефе Эвереста" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png" alt="Презентация о рельефе Эвереста" height="280"></a>
</p>

---

<a id="case-53"></a>
### Пример 53: [План семидневной поездки на Бали](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-053)

**Превратить маршрут в согласованные ежедневные страницы и общий обзор**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png" alt="План семидневной поездки на Бали" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png" alt="План семидневной поездки на Бали" height="280"></a>
</p>

---

## 📖 Руководства

- [Выбор задачи](docs/guide/ru/task-selection.md)
- [Глубина рассуждений](docs/guide/ru/reasoning.md)
- [Изображения и видео](docs/guide/ru/multimodal.md)
- [Контекст и кеширование](docs/guide/ru/context-cache.md)
- [От задачи к результату](docs/guide/ru/workflows.md)
- [Переход с M3 и Preview](docs/guide/ru/migration.md)
- [Поля разных протоколов](docs/guide/ru/protocols.md)

<a id="acknowledge"></a>
## 🙏 Благодарности

Материалы взяты из предоставленного руководства MiniMax M3.1 Flash и связанных проектов. Благодарим открытых участников:

[@EaseLearnAI](https://github.com/EaseLearnAI), [@hetaoBackend](https://github.com/hetaoBackend), [@zch0227](https://github.com/zch0227)

Права на сторонние медиа и промпты сохраняются за авторами. Редакционные материалы распространяются по лицензии [CC BY 4.0](LICENSE) · [Политика медиа](docs/media-policy.md)

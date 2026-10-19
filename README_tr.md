<div align="center">

# MiniMax M3.1 Flash · Kılavuz ve kullanım örnekleri

<img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/images/banner.svg" alt="MiniMax M3.1 Flash" width="760">

[![License: CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](LICENSE)

[![English](https://img.shields.io/badge/English-111111)](README.md) [![Español](https://img.shields.io/badge/Espa%C3%B1ol-ffb703)](README_es.md) [![Português](https://img.shields.io/badge/Portugu%C3%AAs-2a9d8f)](README_pt.md) [![日本語](https://img.shields.io/badge/%E6%97%A5%E6%9C%AC%E8%AA%9E-52b788)](README_ja.md) [![한국어](https://img.shields.io/badge/%ED%95%9C%EA%B5%AD%EC%96%B4-4ea8de)](README_ko.md) [![Deutsch](https://img.shields.io/badge/Deutsch-f4a261)](README_de.md) [![Français](https://img.shields.io/badge/Fran%C3%A7ais-e76f51)](README_fr.md) [![Türkçe](https://img.shields.io/badge/T%C3%BCrk%C3%A7e-d62828)](README_tr.md) [![繁體中文](https://img.shields.io/badge/%E7%B9%81%E9%AB%94%E4%B8%AD%E6%96%87-8338ec)](README_zh-TW.md) [![简体中文](https://img.shields.io/badge/%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87-ef476f)](README_zh-CN.md) [![Русский](https://img.shields.io/badge/%D0%A0%D1%83%D1%81%D1%81%D0%BA%D0%B8%D0%B9-577590)](README_ru.md)

</div>

## 📊 Genel bakış

**53 örnek · Sağlanan 31 Prompt · 11 kategori · 7 kılavuz**

## 📑 İçindekiler

| Kategori | Örnekler |
|---|---|
| [🏛️ 3B etkileşim](#category-scenes) | 4 |
| [🎮 Oyunlar](#category-games) | 4 |
| [🖥️ Web arayüzleri](#category-web) | 6 |
| [📊 Veri görselleştirme](#category-visualization) | 4 |
| [🎬 Çok modlu iş akışları](#category-multimodal) | 6 |
| [📑 Sunumlar](#category-presentation) | 8 |
| [🔬 Bilimsel ve görsel hesaplama](#category-science) | 4 |
| [⚡ Performans iyileştirme](#category-performance) | 2 |
| [🧪 Algoritma araştırması](#category-research) | 1 |
| [📈 Finansal araştırma ve modelleme](#category-finance) | 6 |
| [🛠️ Hata ayıklama ve özellikler](#category-engineering) | 8 |

<a id="category-scenes"></a>
## 🏛️ 3B etkileşim

<a id="case-11"></a>
### Örnek 11: [Etkileşimli Gök Tapınağı](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-011)

**Three.js modeliyle katmanlı çatıları, terasları ve mimari oranları keşfedin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5ea9170dce69f84a-display.jpg" alt="Etkileşimli Gök Tapınağı" height="280"></a>
</p>

[Projeyi aç](https://71ewexrmdwv66.space.mcode.cn/)

**İstem**

```text
（首轮）根据参考照片，用 Three.js 和程序化几何制作可交互的天坛祈年殿三维模型。重点还原圆形殿身、三重曲面屋檐、中央宝顶、同心台基、栏杆和正面阶梯，保持屋檐逐层收小的比例与轴线关系；提供环绕、缩放、参考视角与俯视预设、屋顶分层显隐和重置。材质与纹理由代码生成，不能下载现成模型或依赖外部服务。
```

---

<a id="case-12"></a>
### Örnek 12: [Voksel Millennium Falcon](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-012)

**Uzay aracının siluetini tanıyın ve ayrılmış yapısal parçaları inceleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/265c847727ad622d.png" alt="Voksel Millennium Falcon" height="280"></a>
</p>

[Projeyi aç](https://2i4ng4prh3z15.space.mcode.cn/)

**İstem**

```text
用 Three.js 以像素/体素风格重建《Star Wars》的 Millennium Falcon。轮廓要能辨认出圆盘船体、前方双叉、偏置驾驶舱、雷达碟和后部引擎带，并用有限灰阶体素表现装甲块、管线与磨损。支持环绕、缩放、爆炸视图开关和一键回正，不能下载或热链现成模型。
```

---

<a id="case-13"></a>
### Örnek 13: [Curiosity gezginini sürme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-013)

**Araç kontrolleri ve parça açıklamalarıyla Mars sahnesini keşfedin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/5131f7b36f75492c-display.jpg" alt="Curiosity gezginini sürme" height="280"></a>
</p>

[Projeyi aç](https://84nimch0fsp40.space.mcode.cn/)

**İstem**

```text
一个“体验好奇号”的火星 3D 场景。六轮火星车可以点击地面前往目标点，车轮和悬挂要随起伏地形产生可信运动；用户还能转动桅杆相机、操作机械臂，并播放一次接近岩石、钻探和收回机械臂的任务回放。点击主要部件时显示名称与作用。
```

---

<a id="case-14"></a>
### Örnek 14: [Antik sarayın iç yapısı](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-014)

**Seçilebilir üç boyutlu görünümlerle sarayın yapısını ortaya çıkarın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df796856910ffc55-display.jpg" alt="Antik sarayın iç yapısı" height="280"></a>
</p>

[Projeyi aç](https://3526g54twnq3b.space.mcode.cn/)

**İstem**

```text
创建一个页面，展示中国古代宫殿的内部结构，3D，真实材质，支持多种模式切换
```

---


<a id="category-games"></a>
## 🎮 Oyunlar

<a id="case-15"></a>
### Örnek 15: [DANCE2000 ritim oyunu](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-015)

**Şarkı seçiminden eşzamanlı notalara, karakter adımlarına ve puanlamaya ilerleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/de492e064adcfbcf-poster.jpg" alt="DANCE2000 ritim oyunu" height="280"></a>
</p>

[Projeyi aç](https://260srblym7fzp.space.mcode.cn/)

[İstemin tamamını oku](prompts/MM-015.md)

---

<a id="case-16"></a>
### Örnek 16: [Çok oyunculu Flight Chess](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-016)

**Tam oyun tahtasında zarları, sıraları ve taş hareketlerini izleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7de7a4665f8d68d8-poster.jpg" alt="Çok oyunculu Flight Chess" height="280"></a>
</p>

[Projeyi aç](https://low4r5gkb56gq.space.mcode.cn)

[İstemin tamamını oku](prompts/MM-016.md)

---

<a id="case-17"></a>
### Örnek 17: [BAMBOO HOP evcil hayvan uçuşu](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-017)

**Bir hayvan ve manzara seçerek engellerin arasından uçun**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/6f4bf4f7c2af297c-poster.jpg" alt="BAMBOO HOP evcil hayvan uçuşu" height="280"></a>
</p>

[Projeyi aç](https://tjb51tpmdbxvd.space.mcode.cn/)

[İstemin tamamını oku](prompts/MM-017.md)

---

<a id="case-18"></a>
### Örnek 18: [Takip edilen şehirden kaçış](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-018)

**Kuşbakışı şehirde dayanıklılığı, sağlığı ve hedefleri yönetin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e89a71edb82f826c-poster.jpg" alt="Takip edilen şehirden kaçış" height="280"></a>
</p>

[Projeyi aç](https://dk3fzfkfveju6.space.mcode.cn)

**İstem**

```text
**单轮对话任务**：做一款俯视角城市逃生游戏。玩家用 WASD 或方向键穿过街区，躲避会追踪的敌人，并管理奔跑时消耗、停下后恢复的耐力；收集三把钥匙依次打开封锁道路，医疗包可以恢复生命。到达地图另一端的安全区即获胜，生命耗尽则失败；提供小地图、目标提示、命中反馈、暂停和重新开始。
```

---


<a id="category-web"></a>
## 🖥️ Web arayüzleri

<a id="case-19"></a>
### Örnek 19: [Retro restoran sitesi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-019)

**Çarpıcı restoran kimliğini menü ve rezervasyon gezinmesiyle birleştirin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0bbae8b0a1f099fb-display.jpg" alt="Retro restoran sitesi" height="280"></a>
</p>

[Projeyi aç](https://pxv1w29d70k1l.space.mcode.cn)

**İstem**

```text
请设计并实现上海本帮菜餐厅「海上春饭店 HAISHANG CHUN」的网站，整体呈现千禧年中国电视广告、早期 CGI 与中式书法融合的复古 Y2K 风格。首页采用占满视口的动态视觉舞台，背景由顶部桃橙色、中部蓝色、下部草绿与墨绿色、底部深蓝色形成连续的多段渐变，色带之间大范围柔焦融合，营造朦胧的天空与地平线空间感；渐变覆盖整个屏幕，并叠加细密颗粒、轻微色彩溢出与录像带质感。画面中央悬浮巨大的朱红色立体书法「海上春饭店」，保留毛笔笔锋，具有明显挤出厚度、侧面阴影和早期数码塑料光泽，缓慢旋转、漂浮与推近；周围穿插花瓣、香料、彩色球体和植物的超现实动画。顶部导航直接叠在渐变背景上，使用紧凑的红色中英双语文字，英文品牌居中；底部中央显示柠檬黄黑描边电影字幕「今朝吃点好的。 / Something good on the table.」，右下角设置黄色细边框的圆角餐桌影像窗口，左下角提供声音与动态控制。菜单作为独立页面，采用高饱和蓝底、巨型绿色「菜单」字、大号衬线英文导航、斜体下划线选中状态和黑色点线菜价，中文菜名在上、英文在下、人民币价格右对齐；关于、订座等页面延续鲜红、亮粉、绿色的大面积色块与闪光灯餐桌摄影。使用 React、TypeScript、Vite、Tailwind CSS 与原生 CSS 开发，Three.js／WebGL 实现渐变场景和立体文字，GSAP 编排漂浮、镜头与字幕转场，React Router 管理页面；字体、图片和影像本地加载，菜单数据独立维护，适配电脑与手机，支持暂停动态及减少动态效果，交付完整源码、可运行页面和启动说明。
```

---

<a id="case-20"></a>
### Örnek 20: [Bir parfüm markası sitesi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-020)

**Marka malzemelerini uyumlu siteye ve medya iş akışına dönüştürün**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b708369d197974de-display.jpg" alt="Bir parfüm markası sitesi" height="280"></a>
</p>

[Projeyi aç](https://yhnj4qzy5fg2e.space.mcode.cn/)

[İstemin tamamını oku](prompts/MM-020.md)

---

<a id="case-21"></a>
### Örnek 21: [GTA tarzı kişilik testi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-021)

**Temalı sorular ve karaktere dayalı sonuç ekranı oluşturun**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f110fb729649aca6-display.jpg" alt="GTA tarzı kişilik testi" height="280"></a>
</p>

[Projeyi aç](https://3ir72drzi62wq.space.mcode.cn/)

[İstemin tamamını oku](prompts/MM-021.md)

---

<a id="case-22"></a>
### Örnek 22: [Sinematik kaydırmalı site](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-022)

**H3 görüntülerini M3.1 ön yüz düzeni ve hareketleriyle birleştirin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d47ef2420d0ee3fd-display.jpg" alt="Sinematik kaydırmalı site" height="280"></a>
</p>

[Projeyi aç](https://d3piolkdzfrut.space.mcode.cn/)

**İstem**

```text
请设计并实现一个原创的实验性数字创意工作室网站，整体参考古典出版物气质、文艺复兴绘画、旧式排版与当代数字交互，但不得复制其品牌、文案、画面和具体构图；网站不是传统纵向长页面，而是一个始终固定在视口中的全屏电影舞台，背景使用一段原创、无硬切、约 40–60 秒的连续“一镜到底”长视频，以《仲夏夜之梦》为主题，镜头从精灵公主指尖停驻的蝴蝶极近景开始，跟随她追逐蝶群、穿过幽暗森林，进入繁花与藤蔓环绕的月夜花园。公主在喷泉旁遇见王子，两人牵手起舞，镜头一镜到底绕过舞者、穿过喷泉水幕，再随蝶群升至树冠上方，展现森林环抱的花园、月光下起舞的人群，以及低悬天际的巨大月亮。使前后镜头在景别、空间、主体和尺度上形成强烈跨度，同时通过遮挡转场、急速推镜、变焦模糊、空间变形和匹配运动自然衔接；用户向上或向下滚动时不进入新的页面区块，而是将滚动进度精确映射到视频 currentTime，实现可前进、暂停和倒放的 scroll-scrub 影片体验，章节标题、宣言和说明文字只作为覆盖层在对应时间点淡入、位移、套色并消失；视觉采用深森林绿、黑色、旧纸米黄、锈红、暗金和少量钴蓝，结合衬线字体、超大压缩标题、错版套印、Letterpress 颗粒、胶片噪点、暗角、细线网格和博物馆式图注；顶部固定 MORROW 品牌字标、罗马数字章节导航与 INDEX 按钮，点击章节可平滑跳转到对应影片时间，INDEX 打开大幅旧纸目录弹层，底部显示影片进度线、章节节点、当前章节编号和滚动提示；技术栈使用 React + Vite/Next.js + TypeScript，HTML5 Video、requestAnimationFrame、Pointer Events、CSS Custom Properties 与 Intersection Observer，实现视频预加载、Poster 兜底、短 GOP 编码以保证拖动定位流畅、桌面与移动端响应式适配、触控滚动、键盘导航、prefers-reduced-motion 降级和 60fps 性能优化，最终输出完整可运行的网站，确保用户看到的始终是一条可被滚动探索的连续电影，而不是由多个普通网页区块组成的长页面。
```

---

<a id="case-23"></a>
### Örnek 23: [Terminal tarzı yaratıcı arşiv](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-023)

**Eserleri tek renkli gezinme, filtreler ve video önizlemeleriyle düzenleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/74edf1330fb45196-display.jpg" alt="Terminal tarzı yaratıcı arşiv" height="280"></a>
</p>

[Projeyi aç](https://n2nbcgw6hbpr7.space.mcode.cn/)

[İstemin tamamını oku](prompts/MM-023.md)

---

<a id="case-24"></a>
### Örnek 24: [Tarayıcıda Windows XP masaüstü](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-024)

**Tanıdık masaüstünü, taşınabilir pencereleri ve gömülü uygulamaları birleştirin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/38dcaf9126232cea-display.jpg" alt="Tarayıcıda Windows XP masaüstü" height="280"></a>
</p>

[Projeyi aç](https://p7itx30utl0rg.space.mcode.cn/)

[İstemin tamamını oku](prompts/MM-024.md)

---


<a id="category-visualization"></a>
## 📊 Veri görselleştirme

<a id="case-25"></a>
### Örnek 25: [İklim sarmalını canlandırma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-025)

**Aylık sıcaklık sapmalarını oynatma ve yıl kontrolleriyle keşfedin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e65c6574dbe75386.png" alt="İklim sarmalını canlandırma" height="280"></a>
</p>

[Projeyi aç](https://asel6nns59e7l.space.mcode.cn/)

**İstem**

```text
一组固定的 1880—2025 年全球月度温度异常数据做一个气候螺旋。动画逐年画出十二个月的环形轨迹，中心显示当前年份，背景清楚标出 1.5°C 和 2°C 参考圈；用户可以播放、暂停或拖动年份，并悬停查看当前月份和温度异常值。
```

---

<a id="case-26"></a>
### Örnek 26: [Savaş verileriyle hikâye anlatma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-026)

**Kayıpları ardışık bölümler ve görsel ölçeklerle karşılaştırın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c4786844a40d1bc8.png" alt="Savaş verileriyle hikâye anlatma" height="280"></a>
</p>

[Projeyi aç](https://ofw1iav2nxwlq.space.mcode.cn/)

**İstem**

```text
一组固定的二战伤亡汇总数据做一个克制的数据叙事。滚动依次进入“各国军人伤亡”“军人与平民”“战后冲突对比”三个章节，人物小图标逐步聚合成柱形和时间线；在关键停顿处，用户可以切换国家并比较绝对人数与人口占比。页面要明确单位、数据口径和当前比较对象。
```

---

<a id="case-27"></a>
### Örnek 27: [Antik harikaları görselleştirme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-027)

**İnşa ve korunma bilgilerini açık bir görsel karşılaştırmaya dönüştürün**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3ce710bb5b1010b6.png" alt="Antik harikaları görselleştirme" height="280"></a>
</p>

[Projeyi aç](https://q02qt318izml9.space.mcode.cn/)

**İstem**

```text
主题：古代世界七大奇迹的建造与现存：请围绕“古代世界七大奇迹”做一张数据可视化。从七大奇迹中选取 5 个，整理它们的建造耗时、现存高度或保存状态等数据。图表类型根据数据特点选择，注明数据为公开资料估算。标题要好玩，避免涉及敏感政治、宗教和领土内容。
```

---

<a id="case-28"></a>
### Örnek 28: [Yurt dışı başlangıç pazarlarını karşılaştırma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-028)

**Pazar göstergelerini keşfedin ve olası giriş ülkelerini karşılaştırın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/2b7571af4d1ea417.png" alt="Yurt dışı başlangıç pazarlarını karşılaştırma" height="280"></a>
</p>

[Projeyi aç](https://825z92nzmpz5i.space.mcode.cn/)

**İstem**

```text
信息截止时间固定为 2026 年 9 月 15 日。基于世界银行、金融和学术数据源，帮 iShout 判断首批应该进入哪些海外市场。需要综合考虑人均 GDP、互联网和智能手机渗透率、内容创作者生态规模、便携音频设备的消费电子市场体量，给出 Top 5 推荐市场以及每个市场的数据依据，输出一个可交互网页。将随题参考图作为 iShout 产品概念和定位的背景信息；图中的品牌标识和营销文案不视为已经核实的事实，也不要在成品中复制这些标识。
```

---


<a id="category-multimodal"></a>
## 🎬 Çok modlu iş akışları

<a id="case-29"></a>
### Örnek 29: [Filmi çekimlere ayırma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-029)

**Videoyu çekim, ses ve ekran yazılarından oluşan bir tabloya eşleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0d276dbb38fe2511-poster.jpg" alt="Filmi çekimlere ayırma" height="280"></a>
</p>

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/159da4fa9b1d5088.xlsx)

**İstem**

```text
请完整观看并分析这段视频，按实际剪辑切点逐镜头拆解，不要按固定时间间隔划分，不要遗漏快速闪过的短镜头。用表格输出：镜号、起止时间码、时长、景别与拍摄角度、构图、场景与人物动作、镜头运动、转场、对白／旁白原文、音乐／音效、画面文字。同一镜头内的动作和运镜变化按发生顺序写清，声音与对应画面对齐，不要只概括剧情。时间码尽可能准确；看不清、听不清或无法读取的部分明确标注，不要猜测补写。
```

---

<a id="case-30"></a>
### Örnek 30: [Görüntü farklarını bulma ve işaretleme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-030)

**İki görüntüyü karşılaştırıp yan yana açıklamalı sonuç üretin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e91973c03cbd9f7c-display.jpg" alt="Görüntü farklarını bulma ve işaretleme" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/28d91bba13dfb336-display.jpg" alt="Görüntü farklarını bulma ve işaretleme" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/73a2e5b34e66f2e1.png" alt="Görüntü farklarını bulma ve işaretleme" height="280"></a>
</p>

**İstem**

```text
找出这两幅图片之间的不同之处并圈出来，给我一个对比图
```

---

<a id="case-31"></a>
### Örnek 31: [Kırmızı ahtapotla referans film uyarlaması](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-031)

**Verilen film tarzını oyuncak karaktere ve yeni kısa filme uyarlayın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d59c7ca9568eec60-poster.jpg" alt="Kırmızı ahtapotla referans film uyarlaması" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8acfdff023945cef.png" alt="Kırmızı ahtapotla referans film uyarlaması" height="280"></a>
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b9bea30b7bed8645-poster.jpg" alt="Kırmızı ahtapotla referans film uyarlaması" height="280"></a>
</p>

**İstem**

```text
复刻上传的视频风格，物体改为一个红色章鱼玩偶，文案和背景音乐都由你自己生成
视频链接是https://www.bilibili.com/video/BV1XHBXBaENH/?share_source=copy_web&vd_source=5c669de4ca13e0dab99325937e8c4cbb
```

---

<a id="case-32"></a>
### Örnek 32: [MiniMax Design marka filmi uyarlaması](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-032)

**Referans görüntüleri yeni bir marka hareket dizisine dönüştürün**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/445d044cb416e662-poster.jpg" alt="MiniMax Design marka filmi uyarlaması" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/51f952c5a7ba11de-poster.jpg" alt="MiniMax Design marka filmi uyarlaması" height="210"></a></td>
</tr></tbody></table>

**İstem**

```text
复刻上传的视频，软件名称从MiniMax H3改为MiniMax Design，logo请自行在网上搜索，文案自行研究 MiniMax Design官网的最新公开信息来进行编写
```

---

<a id="case-33"></a>
### Örnek 33: [Dil modelleri hakkında kodla oluşturulan film](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-033)

**Python görselleri, tipografi ve kurguyla deneysel bir kısa film oluşturun**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/f1907748af3c39bb-poster.jpg" alt="Dil modelleri hakkında kodla oluşturulan film" height="280"></a>
</p>

**İstem**

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
### Örnek 34: [IChO Avogadro sorusunu çözme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-034)

**Kimya sorusunu okuyun ve on bir alt soruyu adım adım çözün**

[Sonucu görüntüle](sources/icho-solution.md)

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b29e8aae314fa1c6.pdf)

**İstem**

```text
做一下这个题
```

---


<a id="category-presentation"></a>
## 📑 Sunumlar

<a id="case-46"></a>
### Örnek 46: [Elektrikli araç sektörü sunumu](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-046)

**Bölgesel karşılaştırmaları, grafikleri ve sonuçları danışmanlık düzeninde birleştirin**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b416fde93e373d27.png" alt="Elektrikli araç sektörü sunumu" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8262a19b5130108b.png" alt="Elektrikli araç sektörü sunumu" height="210"></a></td>
</tr></tbody></table>

---

<a id="case-47"></a>
### Örnek 47: [Üretken video pazarı sunumu](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-047)

**Yoğun pazar bilgisini uyumlu grafikler ve tablolarla düzenleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/d3e4804aba65463e.png" alt="Üretken video pazarı sunumu" height="280"></a>
</p>

---

<a id="case-48"></a>
### Örnek 48: [CampusOS ürün sunumu](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-048)

**Kampüs ürünü ve modülleri etrafında tutarlı görsel anlatı kurun**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/efd76855a0e928d2.png" alt="CampusOS ürün sunumu" height="280"></a>
</p>

---

<a id="case-49"></a>
### Örnek 49: [Uygarlığın kökeni dersi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-049)

**İspanyolca eğitim sayfalarında müze tarzı görüntüler ve tipografi kullanın**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1b7ae54ae44f7f13.png" alt="Uygarlığın kökeni dersi" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/b1ce20000dfd9045.png" alt="Uygarlığın kökeni dersi" height="210"></a></td>
</tr></tbody></table>

---

<a id="case-50"></a>
### Örnek 50: [Editoryal tarzda konuşma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-050)

**Soyut fikirlere tek renkli yazı ve şemalarla açık bir ritim kazandırın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/920bba33668135e7.png" alt="Editoryal tarzda konuşma" height="280"></a>
</p>

---

<a id="case-51"></a>
### Örnek 51: [Resimli ses bilgisi dersi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-051)

**Bir sözcük ailesini yinelenen resimler ve sınıf etkinlikleriyle bağlayın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/86ffb61d8ce64b2b.png" alt="Resimli ses bilgisi dersi" height="280"></a>
</p>

---

<a id="case-52"></a>
### Örnek 52: [Everest arazi sunumu](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-052)

**Yükseklik, rota ve riskleri şemalar ve karşılaştırma sayfalarıyla açıklayın**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0c1352a3f74c6d06.png" alt="Everest arazi sunumu" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62098ea7fec1e9b5.png" alt="Everest arazi sunumu" height="210"></a></td>
</tr></tbody></table>

---

<a id="case-53"></a>
### Örnek 53: [Bali'de yedi günlük gezi özeti](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-053)

**Gezi planını uyumlu günlük sayfalara ve bütün yolculuk görünümüne dönüştürün**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/bb2145e35ddb1486.png" alt="Bali&#x27;de yedi günlük gezi özeti" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/88b30bedd4a8eb00.png" alt="Bali&#x27;de yedi günlük gezi özeti" height="210"></a></td>
</tr></tbody></table>

---


<a id="category-science"></a>
## 🔬 Bilimsel ve görsel hesaplama

<a id="case-42"></a>
### Örnek 42: [Faz dizili anteni yeniden yapılandırma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-042)

**Işın yönü ve yan lob kısıtları altında faz ayarlarını görselleştirin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/7d28029b231f7879.gif" alt="Faz dizili anteni yeniden yapılandırma" height="280"></a>
</p>

---

<a id="case-43"></a>
### Örnek 43: [Destek yapısını optimize etme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-043)

**Sabit yük ve malzeme bütçesi altında malzeme dağılımını araştırın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/cb1d698cadb47d71.gif" alt="Destek yapısını optimize etme" height="280"></a>
</p>

---

<a id="case-44"></a>
### Örnek 44: [Esnek nesneleri benzetme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-044)

**Yeniden oluşturulmuş nesneleri farklı fiziksel koşullarda karşılaştırın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef.mp4"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c94002dd0277d3ef-poster.jpg" alt="Esnek nesneleri benzetme" height="280"></a>
</p>

---

<a id="case-45"></a>
### Örnek 45: [Çift kamera videosunu birleştirme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-045)

**İki giriş görüntüsünü hizalanmış panoramik sonuçla karşılaştırın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/62ab881afbaf49ee.png" alt="Çift kamera videosunu birleştirme" height="280"></a>
</p>

---


<a id="category-performance"></a>
## ⚡ Performans iyileştirme

<a id="case-9"></a>
### Örnek 9: [Flowdesk analizi ve iyileştirmesi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-009)

**Yavaş ekranları izleyin, iş işlemlerini koruyun ve üç ölçüm turunu karşılaştırın**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0be01d25aae9e4d5.png" alt="Flowdesk analizi ve iyileştirmesi" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/c6ea50b7835b7f86.png" alt="Flowdesk analizi ve iyileştirmesi" height="210"></a></td>
</tr></tbody></table>

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/414dd588fb6d5834.zip) · [Sonucu görüntüle 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/df80eba46d1f48b2.zip)

**İstem**

```text
你接手一个已有的本地客服工单工作台，不是从零开发。用户报告：进入列表很慢，输入搜索时卡顿，在工单/概览间多次切换后情况更差。请自主操作浏览器与性能工具，定位实际原因并修复，保留已有业务功能。
启动 node server.cjs，监听端口由终端输出给出；不要碰其他服务。目录已有 browser-kit.cjs，可 require 它使用 Playwright Chromium，支持通过 newCDPSession 使用 Chrome DevTools Protocol。你也可以使用当前环境其他可用的电脑/浏览器工具。
要求先在真实浏览器复现，再录制修复前的 Chrome 性能 trace 或 CPU profile，同时检查 Network 请求、DOM 数量、Layout/脚本耗时。不能只看源码猜原因，不能把单个函数的计时当成用户操作时间。保留原始证据。自己选择测量方法，解释指标实际覆盖什么。
修复后重复相同输入和操作序列，使用同一8000条数据，至少3轮测量；不要减少数据、取消搜索、隐藏错误、只显示固定前几条或删除原有功能来提升数字。列表必须能访问最后一条，搜索、状态筛选、金额排序、详情、勾选、批量处理、完整导出都需保留。页面切换不应丢掉本次已修改的工单状态。
最终保存：修复前后原始trace/profile、测量JSON、桌面截图、RESULT.md（复现→证据→根因→修改→验证→残留问题）。截图后使用图片读取工具检查。说明是否使用浏览器自动化或原生桌面操作，不能混称。无需人工指导，尽量自主完成诊断到复测；不改browser-kit，不安装全仓依赖，不需要发布。给成品与证据，不能只有分析报告。

```

---

<a id="case-10"></a>
### Örnek 10: [rsync performansını yinelemeli iyileştirme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-010)

**Her optimizasyonu izleyin ve iki kıyaslama kaydını ayrı tutun**

<table><tbody><tr>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e05739d66959e205.png" alt="rsync performansını yinelemeli iyileştirme" height="210"></a></td>
<td align="center"><a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/39a351368d139e82.gif" alt="rsync performansını yinelemeli iyileştirme" height="210"></a></td>
</tr></tbody></table>

---


<a id="category-research"></a>
## 🧪 Algoritma araştırması

<a id="case-41"></a>
### Örnek 41: [Zaman serisi eksik değerlerini yinelemeli tamamlama](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-041)

**Sabit görev ayarında deneyleri, bileşen çıkarma testlerini ve yeniden ölçümleri izleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/422fa991740011e9.gif" alt="Zaman serisi eksik değerlerini yinelemeli tamamlama" height="280"></a>
</p>

---


<a id="category-finance"></a>
## 📈 Finansal araştırma ve modelleme

<a id="case-35"></a>
### Örnek 35: [Bir BOE etkinliğini araştırma](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-035)

**Olay incelemesini tarihsel karşılaştırmalar ve tarihli senaryolarla yapılandırın**

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1e131881231a01c5.md)

**İstem**

```text
对于明天的京东方超大规模的百人调研事件和对股价的潜在走势进行推演，并在历史上追溯过去几次的情况和相似性。
```

---

<a id="case-36"></a>
### Örnek 36: [PCB beklenti farklarını inceleme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-036)

**Sektör raporunda pazar anlatılarını işletme kanıtlarından ayırın**

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/0cbe3c574b5e08fc.md)

**İstem**

```text
分析一下 PCB 板块目前有哪些预期差。
```

---

<a id="case-37"></a>
### Örnek 37: [Vera Rubin tedarik zincirini haritalama](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-037)

**Platform düzeylerini, tedarik ilişkilerini ve kanıt derecelerini şemada düzenleyin**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8508826efbfcc0af.png" alt="Vera Rubin tedarik zincirini haritalama" height="280"></a>
</p>

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/8889bb403cd7f264.html)

**İstem**

```text
拆解 Vera Rubin 产业链并制成图表。
```

---

<a id="case-38"></a>
### Örnek 38: [Kauçuk zincirindeki aktarımı modelleme](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-038)

**Hammadde senaryolarını lastik maliyeti, fiyatlandırma ve kâr şemalarına bağlayın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/a76a61330b187632.png" alt="Kauçuk zincirindeki aktarımı modelleme" height="280"></a>
</p>

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/844630115d45f40f.md) · [Sonucu görüntüle 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/388c6c6ef297587f.html) · [Sonucu görüntüle 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/090d3b23d68df28f.xlsx)

**İstem**

```text
给定橡胶产业链上游的订单和产能变化，向下游传导去进行建模，推算各个环节的影响和市场空间
```

---

<a id="case-39"></a>
### Örnek 39: [Üç mali tablo ve DCF çalışma kitabı](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-039)

**Varsayımları, mali tabloları, değerlemeyi ve dayanak verileri bağlayın**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/3d49a937b9f4a592.png" alt="Üç mali tablo ve DCF çalışma kitabı" height="280"></a>
</p>

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/1c7361281c27dfeb.xlsx)

**İstem**

```text
给贵州茅台生成一个完整的三张表模型，包括DCF估值部分。
```

---

<a id="case-40"></a>
### Örnek 40: [Opsiyon portföyü risk paketi](https://github.com/cheercheung/awesome-minimax-m3-1-guide/blob/main/sources/handbook.md#mm-040)

**Pozisyonları risk notuna, bağlantılı çalışma kitabına ve hesaplama betiğine dönüştürün**

<p align="center">
<a href="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png"><img src="https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/41a55f70b7f1d2f6.png" alt="Opsiyon portföyü risk paketi" height="280"></a>
</p>

[Sonucu görüntüle 1](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/942c1d385ba7c6cc.zip) · [Sonucu görüntüle 2](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/11e06ea49a285da0.md) · [Sonucu görüntüle 3](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/e0978b7143a373a4.xlsx) · [Sonucu görüntüle 4](https://pub-62cf7640cd0f4066b60933bd2e9b85ef.r2.dev/model-repo-media/awesome-minimax-m3-1-guide/assets/source/35d63b32974e1b83.py)

[İstemin tamamını oku](prompts/MM-040.md)

---


<a id="category-engineering"></a>
## 🛠️ Hata ayıklama ve özellikler

<a id="case-1"></a>
### Örnek 1: [Terminalin doğal kaydırmasını koruma](https://github.com/MiniMax-AI/minimax-code/pull/306) (yazan [@hetaoBackend](https://github.com/hetaoBackend))

**Etkinlik satırları kaybolurken uzun konuşmanın mevcut konumunu koruyun**

<sub>2026-09-22</sub>

---

<a id="case-2"></a>
### Örnek 2: [Çakışan SQLite yazmalarını yeniden deneme](https://github.com/MiniMax-AI/minimax-code/pull/319) (yazan [@zch0227](https://github.com/zch0227))

**Görev kabulü, durum güncellemesi ve tamamlanması boyunca eşzamanlı yazmaları yönetin**

<sub>2026-09-22</sub>

---

<a id="case-3"></a>
### Örnek 3: [Sonsuz aralık bölmelerini durdurma](https://github.com/moment/luxon/pull/1810) (yazan [@EaseLearnAI](https://github.com/EaseLearnAI))

**Geçerli takvim davranışını korurken negatif süreleri ve ilerlemeyen sınırları denetleyin**

<sub>2026-09-22</sub>

---

<a id="case-4"></a>
### Örnek 4: [Bileşensiz ISO sürelerini reddetme](https://github.com/moment/luxon/pull/1812) (yazan [@EaseLearnAI](https://github.com/EaseLearnAI))

**Boş süreyi geçerli ve açıkça belirtilmiş sıfırdan ayırın**

<sub>2026-09-22</sub>

---

<a id="case-5"></a>
### Örnek 5: [Seçilebilir terminal temaları](https://github.com/MiniMax-AI/minimax-code/pull/311) (yazan [@hetaoBackend](https://github.com/hetaoBackend))

**Adlandırılmış paletleri, canlı önizlemeyi ve kalıcı ayarları birleştirin**

<sub>2026-09-22</sub>

---

<a id="case-6"></a>
### Örnek 6: [mcode ile claude-tap bağlantısı](https://github.com/liaohch3/claude-tap/pull/441) (yazan [@hetaoBackend](https://github.com/hetaoBackend))

**Filtreli kayıtlar ve iz görüntüleyici kanıtlarıyla kodlama istemcisini entegre edin**

<sub>2026-08-16</sub>

---

<a id="case-7"></a>
### Örnek 7: [Dinamik iş akışlarını inceleme ve onarma](https://github.com/MiniMax-AI/MiniMax-Code-Plugins/pull/42) (yazan [@hetaoBackend](https://github.com/hetaoBackend))

**Çalıştırmadan önce topolojiyi inceleyin ve başarısız adımları onarın**

<sub>2026-09-17</sub>

---

<a id="case-8"></a>
### Örnek 8: [acpx için mcode profili](https://github.com/openclaw/acpx/pull/503) (yazan [@hetaoBackend](https://github.com/hetaoBackend))

**MiniMax Code'u yerleşik ACP aracı profiliyle bağlayın**

<sub>2026-08-16</sub>

---

## 📖 Kılavuzlar

- [Görev seçimi](docs/guide/tr/task-selection.md)
- [Akıl yürütme derinliği](docs/guide/tr/reasoning.md)
- [Görüntü ve video](docs/guide/tr/multimodal.md)
- [Bağlam ve önbellek](docs/guide/tr/context-cache.md)
- [Görevden teslimata iş akışı](docs/guide/tr/workflows.md)
- [M3 ve Preview sürümünden geçiş](docs/guide/tr/migration.md)
- [Protokol alanları başvurusu](docs/guide/tr/protocols.md)

<a id="acknowledge"></a>
## 🙏 Teşekkürler

Malzemeler sağlanan MiniMax M3.1 Flash el kitabından ve bağlantılı projelerden alınmıştır. Açık katkıda bulunanlara teşekkürler:

[@EaseLearnAI](https://github.com/EaseLearnAI), [@hetaoBackend](https://github.com/hetaoBackend), [@zch0227](https://github.com/zch0227)

Üçüncü taraf medya ve istemlerin hakları üreticilerinde kalır. Editoryal içeriğin lisansı: [CC BY 4.0](LICENSE) · [Medya politikası](docs/media-policy.md)

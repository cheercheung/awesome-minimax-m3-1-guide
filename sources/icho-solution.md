# IChO 2009 · Problem 1

[Source](handbook.md#mm-034)

```text
附件是 ICHO 2009 理论第 1 题，共 11 小问。我把附件内容仅作为题目读取，答案如下。 VOLUME 3 - ICHO 41-45 _opravené_.pdf
Method A：由金晶格估算
1.1 FCC 晶胞含有多少个 Au 原子？
面心立方晶胞：
\[ 8\times\frac18+6\times\frac12=4 \]
所以每个晶胞含有
\[ \boxed{4\text{ 个 Au 原子}} \]
1.2 晶胞体积和质量
晶胞边长：
\[ a=0.408\text{ nm}=4.08\times10^{-10}\text{ m} \]
体积：
\[ V_{\text{cell}}=a^3 =(4.08\times10^{-10})^3 =6.79\times10^{-29}\text{ m}^3 \]
质量：
\[ m_{\text{cell}}=\rho V =(1.93\times10^4)(6.79\times10^{-29}) \]\[ \boxed{m_{\text{cell}}=1.31\times10^{-24}\text{ kg}} \]
1.3 一个 Au 原子的质量及阿伏伽德罗常数
\[ m_{\text{Au}}=\frac{m_{\text{cell}}}{4} =3.28\times10^{-25}\text{ kg} \]
金的摩尔质量为
\[ M_{\text{Au}}=196.97\text{ g mol}^{-1} =0.19697\text{ kg mol}^{-1} \]
因此
\[ N_A=\frac{M_{\text{Au}}}{m_{\text{Au}}} =\frac{0.19697}{3.28\times10^{-25}} \]\[ \boxed{N_A\approx6.01\times10^{23}\text{ mol}^{-1}} \]
Method B：放射性衰变
1.4 判断 \(\alpha\) 衰变和 \(\beta^-\) 衰变
衰变类型
\({}^{226}\mathrm{Ra}\to{}^{222}\mathrm{Rn}\)\(\alpha\)
\({}^{222}\mathrm{Rn}\to{}^{218}\mathrm{Po}\)\(\alpha\)
\({}^{218}\mathrm{Po}\to{}^{214}\mathrm{Pb}\)\(\alpha\)
\({}^{214}\mathrm{Pb}\to{}^{214}\mathrm{Bi}\)\(\beta^-\)
\({}^{214}\mathrm{Bi}\to{}^{214}\mathrm{Po}\)\(\beta^-\)
\({}^{214}\mathrm{Po}\to{}^{210}\mathrm{Pb}\)\(\alpha\)
\({}^{210}\mathrm{Pb}\to{}^{210}\mathrm{Bi}\)\(\beta^-\)
\({}^{210}\mathrm{Bi}\to{}^{210}\mathrm{Po}\)\(\beta^-\)
\({}^{210}\mathrm{Po}\to{}^{206}\mathrm{Pb}\)\(\alpha\)
1.5 40 天后第一个未达到稳态的核素
前面的短寿命核素在 40 天内已经基本达到稳态；而
\[ t_{1/2}({}^{210}\mathrm{Pb})=22.3\text{ 年} \]
远大于 40 天，因此 \({}^{210}\mathrm{Pb}\) 的生成速率和衰变速率还没有相等。
\[ \boxed{{}^{210}\mathrm{Pb}} \]
1.6 163 天内产生的 \(\alpha\) 粒子数
按题目常规处理，将测得的总 \(\alpha\) 衰变速率近似看作这 163 天内的平均恒定速率。
\[ t=163\times24\times3600 =1.40832\times10^7\text{ s} \]\[ A=27.7\text{ GBq}=2.77\times10^{10}\text{ s}^{-1} \]
所以
\[ N_\alpha=At =(2.77\times10^{10})(1.40832\times10^7) \]\[ \boxed{N_\alpha=3.90\times10^{17}} \]
1.7 由氦气体积求 \(N_A\)
氦气体积：
\[ V=10.4\text{ mm}^3=10.4\times10^{-9}\text{ m}^3 \]
氦气的物质的量：
\[ n_{\mathrm{He}}=\frac{PV}{RT} \]\[ n_{\mathrm{He}} =\frac{(101325)(10.4\times10^{-9})} {(8.3145)(273)} =4.64\times10^{-7}\text{ mol} \]
每个 \(\alpha\) 粒子最终形成一个 He 原子，因此
\[ N_\alpha=n_{\mathrm{He}}N_A \]\[ N_A=\frac{N_\alpha}{n_{\mathrm{He}}} =\frac{3.90\times10^{17}}{4.64\times10^{-7}} \]\[ \boxed{N_A\approx8.40\times10^{23}\text{ mol}^{-1}} \]
1.8 计算 Ra 原子数、衰变常数和半衰期
Ra 的物质的量：
\[ n_{\mathrm{Ra}}=\frac{0.192}{226.25} =8.49\times10^{-4}\text{ mol} \]
使用 \(N_A=6.022\times10^{23}\text{ mol}^{-1}\)：
\[ N_{\mathrm{Ra}} =(8.49\times10^{-4})(6.022\times10^{23}) \]\[ \boxed{N_{\mathrm{Ra}}=5.11\times10^{20}\text{ 个}} \]
在到达 \({}^{210}\mathrm{Pb}\) 之前，每发生一次 Ra 衰变链的完整过程，有 4 个 \(\alpha\) 衰变：
\[ {}^{226}\mathrm{Ra},\ {}^{222}\mathrm{Rn},\ {}^{218}\mathrm{Po},\ {}^{214}\mathrm{Po} \]
所以 Ra 的活度为
\[ A_{\mathrm{Ra}}=\frac{27.7\times10^9}{4} =6.925\times10^9\text{ s}^{-1} \]
衰变常数：
\[ \lambda=\frac{A_{\mathrm{Ra}}}{N_{\mathrm{Ra}}} =\frac{6.925\times10^9}{5.11\times10^{20}} \]\[ \boxed{\lambda=1.36\times10^{-11}\text{ s}^{-1}} \]
半衰期：
\[ t_{1/2}=\frac{\ln2}{\lambda} =5.12\times10^{10}\text{ s} \]
换算成年：
\[ \boxed{t_{1/2}\approx1.62\times10^3\text{ 年}} \]
Method C：Perrin 胶体粒子沉降法
粒子半径：
\[ r=2.12\times10^{-7}\text{ m} \]
粒子体积：
\[ V_p=\frac43\pi r^3 =3.99\times10^{-20}\text{ m}^3 \]
1.9 质量和有效质量
(i) 粒子质量：
\[ m=\rho_pV_p =(1.206\times10^3)(3.99\times10^{-20}) \]\[ \boxed{m=4.81\times10^{-17}\text{ kg}} \]
(ii) 排开的水的质量：
\[ m_{\mathrm{H_2O}}=\rho_wV_p =(999)(3.99\times10^{-20}) \]\[ \boxed{m_{\mathrm{H_2O}}=3.99\times10^{-17}\text{ kg}} \]
(iii) 考虑浮力后的有效质量：
\[ m'=m-m_{\mathrm{H_2O}} \]\[ \boxed{m'=8.26\times10^{-18}\text{ kg}} \]
1.10 推导图线斜率
每个粒子的有效质量为 \(m'\)，一摩尔粒子的有效质量为 \(m'N_A\)。因此
\[ E_h-E_{h_0}=m'N_Ag(h-h_0) \]
代入玻尔兹曼分布：
\[ \ln\left(\frac{n_h}{n_{h_0}}\right) =-\frac{m'N_Ag}{RT}(h-h_0) \]
所以图线梯度为
\[ \boxed{ \frac{\mathrm d\ln(n_h/n_{h_0})} {\mathrm d(h-h_0)} =-\frac{m'N_Ag}{RT} } \]
1.11 由斜率求 \(N_A\)
由图上拟合直线读出：
\[ s\approx-0.025\ \mu\text{m}^{-1} =-2.5\times10^4\text{ m}^{-1} \]
因此
\[ N_A=-\frac{sRT}{m'g} \]
取 \(T=288\text{ K}\)、\(g=9.81\text{ m s}^{-2}\)：
\[ N_A =\frac{(2.5\times10^4)(8.3145)(288)} {(8.26\times10^{-18})(9.81)} \]\[ \boxed{N_A\approx7.4\times10^{23}\text{ mol}^{-1}} \]
若直接用表中四个数据点作线性拟合，得到约 \(7.0\times10^{23}\text{ mol}^{-1}\)，差异来自读图和实验数据误差。
```

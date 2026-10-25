# 03 · XOR 核心性质与算法应用

整理日期：2026-10-25。

本文根据研究讨论整理，以维基百科相关条目为索引，补充公式推导、反例和算法应用。“完整”指核心性质体系，不表示穷尽全部 XOR 研究。推论与证明是本文整理内容，不应视为参考条目的逐字表述。XOR 是运算；前缀异或、异或基等是利用它构造的算法。

## 约定

默认讨论非负整数或等长比特串。$\oplus$ 表示 XOR，$\land$ 表示按位 AND，$\lor$ 表示按位 OR。取反固定为 $w$ 位，令 $U=2^w-1$，$\neg a=a\oplus U$。普通加法使用不溢出的整数算术。

Python 的异或符号为 ^，乘方为 **。Python 的 ~a 不是固定宽度取反；当 $0\le a<2^w$ 时，可用 a ^ ((1 << w) - 1) 模拟固定宽度取反。

## 1. 定义与逐位独立性

| a | b | a ⊕ b |
|---|---|---|
| 0 | 0 | 0 |
| 0 | 1 | 1 |
| 1 | 0 | 1 |
| 1 | 1 | 0 |

单比特满足 $a\oplus b=(a+b)\bmod2$。对整数则逐位计算，不进位：[1][8]

$$
a\oplus b=\sum_i ((a_i+b_i)\bmod2)\,2^i.
$$

例如 $5\oplus3=101_2\oplus011_2=110_2=6$。整数整体的 $(a+b)\bmod2$ 只保留奇偶性，不等于整数按位异或。某位的改变不会通过进位影响其他位。

## 2. 基本代数性质

| 性质 | 公式 | 用途 |
|---|---|---|
| 交换律 | $a\oplus b=b\oplus a$ | 调整顺序 |
| 结合律 | $(a\oplus b)\oplus c=a\oplus(b\oplus c)$ | 任意分组 |
| 单位元 | $a\oplus0=a$ | 初始化累积结果 |
| 自逆性 | $a\oplus a=0$ | 成对消去 |
| 消去律 | $(a\oplus b)\oplus b=a$ | 恢复已知混合量 |
| 相等判定 | $a\oplus b=0\iff a=b$ | 比较输入 |
| 方程求解 | $a\oplus x=b\iff x=a\oplus b$ | 唯一求解未知量 |

这些性质逐位继承模 2 加法。[1][8] 消去律的证明：

$$
(a\oplus b)\oplus b=a\oplus(b\oplus b)=a\oplus0=a.
$$

XOR 不具备通常的幂等性。$a\oplus a=a$ 仅在 $a=0$ 时成立。

## 3. 多项异或与出现次数的奇偶性

由交换律、结合律和自逆性：

$$
\underbrace{a\oplus\cdots\oplus a}_{n\text{ 次}}
=\begin{cases}0,&n\text{ 偶数},\\a,&n\text{ 奇数}.\end{cases}
$$

可先删除所有出现偶数次的值，再异或剩余值。例如 $a\oplus b\oplus a\oplus c\oplus b=c$。

多个比特的 XOR 为 1，当且仅当其中 1 的数量为奇数，并非“恰好一个输入为 1”：$1\oplus1\oplus1=1$。

反命题不成立：整体异或为零不代表每个值出现偶数次，反例为 $1\oplus2\oplus3=0$。

## 4. 可逆性、双射与信息损失

固定 $k$，令 $T_k(x)=x\oplus k$。因为 $T_k(T_k(x))=x$，所以它是双射且自身就是逆映射。若 $k\ne0$，它没有不动点，因为 $x\oplus k=x$ 会推出 $k=0$。

| 已知信息 | 能否恢复 |
|---|---|
| $a\oplus b$ 与 $b$ | 唯一恢复 $a$ |
| 仅 $a\oplus b$ | 不能唯一恢复两个未知输入 |

在 $w$ 位空间中，$a\oplus b=c$ 有 $2^w$ 对有序解：每个 $a$ 对应唯一的 $b=a\oplus c$。固定一侧时可逆，不代表两份未知数据压成一份后仍能全部恢复。

## 5. 取反、掩码与逻辑等价式

固定 $w$ 位时：

| 性质 | 恒等式 |
|---|---|
| 全 1 掩码取反 | $a\oplus U=\neg a$ |
| 自身与取反异或 | $a\oplus\neg a=U$ |
| 单侧取反 | $(\neg a)\oplus b=\neg(a\oplus b)$ |
| 双侧取反 | $(\neg a)\oplus(\neg b)=a\oplus b$ |
| 与或表达 | $a\oplus b=(a\land\neg b)\lor(\neg a\land b)$ |
| 另一等价式 | $a\oplus b=(a\lor b)\land\neg(a\land b)$ |

逻辑等价式可以用真值表核对。[2] 取反公式则可将 $\neg a$ 换成 $a\oplus U$ 后消去证明。

$a\oplus m$ 只翻转掩码 $m$ 中为 1 的位置。相同掩码应用两次恢复原值。

## 6. 分配律的方向

AND 对 XOR 满足分配律：[2]

$$
a\land(b\oplus c)=(a\land b)\oplus(a\land c).
$$

反过来通常不成立：

$$
a\oplus(b\land c)\ne(a\oplus b)\land(a\oplus c).
$$

反例：单比特 $a=1,b=0,c=1$，左侧为 1，右侧为 0。

XOR 也不对自身分配，因为：

$$
(a\oplus b)\oplus(a\oplus c)=b\oplus c,
$$

通常不等于 $a\oplus(b\oplus c)$。

## 7. 与普通整数加法的关系

非负整数在不溢出的算术下满足：[2]

$$
a+b=(a\oplus b)+2(a\land b).
$$

证明：每一位上，两比特之和等于其 XOR 加上两倍的 AND；按位权重求和即得。

推论：

$$
a\oplus b=a+b-2(a\land b)\le a+b,
$$

$$
a\oplus b=a+b\iff a\land b=0.
$$

两个数没有共同为 1 的位置时，XOR 等于加法。例如 $5\oplus2=7=5+2$，但 $5\oplus3=6\ne8$。

## 8. 大小关系与最高不同位

XOR 不保持整数顺序。例如 $1<2$，但 $1\oplus3=2>1=2\oplus3$。

设 $a\ne b$，第 $h$ 位是两者最高的不同位：

- 若 $k$ 的第 $h$ 位为 0，$a\oplus k$ 与 $b\oplus k$ 保留原大小关系。
- 若该位为 1，大小关系反转。

证明：更高位仍相同，第 $h$ 位仍是最高不同位；翻转该位就交换谁在该位为 1。这是最大异或算法优先考虑高位的依据。

## 9. 位移与位重排

对非负整数和非负移位量 $s$：

$$
(a\oplus b)\ll s=(a\ll s)\oplus(b\ll s),
$$

$$
(a\oplus b)\gg s=(a\gg s)\oplus(b\gg s).
$$

右移使用逻辑右移；固定宽度左移时两侧统一截断。逐位独立性说明先异或再移动，与先移动再异或等价。固定的位重排、循环移位也保持 XOR。

相容不等于可逆。右移会丢弃低位，固定宽度左移会丢弃高位，不能恢复任意输入。

## 10. 群、向量空间与布尔环

固定 $w$ 位比特串在 XOR 下构成交换群，也构成向量空间 $\mathrm{GF}(2)^w$，其加法为 XOR，标量只有 0、1。因此可研究线性相关、基、维数和高斯消元。[3][9]

再以按位 AND 作为乘法，得到布尔环。[4] 当 $w>1$ 时，这不是域 $\mathrm{GF}(2^w)$：非零串 $01$ 与 $10$ 的 AND 为 $00$，存在零因子。扩域必须另外定义乘法。

设 $n$ 个输入向量的秩为 $r$，把每个输入位置是否选取看作一个选择比特。由线性映射的秩–零化度关系可推导：

| 问题 | 结论 |
|---|---|
| 不同的子集异或结果数 | $2^r$ |
| 可达目标对应的选择方案数 | $2^{n-r}$ |
| 不在张成空间内的目标 | 无解 |
| $n$ 个变量、秩为 $r$ 的齐次方程组 | $2^{n-r}$ 个解 |

方案按输入位置区分，包含空集。核的维数为 $n-r$，每个非空原像都是核的陪集，故大小相同。

## 11. 线性、仿射与表达能力

仅使用输入比特、XOR 和常量的表达式，消去重复项后总能写成：

$$
f(x_1,\ldots,x_n)=c\oplus\alpha_1x_1\oplus\cdots\oplus\alpha_nx_n,
\quad c,\alpha_i\in\{0,1\}.
$$

$c=0$ 时线性，允许常数项时为仿射。仅用 XOR 和常量不能表示 AND：若用仿射式表示二元 AND，00、10、01 均输出 0 就迫使常数与两个系数全为 0，因而不能在 11 输出 1。

一般布尔函数可用含乘积项的代数标准形表示，例如 $x_1x_2\oplus x_3\oplus1$，乘积对应 AND。[5]

固定掩码 XOR 通常是仿射而非线性变换：$k\ne0$ 时 $T_k(0)=k\ne0$，不符合线性映射必须将零映射到零的条件。

## 12. 差异、汉明距离与误差检测

二进制串汉明距离为：[6]

$$
d_H(a,b)=\operatorname{popcount}(a\oplus b).
$$

由消去律，共同掩码不改变距离：

$$
d_H(a\oplus k,b\oplus k)
=\operatorname{popcount}(a\oplus k\oplus b\oplus k)=d_H(a,b).
$$

对全部比特求 XOR 得到奇偶校验位。若实际发生奇数个位的翻转，校验值改变；偶数个位翻转则不变。单个奇偶校验位不能检测所有错误，也不能独自定位错误。

## 13. 概率性质与密码学边界

令 $K$ 在全部 $w$ 位串上均匀随机且独立于 $X$，$Y=X\oplus K$。对任意可能的 $x$ 和任意 $y$：

$$
P(Y=y\mid X=x)=P(K=x\oplus y)=2^{-w}.
$$

所以 $Y$ 均匀且独立于 $X$。独立性不能省略：若 $K=X$，即使两者各自均匀，异或结果仍恒为 0。

对于相互独立的比特 $X_1,\ldots,X_n$，令 $P(X_i=1)=p_i$，则：

$$
P(X_1\oplus\cdots\oplus X_n=1)
=\frac{1-\prod_{i=1}^n(1-2p_i)}2.
$$

证明：令 $Z=X_1\oplus\cdots\oplus X_n$。有 $(-1)^Z=\prod_i(-1)^{X_i}$，由独立性：

$$
1-2P(Z=1)=E[(-1)^Z]=\prod_i E[(-1)^{X_i}]
=\prod_i(1-2p_i).
$$

只要其中一位均匀且独立于其余比特，最终奇偶结果即均匀。

加密 $C=M\oplus K$ 可通过 $M=C\oplus K$ 解密。一次一密依赖均匀随机、独立、保密、与消息等长且不复用的密钥，不能仅凭 XOR 可逆就推断安全。[7]

两个直接的代数后果：

$$
C_1\oplus C_2=M_1\oplus M_2
\quad\text{（同一密钥复用）},
$$

$$
(C\oplus\Delta)\oplus K=M\oplus\Delta.
$$

前者泄露明文关系，但不保证能唯一恢复明文；后者说明密文位翻转造成对应明文位翻转，所以此形式本身不提供完整性保护。

## 14. 算法应用与复杂度

以下为性质的算法推论。复杂度按一个输入能放入机器字计算；$n$ 是输入数量，$w$ 是考虑的位数。

| 问题 | 方法 | 条件与复杂度 |
|---|---|---|
| 唯一出现奇数次的值 | XOR 全部元素 | 必须保证仅一个值出现奇数次；$O(n)$ 时间、$O(1)$ 额外空间 |
| 静态区间 XOR | 前缀 XOR | $O(n)$ 预处理、$O(1)$ 查询、$O(n)$ 空间 |
| 单点修改、区间查询 | 树状数组或线段树 | 更新、查询均为 $O(\log n)$ |
| 目标是否由子集 XOR 得到 | 异或基 | 常规逐位构造 $O(nw)$，检查目标 $O(w)$ |
| 最大子集 XOR | 高位主元异或基 | 基构造后，从高到低贪心查询 $O(w)$ |
| 最大数对 XOR | 二进制 Trie | 典型实现 $O(nw)$ 时间，至多 $O(nw)$ 空间；不同于最大子集问题 |
| 多个 XOR 约束 | GF(2) 高斯消元 | 可判定一致性并求解；成本取决于矩阵规模及位打包方式 |

前缀定义：

$$
P_0=0,\qquad P_{i+1}=P_i\oplus A_i.
$$

半开区间 $[l,r)$ 的结果为：

$$
A_l\oplus\cdots\oplus A_{r-1}=P_r\oplus P_l.
$$

共同前缀出现两次后消去。空区间 $l=r$ 的结果为 0。

Python 任意精度整数不能一概视为单次 $O(1)$ 位运算，长整数需计入位数成本。文档中的异或基、Trie 和方程组属于后续实现方向，不表示已加入代码。

## 验证范围

现有测试覆盖基础恒等式有限枚举、前缀区间与直接计算对照、非法输入、密钥复用的合成数据关系。本文新增的全部理论推论尚未逐项编写测试。有限枚举不能替代一般性证明。本次仅更新文档与 README 入口，不修改算法代码。

## 参考来源

以下为本次讨论使用的资料，检索日期 2026-10-25；网页后续可能更新。本文为中文整理及推导，并非原文翻译或转载。

1. Wikipedia, [Exclusive or](https://en.wikipedia.org/wiki/Exclusive_or) — 定义、逻辑属性与多输入奇偶性。
2. Wikipedia, [Bitwise operation](https://en.wikipedia.org/wiki/Bitwise_operation) — 位运算恒等式、分配律与加法分解。
3. Wikipedia, [Finite field](https://en.wikipedia.org/wiki/Finite_field) — 有限域与特征的背景。
4. Wikipedia, [Boolean ring](https://en.wikipedia.org/wiki/Boolean_ring) — 布尔环结构。
5. Wikipedia, [Algebraic normal form](https://en.wikipedia.org/wiki/Algebraic_normal_form) — 布尔函数的代数表达。
6. Wikipedia, [Hamming distance](https://en.wikipedia.org/wiki/Hamming_distance) — 汉明距离。
7. Wikipedia, [One-time pad](https://en.wikipedia.org/wiki/One-time_pad) — 一次一密的条件与限制。
8. Simon Tatham, [XOR](https://www.chiark.greenend.org.uk/~sgtatham/quasiblog/xor/), 2025-02-14 — 作者对 XOR 的讲解与推导。
9. Princeton COS330, [Lecture 20](https://www.cs.princeton.edu/courses/archive/fall25/cos330/files/lectures/lecture_20.pdf), Fall 2025 — GF(2) 线性代数。本次取得检索摘要，PDF 直连读取返回 403，未逐页核对。

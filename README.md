# XOR Research

研究异或（XOR）的数学性质及其在算法、密码学中的应用。采用“提出问题 → 数学推导 → 代码验证 → 记录边界”的方式推进。代码使用 Python 3.10+，无需第三方依赖。

## 从这里开始

- [基础性质与证明](notes/01-foundations.md)
- [研究路线与实验记录](notes/02-roadmap.md)
- [可运行实验](experiments/xor_lab.py)
- [自动验证](tests/test_xor.py)

在仓库根目录运行：

```bash
python experiments/xor_lab.py
python -m unittest discover -s tests -v
```

Python 中异或写作 `a ^ b`，乘方写作 `a ** b`。本项目的整数实验限定为非负整数；讨论有限位宽时会明确位数。有限枚举用于发现错误和检验实现，不能替代一般性证明。

## 当前范围

已完成基础恒等式的逐位证明、前缀异或区间查询和密钥复用的合成数据演示。后续研究异或基、GF(2) 线性方程组、最大子集异或与概率性质，具体问题见研究路线。所有密码学示例都使用自造数据。

# 研究生：高级理论阅读地图

[← 返回首页](../README.md) · [博士研讨](phd-seminars.md) · [研究实践](research-practice.md)

> 以下均为编辑推荐，不是 Stanford M.S. 指定书目。研究生阶段建议选 **1 个研究主题 + 2 种方法**，不是横扫全部书单。每条线先读主线，再按问题补高级材料。
>
> 标签：**全文**为合法免费可读版本；**书介/检索**通常需借阅或购买；课程不等于教材全文开放。

## 1. 概率、贝叶斯与统计推断

**先修：**多变量微积分、线性代数、本科概率；测度论用于更严格的理论研究，不是所有应用的入场券。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction* (2022) [作者主页/全文](https://probml.github.io/pml-book/book1.html) | 概率建模、统计推断、监督与无监督学习 |
| 进阶 | Murphy, *Probabilistic Machine Learning: Advanced Topics* (2023) [作者主页/全文](https://probml.github.io/pml-book/book2.html) | 图模型、变分推断、采样与深度生成模型 |
| 方法 | Gelman 等, *Bayesian Data Analysis*, 3rd ed. (2013) [作者资源与开放版入口](https://www.stat.columbia.edu/~gelman/book/) | 层级模型、后验预测检验、模型评估；以站内授权说明为准 |
| 理论 | Rick Durrett, *Probability: Theory and Examples*, 5th ed. (2019) [作者资源](https://services.math.duke.edu/~rtd/PTE/pte.html) | 测度概率、条件期望、收敛；按作者页提供版本使用 |

**输出：**实现一个层级贝叶斯模型，报告先验敏感性、收敛诊断、后验预测与可识别性问题。

## 2. 统计学习、优化与泛化

**先修：**线性代数、概率、证明方法；凸优化需微积分与矩阵微分。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Shalev-Shwartz & Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014) [作者资源/全文入口](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/) | PAC、VC 维、泛化界、稳定性 |
| 主线 | Boyd & Vandenberghe, *Convex Optimization* (2004) [全文](https://web.stanford.edu/~boyd/cvxbook/) | 凸性、对偶、最优性条件与数值方法 |
| 进阶 | Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*, 2nd ed. (2009) [全文](https://hastie.su.domains/ElemStatLearn/) | 正则化、模型选择、核方法与集成 |
| 补充 | Goodfellow, Bengio & Courville, *Deep Learning* (2016) [全文](https://www.deeplearningbook.org/) | 深度学习基础；生成模型与架构进展需另补近期论文 |

**输出：**完整证明一个简单假设类的泛化结果，并用实验说明理论假设与实际训练的差距。

## 3. 因果推断与研究设计

**先修：**概率、回归、实验设计；不能把因果图当成自动得出因果结论的工具。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Hernán & Robins, *Causal Inference: What If* (2020) [全文](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) | 反事实、可交换性、选择偏差、时间变化处理 |
| 主线 | Cunningham, *Causal Inference: The Mixtape* (2021) [全文](https://mixtape.scunning.com/) | DAG、工具变量、断点回归、双重差分 |
| 进阶 | Judea Pearl, *Causality*, 2nd ed. (2009) [书目检索](https://search.worldcat.org/search?q=Judea+Pearl+Causality) | 结构因果模型、干预、识别与反事实 |
| 开放进阶 | Peters, Janzing & Schölkopf, *Elements of Causal Inference* (2017) [作者主页/全文](https://www.causality.org/) | 因果发现、独立机制与分布变化 |

**输出：**同一个问题分别用潜在结果与结构因果模型表述，列出识别假设、估计对象与敏感性分析。

## 4. 信息论与表征

**先修：**概率、微积分、线性代数；研究级结果可能需随机过程。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms* (2003) [全文](https://www.inference.org.uk/mackay/itila/) | 信息、编码、推断与学习之间的联系 |
| 进阶 | Cover & Thomas, *Elements of Information Theory*, 2nd ed. (2006) [书目检索](https://search.worldcat.org/search?q=Cover+Thomas+Elements+of+Information+Theory) | 熵、互信息、信道容量、率失真 |
| 研究 | Tishby, Pereira & Bialek (1999), *The Information Bottleneck Method* [预印本](https://arxiv.org/abs/physics/0004057) | 压缩与相关性；注意互信息估计与表征解释的边界 |

**输出：**推导一个率失真或信息瓶颈目标，并解释为什么“压缩得好”不自动等于“有语义理解”。

## 5. 计算认知与理性分析

**先修：**心理学、贝叶斯推断、实验设计、编程。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Farrell & Lewandowsky, *Computational Modeling of Cognition and Behavior* (2018) [书目检索](https://search.worldcat.org/search?q=Farrell+Lewandowsky+Computational+Modeling+of+Cognition+and+Behavior) | 模型拟合、比较、参数恢复与行为解释 |
| 主线 | Goodman & Tenenbaum 等, *Probabilistic Models of Cognition* [在线书](https://probmods.org/) | 概率程序、概念学习、推理与语言 |
| 经典 | David Marr, *Vision* (1982) [书目检索](https://search.worldcat.org/search?q=David+Marr+Vision) | 计算层、算法/表征层与实现层；不是三门独立学科的简单对应 |
| 进阶 | Anderson, *The Adaptive Character of Thought* (1990) [书目检索](https://search.worldcat.org/search?q=Anderson+Adaptive+Character+of+Thought) | 理性分析与适应性解释 |

**输出：**比较规则模型、贝叶斯模型、神经模型对同一任务的预测；使用参数恢复与模型恢复检验可区分性。

## 6. 理论与计算神经科学

**先修：**微分方程、线性代数、概率与神经生物学；不要直接跳进自由能公式。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Gerstner 等, *Neuronal Dynamics* (2014) [全文](https://neuronaldynamics.epfl.ch/) | 神经元模型、脉冲、编码与网络动力学 |
| 主线 | Dayan & Abbott, *Theoretical Neuroscience* (2001) [作者资源](https://www.gatsby.ucl.ac.uk/~dayan/book/) | 神经编码、解码、学习与强化学习；资源页不保证全书开放 |
| 课程 | [Neuromatch Computational Neuroscience](https://compneuro.neuromatch.io/) | 从数据与代码进入计算神经科学 |
| 进阶 | Richard Sutton & Andrew Barto, *Reinforcement Learning: An Introduction*, 2nd ed. (2018) [作者主页/全文](http://incompleteideas.net/book/the-book-2nd.html) | 贝尔曼方程、TD、价值与策略；算法模型不等于生物机制证据 |

**输出：**实现神经元或群体编码模型，评价参数、观测噪声与神经机制解释之间的关系。

## 7. 形式语义、语用与语言计算

**先修：**一阶逻辑、集合与函数、句法与语义入门。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Heim & Kratzer, *Semantics in Generative Grammar* (1998) [书目检索](https://search.worldcat.org/search?q=Heim+Kratzer+Semantics+in+Generative+Grammar) | 类型、组合性、lambda 演算与量化 |
| 主线 | [The Rational Speech Act framework](https://www.problang.org/) [在线教程] | 把语用解释写成概率模型；网站标题与版本以原站为准 |
| 开放补充 | [Language Science Press](https://langsci-press.org/) [开放学术出版] | 按研究问题找语义、语用与语言理论专著，不必整站通读 |
| 进阶 | Jurafsky & Martin, *Speech and Language Processing* [全文草稿](https://web.stanford.edu/~jurafsky/slp3/) | 把形式语言分析与现代语言模型方法对照 |

**输出：**对歧义或语用推断构建组合语义分析与概率模型；明确二者解释目标不同。

## 8. 高级逻辑、类型论与计算基础

**先修：**元逻辑、可计算性、证明经验；类型论还需函数式编程基础。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Boolos, Burgess & Jeffrey, *Computability and Logic*, 5th ed. (2007) [书目检索](https://search.worldcat.org/search?q=Boolos+Burgess+Jeffrey+Computability+and+Logic) | 可计算性、完备性、不完备性 |
| 主线 | *Software Foundations* [全文](https://softwarefoundations.cis.upenn.edu/) | 机器检查证明、程序逻辑；不同卷有不同先修 |
| 进阶 | Robert Harper, *Practical Foundations for Programming Languages*, 2nd ed. (2016) [作者资源](https://www.cs.cmu.edu/~rwh/pfpl/) | 静态与动态语义、类型系统、计算效应 |
| 专题 | *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013) [全文](https://homotopytypetheory.org/book/) | 仅适合有依赖类型与抽象数学准备者；并非所有方向的必读 |

**输出：**形式化一个小语言，证明类型保持或进展；解释定理成立所依赖的语言设计。

## 9. 决策、博弈与社会系统

**先修：**概率、优化、基础经济学；经验决策研究另需实验设计。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | Martin J. Osborne, *An Introduction to Game Theory* (2004) [作者资源](https://www.economics.utoronto.ca/osborne/igt/) | 策略、均衡、动态与信息；资源页不保证整书开放 |
| 主线 | Mykel J. Kochenderfer, Tim A. Wheeler & Kyle H. Wray, *Algorithms for Decision Making* (2022) [全文](https://algorithmsbook.com/) | MDP、POMDP、规划与多智能体 |
| 开放补充 | Shoham & Leyton-Brown, *Multiagent Systems* (2009) [全文](https://www.masfoundations.org/) | 博弈论、机制设计与计算视角 |
| 社会系统 | Matthew J. Salganik, *Bit by Bit: Social Research in the Digital Age* (2018) [全文](https://www.bitbybitbook.com/) | 数字实验、观察数据、合作与研究伦理 |
| 公平与价值 | Barocas, Hardt & Narayanan, *Fairness and Machine Learning* (2023) [全文](https://fairmlbook.org/) | 公平定义、统计限制与社会技术语境 |

**输出：**明确区分规范模型、描述模型和制度设计；展示至少两个指标之间的权衡。

## 10. HCI、具身与社会技术研究

**先修：**心理实验、研究方法、哲学论证；定性方法也需要系统训练。

| 层级 | 文献与访问 | 阅读重点 |
|---|---|---|
| 主线 | [The Encyclopedia of Human-Computer Interaction, 2nd Ed.](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed) [在线章节] | HCI 理论与方法；章节访问条件以原站为准 |
| 经典 | Lucy Suchman, *Human–Machine Reconfigurations* (2007) [书目检索](https://search.worldcat.org/search?q=Suchman+Human+Machine+Reconfigurations) | 情境行动、交互与“智能”的社会条件 |
| 经典 | Edwin Hutchins, *Cognition in the Wild* (1995) [书目检索](https://search.worldcat.org/search?q=Hutchins+Cognition+in+the+Wild) | 分布式认知与真实任务系统 |
| 进阶 | Varela, Thompson & Rosch, *The Embodied Mind* (1991) [书目检索](https://search.worldcat.org/search?q=Varela+Thompson+Rosch+Embodied+Mind) | 具身与生成论；需同时阅读批评与经验研究 |

**输出：**开展一个小型交互研究；在报告中说明任务情境、参与者、研究者位置和结论可迁移范围。

## 进入博士阅读前的最低自检

- [ ] 能独立读懂并复述一个关键证明或模型推导。
- [ ] 能实现至少一个模型并验证参数恢复或数值正确性。
- [ ] 能区分经验结果、理论定理、规范主张和哲学论证。
- [ ] 能对一个研究问题列出两种竞争解释及其判别证据。
- [ ] 能写出 3–5 页研究提案，而不是只罗列想读的书。

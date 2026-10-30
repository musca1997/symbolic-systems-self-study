# 博士阶段：以问题组织文献，而不是以厚度组织书架

[← 首页](../README.md) · [高级理论](graduate-reading.md) · [研究实践](research-practice.md)

> 编辑设计的专题研讨路线，不是 Stanford 官方博士课程。建议每次选一个专题，用 6–8 周完成：概念界定 → 经典争论 → 数学/模型 → 复现或论证 → 研究提案。以下“经典”不表示结论无争议；旧论文也不能替代当前文献检索。
>
> DOI 是稳定定位入口，**不保证开放全文**；标记“预印本/作者稿”的链接需与正式发表版本核对。

## A. 计算、表征与理解：什么才算认知解释？

**先修：**心智哲学、计算理论、认知科学导论。

1. Newell & Simon (1976), *Computer Science as Empirical Inquiry: Symbols and Search*. [DOI](https://doi.org/10.1145/360018.360022)
2. Searle (1980), *Minds, Brains, and Programs*. [DOI](https://doi.org/10.1017/S0140525X00005756)
3. Fodor & Pylyshyn (1988), *Connectionism and Cognitive Architecture: A Critical Analysis*. [DOI](https://doi.org/10.1016/0010-0277%2888%2990031-5)
4. Harnad (1990), *The Symbol Grounding Problem*. [预印本](https://arxiv.org/abs/cs/9906002)
5. Lake, Ullman, Tenenbaum & Gershman (2017), *Building Machines That Learn and Think Like People*. [作者预印本](https://arxiv.org/abs/1604.00289)
6. Bender & Koller (2020), *Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data*. [开放全文](https://aclanthology.org/2020.acl-main.463/)

**争论轴：**系统性是否要求显式符号？行为成功、语义理解与机制解释是不是同一标准？

**研究产物：**给出两个可区分的“理解”定义，设计能让它们产生不同判断的任务；不能只用单一排行榜成绩充当答案。

## B. 贝叶斯认知、资源理性与有限计算

**先修：**贝叶斯推断、决策论、计算认知建模。

1. Griffiths, Chater, Kemp, Perfors & Tenenbaum (2010), *Probabilistic Models of Cognition: Exploring Representations and Inductive Biases*. [DOI](https://doi.org/10.1016/j.tics.2010.05.004)
2. Tenenbaum, Kemp, Griffiths & Goodman (2011), *How to Grow a Mind: Statistics, Structure, and Abstraction*. [DOI](https://doi.org/10.1126/science.1192788)
3. Lieder & Griffiths (2020), *Resource-Rational Analysis: Understanding Human Cognition as the Optimal Use of Limited Computational Resources*. [DOI](https://doi.org/10.1017/S0140525X1900061X)
4. Goodman & Frank (2016), *Pragmatic Language Interpretation as Probabilistic Inference*. [DOI](https://doi.org/10.1016/j.tics.2016.08.005)

**争论轴：**理想观察者模型解释的是任务规范、人的算法，还是研究者选定的目标函数？

**研究产物：**同一数据上比较精确推断、有限采样和启发式；同时评估拟合、复杂度、反应时与跨任务预测。对先验和计算预算做敏感性分析。

## C. 因果、机制与稳健泛化

**先修：**因果图、潜在结果、统计学习理论。

1. Pearl (2009), *Causality*, 2nd ed. [检索](https://search.worldcat.org/search?q=Judea+Pearl+Causality)
2. Peters, Bühlmann & Meinshausen (2016), *Causal Inference by Using Invariant Prediction: Identification and Confidence Intervals*. [预印本](https://arxiv.org/abs/1501.01332)
3. Schölkopf 等 (2021), *Toward Causal Representation Learning*. [预印本](https://arxiv.org/abs/2102.11107)
4. Arjovsky, Bottou, Gulrajani & Lopez-Paz (2019), *Invariant Risk Minimization*. [预印本](https://arxiv.org/abs/1907.02893)

**争论轴：**什么时候环境不变性提供因果信息？表征学习的目标是否可识别？不变性不是充分普适的因果保证。

**研究产物：**建立已知生成机制的模拟环境，改变隐藏混淆、环境多样性与模型设定，报告方法何时失败；补读所选方法的后续反例与修订。

## D. 预测加工、自由能与主动推断

**先修：**概率、变分推断、动力系统、控制与计算神经科学。

1. Rao & Ballard (1999), *Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects*. [DOI](https://doi.org/10.1038/4580)
2. Friston (2010), *The Free-Energy Principle: A Unified Brain Theory?* [DOI](https://doi.org/10.1038/nrn2787)
3. Andy Clark (2013), *Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science*. [DOI](https://doi.org/10.1017/S0140525X12000477)
4. Parr, Pezzulo & Friston (2022), *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. [出版社/开放版本入口](https://mitpress.mit.edu/9780262045353/active-inference/)

**争论轴：**优化目标、过程理论与神经实现证据分别是什么？哪些预测不依赖事后调参？

**研究产物：**从完整假设推导一个最小模型，与控制或强化学习基线比较；明确哪些观察能反驳该模型，不把整个框架当成已被证实的普遍定律。

## E. 语言的组合性、语用与大模型

**先修：**形式语义、语用学、概率模型与神经语言模型。

1. Grice (1975), *Logic and Conversation*. [书目检索](https://search.worldcat.org/search?q=Grice+Logic+and+Conversation)
2. Frank & Goodman (2012), *Predicting Pragmatic Reasoning in Language Games*. [DOI](https://doi.org/10.1126/science.1218633)
3. Linzen, Dupoux & Goldberg (2016), *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies*. [开放全文](https://aclanthology.org/Q16-1037/)
4. Hewitt & Manning (2019), *A Structural Probe for Finding Syntax in Word Representations*. [开放全文](https://aclanthology.org/N19-1419/)
5. Hewitt & Liang (2019), *Designing and Interpreting Probes with Control Tasks*. [开放全文](https://aclanthology.org/D19-1275/)

**争论轴：**可从表征解码的信息是否被模型实际使用？组合泛化与训练数据记忆怎样区分？

**研究产物：**构造受控的句法/语义最小对，并做探针控制、数据泄漏检查与干预；补读近两年的对应任务评测，而不是只使用早期 LSTM 结论评价所有大模型。

## F. 可解释性、表征与神经机制

**先修：**神经网络、统计、神经编码与科学解释。

1. Kriegeskorte, Mur & Bandettini (2008), *Representational Similarity Analysis—Connecting the Branches of Systems Neuroscience*. [开放全文](https://doi.org/10.3389/neuro.06.004.2008)
2. Jain & Wallace (2019), *Attention Is Not Explanation*. [开放全文](https://aclanthology.org/N19-1357/)
3. Wiegreffe & Pinter (2019), *Attention Is Not Not Explanation*. [开放全文](https://aclanthology.org/D19-1002/)
4. Olah 等 (2020), *Zoom In: An Introduction to Circuits*. [开放全文](https://distill.pub/2020/circuits/zoom-in/)

**争论轴：**相似性、可预测性、因果贡献与解释是不同的关系。可视化好看不等于机制已被识别。

**研究产物：**将相关性分析与消融/干预对照；报告分布外稳定性、干预副作用与负结果。机制解释仍需独立验证。

## G. 公平、分布式认知与社会技术系统

**先修：**HCI、统计决策、社会研究方法与研究伦理。

1. Hutchins (1995), *Cognition in the Wild*. [检索](https://search.worldcat.org/search?q=Hutchins+Cognition+in+the+Wild)
2. Suchman (2007), *Human–Machine Reconfigurations*. [检索](https://search.worldcat.org/search?q=Suchman+Human+Machine+Reconfigurations)
3. Selbst, boyd, Friedler, Venkatasubramanian & Vertesi (2019), *Fairness and Abstraction in Sociotechnical Systems*. [DOI](https://doi.org/10.1145/3287560.3287598)
4. Gebru 等 (2021), *Datasheets for Datasets*. [作者预印本](https://arxiv.org/abs/1803.09010)
5. Mitchell 等 (2019), *Model Cards for Model Reporting*. [作者预印本](https://arxiv.org/abs/1810.03993)

**争论轴：**把社会问题写成模型目标时，哪些主体、制度与价值被排除了？

**研究产物：**为一个人机决策系统写技术评价与情境分析，附数据说明、模型卡、利益相关者和部署限制。不要用一个公平指标替代价值判断。

## 每个专题统一交付

- 1 页问题与术语地图：区分规范、计算、算法、实现与制度层次。
- 10–20 篇相关工作矩阵：包含经典、近年进展、批评和负结果；每篇写方法与局限。
- 1 次复现、形式推导或哲学论证重建。
- 1 份 3–5 页提案：研究缺口、竞争假说、识别/证明路径、伦理与失败判据。
- 1 次公开报告；若数据不能公开，提供合成数据与可复现流程。

**更新前沿的方法：**用标题在 ACL Anthology、PMLR/JMLR、期刊官网和 Semantic Scholar 查正式版本，再向前追引文、向后追被引；arXiv 和 OpenReview 用于发现，不将其收录状态当成发表质量的替代证明。

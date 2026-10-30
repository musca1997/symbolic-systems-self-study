# Symbolic Systems 自学指南

### 从心智、语言与计算，到跨学科研究

[![Learning](https://img.shields.io/badge/learning-interdisciplinary-blue)](#培养结构与官方来源)
[![Language](https://img.shields.io/badge/language-中文-red)](#目录)
[![License: CC BY 4.0](https://img.shields.io/badge/content-CC_BY_4.0-lightgrey)](LICENSE)

> 以 **Stanford Symbolic Systems** 的培养结构为参照，整理一条面向自学者的跨学科路线：**本科核心 → 方向深化 → 研究生理论 → 博士研究**。
>
> 独立编写的中文自学指南。培养结构参考 Stanford 官网，书目与阅读路线由编者整理。

## 目录

- [培养结构与官方来源](#培养结构与官方来源)
- [如何使用](#如何使用)
- [先修与学习地图](#先修与学习地图)
- [本科核心书目](#本科核心书目)
- [方向选择](#方向选择)
- [硕博阶段](#硕博阶段)
- [网课与课程组合](#网课与课程组合)
- [自学进度表](#自学进度表)
- [开放资源](#开放资源)
- [贡献与版权](#贡献与版权)

## 培养结构与官方来源

Stanford 的本科培养以**方法训练、领域交叉与研究实践**为主线：

| 官方结构 | 本仓库的自学转译 |
|---|---|
| Preparations：Gateway、微积分与线性代数 | 心智与机器导论；数学准备 |
| Philosophical Analysis | 哲学论证、心智与语言哲学 |
| Formal Methods | 逻辑、可计算性、概率统计 |
| Computational Methods | 编程、算法、计算建模 |
| Empirical Cognitive Science | 心理学、认知科学、语言理论 |
| Cross-Area Requirement | 至少一个把两种方法结合起来的项目 |
| Concentration | 选一个方向系统深化 |
| Advanced Small Seminar、Capstone、Presentation | 读书会、复现、独立研究与公开展示 |

**官方核对来源（查阅日期：2026-10-30）：**

1. [B.S. Program](https://symsys.stanford.edu/undergraduates/bs-program)
2. [Major Policies & Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements)
3. [Core Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements/core-requirements)：页面标注 G4.3，2026-09-01 生效，2026-10-27 更新；明确列出四类方法、跨领域要求、五门课的 Concentration 与实践要求。
4. [Concentrations](https://symsys.stanford.edu/undergraduates/concentrations)
5. [M.S. Program](https://symsys.stanford.edu/graduates/masters-program)：官方定位为研究型硕士，强调语言、信息、人类与机器智能，以及至少两个相关学科的结合。

本科核心课程包括 SYMSYS 1、PHIL 80、CS 103、CS 106A/B、PSYCH 1 等，各模块提供多种选课路径。具体选课规则见官网及相应年份的 Bulletin。

博士阅读部分面向认知科学、计算机科学、语言学、哲学、心理学和神经科学研究，围绕共同问题组织专题。

## 如何使用

- **★ 主线**：每个模块选一本作为主教材。
- **＋ 进阶**：有明确研究需求时再读。
- **[全文]**：作者、出版社、大学或开放出版平台提供的全文。
- **[课程]**：课程讲义、视频、作业等教学材料。
- **[书介]**：出版社或图书主页，通常需购买或通过图书馆借阅。
- **[预印本]**：研究稿件，需确认版本、发表状态和后续修订。

各条目链接至原始资源，并标注访问类型。建议以英文原版为检索基准，配合译本理解术语。

## 先修与学习地图

```text
数学：微积分 → 线性代数 → 概率统计 → 优化 / 测度概率
形式：证明方法 → 一阶逻辑 → 可计算性 → 复杂性 / 类型论
计算：Python → 数据结构与算法 → AI / 统计建模
经验：心理学 → 实验设计 → 认知 / 语言 / 神经数据
哲学：论证写作 → 心智 / 语言 / 科学哲学
                    ↓
         选择一个主方向 + 一个互补方法
                    ↓
           复现 → 研究问题 → 独立论文
```

数学、心理学与哲学可以并行学习；进入理论证明、机器学习和神经建模时，再按模块补齐先修。

## 本科核心书目

### 0. 心智与机器：建立问题地图

| 优先 | 文献 | 为什么读 / 应达到什么 |
|---|---|---|
| ★ | José Luis Bermúdez, *Cognitive Science: An Introduction to the Science of the Mind* [书介](https://www.cambridge.org/highereducation/search?searchTerm=Cognitive%20Science%20Bermudez) | 认识表征、计算、心理实验与神经解释的联系；画出一种认知现象的多层解释图 |
| ★ | Alan Turing (1950), *Computing Machinery and Intelligence* [原文 DOI](https://doi.org/10.1093/mind/LIX.236.433) | 区分“机器能否思考”、操作性检验与智能的本体论问题 |
| ＋ | Andy Clark, *Mindware: An Introduction to the Philosophy of Cognitive Science* [书介](https://global.oup.com/academic/product/mindware-9780199828159) | 比较经典计算、联结主义与具身路线 |

**练习：**用 1,500 字回答“预测人的行为是否等于解释人的心智？”，提出论点、反例、回应与可检验预测。

### 1. 数学与概率准备

| 优先 | 文献 / 开放课程 | 重点 |
|---|---|---|
| ★ | OpenStax, *Calculus* [全文](https://openstax.org/subjects/math) | 单变量、多变量、偏导、积分；按需要选章节 |
| ★ | Hefferon, *Linear Algebra* [全文](https://hefferon.net/linearalgebra/) | 向量空间、线性变换、正交、特征值；兼顾证明与计算 |
| ★ | MIT 18.06 Linear Algebra [课程](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | 矩阵方法、投影、最小二乘、SVD |
| ★ | Hammack, *Book of Proof* [全文](https://www.people.vcu.edu/~rhammack/BookOfProof/) | 集合、函数、归纳、反证、严格写作 |
| ★ | Harvard Stat 110 / Blitzstein & Hwang [课程与作者资源](https://stat110.hsites.harvard.edu/) | 条件概率、随机变量、期望、大数定律、中心极限定理；教材可用版本见站内说明 |
| ＋ | Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* [全文](https://mml-book.github.io/) | 把线代、矩阵微积分与概率接到建模任务 |

**练习：**推导最小二乘；用模拟验证贝叶斯公式和中心极限定理；解释“相关不等于因果”。

### 2. 哲学分析：心智、语言与科学

| 优先 | 文献 | 重点 |
|---|---|---|
| ★ | [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/)（SEP）[全文] | 先读 [Computational Theory of Mind](https://plato.stanford.edu/entries/computational-mind/)、[Functionalism](https://plato.stanford.edu/entries/functionalism/)、[Mental Representation](https://plato.stanford.edu/entries/mental-representation/) |
| ★ | Jaegwon Kim, *Philosophy of Mind* [书目检索](https://search.worldcat.org/search?q=Jaegwon+Kim+Philosophy+of+Mind) | 物理主义、心身因果、功能主义、意识；使用图书馆获取 |
| ★ | [Jim Pryor: Guidelines on Writing a Philosophy Paper](https://www.jimpryor.net/teaching/guidelines/writing.html) [全文] | 论点组织、论证重建与反驳写作 |
| ＋ | [SEP: Scientific Explanation](https://plato.stanford.edu/entries/scientific-explanation/) 与 [Models in Science](https://plato.stanford.edu/entries/models-science/) [全文] | 区分预测、机制、解释与理想化模型 |

**练习：**分别重建功能主义与一种反对意见，明确前提、推理、结论，写成一篇结构完整的短论文。

### 3. 形式方法：逻辑与计算理论

| 优先 | 文献 | 重点 |
|---|---|---|
| ★ | *forall x: Calgary* [全文](https://forallx.openlogicproject.org/) | 命题与一阶逻辑、语义、自然演绎 |
| ★ | *Open Logic Project* [全文](https://openlogicproject.org/) | 逻辑进阶、可计算性与元逻辑；与前一本分工阅读 |
| ★ | Michael Sipser, *Introduction to the Theory of Computation* [书目检索](https://search.worldcat.org/search?q=Sipser+Introduction+to+the+Theory+of+Computation) | 自动机、可判定性、归约、复杂性 |
| ＋ | MIT 18.404J Theory of Computation [课程](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) | 配套讲授与习题 |

**练习：**完成自然演绎证明；证明一个问题不可判定；解释“有效”“可靠”“完备”分别指什么。

### 4. 计算方法：从程序到模型

| 优先 | 文献 / 课程 | 重点 |
|---|---|---|
| ★ | [CS50P](https://cs50.harvard.edu/python/) [课程] | Python、测试、异常、文件处理 |
| ★ | [Stanford CS106B](https://web.stanford.edu/class/cs106b/) [课程] | 递归、抽象数据类型与数据结构；主要使用 C++，需另补语言先修 |
| ★ | Jeff Erickson, *Algorithms* [全文](https://jeffe.cs.illinois.edu/teaching/algorithms/) | 递归、动态规划、贪心、图算法与正确性证明 |
| ★ | Poole & Mackworth, *Artificial Intelligence: Foundations of Computational Agents* [全文](https://artint.info/) | 搜索、约束、知识表示、不确定性与决策 |
| ＋ | [Stanford CS221](https://stanford-cs221.github.io/) [课程] | 把算法与推理、规划、学习连接起来 |

**练习：**实现搜索算法、朴素贝叶斯和一个约束求解器；报告复杂度、基线与失败案例。

### 5. 经验认知科学：心理、实验与神经

| 优先 | 文献 | 重点 |
|---|---|---|
| ★ | OpenStax, *Psychology 2e* [全文](https://openstax.org/details/books/psychology-2e) | 心理学概览、记忆、学习、发展与研究方法 |
| ★ | Navarro, *Learning Statistics with R* [全文](https://learningstatisticswithr.com/) | 从数据分析理解估计、检验与模型；需学习 R |
| ★ | [Research Methods in Psychology](https://opentextbc.ca/researchmethods/) [全文] | 操作化、信效度、实验设计与伦理 |
| ＋ | *Neuroscience Online*, UTHealth [全文](https://nba.uth.tmc.edu/neuroscience/) | 神经基础、感觉运动与高级功能 |
| ＋ | Gazzaniga, Ivry & Mangun, *Cognitive Neuroscience: The Biology of the Mind* [书目检索](https://search.worldcat.org/search?q=Gazzaniga+Ivry+Mangun+Cognitive+Neuroscience) | 从行为和脑损伤、成像证据理解认知功能 |

**练习：**设计一个反应时实验，写出混淆变量、样本量理由、排除标准和分析计划。真人实验准备好知情同意、隐私保护与相应伦理审批。

### 6. 语言理论：从语言结构到计算模型

| 优先 | 文献 | 重点 |
|---|---|---|
| ★ | Anderson 等, *Essentials of Linguistics, 2nd edition* [全文](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/) | 语音、音系、形态、句法与语义；建立自然语言分析基础 |
| ★ | Paul H. Portner, *What Is Meaning? Fundamentals of Formal Semantics* [书目检索](https://search.worldcat.org/search?q=Paul+Portner+What+Is+Meaning) | 指称、真值条件、组合性和量化 |
| ★ | Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft [全文](https://web.stanford.edu/~jurafsky/slp3/) | 从语言现象走向计算模型；草稿持续更新，引用需注明版本日期 |
| ＋ | [Natural Language Toolkit Book](https://www.nltk.org/book/) [全文] | 语料与语言处理入门；部分技术较旧，宜作为练习而非现代模型总览 |

**练习：**给一个量词句写出两种作用域读法；做一次小型语料分析，说明语言学假设与模型误差的关系。

## 方向选择

下列方向名称来自官方 Concentrations 页面，右栏给出相应的自学搭配。建议先选一个主方向。

| 官方方向 | 自学搭配 |
|---|---|
| Applied Logic | 逻辑 + 可计算性 + 形式化验证 |
| Artificial Intelligence | 概率 + 算法 + 机器学习 |
| Biomedical Applications | 生物医学基础 + 统计建模 + 研究伦理 |
| Cognitive Science | 心理实验 + 计算认知 + 哲学解释 |
| Computational Foundations | 算法 + 复杂性 + 编程语言 |
| Computational Social Science | 社会理论 + 因果推断 + 网络数据 |
| Computer Music | 信号处理 + 音乐认知 + 交互系统 |
| Decision Making and Rationality | 决策论 + 博弈论 + 行为实验 |
| Human-Centered Artificial Intelligence | AI + HCI + 价值与社会影响 |
| Human-Computer Interaction | 交互设计 + 实验方法 + 社会技术分析 |
| Learning | 学习科学 + 认知发展 + 统计学习 |
| Mathematical Foundations | 分析 + 概率 + 逻辑 |
| Media and Communication | 传播理论 + 平台研究 + 实证方法 |
| Natural Language | 语言理论 + 语用学 + NLP |
| Neurosciences | 神经基础 + 动力系统 + 统计模型 |
| Philosophical Foundations | 心智与语言哲学 + 逻辑 + 科学哲学 |
| Individually Designed Concentrations | 有明确研究问题后组合；在校生须遵守正式审批规定 |

后续高级书目重点展开逻辑、AI、认知、语言、神经与社会技术方向；生物医学、计算机音乐等方向可在共同基础上继续补充专业课程。

## 硕博阶段

- **[研究生高级理论与文献](docs/graduate-reading.md)**：概率、统计学习、因果、信息论、计算认知、神经、语言语义、逻辑、决策与 HCI。
- **[博士专题与经典论文](docs/phd-seminars.md)**：按研究问题组织经典争论、模型与论文。
- **[研究实践与项目](docs/research-practice.md)**：复现、开放科学、研究计划、博士阶段自检。
- **[来源与链接状态](docs/sources.md)**：培养结构的出处、资源选择原则与链接维护。

## 网课与课程组合

**[完整课程地图 →](docs/courses.md)**：27 组网课与公开课程，逐项列出先修、视频/讲义形式、配套教材、作业建议和自学周数。

| 想学什么 | 推荐起点 |
|---|---|
| 编程与数学 | CS50P / MIT 6.0001、Missing Semester、MIT 18.06、Harvard Stat 110 |
| 哲学与逻辑 | Yale PHIL 181、Stanford Introduction to Logic、MIT 6.042J |
| 心理与语言 | MIT 9.00SC、MIT 24.900 |
| AI 与 NLP | CS221、ISLP/ISLR、MIT 6.S191、CS224N |
| 认知与神经 | Washington Computational Neuroscience、MIT 9.40、Neuromatch、ProbMods |
| 决策与交互 | Game Theory、Model Thinking、CS147 |
| 研究生方法 | EE364A、Brady Neal 因果课、CS228 公开笔记、RSA 教程 |

课程地图还提供四套组合：**零基础 16 周、语言与认知、计算认知与神经、AI 与因果研究准备**，可以按周次直接安排学习。

## 自学进度表

以下按**已有一定基础、每周投入 10–15 小时、约 24 个月**安排，可根据先修和研究兴趣调整。

- [ ] 月 1–3：导论 + Python + 线性代数 + 论证写作
- [ ] 月 4–6：概率 + 一阶逻辑 + 心理学概览
- [ ] 月 7–9：算法 + 可计算性 + 实验设计
- [ ] 月 10–12：语言学 + 心智哲学 + 一个小型交叉项目
- [ ] 月 13–15：选一个方向，读一部高级教材，补数学先修
- [ ] 月 16–18：复现一篇论文；整理结果差异与失败原因
- [ ] 月 19–21：专题读书会；完成相关工作矩阵与研究计划
- [ ] 月 22–24：独立研究原型 + 可运行仓库 + 报告 + 海报

**每周建议：**4 小时教材与习题、3 小时实现或数据分析、2 小时论文、1 小时写作；剩余时间补先修、讨论与复盘。每个阶段用习题、实现或短文检验学习成果。

## 开放资源

| 资源 | 用途 | 使用建议 |
|---|---|---|
| [MIT OpenCourseWare](https://ocw.mit.edu/) / [Stanford Engineering Everywhere](https://see.stanford.edu/) | 数学与计算课程 | 年份较旧的课程需补现代材料 |
| [SEP](https://plato.stanford.edu/) / [Internet Encyclopedia of Philosophy](https://iep.utm.edu/) | 哲学综述与参考文献导航 | 沿条目参考文献继续阅读原始研究 |
| [Open Logic Project](https://openlogicproject.org/) / [OpenStax](https://openstax.org/) | 开放教材 | 分别遵守各资源许可证 |
| [ACL Anthology](https://aclanthology.org/) | NLP 与计算语言学论文 | 会议与年份、论文类型需核对 |
| [arXiv](https://arxiv.org/) / [PhilArchive](https://philarchive.org/) | 预印本与作者存档 | 引用时注明预印本或发表版本 |
| [PMLR](https://proceedings.mlr.press/) / [JMLR](https://www.jmlr.org/) | 机器学习论文 | 阅读主张时同时检查实验设计 |
| [OpenReview](https://openreview.net/) | 论文、评审与讨论 | 可结合评审讨论与录用信息阅读 |
| [OSF](https://osf.io/) | 预注册、数据、材料与复现 | 查看项目授权与数据使用说明 |
| [DANDI](https://dandiarchive.org/) / [OpenNeuro](https://openneuro.org/) | 神经科学开放数据 | 注意数据使用条款及分析规范 |
| [PhilPapers](https://philpapers.org/) / [Semantic Scholar](https://www.semanticscholar.org/) | 文献发现与引文追踪 | 沿索引查找出版社或作者全文 |

## 贡献与版权

欢迎通过 Issue / Pull Request 提交勘误、失效链接、开放版本或有理由的增补。新增资源请附：作者、标题、年份/版次、先修、推荐理由、访问类型及原始来源。优先推荐内容扎实、定位清晰的资源。

本仓库原创文字以 [CC BY 4.0](LICENSE) 授权；外链资源遵循各自的版权与许可。

# 网课与公开课程：从基础到研究专题

[← 首页](../README.md) · [高级书目](graduate-reading.md) · [博士专题](phd-seminars.md)

这份课程地图与书目配合使用：**用讲授建立直觉，用教材补足推导，用作业检验理解。** 每个阶段选一门主课，配一门阅读或实验课，比较容易持续推进。

## 课程怎么选

- **视频课**：有成体系的录播讲授，适合作为自学主线。
- **公开课材料**：提供讲义、阅读清单、作业等，适合按教学日程学习。
- **在线实作**：以代码、交互教材或 notebook 为主，适合边做边学。
- **平台课**：在 Coursera 等平台学习；课程预览、旁听、作业与证书的开放方式可在注册页查看。

下文的周数按每周约 **6–10 小时**估算，是自学安排。课程主页可能滚动到新学期；选定版本后，建议保存 syllabus 和作业清单，保持整轮学习一致。

## 课程总览

| 阶段 | 推荐组合 | 建议产物 |
|---|---|---|
| 基础 | Python + 线性代数 + 概率 + 工具课 | 数据分析小项目 |
| 本科核心 | 哲学 + 逻辑 + 算法 + 心理学 + 语言学 | 论证短文、证明、实验分析 |
| 方向深化 | AI / NLP / 认知 / 神经 / HCI 中选一条 | 课程级项目 |
| 研究生 | 统计学习 + 优化 / 因果 / 图模型 | 推导与论文复现 |
| 研究专题 | 计算认知、语言语用、神经计算等 | 研究提案与独立报告 |

---

## 一、基础工具与数学

### 1. Python：CS50P 或 MIT 6.0001

**入口：**[Harvard CS50P](https://cs50.harvard.edu/python/) · [MIT 6.0001，2016 秋](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)

- **形式：**视频、教学材料与编程练习。
- **先修：**高中数学；适合初学者。
- **怎么选：**CS50P 更聚焦 Python 编程习惯与工具；MIT 6.0001 更强调通过程序分解和求解问题。任选一门主修。
- **重点：**函数、数据结构、递归、调试、测试、复杂度直觉。
- **建议完成：**按顺序做课程习题，再写一个带测试的小型文本分析工具。
- **安排：**8–12 周；每周讲授与编码各占一半左右。

### 2. MIT The Missing Semester

**入口：**[课程主页](https://missing.csail.mit.edu/)

- **形式：**视频、讲义与练习；站内提供不同年份材料。
- **先修：**能写简单程序即可。
- **重点：**命令行、脚本、编辑器、Git、调试与性能分析。
- **建议完成：**为后续课程建立 Git 仓库，整理环境配置与运行命令。
- **安排：**2–4 周，可与 Python 并行。

### 3. MIT 18.06 Linear Algebra

**入口：**[2010 春 OCW](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)

- **形式：**完整录播、作业、考试及部分解答。
- **先修：**代数与基本微积分；同步补向量和矩阵运算。
- **重点：**四个基本子空间、投影、最小二乘、特征值、正定性与 SVD。
- **搭配：**Hefferon *Linear Algebra*，重视定义与证明的部分可从书中补充。
- **建议完成：**至少一半习题；手推最小二乘，再用 NumPy 实现 PCA。
- **安排：**10–14 周。

### 4. 微积分：MIT 18.01SC → 18.02SC

**入口：**[Single Variable Calculus，2010 秋](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) · [Multivariable Calculus，2010 秋](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)

- **形式：**面向自学组织的视频、例题、习题与测验。
- **顺序：**导数与积分 → 多变量函数 → 偏导与梯度 → 多重积分。
- **搭配：**OpenStax *Calculus*。
- **建议完成：**解释梯度方向，手算链式法则，推导简单模型的梯度下降更新。
- **安排：**每门约 10–16 周，已有基础可按章节补修。

### 5. Harvard Stat 110

**入口：**[课程与教材资源](https://stat110.hsites.harvard.edu/)

- **形式：**录播、习题与教材资源。
- **先修：**单变量微积分；多变量基础有助于理解连续分布。
- **重点：**条件概率、随机变量、期望、常用分布、条件期望与极限定理。
- **搭配：**Blitzstein & Hwang, *Introduction to Probability*。
- **建议完成：**条件概率、联合分布和期望部分的习题；用模拟复现三个反直觉概率现象。
- **安排：**12–16 周。

---

## 二、本科共同核心

### 6. 哲学：Yale PHIL 181

**入口：**[Philosophy and the Science of Human Nature](https://oyc.yale.edu/philosophy/phil-181)

- **形式：**Open Yale Courses 录播、文字稿、阅读安排等。
- **先修：**可直接开始，适合练习英文哲学阅读。
- **重点：**将哲学问题与心理学、认知科学研究放在一起讨论，涉及幸福、道德与社会结构。
- **搭配：**首页 SEP 条目与 Jim Pryor 写作指南；心智哲学可继续读 Kim。
- **建议完成：**每两周写一篇 800–1,500 字短文：重建一个论证，提出反对意见，再作回应。
- **安排：**8–12 周。

### 7. 逻辑：Stanford Introduction to Logic

**入口：**[Coursera 课程](https://www.coursera.org/learn/logic-introduction)

- **形式：**平台视频与练习。
- **先修：**基础数学与英文阅读。
- **重点：**形式化表达、逻辑语义与推理。
- **搭配：***forall x: Calgary* 的命题逻辑、一阶逻辑与自然演绎章节。
- **建议完成：**整理语义与证明规则对照表，完成至少 20 个形式化或证明练习。
- **安排：**6–10 周。

### 8. 证明与离散数学：MIT 6.042J

**入口：**[Mathematics for Computer Science，2015 春](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)

- **形式：**视频、开放教材与习题。
- **先修：**高中数学；具备简单编程经验更方便理解应用。
- **重点：**证明、归纳、图、计数、递归与离散概率。
- **搭配：**Hammack *Book of Proof*；证明入门章节可并行阅读。
- **建议完成：**每周提交一份排版清晰的证明作业，保留订正记录。
- **安排：**12–16 周。

### 9. 数据结构与算法：Stanford CS106B → MIT 6.006

**入口：**[CS106B](https://web.stanford.edu/class/cs106b/) · [MIT 6.006，2020 春](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

- **形式：**CS106B 以学期课程材料为入口；MIT 6.006 提供录播、讲义与作业。
- **先修：**编程基础；CS106B 使用 C++，6.006 作业需要 Python 和离散数学基础。
- **重点：**抽象数据类型、递归、图、排序、动态规划、复杂度与正确性。
- **搭配：**Erickson *Algorithms*。
- **建议完成：**实现图搜索和动态规划问题；每个算法附正确性说明与复杂度分析。
- **安排：**CS106B 8–12 周，再用 10–14 周学习算法。

### 10. 可计算性：MIT 18.404J

**入口：**[Theory of Computation，2020 秋](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/)

- **形式：**视频、课程笔记、作业与考试材料。
- **先修：**离散数学、严格证明、基础算法。
- **重点：**自动机、可计算性、可判定性、归约与复杂性。
- **搭配：**Sipser *Introduction to the Theory of Computation*。
- **建议完成：**自动机构造、不可判定性归约及 NP 完全性证明各选一组题。
- **安排：**10–14 周。

### 11. 心理学：MIT 9.00SC

**入口：**[Introduction to Psychology，2011 秋](https://ocw.mit.edu/courses/9-00sc-introduction-to-psychology-fall-2011/)

- **形式：**视频、阅读与自学测验材料。
- **先修：**可直接开始。
- **重点：**认知、学习、记忆、发展、社会心理与研究方法。
- **搭配：**OpenStax *Psychology 2e*，结合较新的综述阅读感兴趣的主题。
- **建议完成：**挑三个实验，分别说明假说、变量、控制条件、结果和替代解释。
- **安排：**8–12 周。

### 12. 语言学：MIT 24.900

**入口：**[Introduction to Linguistics，2012 秋](https://ocw.mit.edu/courses/24-900-introduction-to-linguistics-fall-2012/)

- **形式：**课程讲义、阅读安排与作业材料。
- **先修：**可直接开始；集合与逻辑基础有助于形式分析。
- **重点：**音系、形态、句法、语义与语言的系统结构。
- **搭配：***Essentials of Linguistics, 2nd edition*。
- **建议完成：**音系规则分析、句法树和语义分析各选一组习题。
- **安排：**8–12 周；适合以教材作为主线，课程作业作为检验。

---

## 三、方向深化

### 13. 人工智能：Stanford CS221

**入口：**[Artificial Intelligence: Principles and Techniques](https://stanford-cs221.github.io/)

- **形式：**讲义、作业与历年教学材料，视频入口随学期安排。
- **先修：**数据结构、概率、线性代数与熟练编程。
- **重点：**搜索、约束满足、博弈、MDP、概率推理与学习。
- **搭配：**Poole & Mackworth *Artificial Intelligence*。
- **建议完成：**搜索、MDP、概率模型各完成一个编程任务，再选一个综合项目。
- **安排：**10–14 周。

### 14. 统计学习：ISLP / ISLR

**入口：**[An Introduction to Statistical Learning](https://www.statlearning.com/)

- **形式：**教材全文、配套课程与实验代码；可选 Python 或 R 路线。
- **先修：**概率统计、线性代数、Python 或 R。
- **重点：**回归、分类、重采样、正则化、树模型与无监督学习。
- **搭配：**先以 ISLP/ISLR 为主教材，之后选读 *The Elements of Statistical Learning*。
- **建议完成：**每章一个 lab；期末做包含数据划分、交叉验证与误差分析的预测项目。
- **安排：**10–14 周。

### 15. 深度学习入门：MIT 6.S191

**入口：**[Introduction to Deep Learning](https://introtodeeplearning.com/)

- **形式：**短期课程视频、讲义与实作 lab，按年份发布。
- **先修：**Python、线性代数、微积分与基础机器学习。
- **重点：**神经网络、序列建模、生成模型及前沿应用；内容随年份更新。
- **搭配：***Deep Learning* 的优化与基本架构章节。
- **建议完成：**选定一年的 lab，解释损失函数、数据流程与训练结果。
- **安排：**3–5 周，适合作为方向探索。

### 16. 自然语言处理：Stanford CS224N

**入口：**[Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/)

- **形式：**课程日程、讲义、视频入口与编程作业；选定一个公开材料齐全的学期。
- **先修：**Python、线性代数、概率、微积分、机器学习和神经网络基础。
- **重点：**词表示、序列模型、注意力、Transformer、语言模型与评估。
- **搭配：**Jurafsky & Martin *Speech and Language Processing* 对应章节。
- **建议完成：**至少三个编程作业和一个小型 NLP 项目；加入语言现象分析与误差分类。
- **安排：**10–14 周；预留训练与调试时间。

### 17. 计算神经科学：Washington Coursera 课程

**入口：**[Computational Neuroscience](https://www.coursera.org/learn/computational-neuroscience)

- **形式：**平台视频与练习；教师 Rajesh P. N. Rao、Adrienne Fairhall。
- **先修：**微积分、线性代数、概率与基础编程；同步补神经生物学。
- **重点：**神经编码、解码、信息、神经元模型与学习。
- **搭配：**Dayan & Abbott，或 *Neuronal Dynamics* 的相关章节。
- **建议完成：**复现一个编码/解码示例，改变噪声水平并分析性能。
- **安排：**8–12 周。

### 18. 神经计算：MIT 9.40 与 Neuromatch

**入口：**[MIT Introduction to Neural Computation，2018 春](https://ocw.mit.edu/courses/9-40-introduction-to-neural-computation-spring-2018/) · [Neuromatch Computational Neuroscience](https://compneuro.neuromatch.io/)

- **形式：**MIT 提供课程笔记、阅读与作业；Neuromatch 提供视频、教程和 notebook。
- **先修：**概率、线性代数、微分方程、Python 与神经科学基础。
- **怎么选：**MIT 适合顺序学习理论；Neuromatch 适合按主题动手实践。
- **重点：**神经编码、动力系统、统计建模与认知计算。
- **建议完成：**挑一个神经数据教程，增加模型对照与交叉验证，整理成报告。
- **安排：**10–14 周；也可先用 3–4 周做 Neuromatch 专题试学。

### 19. 博弈与决策：Stanford / UBC Game Theory

**入口：**[Game Theory](https://www.coursera.org/learn/game-theory-1)

- **形式：**平台视频与练习。
- **先修：**基础概率与数学推理。
- **重点：**策略、纳什均衡、混合策略、动态与不完全信息博弈。
- **搭配：**Osborne *An Introduction to Game Theory*。
- **建议完成：**分析三类小型博弈，比较均衡预测与可能的实际行为。
- **安排：**6–10 周。

### 20. 多模型思维：Michigan Model Thinking

**入口：**[Model Thinking](https://www.coursera.org/learn/model-thinking)

- **形式：**平台视频与测验，教师 Scott E. Page。
- **先修：**基础数学；有概率与编程经验可深入模拟。
- **重点：**多种数学与社会科学模型，以及它们适合解释的问题。
- **搭配：**Salganik *Bit by Bit*，用于转向数字社会研究实践。
- **建议完成：**选择一个社会现象，用两个模型分别分析，并比较假设和解释力。
- **安排：**8–12 周。

### 21. HCI：Stanford CS147

**入口：**[CS147 课程目录](https://web.stanford.edu/class/cs147/)

- **形式：**按学期归档的项目、讲义与课程安排；进入具体学期页面学习。
- **先修：**基础设计表达与研究方法；可按项目需要学习原型工具。
- **重点：**需求探索、交互设计、原型、用户评价与迭代。
- **搭配：***The Encyclopedia of Human-Computer Interaction* 对应章节。
- **建议完成：**需求分析 → 两轮原型 → 评价计划 → 迭代报告；读团队项目展示学习如何呈现过程。
- **安排：**8–12 周，适合 2–3 人小组。

---

## 四、研究生理论与专题材料

### 22. 凸优化：Stanford EE364A

**入口：**[Convex Optimization I](https://web.stanford.edu/class/ee364a/) · [教材与补充资源](https://web.stanford.edu/~boyd/cvxbook/)

- **形式：**课程讲义、作业及配套资源；录播可从课程相关入口寻找。
- **先修：**线性代数、多变量微积分、基础概率与证明能力。
- **重点：**凸集、凸函数、对偶、KKT 条件、优化建模与数值求解。
- **建议完成：**手推一个对偶问题，再用 CVXPY 实现回归或资源分配模型。
- **安排：**10–14 周。

### 23. 因果推断：Brady Neal

**入口：**[Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course)

- **形式：**视频、讲义与参考资料。
- **先修：**概率、回归、基础统计。
- **重点：**潜在结果、结构因果模型、混淆、识别与估计。
- **搭配：***Causal Inference: What If* 或 *The Mixtape*。
- **建议完成：**用同一研究问题画 DAG、定义估计对象，完成一个合成数据实验。
- **安排：**8–12 周。

### 24. 概率图模型：Stanford CS228 公开笔记

**入口：**[CS228 Notes](https://ermongroup.github.io/cs228-notes/)

- **形式：**结构化公开笔记，适合以阅读和推导为主学习。
- **先修：**概率、线性代数、算法、基础机器学习。
- **重点：**图表示、条件独立、精确推断、近似推断、参数与结构学习。
- **搭配：**Murphy *Probabilistic Machine Learning: Advanced Topics*。
- **建议完成：**实现一个小图模型的变量消元，再与采样估计对照。
- **安排：**8–12 周。

### 25. 计算认知：Probabilistic Models of Cognition

**入口：**[ProbMods](https://probmods.org/)

- **形式：**带代码示例与练习的在线教材，适合作为实作课程。
- **先修：**概率、基础编程、认知科学导论。
- **重点：**概率程序、推断、概念、归纳学习与语言理解。
- **搭配：**研究生书目中的计算认知模块。
- **建议完成：**选一个概念学习或推理模型，改变先验并分析行为预测。
- **安排：**8–10 周。

### 26. 神经网络与认知：Stanford PSYCH 209 历史材料

**入口：**[Neural Network Models of Cognition](https://web.stanford.edu/class/psych209/)

- **形式：**历史学期的阅读、计算作业与期末项目安排；适合作为专题阅读路线。
- **先修：**神经网络、心理学、概率与编程。
- **重点：**联结主义、分布式表征、学习、感知与认知建模。
- **搭配：**Marr *Vision* 与计算认知模块的竞争模型阅读。
- **建议完成：**选择一个历史作业，用现代工具重新实现；写一份 4–6 页的模型分析。
- **安排：**8–12 周。

### 27. 概率语用：ProbLang / RSA

**入口：**[Probabilistic Language Understanding](https://www.problang.org/)

- **形式：**在线章节、概率模型与示例代码。
- **先修：**贝叶斯推断、语言语义与语用学基础。
- **重点：**说话者与听话者递归推断、指称、信息量与语用推理。
- **搭配：**Grice、Frank & Goodman，以及博士语言专题。
- **建议完成：**实现一个最小 RSA 模型，比较字面听话者与语用听话者的预测。
- **安排：**4–8 周，适合专题读书会。

---

## 五、四套可以直接开学的组合

### A. 零基础起步：16 周

**每周 8–12 小时，以 Python 为主线，心理学建立跨学科兴趣。**

| 周次 | 主课 | 并行内容 | 当期产物 |
|---|---|---|---|
| 1–4 | CS50P 基础 | Missing Semester：命令行与 Git | 带 README 的小程序仓库 |
| 5–8 | CS50P 数据处理与测试 | MIT 9.00SC：研究方法、学习与记忆 | 一篇实验分析卡片 |
| 9–12 | Python 综合练习 | 18.06：矩阵、子空间与投影 | 用代码演示投影与最小二乘 |
| 13–16 | 文本或行为数据小项目 | 继续线代；写一篇哲学论证短文 | 代码、图表与 2–3 页报告 |

线代和心理学在这 16 周先完成核心模块，之后可以继续学完整门课。

### B. 自然语言与认知：两个学期

**先修：**编程、概率与线代。

- **第一学期，12–16 周：**MIT 24.900 为主，配合形式语义入门与逻辑练习。
- **第二学期，12–16 周：**CS224N 为主，选读 RSA 教程；深度学习经验较少时先做 6.S191。
- **最终项目：**选择一个歧义、量词或语用现象，比较语言学分析、概率模型与神经模型。

### C. 计算认知与神经：两个学期

**先修：**概率、Python、线代与心理学基础。

- **第一学期，12–16 周：**Washington Computational Neuroscience 或 MIT 9.40 选一门，配合 Neuromatch 练习。
- **第二学期，12–16 周：**ProbMods 或 PSYCH 209 材料选一条主线，完成模型比较。
- **最终项目：**围绕学习、分类或决策任务，比较两个模型的拟合、恢复与留出预测。

### D. AI 与因果研究准备：两个学期

**先修：**算法、概率、线代、微积分与机器学习基础。

- **第一学期，12–16 周：**EE364A 为主，配合 CS228 的表示与推断章节。
- **第二学期，12–16 周：**Brady Neal 因果课为主，选读统计学习理论并复现一篇因果泛化论文。
- **最终项目：**在已知生成机制的环境中，分析优化目标、识别假设与分布外表现。

## 六、每周执行模板

```text
第 1 次：看讲授，记录 3 个关键概念与 1 个问题。
第 2 次：读配套教材，补齐定义和推导。
第 3 次：独立做习题或编程作业。
第 4 次：订正、测试、写学习日志，并提交到 Git。
每 4 周：用一次小项目或短报告整合所学。
```

**选课顺序建议：**先从当前能做作业的课开始。主课每轮选一门，阅读课或工具课选一门；完成一轮后，再根据项目需要进入下一层。

## 访问与版本记录

本页整理于 **2026-10-30**。整理时读取了 MIT 6.0001、6.042J、9.00SC、24.900、9.40，Yale PHIL 181，CS224N，PSYCH 209，Brady Neal，6.S191，ISLP，Missing Semester 及部分 Coursera 页面。其余入口来自官方课程主页或已有书目资源。

建议在自己的学习记录中保存：课程名称、学校/教师、学期、主页、作业列表与开始日期。Coursera 的具体访问方式见注册页；学期课程中的提交系统与自动评分以当期安排为准。

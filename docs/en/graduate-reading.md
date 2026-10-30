# Graduate Study: An Advanced Theory Reading Map

[← Home](../../README.en.md) · [PhD seminars](phd-seminars.md) · [Research practice](research-practice.md) · [Chinese version](../graduate-reading.md)

> Organize graduate study around **one research theme and two methods**. Start with each module's core readings, then choose advanced material to suit your questions.
>
> Access labels: **Full text** means free to read; **Book information/catalog** helps with purchases or library borrowing; **Course** provides lectures, videos, and exercises.

## 1. Probability, Bayesian Methods, and Statistical Inference

**Prerequisites:** Multivariable calculus, linear algebra, and undergraduate probability. Add measure theory for theoretical research.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Kevin P. Murphy, *Probabilistic Machine Learning: An Introduction* (2022) [Author's site/full text](https://probml.github.io/pml-book/book1.html) | Probabilistic modeling, statistical inference, supervised and unsupervised learning |
| Advanced | Murphy, *Probabilistic Machine Learning: Advanced Topics* (2023) [Author's site/full text](https://probml.github.io/pml-book/book2.html) | Graphical models, variational inference, sampling, and deep generative models |
| Methods | Gelman et al., *Bayesian Data Analysis*, 3rd ed. (2013) [Author resources and open edition](https://www.stat.columbia.edu/~gelman/book/) | Hierarchical models, posterior predictive checks, and model assessment; access terms are listed on the site |
| Theory | Rick Durrett, *Probability: Theory and Examples*, 5th ed. (2019) [Author resources](https://services.math.duke.edu/~rtd/PTE/pte.html) | Measure-theoretic probability, conditional expectation, and convergence; use the editions provided by the author |

**Deliverable:** Implement a hierarchical Bayesian model and report prior sensitivity, convergence diagnostics, posterior predictions, and identifiability issues.

## 2. Statistical Learning, Optimization, and Generalization

**Prerequisites:** Linear algebra, probability, and proof techniques. Convex optimization also requires calculus and matrix differentiation.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Shalev-Shwartz & Ben-David, *Understanding Machine Learning: From Theory to Algorithms* (2014) [Author resources/full text](https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/) | PAC learning, VC dimension, generalization bounds, and stability |
| Core | Boyd & Vandenberghe, *Convex Optimization* (2004) [Full text](https://web.stanford.edu/~boyd/cvxbook/) | Convexity, duality, optimality conditions, and numerical methods |
| Advanced | Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*, 2nd ed. (2009) [Full text](https://hastie.su.domains/ElemStatLearn/) | Regularization, model selection, kernel methods, and ensembles |
| Supplement | Goodfellow, Bengio & Courville, *Deep Learning* (2016) [Full text](https://www.deeplearningbook.org/) | Deep learning foundations; pair with recent papers on generative models and architectures |

**Deliverable:** Give a complete proof of a generalization result for a simple hypothesis class, and use experiments to examine the gap between theoretical assumptions and practical training.

## 3. Causal Inference and Research Design

**Prerequisites:** Probability, regression, and experimental design. Focus on the identification assumptions behind causal graphs.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Hernán & Robins, *Causal Inference: What If* (2020) [Full text](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) | Counterfactuals, exchangeability, selection bias, and time-varying treatments |
| Core | Cunningham, *Causal Inference: The Mixtape* (2021) [Full text](https://mixtape.scunning.com/) | DAGs, instrumental variables, regression discontinuity, and difference-in-differences |
| Advanced | Judea Pearl, *Causality*, 2nd ed. (2009) [Catalog search](https://search.worldcat.org/search?q=Judea+Pearl+Causality) | Structural causal models, interventions, identification, and counterfactuals |
| Open advanced reading | Peters, Janzing & Schölkopf, *Elements of Causal Inference* (2017) [Author's site/full text](https://www.causality.org/) | Causal discovery, independent mechanisms, and distribution shifts |

**Deliverable:** Formulate the same question using potential outcomes and structural causal models. Specify identification assumptions, estimands, and sensitivity analyses.

## 4. Information Theory and Representation

**Prerequisites:** Probability, calculus, and linear algebra. Research-level results may require stochastic processes.

| Level | Reading and access | Focus |
|---|---|---|
| Core | David J. C. MacKay, *Information Theory, Inference, and Learning Algorithms* (2003) [Full text](https://www.inference.org.uk/mackay/itila/) | Connections among information, coding, inference, and learning |
| Advanced | Cover & Thomas, *Elements of Information Theory*, 2nd ed. (2006) [Catalog search](https://search.worldcat.org/search?q=Cover+Thomas+Elements+of+Information+Theory) | Entropy, mutual information, channel capacity, and rate–distortion theory |
| Research | Tishby, Pereira & Bialek (1999), *The Information Bottleneck Method* [Preprint](https://arxiv.org/abs/physics/0004057) | Compression, relevance, mutual information estimation, and representation analysis |

**Deliverable:** Derive a rate–distortion or information bottleneck objective and discuss the relationship between compression objectives and semantic representations.

## 5. Computational Cognition and Rational Analysis

**Prerequisites:** Psychology, Bayesian inference, experimental design, and programming.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Farrell & Lewandowsky, *Computational Modeling of Cognition and Behavior* (2018) [Catalog search](https://search.worldcat.org/search?q=Farrell+Lewandowsky+Computational+Modeling+of+Cognition+and+Behavior) | Model fitting, comparison, parameter recovery, and behavioral explanation |
| Core | Goodman, Tenenbaum et al., *Probabilistic Models of Cognition* [Online book](https://probmods.org/) | Probabilistic programs, concept learning, reasoning, and language |
| Classic | David Marr, *Vision* (1982) [Catalog search](https://search.worldcat.org/search?q=David+Marr+Vision) | Computational, algorithmic/representational, and implementational levels, and their connections |
| Advanced | Anderson, *The Adaptive Character of Thought* (1990) [Catalog search](https://search.worldcat.org/search?q=Anderson+Adaptive+Character+of+Thought) | Rational analysis and adaptive explanations |

**Deliverable:** Compare the predictions of rule-based, Bayesian, and neural models on the same task. Use parameter and model recovery to test whether the models can be distinguished.

## 6. Theoretical and Computational Neuroscience

**Prerequisites:** Differential equations, linear algebra, probability, and neurobiology. These foundations prepare you for predictive processing and active inference.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Gerstner et al., *Neuronal Dynamics* (2014) [Full text](https://neuronaldynamics.epfl.ch/) | Neuron models, spikes, coding, and network dynamics |
| Core | Dayan & Abbott, *Theoretical Neuroscience* (2001) [Author resources](https://www.gatsby.ucl.ac.uk/~dayan/book/) | Neural encoding, decoding, learning, and reinforcement learning; companion materials are on the author's resource page |
| Course | [Neuromatch Computational Neuroscience](https://compneuro.neuromatch.io/) | A data- and code-based introduction to computational neuroscience |
| Advanced | Richard Sutton & Andrew Barto, *Reinforcement Learning: An Introduction*, 2nd ed. (2018) [Author's site/full text](http://incompleteideas.net/book/the-book-2nd.html) | Bellman equations, temporal-difference learning, values, policies, and applications in neuroscience |

**Deliverable:** Implement a neuron or population coding model. Assess the relationship among parameters, observation noise, and explanations of neural mechanisms.

## 7. Formal Semantics, Pragmatics, and Language Computation

**Prerequisites:** First-order logic, sets and functions, and introductory syntax and semantics.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Heim & Kratzer, *Semantics in Generative Grammar* (1998) [Catalog search](https://search.worldcat.org/search?q=Heim+Kratzer+Semantics+in+Generative+Grammar) | Types, compositionality, lambda calculus, and quantification |
| Core | [The Rational Speech Act framework](https://www.problang.org/) [Online tutorial] | Formulating pragmatic interpretation as a probabilistic model; use the title and version listed on the site |
| Open supplement | [Language Science Press](https://langsci-press.org/) [Open scholarly publishing] | Choose monographs on semantics, pragmatics, and linguistic theory to match your research question |
| Advanced | Jurafsky & Martin, *Speech and Language Processing* [Full-text draft](https://web.stanford.edu/~jurafsky/slp3/) | Compare formal linguistic analysis with modern language modeling methods |

**Deliverable:** Develop a compositional semantic analysis and a probabilistic model of ambiguity or pragmatic inference, making their distinct explanatory goals explicit.

## 8. Advanced Logic, Type Theory, and Foundations of Computation

**Prerequisites:** Metalogic, computability, and experience with proofs; type theory also requires functional programming foundations.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Boolos, Burgess & Jeffrey, *Computability and Logic*, 5th ed. (2007) [Catalog search](https://search.worldcat.org/search?q=Boolos+Burgess+Jeffrey+Computability+and+Logic) | Computability, completeness, and incompleteness |
| Core | *Software Foundations* [Full text](https://softwarefoundations.cis.upenn.edu/) | Machine-checked proofs and program logic; prerequisites vary by volume |
| Advanced | Robert Harper, *Practical Foundations for Programming Languages*, 2nd ed. (2016) [Author resources](https://www.cs.cmu.edu/~rwh/pfpl/) | Static and dynamic semantics, type systems, and computational effects |
| Specialized | *Homotopy Type Theory: Univalent Foundations of Mathematics* (2013) [Full text](https://homotopytypetheory.org/book/) | An elective for readers prepared in dependent types and abstract mathematics |

**Deliverable:** Formalize a small language and prove preservation or progress. Explain the language design choices on which the theorem depends.

## 9. Decision Making, Games, and Social Systems

**Prerequisites:** Probability, optimization, and basic economics. Empirical decision research also requires experimental design.

| Level | Reading and access | Focus |
|---|---|---|
| Core | Martin J. Osborne, *An Introduction to Game Theory* (2004) [Author resources](https://www.economics.utoronto.ca/osborne/igt/) | Strategies, equilibria, dynamics, and information; companion materials are on the author's resource page |
| Core | Mykel J. Kochenderfer, Tim A. Wheeler & Kyle H. Wray, *Algorithms for Decision Making* (2022) [Full text](https://algorithmsbook.com/) | MDPs, POMDPs, planning, and multiagent decision making |
| Open supplement | Shoham & Leyton-Brown, *Multiagent Systems* (2009) [Full text](https://www.masfoundations.org/) | Game theory, mechanism design, and computational perspectives |
| Social systems | Matthew J. Salganik, *Bit by Bit: Social Research in the Digital Age* (2018) [Full text](https://www.bitbybitbook.com/) | Digital experiments, observational data, collaboration, and research ethics |
| Fairness and values | Barocas, Hardt & Narayanan, *Fairness and Machine Learning* (2023) [Full text](https://fairmlbook.org/) | Definitions of fairness, statistical limitations, and sociotechnical contexts |

**Deliverable:** Clearly distinguish normative models, descriptive models, and institutional design. Demonstrate a trade-off between at least two metrics.

## 10. HCI, Embodiment, and Sociotechnical Research

**Prerequisites:** Psychological experiments, research methods, and philosophical argumentation. Qualitative methods also call for systematic training.

| Level | Reading and access | Focus |
|---|---|---|
| Core | [The Encyclopedia of Human-Computer Interaction, 2nd Ed.](https://www.interaction-design.org/literature/book/the-encyclopedia-of-human-computer-interaction-2nd-ed) [Online chapters] | HCI theories and methods; chapter access terms are listed on the site |
| Classic | Lucy Suchman, *Human–Machine Reconfigurations* (2007) [Catalog search](https://search.worldcat.org/search?q=Suchman+Human+Machine+Reconfigurations) | Situated action, interaction, and the social conditions of “intelligence” |
| Classic | Edwin Hutchins, *Cognition in the Wild* (1995) [Catalog search](https://search.worldcat.org/search?q=Hutchins+Cognition+in+the+Wild) | Distributed cognition and real-world task systems |
| Advanced | Varela, Thompson & Rosch, *The Embodied Mind* (1991) [Catalog search](https://search.worldcat.org/search?q=Varela+Thompson+Rosch+Embodied+Mind) | Embodiment and enactivism; read alongside critiques and empirical research |

**Deliverable:** Conduct a small interaction study. Describe the task context, participants, researcher positionality, and the scope of transferability of your conclusions.

## Readiness Checklist for PhD-Level Reading

- [ ] Independently understand and reconstruct a key proof or model derivation.
- [ ] Implement at least one model and verify parameter recovery or numerical correctness.
- [ ] Distinguish empirical findings, theoretical theorems, normative claims, and philosophical arguments.
- [ ] Identify two competing explanations for a research question and the evidence that would distinguish them.
- [ ] Write a 3–5-page research proposal covering the question, related work, and methods.

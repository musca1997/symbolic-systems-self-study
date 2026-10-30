# PhD Study: Thematic Seminars and Research Questions

[← Home](../../README.en.md) · [Advanced theory](graduate-reading.md) · [Research practice](research-practice.md) · [Chinese version](../phd-seminars.md)

> Choose one topic at a time and work through it over 6–8 weeks: define concepts → examine classic debates → study the mathematics/models → reproduce results or reconstruct arguments → develop a research proposal. Use classic literature to establish the context, then follow citations into recent research.
>
> Reading links prioritize DOIs, open full texts, and author preprints. Record the version you use when citing a work.

## A. Computation, Representation, and Understanding: What Counts as a Cognitive Explanation?

**Prerequisites:** Philosophy of mind, theory of computation, and introductory cognitive science.

1. Newell & Simon (1976), *Computer Science as Empirical Inquiry: Symbols and Search*. [DOI](https://doi.org/10.1145/360018.360022)
2. Searle (1980), *Minds, Brains, and Programs*. [DOI](https://doi.org/10.1017/S0140525X00005756)
3. Fodor & Pylyshyn (1988), *Connectionism and Cognitive Architecture: A Critical Analysis*. [DOI](https://doi.org/10.1016/0010-0277%2888%2990031-5)
4. Harnad (1990), *The Symbol Grounding Problem*. [Preprint](https://arxiv.org/abs/cs/9906002)
5. Lake, Ullman, Tenenbaum & Gershman (2017), *Building Machines That Learn and Think Like People*. [Author preprint](https://arxiv.org/abs/1604.00289)
6. Bender & Koller (2020), *Climbing towards NLU: On Meaning, Form, and Understanding in the Age of Data*. [Open full text](https://aclanthology.org/2020.acl-main.463/)

**Central debate:** Does systematicity require explicit symbols? How do behavioral success, semantic understanding, and mechanistic explanation relate as standards of evaluation?

**Research output:** Formulate two distinguishable definitions of “understanding” and design tasks on which they yield different judgments. Evaluate results through task performance, generalization, and mechanistic analysis.

## B. Bayesian Cognition, Resource Rationality, and Bounded Computation

**Prerequisites:** Bayesian inference, decision theory, and computational cognitive modeling.

1. Griffiths, Chater, Kemp, Perfors & Tenenbaum (2010), *Probabilistic Models of Cognition: Exploring Representations and Inductive Biases*. [DOI](https://doi.org/10.1016/j.tics.2010.05.004)
2. Tenenbaum, Kemp, Griffiths & Goodman (2011), *How to Grow a Mind: Statistics, Structure, and Abstraction*. [DOI](https://doi.org/10.1126/science.1192788)
3. Lieder & Griffiths (2020), *Resource-Rational Analysis: Understanding Human Cognition as the Optimal Use of Limited Computational Resources*. [DOI](https://doi.org/10.1017/S0140525X1900061X)
4. Goodman & Frank (2016), *Pragmatic Language Interpretation as Probabilistic Inference*. [DOI](https://doi.org/10.1016/j.tics.2016.08.005)

**Central debate:** Does an ideal-observer model explain the task's normative structure, people's algorithms, or the objective function chosen by the researcher?

**Research output:** Compare exact inference, limited sampling, and heuristics on the same data. Assess fit, complexity, response times, and cross-task predictions, and conduct sensitivity analyses of priors and computational budgets.

## C. Causality, Mechanisms, and Robust Generalization

**Prerequisites:** Causal graphs, potential outcomes, and statistical learning theory.

1. Pearl (2009), *Causality*, 2nd ed. [Catalog search](https://search.worldcat.org/search?q=Judea+Pearl+Causality)
2. Peters, Bühlmann & Meinshausen (2016), *Causal Inference by Using Invariant Prediction: Identification and Confidence Intervals*. [Preprint](https://arxiv.org/abs/1501.01332)
3. Schölkopf et al. (2021), *Toward Causal Representation Learning*. [Preprint](https://arxiv.org/abs/2102.11107)
4. Arjovsky, Bottou, Gulrajani & Lopez-Paz (2019), *Invariant Risk Minimization*. [Preprint](https://arxiv.org/abs/1907.02893)

**Central debate:** When does invariance across environments provide causal information? Are the targets of representation learning identifiable? Which assumptions connect environmental invariance to causal identification?

**Research output:** Build simulated environments with known generative mechanisms. Vary hidden confounding, environmental diversity, and model specification, and report the conditions under which methods fail. Read subsequent counterexamples and revisions to your chosen method.

## D. Predictive Processing, Free Energy, and Active Inference

**Prerequisites:** Probability, variational inference, dynamical systems, control, and computational neuroscience.

1. Rao & Ballard (1999), *Predictive Coding in the Visual Cortex: A Functional Interpretation of Some Extra-Classical Receptive-Field Effects*. [DOI](https://doi.org/10.1038/4580)
2. Friston (2010), *The Free-Energy Principle: A Unified Brain Theory?* [DOI](https://doi.org/10.1038/nrn2787)
3. Andy Clark (2013), *Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science*. [DOI](https://doi.org/10.1017/S0140525X12000477)
4. Parr, Pezzulo & Friston (2022), *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. [Publisher/open edition](https://mitpress.mit.edu/9780262045353/active-inference/)

**Central debate:** What are the optimization objective, the process theory, and the evidence for neural implementation? Which predictions hold independently of post hoc parameter tuning?

**Research output:** Derive a minimal model from a complete set of assumptions, compare it with control or reinforcement learning baselines, and propose testable predictions with corresponding falsification conditions.

## E. Linguistic Compositionality, Pragmatics, and Large Language Models

**Prerequisites:** Formal semantics, pragmatics, probabilistic models, and neural language models.

1. Grice (1975), *Logic and Conversation*. [Catalog search](https://search.worldcat.org/search?q=Grice+Logic+and+Conversation)
2. Frank & Goodman (2012), *Predicting Pragmatic Reasoning in Language Games*. [DOI](https://doi.org/10.1126/science.1218633)
3. Linzen, Dupoux & Goldberg (2016), *Assessing the Ability of LSTMs to Learn Syntax-Sensitive Dependencies*. [Open full text](https://aclanthology.org/Q16-1037/)
4. Hewitt & Manning (2019), *A Structural Probe for Finding Syntax in Word Representations*. [Open full text](https://aclanthology.org/N19-1419/)
5. Hewitt & Liang (2019), *Designing and Interpreting Probes with Control Tasks*. [Open full text](https://aclanthology.org/D19-1275/)

**Central debate:** Does a model actually use information that can be decoded from its representations? How can compositional generalization be distinguished from memorization of training data?

**Research output:** Construct controlled syntactic/semantic minimal pairs, with probe controls, data leakage checks, and interventions. Read early LSTM studies alongside language model evaluations from the past two years.

## F. Interpretability, Representation, and Neural Mechanisms

**Prerequisites:** Neural networks, statistics, neural coding, and scientific explanation.

1. Kriegeskorte, Mur & Bandettini (2008), *Representational Similarity Analysis—Connecting the Branches of Systems Neuroscience*. [Open full text](https://doi.org/10.3389/neuro.06.004.2008)
2. Jain & Wallace (2019), *Attention Is Not Explanation*. [Open full text](https://aclanthology.org/N19-1357/)
3. Wiegreffe & Pinter (2019), *Attention Is Not Not Explanation*. [Open full text](https://aclanthology.org/D19-1002/)
4. Olah et al. (2020), *Zoom In: An Introduction to Circuits*. [Open full text](https://distill.pub/2020/circuits/zoom-in/)

**Central debate:** What kinds of explanation are supported by similarity, predictability, and causal contribution? How can interventions test mechanistic hypotheses suggested by visualizations?

**Research output:** Compare correlational analyses with ablations/interventions. Report out-of-distribution stability, intervention side effects, and negative results, and design independent validation.

## G. Fairness, Distributed Cognition, and Sociotechnical Systems

**Prerequisites:** HCI, statistical decision making, social research methods, and research ethics.

1. Hutchins (1995), *Cognition in the Wild*. [Catalog search](https://search.worldcat.org/search?q=Hutchins+Cognition+in+the+Wild)
2. Suchman (2007), *Human–Machine Reconfigurations*. [Catalog search](https://search.worldcat.org/search?q=Suchman+Human+Machine+Reconfigurations)
3. Selbst, boyd, Friedler, Venkatasubramanian & Vertesi (2019), *Fairness and Abstraction in Sociotechnical Systems*. [DOI](https://doi.org/10.1145/3287560.3287598)
4. Gebru et al. (2021), *Datasheets for Datasets*. [Author preprint](https://arxiv.org/abs/1803.09010)
5. Mitchell et al. (2019), *Model Cards for Model Reporting*. [Author preprint](https://arxiv.org/abs/1810.03993)

**Central debate:** Which actors, institutions, and values are left out when a social problem is translated into a modeling objective?

**Research output:** Write a technical evaluation and contextual analysis of a human–AI decision system. Include dataset documentation, a model card, stakeholders, and deployment conditions, and discuss the value trade-offs behind different fairness metrics.

## Deliverables for Every Seminar

- A one-page map of the question and terminology, distinguishing normative, computational, algorithmic, implementational, and institutional levels.
- A related-work matrix of 10–20 papers, including classics, recent advances, critiques, and negative results; summarize each paper's methods and limitations.
- One reproduction study, formal derivation, or reconstruction of a philosophical argument.
- A 3–5-page proposal covering the research gap, competing hypotheses, identification/proof strategy, ethics, and failure criteria.
- One public presentation; for restricted data, use synthetic examples and a reproducible workflow to demonstrate the work.

**Keeping up with research:** Search titles in ACL Anthology, PMLR/JMLR, journal websites, and Semantic Scholar to locate published versions. Follow both references and citing papers. Use arXiv version histories and OpenReview discussions to trace developments.

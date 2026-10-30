# Online and Open Courses: From Foundations to Research Topics

[中文](../courses.md) | **English**

[← Home](../../README.en.md) · [Graduate Reading](graduate-reading.md) · [PhD Seminars](phd-seminars.md)

Use this course map alongside the reading lists: **build intuition through lectures, work through derivations with textbooks, and test your understanding through assignments.** At each stage, choose one main course and one companion reading or practical course to keep your progress manageable and steady.

## Choosing Courses

- **Video courses:** Structured recorded lectures that work well as the backbone of a self-study plan.
- **Open course materials:** Lecture notes, reading lists, assignments, and other resources for following a course schedule.
- **Hands-on online resources:** Code, interactive textbooks, or notebooks for learning by doing.
- **Platform courses:** Courses hosted on Coursera and similar platforms. Check the enrollment page for preview, audit, assignment, and certificate access.

The schedules below assume roughly **6–10 hours per week** of self-study. Course homepages may roll over to a new semester. Once you choose an edition, save its syllabus and assignment list so you can follow a consistent version throughout.

## Course Overview

| Stage | Recommended combination | Suggested output |
|---|---|---|
| Foundations | Python + linear algebra + probability + computing tools | A small data analysis project |
| Undergraduate core | Philosophy + logic + algorithms + psychology + linguistics | Argument essays, proofs, and experimental analyses |
| Specialization | Choose AI, NLP, cognition, neuroscience, or HCI | A course-level project |
| Graduate study | Statistical learning + optimization, causality, or graphical models | Derivations and paper replications |
| Research topics | Computational cognition, language and pragmatics, neural computation, and related topics | A research proposal and an independent report |

---

## I. Foundational Tools and Mathematics

### 1. Python: CS50P or MIT 6.0001

**Links:** [Harvard CS50P](https://cs50.harvard.edu/python/) · [MIT 6.0001, Fall 2016](https://ocw.mit.edu/courses/6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/)

- **Format:** Videos, teaching materials, and programming exercises.
- **Prerequisites:** High school mathematics; suitable for beginners.
- **Choosing between them:** CS50P focuses more on Python programming practices and tools; MIT 6.0001 emphasizes breaking down and solving problems through programs. Choose either as your main course.
- **Focus:** Functions, data structures, recursion, debugging, testing, and an intuitive understanding of complexity.
- **Suggested work:** Complete the course exercises in order, then build a small text analysis tool with tests.
- **Schedule:** 8–12 weeks, dividing your weekly time roughly equally between lectures and coding.

### 2. MIT The Missing Semester

**Link:** [Course homepage](https://missing.csail.mit.edu/)

- **Format:** Videos, notes, and exercises, with materials from multiple years available on the site.
- **Prerequisites:** The ability to write simple programs.
- **Focus:** The command line, scripting, editors, Git, debugging, and profiling.
- **Suggested work:** Set up a Git repository for subsequent courses and document your environment configuration and run commands.
- **Schedule:** 2–4 weeks; can run alongside Python.

### 3. MIT 18.06 Linear Algebra

**Link:** [Spring 2010 OCW](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/)

- **Format:** A complete set of recorded lectures, assignments, exams, and selected solutions.
- **Prerequisites:** Algebra and basic calculus; review vector and matrix operations as needed.
- **Focus:** The four fundamental subspaces, projections, least squares, eigenvalues, positive definiteness, and SVD.
- **Companion reading:** Hefferon's *Linear Algebra*, especially for additional work on definitions and proofs.
- **Suggested work:** Complete at least half the exercises, derive least squares by hand, and implement PCA in NumPy.
- **Schedule:** 10–14 weeks.

### 4. Calculus: MIT 18.01SC → 18.02SC

**Links:** [Single Variable Calculus, Fall 2010](https://ocw.mit.edu/courses/18-01sc-single-variable-calculus-fall-2010/) · [Multivariable Calculus, Fall 2010](https://ocw.mit.edu/courses/18-02sc-multivariable-calculus-fall-2010/)

- **Format:** Videos, worked examples, exercises, and quizzes organized for self-study.
- **Sequence:** Derivatives and integrals → multivariable functions → partial derivatives and gradients → multiple integrals.
- **Companion reading:** OpenStax *Calculus*.
- **Suggested work:** Explain the direction of a gradient, apply the chain rule by hand, and derive gradient descent updates for a simple model.
- **Schedule:** About 10–16 weeks per course; use individual chapters to fill gaps if you already have a foundation.

### 5. Harvard Stat 110

**Link:** [Course and textbook resources](https://stat110.hsites.harvard.edu/)

- **Format:** Recorded lectures, exercises, and textbook resources.
- **Prerequisites:** Single-variable calculus; basic multivariable calculus helps with continuous distributions.
- **Focus:** Conditional probability, random variables, expectation, common distributions, conditional expectation, and limit theorems.
- **Companion reading:** Blitzstein & Hwang, *Introduction to Probability*.
- **Suggested work:** Complete exercises on conditional probability, joint distributions, and expectation; reproduce three counterintuitive probability phenomena through simulation.
- **Schedule:** 12–16 weeks.

---

## II. Shared Undergraduate Core

### 6. Philosophy: Yale PHIL 181

**Link:** [Philosophy and the Science of Human Nature](https://oyc.yale.edu/philosophy/phil-181)

- **Format:** Open Yale Courses recordings, transcripts, reading schedules, and related materials.
- **Prerequisites:** None; a good opportunity to practice reading philosophy in English.
- **Focus:** Philosophical questions considered alongside research in psychology and cognitive science, including happiness, morality, and social structures.
- **Companion reading:** The SEP entries and Jim Pryor's writing guide listed on the home page; continue with Kim for philosophy of mind.
- **Suggested work:** Every two weeks, write an 800–1,500-word essay: reconstruct an argument, raise an objection, and respond to it.
- **Schedule:** 8–12 weeks.

### 7. Logic: Stanford Introduction to Logic

**Link:** [Coursera course](https://www.coursera.org/learn/logic-introduction)

- **Format:** Platform-hosted videos and exercises.
- **Prerequisites:** Basic mathematics and English reading skills.
- **Focus:** Formalization, logical semantics, and reasoning.
- **Companion reading:** The chapters on propositional logic, first-order logic, and natural deduction in *forall x: Calgary*.
- **Suggested work:** Create a reference table comparing semantics and proof rules, and complete at least 20 formalization or proof exercises.
- **Schedule:** 6–10 weeks.

### 8. Proofs and Discrete Mathematics: MIT 6.042J

**Link:** [Mathematics for Computer Science, Spring 2015](https://ocw.mit.edu/courses/6-042j-mathematics-for-computer-science-spring-2015/)

- **Format:** Videos, an open textbook, and exercises.
- **Prerequisites:** High school mathematics; some programming experience makes the applications easier to follow.
- **Focus:** Proofs, induction, graphs, counting, recursion, and discrete probability.
- **Companion reading:** Hammack's *Book of Proof*; read the introductory proof chapters in parallel.
- **Suggested work:** Produce a clearly typeset proof assignment each week and keep a record of corrections.
- **Schedule:** 12–16 weeks.

### 9. Data Structures and Algorithms: Stanford CS106B → MIT 6.006

**Links:** [CS106B](https://web.stanford.edu/class/cs106b/) · [MIT 6.006, Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)

- **Format:** CS106B provides semester-specific course materials; MIT 6.006 offers recorded lectures, notes, and assignments.
- **Prerequisites:** Basic programming. CS106B uses C++; 6.006 assignments require Python and a foundation in discrete mathematics.
- **Focus:** Abstract data types, recursion, graphs, sorting, dynamic programming, complexity, and correctness.
- **Companion reading:** Erickson's *Algorithms*.
- **Suggested work:** Implement solutions to graph search and dynamic programming problems, with a correctness argument and complexity analysis for each algorithm.
- **Schedule:** 8–12 weeks for CS106B, followed by 10–14 weeks for algorithms.

### 10. Computability: MIT 18.404J

**Link:** [Theory of Computation, Fall 2020](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/)

- **Format:** Videos, course notes, assignments, and exam materials.
- **Prerequisites:** Discrete mathematics, rigorous proof writing, and basic algorithms.
- **Focus:** Automata, computability, decidability, reductions, and complexity.
- **Companion reading:** Sipser's *Introduction to the Theory of Computation*.
- **Suggested work:** Choose a set of problems in each of three areas: automata construction, undecidability reductions, and NP-completeness proofs.
- **Schedule:** 10–14 weeks.

### 11. Psychology: MIT 9.00SC

**Link:** [Introduction to Psychology, Fall 2011](https://ocw.mit.edu/courses/9-00sc-introduction-to-psychology-fall-2011/)

- **Format:** Videos, readings, and self-study quizzes.
- **Prerequisites:** None.
- **Focus:** Cognition, learning, memory, development, social psychology, and research methods.
- **Companion reading:** OpenStax *Psychology 2e*, supplemented with more recent reviews on topics that interest you.
- **Suggested work:** Choose three experiments and describe each one's hypothesis, variables, control conditions, results, and alternative explanations.
- **Schedule:** 8–12 weeks.

### 12. Linguistics: MIT 24.900

**Link:** [Introduction to Linguistics, Fall 2012](https://ocw.mit.edu/courses/24-900-introduction-to-linguistics-fall-2012/)

- **Format:** Lecture notes, reading schedules, and assignment materials.
- **Prerequisites:** None; basic set theory and logic help with formal analysis.
- **Focus:** Phonology, morphology, syntax, semantics, and the systematic structure of language.
- **Companion reading:** *Essentials of Linguistics, 2nd edition*.
- **Suggested work:** Choose a set of exercises in each of three areas: phonological rule analysis, syntax trees, and semantic analysis.
- **Schedule:** 8–12 weeks; use the textbook as your main guide and the course assignments to test your understanding.

---

## III. Specialization

### 13. Artificial Intelligence: Stanford CS221

**Link:** [Artificial Intelligence: Principles and Techniques](https://stanford-cs221.github.io/)

- **Format:** Notes, assignments, and materials from past offerings; video access varies by semester.
- **Prerequisites:** Data structures, probability, linear algebra, and strong programming skills.
- **Focus:** Search, constraint satisfaction, games, MDPs, probabilistic inference, and learning.
- **Companion reading:** Poole & Mackworth's *Artificial Intelligence*.
- **Suggested work:** Complete one programming task each on search, MDPs, and probabilistic models, then choose a project that brings these ideas together.
- **Schedule:** 10–14 weeks.

### 14. Statistical Learning: ISLP / ISLR

**Link:** [An Introduction to Statistical Learning](https://www.statlearning.com/)

- **Format:** Full textbooks, companion courses, and lab code, with Python and R paths available.
- **Prerequisites:** Probability and statistics, linear algebra, and Python or R.
- **Focus:** Regression, classification, resampling, regularization, tree-based models, and unsupervised learning.
- **Companion reading:** Start with ISLP/ISLR as your main textbook, then read selected sections of *The Elements of Statistical Learning*.
- **Suggested work:** Complete one lab per chapter. Finish with a prediction project that includes data splitting, cross-validation, and error analysis.
- **Schedule:** 10–14 weeks.

### 15. Introduction to Deep Learning: MIT 6.S191

**Link:** [Introduction to Deep Learning](https://introtodeeplearning.com/)

- **Format:** Short-course videos, notes, and hands-on labs, released by year.
- **Prerequisites:** Python, linear algebra, calculus, and basic machine learning.
- **Focus:** Neural networks, sequence modeling, generative models, and emerging applications; content is updated each year.
- **Companion reading:** The chapters on optimization and basic architectures in *Deep Learning*.
- **Suggested work:** Complete the labs from a single year's offering and explain the loss functions, data pipeline, and training results.
- **Schedule:** 3–5 weeks; useful for exploring the field.

### 16. Natural Language Processing: Stanford CS224N

**Link:** [Natural Language Processing with Deep Learning](https://web.stanford.edu/class/cs224n/)

- **Format:** Course schedules, notes, video links, and programming assignments. Choose a semester with a complete set of public materials.
- **Prerequisites:** Python, linear algebra, probability, calculus, machine learning, and basic neural networks.
- **Focus:** Word representations, sequence models, attention, Transformers, language models, and evaluation.
- **Companion reading:** The relevant chapters in Jurafsky & Martin's *Speech and Language Processing*.
- **Suggested work:** Complete at least three programming assignments and a small NLP project, including analysis of linguistic phenomena and a classification of errors.
- **Schedule:** 10–14 weeks; allow time for training and debugging.

### 17. Computational Neuroscience: University of Washington Coursera Course

**Link:** [Computational Neuroscience](https://www.coursera.org/learn/computational-neuroscience)

- **Format:** Platform-hosted videos and exercises, taught by Rajesh P. N. Rao and Adrienne Fairhall.
- **Prerequisites:** Calculus, linear algebra, probability, and basic programming; study neurobiology alongside the course.
- **Focus:** Neural encoding, decoding, information, neuron models, and learning.
- **Companion reading:** Dayan & Abbott, or relevant chapters of *Neuronal Dynamics*.
- **Suggested work:** Reproduce an encoding or decoding example, vary the noise level, and analyze performance.
- **Schedule:** 8–12 weeks.

### 18. Neural Computation: MIT 9.40 and Neuromatch

**Links:** [MIT Introduction to Neural Computation, Spring 2018](https://ocw.mit.edu/courses/9-40-introduction-to-neural-computation-spring-2018/) · [Neuromatch Computational Neuroscience](https://compneuro.neuromatch.io/)

- **Format:** MIT provides course notes, readings, and assignments; Neuromatch provides videos, tutorials, and notebooks.
- **Prerequisites:** Probability, linear algebra, differential equations, Python, and basic neuroscience.
- **Choosing between them:** MIT suits a sequential study of theory; Neuromatch suits hands-on work organized by topic.
- **Focus:** Neural encoding, dynamical systems, statistical modeling, and cognitive computation.
- **Suggested work:** Choose a neural data tutorial, add model comparisons and cross-validation, and write up the results.
- **Schedule:** 10–14 weeks, or start with a 3–4-week exploration of a Neuromatch topic.

### 19. Games and Decisions: Stanford / UBC Game Theory

**Link:** [Game Theory](https://www.coursera.org/learn/game-theory-1)

- **Format:** Platform-hosted videos and exercises.
- **Prerequisites:** Basic probability and mathematical reasoning.
- **Focus:** Strategies, Nash equilibrium, mixed strategies, dynamic games, and games of incomplete information.
- **Companion reading:** Osborne's *An Introduction to Game Theory*.
- **Suggested work:** Analyze three types of small games, comparing equilibrium predictions with plausible real-world behavior.
- **Schedule:** 6–10 weeks.

### 20. Thinking with Multiple Models: Michigan Model Thinking

**Link:** [Model Thinking](https://www.coursera.org/learn/model-thinking)

- **Format:** Platform-hosted videos and quizzes, taught by Scott E. Page.
- **Prerequisites:** Basic mathematics; probability and programming experience support deeper simulation work.
- **Focus:** A range of mathematical and social science models and the questions they are suited to explaining.
- **Companion reading:** Salganik's *Bit by Bit*, as a bridge to practical digital social research.
- **Suggested work:** Choose a social phenomenon, analyze it using two different models, and compare their assumptions and explanatory power.
- **Schedule:** 8–12 weeks.

### 21. HCI: Stanford CS147

**Link:** [CS147 course directory](https://web.stanford.edu/class/cs147/)

- **Format:** Projects, notes, and schedules archived by semester; open a specific semester's page to begin.
- **Prerequisites:** Basic design communication and research methods; learn prototyping tools as your project requires.
- **Focus:** Exploring user needs, interaction design, prototyping, user evaluation, and iteration.
- **Companion reading:** Relevant chapters of *The Encyclopedia of Human-Computer Interaction*.
- **Suggested work:** Needs analysis → two rounds of prototyping → evaluation plan → iteration report. Study team project showcases to learn how to present your process.
- **Schedule:** 8–12 weeks; well suited to a group of 2–3 people.

---

## IV. Graduate Theory and Specialized Materials

### 22. Convex Optimization: Stanford EE364A

**Links:** [Convex Optimization I](https://web.stanford.edu/class/ee364a/) · [Textbook and supplementary resources](https://web.stanford.edu/~boyd/cvxbook/)

- **Format:** Lecture notes, assignments, and companion resources; follow the course's related links for recorded lectures.
- **Prerequisites:** Linear algebra, multivariable calculus, basic probability, and proof-writing skills.
- **Focus:** Convex sets, convex functions, duality, KKT conditions, optimization modeling, and numerical solution methods.
- **Suggested work:** Derive a dual problem by hand, then implement a regression or resource allocation model in CVXPY.
- **Schedule:** 10–14 weeks.

### 23. Causal Inference: Brady Neal

**Link:** [Introduction to Causal Inference](https://www.bradyneal.com/causal-inference-course)

- **Format:** Videos, notes, and reference materials.
- **Prerequisites:** Probability, regression, and basic statistics.
- **Focus:** Potential outcomes, structural causal models, confounding, identification, and estimation.
- **Companion reading:** *Causal Inference: What If* or *The Mixtape*.
- **Suggested work:** For a single research question, draw a DAG, define the estimand, and complete a synthetic-data experiment.
- **Schedule:** 8–12 weeks.

### 24. Probabilistic Graphical Models: Stanford CS228 Public Notes

**Link:** [CS228 Notes](https://ermongroup.github.io/cs228-notes/)

- **Format:** Structured public notes for study centered on reading and derivations.
- **Prerequisites:** Probability, linear algebra, algorithms, and basic machine learning.
- **Focus:** Graphical representations, conditional independence, exact inference, approximate inference, and parameter and structure learning.
- **Companion reading:** Murphy's *Probabilistic Machine Learning: Advanced Topics*.
- **Suggested work:** Implement variable elimination for a small graphical model and compare it with sampling-based estimates.
- **Schedule:** 8–12 weeks.

### 25. Computational Cognition: Probabilistic Models of Cognition

**Link:** [ProbMods](https://probmods.org/)

- **Format:** An online textbook with code examples and exercises, suitable as a hands-on course.
- **Prerequisites:** Probability, basic programming, and an introduction to cognitive science.
- **Focus:** Probabilistic programs, inference, concepts, inductive learning, and language understanding.
- **Companion reading:** The computational cognition module in the graduate reading list.
- **Suggested work:** Choose a concept-learning or reasoning model, change its priors, and analyze its behavioral predictions.
- **Schedule:** 8–10 weeks.

### 26. Neural Networks and Cognition: Stanford PSYCH 209 Archived Materials

**Link:** [Neural Network Models of Cognition](https://web.stanford.edu/class/psych209/)

- **Format:** Readings, computational assignments, and final project plans from past semesters; useful as a guided reading path through the topic.
- **Prerequisites:** Neural networks, psychology, probability, and programming.
- **Focus:** Connectionism, distributed representations, learning, perception, and cognitive modeling.
- **Companion reading:** Marr's *Vision* and readings on competing models from the computational cognition module.
- **Suggested work:** Choose an archived assignment and reimplement it with modern tools; write a 4–6-page model analysis.
- **Schedule:** 8–12 weeks.

### 27. Probabilistic Pragmatics: ProbLang / RSA

**Link:** [Probabilistic Language Understanding](https://www.problang.org/)

- **Format:** Online chapters, probabilistic models, and example code.
- **Prerequisites:** Bayesian inference and basic linguistic semantics and pragmatics.
- **Focus:** Recursive inference between speakers and listeners, reference, informativeness, and pragmatic reasoning.
- **Companion reading:** Grice, Frank & Goodman, and the PhD language seminar topics.
- **Suggested work:** Implement a minimal RSA model and compare the predictions of literal and pragmatic listeners.
- **Schedule:** 4–8 weeks; well suited to a focused reading group.

---

## V. Four Ready-to-Start Study Tracks

### A. Starting from Scratch: 16 Weeks

**Allow 8–12 hours per week. Use Python as your main course and psychology to build interdisciplinary interest.**

| Weeks | Main course | Alongside it | Output |
|---|---|---|---|
| 1–4 | CS50P fundamentals | Missing Semester: command line and Git | A repository for a small program, with a README |
| 5–8 | CS50P data processing and testing | MIT 9.00SC: research methods, learning, and memory | A short experimental analysis |
| 9–12 | Integrated Python exercises | 18.06: matrices, subspaces, and projections | Code demonstrating projections and least squares |
| 13–16 | A small text or behavioral data project | Continue linear algebra; write a short philosophical argument essay | Code, figures, and a 2–3-page report |

Cover the core modules of linear algebra and psychology during these 16 weeks, then continue toward completing both courses.

### B. Natural Language and Cognition: Two Semesters

**Prerequisites:** Programming, probability, and linear algebra.

- **Semester 1, 12–16 weeks:** Use MIT 24.900 as your main course, alongside an introduction to formal semantics and logic exercises.
- **Semester 2, 12–16 weeks:** Use CS224N as your main course and read selected RSA tutorials. Take 6.S191 first if you have little deep learning experience.
- **Final project:** Choose a phenomenon involving ambiguity, quantifiers, or pragmatics, and compare linguistic analysis, probabilistic models, and neural models.

### C. Computational Cognition and Neuroscience: Two Semesters

**Prerequisites:** Probability, Python, linear algebra, and basic psychology.

- **Semester 1, 12–16 weeks:** Choose either Washington's Computational Neuroscience course or MIT 9.40, alongside Neuromatch exercises.
- **Semester 2, 12–16 weeks:** Use either ProbMods or the PSYCH 209 materials as your main path and complete a model comparison.
- **Final project:** Choose a learning, categorization, or decision-making task, and compare two models in terms of fit, recovery, and held-out prediction.

### D. Preparation for AI and Causal Research: Two Semesters

**Prerequisites:** Algorithms, probability, linear algebra, calculus, and basic machine learning.

- **Semester 1, 12–16 weeks:** Use EE364A as your main course, alongside the representation and inference chapters of CS228.
- **Semester 2, 12–16 weeks:** Use Brady Neal's causal inference course as your main course, read selected statistical learning theory, and replicate a paper on causal generalization.
- **Final project:** In an environment with a known data-generating mechanism, analyze optimization objectives, identification assumptions, and out-of-distribution performance.

## VI. A Weekly Study Template

```text
Session 1: Watch lectures; record 3 key concepts and 1 question.
Session 2: Read the companion textbook; fill in definitions and derivations.
Session 3: Work independently on exercises or programming assignments.
Session 4: Make corrections, run tests, write a study log, and commit your work to Git.
Every 4 weeks: Bring together what you have learned in a small project or short report.
```

**Recommended course sequence:** Start with a course whose assignments you can tackle now. In each study cycle, choose one main course and one reading or tools course. After completing the cycle, move to the next level according to your project's needs.

## Access and Version Notes

This page was compiled on **2026-10-30**. Pages consulted during compilation included MIT 6.0001, 6.042J, 9.00SC, 24.900, and 9.40; Yale PHIL 181; CS224N; PSYCH 209; Brady Neal; 6.S191; ISLP; Missing Semester; and selected Coursera pages. The remaining links come from official course homepages or resources already included in the reading lists.

In your own study log, save the course title, institution or instructor, semester, homepage, assignment list, and start date. Check Coursera enrollment pages for access options. Submission systems and automated grading for semester-based courses follow the arrangements for that particular offering.

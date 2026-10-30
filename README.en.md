# Symbolic Systems: A Self-Study Guide

### Mind, language, computation, and interdisciplinary research

[中文](README.md) | **English**

[![Learning](https://img.shields.io/badge/learning-interdisciplinary-blue)](#curriculum-and-sources)
[![License: CC BY 4.0](https://img.shields.io/badge/content-CC_BY_4.0-lightgrey)](LICENSE)

> An interdisciplinary learning path inspired by **Stanford's Symbolic Systems curriculum**: **undergraduate foundations → concentrations → graduate theory → doctoral research**.
>
> An independently compiled guide. The curriculum structure draws on Stanford's official pages; the reading lists and study plans are editorial selections.

## Contents

- [Curriculum and sources](#curriculum-and-sources)
- [How to use this guide](#how-to-use-this-guide)
- [Learning map](#learning-map)
- [Undergraduate reading](#undergraduate-reading)
- [Choose a concentration](#choose-a-concentration)
- [Graduate study and research](#graduate-study-and-research)
- [Online courses and study tracks](#online-courses-and-study-tracks)
- [Suggested schedule](#suggested-schedule)
- [Open resources](#open-resources)
- [Contributing and licensing](#contributing-and-licensing)

## Curriculum and sources

Stanford's undergraduate curriculum combines **methodological training, interdisciplinary connections, and research practice**:

| Curriculum component | A self-study equivalent |
|---|---|
| Preparations: gateway course, calculus, linear algebra | An introduction to minds and machines; mathematical foundations |
| Philosophical Analysis | Argumentation, philosophy of mind and language |
| Formal Methods | Logic, computability, probability, statistics |
| Computational Methods | Programming, algorithms, computational modeling |
| Empirical Cognitive Science | Psychology, cognitive science, linguistic theory |
| Cross-Area Requirement | A project combining at least two methodological approaches |
| Concentration | Sustained study in one area |
| Advanced Small Seminar, Capstone, Presentation | Reading group, replication, independent research, public presentation |

**Official sources, consulted October 30, 2026:**

1. [B.S. Program](https://symsys.stanford.edu/undergraduates/bs-program)
2. [Major Policies & Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements)
3. [Core Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements/core-requirements): version G4.3, effective September 1, 2026, updated October 27, 2026. Covers the four methodological areas, cross-area work, a five-course concentration, and experiential requirements.
4. [Concentrations](https://symsys.stanford.edu/undergraduates/concentrations)
5. [M.S. Program](https://symsys.stanford.edu/graduates/masters-program): a research-based degree centered on language, information, and human and machine intelligence, bringing together at least two related disciplines.

Core course examples include SYMSYS 1, PHIL 80, CS 103, CS 106A/B, and PSYCH 1. Each area offers several options; see the official pages and the relevant year's Bulletin for course planning.

The doctoral reading section brings together research questions shared by cognitive science, computer science, linguistics, philosophy, psychology, and neuroscience.

## How to use this guide

- **★ Core**: choose one main text per module.
- **＋ Further reading**: add when a research question calls for it.
- **[Full text]**: readable through the author, publisher, university, or open publishing platform.
- **[Course]**: lectures, notes, assignments, and other teaching materials.
- **[Book page]**: publisher or book information; usually available through purchase or a library.
- **[Preprint]**: a research manuscript; record the version you use and follow subsequent revisions.

Entries link to original sources and identify the access type. Use the original English titles when searching for editions and library copies.

## Learning map

```text
Mathematics: calculus → linear algebra → probability/statistics → optimization / measure-theoretic probability
Formal methods: proofs → first-order logic → computability → complexity / type theory
Computation: Python → data structures and algorithms → AI / statistical modeling
Empirical work: psychology → experimental design → cognitive / language / neural data
Philosophy: argumentation → philosophy of mind / language / science
                              ↓
              One main area + one complementary method
                              ↓
             Replication → research question → independent paper
```

Study mathematics, psychology, and philosophy in parallel, adding the relevant prerequisites as you move into proofs, machine learning, and neural modeling.

## Undergraduate reading

### 0. Minds and machines: map the questions

| Priority | Resource | Focus |
|---|---|---|
| ★ | José Luis Bermúdez, *Cognitive Science: An Introduction to the Science of the Mind* [Book page](https://www.cambridge.org/highereducation/search?searchTerm=Cognitive%20Science%20Bermudez) | Connect representation, computation, psychological experiments, and neural explanations; map several levels of explanation for one cognitive phenomenon |
| ★ | Alan Turing (1950), *Computing Machinery and Intelligence* [DOI](https://doi.org/10.1093/mind/LIX.236.433) | Separate questions about thinking, operational tests, and the nature of intelligence |
| ＋ | Andy Clark, *Mindware: An Introduction to the Philosophy of Cognitive Science* [Book page](https://global.oup.com/academic/product/mindware-9780199828159) | Compare classical computation, connectionism, and embodied approaches |

**Exercise:** write a short essay on whether predicting behavior amounts to explaining a mind. Include a thesis, counterexample, reply, and testable prediction.

### 1. Mathematics and probability

| Priority | Resource | Focus |
|---|---|---|
| ★ | OpenStax, *Calculus* [Full text](https://openstax.org/subjects/math) | Single- and multivariable calculus, partial derivatives, integration; select chapters as needed |
| ★ | Hefferon, *Linear Algebra* [Full text](https://hefferon.net/linearalgebra/) | Vector spaces, linear maps, orthogonality, eigenvalues; proofs and computation |
| ★ | MIT 18.06 Linear Algebra [Course](https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/) | Matrix methods, projections, least squares, SVD |
| ★ | Hammack, *Book of Proof* [Full text](https://www.people.vcu.edu/~rhammack/BookOfProof/) | Sets, functions, induction, contradiction, precise writing |
| ★ | Harvard Stat 110 / Blitzstein & Hwang [Course and author resources](https://stat110.hsites.harvard.edu/) | Conditional probability, random variables, expectation, laws of large numbers, central limit theorem; available textbook versions are listed on the site |
| ＋ | Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* [Full text](https://mml-book.github.io/) | Connect linear algebra, matrix calculus, and probability to modeling |

**Exercise:** derive least squares; simulate Bayes' rule and the central limit theorem; explain the distinction between correlation and causation.

### 2. Philosophical analysis: mind, language, and science

| Priority | Resource | Focus |
|---|---|---|
| ★ | [Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/) (SEP) [Full text] | Start with [Computational Theory of Mind](https://plato.stanford.edu/entries/computational-mind/), [Functionalism](https://plato.stanford.edu/entries/functionalism/), and [Mental Representation](https://plato.stanford.edu/entries/mental-representation/) |
| ★ | Jaegwon Kim, *Philosophy of Mind* [Library search](https://search.worldcat.org/search?q=Jaegwon+Kim+Philosophy+of+Mind) | Physicalism, mental causation, functionalism, consciousness |
| ★ | [Jim Pryor: Guidelines on Writing a Philosophy Paper](https://www.jimpryor.net/teaching/guidelines/writing.html) [Full text] | Organizing a thesis, reconstructing arguments, developing objections |
| ＋ | [SEP: Scientific Explanation](https://plato.stanford.edu/entries/scientific-explanation/) and [Models in Science](https://plato.stanford.edu/entries/models-science/) [Full text] | Prediction, mechanisms, explanation, and idealized models |

**Exercise:** reconstruct functionalism and one objection to it. Make the premises, inferences, and conclusions explicit in a short paper.

### 3. Formal methods: logic and computation

| Priority | Resource | Focus |
|---|---|---|
| ★ | *forall x: Calgary* [Full text](https://forallx.openlogicproject.org/) | Propositional and first-order logic, semantics, natural deduction |
| ★ | *Open Logic Project* [Full text](https://openlogicproject.org/) | Advanced logic, computability, metalogic; use after the introductory material |
| ★ | Michael Sipser, *Introduction to the Theory of Computation* [Library search](https://search.worldcat.org/search?q=Sipser+Introduction+to+the+Theory+of+Computation) | Automata, decidability, reductions, complexity |
| ＋ | MIT 18.404J Theory of Computation [Course](https://ocw.mit.edu/courses/18-404j-theory-of-computation-fall-2020/) | Companion lectures and exercises |

**Exercise:** complete natural deduction proofs, prove a problem undecidable, and explain validity, soundness, and completeness.

### 4. Computational methods: programs to models

| Priority | Resource | Focus |
|---|---|---|
| ★ | [CS50P](https://cs50.harvard.edu/python/) [Course] | Python, testing, exceptions, file handling |
| ★ | [Stanford CS106B](https://web.stanford.edu/class/cs106b/) [Course] | Recursion, abstract data types, data structures; prepare for its use of C++ |
| ★ | Jeff Erickson, *Algorithms* [Full text](https://jeffe.cs.illinois.edu/teaching/algorithms/) | Recursion, dynamic programming, greedy algorithms, graphs, correctness proofs |
| ★ | Poole & Mackworth, *Artificial Intelligence: Foundations of Computational Agents* [Full text](https://artint.info/) | Search, constraints, knowledge representation, uncertainty, decision making |
| ＋ | [Stanford CS221](https://stanford-cs221.github.io/) [Course] | Connect algorithms to reasoning, planning, and learning |

**Exercise:** implement search algorithms, naive Bayes, and a constraint solver. Report complexity, baselines, and failure cases.

### 5. Empirical cognitive science: psychology, experiments, neuroscience

| Priority | Resource | Focus |
|---|---|---|
| ★ | OpenStax, *Psychology 2e* [Full text](https://openstax.org/details/books/psychology-2e) | Psychology, memory, learning, development, research methods |
| ★ | Navarro, *Learning Statistics with R* [Full text](https://learningstatisticswithr.com/) | Estimation, hypothesis tests, models, and data analysis in R |
| ★ | [Research Methods in Psychology](https://opentextbc.ca/researchmethods/) [Full text] | Operationalization, reliability, validity, experimental design, ethics |
| ＋ | *Neuroscience Online*, UTHealth [Full text](https://nba.uth.tmc.edu/neuroscience/) | Neural foundations, sensory and motor systems, higher functions |
| ＋ | Gazzaniga, Ivry & Mangun, *Cognitive Neuroscience: The Biology of the Mind* [Library search](https://search.worldcat.org/search?q=Gazzaniga+Ivry+Mangun+Cognitive+Neuroscience) | Evidence from behavior, brain injury, and imaging |

**Exercise:** design a reaction-time experiment. Specify confounds, sample-size rationale, exclusion criteria, and an analysis plan. Prepare informed consent, privacy protections, and the appropriate ethics review for human-participant work.

### 6. Linguistic theory: language structure to computational models

| Priority | Resource | Focus |
|---|---|---|
| ★ | Anderson et al., *Essentials of Linguistics, 2nd edition* [Full text](https://ecampusontario.pressbooks.pub/essentialsoflinguistics2/) | Phonetics, phonology, morphology, syntax, semantics |
| ★ | Paul H. Portner, *What Is Meaning? Fundamentals of Formal Semantics* [Library search](https://search.worldcat.org/search?q=Paul+Portner+What+Is+Meaning) | Reference, truth conditions, compositionality, quantification |
| ★ | Jurafsky & Martin, *Speech and Language Processing*, 3rd ed. draft [Full text](https://web.stanford.edu/~jurafsky/slp3/) | Connect linguistic phenomena to computational models; record the draft version cited |
| ＋ | [Natural Language Toolkit Book](https://www.nltk.org/book/) [Full text] | Introductory corpus work and language processing; useful hands-on exercises alongside current modeling material |

**Exercise:** give two scope readings for a quantified sentence. Analyze a small corpus and relate linguistic hypotheses to model errors.

## Choose a concentration

The names below come from the official Concentrations page. The suggested combinations translate them into self-study paths. Start with one main area.

| Concentration | Suggested combination |
|---|---|
| Applied Logic | Logic + computability + formal verification |
| Artificial Intelligence | Probability + algorithms + machine learning |
| Biomedical Applications | Biomedical foundations + statistical modeling + research ethics |
| Cognitive Science | Psychological experiments + computational cognition + philosophical explanation |
| Computational Foundations | Algorithms + complexity + programming languages |
| Computational Social Science | Social theory + causal inference + network data |
| Computer Music | Signal processing + music cognition + interactive systems |
| Decision Making and Rationality | Decision theory + game theory + behavioral experiments |
| Human-Centered Artificial Intelligence | AI + HCI + values and social impact |
| Human-Computer Interaction | Interaction design + experimental methods + sociotechnical analysis |
| Learning | Learning sciences + cognitive development + statistical learning |
| Mathematical Foundations | Analysis + probability + logic |
| Media and Communication | Communication theory + platform studies + empirical methods |
| Natural Language | Linguistic theory + pragmatics + NLP |
| Neurosciences | Neural foundations + dynamical systems + statistical models |
| Philosophical Foundations | Philosophy of mind and language + logic + philosophy of science |
| Individually Designed Concentrations | Combine areas around a clear research question; enrolled students follow the formal approval process |

The advanced reading focuses on logic, AI, cognition, language, neuroscience, and sociotechnical research. Biomedical applications and computer music can build on these foundations with additional specialist study.

## Graduate study and research

- **[Graduate theory and readings](docs/en/graduate-reading.md)**: probability, learning theory, causality, information theory, computational cognition, neuroscience, semantics, logic, decisions, and HCI.
- **[Doctoral seminars and classic papers](docs/en/phd-seminars.md)**: research questions, debates, models, and papers.
- **[Research practice and projects](docs/en/research-practice.md)**: replication, open science, proposals, and research milestones.
- **[Sources and maintenance](docs/en/sources.md)**: curriculum references, selection principles, and link maintenance.

## Online courses and study tracks

**[Complete course map →](docs/en/courses.md)**: 27 groups of online courses and public course materials, with prerequisites, formats, companion books, suggested assignments, and study schedules.

| Interest | Starting points |
|---|---|
| Programming and mathematics | CS50P / MIT 6.0001, Missing Semester, MIT 18.06, Harvard Stat 110 |
| Philosophy and logic | Yale PHIL 181, Stanford Introduction to Logic, MIT 6.042J |
| Psychology and language | MIT 9.00SC, MIT 24.900 |
| AI and NLP | CS221, ISLP/ISLR, MIT 6.S191, CS224N |
| Cognition and neuroscience | Washington Computational Neuroscience, MIT 9.40, Neuromatch, ProbMods |
| Decisions and interaction | Game Theory, Model Thinking, CS147 |
| Graduate methods | EE364A, Brady Neal's causal inference course, CS228 notes, RSA tutorials |

Four ready-to-follow tracks cover **a 16-week beginner plan, language and cognition, computational cognition and neuroscience, and preparation for AI and causality research**.

## Suggested schedule

A flexible **24-month plan at 10–15 hours per week**, assuming some prior preparation. Adjust the pace to your background and research interests.

- [ ] Months 1–3: introduction + Python + linear algebra + argumentation
- [ ] Months 4–6: probability + first-order logic + introductory psychology
- [ ] Months 7–9: algorithms + computability + experimental design
- [ ] Months 10–12: linguistics + philosophy of mind + a small cross-area project
- [ ] Months 13–15: choose a concentration, study an advanced text, fill mathematical gaps
- [ ] Months 16–18: replicate a paper; document discrepancies and failure cases
- [ ] Months 19–21: reading seminar, related-work matrix, research proposal
- [ ] Months 22–24: independent research prototype + runnable repository + report + poster

**Weekly rhythm:** four hours of textbook study and exercises, three of implementation or data analysis, two of papers, and one of writing. Use remaining time for prerequisites, discussion, and review. Assess each stage through exercises, implementations, or short papers.

## Open resources

| Resource | Use | Suggested approach |
|---|---|---|
| [MIT OpenCourseWare](https://ocw.mit.edu/) / [Stanford Engineering Everywhere](https://see.stanford.edu/) | Mathematics and computing courses | Supplement older courses with current material |
| [SEP](https://plato.stanford.edu/) / [Internet Encyclopedia of Philosophy](https://iep.utm.edu/) | Philosophical overviews and bibliographies | Follow references into original research |
| [Open Logic Project](https://openlogicproject.org/) / [OpenStax](https://openstax.org/) | Open textbooks | Consult each resource's license |
| [ACL Anthology](https://aclanthology.org/) | NLP and computational linguistics papers | Check venue, year, and paper type |
| [arXiv](https://arxiv.org/) / [PhilArchive](https://philarchive.org/) | Preprints and author archives | Cite the version used |
| [PMLR](https://proceedings.mlr.press/) / [JMLR](https://www.jmlr.org/) | Machine learning research | Examine experimental design alongside claims |
| [OpenReview](https://openreview.net/) | Papers, reviews, discussion | Read reviews and publication decisions together |
| [OSF](https://osf.io/) | Preregistration, data, materials, replication | Check project licenses and data-use conditions |
| [DANDI](https://dandiarchive.org/) / [OpenNeuro](https://openneuro.org/) | Open neuroscience data | Follow data-use terms and analysis conventions |
| [PhilPapers](https://philpapers.org/) / [Semantic Scholar](https://www.semanticscholar.org/) | Discovery and citation tracing | Follow records to publisher or author copies |

## Contributing and licensing

Issues and pull requests are welcome for corrections, broken links, open editions, and well-motivated additions. Include the author, title, year or edition, prerequisites, recommendation rationale, access type, and original source. Favor substantial resources with a clear role in the learning path.

Original writing is licensed under [CC BY 4.0](LICENSE). Linked resources retain their own copyright and license terms.

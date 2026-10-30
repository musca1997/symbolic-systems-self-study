# Research Practice: From Reading to Independent Research

[← Home](../../README.en.md) · [Chinese version](../research-practice.md)

## Learning Goals Across Three Stages

| Stage | Core abilities | Appropriate outputs |
|---|---|---|
| Undergraduate core | Understand methods, solve exercises, and analyze basic evidence | Small projects, clear arguments, and runnable implementations |
| Graduate study | Reconstruct papers, select models, and identify assumptions and limitations | Reproduction reports, research proposals, and master's-level research prototypes |
| PhD research | Formulate valuable, tractable new questions and engage with peer scrutiny | Original arguments, theorems, methods, or evidence with a clear contribution |

Measure progress through concrete outputs, and seek ongoing feedback from supervisors, peers, or reading groups.

## Interdisciplinary Project Menu

### Project 1: Bounded-Rational Language Inference

- **Fields:** Formal semantics/pragmatics + Bayesian modeling + psychological experiments.
- **Task:** Implement a minimal Rational Speech Act model and compare it with literal-interpretation and heuristic baselines.
- **Data:** Prefer openly available data with clear licensing, or synthetic data. Follow ethical requirements for experiments with human participants.
- **Evaluation:** Held-out predictions, prior sensitivity, and parameter recovery; analyze the conditions under which the two models can be distinguished.

### Project 2: Correlation and Causation in Visual Classification

- **Fields:** Machine learning + causal inference + scientific explanation.
- **Task:** Generate data with correlated shapes and backgrounds. Compare empirical risk minimization (ERM) with a robust method under environmental shifts.
- **Evaluation:** Environment splits, independent random seeds, confidence intervals, failure cases, known mechanisms, and assumptions.
- **Extension:** Move from synthetic to real data and analyze the additional identification assumptions and measurement errors.

### Project 3: Does the Model Use Syntax?

- **Fields:** Linguistics + neural models + interpretability.
- **Task:** Minimal-pair tests, structural probes, control tasks, and targeted interventions.
- **Evaluation:** Leakage checks, lexical controls, probe capacity, and whether interventions disrupt unrelated information.
- **Extension:** Use interventions to test whether the model actually uses the information revealed by the probe.

### Project 4: Human–AI Decision Making and the Division of Cognitive Labor

- **Fields:** HCI + decision theory + distributed cognition.
- **Task:** Study which tasks and presentation formats allow AI advice to support or interfere with judgment.
- **Evaluation:** Preregistration, controls, order effects, learning effects, effect sizes, and uncertainty.
- **Implementation:** Prefer everyday, low-risk tasks. Arrange ethical approval and informed consent in advance for studies with human participants.

## Minimum Standards for Reproduction Studies

- [ ] Record the research question, published paper version, code version, and data license.
- [ ] Distinguish reproducing the original results from testing on independent data, and define the terminology you use.
- [ ] Document hardware, software environment, random seeds, and run commands.
- [ ] Run simple baselines before complex models.
- [ ] Check figures, tables, data cleaning, hyperparameter selection, and evaluation protocols.
- [ ] Report error bars, computational budgets, failed runs, and departures from the original paper.
- [ ] Prepare materials for public release by removing personal data, credentials, restricted data, and copyrighted material requiring permission.

## Suggested Research Repository Structure

```text
project/
├── README.md             # Question, results, limitations, and how to run
├── environment.yml       # Or pyproject.toml / another pinned environment
├── data/README.md        # Data sources, licenses, and acquisition steps
├── src/
├── tests/
├── configs/
├── notebooks/
├── results/              # Traceable summary results
├── report.md
└── references.bib
```

## Paper Reading Card

```text
Bibliographic details/version:
Research question:
Claim type: empirical / theoretical / normative / philosophical
Key definitions and assumptions:
Methods and baselines:
Evidence or proof:
Scope of conclusions supported by the evidence:
Alternative explanations and limitations:
Reproduction resources and licenses:
Relevance to my question:
Next falsifiable prediction:
```

## Research Proposal Template

1. **Question and significance:** What knowledge do you aim to advance, and why is it worth studying?
2. **Current knowledge and gaps:** Which results are established, and which conclusions conflict?
3. **Competing hypotheses:** Give at least two possible explanations and observations that would distinguish them.
4. **Methods:** Proofs, experiments, simulations, interviews, or mixed methods, with the appropriate evidential standards for each.
5. **Validity:** Identification assumptions, statistical power/precision, model recovery, and external validity.
6. **Open science and ethics:** Preregistration, licensing, privacy, and data management.
7. **Feasibility:** Time, computing resources, data, and tools; a smaller fallback question if the original plan proves unworkable.
8. **Contribution criteria:** What counts as success, and which results would require revising the claims?

## PhD Research Self-Assessment

- Can you explain the question's disciplinary grounding and its interdisciplinary contribution?
- Are the core definitions and assumptions precise enough for others to challenge?
- Can you clearly articulate the strongest objection?
- Have you checked relevant counterexamples, negative results, duplication of existing research, and data leakage?
- What new knowledge does the work contribute beyond changes in tools, datasets, or terminology?
- Can others inspect the derivations, rerun the results, or evaluate the argument?
- Do supervisors, peers, or reading groups provide independent criticism?

Recommended companions: [The Turing Way](https://book.the-turing-way.org/) for reproducible research and collaboration; [OSF](https://osf.io/) for preregistration and materials; [Zotero](https://www.zotero.org/) for reference management.

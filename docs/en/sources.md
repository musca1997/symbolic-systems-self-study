# Sources and Maintenance

[← Home](../../README.en.md) · [Chinese version](../sources.md)

## Sources for the Curriculum Structure

Consulted: **2026-10-30**.

The undergraduate structure draws on Stanford's Symbolic Systems website. The bibliography, study schedule, and graduate and PhD topics were compiled by the guide's editor.

| Source | Material consulted |
|---|---|
| [Core Requirements](https://symsys.stanford.edu/undergraduates/major-policies-requirements/core-requirements) | Preparations, the four Breadth categories, Cross-Area, Advanced Small Seminar, Capstone, and presentation requirements; page version G4.3 |
| [Concentrations](https://symsys.stanford.edu/undergraduates/concentrations) | Concentration names and groupings; individual concentration pages provide detailed course-selection rules |
| [Master's Program](https://symsys.stanford.edu/graduates/masters-program) | The research-oriented master's program and its themes of language, information, intelligence, and interdisciplinary research |

For formal course selection and degree planning, consult the Stanford Bulletin for the relevant academic year. The PhD section is organized around research questions shared across related disciplines and is designed for thematic reading and reading groups.

## Reading Selection Principles

1. Prioritize authors, universities, publishers, original papers, and open publishing platforms.
2. Give each module core and advanced readings, prerequisites, reading priorities, and suggested deliverables.
3. Link paid books to publisher information or library catalogs for purchase or borrowing.
4. Label open resources as full texts, courses, or preprints, and record versions when citing them.
5. Read classics alongside recent research, including competing explanations, critiques, and negative results.

## Link Maintenance

The repository includes `scripts/check_links.py`, which requires Python 3 and curl. Run it from the repository root:

```bash
python scripts/check_links.py --local-only
python scripts/check_links.py > link-check.tsv
```

The initial check corrected an HCI resource URL and one DOI encoding issue, and local file links passed validation. External links scheduled for rechecking include WorldCat, publishers, some DOI links, and university websites that returned timeouts, HTTP 403 responses, or transport errors.

For alternative access, search a library catalog, the publisher's website, or the author's homepage using the author and full title. To report a link issue, include the URL, error message, and date accessed in a repository Issue.

## Future Expansion

The current focus is logic, AI, cognition, language, neuroscience, and sociotechnical research. Biomedical topics, computer music, and other areas are already included in the navigation; contributions of specialized bibliographies and courses are welcome.

## License

Original text is licensed under [CC BY 4.0](../../LICENSE). Linked books, papers, courses, and datasets retain their respective copyrights and terms of use.

# Paper directory

This directory contains the manuscript and its supporting assets.

## Current state

The paper currently exists as a working Markdown source. The LaTeX submission package (`main.tex`, `refs.bib`, `main.bbl`, `figures/`) will be added here prior to arXiv submission. The Markdown source will then be removed in favor of LaTeX as the canonical source, per standard math-ph publishing practice.

## Files (when LaTeX is added)

```
paper/
├── main.tex            # Canonical LaTeX source
├── main.bbl            # Compiled bibliography (kept in repo per arXiv requirements)
├── refs.bib            # BibTeX source
├── figures/            # Paper figures (with generation scripts)
└── README.md           # This file
```

## Compiling the LaTeX source (when present)

```bash
cd paper
latexmk -pdf main.tex
```

To clean build artifacts:

```bash
latexmk -C
```

## arXiv submission

When ready, the arXiv submission tarball is assembled manually:

```bash
cd paper
latexmk -pdf main.tex
tar czf ../arxiv_submission.tar.gz main.tex main.bbl refs.bib figures/
```

Note that arXiv's processing pipeline (since April 2025) requires `main.bbl` to be included alongside `main.tex` for biblatex submissions; do not omit it.

## License

The paper text is licensed under Creative Commons Attribution 4.0 International (CC BY 4.0). See repository-root `LICENSE` for full terms.

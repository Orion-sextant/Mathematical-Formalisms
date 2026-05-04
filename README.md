# Mathematical Formalisms

Mathematical work by **Jared D. Dunahay**
*AEO Trivector LLC, Bedford, NH*

[![Verify](https://github.com/Orion-sextant/Mathematical-Formalisms/actions/workflows/verify.yml/badge.svg)](https://github.com/Orion-sextant/Mathematical-Formalisms/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/code-MIT-yellow.svg)](LICENSE)
[![Papers: CC BY 4.0](https://img.shields.io/badge/papers-CC%20BY%204.0-lightgrey.svg)](LICENSE)

---

This repository is the public companion to mathematical papers and formalisms by Jared D. Dunahay. Each paper lives in its own self-contained subdirectory under [`papers/`](papers/), with the manuscript source, verification code, unit tests, and a deterministic reproduction script.

## Papers

| Year | Title | Status | Code | arXiv | DOI |
|------|-------|--------|------|-------|-----|
| 2026 | A Canonical Non-Commutative Deformation of $\mathbb{T}^8$ Indexed by $\mathrm{Cl}(3,0)$: Spectrum, Pfaffian, and a Pythagorean Spectral Identity | Submitted | [`papers/2026-noncommutative-t8-clifford/`](papers/2026-noncommutative-t8-clifford/) | *(pending)* | *(pending)* |

Each paper directory contains a self-contained README with the theorem-claim-test traceability map, installation, and reproduction instructions.

## Quick verification

To verify all computational claims across all papers in this repository:

```bash
git clone https://github.com/Orion-sextant/Mathematical-Formalisms.git
cd Mathematical-Formalisms
make verify
```

`make verify` installs each paper's package and runs its test suite. Continuous integration runs the same workflow on every commit.

## What "verifies" means here

The unit tests in this repository **verify** the finite algebraic computations stated in the corresponding papers. They check that the canonical data, closed-form identities, and spectral computations reported in print are reproduced exactly (to numerical precision) by independent symbolic and numerical implementations.

The tests do **not** prove the underlying theorems. The proofs are in the papers; the code reproduces the load-bearing computations on which the proofs rest.

## Structure

```
Mathematical-Formalisms/
│
├── README.md                              # This file
├── LICENSE                                # MIT (code) + CC BY 4.0 (papers)
├── CITATION.cff                           # Repository-wide citation metadata
├── Makefile                               # Top-level orchestration
├── pyproject.toml                         # Repository-wide dev tooling
├── .gitignore
├── .github/workflows/verify.yml           # CI: install + test every paper
│
└── papers/
    └── YYYY-paper-slug/
        ├── README.md                      # Paper-specific verification map
        ├── paper/
        │   ├── main.tex                   # LaTeX source
        │   ├── main.bbl                   # Bibliography (kept for arXiv)
        │   ├── refs.bib
        │   └── figures/
        ├── src/                           # Implementation
        ├── tests/                         # Pytest suite
        ├── examples/
        │   └── reproduce_paper_claims.py  # Single deterministic script
        └── pyproject.toml                 # Paper-specific package
```

## Citation

Each paper has its own preferred citation; please cite the relevant paper directly. Software citations are accumulated under a single Zenodo DOI for this repository at each tagged release. See `CITATION.cff` and individual paper subdirectories for details.

## License

- **Code** (`src/`, `tests/`, `examples/`): MIT License
- **Papers and prose documentation** (`papers/*/paper/`, READMEs): Creative Commons Attribution 4.0 International (CC BY 4.0)

See `LICENSE` for full text.

## Author

**Jared D. Dunahay**
AEO Trivector LLC, Bedford, NH

## Archival

Tagged releases are archived to Zenodo, which since November 2024 automatically deposits each release into Software Heritage. This provides each release with both a citable DOI and a persistent SWHID for long-term source preservation.

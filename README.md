# Mathematical Formalisms

Mathematical work by **Jared D. Dunahay**
*AEO Trivector LLC, Bedford, NH*

[![Verify](https://github.com/Orion-sextant/Mathematical-Formalisms/actions/workflows/verify.yml/badge.svg)](https://github.com/Orion-sextant/Mathematical-Formalisms/actions/workflows/verify.yml)
[![License: MIT](https://img.shields.io/badge/code-MIT-yellow.svg)](LICENSE)
[![Papers: CC BY 4.0](https://img.shields.io/badge/papers-CC%20BY%204.0-lightgrey.svg)](LICENSE)
[![ORCID](https://img.shields.io/badge/ORCID-0009-0004-5735-2872-A6CE39?logo=orcid&logoColor=white)](https://orcid.org/0009-0004-5735-2872)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20031519.svg)](https://doi.org/10.5281/zenodo.20031519)

---

This repository is the public companion to mathematical papers and formalisms by Jared D. Dunahay. Each paper lives in its own self-contained subdirectory under [`papers/`](papers/), with the manuscript source, verification code, unit tests, and a deterministic reproduction script.

## Papers

| Year | Title | Status | Code | arXiv | DOI |
|------|-------|--------|------|-------|-----|
| 2026 | A Canonical Non-Commutative Deformation of $\mathbb{T}^8$ Indexed by $\mathrm{Cl}(3,0)$: Spectrum, Pfaffian, and a Pythagorean Spectral Identity | Submitted | [`papers/2026-noncommutative-t8-clifford/`](papers/2026-noncommutative-t8-clifford/) | *(pending)* | [10.5281/zenodo.20031520](https://doi.org/10.5281/zenodo.20031520) |

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
ORCID: [0009-0004-5735-2872](https://orcid.org/0009-0004-5735-2872)

## Archival

Tagged releases are archived on [Zenodo](https://zenodo.org/), which automatically deposits each release into the [Software Heritage Archive](https://www.softwareheritage.org/). Each release carries both a citable DOI and a persistent SWHID for long-term source preservation.

| Identifier | Type | Points to |
|---|---|---|
| [10.5281/zenodo.20031519](https://doi.org/10.5281/zenodo.20031519) | Concept DOI | All versions of this repository |
| [10.5281/zenodo.20031520](https://doi.org/10.5281/zenodo.20031520) | Version DOI | v1.0.0 specifically |

When citing this software, prefer the **concept DOI**, which always resolves to the latest version. When citing a specific snapshot used to reproduce results, use the corresponding version DOI.

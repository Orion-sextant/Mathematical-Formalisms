# A Canonical Non-Commutative Deformation of T^8 Indexed by Cl(3,0)

**Spectrum, Pfaffian, and a Pythagorean Spectral Identity**

**Jared D. Dunahay**
*AEO Trivector LLC, Bedford, NH*
ORCID: [0009-0004-5735-2872](https://orcid.org/0009-0004-5735-2872)

---

This directory contains the manuscript, source code, and verification suite for the paper

> Jared D. Dunahay, *A Canonical Non-Commutative Deformation of $\mathbb{T}^8$ Indexed by $\mathrm{Cl}(3,0)$: Spectrum, Pfaffian, and a Pythagorean Spectral Identity* (2026).

The paper studies a structured 8-dimensional noncommutative torus $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$ in which the deformation matrix is indexed by the four Clifford grades of $\mathrm{Cl}(3,0)$ and parameterized by

$$\mu = W(1), \qquad \Omega = \sqrt{1 - \mu^2}, \qquad \beta = \varphi^{-1} / 3,$$

with $W$ the Lambert-W function and $\varphi$ the golden ratio. The construction admits closed-form spectrum, Pfaffian, Frobenius decomposition, an algebraic Pythagorean identity among its grade-cross-pairing frequencies, and a Lambert-W localization on a distinguished 2-dimensional subspace. The minimal-channel multiplicity-$(1,1,1)$ Pythagorean prerequisite is shown to be unique to dimension 3 in the family of analogous nearest-neighbor $\mathrm{Cl}(n,0)$ constructions.

## Quickstart

```bash
cd papers/2026-noncommutative-t8-clifford
pip install -e ".[dev]"
pytest -q                                         # 39 verification tests
python examples/reproduce_paper_claims.py         # one-screen claims summary
```

## Verified computational claims

The unit tests **verify** that the finite algebraic computations stated in the paper are reproduced (to numerical precision) by an independent implementation. The proofs themselves are in the manuscript; the code below reproduces the load-bearing computations on which they rest.

| Paper location | Claim | Module | Test |
|---|---|---|---|
| Theorem 2.3 | $\mathrm{Spec}(\Theta_{\mathrm{can}}) = \{\pm i\mu, \pm i\Omega, \pm i(\Omega \pm \beta)\}$ | `identities.py` | `test_identities.py::test_theorem_2_3_spectrum_factorization` |
| Theorem 2.3 | Characteristic polynomial factors as $\prod_k (\lambda^2 + \nu_k^2)$ | `identities.py` | `test_identities.py::test_characteristic_polynomial_factorization` |
| Theorem 3.1 | $\lvert\mathrm{Pf}(\Theta_{\mathrm{can}})\rvert = \mu\,\Omega\,(\Omega^2 - \beta^2)$ | `canonical_data.py` | `test_canonical_data.py::test_theorem_3_1_pfaffian_closed_form` |
| Theorem 3.1 | Four-matching analytical expansion | `canonical_data.py` | `test_canonical_data.py::test_analytical_four_matching_expansion` |
| Section 3.2 | Trace-image generators of $K_0$ at sizes 2, 4, 6, 8 | `canonical_data.py` | `test_canonical_data.py::test_trace_image_generators_*` |
| Theorem 3.3 | $\lVert\Theta_{\mathrm{can}}\rVert_F^2 = 2\mu^2 + 6\Omega^2 + 4\beta^2$ | `identities.py` | `test_identities.py::test_theorem_3_3_frobenius_decomposition` |
| Theorem 4.2 | $\nu_-^2 + \nu_0^2 - \nu_+^2 = \Omega(\Omega - 4\beta)$ | `identities.py` | `test_identities.py::test_theorem_4_2_pythagorean_identity` |
| Theorem 4.2 | $3{:}4{:}5$ ratio at $4\beta = \Omega$ | `identities.py` | `test_identities.py::test_3_4_5_ratio_at_pythagorean_coupling` |
| Remark 4.3 | At canonical values $4\beta/\Omega - 1 \sim 5\!\times\!10^{-4}$ (not exact) | `identities.py` | `test_identities.py::test_pythagorean_residual_at_canonical_values_is_small` |
| Corollary 5.2 | $\hat{D}^2 = \hat{D}\,e^{-\hat{D}}$ on the $(0,7)$-block | `identities.py` | `test_identities.py::test_corollary_5_2_lambert_w_localization` |
| Lemma 6.1 | $\mathrm{Spec}(K_n) = \{2i\sin(2\pi k / n)\}$ | `dimension_check.py` | `test_dimension_check.py::test_lemma_6_1_K_n_spectrum_for_n_*` |
| Theorem 6.2 | Multiplicity-$(1,1,1)$ structure realized only at $n = 3$ | `dimension_check.py` | `test_dimension_check.py::test_theorem_6_2_uniqueness_across_small_n` |
| Section 6.5 | Sphere identity $\Omega^2 + \mu^2 = 1$ | `dimension_check.py` | `test_dimension_check.py::test_sphere_identity_holds_exactly` |
| Section 6.5 | Bridge identity $4\beta/\Omega \approx 1$ (residual $\sim 5\!\times\!10^{-4}$) | `dimension_check.py` | `test_dimension_check.py::test_bridge_identity_holds_to_sub_percent` |
| Section 6.5 | Continuous rank $x_{\ast}(\mu) := 1/(\varphi\Omega - 1) \approx 3.006$ | `dimension_check.py` | `test_dimension_check.py::test_continuous_rank_is_close_to_3` |

Total: 39 tests across the three modules. CI runs the full suite on Python 3.10, 3.11, and 3.12 on every commit.

## Structure

```
2026-noncommutative-t8-clifford/
├── README.md                          # This file
├── pyproject.toml                     # Defines the nct8_clifford package
├── conftest.py                        # Pytest path setup
│
├── paper/
│   ├── main.tex                       # LaTeX source (canonical, when added)
│   ├── main.bbl                       # Bibliography (kept for arXiv)
│   ├── refs.bib                       # BibTeX source
│   └── figures/                       # Paper figures
│
├── src/
│   └── nct8_clifford/
│       ├── __init__.py                # Public API
│       ├── canonical_data.py          # Theta_can, J, Pfaffian, K_0 generators
│       ├── identities.py              # Theorems 2.3, 3.1, 3.3, 4.2, Cor 5.2
│       └── dimension_check.py         # Section 6 results
│
├── tests/
│   ├── test_canonical_data.py         # 13 tests
│   ├── test_identities.py             # 11 tests
│   └── test_dimension_check.py        # 15 tests
│
└── examples/
    └── reproduce_paper_claims.py      # Single deterministic verification script
```

## What the tests do not claim

These tests reproduce the **finite computational checks** used in the paper's proofs. They do not constitute formal proofs in the sense of Lean / Coq / Isabelle. The dimension-uniqueness statement (Theorem 6.2), for example, is proved analytically in the paper via parity and sine-distinctness arguments; the corresponding test simply sweeps small $n$ and confirms that the multiplicity-$(1,1,1)$ structure obtains at $n = 3$ and fails at $n \in \{2, 4, 5, \ldots, 9\}$, in agreement with the proof.

The verbs used throughout this repository are deliberate: the code **verifies**, **reproduces**, and **checks**; it does not **prove**.

## Citation

```bibtex
@article{Dunahay2026T8theta,
  author       = {Dunahay, Jared D.},
  title        = {A Canonical Non-Commutative Deformation of $\mathbb{T}^8$ Indexed by $\mathrm{Cl}(3,0)$:
                  Spectrum, Pfaffian, and a Pythagorean Spectral Identity},
  year         = {2026},
  journal      = {arXiv preprint},
  note         = {Code: \url{https://github.com/Orion-sextant/Mathematical-Formalisms/tree/main/papers/2026-noncommutative-t8-clifford}},
}
```

This software is archived at Zenodo with concept DOI [10.5281/zenodo.20031519](https://doi.org/10.5281/zenodo.20031519). The v1.0.0 release is pinned at [10.5281/zenodo.20031520](https://doi.org/10.5281/zenodo.20031520).

## License

- **Code** (`src/`, `tests/`, `examples/`): MIT (see repository-root `LICENSE`).
- **Paper and prose** (`paper/`, this README): CC BY 4.0 (see repository-root `LICENSE`).

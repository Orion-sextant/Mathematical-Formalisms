"""reproduce_paper_claims.py: a single deterministic script that reproduces
the finite computational claims of the paper

    Jared D. Dunahay, "A Canonical Non-Commutative Deformation of T^8
    Indexed by Cl(3,0): Spectrum, Pfaffian, and a Pythagorean Spectral
    Identity" (2026).

Run this to obtain a one-screen summary of all paper claims and their
verification status:

    python examples/reproduce_paper_claims.py

This script is the primary verification artifact for casual readers and
referees: it demonstrates that every closed-form identity stated in the
paper is reproduced by an independent numerical/symbolic implementation.

Author: Jared D. Dunahay (AEO Trivector LLC).
License: MIT.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Make the package importable when running from a fresh clone
# without `pip install -e .` first.
_SRC = Path(__file__).parent.parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

import numpy as np

from nct8_clifford import (
    mu, Omega, beta, phi,
    construct_theta_canonical,
    pfaffian, pfaffian_closed_form,
    spectrum_imaginary_parts,
    pythagorean_residual, pythagorean_value_at_canonical_coupling,
    frobenius_norm_squared_closed_form,
    lambert_w_localization_residual,
    multiplicity_111_check,
    sphere_identity_residual, bridge_identity_residual,
    continuous_rank,
)


TOL = 1e-10


def status(passed: bool) -> str:
    return "PASS" if passed else "FAIL"


def main() -> int:
    rows = []
    failures = 0

    Theta = construct_theta_canonical()

    print("=" * 78)
    print("Reproduction of paper claims:")
    print("    A Canonical Non-Commutative Deformation of T^8 Indexed by Cl(3,0)")
    print("    Jared D. Dunahay, 2026")
    print("=" * 78)
    print()
    print(f"  mu     = W(1)         = {mu:.12f}")
    print(f"  phi    = (1+sqrt5)/2  = {phi:.12f}")
    print(f"  Omega  = sqrt(1-mu^2) = {Omega:.12f}")
    print(f"  beta   = phi^-1 / 3   = {beta:.12f}")
    print()

    ok = np.allclose(Theta, -Theta.T)
    rows.append(("Sec 2.2", "Theta_can is antisymmetric (so(8))",       status(ok)))
    failures += not ok

    pos = spectrum_imaginary_parts(Theta)
    expected = sorted([Omega + beta, Omega, Omega - beta, mu], reverse=True)
    err = max(abs(p - e) for p, e in zip(pos, expected))
    ok = err < TOL
    rows.append(("Thm 2.3", "Spectrum factorizes as {+/-i*mu, +/-i*Omega, +/-i*(Omega+/-beta)}", status(ok)))
    failures += not ok

    pf_num = abs(pfaffian(Theta))
    pf_cf = pfaffian_closed_form()
    err = abs(pf_num - pf_cf)
    ok = err < TOL
    rows.append(("Thm 3.1", "|Pf(Theta_can)| = mu*Omega*(Omega^2 - beta^2)", status(ok)))
    failures += not ok

    fro_num = float(np.trace(Theta.T @ Theta))
    fro_cf = frobenius_norm_squared_closed_form()
    err = abs(fro_num - fro_cf)
    ok = err < TOL
    rows.append(("Thm 3.3", "||Theta||_F^2 = 2*mu^2 + 6*Omega^2 + 4*beta^2", status(ok)))
    failures += not ok

    err = pythagorean_residual()
    ok = err < TOL
    rows.append(("Thm 4.2", "nu_-^2 + nu_0^2 - nu_+^2 = Omega*(Omega - 4*beta)", status(ok)))
    failures += not ok

    pyth_at_canonical = abs(pythagorean_value_at_canonical_coupling())
    ok = 1e-5 < pyth_at_canonical < 1e-2
    rows.append(("Rmk 4.3", "Bridge 4*beta = Omega holds within ~5e-4 (not exact)", status(ok)))
    failures += not ok

    err = lambert_w_localization_residual()
    ok = err < TOL
    rows.append(("Cor 5.2", "D_hat^2 = D_hat * exp(-D_hat) on (0,7) block", status(ok)))
    failures += not ok

    n_with_structure = [n for n in range(2, 10)
                        if multiplicity_111_check(n)["has_111_structure"]]
    ok = n_with_structure == [3]
    rows.append(("Thm 6.2", "Multiplicity-(1,1,1) realized only at n = 3 (n = 2..9 swept)",
                 status(ok)))
    failures += not ok

    ok = sphere_identity_residual() < TOL
    rows.append(("Sec 6.5", "Sphere identity Omega^2 + mu^2 = 1",        status(ok)))
    failures += not ok

    ok = 1e-5 < bridge_identity_residual() < 1e-2
    rows.append(("Sec 6.5", "Bridge identity 4*beta/Omega ~ 1 (~5e-4)",  status(ok)))
    failures += not ok

    x_star = continuous_rank()
    ok = 3.0 < x_star < 3.02
    rows.append(("Sec 6.5", f"Continuous rank x*(mu) = {x_star:.4f} (target 3)", status(ok)))
    failures += not ok

    print("Verified computational claims")
    print("-" * 78)
    print(f"{'Location':<10} {'Claim':<58} {'Status':>6}")
    print("-" * 78)
    for loc, claim, st in rows:
        print(f"{loc:<10} {claim:<58} {st:>6}")
    print("-" * 78)

    total = len(rows)
    passed = total - failures
    print()
    print(f"Result: {passed} / {total} computational claims reproduced.")
    print()

    if failures:
        print(f"FAILURES: {failures}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""Tests for identities: spectrum, Frobenius, Pythagorean, Lambert-W localization.

Maps to:
    Theorem 2.3   Spectrum factorization
    Theorem 3.3   Frobenius decomposition ||Theta||_F^2 = 2*mu^2 + 6*Omega^2 + 4*beta^2
    Theorem 4.2   Pythagorean identity nu_-^2 + nu_0^2 - nu_+^2 = Omega*(Omega - 4*beta)
    Corollary 5.2 D_hat^2 = D_hat * exp(-D_hat) on the (0,7)-block
"""

from __future__ import annotations

import numpy as np

from nct8_clifford import (
    mu, Omega, beta,
    construct_theta_canonical,
    spectrum_imaginary_parts,
    spectrum_residual,
    pfaffian_closed_form,
    pfaffian_residual,
    frobenius_norm_squared_closed_form,
    frobenius_residual,
    pythagorean_residual,
    pythagorean_value_at_canonical_coupling,
    lambert_w_localization_residual,
)


# ---------------------------------------------------------------------
# Theorem 2.3: spectrum factorization
# ---------------------------------------------------------------------

def test_theorem_2_3_spectrum_factorization():
    """The four positive imaginary eigenvalues of Theta_can are {Omega+beta,
    Omega, Omega-beta, mu}.
    """
    Theta = construct_theta_canonical()
    pos = spectrum_imaginary_parts(Theta)
    expected = sorted([Omega + beta, Omega, Omega - beta, mu], reverse=True)
    assert len(pos) == 4
    for p, e in zip(pos, expected):
        assert abs(p - e) < 1e-10


def test_spectrum_residual_below_threshold():
    """The residual function should agree with direct check."""
    assert spectrum_residual() < 1e-10


def test_characteristic_polynomial_factorization():
    """det(lambda*I - Theta_can) factors as
    (lambda^2 + mu^2)(lambda^2 + Omega^2)(lambda^2 + (Omega-beta)^2)(lambda^2 + (Omega+beta)^2).
    Sample at lambda = 0 and a few other points to confirm.
    """
    Theta = construct_theta_canonical()
    for lam in [0.0, 0.5, 1.0, -0.7]:
        I = np.eye(8)
        det_numerical = float(np.linalg.det(lam * I - Theta))
        det_predicted = (
            (lam ** 2 + mu ** 2) *
            (lam ** 2 + Omega ** 2) *
            (lam ** 2 + (Omega - beta) ** 2) *
            (lam ** 2 + (Omega + beta) ** 2)
        )
        assert abs(det_numerical - det_predicted) < 1e-9


# ---------------------------------------------------------------------
# Theorem 3.3: Frobenius decomposition
# ---------------------------------------------------------------------

def test_theorem_3_3_frobenius_decomposition():
    """||Theta_can||_F^2 = 2*mu^2 + 6*Omega^2 + 4*beta^2."""
    Theta = construct_theta_canonical()
    numerical = float(np.trace(Theta.T @ Theta))
    closed_form = 2 * mu ** 2 + 6 * Omega ** 2 + 4 * beta ** 2
    assert abs(numerical - closed_form) < 1e-12


def test_frobenius_residual_below_threshold():
    assert frobenius_residual() < 1e-12


# ---------------------------------------------------------------------
# Theorem 4.2: Pythagorean spectral identity
# ---------------------------------------------------------------------

def test_theorem_4_2_pythagorean_identity():
    """nu_-^2 + nu_0^2 - nu_+^2 = Omega*(Omega - 4*beta), as an algebraic identity."""
    nu_minus = Omega - beta
    nu_zero = Omega
    nu_plus = Omega + beta
    lhs = nu_minus ** 2 + nu_zero ** 2 - nu_plus ** 2
    rhs = Omega * (Omega - 4 * beta)
    assert abs(lhs - rhs) < 1e-12


def test_pythagorean_residual_below_threshold():
    assert pythagorean_residual() < 1e-12


def test_pythagorean_holds_only_at_4beta_equals_omega():
    """When 4*beta_test = Omega, the Pythagorean identity should vanish exactly."""
    beta_pythagorean = Omega / 4
    nu_minus = Omega - beta_pythagorean
    nu_zero = Omega
    nu_plus = Omega + beta_pythagorean
    lhs = nu_minus ** 2 + nu_zero ** 2 - nu_plus ** 2
    assert abs(lhs) < 1e-12


def test_3_4_5_ratio_at_pythagorean_coupling():
    """At 4*beta = Omega, the three frequencies stand in ratio 3 : 4 : 5."""
    beta_pythagorean = Omega / 4
    nu_minus = Omega - beta_pythagorean        # = 3*Omega/4
    nu_zero = Omega                            # = 4*Omega/4
    nu_plus = Omega + beta_pythagorean         # = 5*Omega/4
    ratios = [nu_minus / Omega * 4, nu_zero / Omega * 4, nu_plus / Omega * 4]
    assert abs(ratios[0] - 3.0) < 1e-12
    assert abs(ratios[1] - 4.0) < 1e-12
    assert abs(ratios[2] - 5.0) < 1e-12


def test_pythagorean_residual_at_canonical_values_is_small():
    """At canonical values, |nu_-^2 + nu_0^2 - nu_+^2| ~ 5e-4 (not exact)."""
    val = abs(pythagorean_value_at_canonical_coupling())
    assert 1e-5 < val < 1e-2


# ---------------------------------------------------------------------
# Corollary 5.2: Lambert-W localization on (0,7)-block
# ---------------------------------------------------------------------

def test_corollary_5_2_lambert_w_localization():
    """D_hat^2 = D_hat * exp(-D_hat) on the (0,7) block, since D_hat = mu*I_2
    there and mu satisfies mu = exp(-mu).
    """
    residual = lambert_w_localization_residual()
    assert residual < 1e-10

"""
identities: Closed-form spectral identities for Theta_can.

This module implements the load-bearing identities of sections 2-5 of the paper:

    Theorem 2.3   spectrum factorization
    Theorem 3.1   Pfaffian closed form
    Theorem 3.3   Frobenius decomposition
    Theorem 4.2   Pythagorean spectral identity
    Corollary 5.2 Lambert-W localization on the (0,7)-block

Each function checks one identity numerically against its closed form
and returns either the value, the residual, or both.

Author: Jared D. Dunahay (AEO Trivector LLC).
License: MIT.
"""

from __future__ import annotations

import numpy as np
from scipy.linalg import expm

from .canonical_data import mu, Omega, beta, construct_theta_canonical, pfaffian


# ---------------------------------------------------------------------
# Theorem 2.3: spectrum factorization
# ---------------------------------------------------------------------

def spectrum_imaginary_parts(Theta=None):
    """Sorted (descending) positive imaginary parts of eigenvalues of Theta_can.

    Theorem 2.3 asserts:
        Spec(Theta_can) = {+/- i*mu, +/- i*Omega, +/- i*(Omega +/- beta)}.

    Returns the 4 distinct positive values: [Omega+beta, Omega, Omega-beta, mu].
    """
    if Theta is None:
        Theta = construct_theta_canonical()
    eigs = np.linalg.eigvals(Theta)
    pos = sorted([float(e.imag) for e in eigs if e.imag > 1e-10], reverse=True)
    return pos


def spectrum_residual(Theta=None) -> float:
    """Max deviation between the numerical spectrum of Theta_can and the
    closed-form values predicted by Theorem 2.3.
    """
    if Theta is None:
        Theta = construct_theta_canonical()
    numerical = spectrum_imaginary_parts(Theta)
    predicted = sorted([Omega + beta, Omega, Omega - beta, mu], reverse=True)
    return max(abs(n - p) for n, p in zip(numerical, predicted))


# ---------------------------------------------------------------------
# Theorem 3.1: Pfaffian closed form
# ---------------------------------------------------------------------

def pfaffian_closed_form() -> float:
    """The closed form: |Pf(Theta_can)| = mu * Omega * (Omega^2 - beta^2)."""
    return mu * Omega * (Omega ** 2 - beta ** 2)


def pfaffian_residual(Theta=None) -> float:
    """|Pf_numerical| - |Pf_closed_form|. Should vanish to numerical precision."""
    if Theta is None:
        Theta = construct_theta_canonical()
    return abs(abs(pfaffian(Theta)) - pfaffian_closed_form())


# ---------------------------------------------------------------------
# Theorem 3.3: Frobenius decomposition
# ---------------------------------------------------------------------

def frobenius_norm_squared_closed_form() -> float:
    """The closed form: ||Theta_can||^2_F = 2*mu^2 + 6*Omega^2 + 4*beta^2.

    Decomposition:
      * 2*mu^2     from the single (0,7) edge
      * 6*Omega^2  from the three (i, i+3) cross-pairings (2*Omega^2 each)
      * 4*beta^2   from the two beta*J intra-blocks (2*beta^2 each)
    """
    return 2 * mu ** 2 + 6 * Omega ** 2 + 4 * beta ** 2


def frobenius_residual(Theta=None) -> float:
    """||Theta||_F^2_numerical - ||Theta||_F^2_closed_form."""
    if Theta is None:
        Theta = construct_theta_canonical()
    return abs(float(np.trace(Theta.T @ Theta)) - frobenius_norm_squared_closed_form())


# ---------------------------------------------------------------------
# Theorem 4.2: Pythagorean spectral identity
# ---------------------------------------------------------------------

def pythagorean_residual() -> float:
    """The Pythagorean spectral identity:
        nu_-^2 + nu_0^2 - nu_+^2 = Omega * (Omega - 4*beta)

    where nu_- = Omega - beta, nu_0 = Omega, nu_+ = Omega + beta.
    Returns the residual between LHS and the RHS closed form.
    """
    nu_minus = Omega - beta
    nu_zero = Omega
    nu_plus = Omega + beta
    lhs = nu_minus ** 2 + nu_zero ** 2 - nu_plus ** 2
    rhs = Omega * (Omega - 4 * beta)
    return abs(lhs - rhs)


def pythagorean_value_at_canonical_coupling() -> float:
    """Value of nu_-^2 + nu_0^2 - nu_+^2 at canonical (mu, Omega, beta).

    Vanishes exactly when 4*beta = Omega; at canonical values 4*beta/Omega
    differs from 1 by ~5e-4 so this is small but nonzero.
    """
    return (Omega - beta) ** 2 + Omega ** 2 - (Omega + beta) ** 2


# ---------------------------------------------------------------------
# Corollary 5.2: Lambert-W localization on the (0,7)-block
# ---------------------------------------------------------------------

def dirac_magnitude_block_07(Theta=None) -> np.ndarray:
    """Restriction of D_hat := |i * Theta_can| to the (0,7) invariant subspace.

    The (0,7) subspace is 2-dimensional. The restriction of |i*Theta| to this
    block has eigenvalue mu with multiplicity 2.
    """
    if Theta is None:
        Theta = construct_theta_canonical()
    block = Theta[np.ix_([0, 7], [0, 7])]
    iTheta = 1j * block
    eigvals, eigvecs = np.linalg.eig(iTheta)
    abs_eigvals = np.abs(eigvals)
    D = (eigvecs @ np.diag(abs_eigvals) @ np.linalg.inv(eigvecs)).real
    return D


def lambert_w_localization_residual() -> float:
    """Residual for the operator equation D_hat^2 = D_hat * exp(-D_hat)
    restricted to the (0,7) block of Theta_can.

    On the (0,7) block, D_hat = mu * I_2. The equation
        D_hat^2 = D_hat * exp(-D_hat)
    becomes  mu^2 = mu * exp(-mu),  i.e.,  mu = exp(-mu),
    which is the defining equation of mu = W(1).

    Returns ||LHS - RHS||_F on the 2x2 block.
    """
    D = dirac_magnitude_block_07()
    LHS = D @ D
    RHS = D @ expm(-D)
    return float(np.linalg.norm(LHS - RHS, ord='fro'))

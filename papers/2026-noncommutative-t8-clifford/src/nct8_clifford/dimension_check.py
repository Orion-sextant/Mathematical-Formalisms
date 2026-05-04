"""
dimension_check: Cl(n,0) dimension specificity for the multiplicity-(1,1,1)
Pythagorean prerequisite (section 6 of the paper).

This module implements:

    Definition 6.1   K_n := C_n - C_n^{-1} for n >= 3 (with K_2 a special case)
    Lemma 6.1        Spec(K_n) = {2 i sin(2*pi*k/n) : k = 0, ..., n-1}
    Theorem 6.2      Among integer n >= 2, only n = 3 produces a multiplicity-(1,1,1)
                     spectrum {-c, 0, +c} for the nearest-neighbor cyclic generator K_n.

It also provides the structural identities that pin n=3 in this construction:
the sphere identity, the bridge identity, and the continuous-rank value.

Author: Jared D. Dunahay (AEO Trivector LLC).
License: MIT.
"""

from __future__ import annotations

import numpy as np

from .canonical_data import mu, Omega, beta, phi


# ---------------------------------------------------------------------
# Cyclic-shift antisymmetric generator K_n
# ---------------------------------------------------------------------

def cyclic_shift(n: int) -> np.ndarray:
    """Cyclic shift permutation matrix on R^n.

    (C_n)_{j,i} = 1 iff j == i + 1 (mod n).  Acts as C_n e_i = e_{i+1 mod n}.
    """
    if n < 2:
        raise ValueError("n must be >= 2")
    C = np.zeros((n, n), dtype=float)
    for i in range(n):
        C[(i + 1) % n, i] = 1.0
    return C


def cyclic_generator(n: int) -> np.ndarray:
    """The nearest-neighbor cyclic-shift antisymmetric generator K_n in so(n).

    For n >= 3:  K_n := C_n - C_n^{-1}.
    For n == 2:  the standard symplectic generator [[0, -1], [1, 0]]
                  (since C_2 == C_2^{-1}, the formula above degenerates).
    """
    if n == 2:
        return np.array([[0.0, -1.0], [1.0, 0.0]])
    if n < 2:
        raise ValueError("n must be >= 2")
    C = cyclic_shift(n)
    return C - C.T  # C^{-1} = C^T for a permutation matrix


def spectrum_K_n(n: int) -> np.ndarray:
    """Numerical eigenvalues of K_n (returned as complex array)."""
    return np.linalg.eigvals(cyclic_generator(n))


def spectrum_K_n_predicted(n: int) -> np.ndarray:
    """Closed-form spectrum of K_n per Lemma 6.1, sorted by imaginary part."""
    if n == 2:
        return np.array([1j, -1j])
    vals = np.array([2j * np.sin(2 * np.pi * k / n) for k in range(n)])
    return vals


def spectrum_K_n_residual(n: int, atol: float = 1e-10) -> float:
    """Max absolute distance between numerical and closed-form spectra of K_n."""
    num = sorted(spectrum_K_n(n), key=lambda z: (z.imag, z.real))
    pred = sorted(spectrum_K_n_predicted(n), key=lambda z: (z.imag, z.real))
    return max(abs(a - b) for a, b in zip(num, pred))


# ---------------------------------------------------------------------
# Theorem 6.2: only n = 3 gives multiplicity-(1,1,1) for K_n
# ---------------------------------------------------------------------

def multiplicity_111_check(n: int, tol: float = 1e-9) -> dict:
    """For Spec(K_n), check whether it has the form {-c, 0, +c}
    each with multiplicity exactly 1 (i.e., n == 3 must hold for the exact case;
    other n must fail in some specific way).

    Returns a dict with:
      'spectrum_imag'        : sorted list of imaginary parts
      'zero_multiplicity'    : count of eigenvalues with |im| < tol
      'distinct_pos_pairs'   : count of distinct positive imaginary values
      'has_111_structure'    : True iff zero_mult == 1 and distinct_pos_pairs == 1
    """
    eigs = spectrum_K_n(n)
    imags = sorted(e.imag for e in eigs)
    zero_mult = sum(1 for v in imags if abs(v) < tol)
    pos_imags = [v for v in imags if v > tol]
    distinct = []
    for v in pos_imags:
        if not any(abs(v - u) < tol for u in distinct):
            distinct.append(v)
    return {
        "n": n,
        "spectrum_imag": imags,
        "zero_multiplicity": zero_mult,
        "distinct_pos_pairs": len(distinct),
        "has_111_structure": zero_mult == 1 and len(distinct) == 1,
    }


# ---------------------------------------------------------------------
# Structural identities pinning the construction to n = 3
# ---------------------------------------------------------------------

def sphere_identity_residual() -> float:
    """Omega^2 + mu^2 = 1 should hold exactly."""
    return abs(Omega ** 2 + mu ** 2 - 1.0)


def bridge_identity_residual() -> float:
    """4 * beta = Omega holds approximately at canonical values; residual ~5e-4.

    Returns |4*beta/Omega - 1|.
    """
    return abs(4 * beta / Omega - 1.0)


def continuous_rank() -> float:
    """The continuous rank x*(mu) := 1 / (phi * Omega - 1).

    At mu = W(1), phi = (1+sqrt(5))/2, Omega = sqrt(1 - mu^2):
    this evaluates to ~3.006, distinguishing n = 3 as the closest integer.
    """
    return 1.0 / (phi * Omega - 1.0)


def structural_identities() -> dict:
    """The three structural identities that pin n=3 for this construction.

    Returns {name: (numerical_value, target, |residual|)}.
    """
    return {
        "sphere (Omega^2 + mu^2)":   (Omega ** 2 + mu ** 2, 1.0, sphere_identity_residual()),
        "bridge (4*beta/Omega)":     (4 * beta / Omega,     1.0, bridge_identity_residual()),
        "continuous rank x*(mu)":    (continuous_rank(),    3.0, abs(continuous_rank() - 3.0)),
    }

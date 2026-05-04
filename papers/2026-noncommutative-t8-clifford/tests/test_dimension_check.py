"""Tests for dimension_check: Cl(n,0) dimension specificity.

Maps to:
    Lemma 6.1     Spec(K_n) = {2i sin(2*pi*k/n) : k = 0, ..., n-1}
    Theorem 6.2   Multiplicity-(1,1,1) holds only at n = 3
    Section 6.5   Structural identities (sphere, bridge, continuous rank)
"""

from __future__ import annotations

import numpy as np

from nct8_clifford import (
    cyclic_generator,
    spectrum_K_n_residual,
    multiplicity_111_check,
    sphere_identity_residual,
    bridge_identity_residual,
    continuous_rank,
    structural_identities,
)


# ---------------------------------------------------------------------
# Cyclic generator structure
# ---------------------------------------------------------------------

def test_K_n_is_antisymmetric():
    for n in [2, 3, 4, 5, 6, 7]:
        K = cyclic_generator(n)
        assert np.allclose(K, -K.T), f"K_{n} is not antisymmetric"


def test_K_3_equals_sqrt3_times_J():
    """K_3 should equal sqrt(3) * J where J is the normalized cyclic generator."""
    K3 = cyclic_generator(3)
    expected = np.array([
        [0, -1,  1],
        [1,  0, -1],
        [-1, 1,  0],
    ], dtype=float)
    assert np.allclose(K3, expected)


# ---------------------------------------------------------------------
# Lemma 6.1: spectrum of K_n
# ---------------------------------------------------------------------

def test_lemma_6_1_K_n_spectrum_for_n_3():
    """Spec(K_3) = {0, +i*sqrt(3), -i*sqrt(3)}."""
    assert spectrum_K_n_residual(3) < 1e-10


def test_lemma_6_1_K_n_spectrum_for_n_4():
    """Spec(K_4) = {0, 0, +2i, -2i}."""
    assert spectrum_K_n_residual(4) < 1e-10


def test_lemma_6_1_K_n_spectrum_for_n_5():
    """Spec(K_5) = {0, +/-i*sqrt((5+sqrt(5))/2), +/-i*sqrt((5-sqrt(5))/2)}."""
    assert spectrum_K_n_residual(5) < 1e-10


def test_lemma_6_1_K_n_spectrum_for_n_6_and_7():
    assert spectrum_K_n_residual(6) < 1e-10
    assert spectrum_K_n_residual(7) < 1e-10


# ---------------------------------------------------------------------
# Theorem 6.2: multiplicity-(1,1,1) is unique to n = 3
# ---------------------------------------------------------------------

def test_theorem_6_2_n_equals_3_has_111_structure():
    """At n = 3, the spectrum of K_n has the form {-c, 0, +c} each with mult 1."""
    result = multiplicity_111_check(3)
    assert result["zero_multiplicity"] == 1
    assert result["distinct_pos_pairs"] == 1
    assert result["has_111_structure"] is True


def test_theorem_6_2_n_equals_2_fails():
    """K_2 has no zero eigenvalue (Spec = {+/-i})."""
    result = multiplicity_111_check(2)
    assert result["zero_multiplicity"] == 0
    assert result["has_111_structure"] is False


def test_theorem_6_2_n_equals_4_fails_via_doubled_zero():
    """At n = 4, the zero eigenvalue has multiplicity 2 (sin(0) = sin(pi) = 0)."""
    result = multiplicity_111_check(4)
    assert result["zero_multiplicity"] == 2
    assert result["has_111_structure"] is False


def test_theorem_6_2_n_equals_5_fails_via_extra_pair():
    """At n = 5, there are two distinct nonzero conjugate pairs."""
    result = multiplicity_111_check(5)
    assert result["zero_multiplicity"] == 1
    assert result["distinct_pos_pairs"] == 2
    assert result["has_111_structure"] is False


def test_theorem_6_2_uniqueness_across_small_n():
    """Sweep n = 2..9; only n = 3 should have the (1,1,1) structure."""
    successes = [n for n in range(2, 10)
                 if multiplicity_111_check(n)["has_111_structure"]]
    assert successes == [3]


# ---------------------------------------------------------------------
# Section 6.5: structural identities pinning n = 3
# ---------------------------------------------------------------------

def test_sphere_identity_holds_exactly():
    """Omega^2 + mu^2 = 1 is exact by definition."""
    assert sphere_identity_residual() < 1e-12


def test_bridge_identity_holds_to_sub_percent():
    """4*beta = Omega holds within ~5e-4 at canonical values (not exact)."""
    res = bridge_identity_residual()
    assert 1e-5 < res < 1e-2


def test_continuous_rank_is_close_to_3():
    """x*(mu) = 1/(phi*Omega - 1) should be ~3.006 at canonical values."""
    x_star = continuous_rank()
    assert 3.0 < x_star < 3.02


def test_structural_identities_summary():
    """The structural_identities() summary should report all three diagnostics."""
    s = structural_identities()
    assert "sphere (Omega^2 + mu^2)" in s
    assert "bridge (4*beta/Omega)" in s
    assert "continuous rank x*(mu)" in s
    sphere_val, sphere_target, sphere_err = s["sphere (Omega^2 + mu^2)"]
    assert sphere_target == 1.0
    assert sphere_err < 1e-12

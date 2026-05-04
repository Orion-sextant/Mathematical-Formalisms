"""Tests for canonical_data: Theta_can, Pfaffian, K_0 trace-image generators.

Maps to:
    Theorem 3.1   Pfaffian closed form |Pf(Theta_can)| = mu * Omega * (Omega^2 - beta^2)
    Section 3.2   Trace-image generators of K_0
"""

from __future__ import annotations

import numpy as np

from nct8_clifford import (
    mu, Omega, beta, J,
    construct_theta_canonical,
    pfaffian,
    trace_image_generators,
    analytical_pfaffian_matchings,
)


# ---------------------------------------------------------------------
# Constants and J
# ---------------------------------------------------------------------

def test_mu_is_lambert_w_fixed_point():
    """mu = W(1) should satisfy mu = exp(-mu) (defining equation)."""
    assert abs(mu - float(np.exp(-mu))) < 1e-12


def test_omega_is_spinor_complement():
    """Omega^2 + mu^2 = 1."""
    assert abs(Omega ** 2 + mu ** 2 - 1.0) < 1e-12


def test_J_is_antisymmetric_with_unit_spectrum():
    """J should be antisymmetric with eigenvalues {0, +i, -i}."""
    assert np.allclose(J, -J.T)
    eigs = sorted(np.linalg.eigvals(J), key=lambda z: z.imag)
    assert abs(eigs[0] - (-1j)) < 1e-10
    assert abs(eigs[1].imag) < 1e-10
    assert abs(eigs[2] - (1j)) < 1e-10


# ---------------------------------------------------------------------
# Theta_can structural properties
# ---------------------------------------------------------------------

def test_theta_can_is_antisymmetric():
    Theta = construct_theta_canonical()
    assert np.allclose(Theta, -Theta.T)


def test_theta_can_is_8x8():
    Theta = construct_theta_canonical()
    assert Theta.shape == (8, 8)


def test_theta_can_block_decoupling():
    """The (0, 7) block should be decoupled from indices 1..6."""
    Theta = construct_theta_canonical()
    assert np.allclose(Theta[0, 1:7], 0.0)
    assert np.allclose(Theta[7, 1:7], 0.0)
    assert abs(Theta[0, 7] - mu) < 1e-12


# ---------------------------------------------------------------------
# Theorem 3.1: Pfaffian closed form
# ---------------------------------------------------------------------

def test_theorem_3_1_pfaffian_closed_form():
    """Theorem 3.1: |Pf(Theta_can)| = mu * Omega * (Omega^2 - beta^2)."""
    Theta = construct_theta_canonical()
    pf_numerical = pfaffian(Theta)
    pf_closed_form = mu * Omega * (Omega ** 2 - beta ** 2)
    assert abs(abs(pf_numerical) - pf_closed_form) < 1e-10


def test_pfaffian_squared_equals_determinant():
    """Pf^2 = det for any antisymmetric matrix."""
    Theta = construct_theta_canonical()
    pf = pfaffian(Theta)
    det = float(np.linalg.det(Theta))
    assert abs(pf ** 2 - det) < 1e-10


def test_analytical_four_matching_expansion():
    """The four-matching analytical expansion should reproduce Pf(Theta_can)."""
    Theta = construct_theta_canonical()
    pf_numerical = pfaffian(Theta)
    pf_analytical, _ = analytical_pfaffian_matchings()
    assert abs(pf_numerical - pf_analytical) < 1e-10


# ---------------------------------------------------------------------
# Section 3.2: trace-image generators
# ---------------------------------------------------------------------

def test_trace_image_generators_at_size_2():
    """At |S| = 2, the distinct |Pf| values should be {mu, Omega, beta/sqrt(3)}."""
    Theta = construct_theta_canonical()
    gens = trace_image_generators(Theta)
    expected = sorted([mu, Omega, beta / np.sqrt(3.0)], reverse=True)
    assert len(gens[2]) == 3
    for g, e in zip(gens[2], expected):
        assert abs(g - e) < 1e-10


def test_trace_image_generators_at_size_8():
    """At |S| = 8, the unique value is |Pf(Theta_can)| = mu*Omega*(Omega^2-beta^2)."""
    Theta = construct_theta_canonical()
    gens = trace_image_generators(Theta)
    expected = mu * Omega * (Omega ** 2 - beta ** 2)
    assert len(gens[8]) == 1
    assert abs(gens[8][0] - expected) < 1e-10


def test_trace_image_generators_size_4_count():
    """At |S| = 4, there should be exactly 5 distinct |Pf| values."""
    Theta = construct_theta_canonical()
    gens = trace_image_generators(Theta)
    assert len(gens[4]) == 5


def test_trace_image_generators_size_6_count():
    """At |S| = 6, there should be exactly 4 distinct |Pf| values."""
    Theta = construct_theta_canonical()
    gens = trace_image_generators(Theta)
    assert len(gens[6]) == 4

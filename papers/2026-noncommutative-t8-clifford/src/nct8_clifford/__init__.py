"""nct8_clifford: companion code for the paper

    Jared D. Dunahay, "A Canonical Non-Commutative Deformation of T^8
    Indexed by Cl(3,0): Spectrum, Pfaffian, and a Pythagorean Spectral
    Identity" (2026).

The package is organized along the dependency layers of the paper:

    canonical_data    Theta_can construction; J generator; Pfaffian;
                      trace-image generators of K_0.
    identities        Spectrum (Thm 2.3), Pfaffian closed form (Thm 3.1),
                      Frobenius decomposition (Thm 3.3), Pythagorean
                      spectral identity (Thm 4.2), Lambert-W localization
                      (Cor 5.2).
    dimension_check   Cl(n,0) dimension specificity (section 6): cyclic
                      generator K_n, spectrum (Lemma 6.1), multiplicity-
                      (1,1,1) uniqueness (Thm 6.2), structural identities.
"""

__version__ = "1.0.0"

from .canonical_data import (
    mu, Omega, beta, phi, J,
    construct_theta_canonical,
    pfaffian,
    k_theory_spectrum,
    trace_image_generators,
    analytical_pfaffian_matchings,
)

from .identities import (
    spectrum_imaginary_parts,
    spectrum_residual,
    pfaffian_closed_form,
    pfaffian_residual,
    frobenius_norm_squared_closed_form,
    frobenius_residual,
    pythagorean_residual,
    pythagorean_value_at_canonical_coupling,
    dirac_magnitude_block_07,
    lambert_w_localization_residual,
)

from .dimension_check import (
    cyclic_shift,
    cyclic_generator,
    spectrum_K_n,
    spectrum_K_n_predicted,
    spectrum_K_n_residual,
    multiplicity_111_check,
    sphere_identity_residual,
    bridge_identity_residual,
    continuous_rank,
    structural_identities,
)

__all__ = [
    "mu", "Omega", "beta", "phi", "J",
    "construct_theta_canonical", "pfaffian",
    "k_theory_spectrum", "trace_image_generators",
    "analytical_pfaffian_matchings",
    "spectrum_imaginary_parts", "spectrum_residual",
    "pfaffian_closed_form", "pfaffian_residual",
    "frobenius_norm_squared_closed_form", "frobenius_residual",
    "pythagorean_residual", "pythagorean_value_at_canonical_coupling",
    "dirac_magnitude_block_07", "lambert_w_localization_residual",
    "cyclic_shift", "cyclic_generator",
    "spectrum_K_n", "spectrum_K_n_predicted", "spectrum_K_n_residual",
    "multiplicity_111_check",
    "sphere_identity_residual", "bridge_identity_residual",
    "continuous_rank", "structural_identities",
]

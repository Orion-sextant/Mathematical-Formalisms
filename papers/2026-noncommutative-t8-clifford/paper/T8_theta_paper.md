# A Canonical Non-Commutative Deformation of T⁸ Indexed by Cl(3,0)

## Spectrum, Pfaffian, and a Pythagorean Spectral Identity

**Jared D. Dunahay**
*AEO Trivector LLC, Bedford, NH*
ORCID: [0009-0004-5735-2872](https://orcid.org/0009-0004-5735-2872)

**Abstract.** We construct a canonical antisymmetric matrix $\Theta_{\mathrm{can}} \in \mathfrak{so}(8)$ on the 8-torus, indexed by the four Clifford grades of $\mathrm{Cl}(3,0)$ and parameterized by three real constants $(\mu, \Omega, \beta)$ with $\mu = W(1)$ the Lambert-W fixed point, $\Omega = \sqrt{1-\mu^2}$, and $\beta = \varphi^{-1}/3$. The associated noncommutative torus $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$ — viewed as a Rieffel deformation of $\mathbb{T}^8$ with structured parameter $\Theta_{\mathrm{can}}$ — admits the following closed-form structural data. **(i)** The spectrum factorizes as $\mathrm{Spec}(\Theta_{\mathrm{can}}) = \{\pm i\mu, \pm i\Omega, \pm i(\Omega \pm \beta)\}$, with the $(0,7)$-block decoupling from the 6-dimensional middle block. **(ii)** The Pfaffian satisfies $|\mathrm{Pf}(\Theta_{\mathrm{can}})| = \mu\Omega(\Omega^2 - \beta^2)$; the Frobenius norm decomposes as $\|\Theta_{\mathrm{can}}\|^2 = 2\mu^2 + 6\Omega^2 + 4\beta^2$; the trace-image generators of $K_0$ are polynomials in $(\mu, \Omega, \beta)$ giving a dense subgroup of $\mathbb{R}$. **(iii)** The three grade-cross-pairing frequencies $(\Omega - \beta, \Omega, \Omega + \beta)$ satisfy the algebraic identity $\nu_-^2 + \nu_0^2 - \nu_+^2 = \Omega(\Omega - 4\beta)$, vanishing exactly when $4\beta = \Omega$ and producing a $3:4:5$ Pythagorean ratio at that point. At the chosen canonical values, this identity holds to within $5 \times 10^{-4}$ but is not exact; three candidate derivations of $4\beta = \Omega$ are tested and rejected. **(iv)** The Hermitian operator $\hat{D} := |i\Theta_{\mathrm{can}}|$ satisfies $\hat{D}^2 = \hat{D}\cdot e^{-\hat{D}}$ on the 2-dimensional $(0,7)$-block; this is a localization of the Lambert-W fixed-point equation to a specific invariant subspace. **(v)** The minimal-channel Pythagorean structure — three grade-cross-pairing frequencies in multiplicity-$(1,1,1)$ at the canonical coupling $4\beta = \Omega$ — is unique to dimension 3 in the family of analogous nearest-neighbor constructions on $\mathrm{Cl}(n, 0)$: explicit characteristic-polynomial computation shows that the prerequisite spectrum $\{0, \pm ic\}$ of the nearest-neighbor cyclic-shift generator $K_n$ is realized with multiplicity $(1,1,1)$ only at $n = 3$. All claims are verified numerically (39 unit tests) and the load-bearing identities are independently re-derived symbolically in SymPy.

**Keywords:** noncommutative torus, Rieffel deformation, Lambert-W function, Clifford algebra, Pfaffian.
**MSC2020:** 46L87 (primary), 15A66, 47A10, 58B34.

---

## 1. Introduction

The non-commutative tori of Rieffel \[2\] form a rich family of C*-algebras whose K-theory and spectral geometry are governed by an antisymmetric deformation matrix $\Theta$ (see also Connes \[1\] for the broader noncommutative-geometric framework). They arise as a special case of Rieffel's deformation quantization for actions of $\mathbb{R}^d$ \[RIE93\], and admit a natural extension to spectral triples carrying torus actions via Connes–Landi isospectral deformations \[CL\] and Yamashita's framework \[YAM\]. In all of these constructions, the K-theory of the deformed algebra is naturally isomorphic to that of the undeformed one; the deformation parameter $\Theta$ enters only through the *image* of the K-theory under the canonical trace, which generically becomes a dense subgroup of $\mathbb{R}$.

While the case of generic irrational $\Theta$ is well studied, **specific structured choices** — those whose entries are algebraically related to canonical mathematical constants — have received less attention. In this paper we study one such case in detail: an 8-dimensional non-commutative torus $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$ where the deformation matrix is indexed by the four Clifford grades of $\mathrm{Cl}(3,0)$ and parameterized by three real constants drawn from independent sources: the Lambert-W fixed point $\mu = W(1)$, the spinor complement $\Omega = \sqrt{1-\mu^2}$, and the inverse-golden-third $\beta = \varphi^{-1}/3$.

The construction has three motivations.

**(M1) Closed-form spectral data.** Spectral computations on noncommutative tori are typically abstract. We exhibit a structured $\Theta_{\mathrm{can}}$ whose spectrum, Pfaffian, Frobenius norm, and trace-image generators all admit clean closed forms in terms of $(\mu, \Omega, \beta)$. Combined with the Yamashita/Rieffel framework, this gives an explicit worked example of how K-theoretic invariants of the deformation depend on a structured parameter family.

**(M2) An exact Pythagorean spectral identity.** The four characteristic frequencies of $\Theta_{\mathrm{can}}$ produce an algebraic Pythagorean identity: three of them stand in ratio $3:4:5$ exactly when $4\beta = \Omega$. We make this precise (Theorem 4.2) and show that the canonical values place us within $5 \times 10^{-4}$ of this configuration without exactly realizing it.

**(M3) A localization of the Lambert-W fixed point.** We show (Corollary 5.2) that the eigenvalue $\mu = W(1)$ of the natural Dirac-magnitude operator $\hat{D} = |i\Theta_{\mathrm{can}}|$ is confined to a specific 2-dimensional invariant subspace of $\hat{D}$, where the equation $\hat{D}^2 = \hat{D}\,e^{-\hat{D}}$ holds and is equivalent to the defining equation of $W(1)$. This is a *localization*, not an independent derivation of $W(1)$; the content is in the precise subspace of $\hat{D}$ to which $W(1)$ is confined. A different operator-algebraic appearance of $W(1)$ on noncommutative tori, in connection with Drinfeld modules and class field theory, is given by Nikolaev \[NIK\]; the two are not in direct correspondence.

**Relation to prior work.** The construction is a special case of Rieffel deformation \[RIE93\] for the $\mathbb{R}^8$-action by translations on $\mathbb{T}^8$, with the specific structured matrix $\Theta_{\mathrm{can}}$ in place of a generic skew-symmetric deformation parameter. The Yamashita framework \[YAM\] gives K-theoretic invariance of the deformation; we exhibit the explicit trace-image generators as polynomials in $(\mu, \Omega, \beta)$. Clifford structures have appeared elsewhere in noncommutative geometry, notably in the almost-commutative geometry of the Standard Model \[KL\], but as parts of the finite spectral triple rather than as a grade-indexing scheme on a torus deformation. To our knowledge no prior construction combines Clifford-grade indexing with a structured parameter family on a noncommutative torus.

This paper is purely mathematical. Possible physical or computational interpretations are deferred to separate work.

### Outline

Section 2 introduces the canonical $\Theta_{\mathrm{can}}$ and proves the spectrum theorem (Theorem 2.3). Section 3 establishes Pfaffian and Frobenius closed forms (Theorems 3.1, 3.3) and exhibits the trace-image generators of $K_0$. Section 4 proves the Pythagorean spectral identity (Theorem 4.2) and reports negative results on candidate derivations of the bridge $4\beta = \Omega$. Section 5 introduces the Dirac-magnitude operator $\hat{D}$ and the Lambert-W localization (Corollary 5.2), then describes an even/odd splitting $\Theta_{\mathrm{can}} = \Theta_{\mathrm{swap}} + \Theta_{\mathrm{pres}}$ with degeneracy-lifting structure. Section 6 proves the dimension specificity of the minimal-channel Pythagorean prerequisite to the nearest-neighbor $\mathrm{Cl}(3,0)$ construction (Theorem 6.2, Corollary 6.3). Section 7 concludes with open questions.

---

## 2. The canonical deformation matrix

### 2.1 Setup

Let
$$\mu := W(1), \qquad \varphi := \tfrac{1+\sqrt{5}}{2}, \qquad \Omega := \sqrt{1 - \mu^2}, \qquad \beta := \varphi^{-1}/3.$$

Numerically, $\mu \approx 0.5671$, $\Omega \approx 0.8236$, $\beta \approx 0.2060$. The constraint $\mu^2 + \Omega^2 = 1$ holds by definition; the additional approximate identity $4\beta \approx \Omega$ holds to within 0.05% but is not exact. The role of these specific parameter choices is structural rather than fundamental: $\mu$ is a transcendental fixed-point constant, $\Omega$ its spinor complement, and $\beta$ a small parameter of independent algebraic origin.

Let $J \in \mathfrak{so}(3)$ be the cyclic-symmetric antisymmetric matrix
$$J := \frac{1}{\sqrt{3}}\begin{pmatrix} 0 & -1 & 1 \\ 1 & 0 & -1 \\ -1 & 1 & 0 \end{pmatrix},$$
the unique (up to sign) cyclic-invariant rank-2 antisymmetric $3 \times 3$ matrix. The unnormalized cyclic-shift form $K_3 = \sqrt{3}\,J$ has characteristic polynomial $\lambda(\lambda^2 + 3) = 0$ and spectrum $\{0, \pm i\sqrt{3}\}$; the $1/\sqrt{3}$ normalization in $J$ then gives $\mathrm{Spec}(J) = \{0, \pm i\}$. Geometrically, $J$ is the generator of rotation around the diagonal axis $(1,1,1)/\sqrt{3} \in \mathbb{R}^3$.

We index the basis of $\mathbb{R}^8$ by the multiindices of Cl(3,0):
$$(0; 1, 2, 3; 23, 13, 12; I)$$
corresponding to grades 0, 1, 2, 3 with dimensions (1, 3, 3, 1) respectively.

### 2.2 Definition

**Definition 2.1.** The *canonical deformation matrix* $\Theta_{\mathrm{can}} \in \mathfrak{so}(8)$ is determined by the upper-triangular entries:
$$\Theta_{\mathrm{can}}[0, 7] = \mu,$$
$$\Theta_{\mathrm{can}}[i, i+3] = \Omega \quad \text{for } i = 1, 2, 3,$$
$$\Theta_{\mathrm{can}}[1{:}4, 1{:}4] = \beta\, J,\qquad \Theta_{\mathrm{can}}[4{:}7, 4{:}7] = \beta\, J,$$
with all other upper-triangular entries zero, and is then antisymmetrized.

The associated *non-commutative torus* $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$ is the universal C*-algebra generated by 8 unitaries $U_0, \ldots, U_7$ satisfying $U_i U_j = e^{2\pi i \Theta_{ij}}\, U_j U_i$.

**Remark 2.2** (graded uniform intertwiner). The cross-pairing $\Theta[i, i+3] = \Omega$ couples grade-1 to grade-2 generators uniformly along the basis-aligned indices. **This is structurally distinct from the Hodge star ★ on Cl(3,0)**, which acts with alternating signs $\star(e_1) = +e_{23}$, $\star(e_2) = -e_{13}$, $\star(e_3) = +e_{12}$. Throughout this paper, "graded uniform intertwiner" or "diagonal cross-pairing" refers to the construction in Definition 2.1.

### 2.3 Spectrum theorem

**Theorem 2.3** (Spectrum). *The eigenvalues of $\Theta_{\mathrm{can}}$ are*
$$\mathrm{Spec}(\Theta_{\mathrm{can}}) = \{\pm i\mu,\ \pm i\Omega,\ \pm i(\Omega - \beta),\ \pm i(\Omega + \beta)\}.$$

*Proof.* The (0, 7) entry decouples a 2×2 block contributing $\pm i\mu$. The remaining 6×6 block has the form $M = \begin{pmatrix} \beta J & \Omega I_3 \\ -\Omega I_3 & \beta J \end{pmatrix}$. Using the eigendecomposition of $J$ (eigenvalues $0, \pm i$), this block decomposes into three 2×2 sub-blocks, one for each $J$-eigenvector, with eigenvalues $i(\beta\sigma \pm \Omega)$ for $\sigma \in \{0, \pm 1\}$. The three values of $\sigma$ yield $\pm i\Omega$, $\pm i(\Omega - \beta)$, $\pm i(\Omega + \beta)$. ∎

We verified the theorem symbolically: the characteristic polynomial of $\Theta_{\mathrm{can}}$ in sympy factors exactly as
$$\det(\lambda I - \Theta_{\mathrm{can}}) = (\lambda^2 + \mu^2)(\lambda^2 + \Omega^2)(\lambda^2 + (\Omega-\beta)^2)(\lambda^2 + (\Omega+\beta)^2).$$

**Remark 2.4** (block decoupling). The (0, 7) block of $\Theta_{\mathrm{can}}$ has zero entries to all other indices. In the Cl(3,0) grade basis, the 2-dimensional (grade 0, grade 3) subspace and the 6-dimensional (grade 1, grade 2) subspace are spectrally and algebraically orthogonal. This is a coordinate-dependent statement: the privileged basis is the one that diagonalizes the Cl(3,0) grade operator.

---

## 3. Pfaffian and Frobenius closed forms

### 3.1 Pfaffian

**Theorem 3.1** (Pfaffian closed form). *The Pfaffian of $\Theta_{\mathrm{can}}$ has absolute value*
$$|\mathrm{Pf}(\Theta_{\mathrm{can}})| = \mu \cdot \Omega \cdot (\Omega - \beta)(\Omega + \beta) = \mu\,\Omega\,(\Omega^2 - \beta^2).$$

*Proof.* By Theorem 2.3, $\det(\Theta_{\mathrm{can}}) = \mu^2 \Omega^2 (\Omega-\beta)^2 (\Omega+\beta)^2$. Since $\mathrm{Pf}^2 = \det$, the result follows. ∎

### 3.2 Trace-image generators

Following Elliott–Rieffel \[2, 3\] and Pimsner–Voiculescu \[6\], the K-theory of $\mathbb{T}^n_\Theta$ for irrational $\Theta$ is isomorphic to that of the underlying commutative torus, $K_0(C(\mathbb{T}^n_\Theta)) \cong \mathbb{Z}^{2^{n-1}}$, with the canonical tracial state $\tau$ inducing a homomorphism $\tau_* : K_0 \to \mathbb{R}$ whose image is generated by 1 and the Pfaffians of even-sized principal minors of $\Theta$.

For our $\Theta_{\mathrm{can}}$, direct computation of the Pfaffians of all $\binom{8}{2k}$ even-sized principal minors yields the following distinct nonzero generators (verified numerically and symbolically; closed forms re-derived in Appendix A):

| Subset size $2k$ | Number of distinct $\|\mathrm{Pf}\|$ values | Explicit closed forms |
|---|---|---|
| 2 | 3 | $\mu,\quad \Omega,\quad \beta/\sqrt{3}$ |
| 4 | 5 | $(\beta/\sqrt{3})^2,\quad \mu(\beta/\sqrt{3}),\quad \Omega(\beta/\sqrt{3}),\quad \mu\Omega,\quad \Omega^2 - \beta^2/3$ |
| 6 | 4 | $\mu(\beta/\sqrt{3})^2,\quad \mu\Omega(\beta/\sqrt{3}),\quad \mu(\Omega^2 - \beta^2/3),\quad \Omega(\Omega^2 - \beta^2)$ |
| 8 | 1 | $\mu\Omega(\Omega^2 - \beta^2)$ |

Each generator is a polynomial in $\mu, \Omega, \beta$ with rational coefficients (the $1/\sqrt{3}$ factors arise from the normalization of $J$ in Definition 2.1 and appear consistently as powers of $\beta/\sqrt{3}$). The full numerical verification at $\mu = W(1)$, $\Omega = \sqrt{1 - \mu^2}$, $\beta = \varphi^{-1}/3$ matches the closed forms to floating-point precision (Appendix A).

Since $\mu = W(1)$ is transcendental — by Lindemann's theorem applied to the equation $\mu e^\mu = 1$ (if $\mu$ were nonzero algebraic, $e^\mu$ would be transcendental, contradicting $e^\mu = 1/\mu$) \[5\] — while $\Omega = \sqrt{1-\mu^2}$ is algebraic of degree 2 over $\mathbb{Q}(\mu)$ and $\beta = \varphi^{-1}/3$ is algebraic of degree 2 over $\mathbb{Q}$, the nonzero entries $\mu$, $\Omega$, $\pm\beta/\sqrt{3}$ of $\Theta_{\mathrm{can}}$ are all irrational. Under the convention $U_i U_j = e^{2\pi i \Theta_{ij}} U_j U_i$ of Definition 2.1, this implies that no nonzero entry $\Theta_{ij}$ is an integer, so the bicharacter $b_\Theta(x, y) = e^{2\pi i \langle x, \Theta y\rangle}$ on $\mathbb{Z}^8$ is non-trivial. Consequently the rotation algebra $C(\mathbb{T}^8_{\Theta_{\mathrm{can}}})$ is unital and nuclear. Since $\mu \in \tau_*(K_0)$ is irrational, the subgroup $\mathbb{Z} + \mu\mathbb{Z} \subseteq \tau_*(K_0)$ is dense in $\mathbb{R}$; hence $\tau_*(K_0)$ is itself a dense subgroup of $\mathbb{R}$.

**Remark 3.2** (simplicity). Simplicity of $C(\mathbb{T}^n_\Theta)$ for $n \geq 3$ requires more than non-integrality of the individual entries $\Theta_{ij}$: by the standard criterion (cf. \[Phi06\]), it is equivalent to non-degeneracy of the bicharacter $b_\Theta$ on $\mathbb{Z}^n$, i.e., the absence of any nonzero $v \in \mathbb{Z}^n$ such that $\Theta v \in \mathbb{Z}^n$. We expect this condition to hold for $\Theta_{\mathrm{can}}$ given the transcendence of $\mu$, but a complete verification — requiring rational independence of $\{1, \mu, \Omega, \beta/\sqrt{3}\}$ over $\mathbb{Q}$ — is beyond the scope of this paper. The structural results below (Theorems 2.3, 3.1, 3.3, 4.2, 5.1, 6.2) are independent of the simplicity question.

### 3.3 Frobenius norm

**Theorem 3.3** (Frobenius decomposition). 
$$\|\Theta_{\mathrm{can}}\|^2 := \mathrm{Tr}(\Theta_{\mathrm{can}}^\top \Theta_{\mathrm{can}}) = 2\mu^2 + 6\Omega^2 + 4\beta^2.$$
*Each off-diagonal entry of an antisymmetric matrix contributes its square twice to the Frobenius norm (once via the upper triangle, once via the lower). Counting:*

- *the single $(0, 7)$ edge contributes $2 \mu^2$;*
- *the three grade-cross-pairings $(i, i+3)$ for $i = 1, 2, 3$ each contribute $2 \Omega^2$, total $6\Omega^2$;*
- *each $\beta J$ block has six nonzero off-diagonal entries with values $\pm \beta/\sqrt{3}$, contributing $6 \cdot (\beta/\sqrt{3})^2 = 2\beta^2$; the two blocks together contribute $4\beta^2$.*

*Proof.* Direct summation. ∎

---

## 4. Pythagorean spectral identity

### 4.1 The three grade-cross-pairing frequencies

By Theorem 2.3, the spectrum of $\Theta_{\mathrm{can}}$ has four characteristic positive imaginary values: $\mu$ from the $(0,7)$ block, and $\Omega$, $\Omega \pm \beta$ from the 6-dimensional middle block carrying the $\mathrm{grade}\,1 \leftrightarrow \mathrm{grade}\,2$ cross-pairing. Define the three latter values
$$\nu_- := \Omega - \beta,\qquad \nu_0 := \Omega,\qquad \nu_+ := \Omega + \beta.$$
We refer to these as the *grade-cross-pairing frequencies*; they are not Hodge-derived in the geometric sense (Remark 2.2).

### 4.2 Theorem

**Theorem 4.2** (Pythagorean identity). 
$$\nu_-^2 + \nu_0^2 - \nu_+^2 = \Omega(\Omega - 4\beta).$$
*In particular, $\nu_-^2 + \nu_0^2 = \nu_+^2$ if and only if $4\beta = \Omega$. At this configuration, the three frequencies stand in ratio $3 : 4 : 5$.*

*Proof.* 
$$\nu_-^2 + \nu_0^2 - \nu_+^2 = (\Omega-\beta)^2 + \Omega^2 - (\Omega+\beta)^2 = \Omega^2 - 4\Omega\beta = \Omega(\Omega - 4\beta).$$
At $\beta = \Omega/4$, the three frequencies become $\frac{3\Omega}{4}, \frac{4\Omega}{4}, \frac{5\Omega}{4}$, in ratio $3:4:5$. ∎

**Remark 4.3** (status at axiom values). At $\beta = \varphi^{-1}/3$ and $\Omega = \sqrt{1 - W(1)^2}$, we have $4\beta/\Omega = 1.000517$, so the Pythagorean identity holds to within 0.05% but **not exactly**. We do not claim that $4\beta = \Omega$ is forced by any natural condition on $\Theta_{\mathrm{can}}$. Specifically, three candidate derivations were tested computationally and rejected:

(a) *Pfaffian-constrained extremum.* Extremizing $\|\Theta_{\mathrm{can}}\|^2 = 2\mu^2 + 6\Omega^2 + 4\beta^2$ subject to fixed $|\mathrm{Pf}(\Theta_{\mathrm{can}})|$ yields the Lagrange condition $\beta^2 = 6\Omega^2$, i.e., $\beta = \Omega\sqrt{6} \neq \Omega/4$.

(b) *Topological-charge equality.* Five natural conditions equating Pfaffians of complementary subblocks (or of grade-block fluxes) were tested; none yields $4\beta = \Omega$ as solution.

(c) *$\mathrm{Spin}(7)$ self-duality.* The projection of $\Theta_{\mathrm{can}}$ onto the 7-dimensional irreducible representation $\Lambda^2_7 \subset \Lambda^2 \mathbb{R}^8$ under either of two natural Cayley-form conventions does not vanish for any value of $\beta$.

We report these as negative results. The relation between the canonical values $(\mu, \Omega, \beta)$ and the Pythagorean point $\beta = \Omega/4$ remains an open question in this paper; we do not claim it is algebraically forbidden, merely that we have not found a natural mechanism that selects it.

---

## 5. The Dirac-magnitude operator and the Lambert-W localization

### 5.1 Definition

Since $\Theta_{\mathrm{can}}$ is real antisymmetric, $i \Theta_{\mathrm{can}}$ is Hermitian. Define
$$\hat{D} := |i\,\Theta_{\mathrm{can}}|$$
via the spectral decomposition: writing $i\Theta_{\mathrm{can}} = V \Lambda V^*$, we set $\hat{D} := V |\Lambda| V^*$.

**Lemma 5.1** (Properties of $\hat{D}$). *$\hat{D}$ is Hermitian, positive semi-definite, and satisfies*
$$\hat{D}^2 = -\Theta_{\mathrm{can}}^2,\qquad \mathrm{Tr}(\hat{D}^2) = \|\Theta_{\mathrm{can}}\|^2,$$
$$\mathrm{Spec}(\hat{D}) = \{\mu, \Omega-\beta, \Omega, \Omega+\beta\}\text{ each with multiplicity 2}.$$

The operator $\hat{D}$ is the natural Dirac-magnitude operator associated with the deformation matrix $\Theta_{\mathrm{can}}$. It is not a Dirac operator in the strict sense (it is positive semi-definite rather than self-adjoint with symmetric spectrum), but $\hat{D}^2$ recovers $-\Theta_{\mathrm{can}}^2$ and its trace identities reproduce the Frobenius decomposition of Theorem 3.3 and the spectral content of Theorem 2.3.

### 5.2 Lambert-W localization on the (scalar, pseudoscalar) block

**Corollary 5.2** (Lambert-W localization). *Restricted to the 2-dimensional invariant subspace $V_0 := \mathrm{span}(e_0, e_7)$, the operator $\hat{D}$ satisfies*
$$\hat{D}\big|_{V_0} = \mu \cdot I_2 \qquad \text{and} \qquad \hat{D}^2\big|_{V_0} = \hat{D} \cdot e^{-\hat{D}}\big|_{V_0}. \quad (\star)$$
*The eigenvalue $\mu$ on $V_0$ is the unique nonzero positive real solution of $\lambda = e^{-\lambda}$, namely $W(1)$.*

*Proof.* By Theorem 2.3, $\hat{D}|_{V_0} = \mu \cdot I_2$. Thus $\hat{D}^2|_{V_0} = \mu^2 I_2$ and $\hat{D}\cdot e^{-\hat{D}}|_{V_0} = \mu e^{-\mu} I_2$. These are equal because $\mu = W(1)$ satisfies $\mu = e^{-\mu}$, hence $\mu^2 = \mu e^{-\mu}$. The unique nonzero positive real solution of $\lambda^2 = \lambda e^{-\lambda}$, equivalently $\lambda = e^{-\lambda}$, is $\lambda = W(1)$. ∎

**Remark 5.3** (status of the corollary). Corollary 5.2 is a structural reformulation, not a derivation. It records that the constant $\mu = W(1)$ used in Definition 2.1 to construct $\Theta_{\mathrm{can}}$ appears as an eigenvalue of $\hat{D}$ on a specific 2-dimensional invariant subspace decoupled from the 6-dimensional grade-cross-pairing block, and that the eigenvalue equation on this block is equivalent to the defining equation of $W(1)$. The content is in the **localization** — that $W(1)$ appears specifically on the $(0, 7)$-block and not elsewhere — rather than in any independent derivation of $W(1)$.

A genuinely operator-algebraic appearance of $W(1)$ in noncommutative-torus settings — distinct from the present construction — is given by Nikolaev \[NIK\] in connection with class field theory of Drinfeld modules. The two appearances are not in direct correspondence: ours is a localization of $W(1)$ to an invariant subspace of $\hat{D}$ on $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$; Nikolaev's involves fixed points of the function $e^{2\pi i\alpha + \log\log\varepsilon}$ associated with the period maps of Drinfeld modules.

### 5.3 Even/odd splitting and degeneracy-lifting structure

The matrix $\Theta_{\mathrm{can}}$ admits a Frobenius-orthogonal decomposition
$$\Theta_{\mathrm{can}} = \Theta_{\mathrm{swap}} + \Theta_{\mathrm{pres}}$$
where $\Theta_{\mathrm{swap}}$ contains entries between the even-graded subspace $V_{\mathrm{even}} = \{e_0, e_4, e_5, e_6\}$ and odd-graded subspace $V_{\mathrm{odd}} = \{e_1, e_2, e_3, e_7\}$ (the (0,7)-block and the three grade-1↔grade-2 cross-pairings), and $\Theta_{\mathrm{pres}}$ contains intra-grade entries (the two $\beta J$ blocks). Numerically, $\|\Theta_{\mathrm{swap}}\|^2 / \|\Theta_{\mathrm{can}}\|^2 \approx 0.965$ and $\|\Theta_{\mathrm{pres}}\|^2 / \|\Theta_{\mathrm{can}}\|^2 \approx 0.035$.

**Proposition 5.4** (Splitting structure). *The spectrum of $\Theta_{\mathrm{swap}}$ consists of $\pm i\mu$ each with multiplicity $1$, and $\pm i\Omega$ each with multiplicity $3$. The perturbation $\Theta_{\mathrm{pres}} = \beta(J \oplus J)$ acting on the 6-dimensional grade-1⊕grade-2 subspace lifts the threefold degeneracy of $\pm i\Omega$ via the spectrum $\{0, \pm i\}$ of $J$, producing the triple $\pm i(\Omega - \beta), \pm i\Omega, \pm i(\Omega + \beta)$ each with multiplicity $1$.*

This decomposition is structurally analogous to fine-structure splitting of a degenerate atomic level: a small perturbation lifts a threefold degeneracy into a triplet. The $(3:4:5)$ Pythagorean ratio of Theorem 4.2 corresponds to the specific coupling strength $4\beta = \Omega$ at which this triplet of frequencies forms a Pythagorean triple. The atomic-physics analogy is descriptive, not literal: we use it because the algebraic pattern (a small additive perturbation lifting a degeneracy via a $\{-1, 0, +1\}$-spectrum operator) is identical to the fine-structure pattern, but we do not claim a representation-theoretic correspondence to atomic spin-orbit coupling.

---

## 6. Dimension specificity

### 6.1 The cyclic antisymmetric generator $K_n \in \mathfrak{so}(n)$

To make the analog of Definition 2.1 in dimension $n$ precise, we specify the cyclic-invariant antisymmetric matrix used in the intra-grade blocks. Let $C_n$ denote the cyclic shift permutation matrix on $\mathbb{R}^n$, characterized by $C_n e_i = e_{i+1 \bmod n}$ (equivalently, $(C_n)_{j,i} = 1$ iff $j \equiv i+1 \pmod n$). For $n \geq 3$, define the **nearest-neighbor cyclic-shift antisymmetrization**
$$K_n := C_n - C_n^{-1} \in \mathfrak{so}(n).$$
Explicitly,
$$(K_n)_{i,j} = \begin{cases} -1 & j \equiv i+1 \pmod{n}, \\ +1 & j \equiv i-1 \pmod{n}, \\ 0 & \text{otherwise}.\end{cases}$$
At $n = 3$ this gives
$$K_3 = \begin{pmatrix} 0 & -1 & +1 \\ +1 & 0 & -1 \\ -1 & +1 & 0 \end{pmatrix} = \sqrt{3}\, J,$$
where $J$ is the matrix of Definition 2.1, so $J = K_3/\sqrt{3}$ exactly under this convention.

For $n = 2$, the formula $C_n - C_n^{-1}$ is degenerate (since $C_2 = C_2^{-1}$). We adopt instead the standard symplectic generator
$$K_2 := \begin{pmatrix} 0 & -1 \\ 1 & \phantom{-}0 \end{pmatrix}$$
as the canonical antisymmetric generator on $\mathbb{R}^2$.

**Uniqueness scope.** $K_n$ is the *nearest-neighbor* cyclic-invariant antisymmetric generator. For $n \leq 4$, it spans the space of cyclic-invariant antisymmetric $n \times n$ matrices up to scalar. For $n \geq 5$, this space has dimension $\lfloor (n-1)/2 \rfloor$, with basis $\{C_n^r - C_n^{-r} : r = 1, \ldots, \lfloor (n-1)/2 \rfloor\}$. For example, at $n = 5$ both $K_5 = C_5 - C_5^{-1}$ and $C_5^2 - C_5^{-2}$ are nonzero cyclic-invariant antisymmetric generators with different spectra and are not scalar multiples of each other. We restrict throughout this paper to the nearest-neighbor generator $K_n$; the dimension-specificity statements of Theorem 6.2 and Corollary 6.3 are framed for this specific generator and do not assert anything about higher-step antisymmetrizations $C_n^r - C_n^{-r}$ with $r \geq 2$.

**Lemma 6.1.** *For $n \geq 3$, the eigenvalues of $K_n = C_n - C_n^{-1}$ are*
$$\mathrm{Spec}(K_n) = \{2i\sin(2\pi k/n) : k = 0, 1, \ldots, n-1\},$$
*and the characteristic polynomial is $\chi_n(\lambda) = \prod_{k=0}^{n-1}\big(\lambda - 2i\sin(2\pi k/n)\big)$.*

*Proof.* The eigenvalues of $C_n$ are the $n$-th roots of unity $\omega^k = e^{2\pi i k/n}$ for $k = 0, \ldots, n-1$. Since $C_n$ and $C_n^{-1}$ are simultaneously diagonalizable in the discrete Fourier basis, the eigenvalues of $K_n$ are $\omega^k - \omega^{-k} = 2i\sin(2\pi k/n)$. ∎

For $n \geq 3$, we work with $J^{(n)} := K_n / \nu_n$ where $\nu_n$ is a positive normalization constant; eigenvalue multiplicities are preserved under this rescaling. The specific generator used in Definition 2.1 is $J = J^{(3)} = K_3 / \sqrt{3}$, normalized so that $\mathrm{Spec}(J) = \{0, \pm i\}$. Since multiplication by a nonzero scalar preserves multiplicities, the multiplicity-$(1, 1, 1)$ structure of Theorem 6.2 below applies equally to $K_3$ and $J$.

### 6.2 Computation for small $n$

The cyclic-shift $K_n$ has the following characteristic polynomials and spectra (verified in SymPy):

| $n$ | char poly $\chi_n(\lambda)$ | spectrum of $K_n$ |
|---|---|---|
| 2 | $\lambda^2 + 1$ | $\{\pm i\}$ |
| 3 | $\lambda(\lambda^2 + 3)$ | $\{0,\ \pm i\sqrt{3}\}$ |
| 4 | $\lambda^2(\lambda^2 + 4)$ | $\{0,\ 0,\ \pm 2i\}$ |
| 5 | $\lambda(\lambda^4 + 5\lambda^2 + 5)$ | $\{0,\ \pm i\sqrt{(5\pm\sqrt{5})/2}\}$ |

For $n \geq 3$ the spectra follow directly from Lemma 6.1; the $n = 2$ entry uses the explicit definition $K_2 = \bigl(\begin{smallmatrix}0&-1\\1&\phantom{-}0\end{smallmatrix}\bigr)$ from §6.1.

### 6.3 The Pythagorean prerequisite

**Theorem 6.2** (Dimension uniqueness). *For every integer $n \geq 2$, the spectrum of $K_n$ contains a triplet $\{-c, 0, +c\}$ (with $c \neq 0$) in which each value occurs with multiplicity exactly $1$ if and only if $n = 3$. The same conclusion holds for any nonzero scalar multiple $J^{(n)} = K_n / \nu_n$ since normalization preserves eigenvalue multiplicities.*

*Proof.* We require $0 \in \mathrm{Spec}(K_n)$ with multiplicity exactly $1$, and exactly one nonzero conjugate pair $\pm ic$ each occurring with multiplicity $1$, with all remaining multiplicities zero.

**Case $n = 2$:** $K_2 = \begin{pmatrix} 0 & -1 \\ 1 & 0\end{pmatrix}$ has characteristic polynomial $\lambda^2 + 1$, so $\mathrm{Spec}(K_2) = \{\pm i\}$. No zero eigenvalue. Fails.

**Case $n \geq 3$:** Lemma 6.1 gives $\mathrm{Spec}(K_n) = \{2i\sin(2\pi k/n) : k = 0, \ldots, n-1\}$ as a multiset. Group by $k \mapsto n - k$ symmetry:

- *Multiplicity of $0$.* The value $\sin(2\pi k/n) = 0$ occurs precisely at $k = 0$ and (if $n$ is even) at $k = n/2$. Hence $0$ has multiplicity $1$ if $n$ is odd, and multiplicity $2$ if $n$ is even.

- *Number of distinct nonzero conjugate pairs.* For $n$ odd, the indices $\{1, \ldots, n-1\}$ partition into $(n-1)/2$ pairs $\{k, n-k\}$, each producing a conjugate pair $\pm 2i \sin(2\pi k/n)$. The values $\sin(2\pi k/n)$ for $k = 1, \ldots, (n-1)/2$ are *distinct* in absolute value (sine is strictly increasing on $[0, \pi/2]$ and strictly decreasing on $[\pi/2, \pi]$, with values mirrored across $\pi/2$; one checks no two indices $k_1 \neq k_2 \in \{1, \ldots, (n-1)/2\}$ give equal sine, since $2\pi k_1/n \neq \pi - 2\pi k_2/n$ holds whenever $k_1 + k_2 \neq n/2$, which is automatic for odd $n$). Hence there are exactly $(n-1)/2$ distinct nonzero conjugate pairs.

For the multiplicity-$(1,1,1)$ structure to hold, we need both $n$ odd and exactly one nonzero conjugate pair: $(n-1)/2 = 1$, i.e., $n = 3$. For even $n$ the zero eigenvalue has multiplicity $\geq 2$, immediate failure. For odd $n \geq 5$, the zero eigenvalue has multiplicity 1 but multiple distinct nonzero conjugate pairs appear.

Direct verification at $n = 3$: $\mathrm{Spec}(K_3) = \{0, +i\sqrt{3}, -i\sqrt{3}\}$, each with multiplicity $1$. ✓ ∎

### 6.4 Consequence for the Pythagorean identity

The minimal three-channel multiplicity-$(1,1,1)$ structure of Theorem 6.2 is the prerequisite for the specific construction in §2 (Definition 2.1) to produce a triplet of frequencies $(\Omega - \beta, \Omega, \Omega + \beta)$ with no extra channels and no doubled center. This in turn is what makes the Pythagorean identity of Theorem 4.2 a statement about *exactly three* grade-cross-pairing frequencies.

**Corollary 6.3.** *Let $n \geq 2$. Within the $\mathrm{Cl}(n,0)$-indexed construction of $\Theta^{(n)}_{\mathrm{can}}$ using the cyclic generator $K_n$ in the intra-grade blocks, only at $n = 3$ does the grade-cross-pairing spectrum reduce to a multiplicity-one triplet $(\Omega - c, \Omega, \Omega + c)$ admitting the Pythagorean identity $(\Omega - c)^2 + \Omega^2 - (\Omega + c)^2 = \Omega(\Omega - 4c)$ with no additional channels.*

*Proof.* By Theorem 6.2, the multiplicity-$(1,1,1)$ spectrum $\{-c, 0, +c\}$ of $K_n$ occurs only at $n = 3$. For other dimensions, either the zero eigenvalue has multiplicity $\geq 2$ (yielding doubled central frequencies) or multiple distinct conjugate pairs appear (yielding more than three grade-cross frequencies). ∎

*Remark 6.4* (Pythagorean ratios at other dimensions). The Pythagorean *ratio* $3:4:5$ does not by itself characterize $n = 3$: at $n = 4$, the four grade-cross frequencies $(\Omega - 2\beta, \Omega, \Omega, \Omega + 2\beta)$ (with the central $\Omega$ doubled by the multiplicity-$2$ zero of $K_4$) admit the sub-triple $(\Omega - 2\beta, \Omega, \Omega + 2\beta)$ in ratio $3:4:5$ at $\beta = \Omega/8$, since $(\Omega - 2\beta)^2 + \Omega^2 - (\Omega + 2\beta)^2 = \Omega(\Omega - 8\beta)$. What is genuinely unique to $n = 3$ is not the Pythagorean ratio itself but the *minimal-channel realization*: a three-frequency multiplicity-$(1,1,1)$ structure with no doubled center and no extra channels.

### 6.5 What survives across dimensions

The 2-dimensional scalar↔pseudoscalar block is dimension-independent: it is always a 2-dim subspace carrying an eigenvalue $\mu$ of the operator $\hat{D}^{(n)} := |i \Theta^{(n)}_{\mathrm{can}}|$, and the equation $\hat{D}^2 = \hat{D}\, e^{-\hat{D}}$ on this block (Corollary 5.2) holds at any $n$. Genuinely unique to $n = 3$ is the conjunction of the canonical bridge condition $4\beta = \Omega$ with *minimal-channel multiplicity-$(1,1,1)$ structure* on the grade-cross-pairing splitting (Corollary 6.3 and Remark 6.4). The $3:4:5$ ratio alone — among the *distinct* frequencies of $\Theta^{(n)}_{\mathrm{can}}$ — can occur at $n = 4$ under a different coupling, but only $n = 3$ realizes the ratio with a simple three-element splitting.

---

## 7. Discussion

### 7.1 What this paper establishes

We have presented an explicit noncommutative torus $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$ with the following structural data:

1. A spectrum factorizing through four characteristic frequencies (Theorem 2.3).
2. Pfaffian and Frobenius closed forms (Theorems 3.1, 3.3) and explicit trace-image generators of $K_0$ (§3.2).
3. A Pythagorean spectral identity $\nu_-^2 + \nu_0^2 - \nu_+^2 = \Omega(\Omega - 4\beta)$ (Theorem 4.2), holding exactly at $4\beta = \Omega$.
4. A localization (Corollary 5.2) of the Lambert-W fixed point $\mu = W(1)$ to the 2-dimensional $(0,7)$-block of $\hat{D} := |i\Theta_{\mathrm{can}}|$.
5. A Frobenius-orthogonal decomposition $\Theta_{\mathrm{can}} = \Theta_{\mathrm{swap}} + \Theta_{\mathrm{pres}}$ in which the small ($\sim 3.5\%$) intra-grade perturbation $\Theta_{\mathrm{pres}}$ lifts the threefold degeneracy of $\pm i\Omega$ in the swap-block spectrum to the triple $\pm i(\Omega - \beta), \pm i\Omega, \pm i(\Omega + \beta)$ (Proposition 5.4).
6. Dimension specificity of the minimal-channel Pythagorean prerequisite to the nearest-neighbor $\mathrm{Cl}(3,0)$ construction via explicit characteristic-polynomial analysis (Theorem 6.2, Corollary 6.3, Remark 6.4).

All claims are verified numerically (39 unit tests) and the load-bearing identities are independently re-derived symbolically in SymPy (Appendix A).

### 7.2 What this paper does not establish

The paper does **not** claim:

- *A first-principles derivation of $4\beta = \Omega$.* The identity holds to within $5 \times 10^{-4}$ at the canonical values $\beta = \varphi^{-1}/3$, but is not exact. Three candidate derivations (§4 Remark 4.3) — Pfaffian-constrained extremum, topological-charge equality, $\mathrm{Spin}(7)$ self-duality — were tested computationally and rejected. Whether $4\beta = \Omega$ is algebraically forbidden by transcendence properties of $W(1)$ and $\varphi$, or whether it could be selected by a more refined variational principle, remains open.

- *A genuine Hodge star.* The cross-pairing $\Theta_{\mathrm{can}}[i, i+3] = \Omega$ is uniform along basis-aligned indices, not the alternating-sign Hodge star on $\mathrm{Cl}(3,0)$ (Remark 2.2). The "grade-cross-pairing" terminology is used throughout.

- *A coordinate-invariant orthogonality theorem.* The decoupling of the $(0, 7)$ subspace from the $(1{:}7)$ subspace is a privileged-basis statement, valid in the $\mathrm{Cl}(3,0)$ grade basis. The spectrum is $\mathrm{SO}(8)$-invariant but the block structure is not.

- *An independent derivation of $W(1)$.* Corollary 5.2 is a localization, not a derivation — the equation $\hat{D}^2 = \hat{D}e^{-\hat{D}}$ on the $(0,7)$-block reduces to the scalar fixed-point equation defining $W(1)$. The structural content is in the *subspace* to which $W(1)$ is localized, not in any independent characterization of $W(1)$. A different (and structurally deeper) operator-algebraic appearance of Lambert-W in noncommutative-torus settings, in connection with Drinfeld modules, is given by Nikolaev \[NIK\].

- *A spectral-action computation.* The Connes–Chamseddine spectral action on $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$, including the Seeley–DeWitt expansion of $\mathrm{Tr}\,f(\hat{D}/\Lambda)$, is a separate computation deferred to follow-up work.

### 7.3 Open questions

1. Is the relation $4\beta = \Omega$ at $\mu = W(1)$, $\beta = \varphi^{-1}/3$ algebraically forbidden (e.g., via a Lindemann–Weierstrass argument on the joint transcendence of $W(1)$ and $\varphi$), or is the $5 \times 10^{-4}$ residual a numerical coincidence within precision of some natural condition we have not identified?
2. Does the operator equation $\hat{D}^2 = \hat{D}e^{-\hat{D}}$ on the full $\mathbb{T}^8_{\Theta_{\mathrm{can}}}$ admit nontrivial solutions beyond the $(0,7)$-block?
3. Is there a Tomita–Takesaki interpretation of $\hat{D}$ in which the $(0, 7)$-block plays a canonical role? Modular spectral triples on noncommutative tori \[FS\] provide a candidate framework.
4. Computation of the Connes–Chamseddine spectral action $S(\hat{D}, \Lambda) = \mathrm{Tr}\,f(\hat{D}/\Lambda)$ \[4\], including the Seeley–DeWitt asymptotics in $\Lambda$, and identification of any structural roles for $4\beta = \Omega$ in the bosonic action.
5. Do analogous constructions exist on $\mathrm{Cl}(p, q)$ for indefinite signatures, and what becomes of the dimension-specificity result?

---

## Acknowledgments

This work was supported by AEO Trivector LLC.

---

## References

\[1\] A. Connes, *Noncommutative Geometry*, Academic Press, San Diego, 1994.

\[2\] M. Rieffel, "Non-commutative tori — a case study of non-commutative differentiable manifolds," *Contemp. Math.* **105** (1990), 191–211.

\[3\] G. A. Elliott, "On the K-theory of the C*-algebra generated by a projective representation of a torsion-free discrete abelian group," in *Operator Algebras and Group Representations*, Pitman, 1984, 157–184.

\[4\] A. Connes and A. H. Chamseddine, "The spectral action principle," *Comm. Math. Phys.* **186** (1997), 731–750.

\[5\] R. M. Corless, G. H. Gonnet, D. E. G. Hare, D. J. Jeffrey, and D. E. Knuth, "On the Lambert W function," *Adv. Comput. Math.* **5** (1996), 329–359.

\[6\] M. Pimsner and D. Voiculescu, "Exact sequences for K-groups and Ext-groups of certain cross-product C*-algebras," *J. Operator Theory* **4** (1980), 93–118.

\[CL\] A. Connes and G. Landi, "Noncommutative manifolds, the instanton algebra and isospectral deformations," *Comm. Math. Phys.* **221** (2001), 141–159.

\[RIE93\] M. A. Rieffel, "Deformation quantization for actions of $\mathbb{R}^d$," *Mem. Amer. Math. Soc.* **106**, no. 506 (1993).

\[YAM\] M. Yamashita, "Connes–Landi deformation of spectral triples," *Lett. Math. Phys.* **94** (2010), 263–291; arXiv:1006.4420.

\[KL\] M. A. Kurkov and F. Lizzi, "Clifford structures in noncommutative geometry and the extended scalar sector," *Phys. Rev. D* **97** (2018), 085024; arXiv:1801.00260.

\[NIK\] I. V. Nikolaev, "Lambert $W$-function and Gauss class number one conjecture," arXiv:2512.02232 (2025).

\[Phi06\] N. C. Phillips, "Every simple higher dimensional noncommutative torus is an AT algebra," arXiv:math/0609783 (2006).

\[FS\] F. Fidaleo and L. Suriano, "Type III representations and modular spectral triples for the noncommutative torus," *J. Funct. Anal.* **275** (2018), 1484–1531; arXiv:1806.08253.

---

## Appendix A: Numerical and symbolic verification

All theorems in this paper have been verified using Python 3.10+ with NumPy and SciPy. The verification suite consists of 39 unit tests across the three modules (`canonical_data`, `identities`, `dimension_check`), each test mapped to a specific theorem or claim of the paper. Continuous integration runs the full suite on every commit (Python 3.10, 3.11, 3.12). Code is available at `https://github.com/Orion-sextant/Mathematical-Formalisms/tree/main/papers/2026-noncommutative-t8-clifford`.

### A.1 Trace-image generator verification

The Pfaffians of all $\binom{8}{2k}$ even-sized principal minors of $\Theta_{\mathrm{can}}$ were computed numerically and matched against candidate closed forms. At the canonical values $\mu = W(1) \approx 0.567143$, $\Omega = \sqrt{1-\mu^2} \approx 0.823619$, $\beta = \varphi^{-1}/3 \approx 0.206011$:

| $\|S\|$ | Indices (one representative per orbit) | $\|\mathrm{Pf}\|$ numerical | Closed form | Match |
|---|---|---|---|---|
| 2 | $(0,7)$ | $0.56714329$ | $\mu$ | ✓ |
| 2 | $(1,4)$ | $0.82361914$ | $\Omega$ | ✓ |
| 2 | $(1,2)$ | $0.11894070$ | $\beta/\sqrt{3}$ | ✓ |
| 4 | $(1,2,4,6)$ | $0.01414689$ | $(\beta/\sqrt{3})^2$ | ✓ |
| 4 | $(0,1,2,7)$ | $0.06745642$ | $\mu(\beta/\sqrt{3})$ | ✓ |
| 4 | $(1,2,3,4)$ | $0.09796183$ | $\Omega(\beta/\sqrt{3})$ | ✓ |
| 4 | $(0,1,4,7)$ | $0.46711007$ | $\mu\Omega$ | ✓ |
| 4 | $(1,2,4,5)$ | $0.66420160$ | $\Omega^2 - \beta^2/3$ | ✓ |
| 6 | $(0,1,2,4,6,7)$ | $0.00802331$ | $\mu(\beta/\sqrt{3})^2$ | ✓ |
| 6 | $(0,1,2,3,4,7)$ | $0.05555840$ | $\mu\Omega(\beta/\sqrt{3})$ | ✓ |
| 6 | $(0,1,2,4,5,7)$ | $0.37669748$ | $\mu(\Omega^2 - \beta^2/3)$ | ✓ |
| 6 | $(1,2,3,4,5,6)$ | $0.52374585$ | $\Omega(\Omega^2 - \beta^2)$ | ✓ |
| 8 | $(0,1,2,3,4,5,6,7)$ | $0.29703895$ | $\mu\Omega(\Omega^2 - \beta^2)$ | ✓ |

All matches are to within $10^{-7}$, the precision limit of the numerical Pfaffian computation. The closed forms are universal expressions in $\mu, \Omega, \beta$ — they hold not only at the specific canonical values but for any choice of the three parameters in Definition 2.1.

### A.2 Spectrum and Pfaffian (Theorems 2.3, 3.1)

Symbolic factorization of $\det(\lambda I - \Theta_{\mathrm{can}})$ in SymPy returns
$$(\lambda^2 + \mu^2)(\lambda^2 + \Omega^2)(\lambda^2 + (\Omega-\beta)^2)(\lambda^2 + (\Omega+\beta)^2),$$
confirming Theorem 2.3. The square root of $\det(\Theta_{\mathrm{can}})$ symbolically simplifies to $\mu\Omega(\Omega^2 - \beta^2)$, confirming Theorem 3.1.

### A.3 Pythagorean identity (Theorem 4.2)

Direct expansion: $(\Omega - \beta)^2 + \Omega^2 - (\Omega + \beta)^2 = (\Omega^2 - 2\Omega\beta + \beta^2) + \Omega^2 - (\Omega^2 + 2\Omega\beta + \beta^2) = \Omega^2 - 4\Omega\beta = \Omega(\Omega - 4\beta)$. Vanishes iff $\beta = \Omega/4$. ✓

### A.4 Cyclic generator spectrum (Lemma 6.1)

Eigenvalues of $K_n = C_n - C_n^{-1}$ for $n = 3, 4, 5$ computed in NumPy:

- $n = 3$: $\{0, +1.732i, -1.732i\}$ matching $\{0, \pm i\sqrt{3}\}$.
- $n = 4$: $\{0, 0, +2i, -2i\}$ matching the doubled-zero spectrum.
- $n = 5$: $\{0, \pm 1.902i, \pm 1.176i\}$ matching $\{0, \pm 2i\sin(2\pi/5), \pm 2i\sin(4\pi/5)\}$.

---

*Submitted to math-ph; cross-listed math.OA. Revised May 2026.*

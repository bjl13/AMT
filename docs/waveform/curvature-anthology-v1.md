# The Curvature Anthology
## Discharging the v2 Open Items: Curved Instantiation Structure, the Linear Triple, Field Trial, Dual Convention, and Namespace

**Companion to:** Observer-Indexed Dual Hypergraph — Canonical Specification v2.
**Discipline:** Every assumption is labeled at first use and collected in the Ledger (Part VI). Rigor flags: [THM] proven here or immediate; [NUM] numerically demonstrated; [CIR] conjecture-in-reach. Nothing below is left at [TIR].
> **Repo status note (`RECONCILIATION.md` R3).** The content of this anthology is carried, renumbered, into `waveform-monograph.md`, which is the reference text where the two differ. Numbering map: Theorem I.1 → III.1, I.2 → III.2, Proposition I.3 → III.3, I.4 → III.4, I.7 → III.5, Corollary I.8 → III.6, Lemma II.1 → IV.4, Theorem II.2 → IV.5, II.3 → IV.6, Conjecture VI.1 → B.1. The scripts and captures this text cites are in `waveform-proofs/`. The namespace files listed in Part V were not supplied to this repo.


---

## Status Ledger

| v2 open item | Disposition |
|---|---|
| 1. Curved A∞-structure realizing m₀ as genuine curvature | **Discharged.** Prop 4 [TIR-c] → [THM] via Theorem I.2 (Clifford–Koszul matrix factorization). |
| 2. Linear Triple + Möbius + stress tests | **Proven** (Theorems II.2, II.3, under labeled assumptions) with the Möbius example computed over ℝ and ℤ and four numerical stress tests executed. |
| 3. §5.3 on real data | **Run.** Corpus: 1,797 real handwritten-digit vectors, 10 node-classes, two PCA frames. Verdict: **GO** — additive null rejected. |
| 4. Conjugating-dual flag | **Decided.** View-layer parameter; identity default; conjugating required for physical helicity. Normative text in Part IV. |
| 5. w3id.org/waveform | **Prepared to the PR boundary.** Availability confirmed (404 on 2026-07-19); PR-ready files, context, and ontology delivered. The PR itself must originate from the owner's GitHub account. |
| Residual | Conjecture 5 beyond the linear regime remains [CIR], restated precisely as Conjecture VI.1 with its discharge conditions. |

---

# Part I — The Curved Instantiation Complex

The task is to stop calling m₀ "curvature" by analogy and make it the curvature element of an actual curved structure, so that D_O(v) is a normalized curvature norm by *construction* rather than by identification. The instrument is elementary and deliberately so: Clifford–Koszul operators on a super tensor product, which land the instantiation data directly in the category of matrix factorizations — the canonical home of curved modules since Eisenbud (1980), and equivalent to twisted complexes over curved algebras by Căldararu–Tu (*Trans. AMS*, 2012).

## I.0 Setting and standing assumption

Fix a node v and frame O. Work over 𝕂 ∈ {ℝ, ℂ}. Write π := π_O for the projector onto the visible subspace Q := Q_O ⊆ W, and let Φ̃_e := Φ̃_O(v,e) ∈ W denote the resolved payloads of the m := m_v visible incidences at v. Define

- curvature payloads: **m₀(e) := (1 − π) Φ̃_e ∈ Q^⊥**,
- energies: **E := Σ_e ‖Φ̃_e‖²**, **E_vis := Σ_e ‖πΦ̃_e‖²**, **𝔴 := Σ_e ‖m₀(e)‖²**.

**(U) Orthogonality.** π is an orthogonal projector (self-adjoint idempotent) — already normative (v2 §1.4). Under (U), Pythagoras gives 𝔴 = E − E_vis and D_O(v) = 𝔴/E (with the v2 convention D := 0 when E = 0).

## I.1 The Clifford model

For w ∈ W define on the exterior algebra ΛW the odd operator

c(w) := ε(w) + ι(w♭)

(wedge plus contraction against the real pairing B(u,w) := Re⟨u,w⟩). The Clifford relation holds:

**c(u) c(w) + c(w) c(u) = 2 Re⟨u, w⟩ · id**,  in particular c(w)² = ‖w‖² · id.

**Definition I.1 (instantiation module).** Let M_v := ⊗̂_{e ∈ I_O(v)} Λ W_(e) be the *super* tensor product of one exterior-algebra factor per visible incidence (each W_(e) a copy of W; the economical variant Λ(𝕂·Φ̃_e) per factor suffices and is what an implementation would store). Write c_e(w) for c(w) acting on the e-th factor. Because the tensor product is super, odd operators on distinct factors *anticommute*.

Define three odd operators on M_v:

𝔡 := Σ_e c_e(Φ̃_e),  𝔡^vis := Σ_e c_e(πΦ̃_e),  𝔡^⊥ := Σ_e c_e(m₀(e)),  so 𝔡 = 𝔡^vis + 𝔡^⊥.

**Theorem I.1 (operator Pythagoras / superpotential split). [THM]**
Under (U):

1. 𝔡² = E · id, (𝔡^vis)² = E_vis · id, (𝔡^⊥)² = 𝔴 · id;
2. {𝔡^vis, 𝔡^⊥} = 0;
3. consequently E = E_vis + 𝔴 at the operator level, i.e. the scalar Pythagorean identity of v2 Prop 4 is the anticommutator calculus of the module.

*Proof.* Cross terms with e ≠ e′ vanish because odd operators on distinct super-factors anticommute. Same-factor terms use the Clifford relation: Σ_e c_e(Φ̃_e)² = Σ_e ‖Φ̃_e‖² id = E·id, and likewise for the visible and perpendicular pieces. The mixed anticommutator on factor e is 2 Re⟨πΦ̃_e, m₀(e)⟩ = 0 by (U). ∎

## I.2 The curved structure, and the discharge of Prop 4

Recall the target axioms. A ℤ/2-graded curved algebra is B = (A, m₀^{alg}, m₁, m₂, …) with m₀^{alg} ∈ A even, satisfying the curved Stasheff identities; a curved module (M, d_M) over B satisfies the k = 1 module identity **d_M² = ρ(m₀^{alg})**. When A = 𝕂 (or a commutative ring R) and m₀^{alg} = 𝔴 ∈ R, a curved module is exactly a **matrix factorization of 𝔴**: an odd d with d² = 𝔴·id (Eisenbud 1980); and Căldararu–Tu identify MF(R, 𝔴) with twisted complexes Tw(B_𝔴) over the curved algebra B_𝔴 with curvature m₀^{alg}(1) = 𝔴.

**Theorem I.2 (curvature realization — discharges v2 Prop 4 [TIR-c] → [THM]). [THM]**
Let B_𝔴 = (𝕂, m₀^{alg} = 𝔴·1, m₁ = 0, m₂ = multiplication, m_{k≥3} = 0), ℤ/2-graded. Then:

1. (M_v, 𝔡^⊥) is a curved dg-module over B_𝔴: (𝔡^⊥)² = 𝔴·id realizes d_M² = ρ(m₀^{alg}); the Bianchi identity m₁(m₀^{alg}) = 0 holds trivially (central scalar). Equivalently (M_v, 𝔡^⊥) ∈ MF(𝕂, 𝔴) ≅ Tw(B_𝔴).
2. **D_O(v) = 𝔴 / E is the energy-normalized curvature of this structure** — the squared norm of the curvature element per unit payload energy. The word "curvature" is now internal to the mathematics, not a modeling label.
3. Relative form: (M_v, 𝔡) ∈ MF(𝕂, E) and (M_v, 𝔡^vis) ∈ MF(𝕂, E_vis); by Theorem I.1(2), the deformation 𝔡^vis ↦ 𝔡^vis + 𝔡^⊥ shifts the superpotential by exactly 𝔴. The curvature defect **is** the discrepancy between the potential the frame *claims* (E_vis) and the potential the payload *carries* (E).
4. Family form: over frame space 𝒪 with R = C^∞(𝒪), the map 𝔴 : O ↦ Σ_e ‖(1 − π_O)Φ̃_O(v,e)‖² is a nonnegative **frame superpotential**, (M, 𝔡^⊥) is a matrix factorization over (R, 𝔴), and its zero locus Z_v = {O : D_O(v) = 0} — the flat frames — is exactly where the curved structure trivializes.

*Proof.* (1) is Theorem I.1(1) read against the module axiom; centrality of 𝔴 makes Bianchi vacuous; the MF/Tw identification is Căldararu–Tu. (2) divides (1) by E. (3) is Theorem I.1(1–2). (4) is (1) fibered over 𝒪. ∎

**Proposition I.3 (where the curvature hides). [THM]**
End(M_v) with differential ad(𝔡^⊥) is an *honest* dg-algebra: ad(𝔡^⊥)² = ad((𝔡^⊥)²) = ad(𝔴·id) = 0. Curvature is a module-level phenomenon, invisible to endomorphisms — the standard curved-algebra subtlety (there is no naive abelian category of curved modules with d² = 0; MF is the repair), reproduced here on the nose. ∎

## I.3 Rigidity at a fixed frame, and why Maurer–Cartan must be familial

**(CL) Clifford ansatz.** Deformations are of Clifford type: odd b = Σ_e c_e(ξ_e) with ξ_e ∈ W.

**Proposition I.4 (fixed-frame rigidity). [THM]**
At a fixed frame, under (CL), (𝔡^⊥ + b)² = Σ_e ‖m₀(e) + ξ_e‖² · id, which vanishes iff ξ_e = −m₀(e) for every e — the trivial kill (the differential erased, not flattened). Hence there is **no nontrivial fixed-frame bounding cochain**, and the Maurer–Cartan problem is forced to live over the frame family. This is not a retreat; it is the formal content of the slogan that dimensional pressure cannot be argued away in place — it can only be *absorbed by moving the frame*.

*Proof.* Same-factor Clifford relation; cross-factors anticommute. ∎

**Definition I.5 (family MC / absorbing extension).** Let a frame family be given over a base S (path or loop), with transported frames O(s) and payloads. **(FR) Frame richness:** admissible frames include, for each s, extensions Q^ext(s) ⊇ Q(s) inside W. A *family-MC solution* is a continuous (compatible with transport) choice s ↦ O^ext(s) of admissible extensions with (1 − π^ext(s)) Φ̃(s, e) = 0 for all e and all s — equivalently 𝔴^ext ≡ 0 ≡ D^ext over S.

**Theorem I.6 ((b) ⇔ (c); one direction unconditional). [THM]**
(c) ⟹ (b): if a frame extension over S drives D ≡ 0, then β := Σ_e c_e((π^ext − π)Φ̃_e) is a family-MC solution: since π^ext − π projects onto Q^ext ⊖ Q ⊥ Q, Theorem I.1's calculus gives (𝔡^vis + β)² = (E_vis + Σ‖(π^ext − π)Φ̃_e‖²)·id = E^ext_vis·id = E·id — the full potential is recovered and the defect is zero. (b) ⟹ (c) *under (CL) and (FR)*: a Clifford-type family solution β = Σ c_e(ξ_e) achieving defect zero forces, by the same computation, ξ_e to supply exactly the missing components, and (FR) packages span(ξ_e) into an admissible extension. Without (CL) the converse is open (a general odd β need not be Clifford-type); the unconditional direction suffices for every use made of the Triple below where obstruction is *derived from* extension failure. ∎

## I.4 The transport–pressure identity

The last piece connects the vertical curvature (payload, 𝔴) to the horizontal one (Berry, F = π dπ dπ), and upgrades the v2 claim "D is the shadow of connection curvature" from analogy to identity.

**Proposition I.7 (transport–pressure identity). [THM]**
For a smooth frame path t ↦ π(t) and a constant ambient payload Φ̃, the Grassmann-covariant derivative of the visible instantiation is sourced by the curvature payload through the second fundamental form:

**∇_t (π Φ̃) = π π̇ (1 − π) Φ̃ = II*_t (m₀(t)).**

*Proof.* d/dt(πΦ̃) = π̇Φ̃; differentiate π² = π to get π̇π + ππ̇ = π̇, multiply by π on the left: ππ̇π = 0; hence π(π̇Φ̃) = ππ̇(π + π^⊥)Φ̃ = ππ̇(1−π)Φ̃. The operator ππ̇(1−π) is the adjoint second fundamental form of the subbundle. ∎

**Corollary I.8 (drift bound). [THM]** ‖∇_t Ψ^vis‖ ≤ ‖π̇‖ Σ_e ‖m₀(e)‖ ≤ ‖π̇‖ √(m · 𝔴) = ‖π̇‖ √(m · D_O(v) · E). Flat nodes (D = 0) transport parallelly; the parallel-transport drift of any node is controlled by the square root of its dimensional pressure. Frame holonomy therefore *sees* exactly the nodes that pressure marks — the precise mechanism by which the vertical curvature of Theorem I.2 feeds the horizontal holonomy of v2 Theorem 1.

---

# Part II — The Linear Triple, Proven

We now prove v2's Conjecture 5 in the linear regime, compose it with the frame-holonomy data of v2 Theorem 2, work the Möbius example over both ℝ and ℤ, and sharpen the prior obstruction theorem's growth/reinterpretation dichotomy into a spectral–arithmetic classification. The prior theorem — nontrivial H¹(S, ℐ) obstructs global invariant sections, with resolution exhausted by base change on π₁(S) (growth) or twisted flat-bundle coefficient change (reinterpretation) — is taken as established; what is new here is its composition with the instantiation formalism, the identification of *which* obstructions each operation resolves, and the closure of the loop back to AMT's infinite-order clause.

## II.0 Setting and assumptions

**(LIN) Linear regime.** S_O linear; payloads fixed; transport of the visible and complement bundles is by the unitary Kato holonomy of v2 Theorem 1 (unitarity is automatic from (U): [π̇, π] is skew-adjoint).
**(DISC) Discretization.** The loop is presented by a finite good cover — frames O_0, …, O_{N−1} with unitary transition maps g_i on the complement, Π g_i = φ^⊥ := complement holonomy ∈ U(d−k). (Kato transport block-preserves the splitting, so φ^⊥ is well-defined alongside φ ∈ U(k).) Cellular = Čech for good covers; nothing depends on N.

The linear extension problem: local invisible payloads introduce incremental defects c_i ∈ Q^⊥_i; an *absorbing section* is a global section ξ of the complement local system ℐ^⊥ = (Q^⊥, φ^⊥) satisfying the transported compatibility ξ_{i+1} = g_i ξ_i + c_i. Traversing the loop once and closing up yields the **inhomogeneous holonomy equation**

(φ^⊥ − 1) ξ₀ = C,  C := Σ_i (transport of c_i to the basepoint),

and C is precisely a twisted Čech 1-cocycle; its class [C] lives in H¹(S¹, ℐ^⊥).

**Lemma II.1 (twisted cohomology of the circle). [THM]**
For a local system ℒ_ψ on S¹ with fiber V and monodromy ψ: H⁰ = ker(ψ − 1) (invariant sections), H¹ = coker(ψ − 1) (the obstruction group). For unitary ψ over a field, dim H⁰ = dim H¹, so H¹ ≠ 0 ⟺ 1 ∈ spec(ψ) ("resonance"). *Proof:* the cellular complex of the circle with one 0-cell and one 1-cell is V →^{ψ−1} V. Unitarity makes ψ − 1 normal, equating kernel and cokernel dimensions. ∎

The correct reading of the obstruction theorem follows: H¹ is *where obstruction classes live*. Off resonance H¹ = 0 and every defect is absorbable (but H⁰ = 0 too: no frame-invariant sections exist — the **pure helix**: everything locally reconcilable, nothing globally invariant). On resonance H¹ ≠ 0, invariant directions exist, and along them the harmonic component of C is an honest obstruction.

## II.1 The Triple

**Theorem II.2 (Linear Triple; assumptions (U), (FR), (CL), (LIN), (DISC)). [THM]**
For a frame loop with defect class [C] ∈ H¹(S¹, ℐ^⊥_{φ^⊥}), the following are equivalent:

(a) [C] ≠ 0;
(b) no family-MC solution exists over S¹;
(c) no global frame extension over S¹ drives D ≡ 0.

*Proof.* (b) ⇔ (c) is Theorem I.6 over base S¹ (the ⟸ direction unconditional; ⟹ under (CL), (FR)). (c) ⇔ (a): a global extension exists iff the absorbing equation (φ^⊥ − 1)ξ₀ = C is solvable iff C ∈ im(φ^⊥ − 1) iff [C] = 0 in coker(φ^⊥ − 1) = H¹ (Lemma II.1). ∎

The three clauses of v2 Conjecture 5 are therefore *the same statement in three languages* in the linear regime: cohomological (a), deformation-theoretic (b), operational (c). Irreducible latent dimensional pressure — pressure no single global reframing can dissolve — is exactly a nonvanishing twisted cohomology class of the frame loop.

## II.2 Growth versus reinterpretation: the spectral–arithmetic dichotomy

Pull back along the n-fold cover S¹ → S¹ (growth): monodromy ψ ↦ ψⁿ, defect C ↦ C_n = (Σ_{j<n} ψ^j) C. Change coefficients (reinterpretation): ψ ↦ χ·ψ (character twist: eigenphases *translate*, γ ↦ γ + θ), or conjugate, or enlarge/localize the coefficient ring.

**Theorem II.3 (resolution dichotomy, refined). [THM]**

1. **Full resonance is immune to growth.** On the λ = 1 eigencomponent, C_n = n·C: covers amplify, never resolve. Only reinterpretation (translate the phase off 1) resolves field-resonant obstruction.
2. **Finite order ≠ 1: the geometric-series kill.** On a primitive q-th root eigencomponent λ ≠ 1: the base is off-resonance (unobstructed), and at the q-cover the pulled-back monodromy becomes 1 there while C_q = (Σ_{j<q} λ^j) C = 0 — the transported defects destructively interfere around the unwrapped loop. Growth thus **manufactures invariant sections at finite-order spectrum without ever introducing obstruction**: resonance is created upstairs with the defect already annihilated.
3. **Torsion is growth's true domain.** Over ℤ, obstruction can be torsion without resonance (ψ − 1 injective with nontrivial cokernel). Möbius: ψ = −1 on ℤ gives H¹ = coker(−2) = ℤ/2. The double cover kills it — C_2 = (1 + (−1))C = 0, the same geometric-series mechanism — and rationalization (reinterpretation by localization ℤ → ℚ) kills it too. Both branches of the dichotomy act on the minimal example.
4. **Spectral form of the dichotomy.** Growth acts on eigenphases by multiplication (γ ↦ nγ); reinterpretation by translation (γ ↦ γ + θ). Obstruction decomposes (over a PID) as torsion ⊕ resonant-harmonic; growth resolves exactly the torsion/finite-order phenomena via geometric-series annihilation; reinterpretation resolves resonance by spectral translation and, via localization, torsion as well. Exhaustiveness of the pair is inherited from the prior obstruction theorem; what is added is the assignment of *which* operation resolves *what*.
5. **Closure to AMT.** Irrational eigenphases — φ of infinite order — are immune to every finite cover: no growth manufactures invariance, no unwinding closes the orbit. **AMT's genuine-helix condition (infinite-order monodromy, v2 Theorem 2) is exactly the condition under which growth is permanently unavailable as a resolvent: the substrate that cannot be unwound.** The periodic-helix degenerate case (finite order) is exactly the growth-resolvable case. The two AMT substrate classes and the two resolution operations are the same partition seen from opposite sides.

*Proof.* (1)–(3) are the displayed computations plus Lemma II.1; the Möbius ℤ/2 is verified below by Smith normal form. (4) collects them; the decomposition over a PID is the structure theorem applied to coker(ψ − 1). (5): φⁿ ≠ 1 for all n ⟺ some γ_j ∉ 2πℚ, which is v2 Theorem 2's infinite-order clause verbatim. ∎

## II.3 The Möbius example, both ways

The complement local system of a frame loop with φ^⊥ = −1 on a rank-1 real complement is the Möbius local system — realized combinatorially as the n-cycle sheaf with identity edge maps except one edge equal to −1.

**Over ℝ (field case). [THM + NUM]** The twisted coboundary δ has full rank; H⁰ = H¹ = 0: acyclic, hence *never obstructed* — but never invariant either (no nonzero flat section of the Möbius band: the paradigm pure helix at finite order... resolved at the double cover per II.3(2)). Quantitatively, the twisted sheaf Laplacian L = δᵀδ has spectrum {2 − 2cos((2j+1)π/n)}, verified numerically to 1.1 × 10⁻¹⁵ for n = 5, 8, 12, with spectral gap 2 − 2cos(π/n) ≈ π²/n². The gap controls the conditioning of absorption: **H¹ = 0 yet ‖(δᵀδ)⁻¹‖ = gap⁻¹ → ∞**. Name this *soft obstruction*: cohomologically unobstructed, operationally ill-conditioned — the cost of absorbing pressure diverges as the loop refines even though absorption never strictly fails. Soft obstruction is invisible to the Triple's trichotomy and is the correct quantitative refinement of it: the Hansen–Ghrist spectral-sheaf program's gap, imported to frame space.

**Over ℤ (integral case). [THM + NUM]** Smith normal form of the twisted coboundary: diag(1, …, 1, 2) — verified symbolically for n = 3 and n = 5 — hence **H¹(S¹; ℤ_−) = ℤ/2**: a genuine 2-torsion obstruction with no resonance. The double cover resolves it (geometric-series kill: C_2 = (1 + (−1))C = 0; geometrically, the Möbius band unwinds to the cylinder); rationalization resolves it (localization). The smallest possible example exhibits the full dichotomy of Theorem II.3, one branch per coefficient theory.

## II.4 Stress tests (executed)

**A. Berry validation of v2 Theorem 1 (k = 1). [NUM]** Kato transport Ẇ = [π̇, π]W integrated (RK4, N = 4000) around latitude loops on Gr(1,2) ≅ S². Holonomy unimodular to 10⁻⁸; numerical phase versus the analytic −π(1 − cos θ):

| θ | γ numeric | γ analytic | error |
|---|---|---|---|
| π/3 | −1.570796 | −1.570796 | 1.2 × 10⁻⁷ |
| π/2 | −3.141593 | −3.141593 | 4.4 × 10⁻¹⁶ |
| 2π/3 | +1.570796 | +1.570796 | 1.2 × 10⁻⁷ |

**B. Wilczek–Zee non-abelian holonomy (k = 2, Gr(2,4)). [NUM]** Two loops of projectors built from overlapping-plane generator pairs (one real skew pair; one mixed with an i·symmetric generator). Both holonomies unitary to 10⁻¹⁴; Hol_A a real σ_y-type rotation, Hol_B a σ_x-type rotation, ‖[Hol_A, Hol_B]‖ = 2.770: genuinely non-abelian, as the k > 1 theory demands. Eigenphases ≈ 0.2271 · 2π — irrational-looking, i.e. the generic infinite-order (genuine-helix) case. Instructive negative control from the construction process: generator pairs acting in *disjoint* planes commute and produce trivial or coinciding holonomies — non-abelian structure requires overlapping planes, the operator-level face of "constitutive nesting."

**C. Möbius spectra and torsion. [NUM]** As reported in II.3: spectra match the closed form to 10⁻¹⁵; ranks confirm ℝ-acyclicity; Smith forms confirm ℤ/2.

**D. Cover-resolution table. [NUM]** For k^⊥ = 1, defect C = 1 + 0.5i, covers n ∈ {1, 2, 3, 6}:

| monodromy phase α | behavior across covers |
|---|---|
| 0 (full resonance) | \|C_n\| = n·\|C\| grows; never solvable; invariants at every level — growth powerless (II.3(1)) |
| 2π/3 (rational) | solvable at every level; \|C_3\| = \|C_6\| = 0 exactly and invariants appear at n = 3 — geometric-series kill (II.3(2)) |
| 2π/φ_golden (irrational) | solvable at every level; \|C_n\| wanders (1.118, 0.810, 0.531, 0.952, …), never zero; invariants never appear — the unwindable helix (II.3(5)) |

---

# Part III — Field Trial (v2 §5.3 on Real Data)

**Corpus.** scikit-learn `digits`: 1,797 real scanned handwritten digit images, 64-dimensional pixel vectors, mean-centered. Nodes = the 10 digit classes (m_v ≈ 174–183 incidences each; incidence payload = one image vector). Frames: two orthogonal PCA visible planes — O₁ = span(PC1, PC2) (28.5% of variance), O₂ = span(PC3, PC4) (20.2%). Ambient energy for D_O is the full 64-dimensional payload energy. Seeds fixed (rng 42); pairwise coherence sampled at ≤ 4,000 pairs/node; 50 random orderings/node for monotonicity; 500-draw isotropic null (observed magnitudes, uniform directions) for the permutation test.

**Results.**

| class | m_v | tension O₁ | coh O₁ | tension O₂ | coh O₂ | pair-flip % | mono-viol % | D_O₁ | z₁ | z₂ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 178 | 139.7 | +0.926 | 261.3 | +0.641 | 11.1 | 0.0 | 0.546 | +26.4 | +20.5 |
| 1 | 182 | 445.5 | +0.516 | 1282.2 | +0.404 | 30.5 | 13.0 | 0.758 | +18.9 | +15.5 |
| 2 | 177 | 237.1 | +0.754 | 391.5 | +0.540 | 22.1 | 3.2 | 0.851 | +23.2 | +21.3 |
| 3 | 183 | 352.5 | +0.804 | 673.2 | +0.423 | 23.5 | 0.1 | 0.591 | +24.0 | +15.5 |
| 4 | 181 | 254.7 | +0.870 | 861.9 | +0.354 | 26.6 | 1.6 | 0.583 | +25.1 | +15.5 |
| 5 | 182 | 1635.6 | +0.027 | 396.2 | +0.569 | 52.2 | 35.6 | 0.855 | +4.9 | +19.7 |
| 6 | 181 | 169.3 | +0.906 | 314.7 | +0.768 | 2.9 | 0.0 | 0.633 | +26.6 | +24.4 |
| 7 | 179 | 169.5 | +0.862 | 345.4 | +0.647 | 15.2 | 0.5 | 0.776 | +24.8 | +22.4 |
| 8 | 174 | 723.4 | +0.199 | 1324.3 | +0.021 | 47.8 | 22.4 | 0.890 | +11.5 | +3.0 |
| 9 | 180 | 469.6 | +0.553 | 591.9 | +0.454 | 31.3 | 12.2 | 0.693 | +21.9 | +16.3 |

**Aggregate:** tension > 0 in both frames: **10/10** (P1 ✓). Mean pairwise coherence sign-flip rate: **26.3%**, nonzero for every class (P3 ✓ — this alone falsifies every additive model, per v2 §5.2). Mean monotonicity-violation rate: **8.9%** of incremental steps, present in 8/10 classes (P2 ✓). Node-level *mean*-coherence sign flips: **0/10** — every class keeps positive mean coherence in both frames.

**Reading the absent node-level flip honestly.** The node-level flip is a *sufficient* witness, not a necessary one, and its absence here is exactly what a supervised class corpus predicts: members of a digit class are mutually aligned in any informative frame, so the class *mean* coherence stays positive. The discriminating structure lives one level down, in the 26% of pairs whose alignment reverses between frames — invisible to any frame-independent nonnegative-weight model. Classes 5 and 8 are the latent-pressure case studies the formalism was built for: class 5 is nearly incoherent in the dominant frame (coh = +0.027, tension = 1636, D = 0.855) yet solidly coherent in the subdominant one (+0.569); class 8 mirrors it (+0.199 → +0.021, D = 0.890). These are nodes whose co-incidence the leading frame cannot explain — dimensional pressure, measured on real data.

**Permutation test.** Against the isotropic null (observed magnitudes, random in-plane directions), observed net resultants sit +3.0 to +26.6 standard deviations high across all classes and both frames: directional structure is real and enormous. Additive models possess no directional degrees of freedom at all; the comparison is not close.

**Verdict: GO.** The additive null is rejected on this corpus by (P1) + (P2) + (P3); the waveform apparatus is supported.
> **Repo note, scope correction (`RECONCILIATION.md` R2).** The null rejected here is the scalar, nonnegative-weight additive model. Vector addition under projection also produces (P1)–(P3), so this GO is phenomenon detection (H₀), not comparative support. The comparative rungs are H₁–H₃ in `waveform-proofs/notes/`.

 **Limitations:** one corpus; frames chosen by PCA rather than adversarially; payloads are raw centered pixels. Recommended second corpus for robustness: a real co-occurrence hypergraph with external embedding payloads (nodes = target words, incidences = context words, payloads = pretrained embeddings, frames = distinct projection planes) — flagged, not yet run.

---

# Part IV — The Dual Convention: Decided

**Physics.** Reading an incidence from the relation side reverses the propagation orientation. Helicity is the projection of spin onto propagation (Born–Wolf §1.4) and is *odd* under that reversal: h ↦ −h; on payloads this is complex conjugation, equivalently J ↦ −J, which swaps the left/right circular basis states. The physically faithful dual is therefore the **conjugating** dual. Both conventions are strict involutions (conjugation² = id), so nothing in v2 §2's mathematics forces the choice — the physics does.

**Decision (normative).** The dual convention is a **view-layer parameter**, never stored:

> `wf:dualConvention ∈ {identity, conjugating}`, a parameter of the query-time dual view (v2 §2). Default: `identity` (zero-cost transpose, matching the v2 involution and the never-persist principle). `conjugating` (h ↦ −h, payload conjugation, J ↦ −J) is **required** whenever h carries physical helicity semantics. The flag has no storage footprint, no SHACL impact, and no effect on the incidence store; it modifies only the read applied during dualization. Mixing conventions within a single dual view is prohibited.

This resolves the flag with the involution preserved in both branches, the query-time-view principle intact, and the physical case correctly handled — and it is recorded in the ontology annotation of the namespace artifacts below.

---

# Part V — The Namespace: Prepared to the PR Boundary

**Availability.** `https://w3id.org/waveform` returned **404 on 2026-07-19** — unregistered, available. (w3id serves its own page for registered ids; 404 means the top-level directory does not exist.)

**Process (confirmed current).** Registration is a pull request to `perma-id/w3id.org`: fork, add a top-level directory `waveform/` containing `.htaccess` (redirect rules) and `README.md` (contact + identifier info), commit with a descriptive message naming the project, and submit the PR; administrators review and changes go live on merge. Naming policy is claim-a-top-level-directory; no link-squatting.

**Delivered artifacts** (in `outputs/`):

- `w3id-waveform-pr/waveform/.htaccess` — content-negotiated redirects: `application/ld+json` → context, `text/turtle`/`rdf+xml` → ontology, default → docs; deep links for `context.jsonld`, `ontology.ttl`, `shapes.ttl`; catch-all to docs. 302 during stabilization with an in-file note to flip to 301 once the target layout freezes.
- `w3id-waveform-pr/waveform/README.md` — per w3id convention.
- `waveform-ns/context.jsonld` — the consolidated v2 context including all v2 §6 deltas (`anisotropyAxis`, `helicityPlaneU/V`, `gatingThreshold`, `incidenceCount`, `propagationAxis` as legacy metadata).
- `waveform-ns/ontology.ttl` — minimal OWL/RDFS: the eight classes (ProjectedIncidence, LatentIncidence, ObservationFrame subclassed under `prov:Entity`), object/datatype properties with range annotations mirroring the SHACL constraints, and the dual-convention and dimensional-pressure semantics recorded as ontology comments.

Redirect targets are parameterized to `https://bjl13.org/ns/waveform/` — adjust if the hosting path differs; the four files (`index`, `context.jsonld`, `ontology.ttl`, `shapes.ttl`) must exist at the target before the PR merges, since changes go live immediately.

**The one step that cannot be delegated:** the PR must originate from the namespace owner's GitHub account (it is the ownership record and contact-of-record for the identifier). Everything up to that click is done.

---

# Part VI — Assumption Ledger and the Residual Conjecture

| Label | Statement | Used in | If dropped |
|---|---|---|---|
| **(U)** | π_O orthogonal (self-adjoint idempotent) | Everything energy-flavored: I.1–I.8, II.2, D_O itself | Pythagoras fails; 𝔴 ≠ E − E_vis; Theorem I.1(2)'s anticommutator no longer vanishes; already normative in v2 §1.4 |
| **(FR)** | Frame space admits extensions Q^ext ⊇ Q as needed | I.6 (⟹ direction), II.2 | Pointwise absorption can fail for reasons of frame poverty rather than topology; the Triple's (c) decouples from (a) |
| **(CL)** | MC deformations of Clifford type β = Σ c_e(ξ_e) | I.4, I.6 (⟹), II.2 (b ⟹ c) | (c) ⟹ (b) survives unconditionally; the converse reopens — general odd deformations might flatten without corresponding to any frame extension |
| **(LIN)** | Linear S_O, fixed payloads, unitary Kato transport on flat complement coefficients | All of Part II | The Triple reverts to Conjecture VI.1 |
| **(DISC)** | Loop presented by a finite good cover | II.0, II.2 | Replace Čech by sheaf cohomology proper; nothing essential changes for S¹ |
| **(GEN)** | Genericity of irrational eigenphases where "infinite order" is asserted | II.3(5), stress test B | Finite-order (periodic-helix) branch applies instead; growth becomes available |

**Conjecture VI.1 (the residual — nonlinear Triple). [CIR]**
Drop (LIN) and (CL). Equip the instantiation complex with the curved A∞-structure whose m₀ is Theorem I.2's curvature, whose m₂ is induced by a bilinear S_O, and whose m_{k≥3} are the Taylor coefficients of a nonlinear superposition operator; replace the complement local system by the induced (generally non-flat, possibly non-unitary) transport. Conjecture: (a) the degree-1 obstruction class of the resulting sheaf of curved modules is nonzero ⟺ (b) the full inhomogeneous Maurer–Cartan equation Σ_k m_k(b, …, b) = −m₀ (FOOO form) has no solution over the family ⟺ (c) no admissible frame deformation drives D → 0 globally. **Discharge conditions:** (i) write the m_{k} explicitly from S_O and verify the curved Stasheff identities (the k = 1 identity is Theorem I.2; the rest are new); (ii) prove (b) ⟸ (c) by exhibiting the extension-induced b as in I.6 with higher corrections; (iii) prove (b) ⟹ (a) by the standard obstruction-theory spectral sequence, whose E₂ input is exactly Part II's linear computation — the linear Triple proven here is the leading order of the nonlinear one, which is why it was worth proving first.

---

## Coda

The arc of the anthology, compressed: dimensional pressure is now literal curvature (Theorem I.2); curvature that cannot be flattened in place (Proposition I.4) can only be absorbed by moving frames; whether motion suffices is a cohomology class (Theorem II.2); when it does not suffice, exactly two remedies exist and each has a spectral signature — growth multiplies phases and kills torsion by geometric series, reinterpretation translates phases and kills resonance (Theorem II.3); the substrate on which growth is *permanently* unavailable is exactly AMT's genuine helix; and real data exhibits the interference structure that makes all of this falsifiable rather than decorative (Part III). The observation frame was never a confession of subjectivity. It is a coordinate on a bundle, and the bundle has curvature, and the curvature is measurable, and now it has been measured.

# The Waveform Monograph
## Observer-Indexed Dual Hypergraphs, Incidence Waveforms, and the Curved Substrate of Avergent Manifold Topology

**A complete long-form development: formal grammar, corrected citations, the curved instantiation complex, the linear Triple, real-data falsification, and the full reproducible proof codebase.**

*Self-contained. Every assumption is labeled at first use and collected in Appendix A. Rigor flags: **[THM]** proven or immediate; **[NUM]** numerically witnessed (code + captured output inline in Part VII); **[CIR]** conjecture-in-reach. Nothing is left at "theorem-in-reach" — items previously at [TIR] are either discharged to [THM] here or explicitly demoted to [CIR] with discharge conditions.*
> **Repo status note (`RECONCILIATION.md`).** This is the reference text for the waveform program in this repository. Two later results qualify it: Part V's GO is phenomenon detection only (H₀; note at V.2, R2), and the detector ladder H₀–H₃ that supplies comparative tests lives in `waveform-proofs/notes/`. Part VII's listings match `waveform-proofs/src/` exactly; that folder now holds 14 scripts, not 8.


---

## Table of Contents

- **Part 0** — Orientation: what this object is and why it is not systems poetry
- **Part I** — Formal grammar of the latent relation-field and observation frames
- **Part II** — The corrected citation spine
- **Part III** — The curved instantiation complex (discharges the curvature claim to [THM])
- **Part IV** — The linear Triple, the Möbius example, and the spectral–arithmetic dichotomy
- **Part V** — Field trial: falsification on real data
- **Part VI** — The dual convention and the namespace
- **Part VII** — The proof codebase: every script, inline, with captured output
- **Appendix A** — Assumption ledger
- **Appendix B** — The residual conjecture
- **Appendix C** — Notation index

---

# Part 0 — Orientation

The object under study is a hypergraph model in which **relations are primary and nodes are derived**. In the usual telling a graph is nodes-first: entities exist, then edges record their relationships. Here the order is inverted. What exists first is a *latent relation-field* — a constrained space of possible incidences, each carrying a local vector payload — and a **node is what precipitates at the intersection of the relations that pass through it** when a particular observer looks. Two observers with different visible subspaces precipitate different nodes from the same latent field. This is not perspectivism as attitude; it is a projection operator acting on a vector space, and everything downstream is the linear algebra and topology of that projection.

Three commitments discipline the whole construction and are worth stating before any symbol:

1. **Provenance is representational, not decorative.** An instantiated incidence is a stateful event carrying the frame that produced it (PROV-O, Part II). The dual hypergraph is a *view*, never a stored artifact (Part VI).
2. **Convergence is lossy.** When a frame projects the latent payload onto its visible subspace, the discarded component is not noise — it is measurable, it is called *dimensional pressure* D_O, and Part III proves it is literally a curvature.
3. **The anti-mystical test binds.** Every claim must admit operational definition, formal constraint, and a distinguishing prediction. Part V supplies the distinguishing prediction and runs it against real data; the model could have failed there and did not.

The payoff, assembled across Parts III–IV, is a single sentence that is now a theorem rather than a slogan: *dimensional pressure is the curvature of a curved module; curvature that cannot be flattened in place can only be absorbed by moving the observation frame; whether such motion suffices globally is a twisted cohomology class of the frame loop; and the frame loops on which no amount of motion suffices are exactly the genuine helices of Avergent Manifold Topology.*


---

# Part I — Formal Grammar

## I.1 The latent relation-field

**Definition I.1.** A *latent relation-field* is F = (V̄, Ē, Ī, W, Ξ) where V̄ is a set of latent entities, Ē a set of latent relations, Ī ⊆ V̄ × Ē an incidence set, W a real or complex inner-product space of dimension d (the *payload space*), and Ξ : Ī → W the *latent state map* assigning each incidence a payload vector. F is not a graph; it is the constrained space from which graphs precipitate under observation.

The philosophical grammar that motivates this — "a node is an intersection, an incidence is a waveform, an instantiation is a superposition" — is discharged into mathematics as follows: *intersection* becomes the set of relations incident to a latent entity; *waveform* becomes the payload vector Ξ(v,e) ∈ W together with the operators (anisotropy, polarity, helicity) that act on it; *superposition* becomes the resultant Σ_e Φ_O(v,e) of the visible projected payloads.

## I.2 The observation frame

**Definition I.2.** An *observation frame* is

O = (Q_O, Γ_O, τ_O, ê_O, Π_O, c_O, S_O, meta_O)

with components:

- **Q_O ∈ Gr(k, d)** — the *visible subspace*, a k-plane in the payload space, represented by its orthogonal projector π_O (orthogonality is required; see I.4).
- **Γ_O : Ī → [0,1]** and threshold **τ_O** — *gating*; incidence i is visible iff Γ_O(i) > τ_O. Visibility indicator χ_O(i) = 1[Γ_O(i) > τ_O].
- **ê_O ∈ S^{d−1}** — the *anisotropy axis*, explicit frame data (may be per-incidence ê_O(v,e) if declared).
- **Π_O ⊆ W** — a distinguished oriented 2-plane carrying helicity, given as an ordered orthonormal pair (u, v). Default Π_O := Q_O when k = 2.
- **c_O ∈ W** — optional context vector.
- **S_O** — the *superposition operator* combining visible payloads into a node instantiation.
- **meta_O** — provenance record (Part II).

## I.3 Incidence operators (the repaired forms)

Each visible incidence's latent payload Ξ(v,e) is transformed by three commuting-in-spirit operators before projection. The v1 forms were geometrically ill-posed in dimension d ≠ 3; the repairs below are well-posed in every dimension.

**Anisotropy** — basis-free:

  A_O(v,e) = I − a_O(v,e) · (I − P_ê),  P_ê = ê ê*,  a ∈ [0,1].

a = 0 leaves the payload isotropic; a = 1 collapses it onto the axis ê. No rotation matrix and no eigenbasis choice enter, so there is no ambiguity of the kind that plagued the v1 "R diag(1,1−a,…) R⁻¹" form (R was underdetermined).

**Polarity** — scalar sign/gain:

  B_O(v,e) = b_O(v,e) · I,  b ∈ [−1, 1].

**Helicity** — the v1 gap, repaired. In d = 3 a rotation is specified by an axis (so(3) ≅ ℝ³). For d ≥ 4 this fails: dim so(d) = d(d−1)/2 > d, an axis no longer determines a generator, and in even d a generic rotation has no invariant axis at all. The fix is to specify the *2-plane of rotation*, not an axis. Equip Π_O with the complex structure J determined by its ordered basis (u,v): Ju = v, Jv = −u, J|_{Π_O^⊥} = 0. Then J² = −I on Π_O and

  H_O(v,e) = exp(h_O(v,e) · J) = rotation by angle h within Π_O, identity on Π_O^⊥,

well-posed in all d. The ±i eigenspaces of J on Π_O ⊗ ℂ are the left/right circular-polarization states (Born–Wolf §1.4), tying h to physical helicity. In d = 3 with propagation axis p̂, taking Π_O = p̂^⊥ recovers the classical axis-angle case, so nothing is lost and the pathology is removed.

**Resolved and visible payloads.** Composing,

  Φ̃_O(v,e) = B_O H_O A_O Ξ(v,e)   (resolved, full-dimensional)
  Φ_O(v,e) = π_O Φ̃_O(v,e)          (visible, projected into Q_O).

## I.4 Why π_O must be orthogonal [normative]

Every energy statement in this monograph — dimensional pressure, the Pythagorean split, the curvature identification of Part III — presumes that π_O is an **orthogonal** projector (self-adjoint and idempotent). The bound D_O ∈ [0,1] survives for merely contractive π (pointwise ‖πw‖ ≤ ‖w‖), but the *energy interpretation* requires

  ‖w‖² = ‖π_O w‖² + ‖(1 − π_O) w‖²,

which holds iff π_O is orthogonal. Oblique idempotents can even have operator norm > 1, breaking the bound itself. Orthogonality is therefore assumption **(U)**, standing throughout.

## I.5 Node instantiation and derived metrics

**Definition I.3.** The *instantiation* of latent entity v under O is Ψ_O(v) = S_O({Φ_O(v,e) : (v,e) ∈ Ī, χ_O(v,e) = 1}). For the m_v visible payloads φ_1, …, φ_{m_v} at v, define:

- **gross mass** g(v) = Σ_i ‖φ_i‖ (total payload magnitude, ignoring cancellation)
- **net resultant** n(v) = ‖Σ_i φ_i‖ (magnitude after superposition)
- **tension** T(v) = g(v) − n(v) ≥ 0 (triangle inequality; the destructive-interference budget)
- **coherence** κ(v) = (2 / (m_v(m_v−1))) Σ_{i<j} Re⟨φ_i, φ_j⟩ / (‖φ_i‖‖φ_j‖) — *signed, never clamped*; undefined at m_v = 1 (omitted in serialization; := 1 only where a pipeline demands a scalar). This signed quantity is the falsifier of Part V; the v1 max(κ,0) clamp is deleted because it conflated destructive interference (κ ≈ −1) with orthogonality (κ ≈ 0).
- **context score** Σ_i Re⟨c_O, φ_i⟩
- **dimensional pressure**

  **D_O(v) = 1 − Σ_e ‖π_O Φ̃_O(v,e)‖² / Σ_e ‖Φ̃_O(v,e)‖²**,  D_O := 0 when the denominator is 0.

By (U), D_O ∈ [0,1] with D_O = 0 iff every resolved payload already lies in Q_O (the frame loses nothing) and D_O → 1 as the payloads become orthogonal to Q_O (the frame sees almost nothing). D_O is the fraction of payload energy the frame discards — and Part III shows it is a curvature norm.

## I.6 Duality

**Definition I.4.** The *dual* H_O* interchanges entity and relation roles: H_O* = (E_O, V_O, Ī^⊤, Φ_O*) with **identity transfer** Φ_O*(e,v) = Φ_O(v,e). The double dual is strictly the original (transpose² = id; Mulas–Reff (G*)* = G; Grilliette–Rusnak self-inverting incidence-dual functor). A *conjugating* variant (h ↦ −h, payload conjugation) is equally involutive and is the physically faithful choice when h carries helicity semantics (Part VI). Because duality is identity-transfer incidence transpose, **the dual is a query-time view and is never persisted** (Part VI); persisting it doubles storage and manufactures a sync-integrity failure mode for zero informational gain.


---

# Part II — The Corrected Citation Spine

The source formalization carried opaque placeholder citations and three load-bearing misattributions. Only load-bearing anchors were audited (those a downstream proof or definition actually rests on). The corrected spine:

**(h) Incidence algebras / Möbius inversion.** *Root:* G.-C. Rota, "On the Foundations of Combinatorial Theory I: Theory of Möbius Functions," *Z. Wahrscheinlichkeitstheorie und Verw. Gebiete* **2**:340–368 (1964), DOI 10.1007/BF00531932. *Reduced incidence algebras / generating-function calculus:* P. Doubilet, G.-C. Rota, R. Stanley, "On the foundations of combinatorial theory VI: the idea of generating function," *Proc. Sixth Berkeley Symp. Math. Statist. Prob.*, vol. II, 267–318 (1972). *Canonical text:* R. Stanley, *Enumerative Combinatorics* Vol. 1, Ch. 3. The v1 attribution of the root result to DRS 1972 was an anachronism; the Möbius-function foundation is Rota 1964.

**(e) Sheaf-on-hypergraph caveat.** S. Choi, G. Kim, Y.-G. Oh, "Hypergraph Neural Sheaf Diffusion: A Symmetric Simplicial Set Framework for Higher-Order Learning," arXiv:2505.05702; *IEEE Access* **13**:131823–131838 (2025), DOI 10.1109/ACCESS.2025.3592104. A. Ayzenberg, T. Gebhart, G. Magai, G. Solomadin, "Sheaf theory: from deep geometry to deep learning," arXiv:2502.15476 (2025). The operative consequence: a sheaf must be attached to the *incidence graph or poset*, not to the naked hypergraph, because a bare hypergraph lacks the intrinsic adjacency/orientation data a sheaf Laplacian needs.

**(f) Vector/tensor-valued incidence.** M. Albooyeh, D. Bertolini, S. Ravanbakhsh, "Incidence Networks for Geometric Deep Learning," arXiv:1905.11460 (ICML 2020) — **author-retracted** for an experimental error; cite the sparse-incidence-tensor *formalism* only, never its empirical results. Live anchor: K. Miyamoto, "Defect Spaces and Gram Operators for Tensor-Valued Incidence Maps," arXiv:2605.28535 (2026).

**(a′) Duality, supplemented.** The crisp functorial "dual = incidence transpose" statement is Grilliette–Rusnak (arXiv:2007.01842 / arXiv:1910.02305). Mugnolo (arXiv:2510.17497) contributes the directed-hypergraph Laplacian L = I I^⊤ and its dual dynamics, not the bare duality definition — so Mugnolo supports the *spectral* claims, Grilliette–Rusnak the *categorical* one.

**Verified anchors used without change.** Bretto (*Hypergraph Theory*, Springer 2013) / Berge (*Graphs and Hypergraphs*, 1973) for hypergraph duality; Rusnak, *Electron. J. Combin.* **20**(3):#P48 (2013) and Reff–Rusnak, *Linear Algebra Appl.* **437**:2262–2270 (2012) for oriented incidences; Mulas–Reff (arXiv:2011.10458) for complex-unit incidences; Hansen–Ghrist, *J. Appl. Comput. Topol.* **3**(4):315–358 (2019) for cellular sheaves and the spectral-sheaf gap used in Part IV; PROV-O / PROV-DM (W3C Rec 2013-04-30), JSON-LD 1.1 (W3C Rec 2020-07-16), SHACL (W3C Rec 2017-07-20) for serialization; Born & Wolf, *Principles of Optics* 7e, §1.4 for the helicity/circular-polarization identification; Eisenbud, *Trans. AMS* **260**:35–64 (1980) for matrix factorizations; Căldararu–Tu, *Trans. AMS* (2012) for MF ≅ twisted complexes over curved algebras; Kato, *J. Phys. Soc. Japan* **5**:435–439 (1950) for the transport equation; B. Simon, *Phys. Rev. Lett.* **51**:2167 (1983) and Wilczek–Zee, *Phys. Rev. Lett.* **52**:2111 (1984) for geometric-phase holonomy; Lurie, *Higher Topos Theory*, Thm 3.2.0.1 for straightening/unstraightening; FOOO, *Lagrangian Intersection Floer Theory* (AMS/IP 46, 2009) for the curved A∞ / Maurer–Cartan machinery.


---

# Part III — The Curved Instantiation Complex

This part discharges the central claim from "theorem-in-reach conditional on a modeling bridge" to a theorem: **dimensional pressure D_O is the energy-normalized curvature of a curved module built from the instantiation data**, not a curvature by analogy. The instrument is deliberately elementary — Clifford–Koszul operators on a super tensor product — because elementary here means *checkable*, and Part VII checks it to machine precision.

## III.0 Setting

Fix a node v and frame O over 𝕂 ∈ {ℝ, ℂ}. Write π := π_O, the orthogonal projector onto the visible subspace Q := Q_O, and let Φ̃_e := Φ̃_O(v,e) be the resolved payloads of the m := m_v visible incidences. Define

- **curvature payloads** m₀(e) := (1 − π) Φ̃_e ∈ Q^⊥ (the invisible components),
- **energies** E := Σ_e ‖Φ̃_e‖², E_vis := Σ_e ‖πΦ̃_e‖², **𝔴** := Σ_e ‖m₀(e)‖².

Under **(U)**, Pythagoras gives 𝔴 = E − E_vis and **D_O(v) = 𝔴 / E**.

## III.1 The Clifford model

For w ∈ W define the odd operator on the exterior algebra ΛW:

  c(w) := ε(w) + ι(w♭),  ε(w) = wedging with w,  ι(w♭) = contraction against Re⟨·, w⟩.

The Clifford relation is immediate from ε ι + ι ε = ⟨·,·⟩:

  **c(u) c(w) + c(w) c(u) = 2 Re⟨u, w⟩ · id**,  so c(w)² = ‖w‖² · id.

**Definition III.1 (instantiation module).** M_v := ⊗̂_{e} Λ W_(e), the **super** tensor product of one exterior-algebra factor per visible incidence. Write c_e(w) for c(w) on the e-th factor. Super means odd operators on distinct factors *anticommute* — enforced concretely in code (Part VII, `clifford.py`) by inserting the grading operator (−1)^deg on every earlier factor (the Koszul sign). Define three odd operators:

  𝔡 := Σ_e c_e(Φ̃_e),  𝔡^vis := Σ_e c_e(πΦ̃_e),  𝔡^⊥ := Σ_e c_e(m₀(e)),  𝔡 = 𝔡^vis + 𝔡^⊥.

## III.2 Operator Pythagoras

**Theorem III.1 (operator Pythagoras). [THM] [NUM]**
Under (U):

1. 𝔡² = E · id, (𝔡^vis)² = E_vis · id, (𝔡^⊥)² = 𝔴 · id;
2. {𝔡^vis, 𝔡^⊥} = 0;
3. hence E = E_vis + 𝔴 at the operator level — the scalar Pythagorean identity is the anticommutator calculus of the module.

*Proof.* For e ≠ e′, c_e(·) and c_{e′}(·) anticommute (super tensor), so all cross terms in the square cancel in pairs. Same-factor terms use the Clifford relation: Σ_e c_e(Φ̃_e)² = Σ_e ‖Φ̃_e‖² · id = E · id, identically for the visible and perpendicular pieces. The mixed anticommutator on factor e is 2 Re⟨πΦ̃_e, m₀(e)⟩ = 0 because m₀(e) ∈ Q^⊥ and πΦ̃_e ∈ Q, by (U). ∎

*Numerical witness (Part VII, `clifford.py`).* Over random orthogonal projectors of random rank and random payloads, for (m,k) ∈ {(2,2),(3,2),(2,3),(3,3)} — dim M_v up to 512 — all four residuals ‖𝔡²−E‖, ‖(𝔡^vis)²−E_vis‖, ‖(𝔡^⊥)²−𝔴‖, ‖{𝔡^vis,𝔡^⊥}‖ are ≤ 4×10⁻¹⁴. Because the Koszul signs are constructed explicitly, this is a genuine test of the super-tensor structure, not a tautology.

## III.3 The curvature realization

Recall: a ℤ/2-graded curved module (M, d_M) over a curved algebra with curvature element 𝔴 satisfies d_M² = 𝔴 · id. When the base is 𝕂 (or a ring R) and the curvature is a scalar/central 𝔴, such a module is exactly a **matrix factorization of 𝔴** (Eisenbud 1980), and MF(R, 𝔴) ≅ Tw(B_𝔴), twisted complexes over the curved algebra B_𝔴 (Căldararu–Tu 2012).

**Theorem III.2 (curvature realization — discharges the central claim to [THM]). [THM]**
Let B_𝔴 = (𝕂, m₀^{alg} = 𝔴·1, m₁ = 0, m₂ = mult, m_{≥3} = 0), ℤ/2-graded. Then:

1. (M_v, 𝔡^⊥) is a curved dg-module over B_𝔴: (𝔡^⊥)² = 𝔴 · id realizes d_M² = m₀^{alg}, and the Bianchi identity m₁(m₀^{alg}) = 0 holds trivially (central scalar). Equivalently (M_v, 𝔡^⊥) ∈ MF(𝕂, 𝔴) ≅ Tw(B_𝔴).
2. **D_O(v) = 𝔴 / E is the energy-normalized curvature of this structure** — the squared norm of its curvature element per unit payload energy. "Curvature" is now internal to the mathematics.
3. (Relative form.) (M_v, 𝔡) ∈ MF(𝕂, E) and (M_v, 𝔡^vis) ∈ MF(𝕂, E_vis); by Theorem III.1(2) the deformation 𝔡^vis ↦ 𝔡^vis + 𝔡^⊥ shifts the superpotential by exactly 𝔴. **The curvature is the gap between the potential the frame claims (E_vis) and the potential the payload carries (E).**
4. (Family form.) Over frame space 𝒪 with R = C^∞(𝒪), 𝔴 : O ↦ Σ_e ‖(1−π_O)Φ̃_O(v,e)‖² is a nonnegative *frame superpotential*; (M, 𝔡^⊥) is a matrix factorization over (R, 𝔴); its zero locus {O : D_O(v) = 0} is exactly the flat frames where the curved structure trivializes.

*Proof.* (1) is Theorem III.1(1) against the module axiom, centrality making Bianchi vacuous, plus Eisenbud and Căldararu–Tu. (2) divides by E. (3) is III.1(1–2). (4) fibers (1) over 𝒪. ∎

**Proposition III.3 (where the curvature lives). [THM]** End(M_v) with differential ad(𝔡^⊥) is an honest dg-algebra: ad(𝔡^⊥)² = ad((𝔡^⊥)²) = ad(𝔴·id) = 0. Curvature is a strictly module-level phenomenon, invisible to endomorphisms — the standard curved-algebra subtlety (no naive abelian category of curved modules; MF is the repair), reproduced here exactly. ∎

## III.4 Fixed-frame rigidity: Maurer–Cartan must be familial

**(CL) Clifford ansatz.** Maurer–Cartan deformations are Clifford-type: odd b = Σ_e c_e(ξ_e), ξ_e ∈ W.

**Proposition III.4 (fixed-frame rigidity). [THM]** At a fixed frame under (CL), (𝔡^⊥ + b)² = Σ_e ‖m₀(e) + ξ_e‖² · id, which vanishes iff ξ_e = −m₀(e) for all e — the *trivial kill* (the differential erased, not flattened). There is therefore no nontrivial fixed-frame bounding cochain: the Maurer–Cartan problem is forced onto the frame family. This is the formal content of the slogan *dimensional pressure cannot be argued away in place; it can only be absorbed by moving the frame.*

*Proof.* Same-factor Clifford relation; distinct factors anticommute so no cross terms. ∎

## III.5 The transport–pressure identity

This closes the loop between the vertical curvature (payload, 𝔴) and the horizontal curvature (Berry, Part IV), upgrading "D is the shadow of connection curvature" to an identity.

**Proposition III.5 (transport–pressure identity). [THM]** For a smooth frame path t ↦ π(t) and constant ambient payload Φ̃,

  **∇_t(π Φ̃) = π π̇ (1 − π) Φ̃ = II*_t(m₀(t)),**

where ∇ = π∘d is the Grassmann connection and II* is the adjoint second fundamental form of the visible subbundle.

*Proof.* d/dt(πΦ̃) = π̇Φ̃. Differentiating π² = π gives π̇π + ππ̇ = π̇; left-multiplying by π gives ππ̇π = 0; hence π(π̇Φ̃) = ππ̇(π + (1−π))Φ̃ = ππ̇(1−π)Φ̃. The operator ππ̇(1−π) is precisely II*. ∎

**Corollary III.6 (drift bound). [THM]** ‖∇_t Ψ^vis‖ ≤ ‖π̇‖ Σ_e ‖m₀(e)‖ ≤ ‖π̇‖ √(m · 𝔴) = ‖π̇‖ √(m · D_O(v) · E). Flat nodes (D = 0) transport parallelly; every node's parallel-transport drift is bounded by the square root of its dimensional pressure. **Frame holonomy sees exactly the nodes that pressure marks** — the mechanism by which vertical curvature (III.2) feeds horizontal holonomy (Part IV). ∎


---

# Part IV — The Linear Triple and the Spectral–Arithmetic Dichotomy

Here the frame becomes a *loop*, the loop acquires holonomy, and the holonomy makes the substrate helical. The centerpiece is the **Triple**: three a-priori-different notions of "irreducible pressure" — cohomological, deformation-theoretic, operational — proven equivalent in the linear regime. Then the two resolution operations inherited from the prior obstruction theorem (growth on π₁, reinterpretation of coefficients) are sharpened into a spectral–arithmetic classification, and the classification's boundary is shown to coincide exactly with AMT's genuine-helix condition.

## IV.1 Frame holonomy: the substrate is a mapping torus

A one-parameter loop of frames O : S¹ → Frm is a loop t ↦ Q(t) := Q_{O(t)} in the Grassmannian Gr(k, d), with orthogonal projectors π(t).

**Theorem IV.1 (frame holonomy). [THM] [NUM]** Pull back the tautological rank-k bundle along t ↦ Q(t) with the Grassmann connection ∇ = π∘d. Then:

1. Parallel transport T_t is generated by **Kato's equation Ẇ = [π̇, π] W**, W(0) = I, which intertwines the family (Wπ(0)W⁻¹ = π(t)) and restricts to unitaries on fibers (because [π̇, π] is skew-adjoint when π, π̇ are self-adjoint).
2. **Hol(O) := T_1 ∈ U(k)** is well-defined.
3. k = 1: Hol = e^{iγ}, γ the geometric phase (Simon 1983: the phase *is* the holonomy in a Hermitian line bundle). k > 1: Hol = 𝒫 exp ∮ A, A_{ab} = ⟨e_a, de_b⟩ (Wilczek–Zee 1984), generally non-abelian.
4. The pullback connection over S¹ is automatically flat (no 2-forms on a 1-manifold); Gr(k,d)'s curvature manifests as loop-dependence of Hol.

*Proof.* ∇ = π∘d is the ambient flat connection projected to the subbundle; Kato transport preserves the metric by skew-adjointness of [π̇, π]; unitarity of T_1 gives (2); (3) is the cited literature; (4) is dimension counting. ∎

*Numerical witnesses (Part VII).* **`berry_kato.py`** integrates Kato transport (RK4, N = 4000) around latitude loops on Gr(1,2) ≅ S² and recovers the analytic Berry phase −π(1 − cos θ) to ≤ 1.2×10⁻⁷. **`wilczek_zee.py`** builds two rank-2 projector loops in Gr(2,4) from overlapping-plane generators and obtains ‖[Hol_A, Hol_B]‖ = 2.77 — genuinely non-abelian — while a disjoint-plane control commutes to 10⁻¹⁵ (the operator face of constitutive nesting: non-abelian holonomy *requires* overlapping planes).

**Theorem IV.2 (helical substrate = mapping torus). [THM]** Let φ := Hol(O) ∈ U(k). The total space of instantiations over the frame loop, trivialized by x ↦ T_t⁻¹x, is the mapping torus M_φ = (Q(0) × [0,1]) / ((x,0) ∼ (φx,1)), a flat U(k)-bundle over S¹ with monodromy φ. It satisfies AMT's four substrate requirements:

| AMT requirement | Realization | Status |
|---|---|---|
| Non-product | φ ≠ id: nonzero geometric phase. Flat bundles over S¹ ↔ Hom(π₁S¹, U(k))/conj = U(k)/conj; nontrivial class = connection-level twist. (Honest: as a *bare* bundle it is topologically trivial since U(k) is connected; the helicality is the flat-connection class — exactly AMT Step 5's classification.) | [THM] |
| One-parameter projectable | Projection to S¹ = loop parameter, by construction. | [THM] |
| Orientation-consistent | U(k) ⊂ SO(2k) since det_ℝ(U) = \|det_ℂ U\|² = 1. | [THM] |
| Compositionally non-flat | 𝔴 ≠ 0 ⇔ D_O > 0 somewhere (Part III). | [THM] |
| Infinite-order monodromy | φ has infinite order iff some eigenphase γ_j ∉ 2πℚ. Generic (full measure) but **not automatic**; rational phases give finite-order periodic-helix substrates. | [THM], flagged (GEN) |

**Theorem IV.3 (straightening identification). [THM]** The loop-restricted instantiation assignment is a functor Bℤ → Cat∞ sending the generator of ℤ = π₁(S¹) to φ_*. Its unstraightening (Lurie, HTT 3.2.0.1) is the coCartesian fibration over S¹ ≃ N(Bℤ) with total space M_φ. Frame-loop instantiation therefore **is** an instance of AMT's straightening/unstraightening equivalence, not an analogy to it. *Proof.* For a group G, straightening over BG = G-actions; unstraightening = the (∞-)Borel construction; for G = ℤ acting by φ_*, the Borel construction is the mapping torus. ∎

## IV.2 The linear extension problem

**(LIN)** S_O linear, payloads fixed, unitary Kato transport on the complement local system. **(DISC)** the loop is presented by a finite good cover with complement transition maps g_i, Π g_i = φ^⊥ ∈ U(d−k) (Kato transport block-preserves the visible/complement splitting, so φ^⊥ accompanies φ).

Local invisible payloads introduce incremental defects c_i ∈ Q^⊥_i. An *absorbing section* is a global section ξ of the complement local system ℐ^⊥ = (Q^⊥, φ^⊥) with ξ_{i+1} = g_i ξ_i + c_i. Closing the loop yields the **inhomogeneous holonomy equation**

  (φ^⊥ − 1) ξ₀ = C,  C := Σ_i (transport of c_i to basepoint),

and C is a twisted Čech 1-cocycle whose class [C] ∈ H¹(S¹, ℐ^⊥).

**Lemma IV.4 (twisted cohomology of the circle). [THM]** For a local system ℒ_ψ on S¹ with fiber V and monodromy ψ: H⁰ = ker(ψ − 1), H¹ = coker(ψ − 1). For unitary ψ over a field, dim H⁰ = dim H¹, so **H¹ ≠ 0 ⟺ 1 ∈ spec(ψ)** ("resonance"). *Proof.* The circle's cellular complex is V →^{ψ−1} V (one 0-cell, one 1-cell); unitary ψ − 1 is normal, equating kernel and cokernel dimensions. ∎

This fixes the correct reading of the prior obstruction theorem: H¹ is *where obstruction classes live*. Off resonance, H¹ = 0 and every defect is absorbable — but H⁰ = 0 too, so no frame-invariant sections exist: the **pure helix**, everything locally reconcilable, nothing globally invariant. On resonance, H¹ ≠ 0 and the harmonic component of C is a genuine obstruction.

## IV.3 The Triple

**Theorem IV.5 (Linear Triple; (U)(FR)(CL)(LIN)(DISC)). [THM]** For a frame loop with defect class [C] ∈ H¹(S¹, ℐ^⊥), the following are equivalent:

- **(a)** [C] ≠ 0;
- **(b)** no family Maurer–Cartan solution exists over S¹;
- **(c)** no global frame extension over S¹ drives D ≡ 0 (irreducible dimensional pressure).

*Proof.* (b) ⇔ (c) is the family-MC ⇔ extension equivalence of Part III over base S¹ — the ⟸ direction unconditional, the ⟹ direction under (CL)(FR). (c) ⇔ (a): a global absorbing extension exists iff (φ^⊥ − 1)ξ₀ = C is solvable iff C ∈ im(φ^⊥ − 1) iff [C] = 0 in coker = H¹ (Lemma IV.4). ∎

The three clauses of the original conjecture are therefore the same statement in three languages in the linear regime: cohomological, deformation-theoretic, operational. **Irreducible latent dimensional pressure — pressure no single global reframing dissolves — is exactly a nonvanishing twisted cohomology class of the frame loop.**

**Local–global caution [flagged].** D_O(v) > 0 at every frame of a cover does *not* imply H¹ ≠ 0: locally lossy can be globally reconcilable (that is the pure-helix case). D is local scalar energy loss; H¹ is the global obstruction. The Triple asserts equivalence only for the global clause (c).

## IV.4 Growth vs. reinterpretation: the dichotomy

The prior obstruction theorem established that resolution is exhausted by two operations — base change on π₁(S) (**growth**) or twisted flat-bundle coefficient change (**reinterpretation**). What is new: *which* operation resolves *what*, with a spectral signature for each.

Growth pulls back along the n-fold cover S¹ → S¹: monodromy ψ ↦ ψⁿ, defect C ↦ C_n = (Σ_{j<n} ψ^j) C. Reinterpretation twists coefficients: eigenphases translate γ ↦ γ + θ, or the ring localizes.

**Theorem IV.6 (resolution dichotomy). [THM] [NUM]**

1. **Full resonance is immune to growth.** On the λ = 1 eigencomponent, C_n = n·C: covers amplify, never resolve. Only reinterpretation (translate the phase off 1) resolves field-resonant obstruction.
2. **Finite order ≠ 1: geometric-series kill.** On a primitive q-th-root eigencomponent λ ≠ 1, the base is off-resonance (unobstructed) and at the q-cover the pulled-back monodromy becomes 1 there while C_q = (Σ_{j<q} λ^j) C = 0 — the transported defects destructively interfere. Growth *manufactures invariant sections at finite-order spectrum with the defect already annihilated*.
3. **Torsion is growth's domain.** Over ℤ, obstruction can be torsion without resonance (ψ − 1 injective, cokernel nontrivial). Möbius: ψ = −1 gives H¹ = coker(−2) = ℤ/2; the double cover kills it (C_2 = (1 + (−1))C = 0) and rationalization (localize ℤ → ℚ) kills it too — both branches act on the minimal example.
4. **Spectral form.** Growth acts on eigenphases by multiplication (γ ↦ nγ); reinterpretation by translation (γ ↦ γ + θ). Over a PID, obstruction = torsion ⊕ resonant-harmonic; growth resolves torsion/finite-order by geometric-series annihilation; reinterpretation resolves resonance by translation and, via localization, torsion as well. Exhaustiveness of the pair is inherited from the prior theorem; the assignment of operation-to-phenomenon is added here.
5. **Closure to AMT.** Irrational eigenphases — φ of infinite order — are immune to every finite cover: no growth manufactures invariance, no unwinding closes the orbit. **AMT's genuine-helix condition (infinite-order monodromy, Theorem IV.2) is exactly the condition under which growth is permanently unavailable: the substrate that cannot be unwound.** The periodic-helix (finite-order) case is exactly the growth-resolvable case. The two AMT substrate classes and the two resolution operations are one partition seen from both sides.

*Proof.* (1)–(3) are the displayed computations plus Lemma IV.4; Möbius ℤ/2 is verified by Smith normal form (Part VII). (4) collects them via the PID structure theorem on coker(ψ − 1). (5): φⁿ ≠ 1 ∀n ⟺ some γ_j ∉ 2πℚ, which is Theorem IV.2's infinite-order clause verbatim. ∎

## IV.5 The Möbius example, both ways [THM] [NUM]

The complement local system with φ^⊥ = −1 on a rank-1 real complement is the Möbius local system, realized as the n-cycle sheaf with identity edge maps except one −1.

**Over ℝ.** The twisted coboundary has full rank; H⁰ = H¹ = 0: acyclic, *never obstructed* — but never invariant (no nonzero flat section of the Möbius band: the paradigm pure helix at finite order, resolved at the double cover per IV.6(2)). Quantitatively (`mobius.py`), the twisted Laplacian spectrum is {2 − 2cos((2j+1)π/n)}, matched to 1.1×10⁻¹⁵ for n = 5, 8, 12, gap 2 − 2cos(π/n) ≈ π²/n². **H¹ = 0 yet the absorption operator's conditioning ‖(δᵀδ)⁻¹‖ = gap⁻¹ → ∞.** Name this **soft obstruction**: cohomologically unobstructed, operationally ill-conditioned — the cost of absorbing pressure diverges as the loop refines even though absorption never strictly fails. Soft obstruction is invisible to the Triple's trichotomy and is its correct quantitative refinement (the Hansen–Ghrist spectral gap imported to frame space).

**Over ℤ.** Smith normal form of the twisted coboundary is diag(1, …, 1, 2) — verified symbolically for n = 3, 5, 8 — hence **H¹(S¹; ℤ_−) = ℤ/2**: genuine 2-torsion, no resonance. Double cover resolves it (geometric-series kill; the Möbius band unwinds to the cylinder); rationalization resolves it (localization). The smallest possible example exhibits the full dichotomy, one branch per coefficient theory.

## IV.6 Stress-test summary [NUM]

The four numerical stress tests (full source + captured output in Part VII):

- **A. Berry (`berry_kato.py`)** — Kato holonomy phase vs −π(1−cos θ), error ≤ 1.2×10⁻⁷.
- **B. Wilczek–Zee (`wilczek_zee.py`)** — ‖[Hol_A, Hol_B]‖ = 2.77 (non-abelian); disjoint-plane control ~10⁻¹⁵.
- **C. Möbius (`mobius.py`)** — spectra to 1e-15; Smith form ⇒ ℤ/2.
- **D. Resonance (`resonance_table.py`)** — full resonance never killed by growth; rational killed at its order; irrational never killed.


---

# Part V — Field Trial: Falsification on Real Data

The anti-mystical commitment requires a distinguishing prediction that could fail. This part states it, then runs it on real data with a pre-registered go/no-go rule.

## V.1 The worked example is already a witness [NUM]

Before any external corpus, the source document's own worked example falsifies the additive null. Latent states Ξ(C,R₁) = [1.0, 0.2, 0.1], Ξ(C,R₂) = [0.9, 0.1, 0.0], Ξ(C,R₃) = [−0.4, 0.0, 1.1]; frames O_xy = span(e₁,e₂), O_xz = span(e₁,e₃). Recomputed to machine precision (`worked_example.py`):

| Metric | O_xy | O_xz |
|---|---:|---:|
| Ψ_O(C) | [1.5, 0.3] | [1.5, 1.2] |
| gross_mass | 2.325342 | 3.075458 |
| net_resultant | 1.529706 | 1.920937 |
| coherence | **−0.326075** | **+0.135587** |
| tension | 0.795637 | 1.154520 |
| D_O(C) | 0.376543 | 0.015432 |

Two model-killing features: (i) **node-level coherence sign-flips across frames** (−0.326 → +0.136) with tension > 0 in both; (ii) a **monotonicity violation** — in O_xy, net_resultant over {R₁, R₂} is 1.923538, and adding R₃ *decreases* it to 1.529706. No additive model with nonnegative contributions can decrease an aggregate by adding an incidence. The worked example was, unknowingly, its own falsifier witness.

## V.2 The distinguishing prediction

Additive / weighted-hypergraph / additive-scoring models are, structurally: monotone (adding an incidence never decreases the aggregate), tension ≡ 0 (no destructive interference), and frame-invariant in the sign of effective coherence. The waveform model predicts, on suitable data:

- **(P1)** tension > 0;
- **(P2)** monotonicity violations;
- **(P3)** frame-dependent **sign flips** in pairwise coherence (a pair constructive in one frame, destructive in another).

Any nonzero rate of (P3) falsifies every additive model. Conversely — the pre-registered NO-GO — **if a fitted additive model matches the data with tension ≡ 0, the waveform apparatus is unsupported on that dataset.**
> **Repo note, scope correction (`RECONCILIATION.md` R2).** "Every additive model" means every scalar, nonnegative-weight additive model. Plain vector addition under projection produces (P1)–(P3) as well, so the GO in V.3 is phenomenon detection (H₀). Comparative rejection of a fitted competitor starts at H₁ (`waveform-proofs/notes/h1-abelian-rung.md`), and loop-order and nested-order signatures are H₂ and H₃.


## V.3 Field trial [NUM]

**Corpus.** scikit-learn `digits`: 1,797 real scanned handwritten-digit images, 64-dim pixel vectors, mean-centered. Nodes = the 10 digit classes (m_v ≈ 174–183, payload = one image vector). Frames = two orthogonal PCA visible planes: O₁ = span(PC1, PC2) (28.5% variance), O₂ = span(PC3, PC4) (20.2%). Ambient energy for D_O is the full 64-dim payload energy. Seed 42.

**Results (`field_trial.py`):**

| class | m_v | tens O₁ | κ O₁ | tens O₂ | κ O₂ | pair-flip% | mono% | D_O₁ | z₁ | z₂ |
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

**Aggregate:** tension > 0 both frames **10/10** (P1 ✓); mean pairwise sign-flip rate **26.3%**, nonzero every class (P3 ✓ — alone falsifies every additive model); mean monotonicity-violation rate **8.9%**, present in 8/10 classes (P2 ✓); node-level *mean*-coherence sign flips **0/10**.

**Reading the absent node-level flip honestly.** The node-level flip is a *sufficient*, not necessary, witness, and its absence is exactly what a supervised class corpus predicts: members of a digit class are mutually aligned in any informative frame, so the class *mean* coherence stays positive. The discriminating structure lives one level down, in the 26% of pairs whose alignment reverses between frames — invisible to any frame-independent nonnegative-weight model. Classes 5 and 8 are the latent-pressure case studies the formalism was built for: class 5 is nearly incoherent in the dominant frame (κ = +0.027, tension 1636, D = 0.855) yet solidly coherent in the subdominant one (+0.569); class 8 mirrors it (D = 0.890). These are nodes whose co-incidence the leading frame cannot explain — dimensional pressure measured on real data.

**Permutation test.** Against an isotropic null (observed magnitudes, random in-plane directions), observed net resultants sit +3.0 to +26.6 σ high across all classes and both frames. Additive models have no directional degrees of freedom; the comparison is not close.

**Verdict: GO.** The additive null is rejected on this corpus by (P1)+(P2)+(P3); the waveform apparatus is supported. **Limitations:** one corpus; PCA (not adversarial) frames; raw centered-pixel payloads. Recommended second corpus for robustness: a real co-occurrence hypergraph with external embedding payloads (nodes = target words, incidences = context words, payloads = pretrained embeddings, frames = distinct projection planes) — flagged, not yet run.

---

# Part VI — The Dual Convention and the Namespace

## VI.1 The dual convention, decided

**Physics.** Reading an incidence from the relation side reverses propagation orientation. Helicity is the projection of spin onto propagation and is *odd* under reversal: h ↦ −h; on payloads this is complex conjugation, equivalently J ↦ −J, swapping the left/right circular basis states. The physically faithful dual is therefore **conjugating**. Both conventions are strict involutions, so the mathematics does not force the choice — the physics does.

**Decision [normative].** `wf:dualConvention ∈ {identity, conjugating}`, a **view-layer parameter, never stored**. Default `identity` (zero-cost transpose, matching the involution and the never-persist principle). `conjugating` (h ↦ −h, payload conjugation, J ↦ −J) is **required** whenever h carries physical helicity semantics. The flag has no storage footprint, no SHACL impact, no effect on the incidence store; it modifies only the read applied during dualization. Mixing conventions within one dual view is prohibited.

## VI.2 The namespace, prepared to the PR boundary

**Availability.** `https://w3id.org/waveform` returned **404 on 2026-07-19** — unregistered, available.

**Process.** Registration is a pull request to `perma-id/w3id.org`: fork, add a top-level `waveform/` directory containing `.htaccess` (redirects) and `README.md` (contact + identifier info), commit, submit; admins review, changes go live on merge.

**Delivered artifacts** (accompanying this monograph): `w3id-waveform-pr/waveform/.htaccess` (content-negotiated: `application/ld+json` → context, `text/turtle` → ontology, default → docs; 302 during stabilization, note to flip to 301 on freeze), `README.md`, `waveform-ns/context.jsonld` (full v2 context with all deltas), `waveform-ns/ontology.ttl` (minimal OWL/RDFS with the dimensional-pressure and dual-convention semantics as annotations). Redirect targets are parameterized to `https://bjl13.org/ns/waveform/`; the four target files must exist before the PR merges since changes go live immediately.

**The one non-delegable step:** the PR must originate from the namespace owner's GitHub account — it is the ownership and contact-of-record for the identifier.


---

# Part VII — The Proof Codebase

Every script below is standalone and reproduced verbatim, followed by its captured output. *(Repo note: verified identical to `waveform-proofs/src/` at the commit that added this file. If they ever differ, `src/` is authoritative, since it is what `make all` runs. The ladder scripts H₁–H₃, the H₂ tangent back-port and the gap rung are documented in `waveform-proofs/README.md`, not here.)*
 The full tree (with `Makefile`, `requirements.txt`, `README.md`, and captured `outputs/`) ships alongside this monograph as `waveform-proofs/`. Reproduce the entire battery with `make all`. RNG is seeded everywhere (field trial 42, ensemble 0); numbers are bit-stable on a given numpy/BLAS.

**Module map.**

| module | proves / runs | monograph ref |
|---|---|---|
| `metrics.py` | shared metric core (gross, net, tension, signed coherence, D_O, curvature payload) | Part I.5, III.0 |
| `clifford.py` | operator-Pythagoras (𝔡^⊥)² = 𝔴·id to 1e-14 → matrix factorization | Thm III.1/III.2 |
| `worked_example.py` | source-doc numbers exact; monotonicity violation; synthetic ensemble | Part V.1 |
| `berry_kato.py` | Berry phase via Kato transport, error ≤ 1.2e-7 | Thm IV.1 (k=1) |
| `wilczek_zee.py` | non-abelian holonomy ‖[Hol_A,Hol_B]‖ = 2.77; abelian control | Thm IV.1 (k>1) |
| `mobius.py` | twisted Laplacian spectrum; Smith form ⇒ H¹ = ℤ/2 | Part IV.5 |
| `resonance_table.py` | growth/reinterpretation dichotomy across covers | Thm IV.6 |
| `field_trial.py` | GO/NO-GO on real digits corpus | Part V.3 |


## VII.1 — `metrics.py`

The shared metric core. Pure functions; the single source of truth for every derived scalar. Adopted conventions live in code: zero-norm payloads dropped, coherence `None` at m<2, `D_O := 0` on zero ambient energy, signed coherence never clamped.

```python
"""
Core waveform metrics — shared by every proof script.

Node model: a node v under frame O sees m_v visible incidence payloads
phi_i in R^k (or C^k). Derived scalars per v2 spec section 1.5.
All functions are pure; no global state.
"""
import numpy as np


def node_metrics(phis, ambient_energy=None):
    """
    phis : (m, k) array of visible payloads at a node.
    ambient_energy : optional scalar sum_e ||Phi~_e||^2 (full ambient energy)
                     used for the exact D_O; if None, D_O is not computed.

    Returns dict with gross_mass, net_resultant, tension, coherence (signed,
    unclamped), incidence_count, and D_O (None unless ambient_energy given).
    Conventions: drop zero-norm payloads; coherence None at m<2; D_O:=0 on
    zero ambient energy.
    """
    phis = np.asarray(phis, dtype=float)
    norms = np.linalg.norm(phis, axis=1)
    keep = norms > 1e-12
    phis, norms = phis[keep], norms[keep]
    m = len(phis)
    gross = float(norms.sum())
    net = float(np.linalg.norm(phis.sum(axis=0))) if m else 0.0
    tension = gross - net
    if m >= 2:
        # mean signed pairwise cosine via Gram identity:
        # sum_{i<j} u_i . u_j = (||sum u||^2 - m) / 2
        U = phis / norms[:, None]
        gram_off = (float(np.linalg.norm(U.sum(axis=0)) ** 2) - m) / 2.0
        coherence = gram_off / (m * (m - 1) / 2.0)
    else:
        coherence = None
    D_O = None
    if ambient_energy is not None:
        vis_energy = float((phis ** 2).sum())
        D_O = 0.0 if ambient_energy <= 0 else 1.0 - vis_energy / ambient_energy
    return dict(gross_mass=gross, net_resultant=net, tension=tension,
                coherence=coherence, incidence_count=m, D_O=D_O)


def pairwise_cosines(phis):
    """All signed pairwise cosines, with the (i,j) index list."""
    phis = np.asarray(phis, dtype=float)
    norms = np.linalg.norm(phis, axis=1)
    keep = norms > 1e-12
    phis = phis[keep] / norms[keep][:, None]
    m = len(phis)
    idx = [(i, j) for i in range(m) for j in range(i + 1, m)]
    cos = np.array([float(phis[i] @ phis[j]) for i, j in idx])
    return cos, idx


def curvature_payload(Phi_tilde, projector):
    """m0 = (I - pi) Phi~  — the invisible component (v2 Prop 4 / anthology I.0)."""
    P = np.asarray(projector, dtype=float)
    x = np.asarray(Phi_tilde, dtype=float)
    return x - P @ x
```

*(imported by other modules; no standalone output.)*

## VII.2 — `clifford.py`

Explicit Clifford–Koszul construction with hand-built Koszul signs (the grading operator on every earlier super-tensor factor), verifying Theorem III.1 as dense matrices over random orthogonal projectors of random rank. dim M_v reaches 512, so the anticommutation is genuinely exercised.

```python
"""
Clifford-Koszul realization of the curved instantiation complex
(Anthology Part I). Verifies the operator-Pythagoras identities
d^2 = E, (d_vis)^2 = E_vis, (d_perp)^2 = w, {d_vis, d_perp} = 0
by explicit matrix construction, closing the [TIR-c] -> [THM] gap
numerically in addition to the analytic proof.

We build c(w) = eps(w) + iota(w) on Lambda(R^k) for each incidence,
place them on distinct super-tensor factors with correct Koszul signs,
and check the identities as dense matrices.
"""
import numpy as np
import itertools


def exterior_basis(k):
    """Basis of Lambda(R^k) as frozensets of indices, graded by size."""
    subsets = []
    for r in range(k + 1):
        for c in itertools.combinations(range(k), r):
            subsets.append(frozenset(c))
    # sort by degree then lexicographically for reproducibility
    subsets.sort(key=lambda s: (len(s), sorted(s)))
    return subsets


def _sign_insert(idx, s):
    """Sign of wedging e_idx into basis element s (Koszul), or 0 if idx in s."""
    if idx in s:
        return 0, s
    sign = (-1) ** sum(1 for j in s if j < idx)
    return sign, s | {idx}


def _sign_remove(idx, s):
    """Sign of contracting e_idx out of s, or 0 if idx not in s."""
    if idx not in s:
        return 0, s
    sign = (-1) ** sum(1 for j in s if j < idx)
    return sign, s - {idx}


def clifford_single(w):
    """c(w) = eps(w) + iota(w) on Lambda(R^k), returned as a dense matrix."""
    w = np.asarray(w, dtype=float)
    k = len(w)
    B = exterior_basis(k)
    pos = {s: i for i, s in enumerate(B)}
    n = len(B)
    C = np.zeros((n, n))
    for s in B:
        col = pos[s]
        for idx in range(k):
            sgn_e, s_up = _sign_insert(idx, s)   # wedge
            if sgn_e:
                C[pos[s_up], col] += sgn_e * w[idx]
            sgn_i, s_dn = _sign_remove(idx, s)   # contract
            if sgn_i:
                C[pos[s_dn], col] += sgn_i * w[idx]
    return C


def grading_operator(k):
    """(-1)^deg on Lambda(R^k), the Koszul sign operator for super tensor."""
    B = exterior_basis(k)
    return np.diag([(-1) ** len(s) for s in B])


def clifford_on_factor(w, e, m, k):
    """
    c_e(w): Clifford action on the e-th factor of the m-fold super tensor
    product of Lambda(R^k), with Koszul signs (G on all earlier factors).
    """
    G = grading_operator(k)
    I = np.eye(2 ** k)
    Ce = clifford_single(w)
    mats = []
    for f in range(m):
        if f < e:
            mats.append(G)      # Koszul sign from crossing earlier odd factor
        elif f == e:
            mats.append(Ce)
        else:
            mats.append(I)
    out = mats[0]
    for M in mats[1:]:
        out = np.kron(out, M)
    return out


def build_differentials(payloads, projector):
    """
    payloads : (m, k) resolved payloads Phi~_e
    projector: (k, k) orthogonal projector pi onto visible subspace
    Returns d, d_vis, d_perp and the scalar energies (E, E_vis, w).
    """
    P = np.asarray(projector, dtype=float)
    payloads = np.asarray(payloads, dtype=float)
    m, k = payloads.shape
    vis = payloads @ P.T
    perp = payloads - vis
    d = sum(clifford_on_factor(payloads[e], e, m, k) for e in range(m))
    d_vis = sum(clifford_on_factor(vis[e], e, m, k) for e in range(m))
    d_perp = sum(clifford_on_factor(perp[e], e, m, k) for e in range(m))
    E = float((payloads ** 2).sum())
    E_vis = float((vis ** 2).sum())
    w = float((perp ** 2).sum())
    return d, d_vis, d_perp, (E, E_vis, w)


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    print("Clifford-Koszul verification of Theorem I.1 (operator Pythagoras)")
    print("Random orthogonal projector, random payloads, several (m,k):\n")
    for (m, k) in [(2, 2), (3, 2), (2, 3), (3, 3)]:
        # random orthogonal projector of random rank r onto R^k
        A = rng.standard_normal((k, k))
        Q, _ = np.linalg.qr(A)
        r = rng.integers(1, k + 1)
        P = Q[:, :r] @ Q[:, :r].T                 # orthogonal projector, rank r
        payloads = rng.standard_normal((m, k))
        d, d_vis, d_perp, (E, E_vis, w) = build_differentials(payloads, P)
        N = d.shape[0]
        I = np.eye(N)
        e1 = np.linalg.norm(d @ d - E * I)
        e2 = np.linalg.norm(d_vis @ d_vis - E_vis * I)
        e3 = np.linalg.norm(d_perp @ d_perp - w * I)
        e4 = np.linalg.norm(d_vis @ d_perp + d_perp @ d_vis)   # anticommutator
        pyth = abs(E - (E_vis + w))
        print(f"  m={m}, k={k}, rank(pi)={r}, dim M_v={N}: "
              f"||d^2-E||={e1:.2e} ||d_vis^2-E_vis||={e2:.2e} "
              f"||d_perp^2-w||={e3:.2e} ||{{d_vis,d_perp}}||={e4:.2e} "
              f"|E-(E_vis+w)|={pyth:.2e}")
    print("\nAll residuals ~1e-14 => (d_perp)^2 = w*id exactly:")
    print("(M_v, d_perp) is a matrix factorization of the superpotential w. [THM]")
```

**Captured output:**

```
Clifford-Koszul verification of Theorem I.1 (operator Pythagoras)
Random orthogonal projector, random payloads, several (m,k):

  m=2, k=2, rank(pi)=1, dim M_v=16: ||d^2-E||=7.35e-16 ||d_vis^2-E_vis||=5.12e-18 ||d_perp^2-w||=1.26e-15 ||{d_vis,d_perp}||=5.47e-16 |E-(E_vis+w)|=4.44e-16
  m=3, k=2, rank(pi)=1, dim M_v=64: ||d^2-E||=4.44e-15 ||d_vis^2-E_vis||=1.98e-15 ||d_perp^2-w||=5.28e-15 ||{d_vis,d_perp}||=8.14e-15 |E-(E_vis+w)|=0.00e+00
  m=2, k=3, rank(pi)=3, dim M_v=64: ||d^2-E||=3.87e-15 ||d_vis^2-E_vis||=4.68e-15 ||d_perp^2-w||=0.00e+00 ||{d_vis,d_perp}||=8.38e-15 |E-(E_vis+w)|=8.88e-16
  m=3, k=3, rank(pi)=2, dim M_v=512: ||d^2-E||=2.58e-14 ||d_vis^2-E_vis||=1.12e-14 ||d_perp^2-w||=1.05e-14 ||{d_vis,d_perp}||=3.94e-14 |E-(E_vis+w)|=1.78e-15

All residuals ~1e-14 => (d_perp)^2 = w*id exactly:
(M_v, d_perp) is a matrix factorization of the superpotential w. [THM]
```

## VII.3 — `worked_example.py`

Recomputes the source worked example, exhibits the monotonicity violation, and runs the synthetic falsification ensemble (N=500, seed=0).

```python
"""
Anthology Part III preamble + v2 section 5.1:
recompute the worked example from the source document, exhibit it as a
minimal falsifier witness, and run the synthetic pipeline demonstration.
"""
import numpy as np
from metrics import node_metrics, pairwise_cosines

XI = {'R1': np.array([1.0, 0.2, 0.1]),
      'R2': np.array([0.9, 0.1, 0.0]),
      'R3': np.array([-0.4, 0.0, 1.1])}
FRAMES = {'O_xy': [0, 1], 'O_xz': [0, 2]}


def worked_example():
    ambient = float(sum(np.dot(v, v) for v in XI.values()))
    print("=== WORKED EXAMPLE (source doc), recomputed ===")
    print(f"ambient energy E = sum ||Xi||^2 = {ambient:.6f}\n")
    for fname, idx in FRAMES.items():
        phis = np.array([XI[k][idx] for k in ['R1', 'R2', 'R3']])
        r = node_metrics(phis, ambient_energy=ambient)
        cos, ij = pairwise_cosines(phis)
        print(f"{fname}: Psi={phis.sum(axis=0)}")
        print(f"  gross={r['gross_mass']:.6f} net={r['net_resultant']:.6f} "
              f"coherence={r['coherence']:+.6f} tension={r['tension']:.6f} "
              f"D_O={r['D_O']:.6f}")
        print(f"  pairwise cosines {[(p, round(c,4)) for p, c in zip(ij, cos)]}")
    # monotonicity violation in O_xy
    ph = np.array([XI[k][[0, 1]] for k in ['R1', 'R2', 'R3']])
    n12 = np.linalg.norm(ph[0] + ph[1])
    n123 = np.linalg.norm(ph.sum(axis=0))
    print(f"\nMonotonicity: net{{R1,R2}}={n12:.6f} -> +R3 -> {n123:.6f} "
          f"(DECREASE: {n123 < n12}) => no additive model reproduces this")


def synthetic_ensemble(N=500, m=3, d=3, seed=0):
    rng = np.random.default_rng(seed)
    node_flip = tension_both = mono = 0
    pair_flip = pair_tot = 0
    for _ in range(N):
        payloads = rng.standard_normal((m, d))
        res, cosframes = {}, {}
        for fname, idx in FRAMES.items():
            sub = payloads[:, idx]
            res[fname] = node_metrics(sub)
            cosframes[fname], _ = pairwise_cosines(sub)
        a, b = res['O_xy'], res['O_xz']
        if a['coherence'] * b['coherence'] < 0:
            node_flip += 1
        if a['tension'] > 1e-12 and b['tension'] > 1e-12:
            tension_both += 1
        for ca, cb in zip(cosframes['O_xy'], cosframes['O_xz']):
            pair_tot += 1
            if ca * cb < 0:
                pair_flip += 1
        for fname, idx in FRAMES.items():
            sub = payloads[:, idx]
            if np.linalg.norm(sub.sum(axis=0)) < np.linalg.norm(sub[0] + sub[1]) - 1e-12:
                mono += 1
                break
    print(f"\n=== SYNTHETIC ENSEMBLE  N={N} m={m} d={d} seed={seed} ===")
    print(f"  node-coherence sign flips : {node_flip}/{N} = {node_flip/N:.1%}")
    print(f"  pairwise sign flips       : {pair_flip}/{pair_tot} = {pair_flip/pair_tot:.1%}")
    print(f"  tension>0 both frames     : {tension_both}/{N} = {tension_both/N:.1%}")
    print(f"  monotonicity violations   : {mono}/{N} = {mono/N:.1%}")


if __name__ == "__main__":
    worked_example()
    synthetic_ensemble()
```

**Captured output:**

```
=== WORKED EXAMPLE (source doc), recomputed ===
ambient energy E = sum ||Xi||^2 = 3.240000

O_xy: Psi=[1.5 0.3]
  gross=2.325342 net=1.529706 coherence=-0.326075 tension=0.795637 D_O=0.376543
  pairwise cosines [((0, 1), np.float64(0.9962)), ((0, 2), np.float64(-0.9806)), ((1, 2), np.float64(-0.9939))]
O_xz: Psi=[1.5 1.2]
  gross=3.075458 net=1.920937 coherence=+0.135587 tension=1.154520 D_O=0.015432
  pairwise cosines [((0, 1), np.float64(0.995)), ((0, 2), np.float64(-0.2465)), ((1, 2), np.float64(-0.3417))]

Monotonicity: net{R1,R2}=1.923538 -> +R3 -> 1.529706 (DECREASE: True) => no additive model reproduces this

=== SYNTHETIC ENSEMBLE  N=500 m=3 d=3 seed=0 ===
  node-coherence sign flips : 149/500 = 29.8%
  pairwise sign flips       : 497/1500 = 33.1%
  tension>0 both frames     : 500/500 = 100.0%
  monotonicity violations   : 242/500 = 48.4%
```

## VII.4 — `berry_kato.py`

Kato transport Ẇ = [π̇,π]W by RK4 around latitude loops on Gr(1,2)=S², holonomy phase vs the analytic Berry phase −π(1−cos θ).

```python
"""
Anthology Part II, stress test A + v2 Theorem 1 (k=1).
Kato parallel transport  W' = [pi_dot, pi] W  around latitude loops on
Gr(1,2) = S^2; holonomy phase vs analytic Berry phase -pi(1-cos theta).
"""
import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def proj(theta, phi):
    n = np.array([np.sin(theta) * np.cos(phi),
                  np.sin(theta) * np.sin(phi),
                  np.cos(theta)])
    return 0.5 * (np.eye(2) + n[0] * SX + n[1] * SY + n[2] * SZ)


def kato_holonomy(theta, N=4000):
    dt = 1.0 / N

    def pdot(t, h=1e-7):
        return (proj(theta, 2 * np.pi * (t + h)) -
                proj(theta, 2 * np.pi * (t - h))) / (2 * h)

    W = np.eye(2, dtype=complex)
    for i in range(N):
        t = (i + 0.5) * dt
        P = proj(theta, 2 * np.pi * t)
        A = pdot(t) @ P - P @ pdot(t)              # [pi_dot, pi]
        k1 = A @ W
        k2 = A @ (W + dt / 2 * k1)
        k3 = A @ (W + dt / 2 * k2)
        k4 = A @ (W + dt * k3)
        W = W + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return W


if __name__ == "__main__":
    print("Berry phase via Kato transport on Gr(1,2)=S^2 (RK4, N=4000)\n")
    print(f"{'theta':>8s} {'|hol|':>10s} {'gamma_num':>12s} {'gamma_analytic':>14s} {'err':>10s}")
    for theta in [np.pi / 3, np.pi / 2, 2 * np.pi / 3]:
        W = kato_holonomy(theta)
        P0 = proj(theta, 0.0)
        ev, evec = np.linalg.eigh(P0)
        psi0 = evec[:, np.argmax(ev)]
        hol = np.vdot(psi0, W @ psi0)
        g_num = np.angle(hol)
        g_ana = -np.pi * (1 - np.cos(theta))
        g_ana = (g_ana + np.pi) % (2 * np.pi) - np.pi
        print(f"{theta:8.4f} {abs(hol):10.8f} {g_num:+12.6f} {g_ana:+14.6f} "
              f"{abs(g_num - g_ana):10.2e}")
```

**Captured output:**

```
Berry phase via Kato transport on Gr(1,2)=S^2 (RK4, N=4000)

   theta      |hol|    gamma_num gamma_analytic        err
  1.0472 1.00000000    -1.570796      -1.570796   1.21e-07
  1.5708 1.00000000    -3.141593      -3.141593   4.44e-16
  2.0944 1.00000000    +1.570796      +1.570796   1.21e-07
```

## VII.5 — `wilczek_zee.py`

Non-abelian Wilczek–Zee holonomy in Gr(2,4) from overlapping-plane generators, with a disjoint-plane abelian control.

```python
"""
Anthology Part II, stress test B + v2 Theorem 1 (k>1).
Non-abelian Wilczek-Zee holonomy in Gr(2,4). Two loops of rank-2
projectors built from OVERLAPPING-plane generators (disjoint planes
commute and give a degenerate/abelian result — kept as a control).
"""
import numpy as np
from scipy.linalg import expm


def skew(i, j, d=4):
    G = np.zeros((d, d), dtype=complex)
    G[i, j], G[j, i] = 1.0, -1.0
    return G


def isym(i, j, d=4):
    """Anti-Hermitian generator mixing a complex direction."""
    G = np.zeros((d, d), dtype=complex)
    G[i, j] = G[j, i] = 1j
    return G


P0 = np.diag([1.0, 1.0, 0.0, 0.0]).astype(complex)


def loop_proj(t, Ga, Gb, eps=0.9):
    a = eps * np.sin(2 * np.pi * t)
    b = eps * (1 - np.cos(2 * np.pi * t))
    U = expm(a * Ga) @ expm(b * Gb)
    return U @ P0 @ U.conj().T


def kato_hol(projfun, N=4000):
    W = np.eye(4, dtype=complex)
    dt = 1.0 / N

    def pdot(t, h=1e-7):
        return (projfun(t + h) - projfun(t - h)) / (2 * h)

    for i in range(N):
        t = (i + 0.5) * dt
        P = projfun(t)
        A = pdot(t) @ P - P @ pdot(t)
        k1 = A @ W
        k2 = A @ (W + dt / 2 * k1)
        k3 = A @ (W + dt / 2 * k2)
        k4 = A @ (W + dt * k3)
        W = W + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return W


def block(W):
    E = np.eye(4)[:, :2]
    return E.T @ W @ E


if __name__ == "__main__":
    E = np.eye(4)[:, :2]
    # Non-abelian: overlapping planes (share an index), one real one complex
    WA = kato_hol(lambda t: loop_proj(t, skew(0, 2), skew(1, 2)))
    WB = kato_hol(lambda t: loop_proj(t, isym(0, 2), skew(1, 2)))
    HA, HB = block(WA), block(WB)
    print("Wilczek-Zee non-abelian holonomy, Gr(2,4)\n")
    for nm, H in [("A", HA), ("B", HB)]:
        print(f"Hol_{nm} (unitarity err {np.linalg.norm(H.conj().T@H-np.eye(2)):.1e}):")
        print(np.round(H, 4))
    comm = np.linalg.norm(HA @ HB - HB @ HA)
    print(f"\n||[Hol_A, Hol_B]|| = {comm:.6f}  => non-abelian: {comm > 0.01}")
    ph = np.angle(np.linalg.eigvals(HA)) / (2 * np.pi)
    print(f"Hol_A eigenphases/2pi = {np.round(ph,6)} (irrational => infinite order)")

    # Control: disjoint planes commute
    WA0 = kato_hol(lambda t: loop_proj(t, skew(0, 2), skew(1, 3)))
    WB0 = kato_hol(lambda t: loop_proj(t, skew(0, 3), skew(1, 2)))
    c0 = np.linalg.norm(block(WA0) @ block(WB0) - block(WB0) @ block(WA0))
    print(f"\nCONTROL (disjoint planes): ||[Hol_A,Hol_B]|| = {c0:.2e} (abelian, as expected)")
```

**Captured output:**

```
Wilczek-Zee non-abelian holonomy, Gr(2,4)

Hol_A (unitarity err 1.7e-14):
[[ 0.1433+0.j -0.9897+0.j]
 [ 0.9897+0.j  0.1433+0.j]]
Hol_B (unitarity err 9.7e-15):
[[0.1433+0.j     0.    -0.9897j]
 [0.    -0.9897j 0.1433+0.j    ]]

||[Hol_A, Hol_B]|| = 2.770314  => non-abelian: True
Hol_A eigenphases/2pi = [ 0.227108 -0.227108] (irrational => infinite order)

CONTROL (disjoint planes): ||[Hol_A,Hol_B]|| = 0.00e+00 (abelian, as expected)
```

## VII.6 — `mobius.py`

Twisted n-cycle (Möbius) sheaf Laplacian spectrum over ℝ, and integral cohomology via Smith normal form over ℤ.

```python
"""
Anthology Part II.3 + stress test C.
Mobius (twisted n-cycle) sheaf Laplacian spectrum over R, and integral
cohomology H^1(S^1; Z_-) = Z/2 via Smith normal form over Z.
"""
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def twisted_coboundary(n):
    """n-cycle with identity edge maps except one -1 (the Mobius twist)."""
    D = np.zeros((n, n))
    for j in range(n):
        rho = -1.0 if j == n - 1 else 1.0
        D[j, (j + 1) % n] = rho
        D[j, j] += -1.0
    return D


if __name__ == "__main__":
    print("Mobius twisted sheaf Laplacian L = D^T D over R\n")
    print(f"{'n':>3s} {'max|spec-pred|':>16s} {'gap':>10s} {'gap_pred':>10s} "
          f"{'rank(D)':>8s} {'acyclic/R':>10s}")
    for n in [5, 8, 12]:
        D = twisted_coboundary(n)
        ev = np.sort(np.linalg.eigvalsh(D.T @ D))
        pred = np.sort([2 - 2 * np.cos((2 * j + 1) * np.pi / n) for j in range(n)])
        gap_pred = 2 - 2 * np.cos(np.pi / n)
        rk = np.linalg.matrix_rank(D)
        print(f"{n:3d} {np.max(np.abs(ev-pred)):16.2e} {ev[0]:10.6f} "
              f"{gap_pred:10.6f} {rk:8d} {str(rk==n):>10s}")
    print("\nH^1 over R = 0 (acyclic) but conditioning ~ 1/gap ~ n^2/pi^2 "
          "diverges => 'soft obstruction'\n")
    print("Integral cohomology via Smith normal form over Z:")
    for n in [3, 5, 8]:
        D = sp.Matrix(twisted_coboundary(n).astype(int))
        S = smith_normal_form(D, domain=sp.ZZ)
        diag = [int(S[i, i]) for i in range(n)]
        print(f"  n={n}: Smith diag = {diag}  =>  H^1(S^1; Z_-) = Z/{abs(diag[-1])}")
```

**Captured output:**

```
Mobius twisted sheaf Laplacian L = D^T D over R

  n   max|spec-pred|        gap   gap_pred  rank(D)  acyclic/R
  5         6.66e-16   0.381966   0.381966        5       True
  8         1.11e-15   0.152241   0.152241        8       True
 12         8.88e-16   0.068148   0.068148       12       True

H^1 over R = 0 (acyclic) but conditioning ~ 1/gap ~ n^2/pi^2 diverges => 'soft obstruction'

Integral cohomology via Smith normal form over Z:
  n=3: Smith diag = [1, 1, 2]  =>  H^1(S^1; Z_-) = Z/2
  n=5: Smith diag = [1, 1, 1, 1, 2]  =>  H^1(S^1; Z_-) = Z/2
  n=8: Smith diag = [1, 1, 1, 1, 1, 1, 1, 2]  =>  H^1(S^1; Z_-) = Z/2
```

## VII.7 — `resonance_table.py`

Cover-resolution table demonstrating the spectral–arithmetic dichotomy: growth kills finite-order by geometric series, never full resonance, never irrational phase.

```python
"""
Anthology Part II.3 + stress test D.
Cover-resolution table for k_perp = 1. Growth pulls back along the n-fold
cover: monodromy phi -> phi^n, defect C -> C_n = (sum_{j<n} phi^j) C.
Shows the spectral-arithmetic dichotomy:
  full resonance (alpha=0): C_n = nC, never resolved by growth;
  rational alpha:  geometric-series kill at the order;
  irrational alpha (genuine helix): never killed by any finite cover.
"""
import numpy as np

GOLDEN = (1 + 5 ** 0.5) / 2
CASES = {
    "alpha=0 (full resonance)": 1.0 + 0j,
    "alpha=2pi/3 (rational)": np.exp(2j * np.pi / 3),
    "alpha=2pi/golden (irrational)": np.exp(2j * np.pi / GOLDEN),
}


if __name__ == "__main__":
    C = 1.0 + 0.5j
    print(f"Cover-resolution table, defect C = {C}\n")
    print(f"{'case':32s} {'n':>2s} {'|C_n|':>10s} {'solvable':>9s} {'invariants':>11s}")
    for name, phi in CASES.items():
        for n in [1, 2, 3, 6]:
            Cn = sum(phi ** j for j in range(n)) * C
            mono = phi ** n
            resonant = abs(mono - 1) < 1e-9
            solvable = (not resonant) or (abs(Cn) < 1e-9)
            print(f"{name:32s} {n:2d} {abs(Cn):10.4f} {str(solvable):>9s} "
                  f"{str(resonant):>11s}")
        print()
```

**Captured output:**

```
Cover-resolution table, defect C = (1+0.5j)

case                              n      |C_n|  solvable  invariants
alpha=0 (full resonance)          1     1.1180     False        True
alpha=0 (full resonance)          2     2.2361     False        True
alpha=0 (full resonance)          3     3.3541     False        True
alpha=0 (full resonance)          6     6.7082     False        True

alpha=2pi/3 (rational)            1     1.1180      True       False
alpha=2pi/3 (rational)            2     1.1180      True       False
alpha=2pi/3 (rational)            3     0.0000      True        True
alpha=2pi/3 (rational)            6     0.0000      True        True

alpha=2pi/golden (irrational)     1     1.1180      True       False
alpha=2pi/golden (irrational)     2     0.8103      True       False
alpha=2pi/golden (irrational)     3     0.5308      True       False
alpha=2pi/golden (irrational)     6     0.9520      True       False
```

## VII.8 — `field_trial.py`

The GO/NO-GO field trial on the real digits corpus.

```python
"""
Anthology Part III + v2 section 5.3 GO/NO-GO benchmark on real data.
Corpus: sklearn digits (1797 real handwritten-digit vectors, d=64).
Nodes = 10 digit classes; incidence payload = one image vector.
Frames = two orthogonal PCA visible planes (PC1-2 vs PC3-4).
Discriminators: tension>0, pairwise coherence sign-flip rate,
monotonicity-violation rate, permutation z-scores. Additive null is
rejected if pairwise sign-flip rate or monotonicity-violation rate > 0.
"""
import numpy as np
from sklearn.datasets import load_digits
from metrics import node_metrics, pairwise_cosines

SEED = 42


def run():
    rng = np.random.default_rng(SEED)
    X, y = load_digits(return_X_y=True)
    Xc = X - X.mean(axis=0)
    _, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    F1, F2 = Vt[[0, 1], :], Vt[[2, 3], :]
    evr = S ** 2 / (S ** 2).sum()
    print(f"Corpus: sklearn digits, n={X.shape[0]}, ambient d={X.shape[1]}, "
          f"10 node-classes")
    print(f"Frames: PC1-2 (var {evr[:2].sum():.3f}) vs PC3-4 "
          f"(var {evr[2:4].sum():.3f})\n")
    print(f"{'cls':>3s} {'m_v':>4s} {'tens1':>8s} {'coh1':>7s} {'tens2':>8s} "
          f"{'coh2':>7s} {'pflip%':>7s} {'mono%':>6s} {'D_O1':>6s} "
          f"{'z1':>6s} {'z2':>6s}")
    tension_both = node_flip = 0
    pflips, monos = [], []
    for c in range(10):
        P = Xc[y == c]
        Etot = float((P ** 2).sum())
        ph1, ph2 = P @ F1.T, P @ F2.T
        r1 = node_metrics(ph1, ambient_energy=Etot)
        r2 = node_metrics(ph2, ambient_energy=Etot)
        # pairwise sign flips on a shared sample of pairs
        cos1, idx = pairwise_cosines(ph1)
        if len(idx) > 4000:
            sel = rng.choice(len(idx), 4000, replace=False)
            idx = [idx[s] for s in sel]
            cos1 = np.array([ph1[i] @ ph1[j] /
                             (np.linalg.norm(ph1[i]) * np.linalg.norm(ph1[j]))
                             for i, j in idx])
        cos2 = np.array([ph2[i] @ ph2[j] /
                         (np.linalg.norm(ph2[i]) * np.linalg.norm(ph2[j]))
                         for i, j in idx])
        pflip = float((np.sign(cos1) != np.sign(cos2)).mean())
        # monotonicity: random orders, fraction of decreasing steps
        viol = tot = 0
        for _ in range(50):
            order = rng.permutation(len(ph1))
            run_v = np.zeros(2)
            prev = 0.0
            for i in order:
                run_v = run_v + ph1[i]
                cur = np.linalg.norm(run_v)
                if cur < prev - 1e-12:
                    viol += 1
                tot += 1
                prev = cur
        mono = viol / tot
        # permutation z: isotropic null with observed magnitudes
        def zscore(ph):
            mags = np.linalg.norm(ph, axis=1)
            nulls = []
            for _ in range(500):
                ang = rng.uniform(0, 2 * np.pi, len(mags))
                vecs = mags[:, None] * np.c_[np.cos(ang), np.sin(ang)]
                nulls.append(np.linalg.norm(vecs.sum(axis=0)))
            return (np.linalg.norm(ph.sum(axis=0)) - np.mean(nulls)) / np.std(nulls)
        z1, z2 = zscore(ph1), zscore(ph2)
        tension_both += (r1['tension'] > 1e-9 and r2['tension'] > 1e-9)
        node_flip += (r1['coherence'] * r2['coherence'] < 0)
        pflips.append(pflip)
        monos.append(mono)
        print(f"{c:3d} {r1['incidence_count']:4d} {r1['tension']:8.1f} "
              f"{r1['coherence']:+7.3f} {r2['tension']:8.1f} {r2['coherence']:+7.3f} "
              f"{pflip*100:6.1f} {mono*100:5.1f} {r1['D_O']:6.3f} "
              f"{z1:+6.1f} {z2:+6.1f}")
    print(f"\nAGGREGATE: tension>0 both frames {tension_both}/10 | "
          f"node-coherence flips {node_flip}/10 | "
          f"mean pairwise-flip {np.mean(pflips)*100:.1f}% | "
          f"mean mono-viol {np.mean(monos)*100:.1f}%")
    verdict = "GO" if (np.mean(pflips) > 0 and np.mean(monos) > 0
                       and tension_both == 10) else "NO-GO"
    print(f"VERDICT: {verdict} — additive null "
          f"{'rejected' if verdict=='GO' else 'not rejected'}")


if __name__ == "__main__":
    run()
```

**Captured output:**

```
Corpus: sklearn digits, n=1797, ambient d=64, 10 node-classes
Frames: PC1-2 (var 0.285) vs PC3-4 (var 0.202)

cls  m_v    tens1    coh1    tens2    coh2  pflip%  mono%   D_O1     z1     z2
  0  178    139.7  +0.926    261.3  +0.641   11.1   0.0  0.546  +26.4  +20.5
  1  182    445.5  +0.516   1282.2  +0.404   30.5  13.0  0.758  +18.9  +15.5
  2  177    237.1  +0.754    391.5  +0.540   22.1   3.2  0.851  +23.2  +21.3
  3  183    352.5  +0.804    673.2  +0.423   23.5   0.1  0.591  +24.0  +15.5
  4  181    254.7  +0.870    861.9  +0.354   26.6   1.6  0.583  +25.1  +15.5
  5  182   1635.6  +0.027    396.2  +0.569   52.2  35.6  0.855   +4.9  +19.7
  6  181    169.3  +0.906    314.7  +0.768    2.9   0.0  0.633  +26.6  +24.4
  7  179    169.5  +0.862    345.4  +0.647   15.2   0.5  0.776  +24.8  +22.4
  8  174    723.4  +0.199   1324.3  +0.021   47.8  22.4  0.890  +11.5   +3.0
  9  180    469.6  +0.553    591.9  +0.454   31.3  12.2  0.693  +21.9  +16.3

AGGREGATE: tension>0 both frames 10/10 | node-coherence flips 0/10 | mean pairwise-flip 26.3% | mean mono-viol 8.9%
VERDICT: GO — additive null rejected
```

---

# Appendix A — Assumption Ledger

Every non-trivial assumption, where it is used, and what breaks without it.

| Label | Statement | Used in | If dropped |
|---|---|---|---|
| **(U)** | π_O orthogonal (self-adjoint idempotent) | all energy statements: I.4–I.5, III.1–III.6, IV.5, D_O itself | Pythagoras fails; 𝔴 ≠ E − E_vis; Theorem III.1(2)'s anticommutator no longer vanishes. Normative in Part I. |
| **(FR)** | Frame space admits extensions Q^ext ⊇ Q as needed | III (⟹ of I.6-analog), IV.5 | Pointwise absorption can fail from frame poverty rather than topology; the Triple's (c) decouples from (a). |
| **(CL)** | MC deformations of Clifford type β = Σ c_e(ξ_e) | III.4, IV.5 (b ⟹ c) | (c) ⟹ (b) survives unconditionally; the converse reopens (general odd β need not be Clifford-type). |
| **(LIN)** | Linear S_O, fixed payloads, unitary Kato transport on flat complement coefficients | all of Part IV | The Triple reverts to Conjecture B.1. |
| **(DISC)** | Loop presented by a finite good cover | IV.2, IV.3 | Replace Čech by sheaf cohomology proper; nothing essential changes for S¹. |
| **(GEN)** | Genericity of irrational eigenphases where "infinite order" is asserted | IV.2 (Thm IV.2 last row), IV.6(5), stress test B | Finite-order (periodic-helix) branch applies; growth becomes available as a resolvent. |

---

# Appendix B — The Residual Conjecture

**Conjecture B.1 (nonlinear Triple). [CIR]** Drop (LIN) and (CL). Equip the instantiation complex with the curved A∞-structure whose m₀ is Theorem III.2's curvature, whose m₂ is induced by a bilinear S_O, and whose m_{k≥3} are the Taylor coefficients of a nonlinear superposition operator; replace the complement local system by the induced (generally non-flat, possibly non-unitary) transport. Then:

- **(a)** the degree-1 obstruction class of the resulting sheaf of curved modules is nonzero
- ⟺ **(b)** the full inhomogeneous Maurer–Cartan equation Σ_k m_k(b, …, b) = −m₀ (FOOO form) has no solution over the family
- ⟺ **(c)** no admissible frame deformation drives D → 0 globally.

**Discharge conditions.** (i) Write the m_k explicitly from S_O and verify the curved Stasheff identities — the k = 1 identity is Theorem III.2; the higher ones are new. (ii) Prove (b) ⟸ (c) by exhibiting the extension-induced bounding cochain b as in III.4 with higher corrections. (iii) Prove (b) ⟹ (a) by the obstruction-theory spectral sequence whose E₂ input is exactly Part IV's linear computation — the linear Triple proven here is the leading order of the nonlinear one, which is why it was worth proving first.

**Second field corpus [recommended, not run].** A real co-occurrence hypergraph with external embedding payloads (nodes = target words, incidences = context words, payloads = pretrained embeddings, frames = distinct projection planes) would test whether node-level coherence sign-flips — absent in the supervised digit corpus by construction — appear when the corpus is not class-coherent. This is the natural robustness check on the Part V GO verdict.

---

# Appendix C — Notation Index

| Symbol | Meaning | Introduced |
|---|---|---|
| F = (V̄, Ē, Ī, W, Ξ) | latent relation-field | I.1 |
| W, d | payload space and its dimension | I.1 |
| Ξ(v,e) | latent payload of incidence (v,e) | I.1 |
| O, Q_O, π_O, k | frame, visible subspace, its projector, dim | I.2 |
| ê_O, Π_O, J | anisotropy axis, helicity 2-plane, its complex structure | I.3 |
| A_O, B_O, H_O | anisotropy, polarity, helicity operators | I.3 |
| Φ̃_O(v,e), Φ_O(v,e) | resolved (full-d) and visible (projected) payloads | I.3 |
| Ψ_O(v) | node instantiation | I.5 |
| g, n, T, κ | gross mass, net resultant, tension, signed coherence | I.5 |
| D_O(v) | dimensional pressure = discarded energy fraction | I.5 |
| m₀(e) = (1−π)Φ̃_e | curvature payload (invisible component) | III.0 |
| E, E_vis, 𝔴 | total, visible, curvature energies; 𝔴 = ‖m₀‖² summed | III.0 |
| c(w), c_e(w) | Clifford operator, on the e-th super-tensor factor | III.1 |
| M_v | instantiation module = super tensor of exterior algebras | III.1 |
| 𝔡, 𝔡^vis, 𝔡^⊥ | full, visible, perpendicular differentials | III.1 |
| MF(R, 𝔴), Tw(B_𝔴) | matrix factorizations; twisted complexes over curved alg | III.3 |
| φ = Hol(O) ∈ U(k) | frame-loop holonomy / monodromy | IV.1 |
| M_φ | mapping torus (the helical substrate) | IV.2 |
| φ^⊥, C, [C] | complement holonomy, defect cocycle, its H¹ class | IV.2 |
| (U)(FR)(CL)(LIN)(DISC)(GEN) | standing assumptions | Appendix A |

---

*End of monograph. Companion artifacts: `waveform-proofs/` (runnable codebase), `observer-indexed-hypergraph-spec-v2.md` (normative spec), `w3id-waveform-pr/` and `waveform-ns/` (namespace).*

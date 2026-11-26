# Observer-Indexed Dual Hypergraph with Incidence Waveforms — Canonical Specification v2

**Status:** Post-audit consolidation. Supersedes the v1 formalization document and incorporates the citation/mathematical audit in full.
**Rigor labels used throughout:** [THM] proven or immediate; [TIR] theorem-in-reach (statement fixed, proof sketch given, expansion mechanical); [TIR-c] theorem-in-reach conditional on a flagged modeling bridge; [CIR] conjecture-in-reach.
> **Repo status note (see `RECONCILIATION.md`, R1 and R2).** This spec stays normative for the grammar (§1), duality (§2), citations (§3) and serialization (§6). Theorem status has moved on: Theorems 1–3 and Proposition 4 are [THM] in `waveform-monograph.md` (Theorems IV.1–IV.3, III.2), Conjecture 5's linear case is Theorem IV.5, and the nonlinear case is Conjecture B.1 [CIR]. Every item in §7 has been discharged or decided in `curvature-anthology-v1.md` and the monograph. §5.2's "every additive model" means scalar, nonnegative-weight additive models; see the note there.


---

## 0. Changelog v1 → v2

| Item | v1 | v2 |
|---|---|---|
| Helicity operator | `exp(h J_p̂)` — ill-posed for d≠3 | `exp(h J)`, J a complex structure on a declared 2-plane Π_O; well-posed all d (§1.3) |
| Anisotropy operator | `R diag(1,1−a,…,1−a) R⁻¹` — R underdetermined | Basis-free `A_O = I − a(I − P_ê)`, ê explicit frame data (§1.3) |
| π_O requirement | "contractive" | **Orthogonal projector required** wherever the energy interpretation is invoked (§1.4) |
| D_O zero-denominator | undefined | Convention `D_O := 0` on zero-energy nodes (§1.5) |
| Coherence at m_v = 1 | undefined | N/A in data; := 1 in scalar pipelines requiring a value (§1.5) |
| D̂ heuristic | `max(coherence, 0)` clamp | Clamp dropped; signed coherence retained (§1.5) |
| Citations (h), (e), (f) | misattributed / opaque / unflagged | Corrected (§3) |
| Dual serialization | unstated | Normative: query-time view only, never persisted (§2, §6) |
| AMT connection | absent | Bridge developed as Thms 1–3, Prop 4, Conj 5 (§4) |
| Worked example | unverified | Independently recomputed, exact (§5.1) |

---

## 1. Formal Grammar (corrected)

### 1.1 Latent relation-field

F = (V̄, Ē, Ī, W, Ξ), with Ī ⊆ V̄ × Ē and Ξ : Ī → W, W a real or complex inner-product space of dimension d. The latent field is not a graph; it is the constrained space of possible incidences carrying structured local state.

### 1.2 Observation frame

O = (Q_O, Γ_O, τ_O, ê_O, Π_O, c_O, S_O, meta_O)

- **Q_O ∈ Gr(k, d)** — visible k-plane, represented by an orthogonal projector π_O (see §1.4).
- **Γ_O : Ī → [0,1]** — gating; visibility χ_O(i) = 1[Γ_O(i) > τ_O].
- **ê_O ∈ S^{d−1}** — anisotropy axis. **Explicit frame data** (v2 change; may vary per incidence as ê_O(v,e) if needed, but must be declared).
- **Π_O ⊆ W** — distinguished 2-plane carrying the helicity rotation. **Normative default: Π_O := Q_O when k = 2** (no extra data). Otherwise declared explicitly as an ordered orthonormal pair (u, v). In d = 3 with propagation axis p̂, Π_O = p̂^⊥ recovers the classical case; p̂ is retained as optional metadata only.
- **c_O ∈ W_O** — optional context vector.
- **S_O** — superposition operator.
- **meta_O** — provenance (PROV-O; §6).

### 1.3 Incidence operators (repaired)

**Anisotropy** [basis-free]:

A_O(v,e) = I − a_O(v,e) (I − P_ê), P_ê = ê ê*

a = 0 → isotropic; a = 1 → rank-1 collapse onto ê. No rotation matrix, no basis ambiguity.

**Polarity**: B_O(v,e) = b_O(v,e) · I, b ∈ [−1, 1].

**Helicity** [repaired — the v1 gap]: "rotation about an axis" is canonical only in d = 3 (so(3) ≅ ℝ³ axis-angle). For d ≥ 4, dim so(d) = d(d−1)/2 > d: an axis does not determine a generator, and in even d generic rotations have no fixed axis. Fix: equip W with the complex structure J determined by the ordered pair (u, v) spanning Π_O via Ju = v, Jv = −u, J = 0 on Π_O^⊥. Then J² = −I on Π_O and

H_O(v,e) = exp(h_O(v,e) J) = rotation by h in Π_O, identity on Π_O^⊥.

Well-posed in all d. The ±i eigenspaces of J on Π_O ⊗ ℂ are the left/right circular-polarization basis states (Born–Wolf §1.4), tying h directly to physical helicity.

**Resolved and visible states**:

Φ̃_O(v,e) = B_O H_O A_O Ξ(v,e),   Φ_O(v,e) = π_O(Φ̃_O(v,e)).

### 1.4 Projection requirement [normative]

π_O **must be an orthogonal projector** (self-adjoint idempotent). Rationale: for merely contractive π the bound D_O ∈ [0,1] survives (‖πw‖ ≤ ‖w‖ pointwise), but the energy interpretation requires the Pythagorean split ‖w‖² = ‖πw‖² + ‖w − πw‖², which holds only for orthogonal projectors; oblique idempotents can even have ‖π‖ > 1, breaking the bound itself. Every energy-reading claim in this spec (D_O, Prop 4) presumes orthogonality.

### 1.5 Node instantiation and derived metrics (conventions adopted)

Ψ_O(v) = S_O({Φ_O(v,e) : (v,e) ∈ I_O}). For visible incidences φ_1,…,φ_{m_v} at v:

- gross_mass(v) = Σ‖φ_i‖
- net_resultant(v) = ‖Σφ_i‖  (tension = gross − net ≥ 0 by triangle inequality)
- coherence(v) = (2/(m_v(m_v−1))) Σ_{i<j} Re⟨φ_i, φ_j⟩ / (‖φ_i‖‖φ_j‖) — **signed, never clamped**. Conventions: undefined at m_v = 1 → omit in serialized data (N/A); pipelines requiring a scalar use 1. Zero-payload incidences are dropped from the coherence computation.
- context_score(v) = Σ Re⟨c_O, φ_i⟩
- **D_O(v) = 1 − Σ_e ‖π_O Φ̃_O(v,e)‖² / Σ_e ‖Φ̃_O(v,e)‖²**, with **D_O(v) := 0 when the denominator is 0** (no energy ⇒ no projection loss). D_O ∈ [0,1] by §1.4. [THM]
- Fallback heuristic (ambient states unavailable): D̂_O(v) = ((1 − coherence)/2) · (1 − net/(gross + ε)) · (1 − e^{−m_v}). The v1 clamp max(coherence, 0) is **removed**: it conflated destructive interference (coherence ≈ −1) with orthogonality (≈ 0) and destroyed the falsifier signal of §5. The (1 − coherence)/2 factor maps [−1, 1] → [1, 0] monotonically. D̂ := 0 at m_v = 1. Heuristic only; D preferred whenever Φ̃ exists.

---

## 2. Duality [normative conventions]

H_O* = (E_O, V_O, I_O^⊤, Φ_O*) with **identity transfer** Φ_O*(e,v) = Φ_O(v,e). Involution (H_O*)* ≅ H_O is strict (transpose² = id; Mulas–Reff (G*)* = G; Grilliette–Rusnak self-inverting incidence-dual functor). One flagged subtlety: a *conjugating* dual (h ↦ −h, payload conjugation) is equally involutive and is the physically natural variant (dual reverses handedness). **Normative default: identity transfer.** The conjugating variant, if ever adopted, is a global flag, not a per-record choice.

**Serialization principle [normative]: the dual is a query-time view.** Because duality is identity-transfer incidence transpose, no dual records are ever persisted; the dual is recovered by swapping the roles of EntityNode and RelationNode over the shared incidence store. Persisting duals doubles storage and creates a sync-integrity failure mode for zero informational gain.

---

## 3. Corrected Load-Bearing Citations (defects fixed)

**(h) Incidence algebras / Möbius inversion — misattribution corrected.** Root: G.-C. Rota, "On the Foundations of Combinatorial Theory I: Theory of Möbius Functions," *Z. Wahrscheinlichkeitstheorie und Verw. Gebiete* 2:340–368 (1964), DOI 10.1007/BF00531932. Reduced incidence algebras / generating functions: P. Doubilet, G.-C. Rota, R. Stanley, "On the foundations of combinatorial theory VI," *Proc. Sixth Berkeley Symp.*, vol. II, 267–318 (1972). Canonical text: R. Stanley, *Enumerative Combinatorics* Vol. 1, Ch. 3.

**(e) Sheaf-on-raw-hypergraph caveat — sources named.** S. Choi, G. Kim, Y.-G. Oh, "Hypergraph Neural Sheaf Diffusion: A Symmetric Simplicial Set Framework for Higher-Order Learning," arXiv:2505.05702; *IEEE Access* 13:131823–131838 (2025), DOI 10.1109/ACCESS.2025.3592104 ("absence of intrinsic adjacency relations and orientation systems in hypergraphs creates fundamental challenges for constructing sheaf Laplacians"). A. Ayzenberg, T. Gebhart, G. Magai, G. Solomadin, "Sheaf theory: from deep geometry to deep learning," arXiv:2502.15476 (2025). Consequence stands: sheafify the incidence graph/poset, not the naked hypergraph.

**(f) Vector/tensor-valued incidence — retraction flagged, live anchor added.** M. Albooyeh, D. Bertolini, S. Ravanbakhsh, "Incidence Networks for Geometric Deep Learning," arXiv:1905.11460 (ICML 2020) — **author-retracted for an experimental error**; cite the sparse-incidence-tensor *formalism* only, never the empirical results. Live anchor: K. Miyamoto, "Defect Spaces and Gram Operators for Tensor-Valued Incidence Maps," arXiv:2605.28535 (2026).

**Supplementary (a′):** the crisp functorial "dual = incidence transpose" statement is Grilliette–Rusnak (arXiv:2007.01842 / arXiv:1910.02305); Mugnolo (arXiv:2510.17497) contributes the directed-hypergraph Laplacian L = I I^⊤ and dual dynamics, not the bare duality definition.

Unchanged verified anchors: Bretto (Springer 2013) / Berge (1973) for duality; Rusnak *Electron. J. Combin.* 20(3):#P48 (2013) and Reff–Rusnak *LAA* 437:2262–2270 (2012) for oriented incidences; Mulas–Reff arXiv:2011.10458 for complex-unit incidences; Hansen–Ghrist *J. Appl. Comput. Topol.* 3(4):315–358 (2019) for cellular sheaves; PROV-O / PROV-DM (W3C Rec 2013-04-30), JSON-LD 1.1 (W3C Rec 2020-07-16), SHACL (W3C Rec 2017-07-20); Born–Wolf, *Principles of Optics* 7e §1.4 for helicity.

---

## 4. The AMT Bridge

Setting: each frame O(t) has visible subspace Q(t) := Q_{O(t)} ∈ Gr(k, d). A one-parameter loop of frames O : S¹ → Frm is a loop in the Grassmannian.

### Theorem 1 (Frame holonomy). [TIR]

Let O : S¹ → Frm be piecewise-smooth with Q(1) = Q(0), and let π(t) be the orthogonal projector onto Q(t). Pull back the tautological rank-k bundle τ_k → Gr(k,d) along t ↦ Q(t) and equip it with the Grassmann connection ∇ = π ∘ d. Then:

(i) Parallel transport T_t : Q(0) → Q(t) is generated by Kato's equation Ẇ = [π̇, π] W, W(0) = I (T. Kato, *J. Phys. Soc. Japan* 5:435–439, 1950), which intertwines the family (W π(0) W⁻¹ = π(t)) and restricts to unitaries on the fibers.

(ii) **Hol(O) := T_1 ∈ U(Q(0)) ≅ U(k)** is well-defined.

(iii) k = 1: Hol = e^{iγ} with γ the geometric phase — B. Simon, *Phys. Rev. Lett.* 51(24):2167–2170 (1983): the phase "is precisely the holonomy in a Hermitian line bundle." k > 1: Hol = 𝒫 exp ∮ A with A_{ab} = ⟨e_a, de_b⟩ — F. Wilczek & A. Zee, *Phys. Rev. Lett.* 52(24):2111–2114 (1984).

(iv) The pullback connection over S¹ is automatically **flat** (no 2-forms on a 1-manifold); the curvature of Gr(k,d) (Ω = π dπ ∧ dπ upstairs) manifests as loop-dependence of Hol.

*Proof sketch.* ∇ = π∘d is the ambient flat connection projected to the subbundle (Taylor, *Connections and Curvature*, App. C). Kato transport preserves the metric because [π̇, π] is skew-adjoint (π, π̇ self-adjoint). Unitarity of T_1 gives (ii); (iii) is the cited literature verbatim; (iv) is dimension counting. ∎

### Theorem 2 (Helical substrate = mapping torus of frame holonomy). [TIR]

Let φ := Hol(O) ∈ U(k). The total space of instantiations over the frame loop, E = {(t, x) : x ∈ Q(t)} glued by parallel transport, is isomorphic (via the trivialization x ↦ T_t⁻¹x) to the mapping torus

M_φ = (Q(0) × [0,1]) / ((x, 0) ∼ (φx, 1)),

a fiber bundle over S¹ with flat connection and monodromy φ. This satisfies all four AMT substrate requirements:

| AMT requirement | Realization | Status |
|---|---|---|
| Non-product | φ ≠ id, i.e. nonzero geometric phase. Classification of flat bundles over S¹: Hom(π₁S¹, U(k))/conj = U(k)/conj ∋ [φ]; nontrivial conjugacy class = geometric (connection-level) twist. Note honestly: as a *bare* bundle it is topologically trivial (U(k) connected); the helicality is the flat-connection class — which is exactly the classification AMT's Step 5 already uses. | [THM] |
| One-parameter projectable | Projection to S¹ = the loop parameter, by construction. | [THM] |
| Orientation-consistent | Automatic: U(k) ⊂ SO(2k) since det_ℝ(U) = |det_ℂ(U)|² = 1. | [THM] |
| Compositionally non-flat | m₀ ≠ 0 ⇔ D_O > 0 somewhere (Prop 4). | [TIR-c] |
| Infinite-order monodromy | φ has infinite order iff some eigenvalue phase γ_j ∉ 2πℚ. Generic (full measure in U(k)) but **not automatic**; rational-phase loops give finite-order (periodic-helix/Seifert-like) substrates. | [THM], flagged |

### Theorem 3 (Straightening identification). [TIR]

The loop-restricted instantiation assignment is a functor Bℤ → Cat∞ (linear shadow: Bℤ → Vect) sending the generator of ℤ = π₁(S¹) to φ_*. Its unstraightening (Lurie, *Higher Topos Theory*, Thm 3.2.0.1) is the coCartesian fibration over S¹ ≃ N(Bℤ) with total space M_φ. Hence frame-loop instantiation **is** an instance of AMT's straightening/unstraightening equivalence between coCartesian fibrations over S¹ and functors Bℤ → Cat∞ — not an analogy to it.

*Proof sketch.* For a group G, straightening over BG identifies functors BG → Cat∞ with G-actions; unstraightening is the (∞-)Borel construction. For G = ℤ acting by φ_*, the Borel construction of a ℤ-action is the mapping torus — classically, ℤ-actions ↔ bundles over S¹ ↔ mapping tori; Lurie supplies the ∞-categorical upgrade. ∎

### Proposition 4 (Curvature identification — conditional). [TIR-c]

**Bridge (definitional, flagged):** define the curvature payload m₀(v,e) := (I − π_O) Φ̃_O(v,e) ∈ Q_O^⊥ — the invisible component of the resolved state. Then, with π_O orthogonal (§1.4),

‖Φ̃‖² = ‖π_O Φ̃‖² + ‖m₀‖²  ⟹  **D_O(v) = Σ_e ‖m₀(v,e)‖² / Σ_e ‖Φ̃_O(v,e)‖²**,

i.e. D_O is the normalized squared norm of the curvature payload, and D_O(v) = 0 ⇔ m₀ ≡ 0 at v ⇔ the frame is flat at v. *Proof:* Pythagoras. ∎

Honesty condition: the A∞ reading — m₀ as the degree-2 curvature element of a curved A∞-structure on the instantiation complex, with m₁² = ±m₂(m₀, −) — requires *equipping* that complex with a specified curved structure in which this m₀ is the curvature. Until that structure is written down, Prop 4 is exact as stated but the "curvature" label is a modeling identification, not a derivation. This is the same honesty level as AMT's own policy-parameters-to-m₀ mapping.

### Conjecture 5 (The Triple) + established linear case. [CIR / THM]

**Conjecture.** Under suitable finiteness and topology hypotheses on the frame site (§4-site: order O′ ≤ O by Q_{O′} ⊆ Q_O and Γ_{O′} ≤ Γ_O; covers = jointly-spanning refinements), the following are equivalent:
(a) H¹(Frm; 𝔉) ≠ 0 for the instantiation sheaf 𝔉;
(b) the curved instantiation structure admits no Maurer–Cartan solution (no bounding cochain b with Σ m_n(b,…,b) = 0, in the FOOO sense — *Lagrangian Intersection Floer Theory*, AMS/IP 46, 2009);
(c) no frame extension drives D_O → 0 globally (irreducible latent dimensional pressure).

**Established linear case** — the cohomological obstruction theorem: nontrivial H¹(S, ℐ) obstructs global invariant sections of the instantiation sheaf, and resolution is exhausted by exactly two operations — base change on π₁(S) (growth) or change of twisted flat-bundle coefficients (reinterpretation), with promotive sub-cases classified under reinterpretation by design decision. This is the (a) ⇔ (c) equivalence in the linear/twisted-coefficient regime, and it composes with Theorem 2: the coefficients being *twisted flat-bundle* coefficients is precisely the mapping-torus monodromy data, so the obstruction theorem is already living on the helical substrate. What remains for the full conjecture is (b): specifying the curved A∞-structure of Prop 4's honesty condition and proving MC-solvability ⇔ H¹-vanishing there. Roadmap: Möbius-graph worked example → stress tests, per the existing implementation roadmap.

**Local–global caution [flagged]:** D_O(v) > 0 at every frame of a cover does *not* imply H¹ ≠ 0 — locally lossy can be globally reconcilable. D is local scalar energy loss; H¹ is the global obstruction. The Triple asserts equivalence only for the *global* clause (c).

---

## 5. Falsification: Prediction, Protocol, and Executed Verification

### 5.1 Worked example — independently recomputed [Caveat 1 CLOSED]

Latent states Ξ(C,R₁) = [1.0, 0.2, 0.1], Ξ(C,R₂) = [0.9, 0.1, 0.0], Ξ(C,R₃) = [−0.4, 0.0, 1.1]; frames O_xy, O_xz. Recomputed to machine precision (numpy, this consolidation):

| Metric | O_xy | O_xz | v1 claimed | Verdict |
|---|---:|---:|---|---|
| Ψ_O(C) | [1.5, 0.3] | [1.5, 1.2] | same | ✓ exact |
| gross_mass | 2.325342 | 3.075458 | 2.325 / 3.075 | ✓ |
| net_resultant | 1.529706 | 1.920937 | 1.530 / 1.921 | ✓ |
| coherence | −0.326075 | +0.135587 | −0.326 / 0.136 | ✓ |
| tension | 0.795637 | 1.154520 | 0.796 / 1.155 | ✓ |
| D_O(C) | 0.376543 | 0.015432 | 0.377 / 0.015 | ✓ |

Pairwise coherences: O_xy = {(R₁,R₂): +0.9962, (R₁,R₃): −0.9806, (R₂,R₃): −0.9939}; O_xz = {+0.9950, −0.2465, −0.3417}.

**The worked example is itself a minimal witness of the falsifier:** node-level coherence sign-flips across frames (−0.326 → +0.136) with tension > 0 in both frames, and it contains a **monotonicity violation**: in O_xy, net_resultant over {R₁, R₂} alone is 1.923538; adding R₃ *decreases* it to 1.529706. No additive model with nonnegative contributions can decrease an aggregate by adding an incidence.

### 5.2 Distinguishing prediction

Additive / weighted-hypergraph / additive-scoring models are monotone with tension ≡ 0 and frame-invariant nonnegative effective coherence — structurally. The waveform model predicts, on suitable data: (P1) tension > 0; (P2) monotonicity violations; (P3) frame-dependent **sign flips** in pairwise coherence (a pair constructive in one frame, destructive in another). Any nonzero rate of (P3) falsifies every additive model; conversely, if a fitted additive model matches the data with tension ≡ 0, the waveform apparatus is unsupported on that dataset. Analytic minimal (P3) witness: φ₁ = [1, 0, 1], φ₂ = [0.2, 0, −1] → projected coherence +1.0000 in O_xy, −0.5547 in O_xz (verified).
> **Repo note, scope correction (`RECONCILIATION.md` R2).** "Additive" here means scalar, nonnegative-weight additive scoring. (P1)–(P3) do not separate the waveform model from plain vector addition under projection, which produces all three; that is why the §5.3 synthetic ensemble fires on iid Gaussians. A GO on (P1)–(P3) is phenomenon detection, H₀ in the detector ladder. Comparative rejection of a fitted competitor starts at H₁ (`waveform-proofs/notes/h1-abelian-rung.md`).


### 5.3 Protocol + synthetic pipeline execution

1. Data: nodes with m_v ≥ 2 vector-payload incidences; two frames O₁, O₂ (rotated visible planes).
2. Compute pairwise coherence matrices C¹, C²; per-node tension in both frames; incremental-net monotonicity checks.
3. Discriminators: (a) fraction of nodes with tension > 0; (b) pairwise sign-flip rate; (c) monotonicity-violation rate. Nonzero (b) or (c) is the falsifier for the additive null.
4. Model comparison: held-out AIC/BIC (waveform vs. best additive fit) + permutation test on additive-fit residual vs. measured tension.

Pipeline demonstrated end-to-end on synthetic data (N = 500 nodes, m_v = 3, d = 3, standard-normal payloads, frames xy/xz, seed = 0): node-coherence sign flips 29.8%; pairwise sign flips 33.1% (497/1500); tension > 0 in both frames 100.0%; monotonicity violations 48.4%. On this ensemble every additive model is rejected, as expected by construction — the synthetic run validates the *pipeline*; the go/no-go benchmark of §5.2 applies to real data.

---

## 6. Serialization Deltas (v1 JSON-LD/SHACL layer stands; changes only)

The v1 @context, PROV-O integration (ProjectedIncidence = prov:Entity; projection run = prov:Activity with prov:used → {LatentIncidence, ObservationFrame}; observer = prov:Agent; prov:wasDerivedFrom projected → latent), and SHACL shapes remain normative. Deltas:

**@context additions / changes:**

```json
{
  "anisotropyAxis": { "@id": "wf:anisotropyAxis", "@container": "@list" },
  "helicityPlaneU": { "@id": "wf:helicityPlaneU", "@container": "@list" },
  "helicityPlaneV": { "@id": "wf:helicityPlaneV", "@container": "@list" },
  "gatingThreshold": { "@id": "wf:gatingThreshold", "@type": "xsd:double" },
  "incidenceCount": { "@id": "wf:incidenceCount", "@type": "xsd:integer" },
  "propagationAxis": { "@id": "wf:propagationAxis", "@container": "@list" }
}
```

- `wf:anisotropyAxis` (ê_O): REQUIRED on ObservationFrame whenever any incidence under the frame has anisotropy > 0.
- `wf:helicityPlaneU` / `wf:helicityPlaneV`: the ordered orthonormal pair spanning Π_O, determining J. OPTIONAL when k = 2 (default Π_O = Q_O applies); REQUIRED otherwise if any helicity ≠ 0.
- `wf:gatingThreshold` (τ_O) replaces the ambiguous v1 `wf:gating` scalar.
- `wf:incidenceCount` (m_v) on NodeInstantiation, so consumers can apply the m_v = 1 conventions.
- `wf:propagationAxis` (p̂): optional legacy metadata, d = 3 only, non-normative.
- `wf:coherence` on NodeInstantiation: now OPTIONAL (omit at m_v = 1 per §1.5).

**SHACL deltas:**

```turtle
wf:ObservationFrameShapeV2 a sh:NodeShape ;
  sh:targetClass wf:ObservationFrame ;
  sh:property [ sh:path wf:gatingThreshold ; sh:maxCount 1 ; sh:datatype xsd:double ;
                sh:minInclusive 0.0 ; sh:maxInclusive 1.0 ] ;
  sh:property [ sh:path wf:anisotropyAxis ; sh:maxCount 1 ] ;
  sh:property [ sh:path wf:helicityPlaneU ; sh:maxCount 1 ] ;
  sh:property [ sh:path wf:helicityPlaneV ; sh:maxCount 1 ] .

wf:NodeInstantiationShapeV2 a sh:NodeShape ;
  sh:targetClass wf:NodeInstantiation ;
  sh:property [ sh:path wf:incidenceCount ; sh:minCount 1 ; sh:maxCount 1 ;
                sh:datatype xsd:integer ; sh:minInclusive 1 ] ;
  sh:property [ sh:path wf:coherence ; sh:minCount 0 ; sh:maxCount 1 ;
                sh:datatype xsd:double ; sh:minInclusive -1.0 ; sh:maxInclusive 1.0 ] .

# Unit-norm and orthonormality of axis / plane vectors are NOT expressible in
# SHACL Core (requires arithmetic over rdf:List members). Enforce via
# SHACL-SPARQL with an epsilon tolerance, same pattern as PhiDimensionShape:
# sum-of-squares within [1-eps, 1+eps]; dot(U,V) within [-eps, +eps].
```

**Restated normative principle:** dual records are never persisted (§2). The dual view is a query-time role swap over the shared incidence store.

---

## 7. Open Items (ordered)

1. Write the curved A∞-structure on the instantiation complex realizing Prop 4's m₀ as genuine curvature — this discharges [TIR-c] → [THM] and unlocks clause (b) of the Triple.
2. Prove Conjecture 5 in the linear/harmonic regime end-to-end by composing the obstruction theorem with Thm 2's monodromy data; Möbius-graph example first, then stress tests, per the implementation roadmap.
3. Run §5.3 on real data (candidate: any multi-frame vector-payload corpus); go/no-go per §5.2.
4. Decide the conjugating-dual flag (§2) before any physical-helicity application.
5. Mint the w3id.org/waveform namespace before external interchange.

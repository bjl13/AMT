# The Comparator Ladder Theorem
## The hypothesis hierarchy is the lower central series of the holonomy group

**What this settles.** A methods-bound review raised two points that are, underneath, the same object. First, H₂'s phrase "cannot represent even in principle" is a claim about *all* representations — including higher-dimensional abelian ones and flat connections on larger bundles — and so is a theorem to be proved, not rhetoric to be asserted. Second, the comparator ladder (static → projection, abelian → winding, non-abelian → ordering) looks accidental and should be *derived* from the mathematics, converting the experiments from discoveries into demonstrations. Both resolve at once: the ladder **is** the lower central series of the holonomy group, and the single homomorphism fact that generates the ladder also closes the "bigger abelian model" escape. This note proves it, states the honest boundary, confirms the predicted next rung on an indifferent CPU, and gives the corrected claim language.

Rigor flags: **[THM]** proven here; **[NUM]** exactly demonstrated (`src/ladder_theorem.py` / `outputs/ladder_theorem.txt`); **[ID]** identification with established theory (cited, not reproved); **[OPEN]** honest boundary.

---

## 1. Setup

Two closed frame loops A, B based at a point form a wedge of two circles, whose fundamental group is the free group **F₂ = ⟨a, b⟩** (non-abelian). Any two-loop transport is a **holonomy representation**

  ρ : F₂ → GL(V),  ρ(a) = Hol_A, ρ(b) = Hol_B,

with V the fiber (payload space) and the **full-frame readout** observing ρ(w) for a loop word w by transporting a complete input frame (the experiments use input frame = I, so ρ(w) is read directly, not through a projection).

**Basic commutators and depth.** Let w₁ ∈ {a, b} (weight 1), w₂ = [a, b] (weight 2), w₃ ∈ {[[a,b],a], [[a,b],b]} (weight 3), and generally the weight-k basic commutators, which generate γ_k(F₂) modulo γ_{k+1}(F₂), where γ₁ = F₂ and γ_{k+1} = [F₂, γ_k] is the **lower central series (LCS)**. The **depth-k observable** is

  𝒪_k(ρ) := ρ(w_k) ∈ GL(V),  nontrivial iff ρ(w_k) ≠ I.

Depth 1 is a single-loop holonomy (winding); depth 2 is the commutator-loop holonomy Hol_C read by H₂ (ordering / loop-order dependence).

**Hypothesis classes.** For k ≥ 0 let

  **H_k := { ρ : ρ(F₂) is nilpotent of class ≤ k }.**

H₀ = trivial holonomy = **static vector projection**; H₁ = abelian holonomy (class ≤ 1) = **winding**; H₂ = class ≤ 2 = **ordering**; H₃ = class ≤ 3 = **nested ordering**. The naming the review proposed — H₀/H₁/H₂, each strictly enlarging the hypothesis class — is exactly this filtration, adopted below.

**Class versus detector.** Each label does two jobs, and they differ by one step. As a *hypothesis class*, H_k is "nilpotent of class ≤ k." As a *detector*, H_k is the depth-k test: it uses 𝒪_k to reject H_{k−1}, its null. A positive H_k result therefore certifies **class ≥ k**, a lower bound. It does not place the holonomy in H_k. So H₁ certifies non-trivial holonomy, H₂ certifies *non-abelian* (class ≥ 2), not "class 2", and H₃ certifies class ≥ 3.

---

## 2. The separation theorem

### Theorem 1 (dimension-independent vanishing → closes the overclaim). [THM] [NUM]

If ρ ∈ H_{k−1}, then 𝒪_k(ρ) = I, **for every representation, independent of dim V**.

*Proof.* w_k ∈ γ_k(F₂) by construction. Group homomorphisms carry the LCS onto the LCS of the image: ρ(γ_k(F₂)) = γ_k(ρ(F₂)) (a homomorphic image of a k-fold commutator is the k-fold commutator of the images). Since ρ(F₂) has nilpotency class ≤ k−1, γ_k(ρ(F₂)) = {e}. Hence ρ(w_k) = I. The argument mentions only the group F₂ and the homomorphism ρ; the dimension of V never enters, so no enlargement of V can manufacture a nonzero depth-k observable from a class-<k holonomy. ∎

**Corollary 1 (the corrected non-abelian claim). [THM]** No abelian holonomy (H₁), in any representation dimension, reproduces the depth-2 (ordering) observable in the full-frame readout. This is Theorem 1 at k = 2, and it is the precise, provable replacement for "cannot represent even in principle."

*Numerical corroboration.* For random commuting unitary pairs (shared eigenbasis) in dimensions 2, 5, 12, 40, the depth-2 observable ‖[U_A, U_B] − I‖ is 3×10⁻¹⁶ to 1.3×10⁻¹⁴ (the exact digits vary with the BLAS build) — machine zero at every dimension. The "use a bigger abelian model" escape is closed by computation, not assertion.

### Theorem 2 (strictness — the observable actually separates). [THM] [NUM]

For each k there exists ρ ∈ H_k \ H_{k−1} with 𝒪_k(ρ) ≠ I; hence H₀ ⊊ H₁ ⊊ H₂ ⊊ ⋯ and 𝒪_k separates H_k from H_{k−1}.

*Proof by exhibited witnesses (exact unipotent holonomy in GL(V)).* The free class-k nilpotent quotient realizes a nonzero weight-k basic commutator. Computed exactly (integer arithmetic):

| witness holonomy | class | depth-2 \|[A,B]−I\| | depth-3 \|[[A,B],A]−I\| | depth-4 |
|---|---|---:|---:|---:|
| abelian (H₁) | 1 | **0** | 0 | 0 |
| Heisenberg 3×3 (H₂) | 2 | **1** | **0** | 0 |
| unitriangular 4×4 (H₃) | 3 | 3 | **2** | 0 |

Read-off: depth-2 separates H₁ from H₂ (0 vs 1); depth-3 separates H₂ from H₃ (0 vs 2); depth-4 vanishes at class 3. The filtration is strict and continues. ∎

### The honest boundary [OPEN]

Theorem 1 is stated for the **full-frame readout**. For a **projected readout** π ρ(·) onto a subspace, the vanishing can fail: compression of commuting operators need not commute (π U V π ≠ π V U π even when U V = V U). So higher-dimensional abelian models are **not** excluded for compressed/projected observables; that regime needs its own argument. The three experiments all use the full-frame readout (input frame = I), placing them squarely in the regime where Theorem 1 applies — but the boundary should be stated, not hidden.

### The flat-connection worry, dissolved [THM]

"Could a flat connection on a larger bundle reproduce the observable?" Flatness means holonomy factors through π₁ of the base, which here is F₂ — non-abelian. So a flat connection can have non-abelian holonomy, but then it lies outside H₁ (class ≥ 2): flatness is **orthogonal** to the abelian/non-abelian axis and provides no abelian reproduction of ordering. The worry conflates "flat" (trivial curvature 2-form) with "abelian holonomy" (trivial commutator); over a multiply-looped base these are different, and only the latter defines H₁.

---

## 3. The ladder is the lower central series (and the Chen depth filtration)

Theorems 1–2 assemble into the derivation the review asked for.

### Theorem 3 (the comparator ladder theorem). [THM]

The hypothesis hierarchy {H_k} is the filtration of holonomy representations by nilpotency class of the image; equivalently, by the depth at which the LCS of the holonomy group first survives. The canonical invariant separating consecutive rungs is the depth-k iterated-commutator observable 𝒪_k. Concretely:

  H₀ (static) —projection→ H₁ (abelian) —winding→ H₂ (non-abelian) —ordering→ H₃ —nested ordering→ ⋯

with rung k detected by, and only by, a depth-k observable that every lower rung forces to the identity (Theorem 1) and some class-k holonomy makes nontrivial (Theorem 2).

**Chen correspondence [ID].** 𝒪_k is the group-theoretic shadow of the depth-k **Chen iterated integral** of the connection (K.-T. Chen, *Ann. Math.* 1977; Magnus expansion): depth-1 = ∮ A (the abelianization / winding phase — Berry, monograph Thm IV.1 k=1); depth-2 = ∮∮ F, the curvature two-form integrated over the commutator loop (the ordering / non-abelian phase — Wilczek–Zee, k>1); depth-k = the k-fold iterated integral. The ladder is thus not an experimental artifact but the standard depth filtration of holonomy, read through the lower central series.

**Prediction, confirmed.** Theorem 3 predicts a **depth-3 rung, H₃**: an observable — the nested commutator loop [[A,B],A] — that vanishes for *every* holonomy in H₂ (class ≤ 2) and fires at class 3. The exhibited class-3 witness confirms it (depth-3 = 2 ≠ 0 at class 3, = 0 at class 2). H₁ and H₂ were the statistical detectors for depths 1 and 2; the theorem says there is a canonical depth-3 detector (a matched-null nested-commutator test against the H₂ comparator), and it specifies exactly what that detector must isolate.

---

## 4. Corrected claim language (for H₂)

Replace (now applied in `h2-nonabelian-rung.md`):

> "…detects structure that a transport-bearing but commutative competitor cannot represent even in principle…"

with:

> "…detects a signature no abelian holonomy reproduces in the full-frame readout, in any representation dimension — because a homomorphism carries the commutator of commuting elements to the identity regardless of dimension (Ladder Theorem 1). For a projected readout the exclusion is weaker and open; the experiment uses the full-frame readout, where the exclusion is a theorem."

Add, per the class-versus-detector distinction in Section 1: a positive H₂ result certifies *non-abelian* holonomy (class ≥ 2), a lower bound, not "class 2".

That is the whole of the reviewer's correction, discharged: the claim now names its regime (full-frame), its mechanism (homomorphism preserving commutators), its scope (all dimensions), and its boundary (projected readout, open).

---

## 5. Methodological consequence: the comparators are canonical, not chosen

The review's deepest observation is that the contribution may be **methodological**: a discipline for comparing representational frameworks — (1) specify the weakest comparator; (2) build a statistic invariant under everything the comparator can already do; (3) test whether your framework detects the residual. Theorem 3 upgrades this from good practice to something sharper for any holonomy-based framework:

- The comparators are **not chosen** — they are the successive quotients of the lower central series γ_k/γ_{k+1}. The comparator H_k is "holonomy of nilpotency class ≤ k."
- The invariants are **not chosen** — they are the depth-k Chen brackets. The statistic invariant under H_k is exactly the class of observables of Chen-depth ≤ k; the residual that survives is the depth-(k+1) bracket.
- "Is my framework new?" becomes decidable and graded: **new = detects a depth beyond the comparator's nilpotency class.** H₁ shows depth ≥ 1 beyond static (H₀); H₂ shows depth ≥ 2 beyond abelian (H₁); H₃ shows depth ≥ 3 beyond class ≤ 2 (H₂).

So the methodology, instantiated on transport, is not "construct a clever competitor" but "read the next comparator off the lower central series and test the next Chen bracket." That is the sense in which the ladder was never accidental — and the sentence worth keeping is the reviewer's own, now with a theorem under it: *don't argue your framework is interesting; enlarge the comparator to the next term of the lower central series and make the experiment about the bracket that survives.*

---

## 6. Naming (adopted)

Internal terminology moves to the filtration it actually is. H_k names both the hypothesis class (class ≤ k) and the rung whose detector rejects H_{k−1}; Section 1 gives the distinction.

| was | now | hypothesis class | null the detector rejects | invariant | Chen depth | a positive result certifies |
|---|---|---|---|---|---|---|
| field trial | **H₀** (static) | static vector projection | none (phenomenon detection only) | projection | 0 | — |
| abelian rung / discriminating experiment | **H₁** (abelian) | abelian transport | H₀, fitted static latent | winding ∮A | 1 | non-trivial holonomy |
| non-abelian rung | **H₂** (non-abelian) | class ≤ 2 transport | H₁, spectrum-matched abelian | ordering ∮F | 2 | non-abelian, class ≥ 2 |
| depth-3 rung | **H₃** (nested ordering) | class ≤ 3 transport | H₂, matched class-2 (D8, Heis) | nested ordering | 3 | class ≥ 3 |

The rename is applied across the waveform notes and scripts; `RENAMES.md` lists every change.

---

*Companion: `src/ladder_theorem.py` (exact demonstration), `h1-abelian-rung.md` (H₁), `h2-nonabelian-rung.md` (H₂), `h3-nested-rung.md` (H₃). The ladder theorem makes the last three demonstrations of a structural fact rather than isolated findings — which was the point.*

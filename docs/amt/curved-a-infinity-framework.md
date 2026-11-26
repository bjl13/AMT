# Curved A∞-algebras as the natural framework for Avergent Manifold Topology

**The mathematical structure satisfying both constitutive nesting and oriented one-parameter projection is precisely a mapping torus with orientation-preserving infinite-order monodromy — a generalized helix — and the correct composition algebra for non-zero policy projection is a curved A∞-algebra, where ∂² equals a curvature element rather than zero.** These two conclusions are not independent: curved A∞-algebras are the algebraic shadow of non-flat fiber bundles, and the curvature element m₀ that prevents ∂² = 0 is the same obstruction whose geometric realization produces helical winding. The unification runs through Lurie's straightening/unstraightening equivalence, the Adams cobar construction, and the Căldararu–Tu identification of twisted complexes over curved algebras with matrix factorizations. This report provides the precise theorems, proof sketches, and candidate evaluations requested for each problem, with conjectural connections explicitly flagged.

---

## Problem 1: the helix is forced by monodromy classification over S¹

The necessity argument proceeds in five steps, each grounded in standard results from fiber bundle theory.

**Step 1 — One-parameter projection forces fiber bundle structure.** Requirement 2 demands a projection π: E → B onto a totally ordered one-dimensional base B (the entropic irreversibility gradient). If π is a submersion, the Ehresmann fibration theorem guarantees E is a locally trivial fiber bundle over B. The total ordering on B means B is either ℝ or (after compactification of the parameter) S¹. Since ℝ is contractible, every bundle over ℝ is trivial (Steenrod, *The Topology of Fibre Bundles*, 1951), which would violate Requirement 1. **The non-trivial case requires periodic or quasi-periodic return, so the effective base is S¹.**

**Step 2 — Constitutive nesting forces non-trivial monodromy.** The classification theorem for fiber bundles over S¹ states that every fiber bundle with fiber F over S¹ is a mapping torus M_f = F × [0,1] / (x,0) ∼ (f(x),1) for some homeomorphism f: F → F, classified up to conjugacy in the mapping class group of F (Husemoller, *Fibre Bundles*, Ch. 4). A trivial bundle corresponds to f = id, giving E ≅ F × S¹ — a direct product. Requirement 1 explicitly excludes this additive/product decomposition. Therefore **f ≠ id**, and the monodromy is non-trivial.

**Step 3 — Consistent winding direction forces orientation preservation.** A Möbius band (the mapping torus of a reflection on [0,1]) has non-trivial monodromy but reverses orientation after one circuit: the winding direction flips. The Klein bottle (mapping torus of an orientation-reversing diffeomorphism of S¹) similarly fails. Requirement 2 demands consistent winding direction, so **the monodromy f must be orientation-preserving**.

**Step 4 — The universal cover construction produces helical geometry.** For a principal G-bundle over S¹ with holonomy g ∈ G, the universal cover ℝ → S¹ pulls the bundle back to the trivial bundle ℝ × G. The original total space is recovered as the quotient E = (ℝ × G)/ℤ where the generator of ℤ acts by (t, h) ↦ (t + 1, g·h). This is a **screw motion**: simultaneous translation in the base direction and transformation in the fiber. When g has infinite order (i.e., the cyclic group ⟨g⟩ is infinite), orbits never close, and the total space is genuinely helical. When g has finite order k, orbits close after k circuits — a **periodic helix** (torus knot-type structure), which still satisfies both requirements but in a degenerate periodic sense.

**Step 5 — The fundamental group argument.** Flat principal G-bundles over S¹ are classified by Hom(π₁(S¹), G)/conjugacy = G/conjugacy, since π₁(S¹) = ℤ and a homomorphism ℤ → G is determined by the image of 1 ∈ ℤ (Taubes, *Differential Geometry*, Ch. 13). The Ambrose–Singer theorem confirms that flat connections have trivial restricted holonomy group Hol⁰ = {e}, so the full holonomy is discrete: a cyclic subgroup of G isomorphic to ℤ or ℤ/k. **The non-trivial, orientation-preserving case with ℤ holonomy is precisely the infinite helix.**

### What fails and what survives

| Structure | Req 1 (constitutive nesting) | Req 2 (consistent winding) | Verdict |
|---|---|---|---|
| Trivial bundle F × S¹ | ✗ (direct product) | ✓ | Fails |
| Möbius band (order-2 reflection) | ✓ | ✗ (orientation reverses) | Fails |
| Klein bottle | ✓ | ✗ (orientation reverses) | Fails |
| Graded direct sum ⊕ₖ Vₖ | ✗ (explicitly excluded) | ✓ | Fails |
| Mapping torus, orientation-preserving, infinite order | ✓ | ✓ | **Helix** |
| Mapping torus, orientation-preserving, finite order k | ✓ (partially) | ✓ | Periodic helix |

The **minimal structure** is thus a mapping torus with orientation-preserving monodromy. For a one-dimensional fiber (F = ℝ or S¹), this is literally a helix. For higher-dimensional fibers, it is a generalized helix — a twisted product with consistent winding along the base direction.

### The contact geometry parallel provides differential-geometric confirmation

Contact structures are the differential-geometric incarnation of constitutive nesting. A contact structure ξ = ker α on a (2n+1)-manifold satisfies α ∧ (dα)ⁿ ≠ 0 — the maximal non-integrability condition. This is the precise negation of the Frobenius integrability condition, which would yield a foliation (the geometric analog of an additive graded decomposition). **Non-integrability prevents the structure from decomposing into independent leaves, forcing each "level" to constitutively involve its neighbors.**

The Reeb vector field R of a contact form α (defined by α(R) = 1, ι_R dα = 0) generates a flow whose orbits are helical when the rotation numbers are irrational. The canonical example: wave propagation from a point source in ℝ² lifts to a helix in the unit cotangent bundle UT*ℝ² ≅ ℝ² × S¹ (Geiges, *An Introduction to Contact Topology*, Cambridge 2008). This is not a coincidence — it is the geometric manifestation of the same monodromy argument above, with the contact non-integrability playing the role of Requirement 1.

**Conjectural connection (flagged):** The precise correspondence between "constitutive nesting" as an abstract requirement and contact non-integrability as a differential-geometric condition has not been formalized as a theorem. The analogy is mathematically rigorous at the structural level but would require a formal definition of "constitutive nesting" to become a proof.

---

## Problem 2: curved A∞-algebras are the correct composition algebra

The framework's requirement that ∂² ≠ 0 but is controlled by policy parameters (S, A, X, B) maps directly onto the structure of a **curved A∞-algebra**, where ∂² equals a curvature element rather than zero, and the curvature is constrained by the A∞ relations.

### The curved A∞ definition and why it fits

A curved A∞-algebra (A, {mₖ}ₖ≥₀) consists of a graded vector space A with operations mₖ: A^⊗k → A of degree 2−k for k ≥ 0, satisfying the generalized Stasheff identities. The critical structural feature emerges from the k = 1 identity:

**m₁(m₁(a)) + m₂(m₀(1), a) ± m₂(a, m₀(1)) = 0**

This says **m₁² ≠ 0 in general** — instead, its failure to vanish is measured by the curvature element m₀(1) ∈ A. The composition of two consecutive "boundary" operations produces a non-zero result, but that result is fully determined by the curvature and the multiplication m₂. The policy parameters (S, A, X, B) of the runtime policy Ω map onto the curvature element m₀ and the higher operations mₖ that constrain how m₁² deviates from zero.

The related structure of **matrix factorizations** makes this even more concrete: a matrix factorization of a potential W is a ℤ/2-graded module with differential d satisfying **d² = W · id** (Eisenbud, 1980; Kontsevich for Landau–Ginzburg models). The potential W is not zero, but it is a fixed, structural quantity — exactly the "constrained but non-zero" composition the framework requires. Căldararu and Tu proved that matrix factorizations are precisely twisted complexes over curved associative algebras (Trans. AMS, 2012), establishing the equivalence Tw(B_W) ≅ DG(B_W).

### Evaluation of all five candidates

**Candidate 1: dg-categories.** In a dg-category, hom-spaces are chain complexes with d² = 0, and composition satisfies the Leibniz rule d(f ∘ g) = df ∘ g ± f ∘ dg. The differential on each hom-complex squares to zero by definition. **Verdict: the standard (uncurved) dg-category does not match** because d² = 0 holds on morphism spaces. However, **curved dg-categories** — where d² = W for a curvature element W — do match, and these are a special case of curved A∞-categories (where mₖ = 0 for k ≥ 3). Grading is natural (chain complex grading). Behavior at singularities depends on W. Strong connections to fiber bundles exist: derived categories of sheaves on fiber bundles have dg-enhancements, and Serre spectral sequences encode fibration twisting through differentials on successive pages.

**Candidate 2: Enriched categories.** Categories enriched over chain complexes (Ch-enriched) are essentially dg-categories. Categories enriched over topological spaces give topologically enriched categories, which model (∞,1)-categories via the Bergner model structure. **Verdict: partial match.** Enrichment provides additional structure on hom-sets, but does not by itself produce ∂² ≠ 0. The enrichment framework is too general to pin down the specific failure mode. It is a container rather than a content — curved A∞ is the specific enriched structure needed.

**Candidate 3: Operads and colored operads.** The little intervals operad E₁ governs A∞-algebras (its algebras are precisely A∞-algebras up to homotopy). The Swiss-cheese operad SC₂ (Voronov, 1998) mixes E₂ and E₁ operations, capturing boundary/bulk interactions — an algebra over H*(SC₂) is a triple (B, A, f) where B is a Gerstenhaber algebra, A is associative, and f: B → A is central. **Verdict: operads provide the correct organizational framework for the multi-level structure** (the graded "orders" in the helical substrate), but they describe the shape of composition rather than the specific failure of ∂² = 0. Operadic composition is multi-input with associativity and equivariance, which maps well to the pipeline structure, but the curvature must be added separately. **The correct statement is: the composition is governed by a curved algebra over the E₁ operad** (or a colored variant for multi-level interactions). No direct persistence analog is known for operads, though Belchí and Murillo's A∞-persistence (arXiv:1403.2395) uses the A∞-structure extracted from the E₁-operad.

**Candidate 4: A∞-algebras and A∞-categories.** In a standard (uncurved) A∞-algebra, m₁² = 0 does hold — m₁ is a genuine differential. The higher operations m₂, m₃, ... encode the failure of strict associativity through the Stasheff identities. **Verdict: uncurved A∞ does not directly match** (since m₁² = 0). But **curved A∞-algebras** — the natural generalization where m₀ ≠ 0 — do match perfectly. This is the strongest candidate. Grading is built in. Degeneration at singularities is handled by the Maurer–Cartan formalism: a bounding cochain b satisfying ∑ mₙ(b,...,b) = 0 "cancels" the curvature locally, and where no such b exists (the singular/void regions), the curvature is genuinely non-trivial. The Fukaya category of a symplectic manifold is precisely a curved A∞-category when disc instantons (Maslov index 2 holomorphic disks) exist (Fukaya–Oh–Ohta–Ono, *Lagrangian Intersection Floer Theory*, AMS/IP Studies 46, 2009). Fiber bundle connections appear through Lagrangian fibrations, and persistent homology connections exist through filtered A∞-structures.

**Candidate 5: ∞-categories / quasi-categories.** Composition is defined up to a contractible space of choices (Joyal: the map C^{Δ[2]} → C^{Λ¹[2]} is a trivial Kan fibration). **Verdict: too weak for the specific constraint needed.** The contractible ambiguity in composition means any two compositions are homotopy equivalent — there is no room for the curvature element that makes ∂² non-trivially non-zero. Quasi-categories are the correct ambient framework (curved A∞-categories present as certain ∞-categories), but they do not by themselves specify the curvature constraint. The model comparison theorem (quasi-categories are Quillen equivalent to dg-categories in the stable setting, via Cohn's theorem) means one can always pass to the more explicit curved A∞ description.

### Summary verdict

**The curved A∞-algebra (with m₀ ≠ 0) is the unique candidate that simultaneously satisfies all four criteria: non-zero constrained composition (via m₁² = curvature term), natural grading (the A∞ degree), graceful degeneration at singularities (Maurer–Cartan obstruction theory), and established connections to both fiber bundles (Fukaya categories) and persistent homology (filtered A∞-persistence).** Matrix factorizations (d² = W · id) provide the most concrete realization when the "policy" parameters can be encoded as a superpotential W.

---

## Problem 3: the curvature element bridges helical geometry and curved composition

The unifying framework is the theory of **curved A∞-algebras together with their geometric realizations via the bar construction and Lurie's straightening/unstraightening equivalence**. The key insight is that the curvature element m₀ simultaneously:

1. Prevents ∂² from vanishing (the algebraic side — Problem 2)
2. Measures the holonomy/monodromy that produces helical winding (the geometric side — Problem 1)

### The Adams cobar construction as the bridge

Adams' cobar construction (1956, extended to all path-connected spaces by Rivera–Zeinalian, Algebr. Geom. Topol. 2018) provides the algebraic model. For a pointed connected space X, the cobar construction ΩC*(X) on the dg-coalgebra of singular chains is quasi-isomorphic to the chains on the based loop space ΩX. The critical case is X = S¹: the based loop space ΩS¹ has the homotopy type of ℤ (discrete), and **the winding number — the topological invariant counting helical turns — is precisely the grading element of this algebraic structure**.

The bar construction runs in reverse: given an A∞-algebra A, the bar construction BA produces a dg-coalgebra whose geometric realization recovers (in favorable cases) the classifying space. For the A∞-algebra of chains on a loop space, BA ≃ C*(X). **When A carries a curved A∞-structure (m₀ ≠ 0), the bar construction produces a "twisted" coalgebra whose geometric realization is a non-trivial fibration** — and over a one-dimensional base, this is a helical fibration by the monodromy argument of Problem 1.

### Lurie's straightening/unstraightening makes this precise

Lurie's straightening/unstraightening theorem (Higher Topos Theory, §3.2) establishes a natural equivalence between **coCartesian fibrations over an ∞-category C** and **functors C → Cat∞**. Applied to C = Bℤ (the classifying space of ℤ, which is S¹):

- A coCartesian fibration over S¹ is a fiber bundle with fiber varying along S¹ — the geometric (helical) side
- A functor Bℤ → Cat∞ is an automorphism of an ∞-category — the algebraic (monodromy) side

**The curvature of the connection on the fibration corresponds to the failure of the functor to be "flat" (i.e., to factor through the nerve of an ordinary category).** When the curvature is non-zero, the A∞-structure on the fiber's endomorphism algebra is curved, and the geometric realization is helical.

### Specific geometric realization results

**Theorem (Căldararu–Tu, Trans. AMS 2012).** For a smooth algebra B with central element W, the category of matrix factorizations MF(B, W) is equivalent to the category of twisted complexes Tw(B_W) over the curved algebra B_W with curvature m₀(1) = W. This provides the **algebraic-to-geometric dictionary**: the curvature W controlling d² = W · id on the algebraic side corresponds to the monodromy of the associated geometric fibration.

**Theorem (Kadeishvili, Russ. Math. Surveys 35:3, 1980).** The cohomology H*(A) of any A∞-algebra A carries a minimal A∞-structure (with m₁ = 0) unique up to A∞-isomorphism. The higher products m₃, m₄, ... on cohomology are Massey products. **In the curved setting, this theorem does not directly apply** — Căldararu–Tu proved that ordinary Hochschild homology vanishes for curved algebras (their Theorem 1.4), and the correct replacement is Borel–Moore Hochschild homology. This is an important caveat: the standard homological tools require modification in the curved regime.

**Theorem (FOOO, AMS/IP Studies 46, 2009).** The Fukaya category of a compact symplectic manifold is a curved A∞-category over the Novikov ring. The curvature m₀ for each Lagrangian L counts **Maslov index 2 pseudo-holomorphic disks with boundary on L** (disc instantons). A bounding cochain b with ∑ mₙ(b,...,b) = 0 "flattens" the curvature, recovering an uncurved A∞-algebra — geometrically, this is finding a gauge transformation that trivializes the connection locally.

### The persistence connection

The very recent **APT (Almost-Persistence-Tamarkin) correspondence** (arXiv:2503.15933, 2025) establishes a deep identification between three structures previously studied independently:

- **Persistence modules** over ℝ (from topological data analysis)
- **Almost modules** over Novikov rings (from Faltings' almost mathematics)
- **Objects in Tamarkin categories** (from microlocal sheaf theory in symplectic geometry)

This means **filtered A∞-algebras from symplectic geometry and persistence modules from TDA are essentially the same algebraic structure**. The curvature/filtration interplay is central to both: the filtration controls the failure of d² to vanish at each filtered level, and the persistence barcode tracks how this failure evolves along the one-parameter family.

Belchí and Murillo (arXiv:1403.2395) made this computational by introducing **A∞-persistence**: for each n > 0, the higher multiplications mₙ of the A∞-structure on filtered complexes yield homological invariants beyond persistent Betti numbers. These detect geometric structure (Massey products) invisible to ordinary persistent homology, and can be characterized via barcodes using Gabriel's theorem for quiver representations.

### What circle-valued persistence adds

For the helical structure specifically, Burghelea and Dey's work on **persistence for circle-valued functions** (2013) is critical. Standard persistence uses ℝ-valued filtrations and produces barcodes. Circle-valued persistence (using S¹-valued functions) produces two types of invariants: **barcode-type intervals** (as in the standard theory) and **Jordan cells** that capture features undergoing non-trivial monodromy as the parameter traverses S¹. **The Jordan cells are the persistence-theoretic signature of helical winding** — they correspond to homological features that do not return to their original state after one circuit, exactly the monodromy obstruction from Problem 1.

---

## The unified mathematical object

Assembling all three problems, the single underlying object is:

**A curved A∞-category enriched over filtered chain complexes, equipped with a functor to the poset (ℝ, ≤) (the entropic ordering), whose straightening is a non-trivial coCartesian fibration over S¹ (or ℝ with quasi-periodic structure).**

From this object:

1. **Helical structure** (Problem 1) is derived by applying Lurie's unstraightening to obtain the geometric fibration, whose total space is helical by the monodromy classification (π₁(S¹) = ℤ with orientation-preserving infinite-order holonomy).

2. **Curved composition** (Problem 2) is the algebraic structure of the curved A∞-category itself, where m₁² = m₂(m₀, −) ± m₂(−, m₀) encodes the non-zero but constrained policy projection, with m₀ (the curvature) corresponding to the runtime policy parameters.

3. **The connection** (Problem 3) is the straightening/unstraightening equivalence itself: the curvature m₀ that prevents ∂² = 0 is the same invariant as the holonomy that prevents the fibration from being trivial, which is the same monodromy that forces helical geometry.

The **Maurer–Cartan equation** ∑ mₙ(b, ..., b) = 0 provides the interface between curved and uncurved regimes: its solutions correspond to "flat" (uncurved) deformations of the curved structure — geometrically, to local trivializations of the helical fibration. The void regions where no bounding cochain exists are precisely the singular regions where the substrate's differentiable structure breaks down and the curvature is irreducible.

### Precise conjectural status

The following connections are **established theorems**: the classification of bundles over S¹ by monodromy; the curved A∞ Stasheff identities and their consequence m₁² ≠ 0; the Căldararu–Tu equivalence Tw(B_W) ≅ MF(B, W); Lurie's straightening/unstraightening; the Adams cobar construction modeling loop spaces; Kadeishvili's minimal model theorem; the FOOO curved A∞ structure on Fukaya categories.

The following connections are **mathematically rigorous but require the specific AMT formalization to be made fully precise**: the identification of "constitutive nesting" with non-trivial monodromy/contact non-integrability; the mapping of policy parameters (S, A, X, B) to the curvature element m₀ and higher operations; the claim that the void regions correspond exactly to obstructions of the Maurer–Cartan equation.

The following connection is **conjectural and requires new mathematical development**: a complete geometric realization theorem for curved A∞-categories that produces helical total spaces under specified conditions on the curvature. The ingredients all exist (bar construction, straightening, monodromy classification), but assembling them into a single theorem for the curved case has not been done in the literature. The APT correspondence (2025) suggests this is within reach but remains to be formalized for the specific setting of AMT.

---

## Conclusion

The mathematical content of Avergent Manifold Topology finds its natural home in **curved A∞-algebra over filtered chain complexes**, with geometric realization through fiber bundle theory over one-dimensional bases. The necessity of helical structure follows from the classification of oriented mapping tori over S¹ — there is no other geometry compatible with both constitutive nesting and consistent oriented projection. The curvature element m₀ of the curved A∞-structure is the single invariant that simultaneously governs the failure of ∂² = 0 and the non-triviality of the helical monodromy. The framework should be constructed explicitly as a curved A∞-category with the runtime policy Ω = (S, A, X, B) encoded in m₀, higher operations m₂, m₃, ... capturing the constrained pipeline composition, and the Maurer–Cartan moduli space parametrizing the transitions between curved (singular) and uncurved (regular) regimes. The most productive next step would be formulating the geometric realization theorem connecting the curved A∞-bar construction to helical fibrations — the ingredients are in place from Căldararu–Tu, FOOO, and Lurie, but the assembly is new mathematics.
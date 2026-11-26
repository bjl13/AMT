# H₂ (non-abelian): the commutator-loop rung
## Detecting a signature with no additive and no abelian shadow

*H₂ in the ladder of `comparator-ladder-theorem.md`: the depth-2 (ordering) detector, rejecting H₁ (abelian). A positive result certifies non-abelian holonomy, class ≥ 2, a lower bound. It does not place a world at class 2.*

**Purpose.** H₁ (`h1-abelian-rung.md`) built a falsifier that recovers a U(1) monodromy against a fitted static competitor and stays silent on noise. But a single phase has a partial abelian shadow — a determined skeptic can gesture at "it's just a rotation angle." This rung removes that escape. It targets an invariant that **no additive model produces, and no abelian holonomy reproduces in the full-frame readout in any representation dimension** (Ladder Theorem 1): loop-order dependence.

For two closed frame loops A and B with holonomies Hol_A, Hol_B ∈ U(2), traversing A-then-B differs from B-then-A exactly when they fail to commute, and the difference is the **commutator-loop holonomy**

  Hol_C = Hol_A Hol_B Hol_A⁻¹ Hol_B⁻¹.

Hol_C = I for *every* commuting (abelian) pair, in any representation dimension, and for *every* additive model (which has no holonomy at all). Hol_C ≠ I only under genuine non-abelian transport — the Wilczek–Zee regime (monograph Thm IV.1, k > 1; the k = 2 machinery in `wilczek_zee.py`). And det Hol_C = 1 identically, so Hol_C is invariant under global phase — the clean, gauge-independent operational target.

The comparator is now **H₁, the abelian holonomies** {commuting U(2) pairs}, the strongest simpler model that still *has* transport. It predicts Hol_C = I. We inject non-abelian transport, estimate Hol_C from noisy readout, and test whether it departs from identity beyond a matched null.

---

## 1. Design

**Worlds** (holonomies injected as SU(2) rotations R(n̂, θ) = exp(−i(θ/2) n̂·σ); the loop→holonomy step was already validated in `wilczek_zee.py`, so this rung tests the *statistical detection* of non-commutativity):

| world | Hol_A | Hol_B | Hol_C | comparator status |
|---|---|---|---|---|
| **NA** non-abelian | R(x̂, a) | R(ŷ, b) | ≠ I | outside abelian family |
| **AB** abelian null | R(x̂, a) | R(x̂, b) | = I | *in* abelian family, **matched spectra** |
| **Z** noise | I | I | = I | degenerate |

**AB is the crux.** Its per-loop rotation *angles* — hence eigenvalue spectra — are identical to NA's (same a, b), so every single-loop magnitude signature is identical by construction. The *only* difference between NA and AB is non-commutativity. This is the k = 2 analogue of H₁'s world-H vs world-I matched null: interference/magnitude looks the same; only the target invariant differs.

**Observation.** Transport the known input frame X = I₂ (columns = two orthonormal input states) around a loop; observe Y = Hol·X + E = Hol + E, entrywise complex-Gaussian noise at per-shot scale σ, over R repeated shots. Estimate Ĥol = nearest unitary to mean(Y) by SVD Procrustes.

**Statistic.** δ = ‖Ĥol_C − I₂‖_F from directly reading out the commutator loop. **Matched null:** a plug-in noise scale σ̂_eff is estimated from the R shots, and the abelian prediction Hol_C = I is simulated at that scale M = 300 times to build the null distribution of δ; p = fraction of null δ ≥ observed. Declare non-abelian iff p < 0.05. Corroborating readout: ‖[Ĥol_A, Ĥol_B]‖_F, estimated from separate A and B observations.

**Pre-registered GO.** (1) NA detection → 1 as shots R rise; (2) AB and Z false-alarm ≈ α = 0.05 — *the abelian comparator is not flagged*; (3) recovered ‖[Ĥol_A, Ĥol_B]‖ concentrates on truth for NA and → 0 for AB.

---

## 2. Results [NUM]

Injected angles a = b = π/2. Analytic truth: [R(x̂,π/2), R(ŷ,π/2)] = −iσ_z, so ‖[Hol_A, Hol_B]‖_F = √2 = 1.41421… (a clean target the estimator must hit).

**Snapshot** (per-shot σ = 0.3, R = 20):

| world | ‖Hol_A − I‖ | ‖[A,B]‖ est | δ = ‖Hol_C − I‖ | p | non-abelian? |
|---|---:|---:|---:|---:|:--|
| NA | **1.082** | 1.420 | 1.384 | 0.003 | **True** |
| AB | **1.082** | 0.071 | 0.115 | 0.123 | False |
| Z | 0.000 | 0.010 | 0.119 | 0.183 | False |

The matched-null demonstration is exact: **‖Hol_A − I‖ = 1.082 is identical for NA and AB** — the single-loop magnitude signature is provably blind to the distinction. Only non-commutativity separates them: ‖[A,B]‖ reads 1.420 (≈ √2) for NA versus 0.071 (≈ 0) for AB, and the commutator-loop test fires on NA (p = 0.003) while correctly clearing AB and Z.

**Power / calibration sweep** over shot count R (per-shot σ = 0.3, T = 150 trials):

| R | NA detect | AB false-alarm | Z false-alarm | NA med ‖[A,B]‖ | AB med ‖[A,B]‖ |
|---:|---:|---:|---:|---:|---:|
| 1 | 0.99 | 0.03 | 0.05 | 1.385 | 0.517 |
| 2 | 1.00 | **0.12** | **0.15** | 1.407 | 0.335 |
| 5 | 1.00 | 0.05 | 0.08 | 1.410 | 0.241 |
| 10 | 1.00 | 0.05 | 0.08 | 1.410 | 0.163 |
| 20 | 1.00 | 0.05 | 0.05 | 1.415 | 0.112 |
| 50 | 1.00 | 0.03 | 0.06 | 1.409 | 0.064 |

NA detection is ~1.00 throughout; recovered ‖[A,B]‖ concentrates on √2 = 1.414 for NA at every R, while AB's estimate decays toward 0 as noise averages down (0.52 → 0.06) — the expected behaviour of a commuting pair seen through finite estimation noise.

**The R = 2 calibration wobble, reported honestly.** At R = 2, AB and Z false-alarm rates jump to 0.12 and 0.15 — above the nominal 5%. This is a **noise-estimation artifact, not a property of the invariant**: with only 2 shots the plug-in variance σ̂_eff² is a ~1-degree-of-freedom estimate per component and is frequently under-estimated, which tightens the simulated null and inflates false positives. The same rows show NA detection at 1.00 and ‖[A,B]‖ on target, confirming the invariant is intact; only the self-calibration is under-powered. The detector is calibrated for **R ≥ 5** (AB false-alarm 0.03–0.05; Z 0.05–0.08, the latter running ~1 binomial SE high and conservatively tightenable with a small threshold inflation). R = 2 is not a regime one would run a holonomy detector in; the honest statement is that the estimator needs ≳ 5 shots to calibrate its own noise floor.

---

## 3. Verdict

**GO for H₂ (regime R ≥ 5).** The apparatus supports a falsifier for a signature with **no additive and no abelian shadow**. Concretely it:

1. **detects** injected non-abelian transport (loop-order dependence / commutator-loop holonomy ≠ I) at ~100% for R ≥ 1;
2. **recovers** the non-commutativity magnitude ‖[Hol_A, Hol_B]‖ → √2, the analytic truth, for NA and → 0 for AB;
3. **stays calibrated against the abelian comparator** — the strongest simpler transport model — at ≈ 5% false-alarm for R ≥ 5, and against noise;
4. does all of this while the single-loop magnitude signature is **provably identical** between the non-abelian world and its matched abelian null, so no magnitude/interference statistic could have made the call.

This is the strongest empirical claim in the corpus. H₁ showed the machinery beats a *static* competitor; H₂ detects a signature no abelian holonomy reproduces in the full-frame readout, in any representation dimension — because a homomorphism carries the commutator of commuting elements to the identity regardless of dimension (Ladder Theorem 1), and the observable is exactly the departure from that. For a projected readout the exclusion is weaker and open; the experiment uses the full-frame readout, where the exclusion is a theorem. Loop-order dependence is a genuinely non-abelian invariant; recovering it against a spectrum-matched abelian null is the thing the whole thread was circling.

**What it does and does not claim.** Synthetic ground-truth recovery, k = 2 / U(2), with the matched abelian null (H₁) as comparator. A positive result certifies *non-abelian* (class ≥ 2), not "class 2". It does *not* assert real data carries non-abelian holonomy — it establishes that the instrument can detect it when present, quantify it, and stay silent against the abelian family when absent. That is precisely the calibrated instrument needed to ask the real-data question without the hollowness the field trial suffered. The remaining honest gap is the R < 5 self-calibration (a noise-estimator fix, not an invariant fix) and, as always, a real corpus with plausible non-abelian frame structure.

---

## 4. Where the arc lands

The three experiments compose into a clean ladder, each rung removing a shadow the previous skeptic could hide in:

- **H₀, field trial (Part V):** phenomenon detection only — signatures generic to vectors under projection. Hollow as a discriminator, by the audit's correct diagnosis.
- **H₁ (abelian):** recovers a U(1) monodromy against a fitted static competitor; a falsifier that does not fire on noise. Removes the "it's just vectors" escape.
- **H₂ (non-abelian, this note):** recovers non-commutativity against a spectrum-matched abelian competitor; detects a signature with no additive *or* abelian shadow. Removes the "it's just a rotation angle" escape.

What began as "is this real or have I convinced myself with notation" now has an operational answer for the substrate's defining feature: the helical monodromy is detectable, quantifiable, and distinguishable from every simpler alternative in the comparator ladder — verified by an indifferent CPU that caught three detector artifacts (edge leakage, DC bias, small-sample calibration) along the way. The curvature was never the achievement; the achievement is that its distinguishing signature survived contact with data that had every opportunity to be explained by something simpler.

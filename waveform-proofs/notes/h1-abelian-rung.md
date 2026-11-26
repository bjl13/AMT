# H₁ (abelian): the discriminating experiment
## A falsifier that does not fire on noise: matched-null monodromy recovery

*H₁ in the ladder of `comparator-ladder-theorem.md`: the depth-1 (winding) detector, rejecting H₀ (static). A positive result certifies non-trivial holonomy. World labels H, I, S, Z below are data-generating worlds, not ladder levels.*

**Purpose.** The field trial (H₀, monograph Part V) established *phenomenon detection* — tension, resultant decrease, projection-dependent sign flips all occur on real data — but not *comparative rejection*. An external audit made the reason precise and correct: the waveform implementation superposes with ordinary vector addition Ψ = Σφ_e, so a vector-additive-with-projection model can already produce every one of those signatures. They are generic to vectors under projection, which is why the synthetic ensemble fired on iid Gaussians. The old test cannot separate "waveform structure" from "these are vectors."

This experiment fixes that. It keys on the one object a vector-additive model **cannot** represent: **monodromy** — the helical substrate's defining feature (mapping torus with holonomy φ = exp(hJ), monograph Thm IV.2). It (i) recovers an injected monodromy parameter, (ii) against a *fitted* static-latent competitor — the comparison v2 §5.3 promised and never ran — and (iii) stays calibrated on a matched null engineered to make every old signature fire while containing no monodromy.

Rigor flags as before: **[NUM]** numerically demonstrated; script and captured output in the codebase as `src/h1_monodromy_experiment.py` / `outputs/h1_monodromy_experiment.txt` (formerly `monodromy_experiment.*`).

---

## 1. Design

**Payload model.** A single signal incidence observed under N cyclic frames around a loop; payload y_j ∈ ℂ ≅ ℝ² (the smallest space carrying a continuous U(1) monodromy). Four data-generating worlds, unit signal amplitude a = 1, noise scale set by SNR = |a|²/σ²:

| world | generator | monodromy | interference |
|---|---|---|---|
| **H** helical | y_j = a·e^{i h·j/N} + ε_j | φ = e^{ih} ≠ 1 (genuine) | present |
| **I** incoherent | y_j = a·e^{iθ_j} + ε_j, θ_j ~ U(0,2π) | none (random phases, no winding) | **present, matched** |
| **S** static | y_j = a + ε_j | φ = 1 (trivial bundle) | absent |
| **Z** noise | y_j = ε_j | none (no latent) | present |

World **I** is the crux. It has the same per-step magnitude law as **H** (|e^{iθ}| = |e^{ihj/N}| = 1) and its phases fan around the circle, so it produces **large tension and strong interference with no coherent monodromy**. It is the matched null that a hollow test cannot distinguish from H — and, not coincidentally, it is exactly a phase-scramble of a helical signal, which is what makes it double as the detector's calibration null.

**Old signatures (magnitude-based, what the field trial used).** tension T = Σ‖p_j‖ − ‖Σp_j‖ and the isotropic-null resultant z-score, computed on p_j = (Re y_j, Im y_j).

**New statistic (monodromy, fitted comparison).** Fit two models by least squares:

- **A, static / trivial bundle (φ = 1):** â = mean(y); its fit power is P(0) = |Σy_j|²/N.
- **B, winding (h free):** â(h) = (1/N)Σ_j y_j e^{−ihj/N}; peak power P* = max_{|h|≥h_floor} |Σ_j y_j e^{−ihj/N}|²/N, at ĥ = argmax.

The improvement statistic is **ΔRSS = RSS_A − RSS_B = P* − P(0)** — how much better a winding explains the data than the best static (trivial-bundle) explanation, with the DC/h=0 mode excluded because φ = 1 is precisely *no* monodromy. Significance by **phase-scramble**: randomize the phases of y keeping magnitudes (this *is* world I), recompute ΔRSS on M = 200 scrambles, p = fraction of null ΔRSS ≥ observed. **The matched null is the calibration null.** Declare monodromy iff p < 0.05.

Why ΔRSS and not the raw periodogram peak: two detector defects surfaced and were fixed during the run (this is the experiment working). A raw-peak detector with a hard exclusion band leaked the S world's huge DC peak into the band edge (false positive at ĥ ≈ −0.75, the floor); naive mean-subtraction then biased ĥ for sub-single-turn windings (h = 3 rad ≈ 0.48 turns). The fitted comparison P* − P(0) cures both: it penalizes DC leakage explicitly (S scores ΔRSS < 0) and leaves ĥ unbiased.

**Pre-registered GO conditions.** (1) H-detection → 1 as SNR rises; (2) I, S, Z false-alarm rates ≈ α = 0.05 (calibrated — *does not fire without ground-truth monodromy*); (3) recovered ĥ concentrates on the injected h_true.

---

## 2. Results [NUM]

**Snapshot** (SNR = 5, h_true = 3.0):

| world | tension | z_iso | ĥ | ΔRSS | p | monodromy? |
|---|---:|---:|---:|---:|---:|:--|
| H | 37.13 | 10.6 | **2.985** | 59.02 | 0.005 | **True** |
| I | **90.42** | 0.3 | 9.582 | 1.53 | 0.687 | False |
| S | 4.28 | 18.1 | −0.754 | −4.05 | 1.000 | False |
| Z | 85.36 | −0.8 | 17.876 | 1.52 | 0.607 | False |

**Power / calibration sweep** (T = 120 trials per world per SNR, h_true = 3.0):

| SNR | H detect | I false-alarm | S false-alarm | Z false-alarm | median ĥ \| H |
|---:|---:|---:|---:|---:|---:|
| 0.5 | 1.00 | 0.08 | 0.01 | 0.02 | 3.000 |
| 1.0 | 1.00 | 0.07 | 0.00 | 0.06 | 3.016 |
| 2.0 | 1.00 | 0.05 | 0.00 | 0.03 | 3.016 |
| 5.0 | 1.00 | 0.08 | 0.00 | 0.05 | 2.985 |
| 10.0 | 1.00 | 0.06 | 0.00 | 0.05 | 3.016 |

All three conditions met. The recovered ĥ sits on 3.00 to within grid resolution across every SNR including 0.5 (signal power half the noise power); false-alarm rates on all three nulls hold at the nominal 5%.

**The decisive line is H vs I.** World I carries the *largest* tension in the table (90.4, larger than H's 37.1) — the magnitude/interference signature fires *harder* on the structureless null than on the genuine helix. Yet the monodromy statistic correctly reads I as null (p = 0.69) and H as real (p = 0.005, ĥ = 2.985). This is precisely the separation the old test could not make, and it is the empirical form of the audit's point: **interference signatures are not evidence of waveform structure; recovered monodromy is.**

---

## 3. Verdict, bounded

**GO — H₁: abelian monodromy recovery against a fitted static (H₀) competitor.** The apparatus supports a non-hollow falsifier: a statistic that (a) recovers a ground-truth monodromy parameter no additive model even defines, (b) beats a fitted static-latent competitor by a permutation-calibrated margin, and (c) does **not** fire on noise or on matched-magnitude interference without winding. This is the property the field trial lacked.

**What this does and does not claim.** It does *not* say real data contains monodromy — it says the machinery can detect monodromy when present and stay silent when absent, which is the precondition for asking the real-data question honestly. It is the U(1) / k = 1 (abelian) case. The competitor is the constrained static-latent model (one shared latent projected through all frames), which is the fair non-waveform vector baseline; an unconstrained per-incidence vector model overfits everything and is not a competitor.

**The honest field-trial restatement this licenses** (adopting the audit's language): *GO for phenomenon detection on the digit corpus; comparative model rejection was not performed there because no competitor was fitted. Comparative rejection is performed here, on ground-truth synthetic data, for the monodromy signature specifically.*

---

## 4. The next rung, H₂: non-abelian monodromy [proposed here; built in `h2-nonabelian-rung.md`]

The abelian case has a partial scalar shadow (a single phase). The genuinely waveform-only regime is **k = 2, non-abelian monodromy** φ ∈ U(2) — where Hol_A and Hol_B do not commute (‖[Hol_A, Hol_B]‖ = 2.77 in `wilczek_zee.py`) and *no* scalar or abelian model has any shadow of the structure at all. The extension:

- Worlds H/I/S/Z lift to ℂ² payloads; world H injects a non-abelian holonomy word φ = W(A,B); the competitor is the best abelian (commuting, H₁) monodromy fit.
- Discriminator: does a non-abelian fit beat the best abelian fit beyond the matched null? Non-commutativity is the target invariant — recover ‖[Hol_A, Hol_B]‖ and test it against zero.
- This is the falsifier with no additive *or* abelian shadow: passing it would be the first result where the waveform apparatus detects something no additive model, and no abelian holonomy in any representation dimension under full-frame readout, reproduces (Ladder Theorem 1). A pass certifies non-abelian holonomy (class ≥ 2), not class 2. The Wilczek–Zee machinery is already in the codebase; this is a bounded extension, not new theory.

If H₂ also clears — recovered non-commutativity, calibrated on the abelian null — the apparatus has earned "detects structure no abelian holonomy reproduces in the full-frame readout." If it does not, that is a clean, publishable boundary on what the formalism buys. Either way the ambiguity the whole thread has been circling gets resolved by an indifferent CPU rather than by notation.

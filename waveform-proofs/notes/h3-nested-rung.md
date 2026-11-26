# H₃ (nested ordering): the depth-3 rung
## Nested ordering against a matched H₂ (class-2) null

**Purpose.** The ladder theorem (`comparator-ladder-theorem.md`) predicts a third rung, H₃. Below it sits H₂, which detects loop-order dependence and so rules out every abelian holonomy. It does not rule out a holonomy that is non-abelian but *only just*: nilpotent of class 2, where every commutator is central. A skeptic who concedes ordering can still say "fine, but the ordering is flat; one central phase explains it." H₃ tests that escape. Its observable is the pair of weight-3 basic commutators

  W₃ₐ = Hol([[a,b],a]),  W₃ᵦ = Hol([[a,b],b]),  [x,y] = x y x⁻¹ y⁻¹,

which Ladder Theorem 1 forces to the identity for **every** class-≤2 holonomy, in any representation dimension, under full-frame readout. At class 3 at least one of them is nontrivial. Not necessarily both, which turns out to matter.

What a positive result means has to be stated first, because it is weaker than the label H₃ suggests. A nilpotent subgroup of U(n) is virtually abelian, and unitary class-2 commutators are quantized (Section 3). So for Kato (unitary) transport the realistic worlds are abelian, a finite group sitting exactly at some class, or not nilpotent at all. A firing H₃ detector therefore certifies **class ≥ 3**, a lower bound. It does not place a world at class 3, and the same reading applies retroactively to H₂: it certifies class ≥ 2, i.e. *non-abelian*, not "class 2".

Rigor flags as before: **[NUM]** numerically demonstrated (`src/h3_nested_experiment.py` / `outputs/h3_nested_experiment.txt`); **[THM]** proved here; **[OPEN]** honest boundary.

---

## 1. Construction

**Observation** is H₂'s, unchanged: transport the input frame X = I around a loop, R noisy shots Y = W + E (entrywise complex Gaussian, per-shot σ = 0.3), Ŵ = Procrustes(mean Y). The two nested commutators are traversed as loops in their own right (ten letters each) and read out directly.

**Statistic.** d_x = ‖Ŵ₃ₓ − I‖_F for x ∈ {a, b}, combined as

  T = √(d_a² + d_b²) = ‖diag(Ŵ₃ₐ, Ŵ₃ᵦ) − I‖_F.

Two alternatives are carried for comparison: T_max = max(d_a, d_b), and the single-bracket T₁ = d_a that the ladder note's prediction literally names.

**Matched null.** The class-≤2 prediction W₃ₐ = W₃ᵦ = I is simulated at the estimated noise scale (M = 400 draws). There are two calibrations:

- *plug-in*: H₂'s own method, a per-loop σ̂_eff from the shot spread;
- *studentized*: a bootstrap-t. T is divided by a σ̂ pooled over both loops, and each null draw re-simulates σ̂ from its χ² law. This is the fix for the R < 5 wobble H₂ reported, and it is applied to the H₂ detector as well, for comparison.

**Worlds.** Unitary track, all in U(2):

| world | Hol_A, Hol_B | class | ‖[A,B]−I‖ | ‖W₃ₐ−I‖ | ‖W₃ᵦ−I‖ | depth 4 |
|---|---|---|---:|---:|---:|---:|
| **D8** | mirrors at 0°, 45° | **2** | 2.828 | 0 | 0 | 0 |
| **D16** | mirrors at 0°, 22.5° | 3 | 2.000 | 2.828 | 2.828 | 0 |
| **Q16** | R(ẑ,π/2), R(x̂,π) | 3 | 2.000 | **0** | 2.828 | 0 |
| Dgen | mirrors at 0, 0.5 rad | ∞ | 2.380 | 2.572 | 2.572 | 2.141 |
| WZ | Wilczek–Zee pair, Gr(2,4) | ∞ | 2.770 | 0.786 | 0.786 | 1.493 |
| NN(ε) | R(x̂,ε), R(ŷ,ε) | ∞ | ≈0.71ε² | ≈0.71ε³ | ≈0.71ε³ | ~ε⁴ |

**D8 is the null.** Two mirrors generate a dihedral group whose order is set by the angle between them. At 45° it is D8, class 2; at 22.5° it is D16, class 3. Both generators are reflections in every case, eigenvalues {+1, −1}. So the depth-1 spectra are matched exactly, which is the same matching H₂ used, carried up one level. The H₂ detector fires on all of these worlds, so depth 2 says nothing about which one is class 2.

Matching at depth 2 as well is **impossible in U(2)**, and the reason is structural rather than a design choice. A class-2 non-abelian pair in U(2) has [A,B] = −I exactly (Section 3), so ‖[A,B]−I‖ = 2√2, and every class-≥3 pair has some other value. The unipotent track below is where a null matched at depths 1 *and* 2 exists.

**Q16 is why one bracket is not enough.** With A a quarter-turn about ẑ and B a half-turn about x̂, [A,B] is again a ẑ-rotation. It commutes with A, so W₃ₐ = I, and all of the class-3 signal sits on W₃ᵦ. The ladder note's class-3 witness happens to have the opposite pattern (signal on W₃ₐ only), so between them the two examples show that neither bracket alone is safe.

**Unipotent track (GL(4), non-unitary).** Uni4(ε) is the ladder theorem's class-3 witness scaled by ε. Heis(ε) is a class-2 Heisenberg pair, tuned so that ‖A−I‖ agrees exactly, ‖B−I‖ agrees to within 1%, and ‖[A,B]−I‖ agrees exactly at every ε. All eigenvalues equal 1. Depth 3 is then the only difference: Uni4 has ‖W₃ₐ−I‖ = 2ε³ and W₃ᵦ = I; Heis has both = I. Readout uses real Gaussian noise, and the estimate is the shot mean.

**End-to-end track.** Holonomies are not injected. They come out of discrete Kato (parallel) transport of a 2-frame along closed horizontal loops in Gr(2,4), each built as S → S⊥ → S with prescribed holonomy, and the nested words are traversed as concatenated paths of 241 steps. Jitter (σ_path = 0.01 per step) perturbs every interior subspace on every traversal, and readout noise is σ = 0.1.

---

## 2. Results [NUM]

### 2.1 Separation (σ = 0.3, R = 20, 1000 trials, studentized)

| world | class | H₂ (depth-2) detector | H₃, single bracket | H₃, max | H₃, rss |
|---|---|---:|---:|---:|---:|
| Z | 0 | 0.046 | 0.054 | 0.055 | 0.042 |
| **D8** | **2** | **1.000** | 0.052 | 0.056 | 0.067 |
| D16 | 3 | 1.000 | 1.000 | 1.000 | 1.000 |
| **Q16** | 3 | 1.000 | **0.045** | 1.000 | 1.000 |
| Dgen | ∞ | 1.000 | 1.000 | 1.000 | 1.000 |
| WZ | ∞ | 1.000 | 1.000 | 1.000 | 1.000 |

(Binomial SE at 1000 trials is 0.007. D8's 0.067 under rss is 2.4 SE high; the 4000-trial calibration in 2.2 reads 0.048 at the same R, so it is sampling noise, not bias.)

The H₂ detector fires on D8. It cannot place anything above class 2. H₃ clears D8 at the nominal rate and fires on every class-≥3 world. The single-bracket version is blind to Q16 and returns exactly its false-alarm rate there.

### 2.2 Calibration on the class-2 null vs R (4000 trials, binomial SE ≈ 0.0035)

| R | H₂ plug-in | H₂ student | H₃ plug-in | H₃ student | H₃ max plug-in | H₃ max student |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 0.057 | 0.047 | 0.046 | 0.048 | 0.053 | 0.046 |
| 2 | **0.116** | 0.057 | **0.114** | 0.050 | 0.073 | 0.054 |
| 3 | 0.086 | 0.047 | 0.084 | 0.051 | 0.066 | 0.049 |
| 5 | 0.070 | 0.046 | 0.065 | 0.046 | 0.059 | 0.050 |
| 10 | 0.060 | 0.053 | 0.062 | 0.048 | 0.051 | 0.054 |
| 20 | 0.052 | 0.052 | 0.051 | 0.048 | 0.054 | 0.053 |
| 50 | 0.052 | 0.045 | 0.059 | 0.050 | 0.050 | 0.049 |

Yes, depth 3 has the same low-R miscalibration, and almost to the decimal (0.114 at R = 2 against H₂'s 0.116). That is expected. The plug-in mistake is in the noise estimator, not in the invariant, and the two rungs share the estimator. The studentized null removes it. It holds 0.046–0.057 at every R, R = 2 included, for both rungs. The plug-in only settles to nominal at R ≳ 10 here. H₂'s "calibrated for R ≥ 5" was slightly generous: its own 4000-trial rerun reads 0.070 at R = 5. D16 and Q16 are detected at 1.00 for every R ≥ 1 because their nested holonomies are a full half-turn away from I.

A note on D8 versus pure noise. Under direct readout, D8's nested loops *are* identity loops, so the depth-3 statistic has the same law on D8 as on Z. That is what Theorem 1 promises, and it is why the null can be simulated without knowing the world. D8 is reported because the H₂ detector fires on it.

### 2.3 Repetitions needed vs holonomy angle (NN(ε), σ = 0.3, α = 0.05, power 0.8)

ε is the rotation angle, R(n̂,ε) = exp(−iε n̂·σ/2), the convention in `h2_nonabelian_experiment.py`. In the generator-angle convention exp(−it n̂·σ) the same row is t = ε/2. The figures quoted earlier for "angle 0.1" (depth 2 ≈ 0.028, depth 3 ≈ 0.0056) are this table's ε = 0.2 row.

| ε | ‖W₂−I‖ | depth-3 T (truth) | R₈₀ H₂ | R₈₀ H₃ | ratio | FAR at R₈₀(H₃) |
|---:|---:|---:|---:|---:|---:|---:|
| 1.0 | 0.650 | 0.774 | 2.3 | 1.5 | 0.7 | 0.050 |
| 0.5 | 0.173 | 0.117 | 19 | 51 | 2.7 | 0.054 |
| 0.3 | 0.063 | 0.026 | 142 | 1.0 × 10³ | 7.2 | 0.043 |
| 0.2 | 0.028 | 0.0079 | 691 | 1.1 × 10⁴ | 16 | 0.047 |
| 0.1 | 0.0071 | 0.0010 | 1.1 × 10⁴ | **6.5 × 10⁵** | 60 | 0.053 |
| 0.05 | 0.0018 | 1.3 × 10⁻⁴ | 1.8 × 10⁵ | 4.0 × 10⁷ | 226 | 0.057 |
| 0.03 | 6.4 × 10⁻⁴ | 2.7 × 10⁻⁵ | 1.4 × 10⁶ | **9.2 × 10⁸** | 661 | 0.043 |

The fitted log-log slopes for ε ≤ 0.2 are −4.01 for depth 2 and −5.96 for depth 3, against −4 and −6 in theory. The R₈₀·signal² column is flat (≈0.55 for depth 2, ≈0.65–0.71 for depth 3), so to a good approximation

  R₈₀(H₃) ≈ 7.5 σ² ε⁻⁶,  R₈₀(H₂) ≈ 12 σ² ε⁻⁴,

and the price of H₃ over H₂ grows as ε⁻². At ε = 1 they cost the same. At ε = 0.1 H₃ costs 60 times more, and at ε = 0.03 it costs 660 times more. The false-alarm rate stays nominal out to R ≈ 10⁹, so calibration does not drift at large R. Only the cost does.

### 2.4 Unipotent track: a null matched at depths 1 and 2

| ε | R | H₂ on Heis | H₂ on Uni4 | H₃ FAR on Heis | H₃ power on Uni4 |
|---:|---:|---:|---:|---:|---:|
| 0.5 | 20 | 0.960 | 0.966 | 0.053 | 0.441 |
| 0.5 | 100 | 1.000 | 1.000 | 0.044 | 1.000 |
| 0.2 | 5000 | 1.000 | 1.000 | 0.046 | 0.485 |
| 0.1 | 200000 | 1.000 | 1.000 | 0.051 | 0.290 |

Here the H₂ detector is matched to the decimal on null and alternative, because its observable is equal by construction. H₃ alone separates them. R₈₀ for Uni4 is 40, 770, 8.6 × 10³, 5.5 × 10⁵, 3.6 × 10⁷ at ε = 0.5, 0.3, 0.2, 0.1, 0.05. R₈₀·signal² is again flat at ≈2.2 (larger than in U(2) because only one bracket carries signal, spread over 16 real components with no Procrustes projection). Across all nine (ε, R) cells, the false-alarm rate on Heis runs 0.044–0.060.

### 2.5 The nested loop has to be read as a loop (σ = 0.3, R = 20)

H₂'s "corroborating readout" assembled the bracket from separately estimated Ĥol_A, Ĥol_B. At depth 3 the two readouts behave very differently:

| world | true T | direct (median) | assembled (median) | assembled bias |
|---|---:|---:|---:|---:|
| Z | 0 | 0.128 | 7.9 × 10⁻⁴ | +7.9 × 10⁻⁴ |
| D8 | 0 | 0.128 | **0.395** | **+0.395** |
| D16 | 4.000 | 3.998 | 3.986 | −0.014 |
| NN(0.2) | 7.9 × 10⁻³ | 0.127 | 9.7 × 10⁻³ | +1.8 × 10⁻³ |
| NN(0.1) | 1.0 × 10⁻³ | 0.127 | 2.1 × 10⁻³ | +1.1 × 10⁻³ |

Two things follow, and they pull in opposite directions.

On the class-2 null D8, the assembled bracket sits far from I, because noise in Â and B̂ is propagated through a large [A,B] = −I. On Z it is nearly zero. So the assembled statistic's null law depends on the unknown lower-depth structure, and there is no world-free matched null for it. The direct readout's null law is the same for every class-≤2 world. That is the only reason the depth-3 test above can be calibrated without knowing the world.

Near the identity, though, assembly is dramatically more *efficient*. Its error is suppressed by the square of the single-loop holonomy size, plus a noise-cubed floor, while the direct readout pays the full σ_eff no matter how small the signal. At NN(0.1), the assembled estimate sits within 0.003 of a 0.001 signal, while the direct estimate has a noise floor of 0.127. The ε⁻⁶ cost in 2.3 therefore belongs to the *direct nested-loop readout*, not to depth 3 as such. An assembled depth-3 test would cost closer to the single-loop rate. The catch is that it is biased upward by noise-generated brackets (+1.1 × 10⁻³ on a signal of 1.0 × 10⁻³), so it needs a model-based null: fit the nearest class-2 pair, then bootstrap from it. That null is not built here. **[OPEN]**

### 2.6 End-to-end: Kato transport, not injection

Noiseless transport along the concatenated paths reproduces the algebraic word holonomies to 2.5 × 10⁻¹⁶ – 4.5 × 10⁻¹⁵ for D8, D16, Q16 and WZ. Discrete polar transport is exact on these geodesic segments, so there is no discretization bias to leak into the class-2 null. With jitter, a single loop's holonomy wanders by 0.017 rms, the nested loop by 0.056 rms, and the mean nested holonomy on D8 stays within 0.0015 of I. That is the second-order bias, too small to matter at these R.

| R | D8 FAR, all-component σ̂ | D8 FAR, tangent σ̂ | D16 power | Q16 power | Z FAR, tangent σ̂ |
|---:|---:|---:|---:|---:|---:|
| 5 | 0.070 | 0.035 | 1.00 | 1.00 | 0.050 |
| 20 | 0.062 | 0.050 | 1.00 | 1.00 | 0.058 |
| 100 | 0.073 | 0.033 | 1.00 | 1.00 | 0.047 |

(n = 400 trials at R = 5, 20, binomial SE 0.011; n = 150 at R = 100, SE 0.018.)

This exposed a calibration mode that injected holonomies cannot show. Path jitter moves the holonomy *along the group*. Its spread is almost entirely anti-Hermitian (Hermitian/anti-Hermitian ratio 0.03), while readout noise is isotropic. H₂'s estimator pools all eight real components. It therefore underestimates the spread in exactly the directions that Procrustes keeps, and the false-alarm rate creeps to 0.06–0.07. Estimating σ̂ from the tangent (anti-Hermitian) part of the shot deviations, the components the statistic actually uses, brings it back to 0.033–0.058, conservative if anything. The same fix applies to H₂ once its holonomies come from transport rather than injection.

---

## 3. A shortcut the unitary setting already provides [THM]

**Proposition.** Let A, B ∈ U(n) generate a non-abelian group of class 2. Then ‖[A,B] − I‖_F ≥ g(n) := min over 2 ≤ d ≤ n of 2√d sin(π/d).

*Proof.* Class 2 makes C = [A,B] central in G = ⟨A,B⟩. Unitarity makes the representation completely reducible into G-irreducible blocks. On each block C is a scalar c (Schur). The restriction of a commutator to an invariant block has determinant 1, so c^d = 1 for a block of dimension d. If c = 1 on every block then C = I and G is abelian, so some block has c ≠ 1, which forces d ≥ 2 and |1 − c| ≥ 2 sin(π/d). That block alone contributes √d |1−c| to ‖C − I‖_F. ∎

g(2) = g(3) = g(4) = 2√2 ≈ 2.83. g(8) ≈ 2.17, g(64) ≈ 0.79, g(256) ≈ 0.39, and g(n) ~ 2π/√n for large n.

> **Sharper form (`gap-rung.md` Proposition 1; `RECONCILIATION.md` R7).** The dimension of each irreducible block *equals* the order of c (c is a primitive m-th root of unity on an m-dimensional block), not merely c^d = 1. That gives the complete list of class-2 commutator spectra, which an exact null needs. g(n) is unchanged.

**Consequence.** In a fiber of known dimension n, under full-frame readout, a commutator loop that reads *confidently* nonzero and *confidently* below g(n) already certifies class ≥ 3 from the *depth-2* loop alone. "Confidently" is load-bearing: a raw d̂ < g(n) rule false-alarms on D8 with probability 1, because at C = −I the estimate is biased at second order. `gap-rung.md` builds the calibrated test (an intersection-union test with an se² pivot at ±1 spectra). In U(2) this covers every non-abelian world here except the D8 null, which sits exactly on the gap: D16 and Q16 (2.000), Dgen (2.380), WZ (2.770), and every small-holonomy NN(ε). H₂'s own readout, plus unitarity, plus n, already places a small-holonomy Kato world above class 2.

So in the regime that costs 6.5 × 10⁵ shots at ε = 0.1, H₃ is logically redundant with H₂ for unitary transport in small fibers. It adds independent information in three places:

1. **non-unitary transport** (the GL track: dissipative, non-Hermitian or otherwise non-Kato connections), where class-2 commutators are not quantized and Heis-type nulls sit arbitrarily close to I;
2. **projected readout**, where the naive gap does not survive (`gap-rung.md` §4b), and **large fiber dimension**, where g(n) closes like 1/√n. Under full-frame readout n is the readout dimension, so "unknown n" is not the operative exception; an understated n is fatal to the shortcut, an overstated one only costs power;
3. a certificate that must **not lean on the representation theory of U(n)**. Theorem 1 is dimension-free and model-free; the shortcut is neither.

This is the "virtually abelian" observation turned into a usable bound. It also says how to read the ladder above depth 2 for Kato holonomy: the rungs stay well-defined, but in small fibers their *information* is front-loaded into depth 2.

---

## 4. Verdict

**GO, for the instrument, with the cost and scope stated.** Under full-frame direct readout H₃:

1. **detects** class-≥3 holonomy on every such world tested (D16, Q16, Dgen, WZ, Uni4, NN), including Q16, whose signal sits only on [[A,B],B];
2. **stays calibrated against the H₂ comparator** (matched class-2 worlds D8, Heis): 0.046–0.057 false alarms at every R from 1 to 50 with the studentized null, 0.044–0.060 on Heis across nine (ε, R) cells, and nominal out to R ≈ 10⁹;
3. **separates what depth 2 cannot.** The H₂ detector fires at 1.00 on the class-2 null and, on the unipotent track, at identical rates on null and alternative;
4. **survives end-to-end Kato transport** once σ̂ is taken from the tangent components.

It does **not** come cheap near the identity. R₈₀ ≈ 7.5 σ² ε⁻⁶: 51 shots at ε = 0.5, about 10⁴ at 0.2, 6.5 × 10⁵ at 0.1, 9 × 10⁸ at 0.03. For small holonomies the direct rung is an instrument for large-holonomy worlds or for non-unitary transport. For small unitary holonomies under full-frame readout, Section 3's shortcut does the same job from depth-2 data; `gap-rung.md` gives the calibrated version, R₈₀ ≈ 13 σ²ε⁻⁴.

**Claim language.** "A positive H₃ result certifies that the holonomy group is not nilpotent of class ≤ 2 (class ≥ 3, a lower bound), in any representation dimension, under full-frame readout (Ladder Theorem 1). It does not determine the class." H₂ should be described the same way: *non-abelian* (class ≥ 2), not "class 2".

---

## 5. Limitations

- **Readout regime.** Everything is full-frame. The projected-readout exclusion is still open at depth 3, as it is at depth 2. **[OPEN]**
- **Injection.** The main tracks inject holonomies. The end-to-end track transports them, but along constructed geodesic loops in Gr(2,4) with Gaussian jitter. It is not a physical Hamiltonian family, and not real data.
- **Assembled readout.** Far more efficient near I, but lacking a world-free null. A fitted-class-2 parametric null is the obvious next build. **[OPEN]**
- **Combination rule.** The rss statistic is used throughout. Max is equally calibrated, and on one-bracket worlds such as Q16 it should have the edge, but its power advantage was not swept.
- **Noise model.** Gaussian, independent across shots and loops. Correlated drift between the two nested loops, which share every letter, was not modeled. Under the tangent-σ̂ estimator it would push FAR up, not down.
- **Q16 and D16 are large holonomies.** They are detected at R = 1, so they show separation, not sensitivity. The sensitivity statements come from NN(ε) and Uni4(ε).

---

*Companion: `src/h3_nested_experiment.py` (all seven sections, numpy only, ≈15 min on 4 cores), `outputs/h3_nested_experiment.txt` (captured output). Builds on `h2-nonabelian-rung.md`, `comparator-ladder-theorem.md`, `src/ladder_theorem.py`.*

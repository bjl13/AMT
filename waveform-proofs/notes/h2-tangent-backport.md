# H₂ with the tangent-component σ̂
## Back-porting the H₃ noise fix to the non-abelian rung

**What changed.** H₂ (`notes/h2-nonabelian-rung.md`) reads the commutator loop [a,b] directly, takes δ = ‖Ŵ − I‖_F with Ŵ = Procrustes(mean of R shots), and tests it against the abelian prediction Hol_C = I. A positive result certifies non-abelian holonomy (class ≥ 2), a lower bound. Two things in its calibration are replaced here, both taken from the H₃ rung (`notes/h3-nested-rung.md`):

1. **Studentized null.** The plug-in null (σ̂ estimated, then treated as known) becomes a bootstrap-t: δ/σ̂ is compared with null draws δ*/σ̂*, where each σ̂* is re-drawn from its χ² law. This is H₃ §1's fix for the low-R wobble.
2. **Tangent σ̂.** σ̂ is estimated from the anti-Hermitian part of Ŵ†(Y − Ȳ), the n² real directions that Procrustes keeps, instead of from all 2n² real components. This is H₃ §2.6's fix for transported holonomy, whose spread lies almost entirely along the group.

The observable, the null hypothesis and the claim are unchanged. Only the noise calibration moves.

Rigor flags: **[NUM]** numerical (`src/h2_tangent_experiment.py`, output in `outputs/h2_tangent_experiment.txt`); **[THM]** proved; **[OPEN]** open.

---

## 1. Why the tangent estimate is the right one [THM, elementary]

Let Y = W + E with E isotropic complex Gaussian, v per real component. Write the deviation in the frame of Ŵ: T = Ŵ†(Y − Ȳ). To first order, Procrustes keeps the anti-Hermitian part of T and discards the Hermitian part. So the noise that reaches δ is the tangent noise. Under isotropic noise both parts have per-component variance v, so the all-component and tangent estimates are both unbiased. The tangent one has half the degrees of freedom, n²(R − 1) against 2n²(R − 1). This is checked in §0 of the output: both estimates average 0.0449–0.0450 against v = 0.045, and the tangent estimate's variance is 1.96–2.00 times larger.

Transport noise is not isotropic. Path jitter perturbs the holonomy *within* U(n), so its spread is tangent. On the abelian null AB under Kato transport, the Hermitian/anti-Hermitian spread ratio is 0.019–0.056 (§2). Pooling all components then averages a tangent variance v_read + v_jit with a Hermitian variance v_read, which underestimates exactly the part δ uses.

---

## 2. Results [NUM]

### 2.1 Injected holonomies, isotropic readout (σ = 0.3, H₂'s own setting)

False alarms on the abelian nulls, Z and AB (AB is spectrum-matched to NA). 4000 trials, so the binomial SE is 0.0035. All three calibrations are applied to the same shots in every cell.

| R | plug-in, all (original H₂) | student, all | student, tangent |
|---:|---:|---:|---:|
| 2 | **0.139 / 0.130** | 0.052 / 0.048 | 0.054 / 0.044 |
| 3 | 0.095 / 0.089 | 0.049 / 0.045 | 0.048 / 0.049 |
| 5 | 0.075 / 0.068 | 0.048 / 0.046 | 0.050 / 0.049 |
| 10 | 0.062 / 0.060 | 0.052 / 0.047 | 0.052 / 0.045 |
| 20 | 0.056 / 0.053 | 0.051 / 0.051 | 0.052 / 0.050 |
| 50 | 0.054 / 0.055 | 0.051 / 0.055 | 0.053 / 0.053 |

(Each cell gives Z / AB.)

The original plug-in is over the nominal 0.05 until R ≈ 20. It reads 0.07 at R = 5, so the original note's "calibrated for R ≥ 5" was generous, as H₃ §2.2 already found. Both studentized versions hold 0.044–0.055 from R = 2.

**What the tangent estimate costs here.** With isotropic noise it buys nothing, and its halved degrees of freedom cost a little power at very small R. NA at R = 2 is detected at 0.98 instead of 1.00. NN(0.5) at R = 5 gives 0.215 against 0.233. By R = 20 the two are within 0.01, and on NN(0.3) and NN(0.2) at R = 50–1500 they agree to ±0.01 (0.346 against 0.349, 0.775 against 0.770). So R₈₀ for small holonomy is unchanged, and H₂'s R₈₀ ≈ 12σ²ε⁻⁴ (H₃ §2.3) stands. The plug-in's apparent power edge at small R (0.284 on NN(0.5) at R = 5) is inflated by its false alarms.

### 2.2 End-to-end Kato transport

Discrete Kato transport of a 2-frame in Gr(2,4), using H₃'s construction. The commutator word runs as one 97-step concatenated loop. Without noise, transport reproduces the algebraic commutator holonomy to 1.5 × 10⁻¹⁶ – 2.0 × 10⁻¹⁵ for AB, NA, D8 and NN(0.5). Readout σ is 0.1 (v = 0.005), and path jitter σ_path is swept.

| σ_path | jitter tangent variance ÷ readout variance | commutator-loop rms ‖Hol − I‖ on AB |
|---:|---:|---:|
| 0.01 | 0.06 | 0.035 |
| 0.02 | 0.25 | 0.070 |
| 0.03 | 0.56 | 0.106 |

False alarms on the abelian nulls (max of Z and AB in each cell; 2000 trials, 1000 at R = 100, SE ≈ 0.005–0.007):

| σ_path | R | plug-in, all | student, all | student, tangent |
|---:|---:|---:|---:|---:|
| 0.01 | 2 | 0.145 | 0.059 | 0.055 |
| 0.01 | 5 | 0.090 | 0.059 | 0.059 |
| 0.01 | 20 | 0.066 | 0.057 | 0.053 |
| 0.01 | 100 | 0.061 | 0.058 | 0.053 |
| 0.02 | 2 | 0.168 | 0.061 | 0.053 |
| 0.02 | 5 | 0.103 | 0.070 | 0.054 |
| 0.02 | 20 | 0.082 | **0.077** | 0.054 |
| 0.02 | 100 | 0.082 | **0.085** | 0.051 |
| 0.03 | 2 | 0.208 | 0.083 | 0.053 |
| 0.03 | 5 | 0.135 | **0.098** | 0.049 |
| 0.03 | 20 | 0.113 | **0.104** | 0.051 |
| 0.03 | 100 | 0.092 | **0.091** | 0.049 |

Across all twelve cells and both null worlds the tangent version reads 0.036–0.059. The all-component bootstrap-t stays acceptable at σ_path = 0.01 (0.049–0.059). There the commutator loop's jitter is only 6% of the readout variance, because the loop has four letters against H₃'s ten. As jitter grows it drifts up to 0.10, and studentizing cannot fix it, because the bias is in what σ̂ measures, not in how its uncertainty is handled. The original plug-in carries both errors and reaches 0.21.

Power on the non-abelian worlds: NA and D8 are detected at 1.000 in every cell under every calibration. On the small-holonomy NN(0.3) world the tangent version reads lower when jitter is large (0.682 against 0.764 at σ_path = 0.03, R = 20). Most of that gap is the all-component version's excess false-alarm rate, about 0.05 at that cell. The rest is honest: the tangent σ̂ correctly counts jitter as noise. By R = 100 all versions read 1.000.

---

## 3. Verdict

**Adopt the studentized, tangent-σ̂ calibration as H₂'s detector.**

- It is calibrated from R = 2, on injected holonomies and under end-to-end Kato transport, at every jitter level tested (0.036–0.059 on abelian nulls).
- It costs essentially no power. R₈₀ ≈ 12σ²ε⁻⁴ is unchanged, and the only measurable loss is at R ≤ 5 under isotropic noise.
- The original plug-in is miscalibrated below R ≈ 20 under injection (0.139 at R = 2, 0.075 at R = 5) and at every R under transport jitter (up to 0.21).

**Changes to earlier claims.**

1. `h2-nonabelian-rung.md` §2 says the detector "is calibrated for R ≥ 5". With the plug-in null that holds only from R ≈ 20; the paired 4000-trial rerun reads 0.075 / 0.068 at R = 5. With the recalibration it holds from R = 2.
2. H₃ §2.6 said the tangent fix "applies to the non-abelian rung once its holonomies come from transport". Confirmed. At H₃'s σ_path = 0.01 the effect on H₂ is small (0.059 against 0.053) because the commutator loop is shorter. It reaches 0.08–0.10 when jitter is a quarter to half of the readout variance.
3. The H₂ claim language is unchanged: non-abelian (class ≥ 2), a lower bound.

## 4. Limitations

- Same readout regime as before, full-frame. The projected-readout exclusion stays **[OPEN]**.
- Transport is along constructed geodesic loops with Gaussian jitter that is independent across steps and shots. Correlated drift across shots, such as a slow systematic offset, would bias the mean and is not modeled. No σ̂ estimator fixes it.
- The null draws use isotropic noise at the tangent scale, which overstates the Hermitian part under jitter. That is conservative to first order, because Procrustes discards it, and is consistent with the slightly low 0.036 cell.

*Files: `src/h2_tangent_experiment.py` (numpy only, seeded, ≈18 min on 4 cores) and `outputs/h2_tangent_experiment.txt` (captured output).*

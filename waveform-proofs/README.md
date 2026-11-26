# waveform-proofs

Reproducible numerical verification for the Observer-Indexed Dual Hypergraph
with Incidence Waveforms — the computational backbone of the Curvature
Anthology. Every claim labeled [NUM] in the anthology is regenerated here.

## Layout

```
src/
  metrics.py          core waveform metrics (shared)          [v2 sec 1.5]
  clifford.py         Clifford-Koszul curved complex          [Anthology I]
  worked_example.py   worked example + synthetic ensemble      [v2 5.1]
  berry_kato.py       Berry phase via Kato transport (k=1)      [Thm 1, test A]
  wilczek_zee.py      non-abelian holonomy Gr(2,4) (k=2)        [Thm 1, test B]
  mobius.py           Mobius spectra (R) + torsion (Z)          [II.3, test C]
  resonance_table.py  cover-resolution dichotomy               [II.3, test D]
  field_trial.py      GO/NO-GO on real data (sklearn digits)    [III, 5.3]  H0
  h1_monodromy_experiment.py   abelian monodromy detector       H1
  h2_nonabelian_experiment.py  commutator-loop detector         H2
  h3_nested_experiment.py      nested-commutator detector       H3
  h2_tangent_experiment.py     H2 with tangent sigma-hat        H2
  gap_rung_experiment.py       spectral-gap class>=3 test       H3 via gap
  ladder_theorem.py   exact LCS demonstration of the ladder     [ladder theorem]
Makefile              `make all` runs everything, captures outputs/
requirements.txt
outputs/              captured canonical stdout of each script
```

## Run

```bash
pip install -r requirements.txt
make all          # full battery -> outputs/*.txt
make clifford     # or any single target (see `make` comments)
```

## What each script proves

| script | result | rigor |
|---|---|---|
| clifford.py | (d_perp)^2 = w*id to 1e-14 over random orthogonal projectors and (m,k); (M_v,d_perp) is a matrix factorization of the superpotential w | numerical witness of Theorem I.1/I.2 |
| berry_kato.py | Kato holonomy phase = -pi(1-cos theta) to 1e-7 | validates Theorem 1, k=1 |
| wilczek_zee.py | ||[Hol_A,Hol_B]|| = 2.77 (non-abelian); disjoint-plane control commutes | validates Theorem 1, k>1 |
| mobius.py | twisted Laplacian spectrum = 2-2cos((2j+1)pi/n) to 1e-15; Smith form diag(1..1,2) => H^1=Z/2 | Part II.3 example |
| resonance_table.py | growth kills finite-order (geom. series), never full resonance, never irrational | Theorem II.3 |
| field_trial.py (H₀) | real corpus: tension>0 10/10, pairwise flips 26.3%, mono-viol 8.9% => additive null rejected | Part III GO (phenomenon detection only) |
| `h1_monodromy_experiment.py` (H₁) | abelian U(1) monodromy recovery vs fitted static (H₀) competitor; falsifier that doesn't fire on noise; certifies non-trivial holonomy | h1-abelian-rung.md |
| `h2_nonabelian_experiment.py` (H₂) | U(2) loop-order dependence vs spectrum-matched abelian (H₁) null; signature with no additive/abelian shadow; certifies non-abelian (class ≥ 2) | h2-nonabelian-rung.md |
| `h3_nested_experiment.py` (H₃) | nested commutators [[a,b],a], [[a,b],b] vs matched class-2 (H₂) null, studentized; unipotent, end-to-end Kato and unitary-gap sections; certifies class ≥ 3 | h3-nested-rung.md |
| `h2_tangent_experiment.py` (H₂) | studentized tangent-σ̂ calibration for H₂: size 0.036–0.059 from R = 2, injected and under Kato transport; plug-in reaches 0.21 | h2-tangent-backport.md |
| `gap_rung_experiment.py` (H₃ via gap) | intersection-union test on the H₂ readout against every class-2 spectrum in U(n); certifies class ≥ 3 at H₂'s cost, R₈₀ ≈ 13σ²ε⁻⁴; unitary, full-frame | gap-rung.md |
| `ladder_theorem.py` | exact demonstration that the ladder H₀ ⊊ H₁ ⊊ H₂ ⊊ H₃ is the lower central series: the depth-k commutator separates H_k from H_{k−1}; abelian => depth-2 = 0 in any dimension | comparator-ladder-theorem.md |
| worked_example.py | exact reproduction of source-doc numbers; monotonicity violation exhibited | v2 5.1 |

Determinism: all RNG seeded (field trial seed=42, ensemble seed=0). Numbers
are bit-stable across runs on a given numpy/BLAS.

## Detector ladder (naming)

The hypothesis hierarchy is named by the comparator ladder theorem
(`notes/comparator-ladder-theorem.md`). H_k is the class of holonomies nilpotent
of class ≤ k; the H_k detector uses the depth-k commutator observable to reject
H_{k−1}, so a positive result certifies class ≥ k, a lower bound.

| label | detector | null rejected | certifies |
|---|---|---|---|
| H₀ (static) | field trial, projection signatures | none (phenomenon detection) | — |
| H₁ (abelian) | single-loop winding | H₀, fitted static | non-trivial holonomy |
| H₂ (non-abelian) | commutator loop [a,b] | H₁, spectrum-matched abelian | class ≥ 2 |
| H₃ (nested ordering) | nested loops [[a,b],a], [[a,b],b] | H₂, matched class 2 | class ≥ 3 |

## This folder

`src/` holds every script that was supplied, `outputs/` the canonical captures,
`notes/` the ladder notes, and `RENAMES.md` the old → new map for the H₀–H₃
naming.

- **Rerun and checked:** all twelve scripts are in `src/` (metrics.py is the shared
  library). Ten of the eleven runnable scripts reproduce their captures byte for byte; wilczek_zee differs only in the 1e-14 unitarity-error
  digits (BLAS roundoff), with holonomies, ||[Hol_A,Hol_B]|| = 2.770314 and the
  control unchanged.
- **Added Nov 26:** `src/h2_tangent_experiment.py` with `notes/h2-tangent-backport.md`
  (studentized tangent σ̂ for H₂, now the recommended H₂ calibration) and
  `src/gap_rung_experiment.py` with `notes/gap-rung.md` (class ≥ 3 from the depth-2
  loop via the U(n) spectral gap; unitary, full-frame only). Captures are in
  `outputs/`. `notes/` now holds six notes.

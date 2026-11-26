# Reconciliation log

The rule (Brian, Nov 26, 2026): where documents conflict, favor correctness and
future expansion over whichever version carries a later date, because the work
is written asynchronously. Original wording is kept wherever it is still true;
each change below is either a dated *Repo note* inserted beside the passage or
a correction made in place, and both say which entry here they come from.

## Calls made

**R1. Theorem status: spec v2 vs monograph.**
Spec v2 marks Theorems 1–3 [TIR], Proposition 4 [TIR-c] and lists five open
items. The monograph proves them (Theorems IV.1–IV.3, III.2; linear Conjecture 5
= Theorem IV.5) and the anthology closes all five items.
*Won:* monograph. *Why:* later proofs supersede in-reach labels; the spec's
grammar, duality, citations and serialization are still normative, so its text
stays. *Change:* status note under the spec's header.

**R2. What the field trial rejects.**
Spec v2 §5.2, anthology Part III and monograph V.2/V.3 say a nonzero (P3) rate
"falsifies every additive model" and read the digits GO as support for the
waveform apparatus. The H₁ note records the audit finding that plain vector
addition under projection produces (P1)–(P3) as well, which is why the synthetic
ensemble fires on iid Gaussians.
*Won:* the H₁ note. *Why:* it is the correct statement and it is what the
ladder is built on. The claim stays true for scalar, nonnegative-weight additive
scoring, so the original sentences are kept with their scope stated. *Change:*
scope notes at spec §5.2, anthology Part III verdict, monograph V.2; the
monograph header note repeats it.

**R3. Anthology vs monograph.**
Same results, different numbering and some re-wording.
*Won:* monograph as the reference text. *Why:* it is self-contained, carries
the code inline, and its listings match `waveform-proofs/src/` exactly.
*Change:* numbering map in the anthology's header note (I.1→III.1, I.2→III.2,
I.3→III.3, I.4→III.4, I.7→III.5, I.8→III.6, II.1→IV.4, II.2→IV.5, II.3→IV.6,
VI.1→B.1). `waveform-proofs/README.md` cites anthology numbers; the map
resolves them.

**R4. Monograph Part VII module map vs `waveform-proofs/`.**
Part VII lists 8 scripts; the folder holds 14, including the ladder H₁–H₃,
the H₂ tangent back-port and the gap rung.
*Won:* `waveform-proofs/`. *Why:* it is what runs. The 8 listings were diffed
against `src/` and are identical. *Change:* note in Part VII's intro; `src/` is
named authoritative if they ever drift.

**R5. AMT D.4.2: is the needed object known?**
The draft says no known construction meets D.4.1's four conditions. The curved
A∞ report identifies curved A∞-structures and mapping tori as the framework,
and the monograph proves the waveform instances (Theorems III.2, IV.2).
*Won:* neither wholly. *Why:* the later work speaks to graded compatibility
(condition 1) and the helical geometry, and proposes encoding policy (4) in m₀
without proving it; it does not address entropic monotonicity (2) or void
regularity (3). Saying ∇^av is now known would be
wrong; saying nothing has moved would be too. *Change:* note after D.4.2; ∇^av
and D.3.γ stay open.

**R6. H₂ calibration.**
`h2-nonabelian-rung.md` said the plug-in null "is calibrated for R ≥ 5" and
the verdict read "GO for H₂ (regime R ≥ 5)". The back-port's paired 4000-trial
rerun shows 0.075 / 0.068 at R = 5, calibration only from R ≈ 20 under
injection, and up to 0.21 under Kato transport with jitter. The studentized
tangent σ̂ is calibrated from R = 2.
*Won:* `h2-tangent-backport.md`. *Why:* more trials, more settings, and it
names the cause. *Change:* correction paragraph in H₂ §2; verdict heading,
verdict item 3 and the closing "remaining gap" sentence updated. Invariant and
claim language (class ≥ 2) unchanged.

**R7. H₃ §3 shortcut.**
H₃ §3 stated the block condition as c^d = 1, said any measured
0 < ‖[A,B] − I‖ < g(n) certifies class ≥ 3, and listed "large or unknown
fiber dimension" as an exception. The gap rung proves block dimension equals
the order of c, shows a raw d̂ < g(n) rule false-alarms on D8 with probability 1
(second-order bias at C = −I), and finds the operative exception is projected
readout; understated n is fatal, overstated n costs power only.
*Won:* `gap-rung.md`. *Why:* it is the calibrated, tested version of the same
proposition. *Change:* sharper-form note after the proposition; "Consequence",
exception 2 and the verdict's closing sentence corrected. The proof as written
remains valid for the bound g(n).

**R8. Ladder names across the corpus.**
The H₀–H₃ rename applies to the detector ladder only.
*Won:* the rename, scoped. *Why:* AMT's void homology H_k and the anthology's
and monograph's H⁰/H¹ are standard notation with a different meaning; renaming
them would be wrong. *Change:* none in `docs/`; the top-level README explains
both families.

**R9. Captured outputs vs reruns.**
Rerun on Nov 26 in this environment (numpy 2.5.3, scipy 1.18.1, sympy 1.14.0,
scikit-learn 1.9.1), all 13 runnable scripts via `make`. Every reported number
matches its capture except wilczek_zee's last unitarity-error digits; the only
other differences are `runtime` lines (gap rung, H₂ tangent and H₃ included).
*Won:* captures as committed, unless a rerun changes a reported number. *Why:*
last-digit BLAS roundoff is not a result, and churning captures on it hides
real changes. wilczek_zee differs only in its ~1e-14 unitarity-error digits
(1.3e-14 / 1.5e-14 here against 1.7e-14 / 9.7e-15 captured).

## Noted, not changed

- **N1. Maurer–Cartan form.** The curved A∞ report writes Σₙ mₙ(b,…,b) = 0
  with the sum from n = 0; the anthology and monograph write
  Σ_{k≥1} m_k(b,…,b) = −m₀. Same equation.
- **N2. Base of the helix.** The curved A∞ report needs an S¹ base (or
  quasi-periodic return) for non-triviality, since bundles over ℝ are trivial.
  The AMT draft treats the entropic reference 𝒯 as totally ordered. The
  monograph's mapping torus sits over the frame loop. How 𝒯 and the S¹ base
  relate is not settled in any document here.
- **N3. Citations in the curved A∞ report** (for example "Cohn's theorem" and
  "the APT correspondence (2025)") have not been checked against the
  monograph's corrected citation spine.
- **N4. Namespace target.** Anthology Part V and monograph VI.2 point redirects
  at `https://bjl13.org/ns/waveform/` and describe artifacts
  (`w3id-waveform-pr/`, `waveform-ns/`) that were not supplied. Left as written.
- **N5. Older names in conversation.** "Conjecture VI.1" (anthology) and
  "Conjecture B.1" (monograph) are the same conjecture.

## Not included

- 29 uploads that are byte-identical to files already in `waveform-proofs/`,
  or are their pre-rename originals (old `nonabelian_experiment.py`,
  `monodromy_experiment.py`, `ladder_theorem.py`, their captures, and the
  pre-rename `discriminating-experiment.md`, `nonabelian-rung.md`,
  `comparator-ladder-theorem.md`). The renamed versions are in the repo and
  `waveform-proofs/RENAMES.md` maps every one.
- Two earlier drafts of the `waveform-proofs` README, superseded by the
  current one.

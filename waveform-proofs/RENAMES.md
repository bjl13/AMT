# Rename map: detector ladder → H₀–H₃

Scheme from `notes/comparator-ladder-theorem.md` §6. H_k names the hypothesis class
(holonomy nilpotent of class ≤ k) and the rung whose depth-k detector rejects H_{k−1}.
A positive H_k result certifies class ≥ k (a lower bound), never "class k".

| old name | new name |
|---|---|
| field trial (as a ladder level) | H₀ (static) |
| abelian rung, abelian experiment, discriminating experiment | H₁ (abelian) |
| non-abelian rung, non-abelian experiment / detector | H₂ (non-abelian) |
| depth-3 rung, depth-3 detector, third rung | H₃ (nested ordering) |
| Comparator 0 / 1 / 2 / 3 (meaning the hypothesis) | H₀ / H₁ / H₂ / H₃ |
| "H₂ = class-2", "class-2 (Comparator-2) holonomy" | H₂ = class ≤ 2; detector certifies class ≥ 2 |

## Files

| old file (upload or earlier output) | new file |
|---|---|
| comparator-ladder-theorem.md (upload a2975df4…) | notes/comparator-ladder-theorem.md (name kept) |
| discriminating-experiment.md (upload ec7b5f99…) | notes/h1-abelian-rung.md |
| nonabelian-rung.md (upload fc42c1e3…) | notes/h2-nonabelian-rung.md |
| depth3/depth3-rung.md | notes/h3-nested-rung.md |
| ladder_theorem.py (upload 41c4e3bf…) | src/ladder_theorem.py (name kept) |
| nonabelian_experiment.py (upload cf066289…) | src/h2_nonabelian_experiment.py |
| depth3/depth3_experiment.py | src/h3_nested_experiment.py |
| ladder output (upload 43802c98…) | outputs/ladder_theorem.txt |
| nonabelian output (uploads 5a8838f6…, 101e9ca1…) | outputs/h2_nonabelian_experiment.txt |
| depth3/depth3_experiment.txt | outputs/h3_nested_experiment.txt |
| README (uploads 0ed1207a…, older; 2c619060…, newer, used) | README.md |
| monodromy_experiment.py (upload 3529b8af…) | src/h1_monodromy_experiment.py |
| monodromy output (upload b36043f4…) | outputs/h1_monodromy_experiment.txt (rerun, identical) |

The earlier `depth3/` folder is replaced by the files above. Uploads are untouched.

## Changes by file

**comparator-ladder-theorem.md**
- §1: "H₂ = class-2" → "H₂ = class ≤ 2"; "(Comparator k)" aliases dropped; H₃ added to the list.
- §1: new paragraph "Class versus detector": H_k as class (≤ k) vs H_k as detector (rejects H_{k−1}, certifies ≥ k).
- §2 table header "holonomy" → "witness holonomy" (the rows are exactly class k, which is correct as witnesses).
- §2 machine-zero range 5.5×10⁻¹⁶–1.3×10⁻¹⁴ → 3×10⁻¹⁶–1.3×10⁻¹⁴ (see Outputs below).
- §2 flat connection: "it lies in H₂, not H₁" → "it lies outside H₁ (class ≥ 2)" (a non-abelian flat holonomy need not be class ≤ 2); "defines Comparator 1" → "defines H₁".
- §3: "class-2 (Comparator-2) holonomy" → "holonomy in H₂ (class ≤ 2)"; "abelian and non-abelian experiments" → "H₁ and H₂"; "class-2 comparator" → "H₂ comparator".
- §4: retitled "for H₂"; marked as applied; added the class ≥ 2 sentence.
- §5: "Comparator k" → "the comparator H_k"; rung list now H₁/H₂/H₃, with H₃ stated as done.
- §6: table rebuilt with columns for hypothesis class, null rejected and what a positive result certifies; the "not applied retroactively" sentence replaced by a pointer here. Companion line uses new file names.

**h1-abelian-rung.md** (was discriminating-experiment.md)
- Title → "H₁ (abelian): the discriminating experiment"; one-line ladder placement added.
- Field trial tagged H₀; verdict tagged H₁ vs H₀; script/output paths → `h1_monodromy_experiment.*`.
- §4 → "The next rung, H₂", tagged as built in h2-nonabelian-rung.md; "can represent even in principle" → the ladder theorem's full-frame wording plus "certifies class ≥ 2, not class 2".

**h2-nonabelian-rung.md** (was nonabelian-rung.md)
- Title → "H₂ (non-abelian): the commutator-loop rung"; ladder placement line with the class ≥ 2 claim.
- "cannot produce/represent even in principle" (Purpose and Verdict) → the replacement text from ladder theorem §4 (full-frame, any dimension, projected readout open).
- "comparator family" → "H₁"; "H-vs-I matched null" → "H₁'s world-H vs world-I matched null".
- "What it does and does not claim" gains "certifies non-abelian (class ≥ 2), not class 2".
- §4 arc list: field trial → H₀, abelian rung → H₁, non-abelian rung → H₂.

**h3-nested-rung.md** (was depth3-rung.md)
- Title → "H₃ (nested ordering): the depth-3 rung"; subtitle null → "matched H₂ (class-2) null".
- Every "non-abelian rung/detector" → H₂; every "depth-3 rung/detector", "third rung" → H₃; table headers likewise.
- Script/output/companion paths updated.
- Incidental fix: two references to "Section 6" for the quantization proposition → "Section 3" (where it is).

**ladder_theorem.py**
- Docstring: "H1 abelian (class 1)", "H2 non-abelian (class 2)", "H3 (class 3) <- prediction" → class ≤ 1/2/3; added the class-vs-detector paragraph.
- Printed labels: "H1 abelian (class 1)" → "H1 witness: abelian (class 1)", same for H2/H3; name column widened 28 → 36.

**h2_nonabelian_experiment.py**
- Docstring: "Non-abelian rung" → "H2 (non-abelian, depth 2)" plus the class ≥ 2 claim; "Comparator family" → "Comparator = H1"; "H-vs-I matched null" → "H1 rung's world-H vs world-I"; full-frame/any-dimension clause added.
- First printed line: "non-abelian angles…" → "H2 (non-abelian) detector, angles…".

**h3_nested_experiment.py**
- Docstring: "Depth-3 rung (H3 / Comparator 3)…class-2 null" → "H3 (nested ordering, depth 3)…H2 (class <= 2) null" plus the class ≥ 3 claim; "as in the non-abelian rung" → "as in H2".
- Printed text and column headers: "d3 single/max/rss", "d3 plugin/student", "d3max", "R80 depth2/depth3", "d3 FAR/pow", "depth-3 rung" → H3 equivalents. Depth observables (d1, d2, d3a, d3b, d4) and function names (`depth2_loops`, `depth3_loops`) keep their names: they name a depth, not a rung.

**README.md**: script table and layout use the new names and H labels; added "Detector ladder (naming)" and "This folder" sections.

In all three scripts only string literals changed; the parsed code with strings blanked is identical to the originals.

## Left alone, on purpose

- AMT working draft H_0/H_1/H_k (homology of voids), the anthology's and monograph's H⁰/H¹ (twisted cohomology), Resilience Topology, curved A∞ report: different meaning or no ladder labels.
- Spec v2, anthology and monograph: none of them names the rungs. The monograph's "field trial" (Part V) is a section name and stays.
- field_trial.py and its output, metrics.py and the other scripts: no ladder labels.
- World labels H, I, S, Z (H₁) and NA, AB, Z (H₂) stay. World H is a data-generating world, not a ladder level; the H₁ and H₂ notes now say "world H" where the two could be confused.
- Witness and world classes ("D8 is class 2", "Heisenberg (class 2)") stay: those state a world's exact class, which is correct.

## Outputs

- h2_nonabelian_experiment.txt: identical to the original capture apart from line 1's label.
- ladder_theorem.txt: identical apart from the three witness labels, and the four machine-zero values in the dimension check (now 3.23e-16, 1.29e-15, 2.72e-15, 1.28e-14). The unmodified original script prints the same new values in this environment (numpy 2.5.3, OpenBLAS 0.3.34), so that is BLAS rounding, not the edit.
- h3_nested_experiment.txt: every number identical to the Nov 18 capture; only label text (13 lines) and the runtime line differ.

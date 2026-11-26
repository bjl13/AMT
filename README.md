# AMT

The definitive repository for **Avergent Manifold Topology (AMT)** and the
**waveform program** (Observer-Indexed Dual Hypergraphs with Incidence
Waveforms), its curved substrate, and the reproducible proofs behind it.

When two documents here disagree, the call was made for correctness and room to
grow, not for whichever version is newer, because the work is written
asynchronously. Every such call is listed in [`RECONCILIATION.md`](RECONCILIATION.md),
and the affected passages carry a short *Repo note* pointing there.

## Layout

```
README.md               this index
RECONCILIATION.md       what conflicted, which version won, and why
docs/
  amt/                  the substrate theory
  waveform/             the waveform formalism: spec, anthology, monograph
  background/           predecessor work AMT builds on
waveform-proofs/        runnable code, captured outputs, detector-ladder notes
```

New strands of the program get their own folder beside these: a new theory
part under `docs/amt/`, a new paper under `docs/<strand>/`, a new codebase as a
top-level folder like `waveform-proofs/`, with a line added to the index below.

## Index

### AMT (`docs/amt/`)

| file | what it is | status |
|---|---|---|
| [`amt-working-draft.md`](docs/amt/amt-working-draft.md) | Preamble, Part I (axioms A–E, persistent type-cast state, policy-mediated interpretation, helical substrate) and Appendix D (formalization attempt, divergence points D.1.α–D.3.γ, the avergent connection ∇^av) | working draft; Parts II–V not yet written; ∇^av open |
| [`curved-a-infinity-framework.md`](docs/amt/curved-a-infinity-framework.md) | Curved A∞-algebras as the composition algebra for AMT; helix forced as a mapping torus with infinite-order monodromy | research report; geometric realization theorem conjectural |

### Waveform formalism (`docs/waveform/`)

Read the monograph first. The spec stays normative for grammar, duality,
citations and serialization; the anthology is the paper that discharged the
spec's open items, carried into the monograph with new numbering.

| file | what it is | status |
|---|---|---|
| [`waveform-monograph.md`](docs/waveform/waveform-monograph.md) | Complete development: grammar, citation spine, curved instantiation complex, linear Triple, field trial, dual convention, namespace, full proof codebase inline | reference text |
| [`observer-indexed-hypergraph-spec-v2.md`](docs/waveform/observer-indexed-hypergraph-spec-v2.md) | Canonical Specification v2 | normative for §§1–3, 6; theorem status superseded by the monograph |
| [`curvature-anthology-v1.md`](docs/waveform/curvature-anthology-v1.md) | Discharge of the v2 open items | carried into the monograph |

### Proofs and the detector ladder (`waveform-proofs/`)

`make all` reruns every script and rewrites `outputs/`. See
[`waveform-proofs/README.md`](waveform-proofs/README.md) for the script table.

| note | rung | certifies |
|---|---|---|
| field trial (monograph Part V) | H₀, static | phenomenon detection only |
| [`h1-abelian-rung.md`](waveform-proofs/notes/h1-abelian-rung.md) | H₁, abelian | non-trivial holonomy |
| [`h2-nonabelian-rung.md`](waveform-proofs/notes/h2-nonabelian-rung.md), [`h2-tangent-backport.md`](waveform-proofs/notes/h2-tangent-backport.md) | H₂, non-abelian | class ≥ 2 |
| [`h3-nested-rung.md`](waveform-proofs/notes/h3-nested-rung.md), [`gap-rung.md`](waveform-proofs/notes/gap-rung.md) | H₃, nested ordering | class ≥ 3 |
| [`comparator-ladder-theorem.md`](waveform-proofs/notes/comparator-ladder-theorem.md) | the ladder is the lower central series | — |

### Background (`docs/background/`)

| file | what it is |
|---|---|
| [`resilience-topology.md`](docs/background/resilience-topology.md) ([PDF](docs/background/resilience-topology.pdf)) | Resilience Topology whitepaper: the predictive-resilience framework whose void and inverse-manifold ideas AMT reformulates |

## Naming

Two unrelated families of labels share the letter H:

- **H₀–H₃ (detector ladder).** H_k is the hypothesis that holonomy is nilpotent
  of class ≤ k, and the rung that rejects H_{k−1}. A positive H_k result
  certifies class ≥ k. Map from older names: `waveform-proofs/RENAMES.md`.
- **H_k, H⁰, H¹ (homology and cohomology).** The void homology in the AMT draft
  and the twisted cohomology in the anthology and monograph keep their
  standard meaning.

Rigor flags across the corpus: **[THM]** proven, **[NUM]** numerically
witnessed, **[TIR]/[TIR-c]** theorem-in-reach (spec v2 only), **[CIR]**
conjecture-in-reach, **[OPEN]** stated boundary.

## Open items

- ∇^av, the avergent connection (AMT D.4 / D.3.γ).
- Nonlinear Triple: monograph Conjecture B.1 (anthology Conjecture VI.1).
- Small-holonomy dichotomy proof; fitted class-2 null; projected-readout
  exclusion for H₂, H₃ and the gap rung; a real corpus for the ladder;
  whether AMT's transport (D.4) is unitary, which the gap rung assumes.
- Second field corpus (monograph Appendix B).
- Namespace: the w3id PR artifacts described in monograph VI.2 are not in this
  repository yet.

"""
Anthology Part III preamble + v2 section 5.1:
recompute the worked example from the source document, exhibit it as a
minimal falsifier witness, and run the synthetic pipeline demonstration.
"""
import numpy as np
from metrics import node_metrics, pairwise_cosines

XI = {'R1': np.array([1.0, 0.2, 0.1]),
      'R2': np.array([0.9, 0.1, 0.0]),
      'R3': np.array([-0.4, 0.0, 1.1])}
FRAMES = {'O_xy': [0, 1], 'O_xz': [0, 2]}


def worked_example():
    ambient = float(sum(np.dot(v, v) for v in XI.values()))
    print("=== WORKED EXAMPLE (source doc), recomputed ===")
    print(f"ambient energy E = sum ||Xi||^2 = {ambient:.6f}\n")
    for fname, idx in FRAMES.items():
        phis = np.array([XI[k][idx] for k in ['R1', 'R2', 'R3']])
        r = node_metrics(phis, ambient_energy=ambient)
        cos, ij = pairwise_cosines(phis)
        print(f"{fname}: Psi={phis.sum(axis=0)}")
        print(f"  gross={r['gross_mass']:.6f} net={r['net_resultant']:.6f} "
              f"coherence={r['coherence']:+.6f} tension={r['tension']:.6f} "
              f"D_O={r['D_O']:.6f}")
        print(f"  pairwise cosines {[(p, round(c,4)) for p, c in zip(ij, cos)]}")
    # monotonicity violation in O_xy
    ph = np.array([XI[k][[0, 1]] for k in ['R1', 'R2', 'R3']])
    n12 = np.linalg.norm(ph[0] + ph[1])
    n123 = np.linalg.norm(ph.sum(axis=0))
    print(f"\nMonotonicity: net{{R1,R2}}={n12:.6f} -> +R3 -> {n123:.6f} "
          f"(DECREASE: {n123 < n12}) => no additive model reproduces this")


def synthetic_ensemble(N=500, m=3, d=3, seed=0):
    rng = np.random.default_rng(seed)
    node_flip = tension_both = mono = 0
    pair_flip = pair_tot = 0
    for _ in range(N):
        payloads = rng.standard_normal((m, d))
        res, cosframes = {}, {}
        for fname, idx in FRAMES.items():
            sub = payloads[:, idx]
            res[fname] = node_metrics(sub)
            cosframes[fname], _ = pairwise_cosines(sub)
        a, b = res['O_xy'], res['O_xz']
        if a['coherence'] * b['coherence'] < 0:
            node_flip += 1
        if a['tension'] > 1e-12 and b['tension'] > 1e-12:
            tension_both += 1
        for ca, cb in zip(cosframes['O_xy'], cosframes['O_xz']):
            pair_tot += 1
            if ca * cb < 0:
                pair_flip += 1
        for fname, idx in FRAMES.items():
            sub = payloads[:, idx]
            if np.linalg.norm(sub.sum(axis=0)) < np.linalg.norm(sub[0] + sub[1]) - 1e-12:
                mono += 1
                break
    print(f"\n=== SYNTHETIC ENSEMBLE  N={N} m={m} d={d} seed={seed} ===")
    print(f"  node-coherence sign flips : {node_flip}/{N} = {node_flip/N:.1%}")
    print(f"  pairwise sign flips       : {pair_flip}/{pair_tot} = {pair_flip/pair_tot:.1%}")
    print(f"  tension>0 both frames     : {tension_both}/{N} = {tension_both/N:.1%}")
    print(f"  monotonicity violations   : {mono}/{N} = {mono/N:.1%}")


if __name__ == "__main__":
    worked_example()
    synthetic_ensemble()

"""
Anthology Part III + v2 section 5.3 GO/NO-GO benchmark on real data.
Corpus: sklearn digits (1797 real handwritten-digit vectors, d=64).
Nodes = 10 digit classes; incidence payload = one image vector.
Frames = two orthogonal PCA visible planes (PC1-2 vs PC3-4).
Discriminators: tension>0, pairwise coherence sign-flip rate,
monotonicity-violation rate, permutation z-scores. Additive null is
rejected if pairwise sign-flip rate or monotonicity-violation rate > 0.
"""
import numpy as np
from sklearn.datasets import load_digits
from metrics import node_metrics, pairwise_cosines

SEED = 42


def run():
    rng = np.random.default_rng(SEED)
    X, y = load_digits(return_X_y=True)
    Xc = X - X.mean(axis=0)
    _, S, Vt = np.linalg.svd(Xc, full_matrices=False)
    F1, F2 = Vt[[0, 1], :], Vt[[2, 3], :]
    evr = S ** 2 / (S ** 2).sum()
    print(f"Corpus: sklearn digits, n={X.shape[0]}, ambient d={X.shape[1]}, "
          f"10 node-classes")
    print(f"Frames: PC1-2 (var {evr[:2].sum():.3f}) vs PC3-4 "
          f"(var {evr[2:4].sum():.3f})\n")
    print(f"{'cls':>3s} {'m_v':>4s} {'tens1':>8s} {'coh1':>7s} {'tens2':>8s} "
          f"{'coh2':>7s} {'pflip%':>7s} {'mono%':>6s} {'D_O1':>6s} "
          f"{'z1':>6s} {'z2':>6s}")
    tension_both = node_flip = 0
    pflips, monos = [], []
    for c in range(10):
        P = Xc[y == c]
        Etot = float((P ** 2).sum())
        ph1, ph2 = P @ F1.T, P @ F2.T
        r1 = node_metrics(ph1, ambient_energy=Etot)
        r2 = node_metrics(ph2, ambient_energy=Etot)
        # pairwise sign flips on a shared sample of pairs
        cos1, idx = pairwise_cosines(ph1)
        if len(idx) > 4000:
            sel = rng.choice(len(idx), 4000, replace=False)
            idx = [idx[s] for s in sel]
            cos1 = np.array([ph1[i] @ ph1[j] /
                             (np.linalg.norm(ph1[i]) * np.linalg.norm(ph1[j]))
                             for i, j in idx])
        cos2 = np.array([ph2[i] @ ph2[j] /
                         (np.linalg.norm(ph2[i]) * np.linalg.norm(ph2[j]))
                         for i, j in idx])
        pflip = float((np.sign(cos1) != np.sign(cos2)).mean())
        # monotonicity: random orders, fraction of decreasing steps
        viol = tot = 0
        for _ in range(50):
            order = rng.permutation(len(ph1))
            run_v = np.zeros(2)
            prev = 0.0
            for i in order:
                run_v = run_v + ph1[i]
                cur = np.linalg.norm(run_v)
                if cur < prev - 1e-12:
                    viol += 1
                tot += 1
                prev = cur
        mono = viol / tot
        # permutation z: isotropic null with observed magnitudes
        def zscore(ph):
            mags = np.linalg.norm(ph, axis=1)
            nulls = []
            for _ in range(500):
                ang = rng.uniform(0, 2 * np.pi, len(mags))
                vecs = mags[:, None] * np.c_[np.cos(ang), np.sin(ang)]
                nulls.append(np.linalg.norm(vecs.sum(axis=0)))
            return (np.linalg.norm(ph.sum(axis=0)) - np.mean(nulls)) / np.std(nulls)
        z1, z2 = zscore(ph1), zscore(ph2)
        tension_both += (r1['tension'] > 1e-9 and r2['tension'] > 1e-9)
        node_flip += (r1['coherence'] * r2['coherence'] < 0)
        pflips.append(pflip)
        monos.append(mono)
        print(f"{c:3d} {r1['incidence_count']:4d} {r1['tension']:8.1f} "
              f"{r1['coherence']:+7.3f} {r2['tension']:8.1f} {r2['coherence']:+7.3f} "
              f"{pflip*100:6.1f} {mono*100:5.1f} {r1['D_O']:6.3f} "
              f"{z1:+6.1f} {z2:+6.1f}")
    print(f"\nAGGREGATE: tension>0 both frames {tension_both}/10 | "
          f"node-coherence flips {node_flip}/10 | "
          f"mean pairwise-flip {np.mean(pflips)*100:.1f}% | "
          f"mean mono-viol {np.mean(monos)*100:.1f}%")
    verdict = "GO" if (np.mean(pflips) > 0 and np.mean(monos) > 0
                       and tension_both == 10) else "NO-GO"
    print(f"VERDICT: {verdict} — additive null "
          f"{'rejected' if verdict=='GO' else 'not rejected'}")


if __name__ == "__main__":
    run()

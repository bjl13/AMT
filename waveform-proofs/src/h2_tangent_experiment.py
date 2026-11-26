"""
H2 (non-abelian, class >= 2) with the tangent-component noise estimate and the studentized
bootstrap-t null, run on injected holonomies AND end-to-end through Kato transport.

Why. The H3 rung (h3-nested-rung.md, section 2.6) found that under end-to-end Kato transport the
path jitter moves each holonomy ALONG the group: its spread is almost all anti-Hermitian (tangent),
while readout noise is isotropic. H2's noise estimate pools all 2n^2 real components of the shot
deviations, so it underestimates the spread in exactly the n^2 tangent directions that the
Procrustes estimate keeps, and the false-alarm rate creeps up. The fix estimated sigma from the
tangent (anti-Hermitian) part of W_hat^dagger (Y - mean Y). This script back-ports that fix to H2.

Detector (unchanged observable). Transport the input frame X = I around the commutator loop
[a,b] = a b a^-1 b^-1, R noisy shots Y, W_hat = Procrustes(mean Y), delta = ||W_hat - I||_F.
Null: Hol_C = I (every abelian pair, any dimension, full-frame readout; Ladder Theorem 1).
A positive result certifies non-abelian holonomy (class >= 2), a lower bound.

Three calibrations, applied to the SAME data in every cell (paired comparison):
  plugin/all   -- original H2: plug-in sigma from all 2n^2 components, null simulated at it
  student/all  -- bootstrap-t (H3 section 1), sigma from all components
  student/tan  -- bootstrap-t, sigma from the n^2 tangent components   <- the back-port

Tracks.
  1  injected holonomies, isotropic complex readout noise (H2's own setting), sigma = 0.3
  2  end-to-end: discrete Kato transport of a 2-frame along closed horizontal loops in Gr(2,4)
     (the H3 construction), commutator word traversed as one concatenated loop, per-step path
     jitter sigma_path in {0.01, 0.02, 0.03}, readout sigma 0.1.

numpy only, seeded. Run time ~10 min on 4 cores.
"""
import numpy as np
import time

ALPHA = 0.05
M_NULL = 400
SIGMA = 0.3
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
T0 = time.time()
CALIBS = ['plugin/all', 'student/all', 'student/tan']


def su2(axis, angle):
    n = np.asarray(axis, float); n = n / np.linalg.norm(n)
    G = n[0] * SX + n[1] * SY + n[2] * SZ
    return np.cos(angle / 2) * I2 - 1j * np.sin(angle / 2) * G


def mirror(theta):
    c, s = np.cos(2 * theta), np.sin(2 * theta)
    return np.array([[c, s], [s, -c]], dtype=complex)


def gc(X, Y):
    return X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y)


def dev(M):
    n = M.shape[-1]
    return np.linalg.norm(M - np.eye(n), axis=(-2, -1))


def procrustes(M):
    U, _, Vh = np.linalg.svd(M)
    return U @ Vh


def dag(M):
    return np.conj(np.swapaxes(M, -1, -2))


WORLDS = {
    'Z':     (I2.copy(), I2.copy()),                                  # abelian (trivial)
    'AB':    (su2([1, 0, 0], np.pi / 2), su2([1, 0, 0], np.pi / 2)),  # abelian, spectra matched to NA
    'NA':    (su2([1, 0, 0], np.pi / 2), su2([0, 1, 0], np.pi / 2)),  # H2's non-abelian world
    'D8':    (mirror(0.0), mirror(np.pi / 4)),                        # class 2, [A,B] = -I
    'NN0.5': (su2([1, 0, 0], 0.5), su2([0, 1, 0], 0.5)),              # small holonomy
    'NN0.3': (su2([1, 0, 0], 0.3), su2([0, 1, 0], 0.3)),
}
ABELIAN = {'Z', 'AB'}


# ---------------------------------------------------------------- the three calibrations
def null_devs(scale, d, M, rng):
    """delta of the Procrustes estimate of an identity loop; scale = per-real-component sd (n,)."""
    n = scale.shape[0]
    E = (rng.standard_normal((n, M, d, d)) + 1j * rng.standard_normal((n, M, d, d))) * scale[:, None, None, None]
    return dev(procrustes(np.eye(d) + E))


def decide(delta, s2, df, R, calib, rng, d=2, M=M_NULL):
    """delta (n,), s2 (n,) per-component shot variance estimate with df degrees of freedom.
    Returns reject (n,)."""
    se = np.sqrt(s2 / R)
    Dn = null_devs(se, d, M, rng)
    if calib == 'plugin/all' or R == 1:
        p = (1 + (Dn >= delta[:, None]).sum(1)) / (1 + M)
    else:
        se_star = se[:, None] * np.sqrt(rng.chisquare(df, (len(se), M)) / df)
        p = (1 + (Dn / se_star >= (delta / se)[:, None]).sum(1)) / (1 + M)
    return p < ALPHA


def shot_variances(Y, m, Wh):
    """From R shots Y (n,R,d,d), their mean m and W_hat: per-component variance estimates
    (all components, tangent components) and their degrees of freedom."""
    n, R, d, _ = Y.shape
    dY = Y - m[:, None]
    s2_all = 0.5 * (np.abs(dY) ** 2).sum((1, 2, 3)) / (d * d * (R - 1))      # 2 d^2 (R-1) dof, /2 per comp
    Tm = dag(Wh)[:, None] @ dY
    Ah = 0.5 * (Tm - dag(Tm))
    s2_tan = (np.abs(Ah) ** 2).sum((1, 2, 3)) / (d * d * (R - 1))            # d^2 (R-1) dof
    return s2_all, 2 * d * d * (R - 1), s2_tan, d * d * (R - 1)


def all_calibs(Y, rng):
    """Apply the three calibrations to the same shots. Y (n,R,d,d). Returns dict calib->reject."""
    n, R, d, _ = Y.shape
    m = Y.mean(1)
    Wh = procrustes(m)
    delta = dev(Wh)
    s2a, dfa, s2t, dft = shot_variances(Y, m, Wh)
    return {'plugin/all': decide(delta, s2a, dfa, R, 'plugin/all', rng, d),
            'student/all': decide(delta, s2a, dfa, R, 'student/all', rng, d),
            'student/tan': decide(delta, s2t, dft, R, 'student/tan', rng, d)}, delta


def injected_shots(W, sigma, R, n, rng):
    E = (rng.standard_normal((n, R, 2, 2)) + 1j * rng.standard_normal((n, R, 2, 2))) * sigma / np.sqrt(2)
    return W + E


def hr(title):
    print("\n" + title)
    print("-" * len(title))


# ================================================================ 0. estimator sanity
hr("0. ESTIMATOR SANITY (isotropic readout noise, sigma = 0.3, per-component variance 0.045)")
rng = np.random.default_rng(1)
for R in [2, 5, 20]:
    Y = injected_shots(WORLDS['NA'][0], SIGMA, R, 20000, rng)
    m = Y.mean(1); Wh = procrustes(m)
    s2a, dfa, s2t, dft = shot_variances(Y, m, Wh)
    print(f"R={R:3d}: mean s2_all = {s2a.mean():.4f} (dof {dfa:3d}), mean s2_tan = {s2t.mean():.4f} "
          f"(dof {dft:3d}), var ratio s2_tan/s2_all = {s2t.var()/s2a.var():.2f} (theory 2.00)")
print("Both are unbiased for isotropic noise; the tangent estimate has half the degrees of freedom.")

# ================================================================ 1. injected track
hr(f"1. INJECTED HOLONOMIES, isotropic readout (sigma={SIGMA}, 4000 trials, binomial SE ~0.0035)")
print("False alarms on the abelian nulls Z and AB (AB = spectra matched to NA); power on NA, NN.")
hdr = " | ".join(f"{c:>11s}" for c in CALIBS)
print(f"{'R':>4s} {'world':>6s} | {hdr}")
for R in [2, 3, 5, 10, 20, 50]:
    for iw, w in enumerate(['Z', 'AB', 'NA', 'NN0.5']):
        A, B = WORLDS[w]
        rng = np.random.default_rng(1000 + 10 * R + iw)
        n = 4000 if w in ABELIAN else 1000
        rej, _ = all_calibs(injected_shots(gc(A, B), SIGMA, R, n, rng), rng)
        print(f"{R:4d} {w:>6s} | " + " | ".join(f"{rej[c].mean():11.3f}" for c in CALIBS))

print("\nPower cost of the tangent estimate (half the dof) at small holonomy, NN(eps):")
print(f"{'eps':>5s} {'R':>6s} | " + " | ".join(f"{c:>11s}" for c in CALIBS))
for ie, (e, Rs) in enumerate([(0.5, [5, 10, 20]), (0.3, [50, 100, 200]), (0.2, [300, 700, 1500])]):
    A, B = su2([1, 0, 0], e), su2([0, 1, 0], e)
    for R in Rs:
        rng = np.random.default_rng(5000 + 100 * ie + R)
        # sufficient statistics would be faster, but shots keep the three calibrations paired
        nrep = 1000 if R <= 300 else 400
        rej, _ = all_calibs(injected_shots(gc(A, B), SIGMA, R, nrep, rng), rng)
        print(f"{e:5.2f} {R:6d} | " + " | ".join(f"{rej[c].mean():11.3f}" for c in CALIBS))

# ================================================================ 2. end-to-end Kato transport
hr("2. END-TO-END: Kato transport in Gr(2,4), commutator word read as one concatenated loop")
NSTEP = 12
V0 = np.vstack([np.eye(2), np.zeros((2, 2))]).astype(complex)


def loop_path(U):
    """frames along a closed horizontal loop S -> S_perp -> S with holonomy U (2x2 unitary)."""
    t = np.linspace(0, np.pi / 2, NSTEP + 1)
    seg1 = [np.vstack([np.cos(x) * I2, np.sin(x) * I2]) for x in t]
    seg2 = [np.vstack([np.sin(x) * U, np.cos(x) * I2]) for x in t[1:]]
    return seg1 + seg2


def word_path(letters, gens):
    pts = None
    for g, s in reversed(letters):
        p = loop_path(gens[g])
        if s < 0:
            p = p[::-1]
        pts = p if pts is None else pts + p[1:]
    return pts


def inv_word(wd):
    return [(g, -s) for g, s in reversed(wd)]


WA, WB = [('a', 1)], [('b', 1)]
WC = WA + WB + inv_word(WA) + inv_word(WB)


def polar(M):
    U, _, Vh = np.linalg.svd(M, full_matrices=False)
    return U @ Vh


def transport(pts, nb, sig_path, rng):
    """discrete Kato transport of V0 along pts for nb traversals, per-step jitter of the interior
    subspaces; returns holonomy samples (nb,2,2)."""
    V = np.broadcast_to(V0, (nb, 4, 2)).copy()
    for j in range(1, len(pts)):
        W = pts[j]
        if sig_path > 0 and np.abs(W[2:]).max() > 1e-12:
            G = (rng.standard_normal((nb, 4, 2)) + 1j * rng.standard_normal((nb, 4, 2))) * sig_path / np.sqrt(2)
            W = polar(W + G)
        else:
            W = np.broadcast_to(W, (nb, 4, 2))
        V = W @ polar(dag(W) @ V)
    return V[:, :2, :]


rng = np.random.default_rng(70000)
print("noiseless transport vs algebraic commutator holonomy (max abs entry error):")
for w in ['AB', 'NA', 'D8', 'NN0.5']:
    A, B = WORLDS[w]
    H = transport(word_path(WC, dict(a=A, b=B)), 1, 0.0, rng)[0]
    print(f"  {w:>6s}: {np.abs(H - gc(A, B)).max():.1e}   (path length {len(word_path(WC, dict(a=A, b=B)))} steps)")

SRD = 0.1
print(f"\nreadout sigma = {SRD} (per-component variance {SRD**2/2:.4f}). Jitter-only spread of the commutator")
print("loop holonomy on AB (abelian null), and its Hermitian / anti-Hermitian split:")
for sp in [0.01, 0.02, 0.03]:
    A, B = WORLDS['AB']
    H = transport(word_path(WC, dict(a=A, b=B)), 4000, sp, rng)
    X = H - I2
    herm = np.linalg.norm(0.5 * (X + dag(X))); anti = np.linalg.norm(0.5 * (X - dag(X)))
    tan_var = (np.abs(0.5 * (X - dag(X))) ** 2).sum((1, 2)).mean() / 4
    print(f"  sigma_path={sp:.2f}: rms ||Hol - I|| = {np.sqrt((dev(H)**2).mean()):.3f}, "
          f"Herm/anti-Herm = {herm/anti:.3f}, jitter tangent var/comp = {tan_var:.2e} "
          f"= {tan_var/(SRD**2/2):.2f} x readout")


def e2e_shots(w, R, n, sp, rng):
    A, B = WORLDS[w]
    H = transport(word_path(WC, dict(a=A, b=B)), n * R, sp, rng).reshape(n, R, 2, 2)
    return H + (rng.standard_normal(H.shape) + 1j * rng.standard_normal(H.shape)) * SRD / np.sqrt(2)


print(f"\nFalse alarms (Z, AB) and power (NA, D8, NN0.3), same shots under all three calibrations.")
print("n = 2000 trials for Z, AB (SE ~0.005); 500 for the rest.")
print(f"{'s_path':>6s} {'R':>4s} {'world':>6s} | " + " | ".join(f"{c:>11s}" for c in CALIBS))
for ip, sp in enumerate([0.01, 0.02, 0.03]):
    for R in [2, 5, 20, 100]:
        for iw, w in enumerate(['Z', 'AB', 'NA', 'D8', 'NN0.3']):
            n = 2000 if w in ABELIAN else 500
            if R == 100:
                n = n // 2
            rng = np.random.default_rng(80000 + 1000 * ip + 10 * R + iw)
            rej, _ = all_calibs(e2e_shots(w, R, n, sp, rng), rng)
            print(f"{sp:6.2f} {R:4d} {w:>6s} | " + " | ".join(f"{rej[c].mean():11.3f}" for c in CALIBS))
    print()

print(f"runtime {time.time()-T0:.0f}s")

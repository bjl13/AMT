"""
The gap rung: certify class >= 3 (not nilpotent of class <= 2) from depth-2 data, for unitary
holonomy in a fiber of known dimension n, using the U(n) spectral gap of class-2 commutators.

Theorem (gap-rung.md, Prop. 1, extending h3-nested-rung.md section 3). If A, B in U(n) generate a
nilpotent group of class <= 2, then C = [A,B] is unitarily conjugate to
    I_{n0}  (+)  c_1 I_{m_1} (+) ... (+) c_r I_{m_r},     c_j a PRIMITIVE m_j-th root of unity,
with m_j >= 2 and n0 + sum m_j = n (r = 0 iff abelian). Hence ||C - I||_F is either 0 or
>= g(n) = min_{2<=m<=n} 2 sqrt(m) sin(pi/m), and g(n) is attained (clock-shift pair (+) I).

Test (intersection-union). The null "class <= 2" is the union of
    H0b: C = I (abelian)       and      H0a: C has one of the finitely many class-2 spectra above.
  p_b : H2's commutator-loop detector against C = I (studentized bootstrap-t, tangent sigma_hat).
  p_a : max over class-2 spectra S of a LOWER-tail bootstrap-t p-value: is d_hat = ||W_hat - I||
        significantly below d(S)?  The pivot is (d_hat - d(S)) / se_hat^k with k the delta-method
        order of d_hat - d(S): k = 1 in general, k = 2 when every eigenvalue of S is +-1 (e.g. D8,
        C = -I, where the linear term vanishes and noise only pulls d_hat down at O(se^2)).  The null law of d_hat depends only on the spectrum of C
        (isotropic circular noise, Procrustes is unitarily equivariant), so each S is simulated
        exactly at the estimated noise scale. Spectra with d(S) > g(n) + WIN are dropped (their
        lower quantiles sit far above; the binding spectrum is printed).
  Reject "class <= 2" (certify class >= 3) iff p_a < alpha AND p_b < alpha. By the
  intersection-union principle the size is <= alpha over the whole null, with no multiplicity
  correction, because every class <= 2 world lies in H0a or H0b.

numpy only, seeded. Run time ~15 min on 4 cores.
"""
import numpy as np
from math import gcd
import time

ALPHA = 0.05
M_NULL = 400
SIGMA = 0.3
WIN = 0.6
T0 = time.time()
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


# ---------------------------------------------------------------- algebra
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


def dag(M):
    return np.conj(np.swapaxes(M, -1, -2))


def procrustes(M):
    U, _, Vh = np.linalg.svd(M)
    return U @ Vh


def bdiag(*Ms):
    n = sum(M.shape[0] for M in Ms)
    out = np.zeros((n, n), dtype=complex); i = 0
    for M in Ms:
        k = M.shape[0]; out[i:i + k, i:i + k] = M; i += k
    return out


def haar(n, rng):
    Z = (rng.standard_normal((n, n)) + 1j * rng.standard_normal((n, n))) / np.sqrt(2)
    Q, R = np.linalg.qr(Z)
    return Q * (np.diag(R) / np.abs(np.diag(R)))


def clock_shift(m):
    """Weyl pair in U(m): [X, Z] = scalar primitive m-th root of unity. Class 2."""
    X = np.roll(np.eye(m), 1, axis=0).astype(complex)
    Z = np.diag(np.exp(2j * np.pi * np.arange(m) / m))
    return X, Z


def g_of(n):
    return min(2 * np.sqrt(m) * np.sin(np.pi / m) for m in range(2, n + 1))


def class2_spectra(n):
    """All class-2 commutator spectra in U(n) up to conjugation and complex conjugation:
    list of (d, eigenvalues (n,), label), sorted by d."""
    B = [(m, k) for m in range(2, n + 1) for k in range(1, m) if gcd(k, m) == 1]
    keys = set()

    def rec(start, rem, cur):
        if cur:
            key = tuple(sorted(cur)); conj = tuple(sorted((m, m - k) for m, k in cur))
            keys.add(min(key, conj))
        for i in range(start, len(B)):
            if B[i][0] <= rem:
                rec(i, rem - B[i][0], cur + [B[i]])
    rec(0, n, [])
    out = []
    for key in keys:
        ev = []
        for m, k in key:
            ev += [np.exp(2j * np.pi * k / m)] * m
        ev += [1.0] * (n - len(ev))
        ev = np.array(ev, dtype=complex)
        lab = "+".join(f"{m}:e^(2pi i {k}/{m})" for m, k in key) + (f"+I{n-sum(m for m,_ in key)}" if n > sum(m for m, _ in key) else "")
        out.append((float(np.linalg.norm(ev - 1)), ev, lab))
    return sorted(out, key=lambda t: t[0])


# ---------------------------------------------------------------- readout and the two tests
def suff_stats(W, sigma, R, n, rng):
    """Shot mean and tangent-component variance estimate of R isotropic complex Gaussian shots
    (exact laws; tangent sigma_hat has d^2 (R-1) dof)."""
    d = W.shape[-1]
    m = W + (rng.standard_normal((n, d, d)) + 1j * rng.standard_normal((n, d, d))) * sigma / np.sqrt(2 * R)
    v = sigma ** 2 / 2
    if R > 1:
        df = d * d * (R - 1)
        s2 = v * rng.chisquare(df, n) / df
    else:
        df, s2 = 0, np.full(n, v)
    return m, s2, df


def shot_stats(Y):
    """Same from explicit shots Y (n,R,d,d): mean, tangent variance, dof."""
    n, R, d, _ = Y.shape
    m = Y.mean(1); Wh = procrustes(m)
    Tm = dag(Wh)[:, None] @ (Y - m[:, None])
    Ah = 0.5 * (Tm - dag(Tm))
    return m, (np.abs(Ah) ** 2).sum((1, 2, 3)) / (d * d * (R - 1)), d * d * (R - 1)


def sim_dev(W, se, M, rng, chunk=200):
    """d_hat draws for a loop of holonomy W at per-component noise sd se (n,): (n, M)."""
    d = W.shape[-1]; out = np.empty((len(se), M))
    for i in range(0, len(se), chunk):
        s = se[i:i + chunk]
        E = (rng.standard_normal((len(s), M, d, d)) + 1j * rng.standard_normal((len(s), M, d, d))) * s[:, None, None, None]
        out[i:i + chunk] = dev(procrustes(W + E))
    return out


def pvals(m, s2, df, R, n_null, rng, M=M_NULL, need_a=None):
    """p_b (upper tail vs identity) and p_a (max over class-2 spectra, lower tail).
    n_null: dimension whose class-2 spectra form H0a (normally the readout dimension)."""
    d = m.shape[-1]
    Wh = procrustes(m); dh = dev(Wh); se = np.sqrt(s2 / R); n = len(dh)
    stud = df > 0
    ses = se[:, None] * np.sqrt(rng.chisquare(df, (n, M)) / df) if stud else se[:, None]
    Dn = sim_dev(np.eye(d, dtype=complex), se, M, rng)
    pb = (1 + ((Dn / ses) >= (dh / se)[:, None]).sum(1)) / (1 + M) if stud else (1 + (Dn >= dh[:, None]).sum(1)) / (1 + M)
    pa = np.ones(n); bind = np.full(n, -1)
    specs = [s for s in class2_spectra(n_null) if s[0] <= g_of(n_null) + WIN]
    act = (pb < ALPHA) if need_a is None else need_a
    act = act & (dh < g_of(n_null) + WIN)
    idx = np.where(act)[0]
    if len(idx):
        best = np.zeros(len(idx))
        for js, (dS, ev, _) in enumerate(specs):
            evd = np.concatenate([ev, np.ones(d - len(ev))]) if d > len(ev) else ev
            if len(evd) != d:
                raise ValueError("readout dimension smaller than null dimension")
            Dn = sim_dev(np.diag(evd), se[idx], M, rng)
            if stud:
                # delta-method order of d_hat - d(S): first order unless every eigenvalue is +-1
                # (then the linear term Re tr(W^dag X) vanishes and d_hat - d(S) = O(se^2)).
                k = 1 if np.sum(np.sin(np.angle(evd)) ** 2) > 1e-9 else 2
                p = (1 + (((Dn - dS) / ses[idx] ** k) <= ((dh[idx] - dS) / se[idx] ** k)[:, None]).sum(1)) / (1 + M)
            else:
                p = (1 + (Dn <= dh[idx][:, None]).sum(1)) / (1 + M)
            upd = p > best
            bind[idx[upd]] = js; best = np.maximum(best, p)
        pa[idx] = best
    return pa, pb, dh, bind


def gap_rates(W, R, n, seed, n_null=None, sigma=SIGMA, M=M_NULL):
    rng = np.random.default_rng(seed)
    m, s2, df = suff_stats(W, sigma, R, n, rng)
    pa, pb, dh, bind = pvals(m, s2, df, R, n_null or W.shape[-1], rng, M=M, need_a=np.ones(n, bool))
    return dict(gap=((pa < ALPHA) & (pb < ALPHA)).mean(), a=(pa < ALPHA).mean(), b=(pb < ALPHA).mean(),
                med=np.median(dh), bind=np.bincount(bind[bind >= 0]) if (bind >= 0).any() else [])


def hr(title):
    print("\n" + title)
    print("-" * len(title))


# ================================================================ 0. the theorem, checked
hr("0. CLASS-2 COMMUTATOR SPECTRA IN U(n) AND THE GAP g(n)")
print("Prop. 1: a class-2 commutator is I (+) sum_j c_j I_{m_j}, c_j a primitive m_j-th root of 1.")
print(f"{'n':>3s} {'#spectra':>8s} {'g(n)':>7s}  spectra with d <= g(n) + {WIN} (block m:root, d)")
for n in range(2, 9):
    sp = class2_spectra(n)
    near = "; ".join(f"{lab} {dS:.3f}" for dS, _, lab in sp if dS <= g_of(n) + WIN)
    print(f"{n:3d} {len(sp):8d} {g_of(n):7.3f}  {near}")
print("\nTightness and the block-dimension claim, on explicit class-2 pairs (random basis):")
rng = np.random.default_rng(2)
for name, (A, B) in [('D8', (mirror(0), mirror(np.pi / 4))),
                     ('CS3', clock_shift(3)), ('CS4', clock_shift(4)), ('CS5', clock_shift(5)),
                     ('CS8', clock_shift(8)), ('CS2+CS3', (bdiag(*[clock_shift(2)[0], clock_shift(3)[0]]),
                                                         bdiag(*[clock_shift(2)[1], clock_shift(3)[1]])))]:
    Q = haar(A.shape[0], rng); A, B = Q @ A @ dag(Q), Q @ B @ dag(Q)
    C = gc(A, B)
    central = max(np.abs(gc(C, A) - np.eye(len(A))).max(), np.abs(gc(C, B) - np.eye(len(A))).max())
    ev = np.sort(np.round(np.angle(np.linalg.eigvals(C)) / (2 * np.pi), 4))
    print(f"  {name:>8s} n={A.shape[0]}: ||[A,B]-I|| = {dev(C):.4f}, g(n) = {g_of(A.shape[0]):.4f}, "
          f"class-2 residual {central:.1e}, eig angles/2pi {ev}")
print("The CS_m pair attains 2 sqrt(m) sin(pi/m), so g(n) is the exact infimum over class-2 pairs.")

# ================================================================ worlds
QR = np.random.default_rng(3)


def conj_rand(A, B, rng=QR):
    Q = haar(A.shape[0], rng); return Q @ A @ dag(Q), Q @ B @ dag(Q)


def dih(dtarget):
    """two mirrors whose commutator is a rotation with ||[A,B]-I|| = dtarget (< 2 sqrt 2)."""
    th = 0.5 * np.arcsin(dtarget / (2 * np.sqrt(2)))
    return mirror(0.0), mirror(th)


_wza = procrustes(np.array([[0.1433, -0.9897], [0.9897, 0.1433]], dtype=complex))
_wzb = procrustes(np.array([[0.1433, -0.9897j], [-0.9897j, 0.1433]], dtype=complex))
X4, Z4 = clock_shift(4); X5, Z5 = clock_shift(5); X8, Z8 = clock_shift(8)
NULL_WORLDS = {   # name: (A, B, class)
    'Z':        (I2, I2, 'abelian'),
    'AB':       (su2([1, 0, 0], np.pi / 2), su2([1, 0, 0], np.pi / 2), 'abelian'),
    'D8':       (mirror(0), mirror(np.pi / 4), '2, on g(2)'),
    'D8+I2':    conj_rand(bdiag(mirror(0), I2), bdiag(mirror(np.pi / 4), I2)) + ('2, on g(4)',),
    'CS4':      conj_rand(X4, Z4) + ('2, on g(4)',),
    'CS5':      conj_rand(X5, Z5) + ('2, on g(5)',),
    'CS8':      conj_rand(X8, Z8) + ('2, on g(8)',),
}

# ================================================================ 1. calibration
hr(f"1. CALIBRATION ON CLASS <= 2 WORLDS (injected, sigma={SIGMA}, alpha={ALPHA})")
print("gap = certify class >= 3 (p_a < a and p_b < a): must be <= alpha on every row.")
print("p_a-only and p_b-only shown to see which half of the intersection-union test carries it.")
print(f"{'world':>7s} {'class':>11s} {'n':>2s} {'||C-I||':>8s} {'R':>4s} {'trials':>6s} | {'gap':>6s} "
      f"{'p_a<a':>6s} {'p_b<a':>6s} | {'med d_hat':>9s}")
for iw, (name, (A, B, cl)) in enumerate(NULL_WORLDS.items()):
    C = gc(A, B); n = C.shape[0]
    for R in [1, 2, 5, 20, 100]:
        tr = 4000 if n <= 2 else (2000 if n <= 5 else 1000)
        r = gap_rates(C, R, tr, 1000 + 100 * iw + R)
        print(f"{name:>7s} {cl:>11s} {n:2d} {dev(C):8.3f} {R:4d} {tr:6d} | {r['gap']:6.3f} {r['a']:6.3f} "
              f"{r['b']:6.3f} | {r['med']:9.3f}  binding spectrum counts {list(r['bind'])}")
print("binding spectrum counts: how often each class-2 spectrum (in section-0 order, d <= g+WIN) gave the max p_a")
print("(binomial SE: 0.0035 at 4000 trials, 0.005 at 2000, 0.007 at 1000)")
print("On D8 (C = -I, the farthest point of U(2) from I) noise can only pull d_hat DOWN, so a naive")
print("'d_hat < g' rule would false-alarm; the exact-spectrum null absorbs that bias.")
d8 = gc(*NULL_WORLDS['D8'][:2])
rng = np.random.default_rng(9)
for R in [1, 5, 20]:
    m, s2, df = suff_stats(d8, SIGMA, R, 20000, rng)
    dh = dev(procrustes(m))
    print(f"  D8 R={R:3d}: P(d_hat < g(2)) = {(dh < 2*np.sqrt(2) - 1e-12).mean():.3f}, mean shortfall "
          f"g - d_hat = {(2*np.sqrt(2)-dh).mean():.2e}")

# ================================================================ 2. power near the gap
hr("2. POWER NEAR THE GAP (U(2), class >= 3 worlds with ||C-I|| just below g(2) = 2.828)")
NEAR = [('Dih2.80', dih(2.80)), ('WZ', (_wza, _wzb)), ('Dih2.75', dih(2.75)), ('Dih2.70', dih(2.70)),
        ('Dih2.60', dih(2.60)), ('Dgen', (mirror(0), mirror(0.5))), ('Dih2.40', dih(2.40)),
        ('D16', (mirror(0), mirror(np.pi / 8))), ('Q16', (su2([0, 0, 1], np.pi / 2), su2([1, 0, 0], np.pi)))]
Rs = [1, 2, 5, 10, 20, 50, 100, 300]
print(f"{'world':>8s} {'||C-I||':>8s} {'margin':>7s} | " + " ".join(f"R={R:<4d}" for R in Rs))
for iw, (name, (A, B)) in enumerate(NEAR):
    C = gc(A, B)
    row = [gap_rates(C, R, 1000, 2000 + 100 * iw + R)['gap'] for R in Rs]
    print(f"{name:>8s} {dev(C):8.3f} {2*np.sqrt(2)-dev(C):7.3f} | " + " ".join(f"{x:6.2f}" for x in row))
print("H2 (p_b alone) fires at 1.00 on every row for R >= 1; the gap rung's cost near g is the p_a half.")


def r80(fn, seed, n=400, target=0.8, grid=None):
    grid = grid if grid is not None else np.unique(np.round(np.logspace(0, 12, 61)).astype(np.int64))
    prev = None
    for i, R in enumerate(grid):
        pw = fn(int(R), n, seed + i)
        if pw >= target:
            if prev is None:
                return float(R)
            R0, p0 = prev
            f = (target - p0) / max(pw - p0, 1e-9)
            return float(np.exp(np.log(R0) + f * (np.log(R) - np.log(R0))))
        prev = (R, pw)
    return np.inf


print("\nR80 vs margin (gap-rung power 0.8):")
print(f"{'world':>8s} {'margin':>7s} {'R80':>8s} {'R80*margin^2':>12s}")
for iw, (name, (A, B)) in enumerate(NEAR[:7]):
    C = gc(A, B); mg = 2 * np.sqrt(2) - dev(C)
    R8 = r80(lambda R, n, s: gap_rates(C, R, n, s)['gap'], 3000 + 100 * iw)
    print(f"{name:>8s} {mg:7.3f} {R8:8.3g} {R8*mg**2:12.3f}")

# ================================================================ 3. small holonomy: vs H2 and H3
hr("3. SMALL HOLONOMY NN(eps) = R(x,eps), R(y,eps): R80 of gap rung vs H2 and H3 (sigma=0.3)")


def h3_rate(eps, R, n, seed):
    """H3 direct nested-loop rung, rss of both brackets, studentized pooled bootstrap-t (h3 code)."""
    rng = np.random.default_rng(seed)
    A, B = su2([1, 0, 0], eps), su2([0, 1, 0], eps); C = gc(A, B)
    loops = [gc(C, A), gc(C, B)]
    ms, s2s = [], []
    for W in loops:
        m = W + (rng.standard_normal((n, 2, 2)) + 1j * rng.standard_normal((n, 2, 2))) * SIGMA / np.sqrt(2 * R)
        df = 8 * (R - 1)
        s2 = SIGMA ** 2 / 2 * rng.chisquare(df, n) / df if R > 1 else np.full(n, SIGMA ** 2 / 2)
        ms.append(m); s2s.append(s2)
    T = np.sqrt(sum(dev(procrustes(m)) ** 2 for m in ms))
    se = np.sqrt(np.mean(s2s, 0) / R)
    Tn = np.sqrt(sum(sim_dev(I2, se, M_NULL, rng) ** 2 for _ in loops))
    if R > 1:
        dfp = 16 * (R - 1)
        ses = se[:, None] * np.sqrt(rng.chisquare(dfp, (n, M_NULL)) / dfp)
        p = (1 + (Tn / ses >= (T / se)[:, None]).sum(1)) / (1 + M_NULL)
    else:
        p = (1 + (Tn >= T[:, None]).sum(1)) / (1 + M_NULL)
    return (p < ALPHA).mean()


print(f"{'eps':>5s} {'||C-I||':>9s} | {'R80 H2':>9s} {'R80 gap':>9s} {'R80 H3':>9s} | {'H3/gap':>7s} | "
      f"{'R80gap*d2^2':>11s} | {'FAR gap on D8 at R80gap':>23s}")
rows = []
for ie, e in enumerate([1.0, 0.5, 0.3, 0.2, 0.1, 0.05]):
    C = gc(su2([1, 0, 0], e), su2([0, 1, 0], e)); d2 = dev(C)
    R2 = r80(lambda R, n, s: gap_rates(C, R, n, s)['b'], 4000 + 100 * ie)
    Rg = r80(lambda R, n, s: gap_rates(C, R, n, s)['gap'], 5000 + 100 * ie)
    R3 = r80(lambda R, n, s: h3_rate(e, R, n, s), 6000 + 100 * ie) if e >= 0.1 else np.inf
    far = gap_rates(d8, max(int(round(Rg)), 1), 2000, 7000 + ie)['gap']
    rows.append((e, R2, Rg, R3))
    print(f"{e:5.2f} {d2:9.3e} | {R2:9.3g} {Rg:9.3g} {R3:9.3g} | {R3/Rg:7.3g} | {Rg*d2**2:11.3f} | {far:23.3f}")
le = np.log([r[0] for r in rows[3:]])
print(f"log-log slope of R80 (eps <= 0.2): H2 {np.polyfit(le, np.log([r[1] for r in rows[3:]]), 1)[0]:.2f}, "
      f"gap {np.polyfit(le, np.log([r[2] for r in rows[3:]]), 1)[0]:.2f}")
print("(H3 at eps = 0.05 not rerun: h3-nested-rung.md gives 4.0e7.)")

# ================================================================ 4. scope: misspecified n, non-unitary
hr("4. SCOPE: misspecified fiber dimension, projected readout, non-unitary transport")
print("(a) n UNDERSTATED in the null set: class-2 CS5 in U(5) (||C-I|| = 2.629), tested against")
print("    the class-2 spectra of a smaller assumed fiber (padded with 1s):")
C5 = gc(*NULL_WORLDS['CS5'][:2])
for nn_ in [2, 3, 4, 5]:
    for R in [5, 20, 100]:
        r = gap_rates(C5, R, 1000, 8000 + 10 * nn_ + R, n_null=nn_)
        print(f"    assumed n={nn_} (g={g_of(nn_):.3f}) R={R:3d}: false certification rate {r['gap']:.3f}")

print("\n(b) PROJECTED READOUT: class-2 pair in U(4), only a 2-frame read (top-left 2x2 of the")
print("    commutator-loop action), tested as if n = 2. The compressed block need not be unitary;")
print("    Procrustes forces it, and the result can sit anywhere in U(2):")
for name in ['CS4', 'D8+I2']:
    C = gc(*NULL_WORLDS[name][:2]); P = procrustes(C[:2, :2])
    for R in [5, 20, 100]:
        r = gap_rates(C[:2, :2], R, 1000, 8100 + R + (0 if name == 'CS4' else 50), n_null=2)
        print(f"    {name:>6s}: ||Procrustes(block)-I|| = {dev(P):.3f}, R={R:3d}: false certification {r['gap']:.3f}")
print("    Under projected readout the gap rung is not valid. (H2 itself is unaffected for the")
print("    direct commutator loop of an ABELIAN world, whose block is exactly I.)")

print("\n(c) n OVERSTATED: the same U(2) worlds, fiber really U(8) with 6 trivial dimensions")
print("    (holonomy W (+) I6, full 8x8 readout, null set of U(8), g(8) = 2.165):")
for iw, (name, (A, B)) in enumerate([('D8', NULL_WORLDS['D8'][:2]), ('WZ', (_wza, _wzb)), ('Dgen', (mirror(0), mirror(0.5))),
                                     ('D16', (mirror(0), mirror(np.pi / 8)))]):
    C = bdiag(gc(A, B), np.eye(6, dtype=complex))
    for R in [20, 100]:
        r = gap_rates(C, R, 500, 8200 + 10 * iw + R)
        r2 = gap_rates(gc(A, B), R, 500, 8300 + 10 * iw + R)
        print(f"    {name:>5s} ||C-I||={dev(C):.3f} R={R:3d}: certify rate in U(8) {r['gap']:.3f}   (in U(2): {r2['gap']:.3f})")
print("    Overstating n is conservative: size stays <= alpha, power is lost for g(n') <= ||C-I|| < g(n).")

print("\n(d) NON-UNITARY transport: GL(4) class-2 Heisenberg pair Heis(eps) near I (h3 GL track),")
print("    read with the unitary pipeline as if it were Kato transport (n = 4):")


def E4(i, j):
    M = np.zeros((4, 4), dtype=complex); M[i, j] = 1.0; return M


for e in [0.5, 0.3]:
    A = np.eye(4) + np.sqrt(2) * e * E4(0, 1); B = np.eye(4) + e * E4(1, 2)
    C = gc(A, B)
    for R in [20, 200, 2000]:
        r = gap_rates(C, R, 1000, 8400 + R + int(100 * e))
        print(f"    eps={e}: ||C-I|| = {dev(C):.3f}, R={R:5d}: H2 fires {r['b']:.3f}, gap rung 'certifies class>=3' {r['gap']:.3f}")
print("    Class-2 commutators are not quantized off U(n): the gap rung is unitary-only.")

# ================================================================ 5. end-to-end Kato transport
hr("5. END-TO-END: Kato transport in Gr(2,4), commutator loop, path jitter 0.01/step, readout 0.1")
NSTEP = 12
V0 = np.vstack([np.eye(2), np.zeros((2, 2))]).astype(complex)


def loop_path(U):
    t = np.linspace(0, np.pi / 2, NSTEP + 1)
    return ([np.vstack([np.cos(x) * I2, np.sin(x) * I2]) for x in t] +
            [np.vstack([np.sin(x) * U, np.cos(x) * I2]) for x in t[1:]])


def comm_path(A, B):
    pts = None
    for U, s in reversed([(A, 1), (B, 1), (A, -1), (B, -1)]):
        p = loop_path(U)
        p = p[::-1] if s < 0 else p
        pts = p if pts is None else pts + p[1:]
    return pts


def polar(M):
    U, _, Vh = np.linalg.svd(M, full_matrices=False)
    return U @ Vh


def transport(pts, nb, sp, rng):
    V = np.broadcast_to(V0, (nb, 4, 2)).copy()
    for j in range(1, len(pts)):
        W = pts[j]
        if sp > 0 and np.abs(W[2:]).max() > 1e-12:
            W = polar(W + (rng.standard_normal((nb, 4, 2)) + 1j * rng.standard_normal((nb, 4, 2))) * sp / np.sqrt(2))
        else:
            W = np.broadcast_to(W, (nb, 4, 2))
        V = W @ polar(dag(W) @ V)
    return V[:, :2, :]


SP, SRD = 0.01, 0.1
print(f"{'world':>8s} {'||C-I||':>8s} {'R':>4s} {'trials':>6s} | {'gap':>6s} {'p_a<a':>6s} {'p_b<a':>6s}")
for iw, (name, (A, B)) in enumerate([('AB', NULL_WORLDS['AB'][:2]), ('D8', NULL_WORLDS['D8'][:2]),
                                     ('Dih2.70', dih(2.70)), ('Dih2.40', dih(2.40)), ('WZ', (_wza, _wzb))]):
    rng = np.random.default_rng(9000 + iw)
    pts = comm_path(A, B)
    if iw == 0:
        print(f"  (noiseless transport error on D8 commutator: "
              f"{np.abs(transport(comm_path(*NULL_WORLDS['D8'][:2]), 1, 0, rng)[0] - gc(*NULL_WORLDS['D8'][:2])).max():.1e})")
    for R in [5, 20, 100]:
        n = (1000 if name in ('AB', 'D8') else 300) // (2 if R == 100 else 1)
        H = transport(pts, n * R, SP, rng).reshape(n, R, 2, 2)
        Y = H + (rng.standard_normal(H.shape) + 1j * rng.standard_normal(H.shape)) * SRD / np.sqrt(2)
        m, s2, df = shot_stats(Y)
        pa, pb, dh, _ = pvals(m, s2, df, R, 2, rng, need_a=np.ones(n, bool))
        print(f"{name:>8s} {dev(gc(A, B)):8.3f} {R:4d} {n:6d} | {((pa<ALPHA)&(pb<ALPHA)).mean():6.3f} "
              f"{(pa<ALPHA).mean():6.3f} {(pb<ALPHA).mean():6.3f}")

print(f"\nruntime {time.time()-T0:.0f}s")

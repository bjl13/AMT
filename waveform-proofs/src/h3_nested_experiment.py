"""
H3 (nested ordering, depth 3): nested-commutator detector against a matched H2 (class <= 2) null.
A positive result certifies class >= 3, a lower bound; it does not place a world at class 3.

Target invariant. For two closed frame loops a, b the weight-3 basic commutators of F2 are
    w3a = [[a,b],a]      w3b = [[a,b],b]        ([x,y] = x y x^-1 y^-1)
and they generate gamma_3(F2) mod gamma_4. By Ladder Theorem 1 both loop holonomies are I for
EVERY holonomy of nilpotency class <= 2, in any representation dimension, under full-frame
readout. A class-3 holonomy makes at least one of them != I -- but not necessarily both
(world Q16 below fires only on w3b), so the detector reads BOTH nested-commutator loops and
combines them.

Statistic. Each nested loop is read out as in H2: transport the input frame
X = I around the loop, R noisy shots Y = W + E, W_hat = Procrustes(mean Y), d = ||W_hat - I||_F.
Combined statistic  T = sqrt(d_a^2 + d_b^2)   (Frobenius deviation of diag(W3a, W3b) from I);
also reported: T_max = max(d_a, d_b) and the single-bracket T_1 = d_a.

Matched null. H2 (class <= 2) prediction W3a = W3b = I, simulated at the estimated noise scale
(M_NULL draws). Two calibrations:
  plugin   -- H2's method: per-loop plug-in sigma_eff from the shot spread.
  student  -- bootstrap-t: statistic studentized by a sigma_hat pooled over both loops,
              null draws re-simulate sigma_hat from its chi-square law. Fixes H2's R<5 wobble.

Tracks.
  U  unitary (Kato-compatible) worlds in U(2), all depth-1 spectra matched:
       D8   two mirrors at 45 deg     -> dihedral order 8, CLASS 2  (the matched null)
       D16  two mirrors at 22.5 deg   -> dihedral order 16, class 3 (both brackets fire)
       Q16  R(z,pi/2), R(x,pi)        -> generalized quaternion, class 3, ONLY w3b fires
       Dgen mirrors at 0.5 rad        -> infinite dihedral, not nilpotent
       WZ   the Wilczek-Zee pair from wilczek_zee.py (Gr(2,4))
       NN(eps) R(x,eps), R(y,eps)     -> small-holonomy family, not nilpotent; depth-k ~ eps^k
  G  unipotent GL(4) worlds (exact nilpotent, continuous eps), matched at depths 1 AND 2:
       Heis(eps)  class 2 null         Uni4(eps)  class 3 alternative (ladder_theorem.py H3)
  E  end-to-end: holonomies produced by discrete Kato (parallel) transport of a 2-frame along
     loops in Gr(2,4) with per-step path jitter, words traversed as concatenated loops.

numpy only. Run time a few minutes on 4 cores.
"""
import numpy as np
import time

ALPHA = 0.05
M_NULL = 400
SIGMA = 0.3                     # per-shot readout noise (as in H2)
I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
T0 = time.time()


# ---------------------------------------------------------------- group algebra
def su2(axis, angle):
    n = np.asarray(axis, float); n = n / np.linalg.norm(n)
    G = n[0] * SX + n[1] * SY + n[2] * SZ
    return np.cos(angle / 2) * I2 - 1j * np.sin(angle / 2) * G


def mirror(theta):                     # reflection across the line at angle theta (O(2) in U(2))
    c, s = np.cos(2 * theta), np.sin(2 * theta)
    return np.array([[c, s], [s, -c]], dtype=complex)


def gc(X, Y):                          # group commutator
    return X @ Y @ np.linalg.inv(X) @ np.linalg.inv(Y)


def dev(M):
    n = M.shape[-1]
    return np.linalg.norm(M - np.eye(n), axis=(-2, -1))


def words(A, B):
    """loop holonomies of the words used by the ladder: a, b, [a,b], [[a,b],a], [[a,b],b]."""
    C = gc(A, B)
    return dict(a=A, b=B, c=C, w3a=gc(C, A), w3b=gc(C, B))


def lcs_depths(A, B, kmax=5):
    """max ||w - I|| over all left-normed basic-type commutators of weight k (k = 1..kmax)."""
    level = [A, B]
    out = [max(dev(A), dev(B))]
    level = [gc(A, B)]
    out.append(dev(level[0]))
    for _ in range(3, kmax + 1):
        level = [gc(c, g) for c in level for g in (A, B)]
        out.append(max(dev(c) for c in level))
    return out


def procrustes(M):
    U, _, Vh = np.linalg.svd(M)
    return U @ Vh


# ---------------------------------------------------------------- worlds
def nn(eps):
    return su2([1, 0, 0], eps), su2([0, 1, 0], eps)


_wza = procrustes(np.array([[0.1433, -0.9897], [0.9897, 0.1433]], dtype=complex))
_wzb = procrustes(np.array([[0.1433, -0.9897j], [-0.9897j, 0.1433]], dtype=complex))

U_WORLDS = {
    'Z':    (I2.copy(), I2.copy()),
    'D8':   (mirror(0.0), mirror(np.pi / 4)),
    'D16':  (mirror(0.0), mirror(np.pi / 8)),
    'Q16':  (su2([0, 0, 1], np.pi / 2), su2([1, 0, 0], np.pi)),
    'Dgen': (mirror(0.0), mirror(0.5)),
    'WZ':   (_wza, _wzb),
}
U_CLASS = {'Z': '0', 'D8': '2', 'D16': '3', 'Q16': '3', 'Dgen': 'inf', 'WZ': 'inf'}


def E4(i, j):
    M = np.zeros((4, 4)); M[i, j] = 1.0; return M


def uni4(eps):                         # ladder_theorem.py H3 witness, scaled by eps
    return np.eye(4) + eps * (E4(0, 1) + E4(2, 3)), np.eye(4) + eps * E4(1, 2)


def heis4(eps):
    """class-2 null matched to uni4(eps): ||A-I|| equal, ||[A,B]-I|| equal (exactly)."""
    d2 = dev(gc(*uni4(eps)))
    mu = d2 / (np.sqrt(2) * eps)
    return np.eye(4) + np.sqrt(2) * eps * E4(0, 1), np.eye(4) + mu * E4(1, 2)


# ---------------------------------------------------------------- readout + detector
def sample_loop(W, sigma, R, n, rng, real=False):
    """Sufficient statistics of R Gaussian shots of loop holonomy W, for n independent trials:
    the shot mean, and the pooled per-real-component shot variance (exact chi-square law,
    independent of the mean). Equivalent in distribution to drawing all R shots."""
    d = W.shape[-1]
    if real:
        m = W + rng.standard_normal((n, d, d)) * sigma / np.sqrt(R)
        ncomp, v = d * d, sigma ** 2
    else:
        m = W + (rng.standard_normal((n, d, d)) + 1j * rng.standard_normal((n, d, d))) * sigma / np.sqrt(2 * R)
        ncomp, v = 2 * d * d, sigma ** 2 / 2
    if R > 1:
        df = ncomp * (R - 1)
        s2 = v * rng.chisquare(df, n) / df
    else:
        df, s2 = 0, np.full(n, v)       # R = 1: known per-shot scale (as in the H2 script)
    return m, s2, df


def combine(D, comb):
    if comb == 'rss':
        return np.sqrt((D ** 2).sum(-1))
    if comb == 'max':
        return D.max(-1)
    if comb == 'single':
        return D[..., 0]
    raise ValueError(comb)


def null_devs(scale, d, M, rng, real):
    """deviation of the read-out estimate of an identity loop, scale = sigma_eff (n,)."""
    n = scale.shape[0]
    if real:
        E = rng.standard_normal((n, M, d, d)) * scale[:, None, None, None]
        return dev(np.eye(d) + E)
    E = (rng.standard_normal((n, M, d, d)) + 1j * rng.standard_normal((n, M, d, d))) * scale[:, None, None, None]
    return dev(procrustes(np.eye(d) + E))


def run_detector(loops, sigma, R, n, rng, comb='rss', calib='student', real=False, M=M_NULL):
    """Test H0: every loop in `loops` has holonomy I. Returns (reject (n,), T (n,))."""
    d = loops[0].shape[-1]
    ms, s2s, df = [], [], 0
    for W in loops:
        m, s2, df = sample_loop(W, sigma, R, n, rng, real)
        ms.append(m); s2s.append(s2)
    est = [m if real else procrustes(m) for m in ms]
    D = np.stack([dev(e) for e in est], -1)                         # (n, k)
    T = combine(D, comb)
    k = len(loops)
    S2 = np.stack(s2s, -1)                                          # (n, k) per-shot var / comp
    if calib == 'plugin':                                           # H2: per-loop plug-in
        se = np.sqrt(S2 / R)
        Dn = np.stack([null_devs(se[:, j], d, M, rng, real) for j in range(k)], -1)
        Tn = combine(Dn, comb)
        p = (1 + (Tn >= T[:, None]).sum(1)) / (1 + M)
    elif calib == 'student':                                        # pooled bootstrap-t
        se = np.sqrt(S2.mean(-1) / R)
        Dn = np.stack([null_devs(se, d, M, rng, real) for _ in range(k)], -1)
        Tn = combine(Dn, comb)
        if R > 1:
            dfp = df * k
            se_star = se[:, None] * np.sqrt(rng.chisquare(dfp, (n, M)) / dfp)
            p = (1 + (Tn / se_star >= (T / se)[:, None]).sum(1)) / (1 + M)
        else:
            p = (1 + (Tn >= T[:, None]).sum(1)) / (1 + M)
    else:
        raise ValueError(calib)
    return p < ALPHA, T


def depth3_loops(A, B):
    w = words(A, B); return [w['w3a'], w['w3b']]


def depth2_loops(A, B):
    return [words(A, B)['c']]


def rate(loops, R, n, seed, **kw):
    rng = np.random.default_rng(seed)
    rej, _ = run_detector(loops, kw.pop('sigma', SIGMA), R, n, rng, **kw)
    return rej.mean()


def r80(loop_fn, eps, seed, comb='rss', real=False, n=300, target=0.8):
    """smallest R (log-interpolated) with power >= target; returns (R80, power curve)."""
    grid = np.unique(np.round(np.logspace(0, 12, 61)).astype(np.int64))
    loops = loop_fn(eps)
    prev = None
    for i, R in enumerate(grid):
        pw = rate(loops, int(R), n, seed + i, comb=comb, real=real)
        if pw >= target:
            if prev is None:
                return float(R), pw
            R0, p0 = prev
            f = (target - p0) / max(pw - p0, 1e-9)
            return float(np.exp(np.log(R0) + f * (np.log(R) - np.log(R0)))), pw
        prev = (R, pw)
    return np.inf, prev[1]


def hr(title):
    print("\n" + title)
    print("-" * len(title))


# ================================================================ 0. exact structure
hr("0. EXACT STRUCTURE OF THE WORLDS (no noise)")
print("U(2) track: depth-k = max ||w - I||_F over weight-k left-normed commutators")
print(f"{'world':>6s} {'class':>5s} {'||A-I||':>8s} {'||B-I||':>8s} {'eig A':>20s} "
      f"{'d2 [A,B]':>9s} {'d3a':>7s} {'d3b':>7s} {'d4':>7s} {'d5':>7s}")
for name, (A, B) in U_WORLDS.items():
    w = words(A, B)
    lc = lcs_depths(A, B, 5)
    eA = np.sort_complex(np.round(np.linalg.eigvals(A), 3))
    es = ",".join(f"{e.real:+.0f}" if abs(e.imag) < 1e-9 else f"{e:.2f}" for e in eA)
    print(f"{name:>6s} {U_CLASS[name]:>5s} {dev(A):8.3f} {dev(B):8.3f} {es:>20s} "
          f"{dev(w['c']):9.3f} {dev(w['w3a']):7.3f} {dev(w['w3b']):7.3f} {lc[3]:7.3f} {lc[4]:7.3f}")
print("D8, D16, Dgen: both generators are mirrors, eigenvalues {+1,-1}: depth-1 spectra matched.")
print("Q16: signal only on [[A,B],B]; a single-bracket ([[A,B],A]) detector is blind to it.")
print("U(2) structural fact: a non-abelian class-2 pair in U(2) has [A,B] = -I exactly (central,")
print("det 1, scalar on the irreducible 2-dim block, c^2 = 1). So the class-2 null cannot be")
print("matched to a class-3 world at depth 2 in U(2), and no class-2 unitary pair exists near I.")

print("\nSmall-holonomy family NN(eps) = R(x,eps), R(y,eps) (not nilpotent). eps is the ROTATION")
print("angle, R(n,eps) = exp(-i eps/2 n.sigma), as in h2_nonabelian_experiment.py; in the generator-")
print("angle convention exp(-i t n.sigma) the same row is t = eps/2.")
print(f"{'eps':>6s} {'d1':>8s} {'d2':>10s} {'d3a':>10s} {'d3b':>10s} {'d3/eps^3':>9s} {'d2/eps^2':>9s}")
for e in [1.0, 0.5, 0.3, 0.2, 0.1, 0.05, 0.03, 0.01]:
    w = words(*nn(e))
    print(f"{e:6.2f} {dev(w['a']):8.4f} {dev(w['c']):10.3e} {dev(w['w3a']):10.3e} {dev(w['w3b']):10.3e} "
          f"{dev(w['w3a'])/e**3:9.4f} {dev(w['c'])/e**2:9.4f}")

print("\nGL(4) unipotent track, matched at depths 1 and 2 (all eigenvalues 1):")
print(f"{'eps':>6s} {'world':>6s} {'||A-I||':>8s} {'||B-I||':>8s} {'d2':>10s} {'d3a':>10s} {'d3b':>10s} {'d4':>9s}")
for e in [0.5, 0.2, 0.1]:
    for name, fn in [('Heis', heis4), ('Uni4', uni4)]:
        A, B = fn(e); w = words(A, B); lc = lcs_depths(A, B, 4)
        print(f"{e:6.2f} {name:>6s} {dev(A):8.4f} {dev(B):8.4f} {dev(w['c']):10.3e} "
              f"{dev(w['w3a']):10.3e} {dev(w['w3b']):10.3e} {lc[3]:9.1e}")

# ================================================================ 1. separation snapshot
hr(f"1. SEPARATION (sigma={SIGMA}, R=20, 1000 trials, studentized calibration)")
print(f"{'world':>6s} {'class':>5s} | {'H2 depth-2':>10s} | {'H3 single':>9s} {'H3 max':>7s} {'H3 rss':>7s}")
for iw, (name, (A, B)) in enumerate(U_WORLDS.items()):
    r2 = rate(depth2_loops(A, B), 20, 1000, 11 + 10 * iw)
    rs = rate(depth3_loops(A, B), 20, 1000, 12 + 10 * iw, comb='single')
    rm = rate(depth3_loops(A, B), 20, 1000, 13 + 10 * iw, comb='max')
    rr = rate(depth3_loops(A, B), 20, 1000, 14 + 10 * iw, comb='rss')
    print(f"{name:>6s} {U_CLASS[name]:>5s} | {r2:10.3f} | {rs:9.3f} {rm:7.3f} {rr:7.3f}")
print("H2 fires on every non-abelian world, including the class-2 null D8: it cannot place a")
print("world above class 2. H3 clears D8 at ~alpha and fires on class >= 3;")
print("the single-bracket version misses Q16 entirely.")

# ================================================================ 2. calibration vs R
hr("2. CALIBRATION ON THE CLASS-2 NULL D8 vs R (sigma=0.3, 4000 trials; SE ~ 0.0035)")
print("(direct readout: D8's nested loops ARE identity loops, so D8 and Z are the same null")
print(" in distribution; D8 is used because H2 fires on it.)")
print(f"{'R':>4s} | {'H2 plugin':>9s} {'H2 student':>10s} | {'H3 plugin':>9s} {'H3 student':>10s} "
      f"{'H3max plug':>10s} {'H3max stud':>10s} | {'D16 pow':>7s} {'Q16 pow':>7s}")
D8 = U_WORLDS['D8']
for R in [1, 2, 3, 5, 10, 20, 50]:
    n = 4000
    h2p = rate(depth2_loops(*U_WORLDS['Z']), R, n, 100 + R, calib='plugin')
    h2s = rate(depth2_loops(*U_WORLDS['Z']), R, n, 200 + R, calib='student')
    dp = rate(depth3_loops(*D8), R, n, 300 + R, calib='plugin')
    ds = rate(depth3_loops(*D8), R, n, 400 + R, calib='student')
    mp = rate(depth3_loops(*D8), R, n, 500 + R, calib='plugin', comb='max')
    ms = rate(depth3_loops(*D8), R, n, 600 + R, calib='student', comb='max')
    p16 = rate(depth3_loops(*U_WORLDS['D16']), R, 1000, 700 + R)
    pq = rate(depth3_loops(*U_WORLDS['Q16']), R, 1000, 800 + R)
    print(f"{R:4d} | {h2p:9.3f} {h2s:10.3f} | {dp:9.3f} {ds:10.3f} {mp:10.3f} {ms:10.3f} | {p16:7.2f} {pq:7.2f}")
print("(H2 columns: the depth-2 detector on an identity commutator loop -- reproduces the H2")
print(" R=2 wobble under the plug-in, and shows whether the bootstrap-t removes it.)")

# ================================================================ 3. power vs R and eps
hr("3. R NEEDED FOR POWER 0.8 AT ALPHA 0.05 vs HOLONOMY ANGLE eps (NN(eps), sigma=0.3)")
print("H2 = depth-2 detector on [A,B]; H3 = combined rss depth-3 detector on both nested loops.")
print(f"{'eps':>6s} {'d2 true':>9s} {'d3 rss true':>11s} | {'R80 H2':>11s} {'R80 H3':>11s} "
      f"{'ratio':>8s} | {'R80H2*d2^2':>10s} {'R80H3*d3^2':>10s} | {'FAR@R80H3':>9s}")
rows = []
for i, e in enumerate([1.0, 0.5, 0.3, 0.2, 0.1, 0.05, 0.03]):
    w = words(*nn(e))
    s2 = dev(w['c'])
    s3 = np.sqrt(dev(w['w3a']) ** 2 + dev(w['w3b']) ** 2)
    R2, _ = r80(lambda x: depth2_loops(*nn(x)), e, 10000 + 100 * i)
    R3, _ = r80(lambda x: depth3_loops(*nn(x)), e, 20000 + 100 * i)
    far = rate([I2, I2], max(int(round(R3)), 1), 2000, 30000 + i)
    rows.append((e, s2, s3, R2, R3))
    print(f"{e:6.2f} {s2:9.2e} {s3:11.2e} | {R2:11.3g} {R3:11.3g} {R3/R2:8.3g} | "
          f"{R2*s2**2:10.3f} {R3*s3**2:10.3f} | {far:9.3f}")
e_ = np.log([r[0] for r in rows[3:]]);
sl2 = np.polyfit(e_, np.log([r[3] for r in rows[3:]]), 1)[0]
sl3 = np.polyfit(e_, np.log([r[4] for r in rows[3:]]), 1)[0]
print(f"log-log slope of R80 vs eps (eps <= 0.2): depth-2 {sl2:.2f} (theory -4), depth-3 {sl3:.2f} (theory -6)")
print("R80 * signal^2 is ~constant: R80 ~ c * sigma^2 / ||signal||^2, so R80 scales with sigma^2.")

# ================================================================ 4. GL(4) unipotent track
hr("4. GL(4) UNIPOTENT TRACK: class-2 Heis null matched at depths 1 AND 2 vs class-3 Uni4")
print("real Gaussian readout noise sigma=0.3 per entry, estimate = shot mean (no Procrustes).")
print(f"{'eps':>5s} {'R':>7s} | {'H2 on Heis':>10s} {'H2 on Uni4':>10s} | {'H3 FAR Heis':>11s} {'H3 pow Uni4':>11s}")
for j, (e, Rs) in enumerate([(0.5, [2, 5, 20, 100]), (0.2, [100, 1000, 5000]), (0.1, [1000, 20000, 200000])]):
    for k, R in enumerate(Rs):
        sd = 40000 + 100 * j + 10 * k
        a = rate(depth2_loops(*heis4(e)), R, 2000, sd + 1, real=True)
        b = rate(depth2_loops(*uni4(e)), R, 2000, sd + 2, real=True)
        c = rate(depth3_loops(*heis4(e)), R, 2000, sd + 3, real=True)
        d = rate(depth3_loops(*uni4(e)), R, 2000, sd + 4, real=True)
        print(f"{e:5.2f} {R:7d} | {a:10.3f} {b:10.3f} | {c:11.3f} {d:11.3f}")
print("H2 fires equally on both (depth-2 matched by construction); only H3 separates them.")
print("\nR80 for Uni4(eps) vs Heis null (H3 rss detector):")
print(f"{'eps':>6s} {'d3 true':>10s} {'R80':>10s} {'R80*d3^2':>9s}")
for i, e in enumerate([0.5, 0.3, 0.2, 0.1, 0.05]):
    A, B = uni4(e); w = words(A, B)
    s3 = np.sqrt(dev(w['w3a']) ** 2 + dev(w['w3b']) ** 2)
    R3, _ = r80(lambda x: depth3_loops(*uni4(x)), e, 50000 + 100 * i, real=True)
    print(f"{e:6.2f} {s3:10.3e} {R3:10.3g} {R3*s3**2:9.3f}")

# ================================================================ 5. assembled vs direct
hr("5. WHY THE NESTED LOOP MUST BE READ DIRECTLY (sigma=0.3, R=20, 2000 trials)")
print("assembled = brackets computed from separately estimated A_hat, B_hat (H2's corroborating")
print("readout); direct = nested loop transported and read as one loop.")
print(f"{'world':>6s} {'true d3 rss':>11s} | {'direct med':>10s} {'assembled med':>13s} {'assembled bias':>14s}")
rng = np.random.default_rng(60000)
EXTRA = {'NN(0.5)': nn(0.5), 'NN(0.2)': nn(0.2), 'NN(0.1)': nn(0.1)}
for name in ['Z', 'D8', 'D16', 'Q16', 'WZ', 'NN(0.5)', 'NN(0.2)', 'NN(0.1)']:
    A, B = U_WORLDS[name] if name in U_WORLDS else EXTRA[name]
    truth = np.sqrt(sum(dev(x) ** 2 for x in depth3_loops(A, B)))
    mA, _, _ = sample_loop(A, SIGMA, 20, 2000, rng)
    mB, _, _ = sample_loop(B, SIGMA, 20, 2000, rng)
    Ah, Bh = procrustes(mA), procrustes(mB)
    Ch = gc(Ah, Bh)
    asm = np.sqrt(dev(gc(Ch, Ah)) ** 2 + dev(gc(Ch, Bh)) ** 2)
    dirl = [procrustes(sample_loop(W, SIGMA, 20, 2000, rng)[0]) for W in depth3_loops(A, B)]
    dr = np.sqrt(sum(dev(x) ** 2 for x in dirl))
    print(f"{name:>7s} {truth:11.2e} | {np.median(dr):10.3e} {np.median(asm):13.3e} {np.median(asm)-truth:+14.2e}"
          f"   asm rms err {np.sqrt(((asm-truth)**2).mean()):.2e}")
print("On the class-2 null D8 the assembled bracket is far from I (noise propagated through a")
print("large [A,B] = -I), while on Z it is ~0: its null law depends on the unknown lower-depth")
print("structure, so there is no world-free matched null for it. The direct readout's null law is")
print("the same for every class <= 2 world.")
print("Near the identity the opposite holds: the assembled bracket's error is suppressed by the")
print("square of the single-loop holonomy size (plus a noise^3 floor, cf. Z), not ~ sigma_eff, so")
print("assembling from single-loop estimates is far MORE efficient there (NN rows) -- the eps^-6")
print("cost in section 3 belongs to the direct nested-loop readout, not to depth 3 as such. But it")
print("is biased upward by noise-generated brackets and needs a model-based (fitted class-2) null;")
print("not built here.")

# ================================================================ 6. end-to-end Kato transport
hr("6. END-TO-END: Kato transport in Gr(2,4), words as concatenated loops")
NSTEP = 12
V0 = np.vstack([np.eye(2), np.zeros((2, 2))]).astype(complex)


def loop_path(U):
    """frames along a closed horizontal loop S -> S_perp -> S with holonomy U (2x2 unitary)."""
    t = np.linspace(0, np.pi / 2, NSTEP + 1)
    seg1 = [np.vstack([np.cos(x) * I2, np.sin(x) * I2]) for x in t]
    seg2 = [np.vstack([np.sin(x) * U, np.cos(x) * I2]) for x in t[1:]]
    return seg1 + seg2


def word_path(letters, gens):
    """letters: list like [('a',1),('b',-1),...] for rho(x1)...rho(xn); traversed right-to-left."""
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
W3A = WC + WA + inv_word(WC) + inv_word(WA)
W3B = WC + WB + inv_word(WC) + inv_word(WB)


def polar(M):
    U, _, Vh = np.linalg.svd(M, full_matrices=False)
    return U @ Vh


def transport(pts, nb, sig_path, rng):
    """discrete Kato transport of V0 along pts for nb independent traversals with per-step
    jitter of the interior subspaces; returns holonomy samples (nb,2,2)."""
    V = np.broadcast_to(V0, (nb, 4, 2)).copy()
    for j in range(1, len(pts)):
        W = pts[j]
        if sig_path > 0 and np.abs(W[2:]).max() > 1e-12:     # jitter interior points, not junctions in S
            G = (rng.standard_normal((nb, 4, 2)) + 1j * rng.standard_normal((nb, 4, 2))) * sig_path / np.sqrt(2)
            W = polar(W + G)
        else:
            W = np.broadcast_to(W, (nb, 4, 2))
        V = W @ polar(np.conj(np.swapaxes(W, -1, -2)) @ V)
    return V[:, :2, :]


rng = np.random.default_rng(70000)
print("noiseless transport vs algebraic word holonomy (max ||Hol_transport - Hol_algebra||):")
for name in ['D8', 'D16', 'Q16', 'WZ']:
    A, B = U_WORLDS[name]; g = dict(a=A, b=B); w = words(A, B)
    errs = [np.abs(transport(word_path(wd, g), 1, 0.0, rng)[0] - w[k]).max()
            for wd, k in [(WA, 'a'), (WB, 'b'), (WC, 'c'), (W3A, 'w3a'), (W3B, 'w3b')]]
    print(f"  {name:>4s}: {max(errs):.1e}   (nested-loop path length {len(word_path(W3A, g))} steps)")


def e2e_test(name, R, n, sig_path, sig_read, calib, rng):
    A, B = U_WORLDS[name]; g = dict(a=A, b=B)
    D, S2 = [], []
    for wd in (W3A, W3B):
        H = transport(word_path(wd, g), n * R, sig_path, rng).reshape(n, R, 2, 2)
        Y = H + (rng.standard_normal(H.shape) + 1j * rng.standard_normal(H.shape)) * sig_read / np.sqrt(2)
        m = Y.mean(1); Wh = procrustes(m)
        D.append(dev(Wh))
        dY = Y - m[:, None]
        if calib == 'allcomp':           # H2-style: pooled over all 8 real components
            S2.append(0.5 * (np.abs(dY) ** 2).sum((1, 2, 3)) / (4 * (R - 1)))
            dfl = 8 * (R - 1)
        else:                            # tangent-only: anti-Hermitian part of Wh^dagger dY
            Tm = np.conj(np.swapaxes(Wh, -1, -2))[:, None] @ dY
            Ah = 0.5 * (Tm - np.conj(np.swapaxes(Tm, -1, -2)))
            S2.append((np.abs(Ah) ** 2).sum((1, 2, 3)) / (4 * (R - 1)))
            dfl = 4 * (R - 1)
    D = np.stack(D, -1); T = np.sqrt((D ** 2).sum(-1))
    se = np.sqrt(np.stack(S2, -1).mean(-1) / R)
    Dn = np.stack([null_devs(se, 2, M_NULL, rng, False) for _ in range(2)], -1)
    Tn = np.sqrt((Dn ** 2).sum(-1))
    se_star = se[:, None] * np.sqrt(rng.chisquare(2 * dfl, (n, M_NULL)) / (2 * dfl))
    p = (1 + (Tn / se_star >= (T / se)[:, None]).sum(1)) / (1 + M_NULL)
    return (p < ALPHA).mean(), np.median(T)


SP, SRD = 0.01, 0.1
Hj = transport(word_path(WA, dict(a=U_WORLDS['D8'][0], b=U_WORLDS['D8'][1])), 4000, SP, rng)
print(f"\npath jitter sigma_path={SP}/step, readout sigma={SRD}. Single-loop holonomy jitter: "
      f"rms ||Hol - Hol_0|| = {np.sqrt((dev(Hj @ np.conj(U_WORLDS['D8'][0]).T)**2).mean()):.3f}")
Hn = transport(word_path(W3A, dict(a=U_WORLDS['D8'][0], b=U_WORLDS['D8'][1])), 4000, SP, rng)
Hm = Hn.mean(0)
print(f"D8 nested loop under jitter alone: rms ||W3a - I|| = {np.sqrt((dev(Hn)**2).mean()):.3f}, "
      f"||mean W3a - I|| = {dev(Hm):.4f}, Hermitian/anti-Hermitian spread ratio = "
      f"{np.linalg.norm(0.5*(Hn-I2+np.conj(np.swapaxes(Hn-I2,-1,-2))))/np.linalg.norm(0.5*(Hn-I2-np.conj(np.swapaxes(Hn-I2,-1,-2)))):.3f}")
print(f"\n{'R':>5s} | {'D8 FAR allcomp':>14s} {'D8 FAR tangent':>14s} | {'D16 pow':>7s} {'Q16 pow':>7s} | {'Z FAR tangent':>13s}")
for R in [5, 20, 100]:
    n = 400 if R < 100 else 150
    fa, _ = e2e_test('D8', R, n, SP, SRD, 'allcomp', rng)
    ft, _ = e2e_test('D8', R, n, SP, SRD, 'tangent', rng)
    p16, _ = e2e_test('D16', R, 200, SP, SRD, 'tangent', rng)
    pq, _ = e2e_test('Q16', R, 200, SP, SRD, 'tangent', rng)
    fz, _ = e2e_test('Z', R, n, SP, SRD, 'tangent', rng)
    print(f"{R:5d} | {fa:14.3f} {ft:14.3f} | {p16:7.2f} {pq:7.2f} | {fz:13.3f}")
print("(binomial SE ~0.011 at n=400, ~0.018 at n=150)")

# ================================================================ 7. unitary quantization gap
hr("7. UNITARY SHORTCUT: depth 2 + unitarity + fiber dimension already exclude class 2")
print("If (A,B) in U(n) generate a class-2 non-abelian group, C=[A,B] is central, so on each")
print("irreducible joint block of dim d it is a scalar c with c^d = 1 (det C = 1 on the block), and")
print("c != 1 on at least one block. Hence ||C - I||_F >= g(n) = min_{2<=d<=n} 2 sqrt(d) sin(pi/d).")
print("So 0 < ||[A,B] - I||_F < g(n) certifies class >= 3 from the depth-2 loop alone.")
print(f"{'n':>4s} {'g(n)':>7s}")
for n_ in [2, 3, 4, 6, 8, 16, 32, 64, 256]:
    g = min(2 * np.sqrt(d) * np.sin(np.pi / d) for d in range(2, n_ + 1))
    print(f"{n_:4d} {g:7.3f}")
print("U(2) worlds against g(2) = 2.828:")
for name, (A, B) in list(U_WORLDS.items()) + [('NN(0.1)', nn(0.1)), ('NN(0.03)', nn(0.03))]:
    d2 = dev(gc(A, B))
    verdict = ('abelian' if d2 < 1e-9 else ('class >= 3 by gap' if d2 < 2 * np.sqrt(2) - 1e-9
               else 'at/above gap: depth 2 cannot decide'))
    print(f"  {name:>8s}  ||[A,B]-I|| = {d2:.3e}   {verdict}")
print("Every small-holonomy unitary world is certified class >= 3 by H2's own readout plus the")
print("gap; H3 adds independent information only for non-unitary (GL) transport,")
print("for large or unknown fiber dimension (g(n) ~ 2 pi / sqrt(n) -> 0), or when the certificate")
print("must not lean on the representation theory of U(n).")

print(f"\nruntime {time.time()-T0:.0f}s")

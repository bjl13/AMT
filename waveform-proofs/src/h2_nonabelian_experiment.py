"""
H2 (non-abelian, depth 2): a falsifier with no additive AND no abelian shadow.
A positive result certifies non-abelian holonomy (class >= 2), a lower bound; it does not
place a world at class 2.

Distinctive invariant = loop-order dependence. For two closed frame loops A, B with
holonomies Hol_A, Hol_B in U(2), the commutator-loop holonomy
    Hol_C = Hol_A Hol_B Hol_A^-1 Hol_B^-1
equals I for EVERY commuting (abelian) pair, in any representation dimension under
full-frame readout (Ladder Theorem 1), and for EVERY additive model (which has no
holonomy at all), and differs from I only under genuine non-abelian transport
(Wilczek-Zee, monograph Thm IV.1 k>1). Hol_C is gauge-invariant under global phase
(det Hol_C = 1 identically), so it is the clean operational target.

Comparator = H1, the abelian holonomies {commuting U(2) pairs}. It predicts Hol_C = I.
We inject a non-abelian holonomy, estimate Hol_C from noisy transport of a known input
frame, and test  delta = ||Hol_C_hat - I||_F  against a matched null (Hol_C = I + noise).

Worlds (holonomies injected directly as SU(2) rotations; loop->holonomy already
validated in wilczek_zee.py, so we test the STATISTICAL detection of non-commutativity):
  NA  non-abelian : Hol_A = R(x, a), Hol_B = R(y, b)   -> Hol_C != I
  AB  abelian null: Hol_A = R(x, a), Hol_B = R(x, b)   -> Hol_C  = I  (matched spectra!)
  Z   noise        : Hol_A = Hol_B = I                  -> Hol_C  = I

AB is the crux: identical per-loop rotation ANGLES (eigenvalue spectra) to NA, so any
single-loop magnitude signature is identical by construction; only NON-COMMUTATIVITY
differs. This is the k=2 analogue of the H1 rung's world-H vs world-I matched null.

Observation: transport the input frame X = I2 (columns = 2 orthonormal input states)
around a loop, observe Y = Hol.X + E = Hol + E (E complex-Gaussian, per-shot sigma),
R repeated shots; estimate Hol_hat = nearest unitary to mean(Y) (SVD Procrustes).
Null: plug-in noise sigma_eff estimated from the R shots; simulate Hol_C = I + noise.
"""
import numpy as np

I2 = np.eye(2, dtype=complex)
SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)
M_NULL = 300
ALPHA = 0.05


def su2(axis, angle):
    n = np.asarray(axis, float); n = n/np.linalg.norm(n)
    G = n[0]*SX + n[1]*SY + n[2]*SZ
    return np.cos(angle/2)*I2 - 1j*np.sin(angle/2)*G


def holonomies(world, a, b):
    if world == 'NA':
        HA, HB = su2([1, 0, 0], a), su2([0, 1, 0], b)     # different axes -> noncommuting
    elif world == 'AB':
        HA, HB = su2([1, 0, 0], a), su2([1, 0, 0], b)     # same axis -> commuting, matched angles
    elif world == 'Z':
        HA, HB = I2.copy(), I2.copy()
    else:
        raise ValueError(world)
    HC = HA @ HB @ HA.conj().T @ HB.conj().T
    return HA, HB, HC


def procrustes(M):
    U, _, Vh = np.linalg.svd(M)
    return U @ Vh


def observe(H, sigma, R, rng):
    """R noisy shots of the input frame transported by H; return mean and per-shot noise est."""
    shots = np.array([H + (rng.standard_normal((2, 2)) + 1j*rng.standard_normal((2, 2)))
                      * sigma/np.sqrt(2) for _ in range(R)])
    mean = shots.mean(axis=0)
    # effective noise on the MEAN, estimated from shot spread (per real/imag component)
    if R > 1:
        var_shot = 0.5*(shots.real.var(axis=0, ddof=1) + shots.imag.var(axis=0, ddof=1)).mean()
        sigma_eff = np.sqrt(var_shot/R)
    else:
        sigma_eff = sigma/np.sqrt(2)   # fallback: known per-shot scale
    return mean, sigma_eff


def detect(HC_true, sigma, R, rng):
    meanC, sig_eff = observe(HC_true, sigma, R, rng)
    HC_hat = procrustes(meanC)
    delta = np.linalg.norm(HC_hat - I2)
    # matched null: Hol_C = I + noise at estimated effective scale
    dn = np.empty(M_NULL)
    for t in range(M_NULL):
        Enull = (rng.standard_normal((2, 2)) + 1j*rng.standard_normal((2, 2)))*sig_eff
        dn[t] = np.linalg.norm(procrustes(I2 + Enull) - I2)
    pval = (1 + np.sum(dn >= delta))/(1 + M_NULL)
    return delta, pval, (pval < ALPHA)


def commutator_norm(world, a, b, sigma, R, rng):
    HA, HB, _ = holonomies(world, a, b)
    mA, _ = observe(HA, sigma, R, rng)
    mB, _ = observe(HB, sigma, R, rng)
    HAh, HBh = procrustes(mA), procrustes(mB)
    return np.linalg.norm(HAh @ HBh - HBh @ HAh)


if __name__ == "__main__":
    A, B = np.pi/2, np.pi/2
    print(f"H2 (non-abelian) detector, angles a=b=pi/2; null M={M_NULL}, alpha={ALPHA}\n")

    print("SNAPSHOT (per-shot sigma=0.3, R=20 shots)")
    print(f"{'world':>6s} {'||Hol_A-I||':>11s} {'||[A,B]||_hat':>13s} "
          f"{'delta=||HolC-I||':>16s} {'pval':>7s} {'non-abelian?':>13s}")
    WSEED = {'NA': 11, 'AB': 22, 'Z': 33}
    for w in ['NA', 'AB', 'Z']:
        rng = np.random.default_rng(100 + WSEED[w])
        HA, HB, HC = holonomies(w, A, B)
        loopmag = np.linalg.norm(HA - I2)                 # single-loop magnitude (matched NA vs AB)
        cn = commutator_norm(w, A, B, 0.3, 20, rng)
        delta, pval, det = detect(HC, 0.3, 20, rng)
        print(f"{w:>6s} {loopmag:11.3f} {cn:13.3f} {delta:16.3f} {pval:7.3f} {str(det):>13s}")
    print("\nNote: ||Hol_A - I|| identical for NA and AB by construction (matched spectra) --")
    print("the single-loop magnitude signature CANNOT separate them. Only non-commutativity does.\n")

    WSEED = {'NA': 11, 'AB': 22, 'Z': 33}
    print("POWER/CALIBRATION SWEEP over shot count R (per-shot sigma=0.3, T=150 trials)")
    print(f"{'R':>4s} | {'NA detect':>9s} {'AB falsealarm':>13s} {'Z falsealarm':>13s} "
          f"| {'NA med ||[A,B]||':>16s} {'AB med ||[A,B]||':>16s}")
    for R in [1, 2, 5, 10, 20, 50]:
        T = 150
        det_NA = fa_AB = fa_Z = 0
        cn_NA, cn_AB = [], []
        for t in range(T):
            for w, bucket in [('NA', 'na'), ('AB', 'ab'), ('Z', 'z')]:
                rng = np.random.default_rng(4000*t + WSEED[w] + 3*R)
                HA, HB, HC = holonomies(w, A, B)
                delta, pval, det = detect(HC, 0.3, R, rng)
                if w == 'NA':
                    det_NA += det
                    cn_NA.append(commutator_norm(w, A, B, 0.3, R, rng))
                elif w == 'AB':
                    fa_AB += det
                    cn_AB.append(commutator_norm(w, A, B, 0.3, R, rng))
                else:
                    fa_Z += det
        print(f"{R:4d} | {det_NA/T:9.2f} {fa_AB/T:13.2f} {fa_Z/T:13.2f} "
              f"| {np.median(cn_NA):16.3f} {np.median(cn_AB):16.3f}")
    print(f"\ntrue ||[Hol_A,Hol_B]|| for NA at a=b=pi/2: "
          f"{np.linalg.norm(holonomies('NA',A,B)[0]@holonomies('NA',A,B)[1] - holonomies('NA',A,B)[1]@holonomies('NA',A,B)[0]):.3f}")
    print("GO iff: NA detect -> 1 as R rises; AB & Z falsealarm ~0.05; "
          "NA ||[A,B]|| concentrates on truth, AB ~ 0.")

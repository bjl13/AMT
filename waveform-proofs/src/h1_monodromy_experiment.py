"""
H1 (abelian) rung: a falsifier that does NOT fire on noise.
Rejects H0 (static) via matched-null monodromy recovery; certifies class >= 1.
(Design rationale in notes/h1-abelian-rung.md.)
Worlds: H helical (winding h), I incoherent (random phase, matched magnitudes,
NO winding -- the killer null), S static coherent (phi=1), Z pure noise.
OLD signatures = tension, isotropic z (magnitude-based). NEW = winding-periodogram
peak, significance by phase-scramble (the matched null IS the calibration null).
"""
import numpy as np

N = 96
HGRID = np.linspace(-6*np.pi, 6*np.pi, 1201)
H_FLOOR = 0.75
_MASK = np.abs(HGRID) >= H_FLOOR
_HS = HGRID[_MASK]
_J = np.arange(N)
_E = np.exp(-1j*np.outer(_HS, _J)/N)        # (len_h, N), precomputed once
M_SCRAMBLE = 200
ALPHA = 0.05


def generate(world, snr, h_true, rng):
    a = 1.0 + 0.0j
    sigma = np.sqrt((abs(a)**2)/snr) if snr > 0 else 1.0
    eps = (rng.standard_normal(N) + 1j*rng.standard_normal(N))*sigma/np.sqrt(2)
    if world == 'H':
        return a*np.exp(1j*h_true*_J/N) + eps
    if world == 'I':
        return a*np.exp(1j*rng.uniform(0, 2*np.pi, N)) + eps
    if world == 'S':
        return a*np.ones(N) + eps
    if world == 'Z':
        return (rng.standard_normal(N) + 1j*rng.standard_normal(N))/np.sqrt(2)
    raise ValueError(world)


def peak_of(y):
    P = np.abs(_E @ y)**2 / N
    k = int(np.argmax(P))
    return _HS[k], float(P[k])


def monodromy_test(y, rng):
    # Fitted model comparison (the comparison v2 5.3 promised, now actually run):
    #   Model A (static / trivial bundle phi=1): a_hat = mean(y);  P0 = N|mean|^2
    #   Model B (winding, h free): a_hat(h)=(1/N)sum y e^{-ihj/N}; peak away from DC
    # improvement statistic  dRSS = RSS_A - RSS_B = max_{|h|>=floor} P(h) - P(0),
    # significance by phase-scramble (matched magnitudes, no winding) -> calibration null.
    Pfull = np.abs(_E @ y)**2 / N               # P(h) on |h|>=H_FLOOR grid
    kk = int(np.argmax(Pfull)); h_hat, ppk = _HS[kk], float(Pfull[kk])
    P0 = abs(y.sum())**2 / N                     # DC (h=0) power = static-fit power
    dRSS = ppk - P0
    mags = np.abs(y)
    ph = rng.uniform(0, 2*np.pi, (M_SCRAMBLE, N))
    Y = mags[None, :]*np.exp(1j*ph)
    Pn = np.abs(Y @ _E.T)**2 / N
    P0n = np.abs(Y.sum(axis=1))**2 / N
    dnull = Pn.max(axis=1) - P0n
    pval = (1 + np.sum(dnull >= dRSS))/(1 + M_SCRAMBLE)
    return h_hat, dRSS, pval, (pval < ALPHA)


def old_signatures(y, rng):
    p = np.c_[y.real, y.imag]
    norms = np.linalg.norm(p, axis=1)
    net = np.linalg.norm(p.sum(axis=0))
    tension = norms.sum() - net
    ang = rng.uniform(0, 2*np.pi, (300, N))
    v = norms[None, :, None]*np.stack([np.cos(ang), np.sin(ang)], -1)
    nn = np.linalg.norm(v.sum(axis=1), axis=1)
    z = (net - nn.mean())/nn.std()
    return tension, z


if __name__ == "__main__":
    print(f"N={N}, h_floor={H_FLOOR}, scrambles={M_SCRAMBLE}, alpha={ALPHA}\n")
    rng = np.random.default_rng(1)
    print("SNAPSHOT (snr=5, h_true=3.0)")
    print(f"{'world':>6s} {'tension':>9s} {'z_iso':>8s} | {'h_hat':>7s} "
          f"{'dRSS':>8s} {'pval':>7s} {'monodromy?':>11s}")
    for w in ['H', 'I', 'S', 'Z']:
        y = generate(w, 5, 3.0, np.random.default_rng(100+ord(w)))
        t, z = old_signatures(y, rng)
        hh, dr, pv, det = monodromy_test(y, rng)
        print(f"{w:>6s} {t:9.2f} {z:8.1f} | {hh:7.3f} {dr:8.2f} {pv:7.3f} {str(det):>11s}")

    print("\nPOWER/CALIBRATION SWEEP (T=120 trials/world/snr, h_true=3.0)")
    print(f"{'snr':>5s} | {'H det':>7s} {'I FA':>7s} {'S FA':>7s} {'Z FA':>7s} | {'med h_hat|H':>11s}")
    for snr in [0.5, 1, 2, 5, 10]:
        T = 120
        cnt = {w: 0 for w in 'HISZ'}
        hh_H = []
        for t in range(T):
            for w in 'HISZ':
                y = generate(w, snr, 3.0, np.random.default_rng(7000*t+ord(w)+int(snr*11)))
                hh, dr, pv, det = monodromy_test(y, np.random.default_rng(5000*t+ord(w)))
                cnt[w] += det
                if w == 'H' and det:
                    hh_H.append(hh)
        med = np.median(hh_H) if hh_H else float('nan')
        print(f"{snr:5.1f} | {cnt['H']/T:7.2f} {cnt['I']/T:7.2f} {cnt['S']/T:7.2f} "
              f"{cnt['Z']/T:7.2f} | {med:11.3f}")
    print("\nGO iff H-det -> 1 with SNR; I/S/Z false-alarm ~0.05; recovered h_hat -> 3.000")

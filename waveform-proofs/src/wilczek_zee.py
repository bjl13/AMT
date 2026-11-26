"""
Anthology Part II, stress test B + v2 Theorem 1 (k>1).
Non-abelian Wilczek-Zee holonomy in Gr(2,4). Two loops of rank-2
projectors built from OVERLAPPING-plane generators (disjoint planes
commute and give a degenerate/abelian result — kept as a control).
"""
import numpy as np
from scipy.linalg import expm


def skew(i, j, d=4):
    G = np.zeros((d, d), dtype=complex)
    G[i, j], G[j, i] = 1.0, -1.0
    return G


def isym(i, j, d=4):
    """Anti-Hermitian generator mixing a complex direction."""
    G = np.zeros((d, d), dtype=complex)
    G[i, j] = G[j, i] = 1j
    return G


P0 = np.diag([1.0, 1.0, 0.0, 0.0]).astype(complex)


def loop_proj(t, Ga, Gb, eps=0.9):
    a = eps * np.sin(2 * np.pi * t)
    b = eps * (1 - np.cos(2 * np.pi * t))
    U = expm(a * Ga) @ expm(b * Gb)
    return U @ P0 @ U.conj().T


def kato_hol(projfun, N=4000):
    W = np.eye(4, dtype=complex)
    dt = 1.0 / N

    def pdot(t, h=1e-7):
        return (projfun(t + h) - projfun(t - h)) / (2 * h)

    for i in range(N):
        t = (i + 0.5) * dt
        P = projfun(t)
        A = pdot(t) @ P - P @ pdot(t)
        k1 = A @ W
        k2 = A @ (W + dt / 2 * k1)
        k3 = A @ (W + dt / 2 * k2)
        k4 = A @ (W + dt * k3)
        W = W + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return W


def block(W):
    E = np.eye(4)[:, :2]
    return E.T @ W @ E


if __name__ == "__main__":
    E = np.eye(4)[:, :2]
    # Non-abelian: overlapping planes (share an index), one real one complex
    WA = kato_hol(lambda t: loop_proj(t, skew(0, 2), skew(1, 2)))
    WB = kato_hol(lambda t: loop_proj(t, isym(0, 2), skew(1, 2)))
    HA, HB = block(WA), block(WB)
    print("Wilczek-Zee non-abelian holonomy, Gr(2,4)\n")
    for nm, H in [("A", HA), ("B", HB)]:
        print(f"Hol_{nm} (unitarity err {np.linalg.norm(H.conj().T@H-np.eye(2)):.1e}):")
        print(np.round(H, 4))
    comm = np.linalg.norm(HA @ HB - HB @ HA)
    print(f"\n||[Hol_A, Hol_B]|| = {comm:.6f}  => non-abelian: {comm > 0.01}")
    ph = np.angle(np.linalg.eigvals(HA)) / (2 * np.pi)
    print(f"Hol_A eigenphases/2pi = {np.round(ph,6)} (irrational => infinite order)")

    # Control: disjoint planes commute
    WA0 = kato_hol(lambda t: loop_proj(t, skew(0, 2), skew(1, 3)))
    WB0 = kato_hol(lambda t: loop_proj(t, skew(0, 3), skew(1, 2)))
    c0 = np.linalg.norm(block(WA0) @ block(WB0) - block(WB0) @ block(WA0))
    print(f"\nCONTROL (disjoint planes): ||[Hol_A,Hol_B]|| = {c0:.2e} (abelian, as expected)")

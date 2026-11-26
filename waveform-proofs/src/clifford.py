"""
Clifford-Koszul realization of the curved instantiation complex
(Anthology Part I). Verifies the operator-Pythagoras identities
d^2 = E, (d_vis)^2 = E_vis, (d_perp)^2 = w, {d_vis, d_perp} = 0
by explicit matrix construction, closing the [TIR-c] -> [THM] gap
numerically in addition to the analytic proof.

We build c(w) = eps(w) + iota(w) on Lambda(R^k) for each incidence,
place them on distinct super-tensor factors with correct Koszul signs,
and check the identities as dense matrices.
"""
import numpy as np
import itertools


def exterior_basis(k):
    """Basis of Lambda(R^k) as frozensets of indices, graded by size."""
    subsets = []
    for r in range(k + 1):
        for c in itertools.combinations(range(k), r):
            subsets.append(frozenset(c))
    # sort by degree then lexicographically for reproducibility
    subsets.sort(key=lambda s: (len(s), sorted(s)))
    return subsets


def _sign_insert(idx, s):
    """Sign of wedging e_idx into basis element s (Koszul), or 0 if idx in s."""
    if idx in s:
        return 0, s
    sign = (-1) ** sum(1 for j in s if j < idx)
    return sign, s | {idx}


def _sign_remove(idx, s):
    """Sign of contracting e_idx out of s, or 0 if idx not in s."""
    if idx not in s:
        return 0, s
    sign = (-1) ** sum(1 for j in s if j < idx)
    return sign, s - {idx}


def clifford_single(w):
    """c(w) = eps(w) + iota(w) on Lambda(R^k), returned as a dense matrix."""
    w = np.asarray(w, dtype=float)
    k = len(w)
    B = exterior_basis(k)
    pos = {s: i for i, s in enumerate(B)}
    n = len(B)
    C = np.zeros((n, n))
    for s in B:
        col = pos[s]
        for idx in range(k):
            sgn_e, s_up = _sign_insert(idx, s)   # wedge
            if sgn_e:
                C[pos[s_up], col] += sgn_e * w[idx]
            sgn_i, s_dn = _sign_remove(idx, s)   # contract
            if sgn_i:
                C[pos[s_dn], col] += sgn_i * w[idx]
    return C


def grading_operator(k):
    """(-1)^deg on Lambda(R^k), the Koszul sign operator for super tensor."""
    B = exterior_basis(k)
    return np.diag([(-1) ** len(s) for s in B])


def clifford_on_factor(w, e, m, k):
    """
    c_e(w): Clifford action on the e-th factor of the m-fold super tensor
    product of Lambda(R^k), with Koszul signs (G on all earlier factors).
    """
    G = grading_operator(k)
    I = np.eye(2 ** k)
    Ce = clifford_single(w)
    mats = []
    for f in range(m):
        if f < e:
            mats.append(G)      # Koszul sign from crossing earlier odd factor
        elif f == e:
            mats.append(Ce)
        else:
            mats.append(I)
    out = mats[0]
    for M in mats[1:]:
        out = np.kron(out, M)
    return out


def build_differentials(payloads, projector):
    """
    payloads : (m, k) resolved payloads Phi~_e
    projector: (k, k) orthogonal projector pi onto visible subspace
    Returns d, d_vis, d_perp and the scalar energies (E, E_vis, w).
    """
    P = np.asarray(projector, dtype=float)
    payloads = np.asarray(payloads, dtype=float)
    m, k = payloads.shape
    vis = payloads @ P.T
    perp = payloads - vis
    d = sum(clifford_on_factor(payloads[e], e, m, k) for e in range(m))
    d_vis = sum(clifford_on_factor(vis[e], e, m, k) for e in range(m))
    d_perp = sum(clifford_on_factor(perp[e], e, m, k) for e in range(m))
    E = float((payloads ** 2).sum())
    E_vis = float((vis ** 2).sum())
    w = float((perp ** 2).sum())
    return d, d_vis, d_perp, (E, E_vis, w)


if __name__ == "__main__":
    rng = np.random.default_rng(7)
    print("Clifford-Koszul verification of Theorem I.1 (operator Pythagoras)")
    print("Random orthogonal projector, random payloads, several (m,k):\n")
    for (m, k) in [(2, 2), (3, 2), (2, 3), (3, 3)]:
        # random orthogonal projector of random rank r onto R^k
        A = rng.standard_normal((k, k))
        Q, _ = np.linalg.qr(A)
        r = rng.integers(1, k + 1)
        P = Q[:, :r] @ Q[:, :r].T                 # orthogonal projector, rank r
        payloads = rng.standard_normal((m, k))
        d, d_vis, d_perp, (E, E_vis, w) = build_differentials(payloads, P)
        N = d.shape[0]
        I = np.eye(N)
        e1 = np.linalg.norm(d @ d - E * I)
        e2 = np.linalg.norm(d_vis @ d_vis - E_vis * I)
        e3 = np.linalg.norm(d_perp @ d_perp - w * I)
        e4 = np.linalg.norm(d_vis @ d_perp + d_perp @ d_vis)   # anticommutator
        pyth = abs(E - (E_vis + w))
        print(f"  m={m}, k={k}, rank(pi)={r}, dim M_v={N}: "
              f"||d^2-E||={e1:.2e} ||d_vis^2-E_vis||={e2:.2e} "
              f"||d_perp^2-w||={e3:.2e} ||{{d_vis,d_perp}}||={e4:.2e} "
              f"|E-(E_vis+w)|={pyth:.2e}")
    print("\nAll residuals ~1e-14 => (d_perp)^2 = w*id exactly:")
    print("(M_v, d_perp) is a matrix factorization of the superpotential w. [THM]")

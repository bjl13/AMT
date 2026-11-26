"""
Anthology Part II.3 + stress test C.
Mobius (twisted n-cycle) sheaf Laplacian spectrum over R, and integral
cohomology H^1(S^1; Z_-) = Z/2 via Smith normal form over Z.
"""
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form


def twisted_coboundary(n):
    """n-cycle with identity edge maps except one -1 (the Mobius twist)."""
    D = np.zeros((n, n))
    for j in range(n):
        rho = -1.0 if j == n - 1 else 1.0
        D[j, (j + 1) % n] = rho
        D[j, j] += -1.0
    return D


if __name__ == "__main__":
    print("Mobius twisted sheaf Laplacian L = D^T D over R\n")
    print(f"{'n':>3s} {'max|spec-pred|':>16s} {'gap':>10s} {'gap_pred':>10s} "
          f"{'rank(D)':>8s} {'acyclic/R':>10s}")
    for n in [5, 8, 12]:
        D = twisted_coboundary(n)
        ev = np.sort(np.linalg.eigvalsh(D.T @ D))
        pred = np.sort([2 - 2 * np.cos((2 * j + 1) * np.pi / n) for j in range(n)])
        gap_pred = 2 - 2 * np.cos(np.pi / n)
        rk = np.linalg.matrix_rank(D)
        print(f"{n:3d} {np.max(np.abs(ev-pred)):16.2e} {ev[0]:10.6f} "
              f"{gap_pred:10.6f} {rk:8d} {str(rk==n):>10s}")
    print("\nH^1 over R = 0 (acyclic) but conditioning ~ 1/gap ~ n^2/pi^2 "
          "diverges => 'soft obstruction'\n")
    print("Integral cohomology via Smith normal form over Z:")
    for n in [3, 5, 8]:
        D = sp.Matrix(twisted_coboundary(n).astype(int))
        S = smith_normal_form(D, domain=sp.ZZ)
        diag = [int(S[i, i]) for i in range(n)]
        print(f"  n={n}: Smith diag = {diag}  =>  H^1(S^1; Z_-) = Z/{abs(diag[-1])}")

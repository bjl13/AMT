"""
Anthology Part II.3 + stress test D.
Cover-resolution table for k_perp = 1. Growth pulls back along the n-fold
cover: monodromy phi -> phi^n, defect C -> C_n = (sum_{j<n} phi^j) C.
Shows the spectral-arithmetic dichotomy:
  full resonance (alpha=0): C_n = nC, never resolved by growth;
  rational alpha:  geometric-series kill at the order;
  irrational alpha (genuine helix): never killed by any finite cover.
"""
import numpy as np

GOLDEN = (1 + 5 ** 0.5) / 2
CASES = {
    "alpha=0 (full resonance)": 1.0 + 0j,
    "alpha=2pi/3 (rational)": np.exp(2j * np.pi / 3),
    "alpha=2pi/golden (irrational)": np.exp(2j * np.pi / GOLDEN),
}


if __name__ == "__main__":
    C = 1.0 + 0.5j
    print(f"Cover-resolution table, defect C = {C}\n")
    print(f"{'case':32s} {'n':>2s} {'|C_n|':>10s} {'solvable':>9s} {'invariants':>11s}")
    for name, phi in CASES.items():
        for n in [1, 2, 3, 6]:
            Cn = sum(phi ** j for j in range(n)) * C
            mono = phi ** n
            resonant = abs(mono - 1) < 1e-9
            solvable = (not resonant) or (abs(Cn) < 1e-9)
            print(f"{name:32s} {n:2d} {abs(Cn):10.4f} {str(solvable):>9s} "
                  f"{str(resonant):>11s}")
        print()

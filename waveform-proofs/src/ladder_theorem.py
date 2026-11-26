"""
The comparator ladder = the lower central series of the holonomy group.

Claim to demonstrate structurally (exact integer arithmetic, no noise):
  Depth-k iterated-commutator observable vanishes for every holonomy group of
  nilpotency class < k, and is generically nonzero at class >= k. Hence the
  hypothesis classes H_k = {holonomy nilpotent of class <= k} form a STRICT
  ascending filtration, and the depth-(k+1) observable is the invariant that
  separates H_{k+1} from H_k.

  H0 static (trivial, class 0)      -> projection      (depth 0)
  H1 abelian (class <= 1)           -> winding         (depth 1, single loop)
  H2 non-abelian (class <= 2)       -> ordering        (depth 2, [A,B])
  H3 nested ordering (class <= 3)   -> nested ordering  (depth 3, [[A,B],A])

  H_k names the hypothesis class (class <= k). The H_k detector is the depth-k
  observable: it rejects H_{k-1}, so a positive result certifies class >= k
  (a lower bound), not membership in H_k. The witnesses below are exactly
  class k, i.e. in H_k minus H_{k-1}.

Readout = full holonomy in GL(V). The vanishing direction is the homomorphism
identity rho(gamma_k(G)) = gamma_k(rho(G)); dimension is irrelevant, which is
exactly why no higher-dimensional abelian representation can reproduce a nonzero
depth-2 observable. We use exact unipotent (unitriangular) matrices so the group
commutators are exact.
"""
import numpy as np

def E(i, j, n):
    M = np.zeros((n, n), dtype=np.int64); M[i, j] = 1; return M

def inv_unipotent(M):
    n = M.shape[0]; N = M - np.eye(n, dtype=np.int64)
    out = np.eye(n, dtype=np.int64); term = np.eye(n, dtype=np.int64)
    for _ in range(n):                       # Neumann series terminates (N nilpotent)
        term = -term @ N
        if not term.any(): break
        out = out + term
    return out

def comm(A, B):                              # group commutator A B A^-1 B^-1
    return A @ B @ inv_unipotent(A) @ inv_unipotent(B)

def dev(M):                                  # ||M - I||, 0 iff trivial
    return int(np.abs(M - np.eye(M.shape[0], dtype=np.int64)).sum())

# ---- worlds at increasing nilpotency class -------------------------------
I3 = np.eye(3, dtype=np.int64); I4 = np.eye(4, dtype=np.int64)

# H1 witness, abelian (class 1): two commuting unipotents
A1, B1 = I3 + E(0,1,3), I3 + 2*E(0,1,3)

# H2 witness, non-abelian class 2 (Heisenberg 3x3): [A,B] central, [[A,B],A] = I
A2, B2 = I3 + E(0,1,3), I3 + E(1,2,3)

# H3 witness, class 3 (4x4 unitriangular): [[A,B],A] != I, quadruple bracket = I
A3, B3 = I4 + E(0,1,4) + E(2,3,4), I4 + E(1,2,4)

def report(name, A, B):
    c2 = comm(A, B)
    c3 = comm(c2, A)
    c4 = comm(c3, A)
    print(f"{name:36s}  depth2 |[A,B]-I|={dev(c2):3d}   "
          f"depth3 |[[A,B],A]-I|={dev(c3):3d}   depth4={dev(c4):3d}")
    return dev(c2), dev(c3), dev(c4)

print("Exact iterated-commutator observables (unipotent holonomy in GL(V)):\n")
r1 = report("H1 witness: abelian (class 1)", A1, B1)
r2 = report("H2 witness: Heisenberg (class 2)", A2, B2)
r3 = report("H3 witness: unitriangular (class 3)", A3, B3)

print("\nFiltration read-off:")
print(f"  depth-2 separates H1 from H2 : abelian={r1[0]} (=0), class2={r2[0]} (>0)  -> {r1[0]==0 and r2[0]>0}")
print(f"  depth-3 separates H2 from H3 : class2={r2[1]} (=0), class3={r3[1]} (>0)  -> {r2[1]==0 and r3[1]>0}")
print(f"  depth-4 vanishes at class 3  : class3 depth4={r3[2]} (=0)                 -> {r3[2]==0}")

# ---- the homomorphism fact, checked in a nontrivial representation -------
print("\nHomomorphism check: an ABELIAN group has vanishing depth-2 in ANY dimension.")
rng = np.random.default_rng(0)
for dimn in [2, 5, 12, 40]:
    # random commuting pair: exp of two random matrices sharing an eigenbasis
    Q, _ = np.linalg.qr(rng.standard_normal((dimn, dimn)) + 1j*rng.standard_normal((dimn, dimn)))
    dA = np.exp(1j*rng.uniform(0, 2*np.pi, dimn)); dB = np.exp(1j*rng.uniform(0, 2*np.pi, dimn))
    UA = Q @ np.diag(dA) @ Q.conj().T          # commute: same eigenbasis Q
    UB = Q @ np.diag(dB) @ Q.conj().T
    cc = UA @ UB @ np.linalg.inv(UA) @ np.linalg.inv(UB)
    print(f"  dim={dimn:2d}:  ||[UA,UB]-I|| = {np.linalg.norm(cc - np.eye(dimn)):.2e}  "
          f"(abelian => depth-2 observable = 0, regardless of dimension)")

print("\n=> No abelian holonomy reproduces the depth-2 (ordering) observable in the")
print("   full-frame readout, in ANY representation dimension. The comparator escape")
print("   'use a bigger abelian model' is closed by rho preserving commutators.")

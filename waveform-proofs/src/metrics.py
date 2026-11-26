"""
Core waveform metrics — shared by every proof script.

Node model: a node v under frame O sees m_v visible incidence payloads
phi_i in R^k (or C^k). Derived scalars per v2 spec section 1.5.
All functions are pure; no global state.
"""
import numpy as np


def node_metrics(phis, ambient_energy=None):
    """
    phis : (m, k) array of visible payloads at a node.
    ambient_energy : optional scalar sum_e ||Phi~_e||^2 (full ambient energy)
                     used for the exact D_O; if None, D_O is not computed.

    Returns dict with gross_mass, net_resultant, tension, coherence (signed,
    unclamped), incidence_count, and D_O (None unless ambient_energy given).
    Conventions: drop zero-norm payloads; coherence None at m<2; D_O:=0 on
    zero ambient energy.
    """
    phis = np.asarray(phis, dtype=float)
    norms = np.linalg.norm(phis, axis=1)
    keep = norms > 1e-12
    phis, norms = phis[keep], norms[keep]
    m = len(phis)
    gross = float(norms.sum())
    net = float(np.linalg.norm(phis.sum(axis=0))) if m else 0.0
    tension = gross - net
    if m >= 2:
        # mean signed pairwise cosine via Gram identity:
        # sum_{i<j} u_i . u_j = (||sum u||^2 - m) / 2
        U = phis / norms[:, None]
        gram_off = (float(np.linalg.norm(U.sum(axis=0)) ** 2) - m) / 2.0
        coherence = gram_off / (m * (m - 1) / 2.0)
    else:
        coherence = None
    D_O = None
    if ambient_energy is not None:
        vis_energy = float((phis ** 2).sum())
        D_O = 0.0 if ambient_energy <= 0 else 1.0 - vis_energy / ambient_energy
    return dict(gross_mass=gross, net_resultant=net, tension=tension,
                coherence=coherence, incidence_count=m, D_O=D_O)


def pairwise_cosines(phis):
    """All signed pairwise cosines, with the (i,j) index list."""
    phis = np.asarray(phis, dtype=float)
    norms = np.linalg.norm(phis, axis=1)
    keep = norms > 1e-12
    phis = phis[keep] / norms[keep][:, None]
    m = len(phis)
    idx = [(i, j) for i in range(m) for j in range(i + 1, m)]
    cos = np.array([float(phis[i] @ phis[j]) for i, j in idx])
    return cos, idx


def curvature_payload(Phi_tilde, projector):
    """m0 = (I - pi) Phi~  — the invisible component (v2 Prop 4 / anthology I.0)."""
    P = np.asarray(projector, dtype=float)
    x = np.asarray(Phi_tilde, dtype=float)
    return x - P @ x

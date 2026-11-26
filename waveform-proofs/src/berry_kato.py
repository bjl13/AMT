"""
Anthology Part II, stress test A + v2 Theorem 1 (k=1).
Kato parallel transport  W' = [pi_dot, pi] W  around latitude loops on
Gr(1,2) = S^2; holonomy phase vs analytic Berry phase -pi(1-cos theta).
"""
import numpy as np

SX = np.array([[0, 1], [1, 0]], dtype=complex)
SY = np.array([[0, -1j], [1j, 0]])
SZ = np.array([[1, 0], [0, -1]], dtype=complex)


def proj(theta, phi):
    n = np.array([np.sin(theta) * np.cos(phi),
                  np.sin(theta) * np.sin(phi),
                  np.cos(theta)])
    return 0.5 * (np.eye(2) + n[0] * SX + n[1] * SY + n[2] * SZ)


def kato_holonomy(theta, N=4000):
    dt = 1.0 / N

    def pdot(t, h=1e-7):
        return (proj(theta, 2 * np.pi * (t + h)) -
                proj(theta, 2 * np.pi * (t - h))) / (2 * h)

    W = np.eye(2, dtype=complex)
    for i in range(N):
        t = (i + 0.5) * dt
        P = proj(theta, 2 * np.pi * t)
        A = pdot(t) @ P - P @ pdot(t)              # [pi_dot, pi]
        k1 = A @ W
        k2 = A @ (W + dt / 2 * k1)
        k3 = A @ (W + dt / 2 * k2)
        k4 = A @ (W + dt * k3)
        W = W + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
    return W


if __name__ == "__main__":
    print("Berry phase via Kato transport on Gr(1,2)=S^2 (RK4, N=4000)\n")
    print(f"{'theta':>8s} {'|hol|':>10s} {'gamma_num':>12s} {'gamma_analytic':>14s} {'err':>10s}")
    for theta in [np.pi / 3, np.pi / 2, 2 * np.pi / 3]:
        W = kato_holonomy(theta)
        P0 = proj(theta, 0.0)
        ev, evec = np.linalg.eigh(P0)
        psi0 = evec[:, np.argmax(ev)]
        hol = np.vdot(psi0, W @ psi0)
        g_num = np.angle(hol)
        g_ana = -np.pi * (1 - np.cos(theta))
        g_ana = (g_ana + np.pi) % (2 * np.pi) - np.pi
        print(f"{theta:8.4f} {abs(hol):10.8f} {g_num:+12.6f} {g_ana:+14.6f} "
              f"{abs(g_num - g_ana):10.2e}")

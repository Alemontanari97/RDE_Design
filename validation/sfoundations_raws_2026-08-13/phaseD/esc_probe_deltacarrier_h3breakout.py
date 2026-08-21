# esc_probe_deltacarrier_h3breakout.py
# S-FOUNDATIONS-C4 escalation round 1, minor (c) DELTA-CARRIER, 2026-08-20.
# Executable counter-state for MIN-DELTACARRIER-3 (SUSTAINED) + rejector
# for the DC-1 pointwise CLAIM sup G = p(lambda) on the ADMISSIBLE set.
#
# Two-sided rejector (both halves can FAIL):
#  [A] DC-1 CLAIM half: on the (H3)-admissible set {(q,u): q in
#      (c*, q_max), u in [c(q), q]} the grid-sup of
#      G(q,u) = rho(q) u^2 - lambda rho(q) u + p(q) must NOT exceed
#      p(lambda) (tolerance = derived float slack, see below), and the
#      aligned state (lambda, lambda) must attain it exactly.
#      If the grid-sup exceeds p(lambda) + tol_A, DC-1 step (ii) is DEAD.
#  [B] H3-BREAKOUT half (the refuter's analytic counter-state, verified
#      here numerically): drop (H3), take q in (c*, lambda) with
#      u -> 0+; then G -> p(q) > p(lambda). If G at the breakout state
#      does NOT exceed p(lambda), the hypothesis list is not
#      load-bearing as claimed and the W_cert repair (ESC-r1-3) is
#      unfounded -> probe FAILS.
#
# Model: frozen thermally-perfect reduces to ideal gas along one
# isentrope leaf; gamma = 1.4, cp = 1, h0 = 1, stagnation p_t = 1
# (nondimensional; no number of record is produced -- PASS/FAIL only).
# Pinned-env deps: numpy only.
#
# Tolerances (derived, not magic) [ESC-r2-4 re-derivation, per
# ESC-DELTACARRIER-r1-4: the prior scale p(lambda) was WRONG -- near
# the maximizer (lambda, lambda) the chain computes rho*lam^2 and
# -lam*rho*lam, each ~18x larger than p(lambda), and their cancellation
# sets the absolute rounding noise; the correct budget scale is the
# largest intermediate term, not the result]: slack =
# 64 * eps * max(rho(lambda)*lambda^2, p(lambda)) covers the ~10-flop
# evaluation chain of G and p (each op |rel err| <= eps at its own
# magnitude, chain <= ~10 eps * max-term; 64 is the next power of two
# above with margin factor ~6). The breakout margin is REQUIRED to be
# macroscopic: p(q_mid) - p(lambda) at q_mid = (c* + lambda)/2 is
# O(1) in these units, so we demand exceedance > 1e3 * tol_A (scale
# separation, not a tuned constant; still ~8 orders below the
# breakout exceedance after the rescale).

import numpy as np

GAMMA = 1.4
H0 = 1.0
CP = 1.0  # h = cp*T = T


def state(q):
    """Isentrope leaf: h = h0 - q^2/2; returns (p, rho, c)."""
    h = H0 - 0.5 * q * q
    T = h / CP
    p = (h / H0) ** (GAMMA / (GAMMA - 1.0))
    R = (GAMMA - 1.0) / GAMMA * CP
    rho = p / (R * T)
    c = np.sqrt((GAMMA - 1.0) * h)
    return p, rho, c


def G(q, u, lam):
    p, rho, _ = state(q)
    return rho * u * u - lam * rho * u + p


def main():
    eps = np.finfo(float).eps
    q_star = np.sqrt(2.0 * (GAMMA - 1.0) * H0 / (GAMMA + 1.0))  # sonic
    q_max = np.sqrt(2.0 * H0)
    lam = 1.2  # supersonic multiplier: check
    p_lam, rho_lam, c_lam = state(lam)
    assert lam > c_lam, "lambda not supersonic -- probe misconfigured"
    # (H5b) sanity: gamma_s = rho c^2 / p = gamma >= 1 on the leaf
    gs = rho_lam * c_lam ** 2 / p_lam
    assert abs(gs - GAMMA) < 1e-12, "gamma_s != gamma on ideal leaf"

    # [ESC-r2-4] budget scale = largest intermediate of the G chain at
    # the maximizer (rho*lam^2 ~ 18x p_lam), not the cancelled result.
    tol_A = 64.0 * eps * max(rho_lam * lam * lam, p_lam)

    # --- [A] admissible-set half ---
    qs = np.linspace(q_star * (1 + 1e-9), q_max * (1 - 1e-9), 4001)
    sup_G = -np.inf
    for q in qs:
        _, _, c = state(q)
        if q <= c:
            continue  # not on the strict supersonic branch
        us = np.linspace(c, q, 401)  # u in [c(q), q] (H3 closure)
        g = G(q, us, lam)
        m = g.max()
        if m > sup_G:
            sup_G = m
    g_aligned = G(lam, lam, lam)
    ok_A_sup = sup_G <= p_lam + tol_A
    ok_A_attain = abs(g_aligned - p_lam) <= tol_A
    print(f"[A] grid-sup G = {sup_G:.16e}  vs p(lambda) = {p_lam:.16e}"
          f"  (sup - p_lam = {sup_G - p_lam:+.3e}, tol_A = {tol_A:.3e})")
    print(f"[A] G(lambda,lambda) - p(lambda) = {g_aligned - p_lam:+.3e}")

    # --- [B] H3-breakout half ---
    q_mid = 0.5 * (q_star + lam)  # in (c*, lambda)
    p_mid, _, c_mid = state(q_mid)
    assert q_mid < lam and q_mid > q_star
    u_small = 1e-6  # u -> 0+ : violates (H3) (u < c(q_mid) grossly)
    assert u_small < c_mid
    g_break = G(q_mid, u_small, lam)
    exceed = g_break - p_lam
    ok_B = exceed > 1e3 * tol_A
    print(f"[B] breakout q = {q_mid:.6f} (in (c*, lambda)), u = {u_small:.1e}")
    print(f"[B] G(breakout) - p(lambda) = {exceed:+.6e}"
          f"  (required > {1e3 * tol_A:.3e})")

    verdict = ok_A_sup and ok_A_attain and ok_B
    print("[A] admissible-set bound holds:", ok_A_sup,
          "| aligned attainment exact:", ok_A_attain)
    print("[B] H3-off breakout exceeds ceiling:", ok_B)
    print("PROBE VERDICT:", "PASS" if verdict else "FAIL")
    raise SystemExit(0 if verdict else 1)


if __name__ == "__main__":
    main()

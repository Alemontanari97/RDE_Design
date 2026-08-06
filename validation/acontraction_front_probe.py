#!/usr/bin/env python3
"""a-contraction front probe [RIGOR/A, S16 tranche 2, T2]: sampling
probe (NOT a certificate — declared) of the front obstruction of the
a-contraction / shifted-relative-entropy method (Vasseur-Krupa line)
transplanted to the x-as-time steady BVP frame
(docs/rde_nozzle_acontraction_attack.md; registry [X-ACFR]).

STRUCTURE UNDER TEST (derived self-containedly in the attack doc §3).
Reference = certified S1 front (upstream V_-, downstream V_+, slope
sigma'); competitor = weak entropy solution confined to the certified
convexity box; weight a(y) = a_- upstream / a_+ downstream of the
shifted interface Y(x); entropy pair (eta, q) = (-rho u s, -rho v s),
s = ln(p rho^-gamma), convex in the x-flux m on the certified (M, V)
box (X-IVXC + T-XRED of record). The shift Y' absorbs the front term
EXCEPT on the balance set

    B_r = { u in box : eta_rel(u; V_+) = r * eta_rel(u; V_-) },
    r = a_- / a_+  > 0,

where contraction REQUIRES

    psi_r(u) := q_rel(u; V_+) - r * q_rel(u; V_-)  >=  0   on B_r.

The probe scans r over a log grid, samples B_r inside the box
(bisection in the box-convex parameter coordinates (rho, p, M, V)),
and reports min psi_r / scale. FEASIBLE = some r with min psi_r > 0
above the derived floor. This is a NECESSARY-condition scan of the
known crux (the front term); interior/wall/data bookkeeping is the
doc's §4 (walls are FREE by T-XWALL).

Checks:
  (P0) entropy-pair compatibility dq/dU == Deta(U) . dgy/dU at random
       states (the pair (eta, q) is a genuine entropy pair of the
       x-as-time system) — derived floor.
  (P1) eta_rel > 0 at all in-box samples wrt BOTH V_- and V_+
       (convexity cross-check against the X-IVXC certificate).
  (P2) oracle RH sanity (front states connect; reversed pair too).
  (P3) THE SCAN (verdict payload): r-grid feasibility of psi_r >= 0
       on sampled B_r for the LAX front.
  REJECTORS:
  (R1) DISCRIMINATION: the REVERSED front (V_+ upstream, V_- down-
       stream = entropy-violating expansion shock) must be INFEASIBLE
       for every r — a probe that "certifies" the reversed shock is
       broken.
  (R2) the Deta-correction term must be LIVE: corrupting q_rel to the
       naive difference q(u) - q(ubar) must change the landscape
       beyond the derived floor at fixed seed.

Deterministic: fixed seed, no wall-clock, no magic tolerances (floors
derived from machine eps and printed scales).
"""
import math
import sys

import numpy as np

EPS = sys.float_info.epsilon
GAM = 1.4
SEED = 20260806


# ------------------------------------------------------------ states
def prim_from_box(x):
    """x = (..., 4) box coords (rho, p, M, V) -> primitive (rho,u,v,p)."""
    rho, p, M, V = x[..., 0], x[..., 1], x[..., 2], x[..., 3]
    c = np.sqrt(GAM * p / rho)
    return np.stack([rho, M * c, V * c, p], axis=-1)


def s_of(U):
    rho, p = U[..., 0], U[..., 3]
    return np.log(p * rho ** (-GAM))


def eta_of(U):
    return -U[..., 0] * U[..., 1] * s_of(U)


def q_of(U):
    return -U[..., 0] * U[..., 2] * s_of(U)


def m_of(U):
    rho, u, v, p = (U[..., i] for i in range(4))
    q2 = u * u + v * v
    rH = GAM * p / (GAM - 1.0) + 0.5 * rho * q2
    return np.stack([rho * u, rho * u * u + p, rho * u * v, u * rH],
                    axis=-1)


def gy_of(U):
    rho, u, v, p = (U[..., i] for i in range(4))
    q2 = u * u + v * v
    rH = GAM * p / (GAM - 1.0) + 0.5 * rho * q2
    return np.stack([rho * v, rho * u * v, rho * v * v + p, v * rH],
                    axis=-1)


def dm_dU(U):
    rho, u, v, p = U
    q2 = u * u + v * v
    rH = GAM * p / (GAM - 1.0) + 0.5 * rho * q2
    return np.array([
        [u, rho, 0.0, 0.0],
        [u * u, 2 * rho * u, 0.0, 1.0],
        [u * v, rho * v, rho * u, 0.0],
        [u * 0.5 * q2, rH + rho * u * u, rho * u * v,
         GAM * u / (GAM - 1.0)]])


def dgy_dU(U):
    rho, u, v, p = U
    q2 = u * u + v * v
    rH = GAM * p / (GAM - 1.0) + 0.5 * rho * q2
    return np.array([
        [v, 0.0, rho, 0.0],
        [u * v, rho * v, rho * u, 0.0],
        [v * v, 0.0, 2 * rho * v, 1.0],
        [v * 0.5 * q2, rho * u * v, rH + rho * v * v,
         GAM * v / (GAM - 1.0)]])


def deta_dU(U):
    rho, u, v, p = U
    s = math.log(p * rho ** (-GAM))
    return np.array([-u * s + GAM * u, -rho * s, 0.0, -rho * u / p])


def dq_dU(U):
    rho, u, v, p = U
    s = math.log(p * rho ** (-GAM))
    return np.array([-v * s + GAM * v, 0.0, -rho * s, -rho * v / p])


def Deta(Ubar):
    """Gradient of eta wrt the x-flux m at Ubar (row vector)."""
    return np.linalg.solve(dm_dU(Ubar).T, deta_dU(Ubar))


def rel_pair(U, Ubar):
    """(eta_rel, q_rel)(U; Ubar), vectorized over leading axes of U."""
    D = Deta(Ubar)
    e = eta_of(U) - eta_of(Ubar[None])[0] - (m_of(U)
        - m_of(Ubar[None])[0]) @ D
    q = q_of(U) - q_of(Ubar[None])[0] - (gy_of(U)
        - gy_of(Ubar[None])[0]) @ D
    return e, q


# ------------------------------------------------------------ oracle
def oblique_pair():
    beta = math.radians(40.0)
    rho1, p1 = 1.2, 1.0e5
    c1 = math.sqrt(GAM * p1 / rho1)
    V1 = np.array([rho1, 2.5 * c1, 0.0, p1])
    n = np.array([math.sin(beta), -math.cos(beta)])
    t = np.array([math.cos(beta), math.sin(beta)])
    un1, ut1 = V1[1:3] @ n, V1[1:3] @ t
    Mn1 = abs(un1) / c1
    p2 = p1 * (1.0 + 2.0 * GAM / (GAM + 1.0) * (Mn1**2 - 1.0))
    r2 = rho1 * ((GAM + 1.0) * Mn1**2) / ((GAM - 1.0) * Mn1**2 + 2.0)
    q2 = (un1 * rho1 / r2) * n + ut1 * t
    V2 = np.array([r2, q2[0], q2[1], p2])
    return V1, V2, math.tan(beta)


def rh_residual(Vm, Vp, sig):
    ss = 1.0 / math.sqrt(1.0 + sig * sig)

    def parts(V):
        rho, u, v, p = V
        un = (sig * u - v) * ss
        ut = (u + sig * v) * ss
        h = GAM / (GAM - 1.0) * p / rho
        return np.array([rho * un, p + rho * un**2, ut,
                         h + 0.5 * (un**2 + ut**2)])
    return parts(Vp) - parts(Vm)


# ------------------------------------------------------------ the scan
def box_coords_of(U):
    rho, u, v, p = U
    c = math.sqrt(GAM * p / rho)
    return np.array([rho, p, u / c, v / c])


def make_box(Vm, Vp):
    """Sampling box in (rho, p, M, V): the X-IVXC certified (M, V) box
    [1.15, 3] x [-0.8, 0.8] (record: convexity certified there for
    every (rho, S) via T-XRED), rho/p ranges = the pair's min/max
    padded by the DERIVED factor 1.3 (covers both states; probe
    scope, declared)."""
    bm, bp = box_coords_of(Vm), box_coords_of(Vp)
    lo = np.array([min(bm[0], bp[0]) / 1.3, min(bm[1], bp[1]) / 1.3,
                   1.15, -0.8])
    hi = np.array([max(bm[0], bp[0]) * 1.3, max(bm[1], bp[1]) * 1.3,
                   3.0, 0.8])
    return lo, hi


def balance_scan(Vm, Vp, r_grid, n_samples, rng, corrupt_q=False):
    """For each r: sample the balance set B_r in the box, return
    min psi_r (scaled) and the balance-sample count."""
    lo, hi = make_box(Vm, Vp)
    X = lo + (hi - lo) * rng.random((n_samples, 4))
    U = prim_from_box(X)
    em, qm = rel_pair(U, Vm)
    ep, qp = rel_pair(U, Vp)
    if corrupt_q:
        qm = q_of(U) - q_of(Vm[None])[0]
        qp = q_of(U) - q_of(Vp[None])[0]
    qscale = max(np.percentile(np.abs(qm), 95),
                 np.percentile(np.abs(qp), 95))
    out = []
    for r in r_grid:
        phi = ep - r * em
        pos, neg = np.where(phi > 0)[0], np.where(phi < 0)[0]
        npairs = min(pos.size, neg.size, 1500)
        if npairs < 50:
            out.append((r, np.nan, 0, qscale))
            continue
        A = X[rng.choice(pos, npairs, replace=False)]
        B = X[rng.choice(neg, npairs, replace=False)]
        for _ in range(60):                      # bisection in box coords
            Mid = 0.5 * (A + B)
            Um = prim_from_box(Mid)
            e1, _ = rel_pair(Um, Vm)
            e2, _ = rel_pair(Um, Vp)
            if corrupt_q:
                pass                              # phi unchanged by R2
            phim = e2 - r * e1
            takeA = phim > 0
            A[takeA] = Mid[takeA]
            B[~takeA] = Mid[~takeA]
        Ub = prim_from_box(0.5 * (A + B))
        e1, q1 = rel_pair(Ub, Vm)
        e2, q2 = rel_pair(Ub, Vp)
        if corrupt_q:
            q1 = q_of(Ub) - q_of(Vm[None])[0]
            q2 = q_of(Ub) - q_of(Vp[None])[0]
        psi = q2 - r * q1
        out.append((r, float(np.min(psi)) / qscale, npairs, qscale))
    return out


def main():
    print('== a-contraction front probe (X-ACFR) — PROBE, not a '
          'certificate ==')
    ok = True
    rng = np.random.default_rng(SEED)
    Vm, Vp, sig = oblique_pair()

    # P0: entropy-pair compatibility at random states
    lo, hi = make_box(Vm, Vp)
    Xs = lo + (hi - lo) * rng.random((20, 4))
    worst = 0.0
    for x in Xs:
        U = prim_from_box(x)
        lhs = dq_dU(U)
        rhs = Deta(U) @ dgy_dU(U)
        scale = np.max(np.abs(lhs)) + np.max(np.abs(rhs))
        worst = max(worst, float(np.max(np.abs(lhs - rhs)) / scale))
    good = worst < 1e3 * EPS
    print('  (P0) pair compatibility dq/dU == Deta.dgy/dU: worst rel '
          '%.2e: %s' % (worst, 'PASS' if good else 'FAIL'))
    ok &= good

    # P1: eta_rel > 0 in-box (convexity cross-check vs X-IVXC)
    Xs = lo + (hi - lo) * rng.random((20000, 4))
    U = prim_from_box(Xs)
    em, _ = rel_pair(U, Vm)
    ep, _ = rel_pair(U, Vp)
    escale = max(float(np.percentile(em, 95)),
                 float(np.percentile(ep, 95)))
    floor_e = 1e3 * EPS * escale
    dm = float(np.min(em[np.linalg.norm(U - Vm, axis=1) > 1e-6 *
                          np.linalg.norm(Vm)]))
    dp = float(np.min(ep[np.linalg.norm(U - Vp, axis=1) > 1e-6 *
                          np.linalg.norm(Vp)]))
    good = dm > -floor_e and dp > -floor_e
    print('  (P1) eta_rel >= 0 in-box (20000 samples): min %.3e / %.3e '
          '(floor -%.1e): %s'
          % (dm / escale, dp / escale, floor_e / escale,
             'PASS' if good else 'FAIL'))
    ok &= good

    # P2: RH sanity for the Lax pair (and reversed labels reuse it)
    rres = rh_residual(Vm, Vp, sig)
    scaleH = np.array([Vm[0] * abs(Vm[1]), Vm[3], abs(Vm[1]),
                       GAM / (GAM - 1.0) * Vm[3] / Vm[0]])
    good = bool(np.all(np.abs(rres) <= 1e3 * EPS * scaleH))
    print('  (P2) oracle RH residual == 0:                    %s'
          % ('PASS' if good else 'FAIL'))
    ok &= good

    # P3: the scan (Lax orientation: V_- upstream, V_+ downstream)
    r_grid = np.logspace(-2.0, 2.0, 25)
    res = balance_scan(Vm, Vp, r_grid, 40000, np.random.default_rng(SEED))
    feas = [(r, m) for r, m, n, _ in res if n >= 50 and np.isfinite(m)]
    floor_psi = 1e3 * EPS  # on the SCALED psi
    best = max(feas, key=lambda t: t[1]) if feas else (np.nan, -np.inf)
    feasible = [(r, m) for r, m in feas if m > floor_psi]
    print('  (P3) LAX FRONT r-scan (%d r-values with balance samples):'
          % len(feas))
    for r, m in feas[::4]:
        print('        r = %8.3f   min psi/scale = %+.4e' % (r, m))
    print('        best: r = %.3f, min psi/scale = %+.4e; feasible '
          'r-count: %d' % (best[0], best[1], len(feasible)))
    verdict_lax_feasible = len(feasible) > 0
    print('  (P3) VERDICT PAYLOAD: front condition at the oracle: %s'
          % ('FEASIBLE (r-window found)' if verdict_lax_feasible
             else 'INFEASIBLE (no r passes — honest negative)'))

    # R1: reversed (entropy-violating) front must be infeasible
    res_rev = balance_scan(Vp, Vm, r_grid, 40000,
                           np.random.default_rng(SEED))
    feas_rev = [(r, m) for r, m, n, _ in res_rev
                if n >= 50 and np.isfinite(m) and m > floor_psi]
    good = len(feas_rev) == 0
    print('  [R1] REVERSED front infeasible for every r:      %s '
          '(feasible count %d)' % ('PASS' if good else 'FAIL',
                                   len(feas_rev)))
    ok &= good

    # R2: the Deta correction must be live (corrupted landscape differs)
    res_bad = balance_scan(Vm, Vp, r_grid, 40000,
                           np.random.default_rng(SEED), corrupt_q=True)
    diffs = [abs(m1 - m2) for (_, m1, n1, _), (_, m2, n2, _)
             in zip(res, res_bad)
             if n1 >= 50 and n2 >= 50 and np.isfinite(m1)
             and np.isfinite(m2)]
    good = len(diffs) > 0 and max(diffs) > 1e3 * EPS
    print('  [R2] Deta-correction term LIVE (landscape shift %.2e): %s'
          % (max(diffs) if diffs else 0.0, 'PASS' if good else 'FAIL'))
    ok &= good

    # The probe PASSES iff its checks and rejectors pass; the P3
    # verdict payload (feasible vs infeasible) is REPORTED, not gated:
    # both outcomes are honest science (attack doc adjudicates).
    print('VERDICT: %s' % ('PASS' if ok else 'FAIL'))
    print('PAYLOAD: LAX-FRONT %s'
          % ('FEASIBLE' if verdict_lax_feasible else 'INFEASIBLE'))
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())

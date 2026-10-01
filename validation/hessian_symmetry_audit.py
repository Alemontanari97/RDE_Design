#!/usr/bin/env python3
"""[X-HSYM] THE HESSIAN'S SYMMETRY DEFECT, MEASURED BEFORE SYMMETRISATION (F2 CLOSE 2026-10-01; the duty [P-HESSREJ]
of finding driver-nonsmooth:hessian-no-rejector).

The bell driver (a1_toc_variational_jax.py, R-3) takes its trust-region model from forward differences of the EXACT
adjoint gradient, step dH_j = sqrt(eps) max(|W_j|, 1), and symmetrises it blind: Hw = (Hw + Hw^T)/2. A Hessian that is
wrong (a difference straddling a kink of the replay: a column O(1) wrong) then shapes every step and can pass for a
certifiability limit. This carrier puts the defect against the error model of the differences themselves, on one S18
segment: the TOC posing of [X-O32] S3 (W* = the S18 landing, the C^1 quintic closure, the frozen-schedule replay).

ERROR MODEL (Nocedal-Wright: forward-difference truncation O(dH) plus rounding eps_g/dH), MEASURED: the same columns
at dH/2 give the truncation of the dH column, 2 |H(dH) - H(dH/2)|; the rounding is 2 eps_g / dH_j with eps_g =
NEWTON_TOL_FACTOR eps N_cells max|g| (the march's accumulated certification floor). Band_ij = K_RICH (e_ij + e_ji).
GATES: HS-1 the defect |H - H^T| inside the band, entrywise; HS-2 (the rejector, must FIRE) one column scaled by
corrupt_scale leaves the band; HS-3 directional curvature d^T H_sym d against the Richardson extrapolation of the
second difference of J along d (steps h, h/2, h = eps^(1/4) scale), inside K_RICH (|S(h) - S(h/2)| + d^T e d), for
n_dirs seeded unit directions; HS-4 (READING, the challenger) the BFGS carry along a Newton step of newton_step against
fresh differences at the new point, both scored by the directional Richardson curvature there; HS-5 the driver path
(A1_HESSREJ=1, a1_toc_variational_jax.run_trsqp): one segment at W* with the dH column doctored as in HS-2 is REFUSED by
the driver (HessianDefectError, must fire), the same segment undoctored proceeds (positive control); HS-5b the column
doctored at BOTH steps (a biased column) is refused. MEASURED 2026-10-01: HS-5 does NOT fire -- a kink within one step
moves the half-step columns too and the band absorbs it (ratio <= 1/(2 K_RICH)); HS-2 fires because its band is taken
before the corruption (a biased column). Finding driver-nonsmooth:hessian-no-rejector owns the kink half.
Constants in hessian_symmetry_cases.json. Exit 0 iff HS-1, HS-2 (firing), HS-3 and HS-5 (firing + control) pass.
ON-DEMAND (env: jax)."""
import json
import os
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1          # noqa: E402
import a1_toc_variational_jax as TV      # noqa: E402
import a1_march_scan as SC               # noqa: E402
import thermotab_c1_jax as TH            # noqa: E402
import o32_mesh_convergence as O         # noqa: E402

jax.config.update("jax_enable_x64", True)
EPS = float(jnp.finfo(jnp.float64).eps)
HERE = os.path.dirname(os.path.abspath(__file__))
CA = json.load(open(os.path.join(HERE, "hessian_symmetry_cases.json")))["audit"]["value"]


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def fd_hessian(grad, W, g0, steps):
    n = len(W)
    H = np.empty((n, n))
    for j in range(n):
        e = np.zeros(n)
        e[j] = steps[j]
        H[:, j] = (np.asarray(grad(W + e)) - g0) / steps[j]
    return H


def main():
    t00 = time.perf_counter()
    print("== [X-HSYM] the Hessian's symmetry defect before symmetrisation, on one S18 segment (JAX %s) =="
          % jax.__version__, flush=True)
    tab = A1.prep_tab(A1.build_tab_nasa())
    c1 = TH.build_c1(tab)

    def state_c1(q, ta_ignored):
        return TH.state_q_c1(q, c1)

    solv = SC.cached_solvers(("thc1_nasa", 1.0), state_c1, 1.0)
    cfg = dict(NI=TV.TCASE["NI"], Nw=TV.NW, da_deg=TV.TCASE["da_deg"], yt=TV.TCASE["yt"], rtu=TV.TCASE["rtu"],
               rtd=TV.TCASE["rtd"], xtronc=TV.TCASE["xtronc"])
    W = np.asarray(O.W_STAR, float)
    n = len(W)
    out, plan = TV.run_toc_record(W, tab, cfg, state_fn=state_c1, solvers=solv)
    assert float(out["cert_worst"]) <= 1.0, "the S18 landing must march certified"
    runj = TV.make_run_toc_scan_jit(tab, cfg, plan, state_fn=state_c1, solvers=solv)

    def scalar_J(Wv):
        return -TV.thrust_J(runj(Wv), tab, state_fn=state_c1)

    val = jax.jit(scalar_J)
    grad_j = jax.jit(jax.grad(scalar_J))

    def J(Wv):
        return float(val(jnp.asarray(Wv)))

    def grad(Wv):
        return np.asarray(grad_j(jnp.asarray(Wv)))

    g0 = grad(W)
    ncell = int(out["cert_n"])
    eps_g = A1.NEWTON_TOL_FACTOR * EPS * ncell * float(np.max(np.abs(g0)))
    dH = np.array([EPS ** 0.5 * max(abs(W[j]), 1.0) for j in range(n)])
    print("  segment base W* (n %d), certified cells %d, |g|max %.3e, eps_g %.3e; the driver's steps dH %s"
          % (n, ncell, float(np.max(np.abs(g0))), eps_g, np.array2string(dH, precision=2)), flush=True)
    H1 = fd_hessian(grad, W, g0, dH)
    H2 = fd_hessian(grad, W, g0, dH * 0.5)
    trunc = 2.0 * np.abs(H1 - H2)
    rnd = 2.0 * eps_g / dH[None, :] * np.ones((n, 1))
    e = trunc + rnd
    band = A1.K_RICH * (e + e.T)
    defect = np.abs(H1 - H1.T)
    ratio = np.where(band > 0.0, defect / np.where(band > 0.0, band, 1.0), np.inf)
    i_, j_ = np.unravel_index(int(np.argmax(ratio)), ratio.shape)
    print("  symmetry defect: max |H - H^T| %.3e, max defect/band %.3f at (%d, %d); |H|max %.3e, band median %.3e"
          % (float(defect.max()), float(ratio.max()), i_, j_, float(np.abs(H1).max()), float(np.median(band))), flush=True)
    ok = check("HS-1 the driver's Hessian: symmetry defect inside the measured band, entrywise (max ratio %.3f)"
               % float(ratio.max()), bool(np.all(defect <= band)))
    jc = int(np.argmax(np.linalg.norm(H1, axis=0)))
    Hc = H1.copy()
    Hc[:, jc] = Hc[:, jc] * CA["corrupt_scale"]
    dc = np.abs(Hc - Hc.T)
    fired = bool(np.any(dc > band))
    ok &= check("HS-2 REJECTOR: column %d scaled by %.2f (a kink-straddling difference) leaves the band (max ratio %.1f)"
                % (jc, CA["corrupt_scale"], float(np.max(dc / np.where(band > 0.0, band, 1.0)))), fired)
    Hs = 0.5 * (H1 + H1.T)
    rng = np.random.default_rng(int(CA["seed"]))
    J0 = J(W)

    def directional(Wb, Jb, Hm, em, d):
        h = EPS ** 0.25 * max(float(np.max(np.abs(Wb))), 1.0)
        S1 = (J(Wb + h * d) - 2.0 * Jb + J(Wb - h * d)) / h ** 2
        S2 = (J(Wb + 0.5 * h * d) - 2.0 * Jb + J(Wb - 0.5 * h * d)) / (0.5 * h) ** 2
        R = (4.0 * S2 - S1) / 3.0
        m = float(d @ Hm @ d)
        tol = A1.K_RICH * (abs(S1 - S2) + float(np.abs(d) @ em @ np.abs(d)))
        return m, R, abs(S1 - S2), tol

    for k in range(int(CA["n_dirs"])):
        d = rng.standard_normal(n)
        d /= np.linalg.norm(d)
        m, R, dS, tol = directional(W, J0, Hs, e, d)
        ok &= check("HS-3 direction %d: d^T H d %.6e vs the Richardson second difference %.6e (|S(h)-S(h/2)| %.2e); "
                    "|diff| %.2e <= %.2e" % (k, m, R, dS, abs(m - R), tol), abs(m - R) <= tol)
    s = -np.linalg.solve(Hs, g0)
    s *= CA["newton_step"] / np.linalg.norm(s)
    W1 = W + s
    g1 = grad(W1)
    y = g1 - g0
    Hb = Hs - np.outer(Hs @ s, Hs @ s) / float(s @ Hs @ s) + np.outer(y, y) / float(y @ s)
    dH1 = np.array([EPS ** 0.5 * max(abs(W1[j]), 1.0) for j in range(n)])
    Hf = fd_hessian(grad, W1, g1, dH1)
    Hf = 0.5 * (Hf + Hf.T)
    J1 = J(W1)
    eb, ef = [], []
    for k in range(int(CA["n_dirs"])):
        d = rng.standard_normal(n)
        d /= np.linalg.norm(d)
        _, R, _, _ = directional(W1, J1, Hf, np.zeros((n, n)), d)
        eb.append(abs(float(d @ Hb @ d) - R) / max(abs(R), EPS))
        ef.append(abs(float(d @ Hf @ d) - R) / max(abs(R), EPS))
    print("  HS-4 READING (the challenger): after a Newton step of %.1e the BFGS carry misses the directional curvature "
          "by %s (relative), fresh differences by %s -> %s" % (
              CA["newton_step"], " ".join("%.2e" % v for v in eb), " ".join("%.2e" % v for v in ef),
              "the carry is as good here" if max(eb) <= max(ef) else "fresh differences win"), flush=True)
    # HS-5: the driver path (A1_HESSREJ=1): one segment at W*, the doctored column must be REFUSED by the driver
    # itself; the same segment undoctored must proceed (positive control)
    yL = TV.TCASE["yt"] * np.sqrt(TV.TCASE["eps"])
    gtol = CA["gtol_gscale_factor"] * float(np.linalg.norm(g0))
    old = os.environ.get("A1_HESSREJ")
    os.environ["A1_HESSREJ"] = "1"
    try:
        TV._HESS_DOCTOR = dict(col=jc, scale=CA["corrupt_scale"])
        fired, msg = False, ""
        try:
            TV.run_trsqp(W, tab, cfg, yL, gtol=gtol, xtol=CA["xtol"], max_segments=1, maxiter_per_seg=1,
                         state_fn=state_c1, solvers=solv, verbose=0)
        except TV.HessianDefectError as err:
            fired, msg = True, str(err)
        print("  HS-5 doctored segment: %s" % (msg if fired else "NOT refused"), flush=True)
        ok &= check("HS-5 REJECTOR in the driver: the segment with column %d x %.2f is REFUSED (HessianDefectError)"
                    % (jc, CA["corrupt_scale"]), fired)
        TV._HESS_DOCTOR = None
        refused = False
        try:
            TV.run_trsqp(W, tab, cfg, yL, gtol=gtol, xtol=CA["xtol"], max_segments=1, maxiter_per_seg=1,
                         state_fn=state_c1, solvers=solv, verbose=0)
        except TV.HessianDefectError as err:
            refused, msg = True, str(err)
        ok &= check("HS-5 control: the undoctored segment proceeds through the driver's check%s"
                    % ((" (refused: %s)" % msg) if refused else ""), not refused)
        # HS-5b (declared 2026-10-01 before its run at 19:39, after HS-5 failed; it does not replace HS-5): the same column wrong at
        # BOTH steps (a biased gradient path, not a kink) must be refused by the driver
        TV._HESS_DOCTOR = dict(col=jc, scale=CA["corrupt_scale"], both=True)
        fired_b, msg = False, ""
        try:
            TV.run_trsqp(W, tab, cfg, yL, gtol=gtol, xtol=CA["xtol"], max_segments=1, maxiter_per_seg=1,
                         state_fn=state_c1, solvers=solv, verbose=0)
        except TV.HessianDefectError as err:
            fired_b, msg = True, str(err)
        print("  HS-5b biased column: %s" % (msg if fired_b else "NOT refused"), flush=True)
        ok &= check("HS-5b REJECTOR in the driver: the column %d x %.2f at both steps (a biased column) is REFUSED"
                    % (jc, CA["corrupt_scale"]), fired_b)
    finally:
        TV._HESS_DOCTOR = None
        if old is None:
            os.environ.pop("A1_HESSREJ", None)
        else:
            os.environ["A1_HESSREJ"] = old
    print("VERDICT: %s (%.0f s)" % ("PASS" if ok else "FAIL", time.perf_counter() - t00), flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""[X-OBJD] THE THROAT PANEL OF THE BELL OBJECTIVE: the analytic A/B (F2 CLOSE 2026-10-01; duties [OBJ-DOM-IMPL],
[OBJ-DOM-AB], [OBJ-DOM-REBASE] of finding variational-driver:objective-omits-throat-panel; protocol of record
validation/sfoundations_raws_2026-08-13/phaseD/phaseD_minor_objdom.md section 2, P-1..P-4 and F-1..F-2).

The physics: the bell objective adds up the wall push from the first arc station theta_1 = theta_B/n_B on; the strip of
wall between the throat (theta = 0) and that station is left out. Its push is small and fixed in value, but it grows
with the attachment angle theta_B, so it tilts the optimum. J_A (a1_toc_variational_jax.py, A1_OBJDOM=A) adds it back:
the theta = 0 station (the IVL wall point, plan-frozen) prepended to the wall array, the same trapezoid as the rest
(P-1: panel pressure = the kernel flow at both ends; quadrature = F-1 branch (i)).

Instance: W* = the S18 landing (the incumbent of record of S20's design file), the C^1 quintic closure, one frozen plan.
GATES (declared in validation/PROGRESS_2026-10-01_F2CLOSE.md before authoring):
  T-0  the theta = 0 station equals the record's IVL wall point, bitwise; the first arc station lies on the exact arc.
  T-1  the driver's switch: objective_J is thrust_J unset and thrust_J_A under A1_OBJDOM=A, bitwise.
  P-2  dJ/dW under both objectives through the same jitted replay (one plan, no re-record).
  F-1(a) the gradients differ only in theta_B: every contour component of the difference below eps_g.
  F-1(b) the theta_B component equals the branch-(i) closed form, p'(theta_1) by central differences of the first
       station's pressure (independent of the adjoint); bar K_RICH (|pred(h) - pred(h/2)| + eps_g).
  F-1 rejector (must FIRE): the exact-integral target (c) misses the measured difference by more than the bar.
  F-2  the tilt x Dv_thetaB (the driver's Jacobi rule at W*) > 10 gtol (gtol by the X-TOCV O3.1 rule at W*):
       expected to FIRE; if not, the adjudication re-opens (declared).
  P-3  the driver's TR-SQP under A1_OBJDOM=A from W*, gtol unchanged: status 1/2, KKT <= 10 gtol, constraint <= gtol,
       no nonfinite event, the landing certified with its margin audit (floor = min margin(W*)/K_RICH).
  P-4  J_A - J_B = the panel's closed form at round-off on the ladder r in ladder_r (theta_1 halved); readings: the
       panel against J, against the level-to-level change of J, and its theta_1^2 scaling.
Constants in objdom_ab_cases.json. Exit 0 iff every gate passes (F-2 and the F-1 rejector firing). ON-DEMAND (env: jax)."""
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
CA = json.load(open(os.path.join(HERE, "objdom_ab_cases.json")))["ab"]["value"]


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def panel_closed_form(p0, yt, p1, y1):
    """Branch (i): the theta = 0-station single-interval trapezoid of 2 pi p y dy."""
    return 2.0 * np.pi * 0.5 * (p0 * yt + p1 * y1) * (y1 - yt)


def main():
    t00 = time.perf_counter()
    print("== [X-OBJD] the throat panel of the bell objective: the analytic A/B at the S18 landing (JAX %s) =="
          % jax.__version__, flush=True)
    tab = A1.prep_tab(A1.build_tab_nasa())
    c1 = TH.build_c1(tab)

    def state_c1(q, ta_ignored):
        return TH.state_q_c1(q, c1)

    ta = A1.tab_arrays(tab)
    solv = SC.cached_solvers(("thc1_nasa", 1.0), state_c1, 1.0)
    base = dict(NI=TV.TCASE["NI"], Nw=TV.NW, da_deg=TV.TCASE["da_deg"], yt=TV.TCASE["yt"], rtu=TV.TCASE["rtu"],
                rtd=TV.TCASE["rtd"], xtronc=TV.TCASE["xtronc"])
    yt, rtd = base["yt"], base["rtd"]
    W = np.asarray(O.W_STAR, float)
    n = len(W)
    ok = True

    def p_of(pt):
        return float(state_c1(jnp.sqrt(pt[2] ** 2 + pt[3] ** 2), ta)[1])

    # ---------------- T-0: the theta = 0 station and the first arc station
    print("-- T-0: the theta = 0 station and the arc --", flush=True)
    out, plan = TV.run_toc_record(W, tab, base, state_fn=state_c1, solvers=solv, return_field=True)
    assert float(out["cert_worst"]) <= 1.0, "the S18 landing must march certified"
    n_B = int(plan["n_B"])
    thr = np.asarray(TV.throat_station(base, tab))
    ivl0 = np.asarray(out["cols"][out["n_fan"] - 1]["cline"][0])
    print("  throat station [x, y, u, v] = %s; the record's IVL wall point = %s"
          % (np.array2string(thr, precision=12), np.array2string(ivl0, precision=12)), flush=True)
    ok &= check("T-0 the theta = 0 station IS the record's IVL wall point (bitwise)", np.array_equal(thr, ivl0))
    wall = np.asarray(out["wall"])
    th1 = W[0] / n_B
    y1_arc = yt + rtd * (1.0 - np.cos(th1))
    x1_arc = rtd * np.sin(th1)
    dgeo = max(abs(wall[0, 1] - y1_arc), abs(wall[0, 0] - x1_arc))
    ok &= check("T-0 the first wall station lies on the exact arc at theta_1 = theta_B/n_B = %.6e (n_B %d): "
                "|dx|, |dy| <= %.2e (bar 2 eps max(y, 1) = %.2e)"
                % (th1, n_B, dgeo, 2.0 * EPS * max(y1_arc, 1.0)), dgeo <= 2.0 * EPS * max(y1_arc, 1.0))

    # ---------------- T-1 + P-2: one jitted replay, both objectives
    print("-- T-1 / P-2: both objectives on one frozen plan --", flush=True)
    runj = TV.make_run_toc_scan_jit(tab, base, plan, state_fn=state_c1, solvers=solv)
    thr_j = TV.throat_station(base, tab)

    def JB(Wv):
        return TV.thrust_J(runj(Wv), tab, state_fn=state_c1)

    def JA(Wv):
        return TV.thrust_J_A(runj(Wv), tab, thr_j, state_fn=state_c1)

    Wj = jnp.asarray(W)
    wall_r = runj(Wj)
    old = os.environ.pop("A1_OBJDOM", None)
    try:
        jb_sw = float(TV.objective_J(wall_r, tab, base, state_fn=state_c1))
        os.environ["A1_OBJDOM"] = "A"
        ja_sw = float(TV.objective_J(wall_r, tab, base, state_fn=state_c1))
    finally:
        os.environ.pop("A1_OBJDOM", None)
        if old is not None:
            os.environ["A1_OBJDOM"] = old
    J_B, J_A = float(JB(Wj)), float(JA(Wj))
    ok &= check("T-1 the driver's switch: objective_J = thrust_J unset, = thrust_J_A under A1_OBJDOM=A (bitwise)",
                jb_sw == J_B and ja_sw == J_A)
    gB = np.asarray(jax.grad(JB)(Wj))
    gA = np.asarray(jax.grad(JA)(Wj))
    D = gA - gB
    ncell = int(out["cert_n"])
    eps_g = A1.NEWTON_TOL_FACTOR * EPS * ncell * float(np.max(np.abs(gB)))
    print("  J_B (coded) = %.12e   J_A (panel-inclusive) = %.12e   J_A - J_B = %.6e (%.3e of J)"
          % (J_B, J_A, J_A - J_B, (J_A - J_B) / J_B), flush=True)
    print("  dJ/dW coded  = %s" % np.array2string(gB, precision=6), flush=True)
    print("  dJ/dW with A = %s" % np.array2string(gA, precision=6), flush=True)
    print("  difference   = %s   (eps_g = NEWTON_TOL_FACTOR eps N_cells max|g| = %.3e, N_cells %d)"
          % (np.array2string(D, precision=6), eps_g, ncell), flush=True)

    # ---------------- F-1(a)
    ok &= check("F-1(a) the panel depends on W only through theta_B: max contour |dJ_A - dJ_B| = %.3e <= eps_g %.3e"
                % (float(np.max(np.abs(D[1:]))), eps_g), bool(np.all(np.abs(D[1:]) <= eps_g)))

    # ---------------- F-1(b): branch-(i) prediction with p'(theta_1) by central differences on the frozen replay
    p0 = p_of(thr)
    w0 = np.asarray(wall_r[0])
    p1 = p_of(w0)
    y1 = float(w0[1])
    dy1 = rtd * np.sin(th1) / n_B             # d y(theta_1) / d theta_B at frozen n_B

    def p_first(Wv):
        return p_of(np.asarray(runj(jnp.asarray(Wv))[0]))

    def pred_at(hsc):
        h = EPS ** (1.0 / 3.0) * hsc * max(abs(W[0]), 1.0)
        e = np.zeros(n)
        e[0] = h
        dp1 = (p_first(W + e) - p_first(W - e)) / (2.0 * h)
        return 2.0 * np.pi * (0.5 * (dp1 * y1 + p1 * dy1) * (y1 - yt) + 0.5 * (p0 * yt + p1 * y1) * dy1), dp1

    pr1, dp1a = pred_at(1.0)
    pr2, dp1b = pred_at(0.5)
    bar = A1.K_RICH * (abs(pr1 - pr2) + eps_g)
    print("  p(0) = %.6e  p(theta_1) = %.6e  y(theta_1) - yt = %.6e  dp(theta_1)/dtheta_B = %.6e / %.6e (h, h/2) "
          "-> p'(theta_1)/p = %.4f per rad" % (p0, p1, y1 - yt, dp1a, dp1b, dp1b * n_B / p1), flush=True)
    print("  theta_B component: measured %.10e   branch (i) %.10e   |diff| %.3e   bar %.3e"
          % (D[0], pr2, abs(D[0] - pr2), bar), flush=True)
    ok &= check("F-1(b) the theta_B component equals the branch-(i) closed form inside the bar", abs(D[0] - pr2) <= bar)
    Dc = 2.0 * np.pi * p1 * y1 * rtd * np.sin(th1) / n_B
    print("  exact-integral target (c) 2 pi p y rtd sin(theta_1)/n_B = %.10e: misses by %.3e (%.1f bars)"
          % (Dc, abs(D[0] - Dc), abs(D[0] - Dc) / bar), flush=True)
    ok &= check("F-1 REJECTOR: the target (c) (no quadrature term) is told apart from branch (i) (misses by > bar)",
                abs(D[0] - Dc) > bar)

    # ---------------- F-2: the tilt in the driver's coordinates against 10 gtol
    print("-- F-2: the tilt against the O3 acceptance --", flush=True)
    v = np.asarray(np.random.default_rng(int(CA["o31_seed"])).standard_normal(n))
    v /= np.linalg.norm(v)
    jb_val = jax.jit(JB)

    def dirder(hsc):
        h = EPS ** (1.0 / 3.0) * hsc * max(1.0, float(np.abs(W).max()))
        return (float(jb_val(Wj + h * jnp.array(v))) - float(jb_val(Wj - h * jnp.array(v)))) / (2.0 * h)

    d1, d2 = dirder(1.0), dirder(0.5)
    tol_dp = A1.K_RICH * (abs(d1 - d2) + A1.C_FLOOR * EPS ** (2.0 / 3.0) * max(abs(J_B), 1.0))
    gtol = max(tol_dp, CA["gtol_gscale_factor"] * float(np.linalg.norm(gB)))
    print("  O3.1 at W*: FD %.10e vs <g,v> %.10e (|diff| %.3e, tol_dp %.3e); gtol = max(tol_dp, %.0e |g|) = %.4e"
          % (d2, float(gB @ v), abs(d2 - float(gB @ v)), tol_dp, CA["gtol_gscale_factor"], gtol), flush=True)
    gjit = jax.jit(jax.grad(JB))
    hd = np.empty(n)
    for i in range(n):
        d = EPS ** (1.0 / 3.0) * max(abs(W[i]), 1.0)
        e = np.zeros(n)
        e[i] = d
        hd[i] = (float(np.asarray(gjit(jnp.asarray(W + e)))[i]) - float(np.asarray(gjit(jnp.asarray(W - e)))[i])) \
            / (2.0 * d)
    habs = np.abs(hd)
    Dv = 1.0 / np.sqrt(np.maximum(habs, CA["dv_floor"] * habs.max()))
    Dv = Dv / np.median(Dv)
    tilt = abs(float(D[0]))
    tilt_u = tilt * Dv[0]
    print("  Jacobi scaling at W* (the driver's rule): diag|H| in [%.3e, %.3e]; Dv = %s"
          % (habs.min(), habs.max(), np.array2string(Dv, precision=3)), flush=True)
    print("  tilt %.4e J-units/rad; x Dv_thetaB %.4f = %.4e against 10 gtol = %.4e: x %.1f   (fallback reading: "
          "tilt / (10 gtol) = %.1f against 6)" % (tilt, Dv[0], tilt_u, 10.0 * gtol, tilt_u / (10.0 * gtol),
                                                 tilt / (10.0 * gtol)), flush=True)
    ok &= check("F-2 the tilt in the driver's coordinates exceeds the O3 acceptance 10 gtol (expected to FIRE; "
                "the gradient axis governs)", tilt_u > 10.0 * gtol)

    # ---------------- P-3: the driver's TR-SQP under J_A from W*, gtol unchanged
    print("-- P-3: the driver's TR-SQP under A1_OBJDOM=A from W* (gtol %.4e unchanged) --" % gtol, flush=True)
    H00 = float(hd[0])
    print("  predicted theta_B shift ~ tilt / |H_00| = %.3e rad (H_00 = %.4e)" % (tilt / abs(H00), H00), flush=True)
    yL = TV.TCASE["yt"] * np.sqrt(TV.TCASE["eps"])
    delta_floor = float(out["min_margin"]) / A1.K_RICH
    os.environ["A1_OBJDOM"] = "A"
    t0 = time.perf_counter()
    try:
        opt = TV.run_trsqp(W, tab, base, yL, gtol=gtol, xtol=CA["xtol"],
                           max_segments=int(CA["p3_max_segments"]), state_fn=state_c1, solvers=solv, verbose=0)
    except RuntimeError as err:
        print("  P-3 the driver stopped with a typed error: %s" % err, flush=True)
        check("P-3 converged under J_A at the unchanged gtol", False)
        print("VERDICT: FAIL (%.0f s)" % (time.perf_counter() - t00), flush=True)
        return 1
    finally:
        os.environ.pop("A1_OBJDOM", None)
    res = opt["res"]
    WA = np.asarray(opt["W"], float)
    print("  segments %d, re-records %d, nit %d, evals %d, %.0f s; status %d; KKT %.4e (10 gtol %.4e); constraint "
          "%.3e; nonfinite grad %d obj %d"
          % (opt["n_segments"], opt["re_records"], opt["nit_total"], opt["n_eval"], time.perf_counter() - t0,
             res.status, res.optimality, 10.0 * gtol, res.constr_violation, opt["n_nonfinite_grad"],
             opt["n_nonfinite_obj"]), flush=True)
    print("  W*_A - W* = %s  (theta_B %+.4e rad)" % (np.array2string(WA - W, precision=3), WA[0] - W[0]), flush=True)
    ok &= check("P-3 converged under J_A at the unchanged gtol (status 1/2, KKT <= 10 gtol, constraint <= gtol, "
                "no nonfinite event)",
                res.status in (1, 2) and res.optimality <= 10.0 * gtol and res.constr_violation <= gtol
                and opt["n_nonfinite_grad"] == 0 and opt["n_nonfinite_obj"] == 0)
    out_s, plan_s = TV.run_toc_record(WA, tab, base, state_fn=state_c1, solvers=solv, margin_floor=delta_floor)
    ok &= check("P-3 the landing W*_A certified (worst %.3e) with margin %.4f >= floor %.4f m/s"
                % (float(out_s["cert_worst"]), float(out_s["min_margin"]), delta_floor),
                float(out_s["cert_worst"]) <= 1.0 and float(out_s["min_margin"]) >= delta_floor)
    thr_np = np.asarray(thr_j)
    wsA = np.asarray(out_s["wall"])
    JA_star = float(TV.thrust_J_A(jnp.asarray(wsA), tab, thr_j, state_fn=state_c1))
    JA_W = float(TV.thrust_J_A(jnp.asarray(wall), tab, thr_j, state_fn=state_c1))
    print("  J_A(W*_A) - J_A(W*) = %.4e (record walls; the gain of moving to the J_A optimum)" % (JA_star - JA_W),
          flush=True)

    # ---------------- P-4: value axis on the ladder
    print("-- P-4: the value axis on the ladder (theta_1 halved) --", flush=True)
    rows = []
    for r in CA["ladder_r"]:
        cfg = dict(base)
        cfg["NI"] = r * (base["NI"] - 1) + 1
        cfg["Nw"] = r * base["Nw"]
        cfg["da_deg"] = base["da_deg"] / r
        o_r, pl_r = TV.run_toc_record(W, tab, cfg, state_fn=state_c1, solvers=solv)
        assert float(o_r["cert_worst"]) <= 1.0, "ladder level r=%d not certified" % r
        w_r = jnp.asarray(o_r["wall"])
        th_r = TV.throat_station(cfg, tab)
        jb = float(TV.thrust_J(w_r, tab, state_fn=state_c1))
        ja = float(TV.thrust_J_A(w_r, tab, th_r, state_fn=state_c1))
        w1 = np.asarray(o_r["wall"][0])
        P = panel_closed_form(p_of(np.asarray(th_r)), yt, p_of(w1), float(w1[1]))
        tol = A1.NEWTON_TOL_FACTOR * EPS * abs(ja)
        rows.append(dict(r=r, jb=jb, ja=ja, P=P, th1=W[0] / int(pl_r["n_B"]), S=p_of(np.asarray(th_r)) * yt
                         + p_of(w1) * float(w1[1])))
        print("    r=%d  n_B %-3d theta_1 %.6e  J_B %.12e  J_A %.12e  J_A - J_B %.6e  panel (closed form) %.6e  "
              "|diff| %.2e (bar %.2e)" % (r, int(pl_r["n_B"]), W[0] / int(pl_r["n_B"]), jb, ja, ja - jb, P,
                                          abs((ja - jb) - P), tol), flush=True)
        ok &= check("P-4 r=%d: J_A - J_B = the panel's closed form at round-off (identity a.1)" % r,
                    abs((ja - jb) - P) <= tol)
    if len(rows) >= 2:
        a, b = rows[0], rows[1]
        ratio = a["P"] / b["P"]
        print("  READINGS: panel %.4e = %.2e of J; level change of J: coded %.4e, panel-inclusive %.4e (the panel's "
              "own change %.4e); panel ratio r=%d/r=%d %.5f against (theta_1 ratio)^2 = %.5f (n_B %s; the rest is the "
              "end-pressure sum ratio %.6f)" % (a["P"], a["P"] / a["jb"], b["jb"] - a["jb"], b["ja"] - a["ja"],
                                                b["P"] - a["P"], a["r"], b["r"], ratio, (a["th1"] / b["th1"]) ** 2,
                                                "/".join("%d" % round(W[0] / t["th1"]) for t in (a, b)),
                                                a["S"] / b["S"]), flush=True)
    print("VERDICT: %s (%.0f s)" % ("PASS" if ok else "FAIL", time.perf_counter() - t00), flush=True)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

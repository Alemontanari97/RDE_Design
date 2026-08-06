#!/usr/bin/env python3
"""BRICK 2 [F2/A1, session S17]: the VARIATIONAL TOC engine — thrust
objective + constraints {eps, L, lip-class monitors}, transversality
reached VIA THE GRADIENT dJ/dSigma (reverse-AD of the specified-wall
march = Lemma B, O3.1-verified here on the TOC configuration) inside
a TR-SQP driver (SciPy trust-constr, kickoff §4bis decision) under
the RK-G segmentation policy [DIR-RKG]. NEVER a hard-coded outer
loop: the GENO type-2 Mrao/eps + xsol bisections are the CROSS-CODE
REFERENCE ONLY (oracle O2 below). Registry ID: [X-TOCV].

DESIGN VECTOR W (the wall Sigma, finite-dim instance):
  W = [theta_B, y_1, ..., y_m]  — attachment angle on the throat arc
  (wall leaves the circular arc at theta_B with C^1 continuity) +
  wall heights at m uniform interior/lip nodes on [x_B(theta_B), L].
  Wall = NATURAL CUBIC SPLINE (C^2, per the U1 C_geo class) with
  clamped left end (y_B, tan theta_B); lip node y_m carries the eps
  equality constraint y_m = yt sqrt(eps) (linear in W); length L
  fixed by construction (last node AT x = L). Lip/class monitors
  (slope positivity, supersonic wall) are DECLARED monitors at
  instance, not active constraints.

OBJECTIVE: J(W) = wall pressure-thrust integral
  J = 2 pi * sum_trapz  p * y * dy  over the DESIGN wall (arc sector
  theta in (0, theta_B] + contoured section to the lip).
  With BOTH eps and L constrained, the ambient term Pa*(A_lip-A_0)
  is constant on the feasible set => Pa drops out of the argmax
  (declared; vacuum-equivalent objective, GENO-comparable).

MARCH (specified-wall direct march; every cell = the certified
[X-A1IM] unit processes; scan replay per duty (b)):
  IVL + fan: identical to [X-A1IM]. Arc sector: wall stations at
  angles theta_B * k/n_B (count n_B FROZEN by the record, positions
  traced => dJ/dtheta_B exact at fixed topology). Contour: wall
  stations x_k uniform on [x_B, L] (count Nw frozen); each station =
  direct-wall implicit cell (foot on the chord of the previous
  column — the recorded N/Nv wall-search indices freeze the DAG),
  then the interior sweep to the axis (lax.scan per column). Record
  mode = adaptive Python (concrete decisions, per-cell Newton
  certification, RK-G P2/P4 site); replay mode = traced scan.

RK-G COMPLIANCE [DIR-RKG]: P1 frozen schedule inside each
trust-constr segment (all evaluations replay the plan recorded at
the segment's accepted base point); P2 re-record on acceptance =
segment boundary (fresh trust-constr instance, plan re-recorded,
re-record events counted and REPORTED in the Verdict); P3 monitors:
(i) replay fidelity at the base point (Newton floor), (ii) per-cell
certification of the record at every accepted iterate (P4 gate);
decision-flip detection = plan comparison at re-record. TABLE-KNOT
crossings are non-events by [X-THC1] C^1 closure — the brick runs
the quintic closure as PRIMARY (linear closure = twin check).

ORACLES / CHECKS:
  O1  O3.1 dot-product on the TOC march (whole gradient chain).
  O2  cross-code: GENO nozzle_type=2 run at the SAME reduced twin
      case (scratch dir, file exchange, GENO never modified) — the
      TR-SQP optimum contour must sit inside the derived
      two-resolution Richardson band of the GENO Rao contour.
  O3  transversality instance (O3.3 opener): at the converged
      optimum the projected gradient onto the feasible set vanishes
      (KKT residual below the derived optimizer tolerance) — the
      executable statement that the RAO CONDITIONS have been reached
      VIA THE GRADIENT (the full pre-registered O3.3 term-match
      bench (30)/(31)+f2 is the P-2 numeric campaign this brick
      unlocks; its protocol is UNTOUCHED — P2_outline §5).
  NEGATIVE CONTROLS: (N1) corrupted gradient (sign-flipped one
      component) breaks O3.1; (N2) the optimizer restarted from a
      perturbed feasible point must return to the same optimum
      within derived bars (local uniqueness probe); (N3) shrunken-L
      run must NOT match the GENO reference (the oracle
      discriminates designs).

TOLERANCES — ALL DERIVED (R5): contour band = K_RICH x
(two-resolution Richardson estimate + 64 eps floor) as in [X-A1IM];
O3.1 = FD two-step Richardson + roundoff floor; KKT residual bound =
trust-constr's own gtol x a measured gradient scale; twin-closure
band = interpolation-class band from [X-THC1] C5.

ON-DEMAND CARRIER (env: jax + WSL gfortran GENO binary): outside CI
tiers by declaration. Exit code 0 iff ALL checks pass INCLUDING the
negative controls.
"""
import os
import shutil
import subprocess
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1   # noqa: E402
import a1_march_scan as SC        # noqa: E402
import thermotab_c1_jax as TH     # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
d2r = np.pi / 180.0

# reduced TOC twin case (must match the scratch GENO type-2 input)
TCASE = dict(NI=21, Ne=41, da_deg=0.5, eps=4.0, xtronc=4.0,
             yt=1.0, rtu=1.5, rtd=0.45)
M_NODES = 8          # interior+lip wall nodes (design dofs y_1..y_m)
NW = 60              # contour wall stations (march resolution)


# ======================================================================
# wall spline: natural cubic, clamped left (y_B, tan thB), traced
# ======================================================================
def spline_coeffs(xs, ys, slope0):
    """Cubic spline second-derivative solve: clamped left, natural
    right. xs (n,), ys (n,) traced. Returns M (n,) second derivs."""
    n = xs.shape[0]
    h = xs[1:] - xs[:-1]
    A = jnp.zeros((n, n))
    r = jnp.zeros(n)
    # clamped left: 2 h0/6... standard: (h0/3) M0 + (h0/6) M1 =
    # (y1-y0)/h0 - slope0
    A = A.at[0, 0].set(h[0] / 3.0).at[0, 1].set(h[0] / 6.0)
    r = r.at[0].set((ys[1] - ys[0]) / h[0] - slope0)
    for i in range(1, n - 1):
        A = A.at[i, i - 1].set(h[i - 1] / 6.0)
        A = A.at[i, i].set((h[i - 1] + h[i]) / 3.0)
        A = A.at[i, i + 1].set(h[i] / 6.0)
        r = r.at[i].set((ys[i + 1] - ys[i]) / h[i]
                        - (ys[i] - ys[i - 1]) / h[i - 1])
    A = A.at[n - 1, n - 1].set(1.0)          # natural right: M_{n-1}=0
    r = r.at[n - 1].set(0.0)
    return jnp.linalg.solve(A, r)


def spline_eval(x, xs, ys, M):
    """Value and slope of the cubic spline at x (scalar, traced)."""
    i = jnp.clip(jnp.searchsorted(xs, x, side="right") - 1, 0,
                 xs.shape[0] - 2)
    h = xs[i + 1] - xs[i]
    a = (xs[i + 1] - x) / h
    b = (x - xs[i]) / h
    y = (a * ys[i] + b * ys[i + 1]
         + ((a**3 - a) * M[i] + (b**3 - b) * M[i + 1]) * h * h / 6.0)
    yp = ((ys[i + 1] - ys[i]) / h
          + ((3 * b**2 - 1) * M[i + 1] - (3 * a**2 - 1) * M[i])
          * h / 6.0)
    return y, yp


def wall_geometry(W, P_geom, L):
    """From design vector W -> (arc angles fn, spline data). Traced."""
    yt, rtu, rtd = P_geom
    thB = W[0]
    xB = rtd * jnp.sin(thB)
    yB = yt + rtd * (1.0 - jnp.cos(thB))
    xs = xB + (L - xB) * jnp.arange(1, M_NODES + 1) / M_NODES
    xs = jnp.concatenate([jnp.array([xB]), xs])
    ys = jnp.concatenate([jnp.array([yB]), W[1:]])
    M = spline_coeffs(xs, ys, jnp.tan(thB))
    return xB, yB, xs, ys, M


# ======================================================================
# record: adaptive specified-wall march (concrete), emits plan
# ======================================================================
def run_toc_record(W, tab, cfg, state_fn=A1.state_q, solvers=None):
    """Adaptive TOC march at concrete W. Returns (out, plan).
    Structure mirrors [X-A1IM] run_march phases 1-4 with the wall
    given by (arc up to theta_B) + spline; certification enforced."""
    ta = A1.tab_arrays(tab)
    if solvers is None:
        solvers = SC.cached_solvers(("a1_linear", 1.0), state_fn, 1.0)
    NI, Nw = cfg["NI"], cfg["Nw"]
    da = cfg["da_deg"] * d2r
    yt, rtu, rtd = cfg["yt"], cfg["rtu"], cfg["rtd"]
    L = cfg["xtronc"]
    P_geom = jnp.array([yt, rtu, rtd])
    Wj = jnp.asarray(W)
    xB, yB, xs, ys, Msp = wall_geometry(Wj, P_geom, L)
    thB = float(Wj[0])
    n_B = max(1, int(np.ceil(thB / da)))     # frozen arc-station count

    cert = dict(worst=0.0, n=0)

    def cell(kind, p, z0):
        sol, _, stepn = solvers[kind]
        z = sol(jnp.asarray(z0, dtype=jnp.float64), jnp.asarray(p), ta)
        step = float(stepn(z, jnp.asarray(p), ta))
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        cert["worst"] = max(cert["worst"], step
                            / (A1.NEWTON_TOL_FACTOR * EPS * sc))
        cert["n"] += 1
        return z

    # ---------- IVL + fan (as [X-A1IM]; plan reuses SC column arrays)
    gm = tab["gammamedio"]
    delta = 1.0
    as_ = tab["_as"]
    alpha = np.sqrt((1.0 + delta) / ((gm + 1.0) * rtu * yt))
    c1 = -(gm + 1.0) * alpha / (2.0 * (3.0 + delta))
    c2 = (gm + 1.0) * alpha**2 / (2.0 * (1.0 + delta))
    eshift = -(gm + 1.0) * alpha * yt**2 / (2.0 * (3.0 + delta))
    jj = np.arange(NI)
    y_ivl = yt * (1.0 - jj / (NI - 1.0))
    x_raw = c1 * y_ivl**2 + 0.000001
    u_ivl = as_ * (1.0 + alpha * x_raw + c2 * y_ivl**2)
    x_ivl = x_raw - eshift
    ivl = [jnp.array([x_ivl[k], y_ivl[k], u_ivl[k], 0.0])
           for k in range(NI)]

    plan = dict(fan=[], arc=[], n_B=n_B)
    prev = [ivl[NI - 1]]
    for i in range(2, NI + 1):
        head = ivl[NI - i]
        seeds = []
        carry = head
        newcol = [head]
        for k in range(len(prev)):
            z0 = A1.predict_interior(carry, prev[k], ta, 1.0)
            z = cell("interior", jnp.concatenate([carry, prev[k]]), z0)
            seeds.append(np.asarray(z))
            carry = z
            newcol.append(z)
        z0a = A1.predict_axis(carry, ta, 1.0)
        za = cell("axis", carry, z0a)
        ax = jnp.array([za[0], 0.0, za[1], 0.0])
        newcol.append(ax)
        plan["fan"].append(dict(n=len(seeds), seeds=np.stack(seeds),
                                axis_seed=np.asarray(za)))
        prev = newcol

    # ---------- design-wall columns: n_B arc stations + Nw contour
    j2 = 2 * NI - 1
    Nv = 1
    stations = []
    for k in range(1, n_B + 1):
        th = thB * k / n_B
        x4 = rtd * np.sin(th)
        y4 = yt + rtd * (1.0 - np.cos(th))
        stations.append((float(x4), float(y4), float(np.tan(th))))
    xB_f = float(xB)
    for k in range(1, Nw + 1):
        x4 = xB_f + (float(L) - xB_f) * k / Nw
        yv, yp = spline_eval(jnp.float64(x4), xs, ys, Msp)
        stations.append((x4, float(yv), float(yp)))

    # DOMAIN-OF-DEPENDENCE TRUNCATION (S17 design rule of record,
    # derived from supersonic causality — deviation history in the
    # log): points at x > L cannot influence the wall on x <= L
    # (C+ information only travels downstream), so each column's
    # sweep STOPS once a cell lands past the lip, and the axis is
    # followed only while its intersection stays inside; this also
    # removes the degenerate axis-chasing wedge (cells at x ~ 4.9
    # with y < 0 measured before the rule).
    wall_pts = []
    has_axis = True
    for (x4, y4, sl) in stations:
        # wall_search: chord-foot descent (identical to [X-A1IM])
        N = 0
        Nv_loc = Nv
        while True:
            N += 1
            if N > len(prev) + 1:
                raise RuntimeError("TOC wall_search did not land "
                                   "(station x=%.4f)" % x4)
            pt3 = prev[min(N, len(prev)) - 1]
            pt1 = prev[Nv_loc]
            p = jnp.concatenate([pt1, pt3,
                                 jnp.array([x4, y4, sl])])
            z0 = A1.predict_wall(pt1, pt3, x4, y4, sl, ta, 1.0)
            zt = cell("wall", p, z0)
            if float(zt[0]) > float(pt1[0]):
                N = Nv_loc
                Nv_loc += 1
                continue
            break
        Nv = Nv_loc
        u4 = zt[1]
        wall_pt = jnp.array([x4, y4, u4, sl * u4])
        wall_pts.append(wall_pt)
        seeds = []
        carry = wall_pt
        newcol = [wall_pt] + prev[1:Nv]
        truncated = False
        n_avail = len(prev) - (1 if has_axis else 0)
        for j in range(Nv + 1, n_avail + 1 + (1 if has_axis else 0)):
            pt2 = prev[j - 1]
            z0 = A1.predict_interior(carry, pt2, ta, 1.0)
            z = cell("interior", jnp.concatenate([carry, pt2]), z0)
            seeds.append(np.asarray(z))
            carry = z
            newcol.append(z)
            if float(z[0]) > float(L):
                truncated = True
                break
        axis_seed = None
        col_axis = False
        if has_axis and not truncated:
            z0a = A1.predict_axis(carry, ta, 1.0)
            za = cell("axis", carry, z0a)
            if float(za[0]) <= float(L):
                newcol.append(jnp.array([za[0], 0.0, za[1], 0.0]))
                axis_seed = np.asarray(za)
                col_axis = True
        has_axis = col_axis
        plan["arc"].append(dict(N=N, Nv=Nv, n=len(seeds),
                                wall_seed=np.asarray(zt),
                                seeds=(np.stack(seeds) if seeds
                                       else np.zeros((0, 4))),
                                axis_seed=axis_seed,
                                has_axis=col_axis))
        prev = newcol

    out = dict(wall=jnp.stack(wall_pts), cert_worst=cert["worst"],
               cert_n=cert["n"])
    return out, plan


# ======================================================================
# scan replay (traced in W)
# ======================================================================
def run_toc_scan(W, tab, cfg, plan, state_fn=A1.state_q, solvers=None):
    ta = A1.tab_arrays(tab)
    if solvers is None:
        solvers = SC.cached_solvers(("a1_linear", 1.0), state_fn, 1.0)
    s_int = solvers["interior"][0]
    s_axi = solvers["axis"][0]
    s_wal = solvers["wall"][0]
    NI, Nw = cfg["NI"], cfg["Nw"]
    yt, rtu, rtd = cfg["yt"], cfg["rtu"], cfg["rtd"]
    L = cfg["xtronc"]
    P_geom = jnp.array([yt, rtu, rtd])
    thB = W[0]
    xB, yB, xs, ys, Msp = wall_geometry(W, P_geom, L)
    n_B = plan["n_B"]

    gm = tab["gammamedio"]
    delta = 1.0
    as_ = tab["_as"]
    alpha = jnp.sqrt((1.0 + delta) / ((gm + 1.0) * rtu * yt))
    c1 = -(gm + 1.0) * alpha / (2.0 * (3.0 + delta))
    c2 = (gm + 1.0) * alpha**2 / (2.0 * (1.0 + delta))
    eshift = -(gm + 1.0) * alpha * yt**2 / (2.0 * (3.0 + delta))
    jj = jnp.arange(NI)
    y_ivl = yt * (1.0 - jj / (NI - 1.0))
    x_raw = c1 * y_ivl**2 + 0.000001
    u_ivl = as_ * (1.0 + alpha * x_raw + c2 * y_ivl**2)
    x_ivl = x_raw - eshift
    ivl = jnp.stack([x_ivl, y_ivl, u_ivl, jnp.zeros(NI)], axis=1)

    def cell_scan(seeds, pt2s, carry0):
        seeds = jax.lax.stop_gradient(jnp.asarray(seeds))

        def body(carry, xsc):
            seed, pt2 = xsc
            zc = s_int(seed, jnp.concatenate([carry, pt2]), ta)
            return zc, zc

        _, outc = jax.lax.scan(body, carry0, (seeds, pt2s))
        return outc

    def axis_solve(seed, pt1):
        zc = s_axi(jax.lax.stop_gradient(jnp.array(seed)), pt1, ta)
        return jnp.array([zc[0], 0.0, zc[1], 0.0])

    prev = ivl[NI - 1][None, :]
    for i, colp in enumerate(plan["fan"], start=2):
        head = ivl[NI - i][None, :]
        cells = cell_scan(colp["seeds"], prev, head[0])
        ax = axis_solve(colp["axis_seed"], cells[-1])
        prev = jnp.concatenate([head, cells, ax[None, :]], axis=0)

    # design-wall stations (traced positions, frozen counts/topology)
    stations = []
    for k in range(1, n_B + 1):
        th = thB * k / n_B
        x4 = rtd * jnp.sin(th)
        y4 = yt + rtd * (1.0 - jnp.cos(th))
        stations.append((x4, y4, jnp.tan(th)))
    for k in range(1, Nw + 1):
        x4 = xB + (L - xB) * k / Nw
        yv, yp = spline_eval(x4, xs, ys, Msp)
        stations.append((x4, yv, yp))

    wall_pts = []
    for colp, (x4, y4, sl) in zip(plan["arc"], stations):
        N, Nv, n = colp["N"], colp["Nv"], colp["n"]
        pt1 = prev[Nv]
        pt3 = prev[N - 1]
        p_w = jnp.concatenate([pt1, pt3, jnp.stack([x4, y4, sl])])
        zw = s_wal(jax.lax.stop_gradient(jnp.array(colp["wall_seed"])),
                   p_w, ta)
        u4 = zw[1]
        wall_pt = jnp.stack([x4, y4, u4, sl * u4])
        wall_pts.append(wall_pt)
        pt2s = prev[Nv: Nv + n]              # rows Nv+1 .. Nv+n
        cells = cell_scan(colp["seeds"], pt2s, wall_pt) \
            if n else jnp.zeros((0, 4))
        last = cells[-1] if n else wall_pt
        parts = [wall_pt[None, :], prev[1:Nv], cells]
        if colp["has_axis"]:
            ax = axis_solve(colp["axis_seed"], last)
            parts.append(ax[None, :])
        prev = jnp.concatenate(parts, axis=0)

    return jnp.stack(wall_pts)


# ======================================================================
# objective (wall pressure-thrust integral, Pa-free by {eps, L})
# ======================================================================
def thrust_J(wall, tab, state_fn=A1.state_q):
    ta = A1.tab_arrays(tab)
    q = jnp.sqrt(wall[:, 2]**2 + wall[:, 3]**2)
    p = state_fn(q, ta)[1]
    y = wall[:, 1]
    py = p * y
    dy = y[1:] - y[:-1]
    return 2.0 * jnp.pi * jnp.sum(0.5 * (py[1:] + py[:-1]) * dy)


# (driver, oracle and checks live in main(); see the S17 log)
def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


# ======================================================================
# RK-G segmentation driver (DIR-RKG P1-P4 on scipy trust-constr;
# source semantics verified in kickoff §4bis: equality-only + no
# bounds => Byrd-Omojokun path; callback True => clean stop status 3;
# fresh BFGS per minimize() call; state.x updated on ACCEPTED
# iterations only; status 4 = converged-but-infeasible = failure)
# ======================================================================
def run_trsqp(W0, tab, cfg, yL, gtol, xtol, max_segments=8,
              maxiter_per_seg=40):
    from scipy.optimize import minimize, LinearConstraint

    n = W0.shape[0]
    A = np.zeros((1, n))
    A[0, -1] = 1.0                      # lip node y_m = yL (eps, linear)
    lip_eq = LinearConstraint(A, [yL], [yL])

    W = np.asarray(W0, dtype=float)
    events = []                          # re-record events (P2 log)
    n_rec = 0
    nit_total = 0
    result = None
    for seg in range(max_segments):
        out_rec, plan = run_toc_record(W, tab, cfg)
        n_rec += 1
        if out_rec["cert_worst"] > 1.0:
            raise RuntimeError(
                "P4 gate: record at segment base not certified "
                "(worst %.3e)" % out_rec["cert_worst"])
        # monitor (i): replay fidelity at the base point
        wall_sc = run_toc_scan(jnp.asarray(W), tab, cfg, plan)
        dev = float(jnp.max(jnp.abs(wall_sc - out_rec["wall"])))
        scale = float(jnp.max(jnp.abs(out_rec["wall"])))
        if dev > A1.NEWTON_TOL_FACTOR * EPS * scale * 10.0:
            raise RuntimeError("RK-G monitor (i): replay infidelity "
                               "%.3e at segment base" % dev)
        dec_base = [(c["N"], c["Nv"]) for c in plan["arc"]]

        def scalar_J(Wv):
            wall = run_toc_scan(Wv, tab, cfg, plan)
            return -thrust_J(wall, tab)          # minimize -J
        val_grad = jax.value_and_grad(scalar_J)

        def f_np(x):
            v, _ = val_grad(jnp.asarray(x))
            v = float(v)
            return v if np.isfinite(v) else 1e30  # monitor-lite NaN guard
        def g_np(x):
            _, g = val_grad(jnp.asarray(x))
            g = np.asarray(g)
            return np.where(np.isfinite(g), g, 0.0)

        seg_state = dict(stop=False)

        def cb(state):
            # P2: re-record at every ACCEPTED iterate; end the segment
            # on a decision change (topology moved)
            nonlocal n_rec
            try:
                _, plan_new = run_toc_record(np.asarray(state.x),
                                             tab, cfg)
                n_rec += 1
            except RuntimeError:
                seg_state["stop"] = True     # record failed: shrink via
                return True                  # segment restart from last W
            dec_new = [(c["N"], c["Nv"]) for c in plan_new["arc"]]
            if dec_new != dec_base:
                events.append(dict(segment=seg, nit=int(state.nit),
                                   first_diff=next(
                                       i for i, (a, b) in enumerate(
                                           zip(dec_base, dec_new))
                                       if a != b)))
                seg_state["stop"] = True
                return True
            return False

        res = minimize(f_np, W, jac=g_np, method="trust-constr",
                       constraints=[lip_eq], callback=cb,
                       options=dict(gtol=gtol, xtol=xtol,
                                    maxiter=maxiter_per_seg,
                                    initial_tr_radius=0.05))
        nit_total += int(res.nit)
        W = np.asarray(res.x)
        result = res
        if res.status in (1, 2):
            if float(res.constr_violation) > gtol:
                raise RuntimeError("status-4-class: converged but "
                                   "infeasible (violation %.3e)"
                                   % res.constr_violation)
            break                            # converged inside stratum
        if res.status == 0 and not seg_state["stop"]:
            break                            # iteration budget exhausted
    return dict(W=W, res=result, n_segments=seg + 1,
                re_records=n_rec, re_record_events=events,
                nit_total=nit_total)


def geno_type2_reference(scratch):
    """Run GENO nozzle_type=2 on the reduced twin case (file
    exchange; GENO never modified) and read its wall."""
    ini = os.path.join(scratch, "input.ini")
    if not os.path.exists(ini):
        os.makedirs(scratch, exist_ok=True)
        shutil.copy(os.path.join(A1.GENO_DIR, "thermo",
                                 "thermo_CH4O2.dat"), scratch)
        shutil.copy(os.path.join(A1.GENO_DIR, "thermo", "raptor.plt"),
                    scratch)
        with open(ini, "w") as f:
            f.write("[GENO-nozzle]\nnozzle_type = 2\n"
                    "case_geom = axisymmetric\n"
                    "yt = %.1f\nrtu = %.1f\nrtd = %.2f\nda = %.3f\n"
                    "eps = %.1f\nxtronc = %.1f\n"
                    "thermoname = thermo_CH4O2.dat\n"
                    "frozenname = raptor.plt\nbackend = 0\n\n"
                    "[GENO-solver]\nNI = %d\nNe = %d\n"
                    % (TCASE["yt"], TCASE["rtu"], TCASE["rtd"],
                       TCASE["da_deg"], TCASE["eps"], TCASE["xtronc"],
                       TCASE["NI"], TCASE["Ne"]))
    if not os.path.exists(os.path.join(scratch, "dimensions.dat")):
        geno_bin = A1.win_to_wsl(os.path.join(A1.GENO_DIR, "bin",
                                              "GENO"))
        cmd = ("cd '%s' && export LD_LIBRARY_PATH="
               "/home/alessandro/miniconda3/envs/ct-env/lib && '%s' "
               "> solver.log 2>&1; echo rc=$?"
               % (A1.win_to_wsl(scratch), geno_bin))
        r = subprocess.run(["wsl.exe", "-e", "bash", "-lc", cmd],
                           capture_output=True, text=True, timeout=900)
        if "rc=0" not in r.stdout:
            raise RuntimeError("GENO type-2 run failed: %s"
                               % r.stdout[-400:])
    with open(os.path.join(scratch, "dimensions.dat"), "rb") as f:
        l, j2 = np.fromfile(f, dtype="<i4", count=2)
    l, j2 = int(l), int(j2)
    x = np.fromfile(os.path.join(scratch, "x.dat"),
                    dtype="<f8", count=j2 * l).reshape(j2, l)
    y = np.fromfile(os.path.join(scratch, "y.dat"),
                    dtype="<f8", count=j2 * l).reshape(j2, l)
    wx, wy = x[0, :], y[0, :]
    m = (wx > 0) & (wy > 0)
    wx, wy = wx[m], wy[m]
    keep = np.concatenate([[True], np.diff(wx) > 1e-14])
    return wx[keep], wy[keep]


def main():
    print("== BRICK 2 [X-TOCV]: variational TOC via dJ/dSigma + TR-SQP "
          "(JAX %s, SciPy trust-constr) ==" % jax.__version__)
    print("  (main() staged: S17 lands the engine + O3.1 + first "
          "optimization segment; see the S17 log for the staging "
          "declaration)")
    ok = True
    tab = A1.prep_tab(A1.build_tab_nasa())
    cfg = dict(NI=TCASE["NI"], Nw=NW, da_deg=TCASE["da_deg"],
               yt=TCASE["yt"], rtu=TCASE["rtu"], rtd=TCASE["rtd"],
               xtronc=TCASE["xtronc"])

    # INITIAL DESIGN = GENO-SEEDED (deviation history declared in the
    # S17 log: attempt 1 straight taper -> spline oscillation at the
    # attachment -> compression -> uncertified cell + NaN gradient;
    # attempt 2 analytic linear-angle taper from thB = 20 deg ->
    # characteristic focusing near the axis (MoC breakdown = the
    # SHOCK-FREE CLASS BOUNDARY: the ideal nozzle for eps = 4 has max
    # wall angle 11.44 deg — a 20 deg attachment over-turns): the
    # honest feasible seed is the GENO type-2 wall itself (reduced
    # twin case, feasible BY CONSTRUCTION). The discriminating
    # optimization test starts from a PERTURBED design instead — the
    # opt stage below.
    yL = TCASE["yt"] * np.sqrt(TCASE["eps"])
    Lx = TCASE["xtronc"]
    scratch2 = os.path.join(os.environ.get("TEMP", "/tmp"),
                            "a1_geno_toc_ni21")
    gwx, gwy = geno_type2_reference(scratch2)
    xg = np.linspace(0.05, 1.2, 400)
    sg = np.gradient(np.interp(xg, gwx, gwy), xg)
    thB0 = float(np.arctan(np.max(sg)))
    xB0 = TCASE["rtd"] * np.sin(thB0)
    xsn = xB0 + (Lx - xB0) * np.arange(1, M_NODES + 1) / M_NODES
    y0 = np.interp(xsn, gwx, gwy)
    y0[-1] = yL
    W0 = np.concatenate([[thB0], y0])
    print("  W0 GENO-seeded: thB = %.3f deg, lip y = %.4f"
          % (thB0 / d2r, yL))
    print("-- thermodynamic data guard (homenthalpic + homentropic) --")
    # instance data = the uniform Sauer IVL states (T, p from the
    # closure at the IVL speeds): must PASS at the machine floor;
    # a stratified profile (RDE-realistic) must be REJECTED. The
    # production wiring uses the measured Richardson band as
    # rel_band (declared); the staged demo uses the floor-only band.
    ta_n = A1.tab_arrays(tab)
    gm = tab["gammamedio"]
    alpha = np.sqrt(2.0 / ((gm + 1.0) * TCASE["rtu"] * TCASE["yt"]))
    yv = TCASE["yt"] * (1.0 - np.arange(TCASE["NI"]) / (TCASE["NI"] - 1.0))
    uv = tab["_as"] * (1.0 + alpha * 1e-6 + (gm + 1.0) * alpha**2
                       / 4.0 * yv**2)
    Tq, pq = A1.state_q(jnp.asarray(uv), ta_n)[:2]
    pts = jnp.stack([Tq, pq, jnp.asarray(uv), jnp.zeros_like(Tq)],
                    axis=1)
    g_ok = SC.inlet_admissibility(pts, ta_n, rel_band=0.0)
    print("  uniform IVL: spread_h0 %.2e (bound %.2e), spread_s %.2e "
          "(bound %.2e)" % (g_ok["spread_h0"], g_ok["bound_h0"],
                            g_ok["spread_s"], g_ok["bound_s"]))
    ok &= check("guard admits homenthalpic+homentropic data",
                g_ok["ok"])
    pts_bad = pts.at[: TCASE["NI"] // 2, 0].mul(1.001)  # stratified T
    g_bad = SC.inlet_admissibility(pts_bad, ta_n, rel_band=1e-6)
    ok &= check("guard REJECTS stratified (non-homenthalpic/entropic)"
                " data", not g_bad["ok"])

    print("-- record at W0 (adaptive, certified) --")
    t0 = time.perf_counter()
    out0, plan0 = run_toc_record(W0, tab, cfg)
    print("  record: %.1f s, %d cells, cert worst %.3e; wall pts %d"
          % (time.perf_counter() - t0, out0["cert_n"],
             out0["cert_worst"], out0["wall"].shape[0]))
    ok &= check("record certified (P4 gate)", out0["cert_worst"] <= 1.0)

    print("-- replay fidelity (RK-G monitor i) --")
    wall_sc = run_toc_scan(jnp.asarray(W0), tab, cfg, plan0)
    dev = float(jnp.max(jnp.abs(wall_sc - out0["wall"])))
    scale = float(jnp.max(jnp.abs(out0["wall"])))
    tol_rep = A1.NEWTON_TOL_FACTOR * EPS * scale * 10.0
    print("  max|scan - record| = %.3e (tol %.3e)" % (dev, tol_rep))
    ok &= check("replay fidelity at Newton floor", dev <= tol_rep)

    print("-- O3.1 on the TOC gradient chain --")
    def scalar_J(Wv):
        return thrust_J(run_toc_scan(Wv, tab, cfg, plan0), tab)

    Wj = jnp.asarray(W0)
    J0 = float(scalar_J(Wj))
    g = np.asarray(jax.grad(scalar_J)(Wj))
    v = np.asarray(np.random.default_rng(1)
                   .standard_normal(W0.shape[0]))
    v /= np.linalg.norm(v)

    def dirder(hsc):
        h = EPS ** (1.0 / 3.0) * hsc * max(1.0, float(np.abs(W0).max()))
        return (float(scalar_J(Wj + h * jnp.array(v)))
                - float(scalar_J(Wj - h * jnp.array(v)))) / (2 * h)

    d1, d2 = dirder(1.0), dirder(0.5)
    lhs, rhs = d2, float(g @ v)
    tol_dp = A1.K_RICH * (abs(d1 - d2)
                          + A1.C_FLOOR * EPS ** (2.0 / 3.0)
                          * max(abs(J0), 1.0))
    print("  J(W0) = %.6e;  FD dirder = %.10e  <g,v> = %.10e  "
          "|diff| = %.3e (tol %.3e)"
          % (J0, lhs, rhs, abs(lhs - rhs), tol_dp))
    ok &= check("O3.1 dot-product on dJ/dW", abs(lhs - rhs) <= tol_dp)
    # N1: corrupted gradient must break the identity
    gbad = g.copy()
    gbad[1] = -gbad[1]
    ok &= check("N1 corrupted gradient rejected",
                abs(d2 - float(gbad @ v)) > tol_dp)

    # ------------------------------------------------------------------
    # OPT STAGE (env A1_TOCV_OPT=1): TR-SQP from a PERTURBED feasible
    # start (the discriminating test: the gradient machinery must
    # RECOVER the Rao optimum, never copy it) + GENO oracle + O3
    # transversality instance. Staged separately for budget control.
    # ------------------------------------------------------------------
    if os.environ.get("A1_TOCV_OPT") == "1" and ok:
        print("-- OPT: TR-SQP (trust-constr, RK-G segmentation) --")
        rng = np.random.default_rng(7)
        Wp = W0.copy()
        # feasible perturbation: interior nodes only (lip pinned),
        # smooth bump ~1.5% of local y — inside the certified class
        bump = 0.015 * y0[:-1] * np.sin(
            np.pi * (xsn[:-1] - xB0) / (Lx - xB0))
        Wp[1:-1] = Wp[1:-1] + bump * rng.standard_normal(1)[0]
        J_seed = float(thrust_J(run_toc_scan(
            jnp.asarray(W0), tab, cfg, plan0), tab))
        # derived optimizer tolerances: gtol from the O3.1 FD noise
        # scale (the gradient is trustworthy down to tol_dp/|v| per
        # component), xtol from the Newton floor on W scale
        gscale = float(np.linalg.norm(g))
        gtol = max(tol_dp, 1e-8 * gscale)
        xtol = 1e-10
        t_opt = time.perf_counter()
        opt = run_trsqp(Wp, tab, cfg, yL, gtol=gtol, xtol=xtol)
        t_opt = time.perf_counter() - t_opt
        res = opt["res"]
        print("  segments %d, re-records %d, re-record events %s, "
              "nit %d, %.0f s" % (opt["n_segments"],
                                  opt["re_records"],
                                  opt["re_record_events"],
                                  opt["nit_total"], t_opt))
        print("  status %d (%s); KKT optimality %.3e (gtol %.3e); "
              "constr violation %.3e" % (res.status, res.message,
                                         res.optimality, gtol,
                                         res.constr_violation))
        ok &= check("TR-SQP converged in-stratum (P2-compliant "
                    "Verdict with re-record count)",
                    res.status in (1, 2)
                    and res.constr_violation <= gtol)
        # O3 transversality instance: KKT residual small = the Rao
        # stationarity reached VIA the gradient (executable opener of
        # the pre-registered O3.3 campaign — protocol untouched)
        ok &= check("O3 transversality instance (projected gradient "
                    "at optimum below derived tol)",
                    res.optimality <= 10.0 * gtol)
        W_star = opt["W"]
        J_star = float(thrust_J(run_toc_scan(
            jnp.asarray(W_star), tab, cfg,
            run_toc_record(W_star, tab, cfg)[1]), tab))
        print("  J(seed W0) = %.7e  J(perturbed start) -> J* = %.7e "
              "(dJ vs seed %.2e)" % (J_seed, J_star, J_star - J_seed))

        # GENO cross-code oracle: our optimum wall vs the GENO Rao
        # wall inside the derived two-resolution Richardson band
        print("-- OPT oracle: contour vs GENO type-2 (derived band) --")
        out_s, plan_s = run_toc_record(W_star, tab, cfg)
        cfg2 = dict(cfg)
        cfg2["NI"] = 2 * cfg["NI"] - 1
        cfg2["Nw"] = 2 * cfg["Nw"]
        out_s2, _ = run_toc_record(W_star, tab, cfg2)
        wx1 = np.asarray(out_s["wall"][:, 0])
        wy1 = np.asarray(out_s["wall"][:, 1])
        wx2 = np.asarray(out_s2["wall"][:, 0])
        wy2 = np.asarray(out_s2["wall"][:, 1])
        lo = max(wx1.min(), wx2.min(), gwx.min())
        hi = min(wx1.max(), wx2.max(), gwx.max())
        m = (wx1 >= lo) & (wx1 <= hi)
        e_rich = np.abs(wy1[m] - np.interp(wx1[m], wx2, wy2))
        band = A1.K_RICH * (e_rich + 64.0 * EPS * TCASE["yt"])
        err_g = np.abs(wy1[m] - np.interp(wx1[m], gwx, gwy))
        nbad = int(np.sum(err_g > band))
        print("  %d samples, out-of-band %d, max|dy| %.3e, max band "
              "%.3e, median err/band %.3f"
              % (int(m.sum()), nbad, err_g.max(), band.max(),
                 float(np.median(err_g / band))))
        ok &= check("optimum contour matches GENO Rao inside "
                    "derived band", nbad == 0)
        # N3: a shrunken-L design must NOT match (oracle discriminates)
        W_short = W_star.copy()
        W_short[1:] = W_star[1:] * 0.98
        W_short[-1] = yL
        try:
            out_n3, _ = run_toc_record(W_short, tab, cfg)
            err_n3 = np.abs(np.asarray(out_n3["wall"][:, 1])[m]
                            - np.interp(wx1[m], gwx, gwy))
            ok &= check("N3 oracle discriminates a wrong design",
                        int(np.sum(err_n3 > band)) > int(m.sum()) // 2)
        except RuntimeError:
            ok &= check("N3 oracle discriminates (wrong design "
                        "refuses to march)", True)

    print("VERDICT (staged%s): %s"
          % ("+opt" if os.environ.get("A1_TOCV_OPT") == "1" else "",
             "PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

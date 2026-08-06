#!/usr/bin/env python3
"""SCAN COLUMN ARCHITECTURE [F2/A1, session S17, brick-2 kickoff duty
(b)]: the brick-2 replay engine — each column's interior sweep driven
by jax.lax.scan over its cells (MoC columns are sequential chains: scan
is the correct primitive along a column; vmap stays available across
independent replays at fixed schedule). Registry ID: [X-SCANM].
Normative spec: docs/rde_nozzle_brick2_kickoff.md §3.

WHAT THIS IS: a REPLAY-mode engine only. Record mode stays the
adaptive Python march of [X-A1IM] (topology decisions are concrete by
construction — RK-G P2 lives there). This module consumes the recorded
schedule (decisions + cell seeds), reconstructs the march PLAN by
walking the exact [X-A1IM] control flow on the decision stream (no
floats needed: the flow depends only on decisions and cfg), and
replays the march with per-column scans. The scan body contains the
SAME implicit-solve custom_vjp cell (Newton inside, implicit rule for
the transpose): the Lemma B correspondence is untouched — cells are
driven by scan instead of Python dispatch.

COLUMN-ARRAY REPRESENTATION (derived in-session from the [X-A1IM]
grid indices, verified by the equivalence rejector):
  fan col i    = [head(IVL row NI+1-i)] + cells + [axis], length 2i-1;
                 the pt2 sequence of its cells is EXACTLY col_{i-1}
                 (head..axis), carry = previous new point.
  arc col      = concat([wall point], prev[rows 2..Nv] (void copy),
                 cells(rows Nv+1..j2), [axis(row j2+1)]);
                 'interp' attempts are solved, used only for the
                 traced interpolated wall angle, then discarded (the
                 recorded stream contains their cells — consumed
                 identically to the [X-A1IM] replay).
  straightening col = mach-line point (explicit) + downward scan of
                 cells to the RECORDED crossing row + traced crossing
                 interpolation for the wall streamline point + void
                 copy below; massflow accumulators traced.

EQUIVALENCE REGRESSION (rejector-grade, spec §3(iv)): on the reduced
twin case the scan replay must reproduce the [X-A1IM] Python replay
at the Newton floor (same schedule, same cells: the restructure may
not move a single number beyond roundoff), and O3.1 must hold on the
scan path with the same derived tolerance structure. NEGATIVE
CONTROLS: (N1) a mis-indexed plan (one pt2 gather shifted) must break
the equivalence check; (N2) a corrupted whole-march vjp must break
O3.1.

CLOSURE PLUGGABILITY: the cell residuals are rebuilt here with a
pluggable state closure (state_fn); with the [X-A1IM] linear closure
they are the SAME expressions on the same ta arrays (equivalence
case); the brick engine plugs the [X-THC1] C^1 closure — same
machinery, C^1 coefficients.

ON-DEMAND CARRIER (env: jax): outside the CI tiers by declaration,
like X-A1IM. Exit code 0 iff ALL checks pass INCLUDING the negative
controls.
"""
import os
import sys

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1  # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
d2r = np.pi / 180.0


# ======================================================================
# pluggable-closure residuals (same expressions as [X-A1IM], state_fn
# injected; with state_fn = A1.state_q on the same ta these are the
# identical computations)
# ======================================================================
def make_solvers(state_fn, delta_eff):
    def coef(u, v, y, ta):
        q = jnp.sqrt(u * u + v * v)
        A = jnp.arctan2(v, u)
        _, _, _, c, _, M = state_fn(q, ta)
        mu = jnp.arcsin(1.0 / M)
        lm = jnp.tan(A - mu)
        lp = jnp.tan(A + mu)
        qq = u * u - c * c
        s = delta_eff * c * c * v / y
        return lm, lp, qq, 2.0 * u * v, s

    def resid_int(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        um, vm, ym = 0.5 * (u1 + u4), 0.5 * (v1 + v4), 0.5 * (y1 + y4)
        lm, _, qm, rm0, sm = coef(um, vm, ym, ta)
        rm = rm0 - qm * lm
        up, vp, yp = 0.5 * (u2 + u4), 0.5 * (v2 + v4), 0.5 * (y2 + y4)
        _, lp, qp, rp0, sp = coef(up, vp, yp, ta)
        rp = rp0 - qp * lp
        return jnp.array([
            (y4 - y1) - lm * (x4 - x1),
            (y4 - y2) - lp * (x4 - x2),
            qm * u4 + rm * v4 - (sm * (x4 - x1) + qm * u1 + rm * v1),
            qp * u4 + rp * v4 - (sp * (x4 - x2) + qp * u2 + rp * v2),
        ])

    def resid_axi(z, p, ta):
        x4, u4 = z
        x1, y1, u1, v1 = p
        um, vm, ym = 0.5 * (u1 + u4), 0.5 * v1, 0.5 * y1
        lm, _, qm, rm0, sm = coef(um, vm, ym, ta)
        rm = rm0 - qm * lm
        return jnp.array([
            (0.0 - y1) - lm * (x4 - x1),
            qm * u4 - (sm * (x4 - x1) + qm * u1 + rm * v1),
        ])

    def resid_wal(z, p, ta):
        x2, u4 = z
        x1, y1, u1, v1, x3, y3, u3, v3, x4, y4, slope = p
        D = (x2 - x1) / (x3 - x1)
        y2 = y1 + D * (y3 - y1)
        u2 = u1 + D * (u3 - u1)
        v2 = v1 + D * (v3 - v1)
        v4 = slope * u4
        up, vp, yp = 0.5 * (u2 + u4), 0.5 * (v2 + v4), 0.5 * (y2 + y4)
        _, lp, qp, rp0, sp = coef(up, vp, yp, ta)
        rp = rp0 - qp * lp
        return jnp.array([
            (y4 - y2) - lp * (x4 - x2),
            (qp + slope * rp) * u4
            - (sp * (x4 - x2) + qp * u2 + rp * v2),
        ])

    def resid_leg(z, p, ta):
        (qe,) = z
        (target,) = p
        _, _, rho, _, _, _ = state_fn(qe, ta)
        return jnp.array([rho * qe - target])

    def resid_qme(z, p, ta):
        (q,) = z
        (Me,) = p
        return jnp.array([state_fn(q, ta)[5] - Me])

    mk = A1.make_implicit_solver
    return dict(interior=mk(resid_int), axis=mk(resid_axi),
                wall=mk(resid_wal), legge=mk(resid_leg),
                qofM=mk(resid_qme))


# ======================================================================
# plan reconstruction: walk the [X-A1IM] control flow on the recorded
# decision/seed streams (concrete integers/booleans only)
# ======================================================================
def build_plan(sched_d, cfg):
    NI, Ne = cfg["NI"], cfg["Ne"]
    dec = list(sched_d["dec"])
    zs = [np.asarray(z) for z in sched_d["z"]]
    di = zi = 0

    def next_dec():
        nonlocal di
        v = dec[di]
        di += 1
        return v

    def next_z(n):
        nonlocal zi
        v = zs[zi]
        assert v.shape == (n,), "seed stream shape mismatch"
        zi += 1
        return v

    plan = {}
    plan["q0"] = float(next_dec())
    plan["z_legge"] = next_z(1)

    # fan: col i has 2i-3 cells + axis
    fan = []
    for i in range(2, NI + 1):
        n = 2 * i - 3
        seeds = np.stack([next_z(4) for _ in range(n)])
        fan.append(dict(n=n, seeds=seeds, axis_seed=next_z(2)))
    plan["fan"] = fan

    # arc: attempted columns until 'exit'
    arc = []
    j2 = 2 * NI - 1
    Nv = 1
    n_arc = 0
    while True:
        n_arc += 1
        N, Nv_rec = next_dec()
        wall_seed = next_z(2)
        n = j2 - Nv_rec                      # cells j in [Nv+1, j2]
        seeds = np.stack([next_z(4) for _ in range(n)]) \
            if n else np.zeros((0, 4))
        axis_seed = next_z(2)
        code = next_dec()
        arc.append(dict(N=int(N), Nv=int(Nv_rec), j2=j2, n=n,
                        n_arc=n_arc, wall_seed=wall_seed, seeds=seeds,
                        axis_seed=axis_seed, code=code))
        Nv = int(Nv_rec)
        if code == "exit":
            j2 += 1
            break
        if code == "interp":
            continue                          # column discarded, j2 keeps
        j2 += 1                               # normal step
    plan["arc"] = arc
    plan["j2_exit"] = j2                      # rows 1..j2 in exit column
    plan["z_qme"] = next_z(1)

    # straightening: Ne-1 columns; crossing rows from 'crossed' decs
    stra = []
    for _ in range(Ne - 1):
        n = 0
        seeds = []
        while True:
            j = j2 - 1 - n                    # current row being solved
            assert j >= Nv, "straightening walked past Nv"
            seeds.append(next_z(4))
            n += 1
            if bool(next_dec()):
                break
        N_stop = j2 - n                       # crossing row
        stra.append(dict(n=n, N_stop=N_stop, Nv=Nv,
                         seeds=np.stack(seeds)))
        Nv = N_stop
    plan["stra"] = stra
    assert di == len(dec) and zi == len(zs), \
        "plan walker did not consume the full schedule (%d/%d dec, " \
        "%d/%d z)" % (di, len(dec), zi, len(zs))
    return plan


# ======================================================================
# the scan replay
# ======================================================================
def inlet_admissibility(pts_state, ta, rel_band, state_fn=None):
    """THERMODYNAMIC DATA GUARD (S17, user catch of record): the
    two-family (acoustic-only, Ch.16-twin) cells of this engine are
    EXACT only on HOMENTHALPIC + HOMENTROPIC data — uniform total
    enthalpy h0 AND uniform entropy s across the inlet profile; by
    Crocco (u x omega = grad h0 - T grad s) the pair is exactly the
    irrotationality of the S1 class. Stratified data (RDE-realistic
    per-phase interface profiles) carries per-streamline s/h0 and
    REQUIRES the three-family cell (streamline transport) — a NAMED
    ENGINE EXTENSION SLOT (kickoff doc §3 note; ledger channel c3),
    NOT something to march silently.

    ADMISSIBILITY CRITERION (derived, no magic): a spread is
    admissible iff its first-order field effect sits BELOW the
    march's own measured resolution band rel_band (two-resolution
    Richardson, contour-relative): sub-truncation non-uniformity is
    indistinguishable from uniform data at the certified resolution.
    First-order transfer: d(contour)/y ~ dq/q ~ dh0/q^2  =>
    h0 spread bound = rel_band * q_ref^2;  dp/p ~ ds/Rg  =>
    s spread bound = rel_band * Rg. Machine floor added for the
    exactly-uniform case.

    pts_state: (n, 4) array of per-point (T, p, u, v) PRIMITIVE data
    (independent per-point thermo — the case-C interface contract
    form). Returns dict(ok, spreads, bounds) — caller REJECTS on
    not ok."""
    Tg, hg, sg, cpg, Rg, h0_ref, s0_ref = ta
    T, p = pts_state[:, 0], pts_state[:, 1]
    q2 = pts_state[:, 2] ** 2 + pts_state[:, 3] ** 2
    h = jnp.interp(T, Tg, hg)
    s = jnp.interp(T, Tg, sg) - Rg * jnp.log(p / A1.PREF)
    h0 = h + 0.5 * q2
    q2ref = float(jnp.max(q2))
    d_h0 = float(jnp.max(h0) - jnp.min(h0))
    d_s = float(jnp.max(s) - jnp.min(s))
    floor_h0 = 100.0 * EPS * float(jnp.max(jnp.abs(h0)))
    floor_s = 100.0 * EPS * float(jnp.max(jnp.abs(s)))
    b_h0 = rel_band * q2ref + floor_h0
    b_s = rel_band * float(Rg) + floor_s
    return dict(ok=bool(d_h0 <= b_h0 and d_s <= b_s),
                spread_h0=d_h0, bound_h0=b_h0,
                spread_s=d_s, bound_s=b_s)


_SOLVER_CACHE = {}


def cached_solvers(key, state_fn, delta_eff):
    """Solver sets are cached by key: rebuilding them creates NEW jitted
    callables and forces a full XLA recompilation of every scan on
    every call (measured in-session: multi-GB, tens of minutes) —
    the cache is load-bearing, not an optimization."""
    if key not in _SOLVER_CACHE:
        _SOLVER_CACHE[key] = make_solvers(state_fn, delta_eff)
    return _SOLVER_CACHE[key]


def run_scan(P, tab, cfg, plan, state_fn=None, solvers=None):
    """Differentiable fixed-topology replay driven by per-column scans.
    Returns the same out-dict fields as [X-A1IM] run_march."""
    if state_fn is None:
        state_fn = A1.state_q
        if solvers is None:
            solvers = cached_solvers(("a1_linear", 1.0), state_fn, 1.0)
    ta = A1.tab_arrays(tab)
    if solvers is None:
        solvers = make_solvers(state_fn, 1.0)
    s_int, s_axi = solvers["interior"][0], solvers["axis"][0]
    s_wal, s_leg = solvers["wall"][0], solvers["legge"][0]
    s_qme = solvers["qofM"][0]

    NI, Ne, da = cfg["NI"], cfg["Ne"], cfg["da_deg"] * d2r
    yt, rtu, rtd, eps_ar = P[0], P[1], P[2], P[3]
    gm = tab["gammamedio"]
    delta = 1.0

    # ---------- IVL (identical to [X-A1IM])
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

    _, _, rho_ivl, _, _, _ = state_fn(u_ivl, ta)
    f_m = rho_ivl * u_ivl * y_ivl
    yy = y_ivl[::-1]
    ff = f_m[::-1]
    hgrid = yy[1] - yy[0]
    w = np.ones(NI)
    w[1:-1:2] = 4.0
    w[2:-1:2] = 2.0
    mdot = 2.0 * jnp.pi * hgrid / 3.0 * jnp.sum(jnp.array(w) * ff)

    # ---------- exit Mach from eps
    target = mdot / (jnp.pi * yt**2 * eps_ar)
    z = s_leg(jax.lax.stop_gradient(jnp.array(plan["z_legge"])),
              jnp.array([target]), ta)
    qe = z[0]
    Me = state_fn(qe, ta)[5]

    def cell_scan(solver, seeds, pt2s, carry0):
        seeds = jax.lax.stop_gradient(jnp.asarray(seeds))

        def body(carry, xs):
            seed, pt2 = xs
            zc = solver(seed, jnp.concatenate([carry, pt2]), ta)
            return zc, zc

        _, out = jax.lax.scan(body, carry0, (seeds, pt2s))
        return out

    def axis_solve(seed, pt1):
        zc = solvers["axis"][0](jax.lax.stop_gradient(jnp.array(seed)),
                                pt1, ta)
        return jnp.array([zc[0], 0.0, zc[1], 0.0])

    # ---------- fan
    prev = ivl[NI - 1][None, :]                      # col_1 = [axis IVL]
    for i, colp in enumerate(plan["fan"], start=2):
        head = ivl[NI - i][None, :]
        cells = cell_scan(s_int, colp["seeds"], prev, head[0])
        ax = axis_solve(colp["axis_seed"], cells[-1])
        prev = jnp.concatenate([head, cells, ax[None, :]], axis=0)

    # ---------- arc
    j2 = 2 * NI - 1
    flag_angle = None                                # traced after interp
    valid_wall = []
    for colp in plan["arc"]:
        n_arc, N, Nv = colp["n_arc"], colp["N"], colp["Nv"]
        if flag_angle is None:
            wall_angle = da * n_arc
        else:
            wall_angle = flag_angle
        x4 = rtd * jnp.sin(wall_angle)
        y4 = yt + rtd * (1.0 - jnp.cos(wall_angle))
        l0 = -x4 / (y4 - (rtd + yt))
        pt1 = prev[Nv]                               # row Nv+1
        pt3 = prev[N - 1]                            # row N
        p_w = jnp.concatenate([pt1, pt3, jnp.stack([x4, y4, l0])])
        zw = s_wal(jax.lax.stop_gradient(jnp.array(colp["wall_seed"])),
                   p_w, ta)
        u4 = zw[1]
        wall_pt = jnp.array([x4, y4, u4, l0 * u4])
        pt2s = prev[Nv: j2]                          # rows Nv+1..j2
        cells = cell_scan(s_int, colp["seeds"], pt2s, wall_pt) \
            if colp["n"] else jnp.zeros((0, 4))
        last = cells[-1] if colp["n"] else wall_pt
        ax = axis_solve(colp["axis_seed"], last)
        Max = state_fn(ax[2], ta)[5]

        if colp["code"] == "interp":
            # traced interpolated angle from THIS attempt + prev column
            prev_ax = prev[j2 - 1]                   # row j2 of prev col
            Mj2 = state_fn(jnp.sqrt(prev_ax[2]**2 + prev_ax[3]**2),
                           ta)[5]
            thw_i = jnp.arctan2(wall_pt[3], wall_pt[2])
            thw_p = jnp.arctan2(prev[0][3], prev[0][2])
            flag_angle = (thw_i - thw_p) / (Max - Mj2) * (Me - Mj2) \
                + thw_p
            continue                                 # column discarded

        new_col = jnp.concatenate(
            [wall_pt[None, :], prev[1:Nv], cells, ax[None, :]], axis=0)
        valid_wall.append(wall_pt)
        prev = new_col
        j2 += 1
        if colp["code"] == "exit":
            Me_ach = Max
            break

    # ---------- uniform-exit region
    z = s_qme(jax.lax.stop_gradient(jnp.array(plan["z_qme"])),
              jnp.array([Me_ach]), ta)
    qq = z[0]
    _, _, rexit, _, _, _ = state_fn(qq, ta)
    ye = jnp.sqrt(mdot / (jnp.pi * rexit * qq))
    K_pt = prev[j2 - 1]                              # row j2 (axis of exit)
    xe = K_pt[0] + ye * jnp.sqrt(Me_ach**2 - 1.0)
    dxe = (xe - K_pt[0]) / (Ne - 1.0)

    def rho_th(pt):
        q = jnp.sqrt(pt[2]**2 + pt[3]**2)
        _, _, r, _, _, _ = state_fn(q, ta)
        return r, jnp.arctan2(pt[3], pt[2]), q

    def massflow(pa, pb):
        ra, Aa, qa = rho_th(pa)
        rb, Ab, qb = rho_th(pb)
        dx = pb[0] - pa[0]
        dy = pb[1] - pa[1]
        fna = dy * jnp.cos(Aa) - dx * jnp.sin(Aa)
        fnb = dy * jnp.cos(Ab) - dx * jnp.sin(Ab)
        return jnp.pi * (ra * qa * fna * pa[1] + rb * qb * fnb * pb[1])

    mdot2 = jnp.float64(0.0)
    wall_str = []
    for colp in plan["stra"]:
        n, N_stop, Nv = colp["n"], colp["N_stop"], colp["Nv"]
        mach_prev = prev[j2 - 1]
        mach_new = jnp.array([mach_prev[0] + dxe,
                              mach_prev[1] + dxe
                              / jnp.sqrt(Me_ach**2 - 1.0),
                              qq, 0.0])
        mdot2 = mdot2 + massflow(mach_prev, mach_new)
        # pt2 sequence: rows j2-1 down to N_stop (row Nv -> prev wall)
        rows = np.arange(j2 - 1, N_stop - 1, -1)     # length n
        gat = jnp.stack([prev[0] if r == Nv else prev[r - 1]
                         for r in rows])
        cells = cell_scan(s_int, colp["seeds"], gat, mach_new)
        # massflow strips: pts above = [mach_new, cells[:-1]]
        above = jnp.concatenate([mach_new[None, :], cells[:-1]], axis=0)
        dms = jax.vmap(massflow)(above, cells)
        mdot1 = jnp.sum(dms)
        dm_last = dms[-1]
        D = (mdot - (mdot1 - dm_last + mdot2)) / dm_last
        pt_above = above[-1]
        w_pt = pt_above + D * (cells[-1] - pt_above)
        wall_str.append(w_pt)
        # new column: rows 1..j2: [wall, void copy rows 2..N_stop-1?,
        # ...]; referenced later: rows >= next N_stop' (>= N_stop) and
        # the wall row 1 -> assemble: [w_pt, prev[1:N_stop-1] void,
        # cells reversed (rows N_stop..j2-1), mach_new (row j2)]
        new_col = jnp.concatenate(
            [w_pt[None, :], prev[1:N_stop - 1],
             cells[::-1], mach_new[None, :]], axis=0)
        prev = new_col

    wall = valid_wall + wall_str
    wx = jnp.stack([p[0] for p in wall])
    wy = jnp.stack([p[1] for p in wall])
    return dict(wall_x=wx, wall_y=wy, Me=Me_ach, mdot=mdot,
                n_arc_cols=len(valid_wall), n_str_cols=len(wall_str))


# ======================================================================
# checks
# ======================================================================
def check(label, ok):
    print("  [%s] %s" % (label, "PASS" if ok else "FAIL"))
    return bool(ok)


def main():
    print("== SCAN COLUMN ARCHITECTURE [X-SCANM]: brick-2 replay engine "
          "(JAX %s) ==" % jax.__version__)
    ok = True
    tab = A1.prep_tab(A1.build_tab_nasa())
    P = jnp.array([A1.CASE["yt"], A1.CASE["rtu"], A1.CASE["rtd"],
                   A1.CASE["eps"]])
    cfg = dict(NI=A1.CASE["NI"], Ne=A1.CASE["Ne"],
               da_deg=A1.CASE["da_deg"])

    print("-- record (adaptive [X-A1IM] march) --")
    out_rec, sched = A1.run_march(P, tab, cfg)
    print("  contour: %d arc + %d streamline points; Me = %.6f; "
          "cert worst %.3e over %d cells"
          % (out_rec["n_arc_cols"], out_rec["n_str_cols"],
             float(out_rec["Me"]), out_rec["cert_worst"],
             out_rec["cert_n"]))
    ok &= check("record march certified", out_rec["cert_worst"] <= 1.0)

    print("-- plan reconstruction from the recorded schedule --")
    # wall seeds live in the z-stream: rebuild with wall seeds tagged.
    plan = build_plan(sched.d, cfg)
    n_int = (sum(c["n"] for c in plan["fan"])
             + sum(c["n"] for c in plan["arc"])
             + sum(c["n"] for c in plan["stra"]))
    print("  plan: %d fan cols, %d arc attempts (%d interp), %d "
          "straightening cols; %d interior cells total"
          % (len(plan["fan"]), len(plan["arc"]),
             sum(1 for c in plan["arc"] if c["code"] == "interp"),
             len(plan["stra"]), n_int))

    print("-- scan replay vs [X-A1IM] Python replay (equivalence) --")
    def f_py(Pv):
        o, _ = A1.run_march(Pv, tab, cfg, sched=sched)
        return jnp.concatenate([o["wall_x"], o["wall_y"],
                                jnp.array([o["Me"]])])

    def f_sc(Pv):
        o = run_scan(Pv, tab, cfg, plan)
        return jnp.concatenate([o["wall_x"], o["wall_y"],
                                jnp.array([o["Me"]])])

    base_py = f_py(P)
    base_sc = f_sc(P)
    scale = float(jnp.max(jnp.abs(base_py)))
    tol_eq = A1.NEWTON_TOL_FACTOR * EPS * scale * 10.0
    err_eq = float(jnp.max(jnp.abs(base_py - base_sc)))
    print("  max|scan - python| = %.3e (Newton-floor tol %.3e)"
          % (err_eq, tol_eq))
    ok &= check("scan replay == python replay at Newton floor",
                err_eq <= tol_eq)

    print("-- O3.1 dot-product on the scan path --")
    n_out = base_sc.shape[0]
    v = jnp.array([0.7, -0.4, 0.25, 0.5])
    wv = jnp.array([((-1.0) ** k) * (0.3 + 0.07 * (k % 11))
                    for k in range(n_out)])

    def dirder(hsc):
        h = EPS ** (1.0 / 3.0) * hsc
        return (f_sc(P + h * v) - f_sc(P - h * v)) / (2.0 * h)

    dv_h, dv_h2 = dirder(1.0), dirder(0.5)
    lhs = float(wv @ dv_h2)
    _, vjp_fn = jax.vjp(f_sc, P)
    (JTw,) = vjp_fn(wv)
    rhs = float(JTw @ v)
    tol_dp = A1.K_RICH * (abs(float(wv @ (dv_h - dv_h2)))
                          + A1.C_FLOOR * EPS ** (2.0 / 3.0) * scale)
    err_dp = abs(lhs - rhs)
    print("  [O3.1] <w,Jv> = %.10e  <J^Tw,v> = %.10e  |diff| = %.3e "
          "(tol %.3e)" % (lhs, rhs, err_dp, tol_dp))
    ok &= check("O3.1 dot-product on the scan path", err_dp <= tol_dp)

    print("-- negative controls --")
    # N1: mis-indexed plan (shift one straightening crossing row)
    import copy
    plan_bad = copy.deepcopy(plan)
    plan_bad["stra"][len(plan_bad["stra"]) // 2]["N_stop"] += 1
    plan_bad["stra"][len(plan_bad["stra"]) // 2]["n"] -= 1
    sb = plan_bad["stra"][len(plan_bad["stra"]) // 2]
    sb["seeds"] = sb["seeds"][:-1]
    try:
        base_bad = f_sc_bad = None
        o_bad = run_scan(P, tab, cfg, plan_bad)
        base_bad = jnp.concatenate([o_bad["wall_x"], o_bad["wall_y"],
                                    jnp.array([o_bad["Me"]])])
        dev = float(jnp.max(jnp.abs(base_bad - base_py)))
        print("  [N1] mis-indexed plan deviation = %.3e (floor %.3e)"
              % (dev, tol_eq))
        ok &= check("N1 mis-indexed plan rejected by equivalence",
                    dev > tol_eq)
    except Exception as e:                            # noqa: BLE001
        print("  [N1] mis-indexed plan REFUSES to replay (%s)"
              % type(e).__name__)
        ok &= check("N1 mis-indexed plan rejected (refusal)", True)

    # N2: corrupted whole-march vjp
    rhs_c = float((JTw * (1.0 + 1e-5)
                   + 1e-5 * jnp.max(jnp.abs(JTw))) @ v)
    ok &= check("N2 corrupted scan vjp rejected",
                abs(lhs - rhs_c) > tol_dp)

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""A1 BRICK 2, STEP 9b [F2/A1]: THE PLUG MARCH — assembly of the plug
topology from certified cells, with a march-level EXACT known answer.

TOPOLOGY (the bell, mirrored): columns march downstream at the
PRESCRIBED stations; each column is swept BOTTOM-UP:
  row 1      = SPIKE WALL (prescribed station, solved by the C- mirror
               of the certified inverse-wall cell with a MULTI-COLUMN
               FOOT SEARCH — the bell wall uses the C+ family from
               below; a bottom wall receives C- from above),
  rows 2..M  = interior cells (bottom-up mirror of Brick 1's),
  row M+1    = FREE JET EDGE (step 9a's certified cell: p = pa,
               position solved), fed from ITS OWN column.
Row bookkeeping, one characteristic at a time at both boundaries:
the edge ADDS one row per column (the widening jet gains a crossing;
the bell's j2 += 1 mirrored) and the wall CONSUMES the previous
column's rows below the new foot (their C- terminated on the wall
between stations; prolonging them creates ghost rows below the spike
whose only remaining Newton root is the backward, wrong-branch
crossing — measured: an M1-state mesh limb below the wall, mass +9%).

MARCH-LEVEL ORACLE (planar simple-wave twin, gconst tables). Uniform
flow at M1 meets a corner at the cowl lip with ambient pa = p(M2): the
exact field is (uniform M1) U (centered Prandtl-Meyer fan at the lip)
U (uniform M2 turned by dnu), all closed-form for a calorically
perfect gas. The prescribed "spike" is the EXACT STREAMLINE of that
field through the throat's lower point (fine-step RK4 integration of
the closed-form field, 1e-10 grade — an independent reference, not an
MOC). The marched solution must reproduce:
  P-1  the edge: asymptotic angle = dnu and speed = q(M2) within
       Richardson bands (station-halving),
  P-2  the wall pressure distribution along the spike vs the exact
       simple-wave pressure at each station,
  P-3  mass conservation: flux through the last column = start-line
       flux (per unit depth),
  P-4  momentum closure: exit-column flux = start flux + spike
       pressure push, with the FREE EDGE contributing exactly zero in
       the pa gauge (p = pa on it — the plug's defining property),
  R-1  rejector: corrupted ambient (qpa * 1.01) leaves the P-1 band,
  R-2  rejector: corrupted spike slopes fail to march or leave bands.

STAGE=axi: the same assembly in axisymmetric mode on the real-gas
tables (smoke + internal closures P-3/P-4; the external plug referee
— GENO's RaoPlug — is deferred until its S1/S2 fix, declared).

Run:  .venv-a1/bin/python validation/a1_plug_march.py
      STAGE=axi .venv-a1/bin/python validation/a1_plug_march.py
"""
import os
import sys
import time

import collections
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
import a1_thrust_functional as TF            # noqa: E402
from a1_freejet_unit import (make_resid_freejet, q_at_pa)  # noqa: E402

import jax                                    # noqa: E402
import jax.scipy.special                       # noqa: E402,F401
import jax.numpy as jnp                       # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# the bottom-wall (spike) cell: C- mirror of the inverse-wall cell
# ----------------------------------------------------------------------
def make_resid_wallbot(delta):
    """Foot parameterized by y (z = (y2, u4)): the chord between the
    previous wall point and the interior above it is VERTICAL on the
    start line, so an x-parameterized foot divides by zero there —
    found by the cert localizer at ('wall', 1) on the fine grid; the
    chord is never horizontal near a bottom wall, so y is the robust
    parameter."""
    def resid(z, p, ta):
        y2, u4 = z
        xA, yA, uA, vA, xB, yB, uB, vB, x4, y4, slope = p
        D = (y2 - yA) / (yB - yA)
        x2 = xA + D * (xB - xA)
        u2 = uA + D * (uB - uA)
        v2 = vA + D * (vB - vA)
        v4 = slope * u4
        um, vm = 0.5 * (u2 + u4), 0.5 * (v2 + v4)
        ym = 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = A1._coef(um, vm, ym, ta, delta)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y2) - lm * (x4 - x2),
            (qm + slope * rm) * u4
            - (sm * (x4 - x2) + qm * u2 + rm * v2),
        ])
    return resid


# ----------------------------------------------------------------------
# the top-wall (SHROUD) cell: a DIRECT wall cell (2026-09-24, the shrouded
# plug; additive -- without `shroud=` the march below is bit-identical)
# ----------------------------------------------------------------------
def make_resid_walltop(delta):
    """The column's C+ from pt1 (BELOW, same column) meets the prescribed
    shroud: unknowns z = (x4, u4); the shroud's local shape is the cubic
    Hermite through the two bracketing stations (xA, yA, sA)-(xB, yB, sB)
    (the segment is a recorded decision), so y4 = H(x4) and v4 = H'(x4) u4.
    The bell's wall is INVERSE (station given, foot searched) because a
    top-down column ends ON the wall station; here the column is a C+
    line and the wall point is wherever it arrives (GENO's DirectWall).
    Rows: C+ position, C+ compatibility -- the inwall rows with the foot
    fixed at pt1."""
    def resid(z, p, ta):
        x4, u4 = z
        x1, y1, u1, v1, xA, yA, sA, xB, yB, sB = p
        h = xB - xA
        t = (x4 - xA) / h
        y4 = ((2.0 * t ** 3 - 3.0 * t ** 2 + 1.0) * yA
              + (t ** 3 - 2.0 * t ** 2 + t) * h * sA
              + (-2.0 * t ** 3 + 3.0 * t ** 2) * yB
              + (t ** 3 - t ** 2) * h * sB)
        s4 = ((6.0 * t ** 2 - 6.0 * t) * (yA - yB) / h
              + (3.0 * t ** 2 - 4.0 * t + 1.0) * sA
              + (3.0 * t ** 2 - 2.0 * t) * sB)
        v4 = s4 * u4
        up, vp, yp = 0.5 * (u1 + u4), 0.5 * (v1 + v4), 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = A1._coef(up, vp, yp, ta, delta)
        rp = rp0 - qp * lp
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            qp * u4 + rp * v4 - (sp * (x4 - x1) + qp * u1 + rp * v1),
        ])
    return resid


def margin_of_corners(cA, cB, cC, cD, mask, mg):
    """The fold margin of every cell from its four corners (n, 2) each --
    the signed area over the mean legs floored at ell2, orient-signed;
    padded cells masked to +inf. The ONE formula of the vectorised margin
    (S34), shared by the march's record/replay and the wavefront replay
    (S41) so that both aggregate the same numbers in the same order."""
    xs = jnp.stack([cA[:, 0], cB[:, 0], cC[:, 0], cD[:, 0]], axis=1)
    ys = jnp.stack([cA[:, 1], cB[:, 1], cC[:, 1], cD[:, 1]], axis=1)
    area = 0.5 * jnp.sum(xs * jnp.roll(ys, -1, axis=1)
                         - jnp.roll(xs, -1, axis=1) * ys, axis=1)
    lp = 0.5 * (jnp.hypot(cB[:, 0] - cA[:, 0], cB[:, 1] - cA[:, 1])
                + jnp.hypot(cC[:, 0] - cD[:, 0], cC[:, 1] - cD[:, 1]))
    lm = 0.5 * (jnp.hypot(cD[:, 0] - cA[:, 0], cD[:, 1] - cA[:, 1])
                + jnp.hypot(cC[:, 0] - cB[:, 0], cC[:, 1] - cB[:, 1]))
    v = mg["orient"] * area / jnp.maximum(lp * lm, mg["ell2"])
    if mask is not None:
        v = jnp.where(mask, v, jnp.inf)
    return v


def hermite_seg(x, xA, yA, sA, xB, yB, sB):
    """(y, dy/dx) of the cubic Hermite segment -- the shroud's local shape
    the top cell solves against (numpy or jnp, elementwise)."""
    h = xB - xA
    t = (x - xA) / h
    y = ((2.0 * t ** 3 - 3.0 * t ** 2 + 1.0) * yA + (t ** 3 - 2.0 * t ** 2 + t) * h * sA
         + (-2.0 * t ** 3 + 3.0 * t ** 2) * yB + (t ** 3 - t ** 2) * h * sB)
    dy = ((6.0 * t ** 2 - 6.0 * t) * (yA - yB) / h + (3.0 * t ** 2 - 4.0 * t + 1.0) * sA
          + (3.0 * t ** 2 - 2.0 * t) * sB)
    return y, dy


def make_resid_interior_bu(delta):
    """Bottom-up interior cell (the mirror of Brick 1's): pt1 sits
    BELOW in the SAME column and sends the C+ characteristic; pt2 sits
    on the PREVIOUS column at the same row and sends the C-. (Brick 1's
    top-down cell is the transpose: C- within-column, C+ across.)"""
    def resid(z, p, ta):
        x4, y4, u4, v4 = z
        x1, y1, u1, v1, x2, y2, u2, v2 = p
        up, vp, yp = 0.5 * (u1 + u4), 0.5 * (v1 + v4), 0.5 * (y1 + y4)
        _, lp, qp, rp0, sp = A1._coef(up, vp, yp, ta, delta)
        rp = rp0 - qp * lp
        um, vm, ym = 0.5 * (u2 + u4), 0.5 * (v2 + v4), 0.5 * (y2 + y4)
        lm, _, qm, rm0, sm = A1._coef(um, vm, ym, ta, delta)
        rm = rm0 - qm * lm
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            (y4 - y2) - lm * (x4 - x2),
            qp * u4 + rp * v4 - (sp * (x4 - x1) + qp * u1 + rp * v1),
            qm * u4 + rm * v4 - (sm * (x4 - x2) + qm * u2 + rm * v2),
        ])
    return resid


def mach_np(q, ta_np):
    """state_q's Mach number by numpy on host copies of the tables (the
    seed predictors' need; S41 fast lane)."""
    Tg, hg, sg, cpg, Rg, h0, s0 = ta_np
    T = np.interp(h0 - 0.5 * q * q, hg, Tg)
    cp = np.interp(T, Tg, cpg)
    gam = cp / (cp - Rg)
    return q / np.sqrt(gam * Rg * T)


def predict_bu(pt1, pt2, ta, ta_np=None):
    """Seed for the bottom-up interior cell: straight-line crossing of
    the foot-state characteristics, averaged state."""
    x1, y1, u1, v1 = (float(v) for v in pt1)
    x2, y2, u2, v2 = (float(v) for v in pt2)
    if ta_np is not None:
        M1_, M2_ = mach_np(np.hypot(u1, v1), ta_np), mach_np(np.hypot(u2, v2), ta_np)
    else:
        M1_ = float(A1.state_q(jnp.float64(np.hypot(u1, v1)), ta)[5])
        M2_ = float(A1.state_q(jnp.float64(np.hypot(u2, v2)), ta)[5])
    mu1 = np.arcsin(min(1.0, 1.0 / max(M1_, 1.0001)))
    mu2 = np.arcsin(min(1.0, 1.0 / max(M2_, 1.0001)))
    th1, th2 = np.arctan2(v1, u1), np.arctan2(v2, u2)
    sp = np.tan(th1 + mu1)
    sm = np.tan(th2 - mu2)
    x4 = (y2 - y1 + sp * x1 - sm * x2) / (sp - sm)
    y4 = y1 + sp * (x4 - x1)
    return jnp.array([x4, y4, 0.5 * (u1 + u2), 0.5 * (v1 + v2)])


# ----------------------------------------------------------------------
# the plug march
# ----------------------------------------------------------------------
def plug_march(stations, start, qpa, tab, delta, sched=None,
               consume=True, cells=None, q_edge=None,
               edge_fill=0, rot_pred=None, margin=None, x_traced=False,
               shroud=None, wedge_every=1, fast=False, graph=None):
    """stations = (sx, sy, ssl) spike wall stations (K,), downstream of
    the start line. start = (x0, ys, us, vs) start-line states (row 1 =
    wall/bottom ... row N = edge/top), e.g. the exact corner-fan field
    on a vertical cut — the corner itself lives in the DATA, exactly as
    Brick 1's throat corner lives in its initialExpansion fan; ordinary
    cells cannot jump a centered wave (measured: cert 8.9e9 when they
    were asked to — the restructure of record). consume=False disables
    the wall-side row consumption (diagnostic only: reproduces the
    measured ghost-limb regression the mass check caught).
    cells (optional) = (t_int, t_fj, t_wb) solver triples that swap
    the three cell processes while keeping this driver's certified
    control flow (the swirl extension's seam); q_edge (optional) =
    the edge speed law y -> q (default: the constant qpa; the swirl
    edge carries q_m(y) = sqrt(qpa_tot^2 - Gamma^2/y^2)).
    ROTATIONAL SEAM (S24, additive): when `start` carries SIX rows
    (x0, ys, us, vs, ss, h0s) the march runs with 6-wide nodes
    (x, y, u, v, s, h0) — per-streamline entropy and stagnation
    enthalpy, the general (rotational) inlet. The wall and the free
    edge are streamlines, so their invariants are the bottom/top
    start-row constants, appended by this driver; INTERIOR cells
    return z = (x4, y4, u4, v4, t) with t the streamline-foot
    parameter on the chord pt1-pt2, and this driver stores the node
    with invariants lerped at t. `cells` must then be the rotational
    triple (the carrier's), `q_edge` the constant edge-speed law from
    the edge row's own invariants, and `rot_pred` the interior seed
    predictor. With 4-wide start data every branch below reproduces
    the certified path bit-for-bit (gated).
    edge_fill (int): rows to insert in the FIRST marched column
    between its topmost interior point and the free edge. A column is
    a characteristic while a vertical start line is not, so the first
    column alone opens a wedge there that no cell computes --- MEASURED
    on the plug worlds: gap 0.99 m (rising) and 1.31 m (descending),
    26x and 39x the mean row spacing, against 0.5-1.0x for EVERY other
    column. Mass jumps once, in that column, and is flat thereafter.
    FOLD MARGIN (S29 2026-09-16, additive; [X-PMRG]): margin = dict(
    rho, mu0, m_ref, orient, f_edge, jmin, ell2) switches on the
    in-loop fold margin of M0 Part VI — the signed area of the net's
    TRUE cell (jprev-1, i-1), (jprev, i-1), (jnew, i), (jnew-1, i),
    measured as each interior point is solved (all four corners are
    in G at that moment), over the product of the mean C+ and C-
    legs FLOORED at ell2 (the station spacing squared: a fold counts
    when its inverted cells are resolved, the criterion tightens
    under refinement), orient-signed so that healthy = +sin 2 alpha,
    zero = same-family coalescence, negative = a fold; aggregated
    ONLINE by KS with logaddexp (no mesh stack: the S23 compile
    lesson) over the bucket rows_from_top > f_edge * (rows in the
    column) (the thin row-growth cells at the free jet excluded,
    f_edge derived by the carrier). Returned as margin_ks (traced in
    play mode: differentiable through the replay), margin_min,
    margin_n. Without margin every path below is bit-identical
    (gated by the carrier's D0 check).
    x_traced (throat posing, 2026-09-23; default False: unchanged): the
    station abscissae are DESIGN outputs, not frozen data -- a wall
    posed at fixed record-frame abscissae is marched in a rotated frame,
    where its stations' x' move with the design. Station kst is then
    (sx[kst], sy[kst], ssl[kst]) in both modes (traced in play), the
    schedule keeping only the discrete decisions; the recorded "xcols"
    are the record's own abscissae (a diagnostic, not read back).
    SHROUD (2026-09-24, additive; the shrouded / internal-external plug):
    shroud = (xs, ys, ss) stations of a TOP wall from the start line to
    its lip F = (xs[-1], ys[-1]). The top of every column is then the
    DIRECT top-wall cell (make_resid_walltop) instead of the free jet:
    the column's C+ meets the shroud on the Hermite segment the recorded
    scan brackets; the shroud, like the edge, ADDS one row per column
    (the reflected C-). When the column's C+ would land beyond F, the
    lip is placed by the bell's INVERSE wall cell (A1.make_resid_inwall,
    verbatim) with its foot on the C- leg from the previous shroud point
    to this column's top interior; after F no top cell runs -- the top
    row IS F's C- (the exit characteristic), rows are only consumed at
    the plug, and the march ends when that row reaches the plug or at
    the last station. No free jet, no pa: the region above F's C- is not
    computed. Returns out["shroud"] (the shroud points, F last) and
    out["lip_col"]; out["edge"] is None. Not combined with `cells`
    (rotated frame) or 6-wide nodes. wedge_every (int, default 1) launches
    a wedge column from every m-th start row (the plug's start row always
    included): with one per row the N-1 reflections off the shroud crowd
    into the wedge's short x-range and travel downstream as a C- band 25x
    denser than the rest of the net, degrading the plug-wall cell's
    certificate where the band lands (measured, (280,61) on Migdal); the
    rows a thinned wedge skips take their C- partner from the start line.
    A DESIGNED shroud (S40, [X-TWOP]) passes traced heights and slopes in
    the replay (play mode) only; the record needs concrete stations for
    its bracketing scan.
    fast (S41 2026-09-26, additive; default False = every path below
    unchanged): the RECORD lane's overheads removed -- one fused dispatch
    per cell (solve_cert: the Newton solve and its certificate, the
    VERBATIM step_norm expression, M5a) instead of the custom_vjp wrapper
    plus a second dispatch, and the seed predictors' Mach numbers by numpy
    on host copies of the tables instead of eager state_q calls (a profile
    of the (140,31) record march: 62 percent in predict_bu's two state_q
    calls, 30 percent in the custom_vjp wrapper). The seeds may differ in
    their last bits from the eager path (np.interp vs jnp.interp): the
    converged cells are graded bitwise by the carrier that opts in.
    graph (S41, additive; record mode, 4-wide shroud posing): a dict the
    record fills with the march's DATAFLOW -- every cell's kind, output
    key, input keys, static indices and schedule index, the wedge aliases,
    the ordered wall and shroud outputs and the margin quads' corner keys
    -- for a1_wavefront_replay, which re-executes the frozen schedule by
    anti-diagonal batches (the independent cells of a level in one
    vmapped solve) instead of cell by cell.
    Returns out + sched."""
    ta = A1.tab_arrays(tab)
    if fast and cells is not None:
        raise NotImplementedError("fast: the record-frame 4-wide cells only")
    ta_np = tuple(np.asarray(a, float) for a in ta) if fast else None
    S = A1.Sched("rec") if sched is None else A1.Sched("play", sched.d)
    sx, sy, ssl = stations
    if len(start) == 6:
        x0, ys0, us0, vs0, ss0, h00 = start
        NV = 6
    else:
        x0, ys0, us0, vs0 = start
        ss0 = h00 = None
        NV = 4
    N = len(ys0)
    if graph is not None:
        if S.mode != "rec" or NV == 6 or cells is not None or shroud is None:
            raise NotImplementedError("graph: the record of the 4-wide shroud posing only")
        graph.update(cells=[], alias={}, wall_out=[], shroud_out=[], quads=[], N=N, x_traced=bool(x_traced))

    if cells is None:
        t_int = A1.get_solver(("intbu", delta),
                              lambda: make_resid_interior_bu(delta))
        t_fj = A1.get_solver(("fj", False, delta),
                             lambda: make_resid_freejet(delta))
        t_wb = A1.get_solver(("wb", delta),
                             lambda: make_resid_wallbot(delta))
    else:
        t_int, t_fj, t_wb = cells
    qe_of = (lambda yy: qpa) if q_edge is None else q_edge

    def with_ta(t):
        return (lambda z0, p: t[0](z0, p, ta),
                lambda z, p: t[2](z, p, ta),
                (lambda z0, p: t[3](z0, p, ta)) if len(t) > 3 else None)
    s_int, s_fj, s_wb = with_ta(t_int), with_ta(t_fj), with_ta(t_wb)
    if shroud is not None:
        if cells is not None or NV == 6:
            raise NotImplementedError("shroud: record-frame 4-wide nodes only")
        try:
            sxs, sys_, sss = (np.asarray(v, float) for v in shroud)
        except jax.errors.TracerArrayConversionError:
            # a DESIGNED shroud (S40 2026-09-24, [X-TWOP]; additive: a
            # concrete shroud takes the numpy path above, bit-identical):
            # its heights and slopes are traced in the replay, which reads
            # the stations only at the recorded segment indices -- the
            # bracketing scan (floats) runs in the record alone
            if S.mode == "rec":
                raise ValueError("a traced shroud is replayed, never recorded")
            sxs, sys_, sss = (jnp.asarray(v) for v in shroud)
        if isinstance(sxs, np.ndarray) and np.any(np.diff(sxs) <= 0.0):
            raise ValueError("shroud stations must increase in x")
        s_wt = with_ta(A1.get_solver(("wt", delta), lambda: make_resid_walltop(delta)))
        s_lip = with_ta(A1.get_solver(("wtlip", delta), lambda: A1.make_resid_inwall(delta)))
        lip_done = [False]
        shroud_pts = []
        lip_col = [None]
    cert = dict(worst=0.0, n=0, where=None)
    # region R (S34): the Newton certificate read where the thrust is
    # made -- per-cell ratios kept, the worst over R taken at the end
    cert_cells = [] if (margin is not None and margin.get("region") == "R") else None
    _tag = [None]
    # fold margin accumulators (see the docstring; None = off)
    mg = margin
    m_acc = [None]                 # logaddexp accumulator of -rho*m
    m_min = [None]
    m_n = [0]

    def cell_margin(pA, pB, pC, pD):
        """signed area of the quad A->B->C->D over the mean legs;
        A=(jprev-1,i-1) B=(jprev,i-1) C=(jnew,i) D=(jnew-1,i)."""
        xs = jnp.stack([pA[0], pB[0], pC[0], pD[0]])
        ys = jnp.stack([pA[1], pB[1], pC[1], pD[1]])
        area = 0.5 * jnp.sum(xs * jnp.roll(ys, -1)
                             - jnp.roll(xs, -1) * ys)
        lp = 0.5 * (jnp.hypot(pB[0] - pA[0], pB[1] - pA[1])
                    + jnp.hypot(pC[0] - pD[0], pC[1] - pD[1]))
        lm = 0.5 * (jnp.hypot(pD[0] - pA[0], pD[1] - pA[1])
                    + jnp.hypot(pC[0] - pB[0], pC[1] - pB[1]))
        # resolution-consistent: legs below the station spacing
        # cannot carry a resolved fold (ell2 derived by the caller)
        return area / jnp.maximum(lp * lm, mg["ell2"])

    # VECTORISED margin (S34, additive): margin["vec"] = True collects
    # the four corners of every bucket cell during the march and
    # evaluates the SAME field and the SAME KS aggregate once, on
    # stacked arrays, after it (logsumexp instead of the online
    # logaddexp chain: equal to rounding). Measured on the Humphreys
    # posing (81,41), 3930 cells: the in-loop form costs 173 s per
    # value-and-gradient against 13 s for the objective -- a chain of
    # ~4000 eager logaddexp/hypot ops and their adjoints. The stack is
    # eager (no jit), so the S23 compile trap does not apply.
    m_quads = []

    def margin_acc(mval):
        m_n[0] += 1
        v = mg["orient"] * mval
        m_min[0] = v if m_min[0] is None else jnp.minimum(m_min[0], v)
        e = -mg["rho"] * v
        m_acc[0] = e if m_acc[0] is None else jnp.logaddexp(m_acc[0], e)

    def certify(stepfn, z, p, step=None):
        if S.mode != "rec":
            return
        if step is None:
            step = float(stepfn(z, jnp.asarray(p)))
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        r = step / (A1.NEWTON_TOL_FACTOR * EPS * sc)
        if r > cert["worst"]:
            cert["worst"], cert["where"] = r, _tag[0]
        cert["n"] += 1
        if cert_cells is not None:
            cert_cells.append((r, _tag[0]))

    def cell(solver, p, z0, tag=None):
        _tag[0] = tag
        p = jnp.asarray(p)
        if fast and S.mode == "rec" and solver[2] is not None:
            # the fused record entry: the same Newton, the same step
            # metric, one dispatch; the schedule records z as Sched.cell does
            z, step = solver[2](jnp.asarray(z0), p)
            S.d["z"].append(np.asarray(z))
            certify(solver[1], z, p, step=float(step))
            return z
        z = S.cell(solver[0], p, z0)
        certify(solver[1], z, p)
        return z

    # start line: row 1 = WALL (bottom) ... row M0 = EDGE (top);
    # the mesh GROWS one row per column (the bell's j2 += 1, mirrored):
    # each column is a wall-to-edge characteristic, and the widening
    # jet gets its extra crossing as an extra row — the fix for the
    # measured fixed-row tangling.
    # x0 may be a SCALAR (a vertical cut, the historical posing) or an
    # ARRAY of per-row stations, which lets the caller pose the start
    # data ALONG A CHARACTERISTIC. That matters: a march column IS a
    # characteristic, so a vertical start line forces the first column
    # to bridge from vertical to characteristic geometry, and the free
    # edge takes one enormous step to get there (measured on the
    # configuration-comparison world: the edge advanced 2.35 m in a
    # single chord and leaked 1.45% of the mass, once, in the first
    # column). Posing the start on a characteristic removes the
    # transition entirely.
    x0a = np.atleast_1d(np.asarray(x0, dtype=float))
    if x0a.size == 1:
        x0a = np.full(N, float(x0a[0]))
    G = {}
    for j in range(1, N + 1):
        row = [float(x0a[j - 1]), float(ys0[j - 1]),
               float(us0[j - 1]), float(vs0[j - 1])]
        if NV == 6:
            row += [float(ss0[j - 1]), float(h00[j - 1])]
        G[(j, 1)] = jnp.array(row)
    # REGION R (S34, additive; margin["region"] == "R"): Humphreys'
    # region R -- the domain the contour influences, below the exit C-
    # DB -- read TOPOLOGICALLY on the net: every point carries the id of
    # its C- line (rows are C- lines, re-indexed at the wall), a line
    # ends when the wall consumes it, and the lines still ALIVE in the
    # last column pass above the tip D, i.e. above DB. A cell whose lower
    # C- leg (or wall corner) is on a consumed line is in R.
    track_R = mg is not None and mg.get("region") == "R"
    cline = {(j, 1): j for j in range(2, N + 1)} if track_R else None
    new_line = [N + 1]
    m_qkeys = []
    if NV == 6:
        # wall and edge are STREAMLINES: their invariants are the
        # bottom/top start-row constants for the whole march.
        sw_inv = jnp.array([float(ss0[0]), float(h00[0])])
        se_inv = jnp.array([float(ss0[-1]), float(h00[-1])])

    # MULTI-COLUMN FOOT SEARCH (the fix for the third measured lesson,
    # replacing the characteristic pacing). The wall receives the C-
    # family; the earlier scheme confined its foot to the FIRST
    # segment of the previous column (previous wall -> first interior)
    # and therefore had to PACE the columns (dx = row_gap/|lm|, clamped
    # at 0.30) so the foot stayed there — and the 0.30-long chords
    # crossing the fan gradient biased the midpoint closure (measured:
    # wall speeds high, pressures low, 55% of stations in band). Now
    # the march runs at the PRESCRIBED stations (fine columns) and the
    # wall cell searches the WHOLE previous column — stepping further
    # columns back if needed — for the segment that BRACKETS its
    # arriving characteristic, exactly like the bell's wall_search.
    # Chords shrink from the 0.30 clamp to the station spacing.
    def foot_lm(pt, u4_est, sl):
        """Estimated C- slope at a stored point, toward wall state.
        Bracket HEURISTIC only (a recorded decision, never a
        residual): for 6-wide nodes the Mach comes from the node's
        own h0 (T from the h-table at ht = h0 - q^2/2; entropy is
        not needed for M), else from the certified global closure."""
        u_, v_ = float(pt[2]), float(pt[3])
        um = 0.5 * (u_ + u4_est)
        vm = 0.5 * (v_ + sl * u4_est)
        q_ = float(np.hypot(um, vm))
        if NV == 6:
            Tg, hg, sg, cpg, Rg, _, _ = ta
            ht = float(pt[5]) - 0.5 * q_ * q_
            T_ = float(jnp.interp(ht, hg, Tg))
            cp_ = float(jnp.interp(T_, Tg, cpg))
            gam_ = cp_ / (cp_ - float(Rg))
            c_ = float(np.sqrt(gam_ * float(Rg) * T_))
            Mm = q_ / c_
        else:
            Mm = float(A1.state_q(jnp.float64(q_), ta)[5])
        mum = float(np.arcsin(min(1.0, 1.0 / max(Mm, 1.0001))))
        thm = float(np.arctan2(vm, um))
        return np.tan(thm - mum)

    def wall_foot_search(i, x4, y4, sl, u4_est, M_prev):
        """Find (back-column b, row j) whose segment brackets the
        arriving C- of the wall point at (x4, y4): the bracketing
        function f_j = (y4 - y_j) - lm_j (x4 - x_j) is positive at the
        previous wall (both terms positive) and decreases with row
        height; the first sign change is the foot segment."""
        for b in (1, 2, 3):
            if (1, i - b) not in G:
                break
            Mp = M_prev if b == 1 else max(
                j for j in range(1, M_prev + 1) if (j, i - b) in G)
            f_prev = None
            for j in range(1, Mp + 1):
                pt = G[(j, i - b)]
                f = (y4 - float(pt[1])) - foot_lm(pt, u4_est, sl) \
                    * (x4 - float(pt[0]))
                if f_prev is not None and f_prev > 0.0 >= f:
                    return b, j - 1
                f_prev = f
        return 1, 1                       # fallback: first segment

    x_end_march = None if x_traced else float(sx[-1])
    edge_pts, wall_pts = [], []
    sf_ct = [0]                    # streamline-foot decision counter
    clamp_n = [0]                  # feet landing outside their chord
    wall_foot_n = [0]              # (unused; kept for the out dict)
    foot_nobracket_n = [0]         # feet no column brackets
    foot_diag = []                 # why a scan found no bracket
    tdiag = []                     # solved feet outside their chord
    foot_open_n = [0]              # brackets the iteration could not
                                   # close (reported, never masked)
    tstat = []                     # (t, column, row) diagnostic
    M = N                                     # top row of the PREVIOUS column
    kst = -1
    # THE START-UP WEDGE OF A SHROUDED START (2026-09-24): every column is
    # a C+ line launched from a PLUG station, so the shroud between the
    # start line and the first column's arrival receives no column at all
    # (measured on the exact channel: the first column's C+ landed beyond
    # the lip, one shroud point, the lip placed from the start line). With
    # a free jet on top that wedge is filled with data rows (edge_fill);
    # with a WALL on top it must be marched: WEDGE COLUMNS = the C+ lines
    # launched from the start-line points, top row first (they order left
    # to right by x), each keeping its rows' indices (no wall, nothing
    # consumed) and ending on the shroud (or at the lip). Their column
    # indices precede the plug columns'; the plug wall's foot search then
    # finds its bracket on them like on any column.
    if shroud is not None:
        m_w = max(1, int(wedge_every))
        wedge = sorted(set(list(range(N - 1, 0, -m_w)) + [1]), reverse=True)
    else:
        wedge = []
    i = 1
    ci = -1                                   # column counter, both kinds
    while True:
        i += 1
        ci += 1
        if wedge:
            j0 = wedge.pop(0)
            G[(j0, i)] = G[(j0, 1)]
            if graph is not None:
                graph["alias"][(j0, i)] = (j0, 1)
            jnew = j0
            jsrc0 = j0 + 1
            done = False
            ktag = "w%d" % j0
        else:
            kst += 1
            ktag = kst
            if S.mode == "rec":
                x_next = float(sx[kst])
                S.d.setdefault("xcols", []).append(x_next)
                done = kst == len(sx) - 1
            else:
                x_next = S.d["xcols"][kst]
                done = kst == len(S.d["xcols"]) - 1
            if x_traced:
                x4w, y4w, sl = sx[kst], sy[kst], ssl[kst]
            else:
                x4w = jnp.float64(x_next)
                y4w = jnp.interp(x4w, sx, sy)
                sl = jnp.interp(x4w, sx, ssl)
            if S.mode == "rec":
                u4e = float(G[(1, i - 1)][2])
                b, jf = wall_foot_search(i, float(x4w), float(y4w),
                                         float(sl), u4e, M)
                S.d.setdefault("wfoot", []).append((b, jf))
            else:
                b, jf = S.d["wfoot"][kst]
            ptA = G[(jf, i - b)]
            ptB = G[(jf + 1, i - b)]
            p = jnp.concatenate([ptA, ptB, jnp.array([x4w, y4w, sl])]
                                + ([sw_inv] if NV == 6 else []))
            if S.mode == "rec":
                z0 = jnp.array([0.5 * (float(ptA[1]) + float(ptB[1])),
                                float(ptA[2])])
            else:
                z0 = jnp.zeros(2)
            z = cell(s_wb, p, z0, tag=("wall", kst))
            wpt = jnp.array([x4w, y4w, z[1], sl * z[1]])
            if NV == 6:
                wpt = jnp.concatenate([wpt, sw_inv])
            G[(1, i)] = wpt
            wall_pts.append(wpt)
            if graph is not None:
                graph["cells"].append(dict(kind="wall", out=(1, i), inp=[(jf, i - b), (jf + 1, i - b)],
                                           kst=kst, x_next=x_next, zi=len(S.d["z"]) - 1))
                graph["wall_out"].append((1, i))
            # ---- ROW CONSUMPTION at the wall: the previous column's rows
            # 2..jf lie BELOW the new wall point's foot — their C-
            # characteristics have already terminated on the wall between
            # stations. Prolonging them (the first fine-station build did)
            # creates ghost rows below the spike: Newton's only remaining
            # crossing for such a row is the BACKWARD one, a valid root of
            # the equations on the wrong branch (measured: a whole M1-state
            # mesh limb below the wall, mass +9%). At a solid wall the
            # incoming family must be consumed exactly as the edge adds
            # one: rows are re-indexed from the foot up.
            jsrc0 = (jf + 1 if b == 1 else 2) if consume else 2
            jnew = 1
        # ---- interiors, bottom-up, partnered with previous rows
        #      jsrc0..M (the top one uses the previous EDGE point)
        for jprev in range(jsrc0, M + 1):
            jnew += 1
            if track_R:
                cline[(jnew, i)] = cline.get((jprev, i - 1))
            pt1 = G[(jnew - 1, i)]
            # a thinned wedge: the rows the previous wedge column does not
            # carry take their C- partner from the start line itself
            k2 = (jprev, i - 1) if (jprev, i - 1) in G else (jprev, 1)
            pt2 = G[k2]
            if S.mode == "rec":
                z0 = (rot_pred(pt1, pt2, ta) if NV == 6
                      else predict_bu(pt1, pt2, ta, ta_np))
            else:
                z0 = None
            if NV == 6:
                # STREAMLINE-FOOT BRACKET SEARCH (a recorded decision,
                # the S24 lesson): the foot is NOT always on the chord
                # pt1-pt2 — when the C- drop per column exceeds the
                # row spacing the mesh shears and the backward
                # streamline lands OUTSIDE that chord, and a
                # single-chord lerp EXTRAPOLATES the invariants
                # (measured: a systematic N-independent transport
                # ramp on the stratified-jet oracle). GENO searches
                # the whole previous column for the intersection
                # (inter_solve_gen's present(col) branch); so does
                # this port.
                # STREAMLINE-FOOT BRACKET, ITERATED AGAINST THE
                # SOLVED FOOT (S24 measured): scanning with the
                # PREDICTOR's direction picks the wrong chord for a
                # few percent of cells — measured foot parameters up
                # to t = 10, i.e. ten rows past the chord, and the
                # invariant lerp then EXTRAPOLATES entropy the inlet
                # never supplied (5.6% of nodes, worst +42% of the
                # span). Clamping t instead stores invariants the
                # cell did not solve with and pushes the node off the
                # thermodynamic manifold (measured cert 3.5e11), so
                # the decision itself is iterated: solve, and if the
                # foot fell outside its chord, re-bracket with the
                # SOLVED direction and solve again. The converged
                # bracket is what the schedule records.
                def _scan(x4s, y4s, th0):
                    """(back-column b, row j) whose chord brackets the
                    backward streamline from (x4s, y4s) at angle th0.

                    W-5 FIX: search columns i-1, i-2, i-3 — exactly
                    what `wall_foot_search` already does for the C-
                    arriving at a WALL point. Measured on the
                    stratified spike, the foot of ~1.6% of interior
                    cells lies in NO segment of column i-1 at all, so
                    a single-column scan cannot bracket it, silently
                    returns its own initial guess, and the invariant
                    lerp then EXTRAPOLATES (foot parameters up to
                    t = 12) and manufactures entropy the inlet never
                    supplied. Stepping back a column finds the segment
                    that actually contains the foot.
                    """
                    for b in (1, 2, 3):
                        if (1, i - b) not in G:
                            break
                        Mp = max((j for j in range(1, M + 1)
                                  if (j, i - b) in G), default=0)
                        if Mp < 2:
                            continue
                        f_prev = None
                        for j in range(1, Mp + 1):
                            ptj = G[(j, i - b)]
                            f = ((y4s - float(ptj[1]))
                                 - np.tan(th0) * (x4s - float(ptj[0])))
                            if f_prev is not None and f_prev > 0.0 >= f:
                                return b, min(max(j - 1, 1), Mp - 1)
                            f_prev = f
                    # No column brackets it. Keep the legacy
                    # single-column fallback so this path is never
                    # WORSE than before — but COUNT it, because a
                    # fallback that nobody counts is exactly how W-5
                    # stayed invisible behind a passing mean.
                    Mp = max((j for j in range(1, M + 1)
                              if (j, i - 1) in G), default=0)
                    foot_nobracket_n[0] += 1
                    # WHERE is the foot, if no column brackets it?
                    # f > 0 at BOTH ends => it lies ABOVE the top row;
                    # f < 0 at both ends => BELOW row 1 (the wall
                    # side). Record it rather than guess again.
                    if len(foot_diag) < 40 and Mp > 1:
                        fs = []
                        for jq in (1, Mp):
                            pq = G[(jq, i - 1)]
                            fs.append(float(
                                (y4s - float(pq[1]))
                                - np.tan(th0) * (x4s - float(pq[0]))))
                        foot_diag.append(dict(
                            col=int(i), Mp=int(Mp), jprev=int(jprev),
                            f_row1=fs[0], f_rowMp=fs[1],
                            side=("above-top" if fs[0] > 0 and fs[1] > 0
                                  else "below-row1" if fs[0] < 0
                                  and fs[1] < 0 else "mixed")))
                    return 1, (min(max(jprev, 1), Mp - 1)
                               if Mp > 1 else 1)

                if S.mode == "rec":
                    bsf, jsf = _scan(
                        float(z0[0]), float(z0[1]),
                        float(np.arctan2(float(z0[3]), float(z0[2]))))
                    for _try in range(4):
                        ptSA = G[(jsf, i - bsf)]
                        ptSB = G[(jsf + 1, i - bsf)]
                        zt = np.asarray(s_int[0](
                            jnp.asarray(z0),
                            jnp.concatenate([pt1, pt2, ptSA, ptSB])))
                        tv = float(zt[4])
                        if -1e-9 <= tv <= 1.0 + 1e-9:
                            break
                        bn, jn = _scan(
                            float(zt[0]), float(zt[1]),
                            float(np.arctan2(float(zt[3]),
                                             float(zt[2]))))
                        if (bn, jn) == (bsf, jsf):
                            foot_open_n[0] += 1
                            break
                        bsf, jsf = bn, jn
                    # (b, j), mirroring `wfoot` — the column offset is
                    # now part of the recorded decision, so the replay
                    # freezes WHICH COLUMN the foot came from as well
                    # as which row.
                    S.d.setdefault("sfoot", []).append((bsf, jsf))
                else:
                    bsf, jsf = S.d["sfoot"][sf_ct[0]]
                sf_ct[0] += 1
                ptSA = G[(jsf, i - bsf)]
                ptSB = G[(jsf + 1, i - bsf)]
                p = jnp.concatenate([pt1, pt2, ptSA, ptSB])
            else:
                p = jnp.concatenate([pt1, pt2])
            z = cell(s_int, p,
                     z0 if z0 is not None else jnp.zeros(
                         5 if NV == 6 else 4),
                     tag=("int", ktag, jnew))
            if graph is not None:
                graph["cells"].append(dict(kind="int", out=(jnew, i), inp=[(jnew - 1, i), k2],
                                           zi=len(S.d["z"]) - 1))
            if NV == 6:
                # the cell's t lerps the streamline invariants on the
                # SEARCHED chord (the foot the cell itself refined),
                # CLAMPED to the chord — GENO's rule
                # (t_foot = max(0, min(1, t_foot)), reported through
                # its foot_clamped flag). Entropy and stagnation
                # enthalpy are TRANSPORTED: an unclamped lerp
                # EXTRAPOLATES them past the data that carries them,
                # creating entropy the inlet never supplied (S24
                # measured on the stratified spike: 5.6% of nodes,
                # worst +42% of the inlet span). Clamping keeps every
                # node's invariants inside the convex hull of the
                # chord's, so the transported bound holds by
                # construction; the clamp COUNT is reported, since a
                # march that clamps often is one whose foot search is
                # losing its bracket.
                # W-5 NOTE (2026-08-13, measured): the block above
                # DECLARES a clamp of t_ and `clamp_n` is named for it,
                # but t_ goes into the lerp RAW. Clamping it was TRIED
                # and REVERTED: W-5 then passes by construction
                # (overshoot exactly 0.000e+00, 0/1488 nodes) while
                # W-4 FAILS -- post-wedge mass conservation degrades
                # 7.93e-03 -> 3.72e-02 and the first-column wedge jump
                # 3.37e-02 -> 3.83e-01 (x2.1 -> x24.2 of its uniform
                # baseline). Entropy and h0 are TRANSPORTED, so
                # truncating the interpolated value asserts something
                # the streamline did not carry: the bound holds and
                # the conservation law breaks. W-5 and W-4 are not
                # independent, and no choice of VALUE at a foot of
                # t = 12-18 is right, because the FOOT is wrong.
                t_ = z[4]
                if S.mode == "rec":
                    tv = float(t_)
                    tstat.append((tv, kst, jnew))
                    if tv < -1e-12 or tv > 1.0 + 1e-12:
                        clamp_n[0] += 1
                        # W-5 DIAGNOSTIC (2026-08-13): the SOLVED foot
                        # left the chord the scan had bracketed. This
                        # is the DOMINANT failure (measured 20 of 22
                        # against only 2 unbracketed feet), so the
                        # defect is NOT in the search — it is in the
                        # bracket <-> solve fixed point. Record how far
                        # out, and on which side.
                        if len(tdiag) < 60:
                            tdiag.append(dict(
                                col=int(i), row=int(jnew),
                                b=int(bsf), j=int(jsf), t=float(tv),
                                side=("below" if tv < 0.0 else
                                      "above")))
                # STORE WHAT THE CELL SOLVED WITH (W-5, 2026-08-13).
                # The rotational residual forms its transported pair
                # from clip(t, 0, 1); the node must be written the
                # SAME way or the mesh carries invariants the cell
                # never used. Both orders of this mismatch have now
                # been measured: clamping the storage while the
                # residual was raw broke W-4 (mass 7.93e-03 ->
                # 3.72e-02); leaving the storage raw while the
                # residual clamps left W-5 at 38.85%. Consistency is
                # the requirement, not the clamp itself.
                inv = ptSA[4:6] + jnp.clip(t_, 0.0, 1.0) * (
                    ptSB[4:6] - ptSA[4:6])
                z = jnp.concatenate([z[:4], inv])
            G[(jnew, i)] = z
            if mg is not None and jnew >= mg["jmin"] \
                    and (jprev - 1, i - 1) in G:
                rows_from_top = (M - jsrc0 + 2) - jnew
                if rows_from_top > mg["f_edge"] * (M - jsrc0 + 2):
                    if mg.get("vec"):
                        m_quads.append((G[(jprev - 1, i - 1)], pt2, z, pt1))
                        m_qkeys.append(((jprev - 1, i - 1), i))
                        if graph is not None:
                            graph["quads"].append(((jprev - 1, i - 1), k2, (jnew, i), (jnew - 1, i)))
                    else:
                        margin_acc(cell_margin(G[(jprev - 1, i - 1)], pt2,
                                               z, pt1))
        if shroud is not None and lip_done[0]:
            # ---- after the lip: no top cell; the top row is F's C-
            M = jnew
            if M < 2:
                # the exit characteristic reached the plug: the march
                # is complete (the last column is the wall point alone)
                if S.mode == "rec" and not wedge and ktag == kst:
                    S.d.setdefault("K_cols", []).append(int(i))
                break
        elif shroud is not None:
            # ---- new top row: the SHROUD, met by THIS column's C+
            pt1 = G[(jnew, i)]
            if S.mode == "rec":
                x1_, y1_, u1_, v1_ = (float(v) for v in pt1[:4])
                M1 = (float(mach_np(np.hypot(u1_, v1_), ta_np)) if ta_np is not None
                      else float(A1.state_q(jnp.float64(np.hypot(u1_, v1_)), ta)[5]))
                tcp = np.tan(np.arctan2(v1_, u1_)
                             + np.arcsin(min(1.0, 1.0 / M1)))
                seg = -1
                fprev = None
                for k_ in range(len(sxs)):
                    if sxs[k_] <= x1_:
                        fprev = None
                        continue
                    f_ = (sys_[k_] - y1_) - tcp * (sxs[k_] - x1_)
                    if fprev is not None and fprev > 0.0 >= f_:
                        seg = k_ - 1
                        break
                    if fprev is None and f_ <= 0.0 and k_ > 0:
                        seg = k_ - 1        # the crossing is inside the first segment past x1
                        break
                    fprev = f_
                S.d.setdefault("sseg", []).append(int(seg))
            else:
                seg = S.d["sseg"][ci]
            if seg >= 0:
                xA, yA, sA = sxs[seg], sys_[seg], sss[seg]
                xB, yB, sB = sxs[seg + 1], sys_[seg + 1], sss[seg + 1]
                if S.mode == "rec":
                    fA = (yA - y1_) - tcp * (xA - x1_)
                    fB = (yB - y1_) - tcp * (xB - x1_)
                    xg = xA + (xB - xA) * (fA / (fA - fB) if fA != fB else 0.5)
                    z0 = jnp.array([float(np.clip(xg, xA, xB)), u1_])
                else:
                    z0 = jnp.zeros(2)
                p = jnp.concatenate([pt1[:4], jnp.array([xA, yA, sA, xB, yB, sB])])
                z = cell(s_wt, p, z0, tag=("shroud", ktag))
                y4, s4 = hermite_seg(z[0], xA, yA, sA, xB, yB, sB)
                spt = jnp.array([z[0], y4, z[1], s4 * z[1]])
                if graph is not None:
                    graph["cells"].append(dict(kind="shroud", out=(jnew + 1, i), inp=[(jnew, i)], seg=int(seg),
                                               zi=len(S.d["z"]) - 1))
            else:
                # the LIP F: the bell's inverse wall cell, its foot on the
                # C- leg from the previous shroud point to this column's
                # top interior
                ptP = G[(M, i - 1)]
                p = jnp.concatenate([ptP[:4], pt1[:4],
                                     jnp.array([sxs[-1], sys_[-1], sss[-1]])])
                if S.mode == "rec":
                    z0 = jnp.array([0.5 * (float(ptP[0]) + float(pt1[0])), float(pt1[2])])
                else:
                    z0 = jnp.zeros(2)
                z = cell(s_lip, p, z0, tag=("lip", ktag))
                spt = jnp.array([sxs[-1], sys_[-1], z[1], sss[-1] * z[1]])
                lip_done[0] = True
                lip_col[0] = int(i)
                if graph is not None:
                    graph["cells"].append(dict(kind="lip", out=(jnew + 1, i), inp=[(M, i - 1), (jnew, i)],
                                               zi=len(S.d["z"]) - 1))
            M = jnew + 1
            G[(M, i)] = spt
            shroud_pts.append(spt)
            if graph is not None:
                graph["shroud_out"].append((M, i))
        else:
            # ---- new top row: the free edge, fed from THIS column
            pt1 = G[(jnew, i)]
            pt3 = G[(M, i - 1)]          # previous edge (top of prev col)
            if S.mode == "rec":
                th_g = float(jnp.arctan2(pt3[3], pt3[2]))
                dx_g = max(float(pt1[0]) - float(pt3[0]), 1e-3)
                z0 = jnp.array([float(pt3[0]) + dx_g,
                                float(pt3[1]) + dx_g * np.tan(th_g), th_g])
            else:
                z0 = jnp.zeros(3)
            p = jnp.concatenate([pt1, pt3, jnp.array([qpa])])
            z = cell(s_fj, p, z0, tag=("edge", kst))
            q_e = qe_of(z[1])
            ept = jnp.array([z[0], z[1], q_e * jnp.cos(z[2]),
                             q_e * jnp.sin(z[2])])
            if NV == 6:
                ept = jnp.concatenate([ept, se_inv])
            if edge_fill and kst == 0:
                # fill the start-up wedge: the flow between the topmost
                # interior and the edge is smooth and unsampled, so seed it
                # as DATA (the pattern already used for the throat and lip
                # corners) rather than leave a hole the row-growth rule
                # cannot close at one row per column.
                base = G[(jnew, i)]
                for t in np.linspace(0.0, 1.0, edge_fill + 2)[1:-1]:
                    jnew += 1
                    G[(jnew, i)] = base + t * (ept - base)
            M = jnew + 1
            G[(M, i)] = ept
            edge_pts.append(ept)
        if track_R:
            for jj in range(2, M + 1):
                if (jj, i) not in cline:
                    cline[(jj, i)] = new_line[0]
                    new_line[0] += 1
        if S.mode == "rec" and ktag == kst:
            S.d.setdefault("K_cols", []).append(int(i))
        if done:
            break

    ilast = i
    cert_R = None
    if track_R:
        alive_ = {cline.get((j, ilast)) for j in range(2, M + 1)}
        worst_R, where_R = 0.0, None
        for r_, tg in (cert_cells or []):
            if tg is None:
                continue
            if tg[0] == "wall":
                inr = True
            elif tg[0] == "int":
                inr = (isinstance(tg[1], int)
                       and cline.get((tg[2], 2 + tg[1])) not in alive_)
            else:
                inr = False
            if inr and r_ > worst_R:
                worst_R, where_R = r_, tg
        cert_R = (worst_R, where_R)
    if track_R and m_quads:
        alive = {cline.get((j, ilast)) for j in range(2, M + 1)}
        keep = [(a[0] == 1 or cline.get(a) not in alive) and ic >= 3
                for a, ic in m_qkeys]
        m_quads = [q for q, k_ in zip(m_quads, keep) if k_]
    if mg is not None and mg.get("vec") and m_quads:
        # corners A, B, C, D of every bucket cell, (n, 2) each: every
        # net point is stacked ONCE (a point is a corner of up to four
        # cells) and gathered by index -- one stack, four gathers
        uid, pts_u, ix = {}, [], np.empty((len(m_quads), 4), dtype=int)
        for n_, q in enumerate(m_quads):
            for k in range(4):
                key = id(q[k])
                if key not in uid:
                    uid[key] = len(pts_u)
                    pts_u.append(q[k])
                ix[n_, k] = uid[key]
        PAD = int(mg.get("pad", 0) or 0)
        n_c = ix.shape[0]
        mask = None
        if PAD > 0:
            # FIXED-BLOCK STACK (S41 2026-09-26, opt-in by margin["pad"];
            # default 0 = the path above, bit-identical). jnp.stack of N
            # operands compiles ONE XLA module per N: minutes at 3e4 points
            # (the "Very slow compile" of the (280,61) marches, measured
            # 1400-1800 s against 112 s once cached) and a new module for
            # every distinct cell count, which is how a long walk reached
            # the kernel's memory-mapping cap. Blocks of PAD points (the
            # last block padded by repeating its last point) compile once;
            # the cell arrays are padded to a multiple of PAD with a repeat
            # of the last cell and MASKED out of the min and the KS by +inf
            # (exp(-inf) = 0 exactly: the aggregates are those of the real
            # cells).
            blocks = []
            for i0 in range(0, len(pts_u), PAD):
                blk = pts_u[i0:i0 + PAD]
                blk = blk + [blk[-1]] * (PAD - len(blk))
                blocks.append(jnp.stack(blk)[:, :2])
            PU = jnp.concatenate(blocks, axis=0)
            n_cp = -(-n_c // PAD) * PAD
            ixp = np.concatenate([ix, np.repeat(ix[-1:], n_cp - n_c, axis=0)], axis=0)
            mask = jnp.asarray(np.arange(n_cp) < n_c)
            cA, cB, cC, cD = [PU[ixp[:, k]] for k in range(4)]
        else:
            PU = jnp.stack(pts_u)[:, :2]
            cA, cB, cC, cD = [PU[ix[:, k]] for k in range(4)]
        v = margin_of_corners(cA, cB, cC, cD, mask, mg)
        if mg.get("cells") and S.mode == "rec":
            # per-cell census (S40, additive, record mode only): the
            # margin of every bucket cell with its (A-corner key, column)
            mg["cells_out"] = (np.asarray(v)[:n_c], list(m_qkeys),
                               np.stack([np.asarray(cA), np.asarray(cB),
                                         np.asarray(cC), np.asarray(cD)])[:, :n_c])
        m_n[0] = n_c
        m_min[0] = jnp.min(v)
        m_acc[0] = jax.scipy.special.logsumexp(-mg["rho"] * v)

    col = jnp.stack([G[(j, ilast)] for j in range(1, M + 1)
                     if (j, ilast) in G])
    out = dict(
        edge=(jnp.stack(edge_pts) if edge_pts else None), wall=jnp.stack(wall_pts),
        shroud=(jnp.stack(shroud_pts) if shroud is not None and shroud_pts else None),
        lip_col=(lip_col[0] if shroud is not None else None),
        last_col=col, cert_worst=(cert["worst"] if cert_R is None or S.mode != "rec" else cert_R[0]),
        cert_worst_net=cert["worst"], cert_where_R=(None if cert_R is None else cert_R[1]),
        cert_n=cert["n"],
        cert_where=cert["where"],
        margin_ks=(None if mg is None or m_acc[0] is None
                   else -m_acc[0] / mg["rho"]),
        margin_min=(None if mg is None else m_min[0]),
        margin_n=m_n[0],
        # numpy, deliberately: this is a concrete record-mode artifact
        # (never traced) and every consumer converts it to numpy
        # anyway. jnp.stack over the whole mesh is an XLA compile
        # with K*N operands — measured 7m30 at (241,201) and HOURS
        # at (481,401), 100% CPU inside backend_compile (S23).
        # Values are a memcpy either way: bit-identical.
        mesh_pts=(np.stack([np.asarray(v) for v in G.values()])
                  if S.mode == "rec" else None),
        mesh_keys=(list(G.keys()) if S.mode == "rec" else None),
        foot_clamped_n=clamp_n[0], wall_foot_n=wall_foot_n[0],
        foot_open_n=foot_open_n[0], tstat=tstat,
        foot_nobracket_n=foot_nobracket_n[0],
        sfoot_bhist=dict(collections.Counter(
            b for b, _ in S.d.get('sfoot', []))),
        foot_diag=foot_diag[:40], tdiag=tdiag[:60])
    return out, S


# ----------------------------------------------------------------------
# conservation fluxes through a wall-to-edge polyline (pa gauge)
# ----------------------------------------------------------------------
def col_fluxes(col, ta, pa, delta):
    """Mass and axial-momentum flux (ambient gauge) through a polyline
    of (x, y, u, v) rows, oriented wall -> edge; the normal (dy, -dx)
    points downstream. Weight = 2 pi y for axisymmetric (delta=1),
    1 for planar."""
    c = np.asarray(col)
    q = np.hypot(c[:, 2], c[:, 3])
    st = A1.state_q(jnp.array(q), ta)
    p = np.array(st[1])
    rho = np.array(st[2])
    dx = np.diff(c[:, 0])
    dy = np.diff(c[:, 1])
    um = 0.5 * (c[1:, 2] + c[:-1, 2])
    vm = 0.5 * (c[1:, 3] + c[:-1, 3])
    rm = 0.5 * (rho[1:] + rho[:-1])
    pm = 0.5 * (p[1:] + p[:-1])
    w = (2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])) if delta \
        else 1.0
    dmd = rm * (um * dy - vm * dx) * w
    return (float(np.sum(dmd)),
            float(np.sum(um * dmd + (pm - pa) * dy * w)))


def wall_push_poly(wall, ta, pa, delta):
    """Gauge pressure push of the wall polyline, ∫ (p - pa) w dy with
    signed dy: the momentum theorem for the marched region closes as
    F_out - F_in + push = 0 (the free edge contributes exactly zero
    in the pa gauge — the plug's defining property)."""
    c = np.asarray(wall)
    q = np.hypot(c[:, 2], c[:, 3])
    p = np.array(A1.state_q(jnp.array(q), ta)[1])
    dy = np.diff(c[:, 1])
    pm = 0.5 * (p[1:] + p[:-1])
    w = (2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])) if delta \
        else 1.0
    return float(np.sum((pm - pa) * dy * w))


# ----------------------------------------------------------------------
# exact planar simple-wave reference (gconst)
# ----------------------------------------------------------------------
def pm_exact(gam, Rg, ts, M1, M2):
    def nu(M):
        a = np.sqrt((gam + 1) / (gam - 1))
        return a * np.arctan(np.sqrt((M * M - 1) / a / a)) \
            - np.arctan(np.sqrt(M * M - 1))
    dnu = nu(M2) - nu(M1)

    def state_of_M(M):
        T = ts / (1 + 0.5 * (gam - 1) * M * M)
        q = M * np.sqrt(gam * Rg * T)
        return q

    def field(x, y, lip):
        """exact simple-wave state at (x,y): returns (q, theta)."""
        # ray angle from the lip, measured from +x axis (rays go
        # down-right, angle negative)
        phi = np.arctan2(y - lip[1], x - lip[0])
        mu1 = np.arcsin(1.0 / M1)
        mu2 = np.arcsin(1.0 / M2)
        phi1 = -mu1                       # first ray (theta = 0)
        phi2 = dnu - mu2                  # last ray (theta = dnu)
        if phi <= phi1:
            return state_of_M(M1), 0.0
        if phi >= phi2:
            return state_of_M(M2), dnu
        # in the fan: on the ray, phi = theta - mu(M); invert for M
        from scipy.optimize import brentq

        def f(M):
            # ray angle of the M-characteristic: phi_ray = theta - mu
            return nu(M) - nu(M1) - np.arcsin(1.0 / M) - phi
        M = brentq(f, M1, M2, xtol=1e-12)
        th = nu(M) - nu(M1)
        return state_of_M(M), th
    return dnu, field, state_of_M


def exact_streamline(field, lip, p0, x_end, h=2e-4):
    """RK4 streamline of the exact field from p0 to x_end."""
    xs, ys = [p0[0]], [p0[1]]
    x, y = p0
    while x < x_end:
        def slope(xx, yy):
            q, th = field(xx, yy, lip)
            return np.tan(th)
        k1 = slope(x, y)
        k2 = slope(x + h / 2, y + h * k1 / 2)
        k3 = slope(x + h / 2, y + h * k2 / 2)
        k4 = slope(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    stage = os.environ.get("STAGE", "oracle")
    print("== A1 brick 2 step 9b: plug march [F2/A1] (stage=%s) =="
          % stage)

    if stage == "oracle":
        tg = A1.prep_tab(A1.build_tab_gconst())
        ta = A1.tab_arrays(tg)
        gam, Rg, ts = tg["_g"], tg["Rg"], tg["ts"]
        M1, M2 = 1.5, 2.2
        dnu, field, q_of = pm_exact(gam, Rg, ts, M1, M2)
        q1, q2 = q_of(M1), q_of(M2)
        pa = float(A1.state_q(jnp.float64(q2), ta)[1])
        qpa = q_at_pa(pa, ta, tg["_as"])
        print("  planar simple-wave twin: M1=%.2f M2=%.2f dnu=%.5f"
              " rad; q2=%.3f (tables %.3f)" % (M1, M2, dnu, q2, qpa))
        lip = (0.0, 2.0)
        x0, x_end = 0.5, 3.0

        def run_case(K, N):
            xs, ys = exact_streamline(field, lip, (0.0, 1.0), x_end)
            # start line: exact field on the vertical cut at x0, from
            # the exact edge point down to the exact wall point
            y_wall0 = float(np.interp(x0, xs, ys))
            y_edge0 = lip[1] + np.tan(dnu) * x0
            yline = np.linspace(y_wall0, y_edge0, N)
            us, vs = [], []
            for yy in yline:
                q, th = field(x0, yy, lip)
                us.append(q * np.cos(th))
                vs.append(q * np.sin(th))
            start = (x0, yline, np.array(us), np.array(vs))
            m = xs > x0 + 1e-9
            tgrid = np.linspace(0, 1, K)
            sxa = x0 + tgrid[1:] * (x_end - x0)
            sya = np.interp(sxa, xs, ys)
            ssl = np.interp(sxa, xs, np.gradient(ys, xs))
            st = (jnp.array(sxa), jnp.array(sya), jnp.array(ssl))
            out, _ = plug_march(st, start, qpa, tg, 0.0)
            return out, (xs, ys)

        out_c, _ = run_case(41, 21)
        out_f, exact_w = run_case(81, 41)
        print("  cert: coarse %.3f (n=%d) fine %.3f (n=%d) worst at"
              " %s / %s" % (out_c["cert_worst"], out_c["cert_n"],
                            out_f["cert_worst"], out_f["cert_n"],
                            out_c["cert_where"], out_f["cert_where"]))
        check("all cells Newton-certified", out_c["cert_worst"] <= 1.0
              and out_f["cert_worst"] <= 1.0)

        # P-1: edge asymptotics
        def edge_stats(out):
            e = np.array(out["edge"])
            n = e.shape[0]
            tail = e[int(0.7 * n):]
            th = np.arctan2(tail[:, 3], tail[:, 2]).mean()
            qe = np.hypot(tail[:, 2], tail[:, 3]).mean()
            return th, qe
        thc, qec = edge_stats(out_c)
        thf, qef = edge_stats(out_f)
        band_th = K_RICH * abs(thc - thf) + 64 * EPS * abs(dnu)
        d_th = abs(thf - dnu)
        print("  P-1 edge: angle %.5f vs dnu %.5f (|d|=%.2e,"
              " band=%.2e); speed %.3f vs %.3f"
              % (thf, dnu, d_th, band_th, qef, q2))
        check("P-1 edge angle -> dnu within Richardson band",
              d_th <= band_th)

        # P-2: wall pressures vs the exact field
        def wall_p(out):
            w = np.array(out["wall"])
            q = np.hypot(w[:, 2], w[:, 3])
            p = np.array(A1.state_q(jnp.array(q), ta)[1])
            pex = np.array([A1.state_q(jnp.float64(
                field(w[k, 0], w[k, 1], lip)[0]), ta)[1]
                for k in range(w.shape[0])])
            return w[:, 0], p, pex
        xwc, pc, pexc = wall_p(out_c)
        xwf, pf, pexf = wall_p(out_f)
        # compare at the coarse stations (both grids share the exact
        # wall, bands from grid halving via interpolation)
        pf_i = np.interp(xwc, xwf, pf)
        band_p = K_RICH * np.abs(pc - pf_i) + A1.C_FLOOR * EPS * pa
        dev_p = np.abs(pf_i - np.interp(xwc, xwc, pexc))
        frac = float((dev_p <= band_p).mean())
        print("  P-2 wall pressure: %.0f%% of stations inside band"
              " (max dev/pa %.2e)" % (100 * frac, dev_p.max() / pa))
        check("P-2 wall pressure matches the exact field (>= 90%"
              " in band)", frac >= 0.90)

        # P-3: mass conservation (planar, per unit depth)
        def mass(col):
            c = np.array(col)
            q = np.hypot(c[:, 2], c[:, 3])
            rho = np.array(A1.state_q(jnp.array(q), ta)[2])
            dx = np.diff(c[:, 0])
            um = 0.5 * (c[1:, 2] + c[:-1, 2])
            vm = 0.5 * (c[1:, 3] + c[:-1, 3])
            rm = 0.5 * (rho[1:] + rho[:-1])
            dy_s = np.diff(c[:, 1])          # SIGNED (top-down column)
            # flux through the segment (normal ds = (dy, -dx))
            return float(np.abs(np.sum(rm * (um * dy_s - vm * dx))))
        # start flux: integrate the exact (nonuniform) start line
        yl = np.linspace(lip[1] + np.tan(dnu) * x0,
                         float(np.interp(x0, exact_w[0], exact_w[1])),
                         801)
        uu, vv = [], []
        for yy in yl:
            q, th = field(x0, yy, lip)
            uu.append(q * np.cos(th))
            vv.append(q * np.sin(th))
        uu = np.array(uu)
        rr = np.array(A1.state_q(jnp.array(np.hypot(uu, vv)), ta)[2])
        md0 = float(np.abs(np.trapezoid(rr * uu, yl)))
        mdc = mass(out_c["last_col"])
        mdf = mass(out_f["last_col"])
        band_m = K_RICH * abs(mdc - mdf) + A1.C_FLOOR * EPS * md0
        print("  P-3 mass: exit %.6e vs start %.6e (|d|=%.2e,"
              " band=%.2e)" % (mdf, md0, abs(mdf - md0), band_m))
        check("P-3 mass conserved within band",
              abs(mdf - md0) <= band_m)

        # P-4: momentum closure in the pa gauge (free edge = 0)
        yl_st = np.linspace(float(np.interp(x0, exact_w[0],
                                            exact_w[1])),
                            lip[1] + np.tan(dnu) * x0, 801)
        uu2, vv2 = [], []
        for yy in yl_st:
            q, th = field(x0, yy, lip)
            uu2.append(q * np.cos(th))
            vv2.append(q * np.sin(th))
        stline = np.stack([np.full(801, x0), yl_st,
                           np.array(uu2), np.array(vv2)], axis=1)
        _, Fin = col_fluxes(stline, ta, pa, 0.0)

        def mom_closure(out):
            _, Fout = col_fluxes(np.array(out["last_col"]), ta, pa,
                                 0.0)
            wallpoly = np.vstack([stline[:1], np.array(out["wall"])])
            push = wall_push_poly(wallpoly, ta, pa, 0.0)
            return Fout - Fin + push
        Rm_c = mom_closure(out_c)
        Rm_f = mom_closure(out_f)
        band_F = K_RICH * abs(Rm_c - Rm_f) + A1.C_FLOOR * EPS \
            * abs(Fin)
        print("  P-4 momentum: closure %.4e (coarse %.4e) vs band"
              " %.4e on F_in %.4e; free edge contributes 0 by"
              " construction" % (Rm_f, Rm_c, band_F, Fin))
        check("P-4 momentum closes in the pa gauge within band",
              abs(Rm_f) <= band_F)

        # R-1: corrupted ambient
        def run_bad():
            xs, ys = exact_w
            y_wall0 = float(np.interp(x0, xs, ys))
            y_edge0 = lip[1] + np.tan(dnu) * x0
            yline = np.linspace(y_wall0, y_edge0, 41)
            us, vs = [], []
            for yy in yline:
                q, th = field(x0, yy, lip)
                us.append(q * np.cos(th))
                vs.append(q * np.sin(th))
            start = (x0, yline, np.array(us), np.array(vs))
            tgrid = np.linspace(0, 1, 81)
            sxa = x0 + tgrid[1:] * (x_end - x0)
            st = (jnp.array(sxa),
                  jnp.array(np.interp(sxa, xs, ys)),
                  jnp.array(np.interp(sxa, xs,
                                      np.gradient(ys, xs))))
            o, _ = plug_march(st, start, qpa * 1.01, tg, 0.0)
            return edge_stats(o)
        thb, _ = run_bad()
        print("  R-1: corrupted-ambient edge angle %.5f (|d - dnu| ="
              " %.2e vs band %.2e)" % (thb, abs(thb - dnu), band_th))
        check("R-1 rejector: corrupted ambient leaves the P-1 band",
              abs(thb - dnu) > band_th)

        print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                              time.time() - t0))
        sys.exit(0 if NPASS[0] == NPASS[1] else 1)

    if stage == "axi":
        # the same assembly, axisymmetric (delta = 1), on the real-gas
        # NASA tables. No closed form exists here, so the stage
        # certifies by INTERNAL closures: Newton certification, mass
        # conservation, the pa-gauge momentum theorem (free edge = 0
        # by construction), a source-alive control (the delta = 1 run
        # must differ measurably from delta = 0 on the same data),
        # and a corrupted-spike rejector.
        from scipy.optimize import brentq
        tb = A1.prep_tab(A1.build_tab_nasa())
        ta = A1.tab_arrays(tb)
        as_ = tb["_as"]
        M1, M2 = 1.5, 2.2

        def q_of_M(Mt):
            return brentq(lambda q: float(
                A1.state_q(jnp.float64(q), ta)[5]) - Mt,
                1.02 * as_, 3.2 * as_, xtol=1e-11)
        q1, q2 = q_of_M(M1), q_of_M(M2)
        pa = float(A1.state_q(jnp.float64(q2), ta)[1])
        qpa = q_at_pa(pa, ta, as_)
        # tables-consistent planar corner fan (start-line DATA):
        # dtheta = sqrt(M^2-1)/q dq integrated on the tables' own M(q)
        qs = np.linspace(q1, q2, 400)
        Ms = np.array([float(A1.state_q(jnp.float64(q), ta)[5])
                       for q in qs])
        mus = np.arcsin(np.clip(1.0 / Ms, 0, 1))
        dth = np.sqrt(np.maximum(Ms ** 2 - 1.0, 0.0)) / qs
        ths = np.concatenate([[0.0], np.cumsum(
            0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
        phis = ths - mus                       # ray angles, monotone
        th2 = float(ths[-1])
        print("  tables fan: q %.2f -> %.2f, turn %.5f rad, pa ="
              " %.4e" % (q1, q2, th2, pa))

        def field_tab(x, y, lip):
            ph = np.arctan2(y - lip[1], x - lip[0])
            if ph <= phis[0]:
                return q1, 0.0
            if ph >= phis[-1]:
                return q2, th2
            return (float(np.interp(ph, phis, qs)),
                    float(np.interp(ph, phis, ths)))

        lip = (0.0, 2.0)
        x0, x_end = 0.5, 2.5
        xs, ys = exact_streamline(field_tab, lip, (0.0, 1.0), x_end,
                                  h=5e-4)

        def run_case(K, N, delta, dssl=0.0):
            y_wall0 = float(np.interp(x0, xs, ys))
            y_edge0 = lip[1] + np.tan(th2) * x0
            yline = np.linspace(y_wall0, y_edge0, N)
            us, vs = [], []
            for yy in yline:
                q, th = field_tab(x0, yy, lip)
                us.append(q * np.cos(th))
                vs.append(q * np.sin(th))
            start = (x0, yline, np.array(us), np.array(vs))
            tgrid = np.linspace(0, 1, K)
            sxa = x0 + tgrid[1:] * (x_end - x0)
            st = (jnp.array(sxa), jnp.array(np.interp(sxa, xs, ys)),
                  jnp.array(np.interp(sxa, xs, np.gradient(ys, xs))
                            + dssl))
            out, _ = plug_march(st, start, qpa, tb, delta)
            return out

        out_c = run_case(33, 17, 1.0)
        out_f = run_case(65, 33, 1.0)
        print("  cert: coarse %.3f (n=%d) fine %.3f (n=%d) worst at"
              " %s / %s" % (out_c["cert_worst"], out_c["cert_n"],
                            out_f["cert_worst"], out_f["cert_n"],
                            out_c["cert_where"], out_f["cert_where"]))
        check("A-1 all cells Newton-certified (axi, real-gas)",
              out_c["cert_worst"] <= 1.0 and out_f["cert_worst"]
              <= 1.0)

        # dense start-line polyline for reference fluxes
        yl_st = np.linspace(float(np.interp(x0, xs, ys)),
                            lip[1] + np.tan(th2) * x0, 801)
        uu, vv = [], []
        for yy in yl_st:
            q, th = field_tab(x0, yy, lip)
            uu.append(q * np.cos(th))
            vv.append(q * np.sin(th))
        stline = np.stack([np.full(801, x0), yl_st, np.array(uu),
                           np.array(vv)], axis=1)
        md0, Fin = col_fluxes(stline, ta, pa, 1.0)

        def closures(out):
            md, Fout = col_fluxes(np.array(out["last_col"]), ta, pa,
                                  1.0)
            wallpoly = np.vstack([stline[:1], np.array(out["wall"])])
            push = wall_push_poly(wallpoly, ta, pa, 1.0)
            return md, Fout - Fin + push
        md_c, Rm_c = closures(out_c)
        md_f, Rm_f = closures(out_f)
        band_m = K_RICH * abs(md_c - md_f) + A1.C_FLOOR * EPS * md0
        print("  A-2 mass: exit %.6e vs start %.6e (|d|=%.2e,"
              " band=%.2e)" % (md_f, md0, abs(md_f - md0), band_m))
        check("A-2 mass conserved within band (2 pi y flux)",
              abs(md_f - md0) <= band_m)
        band_F = K_RICH * abs(Rm_c - Rm_f) + A1.C_FLOOR * EPS \
            * abs(Fin)
        print("  A-3 momentum: closure %.4e (coarse %.4e) vs band"
              " %.4e on F_in %.4e" % (Rm_f, Rm_c, band_F, Fin))
        check("A-3 momentum closes in the pa gauge within band",
              abs(Rm_f) <= band_F)

        # A-4: the axisymmetric source must be ALIVE — the same data
        # marched with delta = 0 must differ beyond the axi pair's
        # own Richardson band (guards a silently-planar axi mode)
        out_p = run_case(33, 17, 0.0)
        wq_a = np.hypot(np.array(out_c["wall"])[-1, 2],
                        np.array(out_c["wall"])[-1, 3])
        wq_f = np.hypot(np.array(out_f["wall"])[-1, 2],
                        np.array(out_f["wall"])[-1, 3])
        wq_p = np.hypot(np.array(out_p["wall"])[-1, 2],
                        np.array(out_p["wall"])[-1, 3])
        band_q = K_RICH * abs(wq_a - wq_f) + 64 * EPS * abs(wq_a)
        print("  A-4 source-alive: wall speed at x_end axi %.3f vs"
              " planar %.3f (|d|=%.2e, band=%.2e)"
              % (wq_f, wq_p, abs(wq_f - wq_p), band_q))
        check("A-4 axisymmetric source alive (differs from planar"
              " beyond band)", abs(wq_f - wq_p) > band_q)

        # A-5 rejector: corrupted spike slopes must break closure
        try:
            out_b = run_case(33, 17, 1.0, dssl=0.05)
            _, Rm_b = closures(out_b)
            bad = abs(Rm_b) > band_F
            print("  A-5: corrupted spike slope -> closure %.4e vs"
                  " band %.4e" % (Rm_b, band_F))
        except Exception as ex:                     # noqa: BLE001
            bad = True
            print("  A-5: corrupted spike slope -> march failed"
                  " (%s)" % type(ex).__name__)
        check("A-5 rejector: corrupted spike leaves the closure"
              " band", bad)

        print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                              time.time() - t0))
        sys.exit(0 if NPASS[0] == NPASS[1] else 1)

    print("stage %s not implemented in this carrier version" % stage)
    sys.exit(1)


if __name__ == "__main__":
    main()

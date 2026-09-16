#!/usr/bin/env python3
"""[X-OWAB] OUR WORLD, THE TOURNAMENT ROW [F3/A1]: Rao's construction
against the free-form spike at FULL EXPANSION, on shared constraints,
in the shock-free class (S29 2026-09-16; log
validation/PROGRESS_2026-09-16_S29_readjudication.md sec. 6).

WHAT THE A/B IS. M0's finite sector tournament: two design methods are
compared ONLY on shared constraints. At L = 2.5 m the Rao-vs-spline
A/B was VOID (mass + length exhaust Rao's two degrees of freedom and
the ambient becomes an output, ch_spline sec. vsrao). The fair posing
is full expansion: GENO's axisymmetric ideal-spike member in OUR gas
(CASES/raoplug_ch4o2, validation mode Me_fixed 2.802: theta_E -0.02
deg, L 5.926, closes on the axis) and our free-form spike posed in
TWIN MODE on it — GENO's own start line at the cut x0 = 1.50 as Cauchy
data (mass and gas coincide by construction), the ambient = the
member's lip ambient p_a = 0.9949 of the nominal PA (the analogue of
Rao's Eq. (8); the 0.5 percent residual against the NOMINAL ambient is
a DECLARED posing residual — the tournament at exact PA needs a GENO
member at exact PA, GENO protocol N-75, owner's call), the tip cut at
0.01 y_E (S28, declared). Both sides are marched by the same certified
plug march and graded by the same functional J = F_in + integral
(p_w - p_a) 2 pi y (-dy): [X-RAOFN].

THE CLASS. The S29 finding (secs. 4-5) is that every unconstrained
free-form optimum of the brick-2 line at L = 2.5 m was a FOLDED march
— out of the shock-free class the march is certified for. A
tournament row is therefore a statement only if BOTH contestants are
in the class: the fold margin of [X-PMRG] (signed area of the true net
cell over the mean legs floored at the station spacing squared,
orient-signed, in-loop KS) is derived HERE, on this posing, with Rao's
own contour as the healthy reference (m_ref), and every design of the
row is graded by it.

STAGE audit (default): the row that the S28 instruments already
measured, now class-certified. Posing = rao1961_sqp_return v3 through
ourworld_geno.install (8 knots on [x0 + FREEZE (x_D - x0), x_D], the
near-cut zone FROZEN to Rao's wall at FREEZE 0.35 — the v2 re-posing
of record, declared: the first knot's cardinal function deforms the
wall inside the zone where the twin's Cauchy data still dominates and
the gradient floor there was 60x the interior one; tip pinned at y_D).
Designs of record from validation/_ourworld/sqpret_v3_designs_2026-09-15.npz
([X-OWS3]): W_fit = Rao's contour in spline space, W_p = the 1.5
percent alternating perturbation, W_s = the TR-SQP's return, W_r = the
sign-flipped rejector's end. Measured: (D1) orientation, the
free-edge bucket depth at the doubled resolution, m_ref on Rao's
contour, floors mu0_k = m_ref/2^k, rho, the KS gap; (D2) the margin,
the fold census (column-wise y-monotonicity) and the compression
corner against Rao's own wall angle for each design; (D3) J_fit at K
and 2K-1 -> band_J = K_RICH |dJ| + |grad J(W_fit)|_1 band_W (v2
definition, recomputed); (D4) the gradient floor of Rao's contour with
the near-cut zone FREE (FREEZE 0), reported against the frozen one —
the number that decides whether the `ab` stage may free the near-cut
zone (reported, not gated). CHECKS: A-1 Rao's contour is strictly
healthy on the bucket (the reference of the class); A-2 the returned
optimum W_s is IN the class at the tightest floor; A-3 the tournament
value |J(W_s) - J(W_fit)| <= band_J (the S28 P4b re-read as the A/B:
the free-form optimizer, free to leave Rao's contour, finds NOTHING
outside band_J at these constraints); A-4 REJECTOR: Rao's contour with
a 2 deg compression corner at the first free knot (the S21 optimum's
corner, the mildest fold of record) is INFEASIBLE at every floor with
finite margin and gradient. Artifact: _ourworld/ab_audit.json.

STAGE ab (the walk, multi-hour): margin-constrained TR-SQP at this
posing (the [X-PMRG] driver logic on the rao1961 world: constraint on
the same frozen schedule, value/gradient memo, G1 surrogate,
REQ-NONSTALL on the objective, feasibility gate, derived radius floor)
from W_fit (Rao itself: does a class-constrained optimizer improve on
Rao at all?) and from W_p (the perturbed start: does it come back
inside the class?); OW_FREEZE selects the class (0.35 = the v3 class;
smaller frees the near-cut zone — a NEW posing whose gradient floor
the audit reports). Verdict: gain over Rao vs band_J, class membership
and mu of every returned base, the S28 v3 return-by-direction on W_s.
Consumes ab_audit.json (nothing typed twice). Launched on the owner's
word.

ON-DEMAND CARRIER (env: jax + the GENO run directory, OW_GENO_RUN).
OW_AB_STAGE in {audit, ab}; OW_FREEZE (ab only; default = the audit's
0.35); OWAB_SEGS / OWAB_ITERS (ab budget, defaults 4 / 12).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import jax                                              # noqa: E402
import jax.numpy as jnp                                 # noqa: E402
import ourworld_geno as OW                              # noqa: E402

os.environ.setdefault("RAO_X0", "1.50")
os.environ.setdefault("RAO_K", "161")
os.environ.setdefault("RAO_ART", os.path.join(HERE, "_ourworld"))
os.environ["RAO_GENO_RUN"] = OW.RUN
import rao1961_sqp_return as R                          # noqa: E402
import a1_ideal_march_jax as A1                         # noqa: E402
from a1_plug_march import plug_march                    # noqa: E402
from rao1961_twin import start_from_geno                # noqa: E402

K_RICH = A1.K_RICH
EPS = A1.EPS
ART = os.environ.get("RAO_ART", os.path.join(HERE, "_ourworld"))
AUDIT = os.path.join(ART, "ab_audit.json")
STAGE = os.environ.get("OW_AB_STAGE", "audit")
DESIGNS = os.environ.get("OW_AB_DESIGNS",
                         os.path.join(ART, "sqpret_v3_designs_2026-09-15.npz"))
SEGS = int(os.environ.get("OWAB_SEGS", 4))
ITERS = int(os.environ.get("OWAB_ITERS", 12))
JMIN = 2
N_RUNGS = 4
CORNER_DEG = 2            # the S21 optimum's corner (S29 sec. 4.4): the rejector
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


# ======================================================================
# the march with the margin, on the rao1961 posing
# ======================================================================
def march_m(W, w, mg=None, K=None, start=None):
    st = tuple(np.asarray(v) for v in R.stations(np.asarray(W, float), w, K))
    return plug_march(st, w.start if start is None else start, w.qpa, w.tab,
                      1.0, edge_fill=R.EDGE_FILL, margin=mg)


def margin_replay(W, w, sched, mg):
    out, _ = plug_march(R.stations(W, w), w.start, w.qpa, w.tab, 1.0,
                        sched=A1.Sched("play", sched.d), edge_fill=R.EDGE_FILL,
                        margin=mg)
    return out["margin_ks"] - mg["mu0"]


def margin_and_grad(W, w, sched, mg):
    f = lambda z: margin_replay(z, w, sched, mg)        # noqa: E731
    v, g = jax.value_and_grad(f)(jnp.asarray(W, dtype=float))
    return float(v), np.asarray(g, dtype=float)


def station_spacing(w, K=None):
    Kq = R.K_ST if K is None else K
    return (w.xD - R.X0) / Kq          # stations = linspace(X0, xD, K+1)[1:]


def np_margin(out, sch, N_rows, orient, f_edge, ell2, jmin=JMIN,
              with_depth=False):
    """The numpy census of the recorded net (the [X-PMRG] twin of the
    in-loop margin): per-cell margins over the bucket, plus each cell's
    row depth from the top when asked."""
    keys = out["mesh_keys"]
    pts = np.asarray(out["mesh_pts"])
    idx = {k: n for n, k in enumerate(keys)}
    ms, depth, where = [], [], []
    M = N_rows
    for kst, (b, jf) in enumerate(sch.d["wfoot"]):
        i = 2 + kst
        jsrc0 = (jf + 1) if b == 1 else 2
        top = M - jsrc0 + 2
        for jnew in range(jmin, top + 1):
            jprev = jnew + jsrc0 - 2
            q4 = [(jprev - 1, i - 1), (jprev, i - 1), (jnew, i),
                  (jnew - 1, i)]
            if not all(k in idx for k in q4):
                continue
            if not (top - jnew > f_edge * top):
                continue
            xy = np.array([pts[idx[k], :2] for k in q4])
            A = 0.5 * np.sum(xy[:, 0] * np.roll(xy[:, 1], -1)
                             - np.roll(xy[:, 0], -1) * xy[:, 1])
            lp = 0.5 * (np.linalg.norm(xy[1] - xy[0])
                        + np.linalg.norm(xy[2] - xy[3]))
            lm = 0.5 * (np.linalg.norm(xy[3] - xy[0])
                        + np.linalg.norm(xy[2] - xy[1]))
            ms.append(orient * A / max(lp * lm, ell2))
            depth.append((top - jnew) / top)
            where.append((i, jnew))
        M = max(j for (j, ii) in keys if ii == i)
    if with_depth:
        return np.array(ms), np.array(depth), where
    return np.array(ms)


def fold_census(out):
    """Columns whose recorded points are not strictly increasing in y."""
    keys = out["mesh_keys"]
    pts = np.asarray(out["mesh_pts"])
    cols = {}
    for n, (j, i) in enumerate(keys):
        cols.setdefault(i, []).append((j, pts[n, 1]))
    nfold, first = 0, None
    for i in sorted(cols):
        y = np.array([v for _, v in sorted(cols[i])])
        if (np.diff(y) <= 0).any():
            nfold += 1
            first = i if first is None else first
    return nfold, len(cols), first


def corner_vs_rao(W, w):
    """max over the first knot interval of (wall angle - Rao's wall
    angle), degrees: positive = the wall turned UP relative to Rao's
    (on the plug the wall lies below the flow: a compression corner)."""
    xq, yq, sq = (np.asarray(v) for v in R.stations(np.asarray(W, float), w))
    th_w = np.degrees(np.arctan(sq))
    sl_r = np.gradient(w.wall[:, 1], w.wall[:, 0])
    th_r = np.degrees(np.arctan(np.interp(xq, w.wall[:, 0], sl_r)))
    sel = (xq >= w.xs0) & (xq <= w.xk[0])
    d = th_w[sel] - th_r[sel]
    return float(d.max()), float(xq[sel][int(np.argmax(d))])


def margin_dict(rho, mu0, m_ref, orient, f_edge, ell2, tol=0.0):
    return dict(rho=float(rho), mu0=float(mu0), m_ref=float(m_ref),
                orient=float(orient), f_edge=float(f_edge), jmin=JMIN,
                ell2=float(ell2), tol=float(tol))


def load_designs():
    d = np.load(DESIGNS)
    return dict(xk=np.asarray(d["xk"]), W_fit=np.asarray(d["W_fit"], float),
                W_p=np.asarray(d["W_p"], float), W_s=np.asarray(d["W_s"], float),
                W_r=np.asarray(d["W_r"], float), J=np.asarray(d["J"], float),
                e_rep=float(d["e_rep"]), X0=float(d["X0"]), K=int(d["K"]),
                band=np.asarray(d["band"], float), V=np.asarray(d["V"], float),
                dw=np.asarray(d["dw"], float))


# ======================================================================
# stage audit
# ======================================================================
def audit():
    t00 = time.time()
    say("== [F3] OUR WORLD, the tournament row [X-OWAB] (stage audit):"
        " Rao vs the free-form spike at full expansion, class-certified ==")
    if not os.path.isdir(OW.RUN):
        say("   OW_GENO_RUN not a directory -- nothing to do")
        return False
    Wd = OW.load_world()
    OW.install(R, Wd)
    w = R.setup()
    N = len(w.start[1])
    K = R.K_ST
    say("   posing: X0 %.2f, K %d, N %d, M %d knots on [%.4f, %.4f], FREEZE"
        " %.2f (near-cut zone frozen to Rao's), tip pinned y_D %.4f"
        % (R.X0, K, N, R.M_NODES, w.xs0, w.xD, R.FREEZE, w.yD))
    D = load_designs()
    if not (np.allclose(D["xk"], w.xk) and D["K"] == K
            and abs(D["X0"] - R.X0) < EPS):
        say("FATAL: the designs of record (%s) were posed at knots %s, K %d,"
            " X0 %.2f -- not this posing" % (DESIGNS, D["xk"], D["K"], D["X0"]))
        return False
    check("A-0 the designs of record share this posing (knots, K, X0)", True)
    rec = dict(posing=dict(X0=R.X0, K=K, N=N, M=R.M_NODES, FREEZE=R.FREEZE,
                           xs0=w.xs0, xD=w.xD, yD=w.yD, pa=float(w.pa),
                           run=OW.RUN, ycut=OW.YCUT), designs=DESIGNS)
    ell = station_spacing(w)
    ell2 = ell * ell

    # ---- D1: orientation, bucket depth at the doubled resolution, m_ref
    say("-- D1: the margin of Rao's own contour: orientation, free-edge"
        " bucket (doubled resolution), m_ref, floors, rho --")
    t0 = time.time()
    mg = margin_dict(1.0, 0.0, 1.0, 1.0, 0.0, ell2)
    out, sch = march_m(D["W_fit"], w, mg)
    ms = np_margin(out, sch, N, 1.0, 0.0, ell2)
    orient = float(np.sign(np.median(ms)))
    say("  raw median %+.4f over %d whole-column cells -> orient %+.0f;"
        " cert %.3f (%.0f s)" % (np.median(ms), len(ms), orient,
                                 float(out["cert_worst"]), time.time() - t0))
    K2, N2 = 2 * K - 1, 2 * N - 1
    t0 = time.time()
    start2, _ = start_from_geno(Wd["fld"], Wd["wall"], R.X0, N2)
    ell2_2 = station_spacing(w, K2) ** 2
    mg2 = margin_dict(1.0, 0.0, 1.0, orient, 0.0, ell2_2)
    out2, sch2 = march_m(D["W_fit"], w, mg2, K=K2, start=start2)
    ms2, dep2, wh2 = np_margin(out2, sch2, N2, orient, 0.0, ell2_2,
                               with_depth=True)
    bad = ms2 <= 0.0
    d_meas = float(dep2[bad].max()) if bad.any() else 0.0
    f_edge = 0.5 * K_RICH * d_meas
    say("  Rao's contour at (%d,%d): %d whole-column cells, %d <= 0, deepest"
        " at row fraction %.3f from the top -> f_edge = K_RICH/2 x %.3f = %.3f;"
        " cert %.3f (%.0f s)"
        % (K2, N2, len(ms2), int(bad.sum()), d_meas, d_meas, f_edge,
           float(out2["cert_worst"]), time.time() - t0))
    check("D1a the non-positive cells of Rao's contour (if any) lie in the"
          " free-edge band, not the interior (depth < 1/2)", d_meas < 0.5)
    mg = margin_dict(1.0, 0.0, 1.0, orient, f_edge, ell2)
    out, sch = march_m(D["W_fit"], w, mg)
    ms = np_margin(out, sch, N, orient, f_edge, ell2)
    vmin_np, n_np = float(ms.min()), len(ms)
    vmin_il, n_il = float(out["margin_min"]), int(out["margin_n"])
    check("R-D0 in-loop margin == numpy census on Rao's contour (min %.6f vs"
          " %.6f, cells %d vs %d)" % (vmin_il, vmin_np, n_il, n_np),
          abs(vmin_il - vmin_np) <= K_RICH * EPS * max(1.0, abs(vmin_np))
          and n_il == n_np)
    check("A-1 Rao's contour is strictly healthy on the bucket (m_ref %.4f"
          " > 0; median %.4f)" % (vmin_np, np.median(ms)), vmin_np > 0.0)
    m_ref, Nc = vmin_np, n_np
    floors = [m_ref / 2 ** k for k in range(1, N_RUNGS + 1)]
    rho = K_RICH * np.log(Nc) / floors[-1]
    gap = np.log(Nc) / rho
    mg = margin_dict(rho, floors[0], m_ref, orient, f_edge, ell2, tol=gap)
    out_fit, S_fit = march_m(D["W_fit"], w, mg)
    ks = float(out_fit["margin_ks"])
    check("R-KS  vmin - ln N/rho = %.5f <= KS = %.5f <= vmin = %.5f"
          % (m_ref - gap, ks, m_ref),
          m_ref - gap - K_RICH * EPS <= ks <= m_ref + K_RICH * EPS)
    say("  m_ref %.4f (%d bucket cells), floors %s, rho %.1f, gap %.3e"
        % (m_ref, Nc, ["%.4f" % f for f in floors], rho, gap))
    rec.update(orient=orient, f_edge_meas=d_meas, f_edge=f_edge, m_ref=m_ref,
               N_cells=Nc, floors=floors, rho=rho, gap=gap, ell=ell, ell2=ell2,
               median=float(np.median(ms)), K2=K2, N2=N2)

    # ---- D2: the designs of record, graded
    say("-- D2: the S28 designs of record graded by the margin: min cell, KS,"
        " folded columns, compression corner against Rao's wall --")
    J_fit_rec, J_p_rec, J_s_rec, J_r_rec = D["J"]
    grades = {}
    for tag, Wd_ in (("W_fit (Rao)", D["W_fit"]), ("W_p (1.5 % start)", D["W_p"]),
                     ("W_s (returned optimum)", D["W_s"]),
                     ("W_r (rejector's minimizer)", D["W_r"])):
        t0 = time.time()
        o, s = march_m(Wd_, w, mg)
        nf, nc, first = fold_census(o)
        cdeg, cx = corner_vs_rao(Wd_, w)
        Jd = float(R.J_replay(jnp.asarray(Wd_), w, s))
        mn, ksd = float(o["margin_min"]), float(o["margin_ks"])
        say("  %-27s J %.8e cert %.3f | min cell %+.4f KS %+.4f (%d cells) |"
            " folded columns %d/%d (first %s) | corner vs Rao %+.2f deg at x %.2f"
            "  (%.0f s)" % (tag, Jd, float(o["cert_worst"]), mn, ksd,
                            int(o["margin_n"]), nf, nc, first, cdeg, cx,
                            time.time() - t0))
        grades[tag] = dict(J=Jd, cert=float(o["cert_worst"]), min_cell=mn, ks=ksd,
                           folded=nf, columns=nc, first_fold=first,
                           corner_deg=cdeg, corner_x=cx)
    check("A-2 the returned optimum W_s is IN the class at the tightest floor"
          " (min cell %+.4f >= mu0_1 %.4f) and unfolded (%d folded columns)"
          % (grades["W_s (returned optimum)"]["min_cell"], floors[0],
             grades["W_s (returned optimum)"]["folded"]),
          grades["W_s (returned optimum)"]["min_cell"] >= floors[0]
          and grades["W_s (returned optimum)"]["folded"] == 0)
    rec["grades"] = grades

    # ---- D3: the tournament value and its band
    say("-- D3: the tournament value: J(W_s) - J(W_fit) against band_J"
        " (v2 definition, recomputed here) --")
    t0 = time.time()
    J_fit, g_fit = R.J_and_grad(D["W_fit"], w, S_fit)
    out_fit2, _ = march_m(D["W_fit"], w, None, K=K2)
    J_fit2 = float(w.F_in + R.push_of(out_fit2, w))
    band_W = float(np.max(D["band"]))       # v3: the widest per-direction band
    band_J = K_RICH * abs(J_fit - J_fit2) + float(np.sum(np.abs(g_fit))) * band_W
    gain = grades["W_s (returned optimum)"]["J"] - J_fit
    say("  J_fit %.8e (K %d) vs %.8e (K %d): |dJ| %.3e; |grad J(W_fit)|_1 %.3e,"
        " widest v3 band %.3e -> band_J %.3e (%.0f s)"
        % (J_fit, K, J_fit2, K2, abs(J_fit - J_fit2), np.sum(np.abs(g_fit)),
           band_W, band_J, time.time() - t0))
    say("  record: J_fit %.8e, J_s %.8e (npz); here J_fit %.8e, J_s %.8e"
        % (J_fit_rec, J_s_rec, J_fit, grades["W_s (returned optimum)"]["J"]))
    check("A-3 TOURNAMENT VALUE: the free-form optimizer's return finds"
          " |J(W_s) - J(Rao)| = %.3e N (%+.2e of J) <= band_J %.3e: no gain"
          " over Rao outside the band at shared constraints"
          % (abs(gain), gain / J_fit, band_J), abs(gain) <= band_J)
    rec.update(J_fit=J_fit, J_fit2=J_fit2, band_J=band_J, band_W=band_W,
               gain_vs_rao=gain, gain_rel=gain / J_fit,
               g_floor_frozen=float(np.max(np.abs(g_fit))))

    # ---- A-4: the rejector — a 2 deg compression corner at the first free knot
    say("-- A-4 REJECTOR: Rao's contour with a %d deg compression corner at"
        " the first free knot (the S21 optimum's corner) --" % CORNER_DEG)
    dx = float(w.xk[0] - w.xs0)
    W_c = D["W_fit"].copy()
    W_c[0] += dx * np.tan(np.radians(CORNER_DEG))
    t0 = time.time()
    o, s = march_m(W_c, w, mg)
    nf, nc, first = fold_census(o)
    cdeg, cx = corner_vs_rao(W_c, w)
    mv, gm = margin_and_grad(W_c, w, s, mg)
    ksc, mnc = float(o["margin_ks"]), float(o["margin_min"])
    infeas = [bool(ksc < f) for f in floors]
    say("  first knot +%.1f mm: corner vs Rao %+.2f deg at x %.2f; cert %.3f;"
        " min cell %+.4f KS %+.4f; folded %d/%d (first %s); margin - mu0 %+.4f"
        " finite %s, |grad| %.2e finite %s (%.0f s)"
        % (1e3 * (W_c[0] - D["W_fit"][0]), cdeg, cx, float(o["cert_worst"]),
           mnc, ksc, nf, nc, first, mv, np.isfinite(mv), np.linalg.norm(gm),
           bool(np.all(np.isfinite(gm))), time.time() - t0))
    check("A-4 REJECTOR the cornered contour is INFEASIBLE at every floor %s"
          " with finite margin and gradient" % infeas,
          all(infeas) and np.isfinite(mv) and bool(np.all(np.isfinite(gm))))
    rec["rejector"] = dict(dy_mm=1e3 * (W_c[0] - D["W_fit"][0]), corner_deg=cdeg,
                           min_cell=mnc, ks=ksc, folded=nf, infeasible=infeas)

    # ---- D4: the near-cut zone free — the gradient floor, reported
    say("-- D4 (reported, not gated): the gradient floor of Rao's contour with"
        " the near-cut zone FREE (FREEZE 0) against the frozen posing --")
    t0 = time.time()
    fz = R.FREEZE
    R.FREEZE = 0.0
    w0 = R.setup()
    R.FREEZE = fz
    out0, S0 = march_m(w0.W_fit, w0, None)
    J0f, g0f = R.J_and_grad(w0.W_fit, w0, S0)
    e0 = R.wall_dist(w0.W_fit, w0)
    say("  FREEZE 0: knots on [%.2f, %.4f]; e_rep %.3e (frozen posing %.3e);"
        " |grad J(W_fit)|inf %.3e vs %.3e frozen (x%.1f); J_fit %.8e vs %.8e;"
        " cert %.3f (%.0f s)"
        % (w0.xs0, w0.xD, e0, D["e_rep"], np.max(np.abs(g0f)),
           np.max(np.abs(g_fit)), np.max(np.abs(g0f)) / np.max(np.abs(g_fit)),
           J0f, J_fit, float(out0["cert_worst"]), time.time() - t0))
    rec.update(free_posing=dict(xs0=w0.xs0, e_rep=e0, g_floor=float(
        np.max(np.abs(g0f))), J_fit=J0f, cert=float(out0["cert_worst"]),
        ratio_to_frozen=float(np.max(np.abs(g0f)) / np.max(np.abs(g_fit)))))
    rec.update(stage="audit", seconds=time.time() - t00,
               provenance="[X-OWAB] S29 audit on the [X-OWS3] designs of record")
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(AUDIT, "w"), indent=1)
    say("  audit written to %s" % AUDIT)
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage ab: the margin-constrained walk on this posing
# ======================================================================
def run_trsqp_margin(W0, w, mg, tr0, tr_floor, max_segments=SEGS,
                     maxiter_per_seg=ITERS, tag=""):
    """The [X-PSPL] segmented driver as rao1961_sqp_return carries it,
    with the [X-PMRG] margin path: constraint + memo, G1 surrogate,
    REQ-NONSTALL on the objective, the feasibility gate, a derived
    radius floor. Maximizes J."""
    from scipy.optimize import minimize, NonlinearConstraint
    W = np.asarray(W0, dtype=float)
    W_cert = None
    W_best, J_best, g_best, cw_best = None, -np.inf, None, None
    tr = tr0
    floor = tr_floor
    slack = floor * (1 + 1 / 100)
    n_rec = 0
    worst_cert = 0.0
    ctr = mg.setdefault("counters", dict(m_exec=0, m_dedup=0, m_nonfinite=0,
                                         gm_nonfinite=0))
    j_big = float(np.sqrt(np.finfo(float).max))
    for seg in range(max_segments):
        try:
            out_rec, sched = march_m(W, w, mg)
            n_rec += 1
            cw = float(out_rec["cert_worst"])
            if cw > 1.0:
                raise RuntimeError("record not certified (worst %.3e)" % cw)
        except Exception as err:
            if W_cert is not None and tr > floor:
                tr = max(floor, 0.5 * tr)
                say("    %s[seg %2d] base REJECTED (%s) -> revert, radius %.3e"
                    % (tag, seg, err, tr))
                W = W_cert.copy()
                continue
            raise
        J0, g0 = R.J_and_grad(W, w, sched)
        m0v = float(out_rec["margin_ks"]) - mg["mu0"]
        infeasible = (W_cert is not None and m0v < -mg["tol"])
        if infeasible:
            ctr["infeasible_base"] = ctr.get("infeasible_base", 0) + 1
        if (W_best is not None and J0 < J_best) or infeasible:
            why = ("INFEASIBLE (KS - mu0 %+.4f)" % m0v) if infeasible else "worse"
            if tr <= slack:
                say("    %s[seg %2d] trial %s at the radius floor -> converged"
                    % (tag, seg, why))
                break
            tr = max(floor, 0.5 * tr)
            say("    %s[seg %2d] trial J = %.8e REJECTED (%s) -> revert, radius"
                " %.3e" % (tag, seg, J0, why, tr))
            W = W_best.copy()
            continue
        W_cert = W.copy()
        worst_cert = max(worst_cert, cw)
        if J0 > J_best:
            W_best, J_best, g_best, cw_best = W.copy(), J0, g0.copy(), cw
        say("    %s[seg %2d] J = %.8e  |grad|inf = %.3e  cert = %.3e  KS - mu0"
            " %+.4f (min cell %+.4f)" % (tag, seg, J0, np.max(np.abs(g0)), cw,
                                          m0v, float(out_rec["margin_min"])))

        def fun(z):
            v, g = R.J_and_grad(z, w, sched)
            if not np.isfinite(v):
                ctr["obj_nonfinite"] = ctr.get("obj_nonfinite", 0) + 1
                return j_big, np.zeros_like(np.asarray(g))
            if not np.all(np.isfinite(g)):
                ctr["grad_nonfinite"] = ctr.get("grad_nonfinite", 0) + 1
                g = np.where(np.isfinite(g), g, 0.0)
            return -v, -g

        slot = dict(key=None, v=None, g=None)

        def _mvg(z):
            k = np.asarray(z, float).tobytes()
            if slot["key"] == k:
                ctr["m_dedup"] += 1
                return slot["v"], slot["g"].copy()
            v, g = margin_and_grad(z, w, sched, mg)
            ctr["m_exec"] += 1
            slot.update(key=k, v=v, g=g.copy())
            return v, g

        def m_np(z):
            v, _ = _mvg(z)
            if not np.isfinite(v):
                ctr["m_nonfinite"] += 1
                return -2.0 * K_RICH * mg["m_ref"]
            return v

        def gm_np(z):
            _, g = _mvg(z)
            if not np.all(np.isfinite(g)):
                ctr["gm_nonfinite"] += 1
                g = np.where(np.isfinite(g), g, 0.0)
            return g[None, :]
        cons = [NonlinearConstraint(m_np, 0.0, np.inf, jac=gm_np)]
        while True:
            res = minimize(fun, W, jac=True, method="trust-constr",
                           constraints=cons,
                           options=dict(maxiter=maxiter_per_seg,
                                        initial_tr_radius=tr, gtol=0.0,
                                        xtol=EPS * 100, verbose=0))
            step = float(np.linalg.norm(res.x - W))
            if step > K_RICH * EPS * max(1.0, float(np.linalg.norm(W))) \
                    or tr <= slack:
                break
            tr = max(floor, 0.5 * tr)
            say("    %s[seg %2d] no motion at radius %.3e -> retry at %.3e"
                % (tag, seg, 2 * tr, tr))
        mg["last_res"] = res
        say("    %s[seg %2d] margin counters %s; multipliers %s"
            % (tag, seg, {k: v for k, v in ctr.items() if v},
               [np.asarray(x).ravel().round(3).tolist() for x in (res.v or [])]
               if getattr(res, "v", None) is not None else None))
        if step <= K_RICH * EPS * max(1.0, float(np.linalg.norm(W))):
            say("    %s[seg %2d] no motion -> stop" % (tag, seg))
            break
        W = np.asarray(res.x, dtype=float)
        tr = float(min(0.25, 3 * tr / 2))
    return (W_best if W_best is not None else W), J_best, g_best, n_rec, worst_cert


def ab():
    t00 = time.time()
    say("== [F3] OUR WORLD, the tournament row [X-OWAB] (stage ab): the"
        " margin-constrained walk from Rao and from the perturbed start ==")
    if not os.path.exists(AUDIT):
        say("FATAL: no ab_audit.json at %s -- run the audit stage first" % AUDIT)
        return False
    Au = json.load(open(AUDIT))
    Wd = OW.load_world()
    OW.install(R, Wd)
    freeze = float(os.environ.get("OW_FREEZE", Au["posing"]["FREEZE"]))
    R.FREEZE = freeze
    w = R.setup()
    D = load_designs()
    same_class = abs(freeze - Au["posing"]["FREEZE"]) < EPS
    say("   class: FREEZE %.2f (%s the audited v3 class); floors %s; rho %.1f;"
        " gap %.3e" % (freeze, "=" if same_class else "NOT",
                       ["%.4f" % f for f in Au["floors"]], Au["rho"], Au["gap"]))
    mg = margin_dict(Au["rho"], Au["floors"][0], Au["m_ref"], Au["orient"],
                     Au["f_edge"], Au["ell2"], tol=Au["gap"])
    # the trust radius: derived from the fold scale along +grad J at Rao
    out_fit, S_fit = march_m(w.W_fit, w, mg)
    J_fit, g_fit = R.J_and_grad(w.W_fit, w, S_fit)
    u = g_fit / np.linalg.norm(g_fit)
    ell = Au["ell"]
    n_half = 5
    h_ok, h_bad = None, None
    say("-- the fold scale along +grad J at Rao's contour (step ladder"
        " ell 2^k) --")
    for k in range(-n_half, n_half + 1):
        h = ell * 2.0 ** k
        o, s = march_m(w.W_fit + h * u, w, mg)
        ksh = float(o["margin_ks"])
        say("    h %.3e m: KS %+.4f min %+.4f cert %.3f"
            % (h, ksh, float(o["margin_min"]), float(o["cert_worst"])))
        if ksh >= Au["floors"][0]:
            h_ok = h
        elif h_bad is None:
            h_bad = h
        if h_ok is not None and h_bad is not None and h_bad > h_ok:
            break
    bracketed = h_ok is not None and h_bad is not None and h_bad > h_ok
    check("R-FSC the margin along +grad J crosses mu0_1 inside the ladder"
          " (bracket [%s, %s])" % (h_ok, h_bad), bracketed)
    h_star = float(np.sqrt(h_ok * h_bad)) if bracketed else ell
    tr0 = h_star / K_RICH
    say("  h* %.3e m -> tr0 %.3e m, radius floor %.3e m" % (h_star, tr0,
                                                            tr0 / K_RICH))
    report = dict(audit=Au, freeze=freeze, h_star=h_star, tr0=tr0, walks=[])
    ok = True
    for tag, Ws in (("from Rao (W_fit)", w.W_fit.copy()),
                    ("from the 1.5 % start (W_p)", D["W_p"].copy()
                     if same_class else w.W_fit * (1.0 + R.PERT * np.array(
                         [(-1.0) ** k for k in range(len(w.W_fit))])))):
        say("-- walk %s: %d segments x %d iterations --" % (tag, SEGS, ITERS))
        t0 = time.time()
        mg_w = dict(mg)
        try:
            W_s, J_s, g_s, n_rec, wc = run_trsqp_margin(Ws, w, mg_w, tr0,
                                                        tr0 / K_RICH, tag=tag[:8])
        except Exception as err:
            say("  walk did not complete: %r -- a G1 rejector firing" % (err,))
            report["walks"].append(dict(start=tag, outcome="raise", error=repr(err)))
            ok = False
            continue
        dt = time.time() - t0
        o, s = march_m(W_s, w, mg)
        nf, nc, first = fold_census(o)
        cdeg, cx = corner_vs_rao(W_s, w)
        mn, ks = float(o["margin_min"]), float(o["margin_ks"])
        res = mg_w.get("last_res")
        mu = None
        if res is not None and getattr(res, "v", None):
            mu = -float(np.asarray(res.v[-1]).ravel()[0])
        active = (ks - mg["mu0"]) <= mg["tol"]
        gain = J_s - J_fit
        d_s = R.wall_dist(W_s, w)
        say("  [%s] %.0f s, %d records, worst cert %.3e: J* %.8e (J* - J_fit ="
            " %+.4e N, %+.2e of J), |grad|inf %.3e, dist to Rao %.3e, KS - mu0"
            " %+.4f (min cell %+.4f) -> %s, mu %s, folded %d/%d, corner vs Rao"
            " %+.2f deg, counters %s"
            % (tag, dt, n_rec, wc, J_s, gain, gain / J_fit, np.max(np.abs(g_s)),
               d_s, ks - mg["mu0"], mn, "ACTIVE" if active else "inactive",
               "%.3e" % mu if mu is not None else "n/a", nf, nc, cdeg,
               {k: v for k, v in mg_w.get("counters", {}).items() if v}))
        ok &= check("[%s] C-1 every accepted base certified (worst %.3e)"
                    % (tag, wc), wc <= 1.0)
        ok &= check("[%s] C-2 the returned base is IN the class (min cell %+.4f"
                    " >= mu0_1 %.4f; %d folded columns)" % (tag, mn, mg["mu0"], nf),
                    mn >= mg["mu0"] and nf == 0)
        ok &= check("[%s] C-3 TOURNAMENT VALUE |J* - J(Rao)| = %.3e <= band_J %.3e"
                    % (tag, abs(gain), Au["band_J"]), abs(gain) <= Au["band_J"])
        if active and mu is not None:
            ok &= check("[%s] C-4 dual clause mu >= 0 at an active margin (%.3e)"
                        % (tag, mu), mu >= 0.0)
        report["walks"].append(dict(start=tag, W=W_s.tolist(), J=J_s, gain=gain,
                                    gain_rel=gain / J_fit, cert=wc, min_cell=mn,
                                    ks=ks, active=bool(active), mu=mu, folded=nf,
                                    corner_deg=cdeg, dist_to_rao=d_s,
                                    records=n_rec, seconds=dt,
                                    counters=dict(mg_w.get("counters", {}))))
    report.update(J_fit=J_fit, stage="ab", segs=SEGS, iters=ITERS,
                  seconds=time.time() - t00,
                  provenance="[X-OWAB] S29 ab; posing = ourworld v3 twin mode")
    fn = os.path.join(ART, "ab_walk_f%.2f_s%d_i%d.json" % (freeze, SEGS, ITERS))
    json.dump(report, open(fn, "w"), indent=1)
    say("  report written to %s" % fn)
    return ok and NPASS[0] == NPASS[1]


if __name__ == "__main__":
    t0 = time.time()
    good = ab() if STAGE == "ab" else audit()
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    sys.exit(0 if good else 1)

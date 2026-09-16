#!/usr/bin/env python3
"""[X-PMRG] THE FOLD MARGIN OF THE PLUG [F3/A1] — M0 Part VI's
margin-constrained formulation (max J s.t. g = 0 AND m(W) >= mu_0,
KKT with the margin multiplier mu; D6 REQ-NONSTALL: the margin is a
constraint WITH a gradient — it steers, never stalls, never lets
through) ported from the bell governor [X-MGOV] to the certified plug
march [X-PLUG] and the free-form spike [X-PSPL]. S29 2026-09-16, log
validation/PROGRESS_2026-09-16_S29_readjudication.md (secs. 5.1-5.3:
the field chosen and measured before any code, the derive stage on a
scratch port, the first constrained walk).

WHY. The brick-2 plug line certified its designs cell by cell (Newton
residual, descent, clear of the axis) and never asked whether the
march stayed in the class it is certified FOR: the shock-free one.
Re-adjudicated with the amended S22/S23 carriers (S28 addendum B,
S29 secs. 1-4), every unconstrained free-form optimum of the line
turned out to impose a 12-15 deg compression corner at the wall foot
whose same-family characteristics cross downstream — a folded,
multi-valued march that certifies at every cell (a folded cell solves
its compatibility relations as well as any other) and books a
"gain" through the tangled net. The program already owns the answer
to interior coalescence — the fold margin — and the plug line had
never used it. This carrier makes it executable on the plug.

THE MARGIN FIELD (M0: "distance from same-family characteristic
coalescence"), measured directly on the recorded net rather than
through the governor's `val` (that is Sternin / Rao-Beck Eq. (4), a
pointwise STATE criterion — legitimately negative on certified DEF
fields, and healthy on every rejected bell design of the S20
standoff; it is not a fold detector): for every interior point
(jnew, i) the TRUE net cell [(jprev-1, i-1), (jprev, i-1), (jnew, i),
(jnew-1, i)], jprev = jnew + jsrc0 - 2 from the recorded wall-foot
schedule (row consumption at the wall makes index-aligned
quadrilaterals WRONG — the 2026-09-15 census used them; its
column-wise y-monotonicity census did not, and stands), and

    m = orient * signed area / max(mean C+ leg * mean C- leg, ell^2),

the local Jacobian of the net as the sine of the angle between the
families: healthy reference sin(2 alpha) (median 0.667 = the median
sin 2 alpha on the incumbent, KNOWN ANSWER, sec. 5.1); zero =
coalescence; negative = a fold. The leg product is FLOORED at the
station spacing squared (ell = (L - X0)/(K - 1)): a fold counts when
its inverted cells are RESOLVED — without the floor the 2 mm
free-jet ripples of the incumbent (physical coalescence of weak
compressions at the far end of the C+ lines) weighed like a 30 cm
fold; the criterion tightens under refinement, with the ladder. The
BUCKET excludes the thin row-growth cells at the free jet:
rows_from_top > f_edge * (rows in the column), f_edge = K_RICH/2 x
the measured depth of the deepest non-positive incumbent cell at the
doubled resolution (derived here, D1; 0.11 -> 0.22 on the S21
posing). The margin is computed IN-LOOP by a1_plug_march
(margin=dict(...)): the four corners are in G when the point is
solved, KS-aggregated ONLINE with logaddexp (no mesh stack: the S23
compile lesson), returned as a traced scalar in play mode, so the
constraint's gradient is exact reverse-mode AD through the same
frozen-schedule replay as the objective.

DERIVATIONS OF RECORD (R5 — every constant derived or measured; the
governor's derivations re-used where they apply):
 * KS-MIN AGGREGATE [THEOREM-level, standard]: KS_rho = -(1/rho) ln
   sum exp(-rho m_i) satisfies m_min - ln(N)/rho <= KS <= m_min
   (conservative side: KS >= mu_0 => min m >= mu_0). Checked on the
   incumbent field (R-KS).
 * rho DERIVED as in [X-MGOV]: rho = K_RICH ln(N) / mu_0_min, N =
   measured bucket-cell count, mu_0_min = the smallest floor.
 * FLOOR LADDER mu_0_k = m_ref / 2^k, k = 1..4, m_ref = min m over
   the incumbent's bucket (MEASURED healthy reference: the incumbent
   is strictly feasible at every rung by construction). Activity is
   monotone in mu_0 (a looser floor cannot activate what the tighter
   one left slack): the campaign walks the TIGHTEST rung first and
   stops with the derivation printed if it is inactive there.
 * ORIENTATION measured (D0): the sign of the median cell area in the
   A->B->C->D traversal on the incumbent (-1 on this net), applied so
   that healthy = positive.
 * FOLD SCALE h* (D4): the step along +grad J (the unconstrained
   optimizer's own direction, 0.97 on the first knot) at which the
   incumbent's margin crosses mu_0_1 — bracketed on a geometric step
   ladder ell 2^k, h* = the geometric mean of the bracket; the
   campaign's initial trust radius is DERIVED from it, tr0 = h* /
   K_RICH (the unconstrained default 0.05 m is 20x the fold scale:
   trust-constr's first trials then land deep in the fold, their
   zeroed gradients poison the segment model, and the walk stalls —
   measured, sec. 5.2 (b)).
 * G1 SURROGATE [PRACTICE, rejector-gated]: a non-finite margin
   returns -2 K_RICH m_ref (finite negative); non-finite gradient
   components are zeroed AND COUNTED; the OBJECTIVE carries the same
   REQ-NONSTALL contract (the bell's f_np/g_np, S21 C2) when a margin
   is present — on a folded TRIAL design the replayed J has a finite
   value and an all-NaN adjoint (measured, sec. 5.2 (a)); a silent
   NaN crashed trust-constr's normal step. The counters are
   verdict-bearing: a walk that could not complete is a G1 firing.
 * MULTIPLIER: scipy's trust-constr multiplier of the KS constraint
   is reported with the B-STATIONARITY wording (O1 open in M0: the
   Danskin/Clarke cusp derivative is undischarged, so mu is the
   solver's surrogate estimate; mu > 0 = margin-active). Dual clause
   (unilateral constraint, [T-T7CN] regime 3): mu >= 0 with
   complementarity — checked, not assumed.

MACHINERY REJECTORS (stage derive, all must pass before the campaign):
 (R-D0) the in-loop margin reproduces a numpy census on the same
        record EXACTLY (min and count) — the hook is at the right
        cell; (R-KS) the KS bounds hold on the incumbent field;
 (R-GRAD) the AD margin gradient matches a three-step central-FD
        ladder in two random directions inside the ladder's own
        band, AND a corrupted-gradient control (one component
        doubled) FAILS the same check; (R-G1) the S22 m 12 design,
        the S22 cycle-1 m 11 design and the S23 fine optimum — the
        folded designs of record — are INFEASIBLE at every floor
        with FINITE margin and gradient (the rejector: a margin that
        let them through would be no margin); (R-FSC) the fold scale
        is bracketed (the margin along +grad J crosses mu_0_1 inside
        the ladder), so tr0 is derived, not assumed.

CAMPAIGN (stage campaign, consumes derive.json — nothing here is
typed twice): the S21 posing (L = 2.5 m, theta_E = 0, m = 10 uniform
knots, (61,51)), started at the fan streamline, margin-constrained
TR-SQP on the floor ladder (tightest first, warm-started
continuation, monotonicity stop). Per rung the MANDATORY logs: J and
gain over the streamline, KS - mu_0 and the min cell at the returned
base, activity (KS - mu_0 <= ln N / rho), mu (B-stationarity), the
REQ-NONSTALL counters, certification, the wall angle at the first
station against the incoming flow, the ACTIVE-CUSP CENSUS (bucket
cells with m <= mu_0 + ln N / rho, by column, clustered by
contiguity). Then the RESOLUTION LADDER of the tightest-rung design:
at (2K-1, 2N-1) and (4K-3, 4N-3) its certification and margin
against the incumbent's own m_ref at that resolution (the criterion
tightens: class membership is asked at every rung, never assumed
from the coarse one). A second start (PMRG_STARTS=2): the streamline
displaced by h*/2 along +grad J — inside the class by the fold scale,
leaning into the lever. Verdict checks: every accepted base
certified; the walk completed (REQ-NONSTALL) with finite J, gradient
and margin at the returned base; no loss to its own start; the
returned base feasible (KS - mu_0 >= -ln N / rho, the aggregation
gap); mu >= 0 where active (dual clause). The GAIN is reported
against the S21 band of record at this resolution (0.19 percent) —
a reading, not a gate: the claim this carrier can support is "the
free-form optimum IN the shock-free class at L = 2.5 m, with the
measured price of staying in it", nothing about resolution until the
ladder is walked with the margin on (the S21 -> S22 -> S23
re-runs, PROGRESS NEXT-PARALLELO 1-bis).

ON-DEMAND CARRIER (env: jax). A1_PMRG_STAGE in {derive, campaign}
(default derive); PMRG_SEGS / PMRG_ITERS = segments per rung /
trust-constr iterations per segment (defaults 4 / 12 = the first walk
of record); PMRG_STARTS (1 or 2); PMRG_RUNGS (floor rungs, default 4);
PMRG_LADDER=0 skips the resolution ladder (smoke tests). Artifacts in
validation/_plug_margin/ (derive.json, campaign_*.json committed; npz
not, per the S24 convention).
"""
import json
import os
import sys
import time

import numpy as np

# the S21 posing of record: constants of a1_plug_spline_opt are read
# at import (PSPL_M/K/N); set BEFORE the import unless the caller did
os.environ.setdefault("PSPL_M", "10")
os.environ.setdefault("PSPL_K", "61")
os.environ.setdefault("PSPL_N", "51")

import jax                                              # noqa: E402
import jax.numpy as jnp                                 # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                         # noqa: E402
import a1_config_compare as CC                          # noqa: E402
import a1_plug_spline_opt as P                          # noqa: E402

K_RICH = A1.K_RICH
EPS = A1.EPS
HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.environ.get("PMRG_ART", os.path.join(HERE, "_plug_margin"))
DERIVE = os.path.join(ART, "derive.json")
STAGE = os.environ.get("A1_PMRG_STAGE", "derive")
SEGS = int(os.environ.get("PMRG_SEGS", 4))
ITERS = int(os.environ.get("PMRG_ITERS", 12))
STARTS = int(os.environ.get("PMRG_STARTS", 1))
RUNGS = int(os.environ.get("PMRG_RUNGS", 4))
LADDER = int(os.environ.get("PMRG_LADDER", 1))
JMIN = 2                     # wall cells included (row 1 = the wall)
N_FD = 3                     # central-FD ladder steps
N_DIR = 2                    # random directions for R-GRAD
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


# ======================================================================
# the numpy census on a record: the independent twin of the in-loop
# margin (R-D0), also the source of the row-depth measurement (D1)
# ======================================================================
def np_margin(out, sch, N_rows, orient, f_edge, ell2, jmin=JMIN,
              with_depth=False, with_floor=False):
    """Per-cell margins over the bucket, from the recorded net and the
    recorded wall-foot schedule (jsrc0 per column). with_depth also
    returns each cell's rows_from_top / column height and (col, row);
    with_floor (additive, X-PTRN 2026-09-16) appends the per-cell flag
    'the leg product sat below the floor ell2' -- the cell is UNRESOLVED
    by the criterion's own definition (its margin is A / ell2, not
    sin 2 alpha), which is what the free-jet slivers of a coarse net
    are."""
    keys = out["mesh_keys"]
    pts = np.asarray(out["mesh_pts"])
    idx = {k: n for n, k in enumerate(keys)}
    ms, depth, where, floored = [], [], [], []
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
            floored.append(lp * lm < ell2)
        M = max(j for (j, ii) in keys if ii == i)
    if with_depth and with_floor:
        return np.array(ms), np.array(depth), where, np.array(floored)
    if with_depth:
        return np.array(ms), np.array(depth), where
    return np.array(ms)


def margin_dict(rho, mu0, m_ref, orient, f_edge, ell2):
    return dict(rho=float(rho), mu0=float(mu0), m_ref=float(m_ref),
                orient=float(orient), f_edge=float(f_edge),
                jmin=JMIN, ell2=float(ell2))


def wall_angle_deg(W, c, K=None):
    _, _, sq = P.wall_stations(np.asarray(W, float), c, K=K)
    return float(np.degrees(np.arctan(float(np.asarray(sq)[0]))))


def flow_angle_deg(c):
    us, vs = np.asarray(c["start"][2]), np.asarray(c["start"][3])
    return float(np.degrees(np.arctan2(vs[0], us[0])))


def station_spacing(K):
    return (P.L - P.X0) / (K - 1)


def load_folded_designs(c):
    """The folded designs of record (S28 addendum B / S29): the S22 m 12
    design (committed json), the S22 cycle-1 m 11 design and the S23
    fine optimum (run npz, untracked by convention -> declared skip
    when absent)."""
    out = []
    pj = os.path.join(HERE, "_plug_adaptive", "design_m10_k61_n51.json")
    if os.path.exists(pj):
        art = json.load(open(pj))
        out.append(("S22 adaptive m%d" % len(art["design"]["W"]),
                    np.array([float(eval(v)) for v in art["design"]["xk"]]),
                    np.array([float(eval(v)) for v in art["design"]["W"]])))
    pc = os.path.join(HERE, "_plug_adaptive", "cycle_m10_k61_n51_01.npz")
    if os.path.exists(pc):
        d = np.load(pc)
        out.append(("S22 cycle-1 m%d" % len(d["W"]), np.asarray(d["xk"]),
                    np.asarray(d["W"], float)))
    pf = os.path.join(HERE, "_plug_gain", "fineopt.npz")
    if os.path.exists(pf):
        d = np.load(pf)
        out.append(("S23 fine m%d" % len(d["W_fine"]), np.asarray(d["xk"]),
                    np.asarray(d["W_fine"], float)))
    return out


# ======================================================================
# stage derive
# ======================================================================
def derive():
    t00 = time.time()
    say("== A1 S29: the fold margin of the plug [X-PMRG] (stage derive) ==")
    w = CC.build_world()
    ta = w["ta"]
    c = P.build_case(w)
    K, N = P.K_ST, P.N_ROW
    W0 = np.asarray(c["W0"], float)
    ell = station_spacing(K)
    ell2 = ell * ell
    say("  posing: L %.3f m, theta_E %.1f deg, m %d knots, (K,N) = (%d,%d),"
        " ell %.4e m (leg floor ell^2 %.3e m^2)"
        % (P.L, P.THE_OPT, len(W0), K, N, ell, ell2))
    rec = dict(K=K, N=N, m=len(W0), L=P.L, X0=P.X0, ell=ell, ell2=ell2,
               jmin=JMIN)

    # ---- D0: orientation + in-loop vs numpy on the SAME record
    say("-- D0: orientation, and the in-loop margin against a numpy census"
        " of the same record --")
    mg = margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=1.0, f_edge=0.0,
                     ell2=ell2)
    out, sch = P.march_record(W0, w, c, margin=mg)
    ms = np_margin(out, sch, N, 1.0, 0.0, ell2)
    orient = float(np.sign(np.median(ms)))
    say("  raw median %+.4f over %d whole-column cells -> orient %+.0f"
        % (np.median(ms), len(ms), orient))
    rec["orient"] = orient

    # ---- D1: the edge bucket, measured at the doubled resolution
    say("-- D1: the free-edge bucket depth (doubled resolution), m_ref,"
        " floors, rho --")
    K2, N2 = 2 * K - 1, 2 * N - 1
    c2 = dict(P.build_case(w, N=N2))
    c2["xk"] = c["xk"]
    W02 = np.interp(c["xk"], c2["sx"], c2["sy"])
    t0 = time.time()
    mg2 = margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=orient,
                      f_edge=0.0, ell2=station_spacing(K2) ** 2)
    out2, sch2 = P.march_record(W02, w, c2, K=K2, margin=mg2)
    ms2, dep2, wh2 = np_margin(out2, sch2, N2, orient, 0.0,
                               station_spacing(K2) ** 2, with_depth=True)
    bad = ms2 <= 0.0
    d_meas = float(dep2[bad].max()) if bad.any() else 0.0
    f_edge = 0.5 * K_RICH * d_meas
    say("  incumbent at (%d,%d): %d whole-column cells, %d <= 0, deepest"
        " at row fraction %.3f from the top (col %s) -> f_edge = K_RICH/2"
        " x %.3f = %.3f (%.0f s)"
        % (K2, N2, len(ms2), int(bad.sum()), d_meas,
           wh2[int(np.argmax(dep2 * bad))][0] if bad.any() else None,
           d_meas, f_edge, time.time() - t0))
    check("D1a the incumbent's non-positive cells (if any) lie in the"
          " free-edge band, not the interior (depth < 1/2)",
          d_meas < 0.5)
    rec.update(f_edge_meas=d_meas, f_edge=f_edge, K2=K2, N2=N2)
    # the working-resolution field with the bucket applied
    mg = margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=orient,
                     f_edge=f_edge, ell2=ell2)
    out, sch = P.march_record(W0, w, c, margin=mg)
    ms = np_margin(out, sch, N, orient, f_edge, ell2)
    vmin_np, n_np = float(ms.min()), len(ms)
    vmin_il, n_il = float(out["margin_min"]), int(out["margin_n"])
    say("  bucket (61,51): in-loop min %+.6f / %d cells vs numpy min"
        " %+.6f / %d cells (diff %.1e); median %.4f"
        % (vmin_il, n_il, vmin_np, n_np, abs(vmin_il - vmin_np),
           np.median(ms)))
    check("R-D0 in-loop margin == numpy census (min within %d eps, same"
          " cell count)" % int(K_RICH),
          abs(vmin_il - vmin_np) <= K_RICH * EPS * max(1.0, abs(vmin_np))
          and n_il == n_np)
    check("R-D0b the incumbent is strictly healthy on the bucket (min > 0)",
          vmin_np > 0.0)
    m_ref = vmin_np
    Nc = n_np
    floors = [m_ref / 2 ** k for k in range(1, RUNGS + 1)]
    rho = K_RICH * np.log(Nc) / floors[-1]
    gap = np.log(Nc) / rho
    say("  m_ref %.4f (min over %d bucket cells), floors mu0_k = m_ref/2^k"
        " = %s, rho = K_RICH ln N / mu0_%d = %.1f, KS gap ln N / rho ="
        " %.3e (= mu0_min / K_RICH)"
        % (m_ref, Nc, ["%.4f" % f for f in floors], RUNGS, rho, gap))
    mg = margin_dict(rho=rho, mu0=floors[0], m_ref=m_ref, orient=orient,
                     f_edge=f_edge, ell2=ell2)
    out, sch = P.march_record(W0, w, c, margin=mg)
    ks, vmin = float(out["margin_ks"]), float(out["margin_min"])
    check("R-KS  vmin - ln N/rho = %.5f <= KS = %.5f <= vmin = %.5f"
          % (vmin - gap, ks, vmin),
          vmin - gap - K_RICH * EPS <= ks <= vmin + K_RICH * EPS)
    rec.update(m_ref=m_ref, N_cells=Nc, floors=floors, rho=rho, gap=gap,
               median=float(np.median(ms)))

    # ---- D2: AD vs FD on the frozen schedule, plus the corrupted control
    say("-- D2: AD margin gradient vs a %d-step central-FD ladder (frozen"
        " schedule, incumbent), and a corrupted-gradient control --"
        % N_FD)
    t0 = time.time()
    mv, gm = P.margin_and_grad(W0, w, c, sch, mg)
    say("  margin - mu0_1 = %+.5f, |grad| %.3e (%.0f s incl. compile)"
        % (mv, np.linalg.norm(gm), time.time() - t0))
    rng = np.random.default_rng(0)
    # probe steps DERIVED below the fold scale: ell / K_RICH^k, k = 3..5
    # (0.56 / 0.14 / 0.035 mm at ell 35.8 mm) -- the S29 scratch ladder
    # 1e-4..1e-6 m sat in the same decade; a step at the fold scale
    # (mm) would difference across the class boundary
    hs = [ell / K_RICH ** k for k in range(N_FD, 2 * N_FD)]
    fj = lambda z: float(P.margin_replay(jnp.asarray(z), w, c, sch, mg))  # noqa
    for k in range(N_DIR):
        v = rng.standard_normal(len(W0))
        v /= np.linalg.norm(v)
        vals = np.array([(fj(W0 + h * v) - fj(W0 - h * v)) / (2 * h)
                         for h in hs])
        spread = vals.max() - vals.min()
        band = K_RICH * spread + K_RICH * EPS * abs(mv) / hs[-1]
        ad = float(gm @ v)
        check("R-GRAD dir %d: AD %+.5e  FD ladder %s  |diff| %.2e band %.2e"
              % (k, ad, np.array2string(vals, precision=5),
                 abs(vals[-1] - ad), band), abs(vals[-1] - ad) <= band)
        if k == 0:
            g_bad = gm.copy()
            jb = int(np.argmax(np.abs(g_bad)))
            g_bad[jb] *= 2.0
            adb = float(g_bad @ v)
            check("R-GRAD control: the corrupted gradient (component %d"
                  " doubled) FAILS the same check (|diff| %.2e > band %.2e)"
                  % (jb, abs(vals[-1] - adb), band),
                  abs(vals[-1] - adb) > band)

    # ---- D3: the folded designs of record are infeasible at every floor
    say("-- D3: the folded designs of record must be INFEASIBLE at every"
        " floor with finite margin and gradient (REJECTOR) --")
    designs = load_folded_designs(c)
    if not designs:
        say("  declared skip: no folded design artifact on disk")
    for tag, xkd, Wd in designs:
        cm = dict(c, xk=np.asarray(xkd))
        o, s = P.march_record(Wd, w, cm, margin=mg)
        ksd, mn = float(o["margin_ks"]), float(o["margin_min"])
        mvd, gmd = P.margin_and_grad(Wd, w, cm, s, mg)
        infeas = [bool(ksd < f) for f in floors]
        check("R-G1 %s: KS %+.4f (min cell %+.4f, %d cells; wall theta"
              " st.1 %+.2f deg vs flow %+.2f) infeasible at every floor %s;"
              " margin %+.4f finite %s, grad finite %s |g| %.2e"
              % (tag, ksd, mn, int(o["margin_n"]), wall_angle_deg(Wd, cm),
                 flow_angle_deg(c), infeas, mvd, np.isfinite(mvd),
                 bool(np.all(np.isfinite(gmd))), np.linalg.norm(gmd)),
              all(infeas) and np.isfinite(mvd)
              and bool(np.all(np.isfinite(gmd))))

    # ---- D4: the fold scale along +grad J, and tr0
    say("-- D4: the fold scale h* along +grad J (the optimizer's own"
        " direction), bracketed on a step ladder; tr0 = h*/K_RICH --")
    J0, gJ = P.J_and_grad(W0, w, c, ta, sch)
    u = gJ / np.linalg.norm(gJ)
    say("  J(streamline) %.8e  |grad J| %.3e  direction %s"
        % (J0, np.linalg.norm(gJ), np.array2string(u, precision=3)))
    n_half = 5                        # ladder ell 2^-5 .. ell 2^+5
    h_ok, h_bad, rows = None, None, []
    for k in range(-n_half, n_half + 1):
        h = ell * 2.0 ** k
        o, s = P.march_record(W0 + h * u, w, c, margin=mg)
        ksh, mnh = float(o["margin_ks"]), float(o["margin_min"])
        Jh = float(P.J_replay(jnp.asarray(W0 + h * u), w, c, s, ta))
        cw = float(o["cert_worst"])
        rows.append(dict(h=h, J=Jh, ks=ksh, mmin=mnh, cert=cw))
        say("    h %.3e m: J %.7e (%+.4f %%)  KS %+.4f  min %+.4f  cert %.3f"
            "  theta st.1 %+.2f" % (h, Jh, 100 * (Jh / J0 - 1), ksh, mnh,
                                    cw, wall_angle_deg(W0 + h * u, c)))
        if ksh >= floors[0]:
            h_ok = h
        elif h_bad is None:
            h_bad = h
        if h_bad is not None and h_ok is not None and h_bad > h_ok:
            break
    bracketed = (h_ok is not None and h_bad is not None and h_bad > h_ok)
    check("R-FSC the margin along +grad J crosses mu0_1 inside the ladder"
          " (bracket [%s, %s] m)" % (h_ok, h_bad), bracketed)
    h_star = float(np.sqrt(h_ok * h_bad)) if bracketed else float("nan")
    tr0 = h_star / K_RICH
    say("  h* = sqrt(%.3e x %.3e) = %.3e m -> tr0 = h*/K_RICH = %.3e m"
        % (h_ok or np.nan, h_bad or np.nan, h_star, tr0))
    rec.update(J0=float(J0), gradJ_dir=u.tolist(), fold_ladder=rows,
               h_ok=h_ok, h_bad=h_bad, h_star=h_star, tr0=tr0,
               flow_angle_deg=flow_angle_deg(c),
               wall_angle_deg_inc=wall_angle_deg(W0, c),
               stage="derive", seconds=time.time() - t00,
               provenance="[X-PMRG] S29 derive; posing = S21 [X-PSPL]")
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(DERIVE, "w"), indent=1)
    say("  derived constants written to %s" % DERIVE)
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage campaign
# ======================================================================
def cusp_census(out, sch, N_rows, mg, floors_k):
    """Active-cusp census on a record: bucket cells with m <= mu0 + gap,
    by column, clustered by contiguity."""
    ms, _, wh = np_margin(out, sch, N_rows, mg["orient"], mg["f_edge"],
                          mg["ell2"], with_depth=True)
    thr = floors_k + np.log(len(ms)) / mg["rho"]
    act = [wh[n] for n in range(len(ms)) if ms[n] <= thr]
    cols = sorted(set(i for i, _ in act))
    clusters = 0
    prev = None
    for i in cols:
        if prev is None or i != prev + 1:
            clusters += 1
        prev = i
    return dict(n_active=len(act), columns=cols, clusters=clusters,
                threshold=float(thr), argmin=wh[int(np.argmin(ms))],
                min=float(ms.min()))


def campaign():
    t00 = time.time()
    say("== A1 S29: the fold margin of the plug [X-PMRG] (stage campaign) ==")
    if not os.path.exists(DERIVE):
        say("FATAL: no derive.json at %s — run the derive stage first"
            % DERIVE)
        return False
    D = json.load(open(DERIVE))
    w = CC.build_world()
    ta = w["ta"]
    c = P.build_case(w)
    K, N = P.K_ST, P.N_ROW
    if (K, N, len(c["W0"])) != (D["K"], D["N"], D["m"]):
        say("FATAL: posing (%d,%d,m%d) differs from derive.json (%d,%d,m%d)"
            % (K, N, len(c["W0"]), D["K"], D["N"], D["m"]))
        return False
    W0 = np.asarray(c["W0"], float)
    floors, rho, gap = D["floors"][:RUNGS], D["rho"], D["gap"]
    tr0 = D["tr0"]
    u = np.asarray(D["gradJ_dir"], float)
    th_flow = D["flow_angle_deg"]
    say("  posing (%d,%d) m %d; floors %s; rho %.1f; gap %.3e; tr0 %.3e m"
        " (radius floor tr0/K_RICH %.3e m); segments/rung %d x %d"
        " iterations; starts %d"
        % (K, N, len(W0), ["%.4f" % f for f in floors], rho, gap, tr0,
           tr0 / K_RICH, SEGS, ITERS, STARTS))
    base_mg = dict(rho=rho, m_ref=D["m_ref"], orient=D["orient"],
                   f_edge=D["f_edge"], jmin=JMIN, ell2=D["ell2"],
                   tol=gap)      # feasibility gate of run_trsqp
    mg0 = dict(base_mg, mu0=floors[0])
    o0, s0 = P.march_record(W0, w, c, margin=mg0)
    J0 = float(P.J_replay(jnp.asarray(W0), w, c, s0, ta))
    say("  streamline: J %.8e cert %.3f KS %+.4f min %+.4f"
        % (J0, float(o0["cert_worst"]), float(o0["margin_ks"]),
           float(o0["margin_min"])))
    starts = [("A streamline", W0.copy())]
    if STARTS >= 2:
        starts.append(("B streamline + h*/2 along +grad J",
                       W0 + 0.5 * D["h_star"] * u))
    report = dict(derive=D, rungs=[], ladder=[], starts=[])
    ok = True
    for stag, Ws in starts:
        say("-- start %s --" % stag)
        W_cur = Ws.copy()
        last_ok = None
        for k, mu0 in enumerate(floors, start=1):
            mg = dict(base_mg, mu0=mu0)
            say("-- rung %d/%d: mu0 = %.5f (start %s) --"
                % (k, len(floors), mu0, stag[:1]))
            t0 = time.time()
            try:
                W_new, hist, n_rec = P.run_trsqp(
                    W_cur.copy(), w, c, ta, max_segments=SEGS,
                    maxiter_per_seg=ITERS, margin=mg, tr0=tr0,
                    tr_floor=tr0 / K_RICH)     # derived, not the 1 mm policy
            except Exception as err:            # REQ-NONSTALL breach
                say("  [rung %d] walk did not complete: %r — a G1"
                    " rejector firing; campaign stops here" % (k, err))
                report["rungs"].append(dict(start=stag, rung=k, mu0=mu0,
                                            outcome="raise",
                                            error=repr(err)))
                ok = False
                break
            dt = time.time() - t0
            o, s = P.march_record(W_new, w, c, margin=mg)
            Jn, gn = P.J_and_grad(W_new, w, c, ta, s)
            mvn, gmn = P.margin_and_grad(W_new, w, c, s, mg)
            ksn, mnn = float(o["margin_ks"]), float(o["margin_min"])
            cw = float(o["cert_worst"])
            res = mg.get("last_res")
            mu = None
            if res is not None and getattr(res, "v", None):
                mu = -float(np.asarray(res.v[-1]).ravel()[0])
            active = (ksn - mu0) <= gap
            ctr = mg.get("counters", {})
            cen = cusp_census(o, s, N, mg, mu0)
            th_w = wall_angle_deg(W_new, c)
            gain = 100.0 * (float(Jn) / J0 - 1.0)
            say("  [rung %d] %.0f s, %d segments, %d records: J %.8e"
                " (%+.5f %% vs streamline), cert %.3f, |grad J| %.3e,"
                " KS - mu0 %+.5f (min cell %+.4f) -> %s, mu = %s"
                " (B-stationarity), theta st.1 %+.2f deg (flow %+.2f),"
                " W - W0 [mm] %s, counters %s"
                % (k, dt, len(hist), n_rec, Jn, gain, cw,
                   np.linalg.norm(gn), ksn - mu0, mnn,
                   "ACTIVE" if active else "inactive",
                   "%.4e" % mu if mu is not None else "n/a", th_w, th_flow,
                   np.array2string(1e3 * (W_new - W0), precision=2),
                   {kk: v for kk, v in ctr.items() if v}))
            say("  [rung %d] active-cusp census: %d cells <= mu0 + gap"
                " (%.5f) in columns %s (%d cluster(s)); argmin cell %s"
                " (m %.4f)"
                % (k, cen["n_active"], cen["threshold"], cen["columns"],
                   cen["clusters"], cen["argmin"], cen["min"]))
            ok &= check("rung %d C-1 the returned base is Newton-certified"
                        " (%.3f)" % (k, cw), cw <= 1.0)
            ok &= check("rung %d C-2 REQ-NONSTALL: J, grad J, margin and"
                        " its gradient finite at the returned base"
                        % k, np.isfinite(Jn) and np.all(np.isfinite(gn))
                        and np.isfinite(mvn) and np.all(np.isfinite(gmn)))
            ok &= check("rung %d C-3 no loss to its own start (J %.8e >="
                        " %.8e)" % (k, Jn, J0), float(Jn) >= J0 - K_RICH
                        * EPS * abs(J0))
            ok &= check("rung %d C-4 the returned base is feasible within"
                        " the aggregation gap (KS - mu0 %+.5f >= %+.5f)"
                        % (k, ksn - mu0, -gap), ksn - mu0 >= -gap)
            if active and mu is not None:
                ok &= check("rung %d C-5 dual clause: mu >= 0 at an active"
                            " margin (%.4e)" % (k, mu), mu >= 0.0)
            report["rungs"].append(dict(
                start=stag, rung=k, mu0=mu0, J=float(Jn), gain_pct=gain,
                cert=cw, ks_minus_mu0=ksn - mu0, min_cell=mnn,
                active=bool(active), mu=mu, theta_wall_deg=th_w,
                W=W_new.tolist(), segments=len(hist), records=n_rec,
                seconds=dt, counters=dict(ctr), census=cen))
            last_ok = (W_new.copy(), k, mu0)
            moved = float(np.linalg.norm(W_new - W_cur)) > 0.0
            if k == 1 and not active and moved:
                say("  [rung 1] the margin is INACTIVE at the tightest floor"
                    " after a walk that moved: activity is monotone in mu0,"
                    " so every looser rung is vacuous — the ladder stops"
                    " here (derivation printed, no silent cap)")
                break
            if not moved:
                # no accepted step at all (a budget too small to move, or
                # a stall): inactivity here says nothing about the optimum
                # -- declared, and the ladder does NOT infer from it
                say("  [rung %d] NO MOTION from the start (budget %d x %d):"
                    " activity not adjudicated at this rung, declared"
                    % (k, SEGS, ITERS))
            W_cur = W_new.copy()        # warm-started continuation
        report["starts"].append(dict(start=stag, W_start=Ws.tolist(),
                                     last_rung=(last_ok[1] if last_ok
                                                else None)))
    # ---- the resolution ladder of the tightest-rung design (start A)
    if LADDER and report["rungs"] and report["rungs"][0].get("W"):
        W_t = np.asarray(report["rungs"][0]["W"], float)
        say("-- resolution ladder of the tightest-rung design (start A,"
            " rung 1): certification and margin against the incumbent's"
            " own m_ref at each resolution --")
        for r in range(1, 3):
            Kr, Nr = (2 ** r) * (K - 1) + 1, (2 ** r) * (N - 1) + 1
            cr = dict(P.build_case(w, N=Nr))
            cr["xk"] = c["xk"]
            ellr2 = station_spacing(Kr) ** 2
            mgr = dict(base_mg, ell2=ellr2, mu0=floors[0])
            W0r = np.interp(c["xk"], cr["sx"], cr["sy"])
            t0 = time.time()
            oi, si = P.march_record(W0r, w, cr, K=Kr, margin=mgr)
            m_ref_r = float(oi["margin_min"])
            Ji = float(P.J_replay(jnp.asarray(W0r), w, cr, si, ta, K=Kr))
            od, sd = P.march_record(W_t, w, cr, K=Kr, margin=mgr)
            Jd = float(P.J_replay(jnp.asarray(W_t), w, cr, sd, ta, K=Kr))
            mn_d = float(od["margin_min"])
            in_class = mn_d >= 0.5 * m_ref_r
            say("  (%d,%d): incumbent cert %.3f m_ref %+.4f J %.8e | design"
                " cert %.3f min cell %+.4f KS %+.4f J %.8e (%+.5f %%) ->"
                " %s at mu0_1(r) = m_ref_r/2 = %.4f (%.0f s)"
                % (Kr, Nr, float(oi["cert_worst"]), m_ref_r, Ji,
                   float(od["cert_worst"]), mn_d, float(od["margin_ks"]),
                   Jd, 100 * (Jd / Ji - 1),
                   "IN CLASS" if in_class else "OUT OF CLASS",
                   0.5 * m_ref_r, time.time() - t0))
            report["ladder"].append(dict(K=Kr, N=Nr, cert_inc=float(
                oi["cert_worst"]), m_ref_r=m_ref_r, J_inc=Ji, cert=float(
                od["cert_worst"]), min_cell=mn_d, J=Jd,
                in_class=bool(in_class)))
    report.update(seconds=time.time() - t00, stage="campaign",
                  segs=SEGS, iters=ITERS, starts_n=STARTS,
                  provenance="[X-PMRG] S29 campaign; posing = S21 [X-PSPL]")
    os.makedirs(ART, exist_ok=True)
    tag = "campaign_s%d_i%d_r%d_st%d" % (SEGS, ITERS, RUNGS, STARTS)
    json.dump(report, open(os.path.join(ART, tag + ".json"), "w"),
              indent=1)
    say("  report written to %s" % os.path.join(ART, tag + ".json"))
    return ok and NPASS[0] == NPASS[1]


if __name__ == "__main__":
    t0 = time.time()
    good = campaign() if STAGE == "campaign" else derive()
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                         time.time() - t0))
    sys.exit(0 if good else 1)

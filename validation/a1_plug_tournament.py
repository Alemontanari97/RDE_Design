#!/usr/bin/env python3
"""[X-PTRN] THE PLUG TOURNAMENT AT FULL EXPANSION, GENERAL METHOD
[F3/A1]: our free-form spike, searched WITHOUT knowledge of the answer,
against the classical construction (Rao 1961 / GENO) used only as an
oracle afterwards. S29 2026-09-16 (owner's directive of 16:45: "the
method must search generally — no case-dependent aspects, the optimum
is not known a priori; finding Rao is only a confirmation of
correctness"); log validation/PROGRESS_2026-09-16_S29_readjudication.md
sec. 6.

WHAT IS GENERAL HERE, AND WHAT IS SHARED. The search uses only the
method's own constructions: the corner fan of OUR world (CH4/O2 gas,
chamber, nominal ambient PA), the inlet split theta_E = 0 the method's
own sweep selected ([X-PSPL] step 15), the start radius set by the mass
constraint on the method's own quadrature, the fan streamline as the
incumbent, a clamped-left natural cubic spline on m uniform knots over
the WHOLE design region (x0, L] with the tip radius FREE above the
march's own floor y >= YTIP y_E (the plug march has no axis cell: S28,
declared), the fold margin derived on the incumbent ([X-PMRG]), and
the certified TR-SQP with the margin as a constraint. The SHARED
constraints of the tournament (M0's finite sector tournament: a
comparison is legitimate only on shared constraints) are the gas, the
mass target, the ambient and the length L: L = the abscissa where the
classical member reaches the march's tip floor (the comparison length
is a convention of the contest, not a shape). NOTHING of Rao's contour
enters the search: no frozen zone, no pinned tip at his y_D, no
reference on his wall, no start from his perturbation (the S28 twin
posing did all four as INSTRUMENT checks of the march/driver — legit
there, circular in a tournament).

THE ORACLE. GENO's axisymmetric ideal-spike member in our gas
(CASES/raoplug_ch4o2, validation mode Me_fixed 2.802: theta_E -0.02
deg, L 5.926, closes on the axis; the member expands to 0.9949 PA and
carries -0.37 percent of the mass target — the cross-code posing
residuals of S28, DECLARED) is read only after the search: (i) its
contour transplanted onto the method's own knots (radially shifted by
the start-radius difference at x0, printed), marched and graded by the
same functional J = F_in + integral (p_w - p_a) 2 pi y (-dy) on the same
start line; (ii) the wall distance between the method's optimum and
Rao's contour against the bands the method derives on its own.
CORRECTNESS CONFIRMATION = the method's optimum sits on Rao's contour
within band and its J equals Rao's within band_J; a class-certified
GAIN over Rao beyond band_J would be the finding of the tournament (and
would first be attributed: ambient residual, mass residual, tip floor).

STAGES. derive (default): the posing, the incumbent, its margin
derivation (orientation, free-edge bucket depth at the doubled
resolution, m_ref, floors mu0_k = m_ref/2^k, rho, KS gap), the
representation error of the incumbent and of Rao's contour on the
knots (C-1), J(incumbent) at K and 2K-1 -> band_J (v2 form: K_RICH |dJ|
+ |grad J|_1 band_W), the fold scale along +grad J -> tr0 and the
radius floor (derived), Rao's contour on the method's posing (J, cert,
margin, fold census, wall distance to the incumbent), the REJECTOR (the
incumbent with a 2 deg compression corner at the first knot — the S21
optimum's corner — must be infeasible at every floor). Artifact
_plug_tournament/derive.json. campaign: margin-constrained TR-SQP from
the incumbent (start A) and from its 1.5 percent alternating
perturbation (start B, generic), tip bounded below, PTRN_SEGS x
PTRN_ITERS per start; verdict: gain over the incumbent and over Rao vs
band_J, class membership (margin, fold census) and mu of every
returned base, wall distance to Rao vs band_W. Consumes derive.json.
Multi-hour: launched on the owner's word.

ON-DEMAND CARRIER (env: jax + the GENO run directory for the oracle).
A1_PTRN_STAGE in {derive, campaign}; PTRN_M (knots, default 16), PTRN_K
(stations, default 161), PTRN_N (rows, default 81: the (161,51) pairing
fails to certify the incumbent at a free-jet edge cell, measured), PTRN_SEGS/ITERS
(4/12), PTRN_STARTS (2), PTRN_ART. The length L is derived from the
member's tip-floor crossing (OW_YCUT of ourworld_geno, 0.01 y_E).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import jax.numpy as jnp                                 # noqa: E402
import ourworld_geno as OW                              # noqa: E402

# the shared length: where the classical member reaches the march's tip
# floor (loaded BEFORE a1_plug_spline_opt reads PSPL_L at import)
_W_ORACLE = OW.load_world(verbose=False) if os.path.isdir(OW.RUN) else None
if _W_ORACLE is not None:
    os.environ.setdefault("PSPL_L", "%.10f" % _W_ORACLE["x_end"])
# [X-AFAN] PSPL_FAN=axi: the incumbent is the method's OWN axisymmetric
# member (a1_axi_fan, the inverse march from the terminal ray), and the
# shared length is where THAT member reaches the tip floor -- the
# contest's convention applied to the method's construction; the
# oracle's own tip abscissa is reported beside it. PTRN_L overrides.
FAN_MODE = os.environ.get("PSPL_FAN", "planar")
if FAN_MODE == "axi":
    import a1_config_compare as _CC0                    # noqa: E402
    import a1_axi_fan as AF                             # noqa: E402
    _FAN0 = AF.fan_axi(_CC0.build_world(), 0.0)
    os.environ["PSPL_L"] = os.environ.get("PTRN_L", "%.10f" % _FAN0["x_tip"])
os.environ.setdefault("PSPL_M", os.environ.get("PTRN_M", "16"))
os.environ.setdefault("PSPL_K", os.environ.get("PTRN_K", "161"))
# rows: 81, not the driver's 51 -- the incumbent at L 5.61 certifies at
# (81,41) and (161,81) but not at (161,51) (a free-jet EDGE cell, column
# 75: the (K,N) pairing lottery of S28, not a defect of the design); the
# probe of record is scratch_s2_2026-09-15/inc_cert_probe2_2026-09-16.log
os.environ.setdefault("PSPL_N", os.environ.get("PTRN_N", "81"))

import a1_ideal_march_jax as A1                         # noqa: E402
import a1_config_compare as CC                          # noqa: E402
import a1_plug_spline_opt as P                          # noqa: E402
from a1_plug_margin import (np_margin, margin_dict, wall_angle_deg,  # noqa
                            flow_angle_deg, station_spacing, cusp_census)

K_RICH = A1.K_RICH
EPS = A1.EPS
ART = os.environ.get("PTRN_ART", os.path.join(HERE, "_plug_tournament"))
DERIVE = os.path.join(ART, "derive.json")
STAGE = os.environ.get("A1_PTRN_STAGE", "derive")
SEGS = int(os.environ.get("PTRN_SEGS", 4))
ITERS = int(os.environ.get("PTRN_ITERS", 12))
STARTS = int(os.environ.get("PTRN_STARTS", 2))
# PTRN_ONLY = one start letter (A/B/C): the campaign runs that start alone
# (one process per start on s2; the report file carries the letter)
ONLY = os.environ.get("PTRN_ONLY", "")
N_RUNGS = 4
JMIN = 2
CORNER_DEG = 2            # the S21 optimum's corner: the rejector's kink
PERT = 3 / (2 * 100)      # the generic 1.5 percent alternating start (S26/S28)
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


def fold_census(out):
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


def rao_on_knots(c, Wo):
    """Rao's (GENO's) tip-cut contour transplanted onto the method's
    knots: y at the knots, shifted radially by the start-radius
    difference at x0 so the wall stays continuous with the method's own
    start line (the shift is the cross-code inlet posing, printed)."""
    wall = Wo["wall"]
    y_x0 = float(np.interp(P.X0, wall[:, 0], wall[:, 1]))
    shift = float(c["yw0"]) - y_x0
    W = np.interp(c["xk"], wall[:, 0], wall[:, 1]) + shift
    return W, shift, y_x0


def wall_gap(W1, W2, c):
    _, y1, _ = P.wall_stations(np.asarray(W1, float), c)
    _, y2, _ = P.wall_stations(np.asarray(W2, float), c)
    return float(np.max(np.abs(np.asarray(y1) - np.asarray(y2))))


def rao_wall_dist(W, c, Wo, shift=0.0):
    """max over the stations of |y(W) - (y_Rao(x) + shift)|: shift = 0
    reads Rao's contour as GENO wrote it (the distance the oracle sees,
    inlet posing included), shift = the start-radius difference reads
    its SHAPE on the method's start line."""
    xq, yq, _ = P.wall_stations(np.asarray(W, float), c)
    yr = np.interp(np.asarray(xq), Wo["wall"][:, 0], Wo["wall"][:, 1]) + shift
    return float(np.max(np.abs(np.asarray(yq) - yr)))


# ======================================================================
# stage derive
# ======================================================================
def derive():
    t00 = time.time()
    say("== [F3] the plug tournament at full expansion, general method"
        " [X-PTRN] (stage derive) ==")
    if _W_ORACLE is None:
        say("   OW_GENO_RUN not a directory -- the oracle is absent, nothing to do")
        return False
    Wo = _W_ORACLE
    w = CC.build_world()
    ta = w["ta"]
    c = P.build_case(w)
    K, N, m = P.K_ST, P.N_ROW, P.M_NODES
    # the tip floor in lip radii: OUR lip under the axi fan (the member's
    # own floor, 0.01 y_E of this world), the oracle's y_E on the planar
    # posing (unchanged path)
    ytip = OW.YCUT * (w["RMAX"] if FAN_MODE == "axi" else Wo["y_E"])
    W0 = np.asarray(c["W0"], float)
    say("   posing (OURS): gas %s, p_a %.6g Pa (nominal), mdot target %.6e;"
        " theta_E %.1f deg (the method's sweep), fan %s, x0 %.2f, y_w0 %.5f"
        " (%s); L %.4f m = %s tip-floor abscissa (shared);"
        " m %d uniform knots on (x0, L], K %d, N %d; tip floor y >= %.4f m"
        " (%.2f y_E, the march's own)"
        % (w["tab"]["name"] if "name" in w["tab"] else "nasa", P.PA, w["mdot"],
           np.degrees(P.THE_OPT), FAN_MODE, P.X0, c["yw0"],
           "mass closed on the terminal ray" if FAN_MODE == "axi" else "mass-set",
           P.L, "OUR member's" if FAN_MODE == "axi" else "the member's",
           m, K, N, ytip, OW.YCUT))
    say("   oracle (read only after the search): GENO member theta_E %+.4f"
        " deg, L %.5f, lip p_a %.6g Pa (%.4f of PA), mdot %.6e (%+.2f %% of"
        " the target) -- residuals DECLARED"
        % (Wo["perf"]["theta_E"], Wo["perf"]["L_plug"], Wo["pa"],
           Wo["pa"] / P.PA, Wo["perf"]["mdot"],
           100 * (Wo["perf"]["mdot"] / w["mdot"] - 1)))
    tip_clamped = bool(W0[-1] < ytip)
    if tip_clamped:
        W0[-1] = ytip
    say("   incumbent = %s on the knots (tip y %.5f%s)"
        % ("the method's axisymmetric member [X-AFAN]" if FAN_MODE == "axi"
           else "the fan streamline", W0[-1],
           ", CLAMPED to the floor" if tip_clamped else ""))
    rec = dict(L=P.L, X0=P.X0, m=m, K=K, N=N, ytip=ytip, yw0=float(c["yw0"]),
               pa=float(P.PA), mdot=float(w["mdot"]), thE=float(P.THE_OPT),
               tip_clamped=tip_clamped, W0=W0.tolist(), xk=np.asarray(c["xk"]).tolist(),
               oracle=dict(run=OW.RUN, theta_E=Wo["perf"]["theta_E"],
                           L=Wo["perf"]["L_plug"], pa=Wo["pa"],
                           pa_ratio=Wo["pa"] / P.PA, x_end=Wo["x_end"]))
    ell = station_spacing(K)
    ell2 = ell * ell

    # ---- C-1: representation of the incumbent and of Rao's contour
    say("-- C-1: representation on the knots (incumbent, and Rao's contour"
        " transplanted) --")
    xg = np.linspace(P.X0, P.L, 4 * K)
    _, y0s, _ = P.wall_stations(W0, c)
    e_inc = float(np.max(np.abs(np.asarray(y0s)
                                - np.interp(np.asarray(P.wall_stations(W0, c)[0]),
                                            c["sx"], c["sy"]))))
    W_rao, shift, y_rao_x0 = rao_on_knots(c, Wo)
    e_rao = rao_wall_dist(W_rao, c, Wo, shift)
    d_inc_rao = rao_wall_dist(W0, c, Wo, shift)
    d_inc_rao_raw = rao_wall_dist(W0, c, Wo)
    say("  incumbent: max |spline - streamline| %.3e m; Rao's contour: start"
        " radius at x0 %.5f vs ours %.5f (shift %+.2e m = the cross-code inlet"
        " posing, S28: mass %+.2f %%); transplanted (shifted): max |spline -"
        " wall| %.3e m; incumbent vs Rao's SHAPE (shifted) %.3e m, vs his"
        " wall as written %.3e m"
        % (e_inc, y_rao_x0, c["yw0"], shift,
           100 * (Wo["perf"]["mdot"] / Wo["perf"]["mdot_target"] - 1), e_rao,
           d_inc_rao, d_inc_rao_raw))
    rec.update(e_rep_inc=e_inc, e_rep_rao=e_rao, W_rao=W_rao.tolist(),
               rao_shift=shift, inc_vs_rao=d_inc_rao, inc_vs_rao_raw=d_inc_rao_raw)

    # ---- D1: the margin on the incumbent
    say("-- D1: the fold margin on the incumbent: orientation, free-edge"
        " bucket (doubled resolution), m_ref, floors, rho --")
    mg = margin_dict(1.0, 0.0, 1.0, 1.0, 0.0, ell2)
    t0 = time.time()
    out, sch = P.march_record(W0, w, c, margin=mg)
    ms = np_margin(out, sch, N, 1.0, 0.0, ell2)
    orient = float(np.sign(np.median(ms)))
    say("  raw median %+.4f over %d whole-column cells -> orient %+.0f; cert"
        " %.3f at %s (%.0f s)" % (np.median(ms), len(ms), orient,
                                  float(out["cert_worst"]), out.get("cert_where"),
                                  time.time() - t0))
    check("C-0 the incumbent's record is Newton-certified at (%d,%d) (worst"
          " %.3f) -- the general method's own construction must be marchable"
          " at the shared length" % (K, N, float(out["cert_worst"])),
          float(out["cert_worst"]) <= 1.0)
    K2, N2 = 2 * K - 1, 2 * N - 1
    c2 = dict(P.build_case(w, N=N2))
    c2["xk"] = c["xk"]
    W02 = np.interp(c["xk"], c2["sx"], c2["sy"])
    W02[-1] = max(W02[-1], ytip)
    t0 = time.time()
    mg2 = margin_dict(1.0, 0.0, 1.0, orient, 0.0, station_spacing(K2) ** 2)
    out2, sch2 = P.march_record(W02, w, c2, K=K2, margin=mg2)
    ms2, dep2, _ = np_margin(out2, sch2, N2, orient, 0.0,
                             station_spacing(K2) ** 2, with_depth=True)
    bad = ms2 <= 0.0
    d_meas = float(dep2[bad].max()) if bad.any() else 0.0
    f_edge = 0.5 * K_RICH * d_meas
    how = "deepest non-positive cell x K_RICH/2"
    # the WORKING resolution's own band (additive, 2026-09-16): at
    # (161,81) the axi member's free jet carries row-growth slivers on
    # the top 2-7 rows of the tail columns (cell area 1e-5 .. 1e-4 m^2
    # against a 5e-4 bulk: margins 0.0098 .. 0.036 under the ell^2
    # floor, bulk minimum 0.046) that the doubled resolution (321,161)
    # does NOT have (its top rows sit at 0.053, its minimum 0.0526 is a
    # foot cell), so the doubled-resolution rule alone leaves f_edge 0
    # and a bucket whose minimum is a sliver at x 11 m in the uniform
    # jet, W-independent: the KS would then be anchored on noise. Rule:
    # exclude the top n rows, n = the smallest count for which the
    # bucket minimum is NOT a boundary cell (rows_from_top >= n + 2);
    # a sliver smaller than the minimum would be the minimum, so the
    # band ends exactly where excluding one more row changes nothing.
    # f_edge = K_RICH/2 x that cell's depth; the larger of the two rules.
    msw, depw, wherew = np_margin(out, sch, N, orient, 0.0, ell2,
                                  with_depth=True)
    tops = {}
    for (jj, ii) in out["mesh_keys"]:
        tops[ii] = max(tops.get(ii, 0), jj)
    rft = np.array([tops[ii] - jj for (ii, jj) in wherew])
    # (the shallowest cell class is rows_from_top = 2, not 1: the row
    # classes are walked as they exist, and the band ends when the
    # minimiser over the remaining classes is not in the shallowest one)
    classes = np.unique(rft)
    n_band, d_work = 0, 0.0
    for kc in range(len(classes) - 1):
        sel = rft >= classes[kc]
        i_min = int(np.argmin(np.where(sel, msw, np.inf)))
        if rft[i_min] > classes[kc]:
            break
        n_band = int(classes[kc])
        d_work = float(depw[rft <= classes[kc]].max())
    f_work = 0.5 * K_RICH * d_work
    say("  incumbent at (%d,%d): sliver band = top %d rows (bucket minimum"
        " %.4f at rows_from_top %d beyond it; deepest band cell at row"
        " fraction %.3f -> f_edge %.3f)"
        % (K, N, n_band, float(msw[rft > n_band].min()),
           int(rft[int(np.argmin(np.where(rft > n_band, msw, np.inf)))]),
           d_work, f_work))
    how = "deepest non-positive cell x K_RICH/2 at the doubled resolution"
    if f_work > f_edge:
        f_edge = f_work
        d_meas = d_work
        how = "the working resolution's sliver band (top %d rows) x K_RICH/2" % n_band
    say("  incumbent at (%d,%d): %d whole-column cells, %d <= 0, band from"
        " row fraction %.3f (%s) -> f_edge %.3f; cert %.3f at %s (%.0f s)"
        % (K2, N2, len(ms2), int(bad.sum()), d_meas, how, f_edge,
           float(out2["cert_worst"]), out2.get("cert_where"), time.time() - t0))
    check("D1a the incumbent's non-positive cells (if any) lie in the"
          " free-edge band (depth < 1/2)", d_meas < 0.5)
    mg = margin_dict(1.0, 0.0, 1.0, orient, f_edge, ell2)
    out, sch = P.march_record(W0, w, c, margin=mg)
    ms = np_margin(out, sch, N, orient, f_edge, ell2)
    vmin_np, n_np = float(ms.min()), len(ms)
    check("R-D0 in-loop margin == numpy census (min %.6f vs %.6f, cells %d"
          " vs %d)" % (float(out["margin_min"]), vmin_np, int(out["margin_n"]),
                       n_np),
          abs(float(out["margin_min"]) - vmin_np) <= K_RICH * EPS * max(
              1.0, abs(vmin_np)) and int(out["margin_n"]) == n_np)
    check("R-D0b the incumbent is strictly healthy on the bucket (m_ref %.4f)"
          % vmin_np, vmin_np > 0.0)
    m_ref, Nc = vmin_np, n_np
    floors = [m_ref / 2 ** k for k in range(1, N_RUNGS + 1)]
    rho = K_RICH * np.log(Nc) / floors[-1]
    gap = np.log(Nc) / rho
    mg = margin_dict(rho, floors[0], m_ref, orient, f_edge, ell2)
    mg["tol"] = gap                    # the feasibility gate of run_trsqp
    out, sch = P.march_record(W0, w, c, margin=mg)
    ks = float(out["margin_ks"])
    check("R-KS  vmin - ln N/rho = %.5f <= KS = %.5f <= vmin = %.5f"
          % (m_ref - gap, ks, m_ref),
          m_ref - gap - K_RICH * EPS <= ks <= m_ref + K_RICH * EPS)
    say("  m_ref %.4f (%d cells, median %.4f), floors %s, rho %.1f, gap %.3e"
        % (m_ref, Nc, np.median(ms), ["%.4f" % f for f in floors], rho, gap))
    rec.update(orient=orient, f_edge_meas=d_meas, f_edge=f_edge, m_ref=m_ref,
               N_cells=Nc, floors=floors, rho=rho, gap=gap, ell=ell, ell2=ell2,
               median=float(np.median(ms)))

    # ---- D2: J of the incumbent at K and 2K-1, the gradient floor, band_J
    say("-- D2: the incumbent's thrust at K and 2K-1, its gradient, band_J --")
    t0 = time.time()
    J0, g0 = P.J_and_grad(W0, w, c, ta, sch)
    J02 = float(P.J_replay(jnp.asarray(W02), w, c2, sch2, ta, K=K2))
    g_floor = float(np.max(np.abs(g0)))
    band_W_rep = K_RICH * max(e_inc, e_rao)
    band_J = K_RICH * abs(J0 - J02) + float(np.sum(np.abs(g0))) * band_W_rep
    say("  J(inc) %.8e (K %d) vs %.8e (K %d): |dJ| %.3e; |grad J|inf %.3e,"
        " |grad J|_1 %.3e; band_W(rep) %.3e -> band_J %.3e (%+.2e of J) (%.0f s)"
        % (J0, K, J02, K2, abs(J0 - J02), g_floor, np.sum(np.abs(g0)),
           band_W_rep, band_J, band_J / J0, time.time() - t0))
    rec.update(J0=float(J0), J02=J02, g_floor=g_floor, g_dir=(g0 / np.linalg.norm(g0)).tolist(),
               band_W_rep=band_W_rep, band_J=band_J)

    # ---- D3: Rao's contour on the method's posing (the oracle, graded)
    say("-- D3: Rao's contour on the method's own posing (oracle, graded by"
        " the same march, functional and margin) --")
    t0 = time.time()
    W_r = W_rao.copy()
    W_r[-1] = max(W_r[-1], ytip)
    o, s = P.march_record(W_r, w, c, margin=mg)
    J_r = float(P.J_replay(jnp.asarray(W_r), w, c, s, ta))
    nf, nc, first = fold_census(o)
    say("  Rao: J %.8e (vs incumbent %+.4e N = %+.2e of J; band_J %.3e), cert"
        " %.3f, min cell %+.4f KS %+.4f (%d cells), folded %d/%d (first %s),"
        " theta st.1 %+.2f deg (incumbent %+.2f, flow %+.2f) (%.0f s)"
        % (J_r, J_r - J0, (J_r - J0) / J0, band_J, float(o["cert_worst"]),
           float(o["margin_min"]), float(o["margin_ks"]), int(o["margin_n"]),
           nf, nc, first, wall_angle_deg(W_r, c), wall_angle_deg(W0, c),
           flow_angle_deg(c), time.time() - t0))
    check("O-1 (reported) Rao's contour ON THE KNOTS is in the class (min cell"
          " %+.4f vs mu0_1 %.4f, %d folded columns) -- the knot representation"
          " (%.1e m) is of the order of the fold scale, so this row reads the"
          " transplant, not Rao: the graded row is O-1b"
          % (float(o["margin_min"]), floors[0], nf, e_rao), True)
    # O-1b (2026-09-16 evening): Rao's contour AS WRITTEN (shifted radially
    # by the inlet posing at x0) marched directly as the stations -- no
    # spline through 16 knots between the oracle and the class census.
    # The 16-knot transplant folded 29/162 columns from column 2 while
    # the incumbent on the same knots did not: a 3 mm representation
    # error at the foot is a fold at the fold scale (h* ~3 mm), so the
    # knot row cannot grade Rao's class membership.
    from a1_plug_march import plug_march
    t0 = time.time()
    ow = Wo["wall"]
    xq_r = np.linspace(P.X0, min(P.L, float(ow[-1, 0])), K + 1)[1:]
    yq_r = np.interp(xq_r, ow[:, 0], ow[:, 1]) + shift
    sl_r = np.gradient(np.interp(xq_r, ow[:, 0], ow[:, 1]), xq_r)
    st_r = (jnp.asarray(xq_r), jnp.asarray(yq_r), jnp.asarray(sl_r))
    o_b, s_b = plug_march(st_r, c["start"], c["qpa"], w["tab"], 1.0, margin=mg)
    nf_b, nc_b, first_b = fold_census(o_b)
    say("  Rao AS WRITTEN (shift %+.2e m, %d stations to x %.4f): cert %.3f,"
        " min cell %+.4f KS %+.4f (%d cells), folded %d/%d (first %s) (%.0f s)"
        % (shift, len(xq_r), xq_r[-1], float(o_b["cert_worst"]),
           float(o_b["margin_min"]), float(o_b["margin_ks"]),
           int(o_b["margin_n"]), nf_b, nc_b, first_b, time.time() - t0))
    check("O-1b ORACLE Rao's contour as written is IN the class on our posing"
          " (min cell %+.4f >= mu0_1 %.4f, %d folded columns)"
          % (float(o_b["margin_min"]), floors[0], nf_b),
          float(o_b["margin_min"]) >= floors[0] and nf_b == 0)
    rec.update(margin_rao_written=float(o_b["margin_min"]), folded_rao_written=nf_b,
               cert_rao_written=float(o_b["cert_worst"]))
    check("O-2 ORACLE the incumbent (our fan streamline) equals Rao's contour"
          " within the representation band (%.3e <= %.3e) and in thrust"
          " (|dJ| %.3e <= band_J %.3e)" % (d_inc_rao, band_W_rep, abs(J_r - J0),
                                            band_J),
          d_inc_rao <= band_W_rep and abs(J_r - J0) <= band_J)
    rec.update(J_rao=J_r, cert_rao=float(o["cert_worst"]),
               margin_rao=float(o["margin_min"]), folded_rao=nf)

    # ---- D4: the rejector, and the fold scale along +grad J
    say("-- D4: the rejector (a %d deg corner at the first knot) and the fold"
        " scale along +grad J -> tr0 --" % CORNER_DEG)
    dx = float(c["xk"][0] - P.X0)
    W_c = W0.copy()
    W_c[0] += dx * np.tan(np.radians(CORNER_DEG))
    t0 = time.time()
    o, s = P.march_record(W_c, w, c, margin=mg)
    nf_c, _, _ = fold_census(o)
    mv, gm = P.margin_and_grad(W_c, w, c, s, mg)
    ksc = float(o["margin_ks"])
    infeas = [bool(ksc < f) for f in floors]
    check("R-G1 REJECTOR the cornered incumbent (first knot %+.1f mm, theta st.1"
          " %+.2f deg) is INFEASIBLE at every floor %s (KS %+.4f, %d folded),"
          " margin finite %s, grad finite %s (%.0f s)"
          % (1e3 * (W_c[0] - W0[0]), wall_angle_deg(W_c, c), infeas, ksc, nf_c,
             np.isfinite(mv), bool(np.all(np.isfinite(gm))), time.time() - t0),
          all(infeas) and np.isfinite(mv) and bool(np.all(np.isfinite(gm))))
    u = g0 / np.linalg.norm(g0)
    n_half = 5
    h_ok, h_bad, rows = None, None, []
    for k in range(-n_half, n_half + 1):
        h = ell * 2.0 ** k
        Wh = W0 + h * u
        Wh[-1] = max(Wh[-1], ytip)
        o, s = P.march_record(Wh, w, c, margin=mg)
        ksh = float(o["margin_ks"])
        Jh = float(P.J_replay(jnp.asarray(Wh), w, c, s, ta))
        rows.append(dict(h=h, J=Jh, ks=ksh, cert=float(o["cert_worst"])))
        say("    h %.3e m: J %.7e (%+.4f %%) KS %+.4f min %+.4f cert %.3f theta"
            " st.1 %+.2f" % (h, Jh, 100 * (Jh / J0 - 1), ksh,
                             float(o["margin_min"]), float(o["cert_worst"]),
                             wall_angle_deg(Wh, c)))
        if ksh >= floors[0]:
            h_ok = h
        elif h_bad is None:
            h_bad = h
        if h_ok is not None and h_bad is not None and h_bad > h_ok:
            break
    bracketed = h_ok is not None and h_bad is not None and h_bad > h_ok
    check("R-FSC the margin along +grad J crosses mu0_1 inside the ladder"
          " (bracket [%s, %s] m)" % (h_ok, h_bad), bracketed)
    h_star = float(np.sqrt(h_ok * h_bad)) if bracketed else float("nan")
    tr0 = h_star / K_RICH
    say("  h* %.3e m -> tr0 %.3e m, radius floor tr0/K_RICH %.3e m"
        % (h_star, tr0, tr0 / K_RICH))
    rec.update(fold_ladder=rows, h_ok=h_ok, h_bad=h_bad, h_star=h_star, tr0=tr0,
               flow_angle_deg=flow_angle_deg(c), stage="derive",
               seconds=time.time() - t00,
               provenance="[X-PTRN] S29 derive; posing = the method's own")
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(DERIVE, "w"), indent=1)
    say("  derived constants written to %s" % DERIVE)
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage campaign
# ======================================================================
def campaign():
    from scipy.optimize import Bounds
    t00 = time.time()
    say("== [F3] the plug tournament at full expansion, general method"
        " [X-PTRN] (stage campaign) ==")
    if not os.path.exists(DERIVE):
        say("FATAL: no derive.json at %s -- run the derive stage first" % DERIVE)
        return False
    D = json.load(open(DERIVE))
    Wo = _W_ORACLE
    w = CC.build_world()
    ta = w["ta"]
    c = P.build_case(w)
    K, N, m = P.K_ST, P.N_ROW, P.M_NODES
    if (K, N, m, round(P.L, 6)) != (D["K"], D["N"], D["m"], round(D["L"], 6)):
        say("FATAL: posing differs from derive.json")
        return False
    W0 = np.asarray(D["W0"], float)
    W_rao = np.asarray(D["W_rao"], float)
    floors, rho, gap, tr0 = D["floors"], D["rho"], D["gap"], D["tr0"]
    mg0 = margin_dict(rho, floors[0], D["m_ref"], D["orient"], D["f_edge"],
                      D["ell2"])
    mg0["tol"] = gap
    lo = np.full(len(W0), -np.inf)
    lo[-1] = D["ytip"]
    bounds = Bounds(lo, np.full(len(W0), np.inf))
    say("  posing (%d,%d) m %d L %.4f; floor mu0_1 %.4f; rho %.1f; gap %.3e;"
        " tr0 %.3e m (floor %.3e); %d segments x %d iterations; starts %d;"
        " tip bounded y >= %.4f"
        % (K, N, m, P.L, floors[0], rho, gap, tr0, tr0 / K_RICH, SEGS, ITERS,
           STARTS, D["ytip"]))
    J0 = D["J0"]
    sgn = np.array([(-1.0) ** k for k in range(len(W0))])
    W_p = W0 * (1.0 + PERT * sgn)
    W_p[-1] = max(W_p[-1], D["ytip"])
    starts = [("A incumbent (the method's member)", W0.copy())]
    if STARTS >= 2:
        starts.append(("B 1.5 %% alternating perturbation", W_p.copy()))
    if STARTS >= 3 and FAN_MODE == "axi":
        # start C (owner's question 2026-09-16 evening: "the inverse
        # construction goes against the program's direct process"): the
        # PLANAR corner-wave streamline on the same knots -- generic,
        # certified, in class, 0.84 m from the ideal member -- so the
        # DIRECT machinery alone (march, adjoint, margin, TR-SQP) is
        # asked to find the member from far away; the inverse
        # construction then serves only as the oracle
        P.FAN_MODE = "planar"                  # the planar posing's own sizing
        c_pl = P.build_case(w, N=N)
        P.FAN_MODE = "axi"
        W_pl = np.interp(c["xk"], c_pl["sx"], c_pl["sy"])
        # the planar streamline with the axi foot is OUT of class at
        # once (the flow reaches x0 at -33.2 deg, the planar wall leaves
        # at -26.7: a 6.5 deg compression corner at the first station),
        # so the far start is the RAMP from the member to the planar
        # streamline -- equal at the first knot, the full 0.84 m apart
        # at the tail: generic, far, and graded by the margin at its base
        ramp = np.arange(len(W0), dtype=float) / (len(W0) - 1)
        W_c = W0 + ramp * (W_pl - W0)
        W_c[-1] = max(W_c[-1], D["ytip"])
        say("   start C = ramp from the member to the planar streamline on"
            " the knots: tip y %.4f, max |W_c - W0| %.3e m (planar itself"
            " %.3e m)" % (W_c[-1], float(np.max(np.abs(W_c - W0))),
                          float(np.max(np.abs(W_pl - W0)))))
        starts.append(("C ramp to the planar streamline (generic, far)",
                       W_c.copy()))
    if ONLY:
        starts = [st for st in starts if st[0].startswith(ONLY)]
        say("   PTRN_ONLY=%s: %d start(s) selected" % (ONLY, len(starts)))
    report = dict(derive=D, walks=[])
    fn = os.path.join(ART, "campaign_s%d_i%d_st%d%s.json"
                      % (SEGS, ITERS, STARTS, ("_" + ONLY) if ONLY else ""))
    ok = True
    for tag, Ws in starts:
        say("-- start %s --" % tag)
        mg = dict(mg0)
        t0 = time.time()
        try:
            W_s, hist, n_rec = P.run_trsqp(Ws.copy(), w, c, ta, max_segments=SEGS,
                                           maxiter_per_seg=ITERS, margin=mg,
                                           tr0=tr0, tr_floor=tr0 / K_RICH,
                                           bounds=bounds)
        except Exception as err:
            say("  walk did not complete: %r -- a G1 rejector firing" % (err,))
            report["walks"].append(dict(start=tag, outcome="raise", error=repr(err)))
            ok = False
            continue
        dt = time.time() - t0
        o, s = P.march_record(W_s, w, c, margin=mg)
        J_s, g_s = P.J_and_grad(W_s, w, c, ta, s)
        mv, gm = P.margin_and_grad(W_s, w, c, s, mg)
        nf, nc, first = fold_census(o)
        mn, ks = float(o["margin_min"]), float(o["margin_ks"])
        res = mg.get("last_res")
        mu = None
        if res is not None and getattr(res, "v", None):
            mu = -float(np.asarray(res.v[-1]).ravel()[0])
        active = (ks - floors[0]) <= gap
        cen = cusp_census(o, s, N, mg, floors[0])
        d_rao = rao_wall_dist(W_s, c, Wo, D["rao_shift"])
        d_rao_raw = rao_wall_dist(W_s, c, Wo)
        gain_inc = float(J_s) - J0
        gain_rao = float(J_s) - D["J_rao"]
        ctr = mg.get("counters", {})
        say("  [%s] %.0f s, %d segments, %d records: J* %.8e (vs incumbent"
            " %+.4e N = %+.2e; vs Rao %+.4e N = %+.2e; band_J %.3e), cert %.3f,"
            " |grad J|inf %.3e, KS - mu0 %+.5f (min cell %+.4f) -> %s, mu %s,"
            " folded %d/%d, theta st.1 %+.2f deg (flow %+.2f), tip y %.5f (floor"
            " %.4f), dist to Rao's shape %.3e (as written %.3e; band_W %.3e),"
            " W - W0 [mm] %s, counters %s"
            % (tag, dt, len(hist), n_rec, J_s, gain_inc, gain_inc / J0, gain_rao,
               gain_rao / J0, D["band_J"], float(o["cert_worst"]),
               np.max(np.abs(g_s)), ks - floors[0], mn,
               "ACTIVE" if active else "inactive",
               "%.3e" % mu if mu is not None else "n/a", nf, nc,
               wall_angle_deg(W_s, c), D["flow_angle_deg"], W_s[-1], D["ytip"],
               d_rao, d_rao_raw, D["band_W_rep"],
               np.array2string(1e3 * (W_s - W0), precision=2),
               {k: v for k, v in ctr.items() if v}))
        say("  [%s] active-cusp census: %d cells <= mu0 + gap in columns %s"
            " (%d cluster(s)); argmin %s (m %.4f)"
            % (tag, cen["n_active"], cen["columns"], cen["clusters"],
               cen["argmin"], cen["min"]))
        ok &= check("[%s] C-1 the returned base is certified (%.3f)"
                    % (tag, float(o["cert_worst"])), float(o["cert_worst"]) <= 1.0)
        ok &= check("[%s] C-2 REQ-NONSTALL: J, grad, margin, grad finite at the"
                    " returned base" % tag,
                    np.isfinite(J_s) and np.all(np.isfinite(g_s))
                    and np.isfinite(mv) and np.all(np.isfinite(gm)))
        ok &= check("[%s] C-3 the returned base is IN the class (min cell %+.4f"
                    " >= mu0_1 %.4f, %d folded)" % (tag, mn, floors[0], nf),
                    mn >= floors[0] and nf == 0)
        ok &= check("[%s] C-4 no loss to the incumbent (J* %.8e >= %.8e)"
                    % (tag, J_s, J0), float(J_s) >= J0 - K_RICH * EPS * abs(J0))
        if active and mu is not None:
            ok &= check("[%s] C-5 dual clause mu >= 0 at an active margin (%.3e)"
                        % (tag, mu), mu >= 0.0)
        say("  [%s] ORACLE READING: gain over Rao %+.3e N (%+.2e) %s band_J"
            " %.3e; distance to Rao's contour %.3e %s band_W %.3e"
            % (tag, gain_rao, gain_rao / J0,
               "INSIDE" if abs(gain_rao) <= D["band_J"] else "OUTSIDE", D["band_J"],
               d_rao, "inside" if d_rao <= D["band_W_rep"] else "OUTSIDE",
               D["band_W_rep"]))
        report["walks"].append(dict(
            start=tag, W=W_s.tolist(), J=float(J_s), gain_inc=gain_inc,
            gain_rao=gain_rao, cert=float(o["cert_worst"]), min_cell=mn, ks=ks,
            active=bool(active), mu=mu, folded=nf, dist_to_rao=d_rao,
            dist_to_rao_raw=d_rao_raw,
            tip=float(W_s[-1]), segments=len(hist), records=n_rec, seconds=dt,
            counters=dict(ctr), census=cen,
            inside_band_J=bool(abs(gain_rao) <= D["band_J"]),
            inside_band_W=bool(d_rao <= D["band_W_rep"])))
        # checkpoint: the report so far, after every walk (an overnight
        # leg that dies loses at most the walk in flight)
        json.dump(dict(report, stage="campaign", segs=SEGS, iters=ITERS,
                       starts=STARTS, partial=True), open(fn, "w"), indent=1)
    report.update(stage="campaign", segs=SEGS, iters=ITERS, starts=STARTS,
                  seconds=time.time() - t00, partial=False,
                  provenance="[X-PTRN] S29 campaign; posing = the method's own")
    json.dump(report, open(fn, "w"), indent=1)
    say("  report written to %s" % fn)
    return ok and NPASS[0] == NPASS[1]


if __name__ == "__main__":
    t0 = time.time()
    good = campaign() if STAGE == "campaign" else derive()
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    sys.exit(0 if good else 1)

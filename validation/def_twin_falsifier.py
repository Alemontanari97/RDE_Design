#!/usr/bin/env python3
"""[X-DEFTW] THE F1b DEF TWIN FALSIFIER [F1b/TWIN, session S24] — the
panel's pre-registered twin test (ADVISORY_def_equivalence_panel
2026-08-07, falsifier field VERBATIM: rejection branches F1-F7),
executed at the DECLARED instance (S24 gate [P1]): the GENO defnoz
deep-DEF configuration — axisymmetric bell, yt = 1, rtu = 1.5,
rtd = 0.45, eps = 30, L = xtronc = 8, frozen CH4/O2 tabulated thermo
(the [X-TOCV] O2 cross-code pairing of record). The panel's original
instance clause (perfect gas gamma = 1.4, Table-2 A_E/A_T = 500) is
superseded AS INSTANCE by the S24 session order + D6 F1b SUPERSEDED
text; the branch semantics are untouched. The gamma = 1.4 exactness
role of Eq.(4) is carried by the S4 THEOREM chain (Lambda-form == (G)
on both codes, KAT'd with rejectors: GENO KAT_BFUN; our [X-VMON]).

LEG 1: GENO nozzle_type = 2 at the instance (WSL scratch, file
exchange, GENO NEVER modified), at TWO resolutions (defaults NI = 401
/ Ne = 2001, and halved) for the GENO-side Richardson error; stdout
markers (DEF branch, Dtheta_comp, A4 mass identity) parsed; D'
localized on the GENO OUTPUT FIELD with OUR AD Lambda-form monitor
(argmin val — the DEF construction lands D' on val = 0 inside the
(0, 1e-6) window), with the landing-window + dthetapm-quantization
position bands DERIVED in-run from measured local val gradients.

LEG 2: the direct engine ([X-TOCV] march + the [X-MGOV] margin
machinery structure), margin-CONSTRAINED at the same (eps, L) and the
same thermo, floor ladder mu0_k = m_ref/2^k (k = 1..4, pre-registered
rule, m_ref = measured healthy reference of the DECLARED feasible
start), tightest rung first with warm-started continuation toward
mu0 -> 0 (the floor->0 extrapolation of the falsifier), run to KKT
closure per rung, with the panel's two MANDATORY logs at every rung:
(a) argmin-margin cell coordinates, (b) active-cusp count/location
census at termination. MARGIN BUCKET SCOPE (S24 formulation
adjudication of record, measured — see the in-code block): the
CONTROL-SURFACE bucket (terminal-C+ chain nodes, registered end
exclusion), NOT the whole W-dependent field — at this deep instance
BOTH codes' certified fields legitimately carry val ~ -0.81 at the
attachment, so a whole-field val >= mu0 > 0 constraint is infeasible
for EVERY design of the class and cannot be the constraint EQ-v2
speaks of; the theory names the fold ON the control surface (S4,
Direction A, H2). Multiplier read under the S24-T1 CLOSED res.v
convention: mu(M0) = -res.v[-1][0] (B-STATIONARITY wording, O1
undischarged).

BRANCH SEMANTICS (panel, verbatim; every branch is a VERDICT — a fired
branch is a valid scientific outcome, the carrier's exit code gates
MACHINERY health only): REJECT EQ-v2 if ANY of
  F1 wall-contour gap fails to shrink within the Richardson-derived
     two-code band under joint mesh+knot refinement;
  F2 the direct active-cusp location does not converge to GENO's D'
     on the terminal characteristic;
  F3 f2 = V cos(theta-alpha)/cos(alpha) drifts along the D'E segment
     beyond the derived bar on either design;
  F4 the Lambda-form BF at the direct active cell does not -> 0 under
     refinement (tracked as val_min -> mu0 -> 0 on the ladder);
  F5 the margin binds persistently at an interior/lip/axis-side cell
     with KKT closed (kills H2: demotes EQ-v2 to Direction A only);
  F6 multiple cusps simultaneously active at the optimum (kills H1);
  F7 direct certified J exceeds the DEF J beyond the combined band.
CLAIM CAP (S24 user order, binding): NO classical-optimality wording
in any outcome — F7 reads as "the direct-side surplus prediction
holds/fails on this instance" (O3 = Sternin/Shmyglevskii hard gate).

TOLERANCES — ALL DERIVED (R5): GENO-side band = K_RICH x measured
two-resolution wall difference + the measured |ye - sqrt(eps)|
constraint residual; our-side band = K_RICH x two-resolution
Richardson on the marched wall; class band = M-vs-2M interpolant gap
of the GENO wall; D' bands = landing window (0, 1e-6) and dthetapm/2
mapped through MEASURED val gradients (AD in state, local fit in
position); f2 bar = the [X-O33B] two-resolution construction
re-derived AT THIS INSTANCE; dV_pert cross-implementation band = the
[X-MGOV] armed formula on THIS q-range. GENO |den| < 1e-10 fold-guard
semantic delta honored: our monitor reports den, never a val = 0 read.

INSTANCE GENERALITY: every instance parameter is env-overridable
(A1_DEFTW_*), defaults = the declared defnoz twin; node count and
resolutions are class/mesh knobs, not tuned constants; the ladder,
rho, and every band are derived from measured quantities of THIS
instance by the pre-registered rules.

STAGES (A1_DEFTW_STAGE): "leg1" -> GENO runs + observables (JSON
artifact); "derive" -> engine setup, seeds, ladder + bands + machinery
rejectors (JSON artifact); "campaign" -> the decisive ladder walk +
F1-F7 adjudication (JSON artifact); "refine" -> the optional second
decisive run (final rung at doubled mesh + enriched node class) for
the joint-refinement halves of F1/F4.

ON-DEMAND CARRIER (env: jax + WSL gfortran GENO binary): outside CI
tiers by declaration. Exit 0 iff the executed stage's MACHINERY checks
pass (branch verdicts are reported, never coerced).
"""
import json
import os
import shutil
import subprocess
import sys
import time

import numpy as np
import jax
import jax.numpy as jnp

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1        # noqa: E402
import a1_march_scan as SC             # noqa: E402
import a1_toc_variational_jax as TV    # noqa: E402
import thermotab_c1_jax as TH          # noqa: E402
import o33_bench as O33                # noqa: E402
import locus_diagnosis as LD           # noqa: E402
import margin_governor as MG           # noqa: E402
from adaptive_knot_optimize import (grad_and_J as AK_gJ,
                                    o31_spot as AK_o31)  # noqa: E402

jax.config.update("jax_enable_x64", True)

EPS = float(jnp.finfo(jnp.float64).eps)
d2r = np.pi / 180.0
HERE = os.path.dirname(os.path.abspath(__file__))

# declared twin instance (S24 gate [P1]); every entry env-overridable
CASE = dict(
    yt=float(os.environ.get("A1_DEFTW_YT", "1.0")),
    rtu=float(os.environ.get("A1_DEFTW_RTU", "1.5")),
    rtd=float(os.environ.get("A1_DEFTW_RTD", "0.45")),
    eps=float(os.environ.get("A1_DEFTW_EPS", "30.0")),
    xtronc=float(os.environ.get("A1_DEFTW_XTRONC", "8.0")),
    NI=int(os.environ.get("A1_DEFTW_NI", "21")),
    Nw=int(os.environ.get("A1_DEFTW_NW", "60")),
    da_deg=float(os.environ.get("A1_DEFTW_DA", "0.5")),
)
M_NODES = int(os.environ.get("A1_DEFTW_M", str(TV.M_NODES)))
N_RUNGS = 4                       # pre-registered ladder length
LAND_WIN = 1e-6                   # GENO PM landing window (declared)
DTHETA_PM = 1e-3                  # GENO PM step (declared, rad)
ART_LEG1 = os.path.join(HERE, "s24_deftw_leg1.json")
ART_DERIVE = os.path.join(HERE, "s24_deftw_derive.json")
ART_CAMP = os.path.join(HERE, "s24_deftw_campaign.json")


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# LEG 1 — GENO at the instance (file exchange; GENO never modified)
# ======================================================================
def geno_case_run(scratch, NI_over=None, Ne_over=None):
    """General GENO type-2 runner at CASE (any instance). Returns the
    parsed observables. The atlas folder is the case's own INPUT
    (env-overridable) — part of the declared thermo pairing."""
    atlas = os.environ.get(
        "A1_DEFTW_ATLAS",
        os.path.join(A1.GENO_DIR, "CASES", "defnoz", "INPUT"))
    ini = os.path.join(scratch, "input.ini")
    if not os.path.exists(os.path.join(scratch, "dimensions.dat")):
        os.makedirs(scratch, exist_ok=True)
        shutil.copy(os.path.join(A1.GENO_DIR, "thermo",
                                 "thermo_CH4O2.dat"), scratch)
        shutil.copy(os.path.join(A1.GENO_DIR, "thermo", "raptor.plt"),
                    scratch)
        dst = os.path.join(scratch, "INPUT")
        if not os.path.exists(dst):
            shutil.copytree(atlas, dst)
        solver = ""
        if NI_over or Ne_over:
            solver = ("NI = %d\nNe = %d\n"
                      % (NI_over or 401, Ne_over or 2001))
        with open(ini, "w") as f:
            f.write("[GENO-nozzle]\nnozzle_type = 2\n"
                    "case_geom = axisymmetric\n"
                    "yt = %.6g\nrtu = %.6g\nrtd = %.6g\n"
                    "eps = %.6g\nxtronc = %.6g\n"
                    "thermoname = thermo_CH4O2.dat\n"
                    "frozenname = raptor.plt\nbackend = 0\n"
                    "atlas_folder = INPUT/\n\n[GENO-solver]\n%s"
                    % (CASE["yt"], CASE["rtu"], CASE["rtd"],
                       CASE["eps"], CASE["xtronc"], solver))
        geno_bin = A1.win_to_wsl(os.path.join(A1.GENO_DIR, "bin",
                                              "GENO"))
        cmd = ("cd '%s' && export LD_LIBRARY_PATH="
               "/home/alessandro/miniconda3/envs/ct-env/lib && '%s' "
               "> solver.log 2>&1; echo rc=$?"
               % (A1.win_to_wsl(scratch), geno_bin))
        r = subprocess.run(["wsl.exe", "-e", "bash", "-lc", cmd],
                           capture_output=True, text=True,
                           timeout=1800)
        if "rc=0" not in r.stdout:
            tail = open(os.path.join(scratch, "solver.log"),
                        errors="replace").read()[-600:]
            raise RuntimeError("GENO run failed in %s:\n%s"
                               % (scratch, tail))
    log = open(os.path.join(scratch, "solver.log"),
               errors="replace").read()
    obs = dict(def_marker=None, dtheta_comp=None, a4_rel=None)
    for line in log.splitlines():
        if "DEF: PM-compression branch ACTIVE" in line:
            obs["def_marker"] = line.strip()
            obs["dtheta_comp"] = float(line.split("=")[-1]
                                       .replace("deg", ""))
        if "A4_MASS(TOC)" in line:
            obs["a4_rel"] = float(line.split("rel_gap=")[-1])
    with open(os.path.join(scratch, "dimensions.dat"), "rb") as f:
        l, j2 = np.fromfile(f, dtype="<i4", count=2)
    l, j2 = int(l), int(j2)
    fld = dict()
    for nm in ("x", "y", "u", "v"):
        fld[nm] = np.fromfile(os.path.join(scratch, nm + ".dat"),
                              dtype="<f8", count=j2 * l).reshape(j2, l)
    perf = open(os.path.join(scratch,
                             "performance.dat")).read().split()
    obs["cf"] = float(perf[4])
    obs["theta_max_deg"] = float(perf[8])
    wx, wy = fld["x"][0, :], fld["y"][0, :]
    m = (wx > 0) & (wy > 0)
    wx, wy = wx[m], wy[m]
    keep = np.concatenate([[True], np.diff(wx) > 1e-14])
    obs["wall_x"], obs["wall_y"] = wx[keep], wy[keep]
    obs["field"] = fld
    obs["dims"] = (l, j2)
    return obs


def locate_dprime(obs, lam_fn):
    """D' on the GENO output field via OUR monitor: the DE control
    surface IS the C+ characteristic through the lip, and the DEF
    construction lands its start D' ON the val = 0 boundary (inside
    the (0, 1e-6) window). So: trace the C+ back from the lip
    (slope dy/dx = tan(theta + alpha), interpolated on the field by
    inverse-distance over kd-tree neighbors) and return the val = 0
    crossing. NOTE OF RECORD (S24, measured): the naive whole-field
    argmin-val is WRONG here — the wall/attachment region legitimately
    carries val << 0 (val < 0 is surface-march degeneracy, not field
    invalidity), so the argmin lands at the attachment, not at D'."""
    from scipy.spatial import cKDTree
    fld = obs["field"]
    x = fld["x"].ravel()
    y = fld["y"].ravel()
    u = fld["u"].ravel()
    v = fld["v"].ravel()
    q = np.hypot(u, v)
    th = np.arctan2(v, u)
    fin = (q > 0) & np.isfinite(q) & (y > 0)
    x, y, q, th = x[fin], y[fin], q[fin], th[fin]
    lam = np.asarray(lam_fn(jnp.asarray(q)))
    # alpha = asin(c/q) through the SAME state closure the monitor
    # uses (supplied by the caller — state-consistent by construction)
    al = obs["_alpha"](q)
    Aa = np.tan(th - al)
    Bb = np.tan(al)
    den = 1.0 + lam * (Aa + Bb)
    val = (lam * Bb * (Aa + Bb) - (Aa - Bb)) / den
    good = np.isfinite(val)
    P = np.stack([x[good], y[good]], axis=1)
    qg, thg, alg = q[good], th[good], al[good]
    valg, deng = val[good], den[good]
    tree = cKDTree(P)
    # local cell scale at the lip (median nn distance)
    pE = np.array([obs["wall_x"][-1], obs["wall_y"][-1]])
    dnn, _ = tree.query(pE, k=6)
    cell = float(np.median(dnn[1:]))

    def interp(pt, arr, k=8):
        d, idx = tree.query(pt, k=k)
        w = 1.0 / np.maximum(d, 1e-12)
        return float(np.sum(w * arr[idx]) / np.sum(w)), float(d[0])

    # trace the C+ back from just inside the lip
    pt = pE.copy()
    step = 3.0 * cell
    v_here, _ = interp(pt, valg)
    prev = (pt.copy(), v_here)
    hit = None
    found = False
    for _ in range(200000):
        t_here, _ = interp(pt, thg)
        a_here, _ = interp(pt, alg)
        mslope = np.tan(t_here + a_here)
        dirv = -np.array([1.0, mslope])
        dirv /= np.linalg.norm(dirv)
        pt = pt + step * dirv
        if pt[0] <= 0.0 or pt[1] <= 0.0:
            break
        v_new, dmiss = interp(pt, valg)
        if dmiss > 10.0 * step:      # left the field
            break
        if v_new <= 0.0 <= prev[1]:
            # linear crossing between prev and pt
            tcr = prev[1] / max(prev[1] - v_new, 1e-300)
            hit = prev[0] + tcr * (pt - prev[0])
            found = True
            break
        prev = (pt.copy(), v_new)
    if hit is None:
        hit = pt                     # declared: no crossing found
    d0, i0 = tree.query(hit, k=1)
    # local |dval/ds| around D' for the derived position bands
    dnb, nb = tree.query(hit, k=12)
    fin_nb = np.isfinite(valg[nb])
    slope = np.abs(valg[nb][fin_nb] - valg[i0]) / np.maximum(
        dnb[fin_nb], 1e-300)
    dval_ds = float(np.median(slope[1:])) if fin_nb.sum() > 2 else 0.0
    v_at, _ = interp(hit, valg)
    return dict(x=float(hit[0]), y=float(hit[1]), q=float(qg[i0]),
                theta=float(thg[i0]), val_min=float(v_at),
                den=float(deng[i0]), dval_ds=dval_ds,
                cell=float(np.median(dnb[1:5])),
                crossing_found=found)


def stage_leg1(state_fn):
    ok = True
    lam_fn = LD.make_lambda_fn(state_fn)

    def alpha_np(q):
        c = np.asarray(jax.vmap(
            lambda qq: state_fn(qq, None)[3])(jnp.asarray(q)))
        return np.arcsin(np.minimum(1.0, c / np.asarray(q)))

    print("-- LEG 1: GENO at the instance, two resolutions --")
    # SECOND RESOLUTION = REFINEMENT direction (801/4001), NEVER the
    # halved one: at this instance NI = 201 sends GENO's outer TOC
    # bisection onto the registered N-74 path (non-physical bracket
    # 'mach1 insufficiente -> raddoppio' to Mrao ~ 80, inner loop hang
    # without error stop) — MEASURED in-session S24 and declared; the
    # finer direction is also the standard Richardson refinement.
    res = {}
    for tag, (ni, ne) in (("r1", (None, None)), ("r2", (801, 4001))):
        scr = os.path.join(
            os.environ.get("TEMP", "/tmp"), "s24_deftw_geno_" + tag)
        t0 = time.perf_counter()
        obs = geno_case_run(scr, NI_over=ni, Ne_over=ne)
        obs["_alpha"] = alpha_np
        dt = time.perf_counter() - t0
        dp = locate_dprime(obs, lam_fn)
        print("  [%s] %.0f s: %s; A4 rel = %s; CF = %.4f; "
              "theta_max = %.2f deg; wall %d pts, y_lip = %.5f"
              % (tag, dt, obs["def_marker"], obs["a4_rel"], obs["cf"],
                 obs["theta_max_deg"], len(obs["wall_x"]),
                 obs["wall_y"][-1]))
        print("  [%s] D' (our monitor on the GENO field): (x, y) = "
              "(%.4f, %.4f), q = %.1f, theta = %.3f deg, val_min = "
              "%.3e, den = %.3e, |dval/ds| = %.3e, cell = %.3e"
              % (tag, dp["x"], dp["y"], dp["q"], dp["theta"] / d2r,
                 dp["val_min"], dp["den"], dp["dval_ds"], dp["cell"]))
        ok &= check("%s: DEF branch ACTIVE (flagdef=1 marker)" % tag,
                    obs["def_marker"] is not None)
        ok &= check("%s: A4 mass identity present and O(1e-3) or "
                    "better" % tag,
                    obs["a4_rel"] is not None and obs["a4_rel"] < 1e-2)
        band_v = A1.K_RICH * dp["dval_ds"] * dp["cell"] + LAND_WIN
        ok &= check("%s: D' = val-zero crossing FOUND on the lip C+ "
                    "with |val(D')| = %.2e <= derived band %.2e"
                    % (tag, abs(dp["val_min"]), band_v),
                    dp["crossing_found"]
                    and abs(dp["val_min"]) <= band_v)
        res[tag] = dict(obs=dict(
            def_marker=obs["def_marker"],
            dtheta_comp=obs["dtheta_comp"], a4_rel=obs["a4_rel"],
            cf=obs["cf"], theta_max_deg=obs["theta_max_deg"],
            wall_x=[float(t) for t in obs["wall_x"]],
            wall_y=[float(t) for t in obs["wall_y"]]),
            dprime=dp)
    # GENO-side two-resolution wall band (Richardson error measure)
    w1x = np.array(res["r1"]["obs"]["wall_x"])
    w1y = np.array(res["r1"]["obs"]["wall_y"])
    w2x = np.array(res["r2"]["obs"]["wall_x"])
    w2y = np.array(res["r2"]["obs"]["wall_y"])
    lo = max(w1x.min(), w2x.min())
    hi = min(w1x.max(), w2x.max())
    xs = np.linspace(lo, hi, 600)
    dgeno = float(np.max(np.abs(np.interp(xs, w1x, w1y)
                                - np.interp(xs, w2x, w2y))))
    ye_res = float(abs(w1y[-1] - CASE["yt"] * np.sqrt(CASE["eps"])))
    print("  GENO two-resolution wall difference (max |dy|) = %.4e; "
          "lip constraint residual |ye - yt sqrt(eps)| = %.4e"
          % (dgeno, ye_res))
    d12 = float(np.hypot(
        res["r1"]["dprime"]["x"] - res["r2"]["dprime"]["x"],
        res["r1"]["dprime"]["y"] - res["r2"]["dprime"]["y"]))
    band12 = A1.K_RICH * max(res["r1"]["dprime"]["cell"],
                             res["r2"]["dprime"]["cell"])
    ok &= check("D' two-resolution agreement |D'_r1 - D'_r2| = %.3e "
                "<= K_RICH cell band %.3e" % (d12, band12),
                d12 <= band12)
    # D' landing/quantization bands from measured gradients
    dp = res["r1"]["dprime"]

    def val_of(qth):
        qq, tt = qth[0], qth[1]
        c = state_fn(qq, None)[3]
        alv = jnp.arcsin(jnp.minimum(1.0, c / qq))
        dalpha = jax.grad(lambda z: jnp.arcsin(jnp.minimum(
            1.0, state_fn(z, None)[3] / z)))(qq)
        lamv = qq * dalpha
        Av = jnp.tan(tt - alv)
        Bv = jnp.tan(alv)
        return ((lamv * Bv * (Av + Bv) - (Av - Bv))
                / (1.0 + lamv * (Av + Bv)))

    gq, gth = np.asarray(jax.grad(val_of)(
        jnp.array([dp["q"], dp["theta"]])))
    ds_land = (LAND_WIN + abs(gth) * 0.5 * DTHETA_PM) / max(
        dp["dval_ds"], 1e-300)
    band_dprime = A1.K_RICH * max(dp["cell"], ds_land)
    print("  D' bands: |dval/dq| = %.3e, |dval/dtheta| = %.3e; "
          "landing+PM-step position band = %.4e; grid cell = %.4e; "
          "K_RICH-safeguarded D' band = %.4e"
          % (abs(gq), abs(gth), ds_land, dp["cell"], band_dprime))
    art = dict(case=CASE, res=res, dgeno_wall=dgeno, ye_res=ye_res,
               dval_dq=float(gq), dval_dth=float(gth),
               ds_land=float(ds_land), band_dprime=float(band_dprime))
    json.dump(art, open(ART_LEG1, "w"), indent=1)
    print("  leg-1 artifact -> %s" % ART_LEG1)
    return ok


# ======================================================================
# LEG 2 — engine setup, seeds, instance derivations
# ======================================================================
def setup_engine():
    tab = A1.prep_tab(A1.build_tab_nasa())
    c1 = TH.build_c1(tab)

    def state_c1(q, ta_ignored=None):
        return TH.state_q_c1(q, c1)

    solv = SC.cached_solvers(("thc1_nasa", 1.0), state_c1, 1.0)
    cfg = dict(NI=CASE["NI"], Nw=CASE["Nw"], da_deg=CASE["da_deg"],
               yt=CASE["yt"], rtu=CASE["rtu"], rtd=CASE["rtd"],
               xtronc=CASE["xtronc"])
    return tab, state_c1, solv, cfg


def wall_to_class(wx, wy, cfg, n_nodes):
    """GENO wall -> our uniform node class (the [X-O33B] geno_design
    recipe, instance-general), with the representation check."""
    from scipy.interpolate import CubicSpline
    L = CASE["xtronc"]
    yL = CASE["yt"] * np.sqrt(CASE["eps"])
    xg = np.linspace(wx.min() + 1e-6, min(2.5, wx.max()), 800)
    sg = np.gradient(np.interp(xg, wx, wy), xg)
    thB = float(np.arctan(np.max(sg)))
    xB = cfg["rtd"] * np.sin(thB)
    sel = wx >= xB
    cs = CubicSpline(wx[sel], wy[sel])
    xs = xB + (L - xB) * np.arange(1, n_nodes + 1) / n_nodes
    ys = cs(np.minimum(xs, wx[sel].max()))
    ys[-1] = yL                     # the eps equality pins the lip
    W = np.concatenate([[thB], ys])
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = n_nodes, None
    try:
        _, _, nx, ny, Msp = TV.wall_geometry(
            jnp.asarray(W), jnp.array([CASE["yt"], cfg["rtu"],
                                       cfg["rtd"]]), L)
        xs_chk = wx[sel & (wx <= L)]
        yr = np.array([float(TV.spline_eval(jnp.float64(t), nx, ny,
                                            Msp)[0]) for t in
                       xs_chk[:: max(1, len(xs_chk) // 200)]])
        rep = float(np.max(np.abs(
            yr - wy[sel & (wx <= L)][:: max(1, len(xs_chk) // 200)])))
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    return W, thB, rep


# ======================================================================
# CONTROL-SURFACE MARGIN SCOPE (S24 formulation adjudication of record)
# ======================================================================
# MEASURED AT THIS INSTANCE (S24, both codes): the attachment region
# legitimately carries val ~ -0.81 on CERTIFIED shock-free fields
# (ours at the GENO-seeded design AND GENO's own defnoz output field),
# so "val >= mu0 > 0 over every W-dependent lane" is INFEASIBLE for
# EVERY design of the class here, including GENO's own DEF design —
# it cannot be the constraint EQ-v2 speaks of. The locus the theory
# names (S4, Direction A, H2) is the TERMINAL-C+ CONTROL SURFACE,
# where the (G) boundary is the design-validity boundary and where
# the DEF construction lands D'. The [X-DEFTW] margin bucket is
# therefore the CONTROL-SURFACE bucket (chain nodes, registered end
# exclusion) — the whole-field bucket of [X-MGOV] remains valid AT
# ITS OWN mild instance (eps = 4, all-positive field) and its record
# is untouched; the bucket-scope boundary is an R4 registration duty
# of this session. Freezing semantics: the chain lane mask is built
# at each RUNG START from that rung's record and FROZEN across the
# rung's segments (same spirit as RK-G plan freezing, declared);
# shape mismatches on later segments are cropped/padded and COUNTED.


def chain_nodes_ki(out):
    """(k, i) grid indices of the terminal-C+ chain (the [X-O33B]
    cplus_chain walk, kept as INDICES so nodes map onto the traced
    val_diag lane grid), the chain points, the control-surface mask
    (owner >= n_fan + n_arc, the S19 locus correction), and the
    registered end exclusion (STENCIL_RADIUS both ends)."""
    cols = out["cols"]
    index = {}
    for k, col in enumerate(cols):
        cl = col["cline"]
        for i in range(cl.shape[0]):
            index[(float(cl[i, 0]), float(cl[i, 1]))] = (k, i)
    K = len(cols) - 1
    start = (K, 1) if cols[K]["cline"].shape[0] > 1 else (K - 1, 1)
    kis, pts = [], []
    k, i = start
    while True:
        cl = cols[k]["cline"]
        kis.append((k, i))
        pts.append(np.asarray(cl[i]))
        cp = cols[k]["cplus"]
        if i - 1 < 0 or i - 1 >= cp.shape[0]:
            break
        nxt = cp[i - 1]
        key = (float(nxt[0]), float(nxt[1]))
        if key not in index:
            break
        k, i = index[key]
    kis = kis[::-1]
    pts = np.stack(pts[::-1])
    owner = np.array([k for k, _ in kis])
    cs = owner >= (out["n_fan"] + out["n_arc"])
    idx = np.where(cs)[0]
    reg = cs.copy()
    if len(idx) > 2 * O33.STENCIL_RADIUS:
        reg[idx[:O33.STENCIL_RADIUS]] = False
        reg[idx[-O33.STENCIL_RADIUS:]] = False
    return kis, pts, cs, reg


def val_of_pts(pts, state_fn):
    """(G)/Lambda-form val at march points (u, v in cols 2:4),
    through the SAME state closure and AD Lambda as the monitor."""
    alpha_of, lam_of = MG.make_alpha_lam(state_fn)
    q = np.hypot(pts[:, 2], pts[:, 3])
    th = np.arctan2(pts[:, 3], pts[:, 2])
    al = np.asarray(jax.vmap(alpha_of)(jnp.asarray(q)))
    lam = np.asarray(lam_of(jnp.asarray(q)))
    Aa = np.tan(th - al)
    Bb = np.tan(al)
    den = 1.0 + lam * (Aa + Bb)
    return (lam * Bb * (Aa + Bb) - (Aa - Bb)) / den, den, q, th


def lane_mask_from_chain(out, kis, sel, lane_shape):
    """Boolean mask on the traced val_diag lane grid (columns = arc +
    contour, fan excluded => k_lane = k - n_fan; lane rows = [wall,
    cells..., axis(last)] matching cline order for i < n_cells+1)."""
    m = np.zeros(lane_shape, dtype=bool)
    n_fan = out["n_fan"]
    for (k, i), s in zip(kis, sel):
        if not s:
            continue
        kl = k - n_fan
        if 0 <= kl < lane_shape[0] and 0 <= i < lane_shape[1] - 1:
            m[kl, i] = True
    return m


def cs_stats(tab, cfg, state_fn, solv, W, label=""):
    """Record + control-surface chain val stats at a design."""
    old = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W) - 1, None
    try:
        out, plan = TV.run_toc_record(np.asarray(W, float), tab, cfg,
                                      state_fn=state_fn, solvers=solv,
                                      return_field=True)
    finally:
        TV.M_NODES, TV.KNOT_XI = old
    kis, pts, cs, reg = chain_nodes_ki(out)
    val, den, q, th = val_of_pts(pts, state_fn)
    good = reg & np.isfinite(val)
    return dict(out=out, plan=plan, kis=kis, pts=pts, cs=cs, reg=reg,
                val=val, den=den, q=q,
                m_ref=float(val[good].min()) if good.any() else np.nan,
                N=int(good.sum()),
                q_ref=float(q[good].mean()) if good.any() else np.nan,
                i_min=int(np.where(good)[0][np.argmin(val[good])])
                if good.any() else -1)


def make_margin_fn_cs(tab, cfg, plan, state_fn, solvers, rho, mu0,
                      m_ref, q_ref, mask, shape_events):
    """Traced W -> margin on the CONTROL-SURFACE lane bucket (the
    MG.make_margin_fn structure with the chain mask applied; G1
    finite-fallback semantics preserved; frac_bad denominator = the
    masked lane count)."""
    runv = TV.make_run_toc_scan_jit(tab, cfg, plan, state_fn=state_fn,
                                    solvers=solvers, val_diag=True)
    alpha_of, lam_of = MG.make_alpha_lam(state_fn)

    def margin_W(W):
        _w, q_l, th_l, act = runv(W)
        mloc = mask
        if tuple(q_l.shape) != tuple(mask.shape):
            shape_events["mask_shape_adapt"] += 1
            mm = np.zeros(q_l.shape, dtype=bool)
            r = min(mask.shape[0], q_l.shape[0])
            c = min(mask.shape[1], q_l.shape[1])
            mm[:r, :c] = mask[:r, :c]
            mloc = mm
        sel = jnp.asarray(mloc.reshape(-1))
        q = q_l.reshape(-1)
        th = th_l.reshape(-1)
        a = act.reshape(-1) & sel
        fin = a & jnp.isfinite(q) & jnp.isfinite(th) & (q > 0.0)
        q_z = jnp.where(fin, q, q_ref)
        th_z = jnp.where(fin, th, 0.0)
        al = jax.vmap(alpha_of)(q_z)
        lam = lam_of(q_z)
        A = jnp.tan(th_z - al)
        B = jnp.tan(al)
        val = (lam * B * (A + B) - (A - B)) / (1.0 + lam * (A + B))
        fin2 = fin & jnp.isfinite(val)
        n_fin = jnp.sum(fin2)
        n_sel = max(int(mloc.sum()), 1)
        vmin = jnp.min(jnp.where(fin2, val, jnp.inf))
        vmin_s = jnp.where(n_fin > 0, vmin, 0.0)
        e = jnp.where(fin2, jnp.exp(-rho * (jnp.where(fin2, val,
                                                      vmin_s)
                                            - vmin_s)), 0.0)
        ks = vmin_s - jnp.log(jnp.maximum(jnp.sum(e), 1e-300)) / rho
        ks_part = jnp.where(n_fin > 0, ks, -A1.K_RICH * m_ref)
        frac_bad = (n_sel - n_fin) / n_sel
        return ks_part - A1.K_RICH * m_ref * frac_bad - mu0

    return margin_W


def make_margin_factory_cs(tab, cfg, state_fn, solvers, rho, mu0,
                           m_ref, q_ref, mask, counters):
    """run_trsqp margin_factory with the control-surface bucket."""
    def factory(plan, Dv):
        margin_W = make_margin_fn_cs(tab, cfg, plan, state_fn,
                                     solvers, rho, mu0, m_ref, q_ref,
                                     mask, counters)
        mval_grad = jax.jit(jax.value_and_grad(margin_W))

        def m_np(u):
            v, _ = mval_grad(jnp.asarray(np.asarray(u) * Dv))
            v = float(v)
            if not np.isfinite(v):
                counters["m_nonfinite"] += 1
                return -2.0 * A1.K_RICH * m_ref
            return v

        def gm_np(u):
            _, g = mval_grad(jnp.asarray(np.asarray(u) * Dv))
            g = np.asarray(g) * Dv
            if not np.all(np.isfinite(g)):
                counters["gm_nonfinite"] += 1
                g = np.where(np.isfinite(g), g, 0.0)
            return g

        return m_np, gm_np

    return factory


def stage_derive(tab, state_fn, solv, cfg):
    ok = True
    leg1 = json.load(open(ART_LEG1))
    wx = np.array(leg1["res"]["r1"]["obs"]["wall_x"])
    wy = np.array(leg1["res"]["r1"]["obs"]["wall_y"])
    print("-- derive: GENO-seeded class representative + perturbed "
          "start --")
    W0, thB, rep = wall_to_class(wx, wy, cfg, M_NODES)
    print("  W0 (M = %d): thB = %.3f deg; representation error vs "
          "GENO wall = %.3e" % (M_NODES, thB / d2r, rep))
    W16, _, rep16 = wall_to_class(wx, wy, cfg, 2 * M_NODES)
    print("  class band: M-vs-2M interpolant representation errors "
          "%.3e / %.3e" % (rep, rep16))
    print("-- derive: CONTROL-SURFACE val stats at the GENO seed --")
    st0 = cs_stats(tab, cfg, state_fn, solv, W0, "W0")
    print("  [W0(GENO-seed)] certified %s (worst %.3e); chain %d "
          "nodes (%d registered CS); min CS val = %.6e at chain idx "
          "%d; min |den| on CS = %.4e"
          % (st0["out"]["cert_worst"] <= 1.0, st0["out"]["cert_worst"],
             len(st0["kis"]), st0["N"], st0["m_ref"], st0["i_min"],
             float(np.min(np.abs(st0["den"][st0["reg"]])))))
    ok &= check("GENO seed certified", st0["out"]["cert_worst"] <= 1.0)
    # START SELECTION (general, measured — no tuned constants): the
    # [X-TOCV] recipe bump at amplitude a = 0.015/2^j, both signs,
    # smallest j giving a certified start with CS margin > 0; if the
    # SEED itself is margin-positive it is admitted as candidate
    # of last resort (declared: less discriminating).
    Wp, st_p, sel_note = None, None, "none"
    for j in range(4):
        amp = 0.015 / 2.0 ** j
        for sgn in (+1.0, -1.0):
            Wc = W0.copy()
            xB = cfg["rtd"] * np.sin(W0[0])
            L = CASE["xtronc"]
            n = len(W0) - 1
            xsn = xB + (L - xB) * np.arange(1, n + 1) / n
            bump = amp * W0[1:-1] * np.sin(np.pi * (xsn[:-1] - xB)
                                           / (L - xB))
            Wc[1:-1] = Wc[1:-1] + sgn * bump
            try:
                stc = cs_stats(tab, cfg, state_fn, solv, Wc,
                               "cand")
            except RuntimeError as err:
                print("  [start cand a=%.4f sgn=%+.0f] march raised "
                      "(%s) — candidate discarded, declared"
                      % (amp, sgn, str(err)[:80]))
                continue
            print("  [start cand a=%.4f sgn=%+.0f] cert %.3e, CS "
                  "m_ref = %.6e"
                  % (amp, sgn, stc["out"]["cert_worst"],
                     stc["m_ref"]))
            if stc["out"]["cert_worst"] <= 1.0 and stc["m_ref"] > 0:
                Wp, st_p = Wc, stc
                sel_note = "bump a=%.4f sgn=%+.0f" % (amp, sgn)
                break
        if Wp is not None:
            break
    if Wp is None and st0["m_ref"] > 0:
        Wp, st_p = W0.copy(), st0
        sel_note = "seed itself (declared: less discriminating)"
    ok &= check("feasible start found (%s)" % sel_note, Wp is not None)
    if Wp is None:
        json.dump(dict(case=CASE, fail="no feasible start",
                       m_ref_seed=st0["m_ref"]),
                  open(ART_DERIVE, "w"), indent=1)
        return False
    m_ref = st_p["m_ref"]
    q_ref = st_p["q_ref"]
    N = st_p["N"]
    ladder = [m_ref / 2.0 ** k for k in range(1, N_RUNGS + 1)]
    rho = A1.K_RICH * np.log(N) / ladder[-1]
    print("  CONTROL-SURFACE bucket: N = %d registered chain lanes; "
          "m_ref = %.6e; ladder mu0 = %s; rho = %.4e (gap = %.4e)"
          % (N, m_ref, ["%.4e" % t for t in ladder], rho,
             np.log(N) / rho))
    # dV_pert cross-implementation band on THIS q range ([X-MGOV] D4)
    st = dict(q=st_p["q"][st_p["reg"]])
    alpha_of, lam_of = MG.make_alpha_lam(state_fn)
    qs = np.linspace(st["q"].min(), st["q"].max(), 24)

    def lam_fd(q, dv):
        return q * (float(alpha_of(jnp.float64(q + dv)))
                    - float(alpha_of(jnp.float64(q - dv)))) / (2 * dv)

    lam_ad = np.asarray(lam_of(jnp.asarray(qs)))
    fd10 = np.array([lam_fd(q, 1.0) for q in qs])
    fd05 = np.array([lam_fd(q, 0.5) for q in qs])
    band = A1.K_RICH * np.abs(fd10 - fd05) + 100 * EPS * np.abs(lam_ad)
    worst = float(np.max(np.abs(fd10 - lam_ad) / band))
    print("  [R-FD] max |Lam_FD(1.0) - Lam_AD|/band = %.3f on THIS "
          "q-range [%.0f, %.0f]" % (worst, qs.min(), qs.max()))
    ok &= check("R-FD: GENO-recipe FD Lambda inside the derived band "
                "at the instance", worst <= 1.0)
    # lane mask on the traced val_diag grid (one probe eval for the
    # shapes; the chain (k, i) set comes from the start record)
    runv = TV.make_run_toc_scan_jit(tab, cfg, st_p["plan"],
                                    state_fn=state_fn, solvers=solv,
                                    val_diag=True)
    _w, q_l, _t, _a = runv(jnp.asarray(np.asarray(Wp, float)))
    lane_shape = tuple(int(t) for t in q_l.shape)
    mask = lane_mask_from_chain(st_p["out"], st_p["kis"],
                                st_p["reg"], lane_shape)
    print("  lane grid %s; chain mask lanes = %d (of %d registered "
          "CS nodes; unmapped = axis-row nodes, declared)"
          % (lane_shape, int(mask.sum()), st_p["N"]))
    ok &= check("chain mask nonempty and >= 80%% of the registered "
                "CS nodes mapped",
                mask.sum() >= 0.8 * st_p["N"])
    # margin-gradient spot check + corrupted control at the start
    print("-- derive: margin gradient O3.1-style spot at the start "
          "(CONTROL-SURFACE bucket) --")
    shape_events = dict(mask_shape_adapt=0, m_nonfinite=0,
                        gm_nonfinite=0)
    margin_W = make_margin_fn_cs(tab, cfg, st_p["plan"], state_fn,
                                 solv, rho, ladder[0], m_ref, q_ref,
                                 mask, shape_events)
    mj = jax.jit(margin_W)
    gm = np.asarray(jax.grad(margin_W)(jnp.asarray(Wp)))
    rng = np.random.default_rng(3)
    dv = rng.standard_normal(len(Wp))
    dv /= np.linalg.norm(dv)
    Wj = jnp.asarray(Wp)

    def dd(hsc):
        h = EPS ** (1.0 / 3.0) * hsc
        return (float(mj(Wj + h * jnp.asarray(dv)))
                - float(mj(Wj - h * jnp.asarray(dv)))) / (2.0 * h)

    d1, d2 = dd(1.0), dd(0.5)
    tol_g = A1.K_RICH * (abs(d1 - d2) + A1.C_FLOOR * EPS ** (2.0 / 3.0)
                         * max(1.0, abs(float(mj(Wj)))))
    ok &= check("R-GRAD: AD margin gradient inside the derived band "
                "(|diff| %.3e vs %.3e)" % (abs(float(gm @ dv) - d2),
                                           tol_g),
                abs(float(gm @ dv) - d2) <= tol_g)
    ok &= check("R-GRAD control: corrupted gradient rejected",
                abs(float((gm * 1.01 + 1e-3 * np.abs(gm).max()) @ dv)
                    - d2) > tol_g)
    art = dict(case=CASE, M=M_NODES, W0=[float(t) for t in W0],
               W16=[float(t) for t in W16],
               Wp=[float(t) for t in Wp], rep=rep, rep16=rep16,
               start_note=sel_note,
               m_ref=m_ref, q_ref=q_ref, N=N, rho=float(rho),
               ladder=[float(t) for t in ladder],
               m_ref_seed=st0["m_ref"],
               den_min_cs=float(np.min(np.abs(
                   st_p["den"][st_p["reg"]]))),
               shape_events=shape_events)
    json.dump(art, open(ART_DERIVE, "w"), indent=1)
    print("  derive artifact -> %s" % ART_DERIVE)
    return ok


# ======================================================================
# CAMPAIGN — the decisive ladder walk + F1-F7 adjudication
# ======================================================================
def rung_logs(st, state_fn, mu0, gap, label):
    """The panel's two mandatory logs + F-branch observables at a
    design, ON THE CONTROL-SURFACE bucket (S24 scope of record):
    argmin-CS-val chain node (coordinates), active census along the
    chain (1-D consecutive-run clustering), end-vs-interior binding
    classification (the H2 reading: lip-end / kernel-end binding =
    exclusion sites; strictly interior = classical D' site), f2
    drift (registered norm), wall. st = cs_stats(...) output."""
    out = st["out"]
    reg = st["reg"]
    val = st["val"]
    pts = st["pts"]
    idx = np.where(reg & np.isfinite(val))[0]
    vv = val[idx]
    i_loc = int(np.argmin(vv))
    i_min = int(idx[i_loc])
    # chain-local spacing at the argmin (position band for F2)
    p_min = pts[i_min][:2]
    nb = pts[max(0, i_min - 1)][:2], pts[min(len(pts) - 1,
                                             i_min + 1)][:2]
    r_loc = O33.STENCIL_RADIUS * max(np.hypot(*(p_min - nb[0])),
                                     np.hypot(*(p_min - nb[1])))
    # end-vs-interior: index distance from the registered ends
    d_end = min(i_loc, len(idx) - 1 - i_loc)
    interior = d_end > O33.STENCIL_RADIUS
    # active census on the chain: consecutive-run clustering
    act = vv <= mu0 + gap
    n_act = int(act.sum())
    n_cl = int(np.sum(act & ~np.concatenate([[False], act[:-1]])))
    act_end = bool(act[0] or act[-1])
    rep = O33.surface_report(out, state_fn, label)
    return dict(val_min=float(vv[i_loc]),
                argmin_xy=(float(p_min[0]), float(p_min[1])),
                argmin_interior=bool(interior),
                d_end_nodes=int(d_end), r_chain=float(r_loc),
                census=(n_act, n_cl, act_end),
                f2_drift=rep["d2"], f2_mean=rep["f2"],
                wall=np.asarray(out["wall"][:, :2]))


def stage_campaign(tab, state_fn, solv, cfg):
    ok = True
    leg1 = json.load(open(ART_LEG1))
    der = json.load(open(ART_DERIVE))
    W0 = np.array(der["W0"])
    Wp = np.array(der["Wp"])
    ladder = der["ladder"]
    m_ref, q_ref, rho = der["m_ref"], der["q_ref"], der["rho"]
    gap = np.log(der["N"]) / rho
    yL = CASE["yt"] * np.sqrt(CASE["eps"])
    counters = dict(m_nonfinite=0, gm_nonfinite=0, mask_shape_adapt=0)
    print("-- campaign: margin-constrained ladder on the CONTROL-"
          "SURFACE bucket (tightest first, warm continuation; "
          "floor -> 0) --")
    W_cur = Wp
    rungs = []
    t_camp = time.perf_counter()
    old_class = (TV.M_NODES, TV.KNOT_XI)
    TV.M_NODES, TV.KNOT_XI = len(W_cur) - 1, None
    for k, mu0 in enumerate(ladder, start=1):
        print("-- rung %d/%d: mu0 = %.6e --" % (k, len(ladder), mu0))
        st_cur = cs_stats(tab, cfg, state_fn, solv, W_cur)
        if st_cur["out"]["cert_worst"] > 1.0:
            print("  [rung %d] start not certified (worst %.3e) — "
                  "declared, campaign stops" %
                  (k, st_cur["out"]["cert_worst"]))
            ok = False
            break
        # rung-frozen chain lane mask (declared freezing semantics)
        runv = TV.make_run_toc_scan_jit(tab, cfg, st_cur["plan"],
                                        state_fn=state_fn,
                                        solvers=solv, val_diag=True)
        _w, q_l, _t, _a = runv(jnp.asarray(W_cur))
        mask = lane_mask_from_chain(st_cur["out"], st_cur["kis"],
                                    st_cur["reg"],
                                    tuple(int(t) for t in q_l.shape))
        # derived optimizer tolerance ([X-MGOV] campaign recipe)
        J_w, g_w, scalJ_w = AK_gJ(W_cur, None, tab, cfg,
                                  st_cur["plan"], state_fn, solv)
        dp_o31, tol_dp = AK_o31(W_cur, None, scalJ_w, g_w, J_w)
        ok &= check("rung %d O3.1 at start (%.3e <= %.3e)"
                    % (k, dp_o31, tol_dp), dp_o31 <= tol_dp)
        gtol = max(tol_dp, 1e-8 * float(np.linalg.norm(g_w)))
        factory = make_margin_factory_cs(tab, cfg, state_fn, solv,
                                         rho, mu0, m_ref, q_ref,
                                         mask, counters)
        t0 = time.perf_counter()
        try:
            opt = TV.run_trsqp(W_cur, tab, cfg, yL, gtol=gtol,
                               xtol=1e-10, state_fn=state_fn,
                               solvers=solv, verbose=0,
                               margin_factory=factory)
        except RuntimeError as err:
            print("  [rung %d] walk gate failure (REQ-NONSTALL "
                  "breach = G1 rejector): %s" % (k, err))
            ok = False
            break
        dt = time.perf_counter() - t0
        res = opt["res"]
        W_new = np.asarray(opt["W"], dtype=float)
        # multiplier under the S24-T1 CLOSED convention
        mu_est = None
        try:
            vlist = [np.atleast_1d(np.asarray(t)).ravel()
                     for t in res.v]
            if len(vlist) > 1:
                mu_est = -float(vlist[-1][0])
        except Exception:
            pass
        st_new = cs_stats(tab, cfg, state_fn, solv, W_new)
        lg = rung_logs(st_new, state_fn, mu0, gap, "rung %d" % k)
        margin_active = lg["val_min"] <= mu0 + gap
        print("  [rung %d] %.0f s, segs %d, nit %d, status %s, KKT "
              "%.3e; J = %.7e; mu(M0, B-stat) = %s; min CS val %.6e "
              "(mu0 + gap = %.6e) -> margin %s; argmin (%.4f, %.4f) "
              "%s (d_end %d nodes, r_loc %.3e); census (n_act, "
              "n_clusters, end-active) = %s; f2 drift %.4e; "
              "nf-counters %s"
              % (k, dt, opt["n_segments"], opt["nit_total"],
                 getattr(res, "status", None),
                 float(getattr(res, "optimality", np.nan)),
                 float(-res.fun), mu_est, lg["val_min"], mu0 + gap,
                 "ACTIVE" if margin_active else "inactive",
                 lg["argmin_xy"][0], lg["argmin_xy"][1],
                 "INTERIOR" if lg["argmin_interior"] else "CHAIN-END",
                 lg["d_end_nodes"], lg["r_chain"], lg["census"],
                 lg["f2_drift"], counters))
        rungs.append(dict(
            rung=k, mu0=mu0, J=float(-res.fun),
            kkt=float(getattr(res, "optimality", np.nan)),
            status=int(getattr(res, "status", -1)),
            mu_est=mu_est, val_min=lg["val_min"],
            margin_active=bool(margin_active),
            argmin_xy=lg["argmin_xy"],
            argmin_interior=lg["argmin_interior"],
            d_end_nodes=lg["d_end_nodes"], r_chain=lg["r_chain"],
            census=lg["census"], f2_drift=lg["f2_drift"],
            f2_mean=lg["f2_mean"],
            W=[float(t) for t in W_new],
            wall_x=[float(t) for t in lg["wall"][:, 0]],
            wall_y=[float(t) for t in lg["wall"][:, 1]],
            wtime=dt))
        W_cur = W_new
    TV.M_NODES, TV.KNOT_XI = old_class
    t_camp = time.perf_counter() - t_camp
    print("  campaign wall time: %.0f s" % t_camp)
    ok &= check("campaign: no silently-patched nonfinite events "
                "(%s)" % counters,
                counters["m_nonfinite"] == 0
                and counters["gm_nonfinite"] == 0)

    # ---------------- F1-F7 ADJUDICATION ----------------------------
    print("-- F1-F7 adjudication (panel branches VERBATIM; every "
          "branch a verdict; claim cap: no classical-optimality "
          "wording) --")
    verdicts = {}
    if rungs:
        gx = np.array(leg1["res"]["r1"]["obs"]["wall_x"])
        gy = np.array(leg1["res"]["r1"]["obs"]["wall_y"])
        xB = cfg["rtd"] * np.sin(np.array(rungs[-1]["W"])[0])
        xs = np.linspace(xB + 0.05, CASE["xtronc"] - 1e-6, 400)
        gaps = []
        for r in rungs:
            wxo = np.array(r["wall_x"])
            wyo = np.array(r["wall_y"])
            gaps.append(float(np.max(np.abs(
                np.interp(xs, wxo, wyo) - np.interp(xs, gx, gy)))))
        # combined F1 band: GENO two-res + class-representation +
        # D'-induced position band (all measured leg-1/derive)
        band_f1 = (A1.K_RICH * leg1["dgeno_wall"] + leg1["ye_res"]
                   + der["rep"] + leg1["band_dprime"])
        shrink = all(gaps[i + 1] <= gaps[i] + 1e-12
                     for i in range(len(gaps) - 1))
        print("  F1: wall gap per rung = %s; combined band = %.4e; "
              "monotone shrink toward mu0->0: %s"
              % (["%.4e" % t for t in gaps], band_f1, shrink))
        verdicts["F1"] = dict(
            fired=bool(not (shrink and gaps[-1] <= band_f1)),
            gaps=gaps, band=float(band_f1),
            note="joint mesh+knot refinement half = refine stage")
        dp = leg1["res"]["r1"]["dprime"]
        dlast = float(np.hypot(rungs[-1]["argmin_xy"][0] - dp["x"],
                               rungs[-1]["argmin_xy"][1] - dp["y"]))
        band_f2 = max(leg1["band_dprime"],
                      A1.K_RICH * rungs[-1]["r_chain"])
        dseq = [float(np.hypot(r["argmin_xy"][0] - dp["x"],
                               r["argmin_xy"][1] - dp["y"]))
                for r in rungs]
        print("  F2: |argmin - D'| per rung = %s; band = %.4e"
              % (["%.4e" % t for t in dseq], band_f2))
        verdicts["F2"] = dict(fired=bool(dlast > band_f2),
                              dseq=dseq, band=float(band_f2))
        # F3: f2 drift on our optimum and on the GENO representative
        st_g = cs_stats(tab, cfg, state_fn, solv, W0)
        lg_g = rung_logs(st_g, state_fn, ladder[-1], gap,
                         "GENO-representative")
        # instance-derived f2 bar (the [X-O33B] two-resolution
        # construction at THIS instance, on the GENO representative)
        cfg2 = O33.refine(cfg, 2)
        out_g2, _ = O33.march_design(W0, len(W0) - 1, tab, cfg2,
                                     state_fn, solv)
        rep_g2 = O33.surface_report(out_g2, state_fn, "GENO-rep r=2")
        bar_f2d = (A1.K_RICH * abs(lg_g["f2_drift"] - rep_g2["d2"])
                   + A1.NEWTON_TOL_FACTOR * EPS
                   * int(out_g2["cert_n"]))
        print("  F3: f2 drift ours = %.4e, GENO-rep = %.4e (r2 "
              "%.4e); instance-derived bar = %.4e"
              % (rungs[-1]["f2_drift"], lg_g["f2_drift"],
                 rep_g2["d2"], bar_f2d))
        verdicts["F3"] = dict(
            fired=bool(rungs[-1]["f2_drift"] > bar_f2d
                       or lg_g["f2_drift"] > bar_f2d),
            ours=rungs[-1]["f2_drift"], geno=lg_g["f2_drift"],
            bar=float(bar_f2d))
        # F4: val_min tracks mu0 -> 0 (active) — extrapolate
        act = [r for r in rungs if r["margin_active"]]
        track = [abs(r["val_min"] - r["mu0"]) <= 3 * gap for r in act]
        print("  F4: val_min vs mu0 tracking (|val_min - mu0| <= "
              "3 gap): %s over %d active rungs"
              % (track, len(act)))
        verdicts["F4"] = dict(fired=bool(len(act) == 0
                                         or not all(track)),
                              n_active=len(act))
        interior_seq = [r["argmin_interior"] for r in act]
        verdicts["F5"] = dict(
            fired=bool(len(act) > 0 and not any(interior_seq)),
            interior=interior_seq,
            note="CS scope: chain-END binding (lip/kernel end) = the "
                 "H2 exclusion sites; INTERIOR chain node = a "
                 "classical D' site")
        print("  F5: active argmin STRICTLY INTERIOR on the chain "
              "per active rung: %s" % interior_seq)
        ncl_seq = [r["census"][1] for r in act]
        verdicts["F6"] = dict(
            fired=bool(any(c > 1 for c in ncl_seq)), clusters=ncl_seq)
        print("  F6: active-cusp clusters (1-D consecutive runs) per "
              "active rung: %s" % ncl_seq)
        # F7: J (floor->0, last rung as the closest-to-limit reading)
        # vs J(GENO representative) through the SAME objective
        old = (TV.M_NODES, TV.KNOT_XI)
        TV.M_NODES, TV.KNOT_XI = len(W0) - 1, None
        try:
            out_j, plan_j = TV.run_toc_record(
                W0, tab, cfg, state_fn=state_fn, solvers=solv)
            runj = TV.make_run_toc_scan_jit(
                tab, cfg, plan_j, state_fn=state_fn, solvers=solv)
            J_def = float(TV.thrust_J(runj(jnp.asarray(W0)), tab,
                                      state_fn=state_fn))
        finally:
            TV.M_NODES, TV.KNOT_XI = old
        W16 = np.array(der["W16"])
        old = (TV.M_NODES, TV.KNOT_XI)
        TV.M_NODES, TV.KNOT_XI = len(W16) - 1, None
        try:
            out16, plan16 = TV.run_toc_record(
                W16, tab, cfg, state_fn=state_fn, solvers=solv)
            runj16 = TV.make_run_toc_scan_jit(
                tab, cfg, plan16, state_fn=state_fn, solvers=solv)
            J_def16 = float(TV.thrust_J(runj16(jnp.asarray(W16)),
                                        tab, state_fn=state_fn))
        finally:
            TV.M_NODES, TV.KNOT_XI = old
        Js = [r["J"] for r in rungs]
        band_f7 = A1.K_RICH * abs(J_def - J_def16)
        print("  F7 (SURPLUS-PREDICTION wording only): J per rung = "
              "%s; J_DEF(M) = %.7e, J_DEF(2M) = %.7e -> band = %.4e; "
              "J_last - J_DEF = %.4e"
              % (["%.6e" % t for t in Js], J_def, J_def16, band_f7,
                 Js[-1] - J_def))
        verdicts["F7"] = dict(
            fired=bool(Js[-1] - J_def > band_f7),
            J_ladder=Js, J_def=J_def, J_def16=J_def16,
            band=float(band_f7),
            wording="direct-side surplus prediction only (O3 gate)")
        for br in ("F1", "F2", "F3", "F4", "F5", "F6", "F7"):
            print("  BRANCH %s: %s" % (br, "FIRED" if
                                       verdicts[br]["fired"]
                                       else "not fired"))
    art = dict(case=CASE, rungs=rungs, verdicts=verdicts,
               counters=counters, t_campaign=t_camp)
    json.dump(art, open(ART_CAMP, "w"), indent=1)
    print("  campaign artifact -> %s" % ART_CAMP)
    return ok


def main():
    stage = os.environ.get("A1_DEFTW_STAGE", "leg1")
    print("== [X-DEFTW] F1b DEF twin falsifier (JAX %s; stage %s; "
          "instance %s) ==" % (jax.__version__, stage, CASE))
    tab, state_c1, solv, cfg = setup_engine()
    if stage == "leg1":
        ok = stage_leg1(state_c1)
    elif stage == "derive":
        ok = stage_derive(tab, state_c1, solv, cfg)
    elif stage == "campaign":
        ok = stage_campaign(tab, state_c1, solv, cfg)
    else:
        print("unknown stage %s" % stage)
        return 2
    print("VERDICT (machinery): %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

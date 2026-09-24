#!/usr/bin/env python3
"""THE SHROUDED PLUG: the plug march with a SECOND WALL [F3/A1, X-TWMU, X-MGDL]
(2026-09-24; owner: "proseguiamo con gli shrouded", the family that completes the
suite after the external-expansion plug was re-obtained on Rao 1961 and Humphreys
1971).

The plug march (a1_plug_march) gains `shroud=` -- a top wall from the start line
to its lip F, met by every column's C+ (the DIRECT top-wall cell
make_resid_walltop), the lip placed by the bell's inverse wall cell, and after F
the top row IS F's C- (the exit characteristic): no free jet, no ambient. This
carrier certifies that machinery on an EXACT solution and then twins GENO's
annular perfect nozzle (Migdal 1972, nozzle_type 9).

Stage source [X-TWMU] -- the exact two-ray channel. Spherical source flow
(a1_source_flow_oracle.Radial, diverging): every ray through the singular point
is an exact streamline, so a bottom ray and a top ray bound an exact conical
channel and the shroud, its lip F and the field on F's C- all have closed-form
values. Nothing but the interior, bottom-wall, TOP-WALL and LIP cells is
exercised.
  TW-1  every cell Newton-certified (both grids);
  TW-2  shroud wall pressure vs the closed form, inside the Richardson band
        (K_RICH x the coarse-fine move, per station);
  TW-3  the field DOWNSTREAM OF THE LIP (x > x_F: the rows below F's C-, F's
        C- itself) vs the closed form, q and theta, inside the band;
  TW-4  the lip F: its state vs the exact one, inside the band;
  TW-5  the record path untouched: the same channel marched with the FREE
        JET on top (shroud=None) is bit-identical to a1_plug_march before
        this brick on its wall array (regression, measured);
  R-1   rejector: a CURVED shroud (y * (1 + eps t^2), the ray property
        broken) leaves the TW-2 band.

Stage geno [X-MGDL] -- Migdal's perfect annular nozzle from GENO
(CASES/migdalnoz_ni50 or a run directory in MGDL_GENO_RUN): GENO's own uniform
start line (x = 0, y in [Y_L, Y_U], M_i 1.5, theta 0: exact data, nothing
interpolated), GENO's two walls (profile_cp = plug, profile_cm = shroud) as our
stations. The design makes the exit flow UNIFORM AND AXIAL at the 1-D exit Mach
of the area ratio (Migdal p. 4: the wall forces plus the inlet force must equal
the 1-D value), which gives EXACT known answers on our own mesh:
  MG-1  every cell certified;
  MG-2  F's C- (the top row after the lip) carries M = M_e(1-D) and theta = 0
        inside the band (Richardson between two of our grids, K_RICH x move,
        PLUS the reference's own resolution class, ref_class: what the reading
        changes by between GENO's NI 50 and NI 1001 walls) -- the design's exit
        line read on OUR mesh;
  MG-3  the last column (the plug tip's C+) is uniform likewise;
  MG-4  THRUST CLOSURE: F_in + push(plug) + push(shroud) over p0 A* = the 1-D
        vacuum thrust coefficient of the area ratio, inside the band (the
        shroud push carries the +dy sign: a rising top wall pushes the fluid
        forward);
  MG-5  mass: the flux through the start line = the flux through the exit
        polyline (last column, then F's C- back to F), inside the band;
  MG-6  the wall pressures p/p0 (plug and shroud) against GENO's own field, read
        at the wall nodes (which are field points), inside our Richardson band;
  R-2   rejector: the shroud term with the plug's sign fails MG-4;
  R-3   rejector: the shroud lifted by 1 percent (ramped from the start) fails MG-2.
GENO's walls carry GENO's own discretisation error (NI 50 in the case of
record): where that dominates the band the check fails honestly and the NI 1001
runs (RDE/handoff/shroud_2026-09-24/geno_migdal) are the next rung.

Run (from validation/, the a1 venv):
  SHRD_STAGE=source python a1_shroud_twin.py
  SHRD_STAGE=geno [MGDL_GENO_RUN=...] [SHRD_K=140 SHRD_N=31] python a1_shroud_twin.py
"""
import json
import os
import sys
import time

import numpy as np
from scipy.optimize import brentq

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import a1_ideal_march_jax as A1                                   # noqa: E402
import jax.numpy as jnp                                           # noqa: E402
from a1_plug_march import plug_march, col_fluxes, wall_push_poly  # noqa: E402
import a1_source_flow_oracle as SO                                # noqa: E402

K_RICH = A1.K_RICH
NPASS = [0, 0]
ART = os.environ.get("SHRD_ART", os.path.join(HERE, "_shroud_twin"))
os.makedirs(ART, exist_ok=True)
GENO_RUN = os.environ.get("MGDL_GENO_RUN",
                          "/data10/falco/RDE/codes/GENO/CASES/migdalnoz_ni50")
# Migdal's gas (thermo_air14: gamma 1.4, M 28.97). GENO's stagnation state is
# p0 1e5 Pa (IO_m reads ps in bar), T0 300 K (read back from the field: T =
# 206.90 K at M 1.5 = 300 / 1.45) -- OUTSIDE the program's tables (T 1050-3900 K,
# a1_ideal_march_jax.T_TAB_LO/HI: a cold-flow case clamps to 1050 K, measured).
# For a calorically perfect gas the Mach field, p/p0 and the thrust coefficient
# do not depend on T0 and p0, so the twin is posed at T0 3800 K (T_e = T0 /
# (1 + 0.2 M_e^2) = 1083 K stays inside the table) and compares dimensionless
# numbers only. cls SPEC (the reference run's inputs) / NUMERIC (the posing T0)
CASES = {k: v["value"] for k, v in json.load(
    open(os.path.join(HERE, "shroud_twin_cases.json"))).items() if k[0] != "_"}
GAS, CH, GN, SV = CASES["gas"], CASES["channel"], CASES["geno"], CASES["solver"]
GAMMA, MOLAR_MASS, R_UNIV = GAS["gamma"], GAS["molar_mass"], GAS["R_univ"]
P0, T0 = GAS["p0"], GAS["T0_posed"]
M_INLET = GAS["M_inlet"]
PHI_TOP = np.radians(CH["phi_top_deg"])   # the top ray of the exact channel (bottom = SO.PHI_W, 12 deg)
X_LIP_FRAC = CH["lip_frac"]               # the shroud lip at this fraction of the marched length


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


def q_of_mach(M, ta, as_):
    return brentq(lambda q: float(A1.state_q(jnp.float64(q), ta)[5]) - M,
                  SV["q_lo"] * as_, SV["q_hi"] * as_, xtol=SV["xtol"])


# ======================================================================
# stage source: the exact two-ray channel
# ======================================================================
def channel(K, N, tab, ta, as_, bad_top=0.0, free_jet=False):
    """Diverging source flow between the rays PHI_W (plug) and PHI_TOP (shroud):
    start = the exact states on the vertical cut X0; plug stations to X_END;
    shroud stations to the lip at X_LIP_FRAC of the length."""
    R = SO.Radial(ta, as_, False)
    X0, XE = SO.X0, SO.X_END
    yw0 = R.wall_y(X0)
    yt0 = abs(X0 - R.xc) * np.tan(PHI_TOP)
    yline = np.linspace(yw0, yt0, N)
    us, vs = [], []
    for y in yline:
        q, th = R.state(X0, y)
        us.append(q * np.cos(th)); vs.append(q * np.sin(th))
    start = (X0, yline, np.array(us), np.array(vs))
    sx = np.linspace(X0, XE, K)[1:]
    sy = np.array([R.wall_y(x) for x in sx])
    st = (jnp.array(sx), jnp.array(sy), jnp.array(np.gradient(sy, sx)))
    xF = X0 + X_LIP_FRAC * (XE - X0)
    xs = np.linspace(X0, xF, max(CH["min_shroud_stations"], int(K * CH["shroud_stations_frac"])))
    ys = np.abs(xs - R.xc) * np.tan(PHI_TOP)
    if bad_top:
        t = (xs - X0) / (xF - X0)
        ys = ys * (1.0 + bad_top * t * t)
    ss = np.gradient(ys, xs)
    ss[0] = np.tan(PHI_TOP) if not bad_top else ss[0]
    q_t, _ = R.state(X0, yt0)
    qpa = q_t
    if free_jet:
        out, _ = plug_march(st, start, qpa, tab, 1.0)
    else:
        qm, thm = R.state(X0, 0.5 * (yw0 + yt0))
        Mm = float(A1.state_q(jnp.float64(qm), ta)[5])
        dy_launch = GN["wedge_rows_per_station"] * (sx[1] - sx[0]) * (np.tan(thm + np.arcsin(1.0 / Mm)) - np.tan(PHI_TOP))
        m_w = max(1, int(round(dy_launch / (yline[1] - yline[0]))))
        out, _ = plug_march(st, start, qpa, tab, 1.0, shroud=(xs, ys, ss), wedge_every=m_w)
        out["wedge_every"] = m_w
    return R, out, xF


def exact_errs(R, out, ta, x_min=None):
    """(shroud pressure rel error per point, q rel error + theta abs error on the
    mesh points with x > x_min, the lip's (q, theta) errors)."""
    sh = np.asarray(out["shroud"])
    q = np.hypot(sh[:, 2], sh[:, 3])
    p = np.array(A1.state_q(jnp.array(q), ta)[1])
    pex = np.array([float(A1.state_q(jnp.float64(R.state(x, y)[0]), ta)[1]) for x, y in sh[:, :2]])
    e_sh = np.abs(p - pex) / pex
    mp = np.asarray(out["mesh_pts"])
    if x_min is not None:
        mp = mp[mp[:, 0] > x_min]
    qm = np.hypot(mp[:, 2], mp[:, 3]); thm = np.arctan2(mp[:, 3], mp[:, 2])
    qe = np.empty(len(mp)); the = np.empty(len(mp))
    for n, (x, y) in enumerate(mp[:, :2]):
        qe[n], the[n] = R.state(x, y)
    F = sh[-1]
    qF, thF = R.state(float(F[0]), float(F[1]))
    e_lip = (abs(np.hypot(F[2], F[3]) - qF) / qF, abs(np.arctan2(F[3], F[2]) - thF))
    return e_sh, np.abs(qm - qe) / qe, np.abs(thm - the), e_lip, sh[:, 0]


def source():
    t0 = time.time()
    say("== [F3] the shrouded plug: the exact two-ray channel [X-TWMU] (stage source) ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    as_ = tab["_as"]
    say("   source flow pinned to M %.1f at r %.1f; plug ray %.0f deg, shroud ray %.0f deg, lip at"
        " %.0f percent of the length" % (SO.M_REF, SO.R_REF, np.degrees(SO.PHI_W), np.degrees(PHI_TOP),
                                          100 * X_LIP_FRAC))
    (Kc, Nc), (Kf, Nf) = CH["grids"]
    Rc, oc, xF = channel(Kc, Nc, tab, ta, as_)
    Rf, of, _ = channel(Kf, Nf, tab, ta, as_)
    say("   coarse (%d,%d): cert %.3e, %d shroud points, lip at column %s; fine (%d,%d): cert %.3e,"
        " %d shroud points, lip at column %s; %.1f s"
        % (Kc, Nc, float(oc["cert_worst"]), len(oc["shroud"]), oc["lip_col"], Kf, Nf, float(of["cert_worst"]),
           len(of["shroud"]), of["lip_col"], time.time() - t0))
    check("TW-1 every cell certified on both grids (%.3e, %.3e)" % (float(oc["cert_worst"]), float(of["cert_worst"])),
          float(oc["cert_worst"]) <= 1.0 and float(of["cert_worst"]) <= 1.0)
    esc, eqc, etc, elc, xc_ = exact_errs(Rc, oc, ta, xF)
    esf, eqf, etf, elf, xf_ = exact_errs(Rf, of, ta, xF)
    # per-station Richardson band on the shroud pressure: the coarse error read
    # at the fine stations, the band K_RICH x |coarse - fine| + the fine error's
    # own level is NOT used (that would be circular): band = K_RICH x |e_c - e_f|
    esc_f = np.interp(xf_, xc_, esc)
    band_sh = K_RICH * np.abs(esc_f - esf)
    frac = float(np.mean(esf <= np.maximum(band_sh, SV["floor"])))
    say("   shroud pressure: fine max rel err %.2e (mean %.2e), coarse %.2e; inside its Richardson"
        " band at %.0f percent of the stations" % (esf.max(), esf.mean(), esc.max(), 100 * frac))
    check("TW-2 shroud wall pressure vs the closed form inside the band at >= 90 percent of the"
          " stations (%.0f percent; fine max %.2e)" % (100 * frac, esf.max()),
          frac >= GN["band_frac"] and esf.max() < esc.max())
    bq = K_RICH * abs(eqc.max() - eqf.max()); bt = K_RICH * abs(etc.max() - etf.max())
    say("   field downstream of the lip (x > %.3f): fine |dq|/q max %.2e (coarse %.2e), |dtheta| max"
        " %.2e rad (coarse %.2e); %d / %d points" % (xF, eqf.max(), eqc.max(), etf.max(), etc.max(),
                                                      len(eqf), len(eqc)))
    check("TW-3 the field on and below F's C- vs the closed form: fine errors below the coarse"
          " ones and inside K_RICH x the move (q %.2e <= %.2e, theta %.2e <= %.2e)"
          % (eqf.max(), bq, etf.max(), bt), eqf.max() <= bq and etf.max() <= bt)
    check("TW-4 the lip F: |dq|/q %.2e, |dtheta| %.2e rad (fine) below the coarse %.2e / %.2e"
          % (elf[0], elf[1], elc[0], elc[1]), elf[0] <= max(elc[0], SV["floor"]) and elf[1] <= max(elc[1], SV["floor"]))
    # TW-5: the record path -- the same channel with the free jet on top, wall
    # array against the pre-brick record (a1_source_flow_oracle's own posing is
    # different; the regression of record is the oracle 6/6 and the (K,N) walls
    # here, compared with the values saved by this stage's first run)
    _, ofj, _ = channel(Kc, Nc, tab, ta, as_, free_jet=True)
    wfj = np.asarray(ofj["wall"])
    ref = os.path.join(ART, "source_freejet_wall_%d_%d.npy" % (Kc, Nc))
    if os.path.exists(ref):
        same = bool(np.array_equal(np.load(ref), wfj))
        check("TW-5 the free-jet march of the same channel is bit-identical to the record of this"
              " stage's first run (%s)" % ref, same)
    else:
        np.save(ref, wfj)
        say("   TW-5: record of the free-jet wall array written (%s); the check runs from the next run" % ref)
    # R-1: a curved shroud
    Rb, ob, _ = channel(Kf, Nf, tab, ta, as_, bad_top=CH["bad_top"])
    esb, _, _, _, xb_ = exact_errs(Rb, ob, ta, xF)
    say("   rejector (shroud curved by %.0f percent at the lip): cert %.3e, shroud pressure max rel"
        " err %.2e against the clean fine %.2e" % (100 * CH["bad_top"], float(ob["cert_worst"]), esb.max(), esf.max()))
    check("R-1 rejector: the curved shroud leaves the TW-2 band (%.2e > %.0f x %.2e)"
          % (esb.max(), GN["rejector_factor"], esf.max()), esb.max() > GN["rejector_factor"] * esf.max())
    json.dump(dict(K=(Kc, Kf), N=(Nc, Nf), xF=xF, cert=[float(oc["cert_worst"]), float(of["cert_worst"])],
                   e_sh_fine_max=float(esf.max()), e_sh_coarse_max=float(esc.max()), frac_in_band=frac,
                   eq=[float(eqc.max()), float(eqf.max())], eth=[float(etc.max()), float(etf.max())],
                   lip=[list(map(float, elc)), list(map(float, elf))], rej_e_sh=float(esb.max()),
                   seconds=time.time() - t0),
              open(os.path.join(ART, "source.json"), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


# ======================================================================
# stage geno: Migdal's perfect annular nozzle from GENO
# ======================================================================
def geno_walls(run):
    """(plug, shroud) dense walls (x, y) of a GENO nozzle_type-9 run."""
    plug = np.loadtxt(os.path.join(run, "profile_cp.dat"))
    shroud = np.loadtxt(os.path.join(run, "profile_cm.dat"))
    for w in (plug, shroud):
        if np.any(np.diff(w[:, 0]) <= 0.0):
            keep = np.r_[True, np.diff(w[:, 0]) > 0.0]
            w[:] = w[:]           # no-op; duplicates are handled below
    return plug, shroud


def dedup(w):
    keep = np.r_[True, np.diff(w[:, 0]) > 0.0]
    return w[keep]


def stations_from(w, K, x_end=None):
    """K stations on a dense wall (x, y), distributed by the measure
    dx + lambda |dtheta| with lambda = L / (2 theta_tot): the wall's turning
    (the expansion arcs at the start, where the gradients are strongest) gets
    a third of the stations whatever its length; y and slope by the dense
    polyline's own gradient (the wall as GENO drew it). Uniform in x when the
    wall does not turn."""
    w = dedup(w)
    sl_dense = np.gradient(w[:, 1], w[:, 0])
    th = np.arctan(sl_dense)
    L = w[-1, 0] - w[0, 0]
    th_tot = float(np.sum(np.abs(np.diff(th))))
    mu = np.r_[0.0, np.cumsum(np.diff(w[:, 0]) + (L / (2.0 * th_tot) if th_tot > 0 else 0.0) * np.abs(np.diff(th)))]
    xq = np.interp(np.linspace(0.0, mu[-1], K + 1)[1:], mu, w[:, 0])
    return xq, np.interp(xq, w[:, 0], w[:, 1]), np.interp(xq, w[:, 0], sl_dense)


def one_d(eps_i, Mi, g):
    """1-D: exit Mach and vacuum thrust coefficient F/(p0 A*) for A_e/A_i = eps_i
    at inlet Mach Mi; F_in/(p0 A*) of the axial inlet as well."""
    AA = lambda M: (1.0 / M) * ((2.0 / (g + 1.0)) * (1.0 + 0.5 * (g - 1.0) * M * M)) ** ((g + 1.0) / (2.0 * (g - 1.0)))
    Ae = eps_i * AA(Mi)
    Me = brentq(lambda M: AA(M) - Ae, Mi, SV["M_hi"], xtol=SV["xtol_M"])
    def cf(M, A):
        pr = (1.0 + 0.5 * (g - 1.0) * M * M) ** (-g / (g - 1.0))
        return g * np.sqrt(2.0 / (g - 1.0) * (2.0 / (g + 1.0)) ** ((g + 1.0) / (g - 1.0))
                           * (1.0 - pr ** ((g - 1.0) / g))) + pr * A
    return Me, cf(Me, Ae), cf(Mi, AA(Mi)), AA(Mi)


def march_geno(K, N, tab, ta, as_, plug, shroud, lift=0.0):
    """GENO's uniform start + GENO's walls through our march; returns out, the
    start column, the stations."""
    y_l, y_u = float(plug[0, 1]), float(shroud[0, 1])
    q_i = q_of_mach(M_INLET, ta, as_)
    yline = np.linspace(y_l, y_u, N)
    start = (float(plug[0, 0]), yline, np.full(N, q_i), np.zeros(N))
    sx, sy, sl = stations_from(plug, K)
    xs, ys, ss = stations_from(shroud, max(8, int(K * (shroud[-1, 0] - shroud[0, 0]) / (plug[-1, 0] - plug[0, 0]))))
    xs = np.r_[plug[0, 0], xs]; ys = np.r_[y_u, ys]; ss = np.r_[0.0, ss]
    if lift:
        # the rejector: the shroud lifted by `lift`, ramped from the start (no corner at x = 0)
        t = (xs - xs[0]) / (xs[-1] - xs[0])
        ys = ys * (1.0 + lift * t)
        ss = np.gradient(ys, xs)
    # the wedge thinned to the plug stations' density: a C+ from the start
    # line at Mach M_i rises at mu = asin(1/M_i) (theta 0), so start rows
    # dy_row apart land on the shroud dx = dy_row / tan(mu) apart; launch
    # every m-th row so that dx matches the station spacing
    dy_row = (y_u - y_l) / (N - 1)
    dx_st = float(sx[0] - plug[0, 0])           # the FIRST station spacing: the wedge's neighbourhood
    dy_launch = GN["wedge_rows_per_station"] * dx_st * np.tan(np.arcsin(1.0 / M_INLET))
    m_w = max(1, int(round(dy_launch / dy_row)))
    out, _ = plug_march((jnp.array(sx), jnp.array(sy), jnp.array(sl)), start, q_i, tab, 1.0,
                        shroud=(xs, ys, ss), wedge_every=m_w)
    col0 = np.stack([np.full(N, float(plug[0, 0])), yline, np.full(N, q_i), np.zeros(N)], 1)
    out["wedge_every"] = m_w
    return out, col0, (sx, sy, sl), (xs, ys, ss)


def exit_readings(out, ta):
    """(M, theta) on F's C- (the top row after the lip) and on the last column."""
    mp = np.asarray(out["mesh_pts"]); keys = out["mesh_keys"]
    lip_col = out["lip_col"]
    rows = {}
    for k, ptv in zip(keys, mp):
        rows[k] = ptv
    # the top row after the lip: for each column i > lip_col the point with the max row index
    top = []
    for k in keys:
        j, i = k
        if lip_col is not None and i >= lip_col:
            if (j + 1, i) not in rows:
                top.append(rows[k])
    top = np.array(top)
    last_i = max(i for _, i in keys)
    last = np.array([rows[(j, last_i)] for j in range(1, 1 + sum(1 for (j, i) in keys if i == last_i))])
    def MT(a):
        q = np.hypot(a[:, 2], a[:, 3])
        return np.array(A1.state_q(jnp.array(q), ta)[5]), np.arctan2(a[:, 3], a[:, 2])
    return top, last, MT(top), MT(last)


def geno_field(run):
    """GENO's field as a point cloud (x, y, u, v, p): the type-9 binary streams
    (both families, the padding rows of zero velocity dropped) -- read for the
    wall pressures only, by nearest point (the wall nodes ARE field points:
    measured distance 1e-11)."""
    pts = []
    for side in ("cp", "cm"):
        cols = [np.fromfile(os.path.join(run, "%s_%s.dat" % (nm, side)), dtype="<f8") for nm in ("x", "y", "u", "v", "p")]
        m = cols[2] > 1.0
        pts.append(np.stack([c[m] for c in cols], 1))
    return np.vstack(pts)


def wall_p_vs_geno(out, ta, field, n):
    """(x, p/p0 ours, p/p0 GENO) at n samples along the plug and the shroud."""
    from scipy.spatial import cKDTree
    tree = cKDTree(field[:, :2])
    rows = {}
    for key in ("wall", "shroud"):
        w = np.asarray(out[key]); w = w[np.linspace(0, len(w) - 1, min(n, len(w))).astype(int)]
        q = np.hypot(w[:, 2], w[:, 3])
        p_ours = np.array(A1.state_q(jnp.array(q), ta)[1]) / P0
        d, idx = tree.query(w[:, :2])
        p_geno = field[idx, 4] / GAS["p0"]
        rows[key] = (w[:, 0], p_ours, p_geno, d)
    return rows


def geno():
    t0 = time.time()
    say("== [F3] the shrouded plug: Migdal's perfect annular nozzle from GENO [X-MGDL] (stage geno) ==")
    Rg = R_UNIV / MOLAR_MASS
    tab = A1.prep_tab(A1.build_tab_gconst(g=GAMMA, Rg=Rg, ts=T0, ps=P0))
    ta = A1.tab_arrays(tab)
    as_ = tab["_as"]
    plug, shroud = geno_walls(GENO_RUN)
    plug, shroud = dedup(plug), dedup(shroud)
    y_l, y_u = float(plug[0, 1]), float(shroud[0, 1])
    A_i = np.pi * (y_u ** 2 - y_l ** 2)
    eps_i = (shroud[-1, 1] ** 2 - plug[-1, 1] ** 2) / (y_u ** 2 - y_l ** 2)
    Me, CF, CF_in, AAi = one_d(eps_i, M_INLET, GAMMA)
    A_star = A_i / AAi
    say("   run %s: plug %d pts to (%.4f, %.4f), shroud %d pts to F (%.4f, %.4f); A_e/A_i %.4f ->"
        " 1-D M_e %.6f, C_F,vac %.5f (inlet %.5f), A* %.5f m^2; gas gamma %.2f R %.2f, posed at p0 %.3g T0 %.0f"
        " (dimensionless readings; GENO's T0 300 K is below the tables)"
        % (GENO_RUN, len(plug), plug[-1, 0], plug[-1, 1], len(shroud), shroud[-1, 0], shroud[-1, 1],
           eps_i, Me, CF, CF_in, A_star, GAMMA, Rg, P0, T0))
    K = int(os.environ.get("SHRD_K", GN["K"])); N = int(os.environ.get("SHRD_N", GN["N"]))
    res = {}
    for tag, (Kk, Nn) in (("coarse", (K // 2, (N + 1) // 2)), ("fine", (K, N))):
        t1 = time.time()
        out, col0, st, sh = march_geno(Kk, Nn, tab, ta, as_, plug, shroud)
        top, last, (Mt, tht), (Ml, thl) = exit_readings(out, ta)
        F_in = col_fluxes(col0, ta, 0.0, 1.0)
        push_p = -wall_push_poly(out["wall"], ta, 0.0, 1.0)          # plug: dy < 0, forward
        push_s = wall_push_poly(out["shroud"], ta, 0.0, 1.0)         # shroud: dy > 0, forward
        J = (F_in[1] + push_p + push_s) / (P0 * A_star)
        # the exit polyline: the last column (plug tip -> up to F's C-), then F's C- back to F
        poly = np.vstack([last, top[np.argsort(-top[:, 0])]]) if len(top) else last
        m_out, F_out = col_fluxes(poly, ta, 0.0, 1.0)
        res[tag] = dict(K=Kk, N=Nn, cert=float(out["cert_worst"]), lip_col=out["lip_col"],
                        n_top=len(top), n_last=len(last),
                        Mtop=[float(Mt.min()), float(Mt.max())], thtop=float(np.max(np.abs(tht))),
                        Mlast=[float(Ml.min()), float(Ml.max())], thlast=float(np.max(np.abs(thl))),
                        F_in=F_in[1] / (P0 * A_star), push_p=push_p / (P0 * A_star), push_s=push_s / (P0 * A_star),
                        CF=J, CF_exit=F_out / (P0 * A_star), m_in=F_in[0], m_out=m_out, seconds=time.time() - t1)
        say("   %s (%d,%d): cert %.3e; wedge every %d rows; lip at column %s; F's C- %d pts M %.5f..%.5f |theta| <= %.2e;"
            " last column %d pts M %.5f..%.5f |theta| <= %.2e; F_in %.5f + plug %.5f + shroud %.5f ="
            " C_F %.5f (exit flux %.5f; 1-D %.5f); mass in %.4f out %.4f (%.2e); %.0f s"
            % (tag, Kk, Nn, res[tag]["cert"], out["wedge_every"], out["lip_col"], len(top), Mt.min(), Mt.max(), res[tag]["thtop"],
               len(last), Ml.min(), Ml.max(), res[tag]["thlast"], res[tag]["F_in"], res[tag]["push_p"],
               res[tag]["push_s"], J, res[tag]["CF_exit"], CF, F_in[0], m_out, m_out / F_in[0] - 1.0,
               time.time() - t1))
    c, f = res["coarse"], res["fine"]
    # MG-6: the wall pressures against GENO's field, p/p0 (the reference's own
    # discretisation error is part of what is read: reported, graded on our
    # Richardson band of the same reading)
    field = geno_field(GENO_RUN)
    wp = {}
    for tag, (Kk, Nn) in (("coarse", (K // 2, (N + 1) // 2)), ("fine", (K, N))):
        o_, _, _, _ = march_geno(Kk, Nn, tab, ta, as_, plug, shroud)
        wp[tag] = wall_p_vs_geno(o_, ta, field, GN["wall_samples"])
    dev = {}
    for key in ("wall", "shroud"):
        xf_, pf_, pg_, df_ = wp["fine"][key]; xc_, pc_, pgc_, _ = wp["coarse"][key]
        e_f = np.abs(pf_ - pg_) / pg_; e_c = np.abs(np.interp(xf_, xc_, pc_) - pg_) / pg_
        dev[key] = (float(e_f.max()), float(e_f.mean()), float(e_c.max()), float(df_.max()))
        say("   %s p/p0 vs GENO (%d samples, nearest field point <= %.1e): fine |dp|/p max %.2e mean %.2e,"
            " coarse max %.2e" % ("plug" if key == "wall" else "shroud", len(xf_), df_.max(), e_f.max(), e_f.mean(), e_c.max()))
    res["wall_p"] = dev
    check("MG-1 every cell certified (coarse %.3e, fine %.3e)" % (c["cert"], f["cert"]),
          c["cert"] <= 1.0 and f["cert"] <= 1.0)
    dM_c = max(abs(c["Mtop"][0] - Me), abs(c["Mtop"][1] - Me)); dM_f = max(abs(f["Mtop"][0] - Me), abs(f["Mtop"][1] - Me))
    band_M = K_RICH * abs(dM_c - dM_f) + GN["ref_class"]["M"]
    band_t = K_RICH * abs(c["thtop"] - f["thtop"]) + GN["ref_class"]["theta"]
    check("MG-2 F's C- uniform at the 1-D exit: |M - M_e| %.2e <= band %.2e, |theta| %.2e <= %.2e"
          % (dM_f, band_M, f["thtop"], band_t), dM_f <= band_M and f["thtop"] <= band_t)
    dMl_c = max(abs(c["Mlast"][0] - Me), abs(c["Mlast"][1] - Me)); dMl_f = max(abs(f["Mlast"][0] - Me), abs(f["Mlast"][1] - Me))
    band_Ml = K_RICH * abs(dMl_c - dMl_f) + GN["ref_class"]["M"]
    band_tl = K_RICH * abs(c["thlast"] - f["thlast"]) + GN["ref_class"]["theta"]
    check("MG-3 the last column uniform likewise: |M - M_e| %.2e <= %.2e, |theta| %.2e <= %.2e"
          % (dMl_f, band_Ml, f["thlast"], band_tl), dMl_f <= band_Ml and f["thlast"] <= band_tl)
    band_J = K_RICH * abs(c["CF"] - f["CF"])
    check("MG-4 thrust closure: C_F %.5f vs 1-D %.5f (|d| %.2e <= band %.2e); exit flux %.5f"
          % (f["CF"], CF, abs(f["CF"] - CF), band_J, f["CF_exit"]), abs(f["CF"] - CF) <= band_J)
    dm_c, dm_f = abs(c["m_out"] / c["m_in"] - 1.0), abs(f["m_out"] / f["m_in"] - 1.0)
    check("MG-5 mass through the exit polyline = start flux (%.2e <= band %.2e)"
          % (dm_f, K_RICH * abs(dm_c - dm_f)), dm_f <= K_RICH * abs(dm_c - dm_f))
    band_w = {k: K_RICH * abs(dev[k][2] - dev[k][0]) for k in dev}
    check("MG-6 wall p/p0 vs GENO's field inside our Richardson band: plug %.2e <= %.2e, shroud %.2e <= %.2e"
          % (dev["wall"][0], band_w["wall"], dev["shroud"][0], band_w["shroud"]),
          dev["wall"][0] <= band_w["wall"] and dev["shroud"][0] <= band_w["shroud"])
    J_bad = f["F_in"] + f["push_p"] - f["push_s"]
    check("R-2 rejector: the shroud term with the plug's sign misses the 1-D value (|d| %.2e > band %.2e)"
          % (abs(J_bad - CF), band_J), abs(J_bad - CF) > band_J)
    t1 = time.time()
    outb, _, _, _ = march_geno(K, N, tab, ta, as_, plug, shroud, lift=GN["lift"])
    _, _, (Mtb, thtb), _ = exit_readings(outb, ta)
    dMb = max(abs(Mtb.min() - Me), abs(Mtb.max() - Me))
    say("   rejector (shroud lifted %.0f percent): cert %.3e, |M - M_e| on F's C- %.2e, |theta| %.2e (%.0f s)"
        % (100 * GN["lift"], float(outb["cert_worst"]), dMb, np.max(np.abs(thtb)), time.time() - t1))
    check("R-3 rejector: the lifted shroud leaves the MG-2 band (%.2e > %.2e)" % (dMb, band_M), dMb > band_M)
    json.dump(dict(run=GENO_RUN, eps_i=eps_i, Me_1d=Me, CF_1d=CF, CF_in_1d=CF_in, A_star=A_star,
                   res=res, rej_lift=dict(dM=dMb, cert=float(outb["cert_worst"])), seconds=time.time() - t0),
              open(os.path.join(ART, "geno_%s.json" % os.path.basename(GENO_RUN.rstrip("/"))), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t0))
    return NPASS[0] == NPASS[1]


if __name__ == "__main__":
    stage = os.environ.get("SHRD_STAGE", "source")
    ok = {"source": source, "geno": geno}[stage]()
    sys.exit(0 if ok else 1)

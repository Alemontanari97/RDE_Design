"""Humphreys, Thompson & Hoffman 1971 (AIAA J 9(8):1581-1587) marched
by our engine [F3/A1]: the optimisation twin on the plug line.

THE POSING (p. 1586, read from the paper 2026-09-18): p_c 500 psia,
T_c 6000 R, gas constant 56 ft-lbf/(lbm-R), gamma 1.23, mdot 148.08
lbm/s, p_a 14.7 psia (PR 34.0), plug length T -> D 12.0 in, wall shear
by C_f 0.002 (small: ~0.2 percent of thrust, NOT in our inviscid J),
base pressure by their Eq. (12) = Vander Veen's 0.846 p/M^1.3 (our
member 'veen'), start line Moore-Hall. Two results of record:
  (A) RAO'S METHOD at the same mass, length, ambient, gas and base
      model: cowl lip 8.33 in, injection -58.5 deg, thrust 34,253 lbf,
      contour in their Table 3 (last point x 11.51781, y 1.37506 in,
      slope -13.25 deg);
  (B) THEIR PARAMETRIC OPTIMUM for fixed inlet geometry: lip 7.55 in,
      injection -34 deg, thrust 32,881 lbf, contour in Table 2 (foot
      (-0.56069, 6.71874) in at -36.25 deg, D at (11.51707, 0.95441)
      at -13.26 deg). Their Table 1: 20 runs on the (angle, lip) grid,
      thrust 32,699..32,877 lbf -- the whole grid within 0.5 percent.

STAGE rao (A): our axisymmetric ideal member [X-AFAN] at their lip and
PR, in our gas tables (gconst, gamma 1.23), truncated at their x_D, the
base priced with their own closure. No march is needed for the thrust
of an ideal member: by construction it exhausts the whole mass at
(q_e, theta_E = 0, p_a), so F_full = mdot q_e exactly, and the
truncated member is F(D) = F_full - push(D -> tip) + (p_b - p_a) pi
y_D^2, the wall push read on the fan's own wall states. What the row
reads: (R-1) the member's mass against their 148.08 lbm/s -- Rao's lip
is the mass-consistent lip of the ideal member, or it is not; (R-2)
the thrust against 34,253 lbf; (R-3) y_D against Table 3.

STAGE opt (B): the record's TR-SQP (a1_plug_spline_opt) at their
posing -- their lip, their injection angle (the planar corner fan at
the lip posed with theta_E = theta_i + nu(M_e), which is +22.9 deg:
the jet boundary flares outward, the plug is short), their length,
their base model -- against 32,881 lbf and Table 2. Launched on s2 in
the background; hours. HMPH_PERTURB/HMPH_SEED perturb the start's
knots (gate P-1, the return); HMPH_FAN=axi poses the Rao case from the
ideal member (gate P-2).

STAGE grad (S32, 2026-09-22): the gradient AT the optimum, no walk --
the walk being the instrument under test, it cannot grade itself. Three
designs are differentiated on the same posing (their table, our
table-start landing, the perturbed landing) and the readings are
single-point: G-1 the reverse-AD gradient against central differences
on the FD ladder, G-2/G-3 what a move of the measured stay class
(0.15 in) of each knot buys, G-4 the tip residue the perturbed walk
left, G-5 the same prices under (K,N) -> (2K-1,2N-1). Every price is
graded against the band the march supports ON A MOVE -- the amount by
which the refinement moves the DIFFERENCE between two designs -- and
NOT against the band on the value: the discretisation error is common
to designs of the same family on the same grid, and the value's band
(2.9e-2 of J at (81,41)) is five times the span of the paper's own
20-run grid, so a first-order price graded against it would be
measuring the grid. Run of record on the ladder's two rungs
(PSPL_K/PSPL_N): see the S32 log section 15.

STAGE class (S32, 2026-09-22): is the march of each design IN CLASS?
The Newton certification is blind to a folded net (S29, [X-PMRG] /
[X-PGRS]), and the legs of this row ran the driver WITHOUT the margin,
so the class of every design the thrust rows rest on is an open
question -- including the paper's own contour as WE march it. The
census is the margin carrier's own, the incumbent (the fan's own
streamline) is the control, and the gates also SPLIT this row's two
certification failures, which are not the same mechanism.

STAGE throat (S32, 2026-09-22): THEIR throat from their own table and
text -- the prescribed 0.5-in arc from A to T (known answers: the arc
radius, T -> D = 12.0 in), the start line A -> E normal to the injection,
the throat's Dutton R_c from the paper's OWN mean radius of curvature
(0.705 in: R_c 0.703, corrected from the first S32 reading that had
used the downstream arc), the series kernel's convergence measured AT
that throat, and their stated mass against the choked 1-D mass of the
line A -> E.

STAGE kernel (S32, 2026-09-22 night): the march from THEIR throat on
THEIR geometry -- the annular kernel's line, the lip corner fan through
its field, the rotated-frame cells, the wall = their prescribed arc then
Table 2 -- read as SPECIFIC thrust. Gates H-0..H-6. RESULT OF RECORD: the
pipeline runs (fan and march certified, start line space-like, y_D
theirs, a physical discharge 0.97-0.98 of the choked 1-D against their
1.029) but the three-term series at R_c 0.703 is REJECTED by the march at
its first column (-5.7..-7.4 percent of the mass, then a drift), and the
A/B (HMPH_WALL=parabola, HMPH_RCSCALE) attributes it to the series'
truncation: the same pipeline on the kernel's own wall at R_c 4.0 steps
-1.2 percent and holds. Not the wedge (HMPH_NEDGE), not the fan
(HMPH_NRAYS), not the wall mismatch, not the cut (HMPH_ZCUT), not the
rows (HMPH_N). The transonic region of this throat must be solved
numerically; the series is its upstream condition, not its start line.

Lengths are posed in LIP RADII (the record's YTIP convention, the
Chutkey twin's frame); the paper's inches are converted at the edges.
"""
import os
import sys
import json
import glob
import time

import numpy as np
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                            # noqa: E402
import base_pressure as BP                                 # noqa: E402

ART = os.environ.get("HMPH_ART", os.path.join(HERE, "_humphreys_twin"))
NPASS = [0, 0]

# ---- the paper's posing, in SI ----------------------------------------
IN = 0.0254
LBF = 4.4482216
PSI = 6894.757
P0 = 500.0 * PSI                       # chamber pressure [Pa]
T0 = 6000.0 / 1.8                      # chamber temperature [K]
RG = 56.0 * 5.380320                   # ft-lbf/(lbm-R) -> J/(kg K)
GAMMA = 1.23
LBM = 0.45359237                       # [kg]
MDOT = 148.08 * LBM                    # [kg/s]
PA = 14.7 * PSI                        # ambient [Pa]
X_D = 11.51781 * IN                    # Table 3: Rao's D abscissa from the lip
Y_D_RAO = 1.37506 * IN                 # Table 3: Rao's base radius
F_RAO = 34253.0 * LBF                  # Rao's thrust [N]
R_RAO = 8.33 * IN                      # Rao's cowl lip radius
R_OPT = 7.55 * IN                      # their optimum's lip radius
TH_I_OPT = -34.0                       # their optimum's injection angle [deg]
F_OPT = 32881.0 * LBF
L_TD = 12.0 * IN                       # length T -> D
M_I_FAN = 1.6                          # fan_axi's leading ray (Chutkey twin)
THRUST_TOL = 1e-2                      # the thrust rows' class (their shear is 0.2 percent)


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


def n_turns(ang):
    """Turns of a sampled wall angle: the sign changes of its increments,
    exact zeros (a straight piece) skipped -- stage class K-10's count on
    every design without a straight piece."""
    s = np.sign(np.diff(np.asarray(ang, float)))
    s = s[s != 0.0]
    return int((np.diff(s) != 0.0).sum())


def build_world(R_lip):
    """gconst tables at their (gamma, R, T_c, p_c); lengths in lip radii."""
    tab = A1.prep_tab(A1.build_tab_gconst(g=GAMMA, Rg=RG, ts=T0, ps=P0))
    ta = A1.tab_arrays(tab)
    S = 1.0 / R_lip
    return dict(tab=tab, ta=ta, as_=tab["_as"], P0=P0, T0=T0, RMAX=1.0,
                S=S, PR=P0 / PA, mdot=MDOT * S * S)


def fan_axi_lip(w, n_rays=121, n_lev=121):
    import a1_inlet_angle_opt as IA
    import a1_axi_fan as AF
    IA.MI, IA.PA = M_I_FAN, PA
    AF._CACHE.clear()
    return AF.fan_axi(w, 0.0, n_rays=n_rays, n_lev=n_lev, verbose=False)


# ----------------------------------------------------------------------
# stage rao
# ----------------------------------------------------------------------
def rao():
    t00 = time.time()
    say("== [F3] Humphreys 1971, twin (A): Rao's member at their posing"
        " [X-HMPH] (stage rao) ==")
    w = build_world(R_RAO)
    S = w["S"]
    ta = w["ta"]
    say("   world: gamma %.2f, R %.1f J/kg/K, T_c %.0f K, p_c %.4e Pa,"
        " p_a %.4e Pa (PR %.2f); lip %.2f in; mdot %.3f kg/s"
        % (GAMMA, RG, T0, P0, PA, w["PR"], R_RAO / IN, MDOT))
    from a1_plug_march import col_fluxes
    t0 = time.time()
    fan = fan_axi_lip(w)
    fc = fan["cert"]
    q_e = float(fan["q2"]) if "q2" in fan else None
    pm = fan["pm"]
    q_e = float(pm["qs"][-1])
    T_e, p_e, rho_e, c_e, g_e, M_e = [float(v) for v in
                                       A1.state_q(jnp.float64(q_e), ta)]
    say("   fan_axi (M_i %.2f, %d x %d): cert worst %.3f, %.0f s; M_e %.4f,"
        " q_e %.1f m/s, p_e/p_a %.6f; tip x %.3f in, y_sp0 %.3f in"
        % (M_I_FAN, 121, 121, fc["worst"], time.time() - t0, M_e, q_e,
           p_e / PA, fan["x_tip"] / S / IN, fan["y_sp0"] / S / IN))
    check("R-0 the fan is Newton-certified on every cell the wall depends"
          " on (worst %.3f <= 1)" % fc["worst"], fc["worst"] <= 1.0)
    # ---- R-1: the member's mass vs the paper's -----------------------
    term = np.asarray(fan["rays"][-1])
    md, _ = col_fluxes(term, ta, PA, 1.0)
    md_SI = abs(md) / S / S
    say("   mass through the terminal ray %.3f kg/s = %.2f lbm/s vs the"
        " paper's 148.08 (%+.2e)" % (md_SI, md_SI / 0.45359237,
                                     md_SI / MDOT - 1))
    check("R-1 Rao's cowl lip (8.33 in) is the mass-consistent lip of the"
          " ideal member at this posing: |dm/m| %.2e <= 1e-2 (the tip cut"
          " and the fan's own quadrature)" % abs(md_SI / MDOT - 1),
          abs(md_SI / MDOT - 1) <= THRUST_TOL)
    # ---- the truncated member's thrust --------------------------------
    sx, sy = fan["wall"]
    W = np.array(fan.get("W", None)) if "W" in fan else None
    # the wall states: fan_axi's wall polyline carries (x, y, theta, q)
    # in its own record; recompute q along the wall from the rays'
    # crossings is what it stores -- read it back through fan["wall_q"]
    # if present, else sample the field
    if "wall_q" in fan:
        qw = np.asarray(fan["wall_q"])
    else:
        qw = np.array([fan["field"](float(x), float(y))[0]
                       for x, y in zip(sx, sy)])
    T_w, p_w, rho_w, c_w, g_w, M_w = [np.asarray(v) for v in
                                       A1.state_q(jnp.asarray(qw), ta)]
    xD = X_D * S
    i_D = int(np.searchsorted(sx, xD))
    y_D = float(np.interp(xD, sx, sy))
    p_D = float(np.interp(xD, sx, p_w))
    M_D = float(np.interp(xD, sx, M_w))
    # push from D to the tip (frame units -> SI by 1/S^2)
    xs = np.concatenate([[xD], sx[i_D:]])
    ys = np.concatenate([[y_D], sy[i_D:]])
    ps = np.concatenate([[p_D], p_w[i_D:]])
    dy = np.diff(ys)
    push = float(np.sum((0.5 * (ps[1:] + ps[:-1]) - PA)
                        * 2.0 * np.pi * 0.5 * (ys[1:] + ys[:-1]) * (-dy))) / S / S
    F_full = MDOT * q_e
    pb = float(BP.p_base(p_D, M_D, GAMMA, PA, "veen"))
    base = float(BP.base_term(pb, y_D / S, PA))
    F_D = F_full - push + base
    say("   full ideal member: F = mdot q_e = %.1f kN = %.0f lbf; wall push"
        " beyond D (x %.2f in): %.1f kN; base at D: y_D %.3f in (Table 3:"
        " %.3f), p_D/p_a %.3f, M_D %.3f, Veen p_b/p_a %.3f -> %+.1f kN"
        % (F_full / 1e3, F_full / LBF, X_D / IN, push / 1e3, y_D / S / IN,
           Y_D_RAO / IN, p_D / PA, M_D, pb / PA, base / 1e3))
    say("   TRUNCATED MEMBER AT D: F = %.1f kN = %.0f lbf vs Rao's 34,253"
        " (%+.2e); without the base term %.0f lbf"
        % (F_D / 1e3, F_D / LBF, F_D / F_RAO - 1, (F_full - push) / LBF))
    check("R-2 the ideal member truncated at Rao's D, base priced with"
          " their closure, reproduces Rao's thrust within 1 percent (the"
          " paper's shear model is 0.2 percent, not in ours): %+.2e"
          % (F_D / F_RAO - 1), abs(F_D / F_RAO - 1) <= THRUST_TOL)
    check("R-3 the member's base radius at x_D meets Rao's Table 3 within"
          " 5 percent of y_D (%.3f vs %.3f in, %+.2e)"
          % (y_D / S / IN, Y_D_RAO / IN, y_D / S / Y_D_RAO - 1),
          abs(y_D / S / Y_D_RAO - 1) <= 0.05)

    # ---- R-4 / R-5 (S33): Table 3 against the member, row by row -------
    # S31 read, on a coarse figure, that "Rao's Table 3 lies ON our exact
    # ideal member over its length"; R-3 above already contradicted it at
    # D. The S32 session measured it row by row (2026-09-22) and S33
    # confirms it here: the table complete (the two rows the layout broke
    # recovered), the member's wall angle from its own polyline.
    xm, ym = sx / S / IN, sy / S / IN
    am = np.degrees(np.arctan(np.gradient(ym, xm)))
    T3, T3p = table3_complete(), table3_complete(printed=True)
    inr = (T3[:, 0] >= xm.min()) & (T3[:, 0] <= xm.max())
    dy = T3[inr, 1] - np.interp(T3[inr, 0], xm, ym)
    dth = T3[inr, 2] - np.interp(T3[inr, 0], xm, am)
    dthp = T3p[inr, 2] - np.interp(T3p[inr, 0], xm, am)
    for x_, y_, d_, t_, tp_ in zip(T3[inr, 0], T3[inr, 1], dy, dth, dthp):
        say("   Table 3 at x %8.5f in: y %8.5f, minus the member %+.4f in"
            " (%+.2f %% of y); angle minus the member's wall %+.2f deg%s"
            % (x_, y_, d_, 100.0 * d_ / y_, t_,
               "" if t_ == tp_ else "  (as printed: %+.2f deg)" % tp_))
    check("R-4 Rao's Table 3 does NOT lie on our ideal member: it runs BELOW"
          " it at every row of the member's range, the gap growing"
          " monotonically from %.4f in (x %.2f) to %.4f in at D, %.1f to"
          " %.1f %% of the local radius, their wall angle steeper by"
          " %.2f..%.2f deg -- Rao's length-constrained optimum is not the"
          " ideal member truncated (S31's side finding withdrawn)"
          % (-dy[0], T3[inr, 0][0], -dy[-1], -100.0 * dy[0] / T3[inr, 1][0],
             -100.0 * dy[-1] / T3[inr, 1][-1], -dth.max(), -dth.min()),
          bool(np.all(dy < 0.0) and np.all(np.diff(dy) < 0.0)))
    ty = TABLES["_table3_typo"]
    k = int(np.argmin(np.abs(T3[inr, 0] - ty["x"])))
    nb = dth[[k - 1, k + 1]]
    check("R-5 the printed angle %.5f at x %.5f is a one-digit misprint: the"
          " printed column is not monotone (%s), the corrected %.5f makes it"
          " so (%s) and sits against the member where its neighbours do"
          " (%+.2f vs %+.2f / %+.2f deg; as printed %+.2f)"
          % (ty["printed_deg"], ty["x"],
             "monotone" if np.all(np.diff(T3p[:, 2]) > 0.0) else "broken",
             ty["corrected_deg"],
             "monotone" if np.all(np.diff(T3[:, 2]) > 0.0) else "broken",
             dth[k], nb[0], nb[1], dthp[k]),
          bool(np.all(np.diff(T3[:, 2]) > 0.0)
               and not np.all(np.diff(T3p[:, 2]) > 0.0)
               and nb.min() <= dth[k] <= nb.max()))
    rec = dict(M_e=M_e, q_e=q_e, mdot_member=md_SI, F_full=F_full,
               push_beyond_D=push, y_D_in=y_D / S / IN, p_D_pa=p_D / PA,
               M_D=M_D, pb_pa=pb / PA, base=base, F_D=F_D, F_D_lbf=F_D / LBF,
               F_rao_lbf=34253.0, fan_cert=fc["worst"],
               wall_in=np.c_[sx / S / IN, sy / S / IN, p_w / PA, M_w].tolist(),
               table3_vs_member=np.c_[T3[inr, 0], T3[inr, 1], dy, dth,
                                      dthp].tolist(),
               seconds=time.time() - t00)
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(ART, "rao.json"), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage opt (B): the record's TR-SQP at their posing
# ----------------------------------------------------------------------
# HMPH_CASE = "rao" (lip 8.33 in, injection -58.5 deg ~ our sonic fan
# with theta_E = 0, target 34,253 lbf / Table 3) or "opt" (lip 7.55 in,
# injection -34 deg -> theta_E = -34 + nu(M_e), target 32,881 lbf /
# Table 2). PLANAR fan of record (the axisymmetric one is posed at
# theta_E = 0 only, and the mass must be IMPOSED: the length-
# constrained members pass more mass than the ideal one at their lip,
# see stage rao), the start radius set by the mass at a cut X0 close
# to the lip (0.05 R: the planar strip is declared and short), the
# base priced with their closure, the walk from the fan's own
# streamline. The a1_plug_spline_opt knobs are env-set BEFORE its
# import (its own convention); its ambient and cut constants are
# reposed on this world after.
CASE = os.environ.get("HMPH_CASE", "rao")
X0_R = 0.05
# HMPH_START = "fan" (the planar fan's streamline, the record's start) or
# "table" (the paper's own contour, Table 3 / Table 2, interpolated at the
# knots: the record's O3.3 pattern -- the value at THEIR design, and
# whether the walk stays). Tables in humphreys1971_tables.json.
START = os.environ.get("HMPH_START", "fan")
TABLES = json.load(open(os.path.join(HERE, "humphreys1971_tables.json")))


def read_table(xq, tab, mode=None):
    """THEIR contour at our abscissae, read from their OWN table.

    Their Tables 2 and 3 are SPARSE downstream -- twenty rows, nine of
    them crowded in the first 0.08 in at the foot, then gaps of up to
    2.66 in -- and they print THREE columns: x, y and the wall ANGLE.
    Reading y by straight chords (`np.interp`, the S31 posing) therefore
    puts every knot between two of their points ABOVE their contour,
    which is convex there: measured +0.005 to +0.030 in on the six knots
    of the opt case, a systematic bias in the OBJECTIVE, not in the
    machine. HMPH_TABLE=hermite reads it as the cubic Hermite through
    their (x, y) with THEIR printed angle as the slope -- their own data,
    read as they drew it. Default `chord` keeps every row of record
    bit-identical; `mode` overrides the environment (stage angle reads
    their contour as drawn whatever the leg's setting)."""
    x, y = tab[:, 0], tab[:, 1]
    if (mode or os.environ.get("HMPH_TABLE", "chord")) != "hermite":
        return np.interp(xq, x, y)
    return _hermite(xq, tab)[0]


def table3_complete(printed=False):
    """Rao's Table 3 (p. 1587) in full: the 17 transcribed rows plus the
    two whose columns the PDF layout broke (_table3_recovered_rows), sorted
    in x; unless printed=True, the one-digit misprint of the wall angle at
    x 5.33714 is replaced by its correction (_table3_typo). The record's
    stages keep reading the 17-row transcription (bit-identical); this is
    the table for any reader of the angle column or of the whole contour
    (stage rao R-4/R-5, S33)."""
    t = np.array(TABLES["table3_rao_lip8.33_inj-58.5"], float)
    t = np.vstack([t, np.array(TABLES["_table3_recovered_rows"], float)])
    t = t[np.argsort(t[:, 0])]
    if not printed:
        ty = TABLES["_table3_typo"]
        t[int(np.argmin(np.abs(t[:, 0] - ty["x"]))), 2] = ty["corrected_deg"]
    return t


def _hermite(xq, tab):
    """The cubic Hermite through their (x, y) rows with their printed
    angle as the slope: (y, dy/dx) at xq -- read_table's `hermite`, and
    the contour's DIRECTION as drawn (stage angle)."""
    x, y = tab[:, 0], tab[:, 1]
    m = np.tan(np.radians(tab[:, 2]))
    out = np.empty_like(np.asarray(xq, float))
    der = np.empty_like(out)
    for n, xx in enumerate(np.asarray(xq, float)):
        i = min(max(int(np.searchsorted(x, xx)) - 1, 0), len(x) - 2)
        h = x[i + 1] - x[i]
        t = (xx - x[i]) / h
        out[n] = ((2.0 * t ** 3 - 3.0 * t ** 2 + 1.0) * y[i]
                  + (t ** 3 - 2.0 * t ** 2 + t) * h * m[i]
                  + (-2.0 * t ** 3 + 3.0 * t ** 2) * y[i + 1]
                  + (t ** 3 - t ** 2) * h * m[i + 1])
        der[n] = ((6.0 * t ** 2 - 6.0 * t) * (y[i] - y[i + 1]) / h
                  + (3.0 * t ** 2 - 4.0 * t + 1.0) * m[i]
                  + (3.0 * t ** 2 - 2.0 * t) * m[i + 1])
    return out, der


def _pose(stage, title):
    """The paper's posing on our machine, shared by the stages that walk
    (opt) and the stage that only differentiates (grad): their lip, their
    injection angle, their length, their base model, the knots and THEIR
    contour interpolated at those knots. Bit-identical to the record's
    stage opt, whose lines these are."""
    R_lip = R_RAO if CASE == "rao" else R_OPT
    F_ref = F_RAO if CASE == "rao" else F_OPT
    w = build_world(R_lip)
    S = w["S"]
    L = X_D * S if CASE == "rao" else (L_TD - 0.56069 * IN) * S
    os.environ.setdefault("PSPL_L", "%.10f" % L)
    os.environ.setdefault("PSPL_M", "6")
    os.environ.setdefault("PSPL_K", "81")
    os.environ.setdefault("PSPL_N", "41")
    os.environ.setdefault("PSPL_ITERS", "10")
    os.environ.setdefault("A1_BASE_MODEL", "veen")
    # HMPH_FAN=axi (S32): the axisymmetric fan [X-AFAN] -- admissible for
    # the Rao case only (theta_E = 0); the wall is then the ideal member
    # (Rao's Table 3 to the digitisation, S31) and the mass is the
    # member's own (137.8 lbm/s against their 148.08: the open mass
    # convention), so the thrust rows carry the -7 percent and the
    # SHAPE rows are the test
    if os.environ.get("HMPH_FAN", "planar") == "axi" and CASE == "rao":
        os.environ["PSPL_FAN"] = "axi"
    else:
        os.environ.pop("PSPL_FAN", None)
    import a1_config_compare as CC
    import a1_inlet_angle_opt as IA
    import a1_plug_spline_opt as P
    CC.PA = IA.PA = P.PA = PA
    IA.MI = 1.0002                        # the sonic lip of the paper
    if os.environ.get("PSPL_FAN") == "axi":
        # the axisymmetric fan certifies only with its leading ray at
        # M_i >= 1.6 (X-CHTW, the vertical-characteristic floor); the
        # strip below is declared, as in the Chutkey twin
        IA.MI = M_I_FAN
        import a1_axi_fan as AF
        AF._CACHE.clear()
    IA.X0 = P.X0 = X0_R
    IA.X_END = max(IA.X_END, L)
    P.L = L
    P.CKPT = os.path.join(ART, "_ckpt_" + CASE)
    os.makedirs(P.CKPT, exist_ok=True)
    say("== [F3] Humphreys 1971, twin (B) case %s: %s"
        " [X-HMPH] (stage %s) ==" % (CASE, title, stage))
    # the exhaust angle from the injection angle: theta_E = theta_i + dnu
    fan0 = IA.fan_at(w, 0.0)
    thE = 0.0 if CASE == "rao" else np.radians(TH_I_OPT) + fan0["dnu"]
    say("   lip %.2f in, L %.3f in from the lip (%.4f R), fan turn %.2f deg"
        " -> theta_i %.2f deg, theta_E %.2f deg; mdot %.2f lbm/s imposed"
        " through the cut at X0 %.2f R; base model veen; target %.0f lbf"
        % (R_lip / IN, L / S / IN, L, np.degrees(fan0["dnu"]),
           np.degrees(thE - fan0["dnu"]), np.degrees(thE), MDOT / 0.45359237,
           X0_R, F_ref / LBF))
    c = P.build_case(w, thE=thE)
    ta = w["ta"]
    key = ("table3_rao_lip8.33_inj-58.5" if CASE == "rao"
           else "table2_optimum_lip7.55_inj-34")
    tab = np.array(TABLES[key])
    W_ref = read_table(np.asarray(c["xk"]) / S / IN, tab) * IN * S
    return dict(w=w, S=S, L=L, F_ref=F_ref, P=P, IA=IA, c=c, ta=ta,
                W_ref=W_ref, thE=thE)


def opt():
    t00 = time.time()
    st = _pose("opt", "the TR-SQP at their posing")
    w, S, L, F_ref = st["w"], st["S"], st["L"], st["F_ref"]
    P, c, ta, W_ref, thE = st["P"], st["c"], st["ta"], st["W_ref"], st["thE"]
    if P.PARAM != "y" and (START == "table"
                           or float(os.environ.get("HMPH_PERTURB", 0.0)) > 0.0):
        # the table start and the knot perturbation are tests in y
        # coordinates (their table read at the knots, a displacement of
        # the knots in inches); in angle coordinates the walk opens from
        # the fan's streamline (S33, stage angle)
        say("   PSPL_PARAM=%s: the start is the fan's streamline only"
            % P.PARAM)
        return False
    if START == "table":
        c["W0"] = W_ref.copy()
    elif os.environ.get("PSPL_FAN") == "axi":
        say("   start = the axisymmetric ideal member at the knots (fan_axi); vs Table 3:"
            " max |dy| %.3f in" % (np.max(np.abs(np.asarray(c["W0"]) - W_ref)) / S / IN))
    # RETURN-FROM-PERTURBATION (S32): HMPH_PERTURB = delta [in], seeded
    # normal perturbation of the start's knots (the tip knot kept above
    # its floor); the walk must come back to the reference landing
    delta = float(os.environ.get("HMPH_PERTURB", 0.0))
    ptag = ""
    if delta > 0.0:
        rng = np.random.default_rng(int(os.environ.get("HMPH_SEED", 1)))
        dW = rng.standard_normal(len(c["W0"])) * delta * IN * S
        c["W0"] = np.asarray(c["W0"]) + dW
        say("   perturbation delta %.2f in (seed %s): dW = %s in"
            % (delta, os.environ.get("HMPH_SEED", 1), np.array2string(dW / S / IN, precision=3)))
        # the tag carries it: a perturbed leg must not overwrite the
        # record's landing (it did once, S32 -- the file was restored
        # from the commit and the leg re-filed under this name)
        ptag = "_perturb%.2f_seed%s" % (delta, os.environ.get("HMPH_SEED", 1))
    say("   start radius y_w0 %.3f in (mass-set), F_in %.1f kN; start = %s;"
        " knots %s" % (c["yw0"] / S / IN, c["F_in"] / S / S / 1e3, START,
                       np.array2string(P.knot_radii(c["W0"], c) / S / IN,
                                       precision=3)))
    out0, sched0 = P.march_record(c["W0"], w, c)
    J0 = float(P.J_replay(jnp.asarray(c["W0"]), w, c, sched0, ta))
    say("   the start (%s): cert %.3f, J %.1f kN = %.0f lbf (%+.2e vs"
        " target)" % (START, float(out0["cert_worst"]), J0 / S / S / 1e3,
                      J0 / S / S / LBF, J0 / S / S / F_ref - 1))
    if START == "table":
        check("O-0 at the paper's own contour our functional reads the"
              " paper's thrust within 1 percent (%+.2e; their shear 0.2"
              " percent)" % (J0 / S / S / F_ref - 1),
              abs(J0 / S / S / F_ref - 1) <= THRUST_TOL)
    W, hist, n_rec = P.run_trsqp(np.asarray(c["W0"], float), w, c, ta,
                                 sign=+1.0, max_segments=P.MAXSEG,
                                 maxiter_per_seg=8, verbose=1,
                                 bounds=P.design_bounds(c))
    out1, sched1 = P.march_record(W, w, c)
    J1 = float(P.J_replay(jnp.asarray(W), w, c, sched1, ta))
    yk1 = P.knot_radii(W, c)
    say("   TR-SQP: %d records, J %.1f kN = %.0f lbf (%+.2e vs the paper's"
        " %.0f); cert %.3f; y_D %.3f in"
        % (n_rec, J1 / S / S / 1e3, J1 / S / S / LBF, J1 / S / S / F_ref - 1,
           F_ref / LBF, float(out1["cert_worst"]), float(yk1[-1]) / S / IN))
    if P.PARAM != "y":
        a1 = np.degrees(np.arctan(np.asarray(P.wall_stations(W, c)[2])))
        say("   the landing's wall angle %+.2f..%+.2f deg, %d turn(s);"
            " increments %s deg"
            % (a1.min(), a1.max(), n_turns(a1),
               np.array2string(np.degrees(np.asarray(W)), precision=3)))
    check("O-1 the walk's best design is Newton-certified (%.3f)"
          % float(out1["cert_worst"]), float(out1["cert_worst"]) <= 1.0)
    check("O-2 the thrust reproduces the paper's within 1 percent (their"
          " shear is 0.2 percent; %+.2e)" % (J1 / S / S / F_ref - 1),
          abs(J1 / S / S / F_ref - 1) <= THRUST_TOL)
    if W_ref is not None:
        dknot = np.abs(yk1 - W_ref) / S / IN
        say("   knots vs the paper's table: %s in (max %.3f); y_D %.3f vs %.3f in"
            % (np.array2string(dknot, precision=3), dknot.max(), float(yk1[-1]) / S / IN,
               float(W_ref[-1]) / S / IN))
        if delta > 0.0:
            check("P-1 return from the perturbation: the knots come back to the table"
                  " within delta/3 = %.3f in (max %.3f, the first knot excluded: the"
                  " planar inlet's own +0.34 in)" % (delta / 3.0, dknot[1:].max()),
                  dknot[1:].max() <= delta / 3.0)
        if os.environ.get("PSPL_FAN") == "axi" and START == "fan":
            ktol = TABLES["_knot_class_in"]
            check("P-2 from the ideal member the walk STAYS on Rao's Table 3 within"
                  " %.2f in on every knot (max %.3f)" % (ktol, dknot.max()), dknot.max() <= ktol)
    wall = np.asarray(out1["wall"])
    rec = dict(case=CASE, L_R=L, thE_deg=float(np.degrees(thE)), J0=J0 / S / S,
               J1=J1 / S / S, J1_lbf=J1 / S / S / LBF, F_ref_lbf=F_ref / LBF,
               W_in=(np.asarray(W) / S / IN).tolist(), xk_in=(np.asarray(c["xk"]) / S / IN).tolist(),
               yw0_in=c["yw0"] / S / IN, cert=float(out1["cert_worst"]),
               hist=[list(map(float, h)) if hasattr(h, "__iter__") else float(h) for h in hist],
               wall_in=np.c_[wall[:, 0] / S / IN, wall[:, 1] / S / IN].tolist(),
               seconds=time.time() - t00)
    os.makedirs(ART, exist_ok=True)
    rec["start"] = START
    rec["base_model"] = os.environ["A1_BASE_MODEL"]
    if P.PARAM != "y":
        # angle coordinates: the design itself and the knot radii, never
        # a "W_in" a y-coordinate reader would march as a spline
        rec.pop("W_in")
        rec.update(param=P.PARAM, W_rad=np.asarray(W).tolist(),
                   yk_in=(yk1 / S / IN).tolist())
        ptag += "_" + P.PARAM
    tag = "%s_%s_%s%s" % (CASE, START, os.environ["A1_BASE_MODEL"], ptag)
    json.dump(rec, open(os.path.join(ART, "opt_%s.json" % tag), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage grad: the gradient AT the optimum (no walk)
# ----------------------------------------------------------------------
def grad():
    """Grade the gradient where the walks END, and read the stationarity
    of THEIR contour for OUR functional (S32 section 14's two open
    readings). A walk cannot answer either, the walk being the
    instrument under test: (i) is the reverse-AD gradient the driver
    follows still the derivative of the RE-MARCHED value near the
    optimum, where the marginal cells sit on the certification floor,
    and (ii) is the paper's own contour stationary for us -- read
    against what our own march can resolve, not against a wish.

    Both are single-point measurements. The gradient is graded by the
    driver's own C-2 standard (central differences on a LADDER of steps,
    the band being the differences' own scatter, because the replayed
    march is only piecewise smooth in the design). The stationarity is
    priced: what a move of the measured STAY CLASS (0.15 in, the tables
    JSON) of each knot buys at first order, against the band the same
    design's (K, N) -> (2K-1, 2N-1) refinement supports -- the C-6 rule,
    the band measured by the instrument that read the number."""
    t00 = time.time()
    st = _pose("grad", "the gradient at their optimum")
    w, S, F_ref = st["w"], st["S"], st["F_ref"]
    P, c, ta, W_ref, thE = st["P"], st["c"], st["ta"], st["W_ref"], st["thE"]
    base = os.environ["A1_BASE_MODEL"]
    cls_in = TABLES["_knot_class_in"]

    def per_in(g):
        """dJ/dy at the knots, from the scaled world to lbf per inch."""
        return np.asarray(g) / S * IN / LBF

    # the points to grade: THEIR contour, and the landings our own walks
    # reached from it (the record's, and a perturbed one if it is filed)
    pts = [("their table", np.asarray(W_ref, float))]
    fn = os.path.join(ART, "opt_%s_table_%s.json" % (CASE, base))
    if os.path.exists(fn):
        pts.append(("our landing",
                    np.array(json.load(open(fn))["W_in"]) * IN * S))
    pert = sorted(glob.glob(os.path.join(
        ART, "opt_%s_table_%s_perturb*.json" % (CASE, base))))
    if pert:
        pts.append(("perturbed landing",
                    np.array(json.load(open(pert[0]))["W_in"]) * IN * S))
    rec = dict(case=CASE, base_model=base, stay_class_in=cls_in, points={})
    got = {}
    for name, W in pts:
        W = np.asarray(W, float)
        out, sch = P.march_record(W, w, c)
        J, g = P.J_and_grad(W, w, c, ta, sch)
        got[name] = (W, J, g, sch, out)
        say("   %-18s J %.1f lbf (%+.2e vs the paper's %.0f), cert %.3f,"
            " |grad| %.3e" % (name, J / S / S / LBF, J / S / S / F_ref - 1,
                              F_ref / LBF, float(out["cert_worst"]),
                              float(np.linalg.norm(g))))
        say("                      dJ/dy per knot [lbf/in]: %s"
            % np.array2string(per_in(g), precision=1))
        rec["points"][name] = dict(
            W_in=(W / S / IN).tolist(), J_lbf=J / S / S / LBF,
            cert=float(out["cert_worst"]),
            dJdy_lbf_per_in=per_in(g).tolist())

    W, J, g, sch, out = got["their table"]

    # ---- the band THIS reading's own refinement supports -------------
    K2, N2 = 2 * P.K_ST - 1, 2 * P.N_ROW - 1
    c2 = P.build_case(w, thE=thE, N=N2)
    fine = {}
    for name, (Wn, _Jn, _gn, _sn, _on) in got.items():
        _, s2n = P.march_record(Wn, w, c2, K=K2)
        fine[name] = (float(P.J_replay(jnp.asarray(Wn), w, c2, s2n, ta,
                                       K=K2)), s2n)
    J2, s2 = fine["their table"]
    band_J = A1.K_RICH * abs(J - J2) + A1.C_FLOOR * A1.EPS * abs(J)
    band_lbf = band_J / S / S / LBF
    grid = TABLES["_grid_class_lbf"]
    say("   the march's own band on J at their contour: (%d,%d) %.1f lbf vs"
        " (%d,%d) %.1f lbf -> %.1f lbf (%.2e of J); the paper's own grid"
        " (Table 1) spans %.0f lbf"
        % (P.K_ST, P.N_ROW, J / S / S / LBF, K2, N2, J2 / S / S / LBF,
           band_lbf, band_J / abs(J), grid[1] - grid[0]))
    rec["band_lbf"] = band_lbf
    rec["grid_span_lbf"] = grid[1] - grid[0]

    # ---- the band on a DIFFERENCE, which is what a move buys ---------
    # An optimiser never reads the value: it reads the difference
    # between two designs, and the march's discretisation error is
    # COMMON to designs of the same family on the same grid. Graded
    # against the value's band (here 2.9e-2 of J -- five times the span
    # of the paper's OWN 20-run grid) no first-order price could ever
    # be live, and the gate would be measuring the grid, not the
    # optimum. The band on a move is the amount by which the
    # refinement moves the DIFFERENCE between the graded designs.
    band_dJ = A1.C_FLOOR * A1.EPS * abs(J)
    for name, (Jf, _sf) in sorted(fine.items()):
        if name == "their table":
            continue
        dc, df = got[name][1] - J, Jf - J2
        band_dJ = max(band_dJ, A1.K_RICH * abs(dc - df)
                      + A1.C_FLOOR * A1.EPS * abs(J))
        say("   %-18s minus their table: %+.1f lbf at (%d,%d), %+.1f lbf"
            " at (%d,%d) -- the refinement moves the DIFFERENCE %.1f lbf"
            % (name, dc / S / S / LBF, P.K_ST, P.N_ROW, df / S / S / LBF,
               K2, N2, abs(dc - df) / S / S / LBF))
    band_dlbf = band_dJ / S / S / LBF
    say("   the march's band on a MOVE: %.1f lbf (%.2e of J) against the"
        " value's %.1f lbf; the paper's own grid spans %.0f lbf"
        % (band_dlbf, band_dJ / abs(J), band_lbf, grid[1] - grid[0]))
    rec["band_diff_lbf"] = band_dlbf

    # ---- G-1: the adjoint against central differences, AT the optimum -
    fj = lambda z: P.J_replay(z, w, c, sch, ta)          # noqa: E731
    Wj = jnp.asarray(W, dtype=float)
    ok1 = True
    for k in range(len(g)):
        v = jnp.zeros(len(g)).at[k].set(1.0)
        scale = max(1.0, abs(float(W[k])))
        fd, spread = P.fd_ladder(fj, Wj, v, scale)
        band = (A1.K_RICH * spread
                + A1.C_FLOOR * A1.EPS * abs(J) / (P.FD_LADDER[-1] * scale))
        ok1 = ok1 and (abs(fd - g[k]) <= band)
        say("      knot %d: AD %+.6e  FD %+.6e  |d| %.3e  (ladder spread"
            " %.3e -> band %.3e)" % (k, g[k], fd, abs(fd - g[k]), spread,
                                     band))
    check("G-1 at their optimum the AD gradient matches central finite"
          " differences inside the band the differences' own scatter"
          " supports", ok1)

    # ---- G-2/G-3: what a class-sized move of each knot buys -----------
    price = np.abs(np.asarray(g)) / S * (cls_in * IN) / LBF
    say("   price of a stay-class move (%.2f in) per knot [lbf]: %s"
        % (cls_in, np.array2string(price, precision=1)))
    rec["price_lbf"] = price.tolist()
    check("G-2 at their contour, the inlet knot excluded (the planar cut's"
          " own dof, frozen by the posing), no knot buys more than the"
          " band the march supports on a MOVE over a stay-class"
          " displacement (max %.1f lbf vs %.1f)"
          % (price[1:].max(), band_dlbf), price[1:].max() <= band_dlbf)
    check("G-3 the inlet knot DOES buy more (%.1f lbf vs the band on a"
          " move %.1f): the one live direction at their optimum is the"
          " frozen inlet, not the shape"
          % (price[0], band_dlbf), price[0] > band_dlbf)

    # ---- G-5: is the LANDSCAPE resolved where the VALUE is not? -------
    # The walk follows the gradient, so what must survive the refinement
    # is the gradient, not J. Same contour, same base, the refined grid.
    f2 = lambda z: P.J_replay(z, w, c2, s2, ta, K=K2)    # noqa: E731
    g2 = np.asarray(P.jax.grad(f2)(jnp.asarray(W, dtype=float)), float)
    price2 = np.abs(g2) / S * (cls_in * IN) / LBF
    say("   dJ/dy per knot at (%d,%d) [lbf/in]: %s   (price %s)"
        % (K2, N2, np.array2string(per_in(g2), precision=1),
           np.array2string(price2, precision=1)))
    rec["dJdy_fine_lbf_per_in"] = per_in(g2).tolist()
    rec["price_fine_lbf"] = price2.tolist()
    check("G-5 the LANDSCAPE is resolved where the value is not: under"
          " (K,N) -> (2K-1,2N-1) the price of a stay-class move changes"
          " by less than the band on a move on every knot (max %.1f lbf"
          " vs %.1f)" % (np.abs(price2 - price).max(), band_dlbf),
          np.abs(price2 - price).max() <= band_dlbf)

    # ---- G-4: the tip the perturbed walk did not bring back -----------
    if "perturbed landing" in got:
        Wp, Jp, gp = got["perturbed landing"][:3]
        dtip = abs(float(Wp[-1]) - float(W_ref[-1])) / S / IN
        ptip = abs(float(gp[-1])) / S * (dtip * IN) / LBF
        say("   the perturbed walk's tip residue %.3f in is worth %.1f lbf"
            " on ITS OWN gradient (%.1f lbf/in)"
            % (dtip, ptip, per_in(gp)[-1]))
        rec["tip_residue_in"], rec["tip_price_lbf"] = dtip, ptip
        check("G-4 the tip residue the perturbed walk left (%.3f in) is"
              " worth %.1f lbf at first order -- below the band on a"
              " move (%.1f): the walk does not restore it because nothing"
              " pays for it, which is the P-1 failure read at the"
              " gradient" % (dtip, ptip, band_dlbf), ptip <= band_dlbf)

    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(
        ART, "grad_%s_%s.json" % (CASE, base)), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage class: is the march of each design IN CLASS (unfolded)?
# ----------------------------------------------------------------------
def _census(P, PMG, w, W, case, K=None):
    """The fold census of one design, [X-PMRG]'s own field (stage class):
    (out, sched, per-cell margin and index, resolved, folded, fraction).
    PMG is imported by the caller AFTER _pose (the import-order trap)."""
    e2 = PMG.station_spacing(K or P.K_ST) ** 2
    m = PMG.margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=1.0,
                        f_edge=0.0, ell2=e2)
    out, sch = P.march_record(np.asarray(W, float), w, case, K=K,
                              margin=m)
    N = len(case["start"][1])
    ms, dep, wh, fl = PMG.np_margin(out, sch, N, 1.0, 0.0, e2,
                                    with_depth=True, with_floor=True)
    orient = float(np.sign(np.median(ms)))
    ms, fl = np.asarray(ms) * orient, np.asarray(fl, bool)
    res = ~fl
    neg = res & (ms <= 0.0)
    frac = 100.0 * neg.sum() / max(1, res.sum())
    return dict(out=out, sched=sch, ms=ms, res=res, neg=neg, wh=wh,
                W=np.asarray(W, float), frac=float(frac),
                n_res=int(res.sum()), n_neg=int(neg.sum()))


def _j_parts(P, w, case, W, sched, ta):
    """J_replay's three terms on the same replay -- the momentum through
    the cut (F_in), the wall push, the base term of A1_BASE_MODEL -- with
    the push per wall segment and the wall state at D (stage angle A-7)."""
    xq, yq, sq = P.wall_stations(W, case)
    out, _ = P.plug_march((xq, yq, sq), case["start"], case["qpa"],
                          w["tab"], 1.0, sched=A1.Sched("play", sched.d))
    wall = np.asarray(out["wall"])
    q = np.sqrt(wall[:, 2] ** 2 + wall[:, 3] ** 2)
    st = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), ta)]
    pw = st[1]
    dy = wall[1:, 1] - wall[:-1, 1]
    wgt = 2.0 * np.pi * 0.5 * (wall[1:, 1] + wall[:-1, 1])
    seg = (0.5 * (pw[1:] + pw[:-1]) - P.PA) * wgt * (-dy)
    pb = float(BP.p_base(st[1][-1], st[5][-1], st[4][-1], P.PA, P.BASE_MODEL))
    return dict(F_in=float(case["F_in"]), push=float(seg.sum()),
                base=float(BP.base_term(pb, wall[-1, 1], P.PA)), seg=seg,
                y_D=float(wall[-1, 1]), p_D=float(pw[-1]),
                M_D=float(st[5][-1]), p_b=pb)


def klass():
    """ATTRIBUTE the certification failures of this twin -- and read the
    class of the designs the thrust rows rest on.

    S29 measured, on the S22/S23 spike designs, that the Newton
    certification is BLIND to a folded net: a march whose cells invert
    still certifies, and the thrust it reports is accounted downstream
    through the tangled net ([X-PMRG], the fold margin; [X-PGRS]
    re-stamped OUT OF CLASS on that reading). The Humphreys legs of S31
    and S32 ran the driver WITHOUT the margin -- no class constraint --
    so the question is open for every design of this row, including the
    paper's own contour as WE march it.

    The census is the margin carrier's own (`a1_plug_margin.np_margin`,
    the signed area of the net's true cell over its mean legs, floored
    at the station spacing squared, orient-signed by the median): a
    RESOLVED cell (leg product above the floor -- the floored ones are
    the free-jet slivers the criterion does not resolve) with a
    non-positive margin is a fold. The incumbent of this posing -- the
    fan's own streamline, the start the record's walks open from -- is
    the control: if the criterion called IT folded, the criterion would
    be mis-posed.

    The gates also SPLIT the two certification failures of this row,
    which are not the same mechanism: the 1.5-22 band that parks the
    walks near the optimum (S32 section 14) against the 2.96e8 on the
    paper's contour at the finer rung (section 15)."""
    t00 = time.time()
    st = _pose("class", "the class of the designs (folded net or not)")
    w, S, F_ref = st["w"], st["S"], st["F_ref"]
    P, c, ta, W_ref, thE = st["P"], st["c"], st["ta"], st["W_ref"], st["thE"]
    base = os.environ["A1_BASE_MODEL"]
    import a1_plug_margin as PMG          # imports the driver: after _pose

    ell2 = PMG.station_spacing(P.K_ST) ** 2
    mg = PMG.margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=1.0,
                         f_edge=0.0, ell2=ell2)

    def census(W, case, K=None):
        return _census(P, PMG, w, W, case, K)

    # the designs of this row, in the order of the argument
    pool = [("fan streamline (incumbent)", np.asarray(c["W0"], float)),
            ("their Table 2", np.asarray(W_ref, float))]
    for nm, pat in (("our landing", "opt_%s_table_%s.json" % (CASE, base)),
                    ("perturbed landing",
                     "opt_%s_table_%s_perturb*.json" % (CASE, base))):
        g = sorted(glob.glob(os.path.join(ART, pat)))
        if g:
            pool.append((nm, np.array(json.load(open(g[0]))["W_in"])
                         * IN * S))
    got = {}
    for nm, W in pool:
        r = census(W, c)
        J = float(P.J_replay(jnp.asarray(np.asarray(W, float)), w, c,
                             r["sched"], ta))
        r["J"] = J
        got[nm] = r
        say("   %-26s J %9.1f lbf (%+.2e), cert %.4e at %-16s |"
            " resolved %5d, FOLDED %4d (%.2f %%)"
            % (nm, J / S / S / LBF, J / S / S / F_ref - 1,
               float(r["out"]["cert_worst"]), str(r["out"]["cert_where"]),
               r["n_res"], r["n_neg"], r["frac"]))

    inc = got["fan streamline (incumbent)"]
    check("K-1 the criterion discriminates: the incumbent of this posing"
          " (the fan's own streamline, the start of the record's walks)"
          " has NO folded resolved cell (%d of %d)"
          % (inc["n_neg"], inc["n_res"]), inc["n_neg"] == 0)
    tab = got["their Table 2"]
    check("K-2 the paper's own contour, marched with OUR frozen planar"
          " inlet, is OUT OF CLASS by the incumbent's own standard:"
          " %d folded resolved cells (%.2f %%)"
          % (tab["n_neg"], tab["frac"]), tab["n_neg"] > 0)

    # ---- the two certification failures are not the same mechanism ----
    def neighbourhood(r):
        """The margin at the census cell adjacent to the worst-certified
        cell (np_margin's column i = the march's station kst + 2)."""
        tag = r["out"]["cert_where"]
        kst = int(tag[1])
        sel = [n for n, (i, j) in enumerate(r["wh"]) if i == kst + 2]
        if not sel:
            return None, None, 0
        rows = [r["wh"][n][1] for n in sel]
        # the wall-adjacent census row is the carrier's own jmin
        n0 = sel[int(np.argmin(np.abs(np.array(rows) - PMG.JMIN)))]
        return (float(r["ms"][n0]), bool(r["res"][n0]),
                int(sum(1 for n in sel if r["neg"][n])))

    if "perturbed landing" in got:
        pr = got["perturbed landing"]
        m0, res0, ncol = neighbourhood(pr)
        say("   the walk-parking band: cert %.3f at %s -- the adjacent"
            " resolved cell carries margin %+.4f (%d folded in its column)"
            % (float(pr["out"]["cert_worst"]),
               str(pr["out"]["cert_where"]), m0, ncol))
        check("K-3 the certification floor that PARKS the walks (cert in"
              " the 1.5-22 band, S32 section 14) is NOT a fold: the cell"
              " next to it is resolved and healthy (margin %+.4f) -- the"
              " near-wall conditioning of S31 section 3.3, which the"
              " rotated-frame cell addresses" % m0,
              (m0 is not None) and res0 and m0 > 0.0)

    # ---- the refined rung: the 2.96e8, and whether the fold is the
    # ---- design's or the net's
    K2, N2 = 2 * P.K_ST - 1, 2 * P.N_ROW - 1
    c2 = P.build_case(w, thE=thE, N=N2)
    t2 = census(W_ref, c2, K=K2)
    say("   their Table 2 refined to (%d,%d): cert %.4e at %s, resolved"
        " %d, FOLDED %d (%.2f %%)"
        % (K2, N2, float(t2["out"]["cert_worst"]),
           str(t2["out"]["cert_where"]), t2["n_res"], t2["n_neg"],
           t2["frac"]))
    m2, res2, ncol2 = neighbourhood(t2)
    check("K-4 the 2.96e8 of the finer rung IS a fold, not conditioning:"
          " the worst-certified cell's own column carries %d folded cells"
          % ncol2, ncol2 > 0)
    band_pp = A1.K_RICH * 100.0 * max(1.0 / max(1, tab["n_res"]),
                                      1.0 / max(1, t2["n_res"]))
    check("K-5 the fold is the DESIGN's, not the net's: the folded"
          " fraction is the same at both rungs within the census's own"
          " granularity (%.2f vs %.2f %%, band %.2f pp)"
          % (tab["frac"], t2["frac"], band_pp),
          abs(tab["frac"] - t2["frac"]) <= band_pp)

    # ---- K-6: does the fold REACH what the row argues about? ---------
    # J = F_in (the momentum through the cut, fixed by the imposed mass)
    # + the wall push, and only the push is marched. A fold at column i
    # can reach the wall no further upstream than i, so the push
    # DOWNSTREAM of the first fold is the part of J the tangled net can
    # touch; the scale to read it against is the one this row argues at,
    # the span of the paper's own 20-run grid.
    def reach(r, W):
        cols = np.array([i for (i, j) in r["wh"]])
        if not r["neg"].any():
            return 0, 0.0, 0.0, float("nan")
        kmin = int(cols[r["neg"]].min()) - PMG.JMIN     # column i = kst + 2
        wall = np.asarray(r["out"]["wall"])
        q = np.sqrt(wall[:, 2] ** 2 + wall[:, 3] ** 2)
        pw = np.asarray(A1.state_q(jnp.asarray(q), ta)[1])
        dy = wall[1:, 1] - wall[:-1, 1]
        wgt = 2.0 * np.pi * 0.5 * (wall[1:, 1] + wall[:-1, 1])
        seg = (0.5 * (pw[1:] + pw[:-1]) - P.PA) * wgt * (-dy)
        down = float(seg[kmin:].sum()) if kmin < len(seg) else 0.0
        sx = np.asarray(P.wall_stations(np.asarray(W, float), c)[0])
        return (kmin, down / S / S / LBF, float(seg.sum()) / S / S / LBF,
                float(sx[min(kmin, len(sx) - 1)]) / S / IN)

    span = TABLES["_grid_class_lbf"][1] - TABLES["_grid_class_lbf"][0]
    kmin, down, tot, xf = reach(tab, W_ref)
    say("   their Table 2: the first fold is at column %d (x %.2f in,"
        " %.0f %% along the wall); the wall push is %.0f lbf of J and"
        " %.0f lbf of it (%.0f %%) lies DOWNSTREAM of that fold"
        % (kmin, xf, 100.0 * kmin / (P.K_ST - 1), tot, down,
           100.0 * down / tot))
    kmin2, down2, tot2, xf2 = reach(got["our landing"],
                                    got["our landing"]["W"]) \
        if "our landing" in got else (0, 0.0, 0.0, float("nan"))
    if "our landing" in got:
        say("   our landing: first fold at column %d (x %.2f in), %.0f lbf"
            " of %.0f downstream (%.0f %%)"
            % (kmin2, xf2, down2, tot2, 100.0 * down2 / tot2))
    rec_reach = {}
    check("K-6 the fold REACHES what this row argues about: the wall push"
          " downstream of their contour's first fold (%.0f lbf) exceeds"
          " the span of the paper's own 20-run grid (%.0f lbf) -- the"
          " scale at which this twin's verdicts are read -- so the fold"
          " is not a detail of the net far from the answer"
          % (down, span), down > span)
    # ---- K-7: WHERE the fold comes from -- the inlet the posing froze -
    # The start radius is set by the imposed mass, not by their contour,
    # so the wall begins ABOVE their wall and must come back down to the
    # first knot (which their table sets). It does that with an S-turn,
    # and the second half of an S-turn is a COMPRESSION: characteristics
    # converge, and a march of characteristics carries no shock.
    tab2 = np.array(TABLES["table2_optimum_lip7.55_inj-34"])
    sx, sy, ssl = P.wall_stations(np.asarray(W_ref, float), c)
    sx, sy = np.asarray(sx) / S / IN, np.asarray(sy) / S / IN
    ang = np.degrees(np.arctan(np.asarray(ssl)))
    theirs_y = np.interp(sx, tab2[:, 0], tab2[:, 1])
    d0 = float(sy[0] - theirs_y[0])
    dmax = float(np.abs(sy - theirs_y).max())
    # A plug wall that flattens downstream is not, by itself, a
    # compression: it is the shape of every plug, and the paper's own
    # angle column climbs monotonically from -46.8 deg to -13.3. What
    # is NOT theirs is WHERE the steepening turn happens. Their contour
    # reaches its steepest angle at x = -0.035 in -- UPSTREAM of our cut
    # -- and climbs from there; our wall, forced to start above their
    # wall, re-does that turn INSIDE the marched field, and the net
    # folds just downstream of it.
    x_dip_us = float(sx[int(np.argmin(ang))])
    x_dip_them = float(tab2[int(np.argmin(tab2[:, 2])), 0])
    say("   the inlet the posing froze: we start %+.3f in above their"
        " wall (y_w0 %.3f vs their %.3f at the cut), the deviation peaks"
        " at %+.3f in and the first knot is only at x %.2f in; THEIR"
        " contour is steepest at x %+.3f in (upstream of the cut, x0"
        " %.3f) and climbs from there, OUR wall is steepest at x %+.3f"
        " in -- the turn re-done inside the field, %+.1f -> %+.1f deg"
        % (d0, float(sy[0]), float(theirs_y[0]), dmax,
           float(np.asarray(c["xk"])[0] / S / IN), x_dip_them,
           float(P.X0) / S / IN, x_dip_us, float(ang.min()),
           float(ang[-1])))
    check("K-7 the fold is BORN IN THAT TURN: their contour is steepest"
          " UPSTREAM of our cut (x %+.3f vs x0 %.3f in) while ours is"
          " steepest at x %.2f in, inside the field, and the first folded"
          " column (x %.2f in) lies downstream of OUR turn -- the cause"
          " is the posing's own start radius, not the paper's contour"
          % (x_dip_them, float(P.X0) / S / IN, x_dip_us, xf),
          x_dip_them < float(P.X0) / S / IN < x_dip_us <= xf)
    rec_reach.update(start_above_in=d0, dev_max_in=dmax,
                     x_steepest_ours_in=x_dip_us,
                     x_steepest_theirs_in=x_dip_them)

    # ---- K-8: the wall ANGLE is what the characteristics see ---------
    # y within a hundredth of an inch is not the criterion: the net is
    # built from the wall's DIRECTION. Their third column prints it, and
    # downstream of their own dip it climbs monotonically; ours, from a
    # six-knot spline pinned at a start radius that is not theirs,
    # oscillates about it.
    dang = ang - np.interp(sx, tab2[:, 0], tab2[:, 2])
    nsign = int((np.diff(np.sign(dang)) != 0).sum())
    nturn = int((np.diff(np.sign(np.diff(ang))) != 0).sum())
    say("   the wall ANGLE, which is what the characteristics see: ours"
        " departs from their printed angle by %+.2f deg (x %.2f) to"
        " %+.2f deg (x %.2f), rms %.2f deg, crossing it %d times; their"
        " angle downstream of their dip is MONOTONE, ours turns %d times"
        % (dang.max(), float(sx[int(dang.argmax())]), dang.min(),
           float(sx[int(dang.argmin())]),
           float(np.sqrt((dang ** 2).mean())), nsign, nturn))
    check("K-8 the design vector cannot HOLD their contour: six knots"
          " pinned at a start radius that is not theirs reproduce y to"
          " %.3f in but make the wall ANGLE oscillate about their printed"
          " angle (%d crossings, %.1f deg peak to peak) where theirs is"
          " monotone -- at M 2-3 the Mach angle is 20-30 deg, so a"
          " ten-degree wall error is not a detail of the drawing"
          % (dmax, nsign, float(dang.max() - dang.min())),
          nsign > 1 and nturn > 0)

    rec_reach.update(their_first_fold_col=kmin, their_x_in=xf,
                     their_push_lbf=tot, their_push_downstream_lbf=down,
                     grid_span_lbf=span)

    # ---- K-9: WHY the start radius is not their wall ------------------
    # The posing had to choose. Our start data are an idealised planar
    # corner fan at a sonic lip; theirs are a real annular transonic
    # throat (their "modified Moore-Hall"). The two do not pass the same
    # mass through the same annulus, so the cut can carry THEIR MASS or
    # sit on THEIR WALL, not both. The record chose the mass -- thrust
    # is proportional to it, and a thrust compared at another mass is
    # not a comparison -- and paid with the geometry.
    from a1_plug_march import col_fluxes
    ye0 = c["fan"]["LIP"][1] + np.tan(c["fan"]["th_e"]) * P.X0

    def mass_at(yw):
        yl = np.linspace(yw, ye0, P.N_ROW)
        uv = [c["fan"]["field"](P.X0, y) for y in yl]
        stl = np.stack([np.full(P.N_ROW, P.X0), yl,
                        np.array([q * np.cos(t) for q, t in uv]),
                        np.array([q * np.sin(t) for q, t in uv])], axis=1)
        md, Fi = col_fluxes(stl, w["ta"], P.PA, 1.0)
        return abs(float(md)), float(Fi)

    # both radii read AT THE CUT: the wall's first station is a little
    # downstream of X0, and comparing across stations would price the
    # contour's own slope instead of the posing
    y_cut_them = float(np.interp(float(P.X0) / S / IN, tab2[:, 0],
                                 tab2[:, 1]))
    m_rec, F_rec = mass_at(float(c["yw0"]))
    m_th, F_th = mass_at(y_cut_them * IN * S)
    dm = 100.0 * (m_th / m_rec - 1.0)
    say("   why the cut is not on their wall: at the cut (x %.3f in) our"
        " mass-set wall is %.3f in and theirs is %.3f in; with the wall"
        " AT their contour our planar fan would pass %+.1f %% mass and"
        " carry %+.1f %% inlet momentum -- the cut can hold THEIR MASS or"
        " THEIR WALL, not both, and the record holds the mass"
        % (float(P.X0) / S / IN, float(c["yw0"]) / S / IN, y_cut_them,
           dm, 100.0 * (F_th / F_rec - 1.0)))
    check("K-9 the two posings are NOT interchangeable: putting the wall"
          " on their contour at the cut moves the mass by %.1f percent,"
          " far beyond the 1 percent at which this row's thrust gates"
          " (O-2) are read -- the start line, not the contour, is what"
          " differs from theirs" % dm, abs(dm) > 1.0)
    rec_reach.update(mass_shift_pct_if_their_wall=dm)

    # ---- K-10: the owner's reading -- WAVINESS is what folds the net --
    # The characteristics see the wall's DIRECTION, not its radius. A
    # turn in the wall angle (a curvature sign change) is an
    # expansion/compression alternation, and the compression halves are
    # where the net crosses itself. Their own contour's printed angle
    # column is MONOTONE downstream of its dip; ours need not be, and a
    # six-knot spline in y pinned at a start radius that is not theirs
    # cannot help wiggling. Measured across the pool against the folded
    # fractions the same pool produced.
    def turns_of(W):
        _, _, ssl_ = P.wall_stations(np.asarray(W, float), c)
        a_ = np.degrees(np.arctan(np.asarray(ssl_)))
        return int((np.diff(np.sign(np.diff(a_))) != 0).sum()), a_

    # downstream of their own angle dip (the prescribed throat arc):
    # the rows after the steepest, where their contour is the optimum's
    i_dip = int(np.argmin(tab2[:, 2]))
    t_them = int((np.diff(np.sign(np.diff(tab2[i_dip:, 2]))) != 0).sum())
    say("   THEIR OWN Table 2 (their printed angle column, downstream of"
        " its dip): %d turns -- monotone" % t_them)
    wav = []
    for nm, r in got.items():
        tn, a_ = turns_of(r["W"])
        wav.append((nm, tn, r["frac"]))
        say("   %-26s %d turn(s) in the wall angle (%+.1f..%+.1f deg),"
            " folded %.2f %%" % (nm, tn, a_.min(), a_.max(), r["frac"]))
    rec_wav = [dict(design=nm, turns=tn, folded_pct=fr) for nm, tn, fr in wav]
    inc_t = [tn for nm, tn, _ in wav if nm.startswith("fan")][0]
    clean = [fr for nm, tn, fr in wav if tn == 0]
    wavy = [fr for nm, tn, fr in wav if tn > 0]
    check("K-10 WAVINESS is what folds the net (the owner's reading): the"
          " incumbent turns %d times and folds %.2f percent, while every"
          " design with a turn folds (%s percent) -- and THEIR OWN contour"
          " is monotone (%d turns), so the waviness is the posing's, not"
          " the paper's"
          % (inc_t, max(clean) if clean else -1.0,
             "/".join("%.1f" % f for f in sorted(wavy)), t_them),
          inc_t == 0 and clean and max(clean) == 0.0
          and bool(wavy) and min(wavy) > 0.0 and t_them == 0)

    rec = dict(case=CASE, base_model=base, K=P.K_ST, N=P.N_ROW,
               reach=rec_reach, waviness=rec_wav,
               designs={nm: dict(J_lbf=r["J"] / S / S / LBF,
                                 cert=float(r["out"]["cert_worst"]),
                                 where=str(r["out"]["cert_where"]),
                                 resolved=r["n_res"], folded=r["n_neg"],
                                 folded_pct=r["frac"])
                        for nm, r in got.items()},
               refined=dict(K=K2, N=N2, cert=float(t2["out"]["cert_worst"]),
                            resolved=t2["n_res"], folded=t2["n_neg"],
                            folded_pct=t2["frac"]))
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(
        ART, "class_%s_%s.json" % (CASE, base)), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                           time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage throat: THEIR throat, from their own table and text
# ----------------------------------------------------------------------
def throat():
    """What the paper gives about its own throat, read as numbers of
    record, and whether our series kernel can be posed on it.

    p. 1586: "a mean radius of curvature at the throat of 0.705 in., a
    downstream radius of curvature of 0.5 in., and a length from point
    T to point D of 12.0 in."; p. 1585: the plug curvature downstream of
    the start-line point A is PRESCRIBED so that no corner arises at T,
    where the optimised contour begins, T always downstream of A; the
    start line is always A -> E (the cowl lip). Table 2's nine crowded
    rows at the foot are that prescribed arc, and they are checked here
    against the text (known answers of the transcription) before the
    throat's Dutton parameter R_c is read from the paper's OWN mean
    radius -- not from the downstream arc, which is what the S32 first
    reading did (R_c ~ 1 from rho 0.5 in: corrected here)."""
    t00 = time.time()
    say("== [F3] Humphreys 1971, twin: THEIR throat from their own table"
        " and text [X-HMPH] (stage throat) ==")
    import a1_annular_kernel as AK
    tab = np.array(TABLES["table2_optimum_lip7.55_inj-34"])
    x, y, th = tab[:, 0], tab[:, 1], np.radians(tab[:, 2])
    prec = TABLES["_table_precision_in"]
    rho_paper = TABLES["_downstream_radius_in"]
    R_mean = TABLES["_throat_mean_radius_in"]
    lip_prec = TABLES["_lip_precision_in"]

    # ---- T-1: the crowded rows are a circular arc of the paper's radius
    ds = np.hypot(np.diff(x), np.diff(y))
    dth = np.abs(np.diff(th))
    rho_k = ds / dth                              # radius, interval by interval
    band_rho = A1.K_RICH * (2.0 * prec / ds[0])   # ds known to 2 prec
    n_arc = 1
    while (n_arc < len(rho_k)
           and abs(rho_k[n_arc] / rho_k[0] - 1.0) <= band_rho):
        n_arc += 1
    rho = float(np.mean(rho_k[:n_arc]))
    say("   the foot: %d consecutive intervals turn at constant radius"
        " %.4f in (spread %.1e, band %.1e) from theta %+.2f to %+.2f deg"
        % (n_arc, rho, float(rho_k[:n_arc].max() / rho_k[:n_arc].min() - 1.0),
           band_rho, np.degrees(th[0]), np.degrees(th[n_arc])))
    check("T-1 the arc at the foot IS the paper's prescribed downstream"
          " radius: %.4f in against 0.5 in (band %.1e in)"
          % (rho, A1.K_RICH * rho * 2.0 * prec / ds[0]),
          abs(rho - rho_paper) <= A1.K_RICH * rho * 2.0 * prec / ds[0])

    # ---- T-2: the arc ends at T, and T -> D is their 12.0 in ------------
    xT, yT = float(x[n_arc]), float(y[n_arc])
    LTD = float(x[-1] - xT)
    say("   T = (%.5f, %.5f) in at %+.2f deg; T -> D = %.4f in (paper: %.1f)"
        % (xT, yT, np.degrees(th[n_arc]), LTD, L_TD / IN))
    check("T-2 the arc ends at T and the length T -> D reproduces the"
          " paper's 12.0 in within its printed precision (%.4f, band %.2f)"
          % (LTD, TABLES["_length_TD_precision_in"]),
          abs(LTD - L_TD / IN) <= TABLES["_length_TD_precision_in"])

    # ---- T-3: the start line A -> E is normal to the injection ---------
    E = np.array([0.0, R_OPT / IN])
    A = np.array([x[0], y[0]])
    normal = np.degrees(np.radians(TH_I_OPT) + np.pi / 2)   # 90 + injection
    h = float(np.hypot(*(E - A)))
    ang_AE = float(np.degrees(np.arctan2(E[1] - A[1], E[0] - A[0])))
    band_ang = A1.K_RICH * np.degrees(lip_prec / h)
    say("   start line A -> E: h = %.4f in, inclination %.2f deg from the"
        " axis (90 + injection = %.2f; band %.2f deg from the lip's"
        " printed precision)" % (h, ang_AE, normal, band_ang))
    check("T-3 A -> E is normal to their injection direction (%.2f vs"
          " %.2f deg)" % (ang_AE, normal),
          abs(ang_AE - (normal)) <= band_ang)
    # the alternative reading: h exactly 1.0 in puts the lip at
    E1 = A + 1.0 * np.array([np.cos(np.radians(normal)),
                             np.sin(np.radians(normal))])
    say("   (if h were exactly 1.0 in the lip would sit at (%.4f, %.4f) in:"
        " 7.55 printed to two decimals cannot tell)" % (E1[0], E1[1]))

    # ---- T-4: the throat's R_c from the paper's OWN mean radius ---------
    R_c = R_mean / h
    rc_from = AK.CASES["rc_converged_from"]
    rc_from = rc_from["value"] if isinstance(rc_from, dict) else rc_from
    say("   Dutton's R_c = (mean radius at the throat) / (separation) ="
        " %.3f / %.4f = %.3f -- whatever the split between the walls;"
        " the kernel's declared convergence domain starts at %.2f"
        % (R_mean, h, R_c, rc_from))
    check("T-4 the throat lies INSIDE the series kernel's declared"
          " convergence domain (R_c %.3f >= %.2f)" % (R_c, rc_from),
          R_c >= rc_from)

    # ---- T-5: the kernel's own convergence AT this throat --------------
    gam = GAMMA
    eta = float(os.environ.get("ANK_ETA", 2.0))
    d_m, R_i_m = h * IN, float(y[0]) * IN
    NY = AK.CASES["n_y_profile"]
    NY = NY["value"] if isinstance(NY, dict) else NY
    res = {}
    for label, rc_in, rc_out in (
            ("symmetric split, K 0", R_mean * IN, R_mean * IN),
            ("straight cowl, K 1", 0.5 * R_mean * IN, np.inf)):
        P = AK.throat_params(R_i_m, d_m, -TH_I_OPT, rc_in, rc_out, eta, gam)
        grid, fields, _ = AK.solve_kernel(P["y_i"], P["g1"], P["g2"],
                                          P["h1"], P["h2"], P["b1"], gam, eta)
        ys = np.linspace(grid.y_i, grid.y_o, NY)
        M0, W0 = {}, {}
        for nt in (1, 2, 3):
            u0, v0 = AK.series_uv(grid, fields, P["eps"], gam,
                                  np.zeros(NY), ys, nt)
            q2 = u0 ** 2 + v0 ** 2
            M0[nt] = np.sqrt(q2) / np.sqrt(0.5 * (gam + 1.0)
                                           - 0.5 * (gam - 1.0) * q2)
            W0[nt] = AK.mass_ratio(grid, fields, P["eps"], gam, 0.0, nt)
        d12 = float(np.max(np.abs(M0[2] - M0[1])))
        d23 = float(np.max(np.abs(M0[3] - M0[2])))
        zs3 = AK.sonic_line(grid, fields, P["eps"], gam, ys, 3)
        zl = float(np.nanmax(zs3))
        ul, vl = AK.series_uv(grid, fields, P["eps"], gam,
                              np.full(NY, zl), ys, 3)
        ql = ul ** 2 + vl ** 2
        Ml = np.sqrt(ql) / np.sqrt(0.5 * (gam + 1.0) - 0.5 * (gam - 1.0) * ql)
        thl = np.degrees(np.arctan2(vl, ul))
        Wl = AK.mass_ratio(grid, fields, P["eps"], gam, zl, 3)
        say("   %-22s R_c %.3f eps %.3f y_i %.2f K %.2f: M(x=0) by terms"
            " %.3f/%.3f/%.3f..%.3f, |M2-M1| %.4f |M3-M2| %.4f (ratio %.2f);"
            " W/W* %.4f/%.4f/%.4f; first all-supersonic line at x %+.3f d:"
            " M %.3f..%.3f, theta %+.1f..%+.1f deg, W/W* %.4f"
            % (label, P["R_c"], P["eps"], P["y_i"], P["K"],
               M0[1].mean(), M0[2].mean(), M0[3].min(), M0[3].max(),
               d12, d23, d23 / d12 if d12 > 0 else float("nan"),
               W0[1], W0[2], W0[3], zl * P["K"] * P["eps"] ** 0.5,
               Ml.min(), Ml.max(), thl.min(), thl.max(), Wl))
        res[label] = dict(d12=d12, d23=d23, W3=W0[3], Ml=(Ml.min(), Ml.max()),
                          thl=(thl.min(), thl.max()), R_c=P["R_c"],
                          zl=zl * P["K"] * P["eps"] ** 0.5)
    r0 = res["symmetric split, K 0"]
    check("T-5 at THEIR throat the series still converges on the throat-plane"
          " Mach (third term %.4f below the second %.4f, ratio %.2f): the"
          " truncation band is the ratio, declared" % (r0["d23"], r0["d12"],
                                                       r0["d23"] / r0["d12"]),
          r0["d23"] < r0["d12"])

    # ---- T-6: their mass against the choked 1-D mass of A -> E ---------
    ybar = 0.5 * (float(y[0]) + R_OPT / IN) * IN
    area = 2.0 * np.pi * ybar * d_m
    mstar = (area * P0 * np.sqrt(gam / (RG * T0))
             * (2.0 / (gam + 1.0)) ** (0.5 * (gam + 1.0) / (gam - 1.0)))
    Cd = MDOT / mstar
    lo, hi = AK.CASES["discharge_band"]["value"] \
        if isinstance(AK.CASES["discharge_band"], dict) \
        else AK.CASES["discharge_band"]
    say("   the surface of revolution of A -> E: %.2f in^2; choked 1-D mass"
        " through it %.2f lbm/s; THEIR 148.08 lbm/s is C_d = %.4f of it"
        " (the kernel's own W/W* through the throat plane: %.4f / %.4f for"
        " the two splits; a smooth throat discharges %.2f..%.2f)"
        % (area / IN ** 2, mstar / LBM, Cd, r0["W3"],
           res["straight cowl, K 1"]["W3"], lo, hi))
    check("T-6 their stated mass is a physical discharge of THIS throat"
          " line (C_d %.4f inside the smooth-throat band %.2f..%.2f)"
          % (Cd, lo, hi), lo <= Cd <= hi)

    rec = dict(rho_arc_in=rho, n_arc=n_arc, T_in=[xT, yT], L_TD_in=LTD,
               h_in=h, angle_AE_deg=ang_AE, R_c=R_c, rc_converged_from=rc_from,
               kernel={k: {kk: (list(vv) if isinstance(vv, tuple) else vv)
                           for kk, vv in v.items()} for k, v in res.items()},
               area_in2=area / IN ** 2, mstar_lbm_s=mstar / LBM, Cd=Cd)
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(ART, "throat_%s.json" % CASE), "w"),
              indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                           time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage kernel: the march from THEIR throat, on THEIR geometry
# ----------------------------------------------------------------------
def _char_start(CF, j, field_uv, rk4, to_wall, ywall, xw, sw, xE, yE, q_E,
                th_e, N, n_edge, hs, thf, Xm, Ym, ta, S):
    """The start line ON the march's column characteristic, stage kernel
    with HMPH_IVL=char (S33). plug_march builds each column bottom-up
    along a C+ (wall -> free edge; its rows are C- lines), so a start
    line of that family is parallel to the first column. Pieces, throat
    frame: (i) below the leading ray, the C+ through the kernel's field
    traced BACKWARD from the leading ray's point j to the plug wall;
    (ii) the corner fan's own C+ line j (its Goursat cells join point j
    of ray k-1 to point j of ray k along a C+), leading -> terminal ray;
    (iii) above the terminal ray, the free-jet triangle solved with the
    march's own interior and free-jet cells up to the jet boundary.
    Rows wall -> edge with a per-row abscissa (plug_march's x0 array)."""
    import a1_frame_march as FM
    import a1_plug_march as PM
    fan = np.array([r[j] for r in CF["rays"]])            # L ... T
    # (i) the kernel part: from L backward to the wall
    kp = [(float(fan[0, 0]), float(fan[0, 1]))]
    while kp[-1][1] > ywall(kp[-1][0]):
        kp.append(rk4(*kp[-1], -hs, +1.0))
    x_w, y_w = to_wall(kp)
    curve = np.array([(x_w, y_w)] + kp[-2::-1])           # wall ... L
    # (iii) the edge part: the FREE-JET TRIANGLE between the terminal ray
    # and the jet boundary, solved (not the S32 uniform wedge): for every
    # C+ line i <= j of the fan, from its terminal-ray point up through the
    # C- lines the jet boundary has reflected at its earlier edge points,
    # to its own edge point -- the march's own interior (bottom-up) and
    # free-jet cells, rotated frame. Line j's points are the edge rows.
    t_int, t_fj, _ = FM.make_cells_rot(1.0, thf, Ym)
    cert = [0.0]

    def solve(t, z0, p):
        z = t[0](z0, p, ta)
        sc = max(1.0, float(jnp.max(jnp.abs(z))))
        cert[0] = max(cert[0], float(t[2](z, p, ta))
                      / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc))
        return np.asarray(z, float)

    def mslope(pt, sgn):
        M_ = float(A1.state_q(jnp.float64(np.hypot(pt[2], pt[3])), ta)[5])
        return np.tan(np.arctan2(pt[3], pt[2]) + sgn * np.arcsin(1.0 / M_))

    edge = [np.array([xE, yE, q_E * np.cos(th_e), q_E * np.sin(th_e)])]
    lines = {}
    n_r = len(CF["rays"])
    for i in range(1, j + 1):
        pts = [np.asarray(CF["rays"][n_r - 1][i], float)]
        for m in range(1, i):
            pt1, pt2 = pts[-1], np.asarray(lines[i - 1][m], float)
            lp, lm = mslope(pt1, +1.0), mslope(pt2, -1.0)
            x4 = (pt2[1] - pt1[1] - lm * pt2[0] + lp * pt1[0]) / (lp - lm)
            z0 = jnp.array([x4, pt1[1] + lp * (x4 - pt1[0]),
                            0.5 * (pt1[2] + pt2[2]), 0.5 * (pt1[3] + pt2[3])])
            pts.append(solve(t_int, z0, jnp.concatenate(
                [jnp.asarray(pt1), jnp.asarray(pt2)])))
        pt1, pt3 = pts[-1], edge[-1]
        th3 = float(np.arctan2(pt3[3], pt3[2]))
        dx = max(float(pt1[0]) - float(pt3[0]), hs)
        z = solve(t_fj, jnp.array([pt3[0] + dx, pt3[1] + dx * np.tan(th3), th3]),
                  jnp.concatenate([jnp.asarray(pt1), jnp.asarray(pt3),
                                   jnp.array([q_E])]))
        edge.append(np.array([z[0], z[1], q_E * np.cos(z[2]),
                              q_E * np.sin(z[2])]))
        pts.append(edge[-1])
        lines[i] = pts
    tri = np.array(lines[j][1:])                            # above T_j
    xC, yC, uC, vC = tri[:, 0], tri[:, 1], tri[:, 2], tri[:, 3]
    n_edge = len(tri)
    # (i) resampled by arc length: as many kernel rows as the S32 cut's
    # whole start line (N), the kernel part carrying the bulk of the mass
    nA = N
    sl_ = np.concatenate([[0.0], np.cumsum(np.hypot(np.diff(curve[:, 0]),
                                                    np.diff(curve[:, 1])))])
    sa = np.linspace(0.0, sl_[-1], nA, endpoint=False)
    xA, yA = np.interp(sa, sl_, curve[:, 0]), np.interp(sa, sl_, curve[:, 1])
    uA, vA = [np.array(v, float) for v in field_uv(xA, yA)]
    th_field_w = float(np.degrees(np.arctan2(vA[0], uA[0])))
    vA[0] = float(np.interp(x_w, xw, sw)) * uA[0]          # the wall row on the wall
    say("   the wall row: the kernel's own flow angle there %+.2f deg, the wall's"
        " %+.2f deg (the row is reset to the wall)"
        % (th_field_w, float(np.degrees(np.arctan(np.interp(x_w, xw, sw))))))
    xs = np.concatenate([xA, fan[:, 0], xC])
    ys = np.concatenate([yA, fan[:, 1], yC])
    us = np.concatenate([uA, fan[:, 2], uC])
    vs = np.concatenate([vA, fan[:, 3], vC])
    if not np.all(np.diff(ys) > 0.0):
        bad = np.where(np.diff(ys) <= 0.0)[0]
        raise ValueError("start-line rows not ordered at segments %s (kernel"
                         " rows 0..%d, fan %d..%d, triangle %d..%d); y there %s"
                         % (bad.tolist(), nA - 1, nA, nA + len(fan) - 1,
                            nA + len(fan), len(ys) - 1,
                            np.array2string(ys[max(0, bad[0] - 2):bad[-1] + 3],
                                            precision=5)))
    Xr, Yr, Ur, Vr = FM.to_record(xs, ys, us, vs, thf, Xm, Ym)
    md, F = PM.col_fluxes(np.stack([Xr, Yr, Ur, Vr], 1), ta, PA, 1.0)
    md = abs(float(md))
    nf = len(fan)
    shares = []
    for lo_, hi_ in ((0, nA + 1), (nA, nA + nf), (nA + nf - 1, len(ys))):
        m_, _ = PM.col_fluxes(np.stack([Xr[lo_:hi_], Yr[lo_:hi_], Ur[lo_:hi_],
                                        Vr[lo_:hi_]], 1), ta, PA, 1.0)
        shares.append(abs(float(m_)) / md)
    # the line's alignment with the local C+ (theta + mu, segment means)
    Ms = np.asarray(A1.state_q(jnp.asarray(np.hypot(us, vs)), ta)[5])
    cpd = np.arctan2(vs, us) + np.arcsin(1.0 / np.maximum(Ms, 1.0))
    dev = np.degrees(np.abs(np.arctan2(np.diff(ys), np.diff(xs))
                            - 0.5 * (cpd[1:] + cpd[:-1])))
    parts = (dev[:nA], dev[nA:nA + nf - 1], dev[nA + nf - 1:])
    worst = [float(d.max()) if d.size else 0.0 for d in parts]
    say("   start line ON THE C+ (the march's column family): wall at x' %.4f"
        " in, top at x' %.4f in; %d kernel rows (M %.3f..%.3f), the fan's C+"
        " line %d (%d rows, M %.3f..%.3f), %d free-jet triangle rows (cells"
        " certified %.3f); worst misalignment with the local C+: kernel"
        " %.2e, fan %.2e, triangle %.2e deg; mass %.2f lbm/s (kernel %.3f,"
        " fan %.3f, triangle %.3f)"
        % (x_w / S / IN, xs[-1] / S / IN, nA, Ms[:nA].min(), Ms[:nA].max(), j,
           nf, Ms[nA:nA + nf].min(), Ms[nA:nA + nf].max(), n_edge, cert[0],
           worst[0], worst[1], worst[2], md / S / S / LBM, *shares))
    check("H-1 (char) the start line is supersonic on every row (M >= %.4f),"
          " runs wall -> edge along the C+ and its free-jet triangle is"
          " certified (%.3f)" % (Ms.min(), cert[0]),
          Ms.min() > 1.0 and cert[0] <= 1.0)
    return dict(x_start=float(x_w), start=(xs, ys, us, vs), md_in=md,
                F_in=float(F), n_edge=n_edge, shares=shares, misalign=worst,
                nA=nA, n_fan=nf)


def kernel():
    """The geometry-faithful twin: the annular throat kernel [X-ANKR]
    posed on Humphreys' own throat, its line handed to the march through
    the lip corner fan in a non-uniform field and the rotated-frame cells
    [X-FRMR], the plug wall being THEIR prescribed 0.5-in arc from A to T
    and THEIR Table 2 (read with their printed angles) from T to D. The
    cut holds their WALL; the mass is whatever their throat passes (stage
    throat: their stated mass exceeds it), so the reading of record is
    SPECIFIC thrust J / mdot against theirs (owner, 2026-09-22), with C_F
    on the surface of A -> E beside it.

    The throat's split between the walls -- the one datum the paper does
    not print -- is posed from what it does print: the plug wall's radius
    at A is the downstream arc's 0.5 in (the arc begins ON the start
    line), and the cowl's radius follows from their mean radius 0.705 in
    in the Moore-Hall (harmonic) sense, 1/rc_cowl = 2/R_mean - 1/rc_plug.
    R_c = R_mean / h = 0.703 either way; the split sets K. Declared."""
    t00 = time.time()
    say("== [F3] Humphreys 1971, twin: the march from THEIR throat on THEIR"
        " geometry [X-HMPH] (stage kernel) ==")
    os.environ.setdefault("A1_BASE_MODEL", "veen")
    import a1_annular_kernel as AK
    import a1_frame_march as FM            # the rotated cells, the corner fan
    import a1_plug_march as PM
    import a1_plug_margin as PMG
    from a1_freejet_unit import q_at_pa
    w = build_world(R_OPT)
    S, ta = w["S"], w["ta"]
    KD = FM.CASES["kernel_defaults"]
    z_cut = float(os.environ.get("HMPH_ZCUT", 0.25))
    K = int(os.environ.get("HMPH_K", KD["K"]))
    N = int(os.environ.get("HMPH_N", KD["N"]))
    n_rays = int(os.environ.get("HMPH_NRAYS", KD["n_rays"]))
    n_pts = int(os.environ.get("HMPH_NPTS", KD["n_pts"]))
    gam, eta = GAMMA, float(os.environ.get("ANK_ETA", 2.0))

    # ---- their throat (stage throat's reading, recomputed) -----------
    tab = np.array(TABLES["table2_optimum_lip7.55_inj-34"])
    x, y, th = tab[:, 0], tab[:, 1], np.radians(tab[:, 2])
    prec = TABLES["_table_precision_in"]
    ds = np.hypot(np.diff(x), np.diff(y))
    rho_k = ds / np.abs(np.diff(th))
    band_rho = A1.K_RICH * (2.0 * prec / ds[0])
    n_arc = 1
    while (n_arc < len(rho_k)
           and abs(rho_k[n_arc] / rho_k[0] - 1.0) <= band_rho):
        n_arc += 1
    rho = float(np.mean(rho_k[:n_arc]))
    A, E = np.array([x[0], y[0]]), np.array([0.0, R_OPT / IN])
    h = float(np.hypot(*(E - A)))
    R_mean = TABLES["_throat_mean_radius_in"]
    # HMPH_RCSCALE scales BOTH radii (R_c with them, the split unchanged):
    # the attribution A/B against a throat where the series converges
    rc_scale = float(os.environ.get("HMPH_RCSCALE", 1.0))
    rc_plug = rho * rc_scale
    rc_cowl = rc_scale / (2.0 / R_mean - 1.0 / rho)
    # HMPH_WALL=parabola: the march follows the KERNEL'S OWN inner wall
    # (no field/wall mismatch at all) -- the attribution's control;
    # HMPH_LMAX_D: the march length in separations from the cut (default
    # to D)
    wall_mode = os.environ.get("HMPH_WALL", "theirs")
    lmax_d = os.environ.get("HMPH_LMAX_D")

    # ---- the plug wall, dense, in inches: the arc A -> T, then Table 2
    thA, thT = float(th[0]), float(th[n_arc])
    C = A + rho * np.array([np.sin(thA), -np.cos(thA)])   # centre, wall turning clockwise
    # the arc sampled at the same density as the rest of the wall
    n_arc_pts = max(2, int(FM.CASES["dense_wall_points"]
                           * (float(x[n_arc]) - float(x[0]))
                           / (float(x[-1]) - float(x[0]))))
    tt = np.linspace(thA, thT, n_arc_pts)
    arc_xy = C[None, :] + rho * np.stack([-np.sin(tt), np.cos(tt)], 1)
    xT = float(x[n_arc])
    xd = np.linspace(xT, float(x[-1]), FM.CASES["dense_wall_points"])[1:]
    os.environ["HMPH_TABLE"] = "hermite"           # their contour as they drew it
    yd = read_table(xd, tab)
    Xw = np.concatenate([arc_xy[:, 0], xd]) * IN * S
    Yw = np.concatenate([arc_xy[:, 1], yd]) * IN * S
    say("   their wall: the arc rho %.4f in from A (%+.2f deg) to T (%+.2f deg),"
        " then Table 2 (Hermite on their printed angles) to D; %d dense points"
        % (rho, np.degrees(thA), np.degrees(thT), len(Xw)))

    # ---- the throat frame: x' along the injection, origin mid A -> E ---
    thf = np.radians(TH_I_OPT)
    Xm, Ym = 0.5 * (A + E) * IN * S
    hh = 0.5 * h * IN * S
    d_fr = 2.0 * hh
    xw, yw, _, _ = FM.to_frame(Xw, Yw, np.zeros_like(Xw), np.zeros_like(Xw),
                               thf, Xm, Ym)
    if np.any(np.diff(xw) <= 0.0):
        raise ValueError("the wall is not single-valued in the throat frame")
    sw = np.gradient(yw, xw)
    if wall_mode == "parabola":
        slope_par = (float(np.tan(thA - thf))
                     if os.environ.get("HMPH_SLOPEA", "1") == "1" else 0.0)
        xw = np.linspace(0.0, float(xw[-1]), FM.CASES["dense_wall_points"])
        yw = -hh + slope_par * xw - 0.5 * xw ** 2 / (rc_plug * IN * S)
        sw = slope_par - xw / (rc_plug * IN * S)
        say("   WALL = the kernel's own parabola (rc %.3f in, slope %+.2f deg"
            " at the throat plane): the attribution control"
            % (rc_plug, np.degrees(np.arctan(slope_par))))
    if lmax_d is not None:
        keep = xw <= float(lmax_d) * d_fr
        xw, yw, sw = xw[keep], yw[keep], sw[keep]
        say("   march length capped at %.2f d from the throat plane" % float(lmax_d))
    xA, yA_, _, _ = FM.to_frame(A[0] * IN * S, A[1] * IN * S, 0.0, 0.0, thf, Xm, Ym)
    xE, yE_, _, _ = FM.to_frame(E[0] * IN * S, E[1] * IN * S, 0.0, 0.0, thf, Xm, Ym)
    say("   frame: rotated %+.2f deg, A -> (%.5f, %.5f) h, E -> (%.5f, %.5f) h"
        % (np.degrees(thf), xA / hh, yA_ / hh, xE / hh, yE_ / hh))

    # ---- the kernel on their throat --------------------------------
    # their plug wall at A is NOT tangent to the injection: -36.25 against
    # -34 deg, i.e. -2.25 deg in the throat frame, the arc already
    # diverging on the start line. throat_params carries a wall slope at
    # the throat; HMPH_SLOPEA=0 poses the kernel's wall tangent instead.
    slope_A = (float(np.tan(thA - thf))
               if os.environ.get("HMPH_SLOPEA", "1") == "1" else 0.0)
    P = AK.throat_params(float(y[0]) * IN, h * IN, -TH_I_OPT, rc_plug * IN,
                         rc_cowl * IN, eta, gam, slope_in=slope_A)
    grid, fields, _ = AK.solve_kernel(P["y_i"], P["g1"], P["g2"], P["h1"],
                                      P["h2"], P["b1"], gam, eta)
    eps, Kk = P["eps"], P["K"]
    say("   kernel: plug rc %.3f in (the arc) with wall slope %+.2f deg at A,"
        " cowl rc %.3f in (from their mean %.3f, harmonic), R_c %.3f, g2 %.3f"
        " h2 %.3f, eps %.3f, y_i %.2f; W/W* through the throat plane %.4f"
        " (3 terms)"
        % (rc_plug, np.degrees(np.arctan(slope_A)), rc_cowl, R_mean, P["R_c"],
           P["g2"], P["h2"], eps, P["y_i"],
           AK.mass_ratio(grid, fields, eps, gam, 0.0, 3)))
    xT_fr = float(FM.to_frame(float(x[n_arc]) * IN * S, float(y[n_arc]) * IN * S,
                              0.0, 0.0, thf, Xm, Ym)[0])
    say("   T (the arc's end) sits at x' %.4f in in the frame" % (xT_fr / S / IN))

    def kernel_uv(xp, yp):
        z = (np.asarray(xp, float) / d_fr) / (Kk * eps ** 0.5)
        yk = P["y_i"] + (np.asarray(yp, float) + hh) / d_fr
        u, v = AK.series_uv(grid, fields, eps, gam, z, yk)
        return u * w["as_"], v * w["as_"]

    x_cut = z_cut * Kk * eps ** 0.5 * d_fr
    say("   the truncated series' own mass: W/W* %.4f on the throat plane,"
        " %.4f on the cut (3 terms) -- the drift is the series' residual"
        % (AK.mass_ratio(grid, fields, eps, gam, 0.0, 3),
           AK.mass_ratio(grid, fields, eps, gam, z_cut, 3)))
    # the kernel's own parabola vs their arc at the cut: the wall the field
    # was solved on against the wall the march will follow
    y_par = -hh + slope_A * x_cut - 0.5 * x_cut ** 2 / (rc_plug * IN * S)
    s_par = slope_A - x_cut / (rc_plug * IN * S)
    yw0, sw0 = float(np.interp(x_cut, xw, yw)), float(np.interp(x_cut, xw, sw))
    say("   cut at z %.2f = x' %.4f in (%.3f d): the kernel's plug parabola"
        " y %.5f h, slope %+.2f deg; their arc there y %.5f h, slope %+.2f deg"
        " (gap %.2f deg)"
        % (z_cut, x_cut / S / IN, x_cut / d_fr, y_par / hh,
           np.degrees(np.arctan(s_par)), yw0 / hh, np.degrees(np.arctan(sw0)),
           np.degrees(np.arctan(sw0) - np.arctan(s_par))))

    # ---- the lip corner at E, through the kernel's field -------------
    q_E = q_at_pa(PA, ta, w["as_"])
    u_l, v_l = kernel_uv(xE, yE_)
    q_l, th_l = float(np.hypot(u_l, v_l)), float(np.arctan2(v_l, u_l))
    M_l = float(A1.state_q(jnp.float64(q_l), ta)[5])
    # HMPH_IVL (S33): "cut" = the start line on the vertical cut of the
    # throat frame (every S32 run, bit-identical); "char" = the start line
    # ON A CHARACTERISTIC of the march's own column family (C+: plug_march
    # builds each column bottom-up along a C+ from the wall to the free
    # edge, its rows being C- lines), through the SAME wall point as the
    # cut, so that the first marched column is parallel to the start line
    # and no wedge opens at the edge. Three pieces: the C+ through the
    # kernel's field from the wall to the leading ray; the corner fan's
    # own C+ line (its Goursat cells join ray k-1 to ray k along a C+);
    # the straight C+ of the uniform terminal state to the jet boundary
    # (the S32 wedge approximation, declared).
    ivl = os.environ.get("HMPH_IVL", "cut")
    if ivl == "char":
        hs = (x_cut - float(xE)) / n_pts           # the S32 fan's own step

        def cslope(xx, yy, sgn):
            u_, v_ = kernel_uv(xx, yy)
            M_ = float(A1.state_q(jnp.float64(np.hypot(u_, v_)), ta)[5])
            return np.tan(np.arctan2(v_, u_) + sgn * np.arcsin(1.0 / M_))

        def rk4(xx, yy, hx, sgn):
            k1 = cslope(xx, yy, sgn)
            k2 = cslope(xx + 0.5 * hx, yy + 0.5 * hx * k1, sgn)
            k3 = cslope(xx + 0.5 * hx, yy + 0.5 * hx * k2, sgn)
            k4 = cslope(xx + hx, yy + hx * k3, sgn)
            return xx + hx, yy + hx * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

        def ywall(xx):
            return float(np.interp(xx, xw, yw))

        def to_wall(pts):
            """the last two points bracket the wall: the secant crossing"""
            (xa, ya), (xb, yb) = pts[-2], pts[-1]
            fa, fb = ya - ywall(xa), yb - ywall(xb)
            xc = xa + (xb - xa) * fa / (fa - fb)
            return xc, ywall(xc)

        # the leading ray (the C- from the lip), tabulated to the wall
        lead = [(float(xE), float(yE_))]
        while lead[-1][1] > ywall(lead[-1][0]):
            lead.append(rk4(*lead[-1], hs, -1.0))
        lead = np.array(lead)
        # the C+ from the cut's wall point, forward to the leading ray
        cp = [(float(x_cut), yw0)]
        while cp[-1][1] < float(np.interp(cp[-1][0], lead[:, 0], lead[:, 1])):
            if cp[-1][0] > lead[-1, 0]:
                raise ValueError("the C+ from the cut misses the leading ray")
            cp.append(rk4(*cp[-1], hs, +1.0))
        (xa, ya), (xb, yb) = cp[-2], cp[-1]
        fa = ya - float(np.interp(xa, lead[:, 0], lead[:, 1]))
        fb = yb - float(np.interp(xb, lead[:, 0], lead[:, 1]))
        x_L = xa + (xb - xa) * fa / (fa - fb)
        y_L = float(np.interp(x_L, lead[:, 0], lead[:, 1]))
        u_L, v_L = kernel_uv(x_L, y_L)
        M_L = float(A1.state_q(jnp.float64(np.hypot(u_L, v_L)), ta)[5])
        say("   char start: the C+ from the cut's wall point meets the leading"
            " ray at x' %.4f in (%.3f d, z %.2f), y' %+.3f h: kernel M %.3f,"
            " theta' %+.2f deg, C+ direction %+.2f deg"
            % (x_L / S / IN, x_L / d_fr, x_L / d_fr / (Kk * eps ** 0.5),
               y_L / hh, M_L, np.degrees(np.arctan2(v_L, u_L)),
               np.degrees(np.arctan2(v_L, u_L) + np.arcsin(1.0 / M_L))))
        # the fan with the leading ray's last point AT that crossing and
        # every ray run to the same index: its C+ line n_pts is complete
        CF = FM.corner_fan(w, kernel_uv, (float(xE), float(yE_)), q_l, th_l,
                           x_L, thf, Ym, n_rays, n_pts, q_E, x_stop=np.inf)
    else:
        CF = FM.corner_fan(w, kernel_uv, (float(xE), float(yE_)), q_l, th_l,
                           x_cut, thf, Ym, n_rays, n_pts, q_E)
    th_e = CF["th_E"]
    say("   lip E: kernel state M %.4f, theta' %+.2f deg; corner fan %d rays"
        " to the cut (worst cell cert %.3f), terminal direction %+.2f deg"
        % (M_l, np.degrees(th_l), n_rays, CF["cert"], np.degrees(th_e)))
    check("H-0 the corner fan through the kernel's field certifies on every"
          " cell (%.3f)" % CF["cert"], CF["cert"] <= 1.0)

    # ---- the start line on the cut ----------------------------------
    x_start = float(x_cut)
    if ivl == "char":
        cs = _char_start(CF, n_pts, kernel_uv, rk4, to_wall, ywall, xw, sw,
                         xE, yE_, q_E, th_e, N,
                         int(os.environ.get("HMPH_NEDGE", 2)), hs, thf, Xm,
                         Ym, ta, S)
        x_start, start, md_in, F_in = cs["x_start"], cs["start"], cs["md_in"], cs["F_in"]
        ys, n_edge = cs["start"][1], cs["n_edge"]
    else:
        crs = [c_ for c_ in CF["cross"] if c_ is not None]
        y_lead = float(crs[0][1])
        y_edge = float(yE_) + (x_cut - float(xE)) * np.tan(th_e)
        nA = max(5, int(round(N * (y_lead - yw0) / (y_edge - yw0))))
        yA = np.linspace(yw0, y_lead, nA, endpoint=False)
        uA, vA = kernel_uv(np.full(nA, x_cut), yA)
        vA[0] = sw0 * uA[0]                              # the wall row on the wall
        yB = np.array([c_[1] for c_ in crs])
        uB = np.array([c_[2] for c_ in crs])
        vB = np.array([c_[3] for c_ in crs])
        # the uniform region between the fan's terminal ray and the jet
        # boundary (the streamline from the lip at theta_E): HMPH_NEDGE rows
        n_edge = int(os.environ.get("HMPH_NEDGE", 2))
        yC = np.linspace(yB[-1], y_edge, n_edge + 1)[1:]
        uC, vC = (np.full(n_edge, q_E * np.cos(th_e)),
                  np.full(n_edge, q_E * np.sin(th_e)))
        ys = np.concatenate([yA, yB, yC])
        us, vs = np.concatenate([uA, uB, uC]), np.concatenate([vA, vB, vC])
        assert np.all(np.diff(ys) > 0.0), "rows not ordered"
        start = (float(x_cut), ys, us, vs)
        X0r, Y0r, U0r, V0r = FM.to_record(np.full(len(ys), x_cut), ys, us, vs,
                                          thf, Xm, Ym)
        md_in, F_in = PM.col_fluxes(np.stack([X0r, Y0r, U0r, V0r], 1), ta, PA, 1.0)
        md_in = abs(float(md_in))
        MA = np.asarray(A1.state_q(jnp.asarray(np.hypot(uA, vA)), ta)[5])
        shares = []
        for lo_, hi_ in ((0, nA + 1), (nA, nA + len(yB)), (nA + len(yB) - 1, len(ys))):
            Xs, Ys, Us, Vs = FM.to_record(np.full(hi_ - lo_, x_cut), ys[lo_:hi_],
                                          us[lo_:hi_], vs[lo_:hi_], thf, Xm, Ym)
            m_, _ = PM.col_fluxes(np.stack([Xs, Ys, Us, Vs], 1), ta, PA, 1.0)
            shares.append(abs(float(m_)) / md_in)
        say("   mass on the cut by region: kernel rows %.3f, fan rows %.3f, uniform"
            " wedge (%d rows) %.3f of the whole" % (shares[0], shares[1], n_edge,
                                                    shares[2]))
        sl, _ = FM.spacelike(np.full(len(ys), x_cut), ys, us, vs, ta)
        say("   start line: %d kernel rows (M %.3f..%.3f, theta' %+.2f..%+.2f"
            " deg), %d fan rows, %d edge rows; space-like margin min %+.2f deg;"
            " mass through the cut %.2f lbm/s (their 148.08)"
            % (nA, MA.min(), MA.max(), np.degrees(np.arctan2(vA, uA)).min(),
               np.degrees(np.arctan2(vA, uA)).max(), len(yB), n_edge,
               np.degrees(sl.min()), md_in / S / S / LBM))
        check("H-1 the start line is space-like on every row (min margin %+.2f"
              " deg)" % np.degrees(sl.min()), sl.min() > 0.0)

    # ---- the stations along THEIR wall, from the cut to D ------------
    # HMPH_DS0/HMPH_GROW: the FIRST station spacing and its growth. The
    # bell's march from Sauer advances by the characteristics' own
    # intersection -- infinitesimal at M -> 1 -- and absorbs the start
    # data's residual over many tiny columns; this march advances to
    # PRESCRIBED stations, so the residual is absorbed in one step. The
    # ladder is the test of that difference.
    ds0 = float(os.environ.get("HMPH_DS0",
                               FM.CASES["station_clustering"][0])) * hh
    grow = float(os.environ.get("HMPH_GROW",
                                FM.CASES["station_clustering"][1]))
    ds_max = (xw[-1] - x_start) / K
    xs, dsn = [x_start], ds0
    while xs[-1] + dsn < xw[-1]:
        xs.append(xs[-1] + dsn)
        dsn = min(ds_max, dsn * grow)
    xq = np.array(xs[1:] + [float(xw[-1])])
    stations = (xq, np.interp(xq, xw, yw), np.interp(xq, xw, sw))

    # ---- the march, in the throat frame -----------------------------
    t0 = time.time()
    # the census floor is THIS march's station spacing (the stations
    # cluster from 0.05 h at the cut up to a uniform spacing: the median
    # is the uniform one), not the driver's module constants
    ell2 = float(np.median(np.diff(xq))) ** 2
    mg = PMG.margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=1.0,
                         f_edge=0.0, ell2=ell2)
    # HMPH_EDGEFILL (S33): rows seeded in the FIRST marched column between
    # its topmost interior point and the free edge (plug_march edge_fill:
    # a vertical start line is not a characteristic, so the first column
    # opens a wedge no cell computes). 0 = the S32 runs, bit-identical.
    n_fill = int(os.environ.get("HMPH_EDGEFILL", 0))
    out, sch = PM.plug_march(stations, start, float(q_E), w["tab"], 1.0,
                             cells=FM.make_cells_rot(1.0, thf, Ym), margin=mg,
                             edge_fill=n_fill)
    cert = float(out["cert_worst"])
    say("   stations: first %.2e h, growth %.3f, %d of them to %.2f d%s"
        % (ds0 / hh, grow, len(xq), (xq[-1] - x_start) / d_fr,
           "; %d rows seeded in the first column's edge wedge" % n_fill
           if n_fill else ""))
    say("   march: %d stations, cert %.3e (%d cells) at %s, %.1f s"
        % (len(xq), cert, int(out["cert_n"]), out.get("cert_where"),
           time.time() - t0))
    check("H-2 the march from their throat is Newton-certified (%.3e)" % cert,
          cert <= 1.0)

    # mass by column, in the record frame
    cols = {}
    for (j, i), pt in zip(out["mesh_keys"], out["mesh_pts"]):
        cols.setdefault(i, []).append((j, np.asarray(pt)))
    rows = []
    for i in sorted(cols):
        col = np.array([pt for j, pt in sorted(cols[i])])
        Xc, Yc, Uc, Vc = FM.to_record(col[:, 0], col[:, 1], col[:, 2], col[:, 3],
                                      thf, Xm, Ym)
        md, _ = PM.col_fluxes(np.stack([Xc, Yc, Uc, Vc], 1), ta, PA, 1.0)
        rows.append((i, abs(float(md)) / md_in - 1.0, len(col)))
    # a geometric ladder of columns (2^k - 1), the middle and the last
    picks = sorted(set([2 ** k - 1 for k in range(1, 8)]
                       + [len(rows) // 2, len(rows) - 1]))
    say("   mass vs the cut by column: " + ", ".join(
        "%d: %+.4f" % (rows[i][0], rows[i][1]) for i in picks if i < len(rows)))
    check("H-3 the mass is conserved from the cut to the last column (|dm/m|"
          " %.1e <= %.0e, the march's class)" % (abs(rows[-1][1]), FM.CT.MASS_TOL),
          abs(rows[-1][1]) <= FM.CT.MASS_TOL)

    # the class: the fold census of stage class on this march
    ms, dep, wh, fl = PMG.np_margin(out, sch, len(ys), 1.0, 0.0, ell2,
                                    with_depth=True, with_floor=True)
    orient = float(np.sign(np.median(ms)))
    ms, fl = np.asarray(ms) * orient, np.asarray(fl, bool)
    neg = (~fl) & (ms <= 0.0)
    say("   class: %d resolved cells, %d folded (%.2f %%)"
        % (int((~fl).sum()), int(neg.sum()), 100.0 * neg.sum() / max(1, (~fl).sum())))
    if neg.any():
        cols_f = np.array([i for (i, j) in wh])[neg]
        dep = np.asarray(dep)
        k0 = int(cols_f.min()) - PMG.JMIN
        say("   folded cells in columns %d..%d (of %d), depth from the top"
            " %.2f..%.2f; the first at station %d = x' %.3f in from the cut"
            % (cols_f.min(), cols_f.max(), len(rows), dep[neg].min(),
               dep[neg].max(), k0, (xq[min(k0, len(xq) - 1)] - x_start) / S / IN))
    check("H-4 the march is IN CLASS by the incumbent's standard: no folded"
          " resolved cell (%d)" % int(neg.sum()), int(neg.sum()) == 0)

    # ---- the thrust: F_in + the wall push + the base ------------------
    wall = np.asarray(out["wall"])
    Xw_, Yw_, Uw_, Vw_ = FM.to_record(wall[:, 0], wall[:, 1], wall[:, 2],
                                      wall[:, 3], thf, Xm, Ym)
    q = np.hypot(Uw_, Vw_)
    stt = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), ta)]
    pw, gw, Mw = stt[1], stt[4], stt[5]
    dy = Yw_[1:] - Yw_[:-1]
    wgt = 2.0 * np.pi * 0.5 * (Yw_[1:] + Yw_[:-1])
    push = float(np.sum((0.5 * (pw[1:] + pw[:-1]) - PA) * wgt * (-dy)))
    p_b = float(BP.p_base(pw[-1], Mw[-1], gw[-1], PA, os.environ["A1_BASE_MODEL"]))
    base = float(BP.base_term(p_b, Yw_[-1], PA))
    J = float(F_in) + push + base
    # the readings: J/mdot, C_F on the surface of A -> E, against theirs
    mdot_lbm = md_in / S / S / LBM
    J_lbf = J / S / S / LBF
    area_AE = 2.0 * np.pi * 0.5 * (float(y[0]) + R_OPT / IN) * h      # in^2
    mstar = (area_AE * IN ** 2 * P0 * np.sqrt(gam / (RG * T0))
             * (2.0 / (gam + 1.0)) ** (0.5 * (gam + 1.0) / (gam - 1.0))) / LBM
    Jm_ours, Jm_them = J_lbf / mdot_lbm, F_OPT / LBF / (MDOT / LBM)
    CF_ours = J_lbf / (P0 / PSI * area_AE)
    CF_them = F_OPT / LBF / (P0 / PSI * area_AE)
    say("   thrust: F_in %.0f + push %.0f + base %.0f = J %.1f lbf on %.2f lbm/s"
        " (their 32,881 on 148.08); base radius y_D %.3f in (their 0.954)"
        % (float(F_in) / S / S / LBF, push / S / S / LBF, base / S / S / LBF,
           J_lbf, mdot_lbm, Yw_[-1] / S / IN))
    say("   J/mdot: ours %.2f, theirs %.2f lbf s/lbm (%+.2e); C_F on A -> E:"
        " ours %.4f, theirs %.4f (%+.2e); our discharge %.4f of the choked"
        " 1-D of A -> E (theirs %.4f)"
        % (Jm_ours, Jm_them, Jm_ours / Jm_them - 1.0, CF_ours, CF_them,
           CF_ours / CF_them - 1.0, mdot_lbm / mstar, MDOT / LBM / mstar))
    lo, hi = AK.CASES["discharge_band"]
    check("H-5 the mass their throat passes through our cut is a physical"
          " discharge (%.4f of the choked 1-D, band %.2f..%.2f)"
          % (mdot_lbm / mstar, lo, hi), lo <= mdot_lbm / mstar <= hi)
    check("H-6 the SPECIFIC thrust reproduces theirs within the thrust class"
          " (%+.2e vs %.0e; their shear 0.2 percent not in ours)"
          % (Jm_ours / Jm_them - 1.0, THRUST_TOL),
          abs(Jm_ours / Jm_them - 1.0) <= THRUST_TOL)

    rec = dict(z_cut=z_cut, x_cut_in=x_cut / S / IN, K=len(xq), N=len(ys),
               rc_plug_in=rc_plug, rc_cowl_in=rc_cowl, R_c=P["R_c"], Kasym=P["K"],
               eps=eps, M_lip=M_l, th_E_deg=float(np.degrees(th_e)),
               fan_cert=CF["cert"], cert=cert, where=str(out.get("cert_where")),
               mass_last=rows[-1][1], folded=int(neg.sum()),
               resolved=int((~fl).sum()), J_lbf=J_lbf, mdot_lbm=mdot_lbm,
               F_in_lbf=float(F_in) / S / S / LBF, push_lbf=push / S / S / LBF,
               base_lbf=base / S / S / LBF, y_D_in=float(Yw_[-1] / S / IN),
               J_over_m=Jm_ours, J_over_m_them=Jm_them, CF=CF_ours, CF_them=CF_them,
               discharge=mdot_lbm / mstar, mass_first=rows[1][1], ivl=ivl,
               wall_in=np.stack([Xw_ / S / IN, Yw_ / S / IN], 1).tolist(),
               p_w_over_p0=(pw / P0).tolist(), M_w=Mw.tolist())
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(
        ART, "kernel_%s_z%.2f_N%d_sl%s_e%d_r%d_%s_rc%.2f_ds%s%s.json"
        % (CASE, z_cut, N, os.environ.get("HMPH_SLOPEA", "1"), n_edge,
           n_rays, wall_mode, rc_scale,
           os.environ.get("HMPH_DS0", "def"),
           ("_ef%d" % n_fill if n_fill else "")
           + ("_char_eta%g" % eta if ivl == "char" else ""))), "w"), indent=1)
    # HMPH_TAG (S33): the same record under a caller-chosen name (the A/B
    # stage kab reads its four marches by tag; the name above omits K and
    # the march length, so capped and full marches would collide)
    if os.environ.get("HMPH_TAG"):
        json.dump(rec, open(os.path.join(
            ART, "kernel_%s.json" % os.environ["HMPH_TAG"]), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage kab: the A/B of the two start poses of stage kernel (S33)
# ----------------------------------------------------------------------
def kab():
    """The vertical cut and the start line ON the march's own
    characteristic (C+) are two poses of the SAME physical problem -- their
    throat, the same eta, the same wall point -- marched to D at two rungs
    (stage kernel with HMPH_TAG). Read downstream on THEIR wall, where both
    poses are valid, and graded by the resolution ladder's band on the
    DIFFERENCE (K_RICH x how much the finer rung moves it): the frame
    march's covariance pattern, the peer review's proposal (2026-09-22).
    The first-column mass step alone cannot judge a pose -- it is the one
    functional the C+ start fixes by construction.

      AB-1 the cut's first-column step is STRUCTURAL (its first-order
           Richardson limit lies outside the band of the refinement's own
           move) and the C+ start's is smaller beyond both bands;
      AB-2 the two poses are the same problem downstream: beyond 2 d along
           their wall the wall-pressure difference stays inside its band
           at every station (a FAIL is a finding: one pose carries a real
           error the mass step did not show);
      AB-3 the difference's sign follows the mass each march carries at D.
    Readings: folded fractions, J / mdot against their stated mass and
    against the choked 1-D mass of their line A -> E (stage throat T-6)."""
    t00 = time.time()
    say("== [F3] Humphreys 1971, twin: the A/B of the two start poses"
        " [X-HMPH] (stage kab) ==")
    tags = os.environ.get(
        "HMPH_AB", "cut_toD_eta8_K160N41,cut_toD_eta8_K319N81,"
        "char_toD_eta8_K160N41,char_toD_eta8_K319N81").split(",")
    R = [json.load(open(os.path.join(ART, "kernel_%s.json" % t))) for t in tags]
    c1, c2, h1, h2 = R
    tab = np.array(TABLES["table2_optimum_lip7.55_inj-34"])
    d_in = float(np.hypot(0.0 - tab[0, 0], R_OPT / IN - tab[0, 1]))   # A -> E
    Jm_them = F_OPT / LBF / (MDOT / LBM)
    for t, r in zip(tags, R):
        mstar = r["mdot_lbm"] / r["discharge"]
        say("   %-24s start %.2f lbm/s (%.4f of 1-D), first column %+.4f, D"
            " %+.4f; folded %d of %d (%.2f %%); J/mdot %.2f (%+.2e vs their"
            " stated mass, %+.2e vs their thrust over the 1-D mass %.2f)"
            % (t, r["mdot_lbm"], r["discharge"], r["mass_first"],
               r["mass_last"], r["folded"], r["resolved"],
               100.0 * r["folded"] / max(1, r["resolved"]), r["J_over_m"],
               r["J_over_m"] / Jm_them - 1.0,
               r["J_over_m"] / (F_OPT / LBF / mstar) - 1.0, mstar))

    # ---- AB-1: the step at the first column -----------------------------
    def rich(a, b):
        """first-order limit and the band of the refinement's move"""
        return 2.0 * b - a, A1.K_RICH * abs(b - a)
    lc, bc = rich(c1["mass_first"], c2["mass_first"])
    lh, bh = rich(h1["mass_first"], h2["mass_first"])
    say("   first-column step, Richardson limit and band: cut %+.4f +- %.1e,"
        " C+ %+.4f +- %.1e" % (lc, bc, lh, bh))
    check("AB-1 the vertical cut's first-column step is structural (limit"
          " %+.4f outside its band %.1e) and the C+ start's is smaller beyond"
          " both bands (%.4f + %.1e < %.4f - %.1e)"
          % (lc, bc, abs(lh), bh, abs(lc), bc),
          abs(lc) > bc and abs(lh) + bh < abs(lc) - bc)

    # ---- AB-2 / AB-3: downstream on their wall ---------------------------
    def wall(r):
        w = np.array(r["wall_in"])
        sa = np.concatenate([[0.0], np.cumsum(np.hypot(np.diff(w[:, 0]),
                                                       np.diff(w[:, 1])))])
        return sa, np.array(r["p_w_over_p0"])
    diffs = []
    for a, b in ((c1, h1), (c2, h2)):
        sc, pc = wall(a)
        sh, ph = wall(b)
        sg = np.linspace(max(sc[0], sh[0]), min(sc[-1], sh[-1]),
                         len(a["wall_in"]))
        diffs.append((sg, np.interp(sg, sh, ph) - np.interp(sg, sc, pc),
                      np.interp(sg, sc, pc)))
    sg, d1, pc1 = diffs[0]
    d2 = np.interp(sg, diffs[1][0], diffs[1][1])
    m = sg >= sg[0] + 2.0 * d_in
    band = A1.K_RICH * np.abs(d2 - d1)
    out_ = np.abs(d2[m]) > band[m]
    k = int(np.argmax(np.abs(d2[m])))
    say("   beyond 2 d along their wall (%d stations): C+ minus cut in p_w/p_0"
        " mean %+.3e, worst %+.3e (%.2f %% of p_w) against its band %.1e"
        " there (max band %.1e); outside the band at %.0f %% of the stations"
        % (int(m.sum()), float(d2[m].mean()), float(d2[m][k]),
           100.0 * abs(float(d2[m][k])) / float(pc1[m][k]), float(band[m][k]),
           float(band[m].max()), 100.0 * out_.mean()))
    check("AB-2 the two poses are the same problem downstream: the wall"
          " pressure agrees within the ladder's band on the difference at"
          " every station beyond 2 d (outside at %.0f %%)" % (100.0 * out_.mean()),
          not out_.any())
    carried = [r["mdot_lbm"] * (1.0 + r["mass_last"]) for r in (c2, h2)]
    say("   the mass each march carries at D (finer rung): cut %.2f, C+ %.2f"
        " lbm/s" % tuple(carried))
    check("AB-3 the difference's sign follows the mass each march carries at"
          " D (C+ minus cut: pressure %+.2e, carried mass %+.2f lbm/s)"
          % (float(d2[m].mean()), carried[1] - carried[0]),
          np.sign(d2[m].mean()) == np.sign(carried[1] - carried[0]))
    rec = dict(tags=tags, richardson=dict(cut=[lc, bc], char=[lh, bh]),
               dp_mean=float(d2[m].mean()), dp_worst=float(d2[m][k]),
               band_worst=float(band[m][k]), band_max=float(band[m].max()),
               outside_frac=float(out_.mean()), carried_at_D=carried)
    json.dump(rec, open(os.path.join(ART, "kab_%s.json" % CASE), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


# ----------------------------------------------------------------------
# stage angle: the wall ANGLE as the independent variable (S33)
# ----------------------------------------------------------------------
def angle():
    """Item 1 of the S32 queue ([X-HMPH] K-10, the owner's reading:
    WAVINESS folds the net, and a spline in y pinned at a start that is
    not theirs can only follow their contour by wiggling). The driver's
    PSPL_PARAM=angle takes as design vector the INCREMENTS of the wall
    angle at the frozen knots, the slope linear between knots and
    integrated exactly to the contour, ordered by bounds (W >= 0):
    Humphreys' own independent variable (p. 1585), in which a turning
    wall is not representable. Before any walk:

      A-1 the two bases on THEIR contour from THEIR start T (the end of
          the prescribed arc, stage throat T-2), geometry only: their
          rows read as drawn (the Hermite through x, y and the printed
          angle) are the truth, the knot ladder m, 2m, 4m;
      A-2 the posing's inlet against their contour: the ordered class at
          OUR cut is bounded below by the straight wall at the cut's own
          flow angle -- how far above their contour that bound sits;
      A-3 the incumbent (the fan's streamline) in angle coordinates: the
          representation ladder (the driver's C-1 criterion), its march
          certified, in class, with no turn;
      A-4 the reverse-AD gradient against the FD ladder in the new
          coordinates (the driver's C-2 bands);
      A-5 ORDER => NO TURN on the march's own stations, for random
          ordered designs, with its rejector (one increment reversed must
          turn) and the contrast: y designs inside the stay class;
      A-6 the census of the angle-coordinate landings, once the legs
          have run (HMPH_STAGE=opt PSPL_PARAM=angle | angle_free)."""
    import jax
    t00 = time.time()
    st = _pose("angle", "the wall angle as the independent variable")
    w, S, F_ref = st["w"], st["S"], st["F_ref"]
    P, c, ta, W_ref, thE = st["P"], st["c"], st["ta"], st["W_ref"], st["thE"]
    param = P.PARAM
    if param == "y":
        say("   run with PSPL_PARAM=angle (or angle_free)")
        return False
    import a1_plug_margin as PMG          # imports the driver: after _pose
    rec = dict(case=CASE, param=param, K=P.K_ST, N=P.N_ROW, M=P.M_NODES)
    deg = lambda s: np.degrees(np.arctan(np.asarray(s)))      # noqa: E731
    M = P.M_NODES

    # ---- A-1: the two bases on THEIR contour, from THEIR T -------------
    tab2 = np.array(TABLES["table2_optimum_lip7.55_inj-34"])
    rows = tab2[int(np.argmin(tab2[:, 2])):]       # T..D (stage throat T-2)
    xT, yT, thT = rows[0]
    xd = np.linspace(xT, rows[-1, 0], P.K_ST + 1)  # station-dense sampling
    yh, sh = _hermite(xd, rows)
    t_them = n_turns(deg(sh))
    say("   their contour T..D as drawn (%d rows, the Hermite through x, y"
        " and their angle): %+.2f..%+.2f deg, %d turn(s)"
        % (len(rows), deg(sh).min(), deg(sh).max(), t_them))
    sl_T = float(np.tan(np.radians(thT)))
    rep = []
    for m in (M, 2 * M, 4 * M):
        xk = xT + (rows[-1, 0] - xT) * np.arange(1, m + 1) / m
        cA = dict(x0=xT, yw0=yT, slope0=sl_T, xk=xk)
        WA = np.diff(np.arctan(np.concatenate([[sl_T], _hermite(xk, rows)[1]])))
        yA, sA = [np.asarray(v) for v in P.angle_wall(WA, cA, xd)]
        xs = jnp.asarray(np.concatenate([[xT], xk]))
        ys = jnp.asarray(np.concatenate([[yT], _hermite(xk, rows)[0]]))
        Mc = P.spline_coeffs(xs, ys, sl_T)
        yY, sY = [np.asarray(v) for v in jax.vmap(
            lambda x: P.spline_eval(x, xs, ys, Mc))(jnp.asarray(xd))]
        r = dict(m=m, ang_dy=float(np.abs(yA - yh).max()),
                 ang_dth=float(np.abs(deg(sA) - deg(sh)).max()),
                 ang_turns=n_turns(deg(sA)),
                 y_dy=float(np.abs(yY - yh).max()),
                 y_dth=float(np.abs(deg(sY) - deg(sh)).max()),
                 y_turns=n_turns(deg(sY)))
        rep.append(r)
        say("   m %2d | ANGLE basis: max dy %.4f in, max dtheta %.3f deg,"
            " %d turn(s) | Y basis: max dy %.4f in, max dtheta %.3f deg,"
            " %d turn(s)" % (m, r["ang_dy"], r["ang_dth"], r["ang_turns"],
                             r["y_dy"], r["y_dth"], r["y_turns"]))
    rec["their_T"] = dict(turns_theirs=t_them, ladder=rep)
    check("A-1a their contour, read as drawn from T, is monotone in angle"
          " (%d turns) -- the premise of an ordered representation" % t_them,
          t_them == 0)
    check("A-1b the ORDERED ANGLE basis holds it from their own T with no"
          " turn at any rung and a representation error that falls across"
          " the ladder (%.4f -> %.4f in, the driver's C-1 factor 4)"
          % (rep[0]["ang_dy"], rep[-1]["ang_dy"]),
          all(r["ang_turns"] == 0 for r in rep)
          and rep[0]["ang_dy"] >= 4.0 * rep[-1]["ang_dy"])
    check("A-1c the Y basis from THEIR T at the record's m %d holds it"
          " without a turn too (%d) -- if so the waviness of K-8 is the"
          " pinned start's (the posing), not the basis's"
          % (M, rep[0]["y_turns"]), rep[0]["y_turns"] == 0)

    # ---- A-2: the posing's inlet against their contour -----------------
    # every ordered design leaves the cut at the flow angle and can only
    # turn toward the flow: the straight wall at theta_0 is the LOWEST
    # wall of the class, so where it sits above their contour no ordered
    # design can reach it
    xk_in = np.asarray(c["xk"]) / S / IN
    y_cone = (c["yw0"] + c["slope0"] * (np.asarray(c["xk"]) - P.X0)) / S / IN
    y_them = _hermite(xk_in, tab2)[0]
    gap = y_cone - y_them
    kcl = TABLES["_knot_class_in"]
    th_cut = float(deg(_hermite(np.array([P.X0 / S / IN]), tab2)[1])[0])
    say("   the inlet: at the cut (x %.3f in) the flow angle is %+.2f deg,"
        " their wall's %+.2f; the lowest ordered wall sits %s in above"
        " their contour at the knots"
        % (P.X0 / S / IN, float(deg(c["slope0"])), th_cut,
           np.array2string(gap, precision=3)))
    rec["inlet"] = dict(theta_cut_ours_deg=float(deg(c["slope0"])),
                        theta_cut_theirs_deg=th_cut, gap_in=gap.tolist())
    check("A-2 their contour is OUTSIDE the ordered class of this posing:"
          " the class's lowest wall passes %.3f in above it at the first"
          " knot, beyond the stay class %.2f in -- reaching it takes a"
          " TURN (the steepening their prescribed arc does upstream of our"
          " cut), so RE-1 on Table 2 needs their inlet, not a basis"
          % (gap[0], kcl), gap[0] > kcl)

    # ---- A-3: the incumbent in angle coordinates ------------------------
    ladder = (M, 2 * M, 4 * M, 8 * M)
    dev = {}
    for m in ladder:
        xk = P.X0 + (P.L - P.X0) * np.arange(1, m + 1) / m
        cm = dict(c, xk=xk)
        Wm = P.angle_W0(c["sx"], c["sy"], xk, c["slope0"])
        xq, yq, _ = P.wall_stations(Wm, cm)
        dev[m] = float(np.abs(np.asarray(yq)
                              - np.interp(np.asarray(xq), c["sx"],
                                          c["sy"])).max())
        say("   incumbent, m %2d: max |angle wall - streamline| %.4f in"
            % (m, dev[m] / S / IN))
    W0 = np.asarray(c["W0"], float)
    inc = _census(P, PMG, w, W0, c)
    J_inc = float(P.J_replay(jnp.asarray(W0), w, c, inc["sched"], ta))
    a_inc = deg(P.wall_stations(W0, c)[2])
    say("   incumbent (m %d): J %.1f lbf, cert %.4f, resolved %d, FOLDED %d,"
        " %d turn(s), angle %+.2f..%+.2f deg"
        % (M, J_inc / S / S / LBF, float(inc["out"]["cert_worst"]),
           inc["n_res"], inc["n_neg"], n_turns(a_inc), a_inc.min(),
           a_inc.max()))
    rec["incumbent"] = dict(dev_in={str(m): dev[m] / S / IN for m in ladder},
                            J_lbf=J_inc / S / S / LBF,
                            cert=float(inc["out"]["cert_worst"]),
                            resolved=inc["n_res"], folded=inc["n_neg"],
                            turns=n_turns(a_inc))
    check("A-3 the angle basis is dense on the incumbent (%.4f -> %.4f in"
          " across m %d..%d, factor >= 4) and the incumbent in angle"
          " coordinates marches certified (%.3f), in class (%d folded)"
          " and without a turn"
          % (dev[M] / S / IN, dev[ladder[-1]] / S / IN, M, ladder[-1],
             float(inc["out"]["cert_worst"]), inc["n_neg"]),
          dev[M] >= 4.0 * dev[ladder[-1]]
          and float(inc["out"]["cert_worst"]) <= 1.0
          and inc["n_neg"] == 0 and n_turns(a_inc) == 0)

    # ---- A-4: AD against the FD ladder, in angle coordinates -----------
    J0, g0 = P.J_and_grad(W0, w, c, ta, inc["sched"])
    fj = lambda z: P.J_replay(z, w, c, inc["sched"], ta)      # noqa: E731
    W0j = jnp.asarray(W0)
    ok4, rows4 = True, []
    for k in (0, len(g0) // 2, len(g0) - 1):
        v = jnp.zeros(len(g0)).at[k].set(1.0)
        scale = max(1.0, abs(float(W0[k])))
        fd, spread = P.fd_ladder(fj, W0j, v, scale)
        band = (A1.K_RICH * spread + A1.C_FLOOR * A1.EPS * abs(J0)
                / (P.FD_LADDER[-1] * scale))
        ok4 = ok4 and abs(fd - g0[k]) <= band
        rows4.append(dict(k=k, ad=float(g0[k]), fd=fd, band=band))
        say("   dJ/dW_%d: AD %+.6e  FD %+.6e  |d| %.3e  band %.3e"
            % (k, g0[k], fd, abs(fd - g0[k]), band))
    v = jnp.asarray(np.ones(len(g0)) / np.sqrt(len(g0)))
    fd_v, spread_v = P.fd_ladder(fj, W0j, v, 1.0)
    band_v = (A1.K_RICH * spread_v
              + A1.C_FLOOR * A1.EPS * abs(J0) / P.FD_LADDER[-1])
    dd = abs(float(np.dot(g0, np.asarray(v))) - fd_v)
    say("   <grad, v> %+.8e  FD_v %+.8e  |d| %.3e  band %.3e"
        % (float(np.dot(g0, np.asarray(v))), fd_v, dd, band_v))
    rec["adjoint"] = dict(components=rows4, directional=dd, band=band_v)
    check("A-4 the reverse-AD gradient in angle coordinates matches the"
          " central-FD ladder component-wise and in the directional"
          " identity, inside the ladder's own bands", ok4 and dd <= band_v)

    # ---- A-5: ORDER => NO TURN, the rejector, the y contrast -----------
    rng = np.random.default_rng(int(os.environ.get("HMPH_SEED", 1)))
    n_draw = 2 * M
    t_ord = [n_turns(deg(P.wall_stations(
        W0 * rng.uniform(0.0, 2.0, len(W0)), c)[2])) for _ in range(n_draw)]
    Wx = W0.copy()
    Wx[len(W0) // 2] = -W0[len(W0) // 2]
    t_rej = n_turns(deg(P.wall_stations(Wx, c)[2]))
    try:
        P.PARAM = "y"
        cy = P.build_case(w, thE=thE)
        kc = kcl * IN * S
        t_y = [n_turns(deg(P.wall_stations(
            np.asarray(cy["W0"]) + rng.uniform(-kc, kc, len(W0)), cy)[2]))
            for _ in range(n_draw)]
    finally:
        P.PARAM = param
    say("   %d random ORDERED designs: turns %s; one increment reversed:"
        " %d turn(s); %d y designs inside the stay class (+-%.2f in):"
        " turns %s" % (n_draw, t_ord, t_rej, n_draw, kcl, t_y))
    rec["order"] = dict(ordered=t_ord, reversed=t_rej, y_in_class=t_y)
    check("A-5 ORDER => NO TURN on the march's stations (%d/%d ordered"
          " draws turn-free) and the counter sees a reversal (%d turns);"
          " the y basis turns inside the class the walks call 'staying'"
          " in %d of %d draws" % (sum(t == 0 for t in t_ord), n_draw, t_rej,
                                  sum(t > 0 for t in t_y), n_draw),
          all(t == 0 for t in t_ord) and t_rej > 0
          and any(t > 0 for t in t_y))

    # ---- A-6: the census of the angle-coordinate landings --------------
    # ---- A-7: where their thrust comes from ---------------------------
    # J = F_in (the momentum through the cut, fixed by the imposed mass)
    # + the wall push + the base term, each read on the design's own
    # replay; the folds located by column as in stage class K-6. Their
    # Table 2 (y coordinates, the same grid) is the reference.
    base = os.environ["A1_BASE_MODEL"]
    land = {}
    x_last = float(np.asarray(c["xk"])[-2]) / S / IN    # the last interval

    def anatomy(nm, Wd, case):
        r = _census(P, PMG, w, Wd, case)
        J = float(P.J_replay(jnp.asarray(Wd), w, case, r["sched"], ta))
        pt = _j_parts(P, w, case, Wd, r["sched"], ta)
        sx = np.asarray(P.wall_stations(Wd, case)[0]) / S / IN
        al = deg(P.wall_stations(Wd, case)[2])
        cols = np.array([i for (i, j) in r["wh"]]) - PMG.JMIN
        fc = cols[r["neg"]]
        kmin = int(fc.min()) if fc.size else None
        d = dict(J_lbf=J / S / S / LBF, cert=float(r["out"]["cert_worst"]),
                 resolved=r["n_res"], folded=r["n_neg"], folded_pct=r["frac"],
                 turns=n_turns(al), angle_deg=[float(al.min()), float(al.max())],
                 F_in_lbf=pt["F_in"] / S / S / LBF,
                 push_lbf=pt["push"] / S / S / LBF,
                 base_lbf=pt["base"] / S / S / LBF,
                 sum_err=abs(pt["F_in"] + pt["push"] + pt["base"] - J) / abs(J),
                 y_D_in=pt["y_D"] / S / IN, p_D_pa=pt["p_D"] / P.PA,
                 M_D=pt["M_D"], p_b_pa=pt["p_b"] / P.PA,
                 x_first_fold_in=(float(sx[min(kmin, len(sx) - 1)])
                                  if kmin is not None else None),
                 push_downstream_lbf=(float(pt["seg"][kmin:].sum()) / S / S
                                      / LBF if kmin is not None else 0.0))
        say("   %-18s J %8.1f = F_in %.1f + push %7.1f + base %7.1f lbf"
            " | cert %.3f, FOLDED %4d of %4d (%.2f %%), first fold x %s in,"
            " %d turn(s) | y_D %.3f in, p_D/p_a %.3f, M_D %.3f, p_b/p_a %.3f"
            % (nm, d["J_lbf"], d["F_in_lbf"], d["push_lbf"], d["base_lbf"],
               d["cert"], d["folded"], d["resolved"], d["folded_pct"],
               "%.2f" % d["x_first_fold_in"] if kmin is not None else "-",
               d["turns"], d["y_D_in"], d["p_D_pa"], d["M_D"], d["p_b_pa"]))
        return d

    for prm in ("angle", "angle_free"):
        g = sorted(glob.glob(os.path.join(
            ART, "opt_%s_fan_%s_%s.json" % (CASE, base, prm))))
        if g:
            Wl = np.array(json.load(open(g[0]))["W_rad"])
            land[prm] = anatomy("landing " + prm, Wl, c)
            land[prm]["last_increment_deg"] = float(np.degrees(Wl[-1]))
    rec["landings"] = land
    if "angle" in land:
        la = land["angle"]
        check("A-6 the ORDERED landing is in class: no folded resolved cell"
              " (%d of %d) and no turn (%d)"
              % (la["folded"], la["resolved"], la["turns"]),
              la["folded"] == 0 and la["turns"] == 0)
        try:
            P.PARAM = "y"
            cy = P.build_case(w, thE=thE)
            tb = anatomy("their Table 2 (y)", np.asarray(W_ref, float), cy)
        finally:
            P.PARAM = param
        rec["their_table_y"] = tb
        # the three terms re-add to the replayed J: a sum of K_ST wall
        # segments in another order, so the band is K_ST round-offs
        band_s = A1.C_FLOOR * A1.EPS * P.K_ST
        check("A-7a the anatomy is the functional: F_in + push + base"
              " re-adds to the replayed J (worst %.1e, band %.1e)"
              % (max(la["sum_err"], tb["sum_err"]), band_s),
              max(la["sum_err"], tb["sum_err"]) <= band_s)
        dJ = la["J_lbf"] - tb["J_lbf"]
        dB = la["base_lbf"] - tb["base_lbf"]
        check("A-7b the ordered landing's excess over their contour (%+.1f"
              " lbf on the same grid) is the BASE term (%+.1f lbf; the wall"
              " push %+.1f): the walk sells push for base"
              % (dJ, dB, la["push_lbf"] - tb["push_lbf"]),
              dJ > 0.0 and dB > dJ)
        check("A-7c and it folds only where it buys it: the first folded"
              " column (x %.2f in) lies in the last knot interval (x >= %.2f"
              " in), where the wall turns %+.1f deg and the wall pressure"
              " climbs to %.2f p_a at D -- the base closure is fed a"
              " compressed, FOLDED state (p_b %.2f p_a)"
              % (la["x_first_fold_in"], x_last, la["last_increment_deg"],
                 la["p_D_pa"], la["p_b_pa"]),
              la["x_first_fold_in"] is not None
              and la["x_first_fold_in"] >= x_last)
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(
        ART, "angle_%s_%s_%s.json" % (CASE, base, param)), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t00))
    return NPASS[0] == NPASS[1]


STAGE = os.environ.get("HMPH_STAGE", "rao")

if __name__ == "__main__":
    sys.exit(0 if {"rao": rao, "opt": opt, "grad": grad,
                   "class": klass, "throat": throat,
                   "kernel": kernel, "angle": angle,
                   "kab": kab}.get(STAGE, rao)()
             else 1)

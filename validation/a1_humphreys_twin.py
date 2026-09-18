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
the background; hours.

Lengths are posed in LIP RADII (the record's YTIP convention, the
Chutkey twin's frame); the paper's inches are converted at the edges.
"""
import os
import sys
import json
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
MDOT = 148.08 * 0.45359237             # [kg/s]
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
    rec = dict(M_e=M_e, q_e=q_e, mdot_member=md_SI, F_full=F_full,
               push_beyond_D=push, y_D_in=y_D / S / IN, p_D_pa=p_D / PA,
               M_D=M_D, pb_pa=pb / PA, base=base, F_D=F_D, F_D_lbf=F_D / LBF,
               F_rao_lbf=34253.0, fan_cert=fc["worst"],
               wall_in=np.c_[sx / S / IN, sy / S / IN, p_w / PA, M_w].tolist(),
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


def opt():
    t00 = time.time()
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
    os.environ.pop("PSPL_FAN", None)
    import a1_config_compare as CC
    import a1_inlet_angle_opt as IA
    import a1_plug_spline_opt as P
    CC.PA = IA.PA = P.PA = PA
    IA.MI = 1.0002                        # the sonic lip of the paper
    IA.X0 = P.X0 = X0_R
    IA.X_END = max(IA.X_END, L)
    P.L = L
    P.CKPT = os.path.join(ART, "_ckpt_" + CASE)
    os.makedirs(P.CKPT, exist_ok=True)
    say("== [F3] Humphreys 1971, twin (B) case %s: the TR-SQP at their"
        " posing [X-HMPH] (stage opt) ==" % CASE)
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
    if START == "table":
        key = ("table3_rao_lip8.33_inj-58.5" if CASE == "rao"
               else "table2_optimum_lip7.55_inj-34")
        tab = np.array(TABLES[key])
        W0 = np.interp(np.asarray(c["xk"]) / S / IN, tab[:, 0], tab[:, 1]) * IN * S
        c["W0"] = W0
    say("   start radius y_w0 %.3f in (mass-set), F_in %.1f kN; start = %s;"
        " knots %s" % (c["yw0"] / S / IN, c["F_in"] / S / S / 1e3, START,
                       np.array2string(np.asarray(c["W0"]) / S / IN, precision=3)))
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
                                 maxiter_per_seg=8, verbose=1)
    out1, sched1 = P.march_record(W, w, c)
    J1 = float(P.J_replay(jnp.asarray(W), w, c, sched1, ta))
    say("   TR-SQP: %d records, J %.1f kN = %.0f lbf (%+.2e vs the paper's"
        " %.0f); cert %.3f; y_D %.3f in"
        % (n_rec, J1 / S / S / 1e3, J1 / S / S / LBF, J1 / S / S / F_ref - 1,
           F_ref / LBF, float(out1["cert_worst"]), float(W[-1]) / S / IN))
    check("O-1 the walk's best design is Newton-certified (%.3f)"
          % float(out1["cert_worst"]), float(out1["cert_worst"]) <= 1.0)
    check("O-2 the thrust reproduces the paper's within 1 percent (their"
          " shear is 0.2 percent; %+.2e)" % (J1 / S / S / F_ref - 1),
          abs(J1 / S / S / F_ref - 1) <= THRUST_TOL)
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
    tag = "%s_%s_%s" % (CASE, START, os.environ["A1_BASE_MODEL"])
    json.dump(rec, open(os.path.join(ART, "opt_%s.json" % tag), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return NPASS[0] == NPASS[1]


STAGE = os.environ.get("HMPH_STAGE", "rao")

if __name__ == "__main__":
    sys.exit(0 if {"rao": rao, "opt": opt}.get(STAGE, rao)() else 1)

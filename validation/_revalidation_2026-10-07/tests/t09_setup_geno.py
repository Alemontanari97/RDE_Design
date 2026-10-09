#!/usr/bin/env python3
"""T09 setup -- GENO RaoPlug decks for the Rao 1961 members (literature) and the axial-exit (ideal spike) case.

Gas: Rao's gamma = 1.23 (GENO's synthetic gas of its own raoplug_gamma123 case: M = 20 g/mol, T0 3500 K, P0 6 MPa;
every compared quantity is non-dimensional). Lip radius y_E = 1.
GENO's lip-fan scan covers 60 deg below theta_i (band_edges_slice: 240 steps of 0.25 deg), so the eps 10.69
member (66 deg of turning from M_i 1.10) uses M_i = 1.40 (56 deg). The ideal spike (theta_E = 0, ED down to the axis)
fails in both GENO solvers: Rao (rao61_ideal_e381) and the ideal plug (ideal5_e381) march into the axis and stop with
interior p <= 0 (y = 0.012 and 2e-4; c^2 v / y at y -> 0); the key mass_match does not exist in GENO (ignored). The
axial-exit case therefore ends the plug at R_D = 0.4 (axial_e381_RD04_mi15).
GENO's 1-DOF fixed-inlet mode takes the lip state (M_i, theta_i) and places the control-surface state (M_E, theta_E)
on ONE midpoint step of the Prandtl-Meyer ODE dq = -q tan(alpha) dtheta (Rao_m.f90 pmcompressionstep_cminus_solve,
read 2026-10-07). theta_i is therefore chosen here by emulating that step exactly, so that GENO's (M_E, theta_E) is
Rao's: M_i = 1.10 (GENO's own choice for this case), Me_fixed = M_E pins M_E.
  rao61_e381_pb0   M_E 2.4, theta_E -8.25 deg, p_b = 0                 (Rao's equations, exact end point)
  rao61_e381_pbR   same, p_b = the value that ends ED at Rao's printed R_D = 0.137 (ref/rao1961.py)
  rao61_e1069_pb0  M_E 3.2, theta_E -6.0 deg, p_b = 0
  rao61_e1069_pbR  same, ED ended at Rao's R_D = 0.126
  rao61_ideal_e381 ideal spike: theta_E = 0 at M_E = M_a(eps 3.81) -> uniform axial ED down to the axis (GENO fails)
  hth71_rao        Humphreys et al. 1971's Rao nozzle (ref/rao1961.hth_rao)
  axial_e381_RD04_mi15  axial exit, plug ended at R_D 0.4 (type 5 + external IVL), lip Mach 1.5
  rao61_e381_pbR_mi15   the eps 3.81 member at Rao's D, lip Mach 1.5 (the optimiser's posing, T10)
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import numpy as np                                 # noqa: E402
from scipy.optimize import brentq                  # noqa: E402
import exact                                       # noqa: E402
import geno_io                                     # noqa: E402
import rao1961 as R61                              # noqa: E402
import rv                                          # noqa: E402

GAM, MW, T0, P0, MI = 1.23, 20.0, 3500.0, 6.0e6, 1.10
Rg = 1000.0 * geno_io.RUNI_GENO / MW
G = exact.PerfectGas(GAM, Rg, T0, P0)


def geno_step(Mi, th_i, dth):
    """GENO's one-step PM fan (midpoint fixed point), emulated: returns M after turning by dth."""
    q0 = float(G.q(Mi))
    a0 = np.arcsin(1.0 / Mi)
    q, a, qc = q0, a0, np.inf
    for _ in range(200):
        q1 = q0 - q * np.tan(a) * dth
        if abs(q1 - qc) < 1e-12:
            break
        qc = q1
        q = 0.5 * (q1 + q0)
        a = np.arcsin(1.0 / float(G.M_q(q)))
    return float(G.M_q(q1))


def theta_i_for(M_E, th_E):
    f = lambda thi: geno_step(MI, thi, th_E - thi) - M_E     # noqa: E731
    return brentq(f, th_E + 1e-6, th_E + np.radians(80.0), xtol=1e-14)


def make(name, M_E, th_E_deg, pb_over_pc, constraint=None, Mi=1.10, mass_match=False, yt=None):
    global MI
    MI = Mi
    d = os.path.join(rv.RV, "geno", name)
    os.makedirs(d, exist_ok=True)
    th = geno_io.write_thermo(d, "g123", GAM, Rg, T0, P0)
    thi = theta_i_for(M_E, np.radians(th_E_deg))
    eps = 3.81
    Gm = exact.PerfectGas(th["gamma"], th["R"], T0, P0)
    cstar = float(np.sqrt(th["R"] * T0) / (np.sqrt(th["gamma"]) * (2.0 / (th["gamma"] + 1.0)) **
                                          ((th["gamma"] + 1.0) / (2.0 * (th["gamma"] - 1.0)))))
    solver = {"NI": 401, "moc_gen": ".true.", "pa": 0.0}
    rao = {"yE_plug": 1.0, "theta_i_plug": "%.12f" % np.degrees(thi), "Mi_plug": MI}
    if constraint is None:
        rao["Me_fixed"] = "%.12f" % M_E
    else:
        solver["constraint2"], solver["target2"] = constraint
    geno_io.write_input(d, {
        "GENO-nozzle": {"nozzle_type": 8, "case_geom": "axisymmetric", "thermoname": "thermo_g123.dat",
                        "frozenname": "g123.plt", "backend": 0, "yt": "%.10f" % (yt or 1.0 / np.sqrt(eps))},
        "GENO-solver": solver,
        "GENO-plug": {"Mi_plug": MI, "Rc_plug": 0.005, "eta_b": 0.0, "pb": "%.6f" % (pb_over_pc * P0),
                      "Tc_plug": T0, "pc_plug": P0, "cstar_plug": "%.6f" % cstar},
        "GENO-raoplug": rao})
    json.dump(dict(case=name, gas=[th["gamma"], th["R"], T0, P0], Mi=MI, theta_i_deg=float(np.degrees(thi)),
                   M_E=M_E, theta_E_deg=th_E_deg, pb_over_pc=pb_over_pc, constraint=constraint, thermo=th,
                   cstar=cstar, check_step_M=geno_step(MI, thi, np.radians(th_E_deg) - thi)),
              open(os.path.join(d, "case.json"), "w"), indent=1)
    print("%-18s M_E %.5f theta_E %+.3f deg -> theta_i %.8f deg ; p_b/P_c %.6f  %s" % (
        name, M_E, th_E_deg, np.degrees(thi), pb_over_pc, constraint or ""))


def make_ideal5(name, M_e, Mi=1.10):
    """GENO's ideal plug (nozzle_type 5): IVL = the straight uniform C- from the lip to the axis at M_e, the control
    surface of Rao's member theta_E = 0 (eq. 7: theta_D = 0 -> C3 = 0 -> theta = 0 on ED -> uniform, eq. 6); Phase 1
    marches upstream and truncates at the axis by mass. Lip radius 1: F_plug = pi (rho_e V_e^2) with p_a = p_e."""
    d = os.path.join(rv.RV, "geno", name)
    os.makedirs(d, exist_ok=True)
    th = geno_io.write_thermo(d, "g123", GAM, Rg, T0, P0)
    Gm = exact.PerfectGas(th["gamma"], th["R"], T0, P0)
    pe = float(Gm.p(M_e))
    F = np.pi * th["gamma"] * pe * M_e ** 2
    cstar = float(np.sqrt(th["R"] * T0) / (np.sqrt(th["gamma"]) * (2.0 / (th["gamma"] + 1.0)) **
                                          ((th["gamma"] + 1.0) / (2.0 * (th["gamma"] - 1.0)))))
    geno_io.write_input(d, {
        "GENO-nozzle": {"nozzle_type": 5, "case_geom": "axisymmetric", "thermoname": "thermo_g123.dat",
                        "frozenname": "g123.plt", "backend": 0},
        "GENO-solver": {"NI": 401, "moc_gen": ".true.", "pa": "%.6f" % pe},
        "GENO-plug": {"Mi_plug": Mi, "Me_plug": "%.12f" % M_e, "Rc_plug": 0.005, "eta_b": 0.0,
                      "F_plug": "%.6f" % F, "pb": "%.6f" % pe, "Tc_plug": T0, "pc_plug": P0,
                      "cstar_plug": "%.6f" % cstar}})
    json.dump(dict(case=name, gas=[th["gamma"], th["R"], T0, P0], Mi=Mi, M_e=M_e, p_a=pe, F_plug=F, thermo=th,
                   cstar=cstar), open(os.path.join(d, "case.json"), "w"), indent=1)
    print("%-18s type 5: M_i %.2f M_e %.5f p_a/P_c %.6f F_plug %.6e (lip radius 1)" % (name, Mi, M_e, pe / P0, F))


def make_axial5(name, M_e, R_D, Mi=1.10, NI=401):
    """Axial exit, plug ending at R_D: GENO's inverse-plug solver (nozzle_type 5) started from an external IVL
    (final_plug = 3) = Rao's control surface for theta_E = 0: by (7) C3 = R rho w^2 sin^2(theta) tan(alpha) = 0, so
    theta = 0 on all of ED, (6) gives w = const, (8) gives p_E = p_a: the straight C- from the lip E = (0, 1) at the
    Mach angle, uniform M_e, theta 0, ended at R = R_D (where its mass is the throat's). Base at p_a: thrust =
    mdot V_a, the bound of every contour (no axis: GENO's march diverges at y -> 0)."""
    d = os.path.join(rv.RV, "geno", name)
    os.makedirs(d, exist_ok=True)
    th = geno_io.write_thermo(d, "g123", GAM, Rg, T0, P0)
    Gm = exact.PerfectGas(th["gamma"], th["R"], T0, P0)
    pe, rho, V, T, a = (float(f(M_e)) for f in (Gm.p, Gm.rho, Gm.q, Gm.T, Gm.c))
    xD = (1.0 - R_D) * np.sqrt(M_e ** 2 - 1.0)
    with open(os.path.join(d, "ivl.dat"), "w") as fh:
        for i in range(NI):
            t = i / (NI - 1.0)
            fh.write("%.16e %.16e %.16e %.16e %.16e %.16e %.16e %.16e %.16e %.16e %.16e\n" % (
                t * xD, 1.0 - t * (1.0 - R_D), rho, V, 0.0, pe, a, T, a, M_e, th["gamma"]))
    F = np.pi * th["gamma"] * pe * M_e ** 2                       # lip radius 1 in GENO's Angelino sizing
    cstar = float(np.sqrt(th["R"] * T0) / (np.sqrt(th["gamma"]) * (2.0 / (th["gamma"] + 1.0)) **
                                          ((th["gamma"] + 1.0) / (2.0 * (th["gamma"] - 1.0)))))
    geno_io.write_input(d, {
        "GENO-nozzle": {"nozzle_type": 5, "case_geom": "axisymmetric", "thermoname": "thermo_g123.dat",
                        "frozenname": "g123.plt", "backend": 0},
        "GENO-solver": {"NI": NI, "moc_gen": ".true.", "pa": "%.6f" % pe},
        "GENO-plug": {"Mi_plug": Mi, "Me_plug": "%.12f" % M_e, "Rc_plug": 0.005, "eta_b": 0.0,
                      "F_plug": "%.6f" % F, "pb": "%.6f" % pe, "Tc_plug": T0, "pc_plug": P0,
                      "cstar_plug": "%.6f" % cstar, "final_plug": 3, "ivl_file_plug": "ivl.dat"}})
    json.dump(dict(case=name, gas=[th["gamma"], th["R"], T0, P0], Mi=Mi, M_e=M_e, R_D=R_D, x_D=xD, p_a=pe,
                   mdot=rho * V * np.pi * (1.0 - R_D ** 2), thermo=th, cstar=cstar),
              open(os.path.join(d, "case.json"), "w"), indent=1)
    print("%-18s type 5 + IVL: M_e %.5f, ED (0,1) -> (%.5f, %.2f), p_a/P_c %.6f" % (name, M_e, xD, R_D, pe / P0))


if __name__ == "__main__":
    r = R61.Rao1961(GAM)
    pbR = {}
    for key in ("e381", "e1069"):
        P = R61.PUB[key]
        m = r.member(P["M_E"], P["th_E"], n=200001)
        k = int(np.argmin(np.abs(m["R"] - P["R_D"])))
        M, thv = m["M"][k], m["theta"][k]
        p, rho, w, a = r._state(M)                       # gas with R = T0 = P0 = 1: pressures in P_c
        pbR[key] = float(p - 0.5 * rho * w ** 2 * np.tan(a) * np.sin(-2.0 * thv))
    make("rao61_e381_pb0", 2.4, -8.25, 0.0)
    make("rao61_e381_pbR", 2.4, -8.25, pbR["e381"])
    make("rao61_e1069_pb0", 3.2, -6.0, 0.0, Mi=1.40)
    make("rao61_e1069_pbR", 3.2, -6.0, pbR["e1069"], Mi=1.40)
    Ma = float(G.M_of_area(3.81))
    make("rao61_ideal_e381", Ma, 0.0, 0.0)
    make_ideal5("ideal5_e381", Ma)
    # axial exit with the plug ending off the axis: theta_E = 0 (uniform axial flow at p_a on ED), D where ED's mass
    # equals the throat's (GENO mass match, A* = pi yt^2): mdot = rho_a V_a pi (1 - R_D^2) -> yt^2 = (1 - R_D^2)/eps_a
    RD = 0.4
    # (lip Mach 1.1 here gives a near-sonic last internal C+: the model's march from it is uncertified, 1e16)
    # the optimiser's posings (T10) start from GENO's last internal C+; with M_i = 1.1 that line is near-sonic (Mach
    # angle 65-90 deg) and the march's cells degenerate (certificate 1e16, measured). M_i = 1.5 changes only GENO's
    # internal part: the field between ED and the M = 1.5 fan ray (hence the plug downstream of x_s) is the same.
    make("rao61_e381_pbR_mi15", 2.4, -8.25, pbR["e381"], Mi=1.5)
    # M_i 1.5 still fails for Rao's eps 3.81 plug: just past x_s the wall is at -44.1 deg with Mach angle 41.4 deg, so
    # the C+ columns are horizontal (theta + mu = -2.7 deg) and the wall cell's foot, parameterised by y on that column,
    # is singular (dx/dy -21.7, cond 9e13). M_i 2.0 moves x_s to where the wall is less steep.
    # (M_i 2.0 moves the bad cell into GENO's internal channel: wall -29.4 deg, Mach angle 30.9 deg; the rescue
    #  certifies both, see t10_rao_walk.py)
    # Humphreys, Thompson & Hoffman 1971: the Rao nozzle of their comparison (ref/rao1961.hth_rao: M_E, theta_E from
    # p_a = 14.7 psia and x_D = 11.51781 in with their base model; p_b is then a number)
    h = R61.hth_rao()
    make("hth71_rao", h["M_E"], h["th_E"], h["p_b"])
    make_axial5("axial_e381_RD04_mi15", Ma, RD, Mi=1.5)

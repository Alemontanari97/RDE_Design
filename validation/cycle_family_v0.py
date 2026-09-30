#!/usr/bin/env python3
"""CYCLEFAMILY v0 [X-CYCF] (plan item 5, case A of D6 Annex B; F2.ENGINE 2026-09-30 night; gates declared in
validation/PROGRESS_2026-09-30_F2ENGINE.md before this file was written).

A synthetic RDE outflow family from specs alone: the matched detonation cycle of Stechmann, Heister & Harroun
(JSR 2019; the chain of src/thrust/stechmann_nozzle.py, Cantera + SD Toolbox) gives the post-detonation
stagnation pressure P0, the fill pressure and the pressure ratio PR of the blowdown Pc(xi) = P0 PR^-xi over one
wave period (xi in [0, 1)), with T(xi) isentropic from T_CJ at the paper's gamma_s. The family = K sectors of
equal time (= equal angle in the frame turning with the wave); each sector carries the TIME MEAN of Pc and of T
over the sector. The gas of each phase: the equilibrium products at the phase's own stagnation state, then
FROZEN -- the design tool takes their frozen gamma and R at the extraction state (M_in), the CFD runs the same
composition with its tabulated thermo. Writes, under validation/_cycle_family/<tag>/:
  family_K<K>.json   the design tool's family (w, gamma, R, T0, P0, M, mdot, v = 0)      [TWOP_MU]
  gas_mean.json      the design tool's mean state (gamma, R, T0, P0, M_in, geno_run, T_tab)  [TWOP_GAS]
  phases_cfd.json    the CFD referee's phases (mach, T, p, Y by species name, gamma, R, T0, P0, w) + mean (index K)
usage: .venv-a1/bin/python validation/cycle_family_v0.py [--prop CH4] [--phi 1.0] [--pcp 20] [--ti 200] [--K 12]
       [--min 1.556] [--pa-atm 1.0] [--tag sdt_ch4_phi1_pcp20]"""
import argparse
import json
import os
import sys

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path[:0] = [ROOT, os.path.join(ROOT, "src"), os.path.join(ROOT, "src", "thrust")]
import stechmann_nozzle as SN                                    # noqa: E402
from st_core import Ik, cstar_fn                                  # noqa: E402

ATM = 101325.0
RU = 8314.462618
GENO_RUN = "/data10/falco/RDE/handoff/f3_2026-09-25/geno_rde/stech_run"   # the annulus geometry of the S42 posing (walls only)
OK = True


def check(name, cond, detail=""):
    global OK
    OK &= bool(cond)
    print("  [%s] %s%s" % ("PASS" if cond else "FAIL", name, (" -- " + detail) if detail else ""))
    return bool(cond)


def frozen_gas(mech, X0, T, P):
    """Equilibrium products at (T, P) from the fill composition X0, then frozen: composition (mass fractions), R,
    and a function gamma_frozen(T) = cp/cv of the frozen mixture."""
    import cantera as ct
    gas = ct.Solution(mech)
    gas.TPX = T, P, X0
    gas.equilibrate("TP")
    Y = {k: float(v) for k, v in gas.mass_fraction_dict().items() if v > 1e-12}
    R = RU / gas.mean_molecular_weight
    fro = ct.Solution(mech)

    def gam(Tq):
        fro.TPY = Tq, P, Y
        return float(fro.cp_mass / fro.cv_mass)
    return Y, float(R), gam


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--prop", default="CH4"); ap.add_argument("--phi", type=float, default=1.0)
    ap.add_argument("--pcp", type=float, default=20.0, help="mean chamber pressure of the CP twin [atm] (the paper's Pcp)")
    ap.add_argument("--ti", type=float, default=200.0); ap.add_argument("--K", type=int, default=12)
    ap.add_argument("--min", type=float, default=1.556, help="extraction Mach (the S42 posing)")
    ap.add_argument("--pa-atm", type=float, default=1.0)
    ap.add_argument("--tag", default=None)
    a = ap.parse_args()
    tag = a.tag or "sdt_%s_phi%g_pcp%g" % (a.prop.lower(), a.phi, a.pcp)
    out = os.path.join(HERE, "_cycle_family", tag)
    os.makedirs(out, exist_ok=True)
    print("== [F2a] CycleFamily v0 [X-CYCF]: %s phi %.2f, Pcp %.0f atm, Ti %.0f K, K %d, M_in %.3f, p_a %.2f atm ==" % (a.prop, a.phi, a.pcp, a.ti, a.K, a.min, a.pa_atm))
    # ---- the matched cycle (cached state if on file, else the chain)
    D = SN.load()
    key = SN.dkey(a.prop, int(a.pcp) if float(a.pcp).is_integer() else a.pcp, a.phi)
    st = D["states"].get(key) if isinstance(D.get("states"), dict) else None
    if st is None:
        st = SN.matched(a.prop, a.phi, a.ti, a.pcp)
    P0, PR, TCJ, gs = float(st["P0"]), float(st["PR"]), float(st["TCJ"]), float(st["gamma"])
    cstar0, DC = float(st["cstar0"]), float(st["DC"])
    print("   matched state %s: P0 %.4e Pa (%.2f atm), fill %.3f atm, PR %.3f, T_CJ %.1f K, gamma_s %.4f, R %.2f, c* %.1f, DC %+.4f"
          % (key, P0, P0 / ATM, P0 / PR / ATM, PR, TCJ, gs, float(st["R"]), cstar0, DC))
    lam = np.log(PR)
    e = (gs - 1.0) / gs

    def Pc(xi):
        return P0 * np.exp(-lam * xi)

    def Tc(xi):
        return TCJ * (Pc(xi) / P0) ** e
    # F-1 the cycle mean equals Pcp (1 + DC)
    xi = np.linspace(0.0, 1.0, 400001)
    pmean = np.trapezoid(Pc(xi), xi)
    check("F-1 cycle mean of Pc = Pcp (1 + DC): %.6e vs %.6e" % (pmean, a.pcp * ATM * (1 + DC)), abs(pmean / (a.pcp * ATM * (1 + DC)) - 1) < 1e-6)
    # F-2 sector means: analytic vs quadrature
    edges = np.linspace(0.0, 1.0, a.K + 1)
    P_sec = np.array([P0 * (np.exp(-lam * e0) - np.exp(-lam * e1)) / (lam * (e1 - e0)) for e0, e1 in zip(edges[:-1], edges[1:])])
    P_quad = np.array([np.trapezoid(Pc(np.linspace(e0, e1, 20001)), np.linspace(e0, e1, 20001)) / (e1 - e0) for e0, e1 in zip(edges[:-1], edges[1:])])
    check("F-2 the %d sector means integrate the exponential (analytic vs quadrature)" % a.K, np.max(np.abs(P_sec / P_quad - 1)) < 1e-9)
    T_sec = np.array([np.trapezoid(Tc(np.linspace(e0, e1, 20001)), np.linspace(e0, e1, 20001)) / (e1 - e0) for e0, e1 in zip(edges[:-1], edges[1:])])
    # F-3 mass per cycle (choked exit, mdot/A ~ Pc/c*(Pc)) equals the CP combustor's within the matched tolerance
    k = (gs + 1) / (2 * gs)
    mflux_det = P0 / cstar0 * Ik(PR, k)
    cpm = st["cpm"]
    mflux_cp = a.pcp * ATM / float(cpm["cstar"])
    check("F-3 mass per cycle = the CP combustor's: %.5e vs %.5e (rel %.2e <= 1e-2, the matched tolerance)" % (mflux_det, mflux_cp, abs(mflux_det / mflux_cp - 1)),
          abs(mflux_det / mflux_cp - 1) < 1e-2)
    # ---- the gas of every phase: equilibrium products at the phase's stagnation state, frozen
    mech, fuel, ox = SN._prop(a.prop, a.phi)
    import cantera as ct
    g0 = ct.Solution(os.path.join(ROOT, mech)); g0.set_equivalence_ratio(a.phi, fuel, ox)
    X0 = g0.mole_fraction_dict()
    phases = []
    for kk in range(a.K):
        Y, R, gam = frozen_gas(os.path.join(ROOT, mech), X0, float(T_sec[kk]), float(P_sec[kk]))
        # the extraction state at M_in: static T from the frozen gamma there (fixed point on gamma(T))
        gm = gam(float(T_sec[kk]))
        for _ in range(8):
            Ts = T_sec[kk] / (1 + 0.5 * (gm - 1) * a.min ** 2)
            gm = gam(float(Ts))
        ps = P_sec[kk] * (Ts / T_sec[kk]) ** (gm / (gm - 1))
        phases.append(dict(w=1.0 / a.K, gamma=gm, R=R, T0=float(T_sec[kk]), P0=float(P_sec[kk]), M=a.min, T=float(Ts), p=float(ps), Y=Y,
                           mdot=float(P_sec[kk] / cstar_fn(gm, R, float(T_sec[kk]))), v=0.0))
    ysum = max(abs(sum(p["Y"].values()) - 1) for p in phases)
    check("F-4 every phase: composition sums to one (worst %.1e) and frozen gamma in (1, 5/3): %.4f .. %.4f" % (ysum, min(p["gamma"] for p in phases), max(p["gamma"] for p in phases)),
          ysum < 1e-9 and all(1.0 < p["gamma"] < 5.0 / 3.0 for p in phases))
    # the mean state (time means of P0 and T0; the gas of that state)
    P0m, T0m = float(np.trapezoid(Pc(xi), xi)), float(np.trapezoid(Tc(xi), xi))
    Ym, Rm, gamm = frozen_gas(os.path.join(ROOT, mech), X0, T0m, P0m)
    gmm = gamm(T0m)
    for _ in range(8):
        Tsm = T0m / (1 + 0.5 * (gmm - 1) * a.min ** 2); gmm = gamm(float(Tsm))
    psm = P0m * (Tsm / T0m) ** (gmm / (gmm - 1))
    mean = dict(w=1.0, gamma=gmm, R=Rm, T0=T0m, P0=P0m, M=a.min, T=float(Tsm), p=float(psm), Y=Ym, mdot=float(P0m / cstar_fn(gmm, Rm, T0m)), v=0.0)
    # F-5 the contract by construction: one rigid periodic wave (a synthetic probe record through the monitor), supersonic extraction
    sys.path.insert(0, HERE)
    import single_wave_monitor as SW
    T_per = 235.5e-6                                                   # any period: the family fixes the pattern, not the speed
    t = np.arange(0.0, 8 * T_per, T_per / 2000)
    th = np.array([166.1, 94.1, 22.1, -49.9, -121.9])
    sig = [Pc(((t / T_per) + thi / 360.0) % 1.0) for thi in th]         # the pattern turning toward decreasing theta
    n, rig, lim, rep, T_found, (w1, w2, w3) = SW.run(t, sig, th, "synthetic family", verbose=False)
    check("F-5 the single-wave contract by construction: W-1 n = %d, rigid residual %.1e, turn-to-turn %.1e (all zero within the monitor's resolution)" % (n, rig, rep),
          n == 1 and w1 and w2 and w3)
    check("F-5b the extraction plane is supersonic in every phase (M_in %.3f > 1)" % a.min, a.min > 1.0)
    # R-1 (must fire): a family whose mean pressure is off by one percent
    check("R-1 REJECTOR: a family with the mean pressure off by 1 percent is refused by F-1", not (abs(1.01 * pmean / (a.pcp * ATM * (1 + DC)) - 1) < 1e-6))
    # ---- records
    fam = dict(K=str(a.K), source="CycleFamily v0: Stechmann-Heister-Harroun matched cycle %s (phi %.2f, Pcp %g atm, Ti %g K), sectors of equal time, gas = equilibrium products at the phase's stagnation state, frozen; gamma and R at the extraction state M_in %.3f" % (key, a.phi, a.pcp, a.ti, a.min),
               T_tab=[300.0, 4200.0], phases=[{k_: v for k_, v in p.items() if k_ != "Y" and k_ not in ("T", "p")} for p in phases])
    json.dump(fam, open(os.path.join(out, "family_K%d.json" % a.K), "w"), indent=1)
    json.dump(dict(geno_run=GENO_RUN, gamma=mean["gamma"], R=mean["R"], T0=mean["T0"], P0=mean["P0"], M_in=a.min, T_tab=[300.0, 4200.0],
                   note="CycleFamily v0 time-mean state of %s; the GENO run gives the annulus geometry only (the S42 posing)" % key),
              open(os.path.join(out, "gas_mean.json"), "w"), indent=1)
    # P0 A* of the posing: the THOR annulus (0.792 .. 1.0 of the lip radius 68 mm) at M_in with the mean gas (the design tool's normalisation)
    yl, yu = 0.792 * 0.068, 0.068
    AA = (2.0 / (gmm + 1) * (1 + 0.5 * (gmm - 1) * a.min ** 2)) ** ((gmm + 1) / (2 * (gmm - 1))) / a.min
    P0A = P0m * np.pi * (yu ** 2 - yl ** 2) / AA
    json.dump(dict(source="CycleFamily v0 %s" % key, K=a.K, pa=a.pa_atm * ATM, P0A=float(P0A), P0A_note="P0_mean x A* of the THOR annulus at M_in (the design tool's normalisation)",
                   phases=[dict(phase=kk, mach=p["M"], **p) for kk, p in enumerate(phases)] + [dict(phase=a.K, mach=mean["M"], **mean)]),
              open(os.path.join(out, "phases_cfd.json"), "w"), indent=1)
    print("   phases: P0 %.2f .. %.2f atm, T0 %.0f .. %.0f K, gamma %.4f .. %.4f, R %.1f .. %.1f; mean P0 %.2f atm T0 %.0f K gamma %.4f R %.1f"
          % (P_sec.min() / ATM, P_sec.max() / ATM, T_sec.min(), T_sec.max(), min(p["gamma"] for p in phases), max(p["gamma"] for p in phases),
             min(p["R"] for p in phases), max(p["R"] for p in phases), P0m / ATM, T0m, gmm, Rm))
    print("   lip pressure at M_in over p_a per phase: %s" % np.array2string(np.array([p["p"] for p in phases]) / (a.pa_atm * ATM), precision=2))
    print("   written %s" % out)
    print("VERDICT: %s" % ("PASS" if OK else "FAIL"))
    sys.exit(0 if OK else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""[X-OWNM] THE IDEAL SPIKE OF OUR WORLD AT THE NOMINAL AMBIENT ATTAINS
THE GEOMETRY-FREE CEILING -- the M1 corollary of [T-GB] measured on our
own construction, no GENO in the chain. [F3/A1], S38 2026-09-24 (F3
session 2/4), the value half of the F3 exit leg "certified plug optimum".

WHAT WAS MISSING. The our-world plug instruments of S28 ([X-OWTW],
[X-OWO3], [X-OWS3]) grade designs against GENO's RaoPlug member, which
expands to its own lip ambient 0.9949 PA (GENO's fan fails for theta_E
>= 0 at the exact PA); the tournament [X-PTRN] (S30) runs at the nominal
ambient on [X-AFAN]'s member but grades by paired J differences only,
with a value band of 1-2 percent of J. What the program's theory says
(M0 Prop. 7, THEOREM* within [C-GBCS]; its COROLLARY, mechanism M1) is
sharper: every design's thrust is bounded by mdot V_id, V_id = sqrt(2
(h0 - h(s0, PA))), and the untruncated ideal spike ATTAINS it -- so it is
the global optimum of the class. Whether our march and our construction
actually reach the bound had never been measured.

THE MEASUREMENT. World = a1_config_compare's of record (CH4/O2 frozen
NASA tables: a variable-gamma gas; mdot of the bell's case; lip 2.2695 m;
inflow Mach 2.0 at the lip; PA 7.614420e5 Pa NOMINAL). The member =
fan_axi at [X-AFAN]'s record (241 x 241), traced wall to its tip-floor
node. Designs are MARCHED by the plug march from the vertical cut at x0
through the member's field (the [X-RAOSQ] v3 representation: 8 knots,
near-cut zone frozen, tip pinned -- used here only to march, never to
search). J = F_in through the start line + the wall's push (gauge PA);
above the terminal ray the field at x0 is uniform (q_e, 0, PA), so the
thrust of everything downstream of the cut is J_total = J + rho_e q_e^2
pi (y_E^2 - y_top^2), and for the ideal spike it must equal mdot q_e.
  D-1 the construction certified;
  D-2 the member certified on every rung of the K ladder;
  D-3 CLASS: no fold in Humphreys' region R (the S34 criterion, a1_plug_
      margin census) on the member's record at every rung;
  D-4 mass: start line + uniform part = the world's mdot within the
      construction's two declared residuals (the inflow at its leading
      ray; the tip floor's share);
  D-5 THE CEILING ATTAINED: the deficit d(K) = J_total / (mdot q_e) - 1
      falls with K at the observed order p; its Richardson limit from the
      three certified rungs lies within K_RICH x |limit - limit(p = 1)|
      of zero (the order uncertainty is the band);
  R-1 PAIRED REJECTOR (value): the member beats the 1.5-percent perturbed
      design -- in class in region R -- by a PAIRED difference that is
      resolved on the ladder (positive on every rung, larger than
      K_RICH x its own change between rungs): the functional can see a
      design that is not the optimum, while the unpaired band cannot;
  R-2 CLASS REJECTOR: the chord between the design's endpoints (a
      generic wall) FOLDS in region R -- the census can see a fold.
READINGS (not graded): the chord's and the uniform-turn wall's paired
deficits -- the flatness of the thrust valley around the optimum.

FALSIFIER: a limit deficit beyond its band (the member does not attain
the bound: the march, the construction or [T-GB] is wrong), a design in
class that beats the member beyond the paired band (the bound or the
march is wrong), a rejector that does not fire.

DECLARED. The tip floor at 0.01 y_E (the member closes on the axis; the
excluded tip carries 1e-4 of the exit mass); [X-AFAN]'s inflow posing
(the wall straight upstream of the leading ray at M 2.0); K 321 left out
(uncertified at N 81: a free-jet edge cell, the rung lottery of record).

ENVIRONMENT. OWNM_ART (default _ourworld_nominal/). Constants in
ourworld_nominal_cases.json.
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

CASES = {k: v["value"] for k, v in json.load(
    open(os.path.join(HERE, "ourworld_nominal_cases.json"))).items() if k != "_doc"}
POSE, TURN = CASES["posing"], CASES["turn_reading"]
ART = os.environ.get("OWNM_ART", os.path.join(HERE, "_ourworld_nominal"))
# the [X-RAOSQ] design representation reads its posing at import
os.environ["RAO_X0"] = repr(float(POSE["x0"]))
os.environ["RAO_K"] = str(int(POSE["K_ladder"][1]))
os.environ["RAO_N"] = str(int(POSE["N"]))
os.environ["RAO_ART"] = ART

import jax.numpy as jnp                                 # noqa: E402

import a1_config_compare as CC                          # noqa: E402
import a1_axi_fan as AF                                 # noqa: E402
import a1_plug_margin as PMG                            # noqa: E402
import a1_ideal_march_jax as A1                         # noqa: E402
import rao1961_sqp_return as SR                         # noqa: E402
from a1_plug_march import col_fluxes, plug_march        # noqa: E402
from a1_freejet_unit import q_at_pa                     # noqa: E402

K_RICH = A1.K_RICH
NPASS = [0, 0]


def say(msg):
    print(msg, flush=True)


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def build():
    t0 = time.time()
    w = CC.build_world()
    fa = AF.fan_axi(w, 0.0, int(POSE["fan"][0]), int(POSE["fan"][1]))
    sx, sy = fa["wall"]
    x0 = SR.X0
    ys, us, vs = fa["cut"](x0)
    wd = SR.World()
    wd.tab, wd.ta = w["tab"], w["ta"]
    wd.pa = CC.PA
    wd.qpa = float(q_at_pa(CC.PA, w["ta"], w["tab"]["_as"]))
    wd.wall = np.stack([sx, sy], 1)
    wd.xD = float(sx[-1])
    yq = np.linspace(ys[0], ys[-1], SR.N_ROW)
    wd.start = (x0, yq, np.interp(yq, ys, us), np.interp(yq, ys, vs))
    stl = np.stack([np.full(len(yq), x0), yq, wd.start[2], wd.start[3]], 1)
    m_in, wd.F_in = col_fluxes(stl, wd.ta, wd.pa, 1.0)
    wd.m_in = abs(float(m_in))
    wd.xs0 = x0 + SR.FREEZE * (wd.xD - x0)
    wd.yw0 = float(np.interp(wd.xs0, sx, sy))
    wd.slope0 = float(np.interp(wd.xs0, sx, np.gradient(sy, sx)))
    wd.xk = wd.xs0 + (wd.xD - wd.xs0) * np.arange(1, SR.M_NODES + 1) / SR.M_NODES
    wd.yD = float(sy[-1])
    wd.W_fit = np.interp(wd.xk[:-1], sx, sy)
    wd.y_top, wd.y_E = float(ys[-1]), float(w["RMAX"])
    wd.mdot = float(w["mdot"])
    wd.rho_e = float(A1.state_q(jnp.float64(wd.qpa), wd.ta)[2])
    say("   world: CH4/O2 NASA tables (variable gamma), PA %.6g Pa NOMINAL, M_i %.2f at the lip,"
        " lip %.5f m, mdot %.6g kg/s; member (fan_axi %dx%d) cert %.3f, tip (%.4f, %.4f) m; cut x0"
        " %.2f: %d rows from the wall (y %.5f) to the terminal ray (y %.5f), F_in %.6g N; %.0f s"
        % (CC.PA, CC.MI, wd.y_E, wd.mdot, POSE["fan"][0], POSE["fan"][1], fa["cert"]["worst"],
           wd.xD, wd.yD, x0, SR.N_ROW, yq[0], yq[-1], wd.F_in, time.time() - t0))
    return w, fa, wd


def march(wd, W, K):
    """Record march at K stations: certification, class in region R, J_total."""
    out, S = SR.march_record(np.asarray(W, float), wd, K=K)
    ell2 = float(np.median(np.diff(np.asarray(S.d["xcols"])))) ** 2
    ms, _, _, fl = PMG.np_margin(out, S, len(wd.start[1]), 1.0, 0.0, ell2, with_depth=True,
                                 with_floor=True)
    orient = float(np.sign(np.median(ms)))
    mgR = dict(PMG.margin_dict(rho=1.0, mu0=0.0, m_ref=1.0, orient=orient, f_edge=0.0, ell2=ell2),
               vec=True, region="R")
    st = tuple(np.asarray(v) for v in SR.stations(np.asarray(W, float), wd, K))
    oR, _ = plug_march(st, wd.start, wd.qpa, wd.tab, 1.0, edge_fill=SR.EDGE_FILL, margin=mgR)
    J = float(wd.F_in + SR.push_of(out, wd))
    m_u = wd.rho_e * wd.qpa * np.pi * (wd.y_E ** 2 - wd.y_top ** 2)
    m_tot = wd.m_in + m_u
    Jt = J + m_u * wd.qpa
    return dict(cert=float(out["cert_worst"]), minR=float(oR["margin_min"]), nR=int(oR["margin_n"]),
                J=J, J_total=Jt, m_total=m_tot, d=Jt / (m_tot * wd.qpa) - 1.0)


def richardson(Ks, d):
    """Observed order and limit from three rungs with ratio 2."""
    p = float(np.log(abs((d[0] - d[1]) / (d[1] - d[2]))) / np.log(Ks[1] / Ks[0]))
    lim = d[2] + (d[2] - d[1]) / ((Ks[2] / Ks[1]) ** p - 1.0)
    lim1 = d[2] + (d[2] - d[1])                   # the first-order limit
    return p, lim, lim1


def main():
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    say("== [F3] our world at the NOMINAL ambient: the ideal spike against the [T-GB] ceiling"
        " [X-OWNM] ==")
    w, fa, wd = build()
    Ks = [int(k) for k in POSE["K_ladder"]]
    check("D-1 the ideal spike built by our inverse march certifies (fan_axi %dx%d: %.3f)"
          % (POSE["fan"][0], POSE["fan"][1], fa["cert"]["worst"]), fa["cert"]["worst"] <= 1.0)
    sgn = np.array([(-1.0) ** k for k in range(len(wd.W_fit))])
    designs = {"member": wd.W_fit,
               "perturbed": wd.W_fit * (1.0 + float(POSE["perturb"]) * sgn),
               "chord": wd.yw0 + (wd.yD - wd.yw0) * (wd.xk[:-1] - wd.xs0) / (wd.xD - wd.xs0)}
    th0 = float(np.arctan(wd.slope0))
    xx = np.linspace(wd.xs0, wd.xD, int(TURN["grid"]))

    def turn_y(th1):
        th = th0 + (th1 - th0) * (xx - wd.xs0) / (wd.xD - wd.xs0)
        dy = np.tan(th)
        return wd.yw0 + np.concatenate([[0.0], np.cumsum(0.5 * (dy[1:] + dy[:-1]) * np.diff(xx))])
    from scipy.optimize import brentq
    brk = float(np.radians(TURN["bracket_deg"]))
    th1 = brentq(lambda t: turn_y(t)[-1] - wd.yD, th0 - brk, th0 + brk, xtol=A1.EPS)
    designs["turn"] = np.interp(wd.xk[:-1], xx, turn_y(th1))
    R = {}
    for name, W in designs.items():
        R[name] = []
        for K in (Ks if name in ("member", "perturbed") else Ks[1:]):
            t0 = time.time()
            r = march(wd, W, K)
            r["K"] = K
            R[name].append(r)
            say("   %-9s K %3d: cert %.3e, min margin in R %+.4f (%d cells), J_total %.8e N,"
                " deficit to the ceiling %+.3e (%.0f s); distance to the member %.3e m"
                % (name, K, r["cert"], r["minR"], r["nR"], r["J_total"], r["d"], time.time() - t0,
                   SR.wall_dist(W, wd)))
    mem = R["member"]
    check("D-2 the member certifies on every rung (%s)"
          % ", ".join("K %d: %.3f" % (r["K"], r["cert"]) for r in mem), all(r["cert"] <= 1.0 for r in mem))
    check("D-3 CLASS: no fold in region R on the member at any rung (min margin %s)"
          % ", ".join("%+.4f" % r["minR"] for r in mem), all(r["minR"] > 0.0 for r in mem))
    r_m = mem[-1]["m_total"] / wd.mdot - 1.0
    lead_res = abs(AF.ray_mass(fa["rays"][0], wd.ta, fa["svs"][0]) / wd.mdot - 1.0)
    tip_share = (wd.yD / wd.y_E) ** 2
    check("D-4 mass: start line + uniform part = the world's mdot to %+.2e, within the"
          " construction's declared residuals (inflow at its leading ray %.2e + tip floor share"
          " %.2e)" % (r_m, lead_res, tip_share), abs(r_m) <= lead_res + tip_share)
    d = [r["d"] for r in mem]
    p, lim, lim1 = richardson(Ks, d)
    band5 = K_RICH * abs(lim - lim1)
    ceil = mem[-1]["m_total"] * wd.qpa
    say("   the ceiling mdot V_id = %.8e N (V_id = q_at_pa %.3f m/s); deficits %s; observed order"
        " %.3f; Richardson limit %+.3e (first-order limit %+.3e)"
        % (ceil, wd.qpa, ", ".join("%+.3e" % v for v in d), p, lim, lim1))
    check("D-5 THE CEILING ATTAINED: the member's limit deficit %+.2e, |.| <= K_RICH x the order"
          " uncertainty %.2e" % (lim, band5), abs(lim) <= band5)
    pert = R["perturbed"]
    dJ = [m_["J_total"] - q_["J_total"] for m_, q_ in zip(mem, pert)]
    ch = max(abs(dJ[1] - dJ[0]), abs(dJ[2] - dJ[1]))
    say("   paired: J_total(member) - J_total(perturbed) = %s N (%s of J)"
        % (", ".join("%+.4e" % v for v in dJ), ", ".join("%+.2e" % (v / mem[-1]["J_total"]) for v in dJ)))
    check("R-1 PAIRED REJECTOR: the member beats the in-class perturbed design (min margin in R %s)"
          " by %+.3e N on every rung, > K_RICH x its change between rungs %.3e N"
          % (", ".join("%+.4f" % r["minR"] for r in pert), min(dJ), K_RICH * ch),
          all(r["minR"] > 0.0 for r in pert) and min(dJ) > K_RICH * ch)
    chd = R["chord"]
    check("R-2 CLASS REJECTOR: the chord between the design's endpoints folds in region R (min"
          " margin %s)" % ", ".join("%+.4f" % r["minR"] for r in chd), all(r["minR"] < 0.0 for r in chd))
    rd = {}
    for name in ("chord", "turn"):
        pr = [m_["J_total"] - q_["J_total"] for m_, q_ in zip(mem[1:], R[name])]
        rd[name] = pr
        say("   reading: J_total(member) - J_total(%s) = %s N (%s of J); distance %.3e m"
            % (name, ", ".join("%+.4e" % v for v in pr),
               ", ".join("%+.2e" % (v / mem[-1]["J_total"]) for v in pr), SR.wall_dist(designs[name], wd)))
    rec = dict(npass=list(NPASS), Ks=Ks, deficits=d, order=p, limit=lim, limit1=lim1, band=band5,
               ceiling=ceil, mdot=wd.mdot, m_total=mem[-1]["m_total"], r_m=r_m, lead_res=lead_res,
               member=mem, perturbed=pert, chord=chd, turn=R["turn"], paired=dJ, readings=rd,
               x_tip=wd.xD, y_tip=wd.yD, V_id=wd.qpa)
    fn = os.path.join(ART, "derive_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    say("VERDICT: %s" % ("PASS -- the ideal spike of our world attains the geometry-free ceiling at"
                         " the nominal ambient, in class, from our own construction"
                         if NPASS[0] == NPASS[1] else "FAIL"))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit(main())

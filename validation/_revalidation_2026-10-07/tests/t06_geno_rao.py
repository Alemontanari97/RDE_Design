#!/usr/bin/env python3
"""T06 -- cross-code, axisymmetric plug under its free jet: the model's single-wall plug march (lip fan at E, free
edge at p_a, a1_plug_march.plug_march without shroud) on GENO's Rao plug (nozzle_type 8, run geno/rao_sdt_L0448:
SDT mean gas, lip y_E = 1, M_i 1.556, length 0.448, base p_b 50662 Pa; GENO's output: theta_E -14.79 deg, lip ambient
p_a = 96086 Pa), started from GENO's own data (ref/rao_posing.py: GENO's last internal C+ characteristic, E, the fan
at E to q_pa), the plug = GENO's contour (isobaric edge, then the Phase-1 wall) down to D.

GENO's resolution is FIXED by its code (the C- control surface at step y_E/200, its internal lines at 56 points:
the runs at NI 201/401/801/1601 are identical, measured), so GENO's error is measured on GENO's own data instead:
  e_mass = |mass through GENO's C+ - mass through GENO's ED| / mdot  (both with the same trapezoid, GENO's states)
  e_mom  = |F(C+) - push(GENO's wall p) - F(ED)| / F(ED)             (the momentum theorem on GENO's region C+..ED)
Model ladder: the start line refined by interpolating GENO's C+ data (cubic in chord length; data error ~1e-9) to
55 x {1, 2, 4, 8} + 1 points, fan rays 10 x {1, 2, 4, 8}, plug stations 60 x {1, 2, 4, 8}.
Checks:
  R1 plug wall pressure, model vs GENO: mean relative difference at the finest grid <= 2|change| + e_G, with
     e_G = max(e_mass, e_mom) (GENO's own measured inconsistency, the size of its discretization error);
  R2 the model's thrust J = F(start) - push(plug) vs GENO's same functional on GENO's own data: relative
     difference <= 2|change| + e_G;
  R3 the model's mass through its start line vs GENO's mdot. The model recomputes rho and p from the speed on the exact
     isentrope, GENO's internal states drift from it (measured: rho up to -3.4e-5, p -4.0e-5 on its C+, 1e-10 on
     ED), so the bound is e_mass + max |rho_GENO / rho_isentrope(V) - 1| on the C+;
  R4 the isobaric edge (GENO: dp/ds = 0 there): the model's wall pressure along it constant to 2|change| + e_G;
  R5 every march certified.
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
from scipy.interpolate import CubicSpline          # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_plug_march as PM                         # noqa: E402
import rao_posing as RP                            # noqa: E402

R = rv.Report("t06_geno_rao")
D = os.path.join(rv.RV, "geno", "rao_sdt_L0448")
o2 = lambda a, b: np.log(abs(a) / abs(b)) / np.log(2.0)      # noqa: E731
base = RP.RaoPosing(D, K=60, n_fan=10)
g = base.g
ta, pa = base.ta, base.pa


def fluxes(rows):
    """(mass, momentum in the p_a gauge) through a polyline of GENO rows (x y rho V theta p ...)."""
    u, v = rows[:, 3] * np.cos(rows[:, 4]), rows[:, 3] * np.sin(rows[:, 4])
    dx, dy = np.diff(rows[:, 0]), np.diff(rows[:, 1])
    rm = 0.5 * (rows[1:, 2] + rows[:-1, 2])
    um, vm, pm = 0.5 * (u[1:] + u[:-1]), 0.5 * (v[1:] + v[:-1]), 0.5 * (rows[1:, 5] + rows[:-1, 5])
    w = 2.0 * np.pi * 0.5 * (rows[1:, 1] + rows[:-1, 1])
    dm = rm * (um * dy - vm * dx) * w
    return float(np.sum(dm)), float(np.sum(um * dm + (pm - pa) * dy * w))


# ---- GENO's own consistency on its data (C+ from the plug up; ED from E down to D, reversed to D up)
cp = g.cplus                     # x y rho V theta p T a M gam, plug -> cowl
ed = g.ED[::-1]                  # D -> E
m_cp, F_cp = fluxes(cp)
m_ed, F_ed = fluxes(ed)
wl = g.plug[g.plug[:, 0] >= cp[0, 0] - 1e-12]
wl = np.vstack([cp[:1, :6], wl[:, :6]])
push_g = float(np.sum((0.5 * (wl[1:, 5] + wl[:-1, 5]) - pa) * 2.0 * np.pi * 0.5 * (wl[1:, 1] + wl[:-1, 1])
                      * np.diff(wl[:, 1])))
J_geno = F_cp - push_g
e_mass = abs(m_cp - m_ed) / m_ed
e_mom = abs(J_geno - F_ed) / abs(F_ed)
e_G = max(e_mass, e_mom)
R.note("GENO's own data: mass through C+ %.6f, through ED %.6f (reported mdot %.6f): e_mass %.2e; F(C+) %.6e - push(wall)"
       " %.6e = %.6e vs F(ED) %.6e: e_mom %.2e" % (m_cp, m_ed, g.perf["mdot [kg/s]"], e_mass, F_cp, push_g, J_geno,
                                                   F_ed, e_mom))

# ---- the isobaric edge on GENO's wall: between the C+ line's plug point and where the first wave lands
x_iso = (cp[0, 0], g.x_s)
iso = (wl[:, 0] > x_iso[0] + 1e-9) & (wl[:, 0] < x_iso[1] - 1e-9)
R.note("GENO's wall p along its isobaric edge x %.4f..%.4f: relative spread %.2e" % (
    x_iso[0], x_iso[1], np.ptp(wl[iso, 5]) / np.mean(wl[iso, 5])))
R.note("the wall representation (two not-a-knot cubic splines through GENO's points): max |angle - GENO's flow angle| at"
       " GENO's points %.2e rad" % base.rep_err)


def posing(level):
    """RaoPosing with the start line's C+ part interpolated to 55 * 2^level + 1 points."""
    rp = RP.RaoPosing(D, K=60 * 2 ** level, n_fan=10 * 2 ** level)
    if level > 0:
        s = np.r_[0.0, np.cumsum(np.hypot(np.diff(cp[:, 0]), np.diff(cp[:, 1])))]
        sq = np.linspace(0.0, s[-1], 55 * 2 ** level + 1)
        cs = {k: CubicSpline(s, cp[:, k]) for k in (0, 1, 3, 4)}
        x_, y_, V_, th_ = (cs[k](sq) for k in (0, 1, 3, 4))
        tail = rp.start_arr[len(cp):]                   # E and the fan rows
        st = np.concatenate([np.stack([x_, y_, V_ * np.cos(th_), V_ * np.sin(th_)], 1), tail], 0)
        rp.start = (st[:, 0], st[:, 1], st[:, 2], st[:, 3])
        rp.start_arr = st
        rp.N = len(st)
        F = PM.col_fluxes(st, rp.ta, rp.pa, 1.0)
        rp.mdot_start, rp.F_start = abs(F[0]), F[1]
    return rp


res = []
for lev in range(4):
    rp = posing(lev)
    out, S = rp.march_record()
    W = np.asarray(out["wall"])
    pw = np.asarray(A1.state_q(jnp.asarray(np.hypot(W[:, 2], W[:, 3])), ta)[1])
    pg = np.interp(W[:, 0], wl[:, 0], wl[:, 5])
    e = pw / pg - 1.0
    J = float(rp.J_of(out))
    isom = (W[:, 0] > x_iso[0] + 1e-9) & (W[:, 0] < x_iso[1] - 1e-9)
    r = dict(level=lev, N=rp.N, K=rp.K, L1=float(np.mean(np.abs(e))), Linf=float(np.max(np.abs(e))),
             eJ=J / J_geno - 1.0, J=J, mass=rp.mdot_start / g.perf["mdot [kg/s]"] - 1.0,
             iso=float(np.ptp(pw[isom]) / np.mean(pw[isom])), cert=float(out["cert_worst"]), where=out["cert_where"],
             n=int(out["cert_n"]), x=W[:, 0], e=e)
    res.append(r)
    R.note("level %d (start rows %d, stations %d, %d cells): wall p vs GENO mean %.3e max %.3e | J vs GENO's %+.3e | "
           "start mass vs GENO %+.2e | isobaric-edge spread %.2e | cert %.3f at %s" % (
               lev, rp.N, rp.K, r["n"], r["L1"], r["Linf"], r["eJ"], r["mass"], r["iso"], r["cert"], r["where"]))
for k in range(1, len(res)):
    a, b = res[k - 1], res[k]
    R.note("orders %d->%d: wall p %.2f | J %.2f | isobaric spread %.2f" % (k - 1, k, o2(a["L1"], b["L1"]),
                                                                          o2(a["eJ"], b["eJ"]), o2(a["iso"], b["iso"])))
f, c = res[-1], res[-2]
R.check("R1 wall p, model vs GENO (mean, finest) <= 2|change| + e_G", f["L1"], 2.0 * abs(f["L1"] - c["L1"]) + e_G)
R.check("R2 thrust functional, model vs GENO's on GENO's data <= 2|change| + e_G", f["eJ"],
        2.0 * abs(f["eJ"] - c["eJ"]) + e_G)
import exact                                       # noqa: E402
Gx = exact.PerfectGas(g.gamma, g.R, g.T0, g.P0)
e_rho = float(np.max(np.abs(cp[:, 2] / Gx.rho_q(cp[:, 3]) - 1.0)))
R.note("GENO's C+ states vs the isentrope: max |rho / rho_isen(V) - 1| %.2e" % e_rho)
R.check("R3 the model's start-line mass vs GENO's mdot <= e_mass + max|rho_GENO/rho_isen - 1|", f["mass"], e_mass + e_rho)
R.check("R4 isobaric edge: the model's wall p spread <= 2|change| + e_G", f["iso"], 2.0 * abs(f["iso"] - c["iso"]) + e_G)
R.check("R5 certificates <= 1 over the ladder", max(r["cert"] for r in res), 1.0)


# REJECTOR (R5): the R1 check with the speed on GENO's C+ start line 0.1 % too high (the fan rows kept at q_pa)
def l1_corrupted(level, f=1.001):
    rp = posing(level)
    n_cp = (55 * 2 ** level + 1) if level > 0 else len(cp)
    st = np.array(rp.start_arr, float)
    st[:n_cp, 2:4] *= f
    rp.start, rp.start_arr = (st[:, 0], st[:, 1], st[:, 2], st[:, 3]), st
    o_x, _ = rp.march_record()
    W_x = np.asarray(o_x["wall"])
    p_x = np.asarray(A1.state_q(jnp.asarray(np.hypot(W_x[:, 2], W_x[:, 3])), ta)[1])
    return float(np.mean(np.abs(p_x / np.interp(W_x[:, 0], wl[:, 0], wl[:, 5]) - 1.0)))


cx_, fx_ = l1_corrupted(len(res) - 2), l1_corrupted(len(res) - 1)
R.note("rejector: start-line speed x1.001 -> wall p vs GENO mean %.3e (finest), %.3e (previous)" % (fx_, cx_))
R.reject("R1 wall p, model vs GENO (mean, finest), start-line speed x1.001", fx_, 2.0 * abs(fx_ - cx_) + e_G)

import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
fig, ax = plt.subplots(1, 3, figsize=(17, 4.6))
a = ax[0]
a.plot(g.plug[:, 0], g.plug[:, 1], "k-", lw=2, label="GENO Rao plug")
a.plot(g.cowl[:, 0], g.cowl[:, 1], "k-", lw=2.5, label="GENO cowl")
a.plot(cp[:, 0], cp[:, 1], "b-", lw=1, label="start: GENO's last internal C+")
a.plot(g.ED[:, 0], g.ED[:, 1], "r--", lw=1, label="GENO control surface ED")
a.plot(g.first_wave[:, 0], g.first_wave[:, 1], "g:", lw=1, label="first wave of the lip fan")
a.set_aspect("equal"); a.legend(fontsize=7); a.set_title("GENO's Rao plug (methane gas, length 0.448)"); a.grid(alpha=0.3)
a = ax[1]
a.plot(wl[:, 0], wl[:, 5] / 1e5, "k-", lw=2, label="GENO wall p")
for r in res:
    a.plot(r["x"], (1.0 + r["e"]) * np.interp(r["x"], wl[:, 0], wl[:, 5]) / 1e5, "-", lw=1.0, label="model level %d" % r["level"])
a.axvline(g.x_s, color="g", ls=":", lw=0.8)
a.set_xlabel("x"); a.set_ylabel("p [bar]"); a.legend(fontsize=7); a.grid(alpha=0.3); a.set_title("plug wall pressure")
a = ax[2]
h = np.array([1.0 / r["K"] for r in res])
for key, lab in (("L1", "wall p vs GENO (mean)"), ("eJ", "J vs GENO's"), ("iso", "isobaric-edge spread")):
    a.loglog(h, [abs(r[key]) for r in res], "o-", label=lab)
a.axhline(e_G, color="k", ls=":", label="GENO's own inconsistency e_G")
a.set_xlabel("1/K"); a.legend(fontsize=7); a.grid(alpha=0.3, which="both"); a.set_title("convergence")
rv.savefig(fig, "06_geno_rao.png")
sys.exit(R.save(dict(e_mass=e_mass, e_mom=e_mom, J_geno=J_geno, F_ed=F_ed,
                     levels=[{k: v for k, v in r.items() if k not in ("x", "e")} for r in res])))

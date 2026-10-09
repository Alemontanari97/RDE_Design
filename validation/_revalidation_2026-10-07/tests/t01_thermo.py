#!/usr/bin/env python3
"""T01 — the model's gas (constant-gamma tables, a1_twowall.tab_gconst + a1_ideal_march_jax.state_q) against the
closed-form perfect-gas relations, on the SDT mean state and on each of the 12 phases.

What the model does (a1_ideal_march_jax.py:440-457): q -> h = h0 - q^2/2 -> T by linear interpolation of the
tabulated h(T) (exact for cp = const: h is linear in T) -> p = PREF exp((s0(T) - s0)/R) with s0(T) = cp ln T
interpolated linearly -> rho = p/(R T), c = sqrt(gamma R T), M = q/c.

Error model (derived): T, c, M exact to rounding; s0 interpolation error <= cp dT^2 / (8 T^2) (linear
interpolation of ln T, grid spacing dT) -> relative p (and rho) error <= (cp/R) dT^2 / (8 T^2). Tolerance = 4x that
bound at the coldest tested temperature + 1e-12 rounding allowance. Out-of-table temperatures are CLAMPED by
jnp.interp: the test also checks that every phase's ambient temperature lies inside the table.

Checks:
  C1  state_q vs exact (T, p, rho, c, M) for M in [1, 1.3 M(p_a)] per gas (mean + 12 phases)
  C2  q_of_mach (a1_shroud_twin) vs exact q(M) at M_in
  C3  speed at p_a (the carrier's brentq) vs exact q(p_a)
  C4  pm_turn (Gauss-Legendre, n_gl 16, a1_plug_march) vs exact nu(M_b) - nu(M_a)
  C5  ambient temperature of each phase inside the table range
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import numpy as np                                 # noqa: E402
import jax.numpy as jnp                            # noqa: E402
import a1_ideal_march_jax as A1                    # noqa: E402
import a1_shroud_twin as ST                        # noqa: E402
from a1_plug_march import pm_turn                  # noqa: E402
from scipy.optimize import brentq                  # noqa: E402

R = rv.Report("t01_thermo")
gm = rv.sdt_gas()
fam = rv.sdt_phases()
PA_OVER_P0 = 0.024378            # TWOP_PA of the SDT posing (handoff/plug_2026-09-29/sdt/sdt_env.sh)
pa_abs = PA_OVER_P0 * gm["P0"]   # the carrier's p_a = pa * P0 of the posing's reference state (a1_twowall J)
R.note("p_a = %.1f Pa (TWOP_PA %.6f x P0_mean %.1f)" % (pa_abs, PA_OVER_P0, gm["P0"]))

gases = [("mean", gm["gamma"], gm["R"], gm["T0"], gm["P0"], gm["M_in"])]
for k, ph in enumerate(fam["phases"]):
    gases.append(("phase%02d" % k, ph["gamma"], ph["R"], ph["T0"], ph["P0"], ph["M"]))
T_tab = gm["T_tab"]
dT = (T_tab[1] - T_tab[0]) / (A1.N_TAB - 1)

worst = dict(T=0.0, p=0.0, rho=0.0, c=0.0, M=0.0)
curves = {}
for name, g, Rg, T0, P0, Min in gases:
    G = exact.PerfectGas(g, Rg, T0, P0)
    tab, ta = rv.model_table(g, Rg, T0, P0, fam.get("T_tab", T_tab) if name != "mean" else T_tab)
    M_pa = float(G.M_of_p(pa_abs))
    Ms = np.linspace(1.0, 1.3 * M_pa, 400)
    q = G.q(Ms)
    st = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), ta)]
    ex = dict(T=G.T(Ms), p=G.p(Ms), rho=G.rho(Ms), c=G.c(Ms), M=Ms)
    md = dict(T=st[0], p=st[1], rho=st[2], c=st[3], M=st[5])
    T_min = float(G.T(Ms[-1]))
    bound = (G.cp / Rg) * dT ** 2 / (8.0 * T_min ** 2)
    tol = dict(T=1e-12, c=1e-12, M=1e-12, p=4.0 * bound + 1e-12, rho=4.0 * bound + 1e-12)
    for k in ("T", "p", "rho", "c", "M"):
        e = float(np.max(np.abs(md[k] / ex[k] - 1.0)))
        worst[k] = max(worst[k], e)
        if name in ("mean", "phase00", "phase06"):
            R.check("C1 %s: max rel err %s over M 1..%.2f" % (name, k, Ms[-1]), e, tol[k])
        elif e > tol[k]:
            R.check("C1 %s: max rel err %s over M 1..%.2f" % (name, k, Ms[-1]), e, tol[k])
    curves[name] = (Ms, md["p"] / ex["p"] - 1.0, md["rho"] / ex["rho"] - 1.0)
    # C2: q_of_mach
    qm = ST.q_of_mach(Min, ta, tab["_as"])
    R.check("C2 %s: q_of_mach(M_in %.3f) rel err" % (name, Min), qm / float(G.q(Min)) - 1.0, 1e-9) \
        if name in ("mean", "phase00") else None
    # C3: speed at p_a (the carrier's root, a1_twowall.py _qpa: brentq on state_q p = p_a)
    fq = lambda qq: float(A1.state_q(jnp.float64(qq), ta)[1]) - pa_abs        # noqa: E731
    lo, hi = 1.02 * tab["_as"], 3.2 * tab["_as"]
    while not (np.isfinite(fq(hi)) and fq(hi) < 0.0):
        hi = lo + 0.9 * (hi - lo)
    qpa = brentq(fq, lo, hi, xtol=1e-12 * tab["_as"])
    e3 = qpa / float(G.q_of_p(pa_abs)) - 1.0
    ok3 = abs(e3) <= 4.0 * bound + 1e-10
    if name in ("mean", "phase00", "phase06") or not ok3:
        R.check("C3 %s: speed at p_a rel err (M_pa %.4f)" % (name, M_pa), e3, 4.0 * bound + 1e-10)
    # C5: the ambient temperature inside the table (clamp-free)
    T_pa = float(G.T(M_pa))
    R.check("C5 %s: T(p_a) = %.1f K inside table [%.0f, %.0f]" % (name, T_pa, T_tab[0], T_tab[1]),
            0.0, 0.0, ok=(T_tab[0] < T_pa < T_tab[1]) and (T_tab[0] < T0 < T_tab[1]))

R.note("worst over all 13 gases: " + ", ".join("%s %.2e" % kv for kv in worst.items()))

# C4: pm_turn against the closed form, mean gas, the turns of the lip fan
G = exact.PerfectGas(gm["gamma"], gm["R"], gm["T0"], gm["P0"])
tab, ta = rv.model_table(gm["gamma"], gm["R"], gm["T0"], gm["P0"], T_tab)
M_pa = float(G.M_of_p(pa_abs))
pm_rows = []
for Ma, Mb in ((1.556, M_pa), (1.556, 2.0), (2.0, M_pa), (1.2, 4.0), (1.05, 1.556)):
    num = float(pm_turn(jnp.float64(G.q(Ma)), jnp.float64(G.q(Mb)), ta, 16))
    ex = float(G.nu(Mb) - G.nu(Ma))
    pm_rows.append((Ma, Mb, num, ex))
    # GL-16 on a smooth integrand: error << 1e-10 rad unless the integrand's sqrt(M^2-1) kink at M=1 is in range;
    # tolerance = the table's own p error is irrelevant here (no pressure): rounding 1e-12 rad + the M interpolation
    R.check("C4 pm_turn M %.3f -> %.3f: err (rad), exact %.6f deg" % (Ma, Mb, np.degrees(ex)), num - ex,
            1e-9 if Ma > 1.1 else 1e-6)

# REJECTOR (R5): the C1 pressure check on the mean gas, applied to a table built with gamma 1 % too high
Gr = exact.PerfectGas(gm["gamma"], gm["R"], gm["T0"], gm["P0"])
_, ta_x = rv.model_table(1.01 * gm["gamma"], gm["R"], gm["T0"], gm["P0"], T_tab)
Ms_x = np.linspace(1.0, 1.3 * float(Gr.M_of_p(pa_abs)), 400)
p_x = np.asarray(A1.state_q(jnp.asarray(Gr.q(Ms_x)), ta_x)[1])
bound_x = (Gr.cp / gm["R"]) * dT ** 2 / (8.0 * float(Gr.T(Ms_x[-1])) ** 2)
R.reject("C1 mean: max rel err p, table built with gamma x1.01", float(np.max(np.abs(p_x / Gr.p(Ms_x) - 1.0))),
         4.0 * bound_x + 1e-12)

# figure
import matplotlib                                   # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                     # noqa: E402
fig, ax = plt.subplots(1, 2, figsize=(11, 4))
for name, (Ms, ep, er) in curves.items():
    ax[0].plot(Ms, ep, lw=1.0 if name != "mean" else 2.2, color="k" if name == "mean" else None,
               label=name if name in ("mean", "phase00", "phase06") else None)
ax[0].set_xlabel("Mach"); ax[0].set_ylabel("p_model / p_exact - 1")
ax[0].set_title("Gas tables vs closed form (13 gases)"); ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)
d = np.array([[r[1], r[2] - r[3]] for r in pm_rows])
ax[1].bar(range(len(pm_rows)), np.abs(np.array([r[2] - r[3] for r in pm_rows])) + 1e-18)
ax[1].set_yscale("log"); ax[1].set_xticks(range(len(pm_rows)))
ax[1].set_xticklabels(["%.2f-%.2f" % (r[0], r[1]) for r in pm_rows], fontsize=8)
ax[1].set_ylabel("|pm_turn - exact| [rad]"); ax[1].set_title("Prandtl-Meyer turn of the lip fan"); ax[1].grid(alpha=0.3)
rv.savefig(fig, "01_thermo_tables.png")
sys.exit(R.save(dict(worst=worst)))

#!/usr/bin/env python3
"""A1 BRICK 2, STEP 7 [F2/A1]: THE CYCLE LAYER — per-phase marches,
J = Int F dmu, the T3 ZERO-GAIN ORACLE, and the first mock-RDE cycle.

THE LAYER. An RDE nozzle sees a periodic family of chamber states, not
one: phase xi in [0,1) with the operating measure mu (O2: uniform in xi
= log-uniform in pressure for exponential blowdown). The cycle objective

$$ J_cycle(eps) = Int_0^1 F(eps; P0(xi), T0(xi)) dmu(xi)

is computed here by honest PER-PHASE MARCHES of the Brick-1 engine: each
phase gets its own stagnation state (h0(xi), s0(xi)) rebuilt from the
same EOS-general tables (h0 = h(T0), s0 = s0m(T0) - Rg ln(P0/PREF); the
reconstruction is verified against the table's own reference stagnation
as a build rejector). NO similarity shortcut is coded anywhere — the
collapse must EMERGE, that is the oracle.

STAGE=t3 (default) — THE ZERO-GAIN ORACLE (the hardest test the theory
owns, M0 T3 corollary C3): exponential pressure blowdown at FIXED T0
(PR = 10, P_CJ set so the time-mean <P0> equals the tables' reference
ps). Under pressure scaling the engine must reproduce the collapse:
  T3-1  the blind cycle optimizer lands on eps*(<P0>) — the classical
        design at the MEAN pressure;
  T3-2  ZERO GAIN: J_cycle(eps*(<P0>)) is not beaten beyond the derived
        flatness band — "cycle-aware" optimization buys NOTHING here;
  T3-3  rejector: designing at the PEAK pressure loses measurably;
  T3-4  Lemma A live: the per-phase WALLS at fixed eps coincide to
        near-roundoff across phases (pressure scaling does not move the
        geometry) — the similarity theorem observed in the engine.

STAGE=mock — THE FIRST MOCK RDE (user-posed): exponential P0 AND T0
profiles in theta (single-mode: theta = 2 pi xi), same mean pressure,
TR = PR^((gm-1)/gm) (isentropic-consistent; all values DECLARED mock
placeholders to be replaced by measured cycles). With T0 varying, the
exact collapse dies for real gas (T3's Lemma B needs calorically
perfect) — so "where does the optimization lead?" is measured, not
assumed: the cycle-optimal eps is compared against design-at-<P0>, the
shift and the Isp-equivalent penalty are REPORTED (observational; the
corpus gamma-probe predicts sub-percent shift and second-order
penalty), with the wrong-statistic designs evaluated for contrast.

Every march is cached (validation/_cycle_ckpt.json) — reruns resume.

Run:  .venv-a1/bin/python validation/a1_cycle_layer.py
      STAGE=mock .venv-a1/bin/python validation/a1_cycle_layer.py
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1              # noqa: E402
import a1_thrust_functional as TF            # noqa: E402

import jax.numpy as jnp                      # noqa: E402

EPS = A1.EPS
CASE = A1.CASE
K_RICH = A1.K_RICH
CKPT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                    "_cycle_ckpt.json")
NPASS = [0, 0]
NXI = 5                       # phase quadrature (midpoint rule on xi)
PR = 10.0                     # blowdown spread of the mock cycles


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def phase_tab(tab0, P0, T0):
    """Per-phase stagnation state, RELATIVE to the tables' own
    reference (ts, ps) on the same property tables — zero-point
    conventions of the plt file are inherited, never re-derived."""
    t = dict(tab0)
    T = np.array(tab0["T"])
    h_of = lambda TT: float(np.interp(TT, T, np.array(tab0["h"])))
    s_of = lambda TT: float(np.interp(TT, T, np.array(tab0["s0m"])))
    t["h0"] = tab0["h0"] + h_of(T0) - h_of(tab0["ts"])
    t["s0"] = tab0["s0"] + (s_of(T0) - s_of(tab0["ts"])) \
        - tab0["Rg"] * np.log(P0 / tab0["ps"])
    t["ts"], t["ps"] = float(T0), float(P0)
    return A1.prep_tab(t)


def march_F(eps, P0, T0, pa, tab0, ck):
    key = "%.6f:%.6e:%.3f" % (eps, P0, T0)
    if key in ck:
        r = ck[key]
    else:
        t = phase_tab(tab0, P0, T0)
        ta = A1.tab_arrays(t)
        P = jnp.array([CASE["yt"], CASE["rtu"], CASE["rtd"], eps])
        cfg = dict(NI=CASE["NI"], Ne=CASE["Ne"], da_deg=CASE["da_deg"])
        out, _ = A1.run_march(P, t, cfg)
        qe = float(TF.solve_qe(out["Me"], ta, t["_as"]))
        pe = float(A1.state_q(jnp.float64(qe), ta)[1])
        r = dict(mdot=float(out["mdot"]), qe=qe, pe=pe,
                 ylip=float(out["wall_y"][-1]), Me=float(out["Me"]),
                 wall_y=[float(v) for v in np.array(out["wall_y"])])
        ck[key] = r
        json.dump(ck, open(CKPT, "w"))
    return (r["mdot"] * r["qe"]
            + (r["pe"] - pa) * np.pi * r["ylip"] ** 2), r


def eps_star_of(P0, T0, Me_t, tab0, pa_out=False):
    """Closed-form eps* for a steady chamber at (P0, T0): the eps whose
    exit Mach Me_t gives p_e = pa (exit-area lemma), via the area law."""
    t = phase_tab(tab0, P0, T0)
    ta = A1.tab_arrays(t)
    qt = float(TF.solve_qe(jnp.float64(Me_t), ta, t["_as"]))
    stq = A1.state_q(jnp.float64(qt), ta)
    pa, rho_t = float(stq[1]), float(stq[2])
    # mdot of this phase (IVL Simpson — same formulas as the march)
    F, md = TF.ivl_flux(jnp.array([CASE["yt"], CASE["rtu"],
                                   CASE["rtd"], CASE["eps"]]), t, ta)
    eps = float(md) / (np.pi * CASE["yt"] ** 2 * rho_t * qt)
    return (eps, pa) if pa_out else eps


def eps_star_at_pa(P0, T0, pa, tab0):
    """eps* that expands THIS phase's stagnation down to the GIVEN
    ambient: solve p(q) = pa under this phase's stagnation, then the
    area law. (This is what 'design at the peak pressure' means — the
    fixed-Me variant is pressure-blind and was rejected as a bug.)"""
    from scipy.optimize import brentq
    t = phase_tab(tab0, P0, T0)
    ta = A1.tab_arrays(t)

    def pres(q):
        return float(A1.state_q(jnp.float64(q), ta)[1]) - pa
    qt = brentq(pres, 1.05 * t["_as"], 3.2 * t["_as"], xtol=1e-8)
    stq = A1.state_q(jnp.float64(qt), ta)
    rho_t = float(stq[2])
    F, md = TF.ivl_flux(jnp.array([CASE["yt"], CASE["rtu"],
                                   CASE["rtd"], CASE["eps"]]), t, ta)
    return float(md) / (np.pi * CASE["yt"] ** 2 * rho_t * qt)


def main():
    t0 = time.time()
    stage = os.environ.get("STAGE", "t3")
    print("== A1 brick 2 step 7: cycle layer [F2/A1] (stage=%s) =="
          % stage)
    tab0 = A1.prep_tab(A1.build_tab_nasa())
    ts, ps = tab0["ts"], tab0["ps"]

    # build rejector: stagnation reconstruction reproduces the tables'
    # own reference (h0, s0) at (ts, ps)
    tr = phase_tab(tab0, ps, ts)
    dh = abs(tr["h0"] - tab0["h0"]) / abs(tab0["h0"])
    ds = abs(tr["s0"] - tab0["s0"]) / abs(tab0["s0"])
    # rejector: (i) reference reproduced (relative construction makes
    # this exact); (ii) LEMMA-A LAW: doubling P0 at fixed T0 must scale
    # the static pressure at fixed speed by exactly 2 (the engine-level
    # content of pressure-scaling similarity)
    ta_r = A1.tab_arrays(tr)
    t2 = phase_tab(tab0, 2.0 * ps, ts)
    ta_2 = A1.tab_arrays(t2)
    qprobe = jnp.float64(1.7 * tr["_as"])
    p1 = float(A1.state_q(qprobe, ta_r)[1])
    p2 = float(A1.state_q(qprobe, ta_2)[1])
    dsc = abs(p2 / p1 - 2.0)
    print("  stagnation: ref reproduction dh=%.1e ds=%.1e ;"
          " pressure-scaling law |p(2P0)/p(P0) - 2| = %.2e"
          % (dh, ds, dsc))
    check("phase-tab rejector: reference exact AND scaling law holds",
          dh < 1e-12 and ds < 1e-12 and dsc < 1e-10)

    xi = (np.arange(NXI) + 0.5) / NXI            # midpoint quadrature
    I1 = (1.0 - 1.0 / PR) / np.log(PR)           # O2 closed form
    P_CJ = ps / I1                               # so <P0> = ps
    P0s = P_CJ * PR ** (-xi)
    Pmean = ps
    ck = json.load(open(CKPT)) if os.path.exists(CKPT) else {}

    if stage == "t3":
        T0s = np.full(NXI, ts)                   # FIXED T0: T3 class
    else:
        gm = tab0["gammamedio"]
        TR = PR ** ((gm - 1.0) / gm)             # isentropic-consistent
        T_CJ = 3850.0                            # peak T at wave passage;
        # bounded INSIDE table validity [T_TAB_LO, T_TAB_HI] (a first
        # run with geometric centering pushed T0 to 4162 K, past the
        # 3900 K table edge — np.interp CLAMPS silently: caught, fixed,
        # and now guarded by the range rejector below)
        T0s = T_CJ * TR ** (-xi)
        print("  mock cycle: TR = %.4f, T0 in [%.0f, %.0f] K"
              % (TR, T0s.min(), T0s.max()))
        check("table-range rejector: all phase T0 inside tables",
              T0s.max() < A1.T_TAB_HI - 10 and T0s.min()
              > A1.T_TAB_LO + 10)
    print("  cycle: PR = %.1f, P_CJ = %.4e, <P0> = %.4e, %d phases"
          % (PR, P_CJ, Pmean, NXI))

    # ambient posed from the MEAN phase at target Me 2.8 (interior opt)
    eps_mean, pa = eps_star_of(Pmean, ts, 2.80, tab0, pa_out=True)
    print("  pa = %.6e ; closed-form eps*(<P0>, ts) = %.6f"
          % (pa, eps_mean))

    def J_cycle(eps):
        F = 0.0
        for k in range(NXI):
            Fk, _ = march_F(round(eps, 6), P0s[k], T0s[k], pa, tab0, ck)
            F += Fk
        return F / NXI

    print("-- golden search on J_cycle (blind, [4.2, 6.4]) --")
    gr = 0.5 * (np.sqrt(5.0) - 1.0)
    a, b = 4.2, 6.4
    c, d = b - gr * (b - a), a + gr * (b - a)
    fc, fd = J_cycle(c), J_cycle(d)
    nev = 2
    while b - a > 0.06:
        if fc > fd:
            b, d, fd = d, c, fc
            c = b - gr * (b - a)
            fc = J_cycle(c)
        else:
            a, c, fc = c, d, fd
            d = a + gr * (b - a)
            fd = J_cycle(d)
        nev += 1
        print("    bracket [%.4f, %.4f]  (%d evals, %.0f s)"
              % (a, b, nev, time.time() - t0))
    eps_gs = 0.5 * (a + b)
    Jgs = J_cycle(eps_gs)
    Jmean = J_cycle(eps_mean)
    # flatness band: J is quadratic at the top; derive from the golden
    # window curvature
    band_flat = K_RICH * abs(J_cycle(round(eps_mean + 0.06, 6)) - Jmean)
    print("  eps_gs = %.5f vs eps*(<P0>) = %.5f  (|d| = %.4f)"
          % (eps_gs, eps_mean, abs(eps_gs - eps_mean)))
    print("  J(eps_gs) - J(eps*mean) = %+.4e  (flatness band %.4e)"
          % (Jgs - Jmean, band_flat))

    if stage == "t3":
        check("T3-1 blind cycle optimum == design at the MEAN pressure",
              abs(eps_gs - eps_mean) <= 0.06 + 0.01)
        check("T3-2 ZERO GAIN: no improvement over Rao-at-<P0> beyond"
              " band", Jgs - Jmean <= band_flat)
        eps_peak = eps_star_at_pa(P_CJ, ts, pa, tab0)
        Jpk = J_cycle(round(eps_peak, 6))
        print("  wrong statistic: eps*(P_CJ) = %.4f -> J = %.6e"
              " (loss %+.4e)" % (eps_peak, Jpk, Jpk - Jmean))
        check("T3-3 rejector: peak design measurably loses (> 10x"
              " band)", Jmean - Jpk > 10.0 * band_flat)
        # T3-4: Lemma A live — per-phase walls at eps_mean coincide
        wys = []
        for k in range(NXI):
            key = "%.6f:%.6e:%.3f" % (round(eps_mean, 6), P0s[k], T0s[k])
            wys.append(np.array(ck[key]["wall_y"]))
        nmin = min(len(w) for w in wys)
        dev = max(float(np.max(np.abs(w[:nmin] - wys[0][:nmin])))
                  for w in wys[1:])
        print("  T3-4: max wall deviation across phases at fixed eps ="
              " %.3e (y_t units)" % dev)
        check("T3-4 Lemma A live: pressure scaling does not move the"
              " wall (< 1e-9)", dev < 1e-9)
    else:
        # MOCK RDE: observational findings, corpus-style reporting.
        # Honest reference = design at the MEAN STATE: mean pressure at
        # the cycle's log-mean temperature, SAME ambient (eps*(<P>, ts)
        # would use a temperature the cycle never visits).
        T_ref = float(np.exp(np.mean(np.log(T0s))))
        T_pw = float(np.sum(P0s * T0s) / np.sum(P0s))
        eps_lm = eps_star_at_pa(Pmean, T_ref, pa, tab0)
        eps_pw = eps_star_at_pa(Pmean, T_pw, pa, tab0)
        J_lm = J_cycle(round(eps_lm, 6))
        J_pw = J_cycle(round(eps_pw, 6))
        print("  references: eps*(<P>, ts=%.0f) = %.5f | log-mean"
              " T=%.0f -> %.5f | PRESSURE-WEIGHTED T=%.0f -> %.5f"
              % (ts, eps_mean, T_ref, eps_lm, T_pw, eps_pw))
        print("  shifts of the cycle optimum: vs ts-ref %+.3f%% | vs"
              " log-mean %+.3f%% | vs pressure-weighted %+.3f%%"
              % (100 * (eps_gs - eps_mean) / eps_mean,
                 100 * (eps_gs - eps_lm) / eps_lm,
                 100 * (eps_gs - eps_pw) / eps_pw))
        shift = (eps_gs - eps_pw) / eps_pw
        print("-- mock-RDE findings (observational) --")
        print("  penalty of the PRESSURE-WEIGHTED design under the"
              " true cycle: %+.4e (%.2e rel; flatness band %.2e rel)"
              % (Jgs - J_pw, (Jgs - J_pw) / abs(J_pw),
                 band_flat / abs(J_pw)))
        print("  penalty of the log-mean design: %+.4e (%.2e rel)"
              % (Jgs - J_lm, (Jgs - J_lm) / abs(J_lm)))
        eps_peak = eps_star_at_pa(P_CJ, T0s[0], pa, tab0)
        Jpk = J_cycle(round(eps_peak, 6))
        print("  contrast, wrong statistic: eps*(peak) = %.4f -> loss"
              " %+.4e" % (eps_peak, Jpk - Jgs))
        check("MOCK-1 optimum exists inside the bracket (not at an"
              " edge)", 4.2 + 0.06 < eps_gs < 6.4 - 0.06)
        check("MOCK-2 weighted-average lesson: pressure-weighted"
              " reference beats log-mean (derived comparison)",
              abs(eps_gs - eps_pw) < abs(eps_gs - eps_lm))
        check("MOCK-3 pressure-weighted design penalty is second-order"
              " (<= 10x flatness band)", Jgs - J_pw <= 10.0 * band_flat)
        check("MOCK-4 peak design still loses under the true cycle",
              Jpk < max(Jgs, Jmean))

    print("== %d/%d PASS  (%.1f s, %d J evals) ==" %
          (NPASS[0], NPASS[1], time.time() - t0, nev + 3))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()

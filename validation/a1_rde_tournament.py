#!/usr/bin/env python3
"""A1 [F3/A1] S41 2026-09-27: THE RDE NOZZLE TOURNAMENT -- the Q2D THOR_CAv3
outflow (thermally choked, supersonic at every azimuth) expanded in two-wall
nozzles designed on the Stechmann TIME-MEAN state against nozzles designed
with the PHASES VOTING. Registry ID: [X-RDET].

THE DATA. One snapshot of the exit line holds a whole period of the single
rotating wave (T0: the state at a point depends on theta - Omega t, so a
period at a point is every angle at an instant). Equal azimuthal sectors are
equal durations: the phase family's weights are uniform.

THE STECHMANN STATE (Stechmann, Heister & Harroun 2019): gamma and M frozen,
the nozzle designed at the TIME-MEAN chamber state -- here the theta-mean of
the exit's meridional stagnation state (P0, T0, gamma, R, M_x); the
mass-weighted mean is reported as the sensitivity.

STAGES (STAGE=family | gates): family writes the gas file of the Stechmann
state and the phase families; gates checks the carrier's new options on the
tournament posing (the default path bitwise; one phase = the posing's own
state; the separation closure inert when nothing separates and a smooth
image of the hard cut when a wall detaches).

Run:  STAGE=family .venv-a1/bin/python validation/a1_rde_tournament.py
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HERE = os.path.dirname(os.path.abspath(__file__))
CASES = {k: v["value"] for k, v in json.load(open(os.path.join(HERE, "rde_tournament_cases.json"))).items()
         if not k.startswith("_")}
ART = os.path.join(HERE, "_rde_tournament")
BAR = CASES["units"]["bar_Pa"]
NPASS = [0, 0]


def say(*a):
    print(*a, flush=True)


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    say("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def exit_states():
    """The exit line's meridional stagnation state per azimuthal cell."""
    C = CASES["source"]
    d = np.load(os.path.join(HERE, C["npz"]))
    u, v, p, T, g, R = (d[k + "_last"] for k in ("u", "v", "p", "T", "g", "R"))
    rho = sum(d["rho(%d)_last" % k] for k in range(1, len([n for n in d["names"] if str(n).startswith("rho")]) + 1))
    a = np.sqrt(g * R * T)
    Mx = u / a
    fac = 1 + (g - 1) / 2 * Mx ** 2
    return dict(p=p, T=T, u=u, v=v, g=g, R=R, rho=rho, Mx=Mx, T0=T * fac, P0=p * fac ** (g / (g - 1)), t=float(d["t"]))


def family():
    say("== [F3/A1] the RDE tournament: the Stechmann state and the phase families [X-RDET] (stage family) ==")
    C = CASES["source"]
    E = exit_states()
    n = len(E["p"])
    A_in = np.pi * (C["r_out_m"] ** 2 - (C["r_out_m"] - C["gap_exit_m"]) ** 2)
    mdot_q2d = float(np.mean(E["rho"] * E["u"])) * A_in
    tm = {k: float(np.mean(E[k])) for k in ("g", "R", "T0", "P0", "Mx")}
    w_ = E["rho"] * E["u"]
    mw = {k: float(np.sum(w_ * E[k]) / np.sum(w_)) for k in ("g", "R", "T0", "P0", "Mx")}
    say("   t %.4f ms, %d azimuthal cells, all supersonic (M_x %.3f .. %.3f); mass flow through the inlet annulus %.4f kg/s"
        % (1e3 * E["t"], n, E["Mx"].min(), E["Mx"].max(), mdot_q2d))
    say("   STECHMANN (time-mean): gamma %.5f R %.3f T0 %.1f K P0 %.5f bar M_x %.5f" % (tm["g"], tm["R"], tm["T0"], tm["P0"] / BAR, tm["Mx"]))
    say("   mass-weighted (sensitivity): gamma %.5f R %.3f T0 %.1f K P0 %.5f bar M_x %.5f" % (mw["g"], mw["R"], mw["T0"], mw["P0"] / BAR, mw["Mx"]))
    gas = dict(geno_run=C["geno_run"], gamma=tm["g"], R=tm["R"], T0=tm["T0"], P0=tm["P0"], M_in=tm["Mx"], T_tab=C["T_tab"],
               note="the Stechmann time-mean state of the Q2D THOR_CAv3 exit (theta-arithmetic means)")
    fg_ = os.path.join(ART, "gas_stechmann.json")
    json.dump(gas, open(fg_ + ".tmp", "w"), indent=1)
    os.replace(fg_ + ".tmp", fg_)
    swirl = float(np.mean(E["v"] ** 2) / np.mean(E["u"] ** 2 + E["v"] ** 2))
    say("   swirl: kinetic-energy fraction <v^2>/<u^2+v^2> = %.4f (not in the meridional march: declared)" % swirl)
    for K in C["families"]:
        edges = np.linspace(0, n, K + 1).round().astype(int)
        ph = []
        for k in range(K):
            s_ = slice(edges[k], edges[k + 1])
            ph.append(dict(w=float(edges[k + 1] - edges[k]) / n, gamma=float(np.mean(E["g"][s_])), R=float(np.mean(E["R"][s_])),
                           T0=float(np.mean(E["T0"][s_])), P0=float(np.mean(E["P0"][s_])), M=float(np.mean(E["Mx"][s_])),
                           mdot=float(np.mean((E["rho"] * E["u"])[s_]) * A_in), v=float(np.mean(E["v"][s_]))))
        md = sum(p_["w"] * p_["mdot"] for p_ in ph)
        import a1_ideal_march_jax as A1
        check("family K %d: the sectors' mean mass flow %.5f kg/s = the exit's %.5f (sector means of rho u; rounding band K_RICH eps n)"
              % (K, md, mdot_q2d), abs(md - mdot_q2d) <= A1.K_RICH * A1.EPS * n * mdot_q2d)
        fn_ = os.path.join(ART, "family_K%d.json" % K)
        json.dump(dict(K=K, source=C["npz"], T_tab=C["T_tab"], phases=ph), open(fn_ + ".tmp", "w"), indent=1)
        os.replace(fn_ + ".tmp", fn_)                     # atomic: a walk may be reading it
        say("   K %d: P0 %.3f .. %.3f bar, M %.3f .. %.3f, gamma %.4f .. %.4f" % (K, min(p_["P0"] for p_ in ph) / BAR, max(p_["P0"] for p_ in ph) / BAR,
                                                                     min(p_["M"] for p_ in ph), max(p_["M"] for p_ in ph),
                                                                     min(p_["gamma"] for p_ in ph), max(p_["gamma"] for p_ in ph)))
    say("   %d/%d PASS" % tuple(NPASS))
    return 0 if NPASS[0] == NPASS[1] else 1


def _tw(env):
    """A TwoWall under the given environment (the carrier re-read)."""
    import importlib
    # EVERY carrier switch cleared (a fixed list once left TWOP_JET set from
    # the previous build: JT-2's "without the jet" march ran with it)
    for k in [k_ for k_ in os.environ if k_.startswith("TWOP_")]:
        os.environ.pop(k, None)
    os.environ.update({k: str(v) for k, v in env.items()})
    import a1_twowall as T
    importlib.reload(T)
    return T, T.TwoWall(verbose=False)


def gates():
    say("== [F3/A1] the RDE tournament: the carrier's new options gated [X-RDET] (stage gates) ==")
    import jax
    import jax.numpy as jnp
    C, G = CASES["source"], CASES["gates"]
    t0 = time.time()
    # T-0 the extended table: the closed-form isentrope at the Stechmann exit
    import a1_ideal_march_jax as A1_
    import a1_twowall as T_
    GS0 = json.load(open(os.path.join(ART, "gas_stechmann.json")))
    g_, R_, T0_, P0_ = GS0["gamma"], GS0["R"], GS0["T0"], GS0["P0"]
    NPR_ = P0_ / (C["pa_bar"] * BAR)
    Me_ = np.sqrt(2 / (g_ - 1) * (NPR_ ** ((g_ - 1) / g_) - 1))
    Te_ = T0_ / (1 + (g_ - 1) / 2 * Me_ ** 2)
    qe_ = Me_ * np.sqrt(g_ * R_ * Te_)
    pe_ex = P0_ * (Te_ / T0_) ** (g_ / (g_ - 1))
    tx = A1_.tab_arrays(A1_.prep_tab(T_.tab_gconst(g_, R_, T0_, P0_, GS0["T_tab"])))
    tb = A1_.tab_arrays(A1_.prep_tab(A1_.build_tab_gconst(g=g_, Rg=R_, ts=T0_, ps=P0_)))
    pe_x = float(A1_.state_q(jnp.float64(qe_), tx)[1])
    pe_b = float(A1_.state_q(jnp.float64(qe_), tb)[1])
    # the band: the linear interpolation of s0m = cp ln T on the grid, dT^2 /
    # (8 T^2) in ln T, times g/(g-1) in ln p (derived from the table itself)
    dT_ = (GS0["T_tab"][1] - GS0["T_tab"][0]) / (A1_.N_TAB - 1)
    band0 = T_.K_RICH * (g_ / (g_ - 1)) * (dT_ / Te_) ** 2 / 8
    check("T-0 the extended table at the Stechmann exit (M %.4f, T %.1f K): p %.3f Pa vs the closed-form isentrope %.3f (rel %.1e"
          " <= the grid's interpolation band %.1e); REJECTOR the builder's [1050, 3900] K table clamps there: %.1f Pa (rel %.1e)"
          % (Me_, Te_, pe_x, pe_ex, abs(pe_x / pe_ex - 1), band0, pe_b, abs(pe_b / pe_ex - 1)),
          abs(pe_x / pe_ex - 1) <= band0 and abs(pe_b / pe_ex - 1) > band0)
    # T-1 the default path bitwise (the S41 step-2 record's start)
    R = json.load(open(os.path.join(HERE, "_twowall_cap0.8_atL/walk_TN_2026-09-26.json")))
    T, tw = _tw(dict(TWOP_KERNEL="arc", TWOP_CAP="0.8", TWOP_U0="10"))
    o, _ = tw.march_record(np.asarray(R["W_start"], float))
    check("T-1 the default posing after the edits: J %.12f = the S41 record %.12f (bitwise)" % (float(tw.J_of(o)), R["CF_start"]),
          float(tw.J_of(o)) == R["CF_start"])
    # T-2 a gas file carrying the default constants reproduces the default bitwise
    ST = T.ST
    gdef = dict(geno_run=T.POSE["geno_run"], gamma=ST.GAMMA, R=ST.R_UNIV / ST.MOLAR_MASS, T0=ST.T0, P0=ST.P0, M_in=ST.M_INLET)
    fdef = os.path.join(ART, "gas_default_gate.json")
    json.dump(gdef, open(fdef, "w"))
    T, tw2 = _tw(dict(TWOP_KERNEL="arc", TWOP_CAP="0.8", TWOP_U0="10", TWOP_GAS=fdef))
    o2, _ = tw2.march_record(np.asarray(R["W_start"], float))
    check("T-2 TWOP_GAS with the default constants: J %.12f (bitwise with T-1)" % float(tw2.J_of(o2)), float(tw2.J_of(o2)) == R["CF_start"])
    os.remove(fdef)
    # the tournament posing
    gas = os.path.join(ART, "gas_stechmann.json")
    GS = json.load(open(gas))
    pa = C["pa_bar"] * BAR / GS["P0"]
    env = dict(TWOP_KERNEL="arc", TWOP_CAP=G["cap"], TWOP_U0=G["u0"], TWOP_FREE_EXIT="lip", TWOP_GAS=gas, TWOP_PA=pa,
               TWOP_SHAPE="1", TWOP_NOPLUME="1")
    T, tw = _tw(env)
    W = T.trunc_start(tw)
    o, S = tw.march_record(W)
    Jl, Jg = float(tw.J_of(o)), float(tw._J_gen(o, tw._ctx()))
    check("T-3 the gauge form = the legacy thrust on the tournament posing (Stechmann cut at %.1f, p_a %.3f bar): %.12f vs %.12f"
          " (|d| %.1e <= %.1e)" % (G["cap"], C["pa_bar"], Jg, Jl, abs(Jg - Jl), T.K_RICH * T.A1.EPS * len(o["wall"])),
          abs(Jg - Jl) <= T.K_RICH * T.A1.EPS * len(o["wall"]))
    # T-4 one phase = the posing's own state
    f1 = os.path.join(ART, "family_gate_one.json")
    json.dump(dict(K=1, phases=[dict(w=1.0, gamma=GS["gamma"], R=GS["R"], T0=GS["T0"], P0=GS["P0"], M=GS["M_in"])]), open(f1, "w"))
    T, twm = _tw(dict(env, TWOP_MU=f1))
    om, Sm = twm.march_record(W)
    Jr = float(twm.J_replay(jnp.asarray(W), Sm))
    check("T-4 TWOP_MU with one phase = the posing's state: record %.12f, replay %.12f, single %.12f (bitwise record = single)"
          % (om["J_mu"], Jr, Jg), om["J_mu"] == Jg and abs(Jr - Jg) <= T.K_RICH * T.A1.EPS * len(o["wall"]))
    os.remove(f1)
    # T-5 the separation closure: inert when nothing detaches, a smooth hard cut when a wall does
    T, tws = _tw(dict(env, TWOP_SEP="summerfield"))
    os_, _ = tws.march_record(W)
    Js = float(tws.J_of(os_))
    rd = tws.sep_readout(os_)
    check("T-5a Summerfield at the tournament ambient: nothing detaches on the cut Stechmann nozzle (%s) and J %.12f = %.12f"
          % (rd, Js, Jg), rd["wall"] is None and rd["shroud"] is None and abs(Js - Jg) <= T.K_RICH * T.A1.EPS * len(o["wall"]))
    pa_hi = G["over_pa_bar"] * BAR / GS["P0"]
    T, twa = _tw(dict(env, TWOP_PA=pa_hi))
    oa, _ = twa.march_record(W)
    Ja = float(twa._J_gen(oa, twa._ctx()))
    T, twb = _tw(dict(env, TWOP_PA=pa_hi, TWOP_SEP="summerfield"))
    ob, _ = twb.march_record(W)
    Jb = float(twb.J_of(ob))
    rdb = twb.sep_readout(ob)
    # the hard cut: the gauge pushes truncated at the first point below p_sep
    ctx = twb._ctx()
    pa_abs = twb.pa * twb.P0

    def hard(pts, y0, thr):
        # the hard cut: the gauge push kept up to the first point whose margin
        # p_w / p_sep - 1 falls below thr (thr 0 = the criterion itself)
        c, p_, att = twb._gauge_push(pts, y0, ctx, pa_abs, attach=True)
        c, p_ = np.asarray(c), np.asarray(p_)
        M_ = np.asarray(T.A1.state_q(jnp.asarray(np.hypot(c[:, 2], c[:, 3])), ctx["ta"])[5])
        ok_ = np.cumprod(p_ / np.asarray(twb._p_sep(jnp.asarray(M_), pa_abs)) - 1.0 >= thr).astype(float)
        g_ = (0.5 * (p_[1:] + p_[:-1]) - pa_abs) * 0.5 * (ok_[1:] + ok_[:-1])
        return float(np.sum(g_ * 2 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1]) * np.diff(c[:, 1])))

    def Jcut(thr):
        return float((ctx["F_in"] - pa_abs * np.pi * (twb.y_u ** 2 - twb.y_l ** 2) - hard(ob["wall"], twb.y_l, thr)
                      + hard(ob["shroud"], twb.y_u, thr)) / (twb.P0 * twb.A_star))
    # the smooth closure's transition: sigmoid(+-3) = 0.953 / 0.047 -- the
    # hard cuts at margins +-3 widths bracket 90 % of it
    w3 = 3.0 * T.CASES["separation"]["width"]
    J0c, Jlo, Jhi = Jcut(0.0), Jcut(-w3), Jcut(w3)
    check("T-5b at p_a %.2f bar a wall detaches (%s): the closure J %.6f lies between the hard cuts at margins -/+3 widths"
          " (%.6f, %.6f; the criterion's own %.6f; attached %.6f)" % (G["over_pa_bar"], rdb, Jb, Jlo, Jhi, J0c, Ja),
          (rdb["wall"] is not None or rdb["shroud"] is not None) and min(Jlo, Jhi) <= Jb <= max(Jlo, Jhi))
    # T-6 the phase-voting replay gradient against central differences (K 12)
    T, twv = _tw(dict(env, TWOP_MU=os.path.join(ART, "family_K12.json"), TWOP_SEP="summerfield"))
    ov, Sv = twv.march_record(W)
    Jv = float(twv.J_replay(jnp.asarray(W), Sv))
    gv = np.asarray(jax.grad(lambda z: twv.J_replay(z, Sv))(jnp.asarray(W)))
    k_, h_ = G["knot"], G["fd_step"]
    e_ = np.zeros(len(W)); e_[k_] = h_
    fd = (float(twv.J_replay(jnp.asarray(W + e_), Sv)) - float(twv.J_replay(jnp.asarray(W - e_), Sv))) / (2 * h_)
    check("T-6 phases voting (K 12, Summerfield): record J_mu %.9f = replay %.9f; d/d(knot %d) adjoint %+.6e vs central FD %+.6e"
          " (rel %.1e); worst certificate %.3f; per-phase C_F %s" % (ov["J_mu"], Jv, k_, gv[k_], fd, abs(gv[k_] - fd) / max(abs(fd), T.A1.EPS),
                                                                      ov["cert_worst"], np.array2string(np.array(ov["J_phase"]), precision=4)),
          abs(Jv - ov["J_mu"]) <= T.K_RICH * T.A1.EPS * len(o["wall"]) * len(twv.phases)
          and abs(gv[k_] - fd) <= max(T.K_RICH * abs(fd) * h_ ** 0.5, T.A1.EPS ** 0.5))
    # T-7 the table box (engine-core:F3-table-clamp-silent): a state outside
    # the table reads T pinned at its edge EXACTLY (jnp.interp), so every
    # phase's coldest state over the whole net must lie strictly above T_tab[0]
    tmins = []
    for o_k, ph in zip(ov["outs"], twv.phases):
        pts = np.asarray(o_k["mesh_pts"])
        tmins.append(float(np.min(np.asarray(T.A1.state_q(jnp.asarray(np.hypot(pts[:, 2], pts[:, 3])), ph["ta"])[0]))))
    check("T-7 the table box: every phase's coldest state inside the table (T_min %.1f .. %.1f K > T_tab[0] %.1f K; the builder's"
          " range [%.0f, ...] K would clamp %d of %d phases)" % (min(tmins), max(tmins), C["T_tab"][0], T.A1.T_TAB_LO,
                                                                 sum(1 for t_ in tmins if t_ <= T.A1.T_TAB_LO), len(tmins)),
          min(tmins) > C["T_tab"][0])
    say("   %d/%d PASS in %.0f s" % (NPASS[0], NPASS[1], time.time() - t0))
    return 0 if NPASS[0] == NPASS[1] else 1


def load_designs():
    """The tournament's designs: {name: (W, provenance)} -- the walk's record,
    else its checkpoint (a walk still running: 'checkpoint after n segments'),
    else absent."""
    out = {}
    for name, ref in CASES["eval"]["designs"].items():
        start = ref.startswith("start:")
        fn = os.path.join(HERE, ref[len("start:"):] if start else ref)
        if os.path.exists(fn):
            R_ = json.load(open(fn))
            out[name] = (np.asarray(R_["W_start" if start else "W"], float), "start of " + ref[len("start:"):] if start else "record")
            continue
        ck = os.path.join(os.path.dirname(fn), "walk_TN_checkpoint.json")
        if not start and os.path.exists(ck):
            C_ = json.load(open(ck))
            out[name] = (np.asarray(C_["W"], float), "checkpoint after %d segments (walk running)" % int(C_["segments"]))
    return out


def evaluate():
    """Every design of the tournament judged by every evaluator (the mean
    state, the phase families) under the same closure (TWOP_SEP as the walks
    ran): C_F in units of the Stechmann P0 A*, the thrust in N, the specific
    impulse on the Q2D mass flow, the gain over no nozzle, per phase the C_F,
    the certificate, the class margin and where each wall detaches."""
    say("== [F3/A1] the RDE tournament: the designs judged [X-RDET] (stage eval) ==")
    C, E = CASES["source"], CASES["eval"]
    gas = os.path.join(ART, "gas_stechmann.json")
    GS = json.load(open(gas))
    base = dict(TWOP_KERNEL="arc", TWOP_CAP=CASES["gates"]["cap"], TWOP_U0=CASES["gates"]["u0"], TWOP_FREE_EXIT="lip",
                TWOP_GAS=gas, TWOP_PA=C["pa_bar"] * BAR / GS["P0"], TWOP_SHAPE="1", TWOP_NOPLUME="1",
                TWOP_SEP=os.environ.get("TWOP_SEP", "summerfield"))
    LD = load_designs()
    designs = {k: v[0] for k, v in LD.items()}
    prov = {k: v[1] for k, v in LD.items()}
    say("   designs: %s; closure %s; p_a %.3f bar" % ("; ".join("%s (%s)" % (k, prov[k]) for k in sorted(designs)),
                                                   base["TWOP_SEP"] or "none", C["pa_bar"]))
    mdot = None
    res = {}
    floor0 = json.load(open(os.path.join(ART, "stech", "class_2026-09-27.json")))["floors"][0]
    for ev in E["evaluators"]:
        # "family_K12.json+swirl": the phases with their free vortex (TWOP_SWIRL)
        fam, _, opt = ev.partition("+")
        env = dict(base) if fam == "mean" else dict(base, TWOP_MU=os.path.join(ART, fam))
        if opt == "swirl":
            env["TWOP_SWIRL"] = "1"
        T, tw = _tw(env)
        mg = tw.margin_dict(mu0=0.0, rho=CASES_TW_RHO(), m_ref=1.0)
        A_phys = tw.A_star * C["r_out_m"] ** 2
        if mdot is None:
            mdot = json.load(open(os.path.join(ART, "family_K12.json")))
            mdot = sum(p_["w"] * p_["mdot"] for p_ in mdot["phases"])
        # no nozzle: the inlet line alone in the p_a gauge
        ctxs = tw.phases if tw.phases is not None else [tw._ctx()]
        pa_abs = tw.pa * tw.P0
        J0 = sum(c_["w"] * (c_["F_in"] - pa_abs * np.pi * (tw.y_u ** 2 - tw.y_l ** 2)) for c_ in ctxs) / (tw.P0 * tw.A_star)
        res[ev] = dict(J0=J0)
        for name, W in designs.items():
            o, _ = tw.march_record(W, margin=dict(mg))
            J = float(tw.J_of(o))
            per = []
            outs = o.get("outs", [o])
            for k, (o_k, c_) in enumerate(zip(outs, ctxs)):
                # the exit's wall pressures over p_a (the lip: < 1 = an over-expanded
                # lip, a lip shock in the jet) and the smallest separation margin
                # p_w / p_sep - 1 over both walls (< 0 = detached under the criterion)
                pr = {}
                msep = None
                for key in ("wall", "shroud"):
                    pts = np.asarray(o_k[key])
                    c_q = np.hypot(pts[:, 2], pts[:, 3])
                    if c_.get("G2", 0.0) > 0.0:
                        import a1_swirl_march as SW
                        st_ = SW.state_sw(c_q, pts[:, 1], c_["G2"], c_["ta"])
                    else:
                        st_ = T.A1.state_q(c_q, c_["ta"])
                    p_ = np.asarray(st_[1])
                    pr[key] = float(p_[-1] / pa_abs)
                    if tw.sep:
                        m_ = float(np.min(p_ / np.asarray(tw._p_sep(st_[5], pa_abs)) - 1.0))
                        msep = m_ if msep is None else min(msep, m_)
                # the table box (engine-core:F3-table-clamp-silent): the net's coldest state
                mp_ = np.asarray(o_k["mesh_pts"])
                q_ = np.hypot(mp_[:, 2], mp_[:, 3])
                if c_.get("G2", 0.0) > 0.0:
                    import a1_swirl_march as SW
                    T_min = float(np.min(np.asarray(SW.state_sw(q_, mp_[:, 1], c_["G2"], c_["ta"])[0])))
                else:
                    T_min = float(np.min(np.asarray(T.A1.state_q(q_, c_["ta"])[0])))
                per.append(dict(J=float(tw._J_gen(o_k, c_)), cert=float(o_k["cert_worst"]),
                                ks=(None if o_k.get("margin_ks") is None else float(o_k["margin_ks"])),
                                sep=tw.sep_readout(o_k, c_), P0=c_["P0"], M=c_["M"], p_tip=pr["wall"], p_lip=pr["shroud"],
                                m_sep=msep, T_min=T_min))
            F = J * tw.P0 * A_phys
            res[ev][name] = dict(J=J, F_N=F, Isp=F / (mdot * E["g0"]), gain=J - J0, per=per,
                                 cert=float(o["cert_worst"]), ks=(None if o.get("margin_ks") is None else float(o["margin_ks"])))
            nsep = sum(1 for q in per if q["sep"] and (q["sep"]["wall"] or q["sep"]["shroud"]))
            nfold = sum(1 for q in per if q["ks"] is not None and q["ks"] < floor0)
            nunc = sum(1 for q in per if q["cert"] > 1.0)
            nbox = sum(1 for q in per if q["T_min"] <= C["T_tab"][0])
            say("   %-22s %-3s C_F %.6f (gain over no nozzle %+.5f); F %.2f N, Isp %.2f s; phases: %d of %d out of the fold class"
                " (KS < %.4f), %d detached, %d uncertified (worst cert %.3g), %d out of the table box (T_min %.0f K); lip p/p_a"
                " %.2f .. %.2f" % (ev, name, J, J - J0, F, F / (mdot * E["g0"]), nfold, len(per), floor0, nsep, nunc,
                                   float(o["cert_worst"]), nbox, min(q["T_min"] for q in per), min(q["p_lip"] for q in per),
                                   max(q["p_lip"] for q in per)))
    fn = os.path.join(ART, "eval_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(dict(pa_bar=C["pa_bar"], closure=base["TWOP_SEP"], mdot=mdot, provenance=prov, res=res), open(fn + ".tmp", "w"),
              indent=1, default=float)
    os.replace(fn + ".tmp", fn)
    say("   record: %s" % fn)
    return 0


def swirlgates():
    """The free-vortex swirl in the two-wall march: SW-1 the exact
    radial-equilibrium duct preserved (u uniform, v = 0, the wall pressures
    of radial equilibrium) through the five swirl processes; SW-2 Gamma -> 0
    reproduces the certified march; SW-3 the swirl is alive on the tournament
    posing (the per-phase C_F with and without it differ beyond the Newton
    band)."""
    say("== [F3/A1] the RDE tournament: free-vortex swirl in the two-wall march [X-RDET] (stage swirlgates) ==")
    import jax.numpy as jnp
    import a1_ideal_march_jax as A1
    import a1_plug_march as PM
    import a1_swirl_march as SW
    C = CASES["swirl_gates"]
    t0 = time.time()
    tg = A1.prep_tab(A1.build_tab_gconst())
    ta = A1.tab_arrays(tg)
    from a1_shroud_twin import q_of_mach
    u = q_of_mach(C["M"], ta, tg["_as"])
    G2 = (C["y_plug"] * C["w_over_u"] * u) ** 2

    def duct(K, N, G2_):
        sx = np.linspace(0, C["x_end"], K)[1:]
        st = (jnp.asarray(sx), jnp.full(len(sx), C["y_plug"]), jnp.zeros(len(sx)))
        sxs = np.linspace(0, C["x_shroud_end"], K)
        shr = (sxs, np.full(K, C["y_shroud"]), np.zeros(K))
        yl = np.linspace(C["y_plug"], C["y_shroud"], N)
        start = (0.0, yl, np.full(N, u), np.zeros(N))
        cells = SW.swirl_cells_2w(1.0, G2_)
        out, _ = PM.plug_march(st, start, u, tg, 1.0, shroud=shr, cells=cells)
        return out
    res = []
    for K, N in C["rungs"]:
        o = duct(K, N, G2)
        w = np.array(o["wall"]); sh = np.array(o["shroud"])
        pw = np.asarray(SW.state_sw(jnp.asarray(np.hypot(w[:, 2], w[:, 3])), jnp.asarray(w[:, 1]), G2, ta)[1])
        ps = np.asarray(SW.state_sw(jnp.asarray(np.hypot(sh[:, 2], sh[:, 3])), jnp.asarray(sh[:, 1]), G2, ta)[1])
        pw_ex = float(SW.state_sw(jnp.float64(u), jnp.float64(C["y_plug"]), G2, ta)[1])
        ps_ex = float(SW.state_sw(jnp.float64(u), jnp.float64(C["y_shroud"]), G2, ta)[1])
        mesh = np.array(o["mesh_pts"])
        res.append(dict(du=float(np.max(np.abs(mesh[:, 2] / u - 1))), v=float(np.max(np.abs(mesh[:, 3])) / u),
                        dpw=float(np.max(np.abs(pw / pw_ex - 1))), dps=float(np.max(np.abs(ps / ps_ex - 1))),
                        cert=float(o["cert_worst"]), pw_ex=pw_ex, ps_ex=ps_ex))
    c_, f_ = res
    band = lambda key: A1.K_RICH * abs(c_[key] - f_[key]) + A1.C_FLOOR * A1.EPS * A1.K_RICH   # noqa: E731
    check("SW-1 the two-wall radial-equilibrium duct preserved (fine rung): max |u/u0 - 1| %.1e, max |v|/u0 %.1e, plug p %.1e,"
          " shroud p %.1e off the exact radial equilibrium (p_shroud / p_plug = %.4f); certified %.3f / %.3f"
          % (f_["du"], f_["v"], f_["dpw"], f_["dps"], f_["ps_ex"] / f_["pw_ex"], c_["cert"], f_["cert"]),
          max(f_["du"], f_["v"], f_["dpw"], f_["dps"]) <= max(band("du"), band("v"), band("dpw"), band("dps"), A1.K_RICH * A1.EPS ** 0.5)
          and max(c_["cert"], f_["cert"]) <= 1.0)
    o0 = duct(*C["rungs"][0], 0.0)
    sx = np.linspace(0, C["x_end"], C["rungs"][0][0])[1:]
    st = (jnp.asarray(sx), jnp.full(len(sx), C["y_plug"]), jnp.zeros(len(sx)))
    sxs = np.linspace(0, C["x_shroud_end"], C["rungs"][0][0])
    oc, _ = PM.plug_march(st, (0.0, np.linspace(C["y_plug"], C["y_shroud"], C["rungs"][0][1]), np.full(C["rungs"][0][1], u),
                                np.zeros(C["rungs"][0][1])), u, tg, 1.0,
                          shroud=(sxs, np.full(len(sxs), C["y_shroud"]), np.zeros(len(sxs))))
    d0 = float(np.max(np.abs(np.array(o0["mesh_pts"]) - np.array(oc["mesh_pts"]))))
    check("SW-2 Gamma = 0: the five swirl processes reproduce the certified two-wall march (max |d| over the net %.1e)" % d0,
          d0 <= A1.K_RICH * A1.NEWTON_TOL_FACTOR * A1.EPS * max(1.0, u))
    # SW-3 alive on the tournament posing (the S0 design, K 12)
    gas = os.path.join(ART, "gas_stechmann.json")
    GS = json.load(open(gas))
    env = dict(TWOP_KERNEL="arc", TWOP_CAP=CASES["gates"]["cap"], TWOP_U0=CASES["gates"]["u0"], TWOP_FREE_EXIT="lip",
               TWOP_GAS=gas, TWOP_PA=CASES["source"]["pa_bar"] * BAR / GS["P0"], TWOP_SHAPE="1", TWOP_NOPLUME="1",
               TWOP_SEP="summerfield", TWOP_MU=os.path.join(ART, "family_K12.json"))
    T, twn = _tw(env)
    W = T.trunc_start(twn)
    on, _ = twn.march_record(W)
    T, tws = _tw(dict(env, TWOP_SWIRL="1"))
    osw, _ = tws.march_record(W)
    dJ = np.array(osw["J_phase"]) - np.array(on["J_phase"])
    vk = np.array([ph_["v"] for ph_ in json.load(open(os.path.join(ART, "family_K12.json")))["phases"]])
    check("SW-3 swirl alive on the tournament posing (S0, K 12): J_mu %.6f with swirl vs %.6f without (%+.2e); per phase dC_F %s"
          " for v %s m/s; certificates %.3f / %.3f" % (osw["J_mu"], on["J_mu"], osw["J_mu"] - on["J_mu"],
                                                      np.array2string(dJ, precision=4), np.array2string(vk, precision=0),
                                                      osw["cert_worst"], on["cert_worst"]),
          abs(osw["J_mu"] - on["J_mu"]) > A1.K_RICH * A1.EPS * len(W) and osw["cert_worst"] <= 1.0)
    # SW-4 the swirl replay (sequential: the swirl cells have no wavefront
    # kinds) = the record, and its adjoint = a central difference
    import jax
    osr, Ssw = tws.march_record(W)
    Jr = float(tws.J_replay(jnp.asarray(W), Ssw))
    g = np.asarray(jax.grad(lambda z: tws.J_replay(z, Ssw))(jnp.asarray(W)))
    k_, h_ = CASES["jet_gates"]["knot"], CASES["jet_gates"]["fd_step"]
    e_ = np.zeros(len(W)); e_[k_] = h_
    fd = (float(tws.J_replay(jnp.asarray(W + e_), Ssw)) - float(tws.J_replay(jnp.asarray(W - e_), Ssw))) / (2 * h_)
    check("SW-4 the swirl replay = the record (%.12f vs %.12f); adjoint %+.6e vs central FD %+.6e along knot %d (rel %.1e)"
          % (Jr, float(osr["J_mu"]), g[k_], fd, k_, abs(g[k_] - fd) / max(abs(fd), A1.EPS)),
          abs(Jr - float(osr["J_mu"])) <= A1.K_RICH * A1.EPS * len(osr["outs"][0]["wall"]) * len(tws.phases)
          and abs(g[k_] - fd) <= max(A1.K_RICH * abs(fd) * h_ ** 0.5, A1.EPS ** 0.5))
    say("   %d/%d PASS in %.0f s" % (NPASS[0], NPASS[1], time.time() - t0))
    return 0 if NPASS[0] == NPASS[1] else 1


def jetgates():
    """The free jet after the lip in the two-wall carrier (TWOP_JET)."""
    say("== [F3/A1] the RDE tournament: the free jet in the two-wall carrier [X-RDET] (stage jetgates) ==")
    import jax
    import jax.numpy as jnp
    C, G = CASES["source"], CASES["jet_gates"]
    t0 = time.time()
    gas = os.path.join(ART, "gas_stechmann.json")
    GS = json.load(open(gas))
    Cr = json.load(open(os.path.join(ART, "stech", "class_2026-09-27.json")))
    env = dict(TWOP_KERNEL="arc", TWOP_CAP=CASES["gates"]["cap"], TWOP_U0=CASES["gates"]["u0"], TWOP_FREE_EXIT="lip",
               TWOP_GAS=gas, TWOP_PA=C["pa_bar"] * BAR / GS["P0"], TWOP_SHAPE="1", TWOP_NOPLUME="1")
    # JT-1 both ends at the cap: the jet never reaches a wall
    T, twn = _tw(env)
    W = T.trunc_start(twn)
    on, _ = twn.march_record(W, margin=twn.margin_dict(mu0=Cr["floors"][0], rho=Cr["rho"], m_ref=Cr["m_ref"]))
    T, twj = _tw(dict(env, TWOP_JET="1"))
    oj, _ = twj.march_record(W, margin=twj.margin_dict(mu0=Cr["floors"][0], rho=Cr["rho"], m_ref=Cr["m_ref"]))
    same_w = np.array_equal(np.asarray(on["wall"]), np.asarray(oj["wall"])) and np.array_equal(np.asarray(on["shroud"]), np.asarray(oj["shroud"]))
    check("JT-1 both ends at the cap: the jet leaves every wall point bitwise (%s), J %.12f = %.12f; the lip margin %+.4f (under-expanded)"
          " joins the class (KS %.4f -> %.4f); certificates %.3f / %.3f"
          % (same_w, float(twj.J_of(oj)), float(twn.J_of(on)), float(oj["m_lip"]), float(on["margin_ks"]), float(oj["margin_ks"]),
             on["cert_worst"], oj["cert_worst"]),
          same_w and float(twj.J_of(oj)) == float(twn.J_of(on)) and float(oj["m_lip"]) > 0 and oj["cert_worst"] <= 1.0)
    # JT-2 the plug beyond the lip (the shroud ends at mid-way, the plug at
    # the cap). MEASURED 2026-09-27 (RDE/handoff/f3_2026-09-25/
    # twop_jet_closure_probe.py): the lip's first characteristic lands past
    # the plug tip -- the whole plug lies in the internal flow's domain of
    # dependence, so the jet must leave every plug point and J bitwise; the
    # jet region's momentum and mass residuals are the net's discretisation
    # error, second order: the ratio between the rungs is nearer 4 than 2 or
    # 8 (the band [2 sqrt 2, 4 sqrt 2], the geometric midpoints)
    envx = dict(env, TWOP_U0_S=G["u0_shroud"])
    import a1_plug_march as PM
    rows = []
    for K_, N_ in (G["fine_rung"], (None, None)):         # the coarse rung last: JT-3 replays it
        envk = dict(envx) if K_ is None else dict(envx, TWOP_K=K_, TWOP_N=N_)
        T, twx0 = _tw(envk)
        Wx = T.trunc_start(twx0)
        ox0, _ = twx0.march_record(Wx)
        T, twx = _tw(dict(envk, TWOP_JET="1"))
        ox, Sx = twx.march_record(Wx)
        ctx = twx._ctx()
        pa_abs = twx.pa * twx.P0
        col_in = np.stack([np.full(twx.N, twx.x0), np.linspace(twx.y_l, twx.y_u, twx.N), np.full(twx.N, ctx["q_i"]),
                           np.zeros(twx.N)], 1)
        mi, Fin = PM.col_fluxes(col_in, ctx["ta"], pa_abs, 1.0)
        mo, Fout = PM.col_fluxes(np.array(ox["last_col"]), ctx["ta"], pa_abs, 1.0)
        pw = PM.wall_push_poly(np.vstack([col_in[:1], np.array(ox["wall"])]), ctx["ta"], pa_abs, 1.0)
        ps = PM.wall_push_poly(np.vstack([col_in[-1:], np.array(ox["shroud"])]), ctx["ta"], pa_abs, 1.0)
        xt, xl = (float(v) for v in twx.ends_of(Wx))
        top0 = np.asarray(ox0["last_col"])[-1]
        rows.append(dict(K=twx.K, N=twx.N, xt=xt, xl=xl, top0=top0, same=np.array_equal(np.asarray(ox["wall"]), np.asarray(ox0["wall"])),
                         J=float(twx.J_of(ox)), J0=float(twx0.J_of(ox0)), cert=float(ox["cert_worst"]), cert0=float(ox0["cert_worst"]),
                         nedge=len(ox["edge"]), rm=(Fout - Fin + pw - ps) / Fin, rq=(mo - mi) / mi))
    fi, co = rows
    check("JT-2a the plug beyond the lip (tip x %.3f, lip x %.3f): the lip's first characteristic lands past the tip (the no-jet top"
          " row ends at x %.4f, y %.4f): the jet leaves every plug point bitwise (%s) and J %.12f = %.12f; certified %.3f (jet, %d"
          " edge points) / %.3f" % (co["xt"], co["xl"], co["top0"][0], co["top0"][1], co["same"], co["J"], co["J0"], co["cert"],
                                    co["nedge"], co["cert0"]),
          co["same"] and co["J"] == co["J0"] and co["top0"][0] > co["xt"] and co["cert"] <= 1.0 and co["cert0"] <= 1.0)
    lo_, hi_ = 2.0 * np.sqrt(2.0), 4.0 * np.sqrt(2.0)
    check("JT-2b the jet region's residuals in the p_a gauge (the free edge contributing zero) are second-order discretisation:"
          " momentum %.2e -> %.2e of F_in (ratio %.2f), mass %.2e -> %.2e (ratio %.2f) from (%d,%d) to (%d,%d), in [%.2f, %.2f];"
          " the fine rung bitwise too (%s), certified %.3f" % (co["rm"], fi["rm"], co["rm"] / fi["rm"], co["rq"], fi["rq"], co["rq"] / fi["rq"],
                                                             co["K"], co["N"], fi["K"], fi["N"], lo_, hi_, fi["same"], fi["cert"]),
          lo_ <= co["rm"] / fi["rm"] <= hi_ and lo_ <= co["rq"] / fi["rq"] <= hi_ and fi["same"] and fi["cert"] <= 1.0)
    # JT-3 the replay and its gradient
    Jr = float(twx.J_replay(jnp.asarray(Wx), Sx))
    g = np.asarray(jax.grad(lambda z: twx.J_replay(z, Sx))(jnp.asarray(Wx)))
    k_, h_ = G["knot"], G["fd_step"]
    e_ = np.zeros(len(Wx)); e_[k_] = h_
    fd = (float(twx.J_replay(jnp.asarray(Wx + e_), Sx)) - float(twx.J_replay(jnp.asarray(Wx - e_), Sx))) / (2 * h_)
    check("JT-3 the jet replay = the record (%.12f vs %.12f); adjoint %+.6e vs central FD %+.6e along knot %d (rel %.1e)"
          % (Jr, float(twx.J_of(ox)), g[k_], fd, k_, abs(g[k_] - fd) / max(abs(fd), T.A1.EPS)),
          abs(Jr - float(twx.J_of(ox))) <= T.K_RICH * T.A1.EPS * len(ox["wall"]) and abs(g[k_] - fd) <= max(T.K_RICH * abs(fd) * h_ ** 0.5, T.A1.EPS ** 0.5))
    # JT-4 the over-expanded lip: out of class by the lip margin, the march kept
    T, two = _tw(dict(env, TWOP_JET="1", TWOP_PA=G["over_pa_bar"] * BAR / GS["P0"]))
    oo, _ = two.march_record(W, margin=two.margin_dict(mu0=Cr["floors"][0], rho=Cr["rho"], m_ref=Cr["m_ref"]))
    check("JT-4 the lip over-expanded at %.2f bar: the lip margin %+.4f puts the class below its floor (KS %.4f < %.4f), the march"
          " computed (certified %.3f, J finite %.6f)" % (G["over_pa_bar"], float(oo["m_lip"]), float(oo["margin_ks"]), Cr["floors"][0],
                                                        oo["cert_worst"], float(two.J_of(oo))),
          float(oo["m_lip"]) < 0 and float(oo["margin_ks"]) < Cr["floors"][0] and np.isfinite(float(two.J_of(oo))))
    say("   %d/%d PASS in %.0f s" % (NPASS[0], NPASS[1], time.time() - t0))
    return 0 if NPASS[0] == NPASS[1] else 1


def offdesign():
    """The designs off their ambient: the march does not depend on p_a (no
    jet), so ONE record per design and judge gives C_F(p_a) for every closure
    (none = attached walls, Summerfield, Schmucker): per design, per judge,
    per p_a the C_F in units of the Stechmann P0 A*, the thrust, the phases
    with a detached wall and where. The phase families show which phases
    separate first -- the time-mean state separates at ONE ambient, the
    phases at a spread of them."""
    say("== [F3/A1] the RDE tournament: the designs off their ambient [X-RDET] (stage offdesign) ==")
    C, E, O = CASES["source"], CASES["eval"], CASES["offdesign"]
    t0 = time.time()
    gas = os.path.join(ART, "gas_stechmann.json")
    GS = json.load(open(gas))
    base = dict(TWOP_KERNEL="arc", TWOP_CAP=CASES["gates"]["cap"], TWOP_U0=CASES["gates"]["u0"], TWOP_FREE_EXIT="lip",
                TWOP_GAS=gas, TWOP_PA=C["pa_bar"] * BAR / GS["P0"], TWOP_SHAPE="1", TWOP_NOPLUME="1", TWOP_SEP="summerfield")
    LD = load_designs()
    designs = {k: v[0] for k, v in LD.items()}
    prov = {k: v[1] for k, v in LD.items()}
    say("   designs %s; judges %s; p_a %s bar; closures none / summerfield / schmucker"
        % ("; ".join("%s (%s)" % (k, prov[k]) for k in sorted(designs)), O["judges"], O["pa_bar"]))
    res = {}
    for ev in O["judges"]:
        fam, _, opt = ev.partition("+")
        env = dict(base) if fam == "mean" else dict(base, TWOP_MU=os.path.join(ART, fam))
        if opt == "swirl":
            env["TWOP_SWIRL"] = "1"
        T, tw = _tw(env)
        A_phys = tw.A_star * C["r_out_m"] ** 2
        ctxs = tw.phases if tw.phases is not None else [tw._ctx()]
        A_in = np.pi * (tw.y_u ** 2 - tw.y_l ** 2)
        res[ev] = {}
        recs = {name: tw.march_record(W)[0] for name, W in designs.items()}
        for sep in ("", "summerfield", "schmucker"):
            tw.sep = sep
            for pab in O["pa_bar"]:
                tw.pa = pab * BAR / tw.P0
                pa_abs = tw.pa * tw.P0
                J0 = sum(c_["w"] * (c_["F_in"] - pa_abs * A_in) for c_ in ctxs) / (tw.P0 * tw.A_star)
                row = dict(J0=float(J0))
                for name, o in recs.items():
                    outs = o.get("outs", [o])
                    Jk = [float(tw._J_gen(o_k, c_)) for o_k, c_ in zip(outs, ctxs)]
                    J = sum(c_["w"] * j_ for c_, j_ in zip(ctxs, Jk))
                    det = []
                    if sep:
                        for k, (o_k, c_) in enumerate(zip(outs, ctxs)):
                            rd = tw.sep_readout(o_k, c_)
                            if rd["wall"] is not None or rd["shroud"] is not None:
                                det.append((k, rd))
                    row[name] = dict(J=J, F_N=J * tw.P0 * A_phys, per=Jk, detached=det)
                res[ev]["%s@%g" % (sep or "none", pab)] = row
        for name in recs:
            say("   %-24s %-3s C_F vs p_a %s bar:" % (ev, name, O["pa_bar"]))
            for sep in ("", "summerfield", "schmucker"):
                vals = [res[ev]["%s@%g" % (sep or "none", pab)][name] for pab in O["pa_bar"]]
                say("      %-11s %s | detached phases %s" % (sep or "attached", " ".join("%.5f" % v["J"] for v in vals),
                                                           " ".join("%d" % len(v["detached"]) for v in vals)))
        say("   %-24s no nozzle:  %s" % (ev, " ".join("%.5f" % res[ev]["none@%g" % pab]["J0"] for pab in O["pa_bar"])))
    fn = os.path.join(ART, "offdesign_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(dict(pa_bar=O["pa_bar"], judges=O["judges"], designs=sorted(designs), provenance=prov, res=res), open(fn + ".tmp", "w"),
              indent=1, default=float)
    os.replace(fn + ".tmp", fn)
    say("   record: %s (%.0f s)" % (fn, time.time() - t0))
    return 0


def sepgates():
    """The separation criterion as a CLASS constraint (TWOP_SEP_CLASS, D-GSEP):
    every wall point's margin p_w / p_sep - 1 joins the fold class's KS
    soft-min as the entry mu0 + margin, so a certified in-class design keeps
    both walls attached. SC-1 inert where nothing nears separation (the KS
    moves within its own union bound, J untouched); SC-2 active where the
    closure detaches a wall (the class leaves its floor, and the first wall
    point with a negative margin is the closure's detachment point within
    one station); SC-3 the replayed margin = the record's, adjoint = FD."""
    say("== [F3/A1] the RDE tournament: separation as a class constraint [X-RDET] (stage sepgates) ==")
    import jax
    import jax.numpy as jnp
    C, G = CASES["source"], CASES["gates"]
    t0 = time.time()
    gas = os.path.join(ART, "gas_stechmann.json")
    GS = json.load(open(gas))
    Cr = json.load(open(os.path.join(ART, "stech", "class_2026-09-27.json")))
    env = dict(TWOP_KERNEL="arc", TWOP_CAP=G["cap"], TWOP_U0=G["u0"], TWOP_FREE_EXIT="lip", TWOP_GAS=gas,
               TWOP_PA=C["pa_bar"] * BAR / GS["P0"], TWOP_SHAPE="1", TWOP_NOPLUME="1", TWOP_SEP="summerfield")
    T, tw = _tw(env)
    W = T.trunc_start(tw)
    mg = lambda t_: t_.margin_dict(mu0=Cr["floors"][0], rho=Cr["rho"], m_ref=Cr["m_ref"])     # noqa: E731
    o, _ = tw.march_record(W, margin=mg(tw))
    T, twc = _tw(dict(env, TWOP_SEP_CLASS="1"))
    oc, Sc = twc.march_record(W, margin=mg(twc))
    ks, ksc, msep = float(o["margin_ks"]), float(oc["margin_ks"]), float(oc["m_sep"])
    n_e = len(oc["wall"]) + len(oc["shroud"])
    e_min = Cr["floors"][0] + msep
    bound = np.log1p(n_e * np.exp(-Cr["rho"] * (e_min - ks))) / Cr["rho"]
    check("SC-1 inert at the tournament ambient (%.2f bar): the smallest wall margin p_w/p_sep - 1 = %+.4f; the class KS %.6f ->"
          " %.6f (drop %.2e <= the union bound %.2e over %d entries); J %.12f = %.12f"
          % (C["pa_bar"], msep, ks, ksc, ks - ksc, bound, n_e, float(twc.J_of(oc)), float(tw.J_of(o))),
          msep > 0 and 0.0 <= ks - ksc <= bound + T.K_RICH * T.A1.EPS * max(1.0, abs(ks))
          and float(twc.J_of(oc)) == float(tw.J_of(o)))
    # SC-2 where the closure detaches a wall
    pa_hi = CASES["gates"]["over_pa_bar"] * BAR / GS["P0"]
    T, twh = _tw(dict(env, TWOP_PA=pa_hi, TWOP_SEP_CLASS="1"))
    oh, _ = twh.march_record(W, margin=mg(twh))
    rd = twh.sep_readout(oh)
    ctx = twh._ctx()
    pa_abs = twh.pa * twh.P0
    agree = []
    for key in ("wall", "shroud"):
        pts = np.asarray(oh[key])
        st = T.A1.state_q(jnp.asarray(np.hypot(pts[:, 2], pts[:, 3])), ctx["ta"])
        m_ = np.asarray(st[1]) / np.asarray(twh._p_sep(st[5], pa_abs)) - 1.0
        neg = np.where(m_ < 0.0)[0]
        x_neg = float(pts[neg[0], 0]) if len(neg) else None
        x_cl = None if rd[key] is None else rd[key][0]
        if x_neg is None or x_cl is None:
            agree.append((key, x_neg, x_cl, x_neg is None and x_cl is None))
        else:
            k_cl = int(np.argmin(np.abs(pts[:, 0] - x_cl)))
            agree.append((key, x_neg, x_cl, abs(k_cl - int(neg[0])) <= 1))
    check("SC-2 at %.2f bar the class sees the separation: smallest wall margin %+.4f, KS %.4f < the floor %.4f; the first"
          " negative-margin point vs the closure's detachment (x): %s"
          % (CASES["gates"]["over_pa_bar"], float(oh["m_sep"]), float(oh["margin_ks"]), Cr["floors"][0],
             ", ".join("%s %s / %s (%s)" % (k_, "--" if a_ is None else "%.4f" % a_, "--" if b_ is None else "%.4f" % b_,
                                            "one station" if ok_ else "APART") for k_, a_, b_, ok_ in agree)),
          float(oh["m_sep"]) < 0 and float(oh["margin_ks"]) < Cr["floors"][0] and all(a[3] for a in agree)
          and any(a[1] is not None for a in agree))
    # SC-3 the replayed margin and its adjoint
    mgc = mg(twc)
    mr = float(twc.margin_replay(jnp.asarray(W), Sc, mgc))
    gm = np.asarray(jax.grad(lambda z: twc.margin_replay(z, Sc, mgc))(jnp.asarray(W)))
    k_, h_ = G["knot"], G["fd_step"]
    e_ = np.zeros(len(W)); e_[k_] = h_
    fd = (float(twc.margin_replay(jnp.asarray(W + e_), Sc, mgc)) - float(twc.margin_replay(jnp.asarray(W - e_), Sc, mgc))) / (2 * h_)
    n_ks = int(oc["margin_n"]) + n_e                   # the KS soft-min's entries: the class cells and the wall points
    check("SC-3 the replayed class margin with the separation entries = the record's (%.12f vs %.12f, |d| %.1e <= %.1e over %d"
          " entries); adjoint %+.6e vs central FD %+.6e along knot %d (rel %.1e)"
          % (mr + mgc["mu0"], ksc, abs(mr + mgc["mu0"] - ksc), T.K_RICH * T.A1.EPS * n_ks * max(1.0, abs(ksc)), n_ks, gm[k_], fd, k_,
             abs(gm[k_] - fd) / max(abs(fd), T.A1.EPS)),
          abs(mr + mgc["mu0"] - ksc) <= T.K_RICH * T.A1.EPS * n_ks * max(1.0, abs(ksc))
          and abs(gm[k_] - fd) <= max(T.K_RICH * abs(fd) * h_ ** 0.5, T.A1.EPS ** 0.5))
    say("   %d/%d PASS in %.0f s" % (NPASS[0], NPASS[1], time.time() - t0))
    return 0 if NPASS[0] == NPASS[1] else 1


def CASES_TW_RHO():
    """The class rho of the tournament's class record (the class stage's)."""
    fn = os.path.join(ART, "stech", "class_2026-09-27.json")
    return json.load(open(fn))["rho"] if os.path.exists(fn) else 1.0


if __name__ == "__main__":
    st = os.environ.get("STAGE", "family")
    sys.exit(dict(family=family, gates=gates, eval=evaluate, swirlgates=swirlgates, jetgates=jetgates, sepgates=sepgates, offdesign=offdesign)[st]())

#!/usr/bin/env python3
"""T09 -- literature: Rao 1961 (spike contour for optimum thrust) and Humphreys, Thompson & Hoffman 1971 (the Rao
nozzle of their comparison), each reproduced twice: by our own solver of Rao's equations (ref/rao1961.py, written
from the papers) and by GENO's RaoPlug (decks: tests/t09_setup_geno.py, run on s3).

Tolerances = the printed precision of the papers (half a unit of the last printed digit), except where a derived
error model is stated next to the check.
"""
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "ref"))
import numpy as np                                 # noqa: E402
import matplotlib                                  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                    # noqa: E402
import rv                                          # noqa: E402
import exact                                       # noqa: E402
import rao1961 as R61                              # noqa: E402
import rao_posing as RP                            # noqa: E402

rep = rv.Report("t09_literature")
r = R61.Rao1961(1.23)
GD = lambda c: os.path.join(rv.RV, "geno", c)      # noqa: E731


def geno_case(c):
    """GENO run -> its ED (raoplug_cminus.dat), plug, cowl, performance, and Rao's numbers recomputed from its ED."""
    g = RP.GenoRao(GD(c))
    cj = json.load(open(os.path.join(GD(c), "case.json")))
    G = exact.PerfectGas(*cj["gas"])
    ed = np.loadtxt(os.path.join(GD(c), "raoplug_cminus.dat"), comments="#")
    x, y, th, q = ed.T
    M = G.M_q(q)
    p, rho, a = G.p_q(q), G.rho_q(q), np.arcsin(1.0 / M)
    mid = lambda f: 0.5 * (f[1:] + f[:-1])          # noqa: E731
    dR = -np.diff(y)
    mdot = np.sum(mid(rho * q * np.sin(a) / np.sin(a - th) * 2 * np.pi * y) * dR)
    Fv = np.sum(mid((p + rho * q ** 2 * np.sin(a) * np.cos(th) / np.sin(a - th)) * 2 * np.pi * y) * dR)
    rsws = float(G.rho(1.0) * G.q(1.0))
    A_s = mdot / rsws
    P0 = cj["gas"][3]
    return dict(g=g, L=float(x[-1]), R_D=float(y[-1]), M_D=float(M[-1]), th_D=float(np.degrees(th[-1])),
                p_a=g.pa / P0, p_b=g.pb / P0, eps=float(np.pi / A_s), C_F=float((Fv + g.pb * np.pi * y[-1] ** 2) / (P0 * A_s)),
                F_vac=float(Fv), P0=P0, ed=ed, mdot_perf=g.perf.get("mdot [kg/s]"))


def normal_dist(pts, wall):
    """Signed distance of each point to the polyline (positive above the wall), exact segment projection."""
    a, b = wall[:-1], wall[1:]
    d = b - a
    L2 = np.sum(d * d, 1)
    out = []
    for P in pts:
        t = np.clip(np.sum((P - a) * d, 1) / L2, 0.0, 1.0)
        q = a + t[:, None] * d
        v = P - q
        k = int(np.argmin(np.hypot(v[:, 0], v[:, 1])))
        out.append(np.hypot(*v[k]) * np.sign(d[k, 0] * v[k, 1] - d[k, 1] * v[k, 0]))
    return np.array(out)


res = {}
# ------------------------------------------------------------------ Rao 1961: the paper vs its own equations
for key, cut_case, exact_case in (("e381", "rao61_e381_pbR", "rao61_e381_pb0"), ("e1069", "rao61_e1069_pbR", "rao61_e1069_pb0")):
    P = R61.PUB[key]
    m = r.member(P["M_E"], P["th_E"], n=200001)
    M, th, Rr, x = m["M"], m["theta"], m["R"], m["x"]
    a = np.arcsin(1 / M)
    w = r.G.q(M)
    am, thm, Rm, wm = (0.5 * (f[1:] + f[:-1]) for f in (a, th, Rr, w))
    comp = np.diff(th) + np.diff(w) / wm / np.tan(am) - np.sin(am) * np.sin(thm) / np.sin(thm - am) / Rm * np.diff(Rr)
    rep.check("Rao %s: our ED satisfies the C- compatibility (10), max residual per step" % key,
              float(np.max(np.abs(comp))), 1e-12)
    # the ED cut at Rao's printed R_D
    k = int(np.argmin(np.abs(Rr - P["R_D"])))
    sl = slice(0, k + 1)
    pp, rho = r.G.p(M), r.G.rho(M)
    mid = lambda f: 0.5 * (f[1:] + f[:-1])          # noqa: E731
    dR = -np.diff(Rr[sl])
    dm = mid((rho * w * np.sin(a) / np.sin(a - th) * 2 * np.pi * Rr)[sl]) * dR
    dF = mid(((pp + rho * w ** 2 * np.sin(a) * np.cos(th) / np.sin(a - th)) * 2 * np.pi * Rr)[sl]) * dR
    A_s = dm.sum() / r.rs_ws
    cut = dict(L=float(x[k]), R_D=float(Rr[k]), eps=float(np.pi / A_s), C_F=float(dF.sum() / A_s),
               th_D=float(np.degrees(th[k])), M_D=float(M[k]))
    pb_cut = float(pp[k] - 0.5 * rho[k] * w[k] ** 2 * np.tan(a[k]) * np.sin(-2 * th[k]))
    ex = dict(L=float(m["x_D"]), R_D=float(m["R_D"]), eps=float(m["eps"]), C_F=float(m["C_F"]),
              th_D=float(np.degrees(m["theta_D"])), M_D=float(m["M_D"]), p_a=float(m["p_a"]))
    # error model: half a unit of each printed digit (L 3 decimals, eps 2, C_F 4, theta_D 2) plus the spread of the
    # quantity when the cut moves by the printed R_D's own rounding (+-0.0005)
    half = dict(L=5e-4, eps=5e-3, C_F=5e-5, th_D=5e-3)

    def cut_at(Rc):
        kk = int(np.argmin(np.abs(Rr - Rc)))
        ss = slice(0, kk + 1)
        dR_ = -np.diff(Rr[ss])
        dm_ = mid((rho * w * np.sin(a) / np.sin(a - th) * 2 * np.pi * Rr)[ss]) * dR_
        dF_ = mid(((pp + rho * w ** 2 * np.sin(a) * np.cos(th) / np.sin(a - th)) * 2 * np.pi * Rr)[ss]) * dR_
        As_ = dm_.sum() / r.rs_ws
        return dict(L=float(x[kk]), eps=float(np.pi / As_), C_F=float(dF_.sum() / As_), th_D=float(np.degrees(th[kk])))
    lo, hi = cut_at(P["R_D"] - 5e-4), cut_at(P["R_D"] + 5e-4)
    tol_q = {q: half[q] + 0.5 * abs(hi[q] - lo[q]) for q in half}
    ratios = {q: abs(cut[q] - P[q]) / tol_q[q] for q in half}
    rep.check("Rao %s: ED cut at the printed R_D reproduces L, eps, C_F, theta_D (max |diff| / tolerance; worst: %s)"
              % (key, max(ratios, key=ratios.get)), max(ratios.values()), 1.0)
    rep.note("Rao %s: tolerances %s ; ratios %s" % (key, {q: float("%.2g" % v) for q, v in tol_q.items()},
                                                    {q: float("%.2f" % v) for q, v in ratios.items()}))
    gx, gc = geno_case(exact_case), geno_case(cut_case)
    for nm, gg, ref_ in (("p_b = 0", gx, ex), ("cut at Rao's D", gc, cut)):
        dev = max(abs(gg["L"] / ref_["L"] - 1), abs(gg["M_D"] / ref_["M_D"] - 1), abs(gg["eps"] / ref_["eps"] - 1),
                  abs(gg["C_F"] / ref_["C_F"] - 1))
        rep.check("Rao %s, %s: GENO's L, M_D, eps, C_F vs our solver (max relative difference)" % (key, nm), dev, 2e-4)
    tab = R61.TAB1 if key == "e381" else R61.TAB2
    pts = tab[1:, :2]
    dist = normal_dist(pts, gc["g"].plug[:, :2])
    inside = pts[:, 0] >= gc["g"].x_s
    rep.check("Rao %s: printed contour vs GENO, %d points downstream of x_s, max |normal distance| / R_E" % (
        key, int(inside.sum())), float(np.max(np.abs(dist[inside]))), 1e-3)
    res[key] = dict(printed=P, exact=ex, cut=cut, pb_cut=pb_cut, geno_exact={q: gx[q] for q in ("L", "R_D", "M_D", "th_D", "p_a", "eps", "C_F")},
                    geno_cut={q: gc[q] for q in ("L", "R_D", "M_D", "th_D", "p_a", "eps", "C_F")},
                    dist=dist.tolist(), inside=inside.tolist(), m=m, gc=gc, gx=gx)
    rep.note("Rao %s: printed L %.3f eps %.2f C_F %.4f theta_D %.2f | exact (p_b=0) L %.4f eps %.4f C_F %.5f theta_D %.3f"
             " | cut at R_D %.3f: L %.4f eps %.4f C_F %.5f theta_D %.3f (p_b = %.5f P_c)" % (
                 key, P["L"], P["eps"], P["C_F"], P["th_D"], ex["L"], ex["eps"], ex["C_F"], ex["th_D"], P["R_D"],
                 cut["L"], cut["eps"], cut["C_F"], cut["th_D"], pb_cut))
P = R61.PUB["e381"]
rep.check("Rao e381: p_a / P_c from (8) vs printed 0.0355", res["e381"]["exact"]["p_a"] - P["p_a"], 5e-5)
for key in ("e381", "e1069"):
    P = R61.PUB[key]
    idl = r.ideal(P["eps"])
    rep.check("Rao %s ideal spike: C_F (one-dimensional, exact) vs printed %.4f" % (key, P["ideal_C_F"]),
              idl["C_F"] - P["ideal_C_F"], 5e-5)
    res[key]["ideal"] = idl
    rep.note("Rao %s ideal spike: L = sqrt(M_a^2 - 1) = %.4f (Table 3 %.3f%s), C_F %.5f" % (
        key, idl["L"], P["ideal_L"], ", text %.3f" % P["ideal_L_text"] if "ideal_L_text" in P else "", idl["C_F"]))
rep.check("Rao e381 ideal spike: length sqrt(M_a^2-1) vs the text's 2.428", res["e381"]["ideal"]["L"] - 2.428, 5e-4)


# REJECTOR (R5): the member check (ED cut at the printed R_D vs the printed L, eps, C_F, theta_D) for the e1069 member,
# with our solver run at gamma 1.24 instead of Rao's 1.23
def cut_ratio(rr, key):
    P_ = R61.PUB[key]
    m_ = rr.member(P_["M_E"], P_["th_E"], n=200001)
    M_, th_, R_, x_ = m_["M"], m_["theta"], m_["R"], m_["x"]
    a_, w_ = np.arcsin(1 / M_), rr.G.q(M_)
    pp_, rho_ = rr.G.p(M_), rr.G.rho(M_)
    md_ = lambda f: 0.5 * (f[1:] + f[:-1])          # noqa: E731

    def at(Rc):
        kk = int(np.argmin(np.abs(R_ - Rc)))
        ss = slice(0, kk + 1)
        dR_ = -np.diff(R_[ss])
        dm_ = md_((rho_ * w_ * np.sin(a_) / np.sin(a_ - th_) * 2 * np.pi * R_)[ss]) * dR_
        dF_ = md_(((pp_ + rho_ * w_ ** 2 * np.sin(a_) * np.cos(th_) / np.sin(a_ - th_)) * 2 * np.pi * R_)[ss]) * dR_
        As_ = dm_.sum() / rr.rs_ws
        return dict(L=float(x_[kk]), eps=float(np.pi / As_), C_F=float(dF_.sum() / As_), th_D=float(np.degrees(th_[kk])))
    c_, lo_, hi_ = at(P_["R_D"]), at(P_["R_D"] - 5e-4), at(P_["R_D"] + 5e-4)
    half_ = dict(L=5e-4, eps=5e-3, C_F=5e-5, th_D=5e-3)
    return max(abs(c_[q] - P_[q]) / (half_[q] + 0.5 * abs(hi_[q] - lo_[q])) for q in half_)


rep.reject("Rao e1069: ED cut at the printed R_D vs the printed L, eps, C_F, theta_D (max ratio), gamma 1.24",
           cut_ratio(R61.Rao1961(1.24), "e1069"), 1.0)

# ------------------------------------------------------------------ Humphreys, Thompson & Hoffman 1971
h = R61.hth_rao(n=200001)
H = R61.HTH
rep.check("HTH 1971 Rao nozzle: our R_E vs printed 8.33 in", h["R_E_in"] - H["y_E_in"], 5e-3)
rep.check("HTH 1971 Rao nozzle: our R_D vs Table 3 end point 1.37506 in", h["R_D"] * h["R_E_in"] - H["R_D_in"], 1e-4)
rep.check("HTH 1971 Rao nozzle: our theta_D vs Table 3 -13.25333 deg", np.degrees(h["theta_D"]) - H["th_D_deg"], 5e-3)
rep.check("HTH 1971 Rao nozzle: our thrust vs printed 34,253 lbf (their two methods differ by 2 lbf)",
          h["thrust_lbf"] - H["thrust_lbf"], 5.0)
gh = geno_case("hth71_rao")
dev = max(abs(gh["L"] / h["x_D"] - 1), abs(gh["M_D"] / h["M_D"] - 1), abs(gh["p_a"] / h["p_a"] - 1))
rep.check("HTH 1971: GENO's L, M_D, p_a vs our solver (max relative difference)", dev, 2e-4)
pts = R61.TAB3_HTH[:, :2] / h["R_E_in"]
dist_h = normal_dist(pts, gh["g"].plug[:, :2])
inside_h = pts[:, 0] >= gh["g"].x_s
rep.check("HTH 1971: Table 3 vs GENO, %d points downstream of x_s, max |normal distance| / R_E" % int(inside_h.sum()),
          float(np.max(np.abs(dist_h[inside_h]))), 1e-3)
tip = gh["g"].plug[0]
rep.note("HTH 1971: GENO throat (plug tip) flow angle %.2f deg (internal channel from M_i 1.1); Table 3 first point "
         "%.2f deg; paper's injection angle ~ -58.5" % (np.degrees(tip[4]), R61.TAB3_HTH[0, 2]))
rep.note("HTH 1971: our Rao solution M_E %.5f theta_E %.4f, R_E %.4f in, R_D %.5f in, theta_D %.3f, thrust %.0f lbf" % (
    h["M_E"], h["th_E"], h["R_E_in"], h["R_D"] * h["R_E_in"], np.degrees(h["theta_D"]), h["thrust_lbf"]))

# ------------------------------------------------------------------ figures
fig, ax = plt.subplots(2, 2, figsize=(12.5, 9.0), constrained_layout=True)
for j, (key, tab) in enumerate((("e381", R61.TAB1), ("e1069", R61.TAB2))):
    A = ax[0, j]
    R_ = res[key]
    g = R_["gc"]["g"]
    A.plot(g.plug[:, 0], g.plug[:, 1], "-", color="C0", lw=2.0, label="GENO (Rao's method)")
    A.plot(g.cowl[:, 0], g.cowl[:, 1], "-", color="0.55", lw=1.2, label="GENO cowl")
    m = R_["m"]
    kc = int(np.argmin(np.abs(m["R"] - R_["printed"]["R_D"])))
    A.plot(m["x"][:kc + 1], m["R"][:kc + 1], "--", color="0.35", lw=1.0, label="control surface ED (our solver)")
    A.plot(tab[1:, 0], tab[1:, 1], "o", mfc="none", mec="k", ms=6, label="Rao 1961, Table %d" % (1 + j))
    A.plot([0], [1], "^", color="k", ms=8)
    A.annotate("E (lip)", (0, 1), (0.05, 1.0), fontsize=9)
    A.annotate("D", (tab[-1, 0], tab[-1, 1]), (tab[-1, 0] + 0.02, tab[-1, 1] + 0.03), fontsize=9)
    A.set_aspect("equal")
    A.set_xlim(-0.25, tab[-1, 0] + 0.15)
    A.set_ylim(0.0, 1.08)
    A.set_xlabel("x / R_E")
    A.set_ylabel("R / R_E")
    A.set_title("Rao 1961, eps = %s, L/R_E = %.3f: contour" % (R_["printed"]["eps"], R_["printed"]["L"]))
    A.legend(loc="upper right", fontsize=8)
A = ax[1, 0]
m = res["e381"]["m"]
kc = int(np.argmin(np.abs(m["R"] - R61.PUB["e381"]["R_D"])))
A2 = A.twinx()
A.plot(m["R"], m["M"], "-", color="C3", lw=1.8, label="M (our solver)")
A2.plot(m["R"], np.degrees(m["theta"]), "-", color="C2", lw=1.8, label="theta (our solver)")
ed = res["e381"]["gx"]["ed"]
cj = json.load(open(os.path.join(GD("rao61_e381_pb0"), "case.json")))
Gg = exact.PerfectGas(*cj["gas"])
A.plot(ed[::12, 1], Gg.M_q(ed[::12, 3]), "s", ms=3.5, mfc="none", mec="C3", label="M (GENO)")
A2.plot(ed[::12, 1], np.degrees(ed[::12, 2]), "s", ms=3.5, mfc="none", mec="C2", label="theta (GENO)")
for kk, lab, mk in ((kc, "Rao's D", "o"), (len(m["R"]) - 1, "D for p_b = 0", "x")):
    A.plot(m["R"][kk], m["M"][kk], mk, color="k", ms=8)
    A2.plot(m["R"][kk], np.degrees(m["theta"][kk]), mk, color="k", ms=8)
    A2.annotate(lab, (m["R"][kk], np.degrees(m["theta"][kk])), (m["R"][kk] + 0.05, np.degrees(m["theta"][kk]) - 1.5),
                fontsize=8)
A.set_xlim(1.02, 0.0)
A.set_xlabel("R / R_E along ED (E at 1)")
A.set_ylabel("Mach number", color="C3")
A2.set_ylabel("flow angle theta [deg]", color="C2")
A.set_title("Rao 1961 Fig. 2 redone: M and theta along the control surface (eps 3.81)")
h1, l1 = A.get_legend_handles_labels()
h2, l2 = A2.get_legend_handles_labels()
A.legend(h1 + h2, l1 + l2, loc="lower left", fontsize=8)
A = ax[1, 1]
for key, mk, col in (("e381", "o", "C0"), ("e1069", "s", "C1")):
    tab = R61.TAB1 if key == "e381" else R61.TAB2
    d = np.array(res[key]["dist"])
    ins = np.array(res[key]["inside"])
    A.plot(tab[1:, 0][ins], 1e4 * d[ins], mk + "-", color=col, ms=5, label="Rao 1961 Table %s - GENO" % ("1" if key == "e381" else "2"))
    A.plot(tab[1:, 0][~ins], 1e4 * d[~ins], mk, color=col, mfc="none", ms=7, label="(throat point: GENO's internal channel)")
A.plot(pts[inside_h, 0], 1e4 * dist_h[inside_h], "^-", color="C2", ms=5, label="Humphreys 1971 Table 3 - GENO")
A.axhspan(-7.07, 7.07, color="0.9", zorder=0, label="Rao's 3-decimal printing")
A.set_ylim(-12, 12)
A.set_xlabel("x / R_E")
A.set_ylabel("normal distance to GENO's contour [1e-4 R_E]")
A.set_title("Printed contours vs GENO, point by point")
A.legend(fontsize=8, loc="lower left")
rv.savefig(fig, "09_rao1961_literature.png")

fig, ax = plt.subplots(1, 2, figsize=(12.5, 4.6), constrained_layout=True, gridspec_kw=dict(width_ratios=[1.6, 1]))
A = ax[0]
RE = h["R_E_in"]
A.plot(gh["g"].plug[:, 0] * RE, gh["g"].plug[:, 1] * RE, "-", color="C0", lw=2, label="GENO, Rao's method")
A.plot(gh["g"].cowl[:, 0] * RE, gh["g"].cowl[:, 1] * RE, "-", color="0.55", lw=1.2)
A.plot(R61.TAB3_HTH[:, 0], R61.TAB3_HTH[:, 1], "o", mfc="none", mec="k", ms=6, label="HTH 1971 Table 3 (Rao contour)")
A.plot(R61.TAB2_HTH[:, 0], R61.TAB2_HTH[:, 1], "s", mfc="none", mec="C3", ms=5,
       label="HTH 1971 Table 2 (their fixed-inlet optimum, 32,881 lbf)")
A.plot([0], [RE], "^", color="k", ms=8)
A.annotate("Rao lip, y_E %.2f in" % RE, (0, RE), (0.4, RE + 0.2), fontsize=9)
A.plot([0], [7.55], "^", color="C3", ms=8)
A.annotate("fixed-inlet lip, 7.55 in", (0, 7.55), (0.4, 7.4), fontsize=9, color="C3")
A.set_aspect("equal")
A.set_xlabel("x [in] (from the lip)")
A.set_ylabel("y [in]")
A.set_title("Humphreys, Thompson & Hoffman 1971: Rao nozzle, thrust %.0f lbf (paper 34,253)" % h["thrust_lbf"])
A.legend(fontsize=8)
A = ax[1]
A.plot(R61.TAB3_HTH[inside_h, 0], 1e3 * dist_h[inside_h] * RE, "o-", color="k", ms=5)
A.set_xlabel("x [in]")
A.set_ylabel("Table 3 point - GENO contour [1e-3 in]")
A.set_title("Rao contour of HTH 1971 vs GENO")
A.axhline(0, color="0.6", lw=0.8)
rv.savefig(fig, "09_humphreys1971.png")

out = {k: {kk: vv for kk, vv in v.items() if kk not in ("m", "gc", "gx")} for k, v in res.items()}
out["hth"] = dict(R_E_in=h["R_E_in"], R_D_in=h["R_D"] * h["R_E_in"], th_D=float(np.degrees(h["theta_D"])),
                  thrust_lbf=h["thrust_lbf"], M_E=h["M_E"], th_E=h["th_E"], geno_L=gh["L"], ours_L=float(h["x_D"]),
                  dist=dist_h.tolist())
sys.exit(rep.save(out))

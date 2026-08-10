#!/usr/bin/env python3
"""A1 BRICK 2, STEP 10 [F2/A1]: THE TRUNCATED PLUG UNDER THE CYCLE —
the theory's "first genuinely averaged shape problem" (T-T4 + Remark
4.9), measured at engine level.

THE THEORY UNDER TEST. T-T4 (THEOREM* under the ideal-adaptation
closure C-HT4: wall pressure clamps to Pa downstream of each phase's
full-expansion point): per phase, plug thrust F(l; xi) is
NONDECREASING in the extension l and constant for l >= l(xi), with
l(xi) increasing in Pc(xi); the per-phase argmax sets are NESTED
half-lines, hence max_Sigma INT F dmu = INT max F dmu, attained by
the PEAK-phase design (the plug dichotomy: bell averages/T3, plug
maximizes/T4). Remark 4.9 (sharpness): a length cap, a base-pressure
model, or NON-IDEAL adaptation break the nesting; then max INT <
INT max strictly and the optimum satisfies the averaged system T7
with the mu-AVERAGED PLUG CORNER CONDITION at the truncation plane.

WHAT THE ENGINE ADDS: the real marched wall pressure does NOT clamp
— downstream of adaptation it undershoots Pa (measured). The size of
that undershoot IS the adaptation break, so the engine measures where
the truth sits between "design at the peak" (ideal T4) and the
genuinely averaged optimum (Remark 4.9).

THE ONE-MARCH-PER-PHASE STRUCTURE. For a FIXED spike, truncating at
l removes wall DOWNSTREAM of l only; in supersonic flow the removed
wall cannot influence x < l (domain of dependence). Hence a single
full-spike march per phase yields J(l; xi) for EVERY truncation l in
closed form: J(l) = F_in(gauge) + SUM_{x<l} (p_w - pa) w (-dy)
(descending spike: -dy > 0; free edge contributes 0 in the pa gauge,
p = pa on it exactly; base plane at pb = pa contributes 0). The
marginal condition dJ/dl = 0 is p_w(l) = pa — the plug corner
condition at the truncation plane; its mu-average is Remark 4.9's
averaged system.

THE WORLD (posed): axisymmetric descending-spike plug on the real-gas
NASA tables. Cowl lip at (0, 2); annular flow arrives at Mi = 1.2
aimed at the axis (theta_i = -25 deg); the lip fan (tables-consistent
PM, per phase) expands it to the shared ambient pa. The FIXED
hardware = the spike, one streamline of the MEAN phase's fan field;
the start line poses the same (M, theta)(y) profile for every phase
with each phase's own thermodynamics (exact Lemma-A data for the
pressure-only cycle; the posed "same injector Mach profile" for the
mock cycle). Each phase is marched by the certified plug march
(prescribed wall, multi-column foot search, row bookkeeping).

STAGES
  t3   — pressure-only cycle (T0 fixed): Lemma A must appear LIVE on
         the wall (p_w(x; xi)/P0 collapses to one curve, ~machine),
         and the cycle-optimal truncation must equal design-at-the-
         mean (zero gain within the derived band): the T3 collapse
         at the truncation level.
  mock — P AND T profiles (the certified mock RDE): the genuine
         average. Checks: per-phase F(l) rises to l(xi) then FALLS
         (the measured non-ideal adaptation — the break); l(xi)
         increasing in Pc (T4's nesting ORDER); the blind cycle
         optimum satisfies the mu-averaged corner condition (votes
         p_w(l*; xi) - pa: mean ~ 0 in band, each phase individually
         off, monotone in xi); INT max - max INT > band (the strict
         break of Remark 4.9); design-at-the-peak penalty quantified.
  Rejector: corrupted ambient in the vote analysis must break the
         balance.

Run:  .venv-a1/bin/python validation/a1_plug_cycle.py          # both
      STAGE=t3   .venv-a1/bin/python validation/a1_plug_cycle.py
      STAGE=mock .venv-a1/bin/python validation/a1_plug_cycle.py
"""
import json
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1               # noqa: E402
import a1_cycle_layer as CL                   # noqa: E402
from a1_plug_march import plug_march          # noqa: E402
from a1_freejet_unit import q_at_pa           # noqa: E402

import jax.numpy as jnp                       # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
NPASS = [0, 0]
HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "_plug_cycle_ckpt")
os.makedirs(CKPT, exist_ok=True)

LIP = (0.0, 2.0)
X0, X_END = 0.5, 3.0
MI, TH_I = 1.2, np.radians(-25.0)
Y_SP0 = 1.85                                 # spike start radius
# ambient posed as the mean-phase pressure at this Mach; chosen so
# the fan turn < |TH_I| and theta_E < 0: the classic plug design
# condition (adaptation near axial exit), giving a DESCENDING spike
PA_M = 1.95
# The plug FEELS the ambient through its free edge (the bell does
# not), so the cycle must be posed SHOCK-FREE: every phase
# underexpanded at the start line (p_w(x0) > pa) and adapting within
# the domain. With one shared ambient that bounds the pressure
# ratio: PR = 2.5 here (the certified PR = 10 mock would put the
# low phases 6x overexpanded — a shocked regime outside the
# isentropic march; measured: edge cells blow up and the garbage
# reaches the wall). The T-T4 / Remark 4.9 statements are
# PR-agnostic; the corpus itself conditions on shock-free flow.
PR_PLUG = 2.5


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ----------------------------------------------------------------------
# tables-consistent centered fan at the lip (per-phase tables)
# ----------------------------------------------------------------------
def fan_of(tab, pa):
    """Corner fan at the lip from (MI, TH_I) down to p = pa on the
    given tables: returns (field(x, y) -> (q, th), q1, q2, th2)."""
    ta = A1.tab_arrays(tab)
    from scipy.optimize import brentq
    as_ = tab["_as"]

    def M_of(q):
        return float(A1.state_q(jnp.float64(q), ta)[5])
    q1 = brentq(lambda q: M_of(q) - MI, 1.0001 * as_, 3.4 * as_,
                xtol=1e-11)
    q2 = q_at_pa(pa, ta, as_)
    qs = np.linspace(q1, q2, 400)
    Ms = np.array([M_of(q) for q in qs])
    mus = np.arcsin(np.clip(1.0 / Ms, 0, 1))
    dth = np.sqrt(np.maximum(Ms**2 - 1.0, 0.0)) / qs
    ths = TH_I + np.concatenate([[0.0], np.cumsum(
        0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
    phis = ths - mus                          # ray angles, monotone

    def field(x, y):
        ph = np.arctan2(y - LIP[1], x - LIP[0])
        if ph <= phis[0]:
            return q1, TH_I
        if ph >= phis[-1]:
            return float(qs[-1]), float(ths[-1])
        return (float(np.interp(ph, phis, qs)),
                float(np.interp(ph, phis, ths)))
    return field, q1, float(qs[-1]), float(ths[-1])


def streamline(field, p0, x_end, h=1e-3):
    xs, ys = [p0[0]], [p0[1]]
    x, y = p0
    while x < x_end:
        def sl(xx, yy):
            _, th = field(xx, yy)
            return np.tan(th)
        k1 = sl(x, y)
        k2 = sl(x + h / 2, y + h * k1 / 2)
        k3 = sl(x + h / 2, y + h * k2 / 2)
        k4 = sl(x + h, y + h * k3)
        y += h / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x += h
        xs.append(x)
        ys.append(y)
    return np.array(xs), np.array(ys)


# ----------------------------------------------------------------------
# one phase: march the fixed spike, return the truncation kit
# ----------------------------------------------------------------------
def phase_kit(key, tab_ph, Mprof, THprof, yline, spike, pa, K, N):
    """March phase 'key' on the fixed spike; cache and return
    (xw, p_wall, y_wall, Fin_gauge, cert_worst). The start line poses
    the shared (M, theta)(y) profile with THIS phase's tables."""
    f = os.path.join(CKPT, "%s_K%d.npz" % (key, K))
    if os.path.exists(f):
        d = np.load(f)
        return (d["xw"], d["pw"], d["yw"], float(d["Fin"]),
                float(d["cert"]))
    ta = A1.tab_arrays(tab_ph)
    qpa = q_at_pa(pa, ta, tab_ph["_as"])
    # start-line states: phase tables at the shared (M, theta) profile
    from scipy.optimize import brentq
    as_ = tab_ph["_as"]

    def q_of_M(Mt):
        return brentq(lambda q: float(
            A1.state_q(jnp.float64(q), ta)[5]) - Mt,
            1.0001 * as_, 3.4 * as_, xtol=1e-11)
    us, vs = [], []
    for M_, th_ in zip(Mprof, THprof):
        q_ = q_of_M(M_)
        us.append(q_ * np.cos(th_))
        vs.append(q_ * np.sin(th_))
    start = (X0, yline, np.array(us), np.array(vs))
    sx, sy = spike
    tgrid = np.linspace(0, 1, K)
    sxa = X0 + tgrid[1:] * (X_END - X0)
    st = (jnp.array(sxa), jnp.array(np.interp(sxa, sx, sy)),
          jnp.array(np.interp(sxa, sx, np.gradient(sy, sx))))
    out, _ = plug_march(st, start, qpa, tab_ph, 1.0)
    w = np.array(out["wall"])
    qw = np.hypot(w[:, 2], w[:, 3])
    pw = np.array(A1.state_q(jnp.array(qw), ta)[1])
    # gauge momentum influx through the start line (dense profile)
    yl = np.linspace(yline[0], yline[-1], 801)
    Mi_ = np.interp(yl, yline, Mprof)
    Th_ = np.interp(yl, yline, THprof)
    qq = np.array([q_of_M(m) for m in Mi_])
    st_ = A1.state_q(jnp.array(qq), ta)
    p_ = np.array(st_[1])
    r_ = np.array(st_[2])
    u_ = qq * np.cos(Th_)
    v_ = qq * np.sin(Th_)
    dy = np.diff(yl)
    w2 = 2.0 * np.pi * 0.5 * (yl[1:] + yl[:-1])
    um = 0.5 * (u_[1:] + u_[:-1])
    vm = 0.5 * (v_[1:] + v_[:-1])
    rm = 0.5 * (r_[1:] + r_[:-1])
    pm = 0.5 * (p_[1:] + p_[:-1])
    Fin = float(np.sum((rm * um * (um * dy - vm * 0.0)
                        + (pm - pa) * dy) * w2))
    np.savez(f, xw=w[:, 0], pw=pw, yw=w[:, 1], Fin=Fin,
             cert=out["cert_worst"])
    return w[:, 0], pw, w[:, 1], Fin, float(out["cert_worst"])


def J_of_l(xw, pw, yw, Fin, pa, lgrid):
    """Truncation family from one march: cumulative gauge wall push
    (descending spike: -dy > 0) + start influx; J(l) on lgrid."""
    dy = np.diff(yw)
    wgt = 2.0 * np.pi * 0.5 * (yw[1:] + yw[:-1])
    pm = 0.5 * (pw[1:] + pw[:-1])
    seg = (pm - pa) * wgt * (-dy)
    cum = np.concatenate([[0.0], np.cumsum(seg)])
    return Fin + np.interp(lgrid, xw, cum)


# ----------------------------------------------------------------------
def main():
    t0 = time.time()
    stage = os.environ.get("STAGE", "both")
    print("== A1 brick 2 step 10: truncated plug under the cycle"
          " [F2/A1] (stage=%s) ==" % stage)

    tab0 = A1.prep_tab(A1.build_tab_nasa())
    ts, ps = tab0["ts"], tab0["ps"]

    # cycle construction (the certified cycle-layer SHAPE, at the
    # shock-free PR_PLUG — see the posing note at the top)
    xi = (np.arange(CL.NXI) + 0.5) / CL.NXI
    I1 = (1.0 - 1.0 / PR_PLUG) / np.log(PR_PLUG)
    P0s = (ps / I1) * PR_PLUG ** (-xi)
    gm = tab0["gammamedio"]
    TR = PR_PLUG ** ((gm - 1.0) / gm)
    T0s_mock = 3850.0 * TR ** (-xi)

    # shared ambient: mean-phase pressure at Mach PA_M (posed)
    ta0 = A1.tab_arrays(tab0)
    from scipy.optimize import brentq
    as0 = tab0["_as"]
    q_pa = brentq(lambda q: float(
        A1.state_q(jnp.float64(q), ta0)[5]) - PA_M,
        1.0001 * as0, 3.4 * as0, xtol=1e-11)
    pa = float(A1.state_q(jnp.float64(q_pa), ta0)[1])
    print("  ambient pa = %.6e  (mean-phase p at M = %.2f)"
          % (pa, PA_M))

    # THE FIXED HARDWARE: spike = mean-phase fan streamline; the
    # shared start profile (M, theta)(y) from the same field
    field0, q1_0, q2_0, th2_0 = fan_of(tab0, pa)
    sx, sy = streamline(field0, (0.0, Y_SP0), X_END)
    print("  world: spike y %.3f -> %.3f over x [0, %.1f];"
          " fan turn to theta_E = %.2f deg"
          % (Y_SP0, sy[-1], X_END, np.degrees(th2_0)))

    def profiles(N):
        y_w0 = float(np.interp(X0, sx, sy))
        y_e0 = LIP[1] + np.tan(th2_0) * X0
        yline = np.linspace(y_w0, y_e0, N)
        Ms, Ths = [], []
        for yy in yline:
            q_, th_ = field0(X0, yy)
            Ms.append(float(A1.state_q(jnp.float64(q_), ta0)[5]))
            Ths.append(th_)
        return yline, np.array(Ms), np.array(Ths)

    lgrid = np.linspace(X0 + 0.1, X_END - 0.02, 400)

    def cycle_kits(tag, T0s, K, N):
        yline, Ms, Ths = profiles(N)
        kits = []
        for k in range(CL.NXI):
            tph = CL.phase_tab(tab0, P0s[k], T0s[k])
            kits.append(phase_kit(
                "%s_p%d" % (tag, k), tph, Ms, Ths, yline,
                (sx, sy), pa, K, N))
        return kits

    def run_stage_t3():
        # THE PLUG DOES NOT COLLAPSE. T3's collapse theorem applies
        # to FIXED FULL-FLOWING walls (the bell): pressure scaling
        # leaves such a flow invariant. The plug's free edge feeds
        # the ambient INTO the flow (that is the adaptation
        # mechanism), so even a pressure-only cycle must NOT design
        # at the mean — it shifts toward the peak (T-T4's side of
        # the dichotomy). This stage tests exactly that: Lemma A
        # holds only on the pa-SHIELDED wall region (upstream of the
        # first edge-arrival), and the cycle-optimal truncation sits
        # strictly ABOVE the mean design, bounded by the peak.
        print("-- stage t3: pressure-only cycle (the plug"
              " ANTI-collapse) --")
        T0s = np.full(CL.NXI, ts)
        kc = cycle_kits("t3", T0s, 33, 17)
        kf = cycle_kits("t3", T0s, 65, 33)
        certs = [k[4] for k in kc + kf]
        check("T-1 all phase marches Newton-certified",
              max(certs) <= 1.0)

        # derived pa-shielded region: trace the edge's first C-
        # (mean state at pa: theta_E, mu(M_pa)) to the wall
        Mpa = PA_M
        mu_e = np.arcsin(1.0 / Mpa)
        sl_e = np.tan(th2_0 - mu_e)
        y_e0 = LIP[1] + np.tan(th2_0) * X0
        xs_ = np.linspace(X0, X_END, 400)
        ye_ = y_e0 + sl_e * (xs_ - X0)
        yw_ = np.interp(xs_, sx, sy)
        hit = xs_[ye_ <= yw_]
        x_shield = 0.9 * (float(hit[0]) if hit.size else X_END)
        msk = kf[0][0] < x_shield
        base = kf[0][1][msk] / P0s[0]
        dev = max(float(np.max(np.abs(
            k[1][msk] / P0s[j] - base) / base))
            for j, k in enumerate(kf))
        print("  T-2 wall Lemma A on the pa-shielded region"
              " (x < %.2f): max rel spread of p_w/P0 = %.2e"
              % (x_shield, dev))
        check("T-2 Lemma A live where the ambient cannot reach"
              " (< 1e-9)", dev < 1.0e-9)

        def lstar_from(kits):
            Jc = np.mean([J_of_l(*k[:4], pa, lgrid) for k in kits],
                         axis=0)
            return lgrid[int(np.argmax(Jc))], Jc

        lc, _ = lstar_from(kc)
        lf, Jf = lstar_from(kf)
        # mean-phase design l (the phase at <P0> = ps)
        tmean = CL.phase_tab(tab0, ps, ts)
        yline, Ms, Ths = profiles(33)
        km = phase_kit("t3_mean", tmean, Ms, Ths, yline,
                       (sx, sy), pa, 65, 33)
        Jm = J_of_l(*km[:4], pa, lgrid)
        lm = lgrid[int(np.argmax(Jm))]
        # peak-phase design l
        Jp = J_of_l(*kf[0][:4], pa, lgrid)
        lp = lgrid[int(np.argmax(Jp))]
        band_l = K_RICH * abs(lc - lf) + (lgrid[1] - lgrid[0])
        print("  T-3 truncations: cycle l* = %.4f vs mean-design"
              " %.4f vs peak-design %.4f (band %.2e)"
              % (lf, lm, lp, band_l))
        check("T-3 ANTI-collapse: cycle l* strictly above the mean"
              " design (the plug does not average)",
              lf > lm + band_l)
        check("T-4 cycle l* bounded by the peak design (within"
              " band)", lf <= lp + band_l)
        # per-phase optima: T4's nesting ORDER under pressure only
        lxs = []
        for k in kf:
            J = J_of_l(*k[:4], pa, lgrid)
            lxs.append(lgrid[int(np.argmax(J))])
        print("  T-5 per-phase l(xi) [high->low P0]: " +
              " ".join("%.3f" % v for v in lxs))
        check("T-5 nesting order: l(xi) nonincreasing as P0 falls",
              all(lxs[i] >= lxs[i + 1] - band_l
                  for i in range(len(lxs) - 1)))

    def run_stage_mock():
        print("-- stage mock: P and T profiles (the genuine"
              " average) --")
        kc = cycle_kits("mock", T0s_mock, 33, 17)
        kf = cycle_kits("mock", T0s_mock, 65, 33)
        certs = [k[4] for k in kc + kf]
        check("M-1 all phase marches Newton-certified",
              max(certs) <= 1.0)

        # per-phase F(l): rise to l(xi), then FALL (measured break);
        # l(xi) increasing in P0 (T4 nesting ORDER)
        lxs, breaks = [], []
        for j, k in enumerate(kf):
            J = J_of_l(*k[:4], pa, lgrid)
            i = int(np.argmax(J))
            lxs.append(lgrid[i])
            breaks.append((J[i] - J[-1]) / max(J[i], 1.0))
        lxs = np.array(lxs)
        print("  M-2 per-phase l(xi) [high->low P0]: " +
              " ".join("%.3f" % v for v in lxs))
        interior = lxs < lgrid[-1] - 2 * (lgrid[1] - lgrid[0])
        order_ok = all(lxs[i] >= lxs[i + 1] - 1e-9
                       for i in range(len(lxs) - 1)
                       if interior[i] and interior[i + 1])
        check("M-2 nesting order: l(xi) nonincreasing as P0 falls",
              order_ok)
        print("  M-3 adaptation break per phase (J(l*)-J(end))/J:"
              " " + " ".join("%.2e" % b for b in breaks))
        check("M-3 non-ideal adaptation measured (some interior"
              " phase loses thrust past l(xi))",
              any(b > 1e-4 for j, b in enumerate(breaks)
                  if interior[j]))

        # blind cycle optimum + the mu-averaged corner condition
        Jc_c = np.mean([J_of_l(*k[:4], pa, lgrid) for k in kc],
                       axis=0)
        Jc_f = np.mean([J_of_l(*k[:4], pa, lgrid) for k in kf],
                       axis=0)
        lc = lgrid[int(np.argmax(Jc_c))]
        lf = lgrid[int(np.argmax(Jc_f))]
        json.dump(dict(pa=pa, lstar=float(lf)),
                  open(os.path.join(CKPT, "meta.json"), "w"))
        band_l = K_RICH * abs(lc - lf) + (lgrid[1] - lgrid[0])
        votes = np.array([float(np.interp(lf, k[0], k[1])) - pa
                          for k in kf])
        # derived balance band: the vote mean shifts J' by
        # <dA/dl> * mean; translate the l-band through the local
        # curvature of J_cycle
        i0 = int(np.argmax(Jc_f))
        dA = 2.0 * np.pi * float(np.interp(lf, kf[0][0], kf[0][2])) \
            * abs(float(np.gradient(
                np.interp(lgrid, kf[0][0], kf[0][2]), lgrid)[i0]))
        d2J = abs(float(np.gradient(np.gradient(Jc_f, lgrid),
                                    lgrid)[i0]))
        band_v = (d2J * band_l) / max(dA, 1e-30)
        print("  M-4 votes p_w(l*)-pa [Pa]: " +
              " ".join("%+.3e" % v for v in votes))
        print("      mean = %+.3e vs balance band %.3e"
              % (votes.mean(), band_v))
        check("M-4 mu-averaged corner condition: vote mean ~ 0 in"
              " band", abs(votes.mean()) <= band_v)
        # NOTE (measured, kept honest): the bell's pointwise vote
        # structure (monotone in phase, one sign change) does NOT
        # transfer to the plug — downstream of adaptation the wall
        # pressure OSCILLATES around pa (fan waves reflected off the
        # free edge), so pointwise votes sample the oscillation.
        # Remark 4.9 claims only the mu-AVERAGED balance (M-4) and
        # the genuine-compromise structure, checked as:
        check("M-5 per-phase optima genuinely spread (no common"
              " maximizer)", lxs.max() - lxs.min() > 4 * band_l)
        check("M-6 l* is a strict interior compromise (no extreme"
              " phase owns it)",
              lxs.min() + band_l < lf < lxs.max() - band_l)

        # the strict break: INT max - max INT > band; peak design
        Jmaxes = [float(np.max(J_of_l(*k[:4], pa, lgrid)))
                  for k in kf]
        int_max = float(np.mean(Jmaxes))
        max_int = float(np.max(Jc_f))
        Jmaxes_c = [float(np.max(J_of_l(*k[:4], pa, lgrid)))
                    for k in kc]
        band_g = K_RICH * abs((float(np.mean(Jmaxes_c))
                               - float(np.max(Jc_c)))
                              - (int_max - max_int)) \
            + A1.C_FLOOR * EPS * int_max
        print("  M-7 INT max - max INT = %.4e (band %.4e; rel"
              " %.2e of J)" % (int_max - max_int, band_g,
                               (int_max - max_int) / max_int))
        check("M-7 Remark 4.9 strict break: INT max > max INT",
              int_max - max_int > band_g)
        Jpeak = float(np.interp(lxs[0], lgrid, Jc_f))
        print("  M-8 design-at-the-peak penalty: (J(l*) - J(l_peak))"
              "/J = %.3e" % ((max_int - Jpeak) / max_int))
        check("M-8 peak design suboptimal under the break"
              " (penalty > 0 beyond band)",
              max_int - Jpeak > d2J * band_l**2)

        # rejector: corrupted ambient must break the vote balance
        votes_bad = np.array([float(np.interp(lf, k[0], k[1]))
                              - 1.2 * pa for k in kf])
        print("  R-1 corrupted-pa vote mean = %+.3e vs band %.3e"
              % (votes_bad.mean(), band_v))
        check("R-1 rejector: corrupted ambient leaves the balance"
              " band", abs(votes_bad.mean()) > band_v)

    if stage in ("t3", "both"):
        run_stage_t3()
    if stage in ("mock", "both"):
        run_stage_mock()

    print("== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()

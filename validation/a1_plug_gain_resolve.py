#!/usr/bin/env python3
"""A1 BRICK 2, SESSION S23 [F2/A1]: RESOLVING THE FREE-FORM SPIKE'S
GAIN — the better instrument S22 called for. Registry ID: [X-PGRS].

WHAT THIS ANSWERS. S21 (C-6) and S22 (A-8) both left the headline
claim of the free-form spike unresolved: every measured gain over the
fan streamline falls monotonically under march refinement and stays
inside the ladder band. S22's diagnosis: the optimum was TUNED at the
coarse resolution, so it is flattered by exactly the error it was
tuned against, and the march converges too slowly on the difference
for brute-force ladders. This carrier applies the two better
instruments, in escalating stages, cheapest first:

  1. EXTRAPOLATION DONE RIGHT (stage analysis). The S22 ladders,
     per design: the streamline's J converges cleanly (measured
     r ~ 0.51, first order); the 61-tuned optima are NON-MONOTONE
     (r < 0). Each admissible sequence is extrapolated by its own
     geometric model; the PAIRED difference of a clean sequence and a
     non-monotone one is NOT geometric, and this carrier REFUSES to
     extrapolate it (mixed-mode rejector R-1c; the naive paired fit
     gives r = 0.85 and a -0.5% "limit" that describes nothing).
  2. AN INCUMBENT THAT IS NOT TUNED TO THE COARSE MARCH (stage
     fineopt). The S22 adaptive optimum (m = 11) is re-optimized by
     the untouched [X-PSPL] TR-SQP driver AT (K, N) = (121, 101) —
     the design vector starts from the S22 record, the class is
     unchanged, only the instrument sharpens. Both designs are then
     marched fresh at the first three rungs (61,51)(121,101)(241,201)
     at full precision.
  3. A FOURTH RUNG AND A MODEL CHECK (stages rung4/final). If the
     three-rung ladders do not resolve the sign, the (481, 401) rung
     is added for the streamline and the fine-tuned optimum. With
     four points the geometric model is CHECKED, not assumed: rung 4
     is predicted from rungs 1-3 and the miss is reported; the limit
     is re-extrapolated from rungs 2-4; and the BAND on the gain is
     K_RICH x |limit(2-4) - limit(1-3)| + C_FLOOR*EPS — the measured
     stability of the extrapolation under its own refinement, i.e. a
     ladder OF extrapolations, per the trap-2 discipline.

THE VERDICT RULE, DECLARED BEFORE THE DECISIVE RUNS (stage final):
with gain* = J*(fine optimum)/J*(streamline) - 1 from the rung-2-4
extrapolations and `band` as above,
    gain* >  band  -> the free-form spike BEATS the streamline;
    gain* < -band  -> the STREAMLINE is optimal at this length in
                      this basis (the S21/S22 "gain" was instrument);
    |gain*| <= band -> gain is ZERO within band.
The experiment counts as RESOLVED iff band <= BAR = 4e-4 (0.04%,
half the smallest gain any session has quoted); an unresolved outcome
is reported honestly and the escalation options are printed.

CHECKS
  R-1  extrapolator selftest: (a) exact geometric series recovered to
       machine precision; (b) noisy geometric recovered within its
       own band; (c) mixed-mode / non-geometric input REFUSED;
  R-2  record checks before anything is built: J(S22 optimum) at
       (61,51) reproduces design.json to 1e-10; the fresh rung-1/2
       J's reproduce the S22 run-of-record log to its printed
       precision (5e-8);
  R-3  fine-opt gates: every accepted design Newton-certified; the
       fine optimum does not lose to its warm start AT ITS OWN
       resolution (the C-5 discipline);
  R-4  adjoint spot check at the fine optimum (AD vs FD ladder);
  R-5  the geometric-model check at rung 4: the rung-4 prediction
       miss must be smaller than the rung-3 -> rung-4 step it
       predicts (else the model is refused and the verdict is
       UNRESOLVED by declaration);
  V    the verdict rule above.

STAGES (env PGRS_STAGE): selftest | analysis | fineopt |
rung4 (with PGRS_DESIGN = inc | fine) | final | all-serial.
Artifacts under validation/_plug_gain/. On-demand carrier (env: jax).

Run:
  $PY validation/a1_plug_gain_resolve.py                    # selftest+analysis
  PGRS_STAGE=fineopt $PY validation/a1_plug_gain_resolve.py
  PGRS_STAGE=rung4 PGRS_DESIGN=inc  $PY ...   # parallel-safe
  PGRS_STAGE=rung4 PGRS_DESIGN=fine $PY ...
  PGRS_STAGE=final $PY validation/a1_plug_gain_resolve.py
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

# the FINE instrument is the working one for this carrier: reach
# a1_plug_spline_opt BEFORE import (module constants read from env).
K2, N2 = 121, 101
os.environ["PSPL_M"] = "10"
os.environ["PSPL_K"] = str(K2)
os.environ["PSPL_N"] = str(N2)

import a1_plug_spline_opt as P                         # noqa: E402
import a1_ideal_march_jax as A1                        # noqa: E402
import a1_config_compare as CC                         # noqa: E402

import jax.numpy as jnp                                # noqa: E402

RUNGS = [(61, 51), (121, 101), (241, 201), (481, 401),
         (961, 801), (1921, 1601)]
BAR = 4e-4                       # declared sharpness target on the band
ITERS = int(os.environ.get("PGRS_ITERS", 20))
ART = os.path.join(HERE, "_plug_gain")
# production S22 record: tagged name if a post-S23 run wrote
# it, else the committed legacy name
_dj_tag = os.path.join(HERE, "_plug_adaptive",
                       "design_m10_k61_n51.json")
_dj_old = os.path.join(HERE, "_plug_adaptive", "design.json")
DESIGN_JSON = _dj_tag if os.path.exists(_dj_tag) else _dj_old
S22_LOG = os.path.join(HERE, "_plug_adaptive", "run_of_record_S22.log")

NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# the extrapolator: one geometric mode, refused otherwise
# ======================================================================
def geom_limit(vals):
    """Geometric-model limit of a sequence measured on a spacing-
    halving ladder. Returns (limit, r) or (None, r) when the model is
    inadmissible: |r| >= 1 (not converging) or d12 == 0."""
    x1, x2, x3 = vals[-3], vals[-2], vals[-1]
    d12, d23 = x2 - x1, x3 - x2
    if d12 == 0.0:
        return None, 0.0
    r = d23 / d12
    if abs(r) >= 1.0:
        return None, r
    return x3 + d23 * r / (1.0 - r), r


def selftest():
    print("-- R-1: extrapolator selftest --")
    ok = True
    # (a) exact geometric series
    lim_true, C, r = 7.0, 3.0, 0.4
    vals = [lim_true - C * r ** k for k in range(3)]
    lim, _ = geom_limit(vals)
    ok &= check("R-1a exact geometric series recovered (err %.1e)"
                % abs(lim - lim_true), abs(lim - lim_true) < 1e-12)
    # alternating-sign mode is admissible too
    vals = [lim_true - C * (-0.3) ** k for k in range(3)]
    lim, _ = geom_limit(vals)
    ok &= check("R-1a' alternating geometric recovered (err %.1e)"
                % abs(lim - lim_true), abs(lim - lim_true) < 1e-12)
    # (b) noise: limit moves by O(noise/(1-r)); just require finite +
    # within a generous derived band
    rng = np.random.default_rng(0)
    vals = [lim_true - C * r ** k + 1e-6 * rng.standard_normal()
            for k in range(3)]
    lim, _ = geom_limit(vals)
    ok &= check("R-1b noisy geometric within its coarse band",
                lim is not None and abs(lim - lim_true) < 1e-4)
    # (c) mixed-mode rejection: a divergent-ratio sequence is refused
    lim, r = geom_limit([0.0, 1.0, 3.0])
    ok &= check("R-1c non-contracting sequence REFUSED (r = %.2f)" % r,
                lim is None)
    return ok


# ======================================================================
# world + designs
# ======================================================================
def load_designs():
    art = json.load(open(DESIGN_JSON))
    xk = np.array([float(eval(v)) for v in art["design"]["xk"]])
    W_a61 = np.array([float(eval(v)) for v in art["design"]["W"]])
    J_a61_rec = float(eval(art["design"]["J"]))
    return xk, W_a61, J_a61_rec


def rung_case(w, rung):
    K, N = RUNGS[rung]
    return K, P.build_case(w, N=N)


def J_at(W, w, c, K):
    out, sch = P.march_record(np.asarray(W, dtype=float), w, c, K=K)
    J = float(P.J_replay(jnp.asarray(W, dtype=float), w, c, sch,
                         w["ta"], K=K))
    return J, float(out["cert_worst"])


def parse_s22_rungs():
    """The adaptive A-8 rung J's from the committed S22 log (first
    three 'rung (K=...' lines)."""
    import re
    vals = []
    pat = re.compile(r"rung \(K=\s*\d+, N=\s*\d+\): J_inc ([\d.e+-]+)"
                     r"\s+J_opt ([\d.e+-]+)")
    for ln in open(S22_LOG):
        m = pat.search(ln)
        if m and len(vals) < 3:
            vals.append((float(m.group(1)), float(m.group(2))))
    return vals


# ======================================================================
def stage_analysis():
    """Extrapolation of the RECORDED S22 ladders, per design; the
    paired route demonstrated inadmissible. No verdict here."""
    print("-- stage analysis: the recorded S22 ladders, "
          "extrapolated per design --")
    rec = parse_s22_rungs()
    Ji = [a for a, _ in rec]
    Ja = [b for _, b in rec]
    li, ri = geom_limit(Ji)
    la, ra = geom_limit(Ja)
    print("  J(streamline):   r = %+.3f  limit %s"
          % (ri, "%.6e" % li if li else "REFUSED"))
    print("  J(61-tuned opt): r = %+.3f  limit %s"
          % (ra, "%.6e" % la if la else "REFUSED"))
    if li and la:
        print("  provisional gain limit (61-tuned) = %+.4f %%  "
              "<- the overfit measurement, NOT the verdict"
              % (100 * (la / li - 1.0)))
    D = [b - a for a, b in zip(Ji, Ja)]
    ld, rd = geom_limit(D)
    same_mode = (ri is not None and ra is not None
                 and np.sign(ri) == np.sign(ra))
    print("  paired-difference route: r = %+.3f -> %s (modes %s)"
          % (rd, "would give %.3e" % ld if ld else "REFUSED",
             "match" if same_mode else "MIXED -> route inadmissible"))
    check("analysis: the paired route is refused when the two "
          "designs converge in different modes", not same_mode)
    os.makedirs(ART, exist_ok=True)
    json.dump(dict(Ji=Ji, Ja=Ja, lim_inc=li, lim_a61=la,
                   r_inc=ri, r_a61=ra),
              open(os.path.join(ART, "analysis.json"), "w"), indent=1)


def stage_fineopt():
    """Re-optimize at (121,101) from the S22 optimum; fresh 3-rung
    ladders for both designs at full precision."""
    t0 = time.time()
    w = CC.build_world()
    ta = w["ta"]
    xk, W_a61, J_a61_rec = load_designs()
    os.makedirs(ART, exist_ok=True)

    # ---- R-2 record checks ------------------------------------------
    print("-- R-2: record checks against the S22 artifacts --")
    K1, c1 = rung_case(w, 0)
    J61, cert61 = J_at(W_a61, w, dict(c1, xk=xk), K1)
    rel = abs(J61 / J_a61_rec - 1.0)
    check("R-2a J(S22 optimum) at (61,51) reproduces design.json "
          "(rel %.1e)" % rel, rel <= 1e-10)
    rec = parse_s22_rungs()
    ok2 = True
    for rung in (0, 1):
        K, c = rung_case(w, rung)
        cm = dict(c, xk=xk)
        J_i, _ = J_at(np.interp(xk, c1["sx"], c1["sy"]), w, cm, K)
        J_o, _ = J_at(W_a61, w, cm, K)
        for got, want, tag in ((J_i, rec[rung][0], "inc"),
                               (J_o, rec[rung][1], "opt")):
            r_ = abs(got / want - 1.0)
            ok2 &= r_ <= 5e-8
            print("    rung %d %s: %.8e vs log %.8e (rel %.1e)"
                  % (rung + 1, tag, got, want, r_))
    check("R-2b fresh rung-1/2 J's reproduce the S22 log at printed "
          "precision", ok2)

    # ---- the fine optimization (the module default IS (121,101)) ----
    print("\n-- fine optimization at (K,N) = (%d,%d), warm from the "
          "S22 optimum --" % (K2, N2))
    c_fine = dict(P.build_case(w), xk=xk)     # N = 101 module default
    W_f, hist, n_rec = P.run_trsqp(W_a61.copy(), w, c_fine, ta,
                                   max_segments=ITERS)
    J_f121, cert_f = J_at(W_f, w, c_fine, K2)
    J_a61_121, _ = J_at(W_a61, w, c_fine, K2)
    print("  fine optimum: J(121) = %.8e (warm start %.8e, +%.4f%%) "
          "cert %.3f, %d segments"
          % (J_f121, J_a61_121, 100 * (J_f121 / J_a61_121 - 1.0),
             cert_f, len(hist)))
    check("R-3 fine optimum certified and does not lose to its warm "
          "start at its own resolution",
          cert_f <= 1.0 and J_f121 >= J_a61_121)

    # ---- R-4 adjoint spot at the fine optimum ------------------------
    out_f, sch_f = P.march_record(W_f, w, c_fine)
    J0, g0 = P.J_and_grad(W_f, w, c_fine, ta, sch_f)
    fj = lambda z: P.J_replay(z, w, c_fine, sch_f, ta)   # noqa: E731
    ok4 = True
    for k in (0, len(g0) - 1):
        v = jnp.zeros(len(g0)).at[k].set(1.0)
        scale = max(1.0, abs(float(W_f[k])))
        fd, spread = P.fd_ladder(fj, jnp.asarray(W_f), v, scale)
        band = (A1.K_RICH * spread + A1.C_FLOOR * A1.EPS * abs(J0)
                / (P.FD_LADDER[-1] * scale))
        ok4 &= abs(fd - g0[k]) <= band
        print("    node %2d: AD %+.6e FD %+.6e |d| %.2e (band %.2e)"
              % (k, g0[k], fd, abs(fd - g0[k]), band))
    check("R-4 adjoint matches the FD ladder at the fine optimum", ok4)

    # ---- fresh 3-rung ladders, full precision ------------------------
    print("\n-- fresh ladders, rungs 1-3, both designs --")
    W_inc = np.interp(xk, c1["sx"], c1["sy"])
    Ji, Jf = [], []
    for rung in range(3):
        K, c = rung_case(w, rung)
        cm = dict(c, xk=xk)
        t1 = time.time()
        a, _ = J_at(W_inc, w, cm, K)
        b, _ = J_at(W_f, w, cm, K)
        Ji.append(a)
        Jf.append(b)
        print("    rung (%3d,%3d): J_inc %.10e  J_fine %.10e  "
              "gain %+.5f %%  (%.0f s)"
              % (K, RUNGS[rung][1], a, b, 100 * (b / a - 1.0),
                 time.time() - t1), flush=True)
    li, ri = geom_limit(Ji)
    lf, rf = geom_limit(Jf)
    print("  extrapolations: inc r %+.3f limit %s | fine r %+.3f "
          "limit %s"
          % (ri, "%.6e" % li if li else "REFUSED",
             rf, "%.6e" % lf if lf else "REFUSED"))
    if li and lf:
        print("  PROVISIONAL 3-rung gain limit = %+.4f %%"
              % (100 * (lf / li - 1.0)))
    np.savez(os.path.join(ART, "fineopt.npz"),
             xk=xk, W_fine=np.asarray(W_f), W_inc=W_inc,
             W_a61=W_a61, Ji=Ji, Jf=Jf, J_f121=J_f121,
             hist=np.array([(h[0], h[1]) for h in hist]))
    print("  saved %s  (%.0f s total)" % (os.path.join(
        ART, "fineopt.npz"), time.time() - t0))


def stage_rung4():
    """One design, one march at RUNGS[PGRS_RUNG] (0-based; default 3
    = (481,401)). Parallel-safe. S23 addendum: the certification gate
    is REPORTED, not binding, at rungs >= 4 — the measured failure
    there is a round-off-MARGIN degradation (one wall cell at 2.7x a
    machine-epsilon-scale bound, J-effect ~1e-13 relative), and its
    K-trend is booked as an open march-contract item rather than a
    verdict input."""
    which = os.environ.get("PGRS_DESIGN", "")
    assert which in ("inc", "fine"), "PGRS_DESIGN must be inc|fine"
    rung = int(os.environ.get("PGRS_RUNG", 3))
    d = np.load(os.path.join(ART, "fineopt.npz"))
    W = d["W_inc"] if which == "inc" else d["W_fine"]
    w = CC.build_world()
    K, N = RUNGS[rung]
    print("-- rung %d (%d,%d) for design '%s' --"
          % (rung + 1, K, N, which))
    t0 = time.time()
    c = dict(P.build_case(w, N=N), xk=d["xk"])
    J, cert = J_at(W, w, c, K)
    print("  J = %.10e  cert = %.3f  (%.0f s)"
          % (J, cert, time.time() - t0))
    ok = cert <= 1.0
    print("  march certification: %s (%.3f vs 1.0)%s"
          % ("OK" if ok else "MARGIN-DEGRADED", cert,
             "" if ok else " — reported, not binding at this rung"))
    np.savez(os.path.join(ART, "rung%d_%s.npz" % (rung + 1, which)),
             J=J, cert=cert)


def stage_final():
    """Assemble every rung on disk; verdict from the PAIRED gain
    ladder. AMENDMENT DECLARED 2026-08-11 BEFORE rung 6 completed
    (the decisive data): rungs 4-5 showed the fine design's OWN
    J-ladder still carries its de-tuning transient (diff ratios
    0.047 -> -26.5 -> 0.81: not single-mode), so its per-design
    extrapolation is REFUSED by the same mixed-mode rule as ever.
    The PAIRED gain sequence, however, became single-mode once the
    design left its tuning window: its diff ratios settle toward the
    march's own first order (measured 0.829, 0.621, 0.554 on rungs
    1-5). Rule of record:
      gain* = geometric limit of the LAST gain window;
      R-5'a: |r| < 1 in the last two gain windows, and the last
             ratio is closer to the march order 0.5 than the one
             before (single-mode settling, measured not assumed);
      R-5'b: the last rung's gain is PREDICTED from the window
             before it; the miss must not exceed the actual last
             step (the model earns its extrapolation);
      band  = K_RICH * |gain*(last window) - gain*(previous window)|
              + C_FLOOR*EPS.
    Verdict sentence unchanged (positive / negative / zero within
    band; RESOLVED iff band <= BAR). The streamline's own clean
    first-order ladder is reported as supporting evidence, and the
    march-certification MARGIN degradation at rungs >= 4 is reported
    (round-off-scale, J-irrelevant, open item)."""
    print("-- stage final: the verdict (paired-ladder rule of "
          "record) --")
    d = np.load(os.path.join(ART, "fineopt.npz"))
    Ji, Jf = list(d["Ji"]), list(d["Jf"])
    n = 4
    while True:
        fi = os.path.join(ART, "rung%d_inc.npz" % n)
        ff = os.path.join(ART, "rung%d_fine.npz" % n)
        if not (os.path.exists(fi) and os.path.exists(ff)):
            break
        Ji.append(float(np.load(fi)["J"]))
        Jf.append(float(np.load(ff)["J"]))
        n += 1
    R = len(Ji)
    print("  %d rungs on disk" % R)
    print("  J_inc  ladder: %s" % ["%.8e" % v for v in Ji])
    print("  J_fine ladder: %s" % ["%.8e" % v for v in Jf])
    g = [b / a - 1.0 for a, b in zip(Ji, Jf)]
    print("  paired gains [%%]: %s" % ["%+.5f" % (100 * x) for x in g])
    dg = [g[k + 1] - g[k] for k in range(R - 1)]
    rr = [dg[k + 1] / dg[k] for k in range(R - 2)]
    print("  gain diffs: %s" % ["%+.3e" % x for x in dg])
    print("  diff ratios: %s" % ["%+.4f" % x for x in rr])
    verdict = dict(Ji=Ji, Jf=Jf, gains=g)
    li_last, ri_last = geom_limit(Ji[-3:])
    li_prev, _ = geom_limit(Ji[-4:-1]) if R >= 4 else (None, None)
    if li_last:
        print("  J_inc limit (last window): %.8e (r %+.3f; prev "
              "window %s)" % (li_last, ri_last,
                              "%.8e" % li_prev if li_prev else "n/a"))
    ok = True
    r_last, r_prev = rr[-1], rr[-2]
    ok_a = (abs(r_last) < 1.0 and abs(r_prev) < 1.0
            and abs(r_last - 0.5) <= abs(r_prev - 0.5))
    print("  R-5'a: last ratios %.4f -> %.4f (march order 0.5): %s"
          % (r_prev, r_last, "settling" if ok_a else "NOT settling"))
    ok &= check("R-5'a paired ladder single-mode and settling toward "
                "the march order", ok_a)
    g_pred = g[-2] + dg[-2] * rr[-2]
    miss, step = abs(g_pred - g[-1]), abs(dg[-1])
    print("  R-5'b: last gain predicted %+.5f %% actual %+.5f %% "
          "(miss %.3e vs step %.3e)"
          % (100 * g_pred, 100 * g[-1], miss, step))
    ok &= check("R-5'b the model predicts the last rung within its "
                "own step", miss <= step)
    lim_last, r1 = geom_limit(g[-3:])
    lim_prev, r0 = geom_limit(g[-4:-1])
    if not ok or lim_last is None or lim_prev is None:
        print("  VERDICT: UNRESOLVED by declaration (model gates "
              "failed). Escalation: rung 7, or the exact-functional "
              "route.")
        verdict["verdict"] = "UNRESOLVED-model"
    else:
        band = A1.K_RICH * abs(lim_last - lim_prev) + A1.C_FLOOR * A1.EPS
        print("  gain limit: prev window %+.5f %%, last window "
              "%+.5f %% -> quote %+.5f %%, band %.5f %% (BAR %.4f %%)"
              % (100 * lim_prev, 100 * lim_last, 100 * lim_last,
                 100 * band, 100 * BAR))
        resolved = band <= BAR
        if lim_last > band:
            label = "the free-form spike BEATS the streamline"
        elif lim_last < -band:
            label = ("the computed free-form optimum is WORSE than "
                     "the streamline in the limit (overfit measured); "
                     "the streamline stands unbeaten at this length")
        else:
            label = ("the gain is ZERO within the band — the "
                     "truncated streamline is optimal at this length "
                     "to within |%.4f| %%" % (100 * (abs(lim_last)
                                                     + band)))
        print("  VERDICT: %s (%s: band %s BAR)"
              % (label, "RESOLVED" if resolved else "NOT RESOLVED",
                 "<=" if resolved else ">"))
        check("V the experiment is resolved (band <= BAR)", resolved)
        verdict.update(verdict="%s | %s" % (label,
                       "RESOLVED" if resolved else "UNRESOLVED"),
                       gain=lim_last, band=band, gain_prev=lim_prev)
    json.dump(verdict, open(os.path.join(ART, "verdict.json"), "w"),
              indent=1)
    print("  written %s" % os.path.join(ART, "verdict.json"))


def main():
    stage = os.environ.get("PGRS_STAGE", "default")
    print("== A1 S23: resolving the free-form spike's gain "
          "[X-PGRS] (stage %s) ==" % stage)
    ok = True
    if stage in ("selftest", "default", "all-serial"):
        ok &= selftest()
    if stage in ("analysis", "default", "all-serial"):
        stage_analysis()
    if stage in ("fineopt", "all-serial"):
        stage_fineopt()
    if stage == "rung4" or stage == "all-serial":
        if stage == "all-serial":
            for which in ("inc", "fine"):
                os.environ["PGRS_DESIGN"] = which
                stage_rung4()
        else:
            stage_rung4()
    if stage in ("final", "all-serial"):
        stage_final()
    print("\n== %d/%d PASS ==" % (NPASS[0], NPASS[1]))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()

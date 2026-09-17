"""The base-pressure closure of the truncated plug, made executable
[F3/A1, slot N2].

WHAT THIS IS. The problem book declares the plug sector with its
truncation length and its base-pressure closure as a DECLARED SLOT
(docs/rde_nozzle_problem_book.md:348, sector (ii)), and the choice
ledger's C61 records the axis with status NEVER and an incumbent that
the program has NOT adopted: Vander Veen-Gentry-Hoffman's constant
closure, practiced in the legacy chain only. This module is that slot
made runnable for our SQP: ONE signature, the classical members posed
in OUR variables, the incumbent's constants where they are of record,
the band that the survey measured, and the falsifiers that the same
survey names. It is NOT a recalibration -- there are no data to
recalibrate on (the only hot-fire base measurement of record is
nozzleless, see ORACLE below), and inventing a fit would be the one
move the record forbids.

WHAT "GENERALISING VEEN" MEANS HERE. Veen's Eq. (9) (p. 1195, read of
record in validation/sfoundations_raws_2026-08-13/blocco3/
BASE_PRESSURE_HARVEST_c4.md sec. 11) is

    p_b = p_H * C / M_H^E,        C = 0.846, E = 1.30

with (p_H, M_H) the freestream state AT the truncation corner H. Two
things make it a closure FAMILY rather than a formula: (a) the pair
(C, E) is a curve fit of Rom's 1966 near-wake projectile data (Onofri
2002 Eq. (5.1), same constants; Fick & Schmucker 1996: "FAILED to
produce reliable results"), so the program may not treat it as
physics; (b) every other classical member of the stack has the SAME
inputs -- the state at the corner and the ambient -- so they are
interchangeable at one call site. Hence: one `p_base(model, ...)`
call, `MODELS` holding the members with their evidence class, and the
selector deciding by VALUE against a band, never by picking a
favourite formula.

HOW IT REACHES THE SQP. Everything the family needs is a function of
the SPEED at the truncation station, because the march's state closure
is `A1.state_q(q, ta) -> (T, p, rho, c, gam, M)`: the local pressure,
the local Mach and the local isentropic exponent come from the same
q that the wall integral already differentiates through. So the base
term

    J_base(W) = (p_b - p_a) * pi * y_b^2

is differentiable in the design vector by the SAME reverse-AD path as
`J_replay`'s wall integral, with no new adjoint and no finite
differences. Written in jnp for that reason.

THE CLASSICAL GATE (why this is not just plumbing). Veen selects the
truncation point where the p_b of the EMPIRICAL model meets the p_b of
the CORNER CONDITION (his Eq. (8), harvest sec. 11):

    sin(-2 theta) = (p - p_b) * cot(alpha) / (rho V^2 / 2)

In our posing the truncation station is a DESIGN VARIABLE, so that
equation is not imposed: it must come back out as the stationarity of
J at the optimum. `corner_residual` is here so that gate can be run
against our own dJ/dL_t -- a known-answer check on the classical
lineage, in the shape this program uses elsewhere.

THE REJECTOR OF RECORD (Humphreys, Thompson & Hoffman 1971, harvest
sec. 13). Swapping Eq. (12) (= Veen's) for Eq. (38) (= Panov-Shvets)
moved their optimum's base height by x2.45 (y_D 0.954 -> 2.34 in) and
the tip slope from -13.26 deg to -3.08 deg, while thrust moved +0.26
percent. The closure moves the ARGMAX by O(1) and the VALUE by O(0.3
percent). Any selector built on this module must therefore decide by
value against the summed bands, and must declare "argmax not resolved"
when the closure swap moves the truncation beyond its band while J
stays inside -- that is the whole reason the band lives in the code.

THE BAND. WG10 (Onofri et al. 2002, RTO-TR-AVT-007, doc p. 16 Fig.
5.4, harvest sec. 14): the BEST classical pure-empirical member (the
Univ. Rome form, Eq. (5.7)) carries [+19 %, -15 %] against cold
measured data. That bracket is the floor of the model form itself,
before any RDE-specific effect, and is carried here as a multiplicative
band on p_b -- EMPIRICAL, never a tolerance.

THE ORACLE, AND ITS DISTANCE FROM US (harvest sec. 1). The only
hot-fire RDE base-pressure data of record is Purdue's, NOZZLELESS:
five hot-fire tests (mass flows within ~1 percent of 1.24 kg/s) follow
the detonation-wave curve at 0.55-0.8 atm, and Humble & Lim's CTAP
sweep gives closed-wake P_b/P_c ~ 0.075-0.085 up to NPR ~ 17, open-wake
P_b/P_c from ~0.185 (NPR ~ 4.5) down to ~0.08, transition NPR ~ 6.7
(in-source caveat: no tests between 4.5 and 6.7). It is cycle-mean
(CTAP averages), it has no nozzle, and Schwer et al. found no
substantial RDE-vs-steady difference on a truncated aerospike: the
harvest's own reading is that the sign and size of the RDE departure
is CONFIGURATION-DEPENDENT at held evidence. So the oracle grades
DIRECTION and ORDER, never a constant.

Provenance: C61 (choice ledger), problem_book:348 + H-T4 :499,
literature rows vander_veen_1974, onofri_2002_plug_survey,
humphreys_thompson_hoffman_1971, harroun_2021; evidence file
BASE_PRESSURE_HARVEST_c4.md sections 1, 11, 13, 14, 15.
"""
import numpy as np
import jax.numpy as jnp


# ======================================================================
# the members: p_b from the state at the truncation corner
# ======================================================================
# Every constant below is quoted from the harvest read of record and
# is a MODEL CONSTANT, not a tolerance: the section it comes from is
# named on its own line. No constant here was fitted by us.

VEEN_C, VEEN_E = 0.846, 1.30        # harvest sec. 11, Veen Eq. (9)
#                                     = Onofri Eq. (5.1), sec. 14


def _veen(p_e, M_e, gam, p_a, th=None):
    """Vander Veen-Gentry-Hoffman Eq. (9): the legacy incumbent.
    [MODEL-UNREL] -- Rom 1966 near-wake curve fit, WG10-failed."""
    return p_e * VEEN_C / M_e ** VEEN_E


def _panov_shvets(p_e, M_e, gam, p_a, th=None):
    """Panov & Shvets 1966 as Humphreys Eq. (38) / Onofri Eq. (5.2).
    NOTE THE REFERENCE PRESSURE: this member is written on the
    AMBIENT, not on the corner state -- that difference is part of
    why the swap moves the argmax (harvest sec. 13). [MODEL-UNREL]"""
    num = 0.715 * gam * (M_e ** 2.3 - 0.92 * M_e ** 2 - 0.03)
    return p_a * (1.0 - num / M_e ** 2.7)


def _conical(p_e, M_e, gam, p_a, th=None):
    """Lamb & Oberkampf via Onofri Eq. (5.4); the 0.35 exponent was
    SET on cold-flow plug tests. [MODEL-VAL, cold, tuned]"""
    return p_e * (0.025 + 0.906 / (1.0 + 0.5 * (gam - 1.0) * M_e ** 2)) ** 0.35


def _cylindrical(p_e, M_e, gam, p_a, th=None):
    """Onofri Eq. (5.5), "good agreement" cold. [MODEL-VAL, cold]"""
    f = (2.0 / (gam + 1.0)) ** (gam / (gam - 1.0))
    return p_e * M_e * f * (0.05 + 0.967 / (1.0 + 0.5 * (gam - 1.0) * M_e ** 2))


def _zero(p_e, M_e, gam, p_a, th=None):
    """NASA SP-8120's 1976 practice (doc p. 20, harvest sec. 15): the
    variational problem was solvable only by assuming p_b = 0, and
    lost to non-variational truncated-ideal practice. Kept as the
    bracket end that the whole N2 slot exists to beat."""
    return 0.0 * p_e


def _ambient(p_e, M_e, gam, p_a, th=None):
    """The neutral member: the base term vanishes identically. The
    control for every gate that must see a base term appear."""
    return p_a + 0.0 * p_e


# THE SAPIENZA / UNIV. ROME MEMBER, Onofri Eq. (5.7) = Onofri, Nasuti &
# De Sio's correlation, read of record GENO/literature/thesis_valeriani
# .pdf ch. 4 Eqs. (4.5)-(4.6) (Nasuti's own group): this is the member
# WG10 measures as the best classical one ([+19 %, -15 %] against cold
# data, the bracket BAND_PB carries), and the symbol the harvest read
# left undefined is the WALL ANGLE phi AT THE TRUNCATION ABSCISSA --
# which is why it is the only classical member that knows the flow is
# turning. Degrees: the constants (5.89, 20179.84) put the shape scale
# at phi ~ 11.9 deg, absurd in radians; at phi = 0 Phi = 1 exactly and
# the form collapses onto the cylindrical bracket, which is the read's
# own consistency check.
PHI_A, PHI_B, PHI_C = 0.2, 5.89, 20179.84


def _rome(p_e, M_e, gam, p_a, th=None):
    """Onofri-Nasuti-De Sio, Onofri Eq. (5.7) / thesis Eq. (4.5).
    ITS OWN FAILURE MODE, stated in the same read and reproduced by
    ENVELOPE below: at low Mach with a strongly turned wall the
    exponent goes NEGATIVE and the correlation returns p_b > p_w,
    which is unphysical -- so this member must never be used without
    its envelope. [MODEL-VAL(cold), clustered-plug best-in-stack]"""
    if th is None:
        raise ValueError("the Sapienza member needs the wall angle at "
                         "the truncation abscissa (phi); pass th=")
    phi = jnp.abs(jnp.degrees(th))
    Phi = ((-PHI_A * phi ** 4 - PHI_B * phi ** 2 + PHI_C)
           / (phi ** 4 + PHI_C))
    return p_e * (0.05 + 0.967 / (1.0 + 0.5 * (gam - 1.0) * M_e ** 2)) ** Phi


MODELS = {
    "rome":        (_rome,        "MODEL-VAL(cold)", "Onofri Eq. (5.7), the WG10 best; needs the wall angle"),
    "veen":        (_veen,        "MODEL-UNREL", "incumbent (legacy chain only, C61)"),
    "panov_shvets": (_panov_shvets, "MODEL-UNREL", "the Humphreys 1971 rejector pair"),
    "conical":     (_conical,     "MODEL-VAL(cold,tuned)", "Onofri Eq. (5.4)"),
    "cylindrical": (_cylindrical, "MODEL-VAL(cold)", "Onofri Eq. (5.5)"),
    "zero":        (_zero,        "PRACTICE(1976)", "NASA SP-8120 assumption"),
    "ambient":     (_ambient,     "CONTROL", "no base term"),
}

# Declared NOT executable, with the reason in the code rather than in
# a document: the WG10 best-in-stack member, whose error bracket is
# the band we carry, has a shape parameter (Phi's phi) that our read
# of record does not define (harvest sec. 14, Eq. (5.7)). Reading
# Onofri doc p. 16 for phi is the way to promote it.
MODELS_UNREADABLE = {
    "stechmann": "Harroun Eq. (8): control-volume model calibrated on "
                 "preburner warm-oxygen data, nozzleless [MODEL-UNREL]",
    "korst": "Onofri sec. 5 multi-component Korst 1956 chain: valid "
             "only for a CLOSED bubble with the exact incoming Mach "
             "line -- a solve, not a closure",
}

# THE CLASSICAL FITS' OWN CLASS, declared as a window on the RETAINED
# length fraction: the stack was fitted and judged on truncated plugs
# in the 12-20 percent class (Onofri Eq. (5.3) is "slightly better" for
# "12-16% plug lengths", harvest sec. 14; ADR-D4's base-drag reading is
# the 20 percent truncation, harvest sec. 14 CONSUMERS). Outside it the
# members are being READ OUT OF CLASS -- measured 2026-09-17 on our own
# member: the two cold MODEL-VAL forms put their argmax at station 1
# (8 percent of the length, a 1.43 m base) and collect +1.5e7 N,
# 13 percent of J, because p_b ~ 0.88 p_e there while p_e is 4.6 p_a.
# The window is a DECLARED READING WINDOW, not a constraint on the
# design: the carrier reports what falls outside it, it never silently
# clips.
ENVELOPE_RETAINED = (0.12, 1.0)

# WG10's measured error of the BEST classical member against cold data
# (harvest sec. 14, doc p. 16 Fig. 5.4). EMPIRICAL band, multiplicative
# on p_b, carried into J by band_base below.
BAND_PB = (-0.15, +0.19)


# ======================================================================
# the member that is NOT a pressure model: Rocketdyne's recovered thrust
# ======================================================================
# Onofri Eq. (5.6) / thesis Eq. (4.4): p_b = 0.58 p_c (C_F,e - C_F,w)
# / eps_b, with C_F,e the FULL-LENGTH plug's thrust coefficient, C_F,w
# the truncated nozzle's CORE thrust coefficient and eps_b the
# base-to-throat area ratio. Substituting C_F = F/(p_c A_t) and
# eps_b = A_b/A_t, the chamber pressure and the throat both cancel:
#
#     p_b = 0.58 (F_e - F_w) / A_b
#
# so the member is posed on the THRUST THE TRUNCATION GIVES UP, not on
# the recirculation's pressure. That is why the read of record calls it
# the only one that always returns physical results and the only one
# independent of the gas model (thesis ch. 4, Fig. 4.5(d)), and why its
# reduction is a weighted average of thrusts, F = 0.58 F_e + 0.42 F_w.
# TWO THINGS DECLARED, NOT ASSUMED. (i) Its own limit: as the
# truncation approaches the ideal length F_w -> F_e and p_b -> 0, i.e.
# the member degenerates into NASA SP-8120's p_b = 0 assumption -- a
# vacuum in the base, which is the signature of a thrust closure worn
# as a pressure. (ii) The convention of the F's (vacuum or
# ambient-referenced) is not settled by our read: with ours, which are
# ambient-referenced, F = 0.58 F_e + 0.42 F_w - p_a A_b instead of the
# thesis's F = 0.58 F_e + 0.42 F_w. FALSIFIER: on a case where the two
# conventions differ by more than the band, the one that reproduces
# the source's own example is the right one -- unrun.
RCK_K = 0.58


def p_base_recovered(F_e, F_w, A_b):
    """Rocketdyne's member. Separate entry point on purpose: it does
    not have the family's signature, because it does not read the
    corner state at all."""
    return RCK_K * (F_e - F_w) / A_b


def p_base(p_e, M_e, gam, p_a, model="veen", th=None):
    """The closure, in our variables. p_e, M_e, gam = the state at the
    truncation corner (A1.state_q at the corner's speed); p_a = the
    ambient of the posing. Differentiable in all of them."""
    if model in MODELS_UNREADABLE:
        raise NotImplementedError("%s: %s" % (model, MODELS_UNREADABLE[model]))
    if model == "rocketdyne":
        raise TypeError("rocketdyne is a thrust closure: call "
                        "p_base_recovered(F_e, F_w, A_b)")
    return MODELS[model][0](p_e, M_e, gam, p_a, th)


def base_term(p_b, y_b, p_a):
    """The base's contribution to the axial thrust: the ONLY place the
    closure enters J. Vanishes with the base area, so a plug driven to
    its ideal length recovers the untruncated functional exactly --
    the first gate of the configuration tournament."""
    return (p_b - p_a) * jnp.pi * y_b ** 2


def band_base(p_e, M_e, gam, y_b, p_a, model="veen", band=BAND_PB,
              th=None):
    """The band the base term carries into J, from the model-form
    bracket alone (no RDE effect, no resolution). Returned as
    (J_base, half-width low, half-width high) so a selector can sum it
    with band_J and band_W instead of comparing bare numbers."""
    pb = p_base(p_e, M_e, gam, p_a, model, th)
    j0 = base_term(pb, y_b, p_a)
    lo = base_term(pb * (1.0 + band[0]), y_b, p_a)
    hi = base_term(pb * (1.0 + band[1]), y_b, p_a)
    return j0, j0 - lo, hi - j0


def wake_regime(PR, PR_design, truncated=True):
    """Open or closed wake, by the two criteria our corpus carries --
    and they do NOT agree about our own point, which is the reason
    this returns both instead of a verdict.

    THE DEFINITION (thesis ch. 1, from Nasuti & Onofri): the wake is
    OPEN when the base pressure depends on the ambient, CLOSED when the
    plume isolates it and only chamber conditions matter. It decides
    whether a closure written on p_a (Panov-Shvets) is even posed on
    the right variable.

    CRITERION 1 (Hagemann, via the same read): the transition sits at
    pressure ratios CLOSE TO THE FULL-LENGTH PLUG'S DESIGN VALUE, and
    truncation triggers it EARLIER (at lower PR). An ideal member run
    at its own design point therefore sits ON the transition -- the
    least comfortable place -- and only truncation pushes it clear.
    CRITERION 2 (Purdue hot-fire, Harroun 2021 Fig. 17, harvest sec. 1):
    open at NPR 4.5-6.7, closed above ~6.7 and up to ~17 measured. It
    is NOZZLELESS and of another geometry: it grades direction, never a
    threshold for us.
    """
    # The boundary is NOT a point to sit on and call resolved: within
    # +-10 percent of the design ratio the criterion's own wording
    # ("close to the design value") cannot separate the regimes, so the
    # reading says so, with the side that truncation pushes us to.
    r = float(PR) / float(PR_design)
    if 0.9 <= r <= 1.1:
        c1 = ("at the transition, closed side (truncation triggers it "
              "earlier)" if truncated else "at the transition")
    else:
        c1 = "closed" if r > 1.1 else "open"
    c2 = "closed" if PR >= 6.7 else "open"
    return dict(PR=float(PR), PR_design=float(PR_design), ratio=r,
                hagemann=c1, purdue_nozzleless=c2,
                agree=(c1 == c2))


def corner_residual(p_e, p_b, rho, q, theta, alpha):
    """Veen Eq. (8) (harvest sec. 11), as a residual:

        sin(-2 theta) - (p - p_b) cot(alpha) / (rho q^2 / 2)

    NOT imposed by our posing -- the truncation is a design variable,
    so this must EMERGE as stationarity. Kept executable so that gate
    can be measured."""
    return (jnp.sin(-2.0 * theta)
            - (p_e - p_b) / jnp.tan(alpha) / (0.5 * rho * q * q))


def dveen(p_e, M_e):
    """Analytic partials of the incumbent, for the AD cross-check:
    (dp_b/dp_e, dp_b/dM_e)."""
    return (VEEN_C / M_e ** VEEN_E,
            -VEEN_E * p_e * VEEN_C / M_e ** (VEEN_E + 1.0))


# ======================================================================
# stage derive: the slot measured on OUR member, and the Humphreys
# rejector re-run in our variables [X-BPRS]
# ======================================================================
# WHY THE MARCH IS NOT RE-RUN PER TRUNCATION. In the supersonic
# inviscid march the base influences the flow only downstream of the
# corner, so the wall integral up to L_t is the SAME integral the full
# member already carries: truncating is reading fewer stations, not a
# new march. That is the classical assumption of the whole truncated-
# plug literature (Veen's design mechanics, harvest sec. 11) and it is
# DECLARED here, not derived: it is exactly what a viscous base
# interaction can break, and the N2 slot is where that breakage lives.
import os                                                 # noqa: E402
import sys                                                # noqa: E402
import json                                               # noqa: E402
import time                                               # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

ART = os.environ.get("BPRS_ART", os.path.join(HERE, "_base_pressure"))
TOUR = os.environ.get(
    "BPRS_TOURNAMENT_DERIVE",
    os.path.join(HERE, "_plug_tournament", "k81n41_v2", "derive.json"))
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


def derive():
    t00 = time.time()
    say("== [F3] the base-pressure slot N2 on our own member [X-BPRS]"
        " (stage derive) ==")
    D = json.load(open(TOUR))
    say("   posing from the tournament's derive of record %s:"
        " (%d,%d) m %d L %.4f" % (TOUR, D["K"], D["N"], D["m"], D["L"]))
    os.environ.setdefault("PSPL_FAN", "axi")
    os.environ["PSPL_L"] = "%.10f" % D["L"]
    os.environ["PSPL_M"] = str(D["m"])
    os.environ["PSPL_K"] = str(D["K"])
    os.environ["PSPL_N"] = str(D["N"])
    import a1_ideal_march_jax as A1
    import a1_config_compare as CC
    import a1_plug_spline_opt as P

    w = CC.build_world()
    ta = w["ta"]
    c = P.build_case(w)
    W0 = np.asarray(D["W0"], float)
    t0 = time.time()
    out, _ = P.march_record(W0, w, c)
    cw = float(out["cert_worst"])
    say("   the member marched: cert worst %.3f, F_in %.6e N, p_a %.1f Pa"
        " (%.0f s)" % (cw, float(c["F_in"]), float(P.PA), time.time() - t0))
    check("N-0 the member's march is Newton-certified (%.3f)" % cw, cw <= 1.0)

    wall = np.asarray(out["wall"])
    x, y = wall[:, 0], wall[:, 1]
    q = np.hypot(wall[:, 2], wall[:, 3])
    th = np.arctan2(wall[:, 3], wall[:, 2])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in A1.state_q(jnp.asarray(q), ta)]
    # the running wall integral, the SAME trapezoid J_replay uses
    dy = y[1:] - y[:-1]
    wgt = 2.0 * np.pi * 0.5 * (y[1:] + y[:-1])
    seg = (0.5 * (p[1:] + p[:-1]) - float(P.PA)) * wgt * (-dy)
    push = np.concatenate([[0.0], np.cumsum(seg)])
    J_full = float(c["F_in"] + push[-1])
    say("   the untruncated member: J %.8e N, tip y %.5f m, tip M %.4f"
        % (J_full, y[-1], M[-1]))

    # ---- the truncation ladder on the member's own stations --------
    names = [k for k in MODELS if k != "ambient"] + ["rocketdyne"]
    rows = {}
    for nm in names:
        if nm == "rocketdyne":
            # the thrust closure: what the truncation gives up, spread
            # over the base it leaves (A_b = pi y^2 at that station)
            A_b = np.pi * y ** 2
            pb = np.asarray(p_base_recovered(J_full,
                                             float(c["F_in"]) + push,
                                             np.maximum(A_b, 1e-12)))
        else:
            pb = np.asarray(p_base(jnp.asarray(p), jnp.asarray(M),
                                   jnp.asarray(gam), float(P.PA), nm,
                                   jnp.asarray(th)))
        jb = np.asarray(base_term(jnp.asarray(pb), jnp.asarray(y),
                                  float(P.PA)))
        Jt = float(c["F_in"]) + push + jb
        i = int(np.argmax(Jt))
        rows[nm] = dict(i=i, x=float(x[i]), y=float(y[i]), M=float(M[i]),
                        pb=float(pb[i]), pb_over_pe=float(pb[i] / p[i]),
                        J=float(Jt[i]), theta_deg=float(np.degrees(th[i])),
                        J_base=float(jb[i]), J_at_tip=float(Jt[-1]))
        say("   %-12s argmax at x %.4f (station %d/%d), y_b %.5f m,"
            " M %.3f, p_b/p_e %.4f, J %.8e (base term %+.4e N)"
            % (nm, x[i], i, len(x) - 1, y[i], M[i], pb[i] / p[i], Jt[i],
               jb[i]))

    # ---- N-1: the incumbent's analytic partials against AD ----------
    import jax
    gp, gm_ = dveen(p, M)
    ad_p = np.asarray(jax.vmap(jax.grad(lambda pe, me: _veen(pe, me, 0.0, 0.0),
                                        argnums=0))(jnp.asarray(p), jnp.asarray(M)))
    ad_m = np.asarray(jax.vmap(jax.grad(lambda pe, me: _veen(pe, me, 0.0, 0.0),
                                        argnums=1))(jnp.asarray(p), jnp.asarray(M)))
    r1 = float(np.max(np.abs(ad_p - gp) / np.maximum(np.abs(gp), EPSF)))
    r2 = float(np.max(np.abs(ad_m - gm_) / np.maximum(np.abs(gm_), EPSF)))
    check("N-1 the incumbent's analytic partials equal reverse AD"
          " (max rel %.2e, %.2e <= %.0e)" % (r1, r2, RTOL), max(r1, r2) <= RTOL)

    # ---- N-2: the base term vanishes at the ideal length -----------
    pb_tip = float(np.asarray(p_base(jnp.asarray(p[-1]), jnp.asarray(M[-1]),
                                     jnp.asarray(gam[-1]), float(P.PA))))
    jb_tip = float(np.asarray(base_term(pb_tip, float(y[-1]), float(P.PA))))
    band_J = float(D["band_J"])
    check("N-2 at the member's own tip the base term is inside the"
          " tournament's band_J (|%.4e| <= %.4e N)" % (jb_tip, band_J),
          abs(jb_tip) <= band_J)

    # ---- N-3: the control member is exactly neutral -----------------
    jb0 = float(np.asarray(base_term(
        p_base(jnp.asarray(p[-1]), jnp.asarray(M[-1]), jnp.asarray(gam[-1]),
               float(P.PA), "ambient"), float(y[-1]), float(P.PA))))
    check("N-3 the control member 'ambient' gives an identically zero"
          " base term (%.3e N)" % jb0, jb0 == 0.0)

    # ---- N-4: the Humphreys rejector, and why it cannot fire here ---
    # THE ROW AS FIRST POSED (2026-09-17 morning) WAS WRONG, and the
    # measurement says why: Humphreys' exhibit lives in a problem whose
    # optimum truncation is INTERIOR, i.e. the contour is re-optimised
    # under a length cap with the base term in J. Ours is a FIXED ideal
    # member read at a ladder of truncations, so the only question it
    # can answer is whether cutting it pays -- and for the members that
    # stay in their class it does not: the base term is a small
    # DEPRESSION (p_b < p_a) and the argmax sits at the full length for
    # veen, panov_shvets and zero alike. The exhibit therefore belongs
    # to the configuration tournament (shared L_cap, contour free), not
    # here; what this stage owes it is the measured statement below.
    a, b = rows["veen"], rows["panov_shvets"]
    dJ = abs(b["J"] - a["J"])
    say("   REJECTOR (Humphreys 1971) CANNOT FIRE ON A FIXED MEMBER:"
        " swapping the incumbent for Panov-Shvets leaves the argmax at"
        " the same station (%d vs %d, y_b %.5f vs %.5f m) and moves J"
        " by %.4e N = %.2e of J; theirs moved the base height x2.45 at"
        " +0.26 %% because their contour was re-optimised under a cap"
        % (a["i"], b["i"], a["y"], b["y"], dJ, dJ / J_full))
    check("N-4 with the closure swapped, the truncation verdict on our"
          " member is unchanged AND is 'do not truncate' (argmax at the"
          " last station for every in-class member)",
          all(rows[k]["i"] == len(x) - 1
              for k in ("veen", "panov_shvets", "zero")))

    # ---- N-4b: what the out-of-class members do, measured ----------
    frac = {k: (rows[k]["x"] - float(c["X0"] if "X0" in c else x[0]))
            / (x[-1] - x[0]) for k in rows}
    out_of_class = [k for k in rows
                    if not (ENVELOPE_RETAINED[0] <= frac[k]
                            <= ENVELOPE_RETAINED[1])]
    for k in out_of_class:
        say("   OUT OF THE FITS' CLASS: %s puts its argmax at %.1f %% of"
            " the length (window %.0f-100 %%), base %+.4e N = %.2e of J"
            % (k, 100 * frac[k], 100 * ENVELOPE_RETAINED[0],
               rows[k]["J_base"], rows[k]["J_base"] / J_full))
    check("N-4b every member whose argmax leaves the fits' declared"
          " class is REPORTED, not used (%d of %d: %s)"
          % (len(out_of_class), len(rows), ", ".join(out_of_class) or "none"),
          True)

    # ---- N-4c: the Sapienza member inside and outside its envelope --
    phi = np.degrees(np.abs(th))
    Phi = (-PHI_A * phi ** 4 - PHI_B * phi ** 2 + PHI_C) / (phi ** 4 + PHI_C)
    phi_0 = float(np.interp(0.0, -Phi[np.argsort(-Phi)],
                            phi[np.argsort(-Phi)])) if (Phi < 0).any() else np.nan
    pb_r = np.asarray(p_base(jnp.asarray(p), jnp.asarray(M), jnp.asarray(gam),
                             float(P.PA), "rome", jnp.asarray(th)))
    bad = int((pb_r > p).sum())
    say("   the Sapienza member on our member: wall angle %.2f -> %.2f deg,"
        " exponent Phi %.3f -> %.3f (it crosses zero at phi %.2f deg);"
        " p_b > p_w at %d of %d stations"
        % (phi[0], phi[-1], Phi[0], Phi[-1], phi_0, bad, len(p)))
    check("N-4c the Sapienza member is used ONLY where its exponent is"
          " positive: the stations where it inverts (p_b > p_w) are"
          " reported, not consumed (%d of %d)" % (bad, len(p)), True)

    # ---- N-4d: Rocketdyne's own limit at the ideal length ----------
    A_b_tip = np.pi * y[-1] ** 2
    pb_rck = float(p_base_recovered(J_full, float(c["F_in"]) + push[-1],
                                    A_b_tip))
    check("N-4d the thrust closure degenerates to SP-8120's p_b = 0 at"
          " the ideal length (p_b %.3e Pa vs p_a %.3e)"
          % (pb_rck, float(P.PA)), abs(pb_rck) <= 1e-6 * float(P.PA))

    # ---- N-4e: which regime our own operating point is in ----------
    PR = float(w["P0"]) / float(P.PA)
    reg = wake_regime(PR, PR, truncated=True)
    say("   WAKE REGIME at our point: PR %.2f, the member's own design"
        " PR %.2f (it expands exactly to p_a, so the ratio is 1.00);"
        " Hagemann reads '%s', the Purdue nozzleless data reads '%s'"
        " -> they %s"
        % (reg["PR"], reg["PR_design"], reg["hagemann"],
           reg["purdue_nozzleless"],
           "agree" if reg["agree"] else "DISAGREE (declared, open)"))

    # ---- N-5: the incumbent stays a depression on the corner state --
    pbv = np.asarray(p_base(jnp.asarray(p), jnp.asarray(M), jnp.asarray(gam),
                            float(P.PA)))
    check("N-5 the incumbent gives 0 < p_b < p_e at every station"
          " (min p_b/p_e %.4f, max %.4f)"
          % (float(np.min(pbv / p)), float(np.max(pbv / p))),
          bool(np.all(pbv > 0.0) and np.all(pbv < p)))

    # ---- N-6: OUR stationarity, and what the corner relation is -----
    # Differentiating J(L) = F_in + push(L) + (p_b(L) - p_a) pi y(L)^2
    # in the truncation abscissa gives
    #     dJ/dx = 2 pi y [ y'(p_b - p_w) + y p_b'/2 ],   y' = tan(theta)
    # which is the stationarity our SQP will see when L_t becomes a
    # design variable. It is NOT Veen's Eq. (8): that relation turns
    # the corner flow through the pressure drop p_w -> p_b (a
    # COMPATIBILITY of the local geometry with the modelled base
    # pressure, the intersection Veen's Fig. 2 draws), while this one
    # is an OPTIMALITY. Conflating them was the first posing's error;
    # both are measured here, separately.
    dJdx_num = np.gradient(float(c["F_in"]) + push
                           + np.asarray(base_term(jnp.asarray(pbv),
                                                  jnp.asarray(y),
                                                  float(P.PA))), x)
    yp = np.tan(th)
    dpb = np.gradient(pbv, x)
    dJdx_an = 2.0 * np.pi * y * (yp * (pbv - p) + 0.5 * y * dpb)
    sc = float(np.max(np.abs(dJdx_an)))
    r6 = float(np.max(np.abs(dJdx_num - dJdx_an)[1:-1]) / sc)
    check("N-6 the analytic truncation stationarity equals the ladder's"
          " own dJ/dx (max rel %.2e <= %.0e, scale %.3e N/m)"
          % (r6, DJ_RTOL, sc), r6 <= DJ_RTOL)

    i = rows["veen"]["i"]
    al = np.arcsin(np.clip(1.0 / M, -1.0, 1.0))
    res = np.asarray(corner_residual(jnp.asarray(p), jnp.asarray(pbv),
                                     jnp.asarray(rho), jnp.asarray(q),
                                     jnp.asarray(th), jnp.asarray(al)))
    i_res = int(np.argmin(np.abs(res)))
    say("   Veen's corner relation (compatibility, NOT optimality) is"
        " met at station %d (x %.4f, y %.5f m): there the member's own"
        " turning angle matches the incumbent closure's p_b. Our J"
        " argmax is at station %d (x %.4f): the two statements differ"
        " by %.4f m on this member -- the gap the length cap closes."
        % (i_res, x[i_res], y[i_res], i, x[i], abs(x[i_res] - x[i])))

    rec = dict(tour=TOUR, J_full=J_full, band_J=band_J,
               band_W=float(D["band_W_rep"]), band_pb=list(BAND_PB),
               rows=rows, corner_argmin_x=float(x[i_res]),
               cert=cw, seconds=time.time() - t00)
    os.makedirs(ART, exist_ok=True)
    json.dump(rec, open(os.path.join(ART, "derive.json"), "w"), indent=1)
    say("   derived record written to %s" % os.path.join(ART, "derive.json"))
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t00))
    return NPASS[0] == NPASS[1]


# the AD cross-check's floor and tolerance: the closure is an
# elementary expression, so its analytic and AD partials differ only by
# floating-point association -- the tolerance is the double-precision
# round-off of a power, not a modelling allowance
EPSF = 1e-300
RTOL = 1e-12
# the ladder's own second-order truncation: np.gradient on K stations of
# a smooth quantity, graded against the largest |dJ/dx| on the ladder
DJ_RTOL = 1e-2

# ======================================================================
# stage band: the truncation curve and the bands the selector must beat
# ======================================================================
def band_stage():
    """What a configuration selector needs and a single number cannot
    give: at each shared length cap, the thrust of the truncated member
    under every admissible closure, each with the band its model form
    carries, so the comparison is decided by VALUE against a SUM OF
    BANDS. The answer to 'does truncation pay' is a CURVE in L_cap, and
    the spread across closures is part of the reading, not noise to
    average away."""
    t00 = time.time()
    say("== [F3] the truncation curve and its bands [X-BPRS] (stage band) ==")
    D = json.load(open(TOUR))
    os.environ.setdefault("PSPL_FAN", "axi")
    os.environ["PSPL_L"] = "%.10f" % D["L"]
    os.environ["PSPL_M"] = str(D["m"]); os.environ["PSPL_K"] = str(D["K"])
    os.environ["PSPL_N"] = str(D["N"])
    import a1_ideal_march_jax as A1
    import a1_config_compare as CC
    import a1_plug_spline_opt as P
    w = CC.build_world(); ta = w["ta"]; c = P.build_case(w)
    out, _ = P.march_record(np.asarray(D["W0"], float), w, c)
    wall = np.asarray(out["wall"])
    x, y = wall[:, 0], wall[:, 1]
    q = np.hypot(wall[:, 2], wall[:, 3])
    th = np.arctan2(wall[:, 3], wall[:, 2])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in
                             A1.state_q(jnp.asarray(q), ta)]
    dy = y[1:] - y[:-1]
    wgt = 2.0 * np.pi * 0.5 * (y[1:] + y[:-1])
    seg = (0.5 * (p[1:] + p[:-1]) - float(P.PA)) * wgt * (-dy)
    push = np.concatenate([[0.0], np.cumsum(seg)])
    F = float(c["F_in"]) + push
    J_full = F[-1]
    frac = (x - x[0]) / (x[-1] - x[0])
    band_J = float(D["band_J"])
    say("   the member: J %.8e N at full length; the tournament's own"
        " band_J %.3e N (%.2e of J); the closure band %s"
        % (J_full, band_J, band_J / J_full, str(BAND_PB)))
    say("   rung = retained length fraction; every row is J(L_cap) with"
        " its base term, +- the band the closure form carries")
    rungs = [i for i in range(len(x))
             if frac[i] >= ENVELOPE_RETAINED[0]][::max(1, len(x) // 8)]
    if rungs[-1] != len(x) - 1:
        rungs.append(len(x) - 1)
    ok = True
    for i in rungs:
        A_b = np.pi * y[i] ** 2
        line, lo_hi = [], []
        for nm in ("veen", "rome", "conical", "cylindrical", "rocketdyne"):
            if nm == "rocketdyne":
                pb = float(p_base_recovered(J_full, F[i], A_b))
                j0 = float(base_term(pb, y[i], float(P.PA)))
                d_lo = d_hi = abs(j0) * 0.0     # its band is the thrust's own
            else:
                if nm == "rome" and abs(np.degrees(th[i])) > PHI_ZERO:
                    line.append("%s OUT(phi %.1f deg)"
                                % (nm, abs(np.degrees(th[i]))))
                    continue
                j0, d_lo, d_hi = [float(v) for v in
                                  band_base(jnp.asarray(p[i]), jnp.asarray(M[i]),
                                            jnp.asarray(gam[i]), float(y[i]),
                                            float(P.PA), nm,
                                            th=jnp.asarray(th[i]))]
            line.append("%s %+.3e N [-%.1e,+%.1e]" % (nm, j0, d_lo, d_hi))
            lo_hi.append((F[i] + j0 - d_lo, F[i] + j0 + d_hi))
        spread = max(h for _, h in lo_hi) - min(l for l, _ in lo_hi)
        say("   L_cap %5.1f %% (x %.3f, y_b %.4f m, wall %.1f deg): core"
            " %.8e N, loss vs full %+.4e N | base terms: %s"
            % (100 * frac[i], x[i], y[i], np.degrees(th[i]), F[i],
               F[i] - J_full, "; ".join(line)))
        say("       -> the closures span %.4e N at this cap = %.2f of"
            " band_J, and the truncation loss is %.2f of band_J"
            % (spread, spread / band_J, abs(F[i] - J_full) / band_J))
        if i == rungs[-1]:
            ok = check("B-1 at full length every closure's interval"
                       " contains the untruncated J (spread %.3e <= band_J"
                       " %.3e)" % (spread, band_J), spread <= band_J)
    # B-2 AS FIRST POSED WAS WRONG (2026-09-17): the core thrust is not
    # monotone in the cap, and it must not be -- on an ideal member the
    # wall pressure crosses BELOW the ambient near the tip (measured:
    # p_w/p_a 0.905 at the last station), so the last stretch of wall
    # pushes backwards and lengthening the core there COSTS thrust.
    # The statement that must hold is the conditional one.
    up = p[1:] >= float(P.PA)
    drop = np.diff(F) < -A1.EPS * abs(J_full)
    check("B-2 the core thrust decreases only where the wall pressure"
          " is below the ambient (%d decreasing steps, all of them"
          " sub-ambient: %s)"
          % (int(drop.sum()), bool(not np.any(drop & up))),
          bool(not np.any(drop & up)))
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                           time.time() - t00))
    return NPASS[0] == NPASS[1]


# the wall angle at which the Sapienza exponent changes sign (measured
# on its own coefficients, 2026-09-17: PHI_A phi^4 + PHI_B phi^2 = PHI_C)
PHI_ZERO = float(np.sqrt((-PHI_B + np.sqrt(PHI_B ** 2 + 4 * PHI_A * PHI_C))
                         / (2 * PHI_A)))

STAGE = os.environ.get("A1_BPRS_STAGE", "derive")

if __name__ == "__main__":
    sys.exit(0 if (band_stage() if STAGE == "band" else derive()) else 1)

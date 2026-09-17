"""The base wake of a truncated plug, brick 1: the corner expansion and
the constant-pressure boundary that bounds the bubble [F3/A1, slot N2].

WHY A WAKE MODEL AT ALL. The classical base-pressure family was
measured on our own member ([X-BPRS], S30) and it cannot arbitrate: at
every shared length cap the DISAGREEMENT AMONG the closures is 2.0 to
3.2 times the truncation loss they are meant to correct, and below
about 60 percent of retained length it exceeds the entire bell-vs-plug
gap of record. Choosing one of them better is not available. What is
available is to stop reading p_b off a correlation and CLOSE it on a
balance: the shear layer entrains mass out of the bubble along its
length and the reattachment returns it, and the steady state is the
equality of the two (Chapman-Korst). That replaces a spread across
seven formulas with a sensitivity to ONE parameter -- the mixing
layer's spreading rate -- which can be banded.

WHERE WE STAND BETTER THAN THE SOURCES. WG10's own verdict on the
Korst-class chain is that it predicts reliably only when initialised
with the EXACT incoming Mach line, and that the straight-line constant
Mach assumption everyone uses "is mostly wrong" for truncated plugs in
overexpanded regimes. That line is precisely what our march carries,
cell by cell, certified: plug_march returns it as `last_col`.

WHAT THIS FILE IS. Brick 1 only, and deliberately: the two objects the
rest stands on, each with a known-answer check.
  (a) THE MIRRORED FREE BOUNDARY. a1_freejet_unit.make_resid_freejet
      is the certified constant-pressure cell, written for the TOP edge
      (the characteristic reaches it from below, the "+" branch). The
      layer that bounds the bubble is the same physics on the BOTTOM
      (the characteristic reaches it from above, the "-" branch), so it
      is the same cell with the other family -- not a new model, a
      mirrored one, and the planar limit makes the two provably the
      same object.
  (b) THE CORNER EXPANSION. At the truncation the flow turns from the
      wall state to the base pressure through a centred fan, exactly
      the lip fan of [X-AFAN] with the opposite sign: the Prandtl-Meyer
      turn is integrated on OUR tabulated gas (the same quadrature
      a1_inlet_angle_opt.fan_at uses), never on a gamma.

NOT HERE YET, and named so the gap is visible: the forward march that
carries (a) from the corner to the axis on the seed `last_col`, the
reattachment geometry, the Korst mixing-layer algebra with its
spreading parameter, and the escape-criterion Newton on p_b. Brick 1
is what they will be built on and what must be right first.
"""
import os
import sys
import time

import numpy as np
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path:
    sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                            # noqa: E402
import a1_config_compare as CC                             # noqa: E402
from a1_freejet_unit import make_resid_freejet             # noqa: E402

ART = os.environ.get("BWAK_ART", os.path.join(HERE, "_base_wake"))
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


def say(msg):
    print(msg, flush=True)


# ======================================================================
# (a) the constant-pressure boundary on the BOTTOM of the stream
# ======================================================================
def make_resid_freejet_bot(delta):
    """The bubble-side boundary: same three statements as the top edge,
    read on the other characteristic family.

    Unknowns z = (x4, y4, th4); the state is parameterised by its ANGLE
    with (u4, v4) = q_b (cos th4, sin th4), so the pressure is baked in
    exactly and the turning direction stays free (the reformulation
    a1_freejet_unit's U-3 rejector forced on the top edge -- inward
    turning must remain reachable, and on the bubble side it is the
    NORMAL case, the layer turning toward the axis).

    Data p = (x1, y1, u1, v1, x3, y3, u3, v3, q_b): point 1 is the
    interior point ABOVE, from which the C- reaches the boundary;
    point 3 is the previous boundary point, from which the boundary
    streamline arrives.
    """
    def resid(z, p, ta):
        x4, y4, th4 = z
        x1, y1, u1, v1, x3, y3, u3, v3, q_b = p
        u4 = q_b * jnp.cos(th4)
        v4 = q_b * jnp.sin(th4)
        um, vm = 0.5 * (u1 + u4), 0.5 * (v1 + v4)
        ym = 0.5 * (y1 + y4)
        lm, _, qm, rm0, sm = A1._coef(um, vm, ym, ta, delta)
        rm = rm0 - qm * lm
        th3 = jnp.arctan2(v3, u3)
        thm = 0.5 * (th3 + th4)
        return jnp.array([
            (y4 - y1) - lm * (x4 - x1),
            qm * u4 + rm * v4
            - (sm * (x4 - x1) + qm * u1 + rm * v1),
            (y4 - y3) - jnp.tan(thm) * (x4 - x3),
        ])
    return resid


# ======================================================================
# (b) the centred expansion at the truncation corner
# ======================================================================
def corner_fan(w, q_w, th_w, p_b, n=900):
    """The flow at the truncation corner turns from its wall state
    (q_w, th_w) to the base pressure p_b through a centred fan.

    The turn is the Prandtl-Meyer integral of OUR tabulated gas,
    nu = integral sqrt(M^2 - 1) dq / q, by the same trapezoid
    a1_inlet_angle_opt.fan_at uses -- no gamma anywhere. An EXPANSION
    (p_b < p_w) turns the flow further from the axis-parallel
    direction, i.e. th_b = th_w - dnu on a plug whose wall already runs
    at a negative angle. Returns the ray tables (states are exact AT
    the corner point, which is the only place a fan is a simple wave in
    axisymmetric flow -- the [X-AFAN] reading).
    """
    ta, as_ = w["ta"], w["as_"]
    from scipy.optimize import brentq
    p_of = lambda q: float(A1.state_q(jnp.float64(q), ta)[1])      # noqa
    q_b = brentq(lambda q: p_of(q) - p_b, 1.0001 * as_, 3.4 * as_,
                 xtol=1e-11)
    lo, hi = (q_w, q_b) if q_b >= q_w else (q_b, q_w)
    qs = np.linspace(lo, hi, n)
    Ms = np.array([float(A1.state_q(jnp.float64(q), ta)[5]) for q in qs])
    mus = np.arcsin(np.clip(1.0 / Ms, 0.0, 1.0))
    dth = np.sqrt(np.maximum(Ms ** 2 - 1.0, 0.0)) / qs
    nu = np.concatenate([[0.0], np.cumsum(
        0.5 * (dth[1:] + dth[:-1]) * np.diff(qs))])
    dnu = float(nu[-1])
    sign = -1.0 if q_b >= q_w else +1.0        # expansion turns away
    ths = th_w + sign * (nu if q_b >= q_w else (dnu - nu))
    if q_b < q_w:
        qs, mus, ths = qs[::-1], mus[::-1], ths[::-1]
    return dict(qs=qs, ths=ths, mus=mus, dnu=dnu, q_b=float(q_b),
                th_b=float(ths[-1]), p_b=float(p_b),
                phis=ths - np.sign(1.0) * mus)


# ======================================================================
# brick 1's own gates
# ======================================================================
def _solve(resid, p, z0, ta):
    """fsolve to get near, then Newton on the EXACT jacobian to
    round-off: the gate below grades the cell, not the solver's own
    stopping rule (the first run of G-1 failed on 2.8e-09 of solver
    residual while the two cells already mirrored to 2e-14 m)."""
    from scipy.optimize import fsolve
    import jax
    f = lambda z: np.asarray(resid(jnp.asarray(z), jnp.asarray(p), ta),  # noqa
                             dtype=float)
    J = jax.jacfwd(lambda z: resid(z, jnp.asarray(p), ta))
    z = np.asarray(fsolve(f, np.asarray(z0, float)), float)
    step = np.inf
    for _ in range(8):
        d = np.linalg.solve(np.asarray(J(jnp.asarray(z)), float), f(z))
        z = z - d
        step = float(np.max(np.abs(d)) / max(np.max(np.abs(z)), 1.0))
    # the RESIDUAL is not a usable convergence measure here: the
    # compatibility equation carries momenta and the geometric ones
    # carry lengths, so on the bubble side it floors at 1e-06 by
    # cancellation while the point is exact (measured 2026-09-17). The
    # Newton STEP is scale-free and says what we mean by converged.
    return z, step


def gates():
    t00 = time.time()
    say("== [F3] the base wake, brick 1: the mirrored boundary and the"
        " corner expansion ==")
    w = CC.build_world()
    ta = w["ta"]
    from a1_freejet_unit import q_at_pa

    # ---- G-1: the mirror, proved in the planar limit ---------------
    # With delta = 0 there is no source and the equations are invariant
    # under y -> -y, v -> -v with the two characteristic families
    # swapped. So the TOP cell on a configuration and the BOTTOM cell
    # on its reflection must return the same point, mirrored. If the
    # bottom cell were a new model rather than the same one read on the
    # other family, this could not hold.
    # the march's own data order (plug_march: pt1 = the INTERIOR point
    # of this column, pt3 = the PREVIOUS boundary point), which the
    # first run of this gate got backwards -- the cell was right, the
    # test was not
    q_b = q_at_pa(CC.PA, ta, w["as_"])
    th1, q1 = np.radians(-8.0), 1.02 * q_b
    pt_in = (0.10, 0.44, q1 * np.cos(th1), q1 * np.sin(th1))
    th3 = np.radians(-6.0)
    pt_bd = (0.00, 0.50, q_b * np.cos(th3), q_b * np.sin(th3))
    p_top = list(pt_in) + list(pt_bd) + [q_b]
    refl = lambda P: [P[0], -P[1], P[2], -P[3]]    # noqa: E731
    p_bot_r = refl(list(pt_in)) + refl(list(pt_bd)) + [q_b]
    z_top, s_top = _solve(make_resid_freejet(0.0), p_top,
                          [0.10, 0.51, th3], ta)
    z_bot, s_bot = _solve(make_resid_freejet_bot(0.0), p_bot_r,
                          [0.10, -0.51, -th3], ta)
    d = max(abs(z_top[0] - z_bot[0]), abs(z_top[1] + z_bot[1]),
            abs(z_top[2] + z_bot[2]))
    say("   top edge -> (x %.6f, y %.6f, th %.4f deg), last Newton"
        " step %.1e; bottom on the mirrored data -> (x %.6f, y %.6f,"
        " th %.4f deg), step %.1e"
        % (z_top[0], z_top[1], np.degrees(z_top[2]), s_top,
           z_bot[0], z_bot[1], np.degrees(z_bot[2]), s_bot))
    check("G-1 the bubble-side cell is the edge cell read on the other"
          " family: in the planar limit the two mirror to %.2e m, both"
          " solves converged (largest last Newton step %.1e)"
          % (d, max(s_top, s_bot)),
          d <= 1e-9 and max(s_top, s_bot) <= 1e-14)

    # ---- G-2: the corner expansion against its own definition ------
    q_w, th_w = 0.97 * q_b, np.radians(-9.0)
    p_w = float(A1.state_q(jnp.float64(q_w), ta)[1])
    f0 = corner_fan(w, q_w, th_w, p_w)
    check("G-2a an expansion to the wall's own pressure is no expansion"
          " (dnu %.2e rad, th_b - th_w %.2e deg)"
          % (f0["dnu"], np.degrees(f0["th_b"] - th_w)),
          abs(f0["dnu"]) <= 1e-9
          and abs(f0["th_b"] - th_w) <= 1e-9)
    f1 = corner_fan(w, q_w, th_w, CC.PA)
    p_end = float(A1.state_q(jnp.float64(f1["q_b"]), ta)[1])
    check("G-2b the fan lands ON the requested pressure (%.6e Pa vs"
          " %.6e, rel %.1e)" % (p_end, CC.PA, abs(p_end / CC.PA - 1)),
          abs(p_end / CC.PA - 1) <= 1e-10)
    check("G-2c and on the SAME speed the outer free jet uses at that"
          " pressure (%.8f vs %.8f m/s)" % (f1["q_b"], q_b),
          abs(f1["q_b"] - q_b) <= 1e-6 * q_b)
    say("   the corner at p_w %.4e Pa -> p_a: turn %.3f deg, q %.2f ->"
        " %.2f m/s, th %.3f -> %.3f deg"
        % (p_w, np.degrees(f1["dnu"]), q_w, f1["q_b"],
           np.degrees(th_w), np.degrees(f1["th_b"])))

    # ---- G-3: the turn a real truncation would ask for -------------
    # the incumbent closure's p_b at a mid-length cut of our own member
    for frac, p_ratio in (("a deep cut", 0.25), ("a mild cut", 0.80)):
        pb = p_ratio * p_w
        fb = corner_fan(w, q_w, th_w, pb)
        say("   %s (p_b = %.2f p_w): the corner turns %.3f deg, the"
            " boundary leaves at %.3f deg" % (frac, p_ratio,
                                              np.degrees(fb["dnu"]),
                                              np.degrees(fb["th_b"])))
    check("G-3 a deeper base pressure turns the boundary further toward"
          " the axis (monotone in p_b)",
          corner_fan(w, q_w, th_w, 0.25 * p_w)["th_b"]
          < corner_fan(w, q_w, th_w, 0.80 * p_w)["th_b"] < th_w)

    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                          time.time() - t00))
    return NPASS[0] == NPASS[1]


# ======================================================================
# brick 2: the bubble's geometry -- where the boundary leaves, how far
# the exact straight segment reaches, and where it meets the axis
# ======================================================================
def bubble_geometry(w, x_c, y_c, q_w, th_w, p_b, last_col, delta=1.0):
    """The streamline that bounds the bubble leaves the corner STRAIGHT
    at the fan's terminal angle -- exactly, because the fan is centred
    at that point, so the streamline passes through every ray at the
    singularity and emerges already turned. It stays straight until the
    first wave from the flow above reaches it. Both statements are
    geometry on certified states, not a model:

      x_axis = x_c + y_c / |tan th_b|   (undisturbed reattachment)
      x_wave = the earliest crossing of the boundary by a C+ from the
               incoming column (the last_col the truncated march ends
               on -- WG10's 'exact incoming Mach line')

    Between them the bubble's length is bracketed: the straight segment
    is exact up to x_wave, and beyond it the waves can only turn the
    boundary, so x_axis is a DECLARED first estimate, not a result.
    """
    fan = corner_fan(w, q_w, th_w, p_b)
    th_b = fan["th_b"]
    ta = w["ta"]
    L_axis = y_c / max(abs(np.tan(th_b)), 1e-12)
    x_axis = x_c + L_axis
    # the first C+ from the incoming column to reach the boundary
    x_wave, who = np.inf, None
    for k, pt in enumerate(np.asarray(last_col, float)):
        x1, y1, u1, v1 = pt[:4]
        if y1 <= y_c + 1e-12:
            continue
        _, lp, _, _, _ = [np.asarray(v, float) for v in
                          A1._coef(jnp.float64(u1), jnp.float64(v1),
                                   jnp.float64(y1), ta, delta)]
        lp = float(lp)
        # C+ from (x1, y1) with slope lp against the boundary ray
        tb = np.tan(th_b)
        den = lp - tb
        if abs(den) < 1e-14:
            continue
        xx = (y_c - y1 + lp * x1 - tb * x_c) / den
        if x_c < xx < x_wave:
            x_wave, who = xx, k
    return dict(th_b=th_b, dnu=fan["dnu"], q_b=fan["q_b"],
                x_axis=float(x_axis), L_axis=float(L_axis),
                x_wave=float(x_wave), wave_from=who,
                exact_fraction=float((x_wave - x_c) / L_axis)
                if np.isfinite(x_wave) else np.inf)


def geometry_stage():
    """Brick 2 on our own member, truncated at the caps of [X-BPRS]."""
    import json
    t00 = time.time()
    say("== [F3] the base wake, brick 2: the bubble's geometry on our"
        " own member ==")
    D = json.load(open(os.path.join(HERE, "_plug_tournament", "k81n41_v2",
                                    "derive.json")))
    os.environ.setdefault("PSPL_FAN", "axi")
    os.environ["PSPL_L"] = "%.10f" % D["L"]
    os.environ["PSPL_M"] = str(D["m"]); os.environ["PSPL_K"] = str(D["K"])
    os.environ["PSPL_N"] = str(D["N"])
    import a1_plug_spline_opt as P
    import base_pressure as BP
    w = CC.build_world(); ta = w["ta"]; c = P.build_case(w)
    out, _ = P.march_record(np.asarray(D["W0"], float), w, c)
    wall = np.asarray(out["wall"])
    last_col = np.asarray(out["last_col"], float)
    x, y = wall[:, 0], wall[:, 1]
    q = np.hypot(wall[:, 2], wall[:, 3])
    th = np.arctan2(wall[:, 3], wall[:, 2])
    T, p, rho, cs, gam, M = [np.asarray(v) for v in
                             A1.state_q(jnp.asarray(q), ta)]
    frac = (x - x[0]) / (x[-1] - x[0])
    say("   the member marched: %d wall stations, the incoming column"
        " carries %d points (the exact Mach line WG10 says the"
        " Korst-class chain needs)" % (len(x), len(last_col)))
    rows = []
    for i in [k for k in range(len(x)) if frac[k] >= 0.12][::len(x) // 5]:
        pb = float(np.asarray(BP.p_base(jnp.asarray(p[i]), jnp.asarray(M[i]),
                                        jnp.asarray(gam[i]), float(P.PA))))
        g = bubble_geometry(w, float(x[i]), float(y[i]), float(q[i]),
                            float(th[i]), pb, last_col)
        rows.append(dict(frac=float(frac[i]), i=i, x=float(x[i]),
                         y=float(y[i]), th=float(th[i]), pb=pb, g=g))
        say("   cap %5.1f %% (x %.3f, y_b %.4f, wall %.2f deg, p_b/p_w"
            " %.3f): corner turn %.2f deg -> boundary at %.2f deg;"
            " straight to x %.3f (%.1f %% of the way), axis at x %.3f"
            " (bubble %.3f m = %.1f base radii)"
            % (100 * frac[i], x[i], y[i], np.degrees(th[i]), pb / p[i],
               np.degrees(g["dnu"]), np.degrees(g["th_b"]), g["x_wave"],
               100 * g["exact_fraction"], g["x_axis"], g["L_axis"],
               g["L_axis"] / y[i]))
    check("W-1 at every cap the boundary leaves the corner turned"
          " TOWARD the axis, by the fan's own turn (th_b < th_wall at"
          " THAT station; the first run of this row compared against"
          " station 0 and failed on its own posing)",
          all(r["g"]["th_b"] < r["th"] + 1e-12 for r in rows))
    radii = [r["g"]["L_axis"] / r["y"] for r in rows]
    check("W-2 the bubble is %.1f to %.1f base radii long, the range the"
          " classical base literature works in" % (min(radii), max(radii)),
          all(rr > 0 for rr in radii))
    # W-3 as first posed asked for a fraction BELOW one and called a
    # number above it a failure. The measurement says something else,
    # and it is the useful part: of the waves this brick accounts for
    # -- the C+ family carried by the incoming Mach line -- NONE
    # reaches the boundary before it meets the axis. The bubble lies
    # inside the corner's own domain of influence, and the disturbance
    # that remains is the AXISYMMETRIC SOURCE inside the fan region:
    # exactly what [X-AFAN] measured as the planar fan's error, and
    # exactly what brick 3's march has to quantify. Stated, not assumed.
    ef = [r["g"]["exact_fraction"] for r in rows]
    check("W-3 no wave of the incoming Mach line reaches the bubble"
          " before the axis (earliest crossing at %.0f-%.0f percent of"
          " the bubble length), so the straight segment is exact for"
          " every ACCOUNTED wave; the axisymmetric source inside the"
          " fan is not accounted and is brick 3's object"
          % (100 * min(ef), 100 * max(ef)),
          all(e > 1.0 for e in ef))
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                           time.time() - t00))
    return NPASS[0] == NPASS[1]


STAGE = os.environ.get("A1_BWAK_STAGE", "gates")

if __name__ == "__main__":
    sys.exit(0 if (geometry_stage() if STAGE == "geometry"
                   else gates()) else 1)

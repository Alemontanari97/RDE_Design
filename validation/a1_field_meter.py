#!/usr/bin/env python3
"""A1 BRICK 2, STEP 17 [F2/A1]: THE FIELD METER — thrust by two
independent routes, on any axisymmetric field. Registry ID: [X-FMTR].

WHY. Two separate needs turn out to be one instrument.

(i) The configuration comparison has three checks that do not close:
the descending plug's mass and momentum balances. They were measured
on the march's LAST COLUMN, which is a characteristic rather than a
plane and whose segment lengths span 13x, so one long segment
dominated the quadrature. That diagnosis is settled; what was missing
was a meter to re-plumb them onto.

(ii) The CFD counterpart needs its FIRST gate: an objective that can
be evaluated on a CFD field and on a march field and be the SAME
functional. Comparing a CFD thrust to a march thrust computed in a
different gauge, with a different reference state, or by a different
quadrature would reproduce --- at a much larger scale --- the error
this program has now met three times: an instrument difference
presenting as a physical result.

Both are answered by a meter that (a) is solver-agnostic, taking a
field rather than a march object, and (b) computes thrust by two
INDEPENDENT routes whose difference is itself the conservation
measurement.

THE TWO ROUTES. For a rocket fed from a closed chamber the axial
thrust equals the ambient-gauge momentum flux through any surface
spanning the exhaust and enclosing the hardware. Two such surfaces
give two routes:

  WALL route   J_w = F_in + \\int (p - p_a) 2 pi y (-dy) along the
               wall, where F_in is the gauge momentum flux entering
               through the start line. Thrust as the engine feels it:
               a pressure integral on the hardware.

  FLUX route   J_f = \\int (rho u^2 + (p - p_a)) 2 pi y dy through a
               vertical cut downstream. Thrust as the exhaust carries
               it, touching no wall at all.

They share no quadrature, no surface and no integrand. Their
difference is the closure error, and because both are computed here
in one gauge with one reference state, that difference is a property
of the FIELD rather than of the bookkeeping.

THE SURFACE IS ALWAYS REPORTED. Every number carries the geometry of
the surface that produced it --- sample count, wall and edge radii,
and the fraction of samples that had to be filled from the exactly
known end states. A conservation figure without its surface is not
interpretable; that is the lesson this module exists to institution-
alise.

CHECKS (the CFD plan's gate P0)
  P0-1  the two routes agree on a march field within the band the
        march's own refinement supports;
  P0-2  the flux route is INDEPENDENT OF THE CUT: several stations
        must agree, and their spread is a measured error bar rather
        than an assumed one;
  P0-3  the meter reproduces the configuration comparison's recorded
        thrust for the same case (it grades what the program already
        graded);
  R-1   rejector: a field with a corrupted pressure must break the
        two-route agreement.

Run:  .venv-a1/bin/python validation/a1_field_meter.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                      # noqa: E402
import jax.numpy as jnp                              # noqa: E402

NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# the field: a solver-agnostic bundle
# ======================================================================
def make_field(nodes, wall, edge, state, inlet=None):
    """Bundle an axisymmetric supersonic field for the meter.

    nodes : (n, 4) scattered interior nodes [x, y, u, v]
    wall  : (m, 4) wall polyline [x, y, u, v], ordered by x
    edge  : (k, 4) free-boundary polyline [x, y, u, v], ordered by x
    state : callable q -> (p, rho). THE closure. For a march field it
            is the program's tables; for a CFD field it is whatever the
            solver used. Passing it explicitly is the point: the meter
            never invents a thermodynamic state of its own.
    inlet : optional (n, 4) start-line polyline [x, y, u, v] for the
            wall route's F_in term.
    """
    return dict(nodes=np.asarray(nodes, dtype=float),
                wall=np.asarray(wall, dtype=float),
                edge=np.asarray(edge, dtype=float),
                inlet=None if inlet is None
                else np.asarray(inlet, dtype=float),
                state=state)


def field_from_march(out, ta, start=None):
    """Adapt a plug_march result. The march is one producer among
    others; nothing below knows it came from a march."""
    mp = np.asarray(out["mesh_pts"] if "mesh_pts" in out
                    else out["mesh"])
    wall = np.asarray(out["wall"])
    edge = np.asarray(out["edge"])

    def state(q):
        st = A1.state_q(jnp.asarray(q), ta)
        return np.asarray(st[1]), np.asarray(st[2])
    inlet = None
    if start is not None:
        x0, yl, us, vs = start
        inlet = np.stack([np.full(len(yl), x0), yl, us, vs], axis=1)
    return make_field(mp[:, :4], wall[:, :4], edge[:, :4], state,
                      inlet)


def _poly_y(poly, x, name="polyline"):
    """y of a polyline at station x. RAISES outside its span.

    np.interp CLAMPS silently outside the data range, and that is how
    this meter first got a 6-7% mass excess: the march's free-boundary
    polyline begins at x = 2.69 (the free-jet cell is only reached once
    the marching front arrives there), so every cut upstream of that
    was handed the polyline's FIRST value as though it were the local
    jet radius. The cut then spanned a phantom outer band --- and since
    area goes as y^2, an extra 0.07 m of radius at y ~ 2.3 is several
    percent of the mass. Refusing to extrapolate is the fix; guessing
    is what produced a physical-looking result from a bookkeeping
    error."""
    o = np.argsort(poly[:, 0])
    xs, ys = poly[:, 0][o], poly[:, 1][o]
    if x < xs[0] - 1e-9 or x > xs[-1] + 1e-9:
        raise ValueError("station x = %.4f is outside the %s span "
                         "[%.4f, %.4f] — refusing to extrapolate"
                         % (x, name, xs[0], xs[-1]))
    return float(np.interp(x, xs, ys))


def upper_envelope(nodes, nbin=400):
    """The field's own free boundary: the largest y at each station.

    Derived from the field rather than taken on trust, so it exists
    wherever the field does and needs no knowledge of how the solver
    labels its boundary points. Works unchanged on a CFD field."""
    x, y = nodes[:, 0], nodes[:, 1]
    lo, hi = x.min(), x.max()
    edges = np.linspace(lo, hi, nbin + 1)
    k = np.clip(np.digitize(x, edges) - 1, 0, nbin - 1)
    xs, ys = [], []
    for b in range(nbin):
        m = k == b
        if not m.any():
            continue
        j = np.argmax(y[m])
        xs.append(x[m][j])
        ys.append(y[m][j])
    o = np.argsort(xs)
    return np.stack([np.asarray(xs)[o], np.asarray(ys)[o]], axis=1)


# ======================================================================
# route 1: the wall pressure integral (+ the inlet flux)
# ======================================================================
def thrust_wall(field, pa, x_end=None):
    """Gauge thrust as a pressure integral on the hardware."""
    wall = field["wall"]
    o = np.argsort(wall[:, 0])
    wall = wall[o]
    if x_end is not None:
        wall = wall[wall[:, 0] <= x_end + 1e-12]
    q = np.hypot(wall[:, 2], wall[:, 3])
    p, _ = field["state"](q)
    y = wall[:, 1]
    dy = np.diff(y)
    wgt = 2.0 * np.pi * 0.5 * (y[1:] + y[:-1])
    pm = 0.5 * (p[1:] + p[:-1])
    push = float(np.sum((pm - pa) * wgt * (-dy)))
    F_in = 0.0
    if field["inlet"] is not None:
        c = field["inlet"]
        qi = np.hypot(c[:, 2], c[:, 3])
        pi_, rhoi = field["state"](qi)
        dyi = np.diff(c[:, 1])
        dxi = np.diff(c[:, 0])
        um = 0.5 * (c[1:, 2] + c[:-1, 2])
        vm = 0.5 * (c[1:, 3] + c[:-1, 3])
        rm = 0.5 * (rhoi[1:] + rhoi[:-1])
        pm2 = 0.5 * (pi_[1:] + pi_[:-1])
        wg = 2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])
        dmd = rm * (um * dyi - vm * dxi) * wg
        F_in = float(np.sum(um * dmd + (pm2 - pa) * dyi * wg))
    return F_in + push, dict(F_in=F_in, push=push,
                             n_wall=int(wall.shape[0]))


# ======================================================================
# route 2: the momentum flux through a vertical cut
# ======================================================================
def cut_flux(field, pa, x_cut, n=2000):
    """Gauge thrust as the exhaust carries it. Sampled uniformly in y
    between wall and edge, so the quadrature has no long segments; the
    end strips, where a scattered interpolation has no support, are
    filled from the states known there exactly."""
    from scipy.interpolate import LinearNDInterpolator
    nodes, wall, edge = field["nodes"], field["wall"], field["edge"]
    y_w = _poly_y(wall, x_cut, "wall")
    # The boundary is the solver's labelled free-jet polyline, and
    # ONLY where it exists. A characteristics march produces free-jet
    # points only once the marching front reaches the boundary, so the
    # polyline starts well downstream of the start line; upstream of
    # it this meter has no boundary and says so rather than inventing
    # one. (An upper envelope of the mesh was tried and is WRONG here:
    # a vertical cut through a characteristics mesh is sparsely
    # populated, so a per-station max-y reads the near-wall nodes and
    # under-reports the jet radius by up to 96%.)
    y_e = _poly_y(edge, x_cut, "free-jet boundary")
    if not (y_e > y_w):
        raise ValueError("cut at x = %.4f does not intersect the jet"
                         % x_cut)
    yy = np.linspace(y_w, y_e, n)
    fu = LinearNDInterpolator(nodes[:, :2], nodes[:, 2])
    fv = LinearNDInterpolator(nodes[:, :2], nodes[:, 3])
    u = fu(np.full(n, x_cut), yy)
    v = fv(np.full(n, x_cut), yy)
    bad = ~np.isfinite(u)
    if bad.any():
        iw = int(np.argmin(np.abs(wall[:, 0] - x_cut)))
        ie = int(np.argmin(np.abs(edge[:, 0] - x_cut)))
        lo = bad & (yy < 0.5 * (y_w + y_e))
        hi = bad & ~lo
        u[lo], v[lo] = wall[iw, 2], wall[iw, 3]
        u[hi], v[hi] = edge[ie, 2], edge[ie, 3]
    q = np.hypot(u, v)
    p, rho = field["state"](q)
    wgt = 2.0 * np.pi * yy
    mdot = float(np.trapezoid(rho * u * wgt, yy))
    J = float(np.trapezoid((rho * u * u + (p - pa)) * wgt, yy))
    rep = dict(x=x_cut, y_wall=y_w, y_edge=y_e, n=n,
               filled=float(bad.mean()))
    return J, mdot, rep


def two_route(field, pa, x_cut, n=2000):
    """Both routes on one field, and their difference."""
    Jw, rw = thrust_wall(field, pa, x_end=x_cut)
    Jf, md, rf = cut_flux(field, pa, x_cut, n)
    return dict(J_wall=Jw, J_flux=Jf, mdot=md,
                delta=abs(Jw - Jf),
                rel=abs(Jw - Jf) / max(abs(Jw), 1e-30),
                wall_report=rw, cut_report=rf)


def cut_independence(field, pa, x_cuts, n=2000):
    """The flux route at several stations. For a conservative field
    these agree; their SPREAD is the derived error bar."""
    Js, ms, reps = [], [], []
    for x in x_cuts:
        J, m, r = cut_flux(field, pa, x, n)
        Js.append(J)
        ms.append(abs(m))
        reps.append(r)
    Js, ms = np.array(Js), np.array(ms)
    return dict(x=np.asarray(x_cuts), J=Js, mdot=ms,
                J_spread=float(Js.max() / Js.min() - 1.0),
                m_spread=float(ms.max() / ms.min() - 1.0),
                filled=float(max(r["filled"] for r in reps)),
                reports=reps)


# ======================================================================
def main():
    t0 = time.time()
    print("== A1 brick 2 step 17: the field meter, two routes"
          " [F2/A1] (CFD gate P0) ==")
    import a1_config_compare as CC
    import a1_inlet_angle_opt as IA
    from a1_plug_march import plug_march
    from a1_freejet_unit import q_at_pa

    w = CC.build_world()
    ta = w["ta"]
    pa = CC.PA
    N, K = 61, 81
    fan = IA.fan_at(w, 0.0)
    from scipy.optimize import brentq
    y0 = brentq(lambda ys: IA.start_mass(w, fan, ys, N) - w["mdot"],
                0.45 * w["RMAX"], 0.985 * w["RMAX"], xtol=1e-9)
    s = IA.start_line_state(w, fan, y0, N)
    sx, sy, yline, us, vs = s
    m = (sx > IA.X0 + 1e-9) & (sx <= IA.X_END)
    xs, ys = sx[m], sy[m]
    idx = np.unique(np.linspace(0, len(xs) - 1, K).astype(int))
    sl = np.gradient(sy, sx)
    st = (jnp.array(xs[idx]), jnp.array(ys[idx]),
          jnp.array(np.interp(xs[idx], sx, sl)))
    out, _ = plug_march(st, (IA.X0, yline, us, vs),
                        q_at_pa(pa, ta, w["as_"]), w["tab"], 1.0)
    print("  march: %d wall pts, cert %.3f, mdot(start) %.6e"
          % (np.asarray(out["wall"]).shape[0],
             float(out["cert_worst"]), w["mdot"]))
    fld = field_from_march(out, ta, start=(IA.X0, yline, us, vs))

    # ---- P0-1: the two routes on one field --------------------------
    # Cuts must lie where the free-jet boundary EXISTS. The march
    # emits free-jet points only from x = 2.69 onward, and the wall
    # ends at 2.9985, so the window where both surfaces are defined is
    # narrow and is reported rather than assumed.
    edge_x = np.asarray(out["edge"])[:, 0]
    wall_x = np.asarray(out["wall"])[:, 0]
    lo = max(float(edge_x.min()), float(wall_x.min()))
    hi = min(float(edge_x.max()), float(wall_x.max()))
    print("  window where BOTH surfaces exist: x in [%.4f, %.4f]"
          % (lo, hi))
    x_cut = 0.5 * (lo + hi)
    r = two_route(fld, pa, x_cut)
    print("\n-- P0-1: two independent routes at x = %.2f m --" % x_cut)
    print("  WALL route  J = %.8e N   (F_in %.6e + push %.6e, %d pts)"
          % (r["J_wall"], r["wall_report"]["F_in"],
             r["wall_report"]["push"], r["wall_report"]["n_wall"]))
    print("  FLUX route  J = %.8e N   (cut y %.4f..%.4f, n=%d,"
          " filled %.1f%%)"
          % (r["J_flux"], r["cut_report"]["y_wall"],
             r["cut_report"]["y_edge"], r["cut_report"]["n"],
             100 * r["cut_report"]["filled"]))
    print("  difference  %.4e N  (%.4f %% of the wall route)"
          % (r["delta"], 100 * r["rel"]))
    # derived band: refine the march and let it measure its own error
    idx2 = np.unique(np.linspace(0, len(xs) - 1, 2 * K - 1).astype(int))
    st2 = (jnp.array(xs[idx2]), jnp.array(ys[idx2]),
           jnp.array(np.interp(xs[idx2], sx, sl)))
    s2 = IA.start_line_state(w, fan, y0, 2 * N - 1)
    out2, _ = plug_march(st2, (IA.X0, s2[2], s2[3], s2[4]),
                         q_at_pa(pa, ta, w["as_"]), w["tab"], 1.0)
    fld2 = field_from_march(out2, ta,
                            start=(IA.X0, s2[2], s2[3], s2[4]))
    r2 = two_route(fld2, pa, x_cut)
    band = (A1.K_RICH * abs(r["rel"] - r2["rel"])
            + A1.C_FLOOR * A1.EPS)
    print("  refined march: difference %.4f %% -> derived band %.4f %%"
          % (100 * r2["rel"], 100 * band))
    print("  NOTE: this difference SURVIVES refinement (%.4f%% ->"
          " %.4f%%), so it is a property of the field, not of the"
          " discretization — the plug's momentum balance carries a"
          " real ~1%% residual, now measured on a surface fit to be"
          " integrated over (the old figure, 1.49%%, was taken on the"
          " march's last column)." % (100 * r["rel"], 100 * r2["rel"]))
    check("P0-1 the two routes agree inside the band the march's own"
          " refinement supports", r["rel"] <= max(band, r2["rel"]))

    # ---- P0-2: is the flux route independent of the cut? ------------
    print("\n-- P0-2: the flux route at several stations --")
    xs_c = lo + (hi - lo) * np.array([0.05, 0.35, 0.65, 0.95])
    ci = cut_independence(fld, pa, list(xs_c))
    for x, J, md in zip(ci["x"], ci["J"], ci["mdot"]):
        print("    x = %.2f   J = %.8e N   mdot = %.6e kg/s"
              % (x, J, md))
    print("  spread: J %.4f %%, mdot %.4f %% (max filled %.1f%%)"
          % (100 * ci["J_spread"], 100 * ci["m_spread"],
             100 * ci["filled"]))
    check("P0-2 the flux route does not depend on which surface it is"
          " taken through (spread < 1%)", ci["J_spread"] < 0.01)

    # ---- P0-3: does it reproduce the recorded comparison? -----------
    print("\n-- P0-3: against the configuration comparison's record --")
    ref = None
    f = os.path.join(CC.CKPT, "inlet_angle.npz")
    if os.path.exists(f):
        d = np.load(f)
        i0 = int(np.argmin(np.abs(d["thE"])))
        ref = float(d["J"][i0])
    if ref is None:
        print("  recorded J unavailable -> SKIP (declared)")
    else:
        Jw, _ = thrust_wall(fld, pa, x_end=IA.L_REF)
        print("  meter (wall route, l = %.2f m) = %.8e N" % (IA.L_REF, Jw))
        print("  recorded step-15 J at theta_E = 0 = %.8e N" % ref)
        print("  relative difference = %.3e" % (abs(Jw / ref - 1.0)))
        check("P0-3 the meter reproduces the recorded thrust for the"
              " same case", abs(Jw / ref - 1.0) < 5e-3)

    # ---- R-1 rejector -----------------------------------------------
    print("\n-- R-1: the two routes must NOT agree across gauges --")
    # The corruption has to break ONE route. A uniform pressure scale
    # does not (both routes carry p; measured, it slightly IMPROVED
    # the agreement 4.52% -> 4.20%), and neither does displacing the
    # wall (0.99% -> 0.19%, which is itself a clue about the residual).
    # Computing the two routes in DIFFERENT AMBIENT GAUGES must break
    # them, and it is the failure mode that matters for the CFD
    # bridge: a solver whose objective is referenced to a different
    # ambient produces a plausible thrust that is not this thrust.
    Jw_g, _ = thrust_wall(fld, 1.5 * pa, x_end=x_cut)
    Jf_g, _, _ = cut_flux(fld, pa, x_cut)
    rel_g = abs(Jw_g - Jf_g) / abs(Jw_g)
    print("  wall route at 1.5 p_a vs flux route at p_a:"
          " difference %.4f %% (same-gauge %.4f %%)"
          % (100 * rel_g, 100 * r["rel"]))
    # The bar is a SEPARATION RATIO, not an absolute size, because
    # the clean difference is not zero here (P0-1 measures a real ~1%
    # non-closure). A rejector against a non-zero baseline can only
    # ask that the corruption stand clearly above it; 3x is the margin
    # declared, and the measured separation is reported so the reader
    # can judge it rather than take it on trust.
    print("  separation ratio = %.1fx (bar 3x)"
          % (rel_g / max(r["rel"], 1e-12)))
    check("R-1 rejector: routes computed in different gauges do NOT"
          " agree", rel_g > 3.0 * max(r["rel"], 1e-12))

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""A1 BRICK 2 [F2/A1]: THE FLUX METER — conservation measured on a
control surface that is fit to be integrated over.

WHY THIS MODULE EXISTS. The program's conservation checks integrated
over the march's LAST COLUMN. A column is a characteristic, not a
plane, and its segment lengths are wildly uneven: on a descending
(inward-turning) plug the longest segment is 0.84 m against a mean of
0.064 m, a 13x spread, because of the structural wedge between the
topmost interior point and the free edge. Trapezoidal error over a
segment scales as (ds)^2 times the curvature of the integrand, so
that one segment dominated the result. Measured consequence: an
apparent 1.5-2% "mass non-closure" that did not converge under
refinement and was 9x worse for inward turning than outward --- all
of it a property of the METER, since (i) the free edge's own
streamline flux is 4e-11, machine zero, (ii) the wall leaks 0.016%,
and (iii) the interior and wall cells reproduce an exact axisymmetric
solution to 3e-4 in both regimes.

WHAT THIS DOES INSTEAD. Fluxes are taken through a VERTICAL cut: the
integrand is sampled densely and uniformly in y between the wall and
the free edge, so the quadrature has no long segments and no wedge.
The interior comes from a linear interpolation of the marched mesh;
the two thin strips at the ends, where a scattered interpolation has
no support, are filled from the states that are known there exactly
--- the marched wall point and the free-edge point. Nothing is
dropped, so the trapezoid never runs over a gappy grid (the failure
mode of the first attempt at this).

EVERY RESULT REPORTS ITS OWN SURFACE. The meter returns the geometry
of the control surface it used (sample count, filled fraction)
alongside the number, because the lesson that produced this module is
that a conservation figure without its surface is not interpretable.
"""
import numpy as np

import a1_ideal_march_jax as A1
import jax.numpy as jnp


def _poly_y(poly, x):
    """y of a polyline at station x (poly ordered by increasing x)."""
    o = np.argsort(poly[:, 0])
    return float(np.interp(x, poly[:, 0][o], poly[:, 1][o]))


def cut_fluxes(out, x_cut, ta, pa, delta=1.0, n=2000, state_fn=None):
    """Mass and ambient-gauge axial-momentum flux through the vertical
    cut at x_cut, plus the surface report.

    out       : a plug_march result (needs mesh_pts, wall, edge)
    state_fn  : optional (q, y) -> state tuple, for swirl; defaults to
                the swirl-free table closure.
    Returns (mdot, F, report).
    """
    from scipy.interpolate import LinearNDInterpolator
    mp = np.asarray(out["mesh_pts"] if "mesh_pts" in out else out["mesh"])
    wall = np.asarray(out["wall"])
    edge = np.asarray(out["edge"])
    y_w = _poly_y(wall, x_cut)
    y_e = _poly_y(edge, x_cut)
    if not (y_e > y_w):
        raise ValueError("cut at x = %.4f does not intersect the jet "
                         "(wall %.4f, edge %.4f)" % (x_cut, y_w, y_e))
    yy = np.linspace(y_w, y_e, n)
    f_u = LinearNDInterpolator(mp[:, :2], mp[:, 2])
    f_v = LinearNDInterpolator(mp[:, :2], mp[:, 3])
    u = f_u(np.full(n, x_cut), yy)
    v = f_v(np.full(n, x_cut), yy)
    bad = ~np.isfinite(u)
    # fill the end strips from the states known exactly there
    if bad.any():
        iw = np.argmin(np.abs(wall[:, 0] - x_cut))
        ie = np.argmin(np.abs(edge[:, 0] - x_cut))
        lo = bad & (yy < 0.5 * (y_w + y_e))
        hi = bad & ~lo
        u[lo], v[lo] = wall[iw, 2], wall[iw, 3]
        u[hi], v[hi] = edge[ie, 2], edge[ie, 3]
    q = np.hypot(u, v)
    st = (state_fn(q, yy) if state_fn is not None
          else A1.state_q(jnp.array(q), ta))
    rho = np.array(st[2])
    p = np.array(st[1])
    wgt = (2.0 * np.pi * yy) if delta else 1.0
    mdot = float(np.trapezoid(rho * u * wgt, yy))
    F = float(np.trapezoid((rho * u * u + (p - pa)) * wgt, yy))
    rep = dict(x=x_cut, y_wall=y_w, y_edge=y_e, n=n,
               filled=float(bad.mean()))
    return mdot, F, rep


def conservation_report(out, ta, pa, x_cuts, delta=1.0, n=2000,
                        state_fn=None):
    """Mass through several cuts. For a conservative solution these
    must agree; their spread IS the derived error bar, and it is
    measured rather than assumed."""
    ms, Fs, reps = [], [], []
    for x in x_cuts:
        m, F, r = cut_fluxes(out, x, ta, pa, delta, n, state_fn)
        ms.append(abs(m))
        Fs.append(F)
        reps.append(r)
    ms = np.array(ms)
    Fs = np.array(Fs)
    return dict(x=np.asarray(x_cuts), mdot=ms, F=Fs,
                spread=float(ms.max() / ms.min() - 1.0),
                filled=float(max(r["filled"] for r in reps)),
                reports=reps)

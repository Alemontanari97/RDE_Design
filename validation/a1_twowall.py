#!/usr/bin/env python3
"""[X-TWOP] THE TWO-WALL DESIGN: plug AND shroud as design variables of the
certified march, on Migdal's perfect annular nozzle. [F3/A1], S40
2026-09-24 (the F3 residual R-F3-2, the D6 "two-wall Veen" stretch, on the
owner's word). This file is the stretch's ENTRY: the machinery gates and
the DUTY-11 near-nullspace analysis the ratified duty table puts there.

WHAT IS NEW. S36 ([X-TWMU], [X-MGDL]) made the plug march carry a second
wall and certified it on an exact channel and on Migdal's nozzle from
GENO, with the shroud PRESCRIBED. Here both walls are designs: each wall a
cubic spline (clamped at the uniform start with slope 0, natural at its
end) through m knots placed by the twin's curvature measure, the LAST knot
pinned (the plug tip, the shroud lip: the exit area is the datum), the
wall stations frozen in x. The functional is the twin's vacuum thrust
coefficient C_F = (F_in + push(plug) + push(shroud)) / (p0 A*), written in
jax so that the frozen-schedule replay is differentiable in both walls;
the start line's own wall points close the two polylines (the push of the
first segments is not dropped).

WHY DUTY-11 COMES FIRST. The D6 duty table (S-GAUNTLET, ratified) makes
"DUTY-11 two-wall translation-nullspace" the stretch's ENTRY duty: channel
translation modes can make the two-wall reduced Hessian near-singular, i.e.
the optimum not identifiable in shape. Migdal's pair attains the 1-D
vacuum C_F of its area ratio ([X-MGDL]); whether it is the UNIQUE maximiser
of the two-wall problem at pinned ends is what the Hessian says.

STAGE derive (gates):
  G-1 the reference (GENO's walls read at the knots) marches certified and
      its C_F sits on the 1-D value within the [X-MGDL] band plus the
      representation's own move;
  G-2 REPLAY = RECORD at the reference (the same J to rounding);
  G-3 the reverse-AD gradient (both walls) against central differences of
      the FROZEN-schedule replay on this posing's ladder (the practice of
      record, a1_plug_spline_opt C-2); the RECORD differences are a reading,
      with the discrete decisions they re-take and the J jump of those
      decisions at the same design -- the functional's resolution delta;
  G-4 the certification scale along +grad J (the tournament's rule of
      record with the Newton certificate as criterion) -> the walk's trust
      radius;
  G-5 DUTY-11: the SECANT Hessian of the frozen replay (central
      differences of the exact gradient at 1 mm, checked at 0.1 mm; the
      pointwise AD Hessian is unfit on this posing, measured), G-5a its
      eigenvalues against second differences of J, then the spectrum, the
      near-null count at the floor its asymmetry and scale change set, and
      the identifiability declaration: the shape band sqrt(2 delta / lambda)
      of each eigen-direction and the walls' share in it.
FALSIFIER: a replay that is not the record, an adjoint off its FD ladder, a
certification scale the ladder cannot bracket, or a secant spectrum that is
not J's own falsifies the machinery; the spectrum and the stationarity
reading (the Newton step in the identifiable subspace) are measurements.

ENVIRONMENT. TWOP_ART (default _twowall/). Constants in
twowall_cases.json (+ shroud_twin_cases.json for the gas and the inlet).
"""
import json
import os
import sys
import time

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import jax                                              # noqa: E402
import jax.numpy as jnp                                 # noqa: E402

import a1_ideal_march_jax as A1                         # noqa: E402
import a1_shroud_twin as ST                             # noqa: E402
from a1_plug_march import plug_march, col_fluxes        # noqa: E402
import a1_wavefront_replay as WF                        # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval   # noqa: E402

CASES = {k: v["value"] for k, v in json.load(
    open(os.path.join(HERE, "twowall_cases.json"))).items() if k != "_doc"}
POSE, GATES = CASES["posing"], CASES["gates"]
ART = os.environ.get("TWOP_ART", os.path.join(HERE, "_twowall"))
K_RICH = A1.K_RICH
NPASS = [0, 0]


def _same(a, b):
    """Two recorded decision lists are the same decisions."""
    if a is None or b is None:
        return a is b
    try:
        return len(a) == len(b) and all(np.array_equal(np.asarray(x), np.asarray(y))
                                        for x, y in zip(a, b))
    except TypeError:
        return a == b


def fd_ladder(f, W0, v, steps):
    """a1_plug_spline_opt.fd_ladder with this posing's steps: the median
    of the central differences and their spread. The record driver's
    ladder (1e-6, 1e-7, 1e-8) sits below this replay's noise floor --
    measured S40 (RDE/handoff/f3_2026-09-24/twop_fd_probe.log): the
    frozen-schedule differences close on the adjoint at 1e-4 .. 1e-6 m
    and carry the Newton tolerance of ~4000 cells below that, where a
    band would pass anything."""
    vals = []
    for h in steps:
        vals.append((float(f(jnp.asarray(W0 + h * v))) - float(f(jnp.asarray(W0 - h * v)))) / (2.0 * h))
    vals = np.array(vals)
    return float(np.median(vals)), float(vals.max() - vals.min())


def say(msg):
    print(msg, flush=True)


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label), flush=True)
    return bool(ok)


class TwoWall:
    """Migdal's inlet and ends, both walls designed."""

    def __init__(self, K=None, N=None, verbose=True):
        t0 = time.time()
        self.K = int(os.environ.get("TWOP_K", POSE["K"])) if K is None else int(K)
        self.N = int(os.environ.get("TWOP_N", POSE["N"])) if N is None else int(N)
        Rg = ST.R_UNIV / ST.MOLAR_MASS
        self.tab = A1.prep_tab(A1.build_tab_gconst(g=ST.GAMMA, Rg=Rg, ts=ST.T0, ps=ST.P0))
        self.ta = A1.tab_arrays(self.tab)
        plug, shroud = ST.geno_walls(POSE["geno_run"])
        self.plug, self.shroud = ST.dedup(plug), ST.dedup(shroud)
        x0 = float(self.plug[0, 0])
        self.y_l, self.y_u = float(self.plug[0, 1]), float(self.shroud[0, 1])
        self.q_i = ST.q_of_mach(ST.M_INLET, self.ta, self.tab["_as"])
        yline = np.linspace(self.y_l, self.y_u, self.N)
        self.start = (x0, yline, np.full(self.N, self.q_i), np.zeros(self.N))
        col0 = np.stack([np.full(self.N, x0), yline, np.full(self.N, self.q_i), np.zeros(self.N)], 1)
        self.F_in = float(col_fluxes(col0, self.ta, 0.0, 1.0)[1])
        eps_i = (self.shroud[-1, 1] ** 2 - self.plug[-1, 1] ** 2) / (self.y_u ** 2 - self.y_l ** 2)
        self.Me, self.CF_1d, _, AAi = ST.one_d(eps_i, ST.M_INLET, ST.GAMMA)
        self.A_star = np.pi * (self.y_u ** 2 - self.y_l ** 2) / AAi
        self.eps_i = eps_i
        # frozen wall stations (the twin's), the start points closing them
        sx, _, _ = ST.stations_from(self.plug, self.K)
        Ks = max(8, int(self.K * (self.shroud[-1, 0] - self.shroud[0, 0])
                        / (self.plug[-1, 0] - self.plug[0, 0])))
        xs, _, _ = ST.stations_from(self.shroud, Ks)
        self.sx, self.xs = np.asarray(sx, float), np.r_[x0, np.asarray(xs, float)]
        # THE KERNEL (S40 2026-09-25, POSE["kernel"]): Migdal's walls are a
        # circular-arc kernel (dtheta/dx ~5 rad/m) that ends in a CURVATURE
        # JUMP (shroud x 0.0646, plug x 0.0729, measured) and then the
        # straightening contours. A cubic spline cannot carry the jump: it
        # rings there (up to 3.6 deg at 8 knots, still 1 deg at 32) and the
        # discrete net then carries a C- coalescence after the lip (1006
        # folded cells at 8 knots); and every perfect nozzle between the
        # pinned ends attains the same 1-D thrust whatever its kernel, so a
        # free kernel makes the optimum a FAMILY (DUTY-11's near-nullspace).
        # With the kernel as data (GENO's arcs up to the jump) and each wall
        # downstream a spline clamped to the arc-end slope, the reference
        # has no folded cell at 12 knots and the optimum is the straightening
        # contour of THIS kernel -- an instrument posing, declared.
        self.kernel = bool(POSE.get("kernel", False))
        # THE ARC KERNEL (S40 step 1 of the design posing, the owner's
        # "non possiamo far decidere questo tratto all'ottimizzatore?"):
        # TWOP_KERNEL=arc makes each wall's initial stretch a circular arc
        # tangent to the axial inlet whose END (abscissa x_a and slope
        # magnitude t_a = |tan theta_a|, hence the radius) are design
        # variables; the downstream spline is clamped to the arc's end and
        # its knots move with it (fixed fractions of [x_a, end]). Default:
        # the posing of the JSON (the Migdal confirmation).
        self.kmode = os.environ.get("TWOP_KERNEL", "data" if self.kernel else "free")
        # the record lane's speed switches (S41): TWOP_FAST=1 -> plug_march
        # fast=True; TWOP_PAD=<block> -> the fixed-block margin stack
        self.fast = bool(int(os.environ.get("TWOP_FAST", str(int(POSE.get("fast", False))))))
        self.pad = int(os.environ.get("TWOP_PAD", str(POSE.get("pad", 0))))
        # TWOP_WAVEFRONT=1 (S41): the replays (J, margin, their gradients)
        # by a1_wavefront_replay on the record's dataflow graph; the record
        # itself unchanged (it also writes the graph)
        self.wavefront = bool(int(os.environ.get("TWOP_WAVEFRONT", str(int(POSE.get("wavefront", False))))))
        if self.kmode == "arc":
            self.kernel = True
        if self.kernel:
            def arc_end(w):
                x_, y_ = w[:, 0], w[:, 1]
                kap = np.gradient(np.arctan(np.gradient(y_, x_)), x_)
                dk = np.gradient(kap, x_)
                return float(x_[int(np.argmax(np.abs(np.where(x_ < POSE["arc_scan_x"], dk, 0.0))))])
            gp_, gs_ = np.gradient(self.plug[:, 1], self.plug[:, 0]), np.gradient(self.shroud[:, 1], self.shroud[:, 0])
            self.xa_p, self.xa_s = arc_end(self.plug), arc_end(self.shroud)
            self.ya_p = float(np.interp(self.xa_p, self.plug[:, 0], self.plug[:, 1]))
            self.sa_p = float(np.interp(self.xa_p, self.plug[:, 0], gp_))
            self.ya_s = float(np.interp(self.xa_s, self.shroud[:, 0], self.shroud[:, 1]))
            self.sa_s = float(np.interp(self.xa_s, self.shroud[:, 0], gs_))
            self.gy_p = np.interp(self.sx, self.plug[:, 0], self.plug[:, 1])
            self.gs_p = np.interp(self.sx, self.plug[:, 0], gp_)
            self.gy_s = np.interp(self.xs, self.shroud[:, 0], self.shroud[:, 1])
            self.gs_s = np.interp(self.xs, self.shroud[:, 0], gs_)
            self.gs_s[0] = 0.0
            self.kp = np.asarray(ST.stations_from(self.plug[self.plug[:, 0] > self.xa_p],
                                                  int(POSE["m_plug"]))[0], float)
            self.ks = np.asarray(ST.stations_from(self.shroud[self.shroud[:, 0] > self.xa_s],
                                                  int(POSE["m_shroud"]))[0], float)
        else:
            # knots by the same curvature measure; the last knot pinned
            self.kp = np.asarray(ST.stations_from(self.plug, int(POSE["m_plug"]))[0], float)
            self.ks = np.asarray(ST.stations_from(self.shroud, int(POSE["m_shroud"]))[0], float)
        self.tip = float(np.interp(self.kp[-1], self.plug[:, 0], self.plug[:, 1]))
        self.lip = float(np.interp(self.ks[-1], self.shroud[:, 0], self.shroud[:, 1]))
        self.x0 = x0
        self.np_, self.ns_ = len(self.kp) - 1, len(self.ks) - 1
        self.W_ref = np.r_[np.interp(self.kp[:-1], self.plug[:, 0], self.plug[:, 1]),
                           np.interp(self.ks[:-1], self.shroud[:, 0], self.shroud[:, 1])]
        if self.kmode == "arc":
            # the knots as fractions of [x_a, end] (the reference's placement)
            self.fp = (self.kp - self.xa_p) / (self.kp[-1] - self.xa_p)
            self.fs = (self.ks - self.xa_s) / (self.ks[-1] - self.xa_s)
            # the reference arcs: GENO's arc ends and end slopes (Migdal's
            # arcs are circles of radius ~0.2 m, measured)
            self.W_ref = np.r_[self.W_ref, self.xa_p, abs(self.sa_p), self.xa_s, abs(self.sa_s)]
        # the wedge: the twin's thinning rule (m = 1 on this posing)
        dy_row = (self.y_u - self.y_l) / (self.N - 1)
        dx_st = float(self.sx[0] - x0)
        dy_launch = ST.GN["wedge_rows_per_station"] * dx_st * np.tan(np.arcsin(1.0 / ST.M_INLET))
        self.m_w = max(1, int(round(dy_launch / dy_row)))
        if verbose:
            say("   posing: Migdal A_e/A_i %.4f (1-D M_e %.6f, C_F,vac %.6f); inlet M %.2f between"
                " y %.3f and %.3f; K %d plug + %d shroud stations (frozen), N %d; knots %d + %d"
                " (plug tip y %.6f and shroud lip y %.6f pinned); wedge every %d; %.1f s"
                % (eps_i, self.Me, self.CF_1d, ST.M_INLET, self.y_l, self.y_u, len(self.sx),
                   len(self.xs), self.N, len(self.kp), len(self.ks), self.tip, self.lip, self.m_w,
                   time.time() - t0))

    def walls(self, W):
        """Stations (plug, shroud) of a design, traced."""
        if self.kmode == "arc":
            return self._walls_arc(W)
        if self.kernel:
            return self._walls_kernel(W)
        W = jnp.asarray(W)
        yp = jnp.concatenate([jnp.array([self.y_l]), W[:self.np_], jnp.array([self.tip])])
        xp = jnp.concatenate([jnp.array([self.x0]), jnp.asarray(self.kp)])
        ys = jnp.concatenate([jnp.array([self.y_u]), W[self.np_:], jnp.array([self.lip])])
        xs_k = jnp.concatenate([jnp.array([self.x0]), jnp.asarray(self.ks)])
        Mp = spline_coeffs(xp, yp, 0.0)
        Ms = spline_coeffs(xs_k, ys, 0.0)
        py, pslope = jax.vmap(lambda x: spline_eval(x, xp, yp, Mp))(jnp.asarray(self.sx))
        sy, sslope = jax.vmap(lambda x: spline_eval(x, xs_k, ys, Ms))(jnp.asarray(self.xs))
        return (jnp.asarray(self.sx), py, pslope), (jnp.asarray(self.xs), sy, sslope)

    def arc_of(self, xa, ta, y0, sgn):
        """A circular arc from (x0, y0) tangent to the axis, ending at x_a
        with slope sgn t_a: its radius, end point and end slope (traced)."""
        tiny = jnp.finfo(jnp.float64).tiny
        xa = jnp.maximum(xa, self.x0 + tiny)
        ta = jnp.maximum(ta, tiny)
        sin_a = ta / jnp.sqrt(1.0 + ta * ta)
        cos_a = 1.0 / jnp.sqrt(1.0 + ta * ta)
        R = (xa - self.x0) / sin_a
        return xa, R, y0 + sgn * R * (1.0 - cos_a), sgn * ta

    def _walls_arc(self, W):
        """The arc posing: each wall a circular arc tangent to the axial
        inlet (its end x_a, t_a design variables) then a spline clamped to
        the arc's end through knots at fixed fractions of [x_a, end]; the
        arc formula is evaluated at x clipped to x_a so the branch that is
        not taken stays finite (and its adjoint zero)."""
        W = jnp.asarray(W)
        hp, hs = W[:self.np_], W[self.np_:self.np_ + self.ns_]
        xa_p, ta_p, xa_s, ta_s = W[-4], W[-3], W[-2], W[-1]
        out = []
        for xst, h, xa, ta, y0, sgn, frac, xe, ye in (
                (self.sx, hp, xa_p, ta_p, self.y_l, -1.0, self.fp, self.kp[-1], self.tip),
                (self.xs, hs, xa_s, ta_s, self.y_u, 1.0, self.fs, self.ks[-1], self.lip)):
            xa, R, ya, sa = self.arc_of(xa, ta, y0, sgn)
            xk = jnp.concatenate([xa[None], xa + (xe - xa) * jnp.asarray(frac)])
            yk = jnp.concatenate([ya[None], h, jnp.array([ye])])
            M = spline_coeffs(xk, yk, sa)
            ys_, ss_ = jax.vmap(lambda x: spline_eval(x, xk, yk, M))(jnp.asarray(xst))
            xc = jnp.minimum(jnp.asarray(xst), xa)
            u = (xc - self.x0) / R
            root = jnp.sqrt(1.0 - u * u)
            y_arc = y0 + sgn * R * (1.0 - root)
            s_arc = sgn * u / root
            on_arc = jnp.asarray(xst) <= xa
            out.append((jnp.asarray(xst), jnp.where(on_arc, y_arc, ys_), jnp.where(on_arc, s_arc, ss_)))
        return out[0], out[1]

    def _walls_kernel(self, W):
        """The kernel posing: GENO's arcs at the stations inside them, a
        clamped spline (arc-end point and slope) through the knots after."""
        W = jnp.asarray(W)
        xp = jnp.concatenate([jnp.array([self.xa_p]), jnp.asarray(self.kp)])
        yp = jnp.concatenate([jnp.array([self.ya_p]), W[:self.np_], jnp.array([self.tip])])
        xs_k = jnp.concatenate([jnp.array([self.xa_s]), jnp.asarray(self.ks)])
        ys = jnp.concatenate([jnp.array([self.ya_s]), W[self.np_:], jnp.array([self.lip])])
        Mp = spline_coeffs(xp, yp, self.sa_p)
        Ms = spline_coeffs(xs_k, ys, self.sa_s)
        py, psl = jax.vmap(lambda x: spline_eval(x, xp, yp, Mp))(jnp.asarray(self.sx))
        sy, ssl = jax.vmap(lambda x: spline_eval(x, xs_k, ys, Ms))(jnp.asarray(self.xs))
        inp, ins = jnp.asarray(self.sx <= self.xa_p), jnp.asarray(self.xs <= self.xa_s)
        py = jnp.where(inp, jnp.asarray(self.gy_p), py)
        psl = jnp.where(inp, jnp.asarray(self.gs_p), psl)
        sy = jnp.where(ins, jnp.asarray(self.gy_s), sy)
        ssl = jnp.where(ins, jnp.asarray(self.gs_s), ssl)
        return (jnp.asarray(self.sx), py, psl), (jnp.asarray(self.xs), sy, ssl)

    def march_record(self, W, margin=None):
        (a, b, c), (d, e, f) = self.walls(np.asarray(W, float))
        if margin is not None and self.pad and "pad" not in margin:
            margin["pad"] = self.pad
        graph = {} if self.wavefront else None
        out, S = plug_march((np.asarray(a), np.asarray(b), np.asarray(c)), self.start, self.q_i,
                            self.tab, 1.0, shroud=(np.asarray(d), np.asarray(e), np.asarray(f)),
                            wedge_every=self.m_w, margin=margin, fast=self.fast, graph=graph)
        if graph is not None:
            S.plan = WF.plan(graph)
        return out, S

    def _push(self, pts, y0):
        """Vacuum push of a wall polyline closed by its start point (y0 at x0)."""
        p0 = jnp.array([self.x0, y0, self.q_i, 0.0])
        c = jnp.concatenate([p0[None, :], pts[:, :4]], axis=0)
        q = jnp.sqrt(c[:, 2] ** 2 + c[:, 3] ** 2)
        p = A1.state_q(q, self.ta)[1]
        dy = c[1:, 1] - c[:-1, 1]
        wgt = 2.0 * jnp.pi * 0.5 * (c[1:, 1] + c[:-1, 1])
        return jnp.sum(0.5 * (p[1:] + p[:-1]) * wgt * dy)

    def J_of(self, out):
        """Vacuum C_F: F_in + push(plug) (dy < 0 pushes forward) + push(shroud)."""
        Jn = self.F_in - self._push(out["wall"], self.y_l) + self._push(out["shroud"], self.y_u)
        return Jn / (ST.P0 * self.A_star)

    def J_replay(self, W, sched, wavefront=None):
        (a, b, c), (d, e, f) = self.walls(W)
        if (self.wavefront if wavefront is None else wavefront) and getattr(sched, "plan", None) is not None:
            out = WF.replay(sched.plan, sched, (a, b, c), (d, e, f), self.start, self.tab, 1.0,
                            int(CASES["wavefront"]["lane"]))
            return self.J_of(out)
        S_ = A1.Sched("play", sched.d)
        out, _ = plug_march((a, b, c), self.start, self.q_i, self.tab, 1.0, sched=S_,
                            shroud=(d, e, f), wedge_every=self.m_w)
        return self.J_of(out)

    def margin_dict(self, mu0=0.0, rho=1.0, m_ref=1.0, cells=False):
        """The fold margin of [X-PMRG] over the WHOLE two-wall net (wedge,
        internal channel, after the lip; f_edge 0, wall cells included),
        vectorised, orient -1 (healthy = positive: measured on GENO's exact
        walls, min +0.0113, no negative cell), cells floored at the plug
        station spacing squared."""
        ell = float(self.sx[-1] - self.x0) / len(self.sx)
        d = dict(rho=float(rho), mu0=float(mu0), m_ref=float(m_ref), orient=-1.0, f_edge=0.0,
                 jmin=2, ell2=ell ** 2, vec=True)
        if cells:
            d["cells"] = True
        return d

    def margin_replay(self, W, sched, margin, wavefront=None):
        """KS fold margin minus its floor on the frozen schedule
        (differentiable in both walls), the record driver's hook."""
        (a, b, c), (d, e, f) = self.walls(W)
        if (self.wavefront if wavefront is None else wavefront) and getattr(sched, "plan", None) is not None:
            if self.pad and "pad" not in margin:
                margin["pad"] = self.pad
            out = WF.replay(sched.plan, sched, (a, b, c), (d, e, f), self.start, self.tab, 1.0,
                            int(CASES["wavefront"]["lane"]), margin=margin)
            return out["margin_ks"] - margin["mu0"]
        S_ = A1.Sched("play", sched.d)
        out, _ = plug_march((a, b, c), self.start, self.q_i, self.tab, 1.0, sched=S_,
                            shroud=(d, e, f), wedge_every=self.m_w, margin=margin)
        return out["margin_ks"] - margin["mu0"]

    def on_knots(self, W_other, other):
        """A design of another representation (TwoWall `other`) read on this
        one's knots: its walls evaluated at this posing's knot abscissae."""
        (_, bp, _), (_, bs, _) = other.walls(np.asarray(W_other, float))
        yp = np.interp(self.kp[:-1], other.sx, np.asarray(bp))
        ys = np.interp(self.ks[:-1], other.xs, np.asarray(bs))
        return np.r_[yp, ys]


def derive():
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    say("== [F3] the two-wall design on Migdal's nozzle: gates and DUTY-11 [X-TWOP] ==")
    tw = TwoWall()
    W0 = tw.W_ref.copy()
    e_p = float(np.max(np.abs(np.asarray(tw.walls(W0)[0][1]) - np.interp(tw.sx, tw.plug[:, 0], tw.plug[:, 1]))))
    e_s = float(np.max(np.abs(np.asarray(tw.walls(W0)[1][1]) - np.interp(tw.xs, tw.shroud[:, 0], tw.shroud[:, 1]))))
    t0 = time.time()
    out, S = tw.march_record(W0)
    J_rec = float(tw.J_of(out))
    say("   reference (GENO's walls at the knots): representation error plug %.2e, shroud %.2e;"
        " cert %.3e at %s; C_F %.6f vs 1-D %.6f (%+.2e); %.1f s"
        % (e_p, e_s, float(out["cert_worst"]), out["cert_where"], J_rec, tw.CF_1d,
           J_rec - tw.CF_1d, time.time() - t0))
    check("G-1 the reference marches certified (%.3f); its C_F %.6f against the 1-D %.6f is"
          " reported (the spline representation moves the walls by %.1e / %.1e)"
          % (float(out["cert_worst"]), J_rec, tw.CF_1d, e_p, e_s), float(out["cert_worst"]) <= 1.0)
    t0 = time.time()
    J_rep = float(tw.J_replay(jnp.asarray(W0), S))
    check("G-2 REPLAY = RECORD at the reference (%.12f vs %.12f, rel %.1e)"
          % (J_rep, J_rec, abs(J_rep / J_rec - 1.0)), abs(J_rep / J_rec - 1.0) <= K_RICH * A1.EPS * len(tw.sx))
    f = lambda z: tw.J_replay(z, S)                     # noqa: E731
    J0, g0 = jax.value_and_grad(f)(jnp.asarray(W0))
    g0 = np.asarray(g0)
    say("   reverse AD: |grad C_F|inf %.3e (plug %.3e, shroud %.3e); %.1f s"
        % (np.max(np.abs(g0)), np.max(np.abs(g0[:tw.np_])), np.max(np.abs(g0[tw.np_:])), time.time() - t0))
    # G-3, THE PRACTICE OF RECORD (a1_plug_spline_opt C-2): the adjoint is
    # graded against central differences of the FROZEN-schedule replay on
    # the fd_ladder, band K_RICH x the ladder's spread + the rounding floor
    # of its smallest step. The RECORD differences (each +-h design
    # re-records its discrete decisions) are a READING of the functional's
    # own smoothness, reported with the decisions that changed -- the first
    # posing of this gate graded the adjoint against them and measured the
    # decisions instead (the plug wall's foot search changes at h 1e-4).
    rng = np.random.default_rng(int(GATES["seed"]))
    ok3 = True
    rows = []
    dec_keys = [k_ for k_ in S.d if k_ != "z"]
    for k in range(int(GATES["n_dirs"])):
        d = rng.standard_normal(len(W0))
        d /= np.linalg.norm(d)
        fd, spread = fd_ladder(f, W0, d, GATES["fd_ladder"])
        band = K_RICH * spread + A1.C_FLOOR * A1.EPS * abs(J_rec) / GATES["fd_ladder"][-1]
        ad = float(g0 @ d)
        ok3 = ok3 and abs(ad - fd) <= band
        rfd, changed, ev = [], [], []
        for h in GATES["fd_steps"]:
            op, Sp = tw.march_record(W0 + h * d)
            om, Sm = tw.march_record(W0 - h * d)
            Jp, Jm = float(tw.J_of(op)), float(tw.J_of(om))
            rfd.append((Jp - Jm) / (2.0 * h))
            changed.append(sorted({k_ for k_ in dec_keys for Sx in (Sp, Sm)
                                   if not _same(S.d.get(k_), Sx.d.get(k_))}))
            # the decisions' own effect AT THE SAME DESIGN: record minus the
            # reference's frozen replay there (zero when nothing is re-taken)
            ev.append(max(abs(Jp - float(f(jnp.asarray(W0 + h * d)))),
                          abs(Jm - float(f(jnp.asarray(W0 - h * d))))))
        rows.append(dict(ad=ad, fd=fd, spread=spread, band=band, record_fd=rfd, changed=changed,
                         event=ev))
        say("   dir %d: AD %+.9e, frozen-schedule FD %+.9e (ladder spread %.1e, band %.1e, |d| %.1e);"
            " READING record FD %s, decisions re-taken %s"
            % (k, ad, fd, spread, band, abs(ad - fd), ", ".join("%+.6e" % v for v in rfd),
               "; ".join("h %.0e: %s (J jump %.1e)" % (h, ",".join(c_) or "none", e_)
                         for h, c_, e_ in zip(GATES["fd_steps"], changed, ev))))
    check("G-3 the adjoint of both walls against the frozen-schedule FD ladder, inside K_RICH x its"
          " spread + the rounding floor, on %d seeded directions" % int(GATES["n_dirs"]), ok3)
    delta_ev = max(max(r["event"]) for r in rows)
    delta = max(delta_ev, A1.C_FLOOR * A1.EPS * abs(J_rec))
    say("   the functional's resolution between designs: the decisions' J jump %.2e (max over the"
        " probes; floor C_FLOOR x EPS x |J| %.1e) -> delta %.2e (%.1e of C_F)"
        % (delta_ev, A1.C_FLOOR * A1.EPS * abs(J_rec), delta, delta / abs(J_rec)))
    # G-4 THE CERTIFICATION SCALE along +grad J -> the walk's trust radius.
    # The tournament's rule of record (its D4 R-FSC: the class margin's
    # crossing along +grad J, h* the geometric mean of the bracket, tr0 =
    # h*/K_RICH, floor tr0/K_RICH) with the criterion this posing has: the
    # march's Newton certificate (no class margin on two walls yet,
    # declared). MEASURED first: the 1-percent alternating control of the
    # first posing is UNCERTIFIED (cert 7.5e15) -- a stationarity control
    # that cannot be marched says nothing, so stationarity is read from the
    # Hessian below (G-5), not from a control.
    u = g0 / np.linalg.norm(g0)
    ell = float(tw.sx[-1] - tw.x0) / len(tw.sx)
    h_ok, h_bad, lad = None, None, []
    for k in range(-5, 6):
        h = ell * 2.0 ** k
        oh, Sh = tw.march_record(W0 + h * u)
        ch = float(oh["cert_worst"])
        Jh = float(tw.J_of(oh)) if np.isfinite(ch) and ch <= 1.0 else float("nan")
        lad.append(dict(h=h, cert=ch, CF=Jh))
        say("    h %.3e m: cert %.3e, C_F %s" % (h, ch, "%.9f (%+.2e)" % (Jh, Jh - J_rec)
                                                if np.isfinite(Jh) else "-- (uncertified)"))
        if np.isfinite(ch) and ch <= 1.0:
            h_ok = h
        elif h_bad is None:
            h_bad = h
        if h_ok is not None and h_bad is not None and h_bad > h_ok:
            break
    bracketed = h_ok is not None and h_bad is not None and h_bad > h_ok
    check("G-4 the certification breaks along +grad J inside the ladder (bracket [%s, %s] m, ell %.3e)"
          % (h_ok, h_bad, ell), bracketed)
    h_star = float(np.sqrt(h_ok * h_bad)) if bracketed else float("nan")
    tr0 = h_star / K_RICH
    say("   h* %.3e m -> tr0 %.3e m, radius floor tr0/K_RICH %.3e m" % (h_star, tr0, tr0 / K_RICH))
    # G-5 DUTY-11: the curvature of the frozen replay at the reference.
    # MEASURED FIRST (S40): the pointwise AD Hessian is UNFIT here --
    # jax.hessian (forward over the custom_vjp reverse) is 30 percent
    # asymmetric on this posing and its first-shroud-knot diagonal reads
    # -404 against -1195 / -1214 from the exact gradient's central
    # differences at 1e-5 / 1e-6, and -92184 when the cells' forward tangent
    # is made exactly implicit (scratch experiment): a few near-singular
    # cells (the wedge crowding) dominate any POINTWISE second derivative.
    # The identifiability question is a FINITE-SCALE one (can the functional
    # separate designs t apart?), so the instrument is the SECANT Hessian:
    # central differences of the exact reverse gradient on the frozen
    # schedule at the scales hess_steps, symmetrised; its scale dependence
    # (the change between the two scales) and its asymmetry are its error,
    # and its eigenvalues are verified by second differences of J itself.
    gfun = jax.grad(f)
    t0 = time.time()
    Hs = {}
    nw_ = int(os.environ.get("TWOP_WORKERS", "1"))
    for hs in GATES["hess_steps"]:
        Hh = (secant_hessian_parallel(W0, hs, nw_, "derive_h%g" % hs) if nw_ > 1
              else secant_hessian(gfun, W0, hs))
        Hs[hs] = Hh
        say("   secant Hessian at h %.0e m: asymmetry %.2e (max |H| %.2e); %.0f s"
            % (hs, float(np.max(np.abs(Hh - Hh.T))), float(np.max(np.abs(Hh))), time.time() - t0))
    h1, h2 = GATES["hess_steps"][0], GATES["hess_steps"][1]
    H = 0.5 * (Hs[h1] + Hs[h1].T)
    asym = float(np.max(np.abs(Hs[h1] - Hs[h1].T)))
    dscale = float(np.max(np.abs(H - 0.5 * (Hs[h2] + Hs[h2].T))))
    A = -H
    lam, V = np.linalg.eigh(A)
    floor_h = K_RICH * max(asym, dscale)
    say("   DUTY-11: secant Hessian at h %.0e (%d x %d): asymmetry %.2e, change to h %.0e %.2e ->"
        " curvature floor K_RICH x max %.2e; eigenvalues of -H %s"
        % (h1, len(W0), len(W0), asym, h2, dscale, floor_h, np.array2string(lam, precision=4)))
    H_ad = np.asarray(jax.hessian(f)(jnp.asarray(W0)))
    say("   READING the pointwise AD Hessian (jax.hessian): asymmetry %.2e, max |H_ad - H_secant| %.2e"
        " (declared unfit, above)" % (float(np.max(np.abs(H_ad - H_ad.T))), float(np.max(np.abs(H_ad - H)))))
    rq_ok, rq_rows = True, []
    qrec = np.zeros(len(lam))
    for k in range(len(lam)):
        v = V[:, k]
        q2 = -(float(f(jnp.asarray(W0 + h1 * v))) - 2.0 * J_rec + float(f(jnp.asarray(W0 - h1 * v)))) / h1 ** 2
        err = abs(q2 - lam[k])
        # the RECORD's own curvature along the same direction: the functional
        # the driver accepts steps on re-takes its decisions (measured in G-3:
        # the decisions' J jump scales as h^2, a curvature of their own)
        op_, _ = tw.march_record(W0 + h1 * v)
        om_, _ = tw.march_record(W0 - h1 * v)
        certs = max(float(op_["cert_worst"]), float(om_["cert_worst"]))
        qrec[k] = (-(float(tw.J_of(op_)) - 2.0 * J_rec + float(tw.J_of(om_))) / h1 ** 2
                   if certs <= 1.0 else float("nan"))
        rq_rows.append(dict(k=k, lam=float(lam[k]), q2=q2, q_record=float(qrec[k]), cert=certs))
        rq_ok = rq_ok and err <= floor_h + K_RICH * A1.C_FLOOR * A1.EPS * abs(J_rec) / h1 ** 2
        say("   direction %2d: lambda %+.4e, second difference of the frozen replay %+.4e (|d| %.1e);"
            " READING the record's %+.4e" % (k, lam[k], q2, err, qrec[k]))
    check("G-5a the secant spectrum is J's own: every eigenvalue against the second difference of"
          " the frozen replay along its direction at the same scale, inside the curvature floor"
          " + the rounding floor", rq_ok)
    hv_rows = rq_rows
    split = []
    for k in range(len(lam)):
        v = V[:, k]
        wp, ws = float(np.sum(v[:tw.np_] ** 2)), float(np.sum(v[tw.np_:] ** 2))
        same = float(np.sign(np.sum(v[:tw.np_])) * np.sign(np.sum(v[tw.np_:])))
        split.append((wp, ws, same))
    # identifiability on the SMALLER of the two curvatures (the frozen
    # model's and the record's, conservative); an uncertified record side
    # leaves the frozen one
    lam_id = np.where(np.isfinite(qrec), np.minimum(lam, qrec), lam)
    # IDENTIFIABILITY PER DIRECTION (S41 2026-09-26; the global floor
    # K_RICH x the Hessian's asymmetry was measured far too crude on the
    # arc posing: a direction of curvature 0.032, verified by J's own second
    # difference to 8.5e-4, read as "near-null" against a floor of 1.2):
    # each eigenvalue's floor is K_RICH x its OWN verified error (G-5a) plus
    # the rounding floor of the second difference; the global floor stays a
    # reading. The shape band is quoted in the design's units AND as the
    # wall displacement it makes (the design mixes knot heights, arc ends
    # and end slopes).
    err_k = np.array([abs(r["q2"] - r["lam"]) for r in rq_rows])
    floor_k = K_RICH * err_k + K_RICH * A1.C_FLOOR * A1.EPS * abs(J_rec) / h1 ** 2
    ident = lam_id > floor_k
    n_null = int(np.sum(np.abs(lam_id) <= floor_k))
    n_neg = int(np.sum(lam_id < -floor_k))
    t_band = np.where(ident, np.sqrt(2.0 * delta / np.where(ident, lam_id, 1.0)), np.inf)
    w_band = np.full(len(lam), np.inf)
    for k in range(len(lam)):
        if ident[k]:
            w_band[k] = max(wall_gap(tw, W0 + t_band[k] * V[:, k], W0))
        say("   direction %2d: lambda %+.4e (identifiability on %+.4e, floor %.1e)  band %s  plug %.2f /"
            " shroud %.2f  (%s)" % (k, lam[k], lam_id[k], floor_k[k],
                                    ("%.2e (design units) = %.2e m of wall" % (t_band[k], w_band[k]))
                                    if np.isfinite(t_band[k]) else "  none  ",
                                    split[k][0], split[k][1],
                                    "walls move together" if split[k][2] > 0 else "walls move apart"))
    say("   READING the global floor K_RICH x asymmetry %.2e would call %d direction(s) near-null"
        % (floor_h, int(np.sum(np.abs(lam_id) <= floor_h))))
    proj = V.T @ g0
    s_N = V[:, ident] @ (proj[ident] / lam_id[ident])
    dJ_N = float(0.5 * np.sum(proj[ident] ** 2 / lam_id[ident]))
    g_null = float(np.linalg.norm(proj[~ident]))
    say("   READING (stationarity by the model): the Newton step in the identifiable subspace"
        " |s|inf %.2e m (|s|2 %.2e), predicted gain %.2e of C_F (%.1f x delta); the gradient's"
        " share outside it %.2e of |grad| %.2e" % (np.max(np.abs(s_N)) if s_N.size else 0.0,
                                                    np.linalg.norm(s_N), dJ_N, dJ_N / delta,
                                                    g_null, np.linalg.norm(g0)))
    cond = float(lam[-1] / max(abs(lam[0]), np.finfo(float).tiny))
    check("G-5 DUTY-11 measured: %d identifiable, %d near-null, %d ascent direction(s) at their own"
          " verified floors (condition %.2e); the widest shape band %s of wall" %
          (int(np.sum(ident)), n_null, n_neg, cond,
           ("%.2e m" % np.max(w_band[ident])) if np.any(ident) else "none"), True)
    rec = dict(npass=list(NPASS), CF_ref=J_rec, CF_1d=tw.CF_1d, eps_i=tw.eps_i, e_rep=[e_p, e_s],
               cert=float(out["cert_worst"]), grad_ref=g0.tolist(), fd=rows,
               delta_ev=delta_ev, delta=delta, cert_ladder=lad, ell=ell, h_ok=h_ok, h_bad=h_bad,
               h_star=h_star, tr0=tr0, H=H.tolist(), lam=lam.tolist(), V=V.tolist(), asym=asym,
               floor=floor_h, dscale=dscale, H_ad=H_ad.tolist(), rayleigh=hv_rows, lam_id=lam_id.tolist(), n_null=n_null, n_neg=n_neg, ident=ident.tolist(),
               t_band=[float(x) for x in t_band], w_band=[float(x) for x in w_band], floor_k=floor_k.tolist(), s_newton=s_N.tolist(), dJ_newton=dJ_N,
               split=split, W_ref=W0.tolist(), kp=tw.kp.tolist(), ks=tw.ks.tolist(),
               n_plug=tw.np_)
    fn = os.path.join(ART, "derive_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return 0 if NPASS[0] == NPASS[1] else 1


def classderive():
    """STAGE class -- the fold class of the two-wall posing (S40, after the
    measurement that the unconstrained walks exploit folds): m_ref = the
    reference's own worst cell over the whole net, floors m_ref / 2^k
    (k = 1 .. rungs), rho = K_RICH ln(N) / the last floor, KS gap ln(N) /
    rho (the tournament's rules of record); C-1 the reference is in class;
    C-2 the KS brackets the minimum; REJECTOR C-R the unconstrained walk's
    landing of the 8-knot posing (it folds, and gained C_F above the 1-D
    ideal) read on this posing's knots is INFEASIBLE at every floor; C-S
    the class scale along +grad J (the first floor's crossing) -> the walk's
    trust radius tr0 = h*/K_RICH, floor tr0/K_RICH."""
    import glob
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    say("== [F3] the two-wall fold class [X-TWOP] (stage class) ==")
    tw = TwoWall()
    W0 = tw.W_ref.copy()
    rungs = int(CASES["class"]["rungs"])
    mg = tw.margin_dict(cells=True)
    out, S = tw.march_record(W0, margin=mg)
    v = mg["cells_out"][0]
    m_ref, Nc = float(out["margin_min"]), int(out["margin_n"])
    J0 = float(tw.J_of(out))
    if tw.fast or tw.pad:
        # C-F (S41): the record lane's speed switches (plug_march fast=,
        # margin pad=) against the legacy lane at the reference, BITWISE --
        # every cell, every decision, J, the KS and the minimum
        fast_, pad_ = tw.fast, tw.pad
        tw.fast, tw.pad = False, 0
        mgL = tw.margin_dict()
        t0 = time.time()
        oL, SL = tw.march_record(W0, margin=mgL)
        tL = time.time() - t0
        tw.fast, tw.pad = fast_, pad_
        t0 = time.time()
        oF, SF = tw.march_record(W0, margin=tw.margin_dict())
        tF = time.time() - t0
        # the two lanes solve the same cells to the same Newton tolerance; a
        # seed that differs in its last bits can stop Newton on the other
        # side of that tolerance (measured: bitwise at (140,31), max |dz|
        # 2.3e-11 at (280,61)), so the gate is the CERTIFICATE'S OWN BAND:
        # every cell within K_RICH x NEWTON_TOL_FACTOR x EPS x scale, the
        # decisions identical, J / KS / min within K_RICH x EPS x n_cells
        rz = max(float(np.max(np.abs(a - b))) / (A1.NEWTON_TOL_FACTOR * A1.EPS * max(1.0, float(np.max(np.abs(a)))))
                 for a, b in zip(SL.d["z"], SF.d["z"]))
        dz = max(float(np.max(np.abs(a - b))) for a, b in zip(SL.d["z"], SF.d["z"]))
        same_dec = (len(SL.d["z"]) == len(SF.d["z"]) and all(SL.d[k] == SF.d[k] for k in SL.d if k != "z"))
        rel = [abs(float(tw.J_of(oF)) / float(tw.J_of(oL)) - 1.0),
               abs(float(oF["margin_ks"]) - float(oL["margin_ks"])) / max(abs(float(oL["margin_ks"])), A1.EPS),
               abs(float(oF["margin_min"]) - float(oL["margin_min"])) / max(abs(float(oL["margin_min"])), A1.EPS)]
        tol_rel = K_RICH * A1.EPS * len(SF.d["z"])
        check("C-F the fast record lane (fast %s, pad %d) reproduces the legacy lane at the reference within the"
              " certificate's own band: %d cells, max |dz| %.1e = %.2f of the Newton tolerance (<= K_RICH),"
              " decisions identical %s, J / KS / min relative %.1e / %.1e / %.1e (<= %.1e); %.1f s against %.1f s"
              % (fast_, pad_, len(SF.d["z"]), dz, rz, same_dec, rel[0], rel[1], rel[2], tol_rel, tF, tL),
              same_dec and rz <= K_RICH and max(rel) <= tol_rel)
    check("C-1 the reference is in the fold class over the whole net (min cell %+.4f > 0, %d negative)"
          % (m_ref, int(np.sum(v <= 0))), m_ref > 0.0)
    if int(os.environ.get("TWOP_WORKERS", "1")) > 1:
        # H-P (S41): a Hessian column by the worker processes against the
        # same column in this process -- the parallel metric is the serial
        # one (the schedule at W0 is deterministic; the gradients are the
        # same computation in another process)
        h1_ = GATES["hess_steps"][0]
        t0 = time.time()
        Hp = secant_hessian_parallel(W0, h1_, int(os.environ["TWOP_WORKERS"]), "gate")
        tP = time.time() - t0
        _, S1 = tw.march_record(W0)
        t0 = time.time()
        Hc = secant_hessian(jax.grad(lambda z: tw.J_replay(z, S1)), W0, h1_, cols=[0, len(W0) - 1])
        tS = time.time() - t0
        dcol = max(float(np.max(np.abs(Hp[:, c] - Hc[:, c]))) for c in (0, len(W0) - 1))
        check("H-P the parallel secant Hessian (%d workers, %.0f s for %d columns) equals the in-process"
              " columns 0 and %d (max |dH| %.1e; %.0f s for the two)"
              % (int(os.environ["TWOP_WORKERS"]), tP, len(W0), len(W0) - 1, dcol, tS), dcol == 0.0)
    floors = [m_ref / 2 ** k for k in range(1, rungs + 1)]
    rho = K_RICH * np.log(Nc) / floors[-1]
    gap = np.log(Nc) / rho
    mg = tw.margin_dict(mu0=floors[0], rho=rho, m_ref=m_ref)
    o, S = tw.march_record(W0, margin=mg)
    ks = float(o["margin_ks"])
    check("C-2 KS brackets the minimum: %.6f <= KS %.6f <= %.6f (rho %.1f, gap %.2e)"
          % (m_ref - gap, ks, m_ref, rho, gap),
          m_ref - gap - K_RICH * A1.EPS * max(1.0, abs(m_ref)) <= ks
          <= m_ref + K_RICH * A1.EPS * max(1.0, abs(m_ref)))
    # the rejector: the unconstrained 8-knot landing on these knots
    fw = sorted(glob.glob(os.path.join(ART, CASES["class"]["rejector_walk"])))
    rej = None
    if fw:
        m_keep = (POSE["m_plug"], POSE["m_shroud"])
        POSE["m_plug"], POSE["m_shroud"] = CASES["class"]["rejector_knots"], CASES["class"]["rejector_knots"]
        t8 = TwoWall(verbose=False)
        POSE["m_plug"], POSE["m_shroud"] = m_keep
        W8 = np.asarray(json.load(open(fw[-1]))["W"], float)
        Wr = tw.on_knots(W8, t8)
        orr, _ = tw.march_record(Wr, margin=mg)
        ksr = float(orr["margin_ks"])
        rej = dict(ks=ksr, min=float(orr["margin_min"]), CF=float(tw.J_of(orr)), cert=float(orr["cert_worst"]))
        say("   READING the unconstrained 8-knot landing (C_F %.6f above the 1-D %.6f) read on these knots:"
            " KS %+.4f, min cell %+.4f, C_F here %.6f, %s at the first floor"
            % (json.load(open(fw[-1]))["CF"], tw.CF_1d, ksr, rej["min"], rej["CF"],
               "INFEASIBLE" if ksr < floors[0] else "feasible"))
    J_g, g0 = jax.value_and_grad(lambda z: tw.J_replay(z, S))(jnp.asarray(W0))
    g0 = np.asarray(g0)
    u = g0 / np.linalg.norm(g0)
    ell = float(tw.sx[-1] - tw.x0) / len(tw.sx)
    # READING the class scale along +grad J at the reference (the walk
    # derives its radius at its own start: here the gradient is noise)
    h_ok, h_bad, lad = None, None, []
    for k in CASES["walk"]["ladder_k"]:
        h = ell * 2.0 ** k
        oh, _ = tw.march_record(W0 + h * u, margin=mg)
        ch, kh = float(oh["cert_worst"]), float(oh["margin_ks"])
        lad.append(dict(h=h, cert=ch, ks=kh, CF=float(tw.J_of(oh))))
        say("    h %.3e m: C_F %.9f (%+.2e), KS %+.4f, min %+.4f, cert %.3e"
            % (h, float(tw.J_of(oh)), float(tw.J_of(oh)) - J0, kh, float(oh["margin_min"]), ch))
        ok_h = np.isfinite(ch) and ch <= 1.0 and kh >= floors[0]
        if ok_h:
            h_ok = h
        elif h_bad is None:
            h_bad = h
        if h_ok is not None and h_bad is not None and h_bad > h_ok:
            break
    bracketed = h_ok is not None and h_bad is not None and h_bad > h_ok
    say("   READING the class along +grad J at the reference: bracket [%s, %s] m" % (h_ok, h_bad))
    # the rejector: the UNCONSTRAINED ascent's first move OUT of the class
    # along +grad J (the ladder's h_bad -- at the reference the gradient is
    # knot-scale zig-zag and the break sits at the same 0.17-0.33 mm on
    # both rungs, measured) must be infeasible at EVERY floor, not only
    # the first (S41: the S40 fixed step ell 2^-5 fell below the break at
    # the fine rung, where ell halves)
    if bracketed:
        orj, _ = tw.march_record(W0 + h_bad * u, margin=mg)
        kr = float(orj["margin_ks"])
        check("C-R REJECTOR the unconstrained ascent's first move out of the class (%.2e m along +grad J,"
              " C_F %+.2e) is INFEASIBLE at every floor (KS %+.4f, min cell %+.4f)"
              % (h_bad, float(tw.J_of(orj)) - J0, kr, float(orj["margin_min"])), all(kr < f_ for f_ in floors))
    else:
        check("C-R REJECTOR: the class never breaks along +grad J inside the ladder -- no rejector", False)
    h_star = float(np.sqrt(h_ok * h_bad)) if bracketed else float("nan")
    tr0 = h_star / K_RICH
    say("   floors %s; rho %.1f; gap %.2e; h* %.3e m -> tr0 %.3e m, floor %.3e m"
        % (np.array2string(np.array(floors), precision=4), rho, gap, h_star, tr0, tr0 / K_RICH))
    rec = dict(npass=list(NPASS), m=[len(tw.kp), len(tw.ks)], kernel=tw.kernel, kmode=tw.kmode, K=tw.K, N=tw.N, CF_ref=J0, CF_1d=tw.CF_1d, m_ref=m_ref,
               N_cells=Nc, floors=floors, rho=rho, gap=gap, rejector=rej, ladder=lad, h_ok=h_ok,
               h_bad=h_bad, h_star=h_star, tr0=tr0, W_ref=W0.tolist(), grad_ref=g0.tolist(),
               seconds=time.time() - t00)
    fn = os.path.join(ART, "class_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return 0 if NPASS[0] == NPASS[1] else 1


def wall_gap(tw, W1, W2):
    """max |dy| over the frozen stations, plug and shroud separately (the
    stations are linear in W)."""
    (_, a1, _), (_, b1, _) = tw.walls(np.asarray(W1, float))
    (_, a2, _), (_, b2, _) = tw.walls(np.asarray(W2, float))
    return (float(np.max(np.abs(np.asarray(a1) - np.asarray(a2)))),
            float(np.max(np.abs(np.asarray(b1) - np.asarray(b2)))))


def chord(tw):
    """The generic start: both walls straight from the uniform inlet to the
    pinned ends, read at the knots (it knows nothing of Migdal's curves)."""
    if tw.kernel:
        yp = tw.ya_p + (tw.tip - tw.ya_p) * (tw.kp[:-1] - tw.xa_p) / (tw.kp[-1] - tw.xa_p)
        ys = tw.ya_s + (tw.lip - tw.ya_s) * (tw.ks[:-1] - tw.xa_s) / (tw.ks[-1] - tw.xa_s)
        return np.r_[yp, ys]
    yp = tw.y_l + (tw.tip - tw.y_l) * (tw.kp[:-1] - tw.x0) / (tw.kp[-1] - tw.x0)
    ys = tw.y_u + (tw.lip - tw.y_u) * (tw.ks[:-1] - tw.x0) / (tw.ks[-1] - tw.x0)
    return np.r_[yp, ys]


def hermite_start(tw):
    """A generic straightening start of the kernel posing: each wall the
    cubic Hermite from its arc end (point, slope) to its pinned end with an
    axial exit (slope 0), read at the knots -- posing data only, nothing of
    Migdal's contour. Measured S40: in full it folds (a generic contour
    1 cm off Migdal's carries coalescing compressions), halfway from the
    reference it is in class."""
    def herm(x, xa, ya, sa, xb, yb, sb):
        h = xb - xa
        t = (x - xa) / h
        return ((2 * t ** 3 - 3 * t ** 2 + 1) * ya + (t ** 3 - 2 * t ** 2 + t) * h * sa
                + (-2 * t ** 3 + 3 * t ** 2) * yb + (t ** 3 - t ** 2) * h * sb)
    return np.r_[herm(tw.kp[:-1], tw.xa_p, tw.ya_p, tw.sa_p, tw.kp[-1], tw.tip, 0.0),
                 herm(tw.ks[:-1], tw.xa_s, tw.ya_s, tw.sa_s, tw.ks[-1], tw.lip, 0.0)]


class Metric:
    """The two-wall posing seen in NEWTON variables z: W = W_s + T z with
    T = V diag(lam_eff^-1/2) from the secant Hessian AT THE WALK'S OWN
    START (-H = V diag(lam) V^T, lam floored at K_RICH x its asymmetry),
    so that the curvature of J at the start is the identity in z. The
    record driver sees the same three hooks; W is linear in z, so the
    march, the class margin and their adjoints are the posing's own. The
    metric shapes the path only: a KKT point of the walk is one in W."""

    def __init__(self, tw, Ws, T):
        self.tw, self.Ws, self.T = tw, np.asarray(Ws, float), np.asarray(T, float)

    def W(self, Z):
        return jnp.asarray(self.Ws) + jnp.asarray(self.T) @ jnp.asarray(Z)

    def march_record(self, Z, margin=None):
        return self.tw.march_record(self.Ws + self.T @ np.asarray(Z, float), margin=margin)

    def J_replay(self, Z, sched):
        return self.tw.J_replay(self.W(Z), sched)

    def margin_replay(self, Z, sched, margin):
        return self.tw.margin_replay(self.W(Z), sched, margin)


def secant_hessian(gfun, W0, h, cols=None):
    """Central differences of the exact reverse gradient at scale h (the
    G-5 instrument), unsymmetrised; cols = the columns to compute (all)."""
    n = len(W0)
    H = np.zeros((n, n))
    for j in (range(n) if cols is None else cols):
        e = np.zeros(n)
        e[j] = h
        H[:, j] = (np.asarray(gfun(jnp.asarray(W0 + e))) - np.asarray(gfun(jnp.asarray(W0 - e)))) / (2.0 * h)
    return H


def secant_hessian_parallel(W0, h, workers, tag):
    """The 2n gradients of the secant Hessian are independent: TWOP_WORKERS
    > 1 spreads the columns over that many worker PROCESSES (stage hesscol,
    this file, the same environment: posing, rung, lanes), each recording
    the schedule at W0 itself (deterministic: the same schedule) and
    writing its columns; the parent assembles H. Serial (workers <= 1) is
    the in-process loop, unchanged. Column values do not depend on the
    process (verified by the gate H-P of stage class)."""
    import subprocess
    n = len(W0)
    d = os.path.join(ART, "_hess_%s" % tag)
    os.makedirs(d, exist_ok=True)
    np.save(os.path.join(d, "W0.npy"), np.asarray(W0, float))
    chunks = [list(range(n))[k::workers] for k in range(workers)]
    procs = []
    for k, cols in enumerate(chunks):
        if not cols:
            continue
        env = dict(os.environ, TWOP_STAGE="hesscol", TWOP_HESS_DIR=d, TWOP_HESS_H=repr(float(h)),
                   TWOP_HESS_COLS=",".join(str(c) for c in cols), TWOP_HESS_ID=str(k),
                   XLA_FLAGS=os.environ.get("XLA_FLAGS", "") + " --xla_cpu_multi_thread_eigen=false intra_op_parallelism_threads=4",
                   MALLOC_ARENA_MAX="2")
        procs.append(subprocess.Popen([sys.executable, "-B", "-W", "ignore", os.path.abspath(__file__)], env=env,
                                      stdout=open(os.path.join(d, "worker_%d.log" % k), "w"), stderr=subprocess.STDOUT))
    for pr in procs:
        pr.wait()
    H = np.zeros((n, n))
    done = np.zeros(n, bool)
    for k, cols in enumerate(chunks):
        if not cols:
            continue
        fn = os.path.join(d, "cols_%d.npz" % k)
        if not os.path.exists(fn):
            raise RuntimeError("Hessian worker %d wrote nothing (see %s)" % (k, os.path.join(d, "worker_%d.log" % k)))
        Z = np.load(fn)
        for c, col in zip(Z["cols"], Z["H"].T):
            H[:, int(c)] = col
            done[int(c)] = True
    if not done.all():
        raise RuntimeError("Hessian columns missing: %s" % np.where(~done)[0])
    return H


def hesscol():
    """STAGE hesscol (a worker of secant_hessian_parallel): the columns
    TWOP_HESS_COLS of the secant Hessian at W0 (TWOP_HESS_DIR/W0.npy), scale
    TWOP_HESS_H, on the schedule recorded at W0 in this process."""
    d = os.environ["TWOP_HESS_DIR"]
    W0 = np.load(os.path.join(d, "W0.npy"))
    h = float(os.environ["TWOP_HESS_H"])
    cols = [int(c) for c in os.environ["TWOP_HESS_COLS"].split(",")]
    tw = TwoWall(verbose=False)
    _, S = tw.march_record(W0)
    gfun = jax.grad(lambda z: tw.J_replay(z, S))
    t0 = time.time()
    H = secant_hessian(gfun, W0, h, cols=cols)
    np.savez(os.path.join(d, "cols_%s.npz" % os.environ["TWOP_HESS_ID"]), cols=np.array(cols), H=H[:, cols])
    print("worker %s: columns %s in %.0f s" % (os.environ["TWOP_HESS_ID"], cols, time.time() - t0), flush=True)
    return 0


def arc_start(tw):
    """A generic start of the ARC posing: each wall's arc with its radius
    scaled by arc.start_R_scale at the reference's end angle (a different
    kernel), the downstream wall the cubic Hermite from that arc's end
    (point, slope) to the pinned end with an axial exit, read at the knots
    placed on the new [x_a, end] -- nothing of Migdal's contour after the
    arc."""
    sc = float(CASES["arc"]["start_R_scale"])
    W = []
    arcs = []
    for xa0, ta, y0, sgn, frac, xe, ye in ((tw.xa_p, abs(tw.sa_p), tw.y_l, -1.0, tw.fp, tw.kp[-1], tw.tip),
                                           (tw.xa_s, abs(tw.sa_s), tw.y_u, 1.0, tw.fs, tw.ks[-1], tw.lip)):
        xa = tw.x0 + sc * (xa0 - tw.x0)
        _, R, ya, sa = (float(v) for v in tw.arc_of(jnp.float64(xa), jnp.float64(ta), y0, sgn))
        xk = xa + (xe - xa) * frac[:-1]
        h = xe - xa
        t = (xk - xa) / h
        W.append((2 * t ** 3 - 3 * t ** 2 + 1) * ya + (t ** 3 - 2 * t ** 2 + t) * h * sa
                 + (-2 * t ** 3 + 3 * t ** 2) * ye)
        arcs += [xa, ta]
    return np.r_[W[0], W[1], arcs[0], arcs[1], arcs[2], arcs[3]]


def walk():
    """STAGE walk -- RE-1 on the two-wall posing: the record driver
    (a1_plug_spline_opt.run_trsqp, backtracking) WITH the fold class of the
    stage-class record (KS >= mu0_1 - gap on the frozen schedule; the S40
    measurement: without it the walk from the reference gains C_F above the
    1-D ideal by folding the internal channel) from TWOP_START = A (the
    reference) or G (the chord from the kernel's arc ends to the pinned
    ends, or the largest certified IN-CLASS ramp from the reference toward
    it, declared). RADIUS derived at the walk's OWN start: the class scale
    along its +grad J (the first break of certified-and-in-class on the
    ladder ell 2^k), tr0 = h*/K_RICH, floor tr0/K_RICH -- the tournament's
    rule taken at the start, because at the reference (a flat optimum) the
    gradient is dominated by knot-scale zig-zags that fold within 0.3 mm
    (measured). Budget TWOP_SEGS x TWOP_ITERS; backtrack PSPL_BACKTRACK."""
    import glob
    import a1_plug_spline_opt as P
    t00 = time.time()
    start = os.environ.get("TWOP_START", "A")
    segs = int(os.environ.get("TWOP_SEGS", 12))
    iters = int(os.environ.get("TWOP_ITERS", 8))
    bt = int(os.environ.get("PSPL_BACKTRACK", 4))
    say("== [F3] the two-wall walk, start %s, class-constrained [X-TWOP] (stage walk) ==" % start)
    tw = TwoWall()
    fc = sorted(glob.glob(os.path.join(ART, "class_20*.json")))
    Cr = json.load(open(os.environ.get("TWOP_CLASS", fc[-1])))
    if (Cr["m"] != [len(tw.kp), len(tw.ks)] or not Cr.get("kernel", False) == tw.kernel
            or Cr.get("kmode", "data" if Cr.get("kernel", False) else "free") != tw.kmode
            or (Cr.get("K", tw.K), Cr.get("N", tw.N)) != (tw.K, tw.N)):
        raise ValueError("the class record %s is not this posing's" % fc[-1])
    floors, rho, gap, m_ref = Cr["floors"], Cr["rho"], Cr["gap"], Cr["m_ref"]
    mg0 = tw.margin_dict(mu0=floors[0], rho=rho, m_ref=m_ref)
    mg0["tol"] = gap
    W_ref = tw.W_ref.copy()
    o_ref, _ = tw.march_record(W_ref)
    CF_ref = float(tw.J_of(o_ref))

    def in_class(W):
        o_, s_ = tw.march_record(W, margin=tw.margin_dict(mu0=floors[0], rho=rho, m_ref=m_ref))
        c_, k_ = float(o_["cert_worst"]), float(o_["margin_ks"])
        return (np.isfinite(c_) and c_ <= 1.0 and k_ >= floors[0] - gap), o_, s_, c_, k_

    if start == "A":
        Ws, lam_r = W_ref.copy(), 0.0
    else:
        Wc = arc_start(tw) if start == "R" else (hermite_start(tw) if start == "H" else chord(tw))
        Ws, lam_r = None, None
        for lam_ in CASES["walk"]["ramps"]:
            Wt = W_ref + lam_ * (Wc - W_ref)
            ok_, ot, _, ct, kt = in_class(Wt)
            say("   ramp %.2f toward the generic start: cert %.3e, KS %+.4f (floor %.4f), C_F %.6f, gap to the"
                " reference plug %.3e / shroud %.3e m" % (lam_, ct, kt, floors[0], float(tw.J_of(ot)),
                                                         *wall_gap(tw, Wt, W_ref)))
            if ok_:
                Ws, lam_r = Wt, lam_
                break
        if Ws is None:
            say("   no certified in-class generic start on the ramp: nothing to walk")
            return 1
    ok0, o0, S0, c0, k0 = in_class(Ws)
    gp0, gs0 = wall_gap(tw, Ws, W_ref)
    # the radius at the start: the class scale along +grad J
    J_s, g_s = jax.value_and_grad(lambda z: tw.J_replay(z, S0))(jnp.asarray(Ws))
    g_s = np.asarray(g_s)
    metric = os.environ.get("TWOP_METRIC", "")
    ck = os.path.join(ART, "walk_%sN_checkpoint.json" % start)
    C0 = None
    if os.environ.get("TWOP_RESUME") and os.path.exists(ck):
        C0 = json.load(open(ck))
        if C0["W_start"] != Ws.tolist():
            C0 = None
    if metric == "start" and C0 is not None and "T" in C0:
        T = np.array(C0["T"])
        say("   NEWTON METRIC read from the checkpoint (the secant Hessian at this start, computed once)")
        dN = T @ (T.T @ g_s)
        u = dN / np.linalg.norm(dN)
    elif metric == "start":
        t_m = time.time()
        nw_ = int(os.environ.get("TWOP_WORKERS", "1"))
        Hs = (secant_hessian_parallel(Ws, GATES["hess_steps"][0], nw_, "metric_%s" % start) if nw_ > 1
              else secant_hessian(jax.grad(lambda z: tw.J_replay(z, S0)), Ws, GATES["hess_steps"][0]))
        asym_m = float(np.max(np.abs(Hs - Hs.T)))
        lam_m, V_m = np.linalg.eigh(-0.5 * (Hs + Hs.T))
        floor_m = K_RICH * asym_m
        lam_eff = np.maximum(lam_m, floor_m)
        T = V_m @ np.diag(lam_eff ** -0.5)
        say("   NEWTON METRIC at the start (secant Hessian at h %.0e, %.0f s): asymmetry %.2e -> floor"
            " %.2e; eigenvalues of -H %s (%d floored)" % (GATES["hess_steps"][0], time.time() - t_m,
                                                          asym_m, floor_m, np.array2string(lam_m, precision=3),
                                                          int(np.sum(lam_m < floor_m))))
        dN = T @ (T.T @ g_s)
        u = dN / np.linalg.norm(dN)
    else:
        u = g_s / np.linalg.norm(g_s)
    ell = float(tw.sx[-1] - tw.x0) / len(tw.sx)
    h_ok, h_bad = None, None
    for k in CASES["walk"]["ladder_k"]:
        h = ell * 2.0 ** k
        okh, oh, _, ch, kh = in_class(Ws + h * u)
        say("    start ladder h %.3e m: C_F %+.3e, KS %+.4f, cert %.3e -> %s"
            % (h, float(tw.J_of(oh)) - float(tw.J_of(o0)), kh, ch, "in class" if okh else "OUT"))
        if okh:
            h_ok = h
        elif h_bad is None:
            h_bad = h
        if h_ok is not None and h_bad is not None and h_bad > h_ok:
            break
    if h_ok is None or h_bad is None or h_bad <= h_ok:
        say("   the class scale is not bracketed at the start: no radius, nothing to walk")
        return 1
    tr0 = float(np.sqrt(h_ok * h_bad)) / K_RICH
    say("   start %s (ramp %.2f): C_F %.9f, cert %.3e, KS %+.4f; gap to the reference plug %.3e / shroud"
        " %.3e m; class scale h* %.3e m -> tr0 %.3e m, floor %.3e m; %d segments x %d iterations,"
        " backtrack %d" % (start, lam_r, float(tw.J_of(o0)), c0, k0, gp0, gs0, tr0 * K_RICH, tr0,
                           tr0 / K_RICH, segs, iters, bt))
    if metric == "start":
        # the radius in z: the W-scale h* along the Newton direction over
        # the W-length of a unit z-step along it
        zlen = float(np.linalg.norm(T @ (T.T @ g_s)) / np.linalg.norm(T.T @ g_s))
        tr0_z = tr0 / zlen
        say("   Newton walk in z: a unit z-step along the Newton direction moves the walls %.3e m ->"
            " tr0 %.3e (z), floor %.3e (z)" % (zlen, tr0_z, tr0_z / K_RICH))
        # CHECKPOINTED (S41): the driver calls back at the top of every
        # segment with its certified incumbent; the walk writes it to disk
        # (with the Newton metric T and the radius) and CLEARS jax's
        # compilation caches -- a walk accumulates compiled executables
        # (every march has its own cell count, every count a new set of
        # shapes) and died at the kernel's memory-mapping cap 65530
        # (measured 2026-09-26: 32742 mappings after two segments; 31912 ->
        # 1667 after clearing). TWOP_RESUME=1 restarts from the checkpoint's
        # incumbent with its radius and its metric (no second Hessian).
        Z0, seg0, tr_z = np.zeros(len(Ws)), 0, tr0_z
        if C0 is not None:
            Z0, seg0, tr_z = np.array(C0["Z"]), int(C0["segments"]), float(C0.get("tr", tr0_z))
            say("   RESUMED from the checkpoint: %d segments done, C_F %.9f, radius %.3e (z)"
                % (seg0, C0["CF"], tr_z))
        n_maps = lambda: sum(1 for _ in open("/proc/self/maps"))     # noqa: E731
        say("   memory mappings at the walk's start: %d (cap 65530)" % n_maps())
        pre = Metric(tw, Ws, T)

        def on_segment(seg, W_best, tr):
            if W_best is None:
                return
            Zb = np.asarray(W_best, float)
            oc, _ = tw.march_record(Ws + T @ Zb)
            json.dump(dict(W_start=Ws.tolist(), Z=Zb.tolist(), W=(Ws + T @ Zb).tolist(),
                           CF=float(tw.J_of(oc)), segments=seg0 + seg, tr=float(tr), tr0_z=tr0_z,
                           T=T.tolist()), open(ck, "w"), indent=1)
            m_before = n_maps()
            # the caches are cleared only near the cap (S41: with the
            # wavefront replay the compiled steps ARE the speed -- ~38k
            # mappings that recur at every segment -- and clearing them
            # cost a 2-4 min recompile per segment, measured on the first
            # fine-rung walks)
            if m_before > int(CASES["wavefront"]["map_clear"]):
                jax.clear_caches()
            say("   checkpoint at segment %d: C_F %.9f; mappings %d -> %d (cleared above %d)"
                % (seg0 + seg, float(tw.J_of(oc)), m_before, n_maps(), int(CASES["wavefront"]["map_clear"])))

        Zf, hist, n_rec = P.run_trsqp(Z0, {}, dict(throat=pre), tw.ta, sign=+1.0,
                                      max_segments=segs - seg0, maxiter_per_seg=iters, margin=mg0,
                                      tr0=tr_z, tr_floor=tr0_z / K_RICH, bounds=None, backtrack=bt,
                                      on_segment=on_segment)
        Z = np.asarray(Zf, float)
        Wf = Ws + T @ Z
    else:
        c = dict(throat=tw)
        Wf, hist, n_rec = P.run_trsqp(Ws, {}, c, tw.ta, sign=+1.0, max_segments=segs,
                                      maxiter_per_seg=iters, margin=mg0, tr0=tr0,
                                      tr_floor=tr0 / K_RICH, bounds=None, backtrack=bt)
    Wf = np.asarray(Wf, float)
    okf, of, Sf, cf, kf = in_class(Wf)
    Jf = float(tw.J_of(of))
    gf = np.asarray(jax.grad(lambda z: tw.J_replay(z, Sf))(jnp.asarray(Wf)))
    gp, gs = wall_gap(tw, Wf, W_ref)
    say("   return: C_F %.9f (start %.9f, reference %.9f, 1-D %.6f), cert %.3e, KS %+.4f (%s),"
        " |grad|inf %.3e; gap to the reference plug %.3e / shroud %.3e m (start %.3e / %.3e);"
        " %d records, %.0f s" % (Jf, float(tw.J_of(o0)), CF_ref, tw.CF_1d, cf, kf,
                                 "in class" if okf else "OUT of class", float(np.max(np.abs(gf))),
                                 gp, gs, gp0, gs0, n_rec, time.time() - t00))
    rec = dict(start=start, ramp=lam_r, W_start=Ws.tolist(), W=Wf.tolist(), CF=Jf,
               CF_start=float(tw.J_of(o0)), CF_ref=CF_ref, cert=cf, ks=kf, in_class=bool(okf),
               grad=gf.tolist(), gap_ref=[gp, gs], gap_ref_start=[gp0, gs0], records=n_rec,
               segments=len(hist), seconds=time.time() - t00, tr0=tr0, backtrack=bt, segs=segs,
               iters=iters, counters=dict(mg0.get("counters", {})), metric=metric)
    fn = os.path.join(ART, "walk_%s%s_%s.json" % (start, "N" if metric == "start" else "",
                                                   time.strftime("%Y-%m-%d")))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    return 0


def grade():
    """STAGE grade -- RE-1 on the kernel posing, class-constrained walks of
    record: A from the reference, H from the generic Hermite start (the
    largest in-class ramp). RE-0 both landings certified and IN CLASS;
    RE-1 VALUE (paired, same grid): |C_F(H) - C_F(A)| <= K_RICH x delta;
    RE-1 SHAPE: along every IDENTIFIABLE eigen-direction of the kernel
    posing's secant spectrum (the derive of record, G-5)
    |v_k . (W_H - W_A)| <= K_RICH x its shape band; the directions the
    spectrum cannot identify are reported, never graded. Reading: each
    landing's wall gap to the reference (Migdal's straightening at the
    knots)."""
    import glob
    t00 = time.time()
    fns = sorted(glob.glob(os.path.join(ART, "derive_20*.json")))
    D = json.load(open(os.environ.get("TWOP_DERIVE", fns[-1])))
    say("== [F3] the two-wall re-obtention: RE-1 on the kernel posing [X-TWOP] (stage grade) ==")
    say("   derive of record: %s (%d/%d PASS; delta %.3e)" % (fns[-1], D["npass"][0], D["npass"][1],
                                                           D["delta"]))
    wk = {}
    vs = os.environ.get("TWOP_GRADE_VS", "HN")
    for st, tag in (("A", os.environ.get("TWOP_GRADE_A", "A")), ("H", vs)):
        fw = sorted(glob.glob(os.path.join(ART, "walk_%s_20*.json" % tag)))
        if not fw and tag == "A":
            fw = sorted(glob.glob(os.path.join(ART, "walk_AN_20*.json")))   # the Newton walk from A
        wk[st] = json.load(open(fw[-1]))
        say("   walk %s: %s -- C_F %.9f (start %.9f), cert %.3e, KS %+.4f (%s), gap to the reference plug"
            " %.3e / shroud %.3e m (start %.3e / %.3e), %d records, %.0f s"
            % (st, fw[-1], wk[st]["CF"], wk[st]["CF_start"], wk[st]["cert"], wk[st]["ks"],
               "in class" if wk[st]["in_class"] else "OUT", *wk[st]["gap_ref"], *wk[st]["gap_ref_start"],
               wk[st]["records"], wk[st]["seconds"]))
    check("RE-0 both landings certified and in class (%.3e / %.3e; %s / %s)"
          % (wk["A"]["cert"], wk["H"]["cert"], wk["A"]["in_class"], wk["H"]["in_class"]),
          max(wk["A"]["cert"], wk["H"]["cert"]) <= 1.0 and wk["A"]["in_class"] and wk["H"]["in_class"])
    dJ = wk["H"]["CF"] - wk["A"]["CF"]
    check("RE-1 VALUE (paired): |C_F(H) - C_F(A)| %.3e <= K_RICH x delta %.3e (the start was %.3e below)"
          % (abs(dJ), K_RICH * D["delta"], wk["A"]["CF"] - wk["H"]["CF_start"]),
          abs(dJ) <= K_RICH * D["delta"])
    V = np.array(D["V"])
    lam = np.array(D["lam_id"])
    ident = np.array(D["ident"], bool)
    tb = np.array(D["t_band"], float)
    dW = np.array(wk["H"]["W"]) - np.array(wk["A"]["W"])
    dW0 = np.array(wk["H"]["W_start"]) - np.array(wk["A"]["W"])
    a = V.T @ dW
    a0 = V.T @ dW0
    ok = True
    for k in range(len(lam)):
        r = abs(a[k]) / (K_RICH * tb[k]) if ident[k] else float("nan")
        if ident[k]:
            ok = ok and r <= 1.0
        say("   direction %2d (curvature %+.3e): |a| %.3e (start %.3e)  %s"
            % (k, lam[k], abs(a[k]), abs(a0[k]),
               ("band K_RICH x %.2e -> %.2f" % (tb[k], r)) if ident[k] else "not identifiable: reported"))
    check("RE-1 SHAPE: the generic start's landing coincides with the reference's along every"
          " identifiable direction (%d of %d)" % (int(np.sum(ident)), len(lam)), ok)
    tw = TwoWall(verbose=False)
    gp, gs = wall_gap(tw, wk["H"]["W"], wk["A"]["W"])
    say("   READING the two landings apart by plug %.3e / shroud %.3e m in the walls (H started %.3e / %.3e"
        " from the reference)" % (gp, gs, *wk["H"]["gap_ref_start"]))
    arcs = None
    if tw.kmode == "arc":
        # the arcs the two walks chose, in physical units, and the reference's
        def arc_read(W):
            xa_p, ta_p, xa_s, ta_s = (float(v) for v in np.asarray(W)[-4:])
            out = []
            for xa, ta in ((xa_p, ta_p), (xa_s, ta_s)):
                out += [xa, (xa - tw.x0) * np.sqrt(1.0 + ta * ta) / ta, np.degrees(np.arctan(ta))]
            return out
        arcs = {k: arc_read(v["W"]) for k, v in wk.items()}
        arcs["ref"] = arc_read(tw.W_ref)
        say("   ARCS (x_end m, radius m, end angle deg -- plug | shroud):")
        for k, ar in arcs.items():
            say("      %-4s plug %.4f  R %.4f  %.2f deg | shroud %.4f  R %.4f  %.2f deg"
                % (k, ar[0], ar[1], ar[2], ar[3], ar[4], ar[5]))
        say("   the two walks' arcs differ by: plug end %.2e m, R %.2e m, angle %.3f deg | shroud end %.2e m,"
            " R %.2e m, angle %.3f deg" % tuple(abs(arcs["H"][i] - arcs["A"][i]) for i in range(6)))
    rec = dict(npass=list(NPASS), dCF=dJ, a=a.tolist(), a_start=a0.tolist(), gap_HA=[gp, gs], arcs=arcs,
               walks={k: dict(CF=v["CF"], cert=v["cert"], ks=v["ks"], gap_ref=v["gap_ref"]) for k, v in wk.items()})
    fn = os.path.join(ART, "grade_%s.json" % time.strftime("%Y-%m-%d"))
    json.dump(rec, open(fn, "w"), indent=1, default=float)
    say("   record: %s" % fn)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return 0 if NPASS[0] == NPASS[1] else 1


def wavefront():
    """STAGE wavefront (S41): the anti-diagonal replay against the
    sequential replay at the reference of the current posing and rung --
    WF-1 J, WF-2 its gradient, WF-3 the class margin and its gradient,
    each within K_RICH x EPS x n_cells of the sequential value (bitwise
    reported), and the timings."""
    t00 = time.time()
    os.makedirs(ART, exist_ok=True)
    say("== [F3] the wavefront replay against the sequential replay [X-TWOP] (stage wavefront) ==")
    tw = TwoWall()
    tw.wavefront = True
    W0 = tw.W_ref.copy()
    mg = tw.margin_dict()
    t0 = time.time()
    out, S = tw.march_record(W0, margin=mg)
    say("   record with the graph: %.1f s; %d cells in %d levels (%d batches); %d quads"
        % (time.time() - t0, S.plan["n_cells"], S.plan["n_levels"], len(S.plan["batches"]), S.plan["quads"].shape[0]))
    tol = K_RICH * A1.EPS * S.plan["n_cells"]
    rows = {}
    for name, wf in (("sequential", False), ("wavefront", True), ("wavefront-2", True)):
        t0 = time.time()
        J, g = jax.value_and_grad(lambda z: tw.J_replay(z, S, wavefront=wf))(jnp.asarray(W0))
        g.block_until_ready()
        tJ = time.time() - t0
        t0 = time.time()
        m, gm = jax.value_and_grad(lambda z: tw.margin_replay(z, S, mg, wavefront=wf))(jnp.asarray(W0))
        gm.block_until_ready()
        tm = time.time() - t0
        rows[name] = (float(J), np.asarray(g), float(m), np.asarray(gm), tJ, tm)
        say("   %-10s J %.15g (%.1f s with its gradient), KS - mu0 %.15g (%.1f s with its gradient)"
            % (name, float(J), tJ, float(m), tm))
    a, b = rows["sequential"], rows["wavefront-2"]      # the steady state (the first call compiles)
    dJ = abs(b[0] / a[0] - 1.0)
    dg = float(np.max(np.abs(b[1] - a[1]))) / max(float(np.max(np.abs(a[1]))), A1.EPS)
    dm = abs(b[2] - a[2]) / max(abs(a[2]), A1.EPS)
    dgm = float(np.max(np.abs(b[3] - a[3]))) / max(float(np.max(np.abs(a[3]))), A1.EPS)
    check("WF-1 J: wavefront = sequential to %.1e relative (<= %.1e; bitwise %s)" % (dJ, tol, b[0] == a[0]), dJ <= tol)
    check("WF-2 grad J: max relative difference %.1e (<= %.1e; bitwise %s)"
          % (dg, tol, bool(np.array_equal(a[1], b[1]))), dg <= tol)
    check("WF-3 the class margin %.1e and its gradient %.1e (<= %.1e; bitwise %s / %s)"
          % (dm, dgm, tol, b[2] == a[2], bool(np.array_equal(a[3], b[3]))), max(dm, dgm) <= tol)
    say("   speed-up (steady state, the second wavefront call): J + grad %.1fx, margin + grad %.1fx; the"
        " first call (compiling the padded batches) %.1f / %.1f s"
        % (a[4] / b[4], a[5] / b[5], rows["wavefront"][4], rows["wavefront"][5]))
    json.dump(dict(npass=list(NPASS), K=tw.K, N=tw.N, kmode=tw.kmode, n_cells=S.plan["n_cells"],
                   n_levels=S.plan["n_levels"], dJ=dJ, dg=dg, dm=dm, dgm=dgm, tol=tol,
                   t_seq=[a[4], a[5]], t_wf=[b[4], b[5]]),
              open(os.path.join(ART, "wavefront_K%d_N%d_%s.json" % (tw.K, tw.N, time.strftime("%Y-%m-%d"))), "w"), indent=1)
    say("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1], time.time() - t00))
    return 0 if NPASS[0] == NPASS[1] else 1


if __name__ == "__main__":
    sys.exit({"derive": derive, "class": classderive, "walk": walk,
              "grade": grade, "hesscol": hesscol,
              "wavefront": wavefront}[os.environ.get("TWOP_STAGE", "derive")]())

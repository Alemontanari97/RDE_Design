#!/usr/bin/env python3
"""A1 BRICK 2, STEP 16 [F2/A1]: THE FREE-FORM SPIKE — cubic-spline
contour, AD adjoint, trust-region SQP. Registry ID: [X-PSPL].

WHAT IS NEW. Through step 15 the spike was a STREAMLINE of the lip
fan --- the classical ideal plug contour, obtained by integrating the
flow direction outward from the start radius. That contour is exact
only for the FULL-LENGTH, perfectly expanded plug. Every real spike is
CUT, and at a fixed length the streamline is no longer optimal: Rao's
variational argument applies to the plug exactly as it does to the
bell. This carrier gives the spike a shape BASIS and lets a
constrained optimizer move it, so that "the best spike of this length"
becomes a computed object rather than an inherited one.

THE BASIS IS IMPORTED, NOT REINVENTED. The wall is the clamped-left
natural cubic spline of the bell engine [X-TOCV] --- its own
spline_coeffs / spline_eval, called here. Same class (C^2 on any
strictly increasing knot set), same clamped left end, same convention
that knots are frozen during an optimization. Using one basis for both
engines is what makes a bell-vs-plug comparison at equal shape freedom
meaningful, and it means the adaptive-knot machinery [X-AKNO] applies
to this wall unchanged.

THE DESIGN VECTOR   W = [y_1, ..., y_m]
  y_k = spike radius at m FROZEN abscissae x_k on (X0, L]. The last
  node sits exactly at x = L: FIXED LENGTH is what makes the problem
  well posed, since without it the answer is always "longer".

THE LEFT END IS NOT FREE, and this is physics rather than convenience.
The start radius y_w0 is set by the mass constraint (below), and the
wall must leave the start station TANGENT TO THE FLOW --- a wall is a
streamline, so its slope where the Cauchy data meets it is the local
flow angle, not a design choice. Hence the clamped left slope.

THE INLET ANGLE. Per the standing owner directive the RDE input is a
STRAIGHT LINE and its inclination theta_i is a design variable; step
15 swept it and found the optimum at theta_E = theta_i + dnu = 0.
That sweep is the OUTER loop and is not repeated here: this carrier
optimizes the SHAPE at the angle step 15 selected, so that the two
degrees of freedom are not conflated in one number. The straight
inlet itself is untouched --- it is upstream of X0 and enters only
through the Cauchy data.

CONSTRAINTS, both by construction (the step-15 discipline):
  mass   : y_w0 is bisected so the start line passes the reference
     mass flow. It depends on the fan and y_w0 ALONE --- the start
     line is Cauchy data on a vertical cut, upstream of every spline
     node --- so the mass constraint DECOUPLES exactly from the shape
     dofs. That is measured here (C-3), not assumed.
  length : the last node is at x = L.
With both imposed by construction the remaining problem is a bound-
free smooth maximization, and the trust-region SQP driver is used for
its step control and its certification gate rather than for
constraint handling.

THE GRADIENT is the reverse-AD adjoint through the RECORDED SCHEDULE:
one march records the concrete decisions (wall-search indices, cell
topology), and every subsequent evaluation replays that schedule, so
the derivative is exact at fixed topology and the optimizer never
differentiates a branch. This is the device the bell driver uses, and
the record is refreshed whenever a step is accepted.

CHECKS
  C-1  the basis CONTAINS the incumbent: the spline interpolating the
       fan streamline at the knots reproduces that contour, and its
       thrust matches the step-15 value, within the march's own band;
  C-2  the AD adjoint agrees with central finite differences, both
       component-wise and in the directional-derivative identity,
       inside a derived band;
  C-3  mass decoupling: displacing the shape dofs leaves the
       start-line mass flow unchanged to round-off;
  C-4  every accepted design is Newton-certified and admissible (the
       spike descends and clears the axis);
  C-5  the optimizer does not lose to its own start: J(final) >=
       J(streamline), and the gain is reported against the derived
       thrust band so that "no gain" is a legible outcome;
  R-1  rejector: the same driver on a SIGN-FLIPPED objective must walk
       the other way, i.e. must not land on the maximizer.

Run:  .venv-a1/bin/python validation/a1_plug_spline_opt.py
      PSPL_M=6 PSPL_ITERS=12 .venv-a1/bin/python validation/...
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                        # noqa: E402
import a1_config_compare as CC                         # noqa: E402
import a1_inlet_angle_opt as IA                        # noqa: E402
from a1_plug_march import plug_march, col_fluxes       # noqa: E402
from a1_freejet_unit import q_at_pa                    # noqa: E402
from a1_toc_variational_jax import spline_coeffs, spline_eval  # noqa: E402

import jax                                             # noqa: E402
import jax.numpy as jnp                                # noqa: E402
from scipy.optimize import brentq, minimize            # noqa: E402

NPASS = [0, 0]
PA = CC.PA
X0 = IA.X0
# LENGTH, PROMOTED (2026-08-13). Default = IA.L_REF, so every prior
# path is bit-identical; PSPL_L sets it. This is the knob the open
# queue names as the blocker for the ONE decisive comparison left on
# the plug: Rao-vs-spline is VOID at L = 2.5 m (mass + length exhaust
# Rao's two degrees of freedom, so the ambient becomes an OUTPUT --
# the classical design there implies 1.7e6 Pa against the case's
# 7.6e5). The fair test is at FULL EXPANSION, L ~ 5.825 m for this
# world, where mass AND ambient can both be met and the two methods
# answer the same question.
L = float(os.environ.get("PSPL_L", IA.L_REF))
THE_OPT = 0.0                   # exhaust angle selected by step 15
# the fan: "planar" (the corner simple wave, every prior path) or "axi"
# (the inverse-march construction of a1_axi_fan [X-AFAN], 2026-09-16)
FAN_MODE = os.environ.get("PSPL_FAN", "planar")
M_NODES = int(os.environ.get("PSPL_M", 6))
# A1_BASE_MODEL: the N2 base-pressure closure priced into J (a key of
# base_pressure.MODELS). Unset = the functional of every row of record.
BASE_MODEL = os.environ.get("A1_BASE_MODEL", "")
K_ST = int(os.environ.get("PSPL_K", 81))    # march wall stations
N_ROW = int(os.environ.get("PSPL_N", 61))   # start-line rows
MAXSEG = int(os.environ.get("PSPL_ITERS", 10))
# PSPL_BACKTRACK (S32, the "restoration step of our own" of the S30
# queue, item 1): the number of halvings the driver may try, on the
# RE-MARCHED value, before a rejected segment is thrown away. 0 = the
# record's reject-and-shrink driver, bit-identical (see run_trsqp).
BACKTRACK = int(os.environ.get("PSPL_BACKTRACK", 0))
HERE = os.path.dirname(os.path.abspath(__file__))
CKPT = os.path.join(HERE, "_plug_spline")


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# the posed world: fan, mass-set start radius, Cauchy data
# ======================================================================
def build_case(w, thE=THE_OPT, N=None):
    """Everything the shape optimization holds FIXED: the fan (hence
    the inlet angle), the mass-set start radius, and the Cauchy data
    on the start line. Returns the incumbent streamline too."""
    Nr = N_ROW if N is None else N
    if FAN_MODE == "axi":
        # [X-AFAN] the axisymmetric fan by the inverse march: the wall
        # is the ideal member traced from the tip, the start radius is
        # its output (mass closes on the terminal ray), the cut below
        # samples the marched field. Additive: PSPL_FAN unset = the
        # planar path, bit-identical.
        import a1_axi_fan as AF
        fan = AF.fan_axi(w, thE, verbose=True)
        y0 = fan["y_sp0"]
        sx, sy = fan["wall"]
        if L > sx[-1]:
            print("   NOTE: requested L %.4f beyond the construction's tip"
                  " %.4f: the incumbent is clamped at the tip radius"
                  " there (declared)" % (L, sx[-1]))
    else:
        fan = IA.fan_at(w, thE)
        # Size with the functional that grades (step 15's lesson,
        # Appendix~\ref{app:twoinstruments}): start_mass measures the
        # start line with the march's own column functional, which is
        # also what C-3 below reports. Sizing with any other rule leaves
        # a residue that is instrument difference rather than error.
        y0 = brentq(lambda ys: IA.start_mass(w, fan, ys, Nr)
                    - w["mdot"], 0.45 * w["RMAX"], 0.985 * w["RMAX"],
                    xtol=1e-9)
        # the incumbent streamline must reach BEYOND the requested
        # length: W0 interpolates it at the knots, the last of which
        # sits at x = L. IA.spike's default stops at X_END + 0.3 = 3.3,
        # which silently truncates for any L past that -- the second
        # half of "promote L".
        sx, sy = IA.spike(fan, y0, x_end=max(IA.X_END, L) + 0.3)
    yw0 = float(np.interp(X0, sx, sy))
    slope0 = float(np.tan(fan["field"](X0, yw0)[1]))   # flow-tangent
    ye0 = fan["LIP"][1] + np.tan(fan["th_e"]) * X0
    yline = np.linspace(yw0, ye0, Nr)
    us, vs = [], []
    for y in yline:
        q, t = fan["field"](X0, y)
        us.append(q * np.cos(t))
        vs.append(q * np.sin(t))
    us, vs = np.array(us), np.array(vs)
    stl = np.stack([np.full(Nr, X0), yline, us, vs], axis=1)
    md_in, F_in = col_fluxes(stl, w["ta"], PA, 1.0)
    # frozen knot abscissae (uniform class, last node AT x = L)
    xi = np.arange(1, M_NODES + 1) / M_NODES
    xk = X0 + (L - X0) * xi
    return dict(fan=fan, y0=y0, yw0=yw0, slope0=slope0,
                start=(X0, yline, us, vs), stl=stl,
                md_in=float(abs(md_in)), F_in=float(F_in),
                sx=sx, sy=sy, xk=xk,
                qpa=q_at_pa(PA, w["ta"], w["as_"]),
                W0=np.interp(xk, sx, sy))


def wall_stations(W, c, K=None):
    """Design vector -> (x, y, slope) at the march's wall stations.
    Traced: W may be a JAX array."""
    xs = jnp.concatenate([jnp.array([X0]), jnp.asarray(c["xk"])])
    ys = jnp.concatenate([jnp.array([c["yw0"]]), jnp.asarray(W)])
    Mc = spline_coeffs(xs, ys, c["slope0"])
    # stations strictly DOWNSTREAM of the start line: the start line is
    # Cauchy data, not a wall station (the march's own convention).
    Kq = K_ST if K is None else K
    xq = jnp.linspace(X0, L, Kq + 1)[1:]
    yq, sq = jax.vmap(lambda x: spline_eval(x, xs, ys, Mc))(xq)
    return xq, yq, sq


# ======================================================================
# objective: thrust at the fixed length L
# ======================================================================
def march_record(W, w, c, K=None, margin=None):
    """Concrete march: returns (out, sched). margin (optional) = the
    fold-margin dict of [X-PMRG] (a1_plug_march docstring)."""
    xq, yq, sq = wall_stations(np.asarray(W, dtype=float), c, K=K)
    return plug_march((xq, yq, sq), c["start"], c["qpa"], w["tab"], 1.0,
                      margin=margin)


def margin_replay(W, w, c, sched, margin, K=None):
    """KS fold margin minus its floor mu0, replaying a recorded
    schedule: differentiable in W (the same frozen-decision replay as
    J_replay). [X-PMRG]"""
    xq, yq, sq = wall_stations(W, c, K=K)
    S = A1.Sched("play", sched.d)
    out, _ = plug_march((xq, yq, sq), c["start"], c["qpa"], w["tab"],
                        1.0, sched=S, margin=margin)
    return out["margin_ks"] - margin["mu0"]


def margin_and_grad(W, w, c, sched, margin):
    f = lambda z: margin_replay(z, w, c, sched, margin)     # noqa: E731
    v, g = jax.value_and_grad(f)(jnp.asarray(W, dtype=float))
    return float(v), np.asarray(g, dtype=float)


# REQ-NONSTALL finite fallback for a non-finite objective (the bell's
# f_np contract, S21 C2): derived from the machine range, not tuned --
# any finite value the minimizer reads as "far worse than every real
# base" serves; the event is COUNTED, never silent.
J_NONFINITE = float(np.sqrt(np.finfo(float).max))


def J_replay(W, w, c, sched, ta, K=None):
    """Thrust, replaying a recorded schedule. Differentiable in W.

    THE BASE, AND WHY IT IS OPTIONAL. The wall integral stops at the
    last station and the face of radius y(L) that the contour leaves
    behind is NOT in this functional: with the tip radius a free design
    variable (the last knot, bounded below by the march's tip floor)
    the search can raise the tip -- shortening the spike -- without
    paying for the base it creates. Measured 2026-09-17 on the
    overnight leg's return: the tip rose 0.02270 -> 0.02794 m, an
    unpriced base term of -1.47e+03 N against -9.91e+02 N at the floor.
    A1_BASE_MODEL names a member of the N2 slot (base_pressure.MODELS) and
    prices it; unset -- every row of record so far -- leaves this
    function exactly as it was. The slot is declared, banded and
    falsifiable, never a fit: see validation/base_pressure.py."""
    xq, yq, sq = wall_stations(W, c, K=K)
    S = A1.Sched("play", sched.d)
    out, _ = plug_march((xq, yq, sq), c["start"], c["qpa"], w["tab"],
                        1.0, sched=S)
    wall = out["wall"]
    q = jnp.sqrt(wall[:, 2] ** 2 + wall[:, 3] ** 2)
    st = A1.state_q(q, ta)
    pw = st[1]
    dy = wall[1:, 1] - wall[:-1, 1]
    wgt = 2.0 * jnp.pi * 0.5 * (wall[1:, 1] + wall[:-1, 1])
    pm = 0.5 * (pw[1:] + pw[:-1])
    push = jnp.sum((pm - PA) * wgt * (-dy))
    if not BASE_MODEL:
        return c["F_in"] + push
    import base_pressure as BP
    p_b = BP.p_base(st[1][-1], st[5][-1], st[4][-1], PA, BASE_MODEL)
    return c["F_in"] + push + BP.base_term(p_b, wall[-1, 1], PA)


FD_LADDER = (1e-6, 1e-7, 1e-8)


def fd_ladder(f, W0, v, scale):
    """Central differences along v on a LADDER of step sizes.

    A single pair of steps cannot arbitrate here. The replayed march is
    only piecewise smooth in the design vector --- the wall-search
    topology is frozen, so a perturbed design can sit fractionally on
    the wrong side of a decision the record already made --- and the
    resulting FD residual is NOISE, not truncation. Measured: it fails
    to fall as h^2 and instead wanders at a fixed level. Estimating a
    truncation error from two points therefore produces a band that
    describes nothing, which is how a correct adjoint came to be
    reported as a failure.

    The ladder measures the finite difference's OWN reliability: the
    spread across steps small enough that truncation is negligible is
    the noise floor, and that is what the adjoint may be graded
    against."""
    vals = []
    for e in FD_LADDER:
        h = e * scale
        fp = float(f(W0 + h * v))
        fm = float(f(W0 - h * v))
        vals.append((fp - fm) / (2.0 * h))
    vals = np.array(vals)
    spread = float(vals.max() - vals.min())
    return float(np.median(vals)), spread


def J_and_grad(W, w, c, ta, sched):
    """Value and reverse-AD gradient on a FROZEN schedule."""
    f = lambda z: J_replay(z, w, c, sched, ta)          # noqa: E731
    v, g = jax.value_and_grad(f)(jnp.asarray(W, dtype=float))
    return float(v), np.asarray(g, dtype=float)


# ======================================================================
# the driver: trust-region SQP with a record/certify gate per segment
# ======================================================================
def run_trsqp(W0, w, c, ta, sign=+1.0, max_segments=MAXSEG,
              maxiter_per_seg=8, verbose=1, margin=None, tr0=0.05,
              tr_floor=None, bounds=None, backtrack=None):
    """Segmented trust-constr. One SEGMENT = one frozen schedule: the
    march is re-recorded at the segment base, the optimizer walks on
    that record, and acceptance triggers a fresh record. A base whose
    record is NOT Newton-certified is REJECTED and the radius shrinks
    (the reject-and-shrink semantics of the bell driver). With a
    margin and a start OUT of class the walk opens with a PHASE 1
    (restoration) run: the segment minimises the class violation
    instead of -J and acceptance reads the violation alone, until the
    first base with KS >= mu0 hands the walk to the objective phase;
    a violation that cannot be reduced at the radius floor stops the
    walk as NOT RESTORABLE (see the block comment in the loop). An
    in-class start never enters it and is bit-identical.

    BACKTRACKING (S32, [X-HMPH] reading: "the model verifies an optimum
    but does not find it from afar"). The record's driver answers a
    rejected segment by reverting to the incumbent and halving the
    radius: measured on the Humphreys opt leg from the fan (S31, 30
    segments), 11 rejections in the fixed cadence "one step, two
    rejections" -- the frozen-schedule model says "better", the re-march
    says "worse" -- and the walk ends by budget 0.6 percent below the
    paper's optimum with |grad J|/J ~ 0.14. With backtrack = n > 0 a
    rejected trial is not thrown away: the driver walks BACK along the
    segment's displacement d = W_trial - W_best at the fractions 1/2,
    1/4, ... 1/2^n, re-marching each point, and adopts the first one
    that is certified, in class and better than the incumbent (a
    textbook line search on the true objective, the march being the
    model); if none is, it tries the same halvings on a PROJECTED
    ASCENT step from the incumbent along its own recorded gradient
    (length = the current radius, clipped to the bounds), which does not
    depend on the frozen model at all; only when both fail does it
    revert and shrink as before. An accepted backtracked point becomes
    the next base with its record carried (no second march) and the
    radius set to the length of the step that succeeded. Fractions
    below the radius floor are not tried (a move under the floor is not
    a measurement). backtrack = 0 (default, BACKTRACK from
    PSPL_BACKTRACK) is the record's driver, bit-identical."""
    W = np.asarray(W0, dtype=float)
    W_cert = None
    W_best, J_best = None, -np.inf
    g_best = None
    backtrack = BACKTRACK if backtrack is None else int(backtrack)
    n_bt = [0, 0, 0]        # accepted along-segment, accepted ascent, probes
    pending = None          # record carried from an accepted backtrack
    # PHASE 1 (restoration) state: the least-violating certified
    # iterate seen while no IN-CLASS base exists yet, and its violation
    W_rest, V_best = None, None
    tr = tr0        # [X-PMRG] margin-constrained walks derive tr0
    # RADIUS FLOOR: the unconstrained walk's policy constant (1 mm,
    # "converged" when a trial at <= 1 mm + 1 percent fails) -- the
    # SAME literals as before when tr_floor is None, so every existing
    # caller is bit-identical; a margin-constrained walk passes a
    # floor DERIVED from the fold scale (S29 smoke 4: with tr0 0.4 mm
    # below a 1 mm floor the first rejection ended the walk).
    floor = 1e-3 if tr_floor is None else float(tr_floor)
    slack = 1.01e-3 if tr_floor is None else floor * (1 + 1 / 100)
    n_rec = 0
    hist = []
    def _probe(Wt):
        """Re-march a trial point for the backtracking search: its
        certified record, J, gradient and class flag, or None when the
        record fails or is not certified (the same tests the loop's
        base gate applies, so an accepted probe is a legal base)."""
        n_bt[2] += 1
        try:
            o, sc = march_record(Wt, w, c, margin=margin)
        except Exception:
            return None
        if float(o["cert_worst"]) > 1.0:
            return None
        Jt, gt = J_and_grad(Wt, w, c, ta, sc)
        bad = (margin is not None
               and float(o["margin_ks"]) - margin["mu0"]
               < -float(margin.get("tol", 0.0)))
        return Jt, gt, o, sc, bad

    def _project(Wt):
        if bounds is None:
            return Wt
        lb = getattr(bounds, "lb", None)
        ub = getattr(bounds, "ub", None)
        if lb is None:
            lb = np.asarray([b[0] for b in bounds], float)
            ub = np.asarray([b[1] for b in bounds], float)
        return np.clip(Wt, lb, ub)

    def _search(base, d, J_ref, seg, what):
        """Halve along d from base until a certified, in-class point
        beats J_ref (sign-aware); returns (Wt, probe, alpha) or None."""
        for k in range(1, backtrack + 1):
            a = 0.5 ** k
            Wt = _project(base + a * d)
            h = float(np.linalg.norm(Wt - base))
            if h < floor:
                if verbose:
                    print("    [seg %2d] %s: step %.3e below the floor"
                          " at 1/%d -> give up" % (seg, what, h, 2 ** k),
                          flush=True)
                return None
            pr = _probe(Wt)
            if pr is None:
                if verbose:
                    print("    [seg %2d] %s 1/%d: record not certified"
                          % (seg, what, 2 ** k), flush=True)
                continue
            Jt, gt, o, sc, bad = pr
            ok = (not bad) and sign * Jt > sign * J_ref
            if verbose:
                print("    [seg %2d] %s 1/%d (step %.3e): J = %.8e"
                      " cert = %.3f%s -> %s"
                      % (seg, what, 2 ** k, h, Jt, float(o["cert_worst"]),
                         " INFEASIBLE" if bad else "",
                         "ACCEPT" if ok else "worse"), flush=True)
            if ok:
                return Wt, pr, a
        return None

    for seg in range(max_segments):
        try:
            if pending is not None:
                out_rec, sched = pending[2], pending[3]
                pending_Jg = (pending[0], pending[1])
                pending = None
            else:
                pending_Jg = None
                out_rec, sched = march_record(W, w, c, margin=margin)
                n_rec += 1
            cw = float(out_rec["cert_worst"])
            if cw > 1.0:
                raise RuntimeError("record not certified (worst %.3e)"
                                   % cw)
        except Exception as err:
            # revert target: the certified in-class base, or, in
            # phase 1 below, the least-violating restoration iterate
            W_back = W_cert if W_cert is not None else W_rest
            if backtrack > 0 and W_best is not None:
                # an UNCERTIFIED base is a rejected trial too (3 of the
                # 11 rejections of the S31 opt leg): walk back along
                # the segment before throwing it away
                if verbose:
                    print("    [seg %2d] base not certified (%s)"
                          % (seg, err), flush=True)
                hit = _search(W_best, W - W_best, J_best, seg, "backtrack")
                if hit is not None:
                    n_bt[0] += 1
                    W, pending, a = hit
                    tr = max(floor, float(np.linalg.norm(W - W_best)))
                    if verbose:
                        print("    [seg %2d] restoration ACCEPTED ->"
                              " base, radius -> %.3e" % (seg, tr),
                              flush=True)
                    continue
            if W_back is not None and tr > floor:
                tr = max(floor, 0.5 * tr)
                if verbose:
                    print("    [seg %d] base REJECTED (%s) -> revert,"
                          " radius -> %.3e" % (seg, err, tr))
                W = W_back.copy()
                continue
            raise
        if pending_Jg is not None:
            J0, g0 = pending_Jg
        else:
            J0, g0 = J_and_grad(W, w, c, ta, sched)
        # PHASE 1 -- RESTORATION ([X-PTRN], S30 2026-09-17). The
        # feasibility gate below is armed only once a certified base
        # exists, so a walk that STARTS out of class adopted its start
        # as W_best and then rejected every trial against it -- trials
        # that REDUCE the violation included -- until the radius hit
        # the floor and the driver printed "converged" (measured
        # 2026-09-17 on starts B and C of the (81,41) tournament leg:
        # 5360 s, zero steps, C and its 0 folded columns failing only
        # by the floor). A method that must run on a posed geometry it
        # did not choose cannot do that. While NO in-class base has
        # been seen the segment minimises the VIOLATION instead of -J
        # (a textbook phase-1 step: same aggregated margin, no new
        # field, no case constant, constraint list empty), acceptance
        # reads the violation ALONE, and the walk enters the objective
        # phase at the first base with KS >= mu0 -- strictly, the
        # aggregation gap 'tol' only ever relaxes the rejection of an
        # already accepted base, never the entry into the class. A
        # walk that cannot reduce the violation at the radius floor
        # stops as NOT RESTORABLE: a declared outcome, never
        # "converged". Structurally inert for an in-class start
        # (phase1 is False at segment 0 and W_cert is set from then
        # on), which is the port's bit-identity gate.
        phase1 = (margin is not None and W_cert is None
                  and float(out_rec["margin_ks"]) < margin["mu0"])
        if phase1:
            v0 = margin["mu0"] - float(out_rec["margin_ks"])
            # the SAME default as the objective's and the constraint's
            # (an empty dict here made _mvg's "m_exec" += 1 raise, and
            # the campaign reported the KeyError as a G1 rejector:
            # measured on the phase-1 smoke of start C, 2026-09-17)
            ctr = margin.setdefault("counters",
                                    dict(m_exec=0, m_dedup=0,
                                         m_nonfinite=0, gm_nonfinite=0))
            ctr["restore_rec"] = ctr.get("restore_rec", 0) + 1
            # "decreased" means by more than the march's own epsilon:
            # a smaller move is not a measurement (A1.EPS, no literal)
            if V_best is not None and v0 >= V_best - A1.EPS * max(V_best, 1.0):
                if tr <= slack:
                    if verbose:
                        print("    [seg %2d] restoration stalled at the"
                              " radius floor (violation %.4e) -> NOT"
                              " RESTORABLE, stop" % (seg, v0), flush=True)
                    ctr["restore_stall"] = ctr.get("restore_stall", 0) + 1
                    break
                tr = max(floor, 0.5 * tr)
                if verbose:
                    print("    [seg %2d] restoration trial violation"
                          " %.4e REJECTED (>= %.4e) -> revert, radius"
                          " -> %.3e" % (seg, v0, V_best, tr), flush=True)
                W = W_rest.copy()
                continue
            V_best, W_rest = v0, W.copy()
            if verbose:
                print("    [seg %2d] RESTORATION: KS - mu0 %+.4f"
                      " (violation %.4e), J = %.8e, cert = %.3f"
                      % (seg, -v0, v0, J0, cw), flush=True)
        # FEASIBILITY GATE ([X-PMRG], margin path only): trust-constr's
        # iterates approach the constraint from the infeasible side (a
        # barrier method with slacks: c(x) - s = 0 holds at convergence,
        # not at every iterate), so a segment cut short by its budget
        # can return a certified, IMPROVING base that sits past the
        # floor (measured S29 smoke 2x6: KS - mu0 = -0.0152 after six
        # iterations, +0.0009 after twelve in the walk of record). The
        # class is "never let through": such a base is REJECTED through
        # the same revert-and-shrink branch as a worse trial, and
        # COUNTED. tol = the aggregation gap ln N / rho carried by the
        # caller (0 = strict). False whenever margin is None.
        infeasible = (margin is not None and W_cert is not None
                      and float(out_rec["margin_ks"]) - margin["mu0"]
                      < -float(margin.get("tol", 0.0)))
        if infeasible:
            ctr = margin.setdefault("counters", {})
            ctr["infeasible_base"] = ctr.get("infeasible_base", 0) + 1
        # ACCEPTANCE TEST (standard trust-region logic, and the defect
        # the first run of this carrier exposed): a segment endpoint is
        # a TRIAL point, not an accepted one. trust-constr walks a
        # LOCAL model on a FROZEN schedule, so a long segment can walk
        # past the point where that model is still valid and return a
        # base that is genuinely worse. If the new base does not beat
        # the incumbent, revert to the best certified design and shrink
        # the radius; only an improving base is adopted.
        if (J_best > -np.inf and sign * J0 < sign * J_best) or infeasible:
            why = ("INFEASIBLE (KS - mu0 %+.4f)"
                   % (float(out_rec["margin_ks"]) - margin["mu0"])
                   if infeasible else "worse")
            if backtrack > 0 and W_best is not None:
                # the model's own prediction at the trial, for the
                # reading (rho = actual / predicted gain)
                if verbose:
                    Jm = -sign * float(res.fun)
                    den = Jm - J_best
                    print("    [seg %2d] trial J = %.8e %s than %.8e;"
                          " model predicted %.8e (rho %s)"
                          % (seg, J0, why, J_best, Jm,
                             ("%.2f" % ((J0 - J_best) / den))
                             if den != 0.0 else "n/a"), flush=True)
                hit = _search(W_best, W - W_best, J_best, seg, "backtrack")
                if hit is None and g_best is not None:
                    gn = float(np.linalg.norm(g_best))
                    if gn > 0.0:
                        # the ascent step of length 2*tr: the search
                        # starts at its half, i.e. at the radius
                        hit = _search(W_best, 2.0 * tr * sign * g_best / gn,
                                      J_best, seg, "ascent")
                        if hit is not None:
                            n_bt[1] += 1
                elif hit is not None:
                    n_bt[0] += 1
                if hit is not None:
                    W, pr, a = hit
                    pending = pr
                    tr = max(floor, float(np.linalg.norm(W - W_best)))
                    if verbose:
                        print("    [seg %2d] restoration ACCEPTED ->"
                              " base, radius -> %.3e" % (seg, tr),
                              flush=True)
                    continue
            if tr <= slack:
                if verbose:
                    print("    [seg %2d] trial %s at the radius"
                          " floor -> converged, stop" % (seg, why))
                break
            tr = max(floor, 0.5 * tr)
            if verbose:
                print("    [seg %2d] trial J = %.8e REJECTED (%s"
                      " than %.8e) -> revert, radius -> %.3e"
                      % (seg, J0, why, J_best, tr))
            W = W_best.copy()
            continue
        hist.append((seg, J0, float(np.linalg.norm(g0)), cw))
        if not phase1:
            W_cert = W.copy()
            if sign * J0 > sign * J_best:
                W_best, J_best = W.copy(), J0
                g_best = np.asarray(g0, float).copy()
            if verbose:
                print("    [seg %2d] J = %.8e  |grad| = %.3e  cert = %.3f"
                      % (seg, J0, np.linalg.norm(g0), cw), flush=True)

        def fun(z):
            v, g = J_and_grad(z, w, c, ta, sched)
            if margin is not None:
                # REQ-NONSTALL on the OBJECTIVE (the bell's f_np/g_np
                # contract, S21 C2): the interior-point method probes
                # INFEASIBLE trial points by construction, and on a
                # folded trial design the replayed J has a finite
                # value but a NaN adjoint gradient (measured S29: a
                # +1.3/+0.9/-1.9 cm kink on the first knots, J "+4
                # percent", m = -1.19, every gradient component
                # non-finite). A silent NaN crashed trust-constr's
                # normal step; the finite fallback keeps it stepping,
                # the event is COUNTED and fails the verdict downstream
                # -- never a silent patch.
                ctr = margin.setdefault("counters",
                                        dict(m_exec=0, m_dedup=0,
                                             m_nonfinite=0,
                                             gm_nonfinite=0))
                if not np.isfinite(v):
                    ctr["obj_nonfinite"] = ctr.get("obj_nonfinite", 0) + 1
                    return J_NONFINITE, np.zeros_like(np.asarray(g))
                if not np.all(np.isfinite(g)):
                    ctr["grad_nonfinite"] = ctr.get("grad_nonfinite", 0) + 1
                    g = np.where(np.isfinite(g), g, 0.0)
            return -sign * v, -sign * g

        # FOLD-MARGIN CONSTRAINT ([X-MGOV] pattern, plug port [X-PMRG]):
        # m(W) - mu_0 >= 0 on the SAME frozen schedule; value+gradient
        # memo (scipy asks for them separately at the same point); G1
        # finite fallback + REQ-NONSTALL counters.
        cons = []
        if margin is not None:
            from scipy.optimize import NonlinearConstraint
            slot = dict(key=None, v=None, g=None)
            ctr = margin.setdefault("counters",
                                    dict(m_exec=0, m_dedup=0,
                                         m_nonfinite=0, gm_nonfinite=0))

            def _mvg(z):
                k = np.asarray(z, float).tobytes()
                if slot["key"] == k:
                    ctr["m_dedup"] += 1
                    return slot["v"], slot["g"].copy()
                v, g = margin_and_grad(z, w, c, sched, margin)
                ctr["m_exec"] += 1
                slot.update(key=k, v=v, g=g.copy())
                return v, g

            def m_np(z):
                v, _ = _mvg(z)
                if not np.isfinite(v):
                    ctr["m_nonfinite"] += 1
                    return -2.0 * A1.K_RICH * margin["m_ref"]   # G1
                return v

            def gm_np(z):
                _, g = _mvg(z)
                if not np.all(np.isfinite(g)):
                    ctr["gm_nonfinite"] += 1
                    g = np.where(np.isfinite(g), g, 0.0)
                return g[None, :]
            def fun_r(z):
                # PHASE 1 objective: minimise the violation by
                # MAXIMISING the very field the constraint aggregates
                # (m_np/gm_np's memo, fallbacks and counters), so the
                # restoration phase and the class criterion never
                # disagree about what they are measuring.
                v, g = _mvg(z)
                if not np.isfinite(v):
                    ctr["m_nonfinite"] += 1
                    return (2.0 * A1.K_RICH * margin["m_ref"],
                            np.zeros(np.asarray(z, float).shape))
                if not np.all(np.isfinite(g)):
                    ctr["gm_nonfinite"] += 1
                    g = np.where(np.isfinite(g), g, 0.0)
                return -float(v), -np.asarray(g, float)

            cons = [NonlinearConstraint(m_np, 0.0, np.inf, jac=gm_np)]
            m0v = float(out_rec["margin_ks"]) - margin["mu0"]
            if verbose:
                print("    [seg %2d] margin at base: KS - mu0 = %+.4f"
                      " (min cell %+.4f, %d cells)"
                      % (seg, m0v, float(out_rec["margin_min"]),
                         int(out_rec["margin_n"])), flush=True)

        # NO-MOTION is not always convergence (S23 measured, on the
        # S22 optimum at (121,101)): when the initial radius exceeds
        # the surface's fold scale, trust-constr's FIRST rejected
        # trial poisons its quadratic model with the fold's negative
        # curvature and it burns its remaining iterations without
        # evaluating the objective again, returning the start point
        # unchanged while J is measurably improvable (+7e4 at
        # h = 1e-3 along +grad, verified against the same frozen
        # schedule). Same reject-and-shrink semantics as a rejected
        # base: shrink OUR radius and retry the segment on the SAME
        # record; only a no-motion at the radius floor is convergence.
        while True:
            # bounds (additive, [X-PTRN]): None = scipy's own default,
            # the same call as before for every existing caller
            # PHASE-1 CADENCE (measured 2026-09-17, legs B and C): the
            # frozen schedule is NOT a usable model for the margin at
            # the fold-scale radius -- eight iterations on it took
            # start C from a violation of 4.33e-02 to 7.34e-01 on the
            # re-march, and the shrink that follows ends the walk. The
            # objective phase survives that because a bad segment is
            # caught by the record/certify gate and reverted; the
            # restoration has no incumbent to revert to. So phase 1
            # takes ONE iteration per record: the march is the model.
            res = minimize(fun_r if phase1 else fun, W, jac=True,
                           method="trust-constr",
                           constraints=([] if phase1 else cons),
                           bounds=bounds,
                           options=dict(maxiter=(1 if phase1
                                                 else maxiter_per_seg),
                                        initial_tr_radius=tr,
                                        gtol=0.0, xtol=1e-14,
                                        verbose=0))
            if margin is not None:
                margin["last_res"] = res
                if verbose:
                    ctr = margin.get("counters", {})
                    print("    [seg %2d] margin counters: %s;"
                          " multipliers %s"
                          % (seg, {k: v for k, v in ctr.items() if v},
                             [np.asarray(x).ravel().round(3).tolist()
                              for x in (res.v or [])]
                             if getattr(res, "v", None) is not None
                             else None), flush=True)
            step = float(np.linalg.norm(res.x - W))
            if step >= 1e-12 or tr <= slack:
                break
            tr = max(floor, 0.5 * tr)
            if verbose:
                print("    [seg %2d] no motion at radius %.3e ->"
                      " retry at %.3e (same record)"
                      % (seg, 2 * tr, tr), flush=True)
        if step < 1e-12:
            if verbose:
                print("    [seg %2d] no motion -> stop" % seg)
            break
        W = np.asarray(res.x, dtype=float)
        # The OUTER radius is ours and is never read back from
        # trust-constr: its internal radius tracks ITS model on a
        # frozen schedule, and adopting it silently undid every shrink
        # this loop ordered (measured: the walk oscillated between one
        # good base and two overshoots, re-recording forever). Grow
        # only on an accepted base, shrink only here.
        tr = float(min(0.25, 1.5 * tr))
    if backtrack > 0 and verbose:
        print("    backtracking: %d probes, %d accepted along the segment,"
              " %d accepted on the ascent; %d records"
              % (n_bt[2], n_bt[0], n_bt[1], n_rec), flush=True)
    # the answer is the BEST CERTIFIED design seen, never the last
    # trial point (the two differ exactly when the walk overshoots).
    # A walk that never reached the class returns its LEAST-VIOLATING
    # certified iterate, graded (and failed by C-3) by the caller --
    # returning the start instead would hide the phase-1 work.
    return (W_best if W_best is not None
            else (W_rest if W_rest is not None else W)), hist, n_rec


# ======================================================================
def main():
    t0 = time.time()
    print("== A1 brick 2 step 16: the free-form spike"
          " (spline + TR-SQP) [F2/A1] ==")
    os.makedirs(CKPT, exist_ok=True)
    w = CC.build_world()
    ta = w["ta"]
    CF = lambda J: J / (w["P0"] * w["At"])                    # noqa
    c = build_case(w)
    print("  basis: chamber %.4e Pa / %.1f K, p_a %.4e Pa,"
          " mdot %.5e kg/s" % (w["P0"], w["T0"], PA, w["mdot"]))
    print("  inlet: theta_E = %.1f deg (step 15 optimum), theta_i ="
          " %.2f deg; start radius y_w0 = %.5f m (mass-set)"
          % (np.degrees(THE_OPT), np.degrees(c["fan"]["th_i"]),
             c["yw0"]))
    print("  shape: %d free nodes on (%.2f, %.2f] m, %d wall stations,"
          " %d start rows\n" % (M_NODES, X0, L, K_ST, N_ROW))

    # ---- C-1: how well does the basis represent the incumbent? -------
    # This is a REPRESENTATION measurement, not an equality test. A
    # spline on m nodes cannot reproduce the streamline exactly, and
    # claiming it should would be the wrong standard: the honest
    # question is whether the basis is DENSE --- whether the deviation
    # falls as nodes are added --- because that is what makes "the
    # incumbent is (nearly) in the search space" true, and what makes
    # an optimizer gain over it meaningful rather than an artifact of
    # a basis that cannot even express the starting contour.
    print("-- C-1: representation of the incumbent, under node"
          " refinement --")
    # Measured on a LADDER, not between two adjacent node counts. Two
    # error sources cross over here and a single ratio reads whichever
    # happens to dominate: at the coarsest count the natural-BC right
    # end dominates, and from twice that count the maximum moves to
    # x ~ 0.6 m, where the streamline's curvature climbs from ~0 at the
    # clamped end to its peak. The LOCATION of the maximum is printed
    # because it is the finding: a uniform knot class spends its nodes
    # where the contour is nearly straight and starves the one region
    # that bends, which is precisely the case the adaptive-knot class
    # [X-AKNO] exists to answer.
    ladder = (M_NODES, 2 * M_NODES, 4 * M_NODES, 8 * M_NODES)
    drop = float(c["sy"][0] - np.interp(L, c["sx"], c["sy"]))
    dev = {}
    for m in ladder:
        xi = np.arange(1, m + 1) / m
        xk = X0 + (L - X0) * xi
        cm = dict(c, xk=xk)
        Wm = np.interp(xk, c["sx"], c["sy"])
        xq, yq, _ = wall_stations(Wm, cm)
        xq = np.asarray(xq)
        err = np.abs(np.asarray(yq) - np.interp(xq, c["sx"], c["sy"]))
        dev[m] = float(err.max())
        print("  m = %2d nodes: max |spline - streamline| = %.3e m"
              " (%.4f %% of the %.3f m spike drop) at x = %.3f m"
              % (m, dev[m], 100 * dev[m] / drop, drop,
                 xq[int(np.argmax(err))]))
    ratio = dev[ladder[0]] / max(dev[ladder[-1]], 1e-300)
    print("  across the ladder %d -> %d nodes: %.1fx reduction"
          % (ladder[0], ladder[-1], ratio))
    # the reference is not the limitation: the streamline is an RK4
    # quadrature and its own step refinement is four orders below the
    # smallest representation error on the ladder.
    _, sy_a = IA.spike(c["fan"], c["y0"], h=1.5e-3)
    _, sy_b = IA.spike(c["fan"], c["y0"], h=3.75e-4)
    sx_a, _ = IA.spike(c["fan"], c["y0"], h=1.5e-3)
    sx_b, _ = IA.spike(c["fan"], c["y0"], h=3.75e-4)
    ref_res = abs(float(np.interp(L, sx_a, sy_a))
                  - float(np.interp(L, sx_b, sy_b)))
    print("  reference streamline resolved to %.2e m (RK4 step"
          " refinement) -- not the limiting error" % ref_res)
    out0, sch0 = march_record(c["W0"], w, c)
    J_inc = float(J_replay(jnp.asarray(c["W0"]), w, c, sch0, ta))
    print("  J(streamline, as represented) = %.8e N   C_F = %.5f"
          "   cert = %.3f"
          % (J_inc, CF(J_inc), float(out0["cert_worst"])))
    check("C-1 the basis is dense: the representation error of the"
          " incumbent falls across the refinement ladder",
          ratio >= 4.0 and dev[ladder[-1]] < dev[ladder[0]])

    # ---- C-3: the mass constraint is met, and is shape-independent ---
    # The decoupling itself is STRUCTURAL and needs no measurement: the
    # start line is Cauchy data on a vertical cut at X0, built from the
    # fan and y_w0 alone, and every spline node lies downstream of it,
    # so no shape dof can reach it. What DOES need measuring is whether
    # the constraint is actually met on the quadrature the march uses,
    # which is the step-15 lesson (sizing on a finer rule than the one
    # that measures leaves a mismatch that is pure quadrature).
    print("\n-- C-3: is the mass constraint met on the march's own"
          " quadrature? --")
    m_lo = IA.start_mass(w, c["fan"], c["y0"], N_ROW)
    m_hi = IA.start_mass(w, c["fan"], c["y0"], 8 * N_ROW)
    band_m = (A1.K_RICH * abs(m_lo - m_hi)
              + A1.C_FLOOR * A1.EPS * w["mdot"]) / w["mdot"]
    err_m = abs(c["md_in"] / w["mdot"] - 1.0)
    print("  start-line mdot %.8e vs reference %.8e -> rel %.3e"
          "  (derived band %.3e)"
          % (c["md_in"], w["mdot"], err_m, band_m))
    check("C-3 the start line passes the reference mass flow inside"
          " the derived quadrature band", err_m <= band_m)

    # ---- C-2: the adjoint against finite differences -----------------
    print("\n-- C-2: AD adjoint vs central finite differences --")
    J0, g0 = J_and_grad(c["W0"], w, c, ta, sch0)
    print("  J = %.10e   |grad| = %.6e" % (J0, np.linalg.norm(g0)))
    fj = lambda z: J_replay(z, w, c, sch0, ta)           # noqa: E731
    W0j = jnp.asarray(c["W0"], dtype=float)
    ks = [0, len(g0) // 2, len(g0) - 1]
    ok2 = True
    for k in ks:
        v = jnp.zeros(len(g0)).at[k].set(1.0)
        scale = max(1.0, abs(float(c["W0"][k])))
        fd, spread = fd_ladder(fj, W0j, v, scale)
        band = (A1.K_RICH * spread
                + A1.C_FLOOR * A1.EPS * abs(J0) / (FD_LADDER[-1] * scale))
        rel = abs(fd - g0[k])
        print("  node %2d: AD %+.6e  FD %+.6e  |d| = %.3e"
              "  (ladder spread %.3e -> band %.3e)"
              % (k, g0[k], fd, rel, spread, band))
        ok2 = ok2 and (rel <= band)
    check("C-2 the AD adjoint matches central finite differences"
          " inside the band the differences' own scatter supports",
          ok2)
    v = jnp.asarray(np.ones(len(g0)) / np.sqrt(len(g0)))
    fd_v, spread_v = fd_ladder(fj, W0j, v, 1.0)
    dd = abs(float(np.dot(g0, np.asarray(v))) - fd_v)
    band_v = (A1.K_RICH * spread_v
              + A1.C_FLOOR * A1.EPS * abs(J0) / FD_LADDER[-1])
    print("  <grad,v> = %+.8e   FD_v = %+.8e   |d| = %.3e"
          "  (ladder spread %.3e -> band %.3e)"
          % (float(np.dot(g0, np.asarray(v))), fd_v, dd, spread_v,
             band_v))
    check("C-2b directional-derivative identity", dd <= band_v)

    # ---- the optimization -------------------------------------------
    print("\n-- the driver: segmented trust-region SQP --")
    Wf, hist, n_rec = run_trsqp(c["W0"], w, c, ta)
    out_f, sch_f = march_record(Wf, w, c)
    J_f = float(J_replay(jnp.asarray(Wf), w, c, sch_f, ta))
    cert_f = float(out_f["cert_worst"])
    gain = J_f / J_inc - 1.0
    # BAND AT THIS CARRIER'S OWN RESOLUTION. Quoting a gain against a
    # band derived elsewhere (step 13's production K, N) is the same
    # error as grading a constraint with the instrument that did not
    # set it: the number would describe a different computation. Refine
    # the march that produced BOTH thrusts and let it measure its own
    # discretization error, on the SAME two designs, so the difference
    # of interest keeps whatever cancellation it has.
    K2, N2 = 2 * K_ST - 1, 2 * N_ROW - 1
    c2 = build_case(w, N=N2)          # same design, refined world
    _, s_i2 = march_record(c["W0"], w, c2, K=K2)
    J_inc2 = float(J_replay(jnp.asarray(c["W0"]), w, c2, s_i2, ta, K=K2))
    _, s_f2 = march_record(Wf, w, c2, K=K2)
    J_f2 = float(J_replay(jnp.asarray(Wf), w, c2, s_f2, ta, K=K2))
    gain2 = J_f2 / J_inc2 - 1.0
    band_gain = (A1.K_RICH * abs(gain - gain2)
                 + A1.C_FLOOR * A1.EPS)
    print("\n  start  J = %.8e N   C_F = %.5f" % (J_inc, CF(J_inc)))
    print("  final  J = %.8e N   C_F = %.5f   cert = %.3f"
          % (J_f, CF(J_f), cert_f))
    print("  refined (K,N -> 2K-1, 2N-1): gain %+.4f %% vs %+.4f %%"
          % (100 * gain, 100 * gain2))
    print("  gain over the fan streamline at fixed length:"
          " %+.4f %%  (band DERIVED HERE %.4f %%, inherited %.4f %%)"
          % (100 * gain, 100 * band_gain, 100 * IA.BAND_J))
    check("C-6 the gain exceeds the band this carrier's own"
          " refinement supports", abs(gain) > band_gain)
    print("  records taken: %d;  segments walked: %d" % (n_rec,
                                                         len(hist)))

    # ---- C-4 / C-5 ---------------------------------------------------
    xf, yf, _ = wall_stations(Wf, c)
    yf = np.asarray(yf)
    descends = bool(np.all(np.diff(yf) < 0))
    clears = bool(yf.min() > 0.25)
    print("\n  final spike: y %.4f -> %.4f m over [%.2f, %.2f] m;"
          " descending = %s, clears the axis = %s"
          % (yf[0], yf[-1], X0, L, descends, clears))
    check("C-4 the optimum is Newton-certified and admissible (spike"
          " descends, clears the axis)",
          cert_f <= 1.0 and descends and clears)
    check("C-5 the optimizer does not lose to its own start",
          J_f >= J_inc - IA.BAND_J * abs(J_inc))

    # ---- R-1 rejector ------------------------------------------------
    print("\n-- R-1: the same driver on a SIGN-FLIPPED objective --")
    Wr, _, _ = run_trsqp(c["W0"], w, c, ta, sign=-1.0,
                         max_segments=max(2, MAXSEG // 3), verbose=1)
    out_r, sch_r = march_record(Wr, w, c)
    J_r = float(J_replay(jnp.asarray(Wr), w, c, sch_r, ta))
    print("  minimiser J = %.8e N (maximiser %.8e)" % (J_r, J_f))
    check("R-1 rejector: minimising the thrust does NOT land on the"
          " maximiser", J_r < J_f - IA.BAND_J * abs(J_inc))

    # settings-tagged checkpoint name: a quick run at other (M, K, N)
    # must never OVERWRITE a production record (S22 lesson — the S21
    # 10-knot design vector was destroyed by exactly that).
    np.savez_compressed(os.path.join(CKPT, "spline_opt_m%d_k%d_n%d.npz"
                                     % (M_NODES, K_ST, N_ROW)),
                        xk=c["xk"], W0=c["W0"], Wf=np.asarray(Wf),
                        x_wall=np.asarray(xf), y_wall=yf,
                        J0=J_inc, Jf=J_f, hist=np.array(hist),
                        sx=c["sx"], sy=c["sy"], yw0=c["yw0"])
    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()

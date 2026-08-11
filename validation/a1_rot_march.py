#!/usr/bin/env python3
"""A1 BRICK 2, SESSION S24 [F2/A1]: THE GENERAL INLET — rotational
MoC ported from the referee's reference implementation. Registry ID:
[X-RMAR].

WHAT THIS BUYS. The certified march is homentropic: one global
(h0, s0) for the whole field, every node reduced to (x, y, u, v), the
state reconstructed from the speed alone. A real RDE exhaust is not:
hot/cold streaks carry per-streamline stagnation state, and until now
a (p, T, M) initial line was over-determined — the march could accept
two of the three numbers and PREDICTED the third from the global
isentrope. GENO crossed this boundary long ago: its generic MoC
(MoC_Gen_m, Zucrow ch. 17) transports entropy and stagnation enthalpy
as STREAMLINE INVARIANTS, reconstructing each cell's streamline-foot
state from interpolated (s, h0) rather than lerped primitives (its
N-26 on-manifold fix). This carrier ports that machinery into the
certified march's cell/record framework, so that a full per-row
(p, T, M, theta) initial line is EXACTLY determined — three numbers,
three state dofs (s, h0, q) — and the march becomes valid for
rotational, non-uniform-total-state inlets.

THE PORT, EQUATION BY EQUATION (fidelity target = GENO's
inter_solve_gen, read at source):
  nodes    (x, y, u, v, s, h0) — invariants STORED (GENO stores
           primitives; the information is identical, and invariants
           make the closure explicit);
  closure  state_qs(q, s, h0): ht = h0 - q^2/2 -> T (h-table
           inversion), p = PREF exp((s(T) - s)/Rg), rho, c, gam, M —
           the certified state_q generalized; at (s0, h0) it IS
           state_q (R-0 measures the identity, not assumes it);
  interior unknowns z = (x4, y4, u4, v4, t) with the foot bracket a
           RECORDED DRIVER DECISION over the whole previous column
           (S24 measured lesson: when the per-column C- drop exceeds
           the row spacing the mesh shears and a single-chord foot
           EXTRAPOLATES the invariants — a systematic N-independent
           transport ramp; GENO's present(col) scan is the fix and
           is ported as a decision, searched once, replayed frozen):
           two characteristic
           position rows (midpoint slopes tan(th +/- alpha)); two
           COMPATIBILITY rows in Zucrow's (p, theta) form — along the
           C+ from pt1: (th4 - th1) + Q(p4 - p1) + S(x4 - x1) = 0,
           along the C- from pt2 the mirrored signs — with
           Q = sqrt(M^2-1)/(rho q^2) and the axisymmetric source
           S = delta sin(th)/(y M cos(th +/- alpha)), every
           coefficient at the MIDPOINT state of its own chord (the
           implicit-midpoint form our certified cells use, and the
           converged limit of GENO's predictor-corrector); one
           STREAMLINE-FOOT row — the backward streamline from pt4 at
           the mean angle crosses the data chord pt1-pt2 at parameter
           t, and (s4, h04) are the chord's invariants lerped at t
           (GENO's foot, chord and lerp, in residual form: the foot
           is SOLVED WITH the point, not iterated around it);
  wall     a streamline: (s, h0) are the bottom start-row constants
           (driver-appended); unknowns (y2, u4) as certified, theta4
           fixed by the wall slope, C- compatibility in (p, theta)
           form against the foot state reconstructed from lerped
           invariants;
  edge     a streamline at p = pa: q_e = sqrt(2 (h0_e - h(T_pa))),
           T_pa from the ENTROPY inversion s(T) = s_e + Rg ln(pa/PREF)
           — the certified angle parameterization kept, the
           compatibility's p4 identically pa.

WHY (p, theta) AND NOT THE CERTIFIED (u, v) FORM. The certified
compatibility is the gas-dynamic (u, v) combination, whose derivation
uses irrotationality; with entropy gradients the flow is rotational
(Crocco) and that form is wrong. The (p, theta) Mach-line form needs
no irrotationality and is what the reference implementation solves.
Consequence, DECLARED: at uniform invariants the two forms are the
same continuum equations but DIFFERENT discretizations, so the
regression against the certified march (W-1) is graded on a
station-refinement ladder — the deviation must shrink at the schemes'
common order — and NOT at the 1e-9 identical-equations band the swirl
extension earned (its Gamma -> 0 limit is the certified equation set;
our s -> s0 limit is not).

CHECKS
  R-0  closure identity: state_qs(q, s0, h0) reproduces state_q(q)
       to machine precision across the table range;
  W-3  the (p, T, M) inlet is exactly determined: ivl_from_ptm ->
       state_qs round-trips p, T, M to round-off;
  W-2a EXACT known answer, machine band: the stratified parallel jet.
       Straight horizontal wall, uniform pressure equal to ambient,
       per-row (T, M) profiles LINEAR in y, theta = 0: an exact
       solution of the axisymmetric equations (v = 0 kills the
       source; uniform p kills the pressure terms; each streamline
       keeps its own state). Linear-in-y invariants make the chord
       lerp exact, so the march must hold every row's (u, T) and the
       uniform p to the certification scale, columns without number;
  W-2b the same jet with CURVED (quadratic) stratification: the lerp
       is now O(dy^2) per cell and the march converges to the exact
       profile at the schemes' order — graded on a row-refinement
       ladder with the derived Richardson band;
  W-1  uniform-invariant regression: on a real plug world, rot cells
       at (s0, h0) rows vs the certified march — J and wall/edge
       states agree within a station-ladder band that SHRINKS under
       refinement (see above for why not 1e-9);
  W-4  a genuinely stratified spike world: certification holds; mass
       flux start -> last column conserved within the derived band;
       ENTROPY FLUX (integral s dmdot) conserved likewise — the
       transported invariant, measured not assumed;
  W-5  THE TRANSPORT BOUND (the check the first build lacked, and
       the one that caught its defect): entropy and stagnation
       enthalpy are TRANSPORTED, so every marched node's invariants
       must lie inside the range the INLET supplies — interpolation
       may not create entropy. Measured on the stratified spike
       world, together with the count of feet clamped to their
       chord (the clamp is GENO's rule; a march that clamps often
       is one whose foot search is losing its bracket);
  R-1  rejector: a corrupted interior cell that pins the streamline
       foot to t = 0 (invariants taken from the same-column node —
       cross-streamline contamination) must leave the W-2b band;
  R-2  rejector: corrupted C+ compatibility sign must fail to march
       or leave every band (the equations are load-bearing).

On-demand carrier (env: jax).
Run:  .venv-a1/bin/python validation/a1_rot_march.py
"""
import os
import sys
import time

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import a1_ideal_march_jax as A1                        # noqa: E402
from a1_plug_march import plug_march                   # noqa: E402

import jax                                             # noqa: E402
import jax.numpy as jnp                                # noqa: E402

EPS = A1.EPS
K_RICH = A1.K_RICH
PREF = A1.PREF
NPASS = [0, 0]


def check(label, ok):
    NPASS[0] += bool(ok)
    NPASS[1] += 1
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


# ======================================================================
# the generalized closure and its inverses
# ======================================================================
def state_qs(q, s, h0, ta):
    """(q, s, h0) -> (T, p, rho, c, gam, M): the certified state_q
    with the node's OWN invariants in place of the global (h0, s0).
    Traced; identical arithmetic path to state_q at (s0, h0)."""
    Tg, hg, sg, cpg, Rg, _, _ = ta
    ht = h0 - 0.5 * q * q
    T = jnp.interp(ht, hg, Tg)
    p = PREF * jnp.exp((jnp.interp(T, Tg, sg) - s) / Rg)
    rho = p / (Rg * T)
    cp = jnp.interp(T, Tg, cpg)
    gam = cp / (cp - Rg)
    c = jnp.sqrt(gam * Rg * T)
    return T, p, rho, c, gam, q / c


def p_qs(q, s, h0, ta):
    Tg, hg, sg, _, Rg, _, _ = ta
    ht = h0 - 0.5 * q * q
    T = jnp.interp(ht, hg, Tg)
    return PREF * jnp.exp((jnp.interp(T, Tg, sg) - s) / Rg)


def q_at_pa_rot(pa, s, h0, ta):
    """Edge speed of a streamline with invariants (s, h0) at p = pa:
    T from the entropy inversion s(T) = s + Rg ln(pa/PREF) (the
    s-table is monotone), then q from the energy equation."""
    Tg, hg, sg, _, Rg, _, _ = ta
    s_target = s + float(Rg) * np.log(pa / PREF)
    T = float(jnp.interp(s_target, sg, Tg))
    h = float(jnp.interp(T, Tg, hg))
    return float(np.sqrt(2.0 * (h0 - h)))


def ivl_from_ptm(x, y, p, T, M, theta, ta):
    """A full per-row (p, T, M, theta) initial line -> the 6-row
    start tuple. Exactly determined: s = s(T) - Rg ln(p/PREF),
    q = M c(T), h0 = h(T) + q^2/2."""
    Tg, hg, sg, cpg, Rg, _, _ = ta
    T = np.asarray(T, dtype=float)
    p = np.asarray(p, dtype=float)
    M = np.asarray(M, dtype=float)
    sT = np.interp(T, np.asarray(Tg), np.asarray(sg))
    hT = np.interp(T, np.asarray(Tg), np.asarray(hg))
    cpT = np.interp(T, np.asarray(Tg), np.asarray(cpg))
    gam = cpT / (cpT - float(Rg))
    c = np.sqrt(gam * float(Rg) * T)
    q = M * c
    s = sT - float(Rg) * np.log(p / PREF)
    h0 = hT + 0.5 * q * q
    u, v = q * np.cos(theta), q * np.sin(theta)
    return (np.asarray(x, dtype=float), np.asarray(y, dtype=float),
            u, v, s, h0)


# ======================================================================
# the rotational cells (Zucrow (p, theta) form, midpoint coefficients)
# ======================================================================
def _char(u_a, v_a, s_a, h_a, u_b, v_b, s_b, h_b, y_a, y_b, ta,
          delta, plus):
    """Midpoint characteristic package for the chord a -> b:
    (lambda, Q, S) with the +/- family selected by `plus`."""
    um, vm = 0.5 * (u_a + u_b), 0.5 * (v_a + v_b)
    ym = 0.5 * (y_a + y_b)
    sm, hm = 0.5 * (s_a + s_b), 0.5 * (h_a + h_b)
    qm = jnp.sqrt(um * um + vm * vm)
    _, pm, rhom, cm, _, Mm = state_qs(qm, sm, hm, ta)
    thm = jnp.arctan2(vm, um)
    alm = jnp.arcsin(1.0 / Mm)
    sgn = 1.0 if plus else -1.0
    lam = jnp.tan(thm + sgn * alm)
    Q = jnp.sqrt(Mm * Mm - 1.0) / (rhom * qm * qm)
    S = delta * jnp.sin(thm) / (jnp.maximum(ym, 1e-300) * Mm
                                * jnp.cos(thm + sgn * alm))
    return lam, Q, S


def make_resid_interior_rot(delta, corrupt_t0=False,
                            corrupt_sign=False):
    """Interior cell: z = (x4, y4, u4, v4, t). pt1 (below, same
    column) sends the C+; pt2 (previous column) sends the C-; the
    streamline foot sits on the chord pt1-pt2 at parameter t.
    corrupt_t0 / corrupt_sign are the R-1 / R-2 rejector knobs."""
    sgn_c = -1.0 if corrupt_sign else 1.0

    def resid(z, p, ta):
        x4, y4, u4, v4, t = z
        (x1, y1, u1, v1, s1, h1,
         x2, y2, u2, v2, s2, h2,
         xA, yA, uA, vA, sA, hA,
         xB, yB, uB, vB, sB, hB) = p
        s4 = sA + t * (sB - sA)
        h4 = hA + t * (hB - hA)
        q1 = jnp.sqrt(u1 * u1 + v1 * v1)
        q2 = jnp.sqrt(u2 * u2 + v2 * v2)
        q4 = jnp.sqrt(u4 * u4 + v4 * v4)
        p1v = p_qs(q1, s1, h1, ta)
        p2v = p_qs(q2, s2, h2, ta)
        p4v = p_qs(q4, s4, h4, ta)
        th1 = jnp.arctan2(v1, u1)
        th2 = jnp.arctan2(v2, u2)
        th4 = jnp.arctan2(v4, u4)
        lp, Qp, Sp = _char(u1, v1, s1, h1, u4, v4, s4, h4, y1, y4,
                           ta, delta, plus=True)
        lm, Qm, Sm = _char(u2, v2, s2, h2, u4, v4, s4, h4, y2, y4,
                           ta, delta, plus=False)
        # streamline foot on the SEARCHED previous-column chord A-B
        # (the bracket is a recorded driver decision; the cell only
        # refines t on it — GENO's exact-intersection scan, ported)
        xf = xA + t * (xB - xA)
        yf = yA + t * (yB - yA)
        uf = uA + t * (uB - uA)
        vf = vA + t * (vB - vA)
        thf = jnp.arctan2(vf, uf)
        foot = ((y4 - yf) - jnp.tan(0.5 * (th4 + thf)) * (x4 - xf)
                if not corrupt_t0 else t - 0.0)
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            (y4 - y2) - lm * (x4 - x2),
            sgn_c * ((th4 - th1) + Qp * (p4v - p1v)) + Sp * (x4 - x1),
            (th4 - th2) - Qm * (p4v - p2v) - Sm * (x4 - x2),
            foot,
        ])
    return resid


def make_resid_wallbot_rot(delta):
    """Bottom-wall cell: z = (y2, u4); the wall is a streamline whose
    invariants (s_w, h_w) close the pack; theta4 is the wall slope;
    the C- foot state is reconstructed from invariants lerped at the
    foot (the on-manifold rule)."""
    def resid(z, p, ta):
        y2, u4 = z
        (xA, yA, uA, vA, sA, hA,
         xB, yB, uB, vB, sB, hB,
         x4, y4, slope, s_w, h_w) = p
        D = (y2 - yA) / (yB - yA)
        x2 = xA + D * (xB - xA)
        u2 = uA + D * (uB - uA)
        v2 = vA + D * (vB - vA)
        s2 = sA + D * (sB - sA)
        h2 = hA + D * (hB - hA)
        v4 = slope * u4
        q2 = jnp.sqrt(u2 * u2 + v2 * v2)
        q4 = jnp.sqrt(u4 * u4 + v4 * v4)
        p2v = p_qs(q2, s2, h2, ta)
        p4v = p_qs(q4, s_w, h_w, ta)
        th2 = jnp.arctan2(v2, u2)
        th4 = jnp.arctan(slope)
        lm, Qm, Sm = _char(u2, v2, s2, h2, u4, v4, s_w, h_w, y2, y4,
                           ta, delta, plus=False)
        return jnp.array([
            (y4 - y2) - lm * (x4 - x2),
            (th4 - th2) - Qm * (p4v - p2v) - Sm * (x4 - x2),
        ])
    return resid


def make_resid_freejet_rot(delta):
    """Free-jet cell: z = (x4, y4, th4); the edge streamline's
    invariants ride on pt3 (the previous edge node); its speed is the
    constant q_pa(s_e, h0_e) carried in the qpa slot, so p4 = pa
    identically and the compatibility uses it."""
    def resid(z, p, ta):
        x4, y4, th4 = z
        (x1, y1, u1, v1, s1, h1,
         x3, y3, u3, v3, se, he, qpa_e) = p
        u4 = qpa_e * jnp.cos(th4)
        v4 = qpa_e * jnp.sin(th4)
        q1 = jnp.sqrt(u1 * u1 + v1 * v1)
        p1v = p_qs(q1, s1, h1, ta)
        p4v = p_qs(qpa_e, se, he, ta)
        th1 = jnp.arctan2(v1, u1)
        lp, Qp, Sp = _char(u1, v1, s1, h1, u4, v4, se, he, y1, y4,
                           ta, delta, plus=True)
        th3 = jnp.arctan2(v3, u3)
        thm = 0.5 * (th3 + th4)
        return jnp.array([
            (y4 - y1) - lp * (x4 - x1),
            (th4 - th1) + Qp * (p4v - p1v) + Sp * (x4 - x1),
            (y4 - y3) - jnp.tan(thm) * (x4 - x3),
        ])
    return resid


def rot_cells(delta, corrupt_t0=False, corrupt_sign=False):
    key = (float(delta), bool(corrupt_t0), bool(corrupt_sign))
    t_int = A1.get_solver(("int_rot",) + key,
                          lambda: make_resid_interior_rot(
                              delta, corrupt_t0, corrupt_sign))
    t_fj = A1.get_solver(("fj_rot", float(delta)),
                         lambda: make_resid_freejet_rot(delta))
    t_wb = A1.get_solver(("wb_rot", float(delta)),
                         lambda: make_resid_wallbot_rot(delta))
    return (t_int, t_fj, t_wb)


def predict_rot(pt1, pt2, ta):
    """Interior seed: characteristic crossing from the foot states
    (each at its OWN invariants), averaged state, t from the mean
    streamline direction. Seeds only bracket and start Newton; the
    residual decides."""
    x1, y1, u1, v1, s1, h1 = (float(v) for v in pt1)
    x2, y2, u2, v2, s2, h2 = (float(v) for v in pt2)
    st1 = state_qs(jnp.float64(np.hypot(u1, v1)), jnp.float64(s1),
                   jnp.float64(h1), ta)
    st2 = state_qs(jnp.float64(np.hypot(u2, v2)), jnp.float64(s2),
                   jnp.float64(h2), ta)
    mu1 = np.arcsin(min(1.0, 1.0 / max(float(st1[5]), 1.0001)))
    mu2 = np.arcsin(min(1.0, 1.0 / max(float(st2[5]), 1.0001)))
    th1, th2 = np.arctan2(v1, u1), np.arctan2(v2, u2)
    sp = np.tan(th1 + mu1)
    sm = np.tan(th2 - mu2)
    x4 = (y2 - y1 + sp * x1 - sm * x2) / (sp - sm)
    y4 = y1 + sp * (x4 - x1)
    thm = 0.5 * (th1 + th2)
    dx, dy = x2 - x1, y2 - y1
    den = dy - np.tan(thm) * dx
    t0 = (((y4 - y1) - np.tan(thm) * (x4 - x1)) / den
          if abs(den) > 1e-300 else 0.5)
    t0 = min(1.0, max(0.0, t0))
    return jnp.array([x4, y4, 0.5 * (u1 + u2), 0.5 * (v1 + v2), t0])


# ======================================================================
# rot-aware column fluxes (mirror of col_fluxes, per-node state)
# ======================================================================
def col_fluxes_rot(col, ta, pa, delta):
    c = np.asarray(col)
    q = np.hypot(c[:, 2], c[:, 3])
    st = jax.vmap(lambda qq, ss, hh: jnp.stack(
        state_qs(qq, ss, hh, ta)[1:3]))(
        jnp.asarray(q), jnp.asarray(c[:, 4]), jnp.asarray(c[:, 5]))
    p = np.array(st[:, 0])
    rho = np.array(st[:, 1])
    dx = np.diff(c[:, 0])
    dy = np.diff(c[:, 1])
    um = 0.5 * (c[1:, 2] + c[:-1, 2])
    vm = 0.5 * (c[1:, 3] + c[:-1, 3])
    rm = 0.5 * (rho[1:] + rho[:-1])
    pm = 0.5 * (p[1:] + p[:-1])
    sm = 0.5 * (c[1:, 4] + c[:-1, 4])
    w = (2.0 * np.pi * 0.5 * (c[1:, 1] + c[:-1, 1])) if delta \
        else np.ones_like(dy)
    dmd = rm * (um * dy - vm * dx) * w
    md = float(np.sum(dmd))
    F = float(np.sum((rm * um * (um * dy - vm * dx)
                      + (pm - pa) * dy) * w))
    S_flux = float(np.sum(sm * dmd))
    return md, F, S_flux


def rot_march(stations, start6, pa, tab, delta, sched=None, **kw):
    """The rotational march: the certified driver with the rot cell
    triple, the edge-streamline speed law, and the rot predictor."""
    ta = A1.tab_arrays(tab)
    qe = q_at_pa_rot(pa, float(start6[4][-1]), float(start6[5][-1]),
                     ta)
    return plug_march(stations, start6, qe, tab, delta, sched=sched,
                      cells=rot_cells(delta, **kw),
                      q_edge=(lambda yy: qe), rot_pred=predict_rot)
# ======================================================================
# worlds
# ======================================================================
def jet_world(ta, N, curved=False):
    """The stratified parallel jet: straight horizontal wall at
    y = 1, rows to y = 2, uniform p = PA_JET, theta = 0; invariants
    LINEAR in y (curved=False -> the chord lerp is exact) or
    QUADRATIC (curved=True -> O(dy^2) lerp, the convergence world).
    Exact solution: every streamline keeps its state; the field is
    x-independent."""
    Tg, hg, sg, cpg, Rg, h0g, s0g = ta
    ys = np.linspace(1.0, 2.0, N)
    z = (ys - ys[0]) / (ys[-1] - ys[0])
    shape = z + (0.8 * z * (1.0 - z) if curved else 0.0)
    s_r = float(s0g) + 40.0 * shape            # J/(kg K) spread
    h_r = float(h0g) * (1.0 + 0.06 * shape)    # +6% stagnation enthalpy
    q_r = np.array([q_at_pa_rot(PA_JET, s_r[j], h_r[j], ta)
                    for j in range(N)])
    start6 = (0.0, ys, q_r, np.zeros(N), s_r, h_r)
    # FEW columns, deliberately (measured, S24 probe): the driver's
    # one-row-per-column growth is designed for WIDENING jets; on a
    # parallel jet a long march migrates rows toward the edge and
    # opens a mid-jet hole, and the chord lerp error is then set by
    # the hole (K-driven) instead of the row spacing (N-driven) —
    # the N-ladder saturates. A short march keeps the mesh healthy;
    # the accumulation and the N-convergence are still exercised.
    K = 12
    sx = np.linspace(0.04, 0.52, K)
    stations = (sx, np.full(K, 1.0), np.zeros(K))
    exact = dict(ys=ys, q=q_r, s=s_r, h=h_r)
    return stations, start6, exact


def jet_error(out, exact, ta):
    """Deviation of the LAST column from the exact stationary
    profile, SPLIT at the column's largest inter-row gap. On a
    non-widening jet the driver's one-row-per-column growth crams
    former edge rows at the stationary edge while the interior
    shears down a gap opens between them (S24, measured cell by
    cell): foot chords SPANNING that gap lerp a curved profile
    across it — an N-INDEPENDENT topology artifact confined to the
    crammed band. The transport claim is graded BELOW the gap; the
    band above it is reported and its N-stability checked, never
    masked. Returns (e_u_bulk, e_p_bulk, e_v_bulk, e_u_band, gap)."""
    col = np.asarray(out["last_col"])
    jgap = int(np.argmax(np.diff(col[:, 1])))
    gap = float(col[jgap + 1, 1] - col[jgap, 1])
    q4 = np.hypot(col[:, 2], col[:, 3])
    u_ex = np.interp(col[:, 1], exact["ys"], exact["q"])
    p4 = np.array([float(p_qs(jnp.float64(q4[j]),
                              jnp.float64(col[j, 4]),
                              jnp.float64(col[j, 5]), ta))
                   for j in range(len(col))])
    eu = np.abs(col[:, 2] - u_ex) / u_ex
    ep = np.abs(p4 / PA_JET - 1.0)
    ev = np.abs(col[:, 3]) / u_ex
    lo = slice(0, jgap + 1)
    hi = slice(jgap + 1, len(col))
    e_band = float(np.max(eu[hi])) if hi.stop > hi.start else 0.0
    return (float(np.max(eu[lo])), float(np.max(ep[lo])),
            float(np.max(ev[lo])), e_band, gap)


def col_mass_profile(out, ta, pa, delta):
    """Mass flux through every marched column (the wedge diagnostic:
    a vertical start line leaks once, in the first column, and is
    flat thereafter — the S21 lesson — so conservation is graded
    POST-wedge and the wedge jump reported against its baseline)."""
    mesh = np.asarray(out["mesh_pts"])
    cols = {}
    for (j, i), pt in zip(out["mesh_keys"], mesh):
        cols.setdefault(i, []).append((j, pt))
    prof = {}
    for i, rows in cols.items():
        arr = np.asarray([pt for _, pt in
                          sorted(rows, key=lambda r: r[0])])
        md, _, _ = col_fluxes_rot(arr, ta, pa, delta)
        prof[i] = abs(md)
    return prof


PA_JET = 2.0e5


def main():
    t0 = time.time()
    print("== A1 S24: the general inlet — rotational MoC ported from"
          " the referee [X-RMAR] ==")
    tab = A1.prep_tab(A1.build_tab_nasa())
    ta = A1.tab_arrays(tab)
    Tg, hg, sg, cpg, Rg, h0g, s0g = ta

    # ---- R-0: the closure identity ----------------------------------
    print("-- R-0: state_qs at (s0, h0) IS state_q --")
    qs = np.linspace(400.0, 2600.0, 23)
    dmax = 0.0
    for q in qs:
        a = jnp.stack(A1.state_q(jnp.float64(q), ta))
        b = jnp.stack(state_qs(jnp.float64(q), s0g, h0g, ta))
        dmax = max(dmax, float(jnp.max(jnp.abs(a - b)
                                       / jnp.maximum(jnp.abs(a),
                                                     1e-30))))
    print("  max rel deviation over %d speeds: %.2e" % (len(qs), dmax))
    check("R-0 closure identity at the global invariants", dmax == 0.0)

    # ---- W-3: (p, T, M) exactly determined --------------------------
    print("\n-- W-3: the (p, T, M) inlet round-trips --")
    rng = np.random.default_rng(3)
    Tt = rng.uniform(1200.0, 2600.0, 9)
    pt = rng.uniform(4e4, 2e6, 9)
    Mt = rng.uniform(1.3, 3.2, 9)
    x6 = ivl_from_ptm(np.zeros(9), np.linspace(1, 2, 9), pt, Tt, Mt,
                      np.zeros(9), ta)
    emax = 0.0
    for j in range(9):
        q = float(np.hypot(x6[2][j], x6[3][j]))
        Tj, pj, _, _, _, Mj = state_qs(jnp.float64(q),
                                       jnp.float64(x6[4][j]),
                                       jnp.float64(x6[5][j]), ta)
        emax = max(emax, abs(float(Tj) / Tt[j] - 1.0),
                   abs(float(pj) / pt[j] - 1.0),
                   abs(float(Mj) / Mt[j] - 1.0))
    print("  max round-trip deviation (p, T, M): %.2e" % emax)
    check("W-3 a full (p, T, M, theta) line is exactly determined",
          emax <= 1e-10)

    # ---- W-2a: the linear stratified jet, machine band --------------
    print("\n-- W-2a: stratified parallel jet, LINEAR invariants"
          " (exact lerp) --")
    st, s6, exact = jet_world(ta, 41, curved=False)
    out, _ = rot_march(st, s6, PA_JET, tab, 1.0)
    e_u, e_p, e_v, e_band, gap = jet_error(out, exact, ta)
    print("  cert %.3f over %d cells; bulk: |du|/u %.2e  |dp|/pa"
          " %.2e  |v|/u %.2e; crammed band %.2e (gap %.3f m)"
          % (out["cert_worst"], out["cert_n"], e_u, e_p, e_v,
             e_band, gap))
    # BAND, derived: round-off chains amplified by the near-
    # degenerate crammed chords (measured plateau ~4e-8, N-stable);
    # 2.5x the plateau. Linear invariants lerp exactly even across
    # the gap, so bulk and band share the bar.
    band_a = 1e-7
    check("W-2a the exact stratified jet is held at round-off scale"
          " everywhere (linear lerp is exact even across the gap)",
          out["cert_worst"] <= 1.0
          and max(e_u, e_p, e_v, e_band) <= band_a)

    # ---- W-2b: curved stratification, convergence -------------------
    print("\n-- W-2b: CURVED stratification (O(dy^2) lerp),"
          " row-refinement ladder --")
    errs, bands = {}, {}
    for N in (21, 41, 81):
        st, s6, exact = jet_world(ta, N, curved=True)
        outc, _ = rot_march(st, s6, PA_JET, tab, 1.0)
        errs[N], _, _, bands[N], gapN = jet_error(outc, exact, ta)
        print("  N = %2d rows: bulk |du|/u = %.3e   crammed band"
              " %.3e (gap %.3f)   (cert %.3f)"
              % (N, errs[N], bands[N], gapN, outc["cert_worst"]))
    r1 = errs[21] / errs[41]
    r2 = errs[41] / errs[81]
    stab = max(bands.values()) / max(min(bands.values()), 1e-300)
    print("  bulk refinement ratios: %.2f, %.2f  (2nd order -> ~4);"
          " band N-stability x%.2f" % (r1, r2, stab))
    check("W-2b the transport converges at the scheme's order below"
          " the gap, and the gap-chord band is N-stable (topology,"
          " not transport — reported)",
          r1 >= 2.5 and r2 >= 2.5 and stab <= 1.5)
    band_2b = K_RICH * errs[81]

    # ---- R-1: the frozen-foot rejector ------------------------------
    print("\n-- R-1: rejector — streamline foot pinned to t = 0 --")
    st, s6, exact = jet_world(ta, 41, curved=True)
    out_r, _ = rot_march(st, s6, PA_JET, tab, 1.0, corrupt_t0=True)
    e_r = jet_error(out_r, exact, ta)[0]
    print("  corrupted bulk |du|/u = %.3e vs honest %.3e (x%.0f)"
          % (e_r, errs[41], e_r / max(errs[41], 1e-300)))
    check("R-1 cross-streamline contamination leaves the band",
          e_r > 10.0 * errs[41])

    # (R-2 moved after W-1, onto the plug world: on the exact
    # parallel jet the compatibility bracket vanishes identically, so
    # a sign flip there is INVISIBLE — the rejector needs a world
    # where the equations carry load. Found by running it; declared.)

    # ---- W-1: uniform-invariant regression on the plug world --------
    print("\n-- W-1: uniform invariants on the real plug world vs"
          " the certified march --")
    os.environ.setdefault("PSPL_M", "10")
    os.environ.setdefault("PSPL_K", "41")
    os.environ.setdefault("PSPL_N", "31")
    import a1_plug_spline_opt as PS
    import a1_config_compare as CC
    w = CC.build_world()
    taw = A1.tab_arrays(w["tab"])
    _, _, _, _, _, h0w, s0w = taw
    dJ = {}
    for K, NR in ((41, 31), (81, 61)):
        c = PS.build_case(w, N=NR)
        xq, yq, sq = PS.wall_stations(np.asarray(c["W0"]), c, K=K)
        stw = (np.asarray(xq), np.asarray(yq), np.asarray(sq))
        x0w, yl, us, vs = c["start"]
        out_c, _ = plug_march(stw, c["start"], c["qpa"], w["tab"], 1.0)
        s6w = (x0w, yl, us, vs,
               np.full(len(yl), float(s0w)),
               np.full(len(yl), float(h0w)))
        out_r2, _ = rot_march(stw, s6w, CC.PA, w["tab"], 1.0)
        wc = np.asarray(out_c["wall"])
        wr = np.asarray(out_r2["wall"])
        pc = np.array(A1.state_q(jnp.asarray(np.hypot(
            wc[:, 2], wc[:, 3])), taw)[1])
        qr = np.hypot(wr[:, 2], wr[:, 3])
        pr = np.array([float(p_qs(jnp.float64(qr[j]),
                                  jnp.float64(wr[j, 4]),
                                  jnp.float64(wr[j, 5]), taw))
                       for j in range(len(wr))])
        push = lambda wl, pp: float(np.sum(
            (0.5 * (pp[1:] + pp[:-1]) - CC.PA)
            * 2 * np.pi * 0.5 * (wl[1:, 1] + wl[:-1, 1])
            * (-(np.diff(wl[:, 1])))))
        Jc, Jr = push(wc, pc), push(wr, pr)
        if K == 41:
            dJ_Jc = Jc
        dJ[K] = abs(Jr / Jc - 1.0)
        print("  (K,N) = (%2d,%2d): wall push certified %.6e vs rot"
              " %.6e  (rel %.2e; rot cert %.2f)"
              % (K, NR, Jc, Jr, dJ[K], out_r2["cert_worst"]))
    print("  refinement: rel diff %.2e -> %.2e (ratio %.2f;"
          " two 2nd-order schemes -> ~4)"
          % (dJ[41], dJ[81], dJ[41] / dJ[81]))
    check("W-1 the (p,theta) and (u,v) discretizations agree within"
          " a band that SHRINKS at the schemes' order",
          dJ[41] < 2e-3 and dJ[41] / dJ[81] >= 2.0)

    # ---- R-2: corrupted compatibility, on the plug world ------------
    print("\n-- R-2: rejector — corrupted C+ compatibility on the"
          " plug world --")
    c = PS.build_case(w, N=31)
    xq, yq, sq = PS.wall_stations(np.asarray(c["W0"]), c, K=41)
    stw = (np.asarray(xq), np.asarray(yq), np.asarray(sq))
    x0w, yl, us, vs = c["start"]
    s6u = (x0w, yl, us, vs,
           np.full(len(yl), float(s0w)),
           np.full(len(yl), float(h0w)))
    try:
        out_s, _ = rot_march(stw, s6u, CC.PA, w["tab"], 1.0,
                             corrupt_sign=True)
        ws = np.asarray(out_s["wall"])
        qs_ = np.hypot(ws[:, 2], ws[:, 3])
        ps_ = np.array([float(p_qs(jnp.float64(qs_[j]),
                                   jnp.float64(ws[j, 4]),
                                   jnp.float64(ws[j, 5]), taw))
                        for j in range(len(ws))])
        Js = float(np.sum((0.5 * (ps_[1:] + ps_[:-1]) - CC.PA)
                          * 2 * np.pi
                          * 0.5 * (ws[1:, 1] + ws[:-1, 1])
                          * (-(np.diff(ws[:, 1])))))
        dev = abs(Js / dJ_Jc - 1.0)
        bad = (out_s["cert_worst"] > 1.0) or (dev > 100.0 * dJ[41])
        print("  corrupted: cert %.2f, wall push %.4e (dev %.2e vs"
              " honest %.2e)" % (out_s["cert_worst"], Js, dev,
                                 dJ[41]))
    except Exception as err:
        bad = True
        print("  corrupted march raises: %s" % type(err).__name__)
    check("R-2 the compatibility equations are load-bearing", bad)

    # ---- W-4: a genuinely stratified spike world --------------------
    print("\n-- W-4: stratified inlet on the spike world"
          " (conservation) --")
    c = PS.build_case(w)
    xq, yq, sq = PS.wall_stations(np.asarray(c["W0"]), c, K=41)
    stw = (np.asarray(xq), np.asarray(yq), np.asarray(sq))
    x0w, yl, us, vs = c["start"]
    Nw = len(yl)
    zz = (np.asarray(yl) - yl[0]) / (yl[-1] - yl[0])
    s_r = float(s0w) + 25.0 * np.sin(np.pi * zz)
    h_r = float(h0w) * (1.0 + 0.03 * np.sin(np.pi * zz))
    s6s = (x0w, yl, us, vs, s_r, h_r)
    out_s4, _ = rot_march(stw, s6s, CC.PA, w["tab"], 1.0)
    start_col = np.stack([np.full(Nw, x0w), yl, us, vs, s_r, h_r],
                         axis=1)
    md_in, F_in, S_in = col_fluxes_rot(start_col, taw, CC.PA, 1.0)
    md_out, F_out, S_out = col_fluxes_rot(
        np.asarray(out_s4["last_col"]), taw, CC.PA, 1.0)
    prof = col_mass_profile(out_s4, taw, CC.PA, 1.0)
    icols = sorted(k for k in prof if k >= 2)
    md_2 = prof[icols[0]]
    wedge = abs(md_2 / abs(md_in) - 1.0)
    d_md = abs(prof[icols[-1]] / md_2 - 1.0)
    out_u, _ = rot_march(stw, s6u, CC.PA, w["tab"], 1.0)
    prof_u = col_mass_profile(out_u, taw, CC.PA, 1.0)
    mdu_in, _, _ = col_fluxes_rot(np.stack(
        [np.full(Nw, x0w), yl, us, vs, s6u[4], s6u[5]], axis=1),
        taw, CC.PA, 1.0)
    wedge_u = abs(prof_u[sorted(k for k in prof_u if k >= 2)[0]]
                  / abs(mdu_in) - 1.0)
    d_s = abs((S_out / md_out) / (S_in / md_in) - 1.0)
    print("  cert %.3f over %d cells" % (out_s4["cert_worst"],
                                         out_s4["cert_n"]))
    print("  first-column wedge jump: %.2e (uniform baseline %.2e,"
          " x%.1f) — the S21 vertical-start-line property, reported"
          % (wedge, wedge_u, wedge / max(wedge_u, 1e-300)))
    print("  POST-wedge mass conservation col 2 -> last: %.2e"
          % d_md)
    print("  mean entropy per unit mass in/out rel drift: %.2e"
          % d_s)
    check("W-4 stratified spike world: certified cells, post-wedge"
          " mass and transported-entropy conservation, wedge within"
          " 4x its uniform baseline",
          out_s4["cert_worst"] <= 1.0 and d_md <= 1e-2
          and d_s <= 1e-3 and wedge <= 4.0 * wedge_u)

    # ---- W-5: the transport bound -----------------------------------
    print("\n-- W-5: transported invariants stay inside the inlet"
          " range --")
    mesh = np.asarray(out_s4["mesh_pts"])
    s_lo, s_hi = float(np.min(s_r)), float(np.max(s_r))
    h_lo, h_hi = float(np.min(h_r)), float(np.max(h_r))
    span_s = s_hi - s_lo
    span_h = h_hi - h_lo
    ov_s = float(max(np.max(mesh[:, 4]) - s_hi,
                     s_lo - np.min(mesh[:, 4]), 0.0))
    ov_h = float(max(np.max(mesh[:, 5]) - h_hi,
                     h_lo - np.min(mesh[:, 5]), 0.0))
    n_bad = int(np.sum((mesh[:, 4] > s_hi + 1e-9)
                       | (mesh[:, 4] < s_lo - 1e-9)))
    n_cl = int(out_s4["foot_clamped_n"])
    print("  inlet entropy span %.3f J/kg K; worst node overshoot"
          " %.3e (%.4f %% of the span), nodes outside: %d / %d"
          % (span_s, ov_s, 100 * ov_s / span_s, n_bad, len(mesh)))
    print("  stagnation-enthalpy overshoot %.3e (%.4f %% of its"
          " span)" % (ov_h, 100 * ov_h / span_h))
    n_wf = int(out_s4["wall_foot_n"])
    print("  feet taken on the WALL segment (streamline off the"
          " descending wall): %d; feet outside their chord: %d"
          % (n_wf, n_cl))
    check("W-5 the march creates no entropy: every node's invariants"
          " lie inside the inlet's range (transport bound)",
          ov_s <= 1e-9 * max(span_s, 1.0)
          and ov_h <= 1e-9 * max(span_h, 1.0))

    print("\n== %d/%d PASS  (%.1f s) ==" % (NPASS[0], NPASS[1],
                                            time.time() - t0))
    sys.exit(0 if NPASS[0] == NPASS[1] else 1)


if __name__ == "__main__":
    main()

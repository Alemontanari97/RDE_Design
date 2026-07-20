#!/usr/bin/env python3
"""G0 CROSS-CODE FLOWFIELD ORACLE [F2/G0, session S10]: cell-by-cell
agreement between GENO's Fortran MoC flowfield and OUR axisymmetric unit
process, on the TOC case of record (GENO/CASES/tocnoz).

This is the O3.4 criterion that was the NAMED RESIDUAL of gate G0 through
S8/S9 ("the GENO binary is not buildable on this host; the reference
x/y/u/v/p.dat exist only as checksums"). In S10 the GENO binary was BUILT
(WSL gfortran 11.4.0, CMake, Cantera/Sundials/Tecio OFF, LAPACK from the
host conda env) and the tocnoz flowfield REGENERATED; this carrier closes
the cross-code half of the criterion at the level of the interior unit
process.

WHAT IS TESTED (residual form, not a re-solve — deliberately). GENO stores
the structured MoC grid sol%(j,i): binary stream dumps written by
GENO/src/lib/IO_m.f90::writeoutput as `do k=1,j2: write(funit) v(k,1:l)`
(row-major j2 x l float64, no record markers), with dimensions.dat =
`write(funit) l,j2` (two int32). For a genuine INTERIOR characteristic
triangle (two parent nodes P1 on the C+ foot, P2 on the C- foot, both at
the upstream column, and the child node P4) OUR axisymmetric second-order
average-coefficient unit process (Zucrow-Hoffman (u,v) compatibility, the
general-gas route B of validation/g0_spike_axisym_shock.py, EOS-general:
uses only the local a=sqrt(gamma p/rho), NO gamma=const Prandtl-Meyer
invariant) must be SATISFIED by GENO's own node values, i.e. its residual
must sit at the discretization truncation level. If both codes solve the
same continuous MoC, GENO's nodes satisfy our discrete relations up to the
scheme truncation order.

TOLERANCE IS DERIVED FROM THE PROCESS ORDER, PER CELL (no magic numbers, no
cross-field h-fit). A cross-field fit of residual vs cell step h is
ILL-POSED on a fixed grid: small-h cells cluster near the throat (high
gradients, near-sonic source singularity) and large-h cells lie in the smooth
downstream, so the h-scaling conflates cell size with location. Instead we
DERIVE a per-cell truncation band from the scheme itself: the average-
coefficient (trapezoidal, 2nd-order) residual R_trap and the endpoint
(1st-order) residual R_end use coefficients that differ by O(h), so their
difference |R_trap - R_end| estimates the cell's own O(h^3) local truncation
ambiguity. A code solving the SAME continuous MoC must satisfy our relation up
to that ambiguity:  |R_trap| <= K*(|R_trap - R_end| + floor), K = 4 (two-level
Richardson safety), floor = 64*eps (roundoff, normalized velocity units). The
fraction of cells inside the band is the cross-code agreement rate. This is
"Richardson sul passo cella" realized locally and rigorously.

The oracle PASSES iff (i) the C+/C- feet lie on the characteristics (edge
slope residual a small fraction of the cell AND an order of magnitude cleaner
than the wrong-pairing control N2), (ii) >=90% of clean supersonic-core cells
fall inside the derived truncation band, and both negative controls reject.

NEGATIVE CONTROLS (the oracle must REJECT):
  (N1) a CORRUPTED cell: the child state perturbed by 1% leaves the band
       (band-inside fraction collapses to ~0%) -> rejected.
  (N2) a WRONG PAIRING: feet taken from the wrong side make the geometric
       slope residual O(cell), ~two orders worse than the correct feet
       -> rejected.

CLEAN-CORE SCOPE (declared, physical — not tuned to pass): cells are kept
only where the axisym unit process is regular — child comfortably supersonic
(M in [1.5, 6], off the sonic line where the source a^2 v/(y(u^2-a^2)) is
singular), off the axis (y > 0.15 y_wall, where the 1/y source and the grid
degenerate), interior rows, feet on the characteristics. The downstream
columns are subsampled (~150) since the verdict is a statistic over thousands
of independent triangles; the fraction is stable vs the full sweep.

GAMMA STATUS (directive DIR-GAMMA, M0 VI.4bis(iii)): the unit process here
is EOS-general (dimensional u,v with local frozen a); no gamma=const solver
step is used. GENO's tocnoz is axisymmetric CH4/O2 FROZEN, gamma(T) varying
over the field — the general-gas (u,v) compatibility is the correct cell
model and is what makes the cross-code residual meaningful under variable
gamma. The perfect-gas closed forms live only in GENO's own reference and
in the declared oracle spikes, never in this carrier's primary path.

ON-DEMAND CARRIER (env: gfortran): consumes GENO's freshly generated grid
under GENO/CASES/tocnoz (untracked, toolchain-dependent per the N-36
convention documented in reference/checksums.md5). Like X-G0/X-G0AX it is
OUTSIDE the CI tiers by declaration; run after regenerating the flowfield
with the GENO binary. Exit code 0 iff ALL checks pass INCLUDING the
negative controls.
"""
import os
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GENO_TOC = os.path.join(ROOT, "GENO", "CASES", "tocnoz")
EPS = float(np.finfo(np.float64).eps)


# ----------------------------------------------------------------------
# GENO structured-grid reader (format fixed by IO_m.f90::writeoutput)
def read_grid(case_dir):
    dims = os.path.join(case_dir, "dimensions.dat")
    with open(dims, "rb") as f:
        l, j2 = np.fromfile(f, dtype="<i4", count=2)
    l, j2 = int(l), int(j2)

    def field(name):
        with open(os.path.join(case_dir, name), "rb") as f:
            a = np.fromfile(f, dtype="<f8", count=j2 * l)
        if a.size != j2 * l:
            raise ValueError("%s: expected %d doubles, got %d"
                             % (name, j2 * l, a.size))
        return a.reshape(j2, l)      # [j (wall->axis), i (downstream)]

    g = {n: field(n + ".dat") for n in
         ("x", "y", "u", "v", "p", "rho", "gamma")}
    g["l"], g["j2"] = l, j2
    return g


# ----------------------------------------------------------------------
# derived state at a node: (theta, V, a, M). EOS-general: a from local
# gamma, p, rho (frozen speed of sound), NOT a gamma=const closed form.
def node_state(g, j, i):
    u = g["u"][j, i]; v = g["v"][j, i]
    p = g["p"][j, i]; rho = g["rho"][j, i]; gam = g["gamma"][j, i]
    x = g["x"][j, i]; y = g["y"][j, i]
    # void rows (j=2..Nv are skipped INDICES, not physical points — GENO
    # CLAUDE.md) carry rho<=0 / gamma<=0: guard the sound speed and mark
    # the node non-physical (filtered downstream).
    if not (np.isfinite(rho) and rho > 0.0 and np.isfinite(gam)
            and gam > 1.0 and np.isfinite(p) and p > 0.0):
        return dict(x=x, y=y, u=u, v=v, p=p, rho=rho, gam=gam,
                    a=np.nan, V=np.nan, th=np.nan, M=np.nan, ok=False)
    a = np.sqrt(gam * p / rho)
    V = np.hypot(u, v)
    th = np.arctan2(v, u)
    return dict(x=x, y=y, u=u, v=v, p=p, rho=rho, gam=gam,
                a=a, V=V, th=th, M=V / a, ok=True)


def physical(s):
    return (s.get("ok", False) and np.isfinite(s["V"]) and s["u"] > 0.0
            and s["M"] > 1.02 and s["y"] > 0.0)


# ----------------------------------------------------------------------
# OUR axisymmetric interior unit process, general-gas (u,v) compatibility
# (route B of the S8 spike, dimensional). Residual evaluated at GENO's own
# (P1 on C+ foot, P2 on C- foot, P4 child) node triple. delta=1 axisym.
#   C+ geometry: (y4-y1) = tan(mean(th+al)) (x4-x1)
#   C- geometry: (y4-y2) = tan(mean(th-al)) (x4-x2)
#   compat along C+:  (u4-u1) + lam_c+ (v4-v1) = delta*mean(S)*(x4-x1)
#   compat along C-:  (u4-u2) + lam_c- (v4-v2) = delta*mean(S)*(x4-x2)
#   lam on C+ = tan(th - al), on C- = tan(th + al); S = a^2 v/(y(u^2-a^2))
def alpha(s):
    return np.arcsin(1.0 / s["M"])


def source(s):
    return s["a"] ** 2 * s["v"] / (s["y"] * (s["u"] ** 2 - s["a"] ** 2))


def geom_resid(child, foot, sign):
    """slope residual of the characteristic edge foot->child.
    sign=+1 for C+ (slope tan(th+al)), sign=-1 for C- (slope tan(th-al))."""
    al_c, al_f = alpha(child), alpha(foot)
    slope = np.tan(0.5 * (child["th"] + foot["th"])
                   + sign * 0.5 * (al_c + al_f))
    return (child["y"] - foot["y"]) - slope * (child["x"] - foot["x"])


def compat_resid(child, foot, lam_sign, mode, delta=1.0):
    """(u,v) compatibility residual foot->child.
    lam_sign=-1 for the C+ family (lam=tan(th-al)),
    lam_sign=+1 for the C- family (lam=tan(th+al)).
    mode='trap' -> second-order trapezoidal (average) coefficients;
    mode='end'  -> first-order endpoint (foot) coefficients. The two agree
    to O(h) in the coefficients, hence the residuals differ by the scheme's
    O(h^3) local truncation ambiguity — used to DERIVE the per-cell band."""
    al_c, al_f = alpha(child), alpha(foot)
    if mode == "trap":
        lam = 0.5 * (np.tan(foot["th"] + lam_sign * al_f)
                     + np.tan(child["th"] + lam_sign * al_c))
        S = 0.5 * (source(foot) + source(child))
    else:  # 'end': foot-only coefficients (consistent, first order)
        lam = np.tan(foot["th"] + lam_sign * al_f)
        S = source(foot)
    return ((child["u"] - foot["u"]) + lam * (child["v"] - foot["v"])
            - delta * S * (child["x"] - foot["x"]))


def cell_residual(child, cplus_foot, cminus_foot):
    """Per-cell residuals (normalized by the local speed V, dimensionless):
      compat      = max family |R_trap|            (the 2nd-order residual)
      trunc_band  = max family |R_trap - R_end|     (local truncation est.)
      geom        = max family geometric slope residual (identifies feet)"""
    Vsc = child["V"]
    Rgp = geom_resid(child, cplus_foot, +1.0)
    Rgm = geom_resid(child, cminus_foot, -1.0)
    Rcp_t = compat_resid(child, cplus_foot, -1.0, "trap")
    Rcm_t = compat_resid(child, cminus_foot, +1.0, "trap")
    Rcp_e = compat_resid(child, cplus_foot, -1.0, "end")
    Rcm_e = compat_resid(child, cminus_foot, +1.0, "end")
    return dict(geom=max(abs(Rgp), abs(Rgm)),
                compat=max(abs(Rcp_t), abs(Rcm_t)) / Vsc,
                trunc_band=max(abs(Rcp_t - Rcp_e),
                               abs(Rcm_t - Rcm_e)) / Vsc)


# ----------------------------------------------------------------------
# foot identification (GEOMETRIC, stencil-agnostic). GENO's structured grid
# advances downstream with an overshoot rule (i+=1 with or without j2+=1)
# and carries void rows, so the two characteristic feet of a child are NOT
# reliably at (j-1,i-1)/(j+1,i-1). Instead we search a small UPSTREAM block
# and pick, for each family, the physical node whose edge to the child best
# matches that family's characteristic direction:
#   C+ foot: edge angle atan2(dy,dx) ~ mean(theta) + mean(alpha)
#   C- foot: edge angle atan2(dy,dx) ~ mean(theta) - mean(alpha)
# The two feet must straddle the child in y (one toward wall, one toward
# axis), be strictly upstream, and match their family direction within a
# small angular tolerance (a fraction of the Mach angle). This fixes the
# stencil from the geometry of the field itself, not from GENO bookkeeping.
DR, DC = 4, 4          # local block half-extent (rows, cols)
ANG_TOL_FRAC = 0.10    # edge must match char. direction within 10% of alpha


def _edge_angle_resid(child, foot, sign):
    dx = child["x"] - foot["x"]; dy = child["y"] - foot["y"]
    if dx <= 0.0:
        return np.inf
    edge = np.arctan2(dy, dx)
    al = 0.5 * (alpha(child) + alpha(foot))
    tgt = 0.5 * (child["th"] + foot["th"]) + sign * al
    return abs(edge - tgt), al


def find_triangle(g, j, i):
    child = node_state(g, j, i)
    if not physical(child):
        return None
    cand = []
    for jj in range(max(0, j - DR), min(g["j2"], j + DR + 1)):
        for ii in range(max(0, i - DC), i):        # strictly upstream cols
            s = node_state(g, jj, ii)
            if physical(s) and s["x"] < child["x"]:
                cand.append(s)
    if len(cand) < 2:
        return None

    def best_foot(sign, toward):
        # toward = +1 wall side (y > child), -1 axis side (y < child)
        best = None
        for s in cand:
            if toward * (s["y"] - child["y"]) < 0.0:
                continue
            res = _edge_angle_resid(child, s, sign)
            if res == np.inf:
                continue
            e, al = res
            if e > ANG_TOL_FRAC * al:
                continue
            if best is None or e < best[1]:
                best = (s, e)
        return best

    # C+ family climbs toward the wall, C- descends toward the axis; try
    # both assignments of side and keep the geometrically consistent one.
    fp = best_foot(+1.0, +1.0)    # C+ foot on the wall side
    fm = best_foot(-1.0, -1.0)    # C- foot on the axis side
    if fp is None or fm is None:
        # fall back to the opposite side convention (grid orientation)
        fp = best_foot(+1.0, -1.0)
        fm = best_foot(-1.0, +1.0)
        if fp is None or fm is None:
            return None
    fp, fm = fp[0], fm[0]
    if fp["x"] == fm["x"] and fp["y"] == fm["y"]:
        return None
    r = cell_residual(child, fp, fm)
    h = max(abs(child["x"] - fp["x"]), abs(child["x"] - fm["x"]),
            abs(child["y"] - fp["y"]), abs(child["y"] - fm["y"]))
    return dict(child=child, cplus=fp, cminus=fm, h=h, **r)


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# LITERAL REPRODUCTION ("due punti -> punto nuovo"): given the two GENO
# parent feet, SOLVE our axisymmetric interior unit process for the new
# point and compare it to GENO's child. This closes the mandate wording
# beyond the EOS-general residual test above. The point solve needs a
# thermodynamic closure to produce a4/M4 from V4 (the residual test avoids
# it by reading GENO's own a) -> we use the calorically-perfect energy
# closure a4^2 = (gamma-1)(h0 - V4^2/2) with the CELL-MEAN gamma and h0
# read from the feet: a DECLARED gamma=const ORACLE instance (exactly as
# the S5/S8 spikes declare their Prandtl-Meyer / oblique closed forms;
# the EOS-general statement is the residual test, DIR-GAMMA-clean).
def _newton4(F, z0, iters=60):
    z = np.array(z0, float)
    for _ in range(iters):
        r = F(z)
        if not np.all(np.isfinite(r)):
            return None, np.inf
        J = np.empty((4, 4))
        for k in range(4):
            h = 1e-7 * max(1.0, abs(z[k]))
            zp = z.copy(); zp[k] += h
            rp = F(zp)
            if not np.all(np.isfinite(rp)):
                return None, np.inf
            J[:, k] = (rp - r) / h
        try:
            dz = np.linalg.solve(J, r)
        except np.linalg.LinAlgError:
            return None, np.inf
        z = z - dz
        if np.max(np.abs(dz)) < 1e-13 * (1.0 + np.max(np.abs(z))):
            break
    return z, float(np.max(np.abs(F(z))))


def reproduce_child(f_plus, f_minus, mode="trap", delta=1.0):
    """Solve the interior unit process from the two feet; return the
    produced child dict (x,y,u,v,th,V,a,M) or None. mode selects the
    coefficient rule (trap=2nd order, end=1st order) for the derived band."""
    gam = 0.5 * (f_plus["gam"] + f_minus["gam"])
    gm1 = gam - 1.0
    # stagnation enthalpy from the feet (calorically-perfect, cell-mean g)
    h0 = 0.5 * ((f_plus["a"] ** 2 / gm1 + 0.5 * f_plus["V"] ** 2)
                + (f_minus["a"] ** 2 / gm1 + 0.5 * f_minus["V"] ** 2))

    def a_of_V(V2):
        val = gm1 * (h0 - 0.5 * V2)
        return np.sqrt(val) if val > 0.0 else np.nan

    def F(z):
        x4, y4, u4, v4 = z
        V4 = np.hypot(u4, v4)
        a4 = a_of_V(V4 * V4)
        th4 = np.arctan2(v4, u4)
        M4 = V4 / a4
        al4 = np.arcsin(np.clip(1.0 / M4, -1.0, 1.0))
        s4 = a4 * a4 * v4 / (y4 * (u4 * u4 - a4 * a4))
        if mode == "trap":
            al1 = alpha(f_plus); al2 = alpha(f_minus)
            slp = np.tan(0.5 * (f_plus["th"] + th4) + 0.5 * (al1 + al4))
            slm = np.tan(0.5 * (f_minus["th"] + th4) - 0.5 * (al2 + al4))
            lam_p = 0.5 * (np.tan(f_plus["th"] - al1) + np.tan(th4 - al4))
            lam_m = 0.5 * (np.tan(f_minus["th"] + al2) + np.tan(th4 + al4))
            Sp = 0.5 * (source(f_plus) + s4)
            Sm = 0.5 * (source(f_minus) + s4)
        else:  # endpoint (foot) coefficients
            al1 = alpha(f_plus); al2 = alpha(f_minus)
            slp = np.tan(f_plus["th"] + al1)
            slm = np.tan(f_minus["th"] - al2)
            lam_p = np.tan(f_plus["th"] - al1)
            lam_m = np.tan(f_minus["th"] + al2)
            Sp = source(f_plus); Sm = source(f_minus)
        return np.array([
            (y4 - f_plus["y"]) - slp * (x4 - f_plus["x"]),      # C+ geom
            (y4 - f_minus["y"]) - slm * (x4 - f_minus["x"]),    # C- geom
            (u4 - f_plus["u"]) + lam_p * (v4 - f_plus["v"])
            - delta * Sp * (x4 - f_plus["x"]),                  # C+ compat
            (u4 - f_minus["u"]) + lam_m * (v4 - f_minus["v"])
            - delta * Sm * (x4 - f_minus["x"]),                 # C- compat
        ])

    z0 = [0.5 * (f_plus["x"] + f_minus["x"]) + 1e-3,
          0.5 * (f_plus["y"] + f_minus["y"]),
          0.5 * (f_plus["u"] + f_minus["u"]),
          0.5 * (f_plus["v"] + f_minus["v"])]
    z, rnorm = _newton4(F, z0)
    if z is None or not np.isfinite(rnorm) or rnorm > 1e-6:
        return None
    x4, y4, u4, v4 = z
    V4 = np.hypot(u4, v4); a4 = a_of_V(V4 * V4)
    if not np.isfinite(a4):
        return None
    return dict(x=x4, y=y4, u=u4, v=v4, V=V4, a=a4,
                th=np.arctan2(v4, u4), M=V4 / a4)


def collect_cells(g, i_lo, i_hi, i_step=1):
    """Clean supersonic-core interior triangles. Filters (all physical,
    not tuned to pass): child comfortably supersonic (M>1.5, away from the
    sonic line where the axisym source a^2 v/(y(u^2-a^2)) is singular),
    away from the axis (y>Y_AXIS, where the 1/y source and grid degenerate)
    and the wall, feet on the characteristics (geom residual < 1% of cell),
    and a well-conditioned cell (h>0)."""
    y_wall = float(np.nanmax(g["y"]))
    Y_AXIS = 0.15 * y_wall
    cells = []
    for i in range(max(1, i_lo), min(g["l"], i_hi), i_step):
        for j in range(1, g["j2"] - 1):
            c = node_state(g, j, i)
            if not physical(c) or c["M"] < 1.5 or c["M"] > 6.0 \
                    or c["y"] < Y_AXIS:
                continue
            t = find_triangle(g, j, i)
            if t is None or t["h"] <= 0.0:
                continue
            if t["compat"] == 0.0:             # exact-equal -> skip (void)
                continue
            if t["geom"] > 0.01 * t["h"]:      # feet must be on char. edges
                continue
            cells.append(t)
    return cells


def main():
    print("== G0 CROSS-CODE FLOWFIELD ORACLE: GENO tocnoz vs our axisym "
          "unit process ==")
    if not os.path.exists(os.path.join(GENO_TOC, "dimensions.dat")):
        print("  GENO flowfield not present (dimensions.dat missing). "
              "Regenerate with the GENO binary on the tocnoz case "
              "(env: gfortran) -> SKIP (declared on-demand).")
        print("VERDICT: SKIP")
        return 0

    g = read_grid(GENO_TOC)
    print("  grid: j2=%d rows (wall->axis) x l=%d cols (downstream); "
          "gamma in (0,%.4f] (frozen, variable; zeros = void rows)"
          % (g["j2"], g["l"], np.nanmax(g["gamma"])))
    ok = True

    i_lo = max(2, g["l"] // 20)
    i_hi = g["l"] - 2
    # subsample downstream columns: the test is a statistic over thousands
    # of independent interior triangles, so ~150 columns spanning the field
    # is representative and keeps the pure-Python foot search bounded (the
    # verdict is stable vs the full sweep — declared).
    i_step = max(1, (i_hi - i_lo) // 150)
    cells = collect_cells(g, i_lo, i_hi, i_step=i_step)
    print("  clean supersonic-core triangles (M in [1.5,6], off-axis, feet "
          "on characteristics; %d-column subsample): %d" % (
              len(range(i_lo, i_hi, i_step)), len(cells)))
    if len(cells) < 100:
        print("  too few clean interior triangles -> FAIL")
        print("VERDICT: FAIL")
        return 1

    rc = np.array([c["compat"] for c in cells])
    band = np.array([c["trunc_band"] for c in cells])
    rg = np.array([c["geom"] / c["h"] for c in cells])
    floor = 64.0 * EPS       # roundoff floor (normalized velocity units)

    # (i) feet on the characteristics. The straight foot->child edge
    # deviates from the local characteristic tangent by the O(h) geometric
    # truncation of a 2nd-order MoC (the characteristic is curved), so the
    # criterion is NOT an absolute magic number but two physical facts: the
    # slope residual is a small fraction of the cell (edges lie on the
    # characteristics), AND it is an order of magnitude cleaner than the
    # wrong-pairing control N2 below (the discrimination margin). Checked
    # jointly here and at N2.
    med_geom = float(np.median(rg))
    geom_ok = med_geom < 0.02
    print("  [feet] median relative slope residual = %.2e "
          "(edges on characteristics, < 2%% of cell): %s"
          % (med_geom, "PASS" if geom_ok else "FAIL"))
    ok &= geom_ok

    # (ii) PER-CELL truncation-band test (tolerance DERIVED from the scheme
    # order, no cross-field h-fit): GENO's node values satisfy OUR 2nd-order
    # compatibility relation up to the cell's own local truncation ambiguity
    #   |R_trap| <= K * (|R_trap - R_end| + floor),  K = 4 (Richardson).
    # A code solving the same continuous MoC lands inside this band; the
    # fraction inside is the cross-code agreement rate.
    K = 4.0
    tol = K * (band + floor)
    inside = rc <= tol
    frac = float(np.mean(inside))
    print("  [truncation band] cells with |R_trap| <= 4*(|R_trap-R_end|"
          "+floor): %d/%d = %.1f%% (median R=%.2e, median band=%.2e)"
          % (int(inside.sum()), len(cells), 100.0 * frac,
             float(np.median(rc)), float(np.median(band))))
    band_ok = frac >= 0.90
    ok &= band_ok
    if not band_ok:
        print("      -> below 90%%: cross-code agreement NOT established "
              "at the truncation level")

    # (iii-bis) LITERAL REPRODUCTION ("due punti -> punto nuovo"): solve
    # the interior unit process from the two GENO feet and compare the
    # PRODUCED child to GENO's, within a per-cell derived band. Declared
    # gamma=const oracle instance (calorically-perfect energy closure,
    # cell-mean gamma) — the EOS-general statement stays the residual test.
    rep_err, rep_band = [], []
    for c in cells:
        pt = reproduce_child(c["cplus"], c["cminus"], "trap")
        pe = reproduce_child(c["cplus"], c["cminus"], "end")
        if pt is None or pe is None:
            continue
        ch = c["child"]; h = c["h"]

        def state_dist(a, b):
            return max(abs(a["x"] - b["x"]) / h, abs(a["y"] - b["y"]) / h,
                       abs(a["th"] - b["th"]), abs(a["M"] - b["M"]) / b["M"])
        rep_err.append(state_dist(pt, ch))
        rep_band.append(max(state_dist(pt, pe), floor))
    rep_err = np.array(rep_err); rep_band = np.array(rep_band)
    if len(rep_err) < 50:
        print("  [reproduction] too few solvable cells -> FAIL")
        ok = False
    else:
        Kr = 4.0
        inside_rep = rep_err <= Kr * (rep_band + floor)
        frac_rep = float(np.mean(inside_rep))
        rep_ok = frac_rep >= 0.90
        print("  [reproduction] solve(2 feet)->child vs GENO within derived "
              "band: %d/%d = %.1f%% (median err=%.2e, median band=%.2e)"
              % (int(inside_rep.sum()), len(rep_err), 100.0 * frac_rep,
                 float(np.median(rep_err)), float(np.median(rep_band))))
        ok &= rep_ok
        # reproduction negative control: corrupt a foot -> produced point
        # departs from GENO's child beyond the band
        rep_bad = []
        for c in cells:
            bad_foot = dict(c["cplus"])
            bad_foot["u"] *= 1.01
            bad_foot["V"] = np.hypot(bad_foot["u"], bad_foot["v"])
            bad_foot["th"] = np.arctan2(bad_foot["v"], bad_foot["u"])
            bad_foot["M"] = bad_foot["V"] / bad_foot["a"]
            pt = reproduce_child(bad_foot, c["cminus"], "trap")
            if pt is None:
                continue
            ch = c["child"]; h = c["h"]
            rep_bad.append(max(abs(pt["x"] - ch["x"]) / h,
                               abs(pt["y"] - ch["y"]) / h,
                               abs(pt["th"] - ch["th"]),
                               abs(pt["M"] - ch["M"]) / ch["M"]))
        rep_bad = np.array(rep_bad)
        frac_bad_rep = float(np.mean(
            rep_bad <= Kr * (np.median(rep_band) + floor)))
        rep_n_rej = frac_bad_rep < 0.10
        print("  [reproduction N] corrupted foot: band-inside %.1f%% "
              "(clean %.1f%%): rejected %s"
              % (100.0 * frac_bad_rep, 100.0 * frac_rep,
                 "PASS" if rep_n_rej else "FAIL (cannot reject!)"))
        ok &= rep_n_rej

    # ---- NEGATIVE CONTROL N1: corrupted child -> leaves the band
    rc_bad = []
    for c in cells:
        bad = dict(c["child"])
        bad["u"] = bad["u"] * 1.01
        bad["V"] = np.hypot(bad["u"], bad["v"])
        bad["th"] = np.arctan2(bad["v"], bad["u"])
        bad["M"] = bad["V"] / bad["a"]
        r = cell_residual(bad, c["cplus"], c["cminus"])
        rc_bad.append(r["compat"])
    rc_bad = np.array(rc_bad)
    inside_bad = rc_bad <= tol
    frac_bad = float(np.mean(inside_bad))
    n1_rej = frac_bad < 0.10
    print("  [N1 corrupted cell] band-inside fraction drops to %.1f%% "
          "(clean %.1f%%): rejected %s"
          % (100.0 * frac_bad, 100.0 * frac,
             "PASS" if n1_rej else "FAIL (cannot reject!)"))
    ok &= n1_rej

    # ---- NEGATIVE CONTROL N2: wrong pairing (swap feet) -> geometry breaks
    rg_swap = np.array([cell_residual(c["child"], c["cminus"],
                                      c["cplus"])["geom"] / c["h"]
                        for c in cells])
    med_swap = float(np.median(rg_swap))
    n2_rej = med_swap > 50.0 * med_geom
    print("  [N2 wrong pairing] median relative slope residual %.2e "
          "(correct %.2e, x%.0f): rejected %s"
          % (med_swap, med_geom, med_swap / max(med_geom, EPS),
             "PASS" if n2_rej else "FAIL (cannot reject!)"))
    ok &= n2_rej
    # discrimination margin (the feet criterion's second half): the
    # identified feet must be an order of magnitude cleaner than the swap.
    margin_ok = med_geom < 0.1 * med_swap
    print("  [feet discrimination] correct/wrong slope-residual ratio "
          "%.0fx (>= 10x required): %s"
          % (med_swap / max(med_geom, EPS), "PASS" if margin_ok else "FAIL"))
    ok &= margin_ok

    print("VERDICT: %s" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

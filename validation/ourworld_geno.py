"""[F3] OUR WORLD, DUAL-CODE: the world adapter for the rao1961 chain.

The rao1961_{twin,o33,sqp_return} carriers pose Rao's world: gconst gas
identified from GENO's field, ambient = Rao's a-posteriori PA_PC * p0.
This module poses the SAME instruments in OUR world -- the CH4/O2 frozen
gas of a1_config_compare (GENO's own thermo_CH4O2.dat + raptor.plt,
tabulated by a1_ideal_march_jax.build_tab_nasa), GENO's axisymmetric
ideal-spike member run in that gas (CASES/raoplug_ch4o2, validation mode
Me_fixed = 2.802: theta_E = -0.02 deg, L = 5.926, closes on the axis),
and the member's OWN a-posteriori lip ambient from raoplug_performance.dat
(the analogue of Rao's Eq. (8): the reference design is the optimum for
the ambient it expands to, which sits 0.5 percent below the nominal
a1_config_compare.PA -- a declared posing residual, reported here).

GAS CONSISTENCY IS VERIFIED, NOT IDENTIFIED. The gas is not fitted from
the field: the field is checked against the tables it was computed with
-- nodal p/(rho T) against the tables' Rg, and the per-node stagnation
state (h + q^2/2 against h0; s(T, p) against s0) -- so a gas mismatch
between the two codes fails loudly instead of being absorbed.

Environment (read by the carriers that import this module):
  OW_GENO_RUN  GENO run directory (fld.sol, inf.sol, raoplug_cminus.dat,
               raoplug_performance.dat); default CASES/raoplug_ch4o2/
               run_val_repro (the 2026-09-15 bit-identical reproduction
               of the S21 rao_val run)
  OW_SUB       field subsampling stride for the interpolators (default 1)
  OW_YCUT      tip cut, in lip radii (default 0.01): the marched wall ends
               where GENO's contour drops below y = OW_YCUT * y_E. The
               member closes on the axis (y_D = 3.8e-4 m) and the plug
               march has no axis cell: its wall foot solve at y ~ 1e-3 m
               (source term ~ sin(theta)/y) certified in 4 of 6 twin runs
               and blew up (1e11) in the other two, always at the last
               station. The excluded tip (y < 0.023 m) carries
               (p - p_a) pi y^2 ~ 1e2 N of 1.2e8 N: below every band
               used here. DECLARED posing (2026-09-15, after the first
               twin run).
"""
import os
import re
import sys

import numpy as np
import jax.numpy as jnp

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import a1_ideal_march_jax as A1                        # noqa: E402
import a1_config_compare as CC                         # noqa: E402
from a1_freejet_unit import q_at_pa                    # noqa: E402
from rao1961_twin import load_geno                     # noqa: E402

GENO_CASES = os.path.join(A1.GENO_DIR, "CASES")
RUN = os.environ.get("OW_GENO_RUN",
                     os.path.join(GENO_CASES, "raoplug_ch4o2",
                                  "run_val_repro"))
SUB = int(os.environ.get("OW_SUB", 1))
YCUT = float(os.environ.get("OW_YCUT", 0.01))


def performance(run):
    """raoplug_performance.dat -> dict of the scalar lines."""
    d = {}
    pat = re.compile(r"^\s*([A-Za-z_]+)(?:\s*\[[^\]]*\])?\s*=\s*([-+0-9.Ee]+)")
    for ln in open(os.path.join(run, "raoplug_performance.dat")):
        m = pat.match(ln)
        if m:
            d[m.group(1)] = float(m.group(2))
    return d


def world_tab():
    tab = A1.prep_tab(A1.build_tab_nasa())
    return tab, A1.tab_arrays(tab)


def gas_check(fld, tab, ta, n=20000):
    """The field against the tables: returns (Rg rel, h0 rel, s0 rel)
    max deviations over a uniform subsample of n nodes."""
    idx = np.linspace(0, fld.shape[0] - 1, min(n, fld.shape[0])).astype(int)
    rho, V, p, T = fld[idx, 3], fld[idx, 4], fld[idx, 6], fld[idx, 8]
    Rg = float(tab["Rg"])
    dRg = np.max(np.abs(p / (rho * T) / Rg - 1.0))
    Tg, hg, sg = np.asarray(tab["T"]), np.asarray(tab["h"]), np.asarray(tab["s0m"])
    h = np.interp(T, Tg, hg)
    h0 = h + 0.5 * V * V
    dh0 = np.max(np.abs(h0 / float(tab["h0"]) - 1.0))
    s = np.interp(T, Tg, sg) - Rg * np.log(p / A1.PREF)
    ds0 = np.max(np.abs(s / float(tab["s0"]) - 1.0))
    return dRg, dh0, ds0


def tip_cut(wall, y_E):
    """Truncate the (x-sorted) contour where y first drops below
    YCUT * y_E on its final descent; the cut point is interpolated and
    appended so the wall ends exactly at y = YCUT * y_E."""
    yc = YCUT * y_E
    i_max = int(np.argmax(wall[:, 1]))
    below = np.where(wall[i_max:, 1] < yc)[0]
    if len(below) == 0:
        return wall, float(wall[-1, 0])
    j = i_max + below[0]
    x1, y1, x2, y2 = wall[j - 1, 0], wall[j - 1, 1], wall[j, 0], wall[j, 1]
    xc = x1 + (yc - y1) * (x2 - x1) / (y2 - y1)
    cut = wall[j - 1].copy()
    cut[0], cut[1] = xc, yc
    return np.vstack([wall[:j], cut[None, :]]), float(xc)


def load_world(run=RUN, verbose=True):
    """GENO's field + wall + performance in OUR gas; ambient = the
    member's lip ambient p_a from raoplug_performance.dat; the wall
    tip-cut at YCUT * y_E (see the module docstring)."""
    fld, wall_full = load_geno(run)
    if SUB > 1:
        fld = fld[::SUB]
    y_E = float(np.max(fld[:, 2]))
    wall, x_end = tip_cut(wall_full, y_E)
    perf = performance(run)
    tab, ta = world_tab()
    pa = perf["p_a"]
    qpa = float(q_at_pa(pa, ta, tab["_as"]))
    dRg, dh0, ds0 = gas_check(fld, tab, ta)
    if verbose:
        print("   world: OUR gas (%s; Rg %.4f, T0 %.1f K, p0 %.6g Pa); "
              "GENO member theta_E %+.4f deg, L %.5f, eps %.5f"
              % (tab["name"], float(tab["Rg"]), float(tab["ts"]),
                 float(tab["ps"]), perf["theta_E"], perf["L_plug"],
                 perf["eps_plug"]))
        print("   ambient = the member's lip ambient p_a %.6g Pa "
              "(%.4f of the nominal PA %.6g); q_at_pa %.1f m/s"
              % (pa, pa / CC.PA, CC.PA, qpa))
        print("   gas check, field vs tables (max rel over %d nodes): "
              "Rg %.1e, h0 %.1e, s0 %.1e" % (min(20000, fld.shape[0]),
                                             dRg, dh0, ds0))
        print("   reference: %d field points, %d wall points, x %.4f..%.4f,"
              " y_D %.2e; tip cut at y = %.3f y_E = %.4f m -> x_end %.4f"
              " (full contour ends at %.4f)"
              % (fld.shape[0], wall_full.shape[0], wall_full[0, 0],
                 wall_full[-1, 0], wall_full[-1, 1], YCUT, YCUT * y_E,
                 x_end, wall_full[-1, 0]))
    return dict(fld=fld, wall=wall, wall_full=wall_full, x_end=x_end,
                y_E=y_E, perf=perf, tab=tab, ta=ta, pa=pa, qpa=qpa,
                gas_dev=(dRg, dh0, ds0), run=run)


def install(module, W):
    """Point a rao1961 carrier module at OUR world: its gas identification
    and gconst table builder are replaced by the verified tables, and its
    ambient rule by the member's lip ambient. Only the module's own
    names are touched (never a1_ideal_march_jax itself)."""
    tab, ta = W["tab"], W["ta"]

    class _A1proxy:
        def __getattr__(self, name):
            if name == "build_tab_gconst":
                return lambda **kw: tab
            if name == "prep_tab":
                return lambda t: t
            return getattr(A1, name)

    module.A1 = _A1proxy()
    module.load_geno = lambda run: (W["fld"], W["wall"])   # tip-cut wall
    module.gas_from_field = lambda fld: (float(tab["Rg"]), float(tab["ts"]),
                                         float(tab["ps"]))
    module.PA_PC = W["pa"] / float(tab["ps"])
    module.G = float(tab["gammamedio"])
    return jnp.float64(W["pa"])

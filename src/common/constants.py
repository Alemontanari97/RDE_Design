"""constants.py — single home for the package-wide physical constants,
reference states and standard tolerances.

UNIT CONVENTION (package-wide): SI internally — Pa, K, kg, m, J/kg.
Conversions to atm / bar / MJ/kg happen only at the display / JSON edges.

REFERENCE-STATE CONVENTION (deliberate, paper-driven — do not "unify"):
  * thrust suite (src/thrust): fill P1 = P_ATM (1 atm), T1 = T_STD, ambient
    Pa = P_ATM — the Shepherd–Kasahara Table-1 convention;
  * cycle suite (src/cycles): P1 = P_REF_BAR (1 bar), T1 = T_STD — the
    Wintenberger–Shepherd validation convention.
  Both are stated in validation/interface_audit.md §3; the blessed numbers of
  each suite depend on its own reference pressure.
"""

# ---------------------------------------------------------------- constants
G0 = 9.80665          # standard gravity [m/s^2] (Isp definition)
P_ATM = 101325.0      # standard atmosphere [Pa]  (thrust-suite fill & ambient)
P_REF_BAR = 1.0e5     # 1 bar [Pa]                (cycle-suite fill)
T_STD = 300.0         # standard initial temperature [K]
T_REF = 298.15        # thermochemical standard state [K] (q° anchoring)

# ------------------------------------------------- standard tolerance ladder
# (used by tests/ and quoted in validation reports)
TOL = dict(
    cj_identity_rel=1e-9,     # same CJ from every canonical (cj_core) path
    qtilde_roundtrip=1e-6,    # M_CJ -> q~ -> M_CJ inversion (exact algebra)
    axial_vs_bound_rel=2e-3,  # SK axial sonic point vs independent eq. bound
    cross_solver_rel=2e-3,    # independent CJ solvers vs cj_core (physics)
    cp_collapse_rel=1e-6,     # Stechmann PR->1 vs steady CP identity
    sonic_resid_max=5e-3,     # |w2/a_eq - 1| at any computed CJ point
)

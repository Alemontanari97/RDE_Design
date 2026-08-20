"""R22-F v2 refutation probe, round 4, lens L0.

Feeds R22F-L0-19 (PART A) and R22F-L0-20 (PART B).

PART A -- mu FUNCTIONAL-IDENTITY counterexample (R22F-L0-19, BREAK):
  The centerpiece's argmax-shift schema (S2.2-bis as amended through
  [REV2-r3-*]) defines the curvature floor mu ("smallest reduced-Hessian
  eigenvalue", condition (1) :579-585; "mu_T = the curvature floor over
  the TANGENT cone" :614; "a curvature floor mu per (A)" in (F) :685)
  WITHOUT naming the functional whose Hessian it is, and (D) :647-653
  asserts "The carrier INSTANTIATES the schema object at an interior /
  margin-inactive S*" where the measured carrier of record is the
  segmented TR-Newton Hessian of the REDUCED (engine-computed)
  functional J_red.  The VI chain behind form (T) with the gradient gap
  evaluated at S*_red (the [REV2-r3-2] pin) consumes the curvature
  floor of J_TRUE along the feasible segment.  This probe exhibits a
  1-D convex-feasible-set model in which EVERY printed check passes
  (H-G1..H-G5, conditions (1)-(3), cone pairing, basin check with the
  measured carrier) and the licensed form-(T) bound delta(S*_red)/mu_meas
  under-covers the true argmax shift by an UNBOUNDED factor
  (= mu_red/mu_true); the mu_true instantiation is tight; the corrected
  curvature-transfer form mu_eff = mu_meas - L_H (L_H = sup of the
  Hessian-level residual on the ball) exactly recovers the bound; and
  the value route (F) instantiated with the SAME measured carrier is
  SOUND (J_red-side derivation) -- its own a-posteriori check even
  refuses to certify in the failure regime.  So the defect is isolated
  to the gradient-route mu identity, not to the schema family.

PART B -- H-G5 PROX-REGULAR-DISJUNCT counterexample (R22F-L0-20, REPAIR):
  H-G5 as printed (:706-711) licenses "CONVEX (or locally convex /
  prox-regular with the shift ball inside ONE connected component)".
  The complement of the open unit disk in R^2 is UNIFORMLY prox-regular
  (prox-parameter r = 1, smooth boundary) and connected; with two
  quadratic objectives whose interior anchor points sit at radius
  eps << 1 inside the disk, both argmaxes sit on the unit circle,
  the argmax shift is set by the ANGLE between the anchors (independent
  of eps) while the gradient gap and the value gap scale with eps:
  form (T) and the value route (F) are BOTH violated -- the value
  route's a-posteriori check PASSES while its bound is false -- with
  violation factors growing without bound as eps -> 0.  A convex
  control (unit disk) is tight.  Mechanism: on a boundary concave
  toward the feasible side the effective curvature along the constraint
  surface carries the second-fundamental-form correction
  mu - |multiplier|*kappa, which the ambient-Hessian floor misses; the
  segment between boundary argmaxes is infeasible, killing the VI /
  strong-concavity arguments regardless of prox-parameter margins.

CT-6 clean: all numbers are synthetic counter-model inputs; no number
from the four nozzle papers (P-A..P-D) or any external source is used.
Tolerances are derived (machine epsilon on exact arithmetic / grid
resolution on sampled argmax checks), never magic.

Env: pinned (numpy only; no installs).  Run:  python <this file>
"""

import numpy as np

# ---------------------------------------------------------------------------
# PART A -- mu functional identity (feeds R22F-L0-19)
# ---------------------------------------------------------------------------
print("=" * 72)
print("PART A: mu functional-identity counterexample (R22F-L0-19)")
print("=" * 72)

a = 100.0   # mu_red  = measured engine curvature (J_red Hessian), constant
c = 1.0     # mu_true = curvature of J_true, constant
b = 1.0     # true argmax offset

J_red = lambda x: -0.5 * a * x**2
J_true = lambda x: -0.5 * c * (x - b)**2
dJ_red = lambda x: -a * x
dJ_true = lambda x: -c * (x - b)

R_basin = 2.0                      # certified ball around S*_red (radius)
# Feasible set C = R (trivially convex): H-G5 convex branch holds.

# Analytic argmaxes, verified on a fine grid over the basin.
grid = np.linspace(-R_basin, R_basin, 400001)
h_grid = grid[1] - grid[0]
x1 = 0.0                            # S*_red  (argmax J_red)
x2 = b                              # S*_true (argmax J_true)
assert abs(grid[np.argmax(J_red(grid))] - x1) <= h_grid, "A0a: x1 grid check"
assert abs(grid[np.argmax(J_true(grid))] - x2) <= h_grid, "A0b: x2 grid check"

shift = abs(x2 - x1)                                     # = 1
g_at_x1 = dJ_true(x1) - dJ_red(x1)                       # = c*b
delta = abs(g_at_x1)   # support-function form, M = I, cone = R (full space)

# --- every printed check passes -------------------------------------------
# H-G5: C = R convex.  H-G4: S* interior / margin-inactive (no constraint).
# Condition (3): M = I everywhere, one metric.  Cone pairing (A): delta and
# mu taken on the same (full-space) cone.  Condition (1) basin check with
# the MEASURED carrier (J_red curvature = a, constant, floor sustained on
# every ball -> any certified radius passes the (E) ladder):
bound_T_meas = delta / a
assert bound_T_meas <= R_basin, "A1: basin check (measured carrier) passes"

# --- the licensed form-(T) bound with the measured carrier is FALSE -------
viol_T = shift / bound_T_meas                            # = a/c = 100
print(f"A2: form (T), mu = measured carrier (J_red): bound = {bound_T_meas:.4g}"
      f", actual shift = {shift:.4g}, violation = {viol_T:.1f}x")
assert viol_T >= 50.0, "A2: form (T) with measured mu violated >= 50x"

# --- mu = J_true's floor: tight -------------------------------------------
bound_T_true = delta / c
print(f"A3: form (T), mu = J_true floor: bound = {bound_T_true:.4g} (tight)")
assert abs(bound_T_true - shift) <= 1e-12, "A3: J_true-floor bound tight"

# --- corrected curvature-transfer form: mu_eff = mu_meas - L_H ------------
# L_H = sup over the ball of |J_true'' - J_red''| (Hessian-level residual).
L_H = abs((-c) - (-a))                                   # = a - c = 99
mu_eff = a - L_H                                         # = c = 1
bound_T_eff = delta / mu_eff
print(f"A4: corrected form, mu_eff = mu_meas - L_H = {mu_eff:.4g}: "
      f"bound = {bound_T_eff:.4g} (exactly recovers)")
assert abs(bound_T_eff - shift) <= 1e-12, "A4: corrected form tight"

# --- value route (F) with the SAME measured carrier is SOUND --------------
# J_red-side derivation: J_red(x1)-J_red(x2) >= (mu_red/2)*shift^2 (x1 is
# the J_red argmax, C convex) and the uniform value premise gives
# (mu_red/2)*shift^2 <= 2*eps_U  =>  shift <= 2*sqrt(eps_U/mu_red).
eps_U = np.max(np.abs(J_true(grid) - J_red(grid)))       # sup on the basin
bound_F_meas = 2.0 * np.sqrt(eps_U / a)
print(f"A5: value route, mu = measured carrier: eps_U = {eps_U:.4g}, "
      f"bound = {bound_F_meas:.4g} >= shift {shift:.4g} (SOUND)")
assert bound_F_meas >= shift, "A5: value-route bound holds with measured mu"
# ... and its own a-posteriori check (2*sqrt(eps_U/mu) <= basin radius)
# honestly REFUSES to certify in this regime:
print(f"A6: value-route a-posteriori check: {bound_F_meas:.4g} <= "
      f"{R_basin:.4g}? {bound_F_meas <= R_basin} (honest refusal)")
assert bound_F_meas > R_basin, "A6: value route refuses -- honesty intact"

# --- unbounded growth of the form-(T) violation ---------------------------
viols = []
for a_k in (10.0, 100.0, 1000.0, 10000.0):
    d_k = abs((-c * (0.0 - b)) - (-a_k * 0.0))           # delta = c*b
    viols.append(shift / (d_k / a_k))                    # = a_k/c
print(f"A7: violation factors along mu_red ladder {viols} (unbounded)")
assert all(v2 > v1 for v1, v2 in zip(viols, viols[1:])), "A7: growth monotone"

print("PART A: ALL ASSERTS PASS -- the licensed gradient-route form with")
print("        the measured carrier is FALSE while every printed check")
print("        passes; value route sound; corrected transfer form exact.")

# ---------------------------------------------------------------------------
# PART B -- H-G5 prox-regular disjunct (feeds R22F-L0-20)
# ---------------------------------------------------------------------------
print()
print("=" * 72)
print("PART B: H-G5 prox-regular-disjunct counterexample (R22F-L0-20)")
print("=" * 72)

eps_off = 0.01          # interior offset of the anchor points (radius)
theta = 0.5             # angle between the two anchors [rad]
a1 = eps_off * np.array([1.0, 0.0])
a2 = eps_off * np.array([np.cos(theta), np.sin(theta)])

# Feasible set C = {x : ||x|| >= 1}: complement of the open unit disk.
#   - UNIFORMLY prox-regular with prox-parameter r = 1 (smooth boundary,
#     curvature radius 1) -- analytic fact of the model;
#   - CONNECTED (one component) in R^2;
#   - both objectives are quadratics with Hessian -I (mu floors = 1 for
#     BOTH functionals -- NO mu-identity confound with PART A).
Jr = lambda x: -0.5 * np.sum((x - a1)**2, axis=-1)      # J_red
Jt = lambda x: -0.5 * np.sum((x - a2)**2, axis=-1)      # J_true

# Argmax over C of -||x - a||^2/2 with ||a|| < 1 is the radial projection
# a/||a|| onto the unit circle.  Verify by dense feasible sampling.
phis = np.linspace(0.0, 2.0 * np.pi, 200001)[:-1]
h_phi = phis[1] - phis[0]
rads = np.linspace(1.0, 3.0, 41)
P, R = np.meshgrid(phis, rads)
XY = np.stack([R * np.cos(P), R * np.sin(P)], axis=-1)  # feasible samples
x1B = np.array([1.0, 0.0])
x2B = np.array([np.cos(theta), np.sin(theta)])
iJr = np.unravel_index(np.argmax(Jr(XY)), P.shape)
iJt = np.unravel_index(np.argmax(Jt(XY)), P.shape)
assert np.linalg.norm(XY[iJr] - x1B) <= 3.0 * h_phi, "B0a: x1 sample check"
assert np.linalg.norm(XY[iJt] - x2B) <= 3.0 * h_phi, "B0b: x2 sample check"

shiftB = np.linalg.norm(x2B - x1B)                       # = 2 sin(theta/2)
gB = a2 - a1            # gradient gap: dJt - dJr = (x-a2)*(-1)-(x-a1)*(-1)

# H-G5 prox-regular-disjunct checks as PRINTED: prox-regular (r = 1,
# analytic), shift ball inside ONE connected component (C is connected;
# the whole boundary circle is feasible):
ball = XY[np.linalg.norm(XY - x1B, axis=-1) <= 0.6]
tol_unit = 16.0 * np.finfo(float).eps   # derived: fp error of unit-norm eval
assert ball.size > 0 and np.all(np.linalg.norm(ball, axis=-1) >= 1.0 - tol_unit), \
    "B1: shift ball inside the single connected component of C"
assert np.linalg.norm(x2B - x1B) < 0.6, "B1b: true argmax inside shift ball"

# --- form (T) at S*_red: tangent cone {d : <d, x1> >= 0}, mu_T = 1 --------
n = x1B
gn = float(np.dot(gB, n))
if gn >= 0.0:
    delta_T = float(np.linalg.norm(gB))
else:
    delta_T = float(np.linalg.norm(gB - gn * n))         # cone-boundary max
mu_T = 1.0   # ambient-Hessian floor of BOTH functionals on every cone
bound_TB = delta_T / mu_T
violB_T = shiftB / bound_TB
print(f"B2: form (T): delta_T = {delta_T:.4g}, bound = {bound_TB:.4g}, "
      f"actual shift = {shiftB:.4g}, violation = {violB_T:.1f}x")
assert violB_T >= 50.0, "B2: form (T) violated >= 50x under the disjunct"

# --- value route (F): its a-posteriori check PASSES yet the bound fails ---
basin_r = 0.6
feas = ball                                              # basin cap of C
eps_UB = float(np.max(np.abs(Jt(feas) - Jr(feas))))
bound_FB = 2.0 * np.sqrt(eps_UB / mu_T)
print(f"B3: value route: eps_U = {eps_UB:.4g}, bound = {bound_FB:.4g} vs "
      f"shift {shiftB:.4g}; a-posteriori check {bound_FB:.4g} <= "
      f"{basin_r} PASSES = {bound_FB <= basin_r}")
assert bound_FB <= basin_r, "B3a: value-route a-posteriori check passes"
assert bound_FB < shiftB, "B3b: ... while the value-route bound is FALSE"

# --- convex control: unit disk, interior argmaxes, both bounds tight ------
x1C, x2C = a1, a2                     # interior argmaxes on the convex disk
shiftC = np.linalg.norm(x2C - x1C)
delta_C = float(np.linalg.norm(gB))   # full-space cone at interior argmax
assert abs(delta_C / 1.0 - shiftC) <= 1e-12, "B4: convex control tight"
print(f"B4: convex control (unit disk): bound = shift = {shiftC:.4g} (tight)")

# --- violation grows without bound as eps_off -> 0 ------------------------
grow = []
for e_k in (0.1, 0.01, 0.001):
    g_k = e_k * (np.array([np.cos(theta), np.sin(theta)]) -
                 np.array([1.0, 0.0]))
    gn_k = float(np.dot(g_k, n))
    dT_k = float(np.linalg.norm(g_k) if gn_k >= 0
                 else np.linalg.norm(g_k - gn_k * n))
    grow.append(shiftB / dT_k)
print(f"B5: form-(T) violation factors along eps_off ladder {grow}")
assert all(v2 > v1 for v1, v2 in zip(grow, grow[1:])), "B5: growth monotone"

print("PART B: ALL ASSERTS PASS -- the prox-regular disjunct of H-G5 as")
print("        printed licenses forms whose bounds fail unboundedly;")
print("        convex control tight; nonconvex-boundary curvature is the")
print("        killer (second-fundamental-form correction missing).")

print()
print("ALL ASSERTS PASS (PART A + PART B).")

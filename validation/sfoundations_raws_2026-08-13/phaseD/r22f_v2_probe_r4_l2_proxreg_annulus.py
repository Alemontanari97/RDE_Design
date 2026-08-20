"""
r22f_v2_probe_r4_l2_proxreg_annulus.py — round-4 L2 probe (two attacks).

ATTACK 1 (PARTS A-F, feeds R22F-L2-25, BREAK): the prox-regular
disjunct of H-G5 ([REV2-r3-1](a), centerpiece :704-711) licenses forms
(T) and (F) on a CONNECTED, PROX-REGULAR (positive-reach = 1),
nonconvex feasible set — a 2-D annulus — where BOTH licensed
argmax-shift routes fail UNBOUNDEDLY in the small-perturbation limit,
while every other printed check passes (metric M = I, CONSTANT Hessian
=> uniform curvature floor on every ball, both a-posteriori radius
checks, form (C)'s multiplier-margin clause). The rationale sentence of
[REV2-r3-1] itself names SEGMENT FEASIBILITY as the consumed property;
prox-regularity within one connected component does not deliver it.

ATTACK 2 (PART G, feeds R22F-L2-26, AMENDMENT): the sweep-SAMPLED sup
of [REV2-r3-3](b) does not instantiate the uniform value-error premise:
a residual spike of width < the sweep spacing gives sampled sweep-sup
= 0 while the true basin sup drives an O(1) argmax shift — the
"until the sweep sup is measured, the premise is OPEN" implication is
unsound in the measured => discharged direction. Feasible set = an
interval (convex; H-G5 satisfied), isolating the sampling defect.

Synthetic counter-models only (CT-6 clean: no number from the four
nozzle papers used anywhere). All tolerances DERIVED from grid
resolutions; no magic constants. Pinned env, numpy only.
"""
import numpy as np

MU = 1.0          # curvature: J = -MU/2 |x|^2 +/- eps*x1 ; -Hess = MU*I exactly
R_IN, R_OUT = 1.0, 3.0

def J_red(x1, x2, eps):
    return -0.5 * MU * (x1 ** 2 + x2 ** 2) + eps * x1

def J_true(x1, x2, eps):
    return -0.5 * MU * (x1 ** 2 + x2 ** 2) - eps * x1

# ---------------------------------------------------------------- PART A
# Annulus argmaxes and shift (dense polar grid; tolerance = grid spacing).
EPS0 = 1e-4
nr, nt = 1201, 4801
r = np.linspace(R_IN, R_OUT, nr)
t = np.linspace(0.0, 2.0 * np.pi, nt, endpoint=False)
RR, TT = np.meshgrid(r, t, indexing="ij")
X1, X2 = RR * np.cos(TT), RR * np.sin(TT)
htol = max((R_OUT - R_IN) / (nr - 1), R_OUT * 2.0 * np.pi / nt)  # derived

Jr = J_red(X1, X2, EPS0)
Jt = J_true(X1, X2, EPS0)
ir = np.unravel_index(np.argmax(Jr), Jr.shape)
it_ = np.unravel_index(np.argmax(Jt), Jt.shape)
xr = np.array([X1[ir], X2[ir]])    # reduced argmax S*_red
xt = np.array([X1[it_], X2[it_]])  # true argmax
shift = float(np.linalg.norm(xr - xt))

assert abs(xr[0] - 1.0) < 3 * htol and abs(xr[1]) < 3 * htol, ("A1", xr)
assert abs(xt[0] + 1.0) < 3 * htol and abs(xt[1]) < 3 * htol, ("A2", xt)
assert abs(shift - 2.0) < 6 * htol, ("A3", shift)
print(f"A: annulus argmaxes S*_red={xr}, S*_true={xt}, shift={shift:.6f}")

# ---------------------------------------------------------------- PART B
# Form (T) at S*_red = (+1, 0), inner boundary active (|x| >= R_IN).
# Tangent cone there = {d : d . e_r >= 0} = {d1 >= 0}. Gradient gap
# g = grad J_true - grad J_red = (-2*eps, 0). Support-function residual
# delta_T = sup{ <g, d> : d in cone, |d| <= 1 } — analytic sup = 0,
# attained at d = (0, +-1). Numeric: dense direction sweep of the cone.
g = np.array([-2.0 * EPS0, 0.0])
phis = np.linspace(-np.pi / 2.0, np.pi / 2.0, 100001)  # d1 >= 0 half-circle
vals = g[0] * np.cos(phis) + g[1] * np.sin(phis)
delta_T = float(max(vals.max(), 0.0))  # 0 in cone-interior directions
bound_T = delta_T / MU
assert delta_T <= 2.0 * EPS0 * 1e-9, ("B1", delta_T)   # numerically zero
assert shift > 1.0 and bound_T < 1e-12, ("B2", shift, bound_T)
print(f"B: form (T) licensed bound = {bound_T:.3e} vs actual shift {shift:.3f}"
      f"  -> violation UNBOUNDED (bound is exactly 0)")

# ---------------------------------------------------------------- PART C
# Value route (F): eps_U = sup over the feasible set (and over the
# certified ball containing it) of |J_true - J_red| = 2*eps*|x1| <= 2*eps*R_OUT.
# Bound 2*sqrt(eps_U/MU); actual shift stays 2 for EVERY eps > 0
# (argmaxes are +-e1 independent of eps) -> violation ~ eps^{-1/2}.
eps_ladder = [1e-4, 1e-6, 1e-8]
viols = []
for e in eps_ladder:
    eps_U = 2.0 * e * R_OUT               # exact sup on the annulus
    bound_F = 2.0 * np.sqrt(eps_U / MU)
    viols.append(2.0 / bound_F)           # analytic shift = 2 (A3 witnessed)
assert viols[0] > 20.0, ("C1", viols)     # 41x at eps=1e-4
for k in range(len(viols) - 1):           # x10 per 100x eps drop (sqrt rate)
    ratio = viols[k + 1] / viols[k]
    assert abs(ratio - 10.0) < 1e-6, ("C2", ratio)
print(f"C: value-route violations along eps ladder {eps_ladder}: "
      f"{[f'{v:.1f}x' for v in viols]} -> UNBOUNDED as eps -> 0")

# Both a-posteriori radius checks PASS in the counter-model: basin radius
# R_basin = 4 covers C; bound_T = 0 <= R_basin; bound_F(1e-4) = 0.049 <= R_basin;
# reduced argmax inside the basin. All green while the true shift is 2.
R_basin = 4.0
assert bound_T <= R_basin and 2.0 * np.sqrt(2 * EPS0 * R_OUT / MU) <= R_basin

# ---------------------------------------------------------------- PART D
# Prox-regularity witness: the annulus has POSITIVE REACH = R_IN = 1
# (unique nearest point for every external point at distance < 1: hole
# points p (0 < |p| < 1) project to R_IN*p/|p| with uniqueness gap
# (R_IN+|p|) - (R_IN-|p|) = 2|p| > 0; outside points project radially).
# It is ONE connected component (path-connected in the polar chart).
for s in np.linspace(0.1, 0.9, 9):
    for ang in np.linspace(0.0, 2 * np.pi, 7, endpoint=False):
        p = s * np.array([np.cos(ang), np.sin(ang)])
        d_near = R_IN - s          # to p/|p| * R_IN
        d_far = R_IN + s           # to the antipodal inner-boundary point
        # brute-force check on the boundary grid:
        bts = np.linspace(0.0, 2 * np.pi, 20001, endpoint=False)
        bpts = R_IN * np.stack([np.cos(bts), np.sin(bts)], axis=1)
        dd = np.linalg.norm(bpts - p, axis=1)
        assert abs(dd.min() - d_near) < 1e-6, ("D1", s, ang)
        assert dd.max() > d_far - 1e-6, ("D2", s, ang)
        assert d_far - d_near > 0.1, ("D3",)  # uniqueness gap 2s >= 0.2
print("D: positive reach = 1 witnessed (unique projections in the hole); "
      "one connected component -> the H-G5 prox-regular disjunct is SATISFIED")

# ---------------------------------------------------------------- PART E
# Convex control: same J pair on the full disk |x| <= R_OUT (hole removed).
# Argmaxes at (+-EPS0/MU, 0) (interior), shift = 2*EPS0/MU; form (T) at an
# interior point has full-space cone -> delta_T = |g| = 2*EPS0; bound =
# 2*EPS0/MU = shift exactly (tight); value bound 0.049 >> shift. Both hold.
nr2 = 2401
rd = np.linspace(0.0, R_OUT, nr2)
RR2, TT2 = np.meshgrid(rd, t, indexing="ij")
Y1, Y2 = RR2 * np.cos(TT2), RR2 * np.sin(TT2)
jr2 = J_red(Y1, Y2, EPS0)
jt2 = J_true(Y1, Y2, EPS0)
i2 = np.unravel_index(np.argmax(jr2), jr2.shape)
i3 = np.unravel_index(np.argmax(jt2), jt2.shape)
yr = np.array([Y1[i2], Y2[i2]])
yt = np.array([Y1[i3], Y2[i3]])
shift_cv = float(np.linalg.norm(yr - yt))
htol2 = max(R_OUT / (nr2 - 1), R_OUT * 2.0 * np.pi / nt)
bound_T_cv = 2.0 * EPS0 / MU
assert shift_cv <= bound_T_cv + 4 * htol2, ("E1", shift_cv, bound_T_cv)
assert shift_cv <= 2.0 * np.sqrt(2 * EPS0 * R_OUT / MU) + 4 * htol2, ("E2",)
print(f"E: convex control (disk): shift={shift_cv:.3e} <= form-(T) bound "
      f"{bound_T_cv:.3e} (tight) — nonconvexity isolated as the sole killer")

# ---------------------------------------------------------------- PART F
# Form (C) multiplier-margin clause SATISFIED and blind: at S*_red=(1,0)
# the inner constraint |x| >= R_IN is active with multiplier
# lam = MU - EPS0 (KKT: grad J_red + lam * e_r = 0), strict
# complementarity; perturbation scale |g| = 2*EPS0 << lam. Under J_true
# the SAME point stays a KKT point (lam' = MU + EPS0 > 0): local shift
# of the KKT point = 0, while the global argmax sits at (-1, 0).
lam = MU - EPS0
lam_p = MU + EPS0
assert lam > 0 and lam_p > 0
assert lam / np.linalg.norm(g) > 1e3, ("F1", lam, np.linalg.norm(g))
grad_true_at_xr = np.array([-MU * 1.0 - EPS0, 0.0])
assert np.linalg.norm(grad_true_at_xr + lam_p * np.array([1.0, 0.0])) < 1e-12
print(f"F: multiplier-margin clause holds (lam={lam:.4f} >> |g|={2*EPS0:.1e});"
      " KKT point persists (local shift 0) while the GLOBAL argmax migrates"
      " to the antipode — the clause is structurally blind, as in the L0-16"
      " probe, but now on a CONNECTED prox-regular set.")

# ---------------------------------------------------------------- PART G
# Sweep-sampled sup vs the uniform premise ([REV2-r3-3](b)).
# 1-D basin [0,1], convex feasible set (H-G5 fine). J_true concave with
# floor MU; J_red = J_true + triangular spike of half-width w strictly
# between two sweep samples. Sampled sweep-sup = 0; true sup = E; the
# argmax shift is O(1) — the literal "measured sweep-sup" bound (= 0)
# is FALSE while the TRUE-sup bound holds (lemma sound, premise
# mis-instantiated).
a_true = 0.3
h_sweep = 0.05                       # 21 sweep samples on [0,1]
s_p = 0.7 + h_sweep / 2.0            # spike center strictly between samples
w = h_sweep / 4.0                    # spike half-width < sample spacing
E = 0.12                             # spike height (chosen so spike wins)

def j_true_1d(s):
    return -0.5 * MU * (s - a_true) ** 2

def j_red_1d(s):
    return j_true_1d(s) + E * np.maximum(0.0, 1.0 - np.abs(s - s_p) / w)

sweep = np.arange(0.0, 1.0 + 1e-12, h_sweep)          # the sampled sweep
sampled_sup = float(np.max(np.abs(j_red_1d(sweep) - j_true_1d(sweep))))
fine = np.linspace(0.0, 1.0, 400001)
true_sup = float(np.max(np.abs(j_red_1d(fine) - j_true_1d(fine))))
s_red_star = float(fine[np.argmax(j_red_1d(fine))])
s_true_star = float(fine[np.argmax(j_true_1d(fine))])
shift_g = abs(s_red_star - s_true_star)
ftol = 1.0 / 400000.0

assert sampled_sup < 1e-15, ("G1", sampled_sup)        # spike unseen by sweep
assert abs(true_sup - E) < 1e-12, ("G2", true_sup)
assert abs(s_red_star - s_p) < 2 * ftol, ("G3", s_red_star)
assert shift_g > 0.4, ("G4", shift_g)
bound_sampled = 2.0 * np.sqrt(sampled_sup / MU)        # = 0
bound_true = 2.0 * np.sqrt(true_sup / MU)              # = 0.693
assert bound_sampled < shift_g, ("G5",)                # literal reading FALSE
assert shift_g <= bound_true, ("G6",)                  # lemma itself SOUND
print(f"G: sampled sweep-sup = {sampled_sup:.1e} -> bound {bound_sampled:.1e}"
      f" vs actual shift {shift_g:.3f} (FALSE); true-sup bound"
      f" {bound_true:.3f} holds — the sampled sup does not instantiate the"
      " uniform premise; only a sweep-refinement-stable sup (the"
      " [REV2-r3-5] pattern) or the (U)-class theorem closes it.")

print("\nALL ASSERTS PASS (parts A-G).")

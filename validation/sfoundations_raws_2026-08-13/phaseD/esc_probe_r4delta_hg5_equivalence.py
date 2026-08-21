# esc_probe_r4delta_hg5_equivalence.py
# S-FOUNDATIONS-C4 escalation window, E-5 TARGETED REFUTER (lens L0),
# RES-CAP-1 round-4-delta pass. Feeds finding E5-L0-1 in
# esc_refute_r4delta_l0.md.
#
# TARGET SENTENCE (round-4 delta, [REV2-r4-2](a), printed at H-G5 sites
# phaseD_r22f_centerpiece.md :738-741 and :901-905):
#   "C \cap certified ball CONVEX (equivalently: the segment between
#    S*_red and every point of the shift ball feasible) ..."
# CLAIM UNDER TEST: "equivalently" — i.e. that the parenthetical segment
# condition and convexity of C \cap ball are the same condition.
#
# WHAT THIS PROBE SHOWS (executably, both directions):
#  DIRECTION 1 (star-shaped, nonconvex): a feasible set that is
#   star-shaped about S*_red (segment condition HOLDS in its only
#   executable reading, "every FEASIBLE point of the shift ball") while
#   C \cap ball is NOT convex (witness midpoint infeasible). The two
#   sides of "equivalently" give DIFFERENT license verdicts.
#   Additionally: both licensed bounds (form (T) and the value route)
#   HOLD on this instance — the parenthetical branch is a WEAKER
#   sufficient condition, so the mislabel licenses nothing unsound
#   (this is why the finding is AMENDMENT, not BREAK).
#  DIRECTION 2 (boundary S*, convex): a convex C \cap ball at a
#   margin-active boundary S*_red where the LITERAL reading of the
#   parenthetical ("EVERY point of the shift ball", including
#   infeasible ones) FAILS — the exact vacuity-at-boundary pattern
#   R22F-L2-25 criticized in the round-3 line. Convexity licenses;
#   the literal gloss refuses. Again NOT an equivalence.
#
# Pinned env, numpy only. Synthetic models only (CT-6 clean: no number
# from any nozzle paper). Tolerances derived from grid resolution.

import numpy as np

rng = np.random.default_rng(20260820)

# ----------------------------------------------------------------------
# DIRECTION 1: star-shaped-not-convex feasible set, interior S*_red
# ----------------------------------------------------------------------
# C = { (r,theta) : r <= R(theta) }, R(theta) = 1 + a*cos(3 theta).
# Radial graph about the origin => star-shaped about the origin by
# construction (r' = t*r <= r <= R(theta) along the ray for t in [0,1]).
A_LOBE = 0.4


def R_of(theta):
    return 1.0 + A_LOBE * np.cos(3.0 * theta)


def feasible1(x):
    r = np.hypot(x[0], x[1])
    th = np.arctan2(x[1], x[0])
    return r <= R_of(th) + 1e-12


MU = 1.0                      # both Hessians = -MU*I (constant):
B = np.array([0.35, 0.35])    # J_true argmax target (interior point)
# J_red  = -(MU/2)|x|^2          -> argmax on C at S*_red = origin
# J_true = -(MU/2)|x - B|^2      -> unconstrained argmax at B
# NOTE: identical curvature floors (mu_true = mu_red = MU) => the
# mu-identity repair [REV2-r4-1] is NOT confounded here; H-G6 L_H = 0.
assert feasible1(B), "B must be interior-feasible"
S_RED = np.array([0.0, 0.0])

CERT_RADIUS = 1.5             # certified ball about S*_red covers C
# (max R = 1.4 < 1.5, so C \cap ball = C: the nonconvexity of C itself
#  is the nonconvexity of C \cap ball.)

# --- (1a) C \cap ball is NOT convex: witness pair in two lobes whose
# midpoint is infeasible. Lobes of R(theta) peak at theta = 0, 2pi/3,
# 4pi/3; the boundary dips to 0.6 at theta = pi/3.
p1 = 1.35 * np.array([np.cos(0.12), np.sin(0.12)])          # lobe 1
p2 = 1.35 * np.array([np.cos(2 * np.pi / 3 - 0.12),
                      np.sin(2 * np.pi / 3 - 0.12)])        # lobe 2
mid = 0.5 * (p1 + p2)
assert feasible1(p1) and feasible1(p2), "witness endpoints feasible"
assert not feasible1(mid), "witness midpoint infeasible => NOT convex"

# --- (1b) segment condition, executable reading A ("every feasible
# point of the shift ball"): grid over the ball, segments sampled.
NGRID = 61                    # grid step h = 2*CERT_RADIUS/(NGRID-1)
h = 2 * CERT_RADIUS / (NGRID - 1)
xs = np.linspace(-CERT_RADIUS, CERT_RADIUS, NGRID)
seg_ok = True
lit_fail_witness = None       # literal reading B failure witness
NSEG = 33
ts = np.linspace(0.0, 1.0, NSEG)
for xi in xs:
    for yi in xs:
        p = np.array([xi, yi])
        if np.hypot(xi, yi) > CERT_RADIUS:
            continue
        if feasible1(p):
            # reading A: segment S_RED -> p must be feasible
            for t in ts:
                if not feasible1(S_RED + t * (p - S_RED)):
                    seg_ok = False
        else:
            lit_fail_witness = p  # ball point infeasible => literal
            #                       reading B fails on this set too
assert seg_ok, "star-shapedness about S*_red must hold (reading A)"
assert lit_fail_witness is not None, \
    "ball exits C => literal reading B fails while reading A holds"

# --- (1c) the licensed bounds nevertheless HOLD on this instance.
# True argmax on C by dense grid (resolution-limited, declared):
best, bestval = None, -np.inf
NF = 801
xf = np.linspace(-1.5, 1.5, NF)
hf = xf[1] - xf[0]
for xi in xf:
    for yi in xf:
        p = np.array([xi, yi])
        if feasible1(p):
            v = -(MU / 2) * np.dot(p - B, p - B)
            if v > bestval:
                bestval, best = v, p
shift = np.linalg.norm(best - S_RED)
# form (T): interior S*_red => tangent cone = R^2; delta_T =
# |grad J_true(S_RED) - grad J_red(S_RED)| = |MU*B|
delta_T = MU * np.linalg.norm(B)
bound_T = delta_T / MU
tol_grid = 2.0 * hf  # grid argmax resolution, derived
assert shift <= bound_T + tol_grid, \
    f"form-(T) bound must hold: shift={shift:.4f} bound={bound_T:.4f}"
# value route: eps_U = sup over C of |J_true - J_red| (grid sup,
# lower estimate; adequate here since the bound holds with margin)
eps_grid = 0.0
for xi in xf:
    for yi in xf:
        p = np.array([xi, yi])
        if feasible1(p):
            d = abs(-(MU / 2) * np.dot(p - B, p - B)
                    + (MU / 2) * np.dot(p, p))
            eps_grid = max(eps_grid, d)
bound_V = 2.0 * np.sqrt(eps_grid / MU)
assert shift <= bound_V + tol_grid, \
    f"value-route bound must hold: shift={shift:.4f} bound={bound_V:.4f}"

print("DIRECTION 1 (star-shaped about S*_red, NONCONVEX C \\cap ball):")
print(f"  convexity check: FAILS (witness midpoint infeasible at "
      f"({mid[0]:.3f},{mid[1]:.3f}))")
print(f"  segment condition, reading A (feasible ball points): HOLDS "
      f"({NGRID}x{NGRID} grid, {NSEG}-pt segments)")
print(f"  literal reading B (every ball point): FAILS (witness "
      f"({lit_fail_witness[0]:.3f},{lit_fail_witness[1]:.3f}) infeasible)")
print(f"  licensed bounds on this instance: shift={shift:.4f} <= "
      f"form-(T) {bound_T:.4f} and value-route {bound_V:.4f} (both HOLD)")
print("  => the two sides of 'equivalently' give DIFFERENT license"
      " verdicts; the parenthetical is weaker-but-sufficient, not"
      " equivalent.")

# ----------------------------------------------------------------------
# DIRECTION 2: convex C \cap ball, boundary (margin-active) S*_red
# ----------------------------------------------------------------------
# C = half-plane {x1 <= 0}; J_red = -(MU/2)|x|^2 + c*x1 with c > 0:
# unconstrained argmax (c/MU, 0) is infeasible; constrained argmax is
# the boundary point S*_red = origin (margin-active).
C2 = 0.3


def feasible2(x):
    return x[0] <= 1e-12


S2 = np.array([0.0, 0.0])
# KKT check at S2: grad J_red(S2) = (c, 0) points along +x1, blocked by
# the constraint => S2 is the constrained argmax (concave problem).
SHIFT_BALL_R = 0.5
# convexity of C \cap ball: half-disk — convex (no witness pair can
# exist; verified on a grid for the record)
conv_ok = True
NG2 = 41
g2 = np.linspace(-SHIFT_BALL_R, SHIFT_BALL_R, NG2)
pts = [np.array([xi, yi]) for xi in g2 for yi in g2
       if np.hypot(xi, yi) <= SHIFT_BALL_R and feasible2((xi, yi))]
for _ in range(2000):
    i, j = rng.integers(0, len(pts), 2)
    m = 0.5 * (pts[i] + pts[j])
    if not feasible2(m):
        conv_ok = False
assert conv_ok, "C \\cap ball must be convex (half-disk)"
# literal reading B: the point (SHIFT_BALL_R/2, 0) is in the shift ball
# and INFEASIBLE => "segment between S*_red and every point of the
# shift ball feasible" FAILS at every boundary S* — vacuity pattern.
p_bad = np.array([SHIFT_BALL_R / 2, 0.0])
assert np.linalg.norm(p_bad - S2) <= SHIFT_BALL_R
assert not feasible2(p_bad)
print("DIRECTION 2 (convex half-disk, margin-active boundary S*_red):")
print("  convexity check: HOLDS (2000 random midpoints feasible)")
print(f"  literal reading B: FAILS (ball point ({p_bad[0]:.2f},0)"
      " infeasible) — the gloss un-licenses a validly convex instance"
      " at every boundary S* (the L2-25 vacuity pattern).")
print("  => not an equivalence in this direction either.")

print()
print("PROBE-VERDICT: ALL ASSERTS PASS. The [REV2-r4-2](a) parenthetical"
      " '(equivalently: ...)' is NOT an equivalence: reading A is a"
      " strictly weaker sufficient condition (direction 1), the literal"
      " reading refuses valid convex instances at boundary S*"
      " (direction 2). No unsound license arises from any reading"
      " (direction 1 bounds hold) => AMENDMENT class, wording repair"
      " only: 'the consumed property, a sufficient form' per the"
      " refuters' own L2-25(a)/L0-20(a) fix-shape language.")

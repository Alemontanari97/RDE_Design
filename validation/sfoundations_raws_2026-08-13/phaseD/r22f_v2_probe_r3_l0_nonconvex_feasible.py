"""R22-F v2 probe, round 3, lens L0: nonconvex feasible set kills BOTH
licensed argmax-shift forms while every OTHER printed condition holds.

Target: phaseD_r22f_centerpiece.md §2.2-bis [REV2-r2-3]:
  (A) form (T) tangent-cone bound |shift| <= delta_T/mu_T
      (printed hypothesis "(unconditional on convex feasible sets)" :589);
  (A) form (C) critical-cone bound under the multiplier-margin clause;
  (F) value-route bound |shift| <= 2*sqrt(eps_U/mu);
  H-G4 (:639-642) + R-13 (:1367): "form (T) ... is licensed there" at a
      margin-active S* -- WITHOUT carrying the convexity hypothesis.

Counter-model (synthetic, CT-6 clean: no number from any nozzle paper):
  1-D design space, metric M = I (condition (3) satisfied).
  Feasible set  C = (-inf, -1] U [+1, +inf)   (NONCONVEX: two branches;
      the 1-D cartoon of a margin-type constraint x^2 >= 1).
  J_red(x)  = -x^2 + h x,  h = +0.002  -> strict argmax over C at x1 = +1.
  J_true(x) = -x^2 + g x,  g = -0.005  -> strict argmax over C at x2 = -1.
  Curvature -J'' = 2 = mu, CONSTANT -> the curvature floor is uniform on
  every ball: any basin-radius certificate passes condition (1)'s check.
  Gradient gap grad J_true - grad J_red = (g - h) = -0.007, constant.

PART A: form (T) at x1 = +1. Tangent cone of C at +1 is {d >= 0}
  (d < 0 exits C into (-1,1)). Support-function delta_T
  = sup{ (g-h)*d : d in [0,1] } = 0  =>  licensed bound delta_T/mu = 0.
  Actual global shift = 2. UNBOUNDED violation.
PART B: value route (F). eps_U = sup_{|x|<=R} |J_true - J_red|
  = |g-h|*R = 0.0105 (R = 1.5). Bound 2*sqrt(eps_U/mu) ~= 0.145.
  Actual shift = 2. ~14x violation.
PART C: form (C)'s multiplier-margin clause is SATISFIED and useless:
  constraint c(x) = x^2 - 1 >= 0 active at x1, KKT multiplier
  lam = (2-h)/2 ~= 0.999 >> |g-h| = 0.007 (any named margin holds);
  the LOCAL argmax on the +1 branch does not move at all under the
  perturbation (local active-set stability, Bonnans-Shapiro regime OK) --
  yet the GLOBAL argmax migrates to the other component (shift 2).
  The clause is local; global migration across disconnected feasible
  components is invisible to it. On a convex set global = local, which
  is exactly why the convexity hypothesis is load-bearing.
PART D (control): the CONVEXIFIED set [-R, R]. Both bounds hold
  (form (T) is tight: shift = |g-h|/2 = delta_T/mu exactly), isolating
  nonconvexity as the sole killer.
"""

import numpy as np

h = 0.002    # reduced-functional tilt
g = -0.005   # true-functional tilt
mu = 2.0     # -J'' (curvature floor, constant => uniform on every ball)
R = 1.5      # certified ball radius (contains both argmaxes)
gap = g - h  # constant gradient gap = -0.007

def J_red(x):  return -x**2 + h*x
def J_true(x): return -x**2 + g*x

# --- feasible set C = [-R,-1] U [1,R] (grid) --------------------------------
left  = np.linspace(-R, -1.0, 200001)
right = np.linspace(1.0, R, 200001)
xs = np.concatenate([left, right])

x1 = xs[np.argmax(J_red(xs))]    # reduced argmax
x2 = xs[np.argmax(J_true(xs))]   # true argmax
assert abs(x1 - 1.0) < 2e-5, x1      # strict (h > 0 breaks the tie)
assert abs(x2 + 1.0) < 2e-5, x2      # strict (g < 0)
shift = abs(x2 - x1)
assert shift > 1.999, shift          # global argmax shift = 2

# --- PART A: form (T) tangent-cone bound ------------------------------------
# T_C(x1=+1) = {d >= 0}; support-function form (B): sup{gap*d : d in cone,
# |d| <= 1} = max(gap, 0) = 0 since gap < 0.
delta_T = max(gap, 0.0)
bound_T = delta_T / mu
assert bound_T == 0.0
assert shift > bound_T + 1.9, "form (T) violated UNBOUNDEDLY on nonconvex C"

# --- PART B: value-route bound (F) ------------------------------------------
eps_U = abs(gap) * R                     # uniform value error on the ball
bound_V = 2.0 * np.sqrt(eps_U / mu)
assert bound_V < 0.15, bound_V
assert shift > 13.0 * bound_V, "value route (F) violated ~14x on nonconvex C"

# --- PART C: form (C) multiplier-margin clause satisfied, yet migration -----
lam = (2.0 - h) / 2.0                    # KKT multiplier of x^2-1>=0 at x1
assert lam > 0.99                        # strict complementarity
assert lam > 100.0 * abs(gap)            # multiplier >> any perturbation margin
x_loc = right[np.argmax(J_true(right))]  # local argmax on the +1 branch
assert abs(x_loc - 1.0) < 2e-5           # LOCAL shift = 0: active set stable
# => Bonnans-Shapiro-class local stability holds; global shift is still 2.

# --- PART D: convex control [-R, R] -----------------------------------------
xc = np.linspace(-R, R, 600001)
x1c = xc[np.argmax(J_red(xc))]           # h/2  = +0.001
x2c = xc[np.argmax(J_true(xc))]          # g/2  = -0.0025
shift_c = abs(x2c - x1c)                 # 0.0035
delta_T_cvx = abs(gap)                   # interior point: cone = R
assert abs(shift_c - 0.0035) < 2e-5, shift_c
assert shift_c <= delta_T_cvx / mu + 2e-5      # form (T) holds (tight)
assert shift_c <= bound_V                       # value route holds
print("ALL ASSERTS PASS.")
print(f"  nonconvex C : shift = {shift:.4f}  | form(T) bound = {bound_T:.4f} "
      f"(unbounded violation) | value bound = {bound_V:.4f} "
      f"({shift/bound_V:.1f}x violation)")
print(f"  form (C)    : multiplier lam = {lam:.4f} >> |gap| = {abs(gap):.4f}; "
      f"local shift = {abs(x_loc-1.0):.2e} (clause satisfied, migration unseen)")
print(f"  convex ctrl : shift = {shift_c:.4f} <= delta/mu = "
      f"{delta_T_cvx/mu:.4f} (tight) <= value bound {bound_V:.4f}")

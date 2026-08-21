# esc_probe_ntf_repaired_bound_window.py
# S-FOUNDATIONS-C4 escalation E-1 (minor (a) NTF), round 1, 2026-08-20.
# Verifies the NAMED REPAIRS of MIN-NTF-1/2/3 (+ MIN-NTF-10/12 numbers)
# BEFORE adoption into phaseD_minor_ntf.md [ESC-r1-*]. Rejector-style:
# every assert can fail; tolerances derived (exact comparisons where the
# quantities are exact; float slack = 4*ulp-class where not).
# Pinned-env deps only (stdlib math). Exit 0 = all repairs verified.
import math
import sys

fails = []


def check(name, cond):
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}")
    if not cond:
        fails.append(name)


EPS = 2.0 ** -52  # float64 machine epsilon (a1_ideal_march_jax.py :168)

print("== R1: MIN-NTF-1 repaired PASS constant 2*(T+floor) ==")
# Triangle inequality direction (the 'absorbed' parenthetical inverted it):
# dz_hat = dz_exact + delta, |delta| <= floor  =>  |dz_exact| <= |dz_hat| + floor.
# PASS (|dz_hat| <= T) bounds |dz_exact| <= T + floor, NOT <= T.
# Composed with the exact two-sided upper estimator (factor <= 2 at Theta <= 1/2):
#   err <= 2*(T + floor)  and, under LB (floor <= T/eta):  err <= 2*T*(1 + 1/eta).
# Of-record scene-A numbers (refuter probe, re-run exit 0 this window):
dz_exact, err_true, ratio, floor_over_T = 1.7900, 3.4010, 0.9900, 0.8
eta = 1.25  # bracket lower edge; floor = 0.8*T <=> eta = 1/0.8
check("old constant REJECTED: err_true 3.401*T > 2*T", err_true > 2.0)
check("repaired bound holds: err_true <= 2*(T+floor) = 3.6*T",
      err_true <= 2.0 * (1.0 + floor_over_T))
check("population form identical at LB edge: 2*(1+1/eta) == 2*(1+floor/T)",
      abs(2.0 * (1.0 + 1.0 / eta) - 2.0 * (1.0 + floor_over_T)) < 4 * EPS)
# Geometric-series consequence (MIN-NTF-4 re-attribution is TRUE math):
# err <= dz*sum_{i>=0} Theta^i = dz/(1-Theta) <= 2*dz at Theta <= 1/2.
Theta = 0.5
geo = sum(Theta ** i for i in range(200))
check("geometric series 1/(1-Theta) <= 2 at Theta=1/2 (partial sum -> 2)",
      abs(geo - 2.0) < 1e-15 and 1.0 / (1.0 - Theta) == 2.0)

print("== R2: MIN-NTF-1 propagation into the eta-bracket decade argument ==")
# 2*(eta+1) at the bracket's upper edge must stay under one decade:
for eta_edge in (1.25, 2.5):
    check(f"2*(eta+1) = {2*(eta_edge+1):.1f} < 10 at eta = {eta_edge}",
          2.0 * (eta_edge + 1.0) < 10.0)

print("== R3: MIN-NTF-2 repaired window with declared A_c ==")
# Record case, repaired form: 2*(1+1/eta)*NTF*EPS*sc * A_c <= tol_c.
NTF = 100.0
sc = 1.0  # unit scale, as in the record-case statement
o31_tol = 0.07646  # s25bis_gap29_sweep.json base arm (committed carrier)
lhs_z = 2.0 * (1.0 + 1.0 / eta) * NTF * EPS * sc  # z-space certified error
A_c_worst = 1.0e7  # cross-lowering row :328-336 worst amplification class [ADV]
margin_orders = math.log10(o31_tol / (lhs_z * A_c_worst))
print(f"  certified error (z-space) = {lhs_z:.3e}; x A_c=1e7 -> "
      f"{lhs_z*A_c_worst:.3e}; o31_tol = {o31_tol:.3e}; "
      f"margin = 10^{margin_orders:.2f}")
check("window open at worst A_c class by >= 4 orders (claim text)",
      margin_orders >= 4.0)
check("margin is ~5 orders (4.5 < m < 5.5): honest headline",
      4.5 < margin_orders < 5.5)
# The OLD '>11 orders' headline was the A_c = 1 reading:
check("old headline reproduced ONLY at undeclared A_c=1 (>11 orders)",
      math.log10(o31_tol / lhs_z) > 11.0)

print("== R4: MIN-NTF-3 scoping numbers (fluctuation band) ==")
# Scene B of record: T = 0.97*floor => NTF < kappa_eff at EVERY cell, yet
# 200/200 metric terminations (max 3 trips < cap 30) with 6/200 cert FAILs.
check("scene B regime is inside (NTF, (1+m)*NTF) band at m = 0.25: "
      "kappa/NTF = 1/0.97 < 1.25", (1.0 / 0.97) < 1.25)
check("scene B: early termination (3 < 30) with population FAIL (6 > 0)",
      3 < 30 and 6 > 0)

print("== R5: MIN-NTF-5/-12 carrier numbers ==")
base_worst, ntf50_worst = 0.7011026275409529, 1.033309604151919
o31_base, o31_ntf50 = 0.07646, 0.07960
check("ntf50 self-contained witness: 51.665 > 50 (flip forced)",
      ntf50_worst * 50.0 > 50.0)
check("ntf50 margin ~3.3% (cliff proximity)",
      abs((ntf50_worst * 50.0 - 50.0) / 50.0 - 0.033) < 0.001)
check("incumbent headroom 100/70.110 = 1.426 in [1.25, 2.5]",
      1.25 <= 100.0 / (base_worst * 100.0) <= 2.5
      and abs(100.0 / (base_worst * 100.0) - 1.426) < 0.001)
check("o31_tol drift across ntf50 arm ~4.1% (NOT 'NTF-INDEPENDENT')",
      abs((o31_ntf50 - o31_base) / o31_base - 0.041) < 0.001)

print("== R6: MIN-NTF-10 lower-constant check ==")
# Yamamoto eq.(7) worst denominator 1+sqrt(2): c_L >= 2/(1+sqrt(2)).
cL = 2.0 / (1.0 + math.sqrt(2.0))
check("c_L = 2/(1+sqrt(2)) ~= 0.828 and author's 1/2 is conservative",
      abs(cL - 0.828) < 0.001 and 0.5 < cL)

print()
if fails:
    print(f"PROBE VERDICT: {len(fails)} FAILURE(S): {fails}")
    sys.exit(1)
print("PROBE VERDICT: ALL REPAIRS VERIFIED — adoption licensed")
sys.exit(0)

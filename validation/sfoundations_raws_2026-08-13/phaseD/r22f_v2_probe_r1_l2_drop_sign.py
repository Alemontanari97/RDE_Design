"""R22F-L2 probe (round 1, lens L2): sign + degeneracy of the within-fiber
J-variation under the DROP h0-convention.

TARGET: phaseD_r22f_centerpiece.md [T-DISC-2](i) as printed:
  "Hence J separates single-signedly: J(s_lambda) strictly decreases in
   lambda^2 on the supersonic-map sector."
quantified over the fiber family of [T-DISC-1], which EXPLICITLY includes the
DROP-convention variant ("h0 fixed under the DROP convention verbatim").

CLAIM UNDER ATTACK: strict single-signed DECREASE for all admissible s_lambda.
ATTACK: under DROP the fiber fixes the DATA h0-trace (which excludes swirl
KE), so the PHYSICAL total enthalpy varies along the fiber:
  h0_phys(lambda) = h0_data + Gamma(lambda)^2 / (2 r_in^2).
With Gamma conserved per streamline, the exact per-streamline relation
(swirl5f judgeverify sec. 5.3, re-used at fixed p_e, s, v_e, r_e):
  u_e^2 = 2 (h0_phys - h(p_e, s)) - v_e^2 - Gamma^2 / r_e^2
gives
  Delta u_e^2 = Gamma^2 (1/r_in^2 - 1/r_e^2)
which is > 0 for r_e > r_in (J INCREASES) and == 0 for r_e = r_in
(ZERO separation: degenerate fiber direction).
Record corroboration: swirl5f judgeverify sec. 5.2 (:174-190) computes the
same drop bias, "geometry-signed, ~= 0 at r_exit ~= r_in" (verifier R-B).

Pinned env only (numpy). Exit code 0 = counterexample stands.
"""
import numpy as np

# Fiber data (held fixed across the family): pressure trace (=> h_e fixed at
# fixed s), h0-TRACE (convention-declared), s-trace, mass-flux trace.
H0_DATA = 2.0e6     # J/kg  fiber h0-trace value
H_E     = 1.0e6     # J/kg  h(p_e, s), fixed (p_e, s fixed across the fiber)
V_E     = 0.0       # m/s   exit meridional-radial velocity (fixed, H2.2)
R_IN    = 0.05      # m     interface radius of the swirl-bearing streamtube
UTH1    = 300.0     # m/s   unit-lambda interface swirl (corpus scale:
                    #       eps_theta ~ 0.15-0.20 of an Omega*r ~ 1.8-3.2 km/s
                    #       wheel gives u_theta ~ 270-640 m/s; 300 is in-band)

def u_e(lam, r_e, convention):
    """Exit axial velocity of the fiber element s_lambda."""
    Gamma = lam * UTH1 * R_IN
    if convention == "FOLD":      # data h0 = physical h0 (compensated exhibit)
        h0_phys = H0_DATA
    elif convention == "DROP":    # data h0 excludes swirl KE
        h0_phys = H0_DATA + Gamma**2 / (2.0 * R_IN**2)
    else:
        raise ValueError(convention)
    val = 2.0 * (h0_phys - H_E) - V_E**2 - Gamma**2 / r_e**2
    assert val > 0.0
    return np.sqrt(val)

lams = np.linspace(0.0, 1.0, 11)

# 1) FOLD / compensated variant (physical h0 fixed): theorem core must hold —
#    strict decrease in lambda^2, every geometry.
for r_e in (0.5 * R_IN, R_IN, 2.0 * R_IN):
    ue = np.array([u_e(l, r_e, "FOLD") for l in lams])
    assert np.all(np.diff(ue) < 0.0), "FOLD core violated?!"
print("FOLD (physical-h0-fixed): strict decrease in lambda -- PASS "
      "(theorem core survives)")

# 2) DROP, r_e = 2 r_in: COUNTEREXAMPLE — strict INCREASE.
ue = np.array([u_e(l, 2.0 * R_IN, "DROP") for l in lams])
assert np.all(np.diff(ue) > 0.0), "expected strict increase"
print("DROP, r_e = 2 r_in: u_e(lam=0) = %.6f, u_e(lam=1) = %.6f  m/s "
      "-> J INCREASES (momentum term mdot*u_e up %.3f%%, pressure term "
      "fixed): 'strictly decreases' FALSIFIED"
      % (ue[0], ue[-1], 100.0 * (ue[-1] / ue[0] - 1.0)))

# 3) DROP, r_e = r_in: DEGENERACY — zero separation identically.
ue = np.array([u_e(l, R_IN, "DROP") for l in lams])
assert np.allclose(ue, ue[0], rtol=0.0, atol=1e-12 * ue[0])
print("DROP, r_e = r_in: u_e constant over the whole family "
      "-> ZERO within-fiber J-separation (degenerate fiber direction; "
      "the 'strictly positive' lower-bound reading fails here)")

# 4) Cross-check vs the record's R-B boundary: |drop bias| / fold debit
#    = r_e^2/r_in^2 - 1  ->  equals 1 exactly at r_e = sqrt(2) r_in.
lam = 0.05  # first order
for r_fac, expect in ((np.sqrt(2.0), 1.0), (1.2, 1.2**2 - 1.0)):
    r_e = r_fac * R_IN
    drop = u_e(lam, r_e, "DROP")**2 - u_e(0.0, r_e, "DROP")**2
    fold = u_e(0.0, r_e, "FOLD")**2 - u_e(lam, r_e, "FOLD")**2
    ratio = drop / fold
    assert abs(ratio - expect) < 1e-9, (ratio, expect)
print("ratio |drop|/fold = r_e^2/r_in^2 - 1 verified; = 1 at r_e = "
      "sqrt(2) r_in  (reproduces judgeverify sec 5.2 / R-B boundary)")

print("\nPROBE VERDICT: [T-DISC-2](i) as printed is FALSE on DROP-convention "
      "fiber families (increase for r_e > r_in, zero at r_e = r_in); the "
      "core survives only on physical-h0-fixed comparisons (FOLD or "
      "compensated variant). REPAIR: convention-scope the sign leg.")

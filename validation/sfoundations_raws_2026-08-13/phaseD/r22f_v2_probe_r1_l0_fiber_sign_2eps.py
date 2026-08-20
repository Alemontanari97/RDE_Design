# r22f_v2_probe_r1_l0_fiber_sign_2eps.py
# S-FOUNDATIONS-C4 Blocco 1 v2, round 1, REFUTER lens L0
# (variational/optimization structure). Executable counterexamples for
# findings R22F-L0-4 / R22F-L0-5 / R22F-L0-6 against
# validation/sfoundations_raws_2026-08-13/phaseD/phaseD_r22f_centerpiece.md.
#
# ALL numbers here are SYNTHETIC counter-model inputs (refuter probe):
# they enter NO bound, band, or cell of the deliverable (CT-6 respected;
# no number from the four nozzle papers is used anywhere).
# Env: pinned (numpy only; no installs).

import numpy as np

print("=" * 72)
print("PART A - R22F-L0-4: [T-DISC-3] misapplication of the 2-eps lemma")
print("=" * 72)
# Draft claim ([T-DISC-3]): "if a designer optimizes ANY functional that
# factors through pi ... the resulting design is up to 2*eps_fib
# suboptimal for the true J", eps_fib(P) := sup over the fiber of
# |J(s) - J(s')|.
# Record lemma (swirl5f_fun.md :546-564): J_exact vs J_avg with premise
# (U): sup_Sigma |J_exact - J_avg| <= eps.  The transplant to arbitrary
# f∘pi with eps := eps_fib is FALSE. Counterexample:
# two designs in DIFFERENT fibers, each fiber a singleton (eps_fib = 0),
# surrogate f == 0 (factors through pi trivially).
designs = ["Sigma1", "Sigma2"]
P_trace = {"Sigma1": "P_A", "Sigma2": "P_B"}   # different fibers
J_exact = {"Sigma1": 0.0, "Sigma2": 10.0}
# every fiber realized by exactly one design => eps_fib = 0 for both
eps_fib = 0.0
# f factors through pi and is constant => every design is an argmax of f
f = {d: 0.0 for d in designs}
argmax_f = "Sigma1"  # legitimate argmax selection of f
subopt = max(J_exact.values()) - J_exact[argmax_f]
print(f"eps_fib (both fibers singletons)      = {eps_fib}")
print(f"suboptimality of an argmax of f       = {subopt}")
print(f"draft's claimed ceiling 2*eps_fib     = {2*eps_fib}")
assert subopt > 2 * eps_fib, "counterexample failed?!"
print("=> claim 'up to 2*eps_fib suboptimal for ANY functional factoring")
print("   through pi' is FALSE as stated: suboptimality 10 > 2*eps_fib=0.")
print("   (The record lemma needs (U) for the SPECIFIC surrogate; the")
print("   fiber spread eps_fib does not bound |J_exact - f(pi(.))| for")
print("   arbitrary f. Salvageable content = best-surrogate LOWER bound,")
print("   see finding text.)")

print()
print("=" * 72)
print("PART B - R22F-L0-5: H2.2 over-determination on actual solutions")
print("=" * 72)
# Quasi-1D annular swirling exit, perfect gas (SYNTHETIC counter-model):
# per-phase steady streamtube with invariants (h0_true, s, Gamma).
# Show: at fixed (h0, s, mdot, A_e, r_e) the exit static pressure is an
# OUTPUT; turning on Gamma forces p_e to move (so H2.2 'fixed exit
# static-pressure trace' + fiber-fixed mdot cannot BOTH hold on a pair
# of actual solutions), and the actual Delta J differs from the
# frozen-p_e booking Delta J used by [T-DISC-2](i).
g = 1.25
R = 287.0
cp = g * R / (g - 1.0)
T0 = 3000.0
p0 = 2.0e6
r_e = 0.15
A_e = 0.05
Pa = 0.0  # vacuum reading, keeps the pressure-thrust term clean

def exit_state(p_e, Gam):
    T_e = T0 * (p_e / p0) ** ((g - 1.0) / g)      # s fixed
    ke_ax2 = 2.0 * cp * (T0 - T_e) - (Gam / r_e) ** 2
    if ke_ax2 <= 0.0:
        return None
    u_e = np.sqrt(ke_ax2)                          # v_e = 0 (axial exit)
    rho_e = p_e / (R * T_e)
    return T_e, u_e, rho_e

def flux(p_e, Gam):
    st = exit_state(p_e, Gam)
    return -1.0 if st is None else st[2] * st[1] * A_e

# base (Gamma = 0) solution at a supersonic exit pressure
p_e0 = 0.05 * p0
T_e0, u_e0, rho_e0 = exit_state(p_e0, 0.0)
mdot0 = rho_e0 * u_e0 * A_e
M0 = u_e0 / np.sqrt(g * R * T_e0)
print(f"base: p_e0={p_e0:.4g} Pa, u_e0={u_e0:.1f} m/s, M={M0:.2f}, "
      f"mdot={mdot0:.3f} kg/s")

# swirl on: exit swirl angle ~12 deg at the base state
Gam = u_e0 * np.tan(np.deg2rad(12.0)) * r_e
print(f"Gamma={Gam:.3f} m^2/s  (u_theta,e ~ {Gam/r_e:.1f} m/s)")

# supersonic-branch bisection for p_e1 with the SAME mdot (mass cons.)
grid = np.linspace(1e3, 0.6 * p0, 20000)
fx = np.array([flux(p, Gam) for p in grid])
i_star = int(np.argmax(fx))                        # critical point
lo, hi = grid[0], grid[i_star]                     # flux increasing here
for _ in range(200):
    mid = 0.5 * (lo + hi)
    if flux(mid, Gam) < mdot0:
        lo = mid
    else:
        hi = mid
p_e1 = 0.5 * (lo + hi)
T_e1, u_e1, rho_e1 = exit_state(p_e1, Gam)
mdot1 = rho_e1 * u_e1 * A_e
assert abs(mdot1 - mdot0) / mdot0 < 1e-8

J0 = mdot0 * u_e0 + (p_e0 - Pa) * A_e
J1 = mdot0 * u_e1 + (p_e1 - Pa) * A_e
dJ_actual = J1 - J0
# frozen-p_e booking comparison ([T-DISC-2](i) reading): p_e held at p_e0
st_frozen = exit_state(p_e0, Gam)
dJ_booking = mdot0 * (st_frozen[1] - u_e0)         # pressure term "fixed"
print(f"actual solution with swirl: p_e1={p_e1:.4g} Pa "
      f"(shift {100*(p_e1-p_e0)/p_e0:+.2f}%), u_e1={u_e1:.1f} m/s")
print(f"Delta J booking (frozen p_e, pressure term fixed) = "
      f"{dJ_booking:+.1f} N ({100*dJ_booking/J0:+.3f}% of J)")
print(f"Delta J actual  (mass-conserving pair)            = "
      f"{dJ_actual:+.1f} N ({100*dJ_actual/J0:+.3f}% of J)")
assert abs(p_e1 - p_e0) / p_e0 > 1e-3, "p_e did NOT move?"
print("=> p_e MOVES when Gamma is turned on at fixed (h0,s,mdot,A_e):")
print("   H2.2 (fixed exit static pressure) + fiber-fixed mdot is")
print("   over-determined for actual solution pairs; the pressure-thrust")
print("   term is NOT fixed by the interface P trace, and the actual")
print("   within-fiber Delta J differs from the frozen-p_e booking.")

print()
print("=" * 72)
print("PART C - R22F-L0-6: DROP-convention branch sign reversal")
print("=" * 72)
# [T-DISC-1] admits the family under the DROP convention "verbatim":
# booked h0_b = h + (u^2+v^2)/2 is FIXED while u_theta = lam*Gam0/r_int
# is added => TRUE h0_t(lam) = h0_b + lam^2*Gam0^2/(2 r_int^2).
# Per-streamline exit algebra at frozen (p_e, s, v_e):
#   u_e^2(lam) = u_e^2(0) + lam^2*Gam0^2*(1/r_int^2 - 1/r_e^2).
# => strictly INCREASING in lam^2 when r_e > r_int; identically ZERO
# variation at r_e = r_int. [T-DISC-2](i)'s strict decrease fails on
# this branch of the very family [T-DISC-1] constructs.
r_int = 0.10
Gam0 = 40.0
u_e0_sq = 2.0 * cp * (T0 - T_e0)  # base axial KE at frozen p_e (v_e=0)
for r_exit in (0.15, 0.10, 0.08):
    lam = np.linspace(0.0, 1.0, 5)
    due2 = lam**2 * Gam0**2 * (1.0 / r_int**2 - 1.0 / r_exit**2)
    trend = ("INCREASING" if due2[-1] > 0
             else ("ZERO" if due2[-1] == 0 else "decreasing"))
    print(f"r_e/r_int = {r_exit/r_int:.2f}: Delta(u_e^2) at lam=1 = "
          f"{due2[-1]:+.1f} m^2/s^2  -> momentum thrust {trend}")
assert Gam0**2 * (1/r_int**2 - 1/0.15**2) > 0
assert Gam0**2 * (1/r_int**2 - 1/0.10**2) == 0
print("=> under DROP booking, the sign of the within-fiber momentum-")
print("   thrust variation is GEOMETRY-SIGNED (reverses for r_e > r_int,")
print("   vanishes at r_e = r_int): [T-DISC-2](i) strict decrease and")
print("   [T-DISC-4](a) 'single-signedly' hold only on fixed-TRUE-h0")
print("   comparisons (FOLD/compensated variant, H1.3).")
print()
print("ALL PROBE PARTS RAN; every assert passed.")

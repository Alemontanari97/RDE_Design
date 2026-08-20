"""R22F-L2 probe (round 1, lens L2): epsilon-orders of the 2-epsilon
transfer as instantiated in [T-DISC-3].

TARGET: phaseD_r22f_centerpiece.md sec. 1.3:
  "if a designer optimizes ANY functional that factors through pi ...
   the resulting design is up to 2*eps_fib suboptimal for the true J"
with eps_fib(P) := sup over the fiber of |J(s) - J(s')| (fiber DIAMETER).

RECORD FORM of claim 10 (swirl5f_FINAL_report.md:450-452): premise is
  sup_A |J_exact - J_avg| <= eps        (the GIVEN surrogate's sup-error)
=> any J_avg-maximizer is <= 2*eps-suboptimal; two-point weakening
(eps_1 + eps_2 + eta) proven.

ATTACK: substituting eps := fiber diameter while quantifying over ANY
pi-factoring surrogate is a mis-assembly. Counterexample: a pi-factoring
surrogate with the WRONG inter-fiber ranking incurs suboptimality set by
the inter-fiber J-range, not by fiber diameters.

Pinned env only (pure python). Exit code 0 = counterexample stands.
"""

# Discrete admissible class: two fibers (pressure traces P1, P2).
# J values chosen so fiber diameters are SMALL vs the inter-fiber range.
J = {("P1", "a"): 0.00, ("P1", "b"): 0.10,   # fiber P1: diameter 0.10
     ("P2", "a"): 1.00, ("P2", "b"): 1.05}   # fiber P2: diameter 0.05
fibers = {"P1": ["a", "b"], "P2": ["a", "b"]}

eps_fib = {P: max(J[(P, s)] for s in ss) - min(J[(P, s)] for s in ss)
           for P, ss in fibers.items()}
sup_eps_fib = max(eps_fib.values())          # 0.10
bound_printed = 2.0 * sup_eps_fib            # 0.20 (most generous reading)
J_opt = max(J.values())                      # 1.05

# Adversarial pi-factoring surrogate (a legitimate p-only metric with the
# wrong inter-fiber ranking): G(P1) = 1, G(P2) = 0.
G = {"P1": 1.0, "P2": 0.0}
P_star = max(G, key=G.get)                   # designer picks fiber P1
worst_realized = min(J[(P_star, s)] for s in fibers[P_star])   # 0.00
subopt = J_opt - worst_realized              # 1.05
assert subopt > bound_printed, (subopt, bound_printed)
print("counterexample: pi-factoring surrogate G with wrong ranking -> "
      "suboptimality %.2f  >  2*sup eps_fib = %.2f : the printed 'ANY "
      "functional ... up to 2*eps_fib suboptimal' is FALSE as an upper "
      "bound." % (subopt, bound_printed))

# Claim 10 itself is fine when eps is the surrogate's OWN sup-error:
eps_G = max(abs(J[(P, s)] - G[P]) for P, ss in fibers.items() for s in ss)
assert subopt <= 2.0 * eps_G                 # 1.05 <= 2*1.05: holds
print("record lemma intact with eps = sup|J - G o pi| = %.2f "
      "(2*eps_G = %.2f >= %.2f)." % (eps_G, 2.0 * eps_G, subopt))

# Correct assembly of the irreducibility statement: the BEST pi-factoring
# surrogate is the fiber midrange; its sup-error = half the max diameter.
G_best = {P: 0.5 * (max(J[(P, s)] for s in ss) + min(J[(P, s)] for s in ss))
          for P, ss in fibers.items()}
eps_best = max(abs(J[(P, s)] - G_best[P]) for P, ss in fibers.items()
               for s in ss)
assert abs(eps_best - 0.5 * sup_eps_fib) < 1e-15
P_star = max(G_best, key=G_best.get)         # picks P2 (right fiber)
worst_realized = min(J[(P_star, s)] for s in fibers[P_star])   # 1.00
subopt_best = J_opt - worst_realized         # 0.05
assert subopt_best <= 2.0 * eps_best         # 0.05 <= 0.10: holds
print("best pi-factoring surrogate: eps_G* = sup eps_fib / 2 = %.3f; "
      "realized suboptimality %.3f <= 2*eps_G* = %.3f." %
      (eps_best, subopt_best, 2.0 * eps_best))

print("\nPROBE VERDICT: [T-DISC-3] must bind eps to the SURROGATE'S sup-"
      "error (claim-10 verbatim; per-surrogate), and state irreducibility "
      "via the best-surrogate floor eps_G* = sup_P eps_fib/2 (or the "
      "record's two-point eps_1+eps_2 form) -- not '2*eps_fib for ANY "
      "functional'. REPAIR: reassemble the schema.")

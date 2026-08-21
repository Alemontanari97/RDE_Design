#!/usr/bin/env python3
"""[ESCALATED REFUTER probe, minor (a) NTF, escalation round 2 - 2026-08-20]

Target: revised phaseD_minor_ntf.md par.4 [ESC-r2-1], the H5-conditioned
DETERMINISTIC-ENVELOPE regime claim:

    "DETERMINISTIC-ENVELOPE regime, kappa_eff(cell) >= (1+m)*NTF: UNDER
     H5 (whose lower edge gives realized step >= floor_z/(1+m) >= T(z)
     in this regime), metric-termination is unreachable at that cell -
     the loop exhausts N_NEWTON = 30 trips ... AND the cell then fails
     certification."

SCENE E (boundary counterexample): the regime is defined with >= and
H5's band [floor_z/(1+m), floor_z] is CLOSED. At the included boundary
point kappa_eff = (1+m)*NTF exactly, the band's lower edge equals T(z):
H5 admits the adversarial realization step == floor_z/(1+m) == T at
every trip. The engine's semantics (verified at source this window):
  - loop EXITS at step <= T (a1_ideal_march_jax.py :444-448: continue
    while step > NTF*EPS*sc) -> step = T TERMINATES at trip 1;
  - cert PASS iff ratio = step/T <= 1 (:813) -> ratio = 1.0 PASSES.
So at the boundary BOTH conjuncts of the conditioned bullet fail under
an H5-admissible realization. This is NOT measure-zero hand-waving: H5
is a deterministic band hypothesis (no distribution), so the adversary
may sit AT the edge - the same adversarial-realization game scene A of
record already plays (noise exactly at the floor edge).

SCENE F (verifies the one-character repair): with the regime scoped
STRICT, kappa_eff > (1+m)*NTF, the worst H5-admissible realization is
the band's lower edge floor_z/(1+m) > T strictly: no trip can satisfy
step <= T (cap exhausted) and every cert sample gives ratio > 1 (FAIL).
Checked against the worst case deterministically, so it holds for ALL
H5-admissible realizations. Near-threshold band correspondingly becomes
NTF < kappa_eff <= (1+m)*NTF (boundary point moves to the fluctuation
band, where the model claims nothing deterministic - consistent).

Run:  python esc_probe_ntf_r2_boundary_strictness.py
Exit 0 iff scene E's boundary counterexample stands AND scene F's
strict-scoped claim holds. Pinned-env deps only (stdlib).
"""
import sys

fails = []


def check(name, cond):
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
    if not cond:
        fails.append(name)


N_CELLS, CAP = 200, 30
M = 0.25          # declared fluctuation margin (H5)
T = 1.0e-10       # threshold, emulation scale (as scenes A-D of record)


def march_population(floor, realization):
    """Deterministic adversarial march: per-trip step = realization
    (an H5-admissible value in [floor/(1+M), floor]).
    Engine semantics of record: exit at step <= T; cert PASS iff
    step/T <= 1."""
    term = cert_pass = 0
    trips_at_term = None
    for _ in range(N_CELLS):
        terminated = False
        for k in range(1, CAP + 1):
            step = realization
            if step <= T:            # a1 :444-448 exit condition
                terminated = True
                trips_at_term = k
                break
        if terminated:
            term += 1
        if realization / T <= 1.0:   # a1 :813 cert ratio semantics
            cert_pass += 1
    return term, trips_at_term, cert_pass


print("== SCENE E: included boundary point kappa_eff = (1+m)*NTF ==")
floor_e = (1.0 + M) * T              # kappa_eff = (1+m)*NTF exactly
edge_e = floor_e / (1.0 + M)         # H5 lower edge = T exactly
check("boundary is IN the declared regime (>=): kappa/NTF = 1.25 >= 1.25",
      floor_e / T >= 1.0 + M)
check("adversarial realization is H5-admissible: edge in [floor/(1+m), floor]",
      floor_e / (1.0 + M) <= edge_e <= floor_e)
term_e, trips_e, pass_e = march_population(floor_e, edge_e)
print("  metric terminations: %d/%d at trip %s (claim predicts 0, cap %d)"
      % (term_e, N_CELLS, trips_e, CAP))
print("  cert PASS cells: %d/%d (claim predicts 0)" % (pass_e, N_CELLS))
check("'termination unreachable' FALSE at boundary: all cells exit trip 1",
      term_e == N_CELLS and trips_e == 1)
check("'AND then fails certification' FALSE at boundary: all cells PASS "
      "(ratio = 1.0 <= 1)", pass_e == N_CELLS)

print("== SCENE F: strict scoping kappa_eff > (1+m)*NTF (the repair) ==")
floor_f = (1.0 + M) * T * (1.0 + 1e-9)   # any strict margin
edge_f = floor_f / (1.0 + M)             # worst H5-admissible realization
check("regime strict: kappa/NTF > 1+m", floor_f / T > 1.0 + M)
check("worst-case (band lower edge) step exceeds T strictly", edge_f > T)
term_f, _, pass_f = march_population(floor_f, edge_f)
print("  metric terminations: %d/%d (cap exhausted); cert PASS: %d/%d"
      % (term_f, N_CELLS, pass_f, N_CELLS))
check("strict-scoped claim HOLDS: 0 terminations (cap exhausted)",
      term_f == 0)
check("strict-scoped claim HOLDS: 0 cert PASSes (population FAIL)",
      pass_f == 0)

print()
if fails:
    print("PROBE VERDICT: %d FAILURE(S): %s" % (len(fails), fails))
    sys.exit(1)
print("PROBE VERDICT: SCENE E BOUNDARY COUNTEREXAMPLE STANDS + SCENE F "
      "CONFIRMS THE STRICT-INEQUALITY REPAIR")
sys.exit(0)

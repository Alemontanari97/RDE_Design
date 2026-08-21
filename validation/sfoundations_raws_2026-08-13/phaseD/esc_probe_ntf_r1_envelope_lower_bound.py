#!/usr/bin/env python3
"""[ESCALATED REFUTER probe, minor (a) NTF, escalation round 1 — 2026-08-20]

Target: revised phaseD_minor_ntf.md par.4 [ESC-r1-3], the repaired NTF-4
DETERMINISTIC-ENVELOPE regime claim:

    "DETERMINISTIC-ENVELOPE regime, kappa_eff(cell) >= (1+m)*NTF:
     metric-termination is unreachable at that cell — the loop exhausts
     N_NEWTON = 30 trips ... AND the cell then fails certification."

SCENE C (counterexample to the repair as printed): H1-H4 bound the
evaluation noise from ABOVE only (H3 is an envelope — the revision says
so itself in the near-threshold text). Using the SAME H3-consistent
per-trip sampling class as the sustained refuter scene B
(uniform(0, floor)), set kappa_eff = 2*NTF — deep inside the declared
deterministic-envelope regime at m = 0.25 (2 >= 1.25). The scoped claim
predicts 0/N metric terminations (all cells exhaust the 30-trip cap)
and N/N certification FAILs. The model instance delivers ~N/N
terminations in a few trips and ~N/2 certification PASSes — BOTH
conjuncts fail. So the repair moved the boundary of MIN-NTF-3's defect
(envelope != per-realization) without removing it: the scoped claim is
still not an implication of H1-H4 for ANY m; it needs the
band-limited-fluctuation hypothesis stated EXPLICITLY.

SCENE D (verifies the named one-sentence repair): under the explicit
hypothesis "per-trip realized step within [floor/(1+m), floor]"
(realized/envelope in [1/(1+m), 1], the property the declared margin
m = 0.25 implicitly encodes), the deterministic-envelope claim HOLDS at
kappa_eff = 2*NTF: min step = floor/1.25 = 1.6*T > T, so 0/N
terminations (cap exhausted) and N/N cert FAILs. One explicit
hypothesis sentence repairs the claim; the re-pinned falsifier
(steps consistently below T*(1-band)) already measures exactly this.

Run:  python esc_probe_ntf_r1_envelope_lower_bound.py
Exit 0 iff scene C's counterexample stands AND scene D confirms the
repaired (explicitly conditioned) claim. Pinned-env deps only (numpy).
"""
import numpy as np

rng = np.random.default_rng(20260820)

N_CELLS, CAP = 200, 30
FLOOR = 1.0e-10
M_MARGIN = 0.25          # the revision's declared fluctuation margin


def run_population(T, low_frac):
    """March a population: per-trip realized step ~ floor*U(low_frac, 1)
    (low_frac = 0 reproduces the sustained scene-B sampling class).
    Returns (metric_terminations, max_trips_at_termination, cert_pass)."""
    term, cert_pass, trips_max = 0, 0, 0
    for _ in range(N_CELLS):
        terminated, trips = False, CAP
        for k in range(1, CAP + 1):
            step = FLOOR * rng.uniform(low_frac, 1.0)
            if step <= T:
                terminated, trips = True, k
                break
        if terminated:
            term += 1
            trips_max = max(trips_max, trips)
        cert_step = FLOOR * rng.uniform(low_frac, 1.0)
        if cert_step / T <= 1.0:
            cert_pass += 1
    return term, trips_max, cert_pass


fails = []


def check(name, cond):
    print("  [%s] %s" % ("PASS" if cond else "FAIL", name))
    if not cond:
        fails.append(name)


print("== SCENE C: deterministic-envelope claim vs H3-consistent "
      "wide fluctuation ==")
T_C = 0.5 * FLOOR        # kappa_eff = 2*NTF >= (1+m)*NTF = 1.25*NTF
term_c, tmax_c, pass_c = run_population(T_C, 0.0)
print("  kappa_eff/NTF = %.2f (>= 1+m = %.2f: DETERMINISTIC regime "
      "per [ESC-r1-3])" % (FLOOR / T_C, 1.0 + M_MARGIN))
print("  metric terminations: %d/%d (claim predicts 0), max trips at "
      "termination = %d (cap %d)" % (term_c, N_CELLS, tmax_c, CAP))
print("  cert PASS cells: %d/%d (claim predicts 0)"
      % (pass_c, N_CELLS))
check("regime is deterministic-envelope: kappa/NTF = 2.0 >= 1.25",
      FLOOR / T_C >= 1.0 + M_MARGIN)
check("'termination unreachable' FALSE: terminations reached "
      "(expected ~all; P(none per cell) = 2^-30)", term_c == N_CELLS)
check("terminations are early (max trips < cap)", tmax_c < CAP)
check("'AND then fails certification' FALSE: cert PASS cells > 0 "
      "(expected ~N/2)", pass_c > 0)
check("scene C stays H3-consistent: sampled steps <= floor by "
      "construction (uniform(0, floor))", True)

print("== SCENE D: same regime under the EXPLICIT band hypothesis "
      "(the named repair) ==")
low = 1.0 / (1.0 + M_MARGIN)   # realized/envelope in [1/(1+m), 1]
term_d, tmax_d, pass_d = run_population(T_C, low)
print("  band hypothesis: realized step in [floor/(1+m), floor], "
      "min step = %.2f*T > T" % (low * FLOOR / T_C))
print("  metric terminations: %d/%d; cert PASS cells: %d/%d"
      % (term_d, N_CELLS, pass_d, N_CELLS))
check("min realized step exceeds T: floor/(1+m) = 1.6*T > T",
      low * FLOOR > T_C)
check("claim HOLDS under the explicit hypothesis: 0 terminations "
      "(cap exhausted at every cell)", term_d == 0)
check("claim HOLDS under the explicit hypothesis: 0 cert PASSes "
      "(population FAIL forced)", pass_d == 0)

print()
if fails:
    print("PROBE VERDICT: %d FAILURE(S): %s" % (len(fails), fails))
    raise SystemExit(1)
print("PROBE VERDICT: SCENE C COUNTEREXAMPLE STANDS + SCENE D CONFIRMS "
      "THE EXPLICIT-HYPOTHESIS REPAIR")
raise SystemExit(0)

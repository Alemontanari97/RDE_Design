#!/usr/bin/env python3
"""[REFUTER probe, minor (a) NTF — S-FOUNDATIONS-C4 Blocco 1 v2]
Executable counterexamples for refute_minor_ntf.md findings
MIN-NTF-1 (scene A) and MIN-NTF-3 (scene B).

Both scenes INSTANTIATE the author's own model (phaseD_minor_ntf.md
NTF-1 hypotheses H1-H4): the evaluation-noise envelope is INJECTED at
a declared emulation scale (T = 1e-10 >> true float64 roundoff, so
IEEE noise is negligible against the injected model noise). This is
licit because the attacked statements (NTF-2 composition constant,
NTF-4 termination coupling) are claimed AS CONSEQUENCES OF that model:
a model instance that violates them is a counterexample to the
claimed implication, independent of IEEE specifics.

SCENE A (MIN-NTF-1): the NTF-2 PASS bound  error <= 2*T  with the
"floor term absorbed" parenthetical is FALSE as stated: noise bounded
by the floor can CANCEL part of the exact Newton correction, so a
PASS only yields  ||dz_exact|| <= T + floor,  hence
error <= 2*(T + floor) <= 2*T*(1 + 1/eta) under the author's own LB.
We build a 1D Newton instance, contraction ratio Theta <= 1/2 (H2
checked numerically), noise within the declared floor = 0.8*T
(eta = 1.25, the lower edge of the author's declared bracket), where
the certificate PASSes (ratio 0.99) while the TRUE error is ~3.4*T
> 2*T. The amended bound 2*(T+floor) = 3.6*T holds.

SCENE B (MIN-NTF-3): NTF-4 claims: if NTF < kappa_eff(cell), then
"metric-termination is unreachable at that cell: the loop always
exhausts N_NEWTON = 30 trips AND the cell then fails certification."
kappa_eff is an ENVELOPE constant (H3 bounds ||delta||, it does not
pin each sample). In the near-threshold regime (T a few % below the
envelope floor — exactly the ntf50 arm's 51.7-vs-50 regime), per-trip
noise fluctuation lets the step dip below T at some trip: the loop
terminates ON THE METRIC in a few trips, and the (fresh-sample)
certification step still exceeds T at some cells => FAIL. Termination
+ FAIL coexist; "always exhausts 30 trips" is refuted INSIDE the
model. Consequence: the pinned falsifier of NTF-4 ("trip-count
instrumentation showing metric-termination still reached at the
failing cells ... would refute the same-threshold coupling claim")
can fire on data fully CONSISTENT with the floor model — the
falsifier is over-broad, not just the claim over-strong.

Run:  python r22f_v2_probe_minor_ntf_pass_bound_and_termination.py
Exit 0 iff both scenes reproduce (i.e. the counterexamples stand).
"""
import numpy as np

rng = np.random.default_rng(20260820)


def scene_a():
    print("== SCENE A (MIN-NTF-1): PASS with true error > 2*T ==")
    # Emulation scales (declared): sc = 1 (unit scale), NTF = 100.
    T = 1.0e-10          # = NTF*EPS_emul*sc, the certificate threshold
    eta = 1.25           # author's declared bracket lower edge
    floor = T / eta      # = 0.8*T: LB "NTF >= eta*kappa_eff" holds
    # 1D residual f(z) = a*(z-r) + b*(z-r)^2, root r = 0.
    # Choose the iterate so the EXACT extra Newton step has
    # |dz_exact| = 1.79*T (<= T + floor = 1.8*T, the forceable-PASS
    # edge) with error/|dz_exact| -> 1.9 (t = b*e0/a = 9).
    a, t = 1.0, 9.0
    dz_mag = 1.79 * T                    # target |dz_exact|
    e0 = dz_mag * (1.0 + 2.0 * t) / (1.0 + t)   # since |dz| = e0(1+t)/(1+2t)
    b = t * a / e0
    z_hat, r = e0, 0.0                   # iterate; true root at 0

    def f(z):
        return a * (z - r) + b * (z - r) ** 2

    def fp(z):
        return a + 2.0 * b * (z - r)

    dz_exact = -f(z_hat) / fp(z_hat)
    err_true = abs(z_hat - r)
    # H2 check: contraction ratio Theta = |dz(z1)|/|dz(z0)| <= 1/2
    z1 = z_hat + dz_exact
    theta = abs(-f(z1) / fp(z1)) / abs(dz_exact)
    # Adversarial-but-bounded evaluation noise (H3: |delta| <= floor
    # in step units): delta chosen to CANCEL part of the exact step.
    noise_step = -np.sign(dz_exact) * (-floor)   # opposes dz_exact
    dz_hat = dz_exact + np.sign(dz_exact) * (-floor)
    ratio = abs(dz_hat) / T                       # certificate ratio
    print("  |dz_exact|/T = %.4f  err_true/T = %.4f  Theta = %.4f"
          % (abs(dz_exact) / T, err_true / T, theta))
    print("  injected |noise|/floor = %.3f (<= 1: H3 respected)"
          % (abs(noise_step) / floor))
    print("  certificate ratio = %.4f  -> %s"
          % (ratio, "PASS" if ratio <= 1.0 else "FAIL"))
    claimed = 2.0 * T                 # author's NTF-2 bound as stated
    amended = 2.0 * (T + floor)       # repaired constant
    print("  claimed bound 2*T:        err_true <= 2*T ?   %s "
          "(err/2T = %.3f)" % (err_true <= claimed, err_true / claimed))
    print("  amended bound 2*(T+floor): err_true <= ?      %s "
          "(err/bound = %.3f)" % (err_true <= amended, err_true / amended))
    ok = (theta <= 0.5) and (abs(noise_step) <= floor) \
        and (ratio <= 1.0) and (err_true > claimed) \
        and (err_true <= amended)
    print("  SCENE A COUNTEREXAMPLE %s" % ("STANDS" if ok else "FAILED"))
    return ok


def scene_b():
    print("== SCENE B (MIN-NTF-3): metric-termination reached AND "
          "cert FAIL, NTF < kappa_eff ==")
    # Envelope floor and threshold: T 3% below the envelope
    # (ntf50-arm regime: T = 50, kappa_eff envelope ~51.7).
    floor = 1.0e-10
    T = 0.97 * floor          # NTF < kappa_eff (envelope) at EVERY cell
    n_cells, cap = 200, 30
    trips_used, term_on_metric, cert_fail = [], 0, 0
    for _ in range(n_cells):
        trips = cap
        for k in range(1, cap + 1):
            step = floor * rng.uniform(0.0, 1.0)  # H3-consistent sample
            if step <= T:
                trips = k
                break
        if trips < cap or step <= T:
            term_on_metric += 1
        trips_used.append(trips)
        cert_step = floor * rng.uniform(0.0, 1.0)  # fresh cert sample
        if cert_step / T > 1.0:
            cert_fail += 1
    trips_used = np.array(trips_used)
    print("  cells: %d  T/floor = %.2f  (NTF < kappa_eff everywhere)"
          % (n_cells, T / floor))
    print("  metric-termination reached: %d/%d cells  "
          "(max trips = %d, cap = %d)"
          % (term_on_metric, n_cells, trips_used.max(), cap))
    print("  certification FAIL cells: %d/%d  (population verdict: %s)"
          % (cert_fail, n_cells, "FAIL" if cert_fail else "PASS"))
    # Counterexample stands iff essentially all cells terminate on the
    # metric well before the cap AND the population cert still FAILs.
    ok = (term_on_metric == n_cells) and (trips_used.max() < cap) \
        and (cert_fail > 0)
    print("  => NTF-4's 'always exhausts %d trips' conjunction is %s "
          "in this model instance" % (cap, "FALSE" if ok else "not refuted"))
    print("  SCENE B COUNTEREXAMPLE %s" % ("STANDS" if ok else "FAILED"))
    return ok


if __name__ == "__main__":
    a = scene_a()
    b = scene_b()
    print("PROBE VERDICT: %s" % ("BOTH SCENES STAND" if (a and b)
                                 else "AT LEAST ONE SCENE FAILED"))
    raise SystemExit(0 if (a and b) else 1)

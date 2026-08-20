"""R22F-L2-14 probe (round 2, lens L2): the (vi) BEST cell clause
"on-ray, in-class, with the (J)/(H) gradient channels at their BEST
value-level readings, the shift is plausibly within the in-class
design-delta scale [SE]" -- rate analysis of what value-level readings
can and cannot buy for the argmax shift.

TWO facts, both demonstrated numerically (mu-strongly-concave J_true,
mu = 1, argmax at 0; J_red = J_true + perturbation with uniform value
gap <= a):

(A) SOUND CONTENT THE DRAFT NEVER STATES: under a uniform value-error
    premise (U-type) and curvature floor mu on the basin, the shift IS
    bounded -- but at the SQUARE-ROOT rate: |shift| <= 2*sqrt(a/mu)
    (proof: (mu/2)*shift^2 <= J_true(S*_t) - J_true(S*_r) <= 2a).
    This value-level a-posteriori shift bound is derivable NOW from
    measured mu + M-RED's measured eps; Sec 2.2-bis / the (vi) cell do
    not state it.

(B) THE RATE IS TIGHT, so the [SE] inference "value channels single-
    digit-% => shift plausibly within the in-class design-delta scale"
    does NOT follow: a perturbation of uniform size a moves the argmax
    by Theta(sqrt(a)) -- e.g. a = 1% of the J scale admits a shift of
    ~0.19 design units at mu = 1, two orders above a. sqrt(few %) is
    NOT "in-class delta" scale without further premises.

numpy only; all numbers synthetic (CT-6 respected).
"""
import numpy as np

mu = 1.0
S = np.linspace(-2.0, 2.0, 2_000_001)
J_true = -0.5 * mu * S**2                      # argmax 0, curvature mu

print("fact (A): shift <= 2*sqrt(a/mu) holds on adversarial families")
print("fact (B): shift = Theta(sqrt(a)) attained (value gap = a)")
for a in [1e-1, 1e-2, 1e-3, 1e-4]:
    # adversarial in-gap perturbation: smooth +-a step placed just
    # inside the sqrt(a) window (c = 1.9*sqrt(a) < 2*sqrt(a)):
    c = 1.9 * np.sqrt(a / mu)
    w = 0.01 * c
    J_red = J_true + a * np.tanh((S - c * 0.5) / w)
    value_gap = np.max(np.abs(J_red - J_true))
    S_star_red = S[np.argmax(J_red)]
    shift = abs(S_star_red)
    bound = 2.0 * np.sqrt(value_gap / mu)
    print(f"  a={a:8.1e}  value_gap={value_gap:.3e}  "
          f"|shift|={shift:.4f}  2*sqrt(a/mu)={bound:.4f}  "
          f"shift/value_gap={shift/value_gap:9.1f}")
    assert value_gap <= a + 1e-12
    assert shift <= bound + 1e-6          # (A) the sqrt bound HOLDS
    assert shift >= 0.9 * np.sqrt(a / mu) # (B) sqrt rate ATTAINED
    # the shift is NOT at the value-gap scale (the [SE] inference):
    assert shift > 10 * value_gap or a >= 1e-1

# (A) formal check on random smooth perturbation families as well:
rng = np.random.default_rng(3)
for _ in range(50):
    a = 10.0 ** rng.uniform(-4, -1)
    k = rng.uniform(0.5, 50.0)
    phs = rng.uniform(0, 2 * np.pi)
    J_red = J_true + a * np.sin(k * S + phs)
    shift = abs(S[np.argmax(J_red)])
    assert shift <= 2.0 * np.sqrt(a / mu) + 1e-6

print("ALL ASSERTS PASS: value-level smallness bounds the shift only at")
print("the sqrt rate 2*sqrt(eps/mu) (never stated in the draft), and that")
print("rate is tight -- 'plausibly within the in-class design-delta scale'")
print("does not follow from single-digit-% value readings as printed.")

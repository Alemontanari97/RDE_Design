# Stage-B item XC — "The blowdown measure of the class-A family is log-uniform in pressure" — ADVOCATE position (round 0)

## Question
Is the operating measure mu of the class-A family (exponential blowdown between wave passages) correctly represented as log-uniform in chamber pressure, dmu = dPc/(Pc ln PR), so that every cycle-weighted quantity of the design loop is a Lebesgue integral against that measure, and does the design loop need any other weighting?

## Proposed falsifier (for agreement)
A measured or generated cycle whose pushforward of normalized time onto pressure deviates from the log-uniform law beyond derived drift bars (W1 or KS distance in ln Pc between the empirical and the log-uniform pushforward, threshold derived from the sensitivity bar |dJ| <= Lip(F)·W1) WHILE the exponential blowdown hypothesis still holds falsifies the claim; a deviation caused by a non-exponential blowdown falsifies the hypothesis, not the law.

## Position
1. Under exponential blowdown Pc(t) = P_CJ exp(−λt), λ = ln(PR)/t_c, the normalized time ξ = t/t_c maps to ln Pc affinely: ξ = (ln P_CJ − ln Pc)/ln PR. The pushforward of the uniform measure in ξ is therefore uniform in ln Pc, i.e. dmu = dPc/(Pc ln PR) — a two-line derivation, THEOREM-level within the blowdown model (the record's claims row scope "canonical operating measure under exponential blowdown", claims registry :241-248).
2. The theory downstream is measure-agnostic beyond this instance: the averaged functional and its stationarity conditions hold for any probability measure with the declared mu-hypotheses (probability; mu-a.e. audits; switch-null phases), so the law is a canonical INSTANCE, not an assumption the theorems need.
3. Consequence for the design loop: cycle-weighted quadrature nodes are placed in ln Pc (uniform), never in Pc or t; a designer who samples uniformly in time is already sampling this law; a designer who samples uniformly in pressure over-weights the low-pressure tail by the factor Pc — a bias of order ln PR (~3.9 at PR = 49) on the weight ratio between peak and end of cycle.
4. Cost: none (the law is in place); credibility of the decisive comparison: the same mu, content-hashed, must feed both arms (protocol rejector R-TWIN-3).

## Anchors
docs/claims_registry.yaml :241-248 (canonical operating measure, falsifier = W1/KS drift vs derived bars, carrier = mu-instruments bundle); src/thrust/stechmann_nozzle.py (Step 2: blowdown Pc(t) = PR·Pinit·exp(−λt), λ = ln(PR)/tc, Eqs. 13-14); M0 D-MU :95-110; TWIN protocol §3 (mu log-uniform) and §7 R-TWIN-3.

## What would make me abandon it
The falsifier above firing on class-A generated data with the blowdown hypothesis intact, or a demonstration that the design-loop quadrature is not invariant under the affine map ξ ↦ ln Pc.

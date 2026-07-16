# P3 — Measurable averaged multipliers for the T7 system
# (lambda2 in L^infinity(dmu): statement, proof in the S1 shock-free
# class, declared residue)

Status: RIGOR ATTACK OF RECORD (2026-07-16, rigor session, [F1/P3]).
Target: the named gap P3 of D3 §9 / M0 T7 ("lambda2 in L^2(dmu):
measurable selection + phase-wise constraint qualification — open, no
obstruction known"). Result here: UPGRADE to THEOREM* in the
shock-free S1 class (with the residue named precisely); the general
case stays SCHEMA with the abstract route stated. Gamma status:
EOS-general throughout (the proof uses only the Lemma-A closed form,
itself EOS-general, and measure theory).

------------------------------------------------------------------------------
## 1. Statement

Setting (M0 D2.6 + T7): interface contract (Gamma_d, D, mu) with R3
(measurability of xi -> s(xi)); per-phase state U_xi = the unique S1
solution with data s(xi); per-phase mass-flow constraint
m[Sigma; s(xi)] = mdot(xi); uniform S1 margin delta_S1 > 0 and uniform
supersonicity M(xi, .) >= M_min > 1 on the terminal characteristics
(both part of the D2.6 admission audits).

THEOREM P3-S1 (averaged multiplier regularity, shock-free S1 class;
class THEOREM* — conditional exactly on the declared P7 continuity
hypothesis, see step (iii) and §3). Under the above, for mu-a.e. xi
the per-phase mass multiplier lambda2(xi) exists, is UNIQUE, satisfies
the closed form
    (P3.1)   lambda2(xi) = - f2(xi) = - W_E(xi) cos(theta_E(xi) -/+
             alpha_E(xi)) / cos(alpha_E(xi))
(lip values of phase xi; sign by characteristic family, Lemma A
(L.12)), and the map xi -> lambda2(xi) is mu-measurable and ESSENTIALLY
BOUNDED:
    (P3.2)   lambda2 in L^infinity(dmu) subset L^2(dmu)
(mu a probability measure). In particular the averaged stationarity
system T7(a)-(c) admits its multiplier function in L^2(dmu), closing
gap P3 in this class.

------------------------------------------------------------------------------
## 2. Proof

(i) EXISTENCE + UNIQUENESS per phase (constraint qualification).
Fix xi. In the control-surface formulation the phase-xi mass
constraint is the scalar functional m(.) on the trace data of the
terminal characteristic. The Zowe-Kurcyusz (Robinson) constraint
qualification for a scalar equality constraint reduces to
NON-VANISHING of its derivative at the solution in an admissible
direction. This is supplied by the Prop. A2 computation (docs/
rde_nozzle_P2_lemmaA.md, machine-verified): the contraction of
grad m with the NON-tangent acoustic eigenvector is
    < grad_V m, r+ > = rho (u_n + c) >= rho_min (c_min)(1 + 1) > 0
on the terminal characteristic (u_n = c there), uniformly under the
margin hypotheses. A scalar constraint with nonvanishing derivative
is a submersion: the multiplier exists and is UNIQUE (standard
Lagrange duality for submersed scalar constraints; Zowe-Kurcyusz
gives the Banach-space version). QED (i).

(ii) CLOSED FORM. With existence granted, the multiplier must satisfy
the stationarity system of the phase, whose unique solution for
lambda2 is Rao's first integral: lambda2(xi) = -f2(xi) — this is
exactly Lemma A step 5 ((L.12), derived, corpus-checked,
machine-verified; EOS-general). QED (ii).

(iii) MEASURABILITY. xi -> s(xi) is measurable (contract R3). The map
s -> (W_E, theta_E, alpha_E) (data to lip trace values through the
S1 solution and the lip location) is CONTINUOUS on the admissible
data set: this is the declared P7 continuity hypothesis of record —
in the SHOCK-FREE S1 subclass it follows from classical semiglobal
well-posedness (continuous dependence in the Li Ta-tsien framework,
already the basis of D2.5 canonicity there). The composition
measurable-then-continuous is measurable; (P3.1) is a continuous
function of the lip values wherever cos(alpha_E) > 0. QED (iii).

(iv) UNIFORM BOUND. Under uniform supersonicity 1 < M_min <= M_E(xi)
<= M_max (compact cycle + margins): alpha_E in [arcsin(1/M_max),
arcsin(1/M_min)] with arcsin(1/M_min) < pi/2, so cos(alpha_E) >=
cos(arcsin(1/M_min)) = sqrt(1 - 1/M_min^2) > 0; W_E bounded by the
energy bound (W <= W_max = sqrt(2 h0_max)); |cos(theta -/+ alpha)|
<= 1. Hence |lambda2(xi)| <= W_max / sqrt(1 - 1/M_min^2) uniformly:
lambda2 in L^infinity(dmu). QED (iv), and the theorem.

------------------------------------------------------------------------------
## 3. What is NOT proven here (declared residue, named)

 R-P3.1 ACROSS TRANSVERSAL SHOCKS: step (iii) uses shock-free
        continuous dependence. With fitted fronts the solution map is
        still expected continuous (Majda stability), but the rigorous
        continuous-dependence statement in the S1-with-shocks class is
        part of the same declared conditional as D2.5 canonicity:
        P3-S1 inherits it. Class stays THEOREM* (conditional),
        degrading to SCHEMA if the front count changes on a
        mu-positive set (topology-switch phases are mu-null by T7's
        own hypothesis — consistent).
 R-P3.2 BEYOND CLOSED FORM (reacting gas / no f2): the abstract route
        remains the one named in D3 §9 — phase-wise Zowe-Kurcyusz
        with UNIFORM surjectivity modulus + measurable selection
        (Kuratowski–Ryll-Nardzewski on the multiplier correspondence,
        which is nonempty-closed-valued under (i)); the S1 proof
        above shows the correspondence is single-valued there, which
        is why no selection theorem was needed. SCHEMA.
 R-P3.3 The FUNCTION-SPACE adjoint existence per phase (interior
        adjoint field, not just the scalar multiplier) is Lemma-A/
        Hoffman-map territory (P-2), not P3; across shocks it meets
        G12. Unchanged.

------------------------------------------------------------------------------
## 4. Consequence for T7 and the papers

The averaged system T7(a)-(c) with (**') is now well-posed at the
multiplier level in the shock-free S1 class: the weighted
transversality integrand R(xi) w(xi) has lambda2(xi) bounded
measurable, so (**') is a genuine L^1(dmu) statement. D3 §9 P3 row
upgraded (OPEN -> THEOREM* in S1 shock-free / SCHEMA general);
M0 T7 named-gap list updated accordingly. For P-1 this removes a
referee-facing soft spot (the averaged system's multiplier function
is no longer hypothesized); for P-4 the residue R-P3.1/R-P3.2 is the
honest frontier statement.

Falsifier: exhibit an admissible cycle family (uniform margins) with
a mu-positive set of phases where the per-phase multiplier fails to
exist or (P3.1) fails; or a shock-free S1 family where
xi -> lambda2(xi) is non-measurable (would contradict (iii):
inspect the continuity hypothesis first).

# Hypothesis-minimization ledger — pass 1 + pass 2 (D9 candidate)

Status: GOVERNANCE DELIVERABLE OF RECORD (2026-08-05, S15
deep-foundations campaign, [RIGOR/B]; mandate: "for every standing
hypothesis and conditional a MANDATORY verdict — the operational
definition of a self-sustaining theory"). Registry: [PAP-D9HL].
Scope of pass 1: the 17 rows of the D1 §9 hypothesis ledger + the 7
registry conditionals (C-*). Verdicts are assigned from the EXISTING
record only (every grounds cell cites its record site); no new
mathematics is introduced here — pass 1 is an adjudication pass.

VERDICT VOCABULARY (mandated, one primary verdict per row):
 - DISCHARGED: proven or removed — no longer an assumption.
 - WEAKENED: replaced by a strictly weaker NAMED hypothesis (or
   confined to a named subset/transformed into an enforced,
   monitored object).
 - NECESSARY(counterexample): a counterexample shows the conclusion
   fails without it — cannot be dropped; the counterexample is cited
   (executable where possible).
 - PRICED: cannot yet be dropped or weakened, but violation is
   quantified/monitored through an executable channel.

PASS-1 TOTALS: 0 DISCHARGED / 6 WEAKENED / 5 NECESSARY (every one
with a cited counterexample: 2 machine-exhibited this session, 1
executable in the suite, 1 published page-verified, 1 first-order
breaker) / 13 PRICED. Zero rows unadjudicated. The absence of
outright discharges in pass 1 is honest: discharging takes proofs,
not adjudication — the pass-2 targets are named at the end.
[PASS-2 TOTALS, dated 2026-08-06 (S16, §4): on the original 24 rows
— 3 DISCHARGED (H2, H-I2 on the L4-default class; H-Pa by instance
reclassification) / 4 WEAKENED / 5 NECESSARY (unchanged) / 12
PRICED; PLUS 5 clauses minted after pass 1 adjudicated (all PRICED):
living ledger = 29 rows, zero unadjudicated.]

------------------------------------------------------------------------------
## §1 The D1 §9 rows

| ID | Verdict | Grounds (record sites) |
|---|---|---|
| H-A1 single rotating wave, n-fold, periodic | NECESSARY(cex) | Counterexample MACHINE-EXHIBITED S15: X-SLRW rejector R1 — a counter-rotating admixture makes the transverse resultant nonzero with 2-Omega-pulsating modulus (elliptical orbit), and the T0 steadification fails; docs/rde_nozzle_side_load.md §3 B1. Violation priced separately (PB-5 robust formulation; T0-flatness monitor D6 5-bis). |
| H-A2 axisymmetric wall/control surfaces | NECESSARY(cex) | Counterexample mechanism machine-exhibited: a non-axisymmetric geometric kernel reads m != 0,+-1 harmonics (X-SLRW R3: the m=2 functional of an n=2 pattern is nonzero), and any m != 0 line carries e^{-imOmega t} — time-dependent loads; T0(i) proof uses n_theta = 0 essentially (M0 Theorem 3). |
| H-F1 frozen family (s, mu, Omega_w indep. of Sigma) | PRICED | Chamber-response map with measured contraction q (D6 A6 stage-G); choked-annulus margins 0.97/0.65 documented (registry/D6 Annex B case G); PB-4 bilevel formulation stands ready if q >~ 1. |
| H2 choked feed, fixed A_t | WEAKENED -> DISCHARGED (PASS 2, S16 §4) | M0 [T-TH0] note of record: with a fully axially supersonic interface (L4) the mdot-independence holds EXACTLY without upstream choking — H2 is needed only on subsonic-patch interfaces; choking-margin monitor per row remains. [S16: L4 declared the certified interface DEFAULT (M0 D2.4 dated note); on the default H2 is not an assumption at all; it survives only as a CASE-CLASS closure assumption inside D1 §4.3bis options O2/O3, same monitors.] |
| H-I2 no mean upstream influence through Gamma_d | WEAKENED -> DISCHARGED (PASS 2, S16 §4) | On axially supersonic patches it is a THEOREM, not a hypothesis ([T-NSW]: u_x > c makes x = const spacelike in every frame — no upstream signal); the assumption survives ONLY on declared subsonic patches, where the R2 characteristic-direction audit prices it. [S16: with L4 the certified default (M0 D2.4 dated note), the default-class row is a theorem; the case-class residue keeps the R2 audit.] |
| D1 quasi-steady St -> 0 | PRICED | [T-T3QS]: second-order protection on ray families (first-order sweep correction vanishes on the smooth part, executable carrier group (xvi)); O5-lite pre-registered falsification (D6 A4: P-i/P-ii/P-iii with rejectors); J1 corrector = the A4 deliverable; (P)(v) bar carries St|J1|. |
| D2 azimuthal decoupling | PRICED | [S-BLITE]: the 3-D helical wave-frame march is the EXACT meter of the sweep/D2 residual at marching cost; (P)(v) bar carries the D2 residual; full anchor = A5. |
| D3 per-phase S1 regularity/uniqueness | WEAKENED | Uniqueness in the shock-free class is now THEOREM-SHAPED by two independent mechanisms (S15): [T-XWS] BVP-native weak-strong (mod [C-XBVP]) and [S-D25U-U1] §6 Gronwall-on-differences corollary; membership stays monitored a posteriori (boundary function, D2.5); across fronts the conditional is [C-MAJDA], cleanly separated. From bare assumption to monitored-membership + conditional theorems. [S16: shocked-class WITHIN-STRATUM uniqueness added ([S-D25U-U34] §4.3 -b corollary); C-XBVP(a) discharged at instance level (X-IVXC, S15 reopened segment).] |
| H-T3.1 one frozen gamma | NECESSARY(cex) | Executable counterexample of record: two-gamma counterexample [T-T3-CE], suite group (ix) — the collapse fails at second order with measured gamma_eff; price measured small (D3 §5.2 numbers: eps* shift -0.56%). |
| H-T3.2 full-flowing, supersonic exit | WEAKENED | TRANSFORMED (S12, [D-GSEP]): no longer assumed — ENFORCED as the per-phase state constraint g_sep <= 0 in (P) with active-set multiplier = marginal attachment value; deliberate separation exits the certified class by physics (subsonic feedback + non-rotating dynamics). The cleanest minimization move in the corpus: hypothesis -> constraint. |
| H-T3.3 phase-independent inflow shape | NECESSARY(cex) | First-order breaker: any per-phase (M, theta)(y; xi) profile variation defeats the T3 Lemma-A similarity (N3 channel, D1 §9); at I3 interfaces it holds BY CONSTRUCTION (case-A Verdict class, D6 Annex B) — the necessity is priced by interface class, not removed. |
| H-T4 ideal-adaptation closure | PRICED | Declared model closure [C-HT4] with published bound precedent (Kraiko-Egoryan); sonic cap of record (M0 Prop. 7 sharpening); PB-2 truncation/base-pressure band = the falsifier [named IOU, dated 2026-08-05 (D8 §8 two-lens): executable only under a declared base-pressure closure p_b — proposed C-N2, to be minted at PB-2/OP-2 kickoff]; N2 stays THE declared open problem. |
| H-P1 spectral non-degeneracy, transversal fronts | PRICED | Evans/Arnoldi monitor (A5 certificates); the monodromy margin is the MONITORED SURROGATE of the full condition pending [C-P4RZ]; set-valued J at mode boundaries declared (D1 §9). |
| H-mu measure known | PRICED | The cheapest full pricing in the ledger: J is LINEAR in mu, so the sensitivity report is free (|dJ| <= osc_xi(F)·TV or Lip_xi(F)·W1 — D6 item 15 mu-instruments bundle, ME-5); DRO ball (PB-5) for declared misspecification; [T-O2] fixes the nominal. |
| H-E4 per-phase Rao/corner at gamma(T) frozen | NECESSARY(cex) | PUBLISHED counterexample, page-verified (S6): finite-rate chemistry breaks the corner theory — Hoffman 1967 Eq. (78) (E-residual identity); the frozen case is priced by the Scofield-Hoffman Table-2 oracle (G2) + Hoffman E-residual along optimized contours. |
| H-Pa ambient constant over the cycle | WEAKENED -> DISCHARGED (PASS 2, S16 §4) | T3 Corollary-2 duality (Pa and Pc enter alike): the case-D product measure mu_cycle (x) mu_trajectory removes the hypothesis STRUCTURALLY at zero formulation cost (D6 Annex B case D); constant Pa is a convenience instance, not load-bearing. [S16: adjudicated DISCHARGED as a THEORY hypothesis — constant Pa is the declared INSTANCE of the case-D general form of record; the (P) text is untouched (anchor discipline), the mission channel activates case D when data demand.] |
| H-R1 causal separation (heat release upstream of Gamma_d) | PRICED | Executable rejector minted S14 (PP-6): total-enthalpy-flux residual across Gamma_d (or declared residual-release bound); violation channel documented in RDEs (afterburning) -> N4; row + falsifier in D1 §9. |

------------------------------------------------------------------------------
## §2 The registry conditionals

| ID | Verdict | Grounds |
|---|---|---|
| C-D25U uniform semiglobal stability | WEAKENED | S15: component -a WRITTEN at smooth level with explicit constants ([S-D25U-U1]) and -b as its corollary; certificate honestly AMENDED (five constants, h_min); residual = U3/U4 composition (bounded, named) + -c/U5 (research-grade, lead named: Bressan-Guerra/Ulbrich + Breitkopf-Ulbrich arXiv:2509.22076). [S16 PASS 2: -a chain COMPLETE at class level ([S-D25U-U34]: U3 fronts + U4 composition, LIP_shocked explicit in the five constants); the residual is now SHARP — the single scalar U3-H1 + clauses c2-c4 (adjudicated in §4) + -c/U5 unchanged.] |
| C-MAJDA front stability across fitted shocks | NECESSARY(cex) | Counterexample-level grounds of record: multi-D entropy solutions are non-unique in the wild class (convex integration — the D2.5 citation Brenier-De Lellis-Székelyhidi line is exactly why S2 is never used as a constraint); across-front weak-strong is OPEN for everyone (M0 D2.5). Priced: Lax/Majda transversality is EXECUTABLE at brick level (X-G0AX: sigma_min collapse detected, fold exponent in band). [S16: the IN-CLASS content is SHARPENED to the single scalar U3-H1 (instance-certified, X-U3BD; uniformity by compactness once pointwise — [S-D25U-U34] §2/§6) and a WEAK-LEVEL route is named ([S-ACFR], gated B1-B3); the NECESSARY verdict (wild-class cex) is untouched.] |
| C-HT4 sonic-capped ideal adaptation | PRICED | Declared MODEL CLOSURE by contract (SCAFFOLD §3 rule 4 — not an analytic gap); published bound precedent (Kraiko-Egoryan); executable carriers groups (viii)/(xi); falsifier = PB-2 band. |
| C-IGMIX caloric closure pair | PRICED | Bracketed by the EXECUTABLE pair [frozen, shifting-equilibrium]: [T-EQBR] +6.34..+6.97% ceiling bracket with bars (group (xii)); falsifier = finite-rate leaving the bracket. |
| C-O33 adjoint component match | PRICED, RESIDUAL NOW QUANTIFIED (S19 2026-08-06) | Numeric residual by contract; protocol PRE-REGISTERED (P2_outline §5 + its S19 execution addendum) and EXECUTED ([X-O33B]): the primary gradient-level criterion PASSED, f2 = -lambda2 constant on the control surface for our optimum and for GENO's Rao contour with the two constants agreeing to 2.4e-04, compatibility cancelling to 1.6e-04 against a wrong-sign control at exactly 1.0. STILL OPEN, and now with a number and a cause: the corner identity of identification (iii) closes to 6.6e-02 on the 8-node design (MESH-INDEPENDENT) and 2.0e-02 on a faithful Rao wall, converging in both the design-class and mesh limits — the dominant term is the DESIGN CLASS, not the discretization. Discharge = re-optimize in an adaptive, error-driven knot class and re-measure (D6 item 9, S19 residue (a)). |
| C-P4RZ monodromy Riesz/compactness | PRICED | The monodromy of a linear hyperbolic phase transport is generically NON-smoothing (S14 X2 exchange) — the Riesz step is genuine analysis, not bookkeeping; until discharged the computed eigenvalue margin is a declared MONITORED SURROGATE; fallback route (Kilque/CGW class) flagged in the roads atlas (residue, T2 pending). |
| C-XBVP transfer residuals (minted S15) | PRICED -> WEAKENED (PASS 2, S16 §4) | (a) convexity discharge: DISCHARGED AT INSTANCE LEVEL same session (X-IVXC interval certificate, whole box, all (rho,S) via T-XRED — the priced interval route EXECUTED; abstract-EOS residue = schema); (b) trace bookkeeping priced bounded (Dafermos-class); the algebraic core (T-XSON/T-XWALL) is already THEOREM at abstract EOS. [S16: with (a) discharged at instance, the conditional is CONFINED to the named minimum — (b) traces + the abstract-EOS schema residue of (a): verdict upgraded to WEAKENED.] |

------------------------------------------------------------------------------
## §3 Reading, and pass-2 targets (named, so the ledger is actionable)

READING. The theory's hypothesis surface, adjudicated: nothing rests
on an unexamined assumption; every NECESSARY row carries a
counterexample (four of them executable/machine-checked, one
published & page-verified); every PRICED row names its executable
violation channel. Two S15 items moved rows the same session they
landed: X-SLRW upgraded H-A1/H-A2 counterexamples from prose to
machine-exhibited; T-XWS + S-D25U-U1 weakened D3.

PASS-2 TARGETS (each names its discharge mechanism; no dates
promised):
 1. H2 -> DISCHARGED on L4-standardized interfaces (make axially
    supersonic data the certified default; subsonic patches become a
    declared case-class, not a hypothesis).
 2. H-I2 -> same route as H2 (the two share the subsonic-patch
    residue).
 3. D3 -> WEAKENED further to conditional-free in the shock-free
    class by discharging C-XBVP(a) (interval proof) + (b).
 4. H-Pa -> DISCHARGED by promoting case D (product measure) to the
    default formulation; constant Pa becomes an instance.
 5. C-D25U -a -> full (add U3 fronts + U4 composition to U1: bounded
    classical work, priced by the U1 execution experience).
 6. C-XBVP(a) -> DISCHARGED via the interval-arithmetic route of the
    global-maximum dossier (shared machinery).
Pass 2 closes when every row is DISCHARGED, WEAKENED-to-named-
minimum, or NECESSARY-with-counterexample — i.e. when PRICED rows
remain only where the price is physics (H-F1, H-T4), not missing
work.

------------------------------------------------------------------------------
## §4 Pass 2 (executed 2026-08-06, S16 deep-foundations tranche 2)

Adjudication of the six named pass-2 targets against the record as
of S16 step 4 (post U3/U4 + a-contraction), plus the mandatory
adjudication of every clause MINTED after pass 1. Same discipline:
verdicts from the existing record only; cells cite sites.

### §4.1 The six named targets

| Target (pass-1 §3) | Outcome | Grounds |
|---|---|---|
| 1. H2 -> discharged on L4-default | EXECUTED: DISCHARGED | L4 declared the certified interface DEFAULT (M0 D2.4 dated note, S16): on the default class mdot-independence is EXACT ([T-TH0] L4 note) with no choking assumption; H2 survives only as a CASE-CLASS closure inside D1 §4.3bis O2/O3 (subsonic patches), same monitors — a case-class closure is not a theory hypothesis. |
| 2. H-I2 -> same route | EXECUTED: DISCHARGED | On the L4 default the row is a THEOREM ([T-NSW]); case-class residue keeps the R2 characteristic-direction audit (D1 §4.3bis downgrades written into the Verdict). |
| 3. D3 -> conditional-free shock-free | PARTIAL (stays WEAKENED, residual sharpened) | C-XBVP(a) discharged AT INSTANCE (X-IVXC, S15); (b) still priced (Dafermos-class traces) — the shock-free uniqueness pair (T-XWS + S-D25U-U1 §6) is conditional-free ONLY when (b) closes; S16 adds the shocked within-stratum uniqueness ([S-D25U-U34] -b corollary). Honest: not yet conditional-free. |
| 4. H-Pa -> discharged by case-D promotion | EXECUTED: DISCHARGED (instance reclassification) | Constant Pa adjudicated a declared INSTANCE of the case-D product-measure general form of record (T3 Corollary-2 duality + D6 Annex B case D); nothing in the proof chain uses constancy beyond the instance; (P) text UNTOUCHED (anchor discipline) — the mission channel activates case D when data demand. |
| 5. C-D25U -a -> full | EXECUTED (S16 T1): -a COMPLETE at class level | [S-D25U-U34]: U3 fronts + U4 composition, LIP_shocked explicit in the five constants; residual sharp = U3-H1 + c2-c4 + (-c/U5). Verdict stays WEAKENED (the -c component alone keeps it from DISCHARGED). |
| 6. C-XBVP(a) -> interval route | EXECUTED (S15): instance discharge; verdict PRICED -> WEAKENED | X-IVXC + T-XRED (whole box, every (rho, S)); abstract-EOS statement = schema residue; (b) = the named minimum. |

### §4.2 Clauses minted after pass 1 (mandatory adjudication)

| Clause | Verdict | Grounds / executable channel |
|---|---|---|
| U3-H1 Lopatinskii scalar s_L /= 0 on K_delta ([S-D25U-U34] c1) | PRICED | Instance-certified (X-U3BD: s_L = 1.8685, rejectors active); class-level channel NAMED = interval certification over K_delta (B1, shared substrate); runtime symptom = front-solve conditioning blowup in the A1 march (monitored by its Newton solves). |
| c2 same-front-topology stratum ([S-D25U-U34]) | PRICED (structural scope, not droppable) | Topology changes are DISCRETE march events: the codomain (front count) itself changes, so no fixed-space Lipschitz estimate can cross them — scope, not gap; channels: RK-G policy (trust region + re-record + kink detection) + census S0 strata + the [S-ACFR] weak-level route (topology-free competitor) as the named escape. |
| c3 front-origination Lipschitz ([S-D25U-U34]) | PRICED | Wall-feature origination = automatic (corner RH solve, U3-L1); data-borne fronts = part of the certified data norm; channel: the stage-A data contract audits (front position/slope declared with the family). |
| c4 genuine nonlinearity G > 0 on the state box ([S-D25U-U34]) | PRICED | Automatic for perfect/ideal gas (production oracle class); for tabulated EOS the channel is an EOS-audit on the table (fundamental-derivative sign over the state box — joins the THERMOTAB consistency-invariant duty, D6 item 9); violation (BZT-class states) would kill the entropy-jump floor s_j and with it the U4-A counting — declared. |
| [S-ACFR] confinement clause (competitor in the certified convexity box) | PRICED (load-bearing, not removable by the method) | Relative entropy needs convexity ([X-IVXC] box); escape-from-box stays with the S1 membership monitor + census layer; the clause is the a-contraction analogue of C-XBVP(b) scoping — one shared pricing, two instruments. |

### §4.3 Pass-2 reading

Living ledger = 29 rows (24 original + 5 minted), zero unadjudicated.
Totals: 3 DISCHARGED / 4 WEAKENED / 5 NECESSARY (unchanged, all with
cited counterexamples) / 17 PRICED (12 original + 5 new clauses).
The pass-2 closure criterion of §3 is NOT yet met (PRICED rows still
include missing work, not only physics: U3-H1/B1, C-XBVP(b),
C-P4RZ); the remaining discharge mechanisms are all NAMED with
executable channels — pass 3 targets: B1 (one interval brick
discharges U3-H1 AND arms S-ACFR's B1 with the same machinery),
C-XBVP(b) traces, C-P4RZ or its Kilque/CGW fallback.

Audit line: [Class: PRACTICE (adjudication record; every cell cites
its record site; no new claims) | Falsifier: any row whose cited
grounds do not support its verdict (grep-checkable citations) |
Carrier: none (governance doc; the cited carriers belong to the
rows) | Gamma: n/a (no mathematical content of its own)].

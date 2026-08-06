# Hypothesis-minimization ledger — pass 1 (D9 candidate)

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

------------------------------------------------------------------------------
## §1 The D1 §9 rows

| ID | Verdict | Grounds (record sites) |
|---|---|---|
| H-A1 single rotating wave, n-fold, periodic | NECESSARY(cex) | Counterexample MACHINE-EXHIBITED S15: X-SLRW rejector R1 — a counter-rotating admixture makes the transverse resultant nonzero with 2-Omega-pulsating modulus (elliptical orbit), and the T0 steadification fails; docs/rde_nozzle_side_load.md §3 B1. Violation priced separately (PB-5 robust formulation; T0-flatness monitor D6 5-bis). |
| H-A2 axisymmetric wall/control surfaces | NECESSARY(cex) | Counterexample mechanism machine-exhibited: a non-axisymmetric geometric kernel reads m != 0,+-1 harmonics (X-SLRW R3: the m=2 functional of an n=2 pattern is nonzero), and any m != 0 line carries e^{-imOmega t} — time-dependent loads; T0(i) proof uses n_theta = 0 essentially (M0 Theorem 3). |
| H-F1 frozen family (s, mu, Omega_w indep. of Sigma) | PRICED | Chamber-response map with measured contraction q (D6 A6 stage-G); choked-annulus margins 0.97/0.65 documented (registry/D6 Annex B case G); PB-4 bilevel formulation stands ready if q >~ 1. |
| H2 choked feed, fixed A_t | WEAKENED | M0 [T-TH0] note of record: with a fully axially supersonic interface (L4) the mdot-independence holds EXACTLY without upstream choking — H2 is needed only on subsonic-patch interfaces; choking-margin monitor per row remains. |
| H-I2 no mean upstream influence through Gamma_d | WEAKENED | On axially supersonic patches it is a THEOREM, not a hypothesis ([T-NSW]: u_x > c makes x = const spacelike in every frame — no upstream signal); the assumption survives ONLY on declared subsonic patches, where the R2 characteristic-direction audit prices it. |
| D1 quasi-steady St -> 0 | PRICED | [T-T3QS]: second-order protection on ray families (first-order sweep correction vanishes on the smooth part, executable carrier group (xvi)); O5-lite pre-registered falsification (D6 A4: P-i/P-ii/P-iii with rejectors); J1 corrector = the A4 deliverable; (P)(v) bar carries St|J1|. |
| D2 azimuthal decoupling | PRICED | [S-BLITE]: the 3-D helical wave-frame march is the EXACT meter of the sweep/D2 residual at marching cost; (P)(v) bar carries the D2 residual; full anchor = A5. |
| D3 per-phase S1 regularity/uniqueness | WEAKENED | Uniqueness in the shock-free class is now THEOREM-SHAPED by two independent mechanisms (S15): [T-XWS] BVP-native weak-strong (mod [C-XBVP]) and [S-D25U-U1] §6 Gronwall-on-differences corollary; membership stays monitored a posteriori (boundary function, D2.5); across fronts the conditional is [C-MAJDA], cleanly separated. From bare assumption to monitored-membership + conditional theorems. |
| H-T3.1 one frozen gamma | NECESSARY(cex) | Executable counterexample of record: two-gamma counterexample [T-T3-CE], suite group (ix) — the collapse fails at second order with measured gamma_eff; price measured small (D3 §5.2 numbers: eps* shift -0.56%). |
| H-T3.2 full-flowing, supersonic exit | WEAKENED | TRANSFORMED (S12, [D-GSEP]): no longer assumed — ENFORCED as the per-phase state constraint g_sep <= 0 in (P) with active-set multiplier = marginal attachment value; deliberate separation exits the certified class by physics (subsonic feedback + non-rotating dynamics). The cleanest minimization move in the corpus: hypothesis -> constraint. |
| H-T3.3 phase-independent inflow shape | NECESSARY(cex) | First-order breaker: any per-phase (M, theta)(y; xi) profile variation defeats the T3 Lemma-A similarity (N3 channel, D1 §9); at I3 interfaces it holds BY CONSTRUCTION (case-A Verdict class, D6 Annex B) — the necessity is priced by interface class, not removed. |
| H-T4 ideal-adaptation closure | PRICED | Declared model closure [C-HT4] with published bound precedent (Kraiko-Egoryan); sonic cap of record (M0 Prop. 7 sharpening); PB-2 truncation/base-pressure band = the falsifier [named IOU, dated 2026-08-05 (D8 §8 two-lens): executable only under a declared base-pressure closure p_b — proposed C-N2, to be minted at PB-2/OP-2 kickoff]; N2 stays THE declared open problem. |
| H-P1 spectral non-degeneracy, transversal fronts | PRICED | Evans/Arnoldi monitor (A5 certificates); the monodromy margin is the MONITORED SURROGATE of the full condition pending [C-P4RZ]; set-valued J at mode boundaries declared (D1 §9). |
| H-mu measure known | PRICED | The cheapest full pricing in the ledger: J is LINEAR in mu, so the sensitivity report is free (|dJ| <= osc_xi(F)·TV or Lip_xi(F)·W1 — D6 item 15 mu-instruments bundle, ME-5); DRO ball (PB-5) for declared misspecification; [T-O2] fixes the nominal. |
| H-E4 per-phase Rao/corner at gamma(T) frozen | NECESSARY(cex) | PUBLISHED counterexample, page-verified (S6): finite-rate chemistry breaks the corner theory — Hoffman 1967 Eq. (78) (E-residual identity); the frozen case is priced by the Scofield-Hoffman Table-2 oracle (G2) + Hoffman E-residual along optimized contours. |
| H-Pa ambient constant over the cycle | WEAKENED | T3 Corollary-2 duality (Pa and Pc enter alike): the case-D product measure mu_cycle (x) mu_trajectory removes the hypothesis STRUCTURALLY at zero formulation cost (D6 Annex B case D); constant Pa is a convenience instance, not load-bearing. |
| H-R1 causal separation (heat release upstream of Gamma_d) | PRICED | Executable rejector minted S14 (PP-6): total-enthalpy-flux residual across Gamma_d (or declared residual-release bound); violation channel documented in RDEs (afterburning) -> N4; row + falsifier in D1 §9. |

------------------------------------------------------------------------------
## §2 The registry conditionals

| ID | Verdict | Grounds |
|---|---|---|
| C-D25U uniform semiglobal stability | WEAKENED | S15: component -a WRITTEN at smooth level with explicit constants ([S-D25U-U1]) and -b as its corollary; certificate honestly AMENDED (five constants, h_min); residual = U3/U4 composition (bounded, named) + -c/U5 (research-grade, lead named: Bressan-Guerra/Ulbrich + Breitkopf-Ulbrich arXiv:2509.22076). |
| C-MAJDA front stability across fitted shocks | NECESSARY(cex) | Counterexample-level grounds of record: multi-D entropy solutions are non-unique in the wild class (convex integration — the D2.5 citation Brenier-De Lellis-Székelyhidi line is exactly why S2 is never used as a constraint); across-front weak-strong is OPEN for everyone (M0 D2.5). Priced: Lax/Majda transversality is EXECUTABLE at brick level (X-G0AX: sigma_min collapse detected, fold exponent in band). |
| C-HT4 sonic-capped ideal adaptation | PRICED | Declared MODEL CLOSURE by contract (SCAFFOLD §3 rule 4 — not an analytic gap); published bound precedent (Kraiko-Egoryan); executable carriers groups (viii)/(xi); falsifier = PB-2 band. |
| C-IGMIX caloric closure pair | PRICED | Bracketed by the EXECUTABLE pair [frozen, shifting-equilibrium]: [T-EQBR] +6.34..+6.97% ceiling bracket with bars (group (xii)); falsifier = finite-rate leaving the bracket. |
| C-O33 adjoint component match | PRICED | Numeric residual by contract; protocol PRE-REGISTERED (P2_outline §5: (30)/(31)+f2 compatibility rows, lip-excluded norms) — S15 waiver compensating control (i) keeps it ready; lands with brick 2. |
| C-P4RZ monodromy Riesz/compactness | PRICED | The monodromy of a linear hyperbolic phase transport is generically NON-smoothing (S14 X2 exchange) — the Riesz step is genuine analysis, not bookkeeping; until discharged the computed eigenvalue margin is a declared MONITORED SURROGATE; fallback route (Kilque/CGW class) flagged in the roads atlas (residue, T2 pending). |
| C-XBVP transfer residuals (minted S15) | PRICED | (a) convexity discharge: DISCHARGED AT INSTANCE LEVEL same session (X-IVXC interval certificate, whole box, all (rho,S) via T-XRED — the priced interval route EXECUTED; abstract-EOS residue = schema); (b) trace bookkeeping priced bounded (Dafermos-class); the algebraic core (T-XSON/T-XWALL) is already THEOREM at abstract EOS. |

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

Audit line: [Class: PRACTICE (adjudication record; every cell cites
its record site; no new claims) | Falsifier: any row whose cited
grounds do not support its verdict (grep-checkable citations) |
Carrier: none (governance doc; the cited carriers belong to the
rows) | Gamma: n/a (no mathematical content of its own)].

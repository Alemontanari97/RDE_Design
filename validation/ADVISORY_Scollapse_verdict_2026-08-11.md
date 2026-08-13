# ADVISORY — S-COLLAPSE VERDICT OF RECORD (Campaign A of S-GAUNTLET,
# 2026-08-11; executes ADVISORY_Scollapse_prompt_2026-08-11.md T1-T5.
# Form-2 panels (T1 enunciate + T2 breakers a-e, dedicated refuters)
# + Form-3 red-team + FORM-3 DISCHARGE on full on-file artifacts.)

STATUS: advisory (untracked). LABEL OF RECORD: "JUDGE-ADJUDICATED IN
ONE ROUND — DISCHARGE-VERIFIED ON FULL ON-FILE ARTIFACTS (Form 3,
2026-08-11)". The initial red-team blocked absorption because judges
and red-team had received TRUNCATED artifact slices (an orchestration
defect of the session lead's workflow script, declared in the session
log); the discharge pass verified every adoption against the complete
raws and voided the truncation blockers. ABSORPTION UNBLOCKED under
the corrected wordings below; the judge-added clause register (§7)
lists what may NEVER be quoted as converged. All magnitudes here are
literature-anchored EXPECTATIONS, marked as such; NO numbers of
record were created (no carrier was run); every carrier is NAMED and
dispatched to the F line.
PROVENANCE: workflow wf_3e7f47b9-e4c (17 agents: 2 T1 experts + T1
refuter + T1 judge; 5 breaker derivers + 5 dedicated refuters + T2
judge; T3/T4 synthesizer; Form-3 red-team) + discharge agent on full
artifacts. Full raws in the session journal
(.claude/projects/.../subagents/workflows/wf_3e7f47b9-e4c/journal.jsonl).

------------------------------------------------------------------------------
## 1. HEADLINE VERDICT (the user-mandate question)

THE STRONG CLAIM ("the optimal bell profile and optimal Isp of a
constrained bell COINCIDE with the optimum of the equivalent steady
engine at matched mass flow, Harroun-style, in the GENERAL case") is:
 - REFUTED AS A GENERAL THEOREM, and
 - PROVED AS A CORNER THEOREM: it holds EXACTLY on the p-only scaling
   class (H1-T ideal-gas pin + H2' + H3-p + H4) with vacuum objective
   (H-OBJ), where it is convention-free and matching-free
   (matched-mdot == matched-<p>, degenerate); at Pa != 0 it survives
   ONLY at the measure-pinned design point <Pc>_mu under T-O1's own
   hypotheses; outside, it fails at first order through five named
   channels (a)-(e), each with a named killing carrier.
T3-AS-STATED (M0 [T-T3], docs/rde_nozzle_MASTER.md:512-546) IS
UNBROKEN BY ALL FIVE BREAKERS: every breaker either exits the
hypothesis domain or breaks a DISTINCT object (averaging convention,
constraint activity, twin fairness, domain of definition,
well-posedness of the comparison).

------------------------------------------------------------------------------
## 2. [T-T3-SI] — THE SCALE-INVARIANCE PRECISAZIONE (T1, converged)

TIER 1 — THEOREM (Gibbs closure independently re-derived at Form-3
discharge 2026-08-11). Hypotheses: H1-T thermally-perfect ideal gas
p = rho R T, FROZEN composition, e = e(T) free (gamma(T) allowed);
H1-T is EXACT and not relaxable: for any EOS rho = p f(T) with
e = e(T), Gibbs compatibility (de/dv)_T = T (dp/dT)_v - p = 0 forces
f = C/T — the "rho = p f(T)" generalization (audit theory-core:F2
wording) is EMPTY, and the scaling FAILS for co-volume/virial/
tabulated real-gas EOS; H2' (as in T-T3); H3-p p-only family
P0(xi) = k(xi) P0,1, T0 and inflow shape frozen; H4 uniqueness;
H-OBJ vacuum objective Pa = 0; H-MEAS any probability measure nu in
the validity set with 0 < Int k dnu < inf.
CLAIM (tier 1): F(xi) = k(xi) F1[Sigma] AND mdot(xi) = k(xi)
mdot1[Sigma] (the mdot half is implicit in Lemma A, stated nowhere
in T-T3); hence Isp(xi) = F1/(g0 mdot1) PHASE-CONSTANT and
Isp_cycle[nu] = F1/(g0 mdot1) for EVERY nu: ratio-of-means =
mean-of-ratios, every quasi-arithmetic aggregation coincides, the
shape optimum is nu-INDEPENDENT and coincides with the single-phase
steady optimum; matched-mdot degeneracy (matching at any phase or at
the mean yields the same Isp). The tier-1 Isp half needs NO
frozen-family hypothesis (cancellation pointwise in Sigma).
TIER 2 ((P0,T0)(xi) both vary; ADD H1-C calorically perfect, per
Lemma B) — THEOREM*: F(xi) = k F1 (CF T0-blind), mdot(xi) =
k tau^(-1/2) mdot1 (tau = T0(xi)/T0,1), Isp(xi) = R[Sigma] sqrt(tau);
Isp_cycle[nu] = R[Sigma] C(nu): C nu-dependent, Sigma-independent —
hence shape optimum nu-independent — ONLY UNDER H-F1 (T-O1(i));
bilevel coupling can make the tier-2 optimum nu-dependent. CAP
(T1-JUDGE-ADDED, judge-noticed, conservative — stands AS A CAP):
Lemma B (M0:535-540) carries NO across-shocks clause; the
RH/Mach-similarity check under T0-rescale for calorically perfect
gas is the named THEOREM*->THEOREM promotion condition.
CONTAINMENT (of record, both routes): at Pa = 0 the thrust-argmax
half is a corollary of T-T3 + Lemma C + the T-O2 measure-agnostic
note; the Isp-argmax coincidence with the classical argmax at
<Pc>_mu holds at ANY Pa by T-O1 composed with T-T3. GENUINELY NEW:
explicit mdot scaling, per-phase Isp constancy, every-nu VALUE
equality, matched-mdot degeneracy, tier-2 C(nu) factorization,
detector.
DETECTOR (dual-proof carrier, NAMED, F-line dispatch, NOT
implemented): X-T3SI-conv (expert-1's name of record; "X-SICONV"
was a judge rename — ONE name to be pinned at registration).
Convention sweep {time, mass-flux, log-uniform, atomic empirical}
on one certified per-phase family; exact contrapositive = THEOREM
(nonzero EXACT convention-sensitivity of Isp_cycle implies violation
of the TIER-1+VACUUM set); measured instrument = PRACTICE, needs
DERIVED tolerance + rejector (R5); T0(xi) variation trips it BY
DESIGN (it detects tier-1 departures, not T-T3 violations); KILL
branch: injected T0 variation must reopen the spread with the
sqrt(T0) law.
REGISTRATION PROVIDED-CONDITIONS (refuter's four, binding before
[T-T3-SI] lands in M0): (i) containment table with BOTH routes;
(ii) corrected H1-T (Gibbs form); (iii) H-CON scope clause (the
"which mean is moot" rhetoric holds for GEOMETRIC-ONLY constraint
classes; mixed/performance constraints can reintroduce measure
dependence); (iv) a query-bounded novelty delimiter of its own (the
G2 novelty bound stands on its OLD queries; the 4-query widening was
default-refuted). Additional registration duties: Noble-Abel
known-answer rejector for H1-T (carrier-owed); the
P1_sections_2_4:229-232 "ARBITRARY frozen EOS" echo must be
corrected (NOT covered by the registry fix alone).

------------------------------------------------------------------------------
## 3. THE FIVE BREAKERS (T2, converged; discharge-corrected wordings)

(a) AMBIENT Pa != 0.
 (a-S) J = a<Pc> - Pa·b survives with argmax = Rao-at-<Pc> [THEOREM,
 = T-T3 itself]; Isp_RA = <F>/(g0<mdot>) shares that argmax [THEOREM,
 two-line corollary; deriver-a P2, refuter-a CONFIRMED by independent
 re-derivation] under T-O1's own hypotheses OF RECORD (M0:407-419):
 (i) frozen family H-F1 (cycle family, period, A_t Sigma-independent);
 (ii) choked feed H2 (mdot = Pc A_t / c*(t)); in-theorem failure
 channels: bilevel coupling breaks (i) — thrust-max and Isp-max become
 DIFFERENT problems; unchoked tails break (ii); axially subsonic
 interface patches can make mdot Sigma-dependent; L4 note
 (M0:418-419): fully axially supersonic interface makes (i) and
 mdot-independence EXACT without upstream choking; plus T-T3's own
 H1-H4 on the T-T3 leg. THIS is the ONE hypothesis list of record for
 every future "sea-level coincides" sentence.
 (a-B1) Average-of-ratios Isp collapses to the classical design at
 the HARMONIC mean Pc_harm = <Pc^-1>^-1 < <Pc> strictly [identity
 THEOREM, refuter re-derived]; argmax SHIFT THEOREM* (design-map
 monotonicity lemma missing). Breaks the CONVENTION, not T3.
 (a-B2) Constraint activity governed by ess-inf k (low-k tail), not
 <k> [structure THEOREM*, shift genericity SCHEMA]; the
 separation-margin row is the DECLARED HONEST GAP
 (ADVISORY_rde_choking:319-325) and the a-B2 carrier leg is
 OWNERLESS pending F3-entry assignment.
 (a-B3) Any mu-positive separated phase kills H2': wall-pressure
 plateau clamps near sigma·Pa and cannot k-scale, F(xi) loses
 affinity, the collapse dies even for J [SCHEMA — mechanism exact;
 class pinned by deriver-a and CONFIRMED by refuter-a (separation
 viscous, machinery inviscid); the judge's THEOREM* upgrade via the
 M0:554-555 prose caveat is RETRACTED at discharge]. THEOREM* repair
 QUEUED: formalize the hypothesis-exit lemma (Pa datum enters the
 interior downstream of the separation front, killing ambient-
 blindness); rejector = CARRIER-A K4.
 CORRECTIONS OF RECORD: choking advisory 2-ter(a) "only the
 vacuum-equivalent objective is protected" is TOO NARROW — fixed-wall
 J AND ratio-of-averages Isp (under the T-O1 list above) are also
 protected; the naive "J depends on the k-distribution at first
 order" is FALSE and must never be claimed. Stechmann anchors of
 record: Eq. (4) journal p.888, JSR 56(3) 2019; quotes pp.893-895
 (range tightened at page-verify).
 MAGNITUDES (EXPECTATION): arithmetic-harmonic wedge ~O(50%) of <Pc>
 at RDE amplitudes (P-M sigma/mu~0.70 p.5); Stechmann Fig. 8 p.893
 low-k overexpansion; Harroun pp.670/672 separation delay =>
 inviscid margins conservative.
 CARRIER-A (F5a; K4 monitor F2a): two-convention Pa evaluator on the
 affine family over [T-O2] log-uniform measure; K1 J-affinity
 residual, K2 arithmetic-vs-harmonic argmax audit, K3
 tail-activation constrained argmax, K4 separated-phase/H2' monitor.

(b) PER-PHASE M/T0/gamma/s VARIATION (mixture/Jensen).
 Exact objective = MIXTURE FORM J = a_eff·<Pc> - Pa·b, a_eff =
 <a·Pc>/<Pc>, a = a[Sigma; T0(xi), gamma-law, m(xi), s(xi)] (T0
 restored — omitting it re-invokes Lemma B outside H1) [THEOREM*,
 generalizes T-T3-CE gamma_eff = <Pc gamma>/<Pc>]. Representability
 by one member state is SUFFICIENT for coincidence (the "iff" is
 struck); Jensen gap <J[D]> - J[<D>] = (1/2)F_DD:Cov + R3 [THEOREM*
 under C2 regularity]; ONLY the (p,p) Hessian diagonal vanishes —
 Cov(Pc,T0), Cov(Pc,gamma) cross terms live in the pressure channel;
 pure-p variation alone gives zero gap (control). Optimum-shift
 genericity: CONJECTURE. The Pc-weighted first-order closure is
 T-T3-CE-consistent and DISTINCT from the panel's TWIN-C fair twin —
 conflation prohibited. MAGNITUDE (EXPECTATION): (sigma/mu)^2 ~ 0.5
 (P-M p.5); gamma design penalty second order (envelope).
 CARRIER-B (F2): T-T3-CE extension, two-phase multi-channel
 (Pc,T0,gamma) family; J1 representability audit, J2 Jensen ledger
 with pure-p zero-gap control, J3 instance argmax coincidence.

(c) SWIRL: FIRST vs SECOND MOMENT + RECOVERY ASYMMETRY.
 (c0) The collapse SURVIVES swirl in-hypothesis via BOTH lemmas
 [THEOREM* — assembled from TWO SINGLE-SOURCE pen legs: Lemma A leg
 by deriver-c; Lemma B leg by refuter-c as the REPAIR of
 c0-as-stated, which was refuted-as-incomplete ("Gamma-field
 phase-independent" false under varying T0(xi)); NOT two independent
 derivations; both-identities symbolic carrier mandatory for
 promotion]; calorically-perfect boundary inherited (gamma(T) dies);
 dimensional Gamma-field is phase-DEPENDENT under T0 variation.
 (c1) First moment: NON-BREAKER of record (mean-swirl panel P1
 THEOREM* under H-AM1..5; lead's net-Gamma claim REFUTED, P2);
 qualifier of record = "IDEALIZED axial-injection class" (discrete-
 orifice faceplate torque generically nonzero in real hardware —
 the dropped-qualifier summary form is barred from propagation).
 (c2) Second moment: wedge = swirl-KE flux E_theta =
 <oint rho u_x u_theta^2/2 dA>, positive UNDER THE NAMED through-flow
 condition rho·u_x > 0 (carried by L4 + psi-monotonicity C1 guard),
 strictly first-order, unconstrained by flux nullity [THEOREM* under
 T0]. The break is TWIN-FAIRNESS: identifying the swirl-bearing
 collapsed target with the ZERO-swirl classical optimum (TWIN-A).
 RECOVERY ASYMMETRY: Gamma conserved per streamline => swirl KE
 Gamma^2/(2r^2) decays on outward (bell) and concentrates on inward
 (plug) expansion — sign AGAINST the plug family [per-streamline
 THEOREM* within the N6-2 free-vortex class]. MAGNITUDES
 (EXPECTATION): +6% EAPi / +3% experimental EAP (K-P p.7 CFD / p.11,
 per ADVISORY_rde_choking:246-250).
 CARRIER-C: leg 1 (F2) symbolic five-field scaling KAT in
 n6_swirl_kernel.py checking Lemma A AND Lemma B rows (any failing
 row kills c0); leg 2 (F5a) TWIN-A/TWIN-C evaluation row reporting
 the E_theta debit (panel falsifier A4) + the axial-vs-total rung in
 src/thrust/bounds.py (missing executable of record, F2a hygiene).

(d) SUBSONIC PATCHES: PARTIAL PER-PHASE MAP.
 The per-phase steady supersonic map exists only on Xi_sup = {m(xi)
 >= delta}; on Xi_sub the failure is REGIME CHANGE forced by
 frame-invariant spacelikeness [T-NSW] [partiality THEOREM]. J as
 written is UNDEFINED when mu(Xi_sub) > 0; the well-formed object is
 the TWO-REGIME decomposition (choking census C1, LOAD-BEARING).
 mu(Xi_sub) > 0: page-verified in ONE healthy example (K-P Table 1
 p.6 axial Mach 0.86-1.33 avg 0.99, Fig. 6 p.10, p.14 low-PR) —
 generic-class EXPECTATION, demoted from universal [refuter's attack
 verified on full text at discharge]. O3-SURVIVAL-IN-FORM: REFUTED
 AS STATED; reissued conditional on NEW sub-hypothesis H3-cl
 (certified phase-independent closure patch pattern) or
 whole-interface I3 — K-P Fig. 6's MIGRATING subsonic sector is
 EXPECTED to kill H3-cl; without it the subsonic sector joins
 breaker (b)'s mixture form. MAGNITUDES (EXPECTATION): pure
 M=1-closure component < 5.4% typical (K-P Fig. 7 p.11), ~7% at
 M_8x = 0.6; the 1.7-8.7%/~15% figures are TOTAL EAP-vs-EAPi
 envelopes, never a realized closure band; pressure-band -> Isp-band
 transfer OPEN/SCHEMA.
 CARRIER-D (F2a classifier via U3', F5 consumption): stage-A
 axial-margin classifier m(xi) + two-regime contract; D1 mu(Xi_sub)
 measurement, D2 H3-cl patch-pattern audit, D3 priced closure band.

(e) THE T0 MEASURE / MATCHING CONVENTION.
 E-INV RESTRICTED [refuter counterexample adopted: two equal-weight
 phases (2P0, T0/4) give w-dependent Isp inside full H1-H4]: on the
 P-ONLY SCALING CLASS at Pa=0 every convention yields the same shape
 optimum AND value [THEOREM on the corrected class]; matched-mdot ==
 matched-<p> degenerate there. W1: <G>_t = <G>_mdot -
 cov(rho u_x, G)/<rho u_x> [THEOREM* under T0]; design-pressure
 wedge <Pc>_mdot - <Pc>_t = Var(Pc)/<Pc>_t exact WITHIN the p-only
 class only (c* not frozen by H1+H3); sign clause CONJECTURE. W2
 (DISCHARGE-CORRECTED, the judge's original completion must not
 ship): p_match = <p·u_x/T>/<u_x/T> is THEOREM* ONLY for the twin
 DEFINED by u_s/T_s := <u_x/T>; for the (T_s=<T>, u_s=<u>,
 ideal-gas) twin the exact matched pressure is
 <p·u_x/T>·<T>/<u_x>, differing at order (sigma/mu)^2 — the
 construction must be DECLARED; qualitative content survives
 (p_match - <p> = O(cov) != 0 generically; vanishes in Harroun's lab
 by construction). Fair twin of record = TWIN-C flux-consistent
 (swirl panel S3); Harroun's own averaging convention is UNDECLARED
 (choking SS3-bis) — "compare with Harroun" is not well-posed until
 a convention is pinned; Stechmann is DECLARED mass-weighted
 (Eq. (4) p.888) and exonerated. (e) breaks NO theorem — it is the
 WELL-POSEDNESS/DECLARATION requirement: moot inside the scaling
 class, DECISIVE once (a)-(d) break scaling. MAGNITUDE
 (EXPECTATION): <Pc>_mdot/<Pc>_t = 1.41 at PR=10, 1.21 at PR=5 on
 the [T-O2] log-uniform blowdown (illustrative formula evaluation).
 CARRIER-E (F5a): measure-triple evaluator + twin rows at the three
 matchings; E1 first-order distinctness, E2 cov-sign row (= panel
 falsifier F3), E3 cross-matching designed-optimum coincidence.
 JUDGE-ADDED refinement (full-H1-H4 shape-argmax convention
 invariance via Lemma B T0-blindness, C(w) Sigma-independent UNDER
 H-F1): corroborated by refuter-e's own algebra at discharge but
 still owes its formal refuter pass in the H-F1-qualified form —
 EXCLUDED from registration (guard stands).

------------------------------------------------------------------------------
## 4. T3 MAP — "ARE WE ALWAYS INSIDE THE COLLAPSE?" NO; boundary drawn.

(I) CURRENT TWIN = INSIDE BY CONSTRUCTION. The operating
configuration (vacuum-equivalent + homentropic single frozen-gamma +
single-phase steady, fixed wall, full-flowing) sits inside the
tier-1+vacuum hypothesis set. S18 CLAUSE OF RECORD (discharge-
corrected): the S18 +0.04% agreement is a CORNER MEASUREMENT
(ADVISORY_rde_choking:218-225), NEVER citable as evidence of general
RDE/steady coincidence. NAMED PRECONDITION, NOT YET PERFORMED,
before any "zero-by-theorem inside the corner" phrasing ships: a
five-line hypothesis audit of the S18 twin configuration against
{H-OBJ vacuum, H1-T, H3-p, H2', H4} recorded from the S18 record.
HARROUN SENTENCE OF RECORD (discharge-corrected): "inside
tier-1+vacuum the matched-mdot steady equivalent and the
cycle-averaged optimum coincide exactly and convention-free — a
tier-1 CORNER READING of the TWIN-A construction (zero-swirl
comparison twin, Harroun p.666; pp.665-666 document a comparison
construction, not an optimization); convention degeneracy applies
INSIDE the corner only; TWIN-A misattribution caveats (swirl panel
P4) apply outside." NOT an identification of Harroun's methodology
with the formal tier-1 lab.

(II) RDE APPLICATION = OUTSIDE on the five axes (a)-(e) as in §3;
sea-level verdict of record: "coincides, at <Pc>_mu, weight now
load-bearing, under the T-O1 list of §3(a)" — NOT "no coincidence".

(III) AXIS -> MACHINE -> PHASE TABLE (plan v3 anchors; carriers = §3):
 (a) conventions/Pa: CARRIER-A -> F5a (K4 monitor F2a). If never
     run: claims stay vacuum-only with the <Pc>_mu qualifier.
 (a-B2) tail constraint activity: CARRIER-A K3 -> OWNERLESS; MUST be
     assigned at F3 entry adjudication (the one ownerless row).
 (a-B3) separation: K4 monitor -> F2a (G6 loud reject); SCHEMA
     lemma repair queued.
 (b) mixture form: CARRIER-B -> F2 (contact/slip F2a; var-gamma
     instance F3 exit). Tier-2 tag of record: "T1 JUDGE-ADDED cap,
     judge-noticed" for the Lemma B across-shocks step.
 (c0) swirl in-hypothesis: CARRIER-C leg 1 symbolic KAT -> F2
     (front-loadable); c0 stays THEOREM* until it runs.
 (c2) swirl-KE twin debit: CARRIER-C leg 2 -> F5a; bounds.py
     axial-vs-total rung -> F2a hygiene.
 (d) subsonic patches: CARRIER-D -> F2a OWNS U3' (plan-mandated
     BLOCKER: U3 premise-open, F5 contract cannot freeze before).
 (e) measure/matching: X-T3SI-conv -> F5a (mu-instruments bundle);
     tier-1 corner dry-run of the detector executable in an idle
     window (KAT of the instrument itself).
 DEF twin (F1b) is a DISTINCT object — conflation with TWIN-A/TWIN-C
 prohibited. 3-D residual of all axes -> F6 (B-lite), declared
 industrial gap in hardware claims.

------------------------------------------------------------------------------
## 5. T4 — [X-T3CTRL] PRE-REGISTERED T3-CONTROL ROW (protocol of
## record, class PRACTICE, rejector-gated; text ready for R4)

The full protocol text as synthesized (registered inputs 1-5, derived
bars b1-b4, corner KAT, four-limb rejector, both-outcomes-honest
verdict template, ownership) is ADOPTED with these discharge
corrections baked in: row (a) carries the T-O1 hypothesis list of
§3(a) verbatim; the W2 matched-pressure formula is used ONLY with
its declaring twin construction; the S18/Harroun sentences carry the
§4(I) qualifications. Summary of the protocol (full text = T3/T4
synthesis artifact, journal wf_3e7f47b9-e4c):
 1. OBJECTIVE PAIR J_vac AND J_app (application backpressure) on
    every candidate; vacuum-only campaigns forfeit application claims.
 2. THREE DECLARED MATCHINGS on every steady twin: matched-mdot,
    matched-<p>, TWIN-C flux-consistent; TWIN-B prohibited; TWIN-A
    admitted only as labeled zero-swirl reference. Non-degeneracy on
    nominally tier-1 data is itself a rejection.
 3. BOTH WEIGHTINGS wherever scaling is broken: ratio-of-averages AND
    average-of-ratios; time measure AND mass-flux measure; the
    arithmetic-vs-harmonic design-pressure pair reported.
 4. SUBSONIC-PATCH CLOSURE DECLARED BEFORE THE RUN (H3-cl audit, or
    I3 surrogate, or certified mu(Xi_sub)=0); a run with
    mu(Xi_sub) > 0 and no declared closure is INVALID by rule.
 5. SWIRL ACCOUNTING: E_theta debit under the through-flow guard,
    reported beside the TWIN-C twin.
 BARS b1-b4 DERIVED per campaign (certificate stack; propagation
 through conventions; cov measurement band; closure band) — never
 reused constants. CORNER KAT armed before first decisive use.
 REJECTOR four limbs (convention spread; matching non-degeneracy;
 migrating patch pattern; E_theta beyond scale). OUTCOMES: collapse
 CERTIFIED (data class + Pa named, never extrapolated) or departure
 MEASURED (magnitude ± bar, axis attributed) — both honest; bar
 widening or convention choice post hoc = protocol violation.

------------------------------------------------------------------------------
## 6. PROPOSED M0/REGISTRY DELTAS (paste-ready; EXECUTION DEFERRED —
## S-GAUNTLET non-interference: this session touches no shared doc;
## the F line (or a user-ordered absorption step) executes them)

 DELTA-A1 [T-T3-SI] block after T-T3-CE (M0 ~line 566): the §2 text
  above with the discharge corrections (tier-1 THEOREM with Gibbs
  closure note; tier-2 THEOREM* with the judge-added cap labeled;
  detector with pinned carrier name; the four PROVIDED-conditions
  satisfied in the same edit).
 DELTA-A2 M0:522 Lemma A annotation: THERMAL PIN of record (ideal
  gas, frozen composition; rho = p f(T) Gibbs-collapses; fails for
  co-volume/virial/tabulated EOS).
 DELTA-A3 claims_registry.yaml:264 T-T3 scope: replace "Lemma T3-A
  EOS-general across shocks" (inflation) with the Gibbs-corrected
  scope; ADD T-T3-SI entry (falsifier = X-T3SI-conv rejector); fix
  the P1_sections_2_4:229-232 "ARBITRARY frozen EOS" echo.
 DELTA-A4 [T-T3-MAP] block (T2 judge DELTA 1, with §3's corrected
  wordings for a-B3/c0/W2) + choking-advisory 2-ter(a) correction
  (T2 judge DELTA 2) + Stechmann anchor corrections (DELTA 3) +
  CARRIER-A..E + X-T3SI-conv registered as named F-line dispatch
  items; H3-cl added to the D-CONTRACT vocabulary (D2.4).
 DELTA-A5 [X-T3CTRL] protocol registration in M0/D6 (§5).
 DELTA-A6 hypothesis-ledger rows: H1-T (NECESSARY; Noble-Abel
  known-answer rejector owed), H-OBJ (NECESSARY at value level,
  WEAKENED at argmax level via T-O1), H-F1 tier-2 cross-link, H-CON
  constraint-class scope row.

------------------------------------------------------------------------------
## 7. JUDGE-ADDED / UNADJUDICATED CLAUSE REGISTER (never quote as
## converged)

 1. T1 tier-2 Lemma B across-shocks cap — judge-added (conservative;
    stands as a cap; promotion condition named).
 2. T1 detector hypothesis-set ENUMERATION {H1-T,H2',H3-p,H4,H-OBJ} —
    judge-enumerated expansion of the refuter's "tier-1+vacuum set".
 3. Carrier name "X-SICONV" — judge rename of expert-1's X-T3SI-conv;
    pin ONE name at registration (recommendation: X-T3SI-conv).
 4. T2(e) full-H1-H4 shape-argmax refinement — judge-derived THEOREM*,
    refuter-corroborated at discharge, still owes its formal refuter
    pass in the H-F1-qualified form; EXCLUDED from registration.
 5. T2(e) W2 original judge completion — SUPERSEDED by the discharge
    correction (§3(e)); must not ship.
 RETIRED at discharge: the T1 judge's "JUDGE-ADDED" marker on the
 T-O1 qualifier (the full refuter DID state it in compressed form);
 the T2(d) universality demotion and detector-block adoptions are
 verified faithful on full text.

------------------------------------------------------------------------------
## 8. OPEN ITEMS (inherited + new, deduplicated)

 - Lemma B across-shocks adjudication (tier-2 promotion condition).
 - K2 argmax audit / design-map monotonicity lemma (a-B1 promotion).
 - a-B2 separation-margin carrier leg OWNERLESS -> F3 entry decision.
 - a-B3 hypothesis-exit lemma (SCHEMA -> THEOREM* repair).
 - CARRIER-B J1 representability audit ((b) shift CONJECTURE).
 - Five-field symbolic KATs BOTH identities (c0 promotion).
 - bounds.py axial-vs-total rung + family-selection bookkeeping term
   (missing executables of record).
 - H3-cl realizability on one ingested dataset ((d)).
 - mu(Xi_sub)>0 genericity: needs a second independent dataset.
 - Pressure-band -> Isp-band transfer coefficient (OPEN/SCHEMA).
 - S18 five-line hypothesis audit (named precondition, §4(I)).
 - Harroun averaging convention (settleable only by correspondence/
   re-computation); P-M "no net swirl" computed-or-asserted; panel
   falsifiers F1-F4 + A4 never run by anyone (empirical vacuum).
 - Novelty: [T-T3-SI] needs its own query-bounded delimiter at
   registration; G2 bound stands on its old queries.

R4 NOTE: this advisory IS the same-session theory landing (R4) for
Campaign A; the M0/registry deltas are staged in §6 for execution by
the line that owns those files.

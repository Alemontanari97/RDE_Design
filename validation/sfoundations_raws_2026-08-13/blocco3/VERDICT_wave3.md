# VERDICT_wave3 — S-FOUNDATIONS-C3 BLOCCO 3 WAVE 3 JUDGE OF RECORD
# Date 2026-08-20. BASE = validation/sfoundations_raws_2026-08-13.
# Slots: FAM (C34/C35/C36/C41/C42/C43) | C50 (Form-2 solo) | CONV
# (C4/C17/C18/C24/C25/C38 verification) | REMMARCH (C5/C6/C8/C10/C12/
# C13/C14) | REMENG (C16/C19/C22/C37/C39/C40/C44/C45) | REMPOL
# (C7/C26/C29/C30/C47). Mandate: BRIEF_wave3_refuter_judge.md WAVE
# JUDGE section + BRIEF_wave2_refuter_judge.md JUDGE (verbatim, incl.
# §0.1 source-verification) + BRIEF_wave1_judge.md protocol VERBATIM.
# This judge writes ONLY this file. No registry/doc of record is
# edited; every delta below is a PROPOSAL the landing window executes.

## 0. NULL=FAILURE CHECK — PASS (12/12)

All six panels present and well-formed with machine summaries at EOF
(PANEL_FAM.md 703L, PANEL_C50.md 479L, VERIF_CONV.md 420L,
PANEL_REMMARCH.md 777L, PANEL_REMENG.md 826L, PANEL_REMPOL.md 851L);
all six refutations present and well-formed with machine summaries
(refute_FAM.md 394L, refute_C50.md 471L, refute_CONV.md 269L,
refute_REMMARCH.md 384L, refute_REMENG.md 398L, refute_REMPOL.md
379L). No slot is UNVERIFIED; every cluster is adjudicable this wave.

## 0.1 JUDGE SOURCE-VERIFICATION DECLARATION (spot checks run in THIS window)

Top load-bearing anchors re-verified at the file by this judge
(Read/Grep, this window), at least two per slot:

- FAM: a1_toc_variational_jax.py:1741 `Dv = Dv/np.median(Dv)` —
  CONFIRMED (median(Dv) == 1 identically; R3FAM-4(i) witness holds);
  a1_toc:2224 `tol_dp = A1.K_RICH * (abs(d1-d2) + ...)` — CONFIRMED
  (R3FAM-2's embedded-K witness holds).
- C50: phaseB_tree_diff.md:288-293 — CONFIRMED carries the
  Giles-Pierce/front-motion adjoint content; :330-335 — CONFIRMED is
  the certified-solution-class item (no adjoint front-term): the
  R3C50-6 mis-cite is real.
- CONV: the disputed Q10 grep re-run by this judge
  (`grep -inE "critical cone|B-stationar" docs/*.yaml`): **8 hits
  across 4 registry files** — choice_ledger :421/:534/:539, claims
  :1350/:1874, findings :1136/:1947, glossary :1126. VERIF_CONV's
  "3 locations" is incomplete (R3CONV-7 sustained); the refuter's
  "five registries" is itself a one-off — it is FOUR files, eight
  hits (corrected below). claims :1350 ("B-stationarity qualifier
  until O1", S22) and :1874 ("B-STATIONARITY qualifier (O1
  undischarged)", S24) verified verbatim = the pre-wave-1 carriers.
- REMMARCH: a1_ideal_march_jax.py:1082-1085 — CONFIRMED every row-j2
  exit-line cell is built with the imposed uniform state `qq`
  (F-C14-1 metric ≡ 0 as pinned; R3REMMARCH-1 holds); a1:853-862
  (mdot by Simpson on the Sauer IVL) + :864-879 (Me from
  leggeAree(mdot, eps)) — CONFIRMED (the R3REMMARCH-2 mdot common
  mode is structural).
- REMENG: a1:868-872 `q0 = qs[idx[-1]] if idx.size else
  float(as_)*1.8` — CONFIRMED silent empty-bracket fallback
  (R3REMENG-13 holds); findings :599-607
  (engine-core:F7-legge-bracket-fallback, owner prescription
  verbatim) and :608-616 (engine-core:F8-cert-scale-unit-mixing,
  "~3 decades looser", "no verdict compromised") — CONFIRMED
  (R3REMENG-4/-13 hold); a1:433-448 — CONFIRMED the certification
  metric is the UNDAMPED NEWTON STEP norm vs NEWTON_TOL_FACTOR*EPS*sc
  (R3REMENG-1 holds).
- REMPOL: adaptive_knot_optimize.py:24-68 — CONFIRMED "the indicator
  is a refinement driver, not a verdict row" (:26), Doerfler bulk
  marking + budget cap (:29-34), warm-start deviation "MEASURED and
  printed" (:46-48), per-cycle gates list contains NO
  representation-deviation band, and the [D3] derived stopping floor
  tol_stop = K_RICH*|rel(r=1)-rel(r=2)| EXISTS at :50-54 (the exact
  binding R3REMPOL-1 proposes); findings :573-581
  (engine-core:F3-table-clamp-silent) — CONFIRMED "CONFIRMED LIVE
  S21: the [X-VMON] KAT-B first range left the box and measured
  lam_ad -0.216 vs -1.185 at M ~ 4.7" (R3REMPOL-3 holds: the panel's
  "no known out-of-box march state on committed records" is false).

No refuter witness failed judge re-verification. No panel quote
relied on below was found misquoted beyond the mis-cites the refuters
already logged.

## 0.2 DRY CRITERION AND ESCALATION POSTURE (stated up front)

The wave is **NOT DRY**: 21 REPAIRS are sustained (0 BREAKS). Every
sustained repair has a named, text-level repair which this verdict
ADOPTS on the page (adjudicated repair text carried to the landing —
no extra rounds); therefore ZERO rows auto-escalate under the
standing rule ("sustained REPAIR that cannot be repaired-by-amendment
on the page"). One STRUCTURAL escalation exists by user order,
independent of this rule: **C50 escalates to full Form-2 regardless**
(BRIEF_wave3_depth_addendum.md D1 — runs AFTER this verdict, consumes
it; VERDICT_C50_form2.md will be THE C50 authority of record and
supersedes this verdict's C50 delta if they differ). The D2 REM depth
pass also runs unconditionally after this verdict per the same
addendum. Confirm-on-repairs instance 2 verifies every repair text
sustained here (its brief scope (a)) — the stage is ALWAYS-ON of
record (instance-1 catch CR-W2-1).

---

# §1 FAM — DERIVED-CONSTANTS FAMILY (C34, C35, C36, C41, C42, C43)

Refuter findings adjudicated (17): R3FAM-1 SUSTAINED (REPAIR); -2
SUSTAINED (AMENDMENT); -3 RECLASSED NOTE→AMENDMENT (folded into duty
text); -4 SUSTAINED (REPAIR; judge re-derived the extremal: with
W = Dv∘u a u-radius r leaves W-steps up to max(Dv)·r unresolved, so
the safe scalar form is xtol_u ≤ floor_W/max(Dv), and for a
premature-stop-risk tolerance the safety factor DIVIDES — all three
defect legs hold, :1741 verified); -5 SUSTAINED (AMENDMENT,
PANEL-DERIVED label per the C33 precedent); -6 NO-ATTACK accepted
(scope correct, count 7+1 reproduced); -7 SUSTAINED (AMENDMENT); -8
NOTE accepted (h2 clean); -9 SUSTAINED (REPAIR; judge re-derived
K·r/(r+1): at r=K_RICH=4 coverage 3.2x vs intended 4x = 20% erosion;
r ≥ (1-eps)/eps exact; the 19:1 D-prime datum = 5% line — arithmetic
correct); -10 SUSTAINED (AMENDMENT, tighten P1 — conservative
direction); -11 SUSTAINED (REPAIR; the valve condition genuinely
fails as written: p_obs at deployed sites is the PENDING measurement,
and roles 4/5 invert the conservativeness direction); -12/-13
NO-ATTACK accepted (census reproduced 107/17; C43 legs re-run; the
:1182-vs-:1185 anchor nit carried); -14 SUSTAINED (AMENDMENT); -15
SUSTAINED (AMENDMENT); -16 NOTE sustained (command fixed to -E form;
result true); -17 NOTE sustained (the judge does NOT consume
`alternatives_closed: 14` as a measured count).

### 1.1 C34 — TR floor/caps. VERDICT: ADJUDICATED-SPLIT (panel outcome STANDS with 2 adopted repairs/amendments)

Final delta = PANEL_FAM §4.1 text WITH these adopted modifications:
1. (R3FAM-1 repair, adopted) The immateriality branch reads:
   "immateriality branch: no accepted step within M×
   of either literal, with M = 10 DECLARED sufficient-not-optimized
   (direction argument: larger M makes immateriality HARDER to claim
   = conservative; M = 10 > K_RICH = 4, the registered safety
   constant) — or M derived from the measured rho-histogram support
   width at duty time, superseding the declaration."
2. (R3FAM-2 amendment, adopted) The protocol pin declares the
   embedded safety: "NOTE: tol_dp is itself K_RICH-banded at source
   (a1_toc:2224), so TR_FLOOR_derived = K_RICH × tol_dp/||g||_seg
   carries K_RICH² ≈ 16× on the raw two-point spread — DECLARED as
   the intended compounded safety; the duty window may substitute the
   raw spread with a single declared K. This composition instance is
   NOTIFIED to C41 (a P-tag applies at composition time) and to the
   C42 role census."
3. (R3FAM-3, adopted into duty text) F2-C34-TRFLOOR-DERIVE carries:
   "an engine swap at [P-IPADJ] re-prices the rho-histogram
   accept/reject semantics — re-check at that landing."
Falsifier, duty, dependencies, what-would-overturn: as PANEL_FAM §4.1.

### 1.2 C35 — xtol. VERDICT: ADJUDICATED-SPLIT (outcome STANDS; pinned formula REPLACED by the adopted repair)

Final delta = PANEL_FAM §4.2 text WITH:
1. (R3FAM-4 repair, adopted verbatim) The pinned derived form is
   REPLACED by: "xtol_u = floor_W/(K_RICH × max(Dv)): floor_W (the
   C20-window Newton floor) propagated component-wise through the
   driver's actual W = Dv∘u map, EXTREMAL (max-Dv) direction, safety
   factor DIVIDING (premature-stop is the declared material risk).
   Note of record: the driver normalizes Dv by its own median at
   construction (a1_toc:1741), so any median-based form is vacuous."
   Arithmetic executes in the existing findings-:640 owner window
   (unchanged).
2. (R3FAM-5 amendment, adopted) The formula carries the label
   "PANEL-DERIVED arithmetic (C33 precedent, VERDICT_wave2 §2.3) —
   tree convergence is on the derivation DUTY (O-F25(e)/H-F40
   gradient-side forms), not on this step-scale formula."
Falsifier (negative control), duty (rides findings :633-641 owner
window), dependencies (C20/C18 seam; C36 Dv-map link), and the
FOUND-prose-refutes-label finding: as PANEL_FAM §4.2 (all stand).

### 1.3 C36 — Scaling policy. VERDICT: CONVERGED-panel (outcome STANDS; falsifier re-pinned)

Final delta = PANEL_FAM §4.3 text WITH (R3FAM-7 amendment, adopted):
F-C36 falsifier comparison object PINNED: "refreshed-vs-frozen twin
on the S18 record case compares (a) certificate validity AT EACH
WALK'S OWN endpoint, (b) replay-fidelity/determinism bit-check
(findings :1261 rides), (c) same-base same-seed segment-level
comparison for the scaling-sensitivity claim. A genuine REJECT =
band violation or determinism break — NOT endpoint divergence
(path-dependence of a nonconvex driver is not a refresh defect)."
H^s option-with-stated-precondition, duty F2-C36-DVREFRESH, C32
re-price clause: as PANEL_FAM §4.3.

### 1.4 C41 — Band form/composition. VERDICT: CONVERGED-panel (P1-P4 policy STANDS with P1 tightened and P3 carrying its derived bound)

Final delta = PANEL_FAM §4.4 text WITH:
1. (R3FAM-9 repair, adopted) P3 reads: "max PERMITTED only with a
   recorded dominance certificate r = top/runner-up ≥ K_RICH,
   CARRYING its derived coverage bound K·r/(r+1) and the accepted
   erosion DECLARED (at the threshold r = 4: coverage 3.2× vs
   intended 4× = 20% erosion, sufficient-not-optimized, direction
   stated: higher threshold ⇒ less erosion; an erosion budget eps may
   replace the declaration via r ≥ (1−eps)/eps — the 19:1 D-prime
   datum sits at the 5% line)."
2. (R3FAM-10 amendment, adopted) P1 reads: "components with MEASURED
   or STRUCTURALLY PROVEN independence → RSS (GUM); a merely stated
   argument routes to P2 (conservative direction; this honors the
   pre-registered criterion — the O-F25 'per correlation argument'
   advocacy is noted, not adopted, as the weaker form)."
Falsifier, duty F2-C41-BAND-POLICY, dependencies: as PANEL_FAM §4.4.
NOTIFICATION consumed: the C34 K² instance (§1.1 item 2) is a live
P-tag case for this policy's first pass.

### 1.5 C42 — K_RICH role reuse. VERDICT: ADJUDICATED-SPLIT (ordered per-role program STANDS; interim-validity hypothesis RESTATED per adopted repair; role census +1 notified role)

Final delta = PANEL_FAM §4.5 text WITH:
1. (R3FAM-11 repair, adopted verbatim) The interim validity statement
   is REPLACED by: "interim validity restated honestly: role-1
   (two-resolution Richardson) sites stand under the wave-1 interim
   regime's OWN checkable mechanism (VERDICT_wave1 §2.4: pre-F2
   band-bearing verdicts run the already-built [X-O32] estimator at
   their own sites or declare the row trigger fired) — NOT under a
   blanket conservativeness hypothesis; roles 2/3/6/7/8/10 interim
   validity = the per-role structural declarations of the ordered
   program, pulled forward explicitly as DECLARED-INTERIM (one line
   each at the audit's first window); roles 4/5 (delta_inst =
   min_margin/K_RICH, thr = m_ref/K_RICH) have INVERTED direction
   (larger K = smaller floor) — 'K = 4 conservative' is not
   well-defined for them and no blanket claim is made."
2. (Cross-slot reconciliation, judge) Role-census note delta
   CORRECTED to: "measured 2026-08-20: 107 .py sites / 17 files; 10
   functional roles (9 certificate-bearing + timing declared
   out-of-scope) + **3 notified pending** (C27 w/red-line, wave-1;
   C21 omega-in-z, wave-2; **C8 dev_warm arming floor — wave-3
   REMMARCH notification, PANEL_REMMARCH §4.3, binding**)." The FAM
   census predates the same-wave C8 notification; the census count
   must carry it.
3. Reverse conditionality (from R3REMMARCH-6(i), judge-carried here):
   the C8 arming floor consumes whatever per-role constant the
   F2-C42-KRICH-ROLE-AUDIT lands for that role — derived constant
   substitutes the literal on landing.
Ordered duty F2-C42-KRICH-ROLE-AUDIT, falsifier (published-route
Fs(p_obs) > 4 forces the derived constant), dependencies: as
PANEL_FAM §4.5.

### 1.6 C43 — Asymptotic-range handling. VERDICT: CONFIRM-ALIGNMENT PASS (unchanged)

Final delta = PANEL_FAM §4.6 note-append verbatim, with the anchor
corrected to findings :1182-1190 (row starts at :1182 — R3FAM-13
nit). No status change (MIXED stands), no duty minted. No escalation.

### 1.7 FAM slot census hygiene (adopted amendments)

(R3FAM-14) The "Optim.Eng. 2026 noisy-nonsmooth TR" item is STRUCK
from §2.2 and from the census_recency string (recency garnish with no
one-liner/marker); the span honestly ends 2024/2025. (R3FAM-15) The
SNOPT scaling identity is RE-ANCHORED to findings :1261 ("constraint-
row equilibration (SNOPT lineage)" — registry-carried identity), the
source marked [TITLE]. (R3FAM-16) The cava sweep command is recorded
in its executable -E form (result reproduced true, 6 hits, closure
stands). Escalations from FAM: NONE.

---

# §2 C50 — DATUM-SPACE METRIC (Form-2 solo)

Refuter findings adjudicated (13): R3C50-1 SUSTAINED (REPAIR; judge
re-derived the letter-of-criteria walk: L¹ solo passes S1 via the
computable ‖Λ‖_L∞(A) dual, S2 via the adjoint trace, S3 via the C7.2
TEST — so the frozen firing condition is FALSE as written and the
actual discriminator (sharpness / tie-rule non-vacuity) was applied
post-hoc; the repair makes it a criterion, which the interval-
separation obligation of record legitimates as WELL-POSEDNESS, not
preference); -2 SUSTAINED (REPAIR; the F-2 jump-set RH/entropy audits
are genuinely not L¹-continuous — sharp-vs-smeared front at small L¹
distance is a valid counterexample); -3 SUSTAINED (REPAIR; C7.2's own
":628-629 imposed dual regularity" makes the unconditional
"impossible by construction" an over-claim); -4 SUSTAINED (REPAIR; R5
rigor-class discipline — theorem_ledger :232-239 pins multi-D
shift-differentiability as practice-without-theorem); -5 SUSTAINED
(REPAIR; for d_acc = L¹ the misalignment cost is Σ|[q]_k|·δ_k — the
panel's own §3.1(d) computation; O(jitter×slope) is the [DATA]
amplitude-masquerade formula, wrong slot); -6 SUSTAINED (AMENDMENT;
judge-verified at source: content lives at diff :288-293, not
:330-335 — fix at all four sites); -7 SUSTAINED (AMENDMENT; the 1-D
phase alignment IS a datum-space optimization — honest form adopted +
N-fold ambiguity hazard named for the F2 alignment spec); -8
SUSTAINED (AMENDMENT; penalty-role vs metric-role demotion — the √δ
computation carries A2 alone, independently re-derived by the
refuter); -9 SUSTAINED (AMENDMENT; BINDING — the :2316 finding's own
trigger is "first unsteady-generator ingestion", which can precede a
real-data family: FA-2 must arm at the EARLIER of the two named
triggers); -10 SUSTAINED (AMENDMENT; union tuple shape owed to the F2
duty + the L∞-guard ROLE clause); -11 SUSTAINED (AMENDMENT; grep
commands+counts appended; the displacement-amplitude census lead is
[MEMORY]-depth — carried as a delta-census CANDIDATE for the D1
advocates, citable only after verification per
litreview-verification-protocol); -12 NOTE sustained (adopt the
one-line C56-decided-of-record fix — d_sens's delivery route exists
of record); -13 SUSTAINED (AMENDMENT; datum window W and M0 W1-W4 are
distinct objects — split bullet adopted).

### 2.1 C50 VERDICT: ADJUDICATED-SPLIT-BY-ROLE — outcome STANDS with 5 adopted repairs; STRUCTURAL Form-2 escalation per D1 (user-ordered) declared

Final wave-3 delta = PANEL_C50 §4.1 delta text WITH these adopted
modifications (this text is the wave-3 proposal; **VERDICT_C50_form2.md
supersedes it if different** — the landing applies THAT file's delta
per the depth addendum):
1. (R3C50-1) Criteria block carries S1′: "the sensitivity constant
   must be the actual dual pairing against the perturbation class
   (sharp), not a worst-case-per-unit-mass envelope; conservatism
   that predictably drives the tie rule vacuous fails S1′." Under
   S1′ the split's firing condition IS discharged (L¹ solo fails
   S1′; calibrated-L² solo fails A2): the adjudicated content
   already decides it — criterion-text repair, no re-adjudication.
2. (R3C50-2) A1 clause SCOPED: "A1 (d-continuity) holds for the
   FLUX-INTEGRAL audit class; the F-2 datum-side moving-RH/entropy
   audits (findings :1650-1659, same F2 window) are DECLARED
   REPRESENTATION-LEVEL checks on the delivered reconstruction +
   declared front set ([DATA] Def 7.1, 'rejected administratively'),
   OUTSIDE the d-continuity claim. ALTERNATIVE FORM handed to the D1
   closure judge: product-form acceptance (L¹ on fields ⊕ declared
   jump data), which mirrors d_sens's smooth ⊕ front-block structure
   — the D1 judge picks; the F2 duty must state which."
3. (R3C50-3) Seam clause CONDITIONALIZED: "seam holds under the
   declared regularity: Λ ∈ L∞(A) (C7.2's imposed dual regularity),
   G ∈ L∞ on the smooth complement, front sensitivities finite —
   contract-side declarations verified at instantiation
   (F2-C50-CONTRACT-METRIC), FS-1/FS-2 the live falsifiers." The
   words "impossible by construction" are struck.
4. (R3C50-4) Rigor clause ADDED to the delta text: "front-block
   sensitivities carried at the record's declared rigor:
   shift-differentiability rigorous in 1-D, practice-without-theorem
   in multi-D (theorem_ledger :235; G12 R-G12.2 to-verify); FS-2 is
   the live empirical guard on exactly this gap."
5. (R3C50-5) FA-2 predicted drop := Σ_k |[q]_k|·δ_k over the declared
   jump set (jump-mass × alignment shift); the O(jitter×slope) form
   retained only as the finite-slope-representation reading.
6. (R3C50-9) Duty arming: "FA-1/FA-2/FS-1/FS-2 armed at the EARLIER
   of: F2 contract freeze / first imported real-data family
   (findings :1668) and first unsteady-generator ingestion
   (findings :2324 — FA-2's natural arming point)."
7. (R3C50-10) F2 duty tuple clause: "the contract tuple = [DATA]
   Def 7.1's six slots (Q̂, (N,Ω), χ, U, W, 𝒫) with d/ε/W semantics
   per [PDE] D7.1; the L∞ guard is adopted in the [PDE] ROLE (class
   side condition), converged-on-object with [DATA]'s norm-pair
   member."
8. (R3C50-6/-7/-8/-12/-13) Text amendments as sustained above
   (anchor :288-293 at all four sites; OT reason 1 honest form +
   N-fold hazard named to the F2 alignment spec; Freitag demoted to
   supporting-by-analogy; C56 decided-of-record one-liner; W vs
   W1-W4 bullet split).
Falsifiers FA-1/FS-1/FS-2/F-TIE: as PANEL_C50 §4.2 (verified
genuinely rejecting; FS-2 is first-class). Duty
F2-C50-CONTRACT-METRIC: as §4.3 with items 6-7 above. Dependencies +
what-would-overturn: as §4.4 with the C56 fix.
HANDOFF TO D1 (binding): the D1 advocates + closure judge consume
THIS section; open items handed: the A1 form choice (item 2), the
displacement-amplitude delta-census candidate (R3C50-11(3),
verification-gated), the Métivier optional enrichment
(arXiv:2101.00904).

---

# §3 CONV — CONVERGENT BATCH VERIFICATION (C4, C17, C18, C24, C25, C38)

Refuter findings adjudicated (8): R3CONV-1 SUSTAINED (REPAIR —
absence claimed at full-tree depth, held at condensed depth; the
refuter COMPLETED the sweep: 9 'knot' hits across the four FULL
trees, none a placement law; zero hits on jupp/free-knot/curvature
— claim TRUE, now properly earned); -2 SUSTAINED (AMENDMENT; the
findings :221 family is C18's, N_NEWTON explicitly excluded); -3
SUSTAINED (AMENDMENT; guard-cap clause is panel synthesis — label
it); -4/-5/-6 NO-ATTACK accepted (C18 seam verified 3-anchor; C24
dedup reproduced with the stray :968 immaterial hit noted; C25
anti-inflation exemplary); -7 SUSTAINED (REPAIR; judge re-ran the
grep: 8 hits / 4 registry files — see §0.1; the consumption notice
must carry the pre-wave-1 carriers claims :1350/:1874); -8 SUSTAINED
(AMENDMENT; declared arithmetic replaces the decorative grep
comment — count 7 verified correct by enumeration).

Per-row verdicts (all six panel verdicts STAND):

- **C4: CONFIRMED-CONSISTENT + note-delta**, with (R3CONV-1 repair,
  adopted): the note's silence parenthesis reads "(measured full-tree
  sweep of record: 9 'knot' hits across the four FULL trees, none a
  placement law — opt :367/:430/:432/:467/:480/:1653, var :972, prop
  :778/:786; zero hits for jupp|free knot|free-knot|curvature-based|
  abscissa; refute_CONV.md R3CONV-1 completion consumed as the
  measurement)". Rest of the VERIF_CONV §1 delta verbatim.
- **C17: CONFIRMED on convergence; owner delta STANDS** ("AUDIT F5
  execution (S25)" → F2, C43/C21 bookkeeping-alignment precedent),
  with (R3CONV-2) the support clause reworded ("the sibling C18
  family is already F2-owned at findings :221 — same alignment
  class") and (R3CONV-3) the note's guard-cap clause labeled
  "(panel-proposed composition, not tree content)". Rest verbatim.
- **C18: CONFIRMED-CONSISTENT + note-delta** verbatim (VERIF_CONV
  §3): More-Wild blindly re-derived at O-F25(c); GAP-29 anchors
  verified; C20-Tier-1 seam consistent at all three anchors.
- **C24: CONFIRMED-CONSISTENT + cross-ref note-delta** verbatim
  (VERIF_CONV §4); dedup verdict (diff §2.6/§2.7 already homed at
  findings :1615/:1624, nothing to mint) CONFIRMED.
- **C25: CONFIRMED-CONSISTENT + note-delta** verbatim (VERIF_CONV
  §5) with the 1/4-tree core-of-alternative support scope recorded.
- **C38: CONFIRMED-CONSISTENT + consumption-notice note-delta**,
  with (R3CONV-7 repair, adopted): (a) the Q10 protocol row corrected
  to the measured census "8 hits / 4 registry files (ledger
  :421/:534/:539; claims :1350/:1874; findings :1136/:1947; glossary
  :1126 — judge re-measured 2026-08-20)"; (b) the consumption notice
  extended: "; qualifier semantics already live pre-wave-1 in
  committed claims (claims_registry :1350 S22 corner-metric
  corollary, :1874 S24 F1b twin, both 'until O1') — the declaration
  policy must compose with these carriers too, not only with
  [P-BSTAT]/[P-CERTKS]". Landing priority note (prevents a future
  re-mint) stands.
- Batch machine-summary comment (R3CONV-8): replaced by "6 note
  appends + 1 owner change, enumerated per-row".
Escalations from CONV: NONE.

---

# §4 REMMARCH — MARCH/GEOMETRY REMAINDER (C5, C6, C8, C10, C12, C13, C14)

Refuter findings adjudicated (12): R3REMMARCH-1 SUSTAINED (REPAIR;
judge-verified at a1:1082-1085 — F-C14-1 as pinned can never fire:
vacuous rejector, D-47/R5 class, false premise under the valve); -2
SUSTAINED (REPAIR; judge-verified the mdot→Me common mode at
a1:853-879 — the displaced-restart rejector is blind on that channel
by construction, failing the panel's own frozen criterion on one
channel); -3 SUSTAINED (AMENDMENT; displaced-start operational pin);
-4 SUSTAINED (AMENDMENT; (dv/dy)_axis operand must be defined); -5
SUSTAINED (AMENDMENT; o33 cfg has no Ne field — protocol must name
NI/da_deg/Nw; Fidkowski-Darmofal on-disk closure line owed); -6
SUSTAINED (AMENDMENT; reverse K_RICH conditionality — carried into
C42 §1.5 item 3 — and V-F7 citation demoted); -7 SUSTAINED
(AMENDMENT; G5 corrected to -E form with hits :407/:1290 — conclusion
survives; G2 declared "4 hits, 2 relevant"); -8 SUSTAINED (AMENDMENT;
F-C6-1 inconclusive branch + the de Casteljau object named); -9
NO-ATTACK on C5 accepted (code-verified nesting, honest materiality);
-10 SUSTAINED (AMENDMENT; four anchor corrections: GAP-8 :1173-1181,
GAP-6 :1155-1163, wanted_eca_hoekstra :852-853, insertion_site
:197-213); -11 NOTE sustained (wording "census evidence recorded (Q3
2026-08-20)" replaces "ranking" — the F4b/F5 owner inherits evidence,
not a verdict); -12 NOTE (h2 PASS) accepted.

Per-row verdicts (all seven panel outcome classes STAND):

- **C5: ADJUDICATED-CONVERGED-KEEP** — PANEL_REMMARCH §4.1 verbatim
  (monitor-armed; GAP-34 measured immateriality; F-C5-1 with derived
  threshold + S18 replay control). No sustained attack.
- **C6: ADJUDICATED-SPLIT (guard-object flip; single-author residue
  DISCHARGED by panel+refuter = the owed dual-proof half — the flip's
  evidentiary base survived genuine attack)** — §4.2 WITH (R3REMMARCH-8):
  F-C6-1 gains the branch "if the incumbent guard ALSO rejects the
  synthetic control, instantiate the control at the GAP-23 trigger
  configuration (Nw≥240 / max_ins≥3) where the degradation law admits
  it, or declare the separation not reproduced"; the O-F8 fallback
  names its object: "de Casteljau certified subdivision = a
  Bernstein-form bound on cardinal amplitude over the knot interval".
- **C8: ADJUDICATED-CONVERGED** — §4.3 WITH (R3REMMARCH-6): (i) the
  seam clause "floor constant rides the C42 role-census outcome; a
  derived per-role constant substitutes on landing" added; (ii) the
  V-F7 citation DEMOTED (fold margins do not bear on re-representation
  exactness; O-F32 + the findings-row theorem + measured P3 carry the
  arming case — no double-counted advocacy). K_RICH role notification
  to FAM/C42 CONSUMED (§1.5 item 2).
- **C10: ADJUDICATED-SPLIT** — §4.4 WITH (R3REMMARCH-5): F-C10-1
  names the REAL fields "the three single-direction refinements at
  r=2: NI (IVL rows) / da_deg (arc angle) / Nw (contour-exit
  stations) — o33_bench cfg fields of record (no Ne field exists)";
  census closure line added: "Fidkowski-Darmofal 2011 (on disk):
  output-based adaptation review — not consumed here by stated
  reason: C9 mesh law and C11 estimator are landed authority; the
  diagnostic-vs-production split is not touched by it (materiality
  LOW)". Delta anchor ":850" corrected to ":852-853".
- **C12: ADJUDICATED-PROTOCOL** — §4.5 WITH (R3REMMARCH-2 repair,
  adopted; option (a) preferred with (b) as declared floor): "the
  composed band CARRIES a declared mdot-channel term — the
  Kliegel-Levine second-order mass-flow correction EVALUATED as a
  band term (formula evaluation feeding a bar; NOT an adoption of the
  higher-order start — F4b/F5 scope clause untouched). If the
  evaluation proves non-cheap at the duty window, the declared
  MINIMUM is the named exclusion: 'F-C12-1 certifies start-line
  invariance of the NET; the mdot→Me common mode is covered only at
  F4b/F5' — the certificate never silently over-claims either way."
  PLUS (R3REMMARCH-3): "displaced start = the marched data on column
  +3 taken as the new IVL; the fan is rebuilt from it." PLUS
  (R3REMMARCH-11): "census evidence recorded (Q3 2026-08-20)"
  replaces "census ranking RECORDED ... presumptive first candidate".
  F-C12-2 vacuousness control stands (it covers the net channel; the
  mdot term/exclusion covers the other — stated in the delta).
- **C13: ADJUDICATED-PROTOCOL (single-author residue DISCHARGED as
  for C6)** — §4.6 WITH (R3REMMARCH-4): F-C13-3's operand pinned:
  "(dv/dy)_axis estimated by two-NI Richardson of v1/y1 (the same
  two-NI data F-C13-1 orders) or by the H-F19 one-term series
  coefficient fitted on recorded off-axis cells (v = a1·y + O(y³)) —
  either estimator declared before first use". Swirl obstruction
  stays NAMED-not-decided with correct homes.
- **C14: ADJUDICATED-CONVERGED** — §4.7 WITH (R3REMMARCH-1 repair,
  adopted verbatim): the sentence "the exit-line row j2 cells are
  ALREADY COMPUTED ... costs a max() over existing values" is STRUCK
  (false premise — those cells carry the imposed uniform state, judge
  verified); F-C14-1 RE-ANCHORED: "primary metric = max_j |M_j −
  Me_ach| over the FINAL MARCHED COLUMN (interior cells G[(j,
  i_exit)], j ∈ (Nv, j2], computed via solver_int), with the
  mass-flow closure residual (mdot1+mdot2 vs mdot, a1:1086-1106,
  already accumulated) reported as the free companion residual;
  threshold-derivation and the mass-flux-weighted fallback clauses
  carry over unchanged." Control-surface identity rejector consumed
  from findings :1588 unchanged.

Duties F2-C5-KNOTDRIFT-MONITOR / F2-C6-GUARD-EDIT / F2-C8-ARM-DEVWARM
/ F2-C10-PERDIR-FLAG / F2-C12-STARTLINE-REJECTOR / F2-C13-AXIS-ORACLE
(+ folded F2-C14-EXITBAND): as the panel, with the amended texts.
Escalations from REMMARCH: NONE (both repairs adopted verbatim on the
page — the refuter's own escalation flag is thereby discharged).

---

# §5 REMENG — ENGINE/DRIVER REMAINDER (C16, C19, C22, C37, C39, C40, C44, C45)

Refuter findings adjudicated (15): R3REMENG-1 SUSTAINED (AMENDMENT;
judge-verified at a1:433-448 — the cert metric is the undamped step
norm, already error-oriented; Deuflhard (3.40) attacks the ACCEPT
rule only); -2 SUSTAINED (REPAIR; F-C16-3 as pinned adopts the
challenger on criterion disagreement alone = post-hoc drift against
the panel's own frozen WIN criteria); -3 SUSTAINED (AMENDMENT; the
0.0 trailing candidate is a DOCUMENTED honest-fail NaN-safety path —
NaN-domain robustness becomes an explicit A/B WIN criterion); -4
SUSTAINED (REPAIR; judge-verified findings :608-616 — the record
disparity is ~3 decades, the panel inverted the F8 row's content, and
F-C19-1 as pinned is immediately-firing-or-vacuous); -5 SUSTAINED
(REPAIR; probe admissibility must bound F-C22-1; plus the
bitwise-wording anchor fix); -6 SUSTAINED (REPAIR; F-C37-1/2
dependency cycle is real — census gated on merge gated on census);
-7 SUSTAINED (AMENDMENT; judge PICKS branch (a): the LSQ referee
(instrument 3) is licensed pre-[P-IPADJ] on RECORDED artifacts —
offline, solver-independent, the panel's own census point;
instruments 1-2 ride [P-IPADJ]; F-C39-3's "until" clause is thereby
coherent); -8 SUSTAINED (AMENDMENT; empty margin-active instance set
today + lambda_e coverage = instrument 3 alone — named honestly,
C40's conditional likelier to fire); -9 SUSTAINED (AMENDMENT;
"elimination WINS" conditioned on the twin's O3.1-style check
PASSING); -10 SUSTAINED (AMENDMENT; N-W §8.1 claim re-marked at depth
held; the [FULL] §8.1 read folds into F2-C44-FDSTEP execution — the
book is on disk); -11 SUSTAINED (AMENDMENT; F-C44-3 pinned to ONE
lowering: FD-on-twin vs CS-on-twin, conclusion scoped to the shared
step/stencil logic); -12 SUSTAINED (AMENDMENT; Moré-Wild 2011/2012
re-marked [TITLE]/of-record — papers-needed already concedes the full
text); -13 SUSTAINED (REPAIR; judge-verified a1:872 + findings
:599-607 — the pinned endpoint rejector misses the DOMINANT recorded
failure path (silent 1.8·as on empty bracket), and the F7 findings
row that owns this exact defect went unconsumed because the dedup
grep pattern lacked its tokens); -14 NOTE sustained (post-repair the
valve use is legitimate; the correctness half is load-bearing, not
bookkeeping — classification carried); -15 NOTE sustained (the judge
does not consume `alternatives_closed: 9` as measured; the §6 dedup
pattern under-design is evidenced by the two missed rows).

Per-row verdicts (all eight panel outcome classes STAND):

- **C16: ADJUDICATED-SPLIT** — PANEL_REMENG §4.1 WITH: (R3REMENG-1)
  both rationale sentences corrected ("the certificate consumes the
  UNDAMPED NEWTON STEP norm vs NEWTON_TOL_FACTOR·EPS·sc
  (a1:433-448) — already error-oriented; the challenger's edge is
  confined to the ACCEPT rule (argmin residual non-increase), which
  is what Deuflhard (3.40) indicts"); (R3REMENG-2 repair, adopted)
  F-C16-3 DEMOTED to an instrument of F-C16-1/2: "NMT-reject/
  argmin-accept events are LOGGED as activation instances and A/B
  evidence; they force the challenger only if correlated with cert
  failures or excess implicit solves above the derived threshold" —
  the "forces challenger regardless of cost" overturn clause is
  struck; (R3REMENG-3) F2-C16-DAMPAB gains the explicit WIN
  criterion: "the challenger build must PRESERVE the documented
  NaN-safety property of the trailing 0.0 candidate (a1:418-423:
  stalled cell keeps its iterate and fails certification honestly) —
  else not apples-to-apples", and the "silent outcome"
  characterization is corrected to "documented honest-fail path".
- **C19: ADJUDICATED-ON-COST (retain scalar)** — §4.2 WITH
  (R3REMENG-4 repair, adopted verbatim): the steelman-against
  sentence is REPLACED by the true record ("component-scale disparity
  of record is ~3 decades — engine-core:F8-cert-scale-unit-mixing:
  position components certified only to ~100 eps|u|; no verdict
  compromised, contour bands Richardson-dominated"); F-C19-1 is
  REPLACED by the VERDICT-LAXITY census: "per certification point,
  laxity_i = sc/max(1,|z_i|) per component, compared against the
  margin by which Richardson-dominated bands absorb it (threshold
  derived from the GAP-29 factor-2 headroom on the
  laxity-vs-band-dominance axis, NOT raw disparity); the duty homes
  into the F8 findings row (F2-C19-SCALECENSUS = that row's owner
  window; no new row)". Outcome (retain on cost) survives on the F8
  row's own "no verdict compromised".
- **C22: ADJUDICATED-SPLIT (burden on the predicate)** — §4.3 WITH
  (R3REMENG-5 repair, adopted): "F-C22-1 probe family BOUNDED to the
  admissible class (knot spacing ≥ the refinement floor of record;
  the [X-AKNO] instance family): IN-CLASS disagreement = predicate
  falsified, challenger becomes certificate-bearing reference;
  OUT-OF-CLASS disagreement = evidence routed to C10/C5 (REMMARCH),
  not a predicate verdict"; anchor fix: the "bitwise" wording is the
  GAP-28 findings DELTA text, the ledger note says
  "compiled...gate-verified".
- **C37: ADJUDICATED-DEFAULT+GATED-LEVER (the N6 right-sized panel
  instance, executed)** — §4.4 WITH (R3REMENG-6 repair, adopted
  verbatim): F-C37-1 gains a MERGE-FREE benign proxy, declared
  sufficient-not-optimized: "benign = flips whose certified-class
  (S,xi) labels are unchanged across the boundary under the adopted
  O-F19/H-F11 loci logging, and/or flips whose discarded-Hessian
  columns are lip-only (the findings-magnitude case of record);
  F-C37-2 licenses the merge on the proxy-flagged subset ONLY; a
  proxy-vs-F-C37-2 disagreement on that subset RETIRES the proxy."
  The census is thereby executable merge-free; the cycle is broken.
  F-C37-3 composition rejector and the [P-QNCARRY] arm-B pin stand.
- **C39: verification half INSTRUMENTS-CONVERGED** — §4.5 WITH:
  (R3REMENG-7, branch (a) adopted) ordering pin reworded:
  "instruments 1-2 land WITH [P-IPADJ]; instrument 3 (LSQ referee)
  is licensed NOW on recorded artifacts (offline,
  solver-independent) — F-C39-3 readings pre-[P-IPADJ] stand as
  demotions-until-explained, exactly as pinned"; (R3REMENG-8) two
  preconditions NAMED: "F-C39-2 has an EMPTY instance set today
  (margin inactive at every recorded instance —
  constraints:margin-constraint-no-hess); it becomes well-defined at
  the first margin-active verdict (= the GAP-12 trigger)"; and
  "lambda_e coverage: instrument 1 is structurally vacuous on
  equalities and instrument 2 needs activity — lambda_e verification
  rests on instrument 3 ALONE, so the C40 conditional is materially
  likely to fire (stated honestly)".
- **C40: ADJUDICATED-CONDITIONAL** — §4.6 WITH (R3REMENG-9):
  "F-C40-1: disagreement with the eliminated twin's O3.1-style
  post-optimality check row PASSING = elimination WINS (provenance
  defect demonstrated); disagreement with the check FAILING =
  INVESTIGATE, no winner declared." Fold into F2-C39-MULTVER stands.
- **C44: ADJUDICATED-SPLIT** — §4.7 WITH: (R3REMENG-10) the N-W §8.1
  support re-marked at the depth actually held ("standard-textbook
  error model, [P-HESSREJ] owner-text citation; §8.1 [FULL] read
  folded into F2-C44-FDSTEP execution — on disk"); (R3REMENG-11)
  F-C44-3 pinned to one lowering: "FD-on-twin vs CS-on-twin (numpy
  twin tier, h=1e-20 instrument of record); conclusion scoped to the
  shared step/stencil logic — the engine-tier transfer is by that
  logic, not by cross-lowering comparison"; (R3REMENG-12) Moré-Wild
  2011/2012 re-marked [TITLE]/of-record in the census.
- **C45: ADJUDICATED-WITH-VALVE** — §4.8 WITH (R3REMENG-13 repair,
  adopted verbatim): the rejector family REPLACES the single endpoint
  rejector: "(a) EMPTY-BRACKET ⇒ LOUD REFUSAL — the silent
  q0 = 1.8·as default (a1:872) dies or is gated; (b)
  boundary-interval bracket ⇒ REFUSE; (c) post-solve supersonic-root
  rejector M(qe) > 1 + derived margin (the F7 audit's named check);
  the idx[-1] last-sign-change ordering hypothesis is LOGGED as a
  named, monitored hypothesis." The duty is HOMED:
  "F2-C45-BRACKETGUARD = the execution of
  engine-core:F7-legge-bracket-fallback's owner prescription
  (findings :599-607: derive the scan window from the table box
  (q_max from h0 − h(T_TAB_LO)) + assert bracket found +
  supersonic-root rejector) — cited, not re-minted; no parallel
  object." (R3REMENG-14) The correctness half is carried as
  LOAD-BEARING (not bookkeeping); post-repair the valve treatment is
  legitimate. F-C45-2 derived-window containment and the dormant H2
  vectorization conditional stand.

Escalations from REMENG: NONE (all five repairs adopted verbatim on
the page).

---

# §6 REMPOL — POLICY/TABLES/MASKS REMAINDER (C7, C26, C29, C30, C47)

Refuter findings adjudicated (11): R3REMPOL-1 SUSTAINED (REPAIR;
judge-verified at adaptive_knot:24-68 — insertion is Doerfler-marked
and budget-capped, the deviation is measured-and-printed, NO
insertion band exists: "the band is the insertion band" is a phantom
reference; the [D3] tol_stop derived floor DOES exist at :50-54 and
is the natural binding); -2 NOTE sustained (grep claim corrected:
zero hits, conservative direction); -3 SUSTAINED (AMENDMENT;
judge-verified findings :576 — a committed record DOES carry a
confirmed live box exit (KAT-B, lam_ad −0.216 vs −1.185 at M~4.7);
the panel's incumbent premise is false and the materiality line
upgrades); -4 SUSTAINED (REPAIR; the ~4ΔT band was derived for
INTERNAL JOINT mollification (S24 survey :250-252), not for the
box-edge exit — derivation-by-transplant, the exact class the panel
itself charges against eps_gate); -5 SUSTAINED (AMENDMENT; three
precision fixes incl. the criterion-(d)-discharged-at-build
declaration); -6 SUSTAINED (AMENDMENT; measured cost carrier added to
F-C29-2 — the acceptance is priced, not asserted); -7 NOTE sustained
(R-4 register entry; working-set analogy = census color, not decision
driver); -8 SUSTAINED (AMENDMENT; the negative-control plant must
guarantee an out-of-overlap True lane, else a correct counter is
falsely refuted; per-call rhythm adopted by name); -9 SUSTAINED
(REPAIR; judge re-derived: a within-count ROLE-PERMUTATION of two
values already present in the file preserves count AND multiset —
"closes the within-count swap surface" is false as stated; the
upgrade SHRINKS the surface, it does not close it); -10 NOTE
sustained (621-vs-639 owner-text reconciliation handed to the landing
window, SR-12 class; ESLint behavioral claim survived source check);
-11 NOTE sustained (alternatives_closed: 12 not consumed as
measured).

Per-row verdicts (all five panel outcome classes STAND):

- **C7: ADJUDICATED-SPLIT (insert+remove direction, end-of-cycle
  sweep, measurement-gated)** — PANEL_REMPOL §4.1 WITH (R3REMPOL-1
  repair, adopted verbatim): the phantom band binding is REPLACED:
  "F-C7-2 band = the [D3] derived stopping floor tol_stop = K_RICH ×
  |rel(r=1) − rel(r=2)| (adaptive_knot:50-54 — the goal-metric noise
  floor, already derived); F-C7-1 retire test carries its OWN derived
  deviation band = the measured dev_warm floor across the recorded
  S20 cycles (the quantity the loop already prints), declared as the
  removal counterpart of the measured-not-gated insertion deviation;
  the §3.1 sentence 'every insertion is gated by derived-band
  machinery' is corrected (insertion is Doerfler-marked and
  budget-capped; the deviation is measured and printed — the
  indicator is a refinement driver, not a verdict row)." Grep claim
  corrected per R3REMPOL-2 (zero hits). Direction, F-C7-3 economy
  carrier, duty F2-DUTY-C7-REMOVALTEST, AFEM rejection, scope clause:
  unchanged.
- **C26: ADJUDICATED (traced box-margin flag + rejector, cert_worst
  pattern)** — §4.2 WITH: (R3REMPOL-4 repair, adopted) "F-C26-1
  verdict threshold RE-DERIVED FOR THE EDGE: margin < 0 + the derived
  probe-excursion allowance (FD probes at P±h are the named near-edge
  consumers, findings :579), OR an explicit one-sided edge
  mollification argument with its own falsifier — the interior-joint
  ~4ΔT band is NOT transplanted (it was derived for piece boundaries,
  S24 survey :250-252); the edge derivation lands in the same C-D
  repair window"; (R3REMPOL-3) the incumbent premise sentence is
  REPLACED: "the box-exit mode is NOT hypothetical — CONFIRMED LIVE
  S21 of record (KAT-B first range left the box, lam_ad −0.216 vs
  −1.185 at M~4.7, findings :576); materiality =
  already-happened-once of record"; (R3REMPOL-5) (i) "the margin
  scalar IS the detector" (the index clip at i = n−2 is also
  legitimate in-box — the clip-event equivalence is dropped), (ii)
  the valve's sufficiency hypothesis carries its one-line check ("all
  table reads route through ht/T: state_q :403-405; invert_h :308"),
  (iii) declared: "pre-registered criterion (d) (demonstrably fires)
  is discharged AT BUILD TIME by F-C26-2 (acceptance rejector)".
  Checkify closure (stated reason verified), F-C26-2/3, duty (the
  standing C-D repair): unchanged.
- **C29: ADJUDICATED-SPLIT (decision rule converged; default =
  segment-level re-freeze; smooth gate = escalation branch only)** —
  §4.3 WITH (R3REMPOL-6): F-C29-2 gains the cost carrier: "measured
  cost report at the replay: N_seg × val_diag rebuild cost vs the
  recorded decisive-run-2-class repeat cost — the acceptance is
  priced, not asserted". F-C29-1/3/4 (incl. eps_gate-derived entry
  condition and C3 detector permanence), duty F2-DUTY-C29-MASKGRAIN,
  C28 gates-absolute consumption, O-F19 single-count declaration:
  unchanged.
- **C30: ADJUDICATED (conservation-of-enforcement invariant,
  one-liner)** — §4.4 WITH (R3REMPOL-8): "F-C30-2 plant must
  GUARANTEE at least one True lane beyond the overlap (a shape change
  whose True lanes all sit inside the overlap yields lost_lanes = 0
  HONESTLY and must not count as refutation); logging adopts the
  EXISTING per-margin_W-call rhythm under mismatch (:679) by name —
  no second event semantics minted." Sequencing note (C30 one-liner
  first — it instruments C29's replay for free) stands.
- **C47: ADJUDICATED (ratchet retained + multiset-fingerprint
  upgrade)** — §4.5 WITH (R3REMPOL-9 repair, adopted verbatim): the
  closure claim is REPLACED everywhere (delta text + machine summary)
  by the honest residual declaration: "the multiset upgrade SHRINKS
  the declared limit from {any within-count literal swap} to
  {within-count PERMUTATIONS of the existing in-file value multiset}
  — value-swaps A→B now FAIL; role-permutations of values already
  present both PASS and are the DECLARED RESIDUAL (documented in
  F-C47-2's rejector exactly as the current docstring declares the
  swap limit); positional/context fingerprints (SARIF
  partialFingerprints proper) = the NAMED upgrade path that would
  close it, not adopted (cost above need)." F-C47-1/3, endpoint
  confirmation (per-file classification, F2-entry owner), closed
  alternatives: unchanged. Landing note (R3REMPOL-10): reconcile the
  F2-entry owner-text "621" against the magnitude's re-measured
  37/639 in the same window (SR-12).

Literature-registry rider (PANEL_REMPOL §4.6) handed to the landing:
Lyche-Morken 1987 [TITLE, WANTED-class], Guest-Prevost-Belytschko
2004 [TITLE], SARIF v2.1.0 partialFingerprints [ABS, spec] — landing
decides inclusion per registry policy. Escalations from REMPOL: NONE.

---

# §7 CROSS-SLOT CONSISTENCY (judge paragraphs)

1. **K_RICH economy (FAM ↔ REMMARCH ↔ REMENG).** One census owner
   (C42), consumers notify — the discipline held: C8's arming floor
   is a NEW notified role (census corrected to 10 + 3 notified, §1.5
   item 2) with reverse conditionality pinned (derived per-role
   constant substitutes on landing); C34's pin was caught composing
   K² undeclared (now declared + notified to C41 as a P-tag case);
   C6 deliberately uses its OWN K_amp (declared, keeps the census
   clean). No role is double-owned; no derivation forked.
2. **The noise-floor derivation window (C18/C20 Tier-1) has FOUR
   riders and ONE owner.** C34/C35 (FAM) consume the floor as input;
   C17 (CONV) joins the same derivation seam; C44 (REMENG) rides the
   same measured-noise object for FD steps. All four sides name the
   seam identically (VERDICT_wave2 §4.11 "one question"); no side
   re-derives it. CONSISTENT.
3. **Band/composition discipline.** C41's P1-P4 policy is the
   composition authority; new bands minted this wave (C14 exit band,
   C26 edge margin band, C19 laxity threshold, C12 mdot term) each
   carry their own derivation clause and will carry a P-tag at
   composition time — no site contradicts the policy; the C34 K²
   instance is its first named customer. CONSISTENT.
4. **Churn axis (C22 ↔ C37).** Rate-at-source (C22) vs
   materiality-band (C37) attack the same re-record cost from
   opposite ends; the coupling is declared on both sides, F-C22-3
   hands the rate lever to C37's band, and the merge-free proxy
   repair keeps C37's census executable without C22's outcome.
   CONSISTENT, no double-adjudication.
5. **Mask object (C29 ↔ C30).** One object, two rows: C30's
   one-liner lands FIRST and instruments C29's [R1] replay for free —
   sequencing pinned in both deltas. The C3 detector survives every
   branch of both rows. CONSISTENT.
6. **Envelope box (C25 ↔ C45 ↔ C26).** The H-F6 reachable-set box is
   C25's object (CONV, landed as window-identity with the Gamma_fund
   audit); C45's derived scan window and C26's edge margin both
   CONSUME it by name and neither derives it. One object, one owner,
   two consumers. CONSISTENT.
7. **Multiplier discipline (C39 ↔ C40 ↔ wave-2 C31).** The
   INFORMATION-ONLY constraint is consumed identically on both rows;
   the lambda_e coverage honesty (instrument 3 alone) makes C40's
   conditional structure exactly right-sized; the fold into
   F2-C39-MULTVER avoids a duty split. The B-stationarity semantics
   chain is now dated correctly (pre-wave-1 carriers claims
   :1350/:1874 → wave-1 [P-BSTAT] → C38's residual declaration-policy
   scope). CONSISTENT.

# §8 ESCALATION CALLS

**Rule-triggered escalations: ZERO.** All 21 sustained repairs carry
named text-level repair texts, adopted verbatim (with judge
modifications stated in-line) in §§1-6 — repaired-by-amendment on the
page, so the auto-escalation clause does not fire for any row.
**Structural escalations declared (not rule-triggered):**
1. **C50 → full Form-2** per BRIEF_wave3_depth_addendum.md D1 (user
   order, runs regardless): ADVOCATE-PDE + ADVOCATE-DATA + dedicated
   closure judge, consuming §2 of this verdict;
   VERDICT_C50_form2.md = the C50 authority of record for the
   landing. Open items handed: §2.1 items 2 (A1 form choice) and the
   R3C50-11(3) verification-gated census candidate.
2. **REM depth pass (D2)** runs unconditionally on
   PANEL_/refute_/§§4-6 of this verdict; any GAP row it finds is NOT
   landable until the split-judge re-pass clears it.

# §9 CANDIDATE NEW ROWS + PAPERS NEEDED (consolidated)

**Candidate new ledger/findings rows: ZERO.** All six slots reported
0, dedup-verified by measured greps; both refuter-surfaced defect
homes already exist (engine-core:F7-legge-bracket-fallback,
engine-core:F8-cert-scale-unit-mixing) — the repairs CONSUME them
rather than minting. Literature-registry RIDER entries (not rows):
REMPOL §4.6 trio (Lyche-Morken, GPB04, SARIF spec).

**PAPERS NEEDED (deduplicated across slots, procurement channel):**
1. Moré & Wild, "Estimating computational noise", SISC 33(3) 2011
   (ECNoise) — [FULL] needed at the C34/C35 epsilon_J protocol arm
   AND the F-C44-1 band derivation (FAM item 1 ≡ REMENG item 1: ONE
   procurement row); executable meanwhile on the tol_dp pessimistic
   bound (declared).
2. ASME V&V 20-2009 (R2016) standard text — [FULL] to upgrade C41
   P1/P2 correlation wording; policy executable without it.
3. Xing & Stern 2010 ASME JFE 132:061403 (+2011 closure) — [FULL]
   only when the C42 role-1 audit executes; open mirrors located.
4. Sun & Nocedal 2023 (arXiv:2201.00973, open) — self-procurable at
   the C34 trigger window; recorded so the trigger consumes it
   deliberately.
5. Shi-Xie-Xuan-Nocedal SISC 44(4) 2022 (arXiv:2110.06380 fetchable)
   — F2-C44-FDSTEP; published version = citation of record.
6. CONDITIONAL: Oliveira-Takahashi ITP, ACM TOMS 47(1) 2020 — only if
   F-C22-1 falsifies the predicate and the bracketed reference is
   promoted.
7. CONDITIONAL: Guest-Prevost-Belytschko IJNME 61 (2004) — only if
   F-C29-1 lands JUMPY and the smooth-gate branch arms.
8. OPTIONAL (C50 enrichment, non-blocking): Métivier et al.,
   arXiv:2101.00904 — would raise OT-closure reason 3 to [FULL];
   handed to D1.
9. VERIFICATION-GATED census candidate (NOT a procurement ask yet):
   Hoffman et al. 1995 / Keil-Craig displacement-amplitude
   verification family — [MEMORY]-depth lead (R3C50-11(3)); must be
   verified per litreview-verification-protocol before any citation
   becomes load-bearing; handed to D1.

# §10 FALSIFIERS FOR THIS VERDICT (what would overturn each per-row verdict)

- FAM: a modern source showing noise-floored TR constants harm
  constrained certified loops (C34); a measured u-scale stagnation
  floor ABOVE 1e-10 on production walks (C35); measured refresh cost
  or nondeterminism on the committed stack (C36); a correlation
  measurement showing RSS under-covering at a P1 site — self-repairs
  to P2 by policy (C41); the audit finding K=4
  optimal-or-conservative at every certificate-bearing role (C42
  closes on the incumbent value WITH derivations — either branch
  closes); a discrepancy found between the row text and VERDICT_wave1
  §4.5 (C43).
- C50: a stage-A flux-class audit demonstrated NOT L¹-continuous on
  the L∞∩TV class; a measured datum family whose dominant error mode
  is not front-position jitter; FS-2 failing systematically (demotes
  d_sens to the conservative dual bound); an upstream assimilation
  layer (re-opens the OT closure) — all as PANEL_C50 §4.4;
  additionally, VERDICT_C50_form2.md superseding this delta is the
  DECLARED consumption path, not an overturn.
- CONV: a tree block found adjudicating the knot placement law (C4 —
  none exists per the completed 9-hit sweep); a recorded N_NEWTON
  derivation found (C17); a committed budget line already implying
  the factor-100 semantics (C18); a committed C-A..C-D text already
  containing the Gamma_fund audit (C24); a second independent
  advocacy source for the box (C25 — would upgrade the recorded 1/4
  support scope, not the verdict); a reading of VERDICT_wave1 §2.1
  under which [P-BSTAT] already fixes the reporting policy (C38 — it
  does not).
- REMMARCH: production drift bias exceeding the composed band (C5);
  F-C6-2 finding no separating constant (C6 — incumbent regains
  primary); the F-C8-1 negative control not firing (C8 — rejector
  vacuous, not adopted); a masking event (C10 — promotion
  pre-registered); F-C12-2 staying in-band on the corrupted start
  (C12 — protocol vacuous, H-F16 instrument required); any of
  F-C13-1/2/3 firing (C13 — promotion path pre-registered); F-C14-1
  firing on the re-anchored metric (C14 — mass-flux-weighted fallback
  pre-registered).
- REMENG: F-C16-1 below threshold or F-C16-2 failure (C16 closes on
  incumbent); the laxity census showing band dominance broken (C19
  re-opens with burden inverted); F-C22-1 in-class disagreement (C22
  flips the bearer); F-C37-2 violation (C37 kills the lever); a
  [P-IPADJ] outcome invalidating a band's construction (C39 — bands
  re-derived, stack survives); F-C40-1 disagreement with the twin
  check passing (C40 — elimination wins); F-C44-1 inside-band (C44
  closes on incumbent); F-C45-2 excursion (C45 — severity upgrade,
  derived window forced).
- REMPOL: F-C7-2 firing on the recorded cycle (C7 — removal leg
  refuted, ratchet declared accepted debt); a measured in-corridor
  false-fire rate above the edge band (C26 — band re-derived);
  a jumpy [R1] outcome (C29 — default overturned BY DESIGN, smooth
  gate arms); measured overhead on an int subtraction (C30 — nil,
  declared closed); a measured false-fire burden from benign
  refactors above the review budget (C47 — fingerprint demoted to
  warn-tier).

# §11 MACHINE SUMMARY

```yaml
verdict: VERDICT_wave3
date: 2026-08-20
slots_adjudicated: 6/6   # null=failure PASS, 12/12 files
rows_adjudicated: 33     # FAM 6, C50 1, CONV 6, REMMARCH 7, REMENG 8, REMPOL 5
rows:
  C34: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C35: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C36: {verdict: CONVERGED-panel,   gated: true,  escalation: null}
  C41: {verdict: CONVERGED-panel,   gated: true,  escalation: null}
  C42: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C43: {verdict: CONFIRM-ALIGNMENT-PASS, gated: false, escalation: null}
  C50: {verdict: ADJUDICATED-SPLIT-BY-ROLE, gated: true, escalation: "STRUCTURAL (D1 user-ordered Form-2; VERDICT_C50_form2.md supersedes this delta if different)"}
  C4:  {verdict: CONFIRMED-CONSISTENT, gated: false, escalation: null}
  C17: {verdict: CONFIRMED+OWNER-DELTA, gated: false, escalation: null}
  C18: {verdict: CONFIRMED-CONSISTENT, gated: false, escalation: null}
  C24: {verdict: CONFIRMED-CONSISTENT, gated: false, escalation: null}
  C25: {verdict: CONFIRMED-CONSISTENT, gated: false, escalation: null}
  C38: {verdict: CONFIRMED-CONSISTENT, gated: false, escalation: null}
  C5:  {verdict: ADJUDICATED-CONVERGED-KEEP, gated: true, escalation: null}
  C6:  {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C8:  {verdict: ADJUDICATED-CONVERGED, gated: true, escalation: null}
  C10: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C12: {verdict: ADJUDICATED-PROTOCOL, gated: true, escalation: null}
  C13: {verdict: ADJUDICATED-PROTOCOL, gated: true, escalation: null}
  C14: {verdict: ADJUDICATED-CONVERGED, gated: true, escalation: null}
  C16: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C19: {verdict: ADJUDICATED-ON-COST, gated: false, escalation: null}
  C22: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C37: {verdict: ADJUDICATED-DEFAULT+GATED-LEVER, gated: true, escalation: null}
  C39: {verdict: INSTRUMENTS-CONVERGED (verification half), gated: true, escalation: null}
  C40: {verdict: ADJUDICATED-CONDITIONAL, gated: true, escalation: null}
  C44: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C45: {verdict: ADJUDICATED-WITH-VALVE, gated: false, escalation: null}
  C7:  {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C26: {verdict: ADJUDICATED (protocol converged), gated: false, escalation: null}
  C29: {verdict: ADJUDICATED-SPLIT, gated: true,  escalation: null}
  C30: {verdict: ADJUDICATED (converged), gated: false, escalation: null}
  C47: {verdict: ADJUDICATED (converged), gated: false, escalation: null}
findings_adjudicated: 76   # FAM 17, C50 13, CONV 8, REMMARCH 12, REMENG 15, REMPOL 11
sustained: {breaks: 0, repairs: 21, amendments: 39, notes: 13}
  # repairs by slot: FAM 4 (R3FAM-1/4/9/11), C50 5 (R3C50-1..5),
  # CONV 2 (R3CONV-1/7), REMMARCH 2 (R3REMMARCH-1/2),
  # REMENG 5 (R3REMENG-2/4/5/6/13), REMPOL 3 (R3REMPOL-1/4/9)
  # amendments incl. 2 reclassed NOTE->AMENDMENT (R3FAM-3, R3REMMARCH-11)
overruled: 0   # no refuter finding overruled; 2 refuter-side corrections
  # by the judge: R3CONV-7 "five registries" -> 4 files/8 hits (finding
  # itself sustained); refuter witness sets otherwise verified intact
dry: false     # 21 repairs sustained (dry = zero breaks/repairs)
escalations_rule_triggered: []
escalations_structural: [C50-D1-Form2 (user-ordered), REM-depth-pass-D2 (unconditional)]
amendments_carried: all sustained amendment texts adopted in sections 1-6 (applied at the landing window; no extra rounds)
repairs_carried_to_confirm_stage: 21 (confirm_repairs_wave3 instance-2 scope (a))
ledger_deltas_proposed: 33 (one per row; panel delta text + judge splices, sections 1-6)
notifications_cross_row: [C8->C42 K_RICH role (census 10+3), C42->C8 reverse conditionality, C34-K2->C41 P-tag case, C30-before-C29 sequencing, C25-box->C45/C26 consumers, claims-1350/1874->C38 declaration-policy composition]
candidate_new_rows: 0
papers_needed: 9 entries (5 firm incl. 1 deduplicated FAM+REMENG, 2 conditional, 1 optional-D1, 1 verification-gated-D1)
file: validation/sfoundations_raws_2026-08-13/blocco3/VERDICT_wave3.md
```

---
[APPEND-ONLY RECONCILIATION ANNOTATION, 2026-08-20, orchestrator (REM
depth ledger obs-1 disposition of record): the section-11 global
sustained-count line {repairs: 21, amendments: 39, notes: 13} does
not reconcile against the per-ID enumeration (REM_depth_ledger.md
section-5: 21 repairs EXACT; amendments enumerate to 37 including
the 2 declared NOTE->AMENDMENT reclasses; notes to 11; plus 7
no-attack/accepted items; 21+37+11+7 = 76 = findings_adjudicated).
The per-ID enumeration is the tally of record; the section-11 line
is a slot-neutral count defect — NO disposition or delta text is
affected (verified by the ledger's own per-ID walk). obs-2 =
DECLINED-AS-ALREADY-DECLARED (the R3REMMARCH-11 reclass is declared
in section 11 itself). obs-3 = RECORDED (non-attack-bearing implicit
sub-point, substance acknowledged in the C-row delta; no carrier
change owed).]

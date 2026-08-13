# ADVISORY — S25 PIPELINE SENSE + IMPLEMENTATION FIDELITY: CONVERGED VERDICT

Date: 2026-08-12. Plan tag: [S25/PREP] (R29 pipeline-sense directive,
Form-2 instance 1, convergence layer).

**Label: Form-2 converged round 1 (narrow agenda); judge layer subject
to the standing Form-3 rule — inline check at absorption.**

Judge discipline honored: adjudicated ON THE FILES (no new positions,
no re-derivation beyond arithmetic checks — one arithmetic
reconciliation executed, §1.3). Pairs:

- **A** = `ADVISORY_S25_pipeline_sense_math_2026-08-12.md` (expert)
  vs `sota_gapmap_raws_2026-08-12/s25_refute_pipeline_math.md` (refuter);
- **B** = `ADVISORY_S25_pipeline_impl_fidelity_2026-08-12.md` (expert)
  vs `sota_gapmap_raws_2026-08-12/s25_refute_pipeline_impl.md` (refuter).

Context authorities cited: `AUDIT_agnostic_2026-08-07.md` (:507-519
throat-panel row; :527-533 cross-unit/Dv caveat),
`docs/claims_registry.yaml` [C-EQV2] (:1387-1398),
`ADVISORY_S24_sota_gapmap_2026-08-12.md` (S25-repaired state of record,
header :22-28; GAP-1 :65-105, GAP-2 :107-136, GAP-27 :728-748),
`PROGRESS_2026-08-12_S25_speed.md` (:460-468 in-flight/R29).

The one-pass expert advisories remain on file AS FILED (one-pass
artifacts); **this document is their corrigendum and the verdict of
record where they diverge.**

---

## §0 CONVERGED SUMMARY

Every needs-judge row of both refuter convergence tables exits below as
ADOPTED / REFUTED-with-evidence / OPEN-with-owner — no silent keeps.

- Pair A: 0 substantive claims refuted outright; R1/R2/R3 ADOPTED in
  the refuter-weakened form (final wordings §3); R4's unification
  REFUTED AS FILED and replaced by the adopted partition (§3.4);
  [NEW] 5a merged into the registered AUDIT row (§1) with the
  magnitude verdict resolved AGAINST the math advisory's emphasis;
  [NEW] 5b ADOPTED, extended to three jump channels (§5).
- Pair B: the **0-MISMATCH / 11 faithful / 2 faithful-with-caveat**
  verdict is RATIFIED (two independent passes agree); one correction
  ADOPTED of record (R6 exactness, §4.2); CAV-1 CONFIRMED at the
  refuter's independent sizing (§4.3); CAV-2 merged into §1; the
  m12-F6 "registration-option" reading recorded (§4.4).

---

## §1 THE MERGED SLIVER ROW — one shared object, one row of record

**Identity (settled):** math-review §2.4 [NEW] "arc sliver dJ/dthB
tilt" == impl-review CAV-2 "theta_1 = thB/n_B missing thrust panel" ==
registered audit finding `[CONFIRMED | medium | correlated-error]
variational-driver:objective-omits-throat-panel`
(AUDIT_agnostic_2026-08-07.md:507-519, verifier-confirmed 2026-08-07,
code unchanged at today's line numbers). The impl refuter's §C makes
the object precise, adopted verbatim as the mathematical statement of
the row:

    DJ_sliver(thB) = 2*pi * Int_0^{thB/n_B} p(th)*y(th)*rtd*sin(th) dth,
    p = kernel/fan flow on the fixed arc (W-independent),
    y(th) = yt + rtd*(1 - cos th);
    d(DJ_sliver)/dthB = 2*pi*p(th1)*y(th1)*rtd*sin(th1)/n_B > 0,
    deterministic and sign-definite within a frozen plan;
    piecewise-smooth with O(da^3) jumps across plan re-records
    (n_B = ceil(thB/da) ceil-seam).

All three sources carry the SAME derivative formula (audit :519; math
§2.4; impl-refuter §C(iii)) — the contradiction was never about the
object, only about the comparison axis (§1.3).

### §1.1 Disposition — (a) of the agenda: **YES**

The math advisory's [NEW] flag is STRUCK (dedup miss against the
registered audit — the refuter's dedup refutation stands: the coverage
universe demonstrably includes AUDIT_agnostic, which the gap map itself
uses as coverage authority in AC8/AC9). Both §2.4 (math) and CAV-2 +
refuter-§C (impl) are FOLDED INTO the AUDIT row as **discharge-prior
inputs**: the audit row keeps ownership of the finding and of its own
suggested test (analytic throat-panel A/B: assert
|dJ/dthB(with panel) − dJ/dthB(without)| < gtol at W*), which is the
discharge experiment of record.

Folded-in refuter precisions (now part of the row):
(i) the omission is O(da^2) with da refined in the two-resolution
protocol — the VALUE-side term is inside the Richardson measurement
scope and vanishes as h→0 (sign-deterministic truncation term, not a
non-vanishing model bias); (ii) the F7 band of record is
class-resolution and the sliver CANCELS in it (same cfg/thB both
sides) — **no S24 verdict moves**; (iii) O2 is a contour oracle —
thrust_J never enters it — so no cross-code verdict is touched; no
cross-code J oracle has ever consumed the sliver, and if one is built
(e.g. vs GENO CF integrating from theta = 0) the convention delta must
be declared first; (iv) the audit sub-finding the math advisory missed:
the Pa-drop declaration presumes the anchor A_0 constant while the
implemented anchor A(theta_1) varies with thB — this QUALIFIES the math
advisory's §1.2.3 "theorem-level" wording (exact for the documented
full-wall domain; saved in code only by the vacuum objective — no Pa
term exists anywhere); (v) if the doc-scoping repair is chosen, it must
scope BOTH the J value AND the gradient/Pa statements (scoping only the
value leaves the gradient statement dangling).

### §1.2 Severity — (b): **MEDIUM, inherited from the audit row**

The math advisory's LOW is overridden. The audit's own kept-medium
reasons re-adopted: discrete carrier internally consistent;
contour-level optimum shift far inside the O2 band; continuum
term-match deferred to the pre-registered O3.3 campaign.

### §1.3 The magnitude contradiction — (c): **resolved; gradient axis governs**

Arithmetic of this pass at the audit's S20-instance constants
(p_t = 5e6 Pa, y_t = 1, rtd = 0.45, th1 = da = 0.008727 rad,
n_B = 23, thB = 0.2007 rad; J ≈ 4.07e7 of the m12gate record):

| Axis | Formula | Number | Source claiming it |
|---|---|---|---|
| Gradient row | 2π·p_t·y_t·rtd·sin(th1)/n_B | **5.36e3 J-units/rad** | audit :519 "O(1e3)" — order-class CONFIRMED |
| Value (absolute) | π·p_t·y_t·rtd·th1² | **5.38e2 J-units = 1.0767e-4·p_t** | impl refuter §C(ii) "1.07e-4·p_t" — coefficient CONFIRMED exactly |
| Value (relative) | DJ/J | **1.3e-5** at these constants (instance-dependent; math advisory quoted ~1e-4 at the twin) | math §2.4 — value-axis only |

Exact bridge (verified): d(DJ)/dthB = (2/thB)·DJ — ratio 9.964 = 9.964.
**Same object, same formula, three axes; the units differ** (J/rad vs J
vs dimensionless), so no two of the three numbers ever contradicted
each other as facts.

**VERDICT WORDING OF RECORD:** the finding is a stationarity-TILT
claim, and stationarity is adjudicated on the gradient axis; therefore
**the magnitude of record is the audit's gradient-row figure: O(1e3)
J-units/rad against the O3 acceptance 10·gtol ≈ 9.3 (S20 instance of
record) — 5.8e2× above, and still ~1e2× above under the worst
Dv-coordinate spread (≤ ~6, audit cross-unit row :533)**. The math
advisory's "below every current discrimination band" is **REFUTED as
the governing comparison**; it survives only as the value-axis
statement, where the term is O(da^2), Richardson-scoped, and
F7-cancelling — which is also exactly why no recorded verdict moves
today. The bias is real only against the DECLARED full-domain
functional; the executed walk is internally consistent (AD gives the
exact gradient of the implemented J — clean discretize-then-optimize).

### §1.4 Owner + trigger — (d): **named — F2-entry objective-domain adjudication**

**[OBJ-DOM] "objective-domain adjudication (throat panel)", owner =
F2 entry.** Because the walk is internally consistent and the bias is
vs the DECLARED objective, the repair is a decision about WHICH
functional is the functional of record, i.e. an objective-definition
adjudication, and F2 entry (where the objective is re-derived for the
stratified class anyway) is its natural slot. The two adjudicable
fixes, from the files: **fix-A** — add the theta = 0 throat station /
analytic panel (makes the omitted area W-independent exactly;
re-baselines recorded J values); **fix-B** — declare the coded J
(domain [theta_1, theta_B]) the object of record, scope the M0/doc
value + gradient + Pa statements, and bound the argmax tilt into the
derived KKT tolerance. TRIGGER (two-sided): before the first F2 verdict
that consumes dJ/dthB, AND before the R2 delta-carrier ships (the
ceiling evaluation inherits the same omission — §3.2(iv)); the audit's
suggested A/B test is the cheap discharge experiment either way.

---

## §2 PER-CLAIM VERDICT TABLE

| # | Claim (source) | Converged verdict | Disposition / owner |
|---|---|---|---|
| A-R1 | No continuum object behind K; "no conjecture with a falsifier" | **ADOPTED-WEAKENED** (refuter repairs (a)-(c) mechanical, ratified) | Final wording §3.1; the letter-false clause struck vs [C-EQV2] registry row :1387-1398; exits already owned (C7; GAP-1 → F2) |
| A-R2 | Ideal-march ceiling ⇒ (value, delta) at engine rung | **ADOPTED-WITH-CORRECTIONS** (lemma + delta semantics + sequencing) | OPEN-with-owner: **F2-entry delta-carrier row (placed)** + M0 lemma row at F2 entry; ships only after/with [OBJ-DOM] (§1.4) or with the sliver banded |
| A-R3 | Averaged structure carrier-less; "mu only at rung 1" | **ADOPTED-RESCOPED** ([T3-QS] symbolic carrier exists, suite item xvi; [T-T4] names the rung-1 composition pattern) | Final wording §3.3; Q3 (certifiability-side composition) = pre-F5 obligation, owner F5 entry |
| A-R4 | "Twelve symptoms = one C2 mismatch" | **REFUTED AS FILED** (inconsistent row lists: header 10, §2.5 11, "twelve" only counting 5b silently) → **REPLACED by the adopted partition** | §3.4; GAP rows keep their map owners; repair-order corollary re-derived |
| A-5a | Arc-sliver [NEW] | **MERGED** — fact ADOPTED, [NEW] flag STRUCK, magnitude resolved on the gradient axis | §1; discharge-prior to the AUDIT row; owner [OBJ-DOM] F2 entry; severity MEDIUM inherited |
| A-5b | frac_bad discontinuity [NEW] | **ADOPTED** (dedup-clean vs the full registry) + extended to THREE channels | §5; OPEN-with-owner: F2, GAP-27/GAP-1 window; clause owed independently of GAP-1's outcome |
| A-§2.1 | IVL-envelope note (argmax second-order) | **SETTLED-CLEAN** (refuter: distinct from GAP-6/AC14, correctly kept separate) | Candidate M0-VI discipline line; owner = the advisory's own named window (F5/P-3, before absolute Isp ships) |
| A-6 | Judge-quality (no anchors; dedup universe too narrow; superlatives) | **ADOPTED as standing requirements** | Any second-pass sense review: file:line anchors mandatory + AUDIT-inclusive dedup; the two superlatives non-citable under R5 (no query bound), reviewer color only |
| B-1..13 | 13 fidelity verdicts (quintic basis 36/36, newton_trips, custom_vjp, spline rows, KS/(G)/DE-bucket/C5/R-GRAD, M4/M1/M2/T2) | **RATIFIED faithful** — refuter re-derived 7 symbol-for-symbol, rest source-verified; 30+ anchors resolve; post-repair line numbers prove live-tree provenance | Settled; peripheral half-nit (invert_h `.get(K_NEWT, N_NEWT_INV)` silent fallback) → optional half-line fence, S25-bis list |
| B-3 | R6 sizing "exact … re-derived, correct" | **CORRECTION ADOPTED OF RECORD** (refuter A6) | §4.2; OPEN-with-owner: this window's micro-commit (1-line comment, thermotab :660-663); advisory sentence corrected BY THIS FILE |
| B-4 | CAV-1 edge-stencil caveat | **CONFIRMED at independent sizing** (2.8-4.6 orders below band; band-breaking N_TAB ≈ 220-300) | §4.3; OPEN-with-owner: same micro-commit window (1-line scoping repair; one-sided 4th-order stencils = named cleaner alternative) |
| B-8 | CAV-2 thrust-panel | **MERGED into §1** (the only needs-judge row of pair B) | See §1 |
| B-14 | "Four micro-repairs ≤ 3 lines" | **ADOPTED-QUALIFIED**: F6 "registration-option" reading RECORDED as the intended one (mirror-control option = 5-10 lines) | §4.4; OPEN-with-owner: S25-bis (census R30) micro list |
| B-15 | 0-MISMATCH / 11 faithful / 2 caveat | **RATIFIED** — both independent passes found no math-to-code mismatch; both text defects live in the ADVISORY, not the code | Settled |

---

## §3 FINAL WORDINGS OF RECORD (R1-R4)

### §3.1 R1 (converged)

At frontier instances the pipeline maximizes J over K = {W : the
adaptive record passes every gate}, a solver-defined set. The
registered formalization (tier ladder (P_t) + margin-multiplier KKT;
nesting/constrained-KKT THEOREM, ladder/A_t SCHEMA) intended K to proxy
A_0. **The two registered statements aimed at the set-level link are,
respectively, FALSIFIED (bridge K_disc ~ A_0 — a registered conjecture
with a named falsifier, executed and killed S22, third instance S24/F4;
"no successor quantifier exists", GAP-1) and hypothesis-blocked at the
executed class (EQ-v2 Direction A + H-CLASS: measured failing at
tier-0, margin never activates, 33× floor at the cert-limited stop —
[C-EQV2] a LIVE registry conjecture with a populated falsifier field),
with named exits (C7 refine/enriched-class conditional; GAP-1's in-KKT
certification surrogate) and the limit order registered as O5.** What
survives as R1 — the narrower gap of record — is the argmax-to-(P_t)
continuum-limit gap: no registered statement, theorem or conjecture,
links the argmax over K_h ITSELF (margin-inactive, KKT-open, hence
outside EQ-v2-A's margin-active subject) to a KKT point of any (P_t) as
h → 0 — exactly the "decisive content UNREACHED at this class" the
record itself registers. Certification degrades at val far above the
fold floor in every instance (0.61-0.86 at S20/S22; DE-bucket val
7.31e-2 = 33× the tightest floor at S24 — instance numbers no longer
conflated). EQ-v2 Direction A is untestable **at this class** (the
record's own scope; C7 is the registered route to testability).
Outcome-II points are certified VALUE data plus falsification data;
Q1's sharp form stands as the program-level restatement.

### §3.2 R2 (converged) — the ceiling carrier, ratified with corrections

The globality half of the D2.6 contract — the pair (S*, delta) — is
exercised end-to-end only at rung 1; no delta row exists at any
engine-rung Verdict (grep-verified independently by both passes).
D2.6(iv)'s ladder already names "sonic-capped J_ideal" as a member, so
the proposal is the executable carrier of an already-declared object.
RATIFIED with the refuter's corrections, all adopted:

1. **Proof obligation = the FIXED-EXIT-AREA RELAXATION LEMMA, not the
   truncation dF/dA argument** (which compares an ideal nozzle to a
   truncation of itself and does not bound a non-uniform-exit TOC
   design): momentum theorem on {IVL, wall, axis, exit disk}, C_IVL
   W-independent under the shared-Sauer data contract; pointwise
   Lagrangian maximization at fixed A_e = eps·A_t and fixed mdot gives
   theta = 0 and the uniform supersonic root q = lambda — the ideal
   march's uniform exit at Me(eps) — licensed in-class by per-cell
   u_x − c > 0. The lemma gets its own M0 row with a rigor class at F2
   entry; the advisory's parenthetical would not survive a referee.
2. **Delta semantics**: delta = J_ideal(eps) − J_TOC upper-bounds the
   distance to the constrained optimum while conflating it with the
   irreducible length-cap price. Every Verdict row says **"distance to
   the L-unconstrained fixed-eps ceiling"** — never "distance to global
   at (eps, L)".
3. **The ceiling ships with its own qualifications**: two-resolution
   band + eps-achievement correction (the ideal march stops at
   |M − Me| < 1e-5 and re-targets; lip/eps residual measured 4.4938e-3
   at the twin) — an under-estimated ceiling is anti-conservative for
   delta.
4. **Sequencing**: the ceiling evaluation inherits the throat-panel
   omission — [OBJ-DOM] (§1.4) lands, or the sliver is banded into the
   carrier, BEFORE any (value, delta) Verdict ships. "Today" = today +
   one declared repair.
5. **Hypotheses stated in the carrier**: same eps, same thermo
   leaf/tables, same Sauer IVL/mdot.

OWNER: **F2-entry row (placed; this convergence records it as the row
of record).**

### §3.3 R3 (converged)

The mu-averaged OPTIMALITY structure (T7(b), (**'), VI.4 switch-splits,
VI.4bis quadrature) has no executable carrier anywhere in validation/
or src/; every certified 2-D result is single-phase under the
T0 → T3/[T-T3-SI] license. The flat "mu enters executed code only at
rung 1" is corrected of record: the averaged DATA/correction structure
has exactly one executable, rejector-gated symbolic carrier —
[T3-QS], suite item (xvi) — plus the rung-1 numeric cycle machinery.
"Nowhere named" is scoped: [T-T4] registers the intersection-over-xi
composition pattern at rung 1, with its Sharpness clause naming the
breakage mode (PB-2, the first genuinely averaged shape problem). What
is genuinely unposed — R3's surviving core — is the
**certifiability-side composition**: K(xi) intersections, xi-indexed
margin buckets/D'-analogs, xi-dependent crossing index, branch
gradients under xi-dependent plan topology (Q3 a-c); T3-CONTROL is
physics-side and does not cover it. Q3 stands as the pre-F5 test form
(owner: F5 entry).

### §3.4 R4 (converged) — the partition of record

The nonsmooth problem-class axis is real (C^2-per-stratum driver vs
measured piecewise-smooth problem, hard-min at derived rho ≈ 5.7e4,
solver-bounded feasible set). The "twelve symptoms = one mismatch"
unification is REFUTED AS FILED and REPLACED by the refuter's
partition, adopted of record against the gap map's own CLASS fields:

- **Squarely on-axis (4)**: GAP-2 (B-stationarity notion itself),
  GAP-27 (hard-min one-hot at derived rho), GAP-13 (discretely-moving
  crossing index), GAP-19 (BFGS on stiff constraint curvature).
- **Coupled/partial (4)**: GAP-4 (tolerance-hygiene defect whose bite
  couples via GAP-2), GAP-15 (adjudication lapse; cost
  segmentation-induced), GAP-16 (kink/seam FD half on-axis; missing
  rejector half = R5 hygiene), GAP-17 (efficiency gap; staleness
  generic).
- **R5-hygiene rows EXCLUDED from the unification (4)**: GAP-12,
  GAP-14, GAP-31, GAP-33 — a problem-class upgrade makes none of them
  moot; each is priced S25-cheap independently by the map's own
  OWNER/PLACEMENT fields. (GAP-33 was cited in the advisory header and
  never argued; GAP-2/GAP-12 appeared only in §2.5 — the header/§2.5
  inconsistency is the recorded evidence.)

Repair-order corollary re-derived from the corrected set: **GAP-1 +
GAP-2 together (with GAP-27's derived-budget clause, which GAP-1's
surrogate would otherwise inherit) upgrade outcome-II semantics — the
coherent first move; the hygiene rows proceed orthogonally and are NOT
sequenced behind it.** The advisory's "most rows become moot or cheap"
is struck.

---

## §4 PAIR-B RATIFICATIONS

### §4.1 The 0-mismatch verdict STANDS

Two independent passes (advisory hand-verification + refuter full
re-derivation, 7 pieces symbol-for-symbol) agree: **no math-to-code
MISMATCH exists in the reviewed surface** (thermotab quintic/C-A/trips,
implicit-rule VJP, spline rows, thrust quadrature, M4/M1/M2/T2, KS/(G)
field, DE bucket, C5/R-GRAD controls). The refuter's provenance check
(post-repair line numbers differing from the m12/m4 refuters'
pre-repair numbers) is accepted as evidence the advisory re-opened the
live tree. Both defects found are in the advisory TEXT: the R6
endorsement (§4.2) and the cosmetic §8/§9 self-pointers — recorded, no
verdict flips.

### §4.2 R6 exactness correction — ADOPTED OF RECORD

The exact flip condition for the corrupted-D index control is
**eps > fr_k/i_k, and the i = 0 probe never flips** (the claimed
formula would give it a finite threshold of 1); the code's
fr_k/(i_k+fr_k) is the first-order i >> fr approximation
(counterexample of record: i = 1, fr = 0.5 — claimed 0.333, true 0.5).
**Verdict-neutral at n = 8192**: the deciding probe sits at i ≈ 8190
(discrepancy 1e-4, both argmins coincide, firing margin 1.9998× ≈ the
intended 2×) — the control fires as designed. Repair row: 1-line
comment correction at `validation/thermotab_c1_jax.py:660-663`
("fr/i exact; fr/(i+fr) = first-order approximation, conservative,
argmin unchanged at this geometry"); the advisory §3 sentence
("exact … re-derived, correct") is corrected by this file. **Owner:
this window's micro-commit.**

### §4.3 CAV-1 (C-A edge stencil) — CONFIRMED at the independent sizing

Premise verified at source by both passes (4th-order central stencil
only at interior nodes; edge nodes 2nd-order, error ∝ dT²·cp''' ≠ 0 on
the NASA quartic). Refined and adopted: the probe SET samples 2 of the
4 edge intervals, which exercise all four inexact node data — the
operative claim stands; independent sizing **2.8-3.3 orders below
tol_h_o (h channel, aggressive cp''') to ≈ 4.6 orders (cp channel)** —
jointly "2.8-4.6 orders below band"; **band-breaking at
N_TAB ≈ 220-300** (advisory's "≲ 500" the right ballpark, mildly
conservative); failure direction conservative (spurious-FAIL only —
edge terms cannot mask an interior defect). Repair row: the 1-line
scoping repair ("interior stencil exact on quartics; edge-node
2nd-order error O(dT⁴·cp''') sized 2.8-4.6 orders below every C-A band
at N_TAB = 8192, conservative direction"), with 4th-order one-sided
edge stencils the named cleaner alternative if the file is ever touched
for content. **Owner: same micro-commit window (doc line).**

### §4.4 F6 "registration-option" reading — RECORDED

The four open micro-repairs are all real and open at source (refuter §D
evidence table): m12-F3 (scoping line for the failure-path message
divergence), m12-F6 (M2 memo first-hit control), m12-F11 (bare asserts
strip under `python -O`; two if-not-raise rewrites), m12-F8 (t_grad
identification; 2-line val_grad timing). The "≤ 3 lines each" sizing
holds for F6 **only under the REGISTRATION option** — register the
m12gate A/B as the superseding first-hit control — which is hereby
recorded as the reading intended and adopted; the mirror-control
option is 5-10 lines and is NOT the adopted reading. Recorded note
(refuter): m12-F4 is landed by declaration only (no campaign entry yet
consumes `A1_MEMO_PROBE=0`); wiring the def_twin campaign entry to the
declared permission is an option for the same window, not a duty.
**Owner: S25-bis (census R30) micro list** — together with the A5
half-nit (invert_h `.get("K_NEWT", N_NEWT_INV)` fallback fence,
half-line) and NOTE-5 (stale `get_solver` 3-tuple docstring).

### §4.5 F6 clarification (namespace)

The m12-F6 above is the M2-memo control item; it is distinct from the
gap map's mesh-amr "F6 axis-verification" row — no merge exists or is
implied.

---

## §5 THE frac_bad ROW — [G1-DISC], finding of record

**ADOPTED** (ex math-§2.5 [NEW]; dedup verified CLEAN against the full
registry by the refuter — GAP-27 covers one-hot gradients, AC12
chatter, GAP-14 the crop denominator; nothing registers this jump).
The G1 surrogate margin is **discontinuous in W across lane-failure
set-membership boundaries through THREE channels of one origin**
(`margin_governor.py:175-201`; def_twin variant with denominator
n_sel): (1) frac_bad jumps by 1/n_act when a lane crosses
finite/nonfinite — the returned margin jumps by K_RICH·m_ref/n_act;
(2) ks_part is computed over the CHANGING finite-lane subset and jumps
when a lane enters/exits fin2; (3) the n_fin → 0 fallback switch.
Continuity is declared, correctly, only at frac_bad = 0 (bit-for-bit
exact-KS recovery — verified by both passes). Inside trust-constr this
is a modeled cliff the TR machinery tolerates but nothing prices.

Repair row: **ONE declaration clause** in the [X-MGOV] surrogate
declaration covering all three channels and naming the explicit
C^2-assumption violation. **OWNER: F2, same window as GAP-27/GAP-1**
(the gap map places both at F2, same window) — with the refuter's
precision adopted: **the clause is owed independently of GAP-1's
outcome**, because the G1 surrogate keeps its REQ-NONSTALL steering
duty under the governor re-scoping regardless of the cert-surrogate
decision.

---

## §6 CONSOLIDATED OPEN ROWS (owners named; nothing else remains open)

| Row | Content | Owner / trigger |
|---|---|---|
| [OBJ-DOM] | Objective-domain adjudication (throat panel): fix-A add theta=0 station vs fix-B declare coded J + scope value/gradient/Pa + bound tilt; discharge test = the audit's A/B | **F2 entry**; trigger = first F2 verdict consuming dJ/dthB, AND before the delta carrier ships; severity MEDIUM meanwhile |
| Delta carrier | (value, delta) Verdict field at engine rung; relaxation lemma to M0 with rigor class; delta = "distance to the L-unconstrained fixed-eps ceiling" | **F2 entry (placed)**; sequenced with/after [OBJ-DOM] |
| [G1-DISC] | Three-channel discontinuity declaration clause | **F2, GAP-27/GAP-1 window**; owed regardless of GAP-1 outcome |
| Q3 (a-c) | Certifiability-side cycle composition | **F5 entry** (pre-F5 obligation) |
| R6 comment + CAV-1 scoping | Two 1-line repairs in thermotab (+ advisory corrigendum = this file) | **This window's micro-commit** |
| S25-bis micro list | m12-F3 / F6-registration / F11 / F8 (+ optional F4 wiring, invert_h fence, NOTE-5 docstring) | **S25-bis (census R30)** |
| M0-VI discipline line | IVL-bias quoting discipline (design-to-design/code-to-code only) | **F5/P-3 window** (advisory's own placement) |
| Second-pass standard | file:line anchors mandatory; dedup universe = gap map + AUDIT + registry | Standing, any future sense review |

---

## §7 INSTRUMENT WEIGHT (this whole convergence exercise)

Per the S25 log (PROGRESS_2026-08-12_S25_speed.md:460-468, R29
directive, in-flight item (ii)): **5 agents** (2 single-expert
reviewers, math-sense + impl-fidelity; 2 dedicated Form-2 refuters;
1 fused convergence judge — this pass), **3 layers × 1 round each —
converged at round 1** on the narrow agenda (0 claims required a second
refuter round; pair-B needed exactly one needs-judge merge). Token
counts are NOT journaled in the S25 log for this exercise and are
declared UNRECORDED rather than estimated (R5). Judge-pass consumption:
4 position files + 4 record authorities (AUDIT, claims registry, S24
gap map S25-repaired, S25 log) + 1 arithmetic reconciliation (§1.3).

*Form-2 converged round 1 (narrow agenda); judge layer subject to the
standing Form-3 rule — inline check at absorption. The two one-pass
advisories remain as filed; where they diverge from this file, THIS
FILE governs.*

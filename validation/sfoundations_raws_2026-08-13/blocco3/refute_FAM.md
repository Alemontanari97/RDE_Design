# refute_FAM — WAVE 3 REFUTATION of PANEL_FAM (C34/C35/C36/C41/C42/C43)
# S-FOUNDATIONS-C3, 2026-08-20. Fused refuter, per-row attacks.
# Mandate: BRIEF_wave3_refuter_judge.md (REFUTERS + h1-h3) with the
# wave-2/wave-1 refuter duties (a)-(f)/(g2)/(g4) VERBATIM.
# BASE = validation/sfoundations_raws_2026-08-13. Every count/quote
# below re-measured or re-read at source IN THIS WINDOW (SR-12).

## 0. NULL=FAILURE CHECK — PASS
PANEL_FAM.md present, well-formed (703 lines, machine summary at EOF).

## 1. FINDINGS (per row, then cross-row)

### C34 — TR floor/caps

**R3FAM-1 — REPAIR-NEEDED — the immateriality branch pins a MAGIC
threshold (10x) inside a derived-constants protocol.**
Mechanism: PANEL_FAM §3.1 pins "if the measured histogram shows no
accepted step within 10x of either literal, the literals are
immaterial and are KEPT with a derived-immateriality stamp". The 10x
window is the DECIDING constant of the keep-vs-derive call and is
neither derived nor declared sufficient-not-optimized with a
direction argument — in the one family whose frozen question is
"which constants are DERIVED vs literal" (§1), and against R5
("tolleranze derivate, non magiche") and the panel's own pre-registered
§1 criterion, which specifies the rho-histogram immateriality test
without any window constant. AG-1 does not cover it as written: the
valve requires the sufficient hypothesis DECLARED as such; the 10x
carries no declaration.
Named repair (small, outcome unmoved after it): either derive the
window from the rho-histogram support width, or declare M=10
sufficient-not-optimized WITH the direction argument stated (larger
M => immateriality harder to claim => conservative; M=10 > K_RICH=4,
the repo's registered safety constant, margin_governor.py:28 /
locus_diagnosis.py:39 verified this window).
Witness: PANEL_FAM §3.1 (protocol clause (iii) + immateriality
branch) vs §1 C34 WIN criteria.

**R3FAM-2 — AMENDMENT — the pinned floor formula silently composes
K_RICH TWICE (K^2 band), un-analyzed.**
Mechanism: the pin TR_FLOOR_derived = K_RICH x tol_dp/||g||_seg
inherits the ledger alternative's formula (choice_ledger :493,
verified), but tol_dp is ITSELF K_RICH-banded at source:
a1_toc_variational_jax.py:2224 `tol_dp = A1.K_RICH * (abs(d1 - d2)...`
(read this window). So the derived floor carries K_RICH^2 = 16x on
the raw two-point spread — an undeclared safety composition, i.e.
exactly the C42 role-reuse disease reproduced inside C34's own new
pin, and a live instance of the C41 composition question. Direction
is conservative-for-a-floor only up to the panel's own named failure
mode (too-large floor => Sun-Nocedal step-rejection cascade, caught
by the pinned falsifier), so the outcome stands: text amendment —
declare the embedded K (use the raw spread, or state K^2 is the
intended safety), one line in the protocol pin.
Witness: a1_toc:2224 vs PANEL_FAM §3.1(iii).

**R3FAM-3 — NOTE — engine seam named only implicitly.** The C34
protocol semantics (rho-histogram, radius floor) live on the driver's
segment-level radius management (a1_toc:1367-1369, verified: tr0/
TR_FLOOR/tr_cap are run_trsqp-level, not scipy internals), but the
accept/reject statistics come from the engine of record, which is
itself gated on the never-executed [P-IPADJ] adjudication
(VERDICT_wave2 §2.1, read this window). The panel consumed the C31
frame in §2.5 axis (1) — declared — but the C34 duty should name
that an engine swap at [P-IPADJ] re-prices the rho-histogram
semantics. No outcome impact; judge may fold into the duty text.

### C35 — xtol

**R3FAM-4 — REPAIR-NEEDED — the pinned derived form is vacuous and
anti-conservative AGAINST the panel's own materiality finding.**
Mechanism, three defects in xtol_u = K_RICH x floor_W/median(Dv)
(PANEL_FAM §3.2/§4.2), all verified at source this window:
(i) VACUOUS DIVISOR: the driver normalizes Dv by its own median at
construction — a1_toc_variational_jax.py:1741 `Dv = Dv/np.median(Dv)`
— so median(Dv) == 1 IDENTICALLY and the formula's Dv-dependence is
a no-op: as pinned it degenerates to K_RICH x floor_W, which is not
a propagation "to the u scale via the Dv map" at all.
(ii) WRONG EXTREMAL: with the driver's actual map W = Dv∘u
(lip_eq = LinearConstraint(A * Dv[None,:], ...), a1_toc:1748), a
u-radius r still resolves W-steps up to max(Dv)·r; stopping is
legitimate only when max(Dv)·xtol <= floor_W, i.e. the safe scalar
form is xtol_u <= floor_W/max(Dv). Using the median (== 1) overshoots
the safe bound by a factor max(Dv) — and the measured diagonal spread
is orders (findings driver-nonsmooth:jacobi-scaling-frozen :1257
"mixed scales", kappa_diag printed at a1_toc:1742-1745).
(iii) SAFETY ON THE WRONG SIDE: for a stopping tolerance whose
material risk is PREMATURE STOP (the panel's own §3.2 materiality
paragraph: "premature-stop masquerading as convergence ... MATERIAL"),
a safety factor must SHRINK xtol; the pin MULTIPLIES by K_RICH,
making termination 4x easier. The pin as written is anti-conservative
in precisely the direction the panel declared material.
Named repair: re-pin the FORM as "floor_W propagated component-wise
through the driver's actual W = Dv∘u map, extremal (max-Dv)
direction, safety factor dividing: xtol_u = floor_W/(K_RICH x
max(Dv))", citing the :1741 normalization; arithmetic executes in
the existing findings-:640 owner window (unchanged). Outcome
(ADJUDICATED-SPLIT, derived form, literal -> declared slack) STANDS
after the repair; the panel's own negative-control falsifier would
have caught the defect at duty time — the refutation moves the
catch to now.
Witness: a1_toc:1740-1748, findings :633-641 (re-read), PANEL_FAM
§3.2/§4.2.

**R3FAM-5 — AMENDMENT — provenance label: the formula is
PANEL-DERIVED, not tree- or census-backed (R-4 recalibration).**
Mechanism: the cited tree advocacy derives GRADIENT-side/stationarity
tolerances, not a step-size xtol: O-F25 link (e) full tree :1310-1313
(verified verbatim) is "terminate when ||P∇J|| <= nu·eps_g", a P8
hypothesis test on the gradient norm; H-F40 :1261-1265 (verified) is
a TR-model-bound STATIONARITY tolerance "not a gradient-norm folklore
number". The chain label :1298 "(e) optimizer step/KKT tolerances"
covers step tolerances nominally, but no tree derives the step-scale
form; the panel's gloss "the xtol form is the same doctrine on the
step scale" (§2.3) is the panel's own extension. Diff convergence
(:179-180, verified) is on the derivation DUTY — honest — but the
specific pinned formula must carry the PANEL-DERIVED label (the C33
precedent of record, VERDICT_wave2 §2.3: "PANEL-DERIVED arithmetic
... no literature import claimed"), so the judge/landing does not
inherit it as tree-converged arithmetic. Outcome unmoved.
Witness: phaseA_tree_optimization.md:1296-1313; phaseA_tree_
hyperbolic.md:1261-1265; phaseB_tree_diff.md:179-180.

**R3FAM-6 — NO-ATTACK (scope, declared) — other xtol literals.**
Measured this window: 20 `xtol` lines in non-GENO .py; besides the
row's 1e-10 family (7 no-space sites + the spaced assignment
a1_toc:2264 — the panel's "7 + 1" count REPRODUCED exactly), the
remainder are cj_states.py:74 (brentq root-finder, xtol=1e-6) and
stechmann_nozzle.py XTOL (golden-section). These are different
solvers outside C35's optimizer-step scope and are C47 numeric-lint
territory; the panel's scope is correct. No attack.

### C36 — Scaling policy

**R3FAM-7 — AMENDMENT — the twin-walk falsifier's comparison object
is ambiguous and can fire spuriously.**
Mechanism: "refreshed-vs-frozen twin walk ... any certified verdict
moved beyond its band REJECTS the refresh policy" (§3.3/§4.3). A
refreshed-Dv walk legitimately follows a different path and may land
at a different (equally valid) certified point; cross-walk verdict
difference then reflects path-dependence of a nonconvex driver, not
a refresh defect — the falsifier as worded can reject a good policy
(a rejector must be able to fire, but for the right mechanism). Fix
(text): pin the comparison object — certificate validity AT EACH
WALK'S OWN endpoint + replay-fidelity/determinism bit-check (findings
:1261, already riding) + same-base same-seed segment-level
comparison for the scaling-sensitivity claim; a genuine reject =
band violation or determinism break, not endpoint divergence.
Outcome (refresh direction wins) unmoved.
Witness: PANEL_FAM §3.3 falsifier clause vs findings
driver-nonsmooth:jacobi-scaling-frozen :1259-1262.

**R3FAM-8 — NOTE / no further attack — the "refresh is FREE" premise
is C32-contingent, and the panel handled it correctly.** Verified:
VERDICT_wave2 §2.2 keeps fresh-FD-per-segment as INTERIM policy of
record (so diag(H) is free TODAY) with [P-QNCARRY] as the
measurement-gated challenger; the panel's §4.3 what-would-overturn
names exactly the re-price if carry is promoted. Authority consumed,
consequence named — h2 clean on this seam. No attack sustained.

### C41 — Band form/composition

**R3FAM-9 — REPAIR-NEEDED — the P3 dominance threshold is un-derived
and admits a silent 20% safety erosion by the row's OWN metric.**
Mechanism: P3 permits max-composition when top/runner-up ratio
r >= K_RICH. Using the findings row's own coverage metric (verified
:1194: "comparable components a~b -> K*max covers a+b by 2.11x
(intended 4x)"; check: K·a/(a+b) = 4·1.13/2.13 = 2.12), the
composed coverage under P3 is K·r/(r+1): at the threshold r = K_RICH
= 4 that is 4·4/5 = 3.2x vs intended 4x — a 20% erosion, undeclared,
of the same mechanism class the row was minted to kill (the 2.11x
datum differs only in degree). The threshold value is not derived
from any declared erosion budget: r >= (1-eps)/eps gives eps = 20%
at r=4; a 5% budget needs r >= 19 (the panel's own 19:1 D-prime
datum sits exactly at the 5% line — coverage 3.8x = 95%).
Named repair (policy text, outcome unmoved): P3 carries its derived
coverage bound K·r/(r+1) and EITHER declares the accepted erosion
(sufficient-not-optimized, direction stated: higher threshold =>
less erosion) OR sets the threshold from a declared erosion budget
eps via r >= (1-eps)/eps. One sentence; trivially checkable at
composition time exactly as P3 already requires.
Witness: findings thermo-bands:band-composition-no-declared-rule
:1191-1199 (re-read); PANEL_FAM §3.4 P3; K_RICH = 4 of record
(margin_governor.py:28, this window).

**R3FAM-10 — AMENDMENT — P1 drifts from the pre-registered criterion
(measured independence -> stated argument), permissive direction,
undeclared (g2 post-hoc-drift class).**
Mechanism: §1 C41 WIN criteria (frozen before census): "conservative
where correlation is unknown and collapses to RSS where independence
is MEASURED". Policy P1 as adjudicated grants RSS on "a stated
independence/correlation argument" — an argument is weaker than a
measurement, and the drift eases the LESS conservative branch. The
O-F25 link (f) advocacy (:1313-1314, verified verbatim: "declared
which, per correlation argument") supports the argument-form, so the
drift has a source — but §0-ter requires deciding BY the
pre-registered criterion or declaring the deviation. Fix: either
tighten P1 to "measured or structurally proven independence" or
declare the criterion revision with the O-F25 anchor. Outcome
(declared-policy wins) unmoved.
Witness: PANEL_FAM §1 (C41 criteria) vs §3.4 (P1);
phaseA_tree_optimization.md:1313-1314.

### C42 — K_RICH role reuse

**R3FAM-11 — REPAIR-NEEDED (h1 LOAD-CLASS VALVE audit) — the interim
validity hypothesis is over-scoped and NOT trivially checkable: a
load-bearing certificate-semantics statement rides under the valve.**
Mechanism: §3.5 declares the sufficient hypothesis "K=4 covers Fs=3
(Roache two-grid) and the measured p_obs >= 0.415 coverage bound ...
keeps EVERY current band VALID-AS-CONSERVATIVE while the program
runs" (emphasis on scope). Two defects:
(i) SCOPE: the Roache-Fs=3 and p_obs>=0.415 arguments price ONLY
role 1 (two-resolution Richardson bands). Roles 6 (L_TB Lipschitz
surrogate), 7 (thermo remainder floors), 10 (sensitivity-propagated
landing bands) are bands of entirely different structure — nothing
in the hypothesis prices them; and for roles 4/5 (delta_inst =
min_margin/K_RICH, thr = m_ref/K_RICH — verified a1_toc:2147,
locus_diagnosis:276) the conservativeness DIRECTION inverts (larger
K = smaller floor/threshold), so "K=4 conservative" is not even
well-defined for them. "Every current band" is unsupported as
stated.
(ii) CHECKABILITY (the valve condition): p_obs is NOT measured at
the deployed band sites today — that measurement IS the open duty
(findings mesh-amr:...-not-at-band-sites :1185 verbatim: "K_RICH is
not conditioned on an observed p"; leg (a) exists to produce it). A
hypothesis whose check is the pending campaign is not "strong
trivially-checkable" per AG-1; as written it smuggles the
load-bearing statement (current bands valid) under the valve.
Named repair (outcome — ordered per-role program — unmoved):
restate interim validity honestly: role-1 sites stand under the
wave-1 interim regime's OWN mechanism (VERDICT_wave1 §2.4, verified
this window: pre-F2 band-bearing verdicts run the ALREADY-BUILT
[X-O32] estimator at their own sites or declare the row trigger
fired — that is the checkable clause), NOT under a blanket
conservativeness hypothesis; interim validity of roles 2/3/6/7/8/10
= the per-role structural declarations already in the panel's
ordered program, pulled forward explicitly as DECLARED-INTERIM
(one line each at the audit's first window).
Witness: PANEL_FAM §3.5/§4.5; VERDICT_wave1.md §2.4 (:664-676);
findings :1182-1190.

**R3FAM-12 — NO-ATTACK (declared) — the role census itself.**
Re-measured this window: K_RICH in non-GENO .py = 107 matches / 17
files — the panel's SR-12 count REPRODUCED exactly. Spot-checked
classifications at source: margin_governor:207-209 (role 3 sentinel,
verbatim `-A1.K_RICH * m_ref`), locus_diagnosis:276 (role 5),
a1_toc:2147 (role 4), a1_toc:2164/2224/2490 (role 1/noise carriers),
engine_speed_bench:449 (role 9 timing, correctly declared
out-of-certificate-scope). The stale-"8 roles" correction (10+2
measured) is supported and the notifications N1/N2 are consumed
verbatim (VERDICT_wave1 §4.6, VERDICT_wave2 §4.12 — both read this
window, quotes match). Genuine no-attack: the census is the panel's
best work.

### C43 — CONFIRM-ALIGNMENT

**R3FAM-13 — NO-ATTACK (declared), one anchor nit (NOTE-level).**
All three verification legs independently re-run this window:
(1) VERDICT_wave1 §4.5 text (:842-851) vs ledger row :585-593 —
content identity and status/owner/evidence fields match as the panel
states (status enum MIXED with "adjudicated-with-C11" note, owner
"F2 (aligned with C11; was S25)", evidence = VERDICT_wave1.md#4.5);
(2) the interim-regime identity vs §2.4 holds; (3) the residue chain
C43 -> F2-C11-ESTIMATOR-CAMPAIGN leg (a) -> C42 role-1 is closed and
singly-owned (findings :1189-1190 trigger verbatim as quoted).
Nit: the panel cites the findings row as ":1185-1190"; the row
starts at :1182 (id line). No content consequence. The
confirm-alignment verdict is sound; no attack.

### Cross-row / census protocol (g2)

**R3FAM-14 — AMENDMENT — an "included" census item with no one-liner,
no depth marker, and a self-contradicting recency line.**
Mechanism: §2.2 claims "newest included items 2023-2025" and then
lists inside the same parenthesis "TR gradient-sampling for noisy
nonsmooth, Optim.Eng. 2026" — (i) a 2026 item contradicts
"2023-2025" in the same sentence; (ii) the item appears NOWHERE in
§2.3's per-source one-liners and carries no [FULL]/[ABS]/[TITLE]
marker, violating the §0-ter mandate that included items carry
depth; the machine-summary census_recency string repeats it. Either
the item is included (then it needs its one-liner + marker) or it is
recency garnish (then it must be struck and the span honestly ends
2024/2025). Zero-inflation rule bites exactly here. Outcome of no
row moves; text fix.
Witness: PANEL_FAM §2.2 vs §2.3 vs §6 census_recency.

**R3FAM-15 — AMENDMENT — probable read-depth inflation on the SNOPT
scaling claim.**
Mechanism: §2.3 attributes at [ABS] depth: "production-code precedent
for automatic row/column scaling reducing Jacobian element spread".
The SNOPT paper's abstract (SIREV/SIOPT) describes the SQP method;
the automatic-scaling detail lives in the paper body/user guide —
the claim as anchored likely exceeds abstract content (g2: claims
above held depth). Cheap fix, no outcome impact: re-anchor the
scaling identity to the findings row that already carries it of
record (driver-nonsmooth:jacobi-scaling-frozen :1261
"constraint-row equilibration (SNOPT lineage)") or mark the source
honestly as [TITLE]+registry-carried identity.
Witness: PANEL_FAM §2.3 (Scaling block) vs findings :1261.

**R3FAM-16 — NOTE — cava sweep command not executable as printed;
result nonetheless TRUE (reproduced).**
The §2.4 command `grep -n -i "GCI|K_RICH|safety factor|1\.25|toleran"`
uses alternation without -E; BRE grep treats | literally and returns
zero. Re-run this window with regex alternation semantics: exactly 6
hits at :51/:794/:805/:829/:834/:1153 — the panel's claimed set,
reproduced. The closed-by-stated-reason call (Harroun c_F=1.25 =
semantic noise) STANDS; fix the printed command to its executable
form (add -E) per SR-12 auditability.

**R3FAM-17 — NOTE — two minor protocol nits, no outcome impact.**
(i) Q1's verbatim query embeds the expected winners' author names
("...Sun Nocedal ECNoise More Wild") — auditably transcribed, but
confirmation-shaped; the pre-registered criteria (frozen before
search) are the mitigation of record, and they were honored, so
NOTE only. (ii) machine-summary `alternatives_closed: 14` cites no
enumeration or command (SR-12 spirit); the per-row texts support a
count of that order but the judge should not consume the numeral as
measured.

## 2. h-DUTY DECLARATIONS
- h1 (valve audit): one sustained finding — R3FAM-11 (load-bearing
  interim-validity statement under the valve, not trivially
  checkable). Symmetric over-machinery direction: NONE found — the
  panel's refusals to adopt (O-F7 option-with-precondition, C42
  no-same-window-re-derivation) are correctly right-sized.
- h2 (authority consistency): CLEAN — verified consumed-not-reopened
  at source: VERDICT_wave2 §4.11 (C18/C20 window; C34/C35 consume
  the floor as input), §4.12 + VERDICT_wave1 §4.6 (C42 notifications,
  quotes verbatim), §2.1/§2.2 (C31 frame; C32 interim policy —
  R3FAM-8), VERDICT_wave1 §2.4/§4.5 (C11 regime consumed; C43
  alignment). No re-opening found.
- h3 (scope clauses): CLEAN — no F3/F4b/F5/census-owned item decided;
  role 9 declared out-of-scope; H^s option named-not-adopted.
- h4: n/a (not the CONV slot).

## 3. VERBATIM-QUOTE AUDIT DECLARATION
Verified at source in this window (all matched unless flagged above):
ledger rows :489-497/:499-507/:509-517/:562-573/:575-583/:585-593;
findings :283-291/:633-641/:1182-1190/:1191-1199/:1254-1262; trees
phaseA_tree_optimization.md:1293-1330 (O-F25 + P8),
phaseA_tree_optimization_CONDENSED.md:63-69/:140-146/:190-196,
phaseA_tree_hyperbolic.md:1225-1250/:1253-1269 (H-F39/H-F40),
phaseA_tree_hyperbolic_CONDENSED.md:168-172,
phaseA_tree_variational_CONDENSED.md:234-238 ("no magic 1.25"
verbatim x2); diff phaseB_tree_diff.md:176-211 (all six row
anchors); code a1_toc_variational_jax.py:1367-1370/:1575-1579/
:1697-1748/:1941/:2147/:2164/:2224/:2259-2264/:2490,
margin_governor.py:27-28/:207-209, locus_diagnosis.py:38-39/:276,
engine_speed_bench.py:449; VERDICT_wave1.md §2.4/§4.5/§4.6;
VERDICT_wave2.md §2.1/§2.2/§4.9/§4.11/§4.12; literature registry
:840-855 (Roache/Celik/Eca-Hoekstra WANTED rows); cava hits
reproduced (R3FAM-16). Mis-cites found: the :1185 vs :1182 anchor
nit (R3FAM-13) and the non-executable grep transcription (R3FAM-16);
no substantive misquote found.

## 4. DEDUP REGISTER
No finding above re-mints a registry row: R3FAM-4 attacks the
PANEL's new formula (the underlying defect row :633-641 is cited as
the owner window, unchanged); R3FAM-9 extends the :1194 arithmetic
to the panel's own P3 clause (panel-text defect, not a new
registry-borne fact); R3FAM-11's repair routes through the
already-landed VERDICT_wave1 §2.4 mechanism. Zero candidate new
rows from this refutation.

## 5. MACHINE SUMMARY

```yaml
cluster: FAM
findings:
  - {id: R3FAM-1,  class: REPAIR-NEEDED, row: C34}
  - {id: R3FAM-2,  class: AMENDMENT,     row: C34}
  - {id: R3FAM-3,  class: NOTE,          row: C34}
  - {id: R3FAM-4,  class: REPAIR-NEEDED, row: C35}
  - {id: R3FAM-5,  class: AMENDMENT,     row: C35}
  - {id: R3FAM-6,  class: NO-ATTACK,     row: C35}
  - {id: R3FAM-7,  class: AMENDMENT,     row: C36}
  - {id: R3FAM-8,  class: NOTE,          row: C36}
  - {id: R3FAM-9,  class: REPAIR-NEEDED, row: C41}
  - {id: R3FAM-10, class: AMENDMENT,     row: C41}
  - {id: R3FAM-11, class: REPAIR-NEEDED, row: C42}
  - {id: R3FAM-12, class: NO-ATTACK,     row: C42}
  - {id: R3FAM-13, class: NO-ATTACK,     row: C43}
  - {id: R3FAM-14, class: AMENDMENT,     row: census}
  - {id: R3FAM-15, class: AMENDMENT,     row: census}
  - {id: R3FAM-16, class: NOTE,          row: census}
  - {id: R3FAM-17, class: NOTE,          row: census}
breaks: 0
repairs: 4
amendments: 5
notes: 4
no_attack_declared: 3   # C35 scope, C42 census, C43 (with reasons)
per_row_coverage: "C34 attack / C35 attack / C36 attack / C41 attack / C42 attack / C43 declared no-attack-found (all three legs independently re-verified at source this window)"
outcome_impact: "no BREAK — all six proposed row outcomes stand conditional on the 4 named repairs (C34 immateriality-margin derivation-or-declaration; C35 propagation clause re-pinned on the actual W=Dv∘u map, extremal direction, safety dividing — a1_toc:1741 median-normalization makes the pinned form vacuous; C41 P3 dominance threshold carries its derived coverage bound K*r/(r+1) or an erosion-budget-derived threshold; C42 interim validity hypothesis rescoped to role-1 under the wave-1 par.2.4 mechanism)"
```

# REFUTATION — slot REMPOL (wave 3, S-FOUNDATIONS-C3 blocco 1)

Refuter of record over `BASE/blocco3/PANEL_REMPOL.md` per
BRIEF_wave3_refuter_judge.md (REFUTERS section) + wave-2 refuter duties
verbatim (g-duties incl. g2 census-protocol enforcement, g4 per-row
coverage) + wave-3 additions (h1) valve audit, (h2) authority
consistency, (h3) scope clauses. BASE =
validation/sfoundations_raws_2026-08-13. Date 2026-08-20. Every anchor
attacked below was re-read AT SOURCE in this window (SR-12); the
verbatim-quote audit and the R-4 anti-transplant register are at EOF.
IDs: R3REMPOL-<n>. No file other than this one is written.

---

## Row C7 — outer-loop dof policy

### R3REMPOL-1 [REPAIR-NEEDED] — the pinned removal band does not exist

Mechanism: falsifier-threshold fabrication by reference (attack duty
(e): thresholds DERIVED or magic). F-C7-1 pins "retire iff deviation
<= the derived band (no new constant; the band is the insertion
band)", and §3.1 grounds it on "every insertion is gated by
derived-band machinery". Witness at source: insertion is gated by
NOTHING of the kind. The insertion decision is Doerfler bulk marking
on indicator mass (theta = 1/2 canonical, audit set {0.3,0.5,0.7})
capped at A1_AKN_MAXINS (adaptive_knot_optimize.py:29-32, :337); the
docstring states explicitly "the indicator is a refinement driver,
not a verdict row" (:26); the warm-start representation deviation is
MEASURED AND PRINTED, never gated ("NOT claimed geometry-preserving
... the representation deviation is MEASURED and printed each cycle",
:46-48; dev_warm computed and printed with no check() row,
:435-451). The per-cycle gates that DO exist (:62-68) are Newton
certification, P4 margin floor, RK-G replay, O3.1 spot check — none
is a representation-deviation band. So "the band is the insertion
band" points at a phantom object: as pinned, F-C7-1 cannot execute
and F-C7-2 ("degrades the recorded goal metric beyond the band")
inherits the same dangling reference. The findings-row owner text
(:1334, "derived band") is equally unspecific — the panel's mandate
was precisely to PIN the protocol, and it pinned a name, not a
derivation.
Named repair (outcome stands after it): bind the band to machinery
that EXISTS and is derived — (i) for F-C7-2 the [D3] stopping floor
tol_stop = K_RICH * |rel(r=1) - rel(r=2)| (goal-metric noise floor,
adaptive_knot_optimize.py:50-54) is the natural, already-derived
verdict band; (ii) for F-C7-1 the retire test needs its own derived
deviation band — e.g. the measured dev_warm floor across the recorded
S20 cycles (the same quantity the loop already prints), declared as
the removal counterpart of the measured-not-gated insertion deviation.
Either binding is one sentence in the landing delta; without it the
"no new constant" claim is false and the falsifier cannot fire.
Direction (insert+remove, end-of-cycle sweep, measurement-gated) is
NOT contested — no census or tree position defends the ratchet, the
panel's steelman of AFEM (theorem import fails on the moving optimum)
is verified against findings :1330-1331 verbatim.

### R3REMPOL-2 [NOTE] — grep claim slightly overstated (conservative direction)

Panel §1.0: "no removal path exists — grep 'remove|coarse' measured
this window, only doc-line hits". Re-measured this window:
`grep -in "remove\|coarse" validation/adaptive_knot_optimize.py`
returns ZERO hits, not "doc-line hits". The discrepancy is
conservative (the panel's claim is weaker than reality) and
immaterial to the outcome; recorded for census-protocol accuracy (g2).

---

## Row C26 — out-of-box behavior

### R3REMPOL-3 [AMENDMENT] — incumbent steelman contradicts the findings row of record

Mechanism: contradiction of a record the panel itself cites [FULL]
(attack duty (f)). Panel §3.2 incumbent case: "at every RECORD
instance the box hypothesis held (no known out-of-box march state on
committed records)". Witness: docs/findings_registry.yaml:575
(engine-core:F3-table-clamp-silent magnitude, the row the panel
confirms at :573 in §2.4): "CONFIRMED LIVE S21: the [X-VMON] KAT-B
first range left the box and measured lam_ad -0.216 vs -1.185 at
M ~ 4.7". A committed record DOES carry a confirmed live box exit
with a measured wrong sensitivity. The error runs AGAINST the
incumbent the panel already rejects — outcome unmoved, indeed
strengthened (the box-exit mode is not hypothetical) — but the
landing text must not inherit the false premise, and the materiality
line upgrades from "MATERIAL whenever it happens" to
"already-happened-once of record". Text fix only.

### R3REMPOL-4 [REPAIR-NEEDED] — F-C26-1 verdict threshold is a transplanted constant

Mechanism: underived-in-context tolerance (attack duty (e); R5).
F-C26-1 pins "margin < derived mollification band (~4*DeltaT joint
census, C-C machinery) => verdict row FAILS". Witness: the ~4*DeltaT
band of record was derived for INTERNAL JOINT mollification of the
quintic table ("a box crossing a joint must state the mollification
(~4ΔT) explicitly in the certificate",
ADVISORY_S24_thermo_closure_survey_2026-08-12.md:250-252) — a
smoothness-certificate statement about piece boundaries, not a
domain-edge exit threshold. Reusing it as the box-EDGE margin band is
derivation-by-transplant: the number is derived, but for a different
hypothesis; in context it is magic (exactly the class R5 forbids and
the panel's own C29 §3.3 charges against eps_gate — the panel applies
the standard asymmetrically). The honest edge threshold is either 0
plus the maximal certified probe excursion (FD probes at P±h are the
named near-edge consumers, findings :579), or a fresh edge-side
mollification argument stated as such.
Named repair (outcome stands after it): re-derive or re-justify the
F-C26-1 threshold FOR THE EDGE (0 + derived probe-excursion
allowance, or an explicit one-sided-joint argument with its own
falsifier); the traced-flag protocol, the checkify closure (stated
reason verified: custom_vjp boundary + record-losing abort semantics),
and F-C26-2/3 are not contested.

### R3REMPOL-5 [AMENDMENT] — mechanics precision + gating label

Three text fixes, outcome unmoved: (i) "an index-clip event iff
margin < 0" is imprecise — `_locate` clips the interval index to
[0, n-2] (thermotab_c1_jax.py:183-186), and i = n-2 is also the
LEGITIMATE last in-box cell; the detection event is the margin sign,
not the clip operation (at exact T = Tg[n-1] the clip fires with
margin = 0 and value exact). The pin should say the margin scalar IS
the detector and drop the clip-event equivalence. (ii) The VALVE
sufficiency hypothesis "every table read of the closure routes
through ht/T" is asserted, not shown trivially-checkable — the
landing text should carry the one-line site enumeration (state_q
reads at :403-405; invert_h :308) as the check, since
trivially-checkable is the valve's own admission condition (h1).
(iii) Machine-summary `gated: false` sits uneasily with F-C26-2's own
clause "silence on either => the diagnostic is refuted, C-D stays
open" and with pre-registered criterion (d) ("demonstrably FIRES"),
which at adjudication time is undischarged: declare in the row text
that criterion (d) is discharged at build time by F-C26-2 (acceptance
rejector), so the adjudication is not chargeable with post-hoc
criterion drift (g2).

---

## Row C29 — mask freezing granularity

### R3REMPOL-6 [AMENDMENT] — segment-refreeze cost is asserted, not priced in the pin

Panel §3.3 charges the incumbent with a MEASURED cost (C3 repeat =
decisive run 2, verified at findings :1221) but credits the
challenger with an asserted one: "one mask rebuild per segment = one
val_diag run per segment (bounded, known cost)" — no recorded number
exists for a per-segment val_diag rebuild rhythm, and the mask build
of record requires a full runv with val_diag=True
(def_twin_falsifier.py:1126-1133). F-C29-2's acceptance clause "the
decisive-run-2-class repeat cost must vanish" nets only one side of
the ledger. Amendment: add to F-C29-2 a measured cost carrier
(N_seg × val_diag rebuild cost vs the recorded repeat cost, reported
at the replay) so the acceptance is priced, not asserted. Outcome
(default direction, gating on [R1]) unmoved — the structural
arguments (P2 rhythm coherence, binary KKT semantics per cava :513
verified verbatim, C3 permanence F-C29-4) hold independently.

### R3REMPOL-7 [NOTE] — working-set analogy is a partial transplant (declared no-break)

The census leg "the standard rhythm for re-deriving a working set is
PER STEP/SEGMENT ... a frozen working set across many steps is
nonstandard" (OpenSQP/active-set entries [ABS]) borrows authority
from optimizer working sets for a spatially-indexed enforcement lane
mask feeding ONE aggregated KS constraint — related objects
(active-constraint identification) but different cost structures
(working-set update = cheap pivot; mask rebuild = full val_diag run),
which is exactly why the incumbent froze per rung. The panel uses it
as supporting census, not as the decision driver (the driver is the
findings-row [R1] discriminator + the measured C3 fire), so this does
not rise to a finding — recorded as an R-4 register entry. Otherwise
NO ATTACK FOUND on this row's core: the decision rule maps the
pre-registered §1.1 win conditions onto [R1]'s two outcomes exactly,
the escalation branch's eps_gate-must-be-derived entry condition is
the panel's own R5-consistent bar, C3-fire evidence verified verbatim
(findings :1221; gapmap :393-400; gate code :1193-1223 measures rung
START vs rung END, so "compatible with smooth accumulation" is an
honest reading), O-F19 shared-advocacy declared once (§4.3), C28
gates-absolute consumed not re-opened (h2 clean).

---

## Row C30 — mask crop policy

### R3REMPOL-8 [AMENDMENT] — negative control under-specified; logging rhythm mislabeled

(i) F-C30-2 pins "the findings-row trigger instance planted
deliberately (M_NODES change between derive and rung) must produce
nonzero lost_lanes; silence => the counter is refuted". Witness: the
crop drops lanes only when a TRUE lane lies beyond the overlap
(mm[:r,:c] = mask[:r,:c], def_twin_falsifier.py:683); a planted shape
change whose True lanes all sit inside the overlap yields
lost_lanes = 0 honestly, and the pin as written would then FALSELY
refute a correct counter. The plant must guarantee at least one True
lane out-of-overlap (one extra clause). (ii) "logged per adaptation
event (rides shape_events)" — the existing counter increments per
margin_W CALL under mismatch (:679), not per adaptation episode (the
recorded "16 adaptations" of findings :1230 are call-counts); the pin
should adopt the existing rhythm by name to avoid minting a second
event semantics. Outcome (adopt the invariant, one-liner, VALVE)
unmoved; the valve use is genuine gap-accounting (h1 verified: row
CONFIRMED with owner at findings :1227-1235, verdict-bearing-iff-
margin-active qualifier is declared and preserves the
nonzero-loss-DECLARED obligation). The never-postpone check is
correctly structurally-gated (write mandate boundary + named owner
and trigger) — no attack there.

---

## Row C47 — numeric-lint enforcement policy

### R3REMPOL-9 [REPAIR-NEEDED] — "closes the within-count swap surface" is false as stated

Mechanism: over-claim on the winning option; the winner as described
fails the panel's own pre-registered criterion (c) ("the residual
attack surface is NAMED"). Witness: the pinned upgrade stores the
per-file sorted MULTISET of literal values. A within-count
VALUE-swap (A -> B) changes the multiset and fails — that subclass
closes. But a within-count ROLE-PERMUTATION — exchanging two
literal values already present in the same file between their sites
(e.g. two different thresholds 0.3 and 0.7 swapped) — preserves both
the count AND the multiset and PASSES. The SARIF lineage the panel
cites for provenance closes exactly this via positional/context
partialFingerprints — the component the panel's R-4 recalibration
explicitly dropped ("No positional fingerprint is needed (value
multiset suffices for literals)" §3.5 — false for permutations).
Verdict text "closes the within-count swap surface" (§4.5, machine
summary) would land a false closure claim in the ledger.
Named repair (outcome stands after it): re-declare the residual —
the upgrade SHRINKS the declared limit from {any within-count swap}
to {within-count permutations of the existing in-file value multiset}
— in the row delta and in F-C47-2 (whose seeded rejector should also
document the permutation non-catch as the declared residual, exactly
as the current docstring declares the swap limit). Adoption of the
multiset upgrade is NOT contested (it strictly shrinks the surface at
~zero cost and beats all listed alternatives on the pre-registered
criteria); retention of the ratchet and classification-as-endpoint
verified against the ledger row :633-643 and findings :265-273.

### R3REMPOL-10 [NOTE] — registry-internal count inconsistency (not a panel defect)

The findings row the panel cites carries 37 files / 639 literals in
its magnitude (re-measured S-CERT 2026-08-13, :268) but "the
baselined 621" in its owner text (:272), while the test docstring
still says 622/33 (test_numeric_lint.py:27-28, dated 2026-08-12). The
panel correctly used the newest measured pair (37/639). Surfaced for
the landing window: the owner-text "621" should be reconciled to the
magnitude's re-measure (SR-12 class). Census behavioral claim
spot-checked at source this window: ESLint bulk suppressions DO fail
on unpruned (fallen-count) suppressions — exit code 2 with a
prune-suppressions mandate (eslint.org/docs/latest/use/suppressions;
eslint/eslint PR #20496) — so "falling counts auto-tighten" is
substantively sound ("fail-until-pruned" would be the precise verb);
no inflation finding.

---

## Cross-cutting audits (h1/h2/h3, g2)

### R3REMPOL-11 [NOTE] — machine-summary count not command-tied

`alternatives_closed: 12` in the panel's machine summary has no
enumeration or measured command behind it (SR-12 applies to claims of
count); my own enumeration of explicitly-closed alternatives across
§3.1-3.5 yields a defensible but not unique reading (AFEM; checkify,
untraced assert, warn-extrapolate; smooth-gate-to-branch; incumbent
crops/counters displaced; blanket exemption, hard-fail; + census
sub-options). Immaterial to any verdict; the landing should either
enumerate or drop the scalar.

- (h1) VALVE audit: C26 and C30 are genuinely gap-accounting
  (CONFIRMED findings rows with owners at :573, :1227 — verified);
  the C7 valve (end-of-cycle sweep only, no THB import for a 1-D knot
  vector) is genuine right-sizing, not smuggling; no load-bearing
  statement found hidden under a valve; no over-machinery on
  bookkeeping found. The one valve-adjacent defect (C26 sufficiency
  hypothesis asserted-not-shown) is carried in R3REMPOL-5(ii).
- (h2) AUTHORITY consistency: C28 verdict consumed correctly (ledger
  :423-431 note text matches the panel's characterization verbatim:
  priced-frontier KS, P4/P3(ii) gates ABSOLUTE); the panel's claim
  that VERDICT_wave1/wave2 contain no REMPOL-row adjudication is
  grep-verified this window (the only C30 hits, wave1 :286 and wave2
  :90, are the cava's internal numbering exactly as the panel
  declared). Clean.
- (h3) SCOPE clauses: C7's F3-owned loop-build named-not-decided
  (§4.1); C29 duty F2-owned with the S21 driver-touching pin
  re-affirmed (findings :1225 verified); no census-lemma/phase-owned
  crossing found in any row. Clean.
- (g2) census protocol: query table present and internally consistent
  (8 queries, hits >= screened >= included everywhere); §1.1 decision
  criteria pre-registered and — with the two exceptions charged in
  R3REMPOL-4 (asymmetric R5 application) and R3REMPOL-5(iii)
  (criterion (d) timing) — the adjudications decide BY them, not past
  them; read-depth markers present throughout, and the one behavioral
  claim I tested above [ABS] depth (ESLint) survived source check;
  materiality honest in both directions (C30
  immaterial-now/material-later declared; C7 material-on-budget with
  the artifact-safety carve-out verified at findings :1331; nothing
  ritual found). The two STE arXiv IDs (2602.05119, 2604.21640) are
  unverifiable in-window; the claim they support (binary-forward
  practice) is family-notorious and doctrine-consistent — no finding,
  logged for honesty.

---

## Verbatim-quote audit declaration

Spot-verified AT SOURCE this window, exact: diff :56-59 C7 quote
("No tree defends insertion-only as a ratchet; none demands removal
either. Weak agenda support."); diff :131-132 (C26 PARTIAL), :156-157
(C29 partial-convergent O-F19), :158 (C30 SILENT), :220-224 (C47
SILENT); ledger rows C7/C26/C29/C30/C47 at :200-209/:401-409/
:433-442/:444-452/:633-643 incl. alternatives lists (all covered by
the panel) and row count 57; findings rows at :1218/:1227/:1328/
:573/:265 (line-exact) incl. C3-fire numbers (96->82, 14 nodes,
9.188e-3 vs 2.118e-3 = 4.3x, decisive run 2), 8->20 dofs, 37/639;
code anchors a1_ideal_march_jax.py:403 (jnp.interp line-exact),
thermotab_c1_jax.py:183/:308 (line-exact), adaptive_knot_optimize.py
:32-36/:197/:337/:408, def_twin_falsifier.py:536-539/:677-707/
:1124-1133/:1193-1223 (all confirmed); AUDIT_agnostic :388-400
(cert_worst blind + suggested planted test at :398); thermo survey
C-D :253-257; cava :513 (active-set {L, eps_max, lip, truncation},
sign + complementarity — line-exact); gapmap GAP-13 :393-400;
test_numeric_lint.py docstring :23-45 (declared limit + --inventory).
Mis-cites found: NONE at line level; the two CONTENT mis-statements
are R3REMPOL-1 ("insertion gated by derived-band machinery" — the
source says measured-and-printed, driver-not-verdict) and R3REMPOL-3
(incumbent premise vs findings :575). One count claim unverified and
accepted as plausible-not-load-bearing: "dof cost ... named dominant
when T2 FIRED" (§1.1 C7 materiality) — materiality stands on the
docstring's n+1-evals-per-dof alone.

## R-4 anti-transplant register (8 instances audited)

1. THB coarsening -> 1-D knot vector: recalibrated by the panel
   (valve: no THB import) — clean.
2. AFEM optimality theorems -> moving optimum: import REJECTED by
   pre-registered bar — clean (verified vs findings :1330).
3. ESLint/ratchet industry pattern -> repo ratchet: same-pattern
   claim source-checked — clean (R3REMPOL-10).
4. SARIF partialFingerprints -> value multiset: recalibration DROPPED
   the load-bearing positional component — CHARGED (R3REMPOL-9).
5. SQP working-set rhythm -> DE lane mask: partial analogy, used as
   census color not decision driver — logged (R3REMPOL-7).
6. checkify error monad -> custom_vjp stack: transplant REFUSED with
   stated reason — clean.
7. GPB04/adaptive-beta projection -> eps_gate branch: entry gated on
   derived floor + conditional full-text ask — clean.
8. C-C joint mollification band -> box-edge threshold: transplant
   UNDECLARED — CHARGED (R3REMPOL-4).

## Dedup register

No finding above mints content already carried by a registry row: the
live box-exit instance (R3REMPOL-3) is already IN findings :575 — the
finding is the panel's contradiction of it, not a new row; the
permutation residual (R3REMPOL-9) lands as C47 note text per the
panel's own note-level-amendment route, not a new row; the 621-vs-639
reconciliation (R3REMPOL-10) is an owner-text fix on an existing row.
Candidate new rows from this refutation: NONE.

## MACHINE SUMMARY

```yaml
cluster: REMPOL
findings:
  - {id: R3REMPOL-1,  class: REPAIR-NEEDED, row: C7}
  - {id: R3REMPOL-2,  class: NOTE,          row: C7}
  - {id: R3REMPOL-3,  class: AMENDMENT,     row: C26}
  - {id: R3REMPOL-4,  class: REPAIR-NEEDED, row: C26}
  - {id: R3REMPOL-5,  class: AMENDMENT,     row: C26}
  - {id: R3REMPOL-6,  class: AMENDMENT,     row: C29}
  - {id: R3REMPOL-7,  class: NOTE,          row: C29}
  - {id: R3REMPOL-8,  class: AMENDMENT,     row: C30}
  - {id: R3REMPOL-9,  class: REPAIR-NEEDED, row: C47}
  - {id: R3REMPOL-10, class: NOTE,          row: C47}
  - {id: R3REMPOL-11, class: NOTE,          row: cross-cutting}
breaks: 0
repairs: 3
amendments: 4
notes: 4
per_row_coverage: "C7 attacked (1 repair); C26 attacked (1 repair, 2 amendments); C29 attacked (1 amendment) + declared no-break on the core decision rule with reason; C30 attacked (1 amendment); C47 attacked (1 repair)"
outcome_direction: "no BREAKS-VERDICT — all five proposed row outcomes stand modulo the three named repairs (C7 band binding, C26 edge-threshold derivation, C47 residual re-declaration)"
```

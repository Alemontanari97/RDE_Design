# refute_REMENG — fused refuter, S-FOUNDATIONS-C3 WAVE 3 slot REMENG

Refuter of record for PANEL_REMENG.md (C16/C19/C22/C37/C39/C40/C44/C45).
Duties consumed this window: BRIEF_wave3_refuter_judge.md (REFUTERS incl.
h1-h3) + BRIEF_wave2_refuter_judge.md (g-duties by reference) +
BRIEF_wave1_refuter.md (a)-(f) VERBATIM + BRIEF_wave3_panels.md (§REMENG
mandate). Every anchor below was verified AT THE SOURCE in this window
(see §V). No file edited except this one; env untouched; no package
changes; no git.

Attack coverage: EVERY row carries at least one genuine finding — no
no-attack-found declarations were needed on this slot.

---

## FINDINGS (per row)

### C16 — Newton damping ladder

**R3REMENG-1 | AMENDMENT | C16 — the panel misstates the certificate's
metric (residual vs undamped-step norm) in its own rationale.**
Panel §1 ("certificates consume final residual vs floor, not the damping
path") and §3.1 ("the cell certificate consumes the FINAL residual vs
the derived floor") are FALSE at the anchor: the certification metric is
the UNDAMPED NEWTON STEP norm vs NEWTON_TOL_FACTOR*EPS*sc —
a1_ideal_march_jax.py:433-448, comment of record: "terminate when the
undamped Newton step at the current iterate — exactly the per-cell
certification metric — falls below the certification bound" (S18
kickoff §5bis R-1 amendment). I.e. the certificate is ALREADY
error-oriented (Deuflhard-class ||Dx||); only the damping ACCEPT rule is
residual-based (argmin over sum r*r, :426-429). Mechanism: the
mis-statement narrows the challenger's genuine edge to the accept rule
alone and must not leak into the record. Impact: outcome UNMOVED (the
certified statement is indeed damping-path-invariant either way; the
proposed §4.1 delta text does not carry the error). Fix: correct the
two rationale sentences; state explicitly that Deuflhard (3.40) attacks
the ACCEPT rule only, the termination/cert metric is already
error-oriented.

**R3REMENG-2 | REPAIR-NEEDED | C16 — F-C16-3 elevates the challenger's
criterion to ground truth and overrides the panel's own pre-registered
WIN criteria.**
As pinned: "any accept where the natural monotonicity test REJECTS ...
while argmin non-increase accepts = accept-rule defect of record", with
overturn clause "F-C16-3 firing (forces challenger regardless of cost)".
Mechanism: Deuflhard's NMT is sufficient-condition machinery under
affine-covariant Lipschitz hypotheses (CSM 35 §3.3, verified at source),
not a certificate semantics; per the panel's OWN materiality frame the
certified statement is damping-invariant, so an NMT-reject/argmin-accept
event that still certifies (final step-norm below floor, identical
certified outcome) moves nothing of record. The pre-registered §1 WIN
criterion demanded challenger superiority in eval count / failure rate
AT IDENTICAL CERTIFIED OUTCOMES; F-C16-3 as written adopts the
challenger on a criterion disagreement alone = post-hoc criterion drift
(g2). Witness: a doctored-thought instance — trial t=1.0 accepted by
argmin with ||Dx-bar||>||Dx|| transiently at iterate 2, cell certifies
at iterate 5 in-band: F-C16-3 declares a "defect of record" and forces
the challenger; nothing measurable changed. REPAIR: demote F-C16-3 to
an INSTRUMENT of F-C16-1/2 (NMT-reject-accept events are logged as
activation instances and A/B evidence; they force the challenger only
if correlated with cert failures or excess implicit solves above the
derived threshold). Outcome (SPLIT, census-first) stands after repair.

**R3REMENG-3 | AMENDMENT | C16 — incumbent under-steelmanned: the
in-code recorded rationale is omitted while "no recorded rationale" is
repeated.**
a1_ideal_march_jax.py:418-423 carries a recorded design rationale for
exactly the feature the panel attacks: the trailing 0.0 candidate is a
deliberate NaN-safety mechanism ("a stalled cell keeps its iterate and
FAILS the per-cell certification honestly instead of poisoning the
march with NaN — near-sonic cells transiently leave the M > 1 domain
under full steps, where asin(c/q) is undefined"). The panel's point (ii)
calls the 0.0 accept "a silent outcome" — it is a documented
honest-fail path (stalled cell burns to the trip cap and fails
certification), i.e. the opposite of silent; and the annex verbatim "no
recorded rationale" (true of the LADDER VALUES) is repeated in a way
that reads as no-rationale-for-the-structure. Both directions of
inflation duty (g2/b) bite. Consequence for the pinned A/B: the
challenger build must PRESERVE the NaN-safety property (natural level
function is equally undefined on NaN residuals) — add NaN-domain
robustness as an explicit WIN criterion of F2-C16-DAMPAB, else the A/B
is not apples-to-apples. Outcome unmoved.

### C19 — certification metric scale

**R3REMENG-4 | REPAIR-NEEDED | C19 — the steelman-against is
contradicted by a findings row of record the panel's dedup grep missed,
and F-C19-1 as pinned is either immediately-firing or vacuous.**
Panel §3.2: "our cell states are low-dimensional with components of
comparable magnitude on record instances (F8 LOW)". The record says
otherwise: findings row **engine-core:F8-cert-scale-unit-mixing**
(docs/findings_registry.yaml:608-,CONFIRMED, verified this window):
"single scalar certification scale max(1, max|z|) over mixed-units z =
[x4,y4,u4,v4]: position components certified only to ~100 eps |u| —
about 3 decades looser than their own roundoff floor — while the
comment claims UNIT-CONSISTENT ... no verdict compromised (contour
bands Richardson-dominated)". So: (i) component-scale disparity of
record is ~3 DECADES, not "comparable magnitude" — the panel consumed
"AUDIT F8 LOW" as a materiality number while inverting its content;
(ii) F-C19-1 (per-record disparity census, re-open if disparity exceeds
a threshold) measures a quantity ALREADY measured and known large: with
any threshold below ~10^3 the rejector fires on day one — contradicting
"immaterial-declared" — and with a threshold above it the rejector is
vacuous. Either way the pinned falsifier cannot do the job claimed.
Note the disparity census is also under-specified (scale_i undefined;
with scale_i=|z_i| the ratio is unbounded at zero-crossing components;
with scale_i=max(1,|z_i|) it is identically 1 whenever all |z_i|<=1).
REPAIR: replace F-C19-1 with a VERDICT-LAXITY census on the F8
mechanism: per certification point, laxity_i = sc/max(1,|z_i|) per
component, compared against the margin by which Richardson-dominated
bands absorb it (threshold derived from the GAP-29 factor-2 headroom AS
the panel intended, but on the laxity-vs-band-dominance axis, not raw
disparity); cite engine-core:F8-cert-scale-unit-mixing as the standing
instance and home the duty there (no new row). Outcome (retain scalar
on cost) SURVIVES the repair — F8 itself records "no verdict
compromised" — but the adjudication text and falsifier must be rebuilt
on the true record.

### C22 — wall-foot search

**R3REMENG-5 | REPAIR-NEEDED | C22 — F-C22-1's "ANY disagreement"
trigger is unbounded over probe admissibility.**
As pinned, the doctored two-close-knots probe falsifies the
monotone-foot predicate and flips the certificate-bearer on ANY (N,Nv)
disagreement. But a doctored geometry below the refinement floor /
outside the admissible class (exactly the [X-AKNO] near-degenerate-knot
family the findings row names as trigger) can produce a disagreement
that says nothing about the predicate ON THE CLASS the certificate
quantifies over; the certificate never promised correctness on
inadmissible inputs. F-C22-2 sweeps "to the refinement floor", but
F-C22-1 ALONE flips the bearer. The findings-row verbatim ("the
doctored two-close-knots probe vs a Brent-bracketed reference decides")
was transplanted without class recalibration — an R-4-pattern miss on
an in-repo source. REPAIR: bound the F-C22-1 probe family to the
admissible class (knot spacing >= the refinement floor of record;
[X-AKNO] instance family); in-class disagreement = predicate falsified
(as pinned); out-of-class disagreement = evidence routed to C10/C5
(REMMARCH, named-not-decided — consistent with the panel's own scope
clause). Outcome (SPLIT, burden on the predicate) stands after repair.
NOTE (miscite, hygiene): §3.3 attributes "wall_search decisions bitwise
inside the compiled executor" to the "ledger note"; the ledger C22 note
says "compiled the incumbent scan (gate-verified)" — the "bitwise"
wording lives in the FINDINGS row GAP-28 DELTA text (verified). Content
true, anchor wrong.

### C37 — segmentation trigger

**R3REMENG-6 | REPAIR-NEEDED | C37 — F-C37-1/F-C37-2 are circular as
pinned: the census needs the merge machinery its own outcome gates.**
F-C37-1 defines "benign = candidate-mergeable per F-C37-2's own
definition"; F-C37-2's test is "a merged segment must replay
BIT-IDENTICALLY ... deltas inside the derived band" — executable only
WITH the merge build; but F2-C37-FLIPMAT says "the merge build itself
only fires if F-C37-1 shows materiality". Dependency cycle: census ->
needs merge -> gated on census. As written the materiality census
cannot be executed, and the lever can never be licensed OR killed —
the falsifier pair cannot refute. REPAIR: give F-C37-1 a MERGE-FREE
benign proxy, declared sufficient-not-optimized (consistent with the
row's own frame): e.g. flips whose certified-class labels (S,xi) are
unchanged across the boundary under the adopted O-F19/H-F11 loci
logging, and/or flips whose discarded-Hessian columns are lip-only
(the findings-magnitude lipward case of record); F-C37-2 then licenses
the merge on the proxy-flagged subset only, and a proxy-vs-F-C37-2
disagreement on that subset retires the proxy. Outcome
(DEFAULT+GATED-LEVER) stands after repair. Authority-consistency (h2)
verified clean on this row: N6 verbatim, [P-FLIPMAT] de-registration,
and [P-QNCARRY] arm-B flip-touched invalidation (VERDICT_wave2 :531,
:944) all consumed correctly; the brief itself designates this panel
as the N6 right-sized instance, so no under-weight attack stands.

### C39 — multiplier provenance (verification half)

**R3REMENG-7 | AMENDMENT | C39 — ordering pin vs F-C39-3 incoherence.**
The ordering pin says instruments 1-3 "land WITH [P-IPADJ]" because the
res.v/optimality source adjudication is prerequisite to interpreting
any band; F-C39-3 then contemplates an LSQ-vs-res.v disagreement on the
S18/S24 RECORDED gradients standing "until [P-IPADJ] explains it" —
a reading obtained BEFORE the prerequisite it was declared to wait for.
Either (a) the LSQ referee is licensed pre-[P-IPADJ] on recorded
artifacts (defensible — it is offline and solver-independent, the
panel's own census point), in which case the pin should say instruments
1-2 ride [P-IPADJ] while instrument 3 may run on recorded gradients
now; or (b) all three wait, and F-C39-3's "until" clause is dead text.
Pick one; the stack and F2-C39-MULTVER stand either way.

**R3REMENG-8 | AMENDMENT | C39 (cross-effect C40) — undeclared
preconditions: instrument 2 has NO margin-active checkpoint on the
record corpus, and lambda_e coverage reduces to instrument 3 alone.**
Findings row constraints:margin-constraint-no-hess (verified this
window): "margin INACTIVE at every recorded instance, zero recorded
effect" — so F-C39-2's "at a margin-active checkpoint" has an empty
instance set today; the instrument is well-defined only from the first
margin-active verdict (which is exactly the GAP-12 row's trigger — the
panel should have named it). Separately: instrument 1 (complementarity
band) is structurally VACUOUS for the equality multiplier lambda_e (no
sign/complementarity structure on equalities), and instrument 2 needs
activity — so lambda_e verification rests on instrument 3 (LSQ) ALONE.
Consequence for C40: the conditional "IF the C39 stack (1-3) leaves
lambda_e unverified" is materially LIKELIER to fire than the panel's
framing suggests (one instrument, not three, bears on lambda_e).
Fix: name both preconditions in the §4.5 note delta and state the
lambda_e coverage honestly; no outcome change (the stack remains the
right stack; the conditional structure was built for exactly this).

### C40 — lip equality handling

**R3REMENG-9 | AMENDMENT | C40 — F-C40-1's direction clause presumes
the eliminated twin is defect-free.**
"Disagreement = elimination WINS (provenance defect demonstrated)"
attributes ANY eliminated-vs-row disagreement to res.v provenance; a
twin-implementation bug produces the same signature. The findings owner
text of record (GAP-32, verified) prescribes AD post-optimality "with
an O3.1-style check" — the panel's protocol adopts the mechanism but
drops the check from the falsifier's trust chain. Fix: condition
"elimination WINS" on the twin's O3.1-style post-optimality check row
PASSING; a disagreement with the check failing = INVESTIGATE, no
winner. Conditional outcome structure unmoved. Otherwise clean: N-W
§15.3 [FULL] claims verified AT SOURCE this window (Fletcher Example
15.2 nonlinear-elimination danger, simple elimination (15.9)-(15.10)
exact, 1x1 basis triviality); valve use genuine (severity LOW, "no
record impact" verbatim); anti-entropy fold into F2-C39-MULTVER sound.

### C44 — FD steps

**R3REMENG-10 | AMENDMENT | C44 — read-depth inflation on the
incumbent's load-bearing support.**
§3.7 asserts the incumbent steps "ARE the textbook-derived optima for
smooth noise-free doubles (N-W §8.1 error model)" — an at-[FULL]
strength claim on a section NOT among the declared [FULL] reads (§2.2
declares only §15.3 pp.427-430). The routing via "[P-HESSREJ] findings
owner text" does not carry it: that text (verified) says only
"Nocedal-Wright error model", not that the incumbent's constants are
its derived optima. Duty (g2) read-depth enforcement applies precisely
here because the claim props the "genuinely derived on its own axis"
half of the SPLIT. Fix: read §8.1 (on disk) and mark [FULL], or
re-mark the claim at the depth actually held. (Content is
standard-textbook true; the protocol exists so that is not taken on
faith.)

**R3REMENG-11 | AMENDMENT | C44 — F-C44-3 is ambiguous across the
cross-lowering pin the panel itself declares binding.**
"Complex-step cross-check on the twin tier at one record point ...
disagreement beyond derived band = FD tier defect": if the FD leg is
the ENGINE-path FD and the CS leg the numpy twin, the comparison
crosses lowerings and the cited one-lowering-per-comparison discipline
row rejects the attribution — a disagreement then attributes to
nothing. Fix: pin BOTH legs to the twin lowering (FD-on-twin vs
CS-on-twin), and scope the conclusion to the shared step/stencil logic,
which is what transfers to the engine tier. Outcome unmoved.

**R3REMENG-12 | AMENDMENT | C44 — census auditability gap: Moré-Wild
ECnoise 2011 / derivative-estimates 2012 carried at [ABS] with no
documented access path.**
Neither appears in any Q1-Q6 included set (Q3's single inclusion is
Shi et al 2022), neither is on disk, and the of-record mentions (ledger
C18 alternative "More-Wild noise floors") are TITLE-level. An [ABS]
marker is a read claim for THIS census window (g2). Fix: re-mark at
[TITLE]/of-record — harmless here since papers-needed #1 already
concedes the full text is required before the F-C44-1 band derivation,
so nothing load-bearing rests on the [ABS].

### C45 — leggeAree bracket

**R3REMENG-13 | REPAIR-NEEDED | C45 — the pinned rejector misses the
recorded silent-failure branch; the panel failed to consume the
findings row that owns this exact defect.**
The code (verified): a1_ideal_march_jax.py:868-872 —
`qs = np.linspace(as*1.01, as*2.8, 400)`; sign-change intervals
collected; **`q0 = qs[idx[-1]] if idx.size else float(as_) * 1.8`** —
on EMPTY bracket the scan silently seeds q0 = 1.8*as, and no post-solve
M(qe) > 1 check exists downstream. This is a CONFIRMED findings row of
record: **engine-core:F7-legge-bracket-fallback**
(docs/findings_registry.yaml:599-607, from
AUDIT_agnostic_2026-08-07.md:444-456), whose owner text already
prescribes the closure: "derive the scan window from the table box
(q_max from h0 - h(T_TAB_LO)) + assert bracket found + supersonic-root
rejector". Against that record the panel's closure fails twice:
(i) the pinned "endpoint rejector (root at either grid boundary =>
REFUSE)" does NOT cover the dominant recorded failure path — an
out-of-window root yields an EMPTY idx and the silent 1.8*as default,
not a boundary hit — so the §3.8 claim "the rejector alone converts the
hidden hypothesis into a monitored one" is FALSE as pinned; the audit
of record additionally shows the un-rejected consequence (convergence
to the SUBSONIC root, surfacing only as downstream NaN, "which F1 shows
can itself pass certification silently"); (ii) §6 claims dedup by
measured grep, but the pattern ('...leggeAree|damping...') contains no
token present in the F7 row — the grep ran (SR-12 formally met) but
its pattern missed the row that is C45's correctness-half HOME, so
F2-C45-BRACKETGUARD near-re-mints a weaker version of an owned duty
(duty (f)). A third hidden hypothesis goes unnamed: idx[-1] selection
presumes the supersonic root is the LAST sign change on the grid (the
audit's verifier note records this as the partial mitigation — it
should be a named, monitored hypothesis, not an accident). REPAIR:
F-C45-1's rejector family must cover (a) empty-bracket => LOUD REFUSAL
(the 1.8*as default dies or is gated), (b) boundary-interval bracket =>
REFUSE (the panel's case), (c) post-solve supersonic-root rejector
M(qe) > 1 + margin (the audit's named check), with the idx[-1]
ordering hypothesis logged; the duty text cites and homes into
engine-core:F7-legge-bracket-fallback (owner prescription verbatim)
instead of minting F2-C45-BRACKETGUARD as a parallel object. Outcome
class (CONVERGED-WITH-VALVE, H2 dormant) stands after repair.

**R3REMENG-14 | NOTE | C45 (h1 valve audit) — "GAP-ACCOUNTING" label
under-classes the correctness half.**
A wrong-root seed silently steering the exit-Mach solve is load-bearing
record correctness (the F7 audit's subsonic-root scenario), not
bookkeeping; the valve's sufficient-hypothesis treatment is the RIGHT
machinery, but only once the sufficiency actually covers the existing
branches (R3REMENG-13). Post-repair the valve use is legitimate;
classificatory nit only. Symmetric check (over-machinery on
bookkeeping): none found on this slot — C19/C40 valve/materiality uses
are genuinely cheap.

### Slot-level

**R3REMENG-15 | NOTE | slot — protocol hygiene.**
(i) Machine-summary "alternatives_closed: 9" is a hand count with no
command shown (SR-12 spirit; the rows/dedup counts ARE command-backed).
(ii) The §6 dedup grep pattern was under-designed for its purpose —
demonstrated by the two missed rows (F7-legge, F8-cert-scale) that
carry directly on C45 and C19 (see R3REMENG-4/-13); companion-grep
claims on the other registries are asserted, not shown. (iii) Census
protocol otherwise CLEAN under audit: Q1-Q6 included counts reconcile
with the §2.3 entries (16/16 accounted, sole exception = R3REMENG-12);
no-query closures for C40/C45 carry stated reasons; recency span
1973-2026 honest against items cited; Deuflhard [FULL] claims verified
verbatim at the PDF ((3.40) residual-monotonicity/ill-conditioning,
(3.43) lambda=min(1,1/h_k), Lemma 3.16 bit counting, (3.48)/(3.49)
correction/prediction — all present at the cited book pages); N-W §15.3
[FULL] verified (Fletcher Ex. 15.2, (15.9)-(15.10)); speed-audit
numbers (444x :343, 1.46e-11 :350, >=1.86x :305, N6 :443-444) and
s24_gapv_cell-cert.md:191 verified; VERDICT_wave2 consumptions
(INFORMATION-ONLY :495, [P-QNCARRY] flip-touched :531/:944, [P-HESSREJ]
UNCONDITIONAL :540) verified. Scope clauses (h3) clean: C22->C10/C5,
C37->O2, C44->C18/FAM, C45->C25 all named-not-decided; no
F3/F4b/F5/census-owned crossing found.

---

## §V VERBATIM-QUOTE AUDIT DECLARATION

Verified at source this window: docs/choice_ledger.yaml rows C16-C22
(:296-370) and C37-C45 (:519-615) read in full; phaseB_tree_diff.md
:93-105, :183-222; docs/findings_registry.yaml rows GAP-12 (:1209-),
GAP-16 (:1245-), GAP-17 (:1254-), GAP-18 (:1263-), GAP-19 (:1272-),
GAP-28 (:1346-), GAP-32 (:1364-), F7-legge (:599-607), F8-cert-scale
(:608-); code a1_ideal_march_jax.py:412-451, :805-816, :860-874;
a1_toc_variational_jax.py:1740-1749; VERDICT_wave2.md (grep-verified
lines 495/531/540/944); ADVISORY_engine_speed_audit_2026-08-12.md
:305, :343-350, :440-459; AUDIT_agnostic_2026-08-07.md:444-456;
sota_gapmap_raws_2026-08-12/s24_gapv_cell-cert.md:186-195;
literature/deuflhard_2011...csm35.pdf (pages containing (3.40), (3.43),
Lemma 3.16, (3.48), (3.49) extracted and read);
literature/nocedal_wright_2006...2ed.pdf (§15.3 pages: Fletcher Ex.
15.2, (15.9), (15.10) extracted and read). Web-claim items ([ABS] on
COMSOL/Aria, qpOASES, arXiv ids) not re-fetched — attacked only on
auditability (R3REMENG-12), not on content. Mis-cites found: two,
both logged (R3REMENG-5 NOTE anchor swap; R3REMENG-1 metric).

## DEDUP REGISTER

No new rows minted by this refutation. R3REMENG-4 homes into existing
engine-core:F8-cert-scale-unit-mixing; R3REMENG-13 homes into existing
engine-core:F7-legge-bracket-fallback (both rows pre-date the panel;
the repairs consist of CITING them and adopting their owner
prescriptions). All other findings are defects of the panel text /
falsifier pins and need no registry home.

## MACHINE SUMMARY

```
{cluster: REMENG,
 findings: [
  {id: R3REMENG-1,  class: AMENDMENT,     row: C16},
  {id: R3REMENG-2,  class: REPAIR-NEEDED, row: C16},
  {id: R3REMENG-3,  class: AMENDMENT,     row: C16},
  {id: R3REMENG-4,  class: REPAIR-NEEDED, row: C19},
  {id: R3REMENG-5,  class: REPAIR-NEEDED, row: C22},
  {id: R3REMENG-6,  class: REPAIR-NEEDED, row: C37},
  {id: R3REMENG-7,  class: AMENDMENT,     row: C39},
  {id: R3REMENG-8,  class: AMENDMENT,     row: C39},
  {id: R3REMENG-9,  class: AMENDMENT,     row: C40},
  {id: R3REMENG-10, class: AMENDMENT,     row: C44},
  {id: R3REMENG-11, class: AMENDMENT,     row: C44},
  {id: R3REMENG-12, class: AMENDMENT,     row: C44},
  {id: R3REMENG-13, class: REPAIR-NEEDED, row: C45},
  {id: R3REMENG-14, class: NOTE,          row: C45},
  {id: R3REMENG-15, class: NOTE,          row: slot}
 ],
 breaks: 0, repairs: 5, amendments: 8, notes: 2,
 per_row_coverage: {C16: attacked, C19: attacked, C22: attacked,
                    C37: attacked, C39: attacked, C40: attacked,
                    C44: attacked, C45: attacked},
 key_witnesses: ["a1_ideal_march_jax.py:872 silent 1.8*as fallback vs pinned endpoint-only rejector + findings engine-core:F7-legge-bracket-fallback un-consumed",
                 "findings engine-core:F8-cert-scale-unit-mixing (~3-decade mixed-unit disparity of record) vs panel's 'components of comparable magnitude'",
                 "a1_ideal_march_jax.py:433-448 cert metric = undamped-step norm, not residual",
                 "F-C37-1/2 census-vs-merge-build dependency cycle"]}
```

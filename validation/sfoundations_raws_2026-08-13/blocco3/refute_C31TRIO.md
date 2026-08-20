# REFUTATION — CLUSTER C31TRIO (wave 2)
S-FOUNDATIONS-C2, Blocco 3 wave 2, 2026-08-19. Refuter of record per
BRIEF_wave2_refuter_judge.md (REFUTERS: wave-1 brief verbatim + extra
duties g/g2/h + the reconciliation-honesty duty of
BRIEF_wave2_reconcile.md). BASE = validation/sfoundations_raws_2026-08-13.
Target: `BASE/blocco3/PANEL_C31TRIO.md` read IN FULL (1110 lines).
Inputs read in full: BRIEF_wave2_panels.md (§0/§0-bis/§0-ter +
§C31TRIO), BRIEF_wave1_panels.md §0, BRIEF_wave1_refuter.md,
VERDICT_wave1.md, BRIEF_wave2_reconcile.md. Every anchor relied on
below was re-read AT SOURCE in THIS window (SR-12); greps re-run in
this window are quoted with their measured hit sets.

NULL=FAILURE CHECK: PASS — the panel file exists, is well-formed,
carries all mandated sections (§1 frozen statement with pre-registered
criteria, §2 census with §0-ter(a) table + §2.5 dedup, §3 per-row
adjudication + §3.1-bis + §3.4, §4 verdicts/duties + candidate row +
counting rule, PAPERS NEEDED, §5 machine summary, RECONCILIATION
DECLARATION).

---

## 1. FINDINGS (per-row, both directions)

### RC31T-1 — REPAIR-NEEDED — row C31 — phantom falsifier IDs in the proposed ledger delta

**Claim attacked:** §4.1 note text: "Falsifiers F-C31-1/2/3 (see panel
§4.3)."
**Mechanism:** broken cross-reference minted by the reconcile window's
new §4 content. Measured this window: `grep -n "F-C31"
PANEL_C31TRIO.md` returns EXACTLY ONE hit — line 909, the reference
itself. No falsifier named F-C31-* is DEFINED anywhere in the panel;
§4.3 is the C33 delta (it defines F-C33-1/2/3, a different row). The
§3.1 outcome block pins the A/B protocol (metrics W1-W4,
identical-certified-outcomes guard) and §1.1's WIN RULE states
what-refutes-what, but no named C31 falsifier set exists. Landing the
§4.1 note as filed would write a choice-ledger reference to
non-existent pins — the exact R7 anti-entropy defect class, and the
falsifier-packaging half of refuter duty (e) unmet for C31.
**Witness:** PANEL_C31TRIO.md:909 (sole occurrence); §3.1 outcome
block :627-646 (no IDs); §4.3 :934-953 (C33's falsifiers).
**Repair (outcome stands after it):** define the set by transcribing
the already-adjudicated content — F-C31-1: [P-IPADJ] source
adjudication FAILS (semantics not certifiable) or measured
barrier-restart overhead outside the existing derived bands =>
incumbent-path certification REFUSED, F2 A/B becomes mandatory;
F-C31-2: A/B arm B beats arm A on W2+W3 at non-worse W1/W4 => flip
verdict of record; arm A wins => IP path certified and the flip
candidate closes; F-C31-3: guard violation (certified outcomes diverge
at the declared resolution) => protocol red, neither arm's numbers are
verdict-bearing. Or strike the sentence and reference "§1.1 WIN RULE +
§3.1(iii)-(iv)". Either repair is on-page; the split outcome is
unmoved.

### RC31T-2 — REPAIR-NEEDED — row C32 — claims-registry dedup miss (DIR-RKG) + arm-B pair-provenance under-specification

**Claims attacked:** §2.5 "Claims registry: `grep -n
"optimizer|trust-constr|interior"` -> :1253 ([X-TOCV] ...) + unrelated
hits (:476 Hoffman multipliers, :659 Lemma-B, :771 G0 spike) => no
prior adjudication claim of this cluster's questions. Absence claims
above are bounded by these exact greps." And §3.2 arm B: "SR1-carry
from certified accepted pairs + stale-symptom re-measure + [P-HESSREJ]
armed".
**Mechanism, three legs:**
(i) HIT SET MISREPORTED. Measured this window: the panel's exact grep
returns TEN hits — {476, 659, 771, 800, 1196, 1224, 1253, 1390, 1397,
1945} — not the four the panel names. "Bounded by these exact greps"
is false as stated (SR-12 class; wave-1 RC28-7/RC27-5 precedent, both
SUSTAINED).
(ii) THE DROPPED HIT :1196 IS MATERIAL. It is claims row **DIR-RKG**
(docs/claims_registry.yaml:1193-1204, kind=directive, scope "binding
policy for every brick-2 optimizer"): its scope field RECORDS the C32
incumbent policy as registered policy text — verbatim: "the driver of
record measures Jacobi scaling once + the FULL Hessian at every
segment base by forward differences of the exact adjoint gradient,
held frozen within the segment (policy-conformant: re-measured fresh,
NEVER CARRIED)" — and its falsifier field declares "a brick-2 run that
mixes gradients across a re-record event ... is NONCONFORMING". A
promoted SR1-carry (the panel's own F-C32-2 branch) edits a REGISTERED
DIRECTIVE's scope of record; the flip package must name the DIR-RKG
amendment, and the panel never cites DIR-RKG at all. (It is not a
prior adjudication of C32 — the absence CONCLUSION survives — but it
is the record carrier of the incumbent policy, and the panel's own
grep surfaced it.)
(iii) PAIR PROVENANCE UNPINNED. Arm B never states which gradient
pairs feed the update. Segment-base gradients are computed on
DIFFERENT recorded plans (each segment = fresh record); differencing
them is a CROSS-LOWERING gradient comparison, forbidden by the
standing discipline the panel itself declares binding on "every
engine/curvature consumer in this cluster" (§3.1-bis, citing findings
:328-336: every gradient COMPARISON or FD stencil pins ONE lowering),
and the measured M6 incident (findings :319-327: mixed-lowering
curvature => dH 18% = 5-6x scheme asymmetry, gate-REJECTED) is the
recorded failure mechanism of exactly this class. The valid
construction exists — the accepted-pair (base, accepted-trial) is
same-plan because the trial gradient is evaluated on the frozen plan
BEFORE the re-record — but the facet's determinism argument
(G4:254-261) does not state it, and the naive implementation
(differencing stored per-segment-base gradients) is the cross-lowering
one. Without the pin, arm B's "W1 PASS-by-construction is STATEABLE"
is incomplete: determinism yes, validity contract undeclared.
**Witnesses:** measured grep (10 hits); docs/claims_registry.yaml
:1193-1204 verbatim; findings :328-336, :319-327; facet G4:254-261.
**Repair (outcome stands after it):** (a) correct the §2.5 hit set and
disposition the six dropped hits (:800/:1224/:1390/:1397/:1945 =
token-noise, e.g. "interior cells"; :1196 = DIR-RKG, material); (b)
[P-QNCARRY] arm-B spec gains the pin "secant pairs SAME-LOWERING ONLY
(both gradients from one frozen plan / one compiled executable, C48
B-shape clause); the carried matrix crosses segment boundaries only as
a prior with flip-touched columns invalidated (facet G4 mechanism);
any cross-lowering pair is rejected at update time"; (c) the F-C32-2
promotion package names the DIR-RKG scope/falsifier amendment as a
landing item ("policy-conformant: re-measured fresh, never carried"
cannot survive a carry promotion unamended). [P-HESSREJ]/F-C32-1 would
catch the contamination downstream, but the known-mechanism guard
belongs in the arm spec, not in the crash barrier.

### RC31T-3 — AMENDMENT — row C31 — missing modern census line (IP warm-start repair literature) + axis-recency overstatement

**Claims attacked:** §2.1 warm-start bullet ("IP methods are
'notoriously difficult to warm-start' ... active-set SQP warm-starts
naturally"; newest cited item on this axis = arXiv:2207.03082, 2022,
plus undated Gould lineage and undated Knitro manual) and §2.0 "Every
row's census axis reaches >= 2024".
**Mechanism:** refuter counter-search (this window, search-level
evidence) surfaces an ACTIVE 2023-2026 primal-dual IP WARM-START
repair line absent from the census: WARP benchmark for primal-dual
warm-starting of interior-point solvers (arXiv:2605.05728, 2026 —
"first systematic diagnosis of why primal-only warm-starts fail");
dual-shifted projected-search interior-point method (COAP,
doi 10.1007/s10589-023-00549-1, 2023/24 — "shifts on the dual
variables allow the method to be safely warm-started"); central-path
smoothing warm-start for conic IPM (arXiv:2512.00693, Dec 2025). The
W3 doctrine sentence states a 2000s-2022 consensus as settled while
the modern layer is actively repairing it — the same overstatement
class as wave-1 RC28-6/RC911-12 (both SUSTAINED). The row outcome is
UNMOVED: scipy's tr_interior_point exposes no warm-start interface and
the 19-21 cold restarts are an implementation fact of record (findings
:1239) regardless of what the field can now do — but the incumbent
path's best case (duty c) and the [P-IPADJ] item "implementation
warm-start capability" are under-informed without the line.
**Carried fix:** add the line to §2.1 (ABS-tier, dated); restate W3 as
"primal-only warm-starts fail (WARP); dual-shifted/central-path-
proximal warm-starts are an active 2023-2026 repair line; the
incumbent IMPLEMENTATION exposes no warm-start interface — the cold
restart is of record regardless"; name the line as an input to
[P-IPADJ]'s warm-start item and to the A/B arm-A design; correct the
recency sentence for the Q1/W3 axis (its cited set tops out at 2022).

### RC31T-4 — AMENDMENT — cluster — anchor/attribution mis-cites (all objects real, all numbers of record)

**Verified this window, four fixes:**
(i) §1.0:48 "decisive rung 4560 s pre-M-chain — facet G4": the string
"4560" does NOT occur in the facet (measured grep, 0 hits); true
source = ADVISORY_engine_speed_audit_2026-08-12.md:475 ("21-segment
decisive rung 4560 s").
(ii) §1.0:46 "record 5.58-8.30 s median ... memory
s25bis-speed-complete": the memory carries 5.58 only; the 8.30 median
is PROGRESS_2026-08-12_S25bis_speed.md:329 (:116 gives fresh median
5.58 s [5.50, 5.58, 8.30]). Both numbers genuine, attribution split
across two carriers.
(iii) §2.2 "Dennis-Walker structured-secant lineage named there"
attributed to facet G4:254-261 — actually named at facet :266-267 (the
adjacent SOTA-reference paragraph).
(iv) §2.5 cava hit set "{1113-1121 block, 1241, 1244}": the measured
literal hit lines for the panel's exact pattern are {1118, 1119, 1120,
1241, 1244} (reproduced this window; content characterization — cava's
own numbering-collision family, no engine/curvature row — VERIFIED
correct on all five). State the measured lines; keep the block gloss
as gloss (RC28-7 precedent).

### RC31T-5 — AMENDMENT — cluster — §0-ter(a) query-table internal consistency

(i) The column legend says "Counts = links returned / included in
§2.1-2.3 one-liners", but Q8's 4 included items are cited in §2.4 —
legend should read §2.1-2.4. (ii) The brief's "hits/screened/included"
triple is reduced to two counts; the reduction is de-facto declared
but the screening semantics (what was screened out and by what rule)
is not — one sentence fixes it. (iii) Named-item reconciliation is
short at Q2 (Incl.=5; 3 named in §2.1 + ODYN cited elsewhere without
query attribution) and Q3 (Incl.=5; 4 named). Fix: attribute ODYN's
query, name or decrement the unnamed inclusions. No one-liner claim
above its stated depth was found.

### RC31T-6 — AMENDMENT — row C31 — incumbent-side representation completeness + one above-depth numeric + one false uniqueness claim

(i) V-F30's O3 option line "multiplier trajectories well-behaved for
the marginal-value certificates" (phaseA_tree_variational.md:1324-1326,
verified verbatim) is a genuine PRO-IP advocacy clause on the W2
multiplier axis; the panel's tree-advocacy paragraph quotes only the
large-active-set niche (:1336-1339). The incumbent-path case should
carry it — it is precisely what [P-IPADJ] adjudicates (duty c:
represent the incumbent's genuine case in full).
(ii) §2.1 "IP terminates at a small nonzero barrier value (typically
1e-6..1e-8)": a specific numeric range at [ABS] with no named source —
soften to qualitative or name the source (read-depth honesty,
§0-bis(b)).
(iii) §3.1 disposition 5: "SLSQP (in-env): the only other
inequality-capable scipy engine" is FALSE as written — COBYLA and
COBYQA are in-env inequality-capable `minimize` methods; they fall to
disposition 10 (adjoint-free-as-closer) by class, so the fix is one
word ("the only other inequality-capable GRADIENT-BASED scipy
engine"). Outcome unmoved on all three.

### RC31T-7 — AMENDMENT — row C32 — undeclared widening of a pre-registered criterion (g2(b))

The frozen WIN RULE (§1.2) promotes SR1-carry on "the [P-QNCARRY] A/B
on the recorded S18 walk"; §3.2's F-C32-2 requires success "on BOTH
pre-registered instances (S18 mild + one frontier-class walk)". The
tightening is conservative and well-motivated (the frontier instance
is where C28 makes the choice material) but it amends a pre-registered
criterion without the [AMENDED-AT-RECONCILE] marker the panel's own
write-order declaration promises for §1-relative changes. Fix: one
declared-with-reason marker at §1.2 or §3.2. (Checked the other two
rows for post-hoc drift: C31 and C33 adjudications decide exactly
along their frozen WIN RULEs — no drift found.)

### RC31T-8 — AMENDMENT — row C33 — F-C33-2's cost budget has no stated per-segment total

**Claim attacked:** §3.3 arm 1 "gm is one VJP per eval — cheap vs
record" and F-C33-2 "FD-of-gm cost exceeds its one-VJP-per-eval budget
on the real stack => cost premise false".
**Mechanism:** the budget is stated per-EVAL, but the policy consumes
(n+1) extra VJPs PER SEGMENT BASE (the FD sweep over ~10-11 points;
forwards shared with the objective sweep, one added VJP each). A
falsifier whose threshold is "one VJP per eval" cannot FIRE at a
defined line because no per-segment total or acceptance bound is
stated — the wave-1 RC911-3 defect class (asserted-derived threshold;
SUSTAINED). The record numbers to derive it from exist (replay
0.236 s, val_grad 0.449 s, segment 14.9-20.1 s pessimistic — all of
record, cited not re-measured): the duty must publish the derived
per-segment budget ((n+1) x measured VJP-marginal vs the segment
median, with its band) BEFORE first use of F-C33-2, the same
publish-before-first-use rule wave-1 imposed on F9a's promotion
threshold. Secondary text fix, same row: the §1.3 WIN RULE's
parenthetical "(it is not expected to ...)" telegraphs the expected
outcome inside a frozen criterion — move the expectation out of the
criterion into the adjudication (the burden assignment itself is
sound: the incumbent is an undeclared default of record).

### RC31T-9 — NOTE — row C56 (rider) — judge-schema coverage

The machine summary adds a fourth row key "C56-gradient-role" and §4.4
proposes a C56 status flip (MIXED -> ADJUDICATED). The consumption
itself is mandate-clean and source-verified: the ledger row's own
owner text addresses the gradient role to wave-2 C31TRIO
(choice_ledger.yaml:739, verbatim "gradient role OWED TO wave-2
C31TRIO (forecast, not consumed ...)"), and VERDICT_C9C11_supplement
§4.3 pre-authorizes exactly this landing-time verification ("the
landing VERIFIES that consumption occurred before writing it into the
row"). The §3.1-bis adjudication's four legs verify at source (O-F21
:1144-1148/:1162-1167 recommendation; census Q8 two-leg structure with
the internal O3.1/[X-A1IM] leg independent of the [ABS] web leg;
weight-role template at ledger :250; one-lowering contract :328-336).
BUT the wave-2 judge brief's per-row verdict list
(C31/C32/C33/C1/C2/C3/C49/C20/C21) does not include C56 — the judge
must adjudicate the C56 rider EXPLICITLY as an emergent row (accept,
amend, or defer to landing), not let it ride unexamined. One text nit
inside it: §3.1-bis "A fired F11d re-opens C56 ..., NOT C31 — carried
verbatim" — the row's note says "re-opens THIS row, not C11"; the
"not C31" half is the panel's (correct) in-context inference, not
verbatim carry — label it so.

### RC31T-10 — NOTE — cluster — reconciliation-honesty audit (duty of BRIEF_wave2_reconcile.md)

All four declared repairs are VERIFIED APPLIED in the file as it
stands: R1 (facet path normalized at first citation, §1.0:42 — the
file verifiably lives at validation/sota_gapmap_raws_2026-08-12/); R2
(census stamp describes THIS window and §2.0 exists); R3 (§1.4 axis-2
carries the [AMENDED-AT-RECONCILE] C56 correction — and the correction
is TRUE: C56 verified minted at choice_ledger.yaml:731-740); R4
(§1.0/§1.1 amendment blocks present, write-order declaration extended).
Every §1 "kept verbatim" citation spot-checked verifies at source
(facet :4-21/:36-39/:192-196/:200-203/:245-252/:254-261/:268-271;
kickoff :346-366/:404-413; a1_ideal_march_jax.py:504-517;
diff :159-175; findings rows; the §1.3-W4 KS-Hessian formula
INDEPENDENTLY RE-DERIVED by this refuter — correct; GAP-19 rho/4
arithmetic — correct). No kept section failing verification was
found; no claimed-but-unapplied repair was found. LIMIT, declared: the
partial was overwritten IN PLACE with no snapshot, so the
"written BEFORE any web query" write-order claim and the exact
kept-vs-repaired boundary are unverifiable ex post BY CONSTRUCTION.
Process lever for the landing: reconcile slots should snapshot the
partial (append-only, SR-10 pattern) before rewriting — cheap, and it
makes the next reconciliation declaration checkable.

---

## 2. ATTACKS RUN THAT DID NOT LAND (declared, so the judge sees coverage)

- **(a) Formalization:** hunted incumbent/challenger smuggling in
  §1.1/§1.2/§1.3 — the W5 env asymmetry is DECLARED not hidden; the
  "permanently inequality-bearing" premise survives all C28 branches
  (the margin governor inequality exists since S22 independently of
  GAP-1 — facet G3:189-191); the C33 burden assignment is grounded in
  the undeclared-default fact of record. Only RC31T-8's parenthetical
  survived as a finding.
- **(b) Census absence claims:** counter-searched the C33 "NO
  published exact-KS-Hessian recipe" claim — my search reproduces the
  panel's picture (ill-conditioning phenomenon + adaptive-parameter
  strategies, incl. the exact ScienceDirect 2015 IP-aggregation item
  the panel cites; no recipe) — absence claim STANDS at its stated
  depth. The literature-registry 0-hit grep REPRODUCED (0 hits). The
  ledger explorer-grep REPRODUCED (:654 only). The cava content
  characterization VERIFIED on all five measured hit lines.
- **(c/d) Adjudication both sides:** the 4/4-as-evidence discipline is
  honored (the panel itself softened "4/4 reject IP" to "0/4 recommend
  IP as closer" and disclosed P-F27's bundling and V-F30's niche —
  verified at tree sources); no tree position transplanted without
  recalibration was found beyond RC31T-4(iii)'s line-ref nit; the
  quarantine of adjoint-free is the trees' own 4/4 position verified
  at source (O-F16 :915-930/:953-955, H-F36 :1117-1123/:1131-1134,
  V-F30 :1329-1330, P-F27 :1001-1004/:1026).
- **(e) Pins:** C32's F-C32-1/2/3/4 partition cleanly (close-on-fresh /
  promote / reject-carry / close-HVP) and the determinism bit-compare
  is absolute — no falsifier hole found beyond RC31T-2(iii)'s
  provenance pin and RC31T-8's budget. C33's F-C33-1 is a genuine
  incumbent-comeback branch (the adjudication is falsifiable).
- **(f) Dedup:** the C56 consumption is NOT a re-mint (debt discharge
  pre-authorized by the supplement); the KS-structured arm is labeled
  panel-derived, claims no literature import, and is proposed as a
  protocol arm not a row; the exploration-tier candidate row §4.5 is
  dedup-proven by a grep I reproduced. No verdict of record
  contradicted without declaration.
- **(g) Wave-1 consumption:** all three load-bearing quotes verified
  verbatim against VERDICT_wave1 (§2.1 F-2 "escalate to the engine
  re-adjudication ([P-IPADJ]/C31, bundle fallback named)"; "[P-IPADJ]
  on the same critical path"; §2.2 band-block structure incl. k_max;
  §3 B-stationarity qualifier rule "inherited verbatim" — it is).
  Wave-1 carried ZERO escalations, so no conditionality declaration
  was owed. No advocacy source double-counted as two independent
  validations (O-F16's two uses are different option blocks of one
  fork, declared; the O-F21-item-6 shared use across C32/C33 is the
  diff's own assignment, cited as shared).
- **(h) Route facts / speed numbers:** custom_vjp+defvjp-only VERIFIED
  at a1_ideal_march_jax.py:504-517; every HVP option in the panel is
  N5-gated (no undeclared route change anywhere); one-lowering carried
  (except the arm-B application gap = RC31T-2(iii)); NO re-measurement
  of recorded speed numbers found — every number is cited, and the two
  attribution slips are RC31T-4(i)/(ii). Scipy claims INDEPENDENTLY
  RE-VERIFIED on the installed pinned env (read-only): method switch
  verbatim at minimize_trustregion_constr.py:403-406; NonlinearConstraint
  hess=None -> BFGS() instantiation at _constraints.py:124-128 (the
  panel's "docs' convenience default" claim is source-true).
- **(g2) §0-ter:** decision criteria pre-registered and decided-along
  (except RC31T-7's declared-late widening); materiality honest in
  both directions (C33's decide-now/build-gated split is the cheap
  arm, not ritual depth); steelman present for every closed option
  (bundle at its 2024-2026 best; DFO at the 2025 review; IPOPT closed
  on structural grounds that survive RC31T-3's added line);
  read-depth markers present, one above-depth numeric = RC31T-6(ii);
  axis-bearing sentences present and correct for all five axes
  (axis-3 non-bearing verified against the landed C9 row :228).

---

## 3. VERBATIM-QUOTE AUDIT DECLARATION

Every quotation this refutation relies on was re-read at source in
this window: choice_ledger.yaml rows C31 :452-464 / C32 :466-474 /
C33 :476-485 / C48 :643-651 / C49 :653-663 / C9 :219-228 /
C11 :240-250 / C56 :731-740 (owner :739, note :740);
findings_registry.yaml :1236-1244 / :1245-1253 / :1254-1262 /
:1263-1271 / :1272-1280 / :319-327 / :328-336 / :817;
claims_registry.yaml :1193-1204 (DIR-RKG, verbatim scope + falsifier);
facet s24_gap_driver-nonsmooth.md :1-60 / :180-274; kickoff
:330-424; a1_ideal_march_jax.py :500-518;
ADVISORY_S25bis_diff_convergence :112-125 (B-F11 :119);
ADVISORY_engine_speed_audit :436-449 (N5 :442) / :594-606 (7.3) /
:475 (4560 s); PROGRESS_S25bis :116/:329 (via grep); memory
s25bis-speed-complete :14-18; trees O-F16 :900-960, O-F17 :964-992,
O-F21 :1141-1183, O-F23 :1225-1249, H-F36 :1106-1140, V-F24
:1074-1105, V-F30 :1311-1342, P-F27 :989-1031; diff :155-179;
VERDICT_wave1 §0/§1/§2/§3/§4/§6 (in full);
VERDICT_C9C11_supplement :196-235 + :14-16/:68 (via grep). Measured
greps of this window: panel "F-C31" (1 hit :909); facet "4560"
(0 hits); repo "4560" (speed audit :475); cava panel-pattern
({1118,1119,1120,1241,1244}); ledger explorer-pattern (:654 only);
literature registry panel-pattern (0 hits); claims registry
panel-pattern (10 hits: {476,659,771,800,1196,1224,1253,1390,1397,
1945}). Installed-scipy verification was READ-ONLY (inspect/getsource
on the pinned env; no installs, no mutations). Web counter-searches:
2 queries, search-level evidence only, used solely for
census-completeness (RC31T-3) and for a failed refutation declared in
§2(b).

## 4. DEDUP REGISTER

- RC31T-2's DIR-RKG interaction: grep "DIR-RKG" across
  choice_ledger/findings/blocco3 — the only non-kickoff mention is
  findings :817 (radius semantics, different object). Not carried
  anywhere; fresh.
- RC31T-3's IP warm-start line: literature_registry grep "warm.?start"
  = 0 hits; not in the panel's census; fresh (WANTED-tier candidates
  ride the panel's existing §4.4 rider if sustained).
- RC31T-1's phantom IDs: "F-C31" unique to panel :909; fresh.
- RC31T-8's budget derivation: no existing findings/ledger row pins an
  FD-of-gm per-segment budget (GAP-19 row :1272-1280 carries the
  recipe, no budget); fresh.
- No finding above re-mints a registry row; repairs are proposed as
  amendments to the PANEL/duty text, never as ledger edits (landing
  window owns those).

## 5. MACHINE SUMMARY

```json
{
  "cluster": "C31TRIO",
  "findings": [
    {"id": "RC31T-1", "class": "REPAIR-NEEDED", "row": "C31"},
    {"id": "RC31T-2", "class": "REPAIR-NEEDED", "row": "C32"},
    {"id": "RC31T-3", "class": "AMENDMENT", "row": "C31"},
    {"id": "RC31T-4", "class": "AMENDMENT", "row": "cluster"},
    {"id": "RC31T-5", "class": "AMENDMENT", "row": "cluster"},
    {"id": "RC31T-6", "class": "AMENDMENT", "row": "C31"},
    {"id": "RC31T-7", "class": "AMENDMENT", "row": "C32"},
    {"id": "RC31T-8", "class": "AMENDMENT", "row": "C33"},
    {"id": "RC31T-9", "class": "NOTE", "row": "C56"},
    {"id": "RC31T-10", "class": "NOTE", "row": "cluster"}
  ],
  "breaks": 0,
  "repairs": 2,
  "amendments": 6,
  "notes": 2
}
```

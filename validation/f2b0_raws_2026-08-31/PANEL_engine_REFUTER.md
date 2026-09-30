# PANEL — F2-B0 ENGINE CLUSTER, REFUTER OF RECORD
# Window: F2-B0, 2026-08-31. Form-2 panel, SURFACE A {C31, C32, C37,
# C57, C58, C60, [P-IPADJ], SDP-CAND-8} (decision map :199-206).
# Mandate: attack the INCUMBENT cases and the DUTY SPECS as written —
# not the alternatives (separate advocate). Read-only session; every
# anchor below was opened/grepped in THIS window (SR-12 discipline);
# no engine run, no package touched.
# Severity: KILL = the cited claim is false/unfireable at its anchor;
# WEAKEN = support materially weaker than the row reads; NOTE =
# precision item / verified-survives item.

------------------------------------------------------------------------------
## R1 — C58 incumbent (JAX-primary per G0)

**REF-1 (KILL — on the row's claim as written).** The C58 row states
the incumbent support: "loop-speed falsifier ARMED and subsequently
NOT FIRED by the S25/S25-bis measured MET program"
(`engine_cluster_ledger_rows.md` C58; same wording in
`docs/choice_ledger.yaml` C58). This is FALSE at its anchors: the T2
practicality falsifier **FIRED of record at S18** — "T2 practicality
falsifier FIRED of record (121.6 s vs 35.9 s, curvature+re-record
decomposition, T1/T2a pass) => G0 re-decision review queued"
(`docs/claims_registry.yaml:1252`, X-TOCV row); "'T2 fired' = the S18
verdict that opened the review queue, consumed at S25 with no flip"
(`docs/glossary.yaml:323`); "practicality falsifier FIRED on the twin
case (121.6 s vs 35.9 s)" (`docs/rde_nozzle_MASTER.md:3280`). Earlier
still, T2a FAILED-AS-IMPLEMENTED at S17 (39.8 s vs 1.144 s bound) and
CLOSED the production gate (`docs/rde_nozzle_G0_decision.md:148-159`).
The true history is: fired (S17 as-implemented; S18 of record) →
root-caused → remediated → review consumed at S25 with NO FLIP
(structural cost, not language throughput; G0 doc :172-198).
Tasking note: the brief's "S20 T2 firing" is a mis-cite — the firing
is S18 (S20 is the adaptive-obstruction session). Honesty cuts both
ways: the CORRECTED support ("fired twice, adjudicated no-flip with
measured root cause, then repaired 100.84→25.49 s") is STRONGER
evidence for the incumbent than "never fired" — but the row as
written misstates the record and must be repaired before the 9(e)
sweep consumes it.

**REF-2 (WEAKEN).** "adjoint overhead 1.5 percent measured" is the
UNIT-PROCESS standalone microbenchmark (G0 doc :47-59), carrying the
doc's own caveat "the standalone unit-process timing does not bound
the assembled loop — declared" (:139-140). The engine-scale number of
record is grad/solve = **1.593** (X-LSG0 clean host, S18 note, G0 doc
:166-168) — 59% overhead, still T1-PASS (<= 4). Citing only 1.5% in
the row is selective; the honest support is "T1 = 1.593 <= 4 at
engine scale".

**REF-3 (WEAKEN).** Re-runnability today of the cited executable
evidence: X-G0 (the 52/52 rejector) and X-GENOXC (218/218) are
ON-DEMAND carriers OUTSIDE the CI suite — `ondemand: "env=jax;
pass=2026-07-16; suite=none"` (`docs/claims_registry.yaml:767-769`),
`ondemand: "env=gfortran; pass=2026-07-20; suite=none"` (:795-797) —
so "standing cross-code regression" (G0 doc :27, :243) is not what
the registry records: both are dated July-2026 passes. Worse, the
GENO reference is TODAY not in its of-record state: "patch
strumentazione NON inerte nel working tree GENO (MoC_Gen_m.f90 +42,
Profile_m.f90 +95 incl. AUDIT VARIANT B ...); build WSL ultima = link
error; quarantena + ri-baseline md5 = passo BLOCKING F2-B0"
(`docs/rde_nozzle_PROGRESS.md` GENO-health row; restore command
pre-verified in `ADVISORY_F2B0_prompt_2026-08-31.md:38`). And the
staleness lint that guards these pass stamps is itself P0-defective
(`audit-scert:staleness-import-closure-blind` +
`future-pass-dates-accepted`, F2-B0 order 4). The G0 numbers are true
AT THEIR DATED ANCHORS; none is re-verifiable in-window until B-GENO
clears.

**REF-4 (NOTE).** Discharge semantics: S25/S25-bis did NOT discharge
the falsifier — it remains ARMED on its declared trigger ("a future
T2a failure on this path would be STRUCTURAL and triggers the flip
clause directly", G0 doc :169-171; T1 > 4 the other leg), with the
S25 review consumed no-flip and the T2 lhs REPRICED (n_eval_actual x
t_value_and_grad, :182-185). MET results (segment 14.9-20.1 s vs 30)
are passes-with-margin under the repaired pricing, not a retirement
of the falsifier. Any 9(e) verdict must carry the falsifier forward
armed, not cite MET as closure.

**REF-5 (NOTE).** What a 9(e) delta-sweep must check that the G0 doc
does NOT cover (the honest delta list):
(a) Julia/Enzyme still NEVER benchmarked on this host (G0 doc
:199-201, unchanged honesty row) — the "JAX over Julia" leg rests on
exercised-vs-unexercised, now 6 weeks staler vs the 2026 landscape;
(b) two of the row's four alternatives were NEVER weighed by G0 at
all: "hand-coded adjoint" and "gradient-free foundation" (G0 §3 is
JAX-vs-Julia only; gradient-free contradicts nothing in G0 because
G0's criteria presuppose gradients — it can only be adjudicated by
the re-anchored census);
(c) the ENTRY CONTRACT obligations post-date G0 entirely: C56
one-lowering discrete-AD weight + F11d, C31 information-only
multiplier discipline, C32/C33 curvature pins, C48 one-lowering /
cross-lowering-gradient-floor, C57 adjoint-free tier — the census
must check each framework can REALIZE these (e.g. one-frozen-plan
compiled-executable identity, bit-transparent record/replay);
(d) float64/mixed-precision sub-axis — assigned to C58 by
`FOUNDATION_ENUM_census_c4.md` §3 (:61); G0 mentions float64 only as
a benchmark condition (:50), never as an adjudicated policy;
(e) framework-inherent structural-cost class: XLA re-trace/module
blowup (S17 measured crash), padded-bucket + plan-as-args engine
cache workarounds, vmapped-Hessian M6 — the maintenance price of the
M-chain is JAX-specific engineering the "which foundation best
realizes the architecture" question must weigh cross-framework;
(f) env currency: jaxlib cp313 GIL wheel (N7 declare-not-adopt,
`ADVISORY_engine_speed_audit_2026-08-12.md:445`), numpy 2.5.x O5
pending;
(g) GENO interop leg re-verification post-B-GENO quarantine (REF-3).

**REF-6 (WEAKEN — window coherence, applies to C58 AND C60).** The
derived roadmap places C58/C60 in the F2-B0 node set (:39-40) AND
re-consumes them inside F2.REPR: "stack C58/C60; the 3-D COUNTERPART
decided here at convergence with the census protocol"
(`docs/ROADMAP_critical_path.md:43`); PROGRESS NEXT lists the engine
cluster at item (3) and "dossier S-5F/C51/C58/C60" at item (6). A
F2-B0 adjudication of C58/C60 to closure BEFORE the representation
ladder is decided is therefore sequenced against its own roadmap: a
2.5D/3D representation outcome re-prices the AD-framework and
architecture questions. The F2-B0 verdict must be explicitly
representation-conditional or pin a declared re-entry trigger at
F2.REPR — otherwise it decides at the wrong scale.

**What survives R1:** the carriers exist on disk with negative
controls (X-G0/X-G0AX/X-GENOXC files verified present); every G0
number checked is true at its dated anchor; the S17→S18→S25 firing/
remediation/review chain is fully documented and coherent; the
corrected incumbent case (falsifier live, fired, survived root-cause
adjudication, MET repaired) is STRONGER than the row's compression.
Julia-not-benchmarked is declared, not hidden.

------------------------------------------------------------------------------
## R2 — C60 incumbent (NAND practiced)

**REF-7 (WEAKEN).** The two deferral texts are refereed but DATED
one-liners, and by their own words NOT adjudications:
`docs/rde_nozzle_pipeline_audit.md:105` is a table cell — "one-shot
LNKS now (two immature solvers composed — deferred, not dismissed)"
— in the D7 closing audit dated 2026-07-16 (:3);
`docs/rde_nozzle_general_scheme_panel.md:29` is a Step-3 parenthesis
"(full-space LNKS deferred — two immature solvers composed,
adjoint-opt feasibility refutation)". Both predate brick 2 (S17/S18,
2026-08-06): the premise "two immature solvers" is STALE — the
reduced-space forward+adjoint+driver stack is now mature/certified
(X-TOCV VERDICT PASS, MET program), so the cited cause no longer
describes the stack. The texts cannot be cited as standing support
for keeping NAND unweighed; they are the record of a deferral whose
stated reason has half-expired. (They came out of the 16-agent
refereed process, so "aside" is too weak — "dated refereed deferral,
premise partially expired" is exact.)

**REF-8 (NOTE).** The three NAND supports (certificates on converged
states; MET speed; compiled-chain record) prove NAND-SUFFICIENT, not
SAND-INFERIOR. None excludes SAND or hybrids: a SAND/LNKS run
terminates at a converged KKT point where the same converged-state
certificates can be evaluated post-hoc, and the alternatives list
itself contains "hybrids (reduced-space outer loop with full-space
inner corrections / one-shot warm-started terminal phases)". The row
is honest about exactly this (status NEVER, "never weighed vs SAND in
this ledger", flip re-enters via pinned falsifiers) — the refutation
lands on any panel member tempted to read the supports as a
head-to-head result, not on the row.

**REF-9 (NOTE — the pin asked for).** The repo object that would
break under naive SAND: per-cell certification consumes the UNDAMPED
NEWTON STEP norm on CONVERGED forward states —
`validation/a1_toc_variational_jax.py:941` ("if not stp <=
A1.NEWTON_TOL_FACTOR * EPS * scd"), :950, :364, :1000 — plus the
replay/record machinery, O3.1 identities, and the X-GENOXC truncation
band, all defined on converged fields. Under SAND, intermediate
iterates are not converged states, so per-iterate certificate
semantics would need re-derivation (terminal-phase certification
survives). CAVEAT: the wave-3 judge's anchor for this pin
("a1:433-448", VERDICT_wave3 §5 R3REMENG-1) has DRIFTED — those lines
now hold M5c column-chain code; the pin lives at the lines quoted
above. Any C60 verdict citing a1:433-448 inherits a stale anchor.

**REF-10 (WEAKEN).** Scale relevance: a NAND-vs-SAND head-to-head at
the current 4-field axial n~10 dense per-segment NLPs would measure
almost nothing decision-relevant — SAND/LNKS economics (one coupled
KKT system vs nested solves) differentiate at the 2.5D/3D
representation scale that F2.REPR decides NEXT (REF-6). As specified
("adjudicated as a CLUSTER ... trigger = the F2-entry engine act"),
the C60 window sits BEFORE the information that makes the question
material. The coherent duty is an adjudication conditional on the
F2.REPR outcome, or an explicit finding that at the current scale the
question is immaterial-by-measurement.

**What survives R2:** the incumbent-declared mint is honest and
well-formed (practiced supports are real measurements; dedup grep
reproduced; no-row class correctly named); FORK_LEDGER D-1 (O15)
rider executed as claimed; nothing in the record pretends SAND was
weighed.

------------------------------------------------------------------------------
## R3 — C57 incumbent (local-only)

**REF-11 (WEAKEN).** "no global layer was ever adjudicated
(directive-axis verification 2026-08-19)" is false as an unqualified
sentence. `docs/rde_nozzle_pipeline_audit.md:105` (D7, refereed,
2026-07-16) WEIGHED "deflated continuation · DIRECT/branch-and-bound
· moment-SOS" and ADOPTED "deflation; certified B&B at 2-4 DOF",
rejecting moment-SOS with cause; :107 adopts the "M1-M5 ladder" for
global optimality; M0 defines the mechanism of record — "M4
exhaustive stationary-point enumeration (deflated continuation) +
bound gap" (`docs/rde_nozzle_MASTER.md:3000`). That is an
outside-ledger adjudication of the global question — the same
"weighed of record OUTSIDE this ledger" shape the C60 mint names for
NAND/SAND. The true statement is "no LEDGER row; never head-to-head
vs the modern DFO/BO/evolutionary tier". Note also that C57
alternative 3, "multi-start continuation on the existing branch
machinery (V-F26/V-F7 line)", is essentially the ALREADY-ADOPTED M4
posture — the row lists as an alternative what the audit already
adopted, which the incumbent statement ("none") obscures.

**REF-12 (NOTE).** "The architecture already owns the global
question" would be a rationalization if cited to close C57: M4 is a
DECLARED mechanism at SCHEMA level in M0 (:3000), nothing built; the
tournament lives on `ROADMAP_critical_path.md:24` as F3.TOURNAMENT —
**NOT-OPENED**, `path: non-critical`, "no named D6 step of record"
(finding plan:full-envelope-tournament-no-named-d6-step). The sector
tournament owns TOPOLOGY-level enumeration, not in-sector
multi-modality. So neither "a global layer is redundant by
architecture" nor "a global layer is needed" is measured — which is
exactly what the user-ratified pilot converts into a measurement. The
C57 window may cite the M4/tournament machinery as the incumbent's
declared apparatus, never as executable evidence.

**REF-13 (NOTE).** Pilot ratification consistency: the ratification
text pins "execution and priority are decided at this row's
adjudication window (F2-entry), JOINTLY with the S-5F and
C49-explorer build decisions" (C57 note). The S-5F and C49 build
decisions sit at F2.REPR (`ROADMAP_critical_path.md:100-101` +
PROGRESS NEXT item 6). Therefore: deferring the pilot
execution/priority decision from F2-B0 to F2.REPR is CONSISTENT with
the ratification (F2.REPR is an F2-entry window and is where the
joint inputs exist — the joint clause structurally forces it there);
what would BREACH the ratification is (a) deciding execution at
F2-B0 alone without the S-5F/C49 table, or (b) pushing the decision
past F2.REPR (e.g. to the C49 build execution), which would violate
"decided at this row's adjudication window (F2-entry)".

**What survives R3:** the incumbent's PRACTICED half is true (every
recorded walk is local from continuation/warm starts; no global
layer exists in code); the pilot experiment is well-formed (one
case, three deliverables, purpose-of-record naming the
constitution-bias residue) and its CANDIDATE-only status is
respected by the record so far.

------------------------------------------------------------------------------
## R4 — C31 [P-IPADJ] spec

**REF-14 (WEAKEN).** F-C31-1's second leg cannot fire as specified:
"measured barrier-restart overhead outside the existing derived
bands" (VERDICT_wave2 §1.1 RC31T-1; WIN RULE, PANEL_C31TRIO:131-135)
references "existing derived bands" that DO NOT EXIST as an object
anywhere I could find: the panel itself concedes "in-band restart
overhead — is exactly the unexecuted adjudication"
(PANEL_C31TRIO:630), and the findings row grades the restart
measurement "optional S18-mild A/B for barrier-restart overhead"
(`docs/findings_registry.yaml:1331`). No derived band for restart
overhead exists in the registries or panels (grepped). Spec repair
required at this window: [P-IPADJ] must DERIVE and NAME the band (or
re-word the leg to "outside a band derived in-window from the
S18/S24 walk records") — otherwise the leg is a dangling reference
and arm-A certification has an unfireable criterion.

**REF-15 (NOTE).** F-C31-2 is not fireable today BY DECLARED DESIGN:
arm B (Uno filtersqp preset) is not installed — install is an
O5-class session-boundary user decision (W5 asymmetry, declared
PANEL_C31TRIO:125-130; version-stamp duty DOSSIER §3 item 10:
paper=2.2.0 vs clone=v2.8.0, re-verify presets at installed
version). W2 instrumentation: instruments 1-2 "land WITH [P-IPADJ]";
only instrument 3 (LSQ referee) is licensed NOW on recorded
artifacts (VERDICT_wave3 §5, R3REMENG-7 branch (a)). So of the three
falsifiers, today only F-C31-1 leg A is executable end-to-end.

**REF-16 (WEAKEN).** The "information-only multiplier discipline" is
a PAPER RULE, not an enforced invariant: no assert/lint anywhere
enforces it (grep "INFORMATION.ONLY" over validation/tools/tests
*.py: hits are comments/prints only). The three committed res.v
consumption sites diverge: (a)
`validation/a1_toc_variational_jax.py:2356` — print-only instance
reading, conformant; (b) `validation/def_twin_falsifier.py:1230` —
print-only under the S24-T1 convention mu(M0) = **-res.v[-1][0]**
(:40-41), conformant; (c) `validation/margin_governor.py:620-622`
reads mu_est = **+vlist[-1][0]** (OPPOSITE sign convention, no
negation) and at :645-649 feeds it to `mu_dual_clause`, whose result
GATES the carrier verdict ("ok &= dok") — a committed carrier's
PASS/FAIL rests on the sign of an [P-IPADJ]-unadjudicated quantity.
Two practiced sign conventions + one verdict-bearing consumer =
falsifier-one's semantics leg is LIVE and material (supports the
duty's necessity), and "the discipline is practiced" is only 2/3
true on disk.

**REF-17 (NOTE).** The one in-driver multiplier instrument has a
vacuous branch: `margin_governor.py:638` forces mu_use = 0.0
whenever the margin is inactive, then `mu_dual_clause` (:462-466)
"checks" mu == 0.0 at inactive margins — a tautology at the call
site. The of-record smearing symptom this check exists for ("S24
res.v = +4.8582e4 at an INACTIVE constraint", PANEL_C31TRIO:112-115)
can NEVER fire it; slack=0.0 makes the printed |mu x slack|
identically zero. The [P-IPADJ] spec should name this as an
instrument to repair, not cite it as existing enforcement.

**REF-18 (NOTE — verified, SURVIVES).** The BHN equation-level
anchor set is ON DISK and EXACT:
`literature/byrd_hribar_nocedal_1999_interior_point_nlp_siopt9.pdf`,
p.879 (PDF p.3): Algorithm I step 2 "Set mu <- theta mu, eps_mu <-
theta eps_mu" with theta in (0,1) — the (mu, eps_mu)
constant-factor reduction law as the ledger states; Eq. (2.3) E(x,s;
mu) = max(||grad f + A_h l_h + A_g l_g||_inf, ||S l_g - mu e||_inf,
||h||_inf, ||g+s||_inf) — the 'optimality' source semantics; p.884
(PDF p.8): Eq. (3.15) lambda_k = lambda^LS(...) — subordinate
least-squares estimates — and the verbatim sentence "This approach
could just barely be considered a primal-dual method...". All three
anchors verified at equation level this window. Caveat carried:
paper-on-disk is not scipy-conformance — establishing that
`tr_interior_point` implements THESE equations is [P-IPADJ]'s own
first act, and the DOSSIER §3 inputs (termination alphabet, no
warm-start API, Hessian-degrade warning, preset-fidelity bound)
give F-C31-2/3 a complete guard vocabulary.

**What survives R4:** the falsifier TRIO is structurally sound
(leg-A source adjudication executable today against verified
anchors; F-C31-3's guard alphabet exists via DOSSIER item 1; the
conditioning rider falsifier-two-on-falsifier-one is coherent); the
S24 +4.86e4 symptom and the 19-21 cold restarts are genuine
of-record facts motivating the duty; the 10 arm-B spec inputs are on
disk and verbatim-consumable.

------------------------------------------------------------------------------
## R5 — [P-QNCARRY]+[P-HESSREJ] (C32) and F2-C37-FLIPMAT

**REF-19 (NOTE — owner windows).** (i) is satisfied with one
ambiguity: C32 and C37 ledger rows sit in the derived roadmap at
F2-B0 (`ROADMAP_critical_path.md:39-40`); duty EXECUTION is ordered
"after [P-IPADJ]" (VERDICT_wave2 §2.2), and C31 sits at F2.ENGINE
(:53) — so F2-B0 adjudicates/confirms the specs, F2.ENGINE executes.
The "G0/T2" token in both owners is ambiguous: the queued G0/T2
review was CONSUMED at S25 with no flip (`docs/glossary.yaml:323`),
while `findings_registry.yaml:1443` names a "scheduled G0/T2 review
(F2 entry, census row 7)" — the owners are readable as the F2-entry
review (this window), but a landing edit should disambiguate, else
the duties point at a consumed window.

**REF-20 (NOTE — rejectors CAN fire, SURVIVES, with the seeded
failures named).** [P-HESSREJ] is anchored in a real findings row
with named instruments: `driver-nonsmooth:hessian-no-rejector`
(`findings_registry.yaml:1333-1337`) — "symmetry-defect band
[pre-symmetrization] + directional-Richardson rejector remain
absent"; PARTIAL DELTA S25-bis (nonfinite-lane guard + hess_lane
counter) already landed. Concrete seeded failures that make each
FAIL: [P-HESSREJ] — an FD column straddling a knot/plan seam
(named in the row as the real kink risk, "column O(1) wrong") or an
injected pre-symmetrization asymmetry must be flagged; if the built
rejector passes them, [P-HESSREJ] FAILS its own negative control.
[P-QNCARRY] — feed one CROSS-LOWERING secant pair (gradients from
two compiled plans): the spec REQUIRES rejection at update time
(RC31T-2 repair (b)); acceptance = spec violated. F-C32-3 is
concrete: "two-run bit-compare of the carried matrix"
(PANEL_C31TRIO:786, :793) — nondeterminism fires it outright.

**REF-21 (WEAKEN).** F-C32-2 cannot fully fire today: the promotion
criterion requires "BOTH pre-registered instances" (RC31T-7,
declared-with-reason) = the recorded S18 walk (exists) + the C28
frontier instance (does NOT exist — C28/GAP-1 window sits at
F2.ENGINE, :53, and its [P-BSTAT]/[P-CERTKS] duties are unexecuted).
Promotion is therefore future-gated on an artifact yet to be
produced; the spec nowhere says so explicitly. Not fatal (the
NEGATIVE branches F-C32-1/3 can fire on the first instance alone),
but the panel should declare the asymmetry: the carry can LOSE
today, it cannot WIN today.

**REF-22 (WEAKEN).** F2-C37-FLIPMAT's benign proxy, leg 1: "flips
whose certified-class (S,xi) labels are unchanged across the
boundary under the adopted O-F19/H-F11 loci logging" (VERDICT_wave3
§5; ledger C37). "Adopted" holds only at the FORMAL-FRAME level
(PANEL_REMENG:375-389: "Formal frame adopted from the trees ...
logged as (S,xi) stratification loci (H-F11)"); NO loci/
stratification logging exists in any committed .py (grepped
validation/ — zero hits). Leg 2 ("discarded-Hessian columns are
lip-only") is the executable-today path ONLY IF the segment records
retain per-column Hessian data across re-record events — not
verified on disk by me, not asserted anywhere I found. "The census
is thereby executable merge-free" therefore over-claims
TODAY-executability: it is executable-after-instrumentation (leg 1)
or conditional-on-record-content (leg 2). The spec needs one landing
line naming which leg carries the census and what instrumentation
must land first.

**REF-23 (NOTE).** The F-C37-1/2 cycle break is REAL as logic, not
verbal: the old cycle (census gated on merge gated on census,
R3REMENG-6) is broken because the proxy classifies flips WITHOUT
running any merge, and F-C37-2 (bit-identical replay inside the
derived band) only ever licenses merges on the proxy-flagged subset,
with the disagreement clause RETIRING the proxy
(`docs/glossary.yaml:1326`). Seeded failure for the pair: merge one
proxy-benign flip whose replay leaves the band — F-C37-2 fires,
proxy retired, lever dead (VERDICT_wave3 §10 "F-C37-2 violation
kills the lever"). No circularity remains; the residual risk is
REF-22's instrumentation gap, not the logic.

**What survives R5:** both C32 duties and FLIPMAT have owner
windows reachable from F2-B0, anchored findings rows, and rejectors
with nameable seeded failures; the cycle break stands; the
same-lowering pin (C48 B-shape) and DIR-RKG amendment landing item
are internally consistent with the standing cross-lowering
discipline.

------------------------------------------------------------------------------
## R6 — SDP-CAND-8

**REF-24 (WEAKEN — and the plain statement).** Nothing in the built
record CONSUMES an SDP backend. Measured this window: `grep -icE
"SDP|Clarabel|MOSEK" docs/choice_ledger.yaml` = 0 (matches the
census's own SR-12 grep); no `import clarabel|cvxpy|mosek` anywhere
in validation/ tools/ tests/ src/; the certificate stack of record
is Lanczos + Kaniel-Paige brackets + directional cross-check
(VERDICT_wave2 §2.2), not SDP; the tournament's premium_bound is a
bound-difference THEOREM device (`rde_nozzle_P1_sections_5_7.md:471`),
not SDP; moment-SOS was REJECTED with cause
(`rde_nozzle_pipeline_audit.md:105` "SDP scale explosion"). The only
consumer ever named is the SOS head-to-head bound comparison — for
which the S17 user decision (Clarabel primary + MOSEK academic
fallback) was taken — and that item survives ONLY in archives
("RESTANO: head-to-head SOS (gate env: solver SDP = decisione
utente)", `PROGRESS_ARCHIVE.md:1899, :1934`); it is ABSENT from the
living PROGRESS (grep "SOS" docs/rde_nozzle_PROGRESS.md = 0 hits).
Said plainly, as tasked: **minting C63 today would create a row
whose duty has no live consumer** — a falsifier with no carrier and
no window that runs an SDP solve. The E4 edge's premise ("the
certificate-solver stack is on the SAME F2-entry decision surface")
overstates: there is no SDP certificate-solver stack IN the F2 stack
to put on any surface.

**REF-25 (NOTE).** Events that would make the row live (any one
suffices, each with an existing hook): (i) the SOS head-to-head is
re-queued and executed (bound-ladder M5-class act; its env gate and
solver decision are already of record from S17) — the natural
trigger; (ii) moment-SOS/premium-bound revival at F3.TOURNAMENT
(currently rejected-with-cause — a revival needs that rejection
overturned first); (iii) a certificate re-formulation adopting
LMI/SDP relaxations (e.g. if the Lanczos/KP S* form fails its
[P-BSTAT]-window falsifiers and an SDP bound replaces it). Absent
these, retire-with-named-reason at this window is the
census-consistent outcome — the census itself pre-declared exactly
this branch ("if the SDP layer is retired from the F2 stack, it dies
with a named reason", `FOUNDATION_ENUM_census_c4.md` §5).

**What survives R6:** the candidacy record itself — owner + trigger
assigned so the question cannot close by omission
(never-postpone rule respected, census §6); the S17 solver decision
is real and of record; the mint-OR-retire framing already contains
the honest outcome, so the duty spec needs no repair, only the E4
wording does.

------------------------------------------------------------------------------
## TALLY

- KILL: 1 (REF-1)
- WEAKEN: 11 (REF-2, REF-3, REF-6, REF-7, REF-10, REF-11, REF-14,
  REF-16, REF-21, REF-22, REF-24)
- NOTE: 13 (REF-4, REF-5, REF-8, REF-9, REF-12, REF-13, REF-15,
  REF-17, REF-18, REF-19, REF-20, REF-23, REF-25)

Worst single finding: REF-1 — the C58 row of record asserts its
central falsifier "armed and subsequently NOT FIRED" while the
claims registry, glossary and M0 all record it FIRED at S18 and
consumed no-flip at S25; the row must be repaired before any 9(e)
sweep cites it (the repaired statement is stronger, but that is for
the row to say, not the sweep to assume).

Cross-cutting for the judge: REF-6/REF-10 (C58/C60 double-booking
with F2.REPR) is the one finding that constrains the WINDOW's own
verdict shape: SURFACE A closures on C58/C60 must be
representation-conditional or carry a declared F2.REPR re-entry
trigger.

# FACET 4 VERIFICATION — driver-nonsmooth (adversarial pass, COMPLETED)
Verifier of record, S24 gap census, round-2 finder file
`s24_gap_driver-nonsmooth.md`. This file SUPERSEDES the partial gapv draft
left by the interrupted run (same path): all its verdicts re-derived
independently; three ownership hits it missed are added (R25 choice-ledger
row; speed-advisory N6; speed-advisory §7.3 S1 "quasi-Newton reuse OUT by
policy"), changing two verdicts (G4, G5b).

Method: every citation re-read at source (`a1_toc_variational_jax.py`,
`margin_governor.py`, `adaptive_knot_optimize.py`,
`docs/rde_nozzle_brick2_kickoff.md` §4bis:299-412,
`docs/rde_nozzle_development_plan.md:738`, `docs/rde_nozzle_MASTER.md`
[X-TOCV] :1375-1393 + S20 margin-multiplier KKT :1605-1615 + :1826,
`PROGRESS_2026-08-12_S24_f1b.md` steps 4/9/12-15 numbers grep-verified
verbatim); finder probes A/B/C RE-RUN by this verifier from the finder's
surviving scratchpad scripts (total < 15 s, scratchpad-only, no engine
import); ONE verifier-added source probe (scipy 1.18.0 callback
StopIteration path + barrier init). Ownership swept against: D6 duty rows +
tool matrix; PROGRESS census R1-R27 (:180-260); M0 S20-S24 blocks;
`ADVISORY_engine_speed_audit_2026-08-12.md` + `DISPATCH_Sspeed_to_S25_
2026-08-12.md` (M0-M6, H1-H5, N1-N8, Q1-Q6, dead rows, §7.3 survey rows);
sibling verifier `s24_gapv_constraints.md` (cross-facet dedup).
Default-refute applied. S14-S24 verdicts of record not re-litigated.

**Probe reproduction (this verifier's own runs, 2026-08-12):**
- Probe A (`probe_A_stopiteration.py`, finder scratchpad, re-run): REPRODUCED
  — "CONFIRMED: StopIteration raised by the exact comparator expression on a
  length-only plan change (equal overlap)"; repaired form returns
  first_diff = 4. NOTE: expression-level only; it never enters scipy (see
  G5a refutation).
- Probe B (`probe_B_frontier_kkt.py`, re-run, ~8 s): REPRODUCED bit-level —
  Arm 1: 7 segments, exit cap 1.0e-3, base (0.656847, 0.656847), dist
  7.108e-2, res.optimality = 1.0. Arm 2: status 1, optimality 4.595e-11,
  mu = 0.7091 > 0, dist 2.864e-3, binary gate fired 0 times, max ratio
  0.994281 <= 1.
- Probe C: REPRODUCED on installed scipy 1.18.0 —
  `minimize_trustregion_constr.py:403-406` exactly as quoted
  (`n_ineq == 0 -> 'equality_constrained_sqp' else 'tr_interior_point'`).
- Verifier probe D (source read): (i) `_optimize.py:88-109` — the
  trust-constr arity wrapper `callback(np.copy(res.x), res)` has NO
  exception handling; (ii) `minimize_trustregion_constr.py:454-460` (SQP
  path) and `:499-505` (IP path) wrap the callback call in
  `try/except StopIteration: callback_stop = True` -> status 3; (iii)
  `tr_interior_point.py:321` `barrier_parameter = initial_barrier_parameter`
  (default 0.1, `minimize_trustregion_constr.py:125`), decay 0.2 per outer
  loop — reinitialized at EVERY minimize() call.

---

## G1 (certifiable-set frontier invisible to the KKT system; KS-max C1
## field-level constraint spec) — **CONFIRMED, severity HIGH — as a
## SHARPENING of census R10 + R25, and a cross-facet DUPLICATE**
Citations all verified at source: P4 gate :935-938; P3(ii) :1158-1161;
traced ratio field `_ratio`/`_chain_ratios` :682-700, cert_diag hard-max
return :807-809, consumed ONLY at :1458 (diagnostic check; independently
confirmed by the constraints verifier); margin constraintified
(`margin_governor.py:19-50, 166-203`) but val measured NOT binding (S24
step 13b: min DE val 7.31e-2 = 33x floor, F4 operative verdict verified
verbatim; S22 branch (c) precedent); D6:738 "proximal-bundle (nonsmooth)"
in the tool matrix, never built (no bundle code anywhere in validation/);
outcome-II branch declared instead (`adaptive_knot_optimize.py:484-501`
verified); wiring slot :1179-1182 verified. Math re-derived: KS-max bounds
max r_i <= KSmax_rho <= max r_i + ln(N)/rho CORRECT; sufficiency in fact
STRONGER than the finder states — KSmax >= max r_i alone makes
KSmax_rho <= 1 sufficient; the finder's slack chain "max r_i <= KSmax <=
1 - s + ln(N)/rho = 1" is garbled justification (it invokes the upper
bound backwards) but the extra shift s is only redundant conservatism, not
an error. rho derivation = exact dual of `margin_governor.py:25-29`
(verified). Probe B demonstrates both halves end-to-end (re-run,
reproduced). SOTA attributions real (KS 1979; Poon-Martins SMO 2007
already cited at margin_governor.py:78; Scholtes; Fischer-Burmeister;
Kiwiel).
OWNERSHIP (the finder declared R10 only — INCOMPLETE declaration):
1. Census R10 (PROGRESS :208-210): "rejector field-level C1 —
   GATED(owner F2, trigger = carrier F2b) — RAFFORZATO dalla terza
   istanza S24". G1 is specification content FOR this owned item.
2. Census R25 (PROGRESS :245-250): OPEN choice-ledger row "trattamento
   nonsmooth della frontiera di certificabilità (F2, col rejector C1)" —
   the constraintify-vs-bundle-vs-binary-gate decision G1 argues IS this
   row; adjudication belongs to the CHOICE LEDGER at convergence
   (direttiva choice-adjudication-convergence), not to a finder mint.
3. Cross-facet DUPLICATE: `s24_gap_constraints.md` G7 = the same finding,
   already verified CONFIRMED HIGH by `s24_gapv_constraints.md` (with the
   M0 Le Digabel-Wild attribution correction and the cert_diag/val_diag
   mutual-exclusion implementation caveat :576-577, which applies to THIS
   G1's wiring claim too: a cert row alongside the margin row needs a
   combined diag mode or a second jit replay — the "~5-line append" is
   optimistic on that count).
NOT of record anywhere (survives as the sharpening): the derived-rho
KS-max spec over the existing traced lanes, the surrogate-inside/
gate-outside architecture with P4 kept as verifier, and the analytic
Probe-B demonstration. M0's own S20 block (:1605-1615, margin-multiplier
KKT) shows the pattern for val; no successor quantifier for the
CERTIFICATION field exists of record (registered K_disc~A_0 bridge
FALSIFIED, S22/S24). Severity HIGH (mechanism behind three outcome-II
records; determines representability of frontier-pinned stationary points
in F2). [P-CERTKS] is a legitimate S25/F2 registration under R25.

## G2 (no B-stationarity certificate at outcome-II; ratchet exhaustion =
## de-facto stationarity test) — **CONFIRMED, severity HIGH — sharpens
## R25; fairness annotation retained**
Citations verified: exhaustion exit :1000-1023 (quoted text exact);
TR_FLOOR "(S18 clip)" :897; S24 "KKT OPEN at 1.417e6" verified verbatim
(step 13c; run-1 "pinned ~1.6e6" also verbatim); the reported number is
res.optimality of the problem WITHOUT any certification object
(structurally true: cons = [lip_eq] + optional margin, :1178-1182);
seam-pinned discriminator :1084-1086 = comment-level heuristic, verified;
`rejected_designs` persistence :904-912 verified; s22_rejected_designs.json
EXISTS on disk (verified). Probe B Arm 1 re-run: optimality 1.0 forever at
7.1e-2 from a true constrained optimum — "residual of the wrong problem"
demonstrated. SOTA real (Scheel-Scholtes 2000; BLO gradient sampling;
Larson-Menickelly-Wild SIOPT 2018; Conn-Gould-Toint TRM).
FAIRNESS ANNOTATION (does not overturn): outcome-II is a DECLARED honest
branch (":1005-1010 never a silent success") and S24's attribution has
independent measured support (19 segments of P4 trial rejections, worst
5.0e0..3.4e5, step 13c). What the rejections do NOT establish is the
absence of a certified descent direction (a contaminated TR model — G6 —
could steer every trial uncertifiable while certified descent exists):
that is exactly the missing certificate. EQ-v2 H-CLASS (step 14) leans on
the outcome-II attribution; no recorded number shown WRONG, none
CERTIFIED. E3 (scale conflation 7.7e-2 vs 1.6e6 across instances without
a normalized report) re-derived and correct.
OWNERSHIP: sharpens census R25 (nonsmooth frontier treatment, F2) — the
B-stationarity certificate is the verifier half of that open row; the
convex-hull test on persisted artifacts ([P-BSTAT]) is executable input to
it. Not covered by any duty row as a certificate (searched). HIGH
(verdict-adjacent: it is the epistemic status of every outcome-II exit).

## G3 (engine silently moved to tr_interior_point; cold barrier restarts
## per segment) — **CONFIRMED, severity MEDIUM — wording correction
## retained; no prior adjudication exists**
Verified: kickoff §4bis:335-341 verbatim (equality-only was an explicit
decision "to stay on the TR-SQP path of record"); Probe C re-run confirms
the switch; margin entry :1179-1182 => S22 R-G1d short walk
(`margin_governor.py:359-379`), the S22 campaign, and BOTH S24 decisive
runs (margin_factory armed, ladder of record) ran tr_interior_point. S22
governor log step 6 read: ZERO acknowledgment of the method switch —
"silently" ACCURATE FOR S22. Fresh minimize() per segment :1184-1190 +
verifier probe D(iii): barrier restarts at 0.1 with decay 0.2 at every
segment — cold-restart claim now SOURCE-verified, not just structural.
res.v = +4.8582e4 at an INACTIVE constraint adjudicated "interior-point
barrier estimate, INFORMATION-ONLY" — verbatim of record (steps 13d, 15a).
WORDING CORRECTION (rhetoric, not substance): S24 T1 (step 4) DID read
tr_interior_point.py L218-242 for the multiplier convention — the record
is not unaware of the path; the finder concedes this. What exists nowhere:
a §4bis-grade adjudication of the IP path (barrier update law, what
`optimality` measures there, status semantics, warm-start behavior).
E1 (margin-active barrier x reject-and-shrink interaction untested) is
fair — never reached, untested, unadjudicated.
OWNERSHIP: none found. Speed advisory touches the engine only for the
fun/jac duplication (advisory line 77); no census/duty/conditional row
covers engine re-adjudication; R25 has no engine row. The §4bis
read-the-source standard is the repo's own standing directive
(sota-library-survey-directive) — [P-IPADJ] is its due application, on the
F2 critical path if G1 lands (correct claim). MEDIUM: S18's KKT-closure
record (7.745e-2 <= derived gtol 1.156e-1, M0 [X-TOCV] verified) ran
pre-S22 on the adjudicated path — unaffected; IP-path record numbers are
outcome-II OPEN declarations robust to residual conventions.

## G4 (fresh full FD Hessian per ~one-step segment; "quasi-Newton carry
## never surveyed") — **DOWNGRADED, severity LOW-MEDIUM. Sub-claim
## "never surveyed" REFUTED; cost problem multiply OWNED**
Substance verified: :1087-1096 (n+1 evals, n_eval += n+1 :1095); driver
note (i) :848-852 ("one RK-G segment ~ one productive step"); T2 FIRED
verbatim :1641-1648 ("curvature measurement + RK-G re-records dominate");
kickoff:396-399 + M0 :1381-1383 no-carry policy wording verified; the
determinism argument (carry updated only from accepted certified pairs is
a pure function of walk history => RK-G replay-determinism survives) is
sound as stated; S24 arithmetic (9 dof, 19-21 segments, 76/117 min)
verified.
REFUTED SUB-CLAIM: "quasi-Newton carry that preserves RK-G determinism was
never surveyed". The S-SPEED audit of record ALREADY adjudicated the
curvature-policy alternatives: `ADVISORY_engine_speed_audit_2026-08-12.md`
§7.3 survey row S1 registers "HVP DECLINE-as-default (= N5); quasi-Newton
reuse OUT by policy"; the dispatch carries N5 (jacfwd exact Hessian,
adjudication-only), N8 (colored/sparse FD, owner F2, trigger Q1+M6
shortfall), M6 (vmapped FD Hessian, measured 2.6x, gated), and the DEAD
ROW "dispatch-amortization Hessian story". A registered adopt-or-declare
row is a survey of record — the finder may argue the DECLARED REASON
("by policy") is policy-bound rather than theorem-bound, but that is a
challenge to a registered decision, which belongs to the owned review, not
a mint.
OWNERSHIP: census R7c (G0/T2 review — SCHED S25 ENGINE SPEED SESSION,
"che la consuma con l'evidenza S18+S24") + R22 (S25 speed session, lever
L3 = vmap-Hessian) + dispatch M6/N5/N8/Q1. SURVIVES as the downgraded
finding: the policy-bound-vs-theorem-bound distinction (P2 requires the
MODEL rebuilt, not curvature amnesia; flipped-column locality) as INPUT to
the owned S25/F2 review — new, correctly attributed (CGT; N-W ch.6; BNS
1994; Dennis-Walker), not verdict-bearing. [P-QNCARRY] must be re-routed
through the S1 survey row's re-opening trigger, not run as a free probe.

## G5 (a: comparator StopIteration "crash"; b: no flip-materiality test) —
## **(a) DOWNGRADED, severity LOW — the crash claim REFUTED at system
## level; surviving defect = silent P2 event-log omission.
## (b) CONFIRMED-as-mechanism but OWNED: duplicate of speed conditional
## N6, severity MEDIUM**
(a) Trigger mechanism CONFIRMED end-to-end at source: dec lists = one
entry per station, stations = n_B arc + Nw contour (:326-339, one
plan["arc"].append per station :417); n_B = max(1, ceil(thB/da))
recomputed per record (:218); thB = float(W[0]) (:217) is a design dof;
list != is length-sensitive, zip truncates, `next()` :1170-1173 has no
default — Probe A re-run reproduces the raise. REFUTED CONSEQUENCE: "an
uncaught crash of the whole walk, neither a rejection nor a segment end"
is FALSE on the installed engine — verifier probe D: the wrapper
(`_optimize.py:98-100`) re-raises transparently and BOTH stop_criteria
call sites catch StopIteration and terminate CLEANLY with status 3
(`minimize_trustregion_constr.py:454-460, 499-505`); the repo's own §4bis
adjudication RECORDS this behavior (kickoff:340-342 "raising
StopIteration terminates cleanly with status 3") — the finder's probe
verified the expression, then over-interpreted the system effect against
the repo's own documented source read. SURVIVING DEFECT (real, silent, on
the record path): on a length-only plan change the dict construction
raises BEFORE `events.append` completes and before seg_state["stop"] is
set, so the flip event is DROPPED from `re_record_events`/the "flips %d"
print (the P2 log of record undercounts) while the segment still ends and
the outer loop happens to continue correctly (status 3 unhandled at
:1203/:1220 = fall-through to a fresh segment). A record-keeping defect,
not a crash: LOW. The one-line default repair
(`min(len(dec_base), len(dec_new))`) remains correct and cheap.
(b) Mechanism verified: segment ends on ANY (N,Nv) difference
(:1167-1176); churn measured of record (":849-851 a decision flip fires
at almost every accepted step"; S24 step 12 "flips growing at small
radius" verbatim); no materiality band; the repo owns the right metric
(replay-fidelity band :1041). SOTA real (PC^1 methods; BGNW 2004 SLQP).
OWNERSHIP (missed by the finder AND by the interrupted draft): this IS
speed-dispatch named conditional **N6 — "benign-flip segment merge.
Touches constraint 7 (redefines the RK-G P2 segment boundary); needs its
own panel. Flagged, never traded"** (advisory :443-444, dispatch N6). The
finder's [P-FLIPMAT] A/B would EXECUTE a constraint-7-touching change
without the N6 panel — not licensable as registered. Verdict: the gap is
real and MEDIUM, but it is "sharpens N6" (contributes the :1041
materiality metric to N6's future panel), not a new mint.

## G6 (measured Hessian: no rejector, no derived band; symmetrization
## masks the error signal) — **CONFIRMED, severity MEDIUM**
Verified: FD-of-exact-gradient Hessian :1087-1096; `Hw = 0.5*(Hw+Hw.T)`
:1096 averages away the asymmetry defect and NOTHING checks the matrix
(searched: no band, no rejector anywhere); contrast rows real (O3.1 +
N1 corrupted-gradient control :1478-1496; R-GRAD + corrupted control
`margin_governor.py:298-326`); kink exposure real (`spline_eval`
searchsorted :155-157; FD step sqrt(eps)*scale :1090 can straddle a
knot/plan seam). The masquerade argument (wrong H => trial steps steered
into uncertifiable territory => observationally identical to
certifiability-limiting) is sound and is the main attribution risk at
outcome-II — couples to G2. Boundary honestly noted: P4/P3(ii)
certification is Hessian-independent, TR reduction-ratio is an implicit
behavioral guard, so no recorded certified number is at risk; the gap is
rejector-culture (R5) conformance + outcome-II attribution robustness.
Proposed checks correctly attributed (N-W §8.1; O3.1 pattern lifted one
derivative; Moré-Wild TOMS 2012) and cheap (2 evals/segment).
OWNERSHIP: none. M6's KAT+O3.1 gate is a version-change acceptance gate
for the vmapped rewrite, not a per-segment curvature rejector; N5 is
adjudication-only. [P-HESSREJ] is a legitimate S25 registration. MEDIUM.

## G7 (TR_FLOOR/tr_cap/tr0/xtol declared, not derived) — **CONFIRMED,
## severity HIGH (TR_FLOOR half) / LOW (xtol half)**
Verified: :896-899 tr0 = 0.05, TR_FLOOR = 1e-3 "(S18 clip)", tr_cap =
0.25 — comments only, no derivation anywhere (searched); exhaustion fires
exactly at the ratcheted floor (:992-999, :1000-1023) => 1e-3 IS the
de-facto resolution of the outcome-II declaration, a verdict-bearing exit
three times of record (S20/S22/S24); the floor lives in scaled u
coordinates (measured Dv, median-normalized :1064-1065) => physical size
is instance-dependent => cross-instance "exhausted at the floor"
statements compare different physical resolutions — correct and
previously unstated. xtol = 1e-10 literal at `margin_governor.py:364`
(finder wrote :365, off-by-one, trivial), `:485`,
`adaptive_knot_optimize.py:464`. CORRECTION THAT STRENGTHENS: the finder
credits [X-TOCV] with a DERIVED xtol (:1519-1521) — in fact the comment
(:1516-1517) claims the derivation while the code assigns the literal
1e-10 (:1520): the derivation exists only as prose, nowhere as
arithmetic. Derived-floor proposal uses only measured quantities of
record (tol_dp :1480-1482 verified); [P-TRFLOOR] is pure logged-number
arithmetic. SOTA real (Cartis-Scheinberg 2018; Moré-Wild). R5 applies
squarely.
OWNERSHIP: none (R25's K_RICH-universality row is adjacent, distinct; no
speed/dead row touches TR constants). HIGH on TR_FLOOR (co-determines
when outcome-II verdicts fire and what "exhaustion" resolves), LOW on
xtol (behavioral).

## G8 (Dv measured once, objective-only, never revalidated) —
## **CONFIRMED, severity MEDIUM — with a dead-row boundary declared**
Verified: Dv = None :899, measured only under `if Dv is None:` :1050-1070
(first segment base, 2n evals, objective diagonal only), frozen for the
walk; "conditioning IS the convergence rate" S18 note :858-867 verified;
constraint rows unseen by Dv (lip_eq row scaled :1072; margin evaluated
at u*Dv; no row equilibration anywhere) with rho = 5.7518e+4 of record
(S24 step 9 verbatim) contributing steeper rows — structurally true; the
free-refresh observation is correct (full H re-measured per segment base
:1087-1096, diagonal free). SOTA real (Deuflhard; N-W scaling;
GMS/SNOPT row scaling).
OWNERSHIP/BOUNDARY: no row owns a Dv REFRESH. Declared boundary: the
speed dispatch's dead row "Jacobi-precond removal" (do not resurrect)
bounds this finding from the other side — G8 proposes refreshing, never
removing, the preconditioner, and must not be read against that dead row;
M6's "precond batch" speeds the MEASUREMENT of the same frozen Dv, it
does not refresh it. [P-DVREFRESH] with the bit-compare determinism check
is correctly scoped. MEDIUM.

---

## Cross-cutting checks
- Scope-of-record: S18 KKT 7.745e-2 <= derived gtol 1.156e-1 (M0 [X-TOCV]
  verified); S24 run-1 pinned ~1.6e6 / run-2 1.417e6 at the returned base,
  19-21 segments, margin INACTIVE 33x, F4 operative verdict — all
  grep-verified verbatim in PROGRESS_2026-08-12_S24_f1b.md.
- Honesty frame: verified — every proposal keeps P4/P3(ii) as verifiers;
  nothing weakens a gate.
- Closed verdicts untouched: S22 [X-MGOV] derivations, S24 panel C1-C10,
  the P4 2-run budget, DIR-RKG policy — no finding re-opens them; G4's
  surviving half is routed THROUGH the owned review, G5b's through the N6
  panel, per method rule.
- Probe hygiene: A/B/C re-runs + probe D source reads, < 15 s CPU total,
  scratchpad/site-packages reads only, no tracked file edited, no engine
  import.
- Drop-list (5): fold decisions sound; none hides a HIGH item (budgets are
  budgets; the scale-normalized KKT report lives in G2/G7; the
  learning-flavored frontier model is correctly dropped as
  below-evidence-standard).

## Verdict table
| # | Verdict | Sev | Refuted sub-claims | Ownership pointer |
|---|---------|-----|--------------------|-------------------|
| G1 | CONFIRMED | HIGH | slack-chain wording garbled (harmless); "~5-line append" optimistic vs cert/val diag XOR :576-577 | SHARPENS census R10 + R25; DUPLICATE of constraints-facet G7 (gapv: CONFIRMED HIGH) |
| G2 | CONFIRMED | HIGH | none (fairness: S24 attribution has independent P4-rejection evidence; nothing certified) | SHARPENS census R25 (certificate half) |
| G3 | CONFIRMED | MEDIUM | "silently" true for S22 only; S24 T1 read the extraction (finder concedes) | none (new; §4bis standing directive is the vehicle; F2-critical if G1 lands) |
| G4 | DOWNGRADED | LOW-MED | "never surveyed" REFUTED (advisory §7.3 S1: quasi-Newton reuse OUT by policy; N5/N8/M6 registered) | census R7c + R22; dispatch M6/N5/N8/Q1; dead row "dispatch-amortization Hessian story" |
| G5a | DOWNGRADED | LOW | "uncaught crash of the whole walk" REFUTED (scipy catches -> clean status 3; kickoff:340-342 records it) | none; surviving = silent P2 event-log omission; 1-line repair stands |
| G5b | DOWNGRADED (owned) | MEDIUM | none on mechanism | DUPLICATE of speed conditional N6 ("benign-flip segment merge", own panel, never traded); contributes the :1041 materiality metric |
| G6 | CONFIRMED | MEDIUM | none (boundary: no certified number at risk) | none; [P-HESSREJ] legitimate |
| G7 | CONFIRMED | HIGH/LOW | none; STRENGTHENED (xtol "derivation" is prose even at origin :1520) | none |
| G8 | CONFIRMED | MEDIUM | none | none for refresh; bounded by dead row "Jacobi-precond removal" (removal side only) |

**Counts: 5 CONFIRMED (G1, G2, G3, G6, G7, G8 = 6 findings counting G7
once; see note), 3 DOWNGRADED (G4, G5a, G5b), 0 REFUTED outright.**
Counting per finder heading (G5 = one finding with two halves):
**6 CONFIRMED (G1, G2, G3, G6, G7, G8), 2 DOWNGRADED (G4; G5 — crash half
refuted, materiality half owned by N6), 0 REFUTED.**
HIGH: G1, G2, G7(TR_FLOOR half). Duplicates/owned: G1 (R10+R25 +
constraints-facet G7), G2 (R25), G4 (R7c/R22 + S-SPEED S1/N5/N8/M6),
G5b (N6).

# S24 GAP VERIFICATION — FACET 2: CELL SOLVER + CERTIFICATION (VERIFIER: cell-cert)

Adversarial pass over s24_gap_cell-cert.md. Method: every cited line range
re-read in the actual sources; the finder's probe script
(scratchpad/probe_cell_cert.py) RE-RUN in full (8.8 s, output reproduced
bit-comparable); coverage re-checked against D6 duty rows, M0 S20-S24
registration blocks, the S24 log validation/PROGRESS_2026-08-12_S24_f1b.md
(census step 11, T5 step 16), docs/claims_registry.yaml, and the two
S-SPEED artifacts of record (ADVISORY_Sspeed_prompt_2026-08-12.md,
ADVISORY_engine_speed_audit_2026-08-12.md) which the finder demonstrably
consumed (its "111 s at 7818 cells" baseline exists ONLY there) but did
not dedup against.

VERDICT COUNTS: 4 CONFIRMED / 1 REFUTED / 3 DOWNGRADED.

---

## F1 (table-edge clamp, dead adjoint) — VERDICT: DOWNGRADED, severity MEDIUM

Citations REAL and exact: `a1_ideal_march_jax.py:344-356` (jnp.interp
clamp in state_q), `thermotab_c1_jax.py:143-146` (`_locate` clips i to
n-2, t unbounded => end-segment quintic EXTRAPOLATION — note this is a
DIFFERENT failure mode than a clamp), `:189-197` (invert_h, 8 fixed
trips, no domain check), `:31-33` (G>0 box "contains every
march-realized state" declared, unmonitored). Probe P1 RE-RUN and
REPRODUCED: T_tab = 1050.00 vs exact 946.98 (error 103 K) at 2% past
edge with dT/dq = -0.000e+00 exactly; 536 K at 10%, M 5.055 silent.

DOWNGRADE GROUNDS (coverage): the "missing guard" is ALREADY a NAMED
CONDITIONAL of record — survey condition **C-D "box-edge silent-clamp
rejector (audit row, owner F2)"**, registered in the S24 census (log
step 11) and in the M0 S24 block (~ln 2024: "box-edge silent-clamp
rejector = C-D (owner F2)"), alongside C-C (per-table joint census,
200/201 K clamp + 1000 K joint named). The finder's mandated census
check missed it. Per the gap criterion, "unguarded and missing" cannot
stand as a NEW gap.

WHAT SURVIVES (as discharge-priors for C-D, to be attached to it):
(i) the MEASURED dead-adjoint datum — the clamp zeroes the thermo lane
of dJ/dW exactly, which C-D's wording does not name; (ii) the
clamp-vs-extrapolation distinction between the linear closure (state_q
clamps) and the C1 closure (_locate extrapolates the end quintic) — two
different silent failure signatures under one rejector duty; (iii) the
reachability estimate (edge at M ~ 4.6 gconst); (iv) the concrete fix
class (per-run min/max distance-to-edge in the cert dict + zero-margin
rejector, pattern = a1_toc:227-237 — pattern citation verified).
No verdict of record is affected (everyday instances in-window; the S24
survey proved in-window exact-representation).

## F2 (certificate conditioning + branch blindness at folds) — VERDICT: CONFIRMED, severity HIGH

Citations REAL: `a1_ideal_march_jax.py:430-435` (step_norm = max|J^-1 r|),
`:682-707` (certify docstring claims "Derived from the Newton
contraction" — contraction hypothesis indeed never checked, no kappa(J)
qualification anywhere), `def_twin_falsifier.py` fold-guard honored at
MONITOR level only ("our monitor reports den, never a val = 0 read" —
verified in its header text). Probe P2 RE-RUN and REPRODUCED exactly:
at the EXACT (+) root, ratio = 2.500e+01 => false FAIL (roundoff
amplified by 1/|J|); basin-scale stale-seed shift converges to the (-)
branch with ratio = 0.000e+00 => false PASS. No branch-consistency
monitor exists (the axial-margin rejector a1_toc:226-237 is a CAUSALITY
check, u_x > c, not a root-branch check).

COVERAGE CHECK PASSED (not already covered): the S22 O4 block (M0
~1765) names the S20 mechanism candidates as "spline conditioning,
knot/station mismatch" — certificate-METRIC conditioning is NOT on that
list; mechanism identification is OWNED BY F2, so this finding ENLARGES
an owned candidate list rather than duplicating it. Adversarial check
against [X-CDKAT] (registry ln 1257-1260): the retro-validation proved
the TRIP-CAP hypothesis dead (bit-identity under 30->300); it does NOT
discriminate genuine non-convergence from converged-but-conditioning-
rejected — a conditioning-rejected cell is ALSO a fixed point of the
damped body (t=0 wins every trial) and is bit-identical under cap
raise. So the finding contradicts NO verdict of record while naming a
live re-adjudication lever. SOTA attributions correct (Deuflhard
affine-covariant estimators; Kantorovich; Krawczyk in-house via
[X-IVXC] — registry entry verified at docs/claims_registry.yaml
~ln 1694, finder's path missing the docs/ prefix, trivial).

HIGH because: (a) the false-fail mechanism is a candidate INSIDE the
outcome-II "certifiability-limited" frontier that carries record
verdicts (S20, S22, and S24's OPERATIVE F4 verdict — third measured
instance); (b) the false-pass mode sits on the verdict-bearing O3.1
FD-probe replay path and C2-F2 CERT_PLAY cannot see it (a wrong-branch
root certifies at ratio 0). Declared caveat carried: toy-measured, not
yet demonstrated in the repo's 4x4 cells.

## F3 (scalar cert scale u-dominated) — VERDICT: CONFIRMED, severity LOW

Citations REAL: sc = max(1, max|z|) at `a1_ideal_march_jax.py:393` and
`:699`, and (verifier addition) also at `a1_toc_variational_jax.py:243`
— the same scalar scale on the design-engine path. Docstring :682-688
indeed motivates z-space by unit-consistency and stops one step short
of componentwise scaling. P3 arithmetic RE-RUN: bound 5.107e-11 abs =
5.107e-08 relative at y = 1e-3 vs 2.220e-14 floor — the "2300x"
statement (vs the scale-1 floor) is arithmetically correct. No coverage
found anywhere. Higham/Deuflhard attribution correct. LOW (not
load-bearing at yt = 1; latent unit-dependence against the generality
directive — hygiene tier until a high-q propellant or fine-mesh
near-axis instance makes it load-bearing).

## F4 (no derived seed-basin radius in z-space) — VERDICT: CONFIRMED, severity MEDIUM

Citations REAL: predictor "is O(h) and lands inside" asserted at
`a1_ideal_march_jax.py:540-543` (comment verified verbatim, no bound
anywhere); replay seed = stop-gradient recorded z (`:634`, toc:519 —
both verified); KAT-3 is one instance + one hardened perturbation
(certdiag_kat.py text + registry X-CDKAT row, both verified); M0
1832-1884 verified = [X-TBAK] W-space ball with THEOREM+PRACTICE stack
(mean-value bound + K_RICH two-point L_TB = 4.321067e+01) — and NO
z-space counterpart exists in M0, D6, or the registry (searched:
basin/Kantorovich/alpha-theory — no hit outside PAP/optimization
contexts). The asymmetry claim is exact. P2's basin-vs-h_FD datum
(sqrt(p0) = 1e-4 vs h = 6.06e-6) reproduced. alphaCertified
(Hauenstein-Sottile, TOMS 2012) attribution correct. Finder honestly
declares the C2-F2 mitigation; verifier adds: CERT_PLAY does NOT close
this (F2's false-pass shows a wrong-branch converged replay certifies
at ratio 0). MEDIUM — O3.1 probe validity at frontier instances is
coverage, not a current verdict (record campaigns ran margin-inactive,
far from folds). S25 registered probe is well-formed and correctly
deferred (> 30 s).

## F5 (cert_diag XOR val_diag; equivalence informal) — VERDICT: DOWNGRADED, severity LOW

Citations REAL: XOR declaration + raise at `a1_toc:574-578`;
margin_governor consumes val_diag lanes at trial points (verified,
make_run_toc_scan_jit(..., val_diag=True) in make_margin_fn); no
M0/registry rigor row states traced-metric == record-metric (verified:
X-CDKAT registry row is a KAT record, not an equivalence lemma;
_chain_ratios prefix argument at :691-700 is comment-level only).

DOWNGRADE GROUNDS (two overstatements): (1) "the declaration predates
that consumer and was never re-adjudicated" is FACTUALLY WRONG — the
val_diag paragraph is titled "(S22, F1 governor entry)" and itself
NAMES [X-MGOV] as the consumer; the XOR clause was written concurrently
with and aware of the governor. (2) "NO certification channel" is
overstated: the trial-point deferral contract as written (toc:559-563)
is generic over "TRIAL points inside the optimizer" (not objective-only
as the finder asserts), and every ACCEPTED iterate re-records under
BOTH the P4 cert gate (toc:930-938, verified) and the per-cell
margin-floor rejector (toc:269-274, verified) — the margin path is
certified at acceptance. Additionally no verdict of record rides an
uncertified margin lane: S22/S24 ran margin-INACTIVE (S24 F4: min DE
val 7.31e-2 = 33x the tightest floor).

WHAT SURVIVES (LOW, R4 hygiene): the prefix-exactness lemma of
_chain_ratios is unstated against the truncation lanes (:389-403
verified) and deserves an M0 SCHEMA/PRACTICE row; the replay-vs-record
equivalence family is populated by ONE KAT instance; the val_diag
starvation KAT-3 twin does not exist (true — nothing would fire on a
zero-trip val_diag replay at TRIAL points; steering-quality issue, not
verdict-bearing given the acceptance-time channels). The union-return
one-liner is a fair cheap fix. S25 probe registration well-formed.

## F6 (no early-abort in record mode) — VERDICT: REFUTED (as a gap)

Every factual statement checks out (certify accumulates and never
raises, a1:698-707; cell raises only on the margin rejector,
toc:239-275; P4 fires post-march, toc:930-938; CERT_ARGMAX default-off,
toc:122-125). BUT the gap is ALREADY COVERED — fully specified, owner
assigned, of record: (a) ADVISORY_Sspeed_prompt_2026-08-12.md names
lever **L2 = "early-abort del record alla prima cella non certificata"**
and prices exactly this ("costa 111 s per scoprire 'non certifica',
senza early-abort"); (b) ADVISORY_engine_speed_audit_2026-08-12.md
ships the complete design: **H1 — Early-abort opt-in flag + schema
(MARCH-F2 + DRIVER-F3)**, hooks MANDATORY in the M5(b) chain, owner S25
item 8, gains quantified (~2x uniform / 5-20x adversarial on failing
records), gate conditions (fires earlier never later; doctored-cell
control at cell k; first-offender index stable; schema note); (c)
PROGRESS R22 + the S24 log step 16 NEXT schedule the S25 ENGINE SPEED
SESSION that consumes it. Decisive dedup failure: the finder's own
"baseline of record: 111 s at 7818 cells" exists ONLY in these
advisories — the source that gave it the baseline also names the lever.
Fails the "not already covered by an existing carrier/duty" criterion.

## F7 (wall-foot chord search fragile + wasteful) — VERDICT: DOWNGRADED, severity MEDIUM

Citations REAL: record wall_search loop verified at a1:805-833 (linear
index scan, one FULL implicit solve per attempt, cap RuntimeError,
Nv never steps back) and toc:355-375 (same); the FRAGILITY-of-record
quote at toc:847-852 verified VERBATIM ("the wall-search indices (N,
Nv) are FRAGILE decisions... a decision flip fires at almost every
accepted step: one RK-G segment ~ one productive step") — the
re-record-rate claim is of record, not the finder's inference. D6 knot
insertion "new knot AT A DATA SITE" verified at D6:929 (finder cited
ln 906 — off by 23 lines, quote real; hygiene-level miscite).

COVERAGE CHECK — split result: the SPEED AUDIT does NOT cover the
finder's core lever: M5 keeps wall_search cells EAGER ("Under M5
survives only for eager wall_search cells", audit :347), its H2
"bracket-scan vectorization" is the leggeAree scan (audit :531-532
"bracket scan NOT subsumed (per-record)"), and NO document proposes
making (N, Nv) a DERIVED quantity via bracketed continuous root-finding
— i.e. the audit cuts record COST, nobody owns cutting the decision-flip
RATE that sets n_rec ~ n_segments. That lever survives as genuinely
un-owned. Brent/Shewchuk attributions correct.

DOWNGRADE GROUNDS: (a) the CORRECTNESS half ("accept a wrong foot
silently" under non-monotone spline) is argued from the predicate shape
only — the registered probe was NOT run, so it is PLAUSIBLE, not
measured; the everyday geometry (monotone convex-ish bell walls) gives
no instance of record; (b) the failed-attempt cost half overlaps the
S25 speed-session scope (which owns record-path cost). NET: MEDIUM —
the surviving content is the un-owned derived-(N,Nv) re-record-rate
lever + the unadjudicated monotone-foot assumption, with the S25 probe
correctly registered.

## F8 (solver/cert constants are conventions) — VERDICT: CONFIRMED, severity LOW

Citations REAL and the internal tension verified: a1:84-86 literally
says "100 eps * scale(z) (Newton at the roundoff floor; **spike factor
convention**)" under a header claiming "TOLERANCES — ALL DERIVED (R5,
no magic numbers)"; constants at :145-148; TRIALS ladder at :371 with
the 1/4 -> 1/16 -> 1/64 gap and no recorded rationale (searched);
acceptance = bare argmin over candidates incl. t = 0, no
sufficient-decrease or contraction measurement (:397-416 verified).
The contrast with thermotab's derived C_OPS = 100 ("~64 flops -> C =
100", thermotab:37-40) verified — the repo demonstrably knows how to
derive this class of constant and did not for the march solver.
[X-CDKAT] proved N_NEWTON bites, did not derive it (registry row
verified). Deuflhard NLEQ / Armijo / Higham attributions correct. No
coverage found in D6/M0/advisories. LOW: no verdict rides on it (the
floor convention is uniform repo-wide; damping-ladder waste compounds
the F6 lever, which is owned at S25), but it is a genuine R5-culture
inconsistency worth one derivation paragraph + a measured-contraction
damping upgrade at the F2 engine rebuild.

---

## DROPPED-LIST AUDIT (finder's 5 drops — all legitimate)
1 (wavefront vmap) correctly dropped: owned by the speed audit M-items.
2 (Broyden on 4x4) correct: negligible, dominated by ladder cost.
3 (DWR) correct defer: theorem ledger U3 (ln 681-685, verified) + D6
  DWR-conformance text (ln 886-914, verified) place it in mesh/AMR facet.
4 (float() host-sync) — folded into the early-abort/M5 territory, which
  is owned (see F6): drop is right for THIS facet.
5 (leggeAree 400-point grid, a1:747 verified) — real but one-shot;
  NOTE: its vectorization IS covered by the speed audit H2, so the drop
  is doubly right.

## SUMMARY
| # | Verdict | Severity | One-line ground |
|---|---------|----------|-----------------|
| F1 | DOWNGRADED | MEDIUM | Real + reproduced, but = named conditional C-D (owner F2) of record; survives as measured discharge-priors (dead adjoint, clamp-vs-extrapolation split) |
| F2 | CONFIRMED | HIGH | Both failure modes reproduced; not on any candidate list; [X-CDKAT] does not discriminate it; touches record frontier adjudications + O3.1 path |
| F3 | CONFIRMED | LOW | Arithmetic + both code sites verified (plus toc:243); latent at yt=1 |
| F4 | CONFIRMED | MEDIUM | W-space/z-space asymmetry exact; no counterpart anywhere; CERT_PLAY does not close the wrong-branch case |
| F5 | DOWNGRADED | LOW | "Predates consumer" factually wrong; margin certified at acceptance (P4 + floor rejector); survives as R4 hygiene (prefix lemma + KAT family) |
| F6 | REFUTED | — | Duplicate of speed-audit H1 / prompt L2 / PROGRESS R22, owner S25 item 8; finder consumed the advisory's own baseline without dedup |
| F7 | DOWNGRADED | MEDIUM | Fragility of record verified; derived-(N,Nv) lever genuinely un-owned; wrong-foot half unmeasured (PLAUSIBLE); cost half overlaps S25 |
| F8 | CONFIRMED | LOW | "spike factor convention" under an "ALL DERIVED" header verified; thermotab contrast real; no verdict affected |

Verifier probe ledger: re-ran scratchpad/probe_cell_cert.py (8.8 s, one
process, scratchpad only); no repo files touched; no heavy instance
launched (S24 campaign respected).

# PANEL — REMPOL (C7 dof policy, C26 out-of-box, C29 mask granularity, C30 mask crop, C47 numeric-lint enforcement)

S-FOUNDATIONS-C3 blocco 1 wave 3, per BRIEF_wave3_panels.md §REMPOL
(+ §0 of BRIEF_wave1_panels.md VERBATIM, §0-bis directive axes, §0-ter
world-class census protocol of BRIEF_wave2_panels.md, + wave-3 additions
(i) LOAD-CLASS VALVE, (ii) new papers on disk, (iii) authorities not
re-litigated, (iv) cava per-row citable, (v) ledger = row authority).
BASE = validation/sfoundations_raws_2026-08-13.

CENSUS VALIDITY STAMP: census executed and dated 2026-08-20 (8 WebSearch
queries, protocol table §2.1). All repo file:line anchors below re-read
at source IN THIS WINDOW (SR-12); gapmap-era anchors that have DRIFTED
are re-measured and tagged. Authorities consumed, not re-litigated:
VERDICT_wave1.md (via the C28 ledger-row adjudication note of record,
docs/choice_ledger.yaml:423-431 [FULL]), VERDICT_wave2.md (grep-verified:
no REMPOL row adjudicated there — its 'C30' hits :90 are the CAVA's own
numbering, not ledger C30; same for VERDICT_wave1.md:286). Ledger rows
read in full: C7 :200-209, C26 :401-409, C29 :433-442, C30 :444-452,
C47 :633-643 [FULL]. No registry/doc of record is edited by this panel —
every delta below is PROPOSED for the landing window.

---

## 1. FROZEN FORMAL STATEMENT

### 1.0 Shared sub-problem (frozen before census)

Objects. The certified optimize-loop of record carries four DISCRETE
POLICY SWITCHES that are not numerics of the march itself but decide
WHAT the loop enforces, WHEN it re-derives a frozen object, and WHICH
channel guards its own code hygiene:

- C7: the [X-AKNO] outer loop's dof policy — knot INSERTION only,
  capped per cycle (validation/adaptive_knot_optimize.py:32-36
  [FULL]; insertion site :197, :408; no removal path exists — grep
  'remove|coarse' measured this window, only doc-line hits).
- C26: behavior of the thermo closure when a march/probe state leaves
  the tabulated box — linear path silently CLAMPS with exactly zero
  exterior derivative (validation/a1_ideal_march_jax.py:397-406
  [FULL]: `T = jnp.interp(ht, hg, Tg)` :403; the audit-era anchor
  :344-351 has drifted, re-measured); quintic path silently
  EXTRAPOLATES unboundedly (validation/thermotab_c1_jax.py:183-186
  `_locate` index clip, :308 `invert_h` iterates on it [FULL]).
- C29: freezing granularity of the DE-side chain lane mask — built at
  RUNG start and frozen across the rung's segments (declared
  semantics, validation/def_twin_falsifier.py:536-539 comment +
  :1124-1133 build [FULL]) with the panel-C3 drift gate + repeat-once
  re-freeze (:1193-1223 [FULL]); the plan re-freezes every other
  W-dependent object per RK-G P2 SEGMENT.
- C30: mask shape-adaptation policy — overlap crop
  `mm[:r,:c] = mask[:r,:c]` + occurrence counter `mask_shape_adapt`
  (def_twin_falsifier.py:677-684 [FULL]); the masked KS AND the
  frac_bad denominator are recomputed on the crop (:699-707 [FULL]),
  so a True lane beyond the overlap exits enforcement COUNTED but
  UNBOUNDED.
- C47: the numeric-lint enforcement policy for legacy literals in
  validation/**/*.py — per-file frozen count ratchet vs baseline JSON
  (tests/test_numeric_lint.py:23-40 docstring [FULL]; DECLARED LIMIT
  in-file: within-count literal swaps pass).

Program context (binding): certified marched axisymmetric Euler solver,
JAX custom_vjp discrete-adjoint stack, R5 discipline (tolerances
derived, rejectors must fire), P-gates absolute; C28 verdict of record
(consumed per (iii)): hybrid priced-frontier KS-max on TRACED
quantities with the binary P4/P3(ii) gates kept ABSOLUTE — binary
verdicts are never replaced by smooth surrogates, they are PRICED
alongside them.

LOAD-CLASS DECLARATION (wave-3 (i), applied per row): C26 and C30 are
GAP-ACCOUNTING rows (each already carries a CONFIRMED findings-registry
row with a named owner and a named repair); they are converged below
with strong trivially-checkable sufficient hypotheses,
sufficient-not-optimized, declared as such. C7 and C47 are
bookkeeping-of-a-duty rows with one genuine policy fork each. C29 is
the one row of this panel with live post-adjudication measured evidence
against the incumbent; it gets the full treatment.

### 1.1 Per-row main question + PRE-REGISTERED decision criteria
(frozen BEFORE the census ran; no mid-census amendment was needed)

**C7** — Q: may the outer loop ever RETIRE a dof, or is
insertion-only correct policy for a certified design loop whose
optimum moves per cycle?
Criteria (win conditions): insertion-only WINS iff dof economy is
shown enforced by another mechanism or the ratchet is immaterial at
program scale; insert+remove WINS iff a removal test exists that is
(a) gated by the SAME derived-band machinery as insertion (no new
magic), (b) cheap (no fresh solve class), and (c) cannot corrupt the
of-record artifact (best-cycle save preserved); AFEM-coarsening WINS
only if its optimality theorems transfer to a MOVING optimum
(verifier-corrected attribution says they are proved for FIXED
problems — this is the bar it must clear).
Materiality: dofs 8 -> up to 20 measured on the default 4-cycle run,
n+1 gradient evals/segment per retained dof, and dof cost was the term
named dominant when T2 FIRED — MATERIAL on budget; NOT material to any
number of record (the artifact saves the best cycle's class,
verifier-established). Fork decided on measured cost, not on numbers.

**C26** — Q: what does the certified loop DO when a state leaves the
thermo box, given that C-D already mandates the traced box-exit
rejector?
Criteria: an option WINS iff it (a) is traced/jit-safe through scan
and custom_vjp, (b) is verdict-bearing in the cert_worst pattern (a
P-gate row, not a print), (c) covers BOTH modes (zero-derivative clamp
AND unbounded quintic extrapolation), (d) demonstrably FIRES on a
planted out-of-box control. Silence loses by the standing C-D mandate
(not re-litigated). Materiality: a silent box exit certifies a
WRONG-but-consistent system to the floor (cert_worst structurally
blind to it, AUDIT_agnostic_2026-08-07.md:388-400 [FULL]) — MATERIAL
whenever it happens; the adjudication here is HOW, not whether
(gap-accounting).

**C29** — Q: at what granularity must the DE-chain mask be re-derived
so that the enforced constraint is never stale by more than the
program's own re-freeze rhythm?
Criteria: rung-freeze WINS iff the measured crossing drift within a
rung stays inside STENCIL_RADIUS (it did NOT: C3 fired of record);
segment re-freeze WINS iff recorded per-segment crossing motion is
SMOOTH (accumulates gradually — then re-freezing at the P2 rhythm
bounds staleness by one segment and binary semantics survive); the
smooth gate sigma(val/eps_gate) WINS iff crossing motion is JUMPY
between segments (then any freeze granularity chases it) AND eps_gate
can be DERIVED from a measured val noise floor AND the C3 binary
detector is retained as referee (C28 doctrine: gates absolute).
Materiality: margin inactive 33x at every record instance — no number
of record at risk; the measured cost is real (the C3 repeat consumed
decisive run 2 = one full rung walk) and the attribution risk at a
future margin-ACTIVE instance is the true stake.

**C30** — Q: is a counted crop event enough, or must enforcement loss
be BOUNDED (lost-lane count verdict-bearing)?
Criteria: the invariant WINS iff it is one line, rides existing
counters, and makes nonzero loss verdict-bearing; the incumbent WINS
only if lane loss is impossible by construction (it is not: overlap
crop provably drops out-of-overlap True lanes). Materiality: at record
instances loss can only weaken an inactive-by-33x constraint —
IMMATERIAL to numbers of record, decided on cost (one line) +
certificate honesty at future margin-active instances. Declared
immaterial-now/material-later; LOAD-CLASS VALVE applied.

**C47** — Q: which enforcement policy keeps the validation/ literal
channel closed at least as tightly as the measured debt allows,
without blocking of-record work?
Criteria: a policy WINS iff (a) no new literal can enter silently,
(b) the baseline can never loosen silently, (c) the residual attack
surface is NAMED and shrinkable, (d) it does not freeze validation
work (37 files / 639 baselined literals measured of record, findings
row :268). The declared limit (within-count swaps pass) is the live
attack surface: an option that closes it at ~zero cost beats one that
merely documents it. Materiality: low-medium (a swap needs an
in-count edit to an of-record file that also survives review), but
the closure candidate is cheap, so the fork is decided on cost.

---

## 2. SOTA CENSUS (dated 2026-08-20)

### 2.1 Query protocol table

All queries via WebSearch (US index), 2026-08-20. hits = result links
returned; screened = titles/abstracts read; included = entries carried
into §2.2. The Russian classical school does not bear on this panel's
territory (discrete software/loop policy, not gasdynamics) — axis
closed by stated reason.

| # | verbatim query | row | hits | screened | included |
|---|---|---|---|---|---|
| 1 | adaptive refinement with coarsening spline knot removal optimization loop hierarchical splines | C7 | 9 | 9 | 4 |
| 2 | lint baseline ratchet pattern suppress existing violations only tighten Betterer ESLint bulk suppressions | C47 | 8 | 8 | 4 |
| 3 | jax checkify traced runtime error checking NaN out-of-bounds jit | C26 | 10 | 10 | 2 |
| 4 | projection continuation smoothed Heaviside topology optimization frozen discrete mask differentiable relaxation straight-through estimator | C29 | 9 | 9 | 4 |
| 5 | static analysis baseline fingerprint hash suppression SARIF partial fingerprints track findings across changes | C47 | 10 | 10 | 2 |
| 6 | tabulated equation of state out-of-range guard extrapolation policy hydrodynamics code silent clamp error flag | C26 | 10 | 10 | 3 |
| 7 | working set stabilization active-set changes zigzagging SQP frozen active set strategy convergence | C29 | 9 | 9 | 3 |
| 8 | self-checking invariants scientific software runtime verification conservation property assertion silent failure detection | C30 | 10 | 10 | 2 |

### 2.2 Census entries (read-depth markers per §0-bis(b))

C7 (design-space adapt with retirement):
- [ABS] Giannelli et al., "Suitably graded THB-spline refinement and
  coarsening" (arXiv:1811.00358 / CMAME): refinement AND coarsening
  with admissible-mesh grading — the modern IGA line where coarsening
  is first-class, not an afterthought.
- [ABS] "Topology optimization using fully adaptive truncated
  hierarchical B-splines" (Appl. Math. Model. 2021): design mesh
  locally refined AND coarsened simultaneously inside an optimization
  loop — direct modern precedent for retire-while-optimizing.
- [TITLE] Morin (AFEM lineage page): AFEM-with-coarsening convergence
  line (Binev-Dahmen-DeVore 2004; Stevenson 2007 / CKNS 2008 per the
  gapmap's verifier-corrected attribution — proved for FIXED problems).
- [TITLE] Lyche-Morken 1987 knot removal (the ledger's named
  alternative; classical, error-measured removal).
Recency span C7: 1987-2021+, newest included 2021 [ABS].

C26 (out-of-box behavior):
- [ABS] JAX checkify guide (docs.jax.dev): jit-able runtime error
  checking (user/NaN/OOB checks) — the modern in-framework instrument
  for traced error flags; error-monad functionalization changes call
  signatures through scan/custom_vjp.
- [ABS] Equinox runtime errors (docs.kidger.site): same family,
  eager-abort semantics.
- [ABS] Phantom SPH (arXiv:1702.03930): out-of-table EOS reads ->
  linear extrapolation WITH a user-facing warning — even
  production astro codes refuse pure silence.
- [ABS] singularity-eos (LANL docs): production EOS library with
  explicit models/bounds handling as API policy.
- [TITLE] BADGER EOS library (CPC 2013): off-the-table handling named
  as a first-class design problem.
Recency span C26: 2013-2025 (living framework docs), newest = current
JAX docs [ABS].

C29 (mask granularity / discrete-membership relaxation):
- [TITLE] Guest-Prevost-Belytschko 2004 (already the gapmap's named
  SOTA): smoothed Heaviside projection — the canonical smooth-gate
  ancestor.
- [ABS] "Adaptive beta update scheme in Heaviside projection method of
  topology optimization" (CMAME, in-press 2026): beta-continuation is
  STILL an active research problem — the smooth gate's sharpness
  parameter is a live difficulty, not a solved constant; directly
  feeds the eps_gate-must-be-derived criterion.
- [ABS] Wang-Lazarov-Sigmund robust projection formulations
  (SMO 2011 lineage, via "On projection methods, convergence and
  robust formulations"): projection thresholds handled by robust
  (eroded/dilated) formulations, not by trusting one smooth gate.
- [ABS] straight-through estimator lines for discrete masks (arXiv
  2602.05119, 2604.21640): modern ML practice = hard binary forward,
  smooth backward — evidence that even the differentiable-relaxation
  community keeps the BINARY decision in the forward/verdict path
  (coherent with C28's gates-absolute doctrine).
- [ABS] OpenSQP (arXiv:2512.05392) + active-set stabilization
  literature (grokipedia/Neumaier/ScienceDirect entries): SQP
  working sets stabilize only asymptotically; zigzagging is mitigated
  by multi-constraint working-set updates per iterate — i.e. the
  standard rhythm for re-deriving a working set is PER STEP/SEGMENT,
  not per multi-segment rung; a frozen working set across many steps
  is nonstandard.
- [TITLE] Blondel et al. 2022 (implicit differentiation of
  crossings; gapmap's named SOTA for differentiating the crossing
  location itself).
Recency span C29: 2004-2026, newest 2026 [ABS].

C30 (bounded vs counted events):
- [ABS] E-ACSL/runtime-assertion-checking family (Frama-C line):
  annotations compiled to runtime checks so violations cannot pass
  silently — the general form of "invariant, not counter".
- [ABS] runtime verification surveys (arXiv:1903.04771 et al.):
  lightweight property monitors as the standard between testing and
  proof. External SOTA adds nothing beyond the repo's own
  counted-events discipline "one level deeper" (gapmap GAP-14 SOTA
  line) — axis closed: this row is repo-internal invariant hygiene.
Recency span C30: 2013-2019 families [ABS].

C47 (debt-ratchet lint policy):
- [ABS] ESLint bulk suppressions (eslint.org, current): committed
  suppressions file counts violations per rule/file; new violations
  fail; falling counts auto-tighten — the industry incumbent-twin,
  and it shares EXACTLY the within-count-swap limit class.
- [ABS] eslint-formatter-ratchet (GitHub/npm): per-file+rule allowed
  counts, thresholds only lower — same pattern, same limit.
- [ABS] Notion engineering blog, custom ESLint ratcheting: ratchet as
  the modernization channel at industrial scale — corroborates
  "standard-di-settore" as declared in the row note.
- [ABS] SARIF v2.1.0 partialFingerprints + baselineState (OASIS
  spec; OpenGrep fingerprint restore; Trivy discussion): the industry
  mechanism for tracking findings ACROSS EDITS is content
  fingerprints, not counts — new/unchanged/updated/absent
  dispositions per finding. This is the census's answer to the
  within-count swap surface: identity-level baselines close it.
Recency span C47: 2018-2026 (living specs/tools), newest = current
ESLint/OpenGrep [ABS].

### 2.3 Corpus recency (§0 point 2)

Span 1987-2026; newest items: CMAME adaptive-beta (2026, in-press),
current ESLint/JAX/OpenGrep docs (2025-2026), OpenSQP (2025), THB
coarsening in optimization (2021). Classical anchors (Lyche-Morken
1987, BDD04, GPB04) carried at [TITLE]/[ABS] as the ledger/gapmap
already names them. No claim below exceeds the depth actually read.

### 2.4 Cava citations (per (iv)) + dedup greps (SR-12, measured this window)

- Cava rows: ADVISORY_litreview_confrontation_2026-08-13.md:513
  [FULL at row]: the driver runs ACTIVE-SET on {L, eps_max, lip,
  truncation} with KKT cone semantics (sign + complementarity) — cited
  for C29 as a constraint on the smooth-gate branch: mask membership
  feeds a KKT object whose semantics are binary
  (member/not-member); a soft membership changes what the multiplier
  prices. NOTE OF RECORD: the cava's own correction/decision numbering
  (its C25-C30, e.g. :1231, :1243) is NOT ledger numbering — grep
  verified; no cava row adjudicates ledger C7/C26/C30/C47 (absence
  claim search-proven: grep -in "C7|C26|C29|C30|C47|mask|freez|activ"
  over the cava, hits inspected, none bears beyond :513).
- Dedup greps (commands run 2026-08-20 in this window):
  - `grep -c "^- id:" docs/choice_ledger.yaml` = 57 (row authority
    count confirmed).
  - `grep -in "multiset|literal swap|within-count" docs/*.yaml` ->
    only C47's own note — the fingerprint-baseline upgrade has NO
    existing home (proposed below as a C47 note-delta + duty detail,
    NOT a new row).
  - `grep -rin "checkify" docs/ validation/ tests/` -> zero hits —
    checkify is fresh census input, closed by stated reason in §3.2.
  - Findings homes confirmed (all five rows already owned):
    constraints:mask-rung-freeze-granularity (findings :1218-1226),
    constraints:mask-crop-lane-loss-unbounded (:1227-1235),
    parametrization:insertion-only-dof-ratchet (:1328-1336),
    engine-core:F3-table-clamp-silent (:573-580, C-D),
    test-suite:numeric-lint-scope-hole (:265-273). [FULL]
  - `grep -in "guest|blondel|lyche|betterer|sarif"
    docs/literature_registry.yaml` -> zero hits (rider candidates
    §4.6).

### 2.5 §0-bis axis bearing (one sentence per axis per row, no padding)

- (1) optimizer query-level: bears on C29 ONLY (the mask feeds
  margin_factory, hence the engine's constraint — engine choice itself
  is C31 territory, adjudicated of record, cited not re-opened); does
  not bear on C7 (between-cycle policy), C26 (state closure guard),
  C30 (bookkeeping), C47 (test suite).
- (2) discrete-vs-continuous adjoint / adjoint consistency: bears on
  C26 (the zero-derivative clamp IS an adjoint-consistency hole — the
  discrete adjoint is exactly consistent with the WRONG clamped
  problem, which is why only a traced flag can catch it) and on C29
  (smooth gate would move membership INTO the differentiated path of
  the custom_vjp stack; frozen binary mask keeps it out — declared);
  does not bear on C7/C30/C47.
- (3) moving-mesh/r-adaptive: bears on C7 only as a boundary (knot
  insertion/removal is DESIGN-space adaptivity; mesh-law adaptivity is
  the landed C9/C56 territory — named, not decided here); does not
  bear on the other four.
- (4) adjoint-free routes: does not bear on any REMPOL row (these are
  policy switches inside a gradient-based certified loop, not search
  strategy choices); no fork here changes if the engine were
  adjoint-free, except C29's smooth-gate motivation would vanish
  (noted for honesty).
- (5) emergent sub-aspects: C47 grew one — finding-identity
  (fingerprint) baselines vs count baselines — named and closed in
  §3.5/§4.5; no other emergent axis.

---

## 3. ADJUDICATION

### 3.1 Row C7 — outer-loop dof policy (NEVER; owner F2/F3, GAP-25)

Incumbent case (genuine): insertion-only is SIMPLE, monotone, and
budget-capped (A1_AKN_MAXINS=3/cycle, adaptive_knot_optimize.py:32-36);
the artifact of record saves the BEST cycle's class, so no failed knot
ever pollutes the of-record object (verifier-established, findings
:1331); every insertion is gated by derived-band machinery, and a
removal path adds a failure mode to a loop that is already certified.
Trees (cite-not-regenerate): diff :56-59 PARTIAL — O-F6 stops on a
derived indicator but has NO removal; V-F13's discovery tier implicitly
allows dof reduction; "No tree defends insertion-only as a ratchet;
none demands removal either. Weak agenda support." [FULL]

Alternatives at their best:
- insert+remove (Lyche-Morken): steelman = removal is the mirror
  image of insertion under the SAME derived band — project to the
  coarser class, measure the deviation, retire the knot iff the
  deviation sits below the band; cheap via the warm-start exactness
  theorem (findings :1335). Census: retire-while-optimizing is live
  modern practice (fully adaptive THB in topology optimization, 2021
  [ABS]).
- AFEM coarsening (BDD04/Stevenson/CKNS): steelman = the only lineage
  with PROVEN optimality — but proven for FIXED problems; our optimum
  MOVES per cycle (verifier-corrected attribution of record, findings
  :1331), so the theorem import fails its pre-registered bar. Loses BY
  THAT STATED REASON as a theorem source; survives as mechanism
  inspiration only (the mechanism is the same removal test).

Adjudication: no tree or census item defends the RATCHET as policy;
D6's "dof economy is part of correctness" is unenforced under the
incumbent; the removal-test leg meets all three pre-registered win
conditions (same band machinery, cheap, artifact-safe). But the ledger
does not flip on unmeasured cost: the removal test has never run.
Outcome class: measurement-gated split, LOAD-CLASS VALVE applied
(sufficient-not-optimized: END-OF-CYCLE removal sweep only — no
continuous coarsening, no THB machinery import for a 1-D knot vector
with m ~ 10-30; declared sufficient, not optimal).
SCOPE CLAUSE respected: the F3-owned loop-build integration is NAMED
(the removal leg lands wherever the F2/F3 loop upgrade lands), not
decided here.

### 3.2 Row C26 — out-of-box behavior (NEVER; C-D owner F2)

Incumbent case (genuine): the silent clamp is jnp.interp's native
semantics — zero implementation surface, and at every RECORD instance
the box hypothesis held (no known out-of-box march state on committed
records); the C7-audit hypothesis "the box contains every
march-realized state" is plausibly true in-corridor.
That case is already ADJUDICATED INSUFFICIENT of record: C-D
(ADVISORY_S24_thermo_closure_survey_2026-08-12.md:253-257 [FULL])
mandates the traced box-exit rejector — a hypothesis without a
rejector violates R5 (AUDIT_agnostic_2026-08-07.md:388-400 verifier
note [FULL]: cert_worst is STRUCTURALLY blind to the clamped-consistent
system). Not re-litigated. The adjudication here is HOW the
traced-flag+rejector alternative closes C-D (gap-accounting; VALVE).

Options for the HOW, each at its best:
- (a) Hand-rolled traced margin diagnostic in the out-dict, checked
  like cert_worst (the C-D owner text's own named form, findings
  :580). Steelman of record: the cert_worst pattern already exists,
  survives scan and custom_vjp untouched, and its check() row is
  verdict-bearing by construction.
- (b) jax.experimental.checkify (census [ABS]): jit-able runtime
  error checking with user/NaN/OOB checks — the in-framework modern
  instrument. Closed by stated reason: checkify functionalizes errors
  through the call tree (transformed signatures through scan; an
  experimental API) and the solve path of record is custom_vjp-closed
  — threading an error monad through the custom_vjp boundary is
  exactly the class of stack surgery the one-lowering discipline
  exists to avoid; and its abort-flavored semantics (Equinox variant
  eagerly aborts) LOSES the record, while certificate discipline
  wants flag + verdict on a completed record. Kept as a named fallback
  if the hand-rolled diagnostic is ever shown to miss a mode.
- (c) Un-traced Python assert: fails criterion (a) outright (staged
  out under jit) — closed.
- (d) Warn-and-extrapolate (Phantom-style [ABS]): closes the SILENCE
  but not the WRONG-PHYSICS (an extrapolated state still certifies);
  fails criterion (b) as a verdict-bearer — closed; retained as
  corroboration that production codes reject silence.

Adjudication: option (a) meets all four pre-registered criteria;
BOTH modes are covered by ONE traced scalar per mode-family:
box_margin = min over the march of (ht - h(T_TAB_LO), h(T_TAB_HI) - ht)
on the linear path, and the same margin read at the _locate/invert_h
entry on the quintic path (an index-clip event iff margin < 0).
SUFFICIENT-NOT-OPTIMIZED declaration (VALVE): guarding ht/T alone is
sufficient because every table read of the closure routes through
ht/T (state_q :397-406; invert_h :308) — no full state-box guard in
all variables is built; declared sufficient, not optimal.

### 3.3 Row C29 — mask freezing granularity (MIXED; owner F2 re-adjudication)

Incumbent case (genuine): rung-freeze WAS panel-ratified (panel C3, of
record) and is not naked — it ships a drift DETECTOR (i_cross drift +
frozen-vs-rederived val_min delta, def_twin:1193-1215) and a declared
repeat-once repair (:1216-1223); at the mild instance the mask
degenerates to the whole control surface and the question is vacuous.
The incumbent's honest weakness is MEASURED, post-adjudication:
C3 FIRED of record (i_cross 96->82 = 14 nodes > STENCIL_RADIUS;
drift_val 9.188e-3 vs mu0 2.118e-3 = 4.3x the floor; the repeat
consumed decisive run 2 — findings :1221 [FULL], gapmap GAP-13
:393-418 [FULL]). Consumed as the brief mandates.

Alternatives at their best:
- Segment-level re-freeze (P2 rhythm): steelman = the mask is THE
  ONLY W-dependent frozen object outside the RK-G P2 re-freeze rhythm
  (findings :1221); re-freezing per segment bounds staleness by one
  segment, keeps binary membership semantics (cava :513: the KKT
  object the mask feeds carries sign+complementarity semantics),
  keeps the C3 detector unchanged, and is the exact granularity the
  active-set census calls standard (working sets are re-derived per
  step; freezing across a multi-segment rung is the nonstandard
  choice — OpenSQP/active-set stabilization entries [ABS]). Cost: one
  mask rebuild per segment = one val_diag run per segment (bounded,
  known cost) vs the measured alternative cost of a FULL RUNG REPEAT
  when C3 fires.
- Smooth gate sigma(val/eps_gate): steelman = removes the freeze
  question entirely (membership tracks val continuously) and makes
  the crossing differentiable (GPB04 lineage; Blondel 2022 for the
  crossing itself). Charged against it, from the census at the depth
  read: (i) eps_gate and the sharpness schedule are a LIVE research
  problem (adaptive-beta CMAME 2026 [ABS]) — an underived constant by
  construction unless derived from a measured val noise floor, which
  nobody has measured; (ii) soft membership changes the margin
  semantics (m_ref, frac_bad, and the multiplier's price all become
  eps_gate-dependent); (iii) even the modern relaxation community
  keeps the binary decision in the verdict path (straight-through
  practice [ABS]) — coherent with the C28 verdict of record: smooth
  surrogates PRICE, binary gates DECIDE; (iv) it moves mask membership
  into the differentiated custom_vjp path (axis (2)) — a stack change,
  not a policy tweak.

Adjudication: the findings row's own [R1] probe IS the discriminator
and the two win conditions pre-registered in §1.1 map onto its two
outcomes exactly (smooth per-segment accumulation -> segment
re-freeze suffices; jumpy crossing -> only then does the gate family
earn its complexity). No position on file or in census defends
rung-freeze as the RIGHT granularity — its own ratifying panel never
saw the alternatives, and the post-adjudication measurement went
against it. Outcome: DECISION-RULE CONVERGED, choice
measurement-gated on [R1]; default direction on current evidence =
segment-level re-freeze (the drift of record is between rung start
and rung end — compatible with smooth accumulation — and every
structural argument (rhythm coherence, binary KKT semantics, C3
retention, bounded cost) favors it); smooth gate = ESCALATION BRANCH
only, entered only on a jumpy [R1] outcome, with eps_gate derived
from a measured val noise floor and the C3 detector retained as hard
referee. The C3 detector stays under EVERY branch (findings :1225,
re-affirmed).

### 3.4 Row C30 — mask crop policy (NEVER; owner "S25 one-liner" class)

Incumbent case (genuine): the crop event IS counted
(mask_shape_adapt, def_twin:679) and printed with the shape-events
dict — the repo's counted-events discipline is applied; at every
record instance the constraint sat inactive by 33x, so a lost lane
has never moved a number.
Alternative at its best: conservation-of-enforcement invariant —
lost_lanes = mask.sum() - mloc.sum() logged per adaptation,
verdict-bearing when nonzero (findings :1234 owner text: one line +
margin_governor counter pattern). Census adds only corroboration
(runtime-verification/assertion families [ABS]: violations must not
pass silently); external SOTA axis closed by stated reason — this is
the repo's own discipline one level deeper (gapmap GAP-14 SOTA line),
no literature fork exists.

Adjudication: the incumbent fails the pre-registered bar not on
counting but on BOUNDING (counted event != bounded event, against the
repo's own C4/C5 standard — findings :1230); the invariant meets its
bar trivially (one line, rides the existing shape_events dict).
Trees SILENT (diff :158) — census carries the row alone, and the
census says: adopt. CONVERGED, not gated: there is nothing to
measure before adopting a monotone-information one-liner; the
measured half is only its negative control. LOAD-CLASS VALVE
declared: sufficient hypothesis = lane loss only ever matters when
nonzero at a margin-active instance; the invariant makes exactly that
event verdict-bearing; no further machinery (e.g. re-derive the mask
on every shape change) is built — sufficient, not optimized.
Never-postpone-resolvables check: the edit is cheap but lives in
def_twin_falsifier.py — outside this panel's write mandate;
structurally gated on the landing window/F2-entry cheap window
(named owner, named trigger — findings :1234-1235). Declared, not
dropped.

### 3.5 Row C47 — numeric-lint enforcement policy (SINGLE-AUTHOR refuter-HARDENED)

Incumbent case (genuine): the per-file count ratchet closed a real
channel (the N_NEWT_INV=8 class went in unseen before R28), never
loosens silently (decrease also fails until ratcheted), fails
unbaselined files outright, and ships a seeded rejector proving it
fires every run (test_numeric_lint.py:23-40 [FULL]); it was
refuter-HARDENED with three added rejector directions (RF-9/B-F12
ADOPTED, ledger note :643). The census confirms the row note's
"standard di settore" claim at [ABS]: ESLint bulk suppressions,
eslint-formatter-ratchet, and industrial ratcheting (Notion) are the
SAME pattern — per-file/per-rule counts, only tighten.

Comparative weighing of the listed alternatives (the owed half —
never done before this panel; each at its best):
- Full per-file classification (the src/ taxonomy): the RIGHT
  ENDPOINT, already the named F2-entry owner (findings :272). It is
  not an alternative to the ratchet but its successor; measured scale
  (37 files / 639 literals, findings :268) makes it a window of its
  own. NOT adopted as immediate policy BY THAT STATED REASON (cost),
  CONFIRMED as the endpoint the ratchet must hand over to.
- Blanket exemption (status quo ante): loses by the measured hole
  itself (the channel demonstrably admitted retired-literal classes)
  — closed, no steelman survives the record.
- Hard fail, no ratchet: steelman = the ONLY policy with zero attack
  surface. Loses on pre-registered criterion (d): it blocks all
  validation work behind a 639-literal remediation whose right form
  is classification (validation/ literals are largely frozen
  record numbers — deleting them is not even the desired endpoint).
  Closed by stated reason; its zero-surface property is inherited
  instead via the fingerprint upgrade below.
- EMERGENT option (census, §2.5(5)): identity-level baseline. The
  industry mechanism for tracking findings across edits is content
  fingerprints, not counts (SARIF partialFingerprints/baselineState
  [ABS]; OpenGrep fingerprints [ABS]). Transplanted honestly to this
  repo (R-4 recalibrated): baseline stores, per file, the sorted
  MULTISET of non-trivial literal values (or its hash) instead of the
  bare count. A within-count literal SWAP then changes the multiset
  and FAILS — the declared limit (the live attack surface named by
  the brief) closes at the cost of a baseline-format change plus one
  seeded rejector direction (in-memory swap must fire). No positional
  fingerprint is needed (value multiset suffices for literals;
  line-drift-immune by construction).

Adjudication: incumbent RETAINED as the channel guard (it won its
hardening on the record and the census confirms the pattern), UPGRADED
by the fingerprint pin (closes the declared limit), with full
classification CONFIRMED as the F2-entry endpoint. Trees SILENT below
granularity (diff :220-224) — census carries the row; zero inflation:
every census claim above is [ABS]-level tool/spec reading, none is
represented as measured benchmark evidence.

---

## 4. PROPOSED VERDICTS + DUTIES
(per-row blocks; deltas are PROPOSED TEXT for the landing window;
nothing is edited by this panel)

### 4.1 Row C7 — proposed outcome

**Measurement-gated CONVERGED-ON-PROTOCOL (direction: insert+remove,
removal-test leg; VALVE: end-of-cycle sweep only).**
Proposed status: NEVER -> "ADJUDICATED-SPLIT (policy converged
2026-08-20 wave-3; removal leg gated on F2-DUTY-C7-REMOVALTEST)".
Pinned protocol + falsifiers:
- **F-C7-1 (removal test):** at cycle end, for each knot, project the
  best design to the class without it and measure the representation
  deviation with the SAME machinery insertion uses; retire iff
  deviation <= the derived band (no new constant; the band is the
  insertion band). Executed FIRST on the recorded S20 cycle (the
  findings-row probe verbatim, :1335).
- **F-C7-2 (artifact safety rejector):** the of-record artifact must
  remain the best CERTIFIED cycle's class; a removal that degrades
  the recorded goal metric beyond the band => removal leg refuted at
  that instance, insertion-only stands with the ratchet DECLARED
  in-row as accepted debt.
- **F-C7-3 (economy carrier):** report dof count + evals/segment
  before/after on the recorded cycle — the D6 dof-economy clause gets
  its first measured enforcement instance.
- What-would-overturn: F-C7-2 firing on the recorded cycle, or the
  measured removal-test cost exceeding the per-cycle insertion budget
  it is supposed to save.
**BINDING F2 duty: `F2-DUTY-C7-REMOVALTEST`** (rides the F2/F3 loop
upgrade window of the findings row; the F3 loop-build integration is
NAMED as F3-owned, not decided — SCOPE CLAUSE).
Dependencies: [X-AKNO] warm-start exactness theorem (makes the
projection cheap); C9/C56 mesh-law territory NAMED as disjoint (axis
(3)). Proposed note-delta additionally records: AFEM-optimality
theorems NOT importable (moving optimum; verifier-corrected
attribution re-affirmed), modern retire-while-optimizing precedent
(THB-in-topology-optimization 2021 [ABS]).

### 4.2 Row C26 — proposed outcome

**CONVERGED-ON-PROTOCOL (traced flag + rejector, hand-rolled
cert_worst-pattern; gap-accounting closure of C-D; VALVE declared).**
Proposed status: NEVER -> "ADJUDICATED (protocol converged 2026-08-20
wave-3; build = the standing C-D repair, owner F2 unchanged)".
Pinned protocol + falsifiers:
- **F-C26-1 (both modes, one scalar per family):** traced
  box_margin_ht = min over the march of (ht - h_lo, h_hi - ht)
  carried in the out-dict; linear path reads it at state_q entry,
  quintic path at _locate/invert_h entry (clip event iff margin < 0).
  Checked like cert_worst: margin < derived mollification band
  (~4*DeltaT joint census, C-C machinery) => verdict row FAILS.
- **F-C26-2 (negative control / rejector-fires):** a planted state
  with ht below h(T_TAB_LO) (the audit's own suggested test,
  AUDIT_agnostic_2026-08-07.md:398) must FIRE on BOTH paths; silence
  on either => the diagnostic is refuted, C-D stays open.
- **F-C26-3 (adjoint-hole documentation):** the fired flag carries
  the mode (clamp vs extrapolation) — the clamp mode is an
  adjoint-consistency hole (zero exterior derivative), to be named in
  the R4 back-propagation when the repair lands.
- What-would-overturn: checkify (or successor) becoming
  custom_vjp-transparent AND cheaper — the named fallback would then
  be re-weighed; or a measured in-corridor false-fire rate above the
  mollification band (would force the band's re-derivation).
**F2 duty: the standing C-D repair itself** (engine-core:
F3-table-clamp-silent owner text unchanged — this panel adds the
protocol pins, it does not re-own).
Dependencies: C-C joint-census hypothesis (mollification band
source); C25 envelope-box row (CONV slot this wave — the box the
margin is measured against; named, not decided here).

### 4.3 Row C29 — proposed outcome

**DECISION-RULE CONVERGED, choice measurement-gated on [R1]; default
= segment-level re-freeze; smooth gate = derived-constant escalation
branch only.**
Proposed status: MIXED -> "ADJUDICATED-SPLIT (decision rule converged
2026-08-20 wave-3; granularity choice gated on F2-DUTY-C29-MASKGRAIN
[R1] replay)".
Pinned protocol + falsifiers:
- **F-C29-1 (the [R1] discriminator, adopted as adjudication
  protocol):** replay the recorded run-1 segment bases through
  cs_stats, i_cross per segment (findings :1225 verbatim). Smooth
  monotone accumulation across segments => segment re-freeze ADOPTED;
  a jump > STENCIL_RADIUS within one segment => escalation branch
  armed. Threshold derived, not chosen: the same STENCIL_RADIUS the
  C3 gate already uses.
- **F-C29-2 (segment re-freeze acceptance):** under segment
  re-freeze, replay the recorded rung: C3 must go quiet (drift per
  segment <= STENCIL_RADIUS) and the decisive-run-2-class repeat cost
  must vanish; C3 still firing at segment granularity => segment
  re-freeze refuted, escalation branch mandatory.
- **F-C29-3 (smooth-gate entry conditions, pinned NOW for the
  escalation branch):** eps_gate DERIVED from the measured val noise
  floor on the recorded lanes (no literal); beta/sharpness under a
  declared continuation schedule (adaptive-beta line cited [ABS]);
  the C3 binary detector RETAINED as hard referee (C28
  gates-absolute doctrine, consumed per (iii)); margin semantics
  delta (m_ref/frac_bad under soft weights) documented with a
  measured before/after on the recorded rung.
- **F-C29-4 (detector permanence):** under EVERY branch the C3
  detector stays; any branch that proposes removing it is refused by
  this pin.
- What-would-overturn: a jumpy [R1] outcome overturns the default (by
  design); a measured val noise floor too high to derive eps_gate
  would close the escalation branch and leave segment re-freeze
  unconditional; a future margin-ACTIVE instance with segment
  re-freeze still stale would re-open the row (named trigger).
**BINDING F2 duty: `F2-DUTY-C29-MASKGRAIN`** = F-C29-1/2 execution
(+ F-C29-3 only if armed). Both legs driver-touching (S21 pin,
findings :1225) — F2-owned, re-affirmed.
Dependencies: C28 verdict (priced-frontier/gates-absolute — the
doctrine constraint on the gate branch; shared-source declared:
O-F19's regime-cell advocacy partially converges with rung-freeze,
diff :156-157, and is NOT double-counted as support for the smooth
gate); cava :513 (KKT membership semantics); C30 (the crop invariant
rides the same mask object — landing should sequence C30's one-liner
first, it instruments C29's replay for free).

### 4.4 Row C30 — proposed outcome

**CONVERGED (adopt the conservation-of-enforcement invariant;
one-liner class; VALVE declared; not measurement-gated).**
Proposed status: NEVER -> "ADJUDICATED (converged 2026-08-20 wave-3;
build = the F2-entry cheap window of the findings row)".
Pinned protocol + falsifiers:
- **F-C30-1 (invariant):** lost_lanes = int(mask.sum() - mloc.sum())
  logged per adaptation event (rides shape_events); campaign verdict
  row: lost_lanes == 0, or nonzero loss DECLARED with the lane list
  and the margin state at that instance (verdict-bearing iff
  margin-active).
- **F-C30-2 (rejector-fires negative control):** the findings-row
  trigger instance planted deliberately (M_NODES change between
  derive and rung) must produce nonzero lost_lanes; silence => the
  counter is refuted.
- What-would-overturn: nothing at this cost — the only honest
  overturn is measured overhead, which for an int subtraction is
  nil; declared closed on cost + honesty.
**Duty: the existing findings-row owner unchanged** (F2-entry cheap
window, :1234); this panel adds only the verdict-row semantics pin.
Dependencies: C29 (same mask object; sequencing note in §4.3).
Materiality declared: immaterial to numbers of record
(inactive-by-33x), material to certificate honesty at margin-active
instances — decided on cost.

### 4.5 Row C47 — proposed outcome

**CONVERGED (incumbent ratchet RETAINED + fingerprint upgrade pin;
classification confirmed as F2-entry endpoint).**
Proposed status: SINGLE-AUTHOR -> "ADJUDICATED (alternatives
comparatively weighed 2026-08-20 wave-3; ratchet retained with the
multiset-fingerprint upgrade pinned; classification = endpoint,
F2-entry owner unchanged)".
Pinned protocol + falsifiers:
- **F-C47-1 (fingerprint upgrade, closes the declared limit):**
  baseline format upgraded from per-file COUNT to per-file sorted
  multiset of non-trivial literal values (or its stable hash);
  within-count swap => baseline mismatch => FAIL. Migration is
  mechanical (the --inventory mode already enumerates every unlisted
  literal, test_numeric_lint.py:44-45).
- **F-C47-2 (seeded rejector direction, new):** an in-memory
  single-literal SWAP (count preserved) must fire every run,
  alongside the existing count-bump rejector; silence => upgrade
  refuted, the count ratchet stands with the limit re-declared.
- **F-C47-3 (ratchet-down semantics preserved):** removal of a
  literal still fails until the baseline is regenerated (the
  never-loosens-silently property is format-independent — pinned so
  the upgrade cannot weaken it).
- What-would-overturn: a measured false-fire burden from benign
  refactors (e.g. of-record scripts that legitimately re-derive the
  same value set) above the F2-entry review budget — would demote the
  fingerprint to warn-tier and re-open the pin.
**F2 duty: unchanged owner** (test-suite:numeric-lint-scope-hole,
per-file classification of the baselined 639); F-C47-1/2/3 land as a
test-suite edit in the landing window or the F2-entry hygiene window
— NOT a new row (dedup-verified §2.4: no existing home, but it is a
note-level amendment of C47, not a new choice).
Dependencies: none binding. Closed alternatives: blanket exemption
(the measured hole), hard-fail (blocks 639-literal remediation whose
right endpoint is classification; steelman inherited via F-C47-1).

### 4.6 Literature-registry rider (rides the landing; grep-verified absent §2.4)

Proposed entries (all [ABS] or [TITLE], depth recorded in-entry —
zero inflation): Lyche-Morken 1987 (knot removal; C7 verdict leans on
it as the mechanism name) [TITLE, WANTED-class]; Guest-Prevost-
Belytschko 2004 (smooth-gate ancestor; C29 escalation branch)
[TITLE]; SARIF v2.1.0 partialFingerprints (C47 upgrade provenance)
[ABS, spec]. Landing window decides inclusion per registry policy.

### 4.7 PAPERS NEEDED (mandatory section, §0-bis(c))

- CONDITIONAL ASK (fires only if F-C29-1 lands JUMPY and the
  escalation branch arms): Guest, Prevost, Belytschko, "Achieving
  minimum length scale in topology optimization using nodal design
  variables and projection functions", IJNME 61 (2004) — full text
  needed to transplant the projection/continuation discipline
  honestly before any eps_gate derivation; the claim that waits on it
  is F-C29-3's continuation schedule. Not needed for the default
  branch.
- No other row of this panel has a conclusion waiting on a full text:
  C7/C26/C30/C47 verdicts rest on repo-measured evidence + [ABS]-level
  pattern confirmation, and no claim above is asserted beyond the
  depth read.

### 4.8 Candidate new rows

NONE. All five rows already have findings-registry homes with owners
(measured greps §2.4); the two genuinely new census products
(checkify option for C26, fingerprint baseline for C47) are
note-level amendments of existing rows, dedup-verified unhomed as
rows and deliberately NOT minted (they are protocol details, not
choices).

### 4.9 Cross-cluster consistency (declared)

- C29/C28: gates-absolute doctrine consumed, O-F19 shared advocacy
  declared once (§4.3), no double-count.
- C29/C31: the smooth gate would change the constraint the engine
  sees — engine adjudication cited, not re-opened.
- C26/C25: the envelope-box row (CONV slot, this wave) defines the
  box the C26 margin guards — named seam, no double-adjudication.
- C7/C9-C56: design-space vs mesh-law adaptivity boundary declared
  (axis (3)); no overlap adjudicated.
- C47/C-ledger hygiene: the fingerprint upgrade touches only
  tests/test_numeric_lint.py + baseline JSON — disjoint from every
  other wave-3 slot's files.

INFLATION CHECK: done — every census entry carries its depth marker;
no [ABS] item is cited for a quantitative claim; all numbers above
trace to committed repo files at line anchors re-read this window;
the two S24-era measured numbers used (C3 fire: 14 nodes / 4.3x
floor; 16 adaptations) are cited from their findings rows, not
re-measured (of-record discipline).

---

## 5. MACHINE SUMMARY

```yaml
cluster: REMPOL
rows:
  C7:
    proposed: "ADJUDICATED-SPLIT — insert+remove direction (end-of-cycle removal-test leg, same derived-band machinery); insertion-only retained until measured; AFEM theorem-import rejected (moving optimum)"
    gated: true
    duty: "F2-DUTY-C7-REMOVALTEST (rides F2/F3 loop-upgrade window; F3 build named-not-decided)"
  C26:
    proposed: "ADJUDICATED — traced box-margin flag + rejector (cert_worst pattern), both modes, negative control mandatory; checkify closed by stated reason (custom_vjp boundary), kept as named fallback; VALVE: ht/T-margin sufficient-not-optimized"
    gated: false
    duty: "standing C-D repair (engine-core:F3-table-clamp-silent, owner F2 unchanged; pins F-C26-1..3 added)"
  C29:
    proposed: "ADJUDICATED-SPLIT — decision rule converged ([R1] discriminator, STENCIL_RADIUS threshold); default = segment-level re-freeze; smooth gate = escalation branch only with derived eps_gate + C3 detector permanent (C28 gates-absolute consumed)"
    gated: true
    duty: "F2-DUTY-C29-MASKGRAIN ([R1] replay + segment-refreeze acceptance; escalation pins pre-armed)"
  C30:
    proposed: "ADJUDICATED — conservation-of-enforcement invariant adopted (lost_lanes per adaptation, verdict-bearing iff nonzero at margin-active); one-liner class, VALVE declared, not gated"
    gated: false
    duty: "existing findings-row owner (F2-entry cheap window) + F-C30-1/2 semantics pins"
  C47:
    proposed: "ADJUDICATED — count ratchet retained + multiset-fingerprint baseline upgrade pinned (closes the within-count swap surface, SARIF-fingerprint lineage); blanket-exemption and hard-fail closed by stated reason; classification confirmed F2-entry endpoint"
    gated: false
    duty: "F2-entry hygiene owner unchanged (test-suite:numeric-lint-scope-hole); F-C47-1..3 land as test-suite amendment"
census_recency: "1987-2026; newest: CMAME adaptive-beta projection (2026 in-press), current ESLint/JAX/OpenGrep specs (2025-2026), OpenSQP (2025); 8 queries, protocol table in-file"
alternatives_closed: 12
inflation_check: done
rows_adjudicated: 5
deltas_proposed: 5
escalation_candidates: 0
papers_needed: "1 CONDITIONAL (Guest-Prevost-Belytschko 2004 full text — only if F-C29-1 lands jumpy)"
candidate_new_rows: 0  # dedup-verified by measured grep (§2.4): checkify + fingerprint = note-level amendments, not rows
counts_sr12: "ledger rows = 57 (grep -c '^- id:' docs/choice_ledger.yaml, this window); findings homes for all 5 rows verified at :1218/:1227/:1328/:573/:265"
```

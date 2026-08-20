# BRIEF — BLOCCO 3 WAVE 2 PANELS (Phase C adjudications, right-sized v2)
# S-FOUNDATIONS-C2, 2026-08-19. Clusters: C31TRIO (C31-IP/C32/C33) /
# C1REP (C1 + C2-conditional + C3-challenge + C49) / C2021 (C20+C21).
# Your cluster is named in your task prompt. BASE =
# validation/sfoundations_raws_2026-08-13.

## §0 FRAME
The §0 FRAME of `BASE/blocco3/BRIEF_wave1_panels.md` applies VERBATIM
and is binding (formalize-then-search, modern census with reported
recency, trees-as-advocates by file:line, zero inflation, per-row
adjudication, measurement-gated split with pinned protocol+falsifier,
dedup navigation-first, output schema, env pins). Read it first.
Output file: `BASE/blocco3/PANEL_<cluster>.md`
(<cluster> = C31TRIO | C1REP | C2021).

## §0-bis USER DIRECTIVE 2026-08-19 (binding, supersedes nothing —
## EXTENDS §0; applies to EVERY row of EVERY cluster)
(a) NAMED CROSS-CUTTING AXES: beyond the row's listed alternatives,
the census MUST close (by stated reason, wherever the axis bears on
your rows): (1) optimizer QUERY-LEVEL choice (which engine, modern
SOTA — not only the families the ledger lists); (2) DISCRETE vs
CONTINUOUS adjoint, and adjoint CONSISTENCY of the chosen
discretization (our stack of record: JAX custom_vjp = discrete
AD-adjoint of the marched scheme — the choice itself was NEVER
adjudicated, no ledger row exists: verified 2026-08-19); (3)
MOVING-MESH / r-adaptive families (MMPDE, monitor-function
equidistribution, front-fitting-as-mesh-motion) and the
adjoint-in-moving-mesh interaction; (4) ADJOINT-FREE routes (DFO,
Bayesian/surrogate optimization, evolutionary — at their genuine
best, modern lines); (5) any further sub-aspect that EMERGES during
your census — name it, close it or hand it up as a candidate row.
The list (1)-(4) is EXEMPLARY, not exhaustive — the user stated the
rule twice: this is the GENERAL METHOD for every analysis. EVERY
sub-problem you encounter (inside or beside your rows) gets the same
treatment: formalize it -> confront the modern literature -> state
conclusions at the depth actually read -> ask for papers when full
text is needed. Nothing closes by omission or by approximate
reading.
(b) READ-DEPTH HONESTY (no hallucination, no approximate reading):
every census entry carries its read-depth marker — [FULL] (full text
read) / [ABS] (abstract/metadata only) / [TITLE] (existence only).
Claims above the depth actually held are FORBIDDEN. A conclusion
that would need full text you cannot access does NOT get asserted:
it becomes a PROCUREMENT ASK (c).
(c) PROCUREMENT CHANNEL: the user uploads papers on request. Your
panel file gets a section "PAPERS NEEDED" (may be empty): exact
reference + why the census needs the full text + what claim waits on
it. The orchestrator forwards the asks to the user. Never silently
settle for the approximate reading.
(d) CANDIDATE ROWS: axes (2)/(3)/(4) have NO ledger home today —
where your adjudication develops them beyond your rows' scope,
propose the new row (dedup-verified) in your §4 for the landing
window; do not mint it yourself.

## §0-ter WORLD-CLASS CENSUS PROTOCOL (binding, adopted 2026-08-19
## after over-engineering audit; EXTENDS §0 point 2 and §0-bis)
Your census section MUST additionally carry:
(a) QUERY PROTOCOL TABLE: search strings VERBATIM + databases/
communities covered (incl. the Russian classical school where your
territory is classical-adjacent) + date + counts
(hits/screened/included). Completeness is falsifiable, not asserted.
(b) QUESTION-ANCHORED + PRE-REGISTERED DECISION CRITERIA: your §1
(formal statement) OPENS, per row, with THE SINGLE MAIN QUESTION
that choice exists to answer in this program (one sentence; the
user's prassi: every modeling/algorithmic choice is read from its
driving question). Then, BEFORE any search, freeze per-row WHAT
WOULD MAKE EACH OPTION WIN (decision criteria DERIVED from that
question, not from generic quality). Mid-census amendments legal,
declared with reason. The refuter will attack post-hoc
rationalization against this section.
(c) MATERIALITY: per-row, estimate whether the alternatives differ
above the relevant tolerance/noise floor of the program; an
immaterial fork is decided on cost/simplicity and DECLARED
immaterial (depth follows stakes — this is the anti-over-engineering
valve, use it honestly in BOTH directions).
(d) STEELMAN: every option you reject, reject at its BEST modern
instance, cited.
(e) Your census is DATED (validity stamp in the file).
(f) PER-ROW AXIS BEARING: for each §0-bis axis, one sentence per
row — bears / does not bear and why. No silent omission, no ritual
padding.

WAVE-1 CONSUMPTION (new, binding): read
`BASE/blocco3/VERDICT_wave1.md` (per-row verdicts C28/C27/C9/C11)
BEFORE adjudicating. Where your cluster depends on a wave-1 outcome,
CONSUME the adjudicated verdict (cite it); if the row you depend on
carries an ESCALATION (unsettled), adjudicate MODULO the open
outcomes: state which of your conclusions are invariant and which
are conditional on each branch, and name the conditionality.

## §C31TRIO — OPTIMIZER ENGINE (IP half) + CURVATURE POLICY +
## CONSTRAINT CURVATURE

Rows: docs/choice_ledger.yaml:450-462 (C31 optimizer engine, MIXED:
CONVERGED for eq-path, IP path NEVER — incumbent scipy trust-constr
with the IP path in use since S22; alternatives IPOPT, filter SQP,
SLQP, Uno, proximal-bundle), :464-472 (C32 curvature policy,
SINGLE-AUTHOR: fresh full FD Hessian per segment vs SR1-carry
alternative; speed audit declined quasi-Newton 'OUT by policy' with
no fresh survey), :474-483 (C33 constraint curvature, NEVER: scipy
default BFGS vs exact HVP fwd-over-rev vs FD-of-exact-gradient;
route fact of record: solve is custom_vjp only so jacfwd is blocked
as written — cite ADVISORY_engine_speed_audit_2026-08-12.md par.7.3 +
ADVISORY_S25bis_diff_convergence_2026-08-12.md B-F11).

Diff anchors: BASE/phaseB_tree_diff.md:159-167 (C31: 4/4 CONVERGENT
on TR-SQP-class with derived constants as the CERTIFICATE CLOSER —
O-F16/17 TR-filter SQP with radius constants from the measured
rho-histogram; H-F36 TR-SQP + exact penalties; V-F30 error-aware
inexact TR; P-F27; derivative-free strictly quarantined to
exploration; NONE recommends interior-point as the closer — the
in-use IP path is ACTIVELY CHALLENGED), :168-173 (C32: CG-truncated
Newton on Hessian-VECTOR products in-flight, full spectrum only at
S*; V-F24 Lanczos + derived tolerance; ties to C33, C48 and the
engine:vmap-hessian-adjoint-divergence row), :174-175 (C33: same HVP
family, O-F21 item 6).

WAVE-1 DEPENDENCY: C28's adjudicated representation of the
certifiability constraint (priced-in-KKT vs binary-outside) changes
what the engine must close: consume VERDICT_wave1 C28 (and C27's
aggregation outcome for the constraint structure the engine sees).

QUESTIONS TO FREEZE (shared sub-problem: second-order infrastructure
of the certified design loop; per-row questions individuated):
C31-IP: which engine CLOSES the certificate at the boundary-active
optimum (TR-SQP-class vs interior-point vs current trust-constr IP
path), given the certifiability representation from C28 and the P4
gate discipline; C32: curvature information policy across segments
(fresh FD Hessian per segment vs SR1/quasi-Newton carry with
certified-pair conditions + stale-symptom re-measure + directional
rejector vs HVP-based truncated Newton); C33: curvature of the
CONSTRAINT block (default BFGS vs exact HVP vs FD-of-gradient),
respecting the custom_vjp route fact. Census axes: certificate
semantics at active-set optima, nonsmooth/MPCC interaction,
measured-cost per segment (the speed-audit numbers are of record —
cite, do not re-measure), JAX/adjoint compatibility (one-lowering
discipline row cross-lowering-gradient-floor: gradient comparisons
pin ONE lowering).

Measurement-gating expectation: engine/curvature flips are
build+measure work (F2). Converge on representation + protocol pins
(which benchmark, which derived threshold, what refutes what);
measured half = named binding F2 duty.

## §C1REP — DESIGN BASIS CLASS + RIGHT-END BC (conditional) +
## LEFT-END BC (challenge) + SOLUTION REPRESENTATION (C49)

Rows: docs/choice_ledger.yaml:133-143 (C1 design basis,
SINGLE-AUTHOR on the oscillation axis: incumbent interpolating cubic
heights-as-dofs vs B-spline control polygon / CST / Hicks-Henne; D6
S20 rejection of record D6:915-926 = the incumbent's case to
represent genuinely), :145-154 (C2 right-end BC, NEVER, CONDITIONAL:
if C1 flips to control points, C2 dissolves — the notaknot-twin
DIAGNOSTIC of record: corner residual -82%, cd shift 8.2%, adoption
never adjudicated), :156-162 (C3 left-end BC, DECIDED constructional
— the ONLY decided row directly challenged by the trees), :651-661
(C49 solution representation, NEVER, minted at Phase B; owner note =
the mandate: Form-2 with a GENUINE captured-only advocate seeded
from the trees' option blocks; user question of record 2026-08-17
"perche si fitta una soluzione che potrebbe essere catturata").

Diff anchors: BASE/phaseB_tree_diff.md:22-33 (C1 DIVERGENT-ENRICHING
HIGH: O-F4 Bernstein-form coefficient bounds = EXACT sample-free
sufficient certificates for curvature/angle/cone constraints +
compactness/A(c)-membership by construction, existence link O-F30;
V-F13 two-tier split discovery/certificate; H-F34(f); P-F19 spline
certificate class + analytic Rao spine cross-check — the NEW second
axis = admissibility-certificate EXACTNESS beyond D6's oscillation
axis), :34-37 (C2 conditional dissolve), :38-44 (C3 CHALLENGED:
P-F21 rounded lip at the curvature-bound floor, adjoint regularity
argument; H-F18 exact centered-corner Prandtl-Meyer fan as internal
data at Lambda), §3.3 :330-335 + §2.13 :282-293 (adjoint front-terms
designed-in, Giles-Pierce class — the load-bearing fitted-tier
argument) + §2.14 :294-299 (|J_capture − J_fitted| as measured (v)
carrier) for C49. C49 tree advocacy (from the row note): V-F6/F27,
H-F4/F8/F9/F28, O-F9, P-F12 — the captured option AT ITS GENUINE
BEST; represent it genuinely (the user mandate), never as strawman.

QUESTIONS TO FREEZE (shared sub-problem: WHAT object the optimizer
moves and WHAT object the certificate certifies; per-row
individuated): C1: dof basis for the wall contour (interpolating
cubic vs control-polygon/CST/Hicks-Henne vs two-tier), with the NEW
exactness axis adjudicated ALONGSIDE the D6 oscillation axis (the D6
rejection is single-author evidence FOR the incumbent — weigh it,
do not inherit it); C2: ONLY as declared conditional (adjudicate the
dissolve condition + what happens if C1 holds: the notaknot adoption
question stays F2 — do NOT adjudicate the BC itself here beyond the
conditionality structure); C3: re-open the constructional status vs
the two tree alternatives (rounded lip / PM-fan internal data) —
this touches the census-pin territory (lip circles, cone condition
P-c tension §4.8): NAME the census-lemma interaction, do not decide
census-owned items (F2-exit pin respected); C49: fitted vs captured
vs two-tier vs implicit tracking (HOIST/Zahr; Bonfiglioli-Paciorri)
for the per-phase solution representation — the certificate-bearer
question. Census axes: exact-certificate representations (Bernstein/
B-spline bounds literature, modern CST/shape-parametrization lines),
adjoint consistency across shocks (Giles-Pierce and successors,
modern implicit shock tracking), two-tier architectures in modern
design-optimization practice.

Measurement-gating expectation: C1 flip candidates need the
change-of-basis certificate protocol (post-solve change-of-basis =
S25 evidence pointer) pinned; C49 two-tier needs the
|J_capture − J_fitted| carrier protocol + falsifier pinned (F2/F5
duty). C3 outcome may be a DERIVED-condition amendment (lip radius
at the curvature floor) — if so, pin its falsifier.

## §C2021 — CERTIFICATE QUALIFICATION + SEED VALIDITY

Rows: docs/choice_ledger.yaml:334-345 (C20, NEVER, owner F2 HIGH:
incumbent unqualified one-extra-step ratio; alternatives
kappa(J)-aware derived bound / Kantorovich-alpha-theory /
branch-consistency monitor / interval-Newton [X-IVXC]), :347-356
(C21, NEVER: incumbent asserted O(h) predictor + stale replay seeds
(C2-F2 mitigation); alternatives alpha-theory per-seed certificate /
Kantorovich radius ([X-TBAK] pattern in z); of record: S25-bis
traced-predictor seeds shipped gate-verified = implementation delta,
not an adjudication).

Diff anchors: BASE/phaseB_tree_diff.md:106-112 (C20 ENRICHING:
O-F20 solvability-first doctrine — per-sector sufficient solvability
regions derived dry-level; if the optimum is interior, the hidden
constraint never fires and the certificate is structurally clean — a
NEW qualification mechanism alongside the listed three), :113-115
(C21 ENRICHING: continuation-defined branch + V-F7 fold-margin
monitor inf_xi sigma_min as seed-validity instrument, alternative
family to alpha-theory/Kantorovich).

WAVE-1 DEPENDENCY: C28's outcome (priced certifiability / solvability
regions were part of O-F20's advocacy there) — consume VERDICT_wave1
C28 and keep the two uses of O-F20 distinct: C28 = how the frontier
enters the OPTIMIZATION; C20 = how a delivered certificate is
QUALIFIED. Do not double-count the same advocacy as two independent
validations (declare the shared source).

QUESTIONS TO FREEZE (shared sub-problem: a-priori/a-posteriori
qualification of Newton-based certified solves; per-row
individuated): C20: qualification of the per-column/per-solve
certificate (unqualified ratio vs derived kappa(J) bound vs
Kantorovich/alpha-theory vs interval-Newton vs solvability-region
pre-qualification); C21: validity policy for SEEDS (asserted O(h) +
replay vs per-seed certificate vs Kantorovich radius vs fold-margin
monitored continuation). Census axes: modern validated-numerics and
alpha-theory lines (Smale successors, interval-Newton practice),
continuation/fold-monitoring in design loops, cost per solve at
production counts.

Measurement-gating expectation: both rows likely converge on
protocol+falsifier pins (qualification bound implemented + measured
tightness; seed-certificate fire rate on record campaigns) with the
measured half = named F2 duty.

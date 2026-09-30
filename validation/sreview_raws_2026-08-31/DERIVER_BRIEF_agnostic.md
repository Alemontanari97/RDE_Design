# DERIVER BRIEF — de-novo attack on the problem statement (agnostic; the ONLY input of each deriver; v2 after the order-1 refuter)

READ FIRST: `PROBLEM_STATEMENT_agnostic.md` in this directory (the statement
is the whole problem). HARD INDEPENDENCE RULE: do not open, grep or read any
other file of this repository (no documentation, no other files of this
directory or its parent, no source code, no registries, no logs). Your output is
DISCARDED if it shows knowledge of project-internal names, identifiers,
decisions or sessions. Open-literature knowledge is welcome and must be
tagged [KNOWLEDGE] with author/year (or "textbook") and a read-depth marker:
[full] if you know the work in detail, [abstract] if only its gist, [title]
if only its existence. Never inflate: an approach may be described only as
strongly as your knowledge supports.

## Your deliverable — TWO objects

(1) A structured markdown file you WRITE yourself at the path given in your
task message (one file per lens), containing the complete trees below.
(2) The structured return (schema provided) = a condensed index of the file
(the file is authoritative; the index must not contradict it).

## Level 0 — SP0 STRATEGIES (answer Q0 before any sub-problem; OPEN enumeration)

Enumerate the overall STRATEGIES by which Q0 could be answered, each as a
TUPLE:
  (objective of §2; treatment of the time-dependence of the inflow; spatial
   representation of the flow; flow solver and how the optimizer obtains the
   information it needs; search strategy and the class of guarantee attached
   to the result; the ONE decisive result that would establish the
   strategy's worth).
Two strategies are distinct if they differ in at least one tuple entry.
Include the practice a working propulsion engineer would use today, the
strategies the open literature on periodically unsteady flows and on shape
optimization suggests, hybrids (different entries for the DESIGN loop and
for the EVALUATION of competing designs), and any strategy that changes the
OBJECTIVE or the DESIGN VARIABLES rather than the method. Do not prune to
the obvious; a strategy may be rejected only FOR A STATED REASON, never by
omission. For EACH strategy: the question it really answers (Q0 or a
narrowing of it — say which); cost to a CREDIBLE answer (compute,
person-time, new theory); generality (nozzle configurations, data classes
A-G); which USER PINS of §1 it needs and which it could relax;
falsifiability (what result kills it); time-to-number; its rank in your
recommendation; the mandatory field "WHICH MEASUREMENT WOULD MAKE ME
ABANDON IT"; and the decisive result you would pre-register for it.

## Level 1 — SUB-PROBLEM TREES (for your top strategy; where another
## strategy would differ, say so)

For each sub-problem: the 2026 option space at its genuine best, each option
with cost / generality / risk / literature precedent ([KNOWLEDGE] + depth
marker) / falsifier; your recommendation with grounds; the decision
criterion (what evidence, theorem or measurement decides it); what would
falsify your recommendation; whether the sub-problem is LOAD-BEARING (a
wrong choice poisons the decisive answer) or local.

- SP-OBJ OBJECTIVE: what quantity is optimized, what is constrained, over
      which set of operating conditions — and which choice a propulsion
      referee would accept as THE question (is the nozzle's mean
      performance even the engine's lever, versus combustor-side losses?).
- SP1 TIME: how the time-dependence of the inflow enters the design
      problem (for the design loop and, separately, for the evaluation of
      competing designs); how the residence-time ratio of §1 is measured
      and what each treatment requires of it.
- SP2 FLOW MODEL AND SOLVER for the nozzle under the given data, including
      embedded discontinuities, separated states (the per-instant
      attachment constraint of §4 and how it is enforced) and the
      truncated-base region.
- SP3 INFORMATION FOR THE OPTIMIZER: how the optimizer obtains what it
      needs from the flow model (derivatives or otherwise), how that
      information behaves across discontinuities, and how it is verified
      with a test that can REJECT it.
- SP4 SEARCH STRATEGY over the design space, including the class of
      guarantee attached to the result (local / global / bounded gap) and
      how designs whose state cannot be validated are handled inside the
      search.
- SP5 SPATIAL REPRESENTATION: dimensionality / symmetry of the flow
      representation, what it loses versus the rotating three-dimensional
      field, and how that loss is MEASURED (not estimated); whether the
      designer and the evaluator should use different representations.
- SP6 GEOMETRY AS DESIGN VARIABLES: representation of the solid,
      admissibility certificates (curvature, slope, attachment, envelope),
      as-built tolerance handling, existence of a maximizer.
- SP7 DATA: how each available data class A-G enters the model (generated
      from specs, fitted from captured fields, surrogate), the admissibility
      audits of §3 with loud reject, how the data weights and their
      uncertainty propagate to the answer; for each USER PIN of §1 (pure
      periodic single-mode wave; frozen thermally-perfect mixture; single
      phase) the MAGNITUDE of its effect on the decisive result (with
      provenance) and the cost of relaxing it.
- SP8 PROOF: what constitutes proof that a computed design or number is
      right (per-solve validity checks, a-posteriori error estimation,
      validated numerics, cross-code, experiment), with bands and safety
      factors of derived origin; and how that proof survives changes of
      code version, hardware and execution environment (what margin makes a
      result quotable; how a non-reproducing result is owned).
- SP9 THE DECISIVE RESULT for Q0: configuration, data class, comparator
      (and why it is the STRONGEST one), metric, accuracy class (thrust-
      stand 0.5-1%), bands, kill criterion, pre-registered outcomes
      including the negative one; sensitivity of the decisive difference to
      the data weights and to the base-region model; the EXTERNAL anchor of
      the number (which independent evidence — high-fidelity computation,
      experiment, cross-code — at which accuracy class); the scope of the
      generalization claim from one design point.
- SP-PB BASE REGION: modelling of the truncated base region (plug-type
      solids) and its uncertainty band relative to the materiality
      threshold of §8; whether the decisive difference can be resolved
      above that band.
- SP-CARM THE STRONGEST COMPETING PRACTICE: which classical design, at
      which representative inflow state, with which base treatment, a
      competent designer would field against any new method — and whether
      a competent designer already averages duty in some way.

## Form

Order of battle (dependency order of the forks, load-bearing first).
Dry-level arguments (lemma / counterexample / scaling estimate with explicit
hypotheses) wherever a fork is decidable by a short argument. Keep prose
tight: the trees are the deliverable, not an essay. Number every option.
Every tolerance derived; every recommendation with hypotheses + falsifier.

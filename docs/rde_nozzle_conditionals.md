# CONDITIONALS LEDGER (L4) — the named conditionals, stated ONCE
# (layer L4 of the SCAFFOLD architecture; [F1/SCAFFOLD-M] task M-4)

Status: LEDGER OF RECORD (2026-07-17, S9). Every THEOREM* in the
corpus inherits its conditionals BY ID from this ledger or from the
declared closure/residual conditionals of the registry
(docs/claims_registry.yaml: C-HT4, C-IGMIX, C-O33 — model closures
and numeric residuals, NOT analytic gaps; justification per SCAFFOLD
§3 rule 4 recorded in their entries). This file states the TWO
analytic conditionals; the registry's `inherits` fields are the live
heir index, machine-checked by suite group (xv). CONTENT RULE: the
statements below are TRANSCRIPTIONS of the sources of record
(remaining_conditionals §1; M0 D2.5 + G12-L2) — no rewriting, no new
mathematics. Adding a NEW conditional requires justifying why it is
not one of these two (maintainer contract, SCAFFOLD §3).

------------------------------------------------------------------------------
## C-D25U — uniform semiglobal stability (THE shared analytic conditional)

STATEMENT (verbatim source: docs/rde_nozzle_remaining_conditionals.md
§1, target class THEOREM*). Let D(delta, L_x, C_geo, C_dat) be the
certified set: wall in C^2 with norm <= C_geo; data on the inflow
segment with C^1 norm <= C_dat; axial spacelikeness margin
M_x - 1 >= delta; boundary-function margin >= delta; on shocked
references, Lax front-strength margins >= delta with transversal
wall/front angles >= delta. CLAIM: on D, for x-intervals of length
<= L_x, the S1 solution map (wall, data) -> (U, fronts) is
well-defined and LIPSCHITZ into piecewise-C^1 x C^1-graphs, and C^1
(in the shift sense across fronts), with ALL constants depending ONLY
on (delta, L_x, C_geo, C_dat) — never on the individual solution.

DISCHARGERS (named, none written; source §1): U1 smooth regions
(Li-Yu semiglobal instantiation, Gronwall along characteristics);
U2 slip-wall reflection estimates; U3 fronts (local straightening +
the G12-L2 certified equilibrated s_min, uniform by strength
margins); U4 composition (finitely many regions/fronts, constants
multiply). Discharge cost: bounded classical two-variable
bookkeeping, not research risk.

FALSIFIER: a certified family in D with solution-map Lipschitz
constant blowing up while all margins stay >= delta.

HEIRS (by ID, as of S9; live index = registry `inherits` fields,
lint-checked): [T-T7FS], [T-P7S1], [T-P3], [T-G12S1], [T-LEMA-iv],
[S-S1U], [S-P4F], [S-LBML].
CONSEQUENCE OF DISCHARGE: T7-FS, P7-S1, P3 and (with its assembly)
S1-U convert THEOREM* -> THEOREM in the shock-free class, and the
across-front conditional sharpens to C-MAJDA alone.

------------------------------------------------------------------------------
## C-MAJDA — front stability across fitted shocks

STATEMENT (transcription; sources of record: M0 D2.5 — S1 canonicity
across transversal shocks is a DECLARED conditional "backed by Majda
stability of the fitted fronts"; docs/rde_nozzle_G12_S1.md §2 —
Lemma G12-L2 gives the quantitative finite-dimensional brick).
CLAIM: every fitted transversal front of an S1 reference is
MAJDA-STABLE — the linearized Rankine-Hugoniot map is uniformly
nonsingular (margin bounded away from zero along the front), so the
front position and downstream traces depend Lipschitz-continuously
on the incoming traces, licensing (i) S1 canonicity across shocks
(D2.5) and (ii) shift-differentiability of the fitted-front shape
calculus (G12-S1 residues R-G12.1, R-P3.1).

QUANTITATIVE BRICK ALREADY PROVEN (machine-verified, carrier
[X-G12], PASS 9/9): the linearized RH is nonsingular STRICTLY inside
the Lax condition and degenerates EXACTLY at characteristic fronts
(= the Prop. A2 kernel law [T-A2]); the equilibrated s_min at the
reference is a measured, certified number. WHAT REMAINS CONDITIONAL:
uniformity over the certified family (the function-space step —
strength margins => uniform s_min), i.e. the U3 ingredient of
C-D25U.

FALSIFIER: a certified-Lax front family with degenerating linearized
RH margin (would contradict the G12-L2 margin law).

HEIRS (by ID, as of S9; live index = registry): [D-S1] (canonicity
across fronts), [T-P3], [T-G12S1], [S-S1U].

------------------------------------------------------------------------------
## Reading rule

A THEOREM* cites its conditionals by ID only (e.g. "inherits:
[C-D25U, C-MAJDA]"); the statement is never restated at the citing
site. The registry is the index; THIS file is the single statement
location; the proofs-in-waiting live where the sources of record put
them (remaining_conditionals §1 architecture; G12 §2 brick).

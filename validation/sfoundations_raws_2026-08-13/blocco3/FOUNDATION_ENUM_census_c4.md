# FOUNDATION-CHOICE ENUMERATION — CENSUS ARTIFACT (S-FOUNDATIONS-C4)
# Written 2026-08-21 at the COVERAGE GATE REPAIR pass, discharging critic
# finding CGC-3: the C4 gate brief's FOUNDATION-CHOICE ENUMERATION category
# had mint side-effects (C59/C60, G-14, H20/P34 rows) but no accounting
# carrier — no class definition, no sweep record, no candidate table, no
# closing census. This file is that carrier. Every count/absence claim is
# from a command run in THIS repair window (SR-12), quoted at the claim.

------------------------------------------------------------------------------
## 1. CLASS DEFINITION

A **foundation choice** is a stack-level commitment of the design program —
an axis on which the pipeline PRACTICES one option (by construction, by
inheritance, or by default) while genuine alternatives exist at the SOTA —
whose flip would re-enter multiple downstream adjudications. The defect
class this category hunts (established by the user catches at C49/C56/C58):
**practiced-but-unrowed** — an incumbent is live in the pipeline, sometimes
even weighed of record OUTSIDE the ledger, but NO choice-ledger row exists,
so no future flip has a pinned falsifier to consume and the question can
close by omission. The category's mandate is to HUNT such axes (not merely
transcribe pre-named candidates — the critic's CGC-3/CGC-4 point), and to
close with a census: instances found, homes named, negative statement for
the rest.

Discipline inherited: choice-adjudication-convergence (every algorithmic
choice point adjudicated vs SOTA alternatives, CHOICE LEDGER as artifact);
K1 convention (a minted-but-open row with owner+trigger IS coverage);
zero inflation (a candidate without a genuine practiced incumbent or
without genuine alternatives is rejected with reason, not minted).

------------------------------------------------------------------------------
## 2. CLASS HISTORY — THE SEVEN CAUGHT INSTANCES

| # | Row | Axis | How caught |
|---|---|---|---|
| 1 | C49 | per-phase solution REPRESENTATION (fitted vs captured vs two-tier) | Phase-B diff omission, S-FOUNDATIONS 2026-08-17 |
| 2 | C56 | adjoint REALIZATION per role (discrete AD vs continuous vs dual-consistent) | C9/C11 wave-1 landing 2026-08-19 (VERDICT_C9C11_supplement §4.3) |
| 3 | C58 | differentiable-stack FOUNDATION (JAX vs Enzyme/Tapenade/hand-coded/gradient-free) | user catch 2026-08-20 (3rd instance named as a class) |
| 4 | C59 | TEMPORAL form of the functional (cycle-average vs HB/time-spectral/windowed) | C4 gate window mint 2026-08-21 (injection candidate, addendum-c4 (e) scoping) |
| 5 | C60 | optimizer ARCHITECTURE (NAND vs SAND/LNKS vs hybrids) | C4 gate window mint 2026-08-21 (FORK_LEDGER_141_adjudication D-1/O15 rider executed) |
| 6 | C61 | base-pressure CLOSURE MODEL p_b (Veen legacy-practiced/WG10-FAILED vs WG10 bracket vs Nasuti-Onofri vs derived N2 vs measured) | critic CGC-4, minted at THIS repair pass — the hunted instance the transcribed enumeration missed |
| 7 | C62 | PHASE QUADRATURE over Xi (uniform trapezoid practiced vs Gauss/adaptive/QMC; mint-or-canonicity decision inside the row) | critic CGC-5, minted at THIS repair pass |

The critic's structural diagnosis stands confirmed: instances 1-5 were all
pre-named in the enumeration's inputs; instances 6-7 required the HUNT the
category's first execution skipped.

------------------------------------------------------------------------------
## 3. STACK-LEVEL SWEEP (performed THIS window, pipeline stage by stage)

Method: walk the pipeline stages of record (M0 architecture + the ledger's
own clustering); at each stage ask "what is PRACTICED here, and does a
C-row or a declared home carry the choice?". Sweep commands quoted in §4.

| Stage | Practiced foundation item | Ledger row / declared home |
|---|---|---|
| Interface data / contract | datum = phase-aligned fields + declared fronts, product-ball acceptance | C50 (CLOSED 2026-08-20) + contract findings rows F-1..F-10 (:1643-:1661, :2299-:2353) |
| Interface data / contract | Gamma_d placement, signature status, mean-state rung | C52/C53/C54 (minted 2026-08-19) |
| Thermo | tabulated-backend model (generators free, interface = tables) | C24 (Thermo closure) + standing directive S11 (memory thermo-tabulated-backend); box/out-of-box = C25/C26 |
| Thermo/interop | Cantera-generator -> JAX-consumer interop via tables | declared home = the S11 directive itself (tables ARE the interop contract); no separate axis — the interop question is definitionally inside C24/C25/C26. `grep -icE "interop|cantera" docs/choice_ledger.yaml` = 0 (the WORD is absent; the AXIS is carried, declared here) |
| Numerical precision | float64 everywhere (G0 measured basis: docs/rde_nozzle_G0_decision.md:50 "float64, this host"; roundoff floors C18) | NO dedicated C-row (`grep -icE "float64|x64|precision" docs/choice_ledger.yaml` = 0). DECLARED HOME assigned by THIS census: named sub-axis of the C58 F2-entry census (the framework census weighs precision/mixed-precision as part of "which foundation best realizes the adjudicated architecture"); floors themselves are rowed at C18. Not minted separately: no genuine rival is practiced or advocated anywhere in the record (float32/mixed-precision appears in NO artifact — zero-inflation rule), and the C58 entry contract is the natural adjudication site |
| Per-phase solve | solution representation (fitted/captured/two-tier) | C49 |
| Per-phase solve | march numerics cluster (mesh law, refinement, start line, axis process, damping, caps) | C9/C10/C12/C13/C16/C17 (rowed of record) |
| Lowering | one-lowering policy (no cross-lowering composition) | C48 note (one-lowering, m6gate adjudication) + findings :328 engine:cross-lowering-gradient-floor (`grep -icE "lowering" docs/choice_ledger.yaml` = 7 — carried) |
| Temporal form | cycle-average (canonical-inside-the-pin) | C59 |
| Phase averaging | quadrature rule over Xi (uniform trapezoid practiced) | **C62 — minted at this repair (CGC-5)** |
| Objective/constraints | constraint aggregation; certification metric/qualification; P_amb aggregation | C27; C19/C20; C55 |
| Gradient/adjoint | adjoint realization per role; FD steps; curvature | C56; C44; C32/C33 |
| Optimizer | engine ([P-IPADJ] / Uno arm-B); architecture (NAND/SAND); exploration tier | C31; C60; C57 |
| Foundation stack | AD framework | C58 |
| Certification layer | SDP backend for certificate solves (Clarabel/MOSEK, decided S17 brick-2 by SOTA-survey) | NO C-row (`grep -icE "SDP|Clarabel|MOSEK" docs/choice_ledger.yaml` = 0; only repo hit outside memory = docs/rde_nozzle_PROGRESS_ARCHIVE.md). **CANDIDATE-8, named — see §5** |
| External expansion | base-pressure closure p_b (truncated plug/shrouded) | **C61 — minted at this repair (CGC-4)**; solve mechanics = findings :2519 (H20); harvest = BASE_PRESSURE_HARVEST_c4.md |
| External expansion | plume vortex-sheet stability / decoupling | findings :1607 (distinct-by-declaration from H20) |

------------------------------------------------------------------------------
## 4. SWEEP COMMANDS (the record surfaces searched, all run this window)

- Ledger title census: `grep -nE "^- id: C[0-9]+|^  choice:" docs/choice_ledger.yaml`
  — all 62 titles read; the stage table above maps every practiced stack
  axis found onto them.
- Negative greps (0 hits each, measured): `grep -niE "base.pressure|p_b|Veen"
  docs/choice_ledger.yaml` (pre-C61); `grep -niE "quadrat"` (pre-C62);
  `grep -icE "float64|x64|precision"`; `grep -icE "interop|cantera"`;
  `grep -icE "SDP|Clarabel|MOSEK"`.
- Positive home greps: `grep -icE "lowering"` = 7 (C48 cluster);
  `grep -n "id:" docs/findings_registry.yaml` filtered for the
  contract/plume/engine rows cited above.
- Commit sweep for practiced-but-undocumented arrivals: the 12 C4-window
  commit messages (`git log --oneline 3db05d5~1..HEAD`, measured 12 this
  window incl. the post-sweep 634b972) — the b3da86d harvest commit is the
  carrier that exposed the C61 axis.

------------------------------------------------------------------------------
## 5. CANDIDATE TABLE (found / disposition)

| Candidate axis | Found by | Disposition |
|---|---|---|
| p_b closure model | harvest b3da86d + critic CGC-4 | **MINTED C61** (NEVER, incumbent-declared: Veen practiced in legacy chain only, program slot declared N2 — problem book :348) |
| phase quadrature over Xi | diff §2.10 + critic CGC-5 | **MINTED C62** (NEVER, incumbent-declared: uniform trapezoid practiced; mint-or-canonicity decision carried inside the row) |
| float64 precision policy | this census sweep | NOT MINTED, zero-inflation: no rival practiced or advocated anywhere in the record; declared home = C58 F2-entry census sub-axis (named there by this census) + C18 floors |
| Cantera/JAX table interop | this census sweep | NOT MINTED: the axis is definitionally inside the S11 directive + C24/C25/C26 cluster (tables are the interface contract); no independent choice surface |
| SDP backend (Clarabel/MOSEK) | this census sweep | **CANDIDATE-8, NAMED-NOT-MINTED**: decided S17 brick-2 by SOTA-survey (decision of record, memory s17-brick2-kickoff; archive trace docs/rde_nozzle_PROGRESS_ARCHIVE.md) but NO ledger row; the certificate-solver stack is on the SAME F2-entry decision surface as C58/C31 ([P-IPADJ] cluster). Owner assigned by this census = the C58/C31 F2-entry engine census window; trigger = the F2-entry engine act (the C60 trigger verbatim). Minting adjudication belongs to that window — this census records the candidacy so the question CANNOT close by omission. If the F2-entry census confirms the practiced-incumbent + live-alternatives shape, it mints (8th instance); if the SDP layer is retired from the F2 stack, it dies with a named reason |
| march numerics / optimizer / thermo axes (all others swept in §3) | this census sweep | already rowed (see §3 mapping) — no further practiced-but-unrowed instance found |

------------------------------------------------------------------------------
## 6. CLOSING CENSUS + NEGATIVE STATEMENT

**7 instances of the class caught to date (C49, C56, C58, C59, C60, C61,
C62 — §2), of which 2 minted at this repair pass. One further candidate
(SDP backend) NAMED with owner+trigger, adjudication deferred to its
decision surface, deferral structurally-gated and declared (never-postpone
rule respected: the cheap part — the candidacy record — is executed here;
the adjudication is F2-entry-gated by the same surface that owns C58/C60).**

Negative statement, search-proven: over the surfaces swept in §4 (the full
62-row ledger title census, the findings-registry id census, the pipeline
stage walk of §3, and the 12 C4-window commit messages), **no additional
practiced-but-unrowed foundation choice was found** beyond the seven caught
instances and the one named candidate. Bound declared: the sweep covers the
stack levels of the pipeline of record (data contract -> thermo -> per-phase
solve -> lowering -> temporal/averaging -> objective -> adjoint -> optimizer
-> certification -> external expansion -> foundation stack); axes OUTSIDE
the pipeline of record (e.g. presentation/tooling) are out of class by the
§1 definition.

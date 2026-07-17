# SCAFFOLD — The optimal architecture of the theory corpus
# (blueprint of record for every future maintainer: Opus, Fable, human)

Status: ARCHITECTURE DOCUMENT OF RECORD (2026-07-17, [F1/SCAFFOLD]).
Purpose: re-examine the theory corpus as built (organically, by
session accretion) and define the OPTIMAL scaffolding for future
work — formally complete, implementation-ready, maintainer-agnostic.
This document does not change any mathematics; it defines the target
structure, the claim registry that makes the theory LINTABLE, the
maintainer contract, and the migration plan with acceptance criteria.
ANCHOR: everything serves (P) of M0 D2.6 — the pair (S*, delta).

------------------------------------------------------------------------------
## §0 Diagnosis (honest, one paragraph)

The corpus is COMPLETE and TRACEABLE but not OPTIMALLY SHAPED: truth
is distributed over M0 + D1-D7 + eight attack documents + session
logs; addenda override earlier text in place (correct but layered);
the named conditionals (D2.5-U et al.) are referenced from five
places; per-claim state (class, scope, carrier, falsifier, inherited
conditionals) must be reconstructed by reading. A maintainer landing
cold spends a session rebuilding the graph that the authors hold in
their heads. The fix is NOT rewriting the mathematics — it is giving
the corpus the same discipline the code already has: a typed,
machine-checkable REGISTRY plus a layered reading order.

------------------------------------------------------------------------------
## §1 Target architecture: six layers + one registry

 L0 ANCHOR (2 pages, stable): the problem (P) verbatim (D2.6), the
    rigor legend, the standing directives (gamma-general; pristine;
    verification-sufficiency; periodicity-as-runtime-opportunity;
    anchor-to-(P); one-session-at-a-time; radical citation honesty).
    A maintainer reads L0 FIRST and knows the objective and the rules.
 L1 DEFINITIONS & CONTRACTS: D2.1-D2.6, the interface contract and
    audits, solution classes, the measure. (Today: M0 Part II — keep,
    referenced by ID.)
 L2 THEOREM CORPUS (statements ONLY, one per ID, with class, scope,
    inherited-conditional IDs, carrier IDs, falsifier — proofs
    referenced, not inlined). This is the layer the registry mirrors.
 L3 PROOFS (full, one location per proof; today: M0 Part III + the
    attack documents — they remain the proof layer; no duplication).
 L4 CONDITIONALS LEDGER: every named conditional stated ONCE with its
    constant dependencies and its dischargers (today: D2.5-U in
    rde_nozzle_remaining_conditionals.md §1 is the model). Every
    THEOREM* references conditionals by ID only.
 L5 IMPLEMENTATION FORMULATION: M0 Part VI + VI.4bis pins — the only
    layer the engine reads; each pin cites the theorem IDs that
    ground it.
 L6 OPEN REGISTER: everything not closed, each with discharge cost
    and falsifier (today: remaining_conditionals §5 + the OP list).
 SESSION LOGS: unchanged, append-only, the audit trail (never
    normative).
 CONFLICT RULE (unchanged): L0-L6 of record beat any historical note;
 within the layers, the registry is the INDEX, never the content.

------------------------------------------------------------------------------
## §2 The claim registry (the heart): theory-as-code

File: `docs/claims_registry.yaml` (to be created in the migration).
One entry per object, schema:

    id:        T-LEMA-ii            # stable, never reused
    kind:      theorem | definition | conditional | conjecture |
               schema | carrier | oracle | directive
    class:     THEOREM | THEOREM* | SCHEMA | CONJECTURE | PRACTICE
    scope:     "irrotational homentropic S1; EOS-general"
    statement: one-sentence normative form
    doc:       docs/rde_nozzle_P2_lemmaA.md#3.4
    proof:     docs/... (for theorems)
    inherits:  [C-D25U]             # conditional IDs, empty if none
    carrier:   [X-PA1]              # executable scripts, empty if
                                    # function-space (then suffices: no)
    suffices_symbolic: yes | no
    falsifier: one sentence
    gamma:     EOS-general | gamma-const-oracle | perfect-gas-oracle

CLAIM LINT (new test group, mirror of the numeric lint): a committed
script `tests/test_claims_lint.py` that (a) parses the registry,
(b) verifies every referenced doc anchor exists, every carrier script
exists and is in the run_all suite, every THEOREM* has nonempty
`inherits`, every THEOREM with `suffices_symbolic: yes` has a
carrier, no orphan IDs in docs (grep), and (c) REJECTS on any
violation. The theory then cannot silently drift from its index —
the same rejector discipline the numbers already have.

SEED INVENTORY (the full graph as of 2026-07-17; the migration turns
this table into the YAML):

| ID | Kind/Class | Object | Carrier / inherits |
|---|---|---|---|
| D-P | definition | problem (P) = pair (S*, delta) (D2.6) | — |
| D-CONTRACT | definition | interface contract + audits (D2.4, D1) | audit fields in data |
| D-S1 | definition | solution class S1 + canonicity status (D2.5) | boundary function |
| C-D25U | conditional | uniform semiglobal stability (constants delta, L_x, C_geo, C_dat) | dischargers: U1-U4 (remaining_conditionals §1) |
| C-MAJDA | conditional | front stability across fitted shocks | inherited by S1 canonicity, R-P3.1, R-G12.1 |
| T-TH0 | THEOREM | thrust definition chain, storage exact | proof M0; group (ii) |
| T-O1 | THEOREM | Isp == J at frozen choked feed | proof M0/D3 |
| T-O2 | THEOREM | log-uniform blowdown measure | st_core generator |
| T-T0 | THEOREM | wave-frame exactness, instantaneous constancy | flatness diagnostic |
| T-NSW | THEOREM | axial spacelikeness frame-invariant | margin audit |
| T-T3 | THEOREM | collapse, fixed wall (H1-H4) | groups (ii)(vi) |
| T-T3-CE | THEOREM | two-gamma counterexample + gamma_eff 2nd order | group (ix) |
| T-T4 | THEOREM* | plug peak design (ideal-adaptation closure) | groups (vi)(x) |
| T-GB | THEOREM | geometry-free ceiling + SONIC CAP | group (viii); real-thermo route group (xi) |
| T-OP11e | THEOREM | eps-diagram statements (1)-(4) + scope (5) + multiplicity (6) | group (x); premium_bound |
| T-LEMA-CL | THEOREM | classical stationarity system (L.6)-(L.16), EOS-general | X-PA1 Part 1 |
| T-A2 | THEOREM | kernel solvability on characteristic surfaces | X-PA1 Part 2 |
| T-A3 | THEOREM | f2 = transported adjoint invariant (irrot. homentropic) | X-PA1 Part 3 |
| T-LEMA-iv | THEOREM* | Hoffman component map (page-verified) | inherits C-D25U at field level |
| T-LEMB | THEOREM+SCHEMA | discrete transpose identity + mesh-limit | X-G0 spike; mesh limit -> T-LBML |
| T-P3 | THEOREM* | averaged multipliers lambda2 in L^inf(dmu) | inherits C-D25U; residues R-P3.* |
| T-G12S1 | THEOREM* | shape calculus with fitted shocks (x-as-time) | X-G12; inherits C-D25U, C-MAJDA |
| T-N6-1 | THEOREM | swirl structure (pencil, kernel, laws) | X-N6 Part A |
| T-N6-2 | THEOREM | free-vortex verbatim extension of Rao | X-N6 Part B |
| T-N6-3 | THEOREM | swirl obstruction identity (iff free vortex) | X-N6 Part B3 |
| T-N6-5F | THEOREM (structure) | five-field adjoint: (A,B,M), Lagrange id., gauge l(n) closed form | X-5F; assembly = S-5F |
| T-T7FS | THEOREM* | differentiation under the cycle integral ((P)(ii) rigorous) | inherits C-D25U |
| T-P7S1 | THEOREM* | argmax exists on certified level sets ((P)(i)) | inherits C-D25U |
| S-S1U | SCHEMA | S1-internal uniqueness (bricks proven) | assembly steps named |
| S-5F | SCHEMA | five-field assembly (wall/corner/E_sw) | route named |
| S-P4F | THEOREM* stmt | P4 Fredholm = monodromy condition (1 not in spec Pi) | spectral margin = P1a/P1b |
| S-LBML | SCHEMA | Lemma-B mesh limit (Lax-equivalence route) | O3 falsifiers |
| J-CT1 | CONJECTURE | O(St) corrector (periodic re-scoped) | O5/O4 |
| J-OP11 | CONJECTURE | contour-level topology (duty split) | sector tournament |
| X-PA1 | carrier | pa1_symbolic_lemmaA.py (19/19) | — |
| X-G12 | carrier | g12_shock_linearization.py (9/9) | — |
| X-N6 | carrier | n6_swirl_kernel.py (16/16) | — |
| X-5F | carrier | n6_fivefield_adjoint.py (6/6) | — |
| X-G0 | carrier | g0_spike_jax_moc.py (+ axisym extension in progress, S8-op) | — |
| O-G2 | oracle | S-H 1971 Table 2 diagonal 2290 lbf (E4 gate) | to RUN |
| O-RAOPLUG | oracle | Rao 1961 spike p. 95/Table 3 (C_F 1.5804) | RaoPlug fix gate |
| O-Ob1..7 | oracle | lit_b0bis registry (R5-gated) | to adopt |
| DIR-* | directive | gamma; pristine; sufficiency; periodic-runtime; anchor-(P); one-session | memories + L0 |

(Reading of the table: a maintainer greps an ID, lands on the one
normative statement, sees its class, its carrier, and what it
inherits. NOTHING in the corpus should be citable without an ID.)

------------------------------------------------------------------------------
## §3 Maintainer contract (the "how to work here" page, L0 material)

 1. OPEN: read L0, then the registry, then PROGRESS. Do not read
    history unless auditing.
 2. Every new claim gets an ID, a class, a scope, a gamma tag, a
    sufficiency declaration, a falsifier, and (if symbolic-
    sufficient) a carrier WITH a rejector — before it is cited
    anywhere else. The claim lint enforces this mechanically.
 3. Every discovery mid-work back-propagates SAME SESSION (R4) to the
    proof layer AND the registry.
 4. Conditionals are stated once (L4) and inherited by ID; adding a
    new conditional requires justifying why it is not C-D25U or
    C-MAJDA.
 5. Numbers: only from committed scripts with rejectors (R5,
    unchanged). Citations: only what was read (radical honesty,
    unchanged). Sessions: one at a time, total-order logs, gate
    before execution (unchanged).
 6. The engine (A1+) may only consume L5; if an implementation needs
    a fact not in L5, the fact is first added to L2/L5 with its ID —
    code never front-runs the registry.

------------------------------------------------------------------------------
## §4 Migration plan (bounded, mechanical, verifiable)

 M-1 Create `docs/claims_registry.yaml` from the §2 seed (pure
     transcription; no new mathematics). ACCEPT: every ID resolves.
 M-2 Write `tests/test_claims_lint.py` (checks (a)-(c) of §2) and add
     it to run_all as group (xii). ACCEPT: suite green; a seeded
     deliberate violation is REJECTED (rejector demo).
 M-3 Refactor M0 into L0+L1+L2 pointers (statements stay, proofs
     move by reference only — M0 remains the single master file but
     gains the ID spine; the attack documents become the L3 proof
     layer they already are). ACCEPT: coherence grep, no content
     change (diff = structure only).
 M-4 Consolidate the conditionals into L4 (one file, two entries:
     C-D25U, C-MAJDA + pointers). ACCEPT: no THEOREM* without an
     `inherits` ID; grep-verified.
 M-5 Promote the four rigor carriers from validation/ into the test
     suite (fast tier where runtime allows; else a `--rigor` tier).
     ACCEPT: CI-executable proof layer.
 Cost estimate: one dedicated session (M-1/M-2), one more for
 M-3/M-4/M-5. Zero mathematical risk (structure-only, lint-guarded).

------------------------------------------------------------------------------
## §5 What this buys (why it is the optimal shape)

 - A maintainer (any model, any human) is productive after reading
   TWO pages (L0) plus a grep — instead of a session of archaeology.
 - The theory cannot drift: class inflation, orphan claims, silent
   gamma=const, missing falsifiers are all MACHINE-REJECTED.
 - Papers assemble by query: P-1/P-2 sections cite IDs; the claim map
   of the skeleton becomes a registry view, not a parallel artifact.
 - The single-conditional architecture makes the residual honesty
   auditable at a glance: today the whole theory hangs on C-D25U +
   C-MAJDA and nothing else — that fact, which took this campaign to
   establish, stays VISIBLE structurally.
 - The scaffold is model-agnostic: it encodes the working discipline
   (gate, R4, sufficiency, pristine) as checkable structure rather
   than as prompt lore.

# VERDICT — (A) Contract diff: blind formalizations vs record; (B) Phase D proof L4 => R1

**Role**: JUDGE, S-FOUNDATIONS session bundle (raws keyed 2026-08-13; this verdict authored
2026-08-17). **Authority**: final rigor classes, DOWNGRADE-ONLY; ready-to-land adjudication.
**Plan anchor**: [F-FOUNDATIONS/Phase B+D] per `validation/ADVISORY_Sfoundations_prompt_2026-08-13.md`.

**Inputs read in full**: `contract_blind_pde.md`, `contract_blind_data.md`, `contract_blind_brief.md`;
M0 `docs/rde_nozzle_MASTER.md` Part II (D2.1-D2.6 incl. L4-DEFAULT block, lines 65-336);
`phaseD_L4_implies_R1.md` (r2, 1529 lines, in full); `refute_L4R1_r2_l0.md`, `refute_L4R1_r2_l1.md`
(round-2 refutations; round-1 files consumed via the r1/r2 revision blocks, which anchor every repair).
**Loop state given of record**: refutation loop capped at round 2, NOT-DRY (refuters still producing
objections at cap; all r2 objections consumed by the r2 revision, but the r2-delta repairs have had
ZERO adversarial coverage). **Blind-slot failures: 0.**

**Absence-claim discipline (navigation-first)**: every "absent of record" claim below was
search-verified: grep of M0 for `BV|bounded variation` (hits only in D2.5 solution-theory citations),
`Rankine|jump admissib|budget` (no datum-audit hit; line 577 is theorem context),
`metric|validity window|error bar|uncertainty` (no datum-contract hit); grep of D1
`docs/rde_nozzle_problem_book.md` for `data class|BV|4.3bis` (contract slot named abstractly at
lines 166/182; §4.3bis = subsonic decision tree; no function-space pin). Search scope declared:
M0 + D1 problem book. Other D-docs not swept; severity assignments carry that bound.

---

## PART A — STRUCTURED CONTRACT DIFF

Legend: **[PDE]** = `contract_blind_pde.md` (hyperbolic/trace lens); **[DATA]** =
`contract_blind_data.md` (test-data/UQ lens); **[REC]** = record site.

### (i) RE-DERIVED — independent validation (9 items)

| # | Element | Blind side | Record side |
|---|---------|-----------|-------------|
| R-1 | Supersonic-cut causality with margin as THE legitimacy condition; margin = the certificate | [PDE] C5.1 + D5.1 margin monitor M1 (ess-inf u_nu − a, report violating-set measure); [DATA] Claim 5.1 (M_n ≥ 1+δ with k_c·U(M_n) dressing) | [REC] D2.4 R1 + L4-DEFAULT ("u_x − c ≥ delta margin is the standing certificate"), [T-NSW] mean upstream influence EXCLUDED BY THEOREM |
| R-2 | Characteristic counting 5-supersonic / 4-subsonic; subsonic fifth scalar = closure, never data; closure taxonomy (re-place / impedance / non-reflecting / abandon-cut) with prices; full-state forcing on subsonic patches BANNED | [PDE] C4.1-C4.3; [DATA] Claim 4.1, Def 4.2 (C1/C2/C3-banned) | [REC] D2.4 R2 ("full state only on axially supersonic patches ... incoming invariants + impedance or choking closure, decision tree D1 §4.3bis O1-O4") |
| R-3 | Three cycle representations: time-periodic ≡ phase loop (exact under pure rotating wave) ⇒ one-point measure (strict loss: phase correlations); one-point averages need only the measure; downstream propagation needs the loop | [PDE] D2.3/C2.1 incl. identity (2.1); [DATA] Def 2.3/Claim 2.4 (with the χ(r)-shift counterexample) | [REC] D2.3 mu = pushforward of cycle time (= the measure form), rung-2 objective on it; idealization ladder I0-I4 in D2.4 (I1 = wave frame, I2 = per-phase, I3/I4 = collapsed) |
| R-4 | Wave-frame steady reduction EXACT but conditional on axisymmetry + rotation-invariant BCs + uniqueness/attractor-symmetry hypotheses (named open) | [PDE] C3.1 (H1-H5, gaps declared); [DATA] Claim 3.1 ([PS] at nonlinear level) | [REC] I1 rung + M0 Part V table line 1337 (wave-frame implicit BVP anchor); record's conditionals ledger discipline |
| R-5 | Mode transition / loss of pure periodicity voids the per-phase machinery; purity monitored spectrally | [PDE] (P6), A3, A8; [DATA] (P4), A6 four-clause purity audit, B3 catastrophic bifurcation | [REC] D2.3 scope note (mode transition has no steady per-state F, violates H-A1, routed to robust layer VI.4bis(v)); T0-flatness monitor pin `periodic-wave-data-scope` |
| R-6 | Placement downstream of all heat release + frozen thermally-perfect downstream gas with tabulated caloric window | [PDE] (P1), (H-th); [DATA] (P1), Def 0.2, A5 window guard | [REC] D2.4 "downstream of all heat release"; scope pins frozen/thermally-perfect (memory 2026-08-11); thermo-tabulated backend |
| R-7 | Averaging does not commute with the physics: the mean-datum single solve is NOT an admissible reduction (O(Var) error, no small parameter) | [PDE] C3.3 wave-stress defect, C3.5; [DATA] Claim 3.4 (Jensen counterexample), 3.5 | [REC] the entire rung architecture: averaged objective evaluated on the MEASURE (R-3), never on the averaged state; I4 declared as ladder rung, not approximation; D2.6(v) bar-class note (bars ESTIMATED, not certified) |
| R-8 | Closure choice must be identical across phases and design candidates | [PDE] C4.3 closing paragraph; [DATA] implicit in Def 4.2 pricing | [REC] H3-cl "certified phase-independent closure patch pattern" (D2.4 vocabulary addition) |
| R-9 | Datum acceptance = audit gauntlet with per-audit REJECTING tests and derived tolerances | [PDE] §6 A1-A13; [DATA] §6 A1-A12 + seeded-fault validation of the monitors themselves | [REC] D2.6 stage-A admission audits (characteristic completeness per Lemma 4; Crocco compatibility; per-phase spacelikeness margin; declared closure) + R5 rejector discipline |

**Verdict (i)**: the record's contract SKELETON (cut + margin causality + counting/closures +
measure representation + purity scope + audit-with-rejector culture) is independently re-derived
by BOTH lenses from the physics alone — strong validation that the recorded structure is forced,
not stylistic.

### (ii) DEMANDED-BY-BLIND, ABSENT OF RECORD — finding candidates (10 items)

Each = candidate findings-registry row; severity per repo convention; each with the rejecting test
that would kill the finding.

- **F-1 (P2) — No function-space pin for the interface data class.** Both blinds INDEPENDENTLY
  converge on `BV ∩ L^∞(A; K)` (K compact admissible box), one-sided traces on the jump set, with
  the refinement-stability rejector (TV Cauchy under record/mesh refinement) — [PDE] D2.1/A7,
  [DATA] Def 2.1. [REC] D2.4 and D1 carry "(Gamma_d, data class, validity)" with the class slot
  UNINSTANTIATED (search-verified above). Independent double convergence on the same space is the
  strongest possible blind signal. *Rejecting test*: exhibit a data-class pin in any of-record doc
  (search bound declared above); if found, F-1 dies to a cross-reference fix.
- **F-2 (P2) — Datum-internal admissibility audits missing from the stage-A list.** Moving
  Rankine-Hugoniot consistency on the datum's OWN jump set at the wave trace speed + entropy
  admissibility (no expansion shocks) — [PDE] A6, [DATA] Claim 2.6(i)(ii)/A3/A4. Detects
  fabricated/corrupted/independently-interpolated data. [REC] D2.6 stage-A audits do not include
  it. *Rejecting test*: an of-record audit row implementing datum-side RH/entropy checks.
- **F-3 (P2) — No uncertainty contract on the datum.** Both blinds demand the datum ship as a
  calibrated SET, not a point: nominal + declared metric + certified radius + validity window W
  with extrapolation = NO DATUM (rejected, not error-barred) + robustness obligation on the
  consumer (intervals must separate before two designs are declared distinct; ties reported as
  ties) — [PDE] §7 D7.1/C7.1-C7.3, [DATA] §7 Def 7.1-7.3/Claim 7.4. [REC] has the "validity"
  slot name, D2.6(v) estimated bars, and the A6 robust layer — but no metric, no radius
  semantics, no extrapolation rule at the contract site. *Rejecting test*: of-record definition
  of the datum-space metric + window semantics. (Metric CHOICE itself is disputed between the
  blinds — see D-3.)
- **F-4 (P3) — Global budget-closure audits** (cycle-mean mass/enthalpy flux vs metered feed and
  injected enthalpy within combined uncertainty) — [PDE] A4, [DATA] A1/A2. Cheap, catches
  datum-vs-machine inconsistency. Absent from stage-A list.
- **F-5 (P3) — Design-sweep invariance falsifier** ([DATA] C-ii: same combustor, ≥2 deliberately
  different downstream geometries; datum must be invariant within noise — "THE primary rejecting
  test of the entire cut"). [REC] relies on theorem-level exclusion ([T-NSW], now phaseD Thm 1);
  the sweep is the EXPERIMENTAL test of the theorem's hypotheses and catches channels OUTSIDE the
  Euler+slip scope — exactly the NG-5 viscous channel that phaseD declares invisible to every
  monitor. Complementary, not redundant.
- **F-6 (P3) — Phase-gauge invariance + jitter alignment.** All audit statistics and functionals
  must be invariant under a global phase shift; cycles must be phase-aligned BEFORE averaging or
  wave jitter masquerades as amplitude uncertainty O(jitter × slope) at shocks — [DATA] Claim
  2.5(N4)/7.5(i). Unpinned of record; directly relevant to any future rig/CFD ingestion.
- **F-7 (P3) — Character map χ as datum component with UNKNOWN band** ([DATA] Claim 4.3: near-sonic
  points within k_c·U(M_n) classified UNKNOWN, forced to the conservative subsonic branch).
  Mostly mooted by the L4 default; load-bearing the day the declared subsonic case-class is used.
- **F-8 (P3) — Cheap a-priori quasi-steady admissibility number.** [PDE] C3.6: the per-phase
  (R3/I2) defect has a DETONATION-SPEED-ORDER coefficient — bound (3.3),
  delta_qs = (|u_theta − Omega r| + a)_max TV_alpha(datum) / (r_i ||∂_x F_x||); [DATA] Claim 3.2:
  He ~ O(1) at kHz — "CHECK, don't assume". [REC] carries the loss a posteriori (St|J1| bar,
  [J-CT1], T3QS) but has no a-priori datum-computable admission number for rung I2. Instrument
  gap, not theory gap.
- **F-9 (P3) — Wave-asymmetry demotion rule.** If the Z_m identical-waves residual fails, the
  datum demotes to m′ = 1 with the LONG period; silent use of the short period rejects the
  pipeline ([PDE] A9, [DATA] A6(iv)). Unpinned of record (scope pin fixes n but not the demotion
  protocol).
- **F-10 (P3) — Wall-corner trace compatibility audit** ([PDE] A10): datum corner traces vs
  downstream wall condition to the order demanded by the solution class. NG-3-adjacent (phaseD);
  absent as a datum audit.

### (iii) MISSED BY THE BLIND DERIVATIONS — record depth vs brief underdetermination (6 items)

- **M-1 (record depth)** — Fallback objective targets J_exact^± (liminf/limsup, ALWAYS defined) +
  the certified geometry-free upper wall [S-GBE], + the SRB/physical-measure wording discipline
  (D2.2 S14 additions). Both blinds treat stationarity failure as reject-only; the record
  SURVIVES it with certified brackets. The brief did ask how the periodic hypothesis is handled —
  the blinds under-delivered here: depth, not underdetermination.
- **M-2 (record depth)** — Solution-concept ladder D2.5: BVP-native weak-strong uniqueness
  transfer [T-XWS] (x-as-time relative entropy, sonic bijection, wall flux annihilation),
  C-MAJDA sharpened to the single Lopatinskii scalar U3-H1, a-contraction route [S-ACFR]. The
  blinds flag uniqueness as "open (H4-H5)" / "assumed"; the record has partial THEOREMS.
- **M-3 (record depth)** — Exact mdot-independence on L4 ([T-TH0]) and causality at THEOREM grade
  ([T-NSW]; now phaseD Thm 1/1′): blind counterparts are [SKETCH]/[PS].
- **M-4 (brief underdetermination)** — Everything design-problem-side: admissible set A_gen
  (cone condition, Chenais, attachment pins, sector census), side-load disposition [T-SLRW],
  separation constraint [D-GSEP], averaged adjoint system T7 + weighted transversality,
  globality mechanism (S*, delta). The brief posed only the datum; no blind fault.
- **M-5 (record depth)** — Measure-discipline wording: mu-a.e. readings (ME-4), proxy note
  (PP-4), bar-class note (PP-5) — audit-hardened quantifiers the blinds do not reach.
- **M-6 (record depth)** — Mode transitions ROUTED (robust layer A6/PB-5, CVaR upgrade path)
  rather than only voided ([DATA] B3 "no correction possible" is the coarser verdict).

### (iv) GENUINE DISAGREEMENTS — agenda items (5)

- **D-1 — Mixed/phase-crossing characteristic signature.** [PDE] (P3): signature must be CONSTANT
  in phase and position; mixed signature is INADMISSIBLE outright (sonic set = free boundary of
  the prescription problem). [REC]: subsonic patches are a declared case-class with monitors;
  H3-cl expected to FAIL on migrating patterns (K-P Fig. 6) but the class stays admissible.
  AGENDA: pin whether a phase-migrating sonic line voids the contract (blind-PDE reading) or
  merely downgrades the Verdict (record reading). Feeds F-7.
- **D-2 — Placement as a band.** [DATA]: prefer the most UPSTREAM station with β = 0
  (transportability); [PDE]: admissible band [z_I^-, z_I^+], possibly empty, with DOWNSTREAM
  preference for the phase-family reduction. The two blinds disagree with each other; the record
  fixes Gamma_d without recording the trade. AGENDA: a placement-band remark in D2.4 (or a
  choice-ledger row) naming the two monotone pressures and the emptiness verdict.
- **D-3 — Datum-space metric.** [PDE] C7.1: L^1(A) (TV-metrics ruled out — jump positions never
  measured to TV accuracy; weaker-than-L^1 ruled out by flux continuity); [DATA] U-a:
  thrust-calibrated flux-weighted L^2 + separate L^∞ realizability guard. Genuine two-lens
  disagreement, record silent. AGENDA: choice-adjudication row (per
  `choice-adjudication-convergence`) — candidates: L^1, weighted-L^2 + L^∞ guard, or both
  (acceptance metric vs sensitivity metric).
- **D-4 — Normative status of the mean state I4.** [DATA] Claim 3.4 BANS the mean-datum solve as
  a reduction; [REC] keeps I4 as a ladder rung. Compatible only if I4 carries the O(Var)
  no-small-parameter warning at the site of definition. AGENDA: one-line I4 annotation in D2.4.
- **D-5 — Wave-frame azimuthal MARCHING.** [PDE] C3.2 proves the wave-frame problem is
  symmetrizable-hyperbolic in alpha (|u_theta − Omega r| > a in regime): the periodic orbit could
  be MARCHED in azimuth. [REC] M0 line 549 pins rung-3a as an IMPLICIT BVP (freezing +
  Newton-Krylov). A genuine algorithmic alternative surfaced blind. AGENDA: choice-ledger
  confrontation row (implicit BVP vs azimuthal march), adjudication owed at rung-3a
  implementation time, not before.

**Diff counts**: (i) 9 re-derived; (ii) 10 demanded-missing (3×P2, 7×P3); (iii) 6 missed
(4 record-depth, 1 underdetermination, 1 mixed); (iv) 5 agenda items.

---

## PART B — PROOF VERDICT: `phaseD_L4_implies_R1.md` (r2)

### B.1 Loop accounting

Two adversarial rounds × two lenses (hyperbolic-systems rigor; gas-dynamics physics). Round 1:
12 major objections + N-list + panel items — ALL consumed by r1 (each repair anchored). Round 2:
l0 found R2-O1..O9 + 5 minors; l1 found R2-1..R2-5 (dedup-declared); both lens verdicts
REPAIRABLE, "no core statement broken", with substantial Part-A/B verification records (the
central computations re-derived by hand by BOTH refuters and CONFIRMED: 3b(i) localization,
3b(ii) sharpening, crossing identity + gamma-const anchor 4.5 < 5.6, (BQ)/Lemma 1.2, pencil
diagonalizability, no-resonance step, Corollary 4 rebuild, quadrant (d) witness, Gruneisen
one-liner, meridional discriminant). r2 revision consumed ALL round-2 objections. Loop CAPPED at
round 2, NOT-DRY. **Consequence of record**: proofs attacked in rounds 1-2 carry dual
adversarial verification; proofs NEW IN r2 (Theorem 1′, Proposition 1″, Lemma 1.4, Lemma 3.2,
Corollary 4 row-(a) in-class restatement, (ii′) measurable-field restatement, Lopatinskii
display) carry ZERO adversarial coverage. Blind-slot failures: 0.

### B.2 Judge verification acts (this document)

The judge read the r2 file in full and re-checked, at derivation level: Lemma 1.4's shrinking-
frustum positivity (lambda_max S + S A(nu) ≥ 0 from spec A(nu) ⊂ [−lambda_max, lambda_max] via
the Lemma 1.2 similarity — sound); Theorem 1′ (verbatim instantiation of the twice-audited
Theorem 1 energy argument on C_h — sound); Proposition 1″ bootstrap (t* maximality argument —
sound MODULO (H-UP), as labeled); Lemma 3.2 monotone-intersection (sound given the cited
monotone wave-curve parametrization; scope restriction is load-bearing and correctly declared);
Corollary 4 row (a) in-class transport construction (sound); (ii′) good-sign boundary term
(sound). No new defect found. This is a single-reader check, NOT an adversarial round: it
informs but does not discharge the audit debt below.

### B.3 Final rigor classes (downgrade-only; binding)

| Statement | r2 label | FINAL (judge) | Notes |
|---|---|---|---|
| Lemma 0.1, 0.2 | THEOREM | **THEOREM** | dual-audited |
| Theorem 1 (C^1 core) | THEOREM | **THEOREM** | device-class consumption ONLY via 1′ (vacuous otherwise — R2-O2, accepted) |
| Theorem 1, H^1 extension | THEOREM* | **THEOREM\*** (Rauch 1985) + NG-3 | corners open |
| Theorem 1′ (collar) | THEOREM | **THEOREM** — AUDIT-DEBT-r2 | r2-new; verbatim instantiation |
| Lemma 1.4 (finite speed) | THEOREM | **THEOREM** — AUDIT-DEBT-r2 | r2-new |
| Proposition 1″ | THEOREM modulo (H-UP) | **DOWNGRADE (J-1)**: device-class effective label **SCHEMA-conditional** (NG-9) | the modulo-form stands as literal text; any full-Omega_up device-class R1 quote is SCHEMA until NG-9 discharges |
| Remark 1.5.5 (ii′) | THEOREM | **THEOREM** — AUDIT-DEBT-r2 | characteristic-inflow scoping stands |
| Lemma 2.1, 2.2, Remark 2.4 | THEOREM | **THEOREM** | dual-audited incl. pencil + no-resonance |
| Theorem 2(a)(b) | THEOREM | **THEOREM, conditional on (M-a′)** | (H2.2) volume/axial certificate — never claimable off the segment certificate |
| Theorem 2(c) | SCHEMA | **SCHEMA** | |
| Remark 2.3 (nonlinear per-phase) | SCHEMA | **SCHEMA** (NG-1) | |
| Theorem 3a | THEOREM | **THEOREM** | upstream-facing family qualifier load-bearing |
| Theorem 3b(i),(ii) | THEOREM | **THEOREM** (in-box band) | dual-audited centerpiece |
| Theorem 3b(iii) | THEOREM* | **THEOREM\*** (G4 + MP §V) in-box; **(G2′) forms PRACTICE** | band-collapse convention stands |
| Theorem 3c (unstart class) | THEOREM* in-box | **THEOREM\*** in-box; PRACTICE beyond | NG-11 deliberately unconsumed — phrasing guard binding |
| Lemma 3.1 | THEOREM | **THEOREM** | dual-audited |
| Lemma 3.2 | THEOREM* | **THEOREM\*** — AUDIT-DEBT-r2 | scope = uniform pure-pressurization ONLY; NG-10 legs open |
| 3.4(3) monitor-scope claims | THEOREM / PRACTICE mix | **as labeled**, plus **J-4** below | (M-b) surrogate, breach-locality, (M-c), (H-RW) = PRACTICE, correctly |
| Corollary 4 (all quadrants, 1-D class) | THEOREM | **THEOREM** (in-class) — row (a) restatement AUDIT-DEBT-r2 | multi-D row-(a) remark **THEOREM\*** + NG-3; multi-D impedance NG-4 |
| Section 5 composite | (composite) | **DOWNGRADE (J-2): CONDITIONAL COMPOSITE — no unitary THEOREM label** | quotable form below |

**Binding quotable form of the composite (the reduced label, of record):**
> Split-certificate L4 ⇒ R1: (i) linearized causal separation on the monitored COLLAR of
> Gamma_d — THEOREM (Thm 1′), modulo the PRACTICE bridges (H-RW) and (M-c); full-domain
> device-class form SCHEMA-conditional (NG-9); (ii) steady per-phase causal separation —
> THEOREM, conditional on the SEGMENT certificate (M-a′); (iii) finite-amplitude protection
> boundary priced for PLANAR NORMAL UPSTREAM-FACING fronts only (Pi* threshold, in-box;
> oblique = NG-2, surrogate legs = NG-10), Euler+slip scope only (viscous channel NG-5).
> "L4 ⇒ R1" WITHOUT these qualifiers is not a statement of record.

**Judge downgrade/flag register:**
- **J-1** — Proposition 1″ device-class effective label = SCHEMA-conditional (NG-9).
- **J-2** — Section 5 composite denied a unitary THEOREM label: CONDITIONAL COMPOSITE (per-clause
  labels above are the only quotable ones).
- **J-3 (AUDIT-DEBT-r2)** — flag on every r2-new proof (Thm 1′, Lemma 1.4, Prop 1″ bootstrap,
  Lemma 3.2, Cor 4 row-(a), (ii′), Lopatinskii display): labels RETAINED (judge-checked, B.2) but
  M0 promotion of these specific labels is GATED on one targeted adversarial pass over the
  r2-delta set (the loop capped NOT-DRY; these repairs have zero adversarial coverage). Owner:
  next refutation window (F2-adjacent).
- **J-4 (monitors: SPECIFIED, not ARMED)** — the Section 6 falsifier battery is named with
  derived pass/fail predicates but NOT EXECUTED (no run artifacts in the raws bundle for the
  L4R1 harnesses; search of directory listing). Per R5, every "monitored"/"armed" claim about
  (M-a)/(M-a′)/(M-b)/(M-c) must read "monitor-SPECIFIED"; arming = implementing + running the
  harnesses in the pinned env (numpy only, no installs), with the rejector-of-the-rejector legs
  (subsonic control, broken-marcher check, band-collapse branch) mandatory.

**Named-gaps register NG-1..NG-11**: RATIFIED as written (owners + triggers verified present;
none is a silent postponement; NG-8 is the single retro-propagation item and is BLOCKING — see
C-1). NG-11's phrasing guard ("AN admissible solution breaches", never "THE") is binding.

### B.4 Ready-to-land verdict

**READY-TO-LAND: YES, WITH CONDITIONS** (land = this file + `phaseD_L4_implies_R1.md` as
of-record in `validation/`, ADVISORY_INDEX row + registry rows in the same window per R7/SR-1/2).

- **C-1 (BLOCKING for consumption, not for landing)** — NG-8 retro-propagation to M0
  [D-CONTRACT] L4-DEFAULT: the block must be restated as the SPLIT certificate ((M-a)
  normal-on-surface; (M-a′) axial-on-segment + box membership), or planarity + segment pins
  added. Until the M0 edit window: every certificate check on a non-planar patch uses the
  NORMAL direction; every Theorem-2/3 consumption cites (M-a′) explicitly. Owed under R4 —
  "not optional" (document's own words, ratified).
- **C-2** — AUDIT-DEBT-r2 (J-3): targeted adversarial pass on the r2-delta set before any M0
  promotion of those labels.
- **C-3** — Falsifier harness implementation + execution (J-4) before any "armed monitor" claim;
  results filed as carrier rows.
- **C-4** — Part A finding candidates F-1, F-2, F-3 (P2) to the findings registry with owners
  this window; F-4..F-10 (P3) as registry rows or a named queue entry; D-1..D-5 to the agenda /
  choice ledger (D-3 and D-5 as adjudication rows).

**Session-loop bookkeeping**: refute loop NOT-DRY at cap ⇒ the reduced composite label (J-2) IS
the final label; blind-slot failures 0/0; nothing dropped silently — every residue is a named
gap (NG-1..11), a judge flag (J-1..4), or a landing condition (C-1..4).

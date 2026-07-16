# SESSION LOG — 2026-07-16, Sessione 4: "Fase 1: P-1 skeleton + P-2 Lemma A (+ G0 spike)"

Append-only, total-order log (CLAUDE.md R3 + standing user directive).
One numbered row per step, per generated/modified .md, per codebase
action. Rows are ONLY appended at the end, never inserted.

Branch: `rde-nozzle-program`. HEAD at open: e23bb08.
Untracked at open (expected, untouched): GENO/, scratch_out.txt,
scratch_err.txt, validation/ADR_panel_2026-07-16.md (AWAITING USER
RATIFICATION — no implementation).

---

1. [R2 apertura] Verified branch `rde-nozzle-program` (git branch
   --show-current), HEAD e23bb08, tree clean except expected untracked.
   No other session active on this tree (single-session discipline per
   PROGRESS S2 note).
2. [R2 apertura] Read project memory (research-cycle-averaged-rao,
   gate-pre-esecuzione): state = S3 closed, Fase 1, NEXT = P-1
   skeleton / P-2 Lemma A / G0 spike; standing pre-execution gate
   directive active.
3. [R2 apertura] Read M0 (docs/rde_nozzle_MASTER.md) in full, with
   focus of record: D2.6 (problem (P) = pair (S*, delta), certified
   globality (iv), maximality rationale), Prop. 7 (G-B sonic-cap
   sharpening + OP-11-eps instance + SCOPE non-transfer remark:
   winners rank CLOSURES, premium_bound = tournament device), T7 (**')
   weighted transversality, Part III EAP + S-H bridge remarks.
4. [R2 apertura] Read PROGRESS (docs/rde_nozzle_PROGRESS.md): ORA = S3
   closed at e23bb08 (OP-11-eps DONE 1438b1b, P-2 outline 05001a5, G5
   text e23bb08); NEXT 1-3 = exactly this session's T1-T3; BLOCCATO =
   G5 dispatch, P-2 venue, ADR ratification, G0 decision at Fase 2,
   RaoPlug S1/S2. DECLARED RESTART POINT: Fase 1 (piano D6), tasks
   [F1/P-1], [F1/P-2], [F2-prep/G0].
5. [R2 apertura] Depth reads for the gate: D3 §10quater (Prop. G-B
   sharpened, OP-11-eps statements (1)-(5), non-transfer scope (5)),
   D6 §3 (publication stream: P-1 JPP after M1, P-2 time-sensitive,
   G5 gates all submissions), D2 §b0 (equation-numbered corpus: Rao
   1958 Eqs [1]-[15] page-verified vs RAO.pdf; Hoffman 1967 fields
   lambda1..lambda5 + E (Eq. 78), p. 676 corner death; constraint-pair
   equivalence; Sternin boundary function), P-2 outline of record
   (docs/rde_nozzle_P2_outline.md, esp. §4 skeleton and §5 O3 plan).
6. [R2 apertura] Verified artifacts of record exist on disk:
   figs/phase_diagram_op11.png, data/phase_diagram.{json,md},
   src/thrust/{bounds,phase_diagram}.py, tests/test_bounds.py,
   tests/test_phase_diagram.py (carriers for the P-1 claim map).

7. [GATE PRE-ESECUZIONE] (A) Plan adherence:
   - T1 [F1/P-1 skeleton] -> D6 Fase 1 ("quasi-1D foundations ...
     paper P-1") + D6 §3 stream P-1 (venue JPP; submission gated by
     M1 + G5, WRITING is not) + PROGRESS NEXT 1. PLACED.
   - T2 [F1/P-2 Lemma A] -> D6 §3 stream P-2 (TIME-SENSITIVE, RK-A) +
     P-2 outline §4 (paper §3 = Lemma A identification) + PROGRESS
     NEXT 2. PLACED.
   - T3 [F2-prep/G0 spike] -> D6 90-day plan item 2 (JAX unit-process
     spike instructing gate G0 decision at Fase 2) + PROGRESS NEXT 3.
     PLACED (optional, time permitting).
   (B) Upstream rigor audit (points the tasks rest on, re-read):
   - Sonic-capped ceiling in subcritical: PRESENT and consistent in
     M0 Prop. 7 (sharpening of record) and D3 §10quater (Prop. G-B
     sharpened; naive form test-rejected on 4 subcritical rows).
     Any P-1 text must carry the cap or the "min-cycle NPR >=
     critical" hypothesis explicitly.
   - Weighted transversality (**'): M0 T7(c) states the naive average
     is WRONG outside the T3 class; P-1 skeleton must state (**')
     as the implementable form (falsifier = wrong-averaging rejector
     in tests/test_bell_optimality.py).
   - Non-transfer scope D3 §10quater(5) + M0 Prop. 7 SCOPE: winners
     rank CLOSURES at equal eps_max, NEVER hardware sectors of (P);
     premium_bound = certified tournament device; bell-winning regions
     of (P) EXPECTED at contour level. P-1 skeleton section on the
     phase diagram MUST use exactly this semantics (grep gate at T1
     acceptance).
   - D2.6 canonical (P): optimum = PAIR (S*, delta) at declared
     constraint vector; P-1 must not state any unconditional-global
     claim outside M1/M2/M3 mechanisms.
   - No discrepancy found between M0 and D3/D2/D6 on these points at
     this read (consistency spot-checks: cap wording M0 Prop.7 ==
     D3 §10quater sharpening; (**') wording M0 T7 == D2 §b0 doctrinal
     point; premium_bound wording M0 == D3 (5) == PROGRESS). No R4
     back-propagation needed BEFORE the tasks.
   (C) VERDICT: **gate pre-esecuzione PASS** (references: M0 D2.6,
   M0 Prop. 7 + SCOPE, M0 T7(c); D3 §10quater(1)-(5); D2 §b0; D6 §3 +
   90-day item 2; PROGRESS NEXT 1-3). Tasks T1, T2, T3 cleared for
   execution in this order.

8. [T1 prep] Verified executable-carrier names for the claim map:
   tests/run_all.py groups (i)-(x) (read in full; group labels of
   record), data/phase_diagram.md (winner table + SCOPE block + knee
   table + subcritical strip PR in {49.2126, 64, 90} + vacuum sweep
   numbers), premium_bound max 64.7 s at (PR=90, eps_max=1) per
   PROGRESS/M0.
9. [T1 EXEC] WROTE docs/rde_nozzle_P1_skeleton.md — P-1 paper skeleton
   of record (venue JPP; submission gated M1+G5, declared in header):
   §0 metadata + negative-claims list; §1 intro with QUERY-BOUNDED
   novelty (C26); §2 Theorem 0 + O1/O2 + interface contract; §3 T0
   strengthened + N-SW + N6 negative scope; §4 collapse dichotomy
   (T3 proof, altitude duality, gamma_eff sharpness numbers of record,
   T4 THEOREM* with K-E closure citation); §5 T7/(**') with boxed
   naive-average warning + quasi-1D reduction; §6 G-B + SONIC CAP
   sharpening + OP-0 ladder; §7 phase diagram OP-11-eps with SEMANTICS
   FIRST (D3 §10quater(5) scope opens the section; (P) = D2.6 pair
   form in §7.0; premium_bound = tournament device §7.6; figure
   figs/phase_diagram_op11.png); §8 EAP + S-H bridges (quantitative
   3-5%/6-14% check, phi placement); §9 declared limits (OP-11
   CONJECTURE, P3/G12, D7 B1/B2 biases); appendices incl. A7
   reproducibility; §CM CLAIM MAP C1-C26, each claim -> class +
   falsifier + executable carrier (run_all groups (i)-(x) + data of
   record). Zero orphan claims by construction (map = acceptance
   checklist).
10. [T1 ACCEPT] Coherence grep on the skeleton (pattern:
    winner|hardware|dominan/dominat|optimal/best nozzle|plug is/wins):
    ALL hits are inside closure-semantics or scope-negation sentences
    (lines 22-28 header discipline, §7.1/7.6 scope, C17 "CLOSURE
    ranking only"); NO sentence reads a winner as a hardware verdict.
    VERDICT: T1 acceptance PASS (class+falsifier+carrier per section;
    zero orphans; grep clean).

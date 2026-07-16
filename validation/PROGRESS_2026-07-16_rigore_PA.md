# SESSION LOG — 2026-07-16, Sessione 6 (DEDICATA RIGORE): "attacco ai
# punti scoperti — P-A1, P-A2, P3"

Append-only, total-order log (CLAUDE.md R3). One numbered row per
step. Branch `rde-nozzle-program`, HEAD at open: aaf8b25. Same
conversation as S5 (user: "attaccalo in questa sessione"); R2 reads
(memoria, M0, PROGRESS, Lemma-A draft, P-2 outline) are in-context
from S5 and re-declared here.

1. [R2 apertura] Restart point declared: S5 closed at aaf8b25; this
   session = Sessione 6 dedicata rigore, tasks [F1/P-2] P-A1 + P-A2,
   [F1/P3], optional [F1/OP-11-molteplicita] + Lemma-B mesh-limit.
   The previously drafted "S6" task list becomes Sessione 7.
2. [R2 apertura] PROGRESS NEXT extension DECLARED (plan placement per
   gate A): new NEXT entries to be added at close — P-A1/P-A2 serve
   the P-2 rigor upgrades (D6 §3 stream, TIME-SENSITIVE), P3 serves
   T7 rigor (P-1/P-4 stream). All fit Fase 1 (quasi-1D foundations /
   theory consolidation); no orphan step.
3. [R2 apertura] Environment: sympy 1.14.0 available (no install
   needed); Hoffman 1967 PDF in-house = GENO/literature/
   hoffman-2012-...-chemically-reacting-gas-flows.pdf (AIAA electronic
   re-issue of AIAA J 5(4):670-676, 1967). GENO read-only.

4. [GATE PRE-ESECUZIONE] (A) Plan adherence: T1 (P-A1) -> Lemma A
   §3.6 PENDING register + D6 §3 P-2; T2 (P-A2) -> same; T3 (P3) ->
   D3 §9 P3 entry + M0 T7 named gap; T4/T5 optional per prompt. All
   placed (with the NEXT extension of step 2). (B) Upstream rigor:
   re-read of Lemma A §3.4 in-context — the (i) justification uses a
   dimension-counting argument on admissible trace variations; this
   is the very object T1 attacks: any discrepancy found will be
   treated as DISCOVERY with R4 refinement of the draft (not silent
   patching). Gamma question: T1 symbolic work will be run in
   primitive variables with c^2 symbolic (EOS-general form) AND
   perfect-gas instantiation as cross-check; T2 (Hoffman) is the
   reacting-gas bank (frozen-gamma boundary NOT load-bearing); T3 is
   measure-theoretic (gamma-free). Scope §10quater(5) untouched by
   all tasks. (C) VERDICT: **gate pre-esecuzione PASS** (refs: Lemma A
   draft §3.4/§3.6; D3 §8/§9; D6 §3; M0 T7/D2.6).

5. [T1 EXEC] WROTE validation/pa1_symbolic_lemmaA.py: Part 1 = sympy
   machine verification of the ENTIRE §3.2 classical derivation under
   EOS-general closure rules (dp/dW = -rho W, drho/dW = -rho W/c^2,
   c = W/M symbolic): (L.6), (L.7), (L.10) factorization, (L.12) C+
   and C- families, (L.13), (L.15) corner == CSTR_PA, (L.16) mirror
   == CSTR_PB, + rejector R1 (sign-corrupted corner must fail).
   Part 2 = KERNEL SOLVABILITY LEMMA, EOS-general (c free symbol):
   eigvec check + both flux-covector contractions + rejector R2
   (family specificity) + the exploratory kernel-ratio identity.
6. [T1 DEBUG — declared] First run: 2 FAILs, BOTH script
   normalization bugs, zero math errors: (a) target of (L.10) carried
   a spurious 1/M^2 (the machine lhs equals the hand result exactly;
   bonus identity of record: (M^2-1)sin^2 psi - cos^2 psi ==
   M^2 sin^2 psi - 1); (b) |n| = 1 constraint not substituted in the
   <grad g, r-> check (residual was c rho u (nx^2+ny^2-1), i.e. zero
   under the constraint). Fixed both; re-run.
7. [T1 VERDICT] PASS 14/14 (8 derivation identities + eigvec + 2
   contractions + ratio identity + rejectors R1/R2 both PASS).
8. [T1 DISCOVERY + R4] Prop. A2 (kernel solvability) shows the first
   draft's dimension-count justification of identification (i) was
   TOO LOOSE: on a characteristic surface the adjoint b.c. (L.22) is
   solvable for EVERY lambda2 (both flux covectors annihilate the
   tangent-family kernel identically); moreover the pointwise kernel
   ratio does NOT reproduce f2 (computed: W cos(al) cos(th+al)).
   Hence the invariant does NOT live in the pointwise boundary
   algebra: the adjoint reading of Rao's conditions is the
   TANGENT-FAMILY TRANSPORT along Sigma. R4 SAME SESSION: draft
   §3.3 (new Prop. A2 with carrier), §3.4(i) rewritten (refined
   route), §3.4(ii) precision paragraph, §3.6 register rows updated,
   PENDING P-A1 NARROWED to P-A1' (derive the adjoint transport
   relation and exhibit f2 as its first integral); D3 §8 upgraded
   with the rigor-session paragraph. HONEST STATUS: P-A1 partially
   discharged (solvability half = THEOREM machine-verified; transport
   half = P-A1', precisely stated, open). Classes (i)-(iii) stay
   THEOREM* with the refined route — no overclaim.

9. [T1 COMMIT] 5ec62ef "[F1/P-2] (rigore-T1): P-A1 attack - machine
   verification + kernel solvability lemma, P-A1 narrowed".
10. [T2 EXEC] Hoffman 1967 FULL page-level read: PDF renderer absent
    (no poppler) -> text extraction via pypdf 6.14.2 (already present,
    no install) to UTF-8 file, read in full (7 pages, pp. 670-676).
    Page-verified facts of record: fields h_1..h_4 (one per flow PDE,
    Eq. 17) + g_i species (Eq. 15) + constants C_1 (isoperimetric,
    Eq. 12) and C_2 (streamline multiplier; h_1 = C_2 on AC, Eq. 29);
    interior multiplier PDEs Eqs. (35)-(39) with sources (42)-(44)/
    (55)-(57); hyperbolic (8+2n) system, characteristics = streamlines
    + Mach lines; multiplier compatibility Eqs. (49)-(51) (streamline)
    and (54) (Mach lines); terminal-characteristic data Eqs. (31),
    (33), (34) (g_i = 0 on BC); the FIFTH relation Eq. (32) NOT
    imposed (p. 673: five would OVERSPECIFY unless BC is a
    left-running Mach line — the control surface is selected by b.c.
    counting); endpoint/wall data Eqs. (60)-(65), constant-length
    case Eq. (68); E = y h_1 - (u y' - v) h_3 (Eq. 78 == unused
    Eq. 32) as the a-posteriori optimality check (p. 676).
11. [T2 DISCOVERY + R4] (a) SYMBOL CORRECTION of record: program docs
    paraphrased "lambda1..lambda4 (+lambda5)" — corrected to
    Hoffman's real notation in the draft §3.4(iv) and D3 §8.
    (b) Hoffman p. 673 = the 1967 ANCESTOR of Prop. A2 (surface
    selected by boundary-condition counting): recorded in the map.
    (c) Eq. (54) = the published adjoint transport relation along
    Mach lines -> NEW ROUTE OF RECORD for P-A1' (specialize to frozen
    homentropic, integrate to f2). Draft §3.4(iv) UPGRADED SCHEMA ->
    THEOREM* with the full component-map table (every row
    equation-numbered post-read); P-A2 marked DISCHARGED in the
    PENDING register (numeric half remains in P-A3/O3.2).

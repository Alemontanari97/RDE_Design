# PRIMARY-SOURCE VERIFICATION PASS (Fable, 2026-08-13) — paper-by-paper, vs the FULL corpus of the method

PURPOSE. User-mandated re-verification of the confrontation: the Opus-era reports/verdict
(`ADVISORY_litreview_confrontation_2026-08-13.md`) are treated as an UNRATIFIED QUARRY; every
load-bearing claim is re-checked by direct reading of the PDF **and** of the corresponding point in
the program's own record (M0 lines, docs, code), never against the apparatus brief.
STATUS: stages 0-1 complete; stages 2-5 in progress. Each stage lands here IMMEDIATELY.

VERDICT CALIBRATION SO FAR on the Opus layer: in every spot-check to date, the per-paper READER
reports were accurate; the demonstrated errors lived in DOWNSTREAM summaries (INDEX rows, orchestrator
paraphrases): Liu 2022 "GA+gradient" (false, C4), Paxson-Miki "optimization" framing (C25),
"maximum-average-thrust" descriptor for ISABE (demoted to unverified inference, R1).

---
## STAGE 0 — papers personally read in-session BEFORE this pass (evidence in conversation of record)

| Paper | My coverage | Verified outcome (vs our corpus) |
|---|---|---|
| Humphreys-Thompson-Hoffmann, AIAA J 9(8):1581-1587 (1971) | full | Relaxation = KKT one-shot with surrogate diagonal Jacobian (Eqs. 31-35); E (Eq. 30) = optimality residual on exit characteristic DB, NOT a wall gradient; multipliers = adjoint fields (Eqs. 13-16 same characteristics). Fixed-inlet = our attachment data; general isoperimetric = our constraint bookkeeping. |
| Hoffman, AIAA J 5(4):670-676 (1967) | pp.670-676 | Multiplier-field formulation for reacting flow; E-residual Eq. (78); anti-overspecification argument for Mach-line control surface. Route B pattern of record confirmed. |
| Rao & Beck, AIAA 94-3264 (1994) | full (5pp) | DEF = isentropic jumps ON the control surface to re-enter the valid region bounded by Eq. (4) ≡ our Λ-form/val=0 (S4, proven equivalence `boundary_equivalence_derivation.md`); shocks (if any) downstream of design region; 22% length cut for 0.3% thrust; DEF ∈ our variational family (flagdef). |
| Hoffman, JPP 3(2):150-156 (1987) | full (7pp) | CTP = geometric recipe (truncate + linear compression + Δx_s shift), internal oblique shock is a SIDE-EFFECT; Gogish's shock-benefit premise measured and refuted ("not beneficial… contrary to the principle", p.154); Rao wins all cases by 0.04-0.34% (grid maxima; "limited scope" rider). Concept from Gogish 1966; Rao-Beck (1994) does NOT cite it. Feeds claim 19 external scale (D-11) + CTP admissibility seed (A8, REQ-NONSTALL). |
| Efremov & Kraiko, Fluid Dyn. 39(4):621-632 (2004) | full (12pp) | AUTHORS CORRECTED (not Kraiko-Tillyaeva; file re-key duty C7 stands). Ideal jet thrust augmentor: variational max of PERIOD-AVERAGED thrust R (Eq. 1.7), unknowns = time-functions of exit state F,V,p,s per stream + scalars W,Q; 4 isoperimetric conditions, constant multipliers. Necessary conditions ⇒ p_e=p_a (2.6-2.7), equal exit velocities (2.9), s_e=s_i (2.11) ⇒ optimum collapses to STATIONARY, authors name the cause: preassigned flow rates (Summary p.631) + "fixed metalwork" failure condition. NO wall contour, NO flow PDE field, exit sections uniform by assumption. Kills the phrase "first variational period-averaged thrust problem"; does NOT touch PB-2 (no shape, endogenous time measure, collapsing). Confirms refs [20]=Bogdanov 2002, [21]=ISABE-2003-117 with exact titles. Monito for T-T3: their collapse is constraint-induced — our fixed per-phase mass flow analog must be tested (does T-T3 collapse survive constraint-set changes?). |
| Paxson, Miki, Perkins & Yungster, AIAA 2022-4107 | pp.1-5 of 12 | Cycle-averaged thrust is the METRIC (limit cycle: "cycle averaged thrust remained constant", mass in=out); METHOD is a 2-parameter OFAT sweep (7 designs), no optimizer, no functional varied over a contour. Q2D annulus (CPG, detonation frame) → unsteady periodic BC → 3D frozen RANS. "58.1%→70.0% of notional ideal". C25 framing corrections co-signed. |

## STAGE 1 — Kraiko & Tillyaeva, J. Math. Sci. 208(2):181-198 (2015) — VERIFIED BY ME (pp.181-189 + 195-198; skipped 190-194 = Tricomi eigenfunction numerics)

**What the paper does (my read).** Laval nozzle max thrust INCLUDING the subsonic part (given total
length X, mass flow, stagnation params, p⁺ on possible end face); candidate subsonic contour =
abrupt contraction; question = is it a region of boundary extremum. Conjugate (adjoint) problem for
λ₁,λ₂ over the whole domain, solved BACKWARD from exit; hodograph (3.1)-(3.3): λ₂ satisfies a
2nd-order eq., ELLIPTIC subsonic / HYPERBOLIC supersonic, λ₂V=0 on sonic line ⇒ generalized TRICOMI
problem, eigenfunction solution, Dirichlet solve grid-checked (Fig. 8, 3 grids). Summary p.197: the
design question is LEFT OPEN ("In future … it will become possible to clarify whether an abrupt
contraction is a region of end extremum").

**Chain verified equation-by-equation** (all page-checked by me):
- (2.2) p.184 adjoint field eqs R^u=R^v=0; characteristics coincide with flow C± for V>a.
- (2.3) compatibility (y^{ν−1}ρ cotanμ)dλ₁ ± dλ₂ = 0 — IS Hoffman 1967 Eq. (15) in other variables,
  48 years later, WITHOUT citing Hoffman (nor Rao: first integrals presented as "control contour
  method [2]" with no attribution).
- (2.5)-(2.6) discontinuous multipliers ONLY on C± characteristics; [λ₂]=±[λ₁]y^{ν−1}ρcotanμ
  =±C√(y^{ν−1}ρcotanμ); cause: solvability for ANY contour, convex bends/fans (p.182).
- (2.7) wall BC λ₀=λ₁, λ₂=−y^{ν−1}ρv; exit section λ₁=λ₂=0.
- (2.9) Δχ = endpoint terms + ∫ B^x δx dy, B^x = y^{ν−1}ρv(u−λ₁)′ — **a literal first variation
  w.r.t. contour displacement ⇒ B^x IS the shape-gradient (Hadamard) density on the wall.**
- (2.10) optimality: B^x=0 ⟺ λ₁=u+C on d₊f, **PLUS two INEQUALITIES**
  (p−p⁺−ρuv tanμ)_f ≥ 0, v_f² ≥ 0; "end face ff°, if exists, is a region of boundary extremum".
- (2.13)-(2.14): A^y=0; λ′₀≥0 on ad_, A^x ≤ 0 — more inequality/boundary-extremum conditions;
  §4 (4.17)-(4.18) executable form (λ₂=λ₂,I+λ₂,II with singular part ~η^{1/4}).
- (2.11)-(2.12) closed form λ₁=u+C, λ₂=−y^{ν−1}ρv in triangle hd₊fh (valid AT the optimum only,
  Cauchy data on d₊f) ⇒ Rao's two first integrals on hf; one is a consequence of the other +
  C⁺ compatibility (redundancy note, adoptable).
- References p.198: **8 titles, all Russian school** (Gonor-Kraiko 1969; Kraiko 1979; K-T-Shcherbakov
  1986; Bitsadze; Smirnov; Chernyi 1988; Kraiko 2010; A.A.Kraiko-A.N.Kraiko-P'yankov-Tillyaeva,
  Fluid Dyn. 47(2):223-238 2012). **Zero Jameson/Giles/Pierce/Lions/Pironneau/Lozano; zero Rao,
  zero Hoffman.** The INDEX.md r.47-48 test is EXECUTED by me: NEGATIVE ⇒ P2/G14 bridge stays ours.
- Dating: "Submitted on August 29, 2014"; translated from Probl. Mat. Analiza 80 (April 2015).

**Confrontation vs OUR corpus (points read in M0, not in the brief):**
1. **P2/G14**: bridge survives in the three-legged qualified form (ASO articulation + discrete/
   reverse-AD link + certified-optimizer use). The record gloss "Rao's optimality residual = the
   adjoint gradient" EXISTS in our docs (rde_nozzle_literature_map.md:432,
   rde_nozzle_theorem_ledger.md:410) and is LITERALLY instantiated by (2.9)+(2.10) ⇒ **D-01
   (cancel gloss + rewrite claim 1) CO-SIGNED BY ME on primary sources.** Historical nuance kept:
   HTH-1971 had only the DB residual (needed surrogate ∂E/∂θ); the wall gradient density in print is
   KT2015 — so the 1971 story in our session-opening analysis stands, but the gloss as novelty is dead.
2. **T7(b)** (M0 :1086-1088): our ∫G_ξ dμ + λ_L g_L = 0 with G_ξ = phase Hadamard density is EXACTLY
   the μ-averaged generalization of their B^x=0. Clean containment, verified on equations.
3. **T7(c)** (M0 :1090): written as EQUALITY ∫(dF/ds_E)dμ=0 — VERIFIED. KT2015 writes endpoint
   conditions as INEQUALITIES with boundary-extremum slack precisely when constraints bind, and
   PROVES the length constraint always active (coefficient ρv² tanμ ≥ 0 identically). Our (P) has
   g_i ≤ c_i + active-set driver ⇒ **C31 (cone form D ∈ N_K(s_E*), three declared regimes)
   SUBSTANTIVELY CO-SIGNED.** Still to verify in code: the claim that current carriers are
   sign-blind on λ_e (o33_bench R3/R7) — NOT yet checked by me.
4. **F4b**: jumps only on characteristic surfaces (2.5)-(2.6) ⇒ consistent with the adjudication
   "shock is non-characteristic for the adjoint ⇒ G-P continuity; Kraiko jumps = different object,
   compatible". Third certificate class (A5) formula verified as printed.
5. **Claim 18 non-containment** "design variable in elliptic region ⇒ mixed-type adjoint": REAL,
   seen in (3.1)-(3.3).
6. **A3 oracle preconditions** verified from text: closed form valid only at optimum, only in
   triangle, homentropic-homoenergetic data.

**Errata found BY ME in the Opus verdict** (examples of residual noise, none material):
- R17 evidence date: verdict says "received 1 June 2015"; paper prints "Submitted on August 29,
  2014" (STRENGTHENS the parallel-branches adjudication).
- Litmap/sweep row "Kraiko & Tillyaeva FD 47(2) 2012": authors are FOUR (A.A. Kraiko, A.N. Kraiko,
  P'yankov, Tillyaeva).

**Stage-1 calibration verdict on the Opus layer: READER-ACCURATE.** Every load-bearing citation
checked (2.2, 2.3, 2.5-2.6, 2.7, 2.9, 2.10, 2.11, 2.12, refs, Summary quote) is exact.

---
## REMAINING PROGRAM (stages 2-5, in execution order; each lands here on completion)

- **STAGE 2 (adjoint quality — the session's core question):** Giles-Pierce JFM 426:327-345 (2001)
  vs Lemma B / O3.1 transpose identity / VI.3 certificates / DWR bars + sonic singularity (§3.25
  re-scope); then Ancourt Aerospace 10:797 (2023) vs the fitted-march characteristic structure +
  [X-GENOXC]; then Giles-Pierce 2000 (nomenclature + complex-step A2).
- **STAGE 3 (averaging axis):** Rubino JCP 372 (2018) HB-adjoint duality vs Lemma-B; Zahr-Persson
  periodicity BVP/monodromia vs periodic-wave pin + A20 Floquet-modulo-symmetry corrections;
  Schotthöfer/Krakos window ORDER (A9/A10, estimator side ONLY, C6 discipline); Kaemming-Paxson EAP
  vs M0 remark (already workflow-verified FAITHFUL — spot-check Eq. (1)-(8) + Fig. 11 Jensen instance
  A26 + M-sonic minimality A27).
- **STAGE 4 (RDE axis):** Harroun 2021 CROSS-CHECKED against ADVISORY_rde_choking_2026-08-11 (already
  a full Fable-era read of record — dedup the tranche-2 findings against it; misquote upgrade C26);
  Harroun 2020 (grades: CFD-vs-CFD, psia refuso C11); NASA set (Miki/Teasley×2) = gap statements +
  C19 geometry non-reconstructability; Liu (C4 already established); Ornano C16.
- **STAGE 5 (classical remainder):** Kraiko-Tillyaeva-Baftalovskii JPP 17(6) 2001 (6pp: Busemann
  condition, Sternin 1957 EOS-generality lineage C15/D-07, plug sub-line vs T-T4/E4); Sun 2019
  (C13/C14: R-vs-composition incoherence — NOT a P1 instance); Fernandes (niche verdict + C17
  non-identifiability); Kraiko 2016 (vector thrust non-containment (h); C8 parallel branches);
  Wintenberger-Shepherd (C27: FJ = WORK ceiling upstream of B_EK, cannot falsify shape gains);
  Wolanski (W-number A34; 176-ref witness); JANC (A21/A22 clauses).

## STAGE 2 — Giles & Pierce, JFM 426:327-345 (2001) — READ INTEGRALLY BY ME (19/19 pp, refs included)

**Facts verified with my own eyes:**
- Received 11 June 1998, revised 8 Aug 2000. **26 references: zero nozzle-school classics (no Rao/
  Guderley/Hoffman/Kraiko/Shmyglevskii) and also zero Lions/Pironneau** (adjoint lineage = Jameson
  1988/1995/1999, Reuther, Iollo, Cliff, plus the error-estimation school). Ninth independent
  bibliography with zero crossings — P2/G14 affirmative evidence CONFIRMED.
- §2: RH conditions enforced with an EXTRA multiplier v_s ⇒ **adjoint variables CONTINUOUS at the
  shock** (v(x_s−)=v_s=v(x_s+), p.331), **internal adjoint BC** v₂(x_s)=−(dh/dx(x_s))^{-1} (2.5),
  and **(dv/dx)=0 at the shock** (p.332). Iollo v=0 "over-constrains"; Cliff et al. sign-change =
  coordinate artifact, "misleading" — A4's two rejected readings verified as printed.
- BC counting (p.331-332): n incoming flow characteristics ⇒ (3−n) adjoint BCs; at the shock 3+1
  outgoing adjoint characteristics fixed by 3 continuity + 1 shock BC. **Same anti-overspecification
  counting logic as Hoffman 1967's exit-characteristic argument — two schools, same argument, no
  cross-citation** (new affirmative brick for the "articulation" leg of P2/G14).
- §3: Green's-function construction v^T(ξ)=(I₁|I₂|I₃)(f₁|f₂|f₃)^{-1} (3.2) with source vectors
  ∂F/∂m, ∂F/∂H, ∂F/∂p₀; objective J=∫p dx ("mimics the lift integral") — **NOT thrust** (A1 clause
  verified); duct h(x)=2 / 1+sin²(πx) / 2 (p.341, A1 benchmark verified); **results are PLOTS
  (Figs. 1-4), no tabulated constants** ⇒ A1's "re-derive and double-implement" clause stands.
- §6.1: ∂p/∂m|_{H,p0} = −q/(1−M²), M≈linear through choked throat ⇒ I₁(ξ)~log(ξ): **logarithmic
  singularity at the SONIC THROAT**, reflected in all three adjoint variables (p.342, Fig. 3).
- **Fig. 4 (shocked) verified: the asymptote is at x≈0 (the throat), NOT at the shock (x≈0.2, where
  objectives jump but adjoints are continuous with zero gradient)** ⇒ the G-c re-pricing of A1 is
  CORRECT: the shocked rung inherits the sonic singularity; supersonic case (Fig. 1) is the clean
  negative control (adjoints smooth, zero at exit).
- p.343 (2-D status): adjoint continuity at shock + BC ALONG the shock = "preliminary analysis,
  supported by numerical computations (Giles-Pierce 1997)"; open consistency question for methods
  not enforcing the internal BC; **no sonic-LINE singularity in 2-D if not orthogonal to flow**
  (region-of-influence argument, delegated to GP 1997, NOT on disk — R27 verified); NEW: inverse
  square-root singularity at the incoming stagnation streamline (2-D, unconfirmed by them).

**Confrontation with OUR adjoint construction (the session's core question):**
1. **Our F4b bet sits on the PROVEN side of the controversy.** Differentiating the FITTED front with
   RH enforced is exactly the configuration in which GP2001 proves adjoint continuity (quasi-1D:
   THEOREM-level; 2-D: preliminary+numerical only). Any M0/F4b statement about the 2-D case must
   carry the grade "preliminary analysis + numerical evidence (GP1997/2001)", never "proved".
2. **Honest state of our adjoint fidelity: UNTESTED until A1/A3 are implemented.** O3.1 (transpose
   identity, 2.7e-10) certifies SELF-consistency of the discrete pair; GP2001 is the first available
   independent closed-form fidelity oracle (quasi-1D twin, J=∫p dx, γ=const declared slot). D-08
   scope qualifier co-signed.
3. **The excluded locus of our DWR bars now has a DERIVED reason**: our per-phase march starts at
   the Sauer IVL (near-sonic boundary) — the log-weight region sits exactly there; the o32 exclusion
   norms (IVL/lip/axis) are pre-registered; C33 (state the locus, ≈4× inflated constant in first
   strip as [INF]) co-signed. The singularity is at our domain BOUNDARY, not interior — structurally
   easier than GP's interior sonic throat.
4. **Executable monitor gained (A4)**: the quasi-1D internal BC v₂(x_s)=−1/(dh/dx) ties the adjoint
   AT the front to local geometry — monitor-only analog for our fitted fronts (imposing it would
   overdetermine the discrete adjoint).
5. **A11 screen verified at source** (quasi-1D m=3); the 2-D m=4 correction (entropy + H both
   convect on the doubled streamline family) is the verdict's own and remains to re-derive at
   adoption.

## STAGE 3 — THE PER-PHASE vs PERIODIC-ADJOINT ADJUDICATION (Zahr-Persson pp.1-8 READ BY ME; Rubino via ZP's own characterization + report, targeted read DECLARED DEFERRED)

**Zahr-Persson (arXiv:1512.00616v2), formulation verified:** problem class = ∂U/∂t = L(U,μ,t) with
U(x,0)=U(x,T) (Eq. 1) — EXPLICIT time dependence (deforming domain, flapping kinematics = externally
driven unsteadiness); QoI = cycle integral (Eq. 2); DIRK fully discrete; periodicity u⁽⁰⁾=u⁽ᴺᵗ⁾ makes
the primal a nonlinear TWO-POINT BVP (fixed point of the cycle map, Eq. 9), solved by fixed-point /
Newton-Krylov shooting (Algs. 1-2, matrix-free Jv via directional sensitivity Eq. 18); the adjoint of
the periodically-constrained system = linear two-point BVP in time, existence+uniqueness in App. A;
stability of the orbit via Floquet multipliers of the monodromy (§2.3; neutrally stable systems =
hard case where the full Jacobian must be explored).

**The theoretical anchor for OUR formulation, now nameable from sources:**
1. The general machinery for periodic-flow design EXISTS in two forms — time-domain periodicity-
   constrained adjoint (ZP) and harmonic-balance adjoint (Rubino; ZP p.2 characterizes HB/time-
   spectral as "extremely large-scale, all time instances coupled") — so our gap D2-G3 is a gap of
   APPLICATION+THEOREMS, not of machinery (confirmed at source).
2. **For an AUTONOMOUS rotating wave the ZP machinery as printed is structurally degenerate**: the
   uniqueness of the periodic adjoint BVP requires (I − monodromy) invertible, and a self-rotating
   wave carries the trivial Floquet multiplier 1 (phase mode along the group orbit) — A20's
   "modulo-the-symmetry-group" correction, which I co-sign from the structure, not just from the
   report. The correct move in our class is SYMMETRY REDUCTION — quotient by the rotation — which is
   PRECISELY what the wave-frame/per-phase formulation does (T-T0 exactness). **Our per-phase steady
   adjoint is therefore not a cheap surrogate of the "true" periodic adjoint: in the pinned class
   (single-mode pure rotating wave) it IS the correct symmetry-reduced object, and the naive
   time-domain periodic adjoint would be ill-posed without the same quotient.**
3. The honest boundary, stated with the pin: exactness holds under {pure rotating wave (T0-flatness
   monitor), interface-data scope}; the O(St)/quasi-steady step and the dimensional reduction of the
   per-phase nozzle problem are PRICED approximations SEPARATE from the time-coupling question — and
   Harroun's ranking-blindness threat lives exactly there (decided by R22, not by this adjudication).
   Outside the pin (galloping, mode transitions, W≪1 per A34) the named escalation route is
   ZP/Rubino (+ LSS/NILSS for chaotic, registered at A10) — cite as alternative, never as refutation.

### STAGE 3 — ADDENDUM [IO] (2° passaggio): ZP Appendix A LETTA + minaccia Harroun VERIFICATA SUL PDF

**ZP App. A (pp.28-29) verificata**: la prova di esistenza+unicità dell'adjoint periodico POGGIA
sull'ASSUNZIONE dichiarata che `∂u^(Nt)/∂u₀ − I` sia non singolare alla soluzione periodica ("which
is assumed non-singular", p.28; conclusione p.29). ⇒ Il mio argomento di degenerazione ha ora la
premessa VERIFICATA a stampa: per un'onda rotante AUTONOMA (sistema self-sustained) la monodromia ha
autovalore 1 (modo di fase) e l'assunzione cade ⇒ la macchina ZP come stampata NON si applica senza
quoziente di simmetria. PRECISAZIONE che sposto a primario: per il SOTTOPROBLEMA ugello guidato da
BC periodica imposta (caso "driven", come il loro flapping) la monodromia dissipativa è generica-
mente non singolare e ZP si applicherebbe; l'ancora primaria della NOSTRA formulazione è quindi la
STEADINESS IN ROTATING FRAME (T-T0: dominio assialsimmetrico + onda pura ⇒ problema STEADY nel
riferimento co-rotante — la periodicità è quozientata via esattamente, nessun adjoint periodico
serve in-pin), e l'argomento di Floquet resta il SECONDARIO (perché "usare ZP sull'onda autonoma"
non è l'alternativa banalmente corretta). STATO DI CONVERGENZA dichiarato: fatti [IO]; l'aggiudica-
zione resta single-analyst, refuter-pending per lo standard dual-proof del progetto.

**Harroun 2021 p.671 verificata [IO], quote esatta**: "Using Eq. (7) for the detonation wave, a
coefficient of thrust could be estimated from averaging the discrete constant-pressure axisymmetric
computations for each point in time of the cycle. This quasi-cycle-averaged result estimated the
coefficient of thrust for both the IE and flared aerospike to be 1.25 … As these simulations were
two-dimensional and averaged, this result obviously did not account for the difference that a fully
three-dimensional detonation-wave inflow would have on the nozzle performance."
Esperimenti: TRE test appaiati (Table 3: 77/76, 73/75, 87/86; CTAP 7.4-16.5 atm), Fig. 22 = profili
di pressione nettamente diversi, separazione sul flared a x≈5 cm (low/mid), "The IE aerospike …
may thus be the better design" (claim QUALITATIVO, a quelle condizioni). Fig. 21 [IO visivo]: c_F
separati plug/cowl, cowl IE NEGATIVO (≈ −0.1). PRECISIONE DI RECORD sulla minaccia: (i) il
valutatore cieco è un CUGINO GROSSOLANO del nostro — snapshot 2-D assialsimmetrici a PRESSIONE
UNIFORME per fase (waveform p-only Eq. (7)), non stati di fase risolti in caratteristica; (ii) gli
AUTORI STESSI incolpano la riduzione 2-D almeno quanto la media ("obviously did not account…");
(iii) la separazione media-vs-riduzione NON è decisa dal paper ⇒ R22 resta l'atto che decide, e i
nostri stati di fase più ricchi POTREBBERO discriminare dove i loro p-only non possono — da
dimostrare, mai da asserire.

### STAGE 4 — ADDENDUM 2 [IO]: Stechmann-Heister-Harroun JSR 56(3):887-... §§I-II LETTO + AGGIUDICAZIONE FORMALE dell'analogia Harroun-vs-noi (sfida utente 2026-08-13)

**Stechmann verificato (pp.887-893)**: modello 0-D quasi-steady: waveform esponenziale
P_c(t)=P_R·P_init·e^(−λt) (Eq. 13, λ=ln(P_R)/t_c Eq. 14, tarata su blowdown con side-relief Fig. 3);
per ogni istante espressioni 0-D (Eq. 6-7) + C_F isentropico in forma chiusa (bell Eq. 9 a ε fisso;
**aerospike Eq. 10 IDEALMENTE ADATTATO P_e=P_a sotto il limite di espansione** — è questa
l'idealizzazione da cui esce "aerospikes preferred, 6-8%"); aggregato = **media PESATA IN MASSA**
Isp_RDE = (1/m_cycle)∫ṁ C_F c*/g dt (Eq. 4), con la motivazione esplicita che la media semplice
dell'Isp istantaneo è sbagliata; **Assunzione 3 = uscita RDE chocked/sonica in OGNI punto del ciclo**
(coerente con la riga choking-as-assumption dell'advisory 08-11); caveat CTAP p.893 (il trasduttore
può non catturare l'offset medio sotto instabilità nonlineari).

**AGGIUDICAZIONE FORMALE (la sfida utente era FONDATA — requalifica della "minaccia Harroun"):**
La costruzione di Harroun p.671 è: DUE geometrie fisse; per ogni istante del waveform (= per ogni
pressione camera UNIFORME) un campo steady 2-D assialsimmetrico a pressione costante; media delle
spinte sul ciclo. Confronto formale col nostro impianto, punto a punto:
(i) **parametro di fase**: loro = scalare P_c(t) lungo un blowdown 0-D; nostro = ξ lungo l'onda
   rotante con traccia d'interfaccia COMPLETA s(ξ) = (q,θ,T,s,h0)(ξ) risolta in caratteristica;
(ii) **stato per fase**: loro = UNIFORME (p-only); nostro = non uniforme. Formalmente la loro
   famiglia è l'IMMAGINE della nostra sotto la proiezione s(ξ) ↦ (P(ξ), uniforme, assiale) — un
   membro della classe che il nostro registro T3-CONTROL tratta come convenzione degenere (riga
   Liu Eq. 14), e ciò che la proiezione scarta (swirl per fase O(1), variazione di θ, covarianza
   T-M, struttura wave-frame) è ESATTAMENTE il contenuto della nostra breaker map;
(iii) **misura**: loro mass-weighted (Stechmann Eq. 4); nostra μ con la clausola conventions/
   matching REGISTRATA come grado di libertà (T-T3-MAP (e), inversioni d'ordinamento A26/A33);
(iv) **scopo**: loro VALUTAZIONE di due punti; nostro OTTIMIZZAZIONE con condizioni di ottimalità;
(v) **rischio CONDIVISO**: entrambe le costruzioni sono 2-D-per-fase — ed è la causa che gli autori
   stessi indicano ("obviously did not account ... fully three-dimensional").
**CONSEGUENZA DI RECORD**: l'analogia regge SOLO alla forma esterna (media di valutazioni steady
per fase su geometria fissa); si ROMPE al livello portante (contenuto informativo dello stato di
fase). La cecità del loro valutatore NON stabilisce che il nostro lo sia: stabilisce che la
PROIEZIONE scalare-uniforme lo è — cosa che la nostra teoria PREVEDE (è la classe di collasso/
T3-CONTROL) invece di temere. La minaccia si riqualifica in tre pezzi: (a) i valutatori standard
del campo (Stechmann 0-D, Harroun 2-D const-p) sono ciechi → è la nostra OPPORTUNITÀ, enunciata
come fatto sul campo; (b) che il valutatore RICCO (il nostro) discrimini al percento resta NON
DIMOSTRATO (assenza di evidenza, non evidenza contraria) → R22; (c) il rischio condiviso vero è la
riduzione 2-D-per-fase → R22(b)-vs-(c) la isola. STATO: aggiudicazione [IO] sulle tre fonti
(Harroun p.671, Stechmann §II, ZP App. A) ma single-analyst — refuter/panel pending per lo
standard dual-proof prima di entrare in M0.

## STAGE 5 — PARTIAL: Kraiko-Tillyaeva-Baftalovskii JPP 17(6):1347-1352 (2001), pp.1347-1348 READ BY ME

Page-verified on p.1348 col.2:
- **The slip-line instance (R16) is EXACTLY as adjudicated**: "In 1961 Sternin found out that the
  continuous solutions can be designed not in any choice of point c of the initial rarefaction wave
  fan. After that, in 1962 Shmyglevskii obtained the necessary conditions of maximal thrust IN THE
  FORM OF INEQUALITIES. For these cases he designed the 'discontinuous' optimal solutions (Fig. 1b,
  where ach and lcm are the compression and rarefaction fans, **cn is the shock wave, and ct is the
  slip line**, respectively)." → C30 lineage (Sternin 1961 constructibility boundary + Shmyglevskii
  1962 inequality-form conditions) VERIFIED; the discontinuous optimum carries an INTERNAL shock AND
  a slip line as STRUCTURAL elements.
- **C15 lineage verified**: CCM history as printed — Nikolskii 1950 (fore/afterbody, linear approx);
  Guderley-Hantsch 1955 (transfer to characteristic CC, exact formulation); Busemann condition named
  from Ref. 7; Shmyglevskii 1957 integrated the boundary problem (perfect gas); **Sternin 1957
  arbitrary two-parametric gas** (= EOS-generality, first obtained), "published in the periodical
  scientific press only in the beginning of 1959. A bit earlier, in the end of 1958, Rao published
  the same results" + the criticism episode + "Rao revised the work". All per the 2001 paper =
  **party in the dispute; the "secondo il resoconto di Kraiko et al. 2001" rider stands.**
- Eq. (1): P±_b± − p⁺ = 0 with P± = p(1 ± κM²/(2√(M²−1)) · sin2ϑ) — the corner/transversality pair
  in the ± form: matches our CSTR_PA/PB sign discipline (C+ vs C− corner), GENO convention check OK.
- Eq. (2): the two first integrals on cb — identical objects to KT2015 (2.12) and our f2/f1.

## STAGE 4 — PARTIAL: HARROUN REVISIT (cross-check of ADVISORY_rde_choking_2026-08-11 vs the new pass)

What the 08-11 analysis got RIGHT and keeps: the ONE misquote identified there ("near-perfect
time-averaged expansion" nonexistent) — CONFIRMED by full-text census on BOTH Harrouns (0 occurrences,
C26); separation-delay status "computed result, not measured" (S-GAUNTLET correction) — CONFIRMED and
sharpened; matched-mdot vs matched-⟨p⟩ degeneracy in their frozen lab (§2-bis(i)) — CONFIRMED, now
with attribution rider (twin construction = Paxson & Kaemming AIAA 2012-0770 proposal, NOT community
standard, C25); bell-collapse caution (§2-ter correction of the lead) — INTACT.

What the 08-11 analysis must now REVISE (three items, co-signed):
1. **The clause "T3-novelty REINFORCED by the misquote" is STRUCK** (C26): the misquote row is
   upgraded to "phrase absent AND the paper argues the CONTRARY thesis" (2021 p.661 + Conclusions
   p.672), BUT with two mandatory riders: perimeter = 0-D mass-averaged correlations (not "averaging
   in general"), and the paper's FAVORABLE conclusion (delayed separation → larger area ratios →
   better mission-averaged Isp) must be cited alongside — otherwise our reclassification is itself a
   partisan read.
2. **The "8x base drag" number loses record status** (C29): least grid-converged configuration,
   trend-validated only, CONTESTED in print by Schwer et al. (priv. comm. 5 Jan 2021, quoted in the
   paper; R23 open). The 08-11 USE of it ("band stays wide") survives — the NUMBER does not.
3. **Grade demotion G-d applies retroactively**: the 0.95-vs-0.59 atm surrogate-failure delta is
   CFD-vs-CFD on V1.3 methane (figure-read, no table), with one-sided cross-campaign (V1.4 kerosene)
   corroboration; "0.58-0.60 psia" p.7 is a units refuso for atm (C11). Anywhere the 08-11 advisory's
   downstream users say "measured", the grade is now "CFD-supported with partial experimental
   corroboration".

NEW vs 08-11 (absent there, added by the new pass): the **c_F = 1.25 ranking-blindness** (two
aerospikes indistinguishable by cycle-averaged c_F while experiment separates them) → value
proposition must be stated at the percent scale; **R22 disentanglement experiment** (3-D unsteady vs
3-D phase-averaged vs 2-D phase-averaged) = the deciding act, ours; **R2**: the actual carrier of the
cycle-averaged evaluation threat is Harroun's M.S. thesis (Purdue, July 2019), UNREAD — procurement P0.

## GIUDIZIO FUSO POST-CONTRADDITTORIO (4 refuter, tutti rientrati — chiusura sessione 2026-08-13)

I quattro punti teoricamente ricchi sono passati dal contraddittorio (REFUTE_A/B/C/D su disco).
Esiti e formulazioni di record che sopravvivono:

**A — Ancora simmetria-riduzione: CORRETTA A DUE STADI.** (stadio 1, esatto ma lemma NON scritto)
il quoziente giustifica l'adjoint steady 3-D wave-frame; T-T0 IPOTIZZA il pattern sul campo intero
(M0:442-445) — il lemma di propagazione "BC pura + dominio assialsimmetrico ⇒ steady co-rotante" è
provabile su classe L4 ma va SCRITTO (azione R4). (stadio 2, approssimazione dichiarata) il
passaggio alle marce 2-D per fase scarta l'accoppiamento in θ — M0 stesso: "the only approximation
in the chain" (rung 2). "ZP mal posta" RITIRATO: sul sottoproblema guidato in-pin è ben posta e
DOMINATA in costo (monodromia contrattiva, margine L4); la degenerazione vale per la vista
autonoma. Caveat nuovo: flatness cieca alle armoniche lab-steady da iniettori.

**B — Requalifica Harroun: clausola portante REFUTED.** "La nostra teoria lo prevede" era doppio
abuso di T-T3: fuori ipotesi (valutatore RANS VISCOSO ambient-coupled con separazione e transizione
wake a NPR≈6.7 = breaker (a) di M0:660-664; Pa≠0 costante da solo NON rompe il collasso, Lemma C)
e oggetto sbagliato (il collasso è sulle fasi a parete fissa, mai fra GEOMETRIE). Errori fattuali
miei emendati: "mass-weighted" NON stampato in Harroun (convention UNDECLARED, M0:713-715); Eq. (7)
è log-fit da CFD, non l'esponenziale di Stechmann. Sopravvive: il tie non trasferisce a noi
(proiezione valida solo sul canale inflow; valutatori INCOMPARABILI), lezione primaria = fragilità
della convenzione di media (tocca anche la nostra μ). Rischi finali: 2-D (condiviso), quasi-steady
(condiviso), **INVISCIDO (solo nostro: il loro valutatore vede la separazione, il nostro no)**.

**C — Forma a cono C31: NECESSARIA nella sostanza, SOVRADIMENSIONATA nella forma.** Forma minimale:
UN enunciato `D ∈ N_K(s_E*)` con K dichiarato per istanza; la portata fissa è UGUAGLIANZA (KT2015
2.13) e NON entra nel cono; "il driver gira in active-set all'endpoint" è FALSO
(a1_toc_variational_jax.py:1748 pinna il lip per uguaglianza); M0:1699-1704 dichiara già la
sostituzione di regime 2. Lemma di trasferimento REGGE (dimostrazione elementare: semispazi +
monotonia; viceversa falso, controesempio D=(−1,+3) media +1). C32 CONFERMATA (R=(+2,−1), w=(1,4)
⇒ segni opposti) con qualificatore di regime. **Cecità duale VERA su CINQUE carrier, non tre**
(R3 o33:754; R7 o33:689-695; f3* solo drift; a1:2356-65 usa abs(lam); margin_governor:64-73).
Emenda S2: f3* ≥ 0 identicamente ⇒ il seed rejector va sull'IDENTITÀ, non sul segno.

**D — R16 slip line: TIENE NEL NUCLEO, riqualificato in 4 punti.** Clausole citate fedelmente
(verificate verbatim); rigetto anzi SOVRADETERMINATO (manca (F3) NONINTERACTION D25U:71-73; il
rejector X-U3BD aveva GIÀ rilevato singolare il limite caratteristico). Membership in S1 regge
(problem_book:373-374 include "transversal shocks/contacts") ma è ASSERITA, non certificata; sanare
la collisione di nomi S_1-tier (M0:1606) vs S1-classe. Regime corto DENTRO l'inviluppo (plug corti
= bandiera RDE; S20 boundary-active) ma il gap VINCOLA AL GATE F4b, NON blocca la catena
S-ORDINE→S-CERT→F2. "Struttura, non tolleranza" RAFFORZATO (m·[v_t]=0 ⇒ [v_t]≡0 su ogni Lax; il
limite [S]→0 è la Mach line, mai un contatto). Test di accettazione: PMM 1962 non su disco ⇒
sostituto su disco = secondo schema Shmyglevskii CMMP (M0:1572-76, che GIÀ nominava l'istanza
contatti: chiosa di novità RIDIMENSIONATA).

**Conversioni finali a [IO] pre-chiusura**: Fernandes (pp.868-872: FFD + fmincon/NSGA-II, MoC =
valutatore in NLP generico Eq. 13, zero condizioni di ottimalità ⇒ NICCHIA CONFERMATA); Rubino
(pp.221-225: HB duality-preserving via contrazione Eq. 40, AD CoDiPack, 2K+1 istanze accoppiate ⇒
per fronti ripidi K grande — la famiglia di fasi risolve la ripidezza geometricamente); Ancourt
(refs pp.20-21: 45 voci, classici MoC presenti (Ferri 1946, Meyer-Goldstein, Shapiro,
Liepmann-Roshko) + Lions 1968 + scuola adjoint completa, ZERO scuola variazionale ugelli).

## LOSS-PREVENTION LEDGER (nothing dropped)
- Stage-1 text of record = THIS FILE (conversation-only content now persisted).
- Duties CO-SIGNED so far (ready for user ratification): D-01 (gloss), C31/C30 pair (cone form +
  Shmyglevskii attribution — C30 verified via (2.10)/(2.14) inequality instances; R28 Shmyglevskii
  1962 full text still gates the final wording), C7 (Efremov-Kraiko re-key), C25, C4, R1-demotion.
- Open in-code verification: o33_bench sign-blindness (S1), f3* vs λ_L (S2), per-phase sign scan (S3).
- The three P0s stand: R1 (ISABE full text), R2 (Harroun MS thesis 2019), R22 (disentanglement
  experiment 3D-unsteady vs 3D-phase-averaged vs 2D-phase-averaged).

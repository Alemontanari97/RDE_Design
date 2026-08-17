# HYPAUDIT — [I-GEO + I-STATE]: design axisymmetry + per-phase state axisymmetry vs the in-repo corpus

Auditor: S-FOUNDATIONS hypothesis-audit subagent, 2026-08-17. In-repo sources only.
Hypothesis bundle under audit:
- **[I-GEO]** DESIGN AXISYMMETRY: the nozzle solid S is axisymmetric — a design-class pin.
- **[I-STATE]** PER-PHASE STATE AXISYMMETRY: rung-2 per-phase meridional axisymmetric fields from
  s(ξ), while the true wave-swept flow is 3D; exactness route = co-rotating wave-frame
  steadification; residual = azimuthal commutator/sweep terms carried in a declared residual channel.
Adversarial default applied: literature data wins over internal preference.

CAVEAT of record: `validation/ADVISORY_litreview_confrontation_2026-08-13.md` is CAVA NON
RATIFICATA — cited below only as pending-ratification evidence, never as decided.

---

## 1. VERDICT IN FRONT

**LEGITTIMA-DICHIARATA-MONITORATA** for the pair as posed, with a sharp asymmetry between the
two halves:

- **[I-GEO] is legitimate essentially by construction** — a design-class pin restricts the search
  space, and every RDE nozzle in the read corpus (Harroun's two aerospikes, Paxson-Miki's shrouded
  truncated plug, NASA RDRE hardware) is a body of revolution. The corpus contains exactly one
  asymmetric-design counterinstance (Kraiko 2016 two-sided planar nozzles for vectorial thrust),
  which is a named non-containment of (P), not a contradiction of the pin.
- **[I-STATE] is legitimate ONLY in the exact form the repo's own refuters forced**: per-phase =
  exact rotation quotient (wave-frame steadification) **plus** a declared rung-2 residual
  (the θ-coupling/sweep term), never "the correct object tout court". The measured interface
  fields say the residual's SOURCE terms are **O(1), first-order, not cosmetic** — legitimacy
  survives because the channel is declared, priced (O(St)), metered (B-lite) and backstopped
  (rung 3a), not because the residual is small. The corpus has an **empirical vacuum** exactly
  where the residual would be directly measured.

---

## 2. [I-GEO] DESIGN AXISYMMETRY — corpus confrontation

### 2.1 The corpus designs are uniformly axisymmetric
- [Harroun 2021, reports/harroun_2021_jpp_nozzle_perf.md §2]: all three geometries (nozzleless
  blunt body, IE aerospike = cowl + 22.57° conical plug by MoC per Denton, flared aerospike by the
  NASA ADAPT tool) are bodies of revolution; 2-D axisymmetric meshes "revolved 360 deg with
  one-degree circumferential cells" (p. 665).
- [Paxson-Miki 2022, reports/paxson_miki_2022_nasa_opt.md §2]: baseline and all 7 design variants
  are shrouded truncated plugs — axisymmetric; the two design variables are area ratios of a
  surface of revolution.
- [Miki 2020, reports/miki_2020_nasa_methodology.md]: six hand-drawn axisymmetric geometries.
- [Teasley 2023/2025, reports/teasley_*.md]: RDRE flight-like hardware — annular, axisymmetric
  nozzle subcomponent (2025: nozzle = manufacturing subcomponent, 4-scalar sweeps).
The field's own design practice IS the pin. No paper in the corpus designs a non-axisymmetric
RDE nozzle.

### 2.2 The one counterinstance and why it does not refute
- [Kraiko 2016, ADVISORY_litreview_confrontation §2 row 6 + §1.4 (pending ratification)]:
  two-sided ASYMMETRIC planar maximum-thrust nozzles under VECTORIAL thrust criteria. The
  confrontation verdict already classifies this as a structural NON-CONTAINMENT of (P) (claim 18:
  "criterio di spinta VETTORIALE/Pareto — o si scalarizza in c"), i.e. a declared boundary of the
  problem class, not evidence that the axisymmetric pin is illegitimate inside its scalar-thrust,
  annular-RDE scope. Residual risk to carry: the pin excludes a design family the classical corpus
  proved can win under other criteria — this must remain a NAMED class restriction.

### 2.3 Where real hardware breaks axisymmetry — and where the contract puts it
- [REFUTE_A line (4), reports/REFUTE_A_symmetry_reduction.md r.119-139]: the in-pin declarations
  exist at named M0 anchors (S axisymmetric T-T0 r.444-445; axisymmetric wall r.363-364; Γ_d fixed
  axisymmetric r.116). Discrete injectors live UPSTREAM of Γ_d: "la rottura hardware
  dell'assialsimmetria è fuori dominio di design e dentro la classe-dati. In-pin è dichiarato."
  Verdict TIENE — with the named residue that an injector-locked, LAB-frame-fixed harmonic
  (s(θ, θ−Wt), two-frequency) produces constant thrust and is INVISIBLE to the T0-flatness
  monitor; its detector is the harmonic/contract audit + the TRIPLE (Γ,h0,s) monitor.
- [Mean-swirl panel, ADVISORY_mean_swirl_panel_2026-08-11.md P1/S1]: the geometric kernel is
  machine-verified — any surface of revolution has n_θ ≡ 0, zero axial pressure torque
  ([T-SLRW]); the genuine torque channels are exactly the NON-axisymmetric wetted geometry
  (discrete orifices/posts, "generically nonzero in real hardware EVEN WITH purely axial injected
  streams"), wall shear, swirled/backflow injection, aperiodic storage. So the pin's price is
  known and bounded to declared channels (H-AM1..H-AM5), with the faceplate channel kept DISTINCT
  of record.

**[I-GEO] sub-verdict: LEGITTIMA as a design-class pin** — corpus-conformant, with two named
residues: (a) the vectorial-thrust asymmetric family excluded (Kraiko 2016 non-containment);
(b) injector-locked lab-frame asymmetry lives in the data class and needs its own detector
(harmonic audit, not flatness).

---

## 3. [I-STATE] PER-PHASE STATE AXISYMMETRY — corpus confrontation

### 3.1 The exactness route, as the repo's own refuter left it
The hypothesis's exactness claim must be cited in the REFUTE_A-corrected form, not the Stage-3
original:
- [VERIFICATION_FABLE Stage 3 + Addendum, reports/VERIFICATION_FABLE_2026-08-13.md r.168-214]:
  for an AUTONOMOUS rotating wave, the printed periodic-adjoint machinery (Zahr-Persson) is
  degenerate (trivial Floquet multiplier 1; App. A pp.28-29 assumes (I − monodromy) nonsingular);
  the correct move in the pinned class is the symmetry quotient — wave-frame steadification.
- [REFUTE_A, verdict complessivo r.184-207]: three corrections now bind any citation:
  (a) T-T0 HYPOTHESIZES the rotating pattern on the whole field; the propagation step
  "pure-rotating data + axisymmetric domain ⇒ field pattern" needs the L4 uniqueness + SO(2)
  equivariance lemma, PROVABLE but NOT YET WRITTEN in M0 (duty R4) — "l'attribuzione a 'T-T0
  exactness' da sola è una citazione eccessiva";
  (b) the quotient converts temporal coupling into SPATIAL θ-coupling — the correct
  symmetry-reduced object is the steady 3-D wave-frame adjoint; the 2-D per-phase family is its
  rung-2 quasi-steady factorization, "esatta a meno del termine sweep O(St) prezzato" (REFUTED as
  "the correct object" at the letter);
  (c) "ill-posed" is retired for the driven in-pin subproblem — ZP there is well-posed but
  strictly dominated.
- [ASSESSMENT_methodology_position_2026-08-13.md §3.1]: the ratified honest claim is verbatim
  "per-fase = quoziente esatto + rung-2 dichiarato, MAI 'l'oggetto corretto' tout court."
The hypothesis AS POSED in this audit ("exactness route = wave-frame steadification, residual =
azimuthal commutator terms in a declared residual channel") **is precisely the survived form** —
it does not repeat the refuted Stage-3 title. That is what makes it auditable as legitimate.

### 3.2 What the measured/computed interface fields say about the residual's source magnitude
The rung-2 residual is fed by per-phase azimuthal gradients and relative swirl. Every in-corpus
datum says these are O(1):
- [Miki 2020, reports/miki_2020_nasa_methodology.md T-4 + F-i/ii]: the only published azimuthal
  interface trace in the corpus (Fig. 4, p.6): P0 sweeps ≈5e5 → 2e6 Pa (4×), T0 ≈1400 → 2200 K,
  axial w ≈ 500-800 m/s, u ±400 m/s, TANGENTIAL v ≈ ±300 m/s about ≈0, sharp front near 270°.
  Verbatim (p.2): "While there is no overall net swirl in the combustor outlet flow, there is
  typically a local tangential component of velocity at each circumferential location." The
  per-phase tangential velocity is a large fraction of the axial one — the flow-angle (pitch)
  nonuniformity at the interface is tens of degrees at wave passage, wave-locked.
- [Paxson-Miki 2022, reports/paxson_miki_2022_nasa_opt.md §4-F4, F6]: exit-plane σ/μ ≈ 0.70
  (p.5, via the mean-swirl panel's re-use); "significant local tangential velocity components"
  (p.2) asserted alongside "no net swirl" (asserted, no figure); Fig. 3 Mach 1.15-1.45 is
  TOTAL-velocity Mach — the axial component is never reported, so the data cannot certify the L4
  axially-supersonic margin (correction F4 of record: cite only as "assumed", never as measured).
- [Mean-swirl panel P3, ADVISORY_mean_swirl_panel_2026-08-11.md]: at σ/μ ≈ 0.70 the
  mass-flux/swirl covariance terms carry weight (σ/μ)² ≈ 0.5 — "first-order, not cosmetic"; the
  swirl-KE flux is positive-definite and unconstrained by the flux-nullity theorem. And the
  program's own M0 (as re-verified by REFUTE_A line 5, r.153-158): "the huge relative swirl …
  IS the O(St) sweep term" (M0 r.514-515) — relative swirl W·r ~ D_CJ in the wave frame, i.e. the
  residual channel's carrier is O(1) by the record's own admission; T-T3QS prices the smooth part
  at first order zero on ray cycles, with a JUMP-LOCALIZED residual at fronts whose absorption by
  the fitted sheet is CONJECTURE (P-ii) until O5 measures it.
- **Empirical vacuum (unanimous, mean-swirl panel S2/open items)**: "no time-mean
  tangential-velocity field, profile, or angular-momentum flux is reported anywhere in the read
  corpus" — Paxson-Miki Fig. 3 is instantaneous total Mach never decomposed, Harroun imposes
  zero-swirl inflow BY CONSTRUCTION (2021 p.666: "the incoming flow was not rotating and had no
  vorticity", radially uniform, T = 3400 K uniform), Kaemming-Paxson report axial Mach only.
  Conclusion of record: the residual magnitude has never been DIRECTLY measured by anyone in the
  corpus; what is measured is its SOURCE (O(1) azimuthal nonuniformity and tangential velocity).

### 3.3 The standing empirical threat, and its exact scope
- [Harroun 2021, reports/harroun_2021_jpp_nozzle_perf.md §2bis, F1]: the quasi-cycle-averaged
  2-D axisymmetric per-phase surrogate returns c_F = 1.25 for BOTH aerospikes
  (discrimination-blind), while 3-D unsteady CFD + three paired experiments (Fig. 22, Table 3)
  separate the designs; the authors blame 2-D-ness AND averaging in one breath "and do not
  disentangle the two" (undeclared hypothesis f).
- [Harroun 2020, reports/harroun_2020_validation.md §2 quote + F10]: "the axisymmetric
  cycle-averaging is too simplistic of a method to estimating performance potential" (p.11);
  abstract: "the strength and the necessity for 3D transient computations". F10's adjudicated
  scope: the 3-D-necessity evidence lives in base/wake/cowl-recompression/turbulent-BL physics —
  regions the per-phase inviscid core evaluator already fences off via H2'; "the paper offers no
  evidence that the CORE expansion requires 3D."
- [REFUTE_B, reports/REFUTE_B_harroun_requalification.md]: binding corrections when citing this
  threat: Harroun's blind evaluator is p-only-uniform per phase (waveform Eq. (7), log-fit, T
  uniform, zero swirl, averaging convention UNDECLARED — "mass-weighted" must not be asserted);
  it is a coarse COUSIN, informationally INCOMPARABLE to the characteristic-resolved evaluator
  (their field channel is viscous/ambient-coupled, a superset; the inflow channel is a strict
  projection). The tie 1.25=1.25 is a rounded measure-coincidence of two crossing c_F(NPR)
  curves, NOT a T-T3 instance and NOT proof of per-phase poverty. Three risks of record:
  2-D-per-phase (shared with Harroun), per-phase quasi-steadiness (shared), INVISCID (ours, NOT
  shared). Percent-level ranking power of the per-phase aggregate: NOT demonstrated, proven NULL
  in the tier-1 corner, decided by R22 (3-D unsteady vs 3-D per-phase averaged vs 2-D per-phase
  averaged — "the single highest-value item", Harroun-2021 read §7.4).
- [ADVISORY_litreview_confrontation §1.2 (pending ratification)]: cycle averaging adequate for
  SIZING (Paxson-Miki 6.54 predicted vs ≈6.5 measured cycle-optimal, one-parameter slice, MEDIA)
  and "non è dimostrata adeguata al RANKING DI CONTORNO al livello del percento" — claim 19 and
  the value proposition must be stated at that scale.

### 3.4 Wave-attached structures and per-phase constraint closures
- [Harroun 2021 F2/F3/F6]: the separation point migrates WITHIN the cycle (Fig. 20), the
  separated region has "complex geometry, contrary to the axisymmetric separated flow geometry
  expected for a constant-pressure case" (p. 669), the wake-mode transition NPR ≈ 6.7 is crossed
  every cycle, and g_sep is history/frequency-dependent (Eq. 9, 72 μs replenishment). These are
  wave-attached, non-axisymmetric, memory-carrying structures — but ALL live in the
  viscous/base/ambient-coupled region already excluded by H2'; on that region the per-phase
  axisymmetric evaluator must never claim scope (obligation of record, Harroun-2020 F10). The
  favorable sign (unsteadiness DELAYS separation ⇒ quasi-steady g_sep conservative on this
  instance) is a named direction-of-error, not a validation.

---

## 4. ADJUDICATION

1. **The pair is coherent as (design pin + declared-residual idealization).** [I-GEO] matches the
   entire corpus's design practice and is protected by a machine-verified geometric kernel
   (n_θ ≡ 0, [T-SLRW]); [I-STATE] is stated in the refuter-survived form (quotient exact +
   rung-2 residual declared), which the repo record prices (O(St), T-T3QS), meters (B-lite,
   M0 r.1208) and backstops (rung 3a anchor).
2. **The literature does not contradict either half as posed** — no corpus datum shows a
   non-axisymmetric optimal RDE nozzle in-scope, and no corpus datum refutes wave-frame
   steadification for the single-mode pure rotating class. What the data DOES say: (a) the
   residual's sources are O(1) (σ/μ ≈ 0.70; tangential ±300 m/s vs axial 500-800; P0 4× per
   cycle), so the hypothesis is only honest WITH the residual channel and its monitors, never as
   an approximation-free statement; (b) the one published head-to-head where a per-phase
   axisymmetric surrogate met experiment (Harroun) shows discrimination-blindness at the percent
   level, confounded between averaging and 2-D reduction — R22 is the decider and is not run.
3. **Not LEGITTIMA-ESATTA**: the exactness holds only for the quotient stage, and even that
   currently over-cites T-T0 (propagation lemma unwritten — REFUTE_A duty R4). Not CONDIZIONATA:
   the validity window (single-mode pure rotating wave, L4 margin, H2' core) is already declared
   INSIDE the hypothesis via the pin + residual channel, so the correct grade is the
   declared-and-monitored one. Not DA-RISCOPARE: the posed form already incorporates every
   correction the refuters forced.

**VERDICT: LEGITTIMA-DICHIARATA-MONITORATA.**

## 5. MONITORS REQUIRED (all in-repo, named)

1. **T0-flatness certificate, stated in the WAVE frame** — pin monitor for the pure-rotating
   class; the Miki 2020 Fig. 4 lab-frame trace is strongly non-flat, so a lab-frame reading would
   falsely fail (Miki-2020 read, scoping consequence (a)).
2. **Harmonic/contract audit of the data class** for injector-locked lab-frame asymmetry
   (two-frequency s(θ, θ−Wt) outside CycleFamily) — flatness is provably BLIND to this channel
   (REFUTE_A line 4).
3. **TRIPLE (Γ, h0, s) per-phase spread monitor** with DERIVED threshold + ψ-monotonicity/backflow
   C1 guard, wired as a G6 rejector (mean-swirl panel S4, F-swirl-2).
4. **Angular-momentum balance-residual audit row**: |measured flux − declared J_inj − declared
   shear/numerical torque budget| ≤ derived tolerance, normalized by gross flux, ≥2 stations
   (mean-swirl panel, new contract row).
5. **B-lite meter of the rung-2 sweep/D2 residual** — the cheap exact meter of the declared
   residual channel (M0 r.1208 via REFUTE_A line 5).
6. **Axial-Mach (L4) margin audit measured on data** — never total-velocity Mach (Paxson-Miki
   correction F4).
7. **R22 disentanglement experiment** (3-D unsteady vs 3-D per-phase averaged vs 2-D per-phase
   averaged) — the named decider of averaging-vs-reduction blame (Harroun 2021 read §7.4;
   ASSESSMENT §2).

## 6. RESIDUAL RISKS (named, with owners in the record)

- Percent-level ranking power of the rung-2 aggregate UNPROVEN; proven null in the tier-1 corner;
  Harroun c_F = 1.25 stands as the confounded threat until R22 runs (open, P0-class per
  VERIFICATION_FABLE/REFUTE_B).
- Jump-localized first-order sweep residual at wave fronts: fitted-sheet absorption is
  CONJECTURE P-ii until O5 measures it (M0 r.403-406 via REFUTE_A).
- Empirical vacuum: no time-mean tangential field/profile/AM-flux anywhere in the corpus — the
  residual magnitude itself is unmeasured; first ingested periodic chamber-CFD dataset must arm
  F1-F4/A4 (mean-swirl panel falsifier block).
- The equivariance/propagation lemma (L4 uniqueness + SO(2)) is provable but UNWRITTEN in M0 —
  until written, the exactness route may not cite "T-T0 exactness" alone (REFUTE_A duty R4).
- [I-GEO] excludes the asymmetric/vectorial-thrust design family (Kraiko 2016 non-containment,
  claim 18) — legitimate class restriction, must stay declared.
- Per-phase axisymmetric evaluator has NO scope over base/wake/separated/ambient-coupled regions
  (H2' fence; Harroun 2020 F10 obligation) — μ(Ξ_sub) > 0 is the GENERIC sea-level RDE case
  (Harroun 2020 F5).

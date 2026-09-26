# ADVISORY 2026-09-26 — The procedure for the RDE nozzle: from the two-wall carrier to the cycle-averaged shrouded plug

Status: PROPOSAL for the owner (written 2026-09-26 evening, after the length-cap
result of S41 step 2). Nothing here is executed. Every anchor below was read
again on 2026-09-26 (file:line of the current tree).

## 0. The directive

The owner, 2026-09-26 (Italian, after the cap comparison): "dovremmo stabilire
una procedura per capire come ottimizzare l'ugello per un RDE. Probabilmente
costruiremo il profilo tenendo conto di tutte le fasi contemporaneamente
permettendo ad ognuna di votare in funzione della loro durata, temperatura e
stato della linea iniziale. Siccome ci metteremo nel frame della detonazione
dovremo inoltre ricordare il termine centrifugo."

Three requirements: (R1) all phases at once, each voting by duration,
temperature and initial-line state; (R2) the detonation (wave) frame; (R3) the
centrifugal term is not forgotten. This advisory says what the corpus already
fixes for each, what exists in code, what is missing, and in which order the
missing pieces are built and gated.

## 1. What the corpus already fixes (verified anchors)

R1 — the vote. The objective of record is the cycle average
`J[Σ] = ∫_Ξ F[Σ; s(ξ)] dμ(ξ)` with μ the pushforward of normalised cycle time
(docs/rde_nozzle_problem_book.md:113-133, eq. (AVG)). Proposition O1
(problem_book:94-109) proves the weight is UNITY under choked, frozen feed:
Isp-max and J-max coincide, "no mass-weighting ambiguity survives at the shape
level". The swirl five-field panel states the same in one line: "all data
non-uniformity lives in ξ ↦ s(ξ), never in the ξ-measure"
(validation/swirl5f_panel_2026-08-19/swirl5f_FINAL_report.md:380-381). So the
owner's "vote by duration, temperature and initial-line state" is exactly (AVG):
the DURATION is the weight; the TEMPERATURE and the STATE OF THE LINE are inside
the phase's own thrust F[Σ; s(ξ)], through its data — never a second weight.
The unweighted average was ruled an error (docs/rde_nozzle_pipeline_audit.md,
row E1); the weighted transversality is the required form. The vocabulary
"vote" is already the repo's: validation/a1_cycle_corner.py:1-12 ("the
wave-passage phases vote 'lengthen', the tail phases vote 'shorten', the
μ-weighted average of the votes vanishes").

R2 — the frame. Theorem T0 (docs/rde_nozzle_MASTER.md:512-532): for a
rotating pattern the thrust through any axisymmetric surface is CONSTANT in
time and equals the wave-frame steady integral; "(iii) Coriolis −2W e_x × w is
orthogonal to e_x; centrifugal W²r e_r is radial". The per-phase formulation is
the exact symmetry quotient plus one declared approximation, rung 2 = the
θ-coupling discarded (MASTER:546-559). The data surface: an axial plane carries
data iff u_x > c, in every frame; "CJ-sonicity licenses NO axial MOC"; the
relative swirl (≈ −D_CJ) never enters rung 2, it is the O(St) sweep term
([T-NSW], MASTER:688-711).

R3 — the centrifugal term. It lives in two places, neither of them the thrust:
(a) the FIELD equations of a phase with swirl carry the source ρw²/r in the
r-momentum and −ρvw/r in the θ-momentum (docs/rde_nozzle_N6_swirl.md:21-24,
111-116); in the march this is the extra term of the compatibility relations,
already coded for the free vortex as `c² v/y → (c² + Γ²/y²) v/y`
(validation/a1_swirl_march.py:1-16); (b) the invariant transported along a
streamline in the wave frame is the ROTHALPY I = h0 − ΩΓ, not h0: the current
five-field schema "transports h0 and Γ separately where truth transports only
I" (swirl5f_FINAL_report.md:158-161; N6_swirl.md:171-175). The optimality
system with the centrifugal wall-transversality term is still SCHEMA
(N6_swirl.md:136-141).

The interface. The CycleFamily contract VI.1 (MASTER:3077-3106) lists the
fields per phase: P0, T0, γ(·;ξ), M_in(y;ξ) MERIDIONAL (total Mach prohibited
as the audit quantity), θ_in(y;ξ), s(y;ξ), w or Γ(y;ξ) = R·w (the transported
row), h0(y;ξ), plus μ weights, provenance and the stage-A audits (spacelikeness
margin m_n(ξ) = ess inf (M_n − 1) per phase, Crocco residual, T0 flatness).
The idealisation ladder (problem_book:191-214): I3 = the S-H sonic family
(P0(ξ), T0(ξ), frozen γ, uniform profiles); I2 = the μ-family of meridional
profiles, rung 2's native interface and GENO's (`read_ivl_from_file`); I1 =
steady 3-D wave-frame data (opens N6 only). Sources (development_plan.md
Annex B, :1326-1332): case A specs only → Cantera CJ/HP + S-H blowdown,
log-uniform μ; case B a per-phase generator, upgraded by F5 to a CFD-to-contract
pipeline with the extraction-surface rule "on a surface downstream of the
throat where the axial flow is per-phase supersonic; exact-throat transonic
hand-off = a SEPARATE priced duty; PREMISE-OPEN until U3' (F2a) closes"
(development_plan.md:414-427); case C experiment.

The shape problem. T3/T4 (docs/cycle_averaged_variational_nozzle.md:65-77):
a fixed-wall bell collapses to Rao at ⟨Pc⟩; the ideal untruncated plug is
optimal at P_CJ; "the first genuinely open, genuinely cycle-averaged shape
problem is the TRUNCATED plug (and the shrouded plug), where no single-phase
design is optimal" — i.e. exactly the two-wall object of S40-S41. T2
(cycle_averaged:217-252): per-phase adjoints, a function-valued mass-flow
multiplier λ2(ξ), SHARED geometric multipliers (length, exit radius, lip).
Hypothesis D3 (cycle_averaged:190-192): every per-phase flow MOC-regular.

The constraints. The tier-invariant clause (development_plan.md:472-496):
never stall, a finite negative surrogate at a failed march, and at every
transition "homentropic → stratified data" the margin is RE-DERIVED and KAT-ed
before the first decisive run; the fold governor is "HOMENTROPIC-SCOPED until
the F2 extended (q; s, h0) margin lands" (:465-468). DUTY-14, "tail-governed
constraint activity needs the phase measure", is assigned to the F5a entry
(:579-583); H-CON (docs/rde_nozzle_hypothesis_ledger.md:173-179) prices the
same fact.

## 2. What exists in code, and what is missing

Exists: the certified homentropic march (validation/a1_plug_march.py) with two
ADDITIVE seams — the rotational seam (six-row start (x, y, u, v, s, h0), per-
streamline entropy and stagnation enthalpy, :250-262) carried by
validation/a1_rot_march.py [X-RMAR] (Zucrow ch. 17 three-family form in (p, θ),
"the general inlet", W-5 closed), and the free-vortex swirl seam
validation/a1_swirl_march.py (uniform Γ, h0, s; the meridional flow stays
irrotational by Crocco; the centrifugal source in the compatibility relations).
The two-wall carrier validation/a1_twowall.py (S40-S41): arc posing, length cap,
fold class on the whole net, Newton metric, wavefront replay (2-4 s per
gradient at the coarse rung), the record driver with restoration. The cycle
instruments for ONE degree of freedom: validation/a1_cycle_corner.py (the
μ-weighted corner votes) and a1_plug_cycle.py (truncation length).

Missing: (i) no march carries a NON-UNIFORM Γ(ψ) together with (s, h0) — the
five-field model [S-5F] is SCHEMA, its promotion deferred to the F2 entry;
(ii) no march transports the rothalpy; (iii) no marcher is posed in the wave
frame (no Ω_w, w_rel anywhere in validation/*.py); (iv) no full-contour
μ-averaged shape optimiser: the two-wall carrier is single-state (one uniform
M 1.5 inlet, one isentrope); (v) no CycleFamily instance extracted from a
THOR-class CFD field (the plan's CFD names SU2 for the adjoint route; the
chamber data we own are MOSE_GPU/MOSE_open fields of THOR).

## 3. The procedure (proposal), in order of dependence

### Stage 0 — the data question first (U3' choking adjudication, F2a)

The rule of record: the initial line sits on a station downstream of the
throat where u_x > c in EVERY phase (m_n(ξ) > 0 μ-a.e.). THOR as simulated has
no nozzle: its exit plane is at chamber pressure and the fill phases are
axially subsonic there. The first executable step is therefore a CENSUS on the
fields we already have (THOR CAv2 probe chains, latest fields, no-BL, coarse
ambient): bin the exit-plane flow in the wave frame (θ' = θ − Ω t over the last
laps, Ω from the probe), read u_x/c and the meridional Mach per (θ', r), and
report the μ-measure (duration fraction) of the phases where the plane is
spacelike. Three outcomes, each with its consequence:
 (a) spacelike μ-a.e. — the exit plane is the IVL, I2 data directly;
 (b) not spacelike in the tail — a converging annular section must choke every
     phase at a common throat: the IVL moves to the first supersonic station
     (Sauer-type per-phase expansion from the sonic line, problem_book:284-287,
     or the CFD's own station once the converging section is meshed);
 (c) unchoked phases survive even the throat (the corpus's documented choking
     margins 0.97/0.65 for hydrocarbon cycles, problem_book:104-107) — those
     phases have no MOC data: their μ-weight is reported as UNMODELLED thrust
     (an error bar on J), or they go to the wave-frame march (rung 3, B-lite,
     development_plan.md:816-824), never to a per-phase MOC.
Deliverable: one CycleFamily instance for THOR (VI.1 fields, μ, provenance,
stage-A audits) written by an extraction operator on MOSE_GPU/MOSE_open
fields — the F5 "CFD-to-contract pipeline" of development_plan.md:414-427, with
the wave-frame binning as its first block. This is where R2 and R3 enter the
DATA: the extracted relative swirl is w − Ω r, the contract carries Γ = r·w
(absolute) and h0 (which includes u_θ²/2 by the pinned convention,
hypothesis_ledger swirl5f rows), and the per-phase march transports I = h0 − ΩΓ.

### Stage 1 — the per-phase engine: the stratified swirling march ([S-5F])

Merge the two additive seams into one carrier: six-row start + Γ(ψ) as a
seventh streamline invariant, the (p, θ) three-family compatibility relations
of a1_rot_march with the centrifugal source of a1_swirl_march
`(c² + Γ²/y²) v/y`, the streamline foot carrying (s, I, Γ). A non-uniform Γ(ψ)
makes the meridional flow rotational (Crocco), so the three-family form is
mandatory — it is already the rot march's. Gates, in this order:
 G1-1 four-wide data reproduce the certified homentropic path bit-for-bit (the
       seams' existing gate, kept);
 G1-2 uniform Γ, uniform (s, h0) ≡ a1_swirl_march to round-off;
 G1-3 Γ = 0, stratified (s, h0) ≡ a1_rot_march to round-off;
 G1-4 a KAT against an exact rotational swirling solution (the conical
       free-vortex flow with stratified h0, or Zucrow ch. 17's example) —
       the transition duty of the tier-invariant clause;
 G1-5 the rothalpy diagnostic Δh0 = ΩΔΓ on contact-free bundles (swirl5f E3);
 G1-6 the fold margin RE-DERIVED for the stratified class and KAT-ed (the
       governor is homentropic-scoped today) before any decisive run.
The wavefront replay carries over (one more solver kind per node width).

### Stage 2 — the μ-averaged two-wall optimiser (F5a)

J_μ(W) = Σ_k μ_k F_k(W): ONE geometry (the arc posing with its cap and its
pinned or free ends, S41), one record per phase per trial, the class = the KS
fold margin over the cells of ALL phases (D3 requires every phase MOC-regular;
the tail phase governs, DUTY-14/H-CON: the constraint's activity is
measure-dependent and must be reported per phase), the Newton metric on J_μ.
Cost: K phases × the per-phase cost — at the coarse rung with the wavefront
replay 2-4 s per gradient per phase, so K = 12-24 phases ≈ 1 min per gradient,
one walk in an hour. Gates:
 G2-1 μ = δ (one phase, the uniform M 1.5 line) reproduces the S41 records
       bit-for-bit;
 G2-2 the T3 shadow: a fixed-wall bell (shroud designed, plug given) on the
       S-H blowdown family (case A, log-uniform μ) lands on the Rao bell at
       ⟨Pc⟩ — the collapse theorem as a gate of the whole machine;
 G2-3 the T4 shadow: the untruncated ideal plug lands on the P_CJ design;
 G2-4 the "mean-of-votes ≠ vote-at-mean" reading on the CAPPED shrouded plug:
       the μ-optimum against the optimum at the mean state, with the per-phase
       corner votes (a1_cycle_corner's instrument lifted to the full contour).
Data ladder: I3 FIRST (Cantera CJ + S-H blowdown, no CFD needed, exercises the
optimiser end to end), then I2 from THOR (Stage 0), then the swirl and the
rothalpy (Stage 1) as separate, measured increments — each increment a paired
run so that its effect on the optimum is a number, not a belief.

### Stage 3 — truncation and the base per phase

The wake regime (Fiore 2019 sec. 6.1, S41 §4) is phase-dependent: the lip's
last wave and the pressure ratio move with ξ. The base-pressure convention is
chosen once and applied per phase; the free jet after the lip (S41 step 3) is
where the over-expanded tail phases vote "shorten" and the wave-passage phases
"lengthen" — the corner residual of a1_cycle_corner on the two-wall object.

### Stage 4 — the referee

MOSE_GPU with the designed nozzle attached to THOR (chamber + nozzle mesh, the
manifold-mesh line), time-averaged thrust over laps against J_μ; the flatness of
the thrust trace is T0's own mode-purity diagnostic (N-T0'). The rung-2 error
(θ-coupling discarded, D2) is MEASURED there; the wave-frame solve (B-lite,
rung 3a; azimuthal marching vs implicit BVP is choice C51, adjudicated at
implementation) is promoted only if D2 dominates (G4). The SU2 adjoint route of
docs/rde_nozzle_CFD_plan.md stays as planned and unexecuted.

## 4. Decided, and what needs the owner

Decided by the corpus (no re-litigation): the objective and its weight (O1:
duration only; temperature and line state inside the data); the frame (T0:
wave-frame data and invariants, no frame term in the thrust); the data-surface
rule (u_x > c per phase); per-phase MOC = exact quotient + declared rung 2.

Owner decisions before Stage 2 opens: (i) the data ladder order — I3 (Cantera
blowdown) first, as proposed, or THOR first; (ii) the phase count K and the
binning (uniform in θ', or refined around the front); (iii) the treatment of
unchoked phases — error-barred or the converging section meshed into the CFD;
(iv) whether the ends stay design variables under the cap (S41: the cap is
active, a longer nozzle is always better within the class) or are pinned at L.

First executable step, no decision needed: the Stage-0 census on the THOR CAv2
fields (one day; it decides (iii)).

## 5. Rough budget

Stage 0 census: 1 day; the extraction operator to the VI.1 contract: 1-2 weeks.
Stage 1 engine with its six gates: 2-3 weeks (the margin re-derivation is the
long pole). Stage 2 on the S41 carrier: 1 week to G2-1..G2-4 on I3 data. Stages
3-4 follow the CFD mesh line (manifold/nozzle) and its runs.

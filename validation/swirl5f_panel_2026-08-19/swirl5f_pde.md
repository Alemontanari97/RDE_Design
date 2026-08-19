# The five-field 2.5-D reduction of the wave-frame steady 3-D Euler system:
# exact split, residual anatomy, characteristics, bicharacteristic geometry,
# and the solution class

Author: hyperbolic-systems subagent, 2026-08-19.
Scope: analysis artifact for the proposed per-phase FIVE-FIELD upgrade
(rho, u_x, u_r, u_theta, p at d_theta' = 0 in each slice). Written to
scratchpad only; no repo file touched. Every claim carries one label from
{PROVEN-HERE, PROVEN-IN-RECORD, SCALING-ESTIMATE, HYPOTHESIS, OPEN}.
Record sources read in full before deriving: M0 [T-T0]/[S-T0P]/[T-NSW]
(docs/rde_nozzle_MASTER.md 440-560), docs/rde_nozzle_T3QS.md §1-§3,
docs/rde_nozzle_problem_book.md §8-§9, docs/rde_nozzle_N6_swirl.md,
validation/sfoundations_raws_2026-08-13/phaseD/phaseD_meanswirl_formalization.md
(D.1-D.20, S.22) with judge labels from VERDICT_phaseD_proofs1.md §3.2,
docs/choice_ledger.yaml C51, M0 [S-BLITE] (line ~1351).

------------------------------------------------------------------------------
## §0 Notation, conventions, and the two frame formulations

Cylindrical coordinates (x, r, theta), lab frame; wave azimuth
theta' := theta - Omega t (the record's phi; theta' used throughout per task).
Absolute velocity u_vec = (u, v, w) = (u_x, u_r, u_theta). Relative azimuthal
velocity w_rel := w - Omega r. Swirl invariant Gamma := r w. Meridional speed
q_m := (u^2 + v^2)^(1/2). Stagnation enthalpy h0 := h + (u^2+v^2+w^2)/2.
Rothalpy I := h0 - Omega Gamma (record D.20). Sound speed c, entropy s.
Material derivative along RELATIVE streamlines (record D.19):

    D_rel := u d_x + v d_r + (w_rel / r) d_theta'.

Gas model: as pinned of record (frozen-composition thermally perfect,
p = rho R_g T, h = h(T), gamma(T); phaseD §0). Everything below that uses
only dh = T ds + dp/rho and c^2 as a free positive symbol is EOS-GENERAL;
statements are marked.

TWO equivalent formulations of "steady in the wave frame" exist and MUST NOT
be conflated (this distinction resolves the task's Coriolis question in §2):

 (A) ABSOLUTE-VELOCITY / WAVE-FIXED-COORDINATE form (the record's D.17
     convention): fields F(x, r, theta'), unsteady lab Euler with
     d_t -> -Omega d_theta', absolute velocity components retained.
     NO fictitious forces appear; the frame enters only through the
     independent variable. [PROVEN-IN-RECORD: phaseD D.17, DEFINITION.]

 (B) ROTATING-FRAME / RELATIVE-VELOCITY form: dependent variables
     (rho, u, v, w_rel, p); steady Euler in the rotating frame WITH
     centrifugal force rho Omega^2 r e_r and Coriolis force
     -2 rho Omega e_x x u_rel. This is what the task's item 1 asks for.

Both are written below and their exact equivalence is PROVEN-HERE (§1.3).

------------------------------------------------------------------------------
## §1 The exact steady 3-D Euler system in the wave frame

### §1.1 Formulation (A): absolute velocity, conservative form

Start from lab-frame unsteady compressible Euler in cylindrical coordinates,
conservative (r-weighted) form; then substitute d_t -> -Omega d_theta',
d_theta -> d_theta' (chain rule for theta' = theta - Omega t at fixed
(x, r): d_t|_theta = d_t'|_theta' - Omega d_theta'; wave-frame steadiness
is d_t' = 0). Because r is independent of theta', the substituted term
-Omega d_theta' U = -(1/r) d_theta' (Omega r U) folds into the azimuthal
flux, producing the RELATIVE azimuthal flux with advective factor w_rel.
The exact system, per row (all PROVEN-HERE by direct substitution; each
azimuthal flux is verified against the record in §2.3):

  MASS:
    d_x(r rho u) + d_r(r rho v) + d_theta'( rho w_rel ) = 0

  X-MOMENTUM:
    d_x(r (rho u^2 + p)) + d_r(r rho u v) + d_theta'( rho u w_rel ) = 0

  R-MOMENTUM:
    d_x(r rho u v) + d_r(r (rho v^2 + p)) + d_theta'( rho v w_rel )
        = p + rho w^2

  ANGULAR MOMENTUM (theta-row in Gamma form; density rho Gamma):
    d_x(r rho u Gamma) + d_r(r rho v Gamma)
        + d_theta'( rho w_rel Gamma + r p ) = 0

  ENERGY (density rho E, E = e + |u_vec|^2/2; h0 = E + p/rho):
    d_x(r rho u h0) + d_r(r rho v h0)
        + d_theta'( rho w_rel h0 + Omega r p ) = 0

Derivation of the two nontrivial azimuthal fluxes (PROVEN-HERE):
 - Gamma row: lab flux (1/r)d_theta(rho w Gamma) + d_theta p combines with
   -Omega d_theta'(rho Gamma) as
   (1/r) d_theta'[ rho Gamma w - Omega r rho Gamma + r p ]
   = (1/r) d_theta'[ rho w_rel Gamma + r p ].
 - Energy row: lab flux (1/r)d_theta((rho E + p) w) with
   -Omega d_theta'(rho E) gives (1/r)d_theta'[ rho E w_rel + p w ]
   = (1/r)d_theta'[ (rho E + p) w_rel + p Omega r ]
   = (1/r)d_theta'[ rho h0 w_rel + Omega r p ].
   This is EXACTLY the record's F_phi,rel = rho w_rel h0 + Omega r p
   (phaseD D.18, singular-part display). AGREEMENT, no discrepancy.

There are NO Coriolis or centrifugal frame sources in formulation (A): the
only sources are the geometric/axisymmetric ones (p + rho w^2 in the r-row
written with the d_r(r(rho v^2 + p)) grouping). [PROVEN-HERE, consistent
with PROVEN-IN-RECORD D.17: "no Coriolis/centrifugal fictitious forces are
introduced".]

Primitive form of (A) (PROVEN-HERE by the same substitution in the standard
primitive cylindrical equations; D/Dt = d_t + u d_x + v d_r + (w/r) d_theta
becomes D_rel):

  (P1)  D_rel rho + rho [ d_x u + (1/r) d_r(r v) + (1/r) d_theta' w ] = 0
  (P2)  rho D_rel u + d_x p = 0
  (P3)  rho D_rel v + d_r p = rho w^2 / r
  (P4)  rho D_rel w + (1/r) d_theta' p = - rho v w / r
        equivalently  rho D_rel Gamma + d_theta' p = 0
  (P5)  D_rel s = 0        (smooth regions)
  (P6)  rho D_rel h0 = - Omega d_theta' p     (energy, primitive)

(P4)-Gamma and (P6) are the record's D.19(i)/(ii) pumping identities,
machine-verified there (carrier C1/C2). [PROVEN-IN-RECORD, THEOREM
model-internal; re-derived here from (P2)-(P5) + dh = T ds + dp/rho:
rho D_rel h0 = D_rel p - d_t p|_lab-content = -Omega d_theta' p since the
lab d_t p maps to -Omega d_theta' p. EOS-GENERAL.]
Rothalpy corollary (PROVEN-HERE, one line, = record D.20):
(P6) - Omega x (P4)-Gamma gives  rho D_rel I = 0,  I = h0 - Omega Gamma.

### §1.2 Formulation (B): rotating frame, relative velocity, frame forces

Dependent variables (rho, u, v, w_rel, p), steady in (x, r, theta').
Fictitious body force per unit volume: centrifugal rho Omega^2 r e_r,
Coriolis -2 rho Omega e_x x u_rel where u_rel = (u, v, w_rel).
With e_x x e_r = e_theta, e_x x e_theta = -e_r:
  -2 rho Omega e_x x u_rel = + 2 rho Omega w_rel e_r - 2 rho Omega v e_theta.

Conservative form (PROVEN-HERE; standard rotating-frame Euler specialized
to steady axial-axis rotation):

  MASS:
    d_x(r rho u) + d_r(r rho v) + d_theta'( rho w_rel ) = 0

  X-MOM:
    d_x(r (rho u^2 + p)) + d_r(r rho u v) + d_theta'( rho u w_rel ) = 0

  R-MOM:
    d_x(r rho u v) + d_r(r (rho v^2 + p)) + d_theta'( rho v w_rel )
      = p + rho w_rel^2  +  rho Omega^2 r^2  +  2 rho Omega r w_rel
      [ = p + rho w^2 : the three frame/geometric radial sources resum
        EXACTLY to the absolute centrifugal, since
        w_rel^2 + Omega^2 r^2 + 2 Omega r w_rel = (w_rel + Omega r)^2 = w^2.
        PROVEN-HERE — first consistency check between (A) and (B). ]

  THETA-MOM (linear, density rho w_rel):
    d_x(r rho u w_rel) + d_r(r rho v w_rel) + d_theta'( rho w_rel^2 + p )
      = - rho v w_rel - 2 rho Omega r v     (per r-weighted row: sources
        x r; per unit volume: -rho v w_rel / r - 2 rho Omega v)

  ENERGY (rothalpy form; Coriolis does no work on u_rel, centrifugal is
  the potential -Omega^2 r^2 / 2):
    d_x(r rho u I) + d_r(r rho v I) + d_theta'( rho w_rel I ) = 0,
    I = h + (u^2 + v^2 + w_rel^2)/2 - Omega^2 r^2 / 2  =  h0 - Omega Gamma.
    [PROVEN-HERE: expand (w - Omega r)^2/2 - Omega^2 r^2/2
     = w^2/2 - Omega r w; identical to D.20's I. EOS-GENERAL.]

### §1.3 Equivalence of (A) and (B) — exact, no residue

PROVEN-HERE. Substitute w_rel = w - Omega r into (B) and use that Omega r
is theta'-independent, d_x(Omega r) = 0, d_r(Omega r) = Omega:

 - Mass, x-mom rows: identical term-by-term (w_rel appears only in the
   theta' flux, which matches (A) already).
 - Theta-row: d_x(r rho u w_rel) = d_x(r rho u w) - Omega r d_x(r rho u)/1
   ... precisely: r rho u w_rel = r rho u w - Omega r^2 rho u, and
   d_x(Omega r^2 rho u) + d_r(Omega r^2 rho v) =
   Omega r [d_x(r rho u) + d_r(r rho v)] + Omega r rho v.
   Using the mass row, the bracket equals -d_theta'(rho w_rel), so the
   theta-row of (B) becomes the theta-row of (A) plus
   (-Omega r)(mass row) — the Coriolis source -2 rho Omega r v splits as
   (-rho Omega r v) absorbed by the metric expansion and (-rho Omega r v)
   matching the absolute geometric source -rho v w = -rho v w_rel
   - rho Omega r v. Both bookkeepings close exactly.
 - Energy row: (B)-energy = (A)-energy - Omega x (A)-Gamma-row, an exact
   linear recombination; the Omega r p work flux in (A) cancels against
   Omega x (r p) in the Gamma-row flux.

CONSEQUENCE (used throughout §2): (A) and (B) differ by an INVERTIBLE,
theta'-independent, state-dependent linear recombination of rows plus the
w <-> w_rel + Omega r change of variable. Any statement about "the
residual" is well defined once the formulation is named; residuals map
onto each other by the SAME recombination. [PROVEN-HERE.]

------------------------------------------------------------------------------
## §2 The exact split: five-field 2.5-D operator + residual R(W)

### §2.1 Definition of the split

Let U denote the conservative state (rho, rho u, rho v, rho Gamma, rho E)
and V the primitive state (rho, u, v, w, p). Define, in formulation (A):

  FIVE-FIELD 2.5-D OPERATOR at frozen theta' = xi := every row of §1.1
  with d_theta' struck. This is EXACTLY the record's per-phase system
  D.1 (E1)-(E5) + its conservation form: continuity, both meridional
  momenta with centrifugal rho w^2/r, Gamma transport, h0 (or s)
  transport. ALL curvature/metric sources are RETAINED; ONLY d_theta'
  terms are dropped. [PROVEN-IN-RECORD D.1/D.18; verified here by
  inspection of §1.1.]

  RESIDUAL OPERATOR, conservative form, per row:
      R_cons(U) := (1/r) d_theta' [ F_theta(U) - Omega r U ]
  with F_theta the LAB azimuthal flux of the row. Explicitly (from §1.1):
      R_rho   = (1/r) d_theta'( rho w_rel )
      R_xmom  = (1/r) d_theta'( rho u w_rel )
      R_rmom  = (1/r) d_theta'( rho v w_rel )
      R_Gam   = (1/r) d_theta'( rho w_rel Gamma + r p )
      R_E     = (1/r) d_theta'( rho w_rel h0 + Omega r p )

By construction, EXACT ROW = 2.5-D ROW + RESIDUAL ROW, identically, for
every piecewise-C1 field, in smooth regions — an OPERATOR IDENTITY, not an
approximation statement. [PROVEN-HERE; identical in form to the record's
r4 identity "exact-residual(V) = 2.5D-residual(V) + K(V)" (D.18).]

### §2.2 The split derived twice and diffed

DERIVATION 1 (conservative): §2.1 above, obtained by moving every
d_theta' term of §1.1 to the right-hand side. Nothing else moves; the
sources p + rho w^2 and the Gamma-row structure are theta'-free at fixed
theta' and stay in the frozen operator.

DERIVATION 2 (primitive): strike d_theta' in (P1)-(P6) of §1.1 and
collect the struck terms:

      K_rho  := (w_rel / r) d_theta' rho + (rho / r) d_theta' w
              = (1/r) d_theta'( rho w_rel )          [d_theta'(Omega r)=0]
      K_u    := rho (w_rel / r) d_theta' u
      K_v    := rho (w_rel / r) d_theta' v
      K_Gam  := rho (w_rel / r) d_theta' Gamma + d_theta' p
      K_s    := (w_rel / r) d_theta' s
      K_h0   := (w_rel / r) d_theta' h0 + (Omega / rho) d_theta' p

DIFF OF THE TWO DERIVATIONS (PROVEN-HERE, each a one-line product-rule
computation; this reproduces exactly the record's r4 triangular
recombination identities of D.18):

      R_rho   = K_rho
      R_xmom  = K_u   + u   K_rho
      R_rmom  = K_v   + v   K_rho
      R_Gam   = K_Gam + Gamma K_rho
      R_E     = rho K_h0 + h0 K_rho
      (entropy form:  R_s-cons = rho K_s + s K_rho)

  Sample verification (energy row): (1/r) d_theta'(rho w_rel h0 + Omega r p)
  = h0 (1/r) d_theta'(rho w_rel) + (rho w_rel / r) d_theta' h0
    + Omega d_theta' p
  = h0 K_rho + rho [ (w_rel/r) d_theta' h0 + (Omega/rho) d_theta' p ]
  = h0 K_rho + rho K_h0.   QED.

The recombination is triangular over K_rho with coefficients (u, v, Gamma,
h0, s) bounded and rho bounded away from zero on the class of record:
INVERTIBLE. Hence "R = 0" and "K = 0" are equivalent; the two derivations
agree EXACTLY, with the stated dictionary. [PROVEN-HERE. Also
PROVEN-IN-RECORD: the same identities are printed in D.18 (r4, L1-5);
independent re-derivation here confirms them — a deliberate non-common-mode
check, since I derived both sides from the lab equations, not from the
record's transcription.]

### §2.3 Cross-check against the record operator D(W) and the K list

RECORD OBJECT 1 — T3QS §1:  D(W) = (1/r) d_theta'[ F_theta(W) - Omega r W ].
My R_cons(U) is LITERALLY this operator, row for row, with U = W the
conservative state. AGREEMENT: exact, including the -Omega r W flux shift
(the lab d_t in disguise). Two scope notes, honestly flagged:
  (FLAG-1, scope not discrepancy) T3QS instantiates D(W) at SWIRL-FREE
  data on the four-field 2-D state and reads its content as (a) sweep
  -Omega d_theta' W and (b) azimuthal pressure coupling (1/r) d_theta' p
  "the only content of F_theta at u_theta = 0". For the FIVE-FIELD state
  the operator formula is unchanged but two additional contents are live:
  the Gamma-row sweep of NONZERO Gamma (rho w_rel d_theta' Gamma / r-part)
  and the energy work flux Omega r p. T3QS's reading is the w = 0
  specialization of §3 below; no contradiction.
  (FLAG-2, convention boundary) D(W) contains NO Coriolis piece and NO
  geometric source — CORRECTLY: see §2.4. A transcriber moving to a
  rotating-frame relative-velocity code (formulation B) must put the
  Coriolis terms in the FROZEN operator's sources, never in D; getting
  this wrong is the same type-mismatch defect class D.18 r4 (L1-5)
  prosecutes for the advective-vs-divergence rows.

RECORD OBJECT 2 — phaseD D.18 K rows: my K_rho..K_h0 of §2.2 match the
record's six K rows SYMBOL-FOR-SYMBOL (mass sweep; x/r-mom sweep; Gamma
sweep + torque; entropy sweep; h0 sweep + work), including the per-unit-
mass normalization of the s and h0 rows (whence their rho factors in the
recombination). AGREEMENT. My derivation is independent of the record's
carrier C4 (which the record itself flags as common-mode-blind for five of
seven checks); this document therefore constitutes one independent
re-derivation of the a.c. part of the K list from the lab equations —
the content the record's G-f gap asks for (not carrier-grade: pen grade;
G-f's sympy battery remains the named discharge). [PROVEN-HERE; the
COMPLETENESS claim "no d_theta' term escaped" is proven at pen grade by
§1.1's row-by-row substitution — every d_t and d_theta of the lab system
was transformed and collected; nothing else in the lab system carries
theta-dependence.]

RECORD OBJECT 3 — front atoms. On the declared class, fronts are C1
hypersurfaces steady in theta' with generically nonzero azimuthal normal
n_theta'. My split above is CLASSICAL (smooth regions). The record defines
K distributionally with singular part n_theta' [F_theta,rel] per row
(D.18 r3/r4). My §1.1 fluxes reproduce the record's F_theta,rel entries
(in particular rho w_rel h0 + Omega r p for energy and
rho w_rel Gamma + r p for angular momentum): the atom densities implied by
my conservative split coincide with the record's. I ADOPT the record's
distributional completion at its OWN certification level: D.18 first/second
iff = THEOREM* (judge-downgraded, modulo the G-f battery; VERDICT §3.2
rows "D.18 FIRST iff", "D.18 SECOND iff"). [PROVEN-IN-RECORD at THEOREM*;
nothing here claims above that.]

DISCREPANCY SCAN RESULT: NO discrepancy found between my derivation and
the record operators (D(W), K rows, F_theta,rel entries, recombination
identities, D.19/D.20 identities). Flags raised: FLAG-1, FLAG-2 above
(scope/convention, not contradictions), FLAG-3 in §4-bis (two record
scalings for the transit angle, consistent at scaling order).

### §2.4 Where the Coriolis terms live (the task's explicit question)

PROVEN-HERE (two independent ways):
 (i) In formulation (A) no frame force exists at all (D.17), so none can
     appear in R.
 (ii) In formulation (B) the frame sources rho Omega^2 r^2, 2 rho Omega r
     w_rel, -2 rho Omega r v are functions of the STATE and of r only —
     they contain no d_theta' — so the frozen operator retains them
     ENTIRELY and the residual in (B) is again purely the azimuthal flux
     divergence (1/r) d_theta' F~_theta with the relative fluxes of §1.2.
     The (B)-residual maps onto the (A)-residual by the §1.3 recombination
     (using ONLY the frozen mass row, which the 2.5-D operator carries).
CONCLUSION: the residual contains NO Coriolis or centrifugal piece in
EITHER formulation; all frame/geometric physics sits inside the five-field
frozen operator. The "Coriolis exchange" between h0 and Gamma is not a
residual term but the PROJECTION of the one exact rothalpy transport onto
the two slice invariants — see §3, row 6, and §4.4.

------------------------------------------------------------------------------
## §3 The residual, term by term (physics and order)

Small parameters of record (all SCALING-ESTIMATE with record numbers):
  St_n = n Omega tau_n / (2 pi)  ~ 0.1-1     (per-wave Strouhal, PB §8)
  eps_theta = u_theta / (Omega r) ~ 0.15-0.2 (measured, program frame)
  f_KE = tangential energy fraction ~ 3-6%
  sigma/mu ~ 0.70 (cycle fluctuation level)
Pointwise, d_theta' V = O(1): the wave IS the azimuthal structure
(PROVEN-IN-RECORD, S.22 (g3) reformulation). The ONLY smallness is
TRANSIT-INTEGRATED: each K row, integrated along one meridional transit
within the domain of dependence, contributes O(St_n) relative to the
transported quantity (S.22 g3; the geometric proof is §4-bis). Within-row
mechanism ratios below are data-dependent O(1); orders quoted are the
transit-integrated ones.

ROW 1 — CONTINUITY.  K_rho = (1/r) d_theta'(rho w_rel).
  Physics: MASS SWEEP — azimuthal redistribution of mass by the relative
  sweep; at swirl-free data rho w_rel = -Omega r rho and K_rho =
  -Omega d_theta' rho: the lab-frame d_t rho in disguise. Each slice is
  fed the inlet phase it froze, while reality feeds it the phase lagged
  by the local transit time (the "player-piano roll vs glissando" of
  T3QS §2(a)). Sub-split: sweep part -Omega d_theta' rho [O(1) pointwise]
  + lab azimuthal drift (1/r) d_theta'(rho w) [smaller by eps_theta].
  Transit-integrated order: St_n x (1 + O(eps_theta)).

ROW 2 — X-MOMENTUM.  K_u = rho (w_rel/r) d_theta' u.
  Physics: SWEEP TRANSPORT of axial momentum — the phase-lag mechanism
  applied to the thrust-carrying field; a parcel samples a phase interval
  Delta xi = St_n during its transit instead of one frozen phase.
  Pure sweep (no pressure part: the azimuthal flux of x-momentum is
  purely advective). Order: St_n.

ROW 3 — R-MOMENTUM.  K_v = rho (w_rel/r) d_theta' v.
  Physics: SWEEP TRANSPORT of radial momentum / meridional turning:
  phase-to-phase differences in streamline curvature arrive late. Feeds
  the centrifugal readjustment (the frozen operator's rho w^2/r responds
  to swept-in Gamma changes at the wrong phase). Pure sweep. Order: St_n.

ROW 4 — THETA-MOMENTUM (Gamma row).
  K_Gam = rho (w_rel/r) d_theta' Gamma + d_theta' p.   Two mechanisms:
  (4a) SWEEP of angular momentum, rho (w_rel/r) d_theta' Gamma: azimuthal
       drift of the swirl stratification across phases. Zero at exactly
       swirl-free data; O(eps_theta) relative to row-2 sweep at record
       swirl levels.
  (4b) AZIMUTHAL PRESSURE TORQUE, d_theta' p: INTER-SECTOR PRESSURE
       COUPLING — hot post-wave sectors push azimuthally on cold pre-wave
       sectors. This is the UNIQUE smooth-region source of Gamma in the
       exact flow (D.19(i): rho D_rel Gamma = -d_theta' p) and therefore
       the SWIRL-GENERATION channel the five-field slice cannot see:
       generated swirl is generically non-free-vortex (T3QS §2(b), the
       N6-3 entry point). The five-field upgrade CARRIES Gamma once
       injected through the interface data, but its in-nozzle
       regeneration by d_theta' p remains a residual effect.
  Order: (4a) St_n eps_theta; (4b) St_n x O(1) on the pressure scale of
  the wave (sigma/mu ~ 0.7 makes d_theta' p first-order on the cycle).

ROW 5 — ENTROPY.  K_s = (w_rel/r) d_theta' s.
  Physics: SWEEP of the entropy stratification (hot/cold sector
  interleaving; fill/product interfaces arriving phase-lagged). Pure
  sweep in smooth regions; at fronts the s-row atom is the entropy
  production m[s] on azimuthal-normal sheets (record D.18 r4, singular
  leg — adopted at its THEOREM* label). Order: St_n on the O(1) entropy
  contrast of the cycle.

ROW 6 — ENERGY (h0 row).
  K_h0 = (w_rel/r) d_theta' h0 + (Omega/rho) d_theta' p.  Two mechanisms:
  (6a) SWEEP of stagnation enthalpy (azimuthal energy flux): the
       conservative atom rho w_rel h0 — enthalpy carried across sector
       boundaries by the relative sweep.
  (6b) WAVE WORK, (Omega/rho) d_theta' p: the lab-frame unsteady pressure
       work d_t p / rho seen through the wave frame — the wave-rotor /
       pressure-exchange mechanism by which the rotating pressure field
       does work on the flow; conservative counterpart: the flux
       Omega r p (torque x rotation rate — pressure torque acting at
       frame speed).
  EXACT LINKAGE (PROVEN-HERE, one line):
       K_h0 - Omega (K_Gam / rho) = (w_rel / r) d_theta' I,
  i.e. in the rothalpy variable the residual is PURE SWEEP — the torque
  and work parts cancel identically. The reduction's energy error and its
  swirl error are NOT independent: the exact flow transports the single
  invariant I = h0 - Omega Gamma, the slice transports h0 and Gamma
  separately, and the splitting error is the proportional pumping pair
  D_rel h0 = Omega D_rel Gamma (record D.20 CONSEQUENCE — reproduced
  here from §2.2's rows). This is the precise sense of "Coriolis
  exchange": an O(St_n)-per-transit exchange between h0 and Omega Gamma
  at fixed I, mediated by d_theta' p.
  Order: (6a) St_n; (6b) St_n x (Omega Gamma / h0) with
  Omega Gamma / h0 ~ 2 sqrt(f_KE / (2 f_KE)) ... honest version:
  Omega Gamma / h0 = (Omega r / u_theta) (u_theta^2 / h0) x ... =
  (u_theta^2/h0) / eps_theta ~ (2 f_KE)/eps_theta ~ 0.3-0.8 of h0-scale
  per unit sweep — first-order, not cosmetic. [SCALING-ESTIMATE from the
  named numbers.]

SUMMARY TABLE (conservative atom = what the distributional front reading
prices at fronts; per D.18 the atom density is n_theta' [F_theta,rel]):

| Row | K (primitive) | F_theta,rel (conservative) | Physics |
|---|---|---|---|
| mass | (1/r)d'(rho w_rel) | rho w_rel | mass sweep |
| x-mom | rho(w_rel/r)d'u | rho u w_rel | sweep of axial momentum |
| r-mom | rho(w_rel/r)d'v | rho v w_rel | sweep of radial momentum |
| Gamma | rho(w_rel/r)d'Gamma + d'p | rho w_rel Gamma + r p | swirl sweep + inter-sector torque (swirl generation) |
| s | (w_rel/r)d's | (entropy flux) | entropy sweep (+ front production atoms) |
| energy | (w_rel/r)d'h0 + (Omega/rho)d'p | rho w_rel h0 + Omega r p | enthalpy sweep + wave work (rothalpy split) |

------------------------------------------------------------------------------
## §4 Characteristic analysis of the five-field 2.5-D system

### §4.1 Symbol and characteristic variety (derived, then checked vs record)

Primitive system A_p d_x V + B_p d_r V = S, V = (rho, u, v, w, p), from
D.1 (E1)-(E5) with the pressure row Dp - c^2 Drho = 0. Symbol along the
meridional covector n = (n_x, n_r), u_n := u n_x + v n_r, acting on
V^ = (rho^, u^, v^, w^, p^):

  mass:   u_n rho^ + rho (n_x u^ + n_r v^)            = 0
  x-mom:  rho u_n u^ + n_x p^                          = 0
  r-mom:  rho u_n v^ + n_r p^                          = 0
  th-mom: rho u_n w^                                   = 0
  p-row:  u_n p^ + rho c^2 (n_x u^ + n_r v^)           = 0

Determinant (PROVEN-HERE, computed by cofactor expansion):

  det M(n) = rho^3 u_n^3 ( u_n^2 - c^2 |n|^2 ).

Sources (centrifugal rho w^2/r, geometric -rho v w/r) are zeroth-order:
they do NOT enter the symbol. Setting n = (-lambda, 1) recovers the record
pencil det(B_p - lambda A_p) = (v - lambda u)^3 [(v - lambda u)^2
- c^2 (1 + lambda^2)] and n = e_x gives det A_p = rho^3 u^3 (u^2 - c^2).
[AGREES with PROVEN-IN-RECORD D.3(a),(b),(c) (machine-verified,
n6_swirl_kernel.py Part A) including the rho^3 normalization remark.
Gamma appears NOWHERE in the symbol: D.3(c), swirl deforms solutions
through sources and state, never the characteristic geometry.]

Characteristic families: u_n = 0 — the STREAMLINE, multiplicity THREE,
carrying the transported triple (s, h0, Gamma) (D.2); u_n = +-c|n| — the
two MERIDIONAL MACH lines, real iff q_m > c.

### §4.2 The x-marching well-posedness condition — derivation, not assertion

Three logically distinct conditions (the record's C1/C2 hierarchy, here
DERIVED for the five-field system):

 (a) HYPERBOLICITY of the (x, r) system: real Mach characteristics
     <=> q_m > c (from the discriminant of the acoustic factor).
 (b) SYMBOL INVERTIBILITY of x = const: det A_p != 0 <=> u not in
     {0, +-c}. Necessary, NOT sufficient for a march (D.3(a) rename).
 (c) SPACELIKENESS of x = const (the actual marchability criterion).
     Derivation via the ray cone: for the acoustic eikonal
     q(n) = u_n^2 - c^2 |n|^2, bicharacteristic ray directions on
     q = 0, |n| = 1 are
        dX/dsigma = grad_n q = 2 u_n u_m - 2 c^2 n = 2 c ( +- u_m - c n ),
     i.e. the ray cone is { u_m + c e : e a meridional unit vector }
     (the steady Mach cone around the meridional velocity u_m = (u, v));
     the streamline ray is u_m itself. x = const is spacelike iff EVERY
     ray crosses it in one direction, i.e. iff the x-components
     u + c e_x are one-signed over all |e| = 1:
        min over e of (u + c e_x) = u - c > 0   <=>   u > c.
     The streamline ray needs u > 0, implied. Hence

        X-MARCHING WELL-POSEDNESS  <=>  u_x > c   (AXIAL supersonicity),

     NOT q_m > c (which gives hyperbolicity but admits u < c states where
     the cone straddles the plane: e.g. u = 0.5c, v = 1.2c has q_m > c
     and no march), and NOT total Mach > 1 (|u_vec| > c with u_x < c
     licenses nothing — record D.5(iii) total-Mach hazard; monitors must
     never audit M_tot). Note u_x > c => q_m > c automatically: the
     marching condition is strictly the strongest. On a CURVED data
     surface with meridional unit normal n_m the same cone argument gives
     u_m . n_m > c, i.e. M_n > 1 (record D.4 curved clause; margin of
     record m_n(xi) = ess inf_y (M_n - 1)). Frame invariance: u, v, n_m,
     c all invariant under axis rotations => the criterion is identical
     in every frame ([T-NSW](b)).
     [PROVEN-HERE; AGREES with PROVEN-IN-RECORD D.4/D.5, T-NSW. Swirl
     enters the CRITERION nowhere (D.3(c)) but the STATE: at fixed
     (h0, s, u, v, r) with u > 0, |Gamma| /= 0 cools the state and RAISES
     the margin (D.5(ii), gamma(T)-exact under AUD-c2T) — the five-field
     upgrade is margin-benign at fixed meridional data.]

Symmetrizability: the system is Friedrichs-symmetrizable wherever rho,
c > 0 (standard Euler symmetrizer extended by the two extra transport
rows, which are already diagonal advection): under u > c the x-march is a
symmetric-hyperbolic evolution and local well-posedness follows from the
standard theory. [PROVEN-HERE at the statement level — the symmetrizer is
the classical one; the semiglobal-in-x statement inherits the D2.5
conditional exactly as in G12-S1/N6-1: PROVEN-IN-RECORD (N6-1
consequences), conditional import declared.]

### §4.3 Axis and inner-wall regularity

The class of record is ANNULAR (H-ANN: r_min > 0; phaseD §0), so the axis
is OUT OF CLASS for the certified engine; the statements below govern the
named exception (spike/plug tip closure, aft apex on the axis) and are
labeled individually.

 (i) AXIS r -> 0 (smooth closure). For a velocity field C^1 in Cartesian
     coordinates, axisymmetry forces v = O(r), w = O(r), hence
     Gamma = r w = O(r^2)  and  u_theta -> 0 linearly.
     Sources: rho w^2 / r = O(r) -> 0, rho v w / r = O(r) -> 0: the
     five-field system is REGULAR at the axis iff Gamma vanishes
     quadratically on the axis streamline. [PROVEN-HERE, elementary.]
 (ii) FINITE-ENTHALPY (weaker) condition. Bernoulli (D.2(iii)):
     h = h0(psi) - q_m^2/2 - Gamma(psi)^2 / (2 r^2). Boundedness of h
     along a streamline reaching r = 0 requires Gamma -> 0 at least
     LINEARLY in r (Gamma^2/r^2 bounded). Gamma = O(r^a): a >= 1 finite
     enthalpy (u_theta bounded), 1 <= a < 2 bounded but non-smooth
     (vorticity singular on the axis), a = 2 fully regular solid-body
     core. [PROVEN-HERE.]
 (iii) SPIKE TIP with Gamma_wall != 0: if the inner-wall streamline
     carries nonzero Gamma to a tip at r = 0, NO regular solution exists
     there: w = Gamma/r blows up and h -> -infinity — the classical
     vortex-core / vacuum-core singularity. The physical resolution
     (annular core, cavitation to the table floor h_min, or unsteady
     core) is OUTSIDE the S1 class: the design engine must either
     verify Gamma -> 0 toward the inner streamline in the data or close
     the tip with a DECLARED core model. Core-size scaling: h reaches
     h_min at
        r_core ~ Gamma_tip / sqrt( 2 (h0 - h_min - q_m^2/2) ).
     With the record's tangential energy fraction f_KE ~ 3-6% at the
     interface radius R_int and most of h0 converted to q_m^2/2 in the
     nozzle, r_core / R_int ~ sqrt( f_KE h0 / (h0 - q_m^2/2 - h_min) ),
     lower-bounded by sqrt(f_KE) ~ 0.17-0.25 when little enthalpy
     remains — NOT negligible. [SCALING-ESTIMATE, derivation displayed;
     HYPOTHESIS that the tip streamline carries interface-level Gamma —
     Gamma may decay toward the inner wall in real data; the monitor is
     the D.14 TRIPLE spread on the inner rows.]
 (iv) INNER WALL r = r_b(x) > 0 (in-class): slip BC only; Gamma is
     transported along the wall streamline (D.2). No singularity, but
     free-vortex-like AMPLIFICATION w = Gamma/r is maximal at r_min —
     the total-Mach hazard (D.5(iii)) and the swirl-KE debit concentrate
     at the inner wall; audits must use M_x / M_n there, never M_tot.
     [PROVEN-IN-RECORD D.5(iii) + PROVEN-HERE (monotonicity of Gamma/r
     in r at fixed Gamma).]

### §4.4 Rankine-Hugoniot conditions for Gamma across in-slice fronts

In-slice fronts are meridional curves; as 3-D objects at frozen xi they
have n_theta' = 0. Two types (record §0 classes, re-derived here):

 MASS-CROSSING (u_n != 0): RH rows give [rho u_n] = 0;
 theta-row: [rho u_n w] = 0  =>  [w] = 0  =>  [Gamma] = 0
 (w is tangential to every meridional front: swirl passes through
 in-slice shocks UNCHANGED — the oblique-shock tangential-velocity
 theorem in the theta-direction). Energy row: [rho u_n h0] = 0 =>
 [h0] = 0. Entropy: jumps upward under arc H-CVX, discharged
 gamma(T)-exact (G_fund > 1 closed form). Hence across in-slice shocks
 the five-field system conserves Gamma AND h0 SEPARATELY.
 [PROVEN-HERE, two-line jump algebra; AGREES with PROVEN-IN-RECORD
 D.2 front clauses.]

 CONTACT (u_n = 0): only [p] = 0 forced; [w], [Gamma], [s], [h0] free —
 slip lines carry arbitrary swirl jumps (fill/product interfaces,
 triple-point shear layers). [PROVEN-IN-RECORD D.2/§0 C-fronts.]

 RELATION TO D.20 (the rothalpy statement): in the EXACT 3-D flow a
 wave-steady mass-crossing front with azimuthal normal component
 n_theta' != 0 conserves ONLY I = h0 - Omega Gamma:
 m [h0] = -sigma_n [p], m [Gamma] = -r n_theta' [p] with lab normal
 front speed sigma_n = Omega r n_theta', so [I] = 0 while [h0] and
 [Gamma] are individually NONZERO in proportion to n_theta' [p].
 The in-slice case is the n_theta' = 0 specialization: sigma_n = 0
 => [h0] = 0 and [Gamma] = 0 separately. So the reduction's front
 bookkeeping SPLITS the one exact front invariant [I] = 0 into two —
 exactly the smooth-region D.20 splitting statement carried to fronts —
 and the difference is priced by the residual front atoms
 n_theta' [F_theta,rel] (here n_theta' [rho w_rel Gamma + r p] and
 n_theta' [rho w_rel h0 + Omega r p]). [PROVEN-IN-RECORD D.20
 (mass-crossing leg THEOREM*, twice independently re-derived, carrier
 queued G-a) + PROVEN-HERE consistency of the n_theta' = 0 limit.]

------------------------------------------------------------------------------
## §4-bis Bicharacteristic geometry of the reduction

### §4-bis.1 Rays of the FULL 3-D wave-frame steady system

The steady 3-D operator's advective velocity in wave-fixed coordinates is
the RELATIVE velocity  w_vec := (u, v, w_rel)  (§1.1 primitive form:
D_rel). Characteristic variety, covector zeta with physical components
(zeta_x, zeta_r, zeta_theta) (zeta_theta = (1/r) d_theta' of the phase):

   det = const x (w_vec . zeta)^3 [ (w_vec . zeta)^2 - c^2 |zeta|^2 ]

(the §4.1 computation with the third direction restored; the multiplicity-3
advective root now carries s and the two transverse shear/vorticity modes,
whose invariant combinations along rays are s and I). [PROVEN-HERE at pen
grade — the same cofactor computation with n replaced by the 3-covector;
consistent with the record's 3-D usage in T-NSW and S-BLITE (G12-L1-3D is
the record's named symbolic carrier candidate for exactly this).]

RAY FAMILIES (PROVEN-HERE from the eikonal, as §4.2):
 - ADVECTIVE (streamline) rays: direction w_vec — the relative
   streamlines. With w_rel ~ -Omega r (1 - eps_theta) DOMINANT over
   (u, v) in the chamber and comparable in the nozzle, these are
   HELICES of pitch angle tan(beta) = u / |w_rel| winding OPPOSITE to
   the wave motion.
 - ACOUSTIC rays: the cone { w_vec + c e : e a 3-D unit vector },
   real and one-sided around w_vec with Mach half-angle
   alpha = arcsin(c / |w_vec|) wherever |w_vec| > c — the hyperbolic
   region of [T-NSW](a), whose boundary |w_vec| = c is the CJ surface
   (the causal firewall). The rays are helical bundles around the
   advective helix.

### §4-bis.2 The true domain of dependence and its azimuthal winding

Fix an interior nozzle point P = (x_P, r_P, theta'_P) with the L4 margin
u > c along the march. The TRUE domain of dependence of P is the union of
backward rays from P to the data surface Gamma_d — a WOUND (helical) cone.
Azimuthal winding of each ray, parameterized by x (legitimate since every
backward ray has dx/dsigma < 0 ... i.e. monotone x under u > c):

   d theta' / dx  =  (ray azimuthal component) / ( r x (ray x-component) )

 - Advective ray:  d theta'/dx = w_rel / (r u), so over one transit
      Delta theta'_adv = INT w_rel / (r u) dx
                       = - Omega INT dx / u  +  INT w / (r u) dx
                       = - Omega tau_n ( 1 - O(eps_theta) ),
   tau_n = INT dx/u the convective residence time (PB Def. 8.1). In
   units of the sector angle 2 pi / n:
      |Delta theta'_adv| / (2 pi / n) = n Omega tau_n / (2 pi) x (1 - O(eps_theta))
                                      = St_n (1 - O(eps_theta)).
   THE SWEPT ANGLE PER TRANSIT IS THE PER-WAVE STROUHAL — this is the
   geometric MEANING of St_n. [PROVEN-HERE; identical to
   PROVEN-IN-RECORD PB §8 "Delta theta_sweep / (2 pi / n) = St_n"; the
   correction factor is the lab drift, generically smaller by
   eps_theta ~ 0.15-0.2.]
 - Acoustic rays: azimuthal component w_rel + c e_theta in
   [w_rel - c, w_rel + c], x-component u + c e_x in [u - c, u + c] > 0
   under the margin. Hence the winding of any acoustic ray is bounded by
      |d theta'/dx| <= ( |w_rel| + c ) / ( r (u - c) ),
   and the FULL backward cone from P meets Gamma_d in an azimuthal ARC of
   width
      Delta theta'_dom = St_n x (2 pi / n) x C_geo,
      C_geo in [ 1 - O(eps_theta) ,  (1 + c/|w_rel|) u/(u - c) ]:
   an O(1), MARGIN-CONTROLLED geometric factor (it degenerates only as
   the margin u - c -> 0, consistent with the domain of dependence
   blowing up at sonic marching). [PROVEN-HERE; SCALING-ESTIMATE for the
   bracketing constant. FLAG-3: the record states the same object twice —
   PB Def. 8.1 via tau_n = INT dx/u and S.22 (g3) via
   Delta phi_transit ~ (w_rel/r)(L/W) — which agree at scaling order and
   differ by O(1) on strongly turned streamlines (u vs q_m in the
   denominator); both are the same St_n up to the C_geo class above.
   Consistent, no discrepancy; named because a future carrier should pick
   ONE definition and derive its bars.]

### §4-bis.3 What the per-phase slice does to the domain of dependence

The frozen five-field operator at theta' = xi is a PDE in (x, r) only:
its symbol has no zeta_theta, so every bicharacteristic of the slice
system has d theta'/dsigma = 0 — the rays are the MERIDIONAL PROJECTIONS
(streamline u_m, Mach cone u_m + c e with e in the meridional plane) and
the slice's domain of dependence of P is the plane backward Mach triangle
in {theta' = xi}. [PROVEN-HERE, immediate from §4.1.]

THEREFORE: the reduction replaces the true WOUND cone (azimuthal width
St_n x sector x C_geo) by its MERIDIONAL SECTION (azimuthal width ZERO).
The truncated azimuthal extent — the data the slice never consults — is
exactly St_n sectors' worth of upstream phase information per transit:

   St_n  =  (azimuthal width of the truncated dependence domain)
            / (sector angle),  up to the margin-controlled C_geo.

Quasi-steadiness (St_n -> 0) is precisely RAY-SLICE ALIGNMENT: the wound
cone collapses onto the meridional plane. At the record's St_n ~ 0.1-1
the misalignment is marginal-to-O(1) — the reason rung 2 is not
self-licensing and carries the O(St) corrector obligation (PB §8).
[PROVEN-HERE (geometry); PROVEN-IN-RECORD (the licensing consequence).]

### §4-bis.4 Mechanism-to-ray-family map

 - SWEEP TRANSPORT (K_u, K_v, K_s, sweep parts of K_rho, K_Gam, K_h0;
   T3QS mechanism (a)) lives on the ADVECTIVE (helical streamline) family:
   it is the phase-lag of transported quantities (s, I, momentum content)
   along rays that wind by St_n sectors per transit while the slice
   assumes zero winding.
 - INTER-SECTOR PRESSURE/ACOUSTIC COUPLING (d_theta' p in K_Gam,
   (Omega/rho) d_theta' p in K_h0; T3QS mechanism (b)) lives on the
   ACOUSTIC cone family: pressure signals with e_theta != 0 crossing
   sector boundaries — the azimuthal APERTURE of the Mach cone. The slice
   RETAINS in-plane acoustics (e meridional) and AMPUTATES the azimuthal
   aperture; the amputated signals are the swirl-generation and wave-work
   channels (§3 rows 4b, 6b). The B2 subcritical/acoustic-lag channel of
   T3QS §3 is this family in the unshielded sectors.
 [PROVEN-HERE as a classification; the two-mechanism split itself is
 PROVEN-IN-RECORD (T3QS §2) — the five-field version adds rows 4a/6a to
 mechanism (a).]

### §4-bis.5 Helical foliations: C3 of record and the C51 azimuthal march

Record status: [T-NSW] Consequences name the condition hierarchy — C1
hyperbolicity (|w_vec| > c) does NOT license an axial march; C2 axial
marching = u_x > c; "C3 = any time-like foliation, helical in the wave
frame, never constructed = N6". Choice ledger C51 records the
blind-surfaced alternative: azimuthal MARCHING of the periodic orbit,
"symmetrizable-hyperbolic in alpha where |u_theta - Omega r| > a"
(VERDICT_contract_and_L4R1 D-5), adjudication owed at rung-3a
implementation time. [PROVEN-IN-RECORD.]

Derivation of the azimuthal-march condition (PROVEN-HERE, agrees with
C51): a surface theta' = const has unit normal e_theta; by the §4-bis.1
symbol its spacelikeness condition is |w_vec . e_theta| > c, i.e.

      |w_rel| = |u_theta - Omega r| > c :

exactly the C51 regime condition. In CJ-shielded operation this holds on
the wave-attached hyperbolic domain ([T-NSW](a): |w_rel| ~ D_CJ > c
behind the front... more precisely the marching domain of record sits in
|w_rel| > c); it FAILS on the CJ locus |w_rel| = c itself and in the
whole band |w_rel| < c including the co-rotation locus w_rel = 0.

STRUCTURAL OBSERVATION (PROVEN-HERE, new): the two degeneracy loci of the
C51 march are EXACTLY the two kernel families of the record's D.18 second
iff — H-NC excludes interior of {|w_rel| = c} (azimuthal acoustic
disturbances stationary in the wave frame: the march's characteristic
incidence) and H-WR excludes interior of {w_rel = 0} (the larger
co-rotation kernel: the march's normal velocity vanishes). The hypotheses
that make "K = 0 iff degenerate axisymmetric" true are the same loci on
which an azimuthal march degenerates. The reduction-residual kernel and
the marchability boundary are ONE geometric object.

WHAT A HELICAL-FOLIATION MARCH WOULD RESTORE (the C3/C51 payoff, stated
exactly):
 (i) ALL d_theta' terms — the march evolves entire meridional planes in
     theta', so K is not dropped but INTEGRATED: both residual mechanisms
     (sweep transport AND inter-sector acoustic coupling) are carried
     exactly; the domain of dependence honored is the true wound cone of
     §4-bis.2 (the march follows the winding instead of truncating it).
 (ii) The UNSPLIT invariants: rothalpy I transported as one quantity, no
     h0/Gamma splitting error; front invariant [I] = 0 with the full
     n_theta'-dependent RH (§4.4) — fronts become helical surfaces
     computed as part of the solution (the fitted inherited sheet
     becomes an unknown of the march, cf. [S-BLITE]'s per-station sheet).
 (iii) The periodic orbit structure: marching one sector 2 pi / n in
     theta' with periodic closure replaces the per-phase FAMILY by ONE
     orbit; the per-phase 2.5-D solves are then its theta' = const
     slices, and the reduction error is measurable a posteriori (the
     record's B-lite reading: "the cheap exact meter of the rung-2
     sweep/D2 residual" — note [S-BLITE] achieves this by AXIAL 3-D
     marching under u_x > c, an ALREADY-LICENSED C2 route; the C51
     azimuthal march is the C3-flavored alternative with a DIFFERENT
     regime condition |w_rel| > c and a different failure set).
 (iv) What it does NOT restore: validity outside its regime — the march
     dies structurally at |w_rel| <= c (C51 note of record), i.e.
     precisely at the CJ surface and any co-rotating pockets; a general
     C3 foliation (leaves tilted between e_theta and e_x, normal
     nu = cos(chi) e_theta + sin(chi) e_x, spacelike iff
     |w_rel cos(chi) + u sin(chi)| > c) can interpolate between the C2
     and C51 conditions and pick, pointwise, whichever margin is
     positive — the never-constructed C3 object is exactly this
     chi-field foliation; its construction (a global spacelike foliation
     with helical leaves and periodic closure) is the N6-flavored open
     item. [OPEN: existence/construction of a global C3 foliation for
     record-class data; the pointwise leaf condition above is
     PROVEN-HERE.]

------------------------------------------------------------------------------
## §5 Solution class for the five-field per-phase problem

STATEMENT (HYPOTHESIS LIST — the well-posedness class; each item labeled).
The five-field per-phase problem is posed in the PIECEWISE-SMOOTH
FITTED-FRONT class: V = (rho, u, v, w, p) piecewise C^1 on cl(D) with a
declared front skeleton, under:

 (SC-1) GEOMETRY: D bounded Lipschitz meridional domain, ANNULAR:
    r_min > 0 (H-ANN of record). Axis-reaching extensions (spike tip)
    only with §4.3 conditions (Gamma = O(r^2) smooth / O(r) finite-h) or
    a declared core model. [HYPOTHESIS; record §0.]
 (SC-2) DATA SURFACE: Gamma_d axisymmetric C^1, SPACELIKE with margin
    m_n = ess inf_y (M_n - 1) > 0, M_n = (u n_x + v n_r)/c (curved
    clause); data rows (M_in meridional, theta_in, s, w or Gamma, h0
    profile-grade) in BV cap L-infinity, piecewise C^1; state recovery
    under AUD-cp + AUD-c2T + AUD-hRANGE (unique, all Mach). [HYPOTHESIS;
    the recovery uniqueness is PROVEN-IN-RECORD D.13 THEOREM.]
 (SC-3) MARCH REGION: u > c on the closure of the march domain (axial
    supersonicity — §4.2; equivalently every station surface spacelike).
    This is the L4 interface class + margin propagation. [HYPOTHESIS,
    audited; criterion PROVEN-HERE/IN-RECORD.]
 (SC-4) FRONT SKELETON: finitely many C^1 front curves, two types:
    T-fronts mass-crossing with Lax inequalities + MAJDA UNIFORM
    (Kreiss-Lopatinskii) stability — for the five-field system the front
    symbol determinant is proportional to u_n^3 (u_n^2 - c^2) (N6-1(a)
    analogue at the front; PROVEN-IN-RECORD, machine-verified), nonzero
    inside Lax, degenerating exactly at characteristic incidence; RH
    per §4.4 ([Gamma] = 0, [h0] = 0, [s] > 0 under arc H-CVX, discharged
    gamma(T)-exact G_fund > 1); C-fronts (contacts/slip lines) with
    [p] = 0, tangential jumps free. [HYPOTHESIS list; the RH content
    PROVEN-HERE/IN-RECORD; Majda uniform stability per front is a
    PER-DATASET AUDIT, not a theorem.]
 (SC-5) TRANSPORT STRUCTURE: W... q_m > 0 with H-REACH (every streamline
    of the region meets Gamma_d exactly once) => H-FIB, giving the
    psi-representation s(psi), h0(psi), Gamma(psi) (BV in psi across
    contacts) that the design closure consumes. [HYPOTHESIS; sufficiency
    PROVEN-IN-RECORD D.2 THEOREM.]
 (SC-6) EOS: frozen thermally perfect gamma(T) closure with the finite
    table audits; every front-admissibility use of convexity discharged
    by G_fund = 1 + (gamma-1)(gamma + T gamma')/(2 gamma) > 1.
    [PROVEN-IN-RECORD D.2 r3.]
 (SC-7) WELL-POSEDNESS CONTENT under (SC-1)-(SC-6): local-in-x existence
    and uniqueness of the piecewise-C^1 solution with fitted T-fronts by
    Majda-type shock-front theory transposed to the x-as-time reading,
    extended semiglobally in x by Li Ta-tsien-class estimates under the
    margin; the swirl rows add two diagonal transport equations and do
    not modify the pencil (D.3(c)) — the swirl-free machinery applies
    verbatim. THIS IMPORT IS A FUNCTION-SPACE STEP inheriting the D2.5
    conditional [C-D25U] exactly as G12-S1/N6-1 declare. [HYPOTHESIS
    (named import); structure PROVEN-IN-RECORD N6-1; no new assumption
    introduced here.]
 (SC-8) CONTACT CAVEAT (the honest wall): in classes CONTAINING
    C-fronts, uniqueness is NOT unconditional — supersonic vortex sheets
    are only weakly/neutrally stable (Coulombel-Secchi) with instability
    windows, and multi-D admissible weak solutions on contact data are
    non-unique by convex integration (Chiodaroli-De Lellis-Kreml).
    Therefore the class statement is: EITHER a declared slip-line-free
    sub-scope (auditable per dataset by front census), OR contacts
    carried as FITTED tracked fronts with per-front stability audit and
    uniqueness claimed only within the declared front skeleton.
    [PROVEN-IN-RECORD S.22 (g2b) as the sharpest known obstruction;
    restated here as a class clause, not solved.]
 (SC-9) RESIDUAL ACCOUNTING: the per-phase solution is exact for the
    REDUCED operator; every claim about the 3-D flow prices the residual
    of §2-§3 in transit-integrated form (O(St_n) with the §4-bis
    wound-cone geometry) — the S.22 bound (SCHEMA of record, T-RED's
    input contract) is the named instrument; nothing here upgrades it.
    [HYPOTHESIS discipline; S.22 PROVEN-IN-RECORD at SCHEMA.]

------------------------------------------------------------------------------
## §6 Claim register (this document)

| # | Claim | Label | Where |
|---|-------|-------|-------|
| 1 | Exact wave-frame 3-D system, formulation (A), conservative + primitive, with relative azimuthal fluxes (incl. rho w_rel Gamma + r p, rho w_rel h0 + Omega r p) | PROVEN-HERE (agrees with record D.17/D.18) | §1.1 |
| 2 | Rotating-frame formulation (B) with centrifugal + Coriolis; radial sources resum to rho w^2/r; energy row = rothalpy conservation | PROVEN-HERE | §1.2 |
| 3 | (A) <=> (B) exact equivalence via invertible recombination + mass row | PROVEN-HERE | §1.3 |
| 4 | Split exactness: exact = 2.5-D + R as operator identity; derived twice (conservative/primitive); diff = triangular recombination over K_rho, invertible | PROVEN-HERE (reproduces D.18 r4 identities independently) | §2.1-2.2 |
| 5 | R(W) == record D(W) (T3QS §1) row-for-row; K rows == record D.18 list symbol-for-symbol | PROVEN-HERE cross-check; NO DISCREPANCY; FLAG-1 (T3QS swirl-free scope), FLAG-2 (frame-convention transcription trap) | §2.3-2.4 |
| 6 | No Coriolis/centrifugal piece in the residual, either formulation | PROVEN-HERE | §2.4 |
| 7 | Residual enumeration: 6 rows, mechanisms (mass/x/r sweep; Gamma sweep + inter-sector torque = swirl generation; s sweep; h0 sweep + wave work), with orders in (St_n, eps_theta, f_KE) | PROVEN-HERE (identities) + SCALING-ESTIMATE (orders) | §3 |
| 8 | Rothalpy residual is pure sweep: K_h0 - Omega K_Gam/rho = (w_rel/r) d'I | PROVEN-HERE (agrees with D.20) | §3 row 6 |
| 9 | Five-field symbol det = rho^3 u_n^3 (u_n^2 - c^2 n^2); Gamma leaves the symbol | PROVEN-HERE (agrees with machine-verified D.3) | §4.1 |
| 10 | X-marching well-posedness <=> u_x > c (not q_m > c, not M_tot); curved surface M_n > 1; frame-invariant; derived via ray cone | PROVEN-HERE (agrees with D.4/T-NSW) | §4.2 |
| 11 | Axis regularity: Gamma = O(r^2) smooth / O(r) finite-h; spike-tip vortex-core obstruction + core-radius scaling r_core/R_int >~ sqrt(f_KE) | PROVEN-HERE (conditions) + SCALING-ESTIMATE (core size) + HYPOTHESIS (tip Gamma level) | §4.3 |
| 12 | In-slice RH: [Gamma] = [h0] = 0 across mass-crossing fronts; free across contacts; = n_theta' -> 0 limit of D.20's [I] = 0 with the split priced by the front atoms | PROVEN-HERE + PROVEN-IN-RECORD (D.20 THEOREM*) | §4.4 |
| 13 | 3-D ray families helical; advective winding per transit = St_n sectors (1 - O(eps_theta)); full dependence-domain width = St_n x sector x C_geo, C_geo margin-controlled | PROVEN-HERE + SCALING-ESTIMATE (C_geo); FLAG-3 (two record scalings, consistent) | §4-bis.1-2 |
| 14 | Slice rays have zero winding; reduction truncates the wound cone to its meridional section; St_n = truncated azimuthal width / sector angle (geometric meaning of Strouhal) | PROVEN-HERE (agrees with PB §8, S.22 g1+g3) | §4-bis.3 |
| 15 | Mechanism map: sweep -> advective family; inter-sector coupling -> azimuthal aperture of acoustic cone | PROVEN-HERE (classification) | §4-bis.4 |
| 16 | Azimuthal-march spacelikeness <=> |w_rel| > c (= C51 condition); its degeneracy loci == D.18's H-NC/H-WR kernel loci (new structural identification) | PROVEN-HERE | §4-bis.5 |
| 17 | Helical-foliation march restores: all K terms, wound-cone causality, unsplit rothalpy, helical fitted fronts, periodic-orbit structure; dies at |w_rel| <= c; general C3 leaf condition |w_rel cos chi + u sin chi| > c | PROVEN-HERE (conditions) + OPEN (global C3 foliation construction) | §4-bis.5 |
| 18 | Solution class SC-1..SC-9 (fitted-front piecewise-smooth, Majda-type), with the contact non-uniqueness wall carried as a class clause | HYPOTHESIS list (imports named: [C-D25U], Majda/Coulombel-Secchi audits; g2b wall PROVEN-IN-RECORD) | §5 |

END OF ARTIFACT.

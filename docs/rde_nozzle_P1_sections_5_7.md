# P-1 DRAFT SECTIONS §5, §6 AND §7 — full text of record
# "Cycle-averaged variational nozzle design for rotating detonation
#  engines: exact steadification, a collapse dichotomy, and certified
#  performance bounds"

Status: DRAFT TEXT OF RECORD (2026-07-17, [F1/P-1], session S10) for
sections §5, §6 and §7 of the skeleton of record
(docs/rde_nozzle_P1_skeleton.md, commit 6263c22), companion to the §2/§4
text of record (docs/rde_nozzle_P1_sections_2_4.md, S8). Sources: M0
(theorem statements and proofs — in conflict, M0 wins), D3 (rigor
classes, §10quater), D2 (citations), D4 (novelty contingencies), the
claims registry (docs/claims_registry.yaml — claims cited by registry ID
per SCAFFOLD §5). Acceptance rules (a)-(e) of the skeleton applied PER
SUBSECTION: each subsection closes with an audit line
[Class | Falsifier | Carrier | Gamma status].

CLASS REFRESH vs the skeleton (declared): the skeleton (S5) lists §5.1
as SCHEMA with "named gaps P3, G12". The S6/S8 rigor campaigns UPGRADED
those objects — [T-T7FS], [T-P3], [T-G12S1] are now THEOREM* inheriting
the single named conditional [C-D25U] (+ [C-MAJDA] across fitted
fronts). The paper text below states the CURRENT classes of record from
the registry; the honesty content ("what remains conditional") is
preserved, sharpened from "gaps" to "named inherited conditionals".

NAMING GUARD (inherited from the §2/§4 text, applied): Lemma T3-A/B/C =
the lemmas inside Theorem T3's proof; "P-2 Lemma A"/"P-2 Lemma B" = the
companion paper's bridge lemmas. No unqualified "Lemma A/B" below.

SUBMISSION DISCIPLINE (rule (d)): submission gated by M1 + G5; all
novelty wording is QUERY-BOUNDED; the Kraiko & Osipov PMM 34(6) 1970
contingency is ADJUDICATED (full text read 2026-07-22, containment
mode, mandatory citation — see §4.5; status sync of record S14). Their
"varying flight conditions" contouring remains the closest known
multi-regime cousin of the cycle average; G5 remains the standing gate.

==============================================================================
## §5 The averaged optimality system and the weighted transversality (**')

### §5.1 Stationarity structure: per-phase adjoints, shared wall, shared endpoint

The variational problem delivered by §2-§4 — maximize J[Sigma] =
Int F[Sigma; s(xi)] dmu(xi) over admissible contours Sigma, per-phase
steady Euler constraints, per-phase mass flow fixed, shared geometric
constraints — has a stationarity system whose structure is the paper's
implementable core [T-T7FS]. Three blocks:

(a) PER PHASE (a.e. xi): the per-phase adjoint Euler system. In the
piecewise-smooth MOC-regular class S1 it reduces to the classical
closed form of thrust-optimal contouring: the optimal control surface
is the phase's terminal characteristic, and along it the first
integral

    f2 = V cos(theta -/+ alpha)/cos(alpha) = -lambda2(xi)

identifies the phase's mass-flow multiplier with lip data [T-P3]. The
identification of this classical machinery WITH the continuous adjoint
is the companion paper's bridge (P-2 Lemma A; §5.3).

(b) SHARED WALL: Int_Xi G_xi(x) dmu(xi) + lambda_L g_L(x) = 0 for a.e.
x on the wall, with G_xi the phase's Hadamard shape density. The
reading is the paper's central design fact: NO phase satisfies its own
wall condition — the mu-average does. A cycle-optimal wall is not the
optimal wall of any operating point.

(c) SHARED ENDPOINT — the WEIGHTED transversality (**'):

    Int_Xi (dF/ds_E)[Sigma; s(xi)] dmu(xi) = 0,

which factorizes as R(xi) . w(xi) with R the classical corner residual
(the single-phase Rao endpoint condition) and w > 0 a geometric-
kinematic weight.

  +--------------------------------------------------------------+
  | BOXED WARNING (the implementable form). The weight w(xi) is  |
  | phase-independent EXACTLY in the T3 collapse class — there,  |
  | and only there, (**') reduces to the naive unweighted        |
  | average of the classical corner conditions. Everywhere else  |
  | THE NAIVE AVERAGE IS WRONG: averaging the per-phase optima,  |
  | or averaging the unweighted corner residuals, produces a     |
  | contour that satisfies no optimality condition of the        |
  | averaged problem. Every implementation must use (**'). The   |
  | repo's wrong-averaging rejectors exist precisely to keep     |
  | this distinction executable (§5.2); the -2.39% stale eps*    |
  | class struck in §4.3 was exactly a naive-mean artifact.      |
  +--------------------------------------------------------------+

Doctrinal remark (D2 §b0, carried verbatim): in the classical corpus
the ambient pressure enters the variational problem ONLY through the
endpoint transversality — never through the field equations. The
averaged problem inherits this: Pa appears in (**') and nowhere else,
which is why the whole cycle-dependence of the endpoint condition is
carried by the weight-and-residual factorization.

Non-smoothness is handled, not hidden: topology-switch phases are
mu-measure-zero with F continuous across them, so differentiation
under the cycle integral survives moving switches (boundary terms
cancel); persistent kinks take Clarke subdifferentials.

Rigor status (stated in the paper's honesty voice): differentiation
under the cycle integral — hence that (b)+(c) are genuine L^1(dmu)
statements and (P)(ii) is a rigorous necessary condition — is
THEOREM* [T-T7FS], inheriting the ONE named analytic conditional of
the program (uniform semiglobal stability of the S1 solution map,
[C-D25U]); the multiplier function lambda2(xi) = -f2(lip data) is
THEOREM* [T-P3] (unique, measurable, L^inf(dmu)) in shock-free S1,
inheriting [C-MAJDA] across fitted fronts; the multi-D fitted-shock
shape calculus reduces to the verified 1-D theory within S1
[T-G12S1]. One conditional spine, stated once, inherited by ID — not
a diffuse cloud of caveats.

[Class: THEOREM* ([T-T7FS], [T-P3], [T-G12S1] — inherits [C-D25U],
[C-MAJDA]); the (**') factorization itself is derived structure |
Falsifier: certified margins with a phase family whose derivative
dominates no L^1 envelope (contradicts the uniform estimate); computed
lambda2(xi) drifting from -f2(lip) beyond margins | Carrier: proofs
M0 Part III T7 + docs/rde_nozzle_T7_P7_functionspace.md +
docs/rde_nozzle_P3_multipliers.md; wrong-averaging rejectors in
run_all groups (vi)/(xii) | Gamma status: EOS-GENERAL — the
stationarity system and (**') use no equation of state; the closed
form of f2 is EOS-general (P-2 Lemma A, only Gibbs along the
isentrope + the definition of c^2; claim C12, rule (e) primary form).]

### §5.2 The executable quasi-1D reduction — and its EOS-general carrier

With only the exit-area degree of freedom (the quasi-1D rung on which
§6-§7 live), blocks (b)-(c) degenerate to a single scalar condition
[T-T7RED]: the weighted transversality becomes

    <P_E(eps; xi)>_mu = Pa,

the mu-average of the per-phase exit pressures at the shared area
ratio eps equals ambient. Two forms of this condition must be kept
apart, because the difference is the paper's gamma discipline in
miniature:

- The PRIMARY form solves <P_E(eps; xi)>_mu = Pa on the REAL area-ratio
  inversion per phase — P_E(eps; xi) computed on the Cantera
  frozen-CJ-products isentrope, gamma(T) varying along the expansion.
  This is the form the record carries: eps*_real = 3.49-3.52 across
  the PR = 1-90 grid of §7 (run_all group (xii), [T-T7RED] carrier;
  numbers of record in data/phase_diagram_real.json).
- The CLOSED FORM NPR(eps*) = <Pc>/Pa is the gamma = const evaluation
  of the same condition. It is DEMOTED to a declared oracle: the paper
  uses it as a known-answer check, never as a solver step.

The executable rejector culture applies here with full force: the
wrong-averaging rejector (group (vi)) rejects the naive unweighted
mean (the -2.39% class of §4.3), and the group-(xii) carrier verifies
that the unweighted mean does NOT reproduce the weighted eps* beyond
derived bars — the boxed warning of §5.1 is a test, not a sentence.

[Class: THEOREM [T-T7RED] (executable reduction; EOS-general primary
carrier) | Falsifier: the wrong-averaging rejector — the unweighted
mean reproducing the weighted eps* beyond bars would kill the
distinction | Carrier: run_all groups (vi) and (xii);
data/phase_diagram_real.json (eps*_real of record) | Gamma status:
EOS-GENERAL primary (real isentrope inversion); NPR(eps*) = <Pc>/Pa
= declared gamma-const oracle (claim C13, rule (e): the corner<->eps
closed-form bijection is FORBIDDEN as a solver step — engine pin M0
VI.4bis(iii)).]

### §5.3 Pointer to the companion bridge (P-2)

The identification of the classical Rao/Kraiko machinery with the
continuous adjoint — characteristic surface = adjoint closure surface,
f2 = transported adjoint invariant, corner conditions = endpoint
transversality — is the companion paper's content (P-2 Lemma A, with
the discrete side P-2 Lemma B: reverse-mode AD of the fitted MOC march
IS the transposed adjoint sweep). This paper consumes only the
assembly of those per-phase objects into (**'). The classes of record:
per-phase classical system and kernel/transport propositions THEOREM
([T-LEMA-CL], [T-A2], [T-A3], machine-verified carriers); component
identifications THEOREM*/pending the O3.3 numeric residual [C-O33].

[Class: pointer (content lives in P-2; classes as in registry) |
Falsifier: O3.3 term-match on a TOC case | Carrier: X-PA1/X-P2A1
symbolic carriers (suite groups (xiii)/(xiv)) | Gamma status:
EOS-general per the P-2 audit of record.]

==============================================================================
## §6 Certified bounds: the sonic-capped ceiling and the executable ladder

### §6.1 The geometry-free, topology-free ceiling

For ANY solid set S in ANY topology sector, under choked frozen feed
[T-GB]:

    J[S] <= J_ideal = Int F_id(s(xi); Pa) dmu(xi),

with F_id the thrust of complete isentropic per-streamtube expansion
of phase xi to ambient: shocks only lower exit velocity at given
(mdot, h0, s) per tube; misalignment only loses axial projection.
J_ideal depends on (cycle family, Pa) alone — the ceiling of the bound
ladder, independent of shape AND topology, and therefore the common
yardstick against which every sector of the constrained problem (P)
is measured. The weaker published relaxation (integral inlet fluxes
with redistribution allowed) is Efremov-Kraiko 2004: B_EK >= J_ideal
>= J — cited as the precedent rung above ours.

[Class: THEOREM [T-GB] (proof M0 Prop. 7, appendix A4) | Falsifier:
any admissible exit scan beating the capped formula beyond table-noise
bars (executable rejector) | Carrier: run_all group (viii) ladder |
Gamma status: EOS-GENERAL — V_id = sqrt(2[h0 - h(s, Pa)]) in h(s, P)
form (claim C14, rule (e) primary form).]

### §6.2 The sonic cap: naive complete expansion is not a bound

A contribution of this paper in its own right (claim C15): the naive
"complete expansion to Pa" reading of F_id is NOT a bound below the
critical pressure ratio. The dF/dA_e sign argument behind it covers
only the supersonic branch: on subcritical phases
(1 < Pc/Pa < ((gamma+1)/2)^(gamma/(gamma-1))) the exit matching Pa is
SUBSONIC, and moving from the sonic exit toward it along the subsonic
branch loses thrust monotonically (dF/dA_e = Pe - Pa < 0 there).
The sonic exit strictly beats naive full expansion — executable
counterexample gamma = 1.15, Pc/Pa = 1.3, Delta-CF = +0.0070. The
correct per-streamtube ceiling is complete expansion CAPPED AT THE
SONIC STATE. With the cap the bound is restored and, at eps level,
exactly attained by the per-phase relaxation (int-max == ceiling,
dual-route verified); the naive form is REJECTED by test on the four
subcritical Table-1 rows (choke_margin < 1). Every bound statement in
this paper carries the cap or the explicit hypothesis "min-cycle
NPR >= critical" — including the published S-H spike closure, whose
free branch uses the naive form and therefore inherits the hypothesis
(§7.4 shows what happens when it is violated).

Why this matters for RDEs specifically: a blowdown cycle with
PR = Pc_max/Pc_min large ALWAYS has deep-subcritical tail phases at
low altitude — the regime where the naive ceiling silently stops
being a ceiling is not exotic, it is every cycle's tail.

[Class: THEOREM [T-GB sharpening] | Falsifier: the four subcritical
rows — the naive form must be REJECTED there (a passing naive form
would falsify the cap's necessity) | Carrier: run_all group (viii),
src/thrust/bounds.py, data/bounds_ladder.json | Gamma status:
EOS-GENERAL — the cap criterion is re-verified executably at gamma(T)
(cap located by inverting the monotone w(P) = h + c^2/2); the g=1.15
counterexample is the calorically-perfect oracle instance (claim C15).]

### §6.3 The executable ladder and the measured price of the caloric idealization

The eps-level ladder of record is

    bell <= int-max == capped ideal <= B_EK,

verified dual-route to <= NQ*eps_mach on the 18-row Table-1 anchor,
with M1 duality-gap-zero attainment on the supercritical rows — and,
after §7's diagram, on EVERY Pa > 0 cell at eps_max >= knee. Two
measured deltas of record turn hypotheses into numbers with rejectors:

- THE GAMMA PURGE DELTA. The ceiling's executable primary route is
  EOS-GENERAL (Cantera frozen-CJ-products isentrope; closed forms
  demoted to oracles). On the 12 finite-Pa rows the real gamma(T)
  ceiling sits 4.4% (H2) to 7.9% (RP-1) BELOW the frozen-gamma_s
  closed-form oracle (bars ~0.002%, all significant): the price of
  the caloric idealization AT CEILING LEVEL is now a measured number,
  not a modeling caveat. Known-answer rejector: a constant-cp
  synthetic gas through the same route reproduces the closed forms to
  4.7e-7 (derived tol 1e-6); a corrupted route is rejected. Vacuum
  rows are declared T-floor-truncated LOWER-BOUND instruments.
- THE EQUILIBRIUM BRACKET [T-EQBR]. The shifting-equilibrium ceiling
  (SP-equilibrate isentrope, Gibbs solver, eq sound speed from
  c^2 = dP/drho along the table) sits +6.3% to +7.0% ABOVE the frozen
  ceiling on every PR (bars <= 0.003 s; constant-cp known-answer
  through the equilibrium machinery PASS; corrupted route rejected).
  The pair [frozen, equilibrium] is the executable MODEL BRACKET of
  the caloric closure at ceiling level [C-IGMIX]: any finite-rate
  computation must land inside it, and a result quoted without saying
  WHICH member generated it is under-specified by up to ~7%.

Together the two deltas bracket the honest uncertainty of every
ceiling number this paper quotes: the caloric idealization
overestimates by 4.4-7.9% (purge), and the composition closure spans
a further +6.3-7.0% (bracket). Both are carried per-row in the data
of record.

[Class: THEOREM (executable ladder, [T-GB]); THEOREM* within the
closure pair for the bracket ([T-EQBR] inherits [C-IGMIX]) |
Falsifier: dual-route disagreement > NQ*eps_mach; known-answer
failures; finite-rate computation leaving the [frozen, equilibrium]
bracket beyond bars | Carrier: run_all groups (viii)/(xi)/(xii);
data/bounds_ladder.{json,md}, data/phase_diagram_real.json | Gamma
status: EOS-GENERAL primary route with gamma_s closed forms as
declared oracles (claims C15/C16 + the purge and bracket numbers of
record; rule (e) satisfied in primary form).]

### §6.4 EAP positioning (forward pointer)

J_ideal is the total-energy rung of the ladder; the EAP metric of
Kaemming-Paxson is its pressure-coordinate, axial variant —
EAP_i(axial) <= J_ideal(total), two adjacent rungs of one ladder
(full identification in §8.1). The bound gap J_ideal - J(Sigma*) is
the honest discount on advertised pressure gain.

[Class: THEOREM-link (textual, §8.1 carries it) | Falsifier: their
Eqs. 1-8 term match | Carrier: bounds.py rung split | Gamma status:
n/a (positioning).]

==============================================================================
## §7 The eps-level phase diagram — closures, not hardware

### §7.1 Semantics first (scope statement of record, D3 §10quater(5))

This section's figure (figs/phase_diagram_op11.png: 90 cells,
eps_max x PR at fixed <Pc>, CH4/O2 20-atm anchor + vacuum sweep) is
the paper's most quotable artifact and therefore opens with its scope
statement, carried VERBATIM from the reference ledger:

  The diagram's "winner" ranks VALUE MODELS (closures) at equal
  eps_max, NOT hardware sectors of the constrained problem (P): the
  released capped plug IS the per-phase relaxation, so its dominance
  is dominance of a relaxation over a fixed member — it measures the
  PREMIUM OF ADAPTATION and is SILENT on how much of it a real plug
  retains at the true constraint vector c (truncation, base pressure
  and length are invisible at the eps rung; zero-penalty truncation
  is the spike-favorable corner). Consequently: (a) the topology of
  S*(c) is the OUTPUT of the finite sector tournament at c — not a
  priori {bell, plug, shrouded} — and bell-winning regions of (P)
  are EXPECTED at contour level (direction consistent with Paxson's
  58-70%-of-ideal truncated-plug data). (b) What each cell CERTIFIES
  toward (P) is the premium_bound device of §7.6.

No sentence of this paper reads a diagram winner as a hardware
verdict; the coherence grep enforcing this is part of the draft's
acceptance gate.

[Class: scope statement (binding semantics, [T-OP11e] scope clause) |
Falsifier: any sentence violating the grep | Carrier: the coherence
grep itself (acceptance rule (c)) | Gamma status: n/a (semantics).]

### §7.0 The constrained problem (P), in one block

Admissible set at constraint vector c (envelope, length, lip,
truncation class); uniform cone condition => finitely many topology
sectors; configurations are OUTPUTS of the sector tournament, not
inputs. The optimum delivered is the PAIR (S*, delta): a contour and
a certified globality gap, by a declared mechanism (duality-gap M1,
collapse transfer M2, structure M3, enumeration M4, tournament M5).
This is the canonical problem of record [D-P] (M0 D2.6); everything
in this section is an instrument toward it, never a substitute for it.

[Class: definition [D-P] | Falsifier: any deliverable claiming more
than the pair (S*, delta) | Carrier: the M1-M5 mechanisms as
instantiated below | Gamma status: EOS-general.]

### §7.2 Statement (1): pointwise dominance of the capped-plug closure

Under the SONIC-CAPPED adaptation closure (the T4 closure with §6.2's
cap; declared model closure [C-HT4], published as a bound precedent
by Kraiko-Egoryan), the plug family weakly dominates the fixed bell
POINTWISE in every phase, hence in every mu-average: NO cell of the
eps-level diagram has a strict bell winner. Mechanism: below release
the two candidates coincide as members; after release the capped
ideal is the per-phase argmax, pointwise >= any fixed member.

[Class: THEOREM [T-OP11e stmt (1)] (eps-level; CLOSURE ranking only
per §7.1) | Falsifier: any strict bell winner cell | Carrier: run_all
group (x), 22 checks + 8 negative controls | Gamma status: gamma-const
closed forms at the eps rung, STRUCTURE CONFIRMED at gamma(T) by the
real-route instance of §7.5bis (rule (e): the perfect-gas rung is the
oracle, the real route the primary confirmation).]

### §7.3 Statement (2): attainment — M1 gap-zero including subcritical cycles

At eps_max >= knee the capped plug coincides pointwise with the
per-phase argmax and ATTAINS the capped ceiling: duality-gap-zero
(mechanism M1) on EVERY Pa > 0 cell, INCLUDING subcritical cycles.
This extends the OP-0 attainment (8 supercritical Table-1 rows) to
the whole capped class: the "min-cycle NPR >= critical" hypothesis is
needed by the NAIVE/published closure only, never by the capped one.

[Class: THEOREM [T-OP11e stmt (2)] | Falsifier: gap > 0 at any
eps_max >= knee cell | Carrier: group (x); knee table of record |
Gamma status: as §7.2 — confirmed EOS-generally in §7.5bis.]

### §7.4 Statement (3): the published-closure artifact (a warning to users)

The PUBLISHED S-H spike closure is strictly suboptimal wherever the
cycle has subcritical phases (30 strip cells in the record), and at
the sonic-annulus cap eps_max = 1 it INVERTS the bell/plug ranking
(bell "wins" by 1.7e-2 s at PR = 90): §6.2's sonic-cap discovery
surfacing at topology level. The inversion is an executable artifact,
detected and REJECTED by the negative controls — presented here as a
warning to users of the published closure, not as a result about
nozzles.

[Class: executable counterexample [T-OP11e stmt (3)] | Falsifier: it
IS the rejected artifact (a suite in which the flip passes would be
broken) | Carrier: group (x) negative controls | Gamma status:
artifact of the gamma-const published closure; the real route never
uses that branch.]

### §7.5 Statement (4): structure of the map, and what stays conjecture

Tie region = {PR = 1} (the T3 column) u {eps_max = 1} u
{eps_max <= eps*(Pc_min): the plug never releases and equals the bell
as a member}; a capped-band with strict gap (the genuinely averaged
regime — the truncated plug problem PB-2 lives here); the M1 region
eps_max >= knee. Duty splitting is NOT expressible with the single
shared eps DOF: at contour level the "measure selects the topology"
statement OP-11 remains CONJECTURE [J-OP11], in exactly those words.
The multiplicity reading (wave count k): within the collapse class,
modes with equal <Pc> have the identical optimal fixed wall (THEOREM,
T3 affinity); under the O2 blowdown model, k co-rotating waves give
PR_k = PR_1^(1/k) — multiplicity slides the cycle ALONG the PR axis
toward the tie column, shrinking the adaptation premium (SCHEMA,
feed-closure caveat declared).

[Class: THEOREM (structure) + CONJECTURE [J-OP11] (contour level) |
Falsifier: sector tournament with certified delta-bands contradicting
the selected topology | Carrier: group (x); data/phase_diagram.md |
Gamma status: as §7.2.]

### §7.5bis The real-route instance: the diagram survives its own gamma purge

Rule (e) applied to the whole section at once (the S8 instance of
record, run_all group (xii), src/thrust/phase_diagram_real.py): the
entire 90-cell diagram is RE-DERIVED on the EOS-general primary route
— closed forms in NO primary computation. Results of record:
(i) eps*_real = 3.49-3.52 across the grid (the [T-T7RED] carrier of
§5.2, exercised at diagram scale); (ii) the real adaptation knee sits
BELOW the closed-form knee (10.38 vs ~12.9 at PR = 90): the caloric
idealization OVERESTIMATES the envelope the peak design needs — a
design-relevant sign, not a rounding; (iii) the map structure is
CONFIRMED at gamma(T): tie column, capped band, zero bell cells, M1
attainment on all 41 knee-fitting cells including the 11 subcritical
ones — statement (2) certified EOS-GENERALLY; (iv) the naive
instrument never wins and loses strictly beyond the bar at the
deepest-spread cells. The perfect-gas diagram of §7.2-§7.5 is thereby
demoted, in this paper's own terms, to the declared ORACLE of its
EOS-general twin.

[Class: THEOREM (executable, [T-OP11e] real-route confirmation +
[T-T7RED] carrier) | Falsifier: group (xii)'s six negative controls
(incl. live corrupted known-answer rejection) | Carrier: run_all
group (xii); data/phase_diagram_real.{json,md} | Gamma status:
EOS-GENERAL primary — this subsection IS the section's rule-(e)
discharge.]

### §7.6 The tournament device: what each cell certifies toward (P)

premium_bound := Isp_ideal(capped) - Isp_bell per cell — a THEOREM up
to the bell surrogate's declared C4 model-form bar: a geometry-free
upper bound on the advantage of ANY non-bell solid over that cell's
best fixed bell (max 64.7 s at PR = 90, eps_max = 1 on the record
grid, shrinking to the M1 gap elsewhere). The tournament device: a
certified sector loss band ell_sector(c) > premium_bound closes the
cell FOR the bell with a delta-certificate per D2.6(iv). This — not
the winner colors — is the diagram's contribution to (P). The first
candidate band (the empirical truncation-penalty band, ADR D4) awaits
ratification and is cited as pending, not used.

[Class: THEOREM up to declared C4 bar (premium_bound); SCHEMA (the
tournament, until loss bands land) | Falsifier: a certified sector
band <= premium_bound closing a cell (device misfire); the
premium_bound rejector in group (x) | Carrier: premium_bound field in
data/phase_diagram.json + group (x) | Gamma status: bound built on
the capped ceiling — EOS-general via §6.3's primary route.]

### §7.7 Proven limits framing the map

PR = 1 column: T3 tie (THEOREM). eps_max >= knee: T4/M1 attainment
(THEOREM* under [C-HT4]). Vacuum: no finite optimum in any sector —
eps is a SPECIFICATION, not an optimum (the vacuum area ratios in the
S-H Table 1 are correctly reported by those authors as "maximum values
used"). Tight length + large spread: the conjectured duty-split
region, outside this paper's certified rung.

[Class: THEOREM / THEOREM* / CONJECTURE as labeled | Falsifier: per
§7.2-§7.5 | Carrier: groups (x)/(xii) vacuum sweeps | Gamma status:
as §7.5bis.]

==============================================================================
## CLAIM-MAP CROSS-CHECK (acceptance rule (b))

Skeleton claim-map rows carried by this text: C12 (§5.1, class
REFRESHED SCHEMA -> THEOREM* per registry [T-T7FS], deviation
declared in header), C13 (§5.2, now with the EOS-general carrier
[T-T7RED] group (xii) — primary form upgraded from the skeleton's
gamma-const statement), C14 (§6.1), C15 (§6.2 + purge delta of
record), C16 (§6.3 + equilibrium bracket [T-EQBR], a post-skeleton
record), C17 (§7.2), C18 (§7.3 + EOS-general confirmation §7.5bis),
C19 (§7.4), C20 (§7.5), C21 (§7.6), C22 (§7.7). New records beyond
the skeleton map (to be added as rows at assembly): the purge delta
-4.4..-7.9%, the equilibrium bracket +6.3..+7.0% [T-EQBR], the
real-route diagram instance (§7.5bis) and eps*_real. Registry IDs
used: [T-T7FS], [T-P3], [T-G12S1], [T-T7RED], [T-GB], [T-EQBR],
[T-OP11e], [J-OP11], [D-P], [C-D25U], [C-MAJDA], [C-HT4], [C-IGMIX],
[C-O33], [T-LEMA-CL], [T-A2], [T-A3].

Coherence-grep gate (rule (c)): no sentence above reads a §7 winner
as a hardware verdict; the §7.1 scope statement is verbatim from D3
§10quater(5); every gamma-const object is labeled oracle/demoted;
(**') is never written unweighted outside the T3 class.

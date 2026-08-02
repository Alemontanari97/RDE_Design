# P-1 DRAFT SECTIONS §1, §3, §8 AND §9 — full text of record
# "Cycle-averaged variational nozzle design for rotating detonation
#  engines: exact steadification, a collapse dichotomy, and certified
#  performance bounds"

Status: DRAFT TEXT OF RECORD (2026-07-20, [F1/P-1], session S11) for
sections §1, §3, §8 and §9 of the skeleton of record
(docs/rde_nozzle_P1_skeleton.md), completing the body text: §2/§4 =
docs/rde_nozzle_P1_sections_2_4.md (S8), §5-§7 =
docs/rde_nozzle_P1_sections_5_7.md (S10). Sources: M0 (statements and
proofs — in conflict, M0 wins), D3 (rigor classes), D2 + lit_b0bis
(citations, all verified at the stated depth), D4 (novelty
contingencies), claims registry (claims cited by registry ID).
Acceptance rules (a)-(e) of the skeleton applied PER SUBSECTION; each
subsection closes with an audit line [Class | Falsifier | Carrier |
Gamma status]. Appendices remain at skeleton level (proof imports from
M0), declared.

CLASS REFRESH vs the skeleton (declared): §3.2 is upgraded from the
skeleton's "N6 open" to the THEOREM-GRADE SHARP boundary of the S8
rigor campaign ([T-N6-2]/[T-N6-3]); everything else keeps the
skeleton's classes.

CITATION DISCIPLINE (radical honesty, DIR-CITE): every reference below
is cited at its VERIFIED depth of record (full text / page-verified /
abstract-verified / TOC-verified), and the verification depth is part
of the citation duty. In particular Rao's IAC 1958 chapter is cited
ABSTRACT-VERIFIED ONLY — no claim below attributes to it anything
beyond its abstract.

SUBMISSION DISCIPLINE (rule (d)): submission gated by M1 + G5; all
novelty wording is QUERY-BOUNDED; the Kraiko & Osipov PMM 34(6) 1970
contingency is ADJUDICATED (full text read 2026-07-22, containment
mode, mandatory citation — see §4.5; status sync of record S14).
G5 residual due diligence (Kraiko 1979 TOC, PMM/MZhG items) remains a
standing gate.

==============================================================================
## §1 Introduction

### §1.1 The problem: one nozzle, a cycle of states

A rotating detonation engine feeds ONE fixed nozzle with a periodic
family of thermodynamic states: behind the rotating front, the
nozzle-entry stagnation pressure sweeps through a cycle Pc(xi) rather
than holding a design value. Classical variational nozzle contouring —
the exact thrust-optimal control-surface method of Rao (Jet Propulsion
28(6):377, 1958), its thrust-optimized-parabola approximation (Rao,
ARS J. 30:561, 1960), the Guderley-Armitage school, and the Kraiko
school's four contouring generations (1982, 1994, 2002, 2007; all
verified in the D2 corpus) — assumes ONE steady state. The RDE
literature's response is either AVERAGE-THEN-DESIGN (design the
classical contour at a time-averaged chamber state) or parametric CFD
sweeps; the method-of-characteristics design line for RDE nozzles
(Li, Xu, Huang, J. Propulsion Power 38:849, 2022) is likewise a
single-state design evaluated against unsteady simulation. What has
been missing is the VARIATIONAL PROBLEM THE CYCLE ITSELF POSES: which
single contour maximizes the cycle-averaged thrust, when is the
averaged habit exact, and what certificate does any answer carry?

This paper formulates that problem, proves where the field's habit is
a theorem, prices where it is not, and ships every claim with an
executable falsifier.

VARIABLE-GAMMA GENEALOGY (a citation duty of record). The
general-EOS formulation used throughout this paper is itself classical
lineage, and the duty runs to the founder: Rao's own IAC chapter
("Contoured Rocket Nozzles", Proc. IXth International Astronautical
Congress, Amsterdam 1958, Springer; DOI 10.1007/978-3-7091-4745-0_18)
states in its abstract that "the varying gas properties associated
with chemical equilibrium are accounted for in the thrust optimization
method" — variable-gamma thrust optimization is Rao himself, 1958,
for a SINGLE steady state (abstract-verified only; full text pending
acquisition, G5). The explicit EOS-general statement of the design
equations is classical as well (JOTA 10(3):133, 1972, p. 138; Hoffman
1967 for the rotational four-field machinery), and the Soviet line
states it earlier still: Kraiko 1963, Trudy VTs AN SSSR,
"Variational problems of supersonic flows of gas with arbitrary
thermodynamic properties" — TITLE-VERIFIED via the Kraiko-Osipov 1970
bibliography (ref. [2], transl. p. 1013; full text unacquired, queued
G5), so the attribution here is of FORMULATION per the translated
title, not of verified content. The exact variational-contour line
itself opens with Shmyglevskii (PMM 21(2), 1957). What is NOT
classical is the cycle: none of this line averages over a family of
states.

[Class: expository, every historical claim cited per D2 at verified
depth | Falsifier: any misattributed citation (the coherence grep
checks depth qualifiers) | Carrier: D2 + lit_b0bis verification
records | Gamma status: the genealogy paragraph IS the gamma record —
EOS-general formulation classical (Rao 1958 IAC abstract-verified,
JOTA 1972 page-verified, Kraiko 1963 title-verified), cycle-averaging
new.]

### §1.2 Prior art contained, not competed with

Two industry instruments are close enough to deserve containment
rather than comparison, and §8 proves both are coordinates/instances
of the present formalization: the Equivalent Available Pressure metric
(Kaemming & Paxson, AIAA 2018-4567) and the Stechmann-Heister-Harroun
cycle performance model (J. Spacecraft Rockets 56(3):887, 2019).
Mandatory adjacent citations carried where used: Efremov-Kraiko 2004
and Kraiko-Egoryan 2020 (ideal-adaptation BOUND precedent, cited at
T4's closure), Paxson AIAA 2022-4107 (truncated-plug benchmark),
Giles-Pierce JFM 2001 and Lozano-Ponsin, Aerospace 2025 (adjoint
banks, companion paper P-2), Hoffman 1967 (multiplier fields).

[Class: expository | Falsifier: D2 gap table G1-G17 (any containment
claim failing its verified anchor) | Carrier: §8 term-by-term maps +
in-repo 18/18 validation | Gamma status: n/a (positioning).]

### §1.3 Contributions

(a) the thrust definition chain for periodic engines, with the storage
term exactly zero in the mean ([T-TH0]; §2, claim C1); (b) EXACT
steadification of the single rotating mode — instantaneous thrust
constancy, not merely mean equality ([T-T0]; §3, C5); (c) the collapse
dichotomy: fixed-wall cycle design collapses to the classical contour
at the mean pressure ([T-T3], C8), free-boundary design is replaced by
the peak design ([T-T4], C11), each with sharpness; (d) the averaged
optimality system with the WEIGHTED endpoint transversality (**')
([T-T7FS]; §5, C12-C13); (e) a geometry-free certified ceiling with
the sonic-cap correction to naive complete expansion ([T-GB], C14-C16);
(f) the executable eps-level phase diagram with closure semantics and
the premium_bound tournament device ([T-OP11e], C17-C22); (g) an
executable certificate culture: every claim has a falsifier and an
in-repo carrier with rejectors (claim map §CM; registry-linted).

[Class: index of claims (each row carries its own class) | Falsifier:
per-claim, see §CM | Carrier: run_all groups (i)-(xv) | Gamma status:
per-claim, rule (e).]

### §1.4 Novelty statement (query-bounded)

Every component is prior art in isolation — averaging, variational
contouring, bounds, adjoints. The claim is COMPOSITIONAL: the
constructive, certificate-bearing composition (exact steadification +
collapse dichotomy + weighted averaged transversality + capped ceiling
+ closure-semantics diagram) is unpublished as of the 2026-07-16
six-strand query set of D2, extended by the S7 PMM table-of-contents
sweep (204/204 issues, 1957-1990: zero adjoint-x-contouring hits) and
the S10 lead closures. The statement is QUERY-BOUNDED, and its
Kraiko-Osipov contingency is DISCHARGED: the closest known cousin,
Kraiko & Osipov, PMM 34(6) 1970 (nozzle contouring for varying flight
conditions — a trajectory-averaged shared contour), has been read in
full (2026-07-22) and ADJUDICATED in containment mode; §4.5 carries
the structure-level containment statement and the mandatory citation,
and this revision IS the one promised against that reading. Residual
due diligence (Kraiko 1979 book TOC, PMM full texts, MZhG items) is
declared, not hidden; G5 remains the standing submission gate.

[Class: QUERY-BOUNDED novelty [PAP-P1SK context] | Falsifier: any
surfaced prior composition narrowing the declared deltas (the K-O
1970 full text is READ and adjudicated; the G5 human pass remains
standing) | Carrier: D2 query record + adjudication row 2026-07-22 +
G5_pmm_toc_sweep deliverable | Gamma status: n/a.]

==============================================================================
## §3 Exact steadification and its limits

### §3.1 The steadification theorem

THEOREM ([T-T0], proof in M0; appendix A2). For a single rotating mode
— all fields of the form g(theta - Omega t) — and any fixed
axisymmetric control surface S:
 (i)  the thrust flux F_S(t) is CONSTANT in time, not merely
      mean-equal: each annular strip's theta-integral is
      shift-invariant;
 (ii) F_S equals the identical integral of the wave-frame steady
      fields: on axisymmetric S the rotation adds only an azimuthal
      velocity, so w.n = u.n and w_x = u_x;
 (iii) the rotating-frame steady momentum balance closes with zero
      axial frame forces (Coriolis orthogonal to e_x, centrifugal
      radial).
Consequently the exact objective equals a steady 3-D wave-frame shape
functional with the rotation rate an eigenvalue-like unknown, and the
averaged rung of this paper needs no time-resolved simulation to be
exact in the mean. The free diagnostic is executable: THRUST-TRACE
FLATNESS measures distance from mode purity (any deviation flags data
outside this theorem's scope BEFORE results are used); the diagnostic
is PRACTICE, its data-side carrier arrives with the wave-frame solver
phase (declared).

[Class: THEOREM [T-T0]; diagnostic PRACTICE (pending carrier,
declared) | Falsifier: a single-mode dataset with non-flat thrust
trace (contradiction); diagnostic = the executable monitor |
Carrier: proof M0 (appendix A2); flatness monitor mandatory in every
data contract [D-CONTRACT] | Gamma status: EOS-general — the proof
uses only kinematics and the momentum balance.]

### §3.2 What steadification does NOT license (a sharp boundary)

T0 steadifies the PROBLEM; it does not transfer Rao's two-dimensional
closed-form machinery to the steadified three-dimensional swirling
flow. This boundary is now THEOREM-GRADE SHARP (upgrade vs the
program's earlier "open" wording, declared): (i) the swirl STRUCTURE
survives — meridional Mach lines unchanged, swirl transported as a
streamline invariant, kernel laws identical ([T-N6-1]); (ii) Rao's
machinery DOES extend verbatim to FREE-VORTEX swirl (uniform r u_theta,
h0, s) with the meridional speed in the classical formulas ([T-N6-2]);
(iii) beyond free vortex the pointwise control-surface closure fails by
an EXACT OBSTRUCTION IDENTITY ([T-N6-3]) — field-level adjoint
machinery is then NECESSARY, and the five-field optimality system is
the named schema [S-5F]. The paper therefore claims the exact
steadification AND the precise edge of the classical machinery's
validity on the steadified flow.

[Class: THEOREM boundary ([T-N6-1]/[T-N6-2] THEOREM, [T-N6-3]
obstruction THEOREM; assembly [S-5F] SCHEMA) | Falsifier: exhibiting a
pointwise closure beyond free vortex (contradicts the obstruction
identity) | Carrier: X-N6 / X-5F suite group (xiii) | Gamma status:
EOS-general (the N6 carriers are symbolic-sufficient and EOS-general).]

### §3.3 Spacelikeness and the causal firewall

LEMMA ([T-NSW], proof in M0; appendix A2). In the wave frame the flow
is strongly helical (w_theta ~ -D_CJ). Two distinct facts: (a) TYPE —
the steady operator is hyperbolic where |w| > c, and the relative
sonic locus attached to the wave IS the Chapman-Jouguet surface: a
causal firewall through which no downstream signal climbs in CJ
operation, grounding the frozen-feed hypothesis and locating the
coupling channels in the unshielded sectors (fill region, deflagrative
pockets, oblique-shock tail); (b) DATA SURFACES — a plane x = const is
spacelike iff u_x > c, and since w_x = u_x with c frame-invariant,
AXIAL SPACELIKENESS IS FRAME-INVARIANT. Consequences: hyperbolicity
does NOT license axial marching (the condition hierarchy is strict);
the wave-frame anchor is an implicit boundary-value problem, which
marches nothing; the huge relative swirl never enters the averaged
rung — it IS the O(St) sweep term of the corrector ([J-CT1]). This
lemma licenses the design interface: the data contract's
spacelikeness margin min(M_x - 1) is an executable admission audit
[D-CONTRACT].

[Class: THEOREM [T-NSW] (elementary chain) | Falsifier: none needed
(exact); the audit margin is the executable instrument | Carrier:
stage-A audit fields of the data contract | Gamma status: EOS-general
(c is the local frozen sound speed; no closed form).]

==============================================================================
## §8 Bridges: the formalization contains the field's metric and model

### §8.1 The EAP metric is a coordinate of the ceiling

Verified against the full text (Kaemming & Paxson, AIAA 2018-4567;
NTRS 20180006890). The industry's Equivalent Available Pressure EAP_i
is, term by term from its Eqs. 1-8, the PRESSURE-COORDINATE of this
paper's ceiling J_ideal [T-GB]: each exit segment expanded
isentropically to ambient SEPARATELY (expand-then-average — never
mixed-out-then-expand), mass-flux-weighted specific quantities
(algebraically identical to the time-integrated fluxes of O1
[T-O1]), computed in the detonation frame where "area average = time
average" — which is exactly T0(i), used there tacitly as a fact and
proved here as a theorem. Three deltas complete the containment:
(1) baseline EAP_i declares non-axial energy unavailable while its +6%
variant includes it — two adjacent rungs of the same ladder,
EAP_i(axial) <= J_ideal(total); (2) EAP carries the quasi-steady and
azimuthal-decoupling hypotheses UNSTATED and UNPRICED — the O(St)
corrector [J-CT1] is, among other things, EAP's missing error bar;
(3) EAP is the combustor-alone ceiling: the program's bound gap
J_ideal - J(Sigma*) is the honest discount on advertised pressure gain
(cf. Paxson AIAA 2022-4107: a real truncated plug delivers 58-70% of
the notional ideal). The formalization CONTAINS and COMPLETES the EAP
doctrine rather than competing with it.

[Class: THEOREM-link (textual identification against their Eqs. 1-8)
| Falsifier: their published equations (term match is checkable by any
reader) | Carrier: M0 Part III EAP remark; the axial-vs-total rung
split in src/thrust/bounds.py (group (viii)) | Gamma status:
EOS-general on our side (V_id in h(s,Pa) form); their algebra is
gamma-const — contained as the oracle rung.]

### §8.2 The S-H model's findings are instances of the theorems

Verified against the full-text-derived spec (JSR 56(3):887, 2019,
doi:10.2514/1.A34313) and validated in-repo (18/18 on their Table 1).
Concordances of record: their Eq. (4) cycle Isp IS objective
equivalence O1 [T-O1] (same mdot c* = Pc A_t pivot); their F(t) is the
pure quasi-steady rung-2 proxy — Theorem 0 [T-TH0] supplies the
missing license and the corrector [J-CT1] the missing bar, answering
their own flagged "two timescales" open item; their assumption list
maps 1:1 onto the hypothesis ledger (frozen M, gamma = H-T3.1; choked
exit = H2; exponential blowdown = the O2 measure generator [T-O2];
full-flowing bell = H-T3.2; ideal spike = the T4 closure verbatim).
THEIR THREE NUMERICAL FINDINGS ARE INSTANCES OF THE THEOREMS: the
bell optimum unchanged between detonation and constant-pressure panels
(their Fig. 9) = the T3 collapse [T-T3]; the detonation aerospike
sized by the PEAK with saturating Isp(eps) (their Figs. 10/12) = the
T4 knee/plateau [T-T4]; vacuum area ratios reported as "maximum values
used", not optima (their Table 1 note) = the vacuum no-finite-optimum
theorem. Quantitative convergence check of record: the closed-form
theorem evaluations reproduce their CEA-swept optima to 3-5% (bell)
and 6-14% (spike) at fixed phi — exactly the level warranted, since
their per-column optima re-optimize phi; the full-fidelity JOINT
(phi, eps) reproduction is the in-repo 18/18 validation (certified
phi_opt lattice x closed-form bell_opt). Their computations predate
this theory: independent corroboration, no circularity.

[Class: THEOREM-link + executable check | Falsifier: closed-form
predictions vs their Table 1 beyond the phi-fixed tolerance; the
18/18 validation rejector set | Carrier: run_all groups (ii)/(v);
data/st_opt_validation.md; M0 Part III S-H remark | Gamma status:
their model is gamma-const (declared oracle rung); the containment
statements ([T-O1]/[T-TH0]/[T-T3]/[T-T4]) carry their own gamma
records per rule (e).]

### §8.3 The equivalence ratio is an outer generator parameter

To preempt a referee objection: phi does not join the shape variables.
It is an OUTER, non-variational parameter of the DATA GENERATOR — it
moves the state family s(xi; phi) and the measure mu(phi), not Sigma;
the joint problem is NESTED, max_phi max_Sigma J, with T3/T4 valid at
each fixed phi and the outer loop certified by lattice search
(strict-neighbor certificate; no closed form exists in phi since
Isp(phi) passes through equilibrium chemistry). This is NOT the
bilevel shape-to-chamber feedback problem (out of scope, declared).

[Class: definition + certified lattice carrier | Falsifier: phi_opt
strict-neighbor certificate failure | Carrier: phi_opt lattice
(in-repo, S-H validation chain) | Gamma status: n/a (parameter
placement).]

==============================================================================
## §9 Discussion, declared limits, outlook

### §9.1 What is proven, what is conditional, what is conjectured

Proven within declared scope: the definition chain, steadification,
the dichotomy, the weighted system, the capped ceiling, the eps-level
diagram statements (§§2-7, classes per claim). Conditional: the
program's analytic residue is concentrated in ONE named conditional —
uniform semiglobal stability of the per-phase solution map [C-D25U] —
plus front stability [C-MAJDA] across fitted shocks; every THEOREM*
above inherits exactly these, by ID, and nothing else. The
discrete-to-continuum mesh limit of the adjoint identity is the named
schema [S-LBML]; the multi-D fitted-shock shape calculus reduces to
verified 1-D theory within the marching class [T-G12S1]. Conjectured:
the contour-level phase-diagram topology (duty split) [J-OP11] — the
eps rung provably cannot express it; and the O(St) corrector bar
[J-CT1], re-scoped to a steady sweep-perturbation solve for certified
periodic data. Out of reach by declared boundary: finite-rate
chemistry closed forms (the corner condition dies with the Hoffman
E-residual — the companion paper's boundary), unconditional global
optimality (excluded by theorem), 3-D non-axisymmetric machinery.

[Class: honesty index (each object carries its registry class) |
Falsifier: per-object | Carrier: claims registry + conditionals ledger
(machine-linted) | Gamma status: per-object.]

### §9.2 Generality ladder (what each flow class licenses)

Condensed from the program's ladder: single/k-wave rotating mode —
exact steadification, full certificate stack (this paper's scope);
modulated/counter-rotating regimes — periodic BVP machinery, PRACTICE
demonstrators only; multistable mode sets — per-branch optimization
under a robust (CVaR/DRO) outer layer; chaotic/mode-hopping — bounds
and robust surrogates ONLY, certificates honestly refused. The
periodicity assumption is a property of the EXPECTED DATA, never of
the algorithm: the pipeline keeps the general machinery and exploits
periodic structure at runtime only when the flatness and harmonic-decay
audits certify it (mandatory monitors in the data contract).

[Class: scope table (PRACTICE beyond row 1) | Falsifier: the
flatness/decay monitors (data outside scope is detected, not assumed
away) | Carrier: data-contract audits [D-CONTRACT] | Gamma status:
n/a (scope).]

### §9.3 Declared exposition biases

Two biases are declared rather than laundered (D7 audit): B1 — the
program attacks the averaged rung first because its assets (theorems,
oracles) live there, a schedule choice gated by promotion criteria,
not a claim that rung 2 suffices; B2 — the paper's exposition is
theorem-first with the classical (Rao-form) machinery derived as the
S1 reduction, while the companion P-2 adopts adjoint-first order; both
routes are derived from the bare problem in the respective papers.

[Class: declared-bias statement | Falsifier: D7 §5 de-biasing audit |
Carrier: D7 | Gamma status: n/a.]

### §9.4 Outlook

(1) The truncated plug under a binding length cap is the FIRST
genuinely averaged shape problem (nesting breaks strictly): armed by
the premium_bound tournament device [T-OP11e] and awaiting certified
sector loss bands. (2) The companion paper P-2 proves the classical
machinery IS the closed-form adjoint (bridge lemma), turning every
statement of §5 into implementable gradient code; the differentiable
per-phase engine that executes it is under construction with a
dual-code cross-verification discipline against an independent
Fortran MoC reference. (3) The O(St) corrector [J-CT1] prices the one
approximation of §2; its periodic re-scoping makes it a steady
linearized solve on the wave-frame anchor. (4) The certified-bounds
culture — every number from a committed script with a rejector — is
itself portable to neighboring unsteady-propulsion design problems.

[Class: outlook (no new claims) | Falsifier: n/a | Carrier: n/a |
Gamma status: n/a.]

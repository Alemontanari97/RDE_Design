# ADVISORY — RDE choking census of record (2026-08-11): five primary
# sources read IN FULL; the U3' survey base; consequences for the
# extraction contract. To be absorbed at S21 (addendum block C).

STATUS: advisory (untracked). Readings: Stechmann-Heister-Harroun JSR
56(3) 2019 (12/12 pp), Kaemming-Paxson NTRS 20180006890 (15/15 pp),
Paxson-Miki-Perkins-Yungster AIAA 2022-4107 (12/12 pp),
Harroun-Heister-Ruf JPP 37(5) 2021 (14/14 pp), Gonzalez-Viana et al.
Aerospace 12:502 2025 (17/17 pp). All page anchors below are from
these reads. The user's challenge ("un RDE non vale Sauer o simili;
il concetto di choking va analizzato profondamente") is CONFIRMED by
every source that touches the question.

## 1. WHAT THE LITERATURE ACTUALLY ESTABLISHES ABOUT RDE CHOKING

(a) STECHMANN 2019: choking is a DECLARED ASSUMPTION — p.889
verbatim (corrected at S-GAUNTLET page-verify 2026-08-11): "It is
thus assumed that the flow at the RDE exit plane is sonic at all
points in the cycle to simplify the analysis of the nozzle
performance"; throat =
channel exit plane by declaration ("thermal choking ... defines the
effective throat area. Again, it is assumed..."); the word "Sauer"
never appears; no transonic analysis anywhere. The authors flag the
two-timescale problem and oblique-shock losses as open (p.890,
Conclusion 7).
(b) KAEMMING-PAXSON EAP: the DEFINITION SHIFT of record — p.10:
choking is CYCLE-INTEGRAL, "any choking condition (i.e. maximum mass
flow rate) will have a range of axial Mach numbers... both subsonic
and supersonic portions". Their own data (Table 1 p.6, Fig. 6 p.10):
healthy-case throat-plane AXIAL Mach spans 0.86-1.33, average 0.99 —
a per-phase axially-SUBSONIC patch exists AT THE THROAT during part
of EVERY cycle even when the device is "effectively choked"; at low
PR the exit is substantially subsonic (M~0.5, p.14). Uniform M=1 is
an engineering SURROGATE justified variationally (minimizes computed
EAP, error <5.4%, Fig. 7 p.11).
(c) PAXSON-MIKI 2022: "the unsteady and spatially non-uniform flow
field ... renders common nozzle parameters such as pressure ratio,
and throat Mach number ILL-DEFINED" (p.2). Their annulus has NO
physical throat; the exit is FLUIDICALLY choked in their Q2D
solution (total Mach 1.05-1.65 per phase, Fig. 3 p.5) — but that
Mach includes the significant TANGENTIAL component; per-phase AXIAL
Mach is never shown. The chamber-nozzle DECOUPLING is an
architectural premise (exit BC discards imposed pressure when
sonic/supersonic; no coupled run), not a demonstrated result. Their
steady preliminary sizing must ASSUME "throat Mach number is 1.0"
(p.7) and misses the optimal area ratio by ~31%.
(d) HARROUN 2021: choking BYPASSED — inlet state IMPOSED one
diameter upstream of the channel exit (pressure waveform Eq. (7)
only; T = 3400 K and velocities CONSTANT, zero vorticity, p.665-666;
chamber not simulated); no sonic-surface analysis; the only "sonic"
is descriptive (p.666 "sonic jet"). Two U3'-relevant warnings:
throat RESTRICTIONS can quench detonation at rocket conditions
(p.661, via ref [9]); the applicability of mass-averaged CP models
downstream is "thrown into question" (p.661).
(e) GONZALEZ-VIANA 2025: "the presence of detonation waves creates a
dynamic environment in which the classical nozzle optimization
criterion is no longer valid" (p.14); single-cycle scope declared
(p.3).
(f) THE REPO WAS ALREADY HONEST: problem_book 149-155 concedes the
sonic set is unsteady, wave-attached, azimuthally non-planar, and
"0-D CLOSURES PRESCRIBE CHOKING, NOT GEOMETRY". The census above
turns that concession into page-anchored primary evidence.

## 2. CONSEQUENCES FOR THE EXTRACTION CONTRACT (U3 -> U3', sharpened)

C1 NO GENERIC SUPERSONIC SURFACE: the per-phase axially-supersonic
   extraction surface FAILS on part of every cycle in the healthy
   K-P case and entirely in low-PR regimes. The contract must be
   TWO-REGIME BY CONSTRUCTION: per-phase axially-supersonic patches
   -> characteristic hand-off (stage-A completeness audit); axially-
   subsonic patches -> the declared closure O1/O2/O3 path, which is
   hereby promoted from corner-case to LOAD-BEARING.
C2 THE RIGHT CRITERION IS AXIAL: Paxson-Miki's Fig. 3 shows total
   Mach; the audit must test min_xi(M_AXIAL - 1) with margin — the
   stage-A "characteristic completeness on axially supersonic
   patches" audit is exactly this; the tangential component must be
   explicitly separated (swirl in the data is admissible; it is the
   AXIAL cone that decides spacelikeness).
C3 THE DECOUPLING NEEDS A CERTIFICATE: Paxson-Miki's premise becomes
   OUR executable audit — "all normal characteristics outgoing at
   every phase on the extraction surface, else LOUD REJECT" — the
   certified version of their BC.
C4 THROAT-RESTRICTION CAVEAT (Harroun p.661): configurations with a
   physical converging throat may quench detonation; the use case
   (chamber CFD up to a throat) must carry this as a DATA-VALIDITY
   caveat, not a machinery issue.
C5 SURROGATE PRICING: the Stechmann/K-P M=1 closures our 0-D layer
   implements stay licensed as PRICED surrogates (K-P's own <5.4%
   variational bound; our choke_margin instrumentation) — no change,
   but the price is now page-anchored.

## 3. THE MISQUOTE OF RECORD (verdict-adjacent; immediate F0 fix)

The phrase "near-perfect time-averaged expansion", quoted in
docs/rde_nozzle_literature_map.md lines ~20, ~63-65, ~639 as
Harroun 2021's observation and used as the EMPIRICAL ECHO of
collapse theorem T3, DOES NOT EXIST in the paper (searched all 14
pages). The real evidence is WEAKER AND MIXED: similar
cycle-averaged pressure profiles after the recompression zone
(p.670) + quasi-cycle-averaged C_F ~ 1.25 equal for both aerospikes
(p.671, with the declared 2-D caveat) — AGAINST the paper's own
headline of NON-equivalence downstream (8x base drag p.666-667;
delayed separation p.670/672; "Neither the analytical model ... nor
the previous theory ... are appropriate" p.669). PARADOX: the T3
NOVELTY VERDICT IS STRENGTHENED (no collapse statement exists in
the paper), but the three citing lines must be rewritten with
faithful paraphrase + page anchors, and the phrase must not be
reattributed to Harroun 2019 / AIAA 2019-0197 without page-verify
(sole remaining fetch item). Also regrade P1_sections_2_4 §4.5:
acquisition duty DISCHARGED, echo regraded page-verified-MIXED;
the citable average-then-design evidence becomes "steady MOC design
at fixed NPR 13.7/19.3" (p.662).

## 3-bis. HARROUN'S QUASI-CYCLE-AVERAGED C_F — METHOD PRECISION
## (2026-08-11 evening, pages re-read by the session lead directly)

How it is built (p.670-671): a series of STEADY constant-pressure
AXISYMMETRIC (2-D) simulations of both geometries "at different
constant-pressure inflow conditions spanning the pressure ratios of
the detonation-wave cycle" -> the steady characteristic C_F(NPR)
curves of Fig. 21 (C_F = F/(P_c A_t), Eq. 10) -> "averaging the
discrete constant-pressure axisymmetric computations for each point
in time of the cycle" using the Eq. (7) waveform -> C_F ~ 1.25 for
BOTH designs, used ONLY for design ranking, with the declared 2-D /
no-3-D-inflow caveat.

TWO FACTS OF RECORD:
 (i) NO UNSTEADY C_F EXISTS IN THE PAPER: the 3-D detonation-wave
 simulations are used for flow physics (plume structure Figs. 12/14/
 18/20, base pressures Fig. 13, cycle-averaged plug pressure
 profiles Fig. 19, separation behavior); no integrated C_F or thrust
 from the unsteady runs is reported as a result (thrust appears only
 as the MESH-CONVERGENCE metric on 2-D meshes, Fig. 10, p.665), and
 no unsteady-vs-quasi-steady C_F comparison table exists. The loop
 is closed on PROFILES, not on the functional.
 (ii) THE AVERAGING CONVENTION IS UNSPECIFIED: the text says only
 "averaging ... for each point in time of the cycle" — the natural
 reading is a plain time average, but NO formula or weight is given.
 (An earlier session-lead statement that it is "unweighted, unlike
 Stechmann Eq. 4" was an OVER-READING and is corrected here: the
 convention is UNDECLARED, which is itself the finding.) Note the
 real content of the ambiguity: with P_c(t) varying,
 <C_F(t)>_time != <F>/(<P_c> A_t) — the choice of weight changes
 the number; Stechmann declares mass-weighting (Eq. 4), Harroun
 declares nothing. The literature's averaging MEASURE is not merely
 inconsistent across the school — it is partly undeclared. This is
 direct, page-anchored motivation for the program's T0/measure
 formalization (the functional's weight is a THEOREM-level object,
 not a habit).

## 4. CONTINUITY VERDICT (the user's question, settled on pages)

Full continuity, correct deltas, no phase reorder: Stechmann = the
0-D cycle-bookkeeping ancestor (Eq. 4 mass-weighted averaging ->
our functional; 18/18 Table-1 fidelity in-repo; his Assumption 3 =
our priced H2); Paxson-Miki = the shape-side ancestor (their
notional ideal = the axial mass-flux-averaged rung of our bound
ladder; their periodic hand-off = the uncertified prototype of our
interface contract; G1/G4 novelty rows faithful); Harroun = the
phenomenology ancestor (altitude-compensation and separation-delay
cites FAITHFUL AS A COMPUTED RESULT (measured-status corrected at
S-GAUNTLET page-verify: see 4-bis); the expansion-echo cite was the
one misquote). No source contradicts the program; every correction
is a rank-qualification that the certificate culture absorbs.

## 2-bis. FIXED-DESIGN FIELD COMPARISON — three items surfaced by the
## user's sharpened question (2026-08-11 late)

(i) MATCHING CONVENTION: Harroun's steady twin is matched on MASS
FLOW, not mean pressure (p.665: "a constant pressure that produced
the same mass flow as the detonation-wave case"; p.669: average
mass flow AND speed of sound identical). In THEIR lab (frozen T,u:
mdot ~ p) matched-mdot and matched-<p> DEGENERATE to the same
thing; on REAL RDE data (T, M varying) they diverge by covariance
terms cov(p, u/T) — and NOBODY in the read literature quantifies
which matching gives field similarity. Owner: T0/measure
formalization (the matching convention is part of the theorem
statement, not a habit).
(ii) MEAN SWIRL — CLAIM UNDER ADJUDICATION (2026-08-11 late; the
session lead's first formulation "the time-mean interface state
carries net Gamma != 0, a first-order omitted term" is HEREBY
DEMOTED to a hypothesis pending the dedicated expert panel, because
a CONSERVATION counter-argument exists): the wave drags gas
tangentially in its direction (per-phase u_theta = O(1), P-M p.2),
BUT under {inviscid flow, axisymmetric channel walls (cylinders
exert no theta-force), axial injection with zero angular momentum}
the cycle-averaged ANGULAR-MOMENTUM FLUX through every cross
section must vanish — so the MASS-FLUX-weighted cycle-mean of
r*u_theta is constrained to ~0, and what survives is (a) O(1)
per-phase swirl (owned by N6 + the sweep), (b) possibly nonzero
POINTWISE time-means with compensating radial structure, (c)
weighting/covariance differences between time-mean, mass-flux-mean
and the T0 measure, (d) genuine net swirl only from the
panel-adjudicated torque channels: non-axisymmetric wetted geometry
(discrete injector orifices/posts — generically NONZERO in real
hardware even with axial streams), viscous/numerical wall shear,
swirled or non-axial injection incl. backflow exchange, aperiodic
storage during mode transitions — each a DECLARED mechanism.
[CORRECTED 2026-08-11 per the mean-swirl panel: "wave-count
asymmetries" was WRONG here — unequal wave counts, counter-waves
and throat convergence are NON-channels (THEOREM-level negative,
unanimous); see ADVISORY_mean_swirl_panel_2026-08-11.md.] The T3-control-row "mean field"
construction and the stage-A angular-momentum audit follow from
whichever statement survives the panel
(mean-swirl-adjudication workflow, launched 2026-08-11).
(iii) WAVE-FRONT REFLECTIONS AT THE NOZZLE INLET: Harroun's BC
smooths the detonation front (pressure waveform only, imposed one
diameter upstream; "fine details ... not preserved", p.666), so
front-vs-wall-curvature reflection effects near the inlet are
absent from their lab AND from any steady comparison — an
unmeasured term, owner F4b (data-borne fronts, taxonomy (b)).
EXCURSION SCALE NOTE: P-M p.5 reports interface standard deviations
~70% of the means -> second-order (Jensen) corrections carry weight
(sigma/mu)^2 ~ 0.5 on whatever enters nonlinearly: "small
fluctuations" intuition does NOT apply at RDE amplitudes.

## 2-ter. THE BELL-COLLAPSE QUESTION — formal state at handoff
## (2026-08-11 late; INPUT OF RECORD for the dedicated parallel
## collapse session; contains a CORRECTION of the session lead)

(A) CORRECTION OF RECORD: the lead's repeated claims in this window
("bell: Delta-Isp ~ 0 within bars, Delta-profile ~ band level") were
anchored ONLY on in-hypothesis evidence — Harroun's p-only frozen-T
lab, Stechmann's 0-D with M=1 assumed, and OUR OWN twin (which is
vacuum-equivalent, homentropic, single-phase — i.e. INSIDE the
collapse corner BY CONSTRUCTION; the S18 +0.04% is a CORNER
measurement, not a general fact). Asserting bell-equality in the
GENERAL project case would be wrong. The user's challenge stands.

(B) SCALE-INVARIANCE ANALYSIS (the clean mechanism, to be
formalized to convergence by the dedicated session): under p-only
scaling k(xi) (Lemma T3-A, ideal-gas pin), the per-phase field is a
k-scaled copy, F(xi) = k F1 and mdot(xi) = k mdot1, hence
   Isp = F1/mdot1 — INDEPENDENT of the k-distribution:
the SHAPE optimum is identical for every phase and for EVERY
averaging convention. This is the true content of the collapse and
makes the "which mean pressure" question MOOT inside the
hypotheses. THE BREAKERS (each first-class, owned by the dedicated
session):
 (a) AMBIENT TERM, pa != 0 — FIRST-ORDER break: Isp(xi) =
     (k F1 - pa dA)/(k mdot1) depends on the whole k-distribution;
     low-k phases are overexpanded (Stechmann's own Fig. 8 remark:
     bells "significantly overexpanded before the next detonation
     wave arrives") -> the SEA-LEVEL/booster bell is GENUINELY
     OUTSIDE the collapse; only the vacuum-equivalent objective is
     protected. [ADJUDICATED S-GAUNTLET 2026-08-11, correction of
     record — this clause was TOO NARROW: fixed-wall J (T-T3
     affinity) AND ratio-of-averages Isp (under T-O1(i)+(ii)+L4)
     are ALSO protected at the argmax level, at the measure-pinned
     design point <Pc>_mu; what dies at pa != 0 is
     convention-INDEPENDENCE (average-of-ratios lands at the
     HARMONIC mean <Pc^-1>^-1), tail-governed constraint activity
     (ess-inf k), and separation (H2' exit). Sea-level verdict of
     record = "coincides, at <Pc>_mu, weight now load-bearing",
     not "no coincidence". Stechmann anchors of record: Eq. (4)
     journal p.888, JSR 56(3) 2019; quotes pp.893-895 (range tightened
     at page-verify: p.892 carries Figs. 5-7 only). The naive
     "J depends on the k-distribution at first order" is FALSE.
     See M0 T-T3-MAP.]
 (b) M/T/s PER-PHASE VARIATION: Jensen terms with (sigma/mu)^2 ~
     0.5 at RDE amplitudes (P-M p.5).
 (c) SWIRL, first vs second moment — SETTLED AT LITERATURE LEVEL
     (K-P p.7 VERBATIM: "While for most cases there is no net
     momentum associated with this non-axial momentum, there is
     some energy that is not readily available for axial thrust
     or for turbine work." — quote completed at S-GAUNTLET
     page-verify, the sentence does not end at "thrust");
     magnitudes: +6% EAPi (CFD, p.7), +3% experimental EAP (p.11).
     First moment ~ 0 by angular-momentum conservation (panel
     wf_d37cefa8-e69 adjudicating the theorem-grade hypotheses).
     RECOVERY ASYMMETRY (registered here first): Gamma = r u_theta
     conserved per streamline -> u_theta = Gamma/r -> swirl KE
     Gamma^2/(2r^2) DECAYS on outward expansion (bell/flared:
     partial natural recovery into pressure->axial) and GROWS on
     inward expansion (aerospike/plug: concentrates) — a term
     AGAINST the plug family, OPPOSITE in sign to most other
     RDE-vs-steady effects; the N6-2 free-vortex Bernoulli
     h = h0 - W^2/2 - Gamma0^2/(2y^2) carries exactly this
     mechanism per phase (field-level for general Gamma(psi) by
     N6-3). Missing executables: the axial-vs-total rung in
     src/thrust/bounds.py (reader-flagged) and the
     family-selection bookkeeping term.
 (d) SUBSONIC PATCHES (K-P Fig. 6: axial Mach 0.86-1.33 at the
     throat in the healthy case) — regime change, not perturbation.
 (e) THE T0 MEASURE: moot under scaling, DECISIVE once scaling
     breaks (time-mean vs mass-flux-mean differ by Var(p)/<p> ~
     50% at RDE amplitudes; the formal functional needs no such
     choice — that is precisely its value on the bell too: the
     mean-field methodology carries a free parameter the formal
     one does not).

(C) "CI MUOVIAMO SEMPRE NEL COLLASSO?" — NO: the current twin yes
(by construction), the RDE application no (axes (a)-(e)). The
dedicated session owns the formal map and the definitive
T3-control protocol (application backpressure, declared matchings,
both weightings where scaling is broken, derived bars).

## 4-bis. BREAKER COVERAGE INVENTORY (the user's "have we considered
## all of these?" — answered against the record, 2026-08-11 evening)

SWIRL — the best-covered breaker, via the N6 rigor attack of record
(docs/rde_nozzle_N6_swirl.md + n6_swirl_kernel.py 16/16 +
n6_fivefield_adjoint.py, all symbolic-sufficient machine-verified):
 N6-1 (THEOREM): with swirl the streamline family carries a TRIPLE
 of invariants (s, h0, Gamma = r*w); the meridional Mach lines and
 the x-marching criterion (axial supersonicity) are UNCHANGED;
 centrifugal terms are sources only.
 N6-2 (THEOREM): FREE-VORTEX class (uniform Gamma0, h0, s): Rao's
 whole control-surface machinery holds VERBATIM with W = meridional
 speed (novelty query-bounded vs Tillyaeva 1975, unacquired).
 N6-3 (sharp NEGATIVE, machine-verified): general Gamma(psi) or
 h0(psi) profiles KILL the pointwise closure — field-level
 machinery required. This is the honest boundary and the RDE-real
 case.
 N6-5F: the five-field linearized + adjoint structure (same
 characteristics, Lagrange identity, terminal gauge direction)
 verified — the adjoint side is structurally swirl-ready.
TWO FLAGS FOR THE PLAN (S21+1 absorption):
 (F-swirl-1) The ratified F2 text lists streamline transport of
 "s, h0" only: ADD the Gamma = r*w transport row + centrifugal
 sources + w-profiles in the F2a data contract (the N6-1 structure
 makes this a same-architecture extension, not a redesign; the
 interface data WILL carry swirl — P-M p.2 "significant local
 tangential velocity components").
 (F-swirl-2) Add a SWIRL-UNIFORMITY MONITOR to the stage-A audits
 (measure the Gamma(psi) spread per phase, analogous to T0
 flatness): near-uniform -> the N6-2 free-vortex class applies and
 the closed-form machinery survives swirl; else the field-level
 route is mandatory by N6-3. This turns N6's theorem pair into an
 executable data-contract dichotomy.

OTHER BREAKERS, coverage status:
 - Per-phase Mach variation: covered by design (T3-QS per-phase
   sweep + the TWO-REGIME contract of section 2); engine pending F2.
 - s/h0 stratification (contact): F2 (q;s,h0) manifold + U2; I2
   contract admits profiles; engine pending F2.
 - CONSTRAINT-ACTIVITY / SEPARATION: HONEST GAP — separation is
   viscous, the machinery is inviscid; today only slope/supersonic
   wall monitors exist. Declared scope limit of record; option =
   correlation-based separation-margin constraint at design level
   (CONSERVATIVE for RDE per Harroun's computed cycle-averaged-CFD
   delay; experimentally UNCONFIRMED at the separation location —
   "the pressure measurements ... were not densely located enough
   downstream to confirm this behavior", p.670; experiments confirm
   only the lower recompression-zone pressures); EXPLOITING
   the delay (higher max eps) requires viscous/unsteady evidence
   outside this machinery — never claimable from the inviscid tool.
 - Base/truncation: declared MODEL-CONST band (trunc 0.20
   [0.20-0.40], ADR D4, Harroun-cited); not computable by
   supersonic MoC; Harroun's 8x says the band stays wide until
   measured per instance.
 - St/corrector: in plan (F5b); the St numbers themselves are an
   audit duty (uncarried, problem book section 8).

## 5. ARRIVALS REGISTERED THIS CENSUS (fetch-list bookkeeping)

Already on disk and identified: Giles-Ulbrich SINUM 48(3) 2010
Part 1 (literature/080727464.pdf) AND Part 2 (09078078x.pdf) — the
F4b-entry acquisitions; Lozano-Ponsin Aerospace 12:494 2025
(aerospace-12-00494); Gonzalez-Viana Aerospace 12:502 2025
(aerospace-12-00502, PAGE-VERIFIED FULL READ this census); Wolanski
PCI 34 2013 review (1-s2.0-S1540748912004014); Shepherd-Kasahara
GALCIT FM2017.001 RDE thrust models (rde_model_report.pdf — choking-
relevant, reading queued); Stechmann JSR + Kaemming-Paxson NTRS +
Paxson-Miki Aviation_2022_final + Harroun JPP (parent dir, all READ
IN FULL this census). REMAINING FETCH: AIAA 2019-0197 only.

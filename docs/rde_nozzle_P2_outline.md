# P-2 OUTLINE — The bridge lemma: Rao/Kraiko optimality ≡ closed-form
# adjoint characteristics (with an executable certificate)

Status: PAPER OUTLINE OF RECORD (2026-07-16, [F1/P-2]). TIME-SENSITIVE
(risk register RK-A of D6: Lozano-Ponsin built the 2-D analytic-adjoint
bank in 2025 without citing the classical side; the identification is
cheap and scoopable). Sources of record: D2 §G14 + §b0 (page-verified
classical corpus), D3 §8 (P2 entry) + §11 (falsifier index), M0 VI.3.
Submission gated by G5 (Kraiko 1979/PMM human pass) — writing is not.

------------------------------------------------------------------------------
## P-2 FREEZE OF RECORD (dated 2026-08-11 — fired BY RULE at F1 close)

FREEZE MECHANICS: the dated trigger ratified at S22 T0 (option (b),
ISS-5 rule) fired at the F1 close decided by the user at S23 T0 (log
validation/PROGRESS_2026-08-11_S23_f1close.md; F1 counter of record:
campaign 1/2, session 2/3 — CLOSED 2026-08-11). Freeze = the numeric
content below is the PAPER'S numeric half of record at fallback-B
(two-knob S19) quality; writing proceeds; submission stays G5-gated.

NUMERIC CONTENT AT FREEZE (R5: committed-carrier numbers only —
[X-O33B] S19 campaign + S21 repaired re-run; S19/S21 logs of record):
 - f2 drift = 9.4809e-03 in the REGISTERED norm (S19, CONFIRMED by
   the S21 full re-run after the restore-bug fix), against the
   DERIVED band 1.8696e-02 (replaces the 0.03 literal; its negative
   control fires). HONEST DATUM carried into the text: the drift
   GROWS with mesh refinement (9.5e-03 -> 1.4e-02) — the
   design-class attribution is corroborated, the statement of record
   is TWO-KNOB CONVERGENCE (class enrichment knob + mesh knob), per
   §5(iv) below.
 - Corner-row class evidence: 6.6295e-02 in the committed 8-node
   class vs 2.0e-02 on the faithful Rao wall at the SAME mesh (S19)
   — the class, not the physics, sets the corner accuracy.
 - lambda_e = dJ/dy_lip bookkeeping: measured cross-design agreement
   2.803e-03 (S21 re-issue of record).
 - o32 OBJECTIVE ROW, DECLARED: the objective mesh-convergence row is
   NON-CONCLUSIVE under the pre-registered 0.5 cap (S21
   re-adjudication of record; the claim is NOT killed; named lever =
   a finer ladder — a declared residual of the paper, not a blocker).

C1 FREEZE-BLOCKER ADJUDICATION (user decision, S23 T0, of record):
FREEZE WITH DECLARED CONDITIONAL — the audit-C1 FIELD-LEVEL REJECTOR
(per-cell certification rejector at paper-claim level) remains a
NAMED CONDITIONAL with owner F2 (carrier unbuilt at freeze): every
claim in this paper consuming field-level certification carries the
conditional clause until the F2 carrier lands, and the C1 scope
qualifiers stay mandatory in the text. This is the plan's
named-conditional-with-owner pattern (generality and the SOTA modus
operandi preserved by construction — S23 user pin of record).

UPGRADABILITY (declared): F1 closed on the
certifiability-limited-under-constraint branch with the margin
INACTIVE (no outcome-I result), so the frozen numeric claims stay
two-knob S19; the F1 margin-governance machinery ([X-MGOV] derived
floors, [X-TBAK] tolerance-ball ship backoff) is citable as METHODS
content without touching the frozen numbers.

Rigor legend as in M0: THEOREM / THEOREM* / SCHEMA / CONJECTURE /
PRACTICE. Every claim below carries a class and a falsifier.

------------------------------------------------------------------------------
## 1. The claim (what the paper proves)

LEMMA A (continuous bridge; target class THEOREM* — within the S1
piecewise-smooth class, smooth supersonic region; shock/sonic edges
declared, see §6).
For the classical planar/axisymmetric thrust-optimal contour problem
(fixed mass flow, optional length constraint), the Rao 1958 / Guderley-
Armitage / Kraiko optimality machinery IS the closed-form solution of
the continuous adjoint Euler system restricted to the terminal
characteristic:
  (i)  the statement "the optimal control surface is a characteristic"
       ≡ the adjoint compatibility (characteristic) relations become
       ACTIVE precisely on Mach lines: the control surface where the
       first variation closes is the adjoint characteristic through the
       exit lip;
  (ii) Rao's first integral f2 = V cos(theta ∓ alpha)/cos(alpha) =
       -lambda2 ≡ the adjoint Riemann invariant along that
       characteristic; the isoperimetric multiplier lambda2 (mass) and
       lambda3 (length, f3 = cot(phi)) ≡ the ADJOINT BOUNDARY DATA
       (thrust-objective adjoint b.c. on the exit surface, wall b.c.
       psi·n from the slip condition);
  (iii) the corner/transversality algebra (CSTR_PA/PB of M0 VI.3, sign
       from the characteristic family) ≡ adjoint endpoint conditions;
  (iv) Hoffman's 1967 multiplier FIELDS lambda1..lambda4 (+lambda5 per
       species), which satisfy PDEs along the SAME characteristics as
       the flow, ARE the interior continuous adjoint field, and his
       a-posteriori residual E (Eq. 78) IS the adjoint-PDE residual —
       i.e. the 1967 paper already contains the continuous adjoint
       avant la lettre; the bridge makes this exact and two-sided.
Falsifier (executable): symbolic/numeric term-by-term match on one TOC
case — construct the Giles-Pierce/Lozano-Ponsin analytic adjoint on the
terminal characteristic and subtract Rao's conditions; any nonzero
residual beyond discretization kills claim (ii)/(iii) as stated.

LEMMA B (discrete bridge; class THEOREM for the transpose identity +
SCHEMA for the mesh-limit consistency statement).
Reverse-mode AD of a shock-FITTED MOC space-march is EXACTLY the
discrete adjoint characteristic sweep: the MOC march is a (block-)
triangular nonlinear system over unit processes; its reverse-AD is the
transposed triangular solve, which propagates adjoint invariants
backward along the SAME discrete characteristics (fitted fronts
differentiated as explicit unknowns, never as captured smears). Hence
"AD of a fitted MOC = Rao/Kraiko conditions evaluated discretely", with
the dot-product identity exact at machine precision by construction.
The mesh-limit statement (discrete adjoint → Lemma-A field) is SCHEMA:
it inherits the known adjoint-consistency trap (Giles-Ulbrich SINUM
48:882/905 (2010): interior smearing conditions; Lozano's mesh-divergent
inviscid adjoints) — for FITTED fronts the trap is bypassed by
construction, which is itself a citable point.
Falsifier: O3 dot-product failure at any unit process, or divergence of
the AD gradient from the Rao-condition residual as h → 0 on a smooth
family (see §5).

Scope note (honesty, stated in the paper): "adjoint = Lagrange
multiplier" is folklore at the abstract level; the CONTENT here is the
exact, term-by-term closed-form identification with the 1958-1974
contouring machinery (equation-numbered, page-verified corpus D2 §b0),
its discrete fitted-march twin, and the machine-precision certificate.
None of the three banks states or uses it (query-bounded, §3).

------------------------------------------------------------------------------
## 2. Why now (the scoop window)

Lozano-Ponsin, "On the characteristic structure of the adjoint Euler
equations and the analytic adjoint solution of supersonic inviscid
flows", Aerospace 12(6):494 (2025), arXiv:2503.13007, constructs 2-D
supersonic analytic adjoints WITH characteristic structure and does not
mention Rao/Guderley/Kraiko. The classical bank has been in print since
1967 and the quasi-1D adjoint bank since 2001. Anyone who reads both
sides can write the bridge; we have the third ingredient nobody has
(the executable certificate stack + the fitted-AD statement) and the
motive (the averaged RDE system needs the per-phase adjoint in closed
form — M0 T7(a)). D6 timeline: draft weeks 6-12 of the 90-day plan,
fast-track. P-2 can precede P-1 and cite it as "companion".

------------------------------------------------------------------------------
## 3. The three published banks (mandatory citations; none has the bridge)

B1 CLASSICAL MULTIPLIER FIELDS. Hoffman (1967) — reacting-flow nozzle
   optimization via Lagrange multiplier fields on flow characteristics;
   residual E (Eq. 78); corner bijection dies for reacting gas (p. 676).
   Supporting corpus (page-verified in-house, D2 §b0): Rao 1958 (ARS
   28:377, Eqs [1]-[15]); Guderley-Armitage; Hoffman-Scofield-Thompson
   JOTA 10(3) (1972); Scofield-Hoffman 1971 (var-gamma oracle, Table 2
   frozen thrust 2290 lbf); Kraiko school (1982/1994/2002/2007;
   arbitrary vortical inflow, arbitrary EOS).
B2 ANALYTIC ADJOINTS, QUASI-1D + SHOCK RULES. Giles-Pierce, JFM
   426:327-345 (2001): closed-form quasi-1D adjoint, adjoint continuous
   across the shock with an interior b.c. along it, sonic-throat log
   singularity (the transonic caveat we inherit, D1 §6).
B3 ANALYTIC ADJOINTS, 2-D SUPERSONIC — widened S14 to the
CHARACTERISTIC-STRUCTURE ADJOINT BANK (PAN-S14 F-PETERANC,
arbiter-confirmed): Lozano-Ponsin (2025), above, PLUS the
characteristic-compatibility line its Eq. (30) "can be shown to agree
with" (p. 7): Peter-Desideri, Phys. Fluids 34:086113 (2022, adjoint
Euler ODEs along characteristics); Ancourt-Peter-Atinault, Aerospace
10:797 (2023, adjoint + direct characteristic equations, 2-D); and
the L-P 2023 shock-jump companion (Aerospace 10:267). All three:
MANDATORY-CITE class, ACQUISITION-PENDING — no content claim until
page-verified; the distinction paragraph must cite this bank and
keep the claim = the three-way identification (classical constants =
adjoint data; f2 = the integrable invariant; reverse-AD of the FITTED
primal march = the transposed sweep, with certificates).
Query-bounded novelty claim (restate D2 §G14 verdict + queries, date
2026-07-16): no publication states Rao/Kraiko conditions ≡ closed-form
adjoint, and none states reverse-AD-of-MOC ≡ discrete characteristic
sweep with certificates. Residual risk: Russian-language PMM corpus —
exactly the G5 human pass (§7).

------------------------------------------------------------------------------
## 4. Paper skeleton (sections, with per-section rigor class)

 §1 Introduction: three banks, one bridge; RDE motivation (one page,
    points to P-1: per-phase adjoints assemble into the weighted
    averaged transversality (**')).
 §2 Setup (THEOREM-grade recall): steady Euler in S1, thrust functional
    in wall and control-surface forms (momentum-theorem equality),
    the two isoperimetric constraints; notation aligned to the
    equation-numbered corpus.
 §3 Lemma A proof: write the continuous adjoint system + b.c. for the
    thrust objective with mass-flow constraint; integrate in
    characteristic (Riemann-invariant) form in the smooth supersonic
    region; identify — term by term, with Rao's/Hoffman's equation
    numbers — conditions (i)-(iv) of §1. Corollary: Hoffman's E ≡
    adjoint residual (the 1967 certificate is Level-C avant la lettre).
    [DRAFTED 2026-07-16: docs/rde_nozzle_P2_lemmaA.md — classical side
    fully derived (8 steps, corpus-checked, THEOREM); adjoint structure
    + Prop. A1 THEOREM; (i)-(iii) THEOREM* with O3.3 PENDING; (iv)
    SCHEMA with PENDING page re-read. See D3 §8 status upgrade.]
 §4 Lemma B proof: MOC march as triangular system; reverse AD =
    transposed sweep; fitted-front differentiation (implicit-function
    rules on RH + Lax/Majda transversality); dot-product identity;
    where the Giles-Ulbrich trap would bite and why fitting bypasses it.
 §5 Numerics = the O3 oracle plan (see below).
 §6 Declared boundaries: sonic line (Giles-Pierce log singularity stays
    inside the data interface, D1 §6); shocks (G12: multi-D shape
    calculus rigor is 1-D/quasi-1D — Bressan-Marson, Ulbrich,
    Cliff-Heinkenschloss-Shenoy — cited as the honest frontier);
    reacting gas (corner dies, E = 0 replaces it — N4 ladder).
 §7 Outlook: the averaged (RDE) optimality system as the assembly of
    per-phase closed-form adjoints (bridge to P-1/P-3).

------------------------------------------------------------------------------
## 5. Oracle O3 — the executable certificate (numerics section plan)

Platform: the Phase-A1 differentiable MOC engine (G0 stack: JAX
custom_vjp with implicit rules; GENO-Fortran as independent reference,
dual-code discipline). Contour: one GENO TOC case (Rao bell) + the
Rao-1961 spike Table-1 oracle case (M_E = 2.4, theta_E = -8.25 deg,
gamma = 1.23 → eps = 3.81, X_D/R_E = 1.164, C_F = 1.58) once RaoPlug
S1/S2 is fixed.
 O3.1 Dot-product test at machine precision on EVERY unit process
      (interior, direct/inverse wall, axis, shock point): |<Jv, w> -
      <v, J^T w>| ≤ C·eps_mach with C derived from operation counts —
      tolerance derived, never magic. REJECTOR: any process failing.
 O3.2 Hoffman E-residual → 0 along the optimized contour: evaluate the
      multiplier-field residual E (Eq. 78 specialization to frozen gas)
      on the AD-computed adjoint field; convergence order must match
      the unit-process order O(h^2). REJECTOR: nonvanishing E on a
      converged optimum, or wrong order.
 O3.3 Term match: AD boundary gradient vs Rao condition residuals on a
      perturbed-contour family around the optimum (the D3 §11 P2
      falsifier line: "O3: AD-MOC dot-product + term match with Rao
      conditions"). REJECTOR: mismatch beyond discretization bars.
 PRE-REGISTERED NORMS AND LOCI (S14, PAN-S14 F-LIP, three-lens
 convergent — binding BEFORE the A1 engine produces its first number):
 (a) field-level checks (O3.2, any pointwise psi comparison) are
 evaluated in norms EXCLUDING shrinking neighborhoods of the lip/
 corner, of the sonic line/Sauer IVL, and of the axis (or weighted-L1
 downweighting them): the inviscid adjoint is generically singular at
 such loci (Lozano 2019 trailing-edge mechanism; L-P 2025 p. 3 lists
 "nozzle lips"), the sonic-neighborhood exclusion precautionary per
 Lozano-2018 pp. 4450-4451; a max-norm-to-the-lip O3.2 could FALSE-KILL
 while gradients stay accurate. O3.2 REMAINS a rejector under the
 registered norm. (b) O3.3 (gradient-level) is the PRIMARY kill
 criterion; oracle coordinates = compatibility residuals (L-P 2025
 Eqs. (30)/(31)) + the Prop. A3 f2 drift — NOT the constant-flow
 invariants (33)-(34) (valid only on uniform patches); R1^psi =
 psi1 - H psi4 retained (streamline-valid in general). (c) wrong-family
 rejector: the r+ combination must NOT be conserved. (d) NEW O3-tier
 audit: wall-adjacent adjoint convergence under refinement with a
 declared lip-exponent probe — fitted march vs the capturing control
 run scored on THESE field-level oracles (X1 exchange outcome:
 gradient-only capturing control declined as non-discriminating).
 (e) S-LBML limit target now includes the shock-FOOT adjoint condition
 (form-qualified: the control-surface thrust integrand is nonlinear in
 the state, so the Lozano-2018 taxonomy makes the foot b.c. nontrivial)
 and the characteristic-borne adjoint discontinuities of L-P 2025 —
 which the characteristic-ALIGNED fitted march can represent natively.
 O3.4 Cross-code: JAX gradient vs GENO finite differences on the same
      case (dual-route agreement).
Precedent in-repo NOW (citable as method demonstrator before A1): the
eps-level machinery already runs the same discipline — dual-route
int-max == capped ideal at NQ·eps_mach (OP-0), phase-diagram rejectors
(OP-11-eps) — the paper's certificate culture is already executable.

ADDENDUM (2026-08-06, S19 — EXECUTION NOTE, changes NO criterion and
NO band of the protocol above; it records the LOCUS on which the
protocol's own objects are defined, and one correction of record).
 (i) THE CONTROL SURFACE, stated because the campaign initially got it
 wrong. Rao's control surface is NOT the whole C+ characteristic
 through the lip: it is the piece of that C+ running from the LAST C-
 emitted by the circular throat arc — the kernel boundary, where the
 variational contour begins — up to the lip; equivalently, the C+
 traced BACK from the lip and STOPPED at the kernel boundary. The
 stationarity system (L.5) varies the control-surface data, and those
 data are free only downstream of that boundary; upstream the fixed
 throat arc determines them, so no optimality condition holds there
 and none is claimed. Measured consequence, S19 [X-O33B]: evaluated on
 the FULL C+ down to the axis, f2 drifts ~29% and the row looks
 falsified; evaluated on the classical surface it is constant to
 9.5e-03 for the S18 optimum and to 8.0e-03 for GENO's own Rao
 contour — the SAME residual for two independently obtained designs,
 i.e. the instance's discretization, not a property of either design.
 The boundary is read from the march's own topology (which wall
 segment emits the C- through each node), never from the invariants.
 (ii) NORMS. The pre-registered exclusions (lip/corner, sonic/Sauer,
 axis) are unchanged and were applied; the kernel boundary is not a
 new exclusion but the surface's own endpoint.
 (iii) SECOND FIRST INTEGRAL. (L.13), q rho W^2 sin^2(theta) tan(alpha)
 = -lambda3, is carried in the bench alongside f2 as an independent
 optimality coordinate: our instance fixes the LENGTH, so lambda3 is
 the multiplier our formulation actually owns.
 (iv) THE CORNER ROW. With the exit ordinate CONSTRAINED (the eps
 equality) the free-endpoint transversality (L.14) becomes "augmented
 density at E = multiplier of that constraint", and by the envelope
 theorem applied to the value function shared by the control-surface
 and wall formulations that multiplier IS the AD derivative
 dJ/dy_lip. The executable identity is therefore
   dJ/dy_lip == 2 pi y_E [ p_E - (1/2) rho_E W_E^2 sin(2 theta_E)
                           tan(alpha_E) ]   (pa = 0, vacuum-equivalent
 objective of record). DECLARED HONESTLY: this is an identity of the
 CONTINUUM optimum tested on a FINITE-DIMENSIONAL design, so a
 Richardson band on one instance cannot confirm it; the falsifiable
 statement of record is two-knob convergence (enrich the design class
 toward the continuum optimum; refine the mesh at a design already at
 that optimum) — see [X-O33B] and the S19 log.
 DESIGN-CLASS RESIDUE, with its procedure named (standing directive:
 procedures must be GENERAL, not case-dependent, and economical): the
 brick's wall class — 8 UNIFORMLY spaced nodes carrying a natural
 cubic spline clamped at the attachment — is an instance-tuned choice,
 and S19 measured that it, not the physics, sets the corner row's
 accuracy (6.6e-02 in that class vs 2.0e-02 on a faithful Rao wall at
 the SAME mesh). The discharge is therefore NOT "more uniform nodes":
 it is an adaptive, error-indicator-driven knot construction
 (free-knot / a-posteriori insertion, basis class fixed by the
 regularity the downstream estimate consumes), so that the class
 refines where the Rao residual actually lives and nowhere else.
 (v) CAPTURING CONTROL (item (d)). Vacuous on shock-free twins (zero
 fitted fronts); the wall/lip-adjacent probe half IS executed. The
 control proper is deferred, declared, to the shock-bearing instance.

------------------------------------------------------------------------------
## 6. Risks and dependencies (declared)

 - A1 engine timing: O3 numerics need the differentiable MOC (months
   1-6). Mitigation: Lemma A + a quasi-1D discrete demonstrator
   (closed-form Eq.-9 pipeline differentiated) can carry a first
   submission if the window closes faster.
 - G12/transonic: claims stay inside the declared S1/supersonic scope;
   the paper's honesty section is §4-§6 (this is a feature: none of
   the three banks declares the trap structure explicitly).
 - PMM/Kraiko-1979 unknowns: G5 pass may surface a Soviet antecedent of
   the identification; that DOWNGRADES novelty wording, not the
   certificate content (the falsifiers and Lemma B stay ours).
   Submission blocked until G5 verdict is in (D6 gate).

------------------------------------------------------------------------------
## 7. Venue and timeline — DECISION OF RECORD (2026-07-16, delegated by
##    the user "in modo SOTA"; evidence in the session log
##    validation/PROGRESS_2026-07-16_S4_G5venue.md)

DECISION: PRIMARY VENUE = AIAA JOURNAL, coupled with an arXiv preprint
posted IMMEDIATELY at (G5 pass ∧ Lemma-A draft ready). Rationale, with
the web-verified numbers:
 - The scoop risk (RK-A) is NOT neutralized by venue speed, because
   gate G5 blocks ANY public claim-staking (journal submission AND
   preprint alike — same due-diligence rationale). Once G5 closes, the
   arXiv preprint stakes priority within days at zero cost; after
   that, review latency no longer carries scoop risk and the venue
   should be chosen on AUDIENCE FIT and SIGNAL, not turnaround.
 - Audience fit: the bridge needs readers who BOTH cite Rao/Hoffman
   and run adjoints — that is the AIAA Journal community (Lozano's own
   adjoint mesh-divergence papers are AIAA J 2018/2019; the classical
   contouring corpus is AIAA/ARS lineage). Signal: strongest of the
   three for a theory-of-record identification.
 - Verified numbers (2026-07-16): Aerospace (MDPI) median first
   decision ~18.5 days, acceptance-to-publication ~2.7 days, APC
   2400 CHF; AIAA Journal review "six months or more" (official
   guidance). With priority secured by arXiv, the ~6 months are
   acceptable; the 2400 CHF buys nothing we still need.
FALLBACK (declared triggers): transfer to Aerospace (MDPI) if AIAA J
desk-rejects, or if review exceeds ~8 months / two rounds without
convergence — Aerospace remains apt (B3's venue, direct dialogue).
TERTIARY: JOTA (the 1972 historical loop) only if both propulsion
venues judge it "too mathematical"; wrong primary audience for design
impact, right one for the variational identity per se.
KILL/RE-EVALUATE: if the G5 pass surfaces a Soviet antecedent of the
identification, novelty wording downgrades (D4 §3 contingency) and the
format re-evaluates to AIAA J technical note; the certificates and
Lemma B remain the contribution.
 - Timeline (D6 90-day plan item 7): outline DONE (this document);
   Lemma-A draft + §3 identification weeks 6-9; Lemma B + quasi-1D
   demonstrator weeks 9-12; O3 full numerics attach at M1 (A1 engine);
   arXiv at (G5 ∧ draft); AIAA J submission immediately after.
 - Authorship/acknowledgment of the GENO corpus per repo policy.

------------------------------------------------------------------------------
## 8. Claim register (class + falsifier, one line each)

| Claim | Class | Falsifier |
|---|---|---|
| Lemma A (i)-(iii): Rao conditions = closed-form adjoint on terminal characteristic | THEOREM* (S1, smooth region) | term-by-term residual vs B2/B3 analytic adjoint on one TOC case |
| Lemma A (iv): Hoffman fields = interior adjoint; E = adjoint residual | THEOREM* | evaluate E on AD adjoint field; nonzero at convergence kills |
| Lemma B transpose identity (AD = adjoint sweep) | THEOREM (finite-dim) | O3.1 dot-product at machine precision |
| Lemma B mesh-limit consistency (fitted march) | SCHEMA | O3.2/O3.3 order + term match as h → 0 |
| No published bridge (novelty) | QUERY-BOUNDED (D2 §G14, 2026-07-16) | any citation surfacing it (incl. G5 PMM pass) |
| Certificate culture transfers to averaged system | SCHEMA (points to P-1) | (**') assembly on the quasi-1D reduction (repo test exists) |

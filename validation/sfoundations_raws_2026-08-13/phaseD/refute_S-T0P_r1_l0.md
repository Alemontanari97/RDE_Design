# REFUTE — [S-T0P]/[T-T0P] proof document, ROUND 1, LENS 0

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
(read in full). Lens: FUNCTIONAL-ANALYTIC RIGOR — spaces, operators,
compactness, trace/regularity, every quantifier. Charter: attack
statement truth, every proof step, hypothesis completeness, the claimed
rigor LABEL (over-label = finding), variable-gamma status, falsifier
rejection ability, and ABSENCE (ignored literature routes /
counterexamples). Calibration sources read this window:
docs/rde_nozzle_cauchy_bvp_transfer.md ([T-XSON]/[T-XWALL]/[S-XCONV]/
[T-XWS]/[C-XBVP] declarations, §§1-8).

VERDICT (round 1): REPAIRABLE. One labeled proposition is FALSE AS
STATED with a concrete physically-relevant counterexample (F1); one
stratum of the main theorem is over-labeled on a mis-cited conditional
(F2); three genuine proof gaps in the uniqueness chain (F3, F4, F5);
the equivariance half is essentially sound modulo write-up repairs
(F6). No finding kills the stage-1 architecture; several kill labels
or statements as written.

Severity tiers used: [BREAKS-LABEL] = a claim or its rigor class fails
as written; [GAP] = unjustified proof step threatening the label;
[DEFECT] = hypothesis/falsifier/accounting defect; [NIT] = hygiene.

==============================================================================
## F1 [BREAKS-LABEL] P-HB3(i) is FALSE as stated — concrete counterexample

CLAIM ATTACKED (§6, [P-HB3], labeled THEOREM): "At a mode transition
(wave count n changes during the observation window): (i) H3 fails
outright: the data are invariant under NO nontrivial element of G_full
on any window containing the transition."

OBJECTION. The universally quantified statement is false. Take a
genuine wave-count transition n1 -> n2 with d := gcd(n1, n2) >= 2,
both phases rotating at speed OM:

    s(theta, t) = f(theta - OM t) for t < 0,
                  g(theta - OM t) for t >= 0,

f (2pi/n1)-periodic, g (2pi/n2)-periodic, f != g. This is a genuine
mode transition (wave count changes at t = 0; s is NOT of the global
rotating-wave form since the profile switches). Yet the pure rotation
rho_d = g_{2pi/d, 0} is a NONTRIVIAL element of G_full leaving s
invariant on EVERY window: (g_{2pi/d,0} s)(theta,t) = s(theta - 2pi/d, t)
= s(theta, t) because both f and g are (2pi/d)-periodic. The
physically documented RDE mode-doubling transitions (2 -> 4, 3 -> 6)
sit EXACTLY in this class — the counterexample is not contrived; it is
the generic commensurate transition. The document's own falsifier
("exhibit a transition window on which the data retain an exact
nontrivial space-time symmetry — kills (i) as stated") fires on this
trivially.

SECONDARY DEFECT: the hedge "the claim is for genuine wave-count
changes with generic profiles" appears ONLY inside the falsifier line,
not in the statement; "generic" is undefined (no topology, no measure,
no residual-set claim); and [P-HB3] carries NO proof block at all for
(i) — items (ii)/(iii) are citations of in-house declarations, but (i)
is a mathematical claim asserted bare. Under the binding standard,
THEOREM requires a complete proof: (i) has none and is false as
quantified.

LABEL IMPACT: [P-HB3] THEOREM -> at best PROPOSITION/SCHEMA after
restatement. REPAIR ROUTE (available, cheap): restate (i) as "the data
are invariant under NO nontrivial ONE-PARAMETER subgroup of G_full"
(this is what the steadification mechanism needs, it is provable by
the P-HB2 argument since the profile switch destroys every continuous
helical symmetry), and separately note that discrete rotations rho_d
survive iff d = gcd(n1, n2) >= 2 — which is actually USEFUL content
for the H-DATA monitor (a surviving discrete symmetry at transitions
is a checkable signature). The three-layer boundary reading (data /
objective / certificate) survives unchanged.

==============================================================================
## F2 [BREAKS-LABEL] Stratum (B): [C-MAJDA] inheritance is mis-cited —
## the conditional consumed is a strictly stronger, unregistered object

CLAIM ATTACKED (§4 [T-T0P-U](B), §5 [T-T0P], §9 G3): the front stratum
"inherits [C-MAJDA]... in-class sharpened form: the U3-H1
Lopatinskii-Schur scalar of the bordered front solve"; G3: "Unchanged
by this document, cleanly confined to the front stratum"; §0: "no new
analytic conditional is created".

OBJECTION. The registered [C-MAJDA] / U3-H1 object, per the transfer
doc §7 ("Relation to [C-MAJDA]: ... canonicity ACROSS fitted fronts
remains the declared conditional backed by Majda stability") and per
[S-D25U-U34], is a conditional about the PLANAR STEADY 2-D front
solve: a front curve in a 2-D x-marching problem, with a
Lopatinskii-Schur SCALAR (one transverse frequency direction). The
present theorem needs front-crossing uniqueness for the UNSTEADY 3-D
problem in the x-as-time frame: the fitted front is now a hypersurface
in (x, y, z, t), the transverse variables are (y, z, t), and the
Lopatinskii condition is a determinant condition over a genuinely
LARGER frequency space (two extra transverse directions). Uniform
Kreiss-Lopatinskii stability of a multi-D unsteady shock (Majda 1983,
compressible vortex sheets literature, Coulombel-Secchi) is a
DIFFERENT and STRONGER hypothesis than its planar-steady trace; there
are classical examples of fronts stable under a restricted frequency
class and violently unstable in the full multi-D class (e.g. the
supersonic vortex sheet: 2-D stable for M > sqrt(2), 3-D unstable —
the dimension jump is exactly where front stability is KNOWN to
break). Therefore:

 (a) the sentence "inherits EXACTLY [C-XBVP](a,b) — no new analytic
     conditional is created" (§0/§3) is FALSE for the front stratum:
     the conditional consumed there, call it [C-MAJDA-3DT], is new,
     never registered, and NOT implied by the certified U3-H1 scalar;
 (b) G3's "Unchanged by this document" is false as inheritance
     accounting: the document CHANGES the object the conditional must
     govern while keeping its name;
 (c) THEOREM* requires "complete modulo named CITED conditionals":
     the cited conditional does not cover the use. Stratum (B) of
     [T-T0P-U], and hence [T-T0P] restricted to instances with fitted
     fronts, is SCHEMA, not THEOREM*, as labeled.

LABEL IMPACT: [T-T0P-U] and [T-T0P] should be split-labeled: THEOREM*
on stratum (A) (shock-free), SCHEMA on stratum (B) with the named gap
[C-MAJDA-3DT] (multi-D unsteady front stability/uniqueness on the
certified front set). REPAIR ROUTE: mint the 3-D-unsteady conditional
explicitly with its own registry row and falsifier (the bordered
Lopatinskii determinant over the (eta_y, eta_z, sigma_t) frequency
half-space, evaluated on the certified compact front set); or restrict
the theorem's stated scope to stratum (A) and declare (B) as route.

==============================================================================
## F3 [GAP] Local diffeomorphism is proved; a GLOBAL branch bijection is used

CLAIM ATTACKED (§3 [L-XSON3] "sonic bijection", THEOREM; §4 endgame
"hence M_V = M_U a.e., hence V = U by the branch bijection
(L-XSON3)"; also the definition of (EU-x): "the map U -> M := F_x(U)
is a local diffeomorphism, and (EU) rewrites as...").

OBJECTION. L-XSON3 proves exactly one thing: det(D_U F_x) != 0 on the
branch (via the correct parity/rotation factorization det J_5 =
rho u det J_4). That yields a LOCAL diffeomorphism. But the proof
consumes GLOBAL properties twice:

 (a) the x-as-time system (EU-x) requires W(M), F_y(M), F_z(M) to be
     WELL-DEFINED functions of M on the image F_x(K) — i.e. global
     injectivity of F_x restricted to the K-branch. With only local
     invertibility, W(M) is a priori multi-valued (and physically IS
     two-valued across the sonic fold: the classical supersonic/
     subsonic pair with equal fluxes);
 (b) the final step "M_V = M_U => V = U" is precisely global
     injectivity on K.

The in-house 2-D [T-XSON] carries the SAME limitation of record
(transfer doc §1: "local diffeomorphism (numeric nonvanishing on the
sampled branch)"), so the inheritance does not supply the missing
global statement either; and neither [C-XBVP](a) nor (b) contains it
— so the used property is an UNNAMED conditional, contradicting the
completeness of the §9 gap list ("complete list").

WHY IT MATTERS at this lens: uniqueness theorems die exactly on fold
structures; "the branch selects the state" is a claim, not a step.

REPAIR ROUTE (available, and worth writing since it is short): from
M = (m1, m2, m3, m4, m5) with m1 = rho u > 0, recover v = m3/m1,
w = m4/m1, H = m5/m1 exactly; the remaining planar triple
(rho u, rho u^2 + p, h + u^2/2 = H - (v^2+w^2)/2) is the classical
1-D flux triple, for which one-sidedness of the supersonic root is
provable at abstract EOS from monotonicity of the mass-flux function
along the H-isoline (needs a stated EOS convexity condition — name
it), or can be instance-certified on K by interval arithmetic as an
[X-T0P] check. Until then L-XSON3's label should read: THEOREM for the
determinant statement, the BIJECTION in the lemma title and in the §4
endgame = named gap.

==============================================================================
## F4 [GAP] The quadratic sandwich needs convexity on a CONVEX M-domain —
## pointwise Hessian definiteness on K_M does not deliver c_K

CLAIM ATTACKED (§4, proof of (A)): "strict convexity (L-XC3D +
[C-XBVP](a) block): c_K |M_V - M_U|^2 <= eta(V|U) <= C_K |M_V - M_U|^2,
with c_K > 0 uniform"; §3 L-XC3D: "strict convexity of eta on the 3-D
margin box holds IF AND ONLY IF it holds on the planar (M, V)-box".

OBJECTION. The lower bound is the Taylor identity
eta(V|U) = int_0^1 (1-s)(M_V - M_U)^T D^2eta(M_U + s(M_V - M_U))
(M_V - M_U) ds, which requires D^2 eta >= c_K Id along the SEGMENT
[M_U, M_V] — i.e. Hessian definiteness on a CONVEX set containing the
M-image of K, with eta defined and C^2 there. Three unaddressed
defects:

 (a) K (H5) is cut out by bounds on rotational scalars
     (rho, S, u_x, |u|, c) in PRIMITIVE variables; its image K_M under
     the nonlinear map F_x has no stated convexity. The phrase "3-D
     margin box" is doing silent work: no box in M-coordinates is ever
     defined in this document.
 (b) The in-house certificate [X-IVXC] certifies definiteness over a
     box in MACH-PAIR coordinates (M, V) = (u/c, v/c) (transfer doc
     §2, [T-XRED]); the preimage of a Mach box is not convex in
     m-coordinates. So even at the ideal-gas instance the certified
     region is not of the right shape for the segment argument
     without an additional hull statement.
 (c) The hull condition is LOAD-BEARING, not bookkeeping: the
     in-house carrier's own R1 result (60/60 subsonic-in-x states
     INDEFINITE; "no convex extension across the sonic line exists
     for this eta") means that if conv(K_M) crosses the sonic fold,
     the sandwich genuinely FAILS — this is not a removable
     technicality of [C-XBVP](b) class, and it is not listed under
     any named gap. (Note the same scruple applies to the in-house
     2-D [T-XWS]; this document repeats rather than repairs it, while
     §9 declares its gap list "complete".)

REPAIR ROUTE: either (i) prove/certify definiteness on an explicitly
convex M-superset of K_M staying on the branch (checkable: bound the
hull's Mach-pair image and re-run the interval certificate on the
enlarged box — an [X-T0P] item), or (ii) use the standard convex
localization (replace eta by eta + A|M - M_U|^2 correction / restrict
to a geodesically convex margin tube), or (iii) declare the hull
condition as a NAMED component of the (a)-inheritance. Any of the
three keeps THEOREM* honest; as written the constant c_K is
unjustified.

==============================================================================
## F5 [DEFECT] Hypothesis completeness: the strong side's T-periodicity is
## used but never hypothesized — and it is dangerously close to circular

CLAIM ATTACKED (§4, statement of [T-T0P-U](A): "Let U be a C^1
solution (H6-A) and V an H7/H8 competitor"; proof: "T_t = R/(T Z)
(H8: both solutions T-periodic, so the t-integrals below are over a
compact circle — no boundary terms in t)"; also G-constant
"G := ||D U||_inf over cl(Omega) x [0, T] (finite: C^1 on a compact
slab by H6-A + H8)").

OBJECTION. H8 as written binds "Competitors" — the H7 weak class. H6
nowhere asserts t-periodicity of the strong side. The slab proof
integrates BOTH solutions over T_t: without U-periodicity, (a) the
t-compactification is illegitimate for the U-terms (the smooth entropy
identity of U and the cross terms acquire t-boundary contributions on
any truncation), and (b) ||DU||_inf over cl(Omega) x R is not implied
finite by C^1 regularity alone — the proof quietly uses [0, T] as the
t-domain, which only covers U if U is T-periodic. The eventual
application (§5: uniqueness property for [T-T0P-E], with U = q an
arbitrary S1 class element) needs q T-periodic BEFORE steadiness is
concluded — but t-periodicity of q at the data period is uncomfortably
adjacent to the CONCLUSION being proved (steadiness in the co-rotating
frame implies T-periodicity). This is not fatal — assuming
T-periodicity of the class is strictly weaker than assuming the
rotating-pattern form, exactly as the H8 commentary says — but then
the assumption must be stated ON THE CLASS C(s) (both strata of H6
included), not on "competitors".

LABEL IMPACT: none once repaired (the repair is a quantifier fix), but
under the binding standard ("explicit hypothesis list, every
quantifier") this is a valid hypothesis-completeness finding against a
THEOREM*-labeled statement. REPAIR: amend H8 to "all class members are
T-periodic in t", and note in §5 that for the S1 element this is a
class hypothesis discharged per-instance by the same monitor that
verifies H3 (or lift it altogether via the G5 cone route, which would
also cover U — note G5 as currently drafted lifts periodicity only
"on the COMPETITOR").

==============================================================================
## F6 [GAP] L-STD: per-tau null sets and the front-set invariance are
## glossed

CLAIM ATTACKED (§2.2 [L-STD], THEOREM; §2.3 use in [T-T0P-E]).

OBJECTION, two parts.

 (a) Null-set bookkeeping. The hypothesis is: for EVERY tau,
     q = g_tau q a.e., with the exceptional null set N_tau DEPENDING
     ON tau (an uncountable family). The proof mollifies in t and
     asserts "hence Q_eps(., t) = Q_eps(., 0) for ALL t". For FIXED
     tau, convolution does propagate the a.e. identity, and
     continuity in t upgrades it to all t — but only off an
     x-null-set E_tau that STILL depends on tau. To conclude
     Q_eps(., t) = Q_eps(., 0) for all t simultaneously one needs the
     standard closure: take tau in a countable dense subset of R,
     discard the union of the E_tau, and use continuity of
     tau -> Q_eps(., t - tau) in L^1_loc to cover all tau. The step
     is standard and the conclusion true, but as written the proof
     skips exactly the measure-theoretic point the lemma exists to
     handle ("the measure-theoretic representative handled properly"
     is the lemma's advertised purpose). Under the binding standard:
     unjustified step in a THEOREM-labeled lemma.

 (b) Pointwise refinement. The refinement hypothesis "q continuous
     off a closed null set N with g_tau N = N" is CONSUMED in §5(i)
     ("pointwise off the front set") — but for the application, the
     invariance g_tau N = N of the S1 front set is never established.
     It does follow from the a.e. identity q = g_tau q: for genuine
     (nonzero-jump) transversal fronts, the front set minus a null
     set coincides with the set of non-Lebesgue points of q, which is
     an invariant of the a.e.-equivalence class, hence g_tau-invariant
     when q = g_tau q a.e.; removable (zero-jump) front sheets must
     be excised first. None of this is written; one sentence each
     would close it. As stated, [T-T0P]'s "(and pointwise off the
     front set)" rests on an unproven set identity.

LABEL IMPACT: none after the (short) repairs; both are write-up gaps,
not truth gaps.

==============================================================================
## F7 [DEFECT] The [T-T0P-U]/[T-T0P] instance falsifier cannot actually
## reject the class-restricted statement

CLAIM ATTACKED (§4 FALSIFIER; §9 falsifier table): "a certified
numerical instance ... with TWO distinct K-valued entropy solutions on
identical inflow data — kills the theorem and with it the class
architecture."

OBJECTION. The theorem quantifies over competitors satisfying H7
(divergence-measure normal-trace package = [C-XBVP](b) regularity) AND
H8 (T-periodicity). A discovered second solution that is transient
(not T-periodic) or that lacks the trace package does NOT contradict
the theorem as stated — the statement simply does not speak about it.
Two consequences:

 (a) As a rejector, the falsifier over-claims: for it to "kill the
     theorem" the exhibit must be certified to LIE IN the class, and
     the trace-package membership ([C-XBVP](b)-class regularity of an
     L^inf numerical field) is not a numerically certifiable
     property — no finite computation verifies divergence-measure
     normal traces. The falsifier as stated can only ever kill the
     PHYSICAL reading (the class architecture), not the labeled
     mathematical claim; the document should say which.
 (b) The heavier H7/H8 are, the emptier the falsifier: this is
     exactly the trade the R5 discipline exists to surface. Honest
     repair: state the falsifier in two tiers — tier 1 (kills the
     theorem): a second solution WITH certified class membership
     (executable only for classes whose membership is checkable, e.g.
     piecewise-C^1/BV competitors, where strong traces are free);
     tier 2 (kills the architecture's relevance, not the theorem): any
     reproducible second K-valued entropy solution, class-uncertified.
     Note the same two-tier honesty is ALREADY the de-facto in-house
     standard for [T-XWS] §8 — the extension here silently dropped it.

==============================================================================
## F8 [ABSENCE] Convex-integration non-uniqueness for multi-D compressible
## Euler is unengaged — and it calibrates exactly the two weak points
## (front stratum, H7 weight)

OBJECTION. The known literature route the document never mentions:
admissible (entropy-inequality-satisfying) L^inf weak solutions of
multi-D compressible Euler are massively NON-unique in the presence of
shock-type structures — De Lellis-Szekelyhidi convex integration,
made specific for compressible Euler by Chiodaroli-De Lellis-Kreml
(piecewise-constant Riemann/shock data generating infinitely many
admissible solutions), extended by Klingenberg-Markfelder and others
to full Euler. Relevance here, per weak point:

 (a) STRATUM (B): the wild constructions live precisely where a front
     is present and the strong solution is not C^1. They demonstrate
     that in the naive admissible L^inf class NO pointwise front-
     stability condition of Majda/Lopatinskii type can, by itself,
     restore uniqueness — uniqueness across fronts in multi-D must be
     bought by RESTRICTING THE COMPETITOR CLASS (BV, trace
     conditions, a-contraction shifts). This is the sharpest known
     reason why F2's mis-citation matters: [C-MAJDA-3DT] as a front-
     local scalar condition is arguably NOT EVEN SUFFICIENT in the
     stated H7 class unless the trace package is strong enough to
     exclude wild competitors, and no argument here addresses whether
     it is. A rigorous stratum-(B) claim must either engage this or
     restrict the class visibly.
 (b) H7 CALIBRATION: whether wild solutions can be built INSIDE the
     axially-supersonic margin box K (all velocity oscillations
     keeping u_x - c >= delta) with the H7 traces is exactly the
     question that decides how much of the uniqueness claim is doing
     work. If yes, H7's trace clause is the ONLY wall between the
     theorem and a counterexample, and [C-XBVP](b) is carrying far
     more load than "bookkeeping/technicalities" (the word used
     throughout). If no (the margin obstructs the constructions),
     THAT is a valuable lemma and should be conjectured explicitly.
 (c) The §9 novelty-sweep query list contains no query touching
     non-uniqueness/convex integration/wild solutions; the sweep as
     designed cannot surface the counterexample literature that most
     directly bounds this theorem's reach.

Note: on stratum (A) the objection has no force — weak-strong
uniqueness against a C^1 strong solution is exactly the regime where
relative entropy beats convex integration (the wild solutions attach
to non-smooth data) — which is precisely why the (A)/(B) label split
demanded in F2 is the right cut.

==============================================================================
## F9 [DEFECT] H6 omits front admissibility of the strong side

OBJECTION. H6 defines the S1 class by regularity alone (piecewise C^1,
finitely many transversal C^1 fronts). Two uses require MORE:

 (a) the §3 statement that (EI-x) "across admissible fronts follows
     from the physical entropy condition (S nondecreasing along
     particle paths, positive mass flux)" — for the strong side to be
     comparable in the relative-entropy argument (and for stratum (B)
     assembly, where q's own fronts enter with their jump conditions),
     q's fronts must be Rankine-Hugoniot-consistent AND
     entropy-admissible with positive mass flux. Neither RH
     consistency nor admissibility is part of H6 as written (piecewise
     C^1 alone does not even make q a weak solution);
 (b) the positive-mass-flux clause excludes contact/slip surfaces
     through which m = 0 — if the S1 class is meant to allow fitted
     contact discontinuities (helical slip surfaces are physically on
     the table in this geometry), the per-front entropy argument as
     cited does not cover them (g(S) jumps across a contact with
     m = 0: the entropy flux is continuous, fine for (EI-x), but the
     FRONT-UNIQUENESS machinery cited for stratum (B) is
     shock-specific; vortex-sheet fronts have their own — much worse —
     stability theory). State which front types H6-B admits.

REPAIR: add to H6: "each front is a weak-solution discontinuity (RH)
satisfying the physical entropy condition with mass flux bounded away
from zero" (or admit m = 0 fronts and extend G3 accordingly). One
sentence, but load-bearing for both strata.

==============================================================================
## F10 [DEFECT] The "no new analytic conditional is created" accounting
## claim is false; the §9 gap list is not complete as declared

OBJECTION. §0/§3 claim: "the extension inherits EXACTLY [C-XBVP](a,b)
— no new analytic conditional is created; the two genuinely new
hypotheses are declared as class hypotheses (H8, H9)". Against the
findings above, the true ledger is:

 - [C-MAJDA-3DT] (F2): new, unregistered, strictly stronger than the
   cited planar-steady conditional — an ANALYTIC conditional, not a
   class hypothesis;
 - global branch bijection on K (F3): consumed, proven nowhere,
   contained in no named gap ((a) is definiteness, (b) is traces —
   neither is injectivity);
 - convex-hull/domain condition for the sandwich (F4): consumed,
   contained in no named gap;
 - strong-side T-periodicity (F5): consumed, assigned to no
   hypothesis.

§9 opens: "NAMED GAPS (complete list)". Four items above are absent.
Under the house standard (audit line = the record; gap lists =
complete by declaration), an incomplete gap list declared complete in
a THEOREM*-labeled document is itself a finding, independent of each
gap's individual reparability. REPAIR: extend the ledger (G7-G10) and
re-derive the audit-line label sentence from the extended ledger.

==============================================================================
## F11 [NIT] L-SPACE prose overstep

The lemma's mathematical content (all characteristic x-ray components
>= delta; bounded transverse slopes; compact pullback) is correct and
cleanly proved. The prose conclusion "NO initial-in-t datum exists or
is needed — the interface trace for all t is the complete Cauchy datum
of the x-evolution" is TRUE only relative to a solution class with
controlled behavior as t -> +-infinity (here: H8 periodicity, or the
G5 cone class); for general L^inf-in-t classes the x-evolution on the
infinite t-line is not a Cauchy problem in any proved sense. The
sentence should carry a "(within the H8/G5 class)" qualifier — it is
currently quotable out of context as an unconditional claim inside a
THEOREM-labeled lemma. Also: for WEAK solutions, domain-of-dependence
is not a corollary of bicharacteristic geometry but of the cone-
localized relative-entropy estimate (G5) — the lemma proves the
geometry, the doc should not let it imply the weak-solution statement.

==============================================================================
## F12 [NIT] Wording/micro-gaps (collected)

 (a) [P-HB1]: "the solution inherits EXACTLY the data's invariance
     group" contradicts the correct inclusion Sym(q) >= Sym(s) proved
     two lines above; the parenthesis fixes the intent ("no larger
     group is implied BY THIS MECHANISM") but the headline sentence
     asserts equality of groups, which is false in general (a
     solution can be more symmetric than generic data if uniqueness
     collapses it onto a symmetric object). Reword.
 (b) [P-HB2] proof differentiates phi(sig), tau(sig) without stating
     why a continuous one-parameter subgroup is differentiable
     (continuous homomorphisms R -> R^2 are linear — one clause).
 (c) [T-T0P-E] falsifier: "exhibit q in a class C(s) with the
     uniqueness property and g_tau q outside C(s)" — as stated this
     falsifies L-EQV3, not the theorem (whose proof would survive any
     repair of L-EQV3's route); label the falsifier's target
     precisely, per R5.
 (d) §4 L-COMPAT Step 1 needs E, Q_k in C^1 in W and the state space
     open around the branch point — both true, neither stated.

==============================================================================
## WHAT SURVIVES (verified sound at this lens, this round)

Checked line-by-line and NOT refuted:

 - [L-EQV1]/[L-EQV2]/[L-EQV3]/[L-INV]: the covariance computation
   (dyadic momentum flux congruence, scalar EOS entry), class-
   preservation items (i)-(viii), and the data-invariance computation
   are correct; abstract-EOS status honest.
 - [L-XWALL3]: the 5-component slip solve is CORRECT (recomputed
   independently: d(rho u) = 0, dH = 0, u du = (n_x p' - dp)/rho,
   theta dS = -p'(u.n)/(rho u) = 0), and the "every g, every EOS"
   conclusion follows. A genuinely clean 3-D extension.
 - [L-XC3D]: parity decoupling and the (KEY) cancellation are correct
   (recomputed via dp = -m1 du: dh + u du = theta dS = -dbeta
   directly); h_ww = g'/(theta rho u) confirmed; positivity on K
   sound. The DOMAIN issue (F4) is about the use, not the formula.
 - [L-XSON3]: the parity/rotation factorization det J_5 =
   rho u det J_4 at w = 0 is correct (the gap F3 is about global vs
   local, not the determinant).
 - [L-COMPAT]: both steps verified (the identity D_M eta = D_W E is
   correct and genuinely is the algebraic heart); the
   Kato-Majda-arbitrary-gradient device is standard and correctly
   deployed.
 - [P-HB2]: the Fourier/lattice argument is correct; the discrete
   subgroup conclusion holds; the same-speed multiplicity note is
   exactly right.
 - VARIABLE-GAMMA TABLE: audited per statement; the declarations are
   HONEST — the single ideal-gas-limited ingredient ([X-IVXC],
   gamma = 1.4, entering via G1) is correctly identified and nothing
   else in the chain consumes gamma = const. No gamma finding.
 - The two-stage honesty structure (§7) and the novelty disclaimer
   are consistent with the record.

==============================================================================
## ROUND-1 VERDICT

REPAIRABLE. The equivariance half [T-T0P-E] stands as THEOREM after
the F6 write-up repairs. The uniqueness half stands as THEOREM* on
stratum (A) ONLY AFTER F3 (global bijection), F4 (convex domain), F5
(U-periodicity) are either proved or added to the named-gap ledger;
stratum (B) must be relabeled SCHEMA pending [C-MAJDA-3DT] (F2), with
the convex-integration literature (F8) engaged or the class
restriction made visible. [P-HB3] is false as stated and must be
restated (F1) — the repair is known and strengthens the monitor
design. The gap-ledger completeness claim (F10) and the falsifier
tiering (F7) are accounting repairs. No finding breaks the stage-1
architecture; five findings break labels or statements as written.

Refuter: functional-analytic lens, round 1 of until-dry.
Environment: pinned, untouched; no installs; single-file deliverable.

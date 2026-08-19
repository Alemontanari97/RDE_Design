# ADVERSARIAL REFUTATION — batched r2 pass, LENS l1 (gas dynamics / physics)

Lens: l1 — Rankine-Hugoniot algebra, characteristic structure, thermodynamic
consistency, sign conventions, physical counterexamples, frame/rotation effects.
Date: 2026-08-17. Brief: `r2pass/BRIEF_refuters_r2batch.md`, executed in full.
Targets: the 18 delta legs of DOC-1 (`phaseD/phaseD_stop_proof.md` r3),
DOC-2 (`phaseD/phaseD_meanswirl_formalization.md` r3), DOC-3
(`phaseD_L4_implies_R1.md` r2). All three documents read in full; every leg
read with its revision-block context. DEDUP discipline: every objection below
targets text NEW in the final revision (r3 / r2 respectively); none re-raises a
consumed on-file finding (checked against `refute_S-T0P_r*`, `refute_SWIRL-2D_r*`,
`refute_L4R1_r*` dispositions cited in the documents' ledgers). Labels are not
re-litigated (content pass).

Classification scale: {BREAKS-THE-LEG, REPAIR-NEEDED, AMENDMENT/wording}.

==============================================================================
## DOC-1 — phaseD/phaseD_stop_proof.md (r3)

### Leg 1 — [L-INC] (both strata uses). VERDICT: CONFIRMED.

Strongest attack tried (RH/sign audit of clause (a), stratum (B)): I re-derived
the per-front distributional contribution of the quadruple
(eta, q_y, q_z, q_t) = -g(S)·(rho u, rho v, rho w, rho) across an admissible
H6' front. With space-time unit normal N = (N_sp, N_t), the jump term is
-[g(S)·rho(u·N_sp + N_t)] = -m_st[g(S)] with m_st = |N_sp|·m (m = physical
front-relative mass flux), m_st continuous by the mass RH row. Sign check both
ways: m > 0 ⟹ flow crosses -side → +side ⟹ [g(S)] >= 0 (entropy admissibility,
g' > 0) ⟹ -m[g] <= 0; m < 0 ⟹ [g(S)] <= 0 ⟹ -m[g] <= 0. The claimed
"-|N_sp| m [g(S)] <= 0 for either sign of m" is exactly right, and the |N_sp|
normalization is consistent with the 4-D surface measure. The G9 exclusion of
m = 0 fronts is genuinely load-bearing here (the argument is void at m = 0),
as the leg itself says. Clause (b)'s trace claims for C^1 / piecewise-C^1
fields (classical traces = Chen-Frid traces; BV_loc off codimension-2 sheet
intersections) and clause (c) are correct; the structural-clause automaticity
for state-trace fields ((w1)-(w3): -rho(u·n)g = 0, momentum flux = p n
pointwise at slip; (d1)/(d2) with equality at equal trace) checks out
pointwise. No break found.

### Leg 2 — [L-STD] final no-topology pointwise argument. VERDICT: CONFIRMED.

Strongest attacks tried: (a) the field-map/point-map conflation hazard in
"g_tau N = N ⟹ g_{-tau} x off N": N (essential discontinuity set) transforms
by the POINT map Phi_tau (the state rotation R_phi is a homeomorphism of state
space and cannot create/destroy continuity points), and q = g_tau q a.e. means
the two fields share one a.e.-class, hence one essential discontinuity set; so
Phi_tau(N) = N and the point-level step is legitimate. (b) The
approximation step: continuity of q at x and of g_tau q at x (the latter from
continuity of q at Phi_{-tau}x, off N by invariance), plus a sequence from the
co-null equality set converging to x, gives q(x) = (g_tau q)(x) with no
topology of N consumed — sound; the choice of sequence from a co-null set is
always possible. (c) The eps_n union bookkeeping and the countable-dense
closure (constancy of a continuous function invariant under a dense set of
translations) are correct; L^1_loc-limit uniqueness makes Q_bar
sequence-independent. (d) Setting tau = t pointwise: Phi_{-t}x off N by
invariance, so q_tilde is well-defined where claimed. No break found. This is
the cleanest of the r3 legs.

### Leg 3 — the periodization step (§4 proof head). VERDICT: CONFIRMED with
### one AMENDMENT (L1-1).

**L1-1 (leg 3) — AMENDMENT/wording: the literal "summing telescopes" over the
partition of unity diverges; the true mechanism is a single window whose
translates sum to 1, with telescoping only in the derivative terms.**

Quote (DOC-1, §4 proof head): "pairing (EI-x) with a partition of unity
subordinate to {(kT - T, kT + T)}_{k in Z} — each term a legitimate D'(R_t)
pairing — and summing telescopes by periodicity to the same inequality on
Omega_march x T_t."

Attack at derivation level: the distribution
mu := -(d_x eta + d_y q_y + d_z q_z + d_t q_t) >= 0 is T-periodic in t for a
T-periodic V (that part is right). Pairing mu against phi·chi_k with chi_k the
partition members and SUMMING over k in Z produces, for a T-periodic nonzero
mu, infinitely many equal positive contributions: the literal sum is +infinity,
not the torus inequality — "summing" over the whole partition is pairing
against phi·1, a non-compactly-supported test, undefined in D'. The correct
one-line mechanism (standard): fix ONE window chi with
Sum_k chi(t - kT) = 1; define the torus pairing of any T-periodic test psi >= 0
as <mu, psi·chi> — k-independent by joint periodicity, and equal to the full
torus integral BECAUSE the translates of chi sum to 1; the "telescoping" is
that Sum_k d_t chi(t - kT) = 0 kills the extra d_t chi terms when converting
d_t(psi chi) pairings to torus-distributional-derivative pairings. The
conclusion (torus form of (EI-x) for the T-periodic class) is TRUE and the
class hypothesis consumed (V and the composed quadruple T-periodic) is exactly
the right one; only the printed line does not parse as written. Repair: one
sentence, as above. NOT a break: the leg's content survives verbatim under the
correct wording. (Dedup: r2b-F6 demanded the step be WRITTEN; this objection
is against the adequacy of the newly written line, not a re-raise.)

### Leg 4 — [P-HB3] (i') data-space mollification proof. VERDICT: CONFIRMED.

Strongest attacks tried: (a) window-domain bookkeeping: the invariance
identity on a window W references s at times t - b·sig outside W; I checked
that the L-STD mechanism transplanted to the data space still closes — for X
off the null set, h(t) := S_eps(X, t) satisfies h(t0) = h(t0 - tau) for every
tau in the dense set at each t0 in W, and density + continuity make h constant
on all of {t0 - tau} = R, which is MORE than the claimed "a.e. on the whole
window": no hole. (b) The window-independence iff: rho_n s = s a.e. on
Gamma_d x I iff s_hat 2pi/n-periodic — verified by the change of variable
xi = theta - OM t, whose range covers S^1 for any nontrivial sub-window (and
even for OM = 0 via theta alone); so a genuine wave-count transition is indeed
incompatible with an exact rotating-wave representative. (c) Case b = 0,
a != 0: {a·sig mod 2pi} exhausts SO(2); measurable full-rotation-invariance
gives count = infinity on every sub-window under the stated axisymmetric
convention — consistent, no genuine transition. (d) Velocity-vector
bookkeeping: in cylindrical trace components the action is a pure argument
shift (no component mixing), and Gamma_d is away from the axis — no
singularity issue. The r2-F5 null-graph defect is genuinely repaired: no step
evaluates an a.e. identity on a measure-zero set. No break found.

### Leg 5 — the G8/r2 repricing (gap accounting for [C-XBVP](a')).
### VERDICT: OBJECTION L1-2 (REPAIR-NEEDED); the repricing's negative
### conclusions all CONFIRMED.

What I verified and could not break: (a) the congruence claim — with
G_U(W) := Q_x(W) - D_W E(U)·F_x(W) and h(M) := eta(M) - D_M eta(M_U)·M one has
G_U = h ∘ F_x, D_W G_U(W_U) = D_M eta(M_U)·DF_x - D_W E(U)·DF_x = 0 by the
L-COMPAT identity, and D^2 G_U(W_U) = DF_x^T D^2 eta(M_U) DF_x — congruent to
the M-Hessian exactly as claimed; the transfer of [S-XCONV] R1 subsonic
indefiniteness to W-space is therefore valid. (b) The W-non-convexity of the
supersonic set: verified by a physical mixing exhibit — two marginally
supersonic states with different velocities W-average to a state whose
velocity is the mass-weighted mediant while the velocity variance is deposited
into internal energy (the mixing-shock mechanism), raising c; the average can
be subsonic. The "mediant" mechanism claimed is physically right. (c) The
retraction of "r2 kills the hull problem at its root" is forced; the
route-level-open conclusion stands.

**L1-2 (leg 5) — REPAIR-NEEDED: the GRANTED half of route r2 — W-convexity of
E = -rho g(S) with the lower sandwich E(V|U) >= c|DeltaW|^2 — is itself
conditional on a thermodynamic-stability condition NOT in the §1 gas model and
not named in the row; the r2 gap accounting is still incomplete by one named
condition.**

Quote (DOC-1, G8 row, route r2): "What W-convexity of E = -rho g(S) (Harten;
Godlewski-Raviart — t-EVOLUTION facts) genuinely delivers: (i) E(V|U) >=
c|DeltaW|^2 with all comparison segments inside the convex physical region
({rho >= rho_min} IS convex in W — this half of the pricing was correct); (ii)
flux smoothness on that hull, hence the UPPER/commutator bounds along
W-segments."

Attack at derivation level (thermodynamic consistency — my lens): convexity of
-rho g(S) in the conservative variables W is NOT a free consequence of the §1
gas model. §1 hypothesizes ONLY: Gibbs closure e_rho = p/rho^2, e_S = theta,
c^2 = p_rho|_S > 0, theta > 0. The classical results cited (Harten;
Godlewski-Raviart) require in addition a thermal-stability condition: at ideal
gas, -rho f(S) is (strictly) convex iff f' > 0 AND f''/f' < 1/c_v — already a
condition on g beyond g' > 0 — and at general EOS the route runs through
concavity of s as a function of (specific volume, internal energy), which
needs c_v = theta/e_SS-type positivity (e_SS > 0). NOTHING in §1 pins
e_SS > 0: an abstract EOS with c^2 > 0, theta > 0 and e_SS <= 0 somewhere on K
is in-class for this document and breaks the W-convexity of E there, i.e.
breaks delivered item (i) — the "genuinely delivers" grant fails in-model.
(The corpus knows the needed class: G7 route r-a already names "Bethe-Weyl
class" conditions; DOC-2's own AUD-cp is exactly the c_v > 0 audit at gamma(T);
the G8/r2 row alone consumes the condition silently.) Consequence: even the
PARTIAL reduction credited to r2 ("hull convexity + upper bounds gained") is
conditional on a named-but-absent EOS condition, so the r2 residue is not only
the x-flux segment coercivity — the honest r2 status line should read "partial
reduction MODULO a named thermal-stability condition (e_SS > 0 / s-concavity /
Bethe-Weyl class) + open x-flux coercivity". This STRENGTHENS the row's
conclusion (no viable abstract-EOS route) and does not resurrect any label —
hence REPAIR-NEEDED, not BREAKS: add the condition to the r2 text (and note
that at the standing gamma(T) thermally-perfect closure it is discharged by
the AUD-cp-class finite audit, c_v > 0). Not a re-raise of r2b-F1: that
finding priced the coercivity conflation; this one prices the GRANTED half.

==============================================================================
## DOC-2 — phaseD/phaseD_meanswirl_formalization.md (r3)

### Leg 6 — D.18 singular leg: both iff displays + singular-density
### bookkeeping. VERDICT: FIRST IFF BROKEN (L1-3, BREAKS-THE-LEG); singular
### leg + second iff CONFIRMED at derivation level; two AMENDMENTS (L1-4,
### L1-5).

This was the brief's highest-suspicion target; findings in decreasing
severity.

**L1-3 (leg 6) — BREAKS-THE-LEG: the FIRST IFF is false in the forward
direction as printed; the document's own recorded example (α) refutes it.**

Quote (DOC-2, D.18): "FIRST IFF (bookkeeping, now true): the wave-frame field
solves the exact 3-D system DISTRIBUTIONALLY iff each azimuthal section solves
the per-phase 2.5-D system distributionally (meridional RH included) AND K = 0
as a distribution — a.c. part and front atoms both. (By construction of K as
the operator difference; the atom identity is the singular-density display
above.)"

Attack at derivation level: K is defined by the operator identity
Exact(V) = Reduced(V) + K(V) (per row, as distributions — "Write each exact
wave-frame equation as the corresponding per-phase 2.5-D row PLUS a
residual"). From that identity, {Reduced(V) = 0 AND K(V) = 0} ⟹ Exact(V) = 0:
the ⟸ direction of the printed iff is trivially true. The ⟹ direction is
FALSE: Exact(V) = 0 gives only Reduced(V) = -K(V), and any genuinely
phi-dependent exact solution has K != 0. Two witnesses, both in-scope:
(w1) any SMOOTH exact 3-D wave-frame solution with ∂_phi != 0 — e.g. the
standing RDE wave-frame flow itself, the document's central object: the a.c.
rows K_u = rho(w_rel/r)∂_phi u etc. are nonzero by definition, so the LHS
("solves exact") holds while the RHS conjunct "K = 0" fails; (w2) the
document's OWN example (α) (two constant states across a helical wave-steady
front satisfying the full 3-D RH): an exact distributional solution, whose
distributional K carries the nonzero front atom n_phi[F_phi,rel] =
-[F_m·n_m] != 0 — LHS true, BOTH RHS conjuncts false. So the r3 restatement
is refuted by the same example the r3 revision records; the label
"(bookkeeping, now true)" is false for this display. The TRUE nearby
statements, either of which is the intended bookkeeping: (i) "V solves the
exact 3-D system distributionally IFF each azimuthal section solves the
2.5-D system WITH SOURCE -K (a.c. part and front atoms both)" — the tautology
the parenthetical proof actually proves; or (ii) the two-of-three rule: any
two of {Exact(V) = 0, Reduced(V) = 0, K(V) = 0} imply the third (each
biconditional pairing fails in one direction). Repair is a rewording, but as
printed the leg's first display is a false mathematical statement carrying a
"now true" certification — BREAKS-THE-LEG for the first-iff display.
(Dedup: R4-1 refuted the r2 CLASSICAL-reading iffs; this objection is against
the r3-NEW distributional display, which R4-1's repair produced.)

**L1-4 (leg 6) — AMENDMENT/wording: "on an exact 3-D solution the 3-D RH
atoms vanish" is false for the ENTROPY row; the singular-leg conclusion
survives because the proof never needs the sentence for that row.**

Quote (DOC-2, D.18 singular leg): "on an exact 3-D solution the 3-D RH atoms
vanish, so K's atoms reduce to minus the meridional-RH residual; K = 0 as a
distribution then forces the meridional RH TOO, hence n_phi[F_phi,rel] = 0
row-by-row."

Attack: the K list has SIX rows including K_s; the s row in divergence form
(rho u s fluxes) is NOT a conservation law of the exact system across fronts —
at a genuine mass-crossing shock the exact solution's s-row atom is the
entropy PRODUCTION m[s] > 0, not zero. So the quoted sentence, quantified
row-by-row over the six K rows, is false for the s row, and "K's atoms reduce
to minus the meridional-RH residual" fails there (K_s atom = full production −
meridional production = n_phi g[s], by the operator identity, NOT minus the
meridional residual). The derivation chain is nonetheless sound: (a) the
singular-density display atom(K_row) = n_phi[F_phi,rel(row)] holds as an
OPERATOR identity for arbitrary piecewise-C^1 fields (full atom
[rho s u_rel·N] = |n_m|[rho s û] + n_phi[rho w_rel s], minus the meridional
part, independent of any production bookkeeping) — I verified it row-by-row
including s and energy (F_phi,rel(energy) = rho w_rel h0 + Omega r p, whose
jump at [p] = 0 is g[h0]: the "remaining rows close [h0] = [s] = 0" step is
EOS-free exactly as claimed); (b) the "meridional RH" facts consumed
downstream are the mass/momentum (conservation) rows only, where the vanish
sentence IS true. Repair: scope the sentence to the conservation-form rows
(mass, momenta, energy) and derive the s-row atom directly from the
singular-density display. No content falls.

**L1-5 (leg 6) — AMENDMENT/wording: the decomposition clause "(a.c. part) the
displayed smooth-region K rows" misidentifies the advective K rows with the
a.c. part of the divergence-form residual for the momentum/energy rows.**

Quote (DOC-2, D.18): "the distributional residual of a piecewise-C¹ field
decomposes as (a.c. part) the displayed smooth-region K rows, off fronts;
(singular part) an atom on each front with surface density n_φ · [F_φ,rel]
per row".

Attack: the distributional definition writes each row in cylindrical
DIVERGENCE form; the smooth-region difference of exact-minus-reduced
divergence rows is (1/r)∂_phi F_phi,rel per row — e.g. for the x-momentum row
(1/r)∂_phi(rho u w_rel) = K_u + u·K_rho, which differs from the DISPLAYED
advective K_u = rho(w_rel/r)∂_phi u by u times the mass residual (likewise
v, Γ, h0 rows). The identification "a.c. part = the displayed K rows" is
therefore false as a row-by-row identity; it is true only modulo the
invertible triangular recombination with K_rho (bounded coefficients
u, v, Γ, h0), under which "K = 0" is equivalent in both readings — so both
iffs and the second-iff proof are UNAFFECTED. But the row-by-row
singular-density bookkeeping is declared to "ride the G-f independent
re-derivation", and a G-f executor transcribing the displayed advective rows
as the a.c. parts of the divergence-form residual would build a checker that
FAILS on correct fields — exactly the common-mode/type-mismatch defect class
this document prosecutes elsewhere. Repair: state the recombination
(div-form residual row = advective K row + (u, v, Γ, h0)·K_rho as applicable)
in the definition, and put the one-line identity into the G-f rejector spec.

Singular leg + SECOND IFF, the confirmation half of this leg: I re-derived the
entire RH chain independently (my lens's core): with n_phi != 0 and
[F_phi,rel] = 0 row-wise — mass gives [g] = 0, g := rho w_rel; x/r rows give
g[u] = g[v] = 0 ⟹ [u] = [v] = 0 under the H-WR front-trace reading; the
meridional mass/momentum rows give û[rho] = 0 and n̂_x[p] = n̂_r[p] = 0
resolved by the two-case split (û != 0: [rho] = 0 then [p] = 0; û = 0:
[p] = 0 directly); the θ-row atom [rho Γ w_rel + r p] = r(g[w] + [p]) (r
continuous, Γ = rw) gives [w] = 0; then [g] = w_rel[rho] = 0 with w_rel != 0
closes [rho] = 0 in the û = 0 case; energy row (F_phi,rel = rho w_rel h0 +
Omega r p) gives [h0] = 0 EOS-free; s row gives [s] = 0 EOS-free. All five
state variables continuous ⟹ removable front. The n_phi ≡ 0 branch (tangent
contains ∂_phi everywhere ⟹ union of phi-circles, phi-independent one-sided
limits by the a.c. leg) is correct, and the ⟸ direction is genuinely trivial.
The kernel discussions (|w_rel| = c one-parameter kernel at the CJ locus;
w_rel = 0 larger kernel) are physically right — the CJ-surface reading of the
relative-sonic locus matches [T-NSW](a). No break in the singular leg or the
second iff.

### Leg 7 — D.2 psi-existence three-step argument + H-CVX arc wording.
### VERDICT: CONFIRMED with one AMENDMENT (L1-6).

psi-existence, attacks tried: (1) CLOSEDNESS — I verified the jump identity
independently: for the 1-form omega = rho u r dr - rho v r dx, the
distributional-exterior-derivative atom on a front curve is the jump of
omega's tangential component, [omega(t)] = r[rho u_n] (rotated tangent =
normal) — so distributional closedness IS the mass RH row on BOTH front
types, exactly as printed. (2) PERIODS — the period of omega around a closed
curve is the meridional mass flux through the surface of revolution it
generates; deforming to an internal island boundary (legitimate:
distributional closedness holds in between, fronts included) and using slip
u·n = 0 pointwise on walls (§0/D.1, one-sided traces exist in the declared
class) gives zero period. Residual nit, recorded as attack-tried and NOT
elevated: the proof implicitly assumes every INTERNAL boundary component is a
wetted wall (true for the named strut/pylon instance; an internal inflow
component would carry a nonzero period, but none exists in the declared
geometry class). (3) REGULARITY — omega in L^inf gives psi in W^{1,inf};
quasiconvexity of a bounded Lipschitz domain and the embedding
W^{1,inf} ↪ C^{0,1}(cl D) are standard and correctly invoked; continuity of
psi across fronts follows. The contact-as-single-psi-level claim is immediate
(dpsi = rho u_n r ds = 0 along a u_n = 0 curve). Sound.

H-CVX arc wording, attacks tried: I re-derived the closed form independently
via ds = c_v dT/T - R_g d rho/rho: (∂T/∂rho)_s = R_g T/(c_v rho),
G_fund = 1 + (rho/2c^2)(∂c^2/∂rho)_s = 1 + R_g(gamma + T gamma')/(2 gamma c_v)
= 1 + (gamma-1)(gamma + T gamma')/(2 gamma) — AGREES with the display (this
is now a third independent pen-grade recomputation beside the two the
document records; both audits AUD-cp, AUD-c2T enter exactly where claimed).
The arc quantification is the correct hypothesis for finite-amplitude entropy
monotonicity (Bethe/Weyl/Menikoff-Plohr: the control is G_fund at the RUNNING
Hugoniot state; endpoint convexity straddling a BZT pocket admits Lax fronts
with [s] < 0) — the r3 repair is adequate and the in/out falsifier asymmetry
is real. The crossing-direction conventions ([s] and [p] both read along the
mass flux) are consistent with my leg-1 sign audit. One wording defect:

**L1-6 (leg 7) — AMENDMENT/wording: the parenthetical equivalence "G_fund > 0
along the arc ⟺ genuine nonlinearity along the arc" is false as an
equivalence.**

Quote (DOC-2, D.2 H-CVX): "the fundamental derivative G_fund := 1 +
rho(∂c/∂rho)_s/c is > 0 at every state of the Hugoniot locus joining the two
end states (equivalently: the front's wave family is genuinely nonlinear
along the connecting arc)".

Attack: genuine nonlinearity of the acoustic family is G_fund != 0, not
G_fund > 0; an EOS with G_fund < 0 along the whole arc (BZT regime — the very
counterexample class this clause's own repair history cites) is genuinely
nonlinear along the arc yet admits admissible RAREFACTION shocks with the
OPPOSITE entropy-pressure pairing: under "equivalently" the hypothesis would
admit exactly the states the clause exists to exclude. Harmless in context
(the displayed inequality G_fund > 0 is the operative hypothesis and the
gamma(T) discharge gives G_fund > 1), but the equivalence should read
"equivalently: genuinely nonlinear WITH the convex (compressive-shock)
orientation", or simply be dropped. Not a break.

### Leg 8 — D.16 gross normalizer. VERDICT: CONFIRMED.

Strongest attacks tried: (a) pointwise bound: |rho u_x Γ| = rho|u_x||Γ| >=
rho u_x|Γ| for any u_x sign (rho > 0), so the r3 denominator bounds the r2
one from above and coincides on through-flow-only data exactly as claimed —
no recalibration on clean cases is forced, and the integrand being
nonnegative makes the cycle mean cancellation-free by construction: the
backflow-deflation spurious-FAIL channel (V-3) is genuinely closed.
(b) Dilution attack (the converse hazard): a larger denominator shrinks R_AM,
so could a real torque violation hide on backflow-heavy data? Fails as an
objection because tol_AM is DERIVED per dataset in the same normalization
(periodicity residual + declared stress budgets + quadrature), and the r3
arming extension mandates a backflow-bearing synthetic on which R_AM must
move by the KNOWN amount within bars — a denominator-side pathology now has a
dedicated rejector, which is precisely the numerator/denominator blindness
lesson the clause itself records. (c) Consistency: the D.6 falsifier
normalizer (panel F1) was aligned to the same |·| form — checked, it was
(line "normalized by the gross flux ⟨∮ |ρ u_x Γ| dA⟩"). No break found.

### Leg 9 — D.20 contact split (the r3 two-line RH algebra). VERDICT:
### CONFIRMED (independently re-derived — a third derivation of record).

I re-derived both clauses from the unsteady lab-frame RH with front normal
speed sigma_n = Omega r n_theta (correct for a rigidly co-rotating front:
surface velocity Omega r e_theta, normal speed Omega r n_theta):
mass m := rho(u·n - sigma_n), [m] = 0; momentum m[u] + [p]n = 0; energy
m[E] + [p u·n] = 0. Writing p u·n = p(u·n - sigma_n) + p sigma_n and using
[p m/rho] = m[p/rho]: m[E + p/rho] = -sigma_n[p], i.e. m[h0] = -sigma_n[p] —
matches. Theta-momentum: m[u_theta] + [p]n_theta = 0 ⟹ m[Γ] = -r n_theta[p]
(r continuous on the front) — matches. Hence m[I] = m[h0] - Omega m[Γ] =
[p](Omega r n_theta - sigma_n) = 0: [I] = 0 exactly when m != 0 — the
mass-crossing clause is correct and its m != 0 hypothesis is genuinely
load-bearing. Contact clause: m = 0 ⟹ momentum RH reads [p]n = 0 ⟹ [p] = 0
(n unit); energy RH degenerates to 0 = -sigma_n·0; tangential jumps and hence
[h0], [Γ], [I] all free — correct, and the mirror to D.2's contact clause is
exact. Corollary (a)'s restriction to contact-free bundles and the
two-mechanism verdict text ("non-Euler source OR unbudgeted contact
crossing") are the right consequences; the falsifier pair has genuine
rejection power in both directions (an in-class contact with [p] != 0, or one
where RH alone forces [I] = 0, would each kill the split). Strongest attack
tried and failed: hunting a third RH constraint at m = 0 (e.g. from the
energy row) that would pin [I] — there is none; the energy row is vacuous at
m = 0 once [p] = 0.

### Leg 10 — D.10 theta-halves exhibit (Gamma-flux zeroing). VERDICT:
### CONFIRMED.

Verified directly: with rho u_x axisymmetric and u_theta = +u0 on
0 <= theta < pi, -u0 on pi <= theta < 2pi, the Gamma-flux integrand
rho u_x r u_theta integrates to zero AT EACH RADIUS (the theta-integral
splits into two equal-and-opposite halves with an r-independent cancellation)
— r-fiberwise zeroing exactly as claimed, immune to the r-weighting defect
that killed the r1 equal-mass-flux-halves exhibit (which I re-checked: inner/
outer halves of equal mass flux do carry net Γ-flux, the r3 diagnosis is
right). Meanwhile u_theta^2 = u0^2 everywhere, so E_theta =
(u0^2/2)∮rho u_x dA > 0 and is free — the functional-independence claim
("for every value of the flux-weighted mean of Γ ... arbitrarily large
E_theta") follows by superposing an axisymmetric swirl component for nonzero
targets. Class-membership attack fails: the two slip discontinuities at
theta = 0, pi are C-fronts, admitted by §0/H-AM0. No break.

### Leg 11 — D.8 plane-stress rewording ((2)-channel / census
### exhaustiveness). VERDICT: CONFIRMED.

I re-derived the CV balance independently in the §3 conventions: cycle-
averaging d/dt∫rho Γ + ∮(rho Γ u·n + p r n_theta)dA = ∮r(τ·n)_theta dA over
∂CV = Σ_w ∪ S_inj ∪ S(x), with n_theta ≡ 0 on surfaces of revolution AND on
x-planes, storage killed by H-AM1, S_inj folding to +J_inj under the declared
outward-normal/inflow-sign convention, gives exactly
⟨∮ρu_xΓdA⟩ = J_inj + τ_w + T_S(x) + T_inj — the extended budget display is
the correct divergence-theorem bookkeeping and T_S's integrand r τ_xθ with
n = +e_1 is the right traction component. Census exhaustiveness over
{¬H-AM0..¬H-AM5}: with H-AM2 extended to the FULL ∂CV deviatoric moment, the
recorded failure scenario (free-slip walls, O(1) modeled plane stress —
formerly auditing RED with every hypothesis green) now negates H-AM2 and
lands in channel (2); I attempted to construct a breakage mechanism outside
the extended census (curved station surfaces — excluded by the §3 plane
definition; resolved-fluctuation covariance — correctly excluded from the
budget since it lives inside ⟨ρu_xΓ⟩ itself; radiation/MHD — H-AM5) and
found none. The partial-cancellation false-PASS hazard (plane moment against
wall torque) is priced by auditing to the SUM with per-station budgets. No
break.

==============================================================================
## DOC-3 — phaseD_L4_implies_R1.md (r2)

### Leg 12 — Theorem 1' (collar instantiation). VERDICT: CONFIRMED.

Attacks tried: (a) hypothesis-domain audit — the Theorem 1 energy identity
(EI), Lemmas 1.1-1.3, and the boundary decomposition consume the base state
only where integrated; on C_h the boundary is exactly Gamma_I ∪
(Gamma_w ∩ ∂C_h) ∪ Gamma_in^coll, each with its term controlled (margin
outflow ≥ delta-dissipative; wall zero by (BQ)+(H1.2); collar face zero under
(ii) or good-signed under (ii') with the outward normal of C_h) — the
"verbatim" claim is genuine, and the r2 addition of the (G3)-box clause to
(M-c) closes the one consumed-but-unmonitored hypothesis the r2 refuter
found. (b) Physics attack — sought a signal path into C_h avoiding both
Gamma_I (blocked: all five characteristic speeds >= delta outward, zero
incoming count — re-checked against Lemma 0.2's spectrum) and the collar
face; the slip wall is characteristic (u·n = 0) and (BQ) kills its flux
identically for perturbations obeying u'·n = 0: no path. (c) Corner audit —
the C^1 core needs only the divergence theorem on a Lipschitz domain, and
C_h is hypothesized Lipschitz per (D''). The collar form is exactly the
statement whose hypotheses a slab monitor can certify; the vacuity diagnosis
of the unlocalized Theorem 1 for the device class (rotating-wave complex
upstream by design) is honest. No break.

### Leg 13 — Lemma 1.4 (finite speed; shrinking-frustum positivity).
### VERDICT: CONFIRMED.

The load-bearing display lambda_max S + S A(nu) >= 0 for EVERY unit nu is
correct: N := S^{1/2}A(nu)S^{-1/2} is symmetric (Lemma 1.1) with
spec N = spec A(nu) = {u·nu - c, u·nu (x3), u·nu + c} ⊂ [-lambda_max,
lambda_max] since lambda_max = sup_O(|u| + c) dominates |u·nu| + c; a
symmetric matrix with spectrum >= -lambda_max satisfies N + lambda_max I >= 0;
conjugating back gives the display. The shrinking-domain derivative
bookkeeping is right: the spherical boundary recedes at normal speed
lambda_max, contributing -lambda_max∮<SU,U> (correct sign), and the (EI)
divergence flux adds -∮<SA(nu)U,U>; their sum is <= 0 by the display. The
∂O portions are hypothesis-restricted to walls (zero, Lemma 1.3) and margin
interface (>= 0 the right way, Lemma 1.2). Physics attack tried: is
lambda_max = |u| + c actually the sharp bound for A(nu) over all nu — yes,
max over nu of the largest eigenvalue u·nu + c is attained at nu = u/|u|;
no faster mode exists in the linearized system (entropy/shear ride u). The
frustum hypothesis correctly excludes non-wall/non-interface boundary
contact. The promotion SCHEMA -> THEOREM is earned. No break.

### Leg 14 — Proposition 1'' bootstrap (t* maximality, modulo (H-UP)).
### VERDICT: OBJECTION L1-7 (REPAIR-NEEDED).

**L1-7 (leg 14) — REPAIR-NEEDED: the bootstrap's central step draws a
boundary-trace conclusion from a compactly-contained-interior statement — a
non sequitur as printed; (H-UP) as stated (uniqueness + propagation of
support) does not deliver the face-trace vanishing that the continuation
needs, because the face trace is exactly the coupling channel that (H-UP)
treats as data.**

Quote (DOC-3, Proposition 1'' proof): "by (H-UP) finite speed, support
entering through Gamma_in^coll after t* needs positive time to reach any
fixed interior point, so there is eps_1 > 0 with U == 0 on
Omega_int' x [t*, t* + eps_1] for every compactly-contained Omega_int' — in
particular the interior-side trace feeding Gamma_in^coll stays zero on
[t*, t* + eps_1]."

Attack at derivation level. Two defects, one fatal to the step as printed:
(i) quantifier order — eps_1 is displayed before "for every compactly-
contained Omega_int'", but eps_1 must scale like dist(Omega_int',
Gamma_in^coll)/lambda_glob and degenerates to zero as Omega_int' exhausts
Omega_int: no uniform eps_1 exists. (ii) The "in particular": the trace ON
Gamma_in^coll lies in NO compactly-contained Omega_int' — the conclusion
"U == 0 on compactly-contained subsets for a set-dependent time" cannot
reach the boundary trace at the face. And the gap is not cosmetic: the face
trace is precisely the two-sided coupling channel. Propagation-of-support
for the INTERIOR problem is relative to the face data (which (H-UP)
declares to be the coupling input): with zero initial data it controls U
only OUTSIDE the lambda_glob(t - t*)-neighborhood of the face, while a
characteristic arriving AT the face at time t* + s originates, at time t*,
INSIDE that uncontrolled strip — whose values are influenced by the face
data, which the collar returns as a functional of the same trace
(Theorem 1' determines the collar FROM its face data). The printed argument
is therefore circular exactly at the face: breaking the circle needs either
(r-a) a strengthened (H-UP) that includes trace-level determinism — zero
data + zero face input on [t*, t1] forces the interior's OUTGOING
characteristic trace at the face to vanish on [t*, t1] (a transmission-
problem property, i.e. exactly the NG-9 machinery, folded into the
hypothesis statement), or (r-b) a two-sided lens-shaped energy argument
straddling the face (collar side: Lemma 1.4's frustum with W^{1,infinity}
coefficients; interior side: the (H-UP)-class estimate), which is a real
argument, not a gloss. Since Proposition 1'' is already conditional and
NG-9 already gestures at transmission conditions, the repair is a
statement-level strengthening of (H-UP) plus an honest rewrite of the
bootstrap paragraph — hence REPAIR-NEEDED, not BREAKS: but as printed the
proof of "THEOREM modulo (H-UP)" does not go through from (H-UP) as stated.
(Not a re-raise: R2-O2 demanded the collar/bootstrapped form; this attacks
the r2-new bootstrap itself.)

### Leg 15 — Lemma 3.2 (monotone-intersection; uniform pure-pressurization
### scope). VERDICT: CONFIRMED.

I re-derived the intersection argument: with the 1-family curve through W_1,
u_m = u_1 - f_1(p_m), f_1 increasing, f_1(p_1) = 0, and the 3-family curve
through W_d, u_m = u_d + f_d(p_m), f_d increasing, f_d(p_d) = 0 (both
standard monotone parametrizations for the convex-EOS package, correctly
cited to Menikoff-Plohr §V under (G4) + Gruneisen > 0, the latter verified
in-document as G = R/c_v), velocity matching at u_d = u_1 reads
g(p_m) := f_1(p_m) + f_d(p_m) = 0 with g strictly increasing,
g(p_1) = f_d(p_1) < 0 (p_1 < p_d, f_d increasing through zero at p_d) and
g(p_d) = f_1(p_d) > 0: unique root in (p_1, p_d), hence Pi_left < Pi_d.
Physics cross-check: the resolution of a co-moving pure overpressure is a
1-shock (compressing the stream to p_m > p_1) + contact + 3-rarefaction
(expanding the driver from p_d to p_m) — middle pressure strictly interior,
as the lemma says; and a deceleration u_d < u_1 shifts the matching to
f_1 + f_d = u_1 - u_d > 0, raising the root — confirming both the
conservatism direction and the reality of the scope restriction (the
deceleration control in the falsifier tests exactly this). The load-bearing
scope declaration (uniform state, pure pressurization ONLY; deceleration and
nonuniform-propagation legs = NG-10) is honest and correctly wired into
(M-b). Attack tried and failed: a vacuum/no-intersection configuration —
impossible on the compression side (sign change of g on [p_1, p_d] is
unconditional). No break.

### Leg 16 — Corollary 4 row-(a) in-class transport restatement. VERDICT:
### CONFIRMED.

In the 1-D normal-incidence class with u_0 > c_0: all five characteristic
speeds u_0 - c_0, u_0 (x3), u_0 + c_0 are positive; the incoming count at
x = 0 is five (full state — matching Lemma 1.2's count via the downstream-
side reading) and zero at x = L, so the solution is a finite composition of
downstream constant-speed transport solves from initial data + inflow
traces: existence, uniqueness, continuous dependence are explicit, and no
upstream-running family exists — R1 and R2 both hold in-class, THEOREM by
exhibition. The r2 discipline separating the multi-D reading (Friedrichs/
Lax-Phillips/Rauch existence + NG-3 corners, THEOREM*) from the in-class
THEOREM label is exactly right and closes the r2 refuter's overreach.
Attack tried: whether the "no condition admissible at x = L" clause hides a
weak-boundary-layer subtlety — it does not in this class (no incoming mode
exists to prescribe; any added condition over-determines, which is quadrant
(c)'s content, not row (a)'s). No break.

### Leg 17 — Remark 1.5.5 (ii') measurable-field restatement. VERDICT:
### CONFIRMED with one AMENDMENT (L1-8).

The core is right: with N(x) measurable and <S A(n)V, V> >= 0 on N(x), the
Gamma_in term of (EI) enters with the good sign (-∮ <= 0) and Gronwall runs
verbatim; hypothesis (ii) is the N = {0} special case; the homogeneous-
difference reading of a shared maximal-nonnegative BC is the standard
special case and the sign convention is consistent with (BQ) (checked: the
wall subspace u'·n = 0 at u-bar·n = 0 gives boundary form exactly 0, so the
quoted example subspace is admissible). The characteristic-inflow scoping —
restricting "prescribed incoming characteristic components" to the
non-characteristic constant-multiplicity part of Gamma_in — is the correct
repair, and the injector-rim grazing caveat is physically apt. One
mechanism-level wording defect:

**L1-8 (leg 17) — AMENDMENT/wording: "the acoustic eigenprojectors
degenerate" is the wrong mechanism; what degenerates at u-bar·n in
{0, -c-bar} is the sign classification (incoming/outgoing split), not the
eigenprojectors.**

Quote (DOC-3, Remark 1.5.5): "at sonic-inflow points (u-bar.n = -c-bar) or
grazing points (u-bar.n = 0 ...) the incoming count jumps and the acoustic
eigenprojectors degenerate (Lemma 0.2 arithmetic: 1/c factors against
closing spectral gaps), so 'the same characteristic components' is pointwise
ill-defined there."

Attack: at fixed state with c > 0 the eigenvalues u·n - c, u·n, u·n + c keep
MUTUAL gaps equal to c — the gaps do not close as u·n crosses 0 or -c, and
the spectral projectors of A(n) (Lemma 0.2's eigenvectors r_∓ = (rho, ∓cn,
rho c^2), r_s, r_{t_i}) are perfectly regular there: nothing in the
eigenstructure degenerates. What jumps is the classification of a FIXED,
regular mode from outgoing to incoming as its eigenvalue crosses zero —
i.e., the subspace-valued map "span of incoming modes" is discontinuous (and
at the crossing point ill-defined), which is the true and sufficient reason
the prescription fails to define a measurable N(x) across those loci. The
conclusion and scoping stand; the parenthetical mechanism ("1/c factors
against closing spectral gaps") describes a c -> 0 degeneracy that is not
the one at issue and should be rewritten as the sign-classification jump.
Not a break.

### Leg 18 — the Lopatinskii display. VERDICT: CONFIRMED.

Verified by the normal-mode computation for the half-line problem x < L with
boundary at x = L: Laplace modes e^{st + kappa x} with kappa = -s/lambda per
decoupled family; for Re s > 0, decay as x -> -infinity requires
Re kappa > 0, i.e. lambda < 0 — the stable subspace at x = L is exactly the
span of the single incoming R_- mode (dimension 1 = number of boundary
conditions, correct Kreiss count). The boundary operator R_- - r R_+ applied
to that basis vector has coefficient 1 on the sole incoming amplitude —
frequency- and r-independent, uniformly nonzero: the display "identically 1"
is exact, and the accompanying honesty note (the explicit construction
suffices without invoking Kreiss; there is no reflection loop at this BC
pair since R_- exits at x = 0 into prescribed-R_+ territory) is consistent
with the fourth falsifier leg's single-reflection predicate. Attack tried
and failed: hunting an r-dependence or a frequency where an outgoing mode
enters the stable subspace — impossible at constant coefficients with fixed
signs u_0 ± c_0, u_0 in the subsonic band. No break.

==============================================================================
## Summary table

| Leg | Target | Verdict |
|-----|--------|---------|
| 1 | [L-INC], both strata | CONFIRMED |
| 2 | [L-STD] no-topology pointwise argument | CONFIRMED |
| 3 | periodization step | CONFIRMED (AMENDMENT L1-1) |
| 4 | [P-HB3](i') data-space mollification | CONFIRMED |
| 5 | G8/r2 repricing | OBJECTION L1-2 (REPAIR-NEEDED) |
| 6 | D.18 singular leg + both iffs + atom bookkeeping | OBJECTION L1-3 (BREAKS-THE-LEG, first iff); L1-4, L1-5 (AMENDMENT); singular leg + second iff confirmed |
| 7 | D.2 psi-existence + H-CVX arc | CONFIRMED (AMENDMENT L1-6) |
| 8 | D.16 gross normalizer | CONFIRMED |
| 9 | D.20 contact split RH algebra | CONFIRMED (third independent re-derivation) |
| 10 | D.10 theta-halves exhibit | CONFIRMED |
| 11 | D.8 plane-stress census rewording | CONFIRMED |
| 12 | Theorem 1' collar form | CONFIRMED |
| 13 | Lemma 1.4 finite speed | CONFIRMED |
| 14 | Proposition 1'' bootstrap | OBJECTION L1-7 (REPAIR-NEEDED) |
| 15 | Lemma 3.2 monotone intersection | CONFIRMED |
| 16 | Corollary 4 row-(a) in-class | CONFIRMED |
| 17 | Remark 1.5.5 (ii') | CONFIRMED (AMENDMENT L1-8) |
| 18 | Lopatinskii display | CONFIRMED |

Counting convention: a leg is CONFIRMED iff it carries no BREAKS-THE-LEG and
no REPAIR-NEEDED objection (AMENDMENT/wording objections do not unseat a
leg). Confirmed: 15/18 (all but legs 5, 6, 14).

OVERALL: 8 objections, of which 1 BREAKS-THE-LEG
(L1-1 A, L1-2 R, L1-3 B, L1-4 A, L1-5 A, L1-6 A, L1-7 R, L1-8 A).

==============================================================================
## Falsifier for this pass (rejecting tests against MY verdicts)

- Kills L1-3 (the one BREAKS): a proof that Exact(V) = 0 implies K(V) = 0
  for the distributional K of D.18 — i.e. a derivation of the printed first
  iff's forward direction from the operator identity Exact = Reduced + K —
  or a demonstration that example (α) fails to be an exact distributional
  solution or fails to have a nonzero K atom. Any of these refutes my
  reading and restores the display.
- Kills L1-2: a proof that the §1 gas model (Gibbs closure + c^2 > 0 +
  theta > 0 alone) implies convexity of W ↦ -rho S in conservative
  variables at abstract EOS — equivalently that e_SS > 0 is derivable from
  those hypotheses. (I claim it is independent; an in-class EOS with
  e_SS <= 0 somewhere on K witnesses independence — exhibiting such an EOS
  CONFIRMS my objection, deriving e_SS > 0 REFUTES it.)
- Kills L1-7: a derivation of the face-trace vanishing on [t*, t* + eps]
  from EXACTLY the printed (H-UP) (interior uniqueness + propagation of
  support with the face trace as data) — e.g. a valid argument that the
  interior's outgoing characteristic trace at the face vanishes without any
  transmission-level hypothesis. That would restore the bootstrap as
  printed.
- Kills any CONFIRMED verdict: a derivation-level counterexample to the
  named strongest-attack analysis of that leg (e.g. for leg 9: an unsteady
  lab-frame RH computation with sigma_n = Omega r n_theta yielding
  m[I] != 0 at m != 0; for leg 13: a unit nu and margin state with
  lambda_max S + S A(nu) not PSD; for leg 15: a convex-EOS instance with
  Pi_left >= Pi_d at u_d = u_1). Each CONFIRMED section names the attack it
  survived, so each is independently re-attackable at that point.
- Amendment objections (L1-1, L1-4, L1-5, L1-6, L1-8) are each killed by
  showing the quoted sentence true AS PRINTED under its literal reading
  (e.g. for L1-1: a finite value for the summed pairing against the full
  partition of unity for a nonzero T-periodic mu; for L1-6: a proof that
  arc-GNL implies arc-G_fund > 0).

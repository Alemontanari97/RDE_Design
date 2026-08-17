# ADVERSARIAL REFUTATION — [S-T0P]/[T-T0P] proof document, ROUND 3, LENS 1
# (hyperbolic-PDE structure: characteristics, admissibility, front
#  conditions, symmetry/group-action correctness, physics of the reduction)

Target: validation/sfoundations_raws_2026-08-13/phaseD/phaseD_stop_proof.md
(revision 1 of 2026-08-17, post round-1 disposition per its §10).

FILE-NUMBERING NOTE (audit transparency, SR discipline): this refuter was
tasked with "round 1" and the output path refute_S-T0P_r1_l1.md. That file
EXISTS on disk (mtime 08:10), is an of-record artifact, and is CONSUMED by
the target's §10 revision log, which cites its findings F1-F10 by number;
overwriting it would falsify the audit trail. Round-2 files for both lenses
also exist (r2_l0 08:31, r2_l1 08:34), postdating the revision (doc mtime
08:21) and NOT yet consumed. This attack is therefore filed at the next
free slot for this lens, ROUND 3, against the same revision-1 text that
round 2 targeted. Dedup discipline: every objection below was checked
against ALL FOUR existing lists (r1_l0 F1-F12, r1_l1 F1-F10, r2_l0
F1-F11, r2_l1 F1-F9 — 42 items); each finding states why it is not a
duplicate. No file other than this one was modified.

METHOD: full read of the revised document; independent re-derivation of
the load-bearing algebra (re-confirmed sound this round, see section A);
targeted hunt in the regions the two round-2 refuters did NOT open: the
H9/G4 interface-geometry clause, the corollaries, the H6' class
bookkeeping under t-periodicity, and the regularity class of the front
conditional. Binding standard applied: SOTA rigor, label accuracy,
per-statement gamma status, rejection-capable falsifiers, absence of
known literature routes.

==============================================================================
## A. RE-VERIFIED SOUND THIS ROUND (no objection; independent re-derivation)

 A1. [L-XC3D] (KEY) re-derived by the shortest route: dp = -m1 du from
     the frozen momentum flux gives dp/rho + u du = 0 identically, so
     dh + u du = theta dS = -dbeta in one line; S''(0) = -1/(theta m1^2),
     h_ww = g'/(theta rho u). Dimensional check performed
     (beta is specific-enthalpy-like, [dS/dbeta] = 1/K): consistent.
     Parity zeros of the mixed m_w entries confirmed.
 A2. [L-XWALL3] 5-component solve re-derived (d(rho u) = 0, dH = 0
     => theta dS = -p'(u.n)/(rho u) = 0 at slip): correct at abstract
     EOS, as a STATE-level identity (the r2 objections to its
     trace-level APPLICATION stand; nothing new to add there).
 A3. [L-XSON3] parity/rotation factorization det J_5 = (rho u) det J_4
     at w = 0: confirmed.
 A4. [L-XREC] recovery lines and the reduction to the 1-D triple:
     confirmed (modulo r2-l0-F8's both-roots-in-K correction to the
     biconditional, which I confirm and do not repeat).
 A5. [L-COMPAT] both steps, including D_M eta = D_W E: confirmed.
 A6. §2 group algebra: (ACT) is a genuine G_full-action; L-EQV1's
     dyadic covariance computation, L-INV's shift computation, and the
     [T-T0P-E] assembly (S1-anchored uniqueness consumed only on
     S1-vs-S1 pairs) are correct as logic. L-STD's countable-dense
     closure is correct (modulo r2's closedness/eps_n repairs, not
     repeated).
 A7. Characteristic structure in L-SPACE (speeds u.xi mult. 3,
     u.xi +- c; x-components >= u - c on K): confirmed.
 A8. [P-HB2] Fourier/linearity argument and the k = 0 (axisymmetric
     mean) line imposing no constraint: confirmed.

==============================================================================
## B. NEW OBJECTIONS (none repeats any of the 42 prior items)

------------------------------------------------------------------------------
### F1 — H9/G4: "spacelike ... GUARANTEED by the L4 margin (L-SPACE)" is
### FALSE for a general interface; the needed condition is NORMAL (not
### axial) supersonicity, it is absent from H2/H9/G4, and it FAILS at
### modest interface tilt inside the declared K. G4's "geometric
### bookkeeping" pricing additionally hides a foliation condition and a
### direction-dependent re-instantiation of the H5' box clause.

ATTACKED TEXT: H9: "or more generally a spacelike surface (guaranteed by
the L4 margin, L-SPACE below) that can be mapped to {x = 0} by a C^1
change of the marching variable"; G4: "spacelike reparametrization of
the march (standard, geometric bookkeeping; L-SPACE guarantees
spacelikeness)"; H2's contract wording "every patch axially supersonic
with margin, so full-state data are the well-posed contract".

OBJECTION (characteristics — the core competence of this lens).
L-SPACE proves spacelikeness of the COORDINATE slices {x = const} and of
nothing else: its computation bounds the x-components of the
characteristic speeds, i.e. it controls the direction e_x. A general
axisymmetric Gamma_d with unit downstream normal n = (n_x, n_r, 0) is
spacelike iff ALL characteristic speeds in direction n are positive,
i.e. iff the NORMAL Mach number exceeds one:

    u.n - c = u n_x + u_r n_r - c > 0   on the K-trace states.

The L4/H5' package bounds the AXIAL margin (u - c >= delta) and the
transverse magnitude (q_perp <= 0.8 c). These do NOT imply the normal
margin for tilted patches. Explicit counter-region INSIDE the declared
K (refutation exhibit, inline arithmetic, not a number-of-record): take
u = 1.2 c (a comfortable axial margin), u_r = -0.8 c (admissible:
q_perp = 0.8c), and a meridional tilt of 20 degrees (n_x = cos 20 ~
0.940, n_r = sin 20 ~ 0.342):

    u.n = 1.2 c (0.940) - 0.8 c (0.342) ~ 0.854 c  <  c.

The patch is NOT spacelike: the incoming acoustic characteristic u.n - c
< 0 travels UPSTREAM through it, the full-state data contract loses its
well-posedness rationale on that patch (one characteristic family
carries information from the interior back to the "data" surface), and
every downstream brick that anchors at Gamma_d (the Sigma_0 term of the
§4 budget, the H2 trace contract, the H9 remap) loses its hypothesis.
At 45 degrees the failure is drastic (u.n ~ 0.28 c). So the
parenthetical "guaranteed by the L4 margin" is false as mathematics:
axial supersonicity does not survive projection onto a tilted normal
once the transverse Mach budget of H5' is spent against it.

SECOND LAYER (the remap). Even where Gamma_d IS spacelike, the H9
device "map to {x = 0} by a C^1 change of the marching variable"
requires a spacelike FOLIATION: every level set {x_tilde = const} of
the new marching variable between Gamma_d and the exit must be
spacelike, not just the two end surfaces — the Gronwall budget of §4 is
run on the full one-parameter family of slices. This foliation clause
appears nowhere. It is an open condition, generically satisfiable for
mild tilts, but it is a CONDITION, and for steep Gamma_d (per the
computation above) no admissible foliation exists at all.

THIRD LAYER (the bricks are direction-specific). Under the remap the
evolution flux becomes the tilted combination F_n = n_x F_x + n_r F_r
with a SPATIALLY VARYING direction n(x, r). The §3 bricks are proven
for the fixed direction e_x. By the rotational covariance of Euler they
transfer to any fixed direction with u.n > c — but with the Mach pair
of the certificate re-read in the tilted frame: (M_n, V_n) =
(u.n/c, |u - (u.n)n|/c). The [X-IVXC]/[T-XRED] certificate is consumed
at the TILTED pair, which differs from the axial pair; the H5' box
clause must be re-checked per direction along the foliation (the same
genus of domain hole that l1-F4 found for q_perp and r2-l0-F7 found
for the axial range — here it is generated by GEOMETRY rather than by
the state, which is why neither prior finding covers it). L-XWALL3 is
the one brick that is already direction-general (proven for arbitrary
n) — the document should say that the OTHERS are not.

CONSEQUENCE FOR LABELS: G4 is currently priced as "standard, geometric
bookkeeping" with a false "guarantees" attribution. Honestly stated,
G4 contains: (g4-a) a scope restriction on Gamma_d (uniform normal-Mach
margin u.n - c >= delta_n > 0 over K-trace states — an instance
certificate, same rank as the H5' clauses, checkable a posteriori);
(g4-b) the spacelike-foliation clause; (g4-c) the per-direction box
re-instantiation for the convexity certificate. With Gamma_d = a
coordinate cross-section (the primary case) all three are vacuous and
nothing in §4-§5 is touched — the defect is confined to the
"more generally" branch of H9, but that branch as printed is an
over-claim signed by a lemma that does not prove it.

WHY NEW: l1-F5/l0-F11 attacked L-SPACE's determinacy overreach (fixed
by re-scoping the LEMMA); nobody audited H9/G4's converse direction —
the attribution TO L-SPACE of a property of surfaces L-SPACE never
touches. r2-l0-F7 is about the axial-Mach range of K inside a fixed
axial reading; this finding is about the direction of the slicing
itself. No overlap.

SEVERITY: MEDIUM-HIGH within its scope (a false "guaranteed" clause of
record inside a hypothesis block + a named gap whose pricing hides two
conditions and an instance certificate; the primary cross-section case
is unaffected, which caps the severity below label-breaking).

FALSIFIER OF MY OBJECTION (executable now, symbolic): show that
u n_x + u_r n_r - c > 0 holds on all of K for all unit normals with
n_x > 0 — refuted by the exhibited state, so instead: show the H5'/L4
certificates of record contain a clause bounding interface tilt that I
have missed (a grep of the transfer doc / H2 sources for a normal-Mach
or tilt clause).

REPAIR: restate H9 with (g4-a); move the "guaranteed" parenthetical to
"guaranteed FOR CROSS-SECTIONS by L-SPACE; for tilted Gamma_d =
instance certificate (g4-a)"; extend G4 with (g4-b)/(g4-c); add the
normal-Mach check to the same a-posteriori instance battery that
checks H5'.

------------------------------------------------------------------------------
### F2 — COROLLARY 5.1 overreaches the marched domain: "steady thrust
### through EVERY axisymmetric surface" is not delivered by a theorem
### whose conclusions live on Omega_march only.

ATTACKED TEXT: Cor 5.1: "T-T0's conclusions (steady thrust through
every axisymmetric surface; wave-frame steady momentum balance) hold
for every certified solution in the t-periodic class, not only for
assumed patterns."

OBJECTION. The l1-F10(a) repair correctly re-scoped every uniqueness
and steadification conclusion to Omega_march x R_t ("upstream-of-
Gamma_d points are not marched"). Cor 5.1 was not swept: it discharges
the [T-T0] hypothesis "for every certified solution", quantifying over
"every axisymmetric surface" with no domain restriction. For a thrust
surface (or control volume for the momentum balance) that intersects
the un-marched region upstream of Gamma_d, [T-T0P] says NOTHING about
the field, hence nothing about steadiness of the flux through it; the
corollary as printed re-imports exactly the overreach that F10(a)
removed from the parent theorem. Same defect, smaller print: [T-SLRW]
"applies with its m-content read off q_tilde" — q_tilde exists on
Omega_march only.

WHY NEW: no prior item touches Cor 5.1 or Cor 5.2 (r1's F10(a)
targeted the theorem statements; both r2 files audit §4/§5/§6 but not
the corollaries).

SEVERITY: LOW-MEDIUM (a quantifier overreach in a discharge statement
that the §8 M0 delta would propagate into [T-T0]'s site of record —
cheap to fix, expensive if enshrined).

REPAIR: "every axisymmetric surface CONTAINED IN cl(Omega_march)" and
"momentum balance on control volumes within cl(Omega_march)"; add the
same clause to the §8 delta instruction for [T-T0]/[T-SLRW]
consumption.

------------------------------------------------------------------------------
### F3 — [C-MAJDA-3DT]/G3 under-specifies the REGULARITY CLASS of its
### own discharge: multi-D front stability/uniqueness theory does not
### exist at the H6' piecewise-C^1 regularity, so the conditional as
### minted is not yet a certifiable target.

ATTACKED TEXT: G3's content specification: "uniform Kreiss-Lopatinskii
stability + front-crossing uniqueness for the multi-D UNSTEADY fitted
front (hypersurface in (x,y,z,t); frequency variables (eta_y, eta_z,
sigma_t)), evaluated on the certified compact front set"; H6'-B
("piecewise C^1 ... finitely many transversal C^1 front
hypersurfaces").

OBJECTION (front-condition competence of this lens; DISTINCT from the
two prior G3 attacks — dedupe stated below). Grant the geometry
(persistent or crossed) and grant a verified KL condition on the front
set. The literature body that G3's own falsifier and discharge route
appeal to — Majda's shock stability/existence, Metivier's uniform
stability theory, Coulombel-Secchi's weak-stability continuation — is
a theory of fronts between H^s SOLUTIONS with s large (weighted
anisotropic Sobolev spaces, loss-of-derivative estimates, plus corner/
initial compatibility conditions to all orders). There is NO
stability-or-uniqueness technology for multi-D fronts between merely
piecewise-C^1 states: the paradifferential machinery that converts a
KL determinant into an energy estimate does not run at C^1, and the
document's S1 class (H6', Li Ta-tsien piecewise-C^1 semi-global
framework) sits exactly there. Consequences:
 (a) [C-MAJDA-3DT] as minted specifies WHERE it is evaluated (the
     certified front set) and in which FREQUENCY variables, but not in
     which SOLUTION class its uniqueness half is supposed to hold.
     A conditional without a stated class is not a certifiable
     registry object: two readers can discharge/refute different
     statements under the same label. (This is a registry-hygiene
     defect in the mint itself, beyond r2-l1-F2(c)'s falsifier-split
     point.)
 (b) The gap between the H6' class (piecewise C^1) and the class where
     the cited machinery lives (H^s, s > threshold, with
     compatibility) is itself a NAMED-GAP-rank item: either H6'-B must
     be strengthened to the Sobolev front class on stratum (B) (a
     scope restriction on which S1 elements the stratum covers — and
     then S1 instance certification must check MORE than
     boundary-function margins), or G3 must carry an explicit
     "regularity bridge" sub-gap (uniqueness at piecewise-C^1 via
     front theory = open even in 2-D steady).
 (c) The declared falsifier (vanishing bordered Lopatinskii
     determinant on the front set) is computed from the FRONT STATES
     and is insensitive to the class mismatch: it can neither confirm
     nor reject the uniqueness half in the class where the theorem
     needs it — consistent with r2-l1-F2(c) but for an independent
     reason (class, not bundling).

WHY NEW: l0-F2 (round 1) attacked the planar-steady -> multi-D-unsteady
DIMENSION jump and forced the G3 mint. r2-l1-F2 attacked the front
GEOMETRY (persistent vs crossing) and the falsifier bundling.
Neither raised the solution-REGULARITY class in which the conditional
is to be discharged; the point is orthogonal to both (it survives any
geometric reformulation and any falsifier split).

SEVERITY: MEDIUM for the G3 registry row design (stratum (B) is
already SCHEMA, so no label falls; but the row as proposed in §8/§9
would enter the registry under-specified, and the corpus discipline —
navigation-first, claim-by-label — makes an ambiguous conditional a
propagating defect).

REPAIR: add to G3's content line: "in the front-solution class
[NAME IT: H^s piecewise, s >= s_0(d), with front compatibility], with
the H6'-B piecewise-C^1 membership related to it by [bridge clause:
instance certification of the stronger regularity, or an explicit
open-gap flag]"; mirror the class in the falsifier line.

------------------------------------------------------------------------------
### F4 — H6' front bookkeeping is inconsistent with the t-periodic
### class it serves: "finitely many ... front hypersurfaces" on
### cl(Omega_march) x R excludes every T-periodic candidate with
### per-period front events, silently thinning the S1 class toward the
### steady-pattern conclusion.

ATTACKED TEXT: H6': "The distinguished solution q is piecewise C^1 on
cl(Omega_march) x R with finitely many transversal C^1 front
hypersurfaces"; its interaction with H8' (ALL class elements
T-periodic).

OBJECTION (class-design / physics of the reduction). On the infinite
time line, a T-periodic field whose front set has any t-localized
component (a front sheet that forms and dies within a period — e.g. a
periodically re-forming shocklet, exactly the kind of unsteady residual
whose EXCLUSION is the theorem's job to prove, not to assume) has
COUNTABLY many front sheets in Omega_march x R: one copy per period.
H6' as literally written ("finitely many ... on cl(Omega_march) x R")
excludes such fields from the S1 class BY HYPOTHESIS. The only front
configurations compatible with (finitely many) + (T-periodic) are
t-invariant-or-helical sheets unbounded in t — i.e. the front geometry
of the steady co-rotating pattern. So statement (i) ("every S1-class
solution is a steady pattern"), read against the literal H6', is
quantified over a class whose front bookkeeping already excludes the
natural non-steady candidates: part of the conclusion is smuggled into
the class definition. This does NOT create a circularity in the proof
chain (the H7' competitors carry no front-count clause, so canonicity
(ii) is untouched, and the §4 argument on the torus slab is
indifferent), but it WEAKENS claim (i) below its advertised strength
in exactly the way the document's own honesty discipline (the H8'
"CONSEQUENCE OF THE HONEST QUANTIFIER" paragraph) requires to be
declared — and it is not declared.

WHY NEW: l0-F9 (round 1) attacked the missing ADMISSIBILITY clauses of
H6 fronts (fixed as H6'); r2-l1-F2(a) attacked the undefined
"transversal". The finiteness-vs-periodicity clash is a third,
independent defect of the same block, created by the l0-F5/l1-F2
repair (H8' now binds the strong side, making the clash live) — it
could not have been raised against round 0, where the strong side had
no periodicity clause.

SEVERITY: LOW-MEDIUM (write-up/class-design; one-line repair; no
label falls, but the (i) quantifier note in §5 should mention it
alongside the H8' caveat).

REPAIR: count fronts on the torus slab: "finitely many transversal C^1
front hypersurfaces in cl(Omega_march) x T_t (equivalently: finitely
many modulo T-periodicity)". This admits per-period front events into
the S1 class; the §4(B) machinery sees them through the same G3
conditional, so nothing else changes.

------------------------------------------------------------------------------
### F5 — §9's "no new NUMBERS are claimed" sentence is falsified by the
### revision's own 1.13c exhibit (R5 hygiene nit).

ATTACKED TEXT: §9 falsifier table: "per R5 no new NUMBERS are claimed
in this document (the only closed form, h_ww = g'/(theta rho u), is
symbolic)"; versus H5'/L-XC3D(i): "a per-component 0.8c box would
reach q_perp ~ 1.13c, OUTSIDE the certificate" (revision-1 text, the
l1-F4 repair).

OBJECTION. 1.13 is a number of record in a hypothesis block (it is the
recorded justification for a STRENGTHENED hypothesis clause — H5''s
Euclidean q_perp bound — and §10 cites it as "the 1.13c counter-number
recorded"). It is derivable inline (0.8 sqrt(2) ~ 1.131), but the §9
sentence claims the document contains no new numbers AT ALL, which is
now literally false, and the R5 bar the sentence invokes ("no number
without script + test") is exactly the bar the 1.13 does not meet as
presented. Cheapest honest fix: state the derivation in place
("q_perp = 0.8 sqrt(2) c ~ 1.13c, inline arithmetic") and reword the
§9 sentence to "no new MEASURED numbers; the two symbolic/arithmetic
values (h_ww closed form; 0.8 sqrt(2) c) are derivations, not
measurements". Alternatively add the q_perp box arithmetic to the
[X-T0P] battery (one assert).

WHY NEW: the 1.13c text and the "no new numbers" sentence are both
revision-1 insertions; no prior item compares them.

SEVERITY: LOW (hygiene; but this document's currency is exactly this
kind of honesty, and the sentence is quotable).

==============================================================================
## C. ABSENCE SWEEP (this round's additions)

The r2 files already named: convex-integration axis (consumed),
characteristic-boundary DM-trace literature (r2-l0-F2), time-periodic
classical solutions line (Qu; Yuan school — r2-l1-F3). This round adds
ONE absence, attached to F1: the supersonic-marching literature's OWN
treatment of tilted initial/data surfaces (space-marching PNS/Euler
codes and the classical method-of-characteristics initial-surface
condition: the data surface must be spacelike with respect to the
LOCAL Mach cone — normal Mach > 1, not axial Mach > 1; e.g. the
initial-value-surface condition in Zucrow-Hoffman Ch. 17 and the MoC
literature of record IN THIS REPO's own GENO audit). The document's
own house corpus states the correct condition; H9 cites the wrong
lemma instead. No new external procurement needed — the repair is
navigable in-house.

==============================================================================
## D. VERDICT

The algebraic and group-theoretic core survives a third adversarial
pass untouched (section A) — the document is converging. The new
findings are: one false attribution with a concrete in-K counterexample
and two hidden conditions inside H9/G4 (F1 — the only finding of this
round with mathematical content against a hypothesis block); one
domain-quantifier overreach in a corollary that the M0 delta would
propagate (F2); one under-specified registry mint (F3); one
class-design clash between H6' finiteness and H8' periodicity (F4);
and one R5-hygiene falsehood in §9 (F5).

None of these breaks the architecture or kills a THEOREM-labeled
statement: F1 is confined to the "more generally" branch of H9 (the
cross-section primary case is clean); F2-F5 are statement-hygiene and
registry-design repairs. Combined with the still-unconsumed round-2
lists (whose findings I independently confirm where I re-derived them:
r2-l0-F8's biconditional correction, r2-l1-F6's gamma accounting), the
document is NOT yet sound as labeled, but every defect on file has a
named, bounded, in-session repair.

VERDICT: REPAIRABLE.

Requested revision-2 actions from THIS file: restate H9 + extend G4
with (g4-a)/(g4-b)/(g4-c) and the normal-Mach instance check; scope
Cor 5.1/5.2 to cl(Omega_march); add the regularity-class clause to
G3's mint; re-count H6' fronts on the torus slab; fix the §9 numbers
sentence. All are local; none requires new mathematics beyond the
(g4-a) certificate design.

Lens: hyperbolic-PDE structure (l1). Round: 3. New objections: 5.

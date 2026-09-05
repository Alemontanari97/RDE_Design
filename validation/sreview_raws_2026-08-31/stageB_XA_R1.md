# Stage-B item XA — REFUTER round 1 (of at most 2)

Refuter persona: the certification-stack maintainer who ran the S22 locus
diagnosis (validation/PROGRESS_2026-08-11_S22_governor.md, T2 = log step 5)
and re-ran it under the closure-aware staleness gate at F2-B0 (2026-09-05).

Files read in full or at the cited anchors (no summaries):
stageB_items.json (XA); stageB_XA_A0.md; docs/rde_nozzle_MASTER.md :3111-3116
(VI.2 monitor), :3486-3560 (ladder / margin multiplier / K_disc~A_0 CONJECTURE
+ named falsifier / taxonomy), :4185-4213 (S24 twin verdict, H-CLASS),
:4250-4275 (F2-B0 certificate version-binding); validation/PROGRESS_2026-08-11_
S22_governor.md :21-28 (C-1 table), :77 (T2 verdict), :79 (T4 census);
docs/claims_registry.yaml X-LOCD (:1332-1345), X-MGOV; docs/choice_ledger.yaml
C28 (:450-455); docs/findings_registry.yaml record-path:cert-verdict-recorder-
dependence (:319-328); validation/a1_ideal_march_jax.py :795-830 (certify());
validation/a1_toc_variational_jax.py :262-300; Rao & Beck 1994 AIAA 94-3264
(GENO/literature/rao-beck-2012-...pdf, registry rao_beck_1994, READ-INTEGRAL)
paper pp.2-3 [IO]; Sternin 1961 DAN SSSR 139(2):335-336 (literature/dan25254.pdf,
registry sternin_1961) pp.335-336 [IO, Russian original].

## 1. The falsifier — AGREED WITH THREE AMENDMENTS (binding text below)

The advocate's falsifier is the record's own named falsifier (M0 :3538-3543:
"evaluate the Eq. (4)/Sternin validity relation along the walk: it must
approach its boundary where certification degrades, else the bridge is dead")
and its executable form is on file (validation/locus_diagnosis.py, the C-1
three-way table, branch (c) = falsifier fires). I agree with it as the primary
falsifier, amended so that it cannot be argued around after the fact:

(F-XA-1, primary, quantified) "Healthy" is the PRE-REGISTERED rule of record,
not a judgement: a rejected cell is fold-implicated iff val_min < m_ref/K_RICH
(m_ref = min val over the certified baseline design-wall field; K_RICH = 4,
a1_ideal_march_jax.py:198). A certification failure whose argmax cell AND
whose whole-field val_min both sit at or above m_ref/K_RICH, with the argmin-
val locus off the terminal control-surface chain (distance > STENCIL_RADIUS x
local chain spacing), falsifies K_disc ~ A_0 on that instance.

(F-XA-2, the "conversely" clause is ONE-SIDED) Failures concentrated where val
-> 0 are NECESSARY for the identification, not sufficient: both readings
(physical boundary; numerical class that also breaks where the physics
breaks) predict them. Only the healthy-val failure discriminates. The support
half of the advocate's text is therefore struck as evidence; it remains a
consistency check.

(F-XA-3, structural, added) A_0 is a property of the physical field alone. If
the certification verdict of a FIXED design (fixed W, fixed marched field,
val field unchanged) changes under a change of the recorder or the env
fingerprint, then bd(K_disc) is not a function of the field and cannot be A_0
on that instance. One measured flip is a kill.

The advocate's own abandonment clause ("a certification failure at cells where
the validity monitor is healthy") is exactly F-XA-1. He wrote his kill
condition without checking whether the record had already met it.

## 2. Verdict on the agreed falsifier: it has ALREADY FIRED, three times

(I-1) S20 instance, S22 T2 [X-LOCD], PROGRESS_2026-08-11_S22_governor.md :77.
Five distinct rejected designs, cert_worst {1.170, 2.458, 1.060, 1.455,
1.698}. Threshold m_ref/K_RICH = 1.7209e-01 (m_ref = 6.8837e-01, 1675 pts,
all positive). val at the FAILING (argmax) cell: 0.7133 / 0.8574 / 0.8534 /
0.6512 / 0.8452 = 3.8x to 5.0x the threshold and 0.95x to 1.25x m_ref itself
— the failing cells are as healthy as, or healthier than, the certified
baseline's worst cell. Whole-field val_min 0.612-0.620 = 3.6x threshold,
INTERIOR, off-chain (d 1.52 vs r_st 0.082). Branch (c) unanimous 5/5. The
returned outcome-II base re-certifies (0.4851) with val_min/m_ref = 0.899: no
depression at the frontier. F-XA-1 fires on every one of the five.

(I-2) S22 T4 [X-MGOV] campaign, :79: margin-constrained walk at the TIGHTEST
rung mu_0_1 = 3.405e-01 (m_ref/2): seven rejections at cert_worst 1.531, margin
INACTIVE throughout, active-cusp census 0/0/0, min val 6.186e-01 interior.
If bd(K_disc) were A_0, a KS-min floor at half the healthy reference would
have activated BEFORE certification refused — it never did. The two
constraints are measured as distinct objects on the instance.

(I-3) S24 [X-DEFTW] deep-DEF instance, M0 :4189-4198: the walk "is stopped by
march CERTIFICATION at healthy val" with min DE val 7.31e-2 = 33x the
tightest pre-registered floor, active-cusp census 0/0 — "the THIRD measured
instance of the class-construction mechanism (S20, S22 mild; S24 deep-DEF)".

(I-4) F-XA-3 fires too: findings :319-328 and M0 :4254-4266 (2026-09-05, both
recorders, same tree, same designs): rej-1 and rej-4 CERTIFY on the per-column
recorder while the S22-certified base FAILS (2.023); on the per-cell recorder
rej-1/3/5 certify and the base passes (0.308). X-CDKAT cert_worst moved
2.106e-01 -> 1.813e-01 (−13.9%) under an env change alone. bd(K_disc) moved;
the val field did not. The negative-control O3.2 march is uncertifiable under
the current env on both record paths and on the pass-era tree (env-induced,
X-O32 declared FAILING) — a design whose physics did not change left K_disc.

The position is refuted on its agreed falsifier, on recorded instances, with
the executable instrument the advocate himself names. This is not a
projection: I ran it.

## 3. Objections on defects (all new — round 1)

O-1 [anchor defect, unrepairable as written]. A0 cites "memory of record of the
S20 adjudication (root cause = formulation gap, Sternin boundary as the
forbidden zone)". That reading was SUPERSEDED at S22 T2 (:77 (iv): "for the
S20 instance the certifiable-set boundary is NOT the validity boundary"), at
S24 (H-CLASS), and re-confirmed 2026-09-05. A0 never mentions X-LOCD, T2, the
0.61-0.86 numbers, or the C-1 table. The position is built on a memory the
record has already overturned; the pointers of the item definition name every
one of these files.

O-2 [factual error on the S20 signature, point 2]. "The optimizer pushes toward
a DEF-type coalescence at the control surface ... and the certificate refuses
it." The C-1(a) reading (argmin-val locus on the terminal C+) was tested and
FALSIFIED: the failing cells are near-axis interior, design columns 23-30, x ~
3.93-4.25, y ~ 0.05-0.14 (y_t = 1), never on the terminal C+, never adjacent
to the inserted knots (:77 (i),(iii)). The "signature of a design walking INTO
the forbidden zone" is the signature of Newton stalling at healthy cells.

O-3 [the certificate does not measure what the advocate says it measures].
certify() (a1_ideal_march_jax.py:795-830): ratio = |one extra Newton step at
the solution| / (NEWTON_TOL_FACTOR x eps x scale(z)) — a roundoff-floor
CONTRACTION test in z-space, "derived from the Newton contraction". A ratio
of 1.06-2.46 says the cell converged to 1-2.5 roundoff tolerances instead of
one. A geometrically degenerate cell (characteristics of one family
coalescing, val -> 0, the 4x4 system losing rank) produces ratios of the
class 5.44e7 (T1 STIM-2 starvation) or NaN -> inf (C2-F1). The frontier the
advocate wants to read as "the design has left the shock-free class" is a
factor-of-two-at-eps frontier; the findings row names the mechanism: "ulp
seed differences amplified through the damped-trial selection of a near-non-
convergent cell" (:323, mechanism seed-noise-at-marginal-cell). Point 1's
"where the physics degenerates, the numerics degenerate" is the RIGHT
direction of an implication that is only ever used in the WRONG direction.

O-4 [type error: A_0 of Sternin/Rao-Beck is not a per-cell field boundary].
Page-verified: Rao-Beck 1994 p.2 [IO] derive Eq. (4) "by logarithmic
differentiation of Equation (1) and seeking nontrivial solutions for d(alpha)
and d(theta) from Equations (1) and (3) ... at the point D"; Fig. 2 is a
boundary in the (theta_D, alpha_D) plane of the boundary-built family, and the
invalid region is where "no control surface and hence no optimum thrust
nozzle can be defined"; p.3: "the control surface computations cannot be
started from any of these invalid points". Sternin 1961 p.336 [IO]: dy/d(alpha)
along the extremal CB "passes through zero at some C0 ... geometrically a loop
at the base of the extremal; physically the impossibility of constructing
shock-free solutions of the variational problem for all points of the
characteristic ACP lying to the left of C0 that could serve as starting points
for constructing extremals". Both are CONSTRUCTIBILITY boundaries of the
control-surface extremal in the parameter space of an inverse-designed family.
K_disc is a subset of a 9/10-dof direct wall-spline class certified by an
interior forward march. The record's Lambda-form per-node val is a legitimate
GENERALIZATION (X-VMON, S4 evidence half), but the advocate's "Sternin's
boundary" language claims classical authority for an object the classics
never defined. The advocate's "[KNOWLEDGE, full]" tag on Rao-Beck is not
backed by the page: nothing on pp.2-3 speaks of "wall-reflected
characteristics" or per-cell degeneration. Depth claimed > depth held.

O-5 [the repair route is circular]. The only way to keep "K_disc ≈ A_0" alive
after (I-1)-(I-4) is to widen A_0 to the record's full A_t(mu_0), whose margin
vector includes "the uniform constants of the certified class D(delta, L_x,
C_geo, C_dat, h_min)" (M0 :3493-3497). Then A_0 contains h_min and the
recorder's contraction tolerance by definition, the identification becomes a
tautology, and the road consequence the advocate sells (point 4: a referee
reads the constraint as "shock-free class boundary") is exactly what is lost.
Either A_0 is physical (and the bridge is dead) or the bridge is true (and A_0
is no longer physical).

O-6 [point 3 contradicts the executed formulation]. "No re-formulation of the
certifier is needed" — but the margin-constrained formulation of record
(X-MGOV) was BUILT and RUN and measured inactive while certification rejected
(I-2). C28 (:450-455) records the consequence: incumbent "binary outside gates
only (quantifier bridge falsified)", successor = KS-max on traced per-cell
certification RATIOS (GAP-1) — a second, separate surrogate, precisely because
the fold margin cannot see the certification frontier. The F2.ENGINE duties
(findings :327: recorder pinned in every Verdict, 1/K_RICH ship-gate row,
X-LOCD re-form) exist because the certifier DOES need re-forming. Point 3
asks the loop to un-learn an executed result.

O-7 [scope defect for Q0]. The Lambda-form monitor is EOS-general but NOT
data-general: "homentropic-homoenergetic; F2 owns the extension; plug/C-
mirror unproven" (X-VMON scope). The RDE per-phase field is rotational
(VI.2). The road "read every per-phase certification failure as Sternin's
boundary" presumes a validity monitor that does not yet exist on the data
class Q0 is about. "Zero new machinery" (point 4) is false on the road's own
terms: the monitor extension is the machinery, and it is F2-owned and unbuilt.

O-8 [credibility claim inverted, point 4]. A referee handed "shock-free class
boundary" next to a table where the failing cells carry val 0.65-0.86 against
a healthy reference 0.69 and a fold threshold 0.17 catches the mislabel in
one line. Worse for the TWIN: (I-4) shows a marginal arm can flip PASS/FAIL
with the recorder; calling that flip "the design left the shock-free class"
would put a numerical artifact into the decisive comparison as physics.
Credibility of the decisive experiment FALLS, and the protocol amendment A-1
(cert_worst <= 1/K_RICH under the pinned recorder) exists to prevent exactly
this reading.

O-9 [the salvageable half, named so the advocate cannot claim it as his
position]. The one-directional inclusion K_disc ⊆ A_0 (a certified march is
never a folded field; the certificate is SOUND) is defensible and is already
the record's role for the governor ("EXCLUSION guard for genuinely fold-
approaching designs", :77 CONSEQUENCE). It does not deliver the road: reading
a FAILURE as physics needs the reverse inclusion A_0 ⊆ K_disc (completeness),
which is what (I-1)-(I-3) kill. Retreating to soundness is agreeing with the
incumbent.

## 4. Where the INCUMBENT is weaker than it reads (I serve the truth)

W-1. The incumbent's positive claim "the mechanism is CLASS CONSTRUCTION" is
established BY ELIMINATION of the fold reading only. T2 tested the fold
margin (val); the record's margin vector also carries the CAUSALITY margin
u_x - c (:3491-3492), and the failing cells are NEAR-AXIS (y ~ 0.05-0.14),
where the axisymmetric 1/y source term stresses the unit process. The
causality margin at those cells was not printed in T2 (locus_diagnosis.py
carries no u_x - c column; only the P4 margin_floor rejector guards it in the
march, at 0.0 for in-optimization records). The correct incumbent statement
is "NOT fold-limited; mechanism identification open, F2.ENGINE" — which is
what :77 (iii) says — not "numerical, full stop". This does not help the
advocate: a near-axis causality-margin failure would still be a failure at
healthy FOLD val, off the control surface, and still not Sternin's boundary.

W-2. The incumbent's "bridge FALSIFIED" is instance-class evidence (tier-0
bell 9/10-dof; S20 mild; S24 deep-DEF), not a theorem that NO class can be
fold-limited. The record itself keeps the governor for the fold-approaching
front taxonomy (c). The honest generalization is: at every class executed so
far, certifiability is lost BEFORE the fold margin activates (H-CLASS,
:4185-4191). A class that reaches the (G) boundary before losing
certifiability is a NAMED conditional (C7 refine/enriched-class), not an
impossibility.

W-3. The successor representation is not clean either: the C28 wave-2 rider
records that the priced ratio field and the P4 gate consume the SAME
unqualified ratio and "the wrong-branch mode evades BOTH" (:455). And (I-4)
shows the ratio itself is recorder-bound within a factor K_RICH of the bound.
So the incumbent's certification frontier is a moving target it has only
just started to pin (A-1). None of this rescues the advocate — a frontier that
moves with the recorder is the strongest possible evidence AGAINST its being
A_0 — but the incumbent should not describe K_disc as a well-defined set
without naming the triple (tree, recorder, env) that defines it.

## 5. Verdict

Falsifier: AGREED with amendments F-XA-1/2/3 (binding). On the agreed
falsifier the position is REFUTED on three recorded instances (I-1, I-2, I-3)
and on the structural amendment (I-4), with the executable instrument the
advocate names. The defects O-1 (anchor superseded), O-3 (certificate scale
is eps-relative, not geometric), O-4 (type error vs the page-verified
classics) and O-5 (repair route is circular) are not repairable without
changing the position into the incumbent's soundness half (O-9).

KILL = TRUE. New objections this round: 9 (O-1..O-9); incumbent weaknesses
W-1..W-3 are additional findings for the judge, not objections to the
alternative.

Procurement asks: none. Every load-bearing citation was checked on disk
(Rao-Beck 1994 pp.2-3 [IO]; Sternin 1961 pp.335-336 [IO]); Shmyglevskii
1962 (PMM 26(1)) stays WANTED of record but is not load-bearing here.

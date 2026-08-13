# S24 GAP VERIFICATION — FACET mesh-amr (adversarial pass)

VERIFIER, 2026-08-12. Method: every anchor re-read at source; finder probes
re-run (probe_mesh_amr.py, <1 s, pure numpy — reproduced bit-for-bit);
coverage checked against D6 duty rows, docs/rde_nozzle_PROGRESS.md S24
census (rows R20-R27), M0 S20-S24 blocks, the problem book, AND carriers
the finder did not list. Default-to-REFUTED applied. The single most
consequential verification fact: the finder NEVER READ
validation/o32_mesh_convergence.py ([X-O32], 706 lines) — the repo's
observed-order carrier — and never read the CHOICE LEDGER census row R25
(docs/rde_nozzle_PROGRESS.md:245-250), which already registers "mesh
AMR/DWR (F2)" and "universalita' K_RICH=4 (F2 audit)" as open rows with
owners. Three findings fall or shrink on exactly those two omissions.

SUMMARY: CONFIRMED 1 | DOWNGRADED 5 | REFUTED 2.

---------------------------------------------------------------------------
## F1 (uniform net, no local AMR) — DOWNGRADED (MEDIUM, efficiency/coverage)
ANCHORS VERIFIED: a1_ideal_march_jax.py:723-724 (uniform IVL rows), :800-801
(uniform arc angle), :936 (uniform exit columns), a1_toc :33-34/:337
(uniform Nw, frozen), o33_bench.py:172-177 (refine() joint global) — all
real. The 41.8% localization datum VERIFIED verbatim in
PROGRESS_2026-08-07_S20_adaptive.md ("41.8% of the optimality residual in
the first post-attachment interval").
REFUTING FACTS: (1) COVERAGE — the gap is NOT unregistered: CHOICE LEDGER
row R25 (docs/rde_nozzle_PROGRESS.md:247) carries "mesh AMR/DWR (F2)" as an
open adjudication row with owner F2, and row R21 schedules the F1/F4 joint
mesh+knot refinement leg (S24+1 pre-authorized, else F2 entry). The
finder's framing "the MARCH mesh cannot respond at all ... the named lever
nobody holds" is false as a registration claim: the lever is named and
owned. (2) "refine() = the ONLY refinement operation in the repo" is
inaccurate: [X-O32] runs its own refinement ladder (non-integer ratios
1, 1/2, 1/3, 1/4).
WHAT SURVIVES: the substantive content — no local-refinement PRIMITIVE
exists in any march; the S20 41.8% localization is measured; the
column-local C- insertion design (record-time, RK-G P2-compatible) is a
genuine, correctly-SOTA-referenced contribution the F2 owner row can
consume. SOTA citations checked real (Venditti-Darmofal JCP 2000/2002;
Fidkowski-Darmofal AIAA J 49(4) 2011; Zucrow-Hoffman Vol. 2).
SEVERITY: MEDIUM (efficiency/coverage; no shipped verdict number is wrong —
bands are honest at the meshes used).

---------------------------------------------------------------------------
## F2 (no observed-order / asymptotic-range verification) — DOWNGRADED
##    (headline REFUTED; residual MEDIUM)
HEADLINE REFUTED: validation/o32_mesh_convergence.py [X-O32] (S19, absent
from the finder's source list) IS an observed-order + asymptotic-range
carrier, pre-registered and run: three-level rate estimator (exact
bisection recovery of p, known-answer tested at p0 in {1, 1.5, 2, 3} to
~1e-12, monotonicity machine-checked); dp_model := |p_hat(coarse triple) -
p_hat(fine triple)| is EXPLICITLY the asymptotic-range indicator, and an
out-of-range sequence is declared NON-CONCLUSIVE rather than PASS; a
provably first-order negative control (foot-frozen coefficients) must be
REJECTED by the same band. This is precisely the "THREE meshes, observed
p" machinery the finder cites (Roache 1994 / Celik-ASME V&V 20-2009) as
missing. Row of record: p_fine = 2.5347, dp_tot = 0.6704 ->
NON-CONCLUSIVE, named lever "finer ladder until dp_tot < 0.5" (carrier
header, S21 re-adjudication of record; P2_outline "o32 objective row
NON-CONCLUSIVE").
ANCHORS OTHERWISE VERIFIED: K=4 asserted-not-measured at a1_ideal :88-93;
counterexample datum REAL and of record (f2 drift 9.4809e-03 (r=1) ->
1.4155e-02 (r=2), S21 log + P2_outline:23-28 + M0 ~:1898, carried
honestly); corner row "NOT confirmed at a Richardson band" verified in the
dev plan (~:885-888; finder's :866-868 off by ~20 lines, content real).
WHAT SURVIVES (the residual, genuine): the observed-order machinery exists
but is APPLIED ONLY to the O3.2 registered-norm functionals at the twin
instances; the verdict-bearing two-mesh bands (contour_compare, def_twin
F1/F2/D', o33 field bands) are never routed through it, and K_RICH is not
conditioned on an observed p (that conditioning question is itself already
registered — ledger row R25 "universalita' K_RICH=4"). The finder's
proposed S25 triplet probe partially DUPLICATES an existing carrier and
should be re-scoped to "extend [X-O32]'s estimator to the banded
quantities".
SEVERITY: MEDIUM (coverage extension; the honest-datum handling of record
means no verdict number is misrepresented).

---------------------------------------------------------------------------
## F3 (m_stop floor uncoupled, never measured; joint refine cannot
##    attribute) — DOWNGRADED (LOW); claim (i) REFUTED
CLAIM (i) REFUTED ON THE RECORD: the finder's "the declared 'candidate
ceiling' was registered but never MEASURED" is false. The S19 log (line 49
region, PROGRESS_2026-08-06_S19_o33.md) records the PRE-DECLARED
diagnostic EXECUTED: ladder re-run with m_stop tightened 100x (1e-5 ->
1e-7), RESULT "ATTRIBUTION CONFIRMED": |dMe| along the ladder collapses
from 5.242e-06 / 1.495e-05 / 4.356e-06 (non-monotone, at the constant's
own scale) to 8.465e-08 / 2.325e-08 / 1.108e-08 — i.e. the floor's bite
WAS located and attributed, of record. The machinery is a standing stage
(o32_mesh_convergence.py:595-616, stage "mstop"). The finder's registered
probe P-S25-2 duplicates it. Additionally S22 STIM-1 (of record): with
m_stop = 1e-14 the wall-angle refinement converged to me_gap = 3.553e-15 —
the exit refinement is ~9 orders more accurate than the mirrored floor,
directly against the "quietly degrade past r*" scenario at the tested
case. Cap-30 exits are already rejector-gated (C2-F4, code :873-879, the
S2 check rejects a cap exit) — the finder's own DROP D4 admits this.
CLAIM (ii) SURVIVES, NARROW: per-direction (NI vs da vs Nw/Ne) refinement
for error ATTRIBUTION genuinely does not exist; adjacent to but not
identical with the registered AMR/DWR row.
SEVERITY: LOW (hygiene/attribution sharpness; verdict numbers unaffected).

---------------------------------------------------------------------------
## F4 (DWR named-never-built) — REFUTED (as a gap; coverage)
ANCHORS VERIFIED: ledger 10bis U3 :681-685 verbatim; dev plan DWR at :455
and :740 (finder cited :432/:717 — off, content real); M0:312;
claims_verdict:217; [X-AKNO] f2-indicator "DWR-conformant" adjudication
(M0 ~:1507-1509). All real — and all REGISTRATION, which is the point:
REFUTING FACTS: (1) COVERAGE — DWR for the march is a NAMED, OWNED item of
record twice over: ledger 10bis U3 (Level-C upgrade target) and CHOICE
LEDGER row R25 "mesh AMR/DWR (F2)" (open row, owner F2). Under the
verification mandate a 'missing' claim already covered by a named
conditional with owner does not stand as a gap. (2) The sharp verdict-
facing angle ("every shipped Verdict carries Richardson where M0:312
promises DWR") is DEFUSED at source: M0:313-318 BAR-CLASS NOTE (dated
2026-08-05) declares the (v) bars "ESTIMATED/ASYMPTOTIC indicators ...
NOT certified bounds; certified brackets ship only via the D2.2 fallback",
and o33_bench :96-105 (S21 honesty rewrite) declares exactly which bands
are Richardson and which are structural discriminators. No shipped Verdict
misstates its bar class.
RESIDUAL VALUE (not a gap): the finder's observation that the dual weights
are one vjp call and the per-cell residuals already exist is correct and
useful sizing input for the F2 owner window; the proposed one-off DWR
assembly with sum(eta) vs two-mesh rejector is a good discharge design for
the EXISTING row.

---------------------------------------------------------------------------
## F5 (Sauer start line outside perturbative regime; no start-line
##    rejector) — DOWNGRADED (MEDIUM)
ANCHORS VERIFIED: a1_ideal :719-727 (formulas + the 0.000001 literal,
GENO-mirrored, underived), :662 (gammamedio IVL vs EOS-general march),
:37-40 (declared shared DATA CONTRACT), duplication in a1_march_scan
:334-342. Probe P-A RE-RUN and reproduced exactly.
DOWNGRADING FACTS: (1) PROBE HEADLINE OVERSTATES: the quoted "total
u-perturbation = 0.50 (50% of a*!)" at rtu=1.5 is the ABS-SUM of two
OPPOSITE-SIGN terms (|alpha*x_w| = 0.167, c2*yt^2 = +0.333); the NET wall
perturbation is +0.167 (u = 1.167 a*) — 3x smaller than the headline. The
qualitative point stands (individual first-order terms of 0.17-0.33 are
outside any small-perturbation license, and at the panel's r=0.1 the net
2.5 is meaningless regardless), but the record-case number must be stated
as net 0.17 / terms 0.17+0.33. (2) PARTIAL COVERAGE: (a) the IVL's
fidelity-vs-accuracy boundary IS declared in-code (:37-40 "shared DATA
CONTRACT ... not a solver step" — contra the finder's "never stated for
the IVL"); (b) the problem book (~:284-293) already registers the Sauer
start as a "gamma = const structural limit" with named alternatives
((ii) computed IVL import, (iii) prescribed inlet) AND the standing duty
"The IVL's provenance and accuracy order are part of the Verdict";
(c) KPT-2002 first-order sensitivity of the optimum to the transonic
datum is a registered problem-book row; (d) the O3.2 pre-registered norms
EXCLUDE the sonic-line/Sauer-IVL neighborhood precisely as untrusted
(o32 header + P2_outline :229-233); (e) gamma=const boundary naming is a
standing directive (gamma-variable-generality).
WHAT SURVIVES (genuine, correctly attributed): NO start-line accuracy
REJECTOR exists anywhere (no displaced-IVL invariance test, no
higher-order start to difference against), and the two-resolution band is
STRUCTURALLY blind to the shared IVL model error (both resolutions share
the model) — that instrument-level statement appears in no record doc.
Kliegel-Levine (AIAA J 7(7) 1969, toroidal coordinates, small normalized
throat radius) and Hall (QJMAM 15(4) 1962) attributions are correct and
are the right SOTA anchors.
SEVERITY: MEDIUM — twin/EQ-v2 verdicts are start-line-error-CANCELLING
(both legs share the model, rtu=1.5 on all record instances), so no record
number is affected; the gap bites absolute-accuracy claims and future
compact-throat instances (r -> 0.1).

---------------------------------------------------------------------------
## F6 (axis y->0 verification-free at march level) — CONFIRMED (MEDIUM)
ANCHORS VERIFIED: resid_axis :488-499 (vm = 0.5*v1, ym = 0.5*y1 => v/y
ratio = foot value v1/y1 — exact), :566 GENO guard, :853 (axis M is the
exit-condition read; Me_ach = Max at :889 — the exit topology gates on the
axis cell). Probe P-B RE-RUN: bias/y1^2 = 1.5 constant across y1 = 0.5 ->
0.0625 — O(h^2) coefficient bias, consistency claim honest (finder
explicitly disclaims an order defect).
COVERAGE CHECKED, NOT COVERING: (a) the declared inheritance (:69-72) of
the gconst march oracle is from the S5/S8 spikes; g0_spike_axisym_shock.py
verifies the AXISYMMETRIC SOURCE dual-route at INTERIOR/inverse-wall cells
(brick A) but contains NO axis (y=0) point process — the inherited oracle
never exercises the v/y limit cell; (b) the "near-axis mechanism" residual
(owner F2, S23 close + S24 census R20) is the OPTIMIZATION-stall
mechanism, a different object from discretization verification of the
axis unit process; (c) no MMS/axis-local oracle exists in any carrier;
nothing in D6 duty rows or R20-R27 names one. Newton certification is
ALGEBRAIC-layer only, as the finder says.
Roache MMS (J. Fluids Eng. 2002) and Zucrow-Hoffman axis-point lineage
attributions correct. The proposed S25 gconst axis oracle (2 reduced
marches) is well-posed and non-duplicative.
SEVERITY: MEDIUM — verification-coverage gap at a verdict-load-bearing
read point (every deep-DEF Me is read there), with no evidence of an
actual defect (probe shows consistency; S22 me_gap 3.55e-15 datum shows
the exit machinery itself is accurate).

---------------------------------------------------------------------------
## F7 (D' band grid-cell-floored; local seam refinement unheld) —
##    DOWNGRADED (LOW)
ANCHORS VERIFIED: def_twin_falsifier.py:350, :380-384, :404 (band_dprime =
K_RICH * max(cell, ds_land) — cell-floored when cell > ds_land: exact),
:1120-1127 (F1 band inherits band_dprime), :1146-1147 (F2 band), :321-325
(NI=201 GENO N-74 quirk).
DOWNGRADING FACTS: (1) the "3-line attribution print" the finder proposes
ALREADY EXISTS: :405-408 prints ds_land AND grid cell AND the safeguarded
band side by side — only the max() winner label is implicit; "the current
machinery cannot distinguish" is false. (2) "the GENO leg cannot even
refine freely" overstates: the quirk blocks the HALVED (coarsening)
direction; the refinement direction 801/4001 RAN of record (leg-1 r2).
(3) COVERAGE: local/adaptive refinement is the CHOICE LEDGER R25 row
"mesh AMR/DWR (F2)"; the joint mesh+knot F1/F4 leg is the R21 named
conditional (S24+1 pre-authorized). (4) "could flip a PASS into a
discriminating verdict" is speculative: the D' two-resolution agreement of
record sits INSIDE its band; nothing indicates a near-miss.
WHAT SURVIVES: the structural fact (verdict-sharpness bands floored by the
local cell, shrinkable at ~linear cost by seam-local C- insertion vs
~quadratic global) is true and is useful sizing detail for the R25 owner.
Corner-row logic verified (dev plan corner non-confirmation is real).
SEVERITY: LOW (efficiency/sharpness; registered owner; existing verdicts
honest).

---------------------------------------------------------------------------
## F8 (K_RICH = 4 asserted, reused across heterogeneous roles) — REFUTED
##    (as a gap; coverage)
ANCHORS VERIFIED, ALL REAL: a1_ideal :92-93 (asserted coverage), a1_toc
:196 + :1398-1405 (delta_inst = min_margin/K_RICH — margin-floor role),
def_twin :757 (rho = K_RICH*log(N)/ladder[-1] — KS sharpness role),
:647-649/:668 (padding role). The three-meanings observation is accurate.
REFUTING FACT: COVERAGE — CHOICE LEDGER row R25 (docs/rde_nozzle_PROGRESS
.md:247-250) already carries "universalita' K_RICH=4 (F2 audit)" as an
open row with a named owner. "Universality" is exactly the
cross-role-reuse question the finder raises; the finding restates a
registered audit row. Under the mandate's coverage test it does not stand
as a new gap. Note also each reuse is declared in-code (the finder
concedes this) and the KS-rho instance derives rho from measured ladder
quantities (K_RICH enters as the safety multiplier — the Poon-Martins
adaptive-rho contrast is fair input TO the registered audit, not a new
obligation). GCI factor-of-safety attribution (Roache Fs=3/1.25,
ASME V&V 20) correct; the observed-p conditioning half is F2's residual
and is likewise fed to the same registered rows.
DISPOSITION: the role inventory (anchors above) should be attached as
input to the R25 audit row; no new registration warranted.

---------------------------------------------------------------------------
## DROPPED ITEMS (D1-D4): spot-checked D3 (NT limit :796-798, raises
loudly — correct) and D4 (cap-30 rejector-gated by C2-F4 — correct, and
this materially weakens F3 as noted). Drops legitimate.

## VERDICT TABLE
F1 DOWNGRADED (MEDIUM)  — real efficiency gap, but registered: R25 owner F2
F2 DOWNGRADED (MEDIUM)  — headline REFUTED by [X-O32]; residual = extend
                          observed-order machinery to the banded quantities
F3 DOWNGRADED (LOW)     — (i) REFUTED by S19 mstop diagnostic of record;
                          (ii) narrow attribution point survives
F4 REFUTED              — named+owned twice (ledger U3, R25); BAR-CLASS
                          note defuses the verdict-misstatement angle
F5 DOWNGRADED (MEDIUM)  — probe headline 3x-overstated (abs-sum vs net);
                          partial coverage; the no-rejector/band-blindness
                          instrument gap genuinely survives
F6 CONFIRMED (MEDIUM)   — axis cell verification-free at march level;
                          probes reproduced; not covered by any row
F7 DOWNGRADED (LOW)     — attribution print already exists; GENO refinement
                          ran; lever owned by R25
F8 REFUTED              — exact registered ledger row (K_RICH universality,
                          F2 audit); anchors = input to that row

COUNTS: confirmed 1, downgraded 5, refuted 2.
CROSS-CUTTING VERIFIER NOTE (for the parent): the finder's source list
omitted validation/o32_mesh_convergence.py and the PROGRESS.md CHOICE
LEDGER census — both are mandatory reads for any future mesh/error-control
facet; two of the finder's six S25 probe registrations (P-S25-1 partially,
P-S25-2 wholly) duplicate existing carriers/stages and must be re-scoped
before S25 execution.

---------------------------------------------------------------------------
## SECOND-PASS VERIFICATION OF RECORD (independent re-check, 2026-08-12,
## HEAD 589cc56 — this file was found on disk complete; every load-bearing
## claim re-verified from source before acceptance; ZERO corrections)
Re-verified at source, line-by-line: all 8 findings' code anchors
(a1_ideal_march_jax.py :88-93/:145/:488-499/:566/:719-741/:796-798/
:800-802/:853-900/:862-885/:936/:985-988/:1099-1117; a1_toc :29-39/
:188-198/:330-339/:500-511/:1395-1405; a1_march_scan :334-342;
o33_bench :96-109/:172-177; def_twin_falsifier :16-17/:44-72/:296-307/
:320-327/:350/:380-384/:400-411/:640-679/:757/:1110-1156). Doc anchors:
ledger 10bis U3 :681-685 and corner row :457-464; dev plan DWR :455/:740
and corner non-confirmation :882-892; M0 :312 + BAR-CLASS note :313-318
+ DWR-conformant :1507-1511 + F1-close numbers :1893-1903; P2_outline
:21-31 (drift-grows datum 9.4809e-03, band 1.8696e-02); S21 log :63
(1.4155e-02 r=2); claims_verdict :217; adaptive_knot_optimize header;
S20 log steps 5/6/10 (41.8%/18.9%/17.6%); problem book :284-293 (Sauer
gamma=const limit + alternatives + "provenance and accuracy order are
part of the Verdict" duty). Ownership rows re-read: PROGRESS R20
(near-axis owner F2), R21 (F1/F4 joint refinement, S24+1 else F2), R25
:245-250 ("mesh AMR/DWR (F2)"; "universalita' K_RICH=4 (F2 audit)").
[X-O32] header re-read in full (three-level estimator, ratios 1/1:2/1:3/
1:4, dp_model asymptotic indicator, NON-CONCLUSIVE rule, first-order
negative control, S19 row p_fine = 2.5347 / dp_tot = 0.6704) and stage
"mstop" :595-615; S19 log :53 mstop numbers verbatim (5.242e-06/
1.495e-05/4.356e-06 -> 8.465e-08/2.325e-08/1.108e-08); S22 log :76
STIM-1 verbatim (m_stop 1e-14 -> me_gap 3.553e-15, "~9 orders more
accurate than its GENO-mirrored 1e-5 stop"). g0_spike_axisym_shock.py
grepped: brick A = interior + inverse-wall axisym processes ONLY, no
y=0 axis point process — F6's non-coverage claim stands.
ADDITIONAL OWNERSHIP CHECK not in the first pass (mandate item):
ADVISORY_engine_speed_audit_2026-08-12.md §7.5 DECLARES the speed audit
and this gap map perimeter-DISJOINT ("this audit: speed at equal rigor;
that one: construction completeness"); grep of the advisory + DISPATCH
for mesh/Richardson/K_RICH/AMR/Sauer/axis found no competing dead row —
NO finding here is owned by a speed item M0-M6/H1-H5/N1-N8. Ownership
pointers of this file (R25, R21, ledger U3, R20/F2 near-axis) are the
complete set.
PROBES RE-REPRODUCED (this pass, pure numpy < 1 s, scratchpad
probe_mesh_amr_verify.py): P-A terms at the wall row are
gamma-independent analytically (t1 = -yt/(4 rtu), t2 = +yt/(2 rtu)):
rtu = 1.5 -> t1 = -0.1667, t2 = +0.3333, NET = +0.1667, ABS-SUM =
0.5000; rtu = 0.5 -> NET 0.5000 / ABS-SUM 1.5000; r = 0.1 -> NET
2.5000 / ABS-SUM 7.5000; rtu = 4 -> ABS-SUM 0.1875. The finder's
quoted 0.50/1.50/7.50/0.19 are exactly the ABS-SUM column — the F5
downgrade (headline = abs-sum of opposite-sign terms, net 3x smaller
at the record case) is CONFIRMED, and the finder's qualitative point
survives as stated above. P-B reproduced: bias/y1^2 = 1.5000 constant
over y1 = 0.5 -> 0.0625 (a = 1, b = 2) — O(h^2) coefficient bias,
consistency reading confirmed. No JAX import, no march, no GENO run;
running-campaign untouched.
FINAL: SUMMARY/VERDICT TABLE UNCHANGED — confirmed 1 (F6 MEDIUM),
downgraded 5 (F1 MED, F2 MED, F3 LOW, F5 MED, F7 LOW), refuted 2
(F4, F8 — both as coverage: already registered with owners).

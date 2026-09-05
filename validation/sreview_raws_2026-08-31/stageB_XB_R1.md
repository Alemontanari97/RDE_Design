# Stage-B item XB — REFUTER round 1 (of at most 2)

Persona: unsteady-aerodynamics referee skeptical of exactness claims (per stageB_items.json "XB").
Read in full: stageB_items.json (XB), stageB_XB_A0.md, M0 :25-62 / :100-125 / :265-273 / :488-496 /
:512-640 / :1340-1346 / :1440-1450 / :3010-3020 / :3024-3046 / :3140-3172, problem book :418-500
(sec.7-9, hypothesis ledger H-A1/H-A2/H-F1/D1/D2), st_scoping_number_run.log (49 lines), D6 :270-280 /
:645-660 / :1008-1044, choice ledger C61 :819-830, findings :896 / :2843, TWIN_amendments_PROPOSED.md
rows A-2/A-7. Literature checked AT THE PAGE (registry rows harroun_2020 :633, harroun_2021 :273):
Harroun 2020 p.7; Harroun 2021 pp.668-670. Date 2026-09-05. No file other than this one written.

## 1. Falsifier — AGREE WITH AMENDMENTS (the amended text below is the binding text for the judge)

The advocate's falsifier as written cannot fire, for three reasons. (a) CIRCULARITY: the record's own
mode-purity certificate is the thrust-trace flatness monitor (M0:532 "thrust-trace flatness = executable
mode-purity diagnostic (N-T0')"; VI.4bis(i) :3146; D-MU scope note :108-112). A non-constant F(t) is
therefore re-read as "not single-mode" by the pin's own gauge, and the falsifier reduces to a tautology
(pattern-by-definition => constant-by-substitution). (b) DOMAIN: "an enclosing axisymmetric control
surface" crosses the base pocket and the plume, but the record proves the pattern only on cl(Omega_march)
and SLIP-FREE (Cor 5.1, M0:604-607); a failure on an enclosing surface would be dismissed as out of class,
a pass would not be predicted by the record — neither outcome tests the position. (c) FORM: "m = 0
harmonic content of dF/dt at the wave frequency" is ill-formed for a scalar trace F(t) (no azimuthal
index); "noise floor" is undeclared, so any residual can be absorbed.

BINDING AMENDED FALSIFIER F-XB:
 Leg 1 (theorem level). Interface data on Gamma_d certified single-mode by an INTERFACE-LEVEL test that
 does NOT use the thrust trace: the azimuthal-temporal spectrum of the data lies on the helical line
 (n, Omega) with off-line energy fraction <= eps_data (declared number). S = any fixed axisymmetric
 surface contained in cl(Omega_march); walls axisymmetric; instance certified (S1/L4, slip-free) or
 measured. The position is FALSIFIED if the temporal Fourier component of F_S(t) at any multiple of
 n*Omega/(2*pi) exceeds a declared propagated bound B(eps_data) with B(0) = 0 (linear propagation of the
 off-line energy through the march). Rejector on the falsifier itself: a seeded instance whose marched
 field carries a lab-fixed (non-rotating) perturbation MUST trip Leg 1; if it does not, the test is dead.
 Leg 2 (consequence level, points 3-4 of the position). On the decisive truncated-plug instance the
 consequence is FALSIFIED if the pre-registered uncertainty budget (TWIN A-2) shows a band term that
 wave-frame evaluation does NOT touch (p_b closure, data-generator fidelity, discretization) EXCEEDING the
 O(St) term it removes — i.e. "the largest unmeasured band term is removed" fails as a matter of measured
 ordering. Surfaces crossing the base pocket/plume belong to Leg 2 only.

## 2. Attack on the position on the agreed falsifier

Leg 1 survives this round: no dataset on disk falsifies it (search: the thrust-time-resolved sources in
the read corpus are Harroun 2020/2021 URANS and Jourdaine 2019; none prints F(t) on a marched-domain
surface), and the theta-substitution is sound UNDER the field hypothesis. The attack is therefore on the
hypotheses and on the consequence (Leg 2), where the position states more than it holds.

## 3. Objections (all NEW — round 1)

O1 [rigor class inflation — REPAIRABLE]. The question is posed on DATA ("for inflow data that are a
PURE single-mode rotating wave ... EXACTLY equal") and labelled THEOREM. The record's THEOREM [T-T0]
hypothesizes the pattern ON THE FIELD (M0:513-515). The step data -> field is [T-T0P], "SCHEMA on BOTH
strata" (M0:590-592), restricted to the T-PERIODIC class until G5 is written (:596-599), to cl(Omega_march)
and to SLIP-FREE instances (:600-604); and M0:1343 states that slip-sheet fronts are "the physically
generic RDE front type", excluded by G9. So on the generic RDE front the data-level statement is not
proved at all. The position must read: THEOREM conditional on the pattern; SCHEMA on the data, with the
G-lists and the G9 exclusion named. Depth claimed > depth held = defect.

O2 [circular certificate — REPAIRED by the amendment]. See sec.1(a). Note this defect is INHERITED from
the incumbent (N-T0'), see O9.

O3 [domain mismatch on the decisive number — REPAIRABLE by re-scoping, not by argument]. The consequence
(points 3-4) is drawn for the plug sector ([X-STSC] St_plug up to 1.41, log line 43; findings :896). The
decisive number on a TRUNCATED plug includes the base pocket: a subsonic, recirculating region (Harroun
2021 p.669 [IO]: "gray volumes ... regions of reverse flow (negative axial velocity)"; "the separated flow
region for the RDE had a complex geometry, contrary to the axisymmetric separated flow region expected for
a constant-pressure engine"). That region is (i) outside cl(Omega_march), where T-T0P proves nothing;
(ii) un-marchable by B-lite, which requires u_x - c >= delta on the whole nozzle-only domain (M0:3028-3030;
D6:649-650) — the record itself assigns "subsonic pockets" to the FULL camera-included anchor
(D6:653-655). Hence "a wave-frame evaluation carries NO St correction at all" is established for
full-flowing surfaces inside the march, NOT for the thrust of the decisive object. The base contribution
keeps its own time-dependence class and its own band.

O4 ["largest unmeasured band term removed" is above the depth held — REPAIRABLE]. The O(St) term has NO
number of record: M0:1343 "No number is asserted — asserting one would exceed evidence"; the corrector is
"UNPRICED (F5b)" (TWIN A-7). The base-closure term has a number: [+19%, -15%] on p_b, cold data, classical
floor UNDER the RDE-specific unpriced bars (M0:1443-1447), and the closure choice moves the argmax x2.45
(ledger C61 :830). Harroun 2020 p.7 [IO]: "at present there is no way to create an analytical model
predicting the base pressure"; Fig.7 (same page) detonation-wave and five tests at ~0.55-0.65 atm vs the
matched-mass-flow constant-pressure computation at ~0.9-1.2 atm — a 50-100% base-pressure effect OF THE
CYCLE. An ordering "St term is the largest" cannot be asserted against an unmeasured term; Leg 2 of the
amended falsifier is exactly this check. Point 4 must be reworded to "removes ONE band term, of
unmeasured size, from the evaluation".

O5 [cost claim contradicted by the plan — REPAIRABLE only by re-pricing]. "B-lite is a build item priced
in the record": D6:275-278 places B-lite under "F6 3-D / HARDWARE BRIDGE (horizon, NOT budgeted)";
D6:1039-1042 declares the laptop-scale B-lite/O5-lite scope "industrial gap #2" pending HPC "not currently
evidenced"; the prerequisite brick G12-L1-3D is "never-executed" (findings :2843) and its only
cross-check source carries a printed-typo caveat (M0:3041-3046). The FULL anchor needed for the base pocket
(O3) is Newton-Krylov + Arnoldi + bordered adjoint (D6:656-660), HPC-class. A road whose decisive
experiment rests on an unbudgeted horizon item is priced at "unknown", not "priced".

O6 [what the wave frame does NOT steadify — REPAIRABLE by scoping]. Exactness is relative to the
INTERFACE DATA (D-CONTRACT R2, M0:117-121). The data of the decisive instance are generated by a model
chain (blowdown, wave-frame matching, thermochemistry; TWIN A-2 "P-F14 equilibrium re-evaluation"), and
under H-F1 (problem book ledger) s(.), mu, Omega are FROZEN in Sigma while the real chamber responds
(bilevel PB-4, "chamber response map DeltaPR(Sigma), Deltafill(Sigma)"; H-I2 mean upstream influence).
Both arms share the frozen data, so the COMPARISON is exact w.r.t. those data; but "no St correction at
all, whatever the value of St" is a nozzle-RESPONSE statement only — the generator's own unsteady
approximations and the Sigma-dependence of (s, Omega) survive in the band stack untouched. R20 (M0:560-561:
the pin has "no certified hardware provenance") sits upstream of every exactness claim.

O7 [exactness vs realizability — OPEN, procurement named]. T-T0 computes the thrust of THE pattern; the
physical time-mean is the thrust of the ATTRACTOR. Uniqueness that identifies them is proved only slip-free
(O1). On the generic slip-sheet front the co-rotating pattern may be a solution that the flow does not
select (shear-layer instability of the contact behind the trailing oblique shock); a space-marched B-lite
would then report a number with no time-mean behind it, and Leg 1 could fail with interface purity
PASSING. Compressible-vortex-sheet stability threshold in relative Mach: [APERTO], Miles 1958 (JFM 4:538)
not on disk — PROCUREMENT ASK: needed to state whether the RDE nozzle slip line sits in the stabilized
regime (this decides whether G9 is a technicality or the physics). Harroun 2021 p.670 [IO] shows the
separation point moving within the cycle ("by t = 50 us ... pushing the flow separation point back
downstream") — cycle-locked, but whether it is a RIGIDLY ROTATING structure is NOT stated at the page; the
Harroun 2019 thesis (registry WANTED :812) is the named source for time-resolved traces. Honest status:
this objection is not decided either way on disk; it converts "exact" into "exact for the pattern, if
realized".

O8 [the consequence answers a different question than Q0 — REPAIRABLE by wording]. Point 3 says the St
obligation "constrains the DESIGNER's rung, not the comparison's credibility". True for a comparison of
two FIXED designs; but the road's claim to Q0 ("how to optimize") is an optimality claim, and at St_plug
= 1.4 the per-phase argmax may sit far from the wave-frame optimum. Then a SMALL delta (TWIN A-9,
C57 adequacy-by-bound) is uninterpretable — bad designer or absent gain? — and only a wave-frame DESIGN
step (Lemma-B-lifted adjoint on the march, also unbuilt; M0:3035-3036) could separate the two. The
hybrid's deliverable must be printed as "exact ranking of two given designs under frozen data", never as
an optimality statement; otherwise the road's credibility on Q0 is not raised by the evaluator at all.

O9 [INCUMBENT attacked — where it is WEAKER than the alternative]. (i) M0 Part I (1) :42-44 states
"STEADIFICATION IS EXACT ... the instantaneous thrust is CONSTANT" and [T-T0](i) :517-518 "through every
axisymmetric surface" with NO trace of the Cor 5.1 scoping (cl(Omega_march), slip-free, t-periodic class)
that :596-607 impose 80 lines later; the headline over-claims relative to its own proof. (ii) The
incumbent's certificate N-T0' is the circular gauge of sec.1(a), and VI.4bis(v) :3169 makes that gauge the
switch for the robust layer — a certificate that cannot fail is not a certificate. (iii) D1 sec.8 :492
"T0 as the exact nonperturbative backstop" and VI.4bis(ii) :3151-3156 present the wave-frame anchor as an
available route, while D6 :275 files it as horizon/unbudgeted (O5): the incumbent's backstop is unfunded
and the incumbent never says so. The alternative is more honest on (iii) (it names the build item); it
inherits (i) and (ii) uncorrected.

O10 [hypothesis "Pa constant" + axisymmetric S for the plug with cowl — REPAIRABLE]. T-T0 hypothesizes Pa
constant (M0:515). On the truncated plug the surface closing the control volume across the base is not at
Pa (Harroun 2021 Fig.17 p.669 [IO]: normalized base pressure ~0.08-0.09 of chamber in the closed-wake
regime, "significantly lower than ambient"). Either the base plane is inside the pattern (then O3/O7
apply) or it is a Pa-type boundary (then the hypothesis is false by ~50-100% of p_b, Harroun 2020 Fig.7).
The position must say which, per surface.

## 4. [KNOWLEDGE] claims used in this round — tier and cover

| claim | tier | cover |
|---|---|---|
| no analytical p_b model for the RDE base; ejector mechanism; base p ~0.55-0.65 vs ~0.9-1.2 atm | [IO] | Harroun 2020 p.7 (registry :633, path on disk), read this round |
| reverse-flow base region of complex non-axisymmetric geometry; open/closed wake, P_b/P_c ~0.08-0.09 | [IO] | Harroun 2021 p.669 Fig.17/18 (registry :273) |
| separation point moves within the cycle (t = 0/25/50 us), 72 us period | [IO] | Harroun 2021 p.670 |
| Stechmann base pressure "never reached a steady-state value" | [IO] | Harroun 2021 p.668 |
| compressible vortex-sheet stabilization threshold | [APERTO] | Miles 1958 — NOT on disk; procurement ask in O7 |
| time-resolved F(t) of a single-mode RDE with nozzle | [APERTO] | none in the read corpus; Harroun 2019 thesis WANTED :812 |
| St_plug up to 1.41; O(St) term has no number | record | st log line 43; M0:1343; findings :896 |
| WG10 p_b band [+19%,-15%]; argmax x2.45 | record | M0:1445; ledger C61 :830 |
| B-lite horizon/unbudgeted; G12-L1-3D never executed | record | D6:275-278, :1039-1042; findings :2843 |

## 5. Verdict of the round

KILL = NO. Leg 1 of the agreed falsifier does not fire on anything on disk, and the substitution argument
is sound under the field-pattern hypothesis; the position SURVIVES at the theorem level ONLY as re-scoped
by O1 (THEOREM on the field / SCHEMA on the data, slip-free, cl(Omega_march)). Points 3-4 (the
consequence for the design loop) are REFUTED AS WRITTEN on four repairable counts — O3 (domain of the
decisive number), O4 (unmeasured ordering of band terms), O5 (unpriced evaluator), O8 (evaluation is not
optimization) — and the advocate must either re-scope them to full-flowing surfaces within the march with
a declared base band and a re-priced evaluator, or drop the "credibility RISES" sentence. Open, undecided
on disk: O7 (realizability), with the procurement asks named. Incumbent defects O9(i)-(iii) stand
regardless of the outcome of this item and should be logged as findings against M0 Part I / [T-T0] /
N-T0'. new_objections = 10 (all first-round).

# Stage-B item XB — REFUTER round 2 (of at most 2) — 2026-09-05

Persona: unsteady-aerodynamics referee skeptical of exactness claims (stageB_items.json "XB").
Files read this round, in order: stageB_items.json (XB), stageB_XB_A0.md, stageB_XB_R1.md. NO advocate
reply (stageB_XB_A1.md) exists on disk at the time of writing: the position under attack is A0 as
written, with the R1 objections O1-O10 UNANSWERED. Pointers re-read at the line: M0 :25-62, :512-640,
:3027-3046, :3140-3172; problem book :418-500 (sec.7-9, ledger H-A1/H-A2/H-F1/D1/D2); [X-STSC] run log
(49 lines). Literature checked AT THE PAGE this round: Harroun 2021 (registry harroun_2021 :273, path
literature_review/harroun_2021_...pdf) pp.661-663. No file other than this one written.

## 1. Falsifier — AGREE with R1's amended F-XB, with three further binding amendments

R1 sec.1 replaced the advocate's (circular, out-of-domain, ill-formed) falsifier by F-XB Leg 1 / Leg 2.
I uphold F-XB and amend it in three places; the text below is the BINDING text for the judge.

 (a) SUPPORT SET (precision). Leg 1 reads "spectrum lies on the helical line (n, Omega)". A rigidly
     rotating pattern with n UNEQUAL co-rotating waves (still in T-T0's class) has energy at every
     azimuthal index m at frequency m*Omega, not only at multiples of n. Binding wording: the
     azimuthal-temporal spectrum of the Gamma_d data is supported on the line L = {(m, omega): omega =
     m*Omega, m in Z}; off-line energy fraction <= eps_data.
 (b) PROPAGATION BOUND (no assumed linearity). Leg 1's "linear propagation of the off-line energy
     through the march" is a HYPOTHESIS, not a fact: in a nonlinear march an off-line perturbation can
     grow (shear-layer / contact instability in the wave frame). Binding: B(eps_data) is MEASURED by a
     seeded scaling series (eps in {e, 2e, 4e}, lab-fixed perturbation), not assumed; B(0) = 0 stays; a
     measured superlinear growth is itself a Leg-1-adjacent finding (pattern not the attractor, R1 O7).
 (c) LAB-FIXED LINE (executable rejector, ties to O11 below). The seeded rejector of Leg 1 is made
     concrete: the seed is a stationary azimuthal modulation of the data at index m = N_inj (injector
     count), omega = 0 — the physically generic off-line content. The predicted signature is a
     component of F_S(t) at frequency N_inj*Omega/(2*pi) with amplitude proportional to
     |q~_{N_inj}| * |q_s| (cross-term of the wave's N_inj-th harmonic with the stationary line). If the
     test does not register it at declared amplitude, Leg 1 is dead.

Leg 2 (band-ordering on the decisive truncated-plug instance, TWIN A-2 budget) is unchanged.

## 2. State of the attack on the agreed falsifier

Leg 1 does not fire on anything on disk (unchanged from R1; the read corpus prints NO time-resolved F(t)
on a marched-domain surface — Harroun 2021 p.663 [IO] measures wall/base pressures ONLY through
capillary-tube average pressure (CTAP) ports 23-30 cm long "to eliminate temporal variation": the
experimental literature of record is BLIND to F(t) by instrument design). The theta-substitution is
sound under the field hypothesis; I re-checked the proof of [T-T0](i): the integrand on an axisymmetric
S is G(s, theta - W t) with n independent of theta, and the theta-integral is shift-invariant — the
proof uses NEITHER n-fold symmetry NOR "Pa constant" (a lab-fixed Pa(theta) integrates to a
t-independent term). Two consequences, stated because I serve the truth, not the incumbent: (i) the
theorem-level position is slightly STRONGER than either A0 or [T-T0] print it (hypothesis "Pa constant"
is superfluous for (i)); (ii) wave-frame evaluation removes BOTH per-phase residuals of the problem book
sec.8 — the sweep term (St_n) AND the lab-frame azimuthal-drift term (u_theta tau_n / r) — not only the
St term A0 names. Neither changes the verdict on the consequence (points 3-4).

## 3. NEW objections (round 2). All R1 objections O1-O10 STAND unanswered.

O11 [hypothesis H-A2 fails at the data source — lab-fixed non-axisymmetry floor; REPAIRABLE by scoping
"exact" to the eps_data -> 0 limit]. The position says "whatever the data ... EXACTLY". Every real RDE
feeds the interface from a lab-fixed, NON-axisymmetric injector: Harroun 2021 p.662 [IO]: "an annular
gaseous oxygen (gox) injector with transverse fuel jet injection at or near the location where the gox
stream entered the combustor" (discrete transverse jets; Figs. 3-4 same page show the bolted annular
hardware). A rotating pattern q~(theta - W t) passing over a stationary azimuthal modulation q_s(theta)
of index N_inj produces interface data whose spectrum has a point OFF the line L at (m = N_inj, omega =
0). The thrust cross-term integrates to a component at frequency N_inj*Omega with amplitude ~
|q~_{N_inj}|*|q_s|; for a front-type discontinuity the wave's harmonics decay like 1/m, so the floor is
small (order 1/N_inj of the modulation) but NONZERO and STRUCTURAL: no hardware datum is in the
"pure single-mode" class exactly. The record's H-A2 (problem book ledger :462) covers "axisymmetric
wall and control surfaces" of the NOZZLE; it is silent on the injector, and the D-MU pin declares
purity by monitor, not by construction. Repair: state "exact in the limit eps_data -> 0, with the
lab-fixed line m = N_inj as the generic off-line content and the falsifier's rejector (1c) as its
meter". Note the incumbent's headline "the single-mode RDE has steady thrust" ([T-T0](i) :517) is
literally false of the DEVICE for the same reason; it is true of the PATTERN.

O12 [exact periodicity vs cycle-to-cycle jitter — REPAIRABLE by naming the jitter band]. A0 point 1:
"no error bar from unsteadiness". The only chamber-pressure time trace printed in the read corpus at
the page — Harroun 2021 p.661 Fig.1 [IO] (reproduced from Kindracki et al., primary = [REP], air-
breathing RDE) — shows peak pressures varying between roughly 8 and 16 bar from cycle to cycle over
seven consecutive cycles at ~kHz rate: a factor ~2 in peak amplitude, i.e. the data are NOT exactly
periodic at the ~10% level of the trace energy, before any nozzle question arises. On such data the
off-line energy eps_data is not small, and B(eps_data) — not zero — is the honest unsteady band of any
hardware-level statement. The theorem is untouched (it is an if-then); the sentence "no error bar from
unsteadiness" is above the depth held and must read "no St error bar in the nozzle response; the
data-jitter band B(eps_data) remains and is measured, not assumed". [KNOWLEDGE tier: figure [IO] at
Harroun 2021 p.661; conditions of the Kindracki test (rocket vs air-breathing, propellant, n) [REP]
only — the primary (Kindracki et al., cited as Harroun's ref. [2]) is NOT on disk: PROCUREMENT ASK —
needed only if the judge wants the jitter fraction quoted as a number of record rather than as a
qualitative floor.]

O13 [license/applicability INVERSION — sharpens R1 O3; NEW as an attack on the INCUMBENT's license
table]. [X-STSC] log lines 44-45 print the licence rule of record: bell at record head count (St_n
0.35-0.60) -> "MARGINAL: first-order unsteady corrector MANDATORY; wave-frame backstop"; plug class worst
(St_n up to 1.415) -> "NOT DEFENSIBLE alone: wave-frame / unsteady rung REQUIRED". The wave-frame
instrument named by A0 point 3 (B-lite) is admissible ONLY on a nozzle-only domain with certified
margin u_x - c >= delta (M0 :3027-3030); the truncated plug of the decisive instance carries a subsonic
base pocket, assigned by M0 :3038-3040 itself to the FULL anchor ("subsonic pockets"). Hence: the class
where the record REQUIRES the wave-frame rung is exactly the class where B-lite is inadmissible, and
the class where B-lite is admissible (full-flowing bell) is the class where the record says a first-
order corrector suffices. A0's consequence ("the St obligation constrains the designer's rung, not the
comparison's credibility, provided the wave-frame evaluator exists") is therefore vacuous on the plug
class and redundant on the bell class — unless "wave-frame evaluator" means the FULL anchor (HPC-class,
R1 O5). INCUMBENT defect (new): neither the log's license rule nor VI.4bis(ii) :3151-3156 says that the
plug-class licence can be discharged ONLY by the full anchor or by O5; the record lets a reader believe
B-lite discharges it. Repair (both sides): print the licence table with a third column "instrument
that can discharge it", with B-lite struck from the plug row.

O14 [single-mode vs n-fold symmetric — definitional gap with a cost consequence; REPAIRABLE]. H-A1
(problem book :460) pins "single steadily rotating wave (n-fold symmetric)"; [T-T0] needs only rigid
rotation; [T-T0P] (M0 :610) concludes "q~ n-fold azimuthally symmetric" from H3. Documented RDE
behaviour includes co-rotating waves of UNEQUAL strength ("modulated waves", problem book :436, routed
to "relative periodic orbits / harmonic balance" — i.e. OUT of the cheap class). Two readings of the
pin, with different prices: (A) pin = n-fold symmetric: unequal-wave data are out-of-pin and go to the
robust layer, although T-T0 holds for them — the position's scope is narrower than its theorem; (B)
pin = rigid rotation only: T-T0 covers them, but B-lite's sector reduction to 2*pi/n is lost and the
3-D march runs on the full 2*pi (cost x n), and the spectral purity test must use support (1a), not
multiples of n. A0 and the record must say WHICH; the record currently says (A) in the ledger and
proves (B) in the theorem.

O15 [an St-dependence re-enters through the discrete evaluator — REPAIRABLE by a declared resolution
rule]. "No St correction at all, whatever the value of St" is a statement about the CONTINUOUS
functional. The B-lite march discretizes a field whose azimuthal structure winds helically with pitch
lambda_h = 2*pi*u_x/(n*Omega) = L/St_n (problem book Def. 8.1 :447 with tau_n = L/u): at St_plug =
1.41 the front wraps ~1.4 turns over the plug length. The fitted sheet (M0 :3032 "fitted sheet as
per-station unknown") removes the CAPTURE error of the front, but every smooth theta-gradient of the
field (expansion fan behind the front, contact smearing) scales with lambda_h, so the discretization
band of the evaluator grows with St at fixed (N_x, N_theta). Not a correction term — a resolution
rule — but a band term that A0's "no error bar from unsteadiness" hides; TWIN A-2's "discretization"
line must carry the St-scaling explicitly. Depth held: SCHEMA (scaling argument, no number; the
G12-L1-3D brick is never-executed, R1 O5).

## 4. Objections already on file and NOT repaired (carried, not re-counted)

O1 (rigor class inflation: THEOREM on the field / SCHEMA on the data, slip-free, cl(Omega_march), G9
excludes "the physically generic RDE front type" M0 :1343); O2 (circular certificate, repaired by
F-XB); O3 (domain of the decisive number: base pocket outside the march); O4 (unmeasured ordering of
band terms — the O(St) term has no number of record, M0 :1343); O5 (B-lite is F6 horizon/unbudgeted,
D6 :275-278); O6 (exactness relative to frozen data H-F1); O7 (exactness vs realizability — Miles 1958
PROCUREMENT ASK stands; Harroun 2019 thesis WANTED :812); O8 (evaluation is not optimization); O9
(incumbent over-claim in M0 Part I / [T-T0](i) vs Cor 5.1; N-T0' circular; unfunded backstop); O10
(Pa constant vs base plane, Harroun 2021 p.669 Fig.17). The advocate has not written a repair; under
the round budget these count as CONCEDED-BY-SILENCE for the consequence (points 3-4), NOT for the
theorem-level claim (point 1), which O1 re-scopes rather than kills.

## 5. [KNOWLEDGE] claims used in this round — tier and cover

| claim | tier | cover |
|---|---|---|
| RDE fed by annular gox injector with discrete transverse fuel jets; bolted annular hardware | [IO] | Harroun 2021 p.662 text + Figs. 3-4 (registry :273, path on disk) |
| chamber pressure trace with cycle-to-cycle peak variation ~8-16 bar | [IO] figure / [REP] test conditions | Harroun 2021 p.661 Fig.1 (from Kindracki et al.; primary not on disk — procurement ask in O12) |
| experimental nozzle/base pressures are CTAP time averages, ports 23-30 cm | [IO] | Harroun 2021 p.663 |
| base pressure "never reached a steady-state condition" (Stechmann tests) | [IO] | Harroun 2021 p.662 |
| licence rule bell/plug; St_plug up to 1.415 | record | [X-STSC] log lines 42-45 |
| B-lite margin condition; subsonic pockets -> full anchor; fitted sheet | record | M0 :3027-3040 |
| Def. 8.1 St; sweep vs drift split; "modulated waves" routed out of the cheap class | record | problem book :436-455 |
| H-A1 "n-fold symmetric"; H-A2 walls + control surfaces | record | problem book :460-462 |
| [T-T0P] "q~ n-fold azimuthally symmetric" | record | M0 :606-611 |
| compressible vortex-sheet stability (O7, carried) | [APERTO] | Miles 1958 not on disk (procurement ask stands) |

## 6. Verdict of the round

KILL = NO. The agreed falsifier F-XB (as amended in sec.1) does not fire on anything on disk; the
theorem-level statement (point 1) SURVIVES, re-scoped per R1 O1 and — this round — per O11/O12 ("exact
for the pattern, in the limit eps_data -> 0; the data-jitter band is measured, not assumed"), and is in
one respect stronger than printed (sec.2: no need for n-fold symmetry or Pa constant in (i); removes
both the sweep and the drift residual). The CONSEQUENCE for the design loop (points 3-4) remains REFUTED
AS WRITTEN: to R1's O3/O4/O5/O8 this round adds O13 (the wave-frame instrument A0 names is inadmissible
exactly on the class whose licence requires it) and O15 (an St-dependent discretization band survives
in the evaluator). All defects are REPAIRABLE by re-scoping and re-pricing, none is a refutation of the
theorem, hence no kill. Incumbent defects logged this round: O11 (device vs pattern in [T-T0](i)
wording), O13 (licence table without discharging instrument), O14 (ledger pins n-fold, theorem proves
rigid rotation). new_objections = 5 (O11-O15; O13 is flagged as a sharpening of O3 on the alternative's
side and new on the incumbent's side — the judge may discount it to 4).

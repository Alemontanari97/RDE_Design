# S31 — The base-pressure family graded on measured points, and the ideal-thrust bound (2026-09-18, continuation of S30)

Tag [F3/A1][S31] (brick-2 plug line, branch `rde-nozzle-program`). Own
log because the claims lint binds a carrier's pass-of-record date to
the last commit touching its `doc`: `[X-BPRS]` is re-stamped here at
2026-09-18. Entry handoff: `RDE/handoff/NOZZLE_HANDOFF_2026-09-17.md`
(its §4 named the two unread papers; §5 item 6 asked for them to be
read). Carriers run on s2; logs in `validation/_base_pressure/`.

## 1. What was read (READING_2026-09-17_plug_base_sources.md §3-4)

Chutkey, Vasudevan & Balakrishnan 2014 in full; Channapragada 1963 for
what the Korst chain needs (its equations are figure-borne and are not
transcribed yet). Registry rows `chutkey_2014` READ-INTEGRAL,
`channapragada_1963` READ-PARTIAL.

The thing Chutkey gives that nothing else in the corpus did: **Tables
7-8 carry, at ten annular closed-wake points, the base-lip state (M_lip,
p_lip/p_0) AND the measured p_b** — the closure family's own signature
`p_base(p_e, M_e, gam)`, so the family can be graded with no march.

## 2. Stage `data` (7/7, `run_data_2026-09-18.log`, no march)

Known-answer first: our `_conical`, `_cylindrical`, `_rome` and the new
`_chutkey` reproduce the paper's OWN four model columns (Eq. (1), Fick &
Schmucker cylinder and cone, Onofri) at every point to one printed
digit (34 values, worst 7.6e-05). What we grade is what the literature
consumes.

| member | n | mean | min | max | rms | measured band on p_b |
|---|---|---|---|---|---|---|
| chutkey (Eq. (1), exponent 0.7027, theirs) | 10 | −0.022 | −0.395 | +0.432 | 0.254 | (−0.30, +0.65) |
| cylindrical (= F&S cylinder) | 10 | +0.230 | −0.056 | +0.610 | 0.307 | (−0.38, +0.06) |
| conical (= F&S cone) | 10 | +0.333 | −0.017 | +0.833 | 0.429 | (−0.45, +0.02) |
| rome (Sapienza / Onofri) | 4 | +0.842 | +0.376 | +1.667 | 0.980 | (−0.63, −0.27) |
| **veen (incumbent)** | 10 | **−0.628** | −0.817 | −0.412 | 0.639 | (+0.70, +4.45) |
| panov_shvets (on p_a) | 10 | −0.112 | −0.745 | +1.730 | 0.688 | (−0.63, +2.92) |

Read: the incumbent is BELOW the measured p_b at every point, 2 to 5
times too deep — the quantitative form of Sule & Mueller's "deeper than
the whole measured range" (S30 §4.2). The WG10 "best" member is ABOVE at
every posed point. **The WG10 bracket [+19, −15 %] carried as BAND_PB
holds for no member on this dataset**; the bands of record are now the
measured ones, per member (`BAND_MEASURED`, the inverse of the graded
error, one-sided where the member is biased). Measured p_b/p_lip =
**0.510 ± 0.075 over M_lip 2.61-5.35**: the closed-wake base sits at
half the lip pressure, weakly in Mach; Veen's M^−1.3 fall-off (0.24 →
0.10 over the same range) is not in the data. Closed-wake p_b/p_a spans
0.28-3.04 across the rigs: a closure written on p_a (Panov-Shvets) is
structurally wrong in the closed regime (D-4). Along the ATPN length
series the member falls with plug length as the measurements do (D-5,
Sule & Mueller Fig. 4 trend). Rejector run: the chutkey exponent set to
0.35 fails KA-1 and D-2 (5/7).

The member is THEIR fit on published data, graded by us: no constant in
`base_pressure.py` was fitted by this program.

## 3. Stage `derive` re-run (10/10, 100.1 s): the record rows are unchanged

Every S30 row reproduced to the printed digit; the one new row is
chutkey's, which read at the ladder of our member behaves like the two
cold MODEL-VAL forms — argmax at station 1 (1.2 % of the length), base
term +1.4029e+07 N = 12 % of J — and is REPORTED out of the declared
class by N-4b (4 of 8 members now).

## 4. Stage `band` (3/3, 99.6 s): the ideal-thrust bound, B-3

The untruncated member IS the isentropic expansion of the whole mass to
p_a (B-2: its last stretch is sub-ambient by design), so J_full is the
ideal thrust to the march's resolution, and a truncated member closing
its base through a dissipative recirculation can never exceed it:
**J_trunc = core + base ≤ J_full is a rejector no fit can argue with.**
Measured on our member (central values, caps 12.5-87.5 %):

| member | caps where J_trunc > J_full | by |
|---|---|---|
| chutkey | 12.5 % | +4.51e+05 N |
| conical | 12.5, 25 % | +1.09e+06, +1.10e+05 N |
| cylindrical | 12.5, 25, 37.5 % | +1.27e+06, +3.08e+05, +6.33e+04 N |
| rome | 37.5 % | +1.71e+05 N |
| veen, rocketdyne | none | — |

None with its whole measured interval above the bound. The bound
grades the members in the SAME ORDER as the data, with no data:
chutkey breaks it only below the 20 % shortest plug it was fitted on,
where it already over-reads its own points (+20..+43 % on Tomita and
ATPN 20). B-3 is posed on that threshold (Chutkey Table 2), not on a
number of ours. With the chutkey member priced, the closures span
1.24e+07 / 4.82e+06 / 2.09e+06 / 8.86e+05 / 3.44e+05 N at the caps
12.5-62.5 % — wider than S30's, because the measured bands are wider
than the quoted one. The S30 verdict stands (the family cannot
arbitrate by itself); what changed is that the base term now has a
measured sign and band, and a member that is inside them.

## 5. What this does and does not decide

- Adoption into J of record is NOT taken: `A1_BASE_MODEL` stays unset;
  `chutkey` is executable per leg, choice-ledger C61 stays NEVER with
  the new alternative recorded.
- The regime question (open wake → p_b ≈ p_a, S30 §4.2) is untouched:
  Chutkey's transition PRs (42/57/60/60 on PR_des 66, asymptoting to
  ~0.9 PR_des for long plugs) put our point (PR = PR_des, ≥ 60 %
  retained) on the closed side, the RDE cycle crosses it. Queue item 2
  of the handoff, unchanged.
- The next oracle is a MARCH twin on Chutkey's ATPN (Fig. 2b contour,
  Fig. 9d wall pressure at PR 66.6, lip Mach 2.715/2.986/3.093/3.173 at
  the four truncations, then p_b/p_0 0.0165/0.0131/0.0116/0.0100):
  it grades the INPUT of the closure, the corner state our march
  produces, on a measured case. Digitisation of Fig. 2b/9d by the
  owner (agreed in session).

## 6. Conformity

Files: `validation/base_pressure.py` (member, data, stage data, B-3,
interval print), `READING_2026-09-17_plug_base_sources.md` §3-4,
registry rows (lit: chutkey_2014, channapragada_1963; claims: X-BPRS
re-stamped; flags: A1_BASE_MODEL, A1_BPRS_STAGE; choice: C61
alternative), ADVISORY_INDEX, this log. Lints and suite: quoted in the
commit message.

## 7. The march twin on Chutkey's ATPN, started and OPEN [X-CHTW] (evening)

The owner digitised Fig. 2b (`validation/chutkey2014_fig2b_contour.txt`);
Table 2's four base radii are exact (x, y) points of that contour and
grade the digitisation without us: 0.19/0.10/0.09/−0.04 mm raw, and
0.06/0.00/−0.01/−0.12 mm once the abscissae are shifted by the ONE
parameter the foot identity derives (the first digitised point is the
plug-side throat point (−2.22, 30.55) mm read 0.39 mm late in x; the
first chord then slopes −57.6° against the throat's −56.9°). The mass
through the tilted sonic line equals the choked throat's to 3e-8, and at
T_0 300 K it is 8.19 kg/s against the paper's 8.12 at PR 66: their
stagnation temperature is ambient. T-0: the tilt 56.9° = ν(M_e) on our
tables to 0.01°, i.e. Chutkey's plug is Angelino's posing = our lip fan
with the inlet Mach 1.

**What did not work, with the cause measured** (`a1_chutkey_twin.py`
derive 4/9, `_chutkey_twin/run_derive_2026-09-18.log`):
1. The sonic line as the start column: a double characteristic (μ = 90°),
   Cauchy on it is ill-posed, the march certifies 1e18.
2. The cut at X0 through the axisymmetric fan ([X-AFAN] `fan_axi`): the
   fan of a SONIC lip spans ray angles −146.9…−17.1°, its C- family
   passes through the vertical (M 1.47 on this gas), and every cell of
   the record is in slope form dy = λ dx — the Newton converges to its
   round-off floor (|dz| 1e-9, cond 8.5e9) yet reads uncertified,
   6e2…2e3 in BOTH worlds for M_i ≤ 1.3, 0.02-0.05 for M_i ≥ 1.6; the
   gas is excluded (cold world at M_i 2: 0.024); the geometric scale is
   excluded (identical wall at R = 32 mm and R = 1). With the fan at
   M_i 1.6 (certified 0.049) the plug march from the cut still does not
   certify (7e10, mass −10.7 %): its near-cut cells carry C- within 10°
   of vertical. **The wall rows (p_w/p_0 +8…+13 % above the paper, M −2 %)
   are an indication, not a result (G1).**
3. GENO, read for the same question (`InitialValues_m.f90`
   `IVLINE_annular_solve`, `GenoPlug/src/geno.f90`, `Interior_m.f90`):
   GenoPlug is an internal-external plug (sonic throat upstream on an
   arc R_c, lip at M_i > 1, inverse construction); the direct annular
   start line is Migdal 1972's uniform tilted line at Mi_ann (default
   sonic) — the posing tried in 1 — marched with the same slope-form
   cells (`lm = tan(A − asin(1/M))`). The limit is shared; no Sauer
   exists for the annular throat there (Sauer is the bell's IVL only).

**Indicative, declared, not adjudicated:** Angelino's contour lies
0.75-0.96 mm (3 % of R_lip) ABOVE the M_i-1.6 axisymmetric member over
20-50 % of the length, tip 3.1 mm longer — their "mild compression wave
at the junction" would be this; but that member passes 5 % less mass
than the choked throat (its throat strip is unmarched), so the offset
is not a finding.

**Refined the same night (owner's challenge "is it really the slope
form?"):** the gas tables are excluded (N_TAB 8192 → 65536: 7.5e2 →
6.6e2), the SAME construction certifies in PLANAR flow (δ = 0: 0.07),
and row-equilibrating the Jacobian leaves the step untouched (1.656e-9).
So the floor is the coupling of the near-vertical characteristic with the
AXISYMMETRIC SOURCE: the compatibility row carries S·(x₄ − x₁) with
S = c²v/y ~ 3e7 while x₄ is determined only as x₁ + (y₄ − y₁)/λ, λ ~ 2.7e3
— a 5e-14 jitter in x₄ is 1.5e-6 of residual, the measured floor. GENO
(`Interior_m.f90`) guards only the exactly-vertical `tan = huge` case and
stops at `tol_conv` 1e-8, so it would call this cell converged: it does
not certify at round-off. **The fix is a reformulation, not a brick**:
write the source term as S·(y₄ − y₁)/λ (identical on the characteristic
because the position row enforces (y₄ − y₁) = λ(x₄ − x₁); same roots),
gated on bit-level agreement over the record's worlds and on cert < 1
on Chutkey's fan. Owner's call (it touches the shared certified cell).

**Then, on the owner's "make it work" (late night), the remedies were
TESTED, and none cures — the ledger, all on the worst cell of the M_i
1.05/1.3 fans (cert as slope-form → variant):**
- source term as the projected chord S[(x₄−x₁)+λ(y₄−y₁)]/(1+λ²): 360 → 127;
- the whole cell in direction cosines (rows × cos α, no tan): 360 → 187;
- Jacobian row equilibration: 360 → 360; gas tables ×8: unchanged;
- level refinement (uniform): 121 → 241 levels 646 → 286 (∝ Δs^1.2);
  61 levels 9e9; clustering at the lip (`fan_axi lev_power`, additive
  knob kept): p = 2 1.5e3, p = 3 2.5e3 — the stalled cell moves to
  where the step is widest;
- the same construction PLANAR (δ = 0): 0.07 — certifies.
Two independent formulations converge to the **same root to 5e-12**
(healthy cells 1e-16) and the ideal wall is stable to 1e-3 mm across
every discretisation (y(10 mm) 19.8416-19.8456 mm): the construction is
converged, the certification metric — Newton step ≤ 100 eps |z| — is
not met because the cell's Jacobian is ill-conditioned (κ ~ 1e6 after
equilibration) in the axisymmetric case at low M near the lip, for a
reason not yet isolated (the source term and the tan pole are excluded
as the whole cause). GENO would call these cells converged (tol_conv
1e-8). **DECISION FOR THE OWNER (G1 is the program's rule):** (a) a
conditioning-aware certification bound, derived from the Newton
contraction at the round-off floor — |step| ≤ factor·eps·κ(J)·|z| with κ
reported per cell and the worst κ a row of record — which admits these
cells at their measured 5e-12 determination and keeps truly stalled
cells visible; or (b) G1 strict as it stands, and the sonic-lip line
(Johnson, Humphreys: profiles built from the sonic line) waits for the
mechanism to be isolated. Under (a) the twin proceeds tomorrow: fan at
M_i ~ 1.05, cut at X0, plug march (its cert 7e10 is to be re-read under
the same bound), T-4…T-7.

**The alternative, heavier:** a direction-invariant cell for the
throat kernel — frame rotated by ~−80° (marching radially inward near
the throat) with the axisymmetric source on the true radius; the
sonic-lip fan's characteristic directions span 146° < 180°, so one
frame avoids the vertical for both families — gated on the planar PM
fan as [X-AFAN] G-0. Then T-4…T-7 become readable, the X0 ladder
measures the throat strip, and Fig. 9d (to be digitised) reads the
first 15 mm. Registry: `[X-CHTW]` OPEN, 4/9 of record; ondemand carrier,
no suite gate.

## 8. THE TWIN CLOSES (night): the march on Chutkey's contour certifies and reads the paper's wall state

The cause of the plug march's non-certification was not the cells: it
was the **contour posed as an interpolating spline through the 63
digitised points** — their capture noise (~0.1 mm) entered the wall
angle and the march answered with spurious waves (p_w/p_0 oscillating
±20 % along the plug, rising at the tip; that A/B: cert 7e10). Posed as
a **smoothing spline with residual = the digitisation noise** (rms
0.120 mm = the Table 2 residual after registration, not a number of
ours; foot kept exact, throat tangency clamped), with the cut at X0 =
1.5 mm through the M_i-1.6 axisymmetric fan (cert 0.049):

| | march | paper | rel |
|---|---|---|---|
| p_w/p_0 at 20 / 34 / 41 / 48 % | 0.04255 / 0.02812 / 0.02411 / 0.02120 | 0.04201 / 0.02780 / 0.02368 / 0.02105 | +1.3 / +1.1 / +1.8 / +0.7 % |
| M_wall at the same | 2.706 / 2.978 / 3.081 / 3.168 | 2.715 / 2.986 / 3.093 / 3.173 | −0.3 / −0.3 / −0.4 / −0.2 % |

**cert worst 0.451 over 14 999 cells; derive 8/9** (`run_derive_2026-09-18.log`):
T-0…T-7 PASS, T-4b FAIL (mass along the march −5.6 %, unchanged by
`edge_fill` 0/6 — 6 degrades the certification to 3.41 — a ladder
question, stage ladder). T-7 re-posed: the 0.39 mm foot registration is
not a perturbation the reading is blind to; it is the ORACLE that picks
it (worst error 0.018 shifted vs 0.130 raw). Reading at the oracle's
class: p_lip/p_0 is a ratio of two four-digit numbers (1 % at worst),
M_lip their RANS with a boundary layer; our 1.8 % / 0.4 % is inside it.
Near the tip (x > 85 mm) the march shows a recompression (p_w/p_0 0.015
→ 0.06, M 3.4 → 2.4): their contour is 3 mm longer than the exact member
and turns less than it there; no measurement beyond 48 % to read it
against. Figures (provisional): `_chutkey_twin/figs/01-04`.

**What this means for the program:** on a measured plug with a SONIC
lip, our certified march reproduces the corner state the base-pressure
closure consumes to the oracle's precision — the input side of N2 is
validated on one rig. The fan's own low-M_i floor (§7) is a separate
open row of fan_axi that this twin does not need. **The whole chain,
march → corner state → closure, against the measured base** (p_b/p_0,
derive of record):

| retained | measured | chutkey | cylindrical | veen |
|---|---|---|---|---|
| 20 % | 0.0165 | 0.0240 (+45 %) | 0.0269 (+63 %) | 0.0099 (−40 %) |
| 34 % | 0.0131 | 0.0147 (+12 %) | 0.0176 (+35 %) | 0.0058 (−56 %) |
| 41 % | 0.0116 | 0.0123 (+6 %) | 0.0151 (+30 %) | 0.0047 (−59 %) |
| 48 % | 0.0100 | 0.0106 (+6 %) | 0.0132 (+32 %) | 0.0040 (−60 %) |

Same picture as on the paper's own lip state (stage data): the march
adds < 2 % to it; what remains is the closure's own error, largest on
the shortest plug (+45 % at 20 %, where the member over-reads its own
fitting data too) and 6 % from 41 % on.

**Ladder** (`run_ladder_2026-09-18.log`): every rung certified (worst
0.671 at X0 1.0 mm, the cut 1.8° from the fan's leading ray); between
cuts clear of the leading ray (2.0 → 1.5 mm) the reading moves 1.1-1.3 %;
on the last resolution pair (161,81) → (321,161) 0.6-0.7 % (K_RICH band
2.8 %), against the oracle's 3 % class. L-2/L-3 as first posed graded the
coarsest rung and the leading-ray cut (5 % / 4 %) and were re-posed on
the readable rungs.

## 9. T-4b attributed: the mass defect is the cut data on a non-ideal wall (stage `mass`, 2/2)

Column-by-column mass along the march (`plug_march` returns its mesh):

| posing | cert | column 2 | mid | last |
|---|---|---|---|---|
| Chutkey's contour, cut of record (1.5 mm) | 0.070 | **−6.2 %** | −5.9 % | −5.5 % |
| the fan's OWN wall, same cut | 0.065 | −0.02 % | +0.6 % | +0.7 % |
| the fan's own wall, far cut (0.2 R) | 0.069 | −0.1 % | −0.03 % | 0.00 % |
| Chutkey's contour, far cut (0.2 R) | 5.18 (uncertified) | −3.2 % | −3.2 % | −2.3 % |

On the ideal wall the march conserves mass from either cut; on
Chutkey's it loses it ONCE, in the first marched column (16 of 41 rows
consumed at the wall side, the edge point dropping from 1.0 to 0.94 R),
and is flat after — the signature the `plug_march` docstring records
for the GENO twin. Not the marcher's loss: the cut carries the IDEAL
fan's field, and below the C+ from the foot the real field over
Chutkey's contour is not that; the difference is mass the data send
into the wall. The wall pressure downstream is untouched (T-5/T-6: set
by the local geometry and the incoming waves), the mass is. The remedy
is a start computed ON the contour — the forward throat kernel from the
sonic line, the owner's proposal of the evening — until which −6 % is
the measure of that gap. `edge_fill` (the GENO twin's fix) does not
apply: 0 and 6 give the same loss, 6 degrades the certification.

## 10. Humphreys 1971, the optimisation twin [X-HMPH]: posed, (A) read, (B) launched

Posing read from the paper (p. 1586): p_c 500 psia, T_c 6000 R, R 56
ft·lbf/(lbm·R), γ 1.23, ṁ 148.08 lbm/s, p_a 14.7 psia (PR 34.0), L(T→D)
12.0 in, base Eq. (12) = Veen, shear C_f 0.002 (~0.2 %), Moore-Hall
start; results: Rao at lip 8.33 in / −58.5° → 34,253 lbf (Table 3, y_D
1.375 in); their fixed-inlet optimum at 7.55 in / −34° → 32,881 lbf
(Table 2, y_D 0.954 in); the whole 20-run grid within 0.5 %.

**(A) stage `rao`** (`_humphreys_twin/run_rao_2026-09-18.log`, 2/4 as
posed): our ideal member at lip 8.33 in and PR 34 (fan_axi cert 0.037)
exhausts at M_e 2.8495, q_e 2277.5 m/s; ṁ·q_e = **34,390 lbf** is the
ideal bound, against which Rao loses 0.4 % and their optimum 4.4 %. The
truncated member with Veen base gives 34,255 lbf (Rao 34,253) — but
with the paper's ṁ: the ideal member at that lip passes only 137.8
lbm/s (−7 %; at 7.55 in −24 %), independent of M_i (fixed by the exit:
ρ_e q_e π R_lip²). **With their mass and those lips the ideal member
does not exist**: both Rao's length-constrained member and their
optimum have non-uniform exits (p > p_a at D) and pass more mass than a
full expansion allows at that lip. (A)'s valid reading is the ideal
bound; R-1/R-3 as posed are not rows and are to be re-posed.

**(B) stage `opt`**: the record's TR-SQP (`a1_plug_spline_opt`) at their
posing, planar fan of record with the mass IMPOSED through the start
radius at X0 = 0.05 R, sonic lip (M_i 1.0002), θ_E = 0 (rao) / +22.9°
(opt: θ_i −34° + ν(M_e) — the jet boundary flares outward), base Veen,
6 knots, (81,41), 30 segments × 8 iterations, launched on s2 at ~01:40
(`_humphreys_twin/run_opt_{rao,opt}_2026-09-18.log`, results in
`opt_{rao,opt}.json`). At launch: from the fan's streamline the Rao
case reads 33,473 lbf (−2.3 % of 34,253) with y_D still 3.2 in; segment
8: +0.8 %. To be read at the S32 opening: O-1 certified, O-2 thrust
within 1 % (their shear 0.2 %), and the contour against Tables 3/2.

### 10.1 The legs closed (2032 s / 2052 s, 30 segments each, both certified)

| case | our walk | paper | thrust | y_D ours | y_D paper |
|---|---|---|---|---|---|
| rao (8.33 in, θ_E 0) | 33,780 lbf, cert 0.510 | 34,253 | **−1.4 %** (O-2 FAIL at 1 %) | 2.11 in | 1.375 in |
| opt (7.55 in, −34°) | 32,666 lbf, cert 0.522 | 32,881 | **−0.65 %** (O-2 PASS) | 3.47 in | 0.954 in |

Figure `_humphreys_twin/figs/01_contours_vs_paper.png`. THE READING:
the thrust rows pass or nearly pass because **J is a flat valley** —
the paper's own 20-run grid lies within 0.5 %, and its base-model swap
moves y_D ×2.45 at +0.26 % (S30's reading of the same exhibit) — while
the contours are NOT reproduced: in the Rao case our walk follows Table
3 to ~0.2 in up to x ≈ 8 in, then lifts its tip to y_D 2.11 in where
Rao's bends down to 1.375 (the free-tip behaviour of S30, now with the
base priced); in the opt case the walk ends fat, y_D 3.47 against 0.954,
with the same thrust to 0.65 %. Two causes, both of posing, not of the
walker alone: (i) the walks are unconverged (radius 1e-2 R with
alternating rejections from segment 23 — the S30 stall); (ii) the inlet:
our planar fan with the mass IMPOSED through the start radius (y_w0
6.24 / 6.04 in at X0 = 0.38 in) is not their sonic throat at the lip
(foot 7.61 / 6.72 in at x −0.6 in): the near-lip wall is a different
object, and in the opt case (θ_E +22.9°, the jet flaring) the whole
contour inherits it. The remedy is the same brick the day named three
times: the throat kernel on the contour, from the sonic line.

**A finding on the side, of record:** Rao's Table 3 contour lies ON our
exact ideal member (dotted in the figure) over its whole length up to
the last inch — Rao's length-constrained member at 8.33 in IS the ideal
member truncated, to the digitisation of a printed table — while that
member passes 137.8 lbm/s against their 148.08. Their mass is not the
ideal member's mass at that lip: a 7 % discrepancy in THEIR posing
(throat/discharge/gas convention), to be read before the twin is judged
on thrust at the 1 % level. X-HMPH stays OPEN: 2/2 O-rows read, the
contour rows unmet, the inlet posing declared as the cause.

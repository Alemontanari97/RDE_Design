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

**The brick that closes the twin:** a direction-invariant cell for the
throat kernel — frame rotated by ~−80° (marching radially inward near
the throat) with the axisymmetric source on the true radius; the
sonic-lip fan's characteristic directions span 146° < 180°, so one
frame avoids the vertical for both families — gated on the planar PM
fan as [X-AFAN] G-0. Then T-4…T-7 become readable, the X0 ladder
measures the throat strip, and Fig. 9d (to be digitised) reads the
first 15 mm. Registry: `[X-CHTW]` OPEN, 4/9 of record; ondemand carrier,
no suite gate.

# S30 — The overnight tournament leg read, the restoration gap it exposes, and the record derives re-run on the bucket census (2026-09-17, continuation of S29)

Tag [F3/A1][S30] (brick-2 plug line, branch `brick2-plug`). Own log
because the claims lint binds a carrier's pass-of-record date to the
last commit touching its `doc`: `PROGRESS_2026-09-16_S29_readjudication.md`
is FROZEN as committed in 97960be/a1625d6 (rows X-OWAB, X-AFAN stamped
2026-09-16); the [X-PTRN] row is coined here. Entry handoff:
`RDE/handoff/BRICK2_PLUG_HANDOFF_2026-09-16_notte.md` (its section 2-ter
is the leg read below).

## 1. The overnight leg at the (81,41) rung (launched 01:16, read 12:30)

Three walks in parallel on s2, carrier 8b01014 (the fold census on the
margin's bucket cells), `PSPL_FAN=axi PTRN_K=81 PTRN_N=41
A1_PTRN_STAGE=campaign PTRN_SEGS=20 PTRN_ITERS=8 PTRN_STARTS=3
PTRN_ONLY={A,B,C}`, artifacts `validation/_plug_tournament/k81n41/`.
Posing of the rung (from `run_derive_axi_k81n41_2026-09-17.log`): floor
mu0_1 0.0435, rho 6127.1, gap 1.361e-03, tr0 1.526e-03 m (radius floor
3.816e-04), band_J 2.297e+06 N (1.99e-02 of J, the K 81 -> 161 ladder),
band_W 1.220e-02 m, tip floor y >= 0.0227.

### 1.1 Start A (the incumbent = the method's own axi member): 4/4 PASS, 25782 s

- J* 1.15342773e+08 N: **+5.5684e+04 N over the incumbent (+4.83e-04 of
  J)** and **+5.7362e+04 N over Rao (+4.98e-04)** — both INSIDE band_J
  2.297e+06 (the gain is 2.4 percent of the band): **no resolved gain in
  class on the ideal member**, which is the M0 expectation stated in the
  night handoff section 4.3.
- The return is IN the class with the margin INACTIVE: KS - mu0 +0.04282
  (min cell +0.0864 against mu0_1 0.0435), 0 folded columns out of 81,
  mu -0.000e+00, active-cusp census empty. Certified, cert 0.086 (base
  0.434 at the start).
- Distance to Rao's shape 1.050e-02 m (as written 9.466e-03), INSIDE
  band_W 1.220e-02 — the incumbent was at 9.478e-03, so the walk moves a
  fraction of the band AWAY from Rao while gaining inside the band: the
  two statements ("the optimum is the member" and "the optimum is Rao")
  are both unresolved at this rung, as they must be.
- The motion is in the first knot and the tip: W - W0 = +6.86 mm at knot
  1, +5.25 mm at the tip (tip y 0.02794 against the floor 0.0227), every
  interior knot under 0.36 mm. theta at station 1 -32.30 deg (flow
  -33.16).
- 11 accepted segments out of 20: 9 trials rejected INFEASIBLE, radius
  down to the floor 3.816e-04. Counters at the end: m_exec 88, m_dedup
  88, gm_nonfinite 31, grad_nonfinite 30, infeasible_base 9.

### 1.2 Starts B and C: DEAD at segment 0 — the walks never started

- B (1.5 percent alternating perturbation), 2758 s: the base is already
  OUT of class, KS - mu0 -0.7735 (min cell -0.7300, 75/81 folded).
- C (ramp from the member to the planar streamline, 0.84 m away),
  2602 s: the base has **0 folded columns and min cell +0.0003**, i.e.
  it is geometrically untangled and fails only by the FLOOR (KS - mu0
  -0.0433, and the lowest derived floor is 0.0054 — the start sits below
  even that).
- In both, every trial was rejected with "INFEASIBLE than base" against
  a base that is itself infeasible, the radius halved four times to the
  floor and the driver declared "converged, stop" after 4 segments.
  C-3 (in class) and C-4 (no loss to the incumbent) FAIL in both.
- READING: these two rows measure the DRIVER, not the design space. The
  owner's question of 2026-09-16 evening — "does the direct machinery
  reach the member on its own from the planar streamline?" — is still
  UNANSWERED: walk C never took a step.

## 2. The restoration gap (measured, `a1_plug_spline_opt.run_trsqp`)

The acceptance test of the segmented driver (lines 340-380) rejects a
trial when `margin_ks - mu0 < -tol` and reverts to `W_best`. The gate is
armed only once a certified base exists (`W_cert is not None`), so
segment 0 is always adopted: from an INFEASIBLE start, `W_best` is
infeasible for the rest of the walk, and since trust-constr's barrier
iterates reach feasibility only at convergence (8 iterations per
segment here), every trial comes back infeasible too and is rejected —
**including trials that reduce the violation**. There is no phase-1 /
restoration branch and no filter: the walk can only shrink to the floor.
Cost measured overnight: 5360 s of s2 spent on two walks that took zero
steps.

## 3. The record derives re-run on the bucket census (in flight)

Launched 12:27 on s2 from HEAD fa5263b (census fix 8b01014 in place),
artifacts kept apart from the night's: `_plug_tournament/k81n41_v2/` and
`_plug_tournament/k161n81_v2/`. Both night derives (v5 at (161,81),
00:00, and the (81,41) rung, 00:25) predate the fix and failed O-1b on
the OLD census (Rao as written: margin healthy, 6/82 and 12/162 columns
counted from consumed start-line rows under the wall). ### 3.1 The (81,41) rung: 10/10 PASS (692.7 s, closed 12:39)

Every derived constant reproduces the night's run to the printed digit
-- m_ref 0.0871 (4181 bucket cells), floors 0.0435/0.0218/0.0109/0.0054,
rho 6127.1, gap 1.361e-03, band_W(rep) 1.220e-02 -> band_J 2.297e+06
(1.99e-02 of J), h* 6.106e-03 m -> tr0 1.526e-03 (floor 3.816e-04),
C-0 cert 0.434, O-2 PASS (9.478e-03 <= 1.220e-02; |dJ| 1.679e+03 N) --
so the ONLY thing the census fix moves is the census:
- **O-1b now PASSES**: Rao's contour as written on our posing, cert
  0.108, min cell +0.0626 >= mu0_1 0.0435, **0/81 folded** (was "6/82
  folded" on the old walk, which read rows 1-9 of column 2 kept under
  the wall);
- O-1 (the transplant, reported) 0/81 likewise; R-G1 unchanged as a
  verdict (the cornered incumbent is INFEASIBLE at every floor, KS
  -0.0952) with 9 folded columns counted instead of 15.
The (81,41) rung therefore goes from 9/10 to **10/10**, and the single
FAIL the night left open was an artifact of the census, exactly as
8b01014's message predicted.

### 3.2 The (161,81) rung: 10/10 PASS (2471.3 s, closed 13:12)

The record rung, `k161n81_v2/run_derive_axi_k161n81_2026-09-17.log`.
Constants reproduce the night's v5 run: m_ref 0.0480 (13273 bucket
cells, median 0.4798), floors 0.0240/0.0120/0.0060/0.0030, rho 12647.2,
gap 7.506e-04; J(inc) 1.15825015e+08 at K 161 vs 1.16107271e+08 at
K 321, |dJ| 2.823e+05, |grad J|_1 7.516e+06, band_W(rep) 1.187e-02 ->
**band_J 1.218e+06 (1.05e-02 of J)**; h* 6.106e-03 m -> tr0 1.526e-03
(floor 3.816e-04), the same fold scale the (81,41) rung derives.
Oracle rows:
- **O-1b PASS**: Rao as written, cert 0.409, min cell +0.0747 >=
  mu0_1 0.0240, **0/161 folded** (the night's v5 counted 12/162 and
  failed on them alone, margin +0.0747 unchanged);
- **O-2 PASS**: the incumbent equals Rao's contour within the
  representation band (9.420e-03 <= 1.187e-02) and in thrust
  (|dJ| 1.199e+03 N = 1.04e-05 of J);
- R-G1 PASS (cornered incumbent infeasible at every floor, KS
  -0.0458, 9 folded), R-FSC PASS, C-0 0.393, D1a/R-D0/R-D0b/R-KS PASS.
Both rungs are therefore 10/10 and the census FAIL the night left open
is closed at both. These two logs are the pass of record for the
[X-PTRN] row.

### 3.3 What the two rungs say together

band_J falls from 1.99e-02 of J at (81,41) to 1.05e-02 at (161,81)
while the incumbent-to-Rao thrust difference stays at 1.2-1.7e+03 N
(1.0-1.5e-05 of J) and the shape distance at 9.42-9.48e-03 m: the two
contours agree three orders of magnitude inside the band that the
ladder can resolve, at both rungs. The overnight leg's +4.83e-04 gain
(section 1.1) is 4.6 percent of the (161,81) band and 2.4 percent of
the (81,41) one -- unresolved at either.


## 4. The restoration phase in the driver, and its gate

`a1_plug_spline_opt.run_trsqp` gains a phase 1 (the block comment in the
loop carries the measurement that forced it). Structure: it is armed
only while NO in-class certified base exists, the segment then minimises
the class violation by maximising the constraint's own aggregated
margin (`fun_r` on `_mvg`'s memo, empty constraint list), acceptance
reads the violation alone, entry into the objective phase is at
KS >= mu0 strictly, and a violation that cannot be reduced at the
radius floor stops the walk as NOT RESTORABLE with its own counter.
An in-class start cannot enter it (phase1 is False at segment 0 and
W_cert is set from then on): the port is inert by construction.

- BIT-IDENTITY GATE (`k81n41_gateA/run_gate_A_2026-09-17.log`, 4173 s,
  4/4 PASS): start A, 2 segments x 8 iterations on the night's own
  derive.json. Segments 0 and 1 reproduce the overnight leg line for
  line -- J 1.15287089e+08 / |grad| 9.338e+06 / cert 0.434 / KS +0.0435
  / min cell +0.0871 / 4181 cells, then J 1.15342223e+08 / 6.909e+06 /
  0.158 / +0.0348 / +0.0784 / 4183 -- including the margin counters
  and the multipliers (-0.585, -0.016; then -25742401.238, -24449.555).
- FIRST SMOKE (267 s) caught a real defect: the phase-1 block seeded
  `counters` with an empty dict, so the constraint's `m_exec += 1`
  raised KeyError -- and the campaign reported that KeyError as "a G1
  rejector firing". Fixed by seeding the same default the objective and
  the constraint use. Worth keeping in view: the campaign's blanket
  `except` turns a code error into a physics-shaped verdict.
- PHASE 1 RUNS (`k81n41_smokeC/run_smoke2_C_2026-09-17.log`, 1768 s,
  2 segments x 2 iterations from start C): violation 4.329e-02 ->
  4.224e-02 with min cell +0.0003 -> +0.0014 and 0 folded columns
  throughout, i.e. it moves in the right direction and stays certified.
  It is SLOW: the derived trust radius is 1.526e-03 m while the start
  is 8.4e-01 m from the member, so the long legs (20 segments x 8
  iterations, launched 14:50) are the measurement, not this smoke.

## 5. The gap to Rao, decomposed (PARKED 2026-09-17 evening, owner's call)

Four measurements, all at the (81,41) rung on the tournament's own
derive; artifacts in `validation/_raogap/`.

### 5.1 The functional cannot tell the two contours apart

`run_segment_2026-09-17.log`: the straight segment
W(lam) = W0 + lam (W_rao - W0), marched and graded cell by cell.
J falls monotonically by 1679 N over the whole traverse -- **7e-4 of
band_J** -- while the fold margin falls from +0.0871 to +0.0223 and
crosses the class floor 0.0435 at lam ~ 0.79. The adjoint at our member
projects -1.760e+05 N/m on the Rao direction against |grad J|inf
9.109e+06 (2 percent, and NEGATIVE: the slope points away from Rao);
the segment's own slope -1.903e+05 N/m confirms it to 8 percent.
READING: between the two contours the objective is a FLAT VALLEY, so
nothing in J can pull a walk toward Rao -- the geometry there is
decided by the constraints, not by the functional.

### 5.2 The wall residual is a scale over 95 percent and a tail over 5

From `_axi_fan/oracle_walls.npz`, signed radial difference (GENO minus
ours) over his 4775 contour points: mean +7.70e-04 m, median +8.02e-04.
By band: +0.82/+0.79/+0.67/+0.45 mm from x 0 to 3.5 (y 1.74 -> 0.35),
i.e. a nearly constant RELATIVE offset of +5.7e-04 to +9.4e-04; then
the sign flips and grows, -1.06 mm at x 4.5-5.0, -2.48 at 5.0-5.3,
-5.60 mm at 5.3-5.62 (relative -1.7e-01). A fit dy = b y gives
b = 5.79e-04 with rms residual 2.98e-04 m: ONE constant carries the
front. Candidate cause, declared and NOT yet tested: his member
terminates at 0.9949 of our ambient (and carries -0.37 percent of the
mass target). The tail is the two problems' different end cut (his
contour ends at x 5.6102 with y_D 0.0247; ours reaches 0.0227 at
5.8762) and is where the max 7.77e-03 m sits -- outside the
construction's own ladder band 4.76e-03.

### 5.3 Why the transplant is out of class: nine cells in three columns

`run_why_out_2026-09-17.log`. Ours: min cell +0.0871 at (4,2), the 12
worst spread over columns 3, 4, 29, 64, 67-69, 74, 75; ZERO cells below
the floor. Rao on our 16 knots: min cell +0.0223 at (77,83), the 12
worst ALL in columns 75-77, and only **9 cells of 4181 (0.22 percent)**
below the floor. The transplant's wall angle ends at +0.045 deg against
our -1.852: the spline FLATTENS to reach our L. So the exclusion is the
end constraint, not his curve (as written he is at +0.0626, in class)
and not the basis's general waviness (rms second difference 0.121 deg
against our 0.079). The floor itself is mu0_1 = m_ref/2 with m_ref the
INCUMBENT's own worst cell -- a self-referential class, to be declared
wherever a verdict rides on it; note also that m_ref is rung-specific
by construction (0.0871 at (81,41), 0.0480 at (161,81)) because the
minimum is an extreme-value statistic over 4181 vs 16728 cells.

### 5.4 The overnight gain is discretisation, and it is the foot knot

`run_attrib_2026-09-17.log`: with each move alone, first knot
(+6.864 mm) gives **+5.5401e+04 N = 99.5 percent of the whole gain**,
the tip (+5.247 mm) gives **-1.49e+02 N** (a loss), the other fourteen
knots +9.33e+02 N. So the lever is the FOOT RAISE -- the one this line
re-adjudicated out of class in S21-S23 -- and not the free tip.
`run_gain_ladder2_2026-09-17.log`, the same two designs on the
tournament's rungs: dJ +5.5684e+04 (81,41) -> +3.1633e+04 (161,81) ->
**+1.3953e+04 N (321,161)**, halving per doubling; Richardson on the
three points extrapolates to -3.6e+03 N, i.e. ZERO within the spread.
The walk's return certifies at (81,41) (0.086) and at (321,161)
(0.078) and FAILS at (161,81) (1.312): a rung lottery of the kind
already on record, not a property of the design.
VERDICT: the +4.83e-04 of the overnight leg is the march's own
discretisation at the foot, and the tournament's reading stands as
"no resolved gain over the member".

### 5.5 Parked, with its prediction

The like-for-like comparison has never been run: rebuilding our member
at HIS constants (ambient 0.9949 PA, theta_E -0.0199 deg, his mass) and
at his end cut. Prediction to falsify: the +5.8e-04 front scale
collapses into the construction's ladder band and only the tail
survives. Needs a scratch copy (PA is a constant of record).

## 6. The N2 base-pressure slot made executable [X-BPRS]

`validation/base_pressure.py`, new carrier; the flag `A1_BASE_MODEL`
prices its closure into `a1_plug_spline_opt.J_replay`. The slot's own
question -- what pressure acts on the face a truncated plug leaves --
is the choice ledger's C61 with status NEVER and an incumbent the
program has NOT adopted (Vander Veen's constants, practiced in the
legacy chain only). This is that slot made runnable, not a fit: there
are no data to fit (the only hot-fire base measurement of record is
nozzleless, another geometry, cycle-mean).

### 6.1 What "generalising Veen" turned out to mean

Veen Eq. (9) is `p_b = p_H C / M_H^E`, C = 0.846, E = 1.30, on the
state at the truncation corner -- and it is a curve fit of Rom's 1966
near-wake PROJECTILE data, which Fick & Schmucker and WG10 judge
failed. Every other classical member reads the SAME two inputs (the
corner state and the ambient), so they are interchangeable at one call
site: hence `p_base(p_e, M_e, gam, p_a, model, th)` with `MODELS`
carrying each member's evidence class, and `MODELS_UNREADABLE`
carrying, IN THE CODE, the ones our reads cannot execute and why
(Korst's four-domain chain is a solve, not a closure; Stechmann's is
calibrated on preburner warm-oxygen data).

TWO MEMBERS THE READ OF RECORD UNLOCKED TODAY (thesis_valeriani ch. 4,
Nasuti's own group, on disk and never read):
- **the Sapienza/Univ. Rome member** (Onofri Eq. (5.7)), the one WG10
  measures as best and whose error bracket [+19 %, -15 %] is the band
  this module carries: the symbol the harvest left undefined is the
  WALL ANGLE at the truncation. Its exponent
  `Phi = (-0.2 phi^4 - 5.89 phi^2 + 20179.84)/(phi^4 + 20179.84)`
  changes sign at **phi = 17.4143 deg** (closed form, PHI_ZERO), and
  past that the member returns p_b > p_w -- unphysical, and the exact
  failure the same read describes in words. On our member (wall
  33.03 -> 1.85 deg) it inverts at **25 of 81 stations**.
- **Rocketdyne's member** (Onofri Eq. (5.6)), which is not a pressure
  model at all: substituting C_F = F/(p_c A_t) and eps_b = A_b/A_t,
  `p_b = 0.58 (F_e - F_w)/A_b` -- the chamber and the throat cancel and
  what is left is 58 percent of THE THRUST THE TRUNCATION GIVES UP.
  Separate entry point on purpose. Measured consequence at the ideal
  length: F_w -> F_e so p_b -> 0 EXACTLY, i.e. it degenerates into NASA
  SP-8120's 1976 assumption (base term -1.2321e+03 N, identical to the
  `zero` member) -- the signature of a thrust closure worn as a
  pressure. Declared open: whether the source's C_F are vacuum or
  ambient-referenced (our J is ambient-referenced, so our reduction
  carries an extra -p_a A_b).

### 6.2 The derive of record: 10/10 (95.8 s, `_base_pressure/run_derive_2026-09-17.log`)

On our own member at the (81,41) posing. What it measured:
- **The family disagrees by an order of magnitude and three of its
  members are absurd outside their class.** p_b/p_e at the tip ranges
  0.0000 (zero, rocketdyne) / 0.2166 (veen) / 0.9007 (panov_shvets);
  and read across the whole ladder, `rome`, `conical` and
  `cylindrical` put their argmax at 1.2 percent of the length with base
  terms of +1.94e+07, +1.53e+07, +1.43e+07 N -- **17, 13 and 12 percent
  of J** -- because there p_e is 4.6 p_a on a 1.43 m base. The same
  absurdity is found and cut from the plots in the read of record. The
  window `ENVELOPE_RETAINED` (12-100 percent of length, from Eq. (5.3)'s
  "12-16 % plug lengths" and ADR-D4's 20 percent) REPORTS them; it
  never clips silently.
- **On our member, in class, truncation does not pay**: the argmax sits
  at the last station for veen, panov_shvets, zero and rocketdyne
  alike, and the base term there is a small depression (-9.91e+02 N).
  The Humphreys rejector therefore CANNOT fire on a fixed member (it
  moves the argmax by 0 stations and J by 6.6e-06): his exhibit lives
  where the contour is re-optimised under a cap, which is the
  configuration tournament, not this stage.
- **Our stationarity is not Veen's corner relation.**
  `dJ/dx = 2 pi y [y'(p_b - p_w) + y p_b'/2]` (verified against the
  ladder's own dJ/dx to 1.9e-03) is an OPTIMALITY; Eq. (8) turns the
  corner flow through p_w -> p_b and is a COMPATIBILITY. On our member
  they sit 2.87 m apart. Conflating them was this stage's first posing
  error, recorded here because the correction is the content.
- **The wake regime at our own point is NOT settled**: PR 33.23 equals
  the member's own design PR by construction, so Hagemann's criterion
  puts us AT the transition (closed side, since truncation triggers it
  earlier) while the Purdue nozzleless data would read closed outright.
  They disagree; the module returns both.

### 6.3 Ported into the functional, inert by default

`J_replay` gains the base term under `A1_BASE_MODEL` (unset = the
functional of every row of record). Gate of record
(`_base_pressure/run_basegate_2026-09-17.log`): with the flag unset,
J is IDENTICAL to the last digit for the incumbent (1.1528708908e+08)
and for the overnight leg's return (1.1534277263e+08). With the base
priced, the leg's gain moves by at most -4.79e+02 N of +5.57e+04
(veen; conical -77 N, cylindrical +6 N, zero -636 N): **the base does
not change that ranking**, which is consistent with section 5.4's
attribution of the gain to the foot knot and to discretisation.
WHY THE FLAG EXISTS AT ALL: the tip radius is a free design variable
while the face it creates was not in J, so a walk could shorten the
spike without paying for its base.

### 6.4 The truncation curve and the finding the selector has to live with
(stage `band`, 2/2 PASS, 97.4 s, `_base_pressure/run_band_2026-09-17.log`)

At each shared length cap: the core thrust, the base term of every
admissible closure with the band its model form carries, and the SPREAD
across closures, all in newton against the tournament's own band_J
2.297e+06 (1.99e-02 of J).

| L_cap | wall | loss vs full | closure spread | spread / loss |
|---|---|---|---|---|
| 12.5 % | -24.7 deg | -3.50e+06 N (1.52 band_J) | 7.03e+06 N (3.06 band_J) | 2.0 |
| 25.0 % | -19.3 deg | -1.41e+06 N (0.62) | 3.13e+06 N (1.36) | 2.2 |
| 37.5 % | -15.8 deg | -5.91e+05 N (0.26) | 1.60e+06 N (0.70) | 2.7 |
| 50.0 % | -13.1 deg | -2.39e+05 N (0.10) | 6.62e+05 N (0.29) | 2.8 |
| 62.5 % | -10.9 deg | -8.84e+04 N (0.04) | 2.68e+05 N (0.12) | 3.0 |
| 75.0 % |  -8.9 deg | -2.62e+04 N (0.01) | 8.51e+04 N (0.04) | 3.2 |
| 87.5 % |  -6.8 deg | -5.47e+03 N (0.00) | 1.70e+04 N (0.01) | 3.1 |
| 100 %  |  -1.9 deg | 0 | 1.23e+03 N | -- |

THE FINDING: at every cap the disagreement AMONG the closures is
**2 to 3 times the truncation loss they are supposed to correct**. The
base term as the classical literature leaves it therefore cannot decide
a truncated-plug design at any length: it can be carried and declared,
never used to arbitrate. That is the quantitative form of the harvest's
own verdict ("nothing can be actually said on the average pressure of
the recirculating region") and it is the constraint the bell-vs-plug
selector must be built around -- decide by VALUE against the SUM of
bands, and declare "argmax not resolved" whenever the closure spread
covers the difference, which on this member is everywhere.
Two rows of record from the same run: B-1, at full length every
closure's interval contains the untruncated J (spread 1.23e+03 N);
B-2, the core thrust decreases only where the wall pressure is below
the ambient (exactly one step, the last one -- p_w/p_a 0.905 at the
tip, so the final stretch of an ideal member pushes backwards). B-2 as
first posed asserted plain monotonicity and was wrong; the conditional
statement is the physical one.

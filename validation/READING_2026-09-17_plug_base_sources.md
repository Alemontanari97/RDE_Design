# Reading of record — the plug-base sources read on 2026-09-17 (S30) and 2026-09-18 (S31)

Two papers read in full during S30, in the session that made the N2
base-pressure slot executable ([X-BPRS]) and started the wake chain
(W1/W2); two more on 2026-09-18 (S31, sections 3 and 4), the day the
family was graded on measured points. This file is the READING, with
its page anchors, so the numbers used elsewhere have a home; it is not
an adjudication.

**FILING STATUS, declared:**
- Humphreys, Thompson & Hoffman 1971 — **on disk**,
  `GENO/literature/design-of-maximum-thrust-plug-nozzles-for-fixed-inlet-geometry.pdf`,
  registry row `humphreys_thompson_hoffman_1971`. The content below is
  now PAGE-VERIFIED against the source (it was carried second-hand from
  BASE_PRESSURE_HARVEST_c4.md §13 until today).
- Sule & Mueller 1973, JSR 10(11):689-695 — filed 2026-09-18 (commit
  ef64a59, `GENO/literature/sule1973.pdf`, row `sule_mueller_1973`).
- Chutkey, Vasudevan & Balakrishnan 2014, JSR 51(2):478-490 — **on
  disk**, row `chutkey_2014`, READ IN FULL 2026-09-18 (section 3). Its
  Tables 7-8 are consumed by `base_pressure.py` (stage `data`).
- Channapragada 1963, AIAA J 1(9):2188-2190 — on disk, row
  `channapragada_1963`, READ 2026-09-18 for what the Korst chain needs
  (section 4); its equations are figure-borne and are NOT transcribed
  here (to be done when W4 is written).

---

## 1. Humphreys, Thompson & Hoffman 1971, AIAA J 9(8):1581-1587

Maximum-thrust plug contours for FIXED INLET geometry by the calculus
of variations, with the base pressure inside the functional.

### 1.1 The closure we inherit, at its source (p. 1582, Eq. (12))
`p_b = 0.846 p / M^1.3`, introduced verbatim as "the following
empirical equation which is a curve fit of the data presented in
Ref. 9" = **Rom 1966, near-wake pressure by the momentum integral
method, JSR 3(10):1504-1509**. The paper states what the harvest
reported: the optimisation procedure is INDEPENDENT of the base
pressure model, and the base pressure "must be treated in the
variational problem as a constant which is not known a priori",
recomputed each iteration for compatibility with the flowfield.

### 1.2 The rejector exhibit, page-verified (pp. 1586-1587, Table 4, Fig. 6)
Swapping Eq. (12) for Eq. (38), the Panov-Shvets form
`p_b = p_inf [1 - 0.715 gamma (M^2.3 - 0.92 M^2 - 0.03) / M^2.7]`
(their Ref. 12), at everything else fixed:
- base height y_D **0.954 -> 2.34 in** (x2.45);
- wall slope at D **-13.26 -> -3.08 deg**;
- thrust **32,881 -> 32,965 lbf (+0.26 percent)**.
"the base pressure model has a considerable effect upon the shape of
the plug contour" and "in addition to a direct change in the thrust
contribution of the plug base, the base pressure model significantly
influences the shape of the optimum contour."
CONSEQUENCE FOR US, unchanged by the verification: the closure moves
the ARGMAX by O(1) and the VALUE by O(0.3 percent), so a configuration
selector must decide by value against summed bands and declare "argmax
not resolved" otherwise. NOTE the reference pressure: Eq. (38) is
written on p_inf (the AMBIENT), Eq. (12) on the local p -- the
difference this module's `_panov_shvets` and `_veen` carry, and both
forms are now confirmed against the source, coefficient by coefficient.

### 1.3 THE START-LINE FINDING (p. 1586-1587) — the precedent for our parked Rao item
Their parametric optimum (21 designs, Table 1) lands at cowl lip radius
7.55 in, injection angle -34 deg, thrust **32,881 lbf**. Rao's method on
the SAME mass flow, length, ambient, gas and base-pressure model gives
cowl lip 8.33 in, injection -58.5 deg, thrust **34,253 lbf** -- and
"the two contours are almost identical in shape except in the throat
region, the most significant difference being in the injection angle
and cowl lip radius". They then chase the discrepancy to its cause:
- with a linear sonic start line (Rao's assumption) the contour matched
  "reasonably well but the thrust was approximately 2700 lbf lower";
- **taking a right-running characteristic near the throat FROM RAO'S OWN
  FLOWFIELD as the start line produced "a contour almost identical to
  Rao's" and a thrust of 34,373 lbf against Rao's 34,375** -- a
  difference of 2 lbf, **5.8e-05**;
- verbatim: "when compatible start lines are employed, the two
  techniques yield the same results ... the start line model is very
  important in the design of optimum plug nozzles, and approximations
  in this region should be carefully evaluated."

This is a PRECEDENT OF RECORD for the item S30 parked (§5.5 of the
session log): our member differs from GENO's Rao member by 1.5e-05 of J
and by a uniform 5.8e-04 radial scale traced to the terminal ambient
and the mass convention, i.e. to the POSING, and the literature's own
answer to the same question is that the two methods coincide once the
posing is made compatible. It does not prove our case -- it says the
experiment we parked is the one the field itself ran, and what it found.

---

## 2. Sule & Mueller 1973, JSR 10(11):689-695 (READ IN CONVERSATION, PDF NOT ON DISK)

The experimental truncation parametric the corpus lacked: base pressure
MEASURED by static taps in the plug base, over the open-to-closed wake
range, with plug length as the parameter.

### 2.1 The rigs (pp. 690, Tables 1-2)
Two internal-external-expansion axisymmetric plug nozzles, **conical
plugs converging at 10 deg**: ATP1 (design M 1.90, A_ne/A_nt 1.555,
throat 0.330 in^2, shroud radius 0.405 in, L_max 1.374 in) with six
truncations L/L_max 0.2184-0.4802 and base radii 0.188-0.125 in; ATP2
(M 2.00, 1.688, throat 0.602 in^2, shroud radius 0.568 in, L_max 2.070
in) with five truncations 0.1449-0.3785 and base radii 0.312-0.227 in.
Shroud cylindrical, 0.300 in from the throat. gamma 1.4, T_b/T_01 1.00.

### 2.2 The parametrics (the question that prompted the read)
- **Fig. 4**: closed-wake base pressure ratio vs PLUG LENGTH RATIO
  (hence vs base radius): **p_b decreases as the plug gets longer**,
  experiment and theory, both nozzles; and it decreases with increasing
  area ratio.
- **Fig. 9**: base pressure ratio vs **CONICAL PLUG HALF-ANGLE**, 8 to
  12 deg, three plug lengths: **p_b INCREASES with the angle**, roughly
  0.09 -> 0.18 of P_01 (ATP1, P_01 100 psia, P_at/P_01 0.16). Their
  mechanism: a larger half-angle raises the expansion ratio to the
  shroud exit, so the exit Mach is higher and less expansion remains to
  reach the ambient. CAUTION: this alpha is the half-angle of the WHOLE
  conical plug, not the local wall angle at the truncation, which is the
  phi of the Sapienza correlation -- related variables, not the same one.
- **Fig. 5**: the overall pressure ratio at wake CLOSURE decreases with
  increasing plug length and area ratio: shorter plugs close earlier
  (at lower altitude).
- **Fig. 8**: +100 percent shroud length -> **+104 percent** base
  pressure ratio.

### 2.3 The statement that reorders our plan (pp. 690, 695)
"During the open wake regime of operation the base pressure is
essentially equal to the ambient pressure", repeated in the
conclusions, and visible in Fig. 2 as data lying on the P_b/P_at = 1
line for every plug length. **So in the open regime there is no base
term to model at all.** Since our own operating point sits ON
Hagemann's transition (PR 33.23 equals the member's own design PR), the
REGIME test decides the base term before any closure does.

### 2.4 Their model IS the chain we proposed, and it has TWO empirical inputs
Axisymmetric ROTATIONAL MoC (entropy gradients behind the internal
shock) + Hartree's technique for embedded shocks + an 85 percent
overexpansion trick to make the internal shock appear near the corner
where it physically starts + Korst's restricted mixing theory with an
error-function profile phi = (1 + erf eta)/2, eta = sigma y/x, eta_R = 3,
coupled iteratively to the MoC over a "conetail".
The two empirical inputs, both named in the paper: **the jet spread
parameter sigma** (from Channapragada 1963) **and the recompression
location r3/rb, "found from experimental data"**. This CORRECTS the
claim made in session that a mechanistic closure would reduce the
uncertainty to a single banded parameter: it is two.

### 2.5 The accuracy class to beat, and the validity limit
- theory **15 percent above** experiment in the region of practical
  interest (10 percent for the larger ATP2), attributed to the
  neglected wall boundary layers;
- the internal shock is worth half the error: ATP1 at L/L_max 0.4802,
  experiment **0.070**, no-shock theory 0.0879 (27 percent), with-shock
  0.0783 (**12 percent**);
- the constant-pressure boundary location is predicted to 5.4 percent
  (the order of the experimental accuracy);
- declared validity limit **L/L_max ~ 0.50** for the base-pressure
  solution.
- Measured closed-wake levels: P_b/P_01 0.07-0.18 at P_at/P_01 0.16,
  i.e. **P_b/P_at ~ 0.5-1.1**. Our incumbent closure on our own member
  gives p_b/p_a 0.20-0.43: DEEPER than the whole measured range. Cold
  air, shrouded nozzle, different NPR and geometry -- it grades
  DIRECTION and ORDER, never a value.

---

## 3. Chutkey, Vasudevan & Balakrishnan 2014, JSR 51(2):478-490 (READ IN FULL 2026-09-18)

Truncated ANNULAR plug nozzles (ATPN) of four lengths, cold air,
experiment + RANS, with a closed-wake base-pressure correlation fitted
on the open literature's annular data. The paper the N2 slot was
missing: it gives the base pressure AND the lip state at the same
point, so the closure family can be graded without a march.

### 3.1 The rig (pp. 479-480, Tables 1-2, Figs. 1-4)
Primary nozzle: a convergent duct given ANALYTICALLY (horizontal line
X1 in [-6.294, -3.744] mm; arc R 1.343 mm to -2.743; 45 deg line to
-0.617; arc R 0.867 mm to 0), throat height 2.647 mm, tilted by
theta_t = 56.9 deg. Plug: Angelino's MoC for PR_des 66 (exit M 3.4),
plug exit radius 32 mm (exit area 3.2e-3 m^2), full length 106.2 mm,
area ratio plug/throat 6.18, mdot 8.12 kg/s at design, p_a 101,325 Pa.
Truncations 20 / 34 / 41 / 48 percent, base radii 15.65 / 11.30 /
9.51 / 8.01 mm. **Fig. 2b (p. 479) is the full-length plug contour**
(X 0-106.2 mm, Y 32 -> 0 mm) -- the figure to digitise for a march
twin; Fig. 2a is the primary nozzle (not needed, analytic). A mild
compression wave at the primary-nozzle/plug junction is declared and
said not to affect the inferences (p. 483).

### 3.2 Measurements and CFD (pp. 480-485)
Static taps on the 20 percent plug (plug surface + base, base ports at
several radii: measured p_b "fairly uniform"); the longer plugs carry
base taps only. Stagnation pressure by pitot in the feed pipe (1
percent between transducer and dial gauge). **Fig. 9d (p. 483): plug
pressure p/p_0 vs x at PR 66.6 on the 20 percent plug, five
experimental points (x ~ 0, 2.5, 6, 9.7, 13.5 mm) on the CFD line** --
the wall-pressure comparison of record for a twin; Fig. 9a-c the same
at PR 5.85 / 9.9 / 20.4. RANS (HiFUN, Roe, compressibility-corrected
SA, y+ < 1, grids 1.2e6 and 4.6e6 cells): the PLUG SURFACE pressure is
grid-converged and matches experiment; the BASE pressure is not
predicted -- grid-converged averaged p_b differs from experiment by up
to **35 percent** (11 percent between the two grids at PR 66; p. 485),
non-uniform where the measured one is uniform, and biased
**above** experiment on annular plugs (below on linear ones). This is
the accuracy class of a RANS "confirmation" on a plug base.

### 3.3 Regimes and transition (pp. 483-488, Table 5-6, Fig. 20)
Three regimes: type 1 (wave interactions on the plug), type 2 (plug
lip under the fan: p_lip/p_0 constant), CLOSED wake (p_b/p_0 constant
with PR). Transition PRs measured: **42 / 57 / 60 / 60** for 20 / 34 /
41 / 48 percent (design PR 66), i.e. longer plugs close LATER and the
transition PR **asymptotes to ~0.9 PR_des** (Fig. 20a: the last ray of
the fan impinging at the end of the bubble, Nasuti-Onofri's criterion,
which predicts them to -0.5 / -11.0 / -8.2 / -1.4 percent, Table 6).
In the OPEN wake the annular p_b "varies significantly about the
atmospheric pressure" (unlike the linear plug); "from the viewpoint
of design, it may still be reasonable to assume that an atmospheric
pressure prevails on the base surface in the open wake regime"
(p. 488). NOTE against Sule & Mueller Fig. 5 (closure PR DEcreasing
with plug length): the two rigs disagree on the direction of the
transition PR with length; not adjudicated here.

### 3.4 The closed-wake data and the correlation (pp. 488-489, Tables 7-8, Eq. (1), Fig. 19, 21)
**Tables 7-8**: ten annular closed-wake points (Tomita 1998, their four
ATPN, Fick & Schmucker's 24-module and three annular cases, ref [30])
each with design PR, retained length, plug exit angle beta (their
four), **base-lip Mach M_lip (from the RANS), p_b/p_lip MEASURED,
p_b/p_0 MEASURED**, and the paper's own four model columns (Eq. (1),
Fick & Schmucker cylinder and cone relations, Onofri's relation) with
percent errors. Transcribed verbatim into `base_pressure.CHUTKEY_2014`.
**Eq. (1)** (p. 489): p_b/p_0 = (p_lip/p_0) [0.05 + 0.967 (1 +
(gamma-1)/2 M_lip^2)^-1]^0.7027, the Lamb-Oberkampf cylindrical form
with the exponent least-squares fitted on the ten points. Errors of
Eq. (1) on its own data: +20.0 / +43.2 / +11.0 / +3.9 / +15.4 / +4.9 /
-21.4 / -21.4 / -32.0 / -39.5 percent. **Fig. 19**: closed-wake
p_b/p_0 falls LINEARLY with retained length at -2.3e-4 per percent on
the ATPN series (0.0165 / 0.0131 / 0.0116 / 0.0100), the linearity
Sule & Mueller also reported; the correlation is monotone but not
linear. Onofri's relation: +166.7 / +80.7 / +51.8 / +37.6 percent on
the four ATPN (beta 19.13 / 14.26 / 12.65 / 11.44 deg).

### 3.5 What stage `data` measured on these points (2026-09-18)
Known-answer: our `_conical`, `_cylindrical`, `_rome`, `_chutkey`
reproduce the paper's four model columns at every point to one
printed digit (34 values, worst 7.6e-05) -- our members ARE the
literature's relations. Grading (p_b/p_lip, relative to measured):
chutkey mean -0.02 rms 0.25 [-0.40, +0.43]; cylindrical +0.23 / 0.31;
conical +0.33 / 0.43; Sapienza +0.84 / 0.98 on its 4 points, ABOVE at
every one; **Veen -0.63 mean, [-0.82, -0.41], BELOW at every point**;
Panov-Shvets [-0.74, +1.73] (a p_a-referenced closure on a closed wake
whose measured p_b/p_a spans 0.28-3.04 across rigs). Measured
p_b/p_lip = **0.510 +- 0.075** over M_lip 2.61-5.35: the closed-wake
base sits at half the lip pressure, weakly in Mach -- Veen's M^-1.3
fall-off (0.24 -> 0.10 over the same range) is not in the data. The
WG10 bracket [+19, -15] carried as BAND_PB holds for NO member on this
dataset; the bands of record are now the measured ones, per member.

---

## 4. Channapragada 1963, AIAA J 1(9):2188-2190 (READ 2026-09-18, equations figure-borne)

Technical note: a semi-empirical compressible JET SPREAD PARAMETER
sigma for mixing-zone (Korst-class) analyses. Starting point: Korst &
Tripp's empirical sigma = 12 + 2.76 M. Model: Prandtl mixing length +
Howarth transformation with the density ratio represented by the mean
flow (rho_r/rho ~ (rho_1 + rho_2)/rho_1), giving sigma/sigma* as a
function of the jet Crocco number and the stagnation-temperature ratio
(Eqs. (8)-(9), p. 2189), sigma* = 12 (Tollmien, incompressible; D =
0.25 the divergence constant). Claimed: good correlation with Vasiliu,
Maydew & Reed and Zumwalt's data (with virtual-origin correction);
**upper limit sigma/sigma* = 4 as the Crocco number -> 1**; a hotter
jet gives a LOWER sigma/sigma* (faster spread). The equations are in
the scanned figures and were not transcribed: to be read off the page
when the mixing-layer algebra (W4) is written. What the N2 line takes
today: sigma is the ONE of the Korst chain's two empirical inputs that
has a published closed form in (M, T_0 ratio); its band across the
formulations on Fig. 3 is the band the chain inherits.

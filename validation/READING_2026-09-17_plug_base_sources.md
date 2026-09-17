# Reading of record — the two plug-base sources read on 2026-09-17 (S30)

Two papers read in full during S30, in the session that made the N2
base-pressure slot executable ([X-BPRS]) and started the wake chain
(W1/W2). This file is the READING, with its page anchors, so the
numbers used elsewhere have a home; it is not an adjudication.

**FILING STATUS, declared:**
- Humphreys, Thompson & Hoffman 1971 — **on disk**,
  `GENO/literature/design-of-maximum-thrust-plug-nozzles-for-fixed-inlet-geometry.pdf`,
  registry row `humphreys_thompson_hoffman_1971`. The content below is
  now PAGE-VERIFIED against the source (it was carried second-hand from
  BASE_PRESSURE_HARVEST_c4.md §13 until today).
- Sule & Mueller 1973, JSR 10(11):689-695 — **NOT on disk**. It was read
  in conversation on 2026-09-17; `GENO/literature/` has no copy, so NO
  literature-registry row can cite it yet (the four-roots lint requires
  a resolvable path). **File the PDF before any carrier consumes these
  numbers.** Until then this reading is the only record.

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

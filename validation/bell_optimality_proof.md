# Formal optimality proofs for the nozzle area-ratio in the Stechmann model

Status: THEOREMS within the model's stated hypotheses, not heuristics.
Executable verification: `tests/test_bell_optimality.py` (lemma by central
differences; first/second-order conditions and global dominance on the
shipped Table-1 states).

## Hypotheses (the model, as in the paper and in `st_core.py`)

H1. Quasi-1D isentropic nozzle expansion, gamma and M frozen (paper asm. 2).
H2. Thermally choked throat all cycle: mdot = Pc A_t / c* (Eq. 6).
H3. Fixed geometry (bell): the exit state lies on the isentrope through the
    chamber state, so NPR = Pc/Pe = NPR(eps, gamma) is TIME-CONSTANT.
H4. Full-flowing nozzle (no separation) even when overexpanded (paper choice).
H5. Pc(t) > 0 periodic, integrable (the exponential blowdown is NOT needed
    for these theorems; any cycle shape works).

## Lemma (Euler momentum theorem for a choked isentropic nozzle)

For steady quasi-1D isentropic flow from a reservoir at Pc through a choked
throat, with F = mdot u_e + (Pe - Pa) A_e:

    dF/dA_e = Pe - Pa            (exact)

Proof. Choking (H2) makes mdot independent of A_e. As A_e varies, the exit
state moves along the fixed isentrope, on which the streamwise momentum
balance gives mdot du_e = -A_e dPe. Hence

    dF = mdot du_e + Pe dA_e + A_e dPe - Pa dA_e
       = -A_e dPe  + Pe dA_e + A_e dPe - Pa dA_e = (Pe - Pa) dA_e.  QED

In thrust-coefficient form, dividing by Pc A_t and using eps = A_e/A_t:

    dCF/deps |_Pc = (Pe - Pa)/Pc = 1/NPR(eps,g) - Pa/Pc.

This is simultaneously an algebraic identity of Eq. 9: the derivative of the
momentum term through NPR(eps) cancels exactly against the eps-term's
NPR-variation (CF_mom'(NPR) = eps/NPR^2), leaving only the explicit
(Pe - Pa)/Pc. The executable test verifies this by central differences over
a (gamma, eps, Pc) grid, to guard the implementation, not the calculus.

## Theorem 1 (bell: existence, uniqueness, globality)

Let Isp(eps) = Int[mdot CF c*] / (g0 Int[mdot]) over one cycle. Then, under
H1-H5, with <Pc> the plain TIME mean of Pc(t):

  (a) Isp'(eps) = (A_t tc / (g0 D)) * ( <Pc>/NPR(eps,g) - Pa ),
      D = Int[mdot dt];
  (b) if <Pc>/Pa > NPR(1,g) = ((g+1)/2)^(g/(g-1)), Isp has exactly one
      stationary point eps*, given by NPR(eps*,g) = <Pc>/Pa, and it is the
      GLOBAL maximum on the supersonic branch (strictly increasing before,
      strictly decreasing after; second-order condition automatic);
  (c) otherwise Isp is strictly decreasing and eps* = 1 (boundary).

Proof. The denominator D is eps-independent. In the numerator, mdot c* =
Pc A_t (H2), so N(eps) = A_t Int[Pc CF dt]. The integrand is C^1 in eps on a
compact cycle, so Leibniz applies:

    N'(eps) = A_t Int[ Pc * dCF/deps dt ]           (Leibniz)
            = A_t Int[ (Pe - Pa) dt ]               (Lemma; Pc cancels)
            = A_t tc ( <Pc>/NPR(eps,g) - Pa )       (H3: Pe = Pc/NPR).

Note the mass weighting drops out EXACTLY (mdot c* = Pc A_t): the optimality
mean is the plain time mean, not the mass-weighted one. On the supersonic
branch NPR(., g) is continuous and strictly increasing (area-Mach relation:
dA/dM > 0 for M > 1) with NPR(1) = ((g+1)/2)^(g/(g-1)) and NPR -> inf.
Hence N'(eps) is positive iff NPR < <Pc>/Pa, zero at equality, negative
beyond: a single sign change + -> -. (b), (c) follow. QED

Corollary: the optimum bell is perfectly expanded at the time-mean chamber
pressure, <Pc> = P_CJ * I(1) = Pcp (1 + DC) for the matched exponential
cycle. This is what `bell_opt` evaluates in closed form; the golden-section
search is kept as an independent numerical confirmation (<1e-3 in all rows).

### Theorem 1 through Stechmann's averaging machinery, equation by equation

Nothing in the proof bypasses the mass-weighted cycle averaging; every
Stechmann equation is used where it belongs:

1. Eq. 4 (kept verbatim):  Isp = Int[mdot CF c* dt] / (g0 Int[mdot dt]).
2. Eq. 6 + Eqs. 1/15: mdot(t) = Pc(t) A_t / c*(t) with c*(t) =
   c*0 (Pc/P_CJ)^((g-1)/(2g)). In the NUMERATOR weight the Eq.-15 time
   dependence enters mdot and c* reciprocally and cancels EXACTLY:
       mdot(t) c*(t) = Pc(t) A_t     for ANY c*(t) law.
   This is the pivot of the theorem: the mass weighting does not disappear
   by assumption - it collapses algebraically.
3. Lemma (Eq. 9 identity): N'(eps) = A_t Int[(Pe - Pa) dt].
4. Eqs. 13-14 (exponential blowdown): <Pc>_t = P_CJ I(1),
   I(k) = (1 - PR^-k)/(k ln PR); with the Sec.-III matching
   P_CJ = Pcp (c*0/c*_cp)/I(k), k = (g+1)/(2g), this is exactly
   <Pc>_t = Pcp (1 + DC) - the repo's DC identity.
5. The DENOMINATOR g0 Int[mdot dt] = g0 A_t (P_CJ/c*0) tc I(k) is
   eps-independent: the mass-flow normalization can never move the
   stationary point in eps.

Hence NPR(eps*, g) = <Pc>_t / Pa = Pcp (1 + DC)/Pa, with the PLAIN TIME
mean appearing as an exact CONSEQUENCE of the machinery (step 2), not as a
simplification of it. The plausible-but-wrong alternative - using the
mass-weighted mean pressure <Pc>_mdot = P_CJ I(1+k)/I(k) > <Pc>_t - gives a
measurably larger eps and a strictly lower Isp; the executable test checks
this discrimination per row (T1c), so the test suite can REJECT the wrong
averaging, not merely confirm the right one.

## Theorem 2 (aerospike: monotone, then exactly flat; knee = min argmax)

Under H1-H5 with the ideal-plug closure (Eqs. 10-12; exit-area cap eps_max):

    dCF_spike/deps = (Pe - Pa)/Pc * 1{exit-area-limited} >= 0,

since on the limited set Pe(t, eps) > Pa (Eq. 12) and on the adapted set CF
does not depend on eps. Therefore Isp(eps) is nondecreasing; for eps >=
eps_knee with NPR(eps_knee, g) = Pmax/Pa the limited set is empty at every
instant and Isp is EXACTLY constant. Hence the set of maximizers is
[eps_knee, inf) and eps_knee is its minimum-area element: the correct
engineering optimum. A blind interior-point search would return an arbitrary
plateau point; the closed-form knee plus the sweep verification (monotone
below, flat above) is the rigorous treatment. QED

## Theorem 3 (vacuum: no finite optimum)

Pa = 0 gives N'(eps) = A_t tc <Pc>/NPR(eps) > 0 for all eps: Isp is strictly
increasing, no finite maximizer exists. eps is then a geometric
SPECIFICATION (the paper's eps_max = 15/150), not an optimization result. QED

## Where the theorems can break PHYSICALLY (declared, paper choices kept)

- H4 (no separation): a real overexpanded bell separates late in the cycle
  and loses less than the model's full-flowing CF; the real eps* shifts.
- H2 in the low tail: the 20-atm hydrocarbon cycles dip marginally below
  choking (margins 0.97 / 0.65); the paper retains assumption 3 there.
- H1: gamma frozen; equilibrium-vs-frozen bounds are quantified elsewhere
  in the repo (frozen-composition bound quoted in the examples).

## The outer DOF (phi) has no closed form - and why the lattice is rigorous

Isp(phi) passes through Cantera equilibrium states (HP and CJ): it is not an
analytic function, so no stationarity condition in closed form exists.
The rigorous tool is therefore the certified lattice search of `phi_opt`:
auto-extending bracket (seed-independent), parabolic acceleration, hill-climb
on the 0.01 lattice (the paper's own phi resolution), and the certificate
that both 0.01-neighbours are STRICTLY lower (`ev(p) < F[cur]`, matching
this statement) - an executable local-optimality proof at that resolution -
plus the per-row superiority check against the paper's phi.

Global-in-phi evidence is EXECUTABLE, not narrative: phi_opt scans every
evaluated phi point and counts strict local maxima (n_local_max, persisted
per optimization together with the full [phi, Isp] grid in
data/st_nozzle_opt.json full_rows); `unimodal = (n_local_max == 1)` is a
PASS gate of optfull and is asserted for all 36 optimizations by
tests/test_bell_optimality.py (T3).

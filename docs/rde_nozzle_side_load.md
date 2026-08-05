# Rotating side-load lemma — the m = 1 selection rule (T-SLRW)

Status: THEOREM of record (2026-08-05, S15 deep-foundations campaign,
[RIGOR/A]; user question of record from the S15 mandate). Statement,
full proof, corollaries, breakage channels, and the DISPOSITION OF
RECORD (secondary output vs c-slot) for the problem (P) of M0 D2.6.
Carrier: [X-SLRW] `validation/side_load_rotating_lemma.py` (symbolic
selection rule + numeric full-surface-integral verification + three
rejectors). Registry: [T-SLRW]/[X-SLRW].

Audit line: [Class: THEOREM | Falsifier: carrier rejectors R1-R3
(counter-rotating pair, unequal amplitudes, corrupted kernel) — any
undetected nonzero transverse resultant in the n>=2 class kills the
lemma | Carrier: X-SLRW | Gamma: closure-agnostic (no EOS enters; the
statement is kinematic, valid for ANY scalar wall-pressure trace —
stronger than EOS-general)].

------------------------------------------------------------------------------
## 1. Setting and hypotheses (minimal, by design)

 H-SL1 (geometry): S is a RIGID surface of revolution about the x-axis
       — a finite union of piecewise-C^1 profile patches r = R(x),
       x in [x0, x1] (annular faces x = const included as the
       degenerate case). Nothing else about S is used.
 H-SL2 (data): the wall-pressure trace is a ROTATING PATTERN,
           p(x, theta, t) = f(x, theta - Omega t),
       with f(x, .) 2pi-periodic and L^1 in the azimuth for a.e. x,
       and x -> ||f(x,.)||_{L^1} integrable. Nothing else about p is
       used: NO Euler equations, no smoothness (azimuthal JUMPS —
       shocks — are admitted), no EOS, no irrotationality.

That is the whole hypothesis list. The lemma is KINEMATIC: it holds
for viscous, reacting, turbulent-in-the-corotating-frame flows alike,
provided only that the wall trace rotates rigidly (the [DIR-PERIODIC]
standing data scope) over an axisymmetric surface. This is the
hypothesis-minimization standard of the S15 campaign applied at the
statement level (axis B).

Azimuthal Fourier expansion (defines the coefficients used below):
f(x, phi) = sum_m c_m(x) e^{i m phi}, with c_{-m} = conj(c_m) (p real).

------------------------------------------------------------------------------
## 2. Statement

[T-SLRW] THEOREM (rotating side load; m = 1 selection rule).
Under H-SL1 + H-SL2, write the pressure-load resultants on S as
F = (F_x, F_y, F_z), M = (M_x, M_y, M_z) (moments about the origin,
axis on the x-axis), and set the complex transverse combinations
F_perp := F_y + i F_z, M_perp := M_y + i M_z. Then:

 (i)  GEOMETRIC SELECTION (any p, rotating or not): each resultant is
      a SINGLE-WAVENUMBER functional of the azimuthal spectrum of p:
        F_x  and (for shear-free loads) M_x are m = 0 functionals;
        F_perp and M_perp are m = 1 functionals:
          F_perp(t) = Int_x R(x) [Int_0^{2pi} p e^{i theta} dtheta] dx,
          M_perp(t) = i Int_x R(x)(x + R R') [Int_0^{2pi} p e^{i theta}
                      dtheta] dx.
      Moreover M_x == 0 IDENTICALLY for pressure loads on any surface
      of revolution (the normal has no e_theta component: pressure has
      no lever arm about the axis).
 (ii) ROTATING PATTERN: with p = f(x, theta - Omega t),
          F_perp(t) = 2pi e^{i Omega t} Int_x R(x) conj(c_1(x)) dx,
          M_perp(t) = 2pi i e^{i Omega t} Int_x R(x)(x + R R')
                      conj(c_1(x)) dx:
      both are vectors of CONSTANT MODULUS rotating rigidly at the
      pattern rate Omega; the axial resultant F_x is CONSTANT in time
      (the [T-T0] companion statement, reproved here in the restricted
      wall-trace setting).
 (iii) n-FOLD NULL (the user's question, answered): if the pattern has
      n identical, equally spaced, co-rotating waves — i.e.
      f(x, phi + 2pi/n) = f(x, phi) — then c_m = 0 unless n | m; for
      n >= 2 this kills the m = +-1 line, hence
          F_perp(t) == 0  and  M_perp(t) == 0   IDENTICALLY IN t,
      and LOCALLY IN x: the transverse load DENSITY per unit axial
      length vanishes at every station — no side force, no shear, no
      bending moment at any cross-section, at every instant. (Not an
      average statement: an exact instantaneous null.)
 (iv) n = 1: the side load does NOT vanish pointwise: it is the
      rotating constant-modulus vector of (ii), with
      |F_perp| = 2pi |Int_x R conj(c_1) dx| set by the first azimuthal
      harmonic of the trace. Its time average over any whole number of
      laps is zero, but its magnitude never decays: the honest
      engineering summary is "constant-modulus load rotating at
      Omega" (bearing/gimbal duty), NEVER "zero on average".

PROOF.
(i) Parameterize S by (x, theta): position r_pos = x e_x + R(x) e_r,
e_r = (0, cos theta, sin theta). The outward-from-fluid normal times
the area element is (e_r - R' e_x) R dtheta dx (fluid inside; the
overall sign is a convention that cancels from every claim). Hence
dF = p R (e_r - R' e_x) dtheta dx. The transverse part of e_x is
zero and the transverse part of e_r is (cos theta, sin theta) ~
e^{i theta}: F_perp integrates p against R(x) e^{i theta} — a pure
first-harmonic azimuthal kernel; F_x integrates p against
-R R' — azimuthally constant (m = 0). For the moment:
r_pos x e_r = x (e_x x e_r) = x e_theta and r_pos x e_x =
R (e_r x e_x) = -R e_theta, so dM = p R (x + R R') e_theta dtheta dx
with e_theta = (0, -sin theta, cos theta), whose transverse
combination is -sin theta + i cos theta = i e^{i theta} (again pure
m = 1) and whose axial component is 0 — proving M_x == 0. Annular
faces (normal +-e_x): no transverse force; moment kernel
r_pos x e_x = -rho e_theta, same m = 1 form. Fubini applies by H-SL2.
(ii) Insert the expansion: Int_0^{2pi} e^{i m (theta - Omega t)}
e^{i theta} dtheta = 2pi delta_{m,-1} e^{i Omega t}; only c_{-1} =
conj(c_1) survives, carrying the factor e^{i Omega t}. Constancy of
F_x: the m = 0 line carries e^{-i 0 Omega t} = 1.
(iii) 2pi/n-periodicity forces c_m Int-orthogonality onto multiples
of n: c_m = e^{2pi i m/n} c_m, so c_m = 0 unless m ≡ 0 (mod n). For
n >= 2, m = -1 is not a multiple of n, so the (ii) integrals vanish —
and already the inner theta-integral vanishes at EACH x, giving the
local (density) form.
(iv) Immediate from (ii). QED.

Remark (shear loads). The same selection rule applies componentwise
to any ROTATING-PATTERN surface traction field (viscous shear
included): the transverse resultant of any trace t(x, theta - Omega t)
picks only its m = 1 azimuthal line, by the identical orthogonality
computation. What changes is only the geometric kernel (shear has an
e_theta component, so M_x need not vanish — swirl friction can torque
the wall). This remark is stated for scope honesty; the carrier
verifies the pressure case of record.

------------------------------------------------------------------------------
## 3. Breakage channels (what the null does NOT cover — falsifier map)

The n >= 2 null is a property of IDENTICAL, EQUALLY SPACED,
CO-ROTATING waves — exactly the pure-periodic single-mode class of
[DIR-PERIODIC]. Each departure re-opens the m = 1 line:

 B1 COUNTER-ROTATING ADMIXTURE: p = f+(x, theta - Omega t) +
    f-(x, theta + Omega t) gives F_perp(t) = A e^{i Omega t} +
    B e^{-i Omega t}: an ELLIPTICAL orbit, modulus pulsating at
    2 Omega — nonzero even with "two waves". (Carrier rejector R1.)
 B2 NON-IDENTICAL or UNEQUALLY SPACED waves: c_{+-1} != 0
    generically — e.g. two co-rotating waves of amplitudes 1 and
    1.3 produce a rotating side load of constant modulus. (R2.)
 B3 MODE TRANSITIONS / DRIFT: Omega(t) drift chirps the load;
    n -> n' transitions pass through transient states with full
    azimuthal spectra — side-load SPIKES during mode hopping are
    consistent with (indeed predicted by) the lemma's breakage map.
 B4 ELASTIC / NON-AXISYMMETRIC WALL: H-SL1 fails (the geometric
    kernel acquires other harmonics).

These channels are precisely the impurity channels the T0
thrust-flatness monitor targets (D6 90-days item 5-bis): a measured
side load on a nominally n >= 2 engine is a MODE-IMPURITY DETECTOR
with a theorem behind it.

------------------------------------------------------------------------------
## 4. Disposition of record (c-slot vs secondary output)

DECISION (S15, dated 2026-08-05): the side load enters the program as
a DECLARED SECONDARY OUTPUT, not (now) as a slot in the constraint
vector c of (P) (M0 D2.6). Grounds:

 (a) Inside the certified data scope ([DIR-PERIODIC], n >= 2 pure
     rotating wave) the constraint |F_perp| <= c_SL is inactive BY
     THEOREM — identically zero load, structurally zero multiplier:
     a c-slot would add bookkeeping and one more hypothesis surface
     with zero marginal-value information (against campaign axis B).
 (b) The rung-2 certified machinery resolves axisymmetric per-phase
     states (m = 0); the m = 1 wall trace lives in the D2 azimuthal
     residual channel — a c-slot the state solver cannot evaluate or
     differentiate would be a phantom constraint.

Secondary output, two declared pieces:
 (i)  DATA-LEVEL (available now): the m = 1 azimuthal content of the
      interface trace on Gamma_d = the lemma's impurity metric; it
      rides the T0 flatness monitor's harmonic-decay audit (D6 item
      5-bis) at zero extra cost — the monitor's m = 1 line IS the
      side-load channel.
 (ii) DESIGN-LEVEL, n = 1 (IOU, named): |F_perp| from the (ii)
      formula requires the WALL trace, i.e. a rung-3a field (B-lite
      helical march, [S-BLITE]); until that carrier exists the
      Verdict reports the declared IOU, never a number (R5).

UPGRADE PATH (declared, so the disposition absorbs future work
without changing form): if n = 1 designs enter scope, or when the A6
robust layer prices mode-transition transients, the side load enters
c as a CVaR constraint over the mode measure — this connects to the
roads-atlas "side-load CVaR disposition" residue item (D8 §8
residue; second-lens verified 2026-08-05 — connection of record; the
CVaR c-slot itself remains the declared A6 upgrade path, not a
current constraint).

------------------------------------------------------------------------------
## 5. Relation to the corpus

- [T-T0] proves axial-resultant constancy through EVERY axisymmetric
  surface from the full rotating-pattern FIELD; T-SLRW is its
  transverse companion at the wall-trace level: axial line m = 0
  (constant), transverse line m = 1 (selection rule). Neither implies
  the other; together they classify all six rigid-load resultants of
  a rotating pattern on a surface of revolution.
- The M_x == 0 corollary sharpens the physical reading of swirl
  torque: on an axisymmetric wall only SHEAR can torque the engine —
  pressure contouring cannot (relevant to the N6 free-vortex swirl
  discussion [T-N6-2]).
- Hypothesis-minimization exhibit (axis B): two hypotheses, both
  falsifiable, no closure, no state equations — the strongest rigor
  class in the corpus per hypothesis spent.

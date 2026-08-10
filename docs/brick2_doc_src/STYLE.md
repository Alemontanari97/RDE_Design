# Rework contract for the A1 Brick-2 document (2026-08-07)

Owner directive: *"It has to be very clear and also do not assume
anything to be known. Images must feature axis variables that are
clear and deeply connected to physics and how the program works."*

## 1. The reader we are writing for

An engineer or scientist who is **new to all of it**: new to nozzle
gasdynamics, new to the method of characteristics, new to
optimization and adjoints, new to rotating detonation engines, new
to this program's registry and vocabulary. They are technically
literate (calculus, basic fluid mechanics) but they have **not**
read the theory corpus, have never heard of GENO, Rao, TOC, plug
nozzles, "cycle phases", or "rejectors".

Consequence: **every term is defined at its first use, in the text,
in one clause.** If a sentence cannot be understood by that reader
without looking something up, it is wrong and must be rewritten.

## 2. Hard rules

1. **Define before use.** No symbol, acronym, or piece of jargon
   appears before its plain-language definition. First uses look
   like: "the *area ratio* $\varepsilon$ --- the exit area divided
   by the throat area, the single number that says how much the
   nozzle expands the gas".
2. **No registry tags as explanations.** Never explain a concept by
   its corpus label (T3, T7, T-T4, Remark 4.9, C-HT4, N6-2, O3.3,
   C-O33, N-65...). Name the result by what it *says*; the tag may
   appear at most once per chapter as a parenthetical citation for
   traceability: "the collapse theorem for the fixed bell (its T3)".
3. **Numbers are sacred.** Never change, round, or invent a number,
   a PASS count, a file name, a `\label`, or a `\ref`. Results of
   record are quoted from actual runs.
4. **Every chapter is self-contained on entry.** It opens with a
   short plain-language paragraph: what this step adds, why it is
   needed, what the reader should take away. Then, if the chapter
   introduces new concepts, a short "What you need to know first"
   subsection defining them.
5. **Short sentences, active voice, no ornament.** Prefer "the wall
   pressure falls" to "one observes a diminution of wall pressure".
   Keep the existing section skeleton (The question / How it works,
   in full / What was built / Results of record) --- it works.
6. **Captions are self-contained.** Every figure caption must state
   (i) what is plotted on each axis, with units, (ii) what the
   reader should look at, (iii) what it proves or shows about the
   program. A reader who reads only captions must get the story.
7. **Keep the LaTeX conventions**: `\carrier{}` for carrier scripts,
   `\code{}` for code and file names, `\cite{}` keys unchanged,
   `\label`/`\ref` unchanged, `\emph` for first-use terms.

## 3. Notation, defined once (Chapter "Notation and symbols")

Geometry and flow (all SI):
- $x$ axial coordinate [m], $y$ radial coordinate [m]
- $u$ axial velocity, $v$ radial velocity, $q$ flow speed
  magnitude $\sqrt{u^2+v^2}$ [m/s] ($W$ in Rao's papers)
- $\theta = \arctan(v/u)$ flow angle [rad or deg]
- $p$ static pressure [Pa], $\rho$ density [kg/m^3], $T$ temperature
  [K], $c$ speed of sound [m/s], $\gamma$ ratio of specific heats
- $M = q/c$ Mach number; $\alpha$ Mach angle, $\sin\alpha = 1/M$
- $\nu(M)$ Prandtl--Meyer function [rad]
- $C^{+}, C^{-}$ the two characteristic families, at $\theta \pm \alpha$
- $\delta$ = 0 planar / 1 axisymmetric

Machine and operating point:
- $y_t$ throat radius [m]; $r_{tu}, r_{td}$ throat arc radii [m]
- $A_t, A_e$ throat and exit area [m^2]; $\varepsilon = A_e/A_t$
  area ratio [--]
- $P_0, T_0$ chamber (stagnation) pressure [Pa] and temperature [K]
- $p_a$ ambient (back) pressure [Pa]; $p_e, u_e$ exit values
- $\dot m$ mass flow [kg/s]; $L$ wall length [m]
- $J$ thrust objective [N]; $F$ thrust [N]

Cycle (RDE):
- $\xi \in [0,1]$ cycle phase [--]; $\mu$ the phase measure
- $PR = P_0^{\max}/P_0^{\min}$, $TR$ likewise [--]

Plug and swirl:
- $l$ truncation length of the plug [m]; $D$ truncation point
- $\Gamma = y\,w$ circulation [m^2/s]; $w$ azimuthal velocity [m/s]

Optimality instruments:
- $R_{\rm mom}$ momentum-balance residual between the two thrust
  routes [N]
- $R_{\rm corner}$ corner (endpoint) residual [Pa]
- $f_2 = q\cos(\theta-\alpha)/\cos\alpha$ [m/s], Rao's first
  integral, equal to $-\lambda_2$
- $K_{\rm RICH} = 4$ Richardson safety factor [--]

## 4. Figure axis plan (binding: captions must match)

Principle: **dimensional axes with units, always.** A normalized or
"relative" quantity may appear only *in addition to* a dimensional
one, never instead of it. Schematics get coordinate axes too.
Panel titles say what the panel shows physically; annotations name
the program object being illustrated.

| figure | panel axes (final) |
|---|---|
| `fig_moc_primer` | (a) $x$ [m] vs $y$ [m], angles $\theta,\alpha$ marked; (b) same, cell with midpoint; (c) same, columns + foot |
| `fig_nozzle_primer` (NEW) | (a) $x$ [m] vs $y$ [m] nozzle with throat/exit marked; (b) $x$ [m] vs $M$ [--] and $p$ [bar]; (c) $\varepsilon$ [--] vs $p_e$ [bar] with $p_a$ line |
| `fig_contours` | $x$ [m] vs $y$ [m] |
| `fig_jeps` | (a) $\varepsilon$ [--] vs $J$ [MN]; (b) $\varepsilon$ [--] vs $p_e$ [bar] crossing $p_a$ --- the physics of the optimum |
| `fig_grad_ripple` | bump amplitude [m] vs $\mathrm{d}J/\mathrm{d}a$ [N/m] |
| `fig_f2` | (a) $x$ [m] vs $y$ [m]; (b) arclength [m] vs $f_2$ [m/s]; (c) zoom, same units |
| `fig_stationarity` | bump center $x/L$ [--] vs $|\mathrm{d}J/\mathrm{d}a|$ [N/m], log |
| `fig_cycle` | (a,b) $\varepsilon$ [--] vs $J_{\rm cycle}$ [MN] |
| `fig_votes` | phase $\xi$ [--] vs $p_e - p_a$ [bar] |
| `fig_plug`, `fig_plug_before` | (a) $x$ [m] vs $y$ [m]; (b) $x$ [m] vs $p_w$ [bar] |
| `fig_fan_singularity`, `fig_freejet`, `fig_edge_root_geometry`, `fig_plug_lessons` | $x$ [m] vs $y$ [m] with the marked states |
| `fig_plug_cycle` | (a) $x$ [m] vs $p_w$ [bar]; (b) $l$ [m] vs $J$ [kN] (dimensional, deviation from each curve's own max in kN); (c) $\xi$ vs vote [bar] |
| `fig_plug_posing` | (a) $x$ [m] vs $y$ [m]; (b) $\xi$ vs $p_w(x_0)$ [bar] with $p_a$; (c) $l$ [m] number line |
| `fig_geno_twin` | (a) $x$ [m] vs $p_w$ [bar]; (b) $x$ [m] vs $|\Delta q|$ [m/s]; (c) marched length [m] vs $\Delta q$ [m/s] |
| `fig_swirl` | (a) $p$ [bar] and $M$ [--] vs $y$ [m]; (b) $x$ [m] vs $p_w$ [bar]; (c) $y$ [m] vs $w$ [m/s] --- a real plot, not a cartoon |

## 5. Structure of the reworked document

Front matter (new, written by the owner of this rework):
1. Introduction --- the problem, the two ground rules, how to read
2. What a nozzle does, and what "optimal" means --- physics from zero
3. How the solver computes --- the method of characteristics from zero
4. How this program proves things --- derived tolerances, rejectors,
   oracles; plus the notation table

Then the existing engine chapters (rewritten under this contract),
then status, then the appendix of problems met.

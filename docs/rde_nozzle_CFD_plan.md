# The CFD counterpart of the nozzle optimizer — plan, feasibility, critical points

Status: PLAN OF RECORD (S21, 2026-08-09). Nothing here is executed
yet. Every stage below carries a declared gate; a stage whose gate
fails stops the track rather than being worked around.

---

## 1. Why replace the marching solver at all

The method-of-characteristics engine is exact for what it models and
costs seconds. It should not be abandoned casually. The case for a CFD
counterpart rests entirely on things the march *structurally* cannot
represent, and it is worth being precise about which those are,
because each one is a reason and each one is also a risk.

**Rotationality.** The march assumes an irrotational, isentropic,
shock-free supersonic field. A real RDE exhaust arrives with entropy
gradients from the detonation and with vorticity; downstream of any
shock the flow is rotational by Crocco's theorem. The free-vortex
swirl extension reaches the one rotational case that stays integrable;
beyond it the march has nothing to say.

**Viscosity and heat flux.** There is no boundary layer in the march,
so no skin-friction debit, no displacement thickness correcting the
effective contour, and no wall heat flux — the quantity the reference
RDE work resolves with a 15 nm first cell.

**Separation and base flow.** A truncated spike has a base. The march
replaces it with an assumption; the base pressure is where a real
truncated aerospike wins or loses several percent, and it is set by an
unsteady recirculating wake.

**Shocks.** Off-design operation and any over-expansion produce
shocks, internal and in the plume. The march's free-jet edge is a
kinematic boundary on which `p = p_a`; a real one is a shear layer
with a barrel shock structure.

**The cycle.** An RDE feeds its nozzle a periodically varying total
state. The cycle layer treats this quasi-steadily. Whether that is
legitimate at the real frequency is an open physical question, and
only an unsteady solver can answer it.

**A caution on framing.** The natural conclusion is not that CFD
*replaces* the march but that the march becomes the **oracle**. In the
inviscid, shock-free, irrotational regime the march is exact and the
CFD is an approximation of it; that overlap is the only region where
the CFD optimizer can be *verified* rather than merely run. A CFD
optimizer with no verified regime is an opinion generator. The plan
below is therefore organized so that the overlap is exploited first
and hardest.

---

## 2. What the CFD optimizer must reproduce before it is trusted

The existing program already fixes every element of the optimization
except the flow solver, and all of them transfer unchanged:

| element | existing | in the CFD counterpart |
|---|---|---|
| shape basis | clamped-left natural cubic spline, frozen knots ([X-TOCV], [X-PSPL]) | **the same spline**, driving mesh deformation |
| objective | ambient-gauge axial thrust | **the same functional**, integrated on the CFD wall |
| constraints | mass by construction, length by knot placement | mass by the inlet condition, length by the deformation box |
| gradient | reverse-AD adjoint through a frozen schedule | discrete adjoint of the CFD residual |
| driver | segmented trust-region SQP | the same, or the solver's own |
| verification | derived bands, ladders, rejectors | unchanged, and now including the march itself |

Keeping the basis and the objective *identical* is not tidiness. It is
the only way the two optimizers can be compared, and this session
supplied the cautionary case: a constraint set with one quadrature and
graded with another produced a 7e-5 residue that looked like a
physical defect for several sessions and was an instrument mismatch.
Comparing a CFD thrust to a march thrust computed in a different gauge
would reproduce that error at a much larger scale.

---

## 3. The staged plan

Each stage has a **gate**. Stages are ordered so the cheapest
falsification comes first.

### P0 — Instruments, no CFD required *(days; no dependency)*

Write the objective and the comparison harness against a *field*
rather than against a solver: a reader that takes any axisymmetric
field (march output or CFD output) and returns thrust by the two
independent routes the program already uses — the wall pressure
integral and the momentum flux through a control surface — in the
ambient gauge, on a common basis.

This is `a1_flux_meter` generalized, and it is the piece that lets
every later stage be graded. It also discharges an item already open
on the march side (re-plumbing the configuration comparison's three
unclosed checks onto the meter).

**Gate P0**: the two routes agree on a march field to the band the
march itself supports, and the meter reproduces `a1_config_compare`'s
recorded numbers. If the meter cannot grade the march, it cannot grade
CFD.

### P1 — Solver in place *(days to weeks; the only hard dependency)*

Build SU2 with its discrete-adjoint variant. Rationale: it is the only
mature open code that ships *all four* of {compressible RANS,
axisymmetric, discrete adjoint by operator overloading, shape
deformation with an optimization driver}. OpenFOAM's adjoint solvers
are incompressible-leaning; writing our own adjoint is a multi-month
project that duplicates SU2's.

Known blocker (recorded earlier): SU2 is not installed here and the
build dependencies — meson, ninja, swig — are absent. The AD build is
the heavier one (CoDiPack-based, long compile, large memory).

**Gate P1**: SU2 and SU2 with AD both build; a shipped verification
case reproduces its published result.

### P2 — Primal bridge: does inviscid CFD agree with the march? *(the first real test)*

Run the *same nozzle* — the certified bell of the referee chapter, and
the plug of [X-PSPL] — as axisymmetric Euler in SU2, and compare
against the march: wall pressure distribution station by station, exit
Mach, mass flow, and thrust by both routes.

This is the same confrontation already performed against the
independent Fortran code, where agreement was three to four digits, so
the standard is known and the tolerance is not invented: the CFD must
enter the *same* band, or its disagreement must be explained by a
named mechanism (mesh resolution, far-field placement, the free
boundary treatment).

**Gate P2**: wall pressure within the band the march's own refinement
supports, on a *mesh-refined* ladder — not a single mesh. Thrust
agreement to the same order. **If this fails, everything downstream is
meaningless and the track stops here.**

### P3 — Gradient bridge: is the CFD adjoint the same derivative? *(the decisive stage)*

Parameterize the CFD wall with the *same* spline knots, deform the
mesh from them, and compare three derivatives of the same objective
with respect to the same design vector:

1. the march's reverse-AD adjoint (certified, and the reference),
2. SU2's discrete adjoint,
3. central finite differences on the CFD primal — **on a ladder of
   steps**, per this session's lesson, since a shock-capturing scheme
   is at best piecewise smooth and its finite differences will carry
   noise that does not fall as `h^2`.

**Gate P3**: (2) agrees with (1) within the band (3)'s scatter
supports, in the inviscid shock-free case where (1) is exact. A
disagreement here is diagnostic and must be attributed before
proceeding — mesh-deformation chain rule, objective definition, or a
genuinely different derivative.

### P4 — The zero-gain oracle *(the killer test)*

Run the CFD shape optimization, same basis, same constraints, starting
from the march's optimum, in the inviscid shock-free regime.

**The correct answer is that it finds nothing.** The march's optimum
*is* the optimum there; the march is exact. A CFD optimizer that
reports a meaningful gain over it has a bug — in the objective, the
constraint handling, the mesh deformation, or the gradient — and the
size of the spurious gain measures the size of the bug.

**Gate P4**: the recovered gain is below the CFD's own discretization
band, and the optimizer's design stays within the band of the march
optimum. This is the single most valuable test in the plan, and it is
cheap once P3 passes.

### P5 — Viscous *(where CFD starts earning its cost)*

Turn on RANS. Now measure what the march could never see: the skin
friction debit, the displacement-thickness correction to the effective
contour, and whether the *optimal shape itself* moves once a boundary
layer is present.

Declare in advance whether the adjoint is taken with the turbulence
model frozen or differentiated. Frozen turbulence is the common
practice and is often adequate for shape gradients; it is also a known
source of gradient error in separated flow. Declare it, and measure it
against finite differences once.

**Gate P5**: the viscous optimum reduces to the inviscid one as the
Reynolds number rises; the frozen-turbulence gradient is validated
against finite differences on at least one design.

### P6 — The truncated spike's base *(the hard one)*

The base region is separated and unsteady. Steady RANS will either
fail to converge or converge to something that is not the time mean.

**This is the plan's principal scientific risk** and it is treated
separately in §4.

### P7 — The cycle *(research, not engineering)*

Feed the periodic RDE total state. Two routes: quasi-steady sampling
(cheap, and it *tests* the cycle layer's assumption rather than
assuming it), or URANS with a time-averaged objective and an unsteady
adjoint (expensive, and subject to §4).

**Gate P7**: quasi-steady sampling first, and its result compared
against the existing cycle layer. Only if they disagree is the
unsteady adjoint justified.

---

## 4. Critical points

### 4.1 The unsteady adjoint diverges — the fundamental one

For any flow with positive Lyapunov exponents — separated base flow,
any resolved turbulence, the RDE cycle — the adjoint solution grows
exponentially backwards in time. This is not an implementation defect;
it is the correct behaviour of the adjoint of a chaotic system, and it
makes long-horizon unsteady sensitivities meaningless.

Consequences: P6 and P7 cannot simply "run the adjoint longer".
Options, in increasing cost: short windowed adjoints with the horizon
chosen by measuring the growth rate; a steady RANS treatment with the
base pressure supplied by a model or correlation; or least-squares
shadowing, which is correct but multiplies the cost by another large
factor.

**Recommendation**: do not plan an unsteady adjoint. Plan steady
optimization with an unsteady *verification*, and treat base pressure
as a modelled parameter whose sensitivity is measured by a sweep
rather than by an adjoint.

### 4.2 Shocks make the gradient mesh- and limiter-dependent

A discrete adjoint through a shock-capturing scheme is a well-defined
object, but the object depends on the limiter and the mesh, and it
does not converge to the continuous sensitivity as the mesh refines in
the way a smooth problem does.

**Mitigation**: shock-free designs first (this also matches the
existing route decision on the analytical side). Verify P3 and P4
strictly in the shock-free regime. When shocks are admitted, report
the gradient's mesh dependence explicitly as a measured quantity
rather than assuming it away.

### 4.3 The objective must be the same functional, not the same quantity

SU2's built-in force objectives are defined in *its* conventions —
force along a freestream direction, non-dimensionalized by *its*
reference quantities. Thrust for an internal axisymmetric nozzle in an
ambient gauge is not any of them without care. A custom objective is
required, and it must integrate the same thing the march integrates,
in the same gauge, with the same reference state.

This session's lesson applies directly: two correct rules for the same
integral disagree at their common order, and the disagreement presents
as a physical result. Budget real time for this and verify it on a
field where the answer is known.

### 4.4 The free boundary becomes a domain problem

The march's plug exhaust edge is a boundary condition, `p = p_a`,
imposed on a surface the solution finds. CFD has no such surface: it
needs a far-field domain large enough that the plume develops, with
outflow conditions that do not reflect. Domain size and far-field
placement become convergence parameters that must appear in the
refinement ladder, not just cell count.

### 4.5 Mesh deformation is part of the derivative

The chain from spline knots to wall points to volume mesh to residual
is all inside the gradient. Deformation quality degrades as the design
moves, and a mesh that tangles or skews silently corrupts both
objective and gradient. Mesh quality must be a *monitored gate* on
every accepted design, exactly as per-cell Newton certification is on
the march side — the plug optimizer already reverts and shrinks on a
failed certification, and the same discipline transfers.

### 4.6 Cost, and what it buys

A gradient costs one primal plus one adjoint solve, roughly two to
three times a primal. For the *axisymmetric steady* case the mesh is
small — order 10^5 cells — so a solve is minutes on a few cores and a
50-iteration optimization is hours. **This is affordable, and it is
the main positive feasibility finding of this assessment.**

The comparison is nonetheless stark: the march's gradient is a replay
costing seconds. CFD is three to four orders of magnitude more
expensive per design iteration. That is the price of the physics in
§1, and it is why the staging matters — the cheap exact tool should be
used wherever it is valid, and CFD reserved for where it is not.

Three-dimensional or unsteady cases are a different regime entirely
and should not be planned as optimizations until §4.1 is resolved.

### 4.7 Validation debt

The march's numbers are defended by derived bands, ladders and
deliberate rejectors. A CFD result defended by "the residual dropped
six orders" is not in the same evidentiary class. Every gate above
must be graded the way this program grades: on a ladder, against a
band the computation measures itself, with a rejector that must fire.

---

## 5. Recommended order, and the decision point

P0 and P2 are the whole assessment in miniature and can be reached
without committing to the rest: P0 needs no CFD at all, and P2 answers
whether the two solvers describe the same flow. P3 and P4 then decide
whether a CFD *optimizer* is trustworthy.

**Decision point after P4.** If the zero-gain oracle passes, the
machinery is verified and P5 onward is ordinary engineering with a
known cost. If it fails, the failure is diagnostic and cheap, and it
will have been found before any effort was spent on viscous or
unsteady work.

The honest summary of feasibility: **P0-P5 are feasible and
affordable, and P2-P4 are the parts worth doing first because they are
the parts that can fail informatively. P6 and P7 are research, gated
on the adjoint-divergence problem of §4.1, and should not be promised
as deliverables.**

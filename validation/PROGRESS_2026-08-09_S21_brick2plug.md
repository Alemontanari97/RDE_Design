# S21 — Total-order session log (2026-08-09; REBASING THE BRICK-2 PLUG
# LINE ONTO S20, AND GIVING THE SPIKE A SHAPE)

Session: S21, opened by a USER order with two parts: (1) pull the
latest code and compare it against the plug line developed off-branch;
(2) rebase that line onto the pulled commit, graft everything, "arrive
to the spline implementation, test it and ready for commit".

Standing constraints carried in: the RDE input is a STRAIGHT LINE and
its inclination theta_i is a design variable; outward-turning
aerospikes are EXCLUDED by owner directive; GENO is never modified as
an optimizer side effect; nothing is pushed.

---

## Step 1 — The comparison, and the shape of the divergence

The working tree carrying the plug line is NOT a git checkout. The
checkout is `/data10/falco/RDE/RDE_Design` (branch
`rde-nozzle-program`), and it was **145 commits behind**; fetched and
fast-forwarded `2d2fdbc -> ed84f6e`.

FINDING OF RECORD: the two lines **fork at S14**. Both then wrote a
session numbered S15 and they are different sessions — this line went
straight to Brick 2 on 07-28; the upstream line spent S15-S16 on deep
foundations and opened its OWN Brick 2 at S17 on 08-06, closing it at
S18 and running O3.2/O3.3 at S19 and the adaptive knot class at S20.

The work is **disjoint**. Upstream has no plug, aerospike, free-jet,
swirl-march or cycle carrier; this line has none of X-TOCV, X-AKNO,
X-O33B, X-O32, X-THC1, X-SCANM, X-LSG0 or the S15-S16 foundations
bricks. Nothing was duplicated. The lines share exactly one file, the
march X-A1IM, and there the divergence is three hunks: upstream's S18
while-Newton on the certification metric, upstream's S19 `m_stop`
knob, and this line's `wall_u`/`wall_v` export — never committed, and
depended on by five files here.

Two upstream results supersede items this line had listed as open:
X-TOCV is the spline TR-SQP driver this line's status ledger still
called "remaining work", and S19's locus correction (the control
surface is the C+ traced back from the lip and STOPPED at the kernel
boundary, not run to the axis, on which f2 drifts 2.89e-01) applies to
this line's O3.3 carrier. See step 7.

## Step 2 — The graft, and the one merge

Branch `brick2-plug` off `ed84f6e`. 16 carriers, the 79-page document
tree and the S15 handoff log copied in: all pure additions, no
upstream file overwritten.

The single merge is on the march, and it is ADDITIVE ONLY: `wall_u`,
`wall_v` re-exposed on top of upstream's while-Newton and `m_stop`,
both kept intact. G nodes are `[x, y, u, v]` in both lines (verified
against the unit-process return), so the graft reads two components
the march already carries and feeds nothing back into any decision,
residual or state.

`GENO` is an out-of-tree environment fixture and is symlinked, not
committed.

## Step 3 — Was the solver change harmless? MEASURED, not assumed

Upstream's Newton loop now terminates on the per-cell certification
bound instead of a fixed trip count. That sits underneath every number
in this line's document, so it was measured rather than waved through:
regenerating the case that fixes the common basis on both solvers
gives

  mdot        BIT-IDENTICAL (all four area ratios)
  J0/Me/qe/pe/ylip   1e-15 .. 1e-13 relative

i.e. machine precision. The fixed-trip loop was already converging
past the point where the new rule halts. **No recorded number moves.**

## Step 4 — The suites, re-run on the grafted march

Thirteen clean: thrust_functional 8/8, corner_instrument 5/5,
driver_eps 4/4, wall_march 5/5, o33_toc 5/5 (integrals stage),
cycle_layer 5/5, cycle_corner 8/8, freejet_unit 6/6, plug_march 6/6,
plug_cycle 14/14, geno_plug_twin 8/8, swirl_march 9/9,
source_flow_oracle 6/6.

`a1_config_compare` 7/10. NOT a regression, and this was checked
rather than asserted: the pre-rebase tree returns the same three
failures with the same numbers to every printed digit (mass |d|
1.77e+00, momentum closure 1.5849e+06). The three are the descending
plug's mass and momentum closures, already diagnosed as a property of
the last-column meter.

`a1_flux_meter` has no `main()` — it is the instrument module those
checks are to be re-plumbed onto, not a suite. Recorded as such.

`a1_inlet_angle_opt` 4/6 — also identical pre-rebase, and FIXED in
step 6.

## Step 5 — [X-PSPL], the free-form spike

The spike had always been INHERITED: a streamline of the lip fan,
traced rather than chosen. That contour is optimal for the
FULL-LENGTH ideal plug and not for the cut one — the thrust weight
`2*pi*y` rewards pressure held where the spike is still fat, and a
traced contour cannot bias. This is Rao's length-constrained argument
transposed, and the multiplier lambda3 certified in O3.3 is the
shadow price of exactly that constraint.

Built: design vector = spike radius at m frozen knots, last knot at
the length; wall = **the bell engine's own clamped-left natural cubic
spline, imported from X-TOCV rather than reimplemented** (equal shape
freedom on both sides, and X-AKNO applies to this wall unchanged);
mass and length by construction, with the mass constraint decoupling
EXACTLY from the shape dofs because the start line is Cauchy data
upstream of every knot; gradient = reverse-AD adjoint through the
recorded schedule; driver = segmented trust-region SQP carrying the
certification gate.

VERDICT 7/7 PASS. Gain over the streamline at fixed length
**+0.0908%** against a derived band of 0.0094%; |grad| 5.844e+06 ->
1.472e+05 (40x) over seven accepted segments and nine records; final
spike descends 1.4936 -> 0.8330 m and clears the axis. The
certification gate is load-bearing, not decorative: one segment hit a
record with worst residual 2.318 and was reverted.

DECLARED NOT CONVERGED: final |grad| 1.47e5, six knots, one design
point. The gain is a LOWER BOUND, and the document says so.

## Step 6 — Four defects, each of which had produced a confident
## wrong answer

(i) `a1_inlet_angle_opt` SET its mass constraint with one quadrature
and GRADED it with another — trapezoid of the product `rho*u*2*pi*y`
against the march column functional's product of midpoint means. Both
second-order, both correct, differing at their common order by ~7e-5
on 61 rows: an instrument difference presenting as a physical defect,
which no refinement could remove and which a widened band would have
buried. Sizing with the grading functional drops the residue to
1e-15..3e-10. A second failure dissolved with it: one candidate had
been failing certification at worst 6.5 and been read as a marching
limit of that configuration; with the annulus correctly sized it
certifies at 0.05. **4/6 -> 6/6.**

(ii) The new driver adopted every segment endpoint unconditionally and
reported a 0.21% **loss** as the outcome of a maximization. A segment
endpoint is a trial point; added the acceptance test (revert to the
best certified base and shrink).

(iii) With that in place the walk stopped losing but also stopped
improving, oscillating between one good base and two overshoots. The
outer trust radius was being read back from scipy after each segment,
silently overwriting every shrink the outer loop had ordered. The
outer radius is now the outer loop's own property.

(iv) The adjoint was graded against a central difference whose band
was estimated by halving the step once. That assumes the error is
truncation; here it is not, because the replayed march is only
piecewise smooth in the design vector (the topology is frozen, so a
perturbed design can sit fractionally on the wrong side of a decision
the record already made). Measured over five steps the discrepancy
WANDERS instead of falling as h^2 (one node: -197, +61, +1.8, +0.63,
-0.42). The two-point band described nothing and a CORRECT adjoint was
reported as a failure. Band now comes from the ladder's own scatter.

LESSON OF RECORD, three instances in one session (the C-1 knot ratio,
the T-2 two-instrument constraint, the C-2 two-step band): **two
points can measure a difference, but never a rate, and never the
reliability of the instrument that produced them.** In all three the
blame first fell on the object being measured — the basis, the flow,
the adjoint — and in all three the instrument was at fault.

## Step 7 — Documentation

Document rebuilt at **79 pages**: new Chapter 15 (the free-form
spike), a status-ledger section recording which solver the numbers
stand on, two appendix sections (the two-instrument constraint; the
three ways to mismeasure with two points), and the remaining-work list
rewritten — the spline item is discharged, and the O3.3 locus and the
Rao cross-check are entered in its place.

Registry 125 -> 127: **[X-PLUG]** (the plug line as a whole, carrying
its three open checks in its falsifier) and **[X-PSPL]** (the
free-form spike). Claims lint PASS, rejectors proven.

## OPEN, carried forward

1. **O3.3 locus.** This line's terminal characteristic is taken as a
   whole grid column SELECTED BY MINIMISING the very f2 spread the
   check then reports. The measured spread (4.045e-03) shows none of
   the 2.89e-01 pathology S19 found on the run-to-axis locus — GENO
   col 192 carries only 21 valid nodes — so this is a METHODOLOGICAL
   defect, not a demonstrated wrong number. The locus should be fixed
   a priori and stopped at the kernel boundary, per S19.
2. **Rao cross-check.** [X-PSPL] measures its gain against the
   fan streamline, which is the IDEAL contour, not Rao's
   length-constrained optimum. The decisive comparison is GENO's
   RaoPlug (case type 8) posed on mass + LENGTH — both are offered —
   against the spline optimum at the same two constraints. Near
   agreement is expected and would validate both; a spline win would
   mean it found something outside the two-degree-of-freedom Rao
   family, which is the interesting outcome.
3. **Converge [X-PSPL]**: more segments, more knots or adaptive ones,
   and the thrust band re-derived at the carrier's own resolution.
4. **The three open closures** of `a1_config_compare`, to be
   re-plumbed onto `a1_flux_meter`.

## NEXT

Per the user's order closing this session: the documentation is
brought into the base's format (this log, the INDEX row, the registry
entries), and the next work item is a detailed plan for the **CFD
counterpart** of this optimizer — feasibility and critical points.
---

## Step 8 — The referee, posed in our world

Posing GENO's RaoPlug at our mass and length required running it where
it had never been run, and exposed three defects plus an environment
failure. **Attribution was done before any fix**: our S21 edits were
removed entirely and the failure reproduced identically.

- **The 500-step cap and the reference-case collapse are NOT ours.**
  `NMAX_CMINUS = 500` is in committed GENO. The working binary had been
  built with **gfortran 7 + MKL 2024.1**, neither now installed;
  rebuilding with gfortran 12 at the project's `-O3` produces a binary
  that **fails GENO's own reference case** (theta_E scan collapses to
  0.000, M_E unreachable), while `-O0` on the same source reproduces it
  EXACTLY. GENO is optimization-fragile under the current compiler.
- **The NaN is ours.** `mass_match` exists in ZERO base files. Our mass
  accumulator propagated through a non-closing curve and returned
  mdot = NaN, poisoning a bisection and finally the thermo. FIXED:
  increments tested before accumulating; distinct exit reason 4.
- **The wrong-branch root is ours.** With the guard in, the length
  bisection returned a design meeting length exactly while missing mass
  by **63.6%** (corner-terminated branch). FIXED: with mass-match on, a
  sample counts only if it terminated on mass.
- **The cap was a budget, not a limit.** Raised 500 -> 5000. This is
  what unblocked the classical spike for our ambient.

GATE, applied after EVERY edit: GENO's own reference case reproduces
**exactly** (theta_E -8.25001, L 0.93873, deficit -0.0001%, exit 3).
Two independent routes then agree on the repaired path (bisection
theta_E 7.590 / M_E 2.63429 vs outer-Mach 7.604 / 2.63390).

## Step 9 — Rao's answer for our world, and why the L = 2.5 A/B is void

Mass-matched and expanded to OUR ambient: **L = 5.825 m, eps = 5.148,
theta_E = 0.02504 deg**, p_a 7.619e5 (0.06% from target). Only
computable after the cap lift.

**Cross-code agreement**: our step-15 blind sweep, from the divergence
argument alone, put the optimum at theta_E = 0; Rao's construction puts
the perfectly expanded design at 0.025 deg. Our sweep resolves to
+-2 deg, so this is a CONSISTENCY check between independent routes, not
a precision match.

Consequence: our 2.5 m design is a **57% truncation** of the ideal
spike. And the A/B at 2.5 m is VOID — mass+length consume both degrees
of freedom of Rao's family, so ambient becomes an output (1.7e6 vs our
7.6e5); GENO's wall barely tapers there (1.630/1.548/1.636, eps 2.47)
while ours falls to 0.833. Different machines; comparing their thrusts
would measure the expansion mismatch.

## Step 10 — [X-FMTR], the field meter (CFD gate P0)

Two independent routes on any axisymmetric field, solver-agnostic.
**3/4**: cut-independence 0.40%, reproduces the record to 1.0e-04,
gauge-mismatch rejector separates 5.8x. OPEN: the two routes differ by
**0.99%** against a 0.09% band and the difference survives refinement
(0.99 -> 0.97), so ~1% is a property of the FIELD. This sharpens the
old 1.49% last-column figure: inflated by its meter, but not wholly
caused by it.

Its first version reported +6-7% and the first-column wedge was
suspected; `edge_fill` changed NOTHING at any setting. Cause: the
march emits free-boundary points only from x = 2.69, and the lookup
CLAMPED silently below that, so every upstream cut spanned a phantom
outer band. Diagnostic: at a station on the start line, where the
answer is known to 12 digits, the meter read +6.35%. Fixed by refusing
to extrapolate. (An upper mesh envelope was tried and is WRONG: a
vertical cut through a characteristics mesh is sparse, so per-station
max-y under-reports the radius by up to 96%.)

## Step 11 — [X-PSPL]'s headline FALSIFIED by its own new check

C-6 added: derive the thrust band at the CARRIER'S OWN resolution
instead of inheriting step 13's. On 10 knots / 26 segments:

    gain at (K,N)            +0.1302 %
    gain at (2K-1, 2N-1)     +0.0820 %
    band this supports        0.1930 %   <-- LARGER THAN THE GAIN

**The +0.0908% headline is not resolved.** It was quoted against an
inherited band (0.0094%) from a different computation — the same error
this session met three times — and the caveat was written down before
it was tested. The machinery remains verified (adjoint, basis ladder,
mass to 5e-12, rejector); what is not established is that the free-form
spike beats the streamline. Document corrected: ch_spline
§"The gain is not resolved, and how that was found out".

## NOT DONE this session

- O3.3 locus (still selected by minimising the statistic it reports).
- Adaptive knots on the spike ([X-AKNO] applied) — now the FIRST thing
  worth doing, since step 11 says more shape freedom must be bought
  where the contour bends rather than uniformly.

Registry 127 -> 128 ([X-FMTR]); claims lint PASS.

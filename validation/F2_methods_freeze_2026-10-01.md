# F2 methods freeze (2026-10-01)

Plain rules: short sentences, physics before method. One section per method: what it does, the checks that hold it,
their dates, what is open. The code version frozen is the tree of the F2 closing commit. Every date is the check's
last pass on this machine (claims registry, `ondemand` field). "Declared failing" = the check runs, a gate does not
pass, and an open finding owns it.

## 1. The march (the characteristics solution of the nozzle flow)
- What: marches the supersonic flow from the start line along the walls, cell by cell on the two families of
  characteristics; the gas is a table of states (C^1 closure); each phase of the RDE cycle is one steady march.
- Variants of record: uniform inflow (bell, plug, two walls); layered inflow (each streamline keeps its own entropy and
  total enthalpy).
- Checks: X-A1IM (ideal march, 2026-09-30), X-RMAR (layered march, exact layered jet to round-off, 2026-09-30),
  X-TWOP (two walls, 2026-10-01, after the kernel-arc fix), X-PSPL (plug, 2026-09-30).
- Theory half (M0): F2a block (4) CONTACTS (a contact is carried as a steep smooth layer; its error converges with the
  grid) and the X-RMAR statement. Checked: consistent.
- Open: the layered fold margin and the GENO layered twin (PARKED by the owner, finding
  f2-exit:layered-margin-and-geno-layered-twin-parked).

## 2. The gradient (the exact derivative of the thrust)
- What: reverse-mode differentiation of the march replayed on a frozen plan (the decisions of the march fixed), so
  the gradient is exact for the discrete thrust.
- Checks: X-TOCV O3.1 (bell, 2026-09-30), X-O31R (layered march, 9e-8 against a floor of 3e-6, 2026-09-30), X-O31CS.
- Theory half (M0): Lemma B and the O3.1 rows. Checked: consistent.
- Open: the bell objective omits the throat panel; the panel-inclusive objective exists (A1_OBJDOM=A) and its
  gradient is exactly the coded one plus the panel's (X-OBJD F-1, 2026-10-01); the default switch is owned by finding
  variational-driver:objective-omits-throat-panel. The mesh rate of the bell objective is not conclusive (X-O32, owned by
  mesh-amr:observed-order-not-at-band-sites); its first-order negative control now runs and is rejected (2026-10-01).

## 3. The certificates (when a march, and a design, is trusted)
- What: every cell's Newton solution is certified against the cell's own arithmetic floor; a design must stay in the
  class where waves of one family do not cross (no fold), with a margin.
- Checks: X-CDKAT (the cell check discriminates, 2026-09-30); X-MGOV (the margin governor, with the complementarity
  row and the least-squares multipliers, 2026-10-01); the plug and two-wall no-fold class inside X-PSPL and X-TWOP.
- Theory half (M0): F2-B0 block (a certificate is a property of code tree, recorder and environment together).
  Checked: consistent.
- Open: the Hessian check rejects a biased column but not a kink (X-HSYM declared failing, finding
  driver-nonsmooth:hessian-no-rejector); the margin blind to converging waves (finding twowall:shape-margin-blind-to-convergence).

## 4. The monitors of the input data (is the RDE outflow fit to drive a design)
- What: before a family of exhaust states feeds a design: the state is complete and physical, the extraction surface
  is supersonic with margin (admission); the input is one wave turning rigidly and repeating (single wave); the
  surface is axially supersonic in every cell (choking); 12 sectors resolve the cycle (resolution).
- Checks: X-ADMA (passes on the methane family; declared failing on the THOR family: two averaging rules, finding
  data-contract:thor-family-two-averaging-rules), X-SWAV (declared failing on the THOR data: the wave strength wanders
  2 percent turn to turn), X-CHOK (2026-10-01), X-FRES (12 sectors resolve the thrust to 2e-5; declared failing: its
  rejector does not fire on this nearly linear case, finding family-resolution:line-non-discriminating-on-the-methane-case).
- Theory half (M0): F2a block (1)-(2). Checked: consistent.

## 5. The cycle family (the 12 phases of the RDE exhaust)
- What: from the engine specs, the matched detonation cycle (CJ state + exponential blowdown, Stechmann-Heister-
  Harroun), cut into K sectors of equal time; each sector's gas is the equilibrium products at its own stagnation
  state, then frozen.
- Checks: X-CYCF (2026-10-01).
- Theory half (M0): F2a block (3). Checked: consistent.
- Open: the family is a model of the exhaust, not a chamber simulation.

## 6. The judges (how a design is scored, independently of the optimiser)
- What: (i) the tool over the 12 phases; (ii) 2-D Euler CFD of each phase (MOSE_open, certified convergence, levels c
  and f); (iii) 3-D Euler CFD of the whole nozzle in the frame turning with the wave (the RDE flow itself).
- Checks: the paired demonstration `validation/CFD2_paired_demo_2026-10-01.md` (five plugs and one shrouded pair,
  three judges); X-RDET (the tournament on the 12 phases, 2026-10-01).
- Theory half (M0): F2a block (5) (the frozen pictures rank designs; the absolute thrust of a strong cycle is judged in
  the wave frame) and (6) (the base of a wave-frame run is not judged). Checked: consistent; the shrouded pair adds that
  the tool can credit wall undulations that both CFD judges reject (finding twowall:tool-credits-wall-undulations).
- Open: the 3-D far field drains the still air (finding waveframe:far-field-406-drains-outside-air; the fix is in
  MOSE_open, the owner's code).

## What the freeze means
From the F2 closing commit, a change to any method above re-opens its checks (the claims lint ages them) and is
recorded in D6 as a dated note. The open items above are owned; none blocks the F3 plug sector.

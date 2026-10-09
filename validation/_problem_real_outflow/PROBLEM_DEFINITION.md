# Phase-aware nozzle design on the real RDE outflow: problem definition

2026-10-09. Decided by the owner (section 9) and committed as the protocol of the real-outflow campaign (phase F3.TWIN, census
R47). The open items O1-O4 of section 9 are fixed in this file, dated, before the first walk. No run yet. Every measured number
is reproduced by `tools/run_all.sh` (outputs in `out/`).

## 0. Terms (each word below is used only in this sense)
- STATION: the plane at a given distance x from the injector plate (Q2D's x) where the nozzle begins. Two stations: 7.5 and
  12.5 mm.
- ROW: the Q2D run portata_HP (premixed H2/O2, 241 kg/m2/s), its mean field at the station over one wave period: 528 samples in
  time, psi = the fraction of the period elapsed since the detonation front passed x = 1 mm (the alignment of the Q2D
  snapshots). At 7.5 mm the file `validation/_q2d_hp_inflow/portata_HP_x07.5mm_row.npz`; at 12.5 mm the cell x = 12.49 mm of
  `portata_HP_aligned_field.npz`, cut as the generator cut its rows (checked at 7.5 mm: equal to 6e-8). The row is applied
  uniformly across the annulus gap (Q2D has no radial dimension).
- AXIAL MACH: Mx = u / a, u the axial velocity, a = sqrt(gamma R T) frozen (gamma and R of the sample's composition).
- AXIALLY SUBSONIC: Mx < 1.02 (X-CHOK's line: the data's own uncertainty in Mach).
- P0, T0: total pressure and temperature of the axial motion with the sample's constant gamma:
  T0 = T (1 + (gamma - 1) Mx^2 / 2), P0 = p (T0 / T)^(gamma / (gamma - 1)). The azimuthal velocity (swirl) is never included.
- PHASE: one of K sectors of equal duration T/K; phase k covers psi in [k/K, (k+1)/K).
- REAL PHASE: a phase whose state by C4 (section 3) has Mx >= 1.02. SURROGATE PHASE: a phase replaced by C5.
- THRUST F: newtons, the whole annulus (inner radius 53.85 mm, outer 68.00 mm at the station): the inlet term, the integral of
  (p - p_a + rho u^2) over the station, plus the pressure (p - p_a) on the plug and on the cowl's inner wall, projected on the
  axis. The base and the cowl's outer skin are excluded.
- SHAPE VOTE of a part of the cycle: its share of time x P0. Why: a phase starting uniform at Mach M with constant gamma has a
  Mach field that depends only on (M, gamma, walls), so F = P0 a(M, gamma; walls) - p_a b(walls) and its wall gradient is
  P0 grad a - p_a grad b. P0 is the exact weight of the phase in the shape gradient when M and gamma are common and nothing
  depends on p_a/P0 (no free jet boundary, no separation criterion, no lip margin); otherwise it is the leading weight.
- IDEAL EXHAUST SPEED: the mass average over the period of each sample's speed after an isentropic expansion (its constant
  gamma) from its P0, T0 to p_a.
- GRID BAND: the change of J and of the walls of a landing under one doubling of the march grid.

## 1. Question
Does a nozzle designed with the phases of the real RDE outflow give more cycle-averaged thrust than one designed on a mean
state, with the same hardware, constraints and judges? Designs come from the SQP on the march only; the 3-D CFD is the final
validation, never part of the design chain (owner 2026-10-09).

## 2. What the data say (measured)
| station | axially supersonic | axially subsonic: mass / shape vote | of which behind the front (1) | ideal exhaust speed 0.5 bar / 1 atm | P0 ratio strongest / weakest of 12 phases |
|---|---|---|---|---|---|
| 7.5 mm | 40 % of the period | 36 % / 32.4 % | 7.6 % (Mx 0.67-0.98, P0 7.7-10.5 bar) | 2784 / 2420 m/s | 8.5 |
| 12.5 mm | 84 % | 11 % / 10.0 % | 4.9 % (Mx 0.83-1.0, P0 7-10 bar) | 2778 / 2410 m/s | 5.8 |

Sources: `out/q2d_station_tradeoff.txt`, `out/front_structure.txt`. (1) a high-pressure, axially subsonic slice behind the
oblique shock (7.5 mm: psi 0-0.06; 12.5 mm: psi 0.08-0.15); the other subsonic gas is late in the cycle and at low pressure
(P0 1.7-4.2 bar at 7.5 mm; Mx 0.99-1.02 at 12.5 mm). The axial momentum flux is 6.524 bar at every station. A constant-area
chamber never becomes axially supersonic in every phase (smallest Mx 0.89 at 19.5 mm, `out/q2d_axial_mach.txt`): axially
subsonic phases are inevitable at any station.

## 3. The convention (owner 2026-10-09: simplified, written down)
- C1 Data: the row at the station; its content hash is printed in every verdict.
- C2 Each sample's state: p, T, u, gamma, R (C1); the swirl is dropped.
- C3 K = 24 phases (the check: 48), equal duration, phase 0 from psi = 0.
- C4 Each phase's state: the uniform (p, T, u) that carries exactly the phase's time-mean mass flux <rho u>, axial momentum flux
  <p + rho u^2> and mass-weighted total enthalpy <rho u h0>/<rho u> (h0 = cp T + u^2/2); gamma and R mass-weighted; the root
  on the supersonic branch when the phase's mass-weighted Mx is >= 1, otherwise the subsonic one (the conservation of Cumpsty
  and Horlock, J. Turbomach. 128(1), 2006, applied phase by phase; the root exists for every phase at both stations for
  K = 1, 6, 12, 24 and 48). Its P0, T0 and Mx become the carrier's family entry (w = 1/K, gamma, R, T0, P0, M = Mx).
- C5 A phase whose C4 state has Mx < 1.02 enters with M = 1.02 and its own P0 and T0 (choked at the station: the choking
  closure O3 of the problem book, the sonic family I3 of M0).
- C6 The mean state = C4 with K = 1: at 7.5 mm Mx 1.338, P0 5.566 bar, T0 3524 K; at 12.5 mm Mx 1.316, P0 5.523 bar,
  T0 3557 K (both supersonic: C5 does not apply).

| station | surrogate phases, K = 12 / 24 / 48 | their mass / shape vote at K = 24 | cycle mass, momentum against the row (K = 24) | time-mean P0 |
|---|---|---|---|---|
| 7.5 mm | 6 / 14 / 28 | 34 % / 30 % | +1.0 %, +0.45 % | kept within 0.2 % |
| 12.5 mm | 1 / 3 / 7 | 5 % / 5 % | +0.0 %, +0.0 % (+0.08 % at K = 48) | kept within 0.2 % |

Sources: `out/convention_sonic.txt`, `out/convention_sonic_12.5mm.txt`. The changes of mass and momentum are the same for every
design (they shift the inlet term only).
Declared limit (M0 requires the closure declared before the run, MASTER:1520): in the tool the subsonic gas does not feel the
nozzle; in reality the nozzle feeds back into the chamber through it, and the strong phases push it through in 3-D (in the plug
study's 3-D runs every phase is supersonic 6-11 mm into the nozzle, `out/cfd_axial_mach_vertical.txt`). Only the CFD measures
this.

## 4. The design problem (identical for the arms P and M)
1. Hardware: the annulus at the station (53.85 to 68.00 mm); the chamber upstream is not designed.
2. Start: every phase on the vertical line at the station, uniform across the gap and axial (the carrier as revalidated).
3. Design variables, the same for every contender (owner 2026-10-09, O1 and O2): the injection angle beta of the internal
   nozzle, and the plug's knot heights downstream of the lip (the knots as validated). At each beta the internal nozzle is the
   NON-REFLECTING construction: the hub turns to beta on a short arc and goes on as a straight cone at beta; the cowl is the
   streamline of the field that hub makes alone, ended where the arc's last wave lands on it; the lip and the state delivered
   there are the construction's. The cowl is not optimised by anyone (Rao cannot); it follows beta. The plug's knots are
   offsets carried by the cone at beta; the knots under the cowl stay on the cone (the same freedoms as Rao: A-INLET's cone
   pair). The construction is non-reflecting for one inflow state only: the state it is built on is open item O2b; the knot
   stations, open item O2c, are fixed when the family is built. Tool: the wrapper `validation/twowall_inlet_family.py`
   (beta as a coordinate, a1_twowall.py not edited) and the family builder of the plug study, both written before the
   revalidation and never committed: committed and re-gated with today's code before use (section 7).
4. Constraints: the plug ends at L = 58.45 mm from the station; the lip is the construction's at beta; the base is cut at L with
   p_b = p_a and not judged; p_a = 50 000 Pa; every march certified (certificate <= 1, with the default Newton rescue); a
   landing is quotable only with its worst certificate <= 1/K_RICH = 0.25 (amendment A-1).
5. Veto (the class), the same set for P and M: in every REAL phase of the K-phase family, no fold of characteristics in region
   RC (the cells on the C- lines the plug wall consumes before its tip, and the channel between the walls), no over-expanded
   lip (the lip margin), the Summerfield separation criterion. The surrogate phases are not constrained; their folds and lip
   shocks are reported. TOOL CHANGE: today the carrier reads the class in every phase or in the reference state only
   (TWOP_MU_CLASS = all or ref); the veto on a subset of phases needs a per-phase mask that, with every phase selected,
   reproduces today's class bit for bit; it passes a unit test and the quick regression (X-RVQCK) before any walk.
6. Objective: P maximises J = sum_k w_k F_k over the K phases (w_k = 1/K: each phase's share of the period); M maximises F of
   the C6 state. Not mass weights (F_k already carries the phase's mass); not each phase's own C_F (it would give the weak
   phases the vote of the strong ones). The carrier computes this J (`a1_twowall.py` `_J_gen`: one common normalisation).
7. Number of phases: K = 24. Accepted if the landing at K = 48 lies within the grid band of the K = 24 landing (walls and J);
   rejector: a 3-phase landing must lie outside it (if it does not, the test cannot tell coarse from fine, and that is stated).
   Twelve equal phases do not resolve the front (the slice of note 1 shares one phase with the jump to Mx 1.57).
8. Gradient diagnostics, at the start and at the landing: each phase's share of the cycle gradient; the angle between the
   gradients of P and M (an angle near zero at the start predicts that the two walks land on the same design).

## 5. Arms, references, and the same problem
- P and M solve the same problem (4.1 to 4.5, the same basis, starts, driver, budget and stopping rule) and differ only in the
  objective (4.6).
- Rao (GENO) is the COMPETITOR (owner 2026-10-09): Rao's plug on the construction's lip, designed on the C6 mean state (the
  same problem as M); its two degrees of freedom, beta and the base pressure p_b, are set so that the plug ends at L and passes
  the engine's mass ("Rao with the length given and the angle free", A-INLET of the twin protocol). M may beat it only where
  the length or the construction bind, and every such gain is explained with the equations (the revalidation's rule).
- Classical controls: Rao's plug on the mean states C (Liu), E (Cumpsty-Horlock), F (Kaemming-Paxson), each in its paper's
  convention (the plug study's practice). They are references (what a classical designer delivers); the same judges evaluate
  them.
- Identity card, content-hashed in every verdict: row, convention (tool hash, K), station, the construction's family (its file,
  the state it is built on), w_beta's scale, the knot stations and which are frozen, L, base rule, veto
  (definition and the list of real phases), certificate, ambient, gas tables, grid, driver, starts, budget, stopping rule, code
  commit. Between P and M only the objective may differ. Rejector: a pair with one item changed (L by 0.1 mm; one knot freed)
  must be refused.
- Cross-evaluation: each landing is evaluated on both objectives; P's landing must not lose to M's on J, nor M's to P's on F of
  the C6 state. A violation means a walk did not converge or the problems differ: stop and explain with the equations.
- A second optimiser, if used, calls the same evaluator (the same posing object, march, J, veto, K, grid, starts) and returns
  the bit-identical J and constraint values on one shared design before any walk. Only the step rule may differ.

## 6. Readings and judges
- R-a (tool, at each station): the landing's sensitivity to the convention: C5 as written; C5 keeping the phase's mass instead
  of its P0; and a diagnostic with J over the real phases only (their weights unchanged; never a design). First compared on the
  start design (J and the gradient's direction); a full walk only for a variant that moves them beyond the grid band.
- R-b: the tool's J against the CFD's thrust on the same landing, both with the thrust of section 0; their inlet terms differ
  by the convention's declared effect, so the pressure on the walls is compared as well. The convention's error weighs more at
  7.5 mm: the difference of the two stations' gaps estimates it.
- R-c: the gain P - M at each station, by the tool and by the CFD. The same sign and size at both stations means the conclusion
  does not depend on the convention. The competitor is read the same way: P - R and M - R (R = Rao, section 5).
- The 3-D runs: the plug study's set-up (MOSE_open f4498666, Euler, frozen ONERA-7, a 45-degree sector holding one wave, the
  row with its swirl as the inflow: per-face states in the wave frame, the 410 table in the laboratory frame). Each landing runs
  in the wave frame until three dumps (400, 450, 500 us) agree; the thrust is read over that window. One laboratory-frame twin
  at 12.5 mm. The CFD margin is measured before the campaign on a case already run (O4, O4a). Minimum 8 runs (P, M and R at
  both stations, and the twin), 14 with the classical controls; about 3-4 hours each.

## 7. Order of work (each step on the owner's go)
1. The open items O2b, O2c and O4a fixed; the CFD margin run (O4). The wrapper and the family builder committed and
   re-gated with today's code (the quick regression first); the families of the construction built at both stations; Rao's
   members on them (GENO, s3).
2. The veto mask (4.5) with its unit test; the quick regression.
3. The families written from the rows by the convention's tool (`tools/convention_sonic.py` extended to write them), with its
   identity tests and a rejector (a subsonic phase left without C5 must be refused by X-ADMA's A-2); X-ADMA on the families.
4. At the start designs, at both stations: certificates, veto feasibility, gradient shares and angles, K 24 against 48, R-a.
5. The walks P and M and the controls; fold census; the K = 48 check; cross-evaluation.
6. The 3-D runs; R-b and R-c.

## 8. Not used (recorded)
- `_q2d_hp_inflow/*_family_K*.json`: T0 and P0 with the total Mach but M axial (+11 % mass and momentum if fed to the tool,
  `out/family_contract.txt`). C1-C6 build the phases from the rows instead.
- A start plane inside the nozzle where every phase is supersonic: it would put the CFD in the design chain.

## 9. Decisions and open items
Decided by the owner on 2026-10-09:
- The optimisation does not depend on the CFD; a simplified, written convention for the subsonic phases ("le fasi subsoniche
  sono inevitabili ... tenere ben nota la convenzione ... siccome mi aspetto che le fasi a pressione e mach piu' alto siano le
  piu' rilevanti").
- Both stations; the effect of the convention certified by 3-D runs ("tenere entrambe le sezioni ... certificato da apposite
  run 3D").
- L = 58.45 mm from each station ("usiamo a").
- On the recommendations ("ok"): the entrance free from the station (made precise by O2 below: the injection angle free, the
  cowl its non-reflecting construction), 0.5 bar, the controls C/E/F, the veto on the real phases, the lip point fixed
  (superseded by O2: the lip follows the angle), the convention C1-C6 with K = 24, a protocol of its own; the problem definition unambiguous rather than
  short ("non deve essere necessariamente corta, basta che sia senza equivoci").
Decided by the owner on 2026-10-09, late evening:
- O2: "inizialmente avremo una cowl data siccome rao, che sara' il nostro competitor, non ha modi di ottimizzarla come sqp":
  the cowl is given; Rao is the competitor.
- O3: "le soglie me le presenterai ed io decidero' l'importanza del guadagno": no thresholds set in advance; every difference
  is presented with its measured bands (the tool's grid and K bands, the CFD margin) and the owner judges its importance.
- O4: "la misura dell'errore CFD la possiamo gia' fare girando una versione di un caso che abbiamo gia' girato e vedendo il
  margine": the CFD margin from a refined re-run of a case already run, before the campaign.
- O1: "teniamo per ora i nodi come abbiamo validato, questa cosa dei [modi] la teniamo in stiva siccome l'idea mi piace": the
  walks move knot heights as validated (the wall through them is a cubic spline); the smoothness rule (owner 2026-10-01) is a
  check on every landing (the wall angle must not oscillate along x). PARKED, not used now: a modal basis (each coordinate
  bends the whole wall in a smooth pattern, so the wall cannot undulate).
- O2, refined: "siccome rao necessita di due DOF per realizzare lunghezza e pb in realta' l'angolo del mozzo dovrebbe essere
  parte dell'ottimizzazione e poi venir riconnesso allo stato uscente dal nozzle con una cowl non riflettente": the injection
  angle is a design coordinate of every contender, the cowl the non-reflecting construction at that angle (section 4.3).
Open, to be fixed before the first walk:
- O2b the state the construction is built on. Proposed: the C6 mean state (the state of M and of Rao), at each station.
- O2c the knot stations of the plug downstream of the lip (fixed when the family's range of lips is known).
- O4a which case for the CFD margin. Proposed: that same E design, wave frame, the real row at 7.5 mm, re-run with the
  channel's cells halved axially and radially; the difference in thrust and wall force is the margin.

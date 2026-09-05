# Source-code digest — NASA `Three-Dimensional-Nozzle-Design-Code` (T. Rice, JHU/APL, 2001–2003; NASA release LEW-20180)

Audit scope: complete read of the three computational cores (`MOC_GridCalc_BDE.cpp` 3754 lines, `MOC_GridCalc_BDE_IO.cpp` 760, `STT2001Dlg.cpp` 3117, `3D_MOCGrid.cpp` 2789) plus headers, NR solvers, `engineering_constants.hpp`, dialog wiring, and sample inputs/outputs. All paths below are relative to
`c:\Users\amont\Claude\Projects\Presentazione RDE CVA\rde-lecture-code\Three-Dimensional-Nozzle-Design-Code\`. Line numbers cite the files as cloned (master @ 09ba559).

---

## 1. Repo inventory + provenance

| Item | Fact | Anchor |
|---|---|---|
| Origin | github.com/nasa/Three-Dimensional-Nozzle-Design-Code (clone; remote in `.git/config`) | `license.txt:18` "Please Visit https://github.com/nasa/..." |
| License | **NASA Open Source Agreement (NOSA) v1.3**, designation LEW-20180, POC heath.reising@nasa.gov | `license.txt:1-20` |
| Report | Rice, T., "2D and 3D Method of Characteristic Tools for Complex Nozzle Development," JHU/APL RTDC-TPS-481, 2003 (NTRS 20030067852) | `README.md` (link) |
| Author/era | Tharen Rice, JHU/APL, start dates 7/27/01 (2D), 5/14/02 (3D); light modernization passes by Rice (May 2020, `<fstream>` migration, parser rewrites) and H. Reising (5/28/20, popup suppression `3D_MOC/3D_MOCGrid.cpp:758`) | file headers; `MOC_GridCalc_BDE.cpp:33-37`; `STT2001Dlg.cpp:7-16` |
| Sponsor | "FG888BXX (**NASA GRC PDE Work**)" for MOC_Grid_BDE (`MOC_GridCalc_BDE.h:21`); "FG800XXX (NASA GRC Nozzle Work)" for 3D_MOC (`3D_MOCGrid.hpp:21`); IO adds "FG1CAXXX (URETIS)" (`MOC_GridCalc_BDE_IO.cpp:22`). I.e. written for **pulse-detonation-engine nozzle development** — same application family as the host RDE program. |
| Internal program name | 2D tool self-identifies as **"CONGO-2D"** in `summary.out` (`MOC_GridCalc_BDE_IO.cpp:55`) |
| Git history | GitHub-web-only commits (license/README/.gitattributes edits, deletion of stray output files); no code history — code arrived as a single drop. `git log`: 09ba559..(20 commits, all housekeeping). |
| Layout | `MOC_Grid_BDE/` (+ `outputs_M3.5Perf/`), `STT2001/` (+ `outputs_M3.5Perf/`, `friction_table.txt`), `3D_MOC/` (+ `outputs_cone10/`, `outputs_M4Perfect/`, `outputs_M4RAO/`, NR solver files) |
| Third-party code | **Numerical Recipes in C++** routines vendored in `3D_MOC/`: `newt.cpp`, `lnsrch.cpp`, `ludcmp.cpp`, `lubksb.cpp`, `fmin.cpp`, `sort2.cpp`, `nr.h`, `nrtypes*.h`, `nrutil*.h`. License implications in §5. |
| Units | US customary throughout: psia, °R, slug/ft³ (2D) or lbm/ft³ (3D), inches for geometry with R* = 1 in reference; explicit 12/144 in/ft factors sprinkled in integrals; `GASCON = 1545 ft·lbf/(lbmol·R)`, `GRAV = 32.174` (`engineering_constants.hpp:45,48`). |

The three tools form a pipeline: **MOC_Grid_BDE** designs a 2D/axisymmetric contour and writes a characteristic grid + mass-flow-tagged streamlines → **STT2001** lofts 3-D nozzles by tracing/trimming those streamlines → **3D_MOC** re-analyzes a (possibly modified) 3-D contour by reference-plane characteristics. Coupling between the tools is entirely through text files parsed by column position (§5, hidden couplings).

---

## 2. MOC_Grid_BDE — 2D planar/axisymmetric MoC contour design ("CONGO-2D")

### 2.1 Data structures and conventions
- Node grid `[i][j]`: `j` = right-running characteristic (RRC) index (0 = initial throat line TT′), `i` = point index **along** an RRC, `i=0` at the wall, `i=iLast[j]` at the axis. `maxLRC=1000` (i), `maxRRC=999` (j) hard caps (`MOC_GridCalc_BDE.cpp:66-67`), heap-allocated dense doubles: `mach, pres, temp, rho, x, r, gamma, theta, massflow, thrust, Sthrust` (`MOC_GridCalc_BDE.h:88-90`, alloc `:2691-2734`).
- Per-node **massflow** = integrated mass flux from the axis to the node along its RRC — i.e. a discrete stream function ψ; streamlines are later extracted as iso-mass-flow lines (`MOC_GridCalc_BDE_IO.cpp:414-668`).
- Separate arrays for the last left-running characteristic (LRC) "DE": `mDE,pDE,tDE,rhoDE,xDE,rDE,gDE,thetaDE,massDE` (`MOC_GridCalc_BDE.h:89`).
- Enums (`MOC_GridCalc_BDE.h:36-40`): geometry `TWOD|AXI`; type `RAO|CONE|PERFECT|FIXEDEND`; design parameter `EXITMACH|EPS|NOZZLELENGTH|ENDPOINT|EXITPRESSURE`.
- GUI inputs and defaults (`MOC_GridDlg.cpp:80-101`): M_design=4, nC=101 characteristics (forced odd, `MOC_GridCalc_BDE.cpp:96`), RWTU=RWTD=1 (throat arc radii / R*), γ=1.4, molWt=28.96, p0=1000 psia, T0=530 R, pAmb=0, dTLimit=0.5°, nRRCAboveBD=100, θB initial guess 25°, cone angle 15°, streamline output counts nSLi=10/nSLj=50. Validators: nC∈[2,301], nRRCAboveBD∈[20,1000] (`MOC_GridDlg.cpp:149,170`).

### 2.2 Gas model
Calorically perfect gas, single input γ and molecular weight. γ is **stored per node and linearly averaged/interpolated everywhere** (e.g. `G3 = 0.5*(gamma[ii][j-1]+gamma[i-1][j])`, `:2555`; interpolations `:790,1419`), so the plumbing for variable γ exists, but no mechanism ever changes γ from its input value — effectively γ = const. Isentropic state closure from stagnation conditions everywhere: `CalcIsentropicP_T_RHO` (`:2775-2800`), p = pT/(1+(γ−1)/2 M²)^{γ/(γ−1)}. Flow is everywhere assumed **irrotational, isentropic, shock-free**: there is no shock unit process, θ is clamped to ≥ 0 in the interior solver (`:2601,2676`; BDE region `:3370`), and any M<1 aborts.

### 2.3 Transonic start line (name and lineage identified)
`CalcInitialThroatLine` (`:2805-2900`):
- Radial distribution of start-line points: r_i/R* = [sin(π/2·(n−i)/n)]^1.5 (`:2838`) — a heuristic sinusoidal clustering attributed to "the way it is done in RAO".
- x of each point marched along the local RRC slope `rDyDx = tan(θ−µ)` (`:2842,2855`), with a guard that halves the slope (doubles drdx) until the local Mach ≤ 1.5 (`:2853-2860`) — heuristic.
- Point properties from **`KLThroat`** (`:3103-3178`): explicitly "taken from 'Transonic Flow in Small Throat Radius Curvature Nozzles' by **Kliegel and Levine**… they take the **HALL** method and modify the Axi calculation for a **toroid coordinate system** (R+1). The 2D version is the one developed by HALL." Third-order series u(y,z), v(y,z) in 1/(R_WTU+1); `z = x·sqrt(2 R_S/(γ+1))` (`:3120`). Axi branch `:3117-3140`, planar branch `:3141-3163`. Subsonic start line ⇒ SEC_FAIL with message (`:3171-3175`). The self-describing text is echoed to `summary.out` (`MOC_GridCalc_BDE_IO.cpp:92-98`).
- **`Sauer`** (`:3054-3098`) — "taken from the TDK program… Modified Sauer Transonic for Axisymmetric or Planar Flow (GRN, 1/95)" — is present but its call is **commented out** (`:2847`); dead code. `CalcHallLine` (`:2905-2952`, Hall series + discharge-coefficient CD formula `:2946`) is likewise **never called** (only referenced in a comment `:2822`).
- Alternative start: `throatFlag=1` gives a **uniform-Mach throat plane** from input static conditions + velocity (`mThroat = vel/sqrt(γRT g)`, `:110-116`; branch `:2866-2878`).
- ⚠️ Transcription defects inside `KLThroat` (see §7 RISKS): integer divisions `5/8`→0 (`:3124`) and `1/6`→0 (`:3146`), a `/34` that should be `/384` (`:3129`, compare the same coefficient `/384` in `CalcHallLine:2926`), `*` where `−` belongs (`:3133`, `:3157`), `1181` vs `1881` (`:3133` vs `:3127`). These pollute only third-order terms (and one second-order term via 5/8), so results remain plausible — which is exactly why they survived.

### 2.4 Unit processes — equations as implemented
Compatibility relations are written in "Rao book" form (the code cites "RAO eq. 15" and notes "The RAO manual is wrong in their equations (PTIN). I have corrected them in my copy of the book", `:2472-2474`), with Mach number as the marched variable:

Helper terms (`:2957-3048`):
- `CalcMu` µ = asin(1/M); `MM` = √(M²−1);
- `CalcA` A(M,γ) = √(M²−1) / [M(1+(γ−1)/2·M²)]  — coefficient of dM in dθ = A·dM ± axisymmetric term;
- axisymmetric source terms, chosen by magnitude to avoid the 1/tanθ singularity:
  `CalcB` = 1/[r(√(M²−1)/tanθ − 1)] (LRC, dz form), `Calcb` = 1/[r(√(M²−1)/tanθ + 1)] (RRC, dz form),
  `CalcR` = 1/[r(√(M²−1) + cotθ)] (dr form), `CalcRStar` = 1/[r(√(M²−1) − cotθ)] (dr form);
- characteristic slopes `lDyDx = tan(θ+µ)`, `rDyDx = tan(θ−µ)`; `TanAvg(x,y) = tan((atan x + atan y)/2)` — all segment slopes are **tangent-averaged** between endpoint iterates (modified-Euler / iterated-average corrector, no formal order statement).

**Interior point** `CalcInteriorMeshPoints` (`:2466-2686`): point 3 from LRC out of 1=[ii][j−1] and RRC out of 2=[i−1][j]; position from intersection of tangent-averaged slopes (`:2566-2577`); axisymmetric terms `T[1],T[2]` picked between the dx-form `(x3−x_k)(B_k+B_3)` and dr-form `(r3−r_k)(R_k+R_3)` by comparing |B| vs |R| (`:2584-2591`); then
`M3 = [2(θ2−θ1) + M2(A2+A3) + M1(A1+A3) + T1 + T2] / (A1+A2+2A3)` (`:2593`),
`θ3 = (θ1+θ2)/2 + ¼[M2(A3+A2) − M1(A1+A3) − M3(A2−A1) + T2 − T1]` (`:2598`).
Axis neighbor handling: if r=0 at point 1, B/R taken from the first off-axis point (AXI) or zero (2D) (`:2521-2534`). Iterate to `conCrit=1e-10` relative change in (x,r,M), max **1000** iterations with a fallback acceptance if the best-seen |ΔM| ≤ 5e-4 (`:2643-2654`, comment "1001 Iterations is good, do not change"); else SEC_FAIL. The author documents a known dual-solution pathology: "Another solution can arise where x[i][j] … less than x[i-1][j]. This is not good. I am currently working on how NOT 2 get the later solution" (`:2560-2563`).

**Axis point** `CalcAxialMeshPoint` (`:2262-2313`): r=0, θ=0 imposed; x from the averaged RRC slope; `M3 = M2 + 2(θ2 + b2·(x3−x2))/(A2+A3)` (`:2289`), the factor 2 being the axis reflection; 500-iteration cap, `exit(1)` on failure.

**Wall point on throat arc** `CalcArcWallPoint` (`:835-948`): wall circle r = 1 + RWTD − √(RWTD²−x²), θ_wall = asin(x/RWTD) (`:891-892`); M from the one-characteristic compatibility with T1 chosen by `B[1]<=R[1]` (`:897-903`); if Δθ_wall > DTLIMIT or beyond θB, a **special wall point** is inserted at α = min(θB, θ_prev + DTLIMIT/2) via `CalcSpecialWallPoint` (`:2360-2460`, an interpolated point 4 on RRC j−1 feeds the compatibility).

**Cone wall point** `CalcConeWallPoint` (`:953-1025`): position from LRC∩cone line; M iterated (tolerance 1e-8, 50 iterations).

**Dead code**: `CalcContourWallPoint` (`:2318-2355`) has no callers and carries "TODO: is this right".

### 2.5 The kernel / "BDE" Rao design logic (what BDE means operationally)
"BDE" = the three anchor points of Rao's 1958 method as implemented: **B** = wall point at the end of the initial circular-arc expansion (angle θB), **D** = a point chosen on the last kernel RRC from B, **E** = nozzle-lip/exit point terminating the LRC from D. `CalcContouredNozzle` (`:241-708`) narrates the algorithm explicitly (`:256-273`).

Nested iterations:
1. **Kernel build** `CalcRRCsAlongArc` (`:1030-1116`): march RRCs from TT′ along the arc until x = sin(θB)·RWTD; kernel is *reused* between θB trials (restart index backed off by 5, `j-=5` heuristic, `:324,488`); per-RRC wall mass-flow check: |mdot_wall − mdot_throat|/mdot_throat must be ≤ 2% else hard fail with "Try increasing # of starting characteristics" (`:1085-1089`); RRCs with negative-r points are collapsed (`:1097-1112`); axis Mach > 50 signals θB too large (returns −j, `:1076`).
2. **θB outer loop** (secant, `:476-574`): drives the design parameter (exit Mach / eps / length / endpoint-x / pT/pe from point E) to the target, relative tolerance **1e-8**, ≤20 iterations, with bracketing [θBmin, θBmax] initialized to [0.1°, 50°] (`:63-64`) and updated by failure semantics (SEC_FAIL_LOW ⇒ raise θB, SEC_FAIL_HIGH ⇒ lower; `SetThetaB` 0.8×/1.2× heuristics `:3718-3753`). Iteration history logged to `ThetaB.out`. A pre-pass strategy comment (`:210-215`): for min-length cases the perfect-nozzle solution bounds x_D to stop θB overshoot.
3. **D-point inner loop** `CalcLRCDE` (`:1472-1757`): secant on x_D along RRC B..D. For each trial: mass flow from wall B to D by interpolation of the ψ array (`CalcMdotBD` `:1436-1467`); `FindPointE` constructs the LRC D→E such that **mdot(D→E) = mdot(B→D)**; the **Rao eq. 14 control-surface condition at E** is then enforced:
   `θ_E,req = ½·asin[ 2(p_E − p_a)·144 / (ρ_E w_E² tanµ_E) ]` (`:1541-1543, 1589-1591, 1719-1721`)
   — i.e. sin2θ = 2(p−pa)cotµ/(ρW²) as in Rao 1958 — and the secant drives θ_E(returned) − θ_E,req → 0 (tolerance **1e-7**, ≤50 its). For `FIXEDEND` the condition is r_E = r_match instead (`:1561,1607`). For `PERFECT`, D is simply the axis point of the last kernel RRC (`:1515-1519`), making DE the uniform-exit LRC.
4. **LRC DE construction** `FindPointE` (`:1764-2228`): quotes Rao eq. 12–13 Lagrange-multiplier constancy along DE (`:1770-1773`: L2 = −W cos(θ−µ)/cosµ, L3 = −r ρ W² sin²θ tanµ) but implements the equivalent ODE march: 2D case closed-form (state constant along DE, `:1874-1923`); AXI PERFECT closed-form from the axis (`:1929-1983`); AXI general case integrates dM/dr, dx/dr, dθ/dr along DE by **RKF45** (`RungeKuttaFehlberg` with the standard Fehlberg tableau, `:3458-3509`) inside a step-halving loop `des *= 0.5` until component error estimates < 1e-6 (θ,x,M) / 1e-12 (r) (`:2035-2052`), accumulating trapezoidal annular mass flux `mdot = ½g(ρ0u0+ρEuE − dxdr(ρ0v0+ρEvE))·π(rE²−r0²)/144` (`:2070-2073`); final E located by secant on r using plain **RK4** (`RungeKutta` `:3414-3453`) to mdot tolerance 1e-8 (`:2136-2173`). The derivative system `Deriv` (`:3514-3558`) is the closed-form LRC/mass-flux ODE with an explicit near-singularity warning when tanθ approaches m³/(((γ+1)M²/2−1)M²+1) (`:3536-3540`). nRRCPlus (=nRRCAboveBD) intermediate points are laid down along DE to seed the mesh above BD.
5. **Downstream regions**: `CalcBDERegion` (`:3258-3409`) re-marches LRCs from DE **back toward the wall** (point 2 = [i+1][j], mirrored interior process, 50-it cap, exit(1) on failure); `CalcRemainingMesh` (`:1122-1162`) fills DE→exit toward the axis; `CalcWallContour` (`:1167-1336`) then finds the **wall as the streamline through B**: along each RRC, accumulate trapezoidal mass flux from D outward until it equals mdotMatch = ψ_B − ψ_D (`:1186`), then secant (conCrit, 50 its) with distance-weighted linear interpolation of state (`:1241-1291`); rows re-indexed so the wall is i=0 (`:1294-1321`). `CropNozzleToLength` (`:1341-1429`) cuts all RRCs at the exit plane x_E with linear interpolation and adds the exit axis point; `CalcDE` (`:3638-3714`) resolves the final DE line for reporting.

### 2.6 Iteration/convergence constants (collected)
| Constant | Value | Where |
|---|---|---|
| `conCrit` (unit-process relative change) | 1e-10 | `:62`, used `:878,1247,2285,2411,2564,3334` |
| θB outer tolerance / iterations | 1e-8 rel / 20 (post-hoc accept if <1e-5) | `:476,577` |
| D-point (Rao eq.14) tolerance | 1e-7 / 50 | `:1653` |
| DE RKF45 component tolerances | 1e-6 (M,x,θ), 1e-12 (r) | `:2037-2038` |
| Mass-flow secants | 1e-8 / 50 | `:2136`; wall contour uses conCrit `:1247` |
| Interior iterations | 1000 (+fallback 5e-4) | `:2564,2643` |
| Axis iterations | 500 | `:2285` |
| Kernel wall mass-flow guard | 2% | `:1085` |
| Wall Δθ limit | DTLIMIT (default 0.5°) | `:56,104` |
| Axis-Mach θB rejection | M > 50 | `:1076` |
| Cone / special-point interpolation caps | 50 its | `:985,2412` |

### 2.7 Outputs
`summary.out` (inputs echo, start line, 1D-vs-2D mass flow/thrust/C*/CD, θB answer, DE table, wall contour with per-point %Δψ, exit-plane data, Isp/Cfg; `MOC_GridCalc_BDE_IO.cpp:46-245`); `MOC_Grid.plt` (Tecplot, one zone per RRC: x, r, M, θ, ψ, i; `:274-327`); `MOC_SL.plt` (streamlines as iso-ψ lines interpolated on the grid, revolved every 5° into 37 azimuthal copies for 3-D display, `:414-668`); `Summary.plt` (wall, RRC BD, LRC DE); `rao.dat` (**TDK99-compatible** wall table R/R*, X/R*, θ(deg) — "If you were used RAO, this file would be called WALL_TBL.50", `:672-687`); debug kernels `TT'.out, wall.out, wall_i.out, axis_i.out, center.out, LastKernel.out, UncroppedKernel.out, BFE_Kernel.out, TT'BF_Kernel.out, ThetaB.out`.

---

## 3. STT2001 — Streamline "Tracing" Tool

**Key finding: STT2001 performs no integration of any velocity field.** It is a streamline *selection, scaling, rotation, trimming, and lofting* tool operating purely by interpolation on the streamlines that MOC_Grid_BDE already wrote to `MOC_SL.plt`. There is no RK integrator and no interpolation on the MoC characteristic grid itself for tracing (the grid file is read only for the reflected-wave validity check, below).

### 3.1 Input pipeline
`GetSLData` (`STT2001Dlg.cpp:918-1019`): parses `MOC_SL.plt` — psi (mass-flow %) scraped from fixed columns 21–23 of each `zone t=` header (`:990-994`, brittle), then rows x, dummy, dummy, r, M, p, t, ρ, θ, γ, mdot, j into `xsl/rsl/msl/psl/tsl/thsl/jsl[i][k]` per streamline i (max 4200 points/SL, `nparamPTS`, `:79`). The `.inp` file (fixed-order whitespace-separated, `OnFileOpen` `:2268-2337`) carries: file prefix + 4 filenames; parametric sweep ranges for the SL-field placement (`RSL` scale, `XSL/YSL/ZSL` offsets, start/end/step each — outer loops at `:667-671` write one row per combination to `<prefix>_all_runs.dat`); five throat/trim constraints; pAmbient, aThroat, IspIdeal, MassFlow; symmetry block; check/combo states; MaxLength; GridSF; XStatus.

### 3.2 Throat lofting (`CalcThroatSLs`, `:1024-1158`)
The 3-D nozzle throat is defined by up to **5 circular-arc constraints** (center (YC, ZC), radius RC, azimuth range α..ω, nSL rays, inner/outer surface flag from combo). **Not superellipses — circles only** ((y−yc)²+(z−zc)²=rc², also in `TrimSLs` `:1311`). For each ray angle θ on the arc: compute the constraint point (y,z), its radius r w.r.t. the SL-field center (m_YSL, m_ZSL) and azimuth β (`:1073-1079`); find the pair of axisymmetric streamlines bracketing r/m_RSL at their first station and the interpolation fraction `dr` (new ψ recorded: `newPsi[n] = psi[i] − dr(psi[i]−psi[i-1])`, `:1088-1097`); then for every downstream station j of SL i, **double interpolation**: resample SL i−1 at x = xsl[i][j] (inner while `:1123`), blend radius/pressure with `dr`, place the 3-D point at (x·m_RSL + m_XSL, r_t cosβ + m_YSL, r_t sinβ + m_ZSL) (`:1138-1142`). So every 3-D wall streamline is a radially-blended copy of two axisymmetric streamlines, at fixed azimuth — exact for axisymmetric parents, heuristic when the loft mixes scale/offset. Cross-section morphing along x is therefore *inherited from the parent flowfield*, not prescribed.

### 3.3 Trimming and gridding
- `TrimSLs` (`:1295-1348`): cut each SL at first exit from a constraint circle (within its x- and azimuth-window), linear interpolation to the crossing.
- `TrimSLsToMaxLength` (`:2519-2563`): crop at x = maxX (note dead statement after `break`, `:2557-2558`).
- `FindMaxX` (`:2923-3116`) — **reflected-wave validity bound**: reads `MOC_Grid.plt`, finds the grid point nearest the earliest-trimmed SL endpoint; if that RRC reaches the axis, it walks the reflected wave along the **anti-diagonal [iAxial−m][jMatch+m]** — the code says "This is not exactly right, but it is close" (`:3089-3090`) — and returns the x where the reflected wave first passes inside a traced SL; the nozzle is cropped there because the parent MoC grid is invalid downstream of a wave reflected off a *removed* boundary.
- `TrimSLsDueToAxiRevolution` (`:1548-1714`): for clustered engines (nRev pods about a symmetry center), trims SLs that would intersect a rotated copy, with SL-index matching heuristics (`:1613-1631`) and half-angle/half-radius tolerance bands (`:1666-1672`).
- `CalcGridSLs` (`:1353-1543`): resamples each SL onto `nparamGRIDX = 100·GridSF` x-stations (biased: half the points in the first third of length), interpolated by **5-point Newton divided differences** (quartic; `:1421-1476`) with linear fallback on non-finite or negative-p results (`:1478-1501`). ⚠️ the station formula `xgrid = (x1 + k(x3−x1))·m_RSL/((nparamGRIDX−1)/2) + m_XSL` (`:1378-1379`) divides the whole coordinate (not the step) by (N−1)/2 — a real defect (§7); downstream clamping (`j==0` / `j>newSLPts` branches) hides it partially.

### 3.4 Performance integration (`CalcNozzleParameters`, `:1966-2209`)
Wall surface between adjacent gridded SLs split into two triangles per quad; area = ½|U×V|; axial projection & pressure force via cosθ = rotateSL[n]·W_x/|W| with the orientation flag set from surface side and sweep direction (`:1057-1066, 2059-2064`); the whole integration is done **twice** (x-major and SL-major loops) and cross-checked to 0.1% (`:2203-2207`) — a built-in self-consistency check worth noting. Thrust build-up (`GetPerformanceDataFromMOCSummaryFile`, `:2687-2918`): throat stream thrust taken from the MOC `summary.out` (string-prefix scraping, e.g. `"2-D Gross Thrust"` at fixed offsets `:2737-2817`) scaled by throat-area ratio; Isp = (F_throat + ∫(p)dA_x − F_friction − p_a·A_exit)/mdot (`:2835-2838`); **friction from a user lookup table** `friction_table.txt` (area-ratio → lbf, ≤25 points, linear interpolation, `GetFrictionLoss` `:2568-2605`) — no boundary-layer model whatsoever, the table is externally produced (e.g. by TDK/BLM).

### 3.5 Outputs
ICEM CFD BULKIN card files `<prefix>_ThroatSL.out`, `_TrimSL.out` (LEVEL/POINT format, `:1163-1236, 1720-1789`); **PLOT3D** `_trimmed_P3D.xyz` + `_trimmed_P3D.dat` (pressure) + `_end_P3D.xyz` (`:1793-1885`); Tecplot `<prefix>.plt` and `_Engine.plt` (revolved pod copies, `:1886-1953`); `_cl.dat` centerline/lip trace; `_AvsX.out`, `_AvsSL.out`; `_ThroatSummary.out`; `_STT_summary.out` (loss breakdown); `_all_runs.dat` (sweep table). `Matrix.cpp`/`Vector.cpp` are small self-written linear-algebra classes (only `Vector::crossprod`/`mag` used by the core, `:2044-2074`).

---

## 4. 3D_MOC — 3-D method of characteristics analysis

### 4.1 The scheme actually implemented (named)
**Reference-plane (z-plane) inverse-marching bicharacteristic method**, explicitly attributed in the header comment: "It uses the **reference plane method**… The best write up I have found on this is **W.C. Armstrong, 'A Method of Characteristics Computer Program for Three-Dimensional Supersonic Internal Flows,' AEDC-TR-78-68**" (`3D_MOCGrid.cpp:23-28`). Equation numbers cited in comments (eq 23–25, 27–28, 30–33, 40) are Armstrong's. Large parts (the conic body-fit normal computation with its `goto continue23..34` ladder, `:1107-1241`; `CalcParametricAngle` with `x21..x24` labels, `:2115-2158`) are line-by-line transliterations of Armstrong's FORTRAN.

It is **not** a tetrahedral/Butler scheme and **not** near-characteristics: unknown points sit on prescribed z = const planes; four (field) or three (body) bicharacteristics on the Mach cone connect the new point P2 back to *base points* on the previous plane, whose states come from a surface fit (inverse marching).

### 4.2 Flow model and state
Per-point state (`point.hpp:9-37`): z, p, T, M, γ, molWt, ρ, θ, q, ψ, L, δ, plus x,y. Angles: **θ = flow angle in x–z (tanθ = dx/dz), ψ = flow angle for y (tanψ = dy/dz)** (`:1495-1496, 420-421`); δ = parametric angle around the Mach cone; β = Mach angle. Marched unknowns per point: **(p, θ, ψ)**; everything else recovered isentropically from P1's stagnation state: "Assume isentropic properties along the streamline" (`:590-594`; T, ρ, q, M updates `:518-521, 828-831`). γ and molWt are carried per-point and even surface-fitted (`:2300-2301`) but never vary. **Consequences: homentropic, irrotational-in-effect, shock-free; no entropy/rotationality transport of any kind.** Mach < 1 aborts (field `:522-526`) or triggers wall-refinement retry (body `:836-840`).

### 4.3 Initial-value surface — NOT taken from an axisymmetric solution
`SetInitialPropertiesForCircularThroat` + `SetInitialReferencePlane` (`:201-279, 1435-1510`): the initial plane is a **circular disc with uniform state** — one p, T, M (>1), θ, ψ for all points (dialog defaults p=1000 psia, T=530 R, **M=1.1**, θ=ψ=0; `3D_MOCDlg.cpp:69-88`). Points laid out on rings: ring spacing = r0/_nRadii with _nRadii = int(r0·nDiv/(2πr0))+2, ≥7 points per ring, one center point; outermost ring flagged `_bodyPointFlag` (`:1479-1506`). The sample runs confirm uniform M=1.1 start (`outputs_cone10/z=0.out`). **The "modified version of a MOC_Grid_BDE contour" enters only through the wall geometry file** (`.geo`: count, header, then per-plane `z r0 x0 y0` — circle of radius r0 centered (x0,y0); `:252-273`); the 2D MoC *flow* solution is never ingested. So the M4Perfect/M4RAO samples analyze the 2D-designed *walls* under a fresh uniform sonic-ish start — a deliberate approximation, and an important caution for any "IVS from axisymmetric solution" reading.

### 4.4 Field-point unit process (`CalcFieldPoint`, `:330-546`)
1. P2 provisionally on P1's streamline: x2 = x1 + tanθ12·dz/cosψ12, y2 = y1 + tanψ12·dz (Armstrong eq 27–28; `:418-421`), with θ12, ψ12 P1–P2 averages.
2. Four bicharacteristics at δ, δ+π/2, δ+π, δ+3π/2 (first δ = atan2(x,y) at P1, `:395-404`); base-point location from Armstrong eq 30–33: L = dz/[cosβcosθcosψ − sinβ(sinθcosψcosδ + sinψ sinδ)], x_b = x2 − L(cosβ sinθ + sinβ cosθ cosδ), y_b = y2 − L(cosβ cosθ sinψ − sinβ(sinθ sinψ cosδ − cosψ sinδ)) (`:436-441`). Guard: base point radius > wall radius ⇒ return FAIL and refine dz (`:445-450`).
3. Base-point state and in-plane derivatives from a **thin-plate-spline surface fit** w(x,y) = a0 + a1x + a2y + Σ b_i r_i² ln r_i² over the point + its **8 nearest neighbors** (`SurfaceFit` `:2246-2359`; neighbor search = all-pairs distance + NR `sort2` per plane, `SetNeighborPoints` `:2185-2241`; option "All Point Spline" fits the whole plane, `AllPointSurfaceFit` `:2364-2477`); fitted variables: p, ρ, q, θ, ψ, γ, molWt; analytic TPS derivatives give dθ/dx, dθ/dy, dp/dx, dp/dy (`:1594-1613`). 12×12 (or N+3) linear systems by NR `ludcmp/lubksb`.
4. Normal-direction derivative assembly (Armstrong eq 23–25): dxdN = −cosθ sinδ, dydN = sinθ sinψ sinδ + cosψ cosδ, dzdN = sinθcosψ sinδ − sinψ cosδ; dtdz, dpdz approximated by back-projection along the plane offset (`:474-481`).
5. **Compatibility equation coefficients** `CompEqu` (`:2163-2180`): a0 = 144/(tanβ·ρq²/g) [in²/lbf], a1 = cosδ − sinβ sinδ·dzdN·L/dz, a2 = cosθ(sinδ + sinβ cosδ·dzdN·L/dz), RHS = sinβ·L(sinδ·dtdN − cosθ cosδ·dpdN) + a0·p_b + a1·θ_b + a2·ψ_b, i.e. a0·p2 + a1·θ2 + a2·ψ2 = RHS along each bicharacteristic.
6. Solve the 3×3 linear system for (p2, θ2, ψ2) — four times, over the cyclic triplets {012, 123, 230, 301} of the four bicharacteristics, **and average the four solutions** (`CompatabilityEquationSolverForFieldPoint` `:1248-1316`; NR LU; negative pressure raises a message box `:1312`).
7. Outer fixed-point iteration on (p, θ, ψ) to 1e-5 relative (absolute below 2e-2 for angles), ≤50; nonconvergence ⇒ `exit(1)` (`:412, 529-533`). New parametric angles from `CalcParametricAngle` (`:2115-2158`, quadratic in sinδ/cosδ picking the root nearest the old δ).

### 4.5 Body-point unit process (`CalcBodyPoint`, `:551-904`)
- Wall representation: per z-plane, each 3-adjacent-wall-point triple is classified/fit as CONSTANT_X, CONSTANT_Y, LINE, or CIRCLE (`BodyFit` `:1833-1935`, three-point circle solve); quadratic interpolation of the fit coefficients across planes (k−1, k, k+1) yields the **unit normal to the body surface** at arbitrary z (`CalcUnitNormalToBodySurface` `:910-1243`, Armstrong-FORTRAN goto ladder; circle branch `:1138-1147`, general-conic branch `:1163-1241`; a "Tharen added" patch forces n1>0 at z=0, `:1145-1146`).
- P2 position: intersection of the streamline-projection relation (Armstrong eq 40 coefficients CC, `:671-674`) with the local body fit (`SolveForBodyPointPosition` `:1974-2064`, per-conic closed forms with root selection nearest previous P2; negative discriminant ⇒ `exit(1)`).
- 3 bicharacteristics: δ0 from the surface normal via cosδ = −N1 sinθcosψ + N2 cosθ − N3 sinθ sinψ (`:633-647`), companions at δ0 ± **π/3** ("Tharen changed PI/2 to PI/3… keep the base points in the current nozzle geometry", `:724-725`); a `del -= PI` phase shift is applied along the wall bicharacteristics (`:742-743, 786-787`).
- Solve: **2 compatibility equations + flow tangency** N1·cosψ' ... implemented as f2 = a20·cos(x2) + a21·tan(x1) + a22·sin(x2) with x=(p,θ,ψ) (global `funcv`, `:50-60`) via NR globally convergent **Newton (`newt`)** with analytic Jacobian `funcvDeriv` (`:62-78`), TOLF=1e-8, TOLMIN=1e-12, MAXITS=200 (`newt.cpp:12-14`); done for the 2 (of 3 declared) bicharacteristic pairs {0,1},{0,2} and **averaged** (`CompatabilityEquationSolverForBodyPoint` `:1321-1430`; note `n=2` at `:1339` with comment "I tried varying all of the points and the results are the same").
- Robustness ladder: outer 50-iteration loop; on failure with residuals >1e-3 return FAIL; on FAIL/FAIL_MACH the driver `CalcNozzle` (`:122-187`) calls `AddNewNozzlePoint` (`:2762-2789`) to **insert an interpolated wall plane (halving dz) and restart the whole plane (i = −1)**, up to 15 times, then aborts. Converging ducts (upstream-pointing normal) only warn (`:617-623, 697-703`).

### 4.6 Interpolation stencils, marching, guards — summary
- Marching direction: +z, plane-to-plane, step dz = wall-table spacing (adaptively subdivided by plane insertion only).
- Stencils: 8-nearest-neighbor TPS per point (default) or global TPS; nearest-neighbor search re-done per plane by full sort — O(N²logN).
- Stability guards: base point outside wall ⇒ dz refine; M<1 aborts; tiny-value flushing to zero everywhere (1e-5/1e-8/1e-10) — including inside `funcv`/`funcvDeriv` (`:58, 75`), which can zero Jacobian entries.
- No CFL-like criterion; the only step control is the failure-triggered halving. No shock capture/fitting; no swirl-specific handling (ψ is a Cartesian y-angle, not azimuthal swirl).
- Hardwired limits: `_cFit[5000][7]` (`3D_MOCGrid.hpp:82`); `_pt[i]`, `_wallPt[j]` sized `_nZ*5` planes (`:1682,1698`) while `AddNewNozzlePoint` increments `_nZ` (`:2769`) — ≥4·nZ insertions overflow silently; debug relics `if (k==129 && i==0) i=i;` (`:372-375, 1545-1548`), `if (k==196 && i==77)` (`:611-614`).

### 4.7 Outputs
`full_mesh.plt` (all points, with pT/TT recomputed), `axialStations.plt`, `Streamlines.plt` (each i across k — since points follow streamlines, i = streamline id), `streamtube.plt` (subset via `SL.inp` index list, `:2594-2652`), `Wall.plt`, `Initial Wall.plt`, `z=0.out` (initial plane), `outfile.out` (body-normal log). Dialog defaults: nDiv=36 wall rays, zOutputIncrement=10 (`3D_MOCDlg.cpp:80-88`). Runs on a worker thread (`3D_MOCGridThread.cpp:60`).

---

## 5. Code quality / portability assessment

**Numerical Recipes dependency (license red flag).** `3D_MOC/` vendors verbatim NR-in-C++ source (`newt/lnsrch/fmin/ludcmp/lubksb/sort2`, headers `nr.h`, `nrutil*.h`). The NR license does **not** permit source redistribution; its presence inside a NOSA-1.3 release is NASA's problem, but for the host program it means: **never port or vendor these files**. All uses are trivially replaceable (LU solve of 3×3/12×12 → `numpy/jax.numpy.linalg.solve`; `newt` → `scipy.optimize.root` / a 3-variable Newton with the already-analytic Jacobian; `sort2` → `argsort`). The NOSA 1.3 license itself is OSI-approved but GPL-incompatible and imposes modification-reporting obligations — fine for *reading, oracle use of shipped outputs, and independent re-implementation of the published math*, which is all the host program needs.

**MFC coupling.** Computational cores are classes (`MOC_GridCalc`, `C3D_MOCGrid`) whose MFC tendrils are limited to: `AfxMessageBox` error popups, `CString` filenames, one `MOCPlotDialog` plotting call at the end of the 2D drivers (`MOC_GridCalc_BDE.cpp:702-705, 815-818`), and a `PostMessage` progress callback in 3D (`:137,183`). STT2001 is worse: the entire algorithm lives inside the dialog class `CSTT2001Dlg` with GUI state as algorithm state. Failure handling is `exit(1)` in ~15 places (kills the process mid-GUI).

**Extraction feasibility / effort.**
- MOC_Grid_BDE core: cleanly extractable (replace Afx/CString, delete plot calls). A faithful Python port is 1–2 weeks with tests; **but the host already owns a better 2D MoC** — the value is as *reference implementation and oracle*, not as a port.
- STT2001: algorithm is simple interpolation geometry; a clean-room reimplementation (NumPy) is ~2–4 days and preferable to porting the dialog-entangled original.
- 3D_MOC: the reference-plane scheme is extractable (~2.8k lines, self-contained except NR); a JAX port is feasible (TPS fits, 3×3 solves and the Newton system are differentiable-friendly; the nearest-neighbor `sort2` stencil selection is not, but is fine under `stop_gradient` for forward analysis). Realistic effort for a *verified* port: 2–4 weeks, dominated by reproducing/deciding each Armstrong transliteration quirk. Given the bug census (§7) a re-derivation from Armstrong AEDC-TR-78-68 with this code as cross-check is the honest path.

**Hidden couplings.**
1. Inter-tool file contracts parsed positionally: STT2001 scrapes `MOC_SL.plt` zone headers at columns 21–23 (`STT2001Dlg.cpp:990-994`), `MOC_Grid.plt` zone headers at columns 12–14 (`:3010-3013`), and `summary.out` by string prefix + fixed offsets (`:2737-2817`). Any 2D-side format change silently breaks 3D lofting and performance.
2. Global mutable state in 3D: `_a[3][4]` shared between the class and the free functions `funcv/funcvDeriv` used by NR `newt` (`3D_MOCGrid.cpp:48-78`) — not reentrant.
3. Units: mixed in/ft with literal 12/144 factors inside integrals (e.g. `:1877, 2071-2072, 3218-3225`; `CompEqu` a0 comment "has to be in units of (in2/lbf) to work correctly", `:2170-2173`) — a porting trap.
4. 2D grid reuse-across-secant-trials (kernel restart `j-=5` heuristics) couples solver state with iteration history (`MOC_GridCalc_BDE.cpp:322-326, 486-489`).

**Memory hygiene:** `delete` vs `delete[]` mismatches (`MOC_GridCalc_BDE.cpp:2745-2755`; `3D_MOCGrid.cpp:1713-1717`); `DeleteDataMembers` for the 2D class is never called (no leak growth per run, but the destructor is empty `:74-77`); STT2001 `DeleteArrays(SLCount)` iterates rows allocated with a different count than freed if constraints changed — benign in practice, sloppy in principle.

---

## 6. Sample cases and their oracle value

### 6.1 `MOC_Grid_BDE/outputs_M3.5Perf` — axisymmetric perfect nozzle, M_exit = 3.5
Inputs (from `summary.out`): AXI, PERFECT, exit Mach 3.5, γ=1.4, molWt 28.96, pT=500 psia, TT=530 R, pAmb=0, nC=101, RWTU=RWTD=1, DTLIMIT 0.5°, nRRC=100. Record numbers: **eps = 6.73651, L/R* = 12.5363, CD = 0.984756, exit Mach wall = axis = 3.5, Isp_vac = 69.9496 s, Cfg = 0.699496 (vs ideal 100 declared), θB = 15.2196°**; start-line table with Kliegel–Levine M(r) from 1.17779 (wall) is printed in full.
**Oracle value: high.** (a) Perfect-nozzle contour + uniform M=3.5 exit is directly checkable by the host 2D MoC (F1-class machinery) as an *independent-code* cross-check — exactly the "cross-code agreement is never sufficient" doctrine needs: an external, non-GENO, non-host lineage. (b) CD=0.984756 at RWTU=1 can be compared against the Kliegel–Levine discharge-coefficient series independently. (c) The full RRC grid (`MOC_Grid.plt`) and DE line are shipped. Caveats: KLThroat transcription bugs (§2.3) perturb the start line at third order; conCrit-level agreement should not be expected — treat as a ~1e-3-to-1e-4-class oracle pending re-derivation of the start line.

### 6.2 `STT2001/outputs_M3.5Perf` — 3-D loft of the M3.5 flowfield
`M3.5Perf.inp`: circular constraint r=1.02 (72 SLs, full 360°), throat area 0.7854 in², plus the parent `MOC_sl.plt/MOC_Grid.plt/summary.out/friction_table.txt`. `_STT_summary.out` records the bookkeeping chain (throat thrust 492.024 lbf scaled from MOC 1971.99 by area ratio, pressure force 531.764, friction 131.956 from the table, Isp 23.94 for the trimmed pod). **Oracle value: moderate** — mainly as a regression fixture for any F5-style extraction reimplementation (geometry + area/force integrals reproducible to the 0.1% internal cross-check), not as physics truth (friction is a lookup; the case is a trimmed pod, not a full nozzle).

### 6.3 `3D_MOC/outputs_cone10` — 10° conical nozzle
`cone10.geo`: 217 circular sections, r: 1 → 13.33 (10° half-angle wall from a 1-in throat), uniform start M=1.1, p=1000 psia, T=530 R (`z=0.out`). **Adjudication on the Taylor–Maccoll suggestion: T–M does *not* apply.** This is internal expansion flow from a uniform M=1.1 disc into a diverging cone — no conical shock, no supersonic freestream; the appropriate analytic limit is axisymmetric **radial source flow** far downstream (Mach on spherical caps from A/A* of the equivalent source), and the appropriate code oracle is the host's own 2D axisymmetric MoC run with the identical uniform start line and cone wall. Its real value: **3-D-code-on-axisymmetric-input consistency test** — every azimuthal asymmetry in `full_mesh.plt` is pure numerical error of the 3-D scheme (TPS stencils across the polar singularity will show there first). The Rice 2003 report (companion agent) presumably quantifies exactly this.
### 6.4 `3D_MOC/outputs_M4Perfect` and `outputs_M4RAO`
`.geo` tables (162 planes each, r0(z), x0=y0=0) are the M4 perfect and M4 Rao (min-length) wall contours exported from MOC_Grid_BDE; both analyzed with uniform M=1.1 start. `outputs_M4RAO` adds `SL.inp` (14 streamline indices) → `streamtube.plt`/`tubeout.plt` (stream-tube extraction demo used for the JANNAF layouts `m4jannaf.lay`). **Oracle value:** same 3-D-vs-2D consistency class as cone10 but with curved walls; additionally M4RAO's parent `rao.dat`-type wall is a *Rao design oracle* for the host (see §7 connections). Note the mismatch caveat: the 3-D runs start uniform at M=1.1, whereas the 2D design's throat line is the Kliegel–Levine curved line — wall-pressure comparisons between the two tools carry that start-line inconsistency (the report's own comparison figures inherit it too).

---

## 7. CONNECTIONS to the host program (and anti-connections / risks)

### 7.1 Candidate connections (what / where / why)
1. **F6 "B-lite 3-D helical march demonstrator" ← 3D_MOC scheme.** What: a complete, compilable reference-plane inverse-march bicharacteristic implementation with the Armstrong AEDC-TR-78-68 lineage named in-code (`3D_MOCGrid.cpp:23-28`) — this *locates* one of the plan's "to-locate" 3-D MoC literature anchors operationally (Armstrong complements the cited Ransom/Hoffman/Thompson line; Ransom's is the reference-plane sibling). Where: F6 design decisions on (a) plane orientation (z-planes here; a helical march would tilt the reference surface), (b) interpolation (TPS over scattered neighbors here — works, but is the scheme's soft underbelly), (c) wall treatment (conic section fits + tangency Newton — clean, reusable idea), (d) step control (failure-triggered plane insertion — crude but effective). Why: it is the only in-hand executable 3-D MoC; even used purely as a negative example it sharpens the demonstrator spec.
2. **F6 caution (strong): the "IVS from axisymmetric solution" step does not exist here.** 3D_MOC starts from a *uniform* disc (§4.3). The bridging step the host plans (hand an axisymmetric/stratified MoC state to a 3-D march) is precisely what this code skipped; its samples show the consequence (start-line inconsistency, §6.4). Budget that interface as new work, not as something to imitate.
3. **F5 stream-surface extraction ← STT2001.** What: extraction of stream surfaces from a parent flowfield by ψ-interpolation (mass-flow-tagged grid → iso-ψ lofts), plus the **reflected-wave validity bound** (`FindMaxX`): after trimming a streamsurface, the parent solution is invalid downstream of the characteristic reflected from the removed boundary. Where: F5 requirements list. Why: the host's F5 must implement this bound *rigorously* (domain-of-dependence walk on the characteristic mesh); STT2001's anti-diagonal i−m/j+m walk is self-admittedly approximate (`STT2001Dlg.cpp:3089-3090`) — a named pitfall with a code citation.
4. **F2 stratified march ← ψ-bookkeeping pattern.** What: per-node integrated mass flow as a stream-function coordinate on a characteristic grid (`CalcMassFlowAndThrustAlongMesh`), used for wall-as-streamline construction and extraction. Why: the host's s(ψ), h0(ψ) stratification needs exactly this coordinate on the F2 three-family march; the 2D code demonstrates the trapezoidal-flux discipline (and its 2% failure guard) on a non-orthogonal mesh.
5. **Rao design oracle ← MOC_Grid_BDE RAO mode.** What: an independent (non-Rao-code-lineage-free but non-host, non-GENO) implementation of Rao 1958: control surface DE via Lagrange-multiplier ODE integration (RKF45), mass balance mdot(BD)=mdot(DE), and eq. 14 sin2θ_E = 2(p_E−p_a)cotµ_E/(ρ_E W_E²) (`MOC_GridCalc_BDE.cpp:1541,1719`). Where: validation of the host's cycle-averaged variational optimum in the degenerate uniform-inflow, γ=const limit (the host's functional must reduce to Rao; this code provides a numeric fixture: M4RAO wall table + θB=15.22°-class answers, `rao.dat` TDK-format). Why: a genuinely third-party Rao fixture is scarce; this one ships with its full kernel.
6. **Transonic start-line cross-check ← KLThroat.** What: a second independent implementation (Kliegel–Levine toroid form) next to whatever Sauer-lineage line the host/GENO uses; the code even documents the TDK-Sauer variant side by side (dead `Sauer`, `:3054`). Why: start-line model risk is a named host concern; two series implementations + the report's tables allow a three-way check. **Caution:** fix the §2.3 transcription bugs before using KLThroat numerically.
7. **TDK interoperability detail.** `rao.dat` ≙ TDK99 `WALL_TBL.50` inviscid-contour format (`MOC_GridCalc_BDE_IO.cpp:672-687`) — cheap adapter if the program ever exchanges contours with TDK-era toolchains; likewise STT2001 writes PLOT3D and ICEM BULKIN.
8. **Provenance link.** The 2D tool was sponsored as *NASA GRC PDE work* — historically adjacent to the host's RDE application; citable in the paper's tool-landscape discussion (P-1) as prior detonation-engine-motivated nozzle tooling.

### 7.2 Anti-connections
- **No rotationality anywhere.** All three codes are homentropic/irrotational by construction (2D: Mach-based unit process + global isentropic closure; 3D: single stagnation state per streamline, uniform IVS). Nothing here informs the host's stratified s(ψ), h0(ψ) machinery beyond the ψ-bookkeeping pattern; none of these codes can serve as a stratified-flow oracle.
- **Not a variational/adjoint lineage.** The Rao mode is the classical control-surface construction; no gradients, no design sensitivities; the θB/x_D secant nest is the opposite of the host's adjoint approach — useful only as an endpoint oracle.
- **STT2001 is not a tracer.** Do not cite it as a streamline-integration reference; it interpolates pre-computed streamlines (§3). For F5 the host needs true characteristic-grid interpolation + integration, which this tool avoids entirely.
- **3D_MOC's circular-section-only input** (despite general conic machinery) means it cannot analyze genuinely 3-D (non-circular) nozzles as shipped — the STT2001→3D_MOC pipeline is broken at that joint (the report presumably discusses this; the code path `SetInitialPropertiesForCircularThroat` is the only geometry entry).

### 7.3 RISKS — concrete defects found in code (file:line)
**MOC_Grid_BDE**
1. `MOC_GridCalc_BDE_IO.cpp:156` — `mdotErrRatio` printed in `summary.out` but **never assigned anywhere** (grep-verified): the "Massflow error due to grid at end of Kernel (%)" field is garbage (sample prints 100%).
2. `MOC_GridCalc_BDE.cpp:3124` — `z*(y*y - 5/8)`: **integer division, 5/8 = 0** (axi KLThroat u2 term); same class at `:3146` (`1/6` = 0, 2D u1) and in dead `CalcHallLine:2921,2938` (`5/8`, `15/8`).
3. `:3129` — `(52*G*G + 51*G + 327)*y*y*y*y/34` — should be **/384** (compare `:2926`); `:3133` — `.../1728 * (388*G*G + 1161*G + 1181)...` — `*` where `−` belongs and 1181 vs 1881 (compare `:2931-2932`); `:3157` — same `*`-for-`−` in the 2D v3 term.
4. `:2037-2038` — `dxErr, dTErr, drErr` **read uninitialized** on first evaluation of the while condition (only `dMErr` is preset at `:2035`).
5. `:508` — `while (dS.dSi[2] == SEC_FAIL_LOW || dS.dSi[2] == SEC_FAIL_HIGH && i++ < 20)`: precedence makes the 20-cap apply only to the HIGH branch; a persistent SEC_FAIL_LOW can loop unboundedly.
6. `:1485-1486, 1742-1743` — `xDMaxBisect/xDMinBisect` computed but never used: the intended bisection fallback for secant failures ("There are some cases that fail in the secant method, but do have a solution", `:1740-1741`) was never wired.
7. `:2745-2755` — `delete` on `new[]` arrays (UB); destructor never frees (`:74-77`).
8. `:1097-1112` — negative-r RRC collapse copies 8 state arrays but **not** `massflow` and not thrust rows.
9. `:2318` — `CalcContourWallPoint` dead code with "TODO: is this right".
10. Failure handling by `exit(1)` (e.g. `:925, 1016, 2056, 2184, 2304, 3394`) — any port must convert these to raised errors before batch use.

**STT2001**
11. `STT2001Dlg.cpp:1378-1379` — biased-grid station formula divides the whole coordinate, not the step, by (N−1)/2 (§3.3): x-stations are wrong; masked by clamping logic downstream. Any quantitative reuse must rewrite `CalcGridSLs`.
12. `:1984` — pMax scan `for (i = 0; i <= nNewSLs; i++) ... psl[i][0]`: `psl` is indexed by *parent* SL count (`nSL`), not `nNewSLs`; reads uninitialized rows when nNewSLs ≥ nSL.
13. `:990-994, 3010-3013` — fixed-column parsing of zone headers (3 chars at offset 21/12): breaks silently for ψ or J values with other widths.
14. `:2557-2558` — `maxLength = maxX` after `break`: unreachable; maxLength stays stale when trimming to max length.
15. `:1120-1123` — resampling inner loop starts `k=1` with pre-increment, so index 1 of the neighbor SL is never tested as an upper bracket (first tested is 2); off-by-one interpolation near the throat.
16. Dialog-state = solver-state; `exit(1)` on any file problem (e.g. `:931, 2252, 2587`).

**3D_MOC**
17. `3D_MOCGrid.cpp:1232` — `ax = -2*(fa[2] + (fb[2] + fc[2]*P.z*P.z))/ax;` — pattern elsewhere is `(fb + fc*P.z)*P.z`; missing parenthesis ⇒ wrong quadratic evaluation in the non-circle normal branch.
18. `:1235` — `by = -2*(fa[4] + (fb[4] + fc[3]*P.z)*P.z)/by;` — **fc[3] should be fc[4]** (copy-paste), same branch.
19. `:626-628` vs `:704-706` — comments assign N2/N3 to Y/X and then X/Y respectively; the tangency-equation ordering `_a[2][*]` (`:1352-1354`) vs `funcv` f[2] (`:57`) is internally consistent only for one of the two labelings — flagged as an unresolved sign/axis ambiguity to test, not a proven bug.
20. `:689` — `if (newJK.dSi[0] != ... && newJK.dSi[1] != ...)`: should almost certainly be `||`; a changed j with unchanged k skips the body refit.
21. `:58, 74-75` — flush-to-zero of |f|<1e-10 and Jacobian entries inside `funcv/funcvDeriv` can hand `ludcmp` a singular matrix near converged states.
22. `:2769` + `:1682,1698` — `AddNewNozzlePoint` grows `_nZ` against arrays sized `initial _nZ*5`: >4× insertions ⇒ heap overrun, silent.
23. `:1339` — body compatibility uses only 2 of the 3 bicharacteristic pairs (`n=2` with `pt[3][2]` declared) — author note says results identical; still an inconsistency with the 3-point construction.
24. `:1940-1968` — `FindClosestBodyPoint`: `jMin` uninitialized if all distances ≥ 9e9; also its `while (k < _nZ && _wallPt[0][k].z < X.z) k++;` can index `_wallPt[0][_nZ]` at `:1953` when the loop exits by the first condition.
25. `:372-375, 611-614, 1545-1548` — hardwired debug traps (`k==129`, `k==196 && i==77`) left in shipping code: indicates the exact cases where the author chased failures; useful map of fragility (near-axis point i=0 at deep plane; late body points).
26. NR licensing (§5) — do not carry `newt/ludcmp/...` into any host artifact.

---

## 8. Fidelity ledger — derived vs heuristic (as implemented)

| Element | Class | Anchor |
|---|---|---|
| Characteristic compatibility relations (2D, Mach form, A/B/b/R/R* coefficients) | **Derived** (Rao-text lineage; author claims corrected errata) | `MOC_GridCalc_BDE.cpp:2593-2599, 2966-3014` |
| Kliegel–Levine toroid start-line series | **Derived** (published series) — but transcription-corrupted at 3rd order | `:3103-3178` + §7.2-3 |
| Sauer TDK start line | Derived, dead code | `:3054-3098, 2847` |
| Rao eq. 14 control-surface condition at E; L2/L3 multiplier constancy on DE | **Derived** (Rao 1958) | `:1541, 1719, 1770-1773` |
| RKF45/RK4 tableaux for DE ODE | **Derived** (standard Fehlberg) | `:3414-3509` |
| DE ODE system dM/dr, dθ/dr, dx/dr | Derived (closed-form characteristic/mass-flux algebra) | `:3514-3558` |
| Trapezoidal mass-flow/thrust integration across RRCs | Derived (first-order quadrature choice = practice) | `:3183-3240` |
| Tangent-averaged slopes / coefficient averaging in every unit process | **Practice/heuristic** (no order analysis; iterated to conCrit) | `:3037-3041` et passim |
| sin^1.5 start-line point clustering; drdx-doubling M<1.5 guard | **Heuristic** | `:2838, 2853-2860` |
| θB secant with 0.8×/1.2× moves, [0.1°,50°] bracket, j−=5 kernel restart | **Heuristic** | `:314-316, 3718-3753, 324` |
| 2% wall-mass-flow guard; M>50 θB rejection; 5e-4 interior fallback acceptance | **Heuristic tolerances** | `:1085, 1076, 2645` |
| STT2001 double interpolation of neighbor SLs; ψ-blend loft | Derived-for-axisymmetric-parent, heuristic beyond | `STT2001Dlg.cpp:1102-1150` |
| 5-point divided-difference SL resampling with linear fallback | Practice | `:1421-1501` |
| Reflected-wave bound via i−m/j+m diagonal | **Heuristic (self-declared)** | `:3089-3093` |
| Friction from user table lookup | **External data, heuristic model** | `:2568-2605`, `friction_table.txt` |
| Triangulated pressure/area integration + dual-loop 0.1% self-check | Derived + good practice | `:1966-2209` |
| 3D reference-plane bicharacteristic geometry (eq 23–33), compatibility coefficients, eq 40 wall intersection | **Derived** (Armstrong AEDC-TR-78-68) | `3D_MOCGrid.cpp:418-498, 2163-2180, 671-678` |
| TPS (r²ln r²) surface fit over 8 nearest neighbors | Derived method, **heuristic stencil choice** (8; nearest-by-distance) | `:2246-2359, 2185-2241` |
| Averaging 4 triplet solutions (field) / 2 pair solutions (body) | **Heuristic symmetrization** | `:1259-1315, 1339-1409` |
| δ companions at ±π/3 (body), del−=π shift | **Heuristic** ("Tharen changed PI/2 to PI/3") | `:724-731, 742` |
| Conic body fits + quadratic-in-z normal interpolation | Derived (Armstrong), transliteration-corrupted (§7.17-18) | `:1833-1935, 1107-1241` |
| dz control by wall-plane insertion (≤15 retries) | **Heuristic** | `:141-175, 2762-2789` |
| Outer fixed-point tolerances 1e-5 (p,θ,ψ); newt TOLF 1e-8 | Practice (magic numbers) | `:412, 660`; `newt.cpp:13` |

**Bottom line for the host program:** the mathematics is respectable and traceable (Rao 1958, Kliegel–Levine, Armstrong AEDC-TR-78-68), but the implementations carry enough transcription-level corruption and uninitialized-state UB that *shipped outputs* (not code paths) are the safe oracle currency, at ~1e-3 fidelity class; the code's chief gifts are (i) an operational Armstrong-lineage reference-plane 3-D MoC to steer/caution F6, (ii) the reflected-wave validity requirement for F5, (iii) an independent Rao eq.14 design fixture (M4RAO, rao.dat), and (iv) a second transonic start-line lineage for cross-checking — each usable only after the specific defects catalogued in §7.3 are accounted for.

# Digest — T. Rice, "2D and 3D Method of Characteristic Tools for Complex Nozzle Development, Final Report", JHU/APL RTDC-TPS-481, June 30, 2003 (NASA CASI 20030067852)

Read: ENTIRE report, pp. 1–42 (all sections 1.0–9.0 incl. references and nomenclature; no appendices exist beyond §9.0 Nomenclature — the "appendices" of this report ARE §7 References (pp. 40–41), §8 Acknowledgements (p. 41), §9 Nomenclature (p. 42)). Every claim below carries a page and, where applicable, the report's equation number.

---

## 1. Bibliographic identity, purpose, tool-suite architecture

- **Identity** (pp. 1, 5): Tharen Rice, The Johns Hopkins University Applied Physics Laboratory, Laurel MD. Report RTDC-TPS-481, June 30, 2003. Prepared under NASA Grant NAG3-2460, "Design of Exhaust Nozzle for the RBCC-GTX Concept," with NASA Glenn Research Center. Extension of a follow-on task awarded September 2001 (p. 5).
- **Purpose** (p. 5, §1.0): user's manual + mathematical-algorithm documentation for a GUI-driven (MFC/Windows) 2D MoC nozzle *design* tool and a 3D MoC nozzle *analysis* tool.
- **Lineage** (p. 6, §2.0): Under earlier grants (NAS3-99146, then NAG3-2460; Refs. 1–2) APL built a nozzle **streamline tracing tool called STT2000** (report's name; the cloned repo's "STT2001" is evidently a later build of the same tool — the report itself never uses the string "STT2001"). STT2000 required a known nozzle flowfield; initially the commercial TDK code (SEA Inc.) supplied it. To remove the TDK dependency, the **2D MOC tool** was written; because STT2000 traced streamlines only through 2D flowfields, the **3D MOC tool** was then written to provide a truly 3D flowfield in which to start streamline tracing (p. 6).
- **Chaining architecture** (pp. 6, 18, 36): 2D MOC tool designs a planar/axisymmetric contour and (with print option *Full*) writes the files STT2000 needs; a GUI button "Run Streamline Tracing Tool" launches STT2000 directly from the 2D tool (p. 18, §3.2.9, Fig. 19). The 2D tool's contours are also the geometry *input* to the 3D MOC tool (verification cases, pp. 36–38). So the chain is: **2D MOC (design) → {STT2000 (trace 3D shapes through the 2D field)} and/or → 3D MOC (analyze a given 3D contour + throat conditions)**.
- **Streamline-tracing rationale** (pp. 5–6, §2.0): steady-flow streamline defined by V × ds = 0 **(eq. 1, p. 5)**; a boundary of streamlines is a streamtube carrying constant mass flow (p. 5). Neglecting viscosity, a wall may be inserted along any portion of a streamtube without altering the streamtube's shape/characteristics — the basis of streamline tracing as a 3D design technique (p. 6). Caveats stated: assumes boundary-layer of the traced 3D design does not significantly alter the inviscid field; valid at the design condition only — off-design requires high-fidelity modeling (p. 6). Prior applications: waveriders and supersonic inlets (Refs. 4–10, p. 6); little prior work on nozzle streamline tracing before this effort (p. 6).

---

## 2. MOC_Grid_BDE — the 2D MoC design tool (report §3.0, pp. 7–22)

### 2.1 Scope and gas model
- GUI-driven Windows code; designs **planar and axisymmetric** nozzles; **perfect gas, inviscid** solution algorithm (p. 7). Constant gamma and molecular weight are user inputs (Fig. 12, p. 14; Table 3, p. 37: gamma = 1.4, MW = 28.96). **No variable-gamma, no chemistry, no rotationality: flow is implicitly homentropic/irrotational** (isentropic relations used throughout, e.g. the 1D performance comparison "based on a 1D isentropic process from the nozzle total conditions to a uniform Mach 1 throat", p. 16).
- Nondimensionalization (p. 10, §3.2): all lengths by throat half-height (planar) or throat radius R* (axisymmetric). Dimensional performance assumes R* = 1 in (axisym) or half-height 1 in + reference width 12 in (planar, half-nozzle only — "applicable to SERN nozzle performance calculations", p. 10).

### 2.2 Characteristic/compatibility relations
- **LRC compatibility (axisymmetric)**: d(θ − μ) = −[1/(√(M²−1) + cot θ)] · dr/r **(eq. 2, p. 8)**, with μ = sin⁻¹(1/M) **(eq. 3, p. 8)**. Derivation of the finite-difference method delegated to **Ref. 11 (Moe & Troesch, "The Computation of Jet Flows with Shocks," STL TR-59-0000-00661, 1959)** (p. 8).
- **RRC compatibility (axisymmetric)**: d(θ + μ) = [1/(√(M²−1) − cot θ)] · dr/r **(eq. 4, p. 9)**.
- **Planar case**: "Solving for a planar nozzle simplifies the equations; however the process remains the same" (p. 9) — i.e. the axisymmetric dr/r source term drops; no separate planar equations are printed.
- Note the unusual grouping: these are the θ ± μ (Prandtl-Meyer-like) forms with the axisymmetric source folded in via the (√(M²−1) ± cot θ) denominator; they are equivalent to the standard 2D-axisymmetric characteristic compatibility relations for irrotational flow (the report does not show the derivation; classed REPORT-ASSERTED, derivation in Ref. 11).
- **Characteristic slope for the DE line integration**: dx/dr = 1/tan(θ + μ) **(eq. 5, p. 9)** (LRC direction).

### 2.3 Transonic start line (initial data line TT′) — §3.3, pp. 19–20
- Computed by a **"modified Hall method developed by Kliegel and Levine"** for transonic throat flow **(Ref. 13: Kliegel & Levine, AIAA J. 7(7), 1969, pp. 1375–1378)** (p. 19). Uses a **toroid coordinate system** to get an analytic axial+transverse velocity solution near the throat (p. 19). (This is the classic Kliegel–Levine 1/(R+1)-expansion fix of Hall's small-throat-radius series; report gives no equations for it.)
- Construction (p. 19): calculation **starts at the nozzle wall**; each subsequent point of the line is positioned by constructing an RRC from the preceding point. **Ad-hoc limiter: if local M > 1.5 at a point, the line shape is changed so Mach 1.5 is never exceeded** — "The Mach constraint as well as the line shape is arbitrary. This tool uses this particular method because it has shown to work for many nozzle designs" (p. 19; explicitly declared heuristic).
- **Upstream radius R_up effect** (p. 19, Fig. 22 p. 20): computed flow velocity on the line increases by nearly **1/(R_up + 1)**; smaller R_up ⇒ shallower initial line, higher line Mach (Fig. 22 examples: M = 1.44 for R_up/R* = 1; M = 2.2 for R_up/R* = 0.4 unconstrained; M = 1.50 with constraint), which pushes the constructed RRC downstream and can break the nozzle solution (p. 19).
- Alternative input mode (p. 13, §3.2.4): "Throat Conditions" box — user gives static conditions + velocity (> M 1) directly as the initial-data-line properties instead of solving from total conditions.

### 2.4 Kernel construction and the design (BDE) logic — §3.1, pp. 7–10
Geometry vocabulary (Fig. 3, p. 8; Nomenclature p. 42): throat = two circular arcs, R_up (converging side) and R_down (initial expansion side), both /R*; initial expansion arc TB of angle θ_B (arc length R_down·θ_B); B = end of initial expansion; E = nozzle wall exit point; F = centerline foot of the RRC from B; BD = last RRC of the initial expansion region.

Algorithm (pp. 7–10):
1. **Outer iteration on θ_B** (initial expansion angle) until the given exit design parameter is met at point E (p. 7).
2. From initial data line TT′ (flow known and supersonic everywhere on it, p. 7), march LRC/RRC intersections: from point (1,0) the LRC is solved by finite differencing of eq. 2 (pp. 7–8); wall point (0,1) at the LRC∩wall (wall = arc of radius R_down centered at z = 0; wall condition θ = wall angle) (p. 9); from (0,1) an RRC via eq. 4; interior points at RRC∩LRC intersections (p. 9). Continue until point B. Centerline is the symmetry axis. Result = **kernel TBFT′** (Fig. 5, p. 9).
3. **Point-D inner iteration** (pp. 9–10, Fig. 6 p. 10): D lies on the last kernel RRC (BF). Mass flow crossing BD is computed; an LRC is constructed from D to an unknown E such that **mass flow across DE = mass flow across BD** (mass-flow matching closure). For a **perfect nozzle**, properties along DE are uniform and E follows trivially (p. 9). For other types, E and the DE properties come from a **Runge-Kutta-Fehlberg** integration of dM/dr and dθ/dr (from compatibility eq. 2) and dx/dr (eq. 5) along the LRC (p. 9).
4. Properties at E are compared with the design constraint (nozzle type + design parameter); if matched, the **wall contour B→E is the streamline** obtained by back-calculating RRCs from DE upstream — i.e., completing the MOC grid in region **BDE** and tracing the streamline through it (p. 10, Fig. 6; §3.2.8 p. 17, Fig. 17). If not matched, iterate D and ultimately θ_B; "There exists only one combination of θ_B and D that satisfies all of the equations and constraints" (p. 10, uniqueness ASSERTED not proven).

This is exactly the classical **Rao/kernel–control-surface architecture** (kernel TBFT′ + control characteristic DE + turning-region BDE), hence the repo name MOC_Grid_**BDE** — BDE is the report's own label for the wall-determination region (Figs. 6, 17; "TT'BF_Kernel.out", "BFE_Kernel.out" in Table 1, p. 15). The report never expands "BDE" as an acronym; it is the triangle B–D–E.

### 2.5 Nozzle types (design closure conditions) — §3.2.2, pp. 11–13
1. **Perfect nozzle** (p. 12): uniform exit plane (all properties constant radially), exit flow angle 0 (fully axial); wind-tunnel style, maximum length for a given exit condition (p. 12).
2. **Rao (optimum thrust) nozzle** (p. 12): from G.V.R. Rao's late-1950s optimum-contour analysis (**Ref. 12: Rao, "Exhaust Nozzle Contour for Optimum Thrust," Marquadt [sic] Aircraft Co., ARC Semi-Annual Meeting, June 1957**). Report characterizes it as minimum-length nozzle for a given exit condition; any exit-condition change at that fixed length lowers performance (with declared "subtleties", p. 12). Implemented closure: nozzle-wall exit condition at E for **zero back-pressure**: **sin(2θ_E) = 2 cot(μ_E)/(γ M_E²) (eq. 6, p. 12)**. [This is Rao's control-surface end-point condition; the tool imposes it pointwise at E rather than solving a full variational problem — the variational content is inherited through Rao's derived exit condition. NOTE: eq. 6 as printed is the vacuum (P_a = 0) form of Rao's condition; the GUI has a P_ambient input (Fig. 12, p. 14) but the report only documents the zero-backpressure closure.]
3. **Set End Point** (p. 12): contour forced through a user-set exit wall point (XEnd/R*, REnd/R*). Solutions exist only for lengths between the Rao (minimum) and perfect (maximum) lengths for that area ratio; exit field neither uniform nor Rao-optimal (p. 12).
4. **Cone/Wedge** (p. 13): straight cone (axisym) or wedge (planar) of given half-angle.

Design parameter (one of, §3.2.3 p. 13): exit Mach; area ratio (exit/throat); pressure ratio P_total/P_exit-static; length ratio Xend/R*.

### 2.6 Unit processes
- **Interior point**: LRC∩RRC intersection, finite-difference solution of eqs. 2 and 4 (pp. 7–9; derivation Ref. 11). Details (predictor-corrector or Euler averaging) NOT given in the report.
- **Axis point**: centerline treated as symmetry axis (p. 9); F is the centerline point of the RRC from B (p. 9). No special axis-singularity treatment (dr/r → 0/0) is documented.
- **Wall point (design mode)**: on the prescribed arc TB, wall intersection with LRC, flow angle = wall angle (p. 9). Downstream of B the wall is *solved for* as a streamline (p. 10), not prescribed — i.e., the classical inverse/design wall process.
- **Wall reflection + grid enrichment**: as an LRC reaches the wall it is reflected toward the centerline (p. 17). **DTHETAB (Δθ_B)_MAX limiter** (§3.2.8, pp. 17–18, Figs. 16–18): if the wall-angle difference between adjacent wall points exceeds (Δθ_B)_MAX, a new RRC is inserted at (Δθ_B)_MAX from the prior wall point — characteristic-insertion step control on the expansion arc; nominal 0.25°–0.5°; smaller ⇒ finer grid, more run time (pp. 17–18).
- **# of RRC above BD** (p. 17, Fig. 17): grid density of the BDE region used to back-out the B→E streamline (default 100).
- **Number of Starting Characteristics** (p. 17): number of points on the initial data line (default 101).

### 2.7 Step control, convergence diagnostics, tricks (§3.2.6.1 pp. 15–16; §3.4 pp. 20–22)
- **Internal mass-flow consistency check**: percent difference between integrated mass flow along the last initial-expansion RRC (BDF) and mass flow on the initial data line must be < **2%** or the code notifies and terminates (hard-coded tolerance; "future versions may make this a user input") (p. 16).
- Summary.out reports 2D performance (integration of individual flow points) vs 1D isentropic performance (p. 15–16); θ_B iteration history in ThetaB.out (Table 1, p. 15).
- **Four parameters govern solution health** (p. 20): Downstream radius, Number of starting characteristics, Upstream radius, (Δθ_B)_MAX. Nominal defaults work for most cases; with defaults, 32 of 101 initial-line points define the initial expansion region for R_down/R* = 1 (Fig. 23, p. 21). Too many points ⇒ RRCs run too close together "and sometimes even cross" causing solution difficulties (p. 21) — i.e., **characteristic crossing (compression coalescence) is acknowledged and unhandled: no shock capturing/fitting anywhere in the tool**.
- **R_down is the dominant convergence knob** (p. 21): reducing it to 0.2 halves the number of expansion-region points (32 → 14, Fig. 24 p. 22), coarsens the mesh, amplifies downstream errors; "The downstream radius input seems to have the greatest effect on whether or not the nozzle solution will converge. Keeping this parameter around the nominal 1.0 value is recommended" (p. 21).
- θ_B guess default 25°; longer nozzles (perfect) have lower θ_B than short ones (Rao) (p. 16).

### 2.8 Outputs (Table 1, p. 15)
Summary.plt/.out, rao.dat (contour re-usable as TDK RAO-option input — a deliberate TDK interface), TT'.out, ThetaB.out; Full adds MOC_Grid.plt, MOC_SL.plt (streamlines: Radial×Axial counts set in §3.2.7 p. 16), center.out, wall.out, TT'BF_Kernel.out, BFE_Kernel.out, wall_i.out, axis_i.out, LastKernel.out, Uncropped Kernel.out (grid extended beyond exit plane).

---

## 3. STT2000/STT2001 — streamline tracing tool: WHAT THE REPORT ACTUALLY CONTAINS

**Important negative result of the deep-read: this report does NOT document the STT tool's internal mathematics.** Its algorithmic content lives in the predecessor reports, Ref. 1 (Rice & VanWie, AATDL-00-033, JHU/APL, Feb. 2000, RBCC-Trailblazer) and Ref. 2 (Rice, RTDC-TPS-335, NASA NAG3-2460, May 2001, RBCC-GTX) (pp. 5–6, 40). What THIS report gives:
- Concept and justification of streamline tracing (eq. 1, streamtube mass conservation, inviscid wall-insertion argument) — pp. 5–6 (see §1 above).
- Assumption ledger: inviscid design-point-only validity; BL non-interference assumed; off-design requires high-fidelity tools (p. 6).
- Integration contract with the 2D tool: STT2000 consumes files produced only under the *Full* print option; launched by GUI button from the 2D tool (p. 18, §3.2.9). The natural data carriers are the Full-option flowfield files (MOC_Grid.plt/MOC_SL.plt/kernel matrices, Table 1 p. 15); the report does not specify which files STT2000 reads.
- History: several versions of STT2000 developed under the two previous grants; originally fed by TDK flowfields (p. 6).
- **Nothing on**: interpolation scheme inside the 2D field, streamline ODE integrator, superellipse/lofted cross-section transitions, stream-tube extraction mechanics, or STT output formats. Any such content must be recovered from Refs. 1–2 or from the repo source itself (the code-study agent's domain). Claiming otherwise would be inventing content.

---

## 4. 3D_MOC — 3D MoC analysis tool (report §4.0, pp. 23–35)

### 4.1 Formulation: reference-plane + bicharacteristics hybrid
- Purpose: compute 3D nozzle flowfield given initial throat conditions and a given nozzle contour — an **analysis** tool, not design (p. 23).
- **Reference-plane method**: nozzle parsed into axial stations; each new plane (normal to z, p. 26) computed from the preceding reference plane (p. 23). Within that scaffold, point solutions use **bicharacteristics (rays of the Mach conoid)** — so the scheme is a reference-plane-organized bicharacteristic method, following **Ref. 14: W.C. Armstrong, "A Method of Characteristic Computer Program For Three-Dimensional Supersonic Internal Flows," AEDC-TR-78-68, Jan. 1979** ("A majority of the explanation is echoed below", p. 23; Armstrong specially thanked as "referenced extensively", p. 41).
- **Characteristic surfaces** (p. 24): steady inviscid ideal flow admits stream surfaces (u f_x + v f_y + w f_z)² = 0 **(eq. 7)** and Mach conoids (u g_x + v g_y + w g_z)² − a²(g_x² + g_y² + g_z²) = 0 **(eq. 8)**.
- **Bicharacteristic ray** on the conoid **(eqs. 9–11, p. 24)**: dx = (cosβ sinθ + sinβ cosθ cosδ)dL; dy = (cosβ cosθ sinψ − sinβ(sinθ sinψ cosδ − cosψ sinδ))dL; dz = (cosβ cosθ cosψ − sinβ(sinθ cosψ cosδ + sinψ sinδ))dL, with velocity parametrization u = q sinθ, v = q cosθ sinψ, w = q cosθ cosψ **(eqs. 12–14, p. 24)**; β = Mach angle; δ = parametric angle around the conoid, in the plane normal to q, measured from the plane containing q and x (pp. 24–25, Figs. 26–27). Coordinates: z axial, x, y transverse (Fig. 26 p. 24; Nomenclature p. 42). θ = flow angle w.r.t. x–z plane, ψ = flow angle w.r.t. y–z plane (p. 42).
- **Conoid compatibility equation, difference form** **(eq. 15, p. 25; repeated as eq. 29, p. 29)**:
  (cotβ_i/(ρ_i q_i²))(P₂ − P_i) + cosδ_i(θ₂ − θ_i) + cosθ_i sinθ_i(ψ₂ − ψ_i) + sinβ_i[cosθ_i cosδ_i(∂ψ/∂N)_i − sinδ_i(∂θ/∂N)_i] dL_i = 0,
  where ∂/∂L, ∂/∂N are derivatives along/normal to the bicharacteristic (p. 25). The cross-derivative closure **(eqs. 30–33, p. 29)** expresses (∂θ/∂N)_i via (∂θ/∂x, ∂θ/∂y) from the surface fit and the geometric normals (∂x/∂N)_i = −cosθ sinδ_i, (∂y/∂N)_i = sinθ sinψ sinδ_i + cosψ cosδ_i, (∂z/∂N)_i = sinθ cosψ sinδ_i − sinψ cosδ_i; same form holds for ψ (p. 29).
- **Streamline compatibility** (isentropic-energy relations along a streamline): (γ/(γ−1))R dT = (1/ρ)dP = −q dq **(eq. 16, p. 25)**; used in solved form T₂ = T_T (P₂/P_T)^((γ−1)/γ) **(eq. 34)**, ρ₂ = R T₂/P₂ [as printed — dimensionally this must be ρ₂ = P₂/(R T₂); the printed eq. 35 appears to be a typo in the report] **(eq. 35)**, q₂ = √(2 γ/(γ−1) R (T_T − T₂)) **(eq. 36)** (p. 30), with P_T, T_T the *total conditions along the streamline* — i.e., **homenergetic-isentropic per streamline; since the initial plane is uniform (p. 33), effectively globally isentropic/irrotational in use. No entropy transport, no rotational corrections, no shock treatment anywhere in §4.**

### 4.2 Marching methodology (§4.1.2, pp. 26–32)
- **Initial reference plane** (p. 26): normal to z; user-specified uniform P, T, M, θ, ψ (Fig. 35 p. 34); grid of nearly equally spaced points inside the wall circle (Fig. 28 p. 26), spacing d = 2πR/n_Divisions **(eq. 41, p. 33)**, nominal 36 radial divisions (p. 33). Outermost ring = **body points**; interior = **field points** (p. 26).
- **Wall geometry input** (p. 26, eq. 17): per axial station, a circle r_i² = (x−x_i)² + (y−y_i)² with (r_i, x_i, y_i) per z read from a datafile (Fig. 29 p. 27; first row = number of axial stations; header "Z r0 x0 y0"). So the given 3D contour = z-stack of (possibly offset) circles — general 3D-ness enters via center offsets x0(z), y0(z) and r(z). dz between planes is taken from the geometry file's z-stations (p. 27).
- **Field point unit process** (§4.1.2.2, pp. 27–30; Fig. 30 p. 28): inverse (backward-ray) method. From new-plane point P₂ (first located by projecting the streamline from P₁: x₂ = x₁ + (tanθ/cosψ)dz, y₂ = y₁ + tanψ dz, z₂ = z₁ + dz, **eqs. 18–20, p. 27**), construct **four bicharacteristics back to the initial plane** at δ_i = 0, π/2, π, 3π/2 **(p. 28)**, foot points P₃–P₆ via **eqs. 21–24 (p. 28)** (inverted forms of eqs. 9–11 with dL_i = dz/(cosβ cosθ cosψ − sinβ(sinθ cosψ cosδ_i + sinψ sinδ_i)), and z_i = z₁). Flow properties at the feet from a **surface fit** on the old plane (below). Unknowns in eq. 29 are P₂, θ₂, ψ₂ ⇒ only 3 bicharacteristics needed; per **Ref. 14's recommendation the tool solves four 3-point subsets [(P₃,P₄,P₅), (P₃,P₅,P₆), (P₃,P₄,P₆), (P₆,P₄,P₅)] and averages** the resulting (P₂, θ₂, ψ₂) (p. 30). Then ρ₂, T₂, q₂ from eqs. 34–36 (p. 30). **Predictor-corrector iteration**: new streamline from P₁ using average of P₁,P₂ properties → new P₂ location → resolve, until location and properties converge "within some tolerance" (tolerance value not stated) (p. 30). Repeated for all field points.
- **Body (wall) point unit process** (§4.1.2.2 [numbering duplicated in report], pp. 30–32; Fig. 31 p. 31): new body point P₂ = intersection of {plane defined by the body-surface unit normal and the unit velocity tangent to the surface at P₁} with the body surface at station z₂: B(x,y,z) = 0 **(eq. 37)** solved simultaneously with the plane equation **(eq. 38, p. 31)** (n₁,n₂,n₃ = wall unit normals). **Local body-surface shape approximation** (§4.1.2.2.1, p. 31): around P₁,P₂ the surface is fit as one of four shapes — vertical line x = c; horizontal line y = c; sloped line ax + by = c; circle (x−a)² + (y−b)² = c — solving a, b, c per point to get the normal coefficients (p. 31). [Wall is handled cross-section-wise; only these four 2D primitives — a stated-by-construction geometric limitation.]
  - Compatibility closure at the wall (§4.1.2.3, pp. 31–32): **three** bicharacteristics from P₂ back to the old plane, feet P₃–P₅; P₄ chosen on the line through P₁ normal to the body surface, with parametric angle δ₄ = cos⁻¹(−n₁ sinθ cosψ + n₂ cosθ − n₃ sinθ sinψ) **(eq. 39, p. 32)**; δ for P₃, P₅ iterated so the feet stay inside the flow region (p. 32). Solve: 2 × compatibility (eq. 29) + **flow-tangency constraint n₁ cosψ₂ + n₂ tanθ₂ + n₃ sinψ₂ = 0 (eq. 40, p. 32)** for (P₂, θ₂, ψ₂); **three 2-bicharacteristic subsets (P₃,P₄), (P₃,P₅), (P₄,P₅) solved and averaged**; ρ₂,T₂,q₂ from eqs. 34–36; iterate to convergence as for field points (p. 32).
- **Surface fit for old-plane data** (§4.1.2.2.1, pp. 28–29): thin-plate-spline-type fit from the small-deflection equation of an infinite plate: W(x,y) = a₀ + a₁x + a₂y + Σᵢ b_i r_i² ln r_i² **(eq. 25, p. 28)**, N fit points, closure conditions Σb_i = Σx_i b_i = Σy_i b_i = 0 **(eqs. 26–28, p. 29)**; N+3 unknowns. Derivation in Ref. 14. **Known accuracy issue** (p. 29): initial N = 9 (point + 8 nearest neighbors) gave slight errors — spurious property differences at constant radius in cases where uniform flow was expected; fixed by setting **N = all points in the reference plane** (error eliminated). GUI still offers "9 Point Spline" vs full-plane fit (§4.2.3, p. 33, Fig. 34). Better scattered-data algorithms identified but **not implemented**: ACM Algorithm 792 (Renka, Ref. 15), CSHEP2D/Algorithm 790 (Renka, Ref. 16), Algorithm 761 (Akima, Ref. 17) (p. 29).

### 4.3 Inputs/outputs and operational limits (§4.2, pp. 32–35)
- Only white GUI inputs functional; grayed = placeholders for future implementation (p. 32) — e.g., "Number of Ray Pts" and per-axis print controls appear non-functional (Figs. 25, 33).
- **Uniform initial plane only** (p. 33, §4.2.4): "the flow properties over the entire initial plane are constant. This limits the tool's capability to calculate non-uniform initial flowfields. The solution algorithm presented herein is capable of obtaining a solution starting with a non-uniform flowfield, the hindrance really occurs in the user input." — i.e., **non-uniform inflow is an input-plumbing limitation, not an algorithmic one** (report's own adjudication).
- Progress: code determines total axial steps from geometry file; per-station progress boxes (p. 34). Output decimation eqs. 42–43 (pp. 34–35). "Every N Step Number" output trigger is the crash-forensics mechanism: "This option may come in handy if the tool bombs before completion" — set it to the bombed Step Number to dump the flow at that station (p. 35). [The report thereby acknowledges the tool can "bomb" mid-march; no stability criterion (CFL-like dz limit vs conoid footprint) is documented anywhere.]
- Output files (Table 2, p. 35): Z=0.out (initial plane), Wall.plt, Full_mesh.plt, AxialStations.plt, Initial Wall.plt, Streamlines.plt (all TECPLOT).

---

## 5. Validation content (§5.0, pp. 36–40)

### 5.1 2D MOC tool (p. 36)
- "Numerous example cases"; most extensive verification of the suite. Method: **self-consistency** — run for given design parameters, verify the computed exit plane meets them (e.g., perfect nozzle prescribed M_exit = 4.0 → check resultant exit Mach = 4.0 and exit-plane uniformity) (p. 36). Fig. 39 (p. 36): contours for exit Mach 4.0 — Rao, Perfect, Cone, Set End Point Z/R* = 12 (the repo's M4 perfect/M4 Rao output cases correspond to exactly these). **No quantitative error numbers are reported for the 2D tool alone in this section**; external cross-checks appear only inside the 3D verification (Figs. 42–44: APL 2D vs SEA RAO vs TDK).

### 5.2 3D MOC tool (pp. 36–40)
Two cases, both with geometry generated by the 2D tool and the 3D result compared to the known 2D flowfield (p. 36):
1. **Mach 4 perfect nozzle** (pp. 36–38). 2D-tool generating parameters in Table 3 (p. 37): axisymmetric, perfect, M = 4.0, R_up/R* = R_down/R* = 1.0, throat-conditions box checked, P = 1000 psia, T = 530 R, MW 28.96, γ = 1.4, P_amb = 0, V = 3022 ft/s, θ_B guess 25, RRC above BD 100, DTHETAB 0.5°, 100 starting characteristics; resultant initial (3D input) Mach 1.15181 (p. 36). Fig. 40 (p. 37): wall Mach contours uniform at each axial station, as expected for a perfect nozzle. **Exit-plane statistics vs radial divisions (Table 4, p. 38)**:
   | Radial Divs | 18 | 36 | 72 |
   |---|---|---|---|
   | # points | 67 | 181 | 580 |
   | Avg exit Mach | 4.027 | 4.051 | 4.067 |
   | 3-σ deviation | 0.067 | 0.032 | 0.019 |
   | Avg % difference | 0.664 | 1.29 | 1.67 |
   All cases **over-predict** exit Mach; refining the grid *decreases scatter but increases mean bias* (pp. 37–38). Report's causal attribution (pp. 37–38): the 2D initial data line is an RRC (Z varies) while the 3D initial plane is vertical (Z = const) — an inlet-condition mismatch; plus amplification of small approximation/tolerance errors marching downstream.
2. **Mach 4 Rao nozzle** (pp. 38–40; same inputs but Nozzle Type = Rao). Figs. 42–43 (pp. 38–39): wall and centerline pressure traces, **APL 2D vs SEA RAO vs TDK vs APL 3D — "all the results compare favorably"** (qualitative; log-scale overlay plots, no error norms given). Fig. 44 (p. 39): exit-plane pressure comparison APL 2D vs TDK vs APL 3D (SEA RAO doesn't output exit profiles): "results are similar, however the **2D tool returns a discontinuous profile** which is different from the other two codes. It is unclear as to why this occurs and more investigation may be necessary." Mitigations stated: the 2D exit profile is computed *after* the contour is determined, so the anomaly has **no effect on the nozzle contour**; and it appears **only in the Rao case**, not the perfect nozzle (p. 39). Fig. 45 (p. 40): 3D Rao Mach contours.
- **No cone-flow (e.g., Taylor–Maccoll 10° cone) validation appears in the report.** Taylor–Maccoll is cited only as streamline-tracing background literature (Ref. 8, p. 41). If the repo contains a cone10 case for 3D_MOC, that validation is repo-side, not report-side. The report's cone content is limited to the Cone/Wedge design type (p. 13) and the cone contour in Fig. 39 (p. 36).

---

## 6. Stated limitations / failure modes (report's own words, collected)

**2D tool (MOC_Grid_BDE):**
1. Perfect-gas, inviscid only (p. 7); constant γ, MW (p. 14). No shocks — RRC crossing acknowledged as a *solution difficulty*, not a captured feature (p. 21).
2. Initial-line shape + Mach-1.5 cap "arbitrary", retained because "it has shown to work for many nozzle designs" (p. 19).
3. Hard-coded 2% mass-flow-mismatch kill switch (p. 16).
4. Convergence fragility for off-nominal R_down (recommend ≈ 1.0), too many/few starting characteristics, small R_up (pp. 19–21); errors in the initial region "get amplified as the solution progresses downstream" (p. 21).
5. Rao-case exit-plane pressure discontinuity, unexplained ("unclear as to why… more investigation may be necessary"), declared harmless to the contour (p. 39).
6. Planar performance = half-nozzle only (p. 10).

**STT2000:** design-condition-only validity; inviscid; BL assumed non-interfering (p. 6); mathematics not in this report (Refs. 1–2).

**3D tool (3D_MOC):**
1. Uniform initial plane only in the current input implementation (non-uniform inflow algorithmically possible, blocked by input design) (p. 33).
2. Isentropic/irrotational per construction (eqs. 16, 34–36, uniform totals); no shocks, no entropy layers (pp. 25, 30).
3. Wall cross-sections restricted to circles (eq. 17, p. 26) with local 4-primitive surface approximation (p. 31).
4. Surface-fit accuracy: 9-point TPS fit produced spurious nonuniformity; full-plane fit fixes it (cost: dense (N+3) solve per fit); better ACM algorithms identified but "none have been implemented to date" (p. 29).
5. Exit-Mach over-prediction growing with refinement (Table 4, p. 38), attributed to initial-plane mismatch + downstream error amplification (pp. 37–38).
6. Tool can "bomb" mid-march; diagnostic-dump workflow provided instead of a stability fix (p. 35).
7. Several GUI inputs are non-functional placeholders (p. 32).
8. Convergence tolerances "within some tolerance" — never quantified (pp. 30, 32).
9. Iteration of δ for wall-point feet P₃, P₅ "so that the points are within the nozzle flow region" — criterion not specified (p. 32).

---

## 7. CONNECTIONS to the host program (flags only; not adjudications)

**C1 — F6 3-D bridge / helical march demonstrator (strongest connection).** 3D_MOC (report §4, pp. 23–32) is a complete worked example of a **reference-plane bicharacteristic** 3-D MoC: inverse four-ray conoid stencil (eqs. 9–11, 21–24), conoid compatibility with cross-derivative terms (eqs. 15, 29–33), streamline energy closure (eqs. 16, 34–36), subset-averaging for overdetermination (p. 30), wall tangency closure (eqs. 38–40). This is precisely the third of the three canonical 3-D MoC families (bicharacteristics vs reference-plane vs near-characteristics) the plan's F6 literature slot (Ransom/Hoffman/Thompson) covers — Armstrong AEDC-TR-78-68 (Ref. 14, p. 40) is a locate-worthy primary source in the same lineage. Its **z-station marching organized around streamline projection + backward rays** is structurally the closest published analogue to a "helical march" through an annular RDE-like duct: what/where = eqs. 18–24 pp. 27–28; why = same plane-to-plane transport skeleton, with swirl entering only through nonzero ψ, θ distributions — which the report says the algorithm (not the input) already supports (p. 33).
- **Oracle/KAT potential**: the Mach-4 perfect-nozzle 3D case (Table 3 p. 37, Table 4 p. 38) is a *quantified* known-answer test: uniform-exit target M = 4.0 with published mean/3σ per grid (4.027/0.067 @18, 4.051/0.032 @36, 4.067/0.019 @72). A future 3-D march in the program could be run on the same 2D-designed contour and REQUIRED to beat these numbers (and to not reproduce the bias-grows-with-refinement pathology). If the repo's 3D_MOC executable still runs, it is an independent (non-GENO, non-JAX) cross-code twin for a 3-D demonstrator. Caveat for oracle use: the tool itself is isentropic-irrotational; usable as oracle only on isentropic test data, NOT on stratified RDE data.
- **Cone10 case** (mentioned in the task's repo context): NOT in the report (see §5 above). If present in repo outputs, Taylor–Maccoll (Ref. 8) supplies an exact solution for it — a legitimately independent oracle for any 3-D march — but its provenance must be established from the code/outputs, not this report.

**C2 — F2 three-family march (C+/C−/streamline transport).** The 2D tool's kernel/BDE machinery (pp. 7–10) is the standard *irrotational two-family* architecture; contrast object, not import. Two concrete flags: (i) the **mass-flow-matching closure across BD/DE** (p. 9) is exactly the control-surface mass-balance the program's extraction-surface logic generalizes; (ii) the **DTHETAB characteristic-insertion rule** (pp. 17–18) and the **R_down-dominates-convergence observation** (p. 21) are prior art for the program's step-size/insertion control choices (choice-ledger candidates, cheap to cite). Anti-flag: eqs. 2/4 fold the axisymmetric source into a (√(M²−1) ± cotθ) denominator — a form that degenerates near θ → 0 with r → 0 unless handled; the report is silent on axis treatment, so this is NOT a usable reference for the program's axis unit process.

**C3 — F5 stream-surface/extraction-surface data contract.** The streamline-tracing wall-insertion principle (pp. 5–6) with its explicitly named validity conditions (inviscid, design-point-only, BL non-interference) is the cleanest short statement in this literature cluster of the assumption set under which "trace a stream surface through a known field and call it a wall" is legitimate — directly relevant to F5's per-phase extraction surface and to any RDE-to-nozzle stream-surface hand-off. The report's own caveat (off-design needs high-fidelity modeling, p. 6) maps onto the program's cycle-averaged-vs-instantaneous adjudications.

**C4 — Transonic start line (F2 kernel entry).** Report documents the practitioner's Kliegel–Levine/Hall usage: toroid-coordinate analytic throat solution (p. 19, Ref. 13), wall-first line construction by successive RRCs, ad-hoc M ≤ 1.5 cap, and the quantitative 1/(R_up+1) velocity scaling with worked initial-line examples (Fig. 22, p. 20: M 1.44/2.2/1.50). Useful as an empirical-behavior benchmark for the program's own start-line model and as a named example of an *arbitrary* (self-declared) limiter the program's certified start line must NOT replicate uncredentialed.

**C5 — Rao design closure as cross-check.** Eq. 6 (p. 12), sin2θ_E = 2cotμ_E/(γM_E²) at zero back-pressure, is a one-line falsifiable relation any Rao-type optimal solution of the program (γ-const, uniform-inflow limit) must satisfy at the wall exit point — a cheap rejector-style invariant for the F2 engine's degenerate-limit tests, and the repo's M4 Rao case gives a concrete instance. Also: the report frames Rao entirely through the exit-condition closure, with zero variational machinery — a documented example of the "recipe Rao" the program's variational treatment supersedes.

**C6 — Thin-plate-spline cross-plane interpolation (F6).** Eq. 25–28 (pp. 28–29) + the documented 9-point-fit failure and its full-plane fix (p. 29) + the named-but-unimplemented ACM alternatives (Refs. 15–17) is a ready-made SOTA-survey seed (per the sota-library-survey directive) for the interpolation choice any reference-plane 3-D march must make; the failure mode (spurious azimuthal nonuniformity in a uniform field) is a rejector-test idea: uniform-field preservation as an interpolation-operator oracle.

**Anti-connections (explicitly NOT usable):** (a) no variable-γ, no stratification, no rotational MoC anywhere — the 3-D compatibility set (eqs. 15–16) assumes uniform totals, so it cannot twin the program's stratified F2/F5 marches; (b) no adjoint/sensitivity content; (c) no shock handling; (d) 2D tool's uniqueness claim for (θ_B, D) (p. 10) is asserted without proof — do not cite as a result; (e) STT internals absent (procure Refs. 1–2 if F5/F6 needs them); (f) the report's validation is largely self-consistency + qualitative overlay vs TDK/SEA-RAO — below the program's certificate bar, usable as sanity anchors only.

---

## 8. Fidelity ledger (derived vs empirical vs heuristic, as documented IN the report)

**Derived (with derivation delegated to a citation):**
- 2D compatibility relations eqs. 2–5 (pp. 8–9) — derivation in Ref. 11 (Moe & Troesch 1959).
- Rao exit condition eq. 6 (p. 12) — from Ref. 12 (Rao 1957).
- Kliegel–Levine transonic throat solution (p. 19) — Ref. 13.
- 3-D characteristic surfaces, bicharacteristic rays, conoid compatibility, cross-derivative closure, streamline relations: eqs. 7–16, 21–24, 29–36 (pp. 24–30) — Ref. 14 (Armstrong 1979), "majority of the explanation is echoed" (p. 23).
- TPS surface fit eqs. 25–28 (pp. 28–29) — small-deflection plate equation, derivation in Ref. 14.
- Wall tangency and geometry relations eqs. 37–40 (pp. 31–32).

**Empirical/calibrated (observed behavior, quantified in-report):**
- 1/(R_up+1) initial-line velocity scaling and line-shape sensitivity (p. 19, Fig. 22).
- Grid-convergence table for 3-D exit Mach (Table 4, p. 38) and the bias-vs-scatter trend (pp. 37–38).
- Default parameter set works "for most cases": θ_B guess 25°, DTHETAB 0.25–0.5°, ~100 starting characteristics, R_down ≈ 1.0, 36 radial divisions (pp. 16–18, 21, 33).
- 9-point vs full-plane surface-fit error observation (p. 29).

**Heuristic/arbitrary (self-declared or evidently ad hoc):**
- Initial-data-line shape rule + Mach 1.5 cap: "arbitrary… has shown to work" (p. 19).
- 2% mass-flow mismatch hard abort threshold (p. 16).
- Four-subset (field) / three-subset (wall) solution averaging to "increase accuracy" — Ref. 14 recommendation, no error analysis given (pp. 30, 32).
- Local wall approximation by 4 shape primitives (p. 31).
- δ-iteration for wall feet "within the nozzle flow region", unspecified criterion (p. 32).
- Unquantified convergence tolerances for point iterations (pp. 30, 32).
- Uniqueness of (θ_B, D) combination: asserted, unproven (p. 10).

**Report-internal defects worth flagging when cross-reading the code:**
- Eq. 35 as printed (ρ₂ = R T₂/P₂) is dimensionally inverted; the code presumably implements ρ = P/(RT) (p. 30).
- Text at p. 25 says compatibility comes from "eqs. 8-10" where eqs. 7–8 are the surfaces (minor numbering slip).
- §4.1.2.2 section number is used twice (field point p. 27, body point p. 30).
- Eq. 2's denominator sign convention vs eq. 4 (+cotθ vs −cotθ) should be verified against the code by the code-study agent (candidate transcription hazard).
- Report names the streamline tool STT2000 throughout; repo folder says STT2001 — version increment undocumented in this report.

## References of record cited by the report (pp. 40–41, complete list)
1. Rice & VanWie, AATDL-00-033, JHU/APL, Feb. 2000 (RBCC-Trailblazer nozzle; STT provenance). 2. Rice, RTDC-TPS-335, May 2001 (RBCC-GTX nozzles; STT provenance). 3. Anderson, Fundamentals of Aerodynamics, 1984. 4. VanWie & Molder, AIAA-92-1210. 5. Nonweiler, JRAeS 67, 1963. 6. Maikapar, Fluid Dynamics 1(1), 1966 (stream-surface bodies of conical flows). 7. Rassmussen, JSR 17, 1980. 8. Taylor & Maccoll, Proc. Roy. Soc. A319 [sic; actually A139], 1933. 9. Bowcutt/Anderson/Capriotti, AIAA-87-0272. 10. Corda & Anderson, AIAA-88-0369. 11. Moe & Troesch, STL TR-59-0000-00661, May 1959 (2D MoC finite differencing). 12. Rao, Marquardt, ARC meeting June 1957 (optimum thrust contour). 13. Kliegel & Levine, AIAA J. 7(7), 1969, 1375–1378 (transonic throat). 14. Armstrong, AEDC-TR-78-68, Jan. 1979 (3-D MoC internal flows — the 3D tool's backbone). 15. Renka, ACM TOMS 25(1), 1999, Algorithm 792. 16. Renka, ACM TOMS 25(1), 1999, CSHEP2D/Algorithm 790. 17. Akima, ACM TOMS 22(3), 1996, Algorithm 761.
Acknowledgements (p. 41): DeBonis, Georgiadis, Smith, Trefny (GRC); Rigling (APL); special thanks to W.C. Armstrong.

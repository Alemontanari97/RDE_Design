# REFUTE — adversarial check of `digest_repo_3DNozzleCode.md`

Target: `NASA_STUFF_Nozzle_Inlet/digest_repo_3DNozzleCode.md` (repo digest of `Three-Dimensional-Nozzle-Design-Code`, master @ 09ba559).
Method: every claim re-read at the cited file:line (Read with offset/limit + Grep), plus two empirical checks against shipped outputs that the digest did not run (start-line recomputation, `_AvsX.out` station census). No file in the repo was modified. All paths relative to `Three-Dimensional-Nozzle-Design-Code/`. Date 2026-08-31.

Verdict scale: CONFIRMED (code supports the claim as stated) / PARTIAL (core right, an anchor or qualifier wrong) / REFUTED (code contradicts the claim) / UNVERIFIABLE.

---

## 1. Structural claims S1–S8

| # | Claim | Verdict | Evidence |
|---|---|---|---|
| S1 | 3D_MOC initial plane = uniform-state circular disc (single p,T,M,θ,ψ), dialog default M=1.1; 2D FLOW never ingested, only wall via `.geo` (z r0 x0 y0) | **CONFIRMED** | `3D_MOC/3D_MOCGrid.cpp:257` `geomFile >> z0 >> r0 >> x0 >> y0` is the only geometry read; `:266` calls `SetInitialReferencePlane` once (k==0,j==0); `:1489-1497` assign the same `pres,temp,mach,gamma,mWt,theta,psi` to every `_pt[k][0]`; `3D_MOCDlg.cpp:71` `m_mach0 = 1.1`, `:74` p=1000, `:76` T=530. `OnexeBUTTON` (`3D_MOCDlg.cpp:230-231`) passes only these scalars + `m_geomFile`. Shipped `outputs_cone10/z=0.out` and `outputs_M4Perfect/z=0.out`: every row P=1000, T=530, Mach=1.1, Theta=Psi=0 (rows 2-30 read; formats differ — cone10 lacks the `Radius(in)` column, i.e. older build). |
| S2 | Header names Armstrong AEDC-TR-78-68 + "reference plane method"; field points: 4 bicharacteristics, average of 4 triplet solutions; body points: NR `newt`, average of 2 pairs with `n=2` | **CONFIRMED** | `3D_MOCGrid.cpp:23-28` verbatim; `:1259` `PTN[4][3] = {0,1,2, 1,2,3, 2,3,0, 3,0,1}`, `:1277` loop j<4, `:1314` `X.dSx[i] /= 4.0`; `:1339` `const int n=2, pt[3][2] = {0,1,0,2,1,2};` (three pairs declared, two used), `:1385` `NR::newt(x,check,funcv)`, `:1409` `/= double(n)`; `:1337-1338` author note "I tried varying all of the points and the results are the same". |
| S3 | STT2001 has NO velocity-field integration; parses `MOC_SL.plt` iso-ψ streamlines and interpolates/lofts; throat constraints are circles only | **CONFIRMED** | Grep `Runge|rk4|odeint|Fehlberg|Deriv\(|integrat` (case-insens.) over `STT2001/`: only two GUI strings (`STT2001Dlg.cpp:786` "Integrating nozzle pressures.", `:2207` mismatch message) — no integrator. `thsl[][]` (flow angle) is stored (`:1010`) and freed (`:1257`) but never used to advance a point; the only `tan`/`atan` uses are geometric (`:1942, 2652-2653, 2677`). Loft = pure interpolation `:1081-1143` (`dr` blend `:1088`, resample of SL i-1 `:1123-1128`, placement `:1140-1142`). Circle constraint `:1073-1074` and `:1311` `r = sqrt((yt-yc)^2+(zt-zc)^2)`. Anchors `GetSLData` `:918`, `CalcThroatSLs` `:1024` correct. |
| S4 | NR sources vendored in `3D_MOC/`; license.txt = NOSA 1.3 / LEW-20180 | **PARTIAL** | Files present (`newt.cpp, lnsrch.cpp, ludcmp.cpp, lubksb.cpp, fmin.cpp, sort2.cpp, nr.h, nrtypes.h, nrtypes_nr.h, nrutil.h, nrutil_nr.h`). NR identity is established **by idiom, not by notice**: no NR copyright text anywhere (grep `Copyright` in `3D_MOC/*.{cpp,h}` = 0 hits); idioms: `ludcmp.cpp:7` `TINY=1.0e-20`, `:18` "Singular matrix in routine ludcmp"; `lnsrch.cpp:10` `ALF=1.0e-4`; `newt.cpp:12-13` `MAXITS=200, TOLF=1.0e-8, TOLMIN=1.0e-12, STPMX=100.0`; `nrutil_nr.h:51` "Numerical Recipes standard error handler", `:49` `namespace NR`. Qualifier the digest missed: `nr.h` is the **NR-in-C (2nd ed.) header** (`float` C prototypes, `#if defined(__STDC__)`, `nr.h:25-38`) while `nrtypes_nr.h/nrutil_nr.h` are NR-in-C++ headers — a mixed vintage; `newt.cpp:38-40` is Rice-modified (analytic `funcvDeriv` replaces `fdjac`). License: `license.txt:1` "NASA OPEN SOURCE AGREEMENT VERSION 1.3", `:15` "LEW-20180", `:18` POC heath.reising@nasa.gov — confirmed; note `:194-196` NOSA disclaims third-party software "if present". |
| S5 | Sponsorship strings; "CONGO-2D" | **CONFIRMED** | `MOC_Grid_BDE/MOC_GridCalc_BDE.h:21` "FG888BXX (NASA GRC PDE Work)"; `3D_MOC/3D_MOCGrid.hpp:21` "FG800XXX (NASA GRC Nozzle Work)"; `MOC_GridCalc_BDE_IO.cpp:22` "FG1CAXXX (URETIS)"; `:55` "Summary output file for CONGO-2D". |
| S6 | Rao eq.14 form at 1541-1543/1589-1591/1719-1721; start line from `KLThroat` 3103-3178; `Sauer` dead (call commented 2847); `CalcHallLine` never called; γ per node never varied | **CONFIRMED** | `:1541-1542` `thetaCalc = 0.5 * asin(2*(pres[0][j] - pAmb)*144 / ( rho[0][j]*w0*w0 * tan(CalcMu(mach[0][j]))))`; identical form at `:1589-1590` and `:1719-1720` on `dS.dSx[11],[13],[16],[9]`. `KLThroat` `:3103-3178` with the Kliegel–Levine/Hall attribution `:3105-3108`. `:2847` `//		if (!tFlag) Sauer(i,geom,rUp);`. `CalcHallLine`: grep shows only the definition `:2905`, declaration `.h:118` and a stale comment `:2822` — no call. γ: all 26 `gamma[..][..] =` assignments (grep) are copies/interpolations of existing nodes or of the input `g` (`:644, 2780, 2837`) or of `gammaD/gammaE` derived from the same field (`:1908, 1968, 2090, 2203`); no thermodynamic update anywhere. |
| S7 | `rao.dat` TDK WALL_TBL.50 comment; M3.5Perf numbers eps=6.73651, L/R*=12.5363, CD=0.984756, θB=15.2196°, Isp_vac=69.9496 | **CONFIRMED** | `MOC_GridCalc_BDE_IO.cpp:674-677` "used by TDK99 as the inviscid nozzle contour file. If you were used RAO, this file would be called WALL_TBL.50"; `outputs_M3.5Perf/summary.out:440` `Expansion Ratio: 6.73651`, `:439` `Nozzle Length/R*: 12.5363`, `:165` `CD(2-D/1-D): 0.984756`, `:167` `ThetaB(deg): 15.2196`, `:503` `Isp (lbf-s/lbm): 69.9496`, `:505` `Cfg: 0.699496`. (What these numbers are worth is a different matter — see §3.) |
| S8 | 2% mass-flow guard ~1085-1089; conCrit=1e-10 (~62); 1000-iteration cap + 5e-4 fallback (~2643-2654) | **CONFIRMED** | `:1085` `if ( fabs(mdotErr) > .02)`, `:1088` `return -999019`; `:62` `conCrit = 1e-10`; `:2564` `... && k++<1000 && M[3] >= 1.0`, `:2643` `if ( k == 1001 || M[3] < 1.0)`, `:2645` `if ( minMErr <= 5e-4)`, `:2642` "1001 Iterations is good, do not change". |

**Extra structural claim attacked (digest §4.4 step 3 and §4.6, lines 145/160): "TPS over the point + its 8 nearest neighbors (default)".** **REFUTED on the default.** The dialog default is `m_SurfaceFit = _T("All Point Spline")` (`3D_MOCDlg.cpp:86`); `CalcNozzle` runs `AllPointSurfaceFit(k-1)` when `sFit == "All Point Spline"` (`3D_MOCGrid.cpp:143`), and the 9-point local fit is invoked only when `sFit == "9 Point Spline"` (`:388` field, `:599` body); the derivative branch `:1615` is labelled `else // All Point fit`. So under the shipped default every base-point state comes from a *global* TPS over all plane points (N+3 square LU per plane; N=181 for nDiv=36, r0=1: rings of 1+8+13+19+26+32+38+44 points, matching `z=0.out`). Which option produced the shipped sample outputs is not recorded in any output file — UNVERIFIABLE; the digest's remark about "TPS stencils across the polar singularity" should be re-stated for the global fit.

---

## 2. Bug census B1–B12

Magnitude class: **LEADING** (changes shipped numbers at the 1e-2..1e-1 level), **SECONDARY** (1e-3..1e-2), **INERT** (no effect on shipped outputs / dead path), **COSMETIC** (output-only, dead variables), **HANG** (control-flow only).

| # | Anchor | Quoted line | Digest reading | Verdict | Effect on results |
|---|---|---|---|---|---|
| B1 | `MOC_GridCalc_BDE.cpp:3124` | `... + z*(y*y - 5/8) - (2*G - 3)*z*z/6;` | integer division 5/8 → 0 | **CONFIRMED BUG** | **LEADING** in the AXI start line (see §3: −0.154·z in u2, weighted ½ at R_S=1). Same idiom in dead `CalcHallLine:2921` (`5/8`) and `:2938` (`15/8`, contrast `KLThroat:3139` which correctly writes `15./8.`). |
| B2 | `:3146` | `u[1] = 0.5*y*y - 1/6 + z;` | 1/6 → 0 | **CONFIRMED BUG** | **LEADING for the 2D-planar branch** (u1 loses the constant 1/6, enters U at 1/R_S — 17% at R_S=1); the planar branch is exercised by none of the shipped samples (all AXI). Contrast the AXI line `:3122` which writes `0.25`. |
| B3 | `:3129` vs `:2926` | `z*((52*G*G + 51*G + 327)*y*y*y*y/34 - ...` vs `CalcHallLine:2926` `.../384*r*r*r*r` | /34 should be /384 | **CONFIRMED BUG** (in-repo evidence) | **LEADING**: alone it inflates U by 0.116 at mid start line in the shipped M3.5Perf case (§3). Also confirmed structurally: the z²-term coefficient `/192` at `:3134` equals ½·d/dy of a `/384·y⁴` term, not of `/34`. |
| B4 | `:3133` vs `:2927-2932` | `z*((556*G*G + 1737*G + 3069)*y*y*y*y*y/1728 * (388*G*G + 1161*G + 1181)*y*y/576 + ...` | `*` where `−` belongs; 1181 vs 1881 | **PARTIAL → both defects real, one citation wrong** | `*`→`−`: CONFIRMED by `CalcHallLine:2931` which has `- (388*g*g+1161*g+1181)/576*r*r*r`. 1181→1881: `CalcHallLine:2931` **also** says 1181, so the digest's "compare :2927-2932" does *not* evidence it; the valid argument is structural (digest's other citation `:3133 vs :3127`): the v3 z-term polynomials are exactly d/dy of the u3 z⁰-term polynomials (denominators 10368→1728, 2304→576, 1728→864 = ÷6,÷4,÷2 for y⁶,y⁴,y² derivatives), so the middle polynomial must be `388G²+1161G+1881` as at `:3127`. Same `*`-for-`−` at `:3157` (2D branch) CONFIRMED by the same structure. **Magnitude: LEADING on the flow angle** — at the i=40 point the `*` term alone shifts v3 by ≈0.45 → V by ≈0.044 → θ by ≈1.8°. |
| B5 | `MOC_GridCalc_BDE_IO.cpp:156` | `<< (1-mdotErrRatio)*100;` | never assigned | **CONFIRMED BUG** | **COSMETIC**: repo-wide grep = 2 hits (`.h:92` declaration, `_IO.cpp:156` use); `summary.out:168` prints `100` (member reads as 0). The field "Massflow error due to grid at end of Kernel (%)" is meaningless in every shipped summary. |
| B6 | `MOC_GridCalc_BDE.cpp:508` | `while (dS.dSi[2] == SEC_FAIL_LOW \|\| dS.dSi[2] == SEC_FAIL_HIGH && i++ < 20)` | precedence: cap applies only to HIGH | **CONFIRMED BUG** | **HANG-class, not result-affecting**: loop bisects `[thetaBMin,thetaBMax]` (`:512-515`); a persistently LOW `CalcLRCDE` stalls at thetaBMax forever unless `CalcRRCsAlongArc` returns −999019 (`:522, 534`). No wrong number is produced. |
| B7 | `:1485-1486, 1742-1743` | `... xDLast, xDMaxBisect; double xDMinBisect;` / `if ( param_err[2] < 0.0) xDMaxBisect = xD[2]; else if (...) xDMinBisect = xD[2];` | computed, never used | **CONFIRMED** | **COSMETIC** (grep: 4 hits, all declaration/assignment; the bisection fallback announced at `:1740-1741` was never wired). |
| B8 | `STT2001Dlg.cpp:1378-1379` | `if ( k < nparamGRIDX/2) xgrid[n][k] = (x1+k*(x3-x1))*m_RSL/((nparamGRIDX-1)/2) + m_XSL; else xgrid[n][k] = (x3+k*(x2-x3))*m_RSL/((nparamGRIDX-1)/2) + m_XSL;` | divides whole coordinate by (N−1)/2 | **CONFIRMED BUG — empirically verified** | **LEADING for STT2001 outputs**. `x1 = min x` (`:976,1013`) ≈ 0 so the first half accidentally works; the second half yields x ≈ 0.687·x2 … 1.35·x2 (also `(nparamGRIDX-1)/2` is integer 49). Shipped `STT2001/outputs_M3.5Perf/M3.5Perf_AvsX.out`: stations 1-49 span x=0.085…4.179 (first third of 12.536), station 50 jumps to **8.613** (=0.687·12.536 exactly as predicted), stations 73-100 are 27 duplicates at 12.5363. The band 4.18–8.61 (a third of the nozzle) has **no stations**; pressure force jumps 433.7→522.2 across it. All downstream STT numbers (`_STT_summary.out` pressure force 531.764, Isp) are computed on this grid. |
| B9 | `3D_MOCGrid.cpp:1232, 1235` | `ax = -2*(fa[2] + (fb[2] + fc[2]*P.z*P.z))/ax;` / `by = -2*(fa[4] + (fb[4] + fc[3]*P.z)*P.z) / by;` | missing paren; fc[3] should be fc[4] | **CONFIRMED as code, INERT for shipped inputs** | Pattern at `:1224-1225,1230,1233` is `(fb + fc*P.z)*P.z` and `fc[4]` pairs with `fa[4],fb[4]` — both transcription errors are real. But `ax,by` feed only the sign choice of n2,n3 (`:1237-1240`), and this branch (`continue27`, `:1163-1241`) is reached only when a neighbouring plane's fit is not CIRCLE (`:1107,1112`). `BodyFit` (`:1862-1929`) classifies with exact `==` tests, so a circular section always returns CIRCLE; with circular `.geo` input (the only kind `SetInitialPropertiesForCircularThroat` can read) the branch is dead. |
| B10 | `:689` | `if (newJK.dSi[0] != unitNormal2.dSi[0] && newJK.dSi[1] != unitNormal2.dSi[1])` | should be `\|\|` | **CONFIRMED as written; effect INERT for circular sections, AMBIGUOUS in general** | With `&&`, a j-only change skips `BodyFit(P2)` (`:692`). For a circular section any 3-point `BodyFit` returns the same circle, so the skipped refit changes nothing; k cannot change because P2.z is fixed on plane k. Would matter for genuinely non-circular walls, which the code cannot ingest. |
| B11 | `:2769` vs `:1682, 1698` | `_nZ++;` vs `new XYZPoint[_nZ*5]` | ≥4·nZ insertions overflow silently | **NOT A BUG in practice** | `failCounter` in `CalcNozzle` is a single run-wide counter never reset, and every insertion path requires `failCounter < 15` (`:152, 162`), so `_nZ` grows by at most 15; `_nZ*5 ≥ _nZ+15` whenever `_nZ ≥ 4` (`3D_MOCDlg.cpp:73` default 11; shipped .geo 162/217 planes). The digest's overflow condition is unreachable. |
| B12 | `:58, 74-75` | `if ( f[i] > -1e-10 && f[i] < 1e-10) f[i] = 0.0;` / same on `f[i][j]` | flush-to-zero can singularize `ludcmp` | **CONFIRMED as written; COSMETIC** | `newt` converges at `TOLF=1e-8` (`newt.cpp:13`) ≫ 1e-10, so the residual flush is invisible; Jacobian entries are compatibility coefficients (a0 ≈ 144/(tanβ·ρq²/g) ~ 1e-3 in²/lbf, a1,a2,normals O(1)), far above 1e-10. A singular matrix from the flush would need a genuinely ≈0 entry that is also structurally needed — not shown; `ludcmp` would then use `TINY` (`ludcmp.cpp:47`), not crash. |

**Additional defects found (not in the digest):**

| # | Anchor | Line | Finding | Class |
|---|---|---|---|---|
| N1 | `MOC_GridCalc_BDE.cpp:3148` | `u[2] = (y+6)*y*y*y*y/18 - (2*G+9)*y*y/18 + ...` | `(y+6)` must be `(G+6)`: the paired v2 z-term at `:3149` is `(2*G+12)*y*y*y/9 = d/dy[(G+6)/18·y⁴]`, exactly the u↔v derivative pattern that holds for every other term pair in both branches. 2D-planar branch only. | LEADING (planar) |
| N2 | `:3158` | `... - (26*G*G + 51*G + 189)/144) + ...` | missing `*y` (the AXI analogue `:3134` has `- (52*G*G + 75*G + 279)*y/192`; structurally ½·d/dy of `:3152`'s `(26G²+51G+189)*y*y/144` is `(…)*y/144`). 2D-planar branch only. | LEADING (planar) |
| N3 | `3D_MOCGrid.cpp:152-157` | `if (!CalcFieldPoint(i,k-1, dz) && failCounter < 15) {...}` | After the 15th insertion a **field-point FAIL (base point outside the wall, `:446-449`) is silently ignored** and `_pt[i][k]` is left unset; body points in the same state abort (`:170-174`). Asymmetric, silent. | INERT unless ≥15 failures |
| N4 | `MOC_GridCalc_BDE.cpp:2853-2860` | `while (mach[i][0] > 1.5) { ... KLThroat(...); drdx *= 2.0; }` | The M≤1.5 guard is **active for 48 of the 101 shipped start-line points** (`summary.out:100-147`, i=53…100 all at M=1.492–1.500, x≈0.72 nearly constant): the inner half of the initial data line is guard-generated, not Kliegel–Levine. Cause = the B1/B3/B4 inflation of U (§3). The Rice report's own "M = 1.50 with constraint" for R_up/R*=1 (see `digest_Rice2003_RTDC-TPS-481.md:33`) shows the author's runs carried the same artefact. | LEADING |

---

## 3. Key refutation: the KLThroat defects are LEADING-ORDER in the shipped sample, not "third order"

Digest §2.3 (line 46): "These pollute only third-order terms (and one second-order term via 5/8), so results remain plausible"; §6.1 (line 195): "Oracle value: high … treat as a ~1e-3-to-1e-4-class oracle". **Both REFUTED** by recomputation against `outputs_M3.5Perf/summary.out` (R_S = RWTU = 1 ⇒ RSP = 2, γ = 1.4).

Point i=40 (`summary.out:87`): x/R* = 0.270589, r/R* = 0.727673, printed M = **1.39809**, θ = 7.66209°.
z = x·√(2R_S/(γ+1)) = 0.24702 (`:3120`); y² = 0.529508, y⁴ = 0.280379, y⁶ = 0.148463.

| Term | as coded (`:3122-3139`) | with `/384` only (B3, in-repo evidence) | with `/384` and `5/8=0.625` (B1+B3) |
|---|---|---|---|
| u1 | 0.261774 | 0.261774 | 0.261774 |
| u2 | 0.062721 (5/8→0) | 0.062721 | −0.091667 |
| u3 | 1.001557 (z-term /34 = +0.9178) | 0.072703 | 0.072703 |
| U = 1 + u1/2 + (u1+u2)/4 + (u1+2u2+u3)/8 | **1.385608** | 1.269501 | 1.192307 |
| M = √(U²+V²), V = U·tan θ_printed ≈ 0.186 | **1.39809** (printed 1.39809) | ≈1.283 (−8.2%) | ≈1.207 (−13.7%) |

The as-coded column reproduces the shipped value to 5 significant figures, proving the sample was produced by exactly these lines. The wall point i=0 (x=0 ⇒ z=0) is immune — recomputation gives U = 1.177791 vs printed **1.17779** (`summary.out:47`) — which validates the z⁰ coefficients as transcribed and explains why the table "looks right" at the wall while being 8-14% high in Mach mid-line and clamped at M=1.5 (N4) over the inner half. The `*`-for-`−` in v3 (B4) adds an O(2°) flow-angle error at the same point.

Consequences for the digest's oracle claims:
- `CD(2-D/1-D) = 0.984756` (`summary.out:165`) is the mass flux integrated over this corrupted+clamped line — it must **not** be compared with the Kliegel–Levine discharge-coefficient series (digest §6.1(b)).
- θB = 15.2196°, eps = 6.73651, L/R* = 12.5363 and the contour are the *correct MoC consequence of a wrong initial data line*; they are not KL-consistent perfect-nozzle numbers.
- **Salvage**: the 101-point initial data line is printed in full (`summary.out:46-147`: x, r, M, θ, p, T, ρ, γ, ψ). A host 2D MoC that ingests that exact line as its IDL can still use the shipped kernel/contour/DE line as an **IDL-conditional** oracle of the march + perfect-nozzle construction. Expected agreement class is then set by the unit-process schemes (tangent-averaged, conCrit 1e-10), not by start-line physics.
- Digest §7.1-6 ("second independent KLThroat implementation … fix the bugs before using") stands, but the fix list must include N1/N2 for the planar branch, and the 1181→1881 correction cannot be validated against `CalcHallLine` (which shares it).

---

## 4. Buildability / runnability today (oracle regeneration)

| Item | Finding | Anchor |
|---|---|---|
| Project files | **Only** `STT2001/STT2001.dsw` (VC6 "Format Version 6.00") exists, and it references `.\STT2001.dsp`, which is **absent**. No `.dsp/.vcproj/.vcxproj/.sln` for any of the three tools (glob over the repo). `.rc` + `resource.h` present for all three; `3D_MOC` has **no `StdAfx.cpp`** (the other two do). | glob; `STT2001.dsw:1,6` |
| Toolchain | MSVC + **MFC** mandatory (`AfxMessageBox`, `CString`, `CWinThread`, DDX, `AfxBeginThread` `3D_MOCDlg.cpp:226`); MSVC-only calls `_finite` (`3D_MOCGrid.cpp:1605,1622`), `_getdcwd` (`MOC_GridDlg.cpp:699`). `MOC_Grid_BDE` carries an OLE-Automation proxy (`DlgProxy.*`, `MOC_Grid.odl`) with MIDL outputs committed (`MOC_Grid_h.h:37` `_MSC_VER >= 1020`, `MOC_Grid_i.c`). | cited lines |
| Evidence it compiled recently | "Tharen Rice May 2020" edits: `<fstream>` migration (`MOC_GridCalc_BDE.cpp:33`), C2440 fix (`3D_MOCGridThread.cpp:55-57`, `.h:26`), worker-thread bypass so `CalcNozzle` runs synchronously (`3D_MOCDlg.cpp:233-235`, `3D_MOCGridThread.cpp:46-49`), STT parser rewrites (`STT2001Dlg.cpp:2981`). So the code built on a 2020-era VS — but the project files that did it were not committed. | grep "May 2020" (24 hits) |
| Binaries | None shipped (glob `*.exe/*.dll/*.lib/*.obj` = 0). `MOC_GridDlg.cpp:706,725` hardcodes `..\STT2001\STT2001.exe` via a generated `$$.bat`. | — |
| Batch/CLI entry | None. All three are dialog apps; inputs typed in the GUI (STT2001 additionally loads `.inp`, `readme.txt`). Oracle regeneration = manual GUI runs. | `STT2001/readme.txt`, `MOC_Grid_BDE/readme.txt` |
| NR header mixture | `nr.h` (NR-in-C float prototypes) is included by `3D_MOCGrid.hpp:35` and the NR `.cpp`s; `NR::` namespace lives in `nrutil_nr.h:49`. Whether this mixture compiles as-is could not be checked without a build — UNVERIFIABLE. | cited |

**Verdict:** buildable with ~1 day of project reconstruction (three MFC dialog projects, add sources, synthesize `3D_MOC/StdAfx.cpp`, decide whether to keep the MOC_Grid automation proxy), but (i) there is no batch entry, (ii) a rebuilt binary regenerates the **same defective numbers** unless B1/B3/B4/N1/N2/B8 are patched first, and (iii) any patched build is no longer "the shipped code" — the shipped outputs stay the only unambiguous oracle currency, with the §3 caveat on what they are oracles *of*.

---

## 5. Method-relevant omissions in the digest

1. **Default surface fit inverted** (§1, extra claim): the shipped default is the global "All Point Spline"; the 8/9-point local TPS is opt-in. Cost model (O(N²logN) per plane in digest §4.6) and the "polar-singularity stencil" remark describe the non-default path.
2. **Start-line clamp artefact (N4)**: half of the shipped IDL is the M≤1.5 guard, not KL — this is the actual mechanism behind the report's "constraint" remark and behind the "inlet-condition mismatch" the report blames for 3D-vs-2D bias (`digest_Rice2003:128`): the 2D IDL is itself corrupted.
3. **Two more planar-branch typos (N1, N2)** — any use of the TWOD KLThroat as a cross-check is unsafe without them.
4. **Field-point silent continue after 15 failures (N3)** — the "≤15 retries then abort" description (digest §4.5) holds only for body points.
5. **Third-party code beyond NR**: `Chart.cpp/Chart.h` (MOC_Grid_BDE, STT2001) and `Chart3d.*` (STT2001) are by Kris Jearakul ("Use with your own risk !!", no licence, `Chart.h:2-4`, `Chart3d.h:2-4`); digest §5 lists only NR and calls the STT2001 helpers self-written (true only for `Matrix/Vector`).
6. **B8 is empirically visible in a shipped file** (`M3.5Perf_AvsX.out`), so the STT2001 M3.5Perf fixture (digest §6.2 "Oracle value: moderate … reproducible to 0.1%") is a fixture of a mis-gridded integral; the internal 0.1% cross-check (`STT2001Dlg.cpp:2203-2207`) compares two loop orders over the *same* wrong grid and cannot detect it.
7. **1181 vs 1881**: the defect is shared by `CalcHallLine`, i.e. inherited from a common transcription source — the digest's "compare :2927-2932" for this item is wrong (right for the `*`).

---

## 6. Counts

- Structural S1–S8: **7 CONFIRMED, 1 PARTIAL (S4: NR by idiom only; nr.h is the C header), 0 REFUTED**; extra structural claim (default stencil) **REFUTED**.
- Bug census B1–B12: **CONFIRMED result-affecting 5** (B1, B2[planar], B3, B4, B8), **CONFIRMED cosmetic/hang 4** (B5, B6, B7, B12), **CONFIRMED-as-code but INERT for shipped inputs 2** (B9, B10), **NOT A BUG in practice 1** (B11).
- New defects: **4** (N1, N2, N3, N4).
- Digest fidelity statements REFUTED: 2 (§2.3 "third-order/plausible"; §6.1 "~1e-3–1e-4-class oracle, value high"), with a named salvage (IDL-conditional oracle).

# AUDIT SDTOOLBOX UFFICIALE — zip Caltech (release "Updated April 2026") vs stack RDE/CVA

*Audit rigoroso multi-prospettiva, a convergenza — 2026-07-09.*
*Riferimento ufficiale: `SDToolbox.zip` → `project_build/sdt_official/SDToolbox/` (Python3/sdtoolbox 13 file, Python3/demo 49 demo, data/ ~33 meccanismi + MATLAB). Report: Kao, Zeigler, Bitter, Schmidt, Lawson, Shepherd, GALCIT FM2018.001 (2023) = `ShockDetonation.pdf` (già in cartella; estratto testuale in `project_build/tmp_sk/ShockDetonation.txt`).*
*Nostro stack: `project_build/sdtoolbox/` (vendored, 5 moduli) = `rde-lecture-code/sdtoolbox/` (verificati identici, `diff -rq`), script in `project_build/scripts/` e `rde-lecture-code/src/`.*

**Metodo.** Quattro prospettive indipendenti fatte convergere: (1) diff statico riga-per-riga dei moduli; (2) esecuzione incrociata runtime (stessa fisica, due codebase, stesso Cantera 3.2); (3) spot-check numerici su meccanismi alternativi della zip; (4) chiusura formale su report + demo. Ogni claim ha citazione (file:riga o pagina) e numero misurato.

---

## 1. DIFF CODICE — vendored vs ufficiale

### 1.1 Perimetro

| modulo ufficiale (Python3/sdtoolbox) | nel nostro vendored? | usato dai nostri script? |
|---|---|---|
| `postshock.py` (563 r.) | SÌ (204 r., subset) | SÌ (`CJspeed`, `PostShock_eq`, `PostShock_fr`) |
| `thermo.py` (275 r.) | SÌ (47 r., subset) | SÌ (`soundspeed_eq`; `soundspeed_fr` via znd) |
| `znd.py` (320 r.) | SÌ (107 r.) | SÌ (`zndsolve`) |
| `config.py` | SÌ | SÌ (ERRFT/ERRFV/volumeBoundRatio) |
| `reflections.py`, `stagnation.py`, `cp.py`, `cv.py`, `utilities.py` | NO (scelta dichiarata) | NO (grep completo import: solo CJspeed, PostShock_eq/fr, soundspeed_eq, zndsolve) |

### 1.2 Diff funzione per funzione (solo differenze FUNZIONALI; il cosmetico è ignorato)

**postshock.py — IDENTICO all'ufficiale** per: `LSQ_CJspeed` (stesse somme e formule del fit parabolico), `FHFP`, `CJ_calc` (T₀=2000 K, w₀=2000 m/s, perturbazioni 2%, limiter |ΔT|≤0.2T, cap 500 iter), `CJspeed` (**stesso algoritmo minimum-wave-speed**: sweep di 21 punti sul rapporto di densità con bounds iniziali [1.5, 2.0], fit parabolico ai minimi quadrati, minimo dnew=−b/2a, raffinamento bounds ±0.1% e ripetizione finché R²≥0.99999 con ≥4 sweep; tolleranze ERRFT=ERRFV=1e-4), `PostShock_fr`, `PostShock_eq` (incluso il workaround `len(q)>1`), `shk_calc`, `shk_eq_calc` (guess volumeBoundRatio=5, limiter ΔV: 0.5(V1−V) se V2X>V1 altrimenti 0.2V). Assenti (non usate da noi): `hug_fr`, `hug_eq` (servono solo alle demo di plotting dell'Hugoniot, es. demo_RH*).

**thermo.py** — `soundspeed_eq` **IDENTICA** (metodo TP robusto dell'Appendice G2: 6 equilibrate('TP'), identità DTDP=−DSDP/DSDT, differenze centrate ±1%; restore finale TPX). `eq_state`/`state` identiche. Assenti (non usate): `gruneisen_eq`, `gruneisen_fr`.
**UNICA PATCH FUNZIONALE (nota e ora quantificata)** — `soundspeed_fr`:
- ufficiale (`thermo.py:118-156`): differenza finita one-sided lungo l'isentropa congelata, ρ→1.001ρ via `SVX`;
- nostro (`sdtoolbox/thermo.py:20-24`): `return gas.sound_speed` (Cantera, analitico √(γ_fr R T/W̄), gas ideale) — ~100× più veloce; la versione ufficiale è conservata come `_soundspeed_fr_fd` (righe 26-39).
- **Misura**: |a_FD − a_analitico|/a = 9.8e-5 (reagenti H2/air), 7.6e-5 (stato vN), 5.9e-5 (stato CJ) — è il bias di troncamento O(Δρ) della FD one-sided, ≈(γ−1)/4·10⁻³. **Effetto end-to-end su ZND** (unico consumatore): ufficiale vs nostro su H2/air a U=1969.0, gri30, stessi input → L_ind 0.24460 vs 0.24456 mm (**0.016%**), L_exo 0.05413 vs 0.05414 mm, M_end 0.9253 vs 0.9255. **Patch matematicamente equivalente, impatto ≤0.02% (sotto ogni tolleranza dichiarata).**

**znd.py** — `ZNDSys` (ODE in [P, ρ, x, Y] con η=1−M², M=U/a_fr, σ̇ termicità), `getThermicity`, `getTempDeriv`, `zndsolve` (LSODA, rtol 1e-5, atol 1e-8 default, stesso post-processing e stesso criterio sonico `sonic=η·a_fr²`) **IDENTICI**. Unica differenza: il nostro omette le stampe di warning "eigenvalue detonation" per n==0/n==b nel ramo advanced_output (sola diagnostica; i valori calcolati sono gli stessi). Nota a margine sull'ufficiale: il ramo `if n == b:` (znd.py:254) è dead code (argmax ∈ [0, b−1]) e se mai eseguito farebbe IndexError su `output['M'][b]` — bug latente ufficiale, non ci riguarda.

**config.py** — valori identici (ERRFT=1e-4, ERRFV=1e-4, volumeBoundRatio=5).

### 1.3 Prova runtime di identità
Nostro vendored + `Mevel2017.yaml` alle condizioni esatte di `demo_CJstate.py` (H2:2 O2:1 N2:3.76, 100 kPa, 295 K) riproduce l'output ufficiale **cifra per cifra**: U_CJ=1968.5, P₂=1.5709e6 Pa, T₂=2939.3 K, ρ₂=1.537, w₂=1092.1, a_eq=1090.4, γ_eq=1.163, γ_fr=1.242 (a_fr 1126.6 vs 1126.7 = effetto 7e-5 della patch, unica cifra che si muove).

### 1.4 Quirk dell'ufficiale osservati in esecuzione (non-issue per noi, verbalizzati per rigore)
1. `shk_eq_calc` a U esattamente = U_CJ tocca il cap di 500 iterazioni e stampa "shk_calc did not converge" (messaggio copia-incolla: siamo in shk_eq_calc, `postshock.py:516`): è il comportamento noto alla **tangenza** Rayleigh–Hugoniot; lo stato restituito è corretto (T₂=2943.8 K vs 2944 atteso). Identico nel nostro (stesso codice); le demo ufficiali convivono con la stampa.
2. `demo_vN_state.py` come distribuita importa e usa `PostShock_eq` e stampa lo **stato CJ di equilibrio sotto l'intestazione "vN State"** (verificato eseguendola: w₂=1117.6, a_eq=1120.9 ⇒ w₂/a_eq=0.997≈1, la firma del punto CJ; un vero vN frozen per C2H2:1 O2:2.5 AR:3 avrebbe T≈2800 K, non 3932 K). Mislabel della demo ufficiale; il nostro `vN_state()`/uso di `PostShock_fr` è conforme alla definizione del report (vN = post-shock frozen).

**ESITO COMPITO 1: nessuna divergenza funzionale oltre la patch dichiarata di `soundspeed_fr` (equivalente entro 6-10e-5 locale, ≤0.02% end-to-end) e l'omissione di funzioni/warning non usati.**

---

## 2. MECCANISMI / TERMODINAMICA

### 2.1 Inventario zip (`SDToolbox/data/`)
Yaml+cti paralleli, thermo **NASA7** salvo dove indicato:
- **H2/O2(±N2)**: Mevel2017 (14 sp., range fino a 6000 K), Hong2011, Burke2012, Keromnes2013, Li2015, sandiego20161214_H2only, NASA9/chem-H2O2 (**NASA9**);
- **idrocarburi C1-C4+**: gri30_highT (GRI-3.0 con thermo esteso 300→5000 K, stesse Δh_f; header di J.E. Shepherd 12-2018), Mevel2015 (H2-N2O-HC), Mevel2018 (C2H2/HC, 118+ sp.), sandiego20161214 (San Diego), FFCM2/ffcm1, aramco2, Davis2005 (H2/CO), Blanquart2018, PG14;
- **kerosene/pesanti**: JetSurf2 (C≤12, 348 sp. — include NC12H26; **niente specie NOx**), hexaneFull/Partial/Reduced, pentane*;
- **aria/speciali**: airNASA9ions/noions (**NASA9**), chem-HC-Air (NASA9), OH-*, h2br2, one-step, 2-Butenal, nitric_oxide, methylidyne, hydroxyl; cartelle NASA7/ e NASA9/ con i .dat sorgente (GOOS-BURCAT-RUSCIC).

### 2.2 Cosa usiamo noi
- `gri30.yaml` (builtin Cantera; NASA7, range 200–3500 K) per tutti i gas-phase;
- `data/dodecane_eq_thermo.yaml` (NOSTRO, thermo-only 20 sp.: c12h26 da nDodecane_Reitz + prodotti CHO + **NO, N, N2O, NO2**; range fino a 5000 K) per kerosene;
- `data/gri30_CHO_eq.yaml` (subset C/H/O di gri30, 34 sp.) per equilibri veloci fuel/O2;
- `nDodecane_Reitz.yaml` (builtin) come sorgente.

### 2.3 Spot-check eseguiti (1 atm/101.325 kPa, 300 K salvo demo; tolleranza dichiarata: 0.5%)

| caso | nostro (mech) | ufficiale zip (mech) | Δ U_CJ | esito |
|---|---|---|---|---|
| H2/air φ=1 (295 K, 100 kPa) | 1969.4 (gri30) | 1968.5 (Mevel2017) | **0.05%** | PASS |
| C2H4/O2 φ=1 | 2373.5, T₂=3933.6, γ_e=1.1387 (gri30) | 2373.4, T₂=3933.4, γ_e=1.1387 (gri30_highT) | **0.004%** | PASS |
| C2H2/O2 φ=1 | 2424.8, γ_e=1.1529 (gri30) | 2424.5, γ_e=1.1526 (gri30_highT) | **0.012%** | PASS |
| H2/O2 φ=1 | 2836.4 (gri30) | 2836.4 (gri30_highT) | **0.00%** | PASS |
| C12H26/air φ=1 | 1795.9, T₂=2836 (DODEQ) | 1802.4, T₂=2854 (JetSurf2-thermo¹) | **0.36%** | PASS¹ |
| C12H26/O2 φ=1 | 2341.0, T₂=3882 (DODEQ) | 2336.2, T₂=3870 (JetSurf2-thermo¹) | **0.21%** | PASS |

¹ Subset thermo-only di 16 specie estratto da JetSurf2.yaml ufficiale (per il CJ di equilibrio conta solo il thermo; le specie escluse hanno X<1e-5 al CJ). **Attribuzione del delta aria**: rifacendo il nostro DODEQ **senza** NOx si ottiene 1804.4 → il puro delta dei fit termodinamici (Reitz vs JetSurF) vale **0.11%** (1804.4 vs 1802.4), mentre l'inclusione dei NOx (endotermici: X_NO=0.9% al CJ) vale **−0.47%**. h_f(298 K) del dodecano è **identico** nei due file (−117.652·RT). JetSurf2 non possiede specie NOx: per l'equilibrio kerosene/ARIA il nostro set è termodinamicamente PIÙ completo dell'ufficiale (coerente con CEA); per fuel/O2 il delta residuo è puro fit.

### 2.4 Verdetto termo
- La preoccupazione "gri30 NASA7 cappato a 3500 K con T_CJ fino a 4211 K" è **empiricamente chiusa**: contro gri30_highT (fit McBride NASA TM-4513 fino a 5000 K, stesse Δh_f) le differenze sono ≤0.012% su U_CJ e ≤0.0003 su γ_e, perché l'estrapolazione polinomiale NASA7 di gri30 resta liscia e i due dataset condividono le entalpie di formazione.
- Stessa caratterizzazione (NASA7 ideal-gas) tra zip e nostro; la zip offre in più NASA9 (aria ionizzata ecc.), non necessario al deck.
- **Nessun numero del deck cambia.** Nota soft: per studi dedicati C2H2 l'ufficiale suggerirebbe Mevel2018; per kerosene JetSurf2 come cross-check (fatto qui).

---

## 3. DEMO UFFICIALI (49) — censimento, esecuzioni, confronto coi nostri script

### 3.1 Censimento completo (funzioni SDT; ipotesi eq/fr)

| demo | cosa fa | funzioni SDT | ipotesi chiave |
|---|---|---|---|
| demo_CJ | solo U_CJ + fit plot | CJspeed(+utilities) | min-wave-speed (eq. Hugoniot) |
| demo_CJstate | **CJ state completo** | CJspeed, PostShock_eq, soundspeed_eq/fr | stampa a_eq E a_fr; **γ₂=a²ρ₂/P₂ per entrambe**; w₂=Uρ₁/ρ₂ |
| demo_CJstate_isentrope | **isentropa TZ dal CJ** | CJspeed, PostShock_eq, soundspeed_eq/fr | espansione `SV`-equilibrate, **a_eq nell'integrale di Riemann**, plateau u=0; γ₂_eq=a_eq²ρ/P; **usa gri30_highT per C2H4/O2**; q efficace two-γ |
| demo_CJ_and_shock_state | CJ + riflessioni eq/fr | +reflections | doppio binario eq vs fr |
| demo_PSeq / demo_PSfr | stato post-shock eq / frozen a U dato | PostShock_eq / PostShock_fr | eq vs fr espliciti |
| demo_vN_state | stato "vN" al CJ | CJspeed, **PostShock_eq(!)** | **mislabel ufficiale** (stampa lo stato eq; cfr. §1.4) |
| demo_RH, demo_RH_CJ_isentropes | Rayleigh + Hugoniot eq (col CJ) | CJspeed, PostShock_eq/fr, hug_eq | tangente al CJ; isentrope |
| demo_RH_air, _eq, _isentropes | Hugoniot frozen/eq per aria | PostShock_fr/eq, soundspeed_fr | shock non reattivo |
| demo_ZNDCJ / demo_ZNDshk / demo_ZND_CJ_CV | **struttura ZND** a U_CJ / U dato / +CV | CJspeed, PostShock_fr, zndsolve(, cvsolve) | **partenza vN frozen; M=U/a_fr dentro la zona di reazione** |
| demo_cvCJ, demo_cvshk, demo_cv_comp, demo_cpCJ | esplosioni CV/CP, τ induzione | cvsolve/cpsolve | cinetica, non usati da noi |
| demo_RZshk, demo_STGshk, demo_STG_RZ | reaction zone / stagnazione (Hornung) | PostShock_fr, zndsolve/stgsolve | frozen shock + cinetica |
| demo_EquivalenceRatioSeries, ExplosionSeries, PressureSeries, OverdriveSeries | sweep φ/P/f | CJspeed, PostShock_*, cv, znd, reflections | nostro analogo: sweep_sdt.py |
| demo_equil, demo_TP, demo_exp_state, demo_GasPropAll, demo_species_thermo | equilibri UV/HP/TP, proprietà, a_eq/a_fr(T) | (Cantera) + soundspeed_eq/fr | — |
| demo_g | **γ multipli lungo isentropa eq**: G, κ_fr, κ_eq, cp/cv, **cp_eq/cv_eq (FD ri-equilibrando)** | gruneisen_*, soundspeed_eq/fr | **κ_eq=ρa_eq²/P ≠ (cp/cv)_eq**: il cuore del Compito 4 |
| demo_quasi1d_eq | **ugello quasi-1D di equilibrio**: camera HP → isentropa SP-eq, gola dove **M_eq=u/a_eq=1**, ṁ=ρ*a*_eq | soundspeed_eq | eq + bracket frozen su Isp |
| demo_rocket_impulse | **Isp razzo eq vs frozen** (H2/O2/He, blowdown a Pa=0) | soundspeed_eq | Isp=(u+(P−Pa)/(uρ))/g; eq>fr |
| demo_PrandtlMeyer, _CJ, Detn, Layer | funzione PM / polari dal CJ | soundspeed_eq/fr, PostShock_* | "if equilibrium expansion → equilibrium sound speed in M" (docstring!) |
| demo_oblique, demo_shock_point, demo_shock_adiabat, demo_shock_state_isentrope | polari/adiabatiche di shock frozen | PostShock_fr, soundspeed_fr | frozen (non-reattivo) |
| demo_reflected_eq / _fr, demo_overdriven, demo_precompression_detonation | shock riflessi eq/fr, sovraguidate | reflections, CJspeed, PostShock_eq | eq vs fr espliciti |
| demo_ShockTube, demo_TransientCompression, demo_detonation_pu | tubo d'urto, compressione, **P-u detonazione** (u₂+isentropa eq) | CJspeed, PostShock_*, soundspeed_eq | TZ/matching |

### 3.2 Demo/percorsi ESEGUITI in questo audit
1. **demo_CJstate.py così com'è** (Mevel2017): output integrale in §1.3 — M₂,eq=w₂/a_eq=1092.1/1090.4=**1.0016**, M₂,fr=1092.1/1126.7=**0.9693**; γ₂_eq=1.163, γ₂_fr=1.242.
2. **demo_vN_state.py così com'è** (C2H2/O2/Ar, gri30_highT): w₂/a_eq=0.997 → conferma indipendente della sonicità eq (e scoperta del mislabel, §1.4).
3. **Core di demo_ZNDCJ con modulo ufficiale** (stessi input del nostro run): §1.2 — deltas ≤0.02%.
4. **Core di demo_quasi1d_eq (punto sonico eq) con modulo ufficiale** sul CJ H2/air: P*=2.0622e5 Pa, w*=a*_eq=951.9 m/s, F/ṁ=1353.1 — il nostro `stage_axial` memorizzato dà P*=2.0621e5, w*=951.9, M*=1.0000, F/ṁ=1353.1: **coincidenza a 0.005%**.
5. Cross-run vendored↔ufficiale, meccanismi (§2.3), e identità γ (κ_eq vs cp_eq/cv_eq, §4).

### 3.3 Confronto critico demo ↔ nostri script

| nostro script | demo di riferimento | esito |
|---|---|---|
| `detonation.py` / repo `cj_states.py` (solver CJ indipendente brentq+minimize su Hugoniot eq) | demo_CJstate | **PASS**: stessa definizione γ_eq=ρ₂a_eq²/P₂ (r.77), M2=w2/a_eq (r.82), M2_fr separato; U_CJ concorda con SDT entro 0.1% (VALIDATION.md). Nota: usa soundspeed_eq via `SV`-equilibrate (il metodo "vecchio" del toolbox, valido alle P del CJ; l'ufficiale preferisce TP per robustezza ad alta P) — nessuna differenza numerica rilevata (γ_e concordi a 4 decimali con SDT). |
| `thrust_models.py` stage_cj / repo `sk_models.py` | demo_CJstate | **PASS**: γ_e=ρa_eq²/P (r.101), residuo sonico registrato per OGNI caso (r.109; 1.2-1.6e-3 su 16 casi). |
| `thrust_models.py` stage_axial + `sweep_sk_axial.py` | demo_quasi1d_eq (+demo_rocket_impulse) | **PASS**: isentropa `SP`-equilibrate, gola w=a_eq (bisezione, più fine dell'interpolazione della demo), F/ṁ=w+(P−Pa)/(ρw) identica; verifica incrociata §3.2.4 a 0.005%. La demo calcola anche il **bracket frozen** (Isp_fr<Isp_eq): noi dichiariamo l'ipotesi equilibrio (SK è equilibrio per costruzione) — completezza, non errore. |
| `thrust_models.py` stage_ph (SK K, ΔP_CJ) e stage_stech (one-γ con γ_e) | — (nessuna demo PDE/RDE impulse; demo_rocket_impulse è razzo classico) | **PASS** (fedeltà ai paper già auditata in gamma_audit.md; l'uso di γ_e equilibrio è ora corroborato da demo_CJstate/report Eq. 6.54-6.55). |
| `znd_sdt.py` / repo `znd_profiles.py` | demo_ZNDCJ | **PASS**: pipeline identica CJspeed→PostShock_fr→zndsolve; L_ind/L_exo riproducono l'ufficiale a ≤0.02% (§1.2). |
| `sweep_sdt.py` / repo `cj_sweeps.py` | demo_EquivalenceRatioSeries ecc. | **PASS**: stesse funzioni; miscele fuel/aria (T₂<3500 K, thermo gri30 pienamente valido). |
| `cycles_ws.py` / repo `cycles.py` | demo_CJstate_isentrope (espansione eq) + demo_RH (Rayleigh) | **PASS**: `_expand_eq` = isentropa `SP`-equilibrate (equivalente alla `SV` della demo); vN via PostShock_fr con assert di collinearità di Rayleigh (res<1e-2) — più severo della demo. γ_e_CJ/γ_fr_CJ entrambi registrati. |
| — | demo_CJstate_isentrope (plateau TZ u=0, stato 3) | **NOTA (non errore)**: il deck non usa il plateau TZ esplicito; la storia di pressione RDE è modellata via fit ψ(ξ)=e^(−αξ) di SK (K=1.02/1.54), che È la parametrizzazione SK dell'espansione TZ. Nessuna azione. |
| — | demo_PrandtlMeyer*, demo_oblique, demo_reflected_*, demo_cv*, demo_STG*, demo_ShockTube | non usate dal deck (fenomeni non trattati); nessun obbligo. |

**Errori nostri trovati: NESSUNO. Interpretazioni sbagliate: NESSUNA. Incompletezze: 2 note dichiarative (bracket frozen non mostrato; plateau TZ coperto via SK) — nessun impatto numerico.**

---

## 4. TRATTATO FORMALE γ / velocità del suono (chiusura della questione equilibrio vs frozen)

### 4.1 Definizioni formali (dal report FM2018.001 e dal codice)

**Suono congelato (frozen).** A composizione fissata Y:
a_fr² = (∂P/∂ρ)_{s,Y}  [Eq. 7.81 specializzata; Eq. 9.24, "the definition of the frozen sound speed"]
Per miscela di gas ideali vale l'identità (∂P/∂ρ)_s = (c_p/c_v)(∂P/∂ρ)_T [Eq. 7.105, rep. p. 102] e (∂P/∂ρ)_{T,Y}=RT [Eq. 7.106], quindi
**a_fr² = γ_fr(T)·R·T = γ_fr·P/ρ con γ_fr = c_p,Y/c_v,Y** [Eq. 7.107-7.108].
Implementazioni: ufficiale `thermo.py:118-156` (FD su isentropa SVX congelata); nostra patch `gas.sound_speed` = identica identità analitica (equivalenza misurata 6-10e-5, §1.2).

**Suono di equilibrio (shifting).** La derivata è la pendenza dell'**isentropa di equilibrio**, con la composizione che si RI-EQUILIBRA lungo la perturbazione:
a_eq² = (∂P/∂ρ)_{s, Y=Yeq(P,ρ)}  [Eq. 6.24 (in v: a_e²=−v²(∂P/∂v)_{s,Yeq}), Eq. 7.82]
Forma esplicita con le derivate delle frazioni massiche [Sez. 7.10 "Sound Speed", rep. pp. 99-100; Eq. 7.83-7.87]: da dh=(∂h/∂P)dP+(∂h/∂ρ)dρ+Σᵢ(∂h/∂Yᵢ)dYᵢ e dYᵢ^eq=(∂Yᵢ^eq/∂P)_ρ dP+(∂Yᵢ^eq/∂ρ)_P dρ,

  a_eq² = [ (∂h/∂ρ)_{P,Y} + Σᵢ (∂h/∂Yᵢ)_{P,ρ,Yⱼ≠ᵢ}·(∂Yᵢ^eq/∂ρ)_P ] / [ 1/ρ − (∂h/∂P)_{ρ,Y} − Σᵢ (∂h/∂Yᵢ)_{P,ρ,Yⱼ≠ᵢ}·(∂Yᵢ^eq/∂P)_ρ ]   (Eq. 7.87)

cioè a_fr² con in più i termini di shifting Σᵢ(∂h/∂Yᵢ)(∂Yᵢ^eq/∂·): il calore di reazione rilasciato/assorbito dal ri-equilibrio modifica la compressibilità isentropica. Implementazione: `thermo.py:34-116` (metodo TP, App. G2 — quello nel nostro vendored, identico).

**Disuguaglianza.** **a_fr ≥ a_eq sempre** [Eq. 7.91, rep. p. 100], "irrespective of the nature of the equilibration process, endothermic or exothermic", conseguenza delle proprietà estremali dell'equilibrio (rimando a Fickett & Davis App. 4D). Fisicamente: le onde acustiche in mezzo reagente sono dispersive — le alte frequenze (composizione che non fa in tempo a spostarsi) viaggiano ad a_fr, le basse ad a_eq [rep. Sez. 6, pdf p. ~83]. Misurato al CJ H2/air: a_eq/a_fr = 1091.2/1127.5 = **0.9678**.

**Esponente isentropico di equilibrio.** γ_eq ≡ −(v/P)(∂P/∂v)_{s,eq} [Eq. 6.54, rep. p. ~90] = **a_eq²/(P v) = ρ a_eq²/P** [Eq. 6.55]. È la pendenza logaritmica dell'isentropa di equilibrio, **NON un rapporto di calori specifici**: misurato al CJ H2/air (gri30): κ_eq=ρa_eq²/P=**1.1634** ≠ c_p^eq/c_v^eq (FD ri-equilibrando, metodo demo_g.py)=**1.1745** ≠ γ_fr=c_p/c_v=**1.2420**; mentre κ_fr=ρa_fr²/P=**1.2420**=γ_fr esattamente (identità di gas ideale). demo_g.py (righe 86-87: κ_fr/κ_eq; 130-144: c_p^eq/c_v^eq per FD ri-equilibrando) esiste precisamente per insegnare questa tripla distinzione.

### 4.2 La condizione CJ è sonica rispetto a QUALE a? → **a_eq** (chiuso)
- **Doc**: "A consistent thermodynamic theory will use the **equilibrium sound speed** to define the CJ point and this is what is used in our computations" [rep. Sez. 6, discussione post-Wood&Kirkwood/Fickett&Davis, pdf p. ~87]. Sez. 8.3 (rep. p. 121): l'algoritmo alternativo "Sonic Flow" impone w₂ = a_eq(P₂,T₂,Y₂eq) [Eq. 8.27]; il toolbox implementa il **minimum-wave-speed** proprio per non dover iterare su a_eq — i due sono equivalenti al CJ (tangenza).
- **Codice/demo, verificato eseguendo**: demo_CJstate → M₂,eq=**1.0016**, M₂,fr=**0.9693** (H2/air, Mevel2017); demo_vN_state → w₂/a_eq=**0.997**; i nostri 16 casi in `thrust_models_all.json` → |w₂/a_eq−1| = **1.2-1.6e-3** su tutti (il residuo ~1e-3 è la precisione del fit parabolico del minimo + FD della a_eq, non fisica).
- **Perché M₂,fr≈0.96-0.97 e non 1**: w₂ è unica; a_fr>a_eq (Eq. 7.91) ⇒ w₂/a_fr=(w₂/a_eq)·(a_eq/a_fr)≈0.9678. Il punto CJ è interno al cono acustico frozen ma esattamente sonico rispetto alle perturbazioni di equilibrio (le uniche che sopravvivono a valle a t→∞, dove la cinetica è rilassata).

### 4.3 Chiusura formale per i quattro impieghi
**(a) Condizione CJ: EQUILIBRIO.** M₂ ≡ w₂/a_eq = 1. Ogni check del deck la usa così (`detonation.py:82`, `thrust_models.py:109`). Dichiarare M₂ col suono frozen (0.97) sarebbe un errore di categoria — non lo facciamo mai.
**(b) γ_e nei modelli di spinta SK: EQUILIBRIO.** Il γ_e di SK Eq. 19-22 e Tables 1-2 è ρ₂a_eq²/P₂ al CJ [già dimostrato numericamente in `data/gamma_audit.md` sulle tabelle SK; ora corroborato dal codice ufficiale: demo_CJstate stampa esattamente `gammae=ae**2*rho_2/gas.P` (demo_CJstate.py:51-52) e il report la formalizza in Eq. 6.54-6.55]. I nostri `stage_ph`/`stech_calc` usano quel γ_e (1.13-1.17), MAI c_p/c_v frozen (1.22-1.27).
**(c) Espansione axial-flow / ugello: EQUILIBRIO (con frozen come bracket).** L'espansione dei prodotti è quasi-statica su scale lunghe rispetto alla cinetica vicino al CJ: isentropa di equilibrio h=h(P,s₂) con `equilibrate('SP')` e gola dove w=a_eq — esattamente demo_quasi1d_eq (righe 84-88: M=u_eq/a_eq; 105-112: interpolazione della gola a M=1) e demo_CJstate_isentrope (integrale di Riemann con a_eq, righe 131-132); nostra implementazione verificata a 0.005% (§3.2.4). L'ufficiale affianca sempre il bracket frozen (demo_rocket_impulse): differenza a favore dell'eq perché la ricombinazione (esotermica) restituisce entalpia al flusso; il vero Isp sta tra i due, più vicino all'eq per P alte/T alte.
**(d) Suono nella formulazione ZND: FROZEN — ed è l'unica scelta coerente.** Dentro la zona di reazione la composizione NON è in equilibrio: Y è variabile di stato indipendente che evolve con la cinetica (dYᵢ/dt=ω̇ᵢWᵢ/ρ). Differenziando P=P(ρ,s,Y) [Eq. 9.23] il coefficiente di dρ a (s,Y) fissati è per definizione a_fr² [Eq. 9.24, pdf p. ~146]; i termini di shifting compaiono separatamente come termicità σ̇=Σ(W̄/Wᵢ−h_{s,i}/(c_pT))dYᵢ/dt, che è il forcing delle ODE (η=1−M_fr², `znd.py:60-67,223,236`: `c=soundspeed_fr`, `M=U/c`). Usare a_eq nello ZND conterebbe due volte lo shifting (nel suono E nella termicità). La singolarità sonica ZND (η→0) è quindi frozen; il punto CJ termodinamico resta sonico-equilibrio: i due si riconciliano solo asintoticamente (per questo M_fr a fine zona di reazione ≈0.925-0.96 <1 nei run, e il report discute le eigenvalue detonations quando la coincidenza fallisce).

---

## VERDETTO FINALE

| aspetto | nostro | ufficiale (zip Apr 2026) | esito |
|---|---|---|---|
| Algoritmo CJspeed (sweep+parabola, bounds, tolleranze) | identico riga-per-riga | postshock.py:263-329 | **PASS** |
| CJ_calc/shk_calc/shk_eq_calc (Newton 2%, limiter, cap 500) | identici | postshock.py:198-563 | **PASS** |
| PostShock_eq/fr (solver, guess volumeBoundRatio=5) | identici | idem | **PASS** |
| soundspeed_eq (metodo TP, App. G2) | identico | thermo.py:34-116 | **PASS** |
| soundspeed_fr | `gas.sound_speed` (patch dichiarata) | FD SVX 0.1% | **PASS** (equiv. 6-10e-5; ZND ≤0.02%; `_soundspeed_fr_fd` conservata) |
| zndsolve (ODE, termicità, criterio sonico frozen, LSODA) | identico; senza warning eigenvalue | znd.py | **PASS** (warning = sola diagnostica; ramo n==b ufficiale è dead code) |
| config (ERRFT/ERRFV/volumeBoundRatio) | 1e-4/1e-4/5 | identici | **PASS** |
| hug_fr/hug_eq, gruneisen_*, reflections/stagnation/cp/cv/utilities | omessi | presenti | **PASS** (non usati; omissione documentata in PROVENANCE) |
| Meccanismo gas-phase (gri30 vs gri30_highT/Mevel) | gri30 | zip alternativa | **PASS** (ΔU_CJ ≤0.05% aria, ≤0.012% O2 anche a T₂=4211 K) |
| Kerosene (DODEQ vs JetSurf2) | DODEQ (con NOx) | JetSurf2 (senza NOx) | **PASS** (0.36%/0.21%; delta fit puro 0.11%; nostro set più completo per aria) |
| Convenzione γ_e (spinta SK/Stechmann) | ρ₂a_eq²/P₂ al CJ | demo_CJstate.py:51-52; Eq. 6.54-6.55 | **PASS** |
| Condizione CJ sonica | M₂,eq=1 (resid 1.2-1.6e-3, 16 casi) | Sez. 6/8.3; demo M₂,eq=1.0016 | **PASS** |
| vN state | PostShock_fr (frozen) | def. report (demo_vN_state ufficiale è mislabeled!) | **PASS** (noi corretti; quirk ufficiale verbalizzato) |
| Espansione axial/ugello | SP-equilibrate + gola w=a_eq | demo_quasi1d_eq | **PASS** (0.005%) |
| ZND: suono | frozen (via patch equivalente) | frozen (Eq. 9.24) | **PASS** |
| Etichetta di revisione vendored ("Jan 2021") | mislabel documentale | contenuto = release Apr 2026 | **FIX applicato** (solo docstring/PROVENANCE; zero impatto numerico) |

**FIX APPLICATI** (documentali, nessun numero cambia): aggiornata l'etichetta di revisione e il verbale di verifica in `project_build/sdtoolbox/{__init__,postshock,thermo,znd}.py` e `rde-lecture-code/sdtoolbox/PROVENANCE.md` (il vendored dichiarava "rev. Jan 2021"; il contenuto coincide riga-per-riga con la release ufficiale "Updated April 2026" qui auditata, patch esclusa). **Impatto sui numeri del deck: NESSUNO** — tutti i valori (U_CJ, T₂, p₂/p₁,
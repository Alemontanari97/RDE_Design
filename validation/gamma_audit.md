# AUDIT γ — frozen vs equilibrio nei modelli di spinta RDE (Shepherd–Kasahara, Stechmann–Heister)

*Audit tecnico a convergenza — 2026-07-08.*
*Fonti primarie: `tmp_sk/sk_fulltext.txt` (estratto integrale del report GALCIT FM2017.001, 1793 righe), `tmp_st/st_text.txt` (estratto JSR 56(3) 2019), `specs/sk_spec.md`, `specs/stechmann_spec.md`, `data/thrust_models_all.json` (meta+V&V), `data/vv_thrust.md`, `data/results_main.json`, `scripts/{detonation,analysis,thrust_models,build_deck}.py`.*

**Fatto preliminare dirimente:** la parola **"frozen" non compare mai** né nel full text di Shepherd–Kasahara (grep: 0 occorrenze su 1793 righe) né in quello di Stechmann–Heister–Harroun (0 occorrenze). "Equilibrium" compare in entrambi, sempre in posizione portante.

---

## 1. VERDETTO PER MODELLO

### 1.1 SK — Pressure-history model (Sec. 3, Eq. 11–22): **γ_e = γ dei PRODOTTI, di EQUILIBRIO, valutato allo stato CJ**

Definizione nel paper (dopo Eq. 11):

> "The function ψ depends on the properties of the combustion products, indicated here as a dependence on the ratio of specific heats γe."

e (Sec. 3, dopo Eq. 22):

> "the known modest dependence of UCJ and γe on initial conditions."

γ_e entra in Eq. 13 (K = ∫ψ(ξ; γe)dξ), Eq. 19 (ΔP_CJ ≈ ρc U_CJ²/(γe+1)), Eq. 20 e 22 (F_I/Ṁ ≈ K·U_CJ/(γe+1); Isp_f ≈ K·U_CJ/(Y_f g (γe+1))).

Il paper **non scioglie mai a parole il pedice "e"**; l'identificazione con l'equilibrio è però numericamente univoca:

- **Table 1** (p. 22): "γe 1.169 1.165 1.142 1.137" per H2-air, C2H4-air, C2H4-O2, C3H8-O2 (a 1.5 atm / 255 K). Il γ frozen (cp/cv a composizione congelata) allo stesso stato CJ è ~1.24 per H2-air: **se γe fosse frozen la tabella direbbe 1.24, non 1.169**.
- **Table 2** (App. B, 1 atm / 300 K): "γ 1.163 1.161 1.129 1.139 1.134" allo State 2 (CJ), con a2 = 1091 m/s per H2-air. Verifica: ρ2·a2²/P2 = 1.51·1091²/1.55e6 = **1.160 ≈ 1.163** ⇒ a2 è la **velocità del suono di equilibrio** e γ è l'**esponente isentropico di equilibrio** al CJ (col suono frozen, 1128 m/s, verrebbe 1.24). Coerente con la condizione CJ, che è sonica rispetto al suono di equilibrio (Fickett–Davis).
- Tutta la termochimica del paper è dichiaratamente di equilibrio: "These solutions were computed using realistic thermochemistry **and equilibrium properties** using the Shock and Detonation Toolbox Browne et al. (2017)."
- Replica numerica (vedi §2): con γ_e ≡ ρ2·a_eq²/P2 al CJ gli input di Table 1 sono riprodotti "**gamma_e exact to 3 dp**" (V&V check 3a) e la Isp_f del modello I+II a −0.1% (4702 vs 4706 s).
- Checkpoint SK Fig. 6a (spinta specifica H2-air stechiometrica ≈ 930 m/s): Eq. 20 con γ_e dà 928 m/s; con γ frozen darebbe 896 m/s. **La figura del paper stesso è consistente solo con γ_e di equilibrio.**

**Stato di valutazione:** al punto CJ (State 2), non sui prodotti espansi. La `sk_spec.md` (Sec. 2.0, Notation) lo registra correttamente: "γ_e (or γ) products' ratio of specific heats".

### 1.2 SK — Axial-flow model (Sec. 4, Eq. 33–45): **espansione su isentropa di EQUILIBRIO (shifting), ancorata al CJ (s = s₂)**

Citazione esplicita e inequivocabile (Sec. 4, prima di Eq. 44):

> "In an expansion wave following a detonation, the flow time scales are sufficiently long compared to the chemical time scales (see Wintenberger et al. 2004) that **the flow is to a reasonable approximation in chemical equilibrium and so that h = h(P, s) only**."

> "…the entropy is taken to be constant and equal to the value of the CJ state; for this ideal model we assume that detonation propagates at the CJ speed, UD = UCJ."

> "The density ρ and axial speed w are computed assuming isentropic expansion from the CJ state."

Quindi w = √(2(h₁ − h(P, s₂))) con h(P, s₂) sull'**isentropa di equilibrio chimico passante per il CJ**. Nessun γ costante è coinvolto nel modello numerico (Fig. 8–9, Table 1 riga "Axial Flow Model", Table 2 riga "Axial Sonic Flow"). La replica indipendente con isentropa di equilibrio riproduce tutte e 4 le Isp_f axial di Table 1 entro **±0.2%** (V&V 3b) e P_m/P₂ ∈ [0.218, 0.234] contro lo 0.22–0.25 del paper: se SK avesse usato un'espansione frozen la discrepanza sarebbe di svariati punti percentuali. Caso chiuso.

### 1.3 SK — One-γ closed form (Sec. 4.2, Eq. 46–56): **γ costante il cui VALORE è quello di equilibrio dei prodotti (1.1–1.15)**

> "The one-γ analytical model of the CJ state can be used with perfect gas thermodynamic expressions to estimate the specific thrust."

> "For the range 5 < MCJ < 8 and **1.1 < γ < 1.15 which are of interest for RDEs**, numerical evaluation gives reasonable agreement (within 10%) to the value computed using detailed thermochemistry for P1 = Pa."

Il range dichiarato 1.1–1.15 coincide con i γ_e di equilibrio di Table 1/2 (1.129–1.169) ed **esclude** il frozen (~1.22–1.27). Quindi: formula a γ costante ("frozen value" lungo l'espansione, s = s₂ per Eq. 53), ma il valore da inserire è il γ di equilibrio dei prodotti al CJ. Con footnote 4: la perdita di P_t del 7% attraverso gli urti cambia la temperatura isentropica di <1% — l'ipotesi s = s₂ è controllata.

### 1.4 Stechmann–Heister–Harroun (JSR 2019) — c*, C_F: **proprietà CEA di EQUILIBRIO ai prodotti di detonazione; γ e M tenuti COSTANTI (valore effettivo) lungo ugello e ciclo**

Assunzioni dichiarate (Sec. II):

> "2) Variations in molecular weight M and gas specific heat ratio γ through the nozzle as functions of time and space are negligible."

> "4) **All chemical reactions reach equilibrium conditions behind the detonation front.** Because peak pressures and temperatures are exceedingly high in a detonation combustor, this is a reasonable assumption."

Provenienza delle proprietà:

> "Using NASA Chemical Equilibrium Analysis (CEA) [19] code to derive detonation gas properties and pressure ratios, we can generate approximate pressure-time histories for any RDE."

> "…the temperature computed from Eq. (15), and additional gas properties computed using NASA CEA, one can derive c* and mass flux for a single point on the RDE annulus as a function of time using Eqs. (6) and (7)."

> "All results employ ideal gas and **equilibrium chemistry assumptions**."

Quindi: c*(t) (Eq. 7) e C_F(t) (Eq. 8–11) sono le formule classiche a gas perfetto con γ, M, T0 **dei prodotti di detonazione da CEA in equilibrio** (problema "det" di CEA: stato CJ con composizione di equilibrio); l'assunzione 2 congela il **valore** di γ lungo l'ugello e il ciclo (approccio a "γ effettivo"), non la chimica al fronte. Il paper non dichiara quale colonna γ di CEA sia usata (CEA riporta anche il cp/cv frozen), ma l'assunzione 4 + "equilibrium chemistry assumptions" rendono l'esponente isentropico di equilibrio (GAMMAs di CEA, ~1.1–1.2 per i prodotti) l'unica lettura internamente coerente — anche perché Eq. 15 (T_c ∝ P_c^((γ−1)/γ)) descrive il blowdown isentropico degli stessi prodotti. "Frozen" non compare mai nel testo. La `stechmann_spec.md` registra correttamente: "4) **Equilibrium chemistry** behind the front… Gas properties from NASA CEA [19]" e "Ideal gas + CEA equilibrium chemistry".

---

## 2. EVIDENZA NUMERICA DELLA REPLICA (dirimente dove il testo è implicito)

Da `data/thrust_models_all.json` (campo `meta`) e `data/vv_thrust.md`:

- Definizione usata nei nuovi calcoli: `gamma_e_def: "equilibrium isentropic exponent rho2*a_eq^2/P2 at CJ (a_eq = equilibrium sound speed)"` (SDToolbox `soundspeed_eq`); il frozen è salvato a parte come `gamma_fr = cp/cv`.
- Check 3a (input replica SK Table 1, 1.5 atm/255 K): "U_CJ<=0.05 pct, **gamma_e exact to 3 dp**, P_CJ<=1.5 pct on all 4 cases". Es.: gamma_e calcolato 1.16922 vs γe pubblicato 1.169 (H2-air).
- Check 3b (axial vs SK Table 1): "**all 4 within 0.2%**" (5395/5383, 2285/2280, 912/911, 953/952 s).
- Check 3c (pressure-history I+II vs SK Table 1): H2-air 4702/4706 (−0.1%), C2H4-air −0.9%, C3H8-O2 −4.1%; C2H4-O2 704 s non riproducibile (anomalia A1 documentata, anche internamente incoerente nel report).
- Valori di confronto per H2/air @ 1 atm/300 K: **γ_e = 1.1634** (equilibrio) vs **γ_fr = 1.2420** (frozen). Vecchio `results_main.json`: campo *chiamato* `gamma_eq` = 1.2420 con a2 = 1127.7 m/s ⇒ **il vecchio campo è etichettato male: è il frozen** (origine: `scripts/detonation.py` r. 43, `gamma_eq = gas.cp_mass/gas.cv_mass`, cioè cp/cv a composizione congelata sul gas equilibrato; SK Table 2 dà a2 = 1091 m/s, equilibrio). Curiosamente il vecchio deck lo "sapeva": la slide di validazione recita "The minimum-speed point returns M₂≈0.965 **on the frozen sound speed** — exactly the equilibrium-sound-speed sonic condition."

**Conclusione:** l'ipotesi "γ_e di SK = esponente isentropico di equilibrio al CJ" è l'unica che riproduce simultaneamente γe di Table 1 (3 decimali), a2/γ di Table 2, le Isp axial (±0.2%), il checkpoint di Fig. 6a e la Isp PH H2-air (−0.1%).

---

## 3. IMPLICAZIONI — la correzione A5 è GIUSTA nei numeri finali, ma VA SFUMATA nella narrazione

Testo A5 (`vv_thrust.md`): "results_main.json FovM/Ispf used the FROZEN gamma at CJ (~1.22-1.25) in place of the equilibrium gamma_e (~1.13-1.17) required by SK Eq. 19-20, **and omitted term II**: e.g. H2/air Isp_f 3203 s (deck) -> 4268 s (faithful PH I+II at the same conditions)."

- **Diagnosi concettuale: GIUSTA.** SK Eq. 19–22 richiede γ_e di equilibrio (§1.1); il vecchio pipeline (`analysis.py` r. 15: `FovM=K*cj['UCJ']/(ge+1); Ispf=FovM/(Yf*g)` con `ge` = frozen 1.24) usava il γ sbagliato E ometteva il Term II.
- **Attribuzione numerica: DA SFUMARE.** Decomposizione esatta per H2/air @ 1 atm/300 K, u_c = 300 m/s (numeri da `thrust_models_all.json`):

| Passo | Isp_f [s] | Δ |
|---|---:|---|
| Vecchio deck: Eq. 20 approx, γ frozen 1.242, solo Term I | 3203 | — |
| Fix γ → γ_e 1.1634 (Eq. 20 approx, solo Term I) | 3319 | **+3.6%** |
| ΔP_CJ esatto al posto dell'approx Eq. 19 (solo Term I) | 3195 | −3.7% |
| + Term II (u_c = 300 m/s; P1 = Pa) | **4268** | **+33.6%** |

  I primi due passi quasi si cancellano (coincidenza fortuita: il frozen-γ sottostima Eq. 20 di ~3.6%, ma l'approx Eq. 19 sovrastima ΔP_CJ di ~4%): **il salto 3203→4268 è dominato dal Term II** (contributo u_c/(Y_f g) = 1072 s), non dallo scambio di γ. Presentarlo come "effetto frozen→equilibrio" sarebbe tecnicamente scorretto.
- **Caveat sul 4268:** il Term II con u_c = 300 m/s è il valore CFD di Schwer & Kailasanath adottato da SK in Table 1; dipende dal design dell'iniettore. Se lo si cita come valore "H2/air a 1 atm", dichiarare "I+II con u_c = 300 m/s come in SK Table 1". Per le **mappe in φ** (stile SK Fig. 6) il paper stesso usa il solo termine di detonazione (Eq. 20/22): lì il numero corretto è 3319 s / 928 m/s a φ=1 (γ_e), non 4268 s.

### Numeri/slide del deck che cambiano (da `build_deck.py` + pipeline figure)

1. **Slide "CJ & von Neumann states — wide propellant set"** (build_deck ~r. 234): la colonna intestata **"γ_e" mostra i valori frozen** di `results_main.json` (1.21–1.27). Correzione: sostituire con i γ_e veri da `thrust_models_all.json` → H2/air 1.16, H2/O2 1.13, CH4/air 1.17, CH4/O2 1.13, C2H4/air 1.16, C2H4/O2 1.14, C2H2/O2 1.15, C3H8/O2 1.13, kerosene/O2 1.14 (in alternativa, rietichettare γ_fr — ma è γ_e che serve al filo SK). Il bullet "kerosene/O₂ … with the lowest γ_e" è errato in entrambe le basi: il minimo è H2/O2 (γ_e 1.129; e anche frozen 1.21) → riscrivere.
2. **Slide "Shepherd–Kasahara: specific thrust & impulse"**: `fig_sk_thrust.png` è generata da `figs_more.py` sul vecchio `sweeps.json` (frozen γ, solo Term I) e **l'asse dichiara "≈ K U_CJ/(γ_e+1)"** — mismatch etichetta/valori (curve ~3.5% basse; Ispf H2/air @φ=1 ≈ 3203 invece di 3319). Rigenerare da `data/sweep_sk_cj_phi.json` (già contiene gamma_e per φ, es. 1.1635 a φ=1).
3. **Slide "Thrust models vs. simulation"**: la tabella viene da `sk_tables.json` (valori pubblicati SK, γe 1.169… già di equilibrio) → **non cambia**; la figura `fig_thrust_mach.png` (da `figs_sota2.py`, vecchio `sweeps.json`) va rigenerata: la linearità F/Ṁ ∝ U_CJ resta, i punti salgono ~3.5%.
4. **Equazioni renderizzate** (`eqs.py`: `cj_press`, `sk_FI`, `sk_Isp`): il simbolo γ_e è già corretto; con i vecchi numeri era il valore ad essere incoerente. Aggiungere la nota di slide (v. §4).
5. **Secondario, da verificare a parte:** η_FJ (formula one-γ in `analysis.py`/`suite.py`, `eta_fj_fixed.json`, slide cicli) è anch'essa valutata con γ frozen 1.24; per coerenza col one-γ SK andrebbe rivalutata con γ_e (impatto atteso: qualche punto percentuale su η).
6. **Non cambia:** slide di validazione SDToolbox (usa U_CJ, T2, p2/p1, insensibili alla scelta; la nota su M₂ frozen 0.965 è già corretta e anzi diventa un buon aggancio didattico).

---

## 4. RACCOMANDAZIONE OPERATIVA (quale γ in ogni formula mostrata)

| Formula in slide | γ da usare | Valore tipico |
|---|---|---|
| ΔP_CJ ≈ ρ₁U_CJ²/(γ_e+1) (SK Eq. 19) | γ_e equilibrio al CJ | 1.13–1.17 |
| F_I/Ṁ ≈ K·U_CJ/(γ_e+1), Isp_f (SK Eq. 20/22) | γ_e equilibrio al CJ | idem |
| Axial flow w = √(2(h₁−h(P,s₂))) (SK Eq. 44–45) | **nessun γ**: isentropa di equilibrio via SDToolbox (dirlo esplicitamente) | — |
| One-γ closed form (SK Eq. 46–54), one-γ CJ (M_CJ, p₂/p₁) | γ costante = γ_e dei prodotti | 1.1–1.15 (range del paper) |
| Stechmann c*(t), C_F(t) (Eq. 7–11) | γ, M dei prodotti da CEA **equilibrio**, tenuti costanti lungo ugello/ciclo | ~1.1–1.2 |
| η_FJ one-γ | γ_e (coerenza col CJ state) — rivalutare | — |

**Nota esplicita da mettere in slide (una volta, dove compare γ_e la prima volta):**

> "γ_e = esponente isentropico di **equilibrio** dei prodotti allo stato CJ (γ_e ≡ ρ₂a_eq²/p₂, con a_eq velocità del suono di equilibrio): ~1.13–1.17. Da non confondere con il cp/cv frozen degli stessi prodotti (~1.22–1.25): il CJ è sonico rispetto al suono di *equilibrio* (M₂ = 1 con a_eq; ≈0.965 col suono frozen). Con γ frozen, Eq. 19–22 di Shepherd–Kasahara non riproducono la loro Table 1."

**Fonte numerica unica per il deck:** `data/thrust_models_all.json` (γ_e, γ_fr, PH I/I+II, axial, Stechmann; V&V in `data/vv_thrust.md`). Ritirare `results_main.json` per FovM/Ispf/γ; se resta per U_CJ/T2/p2p1 (validati, check 1), rinominare mentalmente il campo `gamma_eq` → frozen.

---

## Appendice — inventario citazioni chiave (posizioni in `sk_fulltext.txt` / `st_text.txt`)

| # | Fonte | Riga | Citazione (verbatim) |
|---|---|---|---|
| S1 | SK Sec. 3 | 487–488 | "The function ψ depends on the properties of the combustion products, indicated here as a dependence on the ratio of specific heats γe." |
| S2 | SK Sec. 3 | 648 | "the known modest dependence of UCJ and γe on initial conditions" |
| S3 | SK Sec. 4 | 866–870 | "the flow is to a reasonable approximation in chemical equilibrium and so that h = h(P, s) only" |
| S4 | SK Sec. 4 | 872–874 | "the entropy is taken to be constant and equal to the value of the CJ state" |
| S5 | SK Sec. 4 | 908 | "The density ρ and axial speed w are computed assuming isentropic expansion from the CJ state" |
| S6 | SK Sec. 4.2 | 1096–1098 | "For the range 5 < MCJ < 8 and 1.1 < γ < 1.15 which are of interest for RDEs…" |
| S7 | SK Sec. 3/Fig. 4 | 392–393 | "computed using realistic thermochemistry and equilibrium properties using the Shock and Detonation Toolbox" |
| S8 | SK App. B | 1652–1661 | "computed using equilibrium thermochemistry… concentrations determined by the equilibrium solutions. The 53 species found in GRI-Mech 3.0" |
| S9 | SK Table 1 | 1214 | "γe 1.169 1.165 1.142 1.137" |
| S10 | SK Table 2 | 1684 | "γ 1.163 1.161 1.129 1.139 1.134" (con a₂ = 1091, 1005, 1542, 1281, 1269 m/s) |
| T1 | ST Sec. II | 212–213 | "Variations in molecular weight M and gas specific heat ratio γ through the nozzle as functions of time and space are negligible." |
| T2 | ST Sec. II | 219–222 | "All chemical reactions reach equilibrium conditions behind the detonation front. Because peak pressures and temperatures are exceedingly high in a detonation combustor, this is a reasonable assumption." |
| T3 | ST Sec. III | 334–336 | "Using NASA Chemical Equilibrium Analysis (CEA) [19] code to derive detonation gas properties and pressure ratios" |
| T4 | ST Sec. III | 371 | "additional gas properties computed using NASA CEA, one can derive c* and mass flux … using Eqs. (6) and (7)" |
| T5 | ST Sec. III | 476 | "All results employ ideal gas and equilibrium chemistry assumptions." |
| — | SK+ST | grep | "frozen": 0 occorrenze in entrambi i testi |

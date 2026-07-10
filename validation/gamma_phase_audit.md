# AUDIT γ PER FASE — cicli termodinamici Wintenberger–Shepherd (Brayton / Humphrey / Fickett-Jacobs)

*Audit a convergenza (secondo giro) — 2026-07-08. Complementare a `data/gamma_audit.md` (audit γ_e dei modelli di spinta SK/Stechmann, confermato in §4). Fonti: `specs/thermo_spec.md` (§2.6-2.7, §3), `scripts/cycles_ws.py`, `scripts/cycles.py`, `scripts/figs_more.py`, `scripts/thrust_models.py`, `data/cycles_ws.json`, `data/q_mapping.json`. V&V complessiva: `data/cycles_validation.md` (96 PASS / 0 FAIL).*

---

## 0. Regola teorica (dalla spec e dai paper)

| tratto | proprietà corrette | valore (φ=1, 300 K, Cantera) |
|---|---|---|
| compressione 0→1 / 1→2 (reagenti freschi) | γ₁ = cp/cv dei **reagenti** | fuel-air 1.35–1.40 (CH₄-aria **1.388**, H₂-aria 1.401, C₃H₈-aria 1.367); fuel-O₂ 1.29–1.40 (kerosene/O₂ 1.24, vapore pesante) |
| combustione / detonazione (2→3) | **salto con rilascio q**: equilibrio chimico, nessun γ costante; in forma one-γ, relazioni CJ (B2) | — |
| espansione 3/4→5 (prodotti) | γ_e = esponente isentropico di **equilibrio dei prodotti** (ρa²_eq/p al CJ) | 1.13–1.17 sulle 12 miscele (spec §2.7: 1.13–1.2 fuel-O₂, 1.16–1.3 fuel-aria lungo φ) |
| modello one-γ W&S (B2-B3 = A57) | **un unico γ = quello dei PRODOTTI**: il paper prescrive e usa γ = 1.2 (classe fuel-aria) e γ = 1.1 (classe fuel-O₂) in Figs. A16/B3, A22, A23 | 1.2 / 1.1 |

Il paper stesso registra il controesempio: Heiser & Pratt con γ = 1.4 (reagenti) su tutto il ciclo ⇒ η sistematicamente sovrastimate (spec §2.7; quantificato in §2 qui sotto).

---

## 1. Tabella: implementazione × ciclo × tratto → γ usato / γ teorico / esito

### A. Cicli a chimica reale (Cantera 3.2 + SD Toolbox) — `cycles_ws.py three_cycles()`; figure `fig_cycles_pv`, `fig_cycles_eta`; sezioni JSON `fj_mixtures`, `sweep_C3H8_air`, `sweep_CH4_air`

| ciclo | tratto | implementazione (γ usato) | γ teorico | esito |
|---|---|---|---|---|
| tutti | 1→2 compressione | isentropa **frozen dei reagenti** (`gas.SP` a composizione congelata, cp(T) reale variabile; nessuna reazione) | reagenti | **PASS** |
| FJ | 2→3/4 detonazione | `CJspeed` + `PostShock_eq`: salto CJ di **equilibrio**, q implicito negli stati — nessun γ assunto | salto q, equilibrio | **PASS** |
| Humphrey | 2→3 combustione | `equilibrate('UV')` — equilibrio, nessun γ | idem | **PASS** |
| Brayton | 2→3 combustione | `equilibrate('HP')` — equilibrio, nessun γ | idem | **PASS** |
| tutti | 3/4→5 espansione | isentropa di **equilibrio mobile** (`SP`-equilibrate a gradini): γ_e effettivo variabile lungo l'espansione, mai costante | prodotti equilibrio | **PASS** |
| tutti | 5→6/1 rigetto | prodotti equilibrati a (T₁,P₁) | — | **PASS** |
| — | γ *riportati* | `gamma_e_CJ` = ρa²_eq/p (equilibrio) e `gamma_fr_CJ` = cp/cv (frozen) salvati **entrambi ed etichettati** | — | **PASS** |

### B. Modello one-γ analitico — `cycles_ws.py` §1; figure `fig_cycle_family` (A22), ancore A16/B3 in JSON

| ciclo | tratto | γ usato | γ teorico (paper) | esito |
|---|---|---|---|---|
| FJ (B3=A57) | intero ciclo, inclusa compressione A58 (T₂ = T₁π_c^((γ−1)/γ)) | γ = 1.2 unico | prodotti 1.2 (prescrizione W&S; 1.1 per fuel-O₂) | **PASS con riserva quantificata** (§2): fedele al paper, etichettato in figura «γ = 1.2 (detonation products, W&S one-γ model)»; il bias del γ unico sul tratto di compressione è quantificato sotto |
| Humphrey (A60), Brayton (A59) | intero ciclo | γ = 1.2 (stesso family plot) | idem | **PASS** (coerenza interna del confronto a γ comune, dichiarata in figura) |
| ancore η_FJ(M_CJ) A16/B3 | — | γ = 1.2 e 1.1 (entrambe le curve del paper) | idem | **PASS** (validate: 8/8 righe) |

### C. Benchmark steady (onde stazionarie) — `fig_cj_entropy`, `fig_entropy_partition`, `fig_tp_loss`, `fig_eta_fixed_stag`

| oggetto | γ usato | γ teorico | esito |
|---|---|---|---|
| Hugoniot classica (q̃=4) e di ristagno (q̃_t=0.8), partizione Δs, p_t2/p_t1, η(M₀=5) | γ = 1.4 ovunque | scelta **del paper** per l'analisi steady (spec §3.1-3.2: benchmark a γ=1.4, flusso a monte = reagenti/aria) | **PASS** (dichiarato in ogni figura: «γ = 1.4») |
| claim deprecato p_t2/p_t1 ≈ 0.0136 | γ = 1.2 (prodotti) applicato **anche alla compressione ram dei reagenti** | violazione della regola di fase | **FIXED** (giro precedente, confermato): sostituito dai valori supportati 0.074 (q̃=4) / 0.054 (q̃_t=0.8) a γ=1.4; provenienza riprodotta e documentata in JSON `deprecated_0136_reproduction` |

### D. Codice legacy — `figs_more.py` (riscritto in questo giro), `cycles.py`

| item | difetto trovato | fix applicato | esito |
|---|---|---|---|
| D1 `figs_more.py` fig_cycles_pv legacy | one-γ g=1.2 su **tutti** i tratti, inclusa l'isentropa di compressione dei reagenti (riga `v2=v1*pic**(-1/g)`) | bloccata dietro `REGEN_LEGACY_CYCLES` con nota di supersessione; versione corrente da `cycles_ws.py plot` (chimica reale, CH₄-aria); label one-γ esplicita aggiunta anche nel codice gated | **FIXED** |
| D2 `figs_more.py` fig_entropy_partition legacy | γ=1.2, q̃=5.24 → origine del claim 0.0136 | idem (gated); versione corrente a γ=1.4 con ancore 0.074/0.814 | **FIXED** |
| D3 `figs_more.py` fig_tp_loss legacy | urto nei **reagenti** calcolato con γ=1.2 | idem (gated); versione corrente a γ=1.4, urto inerte + onda CJ completa | **FIXED** |
| `cycles.py` (one-γ, γ=1.2, q̃=8) | nessuno: docstring dichiara «representative products EQUILIBRIUM gamma_e»; nessuna figura corrente ne dipende (superseded da `cycles_ws.py`) | — | **PASS** (nota) |
| `data/eta_fj_fixed.json` (γ frozen 1.24) | γ frozen usato come γ_e | ritirato a favore di `fj_mixtures` (audit precedente) | **FIXED** (confermato) |

### E. Modelli di spinta (conferma dell'audit dedicato `data/gamma_audit.md`)

| modello | γ per l'espansione | esito |
|---|---|---|
| SK pressure-history (Eq. 19-22), `thrust_models.py` r. 107/121 | γ_e = ρ₂a²_eq/p₂ al CJ (equilibrio, `soundspeed_eq`); frozen salvato a parte come `gamma_fr` | **CONFERMATO PASS** (replica SK Table 1 a 3 decimali su γ_e) |
| SK axial-flow (Eq. 44-45), r. 217-219 | nessun γ costante: isentropa di equilibrio h(P, s₂) | **CONFERMATO PASS** (Isp ±0.2%) |
| Stechmann c*, C_F | γ prodotti CEA equilibrio, tenuto costante lungo l'ugello (assunzione 2 del paper) | **CONFERMATO PASS** |

---

## 2. Bias del one-γ sul tratto di compressione — quantificazione (caso M₀ = 5)

Il one-γ W&S applica γ_prodotti = 1.2 anche dove fluiscono reagenti (γ_r ≈ 1.39-1.40). Confronto con la variante two-γ (compressione a γ_r = 1.4; ciclo e M_CJ(T₂) a γ_p = 1.2, formula A57/A58 invariata), q̃_R = q_c/RT₁ = 30 (classe CH₄/H₂-aria):

| grandezza | one-γ (1.2) | two-γ (compr. 1.4) | bias one-γ |
|---|---|---|---|
| T_t1/T₀ a M₀ = 5 (compressione ram) | 3.50 | 6.00 | **−42%** |
| π_ram = (T_t1/T₀)^(γ/(γ−1)) a M₀ = 5 | 1838 | 529 | **+247%** |
| p_t2/p_t1 attraverso onda CJ a M = 5 | 0.0136 | 0.0537 (γ=1.4) | perdita sovrastimata **×3.9** (= provenienza del claim deprecato) |
| T₂/T₁ a π_c = 5 | 1.308 | 1.584 | −17.4% |
| T₂/T₁ a π_c = 20 | 1.648 | 2.354 | −30.0% |
| η_FJ a π_c = 5 | 0.379 | 0.478 | **−0.098** |
| η_FJ a π_c = 20 | 0.496 | 0.636 | **−0.140** |
| η_FJ a π_c = π_ram(M₀=5) | 0.694 | 0.848 | −0.154 |

**Validazione incrociata (dirimente):** Cantera CH₄-aria a π_c = 5 dà η_FJ = 0.4751; la variante two-γ prevede 0.478 (Δ = +0.003), il one-γ puro 0.379 (Δ = −0.096). A π_c = 1 i due coincidono per costruzione. ⇒ **l'errore dominante del one-γ lungo π_c è proprio il γ dei prodotti applicato alla compressione dei reagenti**; a π_c = 1 (nessuna precompressione) il modello è invece fedele alla sua calibrazione.

**Direzione opposta (Heiser–Pratt):** γ = 1.4 su *tutto* il ciclo a M_CJ = 5.09 (CH₄-aria) dà η = 0.348 contro 0.218 (γ=1.2) e 0.191 (γ_e = 1.168): sovrastima **+0.13** — è l'errore che il paper imputa a Heiser & Pratt (spec §2.7, nota 7).

**Legame con `data/q_mapping.md`:** per i fuel-aria l'inversione one-γ di M_CJ con γ_e reale dà q_eff/q_c = 1.18–1.30 (> 1): stessa tensione reagenti/prodotti — M_CJ fisico è riferito al suono dei *reagenti* (γ₁ ≈ 1.39, a₁ = 346-409 m/s) mentre il modello implica a₁ = √(γ_e RT₁). Per i fuel-O₂ domina invece la dissociazione: q_eff/q_c = 0.63–0.84.

---

## 3. Esito complessivo

1. **Tutti i tratti delle implementazioni correnti sono conformi alla regola di fase** (tabella §1.A-C): compressione = reagenti, salto = equilibrio con q, espansione = prodotti in equilibrio.
2. **3 difetti storici chiusi in questo giro** (D1-D3: blocchi legacy di `figs_more.py` gated e supersedued) + 2 fix di giri precedenti confermati (0.0136; eta_fj_fixed.json).
3. Il **one-γ resta fedele al paper** (γ = 1.2 prodotti, ora etichettato «detonation products, W&S one-γ model» in `fig_cycle_family`), con il bias del tratto di compressione **quantificato** (§2) e citabile a lezione: sottostima η_FJ di ~0.10-0.15 a π_c = 5-20; il caso 0.0136 è lo stesso bias in direzione perdite.
4. Modelli di spinta: γ_e equilibrio prodotti **confermato** (nessuna azione).

*Fonti numeriche: `data/cycles_ws.json`, `data/q_mapping.json`; V&V: `data/cycles_validation.md` (96/96), `data/vv_thrust.md`.*

---

## 4. MAPPA COMPLETA equilibrio/frozen — ogni punto d'uso della lezione (terzo giro, 2026-07-09)

*Sezione nuova a valle dell'audit CJ-sonico e dei bound di espansione. Fonti: `data/cj_equilibrium_sonic_derivation.md` (derivazione formale + convergenza M₂,eq: 1.00148 → 0.999998 raffinando ERRFT/ERRFV 1e-4 → 1e-6), `data/cj_sonic_convergence.json`, `data/expansion_bounds.{json,md}` (bound eq/frozen/Bray sui 4 propellenti), `data/sdt_official_audit.md` §4, `data/gamma_audit.md`. Questa tabella alimenta la slide "models map" e le note.*

| # | punto d'uso | ipotesi usata | giustificazione formale (1 riga + rif.) | bound/alternativa → effetto |
|---|---|---|---|---|
| 1 | **stato CJ / U_CJ** (tutte le tabelle e i modelli a valle) | Hugoniot di **equilibrio**; sonicità rispetto ad **a_eq** | tangenza Rayleigh–Hugoniot ⇒ ds=0 lungo ℋ ⇒ w₂=a_eq [FM2018 Eq. 6.31–6.39, App. C.2; derivazione backup]; verificato: M₂,eq→1 (2·10⁻⁶) con tolleranze raffinate, U_minwavespeed = U_sonicflow a 1e-7 | col suono frozen M₂,fr=0.960–0.968 SEMPRE: non un bound ma un errore di categoria (Def. II); γ_e 1.13–1.17 vs γ_fr 1.21–1.27 |
| 2 | **stato von Neumann** | post-shock **frozen** (`PostShock_fr`) | urto inerte: zero avanzamento chimico sulla scala dell'urto (ansatz ZND; report §9) | `PostShock_eq` al posto del vN dà il CJ, non un bound (demo_vN_state ufficiale mislabeled: 3932 K vs ~2800 K; sdt_official_audit §1.4) |
| 3 | **ZND interno** (`znd_sdt.py`) | suono **frozen** in η=1−M² (M=U/a_fr); shifting SEPARATO come termicità σ̇ | Y è variabile cinetica: (∂P/∂ρ)_{s,Y}=a_fr² [Eq. 9.23–9.24]; a_eq nello ZND = doppio conteggio dello shifting | non esiste bound alternativo coerente; patch a_fr analitica ≤0.02% su L_ind (sdt_official_audit §1.2) |
| 4 | **espansione TZ / isentropa 3/4→5 dei cicli** (`cycles_ws.py`) | **equilibrio mobile** (`SP`-equilibrate a gradini) | τ_flow ≫ τ_chem a valle del CJ [SK S3 ← Wintenberger 2004]; demo_CJstate_isentrope/demo_quasi1d_eq | frozen = bound inferiore: sull'axial-flow Isp_f −7.3/−12.6% (riga 7); sui cicli stessa direzione, non ricalcolato |
| 5 | **compressione 0→1→2 dei cicli (+ ram)** | isentropa **frozen dei REAGENTI** (γ₁≈1.36–1.40) | nessuna reazione sotto T_ign; regola di fase (spec §2.6; qui §1.A) | γ prodotti sul tratto reagenti = bias one-γ: η_FJ −0.098/−0.140 a π_c=5/20; claim 0.0136 (perdite ×3.9) — §2 qui |
| 6 | **SK pressure-history γ_e (Eq. 19–22)** (`stage_ph`) | γ_e = ρ₂a²_eq/P₂ **equilibrio al CJ** | unica lettura che riproduce SK Table 1 a 3 decimali e Fig. 6a [gamma_audit §1.1; demo_CJstate.py:51–52; Eq. 6.54–6.55] | con γ_fr 1.24: Eq. 20 −3.6% e Table 1/Fig. 6a non riprodotte (gamma_audit §3) |
| 7 | **SK axial-flow (Eq. 44–45)** (`stage_axial`) | isentropa di **equilibrio** s=s₂, nessun γ | dichiarazione esplicita SK [S3–S5]; replica Table 1 ±0.2%; = demo_quasi1d_eq (0.005%) | **frozen dal CJ**: w* −3.4/−4.2%, T/Ṁ sonico −6.8/−10.0%, Isp_f matched −7.3/−12.6%; **Bray (freeze alla gola)**: −0.2/−2.0% su Isp_f, ≡eq al piano sonico [expansion_bounds.md] |
| 8 | **one-γ** (W&S A57–A60 cicli; SK Eq. 46–56; CJ two-γ) | γ costante = **γ_e prodotti equilibrio** (1.1–1.2) | prescrizione dei paper [W&S; SK "1.1<γ<1.15"]; γ_e è la pendenza log dell'isentropa eq al CJ (Eq. 6.54–6.55) | γ_fr: −3.6% su Eq. 20 (storia del vecchio deck, gamma_audit §3); γ=1.4 ovunque (Heiser–Pratt): η +0.13 (§2) |
| 9 | **Stechmann c*, C_F** (`stage_stech`) | camera **CEA equilibrio**; γ_e ed M costanti lungo ugello e ciclo | assunzioni 2+4 del paper [T1–T5]; γ_e costante = linearizzazione dell'isentropa eq al CJ | collocato TRA i bound, adiacente all'equilibrio: variante one-γ entro ±2% dell'eq (H₂/aria +1.6%, fuel-O₂ −0.8/−1.4%), MAI vicina al frozen (−7/−13%) [expansion_bounds §3] |
| 10 | **EAP Kaemming–Paxson** | espansione ideale isentropica di ogni cella a p₀, γ del paper (one-γ prodotti); media di availability | metrica di disponibilità: si media l'availability, non p_t [eap_spec/add_notes; worked example −0.4%] | bound eq/fr non applicato (metrica comparativa a γ fissato; sensibilità non calcolata) |
| 11 | **benchmark steady** (Hugoniot q̃, partizione Δs, p_t2/p_t1, η(M₀)) | γ = 1.4 costante (**reagenti**/aria a monte) | scelta del paper per l'analisi steady (spec §3.1–3.2; §1.C qui) | γ_e prodotti sul tratto reagenti = il claim deprecato 0.0136 (FIXED, §1.C) |
| 12 | **M_CJ nelle tabelle** (U_CJ/a₁) | a₁ = suono **frozen dei reagenti** (346–409 m/s fuel-aria) | definizione di M_CJ; coerenza reagenti a monte (q_mapping.md) | a₁=√(γ_eRT₁) implicita nell'inversione one-γ: q_eff/q_c=1.18–1.30 fuel-aria (già documentato) |

**Sintesi in una riga (per la slide):** *equilibrio* per gli STATI ESTREMI e per l'espansione dei prodotti (CJ, isentrope, γ_e, Stechmann), *frozen* per ciò che attraversa scale più corte della chimica (urto/vN, interno ZND, suono dei reagenti, compressione dei freschi); i bound quantificati valgono −7/−13% (frozen) e −0.2/−2% (Bray alla gola) su Isp_f, ±2% (one-γ Stechmann-like vs equilibrio).

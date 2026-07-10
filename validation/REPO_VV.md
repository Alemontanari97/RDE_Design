# REPO_VV — V&V avversariale della repo come strumento di analisi e design

*Eseguita 2026-07-10 da V&V engineer avversariale (punto di vista: studente che
non sa nulla del progetto). Ambiente: Python 3.10.12, Cantera 3.2.0, NumPy
2.2.6, SciPy 1.15.3, Matplotlib 3.10.9 (conforme a `requirements.txt`),
PYTHONPATH vuoto. Base: commit `863c836`; esito su `9b10e58` + questo report.*

**Verdetto:** repo **PROMOSSA** come strumento didattico di analisi e design.
Installazione copia-incolla senza attriti; tutti i numeri promessi riprodotti
al decimale; dopo il refactoring minimo è una libreria importabile
(`from src.thrust.sk_models import cj_calc, …`) con uno studio di design
end-to-end eseguibile in ~15 s. Tutti i 13 attriti trovati sono stati risolti
(nessuno toccava la fisica validata).

---

## 1. Installazione pulita — PASS

Clone fresco (`git clone` → `/tmp`), PYTHONPATH vuoto, README seguito alla
lettera:

| comando README | promesso | ottenuto | esito |
|---|---|---|---|
| `python examples/example_cj.py` | U_CJ = 1969 m/s (err −0.10% vs 1971), p2/p1 = 15.5, T2 = 2944 K, ~1–2 min | 1969.0 m/s, −0.10%, 15.46, 2944.2 K, **3.2 s** | PASS (stima tempo conservativa) |
| `python examples/example_cycles.py` | η_FJ(CH4/air) = 0.300, bande 0.28–0.31 / 0.18–0.23, M_CJ = 4.599, instant | 0.300; 0.279–0.310 / 0.183–0.231; 4.599; 0.35 s | PASS |
| `python examples/example_thrust.py` | H2/air 1194/1353 m/s, Isp_f 4268/4838 s; Stechmann live 237.1 s = shipped | identici; live−shipped < 0.05 s | PASS |

Cwd-independence verificata (esecuzione da `/` e da `/tmp`): ogni script
risolve i path da `__file__` come dichiarato. `figs/` viaggia nel clone via
`.gitkeep` e `style.save()` fa `os.makedirs(exist_ok=True)`.

## 2. Test funzionali completi — PASS (tutti i moduli, tutte le CLI)

| comando | atteso | ottenuto |
|---|---|---|
| `src/thrust/stechmann_nozzle.py validate` | 18/18 | **18/18 nel file**; a stdout erano 16 (bug di slicing, F1 → fix) |
| `stechmann_nozzle.py optimize / states / fig` | — | OK (quadratura 5.5e-6/7.0e-6 s; figura salvata) |
| `src/thrust/tables.py` | 8/8 verdetti | **8/8 PASS** (3c = PASS* con anomalia di letteratura documentata C2H4-O2 704 s) |
| `src/thrust/sk_models.py all "H2/air"` | CJ+PH+AX | U=1969.0, PH 1193.7, AX 1353.1 — JSON rigenerato **byte-identico** |
| `sk_models.py cj "C12H26/air" "C12H26/O2"` | — | float identici; corretto solo il path mech (F5) |
| `src/cycles/cycles.py onegamma/fj/sweep/validate/plot` | 99/99 | **99 PASS / 0 FAIL**; 12 miscele FJ identiche agli shipped (η_FJ a 4 decimali); 7 figure |
| `src/cycles/q_mapping.py` | 0.00% | **max \|q_major−q_B1\|/q_B1 = 0.00%; max dev M_CJ = 0.00%** |
| `src/cycles/q_formal.py` | — | identità q°/q_c verificate (CH4/air 300 K: +0.0023%; 700 K: −0.298%) |
| `src/detonation/cj_states.py` | tabella 5 casi | OK, M2 = 1.000 esatto, stato vN incluso |
| `src/detonation/znd_profiles.py` (4 casi) | — | Δ_i: H2/air 0.2446, H2/O2 0.0502, CH4/O2 0.1989, C2H4/O2 0.0215 mm — JSON **byte-identico** |
| `src/detonation/cj_sweeps.py` | 4 blocchi, resumabile | ricompute completo ~80 s; U_CJ(φ=1) = 1969.0 nel blocco phi; ripresa per-sezione verificata sul campo |

Nota su Δ_i: ND — nessun valore atteso dichiarato nel README; verificati
contro `data/znd_sdt.json` (identici) e ordine di grandezza di letteratura.

## 3. Modularità come libreria — PASS dopo refactoring minimo

Stato iniziale: moduli-script con `sys.path` hack e import piatti tra sibling;
nessun `__init__.py`; le funzioni di sk_models incapsulavano I/O (JSON+print);
`tables.py` eseguiva tutto all'import. Refactoring (fisica intatta, verificata
per non-regressione):

- `__init__.py` per `src/`, `src/{cycles,detonation,thrust}` (docstring, import
  lazy: importare non computa e non scrive). Package name: mantenuto `src` —
  rinominare avrebbe rotto decine di riferimenti nei report frozen; il costo è
  solo estetico ed è documentato nel README.
- `sk_models`: estratte le funzioni pure `cj_calc / ph_calc / axial_calc`
  (gli stage CLI ora le avvolgono); **nuova** `axial_calc(chem='frozen')` =
  bound inferiore dell'espansione (punto e del design study); id di meccanismo
  portabili nel JSON.
- `stechmann_nozzle`: griglie/tolleranze generalizzate a P_cp arbitraria
  (prima `XTOL[Pcp]` esplodeva fuori da {20,200} atm); import relativo di
  `st_core` con fallback script-mode; `matched/cp_state/det_state` già
  perfettamente riusabili per propellenti nuovi via `PROPS[...]`.
- `tables.py`: avvolto in `main()` → import senza side effect (verificato).

### Studio di design end-to-end (`examples/example_design_study.py`, ~15 s)

C2H4/O2 stechiometrico, riempimento 1 atm/300 K; camera R̄ = 45 mm, gap = 5 mm,
L = 80 mm; ṁ = 0.30 kg/s; trade ugello a P_cp = 10 atm:

| step | risultato |
|---|---|
| (a) CJ | U_CJ = **2373.5 m/s** (= shipped, +0.000%), p_CJ/p1 = 33.18, T_CJ = 3934 K, γ_e = 1.1387, γ_fr = 1.2365 |
| (b) Wolański | u_fill = 168 m/s; λ ≈ 29·Δ_i = 0.62 mm; l_cr = (12±5)λ = 7.5 [4.4–10.6] mm; l_fill = **20.1 mm/rev** (25% di L); **W = 2.69 [1.90–4.61] → nominali 2–3 teste** (banda 1–4) |
| (c) spinta | PH **1979.1 m/s** (termine I 1679.1 + II 300.0), Isp_f = 892 s; AX sonico **1904.7 m/s**, Isp_f = 859 s (matched 941 s); F = 594/571 N |
| (d) bound frozen | **1714.9 m/s = −10.0%** vs equilibrio (Bray in mezzo) — coerente con l'audit §4 (−6.8% H2/air, −10.0% C2H4/O2) |
| (e) η_FJ live | **0.2042** = shipped (three_cycles, chimica completa) |
| (f) Stechmann @10 atm | P_CJ = 37.0 atm, fill 1.11 atm, PR = 33.4, DC = +2.4%, choke margin 0.64 (nota onesta stampata); **bell ε\* = 2.44 → 233.6 s**; **aerospike ε\* = 6.27 → 245.3 s (+5.0%)**; check analitico NPR(ε\*)=⟨Pc⟩/Pa a 1.1e-4 |

Ogni step si auto-verifica contro i JSON shipped; chiusura `OK`.

## 4. Qualità SOTA — PASS

- **Import**: package importabile da qualunque cwd (root su sys.path);
  importare ≠ eseguire (verificato anche per `tables`).
- **Docstring**: già ricche di equazioni+riferimenti in tutti i moduli
  (verificato modulo per modulo); aggiunte quelle delle nuove funzioni con
  equazioni e convenzioni γ.
- **requirements.txt**: versioni minime già presenti e verificate
  (cantera≥3.0, numpy≥1.24, scipy≥1.10, matplotlib≥3.7 + ambiente validato).
- **README**: aggiunte le sezioni **"Use as a design tool"** (studio di design,
  output attesi, tabella delle entry point) e **"Model assumptions map"**
  (condensato della §4 di `gamma_phase_audit.md`: equilibrio per stati estremi
  ed espansione dei prodotti, frozen per urto/ZND/reagenti; bound −7/−13%
  frozen, −0.2/−2% Bray, ±2% one-γ Stechmann).
- **CITATION/PROVENANCE**: allineati all'audit SDT "April 2026"; l'audit ora è
  NELLA repo (`validation/sdt_official_audit.md`) invece che nel build tree.
- **validation/README.md** (nuovo): mappa report→rigeneratore→copia in data/ e
  mappa dei path storici (scripts/→src/, data/gamma_*→validation/), che rende
  non ambigui i riferimenti "Generated by …" dei report frozen.

## 5. Robustezza — PASS (3 test negativi, messaggi migliorati)

| test | prima | dopo |
|---|---|---|
| `sk_models.py all "H6/air"` (miscela non in CASES) | `KeyError: 'H6/air'` (traceback) | `unknown case(s): 'H6/air'` + usage con i 16 case validi |
| `stechmann.matched('RP-2', …)` / `cp_state('CH4', φ=0.05, …)` | `KeyError: 'RP-2'` secco / nessun guard su φ (rischio divergenza silenziosa del Hugoniot) | messaggio con propellenti noti + riga d'esempio per registrarne di nuovi; `ValueError` con range fisico 0.2–3.0 e riferimento alla Table 1 (0.44–1.26) |
| `axial_calc` con mech relativo mancante | errore Cantera generico a valle | `FileNotFoundError: mechanism 'data/nonexistent.yaml' not found under the repo root (…) — restore data/ (git checkout data/) or pass mech= explicitly` |

## 6. Attriti trovati → risolti (13)

| # | attrito | gravità | fix |
|---|---|---|---|
| F1 | stdout di `stechmann validate` mostrava 16/18 righe e ometteva il riepilogo (slice hardcoded); il file era corretto | media (contraddice il badge a video) | slicing ancorato all'header; ora `18/18 rows PASS.` anche a stdout |
| F2 | resumabilità del blocco φ di `cj_sweeps` per-sezione: una run interrotta a metà saltava i fuel mancanti alla ripresa | media (latente) | ripresa per-fuel (`phi H2 done`, …) |
| F3 | `q_formal` stampava `np.float64(…)` nei dict (NumPy 2) | cosmetica | `float(round(…))` |
| F4 | `tables.py` eseguiva tutto all'import | media (libreria) | avvolto in `main()` + guard |
| F5 | JSON shipped con path ASSOLUTO del build tree per il mech kerosene | media (portabilità/provenance) | id mech repo-relativi + resolver; 2 casi CJ rigenerati (diff = sola stringa mech, float identici) |
| F6 | provenance sdtoolbox puntava a `project_build/…` (non consegnato) | media | audit copiato in `validation/`, riferimenti aggiornati |
| F7 | `gamma_phase_audit.md` frozen era la versione vecchia senza §4 (mappa eq/frozen) | media (doc) | refresh alla versione a convergenza |
| F8 | `data/README.md` dichiarava "not shipped" 4 report che invece sono tracciati | bassa | frase corretta |
| F9 | link storici `data/gamma_*` nei report frozen non risolvono nella repo | bassa | mappa path in `validation/README.md` (frozen intatti) |
| F10 | `XTOL[Pcp]` → KeyError per P_cp fuori {20,200} atm (blocca l'uso design) | media (API) | `XTOL.get(Pcp, 1e-3)` + soglie griglia `<= 20` |
| F11 | warning Cantera `ChemEquil… outside valid range` in axial per fuel-O2 | cosmetica | soppressione scoped del solo messaggio atteso (il fallback Gibbs è automatico) |
| F12 | niente `__init__.py`/import di package; funzioni con side-effect | media (modularità) | vedi §3 |
| F13 | errori criptici su case/propellente/φ/mech | media (usabilità) | vedi §5 |

Non-difetti registrati: stima "~1–2 min" di example_cj molto conservativa su
macchine recenti (3 s); `M2w` nel record CJ è la massa molare dei prodotti
(nomenclatura interna coerente con l'uso in `stech_calc`).

## Non-regressione (dopo ogni refactoring)

- Rigenerazioni **byte-identiche** vs shipped: `thrust_models_all.json`
  (H2/air all; C12H26 cj a meno della stringa mech), `znd_sdt.json`,
  `st_nozzle_opt.json`, `st_opt_validation.md`, `thrust_tables.md`,
  `vv_thrust.md`.
- Diff **solo data di run**: `cycles_ws.json`, `q_mapping.{json,md}`
  (ripristinati pristini nel commit); `q_formal.json` mantiene la correzione
  del campo `script` (metadato era del build tree) + jitter float ~1e-15.
- Suite rieseguite dopo OGNI modifica e sul clone finale dello stato
  committato: **18/18, 8/8, 99/99, q_mapping 0.00%, 3 esempi, design study,
  import package da cwd estranea — tutti PASS**.

## Commit

1. `b724ac2` — sdtoolbox provenance: align with the official April 2026 SDT release audit
2. `0c9de0a` — Library API + end-to-end design study; robustness fixes from adversarial V&V
3. `9b10e58` — Docs: 'Use as a design tool' + 'Model assumptions map'; report/path maps
4. *(questo report)* — validation: adversarial V&V report (REPO_VV)

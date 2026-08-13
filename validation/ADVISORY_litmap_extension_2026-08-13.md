# ADVISORY — Litmap extension sweep 1971→2026 (adversarial, 4 independent auditors)
Date: 2026-08-13. Trigger: user challenge "no evolution in later literature? verify rigorously to the present day."
Method: 4 parallel adversarial web auditors, each mandated to FALSIFY one claim; query-bounded per R5.
Extends: ADVISORY_generality_litmap_2026-08-12.md (which remains the page-verified corpus map).
Status: web-search evidence tier (abstracts/snippets unless "full text verified" stated). NOT page-verified
except where noted. No repairs applied; wording duties listed in §6.

## 1. VERDICTS (all four claims SURVIVE within the declared query bounds; two named near-misses)

CLAIM A (Rao=adjoint bridge explicit identification remains ours): **SURVIVES**, weakened only
rhetorically. Near-miss: Kraiko-Tillyaeva, J. Math. Sci. 208:181-198 (2015) — the Russian school
itself names the multiplier system "сопряжённая задача" ("conjugate/adjoint problem for the Lagrange
multipliers", Laval nozzle thrust maximum incl. subsonic part). Internal terminology only; no evidence
of citation of Jameson/Giles-Pierce/ASO, no equivalence statement. So "nobody ever called the
multipliers adjoint" would be FALSE; the substantive claim (explicit published identification
classical-multiplier-field = continuous adjoint of modern shape optimization, optimality residual =
adjoint gradient) was NOT found 1971-2026. Strongest AFFIRMATIVE evidence: Ancourt-Peter-Atinault,
arXiv:2305.03499 (ONERA 2023), MoC applied TO adjoint Euler, validated on a nozzle — FULL TEXT READ,
all 47 refs inspected: zero citations of Rao/Guderley/Hantsch/Hoffman/Kraiko/Shmyglevskii. The
community best positioned to state the bridge does not. Also verified no-bridge: METU thesis (full
lit-review read), Fernandes CEAS Space J 2023 (Rao cited, no adjoint), Zubov 2002 dissertation (RU,
abstract), Yumusak-Eyi 2012 / Eyi 2013 (abstract), Martins 2022 history (snippets: adjoint lineage
starts Lighthill→Pironneau→Jameson, nozzle school bypassed), Giles-Pierce 2000/2001.

CLAIM B (no cycle-averaged variational shape theory): **SURVIVES in the qualified form** (periodic
traveling/rotating-wave inflow, unsteady dynamics inside the constraint). Named near-miss that
FALSIFIES the unqualified reading ("nobody ever posed averaged-thrust variational nozzle design under
time-varying conditions"): **Kraiko-Pyankov-Tillyayeva ISABE-2003-117** + Bogdanov-Kraiko-Pyankov-
Tillyaeva, Aeromekh. Gaz. Din. No.3 (2002) — variational maximum-AVERAGE-thrust contouring under
time-dependent stagnation parameters/throat. Presumed quasi-steady, spatially uniform inflow
(inferred from school methodology + citing context; FULL TEXT UNREAD = residual risk #1).
Residual delta that survives regardless: (i) spatially nonuniform traveling/rotating wave inflow;
(ii) genuinely unsteady dynamics in the constraint (vs quasi-steady regime averaging);
(iii) cycle-average of an unsteady functional (Jensen gap); (iv) optimality conditions derived under
the periodic-wave constraint. Secondary: the adjoint machinery for period-averaged objectives EXISTS
(Rubino et al. JCP 372:220 2018 harmonic-balance adjoint; Zahr-Persson arXiv:1512.00616 periodicity-
constrained adjoint, time-averaged thrust) but was never applied to nozzle contours under wave inflow
— closes the "technology didn't exist" escape; the gap is real. Named threat vector: **JANC**
(arXiv:2504.13750, CPC 2025; Tsinghua, Bing Wang group) — differentiable JAX reacting solver with
adjoint demo on an RDC inverse problem; makes the discrete falsifier buildable. Watch 2026+.

EVOLUTION OF THE CLASSICAL LINE 1971→2026: line stayed alive ONLY in the Kraiko school (CIAM),
always steady-frame: Tillyaeva 1975 (nonuniform AND SWIRLING inflow — closest classical antecedent
to our data class); moment/asymmetry constraints (80s-90s, Fluid Dyn.); plug/spike sub-line
(Baftalovskii-Kraiko-Tillyaeva 1999; Kraiko-Tillyaeva FD 35(6) 2000; JPP 17(6):1347 2001;
FD 37(5) 2002 nonuniform transonic; FD 42(2) 2007 optimal primary-flow direction); curvilinear sonic
line (FD 47(2) 2012); two-sided asymmetric planar (FD 51(1) 2016); 3D = school's own retreat to
direct optimization (FD 49(1) 2014) = declared boundary of the exact theory. Detonation flank
(Egoryan-Kraiko 2016-2022): thermodynamic bounds + skeptical audit of claimed RDE gains
(Thermophys. Aeromech. 29, 2022) — never a variational contour under detonation inflow. US line dead
post Allman-Hoffman 1981; Hoffman JPP 3(2):150 1987 (CTP ≈ Rao in practice) reads as epitaph;
Korte 1992 (least-squares/PNS) = the explicit replacement event. **Verified unoccupied niche: "keep
the variational MoC formulation, swap in a modern optimizer" — no one, any school.** Gas-model
modernizations exist but not on the thrust-optimal problem (Zebbiche 2005-2019 MLN high-T;
dense-gas/ORC 2010s) except Sun et al., Int. J. Aerosp. Eng. 2019 (10.1155/2019/4926413): Rao
control-surface RE-DERIVED for thermally perfect gamma(T), const-gamma contours systematically off
(~1% Isp at large area ratio) — modest genuine theory-side update; compare vs our E4/Lemma-B
var-gamma status. Modern adjoint rebirth of the multiplier content: Giles-Pierce JFM 426:327 (2001,
already registered); + NEW row Ancourt et al. 2023 (adjoint in characteristic form, nozzle-validated
— first modern bridge from adjoint BACK toward MoC structure, still no classical citation).

RDE NOZZLE SOTA 2020-2026: **nothing does variational/adjoint design on a cycle-averaged functional;
no paper even poses which functional the mean flow extremizes.** Three tiers: (1) parametric
CFD-in-the-loop — NASA Glenn (Miki AIAA 2020-3872 methodology; Paxson-Miki 2022-4107 = 2-variable
sweep); NASA Marshall RDRE = experimental parametric variance (length/angles/diameter; nozzle =
manufacturing subcomponent; real methodology if any lives in restricted JANNAF) — Teasley AAS 2025
NTRS 20250000643 read in full. (2) average-then-classical-design: Liu-Cheng-Zhang-Wang (PKU),
AeST 120:107300 (2022): parabolic spike + GA+gradient, 5 objectives — closest formal optimization,
but few-parameter parabola, not free contour, no variational structure; Li-Xu-Huang JPP 38 (2022)
10.2514/1.B38539: area-variation source term in unrolled 2D (quasi-3D), parametric search in
reduced-order unsteady model (NOTE: "area-variational" = area variation, NOT calculus of variations);
AeST 107 (2020) aerospike-from-averaged-outlet; IIT Madras plug 2022-23. Averaging justification is
ALWAYS a-posteriori CFD agreement, never variational — most explicit: IJHE Feb 2026
(S0360319926004568) "applicability of 1D isentropic relations with time-averaged parameters ...
proved" by URANS. (3) surrogate/ML: Sastre et al. HFF 2025 (combustor-level inverse); AIAA
2024-85937 (student ML aerospike); UPM Aerospace 12(6):502 2025 = PULSE detonation multi-objective
(5 params, DoE). **Harroun JPP 2021 remains the standing UNRESOLVED counter-evidence to tier 2**
(mean-designed nozzle does not see mean-flow physics: base suction/delayed separation differ from
comparable steady field; SciTech 2020 could not confirm delayed separation experimentally) — no
2020-2026 paper formally resolves averaged-design validity either way. KTH LES Jan 2026: unsteadiness
survives far into the nozzle (tonal lock to rotating oblique shock) — relevant to any averaging claim.
Our program is the missing arbiter of exactly this debate (consistent with ADVISORY_rde_choking
two-regime contract + Harroun misquote correction already of record).

## 2. Consequence for the program's standing claims
- P2/G14 bridge (Rao = adjoint, identified and measured): KEEP, with new wording caveat (§6-W1).
- D2 gap G3 (no averaged shape theorem): KEEP in qualified form; near-miss row added (§6-A1).
- "First genuinely averaged shape problem" (PB-2): must now carry the ISABE-2003 caveat alongside
  the existing K-O 1970 caveat until human read resolves it.
- Generality niche claim: STRENGTHENED — "variational MoC formulation + modern optimizer" verified
  unoccupied by a dedicated sweep; T-T4 counterpart still NOT-FOUND.

## 3. New litmap rows to ingest (evidence tier: web, verify PDFs before citation-of-record)
Kraiko-Tillyaeva JMS 208 (2015) conjugate problem [A near-miss]; ISABE-2003-117 + Bogdanov 2002
[B near-miss]; Ancourt-Peter-Atinault arXiv:2305.03499 [full text verified]; Sun 2019 var-gamma Rao;
Tillyaeva 1975 swirling/nonuniform profiling; Kraiko school rows F3-F9 (see agent report); Rubino
JCP 2018; Zahr-Persson 1512.00616; JANC 2504.13750 [threat vector]; Liu AeST 2022; Li-Xu-Huang JPP
2022; AeST 107 2020; IJHE Feb 2026; Sastre HFF 2025; UPM Aerospace 12:502 2025; Hoffman JPP 1987;
Korte 1992; Kraiko et al. Thermophys. Aeromech. 29 (2022) RDE-gains audit; Fievisohn-Hoke-Schauer
AIAA 2018-0881 (MoC-native unsteady RDE+nozzle lineage, never extended to design).

## 4. Query-bound of record
The four auditors ran 27 + 33 + 23 + 22 = 105 distinct query strings (2026-08-13, WebSearch) plus
full-text fetches (Ancourt 2023 complete incl. refs; METU thesis lit-review; NTRS 20250000643
complete; CEAS 2023 page; arXiv abstracts). Full per-claim query lists preserved in the four agent
reports of this session (conversation of 2026-08-13); key falsification instrument NOT available:
citation-graph forward sweep (Scopus/WoS) of Rao 1958 / Hoffman 1967 / Guderley-Hantsch 1955
filtered by "adjoint".

## 5. Aggregated named blind spots
(1) ISABE-2003-117 / Bogdanov 2002 full texts unread — highest residual risk (flips B's near-miss
either way). (2) Kraiko-Tillyaeva 2015 reference list unchecked — could flip A's near-miss to bridge.
(3) Russian full-text corpora (eLibrary.ru, Math-Net, TsAGI/CIAM reports; Kraiko 2010 monograph
"Теоретическая газовая динамика: классика и современность"). (4) Chinese-language journals (推进技术
etc.; PKU/NUDT/NUAA publish design-method work there first). (5) Restricted JANNAF (NASA RDRE nozzle
methodology likely lives there). (6) AIAA 2025-2026 proceedings indexing lag. (7) Paywalled full
texts (all AIAA ARC DOIs 403; ScienceDirect 403) — tier-2/3 RDE verdicts rest on abstracts.
(8) Books not inspected: Miele 1965 chapters, Mohammadi-Pironneau, Cassel. (9) Kraiko school
post-2022 nozzle activity unresolved. (10) German (ZFW "adjungierte") and Japanese lines not swept.

## 6. Duties (wording + reading; no code impact)
W1 [claim wording]: everywhere the P2/G14 bridge is stated, add: "the Russian school's internal
'conjugate problem' terminology (Kraiko-Tillyaeva 2015) is the closest adjacent artifact; no published
identification with modern ASO adjoint found (query-bound 2026-08-13)."
W2 [claim wording]: PB-2 / D2-G3 novelty statements add the ISABE-2003 caveat (quasi-steady
average-thrust variational precedent, full text pending human read).
A1 [G5 human-read list +=]: ISABE-2003-117; Bogdanov et al. 2002 (procure, RU); Kraiko-Tillyaeva
2015 (at minimum its reference list).
A2 [procure]: Ancourt arXiv:2305.03499 (on arXiv, free — land in literature/); Sun 2019 (open access);
Hoffman 1987 (free ftp.demec.ufpr.br); Tillyaeva 1975 (TsAGI, hard).
A3 [watch]: JANC / Bing Wang group (Tsinghua) 2026+; Kraiko school successors via eLibrary.ru sweep.
A4 [verify before citing]: Li-Xu-Huang JPP 2022, Liu AeST 2022, IJHE 2026 full texts (paywalled,
verdicts second-hand).

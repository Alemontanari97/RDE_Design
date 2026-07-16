# G5 Item 2a — DIGITAL PMM TOC SWEEP 1957-1990 (query-bounded deliverable)

Status: RECORD (2026-07-16, [F0/G5-2a], session S7 (operational; renumbered from S6 after reconciliation with the concurrent rigor session S6)). Discharges Item 2a
of the commission (validation/G5_kraiko_pmm_commission.md §3, rescoped
in-house in S4 §6.1). Item 1 (Kraiko 1979 monograph TOC) and Item 2b
(full-text read of the papers flagged below + Izv. AN SSSR MZhG) remain
HUMAN/LIBRARY tasks — this sweep produces Item 2b's reading list.

## 0. Query bounds and method (chain of custody)

SOURCE: the official archive pmm.ipmnet.ru/ru/Issues/<year>/<vol>-<n>,
years 1957-1990 = volumes 21-54 (volume = year - 1936), issues 1-6:
**204/204 issue TOCs fetched and screened, zero gaps** (six parallel
agents, per-window reports preserved in the S6 session transcript).
SCREENING LEVEL: titles + author fields only (the TOC pages carry no
abstracts) — a title-level negative is NOT a full-text negative; that
is exactly why the flagged list feeds Item 2b.

METHOD FINDING OF RECORD (binds any future sweep of this archive): the
WebFetch summarizer FABRICATES plausible authors/titles on these
windows-1251-encoded pages (verified independently by multiple agents
against raw HTML). All summarized content was DISCARDED; the sweep of
record was done by raw-HTML fetch + windows-1251 decode + deterministic
TOC-table parsing, with per-issue verification that the parsed entry
count equals the site's own declared count ("Статей в выпуске"), total
~4,300 entries screened. Every flagged citation below was transcribed
from parsed raw HTML, never from a model summary.

AUTHOR SCREEN (all co-author positions): Крайко, Шмыглевский,
Тилляева, Егорян + school co-authors (Борисов, Шипилин, Наумова,
Осипов А.А., Слободкина, Гринь, Ни, Широносов, Шеломовский).
KEYWORD SCREEN: сопло/сопел, вариацион-, оптимальн-, контур,
профилирование, сверхзвуков-, сопряженн- (adjoint/conjugate),
осредн-, периодическ-, нестационарн-, импульс, тяга, реактивн-.

## 1. VERDICTS AGAINST THE COMMISSION CRITERIA (title-level)

(c)+(e) — ADJOINT/"сопряженные уравнения" in connection with
  contouring, pre-2001: **ZERO title hits in 34 years.** No PMM title
  1957-1990 combines adjoint/conjugate equations with gas-dynamic
  contouring; the multiplier-field school never uses the word in
  titles. → **G14 (P-2's bridge-lemma novelty) SURVIVES the digital
  pass**; residual = full-text bodies (Item 2b) + Kraiko 1979 (Item 1).
  Closest title (goes to 2b): Орел, «Задачи в вариациях для плоских
  околозвуковых течений газа», PMM 35(3) 1971, 499-511 (+ remark
  36(5) 1972, 941-943) — "equations in variations" for transonic flow.

(a)+(d) — one contour vs a FAMILY/ensemble/AVERAGED/PERIODIC inflow:
  **no direct hit** (no title contains averaged/periodic inflow +
  shape). HOWEVER, three antecedent lines MUST be read in full text
  before P-1's G6 wording is frozen (D4 §3 contingency armed, wording
  NOT yet downgraded — the objects in the titles are single-state or
  multi-regime, not measure-averaged):
   A1 (TOP FLAG) **Крайко А.Н., Осипов А.А.** — «О построении контура
      сверхзвукового сопла с учетом изменения условий полета
      летательного аппарата», PMM **34(6) 1970, 1067-1075** — nozzle
      contour built "accounting for the variation of the flight
      conditions": the altitude/multi-regime cousin of the cycle
      average (cf. M0 T3 Corollary C2: cycle average and altitude
      average are one mathematics). Whether it optimizes a WEIGHTED/
      AVERAGED functional over the regime family (would touch G6) or
      a constrained/multi-point design (would not) is EXACTLY the
      Item 2b question.
   A2 **Крайко, Тилляева** — «К построению контура минимального
      волнового сопротивления в неоднородном сверхзвуковом потоке»,
      PMM **37(3) 1973, 469-487**, and its ancestor **Шипилин**, PMM
      **28(3) 1964, 543-547** — optimal contour in a NONUNIFORM
      (spatially, not ensemble-) varying inflow.
   A3 **Панасюк А.И., Панасюк В.И.** — «Оптимальное управление с
      усредненным вдоль траектории функционалом», PMM **49(4) 1985,
      524-535** — time-averaged objective, abstract control theory
      (no PDE/shape): methodological adjacency only.

(b) — unsteady/periodic-flow nozzle OPTIMIZATION beyond 1-D impulse:
  **zero hits** (all periodic/unsteady nozzle titles are analysis,
  not design; e.g. Крайко-Ни PMM 44(1) 1980 gas oscillations in
  tubes — physics only).

## 2. The classical line mapped (context corpus, by window)

1957-62 (founding): Шмыглевский 21(2) 195-206 («Некоторые вариационные
  задачи газовой динамики осесимметричных сверхзвуковых течений» —
  the founding exact variational-contour paper); 22(2) 269-273
  (+ correction 24(2) 392); 24(5) 923-926; capstone 26(1) 110-125
  («Вариационные задачи для сверхзвуковых тел вращения и сопел»);
  Рыжов-Шмыглевский 25(3) 453-455. Adjacent optimal-shape cluster:
  Коган 21(2), Жилин 21(2), Булыгина 22(6), Жигулев-Жилин 23(6),
  Гонор 24(6). Laval-nozzle flow analysis line (Рыжов et al.) mapped,
  not design.
1963-68 (school forms): Борисов-Шмыглевский 27(1) 183-185 (formulation
  of variational problems); Шипилин 27(2) 342 (discontinuous
  solutions); Крайко-Наумова-Шмыглевский 28(1) 178-182;
  **Борисов-Шипилин 28(1) 182-183 (maximum-thrust nozzles with
  ARBITRARY ISOPERIMETRIC CONDITIONS — P-2 §2 must cite)**; Крайко
  28(2) 285-295 (variational problems of NONEQUILIBRIUM and
  equilibrium flows — the reacting-gas line, Hoffman's Soviet twin:
  2b read); Крайко 30(2) 312-320 (general method for variational
  problems of supersonic gas dynamics); Борисов 29(1) 106-113 (3-D);
  Крайко-Осипов 32(4) 596-605 (two-phase variational); Miele 31(3)
  548-551.
1969-74 (Tillyaeva enters): A1 + A2 above; Крайко-Тилляева 35(4)
  619-632 (composite-nozzle variational problem); Петухов-Троицкий
  36(4) 578-588 (variational optimization for hyperbolic equations);
  Островский-Пелиновский 36(1) 71-78 (averaged variational principle
  for periodic waves — Whitham-type, methodological).
1975-80 (stability decade): Гринь-Крайко-Тилляева 39(3), 40(3), 41(4);
  Крайко-Широносов 40(4), 44(4); Крайко 43(3) 500-510; Крайко-Ни
  44(1) 77-88; Федоров 39(6) 1032-1042 (Legendre condition in optimal
  supersonic gas dynamics — 2b read for the second-order theory);
  Бутов-Васенин-Шелуха 41(1) 59-64 (NLP route to variational gas
  dynamics); Петухов 39(2) 260-270, 41(3) 387-398 (hyperbolic
  boundary control).
1981-85: Крайко 45(2) 256-265 («Вариационные принципы для течений
  идеального газа с сильными разрывами» — variational principles WITH
  SHOCKS in Eulerian variables: 2b read, touches P-2 §6/G12 framing);
  Слободкина-Яновская 47(3) 411-420; A3 above; Kraiko two-phase/shock
  papers (author hits only).
1986-90: Крайко 51(6) 941-950 (extremal configurations, max critical
  Mach); Григоренко-Крайко 50(1); Крайко-Мунин 53(3); Елизаров-Федоров
  54(4) 571-580 (inverse-BVP shape optimization, Kazan school).

NEGATIVE RESULTS OF RECORD: Егорян — zero occurrences 1957-1990
(consistent with a post-1990 debut); Шмыглевский absent after 1962 in
PMM; Тилляева appears ONLY 1971-1977 with Kraiko (the Kraiko-Tillyaeva
contouring line of the 1980s+ evidently published outside PMM — Izv.
AN SSSR MZhG / TsAGI: exactly the commission's MZhG residual).

## 3. Item 2b priority reading list (ranked)

 1. Крайко-Осипов PMM 34(6) 1970 (A1 — G6-critical).
 2. Крайко-Тилляева PMM 37(3) 1973 + Шипилин PMM 28(3) 1964 (A2).
 3. Крайко PMM 28(2) 1964 (nonequilibrium variational — multiplier
    fields? adjoint avant la lettre on the Soviet side? G14-critical).
 4. Крайко PMM 30(2) 1966 (the general method paper) and Крайко PMM
    45(2) 1981 (variational principles with shocks).
 5. Орел PMM 35(3) 1971 (equations in variations, transonic).
 6. Борисов-Шипилин PMM 28(1) 1964; Федоров PMM 39(6) 1975.
 7. Шмыглевский PMM 21(2) 1957 and 26(1) 1962 (historical anchors for
    P-2 §2; English translations exist).

## 4. Gate G5 status after this deliverable

Item 2a: DONE (this record). Item 1 (Kraiko 1979 TOC) + Item 2b (list
above) + MZhG originals: still HUMAN (dispatch package ready,
validation/G5_dispatch_email.md — user click pending). G5 continues to
BLOCK submissions, not work. Novelty status: G14 unharmed at TOC
level; G6 wording CONTINGENT on the A1 full text (contingency D4 §3
armed, not activated).

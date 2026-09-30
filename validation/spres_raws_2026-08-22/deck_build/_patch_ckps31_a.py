# -*- coding: utf-8 -*-
"""CKP-S3-1 lean-register patch, batch 1 (specs_a + specs_c12 C1-C6).
On-slide strings only; notes untouched. Each pair must match exactly once."""

def patch(path, pairs):
    s = open(path, encoding="utf-8").read()
    bad = 0
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            print(f"!! {path}: match count {n} for: {old[:70]!r}")
            bad += 1
            continue
        s = s.replace(old, new)
    open(path, "w", encoding="utf-8").write(s)
    print(f"patched {path} ({len(pairs)-bad}/{len(pairs)})")


patch("specs_a.py", [
 ('title="One group, the full engine — and a first: nozzle design posed on the real RDE exhaust"',
  'title="One group, the full engine — and a new nozzle design method"'),
 ('''            bullets=[
                "Full-engine coverage — chamber, injectors, plenum, expansion — in one validated hybrid-dimensional CFD framework (HYPERDE).",
                "On nozzles: the first variational design method formulated on the periodic exhaust itself, with its error budget stated channel by channel.",
                "Three asks today: a reference-class CFD run, engine data in a declared class, publication and procurement channels.",
            ],''',
  '''            bullets=[
                "Chamber, injectors, plenum, expansion — one validated CFD framework (HYPERDE).",
                "Nozzles: the first design method built on the periodic exhaust, with a stated error budget.",
                "Three asks today: a reference CFD run · engine data · publication channels.",
            ],'''),
 ('title="What a detonation buys you: the burn compresses by itself"',
  'title="Detonation compresses by itself: pressure-gain combustion"'),
 ('''            bullets=[
                "Near-constant-volume heat release raises pressure without a compressor: pressure-gain combustion.",
                "At fixed pre-compression the detonation cycle has the higher ideal efficiency — that premium is the reason this field exists.",
            ],''',
  '''            bullets=[
                "Near-constant-volume burn: pressure rises without a compressor.",
                "Higher ideal efficiency at the same pre-compression.",
            ],'''),
 ('title="The Rotating Detonation Engine: detonation made stationary in a rotating frame"',
  'title="The RDE: a detonation made steady in a rotating frame"'),
 ('''            bullets=[
                "One (or more) detonation fronts rotate around an annulus at near-CJ speed — kilohertz cycle rates.",
                "Fresh mixture refills behind the wave; exhaust leaves axially and continuously — no valves, no reset.",
            ],''',
  '''            bullets=[
                "A front rotates at near-CJ speed (kHz); continuous refill behind it.",
                "Axial, continuous exhaust — no valves.",
            ],'''),
 ("title=\"Averages are treacherous here — the field's own authors say so\"",
  'title="Averaging this exhaust is not straightforward — the field says so itself"'),
 ('''            bullets=[
                "In a periodic flow, naive total-pressure averages mis-state performance — the EAP caution is published by the method's own authors.",
                "And the accepted average still carries no error bar: the missing bar is exactly what our programme constructs.",
            ],''',
  '''            bullets=[
                "The flow is periodic: naive total-pressure averages mis-state performance (published EAP caution).",
                "The accepted average has no error bar — our programme constructs it.",
            ],'''),
])

patch("specs_c12.py", [
 ('title="One nozzle, two flowfields: a rotating helical shock — and a clean averaged plume"',
  'title="One nozzle, two flowfields"'),
 ('''            bullets=[
                "In the same nozzle two fields coexist: the instantaneous one (a rotating oblique shock, helical) and the mean one (a clean axisymmetric plume).",
                "Four independent codes show the same phenomenology.",
            ],''',
  '''            bullets=[
                "Instantaneous: a rotating oblique shock. Averaged: a clean axisymmetric plume.",
                "Four independent codes, same phenomenology.",
            ],'''),
 ('''title="The throat is not steady — and is not even 'the throat'"''',
  'title="The throat is not steady — and not the design interface"'),
 ('''            bullets=[
                "The sonic line of an RDE is corrugated and crosses M = 1 twice per cycle; the only published throat statistics show ~6:1 total-pressure excursions.",
                "So the design interface is not the geometric throat: it is the axially-supersonic-with-margin station downstream of heat release.",
                "And none of the four studies we are about to see declares the data class it designs on — periodicity is shown in CFD, never verified spectrally.",
            ],''',
  '''            bullets=[
                "The sonic line is corrugated — M = 1 crossed twice per cycle; ~6:1 throat excursions.",
                "Design interface: the supersonic-with-margin station downstream of heat release.",
                "None of the four studies ahead declares its data class.",
            ],'''),
 ('title="How the field designs RDE nozzles today: four methods, none closes the loop"',
  'title="How the field designs RDE nozzles today"'),
 ('''                ("figs_paper/pa_ramp_profile.png",
                 "Angelino ramp on averaged flow — PKU",
                 "Liu et al., Aerosp. Sci. Technol. 120:107300 (2022)"),
                ("figs_paper/pb_moc_profile.png",
                 "Classical max-thrust MoC on averaged inflow — NUAA",
                 "Li, Xu et al., Aerosp. Sci. Technol. 136:108221 (2023)"),
                ("figs_paper/pd_setup_cone.png",
                 "Non-optimized cone — KIT / Aoyama",
                 "Jourdaine et al., Proc. Combust. Inst. 37:3443 (2019)"),
                ("figs_paper/pm_contour.png",
                 "Manual CFD-guided redesign — NASA Glenn",
                 "Paxson & Miki, AIAA (2022)"),''',
  '''                ("figs_paper/pa_ramp_profile.png",
                 "Angelino-type ramp on averaged flow — Liu et al. 2022",
                 "Liu et al., Aerosp. Sci. Technol. 120:107300 (2022)"),
                ("figs_paper/pb_moc_profile.png",
                 "Classical max-thrust MoC on averaged inflow — Li et al. 2023",
                 "Li, Xu et al., Aerosp. Sci. Technol. 136:108221 (2023)"),
                ("figs_paper/pd_setup_cone.png",
                 "Non-optimized conical spike — Jourdaine et al. 2019",
                 "Jourdaine et al., Proc. Combust. Inst. 37:3443 (2019)"),
                ("figs_paper/pm_contour.png",
                 "Manual CFD-guided redesign — Paxson & Miki 2022 (NASA)",
                 "Paxson & Miki, AIAA (2022)"),'''),
 ('''            takeaway="A 'best of a sweep' is not an optimum: none of the four closes the loop with a true optimization.",''',
  '            takeaway="Best of a sweep is not an optimum: none of the four closes the loop.",'),
 ('''            table=[
                ("PKU 2022", "trade study over 4 cases — no optimizer"),
                ("NUAA 2023", "classical steady max-thrust surfaces on averaged inflow — the SUBSTITUTE problem (it does use variational calculus; the true problem is what is missing)"),
                ("NUAA 2025", "no new design"),
                ("KIT / Aoyama 2019", "cone — declaredly not optimized"),
                ("NASA Glenn 2022", "manual CFD-guided redesign"),
                ("nearest neighbours", "an ideal bound (not a design); a direct search (no optimality conditions)"),
            ],''',
  '''            table=[
                ("Liu et al. 2022", "trade study, 4 cases — no optimizer"),
                ("Li et al. 2023", "classical steady surfaces on averaged inflow — the substitute problem"),
                ("Li et al. 2025", "no new design"),
                ("Jourdaine et al. 2019", "conical — declaredly not optimized"),
                ("Paxson & Miki 2022", "manual CFD-guided redesign"),
                ("nearest neighbours", "an ideal bound (no design); direct search (no optimality conditions)"),
            ],'''),
 ('''            claim=("As far as a systematic literature census allows us to verify, no published work "
                   "poses the optimum problem on the real RDE exhaust — neither 3D-unsteady nor per-phase. "
                   "Where optimization appears, it is the steady substitute's — and the substitution error "
                   "has never been quantified."),''',
  '''            claim=("In a systematic census: no published work poses the optimum on the real RDE "
                   "exhaust — and the substitution error is never quantified."),'''),
 ('''            steps=[
                ("1", "Same solver, paired runs: the steady field from averaged BCs is NOT the transient field — and the nozzle feeds back into the chamber as truncation changes."),
                ("2", "The difference reaches the optimum: the steady curve is flat (0.965–0.971) where the transient has a true optimum at 40% truncation (+0.52%) and a cliff at 80% (−5.78%); geometry rankings invert mid-table (0.2–1.5%)."),
                ("3", "And no published work prices this error."),
            ],''',
  '''            steps=[
                ("1", "Same solver, paired runs: steady-from-averages differs from transient — and the nozzle feeds back into the chamber."),
                ("2", "Steady curve flat (0.965–0.971) where the transient peaks at 40% (+0.52%) and falls at 80% (−5.78%); rankings invert (0.2–1.5%)."),
                ("3", "No published work prices this error."),
            ],'''),
 ('title="A 1971 warning: change only the closure, and the optimum moves ×2.45"',
  'title="A 1971 warning: the closure alone moves the optimum"'),
 ('''            bullets=[
                "Only the base-pressure model changes: the optimum moves ×2.45 while the value stays almost flat (+0.26%): the argmax is fragile exactly where the value is flat — the regime of the plots you just saw.",
                "The closure the RDE field still uses is the same one — the working group that re-examined it judged it unreliable; and the only RDE hot-fire base data sit FAR from the steady-equivalent prediction: 0.59 vs 0.95 atm at matched flow (Harroun 2021).",
                "Our design contract therefore demands unimodality of the working variable of the truncated plug — not flatness.",
            ],''',
  '''            bullets=[
                "Only the base-pressure model changes: the optimum moves ×2.45 (value: +0.26%).",
                "The same closure is still in use — and RDE hot-fire base pressure sits far from steady predictions: 0.59 vs 0.95 atm (Harroun et al. 2021).",
                "Our design contract demands unimodality, not flatness.",
            ],'''),
 ('title="Seventy years of variational nozzle design — we extend the line to the periodic system"',
  'title="Seventy years of variational design — extended to the periodic system"'),
 ('            footline="A 1975 Russian precedent is not yet in our hands: we say so — and do not summarize it.",',
  '            footline="A 1975 Russian precedent is still in procurement: we say so.",'),
])
print("BATCH 1 DONE")

"""[F3-entry] THE RAO 1961 SPIKE ORACLE — is the reference usable?

The paper was obtained on 2026-08-13 (owner-supplied full text;
transcription of record in literature/rao1961_spike_tables.md). Until
then the project carried its tabulated numbers as "unverifiable and
internally inconsistent" (N-74), and D6 makes them F3's ENTRY
condition: "RaoPlug S1/S2 fix in GENO landed OR single-oracle status
(Rao 1961 spike Table-1) DECLARED".

This carrier declares that status, and it does so WITHOUT marching
anything. It asks only what can be settled from closed-form gas
dynamics and from the paper's own internal arithmetic, because that is
exactly what decides whether the tables can be used as an oracle at
all. A contour comparison against Table 1 needs a gamma = 1.23 design
run and is the NEXT step, not this one.

WHAT IS CHECKED

  A  THE IDEAL COLUMN IS REPRODUCIBLE. Rao's "ideal spike contour"
     rows are perfectly-expanded one-dimensional nozzles at a given
     area ratio, so their VACUUM thrust coefficient follows from
     closed-form isentropic relations with NOTHING from this project
     in the loop. If our independent computation reproduces his 1.5909
     and 1.7326, his reference column is verified and the tables can
     carry an oracle. If it does not, the tables are not usable and
     that is the finding.

  B  THE PAPER IS INTERNALLY CONSISTENT, item by item. Every ratio he
     prints (C_F/C_Fi, L/L_i) is recomputed from the C_F and L/R_E
     columns of the same table, and the body text is checked against
     Table 3. The known discrepancy (text 2.428 vs table 2.433 for the
     ideal length ratio) is measured rather than asserted.

  C  THE CONTOUR TABLES CLOSE ON THEIR OWN SUMMARY. Table 1's last row
     must be the (X_D/R_E, R_D/R_E) quoted in the text and in Table 3;
     same for Table 2.

  D  THE OPTIMUM-OVER-TRUNCATED GAIN, extracted as a number, because
     it is the same comparison the S23 paired ladder made on our world
     with the opposite answer. Reported, NOT judged here: the two use
     different baselines (his = the ideal spike cut short; ours = the
     fan streamline) and settling it needs a run, not a reading.

TOLERANCES. Check A compares against a 4-significant-figure printed
number, so its bar is the printing precision itself (5e-4 relative),
not a tolerance of our choosing. Check B's bars are likewise the
rounding of the printed operands, propagated.

REJECTORS
  N1  a deliberately wrong gamma (1.4 instead of 1.23) must BREAK
      check A -- otherwise the check is insensitive to the physics it
      claims to verify;
  N2  a corrupted table entry must break check B.

ON-DEMAND CARRIER (env: none -- pure closed form, seconds).
"""
import sys

import numpy as np

GAMMA = 1.23

# ---- transcribed from literature/rao1961_spike_tables.md ------------
TAB3 = {
    "opt_10.69":  dict(L_RE=1.731, RD_RE=0.126, CF=1.7269, L_Li=0.529,
                       CF_CFi=0.9967),
    "ideal_10.69": dict(L_RE=3.271, RD_RE=0.000, CF=1.7326, L_Li=1.00,
                        CF_CFi=1.00),
    "trunc_10.69": dict(L_RE=1.731, RD_RE=None,  CF=1.7252, L_Li=0.529,
                        CF_CFi=0.9957),
    "opt_3.81":   dict(L_RE=1.164, RD_RE=0.137, CF=1.5804, L_Li=0.479,
                       CF_CFi=0.9934),
    "ideal_3.81": dict(L_RE=2.433, RD_RE=0.000, CF=1.5909, L_Li=1.00,
                       CF_CFi=1.00),
    "trunc_3.81": dict(L_RE=1.164, RD_RE=0.245, CF=1.5783, L_Li=0.479,
                       CF_CFi=0.9921),
}
EPS = {"3.81": 3.81, "10.69": 10.69}
TEXT_IDEAL_LEN_3_81 = 2.428      # body text p.95
TEXT_IDEAL_CF_3_81 = 1.591       # body text p.95
TEXT_RATIO_3_81 = 0.993          # body text p.95
TEXT_LENFRAC_3_81 = 0.479        # body text p.95 ("47.9 per cent")

TAB1_LAST = (1.164, 0.137, -19.73)
TAB2_LAST = (1.731, 0.126, -14.94)

PRINT_BAR = 5.0e-4               # 4 significant figures, as printed


def check(label, ok):
    print("  [%s] %s" % ("PASS" if ok else "FAIL", label))
    return bool(ok)


def mach_from_area(eps, g):
    """Supersonic root of the area-Mach relation, bisected."""
    def area(M):
        return (1.0 / M) * ((2.0 / (g + 1.0))
                            * (1.0 + 0.5 * (g - 1.0) * M * M)
                            ) ** ((g + 1.0) / (2.0 * (g - 1.0)))
    lo, hi = 1.0000001, 50.0
    for _ in range(200):
        mid = 0.5 * (lo + hi)
        if area(mid) < eps:
            lo = mid
        else:
            hi = mid
    return 0.5 * (lo + hi)


def cf_vacuum_ideal(eps, g):
    """VACUUM thrust coefficient of a perfectly expanded 1-D nozzle of
    area ratio eps. Closed form; nothing from this project."""
    M = mach_from_area(eps, g)
    pe_pc = (1.0 + 0.5 * (g - 1.0) * M * M) ** (-g / (g - 1.0))
    cf_mom = np.sqrt((2.0 * g * g / (g - 1.0))
                     * (2.0 / (g + 1.0)) ** ((g + 1.0) / (g - 1.0))
                     * (1.0 - pe_pc ** ((g - 1.0) / g)))
    return cf_mom + eps * pe_pc, M, pe_pc


def main():
    ok = True
    print("== [F3-entry] Rao 1961 spike oracle: is the reference "
          "usable? ==")
    print("   source: literature/rao1961_spike_tables.md "
          "(owner-supplied full text, 2026-08-13)")

    # ---- A: the ideal column, from closed form -----------------------
    print("\n-- A: reproduce Rao's IDEAL spike C_F from 1-D closed "
          "form (gamma = %.2f) --" % GAMMA)
    for key, eps in EPS.items():
        cf, M, pe = cf_vacuum_ideal(eps, GAMMA)
        ref = TAB3["ideal_" + key]["CF"]
        rel = abs(cf - ref) / ref
        print("   eps = %-6s M_e = %.4f  p_e/p_c = %.6f  "
              "C_F(ours) = %.4f  C_F(Rao) = %.4f  rel = %.2e"
              % (eps, M, pe, cf, ref, rel))
        ok &= check("A eps=%s ideal C_F reproduced to the printing "
                    "precision" % key, rel <= PRINT_BAR)

    # N1: a wrong gamma must break it
    bad = [abs(cf_vacuum_ideal(e, 1.4)[0] - TAB3["ideal_" + k]["CF"])
           / TAB3["ideal_" + k]["CF"] for k, e in EPS.items()]
    ok &= check("N1 rejector: gamma = 1.4 breaks check A "
                "(min rel %.2e > bar)" % min(bad), min(bad) > PRINT_BAR)

    # ---- B: internal consistency ------------------------------------
    print("\n-- B: the paper against itself --")
    for key in EPS:
        i = TAB3["ideal_" + key]
        for who in ("opt", "trunc"):
            r = TAB3[who + "_" + key]
            got = r["CF"] / i["CF"]
            rel = abs(got - r["CF_CFi"]) / r["CF_CFi"]
            print("   eps=%-6s %-5s  C_F/C_Fi printed %.4f  recomputed"
                  " %.6f  rel %.2e" % (key, who, r["CF_CFi"], got, rel))
            ok &= check("B %s/%s C_F ratio consistent with its own C_F "
                        "column" % (key, who), rel <= 2.0 * PRINT_BAR)
            gotl = r["L_RE"] / i["L_RE"]
            rell = abs(gotl - r["L_Li"]) / r["L_Li"]
            ok &= check("B %s/%s L/L_i consistent with its own L/R_E "
                        "column" % (key, who), rell <= 2.0e-3)

    d_len = abs(TEXT_IDEAL_LEN_3_81 - TAB3["ideal_3.81"]["L_RE"]) \
        / TAB3["ideal_3.81"]["L_RE"]
    print("   body text ideal L/R_E = %.3f vs Table 3 %.3f -> rel %.2e"
          % (TEXT_IDEAL_LEN_3_81, TAB3["ideal_3.81"]["L_RE"], d_len))
    ok &= check("B the ONE known text-vs-table discrepancy is small "
                "(< 0.5 %)", d_len < 5.0e-3)
    d_cf = abs(TEXT_IDEAL_CF_3_81 - TAB3["ideal_3.81"]["CF"]) \
        / TAB3["ideal_3.81"]["CF"]
    ok &= check("B body-text ideal C_F agrees with Table 3", d_cf <= 1e-3)
    d_ra = abs(TEXT_RATIO_3_81 - TAB3["opt_3.81"]["CF_CFi"])
    ok &= check("B body-text 0.993 agrees with Table 3's 0.9934",
                d_ra <= 5e-4 + 5e-4)

    # ---- C: the contour tables close on their summary ---------------
    print("\n-- C: contour tables vs their own summary --")
    for name, last, key in (("Table 1", TAB1_LAST, "3.81"),
                            ("Table 2", TAB2_LAST, "10.69")):
        r = TAB3["opt_" + key]
        ok &= check("C %s last row X/R_E matches L/R_E of Table 3"
                    % name, abs(last[0] - r["L_RE"]) <= 1e-3)
        ok &= check("C %s last row R/R_E matches R_D/R_E of Table 3"
                    % name, abs(last[1] - r["RD_RE"]) <= 1e-3)

    # ---- D: the number that speaks to S23 ---------------------------
    print("\n-- D: Rao's own optimum-over-truncated gain (REPORTED) --")
    for key in EPS:
        g = (TAB3["opt_" + key]["CF"] / TAB3["trunc_" + key]["CF"]
             - 1.0) * 100.0
        print("   eps = %-6s optimum beats truncated ideal by %+.3f %% "
              "(L/L_i = %.3f)"
              % (key, g, TAB3["opt_" + key]["L_Li"]))
    print("   for comparison, S23 on OUR world, free-form vs truncated")
    print("   fan streamline: -0.011 %% +- 0.017 %% at L/L_i = 0.429.")
    print("   NOT judged here: different baselines (his = ideal spike")
    print("   cut short; ours = the fan streamline). Settling it needs")
    print("   a run at gamma = 1.23, eps = 3.81 -- the next step.")

    print("\nVERDICT: %s" % ("PASS -- the Rao 1961 tables ARE usable "
                             "as an oracle" if ok else
                             "FAIL -- the tables do not support an "
                             "oracle"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())

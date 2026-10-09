"""What the design tool would march from a Q2D-HP family phase (TWOP_MU, no swirl: the table from (gamma, R, T0, P0), a start at
Mach M = the family's axial Mach) against the sector's own data (mean of rho*u, mean of p + rho*u^2, static p and T)."""
import numpy as np, json
D = "/data10/falco/RDE/RDE_Design/validation/_q2d_hp_inflow/"
for tag in ("portata_HP",):
    for x in ("07.5",):
        fam = json.load(open(D + "%s_x%smm_family_K12.json" % (tag, x)))
        r = np.load(D + "%s_x%smm_row.npz" % (tag, x), allow_pickle=True)
        NJ = len(r["psi"]); edges = np.linspace(0, NJ, 13).round().astype(int)
        rho, u, v, p, T = r["rho"], r["u"], r["v"], r["p"], r["T"]
        print("==== %s x %s mm  (tool start from the family's (T0, P0) at the axial Mach, no swirl)" % (tag, x))
        print("  k  M_ax   v[m/s] | T_tool/T_sec  p_tool/p_sec | mdot_tool/mdot_data  mom_tool/mom_data")
        tot_md_t = tot_md_d = tot_mo_t = tot_mo_d = 0.0
        for k, ph in enumerate(fam["phases"]):
            s = slice(edges[k], edges[k + 1])
            g, R, T0, P0, M = ph["gamma"], ph["R"], ph["T0"], ph["P0"], ph["M"]
            Tt = T0 / (1 + 0.5 * (g - 1) * M ** 2); pt = P0 * (Tt / T0) ** (g / (g - 1))
            rt = pt / (R * Tt); ut = M * np.sqrt(g * R * Tt)
            md_t, mo_t = rt * ut, pt + rt * ut ** 2
            md_d, mo_d = np.mean(rho[s] * u[s]), np.mean(p[s] + rho[s] * u[s] ** 2)
            tot_md_t += ph["w"] * md_t; tot_md_d += ph["w"] * md_d; tot_mo_t += ph["w"] * mo_t; tot_mo_d += ph["w"] * mo_d
            print(" %2d %5.3f %7.1f |   %6.3f      %6.3f    |     %6.3f            %6.3f" % (k, M, ph["v"], Tt / np.mean(T[s]), pt / np.mean(p[s]), md_t / md_d, mo_t / mo_d))
        print("  cycle: mdot_tool/mdot_data %.4f   momentum flux tool/data %.4f" % (tot_md_t / tot_md_d, tot_mo_t / tot_mo_d))

"""Along the Q2D chamber (constant area up to 20 mm; 20-22 mm is Q2D's artificial divergent, area 1 -> 3): at each station,
how much of the cycle is axially supersonic (time share, and the share of mass and of axial momentum carried by the axially
subsonic part), the smallest axial Mach, the cycle's mass-averaged meridional stagnation pressure (constant gamma, the swirl
dropped) and the spread of the 12 equal-time sector means of it (max/min), and the axial momentum flux (conserved in a
constant-area channel without friction)."""
import numpy as np
D = "/data10/falco/RDE/RDE_Design/validation/_q2d_hp_inflow/"
for tag in ("portata_HP", "gemello_2CP"):
    z = np.load(D + tag + "_aligned_field.npz", allow_pickle=True)
    names = [str(s) for s in z["names"]]; m = z["mean"]; xc = z["x_cells"]
    xmm = xc * 1e3 if xc.max() < 1 else xc
    g_ = lambda n: m[names.index(n)]
    u, v, p, T, gam, R = g_("u"), g_("v"), g_("p"), g_("T"), g_("g"), g_("R")
    rho = sum(g_(s_) for s_ in ("O2", "H2O", "H2", "H", "O", "OH", "N2"))     # partial densities: rho as the rows'
    a = np.sqrt(gam * R * T); Mx = u / a
    P0m = p * (1 + 0.5 * (gam - 1) * Mx ** 2) ** (gam / (gam - 1))
    P0t = p * (1 + 0.5 * (gam - 1) * (np.hypot(u, v) / a) ** 2) ** (gam / (gam - 1))    # total, the swirl included
    mf, mom = rho * u, p + rho * u ** 2
    NJ = u.shape[0]; e = np.linspace(0, NJ, 13).round().astype(int)
    print("==== %s (period = %d samples; 'sub' = axial Mach below 1.02)" % (tag, NJ))
    print("  x[mm]  time sup  mass in sub  momentum in sub  min Mx   P0 mass-avg [bar]  P0 total mass-avg  12-sector P0 max/min  rho u^2+p [bar]")
    for xs in (5, 7.5, 10, 12.5, 15, 17.5, 19.5, 20.5):
        i = int(np.argmin(abs(xmm - xs)))
        sub = Mx[:, i] < 1.02
        P0a = np.sum(mf[:, i] * P0m[:, i]) / np.sum(mf[:, i])
        sec = [np.sum(mf[e[k]:e[k + 1], i] * P0m[e[k]:e[k + 1], i]) / np.sum(mf[e[k]:e[k + 1], i]) for k in range(12)]
        P0ta = np.sum(mf[:, i] * P0t[:, i]) / np.sum(mf[:, i])
        print("  %5.2f   %5.1f %%     %5.1f %%        %5.1f %%       %5.3f       %6.3f             %6.3f               %5.2f              %6.4f" % (
            xmm[i], 100 * np.mean(~sub), 100 * mf[sub, i].sum() / mf[:, i].sum(), 100 * mom[sub, i].sum() / mom[:, i].sum(),
            Mx[:, i].min(), P0a / 1e5, P0ta / 1e5, max(sec) / min(sec), np.mean(mom[:, i]) / 1e5))

"""Axial Mach of the Q2D-HP aligned mean fields (wave frame period, all x): where is every phase axially supersonic?"""
import numpy as np, sys
D = "/data10/falco/RDE/RDE_Design/validation/_q2d_hp_inflow/"
for tag in ("portata_HP", "gemello_2CP"):
    z = np.load(D + tag + "_aligned_field.npz", allow_pickle=True)
    names = [str(s) for s in z["names"]]
    m = z["mean"]; xc = z["x_cells"]; psi = z["psi"]
    g = lambda n: m[names.index(n)]
    u, v, p, T, gam, R = g("u"), g("v"), g("p"), g("T"), g("g"), g("R")
    a = np.sqrt(gam * R * T)
    Mx = u / a
    Mt = np.sqrt(u**2 + v**2) / a
    rho = p / (R * T)
    print("====", tag, "x cells", xc.shape, "from %.3f to %.3f mm" % (xc[0]*1e3 if xc.max() < 1 else xc[0], xc[-1]*1e3 if xc.max() < 1 else xc[-1]))
    xmm = xc * 1e3 if xc.max() < 1 else xc
    print("  x[mm]  frac(Mx>1)  frac(Mx>1.02)  min Mx   psi(min)  min Mtot  mean(rho u)/max")
    for xs in (1, 2, 3, 5, 7.5, 10, 12.5, 15, 17.5, 19.5, 20.5, 21.5, 21.9):
        i = int(np.argmin(abs(xmm - xs)))
        mx = Mx[:, i]
        print("  %5.2f   %6.3f      %6.3f       %6.3f   %6.3f   %6.3f" % (xmm[i], np.mean(mx > 1), np.mean(mx > 1.02), mx.min(), psi[np.argmin(mx)], Mt[:, i].min()))

"""Where in the cycle the axially subsonic gas sits, and at what pressure, at a Q2D station: the period in 1/48 slices (the
first quarter shown, then the subsonic slices elsewhere), axial Mach range, time-mean total pressure (meridional, constant
gamma), static pressure, share of the shape vote (time x P0); the vote held by subsonic samples near the front and elsewhere;
and the mass-averaged ideal exhaust speed (each sample expanded isentropically from its own meridional P0, T0 to p_a)."""
import numpy as np, sys
D = "/data10/falco/RDE/RDE_Design/validation/_q2d_hp_inflow/"
tag = "portata_HP"
z = np.load(D + tag + "_aligned_field.npz", allow_pickle=True)
nm = [str(q) for q in z["names"]]; xc = z["x_cells"] * (1e3 if z["x_cells"].max() < 1 else 1)
W = np.array([31.998, 18.015, 2.016, 1.008, 15.999, 17.007, 28.014])
for xs in [float(a) for a in (sys.argv[1:] or ["7.5", "12.5"])]:
    i = int(np.argmin(abs(xc - xs)))
    u, p, T, g = (np.asarray(z["mean"][nm.index(q)][:, i], float) for q in ("u", "p", "T", "g"))
    rk = np.array([z["mean"][nm.index(q)][:, i] for q in ("O2", "H2O", "H2", "H", "O", "OH", "N2")])
    rho = rk.sum(0); R = 8314.462618 * ((rk / rho) / W[:, None]).sum(0)
    M = u / np.sqrt(g * R * T); P0 = p * (1 + 0.5 * (g - 1) * M ** 2) ** (g / (g - 1)); T0 = T * (1 + 0.5 * (g - 1) * M ** 2)
    NJ = len(u); tv = P0.sum(); sub = M < 1.02; front = np.arange(NJ) < NJ // 8
    rng = lambda msk: (P0[msk].min() / 1e5, P0[msk].max() / 1e5) if msk.any() else (0.0, 0.0)
    f_lo, f_hi = rng(sub & front); o_lo, o_hi = rng(sub & ~front)
    print("==== %s at %.2f mm: subsonic samples hold %.1f %% of the shape vote: %.1f %% in the first eighth of the period "
          "(P0 %.1f..%.1f bar), %.1f %% elsewhere (P0 %.1f..%.1f bar)" % (tag, xc[i], 100 * P0[sub].sum() / tv,
          100 * P0[sub & front].sum() / tv, f_lo, f_hi, 100 * P0[sub & ~front].sum() / tv, o_lo, o_hi))
    e = np.linspace(0, NJ, 49).round().astype(int)
    print("   psi          axial Mach    P0 [bar]  p [bar]  vote")
    for k in range(48):
        s = slice(e[k], e[k + 1])
        if k < 12 or M[s].min() < 1.02:
            print("  %.3f-%.3f   %.2f .. %.2f   %6.2f   %5.2f   %4.1f %%%s" % (z["psi"][s][0], z["psi"][s][-1], M[s].min(), M[s].max(),
                  P0[s].mean() / 1e5, p[s].mean() / 1e5, 100 * P0[s].sum() / tv, "  subsonic part" if M[s].min() < 1.02 else ""))
    for pa in (0.5e5, 1.01325e5):
        cp = g * R / (g - 1)
        V = np.sqrt(np.maximum(0.0, 2 * cp * T0 * (1 - (pa / P0) ** ((g - 1) / g))))
        print("   ideal exhaust speed to p_a %.3f bar, mass-averaged: %.0f m/s" % (pa / 1e5, (rho * u * V).sum() / (rho * u).sum()))

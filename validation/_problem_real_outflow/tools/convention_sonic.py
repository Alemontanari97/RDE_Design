"""A SIMPLE DECLARED CONVENTION for the phases at the nozzle's inlet (the Q2D row at 7.5 mm), no CFD in the chain:
(1) K equal-time sectors, phase 0 at the front; the swirl dropped (meridional state: static p, T and axial speed u);
(2) per sector the uniform state that carries exactly the sector's mass, axial momentum and meridional total enthalpy
    (Cumpsty-Horlock's conservation, sector by sector), on the branch of the sector's mass-averaged axial Mach;
(3) a sector below axial Mach 1.02 is replaced by a SONIC SURROGATE at Mach 1.02 (the choking closure O3 of the problem
    book / the sonic family I3 of M0): variant P0 = its own stagnation state kept (the mass follows), variant MASS = its mass
    flux and total temperature kept (the stagnation pressure follows).
Reports what the convention does to the cycle's mass and axial momentum against the row, the stagnation pressure the MASS
variant takes away, and the share of the time and of the shape vote (time x P0, the exact weight of a phase's vote on the shape
when the march is linear in P0) carried by the surrogate phases."""
import numpy as np, sys
D = "/data10/falco/RDE/RDE_Design/validation/_q2d_hp_inflow/"
tag, xs = (sys.argv[1], sys.argv[2]) if len(sys.argv) > 2 else ("portata_HP", "07.5")
try:
    r = np.load(D + "%s_x%smm_row.npz" % (tag, xs), allow_pickle=True)
    rho, u, p, T, g, R = (np.asarray(r[k], float) for k in ("rho", "u", "p", "T", "gamma", "R"))
except FileNotFoundError:
    # any other station: the aligned mean field's nearest cell, exactly as the generator g2cp_inflow.py cut the 5 and 7.5 mm
    # rows (checked: the 7.5 mm row equals the field's cell at 7.49 mm to 6e-8)
    z = np.load(D + tag + "_aligned_field.npz", allow_pickle=True)
    nm_ = [str(q) for q in z["names"]]; xc_ = z["x_cells"] * (1e3 if z["x_cells"].max() < 1 else 1)
    i_ = int(np.argmin(abs(xc_ - float(xs))))
    u, p, T, g = (np.asarray(z["mean"][nm_.index(q)][:, i_], float) for q in ("u", "p", "T", "g"))
    sp_ = ("O2", "H2O", "H2", "H", "O", "OH", "N2")                 # the field stores partial densities (ONERA-7 order)
    W_ = np.array([31.998, 18.015, 2.016, 1.008, 15.999, 17.007, 28.014])
    rk_ = np.array([z["mean"][nm_.index(q)][:, i_] for q in sp_])
    rho = rk_.sum(0)                                               # the row's rho (checked at 7.5 mm: 1.7e-7)
    R = 8314.462618 * ((rk_ / rho) / W_[:, None]).sum(0)           # R of the composition, as the row's (gamma: the field's, 2e-4)
    xs = "%.2f (cell of the aligned field)" % xc_[i_]
NJ = len(u); LINE = 1.02
m_row, I_row = np.mean(rho * u), np.mean(p + rho * u ** 2)


def stag(pp, TT, MM, gg):
    T0 = TT * (1 + 0.5 * (gg - 1) * MM ** 2)
    return pp * (T0 / TT) ** (gg / (gg - 1)), T0


def at_mach(P0, T0, M, gg, RR):
    TT = T0 / (1 + 0.5 * (gg - 1) * M ** 2); pp = P0 * (TT / T0) ** (gg / (gg - 1)); rr = pp / (RR * TT)
    uu = M * np.sqrt(gg * RR * TT)
    return rr * uu, pp + rr * uu ** 2


print("%s at %s mm: row mass flux %.2f kg/m2/s, axial momentum flux %.4f bar" % (tag, xs, m_row, I_row / 1e5))
print("   K  sectors   time    mass in   shape vote  | variant P0: cycle mass  momentum | variant MASS: cycle momentum,"
      "  P0 taken (worst sector)")
print("      replaced  share   them      (time x P0) |")
loss = []
for K in (1, 6, 12, 24, 48):
    e = np.linspace(0, NJ, K + 1).round().astype(int)
    rows = []
    for k in range(K):
        s = slice(e[k], e[k + 1]); w = (e[k + 1] - e[k]) / NJ
        mf = rho[s] * u[s]
        m, I = mf.mean(), (p[s] + rho[s] * u[s] ** 2).mean()
        gk, Rk = (mf * g[s]).sum() / mf.sum(), (mf * R[s]).sum() / mf.sum()
        cp = gk * Rk / (gk - 1)
        h0 = (mf * (cp * T[s] + 0.5 * u[s] ** 2)).sum() / mf.sum()          # meridional: the swirl dropped
        a2, b = (gk + 1) / (2 * (gk - 1)), gk / (gk - 1) * I / m
        disc = b * b - 4 * a2 * h0
        Mx_avg = (mf * u[s] / np.sqrt(g[s] * R[s] * T[s])).sum() / mf.sum()
        uk = (b + np.sqrt(disc)) / (2 * a2) if Mx_avg >= 1 else (b - np.sqrt(disc)) / (2 * a2)
        pk = I - m * uk; Tk = pk * uk / (m * Rk); Mk = uk / np.sqrt(gk * Rk * Tk)
        P0k, T0k = stag(pk, Tk, Mk, gk)
        rows.append((w, m, I, gk, Rk, Mk, P0k, T0k))
    sub = [rw for rw in rows if rw[5] < LINE]
    t_sub = sum(rw[0] for rw in sub); m_sub = sum(rw[0] * rw[1] for rw in sub) / sum(rw[0] * rw[1] for rw in rows)
    vote = sum(rw[0] * rw[6] for rw in sub) / sum(rw[0] * rw[6] for rw in rows)
    mP = IP = IM = 0.0; worst = 0.0
    for (w, m, I, gk, Rk, Mk, P0k, T0k) in rows:
        if Mk >= LINE:
            mP += w * m; IP += w * I; IM += w * I
            continue
        m1, I1 = at_mach(P0k, T0k, LINE, gk, Rk)                  # variant P0: own stagnation state, sonic
        mP += w * m1; IP += w * I1
        P0s = P0k * m / m1                                         # variant MASS: same mass flux -> P0 scales with it
        _, I2 = at_mach(P0s, T0k, LINE, gk, Rk)
        IM += w * I2; worst = max(worst, 1 - P0s / P0k)
    print("  %2d   %2d / %2d   %4.0f %%   %4.0f %%     %4.0f %%      |   %+6.2f %%   %+6.2f %%   |   %+6.2f %%        %4.1f %%" % (
        K, len(sub), K, 100 * t_sub, 100 * m_sub, 100 * vote, 100 * (mP / m_row - 1), 100 * (IP / I_row - 1),
        100 * (IM / I_row - 1), 100 * worst))
    loss.append((K, sum(rw[0] * rw[6] for rw in rows), sum(rw[0] * rw[5] for rw in rows)))
    if K == 1:
        mean_state = rows[0]

Ms_ = u / np.sqrt(g * R * T)
P0_t = np.mean(p * (1 + 0.5 * (g - 1) * Ms_ ** 2) ** (g / (g - 1)))
print("the TIME-mean total pressure of the cycle (the weight of the shape vote, 1.6) carried by the sector states (before the "
      "surrogate): " + ", ".join("K %d %.3f bar" % (K_, P_ / 1e5) for K_, P_, _ in loss) + ", against %.3f bar sample by sample; "
      "time-mean axial Mach of the sector states " % (P0_t / 1e5) + ", ".join("K %d %.3f" % (K_, M_) for K_, _, M_ in loss)
      + ", against %.3f" % Ms_.mean())

w_, m_, I_, g1, R1, M1, P01, T01 = mean_state
print("K = 1 (the mean-state arm, C6): axial Mach %.3f%s, P0 %.3f bar, T0 %.0f K, gamma %.4f, R %.1f J/kg/K" % (
    M1, " -> 1.020 (C5)" if M1 < LINE else "", P01 / 1e5, T01, g1, R1))

# the 12-phase family under the convention (variant P0), and the lip limit of the weakest phase (rough isentropic estimate)
K = 12
e = np.linspace(0, NJ, K + 1).round().astype(int)
print("\nK = 12 under the convention (variant P0): phase, axial Mach of the conserved state -> start Mach, P0 [bar], T0 [K], "
      "mass share, shape-vote share")
fam = []
for k in range(K):
    s = slice(e[k], e[k + 1]); mf = rho[s] * u[s]
    m, I = mf.mean(), (p[s] + rho[s] * u[s] ** 2).mean()
    gk, Rk = (mf * g[s]).sum() / mf.sum(), (mf * R[s]).sum() / mf.sum(); cp = gk * Rk / (gk - 1)
    h0 = (mf * (cp * T[s] + 0.5 * u[s] ** 2)).sum() / mf.sum()
    a2, b = (gk + 1) / (2 * (gk - 1)), gk / (gk - 1) * I / m
    Mx_avg = (mf * u[s] / np.sqrt(g[s] * R[s] * T[s])).sum() / mf.sum()
    uk = (b + np.sqrt(b * b - 4 * a2 * h0)) / (2 * a2) if Mx_avg >= 1 else (b - np.sqrt(b * b - 4 * a2 * h0)) / (2 * a2)
    pk = I - m * uk; Tk = pk * uk / (m * Rk); Mk = uk / np.sqrt(gk * Rk * Tk)
    P0k, T0k = stag(pk, Tk, Mk, gk)
    Ms = max(Mk, LINE); ms = m if Mk >= LINE else at_mach(P0k, T0k, LINE, gk, Rk)[0]
    fam.append((k, Mk, Ms, P0k, T0k, ms, gk))
tm, tv = sum(f[5] for f in fam), sum(f[3] for f in fam)
for (k, Mk, Ms, P0k, T0k, ms, gk) in fam:
    print("  %2d   %.3f -> %.3f   %6.2f   %5.0f   %5.1f %%   %5.1f %%%s" % (k, Mk, Ms, P0k / 1e5, T0k, 100 * ms / tm, 100 * P0k / tv,
          "   (sonic surrogate)" if Mk < LINE else ""))
wk = min(fam, key=lambda f: f[3])
for pa in (0.5e5, 1.01325e5):
    G = wk[6]
    print("  weakest phase %d (P0 %.2f bar): no lip shock at p_a %.3f bar up to a lip Mach of %.2f (isentropic estimate)" % (
        wk[0], wk[3] / 1e5, pa / 1e5, np.sqrt(2 / (G - 1) * ((wk[3] / pa) ** ((G - 1) / G) - 1))))

"""The design tool starts every phase on a VERTICAL line x = x0 (a1_twowall.py: start = (x0, yline, ...)), so its admissibility
condition is the AXIAL Mach u/a >= 1.02 on a vertical cut of the 3-D field, not the normal Mach on a tilted channel face.
For each radial/azimuthal line (j, k) of the channel, the axial Mach of the kept cell planes is interpolated linearly in x at
the cut x = X; the cut is admissible when every line it crosses is above 1.02. Kept planes: i = 0-5, 7, 8, then every 4th
(about 3 mm apart): a dip between kept planes can be missed (declared). Reports the first admissible cut and the smallest axial
Mach on every cut after it up to the lip (the start must stay admissible under the cowl; beyond the lip the block holds
the jet's edge). usage: cfd_axial_mach_vertical.py <run dir>:<lip x mm after the inlet> ..."""
import numpy as np, glob, os, sys
LINE = 1.02
for arg in sys.argv[1:]:
    c, lip_mm = arg.rsplit(":", 1)
    lip_mm = float(lip_mm)
    fn = sorted(glob.glob(c + "/OUTPUT/field*_x.npz"), key=lambda s: int(os.path.basename(s)[5:-6]))[-1]
    z = np.load(fn, allow_pickle=True)
    ni, nj, nk = z["b2_dims"]
    X = z["b2_xyz"].reshape(3, ni * nj * nk)
    P = np.stack([X[q].reshape((ni, nj, nk), order="F") for q in range(3)], -1)
    ip = z["b2_ip_idx"]
    u, T, g, R = (z["b2_ip_" + n] for n in ("u", "T", "g", "R"))
    Mx = u / np.sqrt(g * R * T)                                  # u = the x-velocity: the same in both frames
    xc = np.stack([0.125 * sum(P[i + a, b:nj - 1 + b, d:nk - 1 + d, 0] for a in (0, 1) for b in (0, 1) for d in (0, 1)) for i in ip])
    x_in = P[0, :, :, 0].mean()
    assert np.all(np.diff(xc, axis=0) > 0), "x not increasing along i"
    Xs = np.arange(xc.min(), xc.max(), 0.25e-3)
    mins = []
    for Xc in Xs:
        inside = (xc[0] <= Xc) & (xc[-1] >= Xc)                   # lines the cut crosses
        n1 = np.clip((xc <= Xc).sum(0) - 1, 0, len(ip) - 2)
        jj, kk = np.indices(n1.shape)
        xa, xb = xc[n1, jj, kk], xc[n1 + 1, jj, kk]
        ma, mb = Mx[n1, jj, kk], Mx[n1 + 1, jj, kk]
        m = ma + (mb - ma) * np.clip((Xc - xa) / (xb - xa), 0, 1)
        mins.append(m[inside].min() if inside.any() else np.nan)
    mins = np.array(mins)
    ok = mins > LINE
    under = (Xs - x_in) * 1e3 <= lip_mm
    after = np.array([np.nanmin(mins[n:][under[n:]]) if under[n] else np.nan for n in range(len(mins))])
    first = next((n for n in range(len(Xs)) if after[n] > LINE), None)
    first_any = next((n for n in range(len(Xs)) if ok[n]), None)
    # the kept i-planes, for comparison with the normal Mach: smallest axial Mach and its x span
    print("%s: axial Mach on vertical cuts (inlet at x = %.2f mm; lip %.2f mm after it)" % (c.split("q2dhp/")[1], x_in * 1e3, lip_mm))
    print("   first cut with min Mx > %.2f: %s mm after the inlet;  first cut from which it STAYS above: %s mm" % (
        LINE, "%.2f" % ((Xs[first_any] - x_in) * 1e3) if first_any is not None else "none",
        "%.2f" % ((Xs[first] - x_in) * 1e3) if first is not None else "none"))
    for d in [d for d in (6, 8, 10, 12, 14, 16, 18, 20, 24, 28, 32, 36) if d <= lip_mm]:
        n = int(np.argmin(abs((Xs - x_in) * 1e3 - d)))
        print("     cut %4.1f mm: min axial Mach %.3f" % (d, mins[n]))

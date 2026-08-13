"""W-5 WALL-SEVERITY SWEEP — find the working regime and its boundary.

THE QUESTION (pre-registered before the run, R5). W-5 fails only in
one corner of a 2x2 that is otherwise clean at machine or scheme
order:

                    flat wall            spike wall
  uniform inv.    R-0 = 0.0            certified (W-1)
  stratified      W-2a = 3.2e-08       W-5 FAIL

So neither the stratification alone nor the spike alone breaks the
transport bound; the failure needs BOTH. This sweep holds the
STRATIFIED INLET FIXED and moves only the WALL, from the flat wall
that is known clean to the real spike that fails:

    y_a(x) = y_flat + a * (y_spike(x) - y_flat),   a = 0 .. 1

and reports, per rung: cells certified, feet whose SOLVED foot left
its chord, feet no column brackets, and the transport-bound overshoot
(the W-5 quantity itself).

WHY THIS AND NOT ANOTHER FIX. Three fixes have now been tried against
W-5 (clamp t; wall-segment foot; iterate the bracket) and a fourth
(multi-column search) was measured DEAD on this world -- the recorded
back-column histogram is {1: 1375}, so its branch never executes. The
diagnostic that ended that guessing showed only 2 feet find no
bracket while 22 leave their chord, i.e. the search is not the defect.
Before a fifth attempt, establish WHERE the method works and what
turns it off.

PREDICTIONS, declared now:
  (P1) a = 0 reproduces the W-2a-class result (overshoot at round-off
       scale, no feet outside their chord);
  (P2) the out-of-chord count is zero up to some a* and then grows --
       i.e. the failure has a geometric THRESHOLD in wall turning,
       not a switch at a = 1;
  (P3) the transport overshoot tracks the out-of-chord count.
FALSIFIER: out-of-chord feet already present at a = 0 (then the flat
case is not clean and W-2a's world differs in some other way), or the
count jumping from 0 to its full value between the last two rungs
(then there is no gradual regime and the sweep teaches nothing).
"""
import os
import sys
import time

import numpy as np

HERE = "/data10/falco/RDE/RDE_Design/validation"
sys.path.insert(0, HERE)
os.chdir(HERE)

import a1_ideal_march_jax as A1                      # noqa: E402
import a1_config_compare as CC                       # noqa: E402
import a1_plug_spline_opt as PS                      # noqa: E402
import a1_rot_march as R                             # noqa: E402


def main():
    w = CC.build_world()
    taw = A1.tab_arrays(w["tab"])
    _, _, _, _, _, h0w, s0w = taw
    c = PS.build_case(w)
    xq, yq, sq = PS.wall_stations(np.asarray(c["W0"]), c, K=41)
    xq = np.asarray(xq, dtype=float)
    yq = np.asarray(yq, dtype=float)

    x0w, yl, us, vs = c["start"]
    yl = np.asarray(yl, dtype=float)
    zz = (yl - yl[0]) / (yl[-1] - yl[0])
    # the SAME stratified inlet at every rung (25 J/kg K of entropy
    # span, 3% of stagnation enthalpy) -- only the wall moves
    s_r = float(s0w) + 25.0 * np.sin(np.pi * zz)
    h_r = float(h0w) * (1.0 + 0.03 * np.sin(np.pi * zz))
    s6s = (x0w, yl, us, vs, s_r, h_r)
    s_lo, s_hi = float(np.min(s_r)), float(np.max(s_r))
    span_s = s_hi - s_lo

    y_flat = float(yq[0])
    print("== W-5 WALL-SEVERITY SWEEP ==")
    print("   inlet: FIXED stratified line, entropy span %.3f J/kg K"
          % span_s)
    print("   wall : y_a = %.4f + a (y_spike - %.4f), a = 0 -> 1"
          % (y_flat, y_flat))
    print("   spike descends %.4f -> %.4f m over %.4f -> %.4f m"
          % (yq[0], yq[-1], xq[0], xq[-1]))
    print()
    hdr = ("     a   max|dy/dx|   cells   cert    out-of-chord"
           "  no-bracket   overshoot %span")
    print(hdr)
    print("   " + "-" * (len(hdr) - 3))

    for a in (0.0, 0.25, 0.5, 0.75, 1.0):
        ya = y_flat + a * (yq - y_flat)
        # slope of the scaled wall, consistent with the geometry
        sa = np.gradient(ya, xq)
        stw = (xq, ya, sa)
        t0 = time.perf_counter()
        try:
            out, _ = R.rot_march(stw, s6s, CC.PA, w["tab"], 1.0)
        except Exception as exc:                      # pragma: no cover
            print("   %5.2f   %-10s  RAISED: %s"
                  % (a, "%.4f" % np.max(np.abs(sa)), exc))
            continue
        mesh = np.asarray(out["mesh_pts"])
        ov = float(max(np.max(mesh[:, 4]) - s_hi,
                       s_lo - np.min(mesh[:, 4]), 0.0))
        print("   %5.2f   %-10.4f  %5d  %6.3f   %8d     %7d"
              "      %8.4f    (%.0f s)"
              % (a, float(np.max(np.abs(sa))), len(mesh),
                 float(out["cert_worst"]), int(out["foot_clamped_n"]),
                 int(out.get("foot_nobracket_n", -1)),
                 100.0 * ov / span_s, time.perf_counter() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())

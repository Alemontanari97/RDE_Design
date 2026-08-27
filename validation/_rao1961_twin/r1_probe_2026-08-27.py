import os, sys, numpy as np, time
sys.path.insert(0, "/data10/falco/RDE/RDE_Design/validation")
os.environ.setdefault("RAO_GENO_RUN", "/data10/falco/RDE/codes/GENO/CASES/raoplug_run_legacy")
import rao1961_sqp_return as M
t0 = time.time()
w = M.setup()
sgn = np.array([(-1.0) ** k for k in range(len(w.W_fit))])
W_p = w.W_fit * (1.0 + M.PERT * sgn)
d0 = M.wall_dist(W_p, w)
print("R1 PROBE: start dist %.3e; minimizer with %d segments" % (d0, 14), flush=True)
W_r, J_r, g_r, n_r, wc = M.run_trsqp(W_p, w, -1.0, max_segments=14, tag="min ")
d_r = M.wall_dist(W_r, w)
print("R1 PROBE RESULT: %d records, worst cert %.3e, J %.8e, dist %.3e (start %.3e) -> %s  (%.0f s)"
      % (n_r, wc, J_r, d_r, d0, "WALKS AWAY" if d_r > d0 else "NO MOTION", time.time() - t0), flush=True)

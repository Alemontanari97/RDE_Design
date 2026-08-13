"""BIT-IDENTITY GATE for the plug march [X-PSPL/X-PAKN].

RUN THIS AFTER ANY EDIT TO `a1_plug_march.py`. It re-marches the S22
adaptive design of record at (K, N) = (61, 51) and requires the
replayed J to reproduce the committed value to `rel 0.0`.

WHY IT EARNS ITS KEEP: an edit to the march can change the flow, the
record FORMAT, or neither, and the three are indistinguishable from a
suite that only checks tolerances. This gate fails on any of them.
It is the guard the S24 handoff calls the most useful one in this
line; it lived in a session scratchpad under /tmp and is committed
here so it survives.

Recovered verbatim from that scratchpad 2026-08-13 and given its
header; the assertion and the numbers are unchanged.
"""
import os, sys, json, time
os.environ["PSPL_M"]="10"; os.environ["PSPL_K"]="61"; os.environ["PSPL_N"]="51"
sys.path.insert(0, "/data10/falco/RDE/RDE_Design/validation")
import numpy as np, jax.numpy as jnp
import a1_plug_spline_opt as P
import a1_config_compare as CC
w = CC.build_world()
art = json.load(open("/data10/falco/RDE/RDE_Design/validation/_plug_adaptive/design.json"))
xk = np.array([float(eval(v)) for v in art["design"]["xk"]])
W  = np.array([float(eval(v)) for v in art["design"]["W"]])
J_rec = float(eval(art["design"]["J"]))
t0=time.time()
c = dict(P.build_case(w), xk=xk)
out, sch = P.march_record(W, w, c)
J = float(P.J_replay(jnp.asarray(W), w, c, sch, w["ta"]))
print("GATE: J %.10e vs record %.10e  rel %.2e  mesh_pts type %s  (%.0f s)"
      % (J, J_rec, abs(J/J_rec-1), type(out["mesh_pts"]).__name__, time.time()-t0))
assert abs(J/J_rec-1) <= 1e-12
print("GATE PASS")

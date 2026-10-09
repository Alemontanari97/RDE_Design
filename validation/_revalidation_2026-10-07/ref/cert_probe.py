"""Take apart the worst-certified PLUG-WALL cell of a recorded march (T05b's analysis as a function): rebuild its inputs
from the record (schedule decisions + net), re-solve it with the model's solver, then take plain Newton steps from the
returned point. A stall = the returned point is one quadratically-convergent step from the root (second step << first);
the geometry of the cell's foot chord (dx2/dy2 = cot(chord angle)) and the conditioning of its Jacobian say why."""
import numpy as np
import jax
import jax.numpy as jnp
import a1_ideal_march_jax as A1
import a1_plug_march as PM


def wall_cell(out, S, ta, delta=1.0):
    tag = out["cert_where"]
    if tag is None or tag[0] != "wall":
        return dict(tag=tag, kind="not a wall cell")
    kst = tag[1]
    i = S.d["K_cols"][kst]
    b, jf = S.d["wfoot"][kst]
    G = {k: np.asarray(v) for k, v in zip(out["mesh_keys"], out["mesh_pts"])}
    A, B, wp = G[(jf, i - b)][:4], G[(jf + 1, i - b)][:4], G[(1, i)]
    sl = wp[3] / wp[2]
    p = jnp.asarray(np.r_[A, B, [wp[0], wp[1], sl]])
    resid = PM.make_resid_wallbot(delta)
    solver = A1.get_solver(("wb", delta), lambda: PM.make_resid_wallbot(delta))
    z, step = solver[3](jnp.asarray([0.5 * (A[1] + B[1]), A[2]]), p, ta)
    sc = max(1.0, float(jnp.max(jnp.abs(z))))
    Jf = jax.jacfwd(resid, argnums=0)
    zz, steps, norms = jnp.asarray(z), [], []
    for _ in range(3):
        r = resid(zz, p, ta)
        dz = jnp.linalg.solve(Jf(zz, p, ta), r)
        steps.append(float(jnp.max(jnp.abs(dz))))
        norms.append(float(jnp.sum(r * r)))
        zz = zz - dz
    M = float(A1.state_q(jnp.float64(np.hypot(wp[2], wp[3])), ta)[5])
    th, mu = np.degrees(np.arctan(sl)), np.degrees(np.arcsin(1.0 / M))
    chord = np.degrees(np.arctan2(B[1] - A[1], B[0] - A[0]))
    return dict(tag=tag, ratio=float(step) / (A1.NEWTON_TOL_FACTOR * A1.EPS * sc), steps=steps, norms=norms,
                stall=bool(steps[1] < 1e-2 * steps[0]), theta=th, mu=mu, chord=chord,
                dxdy=float(1.0 / np.tan(np.radians(chord))) if chord != 0 else float("inf"),
                cond=float(np.linalg.cond(np.asarray(Jf(jnp.asarray(z), p, ta)))))

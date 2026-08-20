"""R22F-L2 probe (round 1, lens L2): degrees-of-freedom of the M-RED band
B-1 uncertainty estimator.

TARGET: phaseD_r22f_centerpiece.md sec. 3.4, band B-1:
  "three-point Richardson on the St-ladder; C2 = measured second divided
   difference, its uncertainty = the ladder's third difference"

ATTACK (dof count): k ladder points support divided differences of order
<= k-1. A THREE-point ladder yields exactly one second divided difference
(= C2 for a quadratic model) and NO third difference: the declared
uncertainty estimator does not exist on the declared ladder. With >= 4
points the third difference exists and the estimator is well-defined.
Zero-magic-constants discipline requires the estimator to be defined.

Pinned env only (numpy). Exit code 0 = defect demonstrated.
"""
import numpy as np

def divided_differences(x, f):
    """Full Newton divided-difference table; row k = order-k differences."""
    table = [np.asarray(f, dtype=float)]
    x = np.asarray(x, dtype=float)
    for k in range(1, len(x)):
        prev = table[-1]
        table.append((prev[1:] - prev[:-1]) / (x[k:] - x[:-k]))
    return table

C2_true = 3.7                                   # model E(St) = C2*St^2
E = lambda st: C2_true * st**2

# Three-point ladder: order-2 difference exists (= C2), order-3 does not.
st3 = np.array([0.1, 0.2, 0.4])
t3 = divided_differences(st3, E(st3))
assert len(t3[2]) == 1 and abs(t3[2][0] - C2_true) < 1e-12
assert len(t3) == 3, "no order-3 row on 3 points"
n_third_diffs = 0 if len(t3) <= 3 else len(t3[3])
print("3-point ladder: second divided difference = %.4f (= C2, exact on "
      "the quadratic); number of third differences available: %d "
      "-> the declared uncertainty ('the ladder's third difference') "
      "DOES NOT EXIST." % (t3[2][0], n_third_diffs))

# Four-point ladder: the estimator becomes well-defined (and correctly
# reads ~0 on an exact quadratic, nonzero when the model is imperfect).
st4 = np.array([0.1, 0.2, 0.4, 0.8])
t4 = divided_differences(st4, E(st4))
assert len(t4[3]) == 1 and abs(t4[3][0]) < 1e-12
E_pert = lambda st: C2_true * st**2 + 0.5 * st**3     # model imperfection
t4p = divided_differences(st4, E_pert(st4))
print("4-point ladder: third difference = %.2e on the exact quadratic "
      "(0 as it must be) and %.4f under a cubic imperfection "
      "(the estimator now measures something)." % (t4[3][0], t4p[3][0]))

print("\nPROBE VERDICT: B-1 as printed is not executable (3 points cannot "
      "produce the declared uncertainty). REPAIR: >= 4-point St-ladder, or "
      "a different declared uncertainty estimator.")

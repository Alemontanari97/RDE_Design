# Stage-B item XB — "Exact steadification for a single rotating mode: the wave-frame objective needs no unsteady correction" — ADVOCATE position (round 0)

## Question
For inflow data that are a PURE single-mode rotating wave (fixed wave count n, exact periodicity, pinned in the data contract with the flatness monitor), is the time-mean thrust of the unsteady flow EXACTLY equal to the steady thrust functional evaluated in the frame co-rotating with the wave — so that a wave-frame evaluation of a design carries NO residence-time (Strouhal) correction at all, whatever the value of St?

## Proposed falsifier (for agreement)
A computed or measured single-mode rotating-wave flow (axisymmetric fixed walls and control surfaces, n-fold symmetric pattern rotating rigidly at Ω) whose instantaneous axial thrust F(t) on an enclosing axisymmetric control surface is NOT constant in time beyond the numerical/measurement noise floor falsifies the claim; equivalently, a nonzero m = 0 harmonic content of dF/dt at the wave frequency on such data.

## Position
1. In the frame rotating with the wave the field is steady by definition of the single-mode pinned data (every quantity is a function of x, r and θ − Ωt). The axial thrust integral over an AXISYMMETRIC control surface is an integral over θ of a function of θ − Ωt at fixed t: substituting θ' = θ − Ωt shows it is independent of t. Hence F(t) ≡ F̄ exactly and the time mean is the steady wave-frame functional — no expansion in St, no corrector, no error bar from unsteadiness (M0 [T-T0] Theorem 3, THEOREM class of record; M0 Part I "STEADIFICATION IS EXACT ... indeed the instantaneous thrust is CONSTANT").
2. The Strouhal number governs the accuracy of the frozen-time per-phase DECOMPOSITION (rung 2), not of the wave-frame evaluation (rung 3): St enters only when the 3-D helical field is replaced by a family of meridional steady fields. Evaluating BOTH arms of a decisive comparison in the wave frame therefore removes the St term from the evaluation band stack entirely; the residual St-dependence lives only in WHERE the per-phase designer put the argmax.
3. Consequence for the road: a hybrid "design per-phase, evaluate in the wave frame" is well-posed at the evaluation level; the St obligation measured on the plug sector ([X-STSC] up to 1.4) constrains the DESIGNER's rung, not the comparison's credibility, provided the wave-frame evaluator exists (B-lite: 3-D helical space-marching at marching cost on the nozzle-only domain with certified axial margin, M0 [S-BLITE]).
4. Cost: the wave-frame evaluator (B-lite) is a build item priced in the record; credibility of the decisive number RISES because the largest unmeasured band term (O(St) reduction) is removed from the evaluation.

## Anchors
M0 Part I :25-62 (structural discovery (1)); M0 [T-T0] Theorem 3 (:512 ff.); M0 Part V ladder row 1 (T0 exact); M0 [S-BLITE] :3027-3044; D1 §7 (periodicity, wave frame, modes); [X-STSC] run log (St values on the plug sector); D-MU scope note (pure-periodic single-mode scope; mode transitions routed to the robust layer, never silently averaged).

## What would make me abandon it
The falsifier above: a single-mode rotating-wave dataset (with the flatness monitor PASSING) whose axial thrust on an axisymmetric control surface is measurably non-constant in time; or a proof that the θ-substitution fails on some admissible axisymmetric control surface (e.g. one that is not invariant under rotation — which would be outside the pinned symmetry class H-A2).

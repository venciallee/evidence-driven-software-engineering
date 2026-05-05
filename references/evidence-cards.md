# Evidence Card Templates

Use these templates when the work needs more structure than the compact card in `SKILL.md`.

## Design Evidence Card

```text
Stage: Design
Evidence level: Quick / Standard / Strict
Problem:
Non-goals:
Constraints:
Decision drivers:
Options considered:
Recommended option:
Why this option:
Risks:
Verification plan:
Decision:
Residual risk:
Solidified as: ADR / RFC / design doc / issue / follow-up
```

## Implementation Evidence Card

```text
Stage: Implementation
Evidence level: Quick / Standard / Strict
Intended behavior:
Changed surfaces:
Risk hypotheses:
Verification plan:
Actual evidence:
Decision:
Residual risk:
Solidified as: tests / docs / observability / follow-up
```

## Testing Evidence Card

```text
Stage: Testing
Evidence level: Quick / Standard / Strict
Requirement or risk model:
Coverage strategy:
Unit evidence:
Integration evidence:
Contract evidence:
E2E evidence:
Manual gates:
Uncovered risks:
Decision:
```

## Browser Runtime Verification Evidence Card

Use this for web UI, dev-server, preview deployment, route, hydration, visual, loading, console, or interaction verification. It pairs well with `vercel:agent-browser-verify` / `agent-browser-verify`.

```text
Stage: Browser runtime verification
Evidence level: Quick / Standard / Strict
Claim being verified:
Target URL / route:
Environment: local dev server / preview deployment / production / other
Viewport / device if relevant:
Browser evidence plan:
- Page load:
- Non-blank content:
- Framework error overlay:
- Console errors:
- Key elements:
- Primary interactions:
- Navigation / affected routes:
- Screenshot / snapshot artifacts:
Server-side correlation plan if loading, stuck, or data-backed:
- Pending network requests:
- Runtime logs:
- API/workflow status:
Actual browser evidence:
Actual server evidence:
Decision: PASS / WARN / FAIL
Residual risk:
Follow-up verification:
```

## Debugging Evidence Card

```text
Stage: Debugging
Evidence level: Standard / Strict
Bug statement:
Reproduction steps:
Hypotheses:
Instrumentation plan:
Pre-fix evidence:
Hypothesis verdicts:
Confirmed root cause:
Fix:
Post-fix evidence:
Instrumentation cleanup:
Residual risk:
```

## Scientific Debug Report

Use this when a bug is non-obvious, reproducible, flaky, async/stateful, integration-heavy, performance-sensitive, or has already had failed fixes.

```text
Observation:
- Bug statement:
- Expected behavior:
- Actual behavior:
- Environment:
- Reproduction status:

Hypotheses:
- H1:
- H2:
- H3:
- H4:
- H5:

Experiments:
- Instrumentation / test / trace plan:
- Signal that confirms each hypothesis:
- Signal that rejects each hypothesis:

Pre-fix evidence:
- Run id:
- Logs / traces / screenshots / tests / artifacts:

Hypothesis verdicts:
- H1: CONFIRMED / REJECTED / INCONCLUSIVE, evidence:
- H2: CONFIRMED / REJECTED / INCONCLUSIVE, evidence:
- H3: CONFIRMED / REJECTED / INCONCLUSIVE, evidence:
- H4: CONFIRMED / REJECTED / INCONCLUSIVE, evidence:
- H5: CONFIRMED / REJECTED / INCONCLUSIVE, evidence:

Conclusion:
- Confirmed root cause:
- Why alternatives were rejected:
- Fix applied:

Post-fix verification:
- Run id:
- Before / after comparison:
- Regression checks:

Cleanup:
- Temporary instrumentation removed / retained as observability / pending:
- Residual risk:
```

## Profiling Evidence Card

```text
Stage: Profiling diagnosis
Evidence level: Standard / Strict
Performance symptom:
Workload:
Baseline:
Method: USE / RED / flamegraph / trace / benchmark / other
Artifacts:
Bottleneck conclusion:
Confidence:
Residual uncertainty:
Next diagnostic or optimization step:
```

## Code Review Evidence Card

```text
Stage: Code review
Evidence level: Quick / Standard / Strict
Change intent:
Reviewed scope:
Risk hypotheses:
Evidence checked:
Findings:
Severity summary:
Decision: APPROVE / COMMENT / REQUEST CHANGES
Testing gaps:
Residual risk:
```

## Performance Optimization Evidence Card

```text
Stage: Performance optimization
Evidence level: Standard / Strict
Target metric:
Workload:
Baseline:
Bottleneck evidence:
Optimization:
Before / after:
Regression checks:
Decision:
Residual risk:
Capacity implication:
```

## Delivery Verification Evidence Card

```text
Stage: Delivery verification
Evidence level: Standard / Strict
Required readiness gate:
Requirement coverage:
Root-cause closure:
Automated verification:
E2E coverage:
Browser runtime verification:
Engineering review:
QA review:
Security / privacy / performance / compatibility gates:
Decision: Review-ready / User-trial-ready / Production-ready / Not-ready
Residual risk:
Next step:
```

## Verification Standard Card

Use this before deep verification when readiness target, users, E2E selection, or acceptance standard is not already explicit.

```text
Verification Standard Card
Readiness target: Review-ready / User-trial-ready / Production-ready
Decision owner:
User roles in scope:
P0 user journey:
P1/P2 journeys:
Environments:
Required E2E suites:
Required browser runtime evidence:
Required non-browser evidence:
Manual gates:
Blocking dimensions:
Explicit non-goals:
Residual risks accepted by user:
```

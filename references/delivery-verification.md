# Delivery Verification Module

This module is the merged home of the former `agent-delivery-verifier` skill. Use it after implementation and before Review, user trial, production release, or final handoff.

The goal is not to run commands mechanically. The goal is to decide whether the work is ready based on evidence.

## Core Rule

Do not claim readiness just because code was written, a build passed, or a minimal E2E loop succeeded. Verify implementation against requirement, plan, root cause, automated evidence, E2E coverage, engineering quality, QA completion, browser/runtime evidence when relevant, and residual risk.

For user-requested software work, Production-ready is the default handoff gate unless the user explicitly lowers the bar. Review-ready and User-trial-ready are internal milestones, not sufficient completion states for normal feature, bug, performance, UX, automation, refactor, or infrastructure work.

## Requirement-Solution-Verification Alignment

Before accepting an implementation as complete, verify this order:

```text
Requirement -> Solution Mechanism -> Verification Standard
```

For non-trivial UI, product behavior, integration, permission, installation, settings, cross-process, visual, or repeated-bug work, reconstruct a Requirement-Solution-Verification Card if one was not produced:

- **Requirement**: expected user-visible or operational outcome, including acceptance criteria.
- **Ambiguities**: anything that should have been clarified because different answers imply different implementations.
- **Solution mechanism**: why the chosen technical model can actually produce the expected outcome.
- **Non-solutions**: tempting patches that cannot satisfy the requirement.
- **Verification standard**: exact automated, runtime, screenshot, log, trace, or manual evidence that would prove acceptance criteria.

Do not count evidence that does not map to this card.

## Evidence-driven Contract

If the implementation handoff includes an Evidence Card, verify every claim in it. If no Evidence Card exists, reconstruct the minimum card:

- **Goal**: intended user or engineering outcome.
- **Claim**: what the implementation says is complete or improved.
- **Hypotheses / risks**: root cause, regression risk, compatibility risk, performance risk, and user-impact risk.
- **Evidence plan**: what should prove completion.
- **Actual evidence**: commands, logs, artifacts, tests, screenshots, traces, profile data, review findings, or manual gates.
- **Decision**: Review-ready, User-trial-ready, Production-ready, or Not-ready.
- **Residual risk**: any unverified area and whether it blocks the required gate.

Do not accept evidence that does not prove the claim being made. A build proves compilability, not feature correctness. A log proves the logged event, not final delivery. A minimal E2E proves only the selected path, not production readiness.

## Verification Standard Discovery

Before verification, define the standard rather than mechanically running commands.

1. **Infer from evidence first**: read request, plan, PR/issue, docs, changed files, tests, scripts, routes, and project guidance.
2. **Identify user roles in scope**: requester/product owner, primary end user, secondary end user, reviewer/maintainer, QA/tester, admin/operator, developer integrator, support/on-call, security/privacy owner, performance owner.
3. **Select E2E suites by risk**: smoke, changed-path, critical user journey, regression, failure/recovery, auth/permission, data consistency, integration, compatibility, accessibility, performance, and deployment as applicable.
4. **Ask only material questions**: ask only when readiness target, primary user, P0 journey, environment, or acceptable limitation is unclear and cannot be inferred.
5. **Write the Verification Standard Card**: include readiness target, decision owner, user roles, journeys, environments, required E2E suites, browser evidence, non-browser evidence, manual gates, blocking dimensions, non-goals, and accepted residual risks.

## Verification Workflow

Announce phases before long-running verification and provide progress updates after each phase or long-running command. Mention progress artifacts such as `progress.md` or `progress.log` when available.

1. **Collect Evidence**: read requirements, plan, changed files, tests, configs, verification scripts, and project guidance.
2. **Confirm Verification Standard**: create or validate the Verification Standard Card. Ask one focused question only for missing material product/user/readiness decisions.
3. **Check Plan Conformance**: confirm implementation follows the plan or justify deviations.
4. **Check Root-Cause Closure**: for bugs, verify whether root cause is removed or only contained. Scientific debugging requires pre-fix evidence, hypothesis verdicts, post-fix evidence, and cleanup status.
5. **Run Engineering Review**: evaluate correctness, architecture consistency, extensibility, robustness, performance, maintainability, testability, observability, security/privacy, compatibility, and regression risk.
6. **Run QA Acceptance Review**: map P0/P1 acceptance criteria to evidence or manual gates.
7. **Evaluate E2E Coverage**: compare selected E2E suites with the Verification Standard Card and downgrade readiness if coverage is insufficient.
8. **Run Browser Runtime Verification For Web UI Work**: page open, load completion, screenshot, interactive snapshot, non-blank body, framework overlay, console errors, key elements, affected navigation, and browser/server correlation for stuck states.
9. **Run Automated Verification**: prefer project verifier, then relevant unit, integration, contract, build/static, UI/E2E, performance, or compatibility checks.
10. **Fix And Repeat**: fix inadequate implementation, tests, or coverage and rerun failed checks plus regressions until required gate passes or a real external blocker is proven.
11. **Decide Readiness**: separately decide Review-ready, User-trial-ready, Production-ready, or Not-ready.

## Engineering Review Scorecard

Mark each dimension PASS, WARN, FAIL, or N/A with evidence:

- Correctness.
- Architecture consistency.
- Extensibility.
- Robustness.
- Performance.
- Maintainability.
- Testability.
- Observability.
- Security and privacy.
- Compatibility.
- Regression risk.

Any FAIL in correctness, security/privacy, severe robustness, or high-risk compatibility blocks readiness.

## QA Acceptance Scorecard

Mark each dimension PASS, WARN, FAIL, or N/A with evidence:

- Requirement completion.
- Acceptance criteria coverage.
- Testability.
- Case completeness.
- Automation coverage.
- E2E coverage and pass rate.
- Browser runtime coverage.
- Stability.
- User experience.
- Data consistency.
- Diagnosability.
- Residual risk.

Any FAIL in P0 requirement completion, acceptance coverage, critical E2E coverage, or automated verification blocks readiness.

## E2E Suite Selection Gate

Select E2E by user role, risk, and readiness target. Do not run only the easiest path unless that path proves the readiness claim.

- **Smoke E2E**: app starts, route loads, no blank page, no blocking error, key shell renders.
- **Changed-path E2E**: exact feature or bug path works through UI, CLI, API, extension, or public interface.
- **Critical user journey E2E**: primary end user completes the P0 workflow from entry to success.
- **Regression E2E**: adjacent or historical path affected by the change still works.
- **Failure/recovery E2E**: validation error, permission denial, empty data, network failure, retry, timeout, cancellation, or recovery state.
- **Auth/permission E2E**: anonymous, logged-in, expired session, wrong role, tenant/account boundary.
- **Data consistency E2E**: create/update/delete, persistence after reload, cache refresh, cross-device or cross-process sync.
- **Integration E2E**: backend API, workflow, webhook, queue, external service, local bridge, or platform runtime path.
- **Compatibility E2E**: target browser/device/OS/version matrix for affected user base.
- **Accessibility E2E**: keyboard path, labels, focus order, contrast, and screen-reader-relevant state where UI changed.
- **Performance E2E**: startup, route transition, interaction latency, large data, memory, CPU, or bundle regression.
- **Deployment E2E**: preview/prod URL, environment variables, serverless/edge functions, static assets, routing, CDN/cache behavior.

Mapping:

- **Review-ready**: smoke E2E or browser runtime check plus changed-path test/inspection for the main diff.
- **User-trial-ready**: critical user journey E2E plus major failure/recovery checks for trial boundary.
- **Production-ready**: critical journeys, key regressions, deployment/preview evidence, observability, compatibility/performance/security gates where relevant.

## Browser Runtime Verification Gate

- **Review-ready**: affected route or main changed path loads, is not blank, has no framework overlay, has no blocking console error, and renders key changed elements.
- **User-trial-ready**: primary user interaction path works in a realistic environment and major failure/recovery states are captured where relevant.
- **Production-ready**: browser verification is paired with automated tests, E2E coverage, compatibility/performance/security checks, deployment or preview evidence, and operational diagnostics.

Browser smoke alone is not enough for Production-ready.

## Readiness Levels

- **Review-ready**: code quality, main requirement path, and baseline automated verification pass; residual risks are visible to reviewers.
- **User-trial-ready**: small group of real users can use the change with explicit boundaries and known risks, without engineering babysitting.
- **Production-ready**: target users can rely on the change long-term without engineering supervision under the agreed scope.
- **Not-ready**: core requirement is uncovered, E2E cannot prove the main path, automation fails, root cause is not closed, or high-risk manual gates remain.

If required gate is Production-ready and actual result is only Review-ready or User-trial-ready, do not hand off as complete. Continue hardening or report the specific external blocker.

## Final Report Shape

```text
阶段性进展：
- Phase ...：已完成/失败/跳过，证据 ...，问题 ...，下一步 ...

完成度结论：Review-ready / User-trial-ready / Production-ready / Not-ready

需求覆盖：
- R1 ...：PASS/WARN/FAIL，证据 ...

根因闭环：
- Root cause ...：closed / contained / unresolved，证据和风险 ...

研发视角 Review：
- Correctness: PASS/WARN/FAIL, evidence ...

QA 视角 Review：
- Requirement completion: PASS/WARN/FAIL, evidence ...

自动化验证：
- command: PASS/FAIL, log/artifact ...

E2E 覆盖判断：
- 已覆盖 ...
- 未覆盖 ...

残余风险和 manual gate：
- risk/gate ...，原因、步骤、证据、readiness 影响 ...
```

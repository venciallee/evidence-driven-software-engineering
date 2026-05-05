# Verification Standards

Use this reference when defining Review-ready, User-trial-ready, and Production-ready standards for a software task. The goal is to reduce review cost by making the agent complete the appropriate evidence loop before asking for human review.

## Why This Exists

Do not make the user review every small step. The agent should keep working until it reaches the requested readiness level or proves a real blocker.

`agent-browser-verify` exists for this reason: browser startup success is not enough, and build success is not enough. A real browser can expose blank pages, hydration errors, broken imports, missing environment variables, stuck loading states, and client/server integration failures that static checks cannot see.

Treat browser verification as one evidence source inside the readiness system, not as the whole readiness system.

## Readiness Levels

### Review-ready

Use when the output is ready for engineering review, not user trial.

Required standard:

- The implementation is coherent enough for another engineer to review.
- Main changed path is covered by code inspection and at least one verification signal.
- Build/static/type/lint checks pass when relevant.
- Tests cover the main changed logic or the test gap is explicit and justified.
- Web UI changes have browser runtime smoke evidence when a route can be opened.
- Known risks are listed with severity and reviewer attention points.
- No obvious P0 correctness, security, data-loss, or crash issue remains.

Review-ready is not enough when the user expects the feature or fix to be usable end to end.

### User-trial-ready

Use when a small group of real users can try the change without engineering babysitting.

Required standard:

- P0 user journey works in a realistic environment.
- User can complete the primary task without hidden manual setup beyond documented prerequisites.
- Major error, empty, loading, permission, and recovery states are usable enough for trial.
- Browser runtime evidence covers the primary interaction, not only page load.
- Automated tests or E2E cover the critical path and key regression risk.
- Diagnostics exist for likely failures: logs, screenshots, traces, reports, or support steps.
- Boundaries and known limitations are clear enough for trial users.

User-trial-ready is not enough for formal release, long-term unattended use, or production-facing workflows.

### Production-ready

Use by default for user-requested software delivery unless the user explicitly lowers the bar.

Required standard:

- P0 and P1 requirements have pass/fail evidence.
- Critical user journeys are covered by E2E, integration, contract, or strong manual gates.
- Failure paths, retries, permissions, empty states, compatibility, persistence, and recovery are handled.
- Security, privacy, data integrity, and authorization risks are reviewed where relevant.
- Performance is measured or bounded where relevant; no unacceptable regression is introduced.
- Observability and diagnostics are sufficient for post-release support.
- Install, update, rollback, migration, or deployment concerns are verified when the change touches them.
- Browser runtime verification is paired with automated tests, deployment/preview evidence, and operational checks for web UI work.
- Residual risks are either non-blocking or explicitly owned with follow-up and readiness impact.

Production-ready is not a claim of perfection. It means target users can rely on the change without engineering supervision under the agreed scope.

## Standard Dimensions

Evaluate readiness across these dimensions. Mark each PASS, WARN, FAIL, or N/A with evidence.

- **Requirement completion**: Intended behavior and acceptance criteria are satisfied.
- **Correctness**: Contracts, state transitions, data flow, edge cases, and error paths are correct.
- **User experience**: Loading, empty, success, error, recovery, copy, interaction, and visual state are acceptable.
- **E2E coverage**: Critical user journeys and key regressions are covered at the right level.
- **Browser runtime health**: Page loads, non-blank content, no framework overlay, no blocking console errors, changed elements render, and primary interactions work.
- **Data consistency**: Persistence, cache, backend/frontend, cross-device, cross-process, async state, and migrations remain consistent.
- **Security and privacy**: Secrets, tokens, PII, permissions, trust boundaries, authn/authz, and logs are safe.
- **Performance and scalability**: Latency, throughput, memory, CPU, I/O, startup, render, bundle size, and cost are acceptable for expected load.
- **Compatibility**: Existing APIs, configs, saved data, old clients, browsers/devices, and platform versions are not unintentionally broken.
- **Reliability**: Retries, timeouts, idempotency, partial failure, network loss, concurrency, and recovery are handled.
- **Observability and diagnosability**: Failures leave useful logs, traces, screenshots, reports, metrics, or runbooks.
- **Maintainability**: Code follows architecture boundaries, is testable, and avoids unnecessary complexity.
- **Release readiness**: Deployment, rollback, migration, feature flags, monitoring, and support handoff are covered when relevant.

## User Roles To Consider

Identify which users matter before choosing E2E tests. Do not default to only the requester.

- **Requester / product owner**: Defines desired outcome, priority, non-goals, and acceptable tradeoffs.
- **Primary end user**: Completes the main workflow; defines usability success.
- **Secondary end user**: Uses adjacent or downstream paths affected by the change.
- **Reviewer / maintainer**: Needs readable code, bounded risk, clear tests, and migration safety.
- **QA / tester**: Needs deterministic steps, stable data, expected results, and coverage matrix.
- **Admin / operator**: Manages configuration, permissions, deployment, monitoring, and rollback.
- **Developer integrator**: Consumes APIs, SDKs, hooks, events, schemas, or extension points.
- **Support / on-call**: Diagnoses failures from logs, traces, screenshots, and user reports.
- **Security / privacy owner**: Reviews auth, data exposure, secrets, PII, and compliance impact.
- **Performance owner**: Owns latency, throughput, capacity, resource cost, and regression thresholds.

If roles conflict, ask the user which role is the decision owner for the current task.

## E2E Automation Selection

Choose the smallest E2E suite that proves the readiness claim.

### Always consider

- **Smoke E2E**: App starts, route loads, no blank page, no blocking error, key shell renders.
- **Changed-path E2E**: The exact feature or bug path works through the UI or public interface.
- **Critical user journey E2E**: The user completes the P0 task from entry to success.
- **Regression E2E**: Historical or adjacent path affected by the change still works.

### Add when relevant

- **Failure/recovery E2E**: Network failure, validation error, permission denial, empty data, retry, timeout, or cancellation.
- **Auth/permission E2E**: Anonymous, logged-in, expired session, wrong role, tenant/account boundary.
- **Data consistency E2E**: Create/update/delete, persistence after reload, cache refresh, cross-device or cross-process sync.
- **Integration E2E**: Backend API, workflow, webhook, queue, external service, or local bridge path.
- **Compatibility E2E**: Browser/device/OS/version matrix for affected user base.
- **Accessibility E2E**: Keyboard path, labels, focus order, contrast, screen-reader-relevant state where user-facing UI changed.
- **Performance E2E**: Startup, route transition, interaction latency, large data, memory, CPU, or bundle regression.
- **Deployment E2E**: Preview/prod URL, environment variables, edge/serverless functions, static assets, routing, CDN/cache behavior.

### Mapping to readiness

- **Review-ready**: smoke E2E or browser runtime check plus changed-path test/inspection for the main diff.
- **User-trial-ready**: critical user journey E2E plus major failure/recovery checks for the trial boundary.
- **Production-ready**: critical user journeys, key regressions, deployment/preview evidence, observability, compatibility/performance/security gates where relevant.

## User Interaction Protocol

Ask the user only for decisions that cannot be discovered from code, docs, logs, tests, or product context. Do not ask after every failed command; keep fixing until a business or access decision is needed.

Before verification, infer what can be inferred, then ask at most one focused question if the answer changes the verification standard materially.

Good questions:

- **Readiness target**: Is this expected to be Review-ready, User-trial-ready, or Production-ready?
- **Primary user**: Which user role must succeed first?
- **P0 journey**: What is the one end-to-end path that must work for this to be useful?
- **Trial boundary**: What limitation is acceptable for trial but not production?
- **Environment**: Should verification target local dev, preview, staging, production, simulator, device, or extension runtime?
- **Risk priority**: If time is constrained, should correctness, compatibility, performance, or user experience be prioritized?

Do not ask the user to decide technical facts that can be inspected. Examples: where auth is implemented, which tests exist, what command starts the app, or whether the page has console errors.

## Verification Standard Card

Use this before running deep verification.

```text
Verification Standard Card
- Readiness target:
- Decision owner:
- User roles in scope:
- P0 user journey:
- P1/P2 journeys:
- Environments:
- Required E2E suites:
- Required browser runtime evidence:
- Required non-browser evidence:
- Manual gates:
- Blocking dimensions:
- Explicit non-goals:
- Residual risks accepted by user:
```

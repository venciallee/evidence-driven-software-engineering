# Development Planning Module

This module is the merged home of the former `agent-development-planner` skill. Use it before implementation starts for non-trivial feature work, bug fixes, refactors, platform changes, performance work, reliability work, security/privacy work, compatibility changes, or test-infrastructure work.

## Purpose

Produce a decision-complete technical and verification plan so implementation does not become a sequence of local patches.

Plan from the requirement and root cause, not from the smallest code diff. Prefer the solution that closes the underlying problem with acceptable risk. Use the smallest safe fix only when release urgency, compatibility, or blast radius makes the thorough solution inappropriate now, and record what remains unresolved.

## Evidence-driven Overlay

Produce a design or implementation Evidence Card before handoff:

- **Goal**: what the plan must prove or deliver.
- **Hypotheses / risks**: what must be true for the design to work and where it is most likely to fail.
- **Evidence plan**: tests, logs, traces, prototypes, benchmarks, review checks, rollout gates, or manual proof needed before delivery can be accepted.
- **Decision**: recommended option and why alternatives were rejected or deferred.
- **Residual risk**: what remains unverified and whether it blocks Review-ready, User-trial-ready, or Production-ready.

Do not treat a design as complete if it has no risk model or no verification plan.

## When To Use

Use this module for:

- New features, user-visible behavior changes, cross-module work, API or contract changes, state-machine changes, performance, reliability, security, privacy, or compatibility work.
- Bug fixes where the cause, impact, or recurrence risk is not obvious.
- Any work that affects P0/P1 paths, release readiness, or E2E automation.
- Any project that lacks E2E coverage for the affected user path.

Use a lightweight version for small changes, but still identify intended behavior, verification, and regression risk.

## Planning Workflow

### Phase 1: Understand Requirement

- Identify user goal, business context, affected users, affected surfaces, and expected behavior.
- Classify scenarios as P0, P1, or P2.
- Capture acceptance criteria, non-goals, constraints, compatibility requirements, rollout constraints, and known risks.
- Determine handoff gate: User-trial-ready by default, Production-ready for release/production/long-term unattended use, or Review-ready only when explicitly review-only.
- Ask the user only for ambiguous product decisions. Do not ask about facts discoverable from code, docs, configs, logs, or tests.

### Phase 2: Research Current System

- Read relevant code paths, tests, configs, schemas, docs, runbooks, and existing verification scripts.
- Identify architecture, module boundaries, data flow, state transitions, extension points, and known test seams.
- Identify current test coverage and gaps across unit, integration, contract, UI/E2E, performance, compatibility, and manual gates.
- Record verified facts separately from hypotheses.

### Phase 3: Analyze Root Cause For Bugs

- Identify trigger conditions, reproduction path, affected users, affected modules, and impact radius.
- Explain why existing validation, state handling, tests, monitoring, or architecture failed to prevent the issue.
- Distinguish symptom, proximate cause, and root cause.
- Identify whether previous local patches exist and whether they failed to address the root cause.

### Phase 4: Research Technical And Industry Options

- Research project-internal patterns first, then official platform or framework documentation when relevant.
- For product experience, developer tools, testing systems, reliability, or platform workflows, research industry practice and competitor approaches when current information matters.
- Summarize what mature systems do, what problem their approach solves, what is worth learning, and what should not be copied.
- Compare options by correctness, user impact, implementation cost, migration cost, blast radius, extensibility, robustness, performance, testability, observability, compatibility, and recurrence risk.
- Cite sources when external research is used, and note recency or uncertainty.

### Phase 5: Compare Solutions

Compare at least these solution types for bug or architecture-sensitive work:

- **Thorough solution**: remove or redesign the root cause. Explain why it prevents recurrence, what mechanisms change, blast radius, migration cost, test cost, and release risk.
- **Minimum safe fix**: narrow containment or emergency fix. Explain what it does not solve, recurrence risk, and follow-up root-cause work.
- **Phased solution**: immediate risk reduction plus later root-cause fix. Define phase boundaries, validation for each phase, and remaining risk.

Recommend the root-cause-oriented solution when risk is acceptable. Recommend a minimum safe fix only when timing, compatibility, or blast radius makes the thorough solution unsafe for current delivery.

### Phase 6: Design Technical Plan

- Define the recommended approach and why it is preferred over alternatives.
- Specify affected modules, data flow, APIs, types, state transitions, persistence, concurrency, error handling, compatibility, observability, and rollback considerations.
- Define test seams, dependency injection, seed data, mocks, fake clocks, selectors, logs, or artifacts needed to make implementation verifiable.
- Identify release or migration risks and how to reduce them.

### Phase 7: Design Systematic Test Strategy

- Map each requirement, risk, and root cause to verification.
- Decide what belongs in unit tests, integration tests, contract tests, UI/E2E tests, compatibility tests, performance tests, stability tests, security checks, and manual gates.
- Cover happy paths, failure paths, empty states, boundary conditions, permissions, concurrency, persistence, cross-device or cross-process state, recovery, and regression cases.
- Define expected evidence: command output, log, report, screenshot, video, trace, artifact, or manual proof.

### Phase 8: Design E2E Automation System

When the project or affected path lacks E2E capability, design the system before proposing a minimal runner.

- **Coverage matrix**: P0/P1/P2 paths, positive paths, failure paths, empty states, permissions, compatibility, cross-device or cross-process paths, data consistency, and recovery.
- **Test layering**: unit, integration, contract, E2E, device-only, or manual gates.
- **Environment**: local, CI, pre-release, simulator, browser, device matrix, and external-service isolation.
- **Data strategy**: seeds, fixtures, test accounts, fake clocks, mock servers, cleanup, and state isolation.
- **Observability**: logs, screenshots, videos, traces, reports, failing commands, and artifact retention.
- **Stability**: condition-based waits, deterministic inputs, no arbitrary sleeps, no shared-state pollution, no uncontrolled external dependencies.
- **Gate policy**: PR-required, merge-required, release-required, scheduled, and manual-gate checks.
- **Phased rollout**: first runnable loop, then P0 expansion, P1/P2 expansion, flake hardening, CI gating, and release gating.

## Readiness Target

- **Review-ready**: sufficient for engineering review; main path and code quality are inspectable with basic automated evidence.
- **User-trial-ready**: small group of real users can use the change with explicit boundaries, limitations, and known risks.
- **Production-ready**: target users can rely on the change long-term without engineering supervision under the agreed scope.
- **Not-ready**: core requirement is unclear, root cause is not closed, E2E coverage is insufficient, automation fails, or high-risk manual gates remain.

Default to User-trial-ready for user-requested features, bugs, optimizations, UX changes, workflow changes, or automation capabilities. Use Production-ready for production release, external users, long-running services, install/update paths, security/privacy-sensitive work, or when the user says production/release/formal delivery. Use Review-ready only for design review, code review, prototype/spike, or explicitly scoped review-only work.

## Shared Planning Output

End with a handoff that implementation and verification can use directly:

```text
Requirement / Root Cause / Recommended Solution / Alternative Solutions / Verification / Priority / Expected Evidence / Readiness Target
```

Also include requirement understanding and non-goals, current-system findings, external research when used, solution comparison, systematic test strategy, E2E automation design if needed, implementation sequence, major risks, required handoff gate, and exact evidence needed before delivery can be handed back.

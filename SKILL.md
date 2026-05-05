---
name: evidence-driven-software-engineering
version: 0.4.1
description: Use this skill when applying Evidence-driven Software Engineering to planning, implementation, testing, debugging, profiling, code review, performance optimization, or delivery verification. It turns engineering claims into explicit hypotheses, evidence plans, verification results, readiness decisions, and residual-risk reports.
---

# Evidence Driven Software Engineering

## Overview

Apply this skill to make software work evidence-based instead of confidence-based. The goal is to ensure important engineering judgments are supported by inspectable evidence: tests, logs, traces, benchmarks, profiles, code-path inspection, review findings, screenshots, reports, or explicit manual gates.

Use this skill as a workflow wrapper around existing design, implementation, debugging, review, profiling, testing, and verification skills. Do not replace specialized skills; require them to produce an Evidence Card and a clear pass/fail/readiness decision.

## Core Rule

Do not claim a plan is sound, a bug is fixed, code is complete, a review is approved, or performance is improved until the claim has matching evidence. If evidence is unavailable, label the gap explicitly and state the readiness impact.

Use this invariant:

```text
Claim = Goal + Hypothesis + Evidence Plan + Actual Evidence + Decision + Residual Risk
```

## Scientific Method Positioning

Treat the Scientific Method as the diagnostic core of this skill. It is most explicit in debugging, but the same pattern applies across design, testing, review, profiling, and performance work.

```text
Observation -> Hypothesis -> Experiment -> Evidence -> Conclusion -> Iteration
```

Map it to software work this way:

- **Observation**: bug report, failing test, slow request, review concern, production symptom, unclear design risk, or user-visible mismatch.
- **Hypothesis**: a specific possible cause, risk, or design assumption that can be confirmed or rejected.
- **Experiment**: test, instrumentation, reproduction, profile, benchmark, code-path trace, prototype, review checklist, or rollout gate.
- **Evidence**: logs, traces, test results, benchmark data, flamegraph, screenshots, CI output, code references, or manual proof.
- **Conclusion**: CONFIRMED, REJECTED, INCONCLUSIVE, PASS, WARN, FAIL, APPROVE, REQUEST CHANGES, or readiness decision.
- **Iteration**: generate new hypotheses when evidence rejects or fails to prove the current claim.

Do not use Scientific Method as a ceremonial label. Require the claim to be falsifiable and the evidence to directly prove or disprove it.

## When To Use

Use this skill for:

- Planning a feature, architecture change, refactor, migration, test system, or workflow improvement.
- Implementing non-trivial software changes where completion requires verification.
- Debugging reproducible, flaky, async, state, integration, runtime, or performance issues.
- Designing test strategy, acceptance criteria, E2E coverage, or regression protection.
- Reviewing code, plans, PRs, performance changes, readiness claims, or delivery quality.
- Profiling or optimizing performance, latency, throughput, memory, startup, rendering, I/O, or cost.
- Producing final handoff reports where the user needs to know what is proven versus still risky.
- Verifying web UI work with browser runtime evidence such as page load, console errors, visual state, interactive snapshots, route navigation, and browser/server log correlation.

Use a lightweight form for low-risk tasks, but still include evidence. Upgrade to strict form when the work touches security, privacy, auth, payments, data migration, persistence, compatibility, production incidents, performance, concurrency, release, or user-facing P0/P1 paths.

## Evidence Level

Choose the evidence level before execution.

- **Quick**: Low-risk, local, reversible change. Require a short Evidence Card and at least one verification signal or a reason verification is inspection-only.
- **Standard**: Normal feature, bug fix, review, test, or workflow change. Require goal, risks, evidence plan, actual evidence, decision, and residual risk.
- **Strict**: High-risk or production-facing work. Require alternatives, risk model, before/after evidence where applicable, acceptance mapping, readiness decision, and explicit unresolved gates.

Default to **Standard**. Use **Strict** for security/privacy, data, concurrency, compatibility, production, performance, release, and repeated-failure work.

## Universal Workflow

Follow this sequence.

1. **Classify the stage**: design, implementation, testing, debugging, profiling, code review, performance optimization, delivery verification, or mixed.
2. **Set the evidence level**: Quick, Standard, or Strict, based on risk and user expectation.
3. **State the target claim**: the plan is viable, the code implements behavior, the root cause is closed, the review can approve, or performance improved.
4. **Identify hypotheses and risks**: list what must be true and what is most likely to fail.
5. **Define the evidence plan before executing**: tests, logs, traces, profile, benchmark, static inspection, screenshots, CI, manual gate, or review checklist.
6. **Execute the work**: use the relevant specialized skill or normal coding workflow.
7. **Collect actual evidence**: include command names, artifact paths, line references, metrics, before/after values, or manual observations.
8. **Make a decision**: PASS, WARN, FAIL, APPROVE, REQUEST CHANGES, Production-ready, User-trial-ready, Review-ready, or Not-ready.
9. **State residual risk**: list what remains unverified and whether it blocks the requested handoff gate.
10. **Solidify the result**: add tests, docs, monitoring, regression cases, checklist updates, ADR, or follow-up tasks when needed.

## Evidence Card

Use this compact card in progress updates, final handoffs, and reviews.

```text
Evidence Card
- Stage:
- Evidence level:
- Goal:
- Claim:
- Hypotheses / risks:
- Evidence plan:
- Actual evidence:
- Decision:
- Residual risk:
- Solidified as:
```

For complex work, load `references/evidence-cards.md` and use the stage-specific templates.

For non-trivial development planning, load `references/development-planning.md`. This module contains the merged `agent-development-planner` workflow.

For delivery verification, readiness decisions, E2E selection, and final handoff, load `references/delivery-verification.md`. This module contains the merged `agent-delivery-verifier` workflow.

For verification standard design, load `references/verification-standards.md`. Use it to define readiness gates, user roles, E2E automation choices, and which questions must be confirmed with the user before verification begins.

For Skill Effect Report retention, load `references/effect-reporting.md` and use `scripts/record_effect_report.py`. Keep at most 50 reports per reports directory.

For version history, integration scope, and evaluation status, inspect `CHANGELOG.md`, `references/integration-manifest.md`, `references/evaluation.md`, and `references/effect-reporting.md`.

## Stage Playbooks

## Built-in Modules

EDSE owns these merged modules:

- **Development Planning**: use `references/development-planning.md` before non-trivial feature, bug, refactor, platform, test-infrastructure, performance, reliability, security, privacy, compatibility, or E2E work.
- **Delivery Verification**: use `references/delivery-verification.md` after implementation and before Review, user trial, production release, or final handoff.

The historical `agent-development-planner` and `agent-delivery-verifier` standalone skill directories are merged into this skill and should not remain under the skills root after migration. The canonical workflows live only in this directory.

### Design

Use RFC, ADR, design review, or ATAM-style tradeoff analysis.

- Define the problem, non-goals, constraints, affected users, affected systems, and success criteria.
- Compare at least two options unless only one is viable; if only one is viable, explain why alternatives are invalid.
- Identify risks by correctness, compatibility, security, reliability, performance, observability, migration, and user impact.
- Define validation before implementation: prototype, contract test, E2E, benchmark, migration rehearsal, rollout, or manual gate.
- Produce ADR/RFC evidence: decision, drivers, alternatives considered, why chosen, consequences, follow-ups.

### Implementation

Use TDD, BDD, small-step development, and red-green-refactor when practical.

- Restate intended behavior before editing.
- Prefer small, reversible changes with a verification signal after each meaningful step.
- Add or update tests for changed behavior and regression risk.
- Treat build/type/lint pass as necessary but not sufficient when behavior changed.
- Final evidence must include changed behavior proof, relevant tests, and any gaps.

### Testing

Use test pyramid, risk-based testing, property-based testing, and contract testing.

- Build a risk model before choosing tests.
- Map each P0/P1 behavior, root cause, or risk to at least one verification method.
- Include happy path, failure path, empty state, boundary, permission, concurrency, persistence, compatibility, and regression cases where relevant.
- Separate unit, integration, contract, UI/E2E, performance, security, and manual gates.
- Do not use coverage percentage as the only quality signal; explain what risk the tests prove.

### Browser Runtime Verification

Use browser verification for web UI, dev-server, route, hydration, rendering, interaction, loading, and visual-regression risk. Treat `vercel:agent-browser-verify` / `agent-browser-verify` as a runtime evidence collector, not as the full acceptance gate.

- Start from the user-facing claim: page loads, changed feature renders, key interaction works, error state is handled, navigation works, or stuck/blank page is fixed.
- Capture browser evidence: URL, viewport if relevant, screenshot, interactive snapshot, body-content check, framework overlay check, console errors, and key DOM/UI elements.
- For changed features, verify at least the affected route and the primary interaction path, not only the home route.
- For loading, spinner, blank, frozen, or hanging pages, correlate browser evidence with server logs, pending network requests, workflow/run status, or backend function logs.
- Classify the result as PASS, WARN, or FAIL. PASS means the browser evidence proves the claim being checked; WARN means basic load works but coverage is incomplete; FAIL means page load, console, overlay, content, interaction, or browser/server correlation failed.
- Record residual risk explicitly: routes not checked, auth states not available, external services mocked, viewport/device not covered, network state not tested, or production deployment not verified.

Browser verification proves runtime UI health for selected routes and interactions. It does not by itself prove full requirement completion, E2E coverage, performance, accessibility, cross-browser compatibility, production deployment health, or long-term stability.

### Debugging

Use systematic debugging and scientific-method debugging.

- **Observe**: state the bug, expected behavior, actual behavior, environment, and reproduction status.
- **Hypothesize**: generate 3-5 precise hypotheses for non-obvious, flaky, async, stateful, integration, or performance-sensitive bugs.
- **Experiment**: add focused instrumentation, tests, traces, or reproduction controls that map directly to hypotheses.
- **Collect evidence**: run a clean pre-fix reproduction and capture logs, traces, screenshots, test output, or runtime state.
- **Conclude**: classify each hypothesis as CONFIRMED, REJECTED, or INCONCLUSIVE with evidence.
- **Fix**: modify only the confirmed root cause or state that the fix is a minimum safe containment with residual risk.
- **Verify**: keep instrumentation active for post-fix verification and compare before/after evidence.
- **Clean up**: remove temporary instrumentation after success, or explain why it remains as permanent observability.

For scientific debugging, the minimum report is: bug statement, hypotheses, instrumentation or experiment plan, pre-fix evidence, hypothesis verdicts, confirmed root cause, fix, post-fix evidence, cleanup status, and residual risk.

### Profiling Diagnosis

Use profiling-driven diagnosis, USE, RED, and flamegraph analysis.

- Establish baseline before interpreting performance.
- Choose the right lens: USE for resources, RED for service behavior, flamegraph for CPU/call-stack cost, trace for latency path.
- Separate bottleneck diagnosis from optimization; first prove where time, memory, I/O, contention, or errors accumulate.
- Include profile artifacts, metrics, sampling conditions, workload, and limitations.

### Code Review

Use Fagan inspection, checklist-based review, and risk-based review.

- Understand change intent before reviewing details.
- Build risk hypotheses: what could break, who is affected, what contract could be violated.
- Inspect high-risk paths first: auth, data mutation, state transitions, async ordering, persistence, compatibility, errors, and tests.
- Report only evidence-backed findings. A strong finding includes scenario, file/line, failure mode, impact, and fix direction.
- Classify findings by severity and give approval decision: APPROVE, COMMENT, or REQUEST CHANGES.

### Performance Optimization

Use performance engineering, benchmark-driven optimization, and capacity planning.

- Define target metric before optimizing: p50, p95, p99, throughput, memory, CPU, startup, render time, cost, or capacity.
- Capture baseline under a stated workload.
- Prove the bottleneck with profile, trace, benchmark, query plan, or resource metrics.
- Make the smallest optimization that addresses the measured bottleneck.
- Compare before/after and check regressions in correctness, resource usage, maintainability, and user-visible behavior.

### Delivery Verification

Use `references/delivery-verification.md` before final handoff.

- Verify requirement completion, root-cause closure, code quality, QA coverage, automated checks, E2E coverage, readiness level, and residual risk.
- For web UI work, include browser runtime verification evidence when a dev server, preview deployment, or local route can be opened.
- Define the Review-ready, User-trial-ready, and Production-ready standard before executing verification. Infer from requirement, code, docs, and risk; ask the user only for product/user/priority decisions that cannot be discovered locally.
- Identify the user roles that matter for the change: requester, end user, reviewer, QA, operator, admin, developer integrator, security/privacy owner, or performance owner.
- Select E2E automation by risk and readiness target: smoke path for Review-ready, primary user journey for User-trial-ready, and critical path plus failure/recovery, compatibility, observability, and deployment evidence for Production-ready.
- Do not collapse Review-ready, User-trial-ready, and Production-ready into one status.
- If the required gate is not met, continue fixing or label the external blocker and remaining work.

## Final Report Shape

Use concise evidence-dense reporting.

```text
Evidence-driven summary:
- Stage:
- Evidence level:
- Goal:
- Decision:
- Evidence:
- Residual risk:
- Readiness / next step:
```

For large work, include a table:

```text
Claim / Evidence Plan / Actual Evidence / Status / Residual Risk
```

## Skill Effect Reporting

After substantial EDSE-guided tasks, create a Skill Effect Report to monitor whether the workflow actually helped. Do not create a report for trivial one-line answers unless the user asks.

Use `scripts/record_effect_report.py` to save reports. The script prunes old reports and keeps only the most recent 50 files in the selected reports directory.

Default local destination:

```text
~/.codex/skill-effect-reports/evidence-driven-software-engineering
```

Report at minimum:

- Task type and readiness target.
- Evidence Card produced: yes/no.
- Verification Standard Card produced: yes/no/not needed.
- User questions asked and why.
- Evidence collected.
- Final readiness decision.
- Missed gates and residual risks.
- Self-score for whether EDSE reduced review cost.

## Anti-Patterns

- Do not treat code written as code verified.
- Do not treat build success as user-facing completion.
- Do not treat a log message as proof unless it proves the claim being made.
- Do not optimize without a baseline.
- Do not review code before understanding intent.
- Do not claim root cause from static reading alone when runtime evidence is practical.
- Do not hide unverified assumptions; label them as assumptions or residual risks.

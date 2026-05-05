# Integration Manifest

This file records skill-level integration points for `evidence-driven-software-engineering`.

## Current Version

- Skill: `evidence-driven-software-engineering`
- Version: `0.3.1`
- Date: 2026-05-05

## Downstream Skills Updated

| Skill | Integration | Expected Behavior Change |
|---|---|---|
| `agent-development-planner` | Evidence-Driven Overlay | Non-trivial plans should include goal, hypotheses/risks, evidence plan, decision, and residual risk. |
| `agent-delivery-verifier` | Evidence-Driven Contract, Verification Standard Discovery, Browser Runtime Verification Gate, E2E Suite Selection Gate | Verification should define readiness standard before deep checks, choose E2E suites by risk, use browser runtime evidence for web UI, and continue until required readiness or real blocker. |
| `code-review` | Evidence-Driven Review Workflow | Reviews should start from intent and risk hypotheses, report evidence-backed findings, and include evidence checked, testing gaps, and residual risks. |
| `performance-oracle` | Evidence-Driven Performance Rule | Performance claims should use target metric, baseline, bottleneck evidence, before/after data, and regression checks. |
| `performance-reviewer` | Evidence-driven review rule | Performance findings need concrete hot path, scale assumption, or measurement evidence; speculative issues become residual risk/testing gap. |

## Compatibility Contract

- Keep `Evidence Card` fields stable unless making a major version change.
- Keep readiness labels stable: `Review-ready`, `User-trial-ready`, `Production-ready`, `Not-ready`.
- Keep Verification Standard Card fields stable unless making a major version change.
- Keep Skill Effect Report core fields stable unless making a major version change.
- Downstream skills may reference this skill by name and may not need to load all reference files unless verification standards or templates are needed.

## Known Limitations

- The local skills directory is not currently a git repository, so versioning is file-based rather than commit-based.
- Static validation proves structure and required guidance coverage only.
- Behavioral improvement requires task-level evaluation across real or replayed software tasks.

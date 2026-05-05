# Integration Manifest

This file records skill-level integration points for `evidence-driven-software-engineering`.

## Current Version

- Skill: `evidence-driven-software-engineering`
- Version: `0.4.1`
- Date: 2026-05-05

## Canonical Modules

| Module | Path | Source Skill |
|---|---|---|
| Development Planning | `references/development-planning.md` | `agent-development-planner` |
| Delivery Verification | `references/delivery-verification.md` | `agent-delivery-verifier` |

## Former Standalone Skills Merged

| Former Skill | New Canonical Module | Migration Status |
|---|---|---|
| `agent-development-planner` | `references/development-planning.md` | Standalone directory removed from the skills root after merge. |
| `agent-delivery-verifier` | `references/delivery-verification.md` | Standalone directory removed from the skills root after merge. |

## Downstream Skills Updated

| Skill | Integration | Expected Behavior Change |
|---|---|---|
| `code-review` | Evidence-Driven Review Workflow | Reviews should start from intent and risk hypotheses, report evidence-backed findings, and include evidence checked, testing gaps, and residual risks. |
| `performance-oracle` | Evidence-Driven Performance Rule | Performance claims should use target metric, baseline, bottleneck evidence, before/after data, and regression checks. |
| `performance-reviewer` | Evidence-driven review rule | Performance findings need concrete hot path, scale assumption, or measurement evidence; speculative issues become residual risk/testing gap. |

## Compatibility Contract

- Keep `Evidence Card` fields stable unless making a major version change.
- Keep readiness labels stable: `Review-ready`, `User-trial-ready`, `Production-ready`, `Not-ready`.
- Keep Verification Standard Card fields stable unless making a major version change.
- Keep Skill Effect Report core fields stable unless making a major version change.
- Keep merged planning and verification module names stable unless making a major version change.
- Downstream skills may reference this skill by name and may not need to load all reference files unless verification standards or templates are needed.

## Known Limitations

- The local skills directory is not currently a git repository, so versioning is file-based rather than commit-based.
- Static validation proves structure and required guidance coverage only.
- Behavioral improvement requires task-level evaluation across real or replayed software tasks.

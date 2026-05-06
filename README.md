# Evidence-driven Software Engineering

Evidence-driven Software Engineering (EDSE) is a workflow skill for making software agents work with evidence instead of confidence. It helps agents plan, implement, debug, review, optimize, and verify software changes without repeatedly asking the user for things the agent should be able to inspect or prove.

The core idea is simple:

```text
Claim = Goal + Hypothesis + Evidence Plan + Actual Evidence + Decision + Residual Risk
```

## Problem

Many coding agents stop too early:

- They write code and claim completion after a build passes.
- They fix bugs from static guesses without runtime evidence.
- They ask the user after every small failure instead of continuing the verification loop.
- They say something is ready without separating Review-ready, User-trial-ready, and Production-ready.
- They leave reviewers to ask: What was verified? What was not verified? What user path actually works?

EDSE exists to reduce that review cost. It gives the agent a reusable evidence loop and a readiness model so it can keep working until the target standard is met or a real blocker is proven.

## Core Workflow

Use EDSE as a wrapper around more specific skills and tools.

```text
Classify stage
-> Set evidence level
-> State the claim
-> Identify hypotheses and risks
-> Define evidence plan
-> Execute work
-> Collect evidence
-> Decide readiness
-> State residual risk
-> Solidify result
```

The universal Evidence Card is:

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

## What It Covers

- Design and architecture review.
- Development planning before implementation.
- Implementation and refactoring.
- Testing strategy and coverage planning.
- Scientific-method debugging.
- Browser runtime verification.
- Code review.
- Profiling and performance optimization.
- Delivery verification and readiness decisions.

Detailed templates live in [`references/evidence-cards.md`](references/evidence-cards.md).

The merged planning and verification modules live in [`references/development-planning.md`](references/development-planning.md) and [`references/delivery-verification.md`](references/delivery-verification.md). The older `agent-development-planner` and `agent-delivery-verifier` standalone skill directories have been removed after migration; EDSE is the canonical home.

## Verification Skill Design

The verification side of EDSE is the merged home of the former `agent-delivery-verifier` skill. Its purpose is not to run more commands; its purpose is to turn a delivery claim into an evidence-backed readiness decision.

Design goals:

- Convert "is it done?" into a falsifiable claim with a target gate: Review-ready, User-trial-ready, Production-ready, or Not-ready.
- Align `Requirement -> Solution Mechanism -> Verification Standard` before accepting an implementation as complete.
- Select the smallest evidence set that proves the claim, including code inspection, automated tests, E2E checks, browser runtime evidence, logs, traces, screenshots, or manual gates when relevant.
- Keep the agent working through failed checks until the required gate passes or a real external blocker is proven.
- Produce a handoff that states what passed, what failed, what remains risky, and what must happen next.

Problems it solves:

- Build, typecheck, or lint success being treated as proof that user-facing behavior works.
- Browser startup or route load being mistaken for full product acceptance.
- Agents asking the user after every failed command instead of continuing the evidence loop.
- Reviews lacking a clear map from requirements to implementation mechanism to verification evidence.
- Overclaiming Production-ready status when the actual evidence only supports Review-ready or User-trial-ready.
- Residual risks being hidden in vague summaries instead of stated as explicit readiness blockers or accepted limitations.

The verification module works best when paired with [`references/verification-standards.md`](references/verification-standards.md) before deep verification and [`references/evidence-cards.md`](references/evidence-cards.md) for the final Delivery Verification Evidence Card.

## Scientific Method

EDSE treats the Scientific Method as the diagnostic core of software work:

```text
Observation -> Hypothesis -> Experiment -> Evidence -> Conclusion -> Iteration
```

In debugging, this means the agent should reproduce the issue, generate hypotheses, add instrumentation or tests, classify each hypothesis as confirmed/rejected/inconclusive, fix the confirmed root cause, verify before/after evidence, and clean up temporary instrumentation.

Use the Scientific Debug Report template in [`references/evidence-cards.md`](references/evidence-cards.md) for non-obvious or repeated bugs.

## Readiness Levels

EDSE distinguishes three delivery standards.

| Level | Meaning | Typical evidence |
|---|---|---|
| Review-ready | Ready for engineering review, not necessarily user use. | Coherent diff, main-path verification, visible residual risks. |
| User-trial-ready | Small group of real users can try it without engineering babysitting. | P0 journey works, major failure states are usable, diagnostics exist. |
| Production-ready | Target users can rely on it under the agreed scope. | P0/P1 evidence, E2E/contract/integration tests, deployment/rollback/observability/security/performance checks where relevant. |

Use [`references/verification-standards.md`](references/verification-standards.md) to define user roles, P0/P1 paths, E2E suite selection, browser verification, and which questions require user confirmation.

## Browser Runtime Verification

For web UI work, EDSE treats browser checks as runtime evidence, not as a complete acceptance gate.

Browser verification should capture:

- Target URL and route.
- Screenshot or visual state.
- Interactive snapshot where available.
- Non-blank content check.
- Framework error overlay check.
- Console errors.
- Key elements and changed interactions.
- Browser/server correlation for stuck, blank, or loading states.

Browser verification proves selected runtime UI paths. It does not by itself prove full E2E coverage, accessibility, performance, cross-browser compatibility, deployment health, or production readiness.

## Installation

For local Codex-style skill directories, copy this folder into the skills root:

```bash
cp -R evidence-driven-software-engineering ~/.codex/skills/
```

Then package or validate it with the bundled skill tooling if available:

```bash
python scripts/evaluate_static.py . --skills-root ~/.codex/skills
```

For a clean distributable archive, exclude local VCS metadata:

```bash
zip -r evidence-driven-software-engineering.zip evidence-driven-software-engineering -x '*/.git/*'
```

This skill is designed to be portable. The report directory can be configured, and no user-specific path is required for open-source use.

## Usage

Use EDSE when a task needs more than an explanation or a trivial edit.

Example prompts:

```text
Use evidence-driven-software-engineering to plan this feature.
Use EDSE to verify whether this is Production-ready.
Use EDSE and scientific debugging to diagnose this flaky bug.
Use EDSE to review this PR and report evidence-backed risks.
Use EDSE to optimize this slow path with baseline and before/after data.
```

Expected output should include the claim being made, the evidence used to support it, the readiness decision, and residual risk.

## Skill Effect Reports

EDSE includes an optional monitoring mechanism for real-world skill effectiveness.

Use [`scripts/record_effect_report.py`](scripts/record_effect_report.py) to save reports:

```bash
printf '%s\n' 'Skill Effect Report
- Task id / title: example
- EDSE self-score: 8' \
  | python scripts/record_effect_report.py --reports-dir ./reports --title example
```

The script keeps only the newest 50 reports per reports directory. This makes it suitable for personal workflow monitoring and for future open-source evaluation artifacts without unbounded local growth.

See [`references/effect-reporting.md`](references/effect-reporting.md) for the report template and scoring rubric.

## Evaluation

Static evaluation is available:

```bash
python scripts/evaluate_static.py . --skills-root ~/.codex/skills
```

Static evaluation checks that required sections, templates, references, and downstream integration anchors exist. It does not prove behavioral effectiveness.

Behavioral evaluation requires replayable tasks and baseline comparison. Suggested metrics:

- Unnecessary user questions per task.
- Missing evidence claims per final answer.
- Correct readiness classification rate.
- E2E suite selection appropriateness.
- Browser runtime defects caught.
- Review rework count.
- Residual risks explicitly reported.
- User-accepted completion rate.

See [`references/evaluation.md`](references/evaluation.md) for the current evaluation plan.

## Versioning

This skill uses semantic versioning:

- PATCH: wording fixes, examples, non-behavioral template cleanup.
- MINOR: new evidence cards, readiness gates, stage playbooks, scripts, or integration guidance.
- MAJOR: changed default readiness semantics, removed or renamed required workflow fields, or incompatible report format changes.

See [`CHANGELOG.md`](CHANGELOG.md) for version history.

## Privacy

Do not store secrets, tokens, private customer data, raw credentials, or unnecessary PII in Evidence Cards or Skill Effect Reports. Store artifact paths and summaries instead of sensitive raw payloads.

## Current Status

Current version: `0.4.1`.

Static coverage is evaluated. Behavioral effectiveness still needs replay or live-task evaluation before making strong claims that EDSE reduces review cost across teams.
# evidence-driven-software-engineering

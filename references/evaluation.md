# Evaluation

## Current Evaluation Status

Current status: **static coverage evaluated, behavioral effectiveness not yet proven**.

The current checks prove that the skill is structurally valid and contains the expected workflow anchors. They do not prove that an agent using the skill will consistently behave better in real tasks.

## What Has Been Evaluated

- Skill packaging and frontmatter validity.
- Required reference files exist.
- Core Evidence-driven workflow exists.
- Scientific Method is included.
- Browser runtime verification is included.
- Verification Standard Card exists.
- Review-ready, User-trial-ready, and Production-ready standards exist.
- E2E suite selection guidance exists.
- User interaction protocol exists.
- Downstream integration anchors exist in planner, verifier, review, and performance skills.
- Skill Effect Report retention support exists and is statically checked.

## What Has Not Been Evaluated Yet

- Whether agents ask fewer unnecessary follow-up questions.
- Whether agents reach Production-ready more consistently.
- Whether Review rework decreases.
- Whether final reports become more evidence-dense.
- Whether agents choose better E2E suites for real tasks.
- Whether browser runtime verification catches real UI defects missed by builds/tests.

## Behavioral Evaluation Plan

Use replayable tasks and compare baseline agent behavior against EDSE-enabled behavior.

### Evaluation Set

- **Design task**: ambiguous feature request requiring user roles, readiness target, and verification standard.
- **Bug task**: reproducible async/state bug requiring Scientific Debug Report.
- **Web UI task**: route or component change requiring browser runtime verification.
- **Code review task**: PR diff requiring intent-first, risk-based findings.
- **Performance task**: suspected slowdown requiring baseline, bottleneck evidence, and before/after comparison.
- **Delivery task**: completed implementation requiring Review/User-trial/Production readiness decision.

### Metrics

- Unnecessary user questions per task.
- Missing evidence claims per final answer.
- Correct readiness classification rate.
- E2E suite selection appropriateness.
- Browser runtime defects caught.
- Review rework count.
- Residual risks explicitly reported.
- User-accepted completion rate.
- Skill Effect Report score trend over the latest 50 reports.

### Pass Criteria

- Each task includes an Evidence Card or equivalent evidence summary.
- Verification standard is defined before deep verification for non-trivial work.
- Production-ready is not claimed without matching evidence.
- Browser runtime verification is used for web UI work when accessible.
- Performance improvement is not claimed without baseline and before/after evidence.
- Review findings are evidence-backed and include residual risk/testing gaps.
- Skill Effect Reports are recorded for substantial EDSE runs and no more than 50 are retained per configured reports directory.

## Static Baseline Result

Initial static evaluation on 2026-05-03: PASS.

This PASS means required files, sections, and integration anchors are present. It does not mean behavioral effectiveness is proven.

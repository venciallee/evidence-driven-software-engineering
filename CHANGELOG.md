# Changelog

Use semantic versioning for this skill.

- **PATCH**: wording fixes, examples, non-behavioral template cleanup.
- **MINOR**: new evidence cards, new readiness gates, new stage playbooks, new integration guidance.
- **MAJOR**: changed default readiness semantics, removed or renamed required workflow fields, incompatible report format changes.

## 0.4.1 - 2026-05-05

### Changed

- Completed the directory-level merge by treating `agent-development-planner` and `agent-delivery-verifier` as removed standalone skills.
- Static evaluator now checks that the two former standalone skill directories are absent from the skills root after migration.
- README now documents clean distributable packaging that excludes local VCS metadata.

## 0.4.0 - 2026-05-05

### Added

- Merged `agent-development-planner` into `references/development-planning.md`.
- Merged `agent-delivery-verifier` into `references/delivery-verification.md`.
- EDSE now declares these as built-in modules and canonical workflow owners.

### Changed

- README now documents EDSE as the canonical home for planning and delivery verification.
- Static evaluator now checks merged planning and delivery verification module coverage.

## 0.3.1 - 2026-05-05

### Added

- Open-source oriented `README.md` with purpose, workflow, readiness levels, installation, evaluation, versioning, and privacy guidance.

### Changed

- Static evaluator now checks README coverage.

## 0.3.0 - 2026-05-03

### Added

- Skill Effect Report lifecycle and retention policy.
- `references/effect-reporting.md` with report template, scoring rubric, and monitoring workflow.
- `scripts/record_effect_report.py` for saving reports and pruning to the newest 50 files.

### Changed

- Static evaluator now checks Skill Effect Report coverage.
- Packaged skill now includes report recording support for open-source reuse.

## 0.2.0 - 2026-05-03

### Added

- Scientific Method positioning as the diagnostic core of the skill.
- Scientific Debug Report template.
- Browser Runtime Verification playbook and Evidence Card.
- Verification Standards reference defining Review-ready, User-trial-ready, Production-ready, standard dimensions, user roles, E2E suite selection, and user interaction protocol.
- Verification Standard Card.
- Static evaluation script and baseline evaluation report.
- Integration manifest for downstream skill updates.

### Integrated

- `agent-development-planner`: requires Evidence Card for non-trivial plans.
- `agent-delivery-verifier`: requires Verification Standard Discovery, browser runtime verification, E2E suite selection, and evidence-driven readiness decisions.
- `code-review`: requires intent-first, risk-hypothesis, evidence-backed review findings.
- `performance-oracle`: requires target metric, baseline, bottleneck evidence, and before/after proof for optimizations.
- `performance-reviewer`: suppresses low-evidence performance findings and records evidence checked.

### Evaluation Status

- Static coverage evaluation passes.
- Behavioral evaluation is not yet proven. A real multi-task A/B trial is still required to measure whether agents ask fewer unnecessary questions, produce better verification evidence, and reduce review rework.

## 0.1.0 - 2026-05-03

### Added

- Initial Evidence-driven Software Engineering workflow.
- Universal Evidence Card.
- Stage playbooks for design, implementation, testing, debugging, profiling, code review, performance optimization, and delivery verification.
- Evidence Card templates.

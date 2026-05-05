# Skill Effect Reporting

Use Skill Effect Reports to monitor whether Evidence-driven Software Engineering actually improves workflow quality. Reports are local operational telemetry for the skill, not user-facing completion reports.

## Retention Policy

Keep at most **50** Skill Effect Reports per reports directory. When the 51st report is saved, delete the oldest report by filename timestamp.

Default local directory:

```text
~/.codex/skill-effect-reports/evidence-driven-software-engineering
```

Allow callers to override the directory with `--reports-dir` so open-source users can store reports in a repo, CI artifact directory, or private local path.

## When To Record

Record a report after substantial EDSE-guided tasks, especially:

- Non-trivial implementation or bug fix.
- Debugging with hypotheses or instrumentation.
- Verification against Review-ready, User-trial-ready, or Production-ready.
- Web UI browser runtime verification.
- Code review that uses risk hypotheses.
- Performance diagnosis or optimization.
- Any task where the user had to ask whether evidence, readiness, or residual risk was complete.

Skip by default for trivial questions, pure explanations, and one-line edits unless the user asks to monitor them.

## Report Template

```text
Skill Effect Report
- Timestamp:
- Task id / title:
- Task type: design / implementation / testing / debugging / browser verification / code review / performance / delivery verification / mixed
- Readiness target: Review-ready / User-trial-ready / Production-ready / Not applicable
- User roles considered:
- P0 user journey:
- Evidence Card produced: yes / no / not needed
- Verification Standard Card produced: yes / no / not needed
- Browser runtime evidence used: yes / no / not applicable
- E2E suites selected:
- User questions asked: count + reasons
- Questions that should have been inferred locally:
- Evidence collected:
- Final decision:
- Missed gates:
- Residual risks:
- User correction needed: yes / no; details
- Review rework observed: yes / no / unknown; details
- EDSE self-score: 0-10
- What to improve in the skill:
```

## Scoring Rubric

Score each report from 0 to 10.

- **0-3**: EDSE mostly failed. Missing evidence, wrong readiness, repeated unnecessary questions, or user had to redirect the workflow.
- **4-6**: Partially useful. Some evidence collected, but readiness or residual risk was incomplete.
- **7-8**: Useful. Evidence and readiness were mostly clear; minor gaps remained.
- **9-10**: Strong. Agent inferred what it could, asked only material questions, collected direct evidence, fixed/retried autonomously, and reduced review burden.

## Optimization Loop

Review the latest 10-20 reports periodically.

- If scores trend below 7, inspect common missed gates and update the relevant playbook.
- If unnecessary questions recur, strengthen the “infer locally before asking” rule.
- If reports lack evidence, strengthen Evidence Card requirements or downstream verifier gates.
- If browser issues escape, expand Browser Runtime Verification or E2E suite selection.
- If Production-ready is overclaimed, harden readiness language in `references/delivery-verification.md`.
- If reports are too verbose, simplify the template but keep the core fields stable.

## Privacy

Do not store secrets, tokens, private customer data, raw credentials, or unnecessary PII in reports. Store artifact paths and summaries instead of sensitive raw payloads.

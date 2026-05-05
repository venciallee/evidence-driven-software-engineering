#!/usr/bin/env python3
"""Static evaluator for evidence-driven-software-engineering skill coverage.

This script checks structural and textual coverage only. It does not prove
behavioral agent quality.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path


REQUIRED_SKILL_PATTERNS = {
    "version": "version: 0.3.1",
    "core_rule": "## Core Rule",
    "scientific_method": "## Scientific Method Positioning",
    "universal_workflow": "## Universal Workflow",
    "browser_runtime_verification": "### Browser Runtime Verification",
    "delivery_verification": "### Delivery Verification",
    "skill_effect_reporting": "## Skill Effect Reporting",
    "anti_patterns": "## Anti-Patterns",
}

REQUIRED_REFERENCE_FILES = [
    "README.md",
    "CHANGELOG.md",
    "references/evidence-cards.md",
    "references/verification-standards.md",
    "references/integration-manifest.md",
    "references/evaluation.md",
    "references/effect-reporting.md",
    "scripts/record_effect_report.py",
]

REQUIRED_VERIFICATION_PATTERNS = {
    "readiness_levels": "## Readiness Levels",
    "review_ready": "### Review-ready",
    "user_trial_ready": "### User-trial-ready",
    "production_ready": "### Production-ready",
    "standard_dimensions": "## Standard Dimensions",
    "user_roles": "## User Roles To Consider",
    "e2e_automation": "## E2E Automation Selection",
    "user_interaction": "## User Interaction Protocol",
    "standard_card": "Verification Standard Card",
}

REQUIRED_README_PATTERNS = {
    "title": "# Evidence-driven Software Engineering",
    "problem": "## Problem",
    "core_workflow": "## Core Workflow",
    "readiness_levels": "## Readiness Levels",
    "installation": "## Installation",
    "evaluation": "## Evaluation",
    "effect_reports": "## Skill Effect Reports",
    "versioning": "## Versioning",
}

REQUIRED_EFFECT_PATTERNS = {
    "retention_policy": "Keep at most **50** Skill Effect Reports",
    "default_directory": "~/.codex/skill-effect-reports/evidence-driven-software-engineering",
    "report_template": "Skill Effect Report",
    "scoring_rubric": "## Scoring Rubric",
    "optimization_loop": "## Optimization Loop",
    "privacy": "## Privacy",
}

OPTIONAL_DOWNSTREAM_SKILLS = {
    "agent-development-planner": ["Evidence-Driven Overlay", "Evidence Card"],
    "agent-delivery-verifier": ["Verification Standard Discovery", "E2E Suite Selection Gate", "Browser Runtime Verification Gate"],
    "code-review": ["Evidence-Driven Review Workflow", "risk hypotheses"],
    "performance-oracle": ["Evidence-Driven Performance Rule", "before/after"],
    "performance-reviewer": ["Evidence-driven review rule", "evidence_checked"],
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_patterns(content: str, patterns: dict[str, str]) -> dict[str, bool]:
    return {name: pattern in content for name, pattern in patterns.items()}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("skill_dir", nargs="?", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--skills-root", default=None)
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    skills_root = Path(args.skills_root).resolve() if args.skills_root else skill_dir.parent

    results: dict[str, object] = {
        "skill_dir": str(skill_dir),
        "checks": {},
        "downstream_checks": {},
        "limitations": [
            "Static coverage only",
            "Does not prove behavioral agent quality",
            "Requires replay or live task evaluation for effectiveness claims",
        ],
    }

    skill_md = skill_dir / "SKILL.md"
    skill_content = read(skill_md) if skill_md.exists() else ""
    results["checks"]["skill_patterns"] = check_patterns(skill_content, REQUIRED_SKILL_PATTERNS)

    readme_path = skill_dir / "README.md"
    readme_content = read(readme_path) if readme_path.exists() else ""
    results["checks"]["readme_patterns"] = check_patterns(readme_content, REQUIRED_README_PATTERNS)

    results["checks"]["reference_files"] = {
        rel: (skill_dir / rel).exists() for rel in REQUIRED_REFERENCE_FILES
    }

    verification_path = skill_dir / "references" / "verification-standards.md"
    verification_content = read(verification_path) if verification_path.exists() else ""
    results["checks"]["verification_patterns"] = check_patterns(
        verification_content, REQUIRED_VERIFICATION_PATTERNS
    )

    effect_path = skill_dir / "references" / "effect-reporting.md"
    effect_content = read(effect_path) if effect_path.exists() else ""
    results["checks"]["effect_patterns"] = check_patterns(effect_content, REQUIRED_EFFECT_PATTERNS)

    for skill_name, patterns in OPTIONAL_DOWNSTREAM_SKILLS.items():
        path = skills_root / skill_name / "SKILL.md"
        content = read(path) if path.exists() else ""
        results["downstream_checks"][skill_name] = {
            pattern: pattern in content for pattern in patterns
        }

    all_check_groups = [
        results["checks"]["skill_patterns"],
        results["checks"]["readme_patterns"],
        results["checks"]["reference_files"],
        results["checks"]["verification_patterns"],
        results["checks"]["effect_patterns"],
    ]
    downstream_groups = list(results["downstream_checks"].values())
    passed = all(all(group.values()) for group in all_check_groups + downstream_groups)
    results["status"] = "PASS" if passed else "FAIL"

    print(json.dumps(results, indent=2, ensure_ascii=False))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())

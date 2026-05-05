#!/usr/bin/env python3
"""Record a Skill Effect Report and keep only the newest reports.

Input report content is read from stdin. The script writes a timestamped Markdown
file and prunes the reports directory to the newest N files, default 50.
"""

from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path


DEFAULT_LIMIT = 50
DEFAULT_REPORTS_DIR = Path.home() / ".codex" / "skill-effect-reports" / "evidence-driven-software-engineering"


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9._-]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-._")
    return value[:80] or "skill-effect-report"


def list_reports(reports_dir: Path) -> list[Path]:
    return sorted(
        [path for path in reports_dir.glob("*.md") if path.is_file()],
        key=lambda path: path.name,
    )


def prune_reports(reports_dir: Path, keep: int) -> list[Path]:
    reports = list_reports(reports_dir)
    excess = max(0, len(reports) - keep)
    removed: list[Path] = []
    for path in reports[:excess]:
        path.unlink()
        removed.append(path)
    return removed


def main() -> int:
    parser = argparse.ArgumentParser(description="Record an EDSE Skill Effect Report")
    parser.add_argument("--reports-dir", default=str(DEFAULT_REPORTS_DIR), help="Directory where reports are stored")
    parser.add_argument("--keep", type=int, default=DEFAULT_LIMIT, help="Maximum reports to keep, default 50")
    parser.add_argument("--title", default="skill-effect-report", help="Short report title used in filename")
    parser.add_argument("--dry-run", action="store_true", help="Print intended path and prune count without writing")
    args = parser.parse_args()

    if args.keep < 1:
        print("--keep must be at least 1", file=sys.stderr)
        return 2

    content = sys.stdin.read().strip()
    if not content:
        print("Report content is required on stdin", file=sys.stderr)
        return 2

    reports_dir = Path(args.reports_dir).expanduser().resolve()
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    report_path = reports_dir / f"{timestamp}-{slugify(args.title)}.md"

    existing_count = len(list_reports(reports_dir)) if reports_dir.exists() else 0
    would_remove = max(0, existing_count + 1 - args.keep)

    if args.dry_run:
        print(f"would_write={report_path}")
        print(f"would_prune={would_remove}")
        return 0

    reports_dir.mkdir(parents=True, exist_ok=True)
    report_path.write_text(content + "\n", encoding="utf-8")
    removed = prune_reports(reports_dir, args.keep)

    print(f"wrote={report_path}")
    print(f"kept={len(list_reports(reports_dir))}")
    print(f"pruned={len(removed)}")
    for path in removed:
        print(f"removed={path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

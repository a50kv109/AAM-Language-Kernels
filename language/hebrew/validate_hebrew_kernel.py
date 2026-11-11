#!/usr/bin/env python3
"""Read-only structural validator for the proposed Hebrew kernel."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as exc:
    raise SystemExit(f"PyYAML is required to validate UTILITY.yaml: {exc}") from exc


ROOT = Path(__file__).resolve().parent
ALLOWED_STATUSES = {
    "VERIFIED",
    "SOURCE_SUPPORTED",
    "INFERRED",
    "PROPOSED",
    "NOT_VERIFIED",
    "RESEARCH_ONLY",
}
REQUIRED_FILES = (
    "INDEX.md",
    "STRUCTURE.md",
    "UTILITY.yaml",
    "passport.md",
    "ground_truth_matrix.md",
    "pattern_registry.csv",
    "core/__init__.py",
    "core/hebrew_core.py",
    "core/hebrew_nlp_adapter.py",
    "examples/basic_usage.py",
    "tests/test_hebrew_core.py",
    "tests/test_hebrew_nlp_adapter.py",
    "extensions/aam_extensions.json",
    "validation/source_comparison.md",
    "validation/known_gaps.md",
    "validation/validation_report.md",
)
REQUIRED_DIRS = (
    "phonetics",
    "grammar",
    "morphology",
    "semantics",
    "context",
    "historical",
    "engineering",
    "sacred",
    "core",
    "examples",
    "tests",
    "extensions",
    "validation",
)


def main() -> int:
    errors: list[str] = []
    checked = 0

    for relative in REQUIRED_FILES:
        checked += 1
        if not (ROOT / relative).is_file():
            errors.append(f"missing required file: {relative}")
    for relative in REQUIRED_DIRS:
        checked += 1
        if not (ROOT / relative).is_dir():
            errors.append(f"missing required directory: {relative}")

    utility = ROOT / "UTILITY.yaml"
    if utility.is_file():
        checked += 1
        try:
            data = yaml.safe_load(utility.read_text(encoding="utf-8"))
            if not isinstance(data, dict):
                errors.append("UTILITY.yaml must contain a mapping")
            elif data.get("status") not in {"PROPOSED"}:
                errors.append("UTILITY.yaml kernel status must remain PROPOSED")
            elif set(data.get("epistemic_statuses", [])) != ALLOWED_STATUSES:
                errors.append("UTILITY.yaml epistemic_statuses do not match the allowed set")
        except yaml.YAMLError as exc:
            errors.append(f"YAML parse error in UTILITY.yaml: {exc}")

    json_files = sorted(ROOT.rglob("*.json"))
    for path in json_files:
        checked += 1
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")

    registry = ROOT / "pattern_registry.csv"
    if registry.is_file():
        checked += 1
        try:
            with registry.open(encoding="utf-8", newline="") as stream:
                reader = csv.DictReader(stream)
                required = {
                    "pattern_id",
                    "language",
                    "source_id",
                    "original_text",
                    "epistemic_status",
                    "validation_status",
                    "version_id",
                }
                fields = set(reader.fieldnames or [])
                if not required.issubset(fields):
                    errors.append(f"pattern_registry.csv missing columns: {sorted(required - fields)}")
                rows = list(reader)
                ids = [row.get("pattern_id", "").strip() for row in rows]
                nonempty_ids = [item for item in ids if item]
                duplicates = sorted({item for item in nonempty_ids if nonempty_ids.count(item) > 1})
                if duplicates:
                    errors.append(f"duplicate pattern IDs: {duplicates}")
                for row in rows:
                    status = row.get("epistemic_status", "").strip()
                    if status not in ALLOWED_STATUSES:
                        errors.append(f"invalid epistemic status for {row.get('pattern_id')}: {status!r}")
        except (OSError, UnicodeDecodeError, csv.Error) as exc:
            errors.append(f"CSV validation error: {exc}")

    for path in sorted(ROOT.rglob("*.md")):
        checked += 1
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"cannot read {path.relative_to(ROOT)}: {exc}")
            continue
        for reference in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
            target_ref = reference.strip().strip("<>")
            if target_ref.startswith(("https://", "http://", "mailto:", "#")):
                continue
            target = (path.parent / target_ref.split("#", 1)[0]).resolve()
            if not target.exists():
                errors.append(f"broken link in {path.relative_to(ROOT)}: {reference}")

    test_modules = list((ROOT / "tests").glob("test_*.py")) if (ROOT / "tests").is_dir() else []
    if not test_modules:
        errors.append("no test modules found under tests/")

    print(f"Files/directories/checks inspected: {checked}")
    print(f"JSON files validated: {len(json_files)}")
    print(f"Markdown links inspected: {sum(1 for _ in ROOT.rglob('*.md'))}")
    print(f"Test modules found: {len(test_modules)}")
    print("Pattern records: 0 (schema present; no source-backed records supplied)")
    if errors:
        print("VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    print("VALIDATION PASSED (structural checks only; not linguistic validation)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

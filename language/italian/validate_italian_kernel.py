#!/usr/bin/env python3
"""Validate the Italian kernel registry and status metadata.

This script checks the Italian language registry for required metadata fields,
validates identifier and status values, and reports warnings for partially
available or unverified source quotations without failing the entire document.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "pattern_registry.md"

REQUIRED_FIELDS = [
    "pattern_id",
    "language",
    "domain",
    "source_record",
    "source_text_status",
    "quotation_status",
    "literal_translation",
    "semantic_explanation",
    "procedural_steps",
    "evidence_level",
    "validation_status",
    "version_id",
]

VALID_EVIDENCE_LEVELS = {
    "VERIFIED_PRIMARY_SOURCE",
    "VERIFIED_WITH_COMMENTARY",
    "HISTORICAL_RECONSTRUCTION",
    "MODERN_INTERPRETATION",
    "HYPOTHESIS",
    "REJECTED",
}

VALID_VALIDATION_STATUSES = {
    "INITIAL",
    "IN_REVIEW",
    "CANONICAL_REGISTERED",
    "RESEARCH_ONLY",
}

VALID_SOURCE_TEXT_STATUS = {
    "original_source_text_available",
    "original_source_text_unavailable",
    "quotation_partially_available",
    "quotation_awaiting_verification",
}

VALID_QUOTATION_STATUS = {
    "exact_quotation_available",
    "quotation_partially_available",
    "quotation_awaiting_verification",
}


def extract_pattern_blocks(text: str):
    blocks = []
    current = None
    for line in text.splitlines():
        if line.startswith("### "):
            if current is not None:
                blocks.append(current)
            current = {"header": line[4:].strip(), "lines": []}
        elif current is not None:
            current["lines"].append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def parse_pattern(block):
    kv = {}
    current_key = None
    for line in block["lines"]:
        if line.startswith("- ") and ":" in line[2:]:
            key, value = line[2:].split(":", 1)
            key = key.strip()
            value = value.strip()
            kv[key] = value
            current_key = key
        elif current_key and line.startswith("  "):
            if kv[current_key]:
                kv[current_key] += " " + line.strip()
            else:
                kv[current_key] = line.strip()
        elif current_key and not line.startswith(" "):
            current_key = None
    return kv


def check_required_fields(pattern_id: str, kv: dict):
    errors = []
    warnings = []

    for field in REQUIRED_FIELDS:
        if field not in kv or not str(kv[field]).strip():
            if field in {"original_text"}:
                status = kv.get("source_text_status", "")
                if status in {"original_source_text_unavailable", "quotation_awaiting_verification", "quotation_partially_available"}:
                    continue
            errors.append(f"Pattern {pattern_id!r} is missing required field {field!r}.")

    evidence = kv.get("evidence_level", "")
    if evidence not in VALID_EVIDENCE_LEVELS:
        errors.append(f"Pattern {pattern_id!r} has invalid evidence_level {evidence!r}.")

    validation_status = kv.get("validation_status", "")
    if validation_status not in VALID_VALIDATION_STATUSES:
        errors.append(f"Pattern {pattern_id!r} has invalid validation_status {validation_status!r}.")

    source_status = kv.get("source_text_status", "")
    if source_status not in VALID_SOURCE_TEXT_STATUS:
        errors.append(f"Pattern {pattern_id!r} has invalid source_text_status {source_status!r}.")

    quotation_status = kv.get("quotation_status", "")
    if quotation_status not in VALID_QUOTATION_STATUS:
        errors.append(f"Pattern {pattern_id!r} has invalid quotation_status {quotation_status!r}.")

    if source_status in {"original_source_text_unavailable", "quotation_awaiting_verification"}:
        warnings.append(f"Pattern {pattern_id!r} has no verified original quotation recorded in the repository.")
    if quotation_status == "quotation_partially_available":
        warnings.append(f"Pattern {pattern_id!r} has only a partial quotation recorded.")

    return errors, warnings


def main() -> int:
    if not REGISTRY.exists():
        raise FileNotFoundError(f"Registry not found: {REGISTRY}")

    text = REGISTRY.read_text(encoding="utf-8")
    blocks = extract_pattern_blocks(text)
    seen = []
    errors = []
    warnings = []

    for block in blocks:
        header = block["header"]
        if not header.startswith("IT_PAT_"):
            continue
        pattern_id = header.split(" ", 1)[0]
        seen.append(pattern_id)
        kv = parse_pattern(block)
        if not kv:
            errors.append(f"Pattern block {header!r} has no metadata fields.")
            continue

        if kv.get("pattern_id") and kv["pattern_id"] != pattern_id:
            errors.append(f"Pattern block {header!r} mismatch: pattern_id={kv['pattern_id']!r}, heading={pattern_id!r}")

        block_errors, block_warnings = check_required_fields(pattern_id, kv)
        errors.extend(block_errors)
        warnings.extend(block_warnings)

    if errors:
        print("ERRORS:")
        for item in errors:
            print(f" - {item}")
        print("\nValidation aborted because errors were found.")
        return 1

    print("Italian kernel validation passed.")
    print(f"Patterns found: {', '.join(seen)}")
    if warnings:
        print("\nWARNINGS:")
        for item in warnings:
            print(f" - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

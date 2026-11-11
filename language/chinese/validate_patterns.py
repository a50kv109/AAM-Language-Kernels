#!/usr/bin/env python3
"""Validate the Chinese pattern registry.

This script distinguishes canonical validation from research-only validation,
checks source availability states separately from structural validity, and
reports warnings independently from errors.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
REGISTRY = ROOT / "pattern_registry.md"

REQUIRED_FIELDS = [
    "pattern_id",
    "language",
    "historical_period",
    "source_title",
    "original_script_title",
    "chapter_or_volume",
    "problem_or_section",
    "edition",
    "textual_witness",
    "source_location",
    "source_reference",
    "original_text",
    "source_text_status",
    "quotation_status",
    "literal_translation",
    "semantic_explanation",
    "procedural_steps",
    "modern_formalization",
    "evidence_level",
    "textual_variants",
    "interpretation_notes",
    "unresolved_questions",
    "validation_status",
    "version_id",
]

CANONICAL_IDS = [
    "ZH_PAT_001",
    "ZH_PAT_002A",
    "ZH_PAT_002B",
    "ZH_PAT_003",
    "ZH_PAT_005",
]
RESEARCH_ONLY_IDS = ["ZH_PAT_004"]
VALID_EVIDENCE_LEVELS = {
    "VERIFIED_PRIMARY_SOURCE",
    "VERIFIED_WITH_COMMENTARY",
    "HISTORICAL_RECONSTRUCTION",
    "MODERN_INTERPRETATION",
    "HYPOTHESIS",
    "REJECTED",
}
VALID_VALIDATION_STATUSES = {
    "CANONICAL_REGISTERED",
    "RESEARCH_ONLY",
    "IN_REVIEW",
    "REJECTED",
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
        elif line.startswith("## "):
            if current is not None:
                blocks.append(current)
                current = None
        elif current is not None:
            current["lines"].append(line)
    if current is not None:
        blocks.append(current)
    return blocks


def parse_pattern(block):
    lines = block["lines"]
    kv = {}
    current_key = None
    for line in lines:
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
        if field not in kv or str(kv[field]).strip() == "":
            if field == "original_text":
                status = kv.get("source_text_status", "")
                if status in {"original_source_text_unavailable", "quotation_awaiting_verification", "quotation_partially_available"}:
                    continue
            errors.append(f"Pattern {pattern_id!r} is missing required field {field!r}.")

    evidence = kv.get("evidence_level", "")
    if evidence not in VALID_EVIDENCE_LEVELS:
        errors.append(f"Pattern {pattern_id!r} has invalid evidence_level {evidence!r}.")

    status = kv.get("validation_status", "")
    if status not in VALID_VALIDATION_STATUSES:
        errors.append(f"Pattern {pattern_id!r} has invalid validation_status {status!r}.")

    source_text_status = kv.get("source_text_status", "")
    if source_text_status not in VALID_SOURCE_TEXT_STATUS:
        errors.append(f"Pattern {pattern_id!r} has invalid source_text_status {source_text_status!r}.")

    quotation_status = kv.get("quotation_status", "")
    if quotation_status not in VALID_QUOTATION_STATUS:
        errors.append(f"Pattern {pattern_id!r} has invalid quotation_status {quotation_status!r}.")

    if pattern_id in CANONICAL_IDS and status == "RESEARCH_ONLY":
        errors.append(f"Canonical pattern {pattern_id!r} cannot be marked RESEARCH_ONLY.")
    if pattern_id in RESEARCH_ONLY_IDS and status != "RESEARCH_ONLY":
        errors.append(f"Research-only pattern {pattern_id!r} must be marked RESEARCH_ONLY.")

    if not kv.get("pattern_id", "").startswith(pattern_id):
        errors.append(f"Pattern {pattern_id!r} has inconsistent pattern_id field.")

    if source_text_status in {"original_source_text_unavailable", "quotation_awaiting_verification"}:
        warnings.append(f"Pattern {pattern_id!r} has no verified original quotation recorded in the repository.")
    if quotation_status == "quotation_partially_available":
        warnings.append(f"Pattern {pattern_id!r} has only a partial quotation recorded.")

    if source_text_status == "original_source_text_available" and not str(kv.get("original_text", "")).strip():
        errors.append(f"Pattern {pattern_id!r} is marked as source text available but original_text is empty.")

    return errors, warnings


def main() -> int:
    if not REGISTRY.exists():
        raise FileNotFoundError(f"Registry not found: {REGISTRY}")

    text = REGISTRY.read_text(encoding="utf-8")
    blocks = extract_pattern_blocks(text)
    canonical_seen = []
    research_seen = []
    errors = []
    warnings = []

    for block in blocks:
        header = block["header"]
        if not header.startswith("ZH_PAT_"):
            continue
        pid = header.split(" ", 1)[0]
        kv = parse_pattern(block)
        if not kv:
            errors.append(f"Pattern block {header!r} has no metadata fields.")
            continue
        if kv.get("pattern_id") and kv["pattern_id"] != pid:
            errors.append(f"Pattern block {header!r} mismatch: pattern_id={kv['pattern_id']!r}, heading={pid!r}")

        block_errors, block_warnings = check_required_fields(pid, kv)
        errors.extend(block_errors)
        warnings.extend(block_warnings)

        if pid in CANONICAL_IDS:
            canonical_seen.append(pid)
        elif pid in RESEARCH_ONLY_IDS:
            research_seen.append(pid)
        else:
            errors.append(f"Unexpected pattern ID {pid!r}; only canonical and research-only IDs are allowed.")

    missing_canonical = [pid for pid in CANONICAL_IDS if pid not in canonical_seen]
    if missing_canonical:
        errors.append(f"Missing canonical pattern IDs: {missing_canonical}")

    extra_canonical = [pid for pid in canonical_seen if pid not in CANONICAL_IDS]
    if extra_canonical:
        errors.append(f"Unexpected canonical IDs: {extra_canonical}")

    missing_research = [pid for pid in RESEARCH_ONLY_IDS if pid not in research_seen]
    if missing_research:
        errors.append(f"Missing research-only pattern IDs: {missing_research}")

    if errors:
        print("ERRORS:")
        for item in errors:
            print(f" - {item}")
        print("\nValidation aborted because errors were found.")
        return 1

    print("Canonical validation passed.")
    print(f"Canonical IDs: {', '.join(CANONICAL_IDS)}")
    print("Research-only validation passed.")
    print(f"Research-only IDs: {', '.join(RESEARCH_ONLY_IDS)}")
    if warnings:
        print("\nWARNINGS:")
        for item in warnings:
            print(f" - {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

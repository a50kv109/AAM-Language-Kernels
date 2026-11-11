#!/usr/bin/env python3
"""Validate geometry canon structure and fixture consistency without dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


CANON_DIR = Path(__file__).resolve().parent
REQUIRED_TYPES = {"OBJECT", "RELATION", "PROPERTY", "RULE"}
REQUIRED_DISTINCTIONS = {
    frozenset(("ENT_CIRCLE_BOUNDARY", "ENT_DISK")),
    frozenset(("ENT_LINE", "ENT_SEGMENT")),
    frozenset(("ENT_ANGLE", "EXTRINSIC_POLAR_ANGLE")),
}


def load_json_yaml(path: Path) -> dict[str, Any]:
    """Load JSON-syntax YAML, which is a YAML 1.2 subset."""
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise ValueError(f"{path}: {error}") from error
    if not isinstance(value, dict):
        raise ValueError(f"{path}: expected a top-level object")
    return value


def _discover_language_kernels(root: Path) -> list[Path]:
    language_dir = root / "language"
    if not language_dir.is_dir():
        return []
    return sorted(
        path
        for path in language_dir.iterdir()
        if path.is_dir()
        and path.name != "master"
        and (path / "passport.md").is_file()
    )


def validate_repository(root: Path) -> list[str]:
    errors: list[str] = []
    canon_dir = root / "engineering" / "geometry_canon"

    try:
        concepts_data = load_json_yaml(canon_dir / "geometry_concepts.yaml")
        benchmark = load_json_yaml(canon_dir / "benchmark" / "cross_language_benchmark.yaml")
    except ValueError as error:
        return [str(error)]

    concepts = concepts_data.get("concepts")
    if not isinstance(concepts, list) or not concepts:
        return ["geometry_concepts.yaml: concepts must be a non-empty list"]

    concept_ids: list[str] = []
    concepts_by_id: dict[str, dict[str, Any]] = {}
    source_registry = concepts_data.get("source_registry", {})
    if not isinstance(source_registry, dict):
        return ["geometry_concepts.yaml: source_registry must be an object"]
    for index, concept in enumerate(concepts):
        label = f"concepts[{index}]"
        if not isinstance(concept, dict):
            errors.append(f"{label}: expected an object")
            continue
        canonical_id = concept.get("canonical_id")
        if not isinstance(canonical_id, str) or not canonical_id:
            errors.append(f"{label}: canonical_id is required")
            continue
        if canonical_id in concepts_by_id:
            errors.append(f"{label}: duplicate canonical_id {canonical_id}")
        concept_ids.append(canonical_id)
        concepts_by_id[canonical_id] = concept
        if concept.get("semantic_type") not in REQUIRED_TYPES:
            errors.append(f"{canonical_id}: invalid semantic_type")
        for field in ("definition", "dimensionality", "relations", "properties", "valid_contexts", "example", "common_errors", "allowed_operations"):
            if field not in concept:
                errors.append(f"{canonical_id}: missing {field}")
        for field in ("relations", "properties", "valid_contexts", "common_errors", "allowed_operations"):
            if not isinstance(concept.get(field), list):
                errors.append(f"{canonical_id}: {field} must be a list")
        if not isinstance(concept.get("allowed_operations"), list):
            errors.append(f"{canonical_id}: allowed_operations must be a list")
        for source_field in ("definition_source", "relation_source", "property_source", "capability_source"):
            source_id = concept.get(source_field)
            if source_id is not None and source_id not in source_registry:
                errors.append(f"{canonical_id}: {source_field} {source_id} is missing from source_registry")
        for relation in concept.get("relations", []):
            if isinstance(relation, dict):
                target = relation.get("target")
                if target is not None and target not in concepts_by_id and target not in {item.get("canonical_id") for item in concepts}:
                    errors.append(f"{canonical_id}: relation target {target} is not a canonical_id")

    concept_set = set(concept_ids)
    if len(concepts) != 18:
        errors.append(f"expected exactly 18 requested concepts; found {len(concepts)}")

    semantic_guard = concepts_data.get("semantic_guard", {})
    distinct_pairs = {
        frozenset(pair)
        for pair in semantic_guard.get("must_remain_distinct", [])
        if isinstance(pair, list) and len(pair) == 2
    }
    for required_pair in REQUIRED_DISTINCTIONS:
        if required_pair not in distinct_pairs:
            errors.append(f"semantic_guard is missing distinction {sorted(required_pair)}")

    kernels = _discover_language_kernels(root)
    discovered_codes: set[str] = set()
    for kernel in kernels:
        index_path = kernel / "INDEX.md"
        if not index_path.is_file() or "engineering/geometry_canon.md" not in index_path.read_text(encoding="utf-8"):
            errors.append(f"{kernel.name}: INDEX.md must link to engineering/geometry_canon.md")
        axis_path = kernel / "engineering" / "geometry_canon.md"
        if not axis_path.is_file():
            errors.append(f"{kernel.name}: missing Engineering Axis geometry_canon.md")
            continue
        axis_text = axis_path.read_text(encoding="utf-8")
        code_match = re.search(r"^\- \*\*Kernel:\*\* .+ \(`([a-z]+)`\)", axis_text, re.MULTILINE)
        mapping_match = re.search(r"\]\(\.\./\.\./\.\./engineering/geometry_canon/language_mappings/([a-z]+)\.yaml\)", axis_text)
        if not code_match:
            errors.append(f"{axis_path}: missing kernel language code")
            continue
        code = code_match.group(1)
        if code in discovered_codes:
            errors.append(f"duplicate mapping language_id {code}")
        discovered_codes.add(code)
        if not mapping_match or mapping_match.group(1) != code:
            errors.append(f"{axis_path}: mapping link does not match language_id {code}")
            continue

        mapping_path = canon_dir / "language_mappings" / f"{code}.yaml"
        try:
            mapping = load_json_yaml(mapping_path)
        except ValueError as error:
            errors.append(str(error))
            continue
        if mapping.get("language_id") != code:
            errors.append(f"{mapping_path}: language_id does not match kernel code {code}")
        if mapping.get("mapping_status") != "PROPOSED":
            errors.append(f"{mapping_path}: expected mapping_status PROPOSED")
        entries = mapping.get("entries")
        if not isinstance(entries, list):
            errors.append(f"{mapping_path}: entries must be a list")
            continue
        mapping_ids = [entry.get("canonical_id") for entry in entries if isinstance(entry, dict)]
        if len(mapping_ids) != len(entries) or len(mapping_ids) != len(set(mapping_ids)):
            errors.append(f"{mapping_path}: entries must have unique canonical_id values")
        if set(mapping_ids) != concept_set:
            errors.append(f"{mapping_path}: canonical_id set does not match geometry concepts")
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            canonical_id = entry.get("canonical_id", "<missing>")
            if not isinstance(entry.get("term"), str) or not entry["term"].strip():
                errors.append(f"{mapping_path}: {canonical_id} needs a non-empty term")
            if entry.get("translation_validation_status") != "NOT_VERIFIED":
                errors.append(f"{mapping_path}: {canonical_id} must remain NOT_VERIFIED")
            if not isinstance(entry.get("grammatical_forms"), list) or not isinstance(entry.get("context_variants"), list):
                errors.append(f"{mapping_path}: {canonical_id} grammatical_forms/context_variants must be lists")
        reverse_terms: dict[str, list[str]] = {}
        for entry in entries:
            if isinstance(entry, dict) and isinstance(entry.get("term"), str):
                reverse_terms.setdefault(entry["term"].casefold(), []).append(entry.get("canonical_id", "<missing>"))
        for term, term_ids in reverse_terms.items():
            if len(term_ids) > 1:
                errors.append(f"{mapping_path}: term {term!r} maps to multiple canonical IDs {term_ids}")

    mapping_files = sorted((canon_dir / "language_mappings").glob("*.yaml"))
    mapping_codes: set[str] = set()
    for mapping_path in mapping_files:
        try:
            mapping_codes.add(load_json_yaml(mapping_path).get("language_id", ""))
        except ValueError as error:
            errors.append(str(error))
    if discovered_codes != mapping_codes:
        errors.append(
            "discovered kernel language codes do not match mapping files "
            f"(kernels={sorted(discovered_codes)}, mappings={sorted(mapping_codes)})"
        )

    if benchmark.get("benchmark_status") != "FIXTURES_ONLY_NOT_EXECUTED":
        errors.append("benchmark must be explicitly marked FIXTURES_ONLY_NOT_EXECUTED")
    if benchmark.get("language_validation_status") != "NOT_RUN":
        errors.append("benchmark language_validation_status must be NOT_RUN")
    if benchmark.get("geometry_skill_execution_status") != "NOT_RUN":
        errors.append("benchmark geometry_skill_execution_status must be NOT_RUN")
    if benchmark.get("candidate_utterance_epistemic_status") != "HYPOTHESIS":
        errors.append("candidate utterances must remain HYPOTHESIS until independently validated")
    if benchmark.get("expected_intent_epistemic_status") != "HYPOTHESIS":
        errors.append("expected intents must remain HYPOTHESIS until executed and verified")
    source_ids = benchmark.get("source_ids", [])
    if any(source_id not in source_registry for source_id in source_ids):
        errors.append("benchmark source_ids must resolve through geometry_concepts.yaml source_registry")
    expected_languages = set(benchmark.get("languages", []))
    if expected_languages != discovered_codes:
        errors.append("benchmark language list does not match discovered language kernels")
    cases = benchmark.get("cases")
    if not isinstance(cases, list):
        errors.append("benchmark cases must be a list")
        cases = []
    for case in cases:
        if not isinstance(case, dict):
            errors.append("benchmark cases must contain objects")
            continue
        case_id = case.get("case_id", "<missing>")
        utterances = case.get("candidate_utterances")
        if not isinstance(utterances, dict) or set(utterances) != expected_languages:
            errors.append(f"{case_id}: candidate utterances must cover every discovered language")
        elif any(not isinstance(text, str) or not text.strip() for text in utterances.values()):
            errors.append(f"{case_id}: candidate utterances must be non-empty strings")
        if not isinstance(case.get("expected_semantic_intent"), dict):
            errors.append(f"{case_id}: expected_semantic_intent must be an object")
        if case.get("intent_fixture_status") != "EXPECTED_NOT_EXECUTED":
            errors.append(f"{case_id}: intent fixture must not be presented as an observed result")
        if case.get("geometry_skill_execution_status") != "NOT_RUN":
            errors.append(f"{case_id}: geometry execution must remain NOT_RUN")
    ambiguity_cases = benchmark.get("ambiguity_cases")
    if not isinstance(ambiguity_cases, list):
        errors.append("benchmark ambiguity_cases must be a list")
        ambiguity_cases = []
    for case in ambiguity_cases:
        if not isinstance(case, dict):
            errors.append("benchmark ambiguity_cases must contain objects")
            continue
        case_id = case.get("case_id", "<missing>")
        utterances = case.get("candidate_utterances")
        if not isinstance(utterances, dict) or set(utterances) != expected_languages:
            errors.append(f"{case_id}: ambiguity candidates must cover every discovered language")
        if case.get("expected_resolution") not in {"AMBIGUOUS", "CLARIFY_REQUIRED"}:
            errors.append(f"{case_id}: expected_resolution must preserve ambiguity")
        if case.get("status") != "EXPECTED_NOT_EXECUTED":
            errors.append(f"{case_id}: ambiguity fixture must not be presented as an observed result")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CANON_DIR.parents[1], help="repository root")
    args = parser.parse_args()
    errors = validate_repository(args.root.resolve())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    mapping_count = len(list((args.root / "engineering/geometry_canon/language_mappings").glob("*.yaml")))
    print(f"Geometry canon structure valid: 18 concepts, {mapping_count} language mappings.")
    print("No linguistic validation or Geometry Skill execution is claimed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

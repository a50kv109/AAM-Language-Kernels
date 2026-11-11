"""Focused structural tests for the shared geometry canon."""

import unittest
from pathlib import Path

from validate_geometry_canon import load_json_yaml, validate_repository


ROOT = Path(__file__).resolve().parents[2]
CANON_DIR = ROOT / "engineering" / "geometry_canon"


class GeometryCanonTests(unittest.TestCase):
    def test_repository_has_complete_language_mappings_and_benchmark_fixtures(self) -> None:
        self.assertEqual(validate_repository(ROOT), [])

    def test_boundary_region_line_and_segment_are_distinct(self) -> None:
        data = load_json_yaml(CANON_DIR / "geometry_concepts.yaml")
        concepts = {item["canonical_id"]: item for item in data["concepts"]}

        self.assertEqual(concepts["ENT_CIRCLE_BOUNDARY"]["dimensionality"], "1D")
        self.assertEqual(concepts["ENT_DISK"]["dimensionality"], "2D")
        self.assertIn("unbounded", concepts["ENT_LINE"]["properties"])
        self.assertIn("bounded", concepts["ENT_SEGMENT"]["properties"])
        self.assertEqual(concepts["REL_PARALLEL"]["semantic_type"], "RELATION")
        self.assertEqual(concepts["REL_PERPENDICULAR"]["semantic_type"], "RELATION")

    def test_fixture_metadata_does_not_claim_observed_language_or_geometry_results(self) -> None:
        benchmark = load_json_yaml(CANON_DIR / "benchmark" / "cross_language_benchmark.yaml")

        self.assertEqual(benchmark["language_validation_status"], "NOT_RUN")
        self.assertEqual(benchmark["geometry_skill_execution_status"], "NOT_RUN")
        self.assertEqual(benchmark["candidate_utterance_epistemic_status"], "HYPOTHESIS")
        self.assertEqual(benchmark["expected_intent_epistemic_status"], "HYPOTHESIS")
        self.assertTrue(all(case["geometry_skill_execution_status"] == "NOT_RUN" for case in benchmark["cases"]))
        self.assertTrue(all(case["intent_fixture_status"] == "EXPECTED_NOT_EXECUTED" for case in benchmark["cases"]))
        self.assertIn("AMBIGUOUS", {case["expected_resolution"] for case in benchmark["ambiguity_cases"]})

    def test_language_mapping_reverse_lookup_does_not_merge_concepts(self) -> None:
        for mapping_path in (CANON_DIR / "language_mappings").glob("*.yaml"):
            mapping = load_json_yaml(mapping_path)
            terms = [entry["term"].casefold() for entry in mapping["entries"]]
            with self.subTest(language=mapping["language_id"]):
                self.assertEqual(len(terms), len(set(terms)))


if __name__ == "__main__":
    unittest.main()

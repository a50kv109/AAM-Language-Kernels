from __future__ import annotations

import json
import unittest
from types import SimpleNamespace

from core.hebrew_nlp_adapter import HebrewNLPAdapter


class HebrewNLPAdapterTests(unittest.TestCase):
    def test_unavailable_engine_is_reported_without_guessing(self) -> None:
        adapter = HebrewNLPAdapter(
            unavailable_status="MODEL_UNAVAILABLE",
            unavailable_reason="Hebrew model is not installed.",
        )
        for text in ("שלום", "ספר", "קראתי ספר", "כתב", "מכתב", "המלך", "כתבו"):
            with self.subTest(text=text):
                result = adapter.analyze(text)
                self.assertEqual(result["processing_status"], "MODEL_UNAVAILABLE")
                self.assertEqual(result["original_text"], text)
                self.assertTrue(all(token["lemma"] is None for token in result["tokens"]))
                self.assertTrue(all(token["pos"] is None for token in result["tokens"]))
                self.assertTrue(
                    all(item["root_status"] == "UNKNOWN" for item in result["root_binyan"])
                )

    def test_pipeline_output_maps_to_structured_result_and_source_span(self) -> None:
        seen: list[str] = []

        def fake_pipeline(text: str) -> SimpleNamespace:
            seen.append(text)
            word = SimpleNamespace(
                id=1,
                text="שלום",
                lemma="שלום",
                upos="NOUN",
                xpos="NN",
                feats="Gender=Masc|Number=Sing|HebBinyan=PAAL",
                head=0,
                deprel="root",
            )
            token = SimpleNamespace(
                text="שלום",
                start_char=0,
                end_char=4,
                words=[word],
            )
            return SimpleNamespace(sentences=[SimpleNamespace(tokens=[token])])

        adapter = HebrewNLPAdapter(
            fake_pipeline,
            engine_version="test-version",
            model_id="he:test-fixture",
        )
        result = adapter.analyze("שלום")

        self.assertEqual(seen, ["שלום"])
        self.assertEqual(result["processing_status"], "SUCCESS")
        self.assertEqual(result["original_text"], "שלום")
        self.assertEqual(result["normalized_text"], "שלום")
        self.assertEqual(result["tokens"][0]["normalized_char_span"], [0, 4])
        self.assertEqual(result["tokens"][0]["source_token_indices"], [0])
        self.assertEqual(result["tokens"][0]["words"][0]["lemma"], "שלום")
        self.assertEqual(result["tokens"][0]["words"][0]["pos"], "NOUN")
        self.assertEqual(
            result["tokens"][0]["words"][0]["morphological_features"]["HebBinyan"],
            "PAAL",
        )
        self.assertEqual(result["root_binyan"][0]["root_status"], "NOT_SUPPORTED")
        self.assertEqual(result["root_binyan"][0]["binyan"], "PAAL")
        self.assertEqual(result["dependencies"][0]["relation"], "root")
        self.assertEqual(result["model_id"], "he:test-fixture")
        json.dumps(result, ensure_ascii=False)

    def test_empty_and_invalid_inputs_have_explicit_results(self) -> None:
        adapter = HebrewNLPAdapter()
        self.assertEqual(adapter.analyze(" \t")["processing_status"], "EMPTY_INPUT")
        with self.assertRaises(TypeError):
            adapter.analyze(None)  # type: ignore[arg-type]

    def test_normalized_input_is_sent_to_the_pipeline_but_source_is_preserved(self) -> None:
        import unicodedata

        original = unicodedata.normalize("NFD", "שָׁלוֹם")
        seen: list[str] = []

        def empty_document_pipeline(text: str) -> SimpleNamespace:
            seen.append(text)
            return SimpleNamespace(sentences=[])

        result = HebrewNLPAdapter(empty_document_pipeline).analyze(original)
        self.assertEqual(result["original_text"], original)
        self.assertEqual(result["normalized_text"], unicodedata.normalize("NFC", original))
        self.assertEqual(seen, [result["normalized_text"]])


if __name__ == "__main__":
    unittest.main()

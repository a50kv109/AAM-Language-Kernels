from __future__ import annotations

import json
import unicodedata
import unittest

from core.hebrew_core import HebrewKernel


class HebrewKernelTests(unittest.TestCase):
    def test_empty_and_whitespace_input_return_empty_result(self) -> None:
        for text in ("", " \t\n"):
            with self.subTest(text=repr(text)):
                self.assertEqual(HebrewKernel.analyze_sentence(text)["status"], "EMPTY_INPUT")
                self.assertEqual(HebrewKernel.analyze_sentence(text)["tokens"], [])

    def test_hebrew_words_are_observed_in_logical_order(self) -> None:
        text = "שלום עולם"
        result = HebrewKernel.analyze_sentence(text)
        self.assertEqual(result["normalized_text"], text)
        self.assertEqual([token["text"] for token in result["tokens"]], ["שלום", "עולם"])
        self.assertTrue(all(token["contains_hebrew_letters"] for token in result["tokens"]))

    def test_final_letter_forms_are_classified_as_hebrew_letters(self) -> None:
        for letter in "ךםןףץ":
            with self.subTest(letter=letter):
                self.assertTrue(HebrewKernel.is_hebrew_letter(letter))

    def test_niqqud_is_preserved_and_counted_as_marks(self) -> None:
        result = HebrewKernel.analyze_sentence("שָׁלוֹם")
        token = result["tokens"][0]
        self.assertEqual(token["text"], "שָׁלוֹם")
        self.assertGreater(token["hebrew_mark_count"], 0)

    def test_nfc_and_nfd_are_supported_without_removing_marks(self) -> None:
        nfc = "שָׁלוֹם֑"
        nfd = unicodedata.normalize("NFD", nfc)
        self.assertEqual(HebrewKernel.normalize(nfd), nfc)
        self.assertEqual(HebrewKernel.normalize_form(nfc, "NFD"), nfd)
        self.assertEqual(HebrewKernel.analyze_sentence(nfd)["original_text"], nfd)
        self.assertEqual(HebrewKernel.analyze_sentence(nfd)["normalized_text"], nfc)
        self.assertIn("֑", HebrewKernel.normalize(nfd))

    def test_mixed_script_digits_punctuation_and_first_strong_direction(self) -> None:
        text = "שלום API-42!"
        result = HebrewKernel.analyze_sentence(text)
        self.assertEqual(result["original_text"], text)
        self.assertEqual(result["normalized_text"], text)
        self.assertEqual(result["direction"]["primary_direction"], "RTL")
        self.assertTrue(result["direction"]["mixed_directional_text"])
        self.assertTrue(result["direction"]["contains_latin_letters"])
        self.assertTrue(result["direction"]["contains_digits"])
        self.assertEqual(result["tokens"][1]["text"], "API-42!")

    def test_nfc_only_normalization_form_is_rejected_when_unknown(self) -> None:
        with self.assertRaises(ValueError):
            HebrewKernel.normalize_form("שלום", "NFKC")

    def test_unknown_root_is_not_guessed_from_letters(self) -> None:
        result = HebrewKernel.analyze_sentence("כתב")
        token = result["tokens"][0]
        self.assertEqual(token["lexical_status"], "UNKNOWN")
        self.assertEqual(token["root_candidates"], [])
        self.assertEqual(result["root_binyan"][0]["root_status"], "UNKNOWN")

    def test_result_is_json_serializable_with_hebrew_text(self) -> None:
        result = HebrewKernel.analyze_sentence("תורה")
        encoded = json.dumps(result, ensure_ascii=False)
        self.assertIn("תורה", encoded)
        self.assertEqual(json.loads(encoded)["tokens"][0]["lexical_status"], "UNKNOWN")

    def test_non_string_input_is_rejected(self) -> None:
        with self.assertRaises(TypeError):
            HebrewKernel.analyze_sentence(None)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()

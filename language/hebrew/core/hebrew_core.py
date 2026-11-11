"""Unicode-preserving text utilities; this module does not perform Hebrew linguistics."""

from __future__ import annotations

import re
import unicodedata
from typing import Any


HEBREW_LETTERS = frozenset("אבגדהוזחטיכלמנסעפצקרשת")
FINAL_FORMS = frozenset("ךםןףץ")
ALL_HEBREW_LETTER_FORMS = HEBREW_LETTERS | FINAL_FORMS


class HebrewKernel:
    """Provide deterministic Unicode and whitespace-token observations."""

    kernel_id = "CORE_HEBREW_V1.0"
    status = "PROPOSED"

    @staticmethod
    def normalize_form(text: str, form: str) -> str:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if form not in {"NFC", "NFD"}:
            raise ValueError("form must be NFC or NFD")
        return unicodedata.normalize(form, text)

    @staticmethod
    def normalize(text: str) -> str:
        return HebrewKernel.normalize_form(text, "NFC")

    @staticmethod
    def is_hebrew_letter(character: str) -> bool:
        return len(character) == 1 and character in ALL_HEBREW_LETTER_FORMS

    @staticmethod
    def _script_metadata(text: str) -> dict[str, Any]:
        strong_directions: list[str] = []
        has_hebrew = False
        has_latin = False
        has_digits = False

        for character in text:
            bidi_class = unicodedata.bidirectional(character)
            if bidi_class in {"R", "AL"}:
                strong_directions.append("RTL")
            elif bidi_class == "L":
                strong_directions.append("LTR")

            if character in ALL_HEBREW_LETTER_FORMS:
                has_hebrew = True
            if character.isalpha() and "LATIN" in unicodedata.name(character, ""):
                has_latin = True
            if character.isdecimal():
                has_digits = True

        return {
            "primary_direction": strong_directions[0] if strong_directions else "LTR",
            "mixed_directional_text": "RTL" in strong_directions and "LTR" in strong_directions,
            "contains_hebrew_letters": has_hebrew,
            "contains_latin_letters": has_latin,
            "contains_digits": has_digits,
            "direction_note": (
                "Direction is the first strong Unicode bidi class; logical order is preserved "
                "and no visual bidi reordering is performed."
            ),
        }

    @staticmethod
    def _empty_analysis(text: str, normalized: str) -> dict[str, Any]:
        return {
            "kernel_id": HebrewKernel.kernel_id,
            "status": "EMPTY_INPUT",
            "processing_status": "EMPTY_INPUT",
            "engine_id": "aam.hebrew.script_only",
            "model_id": None,
            "original_text": text,
            "normalized_text": normalized,
            "tokens": [],
            "lemmas": [],
            "POS": [],
            "morphological_features": [],
            "dependencies": [],
            "root_binyan": [],
            "unresolved_fields": [],
            "provenance": {
                "normalizer": "Python unicodedata",
                "unicode_database_version": unicodedata.unidata_version,
                "nlp_engine": None,
            },
            "direction": HebrewKernel._script_metadata(text),
        }

    @classmethod
    def analyze_sentence(cls, text: str) -> dict[str, Any]:
        normalized = cls.normalize(text)
        if not normalized.strip():
            return cls._empty_analysis(text, normalized)

        tokens = []
        for match in re.finditer(r"\S+", normalized):
            token = match.group()
            letters = [char for char in token if char in ALL_HEBREW_LETTER_FORMS]
            marks = [
                char
                for char in token
                if 0x0591 <= ord(char) <= 0x05C7
                and unicodedata.category(char).startswith("M")
            ]
            tokens.append(
                {
                    "token_id": len(tokens),
                    "source_token_index": len(tokens),
                    "text": token,
                    "normalized_char_span": [match.start(), match.end()],
                    "contains_hebrew_letters": bool(letters),
                    "hebrew_letter_count": len(letters),
                    "hebrew_mark_count": len(marks),
                    "lexical_status": "UNKNOWN" if letters else "NOT_HEBREW",
                    "root_candidates": [],
                    "lemma": None,
                    "pos": None,
                    "morphological_features": None,
                    "dependencies": None,
                }
            )

        direction = cls._script_metadata(text)
        return {
            "kernel_id": cls.kernel_id,
            "status": "OBSERVED",
            "processing_status": "SCRIPT_ONLY",
            "engine_id": "aam.hebrew.script_only",
            "model_id": None,
            "original_text": text,
            "normalized_text": normalized,
            "tokens": tokens,
            "lemmas": [],
            "POS": [],
            "morphological_features": [],
            "dependencies": [],
            "root_binyan": [
                {
                    "token_id": token["token_id"],
                    "word_id": None,
                    "root": None,
                    "root_status": "UNKNOWN",
                    "binyan": None,
                    "binyan_status": "UNKNOWN",
                }
                for token in tokens
                if token["contains_hebrew_letters"]
            ],
            "unresolved_fields": [
                "lemmas",
                "POS",
                "morphological_features",
                "dependencies",
                "root",
                "binyan",
                "semantic_sense",
            ],
            "provenance": {
                "normalizer": "Python unicodedata",
                "unicode_database_version": unicodedata.unidata_version,
                "nlp_engine": None,
            },
            "direction": direction,
            "direction_note": direction["direction_note"],
            "analysis_limit": "Whitespace tokenization and code-point classification only; no morphology or syntax analysis.",
        }

"""Optional Stanza integration for the Hebrew kernel."""

from __future__ import annotations

from collections.abc import Callable
from importlib import import_module
from typing import Any

from .hebrew_core import HebrewKernel


StanzaPipeline = Callable[[str], Any]


class HebrewNLPAdapter:
    """Map Stanza Hebrew UD annotations into the AAM analysis result shape."""

    def __init__(
        self,
        pipeline: StanzaPipeline | None = None,
        *,
        engine_version: str | None = None,
        model_id: str | None = None,
        unavailable_status: str = "ENGINE_UNAVAILABLE",
        unavailable_reason: str = "Stanza Hebrew pipeline has not been configured.",
    ) -> None:
        self._pipeline = pipeline
        self.engine_version = engine_version
        self.model_id = model_id
        self._unavailable_status = unavailable_status
        self._unavailable_reason = unavailable_reason

    @classmethod
    def from_stanza(
        cls,
        *,
        model_id: str = "he:default",
        model_dir: str | None = None,
        processors: str = "tokenize,mwt,pos,lemma,depparse",
    ) -> HebrewNLPAdapter:
        """Load already-installed Stanza models; never download models implicitly."""
        try:
            stanza = import_module("stanza")
        except ModuleNotFoundError as exc:
            return cls(
                model_id=model_id,
                unavailable_status="ENGINE_UNAVAILABLE",
                unavailable_reason=f"Stanza or one of its dependencies is missing: {exc.name}",
            )

        pipeline_options: dict[str, Any] = {
            "lang": "he",
            "processors": processors,
            "use_gpu": False,
            "verbose": False,
            "download_method": None,
        }
        if model_dir is not None:
            pipeline_options["dir"] = model_dir

        try:
            pipeline = stanza.Pipeline(**pipeline_options)
        except FileNotFoundError as exc:
            return cls(
                model_id=model_id,
                engine_version=getattr(stanza, "__version__", None),
                unavailable_status="MODEL_UNAVAILABLE",
                unavailable_reason=f"Stanza Hebrew model is not installed locally: {exc}",
            )

        return cls(
            pipeline,
            engine_version=getattr(stanza, "__version__", None),
            model_id=model_id,
        )

    @staticmethod
    def _features(raw_features: str | None) -> dict[str, str]:
        if not raw_features:
            return {}
        features: dict[str, str] = {}
        for item in raw_features.split("|"):
            key, separator, value = item.partition("=")
            if separator:
                features[key] = value
        return features

    def _unavailable_result(self, text: str) -> dict[str, Any]:
        result = HebrewKernel.analyze_sentence(text)
        if result["processing_status"] != "EMPTY_INPUT":
            result["processing_status"] = self._unavailable_status
            result["unresolved_fields"] = [
                "lemmas",
                "POS",
                "morphological_features",
                "dependencies",
                "root",
                "binyan",
                "semantic_sense",
            ]
        result["engine_id"] = "stanza"
        result["model_id"] = self.model_id
        result["provenance"]["nlp_engine"] = {
            "id": "stanza",
            "version": self.engine_version,
            "model_id": self.model_id,
            "available": False,
            "reason": self._unavailable_reason,
        }
        result["analysis_limit"] = self._unavailable_reason
        return result

    def analyze(self, text: str) -> dict[str, Any]:
        if not isinstance(text, str):
            raise TypeError("text must be a string")
        if self._pipeline is None or not text.strip():
            return self._unavailable_result(text)

        result = HebrewKernel.analyze_sentence(text)
        if result["processing_status"] == "EMPTY_INPUT":
            result["engine_id"] = "stanza"
            result["model_id"] = self.model_id
            result["provenance"]["nlp_engine"] = {
                "id": "stanza",
                "version": self.engine_version,
                "model_id": self.model_id,
                "available": True,
            }
            return result

        document = self._pipeline(result["normalized_text"])
        source_tokens = result["tokens"]
        tokens: list[dict[str, Any]] = []
        lemmas: list[dict[str, Any]] = []
        pos_tags: list[dict[str, Any]] = []
        morphological_features: list[dict[str, Any]] = []
        dependencies: list[dict[str, Any]] = []
        root_binyan: list[dict[str, Any]] = []

        for sentence_index, sentence in enumerate(document.sentences):
            for token in sentence.tokens:
                token_id = len(tokens)
                start = getattr(token, "start_char", None)
                end = getattr(token, "end_char", None)
                char_span = [start, end] if isinstance(start, int) and isinstance(end, int) else None
                source_token_indices = (
                    [
                        source_token["source_token_index"]
                        for source_token in source_tokens
                        if char_span is not None
                        and source_token["normalized_char_span"][0] < char_span[1]
                        and char_span[0] < source_token["normalized_char_span"][1]
                    ]
                    if char_span is not None
                    else []
                )
                word_results: list[dict[str, Any]] = []

                for word in token.words:
                    word_id = getattr(word, "id", None)
                    features = self._features(getattr(word, "feats", None))
                    lemma = getattr(word, "lemma", None)
                    pos = getattr(word, "upos", None)
                    head = getattr(word, "head", None)
                    relation = getattr(word, "deprel", None)
                    binyan = features.get("HebBinyan")
                    word_result = {
                        "word_id": word_id,
                        "text": getattr(word, "text", None) or token.text,
                        "lemma": lemma,
                        "pos": pos,
                        "xpos": getattr(word, "xpos", None),
                        "morphological_features": features,
                        "dependency": {"head": head, "relation": relation},
                        "source_token_id": token_id,
                        "root": None,
                        "root_status": "NOT_SUPPORTED",
                        "binyan": binyan,
                        "binyan_status": "MODEL_OUTPUT" if binyan is not None else "UNKNOWN",
                    }
                    word_results.append(word_result)
                    lemmas.append(
                        {"sentence_id": sentence_index, "word_id": word_id, "value": lemma}
                    )
                    pos_tags.append(
                        {"sentence_id": sentence_index, "word_id": word_id, "value": pos}
                    )
                    morphological_features.append(
                        {
                            "sentence_id": sentence_index,
                            "word_id": word_id,
                            "value": features,
                        }
                    )
                    dependencies.append(
                        {
                            "sentence_id": sentence_index,
                            "word_id": word_id,
                            "head": head,
                            "relation": relation,
                        }
                    )
                    root_binyan.append(
                        {
                            "sentence_id": sentence_index,
                            "word_id": word_id,
                            "root": None,
                            "root_status": "NOT_SUPPORTED",
                            "binyan": binyan,
                            "binyan_status": (
                                "MODEL_OUTPUT" if binyan is not None else "UNKNOWN"
                            ),
                        }
                    )

                tokens.append(
                    {
                        "token_id": token_id,
                        "analysis_token_index": token_id,
                        "source_token_indices": source_token_indices,
                        "text": token.text,
                        "normalized_char_span": char_span,
                        "words": word_results,
                    }
                )

        unresolved_fields = ["root", "semantic_sense"]
        if not root_binyan:
            unresolved_fields.extend(
                ["lemmas", "POS", "morphological_features", "dependencies", "binyan"]
            )
        if any(not token["source_token_indices"] for token in tokens):
            unresolved_fields.append("source_alignment")
        if any(item["value"] is None for item in lemmas):
            unresolved_fields.append("lemmas")
        if any(item["value"] is None for item in pos_tags):
            unresolved_fields.append("POS")
        if any(item["head"] is None or item["relation"] is None for item in dependencies):
            unresolved_fields.append("dependencies")
        if any(item["binyan"] is None for item in root_binyan):
            unresolved_fields.append("binyan")

        result.update(
            {
                "status": "ANALYZED",
                "processing_status": "SUCCESS",
                "engine_id": "stanza",
                "model_id": self.model_id,
                "tokens": tokens,
                "lemmas": lemmas,
                "POS": pos_tags,
                "morphological_features": morphological_features,
                "dependencies": dependencies,
                "root_binyan": root_binyan,
                "unresolved_fields": unresolved_fields,
                "provenance": {
                    "normalizer": "Python unicodedata (NFC)",
                    "unicode_database_version": result["provenance"][
                        "unicode_database_version"
                    ],
                    "nlp_engine": {
                        "id": "stanza",
                        "version": self.engine_version,
                        "model_id": self.model_id,
                        "training_data": (
                            "Hebrew Universal Dependencies model; confirm the installed "
                            "package/revision before interpreting results."
                        ),
                        "automatic_model_download": False,
                    },
                },
                "analysis_limit": (
                    "Stanza annotations reflect the configured Hebrew UD model. "
                    "Root extraction and semantic-sense selection are not provided."
                ),
            }
        )
        return result

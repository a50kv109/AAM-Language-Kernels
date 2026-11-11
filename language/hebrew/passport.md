# Kernel Passport: CORE_HEBREW_V1.0

- **Language:** Hebrew (עברית)
- **ISO 639-3:** `heb`
- **Script:** Hebrew
- **Version:** 1.0.0 (proposed baseline)
- **Status:** PROPOSED / INITIAL BASELINE
- **Architecture:** AAM-V2 / AXIS-10 repository framing
- **Scope:** Evidence-aware catalog of Hebrew research areas, Unicode-preserving script utilities, and an optional NLP integration boundary.
- **Implementation:** NFC analysis normalization, explicit NFC/NFD normalization, preservation of original text and Hebrew marks, whitespace tokenization with normalized-text spans, bidi-direction metadata, and a JSON-compatible AAM result.
- **Optional NLP:** `HebrewNLPAdapter` maps Stanza Hebrew UD pipeline output to token, lemma, POS, morphological-feature, dependency, and provenance fields. Stanza and the Hebrew model are not installed in the current environment; no model download is triggered automatically.
- **Not implemented:** Native root extraction, semantic-sense selection, audio processing, or sacred-text interpretation. Binyan is passed through only if emitted as a model feature.
- **Sources:** The supplied ZIPs and transfer JSON are inventoried in `validation/source_comparison.md`. They contain no bibliographic linguistic references. Linguistic statements beyond code-point handling remain NOT_VERIFIED until sourced.
- **Validation:** Unit tests cover Unicode behavior, the result contract, and Stanza-output mapping with a test double. They do not validate a live Stanza model, Hebrew linguistic accuracy, corpus performance, or historical coverage.

Author-reported AAM extensions and metrics are kept apart from the linguistic scope in `extensions/aam_extensions.json`. They are not objective measurements of Hebrew.

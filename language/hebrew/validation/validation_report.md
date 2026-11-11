# Validation Scope

**Review disposition:** READY FOR INTEGRATION REVIEW — live Stanza/model inference remains pending.

## Executed checks

- `python3 -m unittest discover -s tests -v` — PASS (14 tests).
- `python3 validate_hebrew_kernel.py` — PASS (structural checks only).
- `python3 examples/basic_usage.py` — the script-only result ran; the optional adapter explicitly reported `ENGINE_UNAVAILABLE`.
- Pylance diagnostics for `core/hebrew_core.py` and `core/hebrew_nlp_adapter.py` — no diagnostics.
- Chinese and Italian registry validators — PASS, with their existing missing-quotation warnings.

The structural validator checks file structure, metadata syntax, registry integrity, links, and test presence. Unit tests cover normalization, mark preservation, logical-order and direction metadata, fallback behavior, JSON compatibility, and mapping an injected Stanza-shaped document into the AAM result contract.

Stanza and the Hebrew model were not installed or downloaded in the current environment. No live NLP inference was run. The test double verifies adapter mapping only; it does not establish Hebrew model quality, corpus performance, linguistic completeness, root analysis, historical accuracy, phonetic correctness, or sacred-text interpretation.

The source archive comparison and the failing S test are recorded in [source_comparison.md](source_comparison.md). Kernel status remains PROPOSED / INITIAL BASELINE.

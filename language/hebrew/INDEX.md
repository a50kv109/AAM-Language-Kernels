# Hebrew Language Kernel (CORE_HEBREW_V1.0)

## Status

- **Kernel status:** PROPOSED / INITIAL BASELINE
- **Implementation maturity:** Unicode-preserving script utilities plus an optional Stanza adapter. Stanza and its Hebrew model are not installed in the current environment.
- **Not claimed:** a complete Hebrew grammar, root analyzer, acoustic processor, sacred-text interpreter, or corpus-validated language engine.

## Components

- [passport.md](passport.md) — scope, status, and evidence boundaries.
- [STRUCTURE.md](STRUCTURE.md) — component architecture, optional NLP path, and implementation boundary.
- [ground_truth_matrix.md](ground_truth_matrix.md) — proposed AAM semantic anchors.
- [pattern_registry.csv](pattern_registry.csv) — schema for future source-backed patterns; currently no records are registered.
- [phonetics/](phonetics/) — orthographic and phonetic research inventory.
- [morphology/](morphology/) and [grammar/](grammar/) — research scopes; no morphological parser is implemented.
- [semantics/](semantics/) and [context/](context/) — semantic and ambiguity policies.
- [historical/](historical/) — distinct historical research areas; not a unified norm.
- [engineering/](engineering/) and [sacred/](sacred/) — AAM engineering proposals and cultural concepts.
- [engineering/geometry_canon.md](engineering/geometry_canon.md) — proposed link to the shared geometry canon; terminology is NOT_VERIFIED.
- [core/](core/) — standard-library Unicode/script utilities and the optional [HebrewNLPAdapter](core/hebrew_nlp_adapter.py).
- [examples/](examples/) and [tests/](tests/) — runnable example and behavioral unit tests.
- [extensions/](extensions/) — author-reported AAM extensions kept separate from linguistic evidence.
- [validation/](validation/) — source comparison, known gaps, and validation scope.
- [validate_hebrew_kernel.py](validate_hebrew_kernel.py) — read-only structural validator.

## Epistemic policy

Linguistic facts, source-supported claims, AAM proposals, experimental models, and unknowns are kept distinct. The supplied archives do not include bibliographic linguistic sources. Consequently, descriptive coverage claims remain NOT_VERIFIED until a source record and review are added. `ENGINEERED_IGNORANCE` is preserved: ambiguous roots, omitted arguments, or underdetermined readings remain `UNKNOWN`.

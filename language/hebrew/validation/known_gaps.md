# Known Gaps

- The provided ZIPs contain no bibliographic Hebrew linguistic sources or corpus.
- Root extraction, binyan analysis, inflection, syntax, semantics, historical variation, and contextual disambiguation are not implemented.
- The pattern registry has a schema but zero canonical records.
- `AcousticProcessor` in B/C is placeholder code; no audio features are extracted.
- `PaniniStateMachine` processes Sanskrit-like transliteration examples and is not a Hebrew analyzer; one supplied test fails.
- The source JSON's fixed TDI, Sobornost, sacredness, EVRID, NADI, and ZIC values have no measurement protocol in the package.
- Definitions for OST-1 through OST-9 and MODULE-64 implementation details were not present in the supplied transfer artifacts.
- The core does not perform Unicode Bidirectional Algorithm layout; it only reports first-strong direction and preserves logical order.
- Built-in tokenization remains whitespace-only and does not split punctuation, clitics, or Hebrew multi-word tokens.
- Stanza and the Hebrew UD model are not installed in the current environment. Live model output, model-package identity, and model-specific resource use have not been verified.
- The adapter's result conversion is tested with a pipeline test double, not a live Stanza document.
- Stanza UD outputs are limited by their training treebank/domain and do not establish coverage of historical, biblical, rabbinic, or sacred Hebrew.
- Root extraction is unsupported. Binyan is only passed through from a `HebBinyan` model feature when present; no independent root/binyan engine is included.
- Semantic-sense selection and cross-lingual semantic preservation remain unresolved.
- Sacred/cultural names are listed without definitions or interpretive claims; these need sourced and context-sensitive review.

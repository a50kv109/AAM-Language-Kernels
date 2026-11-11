# CORE_HEBREW_V1.0 Structure

## Layer map

| Area | Scope | Current status |
|---|---|---|
| Phonetics | Hebrew script, pointing marks, pronunciation and acoustic research questions | Inventory only; linguistic claims NOT_VERIFIED |
| Morphology | Roots, binyanim, inflection, gender/number, construct forms, irregular roots | Research outline; no analyzer |
| Grammar | Particles, clause structure, agreement and modern usage | Research outline; no parser |
| Semantics | Lexical senses, polysemy and cultural concepts | No canonical semantic registry |
| Context | Ellipsis and ambiguity handling | Policy only; unresolved cases remain UNKNOWN |
| Historical | Biblical, Mishnaic, Talmudic, Medieval and Modern Hebrew | Separate research scopes; not one shared norm |
| Engineering | SOL anchors and technical-language examples | AAM proposal, not language-specific validation |
| Sacred / cultural | Tanakh, Torah, Talmud, Zohar, Shekhinah, Shabbat and Kashrut | Concept index only; no numerical sacredness score |
| Core utilities | NFC analysis normalization, explicit NFC/NFD normalization, preservation of original text and Hebrew marks, whitespace tokenization, first-strong direction metadata, JSON-compatible result | Implemented and unit-tested; not linguistic parsing |
| NLP adapter | Optional Stanza Hebrew UD pipeline mapping to token, lemma, POS, morphology, and dependency fields | Adapter implemented; Stanza and the Hebrew model are not installed in the current environment |

## Implemented text path

`INPUT → NFC NORMALIZATION (MARKS PRESERVED) → WHITESPACE TOKENIZATION → SCRIPT/DIRECTION METADATA → JSON-COMPATIBLE RESULT`

NFC is used for analysis, while `normalize_form` also exposes NFD for callers that require canonical decomposition. Original input is retained unchanged. Hebrew niqqud and cantillation marks are not stripped. Direction metadata follows the first strong Unicode bidi class and does not implement the Unicode Bidirectional Algorithm or reorder text. The built-in tokenizer splits on whitespace only; it does not identify punctuation boundaries, clitics, morphemes, roots, or syntax.

## Optional Stanza path

`HebrewNLPAdapter.from_stanza()` requests Hebrew tokenization, multi-word-token expansion, POS, lemma, and dependency processors with CPU execution. It sets `download_method=None`; it will not download missing model files. If Stanza or the Hebrew model is absent, results explicitly report `ENGINE_UNAVAILABLE` or `MODEL_UNAVAILABLE`, leaving linguistic fields unresolved. An injected pipeline can also be mapped into the same result contract.

For a provisioned Stanza Hebrew UD model, token-level results retain the Stanza token's normalized-text span and map it back to overlapping whitespace-token indices from the normalized input. Expanded word analyses remain attached to their Stanza token. The result includes lemmas, UPOS/XPOS, parsed morphological features, dependencies, engine/model provenance, and unresolved fields. A `HebBinyan` feature is passed through only when the model emits it. Root extraction and semantic-sense selection remain unsupported; Stanza output is not treated as historical or sacred-text validation.

The Stanza UD model documentation describes models trained on Universal Dependencies treebanks. Their outputs are corpus/model-specific and must not be generalized to all Hebrew periods or genres. See [Stanza pipeline documentation](https://stanfordnlp.github.io/stanza/pipeline.html), [model documentation](https://stanfordnlp.github.io/stanza/available_models.html), and [model download documentation](https://stanfordnlp.github.io/stanza/download_models.html).

## Root and context resolution

No root is inferred by letter overlap or by stripping prefixes/suffixes. No verified root lexicon was supplied. Lexical/root resolution therefore remains `UNKNOWN` in the built-in core and `NOT_SUPPORTED` in the Stanza adapter, including where several roots could plausibly underlie an unpointed form. This is the kernel’s `ENGINEERED_IGNORANCE` boundary, not a missing-value default that callers may silently override.

## AAM extension boundary

OST identifiers, EVRID, NADI, ZIC, MODULE-64 metrics and the Dharma Manifest are recorded separately under `extensions/`. Supplied numerical values are author-reported/proposed metadata, not verified language properties or measured performance. Definitions missing from the transfer package are marked NOT_VERIFIED rather than reconstructed.

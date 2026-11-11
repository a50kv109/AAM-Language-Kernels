# L2_JA Structure

## L1 - GRAMMATICAL CORE
Common clause-order patterns and particle-driven structure, with explicit recognition that Japanese discourse can be flexible and contextually reduced rather than rigidly SOV in every register.

## L2 - LEXICAL & KANJI SEMANTICS
Kanji as semantic nodes and context-sensitive readings, with lexical distinctions treated as a research layer rather than a final corpus-validated catalogue.

## L3 - ENGINEERING SEMANTICS
Mapping of selected SOL anchors and technical terms in a proposed engineering layer, including the [shared geometry-canon mapping](engineering/geometry_canon.md); geometry terms are NOT_VERIFIED and are not a parser or executor.

## L4 - CONTEXT & OMISSION RESOLUTION
Explicit handling of omitted subjects, particles, and context-dependent meaning under `ENGINEERED_IGNORANCE`, without inventing unstated actors or causal assumptions.

## Research extension: input-to-output processing model
- **INPUT**: User text or document context.
- **SEGMENTATION**: Tokenization and candidate grouping.
- **CANDIDATE GENERATION**: Multiple lexical and kanji interpretations.
- **CONTEXT RESOLUTION**: Surrounding-text and domain-aware disambiguation.
- **RANKING**: Confidence-weighted selection.
- **OUTPUT**: Final result, or `UNKNOWN` when evidence is insufficient.

This processing model is documented architecturally for L2_JA research and design exploration. It is not treated as a verified production implementation solely on the basis of structural documentation.
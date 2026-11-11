# Kanji Conversion Patterns

## Status
- **Epistemic status**: SOURCE_SUPPORTED for the general Mozc candidate-generation model; PROPOSED for L2_JA integration.
- **Implementation status**: Research layer only; not a proven runtime feature of this repository.

## 1. Candidate generation and ranking
- **Observed model**: Input reading is mapped to multiple candidate segmentations and kanji readings before final output.
- **AAM use**: This is treated as an architectural analogy for L2_JA candidate generation, not as a claim that the current repository includes a production-grade converter.
- **L2_JA alignment**: Candidate generation is a mechanism for preserving ambiguity until context is strong enough to reduce uncertainty.

## 2. Homophone and near-homophone resolution
- **Example pair**: 観測 (kansoku — measurement) vs 観客 (kankyaku — audience).
- **Architectural interpretation**: Contextual disambiguation should use surrounding text, domain metadata, and object/subject cues before selecting a final reading.
- **Evidence handling**: When context is insufficient, preserve `UNKNOWN` instead of converting to the most likely but unverified choice.

## 3. AAM constraints
- Do not equate the observed Mozc architecture with a fully implemented L2_JA converter.
- Preserve distinction between:
  - confirmed model structure;
  - inferred L2_JA adaptation;
  - unresolved research questions.

## 4. Repository note
This file is intentionally framed as a research extension to the existing Japanese kernel baseline rather than a verified production implementation.

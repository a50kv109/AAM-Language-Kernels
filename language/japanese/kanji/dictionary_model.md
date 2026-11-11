# Dictionary Model

## Status
- **Epistemic status**: SOURCE_SUPPORTED for the general storage approach; PROPOSED for repository integration.
- **Scope**: Research-oriented structural pattern, not a verified final dictionary implementation.

## 1. Hierarchical dictionary structure
- **Observed design**: A compressed dictionary can be organized as a layered tree with domain-level specialization.
- **AAM mapping**: General kanji -> domain vocabulary -> semantic or SOL mapping.
- **Project use**: This supports a structured lookup design for engineering Japanese, but it is not evidence that a complete dictionary engine exists in this repository.

## 2. Separation of lexical layers
- **System dictionary**: Broad, high-confidence lexical entries.
- **User/context dictionary**: Local terms, project-specific language, domain jargon.
- **Research layer**: Ambiguous or historically variant readings.

## 3. AAM integration
- The dictionary model is treated as a design scaffold for organizing lexical knowledge and resolving cross-domain terminology.
- It does not replace provenance discipline or source-backed evidence.

## 4. Repository note
This document contributes to the L2_JA knowledge model as a proposed structure. It is not treated as a fully validated lexical corpus.

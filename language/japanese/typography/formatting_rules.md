# Formatting Rules

## Status
- **Epistemic status**: RESEARCH_ONLY / SOURCE_SUPPORTED
- **Scope**: document-processing guidance for Japanese texts; not a guaranteed runtime implementation.

## 1. Kinsoku Shori (line-break restrictions)
- Kinsoku Shori describes line-breaking and punctuation restrictions used in Japanese typesetting.
- It is a valid document-processing layer concept, especially for extracted text and publishing workflows.
- It is not evidence that the project’s BOOK-NAV or any other runtime component already implements this behavior end-to-end.

## 2. Layout-sensitive parsing
- When a document is segmented or transformed, line break constraints may affect candidate reconstruction.
- This is useful for identifying split technical definitions, but it remains a future implementation concern unless explicitly implemented elsewhere.

## 3. AAM mapping
- This module is treated as a document-processing aid for the L3/L4 pipeline.
- It does not replace the rule that missing information should remain `UNKNOWN` when context is insufficient.

## 4. Repository note
These rules are retained as research-layer notes, preserving evidence discipline without pretending that the entire Japanese document-processing pipeline already exists.

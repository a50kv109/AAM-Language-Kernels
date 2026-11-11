# RESEARCH_CONTEXT_INTEGRATION_ASSESSMENT

## Scope

This assessment was created because the repository did not yet contain a completed `RESEARCH_CONTEXT_INTEGRATION_ASSESSMENT.md` file before the implementation step. The current repository state was therefore assessed directly from the working tree, Git metadata, and the supplied research context before any enrichment work began.

## A. Research understanding

The research aims to test whether a language kernel can retain more than linguistic wording when transferring knowledge between languages. The target is not simple translation, but the preservation of:

- linguistic meaning;
- cultural and historical context;
- conceptual relations;
- procedural knowledge;
- source provenance;
- interpretive boundaries between primary evidence and later reconstruction.

The Chinese historical mathematical tradition was selected as the first target domain because it contains a high density of algorithmic, positional, and procedural conventions that are easy to misstate when handled as mere textual summaries. The attached research notes explicitly treat earlier model output as unreliable when it confused quotations, modern explanations, and reconstructed procedures.

In practical terms, the repository's architecture states a similar objective: preserve semantic invariants across languages using AAM-V2, SOL tags, and AXIS-10. The gap is that the repo currently documents the framework more than it stores source-linked evidence.

## B. Pattern understanding

The five canonical patterns are not merely glossary terms. They are historical computational knowledge objects whose meaning depends on exact source language, exact wording, and a careful split between source text and analytical interpretation.

### ZH_PAT_001 — HESUAN_FRACTION_ADDITION

- Historical source: 《九章算术》, Chapter 1, 方田, item #17.
- Original passage: 「合分術曰：母互乘子，并以為實。母相乘為法。實如法而一。有分者通之。」
- Meaning: fraction addition via cross-multiplication of numerators and multiplication of denominators.
- Procedural significance: this is a direct algorithmic procedure for adding fractions.
- Critical correction: the character `副` is not part of the 合分術 passage. It belongs to a different procedure, 平分術, with `副併為平實`.
- Evidence boundary: the source passage is a primary-source candidate; the correction is a source-disambiguation requirement.
- Integration need: preserve the exact quote and explicitly separate the fraction-addition procedure from the parallel 平分術 operation.

### ZH_PAT_002A — SUNZI_POSITIONAL_ORIENTATION

- Historical source: 《孙子算经》, 卷上.
- Original passage: 「凡算之法：先識其位。一從十橫，百立千僵，千十相望，萬百相當。」
- Meaning: positional orientation of counting rods.
- Procedural significance: the text encodes spatial arrangement by place value.
- Critical correction: do not append the following phrase to this pattern: 「滿六已上，五在上方。六不積算，五不單張。」
- Evidence boundary: that phrase belongs to a different source context and must not be merged.
- Integration need: record the quote and its source boundary carefully, without conflating it with the later bi-quinary rule.

### ZH_PAT_002B — XIAHOU_BIQUINARY_CONSTRUCTION

- Historical source: 《夏侯阳算经》.
- Original passage: 「夫乘除之法，先明九九。一從十橫，百立千僵，千十相望，萬百相當。滿六已上，五在上方。六不積算，五不單張。」
- Meaning: a five-plus-units construction rule for values 6–9.
- Procedural significance: it explains how a five-component combines with lower units.
- Critical correction: the original text must remain distinct from the modern analytical interpretation that values 6–9 can be represented as a five-component plus 1–4.
- Evidence boundary: the textual passage establishes a historical statement; the physical graphical interpretation remains a modern reconstruction.
- Integration need: keep original quote, procedural interpretation, and modern formalization in separate fields.

### ZH_PAT_003 — HAIDAO_GEOMETRIC_SURVEYING

- Historical source: 《海岛算经》, first surveying problem.
- Meaning: a geometric surveying procedure employing two poles and two observation positions.
- Procedural significance: the method uses proportional and similarity relations.
- Critical correction: the observer moves backward 123 paces from the front pole and 127 paces from the rear pole; `五十五步` is a remainder in the island-height result, not the walking distance.
- Evidence boundary: modern formulas must not be silently treated as canonical historical content.
- Integration need: keep the historical procedure distinct from any modern mathematical formalization.

### ZH_PAT_005 — SUNZI_DIVISION_SHIFT

- Historical source: 《孙子算经》, 卷上.
- Original passage: 「凡除之法：與乘正異。乘得在中央，除得在上方。……上位有空絕者，法退二位。餘法皆如乘時……」
- Meaning: positional adjustment in division when empty places occur.
- Procedural significance: it describes a rule for shifting the divisor when a positional gap exists.
- Critical correction: the exact term is `上位`, not `頭位`.
- Evidence boundary: this is not a historical definition of zero; it is a positional rule in a procedural context.
- Integration need: preserve the original wording and separate it from modern interpretations of empty positional value.

### ZH_PAT_004 status

ZH_PAT_004 remains research-only. The attached research notes make it explicit that it is tied to 《数术记遗》 and to edition-specific textual variants, especially the 《四庫全書本》 witness. It must remain outside the canonical set until additional source verification is complete.

## C. Existing versus proposed architecture

The actual repository architecture is documentation-first and partially template-driven. Evidence from the working tree:

- [docs/ARCHITECTURE.md](/home/andrii/Общедоступные/AAM-Language-Kernels/docs/ARCHITECTURE.md) defines AAM-V2, SOL tags, and the AXIS-10 model.
- [MASTER_AXIS10_CONFIG.md](/home/andrii/Общедоступные/AAM-Language-Kernels/MASTER_AXIS10_CONFIG.md) specifies the SOL-tag and ESC framework.
- [docs/GLOSSARY.md](/home/andrii/Общедоступные/AAM-Language-Kernels/docs/GLOSSARY.md) contains a small CEV registry.
- The actual Chinese kernel contains passport, ground-truth matrix, and engineering-term files, but not a full research data layer.

The proposed architecture from the research notes adds five explicit layers:

- source provenance layer;
- procedural knowledge layer;
- cross-lingual semantic preservation layer;
- independent audit layer;
- learning-transfer benchmark layer.

Those layers are not yet implemented in the repository as structured artifacts. They are documented as design goals and are now being prepared for controlled integration.

## D. Schema compatibility

The proposed common pattern schema includes fields such as:

- pattern_id
- language
- historical_period
- source_title
- source_edition
- source_location
- original_text
- literal_translation
- semantic_explanation
- procedural_steps
- modern_formalization
- evidence_level
- textual_variants
- interpretation_notes
- unresolved_questions
- validation_status
- version_id

The current repo does not yet have a canonical pattern registry with this structure. It has a mostly narrative architecture and limited term matrices. Therefore the required path is additive extension, not schema replacement.

## E. Integration strategy

The minimal safe path is:

1. Preserve the existing Chinese passport and ground-truth files.
2. Add a canonical pattern registry under the Chinese kernel.
3. Keep provenance and interpretation as explicit fields.
4. Add version-aware audit metadata.
5. Keep ZH_PAT_004 in a research-only section.
6. Add a small validation script for schema consistency.

This is backward-compatible because it extends the current repository without replacing the core AXIS-10 documentation model.

## F. Validation strategy

Validation must distinguish historical truth from data consistency. Automated validation can confirm that:

- required fields are present;
- unique pattern IDs exist;
- evidence levels are set;
- source and interpretation fields remain separated;
- ZH_PAT_004 is not promoted;
- the five canonical patterns are present and distinct.

Automated tests cannot prove historical correctness; they can only prove that the repository stores the data consistently.

## G. Unresolved questions

The following items still require source research or owner decision:

- Which editions or textual witnesses are authoritative for each pattern?
- How much modern formalization should be stored as canonical knowledge versus analytic extension?
- Should future kernels also adopt the same additive schema?
- What is the minimum evidence threshold for promoting a research item into the canonical set?
- Should the repository remain a documentation-first framework or become a structured evidence dataset as well?

## H. Implementation roadmap

1. Prerequisite work: confirm the current Chinese schema and baseline.
2. Schema preparation: add a minimal, compatible pattern metadata schema.
3. Provenance integration: record exact source data and unresolved fields explicitly.
4. Pattern integration: add the five canonical records.
5. Validation and tests: script-based checks for consistency.
6. Documentation: update the Chinese passport and INDEX to reference the pattern registry.
7. Future cross-lingual experiments: only after the Chinese kernel is stable.

## Result

The repository is not yet in a fully implemented research-data state. It is a conceptual architecture with a base schema and a set of early language-kernel metadata files. The required next step is a disciplined enrichment of the Chinese kernel with source-aware, versioned pattern records while preserving the distinctions between original text, translation, explanation, procedure, formalization, and unresolved uncertainty.

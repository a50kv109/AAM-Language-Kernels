# Chinese Historical Pattern Registry

## Scope

This file records the initial canonical historical patterns for the Chinese kernel and keeps explicit separation between:

- original source text;
- source-text availability state;
- literal translation;
- semantic explanation;
- procedural description;
- modern formalization;
- interpretation notes;
- unresolved questions;
- provenance metadata.

This registry is intentionally minimal and backward-compatible with the existing Chinese kernel metadata.

## Canonical pattern set

### ZH_PAT_001 — HESUAN_FRACTION_ADDITION
- pattern_id: ZH_PAT_001
- language: zh
- historical_period: Han-era mathematical tradition
- source_title: 《九章算术》
- original_script_title: 《九章算术》
- chapter_or_volume: Chapter 1
- problem_or_section: 方田, item #17
- edition: not identified in the current repository
- textual_witness: not identified in the current repository
- source_location: Chapter 1, 方田, item #17
- source_reference: local repository note; exact edition or witness not yet recorded
- original_text: 「合分術曰：母互乘子，并以為實。母相乘為法。實如法而一。有分者通之。」
- source_text_status: original_source_text_available
- quotation_status: exact_quotation_available
- literal_translation: "The method of combining fractions says: multiply the denominators by each other and the numerators by the opposite denominator; sum the products into the numerator. Multiply the denominators together to form the divisor. The resulting numerator is divided by the resulting denominator. If there are fractions, first bring them to a common denominator."
- semantic_explanation: The passage describes the procedure for adding fractions by cross-multiplication and then dividing the resulting numerator by the resulting denominator.
- procedural_steps:
  1. Multiply each numerator by the opposite denominator.
  2. Sum the products to form the combined numerator.
  3. Multiply the denominators together to form the combined denominator.
  4. Divide the combined numerator by the combined denominator.
  5. If necessary, reduce the resulting fraction by common factors.
- modern_formalization: If a/b + c/d = (ad + bc) / bd, the procedure matches the canonical computational structure described by the source.
- evidence_level: VERIFIED_PRIMARY_SOURCE
- textual_variants: None recorded in the current repository notes.
- interpretation_notes: The character `副` does not belong in this passage. It belongs to the separate 平分術 procedure and must not be merged into 合分術.
- unresolved_questions: No direct page or edition witness is recorded in the current repository; exact witness metadata remains to be verified.
- validation_status: CANONICAL_REGISTERED
- version_id: 2026-11-11-v1

### ZH_PAT_002A — SUNZI_POSITIONAL_ORIENTATION
- pattern_id: ZH_PAT_002A
- language: zh
- historical_period: early Chinese computational tradition
- source_title: 《孙子算经》
- original_script_title: 《孙子算经》
- chapter_or_volume: 卷上
- problem_or_section: positional orientation of rod numerals
- edition: not identified in the current repository
- textual_witness: not identified in the current repository
- source_location: 卷上
- source_reference: local repository note; exact edition or witness not yet recorded
- original_text: 「凡算之法：先識其位。一從十橫，百立千僵，千十相望，萬百相當。」
- source_text_status: original_source_text_available
- quotation_status: exact_quotation_available
- literal_translation: "In the method of calculating, first understand the positions. One runs horizontally, ten stands upright, one hundred is set, one thousand is rigid; thousand and ten face each other, ten thousand and one hundred correspond."
- semantic_explanation: The text describes positional orientation and the layout of rod numerals by place value.
- procedural_steps:
  1. Identify the positional values in a rod numeral.
  2. Treat units, tens, hundreds, and thousands as spatially ordered positions.
  3. Maintain the relative orientation of digits according to the rule set.
- modern_formalization: The passage is best treated as a description of positional arrangement rather than as a complete formalized numeral system in modern terms.
- evidence_level: VERIFIED_PRIMARY_SOURCE
- textual_variants: The phrase 「滿六已上，五在上方。六不積算，五不單張。」 must not be attached to this pattern.
- interpretation_notes: The positional-orientation passage is distinct from the bi-quinary construction in ZH_PAT_002B.
- unresolved_questions: Exact witness detail and edition-specific wording remain to be verified.
- validation_status: CANONICAL_REGISTERED
- version_id: 2026-11-11-v1

### ZH_PAT_002B — XIAHOU_BIQUINARY_CONSTRUCTION
- pattern_id: ZH_PAT_002B
- language: zh
- historical_period: early Chinese computational tradition
- source_title: 《夏侯阳算经》
- original_script_title: 《夏侯阳算经》
- chapter_or_volume: not identified in the current repository
- problem_or_section: multiplication and division rule for values 6–9
- edition: not identified in the current repository
- textual_witness: not identified in the current repository
- source_location: unspecified in the current repository notes
- source_reference: local repository note; exact edition or witness not yet recorded
- original_text: 「夫乘除之法，先明九九。一從十橫，百立千僵，千十相望，萬百相當。滿六已上，五在上方。六不積算，五不單張。」
- source_text_status: original_source_text_available
- quotation_status: exact_quotation_available
- literal_translation: "In the method of multiplication and division, first clarify the nine-nine table. One runs horizontally; ten is vertical; one hundred stands; one thousand is upright; thousand and ten correspond; ten thousand and one hundred correspond. When the number is six or more, five is placed above; six is not piled as counting rods, and five is not used singly."
- semantic_explanation: The passage describes a five-plus-units construction principle in which values from 6 to 9 combine a five component with a lower unit component.
- procedural_steps:
  1. Recognize the base positional ordering.
  2. For values 6–9, use the five-component rule.
  3. Combine the five-unit with lower units representing 1–4.
  4. Keep the final mark arrangement consistent with the positional conventions.
- modern_formalization: A modern analytical interpretation may represent 6–9 as a five-component plus 1–4, but that remains an analytical model, not a direct historical proof of every physical detail of rod representation.
- evidence_level: VERIFIED_PRIMARY_SOURCE
- textual_variants: The passage is historically distinct from ZH_PAT_002A and must not be merged with it.
- interpretation_notes: The text establishes the historical rule; the exact physical rod-layout details are not proven by the quotation alone.
- unresolved_questions: The exact graphical form and all physical-implementation details remain under historical interpretation.
- validation_status: CANONICAL_REGISTERED
- version_id: 2026-11-11-v1

### ZH_PAT_003 — HAIDAO_GEOMETRIC_SURVEYING
- pattern_id: ZH_PAT_003
- language: zh
- historical_period: early Chinese mathematical problem tradition
- source_title: 《海岛算经》
- original_script_title: 《海岛算经》
- chapter_or_volume: first surveying problem
- problem_or_section: island-height / surveying problem
- edition: not identified in the current repository
- textual_witness: not identified in the current repository
- source_location: first surveying problem
- source_reference: local repository note; exact witness not yet recorded in the repository
- original_text: ""
- source_text_status: original_source_text_unavailable
- quotation_status: quotation_awaiting_verification
- literal_translation: "The surviving repository record indicates a surveying method using two poles and the observer's position to derive a height or distance by proportional reasoning."
- semantic_explanation: The problem uses two poles and two observation positions to determine height or distance by proportional reasoning.
- procedural_steps:
  1. Establish pole positions and observer positions.
  2. Record the backward distances from the front pole and rear pole.
  3. Use geometric similarity and proportional reasoning to derive the target quantity.
  4. Treat the final remainder as a remainder, not as the walk distance.
- modern_formalization: A modern formula may be generated as a reconstruction, but it must be explicitly marked as a reconstruction and checked against the actual variable definitions of the original problem.
- evidence_level: VERIFIED_WITH_COMMENTARY
- textual_variants: The exact original text for the problem is not yet stored in the current repo as a verified witness; the quantities 123, 127 and 五十五步 are historically significant but not source-linked in the current repository.
- interpretation_notes: The observer moves backward 123 paces from the front pole and 127 paces from the rear pole. The phrase `五十五步` is a remainder in the island-height result, not the observer's walking distance.
- unresolved_questions: Exact source witness, edition detail, and variable definitions require further verification before a formal canonical formula can be treated as fixed.
- validation_status: CANONICAL_REGISTERED
- status_recommendation: keep as canonical only while source witness remains unresolved; if no primary quote is recovered, this record should be demoted to RESEARCH_ONLY and excluded from canonical validation
- version_id: 2026-11-11-v1

### ZH_PAT_005 — SUNZI_DIVISION_SHIFT
- pattern_id: ZH_PAT_005
- language: zh
- historical_period: early Chinese computational tradition
- source_title: 《孙子算经》
- original_script_title: 《孙子算经》
- chapter_or_volume: 卷上
- problem_or_section: division procedure
- edition: not identified in the current repository
- textual_witness: not identified in the current repository
- source_location: 卷上
- source_reference: local repository note; exact edition or witness not yet recorded
- original_text: 「凡除之法：與乘正異。乘得在中央，除得在上方。……上位有空絕者，法退二位。餘法皆如乘時……」
- source_text_status: original_source_text_available
- quotation_status: exact_quotation_available
- literal_translation: "In the method of division, it differs fundamentally from multiplication. What is obtained in multiplication sits in the center; in division it stands in the upper position. If there is an empty gap in the upper position, move the divisor back by two places; the remaining rules are the same as in multiplication."
- semantic_explanation: The passage defines a positional adjustment rule during division under empty-position conditions.
- procedural_steps:
  1. Distinguish division from multiplication.
  2. Place the result according to its positional role.
  3. If the upper position contains an empty gap, shift the divisor by two places.
  4. Continue according to the ordinary multiplication-like procedure.
- modern_formalization: Modern discussions of zero or empty positions should not transform this passage into a formal definition of zero. The source is a procedural statement, not a mathematical definition.
- evidence_level: VERIFIED_PRIMARY_SOURCE
- textual_variants: The exact phrase is `上位`, not `頭位`.
- interpretation_notes: `上位有空絕者，法退二位` is a positional operation within a division procedure; it is not a formal historical definition of zero.
- unresolved_questions: The precise interpretation of “空絕” remains open to scholarly analysis and must not be treated as settled by one modern explanation.
- validation_status: CANONICAL_REGISTERED
- version_id: 2026-11-11-v1

## Research-only records

### ZH_PAT_004 — RESEARCH_ONLY
- pattern_id: ZH_PAT_004
- language: zh
- historical_period: research layer only
- source_title: 《数术记遗》
- original_script_title: 《数术记遗》
- chapter_or_volume: not identified in the current repository
- problem_or_section: edition-specific computational methods and witness comparison
- edition: multiple textual witnesses; the repository currently does not preserve a fully verified canonical edition mapping
- textual_witness: not identified in the current repository; witness-specific values remain under research review
- source_location: fourteen computational methods; edition-specific classification remains unresolved
- source_reference: local repository note; no canonical edition mapping has been accepted yet
- original_text: ""
- source_text_status: original_source_text_unavailable
- quotation_status: quotation_awaiting_verification
- literal_translation: Not yet stabilized.
- semantic_explanation: The field concerns methodological enumeration and classification of computational methods across textual witnesses, especially the 《四庫全書本》 witness.
- procedural_steps: Not yet stabilized; keep separate from the canonical pattern set.
- modern_formalization: Modern functional classification is not to be treated as the author's original classification.
- evidence_level: HISTORICAL_RECONSTRUCTION
- textual_variants: 太乙, 太一, 了知, 計算, 心算, etc. must be preserved as witness-specific data, not merged silently.
- interpretation_notes: This pattern is intentionally excluded from the canonical registry and remains in the research layer pending further verification.
- unresolved_questions: Which editions, witnesses, and classifications are authoritative remains unresolved.
- validation_status: RESEARCH_ONLY
- version_id: 2026-11-11-v1

## Source provenance model

The registry now distinguishes the following source states:

- original_source_text_available
- original_source_text_unavailable
- quotation_partially_available
- quotation_awaiting_verification

These states are intentionally separate from validation status. A record may be structurally valid while its quotation remains unavailable.

## Minimal audit record model

The repository should keep a minimal audit template, not a full audit application:

- audit_id: <generated by a future auditor>
- pattern_id: <pattern identifier>
- target_version_id: <exact version being reviewed>
- reviewed_revision: <git revision or file hash>
- reviewer: <name or institution of the independent reviewer>
- audit_date: <ISO date>
- source_basis: <specific source witness or repository note>
- findings: <primary concerns>
- corrections: <changes applied>
- review_status: <accepted | accepted_with_limitations | rejected>

This model is a placeholder until an independent reviewer assigns an actual record. It is not a historical audit record itself.

## Schema compatibility note

The pattern schema in this file is intentionally compatible with the proposed common pattern fields while preserving the repository's current documentation-first structure. The main addition is the explicit evidence-level and interpretation boundary between historical wording, source availability, and modern analysis.

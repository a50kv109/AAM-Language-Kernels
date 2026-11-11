# Italian Kernel Pattern Registry

## Scope

This file records the initial Italian kernel patterns currently represented in the repository. The registry intentionally preserves the distinction between:

- verified linguistic facts;
- source-backed examples;
- interpretations;
- provisional models;
- unresolved questions;
- modern documentary description.

This is a documentation-first, evidence-aware registry for the Italian kernel and is not a benchmarked corpus validator or parser.

## Canonical pattern set

### IT_PAT_001 — ALLEGRO_TEMPO_MARKER
- pattern_id: IT_PAT_001
- language: it
- domain: music_performance
- source_record: Western classical score directions; illustrative not yet tied to a single verified score excerpt
- original_text: Allegro
- source_text_status: quotation_awaiting_verification
- quotation_status: quotation_awaiting_verification
- literal_translation: cheerful / lively
- semantic_explanation: A qualitative tempo marking indicating a lively or fast character without encoding an exact BPM value.
- procedural_steps:
  1. Preserve the original Italian form.
  2. Record the conventional musical function separately from the literal gloss.
  3. Do not infer a precise metronome value from the term alone.
- modern_formalization: The term is treated as a tempo-character label within a qualitative score lexicon.
- evidence_level: MODERN_INTERPRETATION
- textual_variants: The same basic term may appear in multiple editorial styles, but no corpus verification has been recorded in this repository.
- interpretation_notes: The literal sense and the conventional musical function are distinct.
- unresolved_questions: No verified score excerpt or edition provenance has been added to the repository yet.
- validation_status: INITIAL
- version_id: 2026-11-11-v1

### IT_PAT_002 — ADAGIO_SLOW_TEMPO
- pattern_id: IT_PAT_002
- language: it
- domain: music_performance
- source_record: Western classical score directions; illustrative not yet tied to a single verified score excerpt
- original_text: Adagio
- source_text_status: quotation_awaiting_verification
- quotation_status: quotation_awaiting_verification
- literal_translation: at ease / unhurried
- semantic_explanation: A tempo adjective or adverb indicating a slow, measured character.
- procedural_steps:
  1. Preserve the original lexical form.
  2. Distinguish tempo meaning from expressive nuance in context.
  3. Treat performance decisions as context-dependent rather than mechanically encoded.
- modern_formalization: Adagio is treated as a qualitative tempo descriptor rather than a fixed numerical tempo.
- evidence_level: MODERN_INTERPRETATION
- textual_variants: Variants such as adagio sostenuto may imply additional nuance but are not a separate validated corpus entry here.
- interpretation_notes: There is no measured BPM value in the record; the signaled effect is qualitative and contextual.
- unresolved_questions: Exact performance interpretation remains editorial and context dependent.
- validation_status: INITIAL
- version_id: 2026-11-11-v1

### IT_PAT_003 — CRESCENDO_DYNAMIC_INCREASE
- pattern_id: IT_PAT_003
- language: it
- domain: music_performance
- source_record: Italian dynamic and expression vocabulary from score notation practice
- original_text: Crescendo
- source_text_status: quotation_awaiting_verification
- quotation_status: quotation_awaiting_verification
- literal_translation: growing
- semantic_explanation: Indicates a gradual increase in dynamic intensity over time.
- procedural_steps:
  1. Recognize the term as a dynamic process rather than a single dynamic level.
  2. Keep the change over time distinct from the target dynamic level.
  3. Apply the effect in relation to surrounding directions and instrument context.
- modern_formalization: Dynamic level and dynamic transition are represented as separate semantic dimensions.
- evidence_level: MODERN_INTERPRETATION
- textual_variants: Crescendo and diminuendo are complementary process markers in the same score-language family.
- interpretation_notes: The term denotes a change in intensity, not a fixed loudness value.
- unresolved_questions: No complete corpus of authentic excerpts has been added to the repository yet.
- validation_status: INITIAL
- version_id: 2026-11-11-v1

### IT_PAT_004 — LEGATO_STACCATO_ARTICULATION
- pattern_id: IT_PAT_004
- language: it
- domain: music_performance
- source_record: Italian articulation vocabulary used in performance directions
- original_text: Legato / Staccato
- source_text_status: quotation_awaiting_verification
- quotation_status: quotation_awaiting_verification
- literal_translation: bound / detached
- semantic_explanation: Articulation terms describing how notes should be connected or separated in execution.
- procedural_steps:
  1. Preserve the original performance vocabulary.
  2. Distinguish articulation from dynamics and tempo.
  3. Treat context and notation as decisive for precise execution.
- modern_formalization: These terms describe articulation textures and are not directly equivalent to a single acoustic measurement.
- evidence_level: MODERN_INTERPRETATION
- textual_variants: The repertoire includes related terms such as tenuto, marcato, and portato, but they are not yet separated into a full validated matrix.
- interpretation_notes: Articulation is a musically conventional interpretive layer, not a literal physical measurement.
- unresolved_questions: Authentic score excerpts and historical editorial conventions remain to be collected.
- validation_status: INITIAL
- version_id: 2026-11-11-v1

### IT_PAT_005 — PIU_MENO_COMPARATIVE_MODIFIERS
- pattern_id: IT_PAT_005
- language: it
- domain: music_performance
- source_record: Comparative and degree operators used in standard Italian musical directions
- original_text: Più / Meno / Molto / Poco
- source_text_status: quotation_awaiting_verification
- quotation_status: quotation_awaiting_verification
- literal_translation: more / less / very / little
- semantic_explanation: Degree and comparative operators modify tempo, expression, or dynamic character in context-dependent ways.
- procedural_steps:
  1. Read the comparative operator first.
  2. Identify the head term it modifies.
  3. Preserve the conventional usage without converting to a fixed numerical value.
- modern_formalization: These modifiers are modeled as contextual operators rather than rigid scalar instructions.
- evidence_level: MODERN_INTERPRETATION
- textual_variants: Expressions such as più mosso, meno mosso, molto allegro, and poco ritardando are typical but not yet benchmarked against a corpus.
- interpretation_notes: The meaning depends on the target domain and surrounding score indications.
- unresolved_questions: A curated score corpus is required before a broader comparative grammar can be treated as canonical.
- validation_status: INITIAL
- version_id: 2026-11-11-v1

## Notes on evidence and status

The current Italian music layer is intentionally limited to a curated starting corpus with explicit uncertainty. It is documentation-led rather than benchmark-led.

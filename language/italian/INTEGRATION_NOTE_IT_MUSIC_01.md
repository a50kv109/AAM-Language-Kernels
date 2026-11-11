# Italian Kernel Integration Note — IT-MUSIC-01

## Change scope

This update enriches the existing `language/italian/` kernel. It does not introduce a duplicate Italian kernel and does not alter repository-wide AXIS-10 rules.

## Added

- `music/INDEX.md`: navigation and scope boundary for the music-language layer.
- `music/musical_grammar_patterns.md`: an initial set of Italian constructions used in score directions.
- `music/musical_vocabulary.md`: a starter vocabulary with literal glosses and contextual cautions.

## Corrected

- The Italian `INDEX.md` links now point to the engineering files that actually exist.
- Claims of full readiness were removed. The language kernel remains INITIALIZING.
- Passport metrics are explicitly NOT MEASURED; architectural targets are not presented as benchmark results.
- Two minor mixed-language/typo issues in the engineering term files were corrected.

## Epistemic boundary

The music corpus is illustrative and has not yet been validated against a documented collection of authentic score excerpts. It does not implement a parser, OCR, notation recognition or performance decision system. Ambiguous abbreviations (for example, `rit.`) must remain unresolved until context supports an interpretation.

## Suggested next validation

Build a small evidence pack of score excerpts with edition/page provenance, multiple composers/periods, reviewed glosses and explicit ambiguity labels. Only after that should benchmark metrics be calculated.

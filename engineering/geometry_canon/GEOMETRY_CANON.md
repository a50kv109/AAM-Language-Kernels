# AAM Engineering Geometry Canon

**Version:** 1.0.0
**Status:** Initial candidate; canonical definitions are proposed for review.
**Language mappings:** Proposed, not independently linguistically validated.
**Geometry Skill execution:** Not run for this integration.

## Purpose and boundary

This catalog gives the language kernels shared, language-independent identifiers for a small planar-geometry vocabulary. It is an ontology and semantic-mapping layer, not a language parser, geometry engine, or proof system. Existing AXIS-10/AAM structures remain unchanged.

The canonical records are in [`geometry_concepts.yaml`](./geometry_concepts.yaml). It uses JSON syntax, a dependency-free subset of YAML 1.2, so the repository validator can check it using Python's standard library.

The model preserves the Geometry Skill's key distinction:

`OBJECT != RELATION != PROPERTY != RULE`

In particular:

- `ENT_CIRCLE_BOUNDARY` is a one-dimensional boundary; `ENT_DISK` is a two-dimensional filled region.
- `ENT_LINE` is unbounded; `ENT_SEGMENT` is bounded.
- `ENT_ANGLE` is a geometric configuration. Its scalar measure is a separate property. It is not an extrinsic polar angle.
- `ENT_SIDE` is a polygon-context role of a segment; it is not globally synonymous with a circle chord.
- `REL_PARALLEL`, `REL_PERPENDICULAR`, and `REL_INTERSECTION` are relations, not objects.
- `ENT_RADIUS` is a segment; its length is a scalar. `ENT_DIAMETER` is a constrained segment, not a runtime-verified predicate by implication.

## Source and epistemic status

Definitions and skill capability labels distinguish declarative specifications from executable support. The Geometry Skill's Packages 01–03 are specifications, while its capability model and semantic interface describe a separate runtime boundary. Capability labels in this repository are documentary classifications only; they are not results of running the Skill. Benchmark fixture terms and expected intents are `HYPOTHESIS`; they are not `TOOL-VERIFIED` results.

Package 02 supplies the circle-structure relations and the contextual Side/Chord boundary; it does not define `Parallel`, `Perpendicular`, or `Intersection`. Those three canonical records are AAM extensions whose documented execution capabilities are recorded separately.

Language mapping records preserve candidate native-script terms and their status. Every mapping currently has `translation_validation_status: NOT_VERIFIED`; no source-based linguistic review is claimed. Empty grammatical-form and transliteration fields mean that data has not been supplied. The cited training scenarios T01–T10 were reviewed as references, but were neither imported nor executed.

## Integration model

Each language's Engineering Axis contains a short navigation record linking to its language mapping. The single canonical definition remains in this shared catalog; language-specific files do not redefine geometry.

The mapping files are at [`language_mappings/`](./language_mappings/). Candidate utterances and expected semantic-intent fixtures are in [`benchmark/cross_language_benchmark.yaml`](./benchmark/cross_language_benchmark.yaml).

## Benchmark status

The benchmark intentionally separates:

1. **Fixture parity** — each language has a candidate utterance associated with one expected command shape.
2. **Linguistic validation** — not performed.
3. **Geometry Skill execution** — not performed.
4. **Geometric verification** — not performed in this repository.

The fixtures are not claims that the Skill recognizes the utterances in all languages. The bundled Natural Language Adapter source documents patterns for Russian and English only, and the Geometry Skill remains the deterministic execution/verification boundary.

See [`validation_report.md`](./validation_report.md) for what the local validator does and does not establish.

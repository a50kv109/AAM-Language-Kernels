# Context and Ambiguity Policy

**Status:** PROPOSED policy; contextual inference is not implemented.

- Preserve multiple readings when a source-backed record supports them.
- Do not infer an omitted subject, object, root, or causal link without contextual evidence.
- If supplied evidence cannot resolve a form, return `UNKNOWN`.
- Do not treat AAM-reported metrics or the most frequent guess as linguistic proof.
- Record conflicting readings as a visible conflict for review rather than silently voting between them.

This policy applies `ENGINEERED_IGNORANCE` to the research record. The current core does not perform contextual resolution.

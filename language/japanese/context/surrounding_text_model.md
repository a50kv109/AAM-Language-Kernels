# Surrounding Text Model

## Status
- **Epistemic status**: SOURCE_SUPPORTED for the idea of context-sensitive rewriting; PROPOSED for the AAM integration.
- **Implementation status**: Architectural research pattern; not a confirmed runtime module in this repository.

## 1. Context-sensitive disambiguation
- **Observed pattern**: A system can use preceding text to adjust conversion probabilities and reduce ambiguity.
- **AAM adaptation**: The L4 context layer may use surrounding text as support for subject resolution and term disambiguation.

## 2. Engineered ignorance rule
- If the surrounding context is insufficient, preserve ambiguity and return `UNKNOWN`.
- Do not convert a missing subject or omitted actor into an invented one.
- This rule remains a core constraint of `ENGINEERED_IGNORANCE`.

## 3. Practical interpretation
- **Example**: If text includes a strong subject frame such as `システムが`, the system may rank action-like continuations higher.
- **But**: absent disambiguating cues, multiple interpretations remain plausible and the system should not force a single answer.

## 4. Repository note
This file formalizes a useful research pattern for L4 reasoning, but it is not treated as a verified implementation of a surrounding-text rewriter.

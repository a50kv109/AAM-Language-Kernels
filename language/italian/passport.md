# Italian Language Kernel Passport — IT:13

## Identity

- **Language:** Italiano (Italian)
- **Locale:** it-IT
- **ISO 639-1:** it
- **Core ID:** IT:13
- **Role:** Semantic Gateway
- **Architecture reference:** AAM-V2 / AXIS-10
- **Operational status:** INITIALIZING

## Purpose

The Italian kernel represents Italian lexical, grammatical and contextual meaning for cross-lingual semantic work. It is a language gateway, not an engineering or music-performance executor.

## AXIS-10 CONFIGURATION (Translation & Interpretation Axis)

### Engineering Semantic Compiler (ESC) Status
- **Protocol:** AAM-V2_ARTSYBASHEV
- **Master Config:** [MASTER_AXIS10_CONFIG.md](../../MASTER_AXIS10_CONFIG.md)
- **ESC Enabled:** ✅ YES
- **Validation Level:** DOCUMENTATION + STRUCTURAL REGISTRY CHECKS (not a benchmarked production engine)

### SOL-Tag Implementation
- **Source Tags:** ✅ Implemented at the domain-terminology layer
- **Constraint Tags:** ✅ Implemented in the semantic framing notes
- **Dissipate Tags:** ✅ Implemented where causal/process semantics are relevant
- **Domain:** IT:13 (Italian semantic gateway)

### Integrity Score Target
- **Target IS:** ≥ 0.90 (architectural target only)
- **Current IS:** NOT MEASURED
- **Status:** ⚠️ IN_PROGRESS

### TDI (Tensor Divergence Index) Monitoring
- **Monitoring Enabled:** ✅ DOCUMENTED
- **Threshold:** ≤ 0.35 (architectural target only)
- **Current TDI:** NOT MEASURED
- **Last Measurement:** NOT MEASURED

### Standard Equivalence Vectors (CEV)
- **ISO Standards:** ✅ Referenced at the kernel level
- **DIN Standards:** ✅ Referenced at the engineering domain layer
- **GB Standards:** ✅ Referenced where applicable
- **GOST Standards:** ✅ Referenced where applicable
- **Master Glossary Reference:** [ground_truth_matrix.md](ground_truth_matrix.md)

### ESC Verification Status
- **Physical Causality Check:** ⚠️ LIMITED TO DOCUMENTED TYPOLOGY
- **Semantic Fidelity:** NOT BENCHMARKED
- **Standard Alignment:** PARTIAL / DOCUMENTATION-ONLY
- **Last ESC Run:** NOT RECORDED
- **Next ESC Audit:** REQUIRED AFTER CURATED EVIDENCE PACK IS ADDED

### Compliance Statement
This kernel conforms to the repository's documentation-first architecture and keeps evidence boundaries explicit. It is suitable for controlled terminology and music-language documentation, but it does not claim benchmarked performance or a complete production validation suite.

## AXIS-10 alignment

- [Master AXIS-10 configuration](../../MASTER_AXIS10_CONFIG.md)
- [Semantic governance](../../SEMANTIC_GOVERNANCE.md)
- [Architecture overview](../../docs/ARCHITECTURE.md)
- [Italian pattern registry](./pattern_registry.md)
- [Italian validation script](./validate_italian_kernel.py)

SOL tags (SOURCE, CONSTRAINT, DISSIPATE) may describe causal or process semantics where appropriate. They are not mandatory labels for every ordinary grammatical construction.

## Domain coverage

| Domain | Coverage | Evidence status |
|---|---|---|
| General Italian grammar | Introductory reference only | Not benchmarked |
| Technical terminology | Small curated list | Not independently audited |
| Medical terminology | Small curated list | Not independently audited |
| Specialized/industrial terminology | Small curated list | Not independently audited |
| Musical Italian | Initial pattern corpus | Not validated against a score corpus |

## Integrity and divergence metrics

- **Target Integrity Score:** architectural target only; not measured.
- **Current Integrity Score:** NOT MEASURED
- **TDI:** NOT MEASURED
- **Validation status:** INITIALIZING

No numeric quality score is claimed until a reproducible benchmark and reference annotations exist.

## Scope boundary

The kernel may identify and explain linguistic forms, register, ambiguity and domain-specific instructions. It must preserve uncertainty in damaged or ambiguous source text. Reconstruction of a score, physical interpretation, performance decisions and engineering calculations remain outside this language kernel.

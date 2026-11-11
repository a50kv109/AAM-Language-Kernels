# AAM-V2 Architecture Overview

**Version:** 2.0 (AAM-V2_ARTSYBASHEV)  
**Status:** DOCUMENTED BASELINE  
**Last Updated:** 2026-11-11

---

## 🏗️ Architectural Principles

The repository continues to operate under the **AAM-V2 (Advanced Analytical Model - Version 2)** framing: **AXIS-10 (Translation & Interpretation Axis)** remains the architectural specification, while the repository itself is primarily a documentation-first and metadata-driven library of language kernels rather than a single executable runtime.

This document reflects the current `main` branch, not the earliest template assumptions. In practice, every language directory contains its own combination of `INDEX.md`, `passport.md`, `ground_truth_matrix.md`, engineering glossaries, and, where relevant, specialist modules such as the Italian music layer.

### Current design pattern

```
Language kernel directory
  ├─ INDEX.md                # navigation and scope
  ├─ passport.md             # metadata + AXIS-10 declaration
  ├─ ground_truth_matrix.md  # domain mapping / SOL references
  ├─ engineering/*.md       # terms by engineering axis
  ├─ pattern_registry.md     # controlled pattern records (where applicable)
  ├─ validate_*.py          # repository-level validation scripts
  └─ additional domain modules (e.g. italian/music/)
```

---

## 📦 Repository Structure (actual state on main)

The repository does not currently contain a uniform `logic/` and `data/` sub-structure under every kernel. The actual repository layout is closer to the following:

```
AAM-Language-Kernels/
├── docs/
│   ├── ARCHITECTURE.md
│   ├── AXIS10_GUIDE.md
│   └── GLOSSARY.md
│
├── language/
│   ├── master/
│   │   ├── AXIS10_FULL_TEMPLATE.md
│   │   └── kernel_template/
│   │       └── passport.md
│   │
│   ├── english/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   └── ground_truth_matrix.md
│   │
│   ├── french/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── ground_truth_matrix.md
│   │   └── engineering/
│   │
│   ├── chinese/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── pattern_registry.md
│   │   ├── ground_truth_matrix.md
│   │   ├── validate_patterns.py
│   │   └── engineering/
│   │
│   ├── german/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── ground_truth_matrix.md
│   │   └── engineering/
│   │
│   ├── russian/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── ground_truth_matrix.md
│   │   └── engineering/
│   │
│   ├── ukrainian/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── ground_truth_matrix.md
│   │   └── engineering/
│   │
│   ├── italian/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── pattern_registry.md
│   │   ├── ground_truth_matrix.md
│   │   ├── validate_italian_kernel.py
│   │   ├── INTEGRATION_NOTE_IT_MUSIC_01.md
│   │   ├── music/
│   │   └── engineering/
│   │
│   ├── norwegian/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── ground_truth_matrix.md
│   │   └── engineering/
│   │
│   ├── georgian/
│   │   ├── INDEX.md
│   │   ├── passport.md
│   │   ├── ground_truth_matrix.md
│   │   └── engineering/
│   │
│   └── sanskrit/
│       ├── INDEX.md
│       ├── passport.md
│       ├── ground_truth_matrix.md
│       └── engineering/
│
├── README.md
├── LICENSE
├── MASTER_AXIS10_CONFIG.md
├── SEMANTIC_GOVERNANCE.md
├── SYSTEM_INTEGRATION_REPORT.md
├── RESEARCH_CONTEXT_INTEGRATION_ASSESSMENT.md
└── Master_Kernel_Template.md
```

### Important note
The earlier repository tree describing a uniform `docs/`, `logic/`, and `data/` sub-layout under each language kernel is a template-era description, not the actual layout of the current repository. The current repo is a patchwork of language-specific metadata, engineering terminology, validators, and research layers.

---

## 🧠 AXIS-10, SOL, and ESC in the current repository

The architecture still centers on the following ideas:

- **AXIS-10** remains the governing framework for the repository.
- **SOL tags** are treated as semantic markers for source/constraint/dissipate-style analysis.
- **ESC** is described as the engineering semantic compiler path, but the repository does not presently validate every kernel at the same maturity level.
- **IS** and **TDI** are documented as targets and monitoring concepts, but the current file set does not establish a uniform, measured repository-wide benchmark.

### Evidence from the repository
- `MASTER_AXIS10_CONFIG.md` contains the master configuration specification.
- `language/master/AXIS10_FULL_TEMPLATE.md` provides the template structure for new kernels.
- `passport.md` files contain AXIS-10 declarations and status markers.
- Several kernels include `ground_truth_matrix.md` and engineering vocabularies under `engineering/`.
- Chinese and Italian kernels additionally include `pattern_registry.md` and validation scripts.

### What should not be inferred
The presence of the architectural specification does not prove that all kernels are fully measured, certified, or production-ready. The repository contains explicit `IN_PROGRESS`, `INITIALIZING`, and `NOT MEASURED` declarations in its own passport files.

---

## 📚 Current language kernel inventory

The following directories are present in the repository on `main` and are referenced by the project documentation. Their status is taken from each kernel's own `INDEX.md` and `passport.md` files; it is not normalized into a single global rating.

| Language | Directory | Evidence in repo | Status as documented |
|----------|-----------|------------------|---------------------|
| English | `language/english` | `INDEX.md`, `passport.md`, `ground_truth_matrix.md` | `Current IS: 0.00` / `⚠️ IN_PROGRESS` |
| French | `language/french` | `INDEX.md`, `passport.md`, `ground_truth_matrix.md`, `engineering/` | `Current IS: 0.00` / `⚠️ INITIALIZING_AXIS10` |
| Chinese | `language/chinese` | `INDEX.md`, `passport.md`, `pattern_registry.md`, `validate_patterns.py` | `⚠️ INITIALIZING_AXIS10`; canonical pattern set separated from research-only records |
| German | `language/german` | `INDEX.md`, `passport.md`, `ground_truth_matrix.md`, `engineering/` | `Current IS: 0.00` / `⚠️ INITIALIZING_AXIS10` |
| Russian | `language/russian` | `INDEX.md`, `passport.md`, `ground_truth_matrix.md`, `engineering/` | `Current IS: 0.00` / `⚠️ INITIALIZING_AXIS10` |
| Ukrainian | `language/ukrainian` | `INDEX.md`, `passport.md`, `ground_truth_matrix.md`, `engineering/` | `Current IS: 0.00` / `⚠️ INITIALIZING_AXIS10` |
| Italian | `language/italian` | `INDEX.md`, `passport.md`, `pattern_registry.md`, `validate_italian_kernel.py`, `music/` | `INITIALIZING` — documented baseline, not a validated full language engine |
| Norwegian | `language/norwegian` | `passport.md`, `ground_truth_matrix.md`, `engineering/` | `AXIS-10 ARCHITECTURE READY`; axes listed as `VALIDATED` / `READY` |
| Georgian | `language/georgian` | `passport.md`, `ground_truth_matrix.md`, `engineering/` | `✅ AXIS-10 ARCHITECTURE READY` |
| Sanskrit | `language/sanskrit` | `INDEX.md`, `passport.md`, `ground_truth_matrix.md` | `AXIS-10 Architecture: READY`; role as semantic gateway |

This table is intentionally factual and conservative: it records the repository's own declared state rather than baking in a single normalized project-wide readiness claim.

---

## 🔄 Current development workflow

The repository reflects a real-world workflow, not an automatic build pipeline:

1. Study the master template and the master AXIS-10 specification.
2. Create or extend a language directory and its metadata files.
3. Add domain grounding, terminology, and source/provenance notes.
4. Register controlled patterns or equivalence references where available.
5. Run the validator or validation script for the kernel when present.
6. Keep provenance and status metadata explicit.
7. Create a feature branch and open a PR for review.
8. Merge into `main` after review and validation.
9. Maintain the stable repository baseline.

This sequence is consistent with the repository's actual state and with the project’s documented engineering process.

---

## 📚 Key documents and tool relationship

| Document / project | Role | Notes |
|--------------------|------|-------|
| `MASTER_AXIS10_CONFIG.md` | Core AXIS-10 specification | Source of the architectural rules and tags |
| `language/master/AXIS10_FULL_TEMPLATE.md` | Master template | Defines the expected kernel structure |
| `docs/AXIS10_GUIDE.md` | User-facing guide | Operational guidance for implementation |
| `docs/GLOSSARY.md` | Central glossary | Repository-level terminology reference |
| `Master_Kernel_Template.md` | Template reference | Describes the project's kernel construction conventions |
| `AAM-Language-Kernel-Builder` | Supporting tool | Companion repository for restructuring, module assembly, and export-oriented workflows |

### Relationship between the two repositories

**AAM-Language-Kernels**
- Main repository of language kernels, structured knowledge, documentation, and research records.

**AAM-Language-Kernel-Builder**
- Supporting tool repository used for experiments, modular assembly, and export-oriented processing of language-kernel structures.

The builder is therefore an architectural support project, not proof that every kernel in `AAM-Language-Kernels` was automatically generated by the builder.

**Builder project:** [AAM-Language-Kernel-Builder](https://github.com/a50kv109/AAM-Language-Kernel-Builder)

---

## 🎯 Implementation Status Summary

| Component | Status | Evidence |
|-----------|--------|----------|
| Repository baseline | ✅ STRUCTURED | `README.md`, `docs/`, `language/` |
| AXIS-10 master specification | ✅ DEFINED | `MASTER_AXIS10_CONFIG.md` |
| Master kernel template | ✅ DEFINED | `language/master/AXIS10_FULL_TEMPLATE.md` |
| English kernel | ⚠️ IN_PROGRESS | `language/english/passport.md` |
| French kernel | ⚠️ INITIALIZING_AXIS10 | `language/french/passport.md` |
| Chinese kernel | ⚠️ INITIALIZING_AXIS10 | `language/chinese/passport.md` and `pattern_registry.md` |
| German kernel | ⚠️ INITIALIZING_AXIS10 | `language/german/passport.md` |
| Russian kernel | ⚠️ INITIALIZING_AXIS10 | `language/russian/passport.md` |
| Ukrainian kernel | ⚠️ INITIALIZING_AXIS10 | `language/ukrainian/passport.md` |
| Italian kernel | ⚠️ INITIALIZING | `language/italian/INDEX.md` and `passport.md` |
| Norwegian kernel | ✅ ARCHITECTURE READY | `language/norwegian/passport.md` |
| Georgian kernel | ✅ ARCHITECTURE READY | `language/georgian/passport.md` |
| Sanskrit kernel | ✅ READY | `language/sanskrit/passport.md` |

This summary deliberately distinguishes between:
- architecture definition,
- structured repository state,
- per-kernel implementation status,
- and measured performance claims.

---

## ⚠️ Explicit limitations of the current repository

The current repository should not be read as a fully benchmarked, uniform language-engine platform. The architecture and templates are present, but the actual kernel implementations remain uneven in maturity. In particular:

- `Current IS` values are often `0.00` or not measured.
- `TDI` is documented but not consistently measured across all kernels.
- Some passports declare `READY` or `ARCHITECTURE READY` while other files list the same kernel as `INITIALIZING` or `IN_PROGRESS`.
- The repo contains a mix of standardized documentation, research-only records, and structured but still incomplete kernel materials.
- The `Chinese` and `Italian` kernels are more explicit about provenance boundaries and research-only status than the older template-era documentation suggests.

The right reading of the repo is therefore: a structured but evolving research and documentation platform, not a single finalised semantic engine.

---

**Maintenance:** Repository architecture and documentation  
**Review Cycle:** ongoing  
**Next Milestone:** keep the architecture document aligned with the state of `main` and separate specification from measured implementation.

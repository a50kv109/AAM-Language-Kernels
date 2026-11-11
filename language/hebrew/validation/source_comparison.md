# Hebrew Source Package Comparison

## Inventory and package checksums

| Source | SHA-256 | Components and architecture | Audit finding / usefulness |
|---|---|---|---|
| `Загрузки/Иврит_KERNEL_A.zip` | `da83642681d2afdc7f61073b50147be9101a78eece5e998041cd51c021fb42c9` | `base_kernel.py`, metadata/registry, notebook, one init test, example | Minimal Python shell. `structural_analysis` only calls `split()` and returns constant labels. Useful as provenance and API intent only. |
| `Загрузки/Иврит_KERNEL_B.zip` | `88c0e2f7591aa1e604e603987378e579b20383dde009cd439c968661fefb31ce` | A plus `phonetics/acoustic_module.py` | Acoustic methods return placeholders or constants; numpy is imported but no signal algorithm is implemented. |
| `Загрузки/Иврит_KERNEL_B (1).zip` | `2827e6a9f9f8ad9dbc200aea643b321fd715a38a6b39ed8e86c0f196ea4f772c` | Same paths and file content as B | Archive hash differs; extracted files compare byte-for-byte identical to B. Duplicate source, not a distinct implementation. |
| `Загрузки/Иврит_KERNEL_S.zip` | `fac339266437a09f93a2f9e9d66e35657ad259605a893e6e85db3e22d4f21c45` | `panini_core.py`, synthetic transformations, tests/example | Executable math, but examples and algorithms concern Sanskrit transliteration/mantra, not Hebrew. Chanda test fails. Not integrated as Hebrew functionality. |
| `Загрузки/Иврит_KERNEL_Modernized.zip` | `3ede54ddc31b59480793bafdbfc14e96c83ebbfc57fb533fac29692077a406c8` | Short `base_kernel.py`, metadata/registry, notebook, init test, example | `get_status` only; no Hebrew analysis method. Reported metrics differ from A/B without measurement evidence. “Modernized” does not represent greater language coverage. |
| `Загрузки/gemini-code-1794400372342.json` | `0eb3899ec1591279844d632045cdb564122163123571d93267a1cef66e0014a0` | Embedded constant-output `HebrewCore`, EVRID/NADI/ZIC/MODULE-64/Dharma metadata | Transfer record only; embedded analysis always returns `VALID` and fixed values. Metrics are preserved as reported/proposed, not verified. |
| `Загрузки/Archives/Иврит_KERNEL_A.zip` | `028185c7c49da20bc27a2186109bfbabaf19ae863dcb471f94cf8b3039e873da` | Same extracted file contents as the listed A archive | A duplicate package with different ZIP checksum/timestamps. |
| `Загрузки/Archives/Иврит_KERNEL_C.zip` | `f23f6658e9c8069e9523681f59c646c8515a2843e18664b264d25540416727f4` | C base shell plus acoustic placeholder | Same fixed-output acoustic pattern as B, without the YouTube method. No new Hebrew algorithm. |
| `Загрузки/Archives/Иврит_KERNEL_Modernized.zip` | `c80586e697c76c8c5994dfe7453e44d9fafde8dfd315ad5070dbc9b5f09bb470` | Same extracted file contents as listed Modernized archive | Duplicate package with different ZIP checksum/timestamps. |

The archived A package and the listed A package have different archive hashes, while the extracted files compare byte-for-byte identical. The differing archive bytes therefore do not indicate a distinct implementation.

## Component comparison

| Component | A | B / B (1) | C | S | Modernized | Canonical disposition |
|---|---|---|---|---|---|---|
| Base core | `split()` plus fixed labels | Same as A | Status shell | No Hebrew base core | Status shell | Replaced by a much narrower Unicode observation utility; no claim of morphology |
| Panini Core | — | — | — | Synthetic state machine | — | Excluded from Hebrew runtime; unrelated Sanskrit-style formulas and one failing test |
| Acoustic module | — | Placeholder | Placeholder variant | — | — | Excluded; no acoustic computation |
| Lexical registry | Metadata tags only | Same | Same | Same | Metadata tags only | Empty source-backed pattern registry; no invented lexicon |
| Morphology / grammar / semantics | Absent | Absent | Absent | Absent | Absent | Research outlines, explicitly NOT_VERIFIED |
| Context | Constant output only | Constant output only | Constant output only | Synthetic metric | Constant output only | `UNKNOWN` policy only; no contextual inference |
| Metadata | Reported constants | Reported constants | Reported constants | Reported constants | Different reported TDI constant | Preserved as reported/proposed, not performance evidence |
| Tests | Init assertion | Init assertion | Init assertion | Init, sandhi, chanda assertions | Init assertion | Replaced/supplemented with behavior tests for implemented Unicode utilities |

## Test evidence from supplied packages

- A, B, B (1), C, and Modernized initialization scripts pass when run from their test directories; these tests only check a constant readiness attribute.
- S `test_kernel.py` fails at `test_chanda_validation`: its expected `VALID` result is not returned for the supplied test string.
- The source notebooks contain no saved execution outputs; their cells were inspected, not run.
- No source package contains a Hebrew corpus, Hebrew lexical data, morphology rules, grammar rules, or bibliographic references.

## Canonical assembly decisions

- Retain the package identifier and AAM extension values as reported metadata.
- Do not copy placeholder classes, hardcoded metrics, unused numpy imports, notebook setup, or the unrelated Panini implementation into runtime.
- Add a standard-library-only core for NFC normalization, whitespace tokenization, code-point classification, and JSON-compatible results.
- Keep linguistic analysis, historical interpretation, acoustic processing, and sacred/cultural interpretation unimplemented until sources, data, and behavior tests are provided.

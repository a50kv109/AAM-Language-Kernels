# Matrice di Verità Fondamentale (Ground Truth Matrix): IT:13

## 🎯 MAPPATURA SEMANTICA AXIS-10 (SOL-TAGS)

| Lemma (IT) | Lemma (EN) | Tag SOL | Definizione Operativa | Affidabilità |
| :--- | :--- | :--- | :--- | :--- |
| `Sistema` | `System` | `[S-001]` | Insieme di componenti interagenti. | 1.00 |
| `Nucleo` | `Kernel` | `[S-002]` | Parte centrale di controllo (Kern). | 0.99 |
| `Invarianza` | `Invariance`| `[C-001]` | Proprietà di rimanere immutato. | 1.00 |
| `Deviazione` | `Deviation` | `[D-001]` | Scostamento dal riferimento SDT. | 0.98 |
| `Processo` | `Process` | `[P-001]` | Ciclo di esecuzione tecnica. | 1.00 |
| `Qualità` | `Quality` | `[QLT-001]` | Conformità agli standard (Asse 10). | 1.00 |
| `Ingegneria` | `Engineering` | `[E-001]` | Disciplina tecnica (Asse 8). | 1.00 |
| `Progettazione` | `Design` | `[D-010]` | Sintesi tra ingegneria e design. | 1.00 |
| `Tolleranza` | `Tolerance` | `[T-002]` | Deviazione massima consentita (UNI). | 0.98 |
| `Allegro` | `lively / fast` | `[M-Tempo-001]` | Qualitative tempo indication used in musical scores. | Initial |
| `Adagio` | `slow / unhurried` | `[M-Tempo-002]` | Slower tempo or character marking. | Initial |
| `Crescendo` | `growing` | `[M-Dyn-001]` | Gradual increase in dynamic intensity. | Initial |
| `Legato` | `bound / connected` | `[M-Art-001]` | Smooth articulation across notes or phrases. | Initial |
| `Staccato` | `detached` | `[M-Art-002]` | Short detached articulation. | Initial |
| `Più` | `more` | `[M-Mod-001]` | Comparative operator modifying tempo or expression. | Initial |
| `Meno` | `less` | `[M-Mod-002]` | Comparative operator reducing intensity or animation. | Initial |
| `A tempo` | `at the tempo` | `[M-Return-001]` | Return to the established tempo. | Initial |

---
*Nota: I lemmi sono sincronizzati con l'etallone inglese Golden Standard (EN:10). La registrazione musicale è una collezione iniziale e non un corpus validato di partiture autentiche.*

## 🧩 ITALIAN PATTERN REGISTRY

The detailed Italian kernel pattern records are kept in [pattern_registry.md](./pattern_registry.md). The registry is intentionally minimal and evidence-aware:

- it separates source text, literal gloss, semantic explanation, procedural description, and unresolved questions;
- it keeps musical examples clearly marked as illustrative rather than as verified quotations from a corpus;
- it retains unresolved ambiguity for abbreviations such as `rit.` until context supports a defensible reading.

## 🛡 CONSENSUS_PROTOCOL
```yaml
CONSENSUS_PROTOCOL:
  ON_CONFLICT: "LOG_EVENT_AND_REPORT"
  LOG_FORMAT: 
    STATUS: "CONFLICT_DETECTED"
    CANDIDATES: ["TAG_A", "TAG_B"]
    ACTION: "WAITING_FOR_ARCHITECT_REVIEW"
```

# 真值矩阵 (Ground Truth Matrix): ZH:09

## 🎯 AXIS-10 语义映射 (SOL-TAGS)

| SOL 标签 | 术语 (ZH) | 术语 (EN) | 定义 |
| :--- | :--- | :--- | :--- |
| `[S-001]` | **系统** | System | 一组相互作用的组件。 |
| `[S-002]` | **核心** | Kernel | 中央控制部分。 |
| `[C-001]` | **不变性** | Invariance | 测量条件下保持不变的特性。 |
| `[D-001]` | **偏差** | Deviation | 观察值与标准值之间的差异。 |
| `SOL_ENG_08_001` | **技术系统** | Technical Systems | 复杂的工程组件。 |
| `SOL_MED_09_001` | **医疗设备** | Medical Equipment | 用于诊断和治疗的设备。 |
| `SOL_SPE_10_001` | **自动化** | Automation | 自行控制系统。 |

---
*注：所有引理均与英文基准 (Golden Standard) 同步。*

## 📚 CANONICAL HISTORICAL PATTERN REGISTRY

| Pattern ID | Canonical Name | Source | Evidence Level | Source Availability | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ZH_PAT_001` | HESUAN_FRACTION_ADDITION | 《九章算术》 | VERIFIED_PRIMARY_SOURCE | original_source_text_available | ✅ CANONICAL |
| `ZH_PAT_002A` | SUNZI_POSITIONAL_ORIENTATION | 《孙子算经》 | VERIFIED_PRIMARY_SOURCE | original_source_text_available | ✅ CANONICAL |
| `ZH_PAT_002B` | XIAHOU_BIQUINARY_CONSTRUCTION | 《夏侯阳算经》 | VERIFIED_PRIMARY_SOURCE | original_source_text_available | ✅ CANONICAL |
| `ZH_PAT_003` | HAIDAO_GEOMETRIC_SURVEYING | 《海岛算经》 | VERIFIED_WITH_COMMENTARY | original_source_text_unavailable | ⚠️ CANONICAL_WITH_WARNING |
| `ZH_PAT_005` | SUNZI_DIVISION_SHIFT | 《孙子算经》 | VERIFIED_PRIMARY_SOURCE | original_source_text_available | ✅ CANONICAL |

### Research-only records

| Pattern ID | Status | Source | Notes |
| :--- | :--- | :--- | :--- |
| `ZH_PAT_004` | ⚠️ RESEARCH_ONLY | 《数术记遗》 | Edition-specific witness data remains unresolved; not promoted to canonical status. |

### Source-state note

- `original_source_text_available`: full source quotation preserved in the record.
- `original_source_text_unavailable`: source quotation is missing; the record remains explicit about the gap.
- `quotation_partially_available`: only a partial quotation is recorded.
- `quotation_awaiting_verification`: the quotation status is not yet confirmed.

### Registry reference
The detailed records are held in [pattern_registry.md](./pattern_registry.md).

## 🛡 CONSENSUS_PROTOCOL
```yaml
CONSENSUS_PROTOCOL:
  ON_CONFLICT: "LOG_EVENT_AND_REPORT"
  LOG_FORMAT: 
    STATUS: "CONFLICT_DETECTED"
    CANDIDATES: ["TAG_A", "TAG_B"]
    ACTION: "WAITING_FOR_ARCHITECT_REVIEW"
```

# 工程护照：中文核心 (ZH:09)

## 📋 基本信息
- **语言：** 中文 (Chinese)
- **ISO 代码：** zh-CN
- **角色：** SEMANTIC GATEWAY (AAM-V2) SYNCHRONIZED KERNEL
- **核心 ID：** ZH:09
- **架构版本：** AAM-V2.20-AXIS10
- **完整性协议：** AAM-V2_ARTSYBASHEV

## 🧠 AXIS-10 配置 (10轴标准)

### 工程语义编译器 (ESC) 状态
- **协议：** AAM-V2_ARTSYBASHEV
- **配置 (Master)：** [include: ../../../MASTER_AXIS10_CONFIG.md]
- **主配置链接：** [MASTER_AXIS10_CONFIG.md](../../MASTER_AXIS10_CONFIG.md)
- **ESC 已启用：** ✅ 是
- **验证级别：** FULL (SOL-tags + Integrity Score + TDI)

### 10轴定义：

#### 语言轴 (1-7)：
1. **语义轴：** 概念结构。
2. **语用轴：** 工程沟通。
3. **句法轴：** 准确性与灵活性。
4. **形态轴：** 稳定词尾管理。
5. **情感轴：** 可靠性、精确性。
6. **语境轴：** 工业寄存器。
7. **声符轴：** 技术传统。

#### 工程轴 (8-10)：
8. **技术轴 (工程)：** 设计、ISO/GB 标准。
9. **医疗轴 (生物医学)：** 诊断仪器。
10. **专业轴 (工业)：** 自动化、质量控制。

### 完整性指标
- **目标 IS：** ≥ 0.95
- **TDI 阈值：** ≤ 0.25
- **当前 IS：** 0.00
- **状态：** ⚠️ INITIALIZING_AXIS10

### 合规声明
本核心已集成到 AAM-V2 系统中，并与英文基准 (Golden Standard) 同步。

## 🧭 HISTORICAL PATTERN ENRICHMENT

### 研究范围
中文核心已接收第一批受控历史计算知识记录，并在保持兼容性的前提下扩展了源文本、译意、语义说明、程序步骤、现代形式化和未决问题的分离结构。

### 现有规范模式
- **Canonical Registry:** [pattern_registry.md](./pattern_registry.md)
- **Canonical IDs:** ZH_PAT_001, ZH_PAT_002A, ZH_PAT_002B, ZH_PAT_003, ZH_PAT_005
- **Research-only status:** ZH_PAT_004 remains in the research layer and is not promoted to canonical status.

### 已接入的历史知识
- **ZH_PAT_001** — 合分術 / fractional addition
- **ZH_PAT_002A** — 位置取向 / positional orientation
- **ZH_PAT_002B** — 五位构造 / bi-quinary construction
- **ZH_PAT_003** — 海岛测量 / geometric surveying
- **ZH_PAT_005** — 除法位移 / division positioning rule

### 证据分离原则
每个模式保留以下明确分层：
- 原文
- 直译
- 语义说明
- 程序步骤
- 现代形式化
- 解释说明
- 未决问题

这使得历史事实、现代解释和程序重建可以分别验证，而不被压缩成单一叙述。

### 版本与审计状态
- **Documentation Version:** 2026-11-11
- **Validation Method:** local registry validation script at [validate_patterns.py](./validate_patterns.py)
- **Audit principle:** target version must be recorded explicitly; findings tied to earlier versions must not be silently reused for newer corrected versions.

## 🧾 SOURCE PROVENANCE HARDENING

### Provenance fields now distinguished
The registry now distinguishes between:
- source title and original-script title;
- chapter or volume;
- problem or section;
- edition;
- textual witness;
- source reference;
- source-text availability state;
- quotation availability state;
- evidence level.

This prevents explanatory prose from being mistaken for an original quotation and keeps source availability separate from validation status.

### Source availability states
- `original_source_text_available`
- `original_source_text_unavailable`
- `quotation_partially_available`
- `quotation_awaiting_verification`

These states are explicitly separate from the pattern's canonical or research-only status. A structurally valid record can still contain an unavailable quotation, and the validator reports this as a warning, not as a fatal error.

### Minimal audit model
The repository uses a minimal template for future independent review:
- `audit_id`
- `pattern_id`
- `target_version_id`
- `reviewed_revision`
- `reviewer`
- `audit_date`
- `source_basis`
- `findings`
- `corrections`
- `review_status`

This is deliberately lightweight and does not introduce a full audit application.

### ZH_PAT_003 status note
`ZH_PAT_003` remains in the canonical layer only with an explicit warning that its exact source quotation is unavailable in the current repository. If the source witness remains absent, the record should be demoted to research-only in a later, explicit review. This is not a silent downgrade.

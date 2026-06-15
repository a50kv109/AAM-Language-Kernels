# BENCHMARKS: Ukrainian Core Validation

## TDI (Technical Divergence Index) Formula

The Ukrainian Core introduces a specific linguistic delta:

`TDI_ua = (Δsemantic * 0.6) + (Δstructural * 0.4)`

- **Δsemantic:** Deviation of the Ukrainian term from the SOL primitive intent.
- **Δstructural:** Topological noise introduced by phonetic/syntactic specifics.

---

## TDI Zones

| Zone | TDI Range | Status | Action |
| :--- | :--- | :--- | :--- |
| **Sattva (Green)** | < 0.30 | Optimal | Normal operation. |
| **Rajas (Yellow)** | 0.30 - 0.45 | Warning | Check `failure_modes.md` (Drift Map). Apply Mercury Flow. |
| **Tamas (Red)** | ≥ 0.45 | Critical | **Alyosha Gate.** Immediate Kenosis required. Re-map axes. |

---

## Verification Protocol (Example)

```python
def validate_ua_term(term: str, sol_primitive: str):
    # 1. Fetch mapping from axes.md
    ua_base = get_mapping(sol_primitive)
    
    # 2. Calculate semantic delta
    delta_sem = calculate_semantic_similarity(term, ua_base)
    
    # 3. Calculate structural noise
    delta_str = calculate_syntactic_noise(term)
    
    # 4. Compute TDI
    tdi = (delta_sem * 0.6) + (delta_str * 0.4)
    
    # 5. Decision
    if tdi >= 0.45:
        trigger_kenosis()
        return False
    return True
# AXES: SOL-UA Mapping for Ukrainian Core

## Protocol
AAM-V1_ARTSYBASHEV_UA_KHARKIV_AIANALYSIS  
**Rule:** Absolute priority of engineering physics over linguistic norms.

---

## SOL Primitive Mapping Table

| SOL Primitive | Ukrainian Equivalent (Інженерний еквівалент) | Context Example (Інженерний приклад) |
| :--- | :--- | :--- |
| **SOURCE** | ДЖЕРЕЛО | "Джерело живлення", "Джерело даних" |
| **FLOW** | ПОТІК | "Потік рідини", "Інформаційний потік" |
| **STORAGE** | НАКОПИЧУВАЧ | "Накопичувач енергії", "Буфер даних" |
| **CONSTRAINT** | ОБМЕЖЕННЯ | "Технічне обмеження", "Допуск" |
| **INTERFACE** | СПРЯЖЕННЯ / ІНТЕРФЕЙС | "Спряження валів", "Інтерфейс користувача" |
| **TRANSFORM** | ПЕРЕТВОРЕННЯ | "Перетворення сигналу", "Зміна стану" |
| **DISSIPATE** | РОСІЯННЯ | "Розсіяння тепла", "Демпфування" |
| **CONTROL** | КЕРУВАННЯ | "Зворотний зв'язок", "Система регуляції" |

---

## Operational Rules

1. **No Translation:** The Primitive does not change. Only its *incarnation* in the context changes.
2. **Context Lock:** If a Ukrainian term maps to two primitives (e.g., "Напруга" -> SOURCE or TRANSFORM), the context of the `Drift Map` determines the choice.
3. **Fallback:** If no direct mapping exists, the English SOL Primitive is used to preserve topology.

> **Critical:** This file is the *skeleton* of the Ukrainian Core.
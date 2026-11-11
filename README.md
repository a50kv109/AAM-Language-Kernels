# AAM-Language-Kernels

AAM-Language-Kernels: Модульная архитектура языкового ядра на основе AAM, SOL и AXIS-10.

Документация:
- Основная архитектура: [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md)
- Общий геометрический канон AAM (предложение; языковые соответствия не проверены): [engineering/geometry_canon/GEOMETRY_CANON.md](engineering/geometry_canon/GEOMETRY_CANON.md)

Доступные языковые ядра:
- 🇬🇧 Английский (eng:10 - Golden Standard)
- 🇷🇺 Русский (rus)
- 🇺🇦 Украинский (ukr)
- 🇨🇳 Китайский (zho)
- 🇮🇱 Иврит (heb) — CORE_HEBREW_V1.0 / PROPOSED INITIAL BASELINE; Unicode utilities and optional Stanza adapter (Hebrew model not installed in the current environment)
- 🇯🇵 Японский (jpn) — L2_JA / PROPOSED INITIAL BASELINE
- 🇫🇷 Французский (fra)
- 🇩🇪 Немецкий (deu)
- 🇮🇹 Итальянский (ita)
- 🇳🇴 Норвежский (nor)
- 🇬🇪 Грузинский (kat)
- 🇮🇳 Санскрит (san:16 - Reference Gateway)

### Инструментальная база / Kernel Builder

**AAM-Language-Kernel-Builder**

[https://github.com/a50kv109/AAM-Language-Kernel-Builder](https://github.com/a50kv109/AAM-Language-Kernel-Builder)

Сопутствующий инструментальный репозиторий для исследования, структурирования и сборки языковых ядер AAM. Он отражает архитектурные наработки и механизмы, используемые при формировании модульных языковых структур, но не означает, что все существующие ядра автоматически сгенерированы этим инструментом. Основная роль Builder — инструментальный слой для анализа, сборки и экспорта компонентов языкового ядра.

Для контрибьюторов:
- Используйте `MASTER_AXIS10_CONFIG.md` для стандартизации конфигураций новых ядер.
- Следуйте структуре, описанной в `language/master/AXIS10_FULL_TEMPLATE.md` при добавлении новых `INDEX.md` для языков.
- Соблюдайте `SEMANTIC_GOVERNANCE.md` как конституцию смыслов AAM-V2 для всех шлюзов и интеграций.

Поддержание:
- Лицензия: Apache-2.0 (файл LICENSE)
- Для вопросов и предложений открывайте Issues в репозитории.

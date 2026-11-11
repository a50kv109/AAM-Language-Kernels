# Omission Resolution

If subject (`は`/`が`) is omitted:
1. Search previous sentence for active topic.
2. Track verb directionality (e.g., もらう/あげる/くれる).
3. If unresolved, output `[UNKNOWN_SUBJECT]`. Do not hallucinate actors.
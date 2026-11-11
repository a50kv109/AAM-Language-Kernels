from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core import HebrewKernel, HebrewNLPAdapter


if __name__ == "__main__":
    text = "שלום עולם"
    script_result = HebrewKernel.analyze_sentence(text)
    nlp_result = HebrewNLPAdapter.from_stanza().analyze(text)
    print("Script utilities:")
    print(json.dumps(script_result, ensure_ascii=False, indent=2))
    print("Optional Stanza analysis:")
    print(json.dumps(nlp_result, ensure_ascii=False, indent=2))

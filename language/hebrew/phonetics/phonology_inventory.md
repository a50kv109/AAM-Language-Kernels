# Phonetics and Orthography Inventory

## Scope and epistemic status

The source packages contain no pronunciation tables, recorded speech, or phonetics bibliography. This file is a research checklist; phonetic claims are NOT_VERIFIED and no acoustic model is implemented.

## Orthographic inventory to source and review

- The 22 base consonant-letter characters represented by this kernel: `א ב ג ד ה ו ז ח ט י כ ל מ נ ס ע פ צ ק ר ש ת`.
- The five additional final-form characters recognized by the Unicode utility: `ך ם ן ף ץ`. Their classification as orthographic forms does not imply separate phonemes.
- Pointing / niqqud marks and their combinations with letters. The runtime can count combining marks in the Hebrew Unicode block but does not name, validate, or interpret them.
- Cantillation marks and their interaction with pointed text.
- Guttural-letter descriptions and variation across historical periods, communities, and modern pronunciation traditions.
- Orthography-to-sound correspondence, which must not be assumed one-to-one.

The character inventory is a code-point scope for the limited utility; phonological descriptions remain NOT_VERIFIED because no linguistic reference or audio source was supplied. The Unicode script utilities classify code points and combining marks only. They do not identify phonemes, pronounce text, or validate niqqud placement.

## Acoustic module disposition

`AcousticProcessor` in source variants B and C is a placeholder: formants are returned as `"calibrating..."`, resonance values are constants, and B's YouTube method reports a successful capture without acquiring audio. The numpy import does not implement signal analysis. The module is not integrated into this kernel.

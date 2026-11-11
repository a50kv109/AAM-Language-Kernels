# Italian Musical Grammar Patterns — Initial Set

**Layer:** IT-MUSIC-01  
**Status:** INITIAL / HUMAN REVIEW REQUIRED

This file describes recurring constructions in Italian musical directions. Examples are illustrative, not quotations from a particular score.

## 1. Tempo labels and modifiers
| Pattern | Example | Literal sense | Conventional reading |
|---|---|---|---|
| Adjective used as tempo marking | *Allegro* | cheerful, lively | lively/fast tempo character |
| Adverbial/tempo term | *Adagio* | at ease, unhurried | slow, measured character |
| Comparative modifier | *Più mosso* | more moved | more animated/faster |
| Negative comparative | *Meno mosso* | less moved | less animated/slower |
| Degree modifier + adjective | *Molto allegro* | very lively | strongly lively/fast character |
| Softening modifier + tempo term | *Poco adagio* | a little adagio | somewhat unhurried; context matters |
| Return marker | *A tempo* | at the tempo | return to established tempo |
| Return to first tempo | *Tempo primo* | first tempo | return to opening/first tempo |

**Parsing note:** preserve lexical phrase and conventional function separately. A qualitative marking does not encode an exact BPM value.

## 2. Character and expression
| Pattern | Example | Literal sense | Conventional reading |
|---|---|---|---|
| Manner adverb | *Dolcemente* | sweetly | gentle/tender character |
| Manner adverb | *Leggermente* | lightly | light manner of playing |
| Manner term | *Cantabile* | singably | vocal, singing melodic character |
| Preposition *con* + noun | *Con brio* | with spirit | spirited, energetic |
| Preposition *con* + noun | *Con fuoco* | with fire | fiery/intense expression |
| Preposition *con* + noun | *Con grazia* | with grace | graceful manner |
| Preposition *senza* + noun | *Senza vibrato* | without vibrato | omit/minimize vibrato according to context |

## 3. Dynamics and transitions
| Pattern | Example | Literal sense | Conventional reading |
|---|---|---|---|
| Dynamic term | *Piano* | soft | quiet dynamic |
| Dynamic term | *Forte* | strong | loud dynamic |
| Degree form | *Fortissimo* | very strong | very loud |
| Change process | *Crescendo* | growing | gradually increase volume |
| Change process | *Diminuendo* | diminishing | gradually decrease volume |
| Comparative phrase | *Più forte* | more strong | louder |
| Continuative + dynamic | *Sempre piano* | always soft | maintain a soft dynamic |

Dynamic level and dynamic transition are distinct semantic types: *forte* denotes a level; *crescendo* denotes change over time.

## 4. Articulation and phrasing
| Pattern | Example | Literal sense | Conventional reading |
|---|---|---|---|
| Manner term | *Legato* | bound/connected | smoothly connect notes |
| Manner term | *Staccato* | detached | separate notes |
| Manner term | *Marcato* | marked | distinctly emphasize notes |
| Preposition + noun | *Sotto voce* | under the voice | subdued manner |
| Participial/adjectival term | *Tenuto* | held | sustain/hold as indicated; may include emphasis |
| Preposition + noun | *A piacere* | at pleasure | performer discretion within context/style |

Text directions and graphic articulation marks are separate evidence channels.

## 5. Grammatical operators
### *più* / *meno*
Comparative operators modifying an adjective, adverb or conventional musical term.
- *più forte* — louder.
- *meno mosso* — less animated.
- *più piano* — softer (less loud); avoid translating *piano* mechanically as an instrument.

### *molto* / *poco* / *assai*
Degree modifiers whose scope is the following musical expression.
- *molto agitato* — very agitated.
- *poco ritardando* — a slight slowing.
- *allegro assai* — very lively/fast.

### *con* / *senza*
Prepositions introducing a manner, quality or excluded feature.
- *con anima* — with spirit/animation.
- *con sordino* — with mute.
- *senza sordino* — without mute.

### *sempre*
Continuative operator: maintain a property until changed or contextually superseded.
- *sempre legato* — maintain connected articulation.
- *sempre forte* — maintain a strong dynamic.

### *subito*
Suddenness operator: indicates an abrupt rather than gradual change.
- *subito piano* — become suddenly soft.
- *subito forte* — become suddenly loud.

## 6. Ellipsis and score shorthand
Scores may abbreviate or omit recoverable words. Examples include *accel.* (often *accelerando*) and *rit.* (which may refer to *ritardando* or *ritenuto* depending on context/editorial convention).

**Safety rule:** do not silently expand an ambiguous abbreviation. Preserve the printed form, candidate expansions, contextual evidence and unresolved status.

## 7. Minimal semantic record
```yaml
surface_form: "poco più mosso"
language: it
domain: music_performance
construction:
  degree_modifier: poco
  comparative: piu
  head: mosso
literal_gloss: "a little more moved"
conventional_function: "slightly increase animation/tempo"
dimension: tempo_character
confidence: null
context_required: true
status: INITIAL
```

This is a documentation schema, not an implemented parser.

## 8. Validation tasks
- Collect authentic score excerpts with edition/page provenance.
- Compare directions across composers and periods.
- Record ambiguous cases, especially *rit.*, *poco*, *mosso* and *tenuto*.
- Have a music-literate Italian reviewer assess gloss and conventional interpretation.
- Do not assign IS/TDI values until a reference set and scoring procedure exist.
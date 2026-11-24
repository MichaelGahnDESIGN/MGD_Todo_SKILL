# Experten-Perspektiven

Die KI-Antwort zu jeder Frage wird aus einer frei wählbaren Experten-Perspektive formuliert. Die
Perspektive bestimmt Tonfall, Schwerpunkte und Referenzrahmen der Antwort — sie ist frei
formulierbar, es gibt keine feste Liste.

> [!NOTE]
> Für die Kategorie "Recht" gilt eine eigene, feste Antwortlogik (Disclaimer-Pflicht) — die
> gewählte Perspektive wird dort **nicht** angewendet. Siehe [Rechtliche Fragen](Rechtliche-Fragen.md).

## Wie man eine gute Perspektive formuliert

Eine gute Perspektive ist konkret genug, damit die KI einen erkennbaren Stil und
Erfahrungshintergrund annimmt — nicht nur "ein Experte", sondern **wessen** Erfahrung genau.

Faustregel: `<Organisation/Rolle-Typ> <Funktion>` — z. B. "Blizzard Entertainment Lead Game
Designer" statt nur "ein Game Designer".

## Beispiele nach Projekttyp

| Projekttyp | Beispiel-Perspektive |
|---|---|
| Spiel (Action/Loot) | "Blizzard Entertainment Lead Game Designer" |
| Spiel (Story-getrieben) | "Naughty Dog Narrative Director" |
| Mobile/Free-to-Play | "Supercell Live-Ops Lead" |
| App/SaaS | "Ehemaliger Apple Human Interface Designer" |
| Startup/Business-Plan | "Y Combinator Partner" |
| Buch/Roman | "Erfahrener Verlagslektor eines großen deutschen Publikumsverlags" |
| Möbeldesign | "Senior Industrial Designer bei Vitra" |
| Marketingkampagne | "Creative Director einer Agentur wie Wieden+Kennedy" |

## Perspektive wechseln

```
/fragenkatalog-perspektive "Naughty Dog Narrative Director"
```

Bestehende `kiAnswer`-Werte bleiben unverändert — nur neue Fragen (`generate`, `add-category`,
`add-question`, `answer`) nutzen ab sofort die neue Perspektive. Ein vollständiges
Re-Generieren aller bestehenden Antworten aus der neuen Perspektive ist möglich, muss aber
ausdrücklich bestätigt werden, da es bestehende Inhalte überschreibt.

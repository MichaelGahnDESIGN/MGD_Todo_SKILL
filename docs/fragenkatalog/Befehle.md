# Befehle im Detail

Alle Befehle setzen voraus, dass `.fragenkatalog-config` existiert (angelegt durch
`/fragenkatalog-setup`). Fehlt sie, wird `setup` automatisch vorgeschlagen.

## `/fragenkatalog-setup`

**Beispiel-Eingabe:**

```
/fragenkatalog-setup
> Projektname/-typ: Sternenfänger, ein Mobile-Sammelspiel
> Plattform: iOS, Android
> Perspektive: Blizzard Entertainment Lead Game Designer
> Speicherpfad: docs/Fragenkatalog.html
> Sprache: Deutsch
> Rechts-Kategorie einschließen? Ja
```

**Beispiel-Ausgabe:**

```
✅ Fragenkatalog eingerichtet:
   Projekt: Sternenfänger (Mobile Game, iOS/Android)
   Perspektive: 💙 Blizzard Entertainment Lead Game Designer
   Rechts-Kategorie: aktiv (⚖️)
   Speicherort: docs/Fragenkatalog.html
   Konfiguration: .fragenkatalog-config

Weiter mit: /fragenkatalog-generate 50
```

## `/fragenkatalog-generate [anzahl]`

```
/fragenkatalog-generate 40
```

```
✅ 40 Fragen generiert:
   Kern-Loop: 6 · Welt/Setting: 5 · Story: 4 · Steuerung: 4 ·
   Progression: 5 · Wirtschaft/Balance: 5 · UI/UX/HUD: 4 ·
   Recht: 7

Alle Fragen sofort beantwortet aus: 💙 Blizzard Entertainment Lead Game Designer
(Recht-Fragen mit ⚖️-Disclaimer)

Weiter mit: /fragenkatalog-export
```

## `/fragenkatalog-add-category <name>`

```
/fragenkatalog-add-category "Monetarisierung"
```

```
✅ Kategorie "Monetarisierung" mit 9 Fragen hinzugefügt, alle beantwortet
   aus 💙 Blizzard Entertainment Lead Game Designer.
```

## `/fragenkatalog-add-question <kategorie> <frage>`

```
/fragenkatalog-add-question "UI/UX" "Wie sieht das Onboarding für Erstnutzer aus?"
```

```
✅ Frage #41 zu "UI/UX" hinzugefügt und beantwortet:
   💙 Ein 3-Schritte-Onboarding, das den Kern-Loop direkt erlebbar macht ...
```

## `/fragenkatalog-answer <id-oder-suchtext>`

```
/fragenkatalog-answer 17
```

```
Frage #17 (Wirtschaft/Balance): "Wie werden Premium-Währung und Spielzeit-Farming balanciert?"
Bestehende Antwort vorhanden. Neu beantworten? (j/n)
> j
✅ Frage #17 neu beantwortet aus 💙 Blizzard Entertainment Lead Game Designer.
```

Volltextsuche statt ID:

```
/fragenkatalog-answer "Premium-Währung"
```

## `/fragenkatalog-export`

```
/fragenkatalog-export
```

```
✅ docs/Fragenkatalog.html geschrieben (47 Fragen, 9 Kategorien).
   Öffne die Datei direkt im Browser — keine Internetverbindung nötig.
```

## `/fragenkatalog-import <pfad>`

```
/fragenkatalog-import alte-notizen.json
```

```
Datei enthält 12 Fragen. 2 Duplikate erkannt (ähnlicher question-Text zu #3, #9).
Wie verfahren? (überspringen / überschreiben / als Duplikat anhängen)
> überspringen
✅ 10 neue Fragen importiert, 2 übersprungen. Gesamtstand: 57 Fragen.
```

## `/fragenkatalog-stats`

```
/fragenkatalog-stats
```

```
📊 Fragenkatalog-Statistik
   Gesamt: 57 Fragen in 10 Kategorien
   Eigene Antworten vorhanden: 22 (38,6 %)
   Noch offen: 35

   Recht: 7 Fragen, 1 beantwortet
   Kern-Loop: 6 Fragen, 6 beantwortet
   ...
```

## `/fragenkatalog-pfad <pfad>`

```
/fragenkatalog-pfad projekt/docs/Fragenkatalog.html
```

```
✅ Speicherort geändert: docs/Fragenkatalog.html → projekt/docs/Fragenkatalog.html
   Bestehende Datei am alten Pfad verschieben oder neu exportieren? (verschieben/neu)
```

## `/fragenkatalog-perspektive <beschreibung>`

```
/fragenkatalog-perspektive "Naughty Dog Narrative Director"
```

```
✅ Perspektive geändert: 💙 Blizzard Entertainment Lead Game Designer
   → 💙 Naughty Dog Narrative Director
   Bestehende KI-Antworten bleiben unverändert. Alle 47 bestehenden Antworten jetzt
   aus der neuen Perspektive neu generieren? (j/n)
> n
✅ Neue Perspektive gilt ab sofort für künftige Fragen.
```

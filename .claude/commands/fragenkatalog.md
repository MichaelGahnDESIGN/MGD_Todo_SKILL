---
description: Fragenkatalog erstellen, erweitern, beantworten und exportieren
argument-hint: "[setup|generate|add-category|add-question|answer|export|import|stats|pfad|perspektive] [args...]"
---

# /fragenkatalog

Dieser Slash-Befehl ist der Claude-Code-Einstiegspunkt für den **Fragenkatalog-Skill**. Die
vollständige, verbindliche Spezifikation steht in `skills/fragenkatalog/SKILL.md` —
lies sie vollständig, bevor du irgendeine Unterfunktion ausführst.

## Aufruf

```
/fragenkatalog <unterbefehl> [argumente]
```

Unterstützte Unterbefehle (Details, exaktes Verhalten und Datenmodell stehen in `SKILL.md`):

| Unterbefehl | Entspricht | Kurzbeschreibung |
|---|---|---|
| `setup` | `/fragenkatalog-setup` | Interaktive Ersteinrichtung (Projekt, Plattform, Perspektive, Pfad, Sprache) |
| `generate [anzahl]` | `/fragenkatalog-generate` | Initiale Fragenliste generieren + sofort beantworten |
| `add-category <name>` | `/fragenkatalog-add-category` | Neue Kategorie mit 5–30 Fragen hinzufügen |
| `add-question <kategorie> <frage>` | `/fragenkatalog-add-question` | Einzelne Frage manuell hinzufügen |
| `answer <id-oder-suchtext>` | `/fragenkatalog-answer` | Bestehende Frage (neu) beantworten |
| `export` | `/fragenkatalog-export` | Finale self-contained HTML bauen/aktualisieren |
| `import <pfad>` | `/fragenkatalog-import` | Bestehende JSON/Markdown-Fragenliste importieren |
| `stats` | `/fragenkatalog-stats` | Fortschrittsübersicht anzeigen |
| `pfad <pfad>` | `/fragenkatalog-pfad` | Speicherort der HTML ändern |
| `perspektive <beschreibung>` | `/fragenkatalog-perspektive` | Experten-Perspektive ändern |

Wird kein Unterbefehl übergeben (`/fragenkatalog` allein) oder existiert `.fragenkatalog-config`
noch nicht, führe `setup` aus.

## Verhalten

1. Lies `SKILL.md` (relativ zum Skill-Verzeichnis) vollständig ein.
2. Prüfe, ob `.fragenkatalog-config` im Projekt-Root existiert. Falls nicht und der Unterbefehl
   nicht `setup` ist: weise freundlich darauf hin und biete an, `setup` jetzt auszuführen.
3. Führe den in `SKILL.md` unter dem entsprechenden `/fragenkatalog-<unterbefehl>`-Abschnitt
   beschriebenen Ablauf exakt aus, inklusive Datenmodell (`fragenkatalog.json`), Konfiguration
   (`.fragenkatalog-config`) und HTML-Export-Struktur (`templates/Fragenkatalog.template.html`
   als Basis).
4. Halte alle Ausgaben in der in `.fragenkatalog-config` hinterlegten `language` (Default:
   Deutsch).
5. Bestätige nach jeder Aktion knapp, was geändert wurde (z. B. Anzahl neuer Fragen, neuer
   Dateipfad, aktualisierter Stand).

## Beispiele

```
/fragenkatalog setup
/fragenkatalog generate 50
/fragenkatalog add-category "Monetarisierung"
/fragenkatalog add-question "UI/UX" "Wie sieht das Onboarding für Erstnutzer aus?"
/fragenkatalog answer 17
/fragenkatalog export
/fragenkatalog stats
/fragenkatalog perspektive "Naughty Dog Narrative Director"
```

# Setup-Guide — MGD ToDo SKILL

## Voraussetzungen

- Claude Code (CLI) oder ChatGPT Codex
- Ein Projektordner mit Git (oder ohne)
- Ein Browser zum Öffnen der TODO.html

## Installation

### Option A: Global (Claude Code, empfohlen)

```bash
# Skill-Ordner anlegen
mkdir -p ~/.claude/skills/todo

# SKILL.md kopieren
curl -o ~/.claude/skills/todo/SKILL.md \
  https://raw.githubusercontent.com/MichaelGahnDESIGN/MGD_Todo_SKILL/main/SKILL.md
```

Danach ist `/todo` in jeder Claude-Code-Session verfügbar.

### Option B: Projekt-lokal (Claude Code)

```bash
# Im Projekt-Root
mkdir -p .claude/commands
curl -o .claude/commands/todo.md \
  https://raw.githubusercontent.com/MichaelGahnDESIGN/MGD_Todo_SKILL/main/SKILL.md
```

### Option C: ChatGPT Codex

```bash
mkdir -p .codex/commands
curl -o .codex/commands/todo.md \
  https://raw.githubusercontent.com/MichaelGahnDESIGN/MGD_Todo_SKILL/main/SKILL.md
```

Nutzung:
```bash
codex --instructions .codex/commands/todo.md "/todo"
```

## TODO.html anlegen

```bash
# Template ins Projekt kopieren
mkdir -p PROJEKT/TODO
curl -o PROJEKT/TODO/TODO.html \
  https://raw.githubusercontent.com/MichaelGahnDESIGN/MGD_Todo_SKILL/main/todo/TODO.template.html
```

Oder aus dem lokalen Klon:
```bash
cp path/to/MGD-ToDo-SKILL/todo/TODO.template.html PROJEKT/TODO/TODO.html
```

Die Vorlage enthält zwei Beispiel-Todos (`T001`/`T002`, Kategorie „beispiel"),
die zeigen, wie eine Zeile mit und ohne Unterkategorie aussieht. **Beide Zeilen
nach dem Kopieren löschen** — sonst stehen zwei Platzhalter in der Liste und das
erste echte Todo bekommt `T003`. `/todo-setup` erledigt das automatisch.

## Pfad konfigurieren

```
/todo-pfad PROJEKT/TODO/TODO.html
```

Oder manuell: Erstelle `PROJEKT/TODO/.todo-config` mit dem Pfad zur HTML-Datei (eine Zeile).

## Ersten Einsatz

```
/todo            # Übersicht anzeigen
/todo-add "Mein erstes richtiges Todo"
/todo-close T001
/todo-debug      # Strukturprüfung
```

## Bestehendes Projekt vom Altformat migrieren

Läuft im Projekt bereits eine `TODO.html` mit IDs im Format `T-001` (mit
Bindestrich) und festen Kategorien (`app`/`editor`/`backend`/…)? Das ist
das Format vor Version 1.0.0. Einmalig:

```
/todo-migrate
```

Das legt vorher eine Sicherungskopie an (`TODO.html.vor-migration-<datum>`),
stellt IDs auf `TNNN` um (auch in Querverweisen wie „siehe T-042"),
übernimmt Kopf/Filter/Skript aus der aktuellen Vorlage und behält alle
bestehenden Kategorien als Ausgangspunkt bei — Umbenennen oder Bündeln zu
neuen, freier gewählten Kategorien ist danach optional.

## HTML im Browser öffnen

Einfach `TODO.html` im Browser öffnen (Doppelklick oder via `open PROJEKT/TODO/TODO.html`).
Alle Funktionen (Suche, Filter, Sortierung) laufen lokal im Browser — kein Server nötig.

## Integration in bestehende Projekte

### Mit `/dev` kombinieren

Im DEV-Skill vor dem Deploy:
```
/todo            # Kritische offene Todos prüfen
/dev             # Deploy nur wenn keine Kritisch-Todos offen
```

### Mit `/playtest` kombinieren

Nach dem Playtest:
```
/todo-sync       # Neue Bugfix-Todos aus Test-Todo.md importieren
/todo            # Übersicht prüfen
```

### Mit `/projectclean` kombinieren

Am Release-Ende:
```
/todo-export     # Markdown-Liste für Release-Notes
/projectclean    # Aufräumen
```

## Tipps

- **Nie löschen**: Todos nur als `done` markieren — so bleibt die Geschichte erhalten
- **Secrets**: Niemals Passwörter, Tokens oder personenbezogene Daten in Todos schreiben
- **Committen**: TODO.html versionieren — so sieht man in Git, wann was erledigt wurde
- **IDs**: Sind fortlaufend (T001, T002, …) und werden nie wiederverwendet
- **Kategorien**: Sind Freitext — anlegen, was zum Projekt passt (z. B. „Sicherheit",
  „Datenschutz", „Features"), optional mit Unterkategorie. Der Knopf „🗂 Gruppieren"
  in der HTML zeigt sie als Baum an.

# Changelog

Versionsnummern folgen [Semantic Versioning](https://semver.org/lang/de/):
MAJOR bei Breaking Changes am HTML-/ID-Format, MINOR bei neuen Fähigkeiten
ohne Breaking Change, PATCH bei Fehlerbehebungen.

## 1.0.1 — 2026-09-01

### Behoben

- **`/todo-setup` ließ die Beispielzeilen der Vorlage stehen.** Die Vorlage
  liefert zwei Demo-Todos (`T001`/`T002`, Kategorie „beispiel"), aber weder
  `SKILL.md` noch `docs/setup.md` sagten, was damit geschehen soll. Wer sie
  stehen ließ, hatte zwei Platzhalter in der Liste, und das erste echte
  `/todo-add` vergab `T003` statt `T001`. `/todo-setup` entfernt beide Zeilen
  jetzt ausdrücklich und behält den erklärenden Kommentarblock im `tbody`.

## 1.0.0 — 2026-09-06

### Breaking Changes

- **ID-Format geändert:** `T-NNN` (mit Bindestrich) → `TNNN` (ohne
  Bindestrich), z. B. `T-004` → `T004`. Bestehende `TODO.html`-Dateien
  funktionieren weiter unverändert, sollten aber per neuem `/todo-migrate`
  aufs aktuelle Format gebracht werden.
- **Kategorien sind jetzt Freitext statt eines festen Enums.** Vorher fest:
  `app|editor|backend|infra|ux|playtest|doku`. Jetzt: beliebig anlegbar
  (z. B. „Sicherheit", „Datenschutz", „Features"), inklusive optionaler
  Unterkategorie. Die Filter-Dropdowns in der HTML füllen sich beim Öffnen
  automatisch aus den vorkommenden Werten. Datenattribut umbenannt:
  `data-kat` → `data-kategorie`, neu dazu: `data-unterkategorie` (optional).
- **Badge-Klassen für Kategorien vereinheitlicht:** alle alten `k-app`,
  `k-editor`, `k-backend`, `k-infra`, `k-ux`, `k-playtest`, `k-doku` sind
  entfallen, ersetzt durch die zwei generischen Klassen `k-cat` (Kategorie)
  und `k-subcat` (Unterkategorie) — die Farbe kennzeichnet jetzt „Kategorie
  vs. Unterkategorie", nicht mehr den konkreten Wert.

### Neu

- **`/todo-migrate`** — neuer Befehl, bringt eine bestehende `TODO.html` im
  Altformat automatisiert, mit Sicherungskopie und Validierung, aufs
  aktuelle Format.
- **Gruppieren-Ansicht:** neuer Knopf „🗂 Gruppieren" in der HTML zeigt alle
  Todos als Baum nach Kategorie › Unterkategorie, statt als flache
  sortierbare Liste. Rein clientseitig (kein Server, keine Einstellung
  pro Projekt).
- **Kurz-/Langbeschreibung in Notizen:** die Notizen-Spalte unterstützt jetzt
  optional `<details><summary>Kurzbeschreibung</summary>
  Langbeschreibung…</details>` — die Kurzbeschreibung bleibt beim Überfliegen
  der Liste immer sichtbar, die Langbeschreibung klappt per Klick auf.
  Reiner Text bleibt weiterhin gültig, wenn kein Bedarf für eine
  Langbeschreibung besteht.
- **Neuer Unterkategorie-Filter** in der HTML, dessen Optionen sich nach der
  gewählten Kategorie richten.

### Geändert

- `/todo-add`, `/todo-update`, `/todo-debug`, `/todo-export`, `/todo-sync`
  angepasst: Kategorie/Unterkategorie werden als Freitext behandelt statt
  aus einer festen Liste gewählt; `/todo-debug` erkennt zusätzlich
  Altformat-Reste (`T-NNN`-IDs, `data-kat`) und schlägt `/todo-migrate` vor.
- Platzhalter-Projektname in der Vorlage von „TINTLING" auf generisches
  „PROJEKT" geändert (`/todo-setup` ersetzt ihn ohnehin durch den echten
  Projektnamen — der alte Platzhalter war ein Namensrest aus der
  Entstehung des Skills und gehörte nicht in eine öffentliche Vorlage).

## 0.x — vor Changelog-Einführung

Frühere Änderungen sind in der Commit-Historie nachvollziehbar, aber nicht
einzeln in diesem Changelog aufgeführt.

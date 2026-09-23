# Changelog

## Unreleased

### Neu

- **`/todo-edit <id>`.** Bearbeitet alle Felder eines Todos: Titel, Priorität,
  Kategorie/Unterkategorie, Status (inkl. korrektem Setzen/Entfernen von
  `data-erledigt` und `row-done` je nach Richtung des Statuswechsels),
  Notizen und verknüpfte Links (`.todo-links`) — inklusive Entfernen oder
  Umbenennen bestehender Links, nicht nur Hinzufügen. `/todo-update` bleibt
  unverändert der kürzere Weg für reine Status-/Notiz-Änderungen.
- **Bearbeiten-Modal direkt in der TODO.html.** Jede Zeile bekommt einen
  ✏️-Knopf (neue Spalte „Aktionen", clientseitig ergänzt — funktioniert
  auch mit älteren, noch nicht migrierten Dateien). Öffnet ein Modal mit
  allen Feldern; „Speichern" schreibt die Änderung sofort sichtbar ins DOM
  zurück. Escape-Taste oder Klick außerhalb schließt das Modal ohne
  Änderung.
- **Genereller „💾 Speichern (Download)"-Knopf** in der Kopfzeile — bietet
  den aktuellen Browser-Stand jederzeit als `TODO.html`-Download an, nicht
  nur nach dem Aufräumen. Nach jeder Bearbeitung erscheint zusätzlich ein
  Hinweis-Banner mit demselben Download-Knopf, weil eine im Browser
  geöffnete HTML sich nicht selbst überschreiben kann (gleiches Muster wie
  beim bestehenden Aufräum-Knopf).
- **`data-bearbeitet`** — neues, optionales Attribut, das den Zeitpunkt der
  letzten Bearbeitung festhält (analog zu `data-erledigt`). Rein
  informativ, kein anderer Befehl wertet es aus; `data-erstellt` bleibt
  davon unberührt.
- **Begleit-Skill-Check in `/todo-setup`.** Am Ende des Setup-Dialogs prüft
  der Agent jetzt einmalig, ob die drei anderen Kern-Begleit-Skills
  (MGD_DEV_SKILL, Fragenkatalog-Skill, MGD_Living-Documentation) im Projekt
  oder global installiert sind, und fragt bei fehlenden aktiv nach, ob sie
  per `git clone` mitinstalliert werden sollen. Ergänzend im README ein neuer
  Abschnitt „Die 4 Kern-Begleit-Skills" mit den konkreten Zusammenspiel-Sätzen
  je Skill.

## 1.3.0 — 2026-09-20

### Neu

- **Dokumentationsindex in TODO.html.** Das Template besitzt jetzt eine optionale, von `/todo-index` gepflegte Projekt-Linkleiste.
- **`/todo-link`.** Todos können direkt auf Spezifikationen, Architektur, Rechtsrecherche, Issues oder andere Projektquellen verweisen.
- **`/todo-index`.** Baut einen kompakten Einstieg zu README, PRODUCT, CLAUDE, AGENTS, WIKI/DOCS und todo-relevanten Dokumenten.
- **`/todo-doc-init`.** Optionaler Wiki-Start für komplexe Projekte, ohne bestehende DOCS-Strukturen zu duplizieren.
- **`/todo-archive`.** Datierte Planungs-/Entscheidungsarchive mit der Regel, dauerhafte Entscheidungen zusätzlich in die aktuelle Fach-Doku zu übernehmen.
- **Link-Styles im HTML-Template.** Projektlinks und Todo-Links sind direkt klickbar und bleiben über die Volltextsuche auffindbar.

Versionsnummern folgen [Semantic Versioning](https://semver.org/lang/de/):
MAJOR bei Breaking Changes am HTML-/ID-Format, MINOR bei neuen Fähigkeiten
ohne Breaking Change, PATCH bei Fehlerbehebungen.

## 1.2.0 — 2026-09-19

### Neu

- **`/info` — Projekt-Status-Schnappschuss.** Beantwortet „wie ist der Stand?"
  in wenigen Zeilen: Git-Zustand (Branch, saubere/offene Arbeitskopie, letzter
  Commit, Abgleich mit dem Remote-Tracking-Branch), dieselbe Todo-Statistik
  wie am Ende von `/todo-debug`, und optional ein einfacher Statuscode-Check
  gegen eine erkennbare Live-URL. Ergänzt `/todo` (Fokus auf die Aufgaben-
  liste) um den Gesamtblick auf das Repo, ohne `git status`/`git log` von
  Hand zusammensuchen zu müssen.

## 1.1.1 — 2026-09-01

### Behoben

- **`/todo-migrate` übersprang Dateien auf 1.0er Stand.** Die Idempotenz-Prüfung
  fragte nur „schon `TNNN`-IDs und `data-kategorie`?" und meldete dann „bereits
  migriert". Eine Datei aus 1.0.x sieht strukturell korrekt aus, hat aber weder
  Zeitstempel noch die Knöpfe zum Ausblenden und Aufräumen aus 1.1.0 — sie wäre
  für immer auf dem alten Funktionsstand geblieben. `/todo-migrate` bestimmt
  jetzt drei Stände (Altformat / 1.0er Stand / aktuell) und erneuert beim 1.0er
  Stand Kopf, Fuß und Skript und trägt `data-erstellt` nach.

## 1.1.0 — 2026-09-01

### Neu

- **Zeitstempel an jedem Todo.** Neue Attribute `data-erstellt` (Anlegen) und
  `data-erledigt` (Erledigung, nur bei done-Zeilen), jeweils
  `YYYY-MM-DDTHH:MM`. Die Datumsspalte zeigt bei erledigten Zeilen zusätzlich
  `✓ Erledigungsdatum`. Ältere Dateien ohne diese Attribute bleiben gültig:
  fehlt `data-erstellt`, gilt der Text der Datumsspalte.
- **Erledigte aus- und einblenden.** Neuer Knopf „✓ Erledigte ausblenden" in
  der HTML. Wirkt zusätzlich zu Suche und Filtern, ändert nichts an der Datei,
  Standard ist eingeblendet.
- **Aufräum-Knopf „🧹 Aufräumen".** Entfernt erledigte Todos, deren Erledigung
  mehr als einen Monat zurückliegt. Da eine im Browser geöffnete HTML sich nicht
  selbst speichern kann, entfernt der Knopf die Zeilen in der Ansicht und lädt
  anschließend eine bereinigte `TODO.html` herunter, die die bestehende Datei
  ersetzen muss. Zeilen ohne `data-erledigt` werden nie erfasst.
- **`/todo-cleanup`** — dasselbe Aufräumen direkt an der Datei, mit
  Sicherungskopie und wählbarem Zeitraum (`/todo-cleanup 3monate`).

### Geändert

- **Sicherheitsregel „Niemals löschen" geschärft.** Sie galt bisher pauschal und
  hätte das Aufräumen ausgeschlossen. Jetzt getrennt: *offene* Todos werden nie
  gelöscht, *erledigte* dürfen nach einer Aufbewahrungsfrist raus — mit
  Sicherung, ohne Neuvergabe der IDs.
- `/todo-add` setzt `data-erstellt`, `/todo-close` setzt `data-erledigt`.
  `/todo-debug` prüft beide und meldet fehlende Werte. `/todo-migrate` trägt
  `data-erstellt` aus der Datumsspalte nach; `data-erledigt` bleibt bei
  Altzeilen bewusst leer, weil es sich nicht rekonstruieren lässt.

### Behoben

- **`.claude/commands/todo.md` und `.codex/commands/todo.md` liefen auseinander.**
  Beide sind Kopien der `SKILL.md`, wurden aber in 1.0.1 nicht mitgezogen und
  hingen eine Version zurück. Jetzt wieder deckungsgleich.

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

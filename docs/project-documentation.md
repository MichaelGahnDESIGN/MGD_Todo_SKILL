# Projektdokumentation mit dem TODO-Skill

Stand: 20.09.2026

Der TODO-Skill kann bei kleinen Projekten weiterhin nur eine TODO.html verwalten. Bei komplexen Projekten darf er zusätzlich als Navigationsschicht zwischen Aufgaben und Dokumentation dienen.

## Ziel

Ein Agent soll nicht nur wissen, was offen ist, sondern direkt sehen, warum ein Todo existiert und welche aktuelle Spezifikation dazu gehört.

## Empfohlene Struktur

~~~text
PROJEKT/
  README.md
  PRODUCT.md
  CLAUDE.md
  AGENTS.md
  TODO/
    TODO.html
    .todo-config
  WIKI/
    README.md
    00-PROJEKT/
    01-ENTSCHEIDUNGEN/
    02-ARCHITEKTUR/
    03-PRODUKT/
    04-ROADMAP/
    05-RECHT/
    08-ARCHIV/
    09-OFFENE-FRAGEN/
~~~

Die Struktur ist bewusst nur eine Empfehlung. Bestehende DOCS- oder docs-Verzeichnisse werden respektiert.

## Drei Ebenen

### Aktuelle Spezifikation

Fachseiten, Architektur, Produktentscheidungen und Roadmap. Diese beschreiben, was heute gelten soll.

### Operative Todos

TODO.html enthält konkrete Arbeit und verlinkt auf die aktuelle Spezifikation.

### Archiv

Datierte Gesprächsstände, Übergaben und Entscheidungen. Ein Archiv ist Historie und darf nicht die einzige Quelle einer noch gültigen Entscheidung sein.

## Link-Regel

Ein Todo bekommt nur dann Links, wenn sie für seine Umsetzung oder Prüfung wirklich relevant sind. Keine Link-Sammlung um der Link-Sammlung willen.

Geeignete Beispiele:

* Upload-Todo → Upload-Spezifikation
* Datenbankmigration → Architektur/Datenmodell
* Stripe-Todo → Monetarisierung und Recht
* Moderation → Moderationskonzept und DSA-Recherche

## Sicherheit

Nie indexieren oder verlinken:

* .env
* Passwortdateien
* API-Secrets
* SSH-Zugänge
* private Backups
* persönliche Geheimnisse

## Agenten-Kooperation

Vor Änderungen an TODO oder Dokumentation den aktuellen Stand lesen. Nach einer Produktentscheidung zuerst die aktuelle Fachseite aktualisieren, dann Todo/Archiv. So können Claude Code und Codex kooperieren, ohne dass ein älterer Chat die neuere Spezifikation überschreibt.

# Projektdokumentation mit dem TODO-Skill

Stand: 08.11.2026

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

## Verhältnis zu MGD_Living-Documentation

Die oben beschriebene WIKI-Struktur (`00-PROJEKT/` … `09-OFFENE-FRAGEN/`) ist
eine leichtgewichtige, projekteigene Variante. Wer stattdessen eine
vollständige lebendige Dokumentation mit Entscheidungs-, Risiko- und
Prüfnachweis-Modell will, findet das im eigenständigen Skill
[MGD_Living-Documentation](https://github.com/MichaelGahnDESIGN/MGD_Living-Documentation)
— beide schließen sich nicht aus. Ist Living-Documentation im Projekt
installiert, zeigt `/todo-link` sinnvollerweise auf deren Entscheidungs- oder
Risiko-Abschnitte statt auf eine eigene `01-ENTSCHEIDUNGEN/`-Seite, damit es
nur eine kanonische Quelle je Entscheidung gibt.

Die Living Documentation ist damit nicht nur ein optionaler Begleit-Skill,
sondern Teil des öffentlichen `/todo`-Workflows: TODO verwaltet den
Arbeitsstatus, die Living Documentation den dauerhaften fachlichen Nachweis.
Bei relevanten Änderungen wird zuerst die kanonische Fachseite aktualisiert
und anschließend das Todo verlinkt oder geschlossen. Ein lokaler Stand, ein
Git-Commit, ein GitHub-Push und ein Deployment bleiben getrennte Nachweise.
Private oder externe Living-Documentation-Speicherorte werden dabei nicht
automatisch in ein Repository kopiert oder veröffentlicht.

## Zusammenhängender Abgleich mit `/todo-doku`

`/todo-doku [Thema]` bündelt diesen Ablauf in einem eigenen Agentenbefehl:
Projektregeln und vorhandene Änderungen lesen, die zuständige Fachseite
aktualisieren, die passende Todo-ID abgleichen und den vorhandenen lokalen
Graphify-Befehl ausführen. Die vollständige Anweisung liegt in
[`skills/todo-doku/SKILL.md`](../skills/todo-doku/SKILL.md).

Der Befehl erzeugt keine zweite Wissensablage und macht eine Aufgabe erst
bei einem belegten Ergebnis erledigt. Secrets, private Backups und vom
Projekt geschützte Ordner bleiben ausgeschlossen. Commit, Push,
Wikiveröffentlichung und Deployment benötigen einen gesonderten Auftrag.

### Playbook und Rückweg für die Integration vom 08.11.2026

Ziel: PR #2 auf den aktuellen Hauptbranch übernehmen und als v1.4.0 nutzbar
veröffentlichen. Erst die Claude-/Codex-Dateien mit dem kanonischen Skill
vergleichen und die dokumentierte Installation in einem leeren Testprojekt
prüfen. Danach PR mergen, nur versionierte Veröffentlichungsdateien als ZIP
packen und den Download per SHA-256 gegen das lokale Paket prüfen.

Der vorhandene Stand vor der Integration ist Commit
`9869a1d2ad5c883d2e72d3207c25d690d9cade4c`. Bei Problemen den
Integrationscommit gezielt zurücknehmen und die zuvor installierte
Skill-Fassung weiterverwenden; keine fremden Projektdateien überschreiben.
Für diese Anweisungs- und Dokumentationsänderung sind keine produktiven
Daten betroffen und kein Website- oder Datenbank-Backup nötig.

Geprüft: kanonischer Skill, Claude- und Codex-Befehl sind bytegleich. Die
projektlokale Installation wurde in einem leeren temporären Zielordner mit
Leerzeichen geprüft; die vier Doku-Einstiege und ihre lokalen Skill-Links
sind vorhanden. Alle neun vorhandenen Pfadfinder-Tests sowie
`git diff --check` bestanden. Ein echter KI-Agentenlauf wurde dafür nicht
gestartet; sein Ergebnis hängt weiterhin von Projektregeln und verfügbaren
Werkzeugen des Zielprojekts ab.

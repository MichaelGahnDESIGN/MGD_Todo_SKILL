---
name: wissen
description: >-
  Aktualisiert den nachweisbaren Wissensstand eines Projekts abgestimmt in
  TODO, Graphify und Living Documentation. Für /wissen, Wissenspflege nach
  Änderungen sowie verständliche README- und Wiki-Updates.
metadata:
  version: 1.1.0
  integration:
    - todo
    - graphify
    - living-documentation
---

# /wissen – Projektwissen aktualisieren

`/wissen` räumt nach einer Änderung das Wissen zu **einem aktuellen Projekt**
auf. Es erzeugt keine zweite Dokumentation und aktualisiert nicht blind alle
Repositories. Der Auftrag lautet: Was ist getan, was ist offen und wo steht die
verlässliche Erklärung dazu?

## Die drei Orte haben verschiedene Aufgaben

| Ort | Beantwortet | Nicht dafür gedacht |
| --- | --- | --- |
| `/todo` | Was ist als Nächstes zu tun? | Lange Erklärungen und Architektur |
| `/graphify` | Welche Dateien und Bereiche hängen zusammen? | Funktions- oder Live-Nachweise |
| Living Documentation | Was gilt, warum gilt es und was wurde belegt? | Eine zweite Aufgabenliste |

Das persönliche `MGD_AI-Knowledge_VAULT` ist ein separater, privater
Wissensspeicher. Dort landen wiederverwendbare Erkenntnisse und Profile, aber
keine automatisch kopierten Projektdetails oder Secrets.

## Ablauf

1. **Erst verstehen.** Lies Projektregeln, Git-Status, vorhandene README,
   Wiki und die kanonische Living Documentation. Ermittle vorhandene Pfade
   statt neue Ordner nach Gefühl anzulegen.
2. **Belege sammeln.** Notiere nur tatsächliche Änderungen, Commits, Tests und
   sichtbare Prüfungen. Ein lokaler Build, Git-Push und Live-Stand sind
   getrennte Nachweise.
3. **TODO aktualisieren.** Suche eine konfigurierte `TODO.html` oder
   `.todo-config`. Erledigte Arbeit auf `done` setzen, neue echte Restarbeit
   als Todo erfassen und auf die passende Dokumentation verlinken. Keine
   Aufgaben als erledigt markieren, wenn nur geplant oder vermutet wurde.
4. **Graph aktualisieren.** Wenn Graphify installiert und für das Projekt
   eingerichtet ist, führe `graphify update . --no-cluster` aus. Prüfe den
   Diff der erzeugten Graph-Dateien auf unerwartete entfernte Knoten, Kanten
   oder Reihenfolgeänderungen. Ein Graph ist eine Strukturkarte, kein Test.
   Fehlt Graphify oder eine Projektkonfiguration, halte das als offenen Punkt
   fest; installiere es nicht ungefragt.
5. **Living Documentation aktualisieren.** Ergänze nur die betroffenen
   Aussagen als bestätigten Stand, Entscheidung, offenen Punkt oder Risiko.
   Testumfang und Grenzen klar nennen. Veraltete Aussagen korrigieren oder als
   historisch markieren, statt widersprüchliche Duplikate anzulegen.
6. **README und Wiki verständlich halten.** Erkläre für einen DAU zuerst Ziel,
   Nutzen und den einfachsten Start. Fachbegriffe kurz erklären. Anleitungen
   bleiben als kurze Schritte lesbar; interne Details, Secrets und private
   Betriebsdaten gehören nie hinein.
7. **Prüfen und berichten.** Prüfe Git-Diff, Markdown-Links und die jeweils
   geänderte Hauptfunktion. Nenne ausdrücklich, was nicht geprüft wurde.

## Einheitliche Statuszeichen

Nutze die Zeichen sparsam und konsistent in Antworten, TODOs, READMEs, Wikis
und Living Documentation:

| Zeichen | Bedeutung |
| --- | --- |
| ✅ | Erledigt und passend belegt |
| ☑️ | Noch offen oder nächster konkreter Schritt |
| ❓ | Frage an Michael, die eine Entscheidung braucht |
| ⚠️ | Wichtiger Hinweis, Risiko oder Grenze |
| ℹ️ | Sachliche Zusatzinformation |

Die Symbole ersetzen keine Aussage über Tests oder Bereitstellung. Nach einem
✅ steht daher bei Bedarf kurz, wodurch der Zustand belegt ist.

## Sicherheitsgrenzen

- Keine Passwörter, Tokens, personenbezogenen Daten, Backups oder privaten
  Infrastrukturdetails in TODOs, Graphen, READMEs, Wikis oder Dokumentation.
- Keine Veröffentlichung, Live-Änderung oder Wiki-Synchronisation allein durch
  `/wissen`. Dafür gelten die Projektfreigaben.
- Bei widersprüchlichen Quellen bleibt der Konflikt ein ⚠️ offener Befund, bis
  der tatsächliche Stand geprüft ist.

## Gemeinsame Veröffentlichung

`/wissen` gehört bewusst zu **MGD_Todo_SKILL** und
**MGD_Living-Documentation**. Der Todo-Skill verantwortet die konkrete
Restarbeit, Living Documentation die dauerhafte Erklärung. Deshalb müssen
inhaltliche Änderungen am Skill in beiden öffentlichen Repositories, ihren
READMEs und den dortigen Wiki-Texten im selben Arbeitsblock nachvollziehbar
nachgezogen werden. Der lokale Skill bleibt mit derselben Fassung synchron.

Das bedeutet nicht, dass eine GitHub-Wiki-Seite automatisch veröffentlicht
wird: Eine lokale `wiki/`-Kopie ist nur die versionierbare Quelle. Eine
separate Wiki-Synchronisation oder ein Release braucht weiterhin einen
ausdrücklichen Auftrag.

## Abschlussformat

```text
✅ Aktualisiert: <konkrete Dateien oder Bereiche>
✅ Geprüft: <tatsächliche Prüfung und Ergebnis>
☑️ Offen: <echter Restpunkt oder „keine“>
⚠️ Grenze: <nicht geprüftes Ziel oder Risiko>
```

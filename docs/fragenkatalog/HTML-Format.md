# HTML-Format / Datenmodell

## Kanonisches Zwischenformat

Während der Bearbeitung durch den Agenten liegt der Fragenkatalog als `fragenkatalog.json` vor —
ein flaches JSON-Array:

```json
[
  {
    "id": 1,
    "category": "Kern-Loop",
    "question": "Was ist die zentrale Spielhandlung, die der Spieler alle 30–60 Sekunden wiederholt?",
    "kiAnswer": "Baue einen klaren Ressourcen-Sammeln → Craften → Verbessern-Loop ...",
    "userAnswer": ""
  },
  {
    "id": 2,
    "category": "Recht",
    "question": "Welche Altersfreigabe ist für ein Sammel-/Gacha-Mobile-Game in der EU zu erwarten?",
    "kiAnswer": "In der EU prüft PEGI Zufallsmechaniken (Lootboxen) inzwischen gesondert; je nach Ausgestaltung ist mit PEGI 12–16 zu rechnen, zusätzlich ggf. Hinweispflicht 'beinhaltet Zufallsgegenstände'. Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen einen Anwalt/Fachberater für Jugendschutzrecht, EU konsultieren.",
    "userAnswer": ""
  }
]
```

## Export in die HTML

`/fragenkatalog-export` liest `templates/Fragenkatalog.template.html`, ersetzt darin die Zeile

```js
const COMPLETE_DATA = [];
```

durch das aktuelle Array aus `fragenkatalog.json` und schreibt das Ergebnis an den in
`.fragenkatalog-config` hinterlegten `outputPath`. Die Datei ist danach vollständig
self-contained (kein CDN, kein externer Request) und funktioniert offline als lokale `file://`-
Datei.

## Aufbau der Seite

- **Toolbar**: Kategorie-Filter-Dropdown (mit Fragenanzahl je Kategorie, Rechts-Kategorie mit
  `⚖️`-Präfix), Volltextsuche, Edit-Modus-Toggle, "Neue Frage"-Button (nur im Edit-Modus),
  Export-/Import-Buttons.
- **Statistik-Zeile**: Gesamtanzahl, Anzahl mit eigener Antwort, Anzahl offen, aktuell angezeigt.
- **Tabelle**: Kategorie | Frage (rot) | KI-Antwort (blau `💙`, bei Recht amberfarben `⚖️` +
  Disclaimer) | Eigene Antwort | Aktionen (nur im Edit-Modus).
- **Modal**: Kategorie-Dropdown, Frage-/KI-Antwort-/Eigene-Antwort-Textareas,
  Speichern/Löschen/Abbrechen.

## Wichtige JavaScript-Funktionen

| Funktion | Zweck |
|---|---|
| `initData()` | Lädt Daten aus `localStorage`, sonst Deep Copy von `COMPLETE_DATA` |
| `renderTable()` | Rendert gefilterte Zeilen + Statistik |
| `filterTable()` | Liest Kategorie-Filter + Suchfeld |
| `toggleEditMode()` | Schaltet Edit-Modus um |
| `openEditModal(id)` / `openAddModal()` | Öffnet Modal befüllt bzw. leer |
| `saveEdit()` | Validiert, schreibt State, persistiert, rendert neu |
| `deleteCurrentRow()` | Löscht mit Sicherheitsabfrage |
| `addNewRow()` | Öffnet Add-Modal |
| `exportData()` | Lädt State als JSON-Datei herunter |
| `importData(file)` | Liest/validiert JSON-Datei, merge oder ersetzen |
| `escapeHtml(str)` | XSS-Schutz — jede Ausgabe von Nutzer-/KI-Text läuft hier durch |
| `formatKiAnswer(row)` | Wählt Präfix (`💙`/`⚖️`) und hängt bei Recht-Kategorie den Disclaimer an, falls er fehlt |
| `isLegalCategory(category)` | Prüft Kategorienamen gegen `LEGAL_CATEGORY_NAMES` |

## Persistenz

`localStorage`-Schlüssel: `fragenkatalog_data_v1`. Änderungen im Browser (Edit-Modus) werden
sofort gespeichert und überleben einen Reload — bleiben aber lokal im jeweiligen Browser
(siehe Abschnitt "Grenzen" im README). `COMPLETE_DATA` selbst wird nie mutiert; die Anzeige
arbeitet immer mit einer Kopie im internen State.

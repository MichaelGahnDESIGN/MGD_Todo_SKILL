---
name: fragenkatalog
description: Erstellt und pflegt einen Fragenkatalog für ein Projekt (durchsuchbare HTML-Datei mit KI-Antworten aus Experten-Perspektiven und Feld für die eigene Antwort). Für /fragenkatalog, Fragen sammeln, Konzeptfragen beantworten, exportieren.
---

# Fragenkatalog-Skill — Spezifikation

> Dieser Skill erstellt und pflegt einen **Fragenkatalog** für ein beliebiges Projekt (Spiel, App,
> Website, Buch, Business-Plan, Produktdesign, Marketingkampagne, ...): eine durchsuchbare,
> kategorisierte Liste aller wichtigen Design-/Konzeptfragen, zu jeder Frage sofort eine
> KI-Antwort aus einer frei wählbaren Experten-Perspektive, plus ein leeres Feld für die eigene,
> endgültige Antwort des Projektinhabers. Ergebnis ist eine einzelne self-contained HTML-Datei
> (kein Server, keine Abhängigkeiten, funktioniert offline), die als lebendiges Nachschlagewerk
> im Projekt-Repo abgelegt wird.

## Datenmodell (kanonisches Zwischenformat)

Jede Frage ist ein Objekt mit genau diesen vier (+ id) Feldern:

```json
{
  "id": 1,
  "category": "Kern-Loop",
  "question": "Was ist die zentrale Spielhandlung, die der Spieler alle 30–60 Sekunden wiederholt?",
  "kiAnswer": "Baue einen klaren Ressourcen-Sammeln → Craften → Verbessern-Loop ...",
  "userAnswer": ""
}
```

- `id` — fortlaufende Ganzzahl, eindeutig innerhalb der Datei.
- `category` — Kategorie-Name (String, wird für Filter/Gruppierung genutzt).
- `question` — die Frage selbst (rot dargestellt).
- `kiAnswer` — die KI-Antwort aus der gewählten Experten-Perspektive (blau, mit Präfix-Emoji,
  z. B. `💙 `). Wird beim Rendern in der HTML mit diesem Präfix versehen; im JSON selbst steht
  nur der reine Text.
- `userAnswer` — die eigene, endgültige Antwort des Projektinhabers (schwarz/normal). Bleibt bei
  der Generierung leer und wird vom Nutzer selbst (im Browser, im Edit-Modus) oder über
  `/fragenkatalog-answer` befüllt.

Dieses JSON-Array ist die "Quelle der Wahrheit" während der Bearbeitung durch den Agenten (liegt
als `fragenkatalog.json` neben der Konfigurationsdatei) und wird 1:1 als
`const COMPLETE_DATA = [...]` in die exportierte HTML eingebettet (siehe `/fragenkatalog-export`).

## Rechts-Kategorie und Disclaimer-Pflicht (WICHTIG)

Jeder Fragenkatalog — unabhängig vom Projekttyp — soll eine Kategorie **"Recht"** (bzw.
**"Rechtliches"**) enthalten, die typische rechtliche Recherchefragen für das jeweilige Projekt
abdeckt. Diese Kategorie darf bei `/fragenkatalog-setup` und `/fragenkatalog-generate` **nicht
kommentarlos fehlen** — sie wird immer mitgeneriert, es sei denn, der Nutzer lehnt sie beim Setup
ausdrücklich ab (siehe `/fragenkatalog-setup` unten).

Typische Themen, aus denen der Agent je nach `projectType` (und ggf. `platforms`) sinnvoll
auswählt:

- **Spiele**: Jugendschutz/Alterseinstufung (USK, PEGI, ESRB je nach Zielmarkt),
  Lootbox-/Glücksspielrecht, Plattform-Richtlinien (Apple App Store, Google Play, Steam, Xbox,
  PlayStation), Urheberrecht bei Assets/Musik/Fonts/Third-Party-Content, Markenrecht
  (Titel-/Namenskollision prüfen), AGB/EULA, Impressumspflicht, DSGVO bei Online-Features/
  Accounts/Analytics/Werbung, regionale Altersfreigaben und Exportbeschränkungen.
- **Apps/Software**: DSGVO/Datenschutzerklärung, Cookie-Consent, AGB/Nutzungsbedingungen,
  Impressumspflicht (z. B. § 5 DDG/TMG in Deutschland), Barrierefreiheitsgesetz (BFSG) bei
  EU/DE-Markt, App-Store-Richtlinien-Compliance, Lizenzrecht bei verwendeten
  Open-Source-Abhängigkeiten, Zahlungsabwicklung/PSD2 falls relevant.
- **Bücher/kreative Werke**: Urheberrecht, Zitatrecht, Persönlichkeitsrechte bei realen Vorbildern
  oder Ortsangaben, typische Verlagsvertragsklauseln, Pseudonym-/Namensrecht.
- **Business/Startups**: Gesellschaftsform, Gewerbeanmeldung, Haftungsfragen, Vertragsrecht mit
  Partnern/Lieferanten, branchenspezifische Regularien, Datenschutz bei Kundendaten.
- Für andere Projekttypen leitet der Agent 3–8 passende Rechtsthemen selbst her, nach demselben
  Prinzip wie bei den übrigen Kategorien in `/fragenkatalog-generate`.

### Eigenes Antwort-Format für Rechtsfragen

Anders als bei allen anderen Kategorien, wo die gewählte Experten-Persona (z. B. "Blizzard
Entertainment Game Designer") frei und kreativ mit dem Standard-Präfix (Default `💙`) antwortet,
gilt für die Kategorie "Recht"/"Rechtliches" ein eigenes, striktes Format:

- **Eigenes Präfix**: `⚖️` (Waage-Emoji) statt des normalen KI-Präfixes. Im Template als Konstante
  `LEGAL_PREFIX` hinterlegt, analog zu `KI_PREFIX` aber fest zugeordnet zur Rechts-Kategorie (nicht
  in `.fragenkatalog-config` überschreibbar, da die rechtliche Kennzeichnung immer eindeutig
  erkennbar bleiben muss).
- **Pflicht-Disclaimer**: Jede `kiAnswer` in der Rechts-Kategorie MUSS mit folgendem Satz enden
  (wortwörtlich oder sinngemäß mit gleichem Inhalt):
  > "Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für
  > verbindliche Aussagen einen Anwalt/Fachberater für [konkretes Rechtsgebiet, Land]
  > konsultieren."

  Der Agent ersetzt `[konkretes Rechtsgebiet, Land]` durch eine passende Konkretisierung (z. B.
  "Jugendschutzrecht, Deutschland" oder "Urheberrecht, EU"), wo möglich.
- **Inhaltlicher Stil**: Rechts-Antworten sind **Rechercherichtungen**, keine verbindlichen
  Aussagen — sie benennen relevante Gesetze/Regularien/Anlaufstellen und typische Fallstricke,
  formulieren aber keine Garantien ("ist erlaubt", "ist verboten") ohne Einschränkung. Beispiel-
  Formulierung: "Für [Thema] ist in Deutschland typischerweise [Gesetz/Regularie] relevant; prüfe
  insbesondere [Aspekt]. [Disclaimer-Satz]".
- Das Template (`templates/Fragenkatalog.template.html`) erkennt Rechts-Zeilen automatisch anhand
  des Kategorienamens (case-insensitive: "Recht", "Rechtliches", "Rechtsfragen") über die
  Konstante `LEGAL_CATEGORY_NAMES`, hängt den Disclaimer beim Rendern automatisch an falls er in
  den Rohdaten fehlt (`formatKiAnswer()`), zeigt das Waage-Emoji im Kategorie-Filter und in der
  Kategorie-Spalte, und stellt die KI-Antwort in einer eigenen Akzentfarbe (Amber/Gold-Orange,
  `--amber`) statt Blau dar, um sie optisch klar von Design-Antworten zu unterscheiden.
- Beim Generieren (`/fragenkatalog-generate`, `/fragenkatalog-add-category "Recht"`,
  `/fragenkatalog-answer`) formuliert der Agent Rechts-Antworten selbst bereits inklusive
  Disclaimer-Satz in `kiAnswer` — das Template hängt ihn nur als Sicherheitsnetz an, falls er
  fehlt.

## Konfigurationsdatei `.fragenkatalog-config`

Wird von `/fragenkatalog-setup` angelegt, JSON-Format, im Projekt-Root:

```json
{
  "projectName": "Sternenfänger",
  "projectType": "Mobile Game",
  "platforms": ["iOS", "Android"],
  "perspective": "Blizzard Entertainment Lead Game Designer",
  "perspectivePrefix": "💙",
  "outputPath": "docs/Fragenkatalog.html",
  "dataPath": "docs/fragenkatalog.json",
  "language": "de",
  "includeLegalCategory": true,
  "createdAt": "2026-09-23"
}
```

Alle Befehle lesen/schreiben diese Datei. Existiert sie nicht, verlangen alle Befehle außer
`/fragenkatalog-setup` zuerst den Aufruf von `/fragenkatalog-setup` (freundlicher Hinweis, kein
Fehlerabbruch).

## Befehle

### `/fragenkatalog-setup`

Interaktiver Ersteinrichtungs-Assistent. Fragt nacheinander (oder in einem Rutsch, wenn der
Nutzer alles auf einmal angibt):

1. **Projektname und Projekttyp** — frei formuliert (z. B. "Sternenfänger, ein Mobile-Sammelspiel"
   oder "Kochbuch-App für Familien"). Der Agent leitet daraus einen groben Projekttyp ab (Spiel,
   App, Website, Buch/Roman, Sachbuch, Business-Plan, Produktdesign, Marketingkampagne,
   Sonstiges) — bei Unklarheit nachfragen.
2. **Zielplattform(en)** — nur relevant bei Software/Spielen (z. B. iOS, Android, Web, Desktop,
   Konsole). Bei Büchern/Business-Plänen überspringen.
3. **Experten-Perspektive** — frei wählbar. Der Agent schlägt 3–5 Defaults passend zum Projekttyp
   vor und lässt den Nutzer wählen oder eine eigene Formulierung eingeben:
   - Spiel: "Blizzard Entertainment Lead Game Designer", "Naughty Dog Narrative Director",
     "Nintendo EPD Produzent"
   - App: "Ehemaliger Apple Human Interface Designer", "Y Combinator Startup-Berater",
     "Head of Product bei einem Series-B-Startup"
   - Buch/Roman: "Erfahrener Verlagslektor", "Bestseller-Autor im gewählten Genre"
   - Business: "Y Combinator Partner", "Erfahrener Unternehmensberater (McKinsey-Stil)"
   - Sonstiges: allgemein "Erfahrener Senior-Berater im jeweiligen Fachgebiet"

   Zusätzlich: welches Präfix-Emoji soll KI-Antworten kennzeichnen (Default `💙`, frei änderbar).
4. **Speicherpfad** der finalen HTML-Datei (Default-Vorschlag: `docs/Fragenkatalog.html` im
   Projekt-Root) — analog zu `.todo-config` bei MGD_Todo_SKILL, hier `.fragenkatalog-config`.
5. **Sprache** des Katalogs (Default: Sprache des Projekts/der Konversation, meist Deutsch).
6. **Rechts-Kategorie einschließen?** — Default: Ja. Der Agent weist kurz darauf hin, dass eine
   Kategorie "Recht" mit projekttypischen Rechercheragen (siehe Abschnitt "Rechts-Kategorie und
   Disclaimer-Pflicht" oben) automatisch mit angelegt wird, inkl. Disclaimer-Hinweis, dass dies
   keine Rechtsberatung ersetzt. Nur bei ausdrücklicher Ablehnung durch den Nutzer wird sie
   weggelassen — speichere diese Entscheidung als `includeLegalCategory: true|false` in
   `.fragenkatalog-config`.
7. **Begleit-Skills-Check (einmalig)** — Der Fragenkatalog-Skill ist Teil einer Familie von vier
   zusammengehörigen MGD-Skills (siehe auch [README.md](README.md#verwandte-mgd-projekte)):
   **MGD_DEV_SKILL**, **Fragenkatalog-Skill** (dieser hier), **MGD_Todo_SKILL** und
   **MGD_Living-Documentation**. Nach der bisherigen Konfiguration (Schritte 1–6) prüft der Agent
   aktiv, ob die drei anderen Skills im aktuellen Projekt oder global bereits installiert sind, und
   bietet fehlende Skills zur Mitinstallation an. Dies ist eine echte Prüfung mit konkreten
   Datei-/Ordnerpfaden, kein reiner Prosa-Hinweis.

   **a) Prüfpfade je Skill** (zuerst projekt-lokal relativ zum aktuellen Arbeitsverzeichnis prüfen,
   dann global im Home-Verzeichnis des Nutzers; sobald einer der Pfade existiert, gilt der Skill
   als installiert):

   | Skill | Projekt-lokal (Claude Code / Codex) | Global (Claude Code / Codex) |
   |---|---|---|
   | MGD_DEV_SKILL | `.claude/commands/dev.md` / `.codex/commands/dev.md` oder `.claude/skills/dev/SKILL.md` / `.codex/skills/dev/SKILL.md` | `~/.claude/skills/dev/SKILL.md` / `~/.codex/skills/dev/SKILL.md` oder `~/.claude/commands/dev.md` / `~/.codex/commands/dev.md` |
   | MGD_Todo_SKILL | `.claude/commands/todo.md` / `.codex/commands/todo.md` oder `PROJEKT/TODO/.todo-config` | `~/.claude/skills/todo/SKILL.md` / `~/.codex/skills/todo/SKILL.md` |
   | MGD_Living-Documentation | `.claude/skills/living-documentation/SKILL.md` / `.codex/skills/living-documentation/SKILL.md` (bzw. `.agents/skills/living-documentation/SKILL.md`) | `~/.claude/skills/living-documentation/SKILL.md` / `~/.codex/skills/living-documentation/SKILL.md` |

   Der Agent prüft diese Pfade konkret (z. B. per Datei-/Verzeichnis-Existenzcheck), nicht durch
   bloßes Nachfragen beim Nutzer.

   **b) Fehlende Skills aktiv anbieten** — Fehlt einer oder mehrere der drei Skills (kein Pfad aus
   der Tabelle gefunden), fragt der Agent für jeden fehlenden Skill einzeln nach:

   > "Ich habe festgestellt, dass [Skill X] in diesem Projekt noch nicht installiert ist. Er
   > ergänzt [Nutzen]. Soll ich ihn jetzt mitinstallieren? (ja/nein)"

   mit folgender Nutzen-Kurzfassung je Skill:

   - **MGD_DEV_SKILL**: "Release/Sync/Backup/Cleanup/Tests/Wissensdokumentation rund um dieses
     Projekt — hält u. a. den Fragenkatalog-Stand vor einem Release als Teil der
     Projekt-Wissensdokumentation fest."
   - **MGD_Todo_SKILL**: "eine selbst-gehostete `TODO.html` mit Bearbeiten-Funktion, in die
     unbeantwortete Fragen aus diesem Fragenkatalog als Todos exportiert werden können."
   - **MGD_Living-Documentation**: "eine lebendige Projektdokumentation (Entscheidungen, offene
     Punkte, Risiken, Testnachweise), in die unbeantwortete Fragen aus diesem Fragenkatalog als
     offene Punkte übernommen werden können."

   **c) Bei Zustimmung installieren** — der Agent klont das jeweilige Repo und kopiert gemäß der in
   diesem Repo dokumentierten Zielstruktur (Claude Code, projekt-lokal; Codex analog unter
   `.codex/...`):

   ```bash
   # MGD_DEV_SKILL
   git clone https://github.com/MichaelGahnDESIGN/MGD_DEV_SKILL.git /tmp/mgd-dev-skill-install
   mkdir -p .claude/skills && cp -R /tmp/mgd-dev-skill-install/dev .claude/skills/dev
   mkdir -p .claude/commands && cp /tmp/mgd-dev-skill-install/.claude/commands/*.md .claude/commands/
   # Codex analog: .codex/skills/dev + .codex/commands/*.md aus /tmp/mgd-dev-skill-install/.codex/commands/

   # MGD_Todo_SKILL
   git clone https://github.com/MichaelGahnDESIGN/MGD_Todo_SKILL.git /tmp/mgd-todo-skill-install
   mkdir -p PROJEKT/TODO && cp /tmp/mgd-todo-skill-install/todo/TODO.template.html PROJEKT/TODO/TODO.html
   mkdir -p .claude/skills/todo && cp /tmp/mgd-todo-skill-install/SKILL.md .claude/skills/todo/SKILL.md
   mkdir -p .claude/commands && cp /tmp/mgd-todo-skill-install/.claude/commands/todo.md .claude/commands/
   # Codex analog: .codex/skills/todo + .codex/commands/todo.md

   # MGD_Living-Documentation
   git clone https://github.com/MichaelGahnDESIGN/MGD_Living-Documentation.git /tmp/mgd-living-doc-install
   mkdir -p .claude/skills && cp -R /tmp/mgd-living-doc-install/skills/living-documentation .claude/skills/living-documentation
   # Codex analog: .codex/skills/living-documentation
   ```

   Nach der Installation entfernt der Agent den temporären Klon-Ordner (`rm -rf /tmp/mgd-*-install`)
   und bestätigt in der Setup-Zusammenfassung, welche Begleit-Skills neu installiert wurden.

   **d) Ohne Netzzugriff** — kann der Agent nicht klonen (kein Internetzugriff verfügbar),
   beschreibt er die obigen Schritte nur als konkrete Anleitung für den Nutzer, statt sie
   auszuführen, und ergänzt am Ende jeweils den Hinweis
   `<!-- ggf. exakte Zielpfade beim nächsten Sync mit den Ziel-Repos verifizieren -->`.

   **e) Einmaligkeit** — dieser Check läuft ausschließlich innerhalb von `/fragenkatalog-setup`
   (dem ohnehin einmaligen Erstlauf-Befehl). Alle anderen Befehle (`/fragenkatalog-generate`,
   `/fragenkatalog-answer`, ...) fragen nicht erneut danach.

Am Ende: schreibt `.fragenkatalog-config`, legt eine leere `fragenkatalog.json` (`[]`) am
`dataPath` an, und bestätigt die Einstellungen (inkl. Ergebnis des Begleit-Skills-Checks aus
Schritt 7) dem Nutzer in einer kurzen Zusammenfassung. Schlägt vor, direkt
`/fragenkatalog-generate` auszuführen.

### `/fragenkatalog-generate [anzahl]`

Generiert eine initiale Fragenliste für das Projekt.

- `anzahl` optional (Default: 40–60, je nach Projektkomplexität; bei sehr kleinen Projekten auch
  weniger — der Agent soll sinnvoll abwägen statt stur eine Zahl zu erzwingen).
- Der Agent leitet aus `projectType` (und ggf. `platforms`) sinnvolle Kategorien selbst ab, statt
  eine feste Liste zu verwenden. Richtwerte:
  - **Spiel**: Kern-Loop, Welt/Setting, Story, Spielfiguren/Klassen, Steuerung, Kampf/Mechaniken,
    Progression, Wirtschaft/Balance, Gegner-KI, UI/UX/HUD, Multiplayer (falls relevant),
    Monetarisierung (falls relevant), Optimierung/Performance.
  - **App**: Onboarding, Kernfunktionen, Informationsarchitektur, UI/UX, Datenschutz &
    Sicherheit, Monetarisierung, Skalierung/Infrastruktur, Offline-Verhalten, Benachrichtigungen,
    Barrierefreiheit.
  - **Buch/Roman**: Prämisse & Thema, Figuren, Plot-Struktur, Weltbau/Setting, Erzählperspektive,
    Zielgruppe & Genre-Konventionen, Spannungsbogen, Lektorat/Stil.
  - **Business-Plan**: Problem & Zielgruppe, Geschäftsmodell, Markt & Wettbewerb, Produkt/MVP,
    Go-to-Market, Finanzen & Pricing, Team, Risiken.
  - Bei anderen Projekttypen leitet der Agent 5–10 passende Kategorien selbst her.
  - **Sofern `includeLegalCategory` nicht explizit `false` ist**: zusätzlich immer die Kategorie
    "Recht" mit 5–15 projekttypischen Rechtsfragen (siehe Abschnitt "Rechts-Kategorie und
    Disclaimer-Pflicht"). Diese Fragen werden aus einer neutralen Recherche-Perspektive
    beantwortet (nicht aus der unter `perspective` gewählten Design-/Experten-Persona) und
    erhalten zwingend den Disclaimer-Satz am Ende von `kiAnswer`.
- Jede Frage wird **sofort** aus der in `.fragenkatalog-config` gespeicherten `perspective`
  beantwortet und in `kiAnswer` geschrieben (Freitext, konkret und projektspezifisch — keine
  generischen Plattitüden). `userAnswer` bleibt leer (`""`).
- Ergänzt die Fragen in `fragenkatalog.json` (überschreibt nicht bereits vorhandene Fragen; bei
  einem bestehenden, nicht-leeren Katalog fragt der Agent nach, ob ergänzt oder neu gestartet
  werden soll).
- Am Ende: Zusammenfassung (Anzahl generierter Fragen pro Kategorie) und Hinweis auf
  `/fragenkatalog-export`.

### `/fragenkatalog-add-category <name>`

Fügt eine neue Kategorie mit 5–30 sinnvollen, projektspezifischen Fragen hinzu (Anzahl je nach
Themenbreite der Kategorie vom Agenten gewählt). Jede Frage wird sofort aus der gespeicherten
Perspektive beantwortet. Prüft vorher, ob die Kategorie bereits existiert (dann stattdessen
Vorschlag, `/fragenkatalog-add-question` zu nutzen oder die Kategorie zu erweitern).

### `/fragenkatalog-add-question <kategorie> <frage>`

Fügt eine einzelne Frage manuell zur angegebenen Kategorie hinzu (legt die Kategorie neu an,
falls sie noch nicht existiert). Die KI beantwortet die Frage sofort aus der projektspezifischen
Perspektive und trägt das Ergebnis in `kiAnswer` ein. `userAnswer` bleibt leer.

### `/fragenkatalog-answer <id-oder-suchtext>`

Sucht die Frage per `id` (Ganzzahl) oder per Volltextsuche im `question`-Feld. Bei mehreren
Treffern: Liste anzeigen und Nutzer auswählen lassen. Lässt die KI die gefundene Frage aus der
gespeicherten `perspective` (neu) beantworten und überschreibt `kiAnswer` — nur wenn `kiAnswer`
leer/Platzhalter ist ODER der Nutzer eine Neubeantwortung explizit bestätigt (bestehende
`kiAnswer`-Werte werden nicht kommentarlos überschrieben).

### `/fragenkatalog-export`

Baut/aktualisiert die finale, self-contained HTML-Datei am `outputPath` aus
`templates/Fragenkatalog.template.html` als Basis:

1. Lies `templates/Fragenkatalog.template.html`.
2. Ersetze die Zeile `const COMPLETE_DATA = [];` durch
   `const COMPLETE_DATA = <JSON-Array aus fragenkatalog.json>;` (kompakt oder eingerückt, aber
   valides JS/JSON).
3. Falls `perspectivePrefix` von `.fragenkatalog-config` vom Template-Default (`💙`) abweicht,
   passe die Konstante `KI_PREFIX` im eingebetteten Script entsprechend an.
4. Setze den `<title>` und die `<h1>` auf `projectName` + " — Fragenkatalog".
5. Schreibe das Ergebnis nach `outputPath` (Ordner bei Bedarf anlegen).

Die erzeugte HTML MUSS folgende Struktur/Funktionen enthalten (siehe Template als Referenz-
Implementierung, die 1:1 übernommen wird):

- **Toolbar** über der Tabelle: Kategorie-Filter-Dropdown (mit Fragenanzahl je Kategorie),
  Volltextsuche, Edit-Modus-Toggle-Button, "Neue Frage"-Button (nur im Edit-Modus sichtbar),
  Export- und Import-Buttons.
- **Statistik-Zeile**: Gesamtanzahl, Anzahl mit eigener Antwort, Anzahl offen, aktuell angezeigt.
- **Tabelle** mit Spalten Kategorie | Frage (rot) | KI-Antwort (blau, mit Präfix) | Eigene Antwort
  | Aktionen (nur im Edit-Modus sichtbar, "Bearbeiten"-Button pro Zeile).
- **Modal-Dialog** zum Bearbeiten/Hinzufügen: Kategorie-Dropdown (inkl. Möglichkeit neue
  Kategorie durch Freitext-Auswahl), Frage-Textarea, KI-Antwort-Textarea, Eigene-Antwort-Textarea,
  Speichern/Löschen/Abbrechen-Buttons (Löschen nur beim Bearbeiten bestehender Zeilen).
- **JavaScript-Funktionen** (Namen exakt wie im Template, damit Weiterentwicklungen konsistent
  bleiben):
  - `initData()` — lädt Daten aus `localStorage` falls vorhanden, sonst aus `COMPLETE_DATA`
    (Deep Copy, mutiert `COMPLETE_DATA` nie).
  - `renderTable()` — rendert die (gefilterten) Zeilen inkl. Statistik.
  - `filterTable()` — liest Kategorie-Filter + Suchfeld, ruft `renderTable()`.
  - `toggleEditMode()` — schaltet Edit-Modus um, blendet Aktionen-Spalte/Buttons ein/aus.
  - `openEditModal(id)` / `openAddModal()` — öffnet das Modal befüllt bzw. leer.
  - `saveEdit()` — validiert (Frage darf nicht leer sein), schreibt Änderung in den State,
    persistiert via `localStorage`, rendert neu.
  - `deleteCurrentRow()` — löscht mit Sicherheitsabfrage (`confirm(...)`).
  - `addNewRow()` — Alias/Wrapper für `openAddModal()`.
  - `exportData()` — lädt aktuellen State als JSON-Datei herunter (Browser-Download).
  - `importData(file)` — liest eine JSON-Datei, validiert grob (Array von Objekten mit
    `question`), fragt ob ersetzen oder anhängen, persistiert.
  - `escapeHtml(str)` — escaped `&`, `<`, `>`, `"`, `'` vor jedem Einfügen von Nutzer-/KI-Text in
    `innerHTML`, um XSS zu verhindern. JEDE Ausgabe von `question`, `kiAnswer`, `userAnswer`,
    `category` MUSS durch diese Funktion laufen, bevor sie ins DOM geschrieben wird.
- **localStorage-Persistenz**: Schlüssel `fragenkatalog_data_v1`. Änderungen im Browser
  (Edit-Modus) werden sofort persistiert und überleben einen Reload. `COMPLETE_DATA` selbst bleibt
  unverändert (Immutability — die Anzeige nutzt eine Kopie im State).
- **Keine externen Abhängigkeiten**: kein CDN, kein Framework, reines Vanilla-HTML/CSS/JS,
  funktioniert als lokal geöffnete `file://`-Datei ohne Internetverbindung.

Nach dem Export: Agent bestätigt Pfad und Fragenanzahl, weist darauf hin dass die Datei einfach
im Browser geöffnet werden kann.

### `/fragenkatalog-import <pfad>`

Importiert eine bestehende Fragenliste des Nutzers aus JSON oder Markdown:

- **JSON**: erwartet ein Array von Objekten; mappt bekannte alternative Feldnamen (`aiAnswer` →
  `kiAnswer`, `michaAnswer`/`myAnswer` → `userAnswer`) automatisch.
- **Markdown**: erkennt Fragen z. B. an Überschriften (`### Frage: ...`) oder Listenpunkten
  (`- Frage: ... / Antwort: ...`) — der Agent parst pragmatisch, bei Unklarheit fragt er nach dem
  genauen Format oder schlägt eine Interpretation zur Bestätigung vor.
- Fragt bei Konflikten (gleiche `id` oder sehr ähnlicher `question`-Text) nach: überspringen,
  überschreiben oder als Duplikat anhängen.
- Schreibt Ergebnis zurück nach `fragenkatalog.json`.

### `/fragenkatalog-stats`

Zeigt eine kompakte Übersicht (nur Lesevorgang, keine Änderungen):

- Gesamtanzahl Fragen.
- Fragen pro Kategorie (Tabelle oder Liste).
- Anzahl Fragen mit ausgefüllter `userAnswer` (Fortschritt in %).
- Anzahl noch offener Fragen (leere `userAnswer`).
- Optional: Liste der offenen Fragen (auf Wunsch, um schnell weiterzuarbeiten).

### `/fragenkatalog-pfad <pfad>`

Ändert `outputPath` in `.fragenkatalog-config` (analog `/todo-pfad` bei MGD_Todo_SKILL). Fragt
nach, ob eine bereits existierende HTML-Datei am alten Pfad verschoben oder am neuen Pfad neu
exportiert werden soll.

### `/fragenkatalog-perspektive <beschreibung>`

Ändert `perspective` (und optional `perspectivePrefix`) in `.fragenkatalog-config`. Bestehende
`kiAnswer`-Werte bleiben unangetastet — nur künftige `/fragenkatalog-generate`,
`/fragenkatalog-add-*` und `/fragenkatalog-answer`-Aufrufe nutzen die neue Perspektive. Der Agent
fragt explizit nach, ob stattdessen ALLE bestehenden `kiAnswer`-Werte aus der neuen Perspektive
neu generiert werden sollen ("Re-Generieren") — nur bei ausdrücklicher Bestätigung durchführen,
da dies bestehende Inhalte überschreibt.

## Arbeitsprinzipien für den Agenten

- Immer zuerst `.fragenkatalog-config` prüfen; fehlt sie, `/fragenkatalog-setup` vorschlagen statt
  zu raten.
- KI-Antworten sind erkennbar als Vorschlag markiert (Präfix-Emoji) — nie als Tatsachenbehauptung
  formulieren, sondern als fundierte Expertenmeinung aus der gewählten Perspektive.
- `userAnswer` wird vom Agenten nie automatisch befüllt — das ist ausschließlich die Entscheidung
  des Projektinhabers (im Browser oder auf explizite Bitte im Chat).
- Bei jedem datenverändernden Befehl: `fragenkatalog.json` aktuell halten, damit
  `/fragenkatalog-export` jederzeit den korrekten Stand exportiert.
- Kategorien-Namen konsistent halten (keine Duplikate durch Groß-/Kleinschreibung oder
  Singular/Plural-Varianten — bei Unsicherheit bestehende Kategorie wiederverwenden).

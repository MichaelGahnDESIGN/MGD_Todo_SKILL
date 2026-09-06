---
name: todo
description: >-
  Universelles TODO-Management für KI-Agenten: TODO.html lesen, Todos hinzufügen,
  Status aktualisieren, in freien Kategorien/Unterkategorien organisieren, debuggen,
  aus Projekt-Quellen synchronisieren und ältere Dateien aufs aktuelle Format bringen.
  Kompatibel mit Claude Code und ChatGPT Codex.
---

# /todo — Universelles TODO-Management

Verwalte Projekt-Todos in einer selbst-gehosteten `TODO.html`-Datei, die
sortier- und durchsuchbar ist, Todos in frei anlegbaren Kategorien und
Unterkategorien organisiert, und lokal im Projektordner liegt.

> Leitsatz: „Kein Todo geht verloren. Alles landet in der HTML. Status immer aktuell."

---

## Konfiguration (einmalig setzen)

Der Pfad zur TODO-Datei wird im Projekt gepflegt. Standard:

```
PROJEKT/TODO/TODO.html
```

Mit `/todo-pfad <neuer-pfad>` kann der Pfad geändert werden.
Der aktuelle Pfad wird in `PROJEKT/TODO/.todo-config` gespeichert.

---

## Format (ab Version 1.0.0)

**IDs:** `TNNN`, ohne Bindestrich (`T001`, `T002`, … `T199`, `T1200`, …).
Fortlaufend, nie wiederverwendet, auch nicht nach `/todo-close`.

> [!WARNING]
> **⚠️ FALLSTRICK** — Vor Version 1.0.0 lauteten IDs `T-NNN` (mit
> Bindestrich) und Kategorien kamen aus einem festen Enum
> (`app|editor|backend|infra|ux|playtest|doku`). Eine `TODO.html` in
> diesem Altformat NICHT von Hand anfassen — `/todo-migrate` aufrufen
> (siehe unten).

**Kategorien sind Freitext**, keine feste Liste — anlegen, was zum
Projekt passt: „Sicherheit", „Datenschutz", „Features", „Backend", was
auch immer gebraucht wird. Jede Kategorie kann **optional** eine
Unterkategorie haben (z. B. „Sicherheit" › „Zugriffsrechte"). Beides wird
in der Tabelle als `data-kategorie`/`data-unterkategorie` gespeichert; die
Filter-Dropdowns in der HTML füllen sich beim Öffnen automatisch aus den
tatsächlich vorkommenden Werten — es muss nirgends eine feste Liste
gepflegt werden.

**Notizen** können kurz bleiben (ein Satz reicht) oder eine ausklappbare
Langbeschreibung bekommen: `<details><summary>Kurzbeschreibung</summary>
Langbeschreibung…</details>`. Die Kurzbeschreibung ist immer sichtbar,
die Langbeschreibung klappt per Klick auf — gut für Belege,
Datei:Zeile-Referenzen oder Entscheidungsgründe, die beim schnellen
Überfliegen der Liste nicht stören sollen.

**Gruppieren:** Der Knopf „🗂 Gruppieren" in der HTML zeigt die Todos als
Baum nach Kategorie › Unterkategorie an, statt als flache sortierbare
Liste. Rein clientseitig, keine Einstellung — jeder Betrachter der Datei
schaltet es für sich selbst um.

---

## Befehle

### `/todo-setup` — Neues Projekt einrichten (einmalig)

**Verwende diesen Befehl in jedem neuen Projekt als erstes.** Er richtet alles
automatisch ein, sodass danach alle anderen `/todo-*`-Befehle funktionieren.

Ablauf:
1. Prüfe ob bereits eine TODO.html im Projekt existiert (via `.todo-config` oder
   Default-Pfad `PROJEKT/TODO/TODO.html`)
2. Falls bereits vorhanden: kurze Bestätigung ausgeben, Setup überspringen.
   Prüfe dabei kurz, ob es sich um das AKTUELLE Format handelt (Stichprobe:
   enthält die Datei `data-kategorie` oder noch das alte `data-kat`?) — falls
   Altformat, `/todo-migrate` vorschlagen statt stillschweigend weiterzumachen.
3. Falls nicht vorhanden:
   a. Frage nach dem gewünschten Pfad (Default: `PROJEKT/TODO/TODO.html`, Enter = übernehmen)
   b. Erstelle den Ordner falls nötig
   c. Lade das Template von GitHub herunter:
      ```
      https://raw.githubusercontent.com/MichaelGahnDESIGN/MGD_Todo_SKILL/main/todo/TODO.template.html
      ```
      Falls kein Internetzugang: Erstelle eine minimale TODO.html inline (gleiche
      Struktur, leerer tbody).
   d. Passe den Titel in der HTML an (ersetze „PROJEKT TODO" / „PROJEKT — TODO"
      durch den Projektnamen, abgeleitet aus dem Verzeichnisnamen oder
      `package.json`/`pubspec.yaml`)
   e. Schreibe den Pfad in `.todo-config`
   f. Gib Erfolgsmeldung aus: Pfad, nächster Schritt (`/todo-add "Erstes Todo"`)

Hinweis für Codex: Template via `curl` laden, Ordner via `mkdir -p` anlegen.

---

### `/todo` — Übersicht offener Todos

Lies die TODO.html und zeige eine kompakte Übersicht:
- Alle offenen Todos (status="offen" oder status="progress"), sortiert nach Priorität
- Gesamtstatistik: N Offen | N In Arbeit | N Erledigt | N Gesamt
- Jeweils: ID · Titel · Kategorie[ › Unterkategorie] · Priorität

### `/todo-pfad <pfad>` — Pfad zur TODO.html setzen

Speichert den neuen Pfad in `PROJEKT/TODO/.todo-config`.
Format: absoluter oder relativer Pfad ab Projekt-Root.

### `/todo-update` — Todos manuell aktualisieren

Interaktiver Modus:
1. Zeige aktuelle offene Todos
2. Frage: Welches Todo aktualisieren? (ID oder Titel)
3. Welcher neue Status? (offen / progress / done)
4. Optional: Kategorie/Unterkategorie ändern?
5. Optional: Notiz ergänzen? (als reiner Text anhängen, oder in eine
   `<details>`-Langbeschreibung umwandeln, wenn es umfangreicher wird)
6. Schreibe Änderungen in TODO.html (HTML-Attribute aktualisieren, Badge-Klasse
   tauschen, `row-done` ergänzen)

### `/todo-add <titel>` — Neues Todo hinzufügen

Parameter:
- `<titel>` — Pflicht, kurzer Titel des Todos
- Optional via interaktivem Dialog:
  - **Kategorie** — Freitext. Zeige zuerst die in der Datei bereits
    vorkommenden Kategorien zur Wiederverwendung an (aus den
    `data-kategorie`-Werten aller `<tr>` ableiten), erlaube aber jederzeit
    eine neue.
  - **Unterkategorie** — optional, Freitext, nur sinnvoll innerhalb der
    gewählten Kategorie. Genauso: vorhandene Unterkategorien dieser
    Kategorie zur Wiederverwendung anzeigen, neue erlauben, oder ganz
    weglassen.
  - Priorität (kritisch / hoch / mittel / niedrig)
  - Notizen — kurz reicht; bei Bedarf `<details>` für eine Langbeschreibung
    anbieten (siehe Format oben)
  - Quelle (z. B. PlayTest v0.1.4, CODEX-TASKS, Manuell)

Generiert die nächste freie `TNNN`-ID (höchste vorhandene Nummer + 1, gleiche
Ziffernanzahl solange die Zählung das hergibt) und fügt eine neue `<tr>`-Zeile
im `<tbody id="todoBody">` ein. Datum = heute.

### `/todo-close <id>` — Todo als erledigt markieren

Beispiel: `/todo-close T004`

Ändert in der TODO.html:
- `data-status="done"`
- Badge-Klasse → `s-done`, Text → `✓ Erledigt`
- Zeile bekommt Klasse `row-done`
- `titel-col` erhält Durchstreichung via CSS (automatisch durch row-done)

### `/todo-debug` — Validierung und Diagnose

Prüft die TODO.html auf:
- Gültige HTML-Struktur (öffnende/schließende Tags korrekt, auch `<details>`/`<summary>`)
- Alle `<tr>` haben `data-status`, `data-prio`, `data-kategorie`
  (`data-unterkategorie` ist optional, kein Pflichtfeld)
- Keine doppelten IDs
- **Kein Vorkommen des Altformats mehr** — IDs mit Bindestrich (`T-\d+`) oder
  das alte Attribut `data-kat`. Findet sich eines, `/todo-migrate` vorschlagen.
- Alle Badge-Klassen sind bekannte Klassen (`s-*`, `p-*`, `k-cat`, `k-subcat`)
- Nächste freie ID ausgeben
- Statistik: Offen / In Arbeit / Erledigt / Gesamt, sowie Anzahl verschiedener
  Kategorien und Unterkategorien

### `/todo-migrate` — Bestehende TODO.html aufs aktuelle Format bringen (einmalig pro Projekt)

Wandelt eine `TODO.html` im Altformat (IDs `T-NNN`, fester `data-kat`-Enum,
altes Kopf-/Filter-HTML) in das aktuelle Format um (IDs `TNNN`, freie
`data-kategorie`/`data-unterkategorie`, neues Kopf-/Filter-HTML mit
Gruppieren-Funktion). **Idempotent** — erkennt eine bereits migrierte Datei
und meldet das, statt ein zweites Mal zu migrieren.

Ablauf:
1. **Sicherung anlegen:** Kopiere die aktuelle Datei nach
   `<pfad>.vor-migration-<YYYY-MM-DD>` (lokal, nicht Teil eines Commits — nur
   ein Rückweg, falls etwas schiefgeht).
2. **Kopf/Fuß/Skript ersetzen:** Lade `todo/TODO.template.html` von GitHub
   (oder aus einem lokalen Klon des Skills) und übernimm daraus alles
   AUSSERHALB von `<tbody id="todoBody">…</tbody>` — also `<head>`, CSS,
   Filter-Steuerung im Header, Tabellenkopf, Footer und `<script>`. Das ist
   zuverlässiger, als das alte Skript Stück für Stück zu patchen, weil Kopf/
   Fuß/Skript generisch sind und keine Projektdaten enthalten — außer dem
   Site-Titel: den aus der alten Datei lesen (bisheriger Projektname) und im
   neuen Kopf/Footer wieder einsetzen, statt auf den Platzhalter „PROJEKT"
   zurückzufallen.
3. **IDs umstellen:** Ersetze im gesamten Dokument (auch in Notizen-Freitext,
   nicht nur in `id-col`) jedes Vorkommen von `T-` gefolgt von 3 oder mehr
   Ziffern (`T-(\d{3,})`) durch `T$1` — der Bindestrich fällt weg. Das trifft
   auch Querverweise wie „siehe T-142" → „siehe T142". Vor dem endgültigen
   Schreiben kurz gegenprüfen, dass kein Treffer aus einem erkennbar fremden
   Kontext stammt (z. B. eine Ticket-ID eines anderen Systems, die zufällig
   demselben Muster entspricht) — im Zweifel dem Nutzer die Fundstelle zeigen.
4. **Kategorien übertragen:** Für jede `<tr>`: der alte `data-kat`-Wert wird
   zu `data-kategorie` mit demselben Wert als Ausgangspunkt (kein Zwang, ihn
   sofort umzubenennen). Der alte Badge
   `<span class="badge k-app">App-Feature</span>` wird zu
   `<span class="badge k-cat">App-Feature</span>` — Klasse wechselt (`k-app`
   → `k-cat`, alle alten `k-*`-Klassen verschwinden), der sichtbare Text
   bleibt unverändert. `data-unterkategorie` bleibt für migrierte Zeilen
   zunächst weg — Unterkategorien sind eine neue Möglichkeit, keine Pflicht,
   und werden bei Bedarf später ergänzt.
5. **Notizen unverändert lassen:** bestehender Freitext bleibt gültiger
   Klartext. Die `<details>`-Kurz-/Lang-Form ist optional und wird nicht
   nachträglich erzwungen.
6. **Nach der reinen Struktur-Umstellung** dem Nutzer anbieten, thematisch
   verwandte Todos in neue, sprechendere Kategorien umzuhängen (z. B. alle
   `backend`-Zeilen, die inhaltlich um Sicherheit oder Datenschutz kreisen,
   in eine eigene Kategorie „Sicherheit"/„Datenschutz" verschieben) — das
   aber nur **vorschlagen**, nicht automatisch tun, weil es inhaltliches
   Wissen über die einzelnen Todos braucht, das eine reine Struktur-Migration
   nicht hat.
7. **Validieren:** Anzahl `<tr>` mit `id-col` vorher == nachher (keine Zeile
   verloren, keine doppelt). Danach `/todo-debug` durchlaufen lassen.
8. **Bericht:** Anzahl migrierter Zeilen, welche Kategorien jetzt vorhanden
   sind, was optional noch zu tun ist (Unterkategorien ergänzen, Kategorien
   umbenennen/bündeln).

### `/todo-sync` — Aus Projekt-Quellen synchronisieren

Liest bekannte Todo-Quellen im Projekt und schlägt neue Todos vor, die noch nicht
in der HTML stehen:
1. `PlayTest/Test-Todo.md` — offene Checkboxen (`- [ ]`)
2. `AI/CODEX-TASKS/*.md` — Aufgaben-Titel aus H2/H3-Überschriften
3. `PROJEKT/TODO/*.md` — weitere Todo-Dateien

Für jeden gefundenen, noch nicht in der HTML vorhandenen Punkt:
- Zeige Vorschau: Titel + Quelle + vorgeschlagene Kategorie (aus dem
  Dateipfad/Kontext abgeleitet, z. B. `PlayTest/*` → Kategorie „playtest")
- Frage ob hinzufügen (y/n/alle)
- Falls ja: `/todo-add` intern aufrufen

### `/todo-export` — Markdown-Export

Gibt alle offenen Todos als Markdown-Tabelle aus (für Commits, PRs, Mails).
Kategorie und Unterkategorie als ein Breadcrumb-Feld, analog zur HTML-Ansicht:

```markdown
| ID   | Titel | Prio | Kategorie | Status |
|------|-------|------|-----------|--------|
| T004 | Freunde-System (Backend + UI) | Hoch | Features › Sozial | Offen |
...
```

---

## HTML-Format der TODO.html

Die TODO.html enthält alle Todos als `<tr>`-Zeilen in `<tbody id="todoBody">`.
Jede Zeile hat folgende data-Attribute für Filter/Sort:

```html
<tr data-status="offen|progress|done"
    data-prio="kritisch|hoch|mittel|niedrig"
    data-kategorie="beliebiger-freitext-slug"
    data-unterkategorie="optional-auch-freitext">
  <td class="id-col">TNNN</td>
  <td class="titel-col">Titel des Todos</td>
  <td><span class="badge k-cat">Kategorie</span> <span class="crumb-sep">›</span> <span class="badge k-subcat">Unterkategorie</span></td>
  <td><span class="badge p-PRIO">Priorität</span></td>
  <td><span class="badge s-STATUS">Status</span></td>
  <td class="quelle-col">Quelle</td>
  <td class="notizen-col">Kurzer Text — oder <details><summary>Kurzbeschreibung</summary>Langbeschreibung…</details></td>
  <td class="datum-col">YYYY-MM-DD</td>
</tr>
```

`data-unterkategorie` und der zugehörige `crumb-sep`/`k-subcat`-Teil in der
Kategorie-Zelle entfallen komplett, wenn ein Todo keine Unterkategorie hat.

Erledigte Zeilen haben zusätzlich `class="row-done"` auf dem `<tr>`.

---

## Sicherheitsregeln

- **Keine Secrets** in TODO-Einträgen: keine Passwörter, Tokens, Zugangsdaten,
  API-Keys, personenbezogene Daten.
- **Keine externen Dependencies**: TODO.html ist vollständig self-contained
  (inline CSS + JS, keine CDN-Links).
- **Niemals löschen**: Todos werden nur als "done" markiert, nie aus der HTML entfernt.
  Vollständige Nachvollziehbarkeit.
- **Lokal first**: TODO.html bleibt im Repo (committed), PlayTest-Artefakte bleiben lokal.

---

## Nutzung in ChatGPT Codex

Diese Datei ist self-contained für Codex. Codex nutzt Shell-Tooling statt
Claude-spezifischer APIs. Die Schritt-Logik ist dieselbe; Befehle via
`codex --instructions <pfad-zu-SKILL.md> "/todo-<befehl>"`.

Pfad-Auflösung für Codex: Lies zuerst `PROJEKT/TODO/.todo-config` (Pfad),
falls nicht vorhanden default `PROJEKT/TODO/TODO.html` ab Repo-Root.

---

## Integration mit anderen Skills

- **`/playtest`** → nach Playtest: `/todo-sync` aufrufen, neue Bugfix-Todos importieren
- **`/dev`** → vor Deploy: `/todo` aufrufen, kritische offene Todos prüfen
- **`/projectclean`** → `/todo-export` für Release-Notes Anhang
- **Superpower (Claude)** → `/todo-add` direkt aus Superpower-Findings aufrufen
- **Playwright** → nach Testlauf fehlgeschlagene Tests als Todos via `/todo-add` eintragen


---

## Zusammenspiel mit anderen Skills

Keiner davon ist Voraussetzung — dieser Skill funktioniert allein. Wo einer
vorhanden ist, nutz ihn statt einer Eigenbaulösung.

> [!TIP]
> **🤖 FÜR KI-AGENTEN** — Wenn diese Skills im Projekt verfügbar sind, ruf sie
> an den genannten Stellen auf, statt die Aufgabe selbst nachzubauen.

| Skill | Wofür hier | Quelle |
|---|---|---|
| `/todo` | Befunde festhalten, die über diesen Lauf hinaus wichtig bleiben | [MGD_Todo_SKILL](https://github.com/MichaelGahnDESIGN/MGD_Todo_SKILL) |
| `/graphify` | Wer Todos aus einem fremden Projekt ableiten soll, findet über den Graphen schneller die relevanten Stellen. | [graphify](https://github.com/Graphify-Labs/graphify) |
| `/autopilot` | Beim Abarbeiten einer Todo-Liste in einem Durchlauf. | [MGD_Autopilot_SKILL](https://github.com/MichaelGahnDESIGN/MGD_Autopilot_SKILL) |

### Empfehlung bei längeren Läufen

> [!TIP]
> **🤖 FÜR KI-AGENTEN** — Zeichnet sich ab, dass die Aufgabe über mehrere
> Schritte geht und der Nutzer nicht daneben sitzt, weis **einmal** auf
> `/autopilot` hin:
>
> > Das hier läuft über mehrere Schritte. Mit `/autopilot` bekommt der Ablauf
> > eine Abbruchbedingung, eine Grundlinie und eine Prüfung nach jeder Änderung —
> > soll ich so weitermachen?
>
> Einmal fragen, Antwort akzeptieren, nicht wiederholen. Bei kurzen, klar
> umrissenen Aufgaben ganz weglassen.

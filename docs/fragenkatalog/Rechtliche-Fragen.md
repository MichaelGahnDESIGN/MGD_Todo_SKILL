# Rechtliche Fragen

> [!WARNING]
> **Dieser Skill ersetzt keine Anwaltsleistung.** Alle Antworten in der Kategorie "Recht"
> (bzw. "Rechtliches") sind allgemeine Orientierung zur eigenen Recherche, keine Rechtsberatung
> im rechtlichen Sinne. Sie können veraltet, unvollständig oder für den konkreten Einzelfall
> nicht zutreffend sein. Für verbindliche Aussagen ist immer ein Anwalt bzw. Fachberater für das
> jeweilige Rechtsgebiet und Land zu konsultieren.

## Warum eine eigene Rechts-Kategorie?

Fast jedes Projekt — Spiel, App, Buch, Business — hat rechtliche Aspekte, die früh mitgedacht
werden sollten: Jugendschutz, Datenschutz, Urheberrecht, Plattform-Richtlinien, Vertragsfragen.
Diese Fragen werden in Design-Diskussionen leicht vergessen, weil sie kein "kreatives" Thema
sind. Der Fragenkatalog-Skill nimmt sie deshalb standardmäßig als eigene Kategorie mit auf —
außer der Nutzer lehnt das beim Setup ausdrücklich ab.

## Das Disclaimer-Konzept

Anders als bei Design-Fragen, wo die KI aus einer frei gewählten Kreativ-Persona (z. B. "Blizzard
Entertainment Lead Game Designer") antwortet, gilt für die Rechts-Kategorie ein festes,
nicht-kreatives Format:

- **Eigenes Präfix**: `⚖️` statt `💙` — sofort optisch erkennbar, auch im Kategorie-Filter der
  exportierten HTML.
- **Eigene Akzentfarbe**: Amber/Gold-Orange statt Blau in der Tabelle, um die Antwort klar von
  "normalen" Design-Vorschlägen abzuheben.
- **Pflicht-Disclaimer** am Ende jeder `kiAnswer` in dieser Kategorie:

  > "Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für
  > verbindliche Aussagen einen Anwalt/Fachberater für [Rechtsgebiet, Land] konsultieren."

  `[Rechtsgebiet, Land]` wird vom Agenten so konkret wie möglich ausgefüllt (z. B.
  "Jugendschutzrecht, Deutschland").
- **Formulierungsstil**: Antworten benennen relevante Gesetze/Regularien/Anlaufstellen und
  typische Fallstricke, ohne uneingeschränkte Garantien ("ist erlaubt"/"ist verboten") zu geben.

Das Template erkennt Rechts-Zeilen automatisch am Kategorienamen (case-insensitive: "Recht",
"Rechtliches", "Rechtsfragen") und hängt den Disclaimer beim Rendern zur Sicherheit automatisch
an, falls er im Rohtext fehlen sollte.

## Beispielfragen nach Projekttyp

### Spiel

1. **Frage:** Welche Altersfreigabe (USK/PEGI) ist für ein Fantasy-Rollenspiel mit Kampfszenen zu
   erwarten?
   **⚖️ Antwort:** In Deutschland prüft die USK Gewaltdarstellung, Grusel- und Horrorelemente
   sowie Diskriminierungsinhalte; ein stilisiertes Fantasy-Kampfsystem ohne realistische Gewalt
   liegt häufig im Bereich USK 12–16. PEGI bewertet EU-weit ähnlich, mit eigener Kriterienliste.
   Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für
   verbindliche Aussagen einen Anwalt/Fachberater für Jugendschutzrecht, Deutschland/EU
   konsultieren.

2. **Frage:** Fällt ein "Gacha"-Sammelsystem mit Echtgeld-Käufen unter Glücksspielrecht?
   **⚖️ Antwort:** Das hängt u. a. davon ab, ob gezogene Items einen realen Sekundärmarktwert
   haben und ob Zufall gegen Einsatz mit Gewinnmöglichkeit vorliegt; mehrere EU-Länder (z. B.
   Belgien, Niederlande) haben Lootboxen bereits gesondert reguliert oder verboten. Dies ist
   keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche
   Aussagen einen Anwalt/Fachberater für Glücksspielrecht, EU-Länder-spezifisch konsultieren.

3. **Frage:** Welche Rechte müssen für lizenzierte Musiktracks im Spiel geklärt werden?
   **⚖️ Antwort:** Typischerweise Synchronisationsrechte (Nutzung der Musik im audiovisuellen
   Werk) und ggf. Mechanical/Performance-Rechte je nach Vertriebsweg; bei Streaming-Plattformen
   im Spiel zusätzlich Plattform-eigene Music-Recognition-Systeme beachten. Dies ist keine
   Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen
   einen Anwalt/Fachberater für Urheber- und Musiklizenzrecht konsultieren.

4. **Frage:** Ist der geplante Spieltitel markenrechtlich unbedenklich?
   **⚖️ Antwort:** Vor Festlegung des Titels empfiehlt sich eine Recherche in den relevanten
   Markenregistern (z. B. DPMA für Deutschland, EUIPO für die EU) sowie eine einfache
   Store-Namenssuche, um Verwechslungsgefahr mit bestehenden Marken/Spielen auszuschließen. Dies
   ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche
   Aussagen einen Anwalt/Fachberater für Markenrecht konsultieren.

### App

5. **Frage:** Welche DSGVO-Pflichten entstehen durch die Nutzung eines Analytics-SDKs?
   **⚖️ Antwort:** In der Regel eine Datenschutzerklärung mit Zweck- und Empfängerangaben, ggf.
   Einwilligung vor Tracking (Consent-Banner), Auftragsverarbeitungsvertrag mit dem
   SDK-Anbieter und Prüfung von Drittlandtransfers (z. B. USA). Dies ist keine Rechtsberatung,
   sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen einen
   Anwalt/Fachberater für Datenschutzrecht, EU/DSGVO konsultieren.

6. **Frage:** Besteht Impressumspflicht für eine kostenlose App ohne Werbung?
   **⚖️ Antwort:** In Deutschland besteht die Impressumspflicht (§ 5 DDG, vormals TMG) im
   Regelfall unabhängig von Monetarisierung, sobald die App geschäftsmäßig angeboten wird — reine
   Privatprojekte ohne jede geschäftliche Ausrichtung können anders zu bewerten sein. Dies ist
   keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche
   Aussagen einen Anwalt/Fachberater für Telemedienrecht, Deutschland konsultieren.

7. **Frage:** Welche Lizenzpflichten entstehen durch verwendete Open-Source-Bibliotheken?
   **⚖️ Antwort:** Je nach Lizenztyp (MIT, Apache 2.0, GPL, LGPL ...) unterschiedliche Pflichten
   wie Namensnennung, Lizenztext-Beilage oder Copyleft-Effekte auf eigenen Code; vor Veröffentlichung
   empfiehlt sich eine vollständige Lizenz-Inventur aller Abhängigkeiten. Dies ist keine
   Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen
   einen Anwalt/Fachberater für Lizenz-/IP-Recht konsultieren.

8. **Frage:** Gilt das Barrierefreiheitsgesetz (BFSG) für die geplante App?
   **⚖️ Antwort:** Das BFSG betrifft ab Juni 2025 bestimmte digitale Produkte und Dienstleistungen
   für Verbraucher in Deutschland/EU; ob die konkrete App darunterfällt, hängt u. a. von
   Geschäftsmodell und Zielgruppe ab. Dies ist keine Rechtsberatung, sondern eine allgemeine
   Orientierung zur Recherche. Für verbindliche Aussagen einen Anwalt/Fachberater für
   Barrierefreiheitsrecht, Deutschland/EU konsultieren.

### Buch/kreatives Werk

9. **Frage:** Dürfen reale Personen als Vorbild für Romanfiguren erkennbar verwendet werden?
   **⚖️ Antwort:** Persönlichkeitsrechte realer Personen können berührt sein, wenn sie erkennbar
   und in einem nachteiligen Licht dargestellt werden; die Kunstfreiheit schützt fiktionale
   Bearbeitung, eine Abwägung im Einzelfall ist aber typisch. Dies ist keine Rechtsberatung,
   sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen einen
   Anwalt/Fachberater für Persönlichkeitsrecht/Medienrecht konsultieren.

10. **Frage:** Wie viel darf aus einem fremden Werk zitiert werden?
    **⚖️ Antwort:** Das Zitatrecht (z. B. § 51 UrhG in Deutschland) erlaubt Zitate nur in einem
    durch den Zitatzweck gerechtfertigten Umfang mit Quellenangabe — eine pauschale Wortzahl gibt
    es nicht. Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche.
    Für verbindliche Aussagen einen Anwalt/Fachberater für Urheberrecht konsultieren.

### Business/Startup

11. **Frage:** Welche Gesellschaftsform passt zu einem Zwei-Personen-Startup mit Investorenplan?
    **⚖️ Antwort:** Häufig gewählt wird in Deutschland eine GmbH oder UG (haftungsbeschränkt) wegen
    Haftungsbegrenzung und Investoren-Gewöhnung an diese Rechtsformen; die konkrete Wahl hängt von
    Kapitalbedarf, Haftungsrisiko und geplanter Finanzierungsrunde ab. Dies ist keine
    Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen
    einen Anwalt/Steuerberater für Gesellschaftsrecht konsultieren.

12. **Frage:** Welche Pflichtangaben muss ein Vertrag mit Freelancern enthalten?
    **⚖️ Antwort:** Typischerweise Leistungsbeschreibung, Vergütung, Nutzungsrechte an
    Arbeitsergebnissen, Geheimhaltung, Kündigungsfristen und eine klare Abgrenzung zur
    Scheinselbstständigkeit. Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung
    zur Recherche. Für verbindliche Aussagen einen Anwalt/Fachberater für Vertragsrecht
    konsultieren.

13. **Frage:** Welche Datenschutzpflichten entstehen beim Speichern von Kundendaten in einem
    CRM?
    **⚖️ Antwort:** In der Regel eine Datenschutzerklärung, eine Rechtsgrundlage für die
    Verarbeitung (z. B. Vertragserfüllung), ein Auftragsverarbeitungsvertrag mit dem
    CRM-Anbieter sowie Löschkonzepte nach Zweckfortfall. Dies ist keine Rechtsberatung, sondern
    eine allgemeine Orientierung zur Recherche. Für verbindliche Aussagen einen
    Anwalt/Fachberater für Datenschutzrecht konsultieren.

### Allgemein (projektübergreifend)

14. **Frage:** Welche Pflichtangaben gehören in ein Impressum?
    **⚖️ Antwort:** In Deutschland u. a. Name/Firma, ladungsfähige Anschrift, Kontaktmöglichkeit,
    ggf. Vertretungsberechtigte, Handelsregisternummer und Umsatzsteuer-ID, je nach Rechtsform und
    Angebot. Dies ist keine Rechtsberatung, sondern eine allgemeine Orientierung zur Recherche.
    Für verbindliche Aussagen einen Anwalt/Fachberater für Telemedienrecht, Deutschland
    konsultieren.

15. **Frage:** Braucht eine Website mit Kontaktformular eine Cookie-Consent-Lösung?
    **⚖️ Antwort:** Sobald nicht technisch notwendige Cookies oder vergleichbare Technologien
    (z. B. Tracking-Pixel) eingesetzt werden, ist nach ePrivacy-Grundsätzen/DSGVO in der Regel
    eine Einwilligung vor Setzen der Cookies erforderlich; rein funktionale Formular-Cookies
    können anders zu bewerten sein. Dies ist keine Rechtsberatung, sondern eine allgemeine
    Orientierung zur Recherche. Für verbindliche Aussagen einen Anwalt/Fachberater für
    Datenschutz-/ePrivacy-Recht konsultieren.

## Rechts-Kategorie deaktivieren

Beim Setup kann die automatische Rechts-Kategorie explizit abgelehnt werden
(`includeLegalCategory: false` in `.fragenkatalog-config`). Empfohlen wird das nicht — auch ein
kleines Projekt profitiert davon, rechtliche Recherchepunkte früh sichtbar zu haben, statt sie
erst kurz vor Veröffentlichung zu entdecken.

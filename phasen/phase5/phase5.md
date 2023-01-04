# Phase 5

1. Identifizieren Sie notwendige Daten, die als Voraussetzung für die Angebotserstellung dienen.
    - <code>Grundriss</code>
    - <code>Hardware</code>

2. Analysieren Sie die Datenquellen hinsichtlich der der Bereitsteller/Orte und möglicher Datenformate in denen diese bereitgestellt werden können.


3. Untersuchen Sie die Datenformate/Datenquellen im Detail
    - a) welche Daten werden dargestellt
        <code>
        - Grundriss dargestellte Daten: Fläche, Längen, Flächenverteilung (z.B. Kanten), Anschlüsse (Steckdosen, Wasser), Stromleitungen (wenn Glück), Öffnungen (Türen, Fenster), Schrägen
        - ii.	Hardware: Größe, Gewicht, Kabellänge, Stromverbrauch (Sicherungsschutz), Arbeitsplatzergonomie (Beleuchtung, Klima)
        </code>

    - b) wie werden Daten in den Datenquellen dargestellt
        <code>
        i.	CAD-Format
        1.	Grundriss:
            - .skp
            - .3dm
        2.	Hardware
            - .3dm

        </code>
    - c) wie können diese importiert und sinnvoll weiterverarbeitet werden
        <code>
        - In .pdf abspeichern
        - Python hat ein rhino3dm-Modul
        </code>
    - d) welche Metainformationen sind zur Datenquelle vorhanden


4. Entscheiden Sie, wer die Daten innerhalb der ITSystemHausDD GmbH nutzen und verarbeiten darf.

5. Entscheiden Sie sich für ein Datenformat für das Angebot.

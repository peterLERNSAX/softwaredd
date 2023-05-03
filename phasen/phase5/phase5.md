# Phase 5

### Notwendige Daten 
1. Identifizieren Sie notwendige Daten, die als Voraussetzung für die Angebotserstellung dienen.
    - *Grundriss*
    - *IT-Komponenten/Hardware*

2. Analysieren Sie die Datenquellen hinsichtlich der der Bereitsteller/Orte und möglicher Datenformate in denen diese bereitgestellt werden können.
    - *Grundriss*:
        - *kann vom Kunden bereitgestellt werden als:*
            - *.pdf (Konvertierung in .step erforderlich)*
            - *.[Bildformat] (Konvertierung in .step erforderlich)*
            - *auf Papier (Konvertierung in .step erforderlich)*
            - *.step*
            - *andere 3D/2D-Formate (Konvertierung in .step erforderlich)*
        - *wenn kein Grundriss vorhanden:*
            - *Erstelllung vom Mitarbeiter im .step Format*
    - *Hardware*:
        - *wenn Modell vorhanden, dann als .step aus Datenbank*
        - *wenn Modell nicht vorhanden, dann .step erstellen*
        - *Technische Daten als Tabellenformat (muss in DB integriert werden)*

3. Untersuchen Sie die Datenformate/Datenquellen im Detail
    - a) welche Daten werden dargestellt
      
        - *Grundriss dargestellte Daten: Fläche, Längen, Flächenverteilung (z.B. Kanten), Anschlüsse (Steckdosen, Wasser), Stromleitungen (wenn Glück), Öffnungen (Türen, Fenster), Schrägen*
        - *Hardware: Größe, Gewicht, Kabellänge, Stromverbrauch (Sicherungsschutz), Arbeitsplatzergonomie (Beleuchtung, Klima)*
        

    - b) wie werden Daten in den Datenquellen dargestellt
    
        *CAD-Format*
        1.	*Grundriss:*
            - *.step*
        2.	*Hardware*
            - *.step*

    - c) wie können diese importiert und sinnvoll weiterverarbeitet werden
        - *In .pdf abspeichern*
        - *STEPutils als Python library*
    - d) welche Metainformationen sind zur Datenquelle vorhanden
        -  *Materialeigenschaften (Name, Dichte)*
	     - *geometrische und Baugruppenvalidierungseigenschaften*
	    - *Bezugselemente (Punkte, Ebenen, Achsen, Koordinatensysteme)*
	    - *benutzerdefinierte Parameter (Flächen, Kanten, Kurven)*
	    - *Produktherstellungsinformationen*
      
4. Entscheiden Sie, wer die Daten innerhalb der ITSystemHausDD GmbH nutzen und verarbeiten darf.
    - *ITSystemHausDD GmbH Innendienst*
      - *interne Anwendungsentwickler*
    - *Abteilung Einkauf*
      - *benötigt lediglich Zugriff auf die Daten der IT-Komponenten*
    - *Abteilung Verkauf*
      - *benötigt Zugriff auf alle Daten, die zur Angebotserstellung notwendig sind*

5. Entscheiden Sie sich für ein Datenformat für das Angebot.
  - *.step weil:*
    - *existierende Python library*
    - *kann mit kostenloser opensource Software erstellt und bearbeitet werden*
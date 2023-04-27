# Referentielle Integrität / Beziehungsintegrität

+ Bedingungen, die zur Sicherung der Datenintegrität bei Nutzung relationaler Datenbanken beitragen
+ Datensätze dürfen (über Fremdschlüssel) nur auf existierende Datensätze verweisen
  + Attributwerte eines Fremdschlüssel müssen auch als Attributwerte des Primärschlüssels vorhanden sein
+ Kontrolle der Beziehungen zwischen Datenbojekten   

## Erweiterungen

### Änderungsweitergabe (ÄW)
+ wenn eindeutiger Schlüssel gändert wird, kann DBMS Fremdschlüssel in allen abhängigen Datensätzen anpassen
  + Bsp.: Familienname bei Heirat wird geändert 

### Löschweitergabe (LW)
+ Löschung abhängiger Datensätze bei Löschung des Masterdatensatzes
  + Bsp.: Kunde wird gelöscht -> zugehörige Adresse wird ebenso gelöscht

## Nachteile
+ Prüfung der referentiellen Integrität kostet Rechnerressourcen (vor allem Zeit)
  + bei Import größerer Datenmengen sollten daher die RI-Regeln kurzzeitig außer Kraft gesetzt werden, insofern die Konsistenz der Daten gesichert ist 

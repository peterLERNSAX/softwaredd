# softwaredd
## Dokumentation

### Use-Case-Diagramm
![Schaubild Use-Case](static/images/use-case.png "Title")
[Use-Case Diagramm PDF](use-case.pdf)

### Sequenzdiagramm
![Schaubild Sequenzdiagramm](static/images/Sequenzdiagramm.png "Title")
[Sequenzdiagramm PDF](Sequenzdiagramm.pdf)
### Webserver

Aufsetzen eines Servers über WMware Workstation Player 16
- OS: Debian 11
- Benutzername: user
- Passwort: ******
- IP-Adresse: 192.168.72.129
- Software: Apache2 
- Ordner: /var/www/html/wiki
- Step-by-Step
```bash
  $ apt install apache2
  $ systemctl start apache2
  $ mkdir /var/www/html/wiki
  $ chown -R www-data:www-data /var/www/html/wiki
  $ chmod -R 755 /var/www/html/wiki
  $ nano /var/www/html/wiki/index.html
```
```html
  <html>
    <body>
      <p> Freunde der guten Unterhaltung, es funktioniert!</p>
    </body>
  </html>

```
```bash
  $ nano /etc/apache2/sites-available/wiki.conf
```
```html
  <VirtualHost *80>
	  DocumentRoot /var/www/html/wiki
	  ErrorLog ${APACHE_LOG_DIR}/error.log
	  CustomLOG ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
```
```bash
  $ a2ensite wiki.conf
  $ rm /etc/apache2/sites-enabled/000-default.conf
```

### Notwendige Daten 
1. Identifizieren Sie notwendige Daten, die als Voraussetzung für die Angebotserstellung dienen.
    - *Grundriss*
    - *Hardware*

2. Analysieren Sie die Datenquellen hinsichtlich der der Bereitsteller/Orte und möglicher Datenformate in denen diese bereitgestellt werden können.


3. Untersuchen Sie die Datenformate/Datenquellen im Detail
    - a) welche Daten werden dargestellt
      
        - *Grundriss dargestellte Daten: Fläche, Längen, Flächenverteilung (z.B. Kanten), Anschlüsse (Steckdosen, Wasser), Stromleitungen (wenn Glück), Öffnungen (Türen, Fenster), Schrägen*
        - *Hardware: Größe, Gewicht, Kabellänge, Stromverbrauch (Sicherungsschutz), Arbeitsplatzergonomie (Beleuchtung, Klima)*
        

    - b) wie werden Daten in den Datenquellen dargestellt
    
        *CAD-Format*
        1.	*Grundriss:*
            - .*skp*
            - *.3dm*
        2.	*Hardware*
            - *.3dm*

    - c) wie können diese importiert und sinnvoll weiterverarbeitet werden
        - *In .pdf abspeichern*
        - *Python hat ein rhino3dm-Modul*
    - d) welche Metainformationen sind zur Datenquelle vorhanden


4. Entscheiden Sie, wer die Daten innerhalb der ITSystemHausDD GmbH nutzen und verarbeiten darf.

5. Entscheiden Sie sich für ein Datenformat für das Angebot.

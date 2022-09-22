# softwaredd
## Dokumentation

### Use-Case-Diagramm
![Schaubild Use-Case](static/images/use-case.png "Title")
[Use-Case Diagramm PDF](use-case.pdf)

### Sequenzdiagramm
![Schaubild Sequenzdiagramm](static/images/Sequenzdiagramm.png "Title")
[Use-Case Diagramm PDF](Sequenzdiagramm.pdf)
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

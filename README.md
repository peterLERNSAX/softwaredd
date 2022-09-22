# softwaredd
## Dokumentation

### Use-Case-Diagramm
![Schaubild Use-Case](use-case.png "Title")
[Use-Case Diagramm PDF](use-case.pdf)

### Sequenzdiagramm
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

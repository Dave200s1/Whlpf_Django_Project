# Library management

Andrej Schreiner, David Stefanov, Daniel Wall, Justin Schiller

- Create a virtual environment: python -m venv venv
- Activate a virtual environment: venv\Scripts\activate.bat (Windows) oder source venv/bin/activate (Linux)
- Install package list: pip install -r requirements.txt
- Create new migration files: python manage.py makemigrations
- Apply migration to database: python manage.py migrate
- Import testdata from JSON: python manage.py loaddata \lib_app\testdata\testdata.json
- Statrt server: py manage.py runserver

Adresse der Website: http://127.0.0.1:8000/admin/
- Benutzername: admin
- Passwort: wwwwMMMM

Beispiel:
- http://127.0.0.1:8000/admin/lib_app/book/4/change/
- http://127.0.0.1:8000/admin/lib_app/movie/5/change/

Adresse der App: http://127.0.0.1:8000/lib_app/
- Benutzername: a.schreiner
- Passwort: ddddKKKK

- Benutzername: d.stefanov
- Passwort: hhhhDDDD

Test für Models ausführen: python manage.py test tests.test_models

## Andrej
- Django einrichten
- ER model entwerfen ( [ER.pdf](https://github.com/Dave200s1/Whlpf_Django_Project/blob/main/docs/db/ER.pdf) )
- Models erstellen
- Testdaten für die Datenbank erstellen (JSON)
- Testfälle für Models schreiben
- Administrator-Katalogs: Medien, Benutzer usw. suchen und filtern (admin part)
- Bootstrap einbauen und erstes Basetemplate anlegen, URLs anpassen
- Projektdokumentation (Readme)

## David
- ERM model entwerfen  ( [ERM.png](https://github.com/Dave200s1/Whlpf_Django_Project/blob/main/docs/db/ERM.png) )
- Views schreiben
- Testfälle für Views schreiben
- Benutzer: Medien anzeigen, ausleihen, reservieren, suchen und filtern (app part)
- Projektdokumentation (Readme)

## Daniel
- Wireframe erstellen  ( [Wireframes User Stories.pdf](https://github.com/Dave200s1/Whlpf_Django_Project/blob/main/docs/general/Wireframe%20User%20Storys.pdf) )
- Frontend HTML Template erstellen
- Anlegen eines Superusers zum Anmelden (python manage.py createsuperuser)
  
- Nutzername: admin
- Passwort: 123
- Anlegen einer middleware.py (Automatisches abmelden beim Aufruf der Seite)
- Superuser anmelden (Kein weiteres anmelden mehr möglich)
- Abmelde Button sowie Fehlermeldung beim Falsche eingeben eines Passwortes)
- User menü (Anmelden, Filtern, Ausleihe, Meine Artikel Frontend)
- Mitarbeit der Django Projekt Dokumentation
## Justin
- URL-Lists vorbereiten
- Benutzer: Empfehlungen anzeigen
- Benutzer: Bewertungen und Rezensionen
- Zusätzliche Django Projekt Dokumentation ( [Django Projekt Dokumentation.pdf](https://github.com/Dave200s1/Whlpf_Django_Project/blob/main/docs/general/Django%20Projekt%20Dokumentation.pdf) )

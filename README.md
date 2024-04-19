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

- http://127.0.0.1:8000/admin/lib_app/book/4/change/
- http://127.0.0.1:8000/admin/lib_app/movie/5/change/

Adresse der App: http://127.0.0.1:8000/lib_app/
- Benutzername: a.schreiner
- Passwort: ddddKKKK

- Benutzername: d.stefanov
- Passwort: hhhhDDDD

Test für Models ausführen: python manage.py test tests.test_models


## David
- ER und DB models entwerfen
- Views schreiben
- Testfälle für Views schreiben
- Benutzer: Medien anzeigen, ausleihen, reservieren, suchen und filtern
- Projektdokumentation (Readme)

## Daniel
- Wireframe erstellen
- Benutzer registrieren, an-, abmelden und Passwort zurücksetzen
- User menu hinzufügen
- Templates erweitern

## Andrej
- Django einrichten
- ER und DB models entwerfen
- Models erstellen
- Testdaten für die Datenbank erstellen (JSON)
- Testfälle für Models schreiben
- Administrator-Katalogs: Medien, Benutzer, Empfehlungen, Bewertungen
- Bootstrap einbauen und erstes Basetemplate anlegen
- Projektdokumentation (Readme)

## Justin
- URL-Lists vorbereiten
- Benutzer: Empfehlungen anzeigen
- Benutzer: Bewertungen und Rezensionen
- Zusätzliche Django Projekt Dokumentation ( [Django Projekt Dokumentation.pdf](https://github.com/Dave200s1/Whlpf_Django_Project/blob/main/docs/general/Django%20Projekt%20Dokumentation.pdf) )


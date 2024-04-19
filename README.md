# Library management
![npm bundle size (version)](https://img.shields.io/badge/version-0.0.1-green) ![npm bundle size (version)](https://img.shields.io/badge/language-python3-blue) ![npm bundle size (version)](https://img.shields.io/badge/framework-django5-darkgreen) ![npm bundle size (version)](https://img.shields.io/badge/framework-boostrap5-purple)

Copy the .txt file into the folder where you have cloned your repository, in order to be visible.

Andrej Schreiner, David Stefanov, Daniel Wall, Justin Schiller

- Create a virtual environment: python -m venv venv
- Activate a virtual environment: venv\Scripts\activate.bat (Windows) oder source venv/bin/activate (Linux)
- Install package list: pip install -r requirements.txt
- Create new migration files: python manage.py makemigrations
- Apply migration to database: python manage.py migrate
- Import testdata from JSON: python manage.py loaddata \lib_app\testdata\testdata.json
- Statrt server: py manage.py runserver

Adresse der Website: http://127.0.0.1:8000/admin/
Benutzername: admin
Passwort: wwwwMMMM

http://127.0.0.1:8000/admin/lib_app/book/4/change/
http://127.0.0.1:8000/admin/lib_app/movie/5/change/

http://127.0.0.1:8000/lib_app/
Benutzername: a.schreiner
Passwort: ddddKKKK

Benutzername: d.stefanov
Passwort: hhhhDDDD

Test für Models ausführen: python manage.py test tests.test_models

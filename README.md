# Library management

Copy the .txt file into the folder where you have cloned your repository, in order to be visible.

Install package list: pip install -r requirements.txt

Create new migration files: python manage.py makemigrations
Apply migration to database: python manage.py migrate
Import testdata from JSON: python manage.py loaddata \lib_app\testdata\testdata.json

Statrt server: py manage.py runserver

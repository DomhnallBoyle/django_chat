rm -rf django_chat/migrations/0001_initial.py*
python manage.py makemigrations
psql --dbname="postgres" --command="drop database django_chat;"
psql --dbname="postgres" --command="create database django_chat owner domhnall;"
python manage.py migrate
python manage.py loaddata django_chat/fixtures.json

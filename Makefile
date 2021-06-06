makemigrate_api:
	python manage.py makemigrations api

migrate_api:
	python manage.py migrate api --database=default

all_migrate_api:
	python manage.py migrate --database=default

run:
	python manage.py runserver

createsuperuser:
	python manage.py createsuperuser

install:
	pip install -r win_requirements.txt

freeze:
	pip freeze > win_requirements.txt

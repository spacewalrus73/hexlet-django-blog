run:
	poetry run python3 manage.py runserver
get migration:
	poetry run python3 manage.py makemigrations
see migrate:
	poetry run python3 manage.py sqlmigrate article 0001
migrate:
	poetry run python3 manage.py migrate
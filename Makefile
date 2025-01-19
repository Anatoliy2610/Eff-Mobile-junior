run:
	poetry run python manage.py runserver


migrate:
	poetry run python3 manage.py makemigrations
	poetry run python3 manage.py migrate

test:
	poetry run python3 manage.py test

check:
	poetry run ruff check restaurant

format:
	poetry run ruff format restaurant

isort:
	poetry run isort restaurant
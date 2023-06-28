#### Create a basic pyproject.toml with django as dependency:
`$ poetry init --no-interaction --dependency django`

#### Create venv with all dependencies needed:
`$ poetry install`

#### Init your project
`$ poetry run django-admin startproject apppile`

#### Let’s install psycopg2
`poetry add psycopg2`

#### For macOS if you can’t install or the above command doesn’t work, use the following command instead, just add — binary
`poetry add psycopg2-binary`

#### Create a new user with a password.
`CREATE ROLE admin WITH LOGIN PASSWORD 'admin';`
`ALTER ROLE admin CREATEDB;`

#### In the root of the apppile project, run server:
`poetry run python3 manage.py runserver`


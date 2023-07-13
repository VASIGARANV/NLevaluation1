#### Init your project
`$ django-admin startproject appisle`

#### Let’s install psycopg2
`poetry add psycopg2`

#### For macOS if you can’t install or the above command doesn’t work, use the following command instead, just add — binary
`poetry add psycopg2-binary`

#### Start the Postgres in terminal
`psql postgres`

#### Create a new user with a password.
`CREATE ROLE admin WITH LOGIN PASSWORD 'admin';`

`ALTER ROLE admin CREATEDB;`

#### In the root of the apppile project, run server:
`python3 manage.py runserver`


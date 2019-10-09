# API Flask

Execução manual

- Na raiz:
	- $ pipenv --three
	- $ pipenv shell
	- $ export FLASK_APP=run.py
	- $ export FLASK_ENV=development
	- $ flask run

Modo iterativo:
	- $ flask shell

### Flask DB
	- Comandos do flask db:
	- flask db init: prepara as migrations (models.py)
	- flask db migrate: excuta as migrations
	- flask db upgrade: envia as alterações no banco de dados
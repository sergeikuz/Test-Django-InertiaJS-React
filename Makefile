run:
	uv run python manage.py runserver
	
migrate:
	uv run python manage.py migrate

makemigrations:
	uv run python manage.py makemigrations

install:
	uv sync && cd frontend && npm install && npm run build

admin:
	uv run manage.py createsuperuser

start-backend:
	uv run manage.py runserver

start-frontend:
	cd frontend && npm run dev

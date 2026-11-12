up:
	docker compose up -d

down:
	docker compose down

restart:
	docker compose restart

reload: down up

build:
	docker compose build

.PHONY: up down restart reload build

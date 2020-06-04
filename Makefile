run: down
	docker-compose up -d --build
	docker-compose ps
.PHONY: run

down:
# 	docker-compose down
	docker-compose down --volumes
.PHONY: down

mongo:
	docker-compose exec mongo mongo paranuara
.PHONY: mongo

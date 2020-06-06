run: down
	docker-compose up -d --build
	docker-compose ps
.PHONY: run

test:
	docker-compose -f docker-compose.yaml -f docker-compose-test.yaml up --build --abort-on-container-exit --exit-code-from api api
.PHONY: test

test-cov:
	docker-compose -f docker-compose.yaml -f docker-compose-test.yaml -f docker-compose-test-cov.yaml up --build --abort-on-container-exit --exit-code-from api api
.PHONY: test

down:
	docker-compose down --volumes
.PHONY: down

mongo:
	docker-compose exec mongo mongo paranuara
.PHONY: mongo

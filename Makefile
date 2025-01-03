black-lint:
	black .

black-check:
	black . --check

flake8-check:
	flake8 . --config=.flake8

lint-check: black-check flake8-check

lint-build: black-lint flake8-check

tests:
	pytest app/tests

main:
	docker-compose -f dev.yaml up --build

test:
	docker-compose -f test.yaml up --build
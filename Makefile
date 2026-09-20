.PHONY: install test lint format run

install:
	python -m pip install -e '.[dev]'

test:
	pytest -q

lint:
	ruff check .

format:
	ruff format .

run:
	python -m yby_zero.main

install:
	uv sync

build:
	uv build

reinstall-package:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff --fix

test:
	uv run pytest

check: test lint

test-coverage:
	uv run pytest --cov=gendiff --cov-report xml

.PHONY: install test lint check build

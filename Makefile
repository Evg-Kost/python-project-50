install:
	uv sync

build:
	uv build

reinstall-package:
	uv tool install --force dist/*.whl

lint:
	uv run ruff check gendiff

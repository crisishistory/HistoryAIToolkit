format:
	ruff format .

lint:
	ruff check . --fix

test:
	pytest tests/code/*.py

test_llms:
	pytest tests/llms/*.py
# run all test without verbose mode
test:
	pytest Pytest-Playground/

# run all test in verbose mode
test-v:
	pytest -v Pytest-Playground/

# run all test in parallel
test-p:
	pytest -v -n auto Pytest-Playground/
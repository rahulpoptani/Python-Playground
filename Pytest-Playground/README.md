### test a single file
pytest tests/test_my_functions.py

### Run all test in verbose mode
pytest -v

### Run test for a single class from a test file
pytest -v Pytest-Playground/tests/test_rough.py::TestRough

### Run a single test from a test file
pytest -v Pytest-Playground/tests/test_rough.py::TestRough::test_type

### include print statements
pytest -s Pytest-Playground/tests/test_fixtures.py 
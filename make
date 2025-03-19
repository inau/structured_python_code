install: .env
    python -m venv .env

run: install
    .env\Scripts\pip install -r requirements.txt

run_test: install
    .env\Scripts\python -m pytest

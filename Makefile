init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

codestyle:
	python -m pylint --disable=import-error,no-name-in-module **/*.py

test:
	python -m unittest discover -s . -p "*tests*.py"

init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

codestyle:
	flake8 .

test:
	python -m unittest discover -s tests -p "*tests*.py"

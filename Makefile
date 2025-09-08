init:
	pip install -r requirements.txt
	pip install -r requirements-dev.txt

codestyle:
	flake8 .

test:
	python3 -m unittest discover -s tests -p "*tests*.py"

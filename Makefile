clean:
	find . -name "*.pyc" -exec rm -rf {} \;
	rm -rf *.log

prepare:
	python3.8 -m venv venv
	. venv/bin/activate && pip install -r requirements.txt

unit_tests:
	. venv/bin/activate && pytest -s
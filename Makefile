run:
	python manage.py
	
py_clean:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf

run_tests:
	pytest tests/ -v

lint_check:
	pylint src/*

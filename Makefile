venv: venv/setup

venv/setup:
	test -d venv || virtualenv venv;
	. venv/bin.activate;
	pip install -Ur requirements.txt;
	touch venv/setup

run: venv
	. venv/bin/activate; moq-runner

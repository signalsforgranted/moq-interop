venv: venv/setup

venv/setup:
	test -d venv || python3 -m virtualenv venv
	. venv/bin/activate
	pip3 install -Ur requirements.txt
	python3 setup.py install
	touch venv/setup

run: venv
	. venv/bin/activate; moq-interop-runner

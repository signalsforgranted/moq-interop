venv: venv/setup

venv/setup:
	@test -d venv || python3 -m virtualenv venv
	@. venv/bin/activate
	pip3 install -U pip setuptools wheel
	pip3 install .[dev]
	@touch venv/setup

clean:
	@rm -rf venv *.egg-info build dist
	@find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

run: venv
	@. venv/bin/activate; moq-interop-runner

test: venv
	@. venv/bin/activate; coverage run -m unittest

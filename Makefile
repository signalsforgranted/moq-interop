venv: venv/setup

venv/setup:
	@test -d venv || python3 -m virtualenv venv
	@. venv/bin/activate
	pip3 install -Ur requirements.txt
	pip3 install -e .
	@touch venv/setup

clean:
	@rm -rf venv *.egg-info/

run: venv
	@. venv/bin/activate; moq-interop-runner

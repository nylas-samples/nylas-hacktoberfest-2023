#Ensure the script is run as bash
SHELL:=/bin/bash

#Set help as the default for this makefile.
.DEFAULT: help

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo ""
	@echo "venv                     Create a virtual environment"
	@echo "install                  Install the package and all required core dependencies"
	@echo "run                      Running the app locally"
	@echo "clean                    Remove all build, test, coverage and Python artifacts"

clean: clean-build clean-pyc clean-test

generate_dot_env:
	@if [[ ! -e .env ]]; then \
		cp .env.example .env; \
	fi

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

venv:
	@echo ""
	@echo "*** make a virtual env with poetry***"
	@echo ""
	curl -sSL https://install.python-poetry.org | python3 - --version 1.6.1
	poetry shell
	@echo ""

install: generate_dot_env
	@echo ""
	@echo "*** Generating a .env file and installing the required dependencies... ***"
	@echo ""
	poetry install --only main
	@echo ""

run:
	@echo ""
	@echo "*** Running the app locally... ***"
	@echo ""
	@echo ""
	poetry run update_calendar
	@echo ""

define PRINT_HELP_PYSCRIPT # start of Python section
import re, sys

output = []
# Loop through the lines in this file
for line in sys.stdin:
    # if the line has a command and a comment start with
    #   two pound signs, add it to the output
    match = re.match(r'^([a-zA-Z_%-]+):.*?## (.*)$$', line)
    if match:
        target, help = match.groups()
        output.append("%-18s %s" % (target, help))
# Sort the output in alphanumeric order
output.sort()
# Print the help result
print('\n'.join(output))
endef
export PRINT_HELP_PYSCRIPT # End of python section


CURRENT_GIT_BRANCH = $(shell git branch --show-current)

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

mypy: ## Run mypy in container
ifeq ($(ARGS),)
	mypy cases dashboard positions company main
else
	mypy ${ARGS}
endif

test: ## Run tests
	python -Wd -m coverage run --branch --source=jsonpatch tests.py
	coverage report --show-missing

coverage: ## Run tests with coverage
	coverage run --source=jsonpatch tests.py
	coverage report -m

# Generate requirements files
requirement%.txt: requirement%.in  ## Build requirements files
	pip-compile $${UPGRADE:+-U} -v --resolver backtracking --strip-extras \
		--emit-find-links --no-allow-unsafe --annotate --generate-hashes \
		--reuse-hashes -o $@ $<

requirements: requirements.txt requirements-dev.txt ## Build requirements

requirements-upgrade:
	$(MAKE) -B requirements UPGRADE=1

venv:	## Create and update virtualenv
	@test -d .venv || python -m venv .venv
	@.venv/bin/pip install -U pip
	@.venv/bin/pip install --no-deps -r requirements.txt -r requirements-dev.txt

.PHONY: requirements help venv


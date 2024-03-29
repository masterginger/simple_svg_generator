VENV_DIR = .venv
VENV_BIN = $(VENV_DIR)/bin
PYTHON_BIN = $(VENV_BIN)/python
PIP_BIN = $(VENV_BIN)/pip
BLACK_BIN = $(VENV_BIN)/black
MYPY_BIN = $(VENV_BIN)/mypy
RUFF_BIN = $(VENV_BIN)/ruff
COVERAGE_BIN = $(VENV_BIN)/coverage

.PHONY: venv
venv:
	python -m venv .venv
	$(PIP_BIN) install -e '.[dev]'

.PHONY: lint
lint:
	$(BLACK_BIN) src tests
	$(RUFF_BIN) check src tests --fix
	$(MYPY_BIN) src tests

.PHONY: test
test: lint
	$(COVERAGE_BIN) run -m pytest && $(COVERAGE_BIN) report -m --fail-under=100 && $(COVERAGE_BIN) html

.PHONY: gen
gen:
	@$(PYTHON_BIN) -m ssg gen $(NAME)

.PHONY: gen-and-show
gen-and-show:
	@$(PYTHON_BIN) -m ssg gen --show $(NAME)

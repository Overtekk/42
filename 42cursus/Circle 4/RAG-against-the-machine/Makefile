# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Makefile                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/19 19:29:48 by roandrie        #+#    #+#               #
#  Updated: 2026/09/01 09:38:29 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# ===================
# =		VARIABLES	=
# ===================
# -- Base python commands --
PYTHON			=	python3
PDB 			=	python3 -m pdb
UV_PYTHON		=	uv run python
UV_FLAKE8		=	uv run flake8
UV_MYPY 		=	uv run mypy
MYPY_FLAGS		=	--warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
INSTALL_UV		=	curl -LsSf https://astral.sh/uv/install.sh | sh
CHECK_UV		=	command -v uv

# -- Files & Folders --
SRC				=	src
LINT_TESTER		=	$(SRC)

RUN				=	$(UV_PYTHON) -m $(SRC)

# -- Index command --
max_chunk_size 	?=	2000
# -- Search/Answer command --
query			?=
k				?= 10
context_limit	?= 5000
# -- Search dataset command --
dataset_path	?= "data/datasets/"
save_directory	?= "data/output/search_results/"
answer_save_directory ?= "data/output/search_results_and_answer/"


# ===================
# =		RULES		=
# ===================

.PHONY:		all install run run-debug clean fclean delete-uv  \
			lint lint-strict lint-format \
			index search search_dataset answer answer_dataset eval \
			moulinette moulinette_answer moulinette_search
.SILENT:

all:				install run

install:
					@if	! $(CHECK_UV) > /dev/null 2>&1; then \
							echo "$(BRED)UV not installed. Installing...$(RESET)"; \
							$(INSTALL_UV); \
					fi
					@echo "$(BGREEN)Installing project dependencies using uv...$(RESET)"
					$(UV_SKIP_WHEEL) uv sync $(UV_WARN)

run:				install
					@clear
					$(RUN) execute_pipeline

index:				install
					@clear
					$(RUN) index --max_chunk_size=$(max_chunk_size)

search:				install
					@clear
					$(RUN) search --query="$(query)" --k=$(k)

search_dataset:		install
					@clear
					$(RUN) search_dataset --dataset_path="$(dataset_path)" --k=$(k) --save_directory="$(save_directory)"

answer:				install
					@clear
					$(RUN) answer --query="$(query)" --k=$(k) --context_limit=$(context_limit)

answer_dataset:		install
					@clear
					$(RUN) answer_dataset --student_search_results_path="$(save_directory)" --save_directory="$(answer_save_directory)" --context_limit=$(context_limit)

evaluate:			install
					@clear
					$(RUN) evaluate --student_search_results_path="$(save_directory)" --dataset_path="$(dataset_path)"

moulinette:
					@echo "Use either 'moulinette_search' or 'moulinette_answer'"

moulinette_search:
					chmod u+x run-moulinette.sh
					./run-moulinette.sh evaluate_search

moulinette_answer:
					chmod u+x run-moulinette.sh
					./run-moulinette.sh evaluate_answer

run-debug:			install
					@clear
					$(RUN)

clean:
					@echo "$(YELLOW)Cleaning temporary files, caches and data... 🗑️$(RESET)"
					find . -type d -name "__pycache__" -exec rm -rf {} +
					find . -type f -name "*.pyc" -delete
					find . -type f -name "*.pyo" -delete
					rm -rf .mypy_cache
					rm -rf .pytest_cache
					rm -rf data/

fclean:				clean
					@echo "$(YELLOW)Cleaning .venv, build and dist folder... 🗑️$(RESET)"
					rm -rf .venv
					rm -rf dist

lint:
					@clear
					@echo "$(BMAGENTA)Running standard linting...$(RESET)"
					@status=0; \
					$(UV_FLAKE8) $(LINT_TESTER) || status=$$?; \
					$(UV_MYPY) $(LINT_TESTER) $(MYPY_FLAGS) || status=$$?; \
					exit $$status

lint-strict:
					@clear
					@echo "$(BMAGENTA)Running strict linting...$(RESET)"
					@status=0; \
					$(UV_FLAKE8) $(LINT_TESTER) || status=$$?; \
					$(UV_MYPY) $(LINT_TESTER) $(MYPY_FLAGS) --strict || status=$$?; \
					exit $$status

lint-format:
					uv run ruff format

delete-uv:
					@if $(CHECK_UV) > /dev/null 2>&1; then \
							echo "$(BRED)Deleting uv...$(RESET)"; \
							rm -f $$(which uv); \
					else \
							echo "$(BRED)UV not installed. Cannot delete. Abording.$(RESET)"; \
					fi

# ===================
# =		COLORS		=
# ===================

RESET		=	\033[0m
BGREEN		=	\033[92m
BMAGENTA	=	\033[95m
YELLOW		=	\033[93m
BRED		=	\033[91m

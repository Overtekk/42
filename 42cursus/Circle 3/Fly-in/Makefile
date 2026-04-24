# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Makefile                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 18:22:36 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 10:39:37 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

# ===================
# =		VARIABLES	=
# ===================
PYTHON		=	uv run python
PDB 		=	uv run python -m pdb
FLAKE8		=	uv run flake8
MYPY 		=	uv run mypy
MYPY_FLAGS	=	--warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
SRC_MODULE	=	src
INSTALL_UV	=	curl -LsSf https://astral.sh/uv/install.sh | sh
CHECK_UV	=	command -v uv

# Launch with a custom map. Use "make run M=<path to map>"
M			=

# ===================
# =		RULES		=
# ===================

.PHONY:		all install run run-script run-debug debug clean lint lint-strict delete-uv
.SILENT:

all:		install run

install:
			@if	! $(CHECK_UV) > /dev/null 2>&1; then \
					echo "$(BRED)UV not installed. Installing...$(RESET)"; \
					$(INSTALL_UV); \
			fi
			@echo "$(BGREEN)Installing project dependencies using uv...$(RESET)"
			uv sync

run:
			$(PYTHON) -m $(SRC_MODULE) $(M)

run-debug:
			$(PYTHON) -m $(SRC_MODULE) $(M) --debug

debug:		install
			@echo "$(BGREEN)Running the main script in debug mode...$(RESET)"
			$(PDB) -m $(SRC_MODULE)

clean:
			@echo "$(YELLOW)Cleaning temporary files and caches... 🗑️$(RESET)"
			find . -type d -name "__pycache__" -exec rm -rf {} +
			find . -type f -name "*.pyc" -delete
			find . -type f -name "*.pyo" -delete
			rm -rf .mypy_cache
			rm -rf .pytest_cache

lint:
			@clear
			@echo "$(BMAGENTA)Running standard linting...$(RESET)"
			@status=0; \
			$(FLAKE8) $(SRC_MODULE) || status=$$?; \
			$(MYPY) $(SRC_MODULE) $(MYPY_FLAGS) || status=$$?; \
			exit $$status

lint-strict:
			@clear
			@echo "$(BMAGENTA)Running strict linting...$(RESET)"
			@status=0; \
			$(FLAKE8) $(SRC_MODULE) || status=$$?; \
			$(MYPY) $(SRC_MODULE) $(MYPY_FLAGS) --strict || status=$$?; \
			exit $$status

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

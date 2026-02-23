# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Makefile                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42.fr>         +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 18:22:36 by roandrie        #+#    #+#               #
#  Updated: 2026/02/23 18:22:54 by roandrie        ###   ########.fr        #
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
UV			=	curl -LsSf https://astral.sh/uv/install.sh | sh

# ===================
# =		RULES		=
# ===================

.PHONY:		all install run debug clean lint lint-strict
.SILENT:

all:		install run

install:
			@echo "$(BGREEN)Installing project dependencies using uv...$(RESET)"
			uv sync

run:
			$(PYTHON) -m $(SRC_MODULE)

debug:
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
			@echo "$(BMAGENTA)Running standard linting...$(RESET)"
			$(FLAKE8) $(SRC_MODULE)
			$(MYPY) $(SRC_MODULE) $(MYPY_FLAGS)

lint-strict:
			@echo "$(BMAGENTA)Running strict linting...$(RESET)"
			$(FLAKE8) $(SRC_MODULE)
			$(MYPY) $(SRC_MODULE) --strict

# ===================
# =		COLORS		=
# ===================

RESET		=	\033[0m
BGREEN		=	\033[92m
BMAGENTA	=	\033[95m
YELLOW		=	\033[93m

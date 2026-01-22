# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: roandrie <roandrie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/20 16:18:29 by roandrie          #+#    #+#              #
#    Updated: 2026/01/21 11:42:10 by roandrie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

VENV_PATH = .venv
VENV_PYTHON = $(VENV_PATH)/bin/python3
VENV_PIP = $(VENV_PATH)/bin/pip

PYTHON = $(if $(wildcard $(VENV_PYTHON)), $(VENV_PYTHON), python3)
PIP = $(if $(wildcard $(VENV_PIP)), $(VENV_PIP), pip)

MYPY_FLAGS= --warn-return-any --warn-unused-ignores --ignore-missing-imports \
			--disallow-untyped-defs --check-untyped-defs

SRC_FILES=a_maze_ing.py src/
CONFIG=config.txt

# Prevent rule to be associated with files.
.PHONY: install run debug clean lint lint-strict venv pipfreeze all

# Install all dependencies needed for this project.
install:
				@echo "$(BLUE)Installing dependencies...$(RESET)"
				@$(PIP) install -r requirements.txt
				@echo "$(GREEN)✔ Dependencies installed!$(RESET)"

# Run the main script of the project.
run:
				@echo ""
				@$(PYTHON) a_maze_ing.py $(CONFIG)
				@echo ""

# Run the main script in debug mode.
debug:
				@echo "$(YELLOW)Running in DEBUG mode$(RESET)"
				@$(PYTHON) -m pdb a_maze_ing.py

# Remove temporary files or caches.
clean:
				@echo "$(RED)🚽 Cleaning...$(RESET)"
				@find . -type d -name "__pycache__" -exec rm -rf {} +
				@find . -type f -name "*.pyc" -delete
				@rm -rf .mypy_cache
				@rm -rf .pytest_cache
				@rm -rf .coverage

# Check the norme.
lint:
				@-flake8 ${SRC_FILES}
				@-mypy ${SRC_FILES} $(MYPY_FLAGS)

# Check the norm with strict.
lint-strict:
				@-flake8 ${SRC_FILES}
				@-mypy ${SRC_FILES} $(MYPY_FLAGS) --strict

# Install the virtual environment.
venv:
				@echo "$(BLUE)Create virtual environment$(RESET)"
				@python3 -m venv .venv
				@echo "$(BLUE)Run 'source .venv/bin/activate' to go to the virtual environment."

# Create/update the requirements.txt
pipfreeze:
				@pip freeze > requirements.txt

# Create venv and install dependencies.
all: venv install
				@echo "$(GREEN)✔ Environment set up ready!$(RESET)"

# Colors
RESET=\033[0m
RED=\033[1;31m
BLUE=\033[1;34m
GREEN=\033[1;32m
YELLOW=\033[1;33m

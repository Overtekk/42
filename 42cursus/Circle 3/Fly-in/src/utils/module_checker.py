# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  module_checker.py                                 :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/01 18:03:34 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 10:55:39 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Runtime dependency verification utility.

This module provides a mechanism to check for the existence of required
third-party libraries before the main application attempts to import them,
ensuring a clean error message instead of an import crash.
"""

import importlib.metadata


def module_checker() -> None:
    """Verifies that all required third-party dependencies are installed.

    Iterates through a strict list of required packages and attempts to
    locate their specifications using `importlib.metadata`. This prevents the
    application from crashing with a standard ImportError later on.

    Raises:
        ModuleNotFoundError: If a required package is not found in the current
                             environment.
    """

    required = ['pydantic', 'arcade']
    missing: list[str] = []

    for package_name in required:
        try:
            importlib.metadata.version(package_name)
        except importlib.metadata.PackageNotFoundError:
            missing.append(package_name)

    if missing:
        miss_module = ", ".join(missing)
        raise ModuleNotFoundError(f"missing dependencies {miss_module}.\nUse "
                                  "'uv run python3 run.py <map>' instead.")

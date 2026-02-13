# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  modules_check.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:42:58 by roandrie        #+#    #+#               #
#  Updated: 2026/02/09 08:30:09 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Runtime dependency verification utility.

This module provides a mechanism to check for the existence of required
third-party libraries before the main application attempts to import them,
ensuring a clean error message instead of an import crash.
"""

import importlib.util


def module_checker() -> None:
    """Verifies that all required third-party dependencies are installed.

    Iterates through a strict list of required packages and attempts to
    locate their specifications using `importlib`. This prevents the
    application from crashing with a standard ImportError later on.

    Raises:
        ModuleNotFoundError: If a required package is not found in the current
                             environment. The error message includes
                             instructions to run 'make install'.
    """

    required = ['pydantic', 'colorama']

    for module_name in required:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            raise ModuleNotFoundError(f"missing dependency {module_name}."
                                      "\nUse 'make install' first.")

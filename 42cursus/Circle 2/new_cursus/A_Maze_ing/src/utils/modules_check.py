# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  modules_check.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:42:58 by roandrie        #+#    #+#               #
#  Updated: 2026/02/05 13:25:10 by rruiz           ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""Simple runtime dependency checker.

Raises `ModuleNotFoundError` with an instructive message when a
required dependency is not available.
"""

import importlib.util


def module_checker() -> None:
    """Assert that required third-party modules are importable.

    Raises:
        ModuleNotFoundError: If any required package is missing.
    """

    required = ['pydantic', 'colorama']

    for module_name in required:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            raise ModuleNotFoundError(f"missing dependency {module_name}."
                                      "\nUse 'make install' first.")

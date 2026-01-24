# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  modules_check.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie, rruiz                           +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/01/22 10:42:58 by roandrie        #+#    #+#               #
#  Updated: 2026/01/22 15:05:59 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import importlib.util


def module_checker() -> None:

    required = ['pydantic', 'colorama']

    for module_name in required:
        spec = importlib.util.find_spec(module_name)
        if spec is None:
            raise ModuleNotFoundError(f"missing dependency {module_name}."
                                      "\nUse 'make install' first.")

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  print_debug.py                                    :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/02 14:02:40 by roandrie        #+#    #+#               #
#  Updated: 2026/04/22 10:58:57 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Debug utilaty tool to show validated data. Only showed in the debug mode
state.
"""

from src.models import JsonFunctionCalling, JsonFunctionDefinition
from src.utils import print_log, print_rule


def debug_print_validated_data(data: list[JsonFunctionDefinition] |
                               list[JsonFunctionCalling]) -> None:
    """Print all validated data to the standard stdout.

    Args:
        data (list[JsonFunctionDefinition] | list[JsonFunctionCalling]): a list
        containing a list of Json Function.
    """
    for element in data:
        print(element)
        print("")


def debug_print_generating_process(instructions: str, state: str) -> None:
    """Print the generating process including the instructions for the LLM and
    a rule to delimers each generation.

    Args:
        instructions (str): The instructions formatted for the LLM
        state (str): The generation state
    """
    print_rule(f"Generating {state}")
    print_log(f"-DEBUG-\nInstructions:\n\n{instructions}\n")

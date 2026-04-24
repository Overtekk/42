# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  parser.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 10:25:17 by roandrie        #+#    #+#               #
#  Updated: 2026/04/22 10:55:17 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Main parsing and validation orchestrator.

This module consolidates the command-line argument parsing, environment
verification, and JSON data validation into a single workflow. It ensures
all inputs are strictly compliant with the project's requirements before
the function calling logic begins.
"""

from typing import Any, Tuple
from argparse import Namespace

from src.models import JsonFunctionCalling, JsonFunctionDefinition
from src.utils import print_log, print_rule, print_logo, func_timer
from src.debug import debug_print_validated_data
from src.parser import (argument_parser, validate_json_content,
                        check_llm_available)


@func_timer
def parse() -> Tuple[Namespace, dict[str, list[JsonFunctionDefinition] |
                                     list[JsonFunctionCalling]]]:
    """
    Execute the complete input parsing and validation pipeline.

    This function coordinates several critical steps:
    1. Parses CLI arguments to determine file paths and flags.
    2. Verifies the presence of the LLM SDK and model files.
    3. Validates the structure of the function definitions and prompt tests
       against their respective Pydantic schemas.
    4. Logs validation results and provides debug visualization if requested.

    Returns:
        Tuple[Namespace, dict]: A tuple containing:
            - The parsed Namespace with execution configurations.
            - A dictionary containing lists of validated
              JsonFunctionDefinition and JsonFunctionCalling models.

    Note:
        This function is decorated with @func_timer to monitor the
        total time spent on environment and data preparation.
    """
    args: Namespace = argument_parser()
    check_llm_available()

    validation_map: dict[str, Any] = {
        "func_call": args.func_call,
        "func_def": args.func_def
    }

    validated_data: dict[str, list[JsonFunctionDefinition] |
                         list[JsonFunctionCalling]] = {}

    for schema_type, path in validation_map.items():
        validated_data[schema_type] = validate_json_content(path,
                                                            schema_type)

    print_logo()
    print_rule("")
    print_log(
        f"Successfully validated {len(validated_data['func_def'])} function "
        "definitions."
    )
    print_log(
        f"Successfully validated {len(validated_data['func_call'])} function "
        "calling."
    )

    if args.debug:
        print_rule("", "white")
        print("-DEBUG-")
        debug_print_validated_data(validated_data['func_def'])
        debug_print_validated_data(validated_data['func_call'])

    return (args, validated_data)

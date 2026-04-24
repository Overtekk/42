# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __main__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/23 16:39:56 by roandrie        #+#    #+#               #
#  Updated: 2026/04/24 15:53:48 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any, Tuple, cast
from argparse import Namespace

import sys

from src.generate import generate_answer
from src.parser import parse
from src.utils import print_error, print_rule, print_log
from src.models import JsonFunctionCalling, JsonFunctionDefinition
from src.engine import CallMeMaybe, Prompt, Output


def main() -> int:
    try:
        # Verify that all data are correct
        parsed_data: Tuple[Namespace, Any] = parse()
        args, validated_data = parsed_data

        # Init all needed objects
        ai: CallMeMaybe = CallMeMaybe(
            model_name=args.model,
            functions_definition_path=cast(list[JsonFunctionDefinition],
                                           validated_data['func_def']),
            visualizer=args.visualizer,
            debug=args.debug
        )

        if args.debug:
            print_rule("")

        prompter: Prompt = Prompt(
            functions_calling=cast(list[JsonFunctionCalling],
                                   validated_data['func_call']),
            visualizer=args.visualizer,
            debug=args.debug
        )

        output: Output = Output(
            output_file_path=args.output,
            visualizer=args.visualizer,
            debug=args.debug
        )

        if args.debug:
            print_rule("")

        # Generation process
        generate_answer(ai, prompter, args, output)

        # Write generated result in the output file
        output.write_output()

        print_log("\nGeneration completed. Thanks for you patience!\n")

        return 0

    except ValueError as e:
        print_error(f"{e}")
        return 1
    except Exception as e:
        print_error(f"Critical error: {e}")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())

    except KeyboardInterrupt:
        print_error("\nProgram interrupted by user.")
        sys.exit(130)

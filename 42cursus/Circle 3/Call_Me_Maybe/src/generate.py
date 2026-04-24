# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  generate.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/22 10:29:07 by roandrie        #+#    #+#               #
#  Updated: 2026/04/22 10:40:25 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from typing import Any
from argparse import Namespace

from src.utils import print_log, func_timer
from src.engine import CallMeMaybe, Prompt, Output


@func_timer
def generate_answer(ai: CallMeMaybe, prompter: Prompt, args: Namespace,
                    output: Output) -> None:
    counter: int = 1

    print_log("Generation in process...")

    while True:
        # Get the next prompt from the list
        prompt: str = prompter.get_next_prompt()

        # If there is no more promp, break the loop
        if prompt == "empty":
            if args.debug:
                print_log("-DEBUG-\nNo more prompt available.")
            break

        # Store the result to write it in the output at the end
        result: dict[Any, Any] = ai.run(prompt)
        output.store_result(prompt, result)

        # Print the sequence action
        if not args.visualizer:
            print_log(f"Prompt {counter} finished.")
        counter += 1

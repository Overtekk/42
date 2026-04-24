# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  prompt.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/04 12:04:02 by roandrie        #+#    #+#               #
#  Updated: 2026/04/24 09:49:20 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Prompt management module.

This module is responsible for loading, formatting, and distributing the
natural language prompts sequentially to the LLM engine. It extracts the
raw strings from the parsed JSON schema models.
"""

from typing import Any, List

from pydantic import BaseModel, Field, PrivateAttr

from src.models import JsonFunctionCalling
from src.utils import print_log


class Prompt(BaseModel):
    """
    Manager for the user prompts queued for processing.

    Attributes:
        functions_calling (List[JsonFunctionCalling]): The list of parsed
            prompt objects loaded from the input JSON file.
        visualizer (bool): Flag to enable visualizer mode.
        debug (bool): Flag to enable detailed debug logging.
    """

    functions_calling: List[JsonFunctionCalling] = Field(
        description='Path where promps are stored (json files)'
    )
    visualizer: bool = Field(
        description="The state of the visualizer",
        default=False
    )
    debug: bool = Field(
        description="The state of the debug mode",
        default=False
    )

    _list_prompts: List[str] = PrivateAttr()

    def model_post_init(self, _: Any) -> None:
        """Initialize the private list of prompts after model validation."""

        self._list_prompts: List[str] = []
        self._format_prompt()

    def get_next_prompt(self) -> str:
        """
        Retrieve and remove the next prompt from the queue.

        Returns:
            str: The raw natural language prompt string. Returns "empty"
            if the queue is depleted.
        """
        if self._list_prompts:
            return self._list_prompts.pop(0)

        else:
            return "empty"

    def _format_prompt(self) -> None:
        """
        Extract raw strings from the Pydantic models and populate the queue.

        Iterates through the provided JsonFunctionCalling objects, extracts
        the prompt strings, and stores them internally for sequential
        retrieval.
        Logs the process if debug mode is active.
        """
        skipped_prompt: int = 0

        for prompt in self.functions_calling:
            formatted_prompt = prompt.prompt

            # Skip if the prompt is empty
            if not formatted_prompt or formatted_prompt.isspace():
                if self.debug:
                    print("Empty promp. Skipping.")
                skipped_prompt += 1
                continue

            if self.debug:
                print_log(f"-DEBUG-\nNew prompt added: {formatted_prompt}")

            self._list_prompts.append(formatted_prompt)

        if skipped_prompt > 0:
            print_log(
                "[bright_yellow]"
                "[WARNING]\n"
                f"{skipped_prompt} prompts skipped.\n\n"
                "[/bright_yellow]"
                )

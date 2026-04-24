# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Output.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/20 17:28:32 by roandrie        #+#    #+#               #
#  Updated: 2026/04/23 14:25:15 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Output management module.

This module is responsible for accumulating the generated function calls
and formatting them into the required JSON structure. It handles the
in-memory storage during the generation loop and the final export to
the designated output file.
"""

from typing import Any

import json

from pathlib import Path
from pydantic import BaseModel, Field, PrivateAttr

from src.utils import print_log


class Output(BaseModel):
    """
    Manager for formatting and exporting LLM execution results.

    Attributes:
        output_file_path (Path): The destination path where the final JSON
                                 results will be written.
        visualizer (bool): Flag to enable visualizer mode.
        debug (bool): Flag to enable detailed debug logging.
    """

    output_file_path: Path = Field(
        description='Path where the output will be writted'
    )
    visualizer: bool = Field(
        description="The state of the visualizer",
        default=False
    )
    debug: bool = Field(
        description="The state of the debug mode",
        default=False
    )

    _result_data: list[dict[Any, Any]] = PrivateAttr(default_factory=list)

    def model_post_init(self, context: Any) -> None:
        """Initialize the private internal storage after model validation."""
        self._result_data: list[dict[Any, Any]] = []

        return super().model_post_init(context)

    def store_result(self, prompt: str, result: dict[Any, Any]) -> None:
        """
        Format and store a single prompt's generation result.

        Constructs a dictionary matching the required output schema
        (prompt, name, parameters) and appends it to the internal list.

        Args:
            prompt (str): The original natural language request.
            result (dict[Any, Any]): The raw generation results containing
                                     the function name and its parameters.
        """
        data: dict[Any, Any] = {}

        # Store the prompt
        data['prompt'] = prompt

        # Store the generated name and the parameters
        for key_name, llm_generation_result in result.items():
            match key_name:
                case 'name':
                    data['name'] = llm_generation_result
                case 'parameters':
                    data['parameters'] = llm_generation_result
                case _:
                    print_log(
                        "[yellow]"
                        "Warning, unknown parameters: "
                        f"'{llm_generation_result}'"
                        "[/yellow]"
                    )

        # Add to the list
        self._result_data.append(data)

    def write_output(self) -> None:
        """
        Export the accumulated results to the JSON output file.

        Dumps the internal list of dictionaries into a formatted JSON file
        at the path specified during initialization.

        Raises:
            ValueError: If the internal result data is empty or if an
                error occurs during the file writing process.
        """
        # Security if data is empty
        if not self._result_data:
            raise ValueError("Empty data from output. Cannot write.")

        # Write and convert to json format
        try:
            with open(self.output_file_path, 'w') as f:
                json.dump(self._result_data, f, indent=2)
                print_log(
                    "[green]"
                    f"✅ Successfully writted data in {self.output_file_path}"
                    "[/green]"
                )

        except Exception:
            raise ValueError(f"Error while opening {self.output_file_path}.")

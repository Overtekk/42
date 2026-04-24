# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Vocabulary.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/13 11:41:33 by roandrie        #+#    #+#               #
#  Updated: 2026/04/24 14:51:17 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Vocabulary management module.

This module is responsible for loading the LLM's vocabulary map and providing
utility functions for constrained decoding. It handles the translation between
string tokens and their corresponding integer IDs used by the model's tokenizer
"""

from typing import Any, Dict

import json

from pydantic import BaseModel, Field, PrivateAttr

from src.utils import print_log


class Vocabulary(BaseModel):
    """
    Manager for the LLM's tokenizer vocabulary.

    Attributes:
        path_file (str): The absolute or relative path to the JSON
            vocabulary file.
        debug (bool): Flag to enable detailed debug logging.
    """

    path_file: str = Field(
        description="Path to the vocabulary file"
    )
    debug: bool = Field(
        description="The state of the debug mode",
        default=False
    )

    _vocab_data: Dict[str, int] = PrivateAttr(
        default_factory=dict
    )
    _id_to_token: Dict[int, str] = PrivateAttr(
        default_factory=dict
    )

    def model_post_init(self, context: Any) -> None:
        """Initialize the private vocabulary state."""
        self._load_vocab(self.path_file)

        for key, value in self._vocab_data.items():
            self._id_to_token[value] = key

        return super().model_post_init(context)

    def get_id_to_token_vocab(self) -> Dict[int, str]:
        """
        Return the pre-computed reverse mapping of the vocabulary.

        Returns:
            Dict[int, str]: A dictionary mapping token integer IDs back
            to their string representations. Useful for decoding outputs.
        """
        return self._id_to_token

    def _load_vocab(self, path: str) -> None:
        """
        Load the vocabulary mapping from the specified JSON file.

        Args:
            path (str): The file path to load.

        Raises:
            ValueError: If the file cannot be found, opened, or parsed.
        """
        try:
            # Open the vocab file
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            if "model" in data and "vocab" in data["model"]:
                vocab = data["model"]["vocab"]
            else:
                vocab = data

            if self.debug:
                print_log(
                    "[green]"
                    "✅ Vocabulary loaded!"
                    "[/green]"
                )

            # Save the loaded vocab json file
            self._vocab_data = vocab

        except Exception as e:
            raise ValueError(f"error while loading vocab path {e}")

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  llm_path_checker.py                               :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/13 08:50:14 by roandrie        #+#    #+#               #
#  Updated: 2026/04/22 11:09:16 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
LLM SDK and Model path validation module.

This module is responsible for verifying that the required LLM SDK
directory structure and essential model files are present and
accessible on the filesystem. It ensures the environment is correctly
set up before the core logic attempts to initialize the model.
"""

from pathlib import Path

import pathlib
import os

from src.utils import is_folder_exist, is_file_exist


# Path to the models and the llm
qwen_model_path: dict[str, str] = {
    "init": "llm_sdk/llm_sdk/__init__.py",
    "pyproject": "llm_sdk/pyproject.toml"
}
llm_folder_path: dict[str, str] = {
    "folder": "llm_sdk",
    "sub_folder": "llm_sdk/llm_sdk"
}


def check_llm_available() -> None:
    """
    Verify the availability and readability of the LLM SDK and its models.

    This function performs a series of filesystem checks on predefined paths
    to ensure that the 'llm_sdk' directory and its internal structure exist
    and that the application has read permissions for these locations.

    Raises:
        ValueError: If a required directory or file is missing, or if
            filesystem permissions prevent reading the contents.
    """
    # Check LLM
    for folder_path in llm_folder_path.values():
        path: Path = pathlib.Path(folder_path)

        if not is_folder_exist(path):
            raise ValueError(f"Missing '{path}' folder.")

        if not os.access(path, os.R_OK):
            raise ValueError(f"Path  '{path}' can't be read.")

    # Check Model
    for file_path in qwen_model_path.values():
        model_path: Path = pathlib.Path(file_path)

        if not is_file_exist(model_path):
            raise ValueError(f"Missing '{model_path}' from llm_sdk.")

        if not os.access(model_path, os.R_OK):
            raise ValueError(f"Can't read '{model_path}' from llm_sdk.")

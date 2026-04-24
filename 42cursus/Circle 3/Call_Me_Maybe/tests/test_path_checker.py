# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  test_path_checker.py                              :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/24 15:35:57 by roandrie        #+#    #+#               #
#  Updated: 2026/04/24 16:02:59 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import unittest
import argparse
from pathlib import Path

from src.parser.path_checker import validate_json_input


class TestPathChecker(unittest.TestCase):
    """Test suite for path validation logic."""

    def test_validate_json_input_valid_extension(self) -> None:
        """Test with a valid JSON file."""
        # Setup: Ensure this file actually exists on your disk!
        test_file = "tests/files/valid_json.json"

        # Execution
        result = validate_json_input(test_file)

        # Assertion: Verify the function returns a Path object as expected
        self.assertIsInstance(result, Path)
        self.assertEqual(str(result), test_file)

    def test_validate_json_input_invalid_extension(self) -> None:
        """Test that a .txt file raises an ArgumentTypeError."""
        # Setup: Ensure this .txt file actually exists on your disk!
        test_file = "tests/files/invalid_json.txt"

        # Assertion: The 'with' context manager traps the expected error
        with self.assertRaises(argparse.ArgumentTypeError):
            validate_json_input(test_file)

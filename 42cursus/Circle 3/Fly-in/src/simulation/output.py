# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  output.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/21 14:35:34 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 11:56:26 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Simulation logging output module.

This module provides the LogOutput class, responsible for generating and
formatting the final text file that chronicles the step-by-step movements
of all drones throughout the simulation.
"""

import os

from typing import Dict, List
from pathlib import Path

from src.utils.ui import Display


class LogOutput():
    """
    Handles the creation and writing of simulation movement logs.

    This class ensures the target output directory exists and writes the
    recorded drone movements turn by turn into a uniquely named text file
    based on the loaded map.

    Attributes:
        logs (Dict[int, List[str]]): A dictionary mapping turn numbers to a
                                     list of movement strings for that turn.
        root (Path): The Path object representing the 'output' directory.
        map_name (str): The name of the map file, used to name the log file.
    """

    def __init__(self, map_name: str, logs: Dict[int, List[str]]) -> None:
        """
        Initializes the log output manager and prepares the directory.

        Args:
            map_name (str): The base name of the map, used for the output file.
            logs (Dict[int, List[str]]): The recorded simulation movements.
        """
        self.logs = logs
        self.root = Path("output")
        self.map_name = map_name

        self._create_folder()

    def write_log(self) -> None:
        """
        Writes the formatted simulation logs to the disk.

        Iterates through the stored logs dictionary, concatenates the movements
        for each turn into a single line, and writes them to a text file inside
        the output directory. Catches and reports permission issues.
        """
        try:
            with open(f"{self.root}/{self.map_name}", "w") as f:
                for log_list in self.logs.values():
                    log_line = ""

                    for log in log_list:
                        log_line += f"{log} "
                        f.write(f"{log_line}")

                    f.write("\n")

        except PermissionError:
            Display.error("Can't write logs. Permissions denied to write in "
                          "the 'output' folder")

    def _create_folder(self) -> None:
        """
        Ensures the existence of the root output directory.

        Checks if the designated output folder exists; if not, it creates it
        safely within the project structure.
        """
        if not self.root.exists() or not self.root.is_dir():
            os.makedirs("output")

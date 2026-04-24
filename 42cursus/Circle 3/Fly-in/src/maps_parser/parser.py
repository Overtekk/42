# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  parser.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/02/24 17:33:05 by roandrie        #+#    #+#               #
#  Updated: 2026/03/24 13:43:26 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

"""
Map parsing and validation module.

This module scans the "maps" folder, processes map configuration files, and
categorizes them. Valid maps are parsed into Pydantic models and stored for
the simulation, while invalid maps are isolated with their specific parsing
errors preserved for user correction.
"""

import re

from pathlib import Path
from typing import Any, Dict, List, Set
from typing_extensions import Self

from pydantic import BaseModel, Field, ValidationError, model_validator

from src.utils.ui import Colors
from src.utils.errors import MapError


class Maps():
    """
    Manager class responsible for locating, validating, and storing maps.
    """

    def __init__(self) -> None:
        """
        Initializes the map manager.

        Sets up the root directory path, file extension filters, and internal
        dictionaries for categorizing valid and invalid maps. Automatically
        triggers the map processing routine upon instantiation.
        """
        self.root = Path("maps")
        self.extension = "*.txt"
        self.maps_dict: dict[str, list[str]] = {}
        self.invalid_maps_dict: dict[str, list[tuple[str, str]]] = {}
        self.connection_map: Dict[str, MapModel] = {}

        self._add_maps_to_list()

    def _process_map(self, file_path: Path, category: str) -> None:
        """
        Internal helper to validate a map and assign it to the correct
        category.

        Args:
            file_path (Path): The absolute or relative path to the map file.
            category (str): The folder name acting as the map's category.
        """
        # Create list for the dictionnary if not exist
        if category not in self.maps_dict:
            self.maps_dict[category] = []
        if category not in self.invalid_maps_dict:
            self.invalid_maps_dict[category] = []

        # If the map is valid, we add it to "maps_dict"
        try:
            parsed = MapModel.is_map_valid(file_path)
            self.maps_dict[category].append(file_path.stem)
            self.connection_map[file_path.stem] = parsed
        # If map is invalid, we add it to the "invalid_maps_dict" with
        # all errors listed
        except MapError as e:
            self.invalid_maps_dict[category].append((file_path.stem, str(e)))

        except Exception as e:
            raise MapError(f"Error processing {file_path}: {e}")

    def _cleanup_dictionaries(self) -> None:
        """
        Removes empty categories from the dictionaries.

        Iterates through both valid and invalid map dictionaries to delete
        any category keys that do not contain any parsed maps, ensuring a
        clean state for the user interface menu.
        """
        all_categories = (set(list(self.maps_dict.keys()) +
                              list(self.invalid_maps_dict.keys())))

        for category in all_categories:
            # Valid maps
            if category in self.maps_dict and not self.maps_dict[category]:
                del self.maps_dict[category]

            # Invalid maps
            if (category in self.invalid_maps_dict
                    and not self.invalid_maps_dict[category]):
                del self.invalid_maps_dict[category]

    def _add_maps_to_list(self) -> None:
        """
        Scans the maps directory and processes all discovered text files.

        Iterates through subdirectories to categorize maps, and processes
        root-level text files under an "other" category. Sorts the results
        alphabetically and cleans up empty categories.

        Raises:
            MapError: If the "maps" directory does not exist or is not a
                      directory.
            MapError: If there are permission issues reading the directory.
            MapError: If an unexpected critical error occurs during traversal.
        """
        if not self.root.exists() or not self.root.is_dir():
            raise MapError(f"The maps directory '{self.root}' was not found. "
                           "Create it first and place your maps inside.")

        try:
            for item in self.root.iterdir():

                # Directory
                if item.is_dir():
                    for map_file in item.glob(self.extension):
                        self._process_map(map_file, item.name)

                    if item.name in self.maps_dict:
                        self.maps_dict[item.name].sort()

                # Map file
                elif item.match(self.extension):
                    self._process_map(item, "other")

            if "other" in self.maps_dict:
                self.maps_dict["other"].sort()

            # Clean empty folders
            self._cleanup_dictionaries()

            if self.invalid_maps_dict:
                for category in self.invalid_maps_dict:
                    self.invalid_maps_dict[category].sort()

        except PermissionError:
            raise MapError("Permission denied: Cannot read directory "
                           f"'{self.root}'. Check your permission.")
        except Exception as e:
            raise MapError(f"Unexpected error of type {e}")

    def get_maps_list(self) -> None:
        """
        Prints the current state of valid and invalid maps.
        """
        print(f"{Colors.GREEN}Valid maps:{Colors.END}")
        for category, maps in self.maps_dict.items():
            print(f"{category}: {maps}")

        print(f"{Colors.RED}Invalid maps:{Colors.END}")
        for category, invalid_maps in self.invalid_maps_dict.items():
            print(f"{category}: {invalid_maps}")


class MapModel(BaseModel):
    """
    Data validation model representing a fully parsed simulation map.

    Attributes:
        nb_drones (int): The total number of drones to spawn (must be >= 1).
        start_hub (str): The raw string definition of the starting zone.
        end_hub (str): The raw string definition of the destination zone.
        hub (List[str]): A list of raw string definitions for intermediate
                         zones.
        connection (List[str]): A list of raw string definitions for paths.
        connection_map (Dict[str, List[str]]): A parsed adjacency list mapping
                                               zones to their neighbors.
    """
    nb_drones: int = Field(ge=1)
    start_hub: str
    end_hub: str
    hub: List[str] = Field(default_factory=list)
    connection: List[str] = Field(default_factory=list)
    connection_map: Dict[str, List[str]] = Field(default_factory=dict)

    @classmethod
    def is_map_valid(cls, file: Path) -> "MapModel":
        """
        Parses a map text file and validates its content line by line.

        Extracts keys and values, checks formatting syntax, ensures unique
        zones, and validates raw metadata strings before instantiating the
        Pydantic model.

        Args:
            file (Path): The file path to the map configuration text file.

        Raises:
            MapError: If the file extension is not '.txt'.
            MapError: If the file is not found or lacks read permissions.
            MapError: If parsing fails due to invalid syntax, duplicates, or
                      missing required parameters.

        Returns:
            MapModel: A validated instance of the map configuration.
        """
        if file.suffix != ".txt":
            raise MapError(f"Invalid file extension '{file.suffix}'. Map must "
                           "be a '.txt' file.")

        valid_map_key: Set[str] = {
            "nb_drones", "start_hub", "end_hub", "hub", "connection"
        }
        list_key: Set[str] = {
            "hub", "connection"
        }
        valid_zones = []
        existing_connection: List[str] = []

        raw_config: Dict[str, Any] = {}

        errors_list: List[str] = []
        key_line_map: Dict[str, int] = {}

        is_first_param = True

        try:
            with open(file, "r") as f:
                for i, line in enumerate(f, 1):
                    line = line.split("#", 1)[0].strip()

                    # Ignore empty line and comment
                    if line.startswith("#") or not line:
                        continue

                    # Check if separator exist
                    if ":" not in line:
                        errors_list.append(f"Line {i}: Invalid format "
                                           "(missing ':').")
                        continue

                    # Split key and value
                    key, value = line.split(":", 1)
                    key = key.strip()

                    # Check if key is valid
                    if key not in valid_map_key:
                        errors_list.append(f"Line {i}: key '{key}' doesn't "
                                           "exist.")
                        continue

                    # Check if first key is "nb_drones"
                    if is_first_param:
                        if key != "nb_drones":
                            errors_list.append(f"Line {i}: First parameter"
                                               f" must be 'nb_drones'. "
                                               f"Found '{key}'.")
                        is_first_param = False
                    elif key == "nb_drones":
                        errors_list.append(f"Line {i}: 'nb_drones' must be at "
                                           "the first line.")

                    # Check zones data
                    if key in ["start_hub", "hub", "end_hub"]:
                        zone_data = re.findall(r"\[[^\]]*\]|\S+", value)
                        if len(zone_data) in [3, 4]:
                            if cls._check_valid_zones(zone_data[0]) is False:
                                errors_list.append(f"Line {i}: error in zone "
                                                   f"name ('{zone_data[0]}'). "
                                                   "Check that is a valid "
                                                   "string, with no space and "
                                                   "'-'.")
                            else:
                                if zone_data[0] in valid_zones:
                                    errors_list.append(f"Line {i}: Duplicated"
                                                       " zone name: "
                                                       f"{zone_data[0]}")
                                valid_zones.append(zone_data[0])

                            if cls._check_zone_coords(zone_data[1]) is False:
                                errors_list.append(f"Line {i}: error in zone "
                                                   "coordinates ('"
                                                   f"{zone_data[1]}). Check "
                                                   "that is a valid int.")

                            if cls._check_zone_coords(zone_data[2]) is False:
                                errors_list.append(f"Line {i}: error in zone "
                                                   "coordinates ('"
                                                   f"{zone_data[2]}). Check "
                                                   "that is a valid int.")

                            if len(zone_data) == 4:
                                tmp_error = cls._check_metadata(zone_data[3],
                                                                "zone")
                                if tmp_error:
                                    for e in tmp_error:
                                        errors_list.append(f"Line {i}: {e}")
                        else:
                            if len(zone_data) < 3:
                                errors_list.append(f"Line {i}: Missing datas "
                                                   "for zone. Valid syntax: "
                                                   "<name>(str) <x>(int) <y>"
                                                   "(int) <metadata> (metadata"
                                                   " is optional).")
                            else:
                                errors_list.append(f"Line {i}: Too much datas "
                                                   "for zone. Valid syntax: "
                                                   "<name>(str) <x>(int) <y>"
                                                   "(int) <metadata> (metadata"
                                                   " is optional).")
                    # Check connections data
                    elif key == "connection":
                        zone_data = re.findall(r"\[[^\]]*\]|\S+", value)
                        if len(zone_data) in [1, 2]:
                            tmp_error = cls._check_connection(
                                zone_data[0], existing_connection, valid_zones)
                            if tmp_error:
                                for e in tmp_error:
                                    errors_list.append(f"Line {i}: {e}")
                                continue
                            else:
                                existing_connection.append(zone_data[0])
                                zone1, zone2 = zone_data[0].split("-", 1)
                                inversed = f"{zone2}-{zone1}"
                                existing_connection.append(inversed)

                            if len(zone_data) == 2:
                                tmp_error = cls._check_metadata(zone_data[1],
                                                                "connection")
                                if tmp_error:
                                    for e in tmp_error:
                                        errors_list.append(f"Line {i}: {e}")
                                    continue
                        else:
                            if len(zone_data) < 1:
                                errors_list.append(f"Line {i}: Missing data "
                                                   "for connection. Valid "
                                                   "syntax: <zone1>-<zone2> "
                                                   "<metadata> (metadata is "
                                                   "optional).")
                            else:
                                errors_list.append(f"Line {i}: Too much data "
                                                   "for connection. Valid "
                                                   "syntax: <zone1>-<zone2> "
                                                   "<metadata> (metadata is "
                                                   "optional).")

                    # Constructing data
                    if key in list_key:
                        if key not in raw_config:
                            raw_config[key] = []
                        raw_config[key].append(value)
                        if key not in key_line_map:
                            key_line_map[key] = i
                    else:
                        if key in raw_config:
                            errors_list.append(f"Line {i}: Duplicate key: "
                                               f"'{key}' must be unique.")
                        raw_config[key] = value
                        key_line_map[key] = i

        except FileNotFoundError:
            raise MapError(f"File not found: {file}")

        except PermissionError:
            raise MapError(f"Can't read file, check permissions: {file}")

        except Exception as e:
            raise MapError(f"Critical error reading file {file.name}: {e}")

        try:
            map = cls(**raw_config)
        except ValidationError as e:
            for error in e.errors():
                if not error['loc']:
                    errors_list.append(error['msg'])
                    continue

                field_name = str(error['loc'][0])
                msg = error['msg']

                if error['type'] == "greater_than_equal":
                    msg = (f"Value too small. Must be at least "
                           f"{error['ctx']['ge']}")
                elif error['type'] == "int_parsing":
                    msg = "Value must be an integer"

                line_num = key_line_map.get(field_name, "Unknown")

                if error['type'] == 'missing':
                    errors_list.append(f"Missing required key "
                                       f"'{field_name}'.")
                else:
                    errors_list.append(f"Line {line_num}: Key '{field_name}': "
                                       f"{msg}")

        if errors_list:
            errors_list.sort(key=lambda x: int(x.split()[1].strip(":"))
                             if x.startswith("Line ") else float("inf"))
            raise MapError("\n".join(errors_list))

        return map

    @model_validator(mode='after')
    def _validate_coords(self) -> Self:
        """
        Validates the logical placement of zones on the grid.

        Ensures that the start and end hubs do not share the same coordinates,
        and that no intermediate hub overlaps with the entry or exit points.

        Raises:
            MapError: If start and end coordinates are identical.
            MapError: If any hub shares coordinates with the start or end
                      zones.

        Returns:
            MapModel: The validated MapModel instance.
        """
        seen_coords: set[tuple[int, int]] = set()

        all_zones = self.hub
        start = self.start_hub.split()
        end = self.end_hub.split()

        try:
            start_x = int(start[1])
            start_y = int(start[2])
            end_x = int(end[1])
            end_y = int(end[2])
            start_coords = (start_x, start_y)
            end_coords = (end_x, end_y)
        except ValueError:
            return self

        if start_coords == end_coords:
            raise MapError("Coordinates of start and end must be unique.")

        for zone in all_zones:
            parts = zone.split()

            if len(parts) < 3:
                continue

            try:
                x = int(parts[1])
                y = int(parts[2])
                curr_coords = (x, y)
            except ValueError:
                continue

            if curr_coords == start_coords or curr_coords == end_coords:
                raise MapError(f"Duplicate coordinates: {curr_coords} "
                               "(can't be the same than entry/exit) - "
                               f"for zone '{parts[0]}'")
            seen_coords.add(curr_coords)

        return self

    @model_validator(mode='after')
    def _validate_connection(self) -> Self:
        """
        Validates the overall pathfinding integrity of the mapped connections.

        Populates the connection_map dictionary, checks if start and end zones
        are linked to the network, verifies they are not defined as blocked,
        and runs a BFS traversal to ensure a viable path exists from
        start to end.

        Raises:
            MapError: If no start or end connection is found.
            MapError: If the start or end hub is explicitly blocked.
            MapError: If no continuous path exists between start and end.

        Returns:
            MapModel: The validated MapModel instance.
        """
        all_connections = self.connection

        if len(all_connections) == 0:
            return self

        save_start = None
        end_save = None

        start_split = self.start_hub.strip().split()
        end_split = self.end_hub.strip().split()

        start_name = start_split[0]
        end_name = end_split[0]

        for raw_connection in all_connections:
            connect = re.findall(r"\[[^\]]*\]|\S+", raw_connection)
            zone1, zone2 = connect[0].split("-")
            if save_start is None:
                if zone1 == start_name or zone2 == start_name:
                    save_start = connect[0]
            if end_save is None:
                if zone1 == end_name or zone2 == end_name:
                    end_save = connect[0]
            self.connection_map.setdefault(zone1, []).append(zone2)
            self.connection_map.setdefault(zone2, []).append(zone1)

        if save_start is None:
            raise MapError("No start found. Have you forgot to add it?")
        if end_save is None:
            raise MapError("No end found. Have you forgot to add it?")

        blocked_zones: Set[str] = set()
        all_zone_definitions = self.hub + [self.start_hub, self.end_hub]
        for zone_def in all_zone_definitions:
            if "zone=blocked" in zone_def:
                blocked_name = zone_def.split()[0]
                blocked_zones.add(blocked_name)

        if start_name in blocked_zones:
            raise MapError(f"Start hub '{start_name}' is blocked. "
                           "Path impossible.")
        if end_name in blocked_zones:
            raise MapError(f"End hub '{end_name}' is blocked. "
                           "Path impossible.")

        to_visit = [start_name]
        visited: Set[str] = set()

        while to_visit:
            current_hub = to_visit.pop(0)

            if current_hub == end_name:
                return self

            visited.add(current_hub)
            for neighbor in self.connection_map[current_hub]:
                if (neighbor not in to_visit and neighbor not in visited and
                        neighbor not in blocked_zones):
                    to_visit.append(neighbor)

        raise MapError("No connections between start and end.")

    @staticmethod
    def _check_valid_zones(valid_zones: str) -> bool:
        """
        Validates the string formatting of a zone name.

        Args:
            valid_zones (str): The raw string identifier for the zone.

        Returns:
            bool: True if the string is well-formed (no spaces or dashes),
                  False otherwise.
        """
        if (" " in valid_zones or "-" in valid_zones or
                not isinstance(valid_zones, str)):
            return False
        return True

    @staticmethod
    def _check_zone_coords(coord: str) -> bool:
        """
        Validates that a coordinate string can be converted to an integer.

        Args:
            coord (str): The coordinate string to evaluate.

        Returns:
            bool: True if it can be safely cast to int, False otherwise.
        """
        try:
            int(coord)
            return True
        except ValueError:
            return False

    @staticmethod
    def _check_metadata(metada: str, type: str) -> List[str]:
        """
        Checks if metadata string is correctly formatted and contains valid
        values.

        Parses a raw metadata string (e.g., '[color=red max_drones=5]') and
        validates the keys and values based on the component type ('zone' or
        'connection').

        Args:
            metada (str): The raw metadata string to parse.
            type (str): The context of the metadata ('zone' or 'connection').

        Returns:
            List[str]: A list containing all error messages found during
                       parsing. Returns an empty list if the metadata is
                       fully valid.
        """
        error_list = []
        valid_zone_metadata = {"zone", "color", "max_drones"}
        valid_zone_type = {"normal", "blocked", "restricted", "priority"}
        duplicate_data: List[str] = []

        if not metada.startswith("["):
            error_list.append("Missing '[' at the start.")
        if not metada.endswith("]"):
            error_list.append("Missing ']' at the end.")

        metada = metada.strip("[]")
        metada_list = re.findall(r"\S+", metada)

        for m in metada_list:
            if "=" not in m:
                error_list.append(f"Missing '=' separator in {m}")
                continue

            key, value = m.split("=", 1)

            if type == "zone":
                if key not in valid_zone_metadata:
                    error_list.append(f"{key} is not a valid tag.")
                    continue
            elif type == "connection":
                if key != "max_link_capacity":
                    error_list.append(f"{key} is not a valid tag.")
                    continue

            if key == "zone":
                if value not in valid_zone_type:
                    error_list.append(f"'{key}={value}' is not a valid zone "
                                      "type. Use: 'normal', 'blocked', "
                                      "'restricted', 'priority'.")

            elif key in ["max_drones", "max_link_capacity"]:
                try:
                    n = int(value)
                    if n <= 0:
                        raise ValueError
                except ValueError:
                    error_list.append(f"'{key}={value}' need to be a positive "
                                      "valid int.")

            elif key == "color":
                if not isinstance(value, str):
                    error_list.append(f"'{key}={value}' is not a valid color.")

            if len(duplicate_data) > 0:
                if key in duplicate_data:
                    error_list.append(f"'duplicated key: {key}")
            duplicate_data.append(key)

        return error_list

    @staticmethod
    def _check_connection(connection_name: str, existing_connection: List[str],
                          valid_zones: List[str]) -> List[str]:
        """
        Validates the syntax and referential integrity of a connection string.

        Checks if the connection string correctly links two existing zones
        using a dash separator, and ensures no duplicate links are formed.

        Args:
            connection_name (str): The raw connection string
                                   (e.g., 'hub1-hub2').
            existing_connection (List[str]): A list of already established
                                             connection names.
            valid_zones (List[str]): A list of previously validated zone names.

        Returns:
            List[str]: A list containing all error messages found during
                       parsing. Returns an empty list if the connection string
                       is fully valid.
        """
        error_list = []

        if "-" not in connection_name:
            error_list.append("Missing '-' between zones name.")
            return error_list

        zone1, zone2 = connection_name.split("-", 1)

        if len(valid_zones) == 0:
            error_list.append("Define zones first.")
            return error_list

        if zone1 not in valid_zones:
            error_list.append(f"{zone1} not a valid zone name.")
        if zone2 not in valid_zones:
            error_list.append(f"{zone2} not a valid zone name.")

        if error_list:
            return error_list

        if connection_name in existing_connection:
            error_list.append(f"Duplicated connection: {connection_name}")

        return error_list

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  utils.py                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/01 11:18:23 by roandrie        #+#    #+#               #
#  Updated: 2026/07/20 10:09:54 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import zipfile
import os
from src.utils import print_log, print_rule, check_file_extension
from src.config import PathConfig


IGNORED_PATH = ["__pycache__", ".git"]

EXTENSIONS_TO_CHECK = [".py", ".md", ".txt"]


def extract_archive(zip_path: str) -> None:
    """Extract an archive.

    Extract the given zip file using the zip name.

    Args:
        zip_path (str): Path of the zip file.

    Raises:
        ValueError: If an error occurred during the extracting or if not a zip
                    file.
        ValueError: Error with permissions.
    """
    print_rule()
    print_log("📁 Extracting ...")

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            zf.extractall(path=PathConfig.DEFAULT_VLLM_DIRECTORY)
            print_log("✅ Zip extracted.", color="green")

    except zipfile.BadZipFile:
        raise ValueError("Error when extracting ZIP file.")

    except PermissionError as e:
        raise ValueError(e)


def load_files(vLLM_path: str) -> list[tuple[str, str]]:
    """Files loader.

    Scan all files. If a files have the correct extension, construct it path
    from the root, open it and add the content to the list. In case of error,
    print it to the console without closing the programm.

    Args:
        vLLM_path (str): path of the vLLM folder.

    Returns:
        list[tuple[str, str]]: list of tuples containing the absolute path and
                               the content of the file.
    """
    files_list: list[tuple[str, str]] = []

    # Scan all files from the root, recursive for each folders.
    for root, dirs, filesname in os.walk(
        vLLM_path, topdown=True, onerror=None, followlinks=False
    ):
        # IGNORED FILES OR FOLDERS
        dirs[:] = [d for d in dirs if d not in IGNORED_PATH]

        for file in filesname:
            # CHECK EXTENSION
            for extension in EXTENSIONS_TO_CHECK:
                if not check_file_extension(file, extension):
                    continue

                # Construct the filepath
                filepath: str = os.path.join(root, file)

                # Open the file
                try:
                    with open(filepath, encoding="utf-8") as f:
                        # Add the filepath and file content
                        files_list.append((filepath, f.read()))

                except PermissionError:
                    print_log(f"Permission error for file: {file}.", "red")
                except Exception as e:
                    print_log(
                        f"Error while trying to open file: {file} with error "
                        f"{e}",
                        "red",
                    )

    return files_list

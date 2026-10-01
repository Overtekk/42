# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  ChunkerEngine.py                                  :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/03 14:37:38 by roandrie        #+#    #+#               #
#  Updated: 2026/09/10 10:22:49 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from src.model import MinimalSource
from src.utils import check_file_extension, print_log

CHUNK_OVERLAP: int = 100


class ChunkerEngine:
    """Split source files into fixed-size chunks while preserving context
       boundaries.
    """

    def __init__(self, chunk_size: int) -> None:
        """Initialize the chunking engine.

        Args:
            chunk_size: Maximum size in characters for each chunk.
        """
        self._chunk_size: int = chunk_size

    def process(
        self, file_path: str, content: str
    ) -> list[tuple[MinimalSource, str]] | None:
        """Process a file and return the list of chunk metadata/content pairs.

        Args:
            file_path: Source file being chunked.
            content: Full text content of the file.

        Returns:
            list[tuple[MinimalSource, str]] | None: Chunks if the file type is
            supported, otherwise None.
        """
        for extension in [".txt", ".md"]:
            if check_file_extension(file_path, extension):
                return self._chunk_txt_file(file_path, content)

        if check_file_extension(file_path, ".py"):
            return self._chunk_py_file(file_path, content)

        else:
            print_log(f"Unkown file extension for {file_path}.", "red")
        return None

    # :-----------------:
    #   PRIVATE METHODS
    # :-----------------:

    def _chunk_py_file(
        self, file_path: str, content: str
    ) -> list[tuple[MinimalSource, str]]:
        """Split Python source files using a language-aware text splitter.

        Args:
            file_path: Python file path.
            content: File contents.

        Returns:
            list[tuple[MinimalSource, str]]: Generated chunks and their
            metadata.
        """
        CHUNK_OVERLAP: int = 100

        python_splitter = RecursiveCharacterTextSplitter.from_language(
            language=Language.PYTHON,
            chunk_size=self._chunk_size,
            chunk_overlap=CHUNK_OVERLAP,
        )

        return self._split_text(python_splitter, file_path, content)

    def _chunk_txt_file(
        self, file_path: str, content: str
    ) -> list[tuple[MinimalSource, str]]:
        """Split plain text files using a recursive character splitter.

        Args:
            file_path: Text file path.
            content: File contents.

        Returns:
            list[tuple[MinimalSource, str]]: Generated chunks and their
            metadata.
        """
        # Split the text based on the chunk size. Keep all seperators
        if check_file_extension(file_path, ".md"):
            splitter = RecursiveCharacterTextSplitter.from_language(
                language=Language.MARKDOWN,
                chunk_size=self._chunk_size,
                chunk_overlap=CHUNK_OVERLAP,
            )
        else:
            splitter = RecursiveCharacterTextSplitter(
                chunk_size=self._chunk_size,
                chunk_overlap=CHUNK_OVERLAP,
                keep_separator=True,
            )

        return self._split_text(splitter, file_path, content)

    def _split_text(
        self,
        text_splitter: RecursiveCharacterTextSplitter,
        file_path: str,
        content: str,
    ) -> list[tuple[MinimalSource, str]]:
        """Split text into chunks and attach source position metadata.

        Args:
            text_splitter: Text splitter instance to use.
            file_path: Original file path.
            content: Full document content.

        Returns:
            list[tuple[MinimalSource, str]]: Chunks with character offsets.
        """
        # Create the index and the list
        index: int = 0
        chunked_txt: list[tuple[MinimalSource, str]] = []

        # Split the text into small chunks
        for sub_txt in text_splitter.split_text(content):
            if not sub_txt:
                continue

            # Find the first index of the chunk
            sub_first_index = content.find(sub_txt, index)

            # If failed. Retry from the beginning
            if sub_first_index == -1:
                sub_first_index = content.find(sub_txt)
            # Skip if didn´t find it
            if sub_first_index == -1:
                continue

            # Find the last index of the chunk
            sub_last_index = sub_first_index + len(sub_txt)
            # Update the index
            index = sub_first_index + 1

            # If valids
            if sub_last_index > sub_first_index >= 0:
                # Add the chunk to the list as MinimalSource
                chunked_txt.append(
                    (
                        MinimalSource(
                            file_path=file_path,
                            first_character_index=sub_first_index,
                            last_character_index=sub_last_index,
                        ),
                        sub_txt,
                    )
                )

        return chunked_txt

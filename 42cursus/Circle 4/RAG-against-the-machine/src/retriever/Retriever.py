# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Retriever.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/17 12:07:28 by roandrie        #+#    #+#               #
#  Updated: 2026/09/09 11:53:57 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import os
import bm25s
import json
import Stemmer
from pathlib import Path
from json import JSONDecodeError
from pydantic import ValidationError
from src import RAGError
from src.model import (
    ChunkSearchResult,
    UnansweredQuestion,
    AnsweredQuestion,
    RagDataset,
    MinimalSearchResults,
    StudentSearchResults,
)
from src.utils import print_log, print_rule, is_folder_exist, is_file_exist


class RetrieverEngine:
    """Load the BM25 index and retrieve relevant chunks for a search query."""

    def __init__(self, k: int, directories_list: dict[str, str]) -> None:
        """Initialize the retriever with the BM25 index and chunk database.

        Args:
            k: Number of chunks to retrieve per query.
            directories_list: Storage paths for BM25 and chunk datasets.
        """
        self._k = k
        self._directories_list = directories_list
        self._load_database()

        # Create a stemmer (get the root of multiples same words)
        self.stemmer = Stemmer.Stemmer("english")

    def retrieve(self, query: str) -> list[ChunkSearchResult]:
        """Retrieve the top-k chunk matches for a user query.

        Args:
            query: Query text to search.

        Returns:
            list[ChunkSearchResult]: Ranked retrieved chunks.

        Raises:
            RAGError: If the BM25 index or chunk database is invalid.
        """
        # Tokenize the query
        query_token = bm25s.tokenize(
            query,
            show_progress=True,
            leave=False,
            stopwords="en",
            stemmer=self.stemmer,
        )

        # Retrieve the best match documents from the corpus
        indices, scores = self._retriever.retrieve(
            query_token,
            k=self._k,
            show_progress=True,
            leave_progress=False,
        )

        # Transform the ndarray into a single list
        top_k_indices = indices[0]
        top_k_scores = scores[0]

        # Add the content and score to the result of the retriever
        retrieve_chunks: list[ChunkSearchResult] = []
        for index, score in zip(top_k_indices, top_k_scores):
            try:
                # Find the correspond chunk in the database, copy its data
                data_dict = self._chunks[index]
                # Add the score
                data_dict["score"] = float(score)
                # Create the model and add it to the global list
                chunk_result = ChunkSearchResult.model_validate(data_dict)
                retrieve_chunks.append(chunk_result)
            except IndexError:
                raise RAGError(
                    "Error while trying to find the index in the retriever. "
                    "Re-run the index command."
                )
            except ValidationError:
                raise RAGError(
                    "Error while trying to create the retriever model."
                )

        return retrieve_chunks

    def retrieve_dataset(
        self, dataset: list[AnsweredQuestion | UnansweredQuestion]
    ) -> list[MinimalSearchResults]:
        """Retrieve relevant chunks for each question in a dataset.

        Args:
            dataset: List of questions to process.

        Returns:
            list[MinimalSearchResults]: Retrieval results for each question.
        """
        minimal_search_results: list[MinimalSearchResults] = []
        # Create the Pydantic object and add it to the list
        for data in dataset:
            search_result = MinimalSearchResults(
                question_id=data.question_id,
                question=data.question,
                retrieved_sources=self.retrieve(data.question),
            )
            minimal_search_results.append(search_result)

        return minimal_search_results

    def save_retriever_result(
        self,
        minimal_search_results: list[MinimalSearchResults],
        save_dir: str,
        file_name: str,
    ) -> None:
        """Save search results for a dataset to JSON.

        Args:
            minimal_search_results: Retrieval results to save.
            save_dir: Output directory.
            file_name: Output file name.
        """
        # Create the Pydantic object
        results = StudentSearchResults(
            search_results=minimal_search_results, k=self._k
        )

        # Create the save file path
        save_file_path = os.path.join(save_dir, file_name)
        # Write the result to it
        with open(save_file_path, "w", encoding="utf-8") as f:
            f.write(results.model_dump_json(indent=4))

        print_log(f"Saved student_search_results to '{save_file_path}'")

    def create_dataset(
        self, file_path: Path
    ) -> list[AnsweredQuestion | UnansweredQuestion] | None:
        """Load a JSON dataset file into a validated question list.

        Args:
            file_path: Dataset file path.

        Returns:
            list[AnsweredQuestion | UnansweredQuestion] | None: Parsed
            questions, or None if the file could not be parsed.
        """
        rag_dataset: list[AnsweredQuestion | UnansweredQuestion] = []

        # Check the model between Answered and Unanswered
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                # Valid if the model of the file
                data = json.load(f)
                data_dataset = RagDataset.model_validate(data)
                # Add the dataset to the global list of questions
                rag_dataset.extend(data_dataset.rag_questions)

            except JSONDecodeError:
                print_log(
                    f"⚠️  Error while trying to open '{file_path}'. "
                    "Skipping\n",
                    "gold1",
                )
                return None
            except ValidationError:
                print_log(
                    f"⚠️  '{file_path}' does not seem to be an valid model. "
                    "Skipping\n",
                    "gold1",
                )
                return None

        return rag_dataset

    # :-----------------:
    #   PRIVATE METHODS
    # :-----------------:

    def _load_database(self) -> None:
        """Load the BM25 index and chunk database from disk."""
        # - SECURITY -
        chunk_db_file = os.path.join(
            self._directories_list["chunk_dir"], "chunks_db.json"
        )
        self._security_checker(chunk_db_file)

        # - Load the index folder with bm25 -
        print_rule("BM25 Database")
        print_log("Loading the BM25 database...")
        try:
            self._retriever = bm25s.BM25.load(
                self._directories_list["bm25_dir"], load_corpus=False
            )
        except FileNotFoundError as e:
            raise RAGError(f"{e}\nRe-run the index command.")
        print_log("✅ Done", "green")

        # - Load the chunks database -
        print_rule("Chunk Database")
        print_log("Loading the chunks database...")
        with open(chunk_db_file, "r") as f:
            try:
                self._chunks = json.load(f)
            except JSONDecodeError:
                raise RAGError("Error while trying to open 'chunk_db.json'")

        print_log("✅ Done", "green")
        print_rule()

    def _security_checker(self, chunk_db_file: str) -> None:
        """Validate the presence and integrity of the index and chunk database.

        Args:
            chunk_db_file: Path to the chunk database JSON file.

        Raises:
            RAGError: If the required database files are missing or empty.
        """
        # - BM25 Directory -
        # Check that the BM25 directory exist.
        if not is_folder_exist(self._directories_list["bm25_dir"]):
            raise RAGError(
                "BM25 indexing directory doesn't exist. Cannot launch the "
                "retriever.\nRun the index command first."
            )
        # Check that is not empty
        if len(os.listdir(self._directories_list["bm25_dir"])) == 0:
            raise RAGError("Cannot retrieve. The BM25 folder is empty.")

        # - Chunks Directory -
        # Check that the database exist
        if not is_file_exist(chunk_db_file):
            raise RAGError(
                "Chunk database doesn't exist.\nRun the index command first."
            )
        # Check that the file is not empty
        if os.path.getsize(chunk_db_file) == 0:
            raise RAGError("Chunk database is empty. Is everything ok?")

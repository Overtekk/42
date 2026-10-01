# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  RAGEngine.py                                      :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/29 14:12:52 by roandrie        #+#    #+#               #
#  Updated: 2026/09/09 14:35:20 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

from pathlib import Path
from typing import Any
from src.model.models import ChunkSearchResult, MinimalAnswer
from src.utils import (
    is_folder_exist,
    is_file_exist,
    check_perm_can_read,
    check_perm_can_write,
    print_log,
    print_with_color,
    func_timer,
)
from src.config import PathConfig, RAGConfig, RAGError
from src.indexer import indexer, utils
from src.retriever import RetrieverEngine
from src.answer import AnswerEngine
from src.recall import Recall


LIST_DIRECTORY: dict[str, str] = {
    "vllm_dir": PathConfig.DEFAULT_VLLM_DIRECTORY,
    "index_dir": PathConfig.INDEX_DIRECTORY,
    "bm25_dir": PathConfig.INDEX_BM25_DIRECTORY,
    "chunk_dir": PathConfig.INDEX_CHUNKS_DIRECTORY,
}


class RAGEngine:
    """Main orchestration entry point for indexing, searching, answering and
       evaluation.
    """

    @func_timer
    def index(self, max_chunk_size: int = 2000) -> None:
        """Index the raw vLLM corpus and build the search database.

        The method validates the chunk size, ensures the vLLM data is
        available,
        creates all required directories, and launches the indexing pipeline.

        Args:
            max_chunk_size: Maximum number of characters per chunk.

        Raises:
            ValueError: If the chunk size is invalid or the vLLM data cannot
            be used.
        """
        # - SECURITY -
        try:
            _check_value_range(
                max_chunk_size,
                RAGConfig.MIN_CHUNK_SIZE,
                RAGConfig.MAX_CHUNK_SIZE,
                "max chunk size",
            )
        except RAGError as e:
            raise ValueError(e)

        vLLM_directory: str = PathConfig.DEFAULT_VLLM_DIRECTORY

        # - SECURITY -
        # If vLLM zip or folder do not exist. Stop the program here.
        if not is_file_exist(PathConfig.VLLM_ZIP):
            if not is_folder_exist(vLLM_directory):
                raise ValueError(
                    "vLLM zip or folder not found. Download it first and then"
                    "re-run the program."
                )

        # If folder not found, extract the archive. Otherwise, use the existing
        # folder.
        elif not is_folder_exist(vLLM_directory):
            utils.extract_archive(PathConfig.VLLM_ZIP)
        else:
            if not check_perm_can_read(vLLM_directory):
                raise ValueError(
                    f"Error while trying to open {vLLM_directory}"
                )

        # Check that folders doesn't exist. If not, create them.
        for dir in LIST_DIRECTORY.values():
            _check_path(dir, True)

        # Launch the indexer
        print_log(
            f"Starting the indexing with chunk size of {max_chunk_size}\n",
            "yellow",
        )
        nb_chunks = indexer(vLLM_directory, max_chunk_size, LIST_DIRECTORY)

        print_with_color(
            f"\nIngestion complete! Indexed {nb_chunks} chunks in "
            f"'{PathConfig.INDEX_CHUNKS_DIRECTORY}'.\nIndices saved under "
            f"'{PathConfig.INDEX_BM25_DIRECTORY}'",
            "green",
        )

    @func_timer
    def search(
        self, query: str, k: int = 10, verbose: bool = True
    ) -> list[ChunkSearchResult] | None:
        """Search the indexed corpus for the best matching chunks.

        Args:
            query: User question to search for.
            k: Maximum number of chunks to retrieve.
            verbose: If true, print each chunk result to stdout.

        Returns:
            list[ChunkSearchResult]: Matching chunks ranked by relevance.
            Returns None when verbose output is enabled.

        Raises:
            ValueError: If the query is empty or the retrieval parameters are
            invalid.
        """
        # - SECURITY -
        try:
            _check_value_range(
                k,
                RAGConfig.MIN_K_CHUNKS,
                RAGConfig.MAX_K_CHUNKS,
                "number of results",
            )
        except RAGError as e:
            raise ValueError(e)
        if not query or not isinstance(query, str):
            raise ValueError("Please, provide a valid question.")

        # Init the retriever and retrieve the k best results
        try:
            retriever = RetrieverEngine(k, LIST_DIRECTORY)
            print_log(f"Searching the best {k} documents for '{query}'")
            result = retriever.retrieve(query)
        except RAGError as e:
            raise ValueError(e)

        print_log("✅ Done\n", "green")

        # Go throught the result and print the final results
        if verbose:
            result_msg = ""
            for index in result:
                result_msg += (
                    f"{index.file_path} [{index.first_character_index}:"
                    f"{index.last_character_index}]\n"
                )
            print(result_msg)
            return None
        return result

    @func_timer
    def search_dataset(
        self,
        dataset_path: str = PathConfig.DEFAULT_DATASET_PATH,
        k: int = 10,
        save_directory: str = PathConfig.DEFAULT_SAVE_DIRECTORY,
    ) -> None:
        """Run retrieval over every JSON dataset file in a directory.

        Args:
            dataset_path: Path to a file or directory containing dataset JSON
            files.
            k: Max number of chunks to keep per question.
            save_directory: Directory where student retrieval results are
            stored.

        Raises:
            ValueError: If the dataset path or configuration is invalid.
        """
        # - SECURITY -
        try:
            _check_value_range(
                k,
                RAGConfig.MIN_K_CHUNKS,
                RAGConfig.MAX_K_CHUNKS,
                "number of results",
            )
        except RAGError as e:
            raise ValueError(e)
        # Check path
        _check_path(save_directory, True)

        try:
            # Init the retriever
            retriever = RetrieverEngine(k, LIST_DIRECTORY)

            # Go throught the dataset path given
            path = Path(dataset_path)
            for file in (
                [path] if path.is_file() else list(path.rglob("*.json"))
            ):
                rag_dataset = retriever.create_dataset(file)
                if rag_dataset:
                    search_results = retriever.retrieve_dataset(rag_dataset)
                    retriever.save_retriever_result(
                        search_results, save_directory, file.name
                    )
        except RAGError as e:
            raise ValueError(e)

    @func_timer
    def answer(
        self, query: str, k: int = 10, context_limit: int = 3000
    ) -> None:
        """Generate a concise answer from the retrieved documents.

        Args:
            query: User question to answer.
            k: Number of source chunks to retrieve.
            context_limit: Maximum number of characters to include from
            retrieved sources.

        Raises:
            ValueError: If the prompt or retrieval configuration is invalid.
        """
        # - SECURITY -
        try:
            _check_value_range(
                k,
                RAGConfig.MIN_K_CHUNKS,
                RAGConfig.MAX_K_CHUNKS,
                "token budget",
            )
            _check_value_range(
                context_limit,
                RAGConfig.MIN_CONTEXT_LIMIT,
                RAGConfig.MAX_CONTEXT_LIMIT,
                "context limit",
            )
        except RAGError as e:
            raise ValueError(e)
        if not query or not isinstance(query, str):
            raise ValueError("Please, provide a valid question.")

        try:
            # Search the database for the provided query
            search_result = self.search(query, k, False)

            # Init the engine
            engine = AnswerEngine(context_limit)
            results = engine.answer(search_result, query)
            if not isinstance(results, MinimalAnswer):
                return

        except RAGError as e:
            raise ValueError(e)

        print_with_color("\nRAG: ", "bright_yellow")
        print_with_color(f"{results.answer}\n", "white")
        for source in results.retrieved_sources:
            print_with_color(f"{source.file_path}", "gray66")

    @func_timer
    def answer_dataset(
        self,
        student_search_results_path: str = (PathConfig.DEFAULT_SAVE_DIRECTORY),
        save_directory: str = PathConfig.DEFAULT_ANSWER_SAVE_DIRECTORY,
        context_limit: int = 3000,
    ) -> None:
        """Generate answers for every search result file in a dataset
           directory.

        Args:
            student_search_results_path: Directory or file containing retrieval
            outputs.
            save_directory: Directory where answer files are saved.
            context_limit: Maximum size of the prompt context passed to the
            model.

        Raises:
            ValueError: If the context limit is invalid.
        """
        # - SECURITY -
        try:
            _check_value_range(
                context_limit,
                RAGConfig.MIN_CONTEXT_LIMIT,
                RAGConfig.MAX_CONTEXT_LIMIT,
                "context limit",
            )
        except RAGError as e:
            raise ValueError(e)
        _check_path(save_directory, True)

        try:
            # Init the engine
            engine = AnswerEngine(context_limit)

            # Go throught the dataset path given
            path = Path(student_search_results_path)
            for file in (
                [path] if path.is_file() else list(path.rglob("*.json"))
            ):
                engine.answer_dataset(file, Path(save_directory))

        except RAGError as e:
            raise ValueError(e)

    @func_timer
    def evaluate(
        self,
        student_search_results_path: str = PathConfig.DEFAULT_SAVE_DIRECTORY,
        dataset_path: str = PathConfig.DEFAULT_DATASET_PATH,
    ) -> None:
        """Evaluate student retrieval recall against the reference dataset.

        Args:
            student_search_results_path: Directory or file containing student
            search outputs.
            dataset_path: Path to the reference JSON dataset.

        Raises:
            ValueError: If the evaluation dataset is invalid.
        """
        if (
            not Path(dataset_path).is_file()
            or Path(dataset_path).suffix != ".json"
            or not check_perm_can_read(dataset_path)
        ):
            raise ValueError(
                "Please provide a json file from 'data/datasets'."
            )
        else:
            dataset = Path(dataset_path)

        # Check paths
        try:
            # Init the recaller
            recaller = Recall(dataset)

            student_path = Path(student_search_results_path)
            for file in (
                [student_path]
                if student_path.is_file()
                else list(student_path.rglob("*.json"))
            ):
                recall_results = recaller.recall_file(file)
                recaller.print_recall_results(recall_results)

        except RAGError as e:
            raise ValueError(e)

    def execute_pipeline(self) -> None:
        """Run the default indexing and retrieval pipeline across the project
           datasets.
        """
        # 1. Index
        self.index()
        # 2. Search in the dataset
        self.search_dataset(
            "data/datasets/UnansweredQuestions/dataset_code_public.json",
            10,
            "data/output/search_results/UnansweredQuestions",
        )
        self.search_dataset(
            "data/datasets/UnansweredQuestions/dataset_docs_public.json",
            10,
            "data/output/search_results/UnansweredQuestions",
        )
        self.search_dataset(
            "data/datasets/AnsweredQuestions/dataset_code_public.json",
            10,
            "data/output/search_results/AnsweredQuestions",
        )
        self.search_dataset(
            "data/datasets/AnsweredQuestions/dataset_docs_public.json",
            10,
            "data/output/search_results/AnsweredQuestions",
        )


# :--------------------:
#   PRIVATES FUNCTIONS
# :--------------------:


def _check_path(raw_path: str, is_directory: bool = False) -> None:
    """Path checker for a file or a folder.

    Take the raw path of transform it to a 'Path' object. Create the folders
    parents if they do not exist, then the file or the path. If one of these
    already exist, check for the permission.

    Args:
        raw_path (str): raw path of the folder or file.
        is_directory (bool, optional): If is a folder. Defaults to False.

    Raises:
        ValueError: If an error occurred with permissions.
    """
    path = Path(raw_path)

    # Create the folders if they do not exist
    if path.parent:
        path.parent.mkdir(parents=True, exist_ok=True)

    if is_directory:
        if not is_folder_exist(path):
            path.mkdir()
        else:
            if not check_perm_can_read(path) and not check_perm_can_write(
                path
            ):
                raise ValueError(f"Permission error for {path}")

    else:
        if not is_file_exist(path):
            path.touch()

        else:
            if not check_perm_can_read(path) and not check_perm_can_write(
                path
            ):
                raise ValueError(f"Permission error for {path}")


def _check_value_range(
    variable: Any, min: int, max: int, type_name: str
) -> None:
    """Check the range value of the variable.

    Args:
        variable (Any): variable to check.
        min (int): minimal value range.
        max (int): max value range.
        type_name (str): name of the variable (for clear error message).

    Raises:
        RAGError: if the variable is not a integer.
        RAGError: if the variable is outside range.
    """
    if not _check_if_int(variable):
        raise RAGError(f"Provide a valid number for {type_name}.")

    if not min < variable <= max:
        raise RAGError(
            f"Provide a {type_name} superior to {min} and inferior to {max}"
        )


def _check_if_int(variable: Any) -> bool:
    """Check if the provided value is of type int.

    Args:
        variable (Any): the variable to check.

    Returns:
        bool: False if not an int. True otherwise.
    """
    try:
        int(variable)
    except ValueError:
        return False
    return True


def _get_datasets(path: str) -> dict[str, Path]:
    """Collect the relevant answered and unanswered dataset files.

    Args:
        path: Root directory containing the dataset groups.

    Returns:
        dict[str, Path]: Mapping of dataset labels to their JSON file paths.

    Raises:
        ValueError: If the dataset folder does not exist.
    """
    dataset_dict: dict[str, Path] = {}
    p_path = Path(path)

    if not is_folder_exist(p_path):
        raise ValueError("Datasets not found.")

    for folder in p_path.iterdir():
        if folder.name == "UnansweredQuestions":
            for file in folder.iterdir():
                if file.is_file() and file.suffix == ".json":
                    if file.name == "dataset_docs_public.json":
                        dataset_dict["Unanswered/Doc"] = file
                    elif file.name == "dataset_code_public.json":
                        dataset_dict["Unanswered/Code"] = file

        elif folder.name == "AnsweredQuestions":
            for file in folder.iterdir():
                if file.is_file() and file.suffix == ".json":
                    if file.name == "dataset_docs_public.json":
                        dataset_dict["Answered/Doc"] = file
                    elif file.name == "dataset_code_public.json":
                        dataset_dict["Answered/Code"] = file

    return dataset_dict

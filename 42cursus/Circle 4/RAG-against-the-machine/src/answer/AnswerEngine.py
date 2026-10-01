# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  AnswerEngine.py                                   :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/07/28 17:09:38 by roandrie        #+#    #+#               #
#  Updated: 2026/09/09 15:10:22 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import json
import uuid
from rich.console import Console
from pathlib import Path
from tqdm import tqdm
from transformers import pipeline
from src.model import (
    ChunkSearchResult,
    StudentSearchResults,
    MinimalAnswer,
    StudentSearchResultsAndAnswer,
)
from src.config import RAGError
from src.utils import print_log

MAX_NEW_TOKENS: int = 256
BATCH_SIZE: int = 4

console = Console()


class AnswerEngine:
    """Generate answer text from retrieved document chunks using an LLM
       pipeline.
    """

    def __init__(
        self, context_limit: int, llm_model: str = "Qwen/Qwen3-0.6B"
    ) -> None:
        """Initialize the answer engine and load the language model.

        Args:
            context_limit: Maximum number of characters to include in the
            prompt.
            llm_model: Hugging Face model identifier used for generation.
        """
        self._context_limit = context_limit
        self._llm_model = llm_model

        # Load the LLM
        self._load_llm()

    def answer(
        self,
        source: list[ChunkSearchResult],
        question: str,
        question_id: uuid.UUID | None = None,
    ) -> MinimalAnswer | str:
        """Generate a single answer from a list of retrieved chunks.

        Args:
            source: Retrieved source chunks.
            question: User question to answer.
            question_id: Optional question identifier.

        Returns:
            MinimalAnswer: Structured answer containing the question, sources
            and text.

        Raises:
            RAGError: If the source list is invalid.
        """
        if not source:
            return "Invalid source or empty source. Discarding..."

        # with console.status("[bold green]Generating answer..."):
        message = self._generate_prompt(source, question)
        raw_answer = self._generate_answer(message)
        if not raw_answer:
            "ERROR: Answer generation failed."

        # Clean the answer
        clean_answer = (
            raw_answer.replace("<think>", "").replace("</think>", "").strip()
        )

        answer_result: MinimalAnswer = MinimalAnswer(
            question_id=(
                str(uuid.uuid4()) if question_id is None else
                str(question_id)),
            question=question,
            retrieved_sources=source,
            answer=clean_answer,
        )

        return answer_result

    def answer_dataset(
        self, filepath: Path, save_dir: Path
    ) -> StudentSearchResultsAndAnswer:
        """Generate answers for an entire dataset and save the results.

        Args:
            filepath: Path to the JSON file containing search results.
            save_dir: Directory where the answered dataset is saved.

        Returns:
            StudentSearchResultsAndAnswer: Answered dataset payload.

        Raises:
            RAGError: If the input file is invalid.
        """
        search_result = self._create_dataset(filepath)
        items = search_result.search_results

        print_log(f"Loaded {len(search_result.search_results)} questions.")

        prompts = [
            self._generate_prompt(item.retrieved_sources, item.question)
            for item in items
        ]
        raw_answers = self._generate_batch_answers(prompts)

        list_answer: list[MinimalAnswer] = []
        for item, raw_answer in zip(items, raw_answers):
            clean_answer = (
                raw_answer.replace("<think>", "")
                .replace("</think>", "")
                .strip()
            )
            answer_result = MinimalAnswer(
                question_id=item.question_id,
                question=item.question,
                retrieved_sources=item.retrieved_sources,
                answer=clean_answer,
            )
            list_answer.append(answer_result)

        answered_dataset = StudentSearchResultsAndAnswer(
            search_results=list_answer, k=search_result.k
        )

        save_file_path = Path(save_dir) / filepath.name
        with open(save_file_path, "w", encoding="utf-8") as f:
            f.write(answered_dataset.model_dump_json(indent=4))

        print_log(f"Processed {len(list_answer)} questions.")
        print_log(
            f"Save student_search_results_and_answer to '{save_file_path}'."
        )

        return answered_dataset

    # :-----------------:
    #   PRIVATE METHODS
    # :-----------------:

    def _load_llm(self) -> None:
        """Load the text-generation pipeline used to produce answers."""
        print_log(f"Initializing LLM using '{self._llm_model}'", "gold1")

        # Load the model throught pipeline
        self._pipe = pipeline(
            task="text-generation",
            model=self._llm_model,
            device=0,
            clean_up_tokenization_spaces=False,
        )
        self._pipe.model.generation_config.max_new_tokens = MAX_NEW_TOKENS
        self._pipe.generation_config.max_length = None
        assert self._pipe.tokenizer is not None
        self._pipe.tokenizer.pad_token_id = self._pipe.tokenizer.eos_token_id
        self._pipe.tokenizer.padding_side = "left"

    def _generate_answer(self, message: list[dict[str, str]]) -> str:
        """Generate one answer from a formatted prompt.

        Args:
            message: Prompt payload sent to the model.

        Returns:
            str: Raw model output without the full text prefix.
        """
        output = self._pipe(message, return_full_text=False)
        return str(output[0]["generated_text"])

    def _generate_batch_answers(
        self, messages: list[list[dict[str, str]]]
    ) -> list[str]:
        """Generate answers for multiple prompts in batches.

        Args:
            messages: List of prompt messages for the model.

        Returns:
            list[str]: Generated answers in the same order as the input
            prompts.
        """
        outputs: list[str] = []
        for i in tqdm(
            range(0, len(messages), BATCH_SIZE), desc="Generate answers..."
        ):
            batch = messages[i: i + BATCH_SIZE]
            batch_results = self._pipe(
                batch, batch_size=BATCH_SIZE, return_full_text=False
            )
            for res in batch_results:
                text: str = str(res[0]["generated_text"])
                outputs.append(text)
        return outputs

    def _generate_prompt(
        self, sources: list[ChunkSearchResult], prompt: str
    ) -> list[dict[str, str]]:
        """Build the system and user prompt used to answer a question.

        Args:
            sources: Retrieved chunks used as evidence.
            prompt: User question.

        Returns:
            list[dict[str, str]]: Prompt payload formatted for the model.
        """
        # Preparing source formatting
        formatted_source = "\n".join(
            [str(source.content) for source in sources]
        )
        # Cut if text too long
        if len(formatted_source) > self._context_limit:
            formatted_source = formatted_source[: self._context_limit]

        # Prepare the prompt (/no_think prevent the model to using the <think>)
        return [
            {
                "role": "system",
                "content": (
                    "Answer the user's prompt using ONLY the provided"
                    "sources. Your answer will be concise but helpfull"
                    "for the user."
                    "The sources are: \n\n"
                    f"{formatted_source}"
                ),
            },
            {"role": "user", "content": f"User' prompt: '{prompt}'/no_think"},
        ]

    def _create_dataset(self, filepath: Path) -> StudentSearchResults:
        """Load and validate a dataset file into a Pydantic model.

        Args:
            filepath: JSON file containing search results.

        Returns:
            StudentSearchResults: Validated dataset.

        Raises:
            RAGError: If the input filepath is empty or invalid.
        """
        if filepath is None:
            raise RAGError("empty filepath.")

        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            dataset = StudentSearchResults.model_validate(data)
            return dataset

# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  models.py                                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/29 11:11:55 by roandrie        #+#    #+#               #
#  Updated: 2026/09/09 10:52:41 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import uuid

from pydantic import BaseModel, Field


class MinimalSource(BaseModel):
    """
    Model representing a minimal source of information.

    Attributes:
        file_path (str): Absolute or relative path to the source file.
        first_character_index (int): Index of the first character in the source
        last_character_index (int): Index of the last character in the source.
    """

    file_path: str
    first_character_index: int
    last_character_index: int


class ChunkSearchResult(MinimalSource):
    """
    Model representing a result of a chunk search that inherit from
    MinimalSource.

    Attributes:
        score (float): Score of the result.
        content (str): Content of the chunk.
    """

    score: float
    content: str


class UnansweredQuestion(BaseModel):
    """
    Model representing an unanswered question.

    Attributes:
        question_id (str): uuid of the question.
        question: raw question.
    """

    question_id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    question: str


class AnsweredQuestion(UnansweredQuestion):
    """
    Model representing an answered question.

    Attributes:
        sources (list): list of source information.
        answer: raw question.
    """

    sources: list[MinimalSource]
    answer: str


class RagDataset(BaseModel):
    """
    Model representing a dataset of RAG questions.

    Attributes:
        sources (list): list of answered or unanswered questions.
    """

    rag_questions: list[AnsweredQuestion | UnansweredQuestion]


class MinimalSearchResults(BaseModel):
    """
    Model representing the search result.

    Attributes:
        question_id (str): id of the question.
        question (str): raw question.
        retrieved_sources (list): list of source information.
    """

    question_id: str
    question: str
    retrieved_sources: list[ChunkSearchResult]


class MinimalAnswer(MinimalSearchResults):
    """
    Model representing the search answer.

    Attributes:
        answer (str): search answer string.
    """

    answer: str


class StudentSearchResults(BaseModel):
    """
    Model representing student search results.

    Attributes:
        search_results (list): list of search results.
        k (int): number of results requested.
    """

    search_results: list[MinimalSearchResults]
    k: int


class StudentSearchResultsAndAnswer(BaseModel):
    """
    Model representing student search results with answers.

    Attributes:
        search_results (list): list of answers results.
        k (int): Number of results requested.
    """

    search_results: list[MinimalAnswer]
    k: int

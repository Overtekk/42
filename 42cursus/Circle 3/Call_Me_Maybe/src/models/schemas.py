# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  schemas.py                                        :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/03/29 20:55:21 by roandrie        #+#    #+#               #
#  Updated: 2026/04/17 13:25:09 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Data models and schemas for the Call Me Maybe tool.

This module defines the Pydantic models used to enforce type safety and
structure for JSON data. It includes definitions for data types,
function signatures (definitions), and function calling prompts, ensuring
seamless integration with LLM structured outputs.
"""

from typing import Dict

from enum import Enum
from pydantic import BaseModel


class DataType(str, Enum):
    """
    Enumeration of supported JSON Schema data types.

    Maps common programming types to their JSON Schema equivalents used
    by most LLM function calling implementations.
    """
    NUMBER = "number"
    STRING = "string"
    INT = "integer"
    BOOL = "boolean"
    LIST = "array"
    DICT = "object"


class TypeInfo(BaseModel):
    """
    Wrapper for type information.

    Used to define the expected data type of a parameter or a return value
    in a structured way.

    Attributes:
        type (DataType): The specific data type allowed for this element.
    """
    type: DataType


class JsonFunctionCalling(BaseModel):
    """
    Schema for a function calling test prompt.

    Represents a single natural language input that the LLM will attempt
    to translate into a structured function call.

    Attributes:
        prompt (str): The natural language instruction to process.
    """
    prompt: str


class JsonFunctionDefinition(BaseModel):
    """
    Schema for a formal function definition.

    Provides the LLM with the necessary context (name, description, and
    signature) to understand how and when to call a specific function.

    Attributes:
        name (str): The identifier of the function.
        description (str): A clear explanation of what the function does.
        parameters (Dict[str, TypeInfo]): A mapping of parameter names to
                                          their respective type information.
        returns (TypeInfo): The expected return type of the function.
    """
    name: str
    description: str
    parameters: Dict[str, TypeInfo]
    returns: TypeInfo

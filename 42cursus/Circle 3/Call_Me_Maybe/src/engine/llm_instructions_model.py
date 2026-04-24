# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  llm_instructions_model.py                         :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/04 11:02:48 by roandrie        #+#    #+#               #
#  Updated: 2026/04/24 09:41:32 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
LLM Prompt Generation Module.

This module is responsible for constructing structured natural language prompts
to guide the Large Language Model (LLM) during the function calling process.
It formats the available functions and parameters to enforce constrained
generation for both function name selection and parameter extraction.
"""

from typing import List

from src.models import JsonFunctionDefinition


def get_name_instructions(func_def: List[JsonFunctionDefinition],
                          user_prompt: str) -> str:
    """
    Construct the prompt for function name selection.

    Generates a structured prompt that presents the LLM with a specific task,
    a list of available functions with their descriptions, a formatting model
    (few-shot prompting), and the user's natural language request.

    Args:
        func_def (List[JsonFunctionDefinition]): A list of available function
            definitions to include in the prompt.
        user_prompt (str): The natural language request from the user.

    Returns:
        str: The fully formatted prompt ready to be processed by the LLM.

    Raises:
        ValueError: If func_def is not a list or user_prompt is not a string.
    """
    if not isinstance(func_def, List):
        raise ValueError("function_definition is not a list.")
    if not isinstance(user_prompt, str):
        raise ValueError("user prompt is not a string.")

    # Instruction for the model
    task: str = ("Task: You are a function selector. Given a user request, "
                 "output the name of the best matching function.\n")

    # List of all functions available

    function_def_str: str = "Available functions:\n"
    for function in func_def:
        function_def_str += (
            f"- {function.name}: {function.description}\n"
        )

    # Model for the output
    example_func: JsonFunctionDefinition = func_def[0]
    example_output: str = (
        "Example:\n"
        f"User request: Use {example_func.name}.\n"
        f"The best matching function name is: {example_func.name}\n\n"
    )

    # User prompt
    user_formated_prompt: str = (
        f"User request: {user_prompt}.\n"
        "The best matching function name is: "
    )

    return (
        task + function_def_str + example_output + user_formated_prompt
    )


def get_param_instructions(func_def: JsonFunctionDefinition,
                           user_prompt: str) -> str:
    """
    Construct the prompt for function parameter extraction.

    Generates a structured prompt to guide the LLM in extracting the correct
    parameters for a specifically chosen function based on the user's request.
    It explicitly formats the expected parameters and their types.

    Args:
        func_def (JsonFunctionDefinition): The definition of the selected
            function, including its expected parameters.
        user_prompt (str): The natural language request from the user.

    Returns:
        str: The fully formatted prompt instructing the LLM to generate
        the function's parameters.

    Raises:
        ValueError: If func_def is not a JsonFunctionDefinition or user_prompt
                    is not a string.
    """
    if not isinstance(func_def, JsonFunctionDefinition):
        raise ValueError("function_definition not a JsonFunctionDefinition.")
    if not isinstance(user_prompt, str):
        raise ValueError("user prompt is not a string.")

    # Instruction for the model
    task: str = (
        "Task: You are a function selector. Given a user request, "
        "extract the explicit values from the user request to "
        "populate the parameters. Do NOT solve the problem or "
        "calculate the answer. Only extract the arguments."
    )

    func_str: str = f"{func_def.name}:\n"

    for func_param_name, type_info in func_def.parameters.items():
        func_str += f"{func_param_name} ({type_info.type.value})\n"

    user_formated_prompt: str = (
        f"User request: {user_prompt}.\nEnd each parameter with an new line."
    )

    return (
        task + func_str + user_formated_prompt
    )

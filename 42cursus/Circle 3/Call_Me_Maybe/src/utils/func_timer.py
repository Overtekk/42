# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  func_timer.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/04/21 13:32:36 by roandrie        #+#    #+#               #
#  Updated: 2026/04/22 11:18:22 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #
"""
Performance profiling utilities.

This module provides decorators and tools to measure and log
the execution time of specific functions or methods within the tool.
"""

from typing import Any, Callable

from functools import wraps
from time import perf_counter

from src.utils import print_log


def func_timer(f: Callable[..., Any]) -> Callable[..., Any]:
    """
    Decorator to measure and log the execution time of a function.

    Wraps the target function to calculate the exact time elapsed
    during its execution using a high-resolution performance counter.
    The duration is logged using the project's standard logger.

    Args:
        f (Callable): The function or method to be timed.

    Returns:
        Callable: The wrapped function, which executes the original
        function and returns its unmodified result.
    """
    @wraps(f)
    def wrap(*args: Any, **kwargs: Any) -> Any:
        time_start: float = perf_counter()
        func_result: Any = f(*args, **kwargs)
        time_end: float = perf_counter()

        execution_time: float = time_end - time_start
        minutes, seconds = divmod(execution_time, 60)

        print_log(
            f"\nAction took {int(minutes)} minutes, {seconds:.2f} seconds.\n"
        )

        return func_result
    return wrap

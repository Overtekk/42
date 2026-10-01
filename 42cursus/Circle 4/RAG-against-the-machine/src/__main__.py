# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  __main__.py                                       :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: roandrie <roandrie@student.42lehavre.fr   +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/06/19 19:27:46 by roandrie        #+#    #+#               #
#  Updated: 2026/09/09 11:38:47 by roandrie        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
import fire

from src.utils import print_error, print_with_color
from .RAGEngine import RAGEngine


def main() -> int:
    """Launch the CLI entry point for the RAG engine.

    Returns:
        int: 0 on success, 1 on a handled user-facing error.
    """
    try:
        print_with_color("\n📤 RAG joined the terminal\n", "bright_yellow")

        # Init the CLI with Python Fire by calling the RAGEngine class as
        # argument.
        fire.Fire(RAGEngine)

        print_with_color("\n📥 RAG left the terminal.", "bright_yellow")
        return 0

    except ValueError as e:
        print_error(e)
        print_with_color("\n📥 RAG left the terminal.", "bright_yellow")
        return 1

    except Exception as e:
        print_error(f"Critical error: {e}")
        print_with_color("\nRAG left the terminal.", "bright_yellow")
        return 1


if __name__ == "__main__":
    try:
        sys.exit(main())

    except KeyboardInterrupt:
        print_error("Program interrupted by the user. 😥\nGoodbye!")
        print_with_color("\n📥 RAG left the terminal.", "bright_yellow")
        sys.exit(130)

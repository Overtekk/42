import sys
import os


def not_in_venv() -> None:
    print("Should detect no virtual environment and provide instructions")


def main() -> None:

    # sys.base_prefix point to the base of the Python installation
    # and it can't change inside a virtual environment
    # sys.prefix point where the independent Python files are installed
    if sys.prefix != sys.base_prefix:
        print("test")

    not_in_venv()


if __name__ == "__main__":
    main()

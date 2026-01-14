import sys
import os


def not_in_venv() -> None:
    print("Should detect no virtual environment and provide instructions")


def in_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")

    python_path = os.system
    virtual_env = os.getcwd()
    env_path = os.system
    package_path = os.system

    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {virtual_env}")
    print(f"Environment Path: {env_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    print(f"Package installation path: {package_path}")


def main() -> None:

    # sys.base_prefix point to the base of the Python installation
    # and it can't change inside a virtual environment
    # sys.prefix point where the independent Python files are installed
    if sys.prefix != sys.base_prefix:
        in_venv()
        return

    not_in_venv()


if __name__ == "__main__":
    main()

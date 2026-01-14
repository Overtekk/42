import sys
import os
import site


# Get the path to the executable and the version
python_path = sys.executable
python_version = sys.version_info.minor


def not_in_venv() -> None:
    print("\nMATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {python_path}.{python_version}")
    print("Virtual Environment: None detected")

    print("\nWARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate   # On Windows")

    print("\nThen run this program again.")


def in_venv() -> None:
    print("\nMATRIX STATUS: Welcome to the construct\n")

    # Get all the path and cut before the last '/' to have the name's folder.
    virtual_env = os.path.basename(sys.prefix)
    env_path = sys.prefix

    # site.getsitepackages() returns a list of all global site-packages
    # directories. We select the first one [0], which is the standard location
    # where pip installs third-party libraries in this environment.
    package_path = site.getsitepackages()[0]

    print(f"Current Python: {python_path}")
    print(f"Virtual Environment: {virtual_env}")
    print(f"Environment Path: {env_path}")

    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting the global system.")

    print(f"\nPackage installation path: {package_path}")


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

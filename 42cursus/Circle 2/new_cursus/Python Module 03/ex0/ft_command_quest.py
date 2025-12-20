import sys


def ft_command_quest() -> None:
    """Processes and displays command line arguments provided by the user.

    === Arguments ===
        - No arguments requiered

    === Returns ===
        - None: This function only prints to stdout

    This function reads directly from 'sys.argv' to demonstre how argument
    works. There is 3 examples based on the number of arguments: no
    arguments, a single argument, or multiple arguments.
    """

    print("=== Command Quest ===")

    i = 1

    # === No argument ===

    if len(sys.argv) == 1:
        print("No arguments provided")
        print(f"Program name: {sys.argv[0]}")

    # === Only 1 argument ===

    elif len(sys.argv) == 2:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {len(sys.argv) - 1}")
        print(f"Argument 1: {sys.argv[1]}")

    # === Multiple arguments ===

    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"arguments received: {len(sys.argv) - 1}")
        for arg in sys.argv[1:]:
            print(f"Argument {i}: {arg}")
            i += 1

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()

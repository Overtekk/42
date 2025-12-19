import sys


def ft_command_quest() -> None:
    """Use arguments send by user to demonstrate how to use them"""

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

    # === Total argument ===

    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    ft_command_quest()

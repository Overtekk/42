def file_reader(filename: str) -> None:
    """
    Read and print the file passed in parameters.

    === Arguments ===
        - Filename in string format.

    === Return ===
        - None: only print to stdout.

    This function read the filename in parameters. If the file doesn't exist,
    the program return an error. Else, we read and print the content.
    """

    print(f"Accessing Storage Vault: {filename}")
    try:
        file = open(filename, "r", encoding='utf-8')

        print("Connection established...\n")
        content = file.read()

        print("RECOVERED DATA:")
        print(f"{content}")

        file.close()
        print("Data recovery complete. Storage unit disconnected.")

    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return None


def main() -> None:
    """
    Program entry point.
    """

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    file_reader('ancient_fragment.txt')


if __name__ == "__main__":
    main()

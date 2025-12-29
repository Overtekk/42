import os


def file_writer(filename: str) -> None:
    """
    Read the file passed in parameters and write on it.

    === Arguments ===
        - Filename in string format.

    === Return ===
        - None: only print to stdout.

    This function read the filename in parameters then write some stuff on it.
    If the file doesn't exist, the program return an error. Else, we
    read and print the content.
    """

    text = (
        "[ENTRY 001] New quantum algorithm discovered\n"
        "[ENTRY 002] Efficiency increased by 347%\n"
        "[ENTRY 003] Archived by Data Archivist trainee\n"
        ""
    )

    print(f"Initializing new storage unit: {filename}")

    file = open(filename, "w+", encoding='utf-8')

    file.write(text)
    print("Storage unit created successfully...\n")

    file.seek(0)
    content = file.read()
    print(f"{content}")

    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{filename}' ready for long-term preservation.")


def main() -> None:
    """
    Program entry point.
    """

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n")

    if os.path.exists('new_discovery.txt'):
        print("ERROR: File already exist. Replacing it...")
        os.remove('new_discovery.txt')
        print("File is now fresh to write on!\n")

    file_writer('new_discovery.txt')


if __name__ == "__main__":
    main()

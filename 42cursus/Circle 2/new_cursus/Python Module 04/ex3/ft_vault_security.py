def file_reader(filename: str) -> bool:
    """Read a file and return true or false if file is found.

    == ARGUMENTS ==
        - Filename in string format

    == RETURNS ==
        - Boolean

    Check if filename is correct and read or write on it with the 'with'
    statement. Return true if success, false if not.
    """

    if filename == "classified_data.txt":

        print("Initiating secure vault access...")

        with open(filename, "r", encoding='utf-8') as file:
            print("Vault connection established with failsafe protocols\n")
            print("SECURE EXTRACTION:")

            content = file.read()
            print(f"{content}")

            print("")
            return True

    elif filename == "security_protocols.txt":

        with open(filename, "w+", encoding='utf-8') as file:
            print("SECURE PRESERVATION:")

            entry = "[CLASSIFIED] New security protocols archived"

            file.write(entry)
            file.seek(0)

            content = file.read()
            print(f"{content}")

            print("Vault automatically sealed upon completion")

            print("")
            return True

    else:
        print(f"ERROR: {filename} not found. Run data generator first.\n")
        return False


def main() -> None:
    """
    Program entry point.
    Send file to the 'file_reader' function and return True or False if
    operations is completed.
    """

    is_file_1_open = False
    is_file_2_open = False

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")

    is_file_1_open = file_reader('classified_data.txt')
    is_file_2_open = file_reader('security_protocols.txt')

    if is_file_1_open is True and is_file_2_open is True:
        print("All vault operations completed with maximum security.")
    elif is_file_1_open is False and is_file_2_open is False:
        print("No vault find. Failed to complete.")
    else:
        print("Only one vault completed with maximum security.")


if __name__ == "__main__":
    main()

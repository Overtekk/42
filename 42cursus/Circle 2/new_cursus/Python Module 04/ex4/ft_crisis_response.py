def file_reader(filename: str) -> None:
    """Read a file and check errors.

    == ARGUMENTS ==
        - Filename in string format

    == RETURNS ===
        - None: This function only print to stdout

    This function check the filename in parameters and read it if everything is
    fine. If errors detected, send the appropriate message.
    """

    try:
        with open(filename, "r", encoding='utf-8') as file:

            try:
                content = file.read()
            except UnicodeDecodeError:
                print(f"CRISIS ALERT: Attempting access to '{filename}'")
                print("RESPONSE: Archive can't be read")
                print("STATUS: Crisis handled, system stable")
                return None

            print(f"ROUTINE ACCESS: Attempting access to '{filename}'")
            print(f"SUCCESS: Archive recovered - '{content}'")
            print("STATUS: Normal operations resumed")

    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        return None
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        return None
    except IsADirectoryError:
        print(f"CRISIS ALERT: Attempting access to '{filename}'")
        print("RESPONSE: Security protocols can't open folder")
        print("STATUS: Crisis handled, security maintained")
        return None


def main() -> None:
    """
    Program entry point.
    """

    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n")

    file_reader('lost_archive.txt')

    print("")
    file_reader('classified_vault.txt')

    print("")
    file_reader('standard_archive.txt')

    print("")
    file_reader('corrupted_archive.txt')

    print("")
    file_reader('folder')

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()

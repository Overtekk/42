def garden_operations(n: int, divisor=None, file=None, key=None) -> None:
    """
    Performs operations that may fail.
    This function DOES NOT catch errors, it lets them happen
    so they can be caught by the tester.
    """

    dictionary = {'name': 'Alice', 'age': 23}

    val = int(n)

    if divisor is not None:
        _ = val / divisor

    if file is not None:
        text = open(file, "r")
        text.close()

    if key is not None:
        _ = dictionary[key]


def test_error_types():
    """Function to test each type of error"""

    print("=== Garden Error Types Demo ===")

    # === Test 1: Value Error ===

    print("\nTesting ValueError...")
    try:
        garden_operations(n="abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")
    else:
        print("No error detected!")

    # === Test 2: ZeroDivisionError ===

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(n=10, divisor=0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")
    else:
        print("No error detected!")

    # === Test 3: FileNotFoundError ===

    file_name = "missing.txt"
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(n=10, divisor=5, file=file_name)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file '{file_name}'")
    else:
        print("No error detected!")

    # === Test 4: KeyError ===

    word_to_search = "_plant"
    print("\nTesting KeyError...")
    try:
        garden_operations(n=10, divisor=5, key=word_to_search)
    except KeyError:
        print(f"Caught KeyError: 'missing\\{word_to_search}'")
    else:
        print("No error detected!")

    # === Test 5: Multiple Errors ===

    print("\nTesting multiple errors together...")
    try:
        garden_operations(n=10, divisor=0)
    except (ValueError, ZeroDivisionError):
        print("Caught an error, but program continues!")
    else:
        print("No error detected!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()

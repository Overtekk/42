def check_temperature(temp_str: str) -> int | None:
    """Check the temperature and return it if it's valid.
    We put "#noqa: E722" after "except", since we can't use specific error
    type (not allowed on the subject), and flake8 doesn't like empty except"""

    try:
        temperature = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None
    else:
        if temperature < 0:
            print(f"Error: {temperature}°C is too cold for plants (min 0°C)")
            return None
        elif temperature > 40:
            print(f"Error: {temperature}°C is too hot for plants (max 40°C)")
            return None
        else:
            print(f"Temperature {temperature}°C is perfect for plants!")
            return temperature


def test_temperature_input() -> None:
    """Testing input for check_temperature()"""

    print("=== Garden Temperature Checker ===\n")

    input = (
        25,
        "abc",
        100,
        -50,
    )

    for data in input:
        print(f"Testing temperature: {data}")
        check_temperature(temp_str=data)
        print("")

    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()

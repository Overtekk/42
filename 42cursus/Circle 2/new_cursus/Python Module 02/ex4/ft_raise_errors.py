def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Checker function"""

    try:
        if plant_name is None:
            raise ValueError
    except ValueError:
        print("Error: Plant name cannot be empty!")
        return None

    try:
        if water_level > 10:
            raise ValueError
    except ValueError:
        print(f"Error: Water level {water_level} is too hight (max 10)")
        return None

    try:
        if water_level < 1:
            raise ValueError
    except ValueError:
        print(f"Error: Water level {water_level} is too low (min 1)")
        return None

    try:
        if sunlight_hours > 12:
            raise ValueError
    except ValueError:
        print(f"Error: Sunlight hours {sunlight_hours} is too hight (max 12)")
        return None

    try:
        if sunlight_hours < 2:
            raise ValueError
    except ValueError:
        print(f"Error: Sunlight hours {sunlight_hours} is too low (min 2)")
        return None

    print(f"Plant {plant_name} is healthy!")


def test_plant_check() -> None:
    """Function to demonstrates errors handling with good and bads values"""

    print("=== Garden Plant Health Checker ===")

    # === Test 1: Test with good values ===

    print("\nTesting good values...")
    check_plant_health(plant_name="tomato", water_level=3, sunlight_hours=5)

    # === Test 2: Test with empty plant name ===

    print("\nTesting empty plant name...")
    check_plant_health(plant_name=None, water_level=3, sunlight_hours=5)

    # === Test 3: Test with bad water level ===

    print("\nTesting bad water level...")
    check_plant_health(plant_name="tomato", water_level=15, sunlight_hours=5)
    check_plant_health(plant_name="tomato", water_level=0, sunlight_hours=5)

    # === Test 4: Test with bad sunlight hours ===

    print("\nTesting bad sunlight hours...")
    check_plant_health(plant_name="tomato", water_level=3, sunlight_hours=0)
    check_plant_health(plant_name="tomato", water_level=3, sunlight_hours=20)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_check()

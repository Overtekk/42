def water_plants(plant_list: list) -> None:
    """Water each plant and print a message if there is an error"""

    success = True

    print("Opening watering system")
    try:
        for plant in plant_list:
            print("Watering " + plant)
    except TypeError:
        success = False
        print(f"Error: Cannot water {plant} - invalid plant!")
    finally:
        print("Closing watering system (cleanup)")

    if success is True:
        print("Watering completed successfully!")

    print("\nCleanup always happens, even with errors!")


def test_watering_system() -> None:
    """Demonstrates error handling with two lists. One is good, the other
    have an error.
    """

    good_plant_list = ["tomato", "lettuce", "carrots"]
    bad_plant_list = ["tomato", None, "carrots"]

    print("=== Garden Watering System ===")

    # === Test 1: Testing with good plant list ===

    print("\nTesting normal watering...")
    water_plants(plant_list=good_plant_list)

    # === Test 2: Testing with bad plant list ===

    print("\nTesting with error...")
    water_plants(plant_list=bad_plant_list)


if __name__ == "__main__":
    test_watering_system()

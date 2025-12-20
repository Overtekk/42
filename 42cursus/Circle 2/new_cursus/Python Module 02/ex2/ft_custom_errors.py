# *==============================================*
# |            CUSTOM EXCEPTION CLASSES          |
# *==============================================*

class GardenError(Exception):
    """Basic error for garden problems.
    Inherits from the built-in 'Exception' class or one of its subclasses.
    """

    pass


class PlantError(GardenError):
    """Catch error with watering.
    Inherits from GardenErrors
    """

    pass


class WaterError(GardenError):
    """Catch error with watering.
    Inherits from GardenErrors
    """

    pass


# *==============================================*
# |       FUNCTION TO TEST CUSTOM ERRORS         |
# *==============================================*


def ft_custom_errors() -> None:
    """Demonstrate custom errors"""

    print("=== Custom Garden Errors Demo ===")

    # === Test 1: PlantError ===
    status = "wilting"
    print("\nTesting PlantError...")
    try:
        if status == "wilting":
            raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    else:
        print(f"Tomato plant is {status}!")

    # === Test 2: WaterError ===

    water_in_tank = 5
    print("\nTesting WaterError...")
    try:
        if water_in_tank < 10:
            raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught {e.__class__.__name__}: {e}")
    else:
        print("Tank is full!")

    # === Test 3: All errors ===

    print("\nTesting catching all garden errors...")

    try:
        if status == "wilting":
            raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    else:
        print(f"Tomato plant is {status}!")

    try:
        if water_in_tank < 10:
            raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    else:
        print("Tank is full!")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()

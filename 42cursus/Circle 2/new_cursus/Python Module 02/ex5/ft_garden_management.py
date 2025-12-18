# *==============================================*
# |            CUSTOM EXCEPTION CLASS            |
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


class WateredError(GardenError):
    """Catch error with last watering.
    Inherits from GardenErrors
    """

    pass


# *==============================================*
# |               PLANT CLASS                    |
# *==============================================*

class Plant():
    """Plant model with NAME"""

    def __init__(self, *, name: str, water_level: int,
                 sun_level: int, watered: bool) -> None:
        """Initialize plant"""

        self.name = name
        self.water_level = water_level
        self.sun_level = sun_level
        self.watered = watered


# *==============================================*
# |            GARDEN MANAGER CLASS              |
# *==============================================*


class GardenManager():
    """Main class that manage plants and check errors"""

    def __init__(self) -> None:
        """Initialize Manager"""

        self.garden = []

    def add_to_garden(self, *, plant: Plant) -> None:
        """Add plants to garden ONLY if name is correct"""

        try:
            if plant.name is None:
                raise ValueError
        except ValueError:
            print("Error adding plant: Plant name cannot be empty!")
        else:
            self.garden.append(plant)
            print(f"Added {plant.name} successfully")


    def water_plant(self) -> None:
        """Check if plant have been watered or not"""

        print("Watering plants...")
        print("Opening watering system")

        for plant in self.garden:
            try:
                if plant.watered is True:
                    raise WateredError
            except WateredError as e:
                print(f"Caught {e.__class__.__name__}: {plant.name} have "
                    "already been watered")
            else:
                print(f"Watering {plant.name} - success")
            finally:
                print("Closing watering system (cleanup)")


# *==============================================*
# |               MAIN FUNCTION                  |
# *==============================================*

def ft_garden_management() -> None:
    """Main function"""

    manager = GardenManager()

    plant_list = [
        Plant(name="tomato", water_level=5, sun_level=5, watered=False),
        Plant(name="lettuce", water_level=15, sun_level=3, watered=False),
        Plant(name=None, water_level=0, sun_level=8, watered=True),
        Plant(name="carrot", water_level=9, sun_level=18, watered=True)
    ]

    print("=== Garden Management System ===\n")

    # === Add plants to garden ===

    for plant in plant_list:
        manager.add_to_garden(plant=plant)

    # === Water plants in garden ===

    print("")
    manager.water_plant()


if __name__ == "__main__":
    ft_garden_management()
